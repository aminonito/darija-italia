"""Ponte tra i modelli grafici (visuals.py: mappe, personaggi, icone, barre, calendario, confronto, passi)
e il motore dei video lunghi 16:9 di ITALIA TIMES (wide.py / render_wide.py).

Uso in scenes.py (dopo `from wide import *`):
    import sys; sys.path.insert(0, "/home/claude/darija-italia/engine")
    import bridge_italia_times
poi, dentro build():
    sc.vis("map", T("Lombardia"), view="north", hl=["Lombardia"], pins=["Milano"])
    sc.vis("people", a, people=["office", "woman"], say=[dict(who=0, text="Quanto pago?", at=0.5)])
    sc.vis("icons", T("documenti"), items=[["id", "Documento"], ["file-text", "Modulo"]], box=(960, 200, 1800, 860))
Campi di ogni modello: engine/MODELLI.md. Box default (160, 170, 1760, 880) — area utile 150-880.
"""
import os
import dark, wide
import visuals as V

V.configure(lang="it",
            fonts={"Tajawal-Black": dark.PB, "Tajawal-ExtraBold": dark.PB, "Tajawal-Bold": dark.PS, "Tajawal-Medium": dark.PS},
            accent=dark.GREEN)
V.GREEN = (0, 166, 81)

DEFAULT_BOX = (160, 170, 1760, 880)


def _vis(self, kind, t0, t1=None, box=DEFAULT_BOX, sfx="soft", **spec):
    if kind not in V.DRAW: raise KeyError(f"modello '{kind}' sconosciuto: {sorted(V.DRAW)}")
    it = self._add(k="vis", spec=dict(spec, type=kind), t0=t0, t1=t1, box=tuple(box))
    if sfx: self.sfx.append((t0, sfx))
    return it


wide.Scene.vis = _vis
_orig = wide.render_items


def render_items(layer, sc, t, logo=None):
    _orig(layer, sc, t, logo)
    for it in sc.items:
        if it.get("k") != "vis": continue
        a = wide._alpha(it, t)
        if a > 0.01: V.draw(layer, it["box"], it["spec"], t - it["t0"], a)


wide.render_items = render_items
