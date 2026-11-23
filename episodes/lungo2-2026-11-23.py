import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_J1 = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-23-f.json"), encoding="utf-8"))
_J2 = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-23-r.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo2-2026-11-23-final")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = {k: v.replace("گ", "ك") for k, v in {**_J1["blocks"], **_J2["blocks"]}.items()}
# finali non pronunciati dal TTS (A: "يلاه نبداو" assente; D: troncato dopo "عندهم" → tagliato a 176,42 s)
T["A"] = T["A"].replace(" يلاه نبداو.", "")
T["D"] = T["D"].replace(" حتى يخرج القرار.", ".")

S_HOME = "مغاربة إيطاليا · دليل عملي بالدارجة"
S_REQ = "Farnesina (visti, diniego) · Ambasciata d'Italia a Rabat (checklist 22/4/2026) · Tabella A Dir. 1/3/2000"
S_IT = "Ambasciata d'Italia a Rabat (checklist turismo/invito) · VFS Global Casablanca (checklist turismo)"
S_MA = "Ambasciata d'Italia a Rabat (VERS. 22.04.2026) · VFS Global Casablanca (checklist turismo)"
S_STEP = "Consolato Generale Casablanca · VFS Global · Farnesina (termini) · art. 7 D.Lgs. 286/1998"
S_CASI = "Ambasciata d'Italia a Rabat · VFS Global · InfoImmigrazione · Farnesina"
S_ERR = "Farnesina (diniego visto: TAR Lazio 60 giorni) · art. 7 TUI (500-3.500 €) · Ambasciata Rabat"
S_QA = "Fonti dei capitoli 01-07"
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850); FULL = (160, 300, 1760, 860); MID = (260, 220, 1660, 840)
ICB = (160, 330, 1760, 860); VSB = (260, 220, 1660, 820); BARB = (160, 330, 1760, 840)

MED_BO = dict(view="med", hl=["ITA", "MAR"], route=["Casablanca", "Bologna", "plane"], pins=["Casablanca", "Bologna"], labels=False)
MED_MI = dict(view="med", hl=["ITA", "MAR"], route=["Beni Mellal", "Milano", "plane"], pins=["Beni Mellal", "Milano"], labels=False)
MED_TO = dict(view="med", hl=["ITA", "MAR"], route=["Tanger", "Genova", "ship"], pins=["Tanger", "Torino"], labels=False)

