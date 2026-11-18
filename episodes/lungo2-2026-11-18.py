import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-18.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo2-2026-11-18-final")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = {k: v.replace("گ", "ك") for k, v in JOB["blocks"].items()}
# tagli nell'audio finale (finali troncati dal TTS)
T["C"] = T["C"].replace("فالأخطاء، حيت فيه عقوبات.", "فالأخطاء.")
T["H"] = T["H"].replace(" وإلى عندك سؤال آخر، كتبو فالكومونتير.", "")

S_HOME = "مغاربة إيطاليا · دليل عملي بالدارجة"
S_REQ = "Enac Informa NASpI 2026 · LentePubblica · Assolombarda"
S_DOC = "Enac Informa · LentePubblica · INPS / patronati"
S_PDS = "Assolombarda · Edotto (attesa occupazione) · InformazioneFiscale · Fiscozen"
S_CAL = "Enac Informa NASpI 2026 · LentePubblica (1.456,72 € · 1.584,70 €)"
S_CAS = "Money.it · LeggeInChiaro · Centro Fiscale · PartitaIva.it · Enac Informa"
S_ERR = "Money.it · Fiscozen · LeggeInChiaro · OrizzonteScuola · LentePubblica"
S_QA = "Fonti dei capitoli 01-06"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850); FULL = (160, 300, 1760, 860); MID = (260, 220, 1660, 840)

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="01 · شكون كيحتاج النازبي", src=S_HOME, items=[
   dict(k="head", text="النازبي خطوة بخطوة", at=0.2, until="وباش تعرف من الأول", sub="التعويض على البطالة ديال الإينبس"),
   dict(k="people", at=0.6, until="وباش تعرف من الأول", box=FULL, people=["worker", "hijab", "man"],
        say=[dict(who=0, text="طاحت عليا الخدمة", at=0.8), dict(who=1, text="واش عندي الحق؟", at=3.0)]),
   dict(k="big", text="1.153 €", at="وباش تعرف من الأول", until="شكون كيحتاج هاد الدليل؟", y=450, size=230, color=GOLD, sub="مثال حميد · خام فالشهر · تقريبا 17 شهر"),
   dict(k="map", view="north", pins=["Torino", "Bologna", "Bergamo"], labels=False, at="شكون كيحتاج هاد الدليل؟", until="حميد، عايش فطورينو", box=(160, 200, 1760, 880)),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="حميد، عايش فطورينو", until="خديجة، عايشة فبولونيا", box=L_BOX),
   dict(k="people", at="حميد، عايش فطورينو", until="خديجة، عايشة فبولونيا", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="الكونطرا سالات", at=1.0, bg="gold")]),
   dict(k="map", view="north", pins=["Bologna"], labels=False, at="خديجة، عايشة فبولونيا", until="ويوسف، عايش فبيرغامو", box=L_BOX),
   dict(k="people", at="خديجة، عايشة فبولونيا", until="ويوسف، عايش فبيرغامو", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="الشركة سدات", at=1.0, bg="red")]),
   dict(k="map", view="north", pins=["Bergamo"], labels=False, at="ويوسف، عايش فبيرغامو", until="التلاتة كيسولو", box=L_BOX),
   dict(k="people", at="ويوسف، عايش فبيرغامو", until="التلاتة كيسولو", box=R_BOX, people=["man"],
        say=[dict(who=0, text="بدلت الخدمة...", at=1.0)]),
   dict(k="people", at="التلاتة كيسولو", until="النازبي هي فلوس", box=FULL, people=["worker", "hijab", "man"],
        say=[dict(who=0, text="شحال غادي ناخد؟", at=0.6), dict(who=2, text="فوقاش نطلبها؟", at=2.2, bg="gold")]),
   dict(k="icons", at="النازبي هي فلوس", until="وعلاش هاد الموضوع", box=(160, 330, 1760, 860), items=[
     ["cash", "فلوس كل شهر", "green"], ["building-bank", "من الإينبس", "blue"], ["briefcase", "حق ماشي صدقة", "gold"]], gap=2.5),
   dict(k="map", view="italy", pins=["Torino", "Bologna", "Bergamo", "Napoli", "Bari"], labels=False, at="وعلاش هاد الموضوع", until="فهاد الفيديو غادي", box=L_BOX),
   dict(k="icons", at="وعلاش هاد الموضوع", until="فهاد الفيديو غادي", box=R_BOX, items=[
     ["tool", "البني", "gold"], ["tractor", "الفلاحة", "green"], ["building-factory", "المعامل", "blue"]], gap=1.5),
   dict(k="rows", at="فهاد الفيديو غادي", until="قبل ما نبداو، جوج", y=215, gap=78, size=40, rows=[
     ("شكون عندو الحق", "01", "الأول، شكون"),
     ("الشروط", "02", "التاني، الشروط"),
     ("الوراق والطلب", "03", "التالت، الوراق"),
     ("البيرميسو والمغرب", "04", "الرابع، البيرميسو"),
     ("الحساب", "05", "الخامس، الحساب"),
     ("الحالات الخاصة", "06", "السادس، الحالات"),
     ("الأخطاء والريكورس", "07", "السابع، الأخطاء"),
     ("سؤال وجواب", "08", "التامن، سؤال"),
     ("الملخص", "09", "والتاسع، الملخص"),
   ]),
   dict(k="icons", at="قبل ما نبداو، جوج", until="والأرقام اللي غادي نعطيو", box=(160, 330, 1760, 860), items=[
     ["file-certificate", "جوج مصادر", "green"], ["alert-triangle", "ماشي استشارة قانونية", "gold"], ["users", "الباطرونا", "blue"]], gap=2.5),
   dict(k="people", at="والأرقام اللي غادي نعطيو", box=FULL, people=["clerk", "worker"],
        say=[dict(who=0, text="شكون عندو الحق؟", at=3.0, bg="green")]),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="02 · الشروط", src=S_REQ, items=[
   dict(k="chapter", num="02", title="الشروط", at=0.1, until="الشرط الأول: تكون"),
   dict(k="steps", at="الشرط الأول: تكون", until="كاين جوج ديال الاستثناءات", box=L_BOX, steps=[
     ["الطرد", "1"], ["الكونطرا سالات", "2"], ["الشركة سدات", "3"]], gap=1.6, check_after=0.6),
   dict(k="people", at="الشرط الأول: تكون", until="كاين جوج ديال الاستثناءات", box=R_BOX, people=["office"],
        say=[dict(who=0, text="الاستقالة العادية: لا", at=9.0, bg="red")]),
   dict(k="vs", at="كاين جوج ديال الاستثناءات", until="الشرط التاني: الكوتيزاسيون", box=(260, 220, 1660, 820),
        right=dict(title="الجوستا كاوزا", value="إيه", sub="سبب قوي", icon="scale", color="green"),
        left=dict(title="الولادة", value="إيه", sub="الأم ولا الأب", icon="baby-carriage", color="green"), gap=3.0),
   dict(k="big", text="13", at="الشرط التاني: الكوتيزاسيون", until="مثال: خديجة فبولونيا", y=430, size=280, color=GOLD, sub="سيمانة ديال الكوتيزاسيون فالربع سنين"),
   dict(k="map", view="north", pins=["Bologna"], labels=False, at="مثال: خديجة فبولونيا", until="وحميد فطورينو؟", box=L_BOX),
   dict(k="people", at="مثال: خديجة فبولونيا", until="وحميد فطورينو؟", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="عامين ديال الخدمة", at=1.0, bg="green")]),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="وحميد فطورينو؟", until="ودابا القاعدة الجديدة", box=L_BOX),
   dict(k="people", at="وحميد فطورينو؟", until="ودابا القاعدة الجديدة", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="150 سيمانة", at=4.0, bg="green")]),
   dict(k="calendar", at="ودابا القاعدة الجديدة", until="وهادي هي الحالة ديال يوسف", box=R_BOX, day=1, month=1, sub="2025 · قاعدة التلطاش سيمانة"),
   dict(k="steps", at="ودابا القاعدة الجديدة", until="وهادي هي الحالة ديال يوسف", box=L_BOX, steps=[
     ["خرجتي بإرادتك", "1"], ["خدمة جديدة", "2"], ["13 سيمانة", "3"]], gap=4.0, check_after=0.6),
   dict(k="map", view="north", pins=["Bergamo"], labels=False, at="وهادي هي الحالة ديال يوسف", until="عشرة أقل من تلطاش", box=L_BOX),
   dict(k="people", at="وهادي هي الحالة ديال يوسف", until="عشرة أقل من تلطاش", box=R_BOX, people=["man"],
        say=[dict(who=0, text="جراو عليا فيونيو", at=4.0)]),
   dict(k="bars", at="عشرة أقل من تلطاش", until="علاش دارو هاد القاعدة", box=(160, 330, 1760, 840), bars=[
     ["يوسف", 10, "10", "red"], ["الشرط", 13, "13", "green"]], gap=1.5),
   dict(k="people", at="علاش دارو هاد القاعدة", until="إذن، باش تلخص الشروط", box=FULL, people=["clerk", "man"],
        say=[dict(who=0, text="باش ما يكونش التحايل", at=1.0, bg="gold"), dict(who=1, text="نرد البال", at=6.0, bg="green")]),
   dict(k="icons", at="إذن، باش تلخص الشروط", box=(160, 330, 1760, 860), items=[
     ["briefcase", "بلا ما تبغي", "red"], ["calendar", "13 سيمانة", "gold"], ["alert-triangle", "قاعدة الاستقالة", "red"]], gap=2.5),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="03 · الوراق والطلب", src=S_DOC, items=[
   dict(k="chapter", num="03", title="الوراق والطلب", at=0.1, until="الخبر المزيان"),
   dict(k="people", at="الخبر المزيان", until="واحد: السبيد", box=FULL, people=["clerk"],
        say=[dict(who=0, text="الإينبس عندها الكوتيزاسيون", at=1.5, bg="green")]),
   dict(k="icons", at="واحد: السبيد", until="ربعة: البيرميسو", box=(160, 330, 1760, 860), items=[
     ["fingerprint", "السبيد ولا الكارطا", "blue"], ["id", "الكودشي فيسكالي", "green"], ["credit-card", "الإيبان باسمك", "gold"]], gap=5.0),
   dict(k="warn", text="الإيبان خاصو يكون باسمك", at="هنا كاين غلط", until="ربعة: البيرميسو", y=860),
   dict(k="icons", at="ربعة: البيرميسو", until="وإلى كنتي خدام عند بزاف", box=(160, 330, 1760, 860), items=[
     ["e-passport", "البيرميسو ولا الريسيفوتا", "green"], ["file-text", "ورقة نهاية الخدمة", "gold"], ["receipt", "البوستات باغا", "blue"]], gap=5.0),
   dict(k="people", at="وإلى كنتي خدام عند بزاف", until="ستة: العنوان", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="خدمت عند تلاتة ديال المعلمين", at=0.8), dict(who=1, text="الإينبس كتجمعها", at=4.0, bg="green")]),
   dict(k="icons", at="ستة: العنوان", until="دابا كيفاش دير الطلب؟", box=(160, 330, 1760, 860), items=[
     ["home", "العنوان", "blue"], ["phone", "التيليفون", "green"], ["mail", "الإيميل", "gold"]], gap=1.5),
   dict(k="vs", at="دابا كيفاش دير الطلب؟", until="وفي جميع الحالات", box=(260, 220, 1660, 820),
        right=dict(title="بوحدك", value="أونلاين", sub="الموقع ولا التطبيق", icon="phone", color="blue"),
        left=dict(title="الباطرونا", value="معاك", sub="كيصيفطو الطلب", icon="users", color="green"), gap=6.0),
   dict(k="big", text="68", at="وفي جميع الحالات", until="والمزيان أنك تطلب بكري", y=430, size=300, color=RED, sub="يوم من نهاية الخدمة · آخر أجل"),
   dict(k="steps", at="والمزيان أنك تطلب بكري", until="خلينا نحسبو مع حميد", box=MID, steps=[
     ["الطلب فـ8 أيام الأولى", "8"], ["الطلب من بعد", "+1"]], gap=6.0, check_after=0.6),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="خلينا نحسبو مع حميد", until="إلى صيفط الطلب قبل", box=L_BOX),
   dict(k="people", at="خلينا نحسبو مع حميد", until="إلى صيفط الطلب قبل", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="سالات 31/12", at=1.0, bg="gold")]),
   dict(k="steps", at="إلى صيفط الطلب قبل", until="ومن بعد ما تصيفط الطلب", box=MID, steps=[
     ["نهاية الكونطرا", "31/12"], ["النازبي كتبدا", "8/1"], ["آخر أجل", "9/3"]], gap=3.0, check_after=0.6),
   dict(k="icons", at="ومن بعد ما تصيفط الطلب", until="وحاجة مهمة: الطلب ديال النازبي", box=(160, 330, 1760, 860), items=[
     ["receipt", "الإيصال", "green"], ["check", "واش تقبل", "blue"], ["coin-euro", "المبلغ", "gold"]], gap=2.0),
   dict(k="map", view="italy", pins=["Torino", "Roma", "Bari"], labels=False, at="وحاجة مهمة: الطلب ديال النازبي", box=L_BOX),
   dict(k="people", at="وحاجة مهمة: الطلب ديال النازبي", box=R_BOX, people=["office"],
        say=[dict(who=0, text="غادي نعيطو ليك", at=6.0, bg="gold")]),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="04 · البيرميسو والمغرب", src=S_PDS, items=[
   dict(k="chapter", num="04", title="البيرميسو والسفر للمغرب", at=0.1, until="هادي أسئلة كتجينا"),
   dict(k="people", at="هادي أسئلة كتجينا", until="نبداو بالبيرميسو", box=FULL, people=["man", "hijab"],
        say=[dict(who=0, text="البيرميسو كيطيح؟", at=1.5), dict(who=1, text="نقدر نمشي للمغرب؟", at=4.5, bg="gold")]),
   dict(k="vs", at="نبداو بالبيرميسو", until="وملي يجي وقت التجديد", box=(260, 220, 1660, 820),
        right=dict(title="الخدمة", value="طاحت", sub="طرد ولا استقالة", icon="briefcase", color="red"),
        left=dict(title="البيرميسو", value="باقي", sub="ما كيتسحبش", icon="id", color="green"), gap=3.0),
   dict(k="big", text="1", at="وملي يجي وقت التجديد", until="وإلى كانت النازبي ديالك", y=430, size=300, color=GREEN, sub="عام على الأقل · انتظار الخدمة"),
   dict(k="bars", at="وإلى كانت النازبي ديالك", until="ولكن ما تبقاش مرتاح", box=(160, 330, 1760, 840), bars=[
     ["الأقل", 12, "12", "grey"], ["مثال حميد", 17, "17", "green"]], gap=1.5),
   dict(k="people", at="ولكن ما تبقاش مرتاح", until="وإلى كانت عندك الكارطا", box=FULL, people=["clerk", "worker"],
        say=[dict(who=0, text="بين المدخول", at=1.5, bg="gold"), dict(who=1, text="نقلب على خدمة", at=5.0, bg="green")]),
   dict(k="text", text="الكارطا ديال المدة الطويلة: إقامة دائمة", at="وإلى كانت عندك الكارطا", until="مثال: حميد فطورينو، البيرميسو", y=520, size=64),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="مثال: حميد فطورينو، البيرميسو", until="دابا السفر", box=L_BOX),
   dict(k="steps", at="مثال: حميد فطورينو، البيرميسو", until="دابا السفر", box=R_BOX, steps=[
     ["البيرميسو كيسالي", "1"], ["انتظار الخدمة", "2"], ["الباطرونا", "3"]], gap=3.0, check_after=0.6),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Bologna", "Nador", "plane"], pins=["Bologna", "Nador"], labels=False,
        at="دابا السفر", until="ولكن، وهادي مهمة بزاف", box=(160, 200, 1760, 880)),
   dict(k="people", at="ولكن، وهادي مهمة بزاف", until="مثال: خديجة فالنازبي", box=R_BOX, people=["office"],
        say=[dict(who=0, text="خاصك تكون حاضر", at=2.0, bg="red")]),
   dict(k="steps", at="ولكن، وهادي مهمة بزاف", until="مثال: خديجة فالنازبي", box=L_BOX, steps=[
     ["كينقصو", "1"], ["كتحبس", "2"], ["كتضيع", "3"]], gap=3.0, check_after=0.6),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Bologna", "Nador", "plane"], pins=["Nador"], labels=False,
        at="مثال: خديجة فالنازبي", until="تعطيهم إيميل", box=L_BOX),
   dict(k="people", at="مثال: خديجة فالنازبي", until="تعطيهم إيميل", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="شهر فنادور", at=1.0, bg="green")]),
   dict(k="icons", at="تعطيهم إيميل", until="وإلى بغيتي ترجع تستقر", box=(160, 330, 1760, 860), items=[
     ["mail", "إيميل", "blue"], ["phone", "تيليفون", "green"], ["mailbox", "البوسطا فالموقع", "gold"]], gap=2.0),
   dict(k="map", view="med", hl=["MAR"], pins=["Casablanca", "Oujda"], labels=False, at="وإلى بغيتي ترجع تستقر", until="وحاجة صغيرة ولكن", box=L_BOX),
   dict(k="people", at="وإلى بغيتي ترجع تستقر", until="وحاجة صغيرة ولكن", box=R_BOX, people=["elder"],
        say=[dict(who=0, text="سول قبل ما تقرر", at=3.0, bg="gold")]),
   dict(k="icons", at="وحاجة صغيرة ولكن", until="إذن الملخص ديال هاد الفصل", box=(160, 330, 1760, 860), items=[
     ["home", "العنوان الجديد", "blue"], ["phone", "التيليفون الجديد", "green"]], gap=2.0),
   dict(k="rows", at="إذن الملخص ديال هاد الفصل", y=330, gap=130, size=54, rows=[
     ("الخدمة طاحت", "باقي", "الخدمة طاحت، البيرميسو"),
     ("انتظار الخدمة", "12", "وملي تجدد، كاين"),
     ("السفر للمغرب", "ممكن", "والسفر للمغرب ممكن"),
   ]),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="05 · الحساب", src=S_CAL, items=[
   dict(k="chapter", num="05", title="شحال غادي تشد؟", at=0.1, until="الإينبس كتحسب أولا"),
   dict(k="steps", at="الإينبس كتحسب أولا", until="من بعد، كاين حد مهم", box=MID, steps=[
     ["الخلاصة الخام", "1"], ["قسمة على السيمانات", "2"], ["الخلاصة المتوسطة", "3"]], gap=3.0, check_after=0.6),
   dict(k="big", text="1.456 €", at="من بعد، كاين حد مهم", until="إلى كانت الخلاصة المتوسطة ديالك تحت", y=430, size=220, color=GOLD, sub="الحد ديال 2026"),
   dict(k="vs", at="إلى كانت الخلاصة المتوسطة ديالك تحت", until="وكاين سقف", box=(260, 220, 1660, 820),
        right=dict(title="تحت الحد", value="75%", sub="من الخلاصة", icon="percentage", color="green"),
        left=dict(title="فوق الحد", value="25%", sub="من الفرق", icon="trending-up", color="gold"), gap=4.0),
   dict(k="big", text="1.584 €", at="وكاين سقف", until="نحسبو مع خديجة", y=430, size=220, color=RED, sub="السقف · خام فالشهر"),
   dict(k="map", view="north", pins=["Bologna"], labels=False, at="نحسبو مع خديجة", until="ودابا حميد", box=L_BOX),
   dict(k="steps", at="نحسبو مع خديجة", until="ودابا حميد", box=R_BOX, steps=[
     ["الخلاصة", "1.000 €"], ["النازبي", "750 €"]], gap=4.0, check_after=0.6),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="ودابا حميد", until="المجموع: ألف", box=L_BOX),
   dict(k="steps", at="ودابا حميد", until="ولاحظ: حتى إلى كانت", box=R_BOX, steps=[
     ["حصة من الحد", "1.092 €"], ["حصة من الفرق", "61 €"], ["المجموع", "1.153 €"]], gap=4.0, check_after=0.6),
   dict(k="bars", at="ولاحظ: حتى إلى كانت", until="شحال من شهر؟", box=(160, 330, 1760, 840), bars=[
     ["خديجة", 750, "750 €", "grey"], ["حميد", 1153, "1.153 €", "green"], ["3.000 €", 1478, "1.478 €", "gold"]], gap=1.5),
   dict(k="people", at="شحال من شهر؟", until="حميد عندو مية", box=FULL, people=["office", "worker"],
        say=[dict(who=1, text="شحال من شهر؟", at=0.3), dict(who=0, text="نص السيمانات", at=3.0, bg="green")]),
   dict(k="bars", at="حميد عندو مية", until="وكاين حاجة خاصك تعرفها", box=(160, 330, 1760, 840), bars=[
     ["حميد", 75, "75", "green"], ["خديجة", 52, "52", "gold"], ["الأقصى", 104, "24 شهر", "grey"]], gap=2.5),
   dict(k="big", text="3%", at="وكاين حاجة خاصك تعرفها", until="حميد كيشد ألف", x=1380, y=430, size=220, color=RED, sub="كل شهر من الشهر السادس"),
   dict(k="people", at="وكاين حاجة خاصك تعرفها", until="حميد كيشد ألف", box=L_BOX, people=["clerk"],
        say=[dict(who=0, text="كينقص شوية بشوية", at=3.0, bg="gold")]),
   dict(k="bars", at="حميد كيشد ألف", until="مثال تالت: سعيد", box=(160, 330, 1760, 840), bars=[
     ["الشهور الأولى", 1153, "1.153 €", "green"], ["الشهر السادس", 1119, "1.119 €", "gold"]], gap=2.0),
   dict(k="map", view="south", pins=["Napoli"], labels=False, at="مثال تالت: سعيد", until="علاش هاد الحساب مهم؟", box=L_BOX),
   dict(k="people", at="مثال تالت: سعيد", until="علاش هاد الحساب مهم؟", box=R_BOX, people=["elder"],
        say=[dict(who=0, text="900 € حتى للشهر 8", at=6.0, bg="green")]),
   dict(k="icons", at="علاش هاد الحساب مهم؟", until="والنصيحة: من بعد", box=(160, 330, 1760, 860), items=[
     ["home-dollar", "الكرا", "blue"], ["bolt", "الفاتورات", "gold"], ["world", "الفلوس للمغرب", "green"]], gap=3.0),
   dict(k="people", at="والنصيحة: من بعد", until="إذن تلاتة ديال الأرقام", box=FULL, people=["worker", "clerk"],
        say=[dict(who=0, text="نشوف الحساب فالموقع", at=1.0, bg="green")]),
   dict(k="rows", at="إذن تلاتة ديال الأرقام", y=330, gap=130, size=54, rows=[
     ("من الخلاصة", "75%", "إذن تلاتة"),
     ("السقف خام", "1.584 €", "السقف ديال"),
     ("الأقصى", "24", "ونص السيمانات"),
   ]),
 ]),
 dict(audio="F.wav", text=T["F"], chapter="06 · الحالات الخاصة", src=S_CAS, items=[
   dict(k="chapter", num="06", title="ستة ديال الحالات الخاصة", at=0.1, until="الحالة الأولى: الجوستا"),
   dict(k="people", at="الحالة الأولى: الجوستا", until="هنا عندك الحق", box=R_BOX, people=["woman"],
        say=[dict(who=0, text="ما خلصونيش شهور", at=4.0, bg="red")]),
   dict(k="icons", at="أشهر الأسباب", until="هنا عندك الحق", box=L_BOX, items=[
     ["cash", "الخلاصة", "red"], ["alert-triangle", "التحرش", "red"], ["scale", "شروط تبدلات", "gold"]], gap=4.0),
   dict(k="icons", at="هنا عندك الحق", until="والاستقالة كتدار أونلاين", box=(160, 330, 1760, 860), items=[
     ["receipt", "البوستات باغا", "gold"], ["mail", "الإيميلات", "blue"], ["users", "الشهود", "green"]], gap=2.0),
   dict(k="warn", text="الاستقالة أونلاين: اختار الجوستا كاوزا", at="والاستقالة كتدار أونلاين", until="وقبل ما تستقيل", y=520),
   dict(k="map", view="italy", pins=["Torino", "Roma", "Napoli"], labels=False, at="وقبل ما تستقيل", until="الحالة التانية: الأم", box=L_BOX),
   dict(k="people", at="وقبل ما تستقيل", until="الحالة التانية: الأم", box=R_BOX, people=["clerk"],
        say=[dict(who=0, text="النقابة ولا الباطرونا", at=0.5, bg="green")]),
   dict(k="people", at="الحالة التانية: الأم", until="الحالة التالتة", box=FULL, people=["woman", "man", "child"],
        say=[dict(who=0, text="الفترة ديال الولادة", at=0.8, bg="green")]),
   dict(k="big", text="8.500 €", at="الحالة التالتة", until="مثال: خديجة خدمات", y=430, size=220, color=GOLD, sub="فالعام · خدمة بكونطرا"),
   dict(k="map", view="north", pins=["Bologna"], labels=False, at="مثال: خديجة خدمات", until="ولكن خاصك تصرح", box=L_BOX),
   dict(k="steps", at="مثال: خديجة خدمات", until="ولكن خاصك تصرح", box=R_BOX, steps=[
     ["المدخول", "2.000 €"], ["80%", "1.600 €"]], gap=4.0, check_after=0.6),
   dict(k="people", at="ولكن خاصك تصرح", until="الحالة الرابعة", box=FULL, people=["hijab", "office"],
        say=[dict(who=0, text="فشهر", at=0.8, bg="gold"), dict(who=1, text="نازبي كوم", at=4.0, bg="green")]),
   dict(k="vs", at="الحالة الرابعة", until="الحالة الخامسة", box=(260, 220, 1660, 820),
        right=dict(title="6 شهور ولا أقل", value="كتحبس", sub="ومن بعد كترجع", icon="clock", color="gold"),
        left=dict(title="أكثر من 6 شهور", value="كتسالي", sub="ولا غير محدودة", icon="x", color="red"), gap=5.0),
   dict(k="big", text="5.500 €", at="الحالة الخامسة", until="واللي عندو شي مدخول", y=430, size=220, color=GOLD, sub="فالعام · البارتيتا إيفا"),
   dict(k="calendar", at="واللي عندو شي مدخول", until="الحالة السادسة", box=R_BOX, day=31, month=1, sub="المدخول المتوقع"),
   dict(k="people", at="واللي عندو شي مدخول", until="الحالة السادسة", box=L_BOX, people=["worker"],
        say=[dict(who=0, text="نصرح قبل", at=2.0, bg="gold")]),
   dict(k="people", at="الحالة السادسة", until="من هاد العام تبدلات", box=FULL, people=["man", "girl"],
        say=[dict(who=0, text="بغيت نحل مشروع", at=0.6), dict(who=1, text="النازبي المسبقة", at=3.0, bg="green")]),
   dict(k="bars", at="من هاد العام تبدلات", until="ولكن إلى رجعتي", box=(160, 330, 1760, 840), bars=[
     ["فالأول", 9100, "9.100 € (70%)", "green"], ["من بعد", 3900, "3.900 € (30%)", "gold"]], gap=3.0),
   dict(k="warn", text="خدمة عند معلم = ممكن ترجع الفلوس", at="ولكن إلى رجعتي", until="وفكل هاد الحالات", y=860),
   dict(k="people", at="وفكل هاد الحالات", box=FULL, people=["clerk", "worker"],
        say=[dict(who=0, text="صرح بسرعة", at=1.0, bg="green")]),
 ]),
 dict(audio="G.wav", text=T["G"], chapter="07 · الأخطاء والريكورس", src=S_ERR, items=[
   dict(k="chapter", num="07", title="الأخطاء والريكورس", at=0.1, until="الغلطة الأولى"),
   dict(k="people", at="الغلطة الأولى", until="الغلطة التانية", box=R_BOX, people=["man"],
        say=[dict(who=0, text="نستنى شوية...", at=1.0, bg="red")]),
   dict(k="calendar", at="الغلطة الأولى", until="الغلطة التانية", box=L_BOX, day=9, month=3, sub="آخر أجل فالمثال ديال حميد"),
   dict(k="vs", at="الغلطة التانية", until="الغلطة التالتة", box=(260, 220, 1660, 820),
        right=dict(title="استقالة عادية", value="لا", sub="بلا نازبي", icon="x", color="red"),
        left=dict(title="الجوستا كاوزا", value="إيه", sub="مع الحجج", icon="scale", color="green"), gap=5.0),
   dict(k="big", text="15", at="الغلطة التالتة", until="الغلطة الرابعة", y=430, size=280, color=RED, sub="يوم ديال الغياب بلا مبرر = بحال استقالة"),
   dict(k="steps", at="الغلطة الرابعة", until="الغلطة الخامسة", box=L_BOX, steps=[
     ["المرة الأولى", "جزء"], ["المرة التانية", "شهر"], ["المرة التالتة", "كلشي"]], gap=3.0, check_after=0.6),
   dict(k="people", at="الغلطة الرابعة", until="الغلطة الخامسة", box=R_BOX, people=["office"],
        say=[dict(who=0, text="ما جيتيش للموعد!", at=1.0, bg="red")]),
   dict(k="people", at="الغلطة الخامسة", until="الغلطة السادسة", box=FULL, people=["worker", "clerk"],
        say=[dict(who=0, text="ما صرحتش...", at=0.6), dict(who=1, text="رجع الفلوس", at=4.0, bg="red")]),
   dict(k="icons", at="الغلطة السادسة", until="الغلطة السابعة", box=(160, 330, 1760, 860), items=[
     ["credit-card", "الإيبان باسمك", "gold"], ["e-passport", "البيرميسو صالح", "green"], ["building-bank", "بدلتي البنكا؟", "blue"]], gap=2.5),
   dict(k="people", at="الغلطة السابعة", until="دابا، رفضو ليك", box=R_BOX, people=["girl"],
        say=[dict(who=0, text="ما شفتش الرسالة", at=1.0, bg="red")]),
   dict(k="icons", at="الغلطة السابعة", until="دابا، رفضو ليك", box=L_BOX, items=[
     ["mailbox", "البوسطا", "gold"], ["mail", "الإيميل", "blue"]], gap=2.0),
   dict(k="icons", at="دابا، رفضو ليك", until="إلى كانت غير وراق ناقصة", box=(160, 330, 1760, 860), items=[
     ["clock", "من بعد 68 يوم", "red"], ["calendar", "سيمانات ناقصة", "gold"], ["scale", "الجوستا كاوزا", "blue"], ["file-text", "وراق ناقصة", "green"]], gap=2.5),
   dict(k="vs", at="إلى كانت غير وراق ناقصة", until="عندك تسعين يوم", box=(260, 220, 1660, 820),
        right=dict(title="وراق ناقصة", value="إعادة الدراسة", sub="زيد الوراق", icon="file-text", color="blue"),
        left=dict(title="الرفض على الحق", value="الريكورس", sub="مع الباطرونا", icon="scale", color="gold"), gap=4.0),
   dict(k="big", text="90", at="عندك تسعين يوم", until="وتذكر: ما تبقاش", y=430, size=300, color=GOLD, sub="يوم باش دير الريكورس"),
   dict(k="map", view="italy", pins=["Torino", "Bologna", "Napoli"], labels=False, at="وتذكر: ما تبقاش", until="ونصيحة أخيرة", box=(160, 200, 1760, 880)),
   dict(k="icons", at="ونصيحة أخيرة", box=(160, 330, 1760, 860), items=[
     ["clipboard-check", "الطلب والإيصال", "green"], ["receipt", "البوستات باغا", "gold"], ["file-text", "الكونطرا ورسالة الطرد", "blue"]], gap=2.0),
 ]),
 dict(audio="H.wav", text=T["H"], chapter="08 · سؤال وجواب", src=S_QA, items=[
   dict(k="chapter", num="08", title="سؤال وجواب", at=0.1, until="السؤال الأول"),
   dict(k="people", at="السؤال الأول", until="السؤال التاني:", box=FULL, people=["worker"],
        say=[dict(who=0, text="الكونطرا المحدودة سالات", at=0.5), ]),
   dict(k="people", at="السؤال التاني:", until="السؤال التالت", box=FULL, people=["woman"],
        say=[dict(who=0, text="خرجت باتفاق مع المعلم", at=0.5)]),
   dict(k="people", at="السؤال التالت", until="السؤال الرابع", box=FULL, people=["man"],
        say=[dict(who=0, text="ما عطانيش رسالة الطرد", at=0.5)]),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Milano", "Casablanca", "plane"], pins=["Milano", "Casablanca"], labels=False,
        at="السؤال الرابع", until="السؤال الخامس", box=L_BOX),
   dict(k="people", at="السؤال الرابع", until="السؤال الخامس", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="نمشي للمغرب؟", at=0.5)]),
   dict(k="people", at="السؤال الخامس", until="السؤال السادس", box=R_BOX, people=["student"],
        say=[dict(who=0, text="البيرميسو غادي يسالي", at=0.5)]),
   dict(k="big", text="12", at="السؤال الخامس", until="السؤال السادس", x=560, y=430, size=200, color=GREEN, sub="شهر على الأقل"),
   dict(k="people", at="السؤال السادس", until="السؤال السابع", box=R_BOX, people=["elder"],
        say=[dict(who=0, text="عندي 56 عام", at=0.5)]),
   dict(k="big", text="8", at="السؤال السادس", until="السؤال السابع", x=560, y=430, size=260, color=GOLD, sub="الشهر اللي كيبدا فيه النقصان"),
   dict(k="people", at="السؤال السابع", until="السؤال التامن", box=FULL, people=["worker", "clerk"],
        say=[dict(who=0, text="خدمة ديال 3 شهور", at=0.5), dict(who=1, text="كتحبس وترجع", at=4.0, bg="green")]),
   dict(k="people", at="السؤال التامن", until="السؤال التاسع", box=FULL, people=["girl"],
        say=[dict(who=0, text="فاتو 68 يوم!", at=0.5, bg="red")]),
   dict(k="vs", at="السؤال التاسع", until="السؤال العاشر", box=(260, 220, 1660, 820),
        right=dict(title="خام", value="1.153 €", sub="مثال حميد", icon="coin-euro", color="gold"),
        left=dict(title="صافي", value="أقل", sub="من بعد الضريبة", icon="wallet", color="grey"), gap=3.0),
   dict(k="people", at="السؤال العاشر", until="السؤال الحادي عشر", box=FULL, people=["elder", "man"],
        say=[dict(who=1, text="خديتها قبل، نقدر عاوتاني؟", at=0.5)]),
   dict(k="people", at="السؤال الحادي عشر", until="السؤال التاني عشر", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="شحال كيخلص الباطرونا؟", at=0.5)]),
   dict(k="people", at="السؤال التاني عشر", until="هادو هوما الأسئلة", box=FULL, people=["hijab", "worker"],
        say=[dict(who=1, text="ما خلصونيش آخر شهر", at=0.5, bg="red")]),
   dict(k="people", at="هادو هوما الأسئلة", box=FULL, people=["man", "girl"],
        say=[dict(who=1, text="كتب فالكومونتير", at=1.0, bg="green")]),
 ]),
 dict(audio="I.wav", text=T["I"], chapter="09 · الملخص", src=S_HOME, items=[
   dict(k="head", text="اللائحة النهائية", at=0.1, until="واحد: الشرط الأول", sub="خود تصويرة ديال الشاشة"),
   dict(k="rows", at="واحد: الشرط الأول", until="ورجعنا لحميد", y=190, gap=78, size=40, rows=[
     ("بلا ما تبغي ولا جوستا كاوزا", "1", "واحد: الشرط"),
     ("13 سيمانة فالربع سنين", "2", "جوج: تلطاش"),
     ("الطلب قبل 68 يوم", "3", "تلاتة: الطلب"),
     ("السبيد · الإيبان · البيرميسو", "4", "ربعة: وجد"),
     ("الحساب: 75 فالمية حتى السقف", "5", "خمسة: الحساب"),
     ("المدة: حتى 24 شهر", "6", "ستة: المدة"),
     ("صرح بالخدمة فشهر", "7", "سبعة: أي خدمة"),
     ("السفر: بقى حاضر", "8", "تمنية: سافر"),
     ("الريكورس: 90 يوم", "9", "تسعة: إلى رفضو"),
   ]),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="ورجعنا لحميد", until="وخديجة فبولونيا:", box=L_BOX),
   dict(k="steps", at="ورجعنا لحميد", until="وخديجة فبولونيا:", box=R_BOX, steps=[
     ["31/12", "النهاية"], ["8/1", "البداية"], ["1.153 €", "17 شهر"]], gap=3.0, check_after=0.6),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Bologna", "Nador", "plane"], pins=["Bologna", "Nador"], labels=False,
        at="وخديجة فبولونيا:", until="ويوسف فبيرغامو:", box=L_BOX),
   dict(k="people", at="وخديجة فبولونيا:", until="ويوسف فبيرغامو:", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="750 €", at=2.0, bg="green")]),
   dict(k="people", at="ويوسف فبيرغامو:", until="إذن، الثلاثة ديال الحالات", box=R_BOX, people=["man"],
        say=[dict(who=0, text="حسب قبل ما تستقيل", at=5.0, bg="gold")]),
   dict(k="map", view="north", pins=["Bergamo"], labels=False, at="ويوسف فبيرغامو:", until="إذن، الثلاثة ديال الحالات", box=L_BOX),
   dict(k="icons", at="إذن، الثلاثة ديال الحالات", until="ودابا، سؤال ليك", box=(160, 330, 1760, 860), items=[
     ["school", "المعلومة", "green"], ["clock", "الوقت", "gold"], ["file-text", "الوراق", "blue"]], gap=2.0),
   dict(k="people", at="ودابا، سؤال ليك", until="وإلى عرفتي شي واحد", box=FULL, people=["woman", "worker"],
        say=[dict(who=0, text="إيه ولا لا؟", at=2.0, bg="green")]),
   dict(k="people", at="وإلى عرفتي شي واحد", until="وإلى عجبك هاد العمل", box=FULL, people=["man", "hijab"],
        say=[dict(who=0, text="صيفطو لصاحبك", at=1.0, bg="gold")]),
   dict(k="cta", at="وإلى عجبك هاد العمل", text="ابوني فالقناة", sub="كل نهار دليل مفيد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("النازبي خطوة بخطوة", (236, 196, 96)), "الشروط والوراق والحساب", "شحال غادي تشد؟"],
  num="68", numsub="يوم · آخر أجل لطلب النازبي",
  bottom="مغاربة إيطاليا · دليل عملي بالدارجة",
)
