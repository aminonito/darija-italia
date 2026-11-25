# Modelli grafici (engine/visuals.py)

Usabili nei REEL (campo `"v"` di una scena, al posto di `"big"`) e nei VIDEO LUNGHI (item con `k` = tipo).
Esempio completo: `reels/demo-modelli.json`.

| tipo | a cosa serve | campi |
|---|---|---|
| `map` | dove succede: regioni, città, rotte Italia-Marocco | `view`: italy · north · south · med (Italia + Marocco) · maroc (solo Marocco); `hl`: regioni (es. "Calabria") o paesi in vista med ("ITA", "MAR"); `pins`: città (o `{"city","label","color"}`); `route`: ["Genova","Tanger","ship"] o ["Milano","Casablanca"] (aereo); `labels`: false per non scrivere i nomi delle regioni |
| `people` | chi è coinvolto, dialoghi | `people`: 1-3 ruoli (max 4); `say`: [{"who":0,"text":"...","at":0.6,"bg":"green"}] |
| `icons` | elenchi di cose (documenti, bollette, servizi) | `items`: [[icona, etichetta, colore?]] 2-4; `gap` s tra un'icona e l'altra |
| `bars` | confronto di numeri | `bars`: [[etichetta, valore numerico, testo, colore?]] 2-4 |
| `calendar` | scadenze e date | `day`, `month` (1-12 o testo), `sub` |
| `vs` | prima/dopo, due casi | `right` e `left` = {"title","value","sub","icon" o "person","color"}; `gap` = secondi prima del secondo |
| `steps` | procedura passo passo | `steps`: [[testo, valore]]; `gap`, `check_after` |

Comuni: `t` (ritardo iniziale), `box` (x1,y1,x2,y2; default reel 60,480,1020,1250 · lungo 160,170,1760,850).
Nei lunghi due modelli affiancati: box destro (1000,170,1760,850) e sinistro (160,250,950,780).

Ruoli personaggi: worker man woman hijab elder office doctor student child girl clerk farmer.

Città: Roma Milano Torino Napoli Bologna Firenze Genova Venezia Bari Palermo Catania Verona Brescia Bergamo Padova
"Reggio Calabria" Cagliari Trieste Ancona Perugia Salerno Livorno Civitavecchia Modena Parma "Reggio Emilia" Vicenza
Treviso · Tanger Tetouan Nador Casablanca Rabat Fes Marrakech Agadir Oujda Meknes "Beni Mellal" Khouribga "El Jadida" Kenitra.

Icone (assets/icons, Tabler MIT): alert-triangle baby-carriage bolt briefcase building-bank building-factory
building-hospital building-store bus calculator calendar camera car cash certificate chart-bar check clipboard-check
clock coin-euro credit-card currency-euro droplet e-passport file-certificate file-text fingerprint flame gas-station
heart home home-dollar id key license luggage mail mailbox map-pin percentage phone pig-money pill plane receipt
receipt-tax report-money scale school ship shopping-cart stethoscope ticket tool tractor train trash trending-down
trending-up truck user users wallet world x. Altre: copiarle da @tabler/icons (npm) in assets/icons.

Regole testo: valori con %, +, ≈, € in stringhe brevi; nei fumetti evitare numeri con segni attaccati a parole arabe.
Dati mappa: openpolis/geojson-italy (CC BY 4.0, dati ISTAT), Natural Earth (pubblico dominio). Il Marocco è SEMPRE
disegnato intero, Sahara compreso fino a Guerguerat, come un solo paese senza linee interne (decisione di Amine del
19/11/2026): MAR e SAH di Natural Earth vengono fusi, le viste med e maroc arrivano al 20,3° parallelo e check_morocco()
blocca il render se qualcosa cambia. Città del sud disponibili: Laayoune, Smara, Dakhla, Guerguerat, Tiznit, Guelmim.
Nella vista med al massimo UNA città del sud (sono vicine e le etichette si sovrappongono): per più città usa view maroc.

## Versione italiana (ITALIA TIMES, video lunghi 16:9)
`visuals.configure(lang="it", fonts=..., accent=...)` cambia direzione (sinistra→destra), nomi di città/regioni e mesi in italiano.
Nel motore ITALIA TIMES si usa tramite `engine/bridge_italia_times.py`: in scenes.py dopo `from wide import *`
`import sys; sys.path.insert(0, "/home/claude/darija-italia/engine"); import bridge_italia_times` e poi
`sc.vis(tipo, t0, t1=None, box=(x1,y1,x2,y2), **campi)` (box default 160,170,1760,880; area utile y 150-880).
Le etichette delle regioni scendono da sole se c'è una città vicina; con molte città usa `labels=False`.

## Stile del giorno (engine/theme.py) — decisione di Amine del 24/11/2026
render_reel.py e render16.py scelgono da soli lo stile dalla data nel nome del file:
lunedì-martedì **casablanca** (nero, rosso/verde, archi) · mercoledì-giovedì **chefchaouen** (blu notte, azzurro, rombi,
sottotitoli su pillola scura) · venerdì-sabato **sahara** (terra scura, arancio, onde, parola attiva sottolineata) ·
domenica **zitoun** (verde oliva, oro, puntini). Cambiano sfondo, motivo, aloni, pill del gancio, evidenziazione della
parola, barra di avanzamento e colori di numeri/barre; logo e modelli grafici restano uguali. THEME=<nome> solo per prove.

## doc — il documento vero (25/11/2026)
Foglio chiaro stilizzato di un documento italiano con le voci scritte come sul foglio vero (caratteri latini):
`{"type":"doc","title":"BUSTA PAGA","rows":["LIVELLO","FERIE / PERMESSI","TFR","NETTO"],"focus":2,"tag":"01 · TFR","done":[0,1],"warn":[],"at":0.5}`
- focus = voce evidenziata (barra colorata), tag = etichetta rossa sotto il foglio, done = spunte verdi, warn = x rosse.
- Usalo in 3-4 scene di FILA con lo stesso title/rows e focus diverso (conto alla rovescia 03 → 02 → 01): il foglio
  resta e lo spettatore impara a leggere il SUO documento. Esempi: BUSTA PAGA, CU, BOLLETTA LUCE, PERMESSO DI SOGGIORNO,
  RICEVUTA POSTE, CONTRATTO D'AFFITTO, CEDOLINO PENSIONE, ATTESTAZIONE ISEE, F24.
