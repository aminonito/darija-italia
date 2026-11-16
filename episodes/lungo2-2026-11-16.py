import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-16.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo2-2026-11-16")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = JOB["blocks"]
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850)

S_INTRO = "Prefettura, guida alla cittadinanza (art. 9 L. 91/1992) · Arletti Partners agg. 29/10/2026 · InfoImmigrazione agg. 4/7/2026"
S_REQ = "Arletti Partners (10 anni, reddito, B1, esenzioni) · InfoImmigrazione (8.263,31 / 11.362,05 / +516 €) · Prefettura, guida (B1, lungo periodo, titolo di studio)"
S_DOC = "Prefettura, guida (certificato penale 6 mesi; non serve se entrati < 14 anni) · InfoImmigrazione · Prefettura, legalizzazioni (Marocco: Apostille dal 14/8/2016)"
S_PASSI = "Prefettura, guida (250 € + 16 €, portale) · InfoImmigrazione + Arletti Partners (SPID, 24-36 mesi) · Studio Cataldi + Comune di Venegono S. (giuramento 6 mesi)"
S_FINE = "Prefettura, guida · Arletti Partners · InfoImmigrazione · Studio Cataldi"

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="01 · لمن هاد الدليل", src=S_INTRO, items=[
   dict(k="head", text="الجنسية الإيطالية بالإقامة", at=0.2, until="ساكن فإيطاليا", sub="دليل عملي خطوة بخطوة · Cittadinanza per residenza"),
   dict(k="people", at="ساكن فإيطاليا", until="فهاد الفيديو", box=(160, 320, 1760, 860), people=["man", "hijab", "worker"],
        say=[dict(who=0, text="عشر سنين وأنا هنا", at=0.8), dict(who=1, text="نقدرو ناخدو الجنسية؟", at=3.0, bg="green")]),
   dict(k="icons", at="فهاد الفيديو", until="وناخدو مثال", box=(160, 300, 1760, 860), items=[
     ["scale", "الشروط", "gold"], ["file-text", "الوراق", "blue"], ["clipboard-check", "الخطوات والثمن", "green"], ["alert-triangle", "الغلطات", "red"]], gap=2.0),
   dict(k="map", view="north", hl=["Lombardia"], pins=["Brescia"], labels=False, at="وناخدو مثال", until="معاه مراتو", box=R_BOX),
   dict(k="people", at="وناخدو مثال", until="معاه مراتو", box=L_BOX, people=["man"],
        say=[dict(who=0, text="أنا رشيد، ساكن فبريشيا", at=0.6, bg="green")]),
   dict(k="people", at="معاه مراتو", until="رشيد كمل", box=(160, 320, 1760, 860), people=["man", "hijab", "child", "girl"],
        say=[dict(who=1, text="أنا نادية", at=0.4), dict(who=0, text="وهادو الولاد", at=1.8, bg="green")]),
   dict(k="calendar", at="رشيد كمل", until="معلومة مهمة", box=(160, 260, 1760, 860), day=10, month=3, sub="2016 · 2026 = عشر سنين"),
   dict(k="head", text="القواعد ديال دابا", at="معلومة مهمة", y=380, sub="Regole in vigore oggi · إلا تبدل شي قانون، غادي نقولوها"),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="02 · الشروط", src=S_REQ, items=[
   dict(k="chapter", num="02", title="الشروط", at=0.1, until="الشرط اللول"),
   dict(k="map", view="italy", pins=["Brescia", "Roma", "Napoli"], labels=False, at="الشرط اللول", until="الشرط التاني", box=R_BOX),
   dict(k="big", text="10", at="الشرط اللول", until="الشرط التاني", x=560, y=430, size=240, color=GOLD, sub="سنين ديال الإقامة"),
   dict(k="text", text="بيرميسو صالح وريزيدينسا · حتى للقسم", at="يعني بيرميسو", until="الشرط التاني", x=560, y=720, size=40, color=GREY),
   dict(k="bars", at="الشرط التاني", until="يعني رشيد", box=(160, 300, 1760, 860), bars=[
     ["بوحدك", 8263.31, "8.263,31 €", "green"], ["مع الزوج ولا الزوجة", 11362.05, "11.362,05 €", "gold"], ["رشيد مع العائلة", 12394.05, "12.394 €", "red"]]),
   dict(k="people", at="يعني رشيد", until="الشرط التالت", box=(160, 320, 1760, 860), people=["man", "office"],
        say=[dict(who=0, text="واش الدخل ديالي كافي؟", at=0.6), dict(who=1, text="شوف التلاتة ديال السنين", at=3.0, bg="green")]),
   dict(k="head", text="ملف نقي مع العدالة", at="الشرط التالت", until="الشرط الرابع", y=380, sub="الشرط التالت"),
   dict(k="icons", at="الشرط الرابع", until="ولكن هاد", box=(160, 300, 1760, 860), items=[
     ["school", "سيينا", "gold"], ["school", "بيروجا", "blue"], ["school", "روما تري", "green"], ["certificate", "دانتي أليغييري", "red"]], gap=1.3),
   dict(k="vs", at="ولكن هاد", until="رشيد عندو", box=(260, 360, 1660, 880),
        right=dict(title="ما عندكش الكارطا", value="B1", sub="خاصك الشهادة", icon="certificate", color="red"),
        left=dict(title="عندك الكارطا الطويلة", value="ما خاصاكش", sub="ولا ديبلوم إيطالي", icon="id", color="green"), gap=2.0),
   dict(k="map", view="north", hl=["Lombardia"], pins=["Brescia"], labels=False, at="رشيد عندو", box=R_BOX),
   dict(k="people", at="رشيد عندو", box=L_BOX, people=["man"],
        say=[dict(who=0, text="عندي الكارطا، ما خاصنيش الامتحان", at=0.6, bg="green")]),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="03 · الوراق من إيطاليا ومن المغرب", src=S_DOC, items=[
   dict(k="chapter", num="03", title="الوراق", at=0.1, until="من إيطاليا"),
   dict(k="icons", at="من إيطاليا", until="ومن المغرب", box=(160, 300, 1760, 860), items=[
     ["e-passport", "الباسبور", "blue"], ["id", "البيرميسو والكود فيسكال", "gold"], ["certificate", "شهادة الطاليانية", "green"], ["receipt-tax", "التصريحات ديال الضرائب", "red"]], gap=2.2),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Casablanca", "Milano"], labels=False, at="ومن المغرب", until="هاد الشهادة صالحة", box=R_BOX),
   dict(k="icons", at="ومن المغرب", until="هاد الشهادة صالحة", box=L_BOX, items=[
     ["file-text", "عقد الازدياد", "gold"], ["file-certificate", "شهادة السوابق", "green"]], gap=3.0),
   dict(k="calendar", at="هاد الشهادة صالحة", until="إلا دخلتي", box=(160, 260, 1760, 860), day=6, month="شهور", sub="صلاحية شهادة السوابق"),
   dict(k="people", at="إلا دخلتي", until="والجوج وراق", box=(160, 320, 1760, 860), people=["student", "office"],
        say=[dict(who=0, text="جيت لإيطاليا وأنا صغير", at=0.5), dict(who=1, text="ما خاصاكش السوابق", at=2.4, bg="green")]),
   dict(k="steps", at="والجوج وراق", until="سول البريفيتورا", box=(160, 220, 1760, 840), steps=[
     ["الوثيقة من المغرب", "1"], ["الأبوستيل", "2"], ["الترجمة للطاليانية", "3"]], gap=2.4, check_after=0.8),
   dict(k="people", at="سول البريفيتورا", until="نصيحة صغيرة", box=(160, 320, 1760, 860), people=["man", "clerk"],
        say=[dict(who=0, text="شنو الترجمة اللي بغيتو؟", at=0.6), dict(who=1, text="سول البريفيتورا ديالك", at=2.6, bg="green")]),
   dict(k="warn", text="نصيحة: خرج شهادة السوابق فالأخير", at="نصيحة صغيرة", y=440),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="04 · الخطوات والثمن والمدة", src=S_PASSI, items=[
   dict(k="chapter", num="04", title="الخطوات والثمن", at=0.1, until="الخطوة اللولة"),
   dict(k="rows", at="الخطوة اللولة", until="الخطوة التانية", y=330, gap=140, size=56, rows=[
     ("الكونطريبوتو لوزارة الداخلية", "250 €", "الخطوة اللولة", WHITE),
     ("التانبر", "16 €", "وجيب تانبر", WHITE),
     ("المجموع", "266 €", "يعني فالمجموع", GOLD),
     ("الترجمة والأبوستيل والامتحان: الثمن كيتبدل", "...", "من غير الترجمة", GREY),
   ]),
   dict(k="steps", at="الخطوة التانية", until="الخطوة التالتة", box=(160, 200, 1760, 860), steps=[
     ["دخل بالسبيد", "1"], ["عمر الفورميلير", "2"], ["طلع الوراق", "3"], ["صيفط الطلب", "4"]], gap=1.6, check_after=0.8),
   dict(k="people", at="الخطوة التالتة", until="المدة:", box=(160, 320, 1760, 860), people=["clerk", "man"],
        say=[dict(who=0, text="خاصنا ورقة زايدة", at=0.8), dict(who=1, text="واخا، نصيفطها", at=2.6, bg="green")]),
   dict(k="bars", at="المدة:", until="يعني رشيد", box=(160, 320, 1760, 840), bars=[
     ["عادي (شهر)", 24, "24", "gold"], ["الأقصى (شهر)", 36, "36", "red"]]),
   dict(k="vs", at="يعني رشيد", until="وإلا بدلتي", box=(260, 360, 1660, 880),
        right=dict(title="الطلب", value="1/2027", sub="يناير", icon="calendar", color="gold"),
        left=dict(title="الجواب", value="2029", sub="وممكن حتى 2030", icon="file-certificate", color="green"), gap=2.5),
   dict(k="map", view="north", hl=["Lombardia"], pins=["Brescia"], labels=False, at="وإلا بدلتي", until="الخطوة الرابعة", box=R_BOX),
   dict(k="people", at="وإلا بدلتي", until="الخطوة الرابعة", box=L_BOX, people=["man"],
        say=[dict(who=0, text="بدلت الدار؟ علم البريفيتورا", at=0.5, bg="red")]),
   dict(k="calendar", at="الخطوة الرابعة", until="ومن بعد القسم", box=L_BOX, day=6, month="شهور", sub="من التبليغ ديال الديكري"),
   dict(k="people", at="الخطوة الرابعة", until="ومن بعد القسم", box=R_BOX, people=["clerk"],
        say=[dict(who=0, text="القسم هنا فالكومون", at=2.0, bg="green")]),
   dict(k="people", at="ومن بعد القسم", box=(160, 320, 1760, 860), people=["man", "hijab"],
        say=[dict(who=0, text="ولينا مواطنين إيطاليين", at=0.6), dict(who=1, text="مبروك!", at=2.4, bg="green")]),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="05 · الغلطات والملخص", src=S_FINE, items=[
   dict(k="chapter", num="05", title="الغلطات اللي تبعد عليها", at=0.1, until="الغلطة اللولة"),
   dict(k="warn", text="العشر سنين كتحسب من الريزيدينسا، ماشي من الدخلة", at="الغلطة اللولة", until="الغلطة التالتة", y=300),
   dict(k="warn", text="الدخل ناقص ولا ما مصرحش فشي عام", at="الغلطة التانية", until="الغلطة التالتة", y=440),
   dict(k="map", view="med", hl=["MAR"], pins=["Casablanca"], labels=False, at="الغلطة التالتة", until="الغلطة الرابعة", box=R_BOX),
   dict(k="people", at="الغلطة التالتة", until="الغلطة الرابعة", box=L_BOX, people=["man"],
        say=[dict(who=0, text="السوابق قديمة؟ الطلب يتعطل", at=0.6, bg="red")]),
   dict(k="people", at="الغلطة الرابعة", until="الغلطة الخامسة", box=(160, 320, 1760, 860), people=["woman", "clerk"],
        say=[dict(who=1, text="صيفطنا ليك ميساج!", at=0.8, bg="red"), dict(who=0, text="ما شفتوش...", at=2.8)]),
   dict(k="calendar", at="الغلطة الخامسة", until="نعاودو باختصار", box=(160, 260, 1760, 860), day=6, month="شهور", sub="بلا قسم: الديكري كيضيع"),
   dict(k="head", text="باختصار", at="نعاودو باختصار", until="هادشي معلومات"),
   dict(k="rows", at="نعاودو باختصار", until="هادشي معلومات", y=350, gap=90, size=44, rows=[
     ("الإقامة القانونية (سنين)", "10", "عشر سنين ديال الإقامة", WHITE),
     ("الدخل فالعام · بوحدك", "8.263,31 €", "عشر سنين ديال الإقامة", GOLD),
     ("الطاليانية · إلا ما عندكش الكارطا", "B1", "الطاليانية بي", WHITE),
     ("الثمن", "266 €", "متين وستة وستين", GOLD),
     ("الانتظار (شهر)", "24 - 36", "وجوج حتى", GREEN),
   ]),
   dict(k="people", at="هادشي معلومات", until="وإلا عجبك", box=(160, 300, 1760, 860), people=["hijab", "worker"],
        say=[dict(who=0, text="شحال هادي وانت فإيطاليا؟", at=3.0, bg="green"), dict(who=1, text="تناش عام!", at=5.5)]),
   dict(k="cta", at="وإلا عجبك", text="ابوني فالقناة", sub="كل نهار دليل جديد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("الجنسية الإيطالية", (236, 196, 96)), "بعد 10 سنين", "الشروط والوراق من المغرب"],
  num="266 €", numsub="Cittadinanza italiana per residenza",
  bottom="مغاربة إيطاليا · دليل عملي بالدارجة",
)
