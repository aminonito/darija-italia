import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-15.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo2-2026-11-15")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = JOB["blocks"]
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850)

S_INTRO = "Ministero del Lavoro, circolare congiunta 7185 del 1/10/2026 (quote 2027) · InformazioneFiscale · Edotto · EcNews"
S_REQ = "InformazioneFiscale (SPID, PEC INI-PEC/INAD, CPI 8 giorni, asseverazione) · InfoImmigrazione (max 3 domande, CPI 8 giorni) · Assolombarda · Arletti Partners · Provincia di Trento"
S_DOC = "Provincia autonoma di Trento (documenti, date) · Edotto (precompilazione 23/10-7/12 ore 20, riapertura 9-13/12, click day ore 9) · InformazioneFiscale"
S_PASSI = "Assolombarda (60 giorni, 6 mesi, conferma) · InfoImmigrazione + Diritto.it (Marocco: niente silenzio-assenso) · Edotto + EcNews (conferma 15 giorni, contratto di soggiorno 15 giorni) · Poste/Money.it (kit)"
S_FINE = "Circolare 7185/2026 via Edotto, EcNews, InformazioneFiscale · Assolombarda · Provincia di Trento"

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="01 · شنو هو الديكري فلوسي", src=S_INTRO, items=[
   dict(k="head", text="الديكري فلوسي 2027", at=0.2, until="عندك خوك", sub="دليل عملي خطوة بخطوة · Decreto flussi 2027"),
   dict(k="people", at="عندك خوك", until="الطريق القانوني", box=(160, 320, 1760, 860), people=["worker", "man"],
        say=[dict(who=0, text="خويا باغي يجي يخدم هنا", at=0.6), dict(who=1, text="كيفاش نجيبوه بالقانون؟", at=2.6, bg="green")]),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Beni Mellal", "Bergamo"], labels=False, at="الطريق القانوني", until="معلومة مهمة", box=(160, 200, 1760, 880)),
   dict(k="people", at="معلومة مهمة", until="هاد العام كاينين", box=(160, 320, 1760, 860), people=["office", "worker"],
        say=[dict(who=1, text="شكون اللي كيدير الطلب؟", at=0.8), dict(who=0, text="المعلم، ماشي الخدام", at=2.6, bg="green")]),
   dict(k="big", text="165.850", at="هاد العام كاينين", until="منهم ستة", y=440, size=220, color=GOLD, sub="بلاصة فـ2027 · Quote 2027"),
   dict(k="bars", at="منهم ستة", until="فهاد الفيديو", box=(160, 300, 1760, 860), bars=[
     ["الخدمة الموسمية", 89000, "89.000", "green"], ["ماشي موسمية", 76200, "76.200", "gold"], ["فيهم: العناية بالعائلة", 14000, "14.000", "red"]]),
   dict(k="icons", at="فهاد الفيديو", until="وناخدو مثال", box=(160, 300, 1760, 860), items=[
     ["scale", "الشروط", "gold"], ["calendar", "الوراق والتواريخ", "blue"], ["clipboard-check", "الخطوات", "green"], ["alert-triangle", "الغلطات", "red"]], gap=1.8),
   dict(k="map", view="italy", hl=["Lombardia"], pins=["Bergamo"], labels=False, at="وناخدو مثال", box=R_BOX),
   dict(k="people", at="وناخدو مثال", box=L_BOX, people=["worker"],
        say=[dict(who=0, text="باغي نجيب حمزة من بني ملال", at=2.0, bg="green")]),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="02 · الشروط", src=S_REQ, items=[
   dict(k="chapter", num="02", title="الشروط", at=0.1, until="الشرط اللول"),
   dict(k="icons", at="الشرط اللول", until="الشرط التاني", box=(160, 300, 1760, 860), items=[
     ["id", "السبيد ولا CIE", "gold"], ["building-bank", "البورطال ديال الداخلية", "blue"], ["mail", "البيك (PEC)", "green"]], gap=2.4),
   dict(k="big", text="3 طلبات", at="الشرط التاني", until="الشرط التالت", y=440, size=200, color=GOLD, sub="فالعام · إلا دار المعلم الطلب بوحدو"),
   dict(k="people", at="الشرط التالت", until="إلا ما جاوبوش", box=(160, 320, 1760, 860), people=["clerk", "office"],
        say=[dict(who=1, text="كاين شي خدام هنا فإيطاليا؟", at=1.2), dict(who=0, text="مكتب التشغيل كيجاوب", at=4.5, bg="green")]),
   dict(k="calendar", at="إلا ما جاوبوش", until="الشرط الرابع", box=(160, 260, 1760, 860), day=8, month="أيام", sub="إلا ما جاوبش: كمل"),
   dict(k="head", text="الأسيفيراتسيوني", at="الشرط الرابع", until="ولكن إلا داز", sub="Asseverazione · كونسولينطي، كومرشاليستا ولا محامي"),
   dict(k="vs", at="ولكن إلا داز", until="وفي كل", box=(260, 360, 1660, 880),
        left=dict(title="الشركة بوحدها", value="خاصها", sub="الأسيفيراتسيوني", icon="file-certificate", color="red"),
        right=dict(title="عن طريق الجمعية", value="ما خاصاش", sub="جمعية المعلمين", icon="users", color="green"), gap=1.5),
   dict(k="icons", at="وفي كل", until="يوسف عندو", box=(160, 320, 1760, 840), items=[
     ["cash", "الصالير ديال الكونطرا الجماعية", "gold"], ["home", "السكن ديال الخدام", "green"]], gap=2.0),
   dict(k="people", at="يوسف عندو", box=(160, 320, 1760, 860), people=["worker", "office"],
        say=[dict(who=0, text="عندي شركة ديال البني", at=0.4), dict(who=1, text="خاصك الأسيفيراتسيوني ولا الجمعية", at=2.4, bg="green")]),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="03 · الوراق والتواريخ", src=S_DOC, items=[
   dict(k="chapter", num="03", title="الوراق والتواريخ", at=0.1, until="المعلم كيحضر"),
   dict(k="icons", at="المعلم كيحضر", until="ودابا التواريخ", box=(160, 300, 1760, 860), items=[
     ["e-passport", "باسبور الخدام", "blue"], ["building-factory", "وراق الشركة", "gold"], ["file-text", "الكونطرا المقترحة", "green"], ["home", "السكن (الإيدونيتا)", "red"]], gap=2.0),
   dict(k="calendar", at="أولا، التعمير", until="ومن تسعود", box=L_BOX, day=7, month=12, sub="آخر أجل للتعمير · 20:00"),
   dict(k="people", at="بلا هاد", until="ومن تسعود", box=R_BOX, people=["office"],
        say=[dict(who=0, text="بلا تعمير ما كاين كليك داي", at=0.4, bg="red")]),
   dict(k="head", text="من 9 حتى 13 دجنبر", at="ومن تسعود", until="ثانيا،", y=380, sub="غير باش تكمل الطلبات اللي بديتي · ماشي طلبات جداد"),
   dict(k="steps", at="ثانيا،", until="الطلبات كتدخل", box=(160, 200, 1760, 860), steps=[
     ["الفلاحة الموسمية", "12/1"], ["السياحة الموسمية", "9/2"], ["الخدمة ماشي موسمية", "16/2"], ["العناية بالعائلة", "18/2"]], gap=3.2, check_after=0.8),
   dict(k="people", at="الطلبات كتدخل", until="ويوسف؟", box=(160, 320, 1760, 860), people=["man", "hijab", "worker"],
        say=[dict(who=1, text="الساعة 9:00 بالضبط", at=0.5), dict(who=2, text="اللي سبق كياخد البلاصة", at=2.6, bg="green")]),
   dict(k="map", view="italy", hl=["Lombardia"], pins=["Bergamo"], labels=False, at="ويوسف؟", box=R_BOX),
   dict(k="calendar", at="ويوسف؟", box=L_BOX, day=16, month=2, sub="الكليك داي ديال يوسف · 9:00"),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="04 · الخطوات", src=S_PASSI, items=[
   dict(k="chapter", num="04", title="الخطوات", at=0.1, until="الخطوة اللولة"),
   dict(k="steps", at="الخطوة اللولة", until="القانون كيقول", box=(160, 220, 1760, 840), steps=[
     ["كود فالبيك والكليك داي", "1"], ["السبورطيلو أونيكو والكويستورا", "2"]], gap=6.0, check_after=1.0),
   dict(k="bars", at="القانون كيقول", until="ولكن رد", box=(160, 320, 1760, 840), bars=[
     ["ماشي موسمية (يوم)", 60, "60", "gold"], ["موسمية (يوم)", 20, "20", "green"]]),
   dict(k="people", at="ولكن رد", until="الخطوة التالتة", box=L_BOX, people=["clerk"],
        say=[dict(who=0, text="للمغاربة ماشي أوتوماتيكي", at=0.8, bg="red")]),
   dict(k="map", view="med", hl=["MAR"], pins=["Casablanca"], labels=False, at="ولكن رد", until="الخطوة التالتة", box=R_BOX),
   dict(k="calendar", at="الخطوة التالتة", until="الخطوة الرابعة", box=(160, 260, 1760, 860), day=15, month="يوم", sub="باش يأكد المعلم · ولا الطلب كيترفض"),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Casablanca", "Bergamo"], labels=False, at="الخطوة الرابعة", until="الخطوة الخامسة", box=R_BOX),
   dict(k="people", at="الخطوة الرابعة", until="والنولا أوسطا صالح", box=L_BOX, people=["worker"],
        say=[dict(who=0, text="الفيزا من القنصلية", at=1.5, bg="green")]),
   dict(k="calendar", at="والنولا أوسطا صالح", until="الخطوة الخامسة", box=L_BOX, day=6, month="شهور", sub="صلاحية النولا أوسطا"),
   dict(k="people", at="الخطوة الخامسة", until="الخطوة السادسة", box=L_BOX, people=["worker", "office"],
        say=[dict(who=1, text="نوقعو الكونطرا إلكترونيا", at=1.5, bg="green")]),
   dict(k="calendar", at="الخطوة الخامسة", until="الخطوة السادسة", box=R_BOX, day=15, month="يوم", sub="من الدخلة لإيطاليا"),
   dict(k="rows", at="الخطوة السادسة", until="فالمثال ديالنا", y=420, gap=150, size=54, rows=[
     ("الكيت · بيرميسو حتى عام", "116,46 €", "الخطوة السادسة", WHITE),
     ("الكيت · بيرميسو كثر من عام", "126,46 €", "ومية وستة وعشرين", GOLD),
   ]),
   dict(k="vs", at="فالمثال ديالنا", box=(260, 360, 1660, 880),
        right=dict(title="الكليك داي", value="16/2", sub="الطلب فالكوطا", icon="calendar", color="gold"),
        left=dict(title="النولا أوسطا", value="17/4", sub="تقريبا · وممكن كثر", icon="file-certificate", color="green"), gap=2.5),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="05 · الغلطات والملخص", src=S_FINE, items=[
   dict(k="chapter", num="05", title="الغلطات اللي تبعد عليها", at=0.1, until="الغلطة اللولة"),
   dict(k="warn", text="تفوت 7 دجنبر بلا تعمير مسبق", at="الغلطة اللولة", until="الغلطة التالتة", y=300),
   dict(k="warn", text="البيك ما كيتشافش: 15 يوم ديال التأكيد كيفوتو", at="الغلطة التانية", until="الغلطة التالتة", y=440),
   dict(k="people", at="الغلطة التالتة", until="الغلطة الرابعة", box=L_BOX, people=["man"],
        say=[dict(who=0, text="شي واحد كيبيع الكونطرا؟ رد البال!", at=0.8, bg="red")]),
   dict(k="map", view="med", hl=["ITA", "MAR"], labels=False, at="الغلطة التالتة", until="الغلطة الرابعة", box=R_BOX),
   dict(k="warn", text="الكونطرا ديال الإقامة: 15 يوم من الدخلة", at="الغلطة الرابعة", until="نعاودو باختصار", y=300),
   dict(k="warn", text="النولا أوسطا: 6 شهور باش تطلب الفيزا", at="الغلطة الخامسة", until="نعاودو باختصار", y=440),
   dict(k="head", text="باختصار", at="نعاودو باختصار", until="هادشي معلومات"),
   dict(k="rows", at="نعاودو باختصار", until="هادشي معلومات", y=360, gap=100, size=46, rows=[
     ("التعمير المسبق حتى", "7/12", "التعمير حتى", WHITE),
     ("الكليك داي", "12/1 - 18/2", "الكليك داي من", GOLD),
     ("النولا أوسطا (يوم) · ممكن كثر", "60", "ستين يوم للنولا", WHITE),
     ("الكونطرا ديال الإقامة (يوم)", "15", "والكونطرا فخمسطاش", GREEN),
   ]),
   dict(k="people", at="هادشي معلومات", until="وإلا عجبك", box=(160, 300, 1760, 860), people=["hijab", "worker"],
        say=[dict(who=0, text="عندك شي واحد فالمغرب باغي يخدم؟", at=3.0, bg="green"), dict(who=1, text="ولد خالتي!", at=5.5)]),
   dict(k="cta", at="وإلا عجبك", text="ابوني فالقناة", sub="كل نهار دليل جديد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("الديكري فلوسي 2027", (236, 196, 96)), "جيب خدام من المغرب", "الخطوات والتواريخ"],
  num="16/2", numsub="Decreto flussi 2027 · click day",
  bottom="مغاربة إيطاليا · دليل عملي بالدارجة",
)
