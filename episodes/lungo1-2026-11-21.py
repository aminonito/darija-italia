import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-21.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo1-2026-11-21-final")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = {k: v.replace("گ", "ك") for k, v in JOB["blocks"].items()}
# E: frase con la soglia ISEE (9.796 €) tagliata dall'audio (72,66-76,04 s): Whisper sentiva "1796"; la cifra resta a schermo
T["E"] = T["E"].replace(" هاد العام العتبة هي تسعود آلاف وسبعمية وستة وتسعين أورو.", "")

S_HOME = "مغاربة إيطاليا · خبار مفيدة بالدارجة"
S_PIAT = "D.Lgs. 208/2026 (GU n. 266 del 14/11/2026) · Min. Lavoro 16/11 · Lavorosì · La Legge per Tutti"
S_TFR = "Assolombarda 17/11 · Il Sole 24 Ore 18/11 · EC News 20/11 · Money.it 19/11 · Open / La Nazione 19/11"
S_MAN = "Sky TG24 17/11 · ilpoliticoweb · QuiFinanza · Open · Tgcom24 18/11 · Money.it 20/11 (Codice disabilità)"
S_EN = "ARERA 17/11/2026 (Rapporto 413/2026) · Helpconsumatori · MIMIT via Agenzia Opinione e L'Adige 21/11 · Edotto"
S_CASO = "D.Lgs. 208/2026 artt. 5, 8, 9, 10, 13, 17-18 · Min. Lavoro · La Legge per Tutti 19/11"
S_MAR = "Challenge · Bladi · Boursenews 19-20/11 · Bank Al-Maghrib · Hespress · NARSA via Challenge/Hespress"
S_QA = "Fonti dei capitoli 01-07 · Min. Lavoro circ. 7185/2026 (flussi) · INPS (Carta Dedicata a te)"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850); FULL = (160, 300, 1760, 860)
WIDE = (260, 220, 1660, 830); ICO = (160, 330, 1760, 860); BAR = (160, 300, 1760, 840)
MED = dict(view="med", hl=["ITA", "MAR"], labels=False)

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="00 · أخبار السيمانة", src=S_HOME, items=[
   dict(k="head", text="نشرة السيمانة", at=0.2, until="شنو كاين اليوم؟", sub="السبت 21 نونبر 2026"),
   dict(k="people", at=0.6, until="شنو كاين اليوم؟", box=FULL, people=["worker", "hijab", "elder"],
        say=[dict(who=0, text="شنو الجديد هاد السيمانة؟", at=0.8), dict(who=2, text="خبار بالأرقام", at=4.0, bg="green")]),
   dict(k="rows", at="شنو كاين اليوم؟", until="ومن بعد، مثال عملي", y=280, gap=125, size=50, rows=[
     ("الريدر والأبليكاسيونات", "2/12", "الخبر الأول للناس"),
     ("الزيادة ديال التي إف إر", "5,2%", "الخبر التاني على التي"),
     ("الميزانية ديال 2027", "?", "الخبر التالت على الميزانية"),
     ("البونس ديال الضو والمازوط", "23/11", "الخبر الرابع على الضو"),
   ]),
   dict(k="map", **MED, route=["Milano", "Casablanca"], at="ومن بعد، مثال عملي", until="قبل ما نبداو، جوج", box=(160, 200, 1760, 880)),
   dict(k="icons", at="قبل ما نبداو، جوج", until="يالاه نبداو بالخبر", box=ICO, items=[
     ["file-certificate", "جوج مصادر على الأقل", "green"], ["alert-triangle", "ماشي استشارة", "gold"], ["users", "سول السانديكا", "blue"]], gap=2.5),
   dict(k="chapter", num="01", title="الريدر والأبليكاسيونات", at="يالاه نبداو بالخبر", until="وتنشر فالجريدة الرسمية"),
   dict(k="calendar", at="وتنشر فالجريدة الرسمية", until="شكون كيهمو؟ كيهم", box=R_BOX, day=2, month=12, sub="كيبدا القانون"),
   dict(k="steps", at="وتنشر فالجريدة الرسمية", until="شكون كيهمو؟ كيهم", box=L_BOX, steps=[
     ["القاعدة الأوروبية", "EU"], ["الجريدة الرسمية", "14/11"], ["التنفيذ", "2/12"]], gap=2.5, check_after=0.6),
   dict(k="people", at="شكون كيهمو؟ كيهم", until="أشنو هو الجديد الكبير؟", box=R_BOX, people=["worker", "man"],
        say=[dict(who=0, text="أنا ريدر", at=0.8), dict(who=1, text="وأنا خدام بالتطبيق", at=5.0)]),
   dict(k="icons", at="سواء كان عندو كونطرا", until="أشنو هو الجديد الكبير؟", box=L_BOX, items=[
     ["file-text", "كونطرا", "green"], ["briefcase", "بارتيتا إيفا", "gold"], ["users", "تعاون", "blue"]], gap=2.0),
   dict(k="vs", at="أشنو هو الجديد الكبير؟", until="ولكن رد البال: إلى كنتي", box=WIDE,
        right=dict(title="قبل", value="نتا", sub="خاصك تبين", icon="user", color="grey"),
        left=dict(title="من 2/12", value="المنصة", sub="هي اللي خاصها تبين", icon="building-store", color="green"), gap=6.0),
   dict(k="warn", text="كتحسب غير من 2 دجنبر وطالع", at="ولكن رد البال: إلى كنتي", until="مثلا، إلى كنتي خدام", y=640),
   dict(k="map", view="north", pins=["Milano"], labels=False, at="مثلا، إلى كنتي خدام", box=L_BOX),
   dict(k="people", at="مثلا، إلى كنتي خدام", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="خدام من مارس", at=0.8), dict(who=0, text="كتحسب من جوج دجنبر", at=5.0, bg="gold")]),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="01 · الحقوق الجديدة ديال الريدر", src=S_PIAT, items=[
   dict(k="head", text="الحقوق الجديدة", at=0.2, until="الحق الأول: المعلومات", sub="القانون 208/2026"),
   dict(k="people", at=0.6, until="الحق الأول: المعلومات", box=FULL, people=["worker", "girl"],
        say=[dict(who=0, text="شنو هي الحقوق ديالي؟", at=0.8)]),
   dict(k="icons", at="الحق الأول: المعلومات", until="الحق التاني: القرارات", box=ICO, items=[
     ["map-pin", "المراقبة", "blue"], ["coin-euro", "الخلاص", "green"], ["chart-bar", "التنقيط", "gold"]], gap=2.5),
   dict(k="people", at="الحق التاني: القرارات", until="كاين استثناء واحد", box=R_BOX, people=["clerk"],
        say=[dict(who=0, text="القرار بيد بنادم", at=1.0, bg="green")]),
   dict(k="vs", at="الحق التاني: القرارات", until="كاين استثناء واحد", box=L_BOX,
        right=dict(title="بنادم", value="OK", sub="", icon="user", color="green"),
        left=dict(title="الآلة بوحدها", value="باطل", sub="", icon="x", color="red"), gap=6.0),
   dict(k="big", text="72", at="كاين استثناء واحد", until="الحق التالت: الشرح", y=430, size=240, color=GOLD, sub="ساعة · توقيف قصير"),
   dict(k="steps", at="الحق التالت: الشرح", until="الحق الخامس: إلى", box=WIDE, steps=[
     ["الشرح بالكتابة", "15"], ["المراجعة", "14"], ["التصحيح ولا التعويض", "14"]], gap=4.0, check_after=0.6),
   dict(k="head", text="بالأيام", at="الحق التالت: الشرح", until="الحق الخامس: إلى", y=180, size=60),
   dict(k="calendar", at="الحق الخامس: إلى", until="وكاين حتى حماية", box=R_BOX, day=10, month="أيام", sub="الأسباب ديال السد"),
   dict(k="people", at="الحق الخامس: إلى", until="وكاين حتى حماية", box=L_BOX, people=["man"],
        say=[dict(who=0, text="علاش سديتو الكونط؟", at=1.0)]),
   dict(k="icons", at="وكاين حتى حماية", until="وهاد القانون كيضيف", box=ICO, items=[
     ["x", "الحالة النفسية", "red"], ["x", "الهضرة الخاصة", "red"], ["x", "الأصل والإقامة", "red"], ["x", "الدين والصحة", "red"]], gap=2.5),
   dict(k="icons", at="وهاد القانون كيضيف", until="وحتى التنقيط والتقييمات", box=ICO, items=[
     ["heart", "الصحة", "green"], ["alert-triangle", "الضغط والتعب", "gold"], ["users", "ضد التحرش", "blue"]], gap=2.5),
   dict(k="text", text="التنقيط ديالك معاك", at="وحتى التنقيط والتقييمات", until="وشكون كيراقب هادشي؟", y=520, size=80, color=GOLD),
   dict(k="big", text="30.000 €", at="وشكون كيراقب هادشي؟", until="والمنصة ما عندهاش الحق", y=430, size=220, color=RED, sub="عقوبة على المنصة · فبعض الحالات"),
   dict(k="people", at="والمنصة ما عندهاش الحق", until="إلى ما احترموش الحقوق", box=FULL, people=["worker", "office"],
        say=[dict(who=1, text="ما عندكش الحق تعاقبو", at=1.5, bg="red")]),
   dict(k="steps", at="إلى ما احترموش الحقوق", until="ملاحظة مهمة: هاد القانون", box=WIDE, steps=[
     ["طلب بالكتابة", "1"], ["شكاية · الإسبيتوراتو", "2"], ["لجنة رسمية", "3"], ["المحكمة", "4"]], gap=4.5, check_after=0.6),
   dict(k="map", view="italy", pins=["Milano", "Roma", "Napoli"], labels=False, at="ملاحظة مهمة: هاد القانون", box=L_BOX),
   dict(k="people", at="ملاحظة مهمة: هاد القانون", box=R_BOX, people=["clerk"],
        say=[dict(who=0, text="الخلاص فالاتفاقيات", at=1.0, bg="gold")]),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="02 · التي إف إر والطرد فالواتساب", src=S_TFR, items=[
   dict(k="chapter", num="02", title="التي إف إر طلع", at=0.1, until="هو الفلوس اللي كيجمع"),
   dict(k="people", at="هو الفلوس اللي كيجمع", until="هاد الفلوس ما كيبقاوش", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="شحال تجمع ليا؟", at=1.0), dict(who=1, text="شهر على كل عام", at=6.0, bg="green")]),
   dict(k="steps", at="والزيادة كتحسب هكا", until="ونهار سبعطاش نونبر", box=WIDE, steps=[
     ["ثابت فالعام", "1,5%"], ["من الغلا", "75%"]], gap=3.0, check_after=0.6),
   dict(k="bars", at="ونهار سبعطاش نونبر", until="مثال باش يوضح. خديجة", box=BAR, bars=[
     ["شتنبر", 4.29, "4,29%", "grey"], ["أكتوبر", 5.23, "5,23%", "gold"]], gap=3.0),
   dict(k="head", text="الزيادة على التي إف إر", at="ونهار سبعطاش نونبر", until="مثال باش يوضح. خديجة", y=180, size=60, sub="الغلا فأكتوبر: 5,5 فالمية"),
   dict(k="map", view="north", pins=["Brescia", "Bologna"], labels=False, at="مثال باش يوضح. خديجة", until="ومثال آخر: رشيد", box=L_BOX),
   dict(k="steps", at="مثال باش يوضح. خديجة", until="ومثال آخر: رشيد", box=R_BOX, steps=[
     ["التي إف إر", "8.000 €"], ["الزيادة", "418,80 €"], ["الضريبة", "71,20 €"], ["الصافي", "347,60 €"]], gap=3.0, check_after=0.6),
   dict(k="vs", at="ومثال آخر: رشيد", until="واش هادشي مزيان؟", box=WIDE,
        right=dict(title="الزيادة", value="785 €", sub="قبل الضريبة", icon="trending-up", color="gold"),
        left=dict(title="الصافي", value="652 €", sub="من بعد الضريبة", icon="wallet", color="green"), gap=4.0),
   dict(k="people", at="واش هادشي مزيان؟", until="شنو تدير؟ أولا", box=FULL, people=["hijab", "man"],
        say=[dict(who=0, text="الغلا طلع كثر", at=1.0, bg="red")]),
   dict(k="icons", at="شنو تدير؟ أولا", until="دابا خبر صغير", box=ICO, items=[
     ["receipt", "البوسطا باغا", "gold"], ["users", "المعلم ولا الكونسولينتي", "blue"], ["building-bank", "السانديكا", "green"]], gap=3.0),
   dict(k="head", text="الطرد فالواتساب", at="دابا خبر صغير", until="القصة: خدام طاح", sub="محكمة الشغل · لا سبيتسيا"),
   dict(k="map", view="north", pins=["Genova", "Firenze"], labels=False, at="القصة: خدام طاح", until="علاش؟ القانون كيقول", box=L_BOX),
   dict(k="people", at="القصة: خدام طاح", until="علاش؟ القانون كيقول", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="جاني الطرد فالواتساب", at=1.0, bg="red")]),
   dict(k="icons", at="علاش؟ القانون كيقول", until="النصيحة: إلى وصلاتك", box=ICO, items=[
     ["user", "شكون صيفط", "green"], ["file-text", "باغي يسالي", "green"], ["check", "توصل بيها", "green"]], gap=3.0),
   dict(k="people", at="النصيحة: إلى وصلاتك", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="نتجاهلها؟", at=1.0), dict(who=1, text="سير للسانديكا ديريكت", at=4.0, bg="green")]),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="03 · الميزانية ديال 2027", src=S_MAN, items=[
   dict(k="chapter", num="03", title="الميزانية: باقي مشروع", at=0.1, until="أول حاجة خاصك تعرفها"),
   dict(k="warn", text="باقي ماشي قانون", at="أول حاجة خاصك تعرفها", until="فين وصلات؟ دابا", y=640),
   dict(k="head", text="لجنة الميزانية · مجلس النواب", at="فين وصلات؟ دابا", until="الأحزاب حطو أكثر"),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="ومن بعد كاين تواريخ", until="شنو اللي تبدل هاد السيمانة؟", box=L_BOX),
   dict(k="steps", at="ومن بعد كاين تواريخ", until="شنو اللي تبدل هاد السيمانة؟", box=R_BOX, steps=[
     ["التعديلات", "17/11"], ["النواب", "23/12"], ["الشيوخ", "31/12"]], gap=4.0, check_after=0.6),
   dict(k="big", text="6.600", at="الأحزاب حطو أكثر", until="ومن بعد كاين تواريخ", y=430, size=220, color=GOLD, sub="تعديل تقريبا"),
   dict(k="people", at="شنو اللي تبدل هاد السيمانة؟", until="والحاجة اللي باقية", box=FULL, people=["elder", "man"],
        say=[dict(who=0, text="التقاعد فـ64؟", at=1.0), dict(who=1, text="ما دخلش فالتعديلات", at=6.0, bg="red")]),
   dict(k="calendar", at="والحاجة اللي باقية", until="ومن الاقتراحات اللي كتناقش", box=WIDE, day=1, month="شهر", sub="زيادة فسن التقاعد · العام الجاي"),
   dict(k="bars", at="الأول: البانسيونات", until="التاني: الضريبة", box=BAR, bars=[
     ["المشروع", 2447, "2.447 €", "gold"], ["الاقتراح", 3000, "3.000 €", "blue"]], gap=3.0),
   dict(k="head", text="الزيادة كاملة على البانسيون حتى", at="الأول: البانسيونات", until="التاني: الضريبة", y=180, size=56, sub="خام فالشهر"),
   dict(k="people", at="يعني إلى كانت البانسيون", until="النصيحة: إلى شفتي", box=FULL, people=["elder", "girl"],
        say=[dict(who=0, text="والبانسيون ديالي؟", at=1.0), dict(who=1, text="نتسناو التصويت", at=5.0, bg="gold")]),
   dict(k="vs", at="التاني: الضريبة", until="التالت: كاين اقتراح", box=WIDE,
        right=dict(title="تحت 30 عام", value="1%", sub="2.500 €", icon="percentage", color="green"),
        left=dict(title="الخدامين الجداد", value="؟", sub="غير اقتراح", icon="user", color="grey"), gap=6.0),
   dict(k="icons", at="التالت: كاين اقتراح", until="يعني إلى كانت البانسيون", box=ICO, items=[
     ["receipt-tax", "التسوية من جديد", "gold"], ["credit-card", "الكارطا ديال 300", "gold"]], gap=4.0),
   dict(k="people", at="النصيحة: إلى شفتي", until="ودابا خبر آخر من مجلس", box=FULL, people=["hijab", "man"],
        say=[dict(who=0, text="خرج بونس جديد؟", at=1.0), dict(who=1, text="حتى حاجة ما تقررات", at=5.0, bg="red")]),
   dict(k="head", text="قانون الإعاقة", at="ودابا خبر آخر من مجلس", until="ولكن رد البال: هادي غير", sub="الموافقة الأولى · 18/11"),
   dict(k="steps", at="ولكن رد البال: هادي غير", until="شنو كيتبدل للعائلات", box=WIDE, steps=[
     ["مجلس الوزراء", "1"], ["المؤسسات والبرلمان", "2"], ["الموافقة النهائية", "3"]], gap=3.0, check_after=0.6),
   dict(k="people", at="شنو كيتبدل للعائلات", box=R_BOX, people=["woman", "clerk"],
        say=[dict(who=0, text="الرخص ديال 104؟", at=1.0), dict(who=1, text="كيبقاو", at=5.0, bg="green")]),
   dict(k="map", view="italy", pins=["Torino", "Bari"], labels=False, at="شنو كيتبدل للعائلات", box=L_BOX),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="04 · البونس ديال الضو والمازوط", src=S_EN, items=[
   dict(k="chapter", num="04", title="البونس ديال الضو والغاز", at=0.1, until="شنو قالت؟ تعطاو"),
   dict(k="big", text="4,3", at="شنو قالت؟ تعطاو", until="تقريبا جوج مليون", y=430, size=260, color=GOLD, sub="مليون بونس · 2025"),
   dict(k="bars", at="تقريبا جوج مليون", until="والقيمة ديالهم كاملين", box=BAR, bars=[
     ["الضو", 2.7, "2,7", "gold"], ["الغاز", 1.6, "1,6", "blue"]], gap=3.0),
   dict(k="head", text="عائلة · بالمليون", at="تقريبا جوج مليون", until="والقيمة ديالهم كاملين", y=180, size=60),
   dict(k="vs", at="والقيمة ديالهم كاملين", until="وكاين بونس آخر", box=WIDE,
        right=dict(title="الضو", value="30%", sub="من الفاتورة", icon="bolt", color="gold"),
        left=dict(title="الغاز", value="15%", sub="من الفاتورة", icon="flame", color="blue"), gap=5.0),
   dict(k="people", at="وكاين بونس آخر", until="ولكن الرقم الكلي", box=R_BOX, people=["elder", "woman"],
        say=[dict(who=1, text="الآلة ديال بابا كتاكل الضو", at=1.0)]),
   dict(k="big", text="86.000", at="هاد البونس طلع", until="ولكن الرقم الكلي", y=430, x=560, size=150, color=GREEN, sub="عائلة"),
   dict(k="map", view="italy", pins=["Napoli", "Milano", "Roma"], labels=False, at="ولكن الرقم الكلي", until="كيفاش كتاخد البونس؟", box=L_BOX),
   dict(k="people", at="ولكن الرقم الكلي", until="كيفاش كتاخد البونس؟", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="عندي الحق وما خديتوش", at=1.0, bg="gold")]),
   dict(k="bars", at="كيفاش كتاخد البونس؟", until="النصيحة العملية: الإيزي", box=BAR, bars=[
     ["العتبة العادية", 9796, "9.796 €", "gold"], ["4 دراري ولا كثر", 20000, "20.000 €", "green"]], gap=4.0),
   dict(k="head", text="الإيزي · بلا طلب", at="كيفاش كتاخد البونس؟", until="النصيحة العملية: الإيزي", y=180, size=60),
   dict(k="calendar", at="النصيحة العملية: الإيزي", until="وإلى كان عندك الإيزي", box=WIDE, day=1, month=1, sub="الإيزي الجديد · 2027"),
   dict(k="people", at="وإلى كان عندك الإيزي", until="ودابا المازوط.", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="ما بان حتى خصم", at=1.0), dict(who=1, text="نشوفو الإيزي", at=5.0, bg="green")]),
   dict(k="big", text="23/11", at="ودابا المازوط.", until="شحال كيتباع اليوم؟", y=430, size=240, color=RED, sub="آخر نهار ديال الخصم"),
   dict(k="vs", at="شحال كيتباع اليوم؟", until="مثال: إلى عمرتي", box=WIDE,
        right=dict(title="المازوط", value="2,198 €", sub="اللتر · سيلف", icon="gas-station", color="gold"),
        left=dict(title="الليصانص", value="1,942 €", sub="اللتر · سيلف", icon="gas-station", color="blue"), gap=4.0),
   dict(k="steps", at="مثال: إلى عمرتي", until="وخبر صغير آخر", box=WIDE, steps=[
     ["50 لتر ديال المازوط", "109,90 €"], ["بلا الخصم", "+2,44 €"]], gap=4.0, check_after=0.6),
   dict(k="people", at="وخبر صغير آخر", box=FULL, people=["office", "woman"],
        say=[dict(who=1, text="الفاتورة غادي تنقص؟", at=1.5), dict(who=0, text="ماشي حد أقصى", at=8.0, bg="red")]),
 ]),
 dict(audio="F.wav", text=T["F"], chapter="05 · مثال عملي: يوسف الريدر", src=S_CASO, items=[
   dict(k="chapter", num="05", title="مثال: يوسف الريدر", at=0.1, until="يوسف عندو ستة وعشرين"),
   dict(k="map", view="north", pins=["Milano"], labels=False, at="يوسف عندو ستة وعشرين", until="التطبيق هو اللي كيعطيه", box=L_BOX),
   dict(k="people", at="يوسف عندو ستة وعشرين", until="الخطوة الأولى: من جوج", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="أنا يوسف، ريدر فميلانو", at=1.0)]),
   dict(k="icons", at="التطبيق هو اللي كيعطيه", until="الخطوة الأولى: من جوج", box=L_BOX, items=[
     ["clipboard-check", "الطلبيات", "gold"], ["map-pin", "الجي بي إس", "blue"], ["chart-bar", "التنقيط", "gold"]], gap=2.0),
   dict(k="vs", at="الخطوة الأولى: من جوج", until="الخطوة التانية: المعلومات", box=WIDE,
        right=dict(title="مارس - نونبر", value="؟", sub="القاعدة القديمة", icon="calendar", color="grey"),
        left=dict(title="من 2/12", value="تابع", sub="إلى ما بيناتش المنصة العكس", icon="check", color="green"), gap=6.0),
   dict(k="people", at="الخطوة التانية: المعلومات", until="الخطوة التالتة: نفترضو", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="كيفاش كيتحسب الخلاص؟", at=1.0), dict(who=1, text="من النهار الأول", at=6.0, bg="green")]),
   dict(k="calendar", at="الخطوة التالتة: نفترضو", until="يوسف كيكتب للمنصة", box=R_BOX, day=3, month=12, sub="الكونط موقوف 5 أيام"),
   dict(k="vs", at="خمسة ديال الأيام كتفوت", until="يوسف كيكتب للمنصة", box=L_BOX,
        right=dict(title="الحد", value="72", sub="ساعة", icon="clock", color="gold"),
        left=dict(title="التوقيف", value="120", sub="ساعة", icon="alert-triangle", color="red"), gap=2.0),
   dict(k="steps", at="يوسف كيكتب للمنصة", until="الخطوة الرابعة: نهار", box=WIDE, steps=[
     ["طلب الشرح", "3/12"], ["آخر أجل ديال الجواب", "18/12"]], gap=4.0, check_after=0.6),
   dict(k="steps", at="الخطوة الرابعة: نهار", until="الخطوة الخامسة: نفترضو", box=WIDE, steps=[
     ["طلب المراجعة", "4/12"], ["آخر أجل ديال الجواب", "18/12"]], gap=4.0, check_after=0.6),
   dict(k="steps", at="الخطوة الخامسة: نفترضو", until="الخطوة السادسة: إلى", box=WIDE, steps=[
     ["الكونط تسد", "10/12"], ["آخر أجل ديال الأسباب", "20/12"]], gap=4.0, check_after=0.6),
   dict(k="map", view="north", pins=["Milano", "Torino"], labels=False, at="الخطوة السادسة: إلى", until="وزيد على هادشي", box=L_BOX),
   dict(k="icons", at="الخطوة السادسة: إلى", until="وزيد على هادشي", box=R_BOX, items=[
     ["users", "السانديكا", "green"], ["building-bank", "الإسبيتوراتو", "blue"], ["scale", "المحكمة", "gold"]], gap=3.0),
   dict(k="people", at="وزيد على هادشي", until="شنو خاص يوسف يحتافظ", box=FULL, people=["office", "worker", "man"],
        say=[dict(who=1, text="شاورو معانا قبل", at=1.5, bg="gold")]),
   dict(k="icons", at="شنو خاص يوسف يحتافظ", until="وعلاش هادشي مهم", box=ICO, items=[
     ["camera", "صور الشاشة", "gold"], ["mail", "الرسائل", "gold"], ["receipt", "الكشوفات", "gold"], ["file-text", "نسخ الطلبات", "gold"]], gap=2.5),
   dict(k="map", **MED, route=["Milano", "Casablanca"], at="وعلاش هادشي مهم", until="غلطات خاصك تبعد", box=L_BOX),
   dict(k="people", at="وعلاش هادشي مهم", until="غلطات خاصك تبعد", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="البيرميسو مرتبط بالخدمة", at=1.5, bg="gold")]),
   dict(k="icons", at="غلطات خاصك تبعد", until="وإلى كنتي ريدر", box=ICO, items=[
     ["phone", "غير بالهضرة", "red"], ["trash", "مسح الأبليكاسيون", "red"], ["clock", "التعطيل", "red"], ["cash", "اللي كيطلب الفلوس", "red"]], gap=2.5),
   dict(k="people", at="وإلى كنتي ريدر", box=FULL, people=["girl", "worker"],
        say=[dict(who=0, text="كتب لينا المشكل ديالك", at=1.0, bg="green")]),
 ]),
 dict(audio="G.wav", text=T["G"], chapter="06 · من المغرب", src=S_MAR, items=[
   dict(k="chapter", num="06", title="من المغرب", at=0.1, until="الخبر الأول: قرض جديد"),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Casablanca"], at="الخبر الأول: قرض جديد", until="هاد العرض كيهم", box=(160, 200, 1760, 880)),
   dict(k="icons", at="هاد العرض كيهم", until="كيفاش كيخدم؟", box=ICO, items=[
     ["plane", "المغاربة ديال الخارج", "gold"], ["user", "النساء", "green"], ["droplet", "المشاريع الخضرا", "green"]], gap=3.0),
   dict(k="bars", at="كيفاش كيخدم؟", until="مثال باش يوضح، وهادا", box=BAR, bars=[
     ["البنكة", 50, "50%", "blue"], ["تمويلكوم", 50, "50%", "gold"]], gap=3.0),
   dict(k="head", text="فائدة 2 فالمية · حتى 15 مليون درهم", at="والفائدة على هاد الجزء", until="مثال باش يوضح، وهادا", y=180, size=56),
   dict(k="map", **MED, route=["Torino", "Beni Mellal"], at="مثال باش يوضح، وهادا", until="ولكن رد البال: هادا قرض", box=L_BOX),
   dict(k="steps", at="مثال باش يوضح، وهادا", until="ولكن رد البال: هادا قرض", box=R_BOX, steps=[
     ["المشروع", "1.000.000"], ["تمويلكوم", "500.000"], ["الفائدة فالعام", "10.000"]], gap=3.5, check_after=0.6),
   dict(k="people", at="ولكن رد البال: هادا قرض", until="الخبر التاني: الدرهم", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="نشري بيه دار؟", at=1.0), dict(who=1, text="لا، غير المشاريع", at=4.0, bg="red")]),
   dict(k="vs", at="الخبر التاني: الدرهم", until="والسعر المرجعي دابا", box=WIDE,
        right=dict(title="الدرهم / الأورو", value="0,9%", sub="طلع فالسيمانة", icon="trending-up", color="green"),
        left=dict(title="الدرهم / الدولار", value="0,3%", sub="نزل", icon="trending-down", color="red"), gap=5.0),
   dict(k="big", text="10.900", at="والسعر المرجعي دابا", until="وهادا هو السعر المرجعي", y=430, size=220, color=GOLD, sub="درهم تقريبا مقابل ألف أورو"),
   dict(k="map", **MED, route=["Milano", "Casablanca"], at="وهادا هو السعر المرجعي", until="الخبر التالت: الماتريكولا", box=L_BOX),
   dict(k="people", at="وهادا هو السعر المرجعي", until="الخبر التالت: الماتريكولا", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="قارن قبل ما تصيفط", at=1.5, bg="green")]),
   dict(k="icons", at="الخبر التالت: الماتريكولا", until="يعني إلى عندك طوموبيل", box=ICO, items=[
     ["car", "اللوحة الجديدة", "green"], ["car", "العادية القديمة", "gold"], ["car", "الدولية القديمة", "red"]], gap=3.0),
   dict(k="calendar", at="يعني إلى عندك طوموبيل", until="ومن جهة أخرى، الميزانية", box=R_BOX, day=31, month=12, sub="آخر أجل · اللوحة الدولية"),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Casablanca"], at="يعني إلى عندك طوموبيل", until="ومن جهة أخرى، الميزانية", box=L_BOX),
   dict(k="people", at="ومن جهة أخرى، الميزانية", until="وتذكير صغير:", box=FULL, people=["elder", "man"],
        say=[dict(who=0, text="والمغاربة ديال الخارج؟", at=2.0), dict(who=1, text="ما لقينا حتى إجراء", at=8.0, bg="gold")]),
   dict(k="map", **MED, route=["Casablanca", "Milano"], at="وتذكير صغير:", box=(160, 200, 1760, 880)),
 ]),
 dict(audio="H.wav", text=T["H"], chapter="07 · سؤال وجواب", src=S_QA, items=[
   dict(k="chapter", num="07", title="سؤال وجواب", at=0.1, until="السؤال الأول: أنا ريدر"),
   dict(k="people", at="السؤال الأول: أنا ريدر", until="السؤال التاني: كنكري", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="غادي نولي بكونطرا؟", at=1.0), dict(who=1, text="ماشي أوتوماتيكيا", at=6.0, bg="gold")]),
   dict(k="people", at="السؤال التاني: كنكري", until="السؤال التالت: الزيادة", box=R_BOX, people=["woman"],
        say=[dict(who=0, text="كنكري الدار فسيت", at=1.0)]),
   dict(k="map", view="south", pins=["Napoli", "Bari"], labels=False, at="السؤال التاني: كنكري", until="السؤال التالت: الزيادة", box=L_BOX),
   dict(k="people", at="السؤال التالت: الزيادة", until="السؤال الرابع: المعلم", box=R_BOX, people=["man"],
        say=[dict(who=0, text="غادي تزاد فالخلاص؟", at=1.0)]),
   dict(k="vs", at="السؤال التالت: الزيادة", until="السؤال الرابع: المعلم", box=L_BOX,
        right=dict(title="الخلاص", value="لا", sub="", icon="x", color="red"),
        left=dict(title="التي إف إر", value="نعم", sub="", icon="pig-money", color="green"), gap=4.0),
   dict(k="people", at="السؤال الرابع: المعلم", until="السؤال الخامس: واش", box=FULL, people=["worker", "clerk"],
        say=[dict(who=0, text="الطرد فالواتساب؟", at=1.0), dict(who=1, text="سير بسرعة للسانديكا", at=8.0, bg="red")]),
   dict(k="people", at="السؤال الخامس: واش", until="السؤال السادس: سمعت", box=R_BOX, people=["hijab", "clerk"],
        say=[dict(who=0, text="نطلب البونس؟", at=1.0), dict(who=1, text="لا، بالإيزي", at=4.0, bg="green")]),
   dict(k="icons", at="السؤال الخامس: واش", until="السؤال السادس: سمعت", box=L_BOX, items=[
     ["bolt", "الضو", "gold"], ["flame", "الغاز", "blue"]], gap=2.0),
   dict(k="people", at="السؤال السادس: سمعت", until="السؤال السابع: عندي", box=FULL, people=["elder", "man"],
        say=[dict(who=0, text="التقاعد فـ64؟", at=1.0), dict(who=1, text="ما تبدلات حتى حاجة", at=6.0, bg="gold")]),
   dict(k="people", at="السؤال السابع: عندي", until="السؤال التامن: واش", box=FULL, people=["elder", "clerk"],
        say=[dict(who=0, text="الكارطا ديال 300؟", at=1.0), dict(who=1, text="باقي غير مشروع", at=5.0, bg="red")]),
   dict(k="map", **MED, route=["Bologna", "Casablanca"], at="السؤال التامن: واش", until="السؤال التاسع: المازوط", box=L_BOX),
   dict(k="people", at="السؤال التامن: واش", until="السؤال التاسع: المازوط", box=R_BOX, people=["man"],
        say=[dict(who=0, text="نشري دار؟", at=1.0), dict(who=0, text="غير المشاريع", at=4.0, bg="red")]),
   dict(k="big", text="23/11", at="السؤال التاسع: المازوط", until="السؤال العاشر: لقيت", y=430, size=240, color=GOLD, sub="آخر نهار ديال الخصم"),
   dict(k="calendar", at="السؤال العاشر: لقيت", until="السؤال الحادي عشر", box=R_BOX, day=16, month=12, sub="أول خلاص بالكارطا"),
   dict(k="people", at="السؤال العاشر: لقيت", until="السؤال الحادي عشر", box=L_BOX, people=["woman"],
        say=[dict(who=0, text="لقيت راسي فالليستة", at=1.0, bg="green")]),
   dict(k="steps", at="السؤال الحادي عشر", until="وإلى عندك سؤال آخر", box=WIDE, steps=[
     ["المعلم كيدير الطلب", "1"], ["الملء المسبق", "7/12"], ["الكليك داي", "16/2"]], gap=4.0, check_after=0.6),
   dict(k="text", text="الطلب ما كيتشراش", at="والطلب ما كيتشراش", until="وإلى عندك سؤال آخر", y=880, size=60, color=RED),
   dict(k="people", at="وإلى عندك سؤال آخر", box=FULL, people=["girl", "man"],
        say=[dict(who=0, text="كتب السؤال ديالك", at=0.8, bg="green")]),
 ]),
 dict(audio="I.wav", text=T["I"], chapter="08 · الخلاصة والتواريخ", src=S_HOME, items=[
   dict(k="head", text="الخلاصة", at=0.2, until="واحد: القانون الجديد"),
   dict(k="rows", at="واحد: القانون الجديد", until="وتمنية: إلى كنتي ريدر", y=300, gap=82, size=42, rows=[
     ("الريدر والأبليكاسيونات", "2/12", "واحد: القانون الجديد"),
     ("الزيادة ديال التي إف إر", "5,2%", "جوج: التي إف إر"),
     ("الطرد فالواتساب", "!", "تلاتة: الطرد"),
     ("الميزانية: باقي مشروع", "31/12", "ربعة: الميزانية"),
     ("البونس ديال الضو", "ISEE", "خمسة: البونس"),
     ("الخصم على المازوط", "23/11", "ستة: المازوط"),
     ("من المغرب", "2%", "سبعة: من المغرب"),
   ]),
   dict(k="people", at="وتمنية: إلى كنتي ريدر", until="ودابا التواريخ ديال الأيام", box=FULL, people=["worker"],
        say=[dict(who=0, text="كلشي بالكتابة", at=1.0, bg="green")]),
   dict(k="steps", at="ودابا التواريخ ديال الأيام", until="ونهار واحد وتلاتين دجنبر", box=WIDE, steps=[
     ["المازوط", "23/11"], ["الضريبة + التسوية", "30/11"], ["البانسيون", "1/12"], ["المنصات", "2/12"], ["الديكري فلوسي", "7/12"], ["الأسينيو + الإيمو + الكارطا", "16/12"]], gap=3.0, check_after=0.6),
   dict(k="calendar", at="ونهار واحد وتلاتين دجنبر", until="وإلى فاتك شي فيديو", box=WIDE, day=31, month=12, sub="اللوحات فالمغرب · الميزانية"),
   dict(k="icons", at="وإلى فاتك شي فيديو", until="ونعاودو نقولو", box=ICO, items=[
     ["heart", "الجنسية بالزواج", "gold"], ["car", "البيرمي من الصفر", "blue"], ["briefcase", "النازبي", "green"], ["id", "البيرميسو", "gold"]], gap=2.5),
   dict(k="people", at="ونعاودو نقولو", until="وإلى عجبك هاد الفيديو", box=FULL, people=["clerk", "woman"],
        say=[dict(who=0, text="سول السانديكا ولا الكاف", at=1.0, bg="green")]),
   dict(k="cta", at="وإلى عجبك هاد الفيديو", until="وكتب لينا فالكومونتير", text="ابوني فالقناة", sub="وفعل الجرس"),
   dict(k="people", at="وكتب لينا فالكومونتير", box=FULL, people=["girl", "worker", "hijab"],
        say=[dict(who=1, text="أنا خدام بأبليكاسيون", at=0.8), dict(who=2, text="صيفطو لشي واحد", at=6.0, bg="green")]),
 ]),
]

THUMB = dict(
  title=[("الريدر والأبليكاسيونات: قانون جديد", (236, 196, 96)), "التي إف إر طلع والطرد فالواتساب", "المازوط والبونس ديال الضو"],
  num="2/12", numsub="كيبدا القانون الجديد",
  bottom="مغاربة إيطاليا · خبار مفيدة بالدارجة",
)
