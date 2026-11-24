import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-24.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo1-2026-11-24-final")
BRAND = "مغاربة إيطاليا"
T = {k: v.replace("گ", "ك") for k, v in JOB["blocks"].items()}
EDITS = json.load(open(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-24-edits.json"), encoding="utf-8")) if os.path.exists(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-24-edits.json")) else {}
for k, pairs in EDITS.items():
    for a, b in pairs:
        T[k] = T[k].replace(a, b)

S_HOME = "مغاربة إيطاليا · خبار مفيدة بالدارجة"
S_COLF = "InformazioneFiscale 12/3/2026 · Money.it 13/4/2026 · CGIL Lazio 20/7/2026 · QuiFinanza 8/4/2026"
S_COLF2 = "InformazioneFiscale · CGIL Lazio · Money.it · calcoli nostri"
S_GAS = "Decreto MEF 9/11/2026 · Il Giorno/QN 24/11 (MIMIT) · LaC News24 23/11 · calcoli nostri"
S_BON = "InformazioneFiscale 31/3 · OK!Mugello 23/10 · INPS · QuiFinanza · AGI 20/10 · LentePubblica"
S_DIC = "InformazioneFiscale 12/11 · Centro Fiscale 18/11 · Camera dei deputati · SicurAUTO 10/11 · SmartWorld"
S_CASE = "Money.it 2/6/2026 · Centro Fiscale 16/11 · INPS msg 3691/2026 · EC News · calcoli nostri"
S_MAR = "Min. Finanze Marocco 14/11 · Le360 17/11 · La Vie Eco 17/11 · L'ODJ · H24info · Le Matin · FNH 9/11"
S_QA = "Fonti dei capitoli 01-07"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850); FULL = (160, 300, 1760, 860)
WIDE = (260, 220, 1660, 830); ICO = (160, 330, 1760, 860); BAR = (160, 300, 1760, 840)
MED = dict(view="med", hl=["ITA", "MAR"], labels=False)
BIGMAP = (160, 200, 1760, 880)

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="00 · أخبار السيمانة", src=S_HOME, items=[
   dict(k="head", text="نشرة السيمانة", at=0.2, until="شنو كاين فهاد النشرة؟", sub="الثلاثاء 24 نونبر 2026"),
   dict(k="people", at=0.6, until="شنو كاين فهاد النشرة؟", box=FULL, people=["hijab", "man", "elder"],
        say=[dict(who=0, text="شنو الجديد هاد السيمانة؟", at=0.8), dict(who=2, text="خبار بالأرقام", at=5.0, bg="green")]),
   dict(k="rows", at="شنو كاين فهاد النشرة؟", until="ومن بعد، مثال عملي", y=280, gap=118, size=48, rows=[
     ("الخدامات فالديور", "1.200 €", "عندنا الخدامات"),
     ("المازوط", "24/11", "عندنا المازوط"),
     ("البونسات قبل آخر العام", "31/12", "عندنا البونسات"),
     ("الفلوس ديال دجنبر", "1/12", "عندنا الفلوس"),
   ]),
   dict(k="map", **MED, route=["Milano", "Casablanca"], at="ومن بعد، مثال عملي", until="قبل ما نبداو، جوج", box=BIGMAP),
   dict(k="icons", at="قبل ما نبداو، جوج", until="يالاه نبداو بالخبر", box=ICO, items=[
     ["file-certificate", "جوج مصادر", "green"], ["alert-triangle", "ماشي استشارة", "gold"], ["users", "سول الباترونا", "blue"]], gap=2.5),
   dict(k="chapter", num="01", title="الخدامات فالديور: 1.200 أورو", at="الخبر الأول: الخدامات", until="هاد الأيام كيدور"),
   dict(k="people", at="هاد الأيام كيدور", until="ولكن كاين حاجة حقيقية", box=FULL, people=["woman", "elder"],
        say=[dict(who=0, text="بونس 1.200 € للعائلة؟", at=0.8), dict(who=1, text="ما لقيناهش فالقانون", at=5.5, bg="red")]),
   dict(k="vs", at="ولكن كاين حاجة حقيقية", until="شكون كياخدها؟", box=WIDE,
        right=dict(title="فالواتساب", value="لا", sub="بونس للعائلة", icon="phone", color="red"),
        left=dict(title="فالضرائب", value="1.200 €", sub="حق ديال الخدامة", icon="receipt-tax", color="green"), gap=3.5),
   dict(k="big", text="100 €", sub="فالشهر، فالفيش ديال الخلاص", at="شكون كياخدها؟", until="ولكن الخدامة فالديور، المعلم"),
   dict(k="people", at="ولكن الخدامة فالديور، المعلم", until="وكيفاش كتطلبها؟", box=FULL, people=["hijab", "office"],
        say=[dict(who=1, text="حنا ما كنحسبوش الضرائب", at=1.0), dict(who=0, text="والفلوس فين مشات؟", at=5.0, bg="gold")]),
   dict(k="steps", at="وكيفاش كتطلبها؟", until="وهنا كاين خبر مهم", box=WIDE, steps=[
     ["730 بلا معلم", "1"], ["ولا التصريح العادي", "2"], ["الفلوس فالإيبان", "3"]], gap=3.0, check_after=99),
   dict(k="calendar", at="وهنا كاين خبر مهم", until="ولكن هادي طريق طويلة", box=R_BOX, day=11, month=3, sub="جواب الوزارة فالبرلمان"),
   dict(k="people", at="وهنا كاين خبر مهم", until="ولكن هادي طريق طويلة", box=L_BOX, people=["clerk"],
        say=[dict(who=0, text="الحق ما كيضيعش", at=2.0, bg="green")]),
   dict(k="warn", text="الطريق طويلة: الأحسن تصرح بنفسك", at="ولكن هادي طريق طويلة", until="وشكون معني بهاد الخبر", y=600),
   dict(k="icons", at="وشكون معني بهاد الخبر", until="فكل هاد الحالات", box=ICO, items=[
     ["heart", "بادانطي", "gold"], ["home", "كولف", "blue"], ["user", "بيبي سيتر", "green"], ["car", "سائق / جردينيي", "blue"]], gap=3.0),
   dict(k="map", view="italy", pins=["Genova", "Milano", "Roma", "Napoli"], labels=False, at="فكل هاد الحالات", box=R_BOX),
   dict(k="people", at="فكل هاد الحالات", box=L_BOX, people=["worker"],
        say=[dict(who=0, text="المعلم هو العائلة", at=1.0, bg="gold")]),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="01 · شكون كياخد 1.200 أورو", src=S_COLF, items=[
   dict(k="head", text="الشروط ديال 1.200 أورو", sub="الدخل ديال العام هو اللي كيحكم", at=0.2, until="إلى كان الدخل ديالك تحت"),
   dict(k="bars", at="إلى كان الدخل ديالك تحت", until="خود مثال من عندنا", box=BAR, bars=[
     ["الدخل حتى 15.000", 1200, "1.200 €", "green"], ["بين 15.000 و28.000", 600, "جزء", "gold"], ["فوق 28.000", 0, "0 €", "red"]]),
   dict(k="map", view="north", pins=["Genova"], labels=False, at="خود مثال من عندنا", until="فعام ألفين وخمسة وعشرين", box=R_BOX),
   dict(k="people", at="خود مثال من عندنا", until="فعام ألفين وخمسة وعشرين", box=L_BOX, people=["hijab"],
        say=[dict(who=0, text="فاطمة: 1.000 € فالشهر", at=1.0)]),
   dict(k="steps", at="فعام ألفين وخمسة وعشرين", until="وإلى خدمات غير ستة", box=WIDE, steps=[
     ["الدخل ديال 2025", "12.000 €"], ["تحت 15.000 أورو", "ok"], ["حتى", "1.200 €"]], gap=3.5, check_after=99),
   dict(k="vs", at="وإلى خدمات غير ستة", until="وإلى كنتي كتخدمي عند جوج", box=WIDE,
        right=dict(title="12 شهر", value="1.200 €", sub="العام كامل", icon="calendar", color="green"),
        left=dict(title="6 شهور", value="600 €", sub="تقريبا", icon="calendar", color="gold"), gap=3.0),
   dict(k="icons", at="وإلى كنتي كتخدمي عند جوج", until="ودابا السؤال: فاطمة", box=ICO, items=[
     ["home", "عائلة 1", "blue"], ["home", "عائلة 2", "blue"], ["calculator", "المجموع ديال العام", "gold"]], gap=2.5),
   dict(k="calendar", at="ودابا السؤال: فاطمة", until="ولكن ما تخلعش", box=R_BOX, day=30, month=9, sub="الأجل ديال 730: فات"),
   dict(k="people", at="ودابا السؤال: فاطمة", until="ولكن ما تخلعش", box=L_BOX, people=["hijab"],
        say=[dict(who=0, text="ما درتش التصريح!", at=1.0, bg="red")]),
   dict(k="steps", at="ولكن ما تخلعش", until="شنو خاصك تجمع من دابا؟", box=WIDE, steps=[
     ["الحق ما ضاعش", "1"], ["الباترونا / الكاف", "2"], ["التصريح فربيع 2027", "3"]], gap=4.0, check_after=0.6),
   dict(k="icons", at="شنو خاصك تجمع من دابا؟", until="والفلوس فوقاش كتوصل؟", box=ICO, items=[
     ["file-text", "ورقة الخلاص", "gold"], ["clipboard-check", "الكونطرا", "blue"], ["building-bank", "الإيبان", "green"], ["key", "السبيد", "blue"]], gap=2.5),
   dict(k="calendar", at="والفلوس فوقاش كتوصل؟", until="وحاجة أخرى مهمة", box=WIDE, day="?", month="آخر العام", sub="ولا الشهور الأولى ديال العام اللي من بعد"),
   dict(k="big", text="حق", sub="ماشي بونس، ماشي صدقة", at="وحاجة أخرى مهمة", until="ومن هنا كتبان قيمة الكونطرا"),
   dict(k="vs", at="ومن هنا كتبان قيمة الكونطرا", until="وزيد: إلى كان شي واحد", box=WIDE,
        right=dict(title="بالكونطرا", value="محمية", sub="بونس، بانسيون، بيرميسو", person="hijab", color="green"),
        left=dict(title="بلا كونطرا", value="صعيب", sub="ما كاين حتى ورقة", person="woman", color="red"), gap=4.0),
   dict(k="people", at="وزيد: إلى كان شي واحد", until="وسؤال كيجينا", box=FULL, people=["man", "girl"],
        say=[dict(who=0, text="عطيني 50 € ونجيب ليك البونس", at=0.8, bg="red"), dict(who=1, text="لا! هادي تقلاب", at=4.5, bg="red")]),
   dict(k="people", at="وسؤال كيجينا", box=FULL, people=["elder", "clerk"],
        say=[dict(who=0, text="العائلة تاخدها فبلاصتي؟", at=0.8), dict(who=1, text="لا، هادي ديال الخدامة", at=4.5, bg="green")]),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="02 · المازوط: الخصم سالا", src=S_GAS, items=[
   dict(k="chapter", num="02", title="المازوط: الخصم سالا", at=0.2, until="الحكومة كانت دارت خصم"),
   dict(k="big", text="4,88", sub="سانتيم فاللتر: الخصم اللي مشا", at="الحكومة كانت دارت خصم", until="واليوم، أربعة وعشرين"),
   dict(k="calendar", at="واليوم، أربعة وعشرين", until="جمعية ديال المستهلكين", box=R_BOX, day=24, month=11, sub="أول نهار بلا خصم"),
   dict(k="people", at="واليوم، أربعة وعشرين", until="جمعية ديال المستهلكين", box=L_BOX, people=["worker"],
        say=[dict(who=0, text="واش تمد؟ لا", at=2.0, bg="gold")]),
   dict(k="text", text="جمعية المستهلكين: طلب، ماشي قرار", at="جمعية ديال المستهلكين", until="والأكسيز هي ضريبة", y=600, size=50),
   dict(k="icons", at="والأكسيز هي ضريبة", until="إذن الأكسيز رجعات", box=ICO, items=[
     ["gas-station", "كل لتر", "blue"], ["receipt-tax", "ضريبة", "gold"], ["building-bank", "الدولة", "grey"]], gap=2.0),
   dict(k="vs", at="إذن الأكسيز رجعات", until="وشحال الثمن دابا", box=WIDE,
        right=dict(title="حتى 23/11", value="632,90", sub="الأكسيز على 1000 لتر", icon="gas-station", color="green"),
        left=dict(title="من 24/11", value="672,90", sub="الأكسيز على 1000 لتر", icon="gas-station", color="red"), gap=3.0),
   dict(k="bars", at="وشحال الثمن دابا", until="ولكن إلى رجع الثمن", box=BAR, bars=[
     ["الليصانص", 1.941, "1,941 €", "gold"], ["المازوط", 2.197, "2,197 €", "red"]]),
   dict(k="text", text="الثمن المتوسط فالسيلف، 23/11 (الوزارة)", at="وشحال الثمن دابا", until="ولكن إلى رجع الثمن", y=900, size=40),
   dict(k="big", text="≈ 5", sub="سانتيم فاللتر: الزيادة الممكنة", at="ولكن إلى رجع الثمن", until="شحال كيعني هادشي فالجيب؟"),
   dict(k="map", view="north", pins=["Bergamo"], labels=False, at="شحال كيعني هادشي فالجيب؟", until="الخمسين لتر فيهم", box=R_BOX),
   dict(k="people", at="شحال كيعني هادشي فالجيب؟", until="الخمسين لتر فيهم", box=L_BOX, people=["man"],
        say=[dict(who=0, text="يوسف: 50 لتر ديال المازوط", at=2.0)]),
   dict(k="steps", at="الخمسين لتر فيهم", until="ماشي بزاف، ولكن", box=WIDE, steps=[
     ["50 لتر", "2,44 €"], ["2 مرات فالسيمانة", "4,88 €"], ["فالشهر", "≈ 21 €"]], gap=3.0, check_after=99),
   dict(k="icons", at="ماشي بزاف، ولكن", until="ومثال تاني: خديجة", box=ICO, items=[
     ["home", "الكرا", "blue"], ["bolt", "الضو", "gold"], ["flame", "الشوفاج", "red"]], gap=1.5),
   dict(k="vs", at="ومثال تاني: خديجة", until="واللي كيخدم فالبني", box=WIDE,
        right=dict(title="يوسف: المازوط", value="+21 €", sub="فالشهر تقريبا", person="man", color="red"),
        left=dict(title="خديجة: الليصانص", value="0 €", sub="ما تبدل والو", person="hijab", color="green"), gap=3.0),
   dict(k="people", at="واللي كيخدم فالبني", until="شنو تقدر دير؟", box=FULL, people=["worker", "farmer"],
        say=[dict(who=0, text="كل نهار 80 كيلومتر", at=0.8), dict(who=1, text="حتى أنا", at=4.0)]),
   dict(k="icons", at="شنو تقدر دير؟", until="وإلى كنتي ناوي تهبط", box=ICO, items=[
     ["world", "قارن البومبات", "blue"], ["gas-station", "السيلف أرخص", "green"], ["truck", "الكاميو: المحاسب", "gold"]], gap=5.0),
   dict(k="map", **MED, route=["Genova", "Tanger", "ship"], at="وإلى كنتي ناوي تهبط", until="وما تنساش: الثمن", box=BIGMAP),
   dict(k="vs", at="وما تنساش: الثمن", until="وسؤال كيجينا بزاف", box=WIDE,
        right=dict(title="فالمدينة", value="2,197 €", sub="المازوط فالسيلف", icon="home", color="green"),
        left=dict(title="الأوطوسترادا", value="2,254 €", sub="المازوط فالسيلف", icon="car", color="red"), gap=3.0),
   dict(k="people", at="وسؤال كيجينا بزاف", box=FULL, people=["elder", "clerk"],
        say=[dict(who=0, text="الخصم غادي يرجع؟", at=0.6), dict(who=1, text="ما كنعرفوش", at=3.5, bg="gold")]),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="03 · البونسات قبل آخر العام", src=S_BON, items=[
   dict(k="chapter", num="03", title="البونسات قبل آخر العام", at=0.2, until="إذن خلينا نديرو اللائحة"),
   dict(k="warn", text="فاتك الأجل، فاتتك الفلوس", at="إلى فاتك الأجل", until="إذن خلينا نديرو اللائحة", y=600),
   dict(k="calendar", at="الأول: البونس ديال الكريش", until="شحال؟ إلى تزاد الولد", box=R_BOX, day=31, month=12, sub="آخر أجل: الكريش"),
   dict(k="people", at="الأول: البونس ديال الكريش", until="شحال؟ إلى تزاد الولد", box=L_BOX, people=["woman", "child"],
        say=[dict(who=0, text="طلبت البونس ديال الكريش؟", at=1.0)]),
   dict(k="bars", at="شحال؟ إلى تزاد الولد", until="والفلوس كتجي على حداش", box=BAR, bars=[
     ["قبل 2024: تحت 25.000", 3000, "3.000 €", "green"], ["قبل 2024: حتى 40.000", 2500, "2.500 €", "gold"], ["من 2024: تحت 40.000", 3600, "3.600 €", "green"], ["بلا إيزي", 1500, "1.500 €", "grey"]]),
   dict(k="icons", at="والفلوس كتجي على حداش", until="مثال: نادية فبولونيا", box=ICO, items=[
     ["calendar", "11 شهر", "blue"], ["receipt", "الوصولات", "gold"], ["calculator", "الإيزي ديال الولاد", "green"]], gap=3.0),
   dict(k="map", view="north", pins=["Bologna"], labels=False, at="مثال: نادية فبولونيا", until="يعني تقدر تاخد حتى لتلات مية", box=R_BOX),
   dict(k="big", text="327 €", sub="فالشهر، حتى 11 شهر", at="يعني تقدر تاخد حتى لتلات مية", until="التاني: الكارطا", t=0),
   dict(k="big", text="500 €", sub="كارطا ديديكاطا آ تي", at="التاني: الكارطا", until="من اليوم حتى لستاش"),
   dict(k="calendar", at="من اليوم حتى لستاش", until="وشكون عندو هاد الكارطا؟", box=WIDE, day=16, month=12, sub="خلص شي حاجة قبل: باقي 22 يوم"),
   dict(k="icons", at="وشكون عندو هاد الكارطا؟", until="التالت: البونس ديال الماماوات", box=ICO, items=[
     ["calculator", "الإيزي تحت 15.000", "green"], ["map-pin", "الكومون كيختار", "blue"], ["mailbox", "البوسطا", "gold"], ["shopping-cart", "غير الماكلة", "green"]], gap=2.5),
   dict(k="vs", at="التالت: البونس ديال الماماوات", until="مثال: ماما خدامة", box=WIDE,
        right=dict(title="فالشهر", value="60 €", sub="بونس الماماوات", icon="heart", color="green"),
        left=dict(title="الطلب قبل", value="31/12", sub="باقي 37 يوم", icon="calendar", color="gold"), gap=3.0),
   dict(k="steps", at="مثال: ماما خدامة", until="ولكن رد البال: الخدامات", box=WIDE, steps=[
     ["الولد التاني: ماي", "1"], ["8 شهور", "× 60 €"], ["المجموع", "480 €"]], gap=3.0, check_after=99),
   dict(k="people", at="ولكن رد البال: الخدامات", until="الرابع: البونس ديال الولادة", box=FULL, people=["hijab", "clerk"],
        say=[dict(who=0, text="وأنا بادانطي؟", at=0.6), dict(who=1, text="لا، الخدامات فالديور لا", at=3.0, bg="red")]),
   dict(k="big", text="1.000 €", sub="على كل ولد تزاد فـ2026", at="الرابع: البونس ديال الولادة", until="مثلا، إلى تزاد الولد فعشرة"),
   dict(k="steps", at="مثلا، إلى تزاد الولد فعشرة", until="الخامس، والمهم بزاف", box=WIDE, steps=[
     ["الزيادة", "10/9"], ["+ 120 يوم", "="], ["آخر أجل", "8/1"]], gap=2.5, check_after=99),
   dict(k="calendar", at="الخامس، والمهم بزاف", until="وعلاش هادا مهم؟", box=R_BOX, day=31, month=12, sub="الإيزي كيسالي"),
   dict(k="map", view="italy", pins=["Torino", "Bologna", "Napoli"], labels=False, at="الخامس، والمهم بزاف", until="وعلاش هادا مهم؟", box=L_BOX),
   dict(k="steps", at="وعلاش هادا مهم؟", until="وسؤال من عندكم", box=WIDE, steps=[
     ["الديسو", "يناير"], ["قبل آخر فبراير", "ok"], ["الأسينيو كامل", "مارس"]], gap=3.0, check_after=99),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Nador"], labels=False, at="وسؤال من عندكم", until="نعم، الدار ولا الجزء", box=BIGMAP),
   dict(k="icons", at="نعم، الدار ولا الجزء", box=ICO, items=[
     ["home", "الدار", "gold"], ["building-bank", "الكونطو", "gold"]], gap=3.0),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="04 · الفلوس ديال دجنبر", src=S_DIC, items=[
   dict(k="chapter", num="04", title="دجنبر: البانسيون والمشاريع", at=0.2, until="البانسيون ديال دجنبر كتخلص"),
   dict(k="calendar", at="البانسيون ديال دجنبر كتخلص", until="ومعاها كاينة التريديشيما", box=R_BOX, day=1, month=12, sub="البانسيون + التريديشيما"),
   dict(k="map", view="italy", pins=["Torino", "Roma", "Palermo"], labels=False, at="البانسيون ديال دجنبر كتخلص", until="ومعاها كاينة التريديشيما", box=L_BOX),
   dict(k="vs", at="ومعاها كاينة التريديشيما", until="واللي عندهم بانسيون صغيرة", box=WIDE,
        right=dict(title="طول العام", value="12/12", sub="شهر كامل تقريبا", icon="calendar", color="green"),
        left=dict(title="من يوليوز", value="6/12", sub="النص تقريبا", icon="calendar", color="gold"), gap=5.0),
   dict(k="big", text="154,94 €", sub="الزيادة: الحد الأقصى، بلا طلب", at="واللي عندهم بانسيون صغيرة", until="ولكن ماشي كلشي كياخدها"),
   dict(k="people", at="ولكن ماشي كلشي كياخدها", until="من بعد، الأسينيو أونيكو", box=FULL, people=["elder", "clerk"],
        say=[dict(who=0, text="عندي الأسينيو سوسيالي", at=0.6), dict(who=1, text="هادي ما فيهاش الزيادة", at=3.0, bg="gold")]),
   dict(k="calendar", at="من بعد، الأسينيو أونيكو", until="والمبلغ ديال الأسينيو", box=R_BOX, day=16, month=12, sub="16 ولا 17 دجنبر"),
   dict(k="people", at="واللي قدمو طلب جديد", until="والمبلغ ديال الأسينيو", box=L_BOX, people=["hijab"],
        say=[dict(who=0, text="طلب جديد: آخر الشهر", at=1.0, bg="gold")]),
   dict(k="text", text="الأسينيو كيتحسب بالإيزي", at="والمبلغ ديال الأسينيو", until="ودابا الميزانية ديال", y=600, size=54),
      dict(k="chapter", num="05", title="المشاريع: الميزانية، الجنسية، الكود", at="ودابا الميزانية ديال", until="البرلمانيين قدمو"),
   dict(k="big", text="6.600", sub="تعديل تقريبا", at="البرلمانيين قدمو", until="القانون خاصو يتصادق"),
   dict(k="warn", text="باقي مشروع، ماشي قانون", at="القانون خاصو يتصادق", until="ودابا الجنسية", y=600),
   dict(k="steps", at="ودابا الجنسية", until="شنو فيه؟ كيبغي", box=WIDE, steps=[
     ["مجلس النواب", "دابا"], ["تصويت نهائي", "؟"], ["مجلس الشيوخ", "؟"]], gap=3.0, check_after=99),
   dict(k="icons", at="شنو فيه؟ كيبغي", until="إذن اليوم، القواعد", box=ICO, items=[
     ["certificate", "B1 حتى مع الكارطا", "gold"], ["scale", "أسباب جديدة للرفض", "red"], ["heart", "اليمين بالطاليانية", "blue"]], gap=3.5),
   dict(k="people", at="إذن اليوم، القواعد", until="وإلى ما عندكش الكارطا", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="فالواتساب قالو تصادق!", at=3.0, bg="red"), dict(who=1, text="شوف الجريدة الرسمية", at=7.0, bg="green")]),
   dict(k="calendar", at="ودابا الكود ديال الطريق", until="من بعد مجلس الدولة", box=R_BOX, day=25, month=11, sub="الوراق لمجلس الدولة"),
   dict(k="people", at="ودابا الكود ديال الطريق", until="من بعد مجلس الدولة", box=L_BOX, people=["worker"],
        say=[dict(who=0, text="الكود الجديد بدا؟", at=1.0)]),
   dict(k="steps", at="من بعد مجلس الدولة", until="مثلا، المشروع كيقترح", box=WIDE, steps=[
     ["الحكومة", "25/11"], ["مجلس الدولة", "؟"], ["البرلمان", "12/1"]], gap=3.0, check_after=99),
   dict(k="vs", at="مثلا، المشروع كيقترح", until="والبيرمي المغربي؟", box=WIDE,
        right=dict(title="اليوم", value="50", sub="من بعد: كل 5 سنين", icon="id", color="grey"),
        left=dict(title="الاقتراح", value="65", sub="كل 10 سنين: مشروع", icon="clock", color="gold"), gap=3.5),
   dict(k="map", **MED, route=["Casablanca", "Torino"], at="والبيرمي المغربي؟", box=BIGMAP),
 ]),
 dict(audio="F.wav", text=T["F"], chapter="06 · مثال: عائلة وبادانطي", src=S_CASE, items=[
   dict(k="chapter", num="06", title="مثال عملي: العائلة والبادانطي", at=0.2, until="عائلة إيطالية فجنوة"),
   dict(k="map", view="north", pins=["Genova"], labels=False, at="عائلة إيطالية فجنوة", until="شنو خاص هاد العائلة", box=R_BOX),
   dict(k="people", at="خدمو فاطمة", until="شنو خاص هاد العائلة", box=L_BOX, people=["elder", "hijab"],
        say=[dict(who=1, text="فاطمة: بادانطي بالكونطرا", at=0.8, bg="green")]),
   dict(k="vs", at="شنو خاص هاد العائلة", until="نبداو بالعائلة", box=WIDE,
        right=dict(title="العائلة", value="المعلم", sub="الكوتيزاسيون والخصومات", person="office", color="blue"),
        left=dict(title="فاطمة", value="الخدامة", sub="الحقوق ديالها", person="hijab", color="green"), gap=2.0),
   dict(k="calendar", at="أولا، الكوتيزاسيون", until="والإينبس ما بقاتش", box=WIDE, day=10, month=1, sub="الكوتيزاسيون ديال آخر التريمستر"),
   dict(k="icons", at="والإينبس ما بقاتش", until="وعلاش هادا مهم حتى لفاطمة؟", box=ICO, items=[
     ["mailbox", "ما كاينش فالبوسطا", "red"], ["world", "الورقة فالسيت", "green"], ["alert-triangle", "الروطار: عقوبات", "gold"]], gap=3.0),
   dict(k="icons", at="وعلاش هادا مهم حتى لفاطمة؟", until="تانيا، العائلة تقدر", box=ICO, items=[
     ["wallet", "البانسيون", "green"], ["briefcase", "النازبي", "blue"], ["id", "البيرميسو", "gold"]], gap=2.0),
   dict(k="big", text="1.549,37 €", sub="الكوتيزاسيون: كتنقص من الدخل ديال العائلة", at="تانيا، العائلة تقدر", until="تالتا، إلى كان الشخص"),
   dict(k="steps", at="تالتا، إلى كان الشخص", until="ولكن الخلاص خاصو يكون", box=WIDE, steps=[
     ["ماشي قادر يعيش بوحدو", "1"], ["الدخل تحت 40.000 أورو", "2"], ["19% من 2.100 €", "399 €"]], gap=4.0, check_after=99),
   dict(k="vs", at="ولكن الخلاص خاصو يكون", until="ورابعا، العائلة خاصها", box=WIDE,
        right=dict(title="البانكا / الكارطا", value="ok", sub="كاين الخصم", icon="credit-card", color="green"),
        left=dict(title="الكاش", value="لا", sub="ما كاينش الخصم", icon="cash", color="red"), gap=2.5),
   dict(k="people", at="ورابعا، العائلة خاصها", until="ودابا فاطمة.", box=FULL, people=["office", "clerk"],
        say=[dict(who=1, text="صرحو بالكونطرا قبل الخدمة", at=1.0, bg="gold")]),
   dict(k="icons", at="ودابا فاطمة.", until="رابعا، البيرميسو ديالها", box=ICO, items=[
     ["receipt-tax", "التصريح: 1.200 أورو", "green"], ["x", "بونس الماماوات: لا", "red"], ["calculator", "الإيزي فيناير", "blue"]], gap=6.0),
   dict(k="steps", at="رابعا، البيرميسو ديالها", until="والوراق ديال الخدمة مهمين", box=WIDE, steps=[
     ["البيرميسو كيسالي", "15/3/2027"], ["- 90 يوم", "="], ["آخر أجل", "15/12/2026"]], gap=3.0, check_after=99),
   dict(k="icons", at="والوراق ديال الخدمة مهمين", until="إذن نصيحة لفاطمة", box=ICO, items=[
     ["clipboard-check", "الكونطرا", "blue"], ["receipt", "ورقة الخلاص", "gold"], ["file-certificate", "الكوتيزاسيون", "green"]], gap=2.0),
   dict(k="people", at="إذن نصيحة لفاطمة", until="وحتى العائلة، إلى ما فهماتش", box=FULL, people=["hijab", "girl"],
        say=[dict(who=0, text="كل 3 شهور كنشوف السيت", at=1.0, bg="green")]),
   dict(k="map", view="italy", pins=["Genova", "Roma", "Bari"], labels=False, at="وحتى العائلة، إلى ما فهماتش", until="شنو هي الأخطاء", box=R_BOX),
   dict(k="people", at="وحتى العائلة، إلى ما فهماتش", until="شنو هي الأخطاء", box=L_BOX, people=["office"],
        say=[dict(who=0, text="كلشي مكتوب", at=2.0, bg="green")]),
   dict(k="steps", at="شنو هي الأخطاء", until="وسؤال من عندكم", box=WIDE, steps=[
     ["خدمة بلا كونطرا", "1"], ["كاش بلا ورقة", "2"], ["ما كتشوفش الكوتيزاسيون", "3"], ["بونس ما كاينش", "4"]], gap=2.5, check_after=0.4, bad=True),
   dict(k="people", at="وسؤال من عندكم", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="الكوتيزاسيون كاملين عليا؟", at=0.6), dict(who=1, text="لا، الجزء الكبير على العائلة", at=4.5, bg="green")]),
 ]),
 dict(audio="G.wav", text=T["G"], chapter="07 · من المغرب", src=S_MAR, items=[
   dict(k="chapter", num="07", title="من المغرب: الميزانية والجالية", at=0.2, until="مجلس النواب صادق"),
   dict(k="steps", at="مجلس النواب صادق", until="شنو فيه اللي يقدر", box=WIDE, steps=[
     ["مجلس النواب", "14/11"], ["مجلس المستشارين", "17/11"], ["القراءة التانية", "؟"]], gap=3.0, check_after=99),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Rabat"], labels=False, at="شنو فيه اللي يقدر", until="العتبة ديال الكرا", box=BIGMAP),
   dict(k="bars", at="العتبة ديال الكرا", until="مثال: إلى عندك دار فطنجة", box=BAR, bars=[
     ["العتبة دابا", 40000, "40.000 DH", "grey"], ["العتبة فالمشروع", 60000, "60.000 DH", "gold"]]),
   dict(k="map", **MED, route=["Milano", "Tanger"], at="مثال: إلى عندك دار فطنجة", until="ولكن هادا ما كيعنيش", box=BIGMAP),
   dict(k="steps", at="ولكن هادا ما كيعنيش", until="وحتى لدابا، ما لقينا", box=WIDE, steps=[
     ["4.000 DH × 12", "48.000 DH"], ["تحت 60.000 DH", "المشروع"], ["الضريبة", "سول المحاسب"]], gap=3.0, check_after=99),
   dict(k="warn", text="ما كاين حتى إجراء خاص بالمغاربة اللي برا", at="وحتى لدابا، ما لقينا", until="وفالمشروع حتى حوايج", y=600),
   dict(k="icons", at="وفالمشروع حتى حوايج", until="ولكن هادشي كامل باقي", box=ICO, items=[
     ["briefcase", "أوطو أونطروبرونور", "blue"], ["trending-up", "العتبة: 100.000 DH", "green"], ["trending-down", "الضريبة: من 30 لـ20", "gold"]], gap=3.5),
   dict(k="people", at="ولكن هادشي كامل باقي", until="الخبر التاني: الفلوس", box=FULL, people=["man", "elder"],
        say=[dict(who=0, text="تصادق؟", at=0.6), dict(who=1, text="باقي القراءة التانية", at=2.5, bg="gold")]),
   dict(k="big", text="103", sub="مليار درهم حتى لآخر شتنبر 2026", at="الخبر التاني: الفلوس", until="هادا كيبين شحال"),
   dict(k="map", **MED, route=["Bologna", "Casablanca"], at="هادا كيبين شحال", until="الخبر التالت: الفيش", box=BIGMAP),
   dict(k="steps", at="الخبر التالت: الفيش", until="وهادي كتنفع إلى خاصك", box=WIDE, steps=[
     ["الطلب أونلاين", "1"], ["الخلاص أونلاين", "2"], ["القنصلية", "3"]], gap=3.0, check_after=0.6),
   dict(k="people", at="وهادي كتنفع إلى خاصك", until="ودابا، حيت العطلة", box=FULL, people=["clerk", "hijab"],
        say=[dict(who=0, text="ورقة ما فاتتش 6 شهور", at=3.0, bg="gold"), dict(who=1, text="وواش خاصها ترجمة؟", at=6.0)]),
   dict(k="map", **MED, route=["Milano", "Casablanca"], at="ودابا، حيت العطلة", until="تانيا، إلى هبطتي", box=BIGMAP),
   dict(k="icons", at="تانيا، إلى هبطتي", until="وسؤال: واش الدار", box=ICO, items=[
     ["plane", "طيارة مباشرة", "blue"], ["car", "180 يوم", "gold"], ["luggage", "الكولي: مصاريف", "red"]], gap=2.5),
   dict(k="people", at="وسؤال: واش الدار", until="وإلى عندك شي وثيقة", box=FULL, people=["man", "office"],
        say=[dict(who=0, text="الضريبة فإيطاليا؟", at=0.6), dict(who=1, text="سول المحاسب", at=3.0, bg="gold")]),
   dict(k="icons", at="وإلى عندك شي وثيقة", box=ICO, items=[
     ["e-passport", "الباسبور", "green"], ["id", "البطاقة الوطنية", "blue"], ["calendar", "الموعد من دابا", "gold"]], gap=2.0),
 ]),
 dict(audio="H.wav", text=T["H"], chapter="08 · سؤال وجواب", src=S_QA, items=[
   dict(k="chapter", num="08", title="سؤال وجواب", at=0.2, until="السؤال الأول"),
   dict(k="people", at="السؤال الأول", until="الخلاص بالكاش ماشي", box=FULL, people=["hijab", "elder"],
        say=[dict(who=0, text="كيخلصوني كاش: عادي؟", at=0.8)]),
   dict(k="vs", at="الخلاص بالكاش ماشي", until="السؤال التاني", box=WIDE,
        right=dict(title="بالبانكا", value="دليل", sub="+ الخصم ديال العائلة", icon="building-bank", color="green"),
        left=dict(title="كاش", value="ورقة", sub="كل شهر، ضروري", icon="cash", color="gold"), gap=3.0),
   dict(k="people", at="السؤال التاني", until="الوزارة قالت بلي", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="عمري ما صرحت: خسرت؟", at=0.8)]),
   dict(k="text", text="الحق ما كيضيعش · الكاف ولا الباترونا", at="الوزارة قالت بلي", until="السؤال التالت", y=600, size=50),
   dict(k="people", at="السؤال التالت", until="السؤال الرابع", box=FULL, people=["girl", "office"],
        say=[dict(who=0, text="الخدامة فالديور: النازبي؟", at=0.6), dict(who=1, text="نعم، مع الكوتيزاسيون", at=3.5, bg="green")]),
   dict(k="people", at="السؤال الرابع", until="وسؤال آخر: عندي البارطيتا", box=FULL, people=["worker", "clerk"],
        say=[dict(who=0, text="المازوط غادي يطلع؟", at=0.6), dict(who=1, text="حتى لـ5 سنتيم تقريبا", at=4.0, bg="gold")]),
   dict(k="calendar", at="وسؤال آخر: عندي البارطيتا", until="السؤال الخامس", box=R_BOX, day=30, month=11, sub="الأكونطو التاني: إف 24"),
   dict(k="people", at="وسؤال آخر: عندي البارطيتا", until="السؤال الخامس", box=L_BOX, people=["man"],
        say=[dict(who=0, text="عندي البارطيتا إيفا", at=0.8)]),
   dict(k="people", at="السؤال الخامس", until="لا، الطلب ديال هاد العام", box=FULL, people=["hijab", "child"],
        say=[dict(who=0, text="الكريش من شتنبر: فاتني؟", at=0.8)]),
   dict(k="calendar", at="لا، الطلب ديال هاد العام", until="السؤال السادس", box=WIDE, day=31, month=12, sub="الكريش: الشهور + الوصولات"),
   dict(k="people", at="السؤال السادس", until="وواش نقدر نعمر", box=FULL, people=["elder", "woman"],
        say=[dict(who=0, text="الكارطا ديال 500 € ما خلصت بيها", at=0.8), dict(who=1, text="قبل 16 دجنبر", at=5.0, bg="gold")]),
   dict(k="vs", at="وواش نقدر نعمر", until="السؤال السابع", box=WIDE,
        right=dict(title="الماكلة", value="ok", sub="الأساسية", icon="shopping-cart", color="green"),
        left=dict(title="المازوط", value="لا", sub="ما كيدخلش", icon="gas-station", color="red"), gap=2.0),
   dict(k="people", at="السؤال السابع", until="القانون الجديد باقي مشروع", box=FULL, people=["worker", "clerk"],
        say=[dict(who=0, text="عندي الكارطا: نستنى؟", at=0.8)]),
   dict(k="text", text="القانون الجديد باقي مشروع · القواعد ديال اليوم", at="القانون الجديد باقي مشروع", until="السؤال التامن", y=600, size=46),
   dict(k="people", at="السؤال التامن", until="لا، الإينبس كيحسبها", box=FULL, people=["girl", "elder"],
        say=[dict(who=0, text="الواليدة خاصها تطلب؟", at=0.8)]),
   dict(k="big", text="154,94 €", sub="الحد الأقصى، بوحدها مع 1 دجنبر", at="لا، الإينبس كيحسبها", until="وسؤال آخر: تزاد ليا"),
   dict(k="steps", at="وسؤال آخر: تزاد ليا", until="وسؤال آخر: عندي دار مكرية", box=WIDE, steps=[
     ["الزيادة", "15/10"], ["+ 120 يوم", "="], ["آخر أجل", "12/2/2027"]], gap=3.0, check_after=99),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Tanger"], labels=False, at="وسؤال آخر: عندي دار مكرية", until="لا، باقي فمجلس المستشارين", box=BIGMAP),
   dict(k="people", at="لا، باقي فمجلس المستشارين", until="السؤال التاسع", box=FULL, people=["man"],
        say=[dict(who=0, text="60.000 DH: قانون؟", at=0.8), ]),
   dict(k="people", at="السؤال التاسع", until="والتسجيل الأول قبل سبعة", box=FULL, people=["office", "man"],
        say=[dict(who=1, text="نجيب خويا يخدم؟", at=0.8), dict(who=0, text="المعلم هو اللي كيطلب", at=4.0, bg="green")]),
   dict(k="calendar", at="والتسجيل الأول قبل سبعة", until="والطلب ما كيتشراش", box=WIDE, day=7, month=12, sub="قبل 20:00"),
   dict(k="map", **MED, route=["Casablanca", "Bergamo"], at="والطلب ما كيتشراش", until="وإلى عندك سؤال آخر", box=BIGMAP),
   dict(k="people", at="وإلى عندك سؤال آخر", box=FULL, people=["girl", "elder", "hijab"],
        say=[dict(who=0, text="كتب سؤالك فالكومونتير", at=0.8, bg="green")]),
 ]),
 dict(audio="I.wav", text=T["I"], chapter="09 · الخلاصة والتواريخ", src=S_HOME, items=[
   dict(k="head", text="الخلاصة", at=0.2, until="واحد: الألف ومية"),
   dict(k="rows", at="واحد: الألف ومية", until="خمسة: الميزانية", y=300, gap=118, size=46, rows=[
     ("الخدامات فالديور: حق فالضرائب", "1.200 €", "واحد: الألف"),
     ("المازوط: الخصم سالا", "23/11", "جوج: الخصم"),
     ("البونسات قبل آخر العام", "31/12", "تلاتة: البونسات"),
     ("البانسيون والتريديشيما", "1/12", "ربعة: البانسيون"),
   ]),
   dict(k="rows", at="خمسة: الميزانية", until="ودابا التواريخ ديال", y=300, gap=118, size=46, rows=[
     ("الميزانية، الجنسية، الكود: مشاريع", "?", "خمسة: الميزانية"),
     ("العائلة والبادانطي: خصومات", "399 €", "ستة: العائلة"),
     ("المغرب: العتبة ديال الكرا", "60.000 DH", "سبعة: فالمغرب"),
   ]),
   dict(k="steps", at="ودابا التواريخ ديال", until="الثلاثاء واحد دجنبر", box=WIDE, steps=[
     ["الكود ديال الطريق", "25/11"], ["البلاك فرايداي", "27/11"], ["الأكونطو التاني", "30/11"]], gap=4.0, check_after=99),
   dict(k="steps", at="الثلاثاء واحد دجنبر", until="واحد وتلاتين دجنبر، البونس", box=WIDE, steps=[
     ["البانسيون", "1/12"], ["الديكري فلوسي", "7/12"], ["الكارطا + الأسينيو", "16/12"]], gap=4.0, check_after=99),
   dict(k="steps", at="واحد وتلاتين دجنبر، البونس", until="وإلى فاتك شي فيديو", box=WIDE, steps=[
     ["الماماوات + الكريش + الإيزي", "31/12"], ["الكوتيزاسيون ديال الديور", "10/1"]], gap=4.0, check_after=99),
   dict(k="icons", at="وإلى فاتك شي فيديو", until="وإلى كنتي كتسنى شي خبر", box=ICO, items=[
     ["heart", "الجنسية", "gold"], ["car", "تبديل البيرمي", "blue"], ["id", "البيرميسو", "gold"], ["plane", "الفيزا", "green"]], gap=2.0),
   dict(k="map", view="italy", hl=["Lazio"], pins=["Roma"], labels=False, at="وإلى كنتي كتسنى شي خبر", until="ونعاودو نقولو", box=R_BOX),
   dict(k="people", at="وإلى كنتي كتسنى شي خبر", until="ونعاودو نقولو", box=L_BOX, people=["clerk"],
        say=[dict(who=0, text="سيمانة بسيمانة", at=1.0, bg="green")]),
   dict(k="people", at="ونعاودو نقولو", until="وتذكير صغير", box=FULL, people=["clerk", "woman"],
        say=[dict(who=0, text="سول الباترونا ولا الكاف", at=1.0, bg="green")]),
   dict(k="people", at="وتذكير صغير", until="وحاجة أخيرة", box=FULL, people=["hijab", "elder"],
        say=[dict(who=0, text="صيفطيه لصاحبتك", at=1.0, bg="green"), dict(who=1, text="الكوتيزاسيون فالوقت", at=8.0, bg="gold")]),
   dict(k="warn", text="ما تعطيش السبيد ديالك لحتى واحد", at="وحاجة أخيرة", until="وإلى عجبك هاد الفيديو", y=640),
   dict(k="cta", at="وإلى عجبك هاد الفيديو", until="وكتب لينا فالكومونتير", text="ابوني فالقناة", sub="وفعل الجرس"),
   dict(k="people", at="وكتب لينا فالكومونتير", box=FULL, people=["girl", "worker", "hijab"],
        say=[dict(who=1, text="شنو فادك أكثر؟", at=0.8), dict(who=2, text="صيفطو لشي واحد", at=6.0, bg="green")]),
 ]),
]

THUMB = dict(
  title=[("خدامة فالديور؟", (236, 196, 96)), "1.200 أورو ديال الضرائب: حق ديالك", "وخصم المازوط سالا"],
  num="1.200 €", numsub="ماشي بونس للعائلة",
  bottom="مغاربة إيطاليا · خبار مفيدة بالدارجة",
)
