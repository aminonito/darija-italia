import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_J1 = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-24-f.json"), encoding="utf-8"))
_J2 = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-24-r.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo2-2026-11-24-final")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = {k: v.replace("گ", "ك") for k, v in {**_J1["blocks"], **_J2["blocks"]}.items()}

S_HOME = "مغاربة إيطاليا · دليل عملي بالدارجة"
S_REQ = "art. 116 c.c. · Corte cost. 245/2011 · Moudawana artt. 14, 15, 19 (adala.justice.gov.ma) · L. 65.21"
S_IT = "Min. Giustizia · Comuni di Siracusa, Arezzo, Casalmorano · Studio Cataldi · artt. 107, 162 c.c. · DPR 396/2000"
S_MA = "Moudawana artt. 15, 65 · Fondation Hassan II MRE · Médias24 (circolare 2016) · HCCH (apostille)"
S_STEP = "Comuni (pubblicazioni, 16 €) · art. 30 D.Lgs. 286/1998 · Moudawana art. 15"
S_CASI = "D.Lgs. 30/2007 art. 23 · art. 5 L. 91/1992 · DPR 396/2000 art. 19 · Farnesina · art. 30 TUI"
S_ERR = "art. 30 c. 1-bis TUI · Min. Interno circ. 24/2013 · Corte cost. 245/2011 · Moudawana art. 15"
S_QA = "Fonti dei capitoli 01-07"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850); FULL = (160, 300, 1760, 860); MID = (260, 220, 1660, 840)
ICB = (160, 330, 1760, 860); VSB = (260, 220, 1660, 820); BARB = (160, 330, 1760, 840)

MED_TO = dict(view="med", hl=["ITA", "MAR"], route=["Casablanca", "Torino", "plane"], pins=["Casablanca", "Torino"], labels=False)
MED_FES = dict(view="med", hl=["ITA", "MAR"], route=["Fes", "Milano", "plane"], pins=["Fes", "Milano"], labels=False)
MED_BO = dict(view="med", hl=["ITA", "MAR"], route=["Tanger", "Bologna", "plane"], pins=["Tanger", "Bologna"], labels=False)
MAROC = dict(view="maroc", hl=["MAR"], pins=["Rabat"], labels=False)
MAROC_FES = dict(view="maroc", hl=["MAR"], pins=["Fes"], labels=False)
N_TO = dict(view="north", pins=["Torino"], labels=False)
N_BO = dict(view="north", pins=["Bologna"], labels=False)
ML = (160, 200, 1760, 880); MR = (160, 200, 1760, 880)
N_MI = dict(view="north", pins=["Milano"], labels=False)

