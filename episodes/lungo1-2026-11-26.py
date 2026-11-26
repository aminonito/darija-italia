import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-26.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo1-2026-11-26-final")
BRAND = "مغاربة إيطاليا"
T = {k: v.replace("گ", "ك") for k, v in JOB["blocks"].items()}
EP_EDITS = os.path.join(ROOT, "tts/jobs/lungo1-2026-11-26-edits.json")
EDITS = json.load(open(EP_EDITS, encoding="utf-8")) if os.path.exists(EP_EDITS) else {}
for k, pairs in EDITS.items():
    for a, b in pairs:
        T[k] = T[k].replace(a, b)

S_HOME = "مغاربة إيطاليا · خبار مفيدة بالدارجة"
S_SCU = "DL 170/2026 · QuiFinanza 26/11 · Notizie.it 25/11 · Domani 25/11 · Affaritaliani 19/11 · Scuola Moscati 24/11"
S_SCU2 = "DL 170/2026 · Domani 25/11 · Affaritaliani 19/11 · Notizie.it · QuiFinanza 26/11"
S_SCAD = "Registro: INPS · QuiFinanza · InformazioneFiscale · Codice del consumo art. 17-bis · Min. Lavoro circ. 7185"
S_DIC = "InformazioneFiscale · Centro Fiscale · ARERA del. 58/2026 · Ticonsiglio · INPS · LentePubblica"
S_CASE = "DL 170/2026 (Domani · Affaritaliani) · calcoli nostri"
S_MAR = "Banca d'Italia 9/10/2026 · Bladi 24/10 · Il Sole 24 Ore · AGI 17/2 e 6/5/2026 · L'ODJ · H24info"
S_QA = "Fonti dei capitoli 01-07"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850); FULL = (160, 300, 1760, 860)
WIDE = (260, 220, 1660, 830); ICO = (160, 330, 1760, 860); BAR = (160, 300, 1760, 840)
MED = dict(view="med", hl=["ITA", "MAR"], labels=False)
BIGMAP = (160, 200, 1760, 880)

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="00 · أخبار السيمانة", src=S_HOME, items=[
   dict(k="head", text="نشرة السيمانة", at=0.2, until="شنو كاين فهاد النشرة؟", sub="الخميس 26 نونبر 2026"),
   dict(k="people", at=0.6, until="شنو كاين فهاد النشرة؟", box=FULL, people=["hijab", "man", "child"],
        say=[dict(who=0, text="شنو تبدل فالمدرسة؟", at=0.8), dict(who=1, text="خبار بالأرقام", at=5.0, bg="green")]),
   dict(k="rows", at="شنو كاين فهاد النشرة؟", until="ومن بعد، مثال عملي", y=280, gap=118, size=48, rows=[
     ("المرسوم ديال المدرسة", "30%", "عندنا المرسوم الجديد"),
     ("الآجال ديال آخر نونبر", "27/11 · 30/11", "عندنا الآجال ديال آخر نونبر"),
     ("الفلوس ديال دجنبر", "1/12", "والفلوس ديال دجنبر"),
   ]),
   dict(k="map", view="north", pins=["Brescia"], labels=False, at="ومن بعد، مثال عملي", until="ومن المغرب، الفلوس", box=BIGMAP),
   dict(k="map", **MED, route=["Milano", "Casablanca"], at="ومن المغرب، الفلوس", until="قبل ما نبداو، جوج", box=BIGMAP),
   dict(k="icons", at="قبل ما نبداو، جوج", until="يالاه نبداو.", box=ICO, items=[
     ["file-certificate", "جوج مصادر", "green"], ["alert-triangle", "ماشي استشارة", "gold"], ["users", "سول الباترونا", "blue"]], gap=2.5),
   dict(k="chapter", num="01", title="المرسوم ديال المدرسة", at="الخبر الأول: المرسوم", until="هادا مرسوم قانون رقم"),
   dict(k="big", text="DL 170", sub="30 شتنبر 2026", at="هادا مرسوم قانون رقم", until="فين وصل؟"),
   dict(k="steps", at="فين وصل؟", until="والتصويت الأخير على القانون", box=WIDE, steps=[
     ["مجلس الشيوخ", "80 · 46"], ["الثقة فمجلس النواب", "180 · 112"], ["التصويت الأخير", "?"]], gap=6.0, check_after=99),
   dict(k="calendar", at="والتصويت الأخير على القانون", until="وشنو هو المرسوم ديال القانون؟", box=R_BOX, day=29, month=11, sub="آخر أجل للمصادقة"),
   dict(k="map", view="italy", hl=["Lazio"], pins=["Roma"], labels=False, at="والتصويت الأخير على القانون", until="وشنو هو المرسوم ديال القانون؟", box=L_BOX),
   dict(k="vs", at="وشنو هو المرسوم ديال القانون؟", until="علاش هاد الخبر كيهمك؟", box=WIDE,
        right=dict(title="المرسوم", value="دابا", sub="كيتطبق من النهار الأول", icon="file-text", color="gold"),
        left=dict(title="البرلمان", value="60", sub="يوم باش يصادق", icon="building-bank", color="blue"), gap=4.0),
   dict(k="icons", at="علاش هاد الخبر كيهمك؟", until="وحنا غادي نشرحو", box=ICO, items=[
     ["school", "القسم الأول", "blue"], ["users", "الواليدين", "gold"], ["alert-triangle", "الوجه المغطي", "red"], ["file-text", "الكتب", "green"]], cols=4, gap=3.0),
   dict(k="people", at="وحنا غادي نشرحو", until="ودابا نمشيو للتفاصيل", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="غادي يخرجو ولادنا؟", at=1.0), dict(who=1, text="لا، كل ولد عندو الحق يقرا", at=9.0, bg="green")]),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="02 · سقف التلاميذ الأجانب", src=S_SCU, items=[
   dict(k="chapter", num="02", title="سقف التلاميذ الأجانب", at=0.2, until="أولا، فوقاش؟"),
   dict(k="calendar", at="أولا، فوقاش؟", until="ثانيا، فين؟", box=WIDE, day="2027", month="2028", sub="العام الدراسي"),
   dict(k="icons", at="ثانيا، فين؟", until="ثالثا، شكون كيتحسب؟", box=ICO, items=[
     ["school", "الأول ابتدائي", "blue"], ["school", "الأول إعدادي", "gold"], ["school", "الأول ثانوي", "green"]], gap=2.0),
   dict(k="people", at="ثالثا، شكون كيتحسب؟", until="فالابتدائي، كيتحسب", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="ولدي أجنبي: كيتحسب؟", at=0.6), dict(who=1, text="ماشي ديما", at=3.5, bg="gold")]),
   dict(k="vs", at="فالابتدائي، كيتحسب", until="وفالإعدادي والثانوي", box=WIDE,
        right=dict(title="تزاد هنا + الماطيرنا", value="لا", sub="عادة ما كيتحسبش", person="child", color="green"),
        left=dict(title="جا من برا، بلا ماطيرنا", value="إيه", sub="كيتحسب", person="girl", color="red"), gap=5.0),
   dict(k="vs", at="وفالإعدادي والثانوي", until="رابعا، شنو كيوقع", box=WIDE,
        right=dict(title="3 سنين ونجح", value="لا", sub="ما كيتحسبش", icon="school", color="green"),
        left=dict(title="أقل من 3 سنين", value="إيه", sub="كيتحسب", icon="plane", color="red"), gap=5.0),
   dict(k="map", view="north", pins=["Bergamo", "Brescia"], labels=False, at="رابعا، شنو كيوقع", until="وخامسا، إلى ما قدروش", box=R_BOX),
   dict(k="icons", at="رابعا، شنو كيوقع", until="وخامسا، إلى ما قدروش", box=L_BOX, items=[
     ["map-pin", "البعد على الدار", "blue"], ["heart", "ظروف العائلة", "gold"]], gap=8.0),
   dict(k="big", text="الطاليانية", sub="دروس زايدة للتلاميذ", at="وخامسا، إلى ما قدروش", until="إذن، باش نلخصو"),
   dict(k="warn", text="ماشي منع ديال التسجيل", at="إذن، باش نلخصو", until="وخلي نعاودو بالأمثلة", y=600),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="وخلي نعاودو بالأمثلة", until="ولد جا من مراكش", box=R_BOX),
   dict(k="people", at="وخلي نعاودو بالأمثلة", until="ولد جا من مراكش", box=L_BOX, people=["child"],
        say=[dict(who=0, text="تزاد فطورينو", at=2.0, bg="green")]),
   dict(k="map", **MED, route=["Marrakech", "Milano"], at="ولد جا من مراكش", until="بنت قرات فإيطاليا", box=BIGMAP),
   dict(k="people", at="بنت قرات فإيطاليا", until="وولد جا من فاس", box=FULL, people=["girl", "clerk"],
        say=[dict(who=0, text="قريت 5 سنين هنا", at=0.6), dict(who=1, text="ما كتتحسبيش", at=5.0, bg="green")]),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Fes"], labels=False, at="وولد جا من فاس", until="شنو خاصك دير؟", box=BIGMAP),
   dict(k="icons", at="شنو خاصك دير؟", until="وحاجة أخرى: سجل الولد", box=ICO, items=[
     ["certificate", "الماطيرنا", "blue"], ["report-money", "النتائج", "gold"], ["file-text", "شهادة الازدياد", "green"]], gap=4.0),
   dict(k="steps", at="وحاجة أخرى: سجل الولد", until="وإلى ما فهمتيش شي حاجة", box=WIDE, steps=[
     ["التواريخ ديال المدرسة", "1"], ["التسجيل أونلاين", "2"], ["فالوقت", "3"]], gap=3.0, check_after=99),
   dict(k="people", at="وإلى ما فهمتيش شي حاجة", box=FULL, people=["hijab", "office"],
        say=[dict(who=0, text="عندي سؤال", at=0.6), dict(who=1, text="السكريتاريا كتشرح", at=3.0, bg="green")]),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="03 · الواليدين والكتب", src=S_SCU2, items=[
   dict(k="chapter", num="03", title="الواليدين والطاليانية", at=0.2, until="المرسوم كيقول: إلى لقات"),
   dict(k="steps", at="المرسوم كيقول: إلى لقات", until="والجديد هو العقوبة", box=WIDE, steps=[
     ["المدرسة", "1"], ["الخدمات الاجتماعية", "2"], ["دروس بالمجان", "3"]], gap=6.0, check_after=99),
   dict(k="big", text="200 - 1.000 €", sub="الغرامة: غير إلى رفضتي بلا سبب", at="والجديد هو العقوبة", until="رد البال: ماشي أي واحد"),
   dict(k="people", at="رد البال: ماشي أي واحد", until="وإلى جاتك رسالة", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="ما كنعرفش الطاليانية مزيان", at=0.6), dict(who=1, text="قبلي الدروس", at=8.0, bg="green")]),
   dict(k="icons", at="وإلى جاتك رسالة", until="وحتى بلا هاد القانون", box=ICO, items=[
     ["mail", "ما تخبيهاش", "blue"], ["users", "الباترونا", "gold"], ["clock", "جاوب فالوقت", "green"], ["file-text", "بالكتابة", "blue"]], cols=4, gap=3.0),
   dict(k="map", view="italy", pins=["Milano", "Bologna", "Napoli"], labels=False, at="وحتى بلا هاد القانون", until="الجزء الثالث: الوجه", box=R_BOX),
   dict(k="people", at="وحتى بلا هاد القانون", until="الجزء الثالث: الوجه", box=L_BOX, people=["elder"],
        say=[dict(who=0, text="الشيبيا قريب ليا", at=1.0, bg="green")]),
   dict(k="warn", text="الوجه المغطي ممنوع فالمدرسة", at="الجزء الثالث: الوجه", until="كاين استثناء لأسباب", y=600),
   dict(k="vs", at="كاين استثناء لأسباب", until="هادي قاعدة جديدة", box=WIDE,
        right=dict(title="استثناء", value="الصحة", sub="ولا القراية", icon="stethoscope", color="green"),
        left=dict(title="الغرامة", value="200 - 1.000 €", sub="للواليدين إلى قاصر", icon="alert-triangle", color="red"), gap=4.0),
   dict(k="people", at="هادي قاعدة جديدة", until="الجزء الرابع، وهادا خبر", box=FULL, people=["office", "man"],
        say=[dict(who=0, text="القانون الداخلي غادي يتبدل", at=0.6, bg="gold")]),
   dict(k="bars", at="الجزء الرابع، وهادا خبر", until="يعني عائلات كثر", box=BAR, bars=[
     ["قبل", 30000, "30.000 €", "gold"], ["دابا", 40000, "40.000 €", "green"]]),
   dict(k="text", text="العتبة ديال الإيزي: المساعدة ديال الكتب", at="الجزء الرابع، وهادا خبر", until="يعني عائلات كثر", y=880, size=42),
   dict(k="big", text="21", sub="مليون أورو للكتب المجانية", at="والمرسوم زاد حتى", until="كيفاش كتطلبها؟"),
   dict(k="map", view="italy", pins=["Torino", "Roma", "Palermo"], labels=False, at="كيفاش كتطلبها؟", until="وكاين حوايج أخرى", box=R_BOX),
   dict(k="people", at="كيفاش كتطلبها؟", until="وكاين حوايج أخرى", box=L_BOX, people=["hijab"],
        say=[dict(who=0, text="شوف الكوموني ديالك", at=1.0, bg="green")]),
   dict(k="icons", at="وكاين حوايج أخرى", until="باش نلخصو هاد الخبر", box=ICO, items=[
     ["users", "الأساتذة", "blue"], ["building-factory", "المدارس التقنية", "gold"], ["school", "اللاتينية", "green"]], gap=2.5),
   dict(k="rows", at="باش نلخصو هاد الخبر", y=300, gap=118, size=46, rows=[
     ("السقف فالأقسام الأولى", "2027/28", "باش نلخصو هاد الخبر"),
     ("دروس الواليدين بالمجان", "0 €", "الدروس ديال الطاليانية للواليدين"),
     ("الوجه المغطي ممنوع", "200 - 1.000 €", "الوجه المغطي ممنوع"),
     ("المساعدة ديال الكتب", "40.000 €", "والمساعدة ديال الكتب ولات"),
   ]),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="04 · الآجال ديال آخر نونبر", src=S_SCAD, items=[
   dict(k="chapter", num="04", title="الآجال ديال آخر نونبر", at=0.2, until="نبداو بغدا"),
   dict(k="calendar", at="نبداو بغدا", until="العتبة ديال الإيزي هي", box=R_BOX, day=27, month=11, sub="الأدي: الشحنة العادية"),
   dict(k="people", at="نبداو بغدا", until="العتبة ديال الإيزي هي", box=L_BOX, people=["woman"],
        say=[dict(who=0, text="الأدي غدا", at=1.5, bg="green")]),
   dict(k="big", text="10.140 €", sub="العتبة ديال الإيزي للأدي", at="العتبة ديال الإيزي هي", until="والشهر الأول من بعد"),
   dict(k="big", text="50%", sub="الشهر الأول من بعد التجديد", at="والشهر الأول من بعد", until="وإلى ما وصلاتكش الفلوس"),
   dict(k="people", at="وإلى ما وصلاتكش الفلوس", until="ثانيا، غدا هو البلاك", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="ما وصلاتنيش", at=0.6), dict(who=1, text="شوف الإيزي والطلب", at=3.5, bg="gold")]),
   dict(k="vs", at="ثانيا، غدا هو البلاك", until="مثال: إلى كان التلفاز", box=WIDE,
        right=dict(title="الثمن القديم", value="30", sub="يوم: أرخص ثمن", icon="calendar", color="green"),
        left=dict(title="التخفيض", value="؟", sub="قارن مع الشهر اللي فات", icon="shopping-cart", color="gold"), gap=4.0),
   dict(k="steps", at="مثال: إلى كان التلفاز", until="وإلى شريتي أونلاين", box=WIDE, steps=[
     ["الشهر اللي فات", "120 €"], ["طلعوه", "150 €"], ["التخفيض المكتوب", "120 €"]], gap=4.0, check_after=99, bad=True),
   dict(k="vs", at="وإلى شريتي أونلاين", until="ومن بعد البلاك فرايداي", box=WIDE,
        right=dict(title="أونلاين", value="14", sub="يوم باش ترجعها", icon="world", color="green"),
        left=dict(title="الحانوت", value="لا", sub="ماشي ديما", icon="building-store", color="red"), gap=4.0),
   dict(k="calendar", at="ومن بعد البلاك فرايداي", until="ورد البال من الروابط", box=WIDE, day=30, month=11, sub="السايبر مانداي"),
   dict(k="warn", text="ما تعطي حتى كود لحتى واحد", at="ورد البال من الروابط", until="ودابا نهار الاثنين", y=600),
   dict(k="calendar", at="ودابا نهار الاثنين", until="الأول: الدفعة الثانية", box=WIDE, day=30, month=11, sub="الاثنين: تلاتة ديال الآجال"),
   dict(k="people", at="الأول: الدفعة الثانية", until="الثاني: آبي سوشيال", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="عندي البارتيتا إيفا", at=0.8), dict(who=1, text="F24 قبل الاثنين", at=5.0, bg="gold")]),
   dict(k="big", text="63", sub="عام وخمسة شهور، على الأقل", at="الثاني: آبي سوشيال", until="والمبلغ كيوصل حتى"),
   dict(k="big", text="1.500 €", sub="خام فالشهر، الماكسيموم", at="والمبلغ كيوصل حتى", until="ورد البال: الإينبس"),
   dict(k="people", at="ورد البال: الإينبس", until="الثالث: الروطاماسيون", box=FULL, people=["elder", "clerk"],
        say=[dict(who=0, text="بديت نخدم فـ1998", at=0.8), dict(who=1, text="سول الباترونا قبل", at=4.0, bg="gold")]),
   dict(k="steps", at="الثالث: الروطاماسيون", until="ونزيد حاجة: الديكري", box=WIDE, steps=[
     ["كواطر: تسامح", "7/12"], ["كوينكيس: بلا تسامح", "30/11"]], gap=5.0, check_after=99),
   dict(k="map", **MED, route=["Casablanca", "Milano"], at="ونزيد حاجة: الديكري", until="والطلب كيديرو المشغل", box=R_BOX),
   dict(k="calendar", at="ونزيد حاجة: الديكري", until="والطلب كيديرو المشغل", box=L_BOX, day=7, month=12, sub="على 20:00"),
   dict(k="warn", text="الطلب ما كيتشراش", at="والطلب كيديرو المشغل", y=600),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="05 · الفلوس ديال دجنبر", src=S_DIC, items=[
   dict(k="chapter", num="05", title="الفلوس ديال دجنبر", at=0.2, until="نبداو بالثلاثاء"),
   dict(k="calendar", at="نبداو بالثلاثاء", until="وللبانسيونات الصغيرة", box=R_BOX, day=1, month=12, sub="البانسيون والتريديشيما"),
   dict(k="people", at="نبداو بالثلاثاء", until="وللبانسيونات الصغيرة", box=L_BOX, people=["elder"],
        say=[dict(who=0, text="جوج فمرة وحدة", at=1.5, bg="green")]),
   dict(k="big", text="154,94 €", sub="الزيادة الماكسيموم، بلا طلب", at="وللبانسيونات الصغيرة", until="ونفس النهار، واحد دجنبر"),
   dict(k="icons", at="ونفس النهار، واحد دجنبر", until="والعملية كاملة، من الطلب", box=ICO, items=[
     ["bolt", "غير الضو", "gold"], ["home", "غير الدار", "blue"], ["clock", "نهار خدمة واحد", "green"]], gap=4.0),
   dict(k="big", text="3", sub="سيمانات على الأكثر", at="والعملية كاملة، من الطلب", until="والكود ديال العداد"),
   dict(k="text", text="POD", at="والكود ديال العداد", until="ونصيحة: قبل ما تبدل", y=600, size=90),
   dict(k="people", at="ونصيحة: قبل ما تبدل", until="من بعد، التريديشيما", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="شحال الكيلوواط؟", at=0.6), dict(who=1, text="قارن قبل ما توقع", at=3.0, bg="gold")]),
   dict(k="vs", at="من بعد، التريديشيما", until="ونهار ستاش دجنبر", box=WIDE,
        right=dict(title="الدولة", value="15/12", sub="NoiPA", icon="building-bank", color="green"),
        left=dict(title="القطاع الخاص", value="CCNL", sub="عادة قبل العيد", icon="briefcase", color="gold"), gap=4.0),
   dict(k="calendar", at="ونهار ستاش دجنبر", until="الثانية: الكارطا", box=R_BOX, day=16, month=12, sub="الإيمو · الكارطا"),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="ونهار ستاش دجنبر", until="الثانية: الكارطا", box=L_BOX),
   dict(k="big", text="500 €", sub="الكارطا: أول خلاص قبل 16/12", at="الثانية: الكارطا", until="ومن بعد، ستاش وسبعطاش"),
   dict(k="calendar", at="ومن بعد، ستاش وسبعطاش", until="والمبلغ ديال هاد العام", box=WIDE, day="16·17", month=12, sub="الأسينيو أونيكو"),
   dict(k="bars", at="والمبلغ ديال هاد العام", until="وإلى تزاد ليك ولد", box=BAR, bars=[
     ["الماكسيموم", 203.8, "203,80 €", "green"], ["المينيموم", 58.3, "58,30 €", "gold"]]),
   dict(k="people", at="وإلى تزاد ليك ولد", until="وفالأخير، واحد وتلاتين", box=FULL, people=["hijab", "child"],
        say=[dict(who=0, text="1.000 أورو للمولود", at=1.0, bg="green")]),
   dict(k="calendar", at="وفالأخير، واحد وتلاتين", until="ثانيا، البونس ديال الماماوات", box=R_BOX, day=31, month=12, sub="الإيزي كيموت"),
   dict(k="map", view="south", pins=["Napoli", "Bari"], labels=False, at="وفالأخير، واحد وتلاتين", until="ثانيا، البونس ديال الماماوات", box=L_BOX),
   dict(k="big", text="720 €", sub="البونس ديال الماماوات: الطلب قبل 31/12", at="ثانيا، البونس ديال الماماوات", until="وما تنساش: فالديسو"),
   dict(k="map", **MED, at="وما تنساش: فالديسو", box=R_BOX),
   dict(k="icons", at="وما تنساش: فالديسو", box=L_BOX, items=[
     ["home", "الدار فالمغرب", "gold"], ["building-bank", "الحساب فالمغرب", "blue"]], gap=4.0),
 ]),
 dict(audio="F.wav", text=T["F"], chapter="06 · مثال: عائلة بتلاتة ديال الولاد", src=S_CASE, items=[
   dict(k="chapter", num="06", title="مثال: عائلة بتلاتة ديال الولاد", at=0.2, until="العائلة ديالنا ساكنة"),
   dict(k="map", view="north", pins=["Brescia"], labels=False, at="العائلة ديالنا ساكنة", until="الولد الأول: آدم", box=R_BOX),
   dict(k="people", at="العائلة ديالنا ساكنة", until="الولد الأول: آدم", box=L_BOX, people=["man", "hijab"],
        say=[dict(who=0, text="سمير وحنان", at=1.0)]),
   dict(k="people", at="الولد الأول: آدم", until="البنت الثانية: ياسمين", box=FULL, people=["child", "clerk"],
        say=[dict(who=0, text="آدم: تزاد فبريشيا", at=0.6), dict(who=1, text="ما كيتحسبش", at=9.0, bg="green")]),
   dict(k="map", **MED, route=["Casablanca", "Milano"], at="البنت الثانية: ياسمين", until="شحال قرات فإيطاليا؟", box=BIGMAP),
   dict(k="steps", at="شحال قرات فإيطاليا؟", until="الولد الثالث: عمر", box=WIDE, steps=[
     ["2025/26", "1"], ["2026/27", "2"], ["أقل من 3", "!"]], gap=3.0, check_after=99),
   dict(k="people", at="الولد الثالث: عمر", until="ودابا الحساب.", box=FULL, people=["student", "clerk"],
        say=[dict(who=0, text="عمر: الابتدائي كامل هنا", at=0.6), dict(who=1, text="ما كيتحسبش", at=6.0, bg="green")]),
   dict(k="bars", at="ودابا الحساب.", until="إذن، إلى كانو فالقسم", box=BAR, bars=[
     ["20 تلميذ", 6, "6", "blue"], ["25 تلميذ", 7, "7", "gold"], ["27 تلميذ", 8, "8", "green"]]),
   dict(k="text", text="السقف: 30% بلا ما يفوت", at="ودابا الحساب.", until="إذن، إلى كانو فالقسم", y=880, size=42),
   dict(k="map", view="north", pins=["Brescia"], labels=False, at="إذن، إلى كانو فالقسم", until="وإلى ما كانش الحل", box=BIGMAP),
   dict(k="big", text="الطاليانية", sub="دروس زايدة من الصندوق", at="وإلى ما كانش الحل", until="شنو خاص سمير وحنان"),
   dict(k="steps", at="شنو خاص سمير وحنان", until="وحنان كتقول", box=WIDE, steps=[
     ["الوراق ديال المسار", "1"], ["ياسمين: الطاليانية", "2"], ["التواريخ ديال التسجيل", "3"]], gap=6.0, check_after=99),
   dict(k="people", at="وحنان كتقول", until="وشحال ديال الوقت باقي؟", box=FULL, people=["hijab", "clerk"],
        say=[dict(who=0, text="واش غادي نخلص؟", at=0.6), dict(who=1, text="لا، غير إلى رفضتي", at=4.0, bg="green")]),
   dict(k="big", text="279", sub="يوم: من 26/11 حتى 1/9/2027", at="وشحال ديال الوقت باقي؟", until="ودابا الكتب."),
   dict(k="vs", at="ودابا الكتب.", until="وخمسة ديال الأخطاء", box=WIDE,
        right=dict(title="العتبة الجديدة", value="40.000 €", sub="الإيزي: 35.000 €", icon="file-text", color="green"),
        left=dict(title="العتبة القديمة", value="30.000 €", sub="فوقها", icon="file-text", color="red"), gap=4.0),
   dict(k="steps", at="وخمسة ديال الأخطاء", until="ودابا نمشيو للمغرب", box=WIDE, bad=True, steps=[
     ["الإشاعات", "1"], ["التسجيل فالأخير", "2"], ["الوراق ضاعو", "3"], ["رفض الدروس", "4"], ["نسيان الكتب", "5"]], gap=2.0, check_after=99),
   dict(k="map", **MED, at="ودابا نمشيو للمغرب", box=BIGMAP),
 ]),
 dict(audio="G.wav", text=T["G"], chapter="07 · من المغرب", src=S_MAR, items=[
   dict(k="chapter", num="07", title="من المغرب", at=0.2, until="الخبر الأول: الفلوس"),
   dict(k="map", **MED, route=["Milano", "Casablanca"], at="الخبر الأول: الفلوس", until="فالعام اللي فات، ألفين", box=BIGMAP),
   dict(k="big", text="8,6", sub="مليار أورو خرجو من إيطاليا فـ2025", at="فالعام اللي فات، ألفين", until="وفالربع الثاني"),
   dict(k="big", text="3,1%", sub="نقص فالربع الثاني ديال 2026", at="وفالربع الثاني", until="والمغرب فين؟"),
   dict(k="bars", at="والمغرب فين؟", until="والمنطقة ديال شمال", box=BAR, bars=[
     ["البنغلاديش", 19.4, "19,4%", "grey"], ["المغرب", 7.0, "7,0%", "green"], ["الهند", 6.8, "6,8%", "gold"]]),
   dict(k="text", text="12 شهر حتى يونيو 2026 · Banca d'Italia", at="والمغرب فين؟", until="والمنطقة ديال شمال", y=880, size=40),
   dict(k="map", view="med", hl=["MAR"], labels=False, at="والمنطقة ديال شمال", until="شنو كيعني هادشي ليك؟ إلى كتصيفط", box=BIGMAP),
   dict(k="people", at="شنو كيعني هادشي ليك؟ إلى كتصيفط", until="وحتى من الجهة المغربية", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="شحال العمولة؟", at=0.8), dict(who=1, text="قارن وخلي الوصل", at=4.0, bg="gold")]),
   dict(k="big", text="103", sub="مليار درهم حتى آخر شتنبر", at="وحتى من الجهة المغربية", until="الخبر الثاني: التكوين"),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Casablanca"], labels=False, at="الخبر الثاني: التكوين", until="ومن هاد البرامج", box=BIGMAP),
   dict(k="big", text="500", sub="خدام مغربي فالميكاترونيك", at="ومن هاد البرامج", until="والقاعدة ديالو"),
   dict(k="steps", at="والقاعدة ديالو", until="شنو كيعني هادشي ليك؟ إلى عندك", box=WIDE, steps=[
     ["التكوين فالمغرب", "1"], ["الكونطرا", "2"], ["الخدمة فإيطاليا", "3"]], gap=1.0, check_after=99),
   dict(k="people", at="شنو كيعني هادشي ليك؟ إلى عندك", until="والتذكير: قبل العطلة", box=FULL, people=["worker", "man"],
        say=[dict(who=0, text="خويا باغي يجي يخدم", at=0.8), dict(who=1, text="غير الطرق الرسمية", at=6.0, bg="green")]),
   dict(k="icons", at="والتذكير: قبل العطلة", until="إلى البيرميسو فالتجديد", box=ICO, items=[
     ["e-passport", "الباسبور", "gold"], ["id", "البطاقة الوطنية", "green"], ["license", "البيرميسو", "blue"]], gap=1.5),
   dict(k="map", **MED, route=["Milano", "Casablanca"], at="إلى البيرميسو فالتجديد", until="والبيرمي المغربي تقدر", box=BIGMAP),
   dict(k="people", at="والبيرمي المغربي تقدر", until="وزيد عليها", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="البيرمي والسوابق؟", at=0.6), dict(who=1, text="أونلاين", at=3.0, bg="green")]),
   dict(k="big", text="6", sub="شهور: العمر ديال الورقة للبريفيتورا", at="وزيد عليها", until="ودابا نمشيو للأسئلة"),
 ]),
 dict(audio="H.wav", text=T["H"], chapter="08 · سؤال وجواب", src=S_QA, items=[
   dict(k="chapter", num="08", title="سؤال وجواب", at=0.2, until="السؤال الأول"),
   dict(k="people", at="السؤال الأول", until="السؤال الثاني", box=FULL, people=["hijab", "clerk"],
        say=[dict(who=0, text="بنتي فالرابع ابتدائي", at=0.8), dict(who=1, text="ما كيتبدل والو", at=6.0, bg="green")]),
   dict(k="people", at="السؤال الثاني", until="وتذكر: إلى تزاد هنا", box=FULL, people=["man", "office"],
        say=[dict(who=0, text="تزاد هنا: كيتحسب؟", at=0.8), dict(who=1, text="عادة لا", at=6.0, bg="green")]),
   dict(k="big", text="18 - 19", sub="عام: الجنسية للولاد اللي تزادو هنا", at="وتذكر: إلى تزاد هنا", until="السؤال الثالث"),
   dict(k="people", at="السؤال الثالث", until="السؤال الرابع", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="غادي نخلص 200 أورو؟", at=0.8), dict(who=1, text="ماشي أوتوماتيكي", at=5.0, bg="green")]),
   dict(k="people", at="السؤال الرابع", until="السؤال الخامس", box=FULL, people=["elder", "office"],
        say=[dict(who=0, text="كيمنعو التسجيل؟", at=0.8), dict(who=1, text="لا", at=4.0, bg="green")]),
   dict(k="people", at="السؤال الخامس", until="السؤال السادس", box=FULL, people=["worker", "clerk"],
        say=[dict(who=0, text="الإيزي 33.000", at=0.8), dict(who=1, text="ممكن، سول الكوموني", at=5.0, bg="green")]),
   dict(k="calendar", at="السؤال السادس", until="السؤال السابع", box=R_BOX, day=27, month=11, sub="الأدي"),
   dict(k="people", at="السؤال السادس", until="السؤال السابع", box=L_BOX, people=["girl"],
        say=[dict(who=0, text="الأدي ما وصلاتنيش", at=0.8)]),
   dict(k="people", at="السؤال السابع", until="السؤال الثامن", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="عندي الكونطرا", at=0.8), dict(who=1, text="المشغل كينقصو", at=5.0, bg="green")]),
   dict(k="map", **MED, route=["Milano", "Casablanca"], at="السؤال الثامن", until="السؤال التاسع", box=R_BOX),
   dict(k="people", at="السؤال الثامن", until="السؤال التاسع", box=L_BOX, people=["man"],
        say=[dict(who=0, text="قارن العمولة", at=3.0, bg="gold")]),
   dict(k="people", at="السؤال التاسع", until="السؤال العاشر", box=FULL, people=["student", "clerk"],
        say=[dict(who=0, text="عطيني ألفين أورو؟", at=0.8), dict(who=1, text="نصاب", at=5.0, bg="red")]),
   dict(k="people", at="السؤال العاشر", until="السؤال الحادي عشر", box=FULL, people=["hijab", "man"],
        say=[dict(who=0, text="التخفيض حقيقي؟", at=0.8), dict(who=1, text="شوف 30 يوم", at=4.0, bg="gold")]),
   dict(k="people", at="السؤال الحادي عشر", until="السؤال الثاني عشر", box=FULL, people=["elder", "clerk"],
        say=[dict(who=0, text="خاصني نطلب الزيادة؟", at=0.8), dict(who=1, text="لا، بوحدها", at=5.0, bg="green")]),
   dict(k="people", at="السؤال الثاني عشر", until="وإلى عندك سؤال آخر", box=FULL, people=["woman", "office"],
        say=[dict(who=0, text="الضو فنهار؟", at=0.8), dict(who=1, text="غير المرحلة التقنية", at=4.0, bg="gold")]),
   dict(k="people", at="وإلى عندك سؤال آخر", box=FULL, people=["girl", "elder", "hijab"],
        say=[dict(who=0, text="كتب سؤالك فالكومونتير", at=0.8, bg="green")]),
 ]),
 dict(audio="I.wav", text=T["I"], chapter="09 · الخلاصة والتواريخ", src=S_HOME, items=[
   dict(k="head", text="الخلاصة", at=0.2, until="واحد: المرسوم"),
   dict(k="rows", at="واحد: المرسوم", until="ودابا التواريخ ديال الأيام", y=300, gap=118, size=46, rows=[
     ("المدرسة: السقف فالأقسام الأولى", "30%", "واحد: المرسوم"),
     ("الواليدين: دروس بالمجان", "200 - 1.000 €", "جوج: الواليدين."),
     ("الوجه المغطي ممنوع", "200 - 1.000 €", "تلاتة: الوجه المغطي"),
     ("المساعدة ديال الكتب", "40.000 €", "ربعة: المساعدة"),
     ("المغرب الثاني فالتحويلات", "7%", "خمسة: من المغرب"),
   ]),
   dict(k="steps", at="ودابا التواريخ ديال الأيام", until="الثلاثاء واحد دجنبر:", box=WIDE, steps=[
     ["الأدي · البلاك فرايداي", "27/11"], ["الأكونطو · آبي سوشيال", "30/11"]], gap=4.0, check_after=99),
   dict(k="steps", at="الثلاثاء واحد دجنبر:", until="ستاش دجنبر: الإيمو", box=WIDE, steps=[
     ["البانسيون · الضو", "1/12"], ["الديكري فلوسي", "7/12"], ["التريديشيما ديال الدولة", "15/12"]], gap=4.0, check_after=99),
   dict(k="steps", at="ستاش دجنبر: الإيمو", until="وحاجة عملية: دير ورقة", box=WIDE, steps=[
     ["الإيمو · الكارطا", "16/12"], ["الأسينيو أونيكو", "17/12"], ["الإيزي · الماماوات · الكريش", "31/12"]], gap=4.0, check_after=99),
   dict(k="icons", at="وحاجة عملية: دير ورقة", until="وإلى فاتك شي فيديو", box=ICO, items=[
     ["calendar", "الأجندة", "blue"], ["phone", "التيليفون", "green"]], gap=2.0),
   dict(k="icons", at="وإلى فاتك شي فيديو", until="وكل نهار كاين", box=ICO, items=[
     ["license", "تبديل البيرمي", "blue"], ["id", "البيرميسو", "gold"], ["heart", "الجنسية للولاد", "green"], ["plane", "الفيزا", "blue"]], cols=4, gap=2.0),
   dict(k="steps", at="وكل نهار كاين", until="ومن غدا، غادي نتبعو", box=WIDE, steps=[
     ["فيديو قصير", "13:00"], ["النشرة الطويلة", "16:30"], ["فيديو قصير", "19:00"], ["الشرح الكامل", "20:30"]], gap=2.0, check_after=99),
   dict(k="map", view="italy", hl=["Lazio"], pins=["Roma"], labels=False, at="ومن غدا، غادي نتبعو", until="ونعاودو نقولو", box=BIGMAP),
   dict(k="people", at="ونعاودو نقولو", until="وتذكير صغير", box=FULL, people=["clerk", "woman"],
        say=[dict(who=0, text="سول الباترونا ولا المدرسة", at=1.0, bg="green")]),
   dict(k="map", view="italy", pins=["Milano", "Roma", "Napoli"], labels=False, at="وتذكير صغير", until="وحاجة أخيرة", box=R_BOX),
   dict(k="people", at="وتذكير صغير", until="وحاجة أخيرة", box=L_BOX, people=["hijab"],
        say=[dict(who=0, text="صيفطيه للعائلة", at=1.0, bg="green")]),
   dict(k="warn", text="ما تعطي السبيد ولا الكود لحتى واحد", at="وحاجة أخيرة", until="وإلى عجبك هاد الفيديو", y=640),
   dict(k="cta", at="وإلى عجبك هاد الفيديو", until="وكتب لينا فالكومونتير", text="ابوني فالقناة", sub="وفعل الجرس"),
   dict(k="people", at="وكتب لينا فالكومونتير", box=FULL, people=["girl", "worker", "hijab"],
        say=[dict(who=1, text="شنو فادك أكثر؟", at=0.8), dict(who=2, text="صيفطو لشي واحد", at=6.0, bg="green")]),
 ]),
]

THUMB = dict(
  title=[("ولدك فالمدرسة؟", (236, 196, 96)), "السقف ديال التلاميذ الأجانب", "شكون كيتحسب ومن إمتى"],
  num="30%", numsub="فالقسم الأول",
  bottom="مغاربة إيطاليا · خبار مفيدة بالدارجة",
)
