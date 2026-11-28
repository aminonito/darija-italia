import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-28.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo1-2026-11-28-final")
BRAND = "مغاربة إيطاليا"
T = {k: v.replace("گ", "ك") for k, v in JOB["blocks"].items()}
EP_EDITS = os.path.join(ROOT, "tts/jobs/lungo1-2026-11-28-edits.json")
EDITS = json.load(open(EP_EDITS, encoding="utf-8")) if os.path.exists(EP_EDITS) else {}
for k, pairs in EDITS.items():
    for a, b in pairs:
        T[k] = T[k].replace(a, b)


S_HOME = "مغاربة إيطاليا · خبار مفيدة بالدارجة"
S_PEN = "GU n. 274 del 24/11/2026 (DM 13/11/2026) · Lavorosì 26/11 · DottrinaLavoro 26/11 · InformazioneFiscale 27/11"
S_SCU = "Legge 27/11/2026 n. 219 (GU n. 277) · Scuolainforma 27/11 · Offida.info 27/11 · Lazioeventi 28/11 · BusinessOnline 26/11 · Zon 25/11"
S_MAN = "AGI 26/11 · Il Foglio 26/11 · Public Policy 27/11 · Milano Finanza 24/11 · Camera A.C. 2124-A · SicurAuto · Newsauto"
S_CAR = "MIMIT via LaPresse e Agenzia Opinione 28/11 · Il Post 24/11 · ARERA del. 58/2026 · Askanews · Istat 27/11 · Polizia Postale"
S_DIC = "INPS msg 3801/2026 via Fiscal Focus ed Eutekne 20/11 · QuiFinanza · InformazioneFiscale · registro 22-27/11"
S_CASE = "Calcoli nostri su DM 13/11/2026 (+3,2% provvisorio) · INPS assegno sociale 2026 · LentePubblica (minimo 611,85 €)"
S_MAR = "Bank Al-Maghrib (bkam.ma 27/11) · H24info · Bladi · Maroc Diplomatique 21-22/11 · La Vie Eco · LeBrief · TelQuel"
S_QA = "Fonti dei capitoli 01-08"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850); FULL = (160, 300, 1760, 860)
WIDE = (260, 220, 1660, 830); ICO = (160, 330, 1760, 860); BAR = (160, 300, 1760, 840)
MED = dict(view="med", hl=["ITA", "MAR"], labels=False)
BIGMAP = (160, 200, 1760, 880)

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="00 · أخبار السيمانة", src=S_HOME, items=[
   dict(k="head", text="نشرة السيمانة", at=0.2, until="شنو كاين فهاد النشرة؟", sub="السبت 28 نونبر 2026"),
   dict(k="people", at=0.6, until="شنو كاين فهاد النشرة؟", box=FULL, people=["elder", "hijab", "man"],
        say=[dict(who=0, text="البانسيون غادي تزيد؟", at=0.8), dict(who=2, text="خبار بالأرقام", at=6.0, bg="green")]),
   dict(k="rows", at="شنو كاين فهاد النشرة؟", until="ومن بعد، مثال عملي", y=280, gap=110, size=46, rows=[
     ("البانسيون ديال يناير", "3,2%", "عندنا خبر مزيان"),
     ("المدرسة: ولا قانون", "27/11", "عندنا المرسوم ديال"),
     ("الميزانية والتصويت", "3/12", "عندنا الميزانية ديال"),
     ("المازوط والضو والنصب", "1/12", "عندنا ثمن المازوط"),
     ("الفلوس ديال دجنبر", "31/12", "وعندنا الفلوس والآجال"),
   ]),
   dict(k="map", **MED, route=["Torino", "Casablanca"], at="ومن بعد، مثال عملي", until="ومن المغرب، الدرهم", box=BIGMAP),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Rabat"], labels=False, at="ومن المغرب، الدرهم", until="قبل ما نبداو، جوج", box=BIGMAP),
   dict(k="icons", at="قبل ما نبداو، جوج", until="الخبر الأول: البانسيون", box=ICO, items=[
     ["file-certificate", "جوج مصادر", "green"], ["alert-triangle", "ماشي استشارة", "gold"], ["users", "سول الباترونا", "blue"]], gap=2.5),
   dict(k="chapter", num="01", title="البانسيون ديال يناير تزيد", at="الخبر الأول: البانسيون", until="نهار الثلاثاء أربعة وعشرين"),
   dict(k="calendar", at="نهار الثلاثاء أربعة وعشرين", until="الزيادة هي تلاتة فاصلة", box=R_BOX, day=24, month=11, sub="الجريدة الرسمية"),
   dict(k="map", view="italy", hl=["Lazio"], pins=["Roma"], labels=False, at="نهار الثلاثاء أربعة وعشرين", until="الزيادة هي تلاتة فاصلة", box=L_BOX),
   dict(k="big", text="3,2%", sub="الزيادة من 1 يناير", at="الزيادة هي تلاتة فاصلة", until="شكون كيستافد؟"),
   dict(k="people", at="شكون كيستافد؟", until="ولكن ردو البال لجوج", box=FULL, people=["elder", "clerk"],
        say=[dict(who=0, text="خاصني نطلب الزيادة؟", at=0.8), dict(who=1, text="لا، كتجي بوحدها", at=9.0, bg="green")]),
   dict(k="warn", text="النسبة مؤقتة: كاين تصحيح من بعد", at="الحاجة الأولى: هاد النسبة", until="الحاجة الثانية: الزيادة", y=600),
   dict(k="vs", at="الحاجة الثانية: الزيادة", until="وعلاش تلاتة فاصلة جوج؟", box=WIDE,
        right=dict(title="البانسيون حتى", value="2.447 €", sub="الزيادة كاملة", icon="report-money", color="green"),
        left=dict(title="فوق هاد الرقم", value="أقل", sub="على الجزء الزايد", icon="alert-triangle", color="gold"), gap=6.0),
   dict(k="icons", at="وعلاش تلاتة فاصلة جوج؟", until="حسبناها: إلى كانت", box=ICO, items=[
     ["report-money", "مؤشر الأثمنة", "blue"], ["bolt", "الطاقة", "gold"], ["x", "بانسيون المغرب: لا", "red"]], gap=3.0),
   dict(k="bars", at="حسبناها: إلى كانت", until="هادو حسابات ديالنا", box=BAR, bars=[
     ["700 €", 22.4, "22,40 €", "gold"], ["1.000 €", 32, "32 €", "green"]]),
   dict(k="text", text="الزيادة فالشهر · حساب ديالنا قبل الضريبة", at="حسبناها: إلى كانت", until="هادو حسابات ديالنا", y=880, size=42),
   dict(k="people", at="هادو حسابات ديالنا", until="وتذكير: قبل يناير", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="فين نشوف الرقم؟", at=0.6), dict(who=1, text="التشيدولينو ديال يناير", at=4.0, bg="green")]),
   dict(k="calendar", at="وتذكير: قبل يناير", box=R_BOX, day=1, month=12, sub="البانسيون والتريديشيما"),
   dict(k="people", at="وتذكير: قبل يناير", box=L_BOX, people=["elder"],
        say=[dict(who=0, text="والزيادة الصغيرة بوحدها", at=3.0, bg="green")]),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="02 · المدرسة والإضراب", src=S_SCU, items=[
   dict(k="chapter", num="02", title="المدرسة: المرسوم ولا قانون", at=0.2, until="ودابا عندنا الجديد"),
   dict(k="steps", at="ودابا عندنا الجديد", until="شنو فيه للعائلات", box=WIDE, steps=[
     ["مجلس الشيوخ", "19/11"], ["مجلس النواب", "26/11"], ["الجريدة الرسمية", "27/11"]], gap=3.5),
   dict(k="people", at="شنو فيه للعائلات", until="أولا، السقف", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="شنو تبدل لولادنا؟", at=0.5), dict(who=1, text="نعاودو بالمختصر", at=2.5, bg="green")]),
   dict(k="icons", at="أولا، السقف", until="كيبدا من العام الدراسي", box=ICO, items=[
     ["school", "الأول ابتدائي", "blue"], ["school", "الأول إعدادي", "gold"], ["school", "الأول ثانوي", "green"]], gap=1.5),
   dict(k="calendar", at="كيبدا من العام الدراسي", until="ثانيا، شكون كيتحسب؟", box=R_BOX, day="2027", month="2028", sub="العام الدراسي"),
   dict(k="people", at="كيبدا من العام الدراسي", until="ثانيا، شكون كيتحسب؟", box=L_BOX, people=["child"],
        say=[dict(who=0, text="ماشي هاد العام", at=1.5, bg="green")]),
   dict(k="vs", at="ثانيا، شكون كيتحسب؟", until="ثالثا، إلى فاتت", box=WIDE,
        right=dict(title="تزاد هنا وقرا هنا", value="لا", sub="عادة ما كيتحسبش", person="child", color="green"),
        left=dict(title="3 سنين فإيطاليا", value="لا", sub="الإعدادي والثانوي", person="girl", color="green"), gap=7.0),
   dict(k="map", view="north", pins=["Brescia"], labels=False, at="ثالثا، إلى فاتت", until="رابعا، الواليدين", box=R_BOX),
   dict(k="icons", at="ثالثا، إلى فاتت", until="رابعا، الواليدين", box=L_BOX, items=[
     ["map-pin", "المدارس القراب", "blue"], ["school", "دروس الطاليانية", "green"]], gap=4.0),
   dict(k="people", at="رابعا، الواليدين", until="كاينة ذعيرة من ميتين", box=FULL, people=["man", "office"],
        say=[dict(who=0, text="ما كنعرفش الطاليانية مزيان", at=0.8), dict(who=1, text="دروس بالمجان", at=6.0, bg="green")]),
   dict(k="big", text="200 - 1.000", sub="أورو: غير من بعد إنذار رسمي", at="كاينة ذعيرة من ميتين", until="وحتى الوجه المغطي"),
   dict(k="warn", text="الوجه المغطي ممنوع فالمدرسة", at="وحتى الوجه المغطي", until="خامسا، المساعدة", y=600),
   dict(k="bars", at="خامسا، المساعدة", until="ونعاودو نقولو: هادا", box=BAR, bars=[
     ["قبل", 30000, "30.000 €", "gold"], ["دابا", 40000, "40.000 €", "green"]]),
   dict(k="text", text="العتبة ديال الإيزي: المساعدة ديال الكتب", at="خامسا، المساعدة", until="ونعاودو نقولو: هادا", y=880, size=42),
   dict(k="warn", text="ماشي منع ديال التسجيل", at="ونعاودو نقولو: هادا", until="والنصيحة: جمع", y=600),
   dict(k="icons", at="والنصيحة: جمع", until="وإلى عندك ولد غادي يجي", box=ICO, items=[
     ["certificate", "الشهادات", "blue"], ["report-money", "النتائج", "gold"], ["file-text", "سنين القراية", "green"]], gap=2.0),
   dict(k="map", **MED, route=["Casablanca", "Milano"], at="وإلى عندك ولد غادي يجي", until="وإلى عندك سؤال على الحالة", box=BIGMAP),
   dict(k="people", at="وإلى عندك سؤال على الحالة", until="الخبر الثالث: الإضراب", box=FULL, people=["hijab", "clerk"],
        say=[dict(who=0, text="ولدي كيتحسب؟", at=0.5), dict(who=1, text="سولي المدير", at=3.0, bg="green")]),
   dict(k="chapter", num="03", title="الإضراب العام 4 دجنبر", at="الخبر الثالث: الإضراب", until="تأكد: أربعة وعشرين"),
   dict(k="map", view="italy", pins=["Milano", "Roma", "Napoli"], labels=False, at="تأكد: أربعة وعشرين", until="التران من التسعود", box=BIGMAP),
   dict(k="steps", at="التران من التسعود", until="والترانات الجهوية", box=WIDE, steps=[
     ["الخميس 3 دجنبر", "21:00"], ["الجمعة 4 دجنبر", "21:00"]], gap=3.0, check_after=99),
   dict(k="vs", at="والترانات الجهوية", until="الطيارات نهار الجمعة", box=WIDE,
        right=dict(title="الصباح", value="6 - 9", sub="التران الجهوي", icon="train", color="green"),
        left=dict(title="العشية", value="18 - 21", sub="التران الجهوي", icon="train", color="green"), gap=4.0),
   dict(k="vs", at="الطيارات نهار الجمعة", until="والأوطوروت من العشرة", box=WIDE,
        right=dict(title="الصباح", value="7 - 10", sub="وقت محمي", icon="plane", color="green"),
        left=dict(title="العشية", value="18 - 21", sub="وقت محمي", icon="plane", color="green"), gap=4.0),
   dict(k="steps", at="والأوطوروت من العشرة", until="والطوبيس والميترو", box=WIDE, steps=[
     ["الخميس 3 دجنبر", "22:00"], ["الجمعة 4 دجنبر", "22:00"]], gap=3.0, check_after=99),
   dict(k="icons", at="والطوبيس والميترو", until="إلى عندك سفر للمغرب", box=ICO, items=[
     ["bus", "الطوبيس", "blue"], ["train", "الميترو", "gold"]], gap=1.5),
   dict(k="map", **MED, route=["Milano", "Casablanca"], at="إلى عندك سفر للمغرب", until="وتذكر: الإضراب ماشي", box=BIGMAP),
   dict(k="people", at="وتذكر: الإضراب ماشي", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="خاصني نضرب؟", at=0.5), dict(who=1, text="لا، ماشي واجب", at=3.0, bg="green")]),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="04 · الميزانية 2027", src=S_MAN, items=[
   dict(k="chapter", num="04", title="الميزانية 2027: فين وصلات؟", at=0.2, until="الميزانية دابا فلجنة"),
   dict(k="map", view="italy", hl=["Lazio"], pins=["Roma"], labels=False, at="الميزانية دابا فلجنة", until="النواب دخلو تقريبا", box=BIGMAP),
   dict(k="bars", at="النواب دخلو تقريبا", until="والتواريخ؟", box=BAR, bars=[
     ["دخلو", 6600, "6.600", "blue"], ["ترفضو", 1650, "1/4", "red"], ["مهمين", 700, "700", "gold"]]),
   dict(k="text", text="التعديلات ديال الميزانية", at="النواب دخلو تقريبا", until="والتواريخ؟", y=880, size=42),
   dict(k="steps", at="والتواريخ؟", until="ومن بعد كتمشي لمجلس", box=WIDE, steps=[
     ["التصويت فاللجنة", "3/12"], ["تعديلات الحكومة", "10/12"], ["اللجنة كتسالي", "15/12"], ["القاعة", "18/12"]], gap=4.0, check_after=99),
   dict(k="steps", at="ومن بعد كتمشي لمجلس", until="شنو كاين فالنقاش؟", box=WIDE, steps=[
     ["مجلس الشيوخ", "?"], ["المصادقة النهائية", "31/12"]], gap=3.0, check_after=99),
   dict(k="warn", text="كلشي باقي مشروع", at="شنو كاين فالنقاش؟", until="أولا، كارطا", y=600),
   dict(k="people", at="أولا، كارطا", until="ثانيا، الزيادة ديال", box=FULL, people=["elder", "clerk"],
        say=[dict(who=0, text="تلات مية أورو ليا؟", at=0.8), dict(who=1, text="باقي اقتراح", at=8.0, bg="gold")]),
   dict(k="vs", at="ثانيا، الزيادة ديال", until="ثالثا، البونوس", box=WIDE,
        right=dict(title="النص ديال الحكومة", value="×4", sub="الحد الأدنى", icon="file-text", color="blue"),
        left=dict(title="اقتراحات", value="×5 · ×6", sub="باقي ما تقررش", icon="alert-triangle", color="gold"), gap=5.0),
   dict(k="people", at="ثالثا، البونوس", until="وردو البال: البونوس ديال هاد العام", box=FULL, people=["hijab", "child"],
        say=[dict(who=0, text="جوج ولاد وكنخدم", at=0.8), dict(who=1, text="شحال؟", at=6.0, bg="gold")]),
   dict(k="bars", at="وردو البال: البونوس ديال هاد العام", until="رابعا، الشباب", box=BAR, bars=[
     ["الشهر", 60, "60 €", "gold"], ["العام", 720, "720 €", "green"]]),
   dict(k="text", text="البونوس ديال الماماوات · الطلب قبل 31/12", at="وردو البال: البونوس ديال هاد العام", until="رابعا، الشباب", y=880, size=42),
   dict(k="big", text="1%", sub="على الزيادة فالخلصة · مشروع", at="رابعا، الشباب", until="خامسا، التسوية"),
   dict(k="icons", at="خامسا، التسوية", until="إذن النصيحة", box=ICO, items=[
     ["file-text", "الروطاماسيوني", "blue"], ["alert-triangle", "غير اقتراح", "gold"]], gap=2.0),
   dict(k="people", at="إذن النصيحة", until="وخبر صغير من نفس البرلمان", box=FULL, people=["girl", "office"],
        say=[dict(who=0, text="بونوس جديد من يناير؟", at=0.8), dict(who=1, text="شوف الجريدة الرسمية", at=5.0, bg="green")]),
   dict(k="vs", at="وخبر صغير من نفس البرلمان", until="ونفس الحاجة للكود", box=WIDE,
        right=dict(title="اليوم", value="معفي", sub="عندك الكارطا", icon="id", color="green"),
        left=dict(title="المشروع", value="B1", sub="باقي ما تصادقش", icon="file-text", color="gold"), gap=6.0),
   dict(k="steps", at="ونفس الحاجة للكود", box=WIDE, steps=[
     ["مجلس الدولة", "CdS"], ["البرلمان", "12/1"], ["التطبيق", "2028"]], gap=3.5, check_after=99),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="05 · المازوط والضو والنصب", src=S_CAR, items=[
   dict(k="chapter", num="05", title="المازوط والضو والبلاك فرايداي", at=0.2, until="نبداو بالمازوط."),
   dict(k="calendar", at="نبداو بالمازوط.", until="الثمن المتوسط فالسيلف", box=R_BOX, day=23, month=11, sub="سالا الخصم"),
   dict(k="icons", at="نبداو بالمازوط.", until="الثمن المتوسط فالسيلف", box=L_BOX, items=[
     ["gas-station", "المازوط", "gold"], ["x", "بلا مرسوم جديد", "red"]], gap=3.0),
   dict(k="vs", at="الثمن المتوسط فالسيلف", until="حسبناها: خمسين لتر", box=WIDE,
        right=dict(title="البنزين", value="1,920", sub="أورو فاللتر · 28/11", icon="gas-station", color="green"),
        left=dict(title="المازوط", value="2,187", sub="أورو فاللتر · 28/11", icon="gas-station", color="gold"), gap=4.0),
   dict(k="bars", at="حسبناها: خمسين لتر", until="ومثال آخر: إلى كنتي", box=BAR, bars=[
     ["المازوط", 109.35, "109,35 €", "gold"], ["البنزين", 96.0, "96,00 €", "green"]]),
   dict(k="text", text="50 لتر · الثمن المتوسط فالسيلف", at="حسبناها: خمسين لتر", until="ومثال آخر: إلى كنتي", y=880, size=42),
   dict(k="big", text="875", sub="أورو فالشهر: 8 ديال البلانات", at="ومثال آخر: إلى كنتي", until="ونصيحة: الثمن كيتبدل"),
   dict(k="people", at="ونصيحة: الثمن كيتبدل", until="دابا الضو.", box=FULL, people=["worker", "man"],
        say=[dict(who=0, text="فين أرخص محطة؟", at=0.6), dict(who=1, text="شوف الأثمنة قبل", at=4.0, bg="green")]),
   dict(k="calendar", at="دابا الضو.", until="شكون؟ غير الزبناء", box=R_BOX, day=1, month=12, sub="الضو فنهار"),
   dict(k="icons", at="دابا الضو.", until="شكون؟ غير الزبناء", box=L_BOX, items=[
     ["bolt", "الضو", "gold"], ["clock", "نهار خدمة", "green"]], gap=3.0),
   dict(k="vs", at="شكون؟ غير الزبناء", until="والعملية كاملة", box=WIDE,
        right=dict(title="الدار بلا ديون", value="1", sub="نهار خدمة", icon="bolt", color="green"),
        left=dict(title="ديون ولا شركة", value="10", sub="أيام خدمة", icon="building-store", color="gold"), gap=5.0),
   dict(k="icons", at="والعملية كاملة", until="والثمن ديال الغاز للزبناء", box=ICO, items=[
     ["clock", "3 سيمانات ماكسيموم", "gold"], ["x", "الغاز لا", "red"]], gap=2.5),
   dict(k="people", at="والثمن ديال الغاز للزبناء", until="آخر رقم هو ديال أكتوبر", box=FULL, people=["elder", "clerk"],
        say=[dict(who=0, text="والغاز ديال نونبر؟", at=0.6), dict(who=1, text="باقي ما خرجش", at=3.0, bg="gold")]),
   dict(k="big", text="9,1%", sub="الغاز ديال أكتوبر على شتنبر", at="آخر رقم هو ديال أكتوبر", until="ونصيحة قبل ما تبدل"),
   dict(k="steps", at="ونصيحة قبل ما تبدل", until="وعلاش الطاقة غالية؟", box=WIDE, steps=[
     ["قارن العروض", "1"], ["ذعيرة الخروج", "2"], ["التراجع", "14"], ["الكود فالفاتورة", "POD"]], gap=4.0, check_after=99),
   dict(k="bars", at="وعلاش الطاقة غالية؟", until="وأخيرا، البلاك", box=BAR, bars=[
     ["10/2025", 3.6, "3,6", "gold"], ["10/2026", 6.9, "6,9", "red"]]),
   dict(k="text", text="العجز ديال الطاقة · مليار أورو · معهد الإحصاء", at="وعلاش الطاقة غالية؟", until="وأخيرا، البلاك", y=880, size=42),
   dict(k="people", at="وأخيرا، البلاك", until="أولا، ما تكليكيش", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="تخفيض سبعين فالمية!", at=0.6), dict(who=1, text="رد البال", at=4.0, bg="red")]),
   dict(k="icons", at="أولا، ما تكليكيش", until="وحتى المساجات", box=ICO, items=[
     ["mail", "ما تكليكيش", "red"], ["cash", "بلا فيرمون", "gold"], ["credit-card", "الكارطا المشحونة", "green"]], gap=3.5),
   dict(k="warn", text="الكولي محبوس؟ خلص أورو؟ نصب", at="وحتى المساجات", until="والقانون كيقول: الثمن القديم", y=600),
   dict(k="vs", at="والقانون كيقول: الثمن القديم", until="وإلى طحتي فشي نصب", box=WIDE,
        right=dict(title="الثمن القديم", value="30", sub="يوم: أرخص ثمن", icon="shopping-cart", color="gold"),
        left=dict(title="أونلاين", value="14", sub="يوم باش ترجعها", icon="shopping-cart", color="green"), gap=5.0),
   dict(k="people", at="وإلى طحتي فشي نصب", box=FULL, people=["man", "office"],
        say=[dict(who=0, text="تنصب عليا!", at=0.5), dict(who=1, text="بلغ وعيط للبنك", at=3.0, bg="green")]),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="06 · الفلوس ديال دجنبر", src=S_DIC, items=[
   dict(k="chapter", num="06", title="الفلوس والآجال نهار بنهار", at=0.2, until="نهار الاثنين تلاتين نونبر"),
   dict(k="calendar", at="نهار الاثنين تلاتين نونبر", until="الثلاثاء واحد دجنبر", box=R_BOX, day=30, month=11, sub="التسبيق التاني"),
   dict(k="people", at="نهار الاثنين تلاتين نونبر", until="الثلاثاء واحد دجنبر", box=L_BOX, people=["worker"],
        say=[dict(who=0, text="البارتيتا إيفا: الإيف 24", at=2.0, bg="gold")]),
   dict(k="calendar", at="الثلاثاء واحد دجنبر", until="والزيادة حتى لمية", box=R_BOX, day=1, month=12, sub="البانسيون والتريديشيما"),
   dict(k="big", text="154,94", sub="أورو: الزيادة الماكسيموم", at="والزيادة حتى لمية", until="وردو البال: الأسينيو"),
   dict(k="warn", text="الأسينيو سوسيالي ما كياخدش هاد الزيادة", at="وردو البال: الأسينيو", until="الخميس تلاتة والجمعة", y=600),
   dict(k="steps", at="الخميس تلاتة والجمعة", until="الاثنين سبعة دجنبر", box=WIDE, steps=[
     ["الإضراب", "4/12"], ["آخر نهار للتجديد", "10/12"]], gap=3.5, check_after=99),
   dict(k="big", text="9", sub="أيام: الديكري فلوسي حتى 7/12", at="الاثنين سبعة دجنبر", until="الثلاثاء خمسطاش دجنبر"),
   dict(k="vs", at="الثلاثاء خمسطاش دجنبر", until="الأربعاء ستطاش", box=WIDE,
        right=dict(title="الدولة", value="15/12", sub="التريديشيما", icon="building-store", color="blue"),
        left=dict(title="القطاع الخاص", value="CCNL", sub="عادة قبل عيد الميلاد", icon="report-money", color="green"), gap=4.0),
   dict(k="big", text="18", sub="يوم: أول خلصة بالكارطا", at="الأربعاء ستطاش", until="ستطاش وسبعطاش دجنبر"),
   dict(k="icons", at="ستطاش وسبعطاش دجنبر", until="الخميس واحد وتلاتين", box=ICO, items=[
     ["users", "الأسينيو أونيكو", "green"]], gap=1.0),
   dict(k="calendar", at="الخميس واحد وتلاتين", until="حسبناها: بقاو تلاتة وتلاتين", box=R_BOX, day=31, month=12, sub="الإيزي · الماماوات"),
   dict(k="big", text="33", sub="يوم باقيين", at="حسبناها: بقاو تلاتة وتلاتين", until="وما تنساش الكارطا ديال الأدي"),
   dict(k="steps", at="وما تنساش الكارطا ديال الأدي", until="ودابا خبر من الإينبس", box=WIDE, steps=[
     ["الطلبات الجديدة", "15/12"], ["الشحنة العادية", "23/12"]], gap=3.0, check_after=99),
   dict(k="people", at="ودابا خبر من الإينبس", until="كيفاش توصلك؟", box=FULL, people=["elder", "clerk"],
        say=[dict(who=0, text="رسالة من الإينبس؟", at=0.8), dict(who=1, text="من يناير رقمية", at=6.0, bg="gold")]),
   dict(k="steps", at="كيفاش توصلك؟", until="واللي ما عندوش السبيد", box=WIDE, steps=[
     ["التطبيق آي أو", "1"], ["البيك", "2"], ["الموقع بالسبيد", "3"]], gap=2.5, check_after=99),
   dict(k="icons", at="واللي ما عندوش السبيد", until="النصيحة: إلى عندك واليدين", box=ICO, items=[
     ["mail", "رسالة مضمونة", "blue"], ["users", "التوكيل", "gold"], ["calculator", "بالأقساط", "green"]], gap=3.0),
   dict(k="people", at="النصيحة: إلى عندك واليدين", until="وخبر أخير لهاد الفصل", box=FULL, people=["elder", "girl"],
        say=[dict(who=1, text="نعاونك فالسبيد", at=1.0, bg="green"), dict(who=0, text="وهاد الرسالة؟", at=7.0)]),
   dict(k="vs", at="وخبر أخير لهاد الفصل", box=WIDE,
        right=dict(title="البانسيون", value="3,2%", sub="مؤقتة", icon="report-money", color="green"),
        left=dict(title="الأسينيو أونيكو", value="?", sub="المبالغ فيناير", icon="users", color="gold"), gap=5.0),
 ]),
 dict(audio="F.wav", text=T["F"], chapter="07 · مثال: شحال تزيد البانسيون؟", src=S_CASE, items=[
   dict(k="chapter", num="07", title="مثال: شحال تزيد البانسيون ديالك؟", at=0.2, until="القاعدة بسيطة"),
   dict(k="big", text="× 1,032", sub="البانسيون ديال دجنبر", at="القاعدة بسيطة", until="الحالة الأولى"),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="الحالة الأولى", until="الزيادة: تمن مية", box=R_BOX),
   dict(k="people", at="الحالة الأولى", until="الزيادة: تمن مية", box=L_BOX, people=["elder"],
        say=[dict(who=0, text="تلاتين عام فالمعمل", at=1.5)]),
   dict(k="bars", at="الزيادة: تمن مية", until="وفالعام كامل", box=BAR, bars=[
     ["دجنبر", 800, "800 €", "gold"], ["يناير", 825.6, "825,60 €", "green"]]),
   dict(k="big", text="332,80", sub="أورو فالعام: 13 ديال المرات", at="وفالعام كامل", until="الحالة الثانية"),
   dict(k="map", view="north", pins=["Bologna"], labels=False, at="الحالة الثانية", until="وإلى كانت كتوصلها رسالة", box=R_BOX),
   dict(k="people", at="الحالة الثانية", until="وإلى كانت كتوصلها رسالة", box=L_BOX, people=["hijab"],
        say=[dict(who=0, text="زادت 17 أورو", at=4.0, bg="green")]),
   dict(k="warn", text="رسالة الريد: جاوب كل عام", at="وإلى كانت كتوصلها رسالة", until="الحالة الثالثة", y=600),
   dict(k="map", view="north", pins=["Milano"], labels=False, at="الحالة الثالثة", until="إلى تطبقات عليه", box=R_BOX),
   dict(k="people", at="الحالة الثالثة", until="إلى تطبقات عليه", box=L_BOX, people=["elder"],
        say=[dict(who=0, text="والأسينيو سوسيالي؟", at=1.5)]),
   dict(k="vs", at="إلى تطبقات عليه", until="والحد الأدنى ديال", box=WIDE,
        right=dict(title="2026", value="546,24", sub="أورو فالشهر", icon="report-money", color="blue"),
        left=dict(title="2027 تقدير", value="563,72", sub="حساب ديالنا", icon="calculator", color="green"), gap=4.0),
   dict(k="vs", at="والحد الأدنى ديال", until="وشنو خاصك تدير؟", box=WIDE,
        right=dict(title="الحد الأدنى 2026", value="611,85", sub="أورو فالشهر", icon="report-money", color="blue"),
        left=dict(title="2027 تقدير", value="631,43", sub="حساب ديالنا", icon="calculator", color="green"), gap=4.0),
   dict(k="steps", at="وشنو خاصك تدير؟", until="وعلاش البانسيون فيناير", box=WIDE, steps=[
     ["بلا طلب", "1"], ["التشيدولينو بالسبيد", "2"], ["قارن مع دجنبر", "3"], ["الباترونا", "4"]], gap=4.0, check_after=99),
   dict(k="icons", at="وعلاش البانسيون فيناير", until="والأخطاء اللي بزاف", box=ICO, items=[
     ["report-money", "الضريبة", "blue"], ["map-pin", "الجهة والكوموني", "gold"], ["calculator", "النيتو والبروتو", "green"]], gap=2.5),
   dict(k="people", at="والأخطاء اللي بزاف", until="التاني، ينساو الريد", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="زيادة كبيرة لكلشي؟", at=0.8), dict(who=1, text="لا، غير حتى 2.447", at=5.0, bg="red")]),
   dict(k="warn", text="نسيتي الريد؟ الزيادات تقدر تحبس", at="التاني، ينساو الريد", until="التالت، يسافرو", y=600),
   dict(k="big", text="29", sub="يوم برا: الأسينيو كيتوقف", at="التالت، يسافرو", until="الرابع، يعطيو"),
   dict(k="warn", text="السبيد ديالك ليك بوحدك", at="الرابع، يعطيو", until="وإلى بغيتي الشرح الكامل", y=600),
   dict(k="cta", at="وإلى بغيتي الشرح الكامل", text="الأسينيو سوسيالي", sub="الشرح الكامل فالقناة"),
 ]),
 dict(audio="G.wav", text=T["G"], chapter="08 · من المغرب", src=S_MAR, items=[
   dict(k="chapter", num="08", title="من المغرب", at=0.2, until="الخبر الأول: الدرهم"),
   dict(k="map", **MED, route=["Milano", "Casablanca"], at="الخبر الأول: الدرهم", until="يعني الأورو ولا", box=BIGMAP),
   dict(k="vs", at="يعني الأورو ولا", until="والسعر الرسمي ديال التحويل", box=WIDE,
        right=dict(title="قدام الأورو", value="0,6%", sub="الدرهم نقص", icon="coin-euro", color="gold"),
        left=dict(title="قدام الدولار", value="1,7%", sub="الدرهم نقص", icon="cash", color="gold"), gap=3.0),
   dict(k="big", text="10,99", sub="درهم للأورو · بنك المغرب 27/11", at="والسعر الرسمي ديال التحويل", until="حسبناها: إلى صيفطتي"),
   dict(k="big", text="10.995", sub="درهم على 1.000 أورو", at="حسبناها: إلى صيفطتي", until="ولكن ردو البال: البنك"),
   dict(k="people", at="ولكن ردو البال: البنك", until="والاحتياطي ديال", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="نصرف هنا ولا تما؟", at=0.6), dict(who=1, text="قارن الثمن النهائي", at=4.0, bg="green")]),
   dict(k="big", text="512", sub="مليار درهم: الاحتياطي", at="والاحتياطي ديال", until="الخبر الثاني: التحويلات"),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Rabat"], labels=False, at="الخبر الثاني: التحويلات", until="صيفطو كثر من مية", box=BIGMAP),
   dict(k="big", text="103", sub="مليار درهم حتى لآخر شتنبر", at="صيفطو كثر من مية", until="والأرقام ديال آخر أكتوبر"),
   dict(k="calendar", at="والأرقام ديال آخر أكتوبر", until="الخبر الثالث: قانون", box=R_BOX, day="؟", month=10, sub="أرقام أكتوبر"),
   dict(k="people", at="والأرقام ديال آخر أكتوبر", until="الخبر الثالث: قانون", box=L_BOX, people=["elder"],
        say=[dict(who=0, text="فلوس الجالية", at=2.0, bg="green")]),
   dict(k="steps", at="الخبر الثالث: قانون", until="شنو فيه؟ الكرا", box=WIDE, steps=[
     ["مجلس النواب", "14/11"], ["مجلس المستشارين", "17/11"], ["القراءة الثانية", "?"]], gap=4.0, check_after=99),
   dict(k="bars", at="شنو فيه؟ الكرا", until="يعني إلى عندك دار مكرية", box=BAR, bars=[
     ["قبل", 40000, "40.000 DH", "gold"], ["المشروع", 60000, "60.000 DH", "green"]]),
   dict(k="text", text="الكرا فالعام: بلا اقتطاع من المصدر", at="شنو فيه؟ الكرا", until="يعني إلى عندك دار مكرية", y=880, size=42),
   dict(k="map", **MED, route=["Milano", "Tanger"], at="يعني إلى عندك دار مكرية", until="المقاول الذاتي:", box=BIGMAP),
   dict(k="bars", at="المقاول الذاتي:", until="وكاينين حوايج اجتماعية", box=BAR, bars=[
     ["قبل", 80000, "80.000 DH", "gold"], ["المشروع", 100000, "100.000 DH", "green"]]),
   dict(k="text", text="المقاول الذاتي: النسبة من 30 لـ 20", at="المقاول الذاتي:", until="وكاينين حوايج اجتماعية", y=880, size=42),
   dict(k="icons", at="وكاينين حوايج اجتماعية", until="وحتى لدابا، ما لقينا", box=ICO, items=[
     ["bolt", "الضو بالمجان", "gold"], ["heart", "معاش الأرامل", "green"], ["cash", "الدعم المباشر", "blue"]], gap=3.5),
   dict(k="warn", text="باقي مشروع · ما فيه حتى إجراء للجالية", at="وحتى لدابا، ما لقينا", until="الخبر الرابع", y=600),
   dict(k="big", text="131.000", sub="مستافد من الدعم ديال السكن", at="الخبر الرابع", until="وردو البال للسماسرة"),
   dict(k="people", at="وردو البال للسماسرة", until="وتذكير للعطلة", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="عطيني الفلوس ونقيدك", at=0.6), dict(who=1, text="نصاب!", at=3.0, bg="red")]),
   dict(k="icons", at="وتذكير للعطلة", box=ICO, cols=4, items=[
     ["license", "إي رخصتي", "blue"], ["file-text", "الفيش", "gold"], ["e-passport", "الباسبور", "green"], ["id", "البطاقة الوطنية", "blue"]], gap=1.5),
 ]),
 dict(audio="H.wav", text=T["H"], chapter="09 · سؤال وجواب", src=S_QA, items=[
   dict(k="chapter", num="09", title="سؤال وجواب", at=0.2, until="السؤال الأول"),
   dict(k="people", at="السؤال الأول", until="السؤال الثاني", box=FULL, people=["elder", "clerk"],
        say=[dict(who=0, text="نطلب الزيادة؟", at=0.8), dict(who=1, text="لا، بوحدها", at=6.0, bg="green")]),
   dict(k="vs", at="السؤال الثاني", until="السؤال الثالث", box=WIDE,
        right=dict(title="اليوم", value="3,2%", sub="مؤقتة", icon="report-money", color="gold"),
        left=dict(title="العام الجاي", value="؟", sub="التصحيح", icon="calculator", color="blue"), gap=4.0),
   dict(k="people", at="السؤال الثالث", until="السؤال الرابع", box=FULL, people=["woman", "child"],
        say=[dict(who=0, text="غادي يمنعوه؟", at=0.8), dict(who=1, text="ماشي منع", at=5.0, bg="green")]),
   dict(k="people", at="السؤال الرابع", until="السؤال الخامس", box=FULL, people=["man", "office"],
        say=[dict(who=0, text="غادي نخلص ذعيرة؟", at=0.8), dict(who=1, text="غير إلى رفضتي", at=5.0, bg="gold")]),
   dict(k="people", at="السؤال الخامس", until="السؤال السادس", box=FULL, people=["elder", "girl"],
        say=[dict(who=0, text="كارطا لكاع المتقاعدين؟", at=0.8), dict(who=1, text="غير اقتراح", at=6.0, bg="gold")]),
   dict(k="map", **MED, route=["Milano", "Casablanca"], at="السؤال السادس", until="السؤال السابع", box=R_BOX),
   dict(k="people", at="السؤال السادس", until="السؤال السابع", box=L_BOX, people=["hijab"],
        say=[dict(who=0, text="الطيارة مع الحداش", at=1.0)]),
   dict(k="people", at="السؤال السابع", until="السؤال الثامن", box=FULL, people=["woman", "clerk"],
        say=[dict(who=0, text="والغاز فنهار؟", at=0.8), dict(who=1, text="غير الضو", at=4.0, bg="gold")]),
   dict(k="calendar", at="السؤال الثامن", until="السؤال التاسع", box=R_BOX, day=16, month=12, sub="أول خلصة بالكارطا"),
   dict(k="people", at="السؤال الثامن", until="السؤال التاسع", box=L_BOX, people=["hijab"],
        say=[dict(who=0, text="ما خلصت والو", at=1.0)]),
   dict(k="people", at="السؤال التاسع", until="السؤال العاشر", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="علاش السعر قل؟", at=0.8), dict(who=1, text="الهامش والعمولة", at=6.0, bg="gold")]),
   dict(k="people", at="السؤال العاشر", until="السؤال الحادي عشر", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="الكرا فالمغرب معفي؟", at=0.8), dict(who=1, text="لا، سول محاسب", at=6.0, bg="red")]),
   dict(k="steps", at="السؤال الحادي عشر", until="السؤال الثاني عشر", box=WIDE, steps=[
     ["البيرميسو كيسالي", "10/3/2027"], ["ناقص 90 يوم", "10/12/2026"], ["دير الطلب دابا", "!"]], gap=4.0, check_after=99),
   dict(k="vs", at="السؤال الثاني عشر", until="السؤال الثالث عشر", box=WIDE,
        right=dict(title="9 - 13 دجنبر", value="تكميل", sub="الطلبات القدام", icon="clipboard-check", color="green"),
        left=dict(title="طلب جديد", value="لا", sub="من بعد 7/12", icon="x", color="red"), gap=4.0),
   dict(k="people", at="السؤال الثالث عشر", until="وإلى عندك سؤال آخر", box=FULL, people=["elder", "girl"],
        say=[dict(who=0, text="رسالة كتطلب فلوس", at=0.8), dict(who=1, text="شوف الموقع بالسبيد", at=5.0, bg="green")]),
   dict(k="people", at="وإلى عندك سؤال آخر", box=FULL, people=["girl", "elder", "hijab"],
        say=[dict(who=0, text="كتب سؤالك فالكومونتير", at=0.8, bg="green")]),
 ]),
 dict(audio="I.wav", text=T["I"], chapter="10 · الخلاصة والتواريخ", src=S_HOME, items=[
   dict(k="head", text="الخلاصة", at=0.2, until="واحد: البانسيون"),
   dict(k="rows", at="واحد: البانسيون", until="ودابا التواريخ ديال الأيام", y=300, gap=118, size=46, rows=[
     ("البانسيون ديال يناير", "3,2%", "واحد: البانسيون"),
     ("المدرسة: ولا قانون", "2027", "جوج: المرسوم"),
     ("الميزانية: التصويت", "3/12", "تلاتة: الميزانية"),
     ("المازوط · الضو فنهار", "1/12", "ربعة: المازوط"),
     ("المغرب: الأورو", "10,99", "خمسة: من المغرب"),
   ]),
   dict(k="steps", at="ودابا التواريخ ديال الأيام", until="الثلاثاء واحد دجنبر: البانسيون والتريديشيما", box=WIDE, steps=[
     ["الأكونطو · السايبر مانداي", "30/11"]], gap=2.0, check_after=99),
   dict(k="steps", at="الثلاثاء واحد دجنبر: البانسيون والتريديشيما", until="خمسطاش دجنبر: المجلس", box=WIDE, steps=[
     ["البانسيون · الضو", "1/12"], ["الإضراب", "4/12"], ["الديكري فلوسي", "7/12"], ["الحكومة: التعديلات", "10/12"]], gap=3.0, check_after=99),
   dict(k="steps", at="خمسطاش دجنبر: المجلس", until="وحاجة عملية: دير ورقة", box=WIDE, steps=[
     ["بنك المغرب · التريديشيما", "15/12"], ["الإيمو · الكارطا", "16/12"], ["الميزانية فالقاعة", "18/12"], ["الإيزي · الماماوات", "31/12"]], gap=3.0, check_after=99),
   dict(k="icons", at="وحاجة عملية: دير ورقة", until="وخصوصا الواليدين", box=ICO, items=[
     ["calendar", "الأجندة", "blue"], ["phone", "الواتساب", "green"]], gap=2.0),
   dict(k="people", at="وخصوصا الواليدين", until="وإلى فاتك شي فيديو", box=FULL, people=["elder", "girl"],
        say=[dict(who=1, text="نعاونك فالتشيدولينو", at=1.0, bg="green")]),
   dict(k="icons", at="وإلى فاتك شي فيديو", until="وكل نهار كاين", box=ICO, cols=4, items=[
     ["license", "تبديل البيرمي", "blue"], ["id", "البيرميسو", "gold"], ["heart", "الجنسية", "green"], ["plane", "الفيزا", "blue"]], gap=2.0),
   dict(k="steps", at="وكل نهار كاين", until="ونعاودو نقولو", box=WIDE, steps=[
     ["فيديو قصير", "13:00"], ["النشرة الطويلة", "16:30"], ["فيديو قصير", "19:00"], ["الشرح الكامل", "20:30"]], gap=2.0, check_after=99),
   dict(k="people", at="ونعاودو نقولو", until="وحاجة أخيرة", box=FULL, people=["clerk", "woman"],
        say=[dict(who=0, text="سول الباترونا ولا الكاف", at=1.0, bg="green")]),
   dict(k="warn", text="ما تعطي السبيد ولا الكود لحتى واحد", at="وحاجة أخيرة", until="سيفي هاد الفيديو", y=640),
   dict(k="map", **MED, route=["Milano", "Casablanca"], at="سيفي هاد الفيديو", until="وإلى عجبك هاد الفيديو", box=BIGMAP),
   dict(k="cta", at="وإلى عجبك هاد الفيديو", until="وإلى عندك شي صاحب", text="ابوني فالقناة", sub="وفعل الجرس"),
   dict(k="people", at="وإلى عندك شي صاحب", box=FULL, people=["girl", "elder", "hijab"],
        say=[dict(who=1, text="شنو فادك أكثر؟", at=4.0), dict(who=2, text="صيفطو لشي واحد", at=9.0, bg="green")]),
 ]),
]

THUMB = dict(
  title=[("البانسيون فيناير 2027", (236, 196, 96)), "زيادة مؤقتة: شحال غادي تشد؟", "وأخبار السيمانة بالدارجة"],
  num="3,2%", numsub="زيادة البانسيون",
  bottom="مغاربة إيطاليا · خبار مفيدة بالدارجة",
)
