"""Stili grafici (interfacce) che cambiano con il giorno della settimana — decisione di Amine del 24/11/2026:
"cambia l'interfaccia ogni tanto, lunedì e martedì una, mercoledì e giovedì un'altra, eccetera".

  lunedì + martedì    → casablanca   (nero, rosso e verde, archi: lo stile originale)
  mercoledì + giovedì → chefchaouen  (blu notte, azzurro, rombi)
  venerdì + sabato    → sahara       (terra scura, arancio, onde di dune)
  domenica            → zitoun       (verde oliva, oro, puntini)

Il giorno si prende dalla data nel nome del file (reel-2026-11-25-a.json, lungo2-2026-11-25.py); se non c'è, da oggi
(Europe/Rome). THEME=<nome> forza uno stile (solo per prove). Niente stelle a 6 o 8 punte nei motivi.
"""
import datetime, os, re
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

THEMES = {
    "casablanca": dict(top=(12, 14, 20), bot=(22, 22, 36), glow1=(206, 43, 55), glow2=(0, 98, 51),
                       accent=(206, 43, 55), accent_text=(245, 245, 242), gold=(236, 196, 96), bar=(0, 166, 81),
                       bar2=(0, 98, 51), pattern="arches", cap="box", pill_r=1.0, sub=(200, 200, 205)),
    "chefchaouen": dict(top=(8, 18, 40), bot=(16, 38, 78), glow1=(40, 120, 220), glow2=(0, 170, 200),
                        accent=(36, 120, 226), accent_text=(250, 250, 255), gold=(255, 206, 96), bar=(80, 190, 255),
                        bar2=(28, 92, 170), pattern="diamonds", cap="pill", pill_r=0.3, sub=(190, 210, 235)),
    "sahara": dict(top=(30, 16, 10), bot=(58, 30, 16), glow1=(222, 110, 36), glow2=(150, 60, 28),
                   accent=(214, 98, 30), accent_text=(255, 248, 240), gold=(252, 214, 120), bar=(244, 160, 60),
                   bar2=(150, 70, 24), pattern="waves", cap="underline", pill_r=0.55, sub=(232, 206, 180)),
    "zitoun": dict(top=(8, 24, 18), bot=(14, 44, 32), glow1=(0, 150, 80), glow2=(190, 160, 50),
                   accent=(0, 140, 72), accent_text=(245, 250, 245), gold=(240, 212, 110), bar=(120, 220, 150),
                   bar2=(0, 98, 51), pattern="dots", cap="box", pill_r=0.15, sub=(196, 220, 204)),
}
DAY = {0: "casablanca", 1: "casablanca", 2: "chefchaouen", 3: "chefchaouen", 4: "sahara", 5: "sahara", 6: "zitoun"}


def name_for(path=""):
    if os.environ.get("THEME") in THEMES: return os.environ["THEME"]
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", os.path.basename(path or ""))
    if m: d = datetime.date(*map(int, m.groups()))
    else:
        try:
            from zoneinfo import ZoneInfo
            d = datetime.datetime.now(ZoneInfo("Europe/Rome")).date()
        except Exception: d = datetime.date.today()
    return DAY[d.weekday()]


def pick(path=""):
    n = name_for(path); t = dict(THEMES[n]); t["name"] = n; return t


def background(T, W, H, step=150, alpha=11, glow_boxes=None, blur=170):
    """sfondo: sfumatura verticale + motivo leggero + due aloni colorati."""
    y = np.linspace(0, 1, H)[:, None, None]
    top, bot = np.array(T["top"], np.float32), np.array(T["bot"], np.float32)
    arr = top + (bot - top) * y + np.zeros((1, W, 1), np.float32)
    arr += np.random.default_rng(3).normal(0, 1.0, (H, W, 1))
    im = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).convert("RGBA")
    pat = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(pat); c = (255, 255, 255, alpha); p = T["pattern"]
    if p == "arches":
        for cy in range(0, H + step, step):
            for cx in range(0, W + step, step):
                ox = cx + (step // 2 if (cy // step) % 2 else 0)
                d.arc((ox - 34, cy - 40, ox + 34, cy + 28), 180, 360, fill=c, width=2)
                d.line((ox - 34, cy - 6, ox - 34, cy + 46), fill=c, width=2)
                d.line((ox + 34, cy - 6, ox + 34, cy + 46), fill=c, width=2)
    elif p == "diamonds":
        s = step // 2
        for cy in range(0, H + step, s):
            for cx in range(0, W + step, step):
                ox = cx + (step // 2 if (cy // s) % 2 else 0)
                d.polygon([(ox, cy - 26), (ox + 26, cy), (ox, cy + 26), (ox - 26, cy)], outline=c, width=2)
    elif p == "waves":
        import math
        for k, cy in enumerate(range(-40, H + 80, 70)):
            pts = [(x, cy + 18 * math.sin(x / 140 + k * 0.9)) for x in range(-20, W + 40, 20)]
            d.line(pts, fill=c, width=2)
    elif p == "dots":
        for cy in range(0, H + step, step // 2):
            for cx in range(0, W + step, step // 2):
                ox = cx + (step // 4 if (cy // (step // 2)) % 2 else 0)
                d.ellipse((ox - 4, cy - 4, ox + 4, cy + 4), fill=(255, 255, 255, alpha + 6))
    im = Image.alpha_composite(im, pat)
    g = Image.new("RGBA", (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(g)
    b1, b2 = glow_boxes or ((-400, -300, 600, 700), (W - 600, H - 900, W + 400, H + 100))
    gd.ellipse(b1, fill=T["glow1"] + (70,)); gd.ellipse(b2, fill=T["glow2"] + (75,))
    return Image.alpha_composite(im, g.filter(ImageFilter.GaussianBlur(blur)))


def word_mark(d, T, x0, y0, x1, y1, r):
    """evidenzia la parola che la voce sta dicendo, nello stile del giorno."""
    if T["cap"] == "underline":
        h = max(6, (y1 - y0) // 10); d.rounded_rectangle((x0, y1 - h, x1, y1), h // 2, fill=T["accent"] + (255,))
        return T["gold"]  # colore del testo della parola attiva
    d.rounded_rectangle((x0, y0, x1, y1), max(4, int(r * T["pill_r"] + 4)), fill=T["accent"] + (255,))
    return T["accent_text"]
