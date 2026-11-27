import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_J1 = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-27-f.json"), encoding="utf-8"))
_J2 = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-27-r.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo2-2026-11-27-final")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = {k: v.replace("گ", "ك") for k, v in {**_J1["blocks"], **_J2["blocks"]}.items()}

S_HOME = "مغاربة إيطاليا · دليل عملي بالدارجة"
S_REQ = "INPS scheda Assegno sociale (agg. 20/10/2026) · INPS circ. 131/2022 via Fiscoetasse · QuiFinanza 17/6/2026 · PensioniOggi"
S_IMP = "INPS · Money.it · QuiFinanza · Fiscoetasse · Fanpage · calcoli nostri"
S_DOC = "INPS msg 1997 del 15/6/2026 via QuiFinanza e Fanpage · INPS"
S_MA = "INPS · Money.it · INPS msg 3239/2017 via PensioniOggi · calcoli nostri"
S_STEP = "INPS · Fiscoetasse · Money.it · Fanpage · calcoli nostri"
S_CASI = "INPS · Fiscoetasse · Money.it · QuiFinanza"
S_QA = "Fonti dei capitoli 01-07"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850); FULL = (160, 300, 1760, 860); MID = (260, 220, 1660, 840)
ICB = (160, 330, 1760, 860); VSB = (260, 220, 1660, 820); BARB = (160, 330, 1760, 840); BIGMAP = (160, 200, 1760, 880)
DOCB = (560, 170, 1360, 880)

MED_TO = dict(view="med", hl=["ITA", "MAR"], route=["Casablanca", "Torino", "plane"], pins=["Casablanca", "Torino"], labels=False)
MED_BO = dict(view="med", hl=["ITA", "MAR"], route=["Casablanca", "Bologna", "plane"], pins=["Casablanca", "Bologna"], labels=False)
MED_BS = dict(view="med", hl=["ITA", "MAR"], route=["Casablanca", "Brescia", "plane"], pins=["Casablanca", "Brescia"], labels=False)
MED_OU = dict(view="med", hl=["ITA", "MAR"], route=["Oujda", "Milano", "plane"], pins=["Oujda", "Milano"], labels=False)
MAROC_OU = dict(view="maroc", hl=["MAR"], pins=["Oujda"], labels=False)
MAROC = dict(view="maroc", hl=["MAR"], pins=["Rabat"], labels=False)
N_TO = dict(view="north", pins=["Torino"], labels=False)
N_BO = dict(view="north", pins=["Bologna"], labels=False)
N_MI = dict(view="north", pins=["Milano"], labels=False)
N_BS = dict(view="north", pins=["Brescia"], labels=False)
IT_ALL = dict(view="italy", pins=["Torino", "Bologna", "Brescia"], labels=False)
IT_RM = dict(view="italy", pins=["Roma"], labels=False)

DOC_ROWS = ["STATO CIVILE", "PERMESSO", "INIZIO SOGGIORNO", "ASSENZE", "REDDITI", "DICHIARAZIONI"]
def DOC(focus, tag, at, until):
    return dict(k="doc", at=at, until=until, box=DOCB, title="DOMANDA ASSEGNO SOCIALE", rows=DOC_ROWS,
                focus=focus, tag=tag, done=list(range(focus)), warn=[], doc_at=0.4)

