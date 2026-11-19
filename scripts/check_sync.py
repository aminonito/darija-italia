"""Controllo sincronizzazione sottotitoli-voce (da fare PRIMA della pubblicazione).

Per alcuni sottotitoli di ogni blocco (gli stessi gruppi di parole che render16/render_reel mostrano) trascrive con
Whisper l'audio nell'istante in cui il sottotitolo è a schermo, e anche spostato di ±0,5/1/1,5 s: se le parole del
sottotitolo si sentono meglio spostando, il sottotitolo è sfasato di quello spostamento.
Scarto positivo = il sottotitolo arriva DOPO la voce; negativo = arriva PRIMA.

Uso:
  python3 scripts/check_sync.py episodes/<file>.py            (video lungo, tutti i blocchi)
  python3 scripts/check_sync.py reels/<file>.json <R.wav>     (reel)
Esce con codice 1 se in un blocco lo scarto mediano supera 0,5 s o più di 1 punto su 4 supera 1 s (punti non riconosciuti ignorati).
"""
import sys, os, re, json, importlib.util, subprocess, statistics
import numpy as np, soundfile as sf, sherpa_onnx
from rapidfuzz import fuzz
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "engine"))
from align import align

D = '/home/claude/tts/sherpa-onnx-whisper-small/'
ASR = sherpa_onnx.OfflineRecognizer.from_whisper(encoder=D + 'small-encoder.int8.onnx', decoder=D + 'small-decoder.int8.onnx',
                                                 tokens=D + 'small-tokens.txt', language='ar', task='transcribe', num_threads=2)
MED_MAX, PT_MAX = 0.5, 1.0

TR = str.maketrans({"أ": "ا", "إ": "ا", "آ": "ا", "ى": "ي", "ة": "ه", "ؤ": "و", "ئ": "ي", "ـ": None})
def norm(s):
    s = re.sub(r"[ً-ْٰ]", "", s).translate(TR)
    return re.sub(r"[^ء-ي0-9 ]", " ", s)


def load(path):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-ac", "1", "-ar", "16000", "/tmp/cs16.wav"], check=True)
    x16, _ = sf.read("/tmp/cs16.wav"); x, sr = sf.read(path)
    if x.ndim == 2: x = x.mean(1)
    return x.astype(np.float32), sr, x16.astype(np.float32)


def trim(x, sr):  # stesso taglio di render16 (silenzio iniziale/finale)
    nz = np.where(np.abs(x) > 0.01)[0]
    if not len(nz): return x, 0.0
    a = max(0, nz[0] - int(0.05 * sr)); return x[a: nz[-1] + int(0.15 * sr)], a / sr


def chunks_of(al):
    """stessi gruppi di parole che render16 mostra a schermo."""
    chunks, cur = [], []
    for w, a, b, _ in al:
        if cur and (len(cur) >= 7 or len(" ".join(x[0] for x in cur + [(w,)])) > 46):
            chunks.append(cur); cur = []
        cur.append((w, a, b))
        if w[-1] in ".؟?!:،," and len(cur) >= 3:
            chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    return chunks


SHIFTS = [-4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0]


def heard(x16, a, b):
    a = max(0, int(a * 16000)); b = int(b * 16000)
    seg = x16[a:b]
    if len(seg) < 8000: return ""  # finestra oltre la fine dell'audio (segfault di sherpa con array vuoto)
    st = ASR.create_stream(); st.accept_waveform(16000, seg); ASR.decode_stream(st); return norm(st.result.text)


def check_block(name, wav, text, trim_like_render=True, n=None):
    x, sr, x16 = load(wav)
    off = 0.0
    if trim_like_render: x, off = trim(x, sr)
    al = align(x, sr, text); ch = [c for c in chunks_of(al) if len(c) >= 3]
    dur = len(x) / sr; n = n or (6 if dur > 120 else 4)
    pick = [ch[int((k + 0.5) * len(ch) / n)] for k in range(min(n, len(ch)))]
    res = []; miss = 0
    for c in pick:
        ca, cb = c[0][1], c[-1][2]; ref = norm(" ".join(w for w, _, _ in c))
        def score(sh):  # una trascrizione cortissima (es. una sola parola) dà partial_ratio 100 per caso: la si pesa con ratio
            h = heard(x16, ca + sh + off - 0.1, cb + sh + off + 0.1)
            return fuzz.partial_ratio(ref, h) if len(h) >= 0.5 * len(ref) else fuzz.ratio(ref, h)
        sc = {sh: score(sh) for sh in SHIFTS}
        b0 = max(sc, key=sc.get)
        for sh in (b0 - 0.5, b0 + 0.5): sc[sh] = score(sh)
        b0 = max(sc, key=sc.get); best = sc[b0]
        if best < 55: miss += 1; continue  # Whisper non ritrova il sottotitolo vicino alla voce
        lag = 0.0 if sc[0.0] >= best - 5 else -b0  # positivo = il sottotitolo arriva DOPO la voce
        res.append((ca, lag, best))
    if len(res) < max(2, len(pick) // 2):
        print(f"DA CONTROLLARE {name}: solo {len(res)} sottotitoli su {len(pick)} ritrovati nella voce (sfasamento grande o voce sbagliata)"); return False
    lags = [r[1] for r in res]; med = statistics.median(lags); bad = [l for l in lags if abs(l) > PT_MAX]
    ok = abs(med) <= MED_MAX and len(bad) <= len(lags) // 4
    print(f"{'ok ' if ok else 'FUORI SYNC '}{name}: {dur:.0f}s, {len(res)}/{len(pick)} sottotitoli ritrovati, scarto mediano {med:+.1f}s, oltre {PT_MAX}s: {len(bad)}")
    print("    " + "  ".join(f"{int(tt//60)}:{int(tt%60):02d} {lg:+.1f}" for tt, lg, _ in res))
    return ok


def main():
    src = sys.argv[1]; ok = True
    if src.endswith(".json"):
        R = json.load(open(src)); text = " ".join(s["text"] for s in R["scenes"]) if "scenes" in R else R["text"]
        ok = check_block(os.path.basename(src), sys.argv[2], text)
    else:
        spec = importlib.util.spec_from_file_location("ep", src); EP = importlib.util.module_from_spec(spec); spec.loader.exec_module(EP)
        only = set(sys.argv[2:])
        for i, b in enumerate(EP.BLOCKS):
            if only and b["audio"].split(".")[0] not in only: continue
            ok &= check_block(f"blocco {i+1} ({b['audio']})", os.path.join(EP.AUDIO_DIR, b["audio"]), b["text"])
    print("SINCRONIZZAZIONE OK" if ok else "SINCRONIZZAZIONE DA CORREGGERE")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