BLOCKS = [
 # ---------------------------------------------------------------- 01
 dict(audio="A.wav", text=T["A"], chapter="01 · شكون خاصو هاد الدليل", src=S_HOME, items=[
   dict(k="head", text="الفيزا ديال الزيارة لإيطاليا", at=0.2, until="بزاف ديال الناس كيسولونا", sub="الواليدين والعائلة من المغرب · خطوة بخطوة"),
   dict(k="people", at=0.8, until="بزاف ديال الناس كيسولونا", box=FULL, people=["elder", "woman", "man"],
        say=[dict(who=0, text="بغيت نشوف الحفاد", at=3.0, bg="gold"), dict(who=2, text="شنو خاصها؟", at=7.0, bg="green")]),
   dict(k="people", at="بزاف ديال الناس كيسولونا", until="قبل ما نبداو", box=FULL, people=["hijab", "man"],
        say=[dict(who=0, text="شحال كتخلص؟", at=1.5, bg="gold"), dict(who=1, text="شحال كتسنى؟", at=4.0, bg="green")]),
   dict(k="vs", at="قبل ما نبداو", until="باش يكون الشرح واضح", box=VSB,
        right=dict(title="فيزا الزيارة", value="90 يوم", sub="فكل 180 يوم", icon="plane", color="green"),
        left=dict(title="التجمع العائلي", value="بيرميسو", sub="دليل بوحدو", icon="home", color="gold"), gap=6.0),
   dict(k="map", at="الأول، كريم ساكن", until="التانية، نادية", box=L_BOX, **MED_BO),
   dict(k="people", at="الأول، كريم ساكن", until="التانية، نادية", box=R_BOX, people=["man", "elder"],
        say=[dict(who=1, text="68 عام · شهرين", at=4.0, bg="gold")]),
   dict(k="map", at="التانية، نادية", until="والتالت، يوسف", box=L_BOX, **MED_MI),
   dict(k="people", at="التانية، نادية", until="والتالت، يوسف", box=R_BOX, people=["woman", "elder"],
        say=[dict(who=1, text="متقاعد · شهر", at=4.0, bg="green")]),
   dict(k="map", at="والتالت، يوسف", until="فهاد الدليل غادي", box=L_BOX, **MED_TO),
   dict(k="people", at="والتالت، يوسف", until="فهاد الدليل غادي", box=R_BOX, people=["man", "worker"],
        say=[dict(who=1, text="15 يوم فالصيف", at=3.0, bg="blue")]),
   dict(k="rows", at="فهاد الدليل غادي", until="وكل رقم فهاد الفيديو", y=215, gap=78, size=40, rows=[
     ("شكون خاصو هاد الدليل", "01", "الأول، شكون"),
     ("الشروط", "02", "التاني، الشروط"),
     ("الوراق فإيطاليا", "03", "التالت، الوراق"),
     ("الوراق فالمغرب", "04", "الرابع، الوراق"),
     ("الخطوات والثمن والمدة", "05", "الخامس، الخطوات"),
     ("الحالات الخاصة", "06", "السادس، الحالات"),
     ("الأخطاء والرفض", "07", "السابع، الأخطاء"),
     ("سؤال وجواب", "08", "التامن، سؤال"),
     ("اللائحة النهائية", "09", "والتاسع، لائحة"),
   ]),
   dict(k="icons", at="وكل رقم فهاد الفيديو", until="وعقل مزيان", box=ICB, items=[
     ["world", "الخارجية الإيطالية", "blue"], ["building-bank", "السفارة فالرباط", "gold"], ["file-text", "القنصلية فكازا", "green"]], gap=2.5),
   dict(k="warn", text="محتوى إخباري · ماشي استشارة قانونية", at="وعقل مزيان", until="علاش هاد الموضوع مهم", y=600),
   dict(k="icons", at="علاش هاد الموضوع مهم", until="وكل رفض كيضيع", box=ICB, items=[
     ["file-text", "ورقة ناقصة", "red"], ["building-bank", "كشف ما واضحش", "red"], ["stethoscope", "أسورانس ناقصة", "red"]], gap=2.0),
   dict(k="big", text="رفض", sub="الفلوس والوقت", at="وكل رفض كيضيع", until="وغادي نشوفو حتى", color=RED),
   dict(k="calendar", at="وغادي نشوفو حتى", until="وإلى عندك سؤال على", box=R_BOX, day=48, month="ساعة", sub="التصريح بالاستضافة"),
   dict(k="people", at="وغادي نشوفو حتى", until="وإلى عندك سؤال على", box=L_BOX, people=["office"],
        say=[dict(who=0, text="ما تنساهش", at=2.0, bg="red")]),
   dict(k="people", at="وإلى عندك سؤال على", until=None, box=FULL, people=["student", "hijab"],
        say=[dict(who=0, text="كتب سؤالك", at=1.0, bg="green")]),
 ]),
 # ---------------------------------------------------------------- 02
 dict(audio="B.wav", text=T["B"], chapter="02 · الشروط", src=S_REQ, items=[
   dict(k="chapter", num="02", title="الشروط ديال الفيزا", at=0.1, until="الفيزا اللي كنهضرو عليها"),
   dict(k="icons", at="الفيزا اللي كنهضرو عليها", until="والقاعدة الكبيرة", box=ICB, items=[
     ["plane", "فيزا سي", "blue"], ["camera", "السياحة", "gold"], ["users", "العائلة والصحاب", "green"]], gap=2.5),
   dict(k="big", text="90 / 180", sub="يوم · ماكسيموم", at="والقاعدة الكبيرة", until="مثلا، الواليدة ديال كريم"),
   dict(k="calendar", at="مثلا، الواليدة ديال كريم", until="ولكن عقل: القنصلية", box=R_BOX, day=28, month=9, sub="دخول 1/7 · آخر نهار"),
   dict(k="map", at="مثلا، الواليدة ديال كريم", until="ولكن عقل: القنصلية", box=L_BOX, **MED_BO),
   dict(k="people", at="ولكن عقل: القنصلية", until="ومثال آخر", box=FULL, people=["clerk"],
        say=[dict(who=0, text="المدة مكتوبة فالفيزا", at=1.5, bg="gold")]),
   dict(k="steps", at="ومثال آخر", until="دابا الشروط واحد", box=MID, steps=[
     ["الصيف · شهرين", "60"], ["نونبر · رجعة", "?"], ["كنحسبو 180 يوم اللي فاتو", "90"]], gap=3.0, check_after=0.6),
   dict(k="icons", at="دابا الشروط واحد", until="وفيه على الأقل جوج", box=ICB, items=[
     ["e-passport", "3 شهور من بعد", "green"], ["calendar", "أقل من 10 سنين", "gold"]], gap=4.0),
   dict(k="icons", at="وفيه على الأقل جوج", until="الشرط التاني هو الهدف", box=ICB, items=[
     ["file-text", "جوج صفحات خاويين", "blue"], ["alert-triangle", "جدد قبل الموعد", "red"]], gap=3.0),
   dict(k="people", at="الشرط التاني هو الهدف", until="الشرط التالت هو الفلوس", box=FULL, people=["elder", "clerk"],
        say=[dict(who=1, text="علاش جاي؟ فين؟ شحال؟", at=1.5, bg="blue"), dict(who=0, text="عند ولدي فبولونيا", at=6.0, bg="green")]),
   dict(k="head", text="جدول مرجعي · وزارة الداخلية", at="الشرط التالت هو الفلوس", until="الواليدة ديال كريم، بوحدها", sub="السياحة · Tabella A 2000"),
   dict(k="bars", at="الواليدة ديال كريم، بوحدها", until="هادو أرقام مرجعية", box=BARB, bars=[
     ["الواليدة · 60 يوم", 1880, "1.880 €", "gold"], ["جوج · 30 يوم", 1260, "1.260 €", "green"], ["خو يوسف · 15 يوم", 602, "602 €", "blue"]], gap=3.5),
   dict(k="warn", text="أرقام مرجعية · ماشي ثمن كتخلصو", at="هادو أرقام مرجعية", until="وإلى كان الزائر ما عندوش", y=620),
   dict(k="people", at="وإلى كان الزائر ما عندوش", until="الشرط الرابع هو الأسورانس", box=FULL, people=["man", "elder"],
        say=[dict(who=0, text="أنا نتكلف", at=2.5, bg="green"), dict(who=1, text="ولدي", at=5.0, bg="gold")]),
   dict(k="big", text="30.000 €", sub="الأسورانس · على الأقل", at="الشرط الرابع هو الأسورانس", until="الشرط الخامس هو الوضعية"),
   dict(k="icons", at="الشرط الخامس هو الوضعية", until="وحاجة مهمة بزاف", box=ICB, items=[
     ["briefcase", "خدمة", "blue"], ["wallet", "تقاعد", "gold"], ["building-store", "تجارة", "green"], ["users", "عائلة", "blue"]], gap=1.8),
   dict(k="vs", at="وحاجة مهمة بزاف", until="وحتى بالفيزا فاليد", box=VSB,
        right=dict(title="حق", value="لا", sub="ماشي أوتوماتيكي", icon="x", color="red"),
        left=dict(title="مصلحة مشروعة", value="القنصلية", sub="كتقرر من الملف", icon="scale", color="gold"), gap=4.0),
   dict(k="map", view="italy", pins=["Milano"], labels=False, at="وحتى بالفيزا فاليد", until="والقنصلية تقدر تطلب", box=L_BOX),
   dict(k="people", at="وحتى بالفيزا فاليد", until="والقنصلية تقدر تطلب", box=R_BOX, people=["office"],
        say=[dict(who=0, text="الحدود كتعاود تشوف", at=1.5, bg="blue")]),
   dict(k="people", at="والقنصلية تقدر تطلب", until="ودابا نمشيو للوراق", box=FULL, people=["clerk", "hijab"],
        say=[dict(who=0, text="ورقة زايدة؟", at=1.0, bg="gold"), dict(who=1, text="ها هي", at=3.5, bg="green")]),
   dict(k="text", text="الوراق اللي خاصك نتا", at="ودابا نمشيو للوراق", y=520, size=90, color=GOLD),
 ]),
 # ---------------------------------------------------------------- 03
 dict(audio="C.wav", text=T["C"], chapter="03 · الوراق فإيطاليا", src=S_IT, items=[
   dict(k="chapter", num="03", title="الوراق ديالك فإيطاليا", at=0.1, until="هنا الدور ديال"),
   dict(k="map", view="north", pins=["Bologna", "Milano", "Torino"], labels=False, at="هنا الدور ديال", until="الورقة الأولى والأهم", box=(160, 200, 1760, 880)),
   dict(k="big", text="1", sub="الرسالة ديال الدعوة", at="الورقة الأولى والأهم", until="فيه كتكتب المعلومات"),
   dict(k="icons", at="فيه كتكتب المعلومات", until="كتسنيه بيدك", box=ICB, items=[
     ["user", "نتا", "blue"], ["users", "الضيف والعلاقة", "gold"], ["home", "العنوان", "green"], ["calendar", "المدة", "blue"]], gap=2.5),
   dict(k="calendar", at="كتسنيه بيدك", until="الورقة التانية هي نسخة", box=R_BOX, day=6, month="شهور", sub="ماكسيموم · عمر الرسالة"),
   dict(k="people", at="كتسنيه بيدك", until="الورقة التانية هي نسخة", box=L_BOX, people=["man"],
        say=[dict(who=0, text="سنيتها", at=1.0, bg="green")]),
   dict(k="icons", at="الورقة التانية هي نسخة", until="الورقة التالتة هي الوراق", box=ICB, items=[
     ["id", "الهوية", "blue"], ["license", "البيرميسو صالح", "green"], ["home", "شهادة الريزيدينسا", "gold"]], gap=3.0),
   dict(k="icons", at="الورقة التالتة هي الوراق", until="اللائحة كتقول: إلى كان", box=ICB, items=[
     ["receipt", "البوسطات", "blue"], ["file-certificate", "الكونطرا", "green"], ["report-money", "730 / CU", "gold"]], gap=2.5),
   dict(k="people", at="اللائحة كتقول: إلى كان", until="الورقة الرابعة هي الدليل", box=FULL, people=["elder", "student", "man"],
        say=[dict(who=2, text="المدخول ديالي + القرابة", at=4.0, bg="gold")]),
   dict(k="map", at="الورقة الرابعة هي الدليل", until="الورقة الخامسة هي السكن", box=L_BOX, **MED_BO),
   dict(k="icons", at="الورقة الرابعة هي الدليل", until="الورقة الخامسة هي السكن", box=R_BOX, items=[
     ["file-text", "عقد الازدياد", "gold"], ["file-certificate", "ترجمة", "blue"]], gap=3.0),
   dict(k="vs", at="الورقة الخامسة هي السكن", until="دابا نرجعو للأمثلة", box=VSB,
        right=dict(title="عندك", value="الرسالة", sub="فيها العنوان", icon="home", color="green"),
        left=dict(title="أوطيل", value="حجز", sub="ديال الأوطيل", icon="building-store", color="blue"), gap=3.0),
   dict(k="map", view="north", pins=["Bologna"], labels=False, at="دابا نرجعو للأمثلة", until="حيت الواليدة ديالو", box=L_BOX),
   dict(k="steps", at="دابا نرجعو للأمثلة", until="حيت الواليدة ديالو", box=R_BOX, steps=[
     ["الرسالة", "1"], ["الباسبور + البيرميسو", "2"], ["الريزيدينسا", "3"], ["البوسطات + الكونطرا", "4"]], gap=2.5, check_after=0.5),
   dict(k="people", at="حيت الواليدة ديالو", until="نادية فميلانو", box=FULL, people=["man", "elder"],
        say=[dict(who=0, text="أنا اللي متكلف بكلشي", at=1.5, bg="gold")]),
   dict(k="map", view="north", pins=["Milano"], labels=False, at="نادية فميلانو", until="يوسف فتورينو", box=L_BOX),
   dict(k="people", at="نادية فميلانو", until="يوسف فتورينو", box=R_BOX, people=["woman"],
        say=[dict(who=0, text="بابا عندو البانسيون", at=2.0, bg="green")]),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="يوسف فتورينو", until="وجوج نصائح", box=L_BOX),
   dict(k="people", at="يوسف فتورينو", until="وجوج نصائح", box=R_BOX, people=["man"],
        say=[dict(who=0, text="الرسالة والسكن", at=2.0, bg="blue")]),
   dict(k="vs", at="وجوج نصائح", until="والتانية: إلى البيرميسو", box=VSB,
        right=dict(title="مزيان", value="PDF", sub="واضح ومقروء", icon="file-text", color="green"),
        left=dict(title="لا", value="تصاور", sub="مضببة", icon="x", color="red"), gap=2.5),
   dict(k="people", at="والتانية: إلى البيرميسو", until="ومن دابا، خلي نسخة", box=FULL, people=["worker", "clerk"],
        say=[dict(who=0, text="عندي غير الريسيفوطا", at=1.0, bg="gold"), dict(who=1, text="سول قبل", at=5.0, bg="blue")]),
   dict(k="calendar", at="ومن دابا، خلي نسخة", until="والرسالة خاصها تكون بنفس", box=R_BOX, day=48, month="ساعة", sub="التصريح · الفصل 05"),
   dict(k="icons", at="ومن دابا، خلي نسخة", until="والرسالة خاصها تكون بنفس", box=L_BOX, items=[
     ["e-passport", "نسخة الباسبور", "blue"], ["file-text", "نسخ الوراق", "gold"]], gap=2.0),
   dict(k="icons", at="والرسالة خاصها تكون بنفس", until="ودابا نمشيو للمغرب", box=ICB, items=[
     ["file-text", "الرسالة", "gold"], ["ticket", "الحجز", "blue"], ["stethoscope", "الأسورانس", "green"]], gap=1.5),
   dict(k="text", text="نفس التواريخ · نفس العنوان", at="ودابا نمشيو للمغرب", y=520, size=80, color=GOLD),
 ]),
 # ---------------------------------------------------------------- 04
 dict(audio="D.wav", text=T["D"], chapter="04 · الوراق فالمغرب", src=S_MA, items=[
   dict(k="chapter", num="04", title="الوراق فالمغرب", at=0.1, until="والسفارة فالرباط عندها"),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Rabat"], labels=False,
        at="والسفارة فالرباط عندها", until="وكل واحد فالعائلة", box=(160, 200, 1760, 880)),
   dict(k="people", at="وكل واحد فالعائلة", until="الأول، الاستمارة", box=FULL, people=["elder", "woman", "child"],
        say=[dict(who=2, text="ملف ديالي بوحدي", at=2.0, bg="green")]),
   dict(k="steps", at="الأول، الاستمارة", until="الرابع، حجز", box=MID, steps=[
     ["الاستمارة مسنية", "1"], ["تصويرة 3,5 × 4,5", "2"], ["الباسبور + النسخ", "3"]], gap=4.0, check_after=0.6),
   dict(k="steps", at="الرابع، حجز", until="السابع، وهو اللي", box=MID, steps=[
     ["حجز رايح جاي", "4"], ["السكن", "5"], ["الأسورانس 30.000 €", "6"]], gap=3.0, check_after=0.6),
   dict(k="icons", at="السابع، وهو اللي", until="وعقل: اللائحة ديال الدعوة", box=ICB, items=[
     ["briefcase", "شهادة العمل", "blue"], ["id", "الضمان الاجتماعي", "green"], ["receipt", "3 ورقات الأجرة", "gold"], ["building-bank", "الكشوفات", "blue"]], gap=2.5),
   dict(k="vs", at="وعقل: اللائحة ديال الدعوة", until="إلى كان متقاعد", box=VSB,
        right=dict(title="السياحة", value="3 شهور", sub="الكشوفات", icon="building-bank", color="blue"),
        left=dict(title="الدعوة · الخدامين", value="6 شهور", sub="جيب 6", icon="building-bank", color="gold"), gap=3.0),
   dict(k="icons", at="إلى كان متقاعد", until="إلى كان فلاح", box=ICB, items=[
     ["wallet", "شهادة التقاعد", "gold"], ["building-store", "السجل التجاري", "blue"], ["receipt-tax", "التصريح الضريبي", "green"]], gap=3.0),
   dict(k="icons", at="إلى كان فلاح", until="وهنا كتجي الترجمة", box=ICB, items=[
     ["tractor", "غرفة الفلاحة", "green"], ["users", "شكون متكلف", "gold"], ["cash", "إيصالات التحويل", "blue"]], gap=3.5),
   dict(k="people", at="وهنا كتجي الترجمة", until="والمركز كيطلب جوج", box=FULL, people=["clerk", "elder"],
        say=[dict(who=0, text="ترجمة للطاليانية", at=1.5, bg="blue"), dict(who=0, text="والأبوستي", at=6.0, bg="gold")]),
   dict(k="vs", at="والمركز كيطلب جوج", until="نرجعو للأمثلة", box=VSB,
        right=dict(title="الملف 1", value="الأصل", sub="", icon="file-certificate", color="green"),
        left=dict(title="الملف 2", value="نسخ A4", sub="", icon="file-text", color="blue"), gap=2.0),
   dict(k="map", at="نرجعو للأمثلة", until="الواليد ديال نادية", box=L_BOX, **MED_BO),
   dict(k="steps", at="نرجعو للأمثلة", until="الواليد ديال نادية", box=R_BOX, steps=[
     ["الوراق العادية", "1"], ["وراق كريم", "2"], ["عقد ازدياد مترجم", "3"], ["إيصالات التحويل", "4"]], gap=3.0, check_after=0.5),
   dict(k="map", at="الواليد ديال نادية", until="خو يوسف، فطنجة", box=L_BOX, **MED_MI),
   dict(k="people", at="الواليد ديال نادية", until="خو يوسف، فطنجة", box=R_BOX, people=["elder", "woman"],
        say=[dict(who=0, text="شهادة التقاعد", at=1.5, bg="gold"), dict(who=1, text="ملف بوحدي", at=6.0, bg="green")]),
   dict(k="map", at="خو يوسف، فطنجة", until="ونصيحة أخيرة", box=L_BOX, **MED_TO),
   dict(k="icons", at="خو يوسف، فطنجة", until="ونصيحة أخيرة", box=R_BOX, items=[
     ["briefcase", "شهادة العمل", "blue"], ["building-bank", "الكشوفات", "gold"]], gap=2.0),
   dict(k="vs", at="ونصيحة أخيرة", until="وإلى كانت شي ورقة", box=VSB,
        right=dict(title="مزيان", value="حساب عادي", sub="مع الإيصالات", icon="building-bank", color="green"),
        left=dict(title="شك", value="فلوس فجأة", sub="بلا تفسير", icon="alert-triangle", color="red"), gap=4.0),
   dict(k="people", at="وإلى كانت شي ورقة", until=None, box=FULL, people=["clerk"],
        say=[dict(who=0, text="الباسبور عندنا حتى القرار", at=2.0, bg="blue")]),
 ]),
 # ---------------------------------------------------------------- 05
 dict(audio="E.wav", text=T["E"], chapter="05 · الخطوات والثمن والمدة", src=S_STEP, items=[
   dict(k="chapter", num="05", title="الخطوات والثمن والمدة", at=0.1, until="الخطوة الأولى"),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Rabat"], labels=False, at="الخطوة الأولى", until="الخطوة التانية", box=L_BOX),
   dict(k="vs", at="الخطوة الأولى", until="الخطوة التانية", box=R_BOX,
        right=dict(title="الرباط", value="السفارة", sub="سلا · تمارة · الخميسات", icon="building-bank", color="blue"),
        left=dict(title="المدن الأخرى", value="كازا", sub="القنصلية العامة", icon="building-bank", color="gold"), gap=4.0),
   dict(k="steps", at="الخطوة التانية", until="يعني إلى شي واحد", box=MID, steps=[
     ["الموعد أونلاين", "1"], ["الموقع الرسمي ديال المركز", "2"], ["بلا وسيط", "3"]], gap=3.0, check_after=0.6),
   dict(k="people", at="يعني إلى شي واحد", until="الخطوة التالتة", box=FULL, people=["man", "worker"],
        say=[dict(who=0, text="عطيني الفلوس نجيب ليك الموعد", at=0.8, bg="red"), dict(who=1, text="لا شكرا", at=4.0, bg="green")]),
   dict(k="vs", at="الخطوة التالتة", until="مثلا، الواليدة ديال كريم", box=VSB,
        right=dict(title="من", value="6 شهور", sub="قبل السفر", icon="calendar", color="green"),
        left=dict(title="حتى", value="15 يوم", sub="قبل السفر · عادة", icon="clock", color="red"), gap=3.0),
   dict(k="rows", at="مثلا، الواليدة ديال كريم", until="ولكن ما تسناش اللخر", y=280, gap=110, size=48, rows=[
     ("السفر", "1/7/2027", "مثلا، الواليدة"),
     ("أول نهار للطلب", "1/1/2027", "تقدر تطلب من", GREEN),
     ("آخر أجل عادي", "16/6/2027", "وآخر أجل عادي", RED),
   ]),
   dict(k="people", at="ولكن ما تسناش اللخر", until="الخطوة الرابعة", box=FULL, people=["office", "man"],
        say=[dict(who=0, text="حتى 45 يوم", at=1.5, bg="gold"), dict(who=1, text="نطلب 2-3 شهور قبل", at=6.0, bg="green")]),
   dict(k="icons", at="الخطوة الرابعة", until="والثمن؟", box=ICB, items=[
     ["user", "بنفسو", "blue"], ["file-text", "الأصل والنسخ", "gold"], ["fingerprint", "البصمات", "green"]], gap=2.5),
   dict(k="bars", at="والثمن؟", until="ومن فوق كاين الثمن", box=BARB, bars=[
     ["الكبار", 90, "90 €", "gold"], ["6-12 عام", 45, "45 €", "blue"], ["تحت 6", 1, "0 €", "green"]], gap=2.5),
   dict(k="big", text="≈ 336 MAD", sub="الخدمة ديال المركز · للطلب", at="ومن فوق كاين الثمن", until="مثلا الواليدين ديال نادية"),
   dict(k="map", at="مثلا الواليدين ديال نادية", until="وزيد عليهم الأسورانس", box=L_BOX, **MED_MI),
   dict(k="rows", at="مثلا الواليدين ديال نادية", until="وزيد عليهم الأسورانس", y=300, gap=120, size=50, rows=[
     ("2 فيزات", "180 €", "جوج ديال الفيزات"),
     ("2 خدمة", "≈ 672 MAD", "زايد جوج ديال الخدمة", GOLD),
   ]),
   dict(k="icons", at="وزيد عليهم الأسورانس", until="الخطوة الخامسة", box=ICB, items=[
     ["stethoscope", "الأسورانس", "blue"], ["file-certificate", "الترجمة", "gold"], ["receipt", "الوصل", "green"]], gap=3.0),
   dict(k="vs", at="الخطوة الخامسة", until="الخطوة السادسة", box=VSB,
        right=dict(title="عادة", value="15 يوم", sub="", icon="clock", color="green"),
        left=dict(title="حتى", value="45 يوم", sub="دراسة أكثر", icon="clock", color="gold"), gap=3.0),
   dict(k="map", at="الخطوة السادسة", until="ولكن إلى دخلات من بلاد", box=L_BOX, **MED_BO),
   dict(k="people", at="الخطوة السادسة", until="ولكن إلى دخلات من بلاد", box=R_BOX, people=["office", "elder"],
        say=[dict(who=0, text="الطابع فالباسبور", at=3.0, bg="green")]),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Tanger", "Genova", "ship"], pins=["Tanger"], labels=False,
        at="ولكن إلى دخلات من بلاد", until="الخطوة السابعة", box=L_BOX),
   dict(k="calendar", at="ولكن إلى دخلات من بلاد", until="الخطوة السابعة", box=R_BOX, day=8, month="أيام", sub="التصريح بالحضور · الكيستورا"),
   dict(k="head", text="التصريح بالاستضافة", at="الخطوة السابعة", until="الواليدة وصلات نهار", sub="حتى العائلة · كتابيا"),
   dict(k="icons", at="الخطوة السابعة", until="الواليدة وصلات نهار", box=ICB, items=[
     ["building-bank", "الكيستورا", "blue"], ["id", "الكوميساريا", "gold"], ["home", "الكومون", "green"]], gap=4.0),
   dict(k="calendar", at="الواليدة وصلات نهار", until="واللي ما صرحش", box=R_BOX, day=3, month=7, sub="آخر أجل · 48 ساعة"),
   dict(k="map", view="north", pins=["Bologna"], labels=False, at="الواليدة وصلات نهار", until="واللي ما صرحش", box=L_BOX),
   dict(k="big", text="500 - 3.500 €", sub="الغرامة", at="واللي ما صرحش", until="والخطوة اللخرة", color=RED, size=150),
   dict(k="text", text="الرجوع قبل ما تسالي الفيزا", at="والخطوة اللخرة", y=520, size=80, color=GOLD),
 ]),
 # ---------------------------------------------------------------- 06
 dict(audio="F.wav", text=T["F"], chapter="06 · الحالات الخاصة", src=S_CASI, items=[
   dict(k="chapter", num="06", title="الحالات الخاصة", at=0.1, until="الحالة الأولى"),
   dict(k="people", at="الحالة الأولى", until="إلى سافر بوحدو", box=FULL, people=["elder", "child"],
        say=[dict(who=1, text="حتى أنا جاي", at=2.0, bg="green")]),
   dict(k="steps", at="إلى سافر بوحدو", until="واللي تحت أربعطاش", box=MID, steps=[
     ["بوحدو · جوج الواليدين", "1"], ["مع واحد · اللي ما مسافرش", "2"]], gap=4.0, check_after=0.6),
   dict(k="icons", at="واللي تحت أربعطاش", until="والثمن ديال الفيزا للقاصر", box=ICB, items=[
     ["file-text", "إذن المرافقة", "gold"], ["e-passport", "نسخة الباسبور", "blue"]], gap=3.0),
   dict(k="bars", at="والثمن ديال الفيزا للقاصر", until="الحالة التانية", box=BARB, bars=[
     ["6-12 عام", 45, "45 €", "blue"], ["تحت 6", 1, "0 €", "green"]], gap=2.0),
   dict(k="map", at="الحالة التانية", until="الحالة التالتة", box=L_BOX, **MED_TO),
   dict(k="icons", at="الحالة التانية", until="الحالة التالتة", box=R_BOX, items=[
     ["car", "الكارط كريز", "blue"], ["license", "البيرمي", "gold"], ["file-certificate", "الكارط الخضرا", "green"]], gap=4.0),
   dict(k="people", at="الحالة التالتة", until="الحالة الرابعة", box=FULL, people=["man", "clerk"],
        say=[dict(who=0, text="عندي الجنسية", at=2.0, bg="green"), dict(who=1, text="لائحة خاصة", at=7.0, bg="gold")]),
   dict(k="vs", at="الحالة الرابعة", until="الحالة الخامسة", box=VSB,
        right=dict(title="زيارة", value="العائلة", sub="هاد الدليل", icon="users", color="green"),
        left=dict(title="علاج", value="فيزا أخرى", sub="لائحة بوحدها", icon="building-hospital", color="red"), gap=3.0),
   dict(k="people", at="الحالة الخامسة", until="شوف الدليل ديالنا", box=FULL, people=["elder", "woman"],
        say=[dict(who=0, text="بغينا نبقاو معاك", at=1.5, bg="gold"), dict(who=1, text="التجمع العائلي", at=8.0, bg="blue")]),
   dict(k="text", text="الدليل: التجمع العائلي (12/11)", at="شوف الدليل ديالنا", until="الحالة السادسة", y=520, size=70, color=GOLD),
   dict(k="people", at="الحالة السادسة", until="الحالة السابعة", box=FULL, people=["office"],
        say=[dict(who=0, text="من بعد المدة = خطر الطرد", at=2.0, bg="red")]),
   dict(k="map", view="north", pins=["Torino"], labels=False, at="الحالة السابعة", until="الحالة التامنة", box=L_BOX),
   dict(k="big", text="602 €", sub="مرجع · 15 يوم", at="الحالة السابعة", until="الحالة التامنة", x=1380, y=470, size=180),
   dict(k="icons", at="الحالة التامنة", until="الحالة التاسعة", box=ICB, items=[
     ["e-passport", "الفيزات القديمة", "green"], ["check", "رجع فالوقت", "green"], ["file-text", "الطوابع", "blue"]], gap=3.0),
   dict(k="map", view="maroc", hl=["MAR"], pins=["Rabat"], labels=False, at="الحالة التاسعة", until=None, box=L_BOX),
   dict(k="icons", at="الحالة التاسعة", until=None, box=R_BOX, items=[
     ["id", "بطاقة الإقامة", "gold"], ["file-text", "الوصل", "blue"]], gap=3.0),
 ]),
 # ---------------------------------------------------------------- 07
 dict(audio="G.wav", text=T["G"], chapter="07 · الأخطاء والرفض", src=S_ERR, items=[
   dict(k="chapter", num="07", title="الأخطاء والرفض", at=0.1, until="الخطأ الأول"),
   dict(k="people", at="الخطأ الأول", until="الخطأ التاني", box=FULL, people=["clerk", "elder"],
        say=[dict(who=0, text="الباسبور قريب يسالي", at=1.0, bg="red")]),
   dict(k="steps", bad=True, at="الخطأ التاني", until="الخطأ الرابع", box=MID, steps=[
     ["رسالة قديمة ولا ناقصة", "2"], ["بلا ترجمة ولا أبوستي", "3"]], gap=4.0, check_after=0.6),
   dict(k="vs", at="الخطأ الرابع", until="الخطأ الخامس", box=VSB,
        right=dict(title="الإقامة", value="شهرين", sub="", icon="calendar", color="gold"),
        left=dict(title="الأسورانس", value="شهر", sub="ناقصة", icon="stethoscope", color="red"), gap=3.0),
   dict(k="steps", bad=True, at="الخطأ الخامس", until="الخطأ السابع", box=MID, steps=[
     ["فلوس فجأة", "5"], ["ماشي بالترتيب", "6"]], gap=3.0, check_after=0.6),
   dict(k="people", at="الخطأ السابع", until="الخطأ التامن", box=FULL, people=["man", "hijab"],
        say=[dict(who=0, text="عندي موعد للبيع", at=1.0, bg="red"), dict(who=1, text="غير الموقع الرسمي", at=4.0, bg="green")]),
   dict(k="warn", text="حجز مزور = مشكل كبير", at="الخطأ التامن", until="الخطأ التاسع", y=600),
   dict(k="calendar", at="الخطأ التاسع", until="والغرامة من خمس", box=R_BOX, day=48, month="ساعة", sub="التصريح بالاستضافة"),
   dict(k="icons", at="الخطأ التاسع", until="والغرامة من خمس", box=L_BOX, items=[
     ["user", "نتا", "blue"], ["e-passport", "الضيف", "gold"], ["home", "العنوان", "green"]], gap=2.5),
   dict(k="big", text="500 €", sub="الغرامة · من", at="والغرامة من خمس", until="وخطأ كيتعاود بزاف", color=RED),
   dict(k="icons", at="وخطأ كيتعاود بزاف", until="والخطأ العاشر", box=ICB, items=[
     ["file-text", "الرسالة", "red"], ["ticket", "الحجز", "red"], ["stethoscope", "الأسورانس", "red"]], gap=1.5),
   dict(k="people", at="والخطأ العاشر", until="دابا، إلى جا الرفض", box=FULL, people=["office"],
        say=[dict(who=0, text="وضعية غير قانونية", at=1.5, bg="red")]),
   dict(k="people", at="دابا، إلى جا الرفض", until="اقرا السبب مزيان", box=FULL, people=["elder", "man"],
        say=[dict(who=0, text="ترفضات", at=0.8, bg="red"), dict(who=1, text="شنو السبب؟", at=4.0, bg="gold")]),
   dict(k="icons", at="اقرا السبب مزيان", until="ثانيا، الطعن", box=ICB, items=[
     ["file-text", "ورقة ناقصة", "gold"], ["wallet", "الفلوس", "gold"], ["map-pin", "الهدف", "gold"]], gap=2.5),
   dict(k="map", view="italy", pins=["Roma"], labels=False, at="ثانيا، الطعن", until="هادشي كيعني أنك محتاج", box=L_BOX),
   dict(k="calendar", at="ثانيا، الطعن", until="هادشي كيعني أنك محتاج", box=R_BOX, day=60, month="يوم", sub="الطعن · المحكمة الإدارية لاتسيو"),
   dict(k="people", at="هادشي كيعني أنك محتاج", until="ثالثا، قبل ما تفكر", box=FULL, people=["office", "man"],
        say=[dict(who=0, text="محامي", at=1.0, bg="blue"), dict(who=1, text="ولا نصلح الملف؟", at=6.0, bg="gold")]),
   dict(k="steps", at="ثالثا، قبل ما تفكر", until="مثال: الواليدة ديال كريم", box=MID, steps=[
     ["اقرا السبب", "1"], ["صلح الملف", "2"], ["عاود الطلب", "3"]], gap=3.5, check_after=0.6),
   dict(k="map", view="north", pins=["Bologna"], labels=False, at="مثال: الواليدة ديال كريم", until="هادا مثال من عندنا", box=L_BOX),
   dict(k="vs", at="مثال: الواليدة ديال كريم", until="هادا مثال من عندنا", box=R_BOX,
        right=dict(title="السبب", value="الفلوس", sub="ما بايناش", icon="x", color="red"),
        left=dict(title="الحل", value="CU", sub="الإيصالات · الريزيدينسا", icon="file-text", color="green"), gap=4.0),
   dict(k="warn", text="مثال من عندنا · ماشي ضمانة", at="هادا مثال من عندنا", until="ونصيحة لكل العائلات", y=600),
   dict(k="people", at="ونصيحة لكل العائلات", until=None, box=FULL, people=["woman", "elder", "man"],
        say=[dict(who=1, text="الصراحة فكل ورقة", at=1.5, bg="green")]),
 ]),
 # ---------------------------------------------------------------- 08
 dict(audio="H.wav", text=T["H"], chapter="08 · سؤال وجواب", src=S_QA, items=[
   dict(k="chapter", num="08", title="سؤال وجواب", at=0.1, until="السؤال الأول"),
   dict(k="people", at="السؤال الأول", until="السؤال التاني", box=FULL, people=["hijab", "clerk"],
        say=[dict(who=0, text="ستة شهور؟", at=1.0, bg="gold"), dict(who=1, text="لا · 90 يوم", at=4.5, bg="red")]),
   dict(k="people", at="السؤال التاني", until="السؤال التالت", box=FULL, people=["man", "office"],
        say=[dict(who=0, text="نشري البيي؟", at=1.0, bg="gold"), dict(who=1, text="الحجز كافي", at=4.5, bg="green")]),
   dict(k="people", at="السؤال التالت", until="السؤال الرابع", box=L_BOX, people=["woman"],
        say=[dict(who=0, text="الأسورانس منين؟", at=1.0, bg="gold")]),
   dict(k="icons", at="السؤال التالت", until="السؤال الرابع", box=R_BOX, items=[
     ["stethoscope", "30.000 €", "green"], ["world", "كاع شنغن", "blue"], ["plane", "الرجوع", "gold"]], gap=2.0),
   dict(k="people", at="السؤال الرابع", until="السؤال الخامس", box=FULL, people=["worker", "clerk"],
        say=[dict(who=0, text="بيرميسو 2 سنين؟", at=1.0, bg="gold"), dict(who=1, text="صالح + الريزيدينسا", at=5.0, bg="green")]),
   dict(k="people", at="السؤال الخامس", until="السؤال السادس", box=FULL, people=["elder", "office"],
        say=[dict(who=0, text="نمشي بنفسي؟", at=1.0, bg="gold"), dict(who=1, text="البصمات", at=5.0, bg="blue")]),
   dict(k="map", at="السؤال السادس", until="السؤال السابع", box=L_BOX, **MED_MI),
   dict(k="rows", at="السؤال السادس", until="السؤال السابع", y=300, gap=110, size=48, rows=[
     ("2 فيزات", "180 €", "مية وتمانين أورو"),
     ("الخدمة", "≈ 672 MAD", "زايد تقريبا", GOLD),
   ]),
   dict(k="people", at="السؤال السابع", until="السؤال التامن", box=FULL, people=["man", "elder"],
        say=[dict(who=0, text="بالإيميل؟", at=1.0, bg="gold"), dict(who=1, text="الرسالة مسنية", at=5.0, bg="green")]),
   dict(k="people", at="السؤال التامن", until="وإلى سكنو فأوطيل", box=L_BOX, people=["woman"],
        say=[dict(who=0, text="وصلات · شنو ندير؟", at=1.0, bg="gold")]),
   dict(k="calendar", at="السؤال التامن", until="وإلى سكنو فأوطيل", box=R_BOX, day=48, month="ساعة", sub="التصريح بالاستضافة"),
   dict(k="icons", at="وإلى سكنو فأوطيل", until="السؤال التاسع", box=ICB, items=[
     ["building-store", "الأوطيل", "blue"], ["file-text", "النسخة ديال التصريح", "green"]], gap=2.0),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Tanger", "Genova", "ship"], pins=["Tanger"], labels=False,
        at="السؤال التاسع", until="السؤال العاشر", box=L_BOX),
   dict(k="people", at="السؤال التاسع", until="السؤال العاشر", box=R_BOX, people=["elder"],
        say=[dict(who=0, text="دخلت من إسبانيا", at=1.0, bg="gold"), dict(who=0, text="الكيستورا · 8 أيام", at=7.0, bg="blue")]),
   dict(k="people", at="السؤال العاشر", until="السؤال الحادي عشر", box=FULL, people=["man", "office"],
        say=[dict(who=0, text="ترفضات", at=1.0, bg="red"), dict(who=1, text="السبب · 60 يوم", at=4.0, bg="gold")]),
   dict(k="people", at="السؤال الحادي عشر", until="السؤال التاني عشر", box=FULL, people=["student", "worker"],
        say=[dict(who=0, text="صاحبي؟", at=1.0, bg="gold"), dict(who=1, text="إيه · بلا القرابة", at=4.0, bg="green")]),
   dict(k="people", at="السؤال التاني عشر", until="وسؤال أخير", box=FULL, people=["hijab", "man"],
        say=[dict(who=0, text="سمسار؟", at=1.0, bg="gold"), dict(who=1, text="لا · الموقع الرسمي", at=3.0, bg="red")]),
   dict(k="map", view="med", hl=["ITA", "MAR"], pins=["Bologna"], labels=False, at="وسؤال أخير", until=None, box=L_BOX),
   dict(k="people", at="وسؤال أخير", until=None, box=R_BOX, people=["elder"],
        say=[dict(who=0, text="إسبانيا ولا فرنسا؟", at=1.0, bg="gold"), dict(who=0, text="نفس 90 يوم", at=6.0, bg="blue")]),
 ]),
 # ---------------------------------------------------------------- 09
 dict(audio="I.wav", text=T["I"], chapter="09 · اللائحة النهائية", src=S_HOME, items=[
   dict(k="chapter", num="09", title="اللائحة النهائية", at=0.1, until="الوراق ديالك فإيطاليا"),
   dict(k="rows", at="الوراق ديالك فإيطاليا", until="الوراق ديال الشخص اللي جاي", y=230, gap=110, size=44, rows=[
     ("الرسالة ديال الدعوة", "1", "واحد: الرسالة"),
     ("نسخة الهوية", "2", "جوج: نسخة"),
     ("البيرميسو صالح", "3", "تلاتة: نسخة"),
     ("شهادة الريزيدينسا", "4", "ربعة: شهادة"),
     ("وراق المدخول", "5", "خمسة: الوراق"),
   ]),
   dict(k="rows", at="الوراق ديال الشخص اللي جاي", until="وعاود: الفيزا ديال الزيارة", y=200, gap=82, size=40, rows=[
     ("الاستمارة", "6", "ستة: الاستمارة"),
     ("التصويرة", "7", "سبعة: التصويرة"),
     ("الباسبور + النسخ", "8", "تمنية: الباسبور"),
     ("الحجز رايح جاي", "9", "تسعود: الحجز"),
     ("الأسورانس 30.000 €", "10", "عشرة: الأسورانس"),
     ("الخدمة والكشوفات", "11", "حداش: الوراق"),
     ("القرابة مترجمة", "12", "تناش: الدليل"),
     ("إذن القاصرين", "13", "وتلطاش: الإذن"),
   ]),
   dict(k="vs", at="وعاود: الفيزا ديال الزيارة", until="وعاود معايا الأرقام", box=VSB,
        right=dict(title="الزيارة", value="ماشي بيرميسو", sub="", icon="plane", color="gold"),
        left=dict(title="الوراق بالعربية", value="ترجمة", sub="+ الأبوستي", icon="file-certificate", color="blue"), gap=4.0),
   dict(k="rows", at="وعاود معايا الأرقام", until="ونرجعو للتواريخ", y=200, gap=80, size=40, rows=[
     ("المدة", "90 / 180", "تسعين يوم فكل"),
     ("الفيزا · الكبار", "90 €", "الفيزا تسعين"),
     ("6-12 عام · تحت 6", "45 € · 0", "خمسة وربعين للدراري"),
     ("الخدمة", "≈ 336 MAD", "الخدمة ديال المركز تقريبا"),
     ("الأسورانس", "30.000 €", "الأسورانس تلاتين"),
     ("الطلب", "6 شهور · 15 يوم", "الطلب من ستة"),
     ("القرار", "15 · 45 يوم", "القرار فخمسطاش"),
     ("الاستضافة · الحضور", "48 ساعة · 8 أيام", "التصريح بالاستضافة فتمنية", GOLD),
     ("الطعن", "60 يوم", "والطعن فستين", RED),
   ]),
   dict(k="rows", at="ونرجعو للتواريخ", until="ونرجعو للتلاتة ديالنا", y=260, gap=110, size=46, rows=[
     ("السفر", "1/7/2027", "السفر نهار واحد"),
     ("أول نهار للطلب", "1/1/2027", "الطلب ممكن", GREEN),
     ("آخر أجل عادي", "16/6/2027", "آخر أجل عادي ستاش", RED),
     ("التصريح بالاستضافة", "3/7/2027", "قبل تلاتة يوليوز", GOLD),
   ]),
   dict(k="map", at="ونرجعو للتلاتة ديالنا", until="نادية فميلانو، الواليدين", box=L_BOX, **MED_BO),
   dict(k="people", at="ونرجعو للتلاتة ديالنا", until="نادية فميلانو، الواليدين", box=R_BOX, people=["man", "elder"],
        say=[dict(who=0, text="شهرين قبل", at=3.0, bg="green")]),
   dict(k="map", at="نادية فميلانو، الواليدين", until="ويوسف فتورينو، خوه", box=L_BOX, **MED_MI),
   dict(k="people", at="نادية فميلانو، الواليدين", until="ويوسف فتورينو، خوه", box=R_BOX, people=["woman", "elder"],
        say=[dict(who=1, text="شهادة التقاعد", at=2.0, bg="gold")]),
   dict(k="map", at="ويوسف فتورينو، خوه", until="وإلى كنتي كتشوف", box=L_BOX, **MED_TO),
   dict(k="people", at="ويوسف فتورينو، خوه", until="وإلى كنتي كتشوف", box=R_BOX, people=["man", "worker"],
        say=[dict(who=1, text="الكارط الخضرا", at=2.5, bg="green")]),
   dict(k="icons", at="وإلى كنتي كتشوف", until="والفصول ديال الفيديو", box=ICB, items=[
     ["building-bank", "القنصلية", "blue"], ["world", "المركز الرسمي", "green"], ["users", "الباطرونا", "gold"]], gap=2.5),
   dict(k="text", text="الفصول والمصادر فالوصف", at="والفصول ديال الفيديو", until="ودابا، سؤال ليك", y=600, size=64, color=GOLD),
   dict(k="people", at="ودابا، سؤال ليك", until="وإلى عرفتي شي واحد", box=FULL, people=["woman", "man"],
        say=[dict(who=0, text="إيه ولا لا؟", at=3.0, bg="green")]),
   dict(k="people", at="وإلى عرفتي شي واحد", until="وإلى عجبك", box=FULL, people=["worker", "hijab"],
        say=[dict(who=1, text="صيفطو لصاحبك", at=1.0, bg="gold")]),
   dict(k="cta", at="وإلى عجبك", text="ابوني فالقناة", sub="كل نهار دليل مفيد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("فيزا الزيارة لإيطاليا", (236, 196, 96)), "جيب الواليدين من المغرب", "الوراق والثمن والمدة"],
  num="90 €", numsub="الفيزا · للكبار",
  bottom="مغاربة إيطاليا · دليل عملي بالدارجة",
)
