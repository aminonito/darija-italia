import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-19.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo2-2026-11-19-final")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = {k: v.replace("گ", "ك") for k, v in JOB["blocks"].items()}
# tagli nell'audio finale (finali troncati dal TTS flash)
T["C"] = T["C"].replace(" ودابا نمشيو للامتحان النظري.", "")
T["E"] = T["E"].replace("خاصة، غادي نشوفوها دابا.", "خاصة.")
T["F"] = T["F"].replace(" ما تحشمش تطلبو، راه حق.", "")
# cifra 158 € tolta dall'audio (Whisper sentiva "150"): resta solo a schermo
T["B"] = T["B"].replace("راه كيخالف القانون، والخطية كتبدا من مية وتمنية وخمسين أورو، ويقدرو يحيدو ليه البيرمي.", "راه كيخالف القانون، ويقدرو يحيدو ليه البيرمي.")
T["G"] = T["G"].replace("من بعد، الخطية كتبدا من مية وتمنية وخمسين أورو، ويحيدو ليك البيرمي.", "من بعد، ويحيدو ليك البيرمي.")

S_HOME = "مغاربة إيطاليا · دليل عملي بالدارجة"
S_REQ = "auto.it 6/3/2026 · QuotidianoMotori · MIT accordo Italia-Marocco · Infopatenti"
S_DOC = "Regione FVG Motorizzazione · ComparaSemplice · auto.it"
S_TEO = "SicurAuto · Regione FVG Motorizzazione · auto.it"
S_PRA = "D.M. MIT 294/2025 · QuotidianoMotori · auto.it · SicurAuto · Regione FVG"
S_NEO = "SicurAuto · auto.it 13/3/2026 · QuotidianoMotori (L. 177/2024)"
S_ERR = "Infopatenti · Brocardi art. 135 CdS · SicurAuto · Regione FVG"
S_QA = "Fonti dei capitoli 01-07"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850); FULL = (160, 300, 1760, 860); MID = (260, 220, 1660, 840)
ICB = (160, 330, 1760, 860); VSB = (260, 220, 1660, 820)

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="01 · شكون كيحتاج هاد الدليل", src=S_HOME, items=[
   dict(k="head", text="البيرمي فإيطاليا من الصفر", at=0.2, until="ماشي التبدال ديال البيرمي", sub="الامتحان النظري والتطبيقي · خطوة بخطوة"),
   dict(k="people", at=0.8, until="ماشي التبدال ديال البيرمي", box=FULL, people=["man", "girl", "worker"],
        say=[dict(who=1, text="منين نبدا؟", at=1.0), dict(who=0, text="شحال غادي نخلص؟", at=3.0, bg="gold")]),
   dict(k="vs", at="ماشي التبدال ديال البيرمي", until="اليوم كنهضرو على", box=VSB,
        right=dict(title="التبدال", value="فيديو آخر", sub="البيرمي المغربي", icon="license", color="grey"),
        left=dict(title="الامتحان", value="اليوم", sub="من الصفر", icon="school", color="green"), gap=2.0),
   dict(k="icons", at="اليوم كنهضرو على", until="شكون كيحتاج هاد الدليل؟", box=ICB, items=[
     ["school", "النظري والتطبيقي", "green"], ["file-text", "الوراق", "blue"], ["coin-euro", "الثمن والمدة", "gold"], ["alert-triangle", "الأخطاء", "red"]], gap=1.6),
   dict(k="map", view="italy", pins=["Verona", "Bari"], labels=False, at="شكون كيحتاج هاد الدليل؟", until="الأول، حمزة", box=(160, 200, 1760, 880)),
   dict(k="map", view="north", pins=["Verona"], labels=False, at="الأول، حمزة", until="التانية، سلمى", box=L_BOX),
   dict(k="people", at="الأول، حمزة", until="التانية، سلمى", box=R_BOX, people=["man", "clerk"],
        say=[dict(who=0, text="عندي البيرمي المغربي", at=1.0), dict(who=1, text="فاتو ستة سنين!", at=9.0, bg="red")]),
   dict(k="map", view="north", pins=["Padova"], labels=False, at="التانية، سلمى", until="والتالت، خالد", box=L_BOX),
   dict(k="people", at="التانية، سلمى", until="والتالت، خالد", box=R_BOX, people=["girl"],
        say=[dict(who=0, text="عمري ما سقت", at=1.5, bg="gold")]),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Bari", "Nador", "plane"], pins=["Bari", "Nador"], labels=False,
        at="والتالت، خالد", until="إذن حتى خالد", box=L_BOX),
   dict(k="people", at="والتالت، خالد", until="إذن حتى خالد", box=R_BOX, people=["worker", "clerk"],
        say=[dict(who=0, text="خديتو فالعطلة", at=2.0), dict(who=1, text="من بعد الريزيدينسا", at=7.0, bg="red")]),
   dict(k="steps", at="إذن حتى خالد", until="التلاتة كيسولو", box=MID, steps=[
     ["حمزة · ففيرونا", "+6"], ["سلمى · فبادوفا", "0"], ["خالد · فباري", "!"]], gap=2.5, check_after=0.6),
   dict(k="people", at="التلاتة كيسولو", until="فهاد الفيديو غادي", box=FULL, people=["man", "girl", "worker"],
        say=[dict(who=0, text="واش بالعربية؟", at=2.5), dict(who=2, text="شحال ديال الوقت؟", at=4.0, bg="gold")]),
   dict(k="rows", at="فهاد الفيديو غادي", until="وكل فصل غادي يكون", y=215, gap=78, size=40, rows=[
     ("شكون خاصو هاد الطريق", "01", "الأول، شكون"),
     ("الشروط", "02", "التاني، الشروط"),
     ("الوراق والخلاص", "03", "التالت، الوراق"),
     ("الامتحان النظري", "04", "الرابع، الامتحان"),
     ("الفوليو روزا والتطبيقي", "05", "الخامس، الفوليو"),
     ("الحالات والبيرمي الجديد", "06", "السادس، الحالات"),
     ("الأخطاء", "07", "السابع، الأخطاء"),
     ("سؤال وجواب", "08", "التامن، سؤال"),
     ("اللائحة النهائية", "09", "والتاسع، لائحة"),
   ]),
   dict(k="icons", at="وكل فصل غادي يكون", until="البيرمي فإيطاليا ماشي غير", box=ICB, items=[
     ["calculator", "أمثلة بالحساب", "green"], ["file-certificate", "جوج مصادر", "blue"], ["alert-triangle", "ماشي استشارة قانونية", "gold"]], gap=4.0),
   dict(k="icons", at="البيرمي فإيطاليا ماشي غير", until="والخبر المزيان", box=ICB, items=[
     ["truck", "التوصيل", "blue"], ["tool", "الشانطيات", "gold"], ["bus", "بلا طوبيس", "green"]], gap=2.5),
   dict(k="warn", text="البيرمي المغربي: عام واحد من الريزيدينسا", at="وكاين اللي كيخدم بالبيرمي", until="والخبر المزيان", y=880),
   dict(k="people", at="والخبر المزيان", box=FULL, people=["clerk", "girl"],
        say=[dict(who=0, text="الطريق ماشي مستحيلة", at=0.8, bg="green"), dict(who=1, text="يلاه نبداو!", at=9.0)]),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="02 · الشروط", src=S_REQ, items=[
   dict(k="chapter", num="02", title="الشروط", at=0.1, until="الشرط الأول: العمر"),
   dict(k="big", text="18", at="الشرط الأول: العمر", until="الشرط التاني: الريزيدينسا", y=430, size=300, color=GOLD, sub="عام على الأقل"),
   dict(k="map", view="north", pins=["Padova"], labels=False, at="الشرط التاني: الريزيدينسا", until="الشرط التالت", box=L_BOX),
   dict(k="people", at="الشرط التاني: الريزيدينسا", until="الشرط التالت", box=R_BOX, people=["clerk"],
        say=[dict(who=0, text="مسجل فالكومون؟", at=2.0, bg="green")]),
   dict(k="icons", at="الشرط التالت", until="الشرط الرابع", box=ICB, items=[
     ["e-passport", "البيرميسو صالح", "green"], ["file-text", "نسخة مع الطلب", "blue"], ["receipt", "الريسيفوتا؟ سول", "gold"]], gap=3.5),
   dict(k="people", at="الشرط الرابع", until="هاد الشهادة فيها", box=FULL, people=["doctor", "girl"],
        say=[dict(who=0, text="نشوفو العينين", at=3.0, bg="green")]),
   dict(k="vs", at="هاد الشهادة فيها", until="خلينا نحسبو مع سلمى", box=VSB,
        right=dict(title="الطبيب", value="3 شهور", sub="أقصى مدة", icon="stethoscope", color="gold"),
        left=dict(title="اللجنة الطبية", value="6 شهور", sub="أقصى مدة", icon="building-hospital", color="blue"), gap=5.0),
   dict(k="calendar", at="خلينا نحسبو مع سلمى", until="إذن خاصها تقدم", box=R_BOX, day=10, month=12, sub="2026 · الشهادة الطبية"),
   dict(k="map", view="north", pins=["Padova"], labels=False, at="خلينا نحسبو مع سلمى", until="ودابا السؤال اللي", box=L_BOX),
   dict(k="calendar", at="إذن خاصها تقدم", until="ودابا السؤال اللي", box=R_BOX, day=10, month=3, sub="2027 · آخر أجل للطلب"),
   dict(k="people", at="ودابا السؤال اللي", until="عاوتاني باش يكون واضح", box=FULL, people=["man", "worker"],
        say=[dict(who=0, text="علاش ما نبدلوش؟", at=1.0)]),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Casablanca", "Roma", "plane"], pins=["Casablanca", "Roma"], labels=False,
        at="عاوتاني باش يكون واضح", until="حمزة عندو الريزيدينسا", box=L_BOX),
   dict(k="steps", at="عاوتاني باش يكون واضح", until="حمزة عندو الريزيدينسا", box=R_BOX, steps=[
     ["ريزيدينسا أقل", "6"], ["البيرمي قبل", "1"]], gap=5.0, check_after=0.6),
   dict(k="map", view="north", pins=["Verona"], labels=False, at="حمزة عندو الريزيدينسا", until="نحسبو بالتواريخ", box=L_BOX),
   dict(k="people", at="حمزة عندو الريزيدينسا", until="نحسبو بالتواريخ", box=R_BOX, people=["man"],
        say=[dict(who=0, text="فاتت بزاف", at=2.0, bg="red")]),
   dict(k="bars", at="نحسبو بالتواريخ", until="خالد دار الريزيدينسا فألفين", box=(160, 330, 1760, 840), bars=[
     ["الحد", 6, "6", "green"], ["حمزة", 10, "10", "red"]], gap=1.5),
   dict(k="icons", at="خالد دار الريزيدينسا فألفين", until="إذن جوج بجوج", box=ICB, items=[
     ["home", "الريزيدينسا 2023", "blue"], ["license", "البيرمي 2024", "gold"], ["x", "ما كيتبدلش", "red"]], gap=2.5),
   dict(k="people", at="إذن جوج بجوج", until="وشي حاجة مهمة بزاف", box=FULL, people=["man", "worker", "girl"],
        say=[dict(who=2, text="نفس الطريق!", at=2.0, bg="gold")]),
   dict(k="big", text="1", at="وشي حاجة مهمة بزاف", until="إذن إلى كان كيسوق", y=430, size=300, color=RED, sub="عام واحد بالبيرمي المغربي من الريزيدينسا"),
   dict(k="big", text="158 €", at="إذن إلى كان كيسوق", until="إذن ملخص الشروط", y=430, size=230, color=RED, sub="الخطية كتبدا من 158 € · وكيحيدو البيرمي"),
   dict(k="icons", at="إذن ملخص الشروط", until="وحاجة صغيرة على", box=ICB, items=[
     ["user", "18 عام", "gold"], ["home", "الريزيدينسا", "blue"], ["e-passport", "البيرميسو", "green"], ["stethoscope", "الشهادة الطبية", "gold"]], gap=1.5),
   dict(k="people", at="وحاجة صغيرة على", box=FULL, people=["doctor", "elder"],
        say=[dict(who=1, text="عندي النظاظر", at=8.0, bg="green")]),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="03 · الوراق والخلاص", src=S_DOC, items=[
   dict(k="chapter", num="03", title="الوراق والخلاص", at=0.1, until="كاين جوج ديال الطرق"),
   dict(k="vs", at="كاين جوج ديال الطرق", until="ودابا الوراق، واحد", box=(260, 200, 1660, 780),
        right=dict(title="الأوطوسكويلا", value="كتدير كلشي", sub="الوراق والمواعيد", icon="school", color="green"),
        left=dict(title="بريفاتيستا", value="بوحدك", sub="مكتب الموطوريزاسيون", icon="user", color="blue"), gap=5.0),
   dict(k="warn", text="حتى البريفاتيستا: الدروس ديال السياقة مع الأوطوسكويلا", at="حتى إلى اخترتي", until="ودابا الوراق، واحد", y=880),
   dict(k="icons", at="ودابا الوراق، واحد", until="ربعة: نسخة", box=ICB, items=[
     ["file-text", "TT2112", "blue"], ["id", "الهوية", "green"], ["license", "الكودشي فيسكالي", "gold"]], gap=4.5),
   dict(k="icons", at="ربعة: نسخة", until="سبعة: نسخة", box=ICB, items=[
     ["e-passport", "البيرميسو", "green"], ["stethoscope", "الشهادة الطبية", "gold"], ["camera", "التصاور", "blue"]], gap=2.5),
   dict(k="people", at="سبعة: نسخة", until="وتمنية: الإيصالات", box=FULL, people=["worker", "clerk"],
        say=[dict(who=1, text="نسخة من البيرمي المغربي", at=2.0, bg="gold")]),
   dict(k="icons", at="وتمنية: الإيصالات", until="الخلاص الأول", box=ICB, items=[
     ["receipt", "الإيصالات", "gold"], ["credit-card", "pagoPA", "blue"], ["building-bank", "البورطال", "green"]], gap=2.0),
   dict(k="rows", at="الخلاص الأول", until="هادا غير ديال الدولة", y=330, gap=120, size=50, rows=[
     ("الطلب والنظري · الحقوق", "26,40 €", "الخلاص الأول"),
     ("التنبر ديال الطلب", "16,00 €", "وزيد عليها سطاش"),
     ("التنبر ديال التطبيقي", "16,00 €", "الخلاص التاني"),
     ("المجموع للدولة", "58,40 €", "إذن المجموع", GOLD),
   ]),
   dict(k="icons", at="هادا غير ديال الدولة", until="المصادر اللي شفنا", box=ICB, items=[
     ["stethoscope", "الطبيب", "blue"], ["school", "التسجيل والنظري", "green"], ["car", "الدروس والسيارة", "gold"]], gap=3.0),
   dict(k="big", text="≈ 1.000 €", at="المصادر اللي شفنا", until="نصيحتنا: سول", y=430, size=230, color=GOLD, sub="غالبا مع الأوطوسكويلا · كيختالف من مدينة لمدينة"),
   dict(k="people", at="نصيحتنا: سول", until="وزيد واحد الحاجة", box=FULL, people=["hijab", "clerk"],
        say=[dict(who=0, text="عطيني الثمن مكتوب", at=3.0, bg="green")]),
   dict(k="people", at="وزيد واحد الحاجة", until="نديرو حساب صغير", box=R_BOX, people=["elder"],
        say=[dict(who=0, text="نسمع فالسماعات", at=3.0, bg="green")]),
   dict(k="icons", at="وزيد واحد الحاجة", until="نديرو حساب صغير", box=L_BOX, items=[
     ["file-text", "التصريح", "blue"], ["coin-euro", "16 €", "gold"]], gap=4.0),
   dict(k="map", view="north", pins=["Padova"], labels=False, at="نديرو حساب صغير", until="ولكن إلى سقطت جوج", box=L_BOX),
   dict(k="people", at="نديرو حساب صغير", until="ولكن إلى سقطت جوج", box=R_BOX, people=["girl"],
        say=[dict(who=0, text="58,40 €", at=4.0, bg="green")]),
   dict(k="bars", at="ولكن إلى سقطت جوج", until="إذن خلي كلشي", box=(160, 330, 1760, 840), bars=[
     ["من الأولى", 58.4, "58,40 €", "green"], ["طلب جديد", 100.8, "100,80 €", "red"]], gap=3.0),
   dict(k="icons", at="إذن خلي كلشي", box=ICB, items=[
     ["clipboard-check", "الأصول عندك", "green"], ["camera", "صور كلشي", "blue"], ["receipt", "الإيصال ديال الطلب", "gold"]], gap=3.0),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="04 · الامتحان النظري", src=S_TEO, items=[
   dict(k="chapter", num="04", title="الامتحان النظري", at=0.1, until="خلينا نشرحوه"),
   dict(k="people", at="خلينا نشرحوه", until="كتعطاك تلاتين", box=FULL, people=["student", "clerk"],
        say=[dict(who=0, text="كنخاف من الكويز", at=0.5)]),
   dict(k="steps", at="كتعطاك تلاتين", until="الأسئلة كتخرج بالصدفة", box=MID, steps=[
     ["جملة صحيحة ولا غالطة", "30"], ["دقيقة", "20"], ["أخطاء على الأكثر", "3"]], gap=3.0, check_after=0.6),
   dict(k="icons", at="الأسئلة كتخرج بالصدفة", until="ودابا السؤال اللي كيطرحو الكل", box=ICB, items=[
     ["building-bank", "الأرشيف ديال الوزارة", "blue"], ["phone", "الكويز ديال التدريب", "green"]], gap=3.0),
   dict(k="people", at="ودابا السؤال اللي كيطرحو الكل", until="كاين استثناء غير", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="واش بالعربية؟", at=0.5), dict(who=1, text="لا، بالطليانية", at=2.5, bg="red")]),
   dict(k="map", view="italy", hl=["Valle d'Aosta", "Trentino-Alto Adige"], labels=True, at="كاين استثناء غير", until="ولكن كاين حل مزيان", box=(160, 200, 1760, 880)),
   dict(k="people", at="ولكن كاين حل مزيان", until="هاد الطلب خاصو يتقدم", box=R_BOX, people=["woman"],
        say=[dict(who=0, text="السماعات!", at=6.0, bg="green")]),
   dict(k="icons", at="ولكن كاين حل مزيان", until="هاد الطلب خاصو يتقدم", box=L_BOX, items=[
     ["school", "بلا الإعدادي", "gold"], ["user", "ما كتقراش مزيان", "blue"]], gap=3.0),
   dict(k="steps", at="هاد الطلب خاصو يتقدم", until="شحال من مرة تقدر تدوز؟", box=MID, steps=[
     ["التصريح", "1"], ["نسخة الهوية", "2"], ["الخلاص", "16 €"]], gap=2.5, check_after=0.6),
   dict(k="vs", at="شحال من مرة تقدر تدوز؟", until="خلينا نحسبو مع سلمى", box=(260, 200, 1660, 780),
        right=dict(title="المحاولات", value="2", sub="فستة شهور", icon="clipboard-check", color="green"),
        left=dict(title="بين جوج", value="شهر", sub="على الأقل", icon="calendar", color="gold"), gap=4.0),
   dict(k="warn", text="جوج سقطات ولا 6 شهور = طلب جديد وخلاص جديد", at="إلى سقطتي جوج ديال المرات", until="خلينا نحسبو مع سلمى", y=880),
   dict(k="map", view="north", pins=["Padova"], labels=False, at="خلينا نحسبو مع سلمى", until="إذن عندها حتى", box=L_BOX),
   dict(k="calendar", at="خلينا نحسبو مع سلمى", until="إذن عندها حتى", box=R_BOX, day=15, month=12, sub="2026 · الطلب"),
   dict(k="calendar", at="إذن عندها حتى", until="إلى سقطت فالمرة الأولى", box=R_BOX, day=15, month=6, sub="2027 · آخر أجل للنظري"),
   dict(k="map", view="north", pins=["Padova"], labels=False, at="إذن عندها حتى", until="إلى سقطت فالمرة الأولى", box=L_BOX),
   dict(k="icons", at="إلى سقطت فالمرة الأولى", until="ودابا كيفاش تقرا؟", box=ICB, items=[
     ["x", "يناير: سقطت", "red"], ["calendar", "شهر من بعد", "gold"], ["check", "فبراير ولا مارس", "green"]], gap=2.5),
   dict(k="icons", at="ودابا كيفاش تقرا؟", until="التالتة: تعلم", box=ICB, items=[
     ["phone", "الكويز", "green"], ["school", "فهم، ماشي حفظ", "gold"]], gap=4.0),
   dict(k="icons", at="التالتة: تعلم", until="وإلى كانت الطليانية صعيبة", box=ICB, items=[
     ["alert-triangle", "precedenza", "gold"], ["car", "sorpasso", "blue"], ["map-pin", "sosta", "green"]], gap=1.5),
   dict(k="people", at="وإلى كانت الطليانية صعيبة", until="وعلاش كيسقطو بزاف؟", box=FULL, people=["hijab", "office"],
        say=[dict(who=0, text="كاين شي واحد كيشرح بالعربية؟", at=3.0)]),
   dict(k="people", at="وعلاش كيسقطو بزاف؟", until="لهذا، قرا بشوية", box=R_BOX, people=["student"],
        say=[dict(who=0, text="كلمة وحدة بدلات كلشي!", at=6.0, bg="red")]),
   dict(k="icons", at="وعلاش كيسقطو بزاف؟", until="لهذا، قرا بشوية", box=L_BOX, items=[
     ["alert-triangle", "sempre", "red"], ["alert-triangle", "solo", "red"], ["x", "vietato", "gold"]], gap=1.2),
   dict(k="big", text="30 / 20", at="لهذا، قرا بشوية", until="وفكر فالبرنامج", y=430, size=230, color=GREEN, sub="تلاتين سؤال فعشرين دقيقة · تدرب كامل"),
   dict(k="bars", at="وفكر فالبرنامج", until="ونهار الامتحان، وصل بكري", box=(160, 330, 1760, 840), bars=[
     ["سيمانات", 7, "6-7", "green"], ["ساعة فالنهار", 1, "1", "gold"]], gap=2.0),
   dict(k="people", at="ونهار الامتحان، وصل بكري", box=FULL, people=["girl", "clerk"],
        say=[dict(who=0, text="جبت الوراق", at=1.5, bg="green"), dict(who=1, text="الفوليو روزا جاية", at=8.0)]),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="05 · الفوليو روزا والتطبيقي", src=S_PRA, items=[
   dict(k="chapter", num="05", title="الفوليو روزا والتطبيقي", at=0.1, until="ملي كتدوز النظري"),
   dict(k="big", text="12", at="ملي كتدوز النظري", until="ودابا الدروس ديال السياقة", y=430, size=300, color=GOLD, sub="شهر · الفوليو روزا · ما كتتمددش"),
   dict(k="vs", at="ودابا الدروس ديال السياقة", until="التمنية ديال الساعات مقسومة", box=VSB,
        right=dict(title="القديم", value="6", sub="ساعات", icon="clock", color="grey"),
        left=dict(title="الجديد", value="8", sub="ساعات", icon="clock", color="green"), gap=9.0),
   dict(k="bars", at="التمنية ديال الساعات مقسومة", until="وكتكون ماشي أكثر", box=(160, 330, 1760, 840), bars=[
     ["السيارة والسلامة", 2, "2", "blue"], ["المدينة", 3, "3", "green"], ["خارج المدينة", 2, "2", "gold"], ["الليل", 1, "1", "grey"]], gap=1.8),
   dict(k="text", text="ماشي أكثر من جوج ساعات فالنهار", at="وكتكون ماشي أكثر", until="المصادر ما متفقينش", y=640, size=60, color=GOLD),
   dict(k="people", at="المصادر ما متفقينش", until="ومن غير الأوطوسكويلا", box=FULL, people=["office", "girl"],
        say=[dict(who=1, text="ستة ولا تمنية؟", at=7.0, bg="gold")]),
   dict(k="people", at="ومن غير الأوطوسكويلا", until="وخاص العلامة", box=R_BOX, people=["elder", "girl"],
        say=[dict(who=0, text="البيرمي من 10 سنين", at=4.0, bg="green")]),
   dict(k="steps", at="ومن غير الأوطوسكويلا", until="وخاص العلامة", box=L_BOX, steps=[
     ["البيرمي من", "10"], ["العمر حتى", "65"], ["حداك فالقدام", "1"]], gap=2.5, check_after=0.6),
   dict(k="big", text="P", at="وخاص العلامة", until="وانتبه: مع القاعدة", y=430, size=300, color=WHITE, sub="العلامة ديال المبتدئ فالسيارة"),
   dict(k="warn", text="القاعدة الجديدة: العائلة غير من بعد الساعات ديال الأوطوسكويلا", at="وانتبه: مع القاعدة", until="وفالدروس مع المعلم", y=640),
   dict(k="icons", at="وفالدروس مع المعلم", until="ومنين تقدر تدوز التطبيقي؟", box=ICB, items=[
     ["map-pin", "الدوارات", "gold"], ["car", "الأوطوروت", "blue"], ["home", "الوقوف", "green"]], gap=3.0),
   dict(k="steps", at="ومنين تقدر تدوز التطبيقي؟", until="السيارة ديال الامتحان", box=MID, steps=[
     ["من بعد الفوليو روزا", "30"], ["المحاولات", "3"]], gap=3.5, check_after=0.6),
   dict(k="people", at="السيارة ديال الامتحان", until="خلينا نحسبو مع سلمى", box=R_BOX, people=["office"],
        say=[dict(who=0, text="المرايات؟ السمطة؟", at=6.0, bg="gold")]),
   dict(k="icons", at="السيارة ديال الامتحان", until="خلينا نحسبو مع سلمى", box=L_BOX, items=[
     ["car", "جوج فرانات", "green"], ["check", "المرايات والسمطة", "blue"]], gap=4.0),
   dict(k="calendar", at="خلينا نحسبو مع سلمى", until="الفوليو روزا ديالها صالحة", box=R_BOX, day=20, month=1, sub="2027 · دازت النظري"),
   dict(k="map", view="north", pins=["Padova"], labels=False, at="خلينا نحسبو مع سلمى", until="أول نهار تقدر", box=L_BOX),
   dict(k="calendar", at="الفوليو روزا ديالها صالحة", until="أول نهار تقدر", box=R_BOX, day=20, month=1, sub="2028 · آخر نهار ديال الفوليو روزا"),
   dict(k="calendar", at="أول نهار تقدر", until="إلى دارت الدروس", box=R_BOX, day=19, month=2, sub="2027 · أول تطبيقي ممكن"),
   dict(k="map", view="north", pins=["Padova"], labels=False, at="أول نهار تقدر", until="إلى دارت الدروس", box=L_BOX),
   dict(k="steps", at="إلى دارت الدروس", until="ونهار التطبيقي، وصل", box=MID, steps=[
     ["الشهادة الطبية", "12/2026"], ["النظري", "1/2027"], ["التطبيقي", "الربيع"]], gap=3.0, check_after=0.6),
   dict(k="people", at="ونهار التطبيقي، وصل", until="وملي كتدوز التطبيقي، مبروك", box=FULL, people=["girl", "office"],
        say=[dict(who=1, text="سوق بالسلامة", at=8.0, bg="green")]),
   dict(k="people", at="وملي كتدوز التطبيقي، مبروك", box=FULL, people=["girl", "hijab"],
        say=[dict(who=0, text="دزت!", at=0.5, bg="green"), dict(who=1, text="ولكن رد البال", at=3.0, bg="gold")]),
 ]),
 dict(audio="F.wav", text=T["F"], chapter="06 · الحالات والبيرمي الجديد", src=S_NEO, items=[
   dict(k="chapter", num="06", title="الحالات والبيرمي الجديد", at=0.1, until="فإيطاليا، البيرمي الجديد"),
   dict(k="big", text="3", at="فإيطاليا، البيرمي الجديد", until="القيد الأول", y=430, size=300, color=GOLD, sub="سنين ديال القيود من نهار البيرمي"),
   dict(k="rows", at="القيد الأول", until="القيد التاني", y=380, gap=140, size=52, rows=[
     ("القوة فالطن", "75 kW/t", "القيد الأول"),
     ("القوة فالمجموع", "105 kW", "ولا أكثر من مية وخمسة"),
     ("قبل ما تشري", "الكارط كريز", "قبل ما تشري"),
   ]),
   dict(k="bars", at="القيد التاني", until="القيد التالت", box=(160, 330, 1760, 840), bars=[
     ["الأوطوروت", 100, "100 km/h", "gold"], ["الطرق الكبيرة", 90, "90 km/h", "blue"]], gap=3.0),
   dict(k="big", text="0", at="القيد التالت", until="القيد الرابع", y=430, size=320, color=RED, sub="الشراب: الحد هو صفر"),
   dict(k="vs", at="القيد الرابع", until="والعقوبة إلى سقتي", box=VSB,
        right=dict(title="عادي", value="x1", sub="النقط", icon="license", color="grey"),
        left=dict(title="البيرمي الجديد", value="x2", sub="النقط", icon="license", color="red"), gap=2.0),
   dict(k="rows", at="والعقوبة إلى سقتي", until="وكاين استثناء للقوة", y=400, gap=150, size=52, rows=[
     ("الخطية", "165-660 €", "خطية من مية"),
     ("توقيف البيرمي", "2-8 شهور", "وتوقيف البيرمي", RED),
   ]),
   dict(k="people", at="وكاين استثناء للقوة", until="وكاين حتى الجانب الإيجابي", box=FULL, people=["elder", "student"],
        say=[dict(who=0, text="أنا حداك", at=2.0, bg="green")]),
   dict(k="big", text="+1", at="وكاين حتى الجانب الإيجابي", until="ودابا الحالات ديال الناس", y=430, size=300, color=GREEN, sub="نقطة فالعام بلا مخالفات"),
   dict(k="map", view="north", pins=["Verona"], labels=False, at="حمزة ففيرونا", until="خالد فباري: نفس", box=L_BOX),
   dict(k="people", at="حمزة ففيرونا", until="خالد فباري: نفس", box=R_BOX, people=["man", "office"],
        say=[dict(who=0, text="عندي التجربة...", at=1.0), dict(who=1, text="بحال اللي بادي", at=5.0, bg="gold")]),
   dict(k="map", view="south", pins=["Bari"], labels=False, at="خالد فباري: نفس", until="وحالة أخرى", box=L_BOX),
   dict(k="people", at="خالد فباري: نفس", until="وحالة أخرى", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="الدوارات فإيطاليا", at=8.0, bg="green")]),
   dict(k="steps", at="وحالة أخرى", until="ودابا حالة اللي سقط", box=MID, steps=[
     ["A1 · A2 · A · B1", "1"], ["بلا نظري", "2"], ["غير التطبيقي", "3"]], gap=3.0, check_after=0.6),
   dict(k="steps", at="ودابا حالة اللي سقط", until="وحالة اللي فاتو التناش", box=MID, steps=[
     ["جوج فالنظري", "طلب جديد"], ["تلاتة فالتطبيقي", "فوليو روزا 2"], ["حتى فالتانية", "من الأول"]], gap=4.5, check_after=0.6),
   dict(k="calendar", at="وحالة اللي فاتو التناش", until="وحالة المرا اللي", box=R_BOX, day=12, month="شهر", sub="فاتت؟ طلب جديد"),
   dict(k="icons", at="وحالة اللي فاتو التناش", until="وحالة المرا اللي", box=L_BOX, items=[
     ["file-text", "طلب جديد", "red"], ["stethoscope", "الشهادة الطبية", "gold"]], gap=3.0),
   dict(k="people", at="وحالة المرا اللي", until="وآخر حالة", box=FULL, people=["hijab", "woman"],
        say=[dict(who=0, text="كنخاف نسوق", at=0.8), dict(who=1, text="بشوية بشوية", at=6.0, bg="green")]),
   dict(k="people", at="وآخر حالة", box=FULL, people=["elder", "clerk"],
        say=[dict(who=1, text="السماعات حق", at=3.0, bg="green")]),
 ]),
 dict(audio="G.wav", text=T["G"], chapter="07 · الأخطاء", src=S_ERR, items=[
   dict(k="chapter", num="07", title="الأخطاء", at=0.1, until="الغلطة الأولى"),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Casablanca", "Milano", "plane"], pins=["Casablanca", "Milano"], labels=False,
        at="الغلطة الأولى", until="من بعد، ويحيدو", box=L_BOX),
   dict(k="people", at="الغلطة الأولى", until="من بعد، ويحيدو", box=R_BOX, people=["man"],
        say=[dict(who=0, text="باقي ما سالاش!", at=6.0, bg="red")]),
   dict(k="big", text="158 €", at="من بعد، ويحيدو", until="الغلطة التانية", y=430, size=230, color=RED, sub="الخطية كتبدا من هنا · وكيحيدو البيرمي"),
   dict(k="people", at="الغلطة التانية", until="الغلطة التالتة", box=FULL, people=["student", "elder"],
        say=[dict(who=0, text="غير شوية بوحدي؟", at=0.8, bg="red"), dict(who=1, text="لا! أنا معاك", at=4.0, bg="green")]),
   dict(k="calendar", at="الغلطة التالتة", until="الغلطة الرابعة", box=R_BOX, day=6, month="شهور", sub="من نهار الطلب"),
   dict(k="people", at="الغلطة التالتة", until="الغلطة الرابعة", box=L_BOX, people=["girl"],
        say=[dict(who=0, text="نسيت التاريخ", at=3.0, bg="red")]),
   dict(k="big", text="3", at="الغلطة الرابعة", until="الغلطة الخامسة", y=430, size=300, color=GOLD, sub="شهور · المدة ديال الشهادة الطبية"),
   dict(k="vs", at="الغلطة الخامسة", until="الغلطة السادسة", box=VSB,
        right=dict(title="مسموح", value="105 kW", sub="أقل ولا ساوي", icon="car", color="green"),
        left=dict(title="ممنوع", value="أكثر", sub="توقيف البيرمي", icon="car", color="red"), gap=3.0),
   dict(k="big", text="0", at="الغلطة السادسة", until="الغلطة السابعة", y=430, size=320, color=RED, sub="الشراب فالتلاتة سنين الأولى"),
   dict(k="people", at="الغلطة السابعة", until="الغلطة التامنة", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="عندي الأجوبة...", at=1.0, bg="red"), dict(who=1, text="نصب!", at=5.0, bg="red")]),
   dict(k="icons", at="الغلطة التامنة", until="الغلطة التاسعة", box=ICB, items=[
     ["file-text", "الثمن مكتوب", "green"], ["clock", "الساعة الزايدة", "gold"], ["coin-euro", "إعادة الامتحان", "blue"]], gap=4.0),
   dict(k="vs", at="الغلطة التاسعة", until="الغلطة العاشرة", box=VSB,
        right=dict(title="النظري", value="الهوية", sub="الطلب + السماعات", icon="id", color="blue"),
        left=dict(title="التطبيقي", value="الفوليو روزا", sub="+ الهوية", icon="file-certificate", color="green"), gap=5.0),
   dict(k="people", at="الغلطة العاشرة", until="وزيد الغلطة الحداش", box=FULL, people=["hijab", "office"],
        say=[dict(who=0, text="عطيني الجواب مكتوب", at=7.0, bg="gold")]),
   dict(k="warn", text="كمل الدروس وخود الشهادة قبل الموعد", at="وزيد الغلطة الحداش", until="والغلطة التناش", y=640),
   dict(k="big", text="P", at="والغلطة التناش", until="وأخيرا، ما تعطيش", y=430, size=300, color=WHITE, sub="ما تنساش العلامة ديال المبتدئ"),
   dict(k="icons", at="وأخيرا، ما تعطيش", until="ودابا إلى وقع ليك", box=ICB, items=[
     ["file-text", "الأصول عندك", "green"], ["receipt", "ورقة بلي خداهم", "gold"]], gap=3.0),
   dict(k="map", view="italy", pins=["Verona", "Padova", "Bari"], labels=False, at="ودابا إلى وقع ليك", until="المهم ما تسوقش", box=L_BOX),
   dict(k="steps", at="ودابا إلى وقع ليك", until="المهم ما تسوقش", box=R_BOX, steps=[
     ["طلب جديد", "1"], ["خلاص جديد", "2"], ["عاود", "3"]], gap=2.0, check_after=0.6),
   dict(k="warn", text="ما تسوقش بلا بيرمي صالح", at="المهم ما تسوقش", y=640),
 ]),
 dict(audio="H.wav", text=T["H"], chapter="08 · سؤال وجواب", src=S_QA, items=[
   dict(k="chapter", num="08", title="سؤال وجواب", at=0.1, until="السؤال الأول"),
   dict(k="people", at="السؤال الأول", until="السؤال التاني", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="النظري بالعربية؟", at=0.5), dict(who=1, text="لا · السماعات", at=5.0, bg="gold")]),
   dict(k="people", at="السؤال التاني", until="السؤال التالت", box=R_BOX, people=["elder"],
        say=[dict(who=0, text="البيرمي من 20 عام", at=0.5)]),
   dict(k="steps", at="السؤال التاني", until="السؤال التالت", box=L_BOX, steps=[
     ["ريزيدينسا أقل", "6"], ["البيرمي قبل", "1"]], gap=6.0, check_after=0.6),
   dict(k="people", at="السؤال التالت", until="السؤال الرابع", box=FULL, people=["student", "office"],
        say=[dict(who=0, text="بريفاتيستا أرخص؟", at=0.5), dict(who=1, text="غالبا إيه", at=4.0, bg="green")]),
   dict(k="people", at="السؤال الرابع", until="السؤال الخامس", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="البيرميسو فالتجديد", at=0.5, bg="gold")]),
   dict(k="icons", at="السؤال الرابع", until="السؤال الخامس", box=L_BOX, items=[
     ["receipt", "الريسيفوتا", "gold"], ["e-passport", "البيرميسو القديم", "blue"]], gap=6.0),
   dict(k="people", at="السؤال الخامس", until="السؤال السادس", box=R_BOX, people=["girl"],
        say=[dict(who=0, text="شحال ديال الوقت؟", at=0.5)]),
   dict(k="map", view="north", pins=["Padova"], labels=False, at="السؤال الخامس", until="السؤال السادس", box=L_BOX),
   dict(k="people", at="السؤال السادس", until="السؤال السابع", box=FULL, people=["worker", "clerk"],
        say=[dict(who=0, text="سقطت فالنظري", at=0.5, bg="red"), dict(who=1, text="باقية المحاولة التانية", at=4.0, bg="green")]),
   dict(k="people", at="السؤال السابع", until="السؤال التامن", box=FULL, people=["woman", "elder"],
        say=[dict(who=0, text="شكون يتدرب معايا؟", at=0.5)]),
   dict(k="people", at="السؤال التامن", until="السؤال التاسع", box=FULL, people=["student", "man"],
        say=[dict(who=0, text="الطوموبيل ديال خويا؟", at=0.5)]),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Milano", "Tanger", "plane"], pins=["Milano", "Tanger"], labels=False,
        at="السؤال التاسع", until="السؤال العاشر", box=L_BOX),
   dict(k="people", at="السؤال التاسع", until="السؤال العاشر", box=R_BOX, people=["hijab"],
        say=[dict(who=0, text="فالمغرب؟ سول القنصلية", at=0.5, bg="gold")]),
   dict(k="people", at="السؤال العاشر", until="السؤال الحاداش", box=FULL, people=["elder", "woman"],
        say=[dict(who=0, text="عندي 50 عام", at=0.5), dict(who=1, text="الشرط هو الطبيب", at=5.0, bg="green")]),
   dict(k="people", at="السؤال الحاداش", until="السؤال التناش", box=FULL, people=["girl", "doctor"],
        say=[dict(who=0, text="فين الشهادة الطبية؟", at=0.5)]),
   dict(k="people", at="السؤال التناش", until="السؤال التلطاش", box=R_BOX, people=["man"],
        say=[dict(who=0, text="شحال فيها كيلوواط؟", at=0.5)]),
   dict(k="icons", at="السؤال التناش", until="السؤال التلطاش", box=L_BOX, items=[
     ["file-text", "الكارط كريز", "blue"], ["calculator", "kW · الوزن", "gold"]], gap=3.0),
   dict(k="people", at="السؤال التلطاش", until="وهادو هوما الأسئلة", box=FULL, people=["worker", "office"],
        say=[dict(who=0, text="شدوني بالمغربي", at=0.5, bg="red"), dict(who=1, text="ما تسوقش دابا", at=9.0, bg="gold")]),
   dict(k="people", at="وهادو هوما الأسئلة", box=FULL, people=["man", "girl", "worker"],
        say=[dict(who=1, text="كتب سؤالك فالكومونتير", at=0.5, bg="green")]),
 ]),
 dict(audio="I.wav", text=T["I"], chapter="09 · اللائحة النهائية", src=S_HOME, items=[
   dict(k="head", text="اللائحة النهائية", at=0.1, until="واحد: شوف أولا", sub="خود تصويرة ديال الشاشة"),
   dict(k="rows", at="واحد: شوف أولا", until="ورجعنا للناس ديالنا", y=190, gap=82, size=40, rows=[
     ("التبدال؟ أقل من 6 سنين وقبل الريزيدينسا", "1", "واحد: شوف"),
     ("18 عام · ريزيدينسا · بيرميسو · طبيب", "2", "جوج: إلى لا"),
     ("الوراق والنسخ", "3", "تلاتة: الوراق"),
     ("الخلاص للدولة · 58,40 €", "4", "ربعة: الخلاص"),
     ("النظري: 30 · 20 دقيقة · 3 أخطاء", "5", "خمسة: النظري"),
     ("الفوليو روزا 12 شهر · الدروس 6 ولا 8", "6", "ستة: الفوليو"),
     ("التطبيقي: بعد 30 يوم · 3 محاولات", "7", "سبعة: التطبيقي"),
     ("البيرمي الجديد: 3 سنين · 100 · 0", "8", "تمنية: البيرمي"),
   ]),
   dict(k="map", view="north", pins=["Verona"], labels=False, at="حمزة ففيرونا: وقف", until="سلمى فبادوفا: الشهادة", box=L_BOX),
   dict(k="people", at="حمزة ففيرونا: وقف", until="سلمى فبادوفا: الشهادة", box=R_BOX, people=["man"],
        say=[dict(who=0, text="الكويز كل نهار", at=4.0, bg="green")]),
   dict(k="map", view="north", pins=["Padova"], labels=False, at="سلمى فبادوفا: الشهادة", until="وخالد فباري: فهم", box=L_BOX),
   dict(k="steps", at="سلمى فبادوفا: الشهادة", until="وخالد فباري: فهم", box=R_BOX, steps=[
     ["الطبيب", "12/2026"], ["الطلب قبل", "10/3"], ["النظري قبل", "15/6"]], gap=2.5, check_after=0.6),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Bari", "Nador", "plane"], pins=["Bari", "Nador"], labels=False,
        at="وخالد فباري: فهم", until="إذن التلاتة عندهم", box=L_BOX),
   dict(k="people", at="وخالد فباري: فهم", until="إذن التلاتة عندهم", box=R_BOX, people=["worker"],
        say=[dict(who=0, text="غادي ندوز الامتحان", at=4.0, bg="green")]),
   dict(k="icons", at="إذن التلاتة عندهم", until="وتذكر جوج ديال الحوايج", box=ICB, items=[
     ["school", "المعلومة", "green"], ["clock", "الوقت", "gold"], ["file-text", "الوراق", "blue"]], gap=1.5),
   dict(k="vs", at="وتذكر جوج ديال الحوايج", until="وإلى كان شي حاجة", box=VSB,
        right=dict(title="التواريخ", value="6 · 12", sub="شهور", icon="calendar", color="gold"),
        left=dict(title="القراية", value="الفهم", sub="ماشي الحفظ", icon="school", color="green"), gap=5.0),
   dict(k="text", text="الفصول مكتوبة فالوصف", at="وإلى كان شي حاجة", until="والحساب ديال الفلوس", y=640, size=64, color=GOLD),
   dict(k="bars", at="والحساب ديال الفلوس", until="ودابا، سؤال ليك", box=(160, 330, 1760, 840), bars=[
     ["الدولة", 58.4, "58,40 €", "green"], ["الأوطوسكويلا", 1000, "≈ 1.000 €", "gold"], ["الخطية", 158, "158 €", "red"]], gap=2.5),
   dict(k="people", at="ودابا، سؤال ليك", until="وإلى عرفتي شي واحد", box=FULL, people=["woman", "man"],
        say=[dict(who=0, text="إيه ولا لا؟", at=2.0, bg="green")]),
   dict(k="people", at="وإلى عرفتي شي واحد", until="وإلى عجبك هاد العمل", box=FULL, people=["worker", "hijab"],
        say=[dict(who=1, text="صيفطو لصاحبك", at=1.0, bg="gold")]),
   dict(k="cta", at="وإلى عجبك هاد العمل", text="ابوني فالقناة", sub="كل نهار دليل مفيد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("البيرمي فإيطاليا من الصفر", (236, 196, 96)), "النظري والتطبيقي والوراق", "شحال كيكلف؟"],
  num="58 €", numsub="للدولة · زايد الطبيب والأوطوسكويلا",
  bottom="مغاربة إيطاليا · دليل عملي بالدارجة",
)
