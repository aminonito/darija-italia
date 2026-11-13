"""Modelli grafici animati condivisi da render_reel.py (9:16) e render16.py (16:9).

Ogni funzione disegna in un riquadro box=(x1, y1, x2, y2) di un livello RGBA, al tempo lt (secondi dall'inizio
della scena/elemento) e con opacità a (0-1).

  map       mappa Italia (regioni) o Mediterraneo (Italia-Marocco): regioni evidenziate, città, rotte aereo/nave
  people    personaggi illustrati (lavoratore, donna, hijab, anziano, impiegato, medico, studente, bambino...) con fumetti
  icons     2-4 icone con etichetta (icone Tabler, licenza MIT)
  bars      grafico a barre orizzontali (RTL) animato
  calendar  foglio di calendario con giorno e mese
  vs        confronto a due colonne
  steps     passi numerati con spunta

Dati mappa: regioni ISTAT via openpolis/geojson-italy (CC BY 4.0), paesi Natural Earth (pubblico dominio).
La vista "med" è tagliata a nord del 29° parallelo.
"""
import io, json, math, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FD = os.environ.get("FONTS", "/home/claude/fonts/")
RED = (206, 43, 55); GREEN = (0, 166, 81); MGREEN = (0, 98, 51); WHITE = (245, 245, 242)
GREY = (175, 175, 182); DIM = (95, 95, 102); GOLD = (236, 196, 96); BLUE = (70, 140, 230); ORANGE = (240, 140, 40)
CARD = (30, 33, 42)
_fc = {}


LANG = "ar"      # "ar" = darija (destra→sinistra), "it" = italiano (sinistra→destra)
FONTMAP = {}     # nome logico ("Tajawal-Black", "Tajawal-ExtraBold", "Tajawal-Bold") → percorso .ttf


def configure(lang=None, fonts=None, accent=None):
    """es. configure(lang="it", fonts={"Tajawal-Black": PB, "Tajawal-ExtraBold": PB, "Tajawal-Bold": PS}, accent=(126,214,160))"""
    global LANG, GOLD
    if lang: LANG = lang
    if fonts: FONTMAP.update(fonts); _fc.clear()
    if accent: GOLD = tuple(accent)


def rtl(): return LANG == "ar"


def font(n, s):
    s = max(8, int(s))
    if (n, s) not in _fc:
        p = FONTMAP.get(n, FD + n + ".ttf")
        _fc[(n, s)] = ImageFont.truetype(p, s, layout_engine=ImageFont.Layout.RAQM)
    return _fc[(n, s)]


def ease(x): x = min(1, max(0, x)); return 1 - (1 - x) ** 3
def ease_back(x):
    x = min(1, max(0, x)); c1 = 1.70158; c3 = c1 + 1; return 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2


def fit(d, t, n, s, mw, mn=24):
    while s > mn and d.textlength(t, font=font(n, s)) > mw: s -= 2
    return font(n, s)


def col(c):
    if isinstance(c, str): return {"red": RED, "green": GREEN, "gold": GOLD, "white": WHITE, "blue": BLUE, "orange": ORANGE, "grey": GREY}.get(c, GOLD)
    return tuple(c) if c else GOLD


def paste(lay, im, x, y, a=1.0):
    """incolla im (RGBA) centrato in (x, y) con opacità a."""
    if a <= 0.01 or im.width < 1 or im.height < 1: return
    if a < 0.999: im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * a)))
    lay.alpha_composite(im, (int(x - im.width / 2), int(y - im.height / 2)))


def scaled(im, s):
    s = max(0.02, s)
    if abs(s - 1) < 0.01: return im
    return im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))), Image.BILINEAR)


# ---------------- icone ----------------
_ic = {}


def icon(name, size, color=WHITE, stroke=1.9):
    k = (name, int(size), color, stroke)
    if k not in _ic:
        import cairosvg
        p = os.path.join(ROOT, "assets/icons", name + ".svg")
        if not os.path.exists(p): raise KeyError(f"icona '{name}' non trovata in assets/icons")
        svg = open(p).read().replace("currentColor", "#%02x%02x%02x" % tuple(color[:3])).replace('stroke-width="2"', f'stroke-width="{stroke}"')
        png = cairosvg.svg2png(bytestring=svg.encode(), output_width=int(size), output_height=int(size))
        _ic[k] = Image.open(io.BytesIO(png)).convert("RGBA")
    return _ic[k]


def icon_names():
    return sorted(f[:-4] for f in os.listdir(os.path.join(ROOT, "assets/icons")) if f.endswith(".svg"))


# ---------------- mappe ----------------
MAPS = json.load(open(os.path.join(ROOT, "assets/maps.json")))
CITY = {"Roma": (12.496, 41.903), "Milano": (9.190, 45.464), "Torino": (7.687, 45.070), "Napoli": (14.268, 40.852),
        "Bologna": (11.343, 44.495), "Firenze": (11.256, 43.770), "Genova": (8.946, 44.406), "Venezia": (12.316, 45.441),
        "Bari": (16.872, 41.117), "Palermo": (13.362, 38.116), "Catania": (15.087, 37.508), "Verona": (10.992, 45.438),
        "Brescia": (10.212, 45.542), "Bergamo": (9.670, 45.698), "Padova": (11.877, 45.406), "Reggio Calabria": (15.661, 38.111),
        "Cagliari": (9.122, 39.224), "Trieste": (13.777, 45.650), "Ancona": (13.519, 43.616), "Perugia": (12.389, 43.111),
        "Salerno": (14.768, 40.682), "Livorno": (10.317, 43.549), "Civitavecchia": (11.797, 42.092), "Modena": (10.925, 44.647),
        "Parma": (10.328, 44.802), "Reggio Emilia": (10.630, 44.699), "Vicenza": (11.535, 45.546), "Treviso": (12.245, 45.667),
        "Tanger": (-5.834, 35.760), "Tetouan": (-5.368, 35.589), "Nador": (-2.934, 35.168), "Casablanca": (-7.590, 33.573),
        "Rabat": (-6.850, 34.021), "Fes": (-5.008, 34.018), "Marrakech": (-7.981, 31.630), "Agadir": (-9.598, 30.428),
        "Oujda": (-1.909, 34.681), "Meknes": (-5.547, 33.894), "Beni Mellal": (-6.350, 32.337), "Khouribga": (-6.906, 32.881),
        "El Jadida": (-8.501, 33.232), "Kenitra": (-6.580, 34.261)}