BLOCKS = [
 # ---------------------------------------------------------------- 01
 dict(audio="A.wav", text=T["A"], chapter="01 · شكون خاصو هاد الدليل", src=S_HOME, items=[
   dict(k="head", text="الأسينيو سوسيالي ديال الإينبس", at=0.2, until="واش باباك ولا ماماك", sub="فلوس كل شهر من 67 عام"),
   dict(k="people", at="واش باباك ولا ماماك", until="خاصنا نبداو بحاجة مهمة", box=FULL, people=["elder", "woman"],
        say=[dict(who=0, text="ما عنديش بانسيون", at=1.0, bg="gold"), dict(who=1, text="شكون عندو الحق؟", at=5.0, bg="green")]),
   dict(k="vs", at="خاصنا نبداو بحاجة مهمة", until="وعندها شروط واضحة", box=VSB,
        right=dict(title="البانسيون ديال الخدمة", value="الكونطريبيوطي", sub="على حساب الخدمة", icon="briefcase", color="grey"),
        left=dict(title="الأسينيو سوسيالي", value="مساعدة", sub="للي محتاج", icon="heart", color="green"), gap=2.0),
   dict(k="icons", at="وعندها شروط واضحة", until="وفهاد الدليل غادي نجاوبو", box=ICB, items=[
     ["calendar", "العمر", "gold"], ["home", "السكنى", "blue"], ["id", "الكارطا", "green"], ["wallet", "الدخل", "blue"]], gap=1.0, cols=4),
   dict(k="steps", at="وفهاد الدليل غادي نجاوبو", until="ومن بعد، غادي نشوفو", box=MID, steps=[
     ["شكون عندو الحق", "1"], ["الكارطا والعشر سنين", "2"], ["شحال كتشد", "3"], ["الطلب والخلاص", "4"]], gap=2.5, check_after=0.6),
   dict(k="map", at="ومن بعد، غادي نشوفو", until="وعلاش هاد الموضوع مهم", box=BIGMAP, **MED_TO),
   dict(k="people", at="وعلاش هاد الموضوع مهم", until="وعندنا ربعة ديال الحالات", box=FULL, people=["worker", "hijab", "elder"],
        say=[dict(who=0, text="خدمت بلا كونطرا", at=4.0, bg="red"), dict(who=1, text="بقيت مع الولاد", at=7.0, bg="gold")]),
   dict(k="text", text="ربعة ديال الحالات", at="وعندنا ربعة ديال الحالات", until="الحالة الأولى، الحاج محمد", y=520, size=96, color=GOLD),
   dict(k="map", at="الحالة الأولى، الحاج محمد", until="الحالة التانية، فاطنة", box=L_BOX, **N_TO),
   dict(k="people", at="الحالة الأولى، الحاج محمد", until="الحالة التانية، فاطنة", box=R_BOX, people=["elder"],
        say=[dict(who=0, text="الحاج محمد · تورينو", at=0.8, bg="gold")]),
   dict(k="map", at="الحالة التانية، فاطنة", until="الحالة التالتة، عبد القادر", box=L_BOX, **N_BO),
   dict(k="people", at="الحالة التانية، فاطنة", until="الحالة التالتة، عبد القادر", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="فاطنة · بولونيا", at=0.8, bg="gold")]),
   dict(k="map", at="الحالة التالتة، عبد القادر", until="والحالة الرابعة، لحسن", box=L_BOX, **N_MI),
   dict(k="people", at="الحالة التالتة، عبد القادر", until="والحالة الرابعة، لحسن", box=R_BOX, people=["elder", "woman"],
        say=[dict(who=0, text="عبد القادر وزهرة", at=0.8, bg="gold")]),
   dict(k="map", at="والحالة الرابعة، لحسن", until="فهاد الدليل غادي نمشيو", box=BIGMAP, **MED_BS),
   dict(k="rows", at="فهاد الدليل غادي نمشيو", until="وكل معلومة فهاد الفيديو", y=215, gap=78, size=40, rows=[
     ("شكون خاصو هاد الدليل", "01", "الأول، شكون"),
     ("الشروط", "02", "التاني، الشروط"),
     ("شحال وكيفاش كيتحسب", "03", "التالت، شحال"),
     ("الوراق والطلب الجديد", "04", "الرابع، الوراق"),
     ("المغرب", "05", "الخامس، الجانب"),
     ("الخطوات والتواريخ", "06", "السادس، الخطوات"),
     ("الحالات والأخطاء", "07", "السابع، الحالات"),
     ("سؤال وجواب", "08", "التامن، سؤال"),
     ("اللائحة النهائية", "09", "والتاسع، لائحة"),
   ]),
   dict(k="icons", at="وكل معلومة فهاد الفيديو", until="وعقل مزيان", box=ICB, items=[
     ["building-bank", "الإينبس", "blue"], ["file-text", "مواقع متخصصة", "gold"], ["clipboard-check", "جوج مصادر", "green"]], gap=1.5),
   dict(k="warn", text="محتوى إخباري · ماشي استشارة", at="وعقل مزيان", until="وحاجة أخيرة قبل ما نبداو", y=600),
   dict(k="people", at="وحاجة أخيرة قبل ما نبداو", until=None, box=FULL, people=["woman", "elder"],
        say=[dict(who=0, text="كتب سؤالك", at=1.0, bg="green"), dict(who=1, text="سيفي الفيديو", at=4.5, bg="gold")]),
 ]),
 # ---------------------------------------------------------------- 02
 dict(audio="B.wav", text=T["B"], chapter="02 · الشروط", src=S_REQ, items=[
   dict(k="chapter", num="02", title="الشروط بالتفصيل", at=0.1, until="الشرط الأول: العمر"),
   dict(k="big", text="67", sub="عام · نهار الطلب", at="الشرط الأول: العمر", until="ومن العام الجاي"),
   dict(k="vs", at="ومن العام الجاي", until="الشرط التاني: البيرميسو", box=VSB,
        right=dict(title="البانسيون العادية", value="شهر زايد", sub="2027", icon="calendar", color="gold"),
        left=dict(title="الأسينيو سوسيالي", value="سول", sub="الباترونا", icon="building-bank", color="blue"), gap=4.0),
   dict(k="people", at="الشرط التاني: البيرميسو", until="المغربي، ولا أي واحد", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="البيرميسو ديال الخدمة؟", at=0.6, bg="gold")]),
   dict(k="vs", at="المغربي، ولا أي واحد", until="وكاينين حتى اللاجئين", box=VSB,
        right=dict(title="الخدمة · العائلة", value="لا", sub="ما كيكفيش", icon="x", color="red"),
        left=dict(title="الكارطا", value="إيه", sub="المدة الطويلة", icon="id", color="green"), gap=3.0),
   dict(k="icons", at="وكاينين حتى اللاجئين", until="الشرط التالت: عشر سنين", box=ICB, items=[
     ["id", "الكارطا", "green"], ["world", "اللاجئين والحماية", "blue"], ["users", "عائلة مواطن أوروبي", "gold"]], gap=2.0),
   dict(k="big", text="10", sub="سنين قانونية · بلا انقطاع", at="الشرط التالت: عشر سنين", until="الإينبس كيقسم"),
   dict(k="vs", at="الإينبس كيقسم", until="مثال: الحاج محمد مشا", box=VSB,
        right=dict(title="الخمس سنين الأولى", value="5", sub="أقل من 6 شهور متابعين", icon="calendar", color="green"),
        left=dict(title="الخمس سنين التانية", value="5", sub="ماشي أكثر من 10 شهور", icon="calendar", color="green"), gap=2.0),
   dict(k="map", at="مثال: الحاج محمد مشا", until="ولكن كاينين استثناءات", box=L_BOX, **MED_TO),
   dict(k="people", at="مثال: الحاج محمد مشا", until="ولكن كاينين استثناءات", box=R_BOX, people=["elder"],
        say=[dict(who=0, text="7 شهور فالمغرب", at=1.5, bg="red")]),
   dict(k="icons", at="ولكن كاينين استثناءات", until="إلى كان عندك غياب طويل، جمع", box=ICB, items=[
     ["stethoscope", "الصحة", "red"], ["heart", "الحمل والولادة", "green"], ["school", "التكوين", "blue"], ["briefcase", "الخدمة فبرا", "gold"]], gap=1.2, cols=4),
   dict(k="warn", text="غياب طويل؟ جمع الوراق وسول الباترونا", at="إلى كان عندك غياب طويل، جمع", until="ومثال آخر: فاطنة", y=560),
   dict(k="map", at="ومثال آخر: فاطنة", until="الشرط الرابع: السكنى", box=L_BOX, **N_BO),
   dict(k="people", at="ومثال آخر: فاطنة", until="الشرط الرابع: السكنى", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="من 2010 هنا", at=1.0, bg="green"), dict(who=0, text="ما فاتش شهرين", at=5.0, bg="gold")]),
   dict(k="vs", at="الشرط الرابع: السكنى", until="الشرط الخامس: الدخل", box=VSB,
        right=dict(title="مسجل · عايش فالمغرب", value="لا", sub="", icon="plane", color="red"),
        left=dict(title="ساكن فإيطاليا بصح", value="إيه", sub="كل عام كيتراقب", icon="home", color="green"), gap=2.0),
   dict(k="bars", at="الشرط الخامس: الدخل", until="إذن عاود معايا", box=BARB, bars=[
     ["بوحدك", 7101.12, "7.101,12 €", "gold"], ["مزوجين", 14202.24, "14.202,24 €", "green"]], gap=5.0),
   dict(k="text", text="الحد ديال الدخل فالعام", at="الشرط الخامس: الدخل", until="إذن عاود معايا", y=880, size=44, color=GREY),
   dict(k="steps", at="إذن عاود معايا", until="وإلى كان عندك البيرميسو ديال الخدمة وعندك", box=MID, steps=[
     ["67 عام", "1"], ["الكارطا", "2"], ["10 سنين", "3"], ["ساكن هنا", "4"], ["الدخل تحت الحد", "5"]], gap=1.3, check_after=0.5),
   dict(k="people", at="وإلى كان عندك البيرميسو ديال الخدمة وعندك", until=None, box=FULL, people=["worker", "office"],
        say=[dict(who=1, text="طلب الكارطا أولا", at=1.0, bg="green")]),
 ]),
 # ---------------------------------------------------------------- 03
 dict(audio="C.wav", text=T["C"], chapter="03 · شحال كتشد", src=S_IMP, items=[
   dict(k="chapter", num="03", title="شحال كتشد", at=0.1, until="الأسينيو سوسيالي الكامل هو"),
   dict(k="big", text="546,24 €", sub="فالشهر · 2026", at="الأسينيو سوسيالي الكامل هو", until="وكيتخلص تلطاش"),
   dict(k="calendar", at="وكيتخلص تلطاش", until="والمجموع فالعام", box=MID, day=13, month="خلاص", sub="فالعام · كاين خلاص زايد فدجنبر"),
   dict(k="big", text="7.101,12 €", sub="المجموع فالعام", at="والمجموع فالعام", until="لاحظ حاجة"),
   dict(k="vs", at="لاحظ حاجة", until="إذن الحساب ساهل", box=VSB,
        right=dict(title="الحد ديال الدخل", value="7.101,12 €", sub="للي بوحدو", icon="wallet", color="gold"),
        left=dict(title="الأسينيو فالعام", value="7.101,12 €", sub="نفس الرقم", icon="coin-euro", color="green"), gap=3.0),
   dict(k="steps", at="إذن الحساب ساهل", until="نشوفو الحالات ديالنا", box=MID, steps=[
     ["الحد ناقص الدخل", "1"], ["الباقي على 13", "2"], ["المبلغ ديال الشهر", "3"]], gap=3.0, check_after=0.6),
   dict(k="map", at="نشوفو الحالات ديالنا", until="فاطنة فبولونيا: عندها", box=L_BOX, **N_TO),
   dict(k="people", at="نشوفو الحالات ديالنا", until="فاطنة فبولونيا: عندها", box=R_BOX, people=["elder"],
        say=[dict(who=0, text="بلا دخل", at=2.5, bg="gold"), dict(who=0, text="546,24 €", at=6.5, bg="green")]),
   dict(k="map", at="فاطنة فبولونيا: عندها", until="نحسبو: سبع آلاف", box=BIGMAP, **MED_BO),
   dict(k="rows", at="نحسبو: سبع آلاف", until="ومثال آخر بالأرقام", y=300, gap=125, size=46, rows=[
     ("الحد", "7.101,12 €", "نحسبو: سبع آلاف"),
     ("البانسيون المغربية", "1.200 €", "ناقص ألف وميتين", RED),
     ("الباقي فالعام", "5.901,12 €", "كيبقى خمس آلاف وتسع"),
     ("فالشهر · على 13", "453,93 €", "نقسموها على تلطاش", GOLD),
   ]),
   dict(k="map", at="عبد القادر وزهرة فميلانو: مزوجين", until="الحد ديال المزوجين هو", box=L_BOX, **N_MI),
   dict(k="people", at="عبد القادر وزهرة فميلانو: مزوجين", until="الحد ديال المزوجين هو", box=R_BOX, people=["elder", "woman"],
        say=[dict(who=1, text="9.000 € بجوج", at=2.0, bg="gold")]),
   dict(k="rows", at="الحد ديال المزوجين هو", until="ولو كان الدخل ديالهم صغير", y=300, gap=125, size=46, rows=[
     ("الحد ديال المزوجين", "14.202,24 €", "الحد ديال المزوجين هو"),
     ("الدخل بجوج", "9.000 €", "نحيدو تسع آلاف", RED),
     ("الباقي فالعام", "5.202,24 €", "كيبقى خمس آلاف وميتين"),
     ("فالشهر · على 13", "400,17 €", "على تلطاش: تقريبا ربع مية", GOLD),
   ]),
   dict(k="warn", text="ماشي أكثر من المبلغ الكامل", at="ولو كان الدخل ديالهم صغير", until="دابا، شنو اللي كيتحسب", y=560),
   dict(k="bars", at="ومثال آخر بالأرقام", until="عبد القادر وزهرة فميلانو: مزوجين", box=BARB, bars=[
     ["بلا دخل", 546.24, "546 €", "green"], ["1.200 فالعام", 453.93, "454 €", "gold"], ["3.000 فالعام", 315.47, "315 €", "blue"]], gap=2.0),
   dict(k="text", text="الأسينيو فالشهر على حساب الدخل", at="ومثال آخر بالأرقام", until="عبد القادر وزهرة فميلانو: مزوجين", y=880, size=44, color=GREY),
   dict(k="icons", at="دابا، شنو اللي كيتحسب", until="وشنو اللي ما كيتحسبش", box=ICB, items=[
     ["briefcase", "الخدمة والبانسيون", "blue"], ["building-bank", "الفوائد", "gold"], ["home-dollar", "الكرا", "gold"], ["world", "بانسيون دولة أخرى", "red"]], gap=1.6, cols=4),
   dict(k="icons", at="وشنو اللي ما كيتحسبش", until="وكاين حتى زيادة", box=ICB, items=[
     ["home", "الدار اللي ساكن فيها", "green"], ["pig-money", "التيإفير", "green"], ["receipt", "فلوس قديمة", "green"]], gap=1.5),
   dict(k="people", at="وكاين حتى زيادة", until="وحاجة مهمة بزاف", box=FULL, people=["elder", "office"],
        say=[dict(who=0, text="فاتو 70 عام", at=0.8, bg="gold"), dict(who=1, text="نحسبوها معاك", at=5.0, bg="green")]),
   dict(k="vs", at="وحاجة مهمة بزاف", until="وخلاصة هاد الفصل", box=VSB,
        right=dict(title="للورثة", value="لا", sub="", icon="users", color="red"),
        left=dict(title="برا إيطاليا", value="لا", sub="", icon="plane", color="red"), gap=4.0),
   dict(k="text", text="كل واحد على حساب الدخل ديالو", at="وخلاصة هاد الفصل", until=None, y=560, size=80, color=GOLD),
 ]),
 # ---------------------------------------------------------------- 04
 dict(audio="D.wav", text=T["D"], chapter="04 · الوراق والطلب الجديد", src=S_DOC, items=[
   dict(k="chapter", num="04", title="الوراق والطلب", at=0.1, until="أولا، الهوية الرقمية"),
   dict(k="icons", at="أولا، الهوية الرقمية", until="تانيا، الكود فيسكال", box=ICB, items=[
     ["key", "السبيد", "green"], ["id", "الكارطا الإلكترونية", "blue"], ["credit-card", "كارطا الخدمات", "gold"]], gap=1.5),
   dict(k="icons", at="تانيا، الكود فيسكال", until="تالتا، الدخل", box=ICB, items=[
     ["file-text", "الكود فيسكال", "blue"], ["id", "الكارطا", "green"], ["home", "الريزيدينسا", "gold"]], gap=1.2),
   dict(k="icons", at="تالتا، الدخل", until="والبانسيون اللي جاية من المغرب، جيب", box=ICB, items=[
     ["receipt", "السي يو", "blue"], ["report-money", "التصريح ديال الضرائب", "gold"], ["users", "الزوج ولا الزوجة", "green"]], gap=1.8),
   dict(k="map", at="والبانسيون اللي جاية من المغرب، جيب", until="رابعا، الإيبان", box=BIGMAP, **MED_BO),
   dict(k="big", text="IBAN", sub="الكونطو ديالك", at="رابعا، الإيبان", until="وخامسا، إلى كنتي غبتي"),
   dict(k="icons", at="وخامسا، إلى كنتي غبتي", until="ودابا الخبر الجديد", box=ICB, items=[
     ["stethoscope", "شهادة طبية", "red"], ["briefcase", "ورقة الخدمة", "blue"], ["school", "التكوين", "gold"]], gap=1.5),
   dict(k="big", text="1997", sub="رسالة الإينبس · 15/6/2026", at="ودابا الخبر الجديد", until="الهدف هو يجمع"),
   dict(k="people", at="الهدف هو يجمع", until="خلينا نقراو هاد الطلب", box=FULL, people=["clerk", "elder"],
        say=[dict(who=0, text="كلشي من الأول", at=1.0, bg="green")]),
   DOC(0, "01 · STATO CIVILE", "خلينا نقراو هاد الطلب", "الخانة التانية: البيرميسو"),
   DOC(1, "02 · PERMESSO", "الخانة التانية: البيرميسو", "الخانة التالتة: البداية"),
   DOC(2, "03 · INIZIO SOGGIORNO", "الخانة التالتة: البداية", "الخانة الرابعة: الغياب"),
   DOC(3, "04 · ASSENZE", "الخانة الرابعة: الغياب", "الخانة الخامسة: الدخل"),
   DOC(4, "05 · REDDITI", "الخانة الخامسة: الدخل", "والخانة السادسة: التصريحات"),
   DOC(5, "06 · DICHIARAZIONI", "والخانة السادسة: التصريحات", "وعقل: هاد التصريحات"),
   dict(k="warn", text="التصريح الكاذب: عقوبات ورجوع الفلوس", at="وعقل: هاد التصريحات", until="ونصيحة عملية", y=560),
   dict(k="people", at="ونصيحة عملية", until="وإلى ما عندكش السبيد", box=FULL, people=["elder", "girl"],
        say=[dict(who=1, text="التواريخ ديال السفرات", at=3.0, bg="gold")]),
   dict(k="map", at="وإلى ما عندكش السبيد", until="وإلى الطلب ديالك ناقص", box=L_BOX, **N_TO),
   dict(k="people", at="وإلى ما عندكش السبيد", until="وإلى الطلب ديالك ناقص", box=R_BOX, people=["office"],
        say=[dict(who=0, text="الوراق عليك", at=3.0, bg="gold")]),
   dict(k="icons", at="وإلى الطلب ديالك ناقص", until="وإلى بغيتي تسول", box=ICB, items=[
     ["mailbox", "البوسطا", "gold"], ["world", "السيت", "blue"], ["clock", "المدة محدودة", "red"]], gap=1.5),
   dict(k="people", at="وإلى بغيتي تسول", until=None, box=FULL, people=["elder", "clerk"],
        say=[dict(who=0, text="فين وصل الملف؟", at=1.0, bg="gold"), dict(who=1, text="الرقم ديال الطلب", at=6.0, bg="green")]),
 ]),
 # ---------------------------------------------------------------- 05
 dict(audio="E.wav", text=T["E"], chapter="05 · الجانب المغربي", src=S_MA, items=[
   dict(k="chapter", num="05", title="الجانب المغربي", at=0.1, until="السؤال الأول: البانسيون"),
   dict(k="map", at="السؤال الأول: البانسيون", until="الجواب: إيه", box=BIGMAP, **MED_BO),
   dict(k="vs", at="الجواب: إيه", until="السؤال التاني: الدار", box=VSB,
        right=dict(title="بلا بانسيون", value="546 €", sub="فالشهر", icon="coin-euro", color="green"),
        left=dict(title="فاطنة · بانسيون المغرب", value="454 €", sub="فالشهر · تقريبا", icon="world", color="gold"), gap=4.0),
   dict(k="vs", at="السؤال التاني: الدار", until="مثال من عندنا: دار فوجدة", box=VSB,
        right=dict(title="الدار اللي ساكن فيها", value="ما كتحسبش", sub="", icon="home", color="green"),
        left=dict(title="دار كتكريها", value="الكرا كيتحسب", sub="صرح بيه", icon="home-dollar", color="red"), gap=4.0),
   dict(k="map", at="مثال من عندنا: دار فوجدة", until="بصرف تقريبي", box=BIGMAP, **MAROC_OU),
   dict(k="rows", at="بصرف تقريبي", until="والتصريح ديال الكرا ماشي", y=300, gap=130, size=48, rows=[
     ("الكرا فالعام", "36.000 DH", "بصرف تقريبي"),
     ("بالأورو · تقريبا", "3.300 €", "كتجي تقريبا تلت آلاف"),
     ("الأسينيو فالشهر", "292 €", "كيبقى ليك تقريبا ميتين", GOLD),
   ]),
   dict(k="warn", text="الكرا ديال المغرب خاصو يتصرح", at="والتصريح ديال الكرا ماشي", until="السؤال التالت، وهو الأهم", y=560),
   dict(k="big", text="29", sub="يوم متابعين برا إيطاليا", at="السؤال التالت، وهو الأهم", until="وإلى فات عام كامل"),
   dict(k="steps", at="وإلى فات عام كامل", until="مثال: الحاج محمد سافر", box=MID, steps=[
     ["أكثر من 29 يوم", "التوقيف"], ["عام فالتوقيف", "الحذف"]], gap=1.0, bad=True, check_after=0.5),
   dict(k="map", at="مثال: الحاج محمد سافر", until="هادي خمسة وأربعين يوم", box=BIGMAP, **MED_TO),
   dict(k="vs", at="هادي خمسة وأربعين يوم", until="والحاج محمد قرر", box=VSB,
        right=dict(title="رجع 15 غشت", value="45 يوم", sub="الخلاص كيتوقف", icon="x", color="red"),
        left=dict(title="رجع 25 يوليوز", value="24 يوم", sub="ما كاين مشكل", icon="check", color="green"), gap=5.0),
   dict(k="calendar", at="إذن إلى بغيتي تقضي", until="وإلى كان عندك سبب صحي", box=MID, day=29, month="يوم", sub="الحد ديال كل سفرة"),
   dict(k="people", at="والحاج محمد قرر", until="إذن إلى بغيتي تقضي", box=FULL, people=["elder", "woman"],
        say=[dict(who=0, text="3 سيمانات · يوليوز", at=2.0, bg="gold"), dict(who=0, text="3 سيمانات · شتنبر", at=6.0, bg="green")]),
   dict(k="icons", at="وإلى كان عندك سبب صحي", until="وعقل على حاجة أخرى", box=ICB, items=[
     ["stethoscope", "الشهادات الطبية", "red"], ["mail", "علم الإينبس", "blue"], ["building-bank", "الباترونا", "gold"]], gap=1.8),
   dict(k="warn", text="الغياب الطويل يقدر يقطع العشر سنين", at="وعقل على حاجة أخرى", until="السؤال الرابع: الواليدين", y=560),
   dict(k="map", at="السؤال الرابع: الواليدين", until="والحالة ديال لحسن", box=BIGMAP, **MED_BS),
   dict(k="people", at="والحالة ديال لحسن", until="إذن العشر سنين ديالو", box=FULL, people=["elder", "man"],
        say=[dict(who=0, text="جيت عام 2020", at=1.0, bg="gold")]),
   dict(k="big", text="2030", sub="لحسن · العشر سنين", at="إذن العشر سنين ديالو", until="وفهاد الوقت، العائلة"),
   dict(k="people", at="وفهاد الوقت، العائلة", until=None, box=FULL, people=["man", "elder", "hijab"],
        say=[dict(who=0, text="العائلة كتعاون", at=1.0, bg="green")]),
 ]),
 # ---------------------------------------------------------------- 06
 dict(audio="F.wav", text=T["F"], chapter="06 · الخطوات والتواريخ", src=S_STEP, items=[
   dict(k="chapter", num="06", title="الخطوات والتواريخ", at=0.1, until="الخطوة الأولى: تأكد"),
   dict(k="steps", at="الخطوة الأولى: تأكد", until="الخطوة التانية: دير الطلب", box=MID, steps=[
     ["العمر", "1"], ["الكارطا", "2"], ["10 سنين", "3"], ["الدخل", "4"]], gap=1.3, check_after=0.5),
   dict(k="icons", at="الخطوة التانية: دير الطلب", until="والأرقام كتبان فالشاشة", box=ICB, items=[
     ["world", "السيت ديال الإينبس", "blue"], ["phone", "الكونطاكت سونطر", "gold"], ["building-bank", "الباترونا", "green"]], gap=3.0),
   dict(k="big", text="803 164", sub="من الثابت · 06 164 164 من البورطابل", at="والأرقام كتبان فالشاشة", until="والطريقة التالتة: الباترونا", size=180),
   dict(k="people", at="والطريقة التالتة: الباترونا", until="الخطوة التالتة: الجواب", box=FULL, people=["office", "elder"],
        say=[dict(who=1, text="عندي دخل من المغرب", at=1.5, bg="gold"), dict(who=0, text="نعمرو كلشي مزيان", at=5.5, bg="green")]),
   dict(k="big", text="45", sub="يوم باش يجاوب الإينبس", at="الخطوة التالتة: الجواب", until="وفهاد المدة، ما تبقاش"),
   dict(k="icons", at="وفهاد المدة، ما تبقاش", until="الخطوة الرابعة: الخلاص", box=ICB, items=[
     ["world", "السيت · مرة فالسيمانة", "blue"], ["mailbox", "البوسطا", "gold"], ["building-bank", "الباترونا", "green"]], gap=3.0),
   dict(k="vs", at="الخطوة الرابعة: الخلاص", until="مثال بالتواريخ", box=VSB,
        right=dict(title="من نهار كملتي العمر", value="لا", sub="", icon="x", color="red"),
        left=dict(title="من الشهر اللي من بعد", value="إيه", sub="ما تعطلش الطلب", icon="calendar", color="green"), gap=2.5),
   dict(k="map", at="مثال بالتواريخ", until="ولو كانت دارت الطلب", box=L_BOX, **N_BO),
   dict(k="calendar", at="مثال بالتواريخ", until="ودارت الطلب غير", box=R_BOX, day=10, month=9, sub="كملت 67 عام"),
   dict(k="calendar", at="ودارت الطلب غير", until="الإينبس عندو حتى", box=R_BOX, day=1, month=12, sub="دارت الطلب"),
   dict(k="calendar", at="الإينبس عندو حتى", until="ولو كانت دارت الطلب", box=R_BOX, day=15, month=1, sub="آخر أجل للجواب · 2027"),
   dict(k="big", text="1.300 €", sub="ضاعو بالتعطال · تقريبا", at="ولو كانت دارت الطلب", until="الخطوة الخامسة", color=RED),
   dict(k="icons", at="الخطوة الخامسة", until="الخطوة السادسة", box=ICB, items=[
     ["report-money", "الريد · الدخل", "gold"], ["home", "السكنى فإيطاليا", "green"], ["clipboard-check", "إجباري", "red"]], gap=2.5),
   dict(k="icons", at="الخطوة السادسة", until="ودابا خلينا نشوفو", box=ICB, items=[
     ["trending-up", "الدخل", "gold"], ["heart", "الزواج", "green"], ["plane", "السفر", "red"], ["building-hospital", "مؤسسة صحية", "blue"]], gap=1.2, cols=4),
   dict(k="steps", at="ودابا خلينا نشوفو", until="ونصيحة: حط", box=MID, steps=[
     ["يناير · الخلاص", "1"], ["الربيع · التصريحات", "2"], ["الصيف · 29 يوم", "3"], ["دجنبر · الخلاص الزايد", "4"]], gap=2.8),
   dict(k="people", at="ونصيحة: حط", until="وإلى ما فهمتيش", box=FULL, people=["elder", "girl"],
        say=[dict(who=1, text="تذكير فالتيليفون", at=1.0, bg="green"), dict(who=0, text="نسخة من كل ورقة", at=6.0, bg="gold")]),
   dict(k="people", at="وإلى ما فهمتيش", until=None, box=FULL, people=["elder", "office"],
        say=[dict(who=0, text="رسالة ما فهمتهاش", at=1.0, bg="red"), dict(who=1, text="جيبها هاد السيمانة", at=4.5, bg="green")]),
 ]),
 # ---------------------------------------------------------------- 07
 dict(audio="G.wav", text=T["G"], chapter="07 · الحالات والأخطاء", src=S_CASI, items=[
   dict(k="chapter", num="07", title="الحالات والأخطاء", at=0.1, until="الحالة الأولى: المزوجين"),
   dict(k="map", at="الحالة الأولى: المزوجين", until="الحالة التانية: اللي كيخدم", box=L_BOX, **N_MI),
   dict(k="people", at="الحالة الأولى: المزوجين", until="الحالة التانية: اللي كيخدم", box=R_BOX, people=["elder", "woman"],
        say=[dict(who=1, text="دخل جديد؟ علم الإينبس", at=4.0, bg="gold")]),
   dict(k="people", at="الحالة التانية: اللي كيخدم", until="الحالة التالتة: اللي عندو", box=FULL, people=["worker"],
        say=[dict(who=0, text="الأجرة كتحسب", at=3.0, bg="gold"), dict(who=0, text="التصريح واجب", at=8.0, bg="green")]),
   dict(k="people", at="الحالة التالتة: اللي عندو", until="الحالة الرابعة: اللي دخل", box=FULL, people=["elder", "office"],
        say=[dict(who=0, text="بانسيون صغيرة", at=1.0, bg="gold"), dict(who=1, text="نحسبوها معاك", at=6.0, bg="green")]),
   dict(k="vs", at="الحالة الرابعة: اللي دخل", until="الحالة الخامسة: اللي دخل", box=VSB,
        right=dict(title="بلا بيرميسو", value="ما كتحسبش", sub="", icon="x", color="red"),
        left=dict(title="بالبيرميسو", value="كتحسب", sub="العشر سنين", icon="id", color="green"), gap=4.0),
   dict(k="map", at="الحالة الخامسة: اللي دخل", until="ودابا الأخطاء", box=L_BOX, **N_BS),
   dict(k="people", at="الحالة الخامسة: اللي دخل", until="ودابا الأخطاء", box=R_BOX, people=["elder", "girl"],
        say=[dict(who=1, text="علم الإينبس", at=4.0, bg="gold")]),
   dict(k="big", text="10", sub="أخطاء كيضيعو الفلوس", at="ودابا الأخطاء", until="الغلط الأول", color=RED),
   dict(k="steps", at="الغلط الأول", until="الغلط السادس", box=MID, steps=[
     ["البيرميسو ديال الخدمة", "1"], ["10 سنين بلا بيرميسو", "2"], ["غياب بلا ورقة", "3"], ["البانسيون المغربية", "4"], ["الكرا ديال المغرب", "5"]],
        gap=3.5, bad=True, check_after=0.4),
   dict(k="steps", at="الغلط السادس", until="وشنو دير إلى ترفض", box=MID, steps=[
     ["سفر أكثر من 29 يوم", "6"], ["التصريح ديال كل عام", "7"], ["تعطيل الطلب", "8"], ["وسيط بالفلوس", "9"], ["الرسائل ديال الإينبس", "10"]],
        gap=4.0, bad=True, check_after=0.4),
   dict(k="steps", at="وشنو دير إلى ترفض", until="وإلى الإينبس طلب منك", box=MID, steps=[
     ["اقرا السبب", "1"], ["صحح ودير طلب جديد", "2"], ["الطعن مع الباترونا", "3"]], gap=4.0, check_after=0.6),
   dict(k="people", at="وإلى الإينبس طلب منك", until="وتذكر: الأسينيو", box=FULL, people=["elder", "office"],
        say=[dict(who=0, text="بالأقساط؟", at=4.0, bg="gold")]),
   dict(k="text", text="حق · بالصدق والسكنى الحقيقية", at="وتذكر: الأسينيو", until=None, y=560, size=84, color=GOLD),
 ]),
 # ---------------------------------------------------------------- 08
 dict(audio="H.wav", text=T["H"], chapter="08 · سؤال وجواب", src=S_QA, items=[
   dict(k="chapter", num="08", title="سؤال وجواب", at=0.1, until="السؤال الأول: عندي"),
   dict(k="people", at="السؤال الأول: عندي", until="الجواب: لا. خاصك الكارطا", box=FULL, people=["worker"],
        say=[dict(who=0, text="بيرميسو ديال الخدمة؟", at=1.0, bg="gold")]),
   dict(k="vs", at="الجواب: لا. خاصك الكارطا", until="السؤال التاني: نقدر", box=VSB,
        right=dict(title="الخدمة · جوج سنين", value="لا", sub="", icon="x", color="red"),
        left=dict(title="الكارطا", value="إيه", sub="", icon="id", color="green"), gap=1.5),
   dict(k="people", at="السؤال التاني: نقدر", until="الجواب: لا. الأسينيو ما كيتخلصش", box=FULL, people=["elder"],
        say=[dict(who=0, text="نعيش فالمغرب؟", at=1.0, bg="gold")]),
   dict(k="map", at="الجواب: لا. الأسينيو ما كيتخلصش", until="السؤال التالت: سافرت", box=BIGMAP, **MED_TO),
   dict(k="people", at="السؤال التالت: سافرت", until="الجواب: القاعدة", box=FULL, people=["hijab"],
        say=[dict(who=0, text="20 يوم · جوج مرات", at=2.0, bg="gold")]),
   dict(k="bars", at="الجواب: القاعدة", until="السؤال الرابع: الدار", box=BARB, bars=[
     ["السفرة 1", 20, "20 يوم", "green"], ["السفرة 2", 20, "20 يوم", "green"], ["الحد", 29, "29 يوم", "gold"]], gap=1.0),
   dict(k="people", at="السؤال الرابع: الدار", until="الجواب: لا. الدار", box=FULL, people=["man"],
        say=[dict(who=0, text="الدار ديالي فإيطاليا؟", at=1.5, bg="gold")]),
   dict(k="big", text="0", sub="الدار اللي ساكن فيها ما كتحسبش", at="الجواب: لا. الدار", until="السؤال الخامس", color=GREEN),
   dict(k="people", at="السؤال الخامس", until="الجواب: لا. التيإفير", box=FULL, people=["worker"],
        say=[dict(who=0, text="التيإفير كيتحسب؟", at=1.5, bg="gold")]),
   dict(k="icons", at="الجواب: لا. التيإفير", until="السؤال السادس", box=ICB, items=[["pig-money", "التيإفير · ما كيتحسبش", "green"]], gap=1.0),
   dict(k="people", at="السؤال السادس", until="الجواب: لا. الأسينيو سوسيالي ما", box=FULL, people=["elder", "hijab"],
        say=[dict(who=0, text="المرا من بعدي؟", at=1.5, bg="gold")]),
   dict(k="warn", text="ما كيمشيش للورثة · كل واحد بالشروط ديالو", at="الجواب: لا. الأسينيو سوسيالي ما", until="السؤال السابع", y=560),
   dict(k="people", at="السؤال السابع", until="الجواب: لا. خاصك تكون", box=FULL, people=["man"],
        say=[dict(who=0, text="قبل 67 عام؟", at=1.5, bg="gold")]),
   dict(k="big", text="67", sub="نهار الطلب · حضر الوراق من قبل", at="الجواب: لا. خاصك تكون", until="السؤال التامن"),
   dict(k="people", at="السؤال التامن", until="الجواب: جمع البيرميسوات", box=FULL, people=["girl"],
        say=[dict(who=0, text="العشر سنين كاملين؟", at=1.5, bg="gold")]),
   dict(k="icons", at="الجواب: جمع البيرميسوات", until="السؤال التاسع", box=ICB, items=[
     ["id", "البيرميسوات القدام", "blue"], ["home", "الريزيدينسا", "gold"], ["plane", "تواريخ السفرات", "red"]], gap=2.0),
   dict(k="map", at="السؤال التاسع", until="الجواب: كيتحسب الدخل ديالكم", box=L_BOX, **N_MI),
   dict(k="people", at="السؤال التاسع", until="الجواب: كيتحسب الدخل ديالكم", box=R_BOX, people=["elder", "woman"],
        say=[dict(who=0, text="أنا ما عندي والو", at=3.0, bg="gold")]),
   dict(k="big", text="14.202,24 €", sub="الحد ديال جوج فالعام", at="الجواب: كيتحسب الدخل ديالكم", until="السؤال العاشر"),
   dict(k="people", at="السؤال العاشر", until="الجواب: إيه، كيتزاد", box=FULL, people=["elder"],
        say=[dict(who=0, text="كيتبدل كل عام؟", at=1.5, bg="gold")]),
   dict(k="bars", at="الجواب: إيه، كيتزاد", until="السؤال الحادش", box=BARB, bars=[
     ["2025", 538.69, "538,69 €", "grey"], ["2026", 546.24, "546,24 €", "gold"]], gap=2.0),
   dict(k="map", at="السؤال الحادش", until="الجواب: الفوائد", box=L_BOX, **MAROC),
   dict(k="people", at="السؤال الحادش", until="الجواب: الفوائد", box=R_BOX, people=["man"],
        say=[dict(who=0, text="كونطو فالمغرب؟", at=2.0, bg="gold")]),
   dict(k="text", text="الفوائد كتحسب · صرح بالكونطو", at="الجواب: الفوائد", until="السؤال التناش", y=560, size=80, color=GOLD),
   dict(k="people", at="السؤال التناش", until="الجواب: لا. الإينبس عندو", box=FULL, people=["worker", "elder"],
        say=[dict(who=0, text="نخرجو ليك فسيمانة", at=1.5, bg="red")]),
   dict(k="warn", text="الطلب فابور · ما تخلص حتى وسيط", at="الجواب: لا. الإينبس عندو", until="السؤال التلطاش", y=560),
   dict(k="people", at="السؤال التلطاش", until="الجواب: علم الإينبس", box=FULL, people=["elder", "hijab"],
        say=[dict(who=0, text="بغيت نتزوج", at=1.5, bg="gold")]),
   dict(k="icons", at="الجواب: علم الإينبس", until="وإلى عندك سؤال آخر", box=ICB, items=[
     ["mail", "علم الإينبس", "blue"], ["users", "الدخل ديال جوج", "gold"]], gap=2.0),
   dict(k="people", at="وإلى عندك سؤال آخر", until=None, box=FULL, people=["woman", "man"],
        say=[dict(who=0, text="كتب فالكومونتير", at=1.0, bg="green")]),
 ]),
 # ---------------------------------------------------------------- 09
 dict(audio="I.wav", text=T["I"], chapter="09 · اللائحة النهائية", src=S_HOME, items=[
   dict(k="chapter", num="09", title="اللائحة النهائية", at=0.1, until="واحد: تأكد من العمر"),
   dict(k="rows", at="واحد: تأكد من العمر", until="وعاود معايا الأرقام", y=160, gap=82, size=42, rows=[
     ("67 عام نهار الطلب", "1", "واحد: تأكد"),
     ("الكارطا", "2", "جوج: تأكد"),
     ("العشر سنين والسفرات", "3", "تلاتة: حسب"),
     ("الدخل · المغرب", "4", "ربعة: جمع"),
     ("السبيد والإيبان", "5", "خمسة: وجد"),
     ("الطلب فالوقت", "6", "ستة: دير"),
     ("التصريح كل عام", "7", "سبعة: صرح"),
     ("29 يوم ماكسيموم", "8", "تمنية: ما تبقاش"),
     ("حتى وسيط", "9", "وتسعة: ما تخلص", RED),
   ]),
   dict(k="rows", at="وعاود معايا الأرقام", until="والمبلغ لواحد", y=200, gap=96, size=42, rows=[
     ("المبلغ الكامل فالشهر", "546,24 €", "المبلغ الكامل:", GOLD),
     ("الحد · بوحدك", "7.101,12 €", "الحد ديال الدخل للي بوحدو"),
     ("الحد · مزوجين", "14.202,24 €", "وللمزوجين:"),
     ("العمر", "67", "والعمر:"),
     ("السكنى", "10", "والسكنى:"),
     ("السفر · يوم", "29", "والسفر:"),
     ("الجواب · يوم", "45", "والجواب ديال الإينبس"),
   ]),
   dict(k="text", text="الحد ناقص الدخل · على 13", at="والمبلغ لواحد", until="ونرجعو للحالات", y=540, size=90, color=GOLD),
   dict(k="rows", at="ونرجعو للحالات", until="وكل واحد فيهم", y=260, gap=125, size=44, rows=[
     ("الحاج محمد · تورينو", "546,24 €", "الحاج محمد فتورينو، بلا", GOLD),
     ("فاطنة · بولونيا", "454 €", "فاطنة فبولونيا، مع"),
     ("عبد القادر وزهرة · ميلانو", "400 €", "عبد القادر وزهرة فميلانو، مزوجين"),
     ("لحسن · بريشا", "2030", "ولحسن فبريشا: خاصو", RED),
   ]),
   dict(k="map", at="وكل واحد فيهم", until="وتلاتة ديال النصائح", box=BIGMAP, **IT_ALL),
   dict(k="icons", at="وتلاتة ديال النصائح", until="وإلى كنتي نتا ماشي المعني", box=ICB, items=[
     ["calendar", "ما تعطلش الطلب", "green"], ["file-text", "كلشي بالكتابة", "blue"], ["plane", "حسب الأيام", "gold"]], gap=3.0),
   dict(k="people", at="وإلى كنتي نتا ماشي المعني", until="والفصول ديال الفيديو", box=FULL, people=["man", "elder", "hijab"],
        say=[dict(who=0, text="نجلسو هاد السيمانة", at=2.0, bg="green")]),
   dict(k="text", text="الفصول والمصادر فالوصف", at="والفصول ديال الفيديو", until="ودابا، سؤال ليك", y=600, size=64, color=GOLD),
   dict(k="people", at="ودابا، سؤال ليك", until="وإلى عرفتي شي واحد", box=FULL, people=["woman", "elder"],
        say=[dict(who=0, text="شي واحد فالعائلة؟", at=1.0, bg="gold"), dict(who=1, text="إيه ولا لا", at=4.5, bg="green")]),
   dict(k="people", at="وإلى عرفتي شي واحد", until="وإلى عجبك", box=FULL, people=["hijab", "worker"],
        say=[dict(who=0, text="صيفطو للعائلة", at=1.0, bg="gold")]),
   dict(k="cta", at="وإلى عجبك", text="ابوني فالقناة", sub="كل نهار دليل مفيد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("عندك 67 عام بلا بانسيون؟", (236, 196, 96)), "الأسينيو سوسيالي 2026", "الشروط والسفر للمغرب"],
  num="546 €", numsub="فالشهر · 13 مرة فالعام",
  bottom="مغاربة إيطاليا · دليل عملي بالدارجة",
)