BLOCKS = [
 # ---------------------------------------------------------------- 01
 dict(audio="A.wav", text=T["A"], chapter="01 · شكون خاصو هاد الدليل", src=S_HOME, items=[
   dict(k="head", text="الزواج فإيطاليا وفالمغرب", at=0.2, until="باغي تتزوج هنا فإيطاليا", sub="الكومون · القنصلية · البيرميسو · خطوة بخطوة"),
   dict(k="people", at="باغي تتزوج هنا فإيطاليا", until="ولا تزوجتي فالمغرب عند العدول", box=FULL, people=["woman", "man"],
        say=[dict(who=0, text="فالكومون؟", at=1.0, bg="gold"), dict(who=1, text="شنو خاصنا؟", at=2.5, bg="green")]),
   dict(k="map", at="ولا تزوجتي فالمغرب عند العدول", until="ولا تزوجتي فإيطاليا وما عرفتيش", box=FULL, **MED_FES),
   dict(k="people", at="ولا تزوجتي فإيطاليا وما عرفتيش", until="وفهاد الدليل غادي نشوفو حتى", box=FULL, people=["hijab", "clerk"],
        say=[dict(who=0, text="والقنصلية؟", at=1.5, bg="gold"), dict(who=1, text="3 شهور", at=4.0, bg="blue")]),
   dict(k="icons", at="وفهاد الدليل غادي نشوفو حتى", until="وعلاش دابا؟", box=ICB, items=[
     ["license", "البيرميسو", "blue"], ["building-bank", "المغرب", "gold"], ["calendar", "الآجال", "green"]], gap=2.5),
   dict(k="map", at="وعلاش دابا؟", until="علاش هاد الموضوع مهم؟", box=L_BOX, **MED_BO),
   dict(k="people", at="وعلاش دابا؟", until="علاش هاد الموضوع مهم؟", box=R_BOX, people=["man", "woman"],
        say=[dict(who=0, text="العرس فالصيف", at=2.5, bg="gold"), dict(who=1, text="الوراق من دابا", at=7.0, bg="green")]),
   dict(k="vs", at="علاش هاد الموضوع مهم؟", until="زواج صحيح هنا وما مسجلش", box=VSB,
        right=dict(title="إيطاليا", value="القانون المدني", sub="الكومون", icon="building-bank", color="blue"),
        left=dict(title="المغرب", value="مدونة الأسرة", sub="القنصلية", icon="scale", color="gold"), gap=4.0),
   dict(k="icons", at="زواج صحيح هنا وما مسجلش", until="وزواج تدار فالمغرب", box=ICB, items=[
     ["file-text", "الدفتر", "red"], ["users", "تسجيل الولاد", "red"], ["id", "الوراق فالمغرب", "red"]], gap=2.0),
   dict(k="icons", at="وزواج تدار فالمغرب", until="باش يكون الشرح واضح", box=ICB, items=[
     ["file-certificate", "وراق إيطالية", "red"], ["e-passport", "الجنسية", "red"]], gap=3.0),
   dict(k="text", text="تلاتة ديال الحالات", at="باش يكون الشرح واضح", until="الحالة الأولى، نادية", y=520, size=96, color=GOLD),
   dict(k="map", at="الحالة الأولى، نادية", until="الحالة التانية، هند", box=L_BOX, **N_TO),
   dict(k="people", at="الحالة الأولى، نادية", until="الحالة التانية، هند", box=R_BOX, people=["woman", "man"],
        say=[dict(who=0, text="نادية · الكارطا", at=1.5, bg="gold"), dict(who=1, text="يوسف · الخدمة", at=5.0, bg="green")]),
   dict(k="map", at="الحالة التانية، هند", until="والحالة التالتة، رشيد", box=L_BOX, **N_BO),
   dict(k="people", at="الحالة التانية، هند", until="والحالة التالتة، رشيد", box=R_BOX, people=["hijab", "man"],
        say=[dict(who=0, text="هند · بولونيا", at=1.0, bg="gold"), dict(who=1, text="كريم · إيطالي", at=3.5, bg="blue")]),
   dict(k="map", at="والحالة التالتة، رشيد", until="فهاد الدليل غادي نمشيو", box=L_BOX, **MED_FES),
   dict(k="people", at="والحالة التالتة، رشيد", until="فهاد الدليل غادي نمشيو", box=R_BOX, people=["worker", "woman"],
        say=[dict(who=0, text="معروف فإيطاليا؟", at=6.0, bg="gold"), dict(who=0, text="كيفاش نجيبها؟", at=9.0, bg="green")]),
   dict(k="rows", at="فهاد الدليل غادي نمشيو", until="وكل معلومة فهاد الفيديو", y=215, gap=78, size=40, rows=[
     ("شكون خاصو هاد الدليل", "01", "الأول، شكون"),
     ("الشروط", "02", "التاني، الشروط"),
     ("الكومون والوراق", "03", "التالت، الوراق"),
     ("القنصلية والمغرب", "04", "الرابع، القنصلية"),
     ("الخطوات والثمن والمدة", "05", "الخامس، الخطوات"),
     ("الحالات الخاصة", "06", "السادس، الحالات"),
     ("الأخطاء", "07", "السابع، الأخطاء"),
     ("سؤال وجواب", "08", "التامن، سؤال"),
     ("اللائحة النهائية", "09", "والتاسع، لائحة"),
   ]),
   dict(k="icons", at="وكل معلومة فهاد الفيديو", until="وعقل مزيان", box=ICB, items=[
     ["scale", "القانون المدني", "blue"], ["building-bank", "المحكمة الدستورية", "gold"], ["file-text", "مدونة الأسرة", "green"], ["home", "الكومونات", "blue"]], gap=2.2),
   dict(k="warn", text="محتوى إخباري · ماشي استشارة قانونية", at="وعقل مزيان", until="وحاجة أخيرة قبل ما نبداو", y=600),
   dict(k="people", at="وحاجة أخيرة قبل ما نبداو", until=None, box=FULL, people=["student", "hijab"],
        say=[dict(who=0, text="كتب سؤالك", at=1.0, bg="green")]),
 ]),
 # ---------------------------------------------------------------- 02
 dict(audio="B.wav", text=T["B"], chapter="02 · الشروط", src=S_REQ, items=[
   dict(k="chapter", num="02", title="الشروط فالجهتين", at=0.1, until="القانون المدني الإيطالي، فالفصل"),
   dict(k="big", text="116", sub="القانون المدني الإيطالي · الفصل", at="القانون المدني الإيطالي، فالفصل", until="هادا هو اللي كيسميوه"),
   dict(k="people", at="هادا هو اللي كيسميوه", until="وعقل حتى على هادي", box=FULL, people=["clerk", "man"],
        say=[dict(who=0, text="النولا أوسطا", at=0.5, bg="gold"), dict(who=1, text="من القنصلية", at=4.0, bg="green")]),
   dict(k="icons", at="وعقل حتى على هادي", until="ونفس الفصل كيقول", box=ICB, items=[
     ["user", "عازب", "green"], ["file-text", "مطلق", "gold"], ["file-text", "أرمل", "blue"]], gap=2.5),
   dict(k="map", at="ونفس الفصل كيقول", until="والسؤال اللي كيتعاود", box=L_BOX, **N_TO),
   dict(k="people", at="ونفس الفصل كيقول", until="والسؤال اللي كيتعاود", box=R_BOX, people=["office"],
        say=[dict(who=0, text="الإعلان فالكومون", at=1.0, bg="blue")]),
   dict(k="people", at="والسؤال اللي كيتعاود", until="فعام ألفين وحداش", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="بلا بيرميسو؟", at=1.0, bg="gold"), dict(who=1, text="إيه · تقدر", at=4.0, bg="green")]),
   dict(k="big", text="245/2011", sub="المحكمة الدستورية · الحكم", at="فعام ألفين وحداش", until="يعني تقدر تتزوج فالكومون"),
   dict(k="icons", at="يعني تقدر تتزوج فالكومون", until="ولكن عقل: الزواج بوحدو", box=ICB, items=[
     ["e-passport", "الباسبور", "green"], ["file-certificate", "النولا أوسطا", "gold"]], gap=2.0),
   dict(k="warn", text="الزواج بوحدو ما كيعطيش البيرميسو ديما", at="ولكن عقل: الزواج بوحدو", until="دابا الجهة المغربية", y=600),
   dict(k="map", at="دابا الجهة المغربية", until="فالمادة أربعطاش", box=MR, **MAROC),
   dict(k="big", text="18", sub="عام · المادة 19", at="فالمادة تسعطاش", until="فالمادة أربعطاش", x=1560, y=470),
   dict(k="head", text="المادة 14 · مدونة الأسرة", at="فالمادة أربعطاش", until="يعني الزواج فالكومون الإيطالي", sub="الزواج حسب الإجراءات ديال بلاد الإقامة"),
   dict(k="map", at="يعني الزواج فالكومون الإيطالي", until="المادة كتذكر ستة", box=(160, 330, 1760, 880), **MED_TO),
   dict(k="steps", at="المادة كتذكر ستة", until="هنا كاين نقطة عملية", box=MID, steps=[
     ["الإيجاب والقبول", "1"], ["الأهلية", "2"], ["الولي إلى كان ضروري", "3"],
     ["بلا مانع", "4"], ["الصداق", "5"], ["جوج شهود مسلمين", "6"]], gap=4.5, check_after=0.6),
   dict(k="vs", at="هنا كاين نقطة عملية", until="وإلى كان العقد الإيطالي ما فيهش", box=VSB,
        right=dict(title="الكومون", value="جوج شهود", sub="حتى من العائلة", icon="users", color="blue"),
        left=dict(title="المغرب", value="جوج مسلمين", sub="المادة 14", icon="users", color="gold"), gap=4.0),
   dict(k="people", at="وإلى كان العقد الإيطالي ما فيهش", until="والشرط الأخير فالمغرب", box=FULL, people=["clerk", "hijab"],
        say=[dict(who=0, text="كاين حل فالقنصلية", at=4.0, bg="green")]),
   dict(k="calendar", at="والشرط الأخير فالمغرب", until="نرجعو لنادية ويوسف", box=R_BOX, day=3, month="شهور", sub="الإيداع فالقنصلية · المادة 15"),
   dict(k="map", at="والشرط الأخير فالمغرب", until="ومن عام ألفين وواحد وعشرين", box=L_BOX, **MED_TO),
   dict(k="vs", at="ومن عام ألفين وواحد وعشرين", until="نرجعو لنادية ويوسف", box=L_BOX,
        right=dict(title="من قبل", value="بلاصة الزواج", sub="", icon="map-pin", color="red"),
        left=dict(title="دابا", value="القنصلية ديالك", sub="حسب السكنى", icon="home", color="green"), gap=3.0),
   dict(k="map", at="نرجعو لنادية ويوسف", until="شنو خاصهم؟", box=L_BOX, **N_TO),
   dict(k="people", at="نرجعو لنادية ويوسف", until="شنو خاصهم؟", box=R_BOX, people=["woman", "man"],
        say=[dict(who=0, text="الكارطا", at=4.0, bg="gold"), dict(who=1, text="بيرميسو الخدمة", at=6.5, bg="green")]),
   dict(k="steps", at="شنو خاصهم؟", until="ومن بعد الزواج، عندهم تلاتة", box=MID, steps=[
     ["النولا أوسطا لكل واحد", "1"], ["الإعلان فتورينو", "2"], ["جوج شهود", "3"], ["الشهود والصداق", "4"]], gap=3.0, check_after=0.6),
   dict(k="calendar", at="ومن بعد الزواج، عندهم تلاتة", until="ودابا نمشيو للوراق", box=R_BOX, day=3, month="شهور", sub="من بعد الزواج"),
   dict(k="people", at="ومن بعد الزواج، عندهم تلاتة", until="ودابا نمشيو للوراق", box=L_BOX, people=["clerk"],
        say=[dict(who=0, text="القنصلية", at=1.5, bg="blue")]),
   dict(k="text", text="الكومون الإيطالي", at="ودابا نمشيو للوراق", y=520, size=96, color=GOLD),
 ]),
 # ---------------------------------------------------------------- 03
 dict(audio="C.wav", text=T["C"], chapter="03 · الكومون والوراق", src=S_IT, items=[
   dict(k="chapter", num="03", title="الكومون: 7 خطوات", at=0.1, until="الخطوة الأولى هي النولا"),
   dict(k="map", at="الخطوة الأولى هي النولا", until="عازب، مطلق، ولا أرمل", box=L_BOX, **MED_TO),
   dict(k="people", at="الخطوة الأولى هي النولا", until="عازب، مطلق، ولا أرمل", box=R_BOX, people=["clerk"],
        say=[dict(who=0, text="الشهادة الإدارية", at=3.0, bg="gold")]),
   dict(k="icons", at="عازب، مطلق، ولا أرمل", until="والوراق اللي كتطلب القنصلية", box=ICB, items=[
     ["user", "عازب", "green"], ["file-text", "مطلق", "gold"], ["file-text", "أرمل", "blue"]], gap=0.5),
   dict(k="people", at="والوراق اللي كتطلب القنصلية", until="الخطوة التانية: التصديق", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="شنو نجيب؟", at=1.0, bg="gold"), dict(who=1, text="شوف الموقع الرسمي", at=4.0, bg="blue")]),
   dict(k="map", at="الخطوة التانية: التصديق", until="وإلى جبتي الوثيقة من الإدارة", box=L_BOX, **N_TO),
   dict(k="steps", at="الخطوة التانية: التصديق", until="وإلى جبتي الوثيقة من الإدارة", box=R_BOX, steps=[
     ["القنصلية", "1"], ["البريفيتورا", "2"], ["الكومون", "3"]], gap=3.0, check_after=0.5),
   dict(k="vs", at="وإلى جبتي الوثيقة من الإدارة", until="الخطوة التالتة: الإعلان", box=VSB,
        right=dict(title="القنصلية فإيطاليا", value="تصديق", sub="البريفيتورا", icon="building-bank", color="green"),
        left=dict(title="من المغرب", value="ترجمة", sub="+ تصديق", icon="file-certificate", color="gold"), gap=3.0),
   dict(k="head", text="الإعلان ديال الزواج", at="الخطوة التالتة: الإعلان", until="وإلى كنتو ساكنين فجوج", sub="فالكومون ديال السكنى"),
   dict(k="map", at="وإلى كنتو ساكنين فجوج", until="الإعلان كيتعلق على الأقل", box=(160, 200, 1760, 880), **N_BO),
   dict(k="calendar", at="الإعلان كيتعلق على الأقل", until="يعني تقدر تتزوج من النهار الرابع", box=R_BOX, day=8, month="أيام", sub="التعليق · على الأقل"),
   dict(k="people", at="الإعلان كيتعلق على الأقل", until="يعني تقدر تتزوج من النهار الرابع", box=L_BOX, people=["office"],
        say=[dict(who=0, text="وتلاتة أيام", at=3.0, bg="blue")]),
   dict(k="steps", at="يعني تقدر تتزوج من النهار الرابع", until="وعقل على هادي: الزواج خاصو", box=MID, steps=[
     ["التعليق", "8"], ["التعرض", "3"], ["النهار الرابع: الزواج", "OK"]], gap=2.0, check_after=0.5),
   dict(k="big", text="180", sub="يوم · باش تتزوج", at="وعقل على هادي: الزواج خاصو", until="الثمن ديال الإعلان", color=RED),
   dict(k="bars", at="الثمن ديال الإعلان", until="الخطوة الرابعة: الترجمان", box=BARB, bars=[
     ["نفس الكومون", 16, "16 €", "green"], ["جوج كومونات", 32, "32 €", "gold"]], gap=3.0),
   dict(k="people", at="الخطوة الرابعة: الترجمان", until="الخطوة الخامسة: الشهود", box=FULL, people=["man", "student", "office"],
        say=[dict(who=1, text="الترجمان", at=2.0, bg="gold"), dict(who=2, text="بالوثيقة ديالو", at=8.0, bg="blue")]),
   dict(k="people", at="الخطوة الخامسة: الشهود", until="الخطوة السادسة: القاعة", box=FULL, people=["man", "woman", "worker"],
        say=[dict(who=0, text="شاهد", at=1.5, bg="green"), dict(who=2, text="شاهد تاني", at=3.0, bg="green")]),
   dict(k="head", text="القاعة والنهار", at="الخطوة السادسة: القاعة", until="وكاين كومونات كيطلبو تحجز", sub="الثمن كيقررو كل كومون"),
   dict(k="vs", at="الخطوة السادسة: القاعة", until="وكاين كومونات كيطلبو تحجز", box=(260, 390, 1660, 860),
        right=dict(title="القاعة العادية", value="0 €", sub="فبعض الكومونات · وقت الخدمة", icon="building-bank", color="green"),
        left=dict(title="قاعات أخرى · السبت", value="مئات", sub="ديال الأوروات", icon="coin-euro", color="gold"), gap=5.0),
   dict(k="calendar", at="وكاين كومونات كيطلبو تحجز", until="والخطوة السابعة، اللي كتنساوها", box=R_BOX, day=3, month="شهور", sub="قبل · فبعض الكومونات"),
   dict(k="map", view="italy", pins=["Torino", "Bologna"], labels=False, at="وكاين كومونات كيطلبو تحجز", until="والخطوة السابعة، اللي كتنساوها", box=L_BOX),
   dict(k="head", text="الأملاك", at="والخطوة السابعة، اللي كتنساوها", until="ولكن تقدرو تختارو", sub="مشتركة · ولا كل واحد بوحدو"),
   dict(k="vs", at="ولكن تقدرو تختارو", until="والقوانين الأوروبية", box=VSB,
        right=dict(title="النظام العادي", value="مشتركة", sub="القانون الإيطالي", icon="users", color="blue"),
        left=dict(title="الاختيار", value="مفرقة", sub="نهار الزواج", icon="user", color="gold"), gap=2.0),
   dict(k="icons", at="والقوانين الأوروبية", until="نادية ويوسف، شنو داو", box=ICB, items=[
     ["home", "بلاد السكنى", "blue"], ["e-passport", "بلاد الجنسية", "gold"], ["scale", "سول نوطير", "green"]], gap=3.0),
   dict(k="steps", at="نادية ويوسف، شنو داو", until="حيت جوج بيهم ساكنين فتورينو", box=MID, steps=[
     ["القنصلية", "1"], ["البريفيتورا", "2"], ["الإعلان فتورينو", "3"]], gap=2.0, check_after=0.5),
   dict(k="map", at="حيت جوج بيهم ساكنين فتورينو", until=None, box=L_BOX, **N_TO),
   dict(k="people", at="حيت جوج بيهم ساكنين فتورينو", until=None, box=R_BOX, people=["woman", "man"],
        say=[dict(who=0, text="تنبر واحد", at=1.0, bg="green"), dict(who=1, text="خويا شاهد", at=5.5, bg="gold")]),
 ]),
 # ---------------------------------------------------------------- 04
 dict(audio="D.wav", text=T["D"], chapter="04 · القنصلية والمغرب", src=S_MA, items=[
   dict(k="chapter", num="04", title="القنصلية والتسجيل فالمغرب", at=0.1, until="بزاف ديال الناس كيديرو الزواج"),
   dict(k="people", at="بزاف ديال الناس كيديرو الزواج", until="ومن بعد عامين", box=FULL, people=["woman", "man"],
        say=[dict(who=0, text="تزوجنا!", at=1.0, bg="green"), dict(who=1, text="والمغرب؟", at=4.0, bg="red")]),
   dict(k="icons", at="ومن بعد عامين", until="كيما قلنا، المادة خمسطاش", box=ICB, items=[
     ["users", "تسجيل الولد", "red"], ["file-text", "الدفتر", "red"]], gap=2.0),
   dict(k="calendar", at="كيما قلنا، المادة خمسطاش", until="وإلى ما كانتش قنصلية", box=R_BOX, day=3, month="شهور", sub="المادة 15 · الإيداع"),
   dict(k="map", at="كيما قلنا، المادة خمسطاش", until="وإلى ما كانتش قنصلية", box=L_BOX, **MED_TO),
   dict(k="map", at="وإلى ما كانتش قنصلية", until="ومن بعد، الإدارة كتصيفط", box=ML, **MAROC),
   dict(k="steps", at="ومن بعد، الإدارة كتصيفط", until="وإلى كانو جوج بيهم مزيودين", box=R_BOX, steps=[
     ["القنصلية", "1"], ["الحالة المدنية", "2"], ["قضاء الأسرة", "3"]], gap=2.5, check_after=0.5),
   dict(k="people", at="وإلى كانو جوج بيهم مزيودين", until="شنو كتجيب معاك للقنصلية", box=FULL, people=["man", "woman"],
        say=[dict(who=0, text="تزاديت فإيطاليا", at=1.0, bg="gold"), dict(who=1, text="الرباط", at=4.0, bg="blue")]),
   dict(k="icons", at="شنو كتجيب معاك للقنصلية", until="وكاين قنصليات كيطلبو", box=ICB, items=[
     ["file-text", "نسخة كاملة ديال العقد", "green"], ["id", "الوثائق ديال الهوية", "blue"]], gap=3.0),
   dict(k="icons", at="وكاين قنصليات كيطلبو", until="الأبوستيي هو الختم", box=ICB, items=[
     ["file-certificate", "ترجمة للعربية", "gold"], ["certificate", "الأبوستيي", "blue"]], gap=2.0),
   dict(k="big", text="14/8/2016", sub="المغرب فاتفاقية لاهاي · الأبوستيي", at="الأبوستيي هو الختم", until="ولكن اللائحة بالضبط"),
   dict(k="people", at="ولكن اللائحة بالضبط", until="دابا المشكل ديال الشهود", box=FULL, people=["clerk", "hijab"],
        say=[dict(who=1, text="شحال؟ شحال من وقت؟", at=1.0, bg="gold"), dict(who=0, text="الموقع الرسمي", at=8.0, bg="blue")]),
   dict(k="head", text="الإشهاد الملحق", at="دابا المشكل ديال الشهود", until="القسم ديال التوثيق فالقنصلية كيدير", sub="جوج شهود مسلمين + الصداق"),
   dict(k="people", at="القسم ديال التوثيق فالقنصلية كيدير", until="وحسب منشور ديال عام", box=FULL, people=["elder", "clerk", "man"],
        say=[dict(who=0, text="شاهد", at=2.0, bg="green"), dict(who=2, text="شاهد", at=3.0, bg="green"), dict(who=1, text="الصداق", at=6.0, bg="gold")]),
   dict(k="vs", at="وحسب منشور ديال عام", until="وحاجة مزيانة", box=VSB,
        right=dict(title="العادة", value="واحد يكفي", sub="من الزوجين", icon="user", color="green"),
        left=dict(title="الصداق", value="بجوج", sub="التزام مالي", icon="users", color="gold"), gap=5.0),
   dict(k="people", at="وحاجة مزيانة", until="شنو كتربح من هاد التسجيل", box=FULL, people=["woman", "child"],
        say=[dict(who=0, text="عقد الكومون كيتقبل", at=2.0, bg="green")]),
   dict(k="icons", at="شنو كتربح من هاد التسجيل", until="وعاود: الإيداع ماشي", box=ICB, items=[
     ["id", "الحالة المدنية", "green"], ["file-text", "الدفتر", "green"], ["users", "تسجيل الولاد", "green"]], gap=2.5),
   dict(k="vs", at="وعاود: الإيداع ماشي", until="والطريق التاني فالقنصلية", box=VSB,
        right=dict(title="الإيداع", value="ورقة", sub="فالقنصلية", icon="file-text", color="green"),
        left=dict(title="ماشي", value="عرس تاني", sub="", icon="x", color="red"), gap=2.5),
   dict(k="map", at="والطريق التاني فالقنصلية", until="هنا الملف، حسب المادة", box=L_BOX, **MED_FES),
   dict(k="people", at="والطريق التاني فالقنصلية", until="هنا الملف، حسب المادة", box=R_BOX, people=["clerk", "elder"],
        say=[dict(who=0, text="العدول فالقنصلية", at=2.0, bg="gold")]),
   dict(k="steps", at="هنا الملف، حسب المادة", until="وقاضي الأسرة المكلف", box=MID, steps=[
     ["طلب الإذن · الاستمارة", "1"], ["عقد الازدياد", "2"], ["شهادة إدارية لكل واحد", "3"], ["شهادة طبية لكل واحد", "4"]], gap=3.0, check_after=0.6),
   dict(k="people", at="وقاضي الأسرة المكلف", until="ولكن عقل: هاد الزواج المغربي", box=FULL, people=["office", "elder"],
        say=[dict(who=0, text="الإذن", at=2.0, bg="green")]),
   dict(k="map", at="ولكن عقل: هاد الزواج المغربي", until="نرجعو لنادية ويوسف. تزوجو", box=L_BOX, **N_MI),
   dict(k="people", at="ولكن عقل: هاد الزواج المغربي", until="نرجعو لنادية ويوسف. تزوجو", box=R_BOX, people=["office"],
        say=[dict(who=0, text="التسجيل فالكومون", at=2.0, bg="blue")]),
   dict(k="calendar", at="نرجعو لنادية ويوسف. تزوجو", until="يعني عندهم حتى لعشرين يونيو", box=R_BOX, day=20, month=3, sub="الزواج فالكومون"),
   dict(k="map", at="نرجعو لنادية ويوسف. تزوجو", until="الشهود ديالهم مسلمين", box=L_BOX, **N_TO),
   dict(k="calendar", at="يعني عندهم حتى لعشرين يونيو", until="الشهود ديالهم مسلمين", box=R_BOX, day=20, month=6, sub="آخر أجل · القنصلية"),
   dict(k="steps", at="الشهود ديالهم مسلمين", until=None, box=MID, steps=[
     ["الشهود", "1"], ["الإشهاد الملحق · الصداق", "2"], ["الدفتر العائلي", "3"]], gap=2.5, check_after=0.5),
 ]),
 # ---------------------------------------------------------------- 05
 dict(audio="E.wav", text=T["E"], chapter="05 · الخطوات والثمن والمدة", src=S_STEP, items=[
   dict(k="chapter", num="05", title="الخطوات والثمن والمدة", at=0.1, until="وغادي نتبعو نادية ويوسف"),
   dict(k="map", at="وغادي نتبعو نادية ويوسف", until="الخطوة الأولى: الموعد", box=(160, 200, 1760, 880), **N_TO),
   dict(k="calendar", at="الخطوة الأولى: الموعد", until="الخطوة التانية: البريفيتورا", box=R_BOX, day=2, month="شهور", sub="قبل الزواج · الموعد"),
   dict(k="people", at="الخطوة الأولى: الموعد", until="الخطوة التانية: البريفيتورا", box=L_BOX, people=["clerk"],
        say=[dict(who=0, text="الشهادة الإدارية", at=2.0, bg="gold")]),
   dict(k="steps", at="الخطوة التانية: البريفيتورا", until="الخطوة التالتة: الكومون", box=MID, steps=[
     ["التصديق", "2"], ["نسخ من كلشي", "+"]], gap=3.0, check_after=0.5),
   dict(k="icons", at="الخطوة التالتة: الكومون", until="الخطوة الرابعة: التعليق", box=ICB, items=[
     ["e-passport", "الباسبور", "blue"], ["certificate", "الشهادة مصادق عليها", "green"], ["receipt", "التنبر", "gold"]], gap=2.5),
   dict(k="rows", at="الخطوة الرابعة: التعليق", until="الخطوة الخامسة: نهار الزواج", y=300, gap=120, size=50, rows=[
     ("التعليق", "1/3 - 8/3", "الخطوة الرابعة: التعليق"),
     ("التعرض", "3", "ومن بعد تلاتة أيام ديال التعرض"),
     ("الزواج ممكن من", "12/3", "يعني من نهار طناش", GREEN),
     ("الأجل الأخير", "≈ 4/9", "والأجل الأخير، مية", RED),
   ]),
   dict(k="calendar", at="الخطوة الخامسة: نهار الزواج", until="وقبل التوقيع", box=R_BOX, day=20, month=3, sub="نهار الزواج · 2027"),
   dict(k="people", at="الخطوة الخامسة: نهار الزواج", until="وقبل التوقيع", box=L_BOX, people=["woman", "man"],
        say=[dict(who=1, text="بلا ترجمان", at=6.0, bg="green")]),
   dict(k="vs", at="وقبل التوقيع", until="الخطوة السادسة: عقد الزواج", box=VSB,
        right=dict(title="سولهم", value="الأملاك؟", sub="", icon="scale", color="blue"),
        left=dict(title="اختارو", value="مفرقة", sub="كل واحد بوحدو", icon="user", color="gold"), gap=2.5),
   dict(k="icons", at="الخطوة السادسة: عقد الزواج", until="الخطوة السابعة: الترجمة", box=ICB, items=[
     ["file-text", "نسخة كاملة ديال العقد", "green"]], gap=1.0),
   dict(k="icons", at="الخطوة السابعة: الترجمة", until="الخطوة التامنة: القنصلية", box=ICB, items=[
     ["file-certificate", "الترجمة", "gold"], ["certificate", "الأبوستيي", "blue"], ["calendar", "أبريل", "green"]], gap=2.0),
   dict(k="map", at="الخطوة التامنة: القنصلية", until="الخطوة التاسعة: الدفتر", box=L_BOX, **MED_TO),
   dict(k="calendar", at="الخطوة التامنة: القنصلية", until="الخطوة التاسعة: الدفتر", box=R_BOX, day=20, month=6, sub="قبل · الإيداع"),
   dict(k="icons", at="الخطوة التاسعة: الدفتر", until="والخطوة العاشرة: البيرميسو", box=ICB, items=[
     ["file-text", "الدفتر", "green"]], gap=1.0),
   dict(k="people", at="والخطوة العاشرة: البيرميسو", until="ولكن القانون الإيطالي، فالمادة تلاتين", box=FULL, people=["man", "office"],
        say=[dict(who=0, text="خاصني نبدلو؟", at=1.5, bg="gold"), dict(who=1, text="ماشي ملزم", at=5.0, bg="green")]),
   dict(k="head", text="المادة 30 · القانون الموحد ديال الهجرة", at="ولكن القانون الإيطالي، فالمادة تلاتين", until="سول الباترونا واش", sub="البيرميسو ديال العائلة"),
   dict(k="steps", at="اللي عندو البيرميسو بشي سبب آخر", until="سول الباترونا واش", box=(260, 330, 1660, 860), steps=[
     ["بيرميسو بسبب آخر", "1+"], ["الزواج فإيطاليا", "2"], ["البيرميسو ديال العائلة", "3"]], gap=3.5, check_after=0.5),
   dict(k="people", at="سول الباترونا واش", until="دابا الثمن", box=FULL, people=["worker", "office"],
        say=[dict(who=1, text="الباترونا", at=1.0, bg="blue")]),
   dict(k="bars", at="دابا الثمن", until="القاعة: من صفر", box=BARB, bars=[
     ["نفس الكومون", 16, "16 €", "green"], ["جوج كومونات", 32, "32 €", "gold"]], gap=3.0),
   dict(k="icons", at="القاعة: من صفر", until="والمدة؟", box=ICB, items=[
     ["building-bank", "القاعة", "green"], ["users", "الترجمان", "blue"], ["file-certificate", "الترجمة", "gold"], ["building-bank", "القنصلية · سول", "red"]], gap=2.5),
   dict(k="steps", at="والمدة؟", until="ونفس الحساب لهند وكريم", box=MID, steps=[
     ["من الموعد حتى الزواج · شهور", "2,5"], ["من الإعلان حتى الزواج · سيمانات", "2"], ["من الزواج حتى القنصلية · شهور", "3"]], gap=3.5, check_after=0.5),
   dict(k="map", at="ونفس الحساب لهند وكريم", until="خلاصة هاد الفصل", box=L_BOX, **N_BO),
   dict(k="bars", at="ونفس الحساب لهند وكريم", until="خلاصة هاد الفصل", box=R_BOX, bars=[
     ["بولونيا", 16, "16 €", "green"], ["مودينا", 16, "16 €", "gold"]], gap=2.0),
   dict(k="steps", at="خلاصة هاد الفصل", until=None, box=MID, steps=[
     ["القنصلية", "1"], ["البريفيتورا", "2"], ["الكومون", "3"], ["القنصلية فتلاتة شهور", "4"]], gap=2.0, check_after=0.5),
 ]),
 # ---------------------------------------------------------------- 06
 dict(audio="F.wav", text=T["F"], chapter="06 · الحالات الخاصة", src=S_CASI, items=[
   dict(k="chapter", num="06", title="الحالات الخاصة", at=0.1, until="هند مغربية ساكنة"),
   dict(k="map", at="هند مغربية ساكنة", until="بالنسبة لهند، نفس الطريق", box=L_BOX, **N_BO),
   dict(k="people", at="هند مغربية ساكنة", until="بالنسبة لهند، نفس الطريق", box=R_BOX, people=["hijab", "man"],
        say=[dict(who=1, text="إيطالي", at=2.5, bg="blue")]),
   dict(k="steps", at="بالنسبة لهند، نفس الطريق", until="شنو كيوقع للبيرميسو ديال هند", box=MID, steps=[
     ["النولا أوسطا · هند", "1"], ["الهوية · كريم", "2"], ["الإعلان فجوج كومونات", "3"], ["جوج تنابر", "4"]], gap=2.5, check_after=0.5),
   dict(k="people", at="شنو كيوقع للبيرميسو ديال هند", until="إلى كان كريم عمرو ما عاش", box=FULL, people=["hijab", "office"],
        say=[dict(who=0, text="والبيرميسو ديالي؟", at=0.5, bg="gold"), dict(who=1, text="جوج حالات", at=3.0, bg="blue")]),
   dict(k="vs", at="إلى كان كريم عمرو ما عاش", until="الباترونا كيعاونك تعرف", box=VSB,
        right=dict(title="كريم ما خرجش", value="5 سنين", sub="بيرميسو العائلة · بلا كونتريبيتو", icon="license", color="green"),
        left=dict(title="كريم عاش فأوروبا", value="5 سنين", sub="الكارطا ديال العائلة", icon="world", color="gold"), gap=12.0),
   dict(k="people", at="الباترونا كيعاونك تعرف", until="والجنسية؟", box=FULL, people=["office", "hijab"],
        say=[dict(who=0, text="شمن حالة؟", at=0.5, bg="blue")]),
   dict(k="head", text="الجنسية بالزواج · الفصل 5", at="والجنسية؟", until="هند وكريم تزوجو نهار", sub="جوج سنين · ولا عام مع الولاد"),
   dict(k="rows", at="هند وكريم تزوجو نهار", until="البريفيتورا كتحسب من النهار", y=300, gap=130, size=50, rows=[
     ("الزواج", "10/4/2027", "هند وكريم تزوجو نهار"),
     ("الجنسية", "10/4/2029", "يعني تقدر تطلب", GREEN),
     ("مع الولد", "10/4/2028", "ولا من عشرة أبريل", GOLD),
   ]),
   dict(k="vs", at="البريفيتورا كتحسب من النهار", until="ومن الشروط تاني", box=VSB,
        right=dict(title="الحساب", value="التسجيل", sub="فالكومون الإيطالي", icon="building-bank", color="green"),
        left=dict(title="ماشي", value="العرس", sub="", icon="x", color="red"), gap=3.0),
   dict(k="icons", at="ومن الشروط تاني", until="الحالة التانية: رشيد وسلمى", box=ICB, items=[
     ["school", "الطاليانية B1", "gold"], ["scale", "بلا مانع جنائي", "blue"], ["calendar", "الدليل 20/11", "green"]], gap=2.0),
   dict(k="map", at="الحالة التانية: رشيد وسلمى", until="واش خاصو يتسجل فإيطاليا", box=(160, 200, 1760, 880), **MED_FES),
   dict(k="people", at="واش خاصو يتسجل فإيطاليا", until="القانون ديال الحالة المدنية، فالمادة", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="واش لازم؟", at=0.5, bg="gold"), dict(who=1, text="المادة 19", at=4.0, bg="blue")]),
   dict(k="icons", at="القانون ديال الحالة المدنية، فالمادة", until="يعني بالنسبة لرشيد", box=ICB, items=[
     ["home", "الكومون ديال السكنى", "blue"], ["file-certificate", "الترجمة", "gold"], ["certificate", "الأبوستيي", "green"]], gap=2.5),
   dict(k="vs", at="يعني بالنسبة لرشيد", until="وإلى بغا رشيد يجيب سلمى", box=VSB,
        right=dict(title="جوج أجانب", value="اختيار", sub="", icon="users", color="green"),
        left=dict(title="واحد إيطالي", value="ضروري", sub="القنصلية الإيطالية ولا الكومون", icon="alert-triangle", color="red"), gap=4.5),
   dict(k="map", at="وإلى بغا رشيد يجيب سلمى", until="الحالة التالتة: الزوج اللي", box=L_BOX, **MED_FES),
   dict(k="people", at="وإلى بغا رشيد يجيب سلمى", until="الحالة التالتة: الزوج اللي", box=R_BOX, people=["worker", "woman"],
        say=[dict(who=0, text="التجمع العائلي", at=1.0, bg="gold"), dict(who=1, text="الدليل 12/11", at=4.0, bg="green")]),
   dict(k="people", at="الحالة التالتة: الزوج اللي", until="إلى كان الزوج إيطالي ولا لاجئ", box=FULL, people=["man", "office"],
        say=[dict(who=0, text="ما عنديش البيرميسو", at=1.0, bg="gold")]),
   dict(k="vs", at="إلى كان الزوج إيطالي ولا لاجئ", until="الحالة الرابعة", box=VSB,
        right=dict(title="إيطالي ولا لاجئ", value="كاين طريق", sub="الباترونا · محامي", icon="scale", color="green"),
        left=dict(title="حالات أخرى", value="لا", sub="الزواج ما كيحلش", icon="x", color="red"), gap=4.0),
   dict(k="steps", at="الحالة الرابعة", until="والحالة الخامسة", box=MID, steps=[
     ["بيرميسو أقل من عام", "1"], ["التماسك العائلي", "2"], ["المدخول + السكن", "3"]], gap=3.0, check_after=0.5),
   dict(k="map", at="والحالة الخامسة", until="هادا استثنائي", box=ML, **MAROC_FES),
   dict(k="people", at="هادا استثنائي", until=None, box=FULL, people=["office"],
        say=[dict(who=0, text="إذن القاضي", at=1.0, bg="red")]),
 ]),
 # ---------------------------------------------------------------- 07
 dict(audio="G.wav", text=T["G"], chapter="07 · الأخطاء", src=S_ERR, items=[
   dict(k="chapter", num="07", title="10 أخطاء والحلول", at=0.1, until="الغلطة الأولى"),
   dict(k="people", at="الغلطة الأولى", until="الغلطة التانية", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="بلا بيرميسو ما نقدرش؟", at=0.8, bg="red"), dict(who=1, text="غلط", at=4.0, bg="green")]),
   dict(k="vs", at="الغلطة التانية", until="الغلطة التالتة", box=VSB,
        right=dict(title="مزيان", value="النولا أوسطا", sub="مصادق عليها", icon="file-certificate", color="green"),
        left=dict(title="غلط", value="ورقة أخرى", sub="بلا تصديق", icon="x", color="red"), gap=3.0),
   dict(k="big", text="180", sub="يوم · إلى فاتو كتعاود", at="الغلطة التالتة", until="الغلطة الرابعة", color=RED),
   dict(k="people", at="الغلطة الرابعة", until="الغلطة الخامسة", box=FULL, people=["office", "man"],
        say=[dict(who=0, text="فين الترجمان؟", at=1.0, bg="red")]),
   dict(k="map", at="الغلطة الخامسة", until="حيت بلا تسجيل", box=L_BOX, **MED_TO),
   dict(k="calendar", at="الغلطة الخامسة", until="حيت بلا تسجيل", box=R_BOX, day=3, month="شهور", sub="القنصلية · ما تنساش"),
   dict(k="icons", at="حيت بلا تسجيل", until="الغلطة السادسة", box=ICB, items=[
     ["file-text", "الدفتر", "red"], ["users", "الولاد", "red"], ["id", "الوراق فالمغرب", "red"]], gap=1.5),
   dict(k="map", at="الغلطة السادسة", until="الغلطة السابعة", box=L_BOX, **MED_FES),
   dict(k="people", at="الغلطة السادسة", until="الغلطة السابعة", box=R_BOX, people=["man", "hijab"],
        say=[dict(who=0, text="العدول كافيين؟", at=1.0, bg="gold"), dict(who=1, text="لا · التسجيل", at=6.0, bg="red")]),
   dict(k="vs", at="الغلطة السابعة", until="الغلطة التامنة", box=VSB,
        right=dict(title="صحيح", value="التسجيل", sub="فالكومون", icon="building-bank", color="green"),
        left=dict(title="غلط", value="نهار العرس", sub="فالمغرب", icon="x", color="red"), gap=3.0),
   dict(k="warn", text="الزواج غير على ودّ الوراق = البيرميسو كيتحيد", at="الغلطة التامنة", until="والطلب كيترفض", y=600),
   dict(k="people", at="والطلب كيترفض", until="الغلطة التاسعة", box=FULL, people=["office"],
        say=[dict(who=0, text="المادة 30", at=1.0, bg="red")]),
   dict(k="people", at="الغلطة التاسعة", until="وعندنا غلطة صغيرة", box=FULL, people=["man", "worker"],
        say=[dict(who=0, text="عطيني الفلوس...", at=1.5, bg="red"), dict(who=1, text="لا · نصابة", at=8.0, bg="green")]),
   dict(k="icons", at="وعندنا غلطة صغيرة", until="والغلطة العاشرة", box=ICB, items=[
     ["file-text", "نسخ", "green"], ["camera", "صور الإيصالات", "blue"], ["clipboard-check", "دوسي واحد", "gold"]], gap=2.5),
   dict(k="vs", at="والغلطة العاشرة", until="دابا، شنو دير", box=VSB,
        right=dict(title="ما قلتو والو", value="العادي", sub="", icon="users", color="gold"),
        left=dict(title="من بعد", value="النوطير", sub="إجراءات", icon="scale", color="blue"), gap=4.0),
   dict(k="text", text="إلى ما مشاتش الأمور مزيان", at="دابا، شنو دير", until="إلى القنصلية ما عطاتكش", y=520, size=90, color=GOLD),
   dict(k="steps", at="إلى القنصلية ما عطاتكش", until="إلى الكومون طلب منك", box=MID, steps=[
     ["منشور الداخلية 2013", "1"], ["المحكمة الإيطالية", "2"], ["محامي", "3"]], gap=4.0, check_after=0.5),
   dict(k="people", at="إلى الكومون طلب منك", until="إلى ترفض ليك البيرميسو", box=FULL, people=["office", "woman"],
        say=[dict(who=1, text="كتبوها ليا", at=2.0, bg="gold")]),
   dict(k="map", at="إلى ترفض ليك البيرميسو", until="وإلى كان عندك مشكل فالمغرب", box=L_BOX, **N_TO),
   dict(k="people", at="إلى ترفض ليك البيرميسو", until="وإلى كان عندك مشكل فالمغرب", box=R_BOX, people=["office"],
        say=[dict(who=0, text="بسرعة · الآجال قصار", at=3.0, bg="red")]),
   dict(k="map", at="وإلى كان عندك مشكل فالمغرب", until="القنصلية هي البلاصة", box=ML, **MAROC),
   dict(k="people", at="القنصلية هي البلاصة", until=None, box=FULL, people=["clerk"],
        say=[dict(who=0, text="القنصلية أولا", at=0.5, bg="blue")]),
 ]),
 # ---------------------------------------------------------------- 08
 dict(audio="H.wav", text=T["H"], chapter="08 · سؤال وجواب", src=S_QA, items=[
   dict(k="chapter", num="08", title="سؤال وجواب", at=0.1, until="السؤال الأول"),
   dict(k="people", at="السؤال الأول", until="السؤال التاني", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="غير الباسبور؟", at=1.0, bg="gold"), dict(who=1, text="إيه + النولا أوسطا", at=7.0, bg="green")]),
   dict(k="calendar", at="السؤال التاني", until="السؤال التالت", box=R_BOX, day=8, month="أيام", sub="وتلاتة أيام من بعد"),
   dict(k="people", at="السؤال التاني", until="السؤال التالت", box=L_BOX, people=["woman"],
        say=[dict(who=0, text="شحال كيدوم؟", at=1.0, bg="gold")]),
   dict(k="people", at="السؤال التالت", until="السؤال الرابع", box=L_BOX, people=["man"],
        say=[dict(who=0, text="شحال نخلص؟", at=1.0, bg="gold")]),
   dict(k="bars", at="السؤال التالت", until="السؤال الرابع", box=R_BOX, bars=[
     ["كومون واحد", 16, "16 €", "green"], ["جوج", 32, "32 €", "gold"]], gap=2.0),
   dict(k="map", at="السؤال الرابع", until="السؤال الخامس", box=L_BOX, **MED_TO),
   dict(k="people", at="السؤال الرابع", until="السؤال الخامس", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="القنصلية؟", at=1.0, bg="gold"), dict(who=0, text="3 شهور", at=6.0, bg="green")]),
   dict(k="people", at="السؤال الخامس", until="السؤال السادس", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="الشهود؟", at=1.0, bg="gold"), dict(who=1, text="الإشهاد الملحق", at=5.0, bg="green")]),
   dict(k="people", at="السؤال السادس", until="السؤال السابع", box=FULL, people=["woman", "man"],
        say=[dict(who=0, text="بجوج؟", at=1.0, bg="gold"), dict(who=1, text="واحد يكفي", at=4.0, bg="green")]),
   dict(k="map", at="السؤال السابع", until="السؤال التامن", box=L_BOX, **MED_FES),
   dict(k="vs", at="السؤال السابع", until="السؤال التامن", box=R_BOX,
        right=dict(title="جوج أجانب", value="اختيار", sub="", icon="users", color="green"),
        left=dict(title="واحد إيطالي", value="ضروري", sub="", icon="alert-triangle", color="red"), gap=6.0),
   dict(k="map", at="السؤال التامن", until="السؤال التاسع", box=L_BOX, **MED_BO),
   dict(k="people", at="السؤال التامن", until="السؤال التاسع", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="مراتي فالمغرب", at=1.0, bg="gold"), dict(who=0, text="الدليل 12/11", at=6.0, bg="green")]),
   dict(k="people", at="السؤال التاسع", until="السؤال العاشر", box=FULL, people=["man", "woman"],
        say=[dict(who=0, text="الجنسية؟", at=1.0, bg="gold"), dict(who=1, text="جوج سنين · عام مع الولاد", at=5.0, bg="green")]),
   dict(k="people", at="السؤال العاشر", until="السؤال الحادي عشر", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="البيرميسو كيتبدل؟", at=1.0, bg="gold"), dict(who=1, text="ماشي بزز", at=4.0, bg="blue")]),
   dict(k="vs", at="السؤال الحادي عشر", until="السؤال التاني عشر", box=VSB,
        right=dict(title="مشتركة", value="العادي", sub="", icon="users", color="blue"),
        left=dict(title="مفرقة", value="نهار الزواج", sub="فالعقد", icon="user", color="gold"), gap=2.0),
   dict(k="map", at="السؤال التاني عشر", until="السؤال التالت عشر", box=L_BOX, view="italy", pins=["Torino", "Bologna", "Napoli"], labels=False),
   dict(k="people", at="السؤال التاني عشر", until="السؤال التالت عشر", box=R_BOX, people=["elder"],
        say=[dict(who=0, text="القنصلية بعيدة", at=1.0, bg="gold"), dict(who=0, text="حسب السكنى", at=6.0, bg="blue")]),
   dict(k="people", at="السؤال التالت عشر", until="والسؤال الرابع عشر", box=FULL, people=["student", "clerk"],
        say=[dict(who=0, text="عند العدول هنا؟", at=1.0, bg="gold"), dict(who=1, text="إيه · بالإذن", at=4.0, bg="green")]),
   dict(k="people", at="والسؤال الرابع عشر", until=None, box=FULL, people=["hijab", "clerk"],
        say=[dict(who=0, text="شحال فالقنصلية؟", at=1.0, bg="gold"), dict(who=1, text="سول · ما تخلص حتى واحد برا", at=4.0, bg="red")]),
 ]),
 # ---------------------------------------------------------------- 09
 dict(audio="I.wav", text=T["I"], chapter="09 · اللائحة النهائية", src=S_HOME, items=[
   dict(k="chapter", num="09", title="اللائحة النهائية", at=0.1, until="قبل الزواج فإيطاليا"),
   dict(k="rows", at="قبل الزواج فإيطاليا", until="من بعد الزواج. تمنية", y=200, gap=90, size=42, rows=[
     ("الباسبور صالح", "1", "واحد: الباسبور"),
     ("النولا أوسطا · القنصلية", "2", "جوج: النولا"),
     ("التصديق فالبريفيتورا", "3", "تلاتة: التصديق"),
     ("الإعلان · تنبر 16 €", "4", "ربعة: الطلب"),
     ("جوج شهود", "5", "خمسة: جوج شهود"),
     ("الترجمان", "6", "ستة: الترجمان"),
     ("القاعة والأملاك", "7", "سبعة: القاعة"),
   ]),
   dict(k="rows", at="من بعد الزواج. تمنية", until="وعاود معايا الأرقام", y=240, gap=110, size=44, rows=[
     ("نسخة كاملة ديال العقد", "8", "تمنية: نسخة"),
     ("الترجمة والأبوستيي", "9", "تسعود: الترجمة"),
     ("الإيداع فالقنصلية · 3 شهور", "10", "عشرة: الإيداع", GOLD),
     ("الإشهاد الملحق", "11", "حداش: الإشهاد"),
     ("الدفتر العائلي", "12", "طناش: تحديث"),
   ]),
   dict(k="rows", at="وعاود معايا الأرقام", until="ونرجعو للتلاتة ديالنا", y=230, gap=100, size=44, rows=[
     ("السن · المادة 19", "18", "تمنطاش عام هو"),
     ("التعليق + التعرض", "8 + 3", "تمنية ديال الأيام ديال"),
     ("باش تتزوج", "180", "مية وتمانين يوم باش", RED),
     ("التنبر", "16 €", "سطاش أورو التنبر"),
     ("القنصلية · شهور", "3", "تلاتة ديال الشهور للقنصلية", GOLD),
     ("الجنسية مع إيطالي", "2 · 1", "جوج سنين، ولا عام"),
   ]),
   dict(k="rows", at="ونرجعو للتلاتة ديالنا", until="هند وكريم: الإعلان", y=300, gap=120, size=44, rows=[
     ("الإعلان", "1/3", "الإعلان من واحد مارس"),
     ("الزواج", "20/3", "الزواج نهار عشرين"),
     ("القنصلية قبل", "20/6", "والقنصلية قبل", GOLD),
   ]),
   dict(k="map", at="هند وكريم: الإعلان", until="ورشيد وسلمى:", box=L_BOX, **N_BO),
   dict(k="people", at="هند وكريم: الإعلان", until="ورشيد وسلمى:", box=R_BOX, people=["hijab", "man"],
        say=[dict(who=0, text="بيرميسو العائلة", at=2.5, bg="green"), dict(who=1, text="10/4/2029", at=5.5, bg="gold")]),
   dict(k="map", at="ورشيد وسلمى:", until="وإلى ما كانش عندك وقت", box=L_BOX, **MED_FES),
   dict(k="people", at="ورشيد وسلمى:", until="وإلى ما كانش عندك وقت", box=R_BOX, people=["worker", "woman"],
        say=[dict(who=0, text="التسجيل اختيار", at=2.5, bg="green"), dict(who=1, text="التجمع العائلي", at=6.0, bg="gold")]),
   dict(k="text", text="الفصل 04 · القنصلية", at="وإلى ما كانش عندك وقت", until="وتلاتة ديال النصائح", y=520, size=96, color=GOLD),
   dict(k="icons", at="وتلاتة ديال النصائح", until="وإلى كنتي كتوجد للعرس", box=ICB, items=[
     ["calendar", "القنصلية بكري", "green"], ["clipboard-check", "اللائحة ديال الكومون", "blue"], ["x", "ما تخلص حتى وسيط", "red"]], gap=4.0),
   dict(k="map", at="وإلى كنتي كتوجد للعرس", until="وفالدلائل الجاية", box=(160, 200, 1760, 880), **MED_BO),
   dict(k="people", at="وفالدلائل الجاية", until="والفصول ديال الفيديو", box=FULL, people=["woman", "child", "man"],
        say=[dict(who=1, text="الولاد · الوراق", at=2.0, bg="gold")]),
   dict(k="text", text="الفصول والمصادر فالوصف", at="والفصول ديال الفيديو", until="ودابا، سؤال ليك", y=600, size=64, color=GOLD),
   dict(k="people", at="ودابا، سؤال ليك", until="وإلى عرفتي شي واحد", box=FULL, people=["woman", "man"],
        say=[dict(who=0, text="إيه ولا لا؟", at=3.0, bg="green")]),
   dict(k="people", at="وإلى عرفتي شي واحد", until="وإلى عجبك", box=FULL, people=["worker", "hijab"],
        say=[dict(who=1, text="صيفطو لصاحبك", at=1.0, bg="gold")]),
   dict(k="cta", at="وإلى عجبك", text="ابوني فالقناة", sub="كل نهار دليل مفيد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("تزوجتي فالكومون؟", (236, 196, 96)), "سجل الزواج فالقنصلية", "الوراق والخطوات"],
  num="3 شهور", numsub="الأجل · القنصلية المغربية",
  bottom="مغاربة إيطاليا · دليل عملي بالدارجة",
)
