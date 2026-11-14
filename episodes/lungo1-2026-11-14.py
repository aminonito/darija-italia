import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-14.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo1-2026-11-14")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = dict(JOB["blocks"])
T["C"] = T["C"].replace(" ولكن رد البال: هاد الضريبة ما كتشملش الزيادة ديال تجديد الكونطرا الوطني، ولا خدمة الليل، ولا الأعياد، ولا السوايع الزايدين.", "")  # frase tagliata dall'audio (eccezioni non confermate da 2 fonti)

S_U30 = "Ddl Bilancio 2027 (non ancora legge) · InformazioneFiscale 31/10/2026 · PrestitiOnline 5/11/2026 · QuiFinanza 29/10/2026"
S_ADI = "Calendario INPS (msg 214/2026) · QuiFinanza 29/10/2026 · InformazioneFiscale 9/11/2026"
S_OCSE = "OCSE International Migration Outlook 2026 (12/11/2026) · ANSA 12/11/2026 · AgenSIR 12/11/2026"
S_MRE = "Office des Changes (fin septembre 2026) · L'ODJ 31/10/2026 · H24info/MAP 31/10/2026"
S_HOME = "مغاربة إيطاليا · خبار مفيدة بالدارجة"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850)

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="00 · خبار اليوم", src=S_HOME, items=[
   dict(k="head", text="ربعة خبار مفيدة", at=0.2, until="الخبر الأول للشباب", sub="السبت 14 نونبر 2026"),
   dict(k="people", at=0.6, until="الخبر الأول للشباب", box=(160, 330, 1760, 860), people=["worker", "hijab", "elder"],
        say=[dict(who=1, text="شنو الجديد هاد السيمانة؟", at=0.6), dict(who=0, text="ربعة خبار", at=2.0, bg="green")]),
   dict(k="rows", at="الخبر الأول للشباب", until="يالاه نبداو", y=330, gap=125, size=50, rows=[
     ("ضريبة على الزيادة للشباب (مشروع)", "1%", "الخبر الأول للشباب"),
     ("لاسينيو دي إنكلوزيوني: الشحنة", "27/11", "التاني: لاسينيو"),
     ("تقرير: اللي دخلو عند العائلة", "67%", "التالت: تقرير"),
     ("تحويلات المغاربة ديال الخارج", "103 Mrd DH", "والرابع من"),
   ]),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Milano", "Casablanca"], pins=["Roma", "Rabat"], labels=False, at="يالاه نبداو", box=(160, 200, 1760, 880)),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="01 · ضريبة الزيادة للشباب", src=S_U30, items=[
   dict(k="chapter", num="01", title="ضريبة الزيادة للشباب", at=0.1, until="مشروع قانون"),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="مشروع قانون", until="إلى كان عمرك", box=R_BOX),
   dict(k="text", text="مشروع الميزانية 2027", at="مشروع قانون", until="إلى كان عمرك", x=560, y=470, size=66, color=GOLD),
   dict(k="text", text="فالبرلمان · ماشي قانون باقي", at="مشروع قانون", until="إلى كان عمرك", x=560, y=570, size=46, color=GREY),
   dict(k="head", text="شكون يستافد؟", at="إلى كان عمرك", until="الزيادة اللي يعطيك", sub="الشروط حسب المشروع"),
   dict(k="icons", at="إلى كان عمرك", until="الزيادة اللي يعطيك", box=(160, 330, 1760, 860), items=[
     ["user", "تحت 30 عام", "gold"], ["briefcase", "خدام مع معلم", "blue"], ["wallet", "حتى 28.000 €", "green"]], gap=2.2),
   dict(k="people", at="الزيادة اللي يعطيك", until="ضريبة غير", box=(160, 300, 1760, 860), people=["office", "worker"],
        say=[dict(who=0, text="عندك زيادة", at=0.5), dict(who=1, text="شحال غادي نخلص عليها؟", at=2.2, bg="green")]),
   dict(k="big", text="1%", at="ضريبة غير", until="المعلم يقدر", y=470, size=300, color=GREEN, sub="على الزيادة حتى 2.500 € فالعام"),
   dict(k="vs", at="المعلم يقدر", box=(260, 220, 1660, 820),
        right=dict(title="مرة وحدة", value="2.500 €", icon="cash", color="gold"),
        left=dict(title="مقسومة", value="12 شهر", icon="calendar", color="green"), gap=1.5),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="01 · ضريبة الزيادة للشباب", src=S_U30, items=[
   dict(k="head", text="مثال من عندنا", at=0.1, until="بالضريبة العادية", sub="شاب 25 عام · زيادة 2.000 € فالعام"),
   dict(k="people", at=0.3, until="بالضريبة العادية", box=(160, 330, 1760, 860), people=["worker"],
        say=[dict(who=0, text="المعلم زادني ألفين", at=1.2, bg="green")]),
   dict(k="vs", at="بالضريبة العادية", until="يعني كيبقاو", box=(260, 220, 1660, 820),
        right=dict(title="الضريبة العادية", value="460 €", sub="23% × 2.000 €", icon="receipt-tax", color="red"),
        left=dict(title="المشروع الجديد", value="20 €", sub="1% × 2.000 €", icon="receipt-tax", color="green"), gap=3.5),
   dict(k="big", text="+440 €", at="يعني كيبقاو", until="وأهم حاجة", y=470, size=260, color=GREEN, sub="حساب تقريبي على زيادة 2.000 €"),
   dict(k="calendar", at="وأهم حاجة", box=R_BOX, day=31, month=12, sub="آخر أجل للمصادقة"),
   dict(k="text", text="باقي مشروع فالبرلمان", at="وأهم حاجة", x=560, y=460, size=64, color=RED),
   dict(k="text", text="يقدر يتبدل قبل 31/12", at="وأهم حاجة", x=560, y=560, size=50, color=GREY),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="02 · لاسينيو دي إنكلوزيوني", src=S_ADI, items=[
   dict(k="chapter", num="02", title="لاسينيو دي إنكلوزيوني", at=0.1, until="هاد المساعدة"),
   dict(k="people", at="هاد المساعدة", until="فشهر نونبر", box=(160, 300, 1760, 860), people=["hijab", "clerk"],
        say=[dict(who=0, text="إمتى تجي الفلوس؟", at=0.4), dict(who=1, text="الإيزي حتى 10.140 €", at=2.6, bg="green")]),
   dict(k="map", view="italy", pins=["Torino", "Napoli", "Palermo"], labels=False, at="فشهر نونبر", until="اللي دار طلب", box=R_BOX),
   dict(k="text", text="جوج مواعيد فنونبر", at="فشهر نونبر", until="اللي دار طلب", x=560, y=500, size=72, color=GOLD),
   dict(k="calendar", at="اللي دار طلب", until="واللي كياخدها", box=R_BOX, day=13, month=11, sub="الخلاص الأول · طلب جديد"),
   dict(k="text", text="طلب جديد + الاتفاق الرقمي", at="اللي دار طلب", until="واللي كياخدها", x=560, y=500, size=56, color=GOLD),
   dict(k="calendar", at="واللي كياخدها", until="رد البال: أول", box=R_BOX, day=27, month=11, sub="الشحنة ديال الشهر"),
   dict(k="text", text="اللي كياخدها ديجا", at="واللي كياخدها", until="رد البال: أول", x=560, y=500, size=66, color=GREEN),
   dict(k="big", text="50%", at="رد البال: أول", until="وباش ما", y=470, size=280, color=GOLD, sub="أول شحنة من بعد التجديد"),
   dict(k="steps", at="وباش ما", box=(160, 230, 1760, 820), steps=[
     ["إيزي 2026 صالح", "ISEE"], ["دخل للسيت ديال الإينبس", "INPS"], ["شوف الحالة بالسبيد", "SPID"]], gap=2.5, check_after=1.0),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="03 · تقرير: علاش كيجيو لإيطاليا", src=S_OCSE, items=[
   dict(k="chapter", num="03", title="تقرير: علاش كيجيو؟", at=0.1, until="خرج نهار"),
   dict(k="calendar", at="خرج نهار", until="فإيطاليا، فعام", box=R_BOX, day=12, month=11, sub="تقرير OCSE"),
   dict(k="text", text="منظمة التعاون الاقتصادي", at="خرج نهار", until="فإيطاليا، فعام", x=560, y=500, size=56, color=GOLD),
   dict(k="map", view="med", hl=["ITA"], pins=["Roma", "Milano"], labels=False, at="فإيطاليا، فعام", until="دخلو تقريبا", box=(160, 200, 1760, 880)),
   dict(k="big", text="249.000", at="دخلو تقريبا", until="يعني زيادة ديال ستة", y=470, size=250, color=GOLD, sub="دخلو فـ2025 باش يستقرو"),
   dict(k="big", text="+46%", at="يعني زيادة ديال ستة", until="وعلاش جاو", y=470, size=280, color=GREEN, sub="على عام 2024"),
   dict(k="head", text="علاش جاو؟", at="وعلاش جاو", until="يعني تقريبا جوج", sub="فـ2025 · حسب OCSE"),
   dict(k="bars", at="سبعة وستين", until="يعني تقريبا جوج", box=(160, 380, 1760, 820), bars=[
     ["العائلة", 67, "67%", "green"], ["الاتحاد الأوروبي", 15, "15%", "grey"], ["الخدمة", 13, "13%", "gold"], ["إنسانية", 5, "5%", "grey"]], gap=1.6),
   dict(k="people", at="يعني تقريبا جوج", until="وزيد، المرسوم", box=(160, 300, 1760, 860), people=["man", "woman", "child"],
        say=[dict(who=0, text="جبت العائلة عندي", at=0.6, bg="green")]),
   dict(k="big", text="497.550", at="وزيد، المرسوم", until="إلى بغيتي", y=470, size=240, color=GREEN, sub="ديكريتو فلوسي · 2026-2028 · تلات سنين"),
   dict(k="steps", at="إلى بغيتي", box=(160, 230, 1760, 820), steps=[
     ["الشروط", "1"], ["الوراق", "2"], ["المدة", "3"]], gap=1.2, check_after=0.6),
 ]),
 dict(audio="F.wav", text=T["F"], chapter="04 · تحويلات المغاربة", src=S_MRE, items=[
   dict(k="chapter", num="04", title="تحويلات المغاربة", at=0.1, until="حسب مكتب"),
   dict(k="map", view="med", hl=["MAR"], route=["Milano", "Casablanca"], pins=["Rabat"], labels=False, at="حسب مكتب", until="فنفس المدة", box=(160, 200, 1760, 880)),
   dict(k="bars", at="فنفس المدة", until="يعني زيادة", box=(160, 380, 1760, 820), bars=[
     ["2025 · 9 شهور", 92.62, "92,62 Mrd DH", "grey"], ["2026 · 9 شهور", 103, "+103 Mrd DH", "green"]], gap=2.0),
   dict(k="head", text="مليار درهم", at="فنفس المدة", until="يعني زيادة", sub="يناير حتى شتنبر"),
   dict(k="big", text="+11,3%", at="يعني زيادة", until="وإلى قسمناها", y=470, size=280, color=GREEN, sub="على نفس المدة ديال 2025"),
   dict(k="big", text="+11 Mrd DH", at="وإلى قسمناها", until="ونصيحة صغيرة", y=470, size=220, color=GOLD, sub="فالشهر تقريبا · على 9 شهور"),
   dict(k="people", at="ونصيحة صغيرة", box=(160, 300, 1760, 860), people=["man", "elder"],
        say=[dict(who=0, text="قارن قبل ما تصيفط", at=0.5, bg="green"), dict(who=1, text="الثمن والصرف", at=2.4)]),
 ]),
 dict(audio="G.wav", text=T["G"], chapter="05 · ملخص اليوم", src=S_HOME, items=[
   dict(k="head", text="ملخص اليوم", at=0.1, until="ونتا، شنو"),
   dict(k="rows", at="واحد: ضريبة", until="ونتا، شنو", y=330, gap=125, size=50, rows=[
     ("ضريبة على الزيادة · تحت 30 · مشروع", "1%", "واحد: ضريبة"),
     ("لاسينيو دي إنكلوزيوني", "27/11", "جوج: لاسينيو"),
     ("دخلو عند العائلة · OCSE", "67%", "تلاتة: سبعة"),
     ("تحويلات المغاربة · 9 شهور", "+103 Mrd DH", "وربعة: تحويلات"),
   ]),
   dict(k="people", at="ونتا، شنو", until="وإلى عجبك", box=(160, 300, 1760, 860), people=["woman", "worker"],
        say=[dict(who=0, text="كتب لينا فالكومونتير", at=0.6, bg="green")]),
   dict(k="cta", at="وإلى عجبك", text="ابوني فالقناة", sub="كل نهار خبر مفيد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("ضريبة صغيرة على الزيادة", (236, 196, 96)), "للشباب تحت 30 عام", "ولاسينيو 27 نونبر"],
  num="1%", numsub="مشروع الميزانية 2027",
  bottom="مغاربة إيطاليا · خبار مفيدة بالدارجة",
)
