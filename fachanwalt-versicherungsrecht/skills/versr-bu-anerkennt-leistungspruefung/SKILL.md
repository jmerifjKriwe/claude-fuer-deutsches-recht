---
name: versr-bu-anerkennt-leistungspruefung
description: "Nutze dies, wenn Versr Bu Anerkennt Was Spezial, Versr Bu Leistungspruefung Spezial, Versr Bu Nachpruefung Anerkenntnis im Plugin Fachanwalt Versicherungsrecht konkret bearbeitet werden soll. Auslöser: Bitte Versr Bu Anerkennt Was Spezial, Versr Bu Leistungspruefung Spezial, Versr Bu Nachpruefung Anerkenntnis prüfen.; Erstelle eine Arbeitsfassung zu Versr Bu Anerkennt Was Spezial, Versr Bu Leistungspruefung Spezial, Versr Bu Nachpruefung Anerkenntnis.; Welche Normen und Nachweise brauche ich?."
---

# Versr Bu Anerkennt Was Spezial, Versr Bu Leistungspruefung Spezial, Versr Bu Nachpruefung Anerkenntnis

## Zweck

Dieser Skill ist ein eigenständiger Arbeitsbereich. Er verbindet mehrere sachlich benachbarte Arbeitsmodule. Wähle anhand des Sachverhalts das passende Modul, arbeite dessen Prüfroutine vollständig ab und kombiniere Module nur, wenn der Fall tatsächlich mehrere Themen berührt.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `versr-bu-anerkennt-was-spezial` | Spezialfall Berufsunfaehigkeitsversicherung: Anerkennungsfaktum aktive Versicherung gegen Nachpruefung, konkrete und abstrakte Verweisung, 50-Prozent-BU. Beispielfall Streit ueber Anerkenntnis und Wiedereinsetzung der Leistung. |
| `versr-bu-leistungspruefung-spezial` | Spezialfall BU-Leistungspruefung: Berufsbeschreibung, 50-Prozent-Grenze, Mitwirkungspflichten, Nachpruefungsverfahren. Pruefraster fuer Versicherungsnehmer mit psychischer und somatischer Erkrankung. |
| `versr-bu-nachpruefung-anerkenntnis` | BU-Anerkenntnis, Nachprüfung und Leistungseinstellung: Vergleichszustand, Gesundheitsverbesserung, Berufswechsel, Mitwirkung und Prozessstrategie. |

## Arbeitsweg

Für **Versr Bu Anerkennt Was Spezial, Versr Bu Leistungspruefung Spezial, Versr Bu Nachpruefung Anerkenntnis** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `fachanwalt-versicherungsrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `versr-bu-anerkennt-was-spezial`

**Fokus:** Spezialfall Berufsunfaehigkeitsversicherung: Anerkennungsfaktum aktive Versicherung gegen Nachpruefung, konkrete und abstrakte Verweisung, 50-Prozent-BU. Beispielfall Streit ueber Anerkenntnis und Wiedereinsetzung der Leistung.

# Versr: BU-Anerkennt

## Spezialwissen: Versr: BU-Anerkennt
- **Spezialgegenstand:** Versr: BU-Anerkennt / versr bu anerkennt was spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BU.
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
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieser Skill gehoert zum Plugin `fachanwalt-versicherungsrecht`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
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

## 2. `versr-bu-leistungspruefung-spezial`

**Fokus:** Spezialfall BU-Leistungspruefung: Berufsbeschreibung, 50-Prozent-Grenze, Mitwirkungspflichten, Nachpruefungsverfahren. Pruefraster fuer Versicherungsnehmer mit psychischer und somatischer Erkrankung.

# VersR: BU-Leistungspruefung

## Spezialwissen: VersR: BU-Leistungspruefung
- **Spezialgegenstand:** VersR: BU-Leistungspruefung / versr bu leistungspruefung spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BU.
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
Dieser Skill gehoert zum Plugin `fachanwalt-versicherungsrecht`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

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

## 3. `versr-bu-nachpruefung-anerkenntnis`

**Fokus:** BU-Anerkenntnis, Nachprüfung und Leistungseinstellung: Vergleichszustand, Gesundheitsverbesserung, Berufswechsel, Mitwirkung und Prozessstrategie.

# FA Versicherungsrecht: BU-Nachprüfung

## Einsatz

Für laufende BU-Renten, die nach Nachprüfung gefährdet sind.

## Norm- und Quellenanker

VVG §§ 172–177; AVB BU; ZPO; medizinischer Sachverständigenbeweis.

## Arbeitsfragen

1. Was wurde anerkannt?
2. Welche Änderung behauptet der Versicherer?
3. Ist die Nachprüfungsmitteilung formal und materiell tragfähig?

## Output

Nachprüfungsabwehr, medizinisches Fragenraster und Klageoption.

## Red Flags

- neue Tätigkeit ohne Lebensstellungsprüfung
- Besserung nur aus Aktenlage
- befristetes Anerkenntnis falsch behandelt

## Arbeitsstil

Konkrete Normen, konkrete Unterlagen, konkrete nächste Handlung. Keine pauschalen Empfehlungen; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle.
