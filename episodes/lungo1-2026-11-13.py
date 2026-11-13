import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-13.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo1-2026-11-13")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = JOB["blocks"]

S_FIC = "DGSN · portale ePolice (epolice.ma) · Le360 9/11/2026 · Le Matin 9/11/2026 · Alyaoum24 6/11/2026"
S_MAM = "Ddl Bilancio 2027 (A.C. 3174-bis, art. 57), non ancora legge · Panorama 11/11/2026 · Sbircia la Notizia 12/11/2026 · INPS (bonus 2026)"
S_AU = "Calendario INPS 2026 · Money.it 4/11/2026 · QuiFinanza 27/10/2026 · INPS circolare 7/2026"
S_HOME = "مغاربة إيطاليا · خبار مفيدة بالدارجة"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850)

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="00 · خبار اليوم", src=S_HOME, items=[
   dict(k="head", text="تلاتة خبار مفيدة", at=0.2, until="الخبر الأول جاي", sub="الجمعة 13 نونبر 2026"),
   dict(k="people", at=0.6, until="الخبر الأول جاي", box=(160, 330, 1760, 860), people=["hijab", "man", "elder"],
        say=[dict(who=0, text="شنو الجديد اليوم؟", at=0.6), dict(who=1, text="تلاتة خبار", at=1.8, bg="green")]),
   dict(k="rows", at="الخبر الأول جاي", until="إلى عندك ولاد،", y=380, gap=130, size=50, rows=[
     ("بطاقة السوابق من المغرب: أونلاين", "9/11", "الخبر الأول جاي"),
     ("بونوس الماماوات فـ2027 (مشروع)", "100 €", "التاني: البونوس"),
     ("لاسينيو أونيكو: المواعيد", "19-20/11", "والتالت: المواعيد"),
   ]),
   dict(k="icons", at="إلى عندك ولاد،", items=[["baby-carriage", "الولاد", "gold"], ["file-text", "الدوسي", "blue"], ["wallet", "الفلوس", "green"]], gap=0.4),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="01 · بطاقة السوابق أونلاين", src=S_FIC, items=[
   dict(k="chapter", num="01", title="بطاقة السوابق أونلاين", at=0.1, until="من نهار الاتنين"),
   dict(k="calendar", at="من نهار الاتنين", until="دابا تقدر", box=R_BOX, day=9, month=11, sub="بداية الخدمة"),
   dict(k="text", text="الأمن الوطني · المغرب", at="من نهار الاتنين", until="دابا تقدر", x=560, y=500, size=64, color=GOLD),
   dict(k="map", view="med", hl=["ITA", "MAR"], pins=["Roma", "Rabat"], labels=False, at="دابا تقدر", until="هاد الوثيقة،", box=(160, 200, 1760, 880)),
   dict(k="people", at="هاد الوثيقة،", until="قبل، هاد", box=(160, 300, 1760, 860), people=["clerk", "man"],
        say=[dict(who=0, text="بطاقة السوابق", at=0.4), dict(who=1, text="فين نطلبها؟", at=2.0, bg="green")]),
   dict(k="vs", at="قبل، هاد", until="دابا، الطلب", box=(260, 220, 1660, 820),
        right=dict(title="قبل", value="غير فالمغرب", icon="map-pin", color="grey"),
        left=dict(title="دابا", value="حتى من برا", icon="world", color="green"), gap=1.5),
   dict(k="big", text="ePolice", at="دابا، الطلب", y=480, size=220, color=GOLD, sub="epolice.ma · البوابة ديال البوليس المغربي"),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="01 · بطاقة السوابق أونلاين", src=S_FIC, items=[
   dict(k="steps", at="تلاتة ديال الخطوات", until="ومن بعد،", box=(160, 230, 1760, 820), steps=[
     ["عمر الطلب فإي بوليس", "1"], ["أكد الهوية ديالك إلكترونيا", "2"], ["خلص الواجبات أونلاين", "3"]], gap=3.0, check_after=1.0),
   dict(k="icons", at="ومن بعد،", until="ولكن رد البال:", items=[["clock", "تبع الطلب", "blue"], ["check", "الوثيقة واجدة", "green"]], gap=1.0),
   dict(k="warn", text="ما كتوصلكش فالإيميل: كتاخدها بيديك من القنصلية", at="ولكن رد البال:", until="يعني ختار", y=520),
   dict(k="icons", at="يعني ختار", until="شحال كتخلص", items=[["building-bank", "القنصلية", "gold"], ["map-pin", "قريبة ليك", "green"]], gap=0.6),
   dict(k="head", text="الثمن والمدة؟", at="شحال كتخلص", until="ونصيحة:", sub="المصادر ما عطاتش رقم"),
   dict(k="text", text="شوف البوابة قبل ما تبدا", at="شحال كتخلص", until="ونصيحة:", y=560, size=80, color=GOLD),
   dict(k="head", text="نصيحة", at="ونصيحة:", sub="سول الإدارة الإيطالية قبل"),
   dict(k="people", at="ونصيحة:", box=(160, 330, 1760, 860), people=["office", "hijab"],
        say=[dict(who=1, text="واش هادي هي الوثيقة؟", at=0.5), dict(who=1, text="واش خاصها ترجمة؟", at=3.0, bg="green")]),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="02 · بونوس الماماوات 2027", src=S_MAM, items=[
   dict(k="chapter", num="02", title="بونوس الماماوات 2027", at=0.1, until="فالمشروع"),
   dict(k="head", text="فالشهر", at="البونوس غادي", until="وغادي يتخلص", sub="مشروع قانون الميزانية 2027"),
   dict(k="bars", at="البونوس غادي", until="وغادي يتخلص", box=(160, 380, 1760, 820), bars=[
     ["2026", 60, "60 €", "grey"], ["2027 · مشروع", 100, "100 €", "green"]], gap=1.5),
   dict(k="big", text="300 €", at="وغادي يتخلص", until="شكون اللي", y=480, size=240, color=GREEN, sub="كل 3 شهور · حتى 1.200 € فالعام"),
   dict(k="people", at="شكون اللي", until="إلى كانو جوج،", box=(160, 300, 1760, 860), people=["hijab", "woman"],
        say=[dict(who=0, text="خدامة مع معلم", at=1.0), dict(who=1, text="خدامة لراسي", at=2.4, bg="green")]),
   dict(k="head", text="الولاد", at="إلى كانو جوج،", until="والدخل ديال", sub="الصغير تحت (عام)"),
   dict(k="rows", at="إلى كانو جوج،", until="والدخل ديال", y=440, gap=140, size=54, rows=[
     ("جوج ولاد: الصغير تحت", "10", "إلى كانو جوج،"),
     ("تلاتة ولا كثر: الصغير تحت", "18", "وإلى كانو تلاتة"),
   ]),
   dict(k="big", text="40.000 €", at="والدخل ديال", y=480, size=220, color=GOLD, sub="الحد ديال الدخل ديال الخدمة · الإيزي ما كيدخلش"),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="02 · بونوس الماماوات 2027", src=S_MAM, items=[
   dict(k="head", text="أمثلة من عندنا", at=0.1, until="ماما خدامة", sub="حسابات تقريبية · ماشي رقم رسمي"),
   dict(k="vs", at="ماما خدامة", until="يعني ربع", box=(260, 220, 1660, 820),
        right=dict(title="2026", value="720 €", sub="60 € × 12", icon="coin-euro", color="grey"),
        left=dict(title="2027 · مشروع", value="1.200 €", sub="100 € × 12", icon="coin-euro", color="green"), gap=2.0),
   dict(k="big", text="+480 €", at="يعني ربع", until="وإلى خدمات", y=480, size=250, color=GREEN, sub="1.200 − 720 فالعام"),
   dict(k="big", text="700 €", at="وإلى خدمات", until="ولكن رد البال:", y=480, size=250, color=GOLD, sub="7 شهور × 100 €"),
   dict(k="icons", at="ولكن رد البال:", until="وحاجة أخرى:", items=[["home", "الخدامات فالديور", "red"], ["baby-carriage", "ولد واحد", "red"]], gap=1.5),
   dict(k="text", text="ما داخلينش", at="ولكن رد البال:", until="وحاجة أخرى:", y=900, size=56, color=RED),
   dict(k="calendar", at="وحاجة أخرى:", until="وأهم حاجة:", box=R_BOX, day=31, month=12, sub="آخر الإعفاء ديال الكونتريبوتي"),
   dict(k="text", text="ماماوات · 3 ولاد · كونطرا دايم", at="وحاجة أخرى:", until="وأهم حاجة:", x=560, y=500, size=54, color=GOLD),
   dict(k="warn", text="باقي مشروع فالبرلمان: يقدر يتبدل", at="وأهم حاجة:", until="وديال هاد العام،", y=520),
   dict(k="big", text="31/12", at="وديال هاد العام،", y=480, size=240, color=GOLD, sub="آخر أجل للطلب ديال بونوس 2026"),
 ]),
 dict(audio="F.wav", text=T["F"], chapter="03 · لاسينيو أونيكو", src=S_AU, items=[
   dict(k="chapter", num="03", title="لاسينيو أونيكو", at=0.1, until="ديال شهر نونبر"),
   dict(k="calendar", at="ديال شهر نونبر", until="وديال دجنبر", box=R_BOX, day="19-20", month=11, sub="الخلاص ديال نونبر"),
   dict(k="text", text="اللي كياخدوه ديجا · بلا تبديل", at="ديال شهر نونبر", until="وديال دجنبر", x=560, y=500, size=54, color=GOLD),
   dict(k="calendar", at="وديال دجنبر", until="والمبلغ ما", box=R_BOX, day="16-17", month=12, sub="قبل العيد ديال آخر العام"),
   dict(k="text", text="دجنبر: بكري", at="وديال دجنبر", until="والمبلغ ما", x=560, y=500, size=80, color=GREEN),
   dict(k="head", text="شحال للولد فالشهر؟", at="والمبلغ ما", until="شكون اللي يقدر", sub="ولد تحت 18 عام · على حساب الإيزي"),
   dict(k="bars", at="والمبلغ ما", until="شكون اللي يقدر", box=(160, 380, 1760, 820), bars=[
     ["الأقل", 58.3, "58,30 €", "grey"], ["الأكثر", 203.8, "203,80 €", "green"]], gap=1.5),
   dict(k="head", text="شكون يقدر يتعطل عليه؟", at="شكون اللي يقدر", until="ونصيحة: إلى", sub="آخر الأسبوع ديال نونبر"),
   dict(k="icons", at="اللي دار الطلب", until="ونصيحة: إلى", box=(160, 330, 1760, 840), items=[
     ["file-text", "طلب جديد", "gold"], ["baby-carriage", "ولد جديد", "blue"], ["credit-card", "تبديل الإيبان", "red"], ["report-money", "تبديل الإيزي", "green"]], gap=1.0),
   dict(k="steps", at="ونصيحة: إلى", box=(160, 230, 1760, 820), steps=[
     ["دخل للسيت ديال الإينبس", "INPS"], ["دخل بالسبيد", "SPID"], ["شوف الحالة ديال الخلاص", "OK"]], gap=2.5, check_after=1.0),
 ]),
 dict(audio="G.wav", text=T["G"], chapter="04 · ملخص اليوم", src=S_HOME, items=[
   dict(k="head", text="ملخص اليوم", at=0.1, until="ونتا، شنو"),
   dict(k="rows", at="واحد: الفيش", until="ونتا، شنو", y=380, gap=130, size=50, rows=[
     ("بطاقة السوابق أونلاين · إي بوليس", "9/11", "واحد: الفيش"),
     ("بونوس الماماوات 2027 · مشروع", "100 €", "جوج: البونوس"),
     ("لاسينيو أونيكو", "19-20/11", "وتلاتة: لاسينيو"),
   ]),
   dict(k="people", at="ونتا، شنو", until="وإلى عجبك", box=(160, 300, 1760, 860), people=["woman", "worker"],
        say=[dict(who=0, text="كتب لينا فالكومونتير", at=0.6, bg="green")]),
   dict(k="cta", at="وإلى عجبك", text="ابوني فالقناة", sub="كل نهار خبر مفيد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("بطاقة السوابق من المغرب", (236, 196, 96)), "ولات أونلاين", "وبونوس الماماوات"],
  num="100 €", numsub="بونوس الماماوات 2027 · مشروع",
  bottom="مغاربة إيطاليا · خبار مفيدة بالدارجة",
)
