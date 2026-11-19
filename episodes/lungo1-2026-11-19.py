import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo1-2026-11-19.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo1-2026-11-19-final")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = {k: v.replace("گ", "ك") for k, v in JOB["blocks"].items()}
# punteggiatura più fitta nel capitolo 01 (aggancio sottotitoli: testo parlato invariato)
T["B"] = (T["B"].replace("وافقات على النص نهار أربعطاش أكتوبر، ومن بعد دخل", "وافقات على النص نهار أربعطاش أكتوبر. ومن بعد، دخل")
          .replace("المجلس رفض الطلبات اللي كانت باغية توقف النقاش، والمشروع", "المجلس رفض الطلبات اللي كانت باغية توقف النقاش. والمشروع")
          .replace("بحكم نهائي.", "بحكم نهائي.").replace("وتقدر توصل لستة وتلاتين شهر.", "وتقدر توصل لستة وتلاتين شهر."))

S_HOME = "مغاربة إيطاليا · خبار مفيدة بالدارجة"
S_CIT = "Camera dei deputati, temi A.C. 2124-A · Quotidiano.net 20/10 · Avvenire 14/10"
S_SCI = "Adnkronos 18/11 · Fanpage · Virgilio Notizie · BlogSicilia"
S_ACC = "QuiFinanza · Finanza.com · INPS (assegno unico) · Money.it"
S_MAN = "Sky TG24 18/11 · Tgcom24 18/11 · Milano Finanza 18/11"
S_KAR = "Ministero dell'Interno · Prefettura · InfoImmigrazione · Arletti Partners"
S_MAR = "L'ODJ 15/11 · Atlasinfo · Medias24 9/11 · FNH"
S_QA = "Fonti dei capitoli 01-05 · Polizia di Stato · MIMIT · Altroconsumo"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850); FULL = (160, 300, 1760, 860)
WIDE = (260, 220, 1660, 830)

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="00 · أخبار اليوم", src=S_HOME, items=[
   dict(k="head", text="أخبار اليوم", at=0.2, until="شنو كاين اليوم؟", sub="الخميس 19 نونبر 2026"),
   dict(k="people", at=0.6, until="شنو كاين اليوم؟", box=FULL, people=["hijab", "man", "worker"],
        say=[dict(who=0, text="شنو الجديد اليوم؟", at=0.8), dict(who=2, text="خبار مفيدة بالأرقام", at=3.5, bg="green")]),
   dict(k="rows", at="شنو كاين اليوم؟", until="ومن بعد، غادي ندخلو", y=270, gap=120, size=50, rows=[
     ("الجنسية الإيطالية", "A.C. 2124", "الخبر الأول على"),
     ("الإضراب", "20-21/11", "الخبر التاني على"),
     ("الأكونطو ديال الضريبة", "30/11", "الخبر التالت على"),
     ("الميزانية ديال إيطاليا", "2027", "الخبر الرابع على"),
   ]),
   dict(k="people", at="ومن بعد، غادي ندخلو", until="ومن بعد، خبر من المغرب", box=R_BOX, people=["man"],
        say=[dict(who=0, text="عندي الكارطا", at=0.6, bg="gold")]),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="ومن بعد، غادي ندخلو", until="ومن بعد، خبر من المغرب", box=L_BOX),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Milano", "Casablanca"], pins=["Rabat"], labels=False,
        at="ومن بعد، خبر من المغرب", until="قبل ما نبداو، جوج", box=(160, 200, 1760, 880)),
   dict(k="icons", at="قبل ما نبداو، جوج", until="وتذكير سريع بخبر", box=(160, 330, 1760, 860), items=[
     ["file-certificate", "جوج مصادر على الأقل", "green"], ["alert-triangle", "ماشي استشارة", "gold"], ["users", "سول الباطروناطو", "blue"]], gap=2.5),
   dict(k="vs", at="وتذكير سريع بخبر", until="وحاجة أخرى مهمة", box=WIDE,
        right=dict(title="قبل", value="60", sub="يوم قبل ما يسالي", icon="id", color="grey"),
        left=dict(title="دابا", value="90", sub="يوم قبل ما يسالي", icon="id", color="green"), gap=3.0),
   dict(k="people", at="وحاجة أخرى مهمة", until="وإلى كان عندك شي سؤال على", box=FULL, people=["clerk", "woman"],
        say=[dict(who=0, text="مشروع ماشي قانون", at=0.8, bg="red"), dict(who=1, text="واخا، فهمت", at=4.0, bg="green")]),
   dict(k="map", view="italy", pins=["Milano", "Torino", "Bologna", "Roma", "Napoli"], labels=False, at="وإلى كان عندك شي سؤال على", box=L_BOX),
   dict(k="people", at="وإلى كان عندك شي سؤال على", box=R_BOX, people=["girl"],
        say=[dict(who=0, text="كتب فالكومونتير", at=0.6, bg="green")]),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="01 · الجنسية: مشروع قانون", src=S_CIT, items=[
   dict(k="chapter", num="01", title="الجنسية: مشروع جديد", at=0.1, until="اللجنة ديال الشؤون"),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="اللجنة ديال الشؤون", until="ولكن عقل مزيان", box=L_BOX),
   dict(k="steps", at="اللجنة ديال الشؤون", until="ولكن عقل مزيان", box=R_BOX, steps=[
     ["اللجنة", "14/10"], ["القاعة", "28/10"], ["التصويت", "?"]], gap=3.5, check_after=0.6),
   dict(k="vs", at="ولكن عقل مزيان", until="شنو مكتوب فالمشروع؟", box=WIDE,
        right=dict(title="مجلس النواب", value="1", sub="كيتناقش دابا", icon="building-bank", color="gold"),
        left=dict(title="مجلس الشيوخ", value="2", sub="من بعد", icon="building-bank", color="grey"), gap=3.0),
   dict(k="people", at="شنو مكتوب فالمشروع؟", until="النقطة الأولى: اللغة", box=FULL, people=["office", "hijab"],
        say=[dict(who=1, text="شنو تبدل؟", at=0.4)]),
   dict(k="vs", at="النقطة الأولى: اللغة", until="النقطة التانية: الأحكام", box=WIDE,
        right=dict(title="اليوم", value="لا", sub="الكارطا كتعفي من B1", icon="id", color="green"),
        left=dict(title="المشروع", value="B1", sub="حتى للي عندو الكارطا", icon="school", color="red"), gap=6.0),
   dict(k="icons", at="النقطة التانية: الأحكام", until="النقطة التالتة: اليمين", box=(160, 330, 1760, 860), items=[
     ["building-bank", "جرائم ضد الدولة", "red"], ["pill", "المخدرات فوق 3 سنين", "red"], ["world", "أحكام برا فوق عام", "gold"], ["scale", "قضية مفتوحة = الطلب يتوقف", "blue"]], gap=4.0),
   dict(k="people", at="النقطة التالتة: اليمين", until="النقطة الرابعة: الدراري", box=R_BOX, people=["clerk"],
        say=[dict(who=0, text="اليمين بالإيطالية", at=1.5, bg="gold")]),
   dict(k="calendar", at="النقطة التالتة: اليمين", until="النقطة الرابعة: الدراري", box=L_BOX, day=6, month="شهور", sub="أجل اليمين ما تبدلش"),
   dict(k="bars", at="النقطة الرابعة: الدراري", until="والنقطة الخامسة: سحب", box=(160, 330, 1760, 840), bars=[
     ["الأجل العادي", 24, "24", "gold"], ["أقصى حد", 36, "36", "red"]], gap=2.5),
   dict(k="head", text="أجل الجواب بالشهور", at="النقطة الرابعة: الدراري", until="والنقطة الخامسة: سحب", sub="للدراري اللي تزادو فإيطاليا"),
   dict(k="people", at="شكون كيهمو هاد الخبر", until="النصيحة العملية: ما تصدقش", box=FULL, people=["man", "girl", "elder"],
        say=[dict(who=0, text="عندي الكارطا", at=0.8, bg="gold"), dict(who=1, text="عندي سبعطاش عام", at=4.0)]),
   dict(k="map", view="italy", pins=["Milano", "Torino", "Bologna", "Napoli"], labels=False, at="النصيحة العملية: ما تصدقش", box=L_BOX),
   dict(k="icons", at="النصيحة العملية: ما تصدقش", box=R_BOX, items=[
     ["file-text", "الكونطرات", "green"], ["receipt", "730 ديال كل عام", "green"], ["id", "البيرميسوات", "gold"], ["home", "الريزيدينسا", "blue"]], gap=2.0),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="02 · الإضراب ديال الويكاند", src=S_SCI, items=[
   dict(k="chapter", num="02", title="الإضراب ديال الويكاند", at=0.1, until="غدا الجمعة عشرين نونبر"),
   dict(k="calendar", at="غدا الجمعة عشرين نونبر", until="دابا التران.", box=R_BOX, day=20, month=11, sub="الجمعة · إضراب عام"),
   dict(k="icons", at="غدا الجمعة عشرين نونبر", until="دابا التران.", box=L_BOX, items=[
     ["building-bank", "الإدارات", "gold"], ["school", "المدارس", "gold"], ["bus", "الطوبيس", "red"]], gap=4.0),
   dict(k="steps", at="دابا التران.", until="والتران اللي كيكون", box=WIDE, steps=[
     ["الجمعة: عادي حتى", "21:00"], ["الإضراب", "23 h"], ["السبت: كيسالي", "20:00"]], gap=3.0, check_after=0.6),
   dict(k="map", view="italy", pins=["Milano", "Roma", "Napoli"], labels=False, at="والتران اللي كيكون", until="واش كاين شي تران مضمون", box=L_BOX),
   dict(k="people", at="والتران اللي كيكون", until="واش كاين شي تران مضمون", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="غادي يكمل؟", at=0.6)]),
   dict(k="big", text="1", at="واش كاين شي تران مضمون", until="ومثال باش يوضح", y=420, size=260, color=GREEN, sub="ساعة: التران كيكمل إلى وصل فأقل منها"),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Milano", "Casablanca"], pins=["Bergamo"], labels=False,
        at="ومثال باش يوضح", until="وفالمطارات؟", box=L_BOX),
   dict(k="people", at="ومثال باش يوضح", until="وفالمطارات؟", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="طيارتي نهار السبت!", at=1.5, bg="red")]),
   dict(k="calendar", at="وفالمطارات؟", until="والمدارس؟", box=R_BOX, day=22, month=11, sub="الأحد · مالبينسا"),
   dict(k="map", view="north", pins=["Milano"], labels=False, at="وفالمطارات؟", until="والمدارس؟", box=L_BOX),
   dict(k="people", at="والمدارس؟", until="وحاجة مهمة: التواريخ", box=FULL, people=["woman", "child"],
        say=[dict(who=0, text="شوف الريجيسترو", at=0.8, bg="green")]),
   dict(k="head", text="شوف السيت الرسمي نهار السفر", at="وحاجة مهمة: التواريخ", until="والخلاصة: الجمعة", sub="التواريخ كيتبدلو"),
   dict(k="rows", at="والخلاصة: الجمعة", until="وإلى كنتي غادي تسافر للمغرب", y=300, gap=130, size=52, rows=[
     ("الإضراب العام", "20/11", "الجمعة إضراب"),
     ("التران: من", "21:00 · 20/11", "التسعة ديال الليل ديال الجمعة"),
     ("التران: حتى", "20:00 · 21/11", "حتى التمنية ديال العشية ديال السبت"),
   ]),
   dict(k="people", at="وإلى كنتي غادي تسافر للمغرب", box=R_BOX, people=["man"],
        say=[dict(who=0, text="خلي نهار زايد", at=1.0, bg="gold")]),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Genova", "Tanger", "ship"], labels=False, at="وإلى كنتي غادي تسافر للمغرب", box=L_BOX),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="03 · الأكونطو قبل 30 نونبر", src=S_ACC, items=[
   dict(k="chapter", num="03", title="الأكونطو: آخر أجل 30/11", at=0.1, until="نهار تلاتين نونبر هو"),
   dict(k="calendar", at="نهار تلاتين نونبر هو", until="شكون خاصو يخلصها", box=R_BOX, day=30, month=11, sub="الدفعة التانية ديال الأكونطو"),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="نهار تلاتين نونبر هو", until="شكون خاصو يخلصها", box=L_BOX),
   dict(k="icons", at="شكون خاصو يخلصها", until="وشكون ما خاصوش", box=(160, 330, 1760, 860), items=[
     ["tool", "البارتيتا إيفا", "gold"], ["receipt-tax", "الفورفيتاريو", "gold"], ["home-dollar", "الكرا بلا معلم", "gold"], ["credit-card", "F24", "blue"]], gap=3.0),
   dict(k="people", at="وشكون ما خاصوش", until="كيفاش كتحسب؟", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="خدام بالكونطرا", at=0.6), dict(who=1, text="شوف البوستا باغا", at=5.0, bg="green")]),
   dict(k="vs", at="كيفاش كتحسب؟", until="مثال: سعيد", box=WIDE,
        right=dict(title="يونيو", value="40%", sub="الدفعة الأولى", icon="calendar", color="grey"),
        left=dict(title="نونبر", value="60%", sub="الدفعة التانية", icon="calendar", color="gold"), gap=3.0),
   dict(k="map", view="north", pins=["Brescia"], labels=False, at="مثال: سعيد", until="ستين فالمية فنونبر، يعني", box=L_BOX),
   dict(k="people", at="مثال: سعيد", until="ستين فالمية فنونبر، يعني", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="شحال نخلص؟", at=1.0)]),
   dict(k="bars", at="ستين فالمية فنونبر، يعني", until="ومثال تاني: حسناء", box=(160, 300, 1760, 840), bars=[
     ["الضريبة ديال العام اللي فات", 1500, "1.500 €", "grey"], ["يونيو", 600, "600 €", "blue"], ["نونبر", 900, "900 €", "gold"]], gap=1.5),
   dict(k="map", view="south", pins=["Napoli"], labels=False, at="ومثال تاني: حسناء", until="وإلى كانت الضريبة صغيرة", box=L_BOX),
   dict(k="people", at="ومثال تاني: حسناء", until="وإلى كانت الضريبة صغيرة", box=R_BOX, people=["woman"],
        say=[dict(who=0, text="مرة وحدة فنونبر", at=4.0, bg="green")]),
   dict(k="steps", at="وإلى كانت الضريبة صغيرة", until="وإلى المدخول ديالك هاد العام", box=WIDE, steps=[
     ["ما كاين حتى أكونطو", "< 51,65 €"], ["دفعة وحدة فنونبر", "< 257,52 €"], ["جوج دفعات", "> 257,52 €"]], gap=3.0, check_after=0.6),
   dict(k="people", at="وإلى المدخول ديالك هاد العام", until="ونسيتي ولا تأخرتي", box=FULL, people=["office", "man"],
        say=[dict(who=1, text="نخلص أقل؟", at=0.6), dict(who=0, text="غير مع الكومبتابل", at=6.0, bg="red")]),
   dict(k="icons", at="ونسيتي ولا تأخرتي", until="ودابا، فلوس كتدخل", box=(160, 330, 1760, 860), items=[
     ["receipt", "الضريبة", "gold"], ["alert-triangle", "غرامة صغيرة", "red"], ["clock", "بكري = أقل", "green"]], gap=2.5),
   dict(k="calendar", at="ودابا، فلوس كتدخل", until="إلى ما دخلوش الفلوس", box=R_BOX, day=19, month=11, sub="الأسينيو أونيكو · اليوم وغدا"),
   dict(k="people", at="ودابا، فلوس كتدخل", until="إلى ما دخلوش الفلوس", box=L_BOX, people=["hijab", "child"],
        say=[dict(who=0, text="الأسينيو دخل؟", at=1.0)]),
   dict(k="steps", at="إلى ما دخلوش الفلوس", box=WIDE, steps=[
     ["السيت ديال الإينبس", "1"], ["SPID", "2"], ["الخانة ديال الأسينيو", "3"]], gap=1.5, check_after=0.6),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="04 · الميزانية ديال 2027", src=S_MAN, items=[
   dict(k="chapter", num="04", title="الميزانية 2027: شنو كاين؟", at=0.1, until="كل عام، الحكومة"),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="كل عام، الحكومة", until="هاد العام، الأحزاب", box=L_BOX),
   dict(k="calendar", at="كل عام، الحكومة", until="هاد العام، الأحزاب", box=R_BOX, day=31, month=12, sub="آخر أجل للموافقة"),
   dict(k="big", text="7.000", at="هاد العام، الأحزاب", until="إذن هاد الخبر كله", y=430, size=240, color=GOLD, sub="تقريبا · التعديلات المقدمة"),
   dict(k="people", at="إذن هاد الخبر كله", until="الحاجة الأولى: الكارطا", box=FULL, people=["clerk", "man"],
        say=[dict(who=0, text="كلشي باقي مشروع", at=0.6, bg="red")]),
   dict(k="vs", at="الحاجة الأولى: الكارطا", until="إلى عندك الواليدين", box=WIDE,
        right=dict(title="فوق 75 عام", value="300 €", sub="مصاريف الصحة", icon="stethoscope", color="green"),
        left=dict(title="الميزانية", value="1,6 Mld €", sub="الشروط باقي كتناقش", icon="coin-euro", color="gold"), gap=5.0),
   dict(k="people", at="إلى عندك الواليدين", until="الحاجة التانية: الزيادة", box=FULL, people=["elder", "woman"],
        say=[dict(who=1, text="نتبعو الخبر", at=0.8, bg="green")]),
   dict(k="bars", at="الحاجة التانية: الزيادة", until="شكون كيهمو هادشي؟", box=(160, 300, 1760, 840), bars=[
     ["فالنص: 4 مرات الحد الأدنى", 2447, "2.447 €", "gold"], ["الفكرة: 5 مرات", 3000, "3.000 €", "grey"]], gap=4.0),
   dict(k="head", text="الزيادة الكاملة فالبانسيون حتى", at="الحاجة التانية: الزيادة", until="شكون كيهمو هادشي؟", sub="فالشهر"),
   dict(k="people", at="شكون كيهمو هادشي؟", until="الحاجة التالتة: الشباب", box=R_BOX, people=["elder"],
        say=[dict(who=0, text="الزيادة كاملة", at=0.8, bg="green")]),
   dict(k="map", view="south", pins=["Bari", "Palermo"], labels=False, at="شكون كيهمو هادشي؟", until="الحاجة التالتة: الشباب", box=L_BOX),
   dict(k="vs", at="الحاجة التالتة: الشباب", until="الحاجة الرابعة: المدارس", box=WIDE,
        right=dict(title="الضريبة العادية", value="460 €", sub="على 2.000 € زيادة", icon="receipt-tax", color="red"),
        left=dict(title="تحت 30 عام", value="20 €", sub="1% · حتى 2.500 €", icon="user", color="green"), gap=12.0),
   dict(k="icons", at="الحاجة الرابعة: المدارس", until="ومثال باش يوضح: عبد الله", box=(160, 330, 1760, 860), items=[
     ["school", "البلايص فالمدارس", "gold"], ["users", "تقريبا 7.000", "gold"], ["clock", "تحيد ولا تأجل؟", "blue"]], gap=2.5),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="ومثال باش يوضح: عبد الله", until="النصيحة: ما تعطي", box=L_BOX),
   dict(k="people", at="ومثال باش يوضح: عبد الله", until="النصيحة: ما تعطي", box=R_BOX, people=["elder", "man"],
        say=[dict(who=1, text="شفتها فالفيسبوك", at=2.0), dict(who=0, text="باقي مشروع", at=9.0, bg="red")]),
   dict(k="people", at="النصيحة: ما تعطي", box=FULL, people=["clerk", "hijab"],
        say=[dict(who=0, text="ما تعطي حتى وثيقة", at=0.6, bg="red"), dict(who=1, text="غير الإينبس والكاف", at=5.0, bg="green")]),
 ]),
 dict(audio="F.wav", text=T["F"], chapter="05 · مثال: كريم والجنسية", src=S_KAR, items=[
   dict(k="chapter", num="05", title="مثال: كريم والجنسية", at=0.1, until="كريم عندو أربعين عام"),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="كريم عندو أربعين عام", until="الخطوة الأولى: العشر", box=L_BOX),
   dict(k="people", at="كريم عندو أربعين عام", until="الخطوة الأولى: العشر", box=R_BOX, people=["man", "hijab", "child"],
        say=[dict(who=0, text="باغي الجنسية", at=3.0, bg="gold")]),
   dict(k="calendar", at="الخطوة الأولى: العشر", until="الخطوة التانية: المدخول", box=R_BOX, day=10, month="سنين", sub="من الريزيدينسا، ماشي من الدخول"),
   dict(k="steps", at="الخطوة الأولى: العشر", until="الخطوة التانية: المدخول", box=L_BOX, steps=[
     ["الريزيدينسا", "2014"], ["عشر سنين", "2024"], ["دابا", "2026"]], gap=3.0, check_after=0.6),
   dict(k="bars", at="الخطوة التانية: المدخول", until="الخطوة التالتة: السوابق", box=(160, 300, 1760, 840), bars=[
     ["بوحدو", 8263.31, "8.263,31 €", "gold"], ["مع الزوجة", 11362.05, "11.362,05 €", "green"]], gap=4.0),
   dict(k="head", text="أقل مدخول فالعام", at="الخطوة التانية: المدخول", until="الخطوة التالتة: السوابق", sub="فالتلاتة ديال السنين اللي فاتو"),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Casablanca", "Torino"], pins=["Rabat"], labels=False, at="الخطوة التالتة: السوابق", until="الخطوة الرابعة: اللغة", box=L_BOX),
   dict(k="icons", at="الخطوة التالتة: السوابق", until="الخطوة الرابعة: اللغة", box=R_BOX, items=[
     ["file-certificate", "شهادة السوابق", "gold"], ["file-text", "عقد الازدياد", "gold"], ["certificate", "أبوستيل + ترجمة", "green"]], gap=2.0),
   dict(k="vs", at="الخطوة الرابعة: اللغة", until="شنو يدير كريم؟", box=WIDE,
        right=dict(title="اليوم", value="معفي", sub="عندو الكارطا", icon="id", color="green"),
        left=dict(title="إلى ولا قانون", value="B1", sub="غادي يحتاج الشهادة", icon="school", color="red"), gap=6.0),
   dict(k="people", at="شنو يدير كريم؟", until="الخطوة الخامسة: الطلب", box=R_BOX, people=["man"],
        say=[dict(who=0, text="نحضر للامتحان", at=8.0, bg="green")]),
   dict(k="icons", at="شنو يدير كريم؟", until="الخطوة الخامسة: الطلب", box=L_BOX, items=[
     ["school", "Siena · Perugia", "blue"], ["school", "Roma Tre · Dante", "blue"]], gap=20.0),
   dict(k="bars", at="الخطوة الخامسة: الطلب", until="الخطوة السادسة: الوقت", box=(160, 300, 1760, 840), bars=[
     ["الوزارة", 250, "250 €", "gold"], ["التنبر", 16, "16 €", "grey"], ["المجموع", 266, "266 €", "green"]], gap=2.0),
   dict(k="calendar", at="الخطوة السادسة: الوقت", until="الخطوة الأخيرة: اليمين", box=R_BOX, day=15, month=2, sub="فبراير 2029 · أقصى حد 2030"),
   dict(k="people", at="الخطوة السادسة: الوقت", until="الخطوة الأخيرة: اليمين", box=L_BOX, people=["office"],
        say=[dict(who=0, text="بين عامين وتلاتة", at=1.0, bg="gold")]),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="الخطوة الأخيرة: اليمين", until="والأخطاء اللي خاص كريم", box=L_BOX),
   dict(k="calendar", at="الخطوة الأخيرة: اليمين", until="والأخطاء اللي خاص كريم", box=R_BOX, day=6, month="شهور", sub="اليمين فالكومون"),
   dict(k="people", at="والأخطاء اللي خاص كريم", box=FULL, people=["clerk", "man"],
        say=[dict(who=0, text="رد بالك!", at=0.6, bg="red"), dict(who=1, text="الإيميل الجديد", at=8.0, bg="gold")]),
 ]),
 dict(audio="G.wav", text=T["G"], chapter="06 · من المغرب", src=S_MAR, items=[
   dict(k="chapter", num="06", title="من المغرب", at=0.1, until="الخبر الأول: الميزانية"),
   dict(k="map", view="med", hl=["MAR"], pins=["Rabat", "Casablanca"], labels=False, at="الخبر الأول: الميزانية", until="شنو كيعني هادشي؟", box=L_BOX),
   dict(k="bars", at="مية وتسعة وسبعين", until="شنو كيعني هادشي؟", box=R_BOX, bars=[
     ["نعم", 179, "179", "green"], ["لا", 126, "126", "red"]], gap=2.0),
   dict(k="steps", at="شنو كيعني هادشي؟", until="وشنو فيه للمغاربة", box=WIDE, steps=[
     ["مجلس النواب", "14/11"], ["مجلس المستشارين", "2"], ["الجريدة الرسمية", "3"]], gap=3.0, check_after=0.6),
   dict(k="people", at="وشنو فيه للمغاربة", until="ونصيحة: فهاد الفترة", box=FULL, people=["man", "woman"],
        say=[dict(who=0, text="شي حاجة لينا؟", at=0.6), dict(who=1, text="حتى لدابا لا", at=4.0, bg="gold")]),
   dict(k="icons", at="ونصيحة: فهاد الفترة", until="الخبر التاني: تذكير", box=(160, 330, 1760, 860), items=[
     ["file-text", "الجريدة الرسمية", "green"], ["building-bank", "وزارة المالية", "green"], ["receipt-tax", "الضرائب", "green"], ["alert-triangle", "بلا مصدر = لا", "red"]], gap=2.5),
   dict(k="calendar", at="الخبر التاني: تذكير", until="كيفاش كتمشي؟", box=R_BOX, day=9, month=11, sub="الطلب أونلاين"),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Rabat", "Roma"], labels=False, at="الخبر التاني: تذكير", until="كيفاش كتمشي؟", box=L_BOX),
   dict(k="steps", at="كيفاش كتمشي؟", until="علاش هادشي مهم", box=WIDE, steps=[
     ["البوابة ديال البوليس", "1"], ["الهوية إلكترونيا", "2"], ["الخلاص أونلاين", "3"], ["القنصلية", "4"]], gap=2.0, check_after=0.6),
   dict(k="people", at="علاش هادشي مهم", until="ولكن رد بالك: قبل", box=FULL, people=["hijab", "elder"],
        say=[dict(who=1, text="بلا سفر للمغرب", at=6.0, bg="green")]),
   dict(k="people", at="ولكن رد بالك: قبل", until="والثمن والمدة؟", box=R_BOX, people=["office"],
        say=[dict(who=0, text="شنو كتقبلو؟", at=1.0, bg="gold")]),
   dict(k="map", view="italy", pins=["Roma", "Milano"], labels=False, at="ولكن رد بالك: قبل", until="والثمن والمدة؟", box=L_BOX),
   dict(k="head", text="الثمن والمدة: شوف البوابة", at="والثمن والمدة؟", until="ومثال: سميرة", sub="ما عطاوهمش المصادر"),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Bologna", "Casablanca"], labels=False, at="ومثال: سميرة", until="ونصيحة أخيرة", box=L_BOX),
   dict(k="people", at="ومثال: سميرة", until="ونصيحة أخيرة", box=R_BOX, people=["woman"],
        say=[dict(who=0, text="من القنصلية فبولونيا", at=3.0, bg="green")]),
   dict(k="big", text="6", at="ونصيحة أخيرة", y=430, size=280, color=GOLD, sub="شهور · الصلاحية ديال الشهادة"),
 ]),
 dict(audio="H.wav", text=T["H"], chapter="07 · سؤال وجواب", src=S_QA, items=[
   dict(k="chapter", num="07", title="سؤال وجواب", at=0.1, until="السؤال الأول"),
   dict(k="people", at="السؤال الأول", until="السؤال التاني", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="عندي الكارطا، خاصني B1؟", at=0.6), dict(who=1, text="اليوم لا", at=7.0, bg="green")]),
   dict(k="people", at="السؤال التاني", until="السؤال التالت", box=R_BOX, people=["woman", "girl"],
        say=[dict(who=0, text="ولدي قريب للتمنطاش", at=0.6)]),
   dict(k="vs", at="السؤال التاني", until="السؤال التالت", box=L_BOX,
        right=dict(title="تمنطاش", value="18", sub="عام", icon="user", color="gold"),
        left=dict(title="أجل التصريح", value="1", sub="عام", icon="calendar", color="green"), gap=5.0),
   dict(k="map", view="italy", pins=["Milano", "Roma"], labels=False, at="السؤال التالت", until="السؤال الرابع", box=L_BOX),
   dict(k="people", at="السؤال التالت", until="السؤال الرابع", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="التران ديالي نهار السبت", at=0.6)]),
   dict(k="people", at="السؤال الرابع", until="السؤال الخامس", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="خاصني نخلص الأكونطو؟", at=0.6), dict(who=1, text="المعلم كيقتطعو", at=7.0, bg="green")]),
   dict(k="people", at="السؤال الخامس", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="الأسينيو ما دخلش", at=0.6, bg="red")]),
   dict(k="icons", at="السؤال الخامس", box=L_BOX, items=[
     ["clock", "طلب جديد", "gold"], ["file-text", "الإيزي سالا", "red"], ["credit-card", "الإيبان", "red"]], gap=2.0),
 ]),
 dict(audio="H2.wav", text=T["H2"], chapter="07 · سؤال وجواب", src=S_QA, items=[
   dict(k="people", at=0.2, until="سؤال زايد", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="البيرميسو كيسالي فمارس", at=0.6)]),
   dict(k="calendar", at=0.4, until="سؤال زايد", box=L_BOX, day=15, month=12, sub="آخر أجل: 90 يوم قبل 15/3"),
   dict(k="people", at="السؤال السابع", until="السؤال التامن", box=FULL, people=["elder", "man"],
        say=[dict(who=1, text="الواليد كبير فالعمر", at=0.4), dict(who=0, text="باقي مشروع", at=4.0, bg="red")]),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Casablanca", "Milano"], labels=False, at="السؤال التامن", until="السؤال التاسع", box=L_BOX),
   dict(k="vs", at="السؤال التامن", until="السؤال التاسع", box=R_BOX,
        right=dict(title="صالح", value="1", sub="عام من الريزيدينسا", icon="license", color="gold"),
        left=dict(title="بلا امتحان", value="6", sub="سنين أقل", icon="license", color="green"), gap=6.0),
   dict(k="calendar", at="السؤال التاسع", until="السؤال العاشر", box=R_BOX, day=31, month=12, sub="الإيزي كيسالي"),
   dict(k="people", at="السؤال التاسع", until="السؤال العاشر", box=L_BOX, people=["woman"],
        say=[dict(who=0, text="قبل آخر فبراير", at=6.0, bg="green")]),
   dict(k="people", at="السؤال العاشر", until="والسؤال الأخير", box=R_BOX, people=["girl"],
        say=[dict(who=0, text="نرجع التيليفون؟", at=0.6)]),
   dict(k="icons", at="السؤال العاشر", until="والسؤال الأخير", box=L_BOX, items=[
     ["calendar", "أونلاين: 14 يوم", "green"], ["building-store", "الحانوت: لا", "red"], ["certificate", "الضمان: 2 سنين", "gold"]], gap=4.0),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Milano", "Casablanca"], labels=False, at="سؤال زايد", until="السؤال السابع", box=L_BOX),
   dict(k="icons", at="سؤال زايد", until="السؤال السابع", box=R_BOX, items=[
     ["e-passport", "الباسبور", "green"], ["id", "البيرميسو القديم", "green"], ["receipt", "الريسيفوتا", "green"], ["plane", "طيارة مباشرة", "gold"]], gap=2.0),
   dict(k="people", at="والسؤال الأخير", box=FULL, people=["man", "office"],
        say=[dict(who=0, text="شحال الثمن؟", at=0.6), dict(who=1, text="شوف البوابة", at=4.0, bg="gold")]),
 ]),
 dict(audio="I.wav", text=T["I"], chapter="08 · الخلاصة والتواريخ", src=S_HOME, items=[
   dict(k="chapter", num="08", title="الخلاصة والتواريخ", at=0.1, until="نعاودو ليك المهم"),
   dict(k="people", at="نعاودو ليك المهم", until="واحد: الجنسية", box=FULL, people=["hijab", "worker"],
        say=[dict(who=1, text="عاود ليا المهم", at=0.6)]),
   dict(k="rows", at="واحد: الجنسية", until="النصيحة الكبيرة", y=250, gap=112, size=48, rows=[
     ("الجنسية: مشروع", "B1", "واحد: الجنسية"),
     ("الإضراب", "20-21/11", "جوج: الإضراب"),
     ("الأكونطو", "30/11", "تلاتة: الضرائب"),
     ("الميزانية ديال إيطاليا", "31/12", "ربعة: الميزانية"),
     ("من المغرب", "179-126", "خمسة: من المغرب"),
   ]),
   dict(k="vs", at="النصيحة الكبيرة", until="وها هي التواريخ", box=WIDE,
        right=dict(title="مشروع", value="تسنى", sub="باقي ما تقرر", icon="clock", color="grey"),
        left=dict(title="قانون", value="دير", sub="90 يوم · 30/11", icon="check", color="green"), gap=5.0),
   dict(k="steps", at="وها هي التواريخ", until="ودابا، سؤال ليك", box=(260, 170, 1660, 870), steps=[
     ["الأسينيو أونيكو", "19-20/11"], ["الإضراب", "20-21/11"], ["البلاك فرايدي", "27/11"], ["الأكونطو", "30/11"], ["البانسيون", "1/12"], ["الإيمو والأسينيو", "16/12"]], gap=2.2, check_after=0.6),
   dict(k="map", view="med", hl=["ITA", "MAR"], pins=["Milano", "Casablanca"], labels=False, at="ودابا، سؤال ليك", until="وإلى عرفتي شي واحد", box=L_BOX),
   dict(k="people", at="ودابا، سؤال ليك", until="وإلى عرفتي شي واحد", box=R_BOX, people=["woman", "worker"],
        say=[dict(who=0, text="كتب لينا فالكومونتير", at=3.0, bg="green")]),
   dict(k="people", at="وإلى عرفتي شي واحد", until="وإلى عجبك هاد العمل", box=FULL, people=["man", "hijab"],
        say=[dict(who=0, text="صيفطو لصاحبك", at=1.0, bg="gold")]),
   dict(k="cta", at="وإلى عجبك هاد العمل", text="ابوني فالقناة", sub="كل نهار خبر مفيد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("الجنسية: الكارطا ما بقاتش كافية؟", (236, 196, 96)), "إضراب التران: الجمعة والسبت", "الأكونطو قبل 30 نونبر"],
  num="B1", numsub="مشروع قانون · باقي ما ولاش قانون",
  bottom="مغاربة إيطاليا · خبار مفيدة بالدارجة",
)