CITY_AR = {"Roma": "روما", "Milano": "ميلانو", "Torino": "تورينو", "Napoli": "نابولي", "Bologna": "بولونيا", "Firenze": "فلورنسا",
           "Genova": "جنوة", "Venezia": "فينيسيا", "Bari": "باري", "Palermo": "باليرمو", "Catania": "كاتانيا", "Verona": "فيرونا",
           "Brescia": "بريشيا", "Bergamo": "بيرغامو", "Padova": "بادوفا", "Reggio Calabria": "ريدجو كالابريا", "Cagliari": "كالياري",
           "Trieste": "تريستي", "Ancona": "أنكونا", "Perugia": "بيروجيا", "Salerno": "ساليرنو", "Livorno": "ليفورنو",
           "Civitavecchia": "تشيفيتافيكيا", "Modena": "مودينا", "Parma": "بارما", "Reggio Emilia": "ريدجو إيميليا",
           "Vicenza": "فيتشينزا", "Treviso": "تريفيزو", "Tanger": "طنجة", "Tetouan": "تطوان", "Nador": "الناظور",
           "Casablanca": "كازا", "Rabat": "الرباط", "Fes": "فاس", "Marrakech": "مراكش", "Agadir": "أكادير", "Oujda": "وجدة",
           "Meknes": "مكناس", "Beni Mellal": "بني ملال", "Khouribga": "خريبكة", "El Jadida": "الجديدة", "Kenitra": "القنيطرة"}
REG_AR = {"Lombardia": "لومبارديا", "Piemonte": "بييمونتي", "Veneto": "فينيتو", "Emilia-Romagna": "إيميليا رومانيا",
          "Toscana": "توسكانا", "Lazio": "لاتسيو", "Campania": "كامبانيا", "Puglia": "بوليا", "Sicilia": "صقلية",
          "Calabria": "كالابريا", "Sardegna": "سردينيا", "Liguria": "ليغوريا", "Marche": "ماركي", "Abruzzo": "أبروتسو",
          "Umbria": "أومبريا", "Basilicata": "بازيليكاتا", "Molise": "موليزي", "Friuli-Venezia Giulia": "فريولي",
          "Trentino-Alto Adige": "ترينتينو", "Valle d'Aosta": "فالي داوستا", "ITA": "إيطاليا", "MAR": "المغرب"}
CITY_IT = {"Tanger": "Tangeri", "Tetouan": "Tetuan", "Fes": "Fès", "Meknes": "Meknès", "Marrakech": "Marrakech"}
REG_IT = {"ITA": "Italia", "MAR": "Marocco", "Valle d'Aosta": "Valle d'Aosta"}


def city_label(c): return CITY_AR.get(c, c) if rtl() else CITY_IT.get(c, c)
def reg_label(r): return REG_AR.get(r, r) if rtl() else REG_IT.get(r, r)


VIEWS = {"italy": (6.4, 18.8, 36.4, 47.2), "north": (6.5, 14.0, 43.5, 47.2), "south": (12.2, 18.8, 36.5, 42.6),
         "med": (-11.0, 19.5, 29.0, 47.5)}
_mc = {}


def _proj(view, box):
    lo0, lo1, la0, la1 = VIEWS[view]; k = math.cos(math.radians((la0 + la1) / 2))
    bw, bh = box[2] - box[0], box[3] - box[1]; mw, mh = (lo1 - lo0) * k, la1 - la0
    s = min(bw / mw, bh / mh); ox = box[0] + (bw - mw * s) / 2; oy = box[1] + (bh - mh * s) / 2
    return lambda lon, lat: (ox + (lon - lo0) * k * s, oy + (la1 - lat) * s)


def _shapes(view):
    if view == "med":
        return {c: p for c, p in MAPS["countries"].items() if c not in ("SAH",)}
    return MAPS["italy_regions"]


def _base(view, box):
    key = (view, box)
    if key in _mc: return _mc[key]
    P = _proj(view, box); x1, y1, x2, y2 = box; SS = 2
    im = Image.new("RGBA", ((x2 - x1) * SS, (y2 - y1) * SS), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    polys = {}
    from shapely.geometry import Polygon, box as sbox
    lo0, lo1, la0, la1 = VIEWS[view]; clip = sbox(lo0, la0, lo1, la1)
    for name, ps in _shapes(view).items():
        out = []
        for p in ps:
            g = Polygon(p)
            if not g.is_valid: g = g.buffer(0)
            if not g.intersects(clip): continue
            g = g.intersection(clip)
            for q in ([g] if g.geom_type == "Polygon" else [h for h in getattr(g, "geoms", []) if h.geom_type == "Polygon"]):
                if q.area > 0: out.append([(P(lo, la)[0] - x1, P(lo, la)[1] - y1) for lo, la in q.exterior.coords])
        if out: polys[name] = out
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
    for name, ps in polys.items():
        for p in ps: ds.polygon([(x * SS + 10, y * SS + 14) for x, y in p], fill=(0, 0, 0, 120))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10)))
    for name, ps in polys.items():
        main = view != "med" or name in ("ITA", "MAR")
        fill = (58, 64, 80, 255) if main else (40, 43, 52, 255)
        for p in ps: d.polygon([(x * SS, y * SS) for x, y in p], fill=fill, outline=(98, 104, 120, 255) if main else (62, 66, 76, 255), width=SS * 2)
    im = im.resize((x2 - x1, y2 - y1), Image.LANCZOS)
    _mc[key] = (im, polys, P)
    return _mc[key]


