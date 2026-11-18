"""Allineamento testo-voce.

align(): dal 18/11/2026 l'audio viene diviso in pezzi di 3-6 s tagliati sulle pause; ogni pezzo viene trascritto con
Whisper e ritrovato nel copione, così ogni pezzo è AGGANCIATO alle parole che la voce dice davvero (prima lo sfasamento
arrivava a 3-4 s nei blocchi lunghi). Dentro ogni pezzo si usa il metodo vecchio (align_pauses), descritto qui sotto.
Risultato in cache (~/.cache/darija_align). ALIGN_ASR=0 disattiva l'aggancio.

align_pauses(): senza riconoscimento vocale.

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


def align_pauses(x, sr, text):
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


# ---------------- aggancio con Whisper ----------------
import os, json, hashlib

_ASR = None
_TR = str.maketrans({"أ": "ا", "إ": "ا", "آ": "ا", "ى": "ي", "ة": "ه", "ؤ": "و", "ئ": "ي"})


def _asr():
    global _ASR
    if _ASR is None:
        import sherpa_onnx
        d = os.environ.get("WHISPER_DIR", "/home/claude/tts/sherpa-onnx-whisper-small/")
        _ASR = sherpa_onnx.OfflineRecognizer.from_whisper(encoder=d + "small-encoder.int8.onnx", decoder=d + "small-decoder.int8.onnx",
                                                          tokens=d + "small-tokens.txt", language="ar", task="transcribe", num_threads=2)
    return _ASR


def _norm_map(text):
    """testo normalizzato (senza harakat/segni, alef unificati) + indice nel testo originale per ogni carattere."""
    out, m = [], []
    for i, ch in enumerate(text):
        if re.match(r"[ً-ْٰـ]", ch): continue
        ch = ch.translate(_TR)
        if not re.match(r"[ء-ي0-9]", ch): ch = " "
        if ch == " " and out and out[-1] == " ": continue
        out.append(ch); m.append(i)
    return "".join(out), m


def _chunks(ps, t0, t1, lo=3.0, hi=6.0):
    cuts = [(a + b) / 2 for a, b in ps]; out = []; cur = t0
    while t1 - cur > hi:
        cand = [c for c in cuts if cur + lo <= c <= cur + hi]
        if not cand:  # nessuna pausa: taglia sulla pausa più vicina dopo cur+lo, al massimo cur+hi
            later = [c for c in cuts if c > cur + 1.5]
            nxt = min(later[0], cur + hi) if later else cur + hi
        else:
            nxt = max(cand) if t1 - max(cand) >= lo else min(cand)
        out.append((cur, nxt)); cur = nxt
    out.append((cur, t1))
    return out


def _resample16(x, sr):
    if sr == 16000: return x.astype(np.float32)
    from scipy.signal import resample_poly
    g = np.gcd(sr, 16000); return resample_poly(x, 16000 // g, sr // g).astype(np.float32)


def _boundaries(x, sr, text):
    from rapidfuzz import fuzz
    ps, t0, t1 = pauses(x, sr)
    ch = _chunks(ps, t0, t1)
    if len(ch) < 2: return []
    x16 = _resample16(x, sr); asr = _asr()
    tn, m = _norm_map(text)
    wstarts = [mm.start() for mm in re.finditer(r"\S+", text)]
    voiced = sum(b - a for a, b in _segments(ps, t0, t1)) or 1.0
    rate = len(tn) / voiced
    anc = []  # per pezzo: (inizio_norm, fine_norm, punteggio)
    prev = 0
    for a, b in ch:
        st = asr.create_stream(); st.accept_waveform(16000, x16[int(a * 16000): int(b * 16000)]); asr.decode_stream(st)
        hyp, _ = _norm_map(st.result.text); hyp = hyp.strip()
        exp_len = rate * (b - a)
        lo = max(0, prev - 60); hi = min(len(tn), prev + int(exp_len * 2) + 120)
        if len(hyp) >= 8 and hi > lo:
            r = fuzz.partial_ratio_alignment(hyp, tn[lo:hi])
            s0, s1 = lo + r.dest_start, lo + r.dest_end
            if r.score >= 55 and s0 >= prev - 40 and (s1 - s0) > 0.4 * len(hyp):
                anc.append((s0, s1, r.score)); prev = max(prev, s1); continue
        anc.append(None); prev = min(len(tn), prev + int(exp_len))
    # confini tra un pezzo e il successivo (posizione nel testo originale, all'inizio di una parola)
    bounds = []; last = 0
    for k in range(len(ch) - 1):
        e, s = anc[k], anc[k + 1]
        if e and s: p = (e[1] + s[0]) / 2
        elif e: p = e[1]
        elif s: p = s[0]
        else: bounds.append(None); continue
        po = m[min(int(round(p)), len(m) - 1)]
        w = min(wstarts, key=lambda q: abs(q - po))
        if w <= last: bounds.append(None); continue
        bounds.append(w); last = w
    # pezzi senza aggancio: si uniscono al vicino (togliendo il confine)
    out = []; cs = ch[0][0]
    for k in range(len(ch) - 1):
        if bounds[k] is None: continue
        out.append((ch[k][1], bounds[k]))
    return out  # [(tempo_taglio, posizione_carattere)]


def align(x, sr, text):
    text = text.replace("\n", " ")
    if os.environ.get("ALIGN_ASR", "1") == "0": return align_pauses(x, sr, text)
    key = hashlib.sha1(np.asarray(x, np.float32).tobytes() + text.encode() + str(sr).encode()).hexdigest()[:20]
    cdir = os.path.expanduser("~/.cache/darija_align"); os.makedirs(cdir, exist_ok=True); cf = os.path.join(cdir, key + ".json")
    if os.path.exists(cf):
        cuts = json.load(open(cf))
    else:
        try:
            cuts = _boundaries(x, sr, text)
        except Exception as e:  # niente Whisper: metodo vecchio
            print("align: aggancio Whisper non disponibile:", e); return align_pauses(x, sr, text)
        json.dump(cuts, open(cf, "w"))
    if not cuts: return align_pauses(x, sr, text)
    words = [(mm.group(0), mm.start()) for mm in re.finditer(r"\S+", text)]
    edges = [(0.0, 0)] + [tuple(c) for c in cuts] + [(len(x) / sr, len(text))]
    res = []
    for (ta, pa), (tb, pb) in zip(edges, edges[1:]):
        sub = [(w, p) for w, p in words if pa <= p < pb]
        if not sub: continue
        seg = x[int(ta * sr): int(tb * sr)]
        if len(seg) < sr * 0.2: seg = np.zeros(int(sr * 0.2), np.float32) + 1e-3
        base = sub[0][1]; st = text[base: pb].rstrip()
        for w, a, b, p in align_pauses(seg, sr, st):
            res.append((w, ta + a, ta + b, base + p))
    for k in range(1, len(res)):  # sicurezza: tempi sempre crescenti
        if res[k][1] <= res[k - 1][1]:
            w, a, b, p = res[k]; a = res[k - 1][1] + 0.02; res[k] = (w, a, max(b, a + 0.05), p)
    return res
