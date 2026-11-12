import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-12.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo1-2026-11-12")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = JOB["blocks"]

S_IST = "Istat · Prezzi al consumo, dati provvisori ottobre 2026 (30/10/2026) · Avvenire 30/10/2026"
S_GAS = "ARERA · comunicato 3/11/2026 (gas, vulnerabilità, ottobre 2026) · Open 3/11/2026"
S_CAR = "Decreto Mef-Mase (sconto accise gasolio fino al 23/11) · Sky TG24 e Tgcom24 12/11/2026 · Mimit via Teleborsa e Agenzia Nova 12/11/2026"
S_SAL = "Ipotesi di accordo Cgil-Cisl-Uil e 13 associazioni d'impresa, 12/11/2026 · BlogSicilia · TuttoLavoro24"
S_HOME = "مغاربة إيطاليا · خبار مفيدة بالدارجة"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850)

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="00 · خبار اليوم", src=S_HOME, items=[
   dict(k="head", text="الأسعار والخلصة: ربعة خبار", at=0.2, until="الخبر الأول:", sub="الخميس 12 نونبر 2026"),
   dict(k="people", at=0.6, until="الخبر الأول:", box=(160, 330, 1760, 860), people=["hijab", "worker", "elder"],
        say=[dict(who=0, text="كلشي غلا!", at=0.6), dict(who=1, text="والخلصة؟", at=1.6, bg="green")]),
   dict(k="rows", at="الخبر الأول:", until="إلى كنتي خدام،", y=360, gap=120, size=50, rows=[
     ("الغلا فأكتوبر", "5,4%", "الخبر الأول:"),
     ("الفاتورة ديال الغاز", "+9,1%", "التاني:"),
     ("خصم على المازوط", "23/11", "التالت:"),
     ("اتفاق جديد على الخلصة", "12/11", "والرابع:"),
   ]),
   dict(k="icons", at="إلى كنتي خدام،", items=[["briefcase", "الخدمة", "gold"], ["car", "الطوموبيل", "blue"], ["receipt", "الفاتورة", "red"]], gap=0.4),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="01 · الغلا فأكتوبر", src=S_IST, items=[
   dict(k="chapter", num="01", title="الغلا فأكتوبر", at=0.1, until="الغلا طلع"),
   dict(k="head", text="الغلا على العام اللي فات", at="الغلا طلع", until="شنو اللي غلا", sub="Istat · أرقام أولية"),
   dict(k="bars", at="الغلا طلع", until="شنو اللي غلا", box=(160, 380, 1760, 820), bars=[
     ["أكتوبر 2026", 5.4, "5,4%", "red"], ["شتنبر 2026", 4.2, "4,2%", "grey"]], gap=1.5),
   dict(k="head", text="شنو اللي غلا أكثر؟", at="شنو اللي غلا", until="والغلا الأساسي،", sub="على العام اللي فات"),
   dict(k="bars", at="الطاقة،", until="والغلا الأساسي،", box=(160, 360, 1760, 840), bars=[
     ["الطاقة", 31.4, "31,4%", "red"], ["الماكلة الطرية", 7.5, "7,5%", "gold"], ["القفة ديال الدار", 2.5, "2,5%", "green"]], gap=2.2),
   dict(k="big", text="2%", at="والغلا الأساسي،", y=500, size=240, color=GOLD, sub="الغلا الأساسي: بلا الطاقة والماكلة الطرية"),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="01 · الغلا فأكتوبر", src=S_IST, items=[
   dict(k="vs", at=0.1, until="علاش هادشي", box=(260, 220, 1660, 820),
        right=dict(title="أكتوبر 2025", value="100 €", sub="نفس الحوايج", icon="shopping-cart", color="grey"),
        left=dict(title="أكتوبر 2026", value="105,40 €", sub="+5,4%", icon="shopping-cart", color="red"), gap=1.5),
   dict(k="people", at="علاش هادشي", until="ورد البال:", box=(160, 300, 1760, 860), people=["office", "woman"],
        say=[dict(who=1, text="الخلصة ما طلعاتش", at=0.8), dict(who=0, text="نشوفو الخبر الرابع", at=3.0, bg="green")]),
   dict(k="calendar", at="ورد البال:", until="نصيحة:", box=R_BOX, day=17, month=11, sub="الأرقام النهائية"),
   dict(k="text", text="Istat: الأرقام الأولية يقدرو يتبدلو شوية", at="ورد البال:", until="نصيحة:", x=560, y=500, size=48),
   dict(k="head", text="نصيحة", at="نصيحة:", sub="قارن الأثمنة · شوف الفاتورة مزيان"),
   dict(k="icons", at="نصيحة:", box=(460, 330, 1460, 820), items=[["building-store", "قارن الأثمنة", "gold"], ["receipt", "شوف الفاتورة", "blue"]], gap=0.8),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="02 · الفاتورة ديال الغاز", src=S_GAS, items=[
   dict(k="chapter", num="02", title="الفاتورة ديال الغاز", at=0.1, until="قالت نهار"),
   dict(k="big", text="+9,1%", at="قالت نهار", until="هادشي كيهم", y=470, size=250, color=RED, sub="الغاز · أكتوبر على شتنبر · ARERA 3/11/2026"),
   dict(k="head", text="شكون اللي كيهمو؟", at="هادشي كيهم", until="الثمن ديال الغاز", sub="الكليان فالتوتيلا ديال الفولنيرابيليتا"),
   dict(k="big", text="2,3 M", at="تقريبا جوج مليون", until="الثمن ديال الغاز", y=540, size=200, color=GOLD, sub="كليان تقريبا"),
   dict(k="big", text="88,36 €", at="الثمن ديال الغاز", until="مثلا:", y=480, size=220, color=GOLD, sub="للميغاواط · الغاز بوحدو"),
   dict(k="vs", at="مثلا:", until="نصيحة:", box=(260, 220, 1660, 820),
        right=dict(title="قبل", value="100 €", sub="شتنبر", icon="flame", color="grey"),
        left=dict(title="دابا", value="109 €", sub="أكتوبر", icon="flame", color="red"), gap=1.2),
   dict(k="head", text="البونوس سوسيالي", at="نصيحة:", sub="كيدخل بوحدو فالفاتورة"),
   dict(k="rows", at="البونوس كيجي", y=420, gap=130, size=50, rows=[
     ("الإيزي تحت", "9.796 €", "البونوس كيجي"),
     ("جدد الإيزي كل عام", "DSU", "وخاصك غير"),
   ]),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="03 · خصم على المازوط", src=S_CAR, items=[
   dict(k="chapter", num="03", title="خصم على المازوط", at=0.1, until="ديال تقريبا"),
   dict(k="big", text="-4,88", at="ديال تقريبا", until="هاد الخصم", y=470, size=240, color=GREEN, sub="سنتيم فاللتر · غير المازوط (gasolio)"),
   dict(k="calendar", at="هاد الخصم", until="اليوم، الثمن", box=R_BOX, day=23, month=11, sub="آخر نهار ديال الخصم"),
   dict(k="text", text="ليصانص ما داخلاش", at="وليصانص ما", until="اليوم، الثمن", x=560, y=500, size=64, color=RED),
   dict(k="head", text="الثمن المتوسط فالسيلف", at="اليوم، الثمن", until="مثلا: إلى", sub="Mimit · 12/11/2026"),
   dict(k="bars", at="المازوط تقريبا", until="مثلا: إلى", box=(160, 400, 1760, 800), bars=[
     ["المازوط", 2.218, "2,218 €", "gold"], ["ليصانص", 1.978, "1,978 €", "blue"]], gap=2.0),
   dict(k="icons", at="مثلا: إلى", box=L_BOX, items=[["gas-station", "50 لتر", "gold"]]),
   dict(k="big", text="2,44 €", at="كتربح بهاد", x=1380, y=480, size=200, color=GREEN, sub="50 × 4,88 سنتيم"),
 ]),
 dict(audio="F.wav", text=T["F"], chapter="04 · اتفاق جديد على الخلصة", src=S_SAL, items=[
   dict(k="chapter", num="04", title="اتفاق على الخلصة", at=0.1, until="النقابات الكبار"),
   dict(k="people", at="النقابات الكبار", until="شنو فيه؟", box=(160, 260, 1760, 860), people=["worker", "office", "man"],
        say=[dict(who=0, text="النقابات", at=0.5), dict(who=2, text="الباطرونا: 13 جمعية", at=1.6, bg="green")]),
   dict(k="steps", at="شنو فيه؟", until="وفيه حتى", box=(160, 230, 1760, 820), steps=[
     ["الكونطراطو يتجدد ملي كيسالي", "CCNL"], ["الغلا الحقيقي ضد المتوقع", "IPCA"], ["الخلصة الأساسية كتزيد بالفرق", "+"], ["المراجعة كل عام ولا كل عامين", "1-2"]], gap=4.5, check_after=1.0),
   dict(k="icons", at="وفيه حتى", box=(160, 300, 1760, 820), items=[
     ["users", "التمثيلية", "gold"], ["alert-triangle", "السلامة", "red"], ["school", "التكوين", "green"]], gap=0.8),
 ]),
 dict(audio="G.wav", text=T["G"], chapter="04 · اتفاق جديد على الخلصة", src=S_SAL, items=[
   dict(k="head", text="مثال", at=0.1, until="إلى كانت الخلصة", sub="مثال من عندنا · ماشي رقم رسمي"),
   dict(k="vs", at=0.3, until="إلى كانت الخلصة", box=(260, 370, 1660, 860),
        right=dict(title="الغلا المتوقع", value="2%", icon="chart-bar", color="grey"),
        left=dict(title="الغلا الحقيقي", value="3%", icon="trending-up", color="red"), gap=2.0),
   dict(k="big", text="+16 €", at="إلى كانت الخلصة", until="ولكن رد", y=480, size=250, color=GREEN, sub="فالشهر · 1.600 € × 1%"),
   dict(k="warn", text="ماشي أوطوماتيكي دابا: غير ملي يتجدد الكونطراطو ديال القطاع ديالك", at="ولكن رد", until="وهادا باقي", y=520),
   dict(k="text", text="اتفاق أولي · باقي التوقيع الرسمي", at="وهادا باقي", y=520, size=64, color=GOLD),
 ]),
 dict(audio="H.wav", text=T["H"], chapter="05 · ملخص اليوم", src=S_HOME, items=[
   dict(k="head", text="ملخص اليوم", at=0.1, until="ونتا، شنو"),
   dict(k="rows", at="الغلا طلع", until="ونتا، شنو", y=380, gap=120, size=50, rows=[
     ("الغلا فأكتوبر · النهائي 17/11", "5,4%", "الغلا طلع"),
     ("الغاز ديال التوتيلا", "+9,1%", "الغاز ديال"),
     ("خصم المازوط حتى", "23/11", "المازوط فيه"),
     ("الخلصة تتبع الغلا: اتفاق أولي", "12/11", "والنقابات والباطرونا"),
   ]),
   dict(k="cta", at="ونتا، شنو", text="ابوني فالقناة", sub="كل نهار خبر مفيد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("الغلا طلع فإيطاليا", (236, 196, 96)), "الغاز والمازوط", "والخلصة؟"],
  num="5,4%", numsub="الغلا فأكتوبر 2026",
  bottom="مغاربة إيطاليا · خبار مفيدة بالدارجة",
)
