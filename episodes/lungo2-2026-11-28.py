import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_J1 = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-28-f.json"), encoding="utf-8"))
_J2 = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-28-r.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo2-2026-11-28-final")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = {k: v.replace("گ", "ك") for k, v in {**_J1["blocks"], **_J2["blocks"]}.items()}

S_HOME = "مغاربة إيطاليا · دليل عملي بالدارجة"
S_CCNL = "CCNL lavoro domestico 28/10/2025 · tabelle 2026: LeggeInChiaro, InformazioneFiscale, Money.it, QuiFinanza · calcoli nostri"
S_DOC = "Cose di Casa 25/11/2026 · BusinessOnline · FiscoeTasse · Money.it"
S_MA = "Money.it · FiscoeTasse (ferie) · Min. Lavoro circ. 7185/2026 · InformazioneFiscale · registro 13/11 e 21/11"
S_INPS = "INPS circ. 9 del 3/2/2026 via InformazioneFiscale e LeggiOggi · Money.it · Centro Fiscale · calcoli nostri"
S_DIR = "BusinessOnline · Ticonsiglio · InformazioneFiscale · Money.it · CGIL Lazio"
S_ERR = "BusinessOnline · Ticonsiglio · Centro Fiscale · INPS (NASpI)"
S_QA = "Fonti dei capitoli 01-07"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850); FULL = (160, 300, 1760, 860); MID = (260, 220, 1660, 840)
ICB = (160, 330, 1760, 860); VSB = (260, 220, 1660, 820); BARB = (160, 330, 1760, 840); BIGMAP = (160, 200, 1760, 880)
DOCB = (560, 170, 1360, 880)

MED_PD = dict(view="med", hl=["ITA", "MAR"], route=["Casablanca", "Padova", "plane"], pins=["Casablanca", "Padova"], labels=False)
MED_TO = dict(view="med", hl=["ITA", "MAR"], route=["Casablanca", "Torino", "plane"], pins=["Casablanca", "Torino"], labels=False)
MED_FI = dict(view="med", hl=["ITA", "MAR"], route=["Casablanca", "Firenze", "plane"], pins=["Casablanca", "Firenze"], labels=False)
MED_BM = dict(view="med", hl=["ITA", "MAR"], route=["Beni Mellal", "Torino", "plane"], pins=["Beni Mellal", "Torino"], labels=False)
MAROC = dict(view="maroc", hl=["MAR"], pins=["Rabat"], labels=False)
N_PD = dict(view="north", pins=["Padova"], labels=False)
N_TO = dict(view="north", pins=["Torino"], labels=False)
IT_FI = dict(view="italy", pins=["Firenze"], labels=False)
IT_ALL = dict(view="north", pins=["Torino", "Padova", "Firenze"], labels=False)
IT_RM = dict(view="italy", pins=["Roma"], labels=False)

DOC_ROWS = ["LIVELLO", "ORE", "PAGA ORARIA", "VITTO E ALLOGGIO", "CONTRIBUTI", "NETTO"]
def DOC(focus, tag, at, until):
    return dict(k="doc", at=at, until=until, box=DOCB, title="BUSTA PAGA · LAVORO DOMESTICO", rows=DOC_ROWS,
                focus=focus, tag=tag, done=list(range(focus)), warn=[], doc_at=0.4)

