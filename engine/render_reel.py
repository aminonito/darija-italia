"""Reel 9:16 (1080x1920) in darija: un solo audio, scene temporizzate in proporzione al testo.

Uso: python3 engine/render_reel.py reels/reel-NN.json AUDIO.wav OUT.mp4 [t1 t2 ...]   (con tempi = solo fotogrammi di prova)
"""
import json, math, os, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from align import align, key_time
import visuals as V

W, H, FPS = 1080, 1920, 30
FD = os.environ.get("FONTS", "/home/claude/fonts/")
RED = (206, 43, 55); MGREEN = (0, 98, 51); GREEN = (0, 166, 81); WHITE = (245, 245, 242); GREY = (200, 200, 205); GOLD = (236, 196, 96)
BRAND = "مغاربة إيطاليا"
LEAD, TAIL = 0.25, 0.6
_fc = {}


def font(n, s):
    if (n, s) not in _fc: _fc[(n, s)] = ImageFont.truetype(FD + n + ".ttf", s, layout_engine=ImageFont.Layout.RAQM)
    return _fc[(n, s)]


def ease(x): x = min(1, max(0, x)); return 1 - (1 - x) ** 3
def ease_back(x):
    x = min(1, max(0, x)); c1 = 1.70158; c3 = c1 + 1; return 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2


R = json.load(open(sys.argv[1], encoding="utf-8")); S = R["scenes"]; BRAND = R.get("brand", BRAND)
with wave.open(sys.argv[2]) as w:
    sr = w.getframerate(); X = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
nz = np.where(np.abs(X) > 0.01)[0]; X = X[max(0, nz[0] - int(.05 * sr)): nz[-1] + int(.15 * sr)]
VD = len(X) / sr; TOTAL = LEAD + VD + TAIL
FULL = " ".join(s["text"] for s in S)
ALN = align(X, sr, FULL)
OFF = []; acc = 0
for s_ in S: OFF.append(acc); acc += len(s_["text"]) + 1
def scene_of(pos): return max(k for k in range(len(S)) if OFF[k] <= pos)
STARTS = []
for k in range(len(S)):
    first = [w for w in ALN if w[3] >= OFF[k]]
    STARTS.append(LEAD + (first[0][1] if first else 0.0))
NH = sum(1 for s in S if s["hook"])
WORDS = [(w, LEAD + a, LEAD + b, scene_of(pos)) for w, a, b, pos in ALN]
CH = []; cur = []
for w in WORDS:
    if cur and (len(cur) >= 3 or w[3] != cur[-1][3]): CH.append(cur); cur = []
    cur.append(w)
    if w[0][-1] in ".،,؟?:" : CH.append(cur); cur = []
if cur: CH.append(cur)


