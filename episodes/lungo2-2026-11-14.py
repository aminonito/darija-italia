import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-14.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo2-2026-11-14")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = JOB["blocks"]
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850)

S_INTRO = "Assolombarda (status permanente, documento 10 anni) · Arletti Partners agg. 24/7/2026 · LeggeInChiaro art. 9 TUI"
S_REQ = "Arletti Partners (5 anni, assenze 6/10 mesi, assegno sociale 2026 7.101,12 €, +50% per familiare, casellario e carichi pendenti) · Assolombarda · Studio Cataldi"
S_DOC = "Studio Cataldi (documenti) · Prefettura, brochure test di italiano A2 (domanda online, convocazione entro 60 giorni, esenzioni) · Città metropolitana di Bologna"
S_PASSI = "Money.it agg. 5/10/2026 (100 + 30,46 + 16 + 30 = 176,46 €) · Italiahello (176,46 €) · Arletti Partners (posta, impronte, ritiro)"
S_FINE = "Studio Cataldi + LeggeInChiaro art. 9 TUI (revoca dopo 12 mesi fuori UE, documento ogni 10 anni) · Arletti Partners"

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="01 · شنو هي الكارطا", src=S_INTRO, items=[
   dict(k="head", text="البيرميسو ديال المدة الطويلة", at=0.2, until="واش عييتي", sub="دليل عملي خطوة بخطوة · Permesso UE lungo periodo"),
   dict(k="people", at="واش عييتي", until="اليوم عندنا", box=(160, 320, 1760, 860), people=["worker", "hijab"],
        say=[dict(who=0, text="كل عامين كنجدد البيرميسو!", at=0.6), dict(who=1, text="حتى أنا، وكل مرة كنخلص", at=2.6, bg="green")]),
   dict(k="head", text="الكارطا دي سوجورنو", at="اليوم عندنا", until="هاد البيرميسو ما", sub="Permesso di soggiorno UE per soggiornanti di lungo periodo"),
   dict(k="vs", at="هاد البيرميسو ما", until="فهاد الفيديو", box=(260, 360, 1660, 880),
        left=dict(title="البيرميسو العادي", value="1-2 عام", sub="كتجددو ديما", icon="calendar", color="red"),
        right=dict(title="الكارطا", value="دايمة", sub="الوثيقة كل 10 سنين", icon="check", color="green"), gap=2.0),
   dict(k="icons", at="فهاد الفيديو", until="وناخدو مثال", box=(160, 300, 1760, 860), items=[
     ["scale", "الشروط", "gold"], ["file-text", "الوراق والامتحان", "blue"], ["cash", "الخطوات والثمن", "green"], ["alert-triangle", "الغلطات", "red"]], gap=1.8),
   dict(k="map", view="italy", hl=["Piemonte"], pins=["Torino"], labels=False, at="وناخدو مثال", box=R_BOX),
   dict(k="people", at="وناخدو مثال", box=L_BOX, people=["worker"],
        say=[dict(who=0, text="عندي البيرميسو من 2020", at=1.5, bg="green")]),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="02 · الشروط", src=S_REQ, items=[
   dict(k="chapter", num="02", title="الشروط", at=0.1, until="خاصك يكون"),
   dict(k="big", text="5 سنين", at="خاصك يكون", until="ولكن رد البال", y=440, size=220, color=GOLD, sub="بيرميسو صالح فإيطاليا · سعيد عندو 6"),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Torino", "Casablanca"], labels=False, at="ولكن رد البال", until="ستة ديال الشهور", box=(160, 200, 1760, 880)),
   dict(k="rows", at="ستة ديال الشهور", until="الشرط التاني", y=420, gap=150, size=54, rows=[
     ("الغياب متابع", "6 شهور", "ستة ديال الشهور", GOLD),
     ("الغياب فالمجموع", "10 شهور", "عشرة ديال الشهور", RED),
   ]),
   dict(k="head", text="المدخول: قد الأسينيو سوسيالي", at="الشرط التاني", until="فألفين وستة", sub="Assegno sociale 2026"),
   dict(k="bars", at="فألفين وستة", until="وفهاد الحالة", box=(160, 360, 1760, 840), bars=[
     ["بوحدك", 7101.12, "7.101 €", "green"], ["مع فرد واحد", 10651.68, "10.651 €", "gold"], ["مع جوج", 14202.24, "14.202 €", "red"]]),
   dict(k="head", text="الإيدونيتا ديال الدار", at="وفهاد الحالة", until="الشرط التالت", sub="غير إلا زدتي العائلة فالطلب · من الكومون"),
   dict(k="people", at="الشرط التالت", box=(160, 320, 1760, 860), people=["office", "man"],
        say=[dict(who=1, text="شنو خاصني باش نطلبها؟", at=0.5), dict(who=0, text="سجل عدلي نقي + الطليانية", at=2.8, bg="green")]),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="03 · الوراق والامتحان", src=S_DOC, items=[
   dict(k="chapter", num="03", title="الوراق", at=0.1, until="خاصك الكيت"),
   dict(k="icons", at="خاصك الكيت", until="من بعد، الوراق", box=(160, 320, 1760, 840), items=[
     ["mail", "الكيت ديال البوسطا", "gold"], ["e-passport", "الباسبور كامل", "blue"], ["id", "البيرميسو + الكودتشي", "green"]], gap=1.8),
   dict(k="icons", at="من بعد، الوراق", until="ودابا الامتحان", box=(160, 320, 1760, 840), items=[
     ["receipt-tax", "CU / 730", "gold"], ["cash", "البوسطات باغا", "green"], ["scale", "السجل العدلي", "blue"], ["home", "الإيدونيتا (العائلة)", "red"]], gap=2.2),
   dict(k="head", text="الامتحان ديال الطليانية A2", at="ودابا الامتحان", until="والبريفيتورا", sub="الطلب أونلاين · وزارة الداخلية"),
   dict(k="map", view="italy", hl=["Piemonte"], pins=["Torino"], labels=False, at="والبريفيتورا", until="شكون اللي", box=R_BOX),
   dict(k="calendar", at="والبريفيتورا", until="شكون اللي", box=L_BOX, day=60, month="يوم", sub="الرسالة ديال البريفيتورا"),
   dict(k="steps", at="شكون اللي", until="سعيد قرا", box=(160, 220, 1760, 840), steps=[
     ["شهادة A2 ولا كثر", "1"], ["ديبلوم ديال الثانوي فإيطاليا", "2"], ["الولاد تحت 14 عام", "3"], ["مشكل صحي كبير بشهادة", "4"]], gap=3.5, check_after=0.8),
   dict(k="people", at="سعيد قرا", box=(160, 320, 1760, 860), people=["worker", "student"],
        say=[dict(who=0, text="عندي شهادة A2", at=0.8, bg="green"), dict(who=1, text="إذن بلا امتحان", at=3.0)]),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="04 · الخطوات والثمن", src=S_PASSI, items=[
   dict(k="chapter", num="04", title="الخطوات", at=0.1, until="الخطوة اللولة"),
   dict(k="steps", at="الخطوة اللولة", until="الخطوة التالتة", box=(160, 220, 1760, 840), steps=[
     ["عمر الكيت (الباطرونا ولا الكومون)", "1"], ["خلص فالبوسطا وخود الريسيفوطا", "2"]], gap=7.0, check_after=1.0),
   dict(k="map", view="italy", hl=["Piemonte"], pins=["Torino"], labels=False, at="الخطوة التالتة", until="شحال كتخلص", box=R_BOX),
   dict(k="people", at="الخطوة التالتة", until="شحال كتخلص", box=L_BOX, people=["clerk", "worker"],
        say=[dict(who=0, text="البصمات فالكويستورا", at=0.6, bg="green"), dict(who=1, text="وخديت الكارطا!", at=5.0)]),
   dict(k="rows", at="شحال كتخلص", until="المجموع", y=330, gap=120, size=50, rows=[
     ("الطابع", "16 €", "ستاش أورو", WHITE),
     ("البوسطا", "30 €", "ديال البوسطا", WHITE),
     ("الكارطا الإلكترونية", "30,46 €", "تلاتين أورو وستة", WHITE),
     ("الكونتريبوتو", "100 €", "ومية أورو", WHITE),
   ]),
   dict(k="big", text="176,46 €", at="المجموع", until="قارن", y=470, size=220, color=GOLD, sub="16 + 30 + 30,46 + 100"),
   dict(k="people", at="قارن", box=L_BOX, people=["clerk"],
        say=[dict(who=0, text="مرة وحدة، ماشي كل عامين", at=2.0, bg="green")]),
   dict(k="bars", at="قارن", box=R_BOX, bars=[
     ["بيرميسو عامين", 126.46, "126,46 €", "red"], ["الكارطا", 176.46, "176,46 €", "green"]]),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="05 · الغلطات والملخص", src=S_FINE, items=[
   dict(k="chapter", num="05", title="الغلطات اللي تبعد عليها", at=0.1, until="الغلطة اللولة"),
   dict(k="warn", text="الغياب الطويل فالمغرب كيخرج من الحساب", at="الغلطة اللولة", until="الغلطة التانية", y=300),
   dict(k="warn", text="مدخول ما كاينش فالوراق", at="الغلطة التانية", until="الغلطة التالتة", y=440),
   dict(k="warn", text="العائلة فالطلب بلا الإيدونيتا ديال الدار", at="الغلطة التالتة", until="الغلطة الرابعة", y=580),
   dict(k="people", at="الغلطة الرابعة", until="الغلطة الخامسة", box=L_BOX, people=["elder"],
        say=[dict(who=0, text="الكارطا ممكن تضيع!", at=0.8, bg="red"), dict(who=0, text="12 شهر برا أوروبا: خطر", at=6.0, bg="red")]),
   dict(k="map", view="med", hl=["MAR"], route=["Milano", "Casablanca"], labels=False, at="الغلطة الرابعة", until="الغلطة الخامسة", box=R_BOX),
   dict(k="warn", text="ما تنساش تبدل الوثيقة كل 10 سنين", at="الغلطة الخامسة", until="نعاودو باختصار", y=720),
   dict(k="head", text="باختصار", at="نعاودو باختصار", until="هادشي معلومات"),
   dict(k="rows", at="نعاودو باختصار", until="هادشي معلومات", y=360, gap=100, size=46, rows=[
     ("بيرميسو صالح", "5 سنين", "خمس سنين ديال", WHITE),
     ("المدخول فالعام", "7.101 €", "مدخول قد", GOLD),
     ("الطليانية", "A2", "شهادة ولا", GREEN),
     ("الثمن", "176,46 €", "والتمن تقريبا", GOLD),
   ]),
   dict(k="people", at="هادشي معلومات", until="إلا عجبك", box=(160, 300, 1760, 860), people=["hijab", "worker"],
        say=[dict(who=0, text="شحال هادي وانت فإيطاليا؟", at=2.5, bg="green"), dict(who=1, text="7 سنين!", at=4.5)]),
   dict(k="cta", at="إلا عجبك", text="ابوني فالقناة", sub="كل نهار دليل جديد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("الكارطا دي سوجورنو", (236, 196, 96)), "خطوة بخطوة فإيطاليا", "الشروط والوراق والثمن"],
  num="5 سنين", numsub="Permesso UE lungo periodo",
  bottom="مغاربة إيطاليا · دليل عملي بالدارجة",
)
