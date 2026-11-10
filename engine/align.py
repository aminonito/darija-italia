"""Allineamento testo-voce senza riconoscimento vocale.

Le parole si distribuiscono SOLO sul tempo in cui la voce parla (le pause vengono saltate), in proporzione
ai caratteri; l'inizio di ogni frase (dopo la punteggiatura) viene agganciato alla ripresa della voce
dopo la pausa reale più vicina. Nessuna parola cade nel silenzio.
Ritorna [(parola, inizio, fine, posizione_carattere)] in secondi dall'inizio dell'audio.
"""
import re
import numpy as np

PUNCT = ".،,؟?!:;"


def pauses(x, sr, thr_db=-36, min_len=0.12):
    hop = int(sr * 0.01); n = len(x) // hop
    if n == 0: return [], 0.0, 0.0
    e = np.sqrt(np.mean(x[:n * hop].reshape(n, hop) ** 2, axis=1) + 1e-12)
    db = 20 * np.log10(e / (e.max() + 1e-12)); sil = db < thr_db
    out = []; i = 0
    while i < n:
        if sil[i]:
            j = i
            while j < n and sil[j]: j += 1
            if (j - i) * 0.01 >= min_len: out.append((i * 0.01, j * 0.01))
            i = j
        else: i += 1
    voiced = np.where(~sil)[0]
    t0 = voiced[0] * 0.01 if len(voiced) else 0.0
    t1 = (voiced[-1] + 1) * 0.01 if len(voiced) else n * 0.01
    return [p for p in out if p[0] > t0 and p[1] < t1], t0, t1


def _segments(ps, t0, t1):
    segs = []; cur = t0
    for a, b in ps:
        if a > cur: segs.append((cur, a))
        cur = b
    if t1 > cur: segs.append((cur, t1))
    return segs


def _f2t(segs, f, start=True):
    tot = sum(b - a for a, b in segs) or 1e-6; target = f * tot; acc = 0.0
    for idx, (a, b) in enumerate(segs):
        d = b - a
        if acc + d >= target - 1e-9:
            t = a + (target - acc)
            if start and abs(t - b) < 1e-6 and idx + 1 < len(segs): return segs[idx + 1][0]
            return t
        acc += d
    return segs[-1][1]


def align(x, sr, text):
    text = text.replace("\n", " ")
    ps, t0, t1 = pauses(x, sr)
    words = [(m.group(0), m.start()) for m in re.finditer(r"\S+", text)]
    if not words: return []
    segs = _segments(ps, t0, t1)
    W = [len(w) + 1 for w, _ in words]; tot = sum(W); cum = np.cumsum([0] + W) / tot
    starts = [_f2t(segs, cum[k]) for k in range(len(words))]
    ends = [_f2t(segs, cum[k + 1], start=False) for k in range(len(words))]
    seg_starts = [a for a, b in segs]
    for k in range(1, len(words)):
        if words[k - 1][0][-1] in PUNCT:
            near = min(seg_starts, key=lambda s: abs(s - starts[k]))
            if abs(near - starts[k]) <= 0.8 and near > starts[k - 1]:
                starts[k] = near
    for k in range(1, len(words)):
        starts[k] = max(starts[k], starts[k - 1] + 0.02)
    for k in range(len(words)):
        if k + 1 < len(words): ends[k] = min(max(ends[k], starts[k] + 0.05), starts[k + 1])
        else: ends[k] = max(ends[k], starts[k] + 0.05)
    return [(w, starts[k], ends[k], pos) for k, (w, pos) in enumerate(words)]


def key_time(aligned, text, key):
    """inizio (s) della parola dove inizia la PRIMA occorrenza di key nel testo."""
    pos = text.replace("\n", " ").find(key)
    if pos < 0: raise KeyError(key)
    best = aligned[0]
    for w in aligned:
        if w[3] <= pos: best = w
        else: break
    return best[1]
