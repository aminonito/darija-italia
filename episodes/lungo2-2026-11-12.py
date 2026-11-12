import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-12.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo2-2026-11-12")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = JOB["blocks"]
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850)

S_CHI = "art. 29 D.Lgs. 286/1998 · InfoImmigrazione (guida 25/06/2026) · Assolombarda (ricongiungimento)"
S_REQ = "D.L. 145/2024 conv. L. 187/2024 (2 anni) via Edotto e InfoImmigrazione · assegno sociale 2026 546,24 €/mese (Money.it, InfoImmigrazione) · GR Servizi, TuttoStranieri (formula)"
S_DOC = "Ambasciata d'Italia a Rabat (visto RF) · HCCH: Apostille in vigore per il Marocco dal 2016 · Avv. Lombardini · Assolombarda"
S_PASSI = "Assolombarda · InfoImmigrazione · UNHCR Italia (SUI, bollo 16 €, 8 giorni) · TuttoStranieri · Poste Italiane / Polizia di Stato (kit)"
S_FINE = "InfoImmigrazione · Avvocati-it · Prefettura - Sportello Unico Immigrazione"

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="01 · شكون تقدر تجيب", src=S_CHI, items=[
   dict(k="head", text="التجمع العائلي: جيب العائلة لإيطاليا", at=0.2, until="بزاف ديال الناس", sub="دليل عملي خطوة بخطوة · Ricongiungimento familiare"),
   dict(k="map", view="med", route=["Casablanca", "Milano"], pins=[], at=1.5, until="بزاف ديال الناس", box=(160, 360, 1760, 880)),
   dict(k="people", at="بزاف ديال الناس", until="شكون اللي تقدر", box=(160, 300, 1760, 860), people=["worker", "hijab", "child"],
        say=[dict(who=0, text="منين نبدا؟", at=1.2), dict(who=1, text="شحال خاصني نربح؟", at=3.0, bg="green"), dict(who=0, text="وشحال كياخد؟", at=5.0)]),
   dict(k="chapter", num="01", title="شكون تقدر تجيب", at="شكون اللي تقدر", until="اللول: المرا"),
   dict(k="icons", at="اللول: المرا", until="فهاد الفيديو", box=(160, 300, 1760, 820), items=[
     ["users", "الزوج", "gold"], ["baby-carriage", "الدراري تحت 18", "green"], ["stethoscope", "كبار مريضين", "blue"], ["home", "الوالدين على حسابك", "red"]], gap=4.5),
   dict(k="head", text="اليوم: المرا والدراري", at="فهاد الفيديو", sub="الحالة اللي كتكثر عند المغاربة"),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="02 · الشروط", src=S_REQ, items=[
   dict(k="chapter", num="02", title="الشروط", at=0.1, until="الشرط اللول"),
   dict(k="rows", at="الشرط اللول", until="الشرط التاني", y=380, gap=125, size=52, rows=[
     ("بيرميسو ديال الخدمة (عام على الأقل)", "lavoro", "الشرط اللول", WHITE),
     ("ولا بيرميسو ديال العائلة", "famiglia", "ولا ديال العائلة", WHITE),
     ("ولا الكارطا ديال الإقامة الطويلة", "UE", "ولا الكارطا", GOLD),
   ]),
   dict(k="big", text="2 سنين", at="الشرط التاني", until="أما الدراري", y=460, size=220, color=GOLD, sub="إقامة قانونية بلا انقطاع · للزوج والوالدين · D.L. 145/2024"),
   dict(k="text", text="الدراري الصغار: بلا جوج سنين", at="أما الدراري", until="الشرط التالت", y=740, size=72, color=GREEN),
   dict(k="head", text="الدخل الأدنى فالعام", at="الشرط التالت", until="الشرط الرابع", sub="assegno sociale 2026 = 7.101,12 € · +50% على كل واحد"),
   dict(k="bars", at="إلى بغيتي تجيب", until="وإلى بغيتي تجيب جوج", box=(160, 360, 1760, 840), bars=[
     ["1 واحد", 10651.68, "10.651,68 €", "green"], ["2 جوج", 14202.24, "14.202,24 €", "gold"], ["3 تلاتة", 17752.80, "17.752,80 €", "red"]], gap=4.0),
   dict(k="vs", at="وإلى بغيتي تجيب جوج", until="الشرط الرابع", box=(260, 380, 1660, 900),
        right=dict(title="واحد من العائلة", value="888 €", sub="فالشهر تقريبا", icon="wallet", color="green"),
        left=dict(title="2+ دراري تحت 14", value="14.202 €", sub="فالعام", icon="baby-carriage", color="gold"), gap=0.6),
   dict(k="icons", at="الشرط الرابع", box=(460, 330, 1460, 820), items=[["home", "الإيدونييطا ألوجاتيفا", "gold"], ["building-bank", "من الكومون", "blue"]], gap=1.5),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="03 · الوراق", src=S_DOC, items=[
   dict(k="chapter", num="03", title="الوراق اللي خاصك", at=0.1, until="من جيهتك"),
   dict(k="head", text="نتا فإيطاليا", at="من جيهتك", until="ومن جيهة العائلة", sub="فوطوكوبي + الأصلي"),
   dict(k="icons", at="من جيهتك", until="ومن جيهة العائلة", box=(160, 330, 1760, 840), items=[
     ["e-passport", "الباسبور والبيرميسو", "gold"], ["id", "الكودتشي فيسكالي", "blue"], ["home", "الإيدونييطا", "green"], ["report-money", "الكونطرا والبوسطات", "red"]], gap=1.6),
   dict(k="head", text="العائلة فالمغرب", at="ومن جيهة العائلة", until="ورد البال:", sub="الوراق المغربية"),
   dict(k="icons", at="ومن جيهة العائلة", until="ورد البال:", box=(160, 330, 1760, 840), items=[
     ["e-passport", "الباسبور", "gold"], ["certificate", "عقد الزواج", "red"], ["file-certificate", "عقد الازدياد", "green"], ["file-text", "الدفتر العائلي", "blue"]], gap=1.4),
   dict(k="warn", text="أبوستيي + ترجمة للطليانية", at="ورد البال:", until="نصيحة: جمع", y=420),
   dict(k="text", text="المغرب فنظام الأبوستيي من 2016 · السفارة فالرباط كتطلبها", at="ورد البال:", until="نصيحة: جمع", y=600, size=48, color=GREY),
   dict(k="head", text="نصيحة", at="نصيحة: جمع", sub="جمع الوراق بكري · سول الكومون على الثمن والمدة"),
   dict(k="map", view="med", hl=["MAR"], pins=["Rabat"], labels=False, at="نصيحة: جمع", box=(560, 380, 1360, 900)),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="04 · الخطوات", src=S_PASSI, items=[
   dict(k="chapter", num="04", title="الخطوات وحدة بوحدة", at=0.1, until="الخطوة اللولة"),
   dict(k="steps", at="الخطوة اللولة", until="الخطوة الرابعة", box=(160, 220, 1760, 840), steps=[
     ["الطلب أونلاين فالسبورطيلو أونيكو (سبيد)", "16 €"], ["الموعد فالبريفيتورا بالوراق الأصليين", "SUI"], ["النولا أوسطا: 150 يوم على الأكثر", "6 شهور"]], gap=6.0, check_after=1.0),
   dict(k="map", view="med", route=["Milano", "Casablanca"], pins=["Rabat"], at="الخطوة الرابعة", until="الخطوة الخامسة", box=(160, 380, 1760, 900)),
   dict(k="head", text="الفيزا ديال العائلة", at="الخطوة الرابعة", until="الخطوة الخامسة", sub="30 يوم · مرات كتطول"),
   dict(k="calendar", at="الخطوة الخامسة", until="ومن بعد كتصيفطو", box=R_BOX, day=8, month="أيام", sub="من نهار الدخول"),
   dict(k="text", text="سير للسبورطيلو أونيكو", at="الخطوة الخامسة", until="ومن بعد كتصيفطو", x=560, y=460, size=56),
   dict(k="text", text="وطلب البيرميسو ديال العائلة", at="الخطوة الخامسة", until="ومن بعد كتصيفطو", x=560, y=560, size=56, color=GOLD),
   dict(k="head", text="الكيت ديال البوسطا", at="ومن بعد كتصيفطو", until="يعني من النهار", sub="16 + 30 + 30,46 + 40/50 €"),
   dict(k="big", text="116-126 €", at="فالمجموع تقريبا", until="يعني من النهار", y=500, size=200, color=GOLD, sub="على حساب المدة ديال البيرميسو"),
   dict(k="bars", at="يعني من النهار", box=(160, 380, 1760, 820), bars=[
     ["النولا أوسطا", 150, "150 يوم", "gold"], ["الفيزا", 30, "30 يوم", "blue"], ["البيرميسو", 8, "8 أيام", "green"]], gap=1.2),
   dict(k="text", text="المجموع: تقريبا 6 شهور ولا كثر", at="يعني من النهار", y=880, size=52, color=GOLD),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="05 · الغلطات والملخص", src=S_FINE, items=[
   dict(k="chapter", num="05", title="الغلطات اللي تبعد عليها", at=0.1, until="الغلطة اللولة"),
   dict(k="warn", text="وراق مغربية بلا أبوستيي ولا ترجمة", at="الغلطة اللولة", until="نعاودو باختصار", y=300),
   dict(k="warn", text="الدخل تحت الحد ولا الكونطرا سالات", at="الغلطة التانية", until="نعاودو باختصار", y=420),
   dict(k="warn", text="الطلب بلا الإيدونييطا ديال الدار", at="الغلطة التالتة", until="نعاودو باختصار", y=540),
   dict(k="warn", text="تفوتو التمنية أيام", at="الغلطة الرابعة", until="نعاودو باختصار", y=660),
   dict(k="warn", text="زواج غير على الوراق = رفض", at="والغلطة الخامسة", until="نعاودو باختصار", y=780),
   dict(k="head", text="باختصار", at="نعاودو باختصار", until="هادشي معلومات"),
   dict(k="rows", at="نعاودو باختصار", until="هادشي معلومات", y=360, gap=110, size=48, rows=[
     ("بيرميسو صالح + 2 سنين للزوج", "2", "اللولة: بيرميسو", WHITE),
     ("الدخل لواحد من العائلة", "10.651 €", "التانية: دخل", GOLD),
     ("دار فيها الإيدونييطا", "Comune", "التالتة: دار", WHITE),
     ("الطلب أونلاين + تمبر", "16 €", "الرابعة: الطلب", WHITE),
     ("من بعد الدخول", "8", "والخامسة: تمنية", RED),
   ]),
   dict(k="people", at="هادشي معلومات", until="ونتوما، واش", box=(160, 300, 1760, 860), people=["office", "man"],
        say=[dict(who=0, text="سول فالباطروناطو", at=0.8, bg="green"), dict(who=1, text="ولا فالبريفيتورا", at=2.2)]),
   dict(k="cta", at="ونتوما، واش", text="ابوني فالقناة", sub="كل نهار دليل جديد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("جيب العائلة لإيطاليا", (236, 196, 96)), "التجمع العائلي", "خطوة بخطوة"],
  num="2026", numsub="الشروط والوراق والمدة",
  bottom="مغاربة إيطاليا · دليل عملي بالدارجة",
)
