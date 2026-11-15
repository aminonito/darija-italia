import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-15.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo1-2026-11-15")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = dict(JOB["blocks"])

S_RED = "INPS messaggio 3697 del 12/11/2026 · QuiFinanza 14/11/2026 · Fanpage 14/11/2026"
S_BNN = "INPS scheda Bonus nuovi nati (circ. 45/2026) · InformazioneFiscale · QuiFinanza"
S_DOU = "Douane marocaine (ADII) · demarchesmaroc.com agg. 15/10/2026 · Bladi.net 9/12/2025 · Fes News 9/11/2026"
S_HOME = "مغاربة إيطاليا · خبار مفيدة بالدارجة"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850)

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="00 · خبار اليوم", src=S_HOME, items=[
   dict(k="head", text="تلاتة خبار مفيدة", at=0.2, until="الخبر الأول للمتقاعدين", sub="الحد 15 نونبر 2026"),
   dict(k="people", at=0.6, until="الخبر الأول للمتقاعدين", box=(160, 330, 1760, 860), people=["elder", "hijab", "man"],
        say=[dict(who=1, text="شنو الجديد اليوم؟", at=0.6), dict(who=0, text="تلاتة خبار", at=2.2, bg="green")]),
   dict(k="rows", at="الخبر الأول للمتقاعدين", until="يالاه نبداو", y=330, gap=125, size=50, rows=[
     ("تصريح الريد عند الإينبس", "1/3/2027", "الخبر الأول للمتقاعدين"),
     ("بونوس المولود الجديد", "1.000 €", "الخبر التاني للعائلات"),
     ("الديوانة: طوموبيل المتقاعدين", "-90%", "والخبر التالت"),
   ]),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Milano", "Casablanca"], pins=["Roma", "Rabat"], labels=False, at="يالاه نبداو", box=(160, 200, 1760, 880)),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="01 · المتقاعدين: تصريح الريد", src=S_RED, items=[
   dict(k="chapter", num="01", title="المتقاعدين: تصريح الريد", at=0.1, until="خرجات رسالة"),
   dict(k="calendar", at="خرجات رسالة", until="شكون المعني", box=R_BOX, day=12, month=11, sub="رسالة الإينبس 3697"),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="خرجات رسالة", until="شكون المعني", box=L_BOX),
   dict(k="people", at="شكون المعني", until="الكواتورديتشيزيما", box=(160, 300, 1760, 860), people=["elder", "clerk"],
        say=[dict(who=0, text="واش أنا معني؟", at=0.3), dict(who=1, text="شوف شنو خديتي", at=1.6, bg="green")]),
   dict(k="head", text="شكون خاصو يصرح؟", at="الكواتورديتشيزيما", until="هاد الفلوس كلها", sub="اللي خدا واحد من هادو فـ2025"),
   dict(k="icons", at="الكواتورديتشيزيما", until="هاد الفلوس كلها", box=(160, 330, 1760, 860), items=[
     ["coin-euro", "الكواتورديتشيزيما", "gold"], ["users", "بانسيون الورثة", "blue"], ["trending-up", "الزيادة الاجتماعية", "green"], ["wallet", "التكميل للحد الأدنى", "gold"]], gap=1.6),
   dict(k="people", at="هاد الفلوس كلها", until="آخر أجل", box=(160, 300, 1760, 860), people=["elder", "woman"],
        say=[dict(who=0, text="المدخول ديالي", at=0.4), dict(who=1, text="وديال العائلة", at=2.0, bg="green")]),
   dict(k="calendar", at="آخر أجل", until="تقدر ديرها", box=R_BOX, day=1, month=3, sub="آخر أجل · 2027"),
   dict(k="text", text="تصريح الريد 2026", at="آخر أجل", until="تقدر ديرها", x=560, y=470, size=66, color=GOLD),
   dict(k="text", text="المدخول ديال 2025", at="آخر أجل", until="تقدر ديرها", x=560, y=570, size=48, color=GREY),
   dict(k="steps", at="تقدر ديرها", box=(160, 230, 1760, 820), steps=[
     ["السيت ديال الإينبس", "SPID / CIE"], ["التطبيق", "App"], ["الكاف ولا الباطرونا", "CAF"]], gap=1.8, check_after=0.8),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="01 · المتقاعدين: تصريح الريد", src=S_RED, items=[
   dict(k="head", text="الإينبس كتسترجع الفلوس", at=0.1, until="الاقتطاع كيبدا", sub="الكواتورديتشيزيما ديال 2024"),
   dict(k="people", at=0.3, until="الاقتطاع كيبدا", box=(160, 330, 1760, 860), people=["elder", "office"],
        say=[dict(who=1, text="المدخول كان فوق الحد", at=1.0), dict(who=0, text="شنو غادي يوقع؟", at=3.0, bg="green")]),
   dict(k="map", view="italy", pins=["Torino", "Bologna", "Napoli"], labels=False, at="الاقتطاع كيبدا", until="ولكن كاين حد", box=R_BOX),
   dict(k="text", text="من بانسيون دجنبر", at="الاقتطاع كيبدا", until="ولكن كاين حد", x=560, y=470, size=66, color=GOLD),
   dict(k="text", text="بانسيون الورثة: من يناير 2027", at="الاقتطاع كيبدا", until="ولكن كاين حد", x=560, y=570, size=46, color=GREY),
   dict(k="vs", at="ولكن كاين حد", until="مثال من عندنا", box=(260, 220, 1660, 820),
        right=dict(title="أكثر اقتطاع", value="1/5", sub="من البانسيون فالشهر", icon="percentage", color="gold"),
        left=dict(title="مقسوم حتى", value="60", sub="قسط فالشهر", icon="calendar", color="green"), gap=2.5),
   dict(k="bars", at="مثال من عندنا", until="الإينبس كتصيفط", box=(160, 380, 1760, 820), bars=[
     ["البانسيون", 900, "900 €", "grey"], ["أكثر اقتطاع", 180, "180 €", "red"]], gap=2.0),
   dict(k="head", text="مثال من عندنا", at="مثال من عندنا", until="الإينبس كتصيفط", sub="البانسيون ÷ 5"),
   dict(k="steps", at="الإينبس كتصيفط", until="وما تنساش", box=(160, 230, 1760, 820), steps=[
     ["رسالة بالبيك ولا البريد المضمون", "PEC"], ["شوف الحساب", "1"], ["طلب المراجعة", "30"]], gap=2.2, check_after=0.8),
   dict(k="calendar", at="وما تنساش", box=R_BOX, day=1, month=12, sub="الطريديتشيزيما"),
   dict(k="text", text="الطريديتشيزيما ديال المتقاعدين", at="وما تنساش", x=560, y=470, size=56, color=GOLD),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="02 · ألف أورو للمولود الجديد", src=S_BNN, items=[
   dict(k="chapter", num="02", title="ألف أورو للمولود الجديد", at=0.1, until="عندك الحق"),
   dict(k="people", at="عندك الحق", until="مرة وحدة", box=(160, 300, 1760, 860), people=["woman", "child", "man"],
        say=[dict(who=0, text="تزاد لينا ولد", at=0.2), dict(who=2, text="ألف أورو", at=1.8, bg="green")]),
   dict(k="big", text="1.000 €", at="مرة وحدة", until="الشرط الأول", y=470, size=260, color=GREEN, sub="مرة وحدة · بلا ضريبة"),
   dict(k="head", text="الشروط", at="الشرط الأول", until="والأجانب داخلين", sub="المواليد ديال 2026"),
   dict(k="icons", at="الشرط الأول", until="والأجانب داخلين", box=(160, 330, 1760, 860), items=[
     ["calculator", "الإيزي حتى 40.000 €", "gold"], ["baby-carriage", "لاسينيو أونيكو ما كيتحسبش", "green"], ["home", "ساكن فإيطاليا بلا انقطاع", "blue"]], gap=3.0),
   dict(k="map", view="italy", pins=["Milano", "Bologna", "Roma"], labels=False, at="والأجانب داخلين", until="ولكن قبل", box=R_BOX),
   dict(k="text", text="الأجانب داخلين", at="والأجانب داخلين", until="ولكن قبل", x=560, y=430, size=66, color=GOLD),
   dict(k="text", text="الكارطا ديال المدة الطويلة", at="والأجانب داخلين", until="ولكن قبل", x=560, y=530, size=46, color=WHITE),
   dict(k="text", text="بيرميسو ديال الخدمة", at="والأجانب داخلين", until="ولكن قبل", x=560, y=610, size=46, color=WHITE),
   dict(k="people", at="ولكن قبل", box=(160, 300, 1760, 860), people=["hijab", "clerk"],
        say=[dict(who=0, text="البيرميسو ديالي داخل؟", at=0.3), dict(who=1, text="سول الباطرونا", at=1.8, bg="green")]),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="02 · ألف أورو للمولود الجديد", src=S_BNN, items=[
   dict(k="big", text="120", at=0.1, until="مثال من عندنا", y=470, size=300, color=GOLD, sub="يوم من نهار الزيادة · من بعد يضيع الحق"),
   dict(k="calendar", at="مثال من عندنا", until="الطلب كيديرو", box=R_BOX, day=20, month=3, sub="آخر أجل · 2027"),
   dict(k="text", text="تزاد نهار 20/11/2026", at="مثال من عندنا", until="الطلب كيديرو", x=560, y=470, size=60, color=WHITE),
   dict(k="text", text="من بعد 120 يوم", at="مثال من عندنا", until="الطلب كيديرو", x=560, y=570, size=56, color=GOLD),
   dict(k="steps", at="الطلب كيديرو", until="خاصك إيزي", box=(160, 230, 1760, 820), steps=[
     ["السيت ديال الإينبس", "SPID / CIE"], ["التطبيق", "App"], ["الباطرونا", "Patronato"]], gap=1.8, check_after=0.8),
   dict(k="icons", at="خاصك إيزي", until="وإلى جاوك", box=(160, 300, 1760, 860), items=[
     ["file-certificate", "إيزي صالح", "gold"], ["credit-card", "الإيبان", "green"]], gap=1.5),
   dict(k="people", at="وإلى جاوك", box=(160, 300, 1760, 860), people=["woman", "child", "girl"],
        say=[dict(who=0, text="جوج طلبات", at=0.6, bg="green")]),
 ]),
 dict(audio="F.wav", text=T["F"], chapter="03 · المغرب: الديوانة للمتقاعدين", src=S_DOU, items=[
   dict(k="chapter", num="03", title="المغرب: الديوانة للمتقاعدين", at=0.1, until="الديوانة المغربية"),
   dict(k="map", view="med", hl=["MAR"], route=["Genova", "Tanger", "ship"], pins=["Casablanca"], labels=False, at="الديوانة المغربية", until="تخفيض ديال", box=(160, 200, 1760, 880)),
   dict(k="big", text="-90%", at="تخفيض ديال", until="الشروط:", y=470, size=280, color=GREEN, sub="على الحقوق والرسوم ديال الطوموبيل"),
   dict(k="people", at="الشروط:", until="الطوموبيل خاص", box=R_BOX, people=["elder"],
        say=[dict(who=0, text="عندي 62 عام", at=0.4, bg="green")]),
   dict(k="icons", at="الشروط:", until="الطوموبيل خاص", box=L_BOX, items=[
     ["user", "60 عام ولا كثر", "gold"], ["world", "10 سنين برا", "green"], ["home", "ما رجعتيش تستقر", "blue"]], gap=1.8),
   dict(k="icons", at="الطوموبيل خاص", until="والحساب كيكون", box=(160, 330, 1760, 860), items=[
     ["car", "أقل من 10 سنين", "gold"], ["users", "9 بلايص ولا أقل", "green"]], gap=2.0),
   dict(k="bars", at="والحساب كيكون", box=(160, 380, 1760, 820), bars=[
     ["القيمة ديال الطوموبيل جديدة", 300, "300.000 DH", "green"], ["اللي فوق: الرسوم كاملين", 120, "100%", "red"]], gap=3.0),
   dict(k="head", text="الحد ديال القيمة", at="والحساب كيكون", sub="القيمة وهي جديدة"),
 ]),
 dict(audio="G.wav", text=T["G"], chapter="03 · المغرب: الديوانة للمتقاعدين", src=S_DOU, items=[
   dict(k="vs", at=0.1, until="الطلب كتديرو", box=(260, 220, 1660, 820),
        right=dict(title="مرة وحدة", value="1", sub="فالعمر", icon="certificate", color="gold"),
        left=dict(title="ما تبيعهاش", value="5", sub="سنين", icon="car", color="red"), gap=2.0),
   dict(k="map", view="med", hl=["MAR"], pins=["Tanger", "Casablanca", "Nador"], labels=False, at="الطلب كتديرو", until="الوراق:", box=R_BOX),
   dict(k="people", at="الطلب كتديرو", until="الوراق:", box=L_BOX, people=["elder"],
        say=[dict(who=0, text="بنفسي، بلا وكالة", at=0.6, bg="red")]),
   dict(k="head", text="الوراق", at="الوراق:", until="وهادا هو الملخص", sub="فمكتب الديوانة"),
   dict(k="icons", at="الوراق:", until="وهادا هو الملخص", box=(160, 330, 1760, 860), items=[
     ["id", "البطاقة ولا الباسبور", "gold"], ["file-certificate", "شهادة القنصلية", "green"], ["license", "الكارطا ديال الإقامة", "blue"], ["car", "الدخول المؤقت + الكارط گريز", "gold"]], gap=1.8),
   dict(k="head", text="ملخص اليوم", at="وهادا هو الملخص", until="ونتا، شنو"),
   dict(k="rows", at="واحد: تصريح", until="ونتا، شنو", y=330, gap=125, size=50, rows=[
     ("تصريح الريد عند الإينبس", "1/3/2027", "واحد: تصريح"),
     ("اقتطاع الكواتورديتشيزيما", "max 1/5", "جوج: اقتطاع"),
     ("بونوس المولود · 120 يوم", "1.000 €", "تلاتة: ألف"),
     ("الديوانة للمتقاعدين المغاربة", "-90%", "وربعة: تسعين"),
   ]),
   dict(k="people", at="ونتا، شنو", until="وإلى عجبك", box=(160, 300, 1760, 860), people=["woman", "elder"],
        say=[dict(who=0, text="كتب لينا فالكومونتير", at=0.6, bg="green")]),
   dict(k="cta", at="وإلى عجبك", text="ابوني فالقناة", sub="كل نهار خبر مفيد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("ألف أورو للمولود", (236, 196, 96)), "تصريح الريد للمتقاعدين", "والديوانة فالمغرب"],
  num="1.000 €", numsub="بونوس المولود 2026",
  bottom="مغاربة إيطاليا · خبار مفيدة بالدارجة",
)
