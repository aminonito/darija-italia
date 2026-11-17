import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-17.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo1-2026-11-17-final")
R2 = json.load(open(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-17-r3.json"), encoding="utf-8"))
JOB["blocks"].update(R2["blocks"])
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = {k: v.replace("گ", "ك") for k, v in JOB["blocks"].items()}

S_INF = "Istat 17/11/2026 · ANSA · LaPresse · Tgcom24"
S_BON = "Istat 17/11/2026 · ANSA · ARERA (bonus sociale)"
S_IRP = "Ddl Bilancio 2027 (non ancora legge) · Altroconsumo · Trend Online 6/11/2026"
S_IST = "Istat, Cittadini non comunitari 2025 (22/10/2026) · LaC News24"
S_HOME = "مغاربة إيطاليا · خبار مفيدة بالدارجة"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850)

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="00 · خبار اليوم", src=S_HOME, items=[
   dict(k="head", text="تلاتة خبار مفيدة", at=0.2, until="الخبر الأول على", sub="التلاتا 17 نونبر 2026"),
   dict(k="people", at=0.6, until="الخبر الأول على", box=(160, 330, 1760, 860), people=["woman", "man", "worker"],
        say=[dict(who=0, text="شنو الجديد اليوم؟", at=0.6), dict(who=1, text="تلاتة خبار", at=2.4, bg="green")]),
   dict(k="rows", at="الخبر الأول على", until="وفكل خبر", y=330, gap=125, size=50, rows=[
     ("الغلا فأكتوبر: الرقم النهائي", "5,5%", "الخبر الأول على"),
     ("الضريبة 2027: شكون يربح؟", "500 €", "الخبر التاني للي"),
     ("المغاربة والبيرميسوات الجداد", "1", "والخبر التالت"),
   ]),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Milano", "Casablanca"], pins=["Roma", "Rabat"], labels=False, at="وفكل خبر", box=(160, 200, 1760, 880)),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="01 · الغلا فأكتوبر", src=S_INF, items=[
   dict(k="chapter", num="01", title="الغلا فأكتوبر", at=0.1, until="أكدات الرقم"),
   dict(k="calendar", at="أكدات الرقم", until="التقدير الأول", box=R_BOX, day=17, month=11, sub="الإستات · الرقم النهائي"),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="أكدات الرقم", until="التقدير الأول", box=L_BOX),
   dict(k="bars", at="التقدير الأول", until="وفشهر واحد", box=(160, 330, 1760, 840), bars=[
     ["شتنبر", 4.2, "4,2%", "grey"], ["التقدير الأول", 5.4, "5,4%", "gold"], ["الرقم النهائي", 5.5, "5,5%", "red"]], gap=1.6),
   dict(k="head", text="الغلا على عام", at="التقدير الأول", until="وفشهر واحد", sub="أكتوبر 2026"),
   dict(k="big", text="1%", at="وفشهر واحد", until="شنو اللي طلع", y=470, size=260, color=GOLD, sub="الأسعار فشهر واحد"),
   dict(k="people", at="شنو اللي طلع", until="الطاقة، يعني", box=(160, 300, 1760, 860), people=["hijab", "elder"],
        say=[dict(who=0, text="شنو طلع بزاف؟", at=0.2)]),
   dict(k="icons", at="الطاقة، يعني", until="والماكلة الطرية", box=(160, 330, 1760, 860), items=[
     ["bolt", "الضو", "gold"], ["flame", "الغاز", "red"], ["gas-station", "المازوط", "blue"]], gap=0.9),
   dict(k="bars", at="والماكلة الطرية", until="وهادشي غادي", box=(160, 330, 1760, 840), bars=[
     ["الطاقة", 31.9, "31,9%", "red"], ["الماكلة الطرية", 7.5, "7,5%", "gold"], ["القفة ديال كل نهار", 2.3, "2,3%", "green"]], gap=2.2),
   dict(k="head", text="شنو طلع؟", at="والماكلة الطرية", until="وهادشي غادي", sub="على عام · أكتوبر"),
   dict(k="people", at="وهادشي غادي", box=R_BOX, people=["woman"],
        say=[dict(who=0, text="الفاتورة ديال الشتا", at=0.6, bg="red")]),
   dict(k="map", view="north", pins=["Milano", "Torino", "Bologna"], labels=False, at="وهادشي غادي", box=L_BOX),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="01 · الغلا فأكتوبر", src=S_BON, items=[
   dict(k="people", at=0.1, until="مثال من عندنا", box=(160, 300, 1760, 860), people=["man", "woman"],
        say=[dict(who=1, text="شنو كيعني ليا؟", at=0.2)]),
   dict(k="vs", at="مثال من عندنا", until="يعني مية", box=(260, 220, 1660, 820),
        right=dict(title="عام اللي فات", value="2.000 €", sub="المصروف فالشهر", icon="shopping-cart", color="grey"),
        left=dict(title="دابا", value="2.110 €", sub="نفس الحوايج", icon="shopping-cart", color="red"), gap=3.0),
   dict(k="big", text="110 €", at="يعني مية", until="نصيحة عملية", y=470, size=260, color=RED, sub="زايدين كل شهر"),
   dict(k="icons", at="نصيحة عملية", until="وقبل ما تبدل", box=(160, 330, 1760, 860), items=[
     ["receipt", "الإيزي كل عام", "gold"], ["bolt", "الضو", "green"], ["flame", "الغاز", "green"]], gap=1.5),
   dict(k="head", text="البونس الاجتماعي أوتوماتيكي", at="نصيحة عملية", until="وقبل ما تبدل", sub="ISEE ≤ 9.796 €"),
   dict(k="people", at="وقبل ما تبدل", box=R_BOX, people=["elder", "clerk"],
        say=[dict(who=0, text="نبدل الكونطرا؟", at=0.3), dict(who=1, text="قارن الثمن", at=2.0, bg="green")]),
   dict(k="map", view="south", pins=["Napoli", "Bari", "Palermo"], labels=False, at="وقبل ما تبدل", box=L_BOX),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="02 · الضريبة 2027", src=S_IRP, items=[
   dict(k="chapter", num="02", title="الضريبة 2027: شكون يربح؟", at=0.1, until="الحكومة دارت"),
   dict(k="people", at="الحكومة دارت", until="رد البال", box=(160, 300, 1760, 860), people=["worker", "man", "hijab"],
        say=[dict(who=0, text="واش غادي نربح؟", at=1.2)]),
   dict(k="people", at="رد البال", until="البرلمان خاصو", box=(160, 300, 1760, 860), people=["office", "man"],
        say=[dict(who=0, text="باقي مشروع", at=0.3, bg="red")]),
   dict(k="calendar", at="البرلمان خاصو", until="شنو كاين فيه", box=R_BOX, day=31, month=12, sub="البرلمان · آخر أجل"),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="البرلمان خاصو", until="شنو كاين فيه", box=L_BOX),
   dict(k="bars", at="اليوم، الضريبة", until="فالمشروع، التلاتة", box=(160, 330, 1760, 840), bars=[
     ["حتى 28.000 €", 23, "23%", "green"], ["حتى 50.000 €", 33, "33%", "gold"], ["فوق 50.000 €", 43, "43%", "red"]], gap=2.4),
   dict(k="head", text="الإيربيف اليوم", at="شنو كاين فيه", until="فالمشروع، التلاتة", sub="الأشطر ديال 2026"),
   dict(k="vs", at="فالمشروع، التلاتة", until="يعني التبديل", box=(260, 220, 1660, 820),
        right=dict(title="اليوم", value="50.000 €", sub="آخر حد للشطر التاني", icon="receipt-tax", color="grey"),
        left=dict(title="المشروع 2027", value="55.000 €", sub="آخر حد للشطر التاني", icon="receipt-tax", color="green"), gap=2.0),
   dict(k="big", text="50.000 - 55.000 €", at="يعني التبديل", y=470, size=150, color=GOLD, sub="غير هاد الجزء كيتبدل"),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="02 · الضريبة 2027", src=S_IRP, items=[
   dict(k="people", at=0.1, until="مثال من عندنا", box=(160, 300, 1760, 860), people=["office", "worker"],
        say=[dict(who=1, text="شكون غادي يربح؟", at=0.2), dict(who=0, text="غير الدخل الكبير", at=2.2, bg="green")]),
   dict(k="map", view="north", pins=["Brescia", "Milano"], labels=False, at="مثال من عندنا", until="وسارة عندها", box=L_BOX),
   dict(k="people", at="مثال من عندنا", until="وسارة عندها", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="ما تبدل والو", at=3.0, bg="red")]),
   dict(k="bars", at="وسارة عندها", until="ورد البال، هاد", box=(160, 330, 1760, 840), bars=[
     ["كريم · 30.000 €", 1, "0 €", "grey"], ["سارة · 53.000 €", 300, "300 €", "gold"], ["55.000 € ولا كتر", 500, "500 €", "green"]], gap=2.6),
   dict(k="head", text="شحال كتربح فالعام؟", at="وسارة عندها", until="ورد البال، هاد", sub="مثال من عندنا · مشروع"),
   dict(k="calendar", at="ورد البال، هاد", until="يعني إلى كانت", box=R_BOX, day=1, month=1, sub="غير عام 2027"),
   dict(k="map", view="south", pins=["Napoli", "Bari"], labels=False, at="ورد البال، هاد", until="يعني إلى كانت", box=L_BOX),
   dict(k="people", at="يعني إلى كانت", box=(160, 300, 1760, 860), people=["woman", "worker"],
        say=[dict(who=0, text="الخلصة كيف ما كانت", at=0.8)]),
 ]),
 dict(audio="F.wav", text=T["F"], chapter="03 · المغاربة والبيرميسو: أرقام 2025", src=S_IST, items=[
   dict(k="chapter", num="03", title="المغاربة والبيرميسو: أرقام 2025", at=0.1, until="الإستات نشرات"),
   dict(k="map", view="italy", pins=["Milano", "Torino", "Bologna", "Roma"], labels=False, at="الإستات نشرات", until="فإيطاليا تعطاو", box=(160, 200, 1760, 880)),
   dict(k="big", text="≈ 427.000", at="فإيطاليا تعطاو", until="والمغاربة هوما", y=470, size=220, color=GOLD, sub="بيرميسو جديد فـ2025"),
   dict(k="big", text="≈ 44.500", at="والمغاربة هوما", until="يعني المغرب", y=470, size=220, color=GREEN, sub="بيرميسو جديد للمغاربة"),
   dict(k="map", view="med", hl=["MAR", "ITA"], route=["Casablanca", "Milano", "plane"], pins=["Rabat"], labels=False, at="يعني المغرب", until="والسبب الأول", box=L_BOX),
   dict(k="people", at="يعني المغرب", until="والسبب الأول", box=R_BOX, people=["hijab", "man"],
        say=[dict(who=1, text="حنا اللولين", at=0.4, bg="green")]),
   dict(k="big", text="≈ 40%", at="والسبب الأول", until="وفالجنسية،", y=470, size=240, color=GOLD, sub="البيرميسوات الجداد ديال العائلة"),
   dict(k="bars", at="وفالجنسية،", until="إلى باغي", box=(160, 330, 1760, 840), bars=[
     ["الألبان", 25725, "25.725", "grey"], ["المغاربة", 23386, "23.386", "green"]], gap=2.0),
   dict(k="head", text="ولاو إيطاليين فـ2025", at="وفالجنسية،", until="إلى باغي", sub="≈ 197.000 فالمجموع"),
   dict(k="people", at="إلى باغي", box=R_BOX, people=["woman", "child"],
        say=[dict(who=0, text="شوف الفيديوهات", at=1.0, bg="green")]),
   dict(k="steps", at="إلى باغي", box=L_BOX, steps=[["التجمع العائلي", "12/11"], ["الجنسية بالإقامة", "16/11"]], gap=1.5, check_after=0.6),
 ]),
 dict(audio="G.wav", text=T["G"], chapter="04 · الملخص", src=S_HOME, items=[
   dict(k="head", text="ملخص اليوم", at=0.1, until="ونتا، شنو"),
   dict(k="rows", at="واحد: الغلا", until="ونتا، شنو", y=330, gap=125, size=50, rows=[
     ("الغلا فأكتوبر: دير الإيزي", "5,5%", "واحد: الغلا"),
     ("الضريبة 2027: باقي مشروع", "500 €", "جوج: التخفيض"),
     ("المغاربة اللولين فالبيرميسوات", "44.549", "تلاتة: المغاربة"),
   ]),
   dict(k="map", view="med", hl=["ITA", "MAR"], pins=["Milano", "Casablanca"], labels=False, at="ونتا، شنو", until="كتب لينا", box=L_BOX),
   dict(k="people", at="ونتا، شنو", until="وإلى عجبك", box=R_BOX, people=["woman", "worker"],
        say=[dict(who=0, text="كتب لينا فالكومونتير", at=1.5, bg="green")]),
   dict(k="cta", at="وإلى عجبك", text="ابوني فالقناة", sub="كل نهار خبر مفيد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("الغلا طلع فأكتوبر", (236, 196, 96)), "والضريبة 2027: شكون يربح؟", "المغاربة اللولين فالبيرميسو"],
  num="5,5%", numsub="الغلا فأكتوبر · الإستات",
  bottom="مغاربة إيطاليا · خبار مفيدة بالدارجة",
)
