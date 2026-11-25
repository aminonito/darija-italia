import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_J1 = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-25-f.json"), encoding="utf-8"))
_J2 = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-25-r.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo2-2026-11-25-final")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = {k: v.replace("گ", "ك") for k, v in {**_J1["blocks"], **_J2["blocks"]}.items()}
# tagli audio: finali troncati dal TTS (H dopo "الباسبور الإيطالي.", I dopo "الدليل الجاي.")
T["H"] = T["H"].replace(" وكيبقى عندو حتى الباسبور المغربي.", "")
T["I"] = T["I"].replace(" شكرا على المتابعة، وتهلاو فراسكم.", "")

S_HOME = "مغاربة إيطاليا · دليل عملي بالدارجة"
S_REQ = "L. 91/1992 artt. 4 c. 2 e 14 · DL 36/2025 conv. L. 74/2025 (Normattiva) · DL 69/2013 art. 33 · ASGI"
S_IT = "ASGI scheda neomaggiorenni · Comune di Casalgrande · Min. Giustizia (nascita) · Comune di Sassari"
S_MA = "Code de la nationalité marocaine art. 6, 19 (adala.justice.gov.ma) · LesMRE (consulat.ma)"
S_STEP = "L. 91/1992 art. 4 c. 2 · DL 69/2013 art. 33 · ASGI · Comune di Casalgrande · calcoli nostri"
S_CASI = "L. 91/1992 artt. 4, 9, 14 · DL 36/2025 · Camera A.C. 2124-A (proposta, non legge)"
S_ERR = "DL 69/2013 art. 33 · ASGI · D.Lgs. 83/2026 (90 giorni)"
S_QA = "Fonti dei capitoli 01-07"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850); FULL = (160, 300, 1760, 860); MID = (260, 220, 1660, 840)
ICB = (160, 330, 1760, 860); VSB = (260, 220, 1660, 820); BARB = (160, 330, 1760, 840); BIGMAP = (160, 200, 1760, 880)

MED_BS = dict(view="med", hl=["ITA", "MAR"], route=["Casablanca", "Brescia", "plane"], pins=["Casablanca", "Brescia"], labels=False)
MED_BO = dict(view="med", hl=["ITA", "MAR"], route=["Tanger", "Bologna", "plane"], pins=["Tanger", "Bologna"], labels=False)
MED_TO = dict(view="med", hl=["ITA", "MAR"], route=["Fes", "Torino", "plane"], pins=["Fes", "Torino"], labels=False)
MED_MI = dict(view="med", hl=["ITA", "MAR"], route=["Casablanca", "Milano", "plane"], pins=["Casablanca", "Milano"], labels=False)
MAROC = dict(view="maroc", hl=["MAR"], pins=["Rabat"], labels=False)
N_BS = dict(view="north", pins=["Brescia"], labels=False)
N_TO = dict(view="north", pins=["Torino"], labels=False)
N_BO = dict(view="north", pins=["Bologna"], labels=False)
N_PD = dict(view="north", pins=["Padova"], labels=False)
N_GE = dict(view="north", pins=["Genova"], labels=False)
N_MI = dict(view="north", pins=["Milano"], labels=False)
S_NA = dict(view="south", pins=["Napoli"], labels=False)
S_BA = dict(view="south", pins=["Bari"], labels=False)
IT_ALL = dict(view="italy", pins=["Brescia", "Torino", "Bologna"], labels=False)

