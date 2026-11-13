import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-13.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo2-2026-11-13")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = JOB["blocks"]
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850)

S_INTRO = "MIT comunicato (accordo in vigore 3/6/2025) · SicurAuto 4/4/2025 (1 anno dalla residenza) · Trasporti-Italia 5/6/2025"
S_REQ = "DGT Nord Ovest (agg. 3/6/2025, prot. 15008/23-05-2025: <6 anni, prima della residenza, definitiva) · Trasporti-Italia (art.1 e 3) · Integrazionemigranti.gov.it"
S_DOC = "DGT Nord Ovest (TT2112, dichiarazione sostitutiva, certificato medico in bollo, traduzione solo se richiesta) · SicurAuto · ComparaSemplice"
S_PASSI = "DGT Nord Ovest (PagoPA N003: 10,20 + 32,00 = 42,20 €) · ComparaSemplice (~60 giorni) · Trasporti-Italia + COS Milano (ritiro patente, restituita al Consolato)"
S_FINE = "SicurAuto + certificatimedici.it (1 anno) · DGT Nord Ovest + Integrazionemigranti (6 anni, definitiva, A/B)"

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="01 · لمن هاد الدليل", src=S_INTRO, items=[
   dict(k="head", text="تبدال البيرمي المغربي فإيطاليا", at=0.2, until="القانون الطلياني", sub="دليل عملي خطوة بخطوة · Conversione patente marocchina"),
   dict(k="people", at="القانون الطلياني", until="والخبر الزين", box=(160, 320, 1760, 860), people=["worker", "woman"],
        say=[dict(who=0, text="عندي البيرمي المغربي", at=1.0), dict(who=1, text="واش نقدر نسوق بيه؟", at=3.2, bg="green")]),
   dict(k="big", text="عام 1", at="غير عام واحد", until="من بعد هاد العام", y=430, size=210, color=GOLD, sub="كتسوق بالبيرمي المغربي من نهار الريزيدينسا · باقي من بعدو خاص التبديل"),
   dict(k="calendar", at="تلاتة يونيو", until="ولكن رد البال", box=R_BOX, day=3, month=6, sub="2025 · الاتفاق الجديد دخل فالخدمة"),
   dict(k="text", text="الاتفاق كيخدم غير للموطور والطوموبيل (A / B)", at="غير للموطور", until="فهاد الفيديو", x=360, y=470, size=60, color=WHITE),
   dict(k="chapter", num="01", title="شنو غادي نشوفو", at="فهاد الفيديو", until="تبع معايا"),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="02 · الشروط", src=S_REQ, items=[
   dict(k="chapter", num="02", title="الشروط", at=0.1, until="الشرط اللول"),
   dict(k="big", text="6 سنين", at="الشرط اللول", until="إلا دوزتي", y=440, size=220, color=GOLD, sub="خاص تكون ساكن فإيطاليا بأقل من 6 سنين من الريزيدينسا"),
   dict(k="warn", text="6 سنين ولا كثر = الاتفاق ما كيطبقش", at="إلا دوزتي", until="الشرط التاني", y=780),
   dict(k="head", text="الشرط التاني: بيرمي ديفينيتيف", at="الشرط التاني", until="الشرط التالت", sub="ماشي بروفيزوار · فالمغرب كيبقى بروفيزوار عامين"),
   dict(k="vs", at="فالمغرب", until="وهاد البيرمي", box=(260, 360, 1660, 880),
        left=dict(title="بروفيزوار", value="عامين", sub="ما كيتبدلش", icon="x", color="red"),
        right=dict(title="ديفينيتيف", value="قبل الريزيدينسا", sub="كيتبدل", icon="check", color="green"), gap=2.0),
   dict(k="head", text="الشرط التالت: بيرمي صالح", at="الشرط التالت", until="ورد البال", sub="ماشي سالات مدتو · وفيه كامل المعلومات وتاريخ الازدياد"),
   dict(k="warn", text="بيرمي متبدل من بلاد أخرى غير قابلة = ما كيتقبلش", at="ورد البال", y=760),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="03 · الوراق", src=S_DOC, items=[
   dict(k="chapter", num="03", title="الوراق اللي خاصك", at=0.1, until="اللول، الموديلو"),
   dict(k="icons", at="اللول، الموديلو", until="التالت", box=(160, 320, 1760, 840), items=[
     ["file-text", "موديلو TT 2112", "gold"], ["certificate", "تصريح على الشرف", "blue"]], gap=2.5),
   dict(k="head", text="الشهادة الطبية مهمة", at="التالت", until="الرابع", sub="بالطابع وفيها تصويرة · ماشي أقدم من 3 شهور"),
   dict(k="icons", at="الرابع", until="والسادس", box=(160, 330, 1760, 840), items=[
     ["license", "البيرمي الأصلي + فوطوكوبي", "gold"], ["id", "البيرميسو ديال الإقامة", "green"]], gap=2.2),
   dict(k="icons", at="والسادس", until="أما الترجمة", box=(460, 330, 1460, 820), items=[
     ["id", "الكارطا ناسيونال", "blue"], ["certificate", "الكودتشي فيسكالي", "gold"]], gap=1.4),
   dict(k="warn", text="الترجمة ماشي واجبة ديما: غير إلا طلبوها", at="أما الترجمة", y=900),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="04 · الخطوات والثمن", src=S_PASSI, items=[
   dict(k="chapter", num="04", title="الخطوات والثمن", at=0.1, until="الخطوة اللولة"),
   dict(k="steps", at="الخطوة اللولة", until="رد البال", box=(160, 220, 1760, 840), steps=[
     ["عمر الموديلو TT 2112 وجمع الوراق", "1"], ["خلص بـPagoPA (N003) + طابع الشهادة", "42,20 €"], ["قدم الطلب فالموطوريزاتسيوني", "UMC"]], gap=5.5, check_after=1.0),
   dict(k="head", text="رد البال: البيرمي المغربي", at="رد البال", until="وكتوقع", sub="ما كيتحيدش دابا · كيتحيد غير منين تاخد الطلياني"),
   dict(k="map", view="med", route=["Casablanca", "Milano"], hl=["MAR"], at="رد البال", until="وكتوقع", box=(160, 380, 1760, 900)),
   dict(k="big", text="42,20 €", at="المجموع تقريبا", until="زيد عليهم", y=470, size=220, color=GOLD, sub="PagoPA N003: 10,20 € + 32,00 €"),
   dict(k="rows", at="زيد عليهم", until="الخطوة التالتة", y=420, gap=130, size=54, rows=[
     ("طابع الشهادة الطبية", "16 €", "زيد عليهم", GOLD),
     ("الخلاص ديال الطبيب", "+", "والخلاص ديال الطبيب", WHITE),
   ]),
   dict(k="calendar", at="فالمعدل كيدور", until="ولكن ممكن", box=R_BOX, day=60, month="يوم", sub="فالمعدل · كيختلف من مكتب لمكتب"),
   dict(k="text", text="ممكن يطول أكثر", at="ولكن ممكن", x=360, y=500, size=72, color=GREY),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="05 · الغلطات والملخص", src=S_FINE, items=[
   dict(k="chapter", num="05", title="الغلطات اللي تبعد عليها", at=0.1, until="الغلطة اللولة"),
   dict(k="warn", text="تسوق بالبيرمي المغربي بعد عام بلا تبديل = بحال بلا بيرمي", at="الغلطة اللولة", until="الغلطة التانية", y=300),
   dict(k="warn", text="بيرمي بروفيزوار ولا خديتيه بعد الريزيدينسا", at="الغلطة التانية", until="الغلطة التالتة", y=440),
   dict(k="warn", text="فاتوك 6 سنين وما بدلتيش فالوقت", at="الغلطة التالتة", until="الغلطة الرابعة", y=580),
   dict(k="warn", text="بيرمي متبدل من بلاد غير قابلة", at="الغلطة الرابعة", until="نعاودو باختصار", y=720),
   dict(k="head", text="باختصار", at="نعاودو باختصار", until="هادشي معلومات"),
   dict(k="rows", at="نعاودو باختصار", until="هادشي معلومات", y=360, gap=108, size=48, rows=[
     ("بيرمي ديفينيتيف وقبل الريزيدينسا", "A / B", "البيرمي خاصو", WHITE),
     ("ساكن فإيطاليا بأقل من 6 سنين", "6", "أقل من ست", GOLD),
     ("التمن تقريبا", "42,20 €", "التمن تقريبا", GREEN),
     ("البيرمي المغربي كيتحيد غير فاللخر", "آخر", "والبيرمي المغربي", RED),
   ]),
   dict(k="people", at="هادشي معلومات", until="إلا عجبك", box=(160, 300, 1760, 860), people=["office", "man"],
        say=[dict(who=0, text="سير للموطوريزاتسيوني", at=0.8, bg="green"), dict(who=1, text="ولا لأوطوسكوولا", at=2.4)]),
   dict(k="cta", at="إلا عجبك", text="ابوني فالقناة", sub="كل نهار دليل جديد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("بدل البيرمي المغربي", (236, 196, 96)), "خطوة بخطوة فإيطاليا", "الوثائق والثمن والمدة"],
  num="A / B", numsub="الاتفاق من 3 يونيو 2025",
  bottom="مغاربة إيطاليا · دليل عملي بالدارجة",
)