def _pin(L, x, y, c, al, s=1.0):
    r = 20 * s
    L.ellipse((x - r * 1.9, y - r * 1.9, x + r * 1.9, y + r * 1.9), fill=c + (int(al * 0.25),))
    L.ellipse((x - r, y - r, x + r, y + r), fill=c + (al,), outline=WHITE + (al,), width=max(2, int(4 * s)))


def _label(L, x, y, text, al, size=38, bg=(15, 17, 22), fg=WHITE, anchor="above"):
    f = font("Tajawal-ExtraBold", size); tw = L.textlength(text, font=f); h = size * 1.35
    cy = y - h * 1.15 if anchor == "above" else y + h * 1.15
    L.rounded_rectangle((x - tw / 2 - 20, cy - h / 2, x + tw / 2 + 20, cy + h / 2), h / 2, fill=bg + (int(al * 0.88),))
    L.text((x, cy + 2), text, font=f, fill=fg + (al,), anchor="mm")


def draw_map(lay, box, spec, lt, a=1.0):
    view = spec.get("view", "italy"); box = tuple(int(v) for v in box)
    base, polys, P = _base(view, box)
    ap = a * ease(lt / 0.5)
    sc = 0.94 + 0.06 * ease(lt / 0.7)
    paste(lay, scaled(base, sc), (box[0] + box[2]) / 2, (box[1] + box[3]) / 2, ap)
    cx, cy = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2
    tr = lambda x, y: (cx + (x - cx) * sc, cy + (y - cy) * sc)
    L = ImageDraw.Draw(lay); al = int(255 * a)
    sz = spec.get("size", 1.0)
    # regioni / paesi evidenziati
    for j, name in enumerate(spec.get("hl", [])):
        t0 = spec.get("t", 0.45) + 0.3 * j
        if lt < t0 or name not in polys: continue
        e = ease((lt - t0) / 0.4); c = col(spec.get("color", "gold"))
        pulse = 0.82 + 0.18 * math.sin((lt - t0) * 4)
        for p in polys[name]:
            pts = [tr(box[0] + x, box[1] + y) for x, y in p]
            L.polygon(pts, fill=c + (int(al * e * 0.85 * pulse),), outline=WHITE + (int(al * e),), width=3)
        pin_xy = [tr(*P(*CITY[(q if isinstance(q, str) else q["city"])])) for q in spec.get("pins", [])]
        if spec.get("labels", True):
            xs = [x for p in polys[name] for x, _ in p]; ys = [y for p in polys[name] for _, y in p]
            big = max(polys[name], key=len); mx = sum(x for x, _ in big) / len(big); my = sum(y for _, y in big) / len(big)
            lx, ly = tr(box[0] + mx, box[1] + my)
            if any(abs(lx - px) < 170 * sz and abs(ly + 40 * sz - py) < 90 * sz for px, py in pin_xy): ly += 70 * sz
            _label(L, lx, ly + 40 * sz, reg_label(name), int(al * e), int(36 * sz))
    # rotta
    rt = spec.get("route")
    if rt:
        t0 = spec.get("t", 0.45); A = tr(*P(*CITY[rt[0]])); B = tr(*P(*CITY[rt[1]]))
        mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2; dx, dy = B[0] - A[0], B[1] - A[1]; ln = math.hypot(dx, dy) or 1
        C = (mx - dy / ln * ln * 0.28, my + dx / ln * ln * 0.28 * (-1 if dx > 0 else 1))
        if C[1] > my: C = (mx + dy / ln * ln * 0.28, my - dx / ln * ln * 0.28 * (-1 if dx > 0 else 1))
        bz = lambda u: ((1 - u) ** 2 * A[0] + 2 * (1 - u) * u * C[0] + u * u * B[0], (1 - u) ** 2 * A[1] + 2 * (1 - u) * u * C[1] + u * u * B[1])
        prog = ease((lt - t0) / spec.get("dur", 1.6))
        if lt >= t0:
            _pin(L, *A, RED, al, sz)
            n = 60
            for q in range(int(n * prog)):
                if q % 2 == 0: L.line([bz(q / n), bz((q + 1) / n)], fill=WHITE + (al,), width=int(7 * sz))
            u = max(0.001, prog); p1 = bz(max(0, u - 0.01)); p2 = bz(u)
            ang = math.degrees(math.atan2(-(p2[1] - p1[1]), p2[0] - p1[0]))
            ic = icon("plane" if rt[2:] == [] or rt[2] == "plane" else rt[2], int(86 * sz), GOLD, 2.2)
            ic = ic.rotate(ang - 45 if (rt[2:] == [] or rt[2] == "plane") else 0, resample=Image.BICUBIC, expand=True)
            if prog < 1: paste(lay, ic, *p2, a)
            if prog >= 1:
                _pin(L, *B, GREEN, al, sz)
            for cname, pt, ok in ((rt[0], A, True), (rt[1], B, prog >= 1)):
                if ok: _label(L, pt[0], pt[1], city_label(cname), al, int(38 * sz))
    # città (etichette sotto se troppo vicine a una precedente)
    placed = []
    for j, pn in enumerate(spec.get("pins", [])):
        if isinstance(pn, str): pn = {"city": pn}
        t0 = spec.get("t", 0.45) + spec.get("pin_gap", 0.35) * j
        if lt < t0: continue
        x, y = tr(*P(*CITY[pn["city"]])); e = ease_back((lt - t0) / 0.35)
        if "anchor" not in pn and any(abs(x - px) < 150 * sz and abs(y - py) < 70 * sz and pa == "above" for px, py, pa in placed):
            pn = dict(pn, anchor="below")
        placed.append((x, y, pn.get("anchor", "above")))
        yy = y - 40 * (1 - ease((lt - t0) / 0.3))
        _pin(L, x, yy, col(pn.get("color", "red")), int(al * min(1, e)), sz * max(0.3, e))
        _label(L, x, yy, pn.get("label", city_label(pn["city"])), int(al * ease((lt - t0) / 0.3)), int(36 * sz),
               anchor=pn.get("anchor", "above"))


