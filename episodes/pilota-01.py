import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/pilota-01.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/pilota-01")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = JOB["blocks"]

S_CAL = "Regione Calabria · Ripopola Calabria (ripopola.regione.calabria.it)"
S_BOL = "Consiglio dei ministri 9/11/2026 · MASE · decreto-legge Bollette"
S_SIG = "Legge di bilancio 2026 · ddl Bilancio 2027, relazione tecnica"

BLOCKS = [
 dict(audio="../pilota-01-b01/01.wav", text=T["01"], chapter="مقدمة", src="", items=[
   dict(k="head", text="تلت خبار كيمسّو جيبك", at=0.2, until="واش عرفتي", y=380, size=110),
   dict(k="big", text="0 €", at="واش عرفتي", until="اليوم عندنا", y=470, size=280, sub="دار، إصلاح، وعشر سنين بلا كرا؟"),
   dict(k="head", text="خبار اليوم", at="اليوم عندنا"),
   dict(k="rows", at="اليوم عندنا", y=400, gap=130, rows=[
     ("الديور فابور فكالابريا", "01", "الديور فابور"),
     ("الضو غادي ينقص من يناير", "02", "الفاتورة"),
     ("الدخان غادي يغلا مرتين", "03", "والدخان"),
   ]),
 ]),
 dict(audio="02.wav", text=T["02"], chapter="01 · كالابريا", src=S_CAL, items=[
   dict(k="chapter", num="01", title="الديور فابور فكالابريا", at=0.1, until="الفكرة"),
   dict(k="head", text="Ripopola Calabria", at="الفكرة", sub="مشروع جهة كالابريا باش تعمّر القرى الصغار"),
   dict(k="stats", at="دابا الجهة", stats=[
     ("50", "دار", "خمسين دار"), ("26", "قرية", "ستة وعشرين"), ("5", "بروفينسات", "الخمس"), ("10", "سنين", "لمدة عشر"),
   ]),
   dict(k="warn", text="0 € كرا  ·  0 € إصلاح  ·  الجهة كتخلص الإصلاح", at="ونتا ما كتخلص", y=800),
 ]),
 dict(audio="03.wav", text=T["03"], chapter="01 · كالابريا", src=S_CAL, items=[
   dict(k="head", text="الشروط", at=0.2),
   dict(k="warn", text="ماشي هدية بلا شروط", at=0.2, until="الشرط الأول", y=520),
   dict(k="rows", at="الشرط الأول", y=400, gap=140, rows=[
     ("عمرك فوق 18 عام", "1", "الشرط الأول"),
     ("ساكن برا كالابريا، على الأقل 3 سنين", "2", "الشرط التاني"),
     ("تنقل الريزيدينسا للقرية وتسكن فالدار", "3", "الشرط التالت"),
   ]),
   dict(k="text", text="مثلا: ساكن فتورينو، ميلانو ولا بولونيا؟ تقدر تقدم", at="يعني إلى كنتي", until="الشرط التالت", y=800, size=44, color=GREEN),
 ]),
 dict(audio="04.wav", text=T["04"], chapter="01 · كالابريا", src=S_CAL, items=[
   dict(k="head", text="كيفاش تقدم", at=0.2),
   dict(k="rows", at=0.3, y=390, gap=130, rows=[
     ("الطلب غير أونلاين", "ripopola.regione.calabria.it", "الطلب"),
     ("الديور مازال كيتصلحو", "ماشي غدا", "والمهم", RED),
   ]),
   dict(k="pills", at="نصيحة مني", y=650, pills=[("الخدمة", "الخدمة"), ("المدرسة", "والمدرسة"), ("الطوبيس", "والطوبيس")]),
   dict(k="warn", text="شوف آخر أجل والشروط كاملة فالموقع الرسمي", at="وشوف فالموقع", y=800),
 ]),
 dict(audio="05.wav", text=T["05"], chapter="02 · الضو", src=S_BOL, items=[
   dict(k="chapter", num="02", title="فاتورة الضو", at=0.1, until="نهار تسعة"),
   dict(k="head", text="ديكري بوليتي", at="نهار تسعة", sub="وافق عليه مجلس الوزراء نهار 9 نونبر 2026"),
   dict(k="big", text="−15 €", at="الوزير", until="كيفاش", y=560, size=240, color=GREEN, sub="بمعدل، فكل ميغاواط ساعة، من يناير"),
   dict(k="rows", at="كيفاش", y=470, gap=140, rows=[
     ("سقف تمن الغاز اللي كيتصنع بيه الضو", "58,9 €/MWh", "سقف"),
     ("المدة", "أقصى حد 18 شهر", "لمدة أقصاها", WHITE),
   ]),
   dict(k="warn", text="ملي كيغلا الغاز، كيغلا معاه الضو", at="حيت فإيطاليا", y=800),
 ]),
 dict(audio="06.wav", text=T["06"], chapter="02 · الضو", src=S_BOL + " · calcolo: 2,7 MWh × 15 €", items=[
   dict(k="head", text="شحال غادي تربح؟", at=0.2),
   dict(k="big", text="2.700 kWh", at="العائلة العادية", until="إلى وصلك", y=520, size=200, color=WHITE, sub="استهلاك عائلة عادية فالعام"),
   dict(k="big", text="≈ 40 €", at="إلى وصلك", until="ولكن ماشي", y=520, size=240, color=GREEN, sub="فالعام، إلى وصلك التخفيض كامل (تقدير)"),
   dict(k="rows", at="ولكن ماشي", until="نصيحة", y=420, gap=130, rows=[
     ("الحكومة", "−15 €/MWh", "ولكن ماشي"),
     ("المعارضة · فالشهر", "1,4 €", "واحد من المعارضة", WHITE),
   ]),
   dict(k="warn", text="ديكري: خاص البرلمان يصادق عليه ف60 يوم", at="والديكري", until="نصيحة", y=740),
   dict(k="big", text="كونطرا بتمن ثابت؟", at="نصيحة", y=500, size=130, color=GOLD, sub="يمكن ما يبانش ليك التخفيض دغيا · شوف الكونطرا ديالك"),
 ]),
 dict(audio="../pilota-01-b07/07.wav", text=T["07"], chapter="03 · الدخان", src=S_SIG, items=[
   dict(k="chapter", num="03", title="الدخان غادي يغلا", at=0.1, until="المرة الأولى"),
   dict(k="head", text="جوج زيادات ف2027", at="المرة الأولى", sub="تقديرات رسمية، الثمن كيتبدل من ماركة لماركة"),
   dict(k="rows", at="المرة الأولى", y=480, gap=150, size=56, rows=[
     ("يناير 2027 · للباكية", "≈ +0,25 €", "المرة الأولى"),
     ("فاتح يوليوز 2027 · للباكية", "≈ +0,13 €", "المرة التانية"),
   ]),
   dict(k="text", text="الأتشيزا: من 32 حتى 35,50 € لكل 1000 سيجارة", at="الضريبة", until="المرة التانية", y=720, size=42, color=GREY),
   dict(k="warn", text="زيادة يوليوز مازال فقانون الميزانية، ما تصادقش عليها", at="رد البال", y=780),
 ]),
 dict(audio="08.wav", text=T["08"], chapter="ملخص", src="Fonti complete nella descrizione", items=[
   dict(k="head", text="ملخص اليوم", at=0.2, until="ونتا"),
   dict(k="rows", at=0.3, until="ونتا", y=400, gap=130, rows=[
     ("الديور فابور فكالابريا", "01", "الديور"), ("الضو غادي ينقص", "02", "الضو"), ("الدخان غادي يغلا", "03", "والدخان", RED),
   ]),
   dict(k="big", text="ونتا؟", at="ونتا", until="وإلى عجبك", y=450, size=200, color=GOLD, sub="تقدر تسكن فقرية صغيرة فكالابريا عشر سنين؟ كتب لينا فالكومونتير"),
   dict(k="cta", at="وإلى عجبك", text="ابوني فالقناة", sub="كل نهار خبر مفيد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("ديور فابور", (236, 196, 96)), "فكالابريا", "+ الضو والدخان"],
  num="0 €", numsub="كرا لمدة 10 سنين",
  bottom="كالابريا · فاتورة الضو · الدخان 2027",
)
