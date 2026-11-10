"""Motore video 16:9 (1920x1080) per il notiziario in darija.

Uso:
  python3 engine/render16.py EPISODIO.py preview     -> prev/b<i>_<k>.jpg
  python3 engine/render16.py EPISODIO.py video OUT.mp4
  python3 engine/render16.py EPISODIO.py thumb OUT.jpg

EPISODIO.py definisce: AUDIO_DIR, BRAND, BLOCKS (lista di dict: text, chapter, src, items) e THUMB.
Tempi degli elementi: "at"/"until" = parola chiave del testo (tempo proporzionale ai caratteri) o numero in secondi.
"""
import importlib.util, json, math, os, subprocess, sys, wave
from multiprocessing import Pool
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from align import align, key_time

W, H, FPS = 1920, 1080, 30
CX = W // 2
FD = os.environ.get("FONTS", "/home/claude/fonts/")
RED = (206, 43, 55); GREEN = (0, 166, 81); MGREEN = (0, 98, 51); WHITE = (245, 245, 242)
GREY = (175, 175, 182); DIM = (95, 95, 102); GOLD = (236, 196, 96)
LEAD, TAIL, OUTRO = 0.45, 0.45, 3.0
_fc = {}


def font(name, size):
    k = (name, size)
    if k not in _fc:
        _fc[k] = ImageFont.truetype(FD + name + ".ttf", size, layout_engine=ImageFont.Layout.RAQM)
    return _fc[k]


def ease(x):
    x = min(1.0, max(0.0, x)); return 1 - (1 - x) ** 3


def ease_back(x):
    x = min(1.0, max(0.0, x)); c1 = 1.70158; c3 = c1 + 1
    return 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2


# ---------------- episodio ----------------
spec = importlib.util.spec_from_file_location("ep", sys.argv[1]); EP = importlib.util.module_from_spec(spec); spec.loader.exec_module(EP)
BLOCKS = EP.BLOCKS


def wav_read(p):
    with wave.open(p) as w:
        sr = w.getframerate(); x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
        if w.getnchannels() == 2: x = x.reshape(-1, 2).mean(1)
    return x, sr


AUD = []
for i, b in enumerate(BLOCKS):
    ap = os.path.join(EP.AUDIO_DIR, b["audio"])
    if not os.path.exists(ap):  # anteprima senza audio: silenzio stimato dal testo
        print("ATTENZIONE: manca", ap); AUD.append((np.zeros(int(24000 * len(b["text"]) / 16), np.float32), 24000)); continue
    x, sr = wav_read(ap)
    nz = np.where(np.abs(x) > 0.01)[0]
    if len(nz): x = x[max(0, nz[0] - int(0.05 * sr)): nz[-1] + int(0.15 * sr)]
    AUD.append((x, sr))
DUR = [len(x) / sr for x, sr in AUD]
ALN = [align(x, sr, b["text"]) for (x, sr), b in zip(AUD, BLOCKS)]  # tempi reali delle parole (pause della voce)
BLEN = [LEAD + d + TAIL + (OUTRO if i == len(BLOCKS) - 1 else 0) for i, d in enumerate(DUR)]
START = [sum(BLEN[:i]) for i in range(len(BLOCKS))]
TOTAL = sum(BLEN)
NFR = [int(round(l * FPS)) for l in BLEN]


def kt(i, key):
    """tempo locale (s dall'inizio del blocco) di una parola chiave o di un numero."""
    if key is None: return None
    if isinstance(key, (int, float)): return float(key)
    try:
        return LEAD + key_time(ALN[i], BLOCKS[i]["text"], key)
    except KeyError:
        raise KeyError(f"blocco {i}: '{key}' non trovato")


