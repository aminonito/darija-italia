import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-22.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo1-2026-11-22-final")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = {k: v.replace("گ", "ك") for k, v in JOB["blocks"].items()}
EDITS = json.load(open(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-22-edits.json"), encoding="utf-8")) if os.path.exists(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-22-edits.json")) else {}
for k, pairs in EDITS.items():
    for a, b in pairs:
        T[k] = T[k].replace(a, b)

S_HOME = "مغاربة إيطاليا · خبار مفيدة بالدارجة"
S_GAS = "MEF decreto 9/11/2026 (GU n. 261) · Edotto 10/11 · QuiFinanza 10/11 · MIMIT via ANSA / Soldionline 20-21/11"
S_PEN = "QuiFinanza 21/11/2026 · InformazioneFiscale 12/11 · LentePubblica 20/10 · Trend Online (tredicesima)"
S_AU = "INPS msg 3931/2025 via InformazioneFiscale · ticonsiglio 13/11 · QuiFinanza 11/11 · Edotto 21/10 · MySolution 12/11"
S_TAX = "Edotto 12/11/2026 · InformazioneFiscale 27/10 · C. App. Roma n. 3203/2026 via QuiFinanza 6/11 e QuotidianoPiù 30/10"
S_CIT = "Camera dei deputati A.C. 2124-A (scheda e calendario) · Avvenire 14/10 · SicurAuto 10/11 · SmartWorld 10/11"
S_CASO = "Esempi nostri (calcoli) · fonti dei capitoli 01-04"
S_MAR = "Bank Al-Maghrib via Hespress 22/11 e Bladi 21/11 · Le Matin 14/11 · FNH 15/11 · Le360 17/11 · DGSN / ADII"
S_QA = "Fonti dei capitoli 01-07"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850); FULL = (160, 300, 1760, 860)
WIDE = (260, 220, 1660, 830); ICO = (160, 330, 1760, 860); BAR = (160, 300, 1760, 840)
MED = dict(view="med", hl=["ITA", "MAR"], labels=False)

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="00 · أخبار السيمانة", src=S_HOME, items=[
   dict(k="head", text="نشرة السيمانة", at=0.2, until="شنو كاين فهاد النشرة؟", sub="الأحد 22 نونبر 2026"),
   dict(k="people", at=0.6, until="شنو كاين فهاد النشرة؟", box=FULL, people=["man", "hijab", "elder"],
        say=[dict(who=0, text="شنو الجديد هاد السيمانة؟", at=0.8), dict(who=2, text="خبار بالأرقام", at=4.0, bg="green")]),
   dict(k="rows", at="شنو كاين فهاد النشرة؟", until="ومن بعد، مثال عملي", y=280, gap=118, size=48, rows=[
     ("المازوط", "23/11", "عندنا المازوط"),
     ("البانسيون والزيادة", "1/12", "عندنا البانسيون"),
     ("الأسينيو والماماوات", "720 €", "عندنا الأسينيو"),
     ("الضريبة", "30/11", "عندنا الضريبة"),
     ("مشروع الجنسية", "?", "وعندنا مشروع الجنسية"),
   ]),
   dict(k="map", **MED, route=["Milano", "Casablanca"], at="ومن بعد، مثال عملي", until="قبل ما نبداو، جوج", box=(160, 200, 1760, 880)),
   dict(k="icons", at="قبل ما نبداو، جوج", until="يالاه نبداو بالخبر", box=ICO, items=[
     ["file-certificate", "جوج مصادر", "green"], ["alert-triangle", "ماشي استشارة", "gold"], ["users", "سول الباطرونا", "blue"]], gap=2.5),
   dict(k="chapter", num="01", title="المازوط: الخصم كيسالي", at="يالاه نبداو بالخبر", until="الخصم هو تقريبا خمسة"),
   dict(k="big", text="4,88", sub="سانتيم فاللتر", at="الخصم هو تقريبا خمسة", until="وهاد الخصم كيبقى"),
   dict(k="calendar", at="وهاد الخصم كيبقى", until="شحال كيعني هادشي فالجيب؟", box=R_BOX, day=23, month=11, sub="آخر نهار"),
   dict(k="people", at="ووقتاش كيسالي؟", until="شحال كيعني هادشي فالجيب؟", box=L_BOX, people=["worker", "clerk"],
        say=[dict(who=0, text="واش غادي يتمد؟", at=0.6), dict(who=1, text="حتى لدابا لا", at=4.5, bg="gold")]),
   dict(k="vs", at="شحال كيعني هادشي فالجيب؟", until="وشحال الثمن دابا؟", box=WIDE,
        right=dict(title="50 لتر بالخصم", value="-2,44 €", sub="حتى 23/11", icon="gas-station", color="green"),
        left=dict(title="50 لتر بلا خصم", value="+2,44 €", sub="من 24/11", icon="gas-station", color="red"), gap=5.0),
   dict(k="bars", at="وشحال الثمن دابا؟", until="شنو تدير؟ ما كنقولوش", box=BAR, bars=[
     ["ليصانص", 1.945, "1,945 €", "gold"], ["المازوط", 2.199, "2,199 €", "red"]]),
   dict(k="map", view="italy", pins=["Milano", "Roma", "Napoli"], labels=False, at="شنو تدير؟ ما كنقولوش", until="وسؤال كيجينا بزاف", box=R_BOX),
   dict(k="icons", at="شنو تدير؟ ما كنقولوش", until="وسؤال كيجينا بزاف", box=L_BOX, items=[
     ["world", "الموقع ديال الأثمنة", "blue"], ["truck", "الكاميو: المحاسب", "gold"]], gap=3.0),
   dict(k="people", at="وسؤال كيجينا بزاف", box=FULL, people=["woman", "man"],
        say=[dict(who=0, text="والليصانص؟", at=0.6), dict(who=1, text="لا، غير المازوط", at=4.0, bg="green")]),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="02 · البانسيون ديال دجنبر", src=S_PEN, items=[
   dict(k="chapter", num="02", title="البانسيون ديال دجنبر", at=0.2, until="البانسيون ديال دجنبر كتخلص"),
   dict(k="calendar", at="البانسيون ديال دجنبر كتخلص", until="ومع البانسيون ديال دجنبر كتجي", box=R_BOX, day=1, month=12, sub="البوسطا والبنكة"),
   dict(k="people", at="البانسيون ديال دجنبر كتخلص", until="ومع البانسيون ديال دجنبر كتجي", box=L_BOX, people=["elder"],
        say=[dict(who=0, text="فوقاش كتخلص؟", at=0.6)]),
   dict(k="steps", at="ومع البانسيون ديال دجنبر كتجي", until="وكاين حاجة تالتة", box=WIDE, steps=[
     ["البانسيون", "1/12"], ["الشهر 13", "1/12"]], gap=3.0, check_after=0.6),
   dict(k="big", text="154,94 €", sub="الإمبورتو أجونتيفو", at="وكاين حاجة تالتة", until="الشرط الأول هو المجموع"),
   dict(k="bars", at="الشرط الأول هو المجموع", until="والخبر المزيان: ما خاصكش", box=BAR, bars=[
     ["كاملة", 7954.05, "7.954 €", "green"], ["جزء", 8108.99, "8.109 €", "gold"], ["والو", 9000, "فوق", "red"]]),
   dict(k="icons", at="والخبر المزيان: ما خاصكش", until="خود مثال. السي سعيد", box=ICO, items=[
     ["check", "بلا طلب", "green"], ["building-bank", "الإينبس", "blue"], ["calendar", "مع دجنبر", "gold"]], gap=2.0),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="خود مثال. السي سعيد", until="وخود مثال آخر.", box=R_BOX),
   dict(k="people", at="خود مثال. السي سعيد", until="وخود مثال آخر.", box=L_BOX, people=["elder"],
        say=[dict(who=0, text="580 € فالشهر", at=0.8), dict(who=0, text="1.315 € فدجنبر", at=9.0, bg="green")]),
   dict(k="people", at="وخود مثال آخر.", until="هادا فوق الحد", box=L_BOX, people=["hijab"],
        say=[dict(who=0, text="640 € فالشهر", at=1.0)]),
   dict(k="vs", at="هادا فوق الحد", until="ردو البال لحاجة أخرى", box=WIDE,
        right=dict(title="سعيد", value="7.540 €", sub="زيادة كاملة", person="elder", color="green"),
        left=dict(title="فاطمة", value="8.320 €", sub="بلا زيادة", person="hijab", color="red"), gap=4.0),
   dict(k="map", view="north", pins=["Bologna"], labels=False, at="وخود مثال آخر.", until="هادا فوق الحد", box=R_BOX),
   dict(k="icons", at="ردو البال لحاجة أخرى", until="ومهم: إلى خديتي الزيادة", box=ICO, items=[
     ["file-text", "الشيدولينو", "blue"], ["receipt-tax", "حسابات الضريبة", "gold"], ["id", "السبيد", "green"]], gap=2.5),
   dict(k="warn", text="ماشي من حقك؟ الإينبس يرجع ياخدها", at="ومهم: إلى خديتي الزيادة", until="وإلى الواليدين ديالك", y=640),
   dict(k="people", at="وإلى الواليدين ديالك", until="وباش تفهم الأرقام", box=FULL, people=["man", "elder"],
        say=[dict(who=0, text="نديك للباطرونا", at=0.8, bg="green")]),
   dict(k="big", text="611,85 €", sub="البانسيون الدنيا فالشهر", at="وباش تفهم الأرقام", until="وللي خدام، ماشي متقاعد"),
   dict(k="steps", at="وللي خدام، ماشي متقاعد", box=WIDE, steps=[
     ["الدولة", "15/12"], ["القطاع الخاص", "CCNL"]], gap=3.0, check_after=0.6),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="03 · الأسينيو والماماوات", src=S_AU, items=[
   dict(k="chapter", num="03", title="الأسينيو والماماوات", at=0.2, until="الأسينيو أونيكو ديال دجنبر"),
   dict(k="calendar", at="الأسينيو أونيكو ديال دجنبر", until="أما اللي دار طلب جديد", box=R_BOX, day=16, month=12, sub="و 17 دجنبر"),
   dict(k="people", at="الأسينيو أونيكو ديال دجنبر", until="وشنو كاين على العام الجاي؟", box=L_BOX, people=["hijab", "child"],
        say=[dict(who=0, text="فوقاش الأسينيو؟", at=0.6)]),
   dict(k="people", at="وشنو كاين على العام الجاي؟", until="الأرقام اللي كتدور هي تقديرات", box=FULL, people=["woman", "man"],
        say=[dict(who=0, text="واش غادي يزيد؟", at=0.6), dict(who=1, text="باقي ما رسميش", at=4.5, bg="gold")]),
   dict(k="vs", at="إلى صح هاد التقدير", until="ولكن عاود: هادي تقديرات", box=WIDE,
        right=dict(title="2026", value="203,80 €", sub="الحد الأقصى", icon="coin-euro", color="grey"),
        left=dict(title="2027 تقدير", value="209,70 €", sub="ماشي رسمي", icon="coin-euro", color="gold"), gap=5.0),
   dict(k="warn", text="تقديرات، ماشي أرقام رسمية", at="ولكن عاود: هادي تقديرات", until="والحاجة اللي مضمونة", y=640),
   dict(k="calendar", at="والحاجة اللي مضمونة", until="ودابا البونس ديال الماماوات", box=WIDE, day=28, month=2, sub="الإيزي الجديد قبل"),
   dict(k="big", text="720 €", sub="60 € فالشهر", at="ودابا البونس ديال الماماوات", until="شكون كياخدو؟"),
   dict(k="icons", at="شكون كياخدو؟", until="والخدامات فالديور", box=ICO, items=[
     ["users", "2 ولاد: أقل من 10", "green"], ["users", "3 ولاد: أقل من 18", "green"], ["briefcase", "حتى 40.000 €", "gold"]], gap=3.0),
   dict(k="people", at="والخدامات فالديور", until="المهم هنا هو الأجل", box=FULL, people=["hijab"],
        say=[dict(who=0, text="الكولف والبادانتي: لا", at=0.6, bg="red")]),
   dict(k="calendar", at="المهم هنا هو الأجل", until="وإمتى كيتخلص؟", box=R_BOX, day=31, month=12, sub="آخر أجل للطلب"),
   dict(k="steps", at="المهم هنا هو الأجل", until="وإمتى كيتخلص؟", box=L_BOX, steps=[
     ["الطلب", "31/12"], ["الشروط فدجنبر", "31/1"], ["الطلب أونلاين", "SPID"]], gap=3.0, check_after=0.6),
   dict(k="map", view="north", pins=["Brescia"], labels=False, at="مثال: خديجة خدامة", until="وردو البال: هاد البونس", box=R_BOX),
   dict(k="people", at="مثال: خديجة خدامة", until="وردو البال: هاد البونس", box=L_BOX, people=["woman"],
        say=[dict(who=0, text="جوج ولاد", at=0.6), dict(who=0, text="720 € إلى طلبت", at=6.0, bg="green")]),
   dict(k="vs", at="وردو البال: هاد البونس", until="وكيفاش تعرف واش الأسينيو", box=WIDE,
        right=dict(title="2026", value="60 €", sub="قانون", icon="check", color="green"),
        left=dict(title="2027", value="100 €", sub="مشروع", icon="alert-triangle", color="gold"), gap=4.0),
   dict(k="icons", at="وكيفاش تعرف واش الأسينيو", box=ICO, items=[
     ["phone", "التطبيق ديال الإينبس", "blue"], ["credit-card", "صلح الإيبان", "gold"]], gap=3.0),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="04 · الضريبة والبارت تايم", src=S_TAX, items=[
   dict(k="chapter", num="04", title="الأكونطو والبارت تايم", at=0.2, until="هو آخر أجل باش تخلص"),
   dict(k="calendar", at="هو آخر أجل باش تخلص", until="شكون كيخلصو بيديه؟", box=WIDE, day=30, month=11, sub="الأكونطو التاني"),
   dict(k="icons", at="شكون كيخلصو بيديه؟", until="أما الخدام العادي", box=ICO, items=[
     ["briefcase", "البارتيتا إيفا", "gold"], ["receipt", "الفورفيتاريو", "gold"], ["user", "بلا معلم", "gold"]], gap=2.0),
   dict(k="vs", at="أما الخدام العادي", until="كيفاش كيتحسب؟", box=WIDE,
        right=dict(title="الخدام والمتقاعد", value="بوحدو", sub="البوستا باغا", person="worker", color="green"),
        left=dict(title="البارتيتا إيفا", value="F24", sub="بيدو", person="man", color="gold"), gap=4.0),
   dict(k="bars", at="كيفاش كيتحسب؟", until="خود مثال: كريم", box=BAR, bars=[
     ["يونيو", 40, "40%", "grey"], ["نونبر", 60, "60%", "gold"], ["الفورفيتاريو", 50, "50/50", "green"]]),
   dict(k="map", view="north", pins=["Milano"], labels=False, at="خود مثال: كريم", until="وإلى فاتك الأجل؟", box=R_BOX),
   dict(k="steps", at="خود مثال: كريم", until="ويوسف فالفورفيتاريو", box=L_BOX, steps=[
     ["كريم: الضريبة", "2.000 €"], ["يونيو", "800 €"], ["نونبر", "1.200 €"]], gap=2.5, check_after=0.6),
   dict(k="people", at="ويوسف فالفورفيتاريو", until="وإلى فاتك الأجل؟", box=L_BOX, people=["man"],
        say=[dict(who=0, text="800 € + 800 €", at=1.0)]),
   dict(k="warn", text="فاتك الأجل؟ رافيديمينتو بغرامة", at="وإلى فاتك الأجل؟", until="وكيفاش تخلص الإيف", y=640),
   dict(k="icons", at="وكيفاش تخلص الإيف", until="ودابا خبر آخر كيهم", box=ICO, items=[
     ["phone", "أبليكاسيون البنكة", "blue"], ["world", "موقع الضرائب", "green"], ["mail", "البوسطا", "gold"], ["receipt", "حفظ الوصل", "gold"]], gap=2.0),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="ودابا خبر آخر كيهم", until="الشركة كانت كتحسب", box=R_BOX),
   dict(k="people", at="ودابا خبر آخر كيهم", until="الشركة كانت كتحسب", box=L_BOX, people=["woman", "hijab"],
        say=[dict(who=0, text="خدامة بالبارت تايم", at=1.0), dict(who=1, text="والترقية؟", at=5.0, bg="gold")]),
   dict(k="vs", at="المحكمة قالت:", until="والمحكمة شافت حتى", box=WIDE,
        right=dict(title="الخلصة", value="على الساعات", sub="عادي", icon="coin-euro", color="green"),
        left=dict(title="الأقدمية", value="ما تنقصش", sub="بلا سبب", icon="clock", color="gold"), gap=4.0),
   dict(k="people", at="شنو كيعني هادشي ليك؟", until="ولكن ردو البال: هادا حكم", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="الترقية متعطلة", at=0.6), dict(who=1, text="سولي السانديكا", at=4.0, bg="green")]),
   dict(k="text", text="حكم ديال محكمة وحدة، ماشي قانون", at="ولكن ردو البال: هادا حكم", until="وشنو تشوف فالبوستا باغا؟", y=880, size=56, color=GOLD),
   dict(k="icons", at="وشنو تشوف فالبوستا باغا؟", box=ICO, items=[
     ["chart-bar", "الليفيلو", "blue"], ["clock", "الأقدمية", "gold"], ["users", "قارن", "green"]], gap=2.5),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="05 · الجنسية والكود ديال الطريق", src=S_CIT, items=[
   dict(k="chapter", num="05", title="مشروع الجنسية", at=0.2, until="الجديد هو: حسب البرنامج"),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="الجديد هو: حسب البرنامج", until="ولكن ردو البال مزيان", box=R_BOX),
   dict(k="people", at="الجديد هو: حسب البرنامج", until="ولكن ردو البال مزيان", box=L_BOX, people=["man"],
        say=[dict(who=0, text="التصويت السيمانة الجاية", at=1.0)]),
   dict(k="steps", at="ولكن ردو البال مزيان", until="شنو فيه هاد المشروع؟", box=WIDE, steps=[
     ["مجلس النواب", "1"], ["السينا", "2"], ["الجريدة الرسمية", "3"]], gap=3.0, check_after=0.6),
   dict(k="icons", at="شنو فيه هاد المشروع؟", until="الأول: اللغة.", box=ICO, items=[
     ["certificate", "بي واحد حتى للكارطا", "gold"], ["scale", "أحكام كتمنع", "red"], ["id", "اليمين بالطاليانية", "blue"]], gap=5.0),
   dict(k="vs", at="الأول: اللغة.", until="التاني: بعض الأحكام", box=WIDE,
        right=dict(title="اليوم", value="معفي", sub="بالكارطا", icon="check", color="green"),
        left=dict(title="المشروع", value="B1", sub="حتى بالكارطا", icon="alert-triangle", color="gold"), gap=4.0),
   dict(k="people", at="شنو تدير دابا؟", until="تانيا، تبع الأخبار", box=FULL, people=["worker", "girl"],
        say=[dict(who=0, text="سالا القانون؟", at=0.6), dict(who=1, text="لا، باقي مشروع", at=4.0, bg="red")]),
   dict(k="icons", at="تانيا، تبع الأخبار", until="ودابا الكود ديال الطريق", box=ICO, items=[
     ["building-bank", "البريفيتورا", "blue"], ["users", "الباطرونا", "green"], ["certificate", "بي واحد", "gold"]], gap=3.0),
   dict(k="chapter", num="06", title="الكود ديال الطريق", at="ودابا الكود ديال الطريق", until="والأجل باش الحكومة"),
   dict(k="calendar", at="والأجل باش الحكومة", until="فهاد المشروع كاينين", box=WIDE, day=25, month=11, sub="الحكومة تجاوب"),
   dict(k="icons", at="فهاد المشروع كاينين", until="وشحال باقي فالطريق؟", box=ICO, items=[
     ["license", "10 سنين حتى 65", "gold"], ["phone", "البيرمي فالتيليفون", "blue"]], gap=3.0),
   dict(k="steps", at="وشحال باقي فالطريق؟", until="ولكن اليوم، ما تبدل والو", box=WIDE, steps=[
     ["الحكومة", "25/11"], ["مجلس الدولة", "رأي"], ["البرلمان", "12/1"], ["المصادقة", "?"]], gap=2.5, check_after=0.6),
   dict(k="map", **MED, route=["Casablanca", "Milano"], at="وإلى عندك البيرمي المغربي", until="وتذكير على الشهادة", box=R_BOX),
   dict(k="people", at="وإلى عندك البيرمي المغربي", until="وتذكير على الشهادة", box=L_BOX, people=["man"],
        say=[dict(who=0, text="عام واحد من الريزيدينسا", at=0.8, bg="gold")]),
   dict(k="rows", at="وتذكير على الشهادة", y=300, gap=120, size=48, rows=[
     ("سيينا", "CILS", "الجامعة ديال سيينا"),
     ("بيروجا", "CELI", "والجامعة ديال بيروجا"),
     ("روما تري", "CERT.IT", "والجامعة ديال روما تري"),
     ("دانتي أليغييري", "PLIDA", "والجمعية ديال دانتي"),
   ]),
 ]),
 dict(audio="F.wav", text=T["F"], chapter="07 · مثال عملي: عائلة وحدة", src=S_CASO, items=[
   dict(k="head", text="مثال عملي", at=0.2, until="عائلة الحسني ساكنة", sub="عائلة وحدة، أربعة ديال الحوايج"),
   dict(k="map", view="north", pins=["Brescia"], labels=False, at="عائلة الحسني ساكنة", until="شنو غادي يدخل", box=R_BOX),
   dict(k="people", at="عائلة الحسني ساكنة", until="شنو غادي يدخل", box=L_BOX, people=["elder", "woman", "child"],
        say=[dict(who=0, text="عبد الله", at=0.5), dict(who=1, text="نادية", at=2.0)]),
   dict(k="people", at="شنو غادي يدخل", until="نبداو بعبد الله", box=FULL, people=["man"],
        say=[dict(who=0, text="وأنا مراد، فورفيتاريو", at=0.4)]),
   dict(k="steps", at="نبداو بعبد الله", until="ولكن ردو البال: الشرط", box=WIDE, steps=[
     ["550 × 13", "7.150 €"], ["الحد", "7.954 €"], ["فدجنبر", "≈ 1.255 €"]], gap=4.0, check_after=0.6),
   dict(k="icons", at="وعبد الله يقدر يشوف", until="نادية خدامة العام كامل", box=ICO, items=[
     ["file-text", "الشيدولينو", "blue"], ["users", "الباطرونا", "green"]], gap=3.0),
   dict(k="people", at="نادية خدامة العام كامل", until="شنو خاصها دير؟", box=FULL, people=["woman"],
        say=[dict(who=0, text="البونس: 720 €", at=6.0, bg="green")]),
   dict(k="calendar", at="شنو خاصها دير؟", until="ونادية خاصها تحضر", box=R_BOX, day=31, month=12, sub="البونس ديال الماماوات"),
   dict(k="icons", at="شنو خاصها دير؟", until="ونادية خاصها تحضر", box=L_BOX, items=[
     ["id", "السبيد", "blue"], ["users", "الباطرونا", "green"]], gap=2.5),
   dict(k="calendar", at="ونادية خاصها تحضر", until="ودابا مراد.", box=WIDE, day=1, month=1, sub="الإيزي الجديد"),
   dict(k="vs", at="ودابا مراد.", until="وعندو طوموبيل ديال المازوط", box=WIDE,
        right=dict(title="يونيو", value="600 €", sub="خلص", icon="check", color="green"),
        left=dict(title="قبل 30/11", value="600 €", sub="F24", icon="receipt-tax", color="gold"), gap=4.0),
   dict(k="big", text="+2,5 €", sub="فكل تعميرة من 24/11", at="وعندو طوموبيل ديال المازوط", until="نجمعو الحساب"),
   dict(k="bars", at="نجمعو الحساب", until="ومراد خاصو يخلص ستمية", box=BAR, bars=[
     ["عبد الله", 154.94, "154,94 €", "green"], ["نادية", 720, "720 €", "green"], ["المجموع", 874.94, "≈ 875 €", "gold"]]),
   dict(k="text", text="مراد: 600 € قبل 30/11", at="ومراد خاصو يخلص ستمية", until="والأخطاء اللي خاصهم", y=880, size=58, color=GOLD),
   dict(k="people", at="والأخطاء اللي خاصهم", until="والنصيحة ديالنا", box=FULL, people=["woman", "man"],
        say=[dict(who=0, text="نسيت الطلب!", at=0.6, bg="red"), dict(who=1, text="خلصت بالغرامة", at=5.5, bg="red")]),
   dict(k="steps", at="والنصيحة ديالنا", until="وإلى عندكم حالة بحال", box=WIDE, steps=[
     ["الضريبة", "30/11"], ["البانسيون", "1/12"], ["الأسينيو", "16/12"], ["البونس", "31/12"]], gap=2.5, check_after=0.6),
   dict(k="people", at="وإلى عندكم حالة بحال", box=FULL, people=["clerk", "elder"],
        say=[dict(who=0, text="جيبو الوراق كاملين", at=0.8, bg="green")]),
 ]),
 dict(audio="G.wav", text=T["G"], chapter="08 · من المغرب", src=S_MAR, items=[
   dict(k="chapter", num="08", title="من المغرب", at=0.2, until="حسب الأرقام ديال بنك المغرب"),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Casablanca"], labels=False, at="حسب الأرقام ديال بنك المغرب", until="شنو كيعني هادشي؟", box=R_BOX),
   dict(k="bars", at="حسب الأرقام ديال بنك المغرب", until="شنو كيعني هادشي؟", box=L_BOX, bars=[
     ["الأورو", 0.6, "0,6%", "gold"], ["الدولار", 1.7, "1,7%", "red"]]),
   dict(k="people", at="شنو كيعني هادشي؟", until="مثال: الأورو كان", box=FULL, people=["man", "elder"],
        say=[dict(who=0, text="كنصيفط للواليدين", at=0.6), dict(who=1, text="الأورو كيجيب كثر", at=4.0, bg="green")]),
   dict(k="vs", at="مثال: الأورو كان", until="ولكن ردو البال: هادا هو السعر", box=WIDE,
        right=dict(title="1.000 €", value="≈ 65", sub="درهم زايدين", icon="cash", color="green"),
        left=dict(title="5.000 €", value="≈ 320", sub="درهم زايدين", icon="cash", color="green"), gap=4.0),
   dict(k="icons", at="ولكن ردو البال: هادا هو السعر", until="والسيمانة اللي قبلها", box=ICO, items=[
     ["building-bank", "السعر ديال البنكة", "blue"], ["percentage", "العمولة", "gold"], ["calculator", "قارن", "green"]], gap=2.5),
   dict(k="map", **MED, route=["Milano", "Casablanca"], at="والسيمانة اللي قبلها", until="الخبر التاني: الميزانية", box=(160, 200, 1760, 880)),
   dict(k="steps", at="الخبر التاني: الميزانية", until="بمية وتسعة وسبعين", box=WIDE, steps=[
     ["مجلس النواب", "14/11"], ["مجلس المستشارين", "دابا"], ["القراءة التانية", "?"]], gap=3.0, check_after=0.6),
   dict(k="bars", at="بمية وتسعة وسبعين", until="ودابا هي فمجلس المستشارين", box=BAR, bars=[
     ["مع", 179, "179", "green"], ["ضد", 126, "126", "red"]]),
   dict(k="people", at="واش فيها شي حاجة خاصة", until="والميزانية فالمغرب، فالعادة", box=FULL, people=["hijab", "man"],
        say=[dict(who=0, text="والجالية؟", at=0.6), dict(who=1, text="حتى لدابا: والو", at=3.5, bg="gold")]),
   dict(k="calendar", at="والميزانية فالمغرب، فالعادة", until="الخبر التالت، تذكير", box=WIDE, day=1, month=1, sub="الميزانية كتبدا"),
   dict(k="map", **MED, route=["Casablanca", "Milano"], pins=["Rabat"], at="الخبر التالت، تذكير", until="هاد الورقة كتطلبها", box=R_BOX),
   dict(k="icons", at="الخبر التالت، تذكير", until="هاد الورقة كتطلبها", box=L_BOX, items=[
     ["world", "أونلاين", "blue"], ["building-bank", "القنصلية", "green"]], gap=3.0),
   dict(k="warn", text="صالحة 6 شهور: ما تطلبهاش بكري", at="هاد الورقة كتطلبها", until="الخبر الرابع، للي ناوي", y=640),
   dict(k="map", **MED, route=["Genova", "Tanger", "ship"], at="الخبر الرابع، للي ناوي", until="الطوموبيل بالماتريكولا", box=(160, 200, 1760, 880)),
   dict(k="big", text="180", sub="يوم فالعام للطوموبيل", at="الطوموبيل بالماتريكولا", until="وإلى فاتيتيهم"),
   dict(k="text", text="الخطية: 1.000 - 10.000 درهم", at="وإلى فاتيتيهم", until="إذن حسب الأيام", y=880, size=56, color=RED),
   dict(k="people", at="وإلى مشيتي بالطيارة", box=FULL, people=["girl", "man"],
        say=[dict(who=0, text="الباسبور + البيرميسو", at=3.0), dict(who=1, text="رحلة مباشرة", at=8.0, bg="green")]),
 ]),
 dict(audio="H.wav", text=T["H"], chapter="09 · سؤال وجواب", src=S_QA, items=[
   dict(k="head", text="سؤال وجواب", at=0.2, until="السؤال الأول:"),
   dict(k="people", at="السؤال الأول:", until="السؤال التاني:", box=FULL, people=["elder", "clerk"],
        say=[dict(who=0, text="700 € فالشهر: واش الزيادة؟", at=0.5), dict(who=1, text="9.100 € فالعام: لا", at=8.0, bg="red")]),
   dict(k="people", at="السؤال التاني:", until="السؤال التالت:", box=FULL, people=["hijab", "office"],
        say=[dict(who=0, text="واش كتجي بوحدها؟", at=0.5), dict(who=1, text="إيه، إلى نفس الشروط", at=5.0, bg="green")]),
   dict(k="people", at="السؤال التالت:", until="السؤال الرابع:", box=FULL, people=["man", "woman"],
        say=[dict(who=0, text="المرا ما خدامةش", at=0.5), dict(who=1, text="البونس لا، الأسينيو إيه", at=6.0, bg="gold")]),
   dict(k="people", at="السؤال الرابع:", until="السؤال الخامس:", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="بادانتي وعندي تلاتة ولاد", at=0.5), dict(who=1, text="للأسف لا", at=6.0, bg="red")]),
   dict(k="people", at="السؤال الخامس:", until="السؤال السادس:", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="نخلص الأكونطو بيدي؟", at=0.5), dict(who=1, text="فالعادة لا: البوستا باغا", at=6.0, bg="green")]),
   dict(k="people", at="السؤال السادس:", until="السؤال السابع:", box=FULL, people=["girl", "clerk"],
        say=[dict(who=0, text="عندي الكارطا: بي واحد؟", at=0.5), dict(who=1, text="باقي مشروع", at=7.0, bg="gold")]),
   dict(k="people", at="السؤال السابع:", until="السؤال التامن:", box=FULL, people=["hijab", "office"],
        say=[dict(who=0, text="الأسينيو غادي يزيد؟", at=0.5), dict(who=1, text="تسنى السيركولار", at=5.0, bg="gold")]),
   dict(k="people", at="السؤال التامن:", until="السؤال التاسع:", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="نتسنى الدرهم يطيح؟", at=0.5), dict(who=1, text="قارن العمولة", at=6.0, bg="green")]),
   dict(k="people", at="السؤال التاسع:", until="السؤال العاشر:", box=FULL, people=["worker", "elder"],
        say=[dict(who=0, text="الخصم غادي يرجع؟", at=0.5), dict(who=1, text="حتى لدابا لا", at=4.0, bg="gold")]),
   dict(k="map", **MED, route=["Casablanca", "Milano"], at="السؤال العاشر:", until="السؤال الحداش:", box=R_BOX),
   dict(k="people", at="السؤال العاشر:", until="السؤال الحداش:", box=L_BOX, people=["man", "clerk"],
        say=[dict(who=0, text="نتسنى الكود الجديد؟", at=0.5), dict(who=1, text="لا: عام واحد", at=7.0, bg="red")]),
   dict(k="people", at="السؤال الحداش:", until="وإلى عندك سؤال آخر", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="ما عنديش السبيد", at=0.5), dict(who=1, text="سيري للباطرونا", at=4.0, bg="green")]),
   dict(k="text", text="كتب السؤال ديالك فالكومونتير", at="وإلى عندك سؤال آخر", y=880, size=58, color=GOLD),
 ]),
 dict(audio="I.wav", text=T["I"], chapter="10 · الخلاصة والتواريخ", src=S_HOME, items=[
   dict(k="head", text="الخلاصة", at=0.2, until="واحد: الخصم ديال المازوط"),
   dict(k="rows", at="واحد: الخصم ديال المازوط", until="ستة: الحكم على البارت", y=300, gap=110, size=46, rows=[
     ("الخصم ديال المازوط", "23/11", "واحد: الخصم"),
     ("البانسيون + الزيادة", "154,94 €", "جوج: البانسيون"),
     ("الأسينيو ديال دجنبر", "16/12", "تلاتة: الأسينيو"),
     ("البونس ديال الماماوات", "720 €", "ربعة: البونس"),
     ("الأكونطو التاني", "30/11", "خمسة: الأكونطو"),
   ]),
   dict(k="rows", at="ستة: الحكم على البارت", until="ودابا التواريخ ديال الأيام", y=300, gap=110, size=46, rows=[
     ("البارت تايم والأقدمية", "!", "ستة: الحكم"),
     ("مشروع الجنسية", "?", "سبعة: مشروع"),
     ("الكود ديال الطريق", "?", "تمنية: الكود"),
     ("من المغرب: الدرهم", "0,6%", "وتسعة: من المغرب"),
   ]),
   dict(k="steps", at="ودابا التواريخ ديال الأيام", until="الأربعاء سطاش دجنبر", box=WIDE, steps=[
     ["المازوط", "23/11"], ["الكود", "25/11"], ["الأكونطو", "30/11"], ["البانسيون", "1/12"], ["الديكري فلوسي", "7/12"]], gap=3.5, check_after=0.6),
   dict(k="steps", at="الأربعاء سطاش دجنبر", until="وإلى فاتك شي فيديو", box=WIDE, steps=[
     ["الأسينيو + الإيمو + الكارطا", "16/12"], ["البونس + الإيزي", "31/12"]], gap=4.0, check_after=0.6),
   dict(k="icons", at="وإلى فاتك شي فيديو", until="وغدا كاين ريل جديد", box=ICO, items=[
     ["heart", "الجنسية", "gold"], ["car", "تبديل البيرمي", "blue"], ["id", "البيرميسو", "gold"], ["briefcase", "النازبي", "green"]], gap=2.5),
   dict(k="people", at="ونعاودو نقولو", until="والنصيحة الأخيرة", box=FULL, people=["clerk", "woman"],
        say=[dict(who=0, text="سول الباطرونا ولا الكاف", at=1.0, bg="green")]),
   dict(k="people", at="والنصيحة الأخيرة", until="وحاجة أخيرة: ما تعطيش", box=FULL, people=["elder", "man"],
        say=[dict(who=0, text="بدا بالأجل القريب", at=1.0, bg="gold")]),
   dict(k="warn", text="ما تعطيش السبيد ديالك لحتى واحد", at="وحاجة أخيرة: ما تعطيش", until="وإلى عجبك هاد الفيديو", y=640),
   dict(k="cta", at="وإلى عجبك هاد الفيديو", until="وكتب لينا فالكومونتير", text="ابوني فالقناة", sub="وفعل الجرس"),
   dict(k="people", at="وكتب لينا فالكومونتير", box=FULL, people=["girl", "worker", "hijab"],
        say=[dict(who=1, text="شنو فاد بيك أكثر؟", at=0.8), dict(who=2, text="صيفطو لشي واحد", at=6.0, bg="green")]),
 ]),
]

THUMB = dict(
  title=[("المازوط والبانسيون ديال دجنبر", (236, 196, 96)), "زيادة حتى 154,94 أورو بلا طلب", "البونس ديال الماماوات قبل آخر العام"],
  num="1/12", numsub="البانسيون والزيادة",
  bottom="مغاربة إيطاليا · خبار مفيدة بالدارجة",
)
