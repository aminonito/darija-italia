import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-27.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo1-2026-11-27-final")
BRAND = "مغاربة إيطاليا"
T = {k: v.replace("گ", "ك") for k, v in JOB["blocks"].items()}
EP_EDITS = os.path.join(ROOT, "tts/jobs/lungo1-2026-11-27-edits.json")
EDITS = json.load(open(EP_EDITS, encoding="utf-8")) if os.path.exists(EP_EDITS) else {}
for k, pairs in EDITS.items():
    for a, b in pairs:
        T[k] = T[k].replace(a, b)

S_HOME = "مغاربة إيطاليا · خبار مفيدة بالدارجة"
S_SCI = "Virgilio Notizie 25/11/2026 · Telepass Moveo 25/11/2026"
S_SCU = "Euronews 26/11/2026 · Edunews24 26/11 · DL 170/2026 · Domani · Affaritaliani"
S_FLU = "Min. Lavoro circ. 7185 · InfoImmigrazione · ItalianVisa · InformazioneFiscale · Edotto"
S_CAR = "MIMIT via Teleborsa e Quotidiano.net 26/11 · QuiFinanza 24/11 · Adnkronos 24/11 · DiarioDelWeb 26/11 · Newsauto · Automoto"
S_DIC = "InformazioneFiscale · EnacInforma · QuiFinanza · PuntoMagazine · Codice del consumo art. 17-bis · ARERA 58/2026"
S_CASE = "Calcoli nostri · Your Europe (contanti) · Hespress e H24info 22/11 (BAM) · ADII · InfoImmigrazione"
S_MAR = "Le Matin e Challenge 24/11 · Hespress · H24info 22/11 · MWN 1/11 · Le360 · La Vie Eco 17/11 · Le Matin e FNH 9/11"
S_QA = "Fonti dei capitoli 01-07"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850); FULL = (160, 300, 1760, 860)
WIDE = (260, 220, 1660, 830); ICO = (160, 330, 1760, 860); BAR = (160, 300, 1760, 840)
MED = dict(view="med", hl=["ITA", "MAR"], labels=False)
BIGMAP = (160, 200, 1760, 880)

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="00 · أخبار السيمانة", src=S_HOME, items=[
   dict(k="head", text="نشرة السيمانة", at=0.2, until="شنو كاين فهاد النشرة؟", sub="الجمعة 27 نونبر 2026"),
   dict(k="people", at=0.6, until="شنو كاين فهاد النشرة؟", box=FULL, people=["hijab", "man", "elder"],
        say=[dict(who=0, text="الطيارة ديالي فـ4 دجنبر؟", at=0.8), dict(who=1, text="خبار بالأرقام", at=5.0, bg="green")]),
   dict(k="rows", at="شنو كاين فهاد النشرة؟", until="ومن بعد، مثال عملي", y=280, gap=110, size=46, rows=[
     ("الإضراب العام", "4/12", "عندنا الإضراب العام"),
     ("المرسوم ديال المدرسة ولا قانون", "142 · 112", "عندنا المرسوم ديال"),
     ("الديكري فلوسي", "7/12", "عندنا الديكري فلوسي"),
     ("المازوط والميزانية", "2,19", "عندنا ثمن المازوط"),
     ("الفلوس ديال دجنبر", "1/12", "وعندنا الفلوس ديال"),
   ]),
   dict(k="map", **MED, route=["Torino", "Casablanca"], at="ومن بعد، مثال عملي", until="ومن المغرب، تجديد", box=BIGMAP),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Rabat"], labels=False, at="ومن المغرب، تجديد", until="قبل ما نبداو، جوج", box=BIGMAP),
   dict(k="icons", at="قبل ما نبداو، جوج", until="يالاه نبداو.", box=ICO, items=[
     ["file-certificate", "جوج مصادر", "green"], ["alert-triangle", "ماشي استشارة", "gold"], ["users", "سول الباترونا", "blue"]], gap=2.5),
   dict(k="chapter", num="01", title="الإضراب العام 4 دجنبر", at="الخبر الأول: الإضراب", until="مجموعة ديال النقابات"),
   dict(k="map", view="italy", pins=["Milano", "Roma", "Napoli"], labels=False, at="مجموعة ديال النقابات", until="أولا، التران.", box=BIGMAP),
   dict(k="icons", at="أولا، التران.", until="ثانيا، الطيارات.", box=L_BOX, items=[
     ["train", "التران", "blue"], ["clock", "24 ساعة", "gold"]], gap=2.0),
   dict(k="steps", at="أولا، التران.", until="ثانيا، الطيارات.", box=R_BOX, steps=[
     ["الخميس 3 دجنبر", "21:00"], ["الجمعة 4 دجنبر", "21:00"]], gap=4.0, check_after=99),
   dict(k="vs", at="ثانيا، الطيارات.", until="ثالثا، الأوطوروت.", box=WIDE,
        right=dict(title="الصباح", value="7 - 10", sub="وقت محمي", icon="plane", color="green"),
        left=dict(title="العشية", value="18 - 21", sub="وقت محمي", icon="plane", color="green"), gap=6.0),
   dict(k="steps", at="ثالثا، الأوطوروت.", until="رابعا، الطوبيس", box=WIDE, steps=[
     ["الخميس 3 دجنبر", "22:00"], ["الجمعة 4 دجنبر", "22:00"]], gap=3.0, check_after=99),
   dict(k="icons", at="رابعا، الطوبيس", until="مثال: خديجة", box=ICO, items=[
     ["bus", "الطوبيس", "blue"], ["train", "الميترو", "gold"], ["school", "المدرسة", "green"]], gap=2.5),
   dict(k="map", **MED, route=["Bologna", "Casablanca"], at="مثال: خديجة", until="الطناش ماشي فالأوقات", box=BIGMAP),
   dict(k="people", at="الطناش ماشي فالأوقات", until="وإلى كانت الطيارة مع السبعة", box=FULL, people=["hijab", "clerk"],
        say=[dict(who=0, text="الطيارة مع الطناش", at=0.6), dict(who=1, text="شوفي الإيميل", at=5.0, bg="gold")]),
   dict(k="big", text="7:30", sub="داخلة فالوقت المحمي", at="وإلى كانت الطيارة مع السبعة", until="ومهم تعرف:"),
   dict(k="people", at="ومهم تعرف:", until="وإلى كنتي غادي تسافر بالأوطوروت", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="خاصني نضرب؟", at=0.6), dict(who=1, text="لا، ماشي واجب", at=4.0, bg="green")]),
   dict(k="map", view="north", pins=["Torino", "Genova"], labels=False, at="وإلى كنتي غادي تسافر بالأوطوروت", box=BIGMAP),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="02 · المدرسة: ولا قانون", src=S_SCU, items=[
   dict(k="chapter", num="02", title="المدرسة: المرسوم ولا قانون", at=0.2, until="نهار الخميس ستة وعشرين"),
   dict(k="bars", at="نهار الخميس ستة وعشرين", until="ومجلس الشيوخ كان", box=BAR, bars=[
     ["مع", 142, "142", "green"], ["ضد", 112, "112", "red"], ["ما صوتوش", 4, "4", "gold"]]),
   dict(k="text", text="مجلس النواب · التصويت الأخير · 26/11", at="نهار الخميس ستة وعشرين", until="ومجلس الشيوخ كان", y=880, size=42),
   dict(k="steps", at="ومجلس الشيوخ كان", until="شنو فيه؟ نعاودو", box=WIDE, steps=[
     ["مجلس الشيوخ", "80 · 46"], ["مجلس النواب", "142 · 112"], ["الجريدة الرسمية", "GU"]], gap=4.0, check_after=99),
   dict(k="people", at="شنو فيه؟ نعاودو", until="أولا، السقف", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="شنو تبدل لولادنا؟", at=0.6), dict(who=1, text="غادي نعاودو", at=3.0, bg="green")]),
   dict(k="icons", at="أولا، السقف", until="وماشي هاد العام", box=ICO, items=[
     ["school", "الأول ابتدائي", "blue"], ["school", "الأول إعدادي", "gold"], ["school", "الأول ثانوي", "green"]], gap=2.0),
   dict(k="calendar", at="وماشي هاد العام", until="ثانيا، شكون كيتحسب؟", box=R_BOX, day="2027", month="2028", sub="العام الدراسي"),
   dict(k="vs", at="ثانيا، شكون كيتحسب؟", until="ثالثا، إلى كانو", box=WIDE,
        right=dict(title="تزاد هنا ولا الماطيرنا", value="لا", sub="عادة ما كيتحسبش", person="child", color="green"),
        left=dict(title="3 سنين ونجح", value="لا", sub="الإعدادي والثانوي", person="girl", color="green"), gap=6.0),
   dict(k="map", view="north", pins=["Milano"], labels=False, at="ثالثا، إلى كانو", until="رابعا، الواليدين", box=R_BOX),
   dict(k="icons", at="ثالثا، إلى كانو", until="رابعا، الواليدين", box=L_BOX, items=[
     ["map-pin", "البعد على الدار", "blue"], ["heart", "ظروف العائلة", "gold"]], gap=6.0),
   dict(k="people", at="رابعا، الواليدين", until="والذعيرة من ميتين حتى لألف أورو، غير", box=FULL, people=["man", "office"],
        say=[dict(who=0, text="ما كنعرفش الطاليانية مزيان", at=0.8), dict(who=1, text="دروس بالمجان", at=6.0, bg="green")]),
   dict(k="big", text="200 - 1.000", sub="أورو: الذعيرة غير من بعد إنذار", at="والذعيرة من ميتين حتى لألف أورو، غير", until="خامسا، الوجه"),
   dict(k="warn", text="الوجه المغطي ممنوع فالأنشطة ديال المدرسة", at="خامسا، الوجه", until="سادسا، المساعدة", y=600),
   dict(k="bars", at="سادسا، المساعدة", until="شنو كيعني هادشي", box=BAR, bars=[
     ["قبل", 30000, "30.000 €", "gold"], ["دابا", 40000, "40.000 €", "green"]]),
   dict(k="text", text="العتبة ديال الإيزي: المساعدة ديال الكتب", at="سادسا، المساعدة", until="شنو كيعني هادشي", y=880, size=42),
   dict(k="warn", text="ماشي منع ديال التسجيل", at="شنو كيعني هادشي", until="وشكون اللي غادي يقرر", y=600),
   dict(k="people", at="وشكون اللي غادي يقرر", until="والنصيحة العملية", box=FULL, people=["hijab", "clerk"],
        say=[dict(who=0, text="شكون كيقرر؟", at=0.6), dict(who=1, text="مكتب التعليم والمدراء", at=4.0, bg="green")]),
   dict(k="icons", at="والنصيحة العملية", until="وإلى عندك ولد غادي يجي", box=ICO, items=[
     ["certificate", "الماطيرنا", "blue"], ["report-money", "النتائج", "gold"], ["file-text", "الشهادات", "green"]], gap=3.0),
   dict(k="map", **MED, route=["Casablanca", "Milano"], at="وإلى عندك ولد غادي يجي", until="وكيف ديما", box=BIGMAP),
   dict(k="big", text="2027", sub="فكر فالمدرسة من دابا", at="وكيف ديما"),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="03 · الديكري فلوسي: 10 أيام", src=S_FLU, items=[
   dict(k="chapter", num="03", title="الديكري فلوسي: بقات 10 أيام", at=0.2, until="إلى عندك شي واحد"),
   dict(k="map", **MED, route=["Beni Mellal", "Bergamo"], at="إلى عندك شي واحد", until="اليوم سبعة وعشرين", box=BIGMAP),
   dict(k="calendar", at="اليوم سبعة وعشرين", until="شنو هي التعبئة", box=R_BOX, day=7, month=12, sub="مع 20:00"),
   dict(k="big", text="10", sub="أيام باقية", at="حسبناها: عشرة", until="شنو هي التعبئة", box=L_BOX),
   dict(k="steps", at="شنو هي التعبئة", until="ومن تسعة حتى تلطاش", box=WIDE, steps=[
     ["التعبئة المسبقة", "7/12"], ["الكليك داي", "9:00"]], gap=5.0, check_after=99),
   dict(k="vs", at="ومن تسعة حتى تلطاش", until="شكون اللي كيدير الطلب؟", box=WIDE,
        right=dict(title="9 - 13 دجنبر", value="تكميل", sub="الطلبات القدام", icon="clipboard-check", color="green"),
        left=dict(title="طلب جديد", value="لا", sub="ما كاينش", icon="x", color="red"), gap=5.0),
   dict(k="people", at="شكون اللي كيدير الطلب؟", until="والمشغل خاصو السبيد", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="نقدر نطلب بوحدي؟", at=0.6), dict(who=1, text="لا، المشغل", at=3.5, bg="gold")]),
   dict(k="icons", at="والمشغل خاصو السبيد", until="وشحال ديال البلايص؟", box=ICO, items=[
     ["id", "السبيد", "blue"], ["credit-card", "الكارطا الإلكترونية", "gold"], ["mail", "البيك", "green"]], gap=2.5),
   dict(k="big", text="165.850", sub="بلاصة فالديكري الجديد", at="وشحال ديال البلايص؟", until="منهم ستة وسبعين"),
   dict(k="bars", at="منهم ستة وسبعين", until="والكليك داي، ديما", box=BAR, bars=[
     ["موسمية", 89000, "89.000", "gold"], ["ماشي موسمية", 76200, "76.200", "blue"], ["فالديور", 14000, "14.000", "green"], ["حرة", 650, "650", "red"]]),
   dict(k="steps", at="والكليك داي، ديما", until="مثال: يوسف", box=WIDE, steps=[
     ["الفلاحة", "12/1"], ["السياحة", "9/2"], ["ماشي موسمية", "16/2"], ["فالديور", "18/2"]], gap=3.5, check_after=99),
   dict(k="map", view="north", pins=["Bergamo"], labels=False, at="مثال: يوسف", until="يوسف خاصو يعمر", box=R_BOX),
   dict(k="people", at="مثال: يوسف", until="يوسف خاصو يعمر", box=L_BOX, people=["worker"],
        say=[dict(who=0, text="باغي نجيب حمزة", at=1.5)]),
   dict(k="steps", at="يوسف خاصو يعمر", until="ونصيحة للمشغل", box=WIDE, steps=[
     ["التعبئة", "7/12"], ["الكونطرا والسكن", "CCNL"], ["الكليك داي", "16/2"]], gap=4.0, check_after=99),
   dict(k="people", at="ونصيحة للمشغل", until="وشنو كيوقع من بعد؟", box=FULL, people=["office", "clerk"],
        say=[dict(who=0, text="شوف البيك كل نهار", at=0.6, bg="gold")]),
   dict(k="steps", at="وشنو كيوقع من بعد؟", until="ولكن ردو البال: بالنسبة", box=WIDE, steps=[
     ["النولا أوسطا", "1"], ["الفيزا فالقنصلية", "2"], ["الكونطرا والبيرميسو", "3"]], gap=4.0, check_after=99),
   dict(k="map", **MED, route=["Casablanca", "Bergamo"], at="ولكن ردو البال: بالنسبة", until="تحذير كبير", box=BIGMAP),
   dict(k="people", at="تحذير كبير", until="وإلى بغيتي الشرح", box=FULL, people=["man", "worker"],
        say=[dict(who=0, text="عطيني الفلوس ونجيب ليك الكونطرا", at=0.6), dict(who=1, text="نصاب!", at=5.0, bg="red")]),
   dict(k="warn", text="الطلب ما كيتشراش", at="الطلب كيديرو المشغل الحقيقي", until="وإلى بغيتي الشرح", y=640),
   dict(k="cta", at="وإلى بغيتي الشرح", text="الشرح الكامل فالقناة", sub="الديكري فلوسي خطوة بخطوة"),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="04 · المازوط والمشاريع", src=S_CAR, items=[
   dict(k="chapter", num="04", title="المازوط والميزانية والمشاريع", at=0.2, until="نبداو بالمازوط."),
   dict(k="calendar", at="نبداو بالمازوط.", until="ولكن الثمن ما طلعش", box=R_BOX, day=23, month=11, sub="سالا الخصم"),
   dict(k="icons", at="نبداو بالمازوط.", until="ولكن الثمن ما طلعش", box=L_BOX, items=[
     ["gas-station", "المازوط", "gold"], ["x", "بلا خصم", "red"]], gap=3.0),
   dict(k="vs", at="ولكن الثمن ما طلعش", until="حسبناها: خمسين لتر", box=WIDE,
        right=dict(title="البنزين", value="1,930", sub="أورو فاللتر · 26/11", icon="gas-station", color="green"),
        left=dict(title="المازوط", value="2,192", sub="أورو فاللتر · 26/11", icon="gas-station", color="gold"), gap=4.0),
   dict(k="bars", at="حسبناها: خمسين لتر", until="وتذكر: الخصم كان", box=BAR, bars=[
     ["المازوط", 109.6, "109,60 €", "gold"], ["البنزين", 96.5, "96,50 €", "green"]]),
   dict(k="text", text="50 لتر · الثمن المتوسط فالسيلف", at="حسبناها: خمسين لتر", until="وتذكر: الخصم كان", y=880, size=42),
   dict(k="people", at="وتذكر: الخصم كان", until="كيجيو تقريبا تمن مية", box=FULL, people=["worker", "man"],
        say=[dict(who=0, text="كنخدم بالطوموبيل", at=0.6), dict(who=1, text="احسب الشهر", at=6.0, bg="gold")]),
   dict(k="big", text="877", sub="أورو فالشهر ديال المازوط", at="كيجيو تقريبا تمن مية", until="دابا الميزانية"),
   dict(k="map", view="italy", hl=["Lazio"], pins=["Roma"], labels=False, at="دابا الميزانية", until="النواب دخلو", box=BIGMAP),
   dict(k="bars", at="النواب دخلو", until="اللجنة خاصها تسالي", box=BAR, bars=[
     ["دخلو", 6558, "6.558", "blue"], ["ترفضو", 1700, "1.700", "red"], ["مهمين", 700, "700", "gold"]]),
   dict(k="text", text="التعديلات ديال الميزانية 2027", at="النواب دخلو", until="اللجنة خاصها تسالي", y=880, size=42),
   dict(k="steps", at="اللجنة خاصها تسالي", until="مهم بزاف: حتى", box=WIDE, steps=[
     ["اللجنة", "16/12"], ["القاعة", "18/12"], ["مجلس الشيوخ", "31/12"]], gap=4.0, check_after=99),
   dict(k="people", at="مهم بزاف: حتى", until="ثانيا، الكود الجديد", box=FULL, people=["hijab", "clerk"],
        say=[dict(who=0, text="بونوس جديد من يناير؟", at=0.6), dict(who=1, text="باقي مشروع", at=5.0, bg="gold")]),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="ثانيا، الكود الجديد", until="ملي توصلو الوراق", box=R_BOX),
   dict(k="icons", at="ثانيا، الكود الجديد", until="ملي توصلو الوراق", box=L_BOX, items=[
     ["file-text", "الوراق", "blue"], ["car", "السرعة", "gold"]], gap=4.0),
   dict(k="steps", at="ملي توصلو الوراق", until="يعني باقي مشروع، والقواعد", box=WIDE, steps=[
     ["مجلس الدولة", "20"], ["البرلمان", "12/1"], ["الحكومة", "13/3"]], gap=4.0, check_after=99),
   dict(k="warn", text="الذعائر ديال اليوم هي اللي خدامة", at="يعني باقي مشروع، والقواعد", until="ثالثا، الجنسية", y=600),
   dict(k="vs", at="ثالثا، الجنسية", until="وعلاش كنعاودو", box=WIDE,
        right=dict(title="اليوم", value="معفي", sub="عندك الكارطا", icon="id", color="green"),
        left=dict(title="المشروع", value="B1", sub="باقي ما تصادقش", icon="file-text", color="gold"), gap=5.0),
   dict(k="people", at="وعلاش كنعاودو", box=FULL, people=["elder", "girl"],
        say=[dict(who=0, text="شفتها فالفيسبوك!", at=0.6), dict(who=1, text="المشروع ماشي قانون", at=5.0, bg="green")]),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="05 · الفلوس ديال دجنبر", src=S_DIC, items=[
   dict(k="chapter", num="05", title="الفلوس والآجال نهار بنهار", at=0.2, until="اليوم الجمعة سبعة وعشرين نونبر"),
   dict(k="calendar", at="اليوم الجمعة سبعة وعشرين نونبر", until="واليوم حتى هو البلاك", box=R_BOX, day=27, month=11, sub="الأدي"),
   dict(k="people", at="اليوم الجمعة سبعة وعشرين نونبر", until="واليوم حتى هو البلاك", box=L_BOX, people=["elder"],
        say=[dict(who=0, text="الإيزي تحت 10.140", at=2.0, bg="green")]),
   dict(k="vs", at="واليوم حتى هو البلاك", until="الاثنين تلاتين نونبر: آخر", box=WIDE,
        right=dict(title="أونلاين", value="14", sub="يوم باش ترجعها", icon="shopping-cart", color="green"),
        left=dict(title="فالمحل", value="لا", sub="غير إلى قبل مول المحل", icon="building-store", color="red"), gap=7.0),
   dict(k="people", at="الاثنين تلاتين نونبر: آخر", until="الثلاثاء واحد دجنبر", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="البارتيتا إيفا؟", at=0.6), dict(who=1, text="قبل 30 نونبر", at=3.0, bg="gold")]),
   dict(k="calendar", at="الثلاثاء واحد دجنبر", until="والناس اللي البانسيون", box=R_BOX, day=1, month=12, sub="البانسيون والتريديشيما"),
   dict(k="big", text="154,94", sub="أورو: الزيادة الماكسيموم", at="والناس اللي البانسيون", until="ونفس النهار، اللي"),
   dict(k="icons", at="ونفس النهار، اللي", until="تلاتة وربعة دجنبر: الإضراب", box=ICO, items=[
     ["bolt", "الضو فنهار", "gold"]], gap=1.0),
   dict(k="steps", at="تلاتة وربعة دجنبر: الإضراب", until="ستطاش دجنبر: آخر أجل", box=WIDE, steps=[
     ["الإضراب", "3-4/12"], ["الديكري فلوسي", "7/12"], ["الأدي الجديد", "15/12"]], gap=3.0, check_after=99),
   dict(k="steps", at="ستطاش دجنبر: آخر أجل", until="واحد وتلاتين دجنبر: الإيزي", box=WIDE, steps=[
     ["الإيمو · الكارطا", "16/12"], ["الأسينيو أونيكو", "17/12"], ["الأدي", "23/12"]], gap=4.0, check_after=99),
   dict(k="calendar", at="واحد وتلاتين دجنبر: الإيزي", until="وتذكر: فالطلب", box=R_BOX, day=31, month=12, sub="الإيزي · الماماوات · الكريش"),
   dict(k="bars", at="وهو آخر أجل لطلب", until="وتذكر: فالطلب", box=L_BOX, bars=[
     ["الشهر", 60, "60 €", "gold"], ["العام", 720, "720 €", "green"]]),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Fes"], labels=False, at="وتذكر: فالطلب", until="مثال صغير: فاطمة", box=BIGMAP),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="مثال صغير: فاطمة", until="إلى كانت عندها الشروط", box=R_BOX),
   dict(k="people", at="مثال صغير: فاطمة", until="إلى كانت عندها الشروط", box=L_BOX, people=["hijab", "child"],
        say=[dict(who=0, text="جوج ولاد وكنخدم", at=1.0)]),
   dict(k="big", text="720", sub="أورو: البونوس ديال الماماوات", at="إلى كانت عندها الشروط", until="إذن جوج حوايج"),
   dict(k="icons", at="إذن جوج حوايج", until="ونصيحة: دير ورقة", box=ICO, items=[
     ["file-text", "الماماوات قبل 31/12", "gold"], ["calculator", "الإيزي فيناير", "green"]], gap=4.0),
   dict(k="icons", at="ونصيحة: دير ورقة", until="وإلى ما عرفتيش", box=ICO, items=[
     ["calendar", "الأجندة", "blue"], ["phone", "التيليفون", "green"]], gap=2.0),
   dict(k="people", at="وإلى ما عرفتيش", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="عندي الحق؟", at=0.6), dict(who=1, text="سولي الباترونا من دابا", at=3.0, bg="green")]),
 ]),
 dict(audio="F.wav", text=T["F"], chapter="06 · مثال: السفر للمغرب", src=S_CASE, items=[
   dict(k="chapter", num="06", title="مثال: عائلة غادية للمغرب", at=0.2, until="باغيين يمشيو للمغرب"),
   dict(k="map", **MED, route=["Torino", "Casablanca"], at="باغيين يمشيو للمغرب", until="شنو خاصهم يعرفو؟", box=BIGMAP),
   dict(k="people", at="شنو خاصهم يعرفو؟", until="الحاجة الأولى", box=FULL, people=["man", "woman", "child"],
        say=[dict(who=0, text="شنو خاصنا نعرفو؟", at=0.6)]),
   dict(k="calendar", at="الحاجة الأولى", until="إذن عندو جوج ديال الحلول", box=R_BOX, day=4, month=12, sub="الإضراب"),
   dict(k="map", view="north", pins=["Milano", "Torino"], labels=False, at="وأمو جاية من ميلانو", until="إذن عندو جوج ديال الحلول", box=L_BOX),
   dict(k="vs", at="إذن عندو جوج ديال الحلول", until="الحاجة الثانية", box=WIDE,
        right=dict(title="الوقت المحمي", value="7-10 · 18-21", sub="طيارة فهاد الساعات", icon="plane", color="green"),
        left=dict(title="نهار آخر", value="بدل", sub="بعيد على الإضراب", icon="calendar", color="blue"), gap=5.0),
   dict(k="steps", at="الحاجة الثانية", until="ومن بعد، تسافر بالباسبور", box=WIDE, steps=[
     ["البيرميسو كيسالي", "10/3/2027"], ["ناقص 90 يوم", "10/12/2026"]], gap=6.0, check_after=99),
   dict(k="icons", at="ومن بعد، تسافر بالباسبور", until="ولكن ردو البال: مع", box=ICO, items=[
     ["e-passport", "الباسبور", "blue"], ["id", "البيرميسو القديم", "gold"], ["receipt", "الريسيفوطا", "green"]], gap=2.0),
   dict(k="map", **MED, route=["Torino", "Casablanca"], at="ولكن ردو البال: مع", until="الحاجة الثالثة", box=R_BOX),
   dict(k="people", at="ولكن ردو البال: مع", until="الحاجة الثالثة", box=L_BOX, people=["woman"],
        say=[dict(who=0, text="مباشرة، بلا ستوب", at=1.5, bg="gold")]),
   dict(k="bars", at="الحاجة الثالثة", until="القاعدة ديال الاتحاد", box=BAR, bars=[
     ["كريم", 8000, "8.000 €", "blue"], ["نادية", 3000, "3.000 €", "gold"], ["المجموع", 11000, "11.000 €", "red"]]),
   dict(k="big", text="10.000", sub="أورو ولا كثر: صرح فالديوانة", at="القاعدة ديال الاتحاد", until="وكتحسب حتى العملة"),
   dict(k="icons", at="وكتحسب حتى العملة", until="إذن خاصهم يعمرو", box=ICO, items=[
     ["cash", "العملة", "green"], ["receipt", "الشيكات", "blue"], ["coin-euro", "الذهب", "gold"]], gap=2.0),
   dict(k="people", at="إذن خاصهم يعمرو", until="الحاجة الرابعة", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="عندي 11.000", at=0.6), dict(who=1, text="عمر التصريح", at=3.5, bg="green")]),
   dict(k="big", text="65", sub="درهم زايدين على كل 1.000 أورو", at="الحاجة الرابعة", until="الحاجة الخامسة"),
   dict(k="map", **MED, route=["Genova", "Tanger", "ship"], at="الحاجة الخامسة", until="فالمغرب عندهم مية وتمانين", box=BIGMAP),
   dict(k="big", text="180", sub="يوم فالعام بالماتريكولا الإيطالية", at="فالمغرب عندهم مية وتمانين", until="وشي ملاحظة"),
   dict(k="warn", text="كارطا الأدي ما كتخدمش برا إيطاليا", at="وشي ملاحظة", until="إذن العائلة ديال كريم", y=600),
   dict(k="steps", at="إذن العائلة ديال كريم", until="والأخطاء اللي بزاف", box=WIDE, steps=[
     ["النهار والساعة", "1"], ["التجديد قبل 10/12", "2"], ["التصريح بالفلوس", "3"], ["الصرف", "4"], ["الباسبورات", "5"]], gap=3.0, check_after=99),
   dict(k="people", at="والأخطاء اللي بزاف", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="ستوب فإسبانيا؟", at=0.6), dict(who=1, text="لا مع الريسيفوطا", at=3.0, bg="red")]),
 ]),
 dict(audio="G.wav", text=T["G"], chapter="07 · من المغرب", src=S_MAR, items=[
   dict(k="chapter", num="07", title="من المغرب", at=0.2, until="الخبر الأول: إي رخصتي"),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Rabat"], labels=False, at="الخبر الأول: إي رخصتي", until="شنو كتدير؟", box=BIGMAP),
   dict(k="icons", at="شنو كتدير؟", until="كيفاش؟ كتدخل", box=ICO, items=[
     ["license", "التجديد", "blue"], ["file-text", "النسخة", "gold"], ["report-money", "المعلومات", "green"]], gap=2.5),
   dict(k="steps", at="كيفاش؟ كتدخل", until="شنو ما زال", box=WIDE, steps=[
     ["الهوية الرقمية", "1"], ["الطبيب · التصويرة · التوقيع", "2"], ["الخلاص أونلاين", "3"]], gap=3.0, check_after=99),
   dict(k="people", at="شنو ما زال", until="وتذكر حاجة مهمة", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="نقدر من ميلانو؟", at=0.6), dict(who=1, text="باقي ما واضحش", at=4.0, bg="gold")]),
   dict(k="vs", at="وتذكر حاجة مهمة", until="الخبر الثاني: الدرهم", box=WIDE,
        right=dict(title="البيرمي المغربي", value="1", sub="عام من الريزيدينسا", icon="license", color="gold"),
        left=dict(title="التبديل", value="6", sub="سنين: أقل من", icon="car", color="green"), gap=7.0),
   dict(k="map", **MED, route=["Milano", "Casablanca"], at="الخبر الثاني: الدرهم", until="والاحتياطي ديال", box=BIGMAP),
   dict(k="big", text="512", sub="مليار درهم: الاحتياطي", at="والاحتياطي ديال", until="وشحال من واحد كيقول"),
   dict(k="people", at="وشحال من واحد كيقول", until="الخبر الثالث", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="نصرف هنا ولا تما؟", at=0.6), dict(who=1, text="قارن الثمن النهائي", at=3.5, bg="green")]),
   dict(k="big", text="103", sub="مليار درهم حتى لآخر شتنبر", at="الخبر الثالث", until="والأرقام ديال آخر أكتوبر"),
   dict(k="calendar", at="والأرقام ديال آخر أكتوبر", until="الخبر الرابع", box=R_BOX, day=30, month=11, sub="الأرقام الجديدة؟"),
   dict(k="people", at="والأرقام ديال آخر أكتوبر", until="الخبر الرابع", box=L_BOX, people=["elder"],
        say=[dict(who=0, text="فلوس الجالية", at=2.0, bg="green")]),
   dict(k="steps", at="الخبر الرابع", until="فيها حاجة للمقاول", box=WIDE, steps=[
     ["مجلس النواب", "14/11"], ["مجلس المستشارين", "17/11"], ["القراءة الثانية", "?"]], gap=4.0, check_after=99),
   dict(k="bars", at="فيها حاجة للمقاول", until="وحتى لدابا، ما لقينا", box=BAR, bars=[
     ["قبل", 80000, "80.000 DH", "gold"], ["المشروع", 100000, "100.000 DH", "green"]]),
   dict(k="text", text="المقاول الذاتي: النسبة كتنقص", at="فيها حاجة للمقاول", until="وحتى لدابا، ما لقينا", y=880, size=42),
   dict(k="warn", text="باقي مشروع، ماشي قانون نهائي", at="وحتى لدابا، ما لقينا", until="الخبر الخامس", y=600),
   dict(k="map", **MED, route=["Casablanca", "Roma"], at="الخبر الخامس", until="وهادي مهمة للجنسية", box=BIGMAP),
   dict(k="big", text="6", sub="شهور: العمر ديال الورقة للبريفيتورا", at="وهادي مهمة للجنسية", until="وتذكير للعطلة"),
   dict(k="icons", at="وتذكير للعطلة", box=ICO, items=[
     ["e-passport", "الباسبور", "gold"], ["id", "البطاقة الوطنية", "green"], ["calendar", "الموعد من دابا", "blue"]], gap=1.5),
 ]),
 dict(audio="H.wav", text=T["H"], chapter="08 · سؤال وجواب", src=S_QA, items=[
   dict(k="chapter", num="08", title="سؤال وجواب", at=0.2, until="السؤال الأول"),
   dict(k="people", at="السؤال الأول", until="السؤال الثاني", box=FULL, people=["hijab", "clerk"],
        say=[dict(who=0, text="طيارة مع التمنية الصباح", at=0.8), dict(who=1, text="وقت محمي", at=6.0, bg="green")]),
   dict(k="people", at="السؤال الثاني", until="السؤال الثالث", box=FULL, people=["man", "office"],
        say=[dict(who=0, text="ولدي قرا هنا من الأول", at=0.8), dict(who=1, text="ما كيتحسبش", at=7.0, bg="green")]),
   dict(k="map", **MED, route=["Fes", "Bologna"], at="السؤال الثالث", until="السؤال الرابع", box=R_BOX),
   dict(k="people", at="السؤال الثالث", until="السؤال الرابع", box=L_BOX, people=["worker"],
        say=[dict(who=0, text="المشغل هو اللي كيطلب", at=3.0, bg="gold")]),
   dict(k="people", at="السؤال الرابع", until="السؤال الخامس", box=FULL, people=["girl", "clerk"],
        say=[dict(who=0, text="بونوس جديد من يناير؟", at=0.8), dict(who=1, text="باقي مشروع", at=5.0, bg="gold")]),
   dict(k="steps", at="السؤال الخامس", until="السؤال السادس", box=WIDE, steps=[
     ["البيرميسو كيسالي", "1/2/2027"], ["ناقص 90 يوم", "3/11/2026"], ["دير الطلب دابا", "!"]], gap=4.0, bad=True, check_after=99),
   dict(k="people", at="السؤال السادس", until="السؤال السابع", box=FULL, people=["woman", "office"],
        say=[dict(who=0, text="نرجع التيليفون للمحل؟", at=0.8), dict(who=1, text="غير إلى قبل", at=6.0, bg="gold")]),
   dict(k="people", at="السؤال السابع", until="السؤال الثامن", box=FULL, people=["elder", "clerk"],
        say=[dict(who=0, text="خاصني نطلب الزيادة؟", at=0.8), dict(who=1, text="لا، بوحدها", at=4.0, bg="green")]),
   dict(k="vs", at="السؤال الثامن", until="السؤال التاسع", box=WIDE,
        right=dict(title="تحت", value="9.000", sub="ما كاينش التصريح الأوروبي", icon="cash", color="green"),
        left=dict(title="من", value="10.000", sub="صرح فالديوانة", icon="alert-triangle", color="red"), gap=4.0),
   dict(k="people", at="السؤال التاسع", until="السؤال العاشر", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="نجدد البيرمي من ميلانو؟", at=0.8), dict(who=1, text="سول القنصلية", at=5.0, bg="gold")]),
   dict(k="calendar", at="السؤال العاشر", until="السؤال الحادي عشر", box=R_BOX, day=16, month=12, sub="أول خلصة بالكارطا"),
   dict(k="people", at="السؤال العاشر", until="السؤال الحادي عشر", box=L_BOX, people=["hijab"],
        say=[dict(who=0, text="ما خلصت والو", at=1.0)]),
   dict(k="people", at="السؤال الحادي عشر", until="السؤال الثاني عشر", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="الأكونطو بوحدي؟", at=0.8), dict(who=1, text="غير البارتيتا إيفا", at=5.0, bg="gold")]),
   dict(k="people", at="السؤال الثاني عشر", until="السؤال الثالث عشر", box=FULL, people=["woman", "child"],
        say=[dict(who=0, text="ولدي جاي فالصيف", at=0.8), dict(who=1, text="المدرسة والطاليانية", at=5.0, bg="green")]),
   dict(k="map", **MED, route=["Genova", "Tanger", "ship"], at="السؤال الثالث عشر", until="وإلى عندك سؤال آخر", box=BIGMAP),
   dict(k="people", at="وإلى عندك سؤال آخر", box=FULL, people=["girl", "elder", "hijab"],
        say=[dict(who=0, text="كتب سؤالك فالكومونتير", at=0.8, bg="green")]),
 ]),
 dict(audio="I.wav", text=T["I"], chapter="09 · الخلاصة والتواريخ", src=S_HOME, items=[
   dict(k="head", text="الخلاصة", at=0.2, until="واحد: الإضراب"),
   dict(k="rows", at="واحد: الإضراب", until="ودابا التواريخ ديال الأيام", y=300, gap=118, size=46, rows=[
     ("الإضراب العام", "3-4/12", "واحد: الإضراب"),
     ("المدرسة: ولا قانون", "2027", "جوج: المرسوم"),
     ("الديكري فلوسي", "7/12", "تلاتة: الديكري"),
     ("المازوط بلا خصم · مشاريع", "23/11", "ربعة: المازوط"),
     ("المغرب: إي رخصتي", "online", "خمسة: من المغرب"),
   ]),
   dict(k="steps", at="ودابا التواريخ ديال الأيام", until="الثلاثاء واحد دجنبر: البانسيون والتريديشيما", box=WIDE, steps=[
     ["الأدي · البلاك فرايداي", "27/11"], ["الأكونطو · السايبر مانداي", "30/11"]], gap=4.0, check_after=99),
   dict(k="steps", at="الثلاثاء واحد دجنبر: البانسيون والتريديشيما", until="خمسطاش دجنبر: الأدي للطلبات", box=WIDE, steps=[
     ["البانسيون", "1/12"], ["الإضراب", "3-4/12"], ["الديكري فلوسي", "7/12"], ["البيرميسو", "10/12"]], gap=3.0, check_after=99),
   dict(k="steps", at="خمسطاش دجنبر: الأدي للطلبات", until="وحاجة عملية: دير ورقة", box=WIDE, steps=[
     ["الأدي", "15/12"], ["الإيمو · الكارطا", "16/12"], ["الأسينيو أونيكو", "17/12"], ["الإيزي · الماماوات", "31/12"]], gap=3.0, check_after=99),
   dict(k="icons", at="وحاجة عملية: دير ورقة", until="وخصوصا الواليدين", box=ICO, items=[
     ["calendar", "الأجندة", "blue"], ["phone", "الواتساب", "green"]], gap=2.0),
   dict(k="people", at="وخصوصا الواليدين", until="وإلى فاتك شي فيديو", box=FULL, people=["elder", "girl"],
        say=[dict(who=1, text="نعاونك فالإيزي", at=1.0, bg="green")]),
   dict(k="icons", at="وإلى فاتك شي فيديو", until="وكل نهار كاين", box=ICO, items=[
     ["license", "تبديل البيرمي", "blue"], ["id", "البيرميسو", "gold"], ["heart", "الجنسية", "green"], ["plane", "الفيزا", "blue"]], cols=4, gap=2.0),
   dict(k="steps", at="وكل نهار كاين", until="ونعاودو نقولو", box=WIDE, steps=[
     ["فيديو قصير", "13:00"], ["النشرة الطويلة", "16:30"], ["فيديو قصير", "19:00"], ["الشرح الكامل", "20:30"]], gap=2.0, check_after=99),
   dict(k="people", at="ونعاودو نقولو", until="وحاجة أخيرة", box=FULL, people=["clerk", "woman"],
        say=[dict(who=0, text="سول الباترونا ولا الكاف", at=1.0, bg="green")]),
   dict(k="warn", text="ما تعطي السبيد ولا الكود لحتى واحد", at="وحاجة أخيرة", until="سيفي هاد الفيديو", y=640),
   dict(k="map", **MED, route=["Milano", "Casablanca"], at="سيفي هاد الفيديو", until="وإلى عجبك هاد الفيديو", box=BIGMAP),
   dict(k="cta", at="وإلى عجبك هاد الفيديو", until="وإلى عندك شي صاحب", text="ابوني فالقناة", sub="وفعل الجرس"),
   dict(k="people", at="وإلى عندك شي صاحب", box=FULL, people=["girl", "worker", "hijab"],
        say=[dict(who=1, text="شنو فادك أكثر؟", at=3.0), dict(who=2, text="صيفطو لشي واحد", at=8.0, bg="green")]),
 ]),
]

THUMB = dict(
  title=[("مسافر للمغرب فدجنبر؟", (236, 196, 96)), "الإضراب ديال التران والطيارات", "والديكري فلوسي حتى 7 دجنبر"],
  num="4/12", numsub="الإضراب العام",
  bottom="مغاربة إيطاليا · خبار مفيدة بالدارجة",
)