# ---------------- personaggi ----------------
SKIN = [(236, 192, 152), (205, 150, 108), (168, 112, 74), (128, 86, 58)]
HAIR = (38, 28, 24)
ROLES = {
    "worker": dict(skin=1, hair="short", hat="helmet", shirt=(72, 86, 110), vest=ORANGE),
    "man": dict(skin=2, hair="short", beard=True, shirt=(52, 110, 190)),
    "woman": dict(skin=0, hair="long", shirt=(0, 140, 95)),
    "hijab": dict(skin=1, hair="hijab", hijab=(120, 70, 140), shirt=(120, 70, 140)),
    "elder": dict(skin=2, hair="short", haircol=(205, 205, 210), beard=True, beardcol=(215, 215, 220), glasses=True, shirt=(130, 95, 70)),
    "office": dict(skin=0, hair="short", shirt=(235, 235, 240), jacket=(40, 50, 75), tie=RED),
    "doctor": dict(skin=1, hair="short", shirt=(110, 170, 200), coat=True),
    "student": dict(skin=2, hair="curly", shirt=(220, 80, 70), straps=True),
    "child": dict(skin=1, hair="short", shirt=(240, 190, 60), small=True),
    "girl": dict(skin=2, hair="long", shirt=(230, 100, 140), small=True),
    "clerk": dict(skin=3, hair="short", glasses=True, shirt=(236, 196, 96), lanyard=True),
    "farmer": dict(skin=3, hair="short", hat="straw", shirt=(90, 120, 60), beard=True),
}
_pc = {}


