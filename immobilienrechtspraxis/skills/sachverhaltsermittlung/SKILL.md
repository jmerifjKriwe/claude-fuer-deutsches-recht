---
name: sachverhaltsermittlung
description: Unterstuetzt Inhouse-Juristen bei der zeitraubendsten Phase eines Vorgangs — der Sachverhaltsermittlung. Statt sofort den vollen Sachverhalt zu fordern, fuehrt der Skill einen strukturierten Frageprozess in mehreren Stufen. Stufe eins extrahiert Eckpunkte aus vorhandenen Unterlagen. Stufe zwei stellt gezielte Rueckfragen an Asset-Management oder Hausverwaltung. Stufe drei rekonstruiert eine zeitliche Abfolge. Stufe vier markiert Beweisluecken. Ausgabe ist ein konsolidiertes Sachverhalts-Memo mit klarer Trennung gesichert plausibel offen. Geeignet fuer Mietstreitigkeiten Mietmaengelanzeigen Kuendigungen Bauschadensfaelle und Property-Management-Konflikte.
---

# Sachverhaltsermittlung

## Leitidee

Der Engpass in Inhouse-Arbeit ist selten die rechtliche Bewertung. Es
ist die saubere Erfassung des Sachverhalts. Asset-Management und
Hausverwaltung liefern selten freiwillig den vollen Sachverhalt. Der
Skill fragt strukturiert ab und liefert dem Juristen ein konsolidiertes
Memo, das wirklich verwertbar ist.

## Inputs

- Eingangskorrespondenz (Mieterschreiben Anwaltsschreiben Email)
- Vorhandene Unterlagen (Vertrag Uebergabeprotokoll Mahnungen
  Hausverwaltungsberichte)
- Optional: interne Kommentare aus der Akte

## Methodik in vier Stufen

### Stufe 1 — Extraktion aus Unterlagen

Aus jedem vorhandenen Dokument werden Datum Akteure Ereignisse und
behauptete Maengel extrahiert. Ergebnis ist eine erste rohe
Zeitleiste.

### Stufe 2 — Gezielter Fragenkatalog

Der Skill erzeugt einen Fragenkatalog fuer Asset-Management bzw.
Hausverwaltung. Fragen sind kurz, geschlossen wo moeglich, jeweils
mit Begruendung warum die Frage relevant ist (zB "Wann erfolgte
Mangelanzeige formell? Relevant fuer Beginn Minderungsrecht
§ 536 BGB").

### Stufe 3 — Zeitleisten-Rekonstruktion

Antworten werden in die Zeitleiste integriert. Konflikte zwischen
Aussagen werden markiert.

### Stufe 4 — Beweis und Luecken

Pro Tatsachenbehauptung wird vermerkt: durch welches Beweismittel
gesichert (Urkunde Zeuge Augenschein), bloss plausibel oder offen.

## Output

- `SV_Memo_<Aktenzeichen>.md` mit Abschnitten:
  - Gesicherter Sachverhalt
  - Plausible Annahmen mit Quelle
  - Offene Punkte mit Fragestellung
  - Zeitleiste in Tabellenform
  - Beweisuebersicht
- `Fragenkatalog_<Adressat>.docx` — versendungsfertig an
  Asset-Management oder Hausverwaltung

## Anti-Halluzinations-Regel

Der Skill erfindet KEINE Sachverhaltsdetails. Wo eine Information
fehlt, steht "OFFEN" mit konkreter Frage. Inhouse-Juristen verlieren
sonst das Vertrauen — und das ist der teuerste Verlust.

## Typische Fallkonstellationen

- Mietmaengel — wann angezeigt, wann besichtigt, welcher Mietzins,
  welche Minderungsquote behauptet
- Kuendigung — Form, Zugang, Begruendung, Widerspruch nach
  § 574 BGB
- Eigenbedarf — Bedarfsperson Verwandtschaftsgrad konkrete
  Nutzungsabsicht
- Betriebskostenabrechnung — Abrechnungszeitraum Zugang § 556
  Abs. 3 BGB Frist Einwendungen
- Schoenheitsreparaturen Endrenovierung — Vertragsklausel
  Zeitpunkt der Vertragsbegruendung Renovierungszustand bei
  Einzug
- Bauschaeden — Erstanzeige Sachverstaendiger Beweissicherung

## Beispielformulierungen

- "Mieterschreiben mit Mietmaengelanzeige liegt vor. Erstelle
  Sachverhalts-Memo und Fragenkatalog an Hausverwaltung."
- "Kuendigungsstreit gegen Mieter Schmitt. Antworten der
  Hausverwaltung anbei. Konsolidiere zum Memo."
- "Ich habe nur eine halbe Akte. Welche Fragen muss ich stellen,
  bevor ich rechtlich pruefe?"
