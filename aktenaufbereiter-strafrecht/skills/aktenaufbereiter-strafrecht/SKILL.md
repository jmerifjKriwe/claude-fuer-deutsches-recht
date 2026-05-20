---
name: aktenaufbereiter-strafrecht
description: Strukturierte Aufbereitung strafrechtlicher Akten fuer die Verteidigung. Erzeugt sechs Uebersichten — Aktenvorblatt mit Blattangaben; Personenverzeichnis mit Rolle und Erstnennung; Tatkomplex- und Vorwurfsverzeichnis mit einschlaegigen Normen; Beziehungsverzeichnis der Beteiligten; Chronologie aller relevanten Ereignisse; Fristen- und Terminverzeichnis. Alle Tabellen Excel-faehig mit Band- und Blattangabe als Fundstelle. Fortlaufend ergaenzbar bei Aktennachlieferungen mit Markierung der Neuzugaenge. Erkennt Widersprueche zwischen Vernehmungen und Kontounterlagen. Nimmt KEINE rechtliche Bewertung vor. OCR auf Scans ist Pflicht. Geeignet fuer Wirtschaftsstrafverfahren BtM-Verfahren Vermoegensdelikte und komplexe Strafverfahren.
---

# Aktenaufbereiter Strafrecht

## Leitidee

Quod non est in actis non est in mundo. Wer die Akte nicht
beherrscht beherrscht den Fall nicht. Strafakten umfassen hunderte
bis zehntausende Seiten. Der Skill uebernimmt die mechanische
Erfassungs- und Strukturierungsarbeit — die manchmal wissenschaftliche
Mitarbeiter oder Referendare leisten — und liefert Tabellen die in
Excel weiterverwendbar sind.

Der Skill ersetzt NICHT die eigene Aktenlektuere. Er ist kein
agentisches System das selbstaendig verteidigt. Er ist ein Werkzeug
das die mechanische Vorarbeit beschleunigt und dabei Widersprueche
und Luecken sichtbar macht die beim Durchblaettern leicht uebersehen
werden.

## Inputs

- Digitalisierte Aktenbestandteile (PDF mit OCR Word maschinenlesbar)
- Optional: vorhandene Excel-Tabelle zur Fortschreibung
- Optional: Anklageschrift gesondert (fuer Abgleich)
- Optional: Vorlage-Excel mit Wunsch-Spalten

## OCR-Pflicht

Gescannte Dokumente OHNE Texterkennung werden nicht verlaesslich
verarbeitet. Der Skill weist darauf hin. Manche Systeme lesen
auch ohne OCR aus Bildern — Ergebnisse sind aber deutlich
fehleranfaelliger und nicht empfehlenswert.

## Sechs Uebersichten

### 1. Aktenvorblatt und Inhaltsverzeichnis

Spalten: Nr — Blatt — Datum — Vorgang — Essentialia — Anmerkung
Kanzlei — Anmerkung Mandant.

Blattangaben muessen mit der tatsaechlichen Paginierung
uebereinstimmen. Bei fehlender Paginierung wird so gut wie moeglich
gearbeitet und die Luecke markiert. Unvollstaendige Paginierung ist
besser als gar keine.

### 2. Personenverzeichnis

Spalten: Nr — Name (Nachname Vorname) — Adresse — Prozessrolle —
Blatt der Erstnennung — Anmerkung Kanzlei — Anmerkung Mandant.

Prozessrollen: Beschuldigter Zeuge Geschaedigter Sachverstaendiger
Polizeibeamter Richter Staatsanwalt Verteidiger Nebenklaeger
sonstiger Beteiligter.

Hintergrund: Auf Blatt 700 taucht eine Person auf und man weiss
dass sie schon einmal vorgekommen sein muss aber findet sie nicht
wieder. Genau wie in dicken alten Romanen — deshalb haben die
Personenverzeichnisse. Und deshalb braucht man sie auch fuer
Strafakten.

### 3. Tatkomplex- und Vorwurfsverzeichnis

Spalten: Tatkomplex (I II III ...) — Tatvorwurf und Norm —
Tatzeitraum von bis — Betroffene Personen (Beschuldigte
Geschaedigte) — Beweismittel (Urkunden Zeugen
Sachverstaendigengutachten).

Zusatz: Thematischer Index — auf welchem Blatt welches Thema
behandelt wird. Beispiel: Komplex Kontofaelschung Bl. 125-189
Band I und Bl. 45-72 Band III. Zeugenaussagen zum Untreue-Vorwurf
Bl. 312 Bl. 455 Bl. 678-690.

### 4. Beziehungsverzeichnis

Spalten: Person 1 — Beziehung — Person 2 — Fundstelle (Band
Blatt) — Bemerkungen.

Beziehungstypen: Verwandtschaft Geschaeftspartner Kontakt per Chat
Telefonat E-Mail Mitarbeiter Vorgesetzter. Auf Wunsch
Netzwerkdiagramm als Graph — sonst bleibt es bei der Tabelle.

### 5. Chronologie

Spalten: Nr — Datum — Blatt — Beteiligte — Vorgang — Anmerkung
Kanzlei — Anmerkung Mandant.

Lueckenlos chronologisch geordnet. Zentrales Arbeitsinstrument
fuer Hauptverhandlung Mandantengespraech und Verstaendigung mit
der Staatsanwaltschaft.

### 6. Fristen- und Terminverzeichnis

