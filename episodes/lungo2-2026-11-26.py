import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_J1 = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-26-f.json"), encoding="utf-8"))
_J2 = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-26-r.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo2-2026-11-26-final")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = {k: v.replace("گ", "ك") for k, v in {**_J1["blocks"], **_J2["blocks"]}.items()}

S_HOME = "مغاربة إيطاليا · دليل عملي بالدارجة"
S_REQ = "D.Lgs. 230/2021 · DL 19/2026 art. 7-bis conv. L. 50/2026 · INPS news 22/1/2026 · InformazioneFiscale · Panorama"
S_IMP = "INPS circ. 7/2026 · Money.it · LentePubblica · calcoli nostri"
S_DOC = "INPS · Min. Lavoro (ISEE) · InformazioneFiscale · TuttoCalcolato"
S_MA = "INPS circ. 81/2026 · Edotto · InformazioneFiscale · Panorama · CGN (immobili esteri)"
S_STEP = "INPS · InformazioneFiscale · Money.it · LentePubblica · calcoli nostri"
S_CASI = "INPS · InformazioneFiscale · LentePubblica · D.Lgs. 83/2026"
S_QA = "Fonti dei capitoli 01-07"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850); FULL = (160, 300, 1760, 860); MID = (260, 220, 1660, 840)
ICB = (160, 330, 1760, 860); VSB = (260, 220, 1660, 820); BARB = (160, 330, 1760, 840); BIGMAP = (160, 200, 1760, 880)

MED_TO = dict(view="med", hl=["ITA", "MAR"], route=["Casablanca", "Torino", "plane"], pins=["Casablanca", "Torino"], labels=False)
MED_BS = dict(view="med", hl=["ITA", "MAR"], route=["Casablanca", "Brescia", "plane"], pins=["Casablanca", "Brescia"], labels=False)
MED_GE = dict(view="med", hl=["ITA", "MAR"], route=["Tanger", "Genova", "ship"], pins=["Tanger", "Genova"], labels=False)
MED_MI = dict(view="med", hl=["ITA", "MAR"], route=["Fes", "Milano", "plane"], pins=["Fes", "Milano"], labels=False)
MAROC = dict(view="maroc", hl=["MAR"], pins=["Rabat"], labels=False)
N_BS = dict(view="north", pins=["Brescia"], labels=False)
N_TO = dict(view="north", pins=["Torino"], labels=False)
N_BO = dict(view="north", pins=["Bologna"], labels=False)
N_MI = dict(view="north", pins=["Milano"], labels=False)
N_GE = dict(view="north", pins=["Genova"], labels=False)
N_BG = dict(view="north", pins=["Bergamo"], labels=False)
N_PD = dict(view="north", pins=["Padova"], labels=False)
S_NA = dict(view="south", pins=["Napoli"], labels=False)
IT_ALL = dict(view="italy", pins=["Torino", "Bologna", "Napoli"], labels=False)
IT_RM = dict(view="italy", pins=["Roma"], labels=False)