def bg():
    y = np.linspace(0, 1, H)[:, None]; x = np.linspace(0, 1, W)[None, :]
    arr = np.dstack([12 + 10 * y + 0 * x, 14 + 8 * y + 0 * x, 20 + 16 * y + 0 * x])
    im = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).convert("RGBA")
    pat = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(pat); st = 150
    for cy in range(0, H + st, st):
        for cx in range(0, W + st, st):
            ox = cx + (st // 2 if (cy // st) % 2 else 0)
            d.arc((ox - 34, cy - 40, ox + 34, cy + 28), 180, 360, fill=(255, 255, 255, 11), width=2)
            d.line((ox - 34, cy - 6, ox - 34, cy + 46), fill=(255, 255, 255, 11), width=2)
            d.line((ox + 34, cy - 6, ox + 34, cy + 46), fill=(255, 255, 255, 11), width=2)
    im = Image.alpha_composite(im, pat)
    g = Image.new("RGBA", (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(g)
    gd.ellipse((-400, -300, 600, 700), fill=RED + (70,)); gd.ellipse((W - 600, H - 900, W + 400, H + 100), fill=MGREEN + (75,))
    return Image.alpha_composite(im, g.filter(ImageFilter.GaussianBlur(170)))


def arch(size):
    S4 = size * 4; im = Image.new("RGBA", (S4, S4), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse((0, 0, S4 - 1, S4 - 1), fill=(22, 24, 30, 255)); k = S4 / 1080; w = int(42 * k)
    d.arc((230 * k, 215 * k, 850 * k, 835 * k), 180, 360, fill=RED + (255,), width=w)
    for xx in (254, 826): d.line((xx * k, 520 * k, xx * k, 860 * k), fill=RED + (255,), width=w)
    d.line((200 * k, 860 * k, 880 * k, 860 * k), fill=RED + (255,), width=w)
    for k2, c in enumerate([(0, 146, 70), (244, 245, 240), (206, 43, 55)]):
        d.rectangle((420 * k + k2 * 80 * k, 600 * k, 480 * k + k2 * 80 * k, 760 * k), fill=c + (255,))
    return im.resize((size, size), Image.LANCZOS)


BG = bg()
HDR = Image.new("RGBA", (W, 200), (0, 0, 0, 0)); hd = ImageDraw.Draw(HDR)
HDR.alpha_composite(arch(96), (W - 56 - 96, 60))
hd.text((W - 56 - 96 - 20, 108), BRAND, font=font("Tajawal-Black", 44), fill=WHITE + (255,), anchor="rm")


def fit(d, t, n, s, mw):
    while s > 30 and d.textlength(t, font=font(n, s)) > mw: s -= 6
    return font(n, s)


def frame(t):
    i = max([k for k in range(len(S)) if STARTS[k] - 0.1 <= t] or [0]); lt = t - STARTS[i]; s = S[i]
    z = 1 + 0.05 * t / TOTAL
    bw, bh = int(W / z), int(H / z); ox = (W - bw) // 2 + int(14 * math.sin(t * 0.4)); oy = (H - bh) // 2
    img = BG.crop((ox, oy, ox + bw, oy + bh)).resize((W, H), Image.BILINEAR)
    img.alpha_composite(HDR, (0, 0)); pb = Image.new("RGBA", (W, 260), (0, 0, 0, 0)); d = ImageDraw.Draw(pb)
    # barra progresso a segmenti (RTL)
    sw = (W - 112 - (NH - 1) * 10) / NH
    for k in range(NH):
        x2 = W - 56 - k * (sw + 10); x1 = x2 - sw
        d.rounded_rectangle((x1, 230, x2, 240), 5, fill=(255, 255, 255, 60))
        fr = 1 if k < i else (min(1, max(0, lt / ((STARTS[k + 1] if k + 1 < len(S) else TOTAL) - STARTS[k]))) if k == i else 0)
        if fr > 0: d.rounded_rectangle((x2 - sw * fr, 230, x2, 240), 5, fill=WHITE + (255,))
    img.alpha_composite(pb, (0, 0)); d = ImageDraw.Draw(img)
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); L = ImageDraw.Draw(lay)
    p = ease_back(lt / 0.4)
    if s["hook"]:
        f = font("Tajawal-ExtraBold", 58); tw = L.textlength(s["hook"], font=f); num = f"{i + 1}/{NH}"; fn = font("Tajawal-Bold", 42); nw = L.textlength(num, font=fn)
        wtot = tw + nw + 100; x0 = W / 2 - wtot / 2; y = 400
        L.rounded_rectangle((x0, y - 62, x0 + wtot, y + 62), 62, fill=RED + (255,))
        L.rounded_rectangle((x0 + wtot - nw - 46, y - 52, x0 + wtot - 10, y + 52), 52, fill=(0, 0, 0, 80))
        L.text((x0 + wtot - nw / 2 - 28, y), num, font=fn, fill=WHITE + (230,), anchor="mm")
        L.text((x0 + (wtot - nw - 46) / 2 + 10, y + 2), s["hook"], font=f, fill=WHITE + (255,), anchor="mm")
    if s.get("v"):  # modello grafico (mappa, personaggi, icone, barre, calendario, confronto, passi)
        V.draw(lay, tuple(s["v"].get("box", (60, 480, 1020, 1250))), s["v"], lt)
        if s.get("sub"):
            a = int(255 * ease((lt - 0.25) / 0.4)); fs = fit(L, s["sub"], "Tajawal-Bold", 56, 960)
            L.text((W / 2, 1300), s["sub"], font=fs, fill=GREY + (a,), anchor="mm")
        img.alpha_composite(lay); return finish(img, d, t, i, s)
    big = s.get("big", ""); core = big.replace("+", "").replace("€", "").strip()
    if core.isdigit():
        n = int(core); v = int(round(n * ease(lt / 0.9))); txt = big.replace(core, str(v))
        fb = font("Tajawal-Black", 330); col = GOLD
    else:
        txt = big; fb = fit(L, big, "Tajawal-Black", 250, 940); col = WHITE
    lay2 = Image.new("RGBA", (W, 520), (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay2)
    d2.text((W / 2 + 6, 266), txt, font=fb, fill=(0, 0, 0, 150), anchor="mm"); d2.text((W / 2, 260), txt, font=fb, fill=col + (255,), anchor="mm")
    sc = max(0.01, 0.7 + 0.3 * p); lay2 = lay2.resize((int(W * sc), int(520 * sc)), Image.LANCZOS)
    lay.alpha_composite(lay2, (int(W / 2 - lay2.width / 2), int(780 - lay2.height / 2)))
    if s.get("sub"):
        a = int(255 * ease((lt - 0.25) / 0.4)); fs = fit(L, s["sub"], "Tajawal-Bold", 60, 960)
        L.text((W / 2, 1080), s["sub"], font=fs, fill=GREY + (a,), anchor="mm")
    img.alpha_composite(lay)
    return finish(img, d, t, i, s)


def finish(img, d, t, i, s):
    # sottotitoli
    for c in CH:
        if c[0][1] - 0.05 <= t < c[-1][2] + 0.08:
            fz = 80
            while True:  # riduce il font se la riga supera il bordo
                f = font("Tajawal-ExtraBold", fz); ws = [d.textlength(w[0], font=f) for w in c]; sp = 22
                totw = sum(ws) + sp * (len(ws) - 1)
                if totw <= 980 or fz <= 50: break
                fz -= 4
            x = W / 2 + totw / 2
            for (w, a, b, _), wd in zip(c, ws):
                x -= wd
                if a <= t < b + 0.05: d.rounded_rectangle((x - 10, 1360, x + wd + 10, 1490), 22, fill=RED + (255,))
                d.text((x + wd / 2, 1425), w, font=f, fill=WHITE + (255,), anchor="mm", stroke_width=4, stroke_fill=(0, 0, 0))
                x -= sp
            break
    src = s.get("src", R.get("src_default", ""))
    if src and s["hook"]:
        d.text((W / 2, 1700), "المصدر: " + src, font=font("Tajawal-Medium", 34), fill=(190, 190, 196, 255), anchor="mm")
    return img.convert("RGB")


def audio(path):
    SR = 48000; N = int(TOTAL * SR)
    from scipy.signal import resample_poly
    y = resample_poly(X, SR, sr).astype(np.float32); v = np.zeros(N, np.float32); a = int(LEAD * SR); v[a:a + len(y)] += y[:N - a]
    rng = np.random.default_rng(2); m = np.zeros(N, np.float32); beat = 60 / 92; bar = beat * 4
    ch = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]; mid = lambda q: 440 * 2 ** ((q - 69) / 12)
    for b in range(int(TOTAL / bar) + 2):
        a = int(b * bar * SR); L = int(bar * SR); seg = np.arange(L) / SR; e = min(N, a + L)
        if e <= a: continue
        tone = sum(np.sin(2 * np.pi * mid(q) * seg) for q in ch[b % 4]) + 0.6 * np.sin(2 * np.pi * mid(ch[b % 4][0] - 24) * seg)
        m[a:e] += (tone * np.minimum(1, seg / .4) * np.exp(-seg * .35))[:e - a] * 0.05
    for k in range(int(TOTAL / beat) + 2):
        a = int(k * beat * SR); L = int(.25 * SR); seg = np.arange(L) / SR; e = min(N, a + L)
        if e <= a: continue
        hit = np.sin(2 * np.pi * (50 + 80 * np.exp(-seg * 30)) * seg) * np.exp(-seg * 12) if k % 2 == 0 else rng.normal(0, 1, L) * np.exp(-seg * 25) * .3
        m[a:e] += hit[:e - a] * .22
    env = np.convolve(np.abs(v), np.ones(2400) / 2400, "same")
    m *= np.convolve(np.where(env > .008, .3, 1.), np.ones(9600) / 9600, "same").astype(np.float32)
    fx = np.zeros(N, np.float32)
    for st in STARTS:
        L = int(.12 * SR); seg = np.arange(L) / SR; s0 = int((st + .05) * SR); e = min(N, s0 + L)
        fx[s0:e] += (np.sin(2 * np.pi * (900 - 500 * seg / .12) * seg) * np.exp(-seg * 40) * .25)[:e - s0]
    mix = v + m + fx; mix /= np.abs(mix).max() / .95
    with wave.open("/tmp/reel_raw.wav", "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype(np.int16).tobytes())
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", "/tmp/reel_raw.wav", "-af", "highpass=f=60,loudnorm=I=-14:TP=-1.5:LRA=8", "-ar", "48000", "-ac", "2", path], check=True)


if __name__ == "__main__":
    out = sys.argv[3]
    print("durata", round(TOTAL, 1), "s")
    if len(sys.argv) > 4:
        for tt in sys.argv[4:]: frame(float(tt)).save(f"/tmp/reel_{tt}.jpg", quality=85)
        sys.exit()
    audio("/tmp/reel_mix.wav")
    p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-i", "/tmp/reel_mix.wav",
                          "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
    for n in range(int(TOTAL * FPS)): p.stdin.write(frame(n / FPS).tobytes())
    p.stdin.close(); p.wait()