Spalten: Art (HV-Termin Frist Adresse) — Datum oder Frist —
Beschreibung — Fundstelle (Band Blatt).

Erfasst auch Adressen aller Verfahrensbeteiligten — Gericht
Staatsanwaltschaft Mitverteidiger Nebenklagevertretung.

## Methodik

1. Aktenbestandteile inventarisieren — pro Datei Typ Umfang
   OCR-Status
2. Blatt-fuer-Blatt-Extraktion mit Quellenverweis
3. Querverweis zwischen den sechs Tabellen — Personen aus
   Personenverzeichnis muessen in Beziehung und Chronologie
   konsistent erscheinen
4. Widerspruchspruefung — abweichende Datums- oder Sachangaben
   in verschiedenen Vernehmungen werden BEIDE dokumentiert mit
   Fundstelle
5. Lueckenpruefung — in der Anklageschrift genannte Zeugen die in
   den Vernehmungsprotokollen fehlen werden markiert
6. Ausgabe als Excel-faehige Tabellen

## Anti-Halluzinations-Regel

- Nur Informationen die in der Akte stehen
- Keine eigenen Vermutungen oder Wertungen
- Jede Information mit Band und Blattangabe wenn identifizierbar
- Widersprueche BEIDE dokumentieren mit Fundstelle
- Unsicherheiten kennzeichnen — Beispiel `[Datum unklar]`
  `[Name nur teilweise lesbar]`
- KEINE rechtliche Bewertung der Vorwuerfe
- KEINE Einschaetzung der Erfolgsaussichten der Verteidigung

## Output-Dateien

- `Aktenvorblatt_<Aktenzeichen>.xlsx`
- `Personenverzeichnis_<Aktenzeichen>.xlsx`
- `Tatkomplexe_<Aktenzeichen>.xlsx`
- `Beziehungen_<Aktenzeichen>.xlsx`
- `Chronologie_<Aktenzeichen>.xlsx`
- `Fristen_<Aktenzeichen>.xlsx`

Alternativ ein Sammel-Workbook `Akte_<Aktenzeichen>.xlsx` mit
sechs Tabellenblaettern.

Auf Wunsch zusaetzlich Markdown-Version der Tabellen fuer offline
Nutzung bei Gerichtsterminen ohne stabilen Internet-Zugang.

## Fortlaufende Aktualisierung

Bei Nachlieferungen ergaenzt der Skill die bestehende Tabelle.
Neuzugaenge werden in einer Spalte `Status` mit `NEU` markiert
oder in einer separaten Spalte `Eingang` mit Datum versehen.
Bisherige Eintraege werden nicht ueberschrieben.

Beispielworkflow: "Hier ist meine bisherige Chronologie hier sind
weitere 300 Blaetter Akten — bitte aufnehmen." Der Skill ergaenzt
und markiert.

## Spezialisierungen

### Wirtschaftsstrafverfahren

Zusatztabellen: Finanzstroeme Kontoverbindungen
Transaktionschronologien Gesellschaftsverflechtungen.

### BtM-Verfahren

Zusatztabellen: TKUe-Protokolle Observationsberichte Chatverlaeufe
mit Datum Teilnehmern Inhalt-Zusammenfassung.

### Beweismittelverzeichnis

Separate Tabelle: Beweismittel — Art — Fundstelle in Akte —
Erhebungsgrundlage — Bewertung der Verwertbarkeit. Bewertung
strikt sachlich keine prozesstaktische Empfehlung.

### Anklageschrift-Abgleich

Gegenueberstellung: in der Anklageschrift behauptete Tatsache —
Aktenbefund — Diskrepanz. Markiert wo die Anklage nicht durch die
Akte gedeckt ist.

### Vernehmungsuebersicht

Tabelle aller Vernehmungen: Datum — vernehmender Beamter —
vernommene Person — wesentliche Aussageinhalte — Widersprueche
zu frueheren Aussagen — Fundstelle.

## Beispielformulierungen

- "Erstelle alle sechs Uebersichten zu dieser Strafakte. OCR
  ist gemacht."
- "Hier ist meine bisherige Chronologie und 400 neue Blaetter.
  Bitte aufnehmen mit Markierung der Neuzugaenge."
- "Erzeuge zusaetzlich das Wirtschaftsstraf-Set mit
  Finanzstroemen und Kontoverbindungen."
- "Gleiche die Anklageschrift mit dem Aktenbefund ab und zeige
  Diskrepanzen."
- "Vernehmungsuebersicht mit Widerspruechen zwischen den
  einzelnen Aussagen des Zeugen Mueller."

## Berufsrecht und Datenschutz

Strafakten enthalten hochsensible personenbezogene Daten. Nutzung
nur mit KI-Systemen die DSGVO § 203 StGB und §§ 43a 43e BRAO
vertraglich zusichern und tatsaechlich gewaehrleisten. Verlage
und Gerichtsentscheidungen — § 5 UrhG — geniessen keinen
urheberrechtlichen Schutz; rechtswissenschaftliche Literatur der
Verlage hingegen schon — Lizenzsituation pruefen.

## Pragmatismus

Der Skill ist ein Quick Win. Er ersetzt nicht die Welt — er
beschleunigt das bisherige Verfahren. Wer Chronologien in Excel
fuehrt fuehrt sie weiter — nur eben schneller und vollstaendiger.
Wer im Mandantengespraech praezise auf Blatt 312 zugreifen koennen
muss findet die Stelle in Sekunden statt in Minuten.
