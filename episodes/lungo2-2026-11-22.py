import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_J1 = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-22-f.json"), encoding="utf-8"))
_J2 = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-22-r.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo2-2026-11-22-final")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = {k: v.replace("گ", "ك") for k, v in {**_J1["blocks"], **_J2["blocks"]}.items()}

S_HOME = "مغاربة إيطاليا · دليل عملي بالدارجة"
S_REQ = "INPS scheda ADI · Ministero del Lavoro (pagina ADI) · InformazioneFiscale 16/11/2026"
S_DOC = "INPS scheda ADI · Ministero del Lavoro · InformazioneFiscale · L. 199/2025 c. 208"
S_MAR = "Ministero del Lavoro (tempistiche, obblighi) · INPS scheda ADI · InformazioneFiscale"
S_STEP = "INPS · Ministero del Lavoro · InformazioneFiscale · QuiFinanza 24/2/2026"
S_CASI = "Ministero del Lavoro · INPS (msg 640/2026) · LeggiOggi · InformazioneFiscale"
S_ERR = "Ministero del Lavoro (tempistiche, obblighi e sanzioni) · INPS scheda ADI"
S_QA = "Fonti dei capitoli 01-07"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850); FULL = (160, 300, 1760, 860); MID = (260, 220, 1660, 840)
ICB = (160, 330, 1760, 860); VSB = (260, 220, 1660, 820); BARB = (160, 330, 1760, 840)

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="01 · شكون خاصو هاد الدليل", src=S_HOME, items=[
   dict(k="head", text="الأدي · الأسينيو دي إنكلوزيوني", at=0.2, until="هادي فلوس كل شهر", sub="الشروط والوراق والثمن والمدة · خطوة بخطوة"),
   dict(k="people", at=0.8, until="هادي فلوس كل شهر", box=FULL, people=["elder", "hijab", "man"],
        say=[dict(who=0, text="شنو هو الأدي؟", at=2.5), dict(who=1, text="واش عندي الحق؟", at=5.5, bg="gold")]),
   dict(k="icons", at="هادي فلوس كل شهر", until="ولكن الشروط ديالها", box=ICB, items=[
     ["calendar", "كل شهر", "green"], ["building-bank", "الإينبس", "blue"], ["key", "مساعدة الكرا", "gold"]], gap=2.0),
   dict(k="warn", text="أخطاء صغيرة كتضيع الحق", at="ولكن الشروط ديالها", until="قبل ما نبداو", y=640),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="قبل ما نبداو", until="غادي نشوفو كيفاش", box=L_BOX),
   dict(k="big", text="641 €", sub="تقريبا فالشهر · مصطفى", at="قبل ما نبداو", until="غادي نشوفو كيفاش", x=1380, y=470, size=200),
   dict(k="icons", at="غادي نشوفو كيفاش", until="فهاد الدليل غادي", box=ICB, items=[
     ["id", "شكون يطلب", "blue"], ["car", "الطوموبيل", "red"], ["home", "الدار فالمغرب", "gold"]], gap=3.0),
   dict(k="map", view="north", pins=["Torino", "Brescia", "Bologna"], labels=False,
        at="فهاد الدليل غادي", until="الأول، مصطفى فتورينو", box=(160, 200, 1760, 880)),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="الأول، مصطفى فتورينو", until="التانية، فاطمة", box=L_BOX),
   dict(k="people", at="الأول، مصطفى فتورينو", until="التانية، فاطمة", box=R_BOX, people=["elder"],
        say=[dict(who=0, text="63 عام · بوحدي", at=2.0, bg="gold")]),
   dict(k="map", view="north", pins=["Brescia"], labels=False, at="التانية، فاطمة", until="والتالت، حسن", box=L_BOX),
   dict(k="people", at="التانية، فاطمة", until="والتالت، حسن", box=R_BOX, people=["hijab", "child"],
        say=[dict(who=0, text="عندي جوج ولاد", at=2.0, bg="green")]),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Bologna", "Nador", "plane"], pins=["Bologna", "Nador"], labels=False,
        at="والتالت، حسن", until="كل واحد فيهم", box=L_BOX),
   dict(k="people", at="والتالت، حسن", until="كل واحد فيهم", box=R_BOX, people=["man"],
        say=[dict(who=0, text="عندي جزء من دار", at=3.0, bg="gold")]),
   dict(k="steps", at="كل واحد فيهم", until="الأدي ماشي لكل", box=MID, steps=[
     ["مصطفى · تورينو", "1"], ["فاطمة · بريشيا", "2"], ["حسن · بولونيا", "3"]], gap=1.8, check_after=0.5),
   dict(k="icons", at="الأدي ماشي لكل", until="إلى كنتي شاب", box=ICB, items=[
     ["school", "قاصر", "green"], ["heart", "إعاقة", "blue"], ["user", "فوق 60 عام", "gold"], ["stethoscope", "وضعية صعيبة", "red"]], gap=3.0),
   dict(k="people", at="إلى كنتي شاب", until="تسعة ديال الفصول", box=FULL, people=["student"],
        say=[dict(who=0, text="بوحدي وتحت الستين؟ لا", at=1.5, bg="red")]),
   dict(k="rows", at="تسعة ديال الفصول", until="وكل رقم فهاد الفيديو", y=215, gap=78, size=40, rows=[
     ("شكون خاصو هاد الدليل", "01", "الأول، شكون"),
     ("الشروط", "02", "التاني، الشروط"),
     ("الوراق فإيطاليا والإيزي", "03", "التالت، الوراق"),
     ("الدار والفلوس فالمغرب والسفر", "04", "الرابع، الدار"),
     ("الخطوات والمدة والحساب", "05", "الخامس، الخطوات"),
     ("الحالات الخاصة", "06", "السادس، الحالات"),
     ("الأخطاء والرفض", "07", "السابع، الأخطاء"),
     ("سؤال وجواب", "08", "التامن، سؤال"),
     ("اللائحة النهائية", "09", "والتاسع، لائحة"),
   ]),
   dict(k="icons", at="وكل رقم فهاد الفيديو", until="وعلاش هاد الموضوع مهم دابا؟", box=ICB, items=[
     ["file-certificate", "جوج مصادر", "blue"], ["calculator", "أمثلة بالحساب", "green"], ["scale", "ماشي استشارة قانونية", "gold"]], gap=3.0),
   dict(k="vs", at="وعلاش هاد الموضوع مهم دابا؟", until="والتانية، الإيزي ولا", box=VSB,
        right=dict(title="قبل", value="شهر", sub="التوقف من بعد 18 شهر", icon="clock", color="grey"),
        left=dict(title="من 2026", value="بلا توقف", sub="التجديد مباشرة", icon="calendar", color="green"), gap=4.0),
   dict(k="bars", at="والتانية، الإيزي ولا", until="وزيد على هادشي", box=BARB, bars=[
     ["قبل", 52500, "52.500 €", "grey"], ["دابا", 91500, "91.500 €", "green"], ["المدن الكبار", 120000, "120.000 €", "blue"]], gap=2.5),
   dict(k="text", text="الحد ديال دار السكنى فالإيزي", at="والتانية، الإيزي ولا", until="وزيد على هادشي", y=880, size=42, color=GREY),
   dict(k="calendar", at="وزيد على هادشي", until="يلاه نبداو", box=R_BOX, day=31, month=12, sub="2026 · كيسالي الإيزي"),
   dict(k="people", at="وزيد على هادشي", until="يلاه نبداو", box=L_BOX, people=["woman"],
        say=[dict(who=0, text="فيناير نجدد الإيزي", at=5.0, bg="green")]),
   dict(k="text", text="يلاه نبداو بالشروط", at="يلاه نبداو", y=520, size=80, color=GOLD),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="02 · الشروط", src=S_REQ, items=[
   dict(k="chapter", num="02", title="الشروط ديال الأدي", at=0.1, until="الشرط الأول هو العائلة"),
   dict(k="icons", at="الشرط الأول هو العائلة", until="الشرط التاني هو البيرميسو", box=ICB, items=[
     ["school", "قاصر", "green"], ["heart", "إعاقة", "blue"], ["user", "فوق 60", "gold"], ["stethoscope", "متبوع", "red"]], gap=1.2),
   dict(k="people", at="الشرط التاني هو البيرميسو", until="مواطن أوروبي", box=FULL, people=["clerk", "man"],
        say=[dict(who=1, text="شكون اللي يطلب؟", at=1.5, bg="gold")]),
   dict(k="icons", at="مواطن أوروبي", until="يعني إلى كان عندك", box=ICB, items=[
     ["world", "مواطن أوروبي", "blue"], ["id", "الكارطا دي سوجورنو", "green"], ["certificate", "الحماية الدولية", "gold"]], gap=4.0),
   dict(k="vs", at="يعني إلى كان عندك", until="الشرط التالت هو الإقامة", box=VSB,
        right=dict(title="بيرميسو الخدمة", value="لا", sub="ما يقدرش يطلب", icon="briefcase", color="red"),
        left=dict(title="شي واحد آخر", value="إيه", sub="عندو الكارطا: هو يطلب", icon="users", color="green"), gap=6.0),
   dict(k="big", text="5", sub="سنين فإيطاليا · الجوج اللولين بلا تقطيع", at="الشرط التالت هو الإقامة", until="وهاد الإقامة خاصها", y=430, size=300, color=GOLD),
   dict(k="map", view="italy", pins=["Torino", "Brescia", "Bologna"], labels=False, at="وهاد الإقامة خاصها", until="الشرط الرابع هو الإيزي", box=L_BOX),
   dict(k="people", at="وهاد الإقامة خاصها", until="الشرط الرابع هو الإيزي", box=R_BOX, people=["clerk"],
        say=[dict(who=0, text="الريزيدينسا فالكومون", at=1.0, bg="green")]),
   dict(k="big", text="10.140 €", sub="الإيزي · الحد الأقصى", at="الشرط الرابع هو الإيزي", until="الشرط الخامس هو المدخول", y=450, size=220),
   dict(k="bars", at="الشرط الخامس هو المدخول", until="هاد الرقم كيبدا", box=BARB, bars=[
     ["العتبة العادية", 6500, "6.500 €", "green"], ["كلهم فوق 67", 8190, "8.190 €", "gold"], ["بالكرا", 10140, "10.140 €", "blue"]], gap=6.0),
   dict(k="text", text="المدخول فالعام · مضروب فسلم التعادل", at="الشرط الخامس هو المدخول", until="هاد الرقم كيبدا", y=880, size=44, color=GREY),
   dict(k="steps", at="هاد الرقم كيبدا", until="وإلى كانت العائلة كلها", box=MID, steps=[
     ["الشخص الأول", "1"], ["كيطلع مع كل فرد", "+"], ["الحد الأقصى", "2,2"], ["مع إعاقة خطيرة", "2,3"]], gap=3.5, check_after=0.6),
   dict(k="people", at="وإلى كانت العائلة كلها", until="الشرط السادس هو الممتلكات", box=FULL, people=["elder", "woman"],
        say=[dict(who=0, text="حنا بجوج فوق 67", at=1.0, bg="gold"), dict(who=1, text="وساكنين بالكرا", at=6.0, bg="green")]),
   dict(k="vs", at="الشرط السادس هو الممتلكات", until="والفلوس فالبنكة", box=VSB,
        right=dict(title="دور وأراضي", value="30.000 €", sub="الحد الأقصى", icon="home-dollar", color="gold"),
        left=dict(title="دار السكنى", value="150.000 €", sub="ما كتحسبش تحت هاد الحد", icon="home", color="green"), gap=6.0),
   dict(k="rows", at="والفلوس فالبنكة", until="الشرط السابع", y=300, gap=110, size=50, rows=[
     ("شخص واحد", "6.000 €", "والفلوس فالبنكة"),
     ("كل فرد آخر", "+ 2.000 €", "وكتزاد ألفين"),
     ("الحد", "10.000 €", "حتى لعشرة آلاف"),
     ("كل ولد من بعد التاني", "+ 1.000 €", "وكتزاد ألف"),
   ]),
   dict(k="icons", at="الشرط السابع", until="الشرط التامن", box=ICB, items=[
     ["car", "فوق 1.600 سم³", "red"], ["clock", "36 شهر", "gold"], ["ship", "فلوكة", "blue"]], gap=3.0),
   dict(k="people", at="الشرط التامن", until="والشرط التاسع", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="درت الديميسيون", at=1.5, bg="red"), dict(who=1, text="جوستا كاوزا؟", at=8.0, bg="gold")]),
   dict(k="warn", text="حكم نهائي فالعشر سنين اللولين = ما كاينش الأدي", at="والشرط التاسع", until="دابا نرجعو لمصطفى", y=640),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="دابا نرجعو لمصطفى", until="إذن مصطفى عندو الحق", box=L_BOX),
   dict(k="steps", at="دابا نرجعو لمصطفى", until="إذن مصطفى عندو الحق", box=R_BOX, steps=[
     ["فوق الستين", "63"], ["الكارطا", "عندو"], ["الإقامة", "2008"], ["الإيزي", "7.000"], ["المدخول", "2.400"]], gap=3.5, check_after=0.6),
   dict(k="people", at="إذن مصطفى عندو الحق", box=FULL, people=["elder"],
        say=[dict(who=0, text="عندي الحق", at=0.8, bg="green")]),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="03 · الوراق فإيطاليا والإيزي", src=S_DOC, items=[
   dict(k="chapter", num="03", title="الوراق فإيطاليا", at=0.1, until="أول حاجة، الهوية"),
   dict(k="icons", at="أول حاجة، الهوية", until="بلا هادشي ما تقدرش", box=ICB, items=[
     ["fingerprint", "السبيد", "green"], ["id", "الكارطا الإلكترونية", "blue"], ["credit-card", "كارطا الصحة", "gold"]], gap=2.5),
   dict(k="people", at="بلا هادشي ما تقدرش", until="تاني حاجة، الإيزي", box=FULL, people=["hijab", "clerk"],
        say=[dict(who=0, text="ما عنديش السبيد", at=1.0, bg="gold"), dict(who=1, text="الباطرونا ولا الكاف", at=6.0, bg="green")]),
   dict(k="text", text="الإيزي = الأساس", at="تاني حاجة، الإيزي", until="وفيه كاينين", y=520, size=90, color=GOLD),
   dict(k="icons", at="وفيه كاينين", until="وعندنا فالقناة", box=ICB, items=[
     ["id", "الهوية والكودي فيسكالي", "blue"], ["file-text", "السي أو", "green"], ["key", "كونطرا الكرا", "gold"], ["building-bank", "البنكة والطوموبيل", "red"]], gap=3.0),
   dict(k="text", text="دليل الإيزي كاين فالقناة", at="وعندنا فالقناة", until="وهنا خبر زوين", y=640, size=60, color=GREEN),
   dict(k="map", view="italy", pins=["Milano", "Roma", "Torino"], labels=False, at="وهنا خبر زوين", until="تالت حاجة، البيرميسو", box=L_BOX),
   dict(k="vs", at="وهنا خبر زوين", until="تالت حاجة، البيرميسو", box=R_BOX,
        right=dict(title="عادي", value="91.500 €", sub="الدار ما كتحسبش", icon="home", color="green"),
        left=dict(title="المدن الكبار", value="120.000 €", sub="ميلانو · روما · تورينو", icon="building-bank", color="blue"), gap=5.0),
   dict(k="people", at="تالت حاجة، البيرميسو", until="رابع حاجة، الريزيدينسا", box=FULL, people=["man"],
        say=[dict(who=0, text="عندي الكارطا · خليت نسخة", at=1.5, bg="green")]),
   dict(k="calendar", at="رابع حاجة، الريزيدينسا", until="خامس حاجة", box=R_BOX, day=5, month="سنين", sub="فالريزيدينسا · الجوج اللولين بلا تقطيع"),
   dict(k="map", view="north", pins=["Brescia"], labels=False, at="رابع حاجة، الريزيدينسا", until="خامس حاجة", box=L_BOX),
   dict(k="vs", at="خامس حاجة", until="سادس حاجة", box=VSB,
        right=dict(title="كونطرا مسجلة", value="إيه", sub="مساعدة الكرا", icon="key", color="green"),
        left=dict(title="بلا تسجيل", value="لا", sub="ما كاينش مساعدة", icon="x", color="red"), gap=5.0),
   dict(k="icons", at="سادس حاجة", until="وسابع حاجة", box=ICB, items=[
     ["calendar", "التاريخ", "gold"], ["file-certificate", "البروتوكول", "blue"], ["building-hospital", "الإدارة", "green"]], gap=3.0),
   dict(k="icons", at="وسابع حاجة", until="دابا نشوفو فاطمة", box=ICB, items=[
     ["phone", "التيليفون", "green"], ["mail", "الإيمايل", "blue"]], gap=2.0),
   dict(k="map", view="north", pins=["Brescia"], labels=False, at="دابا نشوفو فاطمة", until="ولكن كاين مشكل", box=L_BOX),
   dict(k="people", at="دابا نشوفو فاطمة", until="ولكن كاين مشكل", box=R_BOX, people=["hijab", "child"],
        say=[dict(who=0, text="الإيزي 8.700 €", at=5.0, bg="green")]),
   dict(k="vs", at="ولكن كاين مشكل", until="وخاصهم يتأكدو", box=VSB,
        right=dict(title="فاطمة", value="لا", sub="بيرميسو العائلة", person="hijab", color="red"),
        left=dict(title="كريم", value="إيه", sub="الكارطا دي سوجورنو", person="man", color="green"), gap=7.0),
   dict(k="people", at="وخاصهم يتأكدو", until="والنقطة الأخيرة", box=FULL, people=["office", "man"],
        say=[dict(who=0, text="الإينبس كتحسب", at=2.0, bg="gold")]),
   dict(k="calendar", at="والنقطة الأخيرة", until="دير الدي إس أو الجديدة", box=MID, day=31, month=12, sub="2026 · كيموت الإيزي"),
   dict(k="calendar", at="دير الدي إس أو الجديدة", box=MID, day=1, month=1, sub="2027 · دي إس أو جديدة"),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="04 · الدار والفلوس فالمغرب والسفر", src=S_MAR, items=[
   dict(k="chapter", num="04", title="المغرب: الدار والفلوس والسفر", at=0.1, until="أول حاجة: الدار"),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Nador", "Agadir"], labels=False, at="أول حاجة: الدار", until="فالدي إس أو خاصك", box=L_BOX),
   dict(k="icons", at="أول حاجة: الدار", until="فالدي إس أو خاصك", box=R_BOX, items=[
     ["home", "دار", "gold"], ["users", "جزء ديال الوالدين", "blue"], ["tractor", "أرض فالبلاد", "green"]], gap=3.0),
   dict(k="big", text="30.000 €", sub="الدور والأراضي · حتى اللي فالمغرب", at="فالدي إس أو خاصك", until="خلينا نشوفو حسن", y=450, size=220),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Bologna", "Nador", "plane"], pins=["Bologna", "Nador"], labels=False,
        at="خلينا نشوفو حسن", until="ولكن إلى كانت عندو", box=L_BOX),
   dict(k="bars", at="خلينا نشوفو حسن", until="والسؤال اللي كيطرحو", box=R_BOX, bars=[
     ["جزء حسن", 25000, "25.000 €", "green"], ["العتبة", 30000, "30.000 €", "gold"], ["دار كاملة", 50000, "50.000 €", "red"]], gap=4.0),
   dict(k="people", at="والسؤال اللي كيطرحو", until="تاني حاجة: الكونطو", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="ما نصرحش وصافي؟", at=1.0, bg="gold"), dict(who=1, text="لا · فيه الحبس", at=6.0, bg="red")]),
   dict(k="icons", at="تاني حاجة: الكونطو", until="تالت حاجة، وهي الأهم", box=ICB, items=[
     ["building-bank", "بنكة مغربية", "gold"], ["wallet", "كتدخل فالفلوس", "blue"], ["clipboard-check", "صرح بيها", "green"]], gap=3.0),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Milano", "Casablanca", "plane"], pins=["Milano", "Casablanca"], labels=False,
        at="تالت حاجة، وهي الأهم", until="إلى غبتي على إيطاليا", box=FULL),
   dict(k="vs", at="إلى غبتي على إيطاليا", until="من غير إلى كان السبب", box=VSB,
        right=dict(title="متتابعين", value="2", sub="شهور برا إيطاليا", icon="plane", color="red"),
        left=dict(title="فالمجموع ف 18 شهر", value="4", sub="شهور برا إيطاليا", icon="calendar", color="red"), gap=4.0),
   dict(k="text", text="السبب صحي خطير بالوراق = ماشي مشكل", at="من غير إلى كان السبب", until="خلينا نشوفو مصطفى", y=640, size=60, color=GREEN),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Torino", "Casablanca", "plane"], pins=["Torino", "Casablanca"], labels=False,
        at="خلينا نشوفو مصطفى", until="الحل: يقصر", box=L_BOX),
   dict(k="people", at="خلينا نشوفو مصطفى", until="الحل: يقصر", box=R_BOX, people=["elder"],
        say=[dict(who=0, text="شهرين ونص فالصيف", at=2.0, bg="red")]),
   dict(k="vs", at="الحل: يقصر", until="رابع حاجة: الكارطا", box=VSB,
        right=dict(title="شهرين ونص", value="لا", sub="كيقطع الإقامة", icon="x", color="red"),
        left=dict(title="شهر واحد", value="إيه", sub="ويحسب الغيابات", icon="check", color="green"), gap=2.5),
   dict(k="icons", at="رابع حاجة: الكارطا", until="خامس حاجة: المعلومات", box=ICB, items=[
     ["world", "برا إيطاليا", "red"], ["shopping-cart", "أونلاين", "red"], ["cash", "تصيفط للمغرب", "red"]], gap=3.0),
   dict(k="icons", at="خامس حاجة: المعلومات", until="وسول الكاف كيفاش", box=ICB, items=[
     ["map-pin", "فين كاينة", "blue"], ["home", "المساحة", "green"], ["user", "شكون مولاها", "gold"], ["percentage", "الجزء ديالك", "red"]], gap=2.5),
   dict(k="people", at="وسول الكاف كيفاش", until="سادس حاجة", box=FULL, people=["woman", "office"],
        say=[dict(who=1, text="عندها قواعد خاصة", at=2.0, bg="gold")]),
   dict(k="calendar", at="سادس حاجة", until="وفالأخير، إلى بغيتي", box=R_BOX, day=15, month="يوم", sub="باش تعلم الإينبس بكل تبديل"),
   dict(k="people", at="سادس حاجة", until="وفالأخير، إلى بغيتي", box=L_BOX, people=["man"],
        say=[dict(who=0, text="ورثت جزء", at=2.0, bg="gold")]),
   dict(k="vs", at="وفالأخير، إلى بغيتي", box=VSB,
        right=dict(title="الحساب العادي", value="إيه", sub="باش تصيفط للعائلة", icon="building-bank", color="green"),
        left=dict(title="كارطا الأدي", value="لا", sub="ما كتخدمش", icon="credit-card", color="red"), gap=3.0),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="05 · الخطوات والمدة والحساب", src=S_STEP, items=[
   dict(k="chapter", num="05", title="الخطوات والمدة والفلوس", at=0.1, until="الخطوة الأولى"),
   dict(k="steps", at="الخطوة الأولى", until="الخطوة التانية", box=MID, steps=[["الدي إس أو", "1"], ["الإيزي", "2"]], gap=3.0, check_after=0.5),
   dict(k="people", at="الخطوة التانية", until="الخطوة التالتة", box=FULL, people=["clerk", "woman"],
        say=[dict(who=1, text="السبيد ولا الباطرونا؟", at=1.5, bg="gold"), dict(who=0, text="بجوج كيخدمو", at=7.0, bg="green")]),
   dict(k="icons", at="الخطوة التالتة", until="الخطوة الرابعة", box=ICB, items=[
     ["world", "السيسل", "blue"], ["clipboard-check", "الباد", "green"], ["alert-triangle", "بلا باد ما كاين خلاص", "red"]], gap=4.0),
   dict(k="people", at="الخطوة الرابعة", until="الخطوة الخامسة", box=FULL, people=["office"],
        say=[dict(who=0, text="من الشهر اللي من بعد الباد", at=4.0, bg="green")]),
   dict(k="vs", at="الخطوة الخامسة", until="فهاد الأيام", box=VSB,
        right=dict(title="الخلصة الأولى", value="15", sub="حدا 15 فالشهر", icon="calendar", color="gold"),
        left=dict(title="من بعد", value="27", sub="حدا 27 فالشهر", icon="calendar", color="green"), gap=3.0),
   dict(k="rows", at="فهاد الأيام", until="الخطوة السادسة", y=320, gap=120, size=52, rows=[
     ("خلصة عادية", "27/11", "سبعة وعشرين نونبر"),
     ("الخلصة الأولى", "15/12", "وخمسطاش دجنبر"),
     ("خلصة عادية قبل العيد", "23/12", "وتلاتة وعشرين دجنبر"),
   ]),
   dict(k="icons", at="الخطوة السادسة", until="الخطوة السابعة", box=ICB, items=[
     ["phone", "ميساج", "blue"], ["mailbox", "البوسطا", "gold"], ["credit-card", "كارطا الإنكلوزيوني", "green"]], gap=3.0),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="الخطوة السابعة", until="الخطوة التامنة", box=L_BOX),
   dict(k="calendar", at="الخطوة السابعة", until="الخطوة التامنة", box=R_BOX, day=120, month="يوم", sub="من الباد · الخدمات الاجتماعية"),
   dict(k="people", at="الخطوة التامنة", until="دابا الحساب ديال مصطفى", box=FULL, people=["worker", "clerk"],
        say=[dict(who=1, text="مركز التشغيل", at=4.0, bg="blue"), dict(who=0, text="كل 90 يوم", at=8.0, bg="gold")]),
   dict(k="rows", at="دابا الحساب ديال مصطفى", until="مثلا، إلى وقع مصطفى", y=260, gap=105, size=48, rows=[
     ("العتبة فالعام", "6.500 €", "الجزء الأول كيكمل"),
     ("المدخول ديال مصطفى", "2.400 €", "مصطفى عندو ألفين"),
     ("الفرق · فالشهر", "341,67 €", "نقسموها على تناش"),
     ("الكرا · فالشهر", "300 €", "الجزء التاني هو الكرا"),
     ("المجموع · فالشهر", "641,67 €", "المجموع: تقريبا", GOLD),
   ]),
   dict(k="calendar", at="مثلا، إلى وقع مصطفى", until="ومن بعد الطلب، تبع", box=R_BOX, day=15, month=12, sub="2026 · الخلصة الأولى ديال مصطفى"),
   dict(k="steps", at="مثلا، إلى وقع مصطفى", until="ومن بعد الطلب، تبع", box=L_BOX, steps=[
     ["الباد · 25/11", "1"], ["البداية · دجنبر", "2"], ["الخلصة · 15/12", "3"]], gap=2.5, check_after=0.5),
   dict(k="icons", at="ومن بعد الطلب، تبع", until="المدة: تمنطاش", box=ICB, items=[
     ["world", "الصفحة ديالك", "blue"], ["coin-euro", "المبلغ والخلصات", "green"], ["file-text", "نسخة من الطلب", "gold"]], gap=3.0),
   dict(k="big", text="18", sub="شهر متتابعين", at="المدة: تمنطاش", until="وكيفاش كيستعمل", y=430, size=300, color=GOLD),
   dict(k="text", text="11.550 €", at="يعني عند مصطفى تقريبا", until="وكيفاش كيستعمل", y=800, size=80, color=GREEN),
   dict(k="icons", at="وكيفاش كيستعمل", until="والكاش", box=ICB, items=[
     ["shopping-cart", "الماكلة", "green"], ["bolt", "الضو والما", "blue"], ["home", "تحويلة للكرا", "gold"]], gap=3.0),
   dict(k="big", text="100 €", sub="كاش فالشهر لشخص واحد", at="والكاش", until="وما كتخدمش فالقمار", y=450, size=220, color=GREEN),
   dict(k="icons", at="وما كتخدمش فالقمار", box=ICB, items=[
     ["ticket", "القمار", "red"], ["flame", "الدخان والشراب", "red"], ["shopping-cart", "أونلاين", "red"], ["world", "برا إيطاليا", "red"]], gap=1.2),
 ]),
 dict(audio="F.wav", text=T["F"], chapter="06 · الحالات الخاصة", src=S_CASI, items=[
   dict(k="chapter", num="06", title="الحالات الخاصة", at=0.1, until="الحالة الأولى"),
   dict(k="people", at="الحالة الأولى", until="الحالة التانية", box=L_BOX, people=["elder", "woman"],
        say=[dict(who=0, text="حنا فوق 67", at=1.0, bg="gold")]),
   dict(k="vs", at="الحالة الأولى", until="الحالة التانية", box=R_BOX,
        right=dict(title="العتبة", value="8.190 €", sub="فالعام", icon="wallet", color="gold"),
        left=dict(title="الكرا", value="1.950 €", sub="الحد فالعام", icon="key", color="green"), gap=6.0),
   dict(k="icons", at="الحالة التانية", until="هاد الناس كيقدرو", box=ICB, items=[
     ["users", "الحماية الاجتماعية", "blue"], ["home", "العنف فالدار", "red"], ["briefcase", "الاستغلال فالخدمة", "gold"]], gap=3.0),
   dict(k="text", text="بلا الخمسة سنين · غير طول المدة ديال البيرميسو", at="هاد الناس كيقدرو", until="الحالة التالتة", y=640, size=56, color=GOLD),
   dict(k="people", at="الحالة التالتة", until="والمدخول الجديد", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="لقيت خدمة!", at=1.0, bg="green"), dict(who=1, text="علمنا فـ 30 يوم", at=7.0, bg="gold")]),
   dict(k="big", text="3.000 €", sub="خام فالعام · ما كيتحسبوش", at="والمدخول الجديد", until="مثلا، كريم زاد", y=450, size=220, color=GREEN),
   dict(k="map", view="north", pins=["Brescia"], labels=False, at="مثلا، كريم زاد", until="ولكن إلى كان كيدخل", box=L_BOX),
   dict(k="bars", at="مثلا، كريم زاد", until="الحالة الرابعة", box=R_BOX, bars=[
     ["10 شهور", 2500, "2.500 €", "green"], ["الحد", 3000, "3.000 €", "gold"], ["12 شهر", 3600, "3.600 €", "red"]], gap=4.0),
   dict(k="text", text="غير 600 € كيتحسبو", at="ولكن إلى كان كيدخل", until="الحالة الرابعة", y=880, size=44, color=GREY),
   dict(k="vs", at="الحالة الرابعة", until="الحالة الخامسة", box=VSB,
        right=dict(title="قبل ما تبدا", value="إيه", sub="علم الإينبس", icon="receipt-tax", color="green"),
        left=dict(title="من بعد", value="لا", sub="الأدي كيطيح", icon="x", color="red"), gap=3.0),
   dict(k="icons", at="الحالة الخامسة", until="الحالة السادسة", box=ICB, items=[
     ["users", "تزاد ولد", "green"], ["luggage", "خرج من الدار", "blue"], ["heart", "تزوج", "gold"]], gap=2.0),
   dict(k="text", text="15 يوم للإعلام · شهر للدي إس أو", at="كاع التبديلات خاصك", until="الحالة السادسة", y=880, size=44, color=GOLD),
   dict(k="people", at="الحالة السادسة", until="ولكن كاينين ناس معفيين", box=FULL, people=["clerk", "worker"],
        say=[dict(who=0, text="بين 18 و59 عام", at=2.0, bg="blue")]),
   dict(k="icons", at="ولكن كاينين ناس معفيين", until="يعني حسن", box=ICB, items=[
     ["user", "فوق الستين", "gold"], ["heart", "إعاقة", "blue"], ["heart", "ولد تحت 3 سنين", "green"], ["users", "3 ولاد ولا كثر", "green"]], gap=2.5),
   dict(k="map", view="north", pins=["Bologna"], labels=False, at="يعني حسن", until="الحالة السابعة", box=L_BOX),
   dict(k="people", at="يعني حسن", until="الحالة السابعة", box=R_BOX, people=["man", "child"],
        say=[dict(who=0, text="تلاتة ديال الولاد", at=1.5, bg="green")]),
   dict(k="people", at="الحالة السابعة", until="الحالة التامنة", box=FULL, people=["student"],
        say=[dict(who=0, text="نتسجل فالقراية ديال الكبار", at=3.0, bg="gold")]),
   dict(k="people", at="الحالة التامنة", until="قولها للمعلم", box=L_BOX, people=["office"],
        say=[dict(who=0, text="نخدمك بلا مدة", at=2.0, bg="green")]),
   dict(k="big", text="8.000 €", sub="تخفيض فالعام للمعلم · 12 شهر", at="الحالة التامنة", until="والحالة التاسعة", x=1380, y=470, size=170, color=GREEN),
   dict(k="steps", at="والحالة التاسعة", until="ولكن الخلصة الأولى", box=MID, steps=[
     ["18 شهر", "1"], ["التجديد بلا توقف", "2"], ["12 شهر", "3"]], gap=3.0, check_after=0.5),
   dict(k="vs", at="ولكن الخلصة الأولى", box=VSB,
        right=dict(title="الشهر الأول", value="320 €", sub="النص · مصطفى", icon="coin-euro", color="gold"),
        left=dict(title="من بعد", value="641 €", sub="المبلغ الكامل", icon="coin-euro", color="green"), gap=4.0),
 ]),
 dict(audio="G.wav", text=T["G"], chapter="07 · الأخطاء وشنو تدير إلى ترفضات", src=S_ERR, items=[
   dict(k="chapter", num="07", title="الأخطاء والرفض", at=0.1, until="الخطأ الأول"),
   dict(k="calendar", at="الخطأ الأول", until="الخطأ التاني", box=R_BOX, day=1, month=1, sub="2027 · دي إس أو جديدة"),
   dict(k="people", at="الخطأ الأول", until="الخطأ التاني", box=L_BOX, people=["woman"],
        say=[dict(who=0, text="نسيت الإيزي!", at=1.0, bg="red")]),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Torino", "Casablanca", "plane"], pins=["Torino", "Casablanca"], labels=False,
        at="الخطأ التاني", until="الخطأ التالت", box=L_BOX),
   dict(k="people", at="الخطأ التاني", until="الخطأ التالت", box=R_BOX, people=["elder"],
        say=[dict(who=0, text="نحسب الأيام", at=4.0, bg="gold")]),
   dict(k="warn", text="ما صرحتيش بالدار فالمغرب؟ مخالفة: الحبس ورجوع الفلوس", at="الخطأ التالت", until="الخطأ الرابع", y=640),
   dict(k="calendar", at="الخطأ الرابع", until="الخطأ الخامس", box=R_BOX, day=120, month="يوم", sub="الموعد ديال الخدمات الاجتماعية"),
   dict(k="people", at="الخطأ الرابع", until="الخطأ الخامس", box=L_BOX, people=["clerk"],
        say=[dict(who=0, text="جاتك الرسالة؟", at=3.0, bg="red")]),
   dict(k="people", at="الخطأ الخامس", until="الخطأ السادس", box=FULL, people=["worker", "office"],
        say=[dict(who=1, text="خدام بلا ما تعلم؟", at=1.0, bg="red")]),
   dict(k="big", text="15", sub="يوم باش تعلم بكل تبديل", at="الخطأ السادس", until="الخطأ السابع", y=430, size=300, color=RED),
   dict(k="vs", at="الخطأ السابع", until="الخطأ التامن", box=VSB,
        right=dict(title="بلا الكارطا", value="لا", sub="ما تطلبش باسمك", icon="x", color="red"),
        left=dict(title="شي واحد فالعائلة", value="إيه", sub="عندو الكارطا", icon="users", color="green"), gap=3.0),
   dict(k="map", view="north", pins=["Bologna"], labels=False, at="الخطأ التامن", until="الخطأ التاسع", box=L_BOX),
   dict(k="vs", at="الخطأ التامن", until="الخطأ التاسع", box=R_BOX,
        right=dict(title="تسجلات", value="5/2024", sub="ألفين سم³", icon="car", color="red"),
        left=dict(title="الأدي من", value="5/2027", sub="من بعد 36 شهر", icon="calendar", color="gold"), gap=5.0),
   dict(k="icons", at="الخطأ التاسع", until="الخطأ العاشر", box=ICB, items=[
     ["world", "المغرب", "red"], ["shopping-cart", "أونلاين", "red"]], gap=1.5),
   dict(k="people", at="الخطأ العاشر", until="والخطأ الحادي عشر", box=FULL, people=["office", "man"],
        say=[dict(who=0, text="عندي ليك خدمة", at=1.0, bg="green"), dict(who=1, text="الرفض بلا سبب = خطر", at=6.0, bg="red")]),
   dict(k="warn", text="شي واحد بغا الفلوس باش يسرع الملف؟ نصاب", at="والخطأ الحادي عشر", until="دابا، شنو كيوقع", y=640),
   dict(k="icons", at="دابا، شنو كيوقع", until="وإلى ترفض الطلب ديالك", box=ICB, items=[
     ["alert-triangle", "التوقف", "gold"], ["x", "الحيد نهائيا", "red"], ["calendar", "طلب جديد من بعد 6 شهور", "blue"]], gap=3.5),
   dict(k="people", at="وإلى ترفض الطلب ديالك", until="تاني حاجة، إلى كان السبب", box=FULL, people=["hijab", "clerk"],
        say=[dict(who=0, text="علاش ترفضت؟", at=1.0, bg="red"), dict(who=1, text="شوفي السبب فالسيت", at=5.0, bg="gold")]),
   dict(k="icons", at="تاني حاجة، إلى كان السبب", until="تالت حاجة، مشي", box=ICB, items=[
     ["map-pin", "تاريخ الريزيدينسا", "blue"], ["id", "البيرميسو", "green"]], gap=2.0),
   dict(k="steps", at="تالت حاجة، مشي", until="مثلا، فاطمة دارت", box=MID, steps=[
     ["الباطرونا", "1"], ["طلب المراجعة", "2"], ["الطعن إلى كان الحق", "3"]], gap=3.0, check_after=0.5),
   dict(k="vs", at="مثلا، فاطمة دارت", box=VSB,
        right=dict(title="باسم فاطمة", value="ترفض", sub="ما عندهاش الكارطا", person="hijab", color="red"),
        left=dict(title="باسم كريم", value="تقبل", sub="طلب جديد", person="man", color="green"), gap=4.0),
 ]),
 dict(audio="H.wav", text=T["H"], chapter="08 · سؤال وجواب", src=S_QA, items=[
   dict(k="chapter", num="08", title="سؤال وجواب", at=0.1, until="السؤال الأول"),
   dict(k="people", at="السؤال الأول", until="الجواب: باسمك لا", box=FULL, people=["worker"],
        say=[dict(who=0, text="بيرميسو ديال جوج سنين", at=1.5, bg="gold")]),
   dict(k="icons", at="الجواب: باسمك لا", until="السؤال التاني", box=ICB, items=[
     ["x", "باسمك لا", "red"], ["id", "الكارطا من بعد 5 سنين", "gold"], ["users", "شي واحد عندو الكارطا", "green"]], gap=3.5),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Bologna", "Tanger", "plane"], pins=["Bologna", "Tanger"], labels=False,
        at="السؤال التاني", until="السؤال التالت", box=L_BOX),
   dict(k="people", at="السؤال التاني", until="السؤال التالت", box=R_BOX, people=["woman"],
        say=[dict(who=0, text="شهر فالصيف؟", at=1.0, bg="gold")]),
   dict(k="people", at="السؤال التالت", until="السؤال الرابع", box=L_BOX, people=["man"],
        say=[dict(who=0, text="دار الوالد فالمغرب", at=1.0, bg="gold")]),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Fes"], labels=False, at="السؤال التالت", until="السؤال الرابع", box=R_BOX),
   dict(k="people", at="السؤال الرابع", until="السؤال الخامس", box=L_BOX, people=["worker"],
        say=[dict(who=0, text="لقيت خدمة", at=1.0, bg="green")]),
   dict(k="big", text="30", sub="يوم باش تعلم الإينبس", at="السؤال الرابع", until="السؤال الخامس", x=1380, y=450, size=240, color=GOLD),
   dict(k="people", at="السؤال الخامس", until="الجواب: الخلصة الأولى", box=FULL, people=["elder"],
        say=[dict(who=0, text="إمتى كيتخلص؟", at=1.0, bg="gold")]),
   dict(k="rows", at="الجواب: الخلصة الأولى", until="السؤال السادس", y=330, gap=130, size=54, rows=[
     ("الخلصة الأولى", "15/12", "فدجنبر: خمسطاش"),
     ("الخلصة العادية", "23/12", "وتلاتة وعشرين للعادية"),
   ]),
   dict(k="people", at="السؤال السادس", until="السؤال السابع", box=L_BOX, people=["hijab"],
        say=[dict(who=0, text="الكرا بالكارطا؟", at=1.0, bg="gold")]),
   dict(k="icons", at="السؤال السادس", until="السؤال السابع", box=R_BOX, items=[
     ["home", "تحويلة وحدة", "green"], ["key", "كونطرا مسجلة", "gold"]], gap=3.0),
   dict(k="people", at="السؤال السابع", until="السؤال التامن", box=FULL, people=["student", "woman"],
        say=[dict(who=1, text="ولدي عندو 19 عام", at=1.0, bg="gold"), dict(who=0, text="القراية ديال الكبار", at=7.0, bg="green")]),
   dict(k="people", at="السؤال التامن", until="السؤال التاسع", box=L_BOX, people=["elder"],
        say=[dict(who=0, text="شهر بلا فلوس؟", at=1.0, bg="red")]),
   dict(k="vs", at="السؤال التامن", until="السؤال التاسع", box=R_BOX,
        right=dict(title="قبل", value="شهر توقف", sub="", icon="x", color="red"),
        left=dict(title="دابا", value="بلا توقف", sub="الشهر الأول النص", icon="check", color="green"), gap=3.0),
   dict(k="people", at="السؤال التاسع", until="السؤال العاشر", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="ما جاتني حتى رسالة", at=1.0, bg="red"), dict(who=1, text="اتصلي بالكومون", at=8.0, bg="green")]),
   dict(k="people", at="السؤال العاشر", until="السؤال الحادي عشر", box=FULL, people=["office", "worker"],
        say=[dict(who=1, text="خايف نخسر الأدي", at=1.0, bg="gold"), dict(who=0, text="عندي تخفيض", at=6.0, bg="green")]),
   dict(k="map", view="north", pins=["Bologna"], labels=False, at="السؤال الحادي عشر", until="السؤال التاني عشر", box=L_BOX),
   dict(k="vs", at="السؤال الحادي عشر", until="السؤال التاني عشر", box=R_BOX,
        right=dict(title="قديمة", value="إيه", sub="ماشي مشكل", icon="car", color="green"),
        left=dict(title="جديدة كبيرة", value="لا", sub="فـ 36 شهر", icon="car", color="red"), gap=6.0),
   dict(k="people", at="السؤال التاني عشر", until="وإلى عندك سؤال آخر", box=L_BOX, people=["hijab"],
        say=[dict(who=0, text="شكون يعاوني؟", at=1.0, bg="gold")]),
   dict(k="icons", at="السؤال التاني عشر", until="وإلى عندك سؤال آخر", box=R_BOX, items=[
     ["id", "الهوية", "blue"], ["file-text", "الإيزي", "green"], ["key", "كونطرا الكرا", "gold"]], gap=3.0),
   dict(k="text", text="سؤالك فالكومونتير", at="وإلى عندك سؤال آخر", y=640, size=64, color=GOLD),
 ]),
 dict(audio="I.wav", text=T["I"], chapter="09 · اللائحة النهائية", src=S_HOME, items=[
   dict(k="chapter", num="09", title="اللائحة النهائية", at=0.1, until="واحد: شوف"),
   dict(k="rows", at="واحد: شوف", until="عاود معايا الأرقام", y=180, gap=72, size=38, rows=[
     ("شوف العائلة", "1", "واحد: شوف"),
     ("شوف البيرميسو", "2", "جوج: شوف"),
     ("احسب الإقامة · 5 سنين", "3", "تلاتة: احسب"),
     ("الإيزي · دي إس أو فيناير", "4", "ربعة: دير"),
     ("صرح بكلشي", "5", "خمسة: صرح"),
     ("دير الطلب", "6", "ستة: دير"),
     ("الباد والكارطا", "7", "سبعة: وقع"),
     ("الموعد · 120 يوم", "8", "تمنية: مشي"),
     ("علم بكل تبديل", "9", "تسعة: علم"),
     ("حسب الغيابات", "10", "وعشرة: حسب"),
   ]),
   dict(k="bars", at="عاود معايا الأرقام", until="والتواريخ القريبين", box=BARB, bars=[
     ["الإيزي", 10140, "10.140 €", "gold"], ["المدخول", 6500, "6.500 €", "green"], ["الكرا فالعام", 3640, "3.640 €", "blue"]], gap=3.0),
   dict(k="rows", at="والتواريخ القريبين", until="ونرجعو للتلاتة", y=270, gap=105, size=46, rows=[
     ("خلصة عادية", "27/11", "سبعة وعشرين نونبر"),
     ("الخلصة الأولى", "15/12", "خمسطاش دجنبر"),
     ("خلصة عادية", "23/12", "تلاتة وعشرين دجنبر"),
     ("كيموت الإيزي", "31/12", "واحد وتلاتين دجنبر كيموت", RED),
     ("دي إس أو جديدة", "1/2027", "وفيناير دير", GOLD),
   ]),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="ونرجعو للتلاتة", until="فاطمة فبريشيا", box=L_BOX),
   dict(k="people", at="ونرجعو للتلاتة", until="فاطمة فبريشيا", box=R_BOX, people=["elder"],
        say=[dict(who=0, text="641 € فالشهر", at=3.0, bg="green")]),
   dict(k="map", view="north", pins=["Brescia"], labels=False, at="فاطمة فبريشيا", until="وحسن فبولونيا", box=L_BOX),
   dict(k="people", at="فاطمة فبريشيا", until="وحسن فبولونيا", box=R_BOX, people=["hijab", "man"],
        say=[dict(who=1, text="أنا نطلب", at=2.5, bg="green")]),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Bologna", "Nador", "plane"], pins=["Bologna", "Nador"], labels=False,
        at="وحسن فبولونيا", until="وإلى كنتي كتشوف", box=L_BOX),
   dict(k="people", at="وحسن فبولونيا", until="وإلى كنتي كتشوف", box=R_BOX, people=["man"],
        say=[dict(who=0, text="ما نشريش طوموبيل جديدة", at=4.0, bg="gold")]),
   dict(k="icons", at="وإلى كنتي كتشوف", until="والفصول ديال الفيديو", box=ICB, items=[
     ["users", "الباطرونا", "green"], ["file-text", "الكاف", "blue"], ["building-bank", "الخدمات الاجتماعية", "gold"]], gap=2.5),
   dict(k="text", text="الفصول والمصادر فالوصف", at="والفصول ديال الفيديو", until="ودابا، سؤال ليك", y=640, size=64, color=GOLD),
   dict(k="people", at="ودابا، سؤال ليك", until="وإلى عرفتي شي واحد", box=FULL, people=["woman", "man"],
        say=[dict(who=0, text="إيه ولا لا؟", at=3.0, bg="green")]),
   dict(k="people", at="وإلى عرفتي شي واحد", until="وإلى عجبك", box=FULL, people=["worker", "hijab"],
        say=[dict(who=1, text="صيفطو لصاحبك", at=1.0, bg="gold")]),
   dict(k="cta", at="وإلى عجبك", text="ابوني فالقناة", sub="كل نهار دليل مفيد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("الأدي من الإينبس", (236, 196, 96)), "الشروط والوراق", "والدار اللي فالمغرب"],
  num="641 €", numsub="فالشهر · مثال",
  bottom="مغاربة إيطاليا · دليل عملي بالدارجة",
)
