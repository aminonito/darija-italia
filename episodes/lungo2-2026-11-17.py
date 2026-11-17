import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = json.load(open(os.path.join(ROOT, "tts/jobs/lungo2-2026-11-17.json"), encoding="utf-8"))
AUDIO_DIR = os.path.join(ROOT, "tts/audio/lungo2-2026-11-17-final")
BRAND = "مغاربة إيطاليا"
GREY = (175, 175, 182); GOLD = (236, 196, 96); RED = (230, 90, 90); WHITE = (245, 245, 242); GREEN = (0, 190, 95)
T = dict(JOB["blocks"])
# frase con una sola fonte tagliata dall'audio (controllo YouTube)
T["D"] = T["D"].replace("كيكون أسرع، ومرات فنفس النهار.", "كيكون أسرع.")
assert "فنفس النهار" not in T["D"]
T["C"] = T["C"].replace("وتوافق، ولا تعطي بعض المعلومات على المداخيل والكونطو ديالها.", "وتوافق.")
assert "بعض المعلومات" not in T["C"]
L_BOX = (160, 250, 950, 780); R_BOX = (1000, 170, 1760, 850)

S_INTRO = "Min. Lavoro, pagina ISEE (validità fino al 31/12) · TuttoCalcolato 6/11/2026 · Fiscal Focus 10/11/2026"
S_DOC = "Fiscal Focus 10/11/2026 + TuttoCalcolato (redditi 2025, patrimonio al 31/12/2025) · CGN/Fisco7 + InvestireOggi (immobili esteri: IVIE) · Fiscomania + Facile.it (conti esteri)"
S_PASSI = "Min. Lavoro (online INPS o CAF) · Money.it + Centro Fiscale agg. 15/11/2026 (precompilata, autorizzazione dei familiari, dati da inserire a mano)"
S_TEMPI = "Money.it + Centro Fiscale (10 giorni lavorativi) · InformazioneFiscale + Sky TG24 + LentePubblica (assegno unico: 28/2, arretrati entro 30/6)"
S_FINE = "Min. Lavoro · INPS · TuttoCalcolato · Centro Fiscale · Money.it"

