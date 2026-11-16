import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-16.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo1-2026-11-16")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = {k: v.replace("گ", "ك") for k, v in JOB["blocks"].items()}

S_CDS = "CdM 13/10/2026 · Edotto 14/10 · Infodifesa 14/10 · QuiFinanza 14/10/2026"
S_CDS2 = "Consiglio di Stato parere 1944/2026 · InMoto 12/11 · SmartWorld 10/11 · BusinessOnline 14/11 · A.G. 448"
S_DOM = "INPS messaggio 3691 del 12/11/2026 · Finanza & Fisco · EC News · InformazioneFiscale · InvestireOggi"
S_FX = "Bank Al-Maghrib (5-11/11/2026) · H24info 14/11 · Hespress 16/11 · Bladi.net 14/11/2026"
S_HOME = "مغاربة إيطاليا · خبار مفيدة بالدارجة"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850)

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="00 · خبار اليوم", src=S_HOME, items=[
   dict(k="head", text="تلاتة خبار مفيدة", at=0.2, until="الخبر الأول على", sub="الاتنين 16 نونبر 2026"),
   dict(k="people", at=0.6, until="الخبر الأول على", box=(160, 330, 1760, 860), people=["man", "hijab", "worker"],
        say=[dict(who=1, text="شنو الجديد اليوم؟", at=0.6), dict(who=0, text="تلاتة خبار", at=2.2, bg="green")]),
   dict(k="rows", at="الخبر الأول على", until="يالاه نبداو", y=330, gap=125, size=50, rows=[
     ("الكود الجديد ديال الطريق والبيرمي", "65", "الخبر الأول على"),
     ("الخدامة فالدار: الخلاص أونلاين", "10/1/2027", "الخبر التاني للي"),
     ("الدرهم قدام الأورو", "+0,9%", "والخبر التالت"),
   ]),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Milano", "Casablanca"], pins=["Roma", "Rabat"], labels=False, at="يالاه نبداو", box=(160, 200, 1760, 880)),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="01 · الكود الجديد ديال الطريق", src=S_CDS, items=[
   dict(k="chapter", num="01", title="الكود الجديد ديال الطريق", at=0.1, until="نهار طلطاش"),
   dict(k="calendar", at="نهار طلطاش", until="ولكن رد البال", box=R_BOX, day=13, month=10, sub="قراءة أولى · 2026"),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="نهار طلطاش", until="ولكن رد البال", box=L_BOX),
   dict(k="people", at="ولكن رد البال", until="شنو كاين فيه", box=(160, 300, 1760, 860), people=["man", "office"],
        say=[dict(who=0, text="واش ولا قانون؟", at=0.2), dict(who=1, text="باقي مشروع", at=1.4, bg="red")]),
   dict(k="vs", at="أولا، البيرمي", until="تانيا:", box=(260, 220, 1660, 820),
        right=dict(title="اليوم", value="50", sub="كل 10 سنين حتى", icon="license", color="grey"),
        left=dict(title="المشروع", value="65", sub="كل 10 سنين حتى", icon="license", color="green"), gap=4.0),
   dict(k="people", at="تانيا:", until="تالتا:", box=R_BOX, people=["man", "worker"],
        say=[dict(who=0, text="البيرمي فالتيليفون", at=0.4, bg="green")]),
   dict(k="map", view="north", pins=["Milano", "Torino", "Bologna"], labels=False, at="تانيا:", until="تالتا:", box=L_BOX),
   dict(k="bars", at="تالتا:", until="ورابعا:", box=(160, 380, 1760, 820), bars=[
     ["الأصناف ديال الخطايا اليوم", 82, "82", "grey"], ["فالمشروع", 21, "21", "green"]], gap=2.0),
   dict(k="head", text="الخطايا", at="تالتا:", until="ورابعا:", sub="الأصناف"),
   dict(k="bars", at="ورابعا:", box=(160, 380, 1760, 820), bars=[
     ["الأجل اليوم (أيام)", 90, "90", "grey"], ["فالمشروع (أيام)", 45, "45", "green"]], gap=2.5),
   dict(k="head", text="المخالفة بالكاميرا", at="ورابعا:", sub="الأجل باش توصلك"),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="01 · الكود الجديد ديال الطريق", src=S_CDS2, items=[
   dict(k="head", text="علاش مازال ما دخلش؟", at=0.1, until="نهار تلاتة"),
   dict(k="people", at=0.3, until="نهار تلاتة", box=(160, 330, 1760, 860), people=["elder", "woman"],
        say=[dict(who=1, text="إمتى غادي يدخل؟", at=0.5)]),
   dict(k="calendar", at="نهار تلاتة", until="الحكومة عندها", box=R_BOX, day=3, month=11, sub="مجلس الدولة وقف الرأي"),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="نهار تلاتة", until="الحكومة عندها", box=L_BOX),
   dict(k="steps", at="الحكومة عندها", until="يعني دابا", box=(160, 230, 1760, 820), steps=[
     ["الحكومة تكمل الوراق", "25/11/2026"], ["الرأي ديال البرلمان", "12/1/2027"], ["الجريدة الرسمية", "?"]], gap=3.5, check_after=0.8),
   dict(k="big", text="اليوم", at="يعني دابا", until="مثال من عندنا", y=470, size=240, color=GOLD, sub="القواعد والخطايا ديال دابا"),
   dict(k="people", at="مثال من عندنا", until="وإلى عندك البيرمي", box=(160, 300, 1760, 860), people=["elder", "clerk"],
        say=[dict(who=0, text="عندي 52 عام", at=0.3), dict(who=1, text="كل 5 سنين", at=2.2, bg="green")]),
   dict(k="map", view="med", hl=["MAR"], route=["Casablanca", "Milano", "plane"], pins=["Rabat"], labels=False, at="وإلى عندك البيرمي", box=(160, 200, 1760, 880)),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="02 · الخدامة فالدار: الكونطريبوتي", src=S_DOM, items=[
   dict(k="chapter", num="02", title="الخدامة فالدار: الكونطريبوتي", at=0.1, until="للعائلات اللي"),
   dict(k="people", at="للعائلات اللي", until="نهار طناش", box=(160, 300, 1760, 860), people=["elder", "hijab", "woman"],
        say=[dict(who=1, text="كنخدم بادانتي", at=1.6), dict(who=0, text="وأنا المعلم", at=3.2, bg="green")]),
   dict(k="calendar", at="نهار طناش", until="شنو فيها", box=R_BOX, day=12, month=11, sub="رسالة الإينبس 3691"),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="نهار طناش", until="شنو فيها", box=L_BOX),
   dict(k="vs", at="شنو فيها", until="اللي عمرو أقل", box=(260, 220, 1660, 820),
        right=dict(title="قبل", value="2025", sub="البولتان بالبوسطا", icon="mail", color="grey"),
        left=dict(title="دابا", value="2026", sub="أونلاين فالإينبس", icon="phone", color="green"), gap=2.5),
   dict(k="bars", at="اللي عمرو أقل", until="والمهم:", box=(160, 380, 1760, 820), bars=[
     ["أقل من 76 عام: أونلاين", 60, "< 76", "green"], ["76 ولا كثر: كاغيط غير 2026", 76, "76+", "gold"]], gap=3.0),
   dict(k="people", at="والمهم:", box=(160, 300, 1760, 860), people=["elder", "office"],
        say=[dict(who=0, text="ما وصلنيش البولتان", at=0.4), dict(who=1, text="خاصك تخلص", at=2.0, bg="red")]),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="02 · الخدامة فالدار: الكونطريبوتي", src=S_DOM, items=[
   dict(k="steps", at=0.1, until="وتقدر تخلص حتى", box=(160, 230, 1760, 820), steps=[
     ["السيت ديال الإينبس", "INPS"], ["البورطال ديال الخلاص", "Portale"], ["الخدامين فالديور", "pagoPA"]], gap=1.8, check_after=0.8),
   dict(k="icons", at="وتقدر تخلص حتى", until="الخلاص كيكون", box=(160, 330, 1760, 860), items=[
     ["building-bank", "البنكة", "gold"], ["mailbox", "البوسطا", "blue"], ["credit-card", "الهوم بانكينغ", "green"], ["phone", "التطبيقات", "gold"]], gap=1.2),
   dict(k="head", text="كل 3 شهور", at="الخلاص كيكون", until="مثال من عندنا", sub="أكتوبر · نونبر · دجنبر"),
   dict(k="calendar", at="مثال من عندنا", until="وإلى تعطلتي", box=R_BOX, day=10, month=1, sub="آخر أجل · 2027"),
   dict(k="text", text="من 1 حتى 10 يناير", at="مثال من عندنا", until="وإلى تعطلتي", x=560, y=470, size=60, color=GOLD),
   dict(k="text", text="أكتوبر · نونبر · دجنبر", at="مثال من عندنا", until="وإلى تعطلتي", x=560, y=570, size=48, color=WHITE),
   dict(k="people", at="وإلى تعطلتي", box=L_BOX, people=["hijab", "elder"],
        say=[dict(who=0, text="البانسيون ديالي", at=3.0, bg="green")]),
   dict(k="map", view="south", pins=["Napoli", "Bari", "Palermo"], labels=False, at="ورد البال:", box=R_BOX),
 ]),
 dict(audio="F.wav", text=T["F"], chapter="03 · المغرب: الدرهم والأورو", src=S_FX, items=[
   dict(k="chapter", num="03", title="المغرب: الدرهم والأورو", at=0.1, until="حسب بنك المغرب"),
   dict(k="map", view="med", hl=["MAR"], route=["Milano", "Casablanca", "plane"], pins=["Rabat"], labels=False, at="حسب بنك المغرب", until="الدرهم طلع", box=(160, 200, 1760, 880)),
   dict(k="vs", at="الدرهم طلع", until="شنو كيعني", box=(260, 220, 1660, 820),
        right=dict(title="قدام الأورو", value="+0,9%", sub="الدرهم طلع", icon="trending-up", color="green"),
        left=dict(title="قدام الدولار", value="-0,3%", sub="الدرهم طاح", icon="trending-down", color="red"), gap=3.0),
   dict(k="people", at="شنو كيعني", until="الأورو دابا", box=(160, 300, 1760, 860), people=["man", "woman"],
        say=[dict(who=1, text="شنو كيعني ليا؟", at=0.2), dict(who=0, text="دراهم أقل", at=1.8, bg="red")]),
   dict(k="big", text="≈ 10,9 DH", at="الأورو دابا", until="مثال من عندنا", y=470, size=220, color=GOLD, sub="1 € · السعر المرجعي"),
   dict(k="bars", at="مثال من عندنا", box=(160, 380, 1760, 820), bars=[
     ["1.000 €", 100, "≈ -100 DH", "red"], ["5.000 €", 500, "≈ -500 DH", "red"]], gap=4.0),
   dict(k="head", text="مثال من عندنا", at="مثال من عندنا", sub="من سيمانة لسيمانة"),
 ]),
 dict(audio="G.wav", text=T["G"], chapter="03 · المغرب: الدرهم والأورو", src=S_FX, items=[
   dict(k="people", at=0.1, until="قبل ما تصيفط", box=R_BOX, people=["man"],
        say=[dict(who=0, text="السعر ديال البنكة؟", at=0.6)]),
   dict(k="map", view="med", hl=["ITA", "MAR"], pins=["Torino", "Casablanca", "Oujda"], labels=False, at=0.1, until="قبل ما تصيفط", box=L_BOX),
   dict(k="icons", at="قبل ما تصيفط", until="وهادا هو الملخص", box=(160, 330, 1760, 860), items=[
     ["coin-euro", "شحال غادي يوصل", "green"], ["receipt", "شحال المصاريف", "gold"]], gap=3.0),
   dict(k="head", text="ملخص اليوم", at="وهادا هو الملخص", until="ونتا، شنو"),
   dict(k="rows", at="واحد: الكود", until="ونتا، شنو", y=330, gap=125, size=50, rows=[
     ("الكود الجديد: باقي مشروع", "65", "واحد: الكود"),
     ("الخدامة فالدار: الخلاص أونلاين", "10/1/2027", "جوج: الكونطريبوتي"),
     ("الدرهم قدام الأورو: قارن", "+0,9%", "تلاتة: الدرهم"),
   ]),
   dict(k="people", at="ونتا، شنو", until="وإلى عجبك", box=(160, 300, 1760, 860), people=["woman", "worker"],
        say=[dict(who=0, text="كتب لينا فالكومونتير", at=0.6, bg="green")]),
   dict(k="cta", at="وإلى عجبك", text="ابوني فالقناة", sub="كل نهار خبر مفيد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("البيرمي حتى 65 عام؟", (236, 196, 96)), "الكود الجديد باقي مشروع", "والخدامة فالدار: الخلاص أونلاين"],
  num="65", numsub="التجديد كل 10 سنين · مشروع",
  bottom="مغاربة إيطاليا · خبار مفيدة بالدارجة",
)