BLOCKS = [
 # ---------------------------------------------------------------- 01
 dict(audio="A.wav", text=T["A"], chapter="01 · شكون خاصو هاد الدليل", src=S_HOME, items=[
   dict(k="head", text="الخدمة فالديور: كولف وبادانتي", at=0.2, until="الكولف اللي كتنقي", sub="الخلصة والحقوق 2026"),
   dict(k="icons", at="الكولف اللي كتنقي", until="واش نتي كتخدمي", box=ICB, items=[
     ["home", "الكولف", "blue"], ["heart", "البادانتي", "gold"], ["users", "البيبي سيتر", "green"]], gap=1.8),
   dict(k="people", at="واش نتي كتخدمي", until="وهاد الموضوع كيهم", box=FULL, people=["hijab", "man"],
        say=[dict(who=0, text="كنخدم فالديور", at=0.8, bg="gold"), dict(who=1, text="باغي بادانتي لبابا", at=3.5, bg="green")]),
   dict(k="vs", at="وهاد الموضوع كيهم", until="خاصنا نبداو بحاجة مهمة", box=VSB,
        right=dict(title="الخدامة", value="الحقوق", sub="الخلصة والراحة", person="hijab", color="gold"),
        left=dict(title="العائلة", value="الواجبات", sub="الإينبس والوراق", person="man", color="green"), gap=6.0),
   dict(k="big", text="28/10/2025", sub="الكونطرا الجديد ديال الخدمة المنزلية", at="خاصنا نبداو بحاجة مهمة", until="وفيه الخلصة الدنيا"),
   dict(k="icons", at="وفيه الخلصة الدنيا", until="وفهاد الدليل غادي نجاوبو", box=ICB, items=[
     ["wallet", "الخلصة", "gold"], ["clock", "السوايع", "blue"], ["plane", "العطلة", "green"], ["pig-money", "التي إف إر", "blue"]], gap=1.2, cols=4),
   dict(k="steps", at="وفهاد الدليل غادي نجاوبو", until="ومن بعد غادي نشوفو", box=MID, steps=[
     ["الخلصة 2026", "1"], ["المستوى والسوايع", "2"], ["الوراق", "3"], ["الكونطريبيوطي", "4"], ["المرض والخروج", "5"]], gap=2.2, check_after=0.6),
   dict(k="map", at="ومن بعد غادي نشوفو", until="شحال كتشد البادانتي", box=BIGMAP, **MED_PD),
   dict(k="icons", at="شحال كتشد البادانتي", until="وعلاش هاد الموضوع مهم", box=ICB, items=[
     ["coin-euro", "الخلصة فالشهر", "gold"], ["receipt", "الكونطريبيوطي", "blue"], ["calculator", "الكلفة فالعام", "green"]], gap=2.5),
   dict(k="people", at="وعلاش هاد الموضوع مهم", until="ولكن فالحقيقة", box=FULL, people=["hijab", "man"],
        say=[dict(who=1, text="بلا كونطرا أحسن ليك", at=2.5, bg="red")]),
   dict(k="icons", at="ولكن فالحقيقة", until="وعندنا تلاتة ديال الحالات", box=ICB, items=[
     ["x", "الكونطريبيوطي", "red"], ["x", "البانسيون", "red"], ["x", "النازبي", "red"], ["x", "البيرميسو", "red"]], gap=1.5, cols=4),
   dict(k="text", text="تلاتة ديال الحالات", at="وعندنا تلاتة ديال الحالات", until="الحالة الأولى، نعيمة", y=520, size=96, color=GOLD),
   dict(k="map", at="الحالة الأولى، نعيمة", until="الحالة التانية، سميرة", box=L_BOX, **N_PD),
   dict(k="people", at="الحالة الأولى، نعيمة", until="الحالة التانية، سميرة", box=R_BOX, people=["hijab", "elder"],
        say=[dict(who=0, text="نعيمة · بادوفا", at=0.8, bg="gold")]),
   dict(k="map", at="الحالة التانية، سميرة", until="والحالة التالتة، حسن", box=L_BOX, **IT_FI),
   dict(k="people", at="الحالة التانية، سميرة", until="والحالة التالتة، حسن", box=R_BOX, people=["woman"],
        say=[dict(who=0, text="سميرة · فيرينزي", at=0.8, bg="gold")]),
   dict(k="map", at="والحالة التالتة، حسن", until="وقبل ما نبداو", box=L_BOX, **N_TO),
   dict(k="people", at="والحالة التالتة، حسن", until="وقبل ما نبداو", box=R_BOX, people=["man", "elder"],
        say=[dict(who=0, text="حسن · تورينو", at=0.8, bg="gold")]),
   dict(k="warn", text="محتوى إخباري · ماشي استشارة قانونية", at="وقبل ما نبداو", until="يلاه نبداو", y=600),
   dict(k="text", text="يلاه نبداو", at="يلاه نبداو", until=None, y=540, size=110, color=GOLD),
 ]),
 # ---------------------------------------------------------------- 02
 dict(audio="B.wav", text=T["B"], chapter="02 · المستوى والسوايع والخلصة 2026", src=S_CCNL, items=[
   dict(k="chapter", num="02", title="المستوى والخلصة", at=0.1, until="الكونطرا فيه تمنية"),
   dict(k="big", text="8", sub="ديال المستويات فالكونطرا", at="الكونطرا فيه تمنية", until="المستوى بي: الكولف"),
   dict(k="rows", at="المستوى بي: الكولف", until="وخاصك تعرف بلي المستوى", y=230, gap=120, size=46, rows=[
     ("الكولف العادية", "B", "المستوى بي: الكولف"),
     ("كبير كيدبر راسو · بيبي سيتر", "BS", "المستوى بي إس"),
     ("ما كيقدرش يدبر راسو", "CS", "المستوى سي إس", GOLD),
     ("بادانتي عندها تكوين", "DS", "والمستوى دي إس"),
   ]),
   dict(k="people", at="وخاصك تعرف بلي المستوى", until="الحاجة التانية: واش ساكنة", box=FULL, people=["hijab", "elder"],
        say=[dict(who=0, text="مكتوب كولف؟", at=3.0, bg="red"), dict(who=0, text="والخدمة بادانتي!", at=7.0, bg="gold")]),
   dict(k="vs", at="الحاجة التانية: واش ساكنة", until="والسوايع: اللي ساكنة", box=VSB,
        right=dict(title="ساكنة مع العائلة", value="بالشهر", sub="كونفيفينتي", icon="home", color="gold"),
        left=dict(title="ما ساكناش", value="بالساعة", sub="نون كونفيفينتي", icon="clock", color="blue"), gap=3.0),
   dict(k="bars", at="والسوايع: اللي ساكنة", until="واللي ساكنة مع العائلة عندها", box=BARB, bars=[
     ["ساكنة · فالسيمانة", 54, "54", "gold"], ["ما ساكناش · فالسيمانة", 40, "40", "blue"]], gap=4.0),
   dict(k="vs", at="واللي ساكنة مع العائلة عندها", until="دابا الخلصة الدنيا", box=VSB,
        right=dict(title="ساكنة · الراحة", value="36", sub="ساعة فالسيمانة", icon="calendar", color="gold"),
        left=dict(title="ما ساكناش · الراحة", value="24", sub="ساعة فالسيمانة", icon="calendar", color="blue"), gap=3.5),
   dict(k="calendar", at="دابا الخلصة الدنيا", until="البادانتي سي إس ساكنة", box=MID, day=1, month=1, sub="الخلصة الجديدة 2026"),
   dict(k="big", text="1.193,84 €", sub="سي إس ساكنة · فالشهر خام", at="البادانتي سي إس ساكنة", until="وهادي زادت"),
   dict(k="bars", at="وهادي زادت", until="البي إس ساكنة", box=BARB, bars=[
     ["2025", 1137.86, "1.137,86 €", "grey"], ["2026", 1193.84, "1.193,84 €", "gold"]], gap=1.5),
   dict(k="bars", at="البي إس ساكنة", until="واللي ما ساكناش، بالساعة", box=BARB, bars=[
     ["BS", 1053.39, "1.053,39 €", "blue"], ["CS", 1193.84, "1.193,84 €", "gold"], ["DS", 1474.73, "1.474,73 €", "green"]], gap=1.5),
   dict(k="bars", at="واللي ما ساكناش، بالساعة", until="وزايد على هادشي", box=BARB, bars=[
     ["A", 6.51, "6,51 €", "grey"], ["B", 7.01, "7,01 €", "blue"], ["BS", 7.45, "7,45 €", "gold"]], gap=1.5),
   dict(k="icons", at="وزايد على هادشي", until="ستة أورو وستة وستين", box=ICB, items=[
     ["shopping-cart", "الماكلة", "gold"], ["home", "النعاس", "blue"]], gap=2.0),
   dict(k="stats", stats=[("6,66 €", "فالنهار", None), ("199,80 €", "فالشهر", "يعني تقريبا ميتين")], at="ستة أورو وستة وستين", until="وهاد الأرقام غادي تزيد"),
   dict(k="steps", at="وهاد الأرقام غادي تزيد", until="مثال سميرة", box=MID, steps=[
     ["2026", "1"], ["2027", "2"], ["2028", "3"]], gap=1.5, check_after=0.4),
   dict(k="map", at="مثال سميرة", until="الحساب ديالنا: هادي", box=L_BOX, **IT_FI),
   dict(k="people", at="مثال سميرة", until="الحساب ديالنا: هادي", box=R_BOX, people=["woman"],
        say=[dict(who=0, text="25 ساعة فالسيمانة", at=2.0, bg="gold")]),
   dict(k="rows", at="الحساب ديالنا: هادي", until="ونعيمة فـبادوفا", y=260, gap=120, size=46, rows=[
     ("الخلصة فالساعة · B", "7,01 €", "الحساب ديالنا: هادي"),
     ("السوايع فالسيمانة", "25", "الحساب ديالنا: هادي"),
     ("فالشهر · خام · تقريبا", "760 €", "سبعمية وستين", GOLD),
   ]),
   dict(k="map", at="ونعيمة فـبادوفا", until="والفرق بين جوج حالات", box=L_BOX, **N_PD),
   dict(k="people", at="ونعيمة فـبادوفا", until="والفرق بين جوج حالات", box=R_BOX, people=["hijab", "elder"],
        say=[dict(who=0, text="سي إس · 1.193 أورو", at=3.0, bg="gold")]),
   dict(k="vs", at="والفرق بين جوج حالات", until=None, box=VSB,
        right=dict(title="نعيمة", value="بالشهر", sub="ساكنة", person="hijab", color="gold"),
        left=dict(title="سميرة", value="بالساعة", sub="ما ساكناش", person="woman", color="blue"), gap=2.0),
 ]),
 # ---------------------------------------------------------------- 03
 dict(audio="C.wav", text=T["C"], chapter="03 · الوراق والكونطرا والبوستا باغا", src=S_DOC, items=[
   dict(k="chapter", num="03", title="الوراق والكونطرا", at=0.1, until="أولا، ليطيرا ديال التشغيل"),
   dict(k="icons", at="أولا، ليطيرا ديال التشغيل", until="وفيها: النهار اللي", box=ICB, items=[
     ["file-text", "ليطيرا مكتوبة", "gold"], ["users", "مسينيا من جوج", "green"]], gap=3.0),
   dict(k="rows", at="وفيها: النهار اللي", until="والنصيحة ديالنا", y=200, gap=88, size=42, rows=[
     ("النهار الأول", "1", "وفيها: النهار اللي"),
     ("الخدمة والمستوى", "2", "والخدمة اللي كديري"),
     ("السوايع والخلصة", "3", "والسوايع، والخلصة"),
     ("محدودة ولا لا", "4", "واش الكونطرا محدودة"),
     ("فترة التجربة", "5", "وفترة التجربة"),
     ("ساكنة ولا لا", "6", "وواش ساكنة"),
   ]),
   dict(k="people", at="والنصيحة ديالنا", until="ودابا كيفاش تقراي", box=FULL, people=["hijab"],
        say=[dict(who=0, text="عندي نسخة", at=1.0, bg="green")]),
   DOC(0, "06 · LIVELLO", "ودابا كيفاش تقراي", "أوري: السوايع"),
   DOC(1, "05 · ORE", "أوري: السوايع", "باغا أوراريا"),
   DOC(2, "04 · PAGA ORARIA", "باغا أوراريا", "فيتو إي ألودجو"),
   DOC(3, "03 · VITTO E ALLOGGIO", "فيتو إي ألودجو", "كونطريبوتي: الجزء"),
   DOC(4, "02 · CONTRIBUTI", "كونطريبوتي: الجزء", "والنيتو"),
   DOC(5, "01 · NETTO", "والنيتو", "إلى شي رقم ما فهمتيهش"),
   dict(k="people", at="إلى شي رقم ما فهمتيهش", until="ثانيا، التصريح فالإينبس", box=FULL, people=["hijab", "office"],
        say=[dict(who=0, text="شنو هادا؟", at=0.8, bg="gold"), dict(who=1, text="نشرحو ليك", at=3.0, bg="green")]),
   dict(k="big", text="قبل النهار الأول", sub="التصريح فالإينبس", at="ثانيا، التصريح فالإينبس", until="ويقدر يديرها فالسيت"),
   dict(k="icons", at="ويقدر يديرها فالسيت", until="شنو هي الوراق اللي كتطلب", box=ICB, items=[
     ["id", "السبيد ولا الكارطا", "blue"], ["phone", "الكونطاكت سانتر", "gold"], ["building-bank", "الباترونا", "green"]], gap=2.5),
   dict(k="icons", at="شنو هي الوراق اللي كتطلب", until="ثالثا، البوستا باغا", box=ICB, items=[
     ["id", "الكودتشي فيسكالي", "blue"], ["license", "ورقة التعريف", "gold"], ["e-passport", "البيرميسو", "green"]], gap=2.0),
   dict(k="vs", at="ثالثا، البوستا باغا", until="حتى هادي خبيها", box=VSB,
        right=dict(title="كل شهر", value="البوستا باغا", sub="الخلصة بالتفصيل", icon="receipt", color="gold"),
        left=dict(title="آخر العام", value="الملخص", sub="كلشي اللي تخلص", icon="file-text", color="blue"), gap=4.0),
   dict(k="icons", at="حتى هادي خبيها", until="رابعا، إلى كان شي تغيير", box=ICB, items=[
     ["e-passport", "البيرميسو", "blue"], ["calculator", "الإيزي", "gold"], ["wallet", "النازبي", "green"], ["certificate", "الجنسية", "blue"]], gap=1.2, cols=4),
   dict(k="steps", at="رابعا، إلى كان شي تغيير", until="ودابا مثال حسن", box=MID, steps=[
     ["زادو السوايع", "1"], ["تبدلات الخلصة", "2"], ["تسالات الخدمة", "3"]], gap=1.8, check_after=0.5),
   dict(k="map", at="ودابا مثال حسن", until="شنو خاص يدير حسن", box=BIGMAP, **MED_TO),
   dict(k="steps", at="شنو خاص يدير حسن", until="وسؤال كيتعاود بزاف", box=MID, steps=[
     ["البيرميسو ديال خديجة", "1"], ["ليطيرا · CS", "2"], ["الإينبس قبل النهار الأول", "3"], ["البوستا باغا", "4"], ["الكونطريبيوطي", "5"]], gap=3.5, check_after=0.6),
   dict(k="people", at="وسؤال كيتعاود بزاف", until="وحاجة أخيرة فهاد الفصل", box=FULL, people=["man", "elder"],
        say=[dict(who=0, text="شكون المعلم؟", at=1.0, bg="gold"), dict(who=1, text="أنا ولا نتا؟", at=3.5, bg="green")]),
   dict(k="people", at="وحاجة أخيرة فهاد الفصل", until=None, box=FULL, people=["man", "hijab"],
        say=[dict(who=0, text="بدا ومن بعد الوراق", at=4.0, bg="red"), dict(who=1, text="بغيت ليطيرا دابا", at=8.0, bg="green")]),
 ]),
 # ---------------------------------------------------------------- 04
 dict(audio="D.wav", text=T["D"], chapter="04 · والمغرب؟ العطلة والسفر والديكري", src=S_MA, items=[
   dict(k="chapter", num="04", title="والمغرب؟", at=0.1, until="عندنا تلاتة ديال المواضيع"),
   dict(k="icons", at="عندنا تلاتة ديال المواضيع", until="أولا، العطلة", box=ICB, items=[
     ["plane", "العطلة", "gold"], ["e-passport", "البيرميسو", "blue"], ["users", "بادانتي من المغرب", "green"]], gap=2.0),
   dict(k="big", text="26", sub="يوم ديال العطلة فالعام", at="أولا، العطلة", until="والأيام كتحسب"),
   dict(k="text", text="من الاثنين حتى السبت", at="والأيام كتحسب", until="والمعلم هو اللي كيحدد", y=540, size=90, color=GOLD),
   dict(k="calendar", at="والمعلم هو اللي كيحدد", until="والعطلة تقدر تتقسم", box=MID, day="6-9", month="الصيف", sub="غالبا بين يونيو وشتنبر"),
   dict(k="text", text="جوج ديال المرات فالعام · ماشي كثر", at="والعطلة تقدر تتقسم", until="وهنا كاينة واحد النقطة", y=560, size=76, color=WHITE),
   dict(k="map", at="وهنا كاينة واحد النقطة", until="ولكن بشرط", box=BIGMAP, **MED_PD),
   dict(k="people", at="ولكن بشرط", until="يعني بدل ما تمشي", box=FULL, people=["hijab", "man"],
        say=[dict(who=0, text="نجمع جوج سنين؟", at=0.5, bg="gold"), dict(who=1, text="موافق", at=1.8, bg="green")]),
   dict(k="vs", at="يعني بدل ما تمشي", until="والنصيحة ديالنا: كتبو", box=VSB,
        right=dict(title="كل عام", value="26 يوم", sub="العطلة العادية", icon="calendar", color="blue"),
        left=dict(title="مجموعة", value="2 سنين", sub="تقريبا شهرين للمغرب", icon="plane", color="gold"), gap=2.5),
   dict(k="icons", at="والنصيحة ديالنا: كتبو", until="ثانيا، السفر مع البيرميسو", box=ICB, items=[
     ["file-text", "الاتفاق مكتوب", "gold"], ["check", "مسيني من جوج", "green"]], gap=2.0),
   dict(k="map", at="ثانيا، السفر مع البيرميسو", until="وخودي معاك الباسبور", box=BIGMAP, **MED_FI),
   dict(k="icons", at="وخودي معاك الباسبور", until="وتذكير مهم", box=ICB, items=[
     ["e-passport", "الباسبور", "blue"], ["id", "البيرميسو القديم", "gold"], ["receipt", "الريسيفوتا", "green"]], gap=1.5),
   dict(k="big", text="90", sub="يوم قبل · طلب التجديد", at="وتذكير مهم", until="ثالثا، كيفاش عائلة"),
   dict(k="map", at="ثالثا، كيفاش عائلة", until="فألفين وسبعة وعشرين، كاينين", box=BIGMAP, **MED_BM),
   dict(k="big", text="14.000", sub="بلاصة · المساعدة العائلية 2027", at="فألفين وسبعة وعشرين، كاينين", until="والطلب كيديرو المعلم"),
   dict(k="people", at="والطلب كيديرو المعلم", until="والبريكومبيلاسيون خاصها", box=FULL, people=["man", "hijab"],
        say=[dict(who=0, text="أنا اللي كندير الطلب", at=0.8, bg="green")]),
   dict(k="calendar", at="والبريكومبيلاسيون خاصها", until="والكليك داي ديال", box=MID, day=7, month=12, sub="البريكومبيلاسيون · 20:00"),
   dict(k="calendar", at="والكليك داي ديال", until="وخاص المعلم يكون", box=MID, day=18, month=2, sub="الكليك داي · 9:00"),
   dict(k="icons", at="وخاص المعلم يكون", until="ومن بعد كتجي النولا", box=ICB, items=[
     ["id", "السبيد ولا الكارطا", "blue"], ["mail", "البيك", "gold"], ["file-text", "3 طلبات بوحدك", "green"]], gap=2.5),
   dict(k="steps", at="ومن بعد كتجي النولا", until="ونعاودو: الطلب", box=MID, steps=[
     ["النولا أوسطا", "1"], ["الفيزا فالقنصلية", "2"], ["الكونطرا ديال الإقامة", "3"]], gap=2.5, check_after=0.5),
   dict(k="people", at="ونعاودو: الطلب", until="وحاجة أخيرة: الكونطريبيوطي", box=FULL, people=["man", "worker"],
        say=[dict(who=0, text="عندي ليك كونطرا بالفلوس", at=1.0, bg="red"), dict(who=1, text="لا، هادا نصب", at=4.5, bg="green")]),
   dict(k="icons", at="وحاجة أخيرة: الكونطريبيوطي", until="ومثال نعيمة", box=ICB, items=[
     ["receipt", "الكونطريبيوطي", "blue"], ["chart-bar", "الحساب فالإينبس", "gold"], ["pig-money", "البانسيون", "green"]], gap=2.5),
   dict(k="map", at="ومثال نعيمة", until="شنو دير؟", box=L_BOX, **N_PD),
   dict(k="people", at="ومثال نعيمة", until="شنو دير؟", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="شهرين فالمغرب", at=2.0, bg="gold")]),
   dict(k="steps", at="شنو دير؟", until=None, box=MID, steps=[
     ["تهضر مع المعلم", "1"], ["الطلب مكتوب", "2"], ["الموافقة فورقة", "3"], ["تشوف البيرميسو", "4"]], gap=2.0, check_after=0.6),
 ]),
 # ---------------------------------------------------------------- 05
 dict(audio="E.wav", text=T["E"], chapter="05 · الكونطريبيوطي والخطوات والكلفة", src=S_INPS, items=[
   dict(k="chapter", num="05", title="الكونطريبيوطي والكلفة", at=0.1, until="والأرقام ديال ألفين وستة"),
   dict(k="big", text="9/2026", sub="المنشور ديال الإينبس · 3 فبراير", at="والأرقام ديال ألفين وستة", until="وكاين جزء كيخلصو"),
   dict(k="vs", at="وكاين جزء كيخلصو", until="للكونطرا اللي ما عندهاش", box=VSB,
        right=dict(title="المعلم", value="الجزء الكبير", sub="", icon="user", color="gold"),
        left=dict(title="الخدامة", value="جزء صغير", sub="من الخلصة", icon="wallet", color="blue"), gap=2.5),
   dict(k="rows", at="للكونطرا اللي ما عندهاش", until="وإلى كانت الكونطرا محدودة", y=210, gap=120, size=42, rows=[
     ("الخلصة حتى 9,61 فالساعة", "1,70 €", "للكونطرا اللي ما عندهاش"),
     ("من 9,61 حتى 11,70", "1,92 €", "ومن تسعة وواحد وستين"),
     ("فوق 11,70", "2,34 €", "وفوق هادشي"),
     ("كثر من 24 ساعة فالسيمانة", "1,24 €", "وإلى كانت الخدمة كثر", GOLD),
   ]),
   dict(k="text", text="الكونطرا المحدودة · زيادة على المعلم", at="وإلى كانت الكونطرا محدودة", until="إمتى كيتخلصو", y=560, size=76, color=WHITE),
   dict(k="steps", at="إمتى كيتخلصو", until="يعني الكونطريبيوطي ديال أكتوبر", box=MID, steps=[
     ["1-10 أبريل", "1"], ["1-10 يوليوز", "2"], ["1-10 أكتوبر", "3"], ["1-10 يناير", "4"]], gap=2.5, check_after=0.6),
   dict(k="calendar", at="يعني الكونطريبيوطي ديال أكتوبر", until="وإلى تسالات الخدمة، كيتخلصو", box=MID, day=10, month=1, sub="أكتوبر · نونبر · دجنبر"),
   dict(k="big", text="10", sub="أيام من النهاية ديال الخدمة", at="وإلى تسالات الخدمة، كيتخلصو", until="والخلاص كيكون بالباغو با"),
   dict(k="icons", at="والخلاص كيكون بالباغو با", until="دابا الحساب ديالنا", box=ICB, items=[
     ["credit-card", "الباغو با", "blue"], ["world", "الأفيزو أونلاين", "gold"]], gap=2.0),
   dict(k="map", at="دابا الحساب ديالنا", until="منها تقريبا حداش", box=L_BOX, **IT_FI),
   dict(k="people", at="دابا الحساب ديالنا", until="منها تقريبا حداش", box=R_BOX, people=["woman"],
        say=[dict(who=0, text="25 ساعة", at=1.5, bg="gold")]),
   dict(k="bars", at="منها تقريبا حداش", until="ونعيمة، ساكنة مع الشيباني", box=BARB, bars=[
     ["فالسيمانة", 42.5, "42,50 €", "blue"], ["على سميرة", 10.75, "10,75 €", "grey"], ["تلت شهور", 552.5, "552,50 €", "gold"]], gap=1.5),
   dict(k="map", at="ونعيمة، ساكنة مع الشيباني", until="يعني تقريبا سبعة وستين", box=L_BOX, **N_PD),
   dict(k="people", at="ونعيمة، ساكنة مع الشيباني", until="يعني تقريبا سبعة وستين", box=R_BOX, people=["hijab", "elder"],
        say=[dict(who=0, text="54 ساعة", at=1.5, bg="gold")]),
   dict(k="bars", at="يعني تقريبا سبعة وستين", until="وشنو كيربح المعلم", box=BARB, bars=[
     ["فالسيمانة", 66.96, "66,96 €", "blue"], ["تلت شهور", 870.48, "870,48 €", "gold"]], gap=2.0),
   dict(k="big", text="1.549,37 €", sub="الكونطريبيوطي كينقصو من الدخل", at="وشنو كيربح المعلم", until="وإلى كانت البادانتي لشخص"),
   dict(k="rows", at="وإلى كانت البادانتي لشخص", until="وخاص الخلاص يكون", y=260, gap=120, size=46, rows=[
     ("الخصم", "19%", "كاين خصم ديال"),
     ("على حد", "2.100 €", "على حد ألفين"),
     ("يعني حتى", "399 €", "يعني حتى تلت مية", GOLD),
   ]),
   dict(k="warn", text="الخلاص بطريقة كتبان · ماشي كاش", at="وخاص الخلاص يكون", until="والخطوات بالترتيب", y=600),
   dict(k="steps", at="والخطوات بالترتيب", until="ومثال حسن فـتورينو", box=MID, steps=[
     ["الوراق", "1"], ["ليطيرا", "2"], ["الإينبس", "3"], ["البوستا باغا", "4"], ["الكونطريبيوطي", "5"], ["التريديتشيزيما والتي إف إر", "6"]], gap=1.5, check_after=0.5),
   dict(k="map", at="ومثال حسن فـتورينو", until="وإلى جمعنا الخلصة", box=L_BOX, **N_TO),
   dict(k="people", at="ومثال حسن فـتورينو", until="وإلى جمعنا الخلصة", box=R_BOX, people=["man", "hijab"],
        say=[dict(who=0, text="870 كل تلت شهور", at=3.0, bg="gold")]),
   dict(k="rows", at="وإلى جمعنا الخلصة", until="يعني البادانتي القانونية", y=260, gap=120, size=44, rows=[
     ("الخلصة × 13", "15.520 €", "وإلى جمعنا الخلصة"),
     ("الكونطريبيوطي فالعام", "3.482 €", "زايد الكونطريبيوطي"),
     ("المجموع تقريبا", "19.000 €", "تسعطاش ألف", GOLD),
   ]),
   dict(k="people", at="يعني البادانتي القانونية", until=None, box=FULL, people=["man", "hijab", "elder"],
        say=[dict(who=0, text="ماشي رخيصة", at=0.8, bg="gold"), dict(who=1, text="ولكن محمية", at=3.0, bg="green")]),
 ]),
 # ---------------------------------------------------------------- 06
 dict(audio="F.wav", text=T["F"], chapter="06 · الحقوق والحالات الخاصة", src=S_DIR, items=[
   dict(k="chapter", num="06", title="الحقوق ديالك", at=0.1, until="التريديتشيزيما: عندك الحق"),
   dict(k="icons", at="التريديتشيزيما: عندك الحق", until="وتقدري تطلبي سلفة", box=ICB, items=[
     ["coin-euro", "التريديتشيزيما", "gold"], ["pig-money", "التي إف إر", "blue"]], gap=4.0),
   dict(k="big", text="70%", sub="سلفة من التي إف إر", at="وتقدري تطلبي سلفة", until="المرض: إلى مرضتي"),
   dict(k="people", at="المرض: إلى مرضتي", until="والكونطرا كيحفظ ليك", box=FULL, people=["hijab", "doctor"],
        say=[dict(who=1, text="هاهي الشهادة", at=3.0, bg="green")]),
   dict(k="bars", at="والكونطرا كيحفظ ليك", until="البيرميسي: اللي ساكنة", box=BARB, bars=[
     ["أقل من 6 شهور", 10, "10", "grey"], ["6 شهور - 2 سنين", 45, "45", "blue"], ["كثر من 2 سنين", 180, "180", "gold"]], gap=2.5),
   dict(k="stats", stats=[("16", "ساعة فالعام · الوقت الكامل", None), ("12", "ساعة · نص الوقت", "ومع نص الوقت")], at="البيرميسي: اللي ساكنة", until="وإلى مات شي حد"),
   dict(k="big", text="3", sub="أيام · وفاة شي حد قريب", at="وإلى مات شي حد", until="الحد والعيد"),
   dict(k="big", text="60%", sub="زيادة · الحد والعيد", at="الحد والعيد", until="الأقدمية: كل جوج"),
   dict(k="steps", at="الأقدمية: كل جوج", until="الماماوات: إلى كنتي", box=MID, steps=[
     ["جوج سنين", "4%"], ["ربعة سنين", "8%"], ["حتى سبعة ديال المرات", "7"]], gap=1.8, check_after=0.5),
   dict(k="people", at="الماماوات: إلى كنتي", until="والضرائب: هنا كاينة", box=FULL, people=["hijab", "office"],
        say=[dict(who=0, text="أنا حاملة", at=1.0, bg="gold"), dict(who=1, text="ما تسينيش قبل ما تسولي", at=3.0, bg="green")]),
   dict(k="vs", at="والضرائب: هنا كاينة", until="هاد البونس، سميتو", box=VSB,
        right=dict(title="خدام عادي", value="فالبوستا باغا", sub="البونس كيوصل بوحدو", icon="briefcase", color="blue"),
        left=dict(title="خدامة فالدار", value="فالسبعمية وتلاتين", sub="خاصها تطلبو", icon="home", color="gold"), gap=4.0),
   dict(k="big", text="1.200 €", sub="حتى · فالعام · الدخل تحت 15.000", at="هاد البونس، سميتو", until="وباش تاخديه"),
   dict(k="icons", at="وباش تاخديه", until="وإلى كنتي كتخدمي عند جوج", box=ICB, items=[
     ["file-text", "730", "gold"], ["file-certificate", "الريديتي", "blue"], ["building-bank", "الكاف ولا الباترونا", "green"]], gap=2.0),
   dict(k="people", at="وإلى كنتي كتخدمي عند جوج", until="وحالة كتوقع بزاف", box=FULL, people=["woman", "man", "elder"],
        say=[dict(who=1, text="كونطرا ديالي", at=2.0, bg="gold"), dict(who=2, text="وكونطرا ديالي", at=4.0, bg="green")]),
   dict(k="people", at="وحالة كتوقع بزاف", until="العائلة خاصها تسالي", box=FULL, people=["hijab", "man"],
        say=[dict(who=1, text="الله يرحمو", at=2.0, bg="gold")]),
   dict(k="icons", at="العائلة خاصها تسالي", until="ومن بعد، مشي للباترونا", box=ICB, items=[
     ["calendar", "الأيام", "blue"], ["plane", "العطلة", "gold"], ["coin-euro", "التريديتشيزيما", "green"], ["pig-money", "التي إف إر", "blue"]], gap=1.5, cols=4),
   dict(k="map", at="ومن بعد، مشي للباترونا", until="والبيبي سيتر", box=BIGMAP, **IT_ALL),
   dict(k="people", at="والبيبي سيتر", until="ومثال سميرة", box=FULL, people=["woman", "child"],
        say=[dict(who=0, text="بي إس · 7,45 أورو", at=2.5, bg="gold")]),
   dict(k="map", at="ومثال سميرة", until="سميرة خاصها جوج", box=L_BOX, **IT_FI),
   dict(k="people", at="ومثال سميرة", until="سميرة خاصها جوج", box=R_BOX, people=["woman"],
        say=[dict(who=0, text="جوج عائلات", at=1.5, bg="gold")]),
   dict(k="steps", at="سميرة خاصها جوج", until=None, box=MID, steps=[
     ["جوج كونطرات", "1"], ["جوج بوستا باغا", "2"], ["730 عند الكاف", "3"]], gap=2.0, check_after=0.5),
 ]),
 # ---------------------------------------------------------------- 07
 dict(audio="G.wav", text=T["G"], chapter="07 · الغلطات وشنو دير إلى مشات خايبة", src=S_ERR, items=[
   dict(k="chapter", num="07", title="الغلطات", at=0.1, until="الغلطة الأولى"),
   dict(k="people", at="الغلطة الأولى", until="الغلطة التانية", box=FULL, people=["hijab"],
        say=[dict(who=0, text="بلا كونطرا؟ لا", at=1.0, bg="red")]),
   dict(k="vs", at="الغلطة التانية", until="الغلطة التالتة", box=VSB,
        right=dict(title="فالكونطرا", value="20", sub="ساعة", icon="file-text", color="grey"),
        left=dict(title="فالحقيقة", value="40", sub="ساعة", icon="clock", color="red"), gap=2.5),
   dict(k="steps", at="الغلطة التالتة", until="والغلطات ديال المعلم", box=MID, steps=[
     ["المستوى غالط", "3"], ["بلا نسخة", "4"], ["العطلة بالهضرة", "5"], ["البيرميسو", "6"], ["ورقة ما فاهماهاش", "7"]], gap=3.5, check_after=0.5, bad=True),
   dict(k="people", at="والغلطات ديال المعلم", until="والغلطة الكبيرة", box=FULL, people=["man", "office"],
        say=[dict(who=1, text="التصريح قبل النهار الأول", at=1.5, bg="red")]),
   dict(k="warn", text="الكونطرا ما كيتشراش", at="والغلطة الكبيرة", until="والغلطة الأخيرة", y=600),
   dict(k="icons", at="والغلطة الأخيرة", until="ودابا، إلى المعلم بغا", box=ICB, items=[
     ["chart-bar", "المستوى", "blue"], ["coin-euro", "الخلصة", "gold"], ["clock", "السوايع", "green"]], gap=1.5),
   dict(k="people", at="ودابا، إلى المعلم بغا", until="إلى كنتي كتخدمي خمسة وعشرين", box=FULL, people=["man", "hijab"],
        say=[dict(who=0, text="غادي نساليو الخدمة", at=1.0, bg="gold"), dict(who=1, text="والبريافيزو؟", at=3.5, bg="green")]),
   dict(k="rows", at="إلى كنتي كتخدمي خمسة وعشرين", until="وإلى ما عطاكش البريافيزو", y=220, gap=110, size=42, rows=[
     ("25 ساعة ولا كثر · حتى 5 سنين", "15", "إلى كنتي كتخدمي خمسة وعشرين"),
     ("25 ساعة ولا كثر · كثر من 5", "30", "وتلاتين يوم"),
     ("أقل من 25 · حتى 2 سنين", "8", "وإلى كنتي كتخدمي أقل"),
     ("أقل من 25 · كثر من 2", "15", "وخمسطاش يوم إلى كانت كثر"),
   ]),
   dict(k="text", text="بلا بريافيزو · كيخلص بلاصتو", at="وإلى ما عطاكش البريافيزو", until="والنازبي: إلى المعلم", y=560, size=80, color=GOLD),
   dict(k="vs", at="والنازبي: إلى المعلم", until="إلى كان عندك على الأقل", box=VSB,
        right=dict(title="حبسوك", value="النازبي", sub="عندك الحق", icon="check", color="green"),
        left=dict(title="خرجتي بإرادتك", value="لا", sub="غالبا ما كاينش", icon="x", color="red"), gap=2.5),
   dict(k="stats", stats=[("13", "سيمانة فربع سنين", None), ("68", "يوم باش تطلبي", "والطلب خاصو يكون")], at="إلى كان عندك على الأقل", until="وإلى بغيتي نتي تخرجي"),
   dict(k="icons", at="وإلى بغيتي نتي تخرجي", until="وإلى ما خلصوكش", box=ICB, items=[
     ["file-text", "ورقة مكتوبة", "blue"], ["clock", "البريافيزو", "gold"], ["check", "نسخة مسينيا", "green"]], gap=1.5),
   dict(k="people", at="وإلى ما خلصوكش", until="وكاين حتى مفتشية الشغل", box=FULL, people=["hijab", "office"],
        say=[dict(who=0, text="ما خلصونيش", at=1.0, bg="red"), dict(who=1, text="نحسبو شنو باقي ليك", at=4.0, bg="green")]),
   dict(k="map", at="وكاين حتى مفتشية الشغل", until="والمهم: خبي الدلائل", box=BIGMAP, **IT_RM),
   dict(k="icons", at="والمهم: خبي الدلائل", until="ومثال خديجة مع حسن", box=ICB, items=[
     ["receipt", "البوستا باغا", "blue"], ["phone", "الميساجات", "gold"], ["building-bank", "التحويلات", "green"], ["users", "الشهود", "blue"]], gap=1.2, cols=4),
   dict(k="map", at="ومثال خديجة مع حسن", until="وخديجة تمشي للباترونا", box=L_BOX, **N_TO),
   dict(k="people", at="ومثال خديجة مع حسن", until="وخديجة تمشي للباترونا", box=R_BOX, people=["man", "hijab"],
        say=[dict(who=0, text="البريافيزو والتي إف إر", at=3.0, bg="gold")]),
   dict(k="big", text="68", sub="يوم باش تطلب النازبي", at="وخديجة تمشي للباترونا", until=None),
 ]),
 # ---------------------------------------------------------------- 08
 dict(audio="H.wav", text=T["H"], chapter="08 · سؤال وجواب", src=S_QA, items=[
   dict(k="chapter", num="08", title="سؤال وجواب", at=0.1, until="السؤال الأول"),
   dict(k="people", at="السؤال الأول", until="الجواب: مشي للسانديكا", box=FULL, people=["hijab"],
        say=[dict(who=0, text="خدمت سنين فالنوار", at=1.0, bg="gold")]),
   dict(k="icons", at="الجواب: مشي للسانديكا", until="السؤال التاني", box=ICB, items=[
     ["building-bank", "السانديكا", "blue"], ["file-text", "الدلائل", "gold"], ["check", "الكونطرا من اليوم", "green"]], gap=2.0),
   dict(k="people", at="السؤال التاني", until="الجواب: فألفين وستة وعشرين، الماكلة", box=FULL, people=["woman"],
        say=[dict(who=0, text="بلا ماكلة؟", at=1.5, bg="gold")]),
   dict(k="stats", stats=[("6,66 €", "فالنهار", None), ("199,80 €", "فالشهر", "يعني تقريبا ميتين")], at="الجواب: فألفين وستة وعشرين، الماكلة", until="السؤال التالت"),
   dict(k="people", at="السؤال التالت", until="الجواب: إيه، كل عائلة", box=FULL, people=["worker"],
        say=[dict(who=0, text="جوج عائلات؟", at=1.0, bg="gold")]),
   dict(k="icons", at="الجواب: إيه، كل عائلة", until="السؤال الرابع", box=ICB, items=[
     ["file-text", "كونطرا لكل عائلة", "blue"], ["receipt", "تصريح لكل عائلة", "gold"]], gap=2.0),
   dict(k="people", at="السؤال الرابع", until="الجواب: العطلة العادية", box=FULL, people=["hijab"],
        say=[dict(who=0, text="شهرين فالمغرب؟", at=1.0, bg="gold")]),
   dict(k="vs", at="الجواب: العطلة العادية", until="السؤال الخامس", box=VSB,
        right=dict(title="العادي", value="26 يوم", sub="كل عام", icon="calendar", color="blue"),
        left=dict(title="مجموعة", value="2 سنين", sub="بموافقة مكتوبة", icon="plane", color="gold"), gap=2.5),
   dict(k="people", at="السؤال الخامس", until="الجواب: ستة وتلاتين ساعة", box=FULL, people=["man", "elder"],
        say=[dict(who=0, text="شحال ديال الراحة؟", at=1.5, bg="gold")]),
   dict(k="stats", stats=[("36", "ساعة راحة فالسيمانة", None), ("54", "ساعة خدمة ماكسيموم", "والماكسيموم ديال الخدمة")], at="الجواب: ستة وتلاتين ساعة", until="السؤال السادس"),
   dict(k="people", at="السؤال السادس", until="الجواب: سالي الكونطرا", box=FULL, people=["man", "woman"],
        say=[dict(who=0, text="بابا مات، شنو نديرو؟", at=1.0, bg="gold")]),
   dict(k="steps", at="الجواب: سالي الكونطرا", until="السؤال السابع", box=MID, steps=[
     ["سالي الكونطرا", "1"], ["الحقوق والتي إف إر", "2"], ["التصريح فالإينبس", "3"]], gap=2.0, check_after=0.5),
   dict(k="people", at="السؤال السابع", until="الجواب: إيه، جزء صغير", box=FULL, people=["hijab"],
        say=[dict(who=0, text="كيتنقصو من الخلصة؟", at=1.0, bg="gold")]),
   dict(k="stats", stats=[("0,43 €", "فالساعة", None), ("0,31 €", "كثر من 24 ساعة", "ولا واحد وتلاتين سنتيم")], at="الجواب: إيه، جزء صغير", until="السؤال التامن"),
   dict(k="people", at="السؤال التامن", until="الجواب: إلى درتي الطلب", box=FULL, people=["woman"],
        say=[dict(who=0, text="عندي غير الريسيفوتا", at=1.5, bg="gold")]),
   dict(k="icons", at="الجواب: إلى درتي الطلب", until="السؤال التاسع", box=ICB, items=[
     ["receipt", "الريسيفوتا", "green"], ["briefcase", "خدمة جديدة", "blue"]], gap=2.0),
   dict(k="people", at="السؤال التاسع", until="الجواب: ما لقيناه", box=FULL, people=["man"],
        say=[dict(who=0, text="بونس 1.200 للعائلة؟", at=1.5, bg="gold")]),
   dict(k="warn", text="ما لقيناه فحتى قانون · الألف ومية ديال الخدامة", at="الجواب: ما لقيناه", until="السؤال العاشر", y=600),
   dict(k="people", at="السؤال العاشر", until="الجواب: إيه، نفس الكونطرا", box=FULL, people=["girl", "child"],
        say=[dict(who=0, text="وأنا بيبي سيتر؟", at=1.0, bg="gold")]),
   dict(k="big", text="BS", sub="نفس الكونطرا", at="الجواب: إيه، نفس الكونطرا", until="السؤال الحادي عشر"),
   dict(k="people", at="السؤال الحادي عشر", until="الجواب: التي إف إر كيتخلص", box=FULL, people=["hijab", "man"],
        say=[dict(who=1, text="التي إف إر داخل", at=1.5, bg="red")]),
   dict(k="text", text="التي إف إر · فالنهاية", at="الجواب: التي إف إر كيتخلص", until="السؤال التاني عشر", y=560, size=90, color=GOLD),
   dict(k="map", at="السؤال التاني عشر", until="الجواب: هي جات بكونطرا", box=BIGMAP, **MED_BM),
   dict(k="people", at="الجواب: هي جات بكونطرا", until="السؤال التالت عشر", box=FULL, people=["worker", "office"],
        say=[dict(who=1, text="سولي الباترونا", at=3.0, bg="green")]),
   dict(k="people", at="السؤال التالت عشر", until="الجواب: المعلم هو اللي كيحدد", box=FULL, people=["hijab"],
        say=[dict(who=0, text="بغيت العطلة فالصيف", at=1.0, bg="gold")]),
   dict(k="calendar", at="الجواب: المعلم هو اللي كيحدد", until="وإلى عندك سؤال آخر", box=MID, day="6-9", month="الصيف", sub="هضري من بكري"),
   dict(k="people", at="وإلى عندك سؤال آخر", until=None, box=FULL, people=["woman", "man"],
        say=[dict(who=0, text="كتب فالكومونتير", at=1.0, bg="green")]),
 ]),
 # ---------------------------------------------------------------- 09
 dict(audio="I.wav", text=T["I"], chapter="09 · اللائحة النهائية", src=S_HOME, items=[
   dict(k="chapter", num="09", title="اللائحة النهائية", at=0.1, until="إلى كنتي خدامة فالدار"),
   dict(k="people", at="إلى كنتي خدامة فالدار", until="واحد: عندك ليطيرا", box=FULL, people=["hijab", "woman"],
        say=[dict(who=0, text="اللائحة ديالي", at=1.0, bg="gold")]),
   dict(k="rows", at="واحد: عندك ليطيرا", until="وإلى كنتي عائلة", y=190, gap=74, size=40, rows=[
     ("ليطيرا مسينيا", "1", "واحد: عندك ليطيرا"),
     ("التصريح فالإينبس", "2", "جوج: المعلم صرح"),
     ("المستوى الصحيح", "3", "تلاتة: المستوى"),
     ("الخلصة والسوايع", "4", "ربعة: الخلصة"),
     ("البوستا باغا", "5", "خمسة: كتاخدي"),
     ("العطلة مكتوبة", "6", "ستة: العطلة"),
     ("البيرميسو · 90 يوم", "7", "سبعة: البيرميسو"),
     ("السبعمية وتلاتين", "8", "تمنية: كل عام"),
     ("الكونطريبيوطي", "9", "تسعة: شوفي"),
   ]),
   dict(k="people", at="وإلى كنتي عائلة", until="واحد: تأكد من البيرميسو", box=FULL, people=["man", "elder"],
        say=[dict(who=0, text="وأنا المعلم", at=1.0, bg="gold")]),
   dict(k="rows", at="واحد: تأكد من البيرميسو", until="ونعاودو الأرقام المهمة", y=210, gap=100, size=42, rows=[
     ("البيرميسو ديال الخدامة", "1", "واحد: تأكد من البيرميسو"),
     ("ليطيرا بالمستوى الصحيح", "2", "جوج: كتب ليطيرا"),
     ("الإينبس قبل النهار الأول", "3", "تلاتة: صرح"),
     ("الكونطريبيوطي · يناير", "4", "ربعة: خلص"),
     ("الإيصالات للضرائب", "5", "خمسة: حتافظ"),
     ("الديكري فلوسي", "6", "ستة: وإلى باغي"),
   ]),
   dict(k="rows", at="ونعاودو الأرقام المهمة", until="والتواريخ الجايين", y=220, gap=110, size=42, rows=[
     ("سي إس ساكنة · فالشهر", "1.193,84 €", "ونعاودو الأرقام المهمة", GOLD),
     ("بي بالساعة", "7,01 €", "الكولف بي بالساعة"),
     ("السوايع · ساكنة / ما ساكناش", "54 / 40", "الماكسيموم:"),
     ("العطلة · يوم", "26", "العطلة: ستة وعشرين"),
     ("الكونطريبيوطي فالساعة", "1,24 - 2,34 €", "والكونطريبيوطي: من"),
   ]),
   dict(k="calendar", at="والتواريخ الجايين", until="وعشرة يناير آخر نهار", box=MID, day=7, month=12, sub="البريكومبيلاسيون"),
   dict(k="calendar", at="وعشرة يناير آخر نهار", until="وتمنطاش فبراير الكليك", box=MID, day=10, month=1, sub="الكونطريبيوطي"),
   dict(k="calendar", at="وتمنطاش فبراير الكليك", until="نعيمة، وسميرة، وحسن", box=MID, day=18, month=2, sub="الكليك داي"),
   dict(k="map", at="نعيمة، وسميرة، وحسن", until="ولكن القاعدة وحدة", box=BIGMAP, **IT_ALL),
   dict(k="icons", at="ولكن القاعدة وحدة", until="وإلى كان عندك شك", box=ICB, items=[
     ["file-text", "الوراق مكتوبين", "blue"], ["clock", "التصريح فالوقت", "gold"], ["calculator", "الحقوق محسوبة", "green"]], gap=1.5),
   dict(k="people", at="وإلى كان عندك شك", until="ونتي، كتخدمي فالديور", box=FULL, people=["hijab", "office"],
        say=[dict(who=1, text="سولي قبل", at=2.0, bg="green")]),
   dict(k="people", at="ونتي، كتخدمي فالديور", until="سيفي هاد الفيديو", box=FULL, people=["hijab", "man"],
        say=[dict(who=0, text="عندي الكونطرا", at=1.0, bg="green"), dict(who=1, text="باقي", at=3.5, bg="gold")]),
   dict(k="people", at="سيفي هاد الفيديو", until="ابوني فالقناة", box=FULL, people=["woman", "hijab"],
        say=[dict(who=0, text="صيفطو لصاحبتك", at=1.0, bg="gold")]),
   dict(k="cta", at="ابوني فالقناة", text="ابوني فالقناة", sub="كل نهار دليل مفيد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("خدامة فالديور ولا بادانتي؟", (236, 196, 96)), "الخلصة والحقوق 2026", "العطلة للمغرب والكونطرا"],
  num="1.193 €", numsub="الحد الأدنى · بادانتي ساكنة",
  bottom="مغاربة إيطاليا · دليل عملي بالدارجة",
)
