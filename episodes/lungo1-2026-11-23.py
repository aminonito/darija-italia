import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-23.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo1-2026-11-23-final")
BRAND = "مغاربة إيطاليا"
T = {k: v.replace("گ", "ك") for k, v in JOB["blocks"].items()}
EDITS = json.load(open(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-23-edits.json"), encoding="utf-8")) if os.path.exists(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-23-edits.json")) else {}
for k, pairs in EDITS.items():
    for a, b in pairs:
        T[k] = T[k].replace(a, b)

S_HOME = "مغاربة إيطاليا · خبار مفيدة بالدارجة"
S_GAS = "Decreto MEF 9/11/2026 · Automoto 23/11 · Alanews 22/11 · Redigo 10/11 · MIMIT via Teleborsa 23/11"
S_BF = "Codice del consumo art. 17-bis · IlFaroOnline 23/11 · Newsauto · MIMIT · Altroconsumo · Commissione UE"
S_MAN = "AGI 21/11 e 30/10 · ANSA 18/11 · Agimeg 23/11 · Businessonline 23/11 · Open 28/10 · Fiscal Focus 9/11"
S_INPS = "INPS msg 3801 del 19/11/2026 via Redigo e PensioniFacili · Centro Fiscale 18/11 · InformazioneFiscale 12/11"
S_CIT = "Camera A.C. 2124-A · Quotidiano.net 20/10 · AGI 20/10 · Quattroruote 16/11 · Sicurauto · lavoro.gov.it"
S_NN = "INPS scheda Bonus nuovi nati · INPS news 11/8/2026 · LeggiOggi 30/4 · Fanpage 11/4 · calcoli nostri"
S_MAR = "LeBrief 17/11 · La Vie Eco 17/11 · BAM via Hespress 22/11 e Maroc Diplomatique 21/11 · FNH 9/11 · Yabiladi"
S_QA = "Fonti dei capitoli 01-07 · ARERA del. 58/2026 (luce)"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850); FULL = (160, 300, 1760, 860)
WIDE = (260, 220, 1660, 830); ICO = (160, 330, 1760, 860); BAR = (160, 300, 1760, 840)
MED = dict(view="med", hl=["ITA", "MAR"], labels=False)

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="00 · أخبار السيمانة", src=S_HOME, items=[
   dict(k="head", text="نشرة السيمانة", at=0.2, until="شنو كاين فهاد النشرة؟", sub="الاثنين 23 نونبر 2026"),
   dict(k="people", at=0.6, until="شنو كاين فهاد النشرة؟", box=FULL, people=["man", "hijab", "elder"],
        say=[dict(who=0, text="شنو الجديد هاد السيمانة؟", at=0.8), dict(who=2, text="خبار بالأرقام", at=4.0, bg="green")]),
   dict(k="rows", at="شنو كاين فهاد النشرة؟", until="ومن بعد، مثال عملي", y=280, gap=118, size=48, rows=[
     ("المازوط", "23/11", "عندنا المازوط"),
     ("البلاك فرايداي", "27/11", "عندنا البلاك فرايداي"),
     ("الميزانية ديال 2027", "?", "عندنا الميزانية"),
     ("الإينبس والبانسيون", "1/12", "عندنا الإينبس"),
     ("الجنسية والكود", "?", "عندنا مشروع الجنسية"),
   ]),
   dict(k="map", **MED, route=["Milano", "Casablanca"], at="ومن بعد، مثال عملي", until="قبل ما نبداو، جوج", box=(160, 200, 1760, 880)),
   dict(k="icons", at="قبل ما نبداو، جوج", until="يالاه نبداو بالخبر", box=ICO, items=[
     ["file-certificate", "جوج مصادر", "green"], ["alert-triangle", "ماشي استشارة", "gold"], ["users", "سول الباطرونا", "blue"]], gap=2.5),
   dict(k="chapter", num="01", title="المازوط: الخصم كيسالي", at="يالاه نبداو بالخبر", until="الخصم هو ربعة سنتيم"),
   dict(k="big", text="4,88", sub="سانتيم فاللتر", at="الخصم هو ربعة سنتيم", until="ولكن هاد الخصم كان محدود"),
   dict(k="calendar", at="ولكن هاد الخصم كان محدود", until="جمعية ديال المستهلكين", box=R_BOX, day=23, month=11, sub="آخر نهار"),
   dict(k="people", at="وحتى لدابا، ما كاين", until="إذن من غدا", box=L_BOX, people=["worker", "clerk"],
        say=[dict(who=0, text="واش غادي يتمد؟", at=0.6), dict(who=1, text="حتى لدابا لا", at=4.0, bg="gold")]),
   dict(k="text", text="جمعية المستهلكين: طلب، ماشي قرار", at="جمعية ديال المستهلكين", until="إذن من غدا", y=880, size=44),
   dict(k="vs", at="إذن من غدا", until="شحال كيعني هادشي فالجيب؟", box=WIDE,
        right=dict(title="حتى 23/11", value="632,90", sub="الأكسيز على 1000 لتر", icon="gas-station", color="green"),
        left=dict(title="من 24/11", value="672,90", sub="إلى ما تمدش", icon="gas-station", color="red"), gap=4.0),
   dict(k="big", text="2,44 €", sub="زايدين فـ50 لتر", at="شحال كيعني هادشي فالجيب؟", until="وإلى كتعمر جوج مرات"),
   dict(k="big", text="≈ 20 €", sub="فالشهر: جوج عمرات فالسيمانة", at="وإلى كتعمر جوج مرات", until="وعلاش الخصم كان صغير"),
   dict(k="icons", at="وعلاش الخصم كان صغير", until="وشحال الثمن دابا؟", box=ICO, items=[
     ["receipt-tax", "الضريبة الزايدة", "gold"], ["gas-station", "خصم صغير", "green"], ["clock", "مدة قصيرة", "red"]], gap=2.0),
   dict(k="bars", at="وشحال الثمن دابا؟", until="شنو تدير؟ ما كنقولوش", box=BAR, bars=[
     ["ليصانص", 1.941, "1,941 €", "gold"], ["المازوط", 2.197, "2,197 €", "red"]]),
   dict(k="map", view="italy", pins=["Milano", "Roma", "Napoli"], labels=False, at="شنو تدير؟ ما كنقولوش", until="وإلى كنتي ناوي تهبط", box=R_BOX),
   dict(k="icons", at="شنو تدير؟ ما كنقولوش", until="وإلى كنتي ناوي تهبط", box=L_BOX, items=[
     ["world", "قارن الأثمنة", "blue"], ["truck", "الكاميو: المحاسب", "gold"]], gap=3.0),
   dict(k="map", **MED, route=["Genova", "Tanger", "ship"], at="وإلى كنتي ناوي تهبط", until="وسؤال كيجينا بزاف", box=(160, 200, 1760, 880)),
   dict(k="people", at="وسؤال كيجينا بزاف", box=FULL, people=["woman", "man"],
        say=[dict(who=0, text="والليصانص؟", at=0.6), dict(who=1, text="لا، غير المازوط", at=4.0, bg="green")]),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="02 · البلاك فرايداي", src=S_BF, items=[
   dict(k="chapter", num="02", title="البلاك فرايداي: التخفيض الحقيقي", at=0.2, until="النهار الكبير"),
   dict(k="calendar", at="النهار الكبير", until="وبزاف ديال الناس", box=R_BOX, day=27, month=11, sub="الجمعة: البلاك فرايداي"),
   dict(k="calendar", at="ومن بعد كاين السايبر", until="وبزاف ديال الناس", box=L_BOX, day=30, month=11, sub="السايبر مانداي"),
   dict(k="people", at="وبزاف ديال الناس", until="ولكن خاصك تعرف قاعدة", box=FULL, people=["girl", "man", "hijab"],
        say=[dict(who=0, text="نشري التيليفون دابا؟", at=0.6), dict(who=2, text="شوف الثمن قبل", at=3.5, bg="gold")]),
   dict(k="head", text="أرخص ثمن فـ30 يوم", sub="هو الثمن القديم ديال التخفيض", at="ولكن خاصك تعرف قاعدة", until="خود مثال من عندنا"),
   dict(k="steps", at="خود مثال من عندنا", until="واش هادا تخفيض؟", box=WIDE, steps=[
     ["طول الشهر", "120 €"], ["الأسبوع اللي فات", "150 €"], ["اليوم: «تخفيض»", "120 €"]], gap=3.5, check_after=0.6),
   dict(k="vs", at="واش هادا تخفيض؟", until="ومثال تاني", box=WIDE,
        right=dict(title="تخفيض كذاب", value="120 €", sub="نفس الثمن", icon="x", color="red"),
        left=dict(title="تخفيض حقيقي", value="< 120 €", sub="تحت أرخص ثمن", icon="check", color="green"), gap=3.0),
   dict(k="bars", at="ومثال تاني", until="إذن قبل ما تشري", box=BAR, bars=[
     ["أرخص ثمن فالشهر", 60, "60 €", "gold"], ["اليوم", 48, "48 €", "green"]]),
   dict(k="text", text="ربحتي 12 € (20%)", at="هنا التخفيض حقيقي", until="إذن قبل ما تشري", y=900, size=46),
   dict(k="icons", at="إذن قبل ما تشري", until="وزيد على هادشي", box=ICO, items=[
     ["chart-bar", "التاريخ ديال الثمن", "blue"], ["camera", "صور الثمن", "gold"]], gap=3.0),
   dict(k="icons", at="أولا، شري من السيت", until="رابعا، رد البال", box=ICO, items=[
     ["world", "سيت معروف", "green"], ["credit-card", "خلص بالكارطا", "blue"], ["key", "ما تعطي الكود", "red"]], gap=4.0),
   dict(k="people", at="رابعا، رد البال", until="وإلى شريتي أونلاين", box=FULL, people=["elder", "woman"],
        say=[dict(who=0, text="خلص شي أورو للكولي؟", at=0.6), dict(who=1, text="تقلاب! ما تكليكيش", at=3.5, bg="red")]),
   dict(k="vs", at="وإلى شريتي أونلاين", until="وعلى كل حاجة جديدة", box=WIDE,
        right=dict(title="أونلاين", value="14", sub="يوم باش ترجعو", icon="world", color="green"),
        left=dict(title="فالحانوت", value="لا", sub="غير إلى بغا الحانوت", icon="building-store", color="red"), gap=4.0),
   dict(k="big", text="2", sub="عامين ديال الضمانة", at="وعلى كل حاجة جديدة", until="وإلى شفتي شي تخفيض كذاب"),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="وإلى شفتي شي تخفيض كذاب", until="شوف هاد الصورة", box=R_BOX),
   dict(k="icons", at="وإلى شفتي شي تخفيض كذاب", until="شوف هاد الصورة", box=L_BOX, items=[
     ["alert-triangle", "بلغ على التخفيض الكذاب", "gold"]], gap=1.0),
   dict(k="vs", at="شوف هاد الصورة", until="وخلي شي فلوس لدجنبر", box=WIDE,
        right=dict(title="لائحة من قبل", value="ربح", sub="مقارن الأثمنة", person="woman", color="green"),
        left=dict(title="كيشري وصافي", value="خسارة", sub="غير حيت تخفيض", person="man", color="red"), gap=4.0),
   dict(k="icons", at="وخلي شي فلوس لدجنبر", until="وسؤال من عندكم", box=ICO, items=[
     ["home", "الكرا", "blue"], ["bolt", "الضو", "gold"], ["wallet", "آخر العام", "green"]], gap=2.0),
   dict(k="people", at="وسؤال من عندكم", box=FULL, people=["student", "clerk"],
        say=[dict(who=0, text="نقدر نرجعو للحانوت؟", at=0.6), dict(who=1, text="سول على السياسة ديالهم", at=4.0, bg="gold")]),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="03 · الميزانية ديال 2027", src=S_MAN, items=[
   dict(k="chapter", num="03", title="الميزانية ديال 2027: باقي مشروع", at=0.2, until="هي دابا فالبرلمان"),
   dict(k="map", view="italy", hl=["Lazio"], pins=["Roma"], labels=False, at="هي دابا فالبرلمان", until="البرلمانيين قدمو", box=R_BOX),
   dict(k="big", text="6.600", sub="تعديل تقريبا", at="البرلمانيين قدمو", until="اليوم، فالعشية"),
   dict(k="steps", at="اليوم، فالعشية", until="إذن كل حاجة غادي نقولوها", box=WIDE, steps=[
     ["التعديلات المقبولة", "23/11"], ["التصويت فاللجنة", "دجنبر"], ["النواب + الشيوخ", "?"], ["القانون", "31/12"]], gap=3.0, check_after=99),
   dict(k="warn", text="باقي مشروع، ماشي قانون", at="إذن كل حاجة غادي نقولوها", until="شنو كاين فالنص", y=600),
   dict(k="bars", at="أولا، الضريبة على الدخل", until="مثلا، كريم", box=BAR, bars=[
     ["الشريحة دابا حتى", 50000, "50.000 €", "grey"], ["الشريحة فالمشروع حتى", 55000, "55.000 €", "gold"]]),
   dict(k="vs", at="مثلا، كريم", until="تانيا، الكونجي", box=WIDE,
        right=dict(title="كريم فبريشا", value="30.000 €", sub="ما كيتبدل والو", person="worker", color="grey"),
        left=dict(title="سارة", value="53.000 €", sub="كتستافد شوية", person="woman", color="green"), gap=4.0),
   dict(k="people", at="تانيا، الكونجي", until="تالتا، البونس ديال التشغيل", box=L_BOX, people=["hijab", "child"],
        say=[dict(who=0, text="شهر زايد بـ80%؟", at=0.8)]),
   dict(k="vs", at="دابا، كاين تلاتة", until="تالتا، البونس ديال التشغيل", box=R_BOX,
        right=dict(title="دابا", value="3", sub="شهور بـ80%", icon="calendar", color="grey"),
        left=dict(title="المشروع", value="4", sub="شهور بـ80%", icon="calendar", color="green"), gap=3.0),
   dict(k="icons", at="تالتا، البونس ديال التشغيل", until="رابعا، الكارطا", box=L_BOX, items=[
     ["user", "النساء", "gold"], ["school", "تحت 35 عام", "blue"], ["map-pin", "الجنوب", "green"]], gap=2.5),
   dict(k="map", view="south", pins=["Napoli", "Bari", "Palermo"], labels=False, at="وفالجنوب", until="رابعا، الكارطا", box=R_BOX),
   dict(k="big", text="300 €", sub="كارطا للناس فوق 75 عام", at="رابعا، الكارطا", until="ولكن هاد الكارطا باقي"),
   dict(k="people", at="ولكن هاد الكارطا باقي", until="خامسا، البانسيون", box=FULL, people=["elder", "woman", "doctor"],
        say=[dict(who=0, text="غير للصحة؟", at=0.6), dict(who=1, text="ولا للبادانطي؟", at=3.0), dict(who=2, text="باقي كيتناقشو", at=6.0, bg="gold")]),
   dict(k="bars", at="خامسا، البانسيون", until="وسادسا، كاين اقتراح", box=BAR, bars=[
     ["دابا: 4 مرات", 4, "≈ 2.447 €", "grey"], ["اقتراح: 5 مرات", 5, "≈ 3.000 €", "gold"], ["اقتراح: 6 مرات", 6, "؟", "gold"]]),
   dict(k="icons", at="وسادسا، كاين اقتراح", until="ما غاديش ندخلو فالسياسة", box=ICO, items=[
     ["receipt", "الروتاماسيون", "gold"], ["home", "الكوندونو", "gold"]], gap=3.0),
   dict(k="steps", at="ما غاديش ندخلو فالسياسة", until="وملي يتصادق القانون", box=WIDE, steps=[
     ["القانون فالجريدة الرسمية", "1"], ["التعليمات ديال الإينبس", "2"], ["الطلب ديالك", "3"]], gap=3.5, check_after=99),
   dict(k="people", at="شكون مهتم بهاد الخبر؟", until="وسؤال من عندكم", box=FULL, people=["man", "student", "elder"],
        say=[dict(who=1, text="باقي ما بدا والو", at=1.5, bg="gold")]),
   dict(k="vs", at="وسؤال من عندكم", box=WIDE,
        right=dict(title="البونس 2026", value="60 €", sub="فالشهر: الطلب حتى 31/12", icon="calendar", color="green"),
        left=dict(title="البونس 2027", value="100 €", sub="باقي مشروع", icon="clock", color="gold"), gap=4.0),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="04 · الإينبس والبانسيون", src=S_INPS, items=[
   dict(k="chapter", num="04", title="الإينبس: رسائل رقمية والبانسيون", at=0.2, until="رقم تلاتة آلاف"),
   dict(k="head", text="الرسالة 3801", sub="19 نونبر 2026", at="رقم تلاتة آلاف", until="شنو كتقول؟"),
   dict(k="calendar", at="شنو كتقول؟", until="شنو هي هاد الرسائل؟", box=R_BOX, day=1, month=1, sub="من يناير 2027، شوية بشوية"),
   dict(k="people", at="شنو كتقول؟", until="شنو هي هاد الرسائل؟", box=L_BOX, people=["clerk"],
        say=[dict(who=0, text="الرسائل عبر سيند", at=0.8, bg="green")]),
   dict(k="people", at="شنو هي هاد الرسائل؟", until="المرحلة الأولى", box=FULL, people=["elder", "man"],
        say=[dict(who=0, text="علاش خاصني نرجع الفلوس؟", at=0.6), dict(who=1, text="شوف السبب فالرسالة", at=4.5, bg="gold")]),
   dict(k="steps", at="المرحلة الأولى", until="فين غادي توصلك؟", box=WIDE, steps=[
     ["البانسيونات والأسينيو سوسيالي", "1"], ["الإعاقة المدنية", "2"]], gap=3.5, check_after=99),
   dict(k="icons", at="فين غادي توصلك؟", until="وإلى ما عندكش السبيد", box=ICO, items=[
     ["phone", "الأبليكاسيون آيو", "blue"], ["mail", "البيك", "gold"], ["world", "السيت بالسبيد", "green"]], gap=3.0),
   dict(k="map", view="north", pins=["Milano", "Torino", "Bologna"], labels=False, at="وإلى ما عندكش السبيد", until="والإجراءات ديال الاسترجاع", box=R_BOX),
   dict(k="icons", at="وإلى ما عندكش السبيد", until="والإجراءات ديال الاسترجاع", box=L_BOX, items=[
     ["mailbox", "رسالة مضمونة", "gold"], ["users", "توكيل", "blue"]], gap=3.0),
   dict(k="warn", text="الأجل كيبدا يدور عليك", at="علاش هادشي مهم؟", until="إذن نصيحة", y=600),
   dict(k="people", at="إذن نصيحة", until="وكون عاقل", box=FULL, people=["girl", "elder"],
        say=[dict(who=0, text="نفعلو الإشعارات", at=0.8, bg="green"), dict(who=1, text="عاوني يا بنتي", at=4.0)]),
   dict(k="warn", text="الإينبس ما كتطلبش الكود ديال السبيد", at="وكون عاقل", until="وشنو تدير إلى وصلاتك", y=600),
   dict(k="steps", at="وشنو تدير إلى وصلاتك", until="ودابا، البانسيون ديال دجنبر", box=WIDE, steps=[
     ["قرا المبلغ والسبب", "1"], ["الباطرونا", "2"], ["الأقساط", "3"]], gap=3.5, check_after=0.6),
   dict(k="calendar", at="ودابا، البانسيون ديال دجنبر", until="ومعاها كاينة التريديشيما", box=R_BOX, day=1, month=12, sub="البانسيون + التريديشيما"),
   dict(k="map", view="italy", pins=["Torino", "Bologna", "Napoli"], labels=False, at="ودابا، البانسيون ديال دجنبر", until="ومعاها كاينة التريديشيما", box=L_BOX),
   dict(k="vs", at="ومعاها كاينة التريديشيما", until="واللي عندهم بانسيون صغيرة", box=WIDE,
        right=dict(title="طول العام", value="12/12", sub="شهر كامل تقريبا", icon="calendar", color="green"),
        left=dict(title="من يوليوز", value="6/12", sub="غير الجزء", icon="calendar", color="gold"), gap=4.0),
   dict(k="big", text="154,94 €", sub="زيادة حتى هاد المبلغ، بلا طلب", at="واللي عندهم بانسيون صغيرة", until="ومن بعد، الأسينيو أونيكو"),
   dict(k="calendar", at="ومن بعد، الأسينيو أونيكو", until="وما تنساش: الإيزي", box=R_BOX, day=16, month=12, sub="16-17 دجنبر"),
   dict(k="people", at="واللي قدمو طلب جديد", until="وما تنساش: الإيزي", box=L_BOX, people=["hijab", "clerk"],
        say=[dict(who=0, text="وأنا طلب جديد؟", at=0.6), dict(who=1, text="آخر الشهر", at=3.0, bg="gold")]),
   dict(k="steps", at="وما تنساش: الإيزي", until="شكون معني", box=WIDE, steps=[
     ["الإيزي كيسالي", "31/12"], ["الديسو الجديدة", "يناير"], ["الأسينيو كامل", "قبل 28/2"]], gap=3.0, check_after=99),
   dict(k="people", at="وسؤال كيجينا", box=FULL, people=["elder", "clerk"],
        say=[dict(who=0, text="ما عنديش السبيد؟", at=0.6), dict(who=1, text="رسالة فالبوسطا", at=4.0, bg="green")]),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="05 · الجنسية، الكود والفلوسي", src=S_CIT, items=[
   dict(k="chapter", num="05", title="الجنسية والكود والديكري", at=0.2, until="كاين مشروع قانون"),
   dict(k="steps", at="كاين مشروع قانون", until="شنو فيه؟", box=WIDE, steps=[
     ["اللجنة", "14/10"], ["القاعة ديال النواب", "دابا"], ["مجلس الشيوخ", "؟"], ["قانون", "؟"]], gap=3.0, check_after=99),
   dict(k="warn", text="باقي مشروع، ماشي قانون", at="إذن هو باقي مشروع", until="شنو فيه؟", y=880),
   dict(k="vs", at="أولا، اللغة", until="تانيا، كاين أسباب", box=WIDE,
        right=dict(title="دابا", value="معفي", sub="اللي عندو الكارطا", icon="id", color="green"),
        left=dict(title="المشروع", value="B1", sub="الشهادة خاصة", icon="certificate", color="gold"), gap=5.0),
   dict(k="icons", at="تانيا، كاين أسباب", until="والمدة ديال الجواب", box=ICO, items=[
     ["scale", "جرائم خطيرة", "red"], ["clock", "قضية: الملف كيتوقف", "gold"], ["heart", "اليمين بالطاليانية", "blue"]], gap=4.0),
   dict(k="big", text="24 / 36", sub="شهر ديال الجواب", at="والمدة ديال الجواب", until="شنو كيعني هادشي ليك؟"),
   dict(k="people", at="شنو كيعني هادشي ليك؟", until="كاين ربعة ديال الجهات", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="نطلب دابا؟", at=0.6), dict(who=1, text="القواعد ديال اليوم", at=3.5, bg="green")]),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="كاين ربعة ديال الجهات", until="ودابا الكود ديال الطريق", box=R_BOX),
   dict(k="icons", at="كاين ربعة ديال الجهات", until="ودابا الكود ديال الطريق", box=L_BOX, items=[
     ["school", "سيينا", "blue"], ["school", "بيروجا", "blue"], ["school", "روما تري", "blue"], ["school", "دانتي", "blue"]], gap=1.5),
   dict(k="big", text="65", sub="تجديد البيرمي كل 10 سنين (مشروع)", at="ودابا الكود ديال الطريق", until="ولكن مجلس الدولة"),
   dict(k="icons", at="ولكن مجلس الدولة", until="الأجل باش تجاوب", box=ICO, items=[
     ["scale", "مجلس الدولة", "gold"], ["file-text", "وثائق ناقصة", "red"], ["key", "الخصوصية", "blue"]], gap=2.5),
   dict(k="calendar", at="الأجل باش تجاوب", until="ومن بعد، البرلمان", box=R_BOX, day=25, month=11, sub="جواب الحكومة"),
   dict(k="people", at="الأجل باش تجاوب", until="والبيرمي المغربي؟", box=L_BOX, people=["worker"],
        say=[dict(who=0, text="الخطيات القدام", at=3.0, bg="gold")]),
   dict(k="map", **MED, route=["Casablanca", "Torino"], at="والبيرمي المغربي؟", until="وفالأخير الديكري فلوسي", box=(160, 170, 1760, 790)),
   dict(k="text", text="عام واحد · أقل من 6 سنين · قبل الريزيدينسا", at="كيبقى صالح عام واحد", until="وفالأخير الديكري فلوسي", y=850, size=40),
   dict(k="calendar", at="وفالأخير الديكري فلوسي", until="والكليك داي ديال الخدمة", box=R_BOX, day=7, month=12, sub="قبل الساعة 20:00"),
   dict(k="people", at="وفالأخير الديكري فلوسي", until="والكليك داي ديال الخدمة", box=L_BOX, people=["office", "worker"],
        say=[dict(who=0, text="أنا اللي نطلب", at=1.0, bg="green")]),
   dict(k="calendar", at="والكليك داي ديال الخدمة", until="وانتبه: الطلب", box=WIDE, day=16, month=2, sub="الكليك داي: 9 ديال الصباح"),
   dict(k="people", at="وانتبه: الطلب", until="وهاد الأيام، كتسمع", box=FULL, people=["man", "elder"],
        say=[dict(who=0, text="عطيني الفلوس ونجيب ليك الكونطرا", at=0.6, bg="red"), dict(who=1, text="هادي تقلاب", at=4.0, bg="red")]),
   dict(k="icons", at="وهاد الأيام، كتسمع", until="وسؤال: واش القانون", box=ICO, items=[
     ["phone", "الواتساب: لا", "red"], ["file-certificate", "المصادر الرسمية", "green"], ["users", "الباطرونا", "blue"]], gap=2.5),
   dict(k="people", at="وسؤال: واش القانون", box=FULL, people=["hijab", "clerk"],
        say=[dict(who=0, text="والطلب اللي قدمت؟", at=0.6), dict(who=1, text="نستناو النص النهائي", at=4.0, bg="gold")]),
 ]),
 dict(audio="F.wav", text=T["F"], chapter="06 · مثال: بونس الولادة", src=S_NN, items=[
   dict(k="chapter", num="06", title="مثال عملي: 1.000 € ديال الولادة", at=0.2, until="هاد البونس كتعطيه"),
   dict(k="big", text="1.000 €", sub="مرة وحدة على كل ولد", at="هاد البونس كتعطيه", until="الشروط: أولا"),
   dict(k="icons", at="الشروط: أولا", until="والأهم: الأجل", box=ICO, items=[
     ["calculator", "الإيزي تحت 40.000", "green"], ["home", "ساكن فإيطاليا", "blue"], ["id", "بيرميسو صالح", "gold"]], gap=5.0),
   dict(k="big", text="120", sub="يوم من نهار الزيادة", at="والأهم: الأجل", until="خلينا نشوفو"),
   dict(k="map", view="north", pins=["Bergamo", "Torino"], labels=False, at="خلينا نشوفو", until="الحساب: من واحد غشت", box=R_BOX),
   dict(k="people", at="العائلة الأولى", until="الحساب: من واحد غشت", box=L_BOX, people=["hijab", "man"],
        say=[dict(who=0, text="ريم تزادت 1 غشت", at=1.0)]),
   dict(k="steps", at="الحساب: من واحد غشت", until="العائلة التانية", box=WIDE, steps=[
     ["الزيادة", "1/8"], ["زيد 120 يوم", "="], ["آخر أجل", "29/11"]], gap=3.0, check_after=99),
   dict(k="vs", at="العائلة التانية", until="ولكن واش يستناو؟", box=WIDE,
        right=dict(title="ريم فبيرغامو", value="29/11", sub="آخر أجل: الأحد", person="hijab", color="red"),
        left=dict(title="الولد فتورينو", value="20/3", sub="2027، ولكن طلب دابا", person="woman", color="green"), gap=4.0),
   dict(k="warn", text="الفلوس بالترتيب حتى تسالي الميزانية", at="حيت الفلوس كتخلص بالترتيب", until="وكل ولد عندو", y=600),
   dict(k="people", at="وكل ولد عندو", until="شنو خاصك؟", box=FULL, people=["woman", "child", "girl"],
        say=[dict(who=0, text="جوج توام: جوج طلبات", at=1.0, bg="green")]),
   dict(k="icons", at="شنو خاصك؟", until="وكيفاش تطلب؟", box=ICO, items=[
     ["calculator", "الإيزي ديال الولد", "green"], ["key", "السبيد / الكارطا", "blue"], ["file-text", "المعلومات ديال الولد", "gold"]], gap=5.0),
   dict(k="icons", at="وكيفاش تطلب؟", until="الخطوات: كتدخل", box=ICO, items=[
     ["world", "السيت ديال الإينبس", "blue"], ["phone", "الأبليكاسيون", "green"], ["users", "الباطرونا", "gold"]], gap=2.5),
   dict(k="steps", at="الخطوات: كتدخل", until="ومن بعد، تبع الحالة", box=WIDE, steps=[
     ["دخل بالسبيد", "1"], ["بونس المولود الجديد", "2"], ["عمر وصيفط", "3"], ["حفظ الإيصال", "4"]], gap=2.5, check_after=99),
   dict(k="people", at="ومن بعد، تبع الحالة", until="شنو هي الأخطاء", box=FULL, people=["clerk", "man"],
        say=[dict(who=0, text="جاوب بسرعة", at=2.5, bg="gold")]),
   dict(k="steps", at="شنو هي الأخطاء", until="والخطأ الخامس", box=WIDE, steps=[
     ["تستنى الإيزي الجديد", "1"], ["إيزي فيه غلط", "2"], ["طلب لجوج ولاد", "3"], ["الأجل من الكومون", "4"]], gap=4.0, check_after=0.4, bad=True),
   dict(k="people", at="والخطأ الخامس", until="وحاجة أخرى", box=FULL, people=["elder", "hijab"],
        say=[dict(who=0, text="تبع الطلب!", at=0.8, bg="red")]),
   dict(k="calendar", at="وحاجة أخرى", until="ونعاودو: هاد المعلومات", box=R_BOX, day=12, month=8, sub="الأجل الخاص: فات"),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="وحاجة أخرى", until="ونعاودو: هاد المعلومات", box=L_BOX),
   dict(k="people", at="ونعاودو: هاد المعلومات", until="وسؤال: واش هاد الفلوس", box=FULL, people=["clerk", "woman"],
        say=[dict(who=0, text="البيرميسو فالتجديد؟ سول", at=1.0, bg="gold")]),
   dict(k="vs", at="وسؤال: واش هاد الفلوس", box=WIDE,
        right=dict(title="البونس", value="1.000 €", sub="مرة وحدة", icon="coin-euro", color="green"),
        left=dict(title="الأسينيو", value="كل شهر", sub="حاجة أخرى", icon="calendar", color="blue"), gap=3.0),
 ]),
 dict(audio="G.wav", text=T["G"], chapter="07 · من المغرب", src=S_MAR, items=[
   dict(k="chapter", num="07", title="من المغرب: الكرا والدرهم", at=0.2, until="مجلس النواب صادق"),
   dict(k="steps", at="مجلس النواب صادق", until="شنو فيه اللي يقدر", box=WIDE, steps=[
     ["مجلس النواب", "ok"], ["مجلس المستشارين", "17/11"], ["القراءة التانية", "؟"]], gap=3.0, check_after=99),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Rabat"], labels=False, at="شنو فيه اللي يقدر", until="المشروع كيطلع هاد العتبة", box=(160, 200, 1760, 880)),
   dict(k="bars", at="المشروع كيطلع هاد العتبة", until="خود مثال من عندنا", box=BAR, bars=[
     ["العتبة دابا", 40000, "40.000 DH", "grey"], ["العتبة فالمشروع", 60000, "60.000 DH", "gold"]]),
   dict(k="map", **MED, route=["Milano", "Tanger"], at="خود مثال من عندنا", until="مع العتبة القديمة", box=(160, 200, 1760, 880)),
   dict(k="steps", at="مع العتبة القديمة", until="ولكن الضريبة على الكرا", box=WIDE, steps=[
     ["4.000 DH × 12", "48.000"], ["فوق 40.000", "دابا"], ["تحت 60.000", "المشروع"]], gap=3.0, check_after=0.6),
   dict(k="people", at="ولكن الضريبة على الكرا", until="وفالمشروع حتى أشياء", box=FULL, people=["man", "office"],
        say=[dict(who=0, text="ونخلص الضريبة؟", at=0.6), dict(who=1, text="سول محاسب فالمغرب", at=3.5, bg="gold")]),
   dict(k="icons", at="وفالمشروع حتى أشياء", until="وما لقيناش فالمصادر", box=ICO, items=[
     ["briefcase", "أوطو أونطروبرونور", "blue"], ["percentage", "من 30% لـ20%", "green"], ["trending-down", "الضريبة كتنقص", "gold"]], gap=4.0),
   dict(k="warn", text="ما كاين حتى إجراء خاص بالمغاربة اللي برا", at="وما لقيناش فالمصادر", until="الخبر التاني: الدرهم", y=600),
   dict(k="vs", at="الخبر التاني: الدرهم", until="شنو كيعني هادشي إلى كتصيفط", box=WIDE,
        right=dict(title="قدام الأورو", value="-0,6%", sub="الدرهم، السيمانة اللي فاتت", icon="currency-euro", color="gold"),
        left=dict(title="قدام الدولار", value="-1,7%", sub="الدرهم، السيمانة اللي فاتت", icon="coin-euro", color="gold"), gap=4.0),
   dict(k="map", **MED, route=["Milano", "Casablanca"], at="شنو كيعني هادشي إلى كتصيفط", until="إلى صيفطتي ألف أورو", box=(160, 200, 1760, 880)),
   dict(k="big", text="+60 / 70 DH", sub="على 1.000 € تقريبا", at="إلى صيفطتي ألف أورو", until="ولكن هادا هو الثمن المرجعي"),
   dict(k="people", at="ولكن هادا هو الثمن المرجعي", until="الخبر التالت", box=FULL, people=["hijab", "worker"],
        say=[dict(who=0, text="شحال غادي يوصل بالدرهم؟", at=1.0), dict(who=1, text="قارن جوج ولا تلاتة", at=5.0, bg="green")]),
   dict(k="steps", at="الخبر التالت", until="وهادي كتنفع", box=WIDE, steps=[
     ["الطلب أونلاين", "1"], ["الخلاص أونلاين", "2"], ["القنصلية", "3"]], gap=3.0, check_after=0.6),
   dict(k="map", **MED, pins=["Milano", "Roma"], at="وهادي كتنفع", until="وسؤال: واش كاين", box=R_BOX),
   dict(k="people", at="وهادي كتنفع", until="وسؤال: واش كاين", box=L_BOX, people=["clerk"],
        say=[dict(who=0, text="سول الإدارة الإيطالية", at=1.0, bg="gold")]),
   dict(k="map", **MED, route=["Genova", "Tanger", "ship"], at="وسؤال: واش كاين", box=(160, 200, 1760, 880)),
 ]),
 dict(audio="H.wav", text=T["H"], chapter="08 · سؤال وجواب", src=S_QA, items=[
   dict(k="chapter", num="08", title="سؤال وجواب", at=0.2, until="السؤال الأول"),
   dict(k="people", at="السؤال الأول", until="لا، باقي عندك الوقت", box=FULL, people=["hijab", "child"],
        say=[dict(who=0, text="تزاد 15 شتنبر: فاتني؟", at=0.8)]),
   dict(k="steps", at="لا، باقي عندك الوقت", until="السؤال التاني", box=WIDE, steps=[
     ["الزيادة", "15/9"], ["زيد 120 يوم", "="], ["آخر أجل", "13/1"]], gap=2.5, check_after=99),
   dict(k="people", at="السؤال التاني", until="إلى شريتيه من الحانوت", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="نرجع التيليفون؟", at=0.8)]),
   dict(k="vs", at="إلى شريتيه من الحانوت", until="السؤال التالت", box=WIDE,
        right=dict(title="الحانوت", value="لا", sub="غير السياسة ديالهم", icon="building-store", color="red"),
        left=dict(title="أونلاين", value="14", sub="يوم", icon="world", color="green"), gap=3.0),
   dict(k="people", at="السؤال التالت", until="نعم. من واحد دجنبر", box=FULL, people=["woman", "girl"],
        say=[dict(who=0, text="تبدال الضو ولا ساهل؟", at=0.8)]),
   dict(k="calendar", at="نعم. من واحد دجنبر", until="ولكن قبل ما تبدل", box=R_BOX, day=1, month=12, sub="الضو: نهار خدمة واحد"),
   dict(k="map", view="north", pins=["Bologna"], labels=False, at="نعم. من واحد دجنبر", until="ولكن قبل ما تبدل", box=L_BOX),
   dict(k="icons", at="ولكن قبل ما تبدل", until="السؤال الرابع", box=ICO, items=[
     ["bolt", "غير الضو", "gold"], ["alert-triangle", "غرامة؟", "red"], ["clock", "14 يوم", "green"]], gap=2.5),
   dict(k="people", at="السؤال الرابع", until="مع القواعد ديال اليوم", box=FULL, people=["worker", "clerk"],
        say=[dict(who=0, text="الكارطا وبي واحد؟", at=0.8)]),
   dict(k="vs", at="مع القواعد ديال اليوم", until="السؤال الخامس", box=WIDE,
        right=dict(title="اليوم", value="معفي", sub="مع الكارطا", icon="id", color="green"),
        left=dict(title="المشروع", value="B1", sub="باقي ماشي قانون", icon="clock", color="gold"), gap=3.0),
   dict(k="people", at="السؤال الخامس", until="لا، الزيادة كتجي", box=FULL, people=["hijab", "elder"],
        say=[dict(who=0, text="الوالدة خاصها تطلب؟", at=0.8)]),
   dict(k="big", text="154,94 €", sub="أوتوماتيكيا مع 1 دجنبر", at="لا، الزيادة كتجي", until="السؤال السادس"),
   dict(k="people", at="السؤال السادس", until="نعم. الدار ولا الجزء", box=FULL, people=["man", "woman"],
        say=[dict(who=0, text="الدار فالمغرب فالإيزي؟", at=0.8)]),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Nador", "Casablanca"], labels=False, at="نعم. الدار ولا الجزء", until="السؤال السابع", box=R_BOX),
   dict(k="icons", at="نعم. الدار ولا الجزء", until="السؤال السابع", box=L_BOX, items=[
     ["home", "الدار", "gold"], ["building-bank", "الكونطو", "gold"]], gap=2.0),
   dict(k="people", at="السؤال السابع", until="نعم، الأكونطو التاني", box=FULL, people=["hijab", "office"],
        say=[dict(who=0, text="عندي البارطيتا إيفا", at=0.8)]),
   dict(k="calendar", at="نعم، الأكونطو التاني", until="السؤال التامن", box=WIDE, day=30, month=11, sub="الأكونطو التاني: إف 24"),
   dict(k="people", at="السؤال التامن", until="السؤال التاسع", box=FULL, people=["worker", "clerk"],
        say=[dict(who=0, text="المازوط من غدا؟", at=0.8), dict(who=1, text="الخصم كيسالي اليوم", at=4.0, bg="gold")]),
   dict(k="people", at="السؤال التاسع", until="ومن بعد كيستنى الكليك داي", box=FULL, people=["office", "man"],
        say=[dict(who=1, text="نجيب خويا من المغرب؟", at=0.8), dict(who=0, text="قبل 7 دجنبر", at=5.0, bg="green")]),
   dict(k="map", **MED, route=["Casablanca", "Treviso"], at="ومن بعد كيستنى الكليك داي", until="وإلى عندك سؤال آخر", box=(160, 200, 1760, 880)),
   dict(k="people", at="وإلى عندك سؤال آخر", box=FULL, people=["girl", "elder", "man"],
        say=[dict(who=0, text="كتب سؤالك فالكومونتير", at=0.8, bg="green")]),
 ]),
 dict(audio="I.wav", text=T["I"], chapter="09 · الخلاصة والتواريخ", src=S_HOME, items=[
   dict(k="head", text="الخلاصة", at=0.2, until="واحد: الخصم ديال المازوط"),
   dict(k="rows", at="واحد: الخصم ديال المازوط", until="خمسة: البانسيون", y=300, gap=110, size=46, rows=[
     ("الخصم ديال المازوط", "23/11", "واحد: الخصم"),
     ("البلاك فرايداي", "27/11", "جوج: البلاك"),
     ("الميزانية: مشروع", "?", "تلاتة: الميزانية"),
     ("رسائل الإينبس", "2027", "ربعة: الإينبس"),
   ]),
   dict(k="rows", at="خمسة: البانسيون", until="ودابا التواريخ ديال الأيام", y=300, gap=110, size=46, rows=[
     ("البانسيون والتريديشيما", "1/12", "خمسة: البانسيون"),
     ("الجنسية والكود: مشاريع", "?", "ستة: مشروع"),
     ("بونس الولادة", "1.000 €", "سبعة: البونس"),
     ("الكرا فالمغرب", "60.000 DH", "تمنية: فالمغرب"),
     ("الإيزي: الدار فالمغرب", "!", "وتسعة: إلى عندك"),
   ]),
   dict(k="steps", at="ودابا التواريخ ديال الأيام", until="الأحد تسعة وعشرين", box=WIDE, steps=[
     ["المازوط", "23/11"], ["الكود ديال الطريق", "25/11"], ["البلاك فرايداي", "27/11"]], gap=3.5, check_after=99),
   dict(k="steps", at="الأحد تسعة وعشرين", until="الاثنين سبعة دجنبر", box=WIDE, steps=[
     ["بونس الولادة (1/8)", "29/11"], ["الأكونطو التاني", "30/11"], ["البانسيون + الضو", "1/12"]], gap=4.0, check_after=99),
   dict(k="steps", at="الاثنين سبعة دجنبر", until="وإلى فاتك شي فيديو", box=WIDE, steps=[
     ["الديكري فلوسي", "7/12"], ["الأسينيو", "16/12"], ["الإيزي + بونس الماماوات", "31/12"]], gap=4.0, check_after=99),
   dict(k="icons", at="وإلى فاتك شي فيديو", until="وإلى كنتي كتسنى شي خبر", box=ICO, items=[
     ["heart", "الجنسية", "gold"], ["car", "تبديل البيرمي", "blue"], ["id", "البيرميسو", "gold"], ["briefcase", "النازبي", "green"]], gap=2.0),
   dict(k="map", view="italy", hl=["Lazio"], pins=["Roma"], labels=False, at="وإلى كنتي كتسنى شي خبر", until="ونعاودو نقولو", box=R_BOX),
   dict(k="people", at="ونعاودو نقولو", until="وتذكير صغير", box=FULL, people=["clerk", "woman"],
        say=[dict(who=0, text="سول الباطرونا ولا الكاف", at=1.0, bg="green")]),
   dict(k="people", at="وتذكير صغير", until="وحاجة أخيرة: ما تعطيش", box=FULL, people=["elder", "man"],
        say=[dict(who=0, text="شوف الفيش ديال الخلاص", at=1.0), dict(who=1, text="بدا بالأجل القريب", at=6.0, bg="gold")]),
   dict(k="warn", text="ما تعطيش السبيد ديالك لحتى واحد", at="وحاجة أخيرة: ما تعطيش", until="وإلى عجبك هاد الفيديو", y=640),
   dict(k="cta", at="وإلى عجبك هاد الفيديو", until="وكتب لينا فالكومونتير", text="ابوني فالقناة", sub="وفعل الجرس"),
   dict(k="people", at="وكتب لينا فالكومونتير", box=FULL, people=["girl", "worker", "hijab"],
        say=[dict(who=1, text="شنو فاد بيك أكثر؟", at=0.8), dict(who=2, text="صيفطو لشي واحد", at=6.0, bg="green")]),
 ]),
]

THUMB = dict(
  title=[("خصم المازوط كيسالي اليوم", (236, 196, 96)), "البلاك فرايداي: التخفيض الحقيقي", "1.000 أورو للولادة فـ120 يوم"],
  num="23/11", numsub="آخر نهار ديال الخصم",
  bottom="مغاربة إيطاليا · خبار مفيدة بالدارجة",
)
