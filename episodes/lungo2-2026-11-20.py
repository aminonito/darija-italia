import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-20.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo2-2026-11-20-final")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = {k: v.replace("گ", "ك") for k, v in JOB["blocks"].items()}

S_HOME = "مغاربة إيطاليا · دليل عملي بالدارجة"
S_REQ = "L. 91/1992 art. 5-6 · Prefettura istruzioni cittadinanza · Studio Cataldi · LeggeInChiaro"
S_DOC = "Prefettura istruzioni cittadinanza · Boccadutri · ilDiritto · InfoImmigrazione"
S_MAR = "Prefettura istruzioni · Prefettura tabella legalizzazioni · Boccadutri · InfoImmigrazione"
S_STEP = "Studio Cataldi · Boccadutri · ilDiritto · Prefettura istruzioni cittadinanza"
S_CASI = "Corte cost. 195/2022 · Boccadutri · Prefettura · Camera A.C. 2124-A"
S_ERR = "Prefettura istruzioni · InfoImmigrazione · LeggeInChiaro art. 6"
S_QA = "Fonti dei capitoli 01-07"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850); FULL = (160, 300, 1760, 860); MID = (260, 220, 1660, 840)
ICB = (160, 330, 1760, 860); VSB = (260, 220, 1660, 820); BARB = (160, 330, 1760, 840)

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="01 · شكون كيحتاج هاد الدليل", src=S_HOME, items=[
   dict(k="head", text="الجنسية الإيطالية بالزواج", at=0.2, until="قبل ما نبداو", sub="الشروط والوراق والثمن والمدة · خطوة بخطوة"),
   dict(k="people", at=0.8, until="قبل ما نبداو", box=FULL, people=["hijab", "man", "woman"],
        say=[dict(who=0, text="إمتى نقدر نطلب؟", at=2.0), dict(who=1, text="شحال كنخلص؟", at=6.0, bg="gold")]),
   dict(k="vs", at="قبل ما نبداو", until="خلينا نعرفو تلاتة", box=VSB,
        right=dict(title="بالإقامة", value="10", sub="سنين · دليل آخر", icon="home", color="grey"),
        left=dict(title="بالزواج", value="اليوم", sub="هاد الدليل", icon="users", color="green"), gap=3.0),
   dict(k="map", view="med", hl=["ITA", "MAR"], pins=["Torino", "Bologna", "Casablanca"], labels=False,
        at="خلينا نعرفو تلاتة", until="الأولى، نادية", box=(160, 200, 1760, 880)),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="الأولى، نادية", until="التاني، يوسف", box=L_BOX),
   dict(k="people", at="الأولى، نادية", until="التاني، يوسف", box=R_BOX, people=["hijab", "man"],
        say=[dict(who=0, text="تزوجت فتورينو", at=3.0, bg="green"), dict(who=0, text="إمتى نطلب؟", at=14.0, bg="gold")]),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Fes", "Bologna", "plane"], pins=["Fes", "Bologna"], labels=False,
        at="التاني، يوسف", until="والتالتة، سلمى", box=L_BOX),
   dict(k="people", at="التاني، يوسف", until="والتالتة، سلمى", box=R_BOX, people=["worker", "woman"],
        say=[dict(who=0, text="تزوجنا ففاس", at=3.0), dict(who=0, text="واش كيتحسب؟", at=10.0, bg="gold")]),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Casablanca"], labels=False, at="والتالتة، سلمى", until="علاش هاد التلاتة؟", box=L_BOX),
   dict(k="people", at="والتالتة، سلمى", until="علاش هاد التلاتة؟", box=R_BOX, people=["girl", "man"],
        say=[dict(who=0, text="وأنا فالمغرب؟", at=8.0, bg="gold")]),
   dict(k="steps", at="علاش هاد التلاتة؟", until="كل واحد فيهم", box=MID, steps=[
     ["نادية · تزوجات فإيطاليا", "1"], ["يوسف · تزوج فالمغرب", "2"], ["سلمى · عايشة فالمغرب", "3"]], gap=2.5, check_after=0.6),
   dict(k="people", at="كل واحد فيهم", until="فهاد الفيديو غادي", box=FULL, people=["hijab", "worker", "girl"],
        say=[dict(who=1, text="بالأرقام والتواريخ", at=1.5, bg="green")]),
   dict(k="rows", at="فهاد الفيديو غادي", until="وكل رقم فهاد الفيديو", y=215, gap=78, size=40, rows=[
     ("شكون خاصو هاد الطريق", "01", "الأول، شكون"),
     ("الشروط بالتفصيل", "02", "التاني، الشروط"),
     ("الوراق من إيطاليا", "03", "التالت، الوراق"),
     ("الوراق من المغرب", "04", "الرابع، الوراق"),
     ("الخطوات والثمن والمدة", "05", "الخامس، الخطوات"),
     ("الحالات الخاصة", "06", "السادس، الحالات"),
     ("الأخطاء والرفض", "07", "السابع، الأخطاء"),
     ("سؤال وجواب", "08", "التامن، سؤال"),
     ("اللائحة النهائية", "09", "والتاسع، لائحة"),
   ]),
   dict(k="icons", at="وكل رقم فهاد الفيديو", until="وعلاش هاد الموضوع مهم؟", box=ICB, items=[
     ["file-certificate", "جوج مصادر", "blue"], ["calculator", "أمثلة بالحساب", "green"], ["scale", "ماشي استشارة قانونية", "gold"]], gap=3.0),
   dict(k="bars", at="وعلاش هاد الموضوع مهم؟", until="والجنسية الإيطالية كتعطيك", box=BARB, bars=[
     ["بالإقامة", 10, "10", "grey"], ["بالزواج فإيطاليا", 2, "2", "green"]], gap=1.5),
   dict(k="text", text="السنين ديال الإقامة", at="وعلاش هاد الموضوع مهم؟", until="والجنسية الإيطالية كتعطيك", y=880, size=46, color=GREY),
   dict(k="icons", at="والجنسية الإيطالية كتعطيك", until="الطريق كاملة كتبدا", box=ICB, items=[
     ["e-passport", "الباسبور الإيطالي", "blue"], ["plane", "السفر فأوروبا", "green"], ["briefcase", "الخدمة فأوروبا", "gold"]], gap=1.8),
   dict(k="people", at="الطريق كاملة كتبدا", box=FULL, people=["clerk", "hijab"],
        say=[dict(who=0, text="البورطال ثم الكومون", at=1.0, bg="green"), dict(who=1, text="يلاه نبداو!", at=7.0)]),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="02 · الشروط بالتفصيل", src=S_REQ, items=[
   dict(k="chapter", num="02", title="الشروط بالتفصيل", at=0.1, until="القانون الإيطالي ديال الجنسية"),
   dict(k="icons", at="القانون الإيطالي ديال الجنسية", until="الشرط الأول", box=ICB, items=[
     ["scale", "القانون 91/1992", "blue"], ["file-text", "المادة 5", "gold"]], gap=2.0),
   dict(k="people", at="الشرط الأول", until="الشرط التاني: المدة", box=FULL, people=["hijab", "man"],
        say=[dict(who=1, text="أنا إيطالي", at=1.0, bg="green"), dict(who=0, text="الزواج مسجل", at=3.5, bg="green")]),
   dict(k="vs", at="الشرط التاني: المدة", until="الإقامة القانونية معناها", box=VSB,
        right=dict(title="فإيطاليا", value="2", sub="سنين ديال الإقامة", icon="home", color="green"),
        left=dict(title="برا إيطاليا", value="3", sub="سنين ديال الزواج", icon="world", color="gold"), gap=5.0),
   dict(k="icons", at="الإقامة القانونية معناها", until="والبريفيتورا كتحسب", box=ICB, items=[
     ["e-passport", "البيرميسو صالح", "green"], ["home", "الريزيدينسا", "blue"], ["file-text", "مسجل فالوراق", "gold"]], gap=2.0),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="والبريفيتورا كتحسب", until="إلى كنتي عايش برا", box=L_BOX),
   dict(k="people", at="والبريفيتورا كتحسب", until="إلى كنتي عايش برا", box=R_BOX, people=["clerk"],
        say=[dict(who=0, text="من نهار التسجيل", at=1.5, bg="gold")]),
   dict(k="bars", at="وهنا خبر مزيان", until="خلينا نحسبو مع نادية", box=BARB, bars=[
     ["فإيطاليا", 12, "12", "green"], ["برا إيطاليا", 18, "18", "gold"]], gap=2.0),
   dict(k="text", text="شهور · المدة مع الولاد", at="يعني فإيطاليا عام", until="خلينا نحسبو مع نادية", y=880, size=46, color=GREY),
   dict(k="calendar", at="خلينا نحسبو مع نادية", until="زيد جوج سنين", box=R_BOX, day=15, month=3, sub="2025 · التسجيل فتورينو"),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="خلينا نحسبو مع نادية", until="ولكن إلى تزاد ليهم", box=L_BOX),
   dict(k="calendar", at="زيد جوج سنين", until="ولكن إلى تزاد ليهم", box=R_BOX, day=15, month=3, sub="2027 · تقدر تطلب"),
   dict(k="vs", at="ولكن إلى تزاد ليهم", until="الشرط التالت", box=VSB,
        right=dict(title="بلا ولاد", value="15/3/2027", sub="", icon="calendar", color="gold"),
        left=dict(title="مع ولد", value="15/3/2026", sub="فاتت · تقدر دابا", icon="heart", color="green"), gap=3.0),
   dict(k="people", at="الشرط التالت", until="الشرط الرابع", box=FULL, people=["woman", "man"],
        say=[dict(who=0, text="بلا طلاق", at=1.5, bg="red"), dict(who=1, text="حتى للديكري", at=9.0, bg="gold")]),
   dict(k="icons", at="الشرط الرابع", until="الشرط الخامس", box=ICB, items=[
     ["school", "الإيطالية B1", "green"], ["certificate", "معهد معترف بيه", "blue"]], gap=2.0),
   dict(k="steps", at="الشرط الخامس", until="ولكن رد البال", box=MID, steps=[
     ["جرائم ضد الدولة", "1"], ["جريمة عمدية: الحد الأقصى 3 سنين", "2"], ["عقوبة من برا: كثر من عام", "3"], ["الأمن ديال الدولة", "4"]], gap=4.0, check_after=0.6),
   dict(k="people", at="ولكن رد البال", until="وشنو اللي ما كاينش؟", box=FULL, people=["clerk", "man"],
        say=[dict(who=0, text="رد الاعتبار", at=1.0, bg="green"), dict(who=1, text="القضية باقة؟", at=7.0, bg="gold")]),
   dict(k="vs", at="وشنو اللي ما كاينش؟", until="ملخص الشروط", box=VSB,
        right=dict(title="بالإقامة", value="الدخل", sub="3 سنين", icon="report-money", color="grey"),
        left=dict(title="بالزواج", value="بلا دخل", sub="ما كاينش هاد الشرط", icon="users", color="green"), gap=2.5),
   dict(k="icons", at="ملخص الشروط", box=ICB, items=[
     ["users", "الزواج مسجل", "green"], ["calendar", "المدة", "gold"], ["school", "اللغة", "blue"], ["id", "السوابق", "red"]], gap=1.5),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="03 · الوراق من إيطاليا", src=S_DOC, items=[
   dict(k="chapter", num="03", title="الوراق من إيطاليا", at=0.1, until="من دجنبر"),
   dict(k="calendar", at="من دجنبر", until="كاين ربعة ديال الطرق", box=R_BOX, day=4, month=12, sub="2018 · B1 واجب"),
   dict(k="people", at="من دجنبر", until="كاين ربعة ديال الطرق", box=L_BOX, people=["student"],
        say=[dict(who=0, text="بلاها ما كيتقبلش", at=3.0, bg="red")]),
   dict(k="steps", at="كاين ربعة ديال الطرق", until="الطريق الأولى", box=MID, steps=[
     ["شهادة B1 من معهد", "1"], ["القراية فإيطاليا", "2"], ["الكارطا", "3"], ["عقد الاندماج", "4"]], gap=0.6, check_after=0.6),
   dict(k="map", view="italy", pins=["Roma", "Perugia", "Firenze"], labels=False, at="الطريق الأولى", until="الطريق التانية", box=L_BOX),
   dict(k="icons", at="الطريق الأولى", until="الطريق التانية", box=R_BOX, items=[
     ["school", "سيينا", "green"], ["school", "بيروجا", "blue"], ["school", "روما تري", "gold"], ["school", "دانتي أليغييري", "green"]], gap=1.5),
   dict(k="icons", at="الطريق التانية", until="ولكن رد البال", box=ICB, items=[
     ["school", "القراية فإيطاليا", "green"], ["e-passport", "الكارطا", "blue"], ["file-text", "عقد الاندماج", "gold"]], gap=5.0),
   dict(k="people", at="ولكن رد البال", until="ويوسف دار كورس", box=FULL, people=["hijab", "worker"],
        say=[dict(who=0, text="بيرميسو العائلة؟", at=1.0, bg="gold"), dict(who=1, text="ما كيعفيكش", at=3.0, bg="red")]),
   dict(k="map", view="north", pins=["Bologna"], labels=False, at="ويوسف دار كورس", until="نصيحة: سجل", box=L_BOX),
   dict(k="people", at="ويوسف دار كورس", until="نصيحة: سجل", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="الكورس ما كافيش", at=3.0, bg="red")]),
   dict(k="warn", text="سجل فالامتحان بكري: الشهادة خاصها تكون عندك نهار الطلب", at="نصيحة: سجل", until="الوثيقة التانية", y=880),
   dict(k="icons", at="الوثيقة التانية", until="الوثيقة الخامسة", box=ICB, items=[
     ["e-passport", "البيرميسو ولا الكارطا", "green"], ["id", "نسخة الباسبور", "blue"], ["file-text", "عقد الزواج من برا", "gold"]], gap=4.0),
   dict(k="bars", at="الوثيقة الخامسة", until="هادشي ماشي هو كلشي", box=BARB, bars=[
     ["المساهمة", 250, "250 €", "gold"], ["التامبر", 16, "16 €", "blue"], ["المجموع", 266, "266 €", "green"]], gap=4.0),
   dict(k="icons", at="هادشي ماشي هو كلشي", until="الوثيقة السادسة", box=ICB, items=[
     ["file-text", "الترجمة", "blue"], ["certificate", "الأبوستيل", "gold"], ["school", "الامتحان", "green"]], gap=1.5),
   dict(k="text", text="كيتخلصو بوحدهم · الثمن كيتبدل", at="والثمن ديالهم", until="الوثيقة السادسة", y=880, size=46, color=GREY),
   dict(k="people", at="الوثيقة السادسة", until="وكيفاش كتصيفط الوراق؟", box=FULL, people=["office", "hijab"],
        say=[dict(who=0, text="غير على الأنترنيت", at=2.0, bg="gold"), dict(who=1, text="عندي السبيد", at=7.0, bg="green")]),
   dict(k="vs", at="وكيفاش كتصيفط الوراق؟", until="خلينا نجمعو", box=VSB,
        right=dict(title="التيليفون", value="لا", sub="تصويرة", icon="phone", color="red"),
        left=dict(title="السكانير", value="إيه", sub="ملف واحد كامل", icon="file-text", color="green"), gap=2.5),
   dict(k="icons", at="خلينا نجمعو", until="ونادية؟", box=ICB, items=[
     ["school", "اللغة", "green"], ["e-passport", "البيرميسو", "blue"], ["coin-euro", "266 €", "gold"], ["key", "السبيد", "green"]], gap=1.5),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="ونادية؟", box=L_BOX),
   dict(k="people", at="ونادية؟", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="باقي غير اللغة", at=4.0, bg="gold"), dict(who=0, text="نسجل دابا", at=10.0, bg="green")]),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="04 · الوراق من المغرب", src=S_MAR, items=[
   dict(k="chapter", num="04", title="الوراق من المغرب", at=0.1, until="الوثيقة الأولى"),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Casablanca", "Torino", "plane"], pins=["Casablanca", "Torino"], labels=False,
        at="الوثيقة الأولى", until="خاصو يكون فيه", box=(160, 200, 1760, 880)),
   dict(k="icons", at="خاصو يكون فيه", until="الوثيقة التانية", box=ICB, items=[
     ["file-certificate", "عقد الازدياد الكامل", "green"], ["users", "الأب والأم", "blue"], ["x", "ماشي المختصر", "red"]], gap=2.5),
   dict(k="people", at="الوثيقة التانية", until="وهنا حاجة مهمة بزاف", box=FULL, people=["clerk", "man"],
        say=[dict(who=0, text="السوابق ديال المغرب", at=1.5), dict(who=1, text="وسكنت فإسبانيا", at=6.0, bg="gold")]),
   dict(k="big", text="6", at="وهنا حاجة مهمة بزاف", until="خلينا نحسبو", y=430, size=300, color=RED, sub="شهور · من نهار خرجات الشهادة"),
   dict(k="calendar", at="خلينا نحسبو", until="كتبقى صالحة", box=R_BOX, day=1, month=2, sub="2027 · خرجات الشهادة"),
   dict(k="people", at="خلينا نحسبو", until="والنصيحة: طلب", box=L_BOX, people=["hijab"],
        say=[dict(who=0, text="نحسبو مزيان", at=1.0, bg="gold")]),
   dict(k="calendar", at="كتبقى صالحة", until="والنصيحة: طلب", box=R_BOX, day=1, month=8, sub="2027 · آخر نهار"),
   dict(k="steps", at="والنصيحة: طلب", until="ودابا الأبوستيل", box=MID, steps=[
     ["الوراق الآخرين", "1"], ["شهادة السوابق فالآخر", "2"], ["الطلب دغيا", "3"]], gap=3.0, check_after=0.6),
   dict(k="calendar", at="ودابا الأبوستيل", until="الأبوستيل هو واحد", box=R_BOX, day=14, month=8, sub="2016 · الأبوستيل مع إيطاليا"),
   dict(k="map", view="med", hl=["ITA", "MAR"], pins=["Rabat", "Roma"], labels=False, at="ودابا الأبوستيل", until="الأبوستيل هو واحد", box=L_BOX),
   dict(k="vs", at="الأبوستيل هو واحد", until="ومن بعد الأبوستيل", box=VSB,
        right=dict(title="قبل", value="التصديق", sub="القنصلية", icon="building-bank", color="grey"),
        left=dict(title="دابا", value="أبوستيل", sub="فالمغرب", icon="certificate", color="green"), gap=2.5),
   dict(k="vs", at="ومن بعد الأبوستيل", until="الوثيقة التالتة", box=VSB,
        right=dict(title="فالمغرب", value="مترجم", sub="محلف", icon="file-text", color="blue"),
        left=dict(title="فإيطاليا", value="محلفة", sub="فالمحكمة", icon="scale", color="gold"), gap=4.0),
   dict(k="text", text="سول البريفيتورا ديالك قبل ما تخلص", at="قبل ما تخلص الترجمة", until="الوثيقة التالتة", y=880, size=46, color=GOLD),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Fes", "Bologna", "plane"], pins=["Fes", "Bologna"], labels=False,
        at="الوثيقة التالتة", until="ورد البال: المدة", box=L_BOX),
   dict(k="people", at="الوثيقة التالتة", until="ورد البال: المدة", box=R_BOX, people=["worker", "woman"],
        say=[dict(who=0, text="تزوجنا عند العدول", at=4.0), dict(who=1, text="نسجلوه فالكومون", at=12.0, bg="green")]),
   dict(k="vs", at="ورد البال: المدة", until="إذن إلى كنتي تزوجتي", box=VSB,
        right=dict(title="العرس", value="2023", sub="ما كيتحسبش", icon="calendar", color="grey"),
        left=dict(title="التسجيل فالكومون", value="2025", sub="من هنا كتحسب", icon="home", color="green"), gap=3.0),
      dict(k="warn", text="تزوجتي فالمغرب؟ سجل الزواج فالكومون اليوم", at="إذن إلى كنتي تزوجتي", until="وحتى يوسف", y=880),
   dict(k="people", at="وحتى يوسف", until="وحالة أخيرة", box=FULL, people=["worker", "clerk"],
        say=[dict(who=1, text="سول وتأكد", at=4.0, bg="gold")]),
   dict(k="icons", at="وحالة أخيرة", box=ICB, items=[
     ["id", "السمية فالمغرب", "blue"], ["e-passport", "السمية فالباسبور", "gold"], ["file-text", "وثيقة كتشرح", "green"]], gap=2.0),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="05 · الخطوات والثمن والمدة", src=S_STEP, items=[
   dict(k="chapter", num="05", title="الخطوات والثمن والمدة", at=0.1, until="الخطوة الأولى"),
   dict(k="people", at="الخطوة الأولى", until="الخطوة التانية", box=FULL, people=["office", "man"],
        say=[dict(who=0, text="الزواج، ماشي الإقامة", at=4.0, bg="gold"), dict(who=1, text="النوع الغلط!", at=9.0, bg="red")]),
   dict(k="steps", at="الخطوة التانية", until="ومن بعد؟", box=MID, steps=[
     ["البورطال بالسبيد", "1"], ["الاستمارة", "2"], ["الوراق المسكانيين", "3"], ["الخلاص 266 €", "4"], ["الإرسال والوصل", "5"]], gap=6.0, check_after=0.6),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="ومن بعد؟", until="ونصيحة: دير ملف", box=L_BOX),
   dict(k="people", at="ومن بعد؟", until="ونصيحة: دير ملف", box=R_BOX, people=["clerk"],
        say=[dict(who=0, text="ناقصاك وثيقة", at=6.0, bg="gold")]),
   dict(k="icons", at="ونصيحة: دير ملف", until="وشحال ديال الوقت؟", box=ICB, items=[
     ["receipt", "الوصل", "blue"], ["coin-euro", "الخلاصات", "gold"], ["clipboard-check", "رقم الملف", "green"]], gap=2.0),
   dict(k="bars", at="وشحال ديال الوقت؟", until="خلينا نحسبو مع نادية", box=BARB, bars=[
     ["عادة", 24, "24", "green"], ["أقصى حد", 36, "36", "gold"]], gap=2.5),
   dict(k="text", text="شهر للجواب", at="وتقدر تزيد", until="خلينا نحسبو مع نادية", y=880, size=46, color=GREY),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="خلينا نحسبو مع نادية", until="وشي مصادر كتقول", box=L_BOX),
   dict(k="steps", at="خلينا نحسبو مع نادية", until="وشي مصادر كتقول", box=R_BOX, steps=[
     ["الطلب", "1/4/2027"], ["عادة قبل", "1/4/2029"], ["أقصى حد", "1/4/2030"]], gap=4.0, check_after=0.6),
   dict(k="warn", text="ملف كامل من الأول كيربحك الوقت", at="وشي مصادر كتقول", until="وفهاد المدة", y=880),
   dict(k="people", at="وفهاد المدة", until="الخطوة السادسة", box=FULL, people=["hijab", "clerk"],
        say=[dict(who=0, text="جددت البيرميسو", at=3.0, bg="green"), dict(who=1, text="العنوان الجديد؟", at=7.0, bg="gold")]),
   dict(k="icons", at="الخطوة السادسة", until="الخطوة السابعة", box=ICB, items=[
     ["home", "الريزيدينسا", "blue"], ["users", "الزواج", "green"], ["id", "السوابق", "gold"]], gap=3.0),
   dict(k="calendar", at="الخطوة السابعة", until="إلى نوتيفيكا", box=R_BOX, day=6, month="شهور", sub="من النوتيفيكا للحلفان"),
   dict(k="people", at="الخطوة السابعة", until="إلى نوتيفيكا", box=L_BOX, people=["man"],
        say=[dict(who=0, text="نحلف فالكومون", at=4.0, bg="green")]),
   dict(k="vs", at="إلى نوتيفيكا", until="خود موعد", box=VSB,
        right=dict(title="النوتيفيكا", value="10/2/2029", sub="", icon="mail", color="blue"),
        left=dict(title="الحلفان قبل", value="10/8/2029", sub="", icon="calendar", color="red"), gap=3.0),
   dict(k="warn", text="ما حلفتيش فالوقت؟ الديكري كيطيح", at="إلى ما حلفتيش", until="ومن بعد الحلفان", y=880),
   dict(k="icons", at="ومن بعد الحلفان", until="الملخص ديال الفلوس", box=ICB, items=[
     ["id", "الكارطا الإيطالية", "green"], ["e-passport", "الباسبور الإيطالي", "blue"]], gap=2.0),
   dict(k="rows", at="الملخص ديال الفلوس", y=300, gap=110, size=46, rows=[
     ("للدولة", "266 €", "الملخص ديال الفلوس"),
     ("الإقامة من التسجيل", "2", "والملخص ديال الوقت"),
     ("الجواب عادة بالشهور", "24", "من بعد حتى"),
     ("أقصى حد بالشهور", "36", "ولا ستة وتلاتين،"),
     ("الحلفان بالشهور", "6", "ومن بعد ستة"),
   ]),
 ]),
 dict(audio="F.wav", text=T["F"], chapter="06 · الحالات الخاصة", src=S_CASI, items=[
   dict(k="chapter", num="06", title="الحالات الخاصة", at=0.1, until="واش تقدر تطلب الجنسية؟"),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Casablanca", "Roma", "plane"], pins=["Casablanca", "Roma"], labels=False,
        at="واش تقدر تطلب الجنسية؟", until="سلمى تزوجات بكريم", box=L_BOX),
   dict(k="people", at="واش تقدر تطلب الجنسية؟", until="سلمى تزوجات بكريم", box=R_BOX, people=["girl", "clerk"],
        say=[dict(who=1, text="القنصلية الإيطالية", at=8.0, bg="green")]),
   dict(k="calendar", at="سلمى تزوجات بكريم", until="زيد تلاتة", box=R_BOX, day=10, month=6, sub="2024 · الزواج"),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Casablanca"], labels=False, at="سلمى تزوجات بكريم", until="ولكن سلمى وكريم", box=L_BOX),
   dict(k="calendar", at="زيد تلاتة", until="ولكن سلمى وكريم", box=R_BOX, day=10, month=6, sub="2027 · بلا ولاد"),
   dict(k="vs", at="ولكن سلمى وكريم", until="وشرط واحد", box=VSB,
        right=dict(title="بلا ولاد", value="10/6/2027", sub="3 سنين", icon="calendar", color="gold"),
        left=dict(title="مع ولد", value="10/12/2025", sub="فاتت · تقدر دابا", icon="heart", color="green"), gap=3.0),
   dict(k="icons", at="وشرط واحد", until="الحالة التانية", box=ICB, items=[
     ["file-text", "الزواج مسجل", "blue"], ["school", "شهادة اللغة", "green"]], gap=2.0),
   dict(k="people", at="الحالة التانية", until="قبل، كانت الوفاة", box=FULL, people=["elder", "hijab"],
        say=[dict(who=1, text="الله يرحم الجميع", at=3.0)]),
   dict(k="vs", at="قبل، كانت الوفاة", until="إذن إلى كان الطلب", box=VSB,
        right=dict(title="قبل", value="كيتوقف", sub="", icon="x", color="red"),
        left=dict(title="من 2022", value="كمل", sub="الحكم 195/2022", icon="scale", color="green"), gap=4.0),
   dict(k="people", at="الحالة التالتة", until="الحالة الرابعة", box=FULL, people=["woman", "man"],
        say=[dict(who=0, text="قبل الديكري؟", at=1.5, bg="red"), dict(who=1, text="سول محامي", at=7.0, bg="gold")]),
   dict(k="steps", at="الحالة الرابعة", until="الحالة الخامسة", box=MID, steps=[
     ["الزواج", "1"], ["ولا إيطالي", "2"], ["المدة كتبدا من هنا", "3"]], gap=4.0, check_after=0.6),
   dict(k="map", view="med", hl=["ITA", "MAR"], pins=["Rabat", "Roma"], labels=False, at="الحالة الخامسة", until="والولاد اللي عندهم", box=L_BOX),
   dict(k="people", at="الحالة الخامسة", until="والولاد اللي عندهم", box=R_BOX, people=["man"],
        say=[dict(who=0, text="نخسر المغربية؟", at=1.0, bg="gold")]),
   dict(k="icons", at="والولاد اللي عندهم", until="الحالة السادسة", box=ICB, items=[
     ["users", "أب ولا أم إيطالية", "blue"], ["heart", "إيطاليين من الزيادة", "green"]], gap=2.0),
   dict(k="vs", at="الحالة السادسة", until="هاد المشروع باقي", box=VSB,
        right=dict(title="اليوم", value="معفي", sub="مع الكارطا", icon="e-passport", color="green"),
        left=dict(title="المشروع", value="B1", sub="ماشي قانون باقي", icon="school", color="gold"), gap=4.0),
   dict(k="icons", at="هاد المشروع باقي", until="ولكن النصيحة", box=ICB, items=[
     ["clipboard-check", "اللجنة: داز", "green"], ["scale", "مجلس النواب: باقي", "gold"], ["building-bank", "مجلس الشيوخ: باقي", "gold"]], gap=2.5),
   dict(k="text", text="دوز الامتحان على كل حال", at="ولكن النصيحة", until="الحالة السابعة", y=640, size=64, color=GOLD),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Fes", "Bologna", "plane"], pins=["Fes", "Bologna"], labels=False,
        at="الحالة السابعة", box=L_BOX),
   dict(k="people", at="الحالة السابعة", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="بيرميسو العائلة", at=4.0, bg="green")]),
 ]),
 dict(audio="G.wav", text=T["G"], chapter="07 · الأخطاء والرفض", src=S_ERR, items=[
   dict(k="chapter", num="07", title="الأخطاء والرفض", at=0.1, until="الغلطة الأولى"),
   dict(k="people", at="الغلطة الأولى", until="الغلطة التانية", box=FULL, people=["worker", "clerk"],
        say=[dict(who=0, text="من نهار العرس؟", at=1.0, bg="gold"), dict(who=1, text="من التسجيل!", at=6.0, bg="red")]),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Casablanca", "Milano", "plane"], pins=["Casablanca", "Milano"], labels=False,
        at="الغلطة التانية", until="بزاف ديال الناس كيجيبو", box=(160, 200, 1760, 880)),
   dict(k="vs", at="بزاف ديال الناس كيجيبو", until="الغلطة التالتة", box=VSB,
        right=dict(title="الصيف", value="الشهادة", sub="", icon="calendar", color="green"),
        left=dict(title="الشتا", value="ماتت", sub="كثر من 6 شهور", icon="x", color="red"), gap=4.0),
   dict(k="icons", at="الغلطة التالتة", until="الغلطة الخامسة", box=ICB, items=[
     ["certificate", "بلا أبوستيل", "red"], ["file-text", "بلا ترجمة", "red"], ["school", "بلا B1", "red"]], gap=4.0),
   dict(k="people", at="الغلطة الخامسة", until="الغلطة السادسة", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="سكنت فإسبانيا", at=1.5), dict(who=1, text="السوابق ديالها؟", at=4.0, bg="gold")]),
   dict(k="icons", at="الغلطة السادسة", until="الغلطة التامنة", box=ICB, items=[
     ["x", "النوع الغلط", "red"], ["phone", "الوراق بالتيليفون", "red"]], gap=4.0),
   dict(k="icons", at="الغلطة التامنة", until="والغلطة الحضاش", box=ICB, items=[
     ["mail", "العنوان القديم", "red"], ["e-passport", "البيرميسو مات", "red"], ["calendar", "الحلفان فات", "red"]], gap=4.0),
   dict(k="warn", text="زواج غير على الوراق = الرفض ومشاكل قانونية", at="والغلطة الحضاش", until="ودابا، شنو تدير", y=880),
   dict(k="people", at="ودابا، شنو تدير", until="الحالة التانية: فاتت", box=FULL, people=["hijab", "clerk"],
        say=[dict(who=1, text="ناقصاك وثيقة", at=3.0, bg="gold"), dict(who=0, text="نصيفطها دابا", at=6.0, bg="green")]),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="الحالة التانية: فاتت", until="الحالة التالتة: وصلاتك", box=L_BOX),
   dict(k="steps", at="الحالة التانية: فاتت", until="الحالة التالتة: وصلاتك", box=R_BOX, steps=[
     ["البورطال", "1"], ["تذكير", "2"], ["المحكمة الإدارية", "3"]], gap=3.0, check_after=0.6),
   dict(k="people", at="الحالة التالتة: وصلاتك", until="الحالة الرابعة: الرفض", box=FULL, people=["man", "office"],
        say=[dict(who=0, text="جات رسالة!", at=1.5, bg="gold"), dict(who=1, text="جاوب فالوقت", at=9.0, bg="green")]),
   dict(k="vs", at="الحالة الرابعة: الرفض", until="وإلى كان الرفض بسبب", box=VSB,
        right=dict(title="الطعن", value="التار", sub="مع محامي", icon="scale", color="blue"),
        left=dict(title="طلب جديد", value="صلح السبب", sub="", icon="file-text", color="green"), gap=4.0),
   dict(k="text", text="رد الاعتبار كيحيد المنع", at="وإلى كان الرفض بسبب", until="ونصيحة عامة", y=640, size=64, color=GOLD),
   dict(k="people", at="ونصيحة عامة", until="اللي بغا يعاونك", box=FULL, people=["man", "woman"],
        say=[dict(who=0, text="نسرع ليك الملف", at=1.5, bg="red"), dict(who=1, text="لا، شكرا", at=5.0, bg="green")]),
   dict(k="icons", at="اللي بغا يعاونك", box=ICB, items=[
     ["building-bank", "الباترونا", "green"], ["scale", "المحامي المسجل", "blue"], ["receipt", "الوصل", "gold"]], gap=2.0),
 ]),
 dict(audio="H.wav", text=T["H"], chapter="08 · سؤال وجواب", src=S_QA, items=[
   dict(k="chapter", num="08", title="سؤال وجواب", at=0.1, until="السؤال الأول"),
   dict(k="map", view="north", pins=["Milano"], labels=False, at="السؤال الأول", until="السؤال التاني", box=L_BOX),
   dict(k="people", at="السؤال الأول", until="السؤال التاني", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="عام ونص وعندنا بنت", at=1.5, bg="gold"), dict(who=0, text="إيه: عام واحد", at=10.0, bg="green")]),
   dict(k="people", at="السؤال التاني", until="السؤال التالت", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="نوري الدخل؟", at=1.5, bg="gold"), dict(who=1, text="لا", at=5.0, bg="green")]),
   dict(k="map", view="north", pins=["Brescia"], labels=False, at="السؤال التالت", until="السؤال الرابع", box=L_BOX),
   dict(k="people", at="السؤال التالت", until="السؤال الرابع", box=R_BOX, people=["woman"],
        say=[dict(who=0, text="عندي الكارطا", at=1.5, bg="gold"), dict(who=0, text="اليوم معفية", at=9.0, bg="green")]),
   dict(k="people", at="السؤال الرابع", until="السؤال الخامس", box=FULL, people=["worker", "clerk"],
        say=[dict(who=0, text="عند العدول؟", at=1.5, bg="gold"), dict(who=1, text="سجلو فالكومون", at=6.0, bg="green")]),
   dict(k="map", view="south", pins=["Palermo"], labels=False, at="السؤال الخامس", until="السؤال السادس", box=L_BOX),
   dict(k="bars", at="السؤال الخامس", until="السؤال السادس", box=R_BOX, bars=[
     ["المساهمة", 250, "250 €", "gold"], ["التامبر", 16, "16 €", "blue"]], gap=3.0),
   dict(k="people", at="السؤال السادس", until="السؤال السابع", box=FULL, people=["elder", "clerk"],
        say=[dict(who=0, text="فاتو عامين!", at=1.5, bg="red"), dict(who=1, text="24 حتى 36 شهر", at=8.0, bg="gold")]),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Torino", "Casablanca", "plane"], pins=["Torino", "Casablanca"], labels=False,
        at="السؤال السابع", until="السؤال التامن", box=L_BOX),
   dict(k="people", at="السؤال السابع", until="السؤال التامن", box=R_BOX, people=["girl"],
        say=[dict(who=0, text="نمشيو للمغرب؟", at=1.5, bg="gold"), dict(who=0, text="سول قبل", at=12.0, bg="red")]),
   dict(k="people", at="السؤال التامن", until="والسؤال التاسع", box=FULL, people=["student", "elder"],
        say=[dict(who=0, text="نجيب الوالدين؟", at=1.5, bg="gold"), dict(who=1, text="موضوع آخر", at=6.0)]),
   dict(k="people", at="والسؤال التاسع", until="والسؤال العاشر", box=FULL, people=["hijab", "office"],
        say=[dict(who=0, text="خاصني محامي؟", at=1.5, bg="gold"), dict(who=1, text="لا، بالسبيد", at=5.0, bg="green")]),
   dict(k="map", view="north", pins=["Padova"], labels=False, at="والسؤال العاشر", until="وهادي هي الأسئلة", box=L_BOX),
   dict(k="people", at="والسؤال العاشر", until="وهادي هي الأسئلة", box=R_BOX, people=["man"],
        say=[dict(who=0, text="الحلفان صعيب؟", at=1.5, bg="gold"), dict(who=0, text="جملة قصيرة", at=6.0, bg="green")]),
   dict(k="text", text="سؤالك فالكومونتير", at="وهادي هي الأسئلة", y=640, size=64, color=GOLD),
 ]),
 dict(audio="I.wav", text=T["I"], chapter="09 · اللائحة النهائية", src=S_HOME, items=[
   dict(k="chapter", num="09", title="اللائحة النهائية", at=0.1, until="واحد: تأكد"),
   dict(k="rows", at="واحد: تأكد", until="خلينا نرجعو", y=180, gap=72, size=38, rows=[
     ("الزواج مسجل فالكومون", "1", "واحد: تأكد"),
     ("2 سنين فإيطاليا ولا 3 برا · النص مع الولاد", "2", "جوج: احسب"),
     ("اللغة B1 ولا الإعفاء", "3", "تلاتة: الشهادة"),
     ("عقد الازدياد والسوابق: أبوستيل وترجمة", "4", "ربعة: من المغرب"),
     ("البيرميسو · الباسبور · السبيد", "5", "خمسة: من إيطاليا"),
     ("الخلاص للدولة", "6", "ستة: الخلاص"),
     ("الطلب على البورطال", "7", "سبعة: الطلب"),
     ("شوف البورطال كل سيمانة", "8", "تمنية: من بعد"),
     ("الحلفان قبل 6 شهور", "9", "تسعود: الحلفان"),
     ("الرفض؟ جاوب وصلح", "10", "وعشرة: إلى جاك"),
   ]),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="نادية فتورينو", until="يوسف فبولونيا", box=L_BOX),
   dict(k="people", at="نادية فتورينو", until="يوسف فبولونيا", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="مارس 2027", at=4.0, bg="green")]),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Fes", "Bologna", "plane"], pins=["Fes", "Bologna"], labels=False,
        at="يوسف فبولونيا", until="وسلمى فالدار البيضاء", box=L_BOX),
   dict(k="people", at="يوسف فبولونيا", until="وسلمى فالدار البيضاء", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="نسجل الزواج", at=2.0, bg="gold")]),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Casablanca"], labels=False, at="وسلمى فالدار البيضاء", until="إذن التلاتة عندهم", box=L_BOX),
   dict(k="people", at="وسلمى فالدار البيضاء", until="إذن التلاتة عندهم", box=R_BOX, people=["girl"],
        say=[dict(who=0, text="نقدم دابا", at=4.0, bg="green")]),
   dict(k="icons", at="إذن التلاتة عندهم", until="وإلى كان شي حاجة", box=ICB, items=[
     ["calendar", "التسجيل", "blue"], ["clock", "السوابق", "gold"], ["users", "الحلفان", "green"]], gap=3.0),
   dict(k="text", text="الفصول مكتوبة فالوصف", at="وإلى كان شي حاجة", until="ودابا، سؤال ليك", y=640, size=64, color=GOLD),
   dict(k="people", at="ودابا، سؤال ليك", until="وإلى عرفتي شي واحد", box=FULL, people=["woman", "man"],
        say=[dict(who=0, text="إيه ولا لا؟", at=2.0, bg="green")]),
   dict(k="people", at="وإلى عرفتي شي واحد", until="وإلى عجبك هاد العمل", box=FULL, people=["worker", "hijab"],
        say=[dict(who=1, text="صيفطو لصاحبك", at=1.0, bg="gold")]),
   dict(k="cta", at="وإلى عجبك هاد العمل", text="ابوني فالقناة", sub="كل نهار دليل مفيد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("الجنسية الإيطالية بالزواج", (236, 196, 96)), "الشروط ووراق المغرب", "شحال كتخلص؟"],
  num="266 €", numsub="للدولة · زايد الترجمة والأبوستيل",
  bottom="مغاربة إيطاليا · دليل عملي بالدارجة",
)