def person(role, h):
    """mezzobusto illustrato, altezza h px."""
    k = (role, int(h))
    if k in _pc: return _pc[k]
    R = dict(ROLES.get(role, ROLES["man"])); SS = 3; S = h * SS; w = int(S * 0.92)
    im = Image.new("RGBA", (w, int(S)), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    sk = SKIN[R.get("skin", 1)]; hc = R.get("haircol", HAIR)
    hr = S * (0.2 if R.get("small") else 0.17); hx, hy = w / 2, S * (0.36 if R.get("small") else 0.33)
    body_top = hy + hr * 1.25
    if R["hair"] == "long":  # capelli dietro
        d.rounded_rectangle((hx - hr * 1.22, hy - hr * 1.05, hx + hr * 1.22, hy + hr * 1.9), hr * 0.9, fill=hc)
    if R["hair"] == "hijab":
        d.rounded_rectangle((hx - hr * 1.42, hy - hr * 1.32, hx + hr * 1.42, body_top + hr * 1.6), hr * 1.3, fill=R["hijab"])
    # corpo
    sh = R["shirt"]
    d.rounded_rectangle((w * 0.08, body_top, w * 0.92, S * 1.25), S * 0.17, fill=sh)
    if R.get("jacket"):
        j = R["jacket"]
        d.polygon([(w * 0.08 + S * 0.05, body_top + S * 0.03), (hx - S * 0.02, body_top + S * 0.05), (hx - S * 0.1, S), (w * 0.08, S)], fill=j)
        d.polygon([(w * 0.92 - S * 0.05, body_top + S * 0.03), (hx + S * 0.02, body_top + S * 0.05), (hx + S * 0.1, S), (w * 0.92, S)], fill=j)
        d.rounded_rectangle((w * 0.08, body_top + S * 0.12, w * 0.24, S * 1.25), S * 0.08, fill=j)
        d.rounded_rectangle((w * 0.76, body_top + S * 0.12, w * 0.92, S * 1.25), S * 0.08, fill=j)
    if R.get("coat"):
        c = (240, 242, 245)
        d.polygon([(w * 0.08, body_top + S * 0.1), (hx - S * 0.05, body_top), (hx - S * 0.03, S), (w * 0.08, S)], fill=c)
        d.polygon([(w * 0.92, body_top + S * 0.1), (hx + S * 0.05, body_top), (hx + S * 0.03, S), (w * 0.92, S)], fill=c)
        d.rounded_rectangle((w * 0.08, body_top + S * 0.06, w * 0.92, body_top + S * 0.2), S * 0.08, fill=c)
        d.rectangle((hx - S * 0.05, body_top, hx + S * 0.05, S), fill=R["shirt"])
        d.arc((hx - S * 0.13, body_top - S * 0.02, hx + S * 0.13, body_top + S * 0.26), 0, 180, fill=(60, 64, 72), width=int(S * 0.018))
        d.ellipse((hx + S * 0.07, body_top + S * 0.2, hx + S * 0.13, body_top + S * 0.26), fill=(150, 155, 165))
    if R.get("vest"):
        v = R["vest"]
        d.polygon([(w * 0.08, body_top + S * 0.08), (hx - S * 0.06, body_top + S * 0.02), (hx - S * 0.08, S), (w * 0.08, S)], fill=v)
        d.polygon([(w * 0.92, body_top + S * 0.08), (hx + S * 0.06, body_top + S * 0.02), (hx + S * 0.08, S), (w * 0.92, S)], fill=v)
        for yy in (0.78, 0.88):
            d.rectangle((w * 0.08, S * yy, hx - S * 0.075, S * yy + S * 0.025), fill=(230, 230, 220))
            d.rectangle((hx + S * 0.075, S * yy, w * 0.92, S * yy + S * 0.025), fill=(230, 230, 220))
    if R.get("straps"):
        for sx in (-1, 1):
            d.rounded_rectangle((hx + sx * S * 0.2 - S * 0.03, body_top + S * 0.02, hx + sx * S * 0.2 + S * 0.03, S), S * 0.02, fill=(40, 44, 60))
    if R.get("lanyard"):
        d.line([(hx - S * 0.07, body_top), (hx, body_top + S * 0.22), (hx + S * 0.07, body_top)], fill=(40, 80, 160), width=int(S * 0.012))
        d.rounded_rectangle((hx - S * 0.05, body_top + S * 0.2, hx + S * 0.05, body_top + S * 0.32), S * 0.01, fill=WHITE)
    # collo
    if R["hair"] != "hijab":
        d.rounded_rectangle((hx - hr * 0.42, hy + hr * 0.6, hx + hr * 0.42, body_top + S * 0.04), hr * 0.2, fill=tuple(int(v * 0.9) for v in sk))
    if R.get("tie"):
        d.polygon([(hx - S * 0.025, body_top + S * 0.01), (hx + S * 0.025, body_top + S * 0.01), (hx + S * 0.04, body_top + S * 0.26),
                   (hx, body_top + S * 0.31), (hx - S * 0.04, body_top + S * 0.26)], fill=R["tie"])
    # testa
    if R["hair"] != "hijab":
        for ex in (-1, 1): d.ellipse((hx + ex * hr * 0.98 - hr * 0.16, hy - hr * 0.1, hx + ex * hr * 0.98 + hr * 0.16, hy + hr * 0.25), fill=sk)
    d.ellipse((hx - hr, hy - hr * 1.05, hx + hr, hy + hr * 1.0), fill=sk)
    if R.get("beard"):
        bc = R.get("beardcol", hc)
        d.chord((hx - hr * 0.98, hy - hr * 0.6, hx + hr * 0.98, hy + hr * 1.0), 0, 180, fill=bc)
        d.ellipse((hx - hr * 0.3, hy + hr * 0.32, hx + hr * 0.3, hy + hr * 0.58), fill=sk)
    # capelli sopra
    if R["hair"] in ("short", "long", "curly"):
        d.chord((hx - hr * 1.04, hy - hr * 1.12, hx + hr * 1.04, hy + hr * 0.5), 180, 360, fill=hc)
        if R["hair"] == "curly":
            for q in range(7):
                ang = math.pi + q * math.pi / 6; d.ellipse((hx + math.cos(ang) * hr * 0.92 - hr * 0.26, hy - hr * 0.3 + math.sin(ang) * hr * 0.92 - hr * 0.26,
                                                            hx + math.cos(ang) * hr * 0.92 + hr * 0.26, hy - hr * 0.3 + math.sin(ang) * hr * 0.92 + hr * 0.26), fill=hc)
        if R["hair"] == "long":
            d.pieslice((hx - hr * 1.1, hy - hr * 1.15, hx + hr * 0.6, hy + hr * 0.4), 180, 300, fill=hc)
    if R["hair"] == "hijab":
        d.chord((hx - hr * 1.08, hy - hr * 1.15, hx + hr * 1.08, hy + hr * 0.25), 180, 360, fill=R["hijab"])
    # viso
    ec = (30, 26, 26)
    for ex in (-1, 1):
        d.ellipse((hx + ex * hr * 0.36 - hr * 0.09, hy + hr * 0.02 - hr * 0.11, hx + ex * hr * 0.36 + hr * 0.09, hy + hr * 0.02 + hr * 0.11), fill=ec)
        d.line([(hx + ex * hr * 0.22, hy - hr * 0.3), (hx + ex * hr * 0.5, hy - hr * 0.25)], fill=hc if R["hair"] != "hijab" else (60, 40, 40), width=int(hr * 0.07))
        d.ellipse((hx + ex * hr * 0.55 - hr * 0.12, hy + hr * 0.25, hx + ex * hr * 0.55 + hr * 0.12, hy + hr * 0.4), fill=tuple(int(0.8 * v + 0.2 * w) for v, w in zip(sk, (240, 110, 110))))
    if R.get("glasses"):
        for ex in (-1, 1): d.ellipse((hx + ex * hr * 0.36 - hr * 0.22, hy - hr * 0.2, hx + ex * hr * 0.36 + hr * 0.22, hy + hr * 0.24), outline=(40, 40, 45), width=int(hr * 0.06))
        d.line([(hx - hr * 0.14, hy), (hx + hr * 0.14, hy)], fill=(40, 40, 45), width=int(hr * 0.05))
    d.arc((hx - hr * 0.26, hy + hr * 0.2, hx + hr * 0.26, hy + hr * 0.52), 20, 160, fill=(120, 40, 40), width=int(hr * 0.08))
    # cappelli
    if R.get("hat") == "helmet":
        d.chord((hx - hr * 1.1, hy - hr * 1.3, hx + hr * 1.1, hy + hr * 0.5), 180, 360, fill=(250, 200, 40))
        d.rounded_rectangle((hx - hr * 1.3, hy - hr * 0.48, hx + hr * 1.3, hy - hr * 0.3), hr * 0.08, fill=(225, 175, 20))
        d.rectangle((hx - hr * 0.1, hy - hr * 1.28, hx + hr * 0.1, hy - hr * 0.5), fill=(230, 180, 25))
    if R.get("hat") == "straw":
        d.ellipse((hx - hr * 1.7, hy - hr * 0.7, hx + hr * 1.7, hy - hr * 0.3), fill=(215, 180, 110))
        d.chord((hx - hr * 0.95, hy - hr * 1.4, hx + hr * 0.95, hy - hr * 0.1), 180, 360, fill=(225, 190, 120))
        d.rectangle((hx - hr * 0.95, hy - hr * 0.72, hx + hr * 0.95, hy - hr * 0.6), fill=(170, 60, 50))
    im = im.resize((w // SS, int(S) // SS), Image.LANCZOS)
    _pc[k] = im
    return im


def bubble(L, x, y, text, al, size=44, maxw=600, tail="down", bg=WHITE, fg=(20, 20, 26)):
    f = fit(L, text, "Tajawal-ExtraBold", size, maxw); tw = L.textlength(text, font=f); h = f.size * 1.6
    bx1, bx2 = x - tw / 2 - 34, x + tw / 2 + 34; by1, by2 = y - h, y
    L.rounded_rectangle((bx1, by1, bx2, by2), 30, fill=bg + (al,))
    if tail == "down": L.polygon([(x - 22, by2 - 2), (x + 22, by2 - 2), (x, by2 + 30)], fill=bg + (al,))
    L.text((x, (by1 + by2) / 2 + 3), text, font=f, fill=fg + (al,), anchor="mm")


def draw_people(lay, box, spec, lt, a=1.0):
    x1, y1, x2, y2 = box; ppl = spec["people"]; n = len(ppl); bw = x2 - x1
    ph = spec.get("h", min((y2 - y1) * 0.74, bw / n * 1.3 / 0.92))
    L = ImageDraw.Draw(lay); al = int(255 * a)
    xs = [(x2 - bw * (j + 0.5) / n) if rtl() else (x1 + bw * (j + 0.5) / n) for j in range(n)]
    ground = y2
    for j, r in enumerate(ppl):
        t0 = 0.12 + 0.18 * j
        if lt < t0: continue
        e = ease_back((lt - t0) / 0.45); bob = 6 * math.sin((lt + j) * 2.2)
        im = person(r, ph * (0.78 if ROLES.get(r, {}).get("small") else 1.0))
        im = scaled(im, max(0.05, e))
        # taglio in basso: il busto "esce" dal bordo
        x = xs[j]; yb = ground + bob
        tmp = Image.new("RGBA", lay.size, (0, 0, 0, 0)); tmp.alpha_composite(im, (int(x - im.width / 2), int(yb - im.height)))
        tmp = tmp.crop((0, 0, lay.width, int(ground))); full = Image.new("RGBA", lay.size, (0, 0, 0, 0)); full.alpha_composite(tmp, (0, 0))
        if a < 0.999: full.putalpha(full.getchannel("A").point(lambda v: int(v * a)))
        lay.alpha_composite(full)
    for b in spec.get("say", []):
        if isinstance(b, str): b = {"text": b}
        who = b.get("who", 0); t0 = b.get("at", 0.55)
        if lt < t0 or who >= n: continue
        e = ease_back((lt - t0) / 0.35); ab = int(al * ease((lt - t0) / 0.2))
        im_h = ph * (0.78 if ROLES.get(ppl[who], {}).get("small") else 1.0)
        top = ground - im_h * 0.98
        tmp = Image.new("RGBA", lay.size, (0, 0, 0, 0)); T = ImageDraw.Draw(tmp)
        bubble(T, xs[who], top - 10, b["text"], 255, b.get("size", spec.get("say_size", 46)), maxw=min(bw * 0.92, b.get("maxw", 900)),
               bg=col(b["bg"]) if b.get("bg") else WHITE, fg=(255, 255, 255) if b.get("bg") else (20, 20, 26))
        tmp = scaled(tmp, 1.0); sc = max(0.05, e)
        if sc < 0.999:
            cx, cy = xs[who], top
            t2 = tmp.resize((int(tmp.width * sc), int(tmp.height * sc)), Image.BILINEAR); tmp = Image.new("RGBA", lay.size, (0, 0, 0, 0))
            tmp.alpha_composite(t2, (int(cx - cx * sc), int(cy - cy * sc)))
        if ab < 255: tmp.putalpha(tmp.getchannel("A").point(lambda v: int(v * ab / 255)))
        lay.alpha_composite(tmp)


# ---------------- icone con etichetta ----------------
def draw_icons(lay, box, spec, lt, a=1.0):
    x1, y1, x2, y2 = box; its = spec["items"]; n = len(its)
    cols = spec.get("cols", n if n <= 3 else 2); rows = math.ceil(n / cols)
    cw, chh = (x2 - x1) / cols, (y2 - y1) / rows
    L = ImageDraw.Draw(lay); al = int(255 * a)
    for j, it in enumerate(its):
        name, lab = it[0], it[1]; c = col(it[2]) if len(it) > 2 else [GOLD, GREEN, BLUE, RED][j % 4]
        t0 = spec.get("t", 0.15) + spec.get("gap", 0.35) * j
        if lt < t0: continue
        e = ease_back((lt - t0) / 0.4); aj = int(al * ease((lt - t0) / 0.25))
        cx = (x2 - cw * (j % cols + 0.5)) if rtl() else (x1 + cw * (j % cols + 0.5)); cy = y1 + chh * (j // cols + 0.5)
        s = min(cw, chh) * 0.92; r = s * 0.42 * max(0.05, e)
        L.rounded_rectangle((cx - s / 2, cy - s / 2, cx + s / 2, cy + s / 2), s * 0.14, fill=CARD + (int(aj * 0.9),))
        L.ellipse((cx - r * 0.82, cy - s * 0.12 - r * 0.82, cx + r * 0.82, cy - s * 0.12 + r * 0.82), fill=c + (int(aj * 0.25),))
        ic = icon(name, int(r * 1.1), c, 1.8); paste(lay, ic, cx, cy - s * 0.12, aj / 255)
        f = fit(L, lab, "Tajawal-ExtraBold", s * 0.13, s * 0.92); L.text((cx, cy + s * 0.32), lab, font=f, fill=WHITE + (aj,), anchor="mm")


# ---------------- barre ----------------
def draw_bars(lay, box, spec, lt, a=1.0):
    x1, y1, x2, y2 = box; bars = spec["bars"]; n = len(bars); mx = max(b[1] for b in bars) or 1
    L = ImageDraw.Draw(lay); al = int(255 * a); rh = (y2 - y1) / n; lw = spec.get("label_w", (x2 - x1) * 0.34)
    if spec.get("title"):
        pass
    for j, b in enumerate(bars):
        lab, val, disp = b[0], b[1], b[2]; c = col(b[3]) if len(b) > 3 else [GOLD, GREEN, BLUE, RED][j % 4]
        t0 = spec.get("t", 0.2) + spec.get("gap", 0.3) * j
        if lt < t0: continue
        e = ease((lt - t0) / 0.9); aj = int(al * ease((lt - t0) / 0.25)); cy = y1 + rh * (j + 0.5); bh = min(rh * 0.5, 110)
        f = fit(L, lab, "Tajawal-ExtraBold", min(rh * 0.3, 54), lw - 20)
        fv = font("Tajawal-Black", min(bh * 0.75, 60))
        if rtl():
            L.text((x2, cy), lab, font=f, fill=WHITE + (aj,), anchor="rm")
            bx2 = x2 - lw; full = (bx2 - x1) * 0.7; bl = full * val / mx * e
            L.rounded_rectangle((bx2 - full, cy - bh / 2, bx2, cy + bh / 2), bh / 2, fill=(255, 255, 255, int(aj * 0.07)))
            if bl > 4: L.rounded_rectangle((bx2 - bl, cy - bh / 2, bx2, cy + bh / 2), bh / 2, fill=c + (aj,))
            L.text((bx2 - bl - 18, cy + 2), disp, font=fv, fill=c + (aj,), anchor="rm")
        else:
            L.text((x1, cy), lab, font=f, fill=WHITE + (aj,), anchor="lm")
            bx1 = x1 + lw; full = (x2 - bx1) * 0.7; bl = full * val / mx * e
            L.rounded_rectangle((bx1, cy - bh / 2, bx1 + full, cy + bh / 2), bh / 2, fill=(255, 255, 255, int(aj * 0.07)))
            if bl > 4: L.rounded_rectangle((bx1, cy - bh / 2, bx1 + bl, cy + bh / 2), bh / 2, fill=c + (aj,))
            L.text((bx1 + bl + 18, cy + 2), disp, font=fv, fill=c + (aj,), anchor="lm")


# ---------------- calendario ----------------
MONTH_IT = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre",
            "novembre", "dicembre"]
MONTH_AR = ["يناير", "فبراير", "مارس", "أبريل", "ماي", "يونيو", "يوليوز", "غشت", "شتنبر", "أكتوبر", "نونبر", "دجنبر"]


def draw_calendar(lay, box, spec, lt, a=1.0):
    x1, y1, x2, y2 = box; cx, cy = (x1 + x2) / 2, (y1 + y2) / 2; s = min(x2 - x1, y2 - y1) * 0.8
    al = int(255 * a); e = ease_back(lt / 0.5)
    tmp = Image.new("RGBA", (int(s), int(s)), (0, 0, 0, 0)); T = ImageDraw.Draw(tmp)
    T.rounded_rectangle((0, 0, s - 1, s - 1), s * 0.1, fill=(246, 246, 242, 255))
    T.rounded_rectangle((0, 0, s - 1, s * 0.3), s * 0.1, fill=RED + (255,)); T.rectangle((0, s * 0.18, s - 1, s * 0.3), fill=RED + (255,))
    for rx in (0.3, 0.7): T.rounded_rectangle((s * rx - s * 0.03, -s * 0.0, s * rx + s * 0.03, s * 0.08), s * 0.02, fill=(60, 60, 66, 255))
    m = spec.get("month"); m = (MONTH_AR if rtl() else MONTH_IT)[m - 1] if isinstance(m, int) else m
    T.text((s / 2, s * 0.16), m, font=fit(T, m, "Tajawal-Black", s * 0.14, s * 0.85), fill=WHITE + (255,), anchor="mm")
    dd = str(spec["day"]); T.text((s / 2, s * 0.6), dd, font=fit(T, dd, "Tajawal-Black", s * 0.46, s * 0.85), fill=(25, 25, 30, 255), anchor="mm")
    if spec.get("sub"): T.text((s / 2, s * 0.88), spec["sub"], font=fit(T, spec["sub"], "Tajawal-Bold", s * 0.075, s * 0.85), fill=(90, 90, 98, 255), anchor="mm")
    sh = Image.new("RGBA", (int(s * 1.2), int(s * 1.2)), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((s * 0.12, s * 0.15, s * 1.1, s * 1.13), s * 0.1, fill=(0, 0, 0, 140))
    paste(lay, scaled(sh.filter(ImageFilter.GaussianBlur(20)), max(0.05, e)), cx, cy, a)
    tmp = tmp.rotate(-4 * (1 - ease(lt / 0.6)) + 2 * math.sin(lt * 1.3) * 0.3, resample=Image.BICUBIC, expand=True)
    paste(lay, scaled(tmp, max(0.05, e)), cx, cy, a)


# ---------------- confronto ----------------
def draw_vs(lay, box, spec, lt, a=1.0):
    x1, y1, x2, y2 = box; L = ImageDraw.Draw(lay); al = int(255 * a); gap = 40; cw = (x2 - x1 - gap) / 2
    sides = [(spec["right"], 0), (spec["left"], 1)] if rtl() else [(spec["left"], 1), (spec["right"], 0)]
    for j, (sd, pos) in enumerate(sides):
        t0 = spec.get("t", 0.2) + spec.get("gap", 0.6) * j
        if lt < t0: continue
        e = ease((lt - t0) / 0.4); aj = int(al * e); c = col(sd.get("color", "gold" if j == 0 else "grey"))
        bx2 = x2 - pos * (cw + gap); bx1 = bx2 - cw; dy = 40 * (1 - e)
        L.rounded_rectangle((bx1, y1 + dy, bx2, y2 + dy), 40, fill=CARD + (int(aj * 0.92),), outline=c + (aj,), width=4)
        cx = (bx1 + bx2) / 2; hh = y2 - y1
        if sd.get("icon"): paste(lay, icon(sd["icon"], int(min(cw, hh) * 0.26), c, 1.8), cx, y1 + dy + hh * 0.2, aj / 255)
        if sd.get("person"):
            p = person(sd["person"], hh * 0.32); paste(lay, p, cx, y1 + dy + hh * 0.2, aj / 255)
        L.text((cx, y1 + dy + hh * 0.43), sd["title"], font=fit(L, sd["title"], "Tajawal-ExtraBold", hh * 0.075, cw * 0.86), fill=WHITE + (aj,), anchor="mm")
        L.text((cx, y1 + dy + hh * 0.63), sd["value"], font=fit(L, sd["value"], "Tajawal-Black", hh * 0.16, cw * 0.86), fill=c + (aj,), anchor="mm")
        if sd.get("sub"): L.text((cx, y1 + dy + hh * 0.82), sd["sub"], font=fit(L, sd["sub"], "Tajawal-Bold", hh * 0.05, cw * 0.86), fill=GREY + (aj,), anchor="mm")
    t1 = spec.get("t", 0.2) + spec.get("gap", 0.6)
    if lt > t1:
        e = ease_back((lt - t1) / 0.4); r = 54 * max(0.05, e); cx = x2 - cw - gap / 2; cy = (y1 + y2) / 2
        L.ellipse((cx - r, cy - r, cx + r, cy + r), fill=RED + (al,), outline=WHITE + (al,), width=4)
        L.text((cx, cy + 3), spec.get("mid", "VS"), font=font("Tajawal-Black", r * 0.8), fill=WHITE + (al,), anchor="mm")


# ---------------- passi ----------------
def draw_steps(lay, box, spec, lt, a=1.0):
    x1, y1, x2, y2 = box; st = spec["steps"]; n = len(st); L = ImageDraw.Draw(lay); al = int(255 * a)
    rh = (y2 - y1) / n; r = min(rh * 0.32, 56)
    for j, s in enumerate(st):
        t0 = spec.get("t", 0.2) + spec.get("gap", 0.55) * j
        if lt < t0: continue
        e = ease((lt - t0) / 0.35); aj = int(al * e); cy = y1 + rh * (j + 0.5); cx = (x2 - r - 6) if rtl() else (x1 + r + 6); dx = 30 * (1 - e)
        if j < n - 1 and lt > t0 + 0.3:
            L.line([(cx, cy + r), (cx, cy + rh - r)], fill=(80, 84, 96, aj), width=6)
        done = lt > t0 + spec.get("check_after", 0.45)
        L.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(GREEN if done else CARD) + (aj,), outline=GREEN + (aj,), width=5)
        if done: paste(lay, icon("check", int(r * 1.2), WHITE, 3), cx, cy, aj / 255)
        else: L.text((cx, cy + 3), str(j + 1), font=font("Tajawal-Black", r * 1.0), fill=WHITE + (aj,), anchor="mm")
        lab = s if isinstance(s, str) else s[0]
        f = fit(L, lab, "Tajawal-ExtraBold", min(rh * 0.36, 58), (x2 - x1) - r * 2 - 60)
        if rtl(): L.text((cx - r - 34 - dx, cy + 2), lab, font=f, fill=WHITE + (aj,), anchor="rm")
        else: L.text((cx + r + 34 + dx, cy + 2), lab, font=f, fill=WHITE + (aj,), anchor="lm")
        if not isinstance(s, str) and len(s) > 1:
            L.text((x1, cy + 2) if rtl() else (x2, cy + 2), s[1], font=font("Tajawal-Black", min(rh * 0.38, 60)), fill=GOLD + (aj,),
                   anchor="lm" if rtl() else "rm")


DRAW = {"map": draw_map, "people": draw_people, "icons": draw_icons, "bars": draw_bars, "calendar": draw_calendar,
        "vs": draw_vs, "steps": draw_steps}


def draw(lay, box, spec, lt, a=1.0):
    DRAW[spec["type"]](lay, box, spec, lt, a)