BLOCKS = [
 dict(audio="A.wav", text=T["A"], chapter="01 · لمن هاد الدليل", src=S_INTRO, items=[
   dict(k="people", at=0.2, until="كلشي كيبدا", box=(160, 320, 1760, 860), people=["hijab", "man", "child"],
        say=[dict(who=0, text="عندي الأسينيو ديال الولاد", at=0.8), dict(who=1, text="وأنا باغي بونس الضو", at=3.4, bg="green")]),
   dict(k="head", text="الإيزي 2027", at="كلشي كيبدا", until="والإيزي ديال", sub="ISEE 2027 · دليل عملي خطوة بخطوة"),
   dict(k="calendar", at="والإيزي ديال", until="اليوم عندنا", box=(160, 260, 1760, 860), day=31, month=12, sub="الإيزي ديال 2026 كيموت · الجديد من 1 يناير"),
   dict(k="icons", at="غادي نشوفو", until="وناخدو مثال", box=(160, 300, 1760, 860), items=[
     ["file-text", "الوراق", "blue"], ["home", "اللي فالمغرب", "gold"], ["clipboard-check", "أونلاين ولا الكاف", "green"], ["alert-triangle", "الغلطات", "red"]], gap=2.2),
   dict(k="map", view="north", hl=["Emilia-Romagna"], pins=["Bologna"], labels=False, at="وناخدو مثال", until="ساكنين بالكرا", box=R_BOX),
   dict(k="people", at="وناخدو مثال", until="ساكنين بالكرا", box=L_BOX, people=["worker", "hijab"],
        say=[dict(who=0, text="أنا يوسف، فبولونيا", at=0.6, bg="green"), dict(who=1, text="وأنا فاطمة", at=2.6)]),
   dict(k="map", view="med", hl=["ITA", "MAR"], route=["Bologna", "Nador"], pins=["Nador"], labels=False, at="ساكنين بالكرا", until="معلومة مهمة", box=R_BOX),
   dict(k="icons", at="ساكنين بالكرا", until="معلومة مهمة", box=L_BOX, items=[
     ["key", "الكرا فإيطاليا", "blue"], ["home", "جزء دار فالناظور", "gold"], ["building-bank", "كونطو فالمغرب", "green"]], gap=1.8),
   dict(k="head", text="القواعد ديال دابا", at="معلومة مهمة", y=380, sub="Regole in vigore oggi · إلا تبدل شي حاجة غادي نقولوها"),
 ]),
 dict(audio="B.wav", text=T["B"], chapter="02 · الوراق: شنو خاصك توجد", src=S_DOC, items=[
   dict(k="chapter", num="02", title="الوراق", at=0.1, until="الإيزي هو رقم"),
   dict(k="steps", at="الإيزي هو رقم", until="وهاد التصريح", box=(160, 220, 1760, 840), steps=[
     ["شحال دخلتي", "1"], ["شنو عندك", "2"], ["شحال من واحد فالعائلة", "3"]], gap=1.6, check_after=0.6),
   dict(k="vs", at="وهاد التصريح", until="دابا الوراق", box=(260, 360, 1660, 880),
        right=dict(title="المداخيل", value="2025", sub="العام كامل", icon="report-money", color="gold"),
        left=dict(title="الكونطو", value="31/12/2025", sub="ماشي اليوم", icon="building-bank", color="green"), gap=3.0),
   dict(k="icons", at="دابا الوراق", until="ودابا الحاجة", box=(160, 300, 1760, 860), items=[
     ["id", "البطاقة والكود فيسكال", "blue"], ["receipt-tax", "CU / 730", "gold"], ["key", "الكونطرا ديال الكرا", "green"], ["car", "الكونطوات والتوموبيل", "red"]], gap=4.0),
   dict(k="map", view="med", hl=["MAR"], pins=["Nador", "Casablanca"], labels=False, at="ودابا الحاجة", until="يوسف خاصو", box=R_BOX),
   dict(k="people", at="ودابا الحاجة", until="يوسف خاصو", box=L_BOX, people=["man"],
        say=[dict(who=0, text="الدار فالمغرب؟ حتى هي كتدخل", at=1.2, bg="red")]),
   dict(k="people", at="يوسف خاصو", box=(160, 320, 1760, 860), people=["worker", "clerk"],
        say=[dict(who=0, text="شنو نجيب من المغرب؟", at=0.5), dict(who=1, text="عقد الدار وورقة البانكا", at=2.6, bg="green")]),
 ]),
 dict(audio="C.wav", text=T["C"], chapter="03 · الخطوات: أونلاين ولا الكاف", src=S_PASSI, items=[
   dict(k="chapter", num="03", title="الخطوات", at=0.1, until="عندك جوج طرق"),
   dict(k="vs", at="عندك جوج طرق", until="الخطوة اللولة", box=(260, 360, 1660, 880),
        right=dict(title="أونلاين", value="INPS", sub="البريكومبيلاطا بالسبيد", icon="phone", color="green"),
        left=dict(title="الكاف", value="CAF", sub="بالوراق كاملين", icon="users", color="gold"), gap=1.5),
   dict(k="steps", at="الخطوة اللولة", until="فاطمة خاصها", box=(160, 200, 1760, 860), steps=[
     ["دخل بالسبيد ولا الكارطا", "1"], ["موافقة كل واحد كبير", "2"], ["شوف المعلومات وصحح", "3"], ["زيد التوموبيل واللي فالمغرب", "4"], ["صيفط وحمل الإيزي", "5"]], gap=1.2, check_after=0.6),
   dict(k="people", at="فاطمة خاصها", until="الخطوة التالتة", box=(160, 320, 1760, 860), people=["hijab", "worker"],
        say=[dict(who=1, text="دخلي بالسبيد ديالك", at=0.6), dict(who=0, text="واخا، وافقت", at=2.8, bg="green")]),
   dict(k="people", at="مغمض العينين", until="الخطوة الرابعة", box=(160, 320, 1760, 860), people=["man"],
        say=[dict(who=0, text="شوف مزيان قبل ما تقبل", at=0.4, bg="red")]),
   dict(k="icons", at="الخطوة الرابعة", until="الخطوة الخامسة", box=(160, 300, 1760, 860), items=[
     ["car", "التوموبيل", "blue"], ["home", "الدار فالمغرب", "gold"], ["building-bank", "الكونطو فالمغرب", "green"]], gap=1.4),
   dict(k="map", view="north", hl=["Emilia-Romagna"], pins=["Bologna"], labels=False, at="الطريق التانية", until="وفالكاف ولا", box=R_BOX),
   dict(k="people", at="الطريق التانية", until="وفالكاف ولا", box=L_BOX, people=["clerk", "worker"],
        say=[dict(who=1, text="بشحال؟", at=4.5), dict(who=0, text="سول قبل", at=6.0, bg="green")]),
   dict(k="warn", text="المعلومات اللي كتعطي: تحت المسؤولية ديالك", at="وفالكاف ولا", y=440),
 ]),
 dict(audio="D.wav", text=T["D"], chapter="04 · المدة والأسينيو أونيكو", src=S_TEMPI, items=[
   dict(k="chapter", num="04", title="المدة", at=0.1, until="أونلاين بالبريكومبيلاطا"),
   dict(k="rows", at="أونلاين بالبريكومبيلاطا", until="مثال يوسف", y=380, gap=150, size=56, rows=[
     ("أونلاين بالبريكومبيلاطا: أسرع", "INPS", "أونلاين بالبريكومبيلاطا", GREEN),
     ("الطريق العادية: أيام ديال الخدمة", "10", "والطريق العادية", GOLD),
   ]),
   dict(k="map", view="north", hl=["Emilia-Romagna"], pins=["Bologna"], labels=False, at="مثال يوسف", until="وعلاش هاد", box=R_BOX),
   dict(k="vs", at="مثال يوسف", until="وعلاش هاد", box=(160, 300, 960, 860),
        right=dict(title="التصريح", value="8/1", sub="2027", icon="calendar", color="gold"),
        left=dict(title="الإيزي", value="22/1", sub="تقريبا", icon="file-certificate", color="green"), gap=3.5),
   dict(k="calendar", at="وعلاش هاد", until="وإلا درتيه", box=(160, 260, 1760, 860), day=28, month=2, sub="آخر فبراير: المبلغ الكامل من مارس"),
   dict(k="calendar", at="وإلا درتيه", until="يعني يوسف", box=(160, 260, 1760, 860), day=30, month=6, sub="قبل آخر يونيو: كيرجعو الفرق من مارس"),
   dict(k="people", at="يعني يوسف", until="ملي كيخرج", box=(160, 320, 1760, 860), people=["worker", "hijab"],
        say=[dict(who=1, text="ما نتسناوش حتى مارس", at=0.6, bg="green")]),
   dict(k="people", at="ملي كيخرج", until="والإيزي الجديد", box=(160, 320, 1760, 860), people=["man", "office"],
        say=[dict(who=1, text="كاينة شي ملاحظة؟", at=1.5), dict(who=0, text="نصحح بتصريح جديد", at=4.5, bg="green")]),
   dict(k="calendar", at="والإيزي الجديد", box=(160, 260, 1760, 860), day=31, month=12, sub="الإيزي الجديد صالح حتى آخر 2027"),
 ]),
 dict(audio="E.wav", text=T["E"], chapter="05 · الغلطات والملخص", src=S_FINE, items=[
   dict(k="chapter", num="05", title="الغلطات اللي تبعد عليها", at=0.1, until="الغلطة اللولة"),
   dict(k="warn", text="تستنى حتى مارس: تخسر المبلغ الكامل", at="الغلطة اللولة", until="الغلطة التالتة", y=300),
   dict(k="warn", text="الكونطو: شحال كان فآخر ديال العام، ماشي اليوم", at="الغلطة التانية", until="الغلطة التالتة", y=440),
   dict(k="map", view="med", hl=["MAR"], pins=["Nador"], labels=False, at="الغلطة التالتة", until="الغلطة الرابعة", box=R_BOX),
   dict(k="people", at="الغلطة التالتة", until="الغلطة الرابعة", box=L_BOX, people=["man"],
        say=[dict(who=0, text="نسيتي الدار ديال المغرب؟", at=0.5, bg="red")]),
   dict(k="people", at="الغلطة الرابعة", until="نعاودو باختصار", box=(160, 320, 1760, 860), people=["hijab", "worker"],
        say=[dict(who=0, text="قبلتي بلا ما تشوف؟", at=0.6, bg="red"), dict(who=1, text="وأنا ما وافقتش...", at=4.5)]),
   dict(k="head", text="باختصار", at="نعاودو باختصار", until="هادشي معلومات"),
   dict(k="rows", at="نعاودو باختصار", until="هادشي معلومات", y=350, gap=90, size=44, rows=[
     ("الإيزي القديم كيموت", "31/12", "الإيزي كيموت", WHITE),
     ("المداخيل", "2025", "المداخيل ديال", GOLD),
     ("الكونطو كيف كان", "31/12/2025", "الكونطو كيف", WHITE),
     ("الدار والكونطو فالمغرب: كتصرح بيهم", "Marocco", "واللي عندك فالمغرب", GOLD),
     ("للأسينيو كامل: قبل", "28/2", "وقبل آخر فبراير", GREEN),
   ]),
   dict(k="people", at="هادشي معلومات", until="وإلا عجبك", box=(160, 300, 1760, 860), people=["woman", "worker"],
        say=[dict(who=0, text="أونلاين ولا فالكاف؟", at=3.5, bg="green"), dict(who=1, text="أنا فالكاف!", at=6.0)]),
   dict(k="cta", at="وإلا عجبك", text="ابوني فالقناة", sub="كل نهار دليل جديد للمغاربة فإيطاليا"),
 ]),
]

THUMB = dict(
  title=[("الإيزي 2027", (236, 196, 96)), "خطوة بخطوة", "الوراق والدار اللي فالمغرب"],
  num="31/12", numsub="ISEE 2027 · DSU",
  bottom="مغاربة إيطاليا · دليل عملي بالدارجة",
)