# ---------------- sfondo e header ----------------
def make_bg():
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    arr = np.zeros((H, W, 3), np.float32) + np.array([12, 14, 20], np.float32)
    arr += (yy / H)[..., None] * np.array([6, 6, 12], np.float32)
    rng = np.random.default_rng(3); arr += rng.normal(0, 1.1, (H, W, 1))
    img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).convert("RGBA")
    pat = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(pat); step = 150
    for cy in range(0, H + step, step):
        for cx in range(0, W + step, step):
            ox = cx + (step // 2 if (cy // step) % 2 else 0)
            d.arc((ox - 34, cy - 40, ox + 34, cy + 28), 150, 30, fill=(255, 255, 255, 9), width=2)
            d.line((ox - 30, cy - 3, ox - 30, cy + 46), fill=(255, 255, 255, 9), width=2)
            d.line((ox + 30, cy - 3, ox + 30, cy + 46), fill=(255, 255, 255, 9), width=2)
    img = Image.alpha_composite(img, pat)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0)); g = ImageDraw.Draw(glow)
    g.ellipse((-400, -400, 700, 500), fill=RED + (55,)); g.ellipse((W - 700, H - 500, W + 400, H + 400), fill=MGREEN + (60,))
    return Image.alpha_composite(img, glow.filter(ImageFilter.GaussianBlur(180)))


