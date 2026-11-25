import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-25.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo1-2026-11-25-final")
BRAND = "مغاربة إيطاليا"
T = {k: v.replace("گ", "ك") for k, v in JOB["blocks"].items()}
EP_EDITS = os.path.join(ROOT, "tts/jobs/lungo1-2026-11-25-edits.json")
EDITS = json.load(open(EP_EDITS, encoding="utf-8")) if os.path.exists(EP_EDITS) else {}
for k, pairs in EDITS.items():
    for a, b in pairs:
        T[k] = T[k].replace(a, b)

S_HOME = "مغاربة إيطاليا · خبار مفيدة بالدارجة"
S_PERM = "MAP 24/11 · Le Matin 24/11 · Yabiladi · InfoMagazine 24/11 · Medias24"
S_CASA = "Ddl Bilancio 2027 art. 4 · FiscoeTasse 4/11 · Ediltecnico 9/11 · InformazioneFiscale · Affaritaliani"
S_GAS = "ANSA 24/11 (MIMIT) · Money.it 24/11 · Stato Quotidiano 24/11 · QuiFinanza · calcoli nostri"
S_DIC = "Ticonsiglio 13/11 · InformazioneFiscale · LentePubblica · Fiscal Focus · National Daily Press 24/11"
S_LEG = "Camera dei deputati · Forum Terzo Settore 16/11 · SicurAUTO 10/11 · BusinessOnline 14/11 · Automoto 15/11"
S_CASE = "FiscoeTasse · Ediltecnico · Affaritaliani · QuiFinanza · calcoli nostri"
S_MAR = "MAP · Le Matin · DGSN · Hespress · Bladi · Le Matin 14/11 · FNH · H24info"
S_QA = "Fonti dei capitoli 01-07"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850); FULL = (160, 300, 1760, 860)
WIDE = (260, 220, 1660, 830); ICO = (160, 330, 1760, 860); BAR = (160, 300, 1760, 840)
MED = dict(view="med", hl=["ITA", "MAR"], labels=False)
BIGMAP = (160, 200, 1760, 880)

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="00 · أخبار السيمانة", src=S_HOME, items=[
   dict(k="head", text="نشرة السيمانة", at=0.2, until="شنو كاين فهاد النشرة؟", sub="الأربعاء 25 نونبر 2026"),
   dict(k="people", at=0.6, until="شنو كاين فهاد النشرة؟", box=FULL, people=["hijab", "man", "elder"],
        say=[dict(who=0, text="شنو الجديد هاد السيمانة؟", at=0.8), dict(who=2, text="خبار بالأرقام", at=5.0, bg="green")]),
   dict(k="rows", at="شنو كاين فهاد النشرة؟", until="ومن بعد، مثال عملي", y=280, gap=118, size=48, rows=[
     ("البيرمي المغربي من التيليفون", "E-ROKHSATI", "عندنا البيرمي المغربي"),
     ("البونس ديال الدار", "2027", "عندنا البونس ديال الدار"),
     ("المازوط بلا خصم", "24/11", "عندنا المازوط"),
     ("الفلوس ديال دجنبر", "1/12", "وعندنا الفلوس ديال دجنبر"),
   ]),
   dict(k="map", **MED, route=["Milano", "Casablanca"], at="ومن بعد، مثال عملي", until="قبل ما نبداو، جوج", box=BIGMAP),
   dict(k="icons", at="قبل ما نبداو، جوج", until="يالاه نبداو.", box=ICO, items=[
     ["file-certificate", "جوج مصادر", "green"], ["alert-triangle", "ماشي استشارة", "gold"], ["users", "سول الباترونا", "blue"]], gap=2.5),
   dict(k="chapter", num="01", title="البيرمي المغربي من التيليفون", at="الخبر الأول: البيرمي المغربي", until="نهار الثلاثاء أربعة وعشرين"),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Rabat"], labels=False, at="نهار الثلاثاء أربعة وعشرين", until="شنو كدير هاد المنصة؟", box=BIGMAP),
   dict(k="text", text="E-ROKHSATI · NARSA · 24/11/2026", at="نهار الثلاثاء أربعة وعشرين", until="شنو كدير هاد المنصة؟", y=880, size=42),
   dict(k="icons", at="شنو كدير هاد المنصة؟", until="والمنصة خدامة النهار", box=ICO, items=[
     ["license", "التجديد", "green"], ["id", "نسخة جديدة", "gold"], ["file-text", "ورقة المعلومات", "blue"]], gap=4.0),
   dict(k="big", text="24/7", sub="النهار والليل، كل السيمانة", at="والمنصة خدامة النهار", until="كيفاش كتدخل؟"),
   dict(k="steps", at="كيفاش كتدخل؟", until="وهادي ماشي أول خطوة", box=WIDE, steps=[
     ["الهوية الرقمية", "1"], ["المعلومات ديال البيرمي", "2"], ["الخلاص", "3"], ["الوصل والتتبع", "4"]], gap=4.0, check_after=99),
   dict(k="calendar", at="وهادي ماشي أول خطوة", until="وعلاش هاد الخبر كيهم", box=R_BOX, day=9, month=11, sub="ورقة السوابق أونلاين"),
   dict(k="people", at="وهادي ماشي أول خطوة", until="وعلاش هاد الخبر كيهم", box=L_BOX, people=["clerk"],
        say=[dict(who=0, text="الإدارة ولات رقمية", at=1.5, bg="green")]),
   dict(k="map", **MED, route=["Casablanca", "Milano"], at="وعلاش هاد الخبر كيهم", until="ولكن رد البال لتلاتة", box=BIGMAP),
   dict(k="people", at="ولكن رد البال لتلاتة", until="وتذكير مهم: البيرمي", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="شحال الثمن؟ وشحال المدة؟", at=0.8), dict(who=1, text="ما تقالوش فالمصادر", at=5.0, bg="gold")]),
   dict(k="vs", at="وتذكير مهم: البيرمي", box=WIDE,
        right=dict(title="فإيطاليا", value="12", sub="شهر من الريزيدينسا", icon="license", color="gold"),
        left=dict(title="من بعد", value="تبديل", sub="ولا الامتحان", icon="car", color="red"), gap=4.0),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="02 · البونس ديال الدار", src=S_CASA, items=[
   dict(k="chapter", num="02", title="البونس ديال الدار", at=0.2, until="إلى عندك دار فإيطاليا"),
   dict(k="people", at="إلى عندك دار فإيطاليا", until="نبداو بالقانون ديال دابا", box=FULL, people=["man", "woman"],
        say=[dict(who=0, text="باغي نصلح الكوزينة", at=0.8), dict(who=1, text="واش كاين بونس؟", at=4.0, bg="gold")]),
   dict(k="bars", at="نبداو بالقانون ديال دابا", until="والسقف ديال المصاريف", box=BAR, bars=[
     ["السكنى الرئيسية", 50, "50%", "green"], ["دار أخرى", 36, "36%", "gold"]]),
   dict(k="text", text="القانون ديال 2026", at="نبداو بالقانون ديال دابا", until="والسقف ديال المصاريف", y=880, size=42),
   dict(k="big", text="96.000 €", sub="السقف ديال المصاريف لكل دار", at="والسقف ديال المصاريف", until="والخصم ما كيجيكش"),
   dict(k="big", text="10", sub="سنين: جزء كل عام فالتصريح", at="والخصم ما كيجيكش", until="ودابا الجديد."),
   dict(k="calendar", at="ودابا الجديد.", until="وبلا هاد المشروع", box=R_BOX, day=28, month=10, sub="مجلس الوزراء: المشروع"),
   dict(k="map", view="italy", hl=["Lazio"], pins=["Roma"], labels=False, at="ودابا الجديد.", until="وبلا هاد المشروع", box=L_BOX),
   dict(k="vs", at="وبلا هاد المشروع", until="ولكن رد البال: هادا باقي", box=WIDE,
        right=dict(title="بالمشروع", value="50 / 36", sub="فالمية، فـ2027", icon="home", color="green"),
        left=dict(title="بلا المشروع", value="36 / 30", sub="فالمية", icon="home", color="red"), gap=3.0),
   dict(k="warn", text="مشروع، ماشي قانون: يقدر يتبدل", at="ولكن رد البال: هادا باقي", until="وشنو ما كاينش فالمشروع؟", y=600),
   dict(k="people", at="وشنو ما كاينش فالمشروع؟", until="وفالمشروع، السقف ديال الأشغال", box=FULL, people=["elder", "clerk"],
        say=[dict(who=0, text="والإيكوبونوس؟", at=0.8), dict(who=1, text="ما كاينش فالنص", at=4.0, bg="red")]),
   dict(k="icons", at="وفالمشروع، السقف ديال الأشغال", until="وكاين حتى البونس ديال الموبيليا", box=ICO, items=[
     ["bolt", "الطاقة", "gold"], ["home", "سقف واحد", "blue"], ["flame", "الشوديار", "red"]], gap=2.5),
   dict(k="steps", at="وكاين حتى البونس ديال الموبيليا", until="شكون كيستافد؟", box=WIDE, steps=[
     ["الموبيليا", "50%"], ["السقف", "5.000 €"], ["فالعام", "250 €"]], gap=4.0, check_after=99),
   dict(k="people", at="شكون كيستافد؟", until="وشنو خاصك دير قبل", box=FULL, people=["worker", "clerk"],
        say=[dict(who=0, text="كنخلص الضريبة فإيطاليا", at=0.8), dict(who=1, text="الخصم من الضريبة ديالك", at=5.0, bg="green")]),
   dict(k="icons", at="وشنو خاصك دير قبل", until="وغادي نرجعو لهاد الخبر", box=ICO, items=[
     ["clipboard-check", "الشروط", "blue"], ["credit-card", "ماشي بالكاش", "green"], ["receipt", "الفاتورات", "gold"], ["users", "الكاف", "blue"]], cols=4, gap=5.0),
   dict(k="map", view="north", pins=["Bologna", "Torino", "Brescia"], labels=False, at="وغادي نرجعو لهاد الخبر", box=R_BOX),
   dict(k="people", at="وغادي نرجعو لهاد الخبر", box=L_BOX, people=["hijab"],
        say=[dict(who=0, text="تلاتة ديال العائلات", at=1.0, bg="green")]),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="03 · المازوط والأدي", src=S_GAS, items=[
   dict(k="chapter", num="03", title="المازوط من بعد الخصم", at=0.2, until="وما خرج حتى قرار"),
   dict(k="big", text="4,88", sub="سانتيم فاللتر: الخصم اللي سالا", at="وما خرج حتى قرار", until="ولكن كاينة مفاجأة"),
   dict(k="calendar", at="ولكن كاينة مفاجأة", until="حسب الأرقام ديال وزارة", box=R_BOX, day=24, month=11, sub="أول نهار بلا خصم"),
   dict(k="people", at="ولكن كاينة مفاجأة", until="حسب الأرقام ديال وزارة", box=L_BOX, people=["worker"],
        say=[dict(who=0, text="الثمن ما طلعش!", at=1.5, bg="green")]),
   dict(k="bars", at="حسب الأرقام ديال وزارة", until="واللي عندو الطوموبيل بالغاز", box=BAR, bars=[
     ["المازوط", 2.196, "2,196 €", "red"], ["الليصانص", 1.939, "1,939 €", "gold"]]),
   dict(k="text", text="الثمن المتوسط فالسيلف، 24/11 (الوزارة)", at="حسب الأرقام ديال وزارة", until="واللي عندو الطوموبيل بالغاز", y=880, size=40),
   dict(k="icons", at="واللي عندو الطوموبيل بالغاز", until="علاش ما طلعش؟", box=ICO, items=[
     ["gas-station", "الغاز", "blue"], ["flame", "الميثان", "gold"]], gap=2.0),
   dict(k="text", text="GPL 0,844 €/l · Metano 2,155 €/kg", at="واللي عندو الطوموبيل بالغاز", until="علاش ما طلعش؟", y=880, size=42),
   dict(k="map", **MED, at="علاش ما طلعش؟", until="شحال كيعني هادشي فالجيب؟", box=BIGMAP),
   dict(k="vs", at="شحال كيعني هادشي فالجيب؟", until="وفالأوطوسترادا، المازوط", box=WIDE,
        right=dict(title="50 لتر مازوط", value="109,80 €", sub="السيلف", icon="gas-station", color="red"),
        left=dict(title="50 لتر ليصانص", value="96,95 €", sub="السيلف", icon="gas-station", color="gold"), gap=8.0),
   dict(k="vs", at="وفالأوطوسترادا، المازوط", until="وخبر آخر: المدير", box=WIDE,
        right=dict(title="فالمدينة", value="109,80 €", sub="50 لتر مازوط", icon="home", color="green"),
        left=dict(title="الأوطوسترادا", value="112,60 €", sub="50 لتر مازوط", icon="car", color="red"), gap=3.0),
   dict(k="people", at="وخبر آخر: المدير", until="والسوق كيتبدل", box=FULL, people=["office", "man"],
        say=[dict(who=1, text="السقف حتى آخر العام؟", at=0.8), dict(who=0, text="ما كاينش قرار رسمي", at=6.0, bg="red")]),
   dict(k="icons", at="النصيحة: قارن الأثمنة", until="ودابا نمشيو للعائلات", box=ICO, items=[
     ["world", "قارن المحطات", "blue"], ["gas-station", "السيلف أرخص", "green"], ["truck", "المحاسب", "gold"]], gap=3.0),
   dict(k="people", at="ودابا نمشيو للعائلات", until="والعتبة ديال الإيزي", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="الأدي فوقاش؟", at=0.8), dict(who=1, text="الجمعة 27 نونبر", at=5.0, bg="green")]),
   dict(k="calendar", at="والعتبة ديال الإيزي", until="والشهر الأول من بعد", box=R_BOX, day=27, month=11, sub="الأدي: الشحنة العادية"),
   dict(k="map", view="south", pins=["Napoli"], labels=False, at="والعتبة ديال الإيزي", until="والشهر الأول من بعد", box=L_BOX),
   dict(k="text", text="ISEE ≤ 10.140 €", at="والعتبة ديال الإيزي", until="والشهر الأول من بعد", y=880, size=44),
   dict(k="big", text="50%", sub="الشهر الأول من بعد التجديد", at="والشهر الأول من بعد", until="وإلى ما وصلاتكش الفلوس"),
   dict(k="warn", text="ما تعطيش الكارطا ولا الكود لحتى واحد", at="وإلى ما وصلاتكش الفلوس", until="ونفس النهار، سبعة", y=600),
   dict(k="vs", at="ونفس النهار، سبعة", until="وفالشرا أونلاين", box=WIDE,
        right=dict(title="الثمن القديم", value="30", sub="يوم: أرخص ثمن", icon="calendar", color="green"),
        left=dict(title="التخفيض الكبير", value="؟", sub="شوف الشهر اللي فات", icon="shopping-cart", color="gold"), gap=4.0),
   dict(k="vs", at="وفالشرا أونلاين", box=WIDE,
        right=dict(title="أونلاين", value="14", sub="يوم باش ترجعها", icon="world", color="green"),
        left=dict(title="الحانوت", value="لا", sub="ماشي ديما", icon="building-store", color="red"), gap=3.0),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="04 · الفلوس ديال دجنبر", src=S_DIC, items=[
   dict(k="chapter", num="04", title="الفلوس ديال دجنبر", at=0.2, until="نبداو بالبانسيون."),
   dict(k="calendar", at="نبداو بالبانسيون.", until="وللبانسيونات الصغيرة", box=R_BOX, day=1, month=12, sub="البانسيون والتريديشيما"),
   dict(k="people", at="نبداو بالبانسيون.", until="وللبانسيونات الصغيرة", box=L_BOX, people=["elder"],
        say=[dict(who=0, text="جوج فمرة وحدة", at=1.5, bg="green")]),
   dict(k="big", text="154,94 €", sub="الزيادة الماكسيموم، بلا طلب", at="وللبانسيونات الصغيرة", until="ومن بعد، الأسينيو أونيكو"),
   dict(k="calendar", at="ومن بعد، الأسينيو أونيكو", until="والطلبات الجديدة،", box=WIDE, day="16·17", month=12, sub="الأسينيو أونيكو بلا تبديل"),
   dict(k="people", at="والطلبات الجديدة،", until="وما تنساش: الإيزي ديالك", box=FULL, people=["hijab", "clerk"],
        say=[dict(who=0, text="بدلت الإيبان", at=0.8), dict(who=1, text="الأسبوع الأخير", at=5.0, bg="gold")]),
   dict(k="calendar", at="وما تنساش: الإيزي ديالك", until="والمبلغ ديال الأسينيو", box=R_BOX, day=31, month=12, sub="الإيزي كيموت"),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="وما تنساش: الإيزي ديالك", until="والمبلغ ديال الأسينيو", box=L_BOX),
   dict(k="bars", at="والمبلغ ديال الأسينيو", until="والتريديشيما ديال الخدامين", box=BAR, bars=[
     ["الماكسيموم", 203.8, "203,80 €", "green"], ["المينيموم", 58.3, "58,30 €", "gold"]]),
   dict(k="vs", at="والتريديشيما ديال الخدامين", until="ودابا الآجال ديال", box=WIDE,
        right=dict(title="الدولة", value="15/12", sub="NoiPA", icon="building-bank", color="green"),
        left=dict(title="القطاع الخاص", value="CCNL", sub="عادة قبل العيد", icon="briefcase", color="gold"), gap=3.0),
   dict(k="calendar", at="ودابا الآجال ديال", until="الأجل الأول: الأكونطو", box=WIDE, day=30, month=11, sub="الاثنين: تلاتة ديال الآجال"),
   dict(k="people", at="الأجل الأول: الأكونطو", until="الأجل الثاني: آبي سوشيال", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="عندي البارتيتا إيفا", at=0.8), dict(who=1, text="F24 قبل الاثنين", at=4.0, bg="gold")]),
   dict(k="people", at="الأجل الثاني: آبي سوشيال", until="خاصك تكون عندك على الأقل", box=FULL, people=["elder", "clerk"],
        say=[dict(who=0, text="شنو هي آبي سوشيال؟", at=0.8), dict(who=1, text="فلوس قبل البانسيون", at=4.0, bg="green")]),
   dict(k="big", text="63", sub="عام وخمسة شهور، على الأقل", at="خاصك تكون عندك على الأقل", until="وتكون فوحدة من هاد"),
   dict(k="icons", at="وتكون فوحدة من هاد", until="والمبلغ يوصل حتى", box=ICO, items=[
     ["briefcase", "بلا خدمة", "blue"], ["heart", "العائلة", "gold"], ["stethoscope", "إعاقة", "green"], ["tool", "خدمة صعيبة", "red"]], cols=4, gap=2.5),
   dict(k="big", text="1.500 €", sub="خام فالشهر، الماكسيموم", at="والمبلغ يوصل حتى", until="ولكن رد البال: الإينبس"),
   dict(k="warn", text="أول كوتيزاسيون من بعد 1995؟ سول الباترونا", at="ولكن رد البال: الإينبس", until="وهادشي كيهم بزاف", y=600),
   dict(k="map", view="italy", pins=["Milano", "Bologna", "Napoli"], labels=False, at="وهادشي كيهم بزاف", until="الأجل الثالث", box=R_BOX),
   dict(k="people", at="وهادشي كيهم بزاف", until="الأجل الثالث", box=L_BOX, people=["worker"],
        say=[dict(who=0, text="أول كوتيزاسيون: 2001", at=1.0, bg="gold")]),
   dict(k="steps", at="الأجل الثالث", until="وحاجة أخيرة فهاد الخبر", box=WIDE, steps=[
     ["كواطر: تسامح", "7/12"], ["كوينكيس: بلا تسامح", "30/11"]], gap=6.0, check_after=99),
   dict(k="map", view="italy", pins=["Torino", "Bari", "Palermo"], labels=False, at="وحاجة أخيرة فهاد الخبر", until="والكارطا ديال خمسمية", box=R_BOX),
   dict(k="people", at="وحاجة أخيرة فهاد الخبر", until="والكارطا ديال خمسمية", box=L_BOX, people=["woman"],
        say=[dict(who=0, text="شوف الكومون ديالك", at=1.5, bg="green")]),
   dict(k="calendar", at="والكارطا ديال خمسمية", box=WIDE, day=16, month=12, sub="الكارطا: أول خلاص"),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="05 · مشاريع، ماشي قوانين", src=S_LEG, items=[
   dict(k="chapter", num="05", title="مشاريع، ماشي قوانين", at=0.2, until="نبداو بالجنسية الإيطالية"),
   dict(k="people", at="نبداو بالجنسية الإيطالية", until="المشروع رقم ألفين", box=FULL, people=["girl", "man"],
        say=[dict(who=0, text="تبدل القانون ديال الجنسية؟", at=0.8), dict(who=1, text="لا، ما زال", at=5.0, bg="green")]),
   dict(k="steps", at="المشروع رقم ألفين", until="يعني دابا، القواعد", box=WIDE, steps=[
     ["مجلس النواب", "1"], ["مجلس الشيوخ", "2"], ["الجريدة الرسمية", "3"]], gap=4.0, check_after=99),
   dict(k="icons", at="يعني دابا، القواعد", until="واللي عندو الكارطا ديال المدة", box=ICO, items=[
     ["calendar", "الإقامة", "blue"], ["coin-euro", "الدخل", "gold"], ["file-certificate", "النقا", "green"], ["school", "B1", "blue"]], cols=4, gap=2.5),
   dict(k="vs", at="واللي عندو الكارطا ديال المدة", until="وشنو كيقترح المشروع؟", box=WIDE,
        right=dict(title="اليوم", value="معفي", sub="بالكارطا", icon="id", color="green"),
        left=dict(title="المشروع", value="B1", sub="حتى بالكارطا", icon="school", color="red"), gap=3.0),
   dict(k="icons", at="وشنو كيقترح المشروع؟", until="وإلى سمعتي شي تعديل", box=ICO, items=[
     ["id", "بلا إعفاء", "red"], ["alert-triangle", "أسباب الرفض", "gold"], ["users", "اليمين بالإيطالية", "blue"]], gap=2.5),
   dict(k="warn", text="التعديل ماشي قانون", at="وإلى سمعتي شي تعديل", until="وفالمشروع حتى الولاد", y=600),
   dict(k="people", at="وفالمشروع حتى الولاد", until="الخبر الثاني فهاد الباب", box=FULL, people=["hijab", "clerk"],
        say=[dict(who=0, text="ولدي تزاد فإيطاليا", at=0.8), dict(who=1, text="اليمين فستة شهور", at=7.0, bg="gold")]),
   dict(k="head", text="الكود الجديد ديال الطريق", sub="باقي مشروع", at="الخبر الثاني فهاد الباب", until="مجلس الدولة وقف"),
   dict(k="calendar", at="مجلس الدولة وقف", until="شنو طلب بالضبط؟", box=R_BOX, day=25, month=11, sub="أجل الحكومة"),
   dict(k="map", view="italy", hl=["Lazio"], pins=["Roma"], labels=False, at="مجلس الدولة وقف", until="شنو طلب بالضبط؟", box=L_BOX),
   dict(k="icons", at="شنو طلب بالضبط؟", until="ومن بعد، مجلس الدولة", box=ICO, items=[
     ["building-bank", "الوزارات", "blue"], ["map-pin", "الجهات", "gold"], ["key", "المعطيات", "green"], ["car", "السرعة", "red"]], cols=4, gap=2.0),
   dict(k="calendar", at="ومن بعد، مجلس الدولة", until="والقانون الجديد، إلى دوز", box=WIDE, day=12, month=1, sub="رأي البرلمان"),
   dict(k="big", text="2028", sub="على الأقل، إلى دوز القانون", at="والقانون الجديد، إلى دوز", until="يعني اليوم والعام الجاي"),
   dict(k="people", at="يعني اليوم والعام الجاي", until="الخبر الثالث: الميزانية", box=FULL, people=["worker", "clerk"],
        say=[dict(who=0, text="الخطايا تبدلات؟", at=0.8), dict(who=1, text="لا، ديال اليوم", at=4.0, bg="green")]),
   dict(k="map", view="italy", hl=["Lazio"], pins=["Roma"], labels=False, at="الخبر الثالث: الميزانية", until="كل شي قلناه", box=BIGMAP),
   dict(k="rows", at="كل شي قلناه", until="ولكن البونس ديال الماماوات ديال هاد العام", y=300, gap=118, size=46, rows=[
     ("البونس ديال الدار", "2027", "كل شي قلناه"),
     ("الماماوات: 100 أورو", "2027", "ونفس الشي للبونس"),
     ("الضريبة ديال الشباب", "2027", "وللضريبة ديال واحد"),
   ]),
   dict(k="text", text="مشاريع: باقي ما تصادقوش", at="كل شي قلناه", until="ولكن البونس ديال الماماوات ديال هاد العام", y=760, size=46),
   dict(k="vs", at="ولكن البونس ديال الماماوات ديال هاد العام", until="القاعدة ديالنا بسيطة", box=WIDE,
        right=dict(title="هاد العام: قانون", value="720 €", sub="الطلب قبل 31/12", person="hijab", color="green"),
        left=dict(title="العام الجاي", value="مشروع", sub="ماشي قانون", person="woman", color="red"), gap=4.0),
   dict(k="people", at="القاعدة ديالنا بسيطة", until="ودابا نمشيو للمثال", box=FULL, people=["elder", "woman"],
        say=[dict(who=1, text="شنو خدام اليوم؟", at=0.8), dict(who=0, text="وشنو باقي مشروع؟", at=4.5, bg="gold")]),
   dict(k="map", view="north", pins=["Bologna", "Torino", "Brescia"], labels=False, at="ودابا نمشيو للمثال", box=BIGMAP),
 ]),
 dict(audio="F.wav", text=T["F"], chapter="06 · مثال: الدار بالحساب", src=S_CASE, items=[
   dict(k="chapter", num="06", title="مثال: البونس ديال الدار بالحساب", at=0.2, until="العائلة الأولى: يوسف"),
   dict(k="map", view="north", pins=["Bologna"], labels=False, at="العائلة الأولى: يوسف", until="بالقانون ديال هاد العام", box=R_BOX),
   dict(k="people", at="العائلة الأولى: يوسف", until="بالقانون ديال هاد العام", box=L_BOX, people=["man"],
        say=[dict(who=0, text="يوسف: 20.000 أورو", at=1.0)]),
   dict(k="steps", at="بالقانون ديال هاد العام", until="وإلى كانت النسبة ستة", box=WIDE, steps=[
     ["المصاريف", "20.000 €"], ["الخصم كامل", "10.000 €"], ["فالعام", "1.000 €"]], gap=4.0, check_after=99),
   dict(k="vs", at="وإلى كانت النسبة ستة", until="الفرق بين الجوج", box=WIDE,
        right=dict(title="50%", value="1.000 €", sub="فالعام", icon="home", color="green"),
        left=dict(title="36%", value="720 €", sub="فالعام", icon="home", color="gold"), gap=3.0),
   dict(k="big", text="2.800 €", sub="الفرق على عشر سنين", at="الفرق بين الجوج", until="وهنا كيبان علاش"),
   dict(k="people", at="وهنا كيبان علاش", until="ويوسف باغي يشري", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="نستنى ولا نبدا؟", at=0.8), dict(who=1, text="تبع الميزانية", at=3.5, bg="green")]),
   dict(k="bars", at="ويوسف باغي يشري", until="ميتين وخمسين أورو فالعام لمدة", box=BAR, bars=[
     ["الموبيليا", 6000, "6.000 €", "grey"], ["السقف", 5000, "5.000 €", "gold"], ["الخصم", 2500, "2.500 €", "green"]]),
   dict(k="big", text="250 €", sub="فالعام، عشر سنين", at="ميتين وخمسين أورو فالعام لمدة", until="العائلة الثانية: نادية"),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="العائلة الثانية: نادية", until="هادي ماشي سكنى رئيسية", box=R_BOX),
   dict(k="people", at="العائلة الثانية: نادية", until="هادي ماشي سكنى رئيسية", box=L_BOX, people=["hijab"],
        say=[dict(who=0, text="نادية: دار ثانية مكرية", at=1.0)]),
   dict(k="steps", at="هادي ماشي سكنى رئيسية", until="وإلى ما تصادقش المشروع، والنسبة", box=WIDE, steps=[
     ["المصاريف", "10.000 €"], ["الخصم 36%", "3.600 €"], ["فالعام", "360 €"]], gap=4.0, check_after=99),
   dict(k="vs", at="وإلى ما تصادقش المشروع، والنسبة", until="العائلة الثالثة: كريم", box=WIDE,
        right=dict(title="36%", value="360 €", sub="فالعام", icon="home", color="green"),
        left=dict(title="30%", value="300 €", sub="فالعام", icon="home", color="red"), gap=3.0),
   dict(k="map", view="north", pins=["Brescia"], labels=False, at="العائلة الثالثة: كريم", until="ولكن السقف هو ستة", box=R_BOX),
   dict(k="people", at="العائلة الثالثة: كريم", until="ولكن السقف هو ستة", box=L_BOX, people=["worker"],
        say=[dict(who=0, text="كريم: 120.000 أورو", at=1.0)]),
   dict(k="bars", at="ولكن السقف هو ستة", until="ربعة آلاف وتمن مية أورو فالعام. والربعة", box=BAR, bars=[
     ["المصاريف", 120000, "120.000 €", "grey"], ["السقف", 96000, "96.000 €", "gold"], ["الخصم", 48000, "48.000 €", "green"]]),
   dict(k="big", text="4.800 €", sub="فالعام، عشر سنين", at="ربعة آلاف وتمن مية أورو فالعام. والربعة", until="ولكن هنا كاين سؤال مهم"),
   dict(k="people", at="ولكن هنا كاين سؤال مهم", until="ودابا الأخطاء اللي", box=FULL, people=["worker", "clerk"],
        say=[dict(who=0, text="الضريبة ديالي صغيرة؟", at=0.8), dict(who=1, text="سول الكاف قبل", at=5.0, bg="green")]),
   dict(k="steps", at="ودابا الأخطاء اللي", until="الخطأ الرابع", box=WIDE, bad=True, steps=[
     ["الخلاص بالكاش", "1"], ["الفاتورات ضاعو", "2"], ["نسيتي التصريح", "3"]], gap=4.0, check_after=99),
   dict(k="steps", at="الخطأ الرابع", until="وإلى كنتي كتكري وباغي", box=WIDE, bad=True, steps=[
     ["المشروع بحال القانون", "4"], ["الدار المكرية بحال ديالك", "5"]], gap=4.0, check_after=99),
   dict(k="people", at="وإلى كنتي كتكري وباغي", box=FULL, people=["girl", "clerk"],
        say=[dict(who=0, text="كنكري: شنو ندير؟", at=0.8), dict(who=1, text="سول الكاف", at=4.0, bg="gold")]),
 ]),
 dict(audio="G.wav", text=T["G"], chapter="07 · من المغرب", src=S_MAR, items=[
   dict(k="chapter", num="07", title="من المغرب", at=0.2, until="الخبر الأول: نرجعو"),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Rabat"], labels=False, at="الخبر الأول: نرجعو", until="باش تدخل، خاصك", box=BIGMAP),
   dict(k="people", at="باش تدخل، خاصك", until="والمنصة، حسب الوزارة", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="عندي الحساب الرقمي؟", at=0.8), dict(who=1, text="ديرو قبل العطلة", at=5.0, bg="green")]),
   dict(k="vs", at="والمنصة، حسب الوزارة", until="الخبر الثاني: ورقة", box=WIDE,
        right=dict(title="الطلبات فالنهار", value="4.000", sub="كثر من", icon="file-text", color="green"),
        left=dict(title="البيرميات فالمغرب", value="11.000.000", sub="كثر من", icon="license", color="gold"), gap=3.0),
   dict(k="calendar", at="الخبر الثاني: ورقة", until="والبريفيتورا فإيطاليا", box=R_BOX, day=9, month=11, sub="الفيش أونلاين"),
   dict(k="map", **MED, route=["Casablanca", "Milano"], at="الخبر الثاني: ورقة", until="والبريفيتورا فإيطاليا", box=L_BOX),
   dict(k="big", text="6", sub="شهور: العمر ديال الورقة للبريفيتورا", at="والبريفيتورا فإيطاليا", until="الخبر الثالث: الصرف"),
   dict(k="big", text="0,6%", sub="الدرهم نقص قدام الأورو", at="الخبر الثالث: الصرف", until="بالحساب ديالنا، على ألف"),
   dict(k="steps", at="بالحساب ديالنا، على ألف", until="ولكن الثمن اللي كتعطيك", box=WIDE, steps=[
     ["صيفطتي", "1.000 €"], ["زايدين تقريبا", "≈ 65 DH"]], gap=3.0, check_after=99),
   dict(k="people", at="ولكن الثمن اللي كتعطيك", until="والتحويلات ديال المغاربة", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="شحال الصرف اليوم؟", at=0.8), dict(who=1, text="قارن العمولة", at=4.0, bg="gold")]),
   dict(k="big", text="103", sub="مليار درهم حتى آخر شتنبر", at="والتحويلات ديال المغاربة", until="الخبر الرابع: الميزانية"),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Rabat"], labels=False, at="الخبر الرابع: الميزانية", until="وفيها اقتراح يطلع", box=BIGMAP),
   dict(k="bars", at="وفيها اقتراح يطلع", until="مثلا، إلى عندك دار فطنجة", box=BAR, bars=[
     ["دابا", 40000, "40.000 DH", "gold"], ["المشروع", 60000, "60.000 DH", "green"]]),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Tanger"], labels=False, at="مثلا، إلى عندك دار فطنجة", until="ولكن هادا باقي مشروع، وما", box=R_BOX),
   dict(k="people", at="مثلا، إلى عندك دار فطنجة", until="ولكن هادا باقي مشروع، وما", box=L_BOX, people=["man"],
        say=[dict(who=0, text="الكرا: 48.000 درهم", at=1.0)]),
   dict(k="warn", text="باقي مشروع · سول محاسب فالمغرب", at="ولكن هادا باقي مشروع، وما", until="وفنفس المشروع، العتبة", y=600),
   dict(k="vs", at="وفنفس المشروع، العتبة", until="الخبر الخامس: نصائح", box=WIDE,
        right=dict(title="دابا", value="80.000 DH", sub="30%", icon="briefcase", color="gold"),
        left=dict(title="المشروع", value="100.000 DH", sub="20%", icon="briefcase", color="green"), gap=3.0),
   dict(k="map", **MED, route=["Milano", "Casablanca"], at="الخبر الخامس: نصائح", until="وإلى كنتي غادي بالطوموبيل", box=BIGMAP),
   dict(k="map", **MED, route=["Genova", "Tanger", "ship"], at="وإلى كنتي غادي بالطوموبيل", until="وإلى خاصك شي ورقة", box=BIGMAP),
   dict(k="icons", at="وإلى خاصك شي ورقة", box=ICO, items=[
     ["calendar", "الموعد", "blue"], ["e-passport", "الباسبور", "gold"], ["id", "البطاقة الوطنية", "green"], ["plane", "الطيارة", "blue"]], cols=4, gap=4.0),
 ]),
 dict(audio="H.wav", text=T["H"], chapter="08 · سؤال وجواب", src=S_QA, items=[
   dict(k="chapter", num="08", title="سؤال وجواب", at=0.2, until="السؤال الأول"),
   dict(k="people", at="السؤال الأول", until="الجواب: لا. التجديد", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="جددتو فالمغرب: نسوق بيه هنا؟", at=0.8)]),
   dict(k="map", **MED, at="الجواب: لا. التجديد", until="السؤال الثاني", box=R_BOX),
   dict(k="icons", at="الجواب: لا. التجديد", until="السؤال الثاني", box=L_BOX, items=[
     ["calendar", "عام واحد", "gold"], ["license", "التبديل", "green"], ["alert-triangle", "ولا الامتحان", "red"]], gap=4.0),
   dict(k="people", at="السؤال الثاني", until="السؤال الثالث", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="ضاع ليا البيرمي المغربي", at=0.8), dict(who=1, text="نسخة جديدة فالمنصة", at=4.0, bg="green")]),
   dict(k="people", at="السؤال الثالث", until="السؤال الرابع", box=FULL, people=["hijab", "office"],
        say=[dict(who=0, text="كنكري الدار: البونس؟", at=0.8), dict(who=1, text="سول الكاف", at=8.0, bg="gold")]),
   dict(k="people", at="السؤال الرابع", until="الجواب: القواعد ديال هاد العام", box=FULL, people=["worker"],
        say=[dict(who=0, text="بديت الإصلاح هاد العام", at=0.8)]),
   dict(k="vs", at="الجواب: القواعد ديال هاد العام", until="السؤال الخامس", box=WIDE,
        right=dict(title="2026", value="قانون", sub="حتى 31/12", icon="home", color="green"),
        left=dict(title="2027", value="مشروع", sub="باقي", icon="home", color="red"), gap=3.0),
   dict(k="people", at="السؤال الخامس", until="السؤال الإضافي", box=FULL, people=["farmer", "clerk"],
        say=[dict(who=0, text="علاش المازوط ما طلعش؟", at=0.8), dict(who=1, text="السوق هبط", at=4.5, bg="green")]),
   dict(k="people", at="السؤال الإضافي", until="السؤال السادس", box=FULL, people=["elder", "woman"],
        say=[dict(who=0, text="البونات ديال الكومون؟", at=0.8), dict(who=1, text="شوف الموقع اليوم", at=5.0, bg="gold")]),
   dict(k="calendar", at="السؤال السادس", until="السؤال السابع", box=R_BOX, day=27, month=11, sub="الأدي"),
   dict(k="people", at="السؤال السادس", until="السؤال السابع", box=L_BOX, people=["girl"],
        say=[dict(who=0, text="الأدي ما وصلاتش", at=0.8)]),
   dict(k="people", at="السؤال السابع", until="السؤال الثامن", box=FULL, people=["elder", "clerk"],
        say=[dict(who=0, text="سالات ليا النازبي", at=0.8), dict(who=1, text="قبل 30 نونبر", at=5.0, bg="gold")]),
   dict(k="people", at="السؤال الثامن", until="السؤال التاسع", box=FULL, people=["student", "clerk"],
        say=[dict(who=0, text="الجنسية بعشرين عام؟", at=0.8), dict(who=1, text="لا، عشر سنين", at=4.0, bg="green")]),
   dict(k="people", at="السؤال التاسع", until="وإلى عندك سؤال آخر", box=FULL, people=["man", "office"],
        say=[dict(who=0, text="الخطايا تبدلات؟", at=0.8), dict(who=1, text="لا، ديال اليوم", at=4.0, bg="green")]),
   dict(k="people", at="وإلى عندك سؤال آخر", box=FULL, people=["girl", "elder", "hijab"],
        say=[dict(who=0, text="كتب سؤالك فالكومونتير", at=0.8, bg="green")]),
 ]),
 dict(audio="I.wav", text=T["I"], chapter="09 · الخلاصة والتواريخ", src=S_HOME, items=[
   dict(k="head", text="الخلاصة", at=0.2, until="واحد: البيرمي المغربي"),
   dict(k="rows", at="واحد: البيرمي المغربي", until="خمسة: الجنسية", y=300, gap=118, size=46, rows=[
     ("البيرمي المغربي من التيليفون", "E-ROKHSATI", "واحد: البيرمي"),
     ("البونس ديال الدار: 2027 مشروع", "50% · 36%", "جوج: البونس"),
     ("المازوط: الخصم سالا", "2,196 €", "تلاتة: المازوط"),
     ("الأدي والبانسيون", "27/11 · 1/12", "ربعة: الأدي"),
   ]),
   dict(k="rows", at="خمسة: الجنسية", until="ودابا التواريخ ديال الأيام", y=300, gap=118, size=46, rows=[
     ("الجنسية، الكود، الميزانية: مشاريع", "?", "خمسة: الجنسية"),
     ("المغرب: السوابق والصرف", "0,6%", "ستة: فالمغرب"),
     ("قبل العطلة: الباسبور والبطاقة", "Marocco", "وقبل العطلة، شوف"),
   ]),
   dict(k="steps", at="ودابا التواريخ ديال الأيام", until="الثلاثاء واحد دجنبر:", box=WIDE, steps=[
     ["الأدي · البلاك فرايداي", "27/11"], ["الأكونطو · آبي سوشيال", "30/11"]], gap=4.0, check_after=99),
   dict(k="steps", at="الثلاثاء واحد دجنبر:", until="ستاش دجنبر: الإيمو", box=WIDE, steps=[
     ["البانسيون · الضو", "1/12"], ["الروطاماسيون كواطر", "7/12"], ["الديكري فلوسي", "7/12"]], gap=4.0, check_after=99),
   dict(k="steps", at="ستاش دجنبر: الإيمو", until="وإلى فاتك شي فيديو", box=WIDE, steps=[
     ["الإيمو · الكارطا", "16/12"], ["الأسينيو أونيكو", "17/12"], ["الماماوات · الإيزي · الدار", "31/12"]], gap=4.0, check_after=99),
   dict(k="icons", at="وإلى فاتك شي فيديو", until="وكل نهار كاين", box=ICO, items=[
     ["license", "تبديل البيرمي", "blue"], ["id", "البيرميسو", "gold"], ["heart", "الجنسية", "green"], ["plane", "الفيزا", "blue"]], cols=4, gap=2.0),
   dict(k="steps", at="وكل نهار كاين", until="ونعاودو نقولو", box=WIDE, steps=[
     ["فيديو قصير", "13:00"], ["النشرة الطويلة", "16:30"], ["فيديو قصير", "19:00"], ["الشرح الكامل", "20:30"]], gap=3.0, check_after=99),
   dict(k="people", at="ونعاودو نقولو", until="وتذكير صغير", box=FULL, people=["clerk", "woman"],
        say=[dict(who=0, text="سول الكاف ولا الباترونا", at=1.0, bg="green")]),
   dict(k="map", view="italy", pins=["Milano", "Roma", "Napoli"], labels=False, at="وتذكير صغير", until="وحاجة أخيرة", box=R_BOX),
   dict(k="people", at="وتذكير صغير", until="وحاجة أخيرة", box=L_BOX, people=["hijab"],
        say=[dict(who=0, text="صيفطيه للعائلة", at=1.0, bg="green")]),
   dict(k="warn", text="ما تعطيش السبيد ولا الهوية الرقمية لحتى واحد", at="وحاجة أخيرة", until="وإلى عجبك هاد الفيديو", y=640),
   dict(k="cta", at="وإلى عجبك هاد الفيديو", until="وكتب لينا فالكومونتير", text="ابوني فالقناة", sub="وفعل الجرس"),
   dict(k="people", at="وكتب لينا فالكومونتير", box=FULL, people=["girl", "worker", "hijab"],
        say=[dict(who=1, text="شنو فادك أكثر؟", at=0.8), dict(who=2, text="صيفطو لشي واحد", at=6.0, bg="green")]),
 ]),
]

THUMB = dict(
  title=[("البيرمي المغربي؟", (236, 196, 96)), "ولا كيتجدد من التيليفون", "وبونس الدار فالعام الجاي"],
  num="50%", numsub="بونس الدار",
  bottom="مغاربة إيطاليا · خبار مفيدة بالدارجة",
)
