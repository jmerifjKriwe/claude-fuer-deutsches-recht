---
name: vertragserstellung-musterbasiert
description: "Nutze dies, wenn Vertragserstellung Musterbasiert, Vertragspruefung Playbook, Immo Share Deal Grunderwerbsteuer im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Bitte Vertragserstellung Musterbasiert, Vertragspruefung Playbook, Immo Share Deal Grunderwerbsteuer prüfen.; Erstelle eine Arbeitsfassung zu Vertragserstellung Musterbasiert, Vertragspruefung Playbook, Immo Share Deal Grunderwerbsteuer.; Welche Normen und Nachweise brauche ich?."
---

# Vertragserstellung Musterbasiert, Vertragspruefung Playbook, Immo Share Deal Grunderwerbsteuer

## Zweck

Dieser Skill ist ein eigenständiger Arbeitsbereich. Er verbindet mehrere sachlich benachbarte Arbeitsmodule. Wähle anhand des Sachverhalts das passende Modul, arbeite dessen Prüfroutine vollständig ab und kombiniere Module nur, wenn der Fall tatsächlich mehrere Themen berührt.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `vertragserstellung-musterbasiert` | Immobilienrechtliche Vertraege auf Musterbasis erstellen: Kaufvertrag, Mietvertrag, WEG-Beschluss. Normen: §§ 433 ff. 535 ff. 873 BGB, WEG, GrEStG. Prüfraster: Musterauswahl, Anpassung an Sachverhalt, Notarerfordernis. Output: Vertragsentwurf auf Musterbasis. Abgrenzung: nicht individuelle Vertragsprüfung. |
| `vertragspruefung-playbook` | Immobilienrechtliche Vertraege nach standardisiertem Playbook prüfen: Kaufvertrag, Grundschuld, WEG. Normen: §§ 433 ff. 873 ff. BGB, WEG, GrEStG, GBO. Prüfraster: Playbook-Checkliste, Risikoklauseln, Notar- und Formerfordernisse. Output: Vertragsprüfergebnis mit Markierungen. Abgrenzung: nicht Vertragserstellung. |
| `immo-share-deal-grunderwerbsteuer` | Immobilien Share Deal Grunderwerbsteuer §§ 1 Abs. 2a, Abs. 2b, Abs. 3 GrEStG: Schwellen 90 Prozent, 5/10 Jahre Halte. Vergleich Asset Deal vs. Share Deal. Auswirkungen MoPeG. |

## Arbeitsweg