def arch(size, col=RED):
    S4 = size * 4; im = Image.new("RGBA", (S4, S4), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse((0, 0, S4 - 1, S4 - 1), fill=(22, 24, 30, 255)); k = S4 / 1080; w = int(42 * k)
    d.arc((230 * k, 215 * k, 850 * k, 835 * k), 180, 360, fill=col + (255,), width=w)
    for xx in (254, 826): d.line((xx * k, 520 * k, xx * k, 860 * k), fill=col + (255,), width=w)
    d.line((200 * k, 860 * k, 880 * k, 860 * k), fill=col + (255,), width=w)
    for k2, c in enumerate([(0, 146, 70), (244, 245, 240), (206, 43, 55)]):
        d.rectangle((420 * k + k2 * 80 * k, 600 * k, 480 * k + k2 * 80 * k, 760 * k), fill=c + (255,))
    return im.resize((size, size), Image.LANCZOS)


BG = make_bg()
LOGO = arch(84)


def header(i):
    hd = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(hd)
    hd.alpha_composite(LOGO, (W - 60 - 84, 36))
    d.text((W - 60 - 84 - 18, 78), EP.BRAND, font=font("Tajawal-Black", 40), fill=WHITE + (255,), anchor="rm")
    lab = BLOCKS[i].get("chapter", "")
    if lab:
        f = font("Tajawal-Bold", 30); tw = d.textlength(lab, font=f)
        d.rounded_rectangle([60, 48, 60 + tw + 52, 108], 30, fill=(255, 255, 255, 20))
        d.text((86 + tw / 2 + 0, 78), lab, font=f, fill=(255, 255, 255, 235), anchor="mm")
        for k, c in enumerate([(0, 146, 70), (244, 245, 240), (206, 43, 55)]):
            d.rectangle([86 + k * 30, 118, 86 + k * 30 + 26, 122], fill=c + (255,))
    src = BLOCKS[i].get("src", "")
    if src:
        d.text((CX, 1046), "المصدر: " + src, font=font("Tajawal-Medium", 24), fill=(120, 120, 128, 255), anchor="mm")
    return hd


# ---------------- sottotitoli ----------------
def caption_chunks(i):
    chunks, cur = [], []
    for w, a, b, _ in ALN[i]:
        if cur and (len(cur) >= 7 or len(" ".join(x[0] for x in cur + [(w,)])) > 46):
            chunks.append(cur); cur = []
        cur.append((w, LEAD + a, LEAD + b))
        if w[-1] in ".؟?!:،," and len(cur) >= 3:
            chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    return chunks


def draw_caption(img, chunks, t):
    cur = None
    for k, c in enumerate(chunks):
        end = chunks[k + 1][0][1] if k + 1 < len(chunks) else c[-1][2] + 0.3
        if c[0][1] - 0.05 <= t < end: cur = c
    if not cur: return
    f = font("Tajawal-ExtraBold", 54); d0 = ImageDraw.Draw(img)
    ws = [d0.textlength(w, font=f) for w, _, _ in cur]; sp = 18
    tot = sum(ws) + sp * (len(ws) - 1)
    lay = Image.new("RGBA", (W, 140), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([CX - tot / 2 - 34, 22, CX + tot / 2 + 34, 118], 26, fill=(0, 0, 0, 120))
    x = CX + tot / 2
    for (w, a, b), wd in zip(cur, ws):
        x -= wd
        if a <= t < b:
            d.rounded_rectangle([x - 8, 30, x + wd + 8, 110], 16, fill=RED + (255,))
        d.text((x + wd / 2, 70), w, font=f, fill=WHITE + (255,), anchor="mm")
        x -= sp
    img.alpha_composite(lay, (0, 900))


# ---------------- elementi grafici ----------------
def alpha(i, it, t, fade=0.3):
    t0 = kt(i, it.get("at", 0.0)) if it.get("at") is not None else LEAD
    if t < t0: return 0.0, t0
    a = ease((t - t0) / fade)
    t1 = kt(i, it.get("until"))
    if t1 is not None and t > t1: a *= max(0.0, 1 - (t - t1) / 0.25)
    return a, t0


def fit(d, txt, name, size, maxw, minsize=30):
    while size > minsize and d.textlength(txt, font=font(name, size)) > maxw: size -= 4
    return font(name, size)


def draw_items(lay, i, t):
    d = ImageDraw.Draw(lay)
    for it in BLOCKS[i]["items"]:
        a, t0 = alpha(i, it, t)
        if a <= 0.01: continue
        al = int(255 * a); k = it["k"]; lt = t - t0
        if k == "chapter":
            e = ease(lt / 0.5); dx = int(70 * (1 - e))
            d.text((CX + 60 + dx, 470), it["num"], font=font("Tajawal-Black", 300), fill=GREEN + (al,), anchor="lm")
            d.rectangle([CX + 20, 330, CX + 26, 610], fill=DIM + (al,))
            f = fit(d, it["title"], "Tajawal-Black", 96, 820)
            d.text((CX - 20 - dx, 470), it["title"], font=f, fill=WHITE + (al,), anchor="rm")
        elif k == "head":
            dy = int(22 * (1 - ease(lt / 0.35)))
            f = fit(d, it["text"], "Tajawal-Black", it.get("size", 84), 1640)
            d.text((W - 140, it.get("y", 200) + dy), it["text"], font=f, fill=WHITE + (al,), anchor="ra")
            if it.get("sub"):
                d.text((W - 144, it.get("y", 200) + dy + f.size + 18), it["sub"], font=font("Tajawal-Bold", 38), fill=GREY + (al,), anchor="ra")
        elif k == "big":
            s = 0.88 + 0.12 * ease_back(lt / 0.45)
            f = fit(d, it["text"], "Tajawal-Black", int(it.get("size", 220) * s), 1600)
            y = it.get("y", 500)
            d.text((it.get("x", CX), y), it["text"], font=f, fill=it.get("color", GOLD) + (al,), anchor="mm")
            if it.get("sub"):
                fs = fit(d, it["sub"], "Tajawal-Bold", 46, 1500)
                d.text((it.get("x", CX), y + it.get("size", 220) * 0.62), it["sub"], font=fs, fill=GREY + (al,), anchor="mm")
        elif k == "stats":
            n = len(it["stats"]); w = 1560 / n
            for j, (num, lab, key) in enumerate(it["stats"]):
                tj = kt(i, key) if key is not None else t0
                if t < tj: continue
                aj = int(al * ease((t - tj) / 0.3)); s = 0.85 + 0.15 * ease_back((t - tj) / 0.4)
                x = W - 180 - w * j - w / 2 + 20
                d.text((x, 470), num, font=font("Tajawal-Black", int(170 * s)), fill=GOLD + (aj,), anchor="mm")
                d.text((x, 600), lab, font=font("Tajawal-Bold", 46), fill=WHITE + (aj,), anchor="mm")
        elif k == "rows":
            y0, gap = it.get("y", 380), it.get("gap", 120)
            for j, r in enumerate(it["rows"]):
                tj = kt(i, r[2]) if len(r) > 2 and r[2] is not None else t0
                if t < tj: continue
                aj = int(al * ease((t - tj) / 0.3)); dx = int(30 * (1 - ease((t - tj) / 0.35)))
                y = y0 + j * gap
                fl = fit(d, r[0], "Tajawal-Bold", it.get("size", 52), 900)
                d.text((W - 220 - dx, y), r[0], font=fl, fill=WHITE + (aj,), anchor="rm")
                col = r[3] if len(r) > 3 else GREEN
                fv = fit(d, r[1], "Tajawal-Black", it.get("size", 52) + 8, 620)
                d.text((220 - dx, y), r[1], font=fv, fill=col + (aj,), anchor="lm")
                d.line([(220, y + gap / 2), (W - 220, y + gap / 2)], fill=(52, 52, 60, aj), width=2)
        elif k == "pills":
            f = font("Tajawal-ExtraBold", 50); gapx = 36
            ws = [d.textlength(p, font=f) + 80 for p, _ in it["pills"]]
            x = CX + (sum(ws) + gapx * (len(ws) - 1)) / 2; y = it.get("y", 640)
            for (p, key), wd in zip(it["pills"], ws):
                tj = kt(i, key) if key is not None else t0
                x1 = x - wd
                if t >= tj:
                    aj = int(al * ease((t - tj) / 0.3))
                    d.rounded_rectangle([x1, y - 46, x, y + 46], 46, fill=MGREEN + (int(aj * 0.9),))
                    d.text(((x + x1) / 2, y), p, font=f, fill=WHITE + (aj,), anchor="mm")
                x = x1 - gapx
        elif k == "text":
            f = fit(d, it["text"], it.get("font", "Tajawal-Bold"), it.get("size", 52), 1640)
            d.text((it.get("x", CX), it.get("y", 640)), it["text"], font=f, fill=it.get("color", WHITE) + (al,), anchor="mm")
        elif k == "warn":
            f = fit(d, it["text"], "Tajawal-Bold", 44, 1500); tw = d.textlength(it["text"], font=f); y = it.get("y", 790)
            d.rounded_rectangle([CX - tw / 2 - 44, y - 44, CX + tw / 2 + 44, y + 44], 44, fill=(92, 28, 32, int(al * 0.92)))
            d.text((CX, y), it["text"], font=f, fill=(255, 205, 200, al), anchor="mm")
        elif k == "cta":
            s = 0.85 + 0.15 * ease_back(lt / 0.5)
            lg = arch(int(150 * s)); lg.putalpha(lg.getchannel("A").point(lambda v: int(v * a)))
            lay.alpha_composite(lg, (int(CX - lg.width / 2), 300))
            d.text((CX, 560), it.get("text", "ابوني فالقناة"), font=font("Tajawal-Black", 120), fill=WHITE + (al,), anchor="mm")
            d.text((CX, 680), it.get("sub", ""), font=font("Tajawal-Bold", 46), fill=GREY + (al,), anchor="mm")


HDR = {}
CAPS = {}


def frame(i, n):
    t = n / FPS
    if i not in HDR: HDR[i] = header(i); CAPS[i] = caption_chunks(i)
    img = BG.copy()
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); draw_items(lay, i, t)
    fade = 1.0
    if n < 8: fade = n / 8
    end_o = BLEN[i] - (OUTRO if i == len(BLOCKS) - 1 else 0)
    if i < len(BLOCKS) - 1 and n > NFR[i] - 8: fade = max(0.0, (NFR[i] - 1 - n) / 8)
    if t > end_o: fade *= max(0.0, 1 - (t - end_o) / 0.4)
    if fade < 0.999: lay.putalpha(lay.getchannel("A").point(lambda v: int(v * fade)))
    img.alpha_composite(lay)
    if t > end_o:  # outro
        a2 = ease((t - end_o - 0.2) / 0.5)
        if a2 > 0:
            lg = arch(220); lg.putalpha(lg.getchannel("A").point(lambda v: int(v * a2)))
            img.alpha_composite(lg, (CX - 110, 330))
            ImageDraw.Draw(img).text((CX, 640), EP.BRAND, font=font("Tajawal-Black", 90), fill=WHITE + (int(255 * a2),), anchor="mm")
        return img.convert("RGB")
    img.alpha_composite(HDR[i]); draw_caption(img, CAPS[i], t)
    g = (START[i] + t) / TOTAL
    ImageDraw.Draw(img).rectangle([W - int(W * g), H - 7, W, H], fill=GREEN + (255,))
    return img.convert("RGB")


def render_block(i):
    os.makedirs("build", exist_ok=True); tmp = f"build/b{i}.tmp.mp4"
    p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", tmp], stdin=subprocess.PIPE)
    for n in range(NFR[i]): p.stdin.write(frame(i, n).tobytes())
    p.stdin.close(); p.wait(); os.replace(tmp, f"build/b{i}.mp4"); return i


# ---------------- audio ----------------
def build_audio(path):
    SR = 48000; N = int(TOTAL * SR) + SR; voice = np.zeros(N, np.float32)
    from scipy.signal import resample_poly
    for i, (x, sr) in enumerate(AUD):
        y = resample_poly(x, SR, sr).astype(np.float32) if sr != SR else x
        a = int((START[i] + LEAD) * SR); voice[a:a + len(y)] += y[:N - a]
    rng = np.random.default_rng(1); music = np.zeros(N, np.float32)
    beat = 60 / 84; bar = beat * 4
    chords = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]
    mid = lambda m: 440 * 2 ** ((m - 69) / 12)
    for b in range(int(TOTAL / bar) + 2):
        c = chords[b % 4]; a = int(b * bar * SR); L = int(bar * SR); seg = np.arange(L) / SR
        env = np.minimum(1, seg / 0.4) * np.exp(-seg * 0.35)
        tone = sum(np.sin(2 * np.pi * mid(m) * seg) + 0.3 * np.sin(4 * np.pi * mid(m) * seg) for m in c) + 0.6 * np.sin(2 * np.pi * mid(c[0] - 24) * seg)
        e = min(N, a + L)
        if e > a: music[a:e] += (tone * env)[:e - a] * 0.05
    for k in range(int(TOTAL / beat) + 2):
        a = int(k * beat * SR); L = int(0.25 * SR); seg = np.arange(L) / SR
        hit = np.sin(2 * np.pi * (50 + 80 * np.exp(-seg * 30)) * seg) * np.exp(-seg * 12) if k % 2 == 0 else rng.normal(0, 1, L) * np.exp(-seg * 25) * 0.3
        e = min(N, a + L)
        if e > a: music[a:e] += hit[:e - a] * 0.2
    env = np.convolve(np.abs(voice), np.ones(2400) / 2400, "same")
    duck = np.convolve(np.where(env > 0.008, 0.28, 1.0), np.ones(9600) / 9600, "same").astype(np.float32)
    music *= duck; f0 = int(0.4 * SR); music[:f0] *= np.linspace(0, 1, f0); music[-2 * SR:] *= np.linspace(1, 0, 2 * SR)
    sfx = np.zeros(N, np.float32)
    def whoosh(at):
        L = int(0.45 * SR); n = rng.normal(0, 1, L).astype(np.float32); y = np.zeros(L, np.float32); acc = 0.0
        for j in range(0, L):
            al = 0.02 + 0.45 * math.sin(math.pi * j / L); acc += al * (n[j] - acc); y[j] = acc
        y *= np.sin(np.pi * np.arange(L) / L) * 0.35; s = int(at * SR); e = min(N, s + L); sfx[s:e] += y[:e - s]
    def pop(at):
        L = int(0.12 * SR); seg = np.arange(L) / SR; y = np.sin(2 * np.pi * (900 - 500 * seg / 0.12) * seg) * np.exp(-seg * 40) * 0.25
        s = int(at * SR); e = min(N, s + L); sfx[s:e] += y[:e - s]
    for i, b in enumerate(BLOCKS):
        whoosh(max(0, START[i] - 0.15))
        for it in b["items"]:
            if it["k"] in ("big", "warn", "head"): pop(START[i] + (kt(i, it.get("at")) if it.get("at") is not None else LEAD))
    mix = voice + music * 0.9 + sfx
    mix = mix[: int(TOTAL * SR)]
    mix /= max(1e-6, np.abs(mix).max()) / 0.95
    pcm = (np.clip(mix, -1, 1) * 32767).astype(np.int16)
    with wave.open("build/mix_raw.wav", "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", "build/mix_raw.wav", "-af",
                    "highpass=f=60,acompressor=threshold=-20dB:ratio=2.5:attack=5:release=120,loudnorm=I=-14:TP=-1.5:LRA=9",
                    "-ar", "48000", "-ac", "2", path], check=True)


