---
name: kompendium-09-btr-erstantrag-und-e-bis-dokumentenscan-akten
description: "betreuungsrecht: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (btr-erstantrag-und-eilantrag, btr-zwangsmedikation-genehmigung-spezial, dokumentenscan-aktenablage-und-belegmappe) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 09 - betreuungsrecht

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `btr-erstantrag-und-eilantrag` | Erstantrag auf Betreuung beim Amtsgericht: § 1814 BGB Voraussetzungen seit Reform 2023, Eilantrag bei Gefahr im Verzug, einstweilige Anordnung § 300 FamFG. Strukturierte Antragsvorlage und Erfordernisse Sachverstaendigengutachten. |
| `btr-zwangsmedikation-genehmigung-spezial` | Spezialfall Genehmigung Zwangsmedikation § 1832 BGB nach Reform: enge Voraussetzungen, Erforderlichkeit, weniger eingreifende Mittel, gerichtliche Anhoerung Betroffener, Verfahrenspflegerbestellung. Pruefraster und Mustertexte. |
| `dokumentenscan-aktenablage-und-belegmappe` | Scan- und Ablageworkflow für Betreuungsakten: sortiert Fotos, PDFs, E-Mails, Bescheide, Kontoauszüge, Heim- und Arztunterlagen in eine gerichtstaugliche Belegmappe mit Fristen, Belegnummern, Datenschutzmarkierung und Lückenliste. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `btr-erstantrag-und-eilantrag`

**Frühere Beschreibung:** Erstantrag auf Betreuung beim Amtsgericht: § 1814 BGB Voraussetzungen seit Reform 2023, Eilantrag bei Gefahr im Verzug, einstweilige Anordnung § 300 FamFG. Strukturierte Antragsvorlage und Erfordernisse Sachverstaendigengutachten.

# Btr: Erst- und Eilantrag

## Spezialwissen: Btr: Erst- und Eilantrag
- **Spezialgegenstand:** Btr: Erst- und Eilantrag / btr erstantrag und eilantrag. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGB, FamFG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieser Skill gehoert zum Plugin `betreuungsrecht`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Skill nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `btr-zwangsmedikation-genehmigung-spezial`

**Frühere Beschreibung:** Spezialfall Genehmigung Zwangsmedikation § 1832 BGB nach Reform: enge Voraussetzungen, Erforderlichkeit, weniger eingreifende Mittel, gerichtliche Anhoerung Betroffener, Verfahrenspflegerbestellung. Pruefraster und Mustertexte.

# Btr: Zwangsmedikation

## Spezialwissen: Btr: Zwangsmedikation
- **Spezialgegenstand:** Btr: Zwangsmedikation / btr zwangsmedikation genehmigung spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGB.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieser Skill gehoert zum Plugin `betreuungsrecht`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Skill nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `dokumentenscan-aktenablage-und-belegmappe`

**Frühere Beschreibung:** Scan- und Ablageworkflow für Betreuungsakten: sortiert Fotos, PDFs, E-Mails, Bescheide, Kontoauszüge, Heim- und Arztunterlagen in eine gerichtstaugliche Belegmappe mit Fristen, Belegnummern, Datenschutzmarkierung und Lückenliste.

# Dokumentenscan, Aktenablage und Belegmappe

## Zweck

Ehrenamtliche Betreuer verlieren oft nicht am Recht, sondern an Papier. Dieser Skill macht aus einem Stapel Post, Handyfotos, PDFs, E-Mails und Kontoauszügen eine nutzbare Akte.

## Ordnerlogik

Empfohlene Struktur:

```text
01_gericht
02_person-und-wuensche
03_gesundheit-und-pflege
04_wohnen-und-heim
05_vermoegen-und-konten
06_vertraege-und-versicherungen
07_behoerden-und-sozialleistungen
08_korrespondenz
09_berichte-und-entwuerfe
10_risiko-und-genehmigung
```

## Belegnummern

Nutze sprechende Belegnummern:

```text
G-2026-001_Beschluss_AG_Mitte_2026-05-12.pdf
K-2026-014_Kontoauszug_Sparkasse_Mai_2026.pdf
H-2026-003_Heimvertrag_Auszug_2026-05-18.pdf
M-2026-002_Medikationsplan_2026-05-20.jpg
```

## Scan-Regeln

- Jede Seite vollständig, gerade, lesbar, mit Datum.
- Umschläge nur scannen, wenn Zustellung/Frist wichtig sein kann.
- Bescheide immer mit Rechtsbehelfsbelehrung erfassen.
- Kontoauszüge vollständig, nicht nur auffällige Buchungen.
- Medizinische Daten besonders markieren und nur zweckbezogen verwenden.
- WhatsApp/SMS nur übernehmen, wenn Inhalt für Wunsch, Konflikt, Frist oder Beweis wichtig ist.

## Automatische Auswertung

Bei Uploads:

1. Dokumentart erkennen.
2. Datum, Absender, Aktenzeichen, Frist und Betrag herausziehen.
3. Datenschutzstufe setzen: normal / sensibel / Gesundheitsdaten / höchst sensibel.
4. Passenden Ordner und Belegnummer vorschlagen.
5. Lücken nennen: fehlende Seiten, unleserliche Stellen, fehlende Anlagen.
6. Nächsten Skill routen: Jahresbericht, Vermögensverzeichnis, Genehmigung, Kontoanalyse oder Gerichtskommunikation.

## Output

- `Aktenindex`
- `Belegliste`
- `Fristenliste`
- `Lückenliste`
- `Einreichungspaket für Betreuungsgericht`

## Qualitätsgate

Keine erfundenen Inhalte. Wenn ein Scan unleserlich ist, ausdrücklich sagen, welche Passage fehlt. Bei rechtlich tragenden Aussagen Normtext und Formularstand live prüfen.