Für **Vertragserstellung Musterbasiert, Vertragspruefung Playbook, Immo Share Deal Grunderwerbsteuer** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `immobilienrechtspraxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `vertragserstellung-musterbasiert`

**Fokus:** Immobilienrechtliche Vertraege auf Musterbasis erstellen: Kaufvertrag, Mietvertrag, WEG-Beschluss. Normen: §§ 433 ff. 535 ff. 873 BGB, WEG, GrEStG. Prüfraster: Musterauswahl, Anpassung an Sachverhalt, Notarerfordernis. Output: Vertragsentwurf auf Musterbasis. Abgrenzung: nicht individuelle Vertragsprüfung.

# Vertragserstellung musterbasiert

## Fachkern: Vertragserstellung musterbasiert
- **Spezialgegenstand:** Vertragserstellung musterbasiert wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB, GBO, WEG, BauGB, ErbbauRG, MaBV, Mietrecht, Grundpfandrechte, Notar-/Registervollzug und öffentlich-rechtliche Lasten.
- **Entscheidende Weiche:** Trenne Eigentum, Besitz, Grundbuchabteilung, Belastung, Fälligkeit, Vollzug, Mängel, Miet-/Nutzungsverhältnis und Finanzierung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Leitidee

Vertragserstellung ist NICHT voll an die KI delegierbar. Die KI ist ein
disziplinierter Schreibtisch, der vorgegebene Klauseln einsetzt, Platzhalter
befüllt und Querverweise konsistent haelt. Sie ist KEIN Drafter und schreibt
keine eigenen Klauseln in tragenden Punkten.

## Inputs

- Mustervertrag (.docx) der Kanzlei oder Rechtsabteilung
- Term Sheet oder Eckpunktepapier (.docx, .md, .pdf, freier Text)
- Optional: vorhandene Vorgängerverträge zur Stilreferenz
- Optional: Anlagenliste (Lageplan, Baubeschreibung, Hausordnung,
  Betriebskostenaufstellung)

## Klauselschutz — die zentrale Regel

Jede Klausel im Muster, die NICHT als Platzhalter markiert ist, ist tabu.
Markierungen die der Skill respektiert:

- `[[...]]` doppelte eckige Klammern für freie Eingaben
- `{{...}}` doppelte geschweifte Klammern für typisierte Variablen
- `__________` Unterstrich-Strecken für Daten und Betraege
- Gelb hinterlegte Felder im Word-Dokument
- Kommentare am Rand mit Praefix `KI:`

Findet die KI an einer NICHT-markierten Stelle einen logischen Widerspruch
zum Term Sheet (zB Term Sheet sagt befristet, Muster ist unbefristet),
DARF sie die Klausel nicht selbst ändern. Sie protokolliert den Konflikt
und gibt das Dokument unverändert zurück mit Hinweis.

## Methodik

1. Mustervertrag laden und alle Platzhalter inventarisieren
2. Term Sheet parsen — Parteien, Objekt, wirtschaftliche Eckpunkte,
   Sondervereinbarungen
3. Mapping Term-Sheet-Position auf Musterplatzhalter erstellen
4. Platzhalter befuellen, Querverweise (§-Verweise, Anlagen) anpassen
5. Konsistenzprüfung: Daten, Betraege ohne Komma in der Beschreibung,
   Parteiennennungen, Pluralformen
6. Änderungsprotokoll erzeugen — welche Platzhalter befüllt, welche offen,
   welche Konflikte
7. Roter Block oben im Dokument: was zwingend manuell zu prüfen ist

## Output

- `Vertrag_<Objekt>_<Datum>.docx` auf Muster-Layout, Platzhalter befüllt
- `Aenderungsprotokoll.md` mit Tabelle Platzhalter — Wert — Quelle im Term Sheet
- `Manuelle_Pruefung.md` mit Liste der Punkte die nur ein Jurist
  entscheiden kann (zB GenehmigungspflichtigerVerkauf §§ 1365 BGB,
  Vorkaufsrechte §§ 24 ff. BauGB, Denkmalschutz, Erbbauzins-Anpassung)

## Typische manuelle Pruefpunkte bei Immobilienverträgen

- Vorkaufsrechte der Gemeinde §§ 24 ff. BauGB
- Genehmigung nach § 1365 BGB bei Verfügung über das Vermögen im Ganzen
- Grundstücksverkehrsgenehmigung GrdstVG
- Sanierungsvermerk § 144 BauGB, Erhaltungssatzung § 172 BauGB
- Wohnungseigentumsumwandlung § 250 BauGB (Genehmigungspflicht)
- WEG-Beschlüsse als Anlage (Beschlussfähigkeit, Anfechtungsfristen)
- Erbbauzins-Anpassungsklauseln und Heimfallrecht
- Mietpreisbremse §§ 556d ff. BGB, qualifizierter Mietspiegel
- Schriftform Gewerbemietvertrag § 550 BGB (Heilung schwierig)
- Betriebskostenkatalog Verordnung 2003, Umlagevereinbarung
- Indexmiete §§ 557b BGB versus Staffelmiete § 557a BGB

## Beispielformulierungen

- "Erstelle aus Mustervertrag Gewerbemiete und beigefügtem Term Sheet
  einen Entwurf. Achte auf Schriftform § 550 BGB."
- "Befuelle den Wohnraummietvertrag-Muster mit den Eckpunkten aus dem
  Eckpunktepapier. Prüfe ob Mietpreisbremse greift und markiere."
- "Erstelle WEG-Verwaltervertrag aus Muster, Term Sheet anbei,
  Bestellungsbeschluss als Anlage einfügen."

## Aktuelle Rechtsprechung — Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette

- Schriftform: § 550 BGB, § 311b BGB
- Mietpreisbremse: §§ 556d ff. BGB
- Modernisierung: §§ 555a ff. BGB
- WEG-Verwaltervertrag: §§ 26 ff. WEG

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `vertragspruefung-playbook`

**Fokus:** Immobilienrechtliche Vertraege nach standardisiertem Playbook prüfen: Kaufvertrag, Grundschuld, WEG. Normen: §§ 433 ff. 873 ff. BGB, WEG, GrEStG, GBO. Prüfraster: Playbook-Checkliste, Risikoklauseln, Notar- und Formerfordernisse. Output: Vertragsprüfergebnis mit Markierungen. Abgrenzung: nicht Vertragserstellung.

# Vertragsprüfung gegen Playbook

## Fachkern: Vertragsprüfung gegen Playbook
- **Spezialgegenstand:** Vertragsprüfung gegen Playbook wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB, GBO, WEG, BauGB, ErbbauRG, MaBV, Mietrecht, Grundpfandrechte, Notar-/Registervollzug und öffentlich-rechtliche Lasten.
- **Entscheidende Weiche:** Trenne Eigentum, Besitz, Grundbuchabteilung, Belastung, Fälligkeit, Vollzug, Mängel, Miet-/Nutzungsverhältnis und Finanzierung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Leitidee

Externe Verträge werden nicht freihändig geprüft, sondern gegen ein
hauseigenes Playbook. Das Playbook ist die institutionalisierte
Verhandlungserfahrung der Abteilung. Der Skill liefert Prüfergebnis,
Redline-Empfehlung und Business-Memo in einem Lauf.

## Inputs

- Externer Vertrag (.docx oder .pdf)
- Playbook (`playbook.md` oder `playbook.json`) mit Klauselkatalog
- Optional: interne Richtlinien (zB Mindest-Indexschwelle Maximalmietzeit)
- Optional: Vorvertrag oder LOI als Auslegungshilfe

## Playbook-Schema

```json
{
  "klausel_id": "indexmiete",
  "soll": "VPI mit Schwelle 5 Prozent und Mindestabstand zwölf Monate",
  "toleranz": "Schwelle drei bis sieben Prozent",
  "rot": "Vollindexierung ohne Schwelle oder Mindestabstand",
  "eskalation": "Asset-Management bei Abweichung",
  "fundstelle": "§ 557b BGB"
}
```

## Methodik

1. Vertrag in Klauseln segmentieren
2. Jede Klausel einem Playbook-Eintrag zuordnen (Klassifikation per
   Schlüsselwort und Semantik)
3. Ampel setzen — GRUEN entspricht Soll, GELB innerhalb Toleranz, ROT
   außerhalb Toleranz
4. Fehlende Klauseln als WEISS markieren (Schutzlücke)
5. Redline-Vorschlag in Tracked Changes erzeugen wo ROT oder WEISS
6. Business-Memo mit drei bis fünf Punkten was wirklich wirtschaftlich
   relevant ist

## Output

- `Pruefbericht_<Vertragsname>.md` mit Ampelmatrix in Tabellenform
- `<Vertragsname>_redlined.docx` mit Tracked Changes auf Klauselbasis
- `Memo_Business.md` — eine Seite, in Klartext, für Geschäftsleitung

## Typische Prüfthemen im Immobilienrecht

- Schriftform Gewerbemiete § 550 BGB inklusive aller Nachtraege
- Indexmiete § 557b BGB versus Staffelmiete § 557a BGB
- Konkurrenzschutz und Sortimentsschutz bei Gewerberaum
- Untervermietung und Nutzungsänderung
- Betriebskostenkatalog Verordnung 2003 und Umlagevereinbarung
- Schönheitsreparaturen-Klauseln (BGH-Rechtsprechung Quotenklausel)
- Endrenovierungsklauseln (unwirksam wenn formularmaessig)
- Mietpreisbremse §§ 556d ff. BGB bei Wohnraum
- Kappungsgrenze § 558 Abs. 3 BGB
- Kündigungsausschluss und Mindestlaufzeit
- Gewährleistungsausschluss beim Grundstückskaufvertrag und Arglist
- Erschliessungskosten und Anliegerbeitraege
- Altlasten und Baulastenverzeichnis
- Belastung mit Grunddienstbarkeiten und Wegerechten

## Beispielformulierungen

- "Prüfe diesen Gewerbemietvertrag gegen unser Playbook. Schwerpunkt
  Schriftform Indexierung und Konkurrenzschutz."
- "Externer Kaufvertrag liegt vor. Vergleiche mit Playbook und liefere
  Ampelmatrix plus Redline."
- "Property-Management-Vertrag ist gekommen. Was muss vor Unterschrift
  geändert werden, gemessen an unseren Mindeststandards?"

## Aktuelle Rechtsprechung — Leitsaetze fuer Playbook-Pruefung (Stand 05/2026, verifiziert dejure.org)

- **BGH 24.06.2020, VIII ZR 219/19** (Schriftform Gewerbemietvertrag § 550 BGB): Wahrung der Schriftform setzt voraus, dass alle wesentlichen Vertragsbedingungen aus einer Urkunde hervorgehen; bei Verweis auf Anlagen muessen diese koerperlich mit der Urkunde verbunden oder eindeutig in Bezug genommen sein. Quelle: dejure.org/2020,17128.
- **BGH 18.11.2020, VIII ZR 123/20** (Mietendeckel Berlin im Rahmen § 556d BGB) — vor Vermietung Pruefung der Spannungs-Gebiets-Verordnung. Quelle: dejure.org/2020,42367.
- **BVerfG 25.03.2021, 2 BvF 1/20** (Berliner Mietendeckel-Beschluss): Landesgesetzliche Mietpreisregelung verfassungswidrig (Bundesrecht abschliessend). Quelle: bundesverfassungsgericht.de.
- **BGH 18.03.2020, VIII ZR 64/19** — Maengel bei Wohnraummiete als Mietminderungsgrund. Quelle: dejure.org/2020,4895.
- **BGH 27.06.2024, I ZR 98/23** (Katjes „klimaneutral"): Greenwashing in Mietvertraegen mit ESG-Bezug; Substantiierungspflicht. Quelle: bundesgerichtshof.de PM 144/2024.

Konkrete weitere Entscheidungen vor Ausgabe per dejure.org / bundesgerichtshof.de mit Datum verifizieren.

## Paragrafenkette Immobilienvertraege

- Kaufvertrag: §§ 433 ff. BGB, § 311b BGB (Formzwang Notar), §§ 437 ff. BGB (Maengelrechte), § 442 BGB (Ausschluss Arglist)
- Gewerbemiete: §§ 535 ff. BGB, § 550 BGB (Schriftform langfristig), § 557b BGB (Indexmiete), §§ 579, 580 BGB (Sonderregeln)
- Wohnraummiete: §§ 549 ff. BGB, § 558 BGB (Kappungsgrenze), §§ 555b ff. BGB (Modernisierung), §§ 573 ff. BGB (Kuendigung)
- WEG-Verwaltervertrag: §§ 26 ff. WEG, § 19 Abs. 2 Nr. 6 WEG

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Integration mit Projekten und Agenten

Der Skill ist so gebaut, dass er in einem Projekt-Ordner mit fixiertem
Playbook und Vertragstyp laeuft. Ein Agent kann auf eingehende Vertraege
auf einem Watch-Ordner reagieren und automatisch die Pruefung anstossen.
Siehe Skill `projekt-arbeitsweise`.

## 3. `immo-share-deal-grunderwerbsteuer`

**Fokus:** Immobilien Share Deal Grunderwerbsteuer §§ 1 Abs. 2a, Abs. 2b, Abs. 3 GrEStG: Schwellen 90 Prozent, 5/10 Jahre Halte. Vergleich Asset Deal vs. Share Deal. Auswirkungen MoPeG.

# Share-Deal GrEStG

## Fachkern: Share-Deal GrEStG
- **Spezialgegenstand:** Share-Deal GrEStG wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB, GBO, WEG, BauGB, ErbbauRG, MaBV, Mietrecht, Grundpfandrechte, Notar-/Registervollzug und öffentlich-rechtliche Lasten.
- **Entscheidende Weiche:** Trenne Eigentum, Besitz, Grundbuchabteilung, Belastung, Fälligkeit, Vollzug, Mängel, Miet-/Nutzungsverhältnis und Finanzierung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** – streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - nur einschlaegige Normen, verifizierte Rechtsprechung und frei pruefbare amtliche Quellen; keine Literatur- oder Datenbankfundstellen erfinden.
3. **Pruefung im Gutachtenstil** – Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** – konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieser Skill gehoert zum Plugin `immobilienrechtspraxis`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen/Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Skill nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
