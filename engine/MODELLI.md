# Modelli grafici (engine/visuals.py)

Usabili nei REEL (campo `"v"` di una scena, al posto di `"big"`) e nei VIDEO LUNGHI (item con `k` = tipo).
Esempio completo: `reels/demo-modelli.json`.

| tipo | a cosa serve | campi |
|---|---|---|
| `map` | dove succede: regioni, città, rotte Italia-Marocco | `view`: italy · north · south · med; `hl`: regioni (es. "Calabria") o paesi in vista med ("ITA", "MAR"); `pins`: città (o `{"city","label","color"}`); `route`: ["Genova","Tanger","ship"] o ["Milano","Casablanca"] (aereo); `labels`: false per non scrivere i nomi delle regioni |
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
Dati mappa: openpolis/geojson-italy (CC BY 4.0, dati ISTAT), Natural Earth (pubblico dominio). La vista med è tagliata
sopra il 29° parallelo.
