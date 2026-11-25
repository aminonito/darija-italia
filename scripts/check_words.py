"""Controllo parole sbagliate (correzioni di Amine) nei copioni, sottotitoli, grafiche, titoli e caption.

Uso: python3 scripts/check_words.py <file> [<file> ...]   (json dei job TTS o dei reel, file episodes/*.py, testi)
Esce con codice 1 se trova una forma sbagliata. Aggiungi qui ogni nuova correzione di Amine.
"""
import re, sys

AR = "ء-ي"
# (regex della forma sbagliata, forma giusta, nota)
WRONG = [
    (rf"كومون(?![{AR}])", "الكوموني", "Comune: si dice الكوموني, mai الكومون (Amine 25/11/2026); الكومونتير = commento va bene"),
]


def main():
    bad = 0
    for p in sys.argv[1:]:
        txt = open(p, encoding="utf-8").read()
        for n, line in enumerate(txt.splitlines(), 1):
            for rx, good, note in WRONG:
                for m in re.finditer(rx, line):
                    bad += 1
                    a = max(0, m.start() - 25)
                    print(f"{p}:{n}: «{line[a:m.end() + 10].strip()}» → usa {good} ({note})")
    print("parole ok" if not bad else f"{bad} parole da correggere")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