BLOCKS = [
 # ---------------------------------------------------------------- 01
 dict(audio="A.wav", text=T["A"], chapter="01 · شكون خاصو هاد الدليل", src=S_HOME, items=[
   dict(k="head", text="الأسينيو أونيكو ديال الإينبس", at=0.2, until="عندك ولد صغير ولا جوج", sub="فلوس كل شهر على الولاد"),
   dict(k="people", at="عندك ولد صغير ولا جوج", until="هاد الفيديو ليك", box=FULL, people=["woman", "child", "man"],
        say=[dict(who=0, text="شحال كنشدو؟", at=1.0, bg="gold"), dict(who=2, text="والولاد فالمغرب؟", at=5.5, bg="green")]),
   dict(k="vs", at="خاصنا نبداو بحاجة مهمة", until="والمبلغ ماشي بحال بحال", box=VSB,
        right=dict(title="بونوس", value="مرة وحدة", sub="", icon="ticket", color="grey"),
        left=dict(title="الأسينيو أونيكو", value="كل شهر", sub="حتى 21 عام فبعض الحالات", icon="calendar", color="green"), gap=2.0),
   dict(k="icons", at="والمبلغ ماشي بحال بحال", until="وفهاد الدليل غادي نجاوبو", box=ICB, items=[
     ["file-certificate", "الإيزي", "gold"], ["users", "عدد الولاد", "blue"], ["calendar", "العمر", "green"], ["briefcase", "الخدمة", "blue"]], gap=1.5, cols=4),
   dict(k="steps", at="وفهاد الدليل غادي نجاوبو", until="ومن بعد، غادي نشوفو الجانب المغربي", box=MID, steps=[
     ["شكون عندو الحق", "1"], ["البيرميسو والعامين", "2"], ["شحال كتشد", "3"], ["الطلب والخلاص", "4"]], gap=2.0, check_after=0.6),
   dict(k="map", at="ومن بعد، غادي نشوفو الجانب المغربي", until="وغادي نديرو الحساب", box=BIGMAP, **MED_TO),
   dict(k="calendar", at="وغادي نديرو الحساب", until="وعندنا ربعة ديال الحالات", box=MID, day=12, month="شهر", sub="الحساب ولد بولد"),
   dict(k="text", text="ربعة ديال الحالات", at="وعندنا ربعة ديال الحالات", until="الحالة الأولى، يوسف", y=520, size=96, color=GOLD),
   dict(k="map", at="الحالة الأولى، يوسف", until="الحالة التانية، خديجة", box=L_BOX, **N_TO),
   dict(k="people", at="الحالة الأولى، يوسف", until="الحالة التانية، خديجة", box=R_BOX, people=["man", "child"],
        say=[dict(who=0, text="يوسف · تورينو", at=0.8, bg="gold")]),
   dict(k="map", at="الحالة التانية، خديجة", until="الحالة التالتة، كريم", box=L_BOX, **N_BO),
   dict(k="people", at="الحالة التانية، خديجة", until="الحالة التالتة، كريم", box=R_BOX, people=["hijab", "girl"],
        say=[dict(who=0, text="خديجة · بولونيا", at=0.8, bg="gold")]),
   dict(k="map", at="الحالة التالتة، كريم", until="والحالة الرابعة، رشيد", box=L_BOX, **N_MI),
   dict(k="people", at="الحالة التالتة، كريم", until="والحالة الرابعة، رشيد", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="ما عنديش الإيزي", at=2.5, bg="red")]),
   dict(k="map", at="والحالة الرابعة، رشيد", until="فهاد الدليل غادي نمشيو", box=BIGMAP, **MED_BS),
   dict(k="rows", at="فهاد الدليل غادي نمشيو", until="وكل معلومة فهاد الفيديو", y=215, gap=78, size=40, rows=[
     ("شكون خاصو هاد الدليل", "01", "الأول، شكون"),
     ("الشروط", "02", "التاني، الشروط"),
     ("شحال والزيادات", "03", "التالت، شحال"),
     ("الوراق والإيزي", "04", "الرابع، الوراق"),
     ("المغرب", "05", "الخامس، الجانب"),
     ("الخطوات والخلاص", "06", "السادس، الخطوات"),
     ("الحالات والأخطاء", "07", "السابع، الحالات"),
     ("سؤال وجواب", "08", "التامن، سؤال"),
     ("اللائحة النهائية", "09", "والتاسع، لائحة"),
   ]),
   dict(k="icons", at="وكل معلومة فهاد الفيديو", until="وعقل مزيان", box=ICB, items=[
     ["building-bank", "الإينبس", "blue"], ["scale", "القانون", "gold"], ["file-text", "الدوريات", "green"]], gap=1.5),
   dict(k="warn", text="محتوى إخباري · ماشي استشارة", at="وعقل مزيان", until="وحاجة أخيرة قبل ما نبداو", y=600),
   dict(k="people", at="وحاجة أخيرة قبل ما نبداو", until=None, box=FULL, people=["woman", "man"],
        say=[dict(who=0, text="كتب سؤالك", at=1.0, bg="green"), dict(who=1, text="سيفي الفيديو", at=6.0, bg="gold")]),
 ]),
 # ---------------------------------------------------------------- 02
 dict(audio="B.wav", text=T["B"], chapter="02 · الشروط", src=S_REQ, items=[
   dict(k="chapter", num="02", title="الشروط بالتفصيل", at=0.1, until="جا بمرسوم تشريعي"),
   dict(k="big", text="230/2021", sub="المرسوم التشريعي ديال الأسينيو أونيكو", at="جا بمرسوم تشريعي", until="الشرط الأول: البيرميسو"),
   dict(k="icons", at="الشرط الأول: البيرميسو", until="وعندنا خبر مزيان", box=ICB, items=[
     ["id", "الكارطا", "green"], ["briefcase", "الخدمة · +6 شهور", "blue"], ["school", "البحث · +6 شهور", "gold"]], gap=3.5),
   dict(k="people", at="وعندنا خبر مزيان", until="الشرط التاني: تكون ساكن", box=FULL, people=["worker", "clerk"],
        say=[dict(who=0, text="انتظار الخدمة؟", at=1.0, bg="gold"), dict(who=1, text="إيه · مع تحفظ", at=6.0, bg="blue")]),
   dict(k="map", at="الشرط التاني: تكون ساكن", until="الشرط التالت: تكون خاضع", box=BIGMAP, **IT_ALL),
   dict(k="vs", at="الشرط التالت: تكون خاضع", until="الشرط الرابع، وهادا تبدل", box=VSB,
        right=dict(title="الضريبة ما خرجاتش", value="كيتحسب", sub="دخل صغير", icon="receipt-tax", color="green"),
        left=dict(title="خلصتي الضريبة", value="كيتحسب", sub="", icon="receipt", color="green"), gap=4.0),
   dict(k="vs", at="الشرط الرابع، وهادا تبدل", until="ولكن عقل: هادشي", box=VSB,
        right=dict(title="قبل", value="عامين", sub="ديال السكنى", icon="clock", color="red"),
        left=dict(title="من 21/4/2026", value="تحيد", sub="DL 19/2026", icon="scale", color="green"), gap=5.0),
   dict(k="warn", text="البيرميسو المناسب باقي شرط", at="ولكن عقل: هادشي", until="وإلى كنتي جديد فإيطاليا", y=560),
   dict(k="people", at="وإلى كنتي جديد فإيطاليا", until="دابا الشروط ديال الولاد", box=FULL, people=["man", "office"],
        say=[dict(who=1, text="سول الباترونا", at=1.0, bg="green")]),
   dict(k="steps", at="دابا الشروط ديال الولاد", until="كيقرا فالمدرسة", box=MID, steps=[
     ["قاصر · ديما", "1"], ["من 18 حتى 21 · بشروط", "2"], ["إعاقة · بلا حد", "3"]], gap=2.5, check_after=0.6),
   dict(k="icons", at="كيقرا فالمدرسة", until="والولد اللي عندو إعاقة، كيتحسب", box=ICB, items=[
     ["school", "كيقرا", "blue"], ["briefcase", "تحت 8.000 €", "gold"], ["building-bank", "مكتب التشغيل", "green"], ["heart", "الخدمة المدنية", "blue"]], gap=2.5, cols=4),
   dict(k="map", at="مثال: سارة", until="وشرط أخير", box=L_BOX, **N_PD),
   dict(k="people", at="مثال: سارة", until="أما إلى طلع الدخل", box=R_BOX, people=["student"],
        say=[dict(who=0, text="6.000 € فالعام", at=2.0, bg="green")]),
   dict(k="bars", at="أما إلى طلع الدخل", until="وشرط أخير", box=R_BOX, bars=[
     ["سارة", 6000, "6.000 €", "green"], ["الحد", 8000, "8.000 €", "gold"]], gap=1.5),
   dict(k="vs", at="وشرط أخير", until=None, box=VSB,
        right=dict(title="بلا إيزي", value="58,30 €", sub="الأدنى", icon="x", color="red"),
        left=dict(title="مع الإيزي", value="203,80 €", sub="حتى", icon="file-certificate", color="green"), gap=6.0),
 ]),
 # ---------------------------------------------------------------- 03
 dict(audio="C.wav", text=T["C"], chapter="03 · شحال والزيادات", src=S_IMP, items=[
   dict(k="chapter", num="03", title="شحال كتشد", at=0.1, until="بعد الزيادة ديال واحد"),
   dict(k="big", text="1,4%", sub="الزيادة ديال 2026", at="بعد الزيادة ديال واحد", until="نبداو بالولد القاصر"),
   dict(k="bars", at="نبداو بالولد القاصر", until="وبين هاد جوج الأرقام", box=BARB, bars=[
     ["الإيزي تحت 17.468", 203.8, "203,80 €", "green"], ["فوق 46.582 · بلا إيزي", 58.3, "58,30 €", "red"]], gap=6.0),
   dict(k="text", text="فالشهر · على كل ولد قاصر", at="نبداو بالولد القاصر", until="وبين هاد جوج الأرقام", y=880, size=44, color=GREY),
   dict(k="steps", at="وبين هاد جوج الأرقام", until="الولد من تمنطاش حتى عشرين", box=MID, steps=[
     ["17.468 € · 203,80 €", "1"], ["الإيزي كيطلع · المبلغ كينقص", "2"], ["46.582 € · 58,30 €", "3"]], gap=1.2),
   dict(k="bars", at="الولد من تمنطاش حتى عشرين", until="ودابا الزيادات", box=BARB, bars=[
     ["الأعلى", 99.1, "99,10 €", "green"], ["الأدنى", 29.1, "29,10 €", "gold"]], gap=3.0),
   dict(k="people", at="ودابا الزيادات", until="الزيادة الأولى", box=FULL, people=["hijab", "man"],
        say=[dict(who=0, text="كاينين زيادات؟", at=1.0, bg="gold")]),
   dict(k="icons", at="الزيادة الأولى", until="الزيادة التالتة", box=ICB, items=[
     ["heart", "تحت عام · زيادة النص", "green"], ["users", "3 ولاد · الصغار", "blue"]], gap=6.0),
   dict(k="icons", at="الزيادة التالتة", until="الزيادة الخامسة", box=ICB, items=[
     ["user", "من التالت · 99,10", "gold"], ["users", "4 ولاد · 150 €", "green"]], gap=5.0),
   dict(k="icons", at="الزيادة الخامسة", until="دابا الحساب ديال الحالات", box=ICB, items=[
     ["briefcase", "بجوج خدامين · 34,90", "blue"], ["user", "الأم تحت 21 · 23,30", "gold"], ["heart", "الإعاقة · 122,30", "green"]], gap=3.5),
   dict(k="map", at="دابا الحساب ديال الحالات", until="وفالعام، ربع آلاف", box=L_BOX, **N_TO),
   dict(k="people", at="دابا الحساب ديال الحالات", until="وفالعام، ربع آلاف", box=R_BOX, people=["man", "child", "girl"],
        say=[dict(who=0, text="407,60 € فالشهر", at=6.0, bg="green")]),
   dict(k="big", text="4.891 €", sub="يوسف · فالعام", at="وفالعام، ربع آلاف", until="خديجة فبولونيا"),
   dict(k="map", at="خديجة فبولونيا", until="البنت ديال ربع سنين", box=L_BOX, **N_BO),
   dict(k="rows", at="البنت ديال ربع سنين", until="وكريم فميلانو", y=300, gap=120, size=46, rows=[
     ("البنت · 4 سنين", "203,80 €", "البنت ديال ربع سنين"),
     ("الولد · تحت عام · 50%+", "305,70 €", "والولد اللي تزاد هاد العام"),
     ("المجموع فالشهر", "509,50 €", "المجموع: خمس مية", GOLD),
   ]),
   dict(k="map", at="وكريم فميلانو", until="لو كان الإيزي ديالو", box=L_BOX, **N_MI),
   dict(k="people", at="وكريم فميلانو", until="لو كان الإيزي ديالو", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="116,60 €", at=3.0, bg="red")]),
   dict(k="vs", at="لو كان الإيزي ديالو", until=None, box=VSB,
        right=dict(title="بلا إيزي", value="116,60 €", sub="كريم", icon="x", color="red"),
        left=dict(title="مع الإيزي", value="407,60 €", sub="بحال يوسف", icon="file-certificate", color="green"), gap=4.0),
 ]),
 # ---------------------------------------------------------------- 04
 dict(audio="D.wav", text=T["D"], chapter="04 · الوراق والإيزي", src=S_DOC, items=[
   dict(k="chapter", num="04", title="الوراق والإيزي", at=0.1, until="الأول، الهوية الرقمية"),
   dict(k="icons", at="الأول، الهوية الرقمية", until="التاني، الكود فيسكال", box=ICB, items=[
     ["key", "السبيد", "blue"], ["id", "الكارطا الإلكترونية", "green"], ["building-bank", "الباترونا", "gold"]], gap=1.5),
   dict(k="people", at="التاني، الكود فيسكال", until="التالت، البيرميسو", box=FULL, people=["man", "child"],
        say=[dict(who=0, text="الكود فيسكال ديال الولد", at=1.0, bg="gold")]),
   dict(k="icons", at="التالت، البيرميسو", until="والخامس، والأهم", box=ICB, items=[
     ["license", "البيرميسو", "blue"], ["wallet", "الإيبان", "green"]], gap=2.5),
   dict(k="calendar", at="والإيزي كيموت كل عام", until="الإيزي ديال العام الجاي", box=MID, day=31, month=12, sub="كيسالي الإيزي · كل عام"),
   dict(k="vs", at="الإيزي ديال العام الجاي", until="باش دير الإيزي، كاينين", box=VSB,
        right=dict(title="الصولد ديال اليوم", value="لا", sub="", icon="x", color="red"),
        left=dict(title="مداخيل 2025 · 31/12/2025", value="إيه", sub="الإيزي 2027", icon="calendar", color="green"), gap=5.0),
   dict(k="map", at="باش دير الإيزي، كاينين", until="الطريق التانية: الكاف", box=L_BOX, **N_TO),
   dict(k="steps", at="باش دير الإيزي، كاينين", until="الطريق التانية: الكاف", box=R_BOX, steps=[
     ["الموقع · السبيد", "1"], ["الموافقة ديال الكبار", "2"], ["زيد اللي ناقص", "3"]], gap=4.0),
   dict(k="people", at="الطريق التانية: الكاف", until="والوراق اللي خاصك تحضر", box=FULL, people=["office", "woman"],
        say=[dict(who=1, text="شحال الثمن؟", at=1.5, bg="gold")]),
   dict(k="icons", at="والوراق اللي خاصك تحضر", until="ودابا، باش تعرف تقرا", box=ICB, items=[
     ["id", "البطاقة", "blue"], ["file-text", "المداخيل", "gold"], ["home", "الكرا · الدار", "green"], ["car", "الطوموبيل", "blue"]], gap=2.5, cols=4),
   dict(k="head", text="كيفاش تقرا الورقة ديال الإيزي", at="ودابا، باش تعرف تقرا", until="الأول، الرقم النهائي", sub="03 · 02 · 01"),
   dict(k="bars", at="الأول، الرقم النهائي", until="التاني، التاريخ ديال الصلاحية", box=BARB, bars=[
     ["يوسف", 11800, "11.800 €", "green"], ["الحد الأعلى", 17468, "17.468 €", "gold"], ["الحد الأدنى", 46582, "46.582 €", "red"]], gap=6.0),
   dict(k="calendar", at="التاني، التاريخ ديال الصلاحية", until="والتالت، الملاحظات", box=MID, day=31, month=12, sub="الصلاحية"),
   dict(k="warn", text="اختلاف ولا نقص؟ صلحو", at="والتالت، الملاحظات", until="والإيزي اللي كيخص الولاد", y=560),
   dict(k="icons", at="والإيزي اللي كيخص الولاد", until="وإلى ما عرفتيش تدير", box=ICB, items=[
     ["building-hospital", "بونوس الكريش", "blue"], ["heart", "بونوس الولادة", "green"]], gap=4.0),
   dict(k="people", at="وإلى ما عرفتيش تدير", until=None, box=FULL, people=["clerk", "hijab"],
        say=[dict(who=0, text="جيب الوراق", at=2.0, bg="green")]),
 ]),
 # ---------------------------------------------------------------- 05
 dict(audio="E.wav", text=T["E"], chapter="05 · الجانب ديال المغرب", src=S_MA, items=[
   dict(k="chapter", num="05", title="الجانب ديال المغرب", at=0.1, until="نبداو بالممتلكات"),
   dict(k="map", at="نبداو بالممتلكات", until="ونفس الشي للكونطو", box=BIGMAP, **MAROC),
   dict(k="icons", at="ونفس الشي للكونطو", until="وبزاف ديال الناس كيقولو", box=ICB, items=[
     ["home", "الدار فالمغرب", "gold"], ["building-bank", "الكونطو فالمغرب", "blue"]], gap=4.0),
   dict(k="people", at="وبزاف ديال الناس كيقولو", until="مثال بسيط: نادية", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="ما غاديش يعرفو", at=1.0, bg="red"), dict(who=1, text="ترجع الفلوس", at=7.0, bg="blue")]),
   dict(k="map", at="مثال بسيط: نادية", until="إلى صرحات بيها", box=BIGMAP, **MED_GE),
   dict(k="vs", at="إلى صرحات بيها", until="والنصيحة: صرح بكلشي", box=VSB,
        right=dict(title="ما صرحاتش", value="خطر", sub="رد الفلوس", icon="alert-triangle", color="red"),
        left=dict(title="صرحات", value="آمن", sub="أسينيو أقل شوية", icon="clipboard-check", color="green"), gap=5.0),
   dict(k="people", at="والنصيحة: صرح بكلشي", until="دابا الولاد اللي باقيين", box=FULL, people=["office"],
        say=[dict(who=0, text="صرح بكلشي", at=1.0, bg="green")]),
   dict(k="map", at="دابا الولاد اللي باقيين", until="الجواب، حسب المصادر", box=BIGMAP, **MED_BS),
   dict(k="vs", at="الجواب، حسب المصادر", until="بدورية فيوليوز", box=VSB,
        right=dict(title="الولاد فالمغرب", value="لا", sub="", icon="x", color="red"),
        left=dict(title="الولاد فدولة أوروبية", value="إيه", sub="من 2026", icon="world", color="green"), gap=4.0),
   dict(k="big", text="81/2026", sub="الدورية ديال الإينبس · يوليوز", at="بدورية فيوليوز", until="وشنو يدير رشيد"),
   dict(k="steps", at="وشنو يدير رشيد", until="يعني الترتيب ديال رشيد", box=MID, steps=[
     ["يوصلو الولاد", "1"], ["الكود فيسكال", "2"], ["الريزيدينسا", "3"], ["الإيزي الجديد", "4"], ["الأسينيو", "5"]], gap=2.5),
   dict(k="people", at="يعني الترتيب ديال رشيد", until="وحاجة أخرى مهمة", box=FULL, people=["man", "child", "girl"],
        say=[dict(who=0, text="بكري ماشي من بعد", at=4.0, bg="gold")]),
   dict(k="map", at="وحاجة أخرى مهمة", until="وإلى كان عندك شك", box=L_BOX, **MED_MI),
   dict(k="vs", at="إلى رجعتي تعيش فالمغرب", until="وإلى كان عندك شك", box=R_BOX,
        right=dict(title="رجعتي تعيش", value="لا", sub="", icon="home", color="red"),
        left=dict(title="عطلة", value="عادي", sub="", icon="plane", color="green"), gap=1.0),
   dict(k="people", at="وإلى كان عندك شك", until=None, box=FULL, people=["hijab", "office"],
        say=[dict(who=0, text="الفيسبوك؟", at=1.0, bg="red"), dict(who=1, text="الباترونا", at=4.0, bg="green")]),
 ]),
 # ---------------------------------------------------------------- 06
 dict(audio="F.wav", text=T["F"], chapter="06 · الخطوات والخلاص", src=S_STEP, items=[
   dict(k="chapter", num="06", title="الخطوات والخلاص", at=0.1, until="وكاين أربعة ديال الطرق"),
   dict(k="icons", at="وكاين أربعة ديال الطرق", until="الخطوة الأولى", box=ICB, items=[
     ["world", "الموقع", "blue"], ["phone", "التطبيق", "green"], ["building-bank", "الباترونا", "gold"], ["mail", "الخدمة بالتيليفون", "blue"]], gap=1.5, cols=4),
   dict(k="steps", at="الخطوة الأولى", until="إمتى كتوصل الفلوس", box=MID, steps=[
     ["الإيزي", "1"], ["طلب واحد", "2"], ["الولاد والإيبان", "3"], ["الوصل", "4"], ["تبع الحالة", "5"]], gap=2.5),
   dict(k="calendar", at="إمتى كتوصل الفلوس", until="مثال: درتي الطلب", box=R_BOX, day=1, month="شهر", sub="الخلاص الأول · الشهر اللي من بعد"),
   dict(k="map", at="إمتى كتوصل الفلوس", until="مثال: درتي الطلب", box=L_BOX, **N_TO),
   dict(k="vs", at="مثال: درتي الطلب", until="ومن بعد، الخلاص كيكون", box=VSB,
        right=dict(title="الطلب", value="15 يناير", sub="", icon="file-text", color="blue"),
        left=dict(title="الخلاص الأول", value="آخر فبراير", sub="", icon="coin-euro", color="green"), gap=2.0),
   dict(k="calendar", at="وفدجنبر كيتقدم", until="مثال آخر: خديجة", box=MID, day=16, month=12, sub="16 و17 دجنبر 2026"),
   dict(k="map", at="مثال آخر: خديجة", until="ودابا أهم حاجة", box=L_BOX, **N_BO),
   dict(k="people", at="مثال آخر: خديجة", until="ودابا أهم حاجة", box=R_BOX, people=["hijab", "child"],
        say=[dict(who=0, text="الوقت هو الفلوس", at=8.0, bg="gold")]),
   dict(k="vs", at="ودابا أهم حاجة", until="التاريخ الأول: آخر فبراير", box=VSB,
        right=dict(title="الإيزي", value="كل عام", sub="جديد", icon="file-certificate", color="red"),
        left=dict(title="الطلب", value="أوتوماتيكي", sub="كيتجدد", icon="clipboard-check", color="green"), gap=4.0),
   dict(k="calendar", at="التاريخ الأول: آخر فبراير", until="التاريخ التاني: آخر يونيو", box=MID, day=28, month=2, sub="الإيزي الجديد · المبلغ الكامل من مارس"),
   dict(k="calendar", at="التاريخ التاني: آخر يونيو", until="مثال بالتواريخ", box=MID, day=30, month=6, sub="الفرق من مارس"),
   dict(k="map", at="مثال بالتواريخ", until="أما كريم", box=L_BOX, **N_TO),
   dict(k="people", at="مثال بالتواريخ", until="أما كريم", box=R_BOX, people=["man"],
        say=[dict(who=0, text="10 يناير · 49 يوم قبل", at=2.0, bg="green")]),
   dict(k="vs", at="أما كريم", until="وشي حوايج خاصك تعلم", box=VSB,
        right=dict(title="شتنبر", value="كيضيع", sub="مارس حتى غشت", icon="x", color="red"),
        left=dict(title="ماي", value="كيرجع", sub="الفرق من مارس", icon="coin-euro", color="green"), gap=3.0),
   dict(k="icons", at="وشي حوايج خاصك تعلم", until="ومن اليوم حتى واحد وتلاتين", box=ICB, items=[
     ["heart", "ولد جديد", "green"], ["school", "ولد كمل 18", "gold"], ["briefcase", "الخدمة", "blue"], ["wallet", "الإيبان", "blue"]], gap=1.5, cols=4),
   dict(k="big", text="35", sub="يوم حتى 31 دجنبر", at="ومن اليوم حتى واحد وتلاتين", until=None),
 ]),
 # ---------------------------------------------------------------- 07
 dict(audio="G.wav", text=T["G"], chapter="07 · الحالات والأخطاء", src=S_CASI, items=[
   dict(k="chapter", num="07", title="الحالات الخاصة والأخطاء", at=0.1, until="الحالة الأولى: تزاد ليك"),
   dict(k="people", at="الحالة الأولى: تزاد ليك", until="وما تنساش، كاين حتى", box=FULL, people=["woman", "child"],
        say=[dict(who=0, text="زيدو بلا تعطال", at=2.0, bg="green"), dict(who=0, text="50% حتى العام", at=7.0, bg="gold")]),
   dict(k="big", text="1.000 €", sub="بونوس الولادة · 120 يوم", at="وما تنساش، كاين حتى", until="الحالة التانية"),
   dict(k="map", at="الحالة التانية", until="الحالة التالتة", box=L_BOX, **N_PD),
   dict(k="people", at="الحالة التانية", until="الحالة التالتة", box=R_BOX, people=["student"],
        say=[dict(who=0, text="كنقرا ولا كنخدم؟", at=3.0, bg="gold")]),
   dict(k="calendar", at="الحالة التالتة", until="الحالة الرابعة", box=MID, day=90, month="يوم", sub="التجديد قبل ما يسالي البيرميسو"),
   dict(k="warn", text="انتظار الخدمة · مع تحفظ", at="الحالة الرابعة", until="الحالة الخامسة", y=560),
   dict(k="bars", at="الحالة الخامسة", until="دابا الأخطاء", box=BARB, bars=[
     ["الزيادة الثابتة", 150, "150 €", "green"], ["من الولد التالت", 99.1, "99,10 €", "gold"]], gap=5.0),
   dict(k="steps", bad=True, at="دابا الأخطاء", until="الغلطة الرابعة", box=MID, steps=[
     ["بلا إيزي · 291 أورو", "1"], ["الإيزي ما تجددش", "2"], ["خبيتي المغرب", "3"]], gap=3.0),
   dict(k="steps", bad=True, at="الغلطة الرابعة", until="الغلطة السابعة", box=MID, steps=[
     ["18 عام بلا تصريح", "4"], ["الولد الجديد متأخر", "5"], ["إيبان غالط", "6"]], gap=4.0),
   dict(k="people", at="الغلطة السابعة", until="والغلطة التامنة", box=FULL, people=["man", "worker"],
        say=[dict(who=0, text="عطيني الفلوس", at=1.0, bg="red"), dict(who=1, text="كذب", at=6.0, bg="green")]),
   dict(k="steps", bad=True, at="والغلطة التامنة", until="وشنو دير إلى الطلب ترفض", box=MID, steps=[
     ["الرسائل ما تقراوش", "8"], ["العائلة ناقصة", "9"], ["دخل كبير بلا تصريح", "10"]], gap=4.0),
   dict(k="steps", at="وشنو دير إلى الطلب ترفض", until="وإلى الإينبس طلب منك", box=MID, steps=[
     ["شوف السبب", "1"], ["إيزي جديد", "2"], ["الباترونا · إعادة النظر", "3"]], gap=4.0),
   dict(k="people", at="وإلى الإينبس طلب منك", until=None, box=FULL, people=["hijab", "office"],
        say=[dict(who=0, text="رسالة ديال الإينبس", at=1.0, bg="red"), dict(who=1, text="نشوفو الحل", at=4.0, bg="green")]),
 ]),
 # ---------------------------------------------------------------- 08
 dict(audio="H.wav", text=T["H"], chapter="08 · سؤال وجواب", src=S_QA, items=[
   dict(k="chapter", num="08", title="سؤال وجواب", at=0.1, until="السؤال الأول، من سعيد"),
   dict(k="map", at="السؤال الأول، من سعيد", until="الجواب: إيه، البيرميسو الموحد", box=L_BOX, **N_BG),
   dict(k="people", at="السؤال الأول، من سعيد", until="الجواب: إيه، البيرميسو الموحد", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="بيرميسو عامين؟", at=2.0, bg="gold")]),
   dict(k="text", text="إيه · أكثر من 6 شهور", at="الجواب: إيه، البيرميسو الموحد", until="السؤال التاني، من فاطمة", y=520, size=80, color=GREEN),
   dict(k="map", at="السؤال التاني، من فاطمة", until="الجواب: الطلب يقدر يديرو", box=L_BOX, **S_NA),
   dict(k="people", at="السؤال التاني، من فاطمة", until="الجواب: الطلب يقدر يديرو", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="شكون يطلب؟", at=3.0, bg="gold")]),
   dict(k="people", at="الجواب: الطلب يقدر يديرو", until="السؤال التالت، من حميد", box=FULL, people=["man", "woman"],
        say=[dict(who=0, text="واحد منا", at=1.0, bg="green")]),
   dict(k="map", at="السؤال التالت، من حميد", until="السؤال الرابع، من سلمى", box=BIGMAP, **MED_TO),
   dict(k="people", at="السؤال الرابع، من سلمى", until="الجواب: لا، كتاخدي", box=FULL, people=["girl"],
        say=[dict(who=0, text="بلا إيزي؟", at=2.0, bg="gold")]),
   dict(k="big", text="58,30 €", sub="الأدنى · بلا إيزي", at="الجواب: لا، كتاخدي", until="السؤال الخامس، من عبد الله"),
   dict(k="people", at="السؤال الخامس، من عبد الله", until="الجواب: إيه، حتى يكمل", box=FULL, people=["elder", "student"],
        say=[dict(who=1, text="19 عام · الجامعة", at=2.0, bg="gold")]),
   dict(k="calendar", at="الجواب: إيه، حتى يكمل", until="السؤال السادس، من خديجة", box=MID, day=21, month="عام", sub="ما دام كيقرا"),
   dict(k="map", at="السؤال السادس، من خديجة", until="الجواب: إلى كانت ديال باباك", box=BIGMAP, **MAROC),
   dict(k="vs", at="الجواب: إلى كانت ديال باباك", until="السؤال السابع، من يونس", box=VSB,
        right=dict(title="جزء باسمك", value="إيه", sub="صرح بيه", icon="home", color="gold"),
        left=dict(title="ديال الواليد وحدو", value="لا", sub="", icon="user", color="green"), gap=3.0),
   dict(k="people", at="السؤال السابع، من يونس", until="الجواب: فالأسبوع الأخير", box=FULL, people=["man"],
        say=[dict(who=0, text="إمتى الفلوس؟", at=2.0, bg="gold")]),
   dict(k="calendar", at="الجواب: فالأسبوع الأخير", until="السؤال التامن، من نزهة", box=MID, day=1, month="شهر", sub="الأسبوع الأخير ديال الشهر الجاي"),
   dict(k="people", at="السؤال التامن، من نزهة", until="السؤال التاسع، من رشيد", box=FULL, people=["hijab", "clerk"],
        say=[dict(who=0, text="انتظار الخدمة؟", at=2.0, bg="gold"), dict(who=1, text="إيه · مع تحفظ", at=7.0, bg="blue")]),
   dict(k="map", at="السؤال التاسع، من رشيد", until="الجواب: زيدو فالطلب", box=L_BOX, **N_GE),
   dict(k="people", at="السؤال التاسع، من رشيد", until="الجواب: زيدو فالطلب", box=R_BOX, people=["man", "child"],
        say=[dict(who=0, text="ولد تالت", at=3.0, bg="gold")]),
   dict(k="icons", at="الجواب: زيدو فالطلب", until="السؤال العاشر، من هند", box=ICB, items=[
     ["file-text", "زيدو فالطلب", "blue"], ["file-certificate", "إيزي جديد", "gold"], ["heart", "50% تحت عام", "green"]], gap=2.0),
   dict(k="people", at="السؤال العاشر، من هند", until="الجواب: كل عام كيتزاد", box=FULL, people=["woman"],
        say=[dict(who=0, text="العام الجاي؟", at=2.0, bg="gold")]),
   dict(k="warn", text="الأرقام الجديدة باقي ما خرجوش", at="الجواب: كل عام كيتزاد", until="السؤال الحادش", y=560),
   dict(k="map", at="السؤال الحادش", until="الجواب: لا. ما تخلص", box=L_BOX, **IT_RM),
   dict(k="people", at="السؤال الحادش", until="الجواب: لا. ما تخلص", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="وسيط بالفلوس؟", at=3.0, bg="red")]),
   dict(k="warn", text="الطلب بلا فلوس · ما تخلص حتى وسيط", at="الجواب: لا. ما تخلص", until="والسؤال التناش", y=560),
   dict(k="map", at="والسؤال التناش", until="الجواب: لا، ما تتسنايش", box=L_BOX, **N_BO),
   dict(k="people", at="والسؤال التناش", until="الجواب: لا، ما تتسنايش", box=R_BOX, people=["girl"],
        say=[dict(who=0, text="نتسنى 2027؟", at=4.0, bg="gold")]),
   dict(k="vs", at="الجواب: لا، ما تتسنايش", until="وإلى عندك سؤال آخر", box=VSB,
        right=dict(title="تسنيتي", value="كيضيع", sub="كل شهر", icon="clock", color="red"),
        left=dict(title="الطلب دابا", value="الشهر الجاي", sub="الخلاص", icon="coin-euro", color="green"), gap=3.0),
   dict(k="people", at="وإلى عندك سؤال آخر", until=None, box=FULL, people=["woman", "man"],
        say=[dict(who=0, text="كتب فالكومونتير", at=1.0, bg="green")]),
 ]),
 # ---------------------------------------------------------------- 09
 dict(audio="I.wav", text=T["I"], chapter="09 · اللائحة النهائية", src=S_HOME, items=[
   dict(k="chapter", num="09", title="اللائحة النهائية", at=0.1, until="واحد: تأكد من البيرميسو"),
   dict(k="rows", at="واحد: تأكد من البيرميسو", until="وعاود معايا الأرقام", y=170, gap=88, size=42, rows=[
     ("البيرميسو المناسب", "1", "واحد: تأكد"),
     ("الريزيدينسا والكود فيسكال", "2", "جوج: الريزيدينسا"),
     ("الإيزي من يناير", "3", "تلاتة: دير"),
     ("صرح بكلشي", "4", "ربعة: صرح"),
     ("طلب واحد", "5", "خمسة: دير"),
     ("الإيبان صحيح", "6", "ستة: حط"),
     ("علم بكل تبديل", "7", "سبعة: علم"),
     ("حتى وسيط", "8", "تمنية: ما تخلص", RED),
   ]),
   dict(k="rows", at="وعاود معايا الأرقام", until="ونرجعو للحالات ديالنا", y=230, gap=110, size=44, rows=[
     ("الأعلى · ولد قاصر", "203,80 €", "المبلغ الأعلى", GOLD),
     ("الأدنى", "58,30 €", "المبلغ الأدنى"),
     ("حد الإيزي للأعلى", "17.468 €", "الحد ديال الإيزي"),
     ("الولد تحت عام", "50%", "والولد تحت عام"),
     ("ربعة ديال الولاد", "150 €", "والعائلة ديال ربعة"),
   ]),
   dict(k="rows", at="ونرجعو للحالات ديالنا", until="وتلاتة ديال النصائح", y=260, gap=125, size=44, rows=[
     ("يوسف · تورينو", "407,60 €", "يوسف فتورينو"),
     ("خديجة · بولونيا", "509,50 €", "خديجة فبولونيا", GOLD),
     ("كريم · بلا إيزي", "-291 €", "كريم فميلانو", RED),
     ("رشيد · الولاد فالمغرب", "التجمع العائلي", "ورشيد فبريشا"),
   ]),
   dict(k="icons", at="وتلاتة ديال النصائح", until="والفصول ديال الفيديو", box=ICB, items=[
     ["calendar", "الإيزي من يناير", "green"], ["mail", "كلشي بالكتابة", "blue"], ["building-bank", "الباترونا", "gold"]], gap=3.0),
   dict(k="text", text="الفصول والمصادر فالوصف", at="والفصول ديال الفيديو", until="ودابا، سؤال ليك", y=600, size=64, color=GOLD),
   dict(k="people", at="ودابا، سؤال ليك", until="وإلى عرفتي شي واحد", box=FULL, people=["woman", "man"],
        say=[dict(who=0, text="درتي الإيزي؟", at=1.0, bg="gold"), dict(who=1, text="إيه ولا لا", at=4.0, bg="green")]),
   dict(k="people", at="وإلى عرفتي شي واحد", until="وإلى عجبك", box=FULL, people=["hijab", "worker"],
        say=[dict(who=0, text="صيفطو للعائلة", at=1.0, bg="gold")]),
   dict(k="cta", at="وإلى عجبك", text="ابوني فالقناة", sub="كل نهار دليل مفيد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("عندك ولاد فإيطاليا؟", (236, 196, 96)), "الأسينيو أونيكو 2026", "شحال كتشد على كل ولد"],
  num="203,80 €", numsub="حتى · فالشهر على كل ولد",
  bottom="مغاربة إيطاليا · دليل عملي بالدارجة",
)
