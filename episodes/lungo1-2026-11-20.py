import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-20.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo1-2026-11-20-final")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = {k: v.replace("گ", "ك") for k, v in JOB["blocks"].items()}
# C: ultima frase troncata dal TTS, tagliata dall'audio (169,45 s)
T["C"] = T["C"].replace(" يعني الأسينيو اللي كتاخد ما كيطلعش ليك الإيزي فهاد الحساب.", "")

S_HOME = "مغاربة إيطاليا · خبار مفيدة بالدارجة"
S_ROT = "InformazioneFiscale 26/10 · Edotto 16/11 (L. 199/2025, DL 38/2026)"
S_SEND = "INPS messaggio 3801 del 19/11/2026 · Edotto 20/11 · Money.it 20/11"
S_NIDO = "INPS circ. 29/2026 · QuiFinanza · BusinessOnline · INPS msg 205/2026 · Edotto"
S_APE = "INPS msg 3694 del 12/11/2026 · LentePubblica 19/11 · Fiscal Focus · InformazioneFiscale"
S_FLASH = "Sky TG24 · Tgcom24 · SmartWorld (accise) · QuiFinanza · Trend Online · Min. Lavoro"
S_CASO = "INPS circ. 29/2026 · QuiFinanza · BusinessOnline · Edotto (msg 205/2026)"
S_MAR = "Douane ADII circ. 6659/311 · Bladi.net · Ecoactu · Office des Changes (art. 155-160)"
S_QA = "Fonti dei capitoli 01-06"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850); FULL = (160, 300, 1760, 860)
WIDE = (260, 220, 1660, 830); ICO = (160, 330, 1760, 860); BAR = (160, 300, 1760, 840)
MED = dict(view="med", hl=["ITA", "MAR"], labels=False)

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="00 · أخبار اليوم والتسوية", src=S_HOME, items=[
   dict(k="head", text="أخبار اليوم", at=0.2, until="شنو كاين اليوم؟", sub="الجمعة 20 نونبر 2026"),
   dict(k="people", at=0.6, until="شنو كاين اليوم؟", box=FULL, people=["hijab", "man", "elder"],
        say=[dict(who=1, text="شنو الجديد هاد السيمانة؟", at=0.8), dict(who=2, text="خبار بالأرقام", at=4.0, bg="green")]),
   dict(k="rows", at="شنو كاين اليوم؟", until="ومن بعد، أخبار سريعة", y=280, gap=125, size=50, rows=[
     ("التسوية ديال الكارطيلات", "30/11", "الخبر الأول على"),
     ("الإينبس فالتيليفون", "2027", "الخبر التاني على"),
     ("البونس ديال الكريش", "3.000 €", "الخبر التالت على"),
     ("آبي سوشيال", "30/11", "الخبر الرابع للناس"),
   ]),
   dict(k="icons", at="ومن بعد، أخبار سريعة", until="ومن بعد، مثال عملي", box=ICO, items=[
     ["gas-station", "المازوط", "gold"], ["coin-euro", "البانسيون ديال دجنبر", "green"], ["briefcase", "الديكري فلوسي", "blue"]], gap=2.5),
   dict(k="map", **MED, route=["Genova", "Tanger", "ship"], at="ومن بعد، مثال عملي", until="قبل ما نبداو، جوج", box=(160, 200, 1760, 880)),
   dict(k="icons", at="قبل ما نبداو، جوج", until="يالاه نبداو بالخبر", box=ICO, items=[
     ["file-certificate", "جوج مصادر على الأقل", "green"], ["alert-triangle", "ماشي استشارة", "gold"], ["users", "سول الباطروناطو", "blue"]], gap=2.5),
   dict(k="chapter", num="01", title="التسوية: أجل 30 نونبر", at="يالاه نبداو بالخبر", until="شكون كيهمو؟ كيهم"),
   dict(k="people", at="شكون كيهمو؟ كيهم", until="نهار تلاتين نونبر، اللي هو", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="عندي كارطيلا", at=0.6, bg="gold")]),
   dict(k="vs", at="كاين جوج ديال التسويات", until="نهار تلاتين نونبر، اللي هو", box=L_BOX,
        right=dict(title="القديمة", value="4", sub="الرابعة", icon="receipt-tax", color="grey"),
        left=dict(title="الجديدة", value="5", sub="الخامسة", icon="receipt-tax", color="gold"), gap=3.0),
   dict(k="calendar", at="نهار تلاتين نونبر، اللي هو", until="دابا الفرق المهم", box=R_BOX, day=30, month=11, sub="التنين · 3 أقساط"),
   dict(k="steps", at="كيطيحو تلاتة ديال الأقساط", until="دابا الفرق المهم", box=L_BOX, steps=[
     ["الجديدة: القسط", "3"], ["القديمة: القسط", "14"], ["اللي رجعو: القسط", "6"]], gap=3.0, check_after=0.6),
   dict(k="vs", at="دابا الفرق المهم", until="مثال باش يوضح: إلى", box=WIDE,
        right=dict(title="القديمة", value="7/12", sub="5 أيام ديال التسامح", icon="calendar", color="green"),
        left=dict(title="الجديدة", value="30/11", sub="بلا تسامح", icon="alert-triangle", color="red"), gap=5.0),
   dict(k="map", view="italy", pins=["Milano", "Torino", "Roma", "Napoli"], labels=False, at="مثال باش يوضح: إلى", box=L_BOX),
   dict(k="people", at="مثال باش يوضح: إلى", box=R_BOX, people=["man", "office"],
        say=[dict(who=0, text="عندي حتى 7 دجنبر؟", at=1.0), dict(who=1, text="غير فالقديمة", at=7.0, bg="red")]),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="02 · الإينبس فالتيليفون", src=S_ROT, items=[
   dict(k="head", text="التسوية القديمة: إلى ما خلصتيش؟", at=0.2, until="فالتسوية الجديدة، كتطيح"),
   dict(k="icons", at=0.6, until="فالتسوية الجديدة، كتطيح", box=ICO, items=[
     ["x", "قسط ما تخلصش", "red"], ["alert-triangle", "التسوية كتطيح", "red"], ["calendar", "تقسيط عادي ممكن", "green"]], gap=3.0),
   dict(k="people", at="فالتسوية الجديدة، كتطيح", until="النصيحة: شوف الورقة", box=R_BOX, people=["clerk"],
        say=[dict(who=0, text="جوج أقساط = نهاية التسوية", at=1.0, bg="red")]),
   dict(k="bars", at="فالتسوية الجديدة، كتطيح", until="النصيحة: شوف الورقة", box=L_BOX, bars=[
     ["القديمة", 1, "1", "gold"], ["الجديدة", 2, "2", "red"]], gap=2.0),
   dict(k="icons", at="النصيحة: شوف الورقة", until="دابا الخبر التاني، على", box=ICO, items=[
     ["file-text", "الورقة ديال التسوية", "gold"], ["phone", "السيت بالسبيد", "blue"], ["users", "الكاف ولا الكومبتابل", "green"], ["clock", "خلص بكري", "green"]], gap=2.5),
   dict(k="chapter", num="02", title="الإينبس فالتيليفون", at="دابا الخبر التاني، على", until="شكون كيهمو هادشي فالمرحلة"),
   dict(k="calendar", at="شكون كيهمو هادشي فالمرحلة", until="وشنو هي الوراق اللي غادي", box=R_BOX, day=1, month=1, sub="يناير 2027 · بالتدريج"),
   dict(k="people", at="شكون كيهمو هادشي فالمرحلة", until="وشنو هي الوراق اللي غادي", box=L_BOX, people=["elder", "woman"],
        say=[dict(who=0, text="عندي البانسيون", at=0.8, bg="gold")]),
   dict(k="icons", at="وشنو هي الوراق اللي غادي", until="كيفاش غادي توصلك؟", box=ICO, items=[
     ["mail", "الإشعار الأول", "gold"], ["clock", "التذكير", "gold"], ["calculator", "الحساب", "blue"], ["receipt", "التقسيط", "green"]], gap=2.0),
   dict(k="steps", at="كيفاش غادي توصلك؟", until="وإلى ما عندكش السبيد", box=WIDE, steps=[
     ["التطبيق إيو", "1"], ["البريد المصادق PEC", "2"], ["SEND · notifichedigitali.it", "3"]], gap=4.0, check_after=0.6),
   dict(k="map", view="italy", pins=["Bologna", "Roma", "Bari"], labels=False, at="وإلى ما عندكش السبيد", until="علاش هاد الخبر مهم", box=L_BOX),
   dict(k="people", at="وإلى ما عندكش السبيد", until="علاش هاد الخبر مهم", box=R_BOX, people=["elder", "girl"],
        say=[dict(who=0, text="ما عنديش السبيد", at=0.8), dict(who=1, text="رسالة مضمونة", at=4.5, bg="green")]),
   dict(k="vs", at="علاش هاد الخبر مهم", until="النصيحة العملية: إلى", box=WIDE,
        right=dict(title="قريتي الورقة", value="OK", sub="التقسيط ولا الاعتراض", icon="check", color="green"),
        left=dict(title="ما قريتيهاش", value="!", sub="الأجل يقدر يفوتك", icon="alert-triangle", color="red"), gap=4.0),
   dict(k="people", at="النصيحة العملية: إلى", box=FULL, people=["man", "elder"],
        say=[dict(who=0, text="نحلو التطبيق إيو", at=1.5, bg="green"), dict(who=1, text="باش نشوف الرسائل", at=6.0)]),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="03 · البونس ديال الكريش", src=S_NIDO, items=[
   dict(k="chapter", num="03", title="البونس ديال الكريش", at=0.1, until="هاد البونس كيعطيه الإينبس"),
   dict(k="people", at="هاد البونس كيعطيه الإينبس", until="شحال كيعطي؟ كيتعلق", box=FULL, people=["hijab", "child"],
        say=[dict(who=0, text="الكريش غالية", at=0.6)]),
   dict(k="bars", at="شحال كيعطي؟ كيتعلق", until="والفلوس كتتقسم على", box=BAR, bars=[
     ["الإيزي حتى 25 ألف", 3000, "3.000 €", "green"], ["من 25 حتى 40 ألف", 2500, "2.500 €", "gold"], ["المزدادين من 2024", 3600, "3.600 €", "blue"]], gap=4.5),
   dict(k="head", text="البونس فالعام", at="شحال كيعطي؟ كيتعلق", until="والفلوس كتتقسم على", y=180, size=60),
   dict(k="vs", at="والفلوس كتتقسم على", until="ولكن رد بالك: البونس", box=WIDE,
        right=dict(title="الإيزي حتى 25 ألف", value="272,72 €", sub="فالشهر · 11 شهر", icon="calendar", color="green"),
        left=dict(title="من 25 حتى 40 ألف", value="227,27 €", sub="فالشهر · 11 شهر", icon="calendar", color="gold"), gap=4.0),
   dict(k="people", at="ولكن رد بالك: البونس", until="شنو الجديد؟ القاعدة", box=R_BOX, people=["clerk"],
        say=[dict(who=0, text="بلا وصل، ما كاين فلوس", at=1.0, bg="red")]),
   dict(k="icons", at="ولكن رد بالك: البونس", until="شنو الجديد؟ القاعدة", box=L_BOX, items=[
     ["receipt", "الوصل", "green"], ["credit-card", "خلاص كيبان", "green"]], gap=2.0),
   dict(k="steps", at="شنو الجديد؟ القاعدة", until="ودابا حاجة مهمة بزاف للمغاربة", box=WIDE, steps=[
     ["طلب واحد", "1"], ["صالح حتى 3 سنين", "3"], ["كل عام: الشهور + الوصولات", "+"]], gap=3.0, check_after=0.6),
   dict(k="map", view="north", pins=["Torino", "Brescia"], labels=False, at="ودابا حاجة مهمة بزاف للمغاربة", until="هاد البيرميسو كيعطيوه", box=L_BOX),
   dict(k="people", at="ودابا حاجة مهمة بزاف للمغاربة", until="هاد البيرميسو كيعطيوه", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="البيرميسو ديال انتظار الخدمة", at=2.0, bg="gold")]),
   dict(k="calendar", at="هاد البيرميسو كيعطيوه", until="وفيناير ديال هاد العام", box=R_BOX, day=1, month="عام", sub="على الأقل · فالتجديد"),
   dict(k="icons", at="هاد البيرميسو كيعطيوه", until="وفيناير ديال هاد العام", box=L_BOX, items=[
     ["id", "انتظار الخدمة", "gold"], ["briefcase", "خدمة جديدة", "green"]], gap=2.5),
   dict(k="vs", at="وفيناير ديال هاد العام", until="ولكن كاين تفصيل", box=WIDE,
        right=dict(title="قبل", value="لا", sub="الإينبس كان كيرفض", icon="x", color="red"),
        left=dict(title="دابا", value="نعم", sub="msg INPS 205/2026", icon="check", color="green"), gap=4.0),
   dict(k="warn", text="كيتخلص مع إمكانية الاسترجاع: تبع الأخبار", at="ولكن كاين تفصيل", until="شكون كيهمو هادشي؟ مثلا", y=820),
   dict(k="head", text="محكمة النقض باقي ما حكماتش", at="ولكن كاين تفصيل", until="شكون كيهمو هادشي؟ مثلا", sub="الحكم ولا قانون جديد"),
   dict(k="people", at="شكون كيهمو هادشي؟ مثلا", until="وكيفاش كتطلب البونس", box=FULL, people=["man", "woman", "child"],
        say=[dict(who=0, text="تحبسات ليا الخدمة", at=0.8), dict(who=1, text="سير للباطروناطو", at=8.0, bg="green")]),
   dict(k="steps", at="وكيفاش كتطلب البونس", box=WIDE, steps=[
     ["السيت ديال الإينبس · SPID", "1"], ["الكاف ولا الباطروناطو", "2"], ["الإيزي ديال الولاد", "3"]], gap=3.0, check_after=0.6),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="04 · آبي سوشيال: أجل 30/11", src=S_APE, items=[
   dict(k="chapter", num="04", title="آبي سوشيال: أجل 30 نونبر", at=0.1, until="كيخليك تخرج"),
   dict(k="people", at="كيخليك تخرج", until="آخر أجل باش تطلب", box=R_BOX, people=["elder"],
        say=[dict(who=0, text="نخرج بكري؟", at=1.0)]),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="كيخليك تخرج", until="آخر أجل باش تطلب", box=L_BOX),
   dict(k="calendar", at="آخر أجل باش تطلب", until="شنو هي الشروط؟", box=R_BOX, day=30, month=11, sub="آخر فرصة هاد العام"),
   dict(k="steps", at="آخر أجل باش تطلب", until="شنو هي الشروط؟", box=L_BOX, steps=[
     ["مارس", "31/3"], ["يوليوز", "15/7"], ["نونبر", "30/11"]], gap=2.0, check_after=0.6),
   dict(k="big", text="63", at="شنو هي الشروط؟ أولا", until="تانيا، خاصك تكون", y=430, size=240, color=GOLD, sub="عام وخمسة شهور"),
   dict(k="icons", at="تانيا، خاصك تكون", until="وشحال ديال السنين", box=ICO, items=[
     ["briefcase", "سالا النازبي", "gold"], ["heart", "كتعاون فرد من العائلة", "gold"], ["stethoscope", "إعاقة 74 فالمية ولا كتر", "gold"], ["tool", "خدمة صعيبة", "gold"]], gap=3.0),
   dict(k="bars", at="وشحال ديال السنين", until="وشحال كتاخد؟", box=BAR, bars=[
     ["أغلب الحالات", 30, "30", "gold"], ["الخدمات الصعيبة", 36, "36", "red"]], gap=3.0),
   dict(k="head", text="سنين ديال الكوتيزاسيون", at="وشحال ديال السنين", until="وشحال كتاخد؟", y=180, size=60, sub="العيالات: عام أقل على كل دري، حتى 2"),
   dict(k="big", text="1.500 €", at="وشحال كتاخد؟", until="دابا الحاجة المهمة بزاف", y=450, size=230, color=GREEN, sub="أقصى حد فالشهر · بلا الشهر 13"),
   dict(k="people", at="دابا الحاجة المهمة بزاف", until="علاش هادشي كيهم المغاربة", box=FULL, people=["clerk", "man"],
        say=[dict(who=0, text="بديتي الخدمة من بعد 1995", at=2.0, bg="red")]),
   dict(k="vs", at="علاش هادشي كيهم المغاربة", until="مثلا واحد جا فعام", box=WIDE,
        right=dict(title="بدا قبل 1996", value="OK", sub="يقدر يطلب", icon="check", color="green"),
        left=dict(title="بدا من 1996", value="لا", sub="كيترفض دابا", icon="x", color="red"), gap=3.0),
   dict(k="map", **MED, route=["Casablanca", "Milano"], at="مثلا واحد جا فعام", until="وكاين خبر مزيان للخدامات", box=(160, 200, 1760, 880)),
   dict(k="people", at="وكاين خبر مزيان للخدامات", until="والعام الجاي؟ الاستمرار", box=FULL, people=["hijab", "elder"],
        say=[dict(who=0, text="المعلم مات", at=2.0), dict(who=0, text="بحال الطرد", at=7.0, bg="green")]),
   dict(k="warn", text="2027: باقي مشروع، ماشي قانون", at="والعام الجاي؟ الاستمرار", until="كيفاش كتطلب؟ أونلاين", y=640),
   dict(k="steps", at="كيفاش كتطلب؟ أونلاين", until="مثال باش يوضح: إبراهيم", box=WIDE, steps=[
     ["الإينبس · SPID · CIE", "1"], ["الباطروناطو", "2"], ["قبل 30/11", "!"]], gap=3.0, check_after=0.6),
   dict(k="map", view="north", pins=["Brescia"], labels=False, at="مثال باش يوضح: إبراهيم", box=L_BOX),
   dict(k="steps", at="مثال باش يوضح: إبراهيم", box=R_BOX, steps=[
     ["تزاد", "5/1963"], ["بدا الخدمة", "1990"], ["العمر المطلوب", "10/2026"], ["الطلب قبل", "30/11"]], gap=4.0, check_after=0.6),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="05 · أخبار سريعة", src=S_FLASH, items=[
   dict(k="chapter", num="05", title="أخبار سريعة", at=0.1, until="الخبر الأول على المازوط"),
   dict(k="big", text="4,88", at="الخبر الأول على المازوط", until="شحال كتربح؟", y=420, size=260, color=GOLD, sub="سنتيم فاللتر · غير المازوط"),
   dict(k="calendar", at="شحال كتربح؟", until="والنصيحة: الثمن ماشي", box=R_BOX, day=23, month=11, sub="آخر نهار ديال الخصم"),
   dict(k="vs", at="شحال كتربح؟", until="والنصيحة: الثمن ماشي", box=L_BOX,
        right=dict(title="50 لتر", value="2,44 €", sub="الربح", icon="gas-station", color="green"),
        left=dict(title="البنزين", value="0", sub="ما فيه خصم", icon="gas-station", color="grey"), gap=3.0),
   dict(k="map", view="italy", pins=["Milano", "Roma", "Palermo"], labels=False, at="والنصيحة: الثمن ماشي", until="الخبر التاني للمتقاعدين", box=L_BOX),
   dict(k="people", at="والنصيحة: الثمن ماشي", until="الخبر التاني للمتقاعدين", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="نقارن الأثمنة", at=1.0, bg="green")]),
   dict(k="calendar", at="الخبر التاني للمتقاعدين", until="هاد المبلغ كيجي بوحدو", box=R_BOX, day=1, month=12, sub="البانسيون والشهرية التلطاش"),
   dict(k="people", at="الخبر التاني للمتقاعدين", until="هاد المبلغ كيجي بوحدو", box=L_BOX, people=["elder"],
        say=[dict(who=0, text="حتى 154,94 أورو", at=4.0, bg="gold")]),
   dict(k="icons", at="هاد المبلغ كيجي بوحدو", until="إلى عندك الواليدين متقاعدين", box=ICO, items=[
     ["check", "بلا طلب", "green"], ["x", "التعويض الاجتماعي: لا", "red"], ["x", "الإعاقة المدنية: لا", "red"]], gap=3.0),
   dict(k="people", at="إلى عندك الواليدين متقاعدين", until="وللخدامين فالقطاع الخاص", box=FULL, people=["man", "elder"],
        say=[dict(who=0, text="نشوفو الورقة ديال دجنبر", at=1.0, bg="green")]),
   dict(k="vs", at="وللخدامين فالقطاع الخاص", until="ودابا التذكير", box=WIDE,
        right=dict(title="القطاع الخاص", value="CCNL", sub="مع خلصة دجنبر", icon="briefcase", color="gold"),
        left=dict(title="الدولة", value="15/12", sub="الشهرية 13", icon="building-bank", color="green"), gap=4.0),
   dict(k="calendar", at="ودابا التذكير", until="والتواريخ الأخرى ديال", box=R_BOX, day=7, month=12, sub="الملء المسبق · حتى 20:00"),
   dict(k="people", at="ودابا التذكير", until="والتواريخ الأخرى ديال", box=L_BOX, people=["office"],
        say=[dict(who=0, text="المعلم هو اللي كيطلب", at=6.0, bg="gold")]),
   dict(k="map", **MED, route=["Casablanca", "Bergamo"], at="إلى عندك واحد فالعائلة", until="ورد بالك مزيان", box=(160, 200, 1760, 880)),
   dict(k="steps", at="والتواريخ الأخرى ديال", until="إلى عندك واحد فالعائلة", box=WIDE, steps=[
     ["الفلاحة الموسمية", "12/1"], ["السياحة الموسمية", "9/2"], ["ماشي موسمية", "16/2"], ["الخدمة فالديور", "18/2"]], gap=2.5, check_after=0.6),
   dict(k="people", at="ورد بالك مزيان", until="وعندنا فيديو كامل", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="عطيني الفلوس ونجيب ليك عقد", at=1.0, bg="red"), dict(who=1, text="هادي نصبة!", at=5.0, bg="red")]),
   dict(k="text", text="الطلب ما كيتشراش", at="وعندنا فيديو كامل", y=520, size=80, color=GOLD),
 ]),
 dict(audio="F.wav", text=T["F"], chapter="06 · مثال: فاطمة والكريش", src=S_CASO, items=[
   dict(k="chapter", num="06", title="مثال: فاطمة والكريش", at=0.1, until="فاطمة ساكنة فبولونيا"),
   dict(k="map", view="north", pins=["Bologna"], labels=False, at="فاطمة ساكنة فبولونيا", until="الخطوة الأولى: الإيزي", box=L_BOX),
   dict(k="people", at="فاطمة ساكنة فبولونيا", until="الخطوة الأولى: الإيزي", box=R_BOX, people=["hijab", "man", "child"],
        say=[dict(who=0, text="شحال يرجع الإينبس؟", at=7.0)]),
   dict(k="vs", at="الخطوة الأولى: الإيزي", until="الخطوة التانية: الحساب", box=WIDE,
        right=dict(title="الإيزي ديالهم", value="18.000 €", sub="الإيزي ديال الولاد", icon="file-text", color="gold"),
        left=dict(title="البونس", value="3.000 €", sub="فالعام", icon="coin-euro", color="green"), gap=5.0),
   dict(k="bars", at="الخطوة التانية: الحساب", until="وفالعام كامل، الإينبس", box=BAR, bars=[
     ["الكريش فالشهر", 350, "350 €", "grey"], ["الإينبس", 272.73, "272,72 €", "green"], ["من الجيب", 77.27, "77 €", "gold"]], gap=3.0),
   dict(k="vs", at="وفالعام كامل، الإينبس", until="الخطوة التالتة: الطلب", box=WIDE,
        right=dict(title="الإينبس فالعام", value="3.000 €", sub="11 شهر", icon="building-bank", color="green"),
        left=dict(title="العائلة فالعام", value="850 €", sub="بلاصة 3.850", icon="home", color="gold"), gap=3.0),
   dict(k="steps", at="الخطوة التالتة: الطلب", until="الخطوة الرابعة: الوصولات", box=WIDE, steps=[
     ["SPID ولا الباطروناطو", "1"], ["البونس ديال الكريش", "2"], ["الكريش + الشهور", "3"]], gap=3.0, check_after=0.6),
   dict(k="icons", at="الخطوة الرابعة: الوصولات", until="دابا مثال تاني", box=ICO, items=[
     ["building-bank", "البنكة", "green"], ["credit-card", "الكارطا", "green"], ["cash", "كاش بلا وصل: لا", "red"], ["receipt", "الوصل فالسيت", "gold"]], gap=2.5),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="دابا مثال تاني", until="ومثال تالت", box=L_BOX),
   dict(k="bars", at="دابا مثال تاني", until="ومثال تالت", box=R_BOX, bars=[
     ["السقف فالشهر", 227.27, "227 €", "grey"], ["الكريش", 200, "200 €", "gold"], ["كيرجع", 200, "200 €", "green"]], gap=3.0),
   dict(k="map", view="north", pins=["Brescia"], labels=False, at="ومثال تالت", until="شنو الأخطاء اللي خاص", box=L_BOX),
   dict(k="people", at="ومثال تالت", until="شنو الأخطاء اللي خاص", box=R_BOX, people=["woman", "child"],
        say=[dict(who=0, text="انتظار الخدمة", at=4.0, bg="gold"), dict(who=0, text="الطلب كيتقبل", at=12.0, bg="green")]),
   dict(k="people", at="شنو الأخطاء اللي خاص", until="وإلى عندك دري عندو مرض", box=R_BOX, people=["clerk"],
        say=[dict(who=0, text="رد بالك!", at=0.6, bg="red")]),
   dict(k="icons", at="شنو الأخطاء اللي خاص", until="وإلى عندك دري عندو مرض", box=L_BOX, items=[
     ["file-text", "بلا إيزي", "red"], ["cash", "كاش بلا وصل", "red"], ["clock", "الوصولات فالتأخير", "red"], ["calculator", "كتر من الثمن", "red"]], gap=4.0),
   dict(k="vs", at="وإلى عندك دري عندو مرض", box=WIDE,
        right=dict(title="الكريش", value="1", sub="الثمن ديال الشهر", icon="school", color="gold"),
        left=dict(title="العون فالدار", value="2", sub="مرض مزمن خطير", icon="home", color="blue"), gap=3.0),
 ]),
 dict(audio="G.wav", text=T["G"], chapter="07 · من المغرب", src=S_MAR, items=[
   dict(k="chapter", num="07", title="من المغرب", at=0.1, until="الخبر الأول على الطوموبيل"),
   dict(k="map", **MED, route=["Genova", "Tanger", "ship"], at="الخبر الأول على الطوموبيل", until="وكاينة حالة خاصة", box=(160, 200, 1760, 880)),
   dict(k="big", text="180", at="ولكن غير مية وتمانين يوم", until="وكاينة حالة خاصة", y=230, x=1660, size=200, color=GOLD, sub="يوم فالعام"),
   dict(k="calendar", at="وكاينة حالة خاصة", until="وإلى فاتتك المدة؟", box=R_BOX, day=1, month=12, sub="كتسالي من هنا؟ زيد ستة شهور"),
   dict(k="people", at="وكاينة حالة خاصة", until="وإلى فاتتك المدة؟", box=L_BOX, people=["man"],
        say=[dict(who=0, text="نازل فدجنبر", at=1.0, bg="gold")]),
   dict(k="bars", at="وإلى فاتتك المدة؟", until="وما تنساش: خلي معاك", box=BAR, bars=[
     ["أقل خطية", 1000, "1.000 DH", "gold"], ["أكبر خطية", 10000, "10.000 DH", "red"]], gap=3.0),
   dict(k="icons", at="وما تنساش: خلي معاك", until="وشكون يقدر يسوق", box=ICO, items=[
     ["car", "وراق الطوموبيل باسمك", "green"], ["id", "البيرميسو ديال إيطاليا", "green"], ["file-text", "ورقة الديوانة", "green"]], gap=2.0),
   dict(k="vs", at="وشكون يقدر يسوق", until="وإلى عندك شي شك فالحالة", box=WIDE,
        right=dict(title="ساكن برا", value="يسوق", sub="بالوراق", icon="user", color="green"),
        left=dict(title="ساكن فالمغرب", value="معاك", sub="غير وانت حاضر", icon="users", color="red"), gap=4.0),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Tanger", "Casablanca", "Laayoune", "Dakhla"], labels=False,
        at="وإلى عندك شي شك فالحالة", until="الخبر التاني على الناس", box=L_BOX),
   dict(k="people", at="وإلى عندك شي شك فالحالة", until="الخبر التاني على الناس", box=R_BOX, people=["clerk"],
        say=[dict(who=0, text="سول الديوانة", at=1.0, bg="green")]),
   dict(k="steps", at="الخبر التاني على الناس", until="ولكن هادشي كيتطلب الدليل", box=WIDE, steps=[
     ["الفلوس من إيطاليا", "€"], ["بالعملة الصعبة", "DH"], ["الدار فالمغرب", "1"], ["الرجوع ديال الفلوس", "OK"]], gap=4.0, check_after=0.6),
   dict(k="icons", at="ولكن هادشي كيتطلب الدليل", until="علاش هادشي مهم؟ مثلا", box=ICO, items=[
     ["building-bank", "وصل البنكة الإيطالية", "green"], ["receipt", "وصل البنكة المغربية", "green"], ["file-certificate", "العقد عند الموثق", "gold"]], gap=3.0),
   dict(k="map", **MED, route=["Milano", "Tanger"], at="علاش هادشي مهم؟ مثلا", until="إذن النصيحة: ما تخلصش", box=L_BOX),
   dict(k="people", at="علاش هادشي مهم؟ مثلا", until="إذن النصيحة: ما تخلصش", box=R_BOX, people=["man", "office"],
        say=[dict(who=0, text="باغي نرجع الفلوس", at=5.0), dict(who=1, text="فين الوصولات؟", at=11.0, bg="red")]),
   dict(k="vs", at="إذن النصيحة: ما تخلصش", until="وحتى إلى كنتي غادي تكري", box=WIDE,
        right=dict(title="عن طريق البنكة", value="OK", sub="بالوصولات", icon="building-bank", color="green"),
        left=dict(title="كاش فالمغرب", value="!", sub="بلا دليل", icon="cash", color="red"), gap=3.0),
   dict(k="head", text="الكرا من بعد الضرائب المغربية", at="وحتى إلى كنتي غادي تكري", sub="يقدر يتحول لبرا"),
   dict(k="icons", at="وحتى إلى كنتي غادي تكري", box=ICO, items=[
     ["home-dollar", "الكرا", "gold"], ["receipt-tax", "الضرائب فالمغرب", "blue"], ["plane", "التحويل لبرا", "green"]], gap=2.5),
 ]),
 dict(audio="H.wav", text=T["H"], chapter="08 · سؤال وجواب", src=S_QA, items=[
   dict(k="chapter", num="08", title="سؤال وجواب", at=0.1, until="السؤال الأول: عندي كارطيلا"),
   dict(k="people", at="السؤال الأول: عندي كارطيلا", until="السؤال التاني: أنا ما عنديش", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="نخلص غير شي جزء؟", at=0.8), dict(who=1, text="القسط الناقص = ما تخلصش", at=7.0, bg="red")]),
   dict(k="people", at="السؤال التاني: أنا ما عنديش", until="السؤال التالت: عندي البيرميسو", box=R_BOX, people=["girl", "elder"],
        say=[dict(who=0, text="بابا ما عندوش السبيد", at=0.8), dict(who=1, text="رسالة مضمونة", at=7.0, bg="green")]),
   dict(k="map", view="italy", pins=["Torino", "Firenze", "Bari"], labels=False, at="السؤال التاني: أنا ما عنديش", until="السؤال التالت: عندي البيرميسو", box=L_BOX),
   dict(k="people", at="السؤال التالت: عندي البيرميسو", until="السؤال الرابع: الكريش", box=R_BOX, people=["man"],
        say=[dict(who=0, text="رفضو ليا الأسينيو", at=1.0)]),
   dict(k="icons", at="سير للباطروناطو وطلب يعاودو", until="السؤال الرابع: الكريش", box=L_BOX, items=[
     ["id", "البيرميسو", "gold"], ["file-text", "الإيزي", "gold"], ["mail", "الرفض", "gold"]], gap=2.0),
   dict(k="people", at="السؤال الرابع: الكريش", until="السؤال الخامس: عندي تلاتة", box=FULL, people=["hijab", "child"],
        say=[dict(who=0, text="الكريش خاصة؟", at=0.8), dict(who=0, text="إلى كانت مرخصة: نعم", at=5.0, bg="green")]),
   dict(k="people", at="السؤال الخامس: عندي تلاتة", until="السؤال السادس: نزلت", box=R_BOX, people=["elder"],
        say=[dict(who=0, text="بديت فعام 2000", at=1.5)]),
   dict(k="vs", at="السؤال الخامس: عندي تلاتة", until="السؤال السادس: نزلت", box=L_BOX,
        right=dict(title="قبل 1996", value="OK", sub="", icon="check", color="green"),
        left=dict(title="من 1996", value="لا", sub="دابا", icon="x", color="red"), gap=12.0),
   dict(k="map", **MED, route=["Genova", "Tanger", "ship"], at="السؤال السادس: نزلت", until="السؤال السابع: شريت", box=L_BOX),
   dict(k="bars", at="السؤال السادس: نزلت", until="السؤال السابع: شريت", box=R_BOX, bars=[
     ["الصيف", 90, "90", "gold"], ["الباقي", 90, "90", "green"], ["المجموع", 180, "180", "grey"]], gap=3.0),
   dict(k="people", at="السؤال السابع: شريت", until="السؤال التامن: واش", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="خلصت جزء كاش", at=0.8), dict(who=1, text="الدليل ديال العملة الصعبة", at=6.0, bg="gold")]),
   dict(k="people", at="السؤال التامن: واش", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="والبنزين؟", at=1.0)]),
   dict(k="vs", at="السؤال التامن: واش", box=L_BOX,
        right=dict(title="المازوط", value="4,88", sub="سنتيم", icon="gas-station", color="green"),
        left=dict(title="البنزين", value="0", sub="", icon="gas-station", color="grey"), gap=4.0),
 ]),
 dict(audio="I.wav", text=T["I"], chapter="09 · الخلاصة والتواريخ", src=S_HOME, items=[
   dict(k="head", text="الخلاصة", at=0.2, until="ودابا التواريخ ديال الأيام الجاية"),
   dict(k="rows", at="واحد: الضرائب", until="ودابا التواريخ ديال الأيام الجاية", y=340, gap=92, size=44, rows=[
     ("التسوية ديال الكارطيلات", "30/11", "واحد: الضرائب"),
     ("الإينبس فالتطبيق إيو", "2027", "جوج: الإينبس"),
     ("البونس ديال الكريش", "3.000 €", "تلاتة: البونس"),
     ("آبي سوشيال", "30/11", "ربعة: آبي سوشيال"),
     ("المازوط والبانسيون", "23/11 · 1/12", "خمسة: الأخبار السريعة"),
     ("الطوموبيل فالمغرب", "180", "ستة: من المغرب"),
   ]),
   dict(k="steps", at="ودابا التواريخ ديال الأيام الجاية", until="ونعاودو نقولو", box=WIDE, steps=[
     ["المازوط", "23/11"], ["البلاك فرايدي", "27/11"], ["التسوية + آبي + الضريبة", "30/11"], ["البانسيون", "1/12"], ["الديكري فلوسي", "7/12"], ["الأسينيو + الإيمو", "16/12"]], gap=2.4, check_after=0.6),
   dict(k="people", at="ونعاودو نقولو", until="وإلى عجبك هاد الفيديو", box=FULL, people=["clerk", "woman"],
        say=[dict(who=0, text="سول الباطروناطو", at=1.0, bg="green")]),
   dict(k="cta", at="وإلى عجبك هاد الفيديو", until="وكتب لينا فالكومونتير", text="ابوني فالقناة", sub="وفعل الجرس"),
   dict(k="people", at="وكتب لينا فالكومونتير", box=FULL, people=["girl", "man", "hijab"],
        say=[dict(who=0, text="شنو الموضوع الجاي؟", at=0.8), dict(who=2, text="صيفطو لشي واحد", at=6.0, bg="green")]),
 ]),
]

THUMB = dict(
  title=[("30 نونبر: التسوية وآبي سوشيال", (236, 196, 96)), "البونس ديال الكريش حتى 3.000 أورو", "الإينبس فالتيليفون من 2027"],
  num="30/11", numsub="آخر أجل · الضرائب والتقاعد",
  bottom="مغاربة إيطاليا · خبار مفيدة بالدارجة",
)