BLOCKS = [
 # ---------------------------------------------------------------- 01
 dict(audio="A.wav", text=T["A"], chapter="01 · شكون خاصو هاد الدليل", src=S_HOME, items=[
   dict(k="head", text="الجنسية الإيطالية للولاد", at=0.2, until="ولدك تزاد هنا فإيطاليا", sub="تزاد هنا · جا صغير · مع الواليد"),
   dict(k="people", at="ولدك تزاد هنا فإيطاليا", until="ولا بنتك جات صغيرة", box=FULL, people=["student", "woman"],
        say=[dict(who=0, text="عندي 17 عام", at=0.8, bg="gold"), dict(who=1, text="واش إيطالي؟", at=2.5, bg="green")]),
   dict(k="map", at="ولا بنتك جات صغيرة", until="ولا نتا ولا مراتك", box=BIGMAP, **MED_BO),
   dict(k="people", at="ولا نتا ولا مراتك", until="هاد الفيديو ليك", box=FULL, people=["man", "hijab", "child"],
        say=[dict(who=0, text="الجنسية ديالي", at=1.0, bg="gold"), dict(who=2, text="وأنا؟", at=4.0, bg="green")]),
   dict(k="vs", at="خاصنا نبداو بحاجة مهمة", until="أما الولد ديال الأجانب", box=VSB,
        right=dict(title="تزاد فإيطاليا", value="ماشي أوتوماتيكي", sub="من واليدين أجانب", icon="map-pin", color="red"),
        left=dict(title="الأب ولا الأم إيطالي", value="إيطالي", sub="بالدم", icon="users", color="green"), gap=6.0),
   dict(k="warn", text="عندو أجل محدود", at="أما الولد ديال الأجانب", until="فهاد الدليل غادي نشوفو جوج", y=560),
   dict(k="icons", at="فهاد الدليل غادي نشوفو جوج", until="ومن بعد، غادي نشوفو الجانب المغربي", box=ICB, items=[
     ["map-pin", "تزاد هنا · 18 عام", "green"], ["users", "مع الواليد · قاصر", "gold"]], gap=6.0),
   dict(k="map", at="ومن بعد، غادي نشوفو الجانب المغربي", until="وغادي نديرو الحساب", box=BIGMAP, **MAROC),
   dict(k="calendar", at="وغادي نديرو الحساب", until="وعندنا تلاتة ديال الحالات", box=MID, day=18, month="عام", sub="الحساب ديال التواريخ"),
   dict(k="text", text="تلاتة ديال الحالات", at="وعندنا تلاتة ديال الحالات", until="الحالة الأولى، ياسين", y=520, size=96, color=GOLD),
   dict(k="map", at="الحالة الأولى، ياسين", until="الحالة التانية، سلمى", box=L_BOX, **N_BS),
   dict(k="people", at="الحالة الأولى، ياسين", until="الحالة التانية، سلمى", box=R_BOX, people=["student"],
        say=[dict(who=0, text="ياسين · بريشا", at=1.0, bg="gold")]),
   dict(k="map", at="الحالة التانية، سلمى", until="والحالة التالتة، كريم", box=L_BOX, **N_TO),
   dict(k="people", at="الحالة التانية، سلمى", until="والحالة التالتة، كريم", box=R_BOX, people=["girl"],
        say=[dict(who=0, text="سلمى · تورينو", at=1.0, bg="gold")]),
   dict(k="map", at="والحالة التالتة، كريم", until="فهاد الدليل غادي نمشيو", box=L_BOX, **N_BO),
   dict(k="people", at="والحالة التالتة، كريم", until="فهاد الدليل غادي نمشيو", box=R_BOX, people=["man", "child", "girl"],
        say=[dict(who=0, text="كريم · بولونيا", at=1.0, bg="gold"), dict(who=2, text="جيت من المغرب", at=6.0, bg="green")]),
   dict(k="rows", at="فهاد الدليل غادي نمشيو", until="وكل معلومة فهاد الفيديو", y=215, gap=78, size=40, rows=[
     ("شكون خاصو هاد الدليل", "01", "الأول، شكون"),
     ("الشروط", "02", "التاني، الشروط"),
     ("الوراق فإيطاليا", "03", "التالت، الوراق"),
     ("المغرب والقنصلية", "04", "الرابع، الجانب"),
     ("الخطوات والثمن والمدة", "05", "الخامس، الخطوات"),
     ("الحالات الخاصة", "06", "السادس، الحالات"),
     ("الأخطاء", "07", "السابع، الأخطاء"),
     ("سؤال وجواب", "08", "التامن، سؤال"),
     ("اللائحة النهائية", "09", "والتاسع، لائحة"),
   ]),
   dict(k="icons", at="وكل معلومة فهاد الفيديو", until="وعقل مزيان", box=ICB, items=[
     ["scale", "قانون الجنسية", "blue"], ["building-bank", "الوزارات", "gold"], ["home", "الكومونات", "green"], ["file-text", "القانون المغربي", "blue"]], gap=2.0),
   dict(k="warn", text="محتوى إخباري · ماشي استشارة قانونية", at="وعقل مزيان", until="وحاجة أخيرة قبل ما نبداو", y=600),
   dict(k="people", at="وحاجة أخيرة قبل ما نبداو", until=None, box=FULL, people=["woman", "man"],
        say=[dict(who=0, text="كتب سؤالك", at=1.0, bg="green"), dict(who=1, text="صيفطو للعائلة", at=6.0, bg="gold")]),
 ]),
 # ---------------------------------------------------------------- 02
 dict(audio="B.wav", text=T["B"], chapter="02 · الشروط", src=S_REQ, items=[
   dict(k="chapter", num="02", title="الشروط بالتفصيل", at=0.1, until="القانون ديال الجنسية الإيطالية"),
   dict(k="big", text="91/1992", sub="قانون الجنسية الإيطالية · المادة 4", at="القانون ديال الجنسية الإيطالية", until="يعني عندنا تلاتة ديال الشروط"),
   dict(k="steps", at="يعني عندنا تلاتة ديال الشروط", until="ودابا الخبر المزيان", box=MID, steps=[
     ["تزاد فإيطاليا", "1"], ["الإقامة القانونية بلا انقطاع", "2"], ["الإعلان من 18 حتى 19", "3"]], gap=9.0, check_after=0.6),
   dict(k="map", at="الشرط الأول: يكون تزاد", until="الشرط التاني: الإقامة", box=L_BOX, **IT_ALL),
   dict(k="icons", at="والإقامة القانونية كتعني", until="والشرط التالت: الإعلان", box=ICB, items=[
     ["license", "البيرميسو", "blue"], ["home", "الريزيدينسا", "green"]], gap=3.0),
   dict(k="calendar", at="والشرط التالت: الإعلان", until="ودابا الخبر المزيان", box=R_BOX, day=1, month="عام", sub="من 18 حتى 19 عام"),
   dict(k="vs", at="ودابا الخبر المزيان", until="وشنو كيوقع إلى كانت", box=VSB,
        right=dict(title="المدخول", value="ما كاينش", sub="شرط", icon="cash", color="green"),
        left=dict(title="امتحان اللغة", value="ما كاينش", sub="شرط", icon="school", color="green"), gap=3.0),
   dict(k="people", at="وشنو كيوقع إلى كانت", until="هنا كاين قانون آخر", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="تعطلنا فالتجديد", at=1.5, bg="gold"), dict(who=1, text="والريزيدينسا؟", at=5.0, bg="blue")]),
   dict(k="big", text="33", sub="المادة · المرسوم 69/2013", at="هنا كاين قانون آخر", until="كيقول بلي الأخطاء"),
   dict(k="vs", at="كيقول بلي الأخطاء", until="يعني الشواهد ديال المدرسة", box=VSB,
        right=dict(title="غلط الواليدين", value="ما كيتحسبش", sub="على الولد", icon="users", color="green"),
        left=dict(title="غلط الإدارة", value="ما كيتحسبش", sub="على الولد", icon="building-bank", color="green"), gap=3.0),
   dict(k="icons", at="يعني الشواهد ديال المدرسة", until="ونفس المادة كتقول", box=ICB, items=[
     ["school", "المدرسة", "blue"], ["stethoscope", "التلقيح", "green"], ["building-hospital", "الطبيب", "gold"]], gap=1.5),
   dict(k="map", at="ونفس المادة كتقول", until="وإلى ما وصلاتش هاد الرسالة", box=L_BOX, **N_BS),
   dict(k="people", at="ونفس المادة كتقول", until="وإلى ما وصلاتش هاد الرسالة", box=R_BOX, people=["clerk"],
        say=[dict(who=0, text="رسالة مكتوبة", at=1.5, bg="blue"), dict(who=0, text="6 شهور قبل", at=6.0, bg="gold")]),
   dict(k="people", at="وإلى ما وصلاتش هاد الرسالة", until="دابا الطريق التانية", box=FULL, people=["student", "woman"],
        say=[dict(who=0, text="ما وصلاتنيش", at=1.0, bg="red"), dict(who=1, text="الحق كيبقى", at=4.5, bg="green")]),
   dict(k="head", text="الطريق التانية: مع الواليد", at="دابا الطريق التانية", until="المادة الربعطاش", sub="الولاد القاصرين"),
   dict(k="people", at="المادة الربعطاش", until="ولكن فعام ألفين وخمسة وعشرين", box=FULL, people=["man", "child", "girl"],
        say=[dict(who=0, text="خديت الجنسية", at=1.5, bg="gold"), dict(who=1, text="وحنا معاك", at=5.0, bg="green")]),
   dict(k="calendar", at="ولكن فعام ألفين وخمسة وعشرين", until="مثال بسيط", box=R_BOX, day=2, month="سنين", sub="الإقامة القانونية · 36/2025"),
   dict(k="map", at="ولكن فعام ألفين وخمسة وعشرين", until="مثال بسيط", box=L_BOX, **N_BO),
   dict(k="vs", at="مثال بسيط", until="وشي حاجة أخرى", box=VSB,
        right=dict(title="عام ونص · تزادت هنا", value="كتاخدها", sub="من الولادة", icon="heart", color="green"),
        left=dict(title="10 سنين · دخل عام هادي", value="لا", sub="أقل من جوج سنين", icon="plane", color="red"), gap=6.0),
   dict(k="people", at="وشي حاجة أخرى", until=None, box=FULL, people=["student"],
        say=[dict(who=0, text="القرار ليا من بعد", at=4.0, bg="gold")]),
 ]),
 # ---------------------------------------------------------------- 03
 dict(audio="C.wav", text=T["C"], chapter="03 · الوراق فإيطاليا", src=S_IT, items=[
   dict(k="chapter", num="03", title="الوراق فإيطاليا", at=0.1, until="المكان هو مكتب"),
   dict(k="map", at="المكان هو مكتب", until="وإلى ما لقيتيش موعد", box=L_BOX, **N_BS),
   dict(k="people", at="المكان هو مكتب", until="وإلى ما لقيتيش موعد", box=R_BOX, people=["student", "clerk"],
        say=[dict(who=0, text="باغي موعد", at=1.5, bg="gold"), dict(who=1, text="الحالة المدنية", at=4.0, bg="blue")]),
   dict(k="icons", at="وإلى ما لقيتيش موعد", until="دابا الوراق اللي كيطلبو", box=ICB, items=[
     ["mail", "الإيميل", "blue"], ["mailbox", "البيك", "green"], ["file-text", "دليل بلي طلبتي", "gold"]], gap=2.5),
   dict(k="steps", at="دابا الوراق اللي كيطلبو", until="وشنو هوما الوثائق", box=MID, steps=[
     ["عقد الازدياد ولا تصريح", "1"], ["الباسبور والبيرميسو", "2"], ["الدليل على الإقامة", "3"], ["الوصل ديال 250 €", "4"]], gap=8.0, check_after=0.6),
   dict(k="big", text="250 €", sub="لوزارة الداخلية", at="والوثيقة الرابعة: الوصل", until="وشنو هوما الوثائق"),
   dict(k="icons", at="وشنو هوما الوثائق", until="ونصيحة عملية", box=ICB, items=[
     ["license", "البيرميسوات", "blue"], ["stethoscope", "التلقيح", "green"], ["building-hospital", "السبيطار", "gold"], ["school", "المدرسة", "blue"]], gap=2.0),
   dict(k="people", at="ونصيحة عملية", until="ودير نسخ من كلشي", box=FULL, people=["hijab", "child"],
        say=[dict(who=0, text="ملف فالدار", at=1.5, bg="gold"), dict(who=1, text="كل عام", at=5.0, bg="green")]),
   dict(k="warn", text="نسخ · الأصول عندك", at="ودير نسخ من كلشي", until="دابا الطريق التانية، ديال الولاد", y=560),
   dict(k="head", text="الطريق التانية: الوراق", at="دابا الطريق التانية، ديال الولاد", until="وملي كيحلف الواليد", sub="الطلب ديال الواليد"),
   dict(k="steps", at="وملي كيحلف الواليد", until="الوراق اللي كتعاون هنا", box=MID, steps=[
     ["قاصر", "1"], ["ساكن مع الواليد", "2"], ["جوج سنين ديال الإقامة", "3"]], gap=3.0, check_after=0.6),
   dict(k="icons", at="الوراق اللي كتعاون هنا", until="وإلى كان شي ولد تزاد فالمغرب", box=ICB, items=[
     ["home", "شهادة العائلة", "green"], ["license", "البيرميسو ديال الولاد", "blue"], ["calendar", "تاريخ الدخول", "gold"]], gap=3.0),
   dict(k="map", at="وإلى كان شي ولد تزاد فالمغرب", until="ونرجعو للولادة هنا", box=BIGMAP, **MED_BO),
   dict(k="vs", at="التصريح بالولادة كيتدار", until="ومن بعد، سجل الولد", box=VSB,
        right=dict(title="السبيطار", value="3", sub="أيام", icon="building-hospital", color="green"),
        left=dict(title="الكومون", value="10", sub="أيام", icon="building-bank", color="gold"), gap=4.0),
   dict(k="people", at="ومن بعد، سجل الولد", until=None, box=FULL, people=["man", "woman", "child"],
        say=[dict(who=0, text="الريزيدينسا", at=1.0, bg="green"), dict(who=1, text="البيرميسو", at=3.5, bg="gold")]),
 ]),
 # ---------------------------------------------------------------- 04
 dict(audio="D.wav", text=T["D"], chapter="04 · المغرب والقنصلية", src=S_MA, items=[
   dict(k="chapter", num="04", title="المغرب والقنصلية", at=0.1, until="هاد الجزء مهم"),
   dict(k="people", at="هاد الجزء مهم", until="نبداو بالقانون المغربي", box=FULL, people=["elder", "woman"],
        say=[dict(who=0, text="غادي يضيع المغربية؟", at=3.0, bg="red")]),
   dict(k="map", at="نبداو بالقانون المغربي", until="يعني الولد اللي تزاد فإيطاليا من أب", box=BIGMAP, **MAROC),
   dict(k="big", text="6", sub="الفصل · قانون الجنسية المغربية", at="فالفصل السادس", until="يعني الولد اللي تزاد فإيطاليا من أب"),
   dict(k="vs", at="يعني الولد اللي تزاد فإيطاليا من أب", until="وحاجة مهمة للأمهات", box=VSB,
        right=dict(title="من أب مغربي", value="مغربي", sub="من الولادة", icon="user", color="green"),
        left=dict(title="من أم مغربية", value="مغربي", sub="من الولادة", icon="user", color="green"), gap=2.5),
   dict(k="people", at="وحاجة مهمة للأمهات", until="وواش كيضيع الجنسية المغربية", box=FULL, people=["hijab", "student"],
        say=[dict(who=0, text="قبل 2007؟", at=2.0, bg="gold"), dict(who=1, text="سول القنصلية", at=9.0, bg="blue")]),
   dict(k="steps", at="وواش كيضيع الجنسية المغربية", until="إذن ولدك يقدر يكون", box=MID, steps=[
     ["خدا جنسية أخرى", "1"], ["ما كيضيعش المغربية", "2"], ["غير بمرسوم من بعد طلب", "3"]], gap=4.0, check_after=0.6),
   dict(k="map", at="إذن ولدك يقدر يكون", until="وكاين حالة خاصة", box=BIGMAP, **MED_MI),
   dict(k="people", at="وكاين حالة خاصة", until="دابا الخطوة العملية", box=FULL, people=["student", "woman"],
        say=[dict(who=0, text="من 18 حتى 20", at=4.0, bg="gold"), dict(who=1, text="اختيار، ماشي واجب", at=8.0, bg="green")]),
   dict(k="head", text="تسجيل الولادة فالقنصلية", at="دابا الخطوة العملية", until="التصريح يقدر يديرو", sub="الحالة المدنية المغربية"),
   dict(k="map", at="التصريح يقدر يديرو", until="الوثائق اللي كتطلبها القنصلية", box=L_BOX, **MED_TO),
   dict(k="people", at="التصريح يقدر يديرو", until="الوثائق اللي كتطلبها القنصلية", box=R_BOX, people=["man", "clerk"],
        say=[dict(who=0, text="موعد أونلاين", at=3.0, bg="green"), dict(who=1, text="التصريح بالولادة", at=7.0, bg="blue")]),
   dict(k="icons", at="الوثائق اللي كتطلبها القنصلية", until="وإلى بغاو الترجمة", box=ICB, items=[
     ["file-text", "الدفتر العائلي", "gold"], ["file-certificate", "عقد الازدياد", "blue"], ["id", "البطاقة الوطنية", "green"], ["heart", "عقد الزواج", "gold"]], gap=1.8),
   dict(k="people", at="وإلى بغاو الترجمة", until="وإلى ما سجلتيهش فالوقت", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="الترجمة؟", at=0.8, bg="gold"), dict(who=1, text="سولي قبل", at=3.0, bg="blue")]),
   dict(k="vs", at="وإلى ما سجلتيهش فالوقت", until="ومن بعد التسجيل", box=VSB,
        right=dict(title="فالوقت", value="ساهل", sub="الوراق العادية", icon="clock", color="green"),
        left=dict(title="متأخر", value="ممكن", sub="وراق زايدين", icon="alert-triangle", color="gold"), gap=4.0),
   dict(k="icons", at="ومن بعد التسجيل", until="ونصيحة: ما تخليش", box=ICB, items=[
     ["e-passport", "الباسبور المغربي", "green"], ["license", "البيرميسو هنا", "blue"], ["plane", "السفر للمغرب", "gold"]], gap=4.0),
   dict(k="map", at="ونصيحة: ما تخليش", until=None, box=BIGMAP, **MED_BS),
 ]),
 # ---------------------------------------------------------------- 05
 dict(audio="E.wav", text=T["E"], chapter="05 · الخطوات والثمن والمدة", src=S_STEP, items=[
   dict(k="chapter", num="05", title="الخطوات والثمن والمدة", at=0.1, until="نبداو بالطريق الأولى"),
   dict(k="steps", at="نبداو بالطريق الأولى", until="ومن بعد، يقدر يطلب الكارطا", box=MID, steps=[
     ["رد البال على البوسطة", "1"], ["جمع الوراق", "2"], ["خلص 250 €", "3"], ["الموعد فالكومون", "4"], ["الإعلان", "5"], ["الكومون كيتحقق", "6"]], gap=7.5, check_after=0.6),
   dict(k="icons", at="ومن بعد، يقدر يطلب الكارطا", until="دابا الحساب مع ياسين", box=ICB, items=[
     ["id", "الكارطا الإيطالية", "green"], ["e-passport", "الباسبور الإيطالي", "blue"]], gap=2.0),
   dict(k="map", at="دابا الحساب مع ياسين", until="كمل تمنطاش عام نهار", box=BIGMAP, **N_BS),
   dict(k="calendar", at="كمل تمنطاش عام نهار", until="يعني آخر نهار باش يصرح", box=R_BOX, day=10, month=3, sub="2026 · 18 عام"),
   dict(k="people", at="كمل تمنطاش عام نهار", until="يعني آخر نهار باش يصرح", box=L_BOX, people=["student"],
        say=[dict(who=0, text="ياسين", at=0.5, bg="gold")]),
   dict(k="calendar", at="يعني آخر نهار باش يصرح", until="اليوم حنا", box=MID, day=10, month=3, sub="2027 · آخر نهار"),
   dict(k="big", text="105", sub="يوم باقيين · من 25 نونبر", at="اليوم حنا", until="هادا وقت كافي"),
   dict(k="people", at="هادا وقت كافي", until="والحساب مع سلمى", box=FULL, people=["student", "clerk"],
        say=[dict(who=0, text="الموعد هاد السيمانة", at=6.0, bg="green"), dict(who=1, text="مرحبا", at=9.0, bg="blue")]),
   dict(k="map", at="والحساب مع سلمى", until="الرسالة ديال الكومون خاصها", box=L_BOX, **N_TO),
   dict(k="calendar", at="والحساب مع سلمى", until="الرسالة ديال الكومون خاصها", box=R_BOX, day=2, month=9, sub="2027 · 18 عام"),
   dict(k="rows", at="الرسالة ديال الكومون خاصها", until="دابا الثمن.", y=260, gap=120, size=44, rows=[
     ("الرسالة ديال الكومون", "3/2027 - 9/2027", "الرسالة ديال الكومون"),
     ("الإعلان من", "2/9/2027", "والإعلان ممكن"),
     ("آخر نهار", "2/9/2028", "حتى لجوج شتنبر", GOLD),
   ]),
   dict(k="bars", at="دابا الثمن.", until="ودابا المدة", box=BARB, bars=[
     ["المساهمة الرسمية", 250, "250 €", "gold"], ["النسخ والشواهد", 40, "؟", "blue"]], gap=6.0),
   dict(k="people", at="ودابا المدة", until="ودابا الطريق التانية، مع كريم", box=FULL, people=["clerk", "office"],
        say=[dict(who=0, text="نفس النهار", at=2.0, bg="green"), dict(who=1, text="نتحققو قبل", at=5.5, bg="gold")]),
   dict(k="map", at="ودابا الطريق التانية، مع كريم", until="ولكن البنت ديالو ريم", box=L_BOX, **N_BO),
   dict(k="people", at="ودابا الطريق التانية، مع كريم", until="ولكن البنت ديالو ريم", box=R_BOX, people=["man", "child"],
        say=[dict(who=1, text="آدم · 2016", at=4.0, bg="gold"), dict(who=1, text="كياخدها", at=12.0, bg="green")]),
   dict(k="map", at="ولكن البنت ديالو ريم", until="إلى حلف كريم نهار", box=BIGMAP, **MED_BO),
   dict(k="bars", at="إلى حلف كريم نهار", until="إذن ريم ما كتاخدش", box=BARB, bars=[
     ["الشرط · سنين", 2.0, "2", "green"], ["ريم · سنين", 1.3, "1,3", "red"]], gap=4.0),
   dict(k="vs", at="إذن ريم ما كتاخدش", until=None, box=VSB,
        right=dict(title="آدم", value="إيطالي", sub="مع باه", icon="user", color="green"),
        left=dict(title="ريم", value="لا", sub="أقل من جوج سنين", icon="user", color="red"), gap=2.0),
 ]),
 # ---------------------------------------------------------------- 06
 dict(audio="F.wav", text=T["F"], chapter="06 · الحالات الخاصة", src=S_CASI, items=[
   dict(k="chapter", num="06", title="الحالات الخاصة", at=0.1, until="الحالة الأولى: الولد تزاد"),
   dict(k="people", at="الحالة الأولى: الولد تزاد", until="هنا كترجع المادة", box=FULL, people=["man", "woman", "child"],
        say=[dict(who=1, text="الريزيدينسا من 5 سنين", at=3.0, bg="red")]),
   dict(k="icons", at="هنا كترجع المادة", until="الحالة التانية: البيرميسو", box=ICB, items=[
     ["stethoscope", "التلقيح", "green"], ["heart", "طبيب الأطفال", "gold"], ["school", "الكريش", "blue"]], gap=3.0),
   dict(k="people", at="الحالة التانية: البيرميسو", until="الحالة التالتة: الولد تزاد", box=FULL, people=["worker", "clerk"],
        say=[dict(who=0, text="تعطلت فالتجديد", at=1.5, bg="gold"), dict(who=1, text="سول جمعية", at=9.0, bg="blue")]),
   dict(k="map", at="الحالة التالتة: الولد تزاد", until="هنا الإقامة تقطعات", box=BIGMAP, **MED_TO),
   dict(k="warn", text="الإقامة تقطعات · سول مختص", at="هنا الإقامة تقطعات", until="الحالة الرابعة: الولد جا صغير", y=560),
   dict(k="map", at="الحالة الرابعة: الولد جا صغير", until="عندو جوج ديال الإمكانيات", box=BIGMAP, **MED_MI),
   dict(k="vs", at="عندو جوج ديال الإمكانيات", until="الحالة الخامسة: الولد كبير", box=VSB,
        right=dict(title="مع الواليد", value="قاصر", sub="+ جوج سنين", icon="users", color="green"),
        left=dict(title="بوحدو ملي يكبر", value="10 سنين", sub="الإقامة + المدخول + اللغة", icon="user", color="gold"), gap=6.0),
   dict(k="people", at="الحالة الخامسة: الولد كبير", until="الحالة السادسة: الواليدين", box=FULL, people=["elder", "student"],
        say=[dict(who=0, text="خديت الجنسية", at=1.5, bg="gold"), dict(who=1, text="20 عام · بوحدي", at=4.5, bg="red")]),
   dict(k="people", at="الحالة السادسة: الواليدين", until="فهاد الحالات، الوراق", box=FULL, people=["man", "child", "woman"],
        say=[dict(who=0, text="الأب", at=2.0, bg="blue"), dict(who=2, text="ساكن معايا", at=4.0, bg="gold")]),
   dict(k="icons", at="فهاد الحالات، الوراق", until="الحالة السابعة: الولد ديال أم", box=ICB, items=[
     ["home", "السكنى", "green"], ["building-bank", "البريفيتورا", "blue"]], gap=3.0),
   dict(k="map", at="الحالة السابعة: الولد ديال أم", until="خاص غير تسجيل الولادة", box=BIGMAP, **MED_BS),
   dict(k="icons", at="خاص غير تسجيل الولادة", until="الحالة التامنة: المشروع", box=ICB, items=[
     ["building-bank", "الكومون الإيطالي", "blue"], ["file-text", "القنصلية المغربية", "gold"]], gap=2.5),
   dict(k="vs", at="الحالة التامنة: المشروع", until="ما تتسناش القانون الجديد", box=VSB,
        right=dict(title="القانون دابا", value="كيطبق", sub="91/1992", icon="scale", color="green"),
        left=dict(title="المشروع", value="ماشي قانون", sub="A.C. 2124-A", icon="file-text", color="gold"), gap=5.0),
   dict(k="warn", text="ما تتسناش القانون الجديد", at="ما تتسناش القانون الجديد", until="والحالة التاسعة", y=560),
   dict(k="map", at="والحالة التاسعة", until=None, box=BIGMAP, **MED_BS),
 ]),
 # ---------------------------------------------------------------- 07
 dict(audio="G.wav", text=T["G"], chapter="07 · الأخطاء", src=S_ERR, items=[
   dict(k="chapter", num="07", title="الأخطاء وشنو تدير", at=0.1, until="الغلط الأول، وهو الأخطر"),
   dict(k="people", at="الغلط الأول، وهو الأخطر", until="الغلط التاني: تظن", box=FULL, people=["student", "clerk"],
        say=[dict(who=0, text="عندي 19 عام", at=2.0, bg="gold"), dict(who=1, text="فات الأجل", at=5.0, bg="red")]),
   dict(k="vs", at="الغلط التاني: تظن", until="الغلط التالت: الريزيدينسا", box=VSB,
        right=dict(title="تزاد هنا", value="ماشي أوتوماتيكي", sub="خاص الإعلان", icon="x", color="red"),
        left=dict(title="المدرسة · الصحة", value="ما كيعطيوش", sub="الجنسية", icon="x", color="red"), gap=3.0),
   dict(k="map", at="الغلط التالت: الريزيدينسا", until="الغلط الرابع", box=L_BOX, **N_PD),
   dict(k="people", at="الغلط التالت: الريزيدينسا", until="الغلط الرابع", box=R_BOX, people=["man"],
        say=[dict(who=0, text="بدلت الدار", at=2.0, bg="red"), dict(who=0, text="والريزيدينسا؟", at=5.0, bg="gold")]),
   dict(k="icons", at="الغلط الرابع", until="الغلط الخامس", box=ICB, items=[
     ["school", "المدرسة", "blue"], ["stethoscope", "التلقيح", "green"], ["license", "البيرميسوات", "gold"]], gap=1.8),
   dict(k="calendar", at="الغلط الخامس", until="الغلط السادس", box=MID, day=90, month="يوم", sub="قبل ما يسالي البيرميسو"),
   dict(k="people", at="الغلط السادس", until="الغلط السابع", box=FULL, people=["man", "child"],
        say=[dict(who=0, text="حسب جوج سنين", at=3.0, bg="gold")]),
   dict(k="map", at="الغلط السابع", until="الغلط التامن", box=BIGMAP, **MED_MI),
   dict(k="people", at="الغلط التامن", until="الغلط التاسع", box=FULL, people=["office", "woman"],
        say=[dict(who=0, text="نسرع ليك؟", at=1.0, bg="red"), dict(who=1, text="لا · غير الكومون", at=4.0, bg="green")]),
   dict(k="warn", text="المشروع ماشي قانون · الأجل كيجري", at="الغلط التاسع", until="ودابا، شنو تدير", y=560),
   dict(k="steps", at="ودابا، شنو تدير", until="وإلى جاك الرفض", box=MID, steps=[
     ["ما كاينش موعد · رسالة بالبيك", "1"], ["ثغرة · وثائق المدرسة والصحة", "2"], ["المادة 33", "3"]], gap=8.0, check_after=0.6),
   dict(k="people", at="وإلى جاك الرفض", until="ونفس الشي للطريق التانية", box=FULL, people=["student", "office"],
        say=[dict(who=0, text="جاني الرفض", at=1.0, bg="red"), dict(who=1, text="القاضي · بسرعة", at=8.0, bg="gold")]),
   dict(k="map", at="ونفس الشي للطريق التانية", until="وتذكر: الأجل", box=L_BOX, **N_BO),
   dict(k="people", at="ونفس الشي للطريق التانية", until="وتذكر: الأجل", box=R_BOX, people=["man"],
        say=[dict(who=0, text="السبب بالكتابة", at=4.0, bg="gold")]),
   dict(k="big", text="19", sub="عام · آخر أجل عادي", at="وتذكر: الأجل", until=None),
 ]),
 # ---------------------------------------------------------------- 08
 dict(audio="H.wav", text=T["H"], chapter="08 · سؤال وجواب", src=S_QA, items=[
   dict(k="chapter", num="08", title="سؤال وجواب", at=0.1, until="السؤال الأول، من سارة"),
   dict(k="map", at="السؤال الأول، من سارة", until="الجواب: لا، ما كيوليش", box=L_BOX, **N_MI),
   dict(k="people", at="السؤال الأول، من سارة", until="الجواب: لا، ما كيوليش", box=R_BOX, people=["woman"],
        say=[dict(who=0, text="إيطالي بوحدو؟", at=1.5, bg="gold")]),
   dict(k="vs", at="الجواب: لا، ما كيوليش", until="السؤال التاني، من حمزة", box=VSB,
        right=dict(title="أوتوماتيكي", value="لا", sub="", icon="x", color="red"),
        left=dict(title="الإعلان", value="18 - 19", sub="عام", icon="building-bank", color="green"), gap=2.0),
   dict(k="map", at="السؤال التاني، من حمزة", until="الجواب: إلى ما وصلاتكش", box=L_BOX, **S_NA),
   dict(k="people", at="السؤال التاني، من حمزة", until="الجواب: إلى ما وصلاتكش", box=R_BOX, people=["student"],
        say=[dict(who=0, text="عندي 19 عام", at=1.0, bg="red")]),
   dict(k="people", at="الجواب: إلى ما وصلاتكش", until="السؤال التالت، من فاطمة", box=FULL, people=["clerk"],
        say=[dict(who=0, text="بلا رسالة · الحق كيبقى", at=2.0, bg="green")]),
   dict(k="map", at="السؤال التالت، من فاطمة", until="الجواب: البيرميسو ديال الواليدين", box=L_BOX, **N_PD),
   dict(k="people", at="السؤال التالت، من فاطمة", until="الجواب: البيرميسو ديال الواليدين", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="مكتوب معانا", at=3.0, bg="gold")]),
   dict(k="icons", at="الجواب: البيرميسو ديال الواليدين", until="السؤال الرابع، من يوسف", box=ICB, items=[
     ["license", "بيرميسو الواليدين", "blue"], ["home", "الريزيدينسا", "green"], ["school", "المدرسة", "gold"]], gap=2.0),
   dict(k="people", at="السؤال الرابع، من يوسف", until="الجواب: ميتين وخمسين", box=FULL, people=["worker"],
        say=[dict(who=0, text="شحال؟", at=1.5, bg="gold")]),
   dict(k="big", text="250 €", sub="لوزارة الداخلية", at="الجواب: ميتين وخمسين", until="السؤال الخامس، من خديجة"),
   dict(k="map", at="السؤال الخامس، من خديجة", until="الجواب: لا، فالطريق", box=L_BOX, **N_GE),
   dict(k="people", at="السؤال الخامس، من خديجة", until="الجواب: لا، فالطريق", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="امتحان؟ مدخول؟", at=2.0, bg="gold")]),
   dict(k="vs", at="الجواب: لا، فالطريق", until="السؤال السادس، من رشيد", box=VSB,
        right=dict(title="المدخول", value="لا", sub="", icon="cash", color="green"),
        left=dict(title="امتحان اللغة", value="لا", sub="", icon="school", color="green"), gap=2.0),
   dict(k="people", at="السؤال السادس، من رشيد", until="الجواب: لا. القانون المغربي", box=FULL, people=["man"],
        say=[dict(who=0, text="والمغربية؟", at=3.0, bg="gold")]),
   dict(k="map", at="الجواب: لا. القانون المغربي", until="السؤال السابع، من نادية", box=BIGMAP, **MED_TO),
   dict(k="map", at="السؤال السابع، من نادية", until="الجواب: بالقانون الجديد", box=L_BOX, **S_BA),
   dict(k="people", at="السؤال السابع، من نادية", until="الجواب: بالقانون الجديد", box=R_BOX, people=["woman", "girl"],
        say=[dict(who=1, text="عام هادي", at=4.0, bg="gold")]),
   dict(k="calendar", at="الجواب: بالقانون الجديد", until="السؤال التامن، من عبد الله", box=MID, day=2, month="سنين", sub="الإقامة القانونية"),
   dict(k="people", at="السؤال التامن، من عبد الله", until="الجواب: إلى حلفتي", box=FULL, people=["elder", "student"],
        say=[dict(who=1, text="17 عام", at=2.0, bg="gold")]),
   dict(k="vs", at="الجواب: إلى حلفتي", until="السؤال التاسع، من سلمى", box=VSB,
        right=dict(title="حلف الواليد قبل", value="مع الواليد", sub="قاصر + جوج سنين", icon="users", color="green"),
        left=dict(title="كمل 18 قبل", value="الإعلان", sub="تزاد وعاش هنا", icon="user", color="gold"), gap=8.0),
   dict(k="map", at="السؤال التاسع، من سلمى", until="الجواب: الغياب الطويل", box=BIGMAP, **MED_TO),
   dict(k="warn", text="الغياب الطويل · سول مختص", at="الجواب: الغياب الطويل", until="والسؤال العاشر", y=560),
   dict(k="people", at="والسؤال العاشر", until="الجواب: إيه، التسجيل", box=FULL, people=["man", "child"],
        say=[dict(who=0, text="متأخر؟", at=4.0, bg="gold")]),
   dict(k="people", at="الجواب: إيه، التسجيل", until="والسؤال الحادش", box=FULL, people=["clerk"],
        say=[dict(who=0, text="ممكن · وراق زايدين", at=1.0, bg="green")]),
   dict(k="map", at="والسؤال الحادش", until="الجواب: لا، ملي كيولي", box=L_BOX, **dict(view="italy", pins=["Perugia"], labels=False)),
   dict(k="people", at="والسؤال الحادش", until="الجواب: لا، ملي كيولي", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="باقي البيرميسو؟", at=3.0, bg="gold")]),
   dict(k="icons", at="الجواب: لا، ملي كيولي", until=None, box=ICB, items=[
     ["id", "الكارطا الإيطالية", "green"], ["e-passport", "الباسبور الإيطالي", "blue"]], gap=3.0),
 ]),
 # ---------------------------------------------------------------- 09
 dict(audio="I.wav", text=T["I"], chapter="09 · اللائحة النهائية", src=S_HOME, items=[
   dict(k="chapter", num="09", title="اللائحة النهائية", at=0.1, until="إلى عندك ولد تزاد فإيطاليا"),
   dict(k="rows", at="إلى عندك ولد تزاد فإيطاليا", until="وإلى كنتي غادي تاخد", y=200, gap=90, size=42, rows=[
     ("التصريح بالولادة", "1", "واحد: صرح"),
     ("الريزيدينسا", "2", "جوج: سجلو"),
     ("البيرميسو فالوقت", "3", "تلاتة: البيرميسو"),
     ("القنصلية والباسبور", "4", "ربعة: سجل"),
     ("ملف فالدار", "5", "خمسة: ملف"),
     ("الرسالة ديال الكومون", "6", "ستة: ملي"),
     ("الإعلان · 250 €", "7", "سبعة: من", GOLD),
   ]),
   dict(k="rows", at="وإلى كنتي غادي تاخد", until="وعاود معايا الأرقام", y=280, gap=120, size=44, rows=[
     ("نفس الريزيدينسا", "8", "تمنية: تأكد"),
     ("جوج سنين لكل ولد", "9", "تسعود: حسب", GOLD),
     ("الراشد · طريق ديالو", "10", "وعشرة: الولد"),
   ]),
   dict(k="rows", at="وعاود معايا الأرقام", until="ونرجعو للتلاتة ديالنا", y=230, gap=100, size=44, rows=[
     ("البداية · عام", "18", "تمنطاش عام هو"),
     ("آخر أجل عادي · عام", "19", "تسعطاش عام هو", RED),
     ("الرسالة · شهور قبل", "6", "ستة ديال الشهور قبل"),
     ("الثمن", "250 €", "ميتين وخمسين أورو هو"),
     ("الإقامة مع الواليد · سنين", "2", "جوج سنين ديال الإقامة للولاد", GOLD),
     ("الولادة · أيام", "3 · 10", "وتلاتة وعشرة"),
   ]),
   dict(k="rows", at="ونرجعو للتلاتة ديالنا", until="وإلى كنتي مغربي", y=300, gap=130, size=44, rows=[
     ("ياسين · آخر نهار", "10/3/2027", "ياسين فبريشا", RED),
     ("سلمى · من", "2/9/2027", "سلمى فتورينو"),
     ("كريم · آدم نعم · ريم لا", "2016 · 2026", "وكريم فبولونيا", GOLD),
   ]),
   dict(k="map", at="وإلى كنتي مغربي", until="وتلاتة ديال النصائح", box=BIGMAP, **MED_BS),
   dict(k="icons", at="وتلاتة ديال النصائح", until="وإلى عندك شي حالة صعيبة", box=ICB, items=[
     ["calendar", "ما تتسناش", "green"], ["mail", "كلشي بالكتابة", "blue"], ["x", "ما تخلص حتى وسيط", "red"]], gap=4.0),
   dict(k="people", at="وإلى عندك شي حالة صعيبة", until="والفصول ديال الفيديو", box=FULL, people=["office", "woman"],
        say=[dict(who=0, text="جمعية · باترونا", at=2.0, bg="green"), dict(who=1, text="شنو ناقص؟", at=8.0, bg="gold")]),
   dict(k="text", text="الفصول والمصادر فالوصف", at="والفصول ديال الفيديو", until="ودابا، سؤال ليك", y=600, size=64, color=GOLD),
   dict(k="people", at="ودابا، سؤال ليك", until="وإلى عرفتي شي واحد", box=FULL, people=["student", "woman"],
        say=[dict(who=1, text="إيه ولا لا؟", at=3.0, bg="green")]),
   dict(k="people", at="وإلى عرفتي شي واحد", until="وإلى عجبك", box=FULL, people=["man", "hijab"],
        say=[dict(who=1, text="صيفطو للعائلة", at=1.0, bg="gold")]),
   dict(k="cta", at="وإلى عجبك", text="ابوني فالقناة", sub="كل نهار دليل مفيد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("تزاد ولدك فإيطاليا؟", (236, 196, 96)), "الجنسية الإيطالية", "قبل ما يفوت الأجل"],
  num="18", numsub="عام · الإعلان فالكومون",
  bottom="مغاربة إيطاليا · دليل عملي بالدارجة",
)