def chapters():
    out = []; last = None
    for i, b in enumerate(BLOCKS):
        c = b.get("chapter", "")
        if c != last:
            s = int(START[i]); out.append(f"{s // 60}:{s % 60:02d} {c}"); last = c
    return out


def thumb(path):
    T = EP.THUMB; im = BG.copy(); d = ImageDraw.Draw(im)
    im.alpha_composite(arch(150), (W - 210, 60))
    d.text((W - 230, 135), EP.BRAND, font=font("Tajawal-Black", 52), fill=WHITE + (255,), anchor="rm")
    y = 300
    for line in T["title"]:
        txt, col = line if isinstance(line, tuple) else (line, WHITE)
        f = fit(d, txt, "Tajawal-Black", 150, 980)
        d.text((W - 110, y), txt, font=f, fill=col + (255,), anchor="ra"); y += f.size + 30
    d.text((470, 520), T["num"], font=fit(d, T["num"], "Tajawal-Black", 260, 600), fill=GOLD + (255,), anchor="mm")
    d.text((470, 690), T["numsub"], font=font("Tajawal-Bold", 48), fill=GREY + (255,), anchor="mm")
    for k, c in enumerate([(0, 146, 70), (244, 245, 240), (206, 43, 55)]):
        d.rectangle([W - 110 - 3 * 70 + k * 70, 900, W - 110 - 3 * 70 + k * 70 + 62, 912], fill=c + (255,))
    d.text((W - 110, 960), T["bottom"], font=font("Tajawal-Bold", 46), fill=GREY + (255,), anchor="ra")
    im.convert("RGB").save(path, quality=92)


if __name__ == "__main__":
    cmd = sys.argv[2]
    os.makedirs("build", exist_ok=True); os.makedirs("prev", exist_ok=True)
    print("durate blocchi", [round(x, 1) for x in DUR], "totale", round(TOTAL, 1), "s")
    if cmd == "preview":
        sel = [int(x) for x in sys.argv[3:]] or range(len(BLOCKS))
        for i in sel:
            for k, fr in enumerate((0.18, 0.5, 0.85)):
                n = int((LEAD + DUR[i] * fr) * FPS); frame(i, n).save(f"prev/b{i}_{k}.jpg", quality=80)
    elif cmd == "video":
        out = sys.argv[3]
        with Pool(min(len(BLOCKS), os.cpu_count() or 4)) as p: p.map(render_block, range(len(BLOCKS)))
        build_audio("build/mix.wav")
        with open("build/list.txt", "w") as f:
            for i in range(len(BLOCKS)): f.write(f"file 'b{i}.mp4'\n")
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", "build/list.txt", "-c", "copy", "build/v.mp4"], check=True)
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", "build/v.mp4", "-i", "build/mix.wav", "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                        "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out], check=True)
        print("\n".join(chapters()))
    elif cmd == "thumb":
        thumb(sys.argv[3])
