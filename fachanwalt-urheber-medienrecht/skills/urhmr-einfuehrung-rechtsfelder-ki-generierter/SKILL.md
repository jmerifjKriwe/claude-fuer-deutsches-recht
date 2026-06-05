---
name: urhmr-einfuehrung-rechtsfelder-ki-generierter
description: "Nutze dies, wenn Urhmr Einfuehrung Rechtsfelder, Urhmr Ki Generierter Content Spezial, Urhmr Leistungsschutzrecht Presse Spezial im Plugin Fachanwalt Urheber Medienrecht konkret bearbeitet werden soll. Auslöser: Bitte Urhmr Einfuehrung Rechtsfelder, Urhmr Ki Generierter Content Spezial, Urhmr Leistungsschutzrecht Presse Spezial prüfen.; Erstelle eine Arbeitsfassung zu Urhmr Einfuehrung Rechtsfelder, Urhmr Ki Generierter Content Spezial, Urhmr Leistungsschutzrecht Presse Spezial.; Welche Normen und Nachweise brauche ich?."
---

# Urhmr Einfuehrung Rechtsfelder, Urhmr Ki Generierter Content Spezial, Urhmr Leistungsschutzrecht Presse Spezial

## Zweck

Dieser Skill ist ein eigenständiger Arbeitsbereich. Er verbindet mehrere sachlich benachbarte Arbeitsmodule. Wähle anhand des Sachverhalts das passende Modul, arbeite dessen Prüfroutine vollständig ab und kombiniere Module nur, wenn der Fall tatsächlich mehrere Themen berührt.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `urhmr-einfuehrung-rechtsfelder` | Urheber- und Medienrecht einfuehrend: UrhG, Verwertungsgesellschaften, Persoenlichkeitsrecht, Aeusserungsrecht (Presse-, Rundfunkrecht), Wettbewerbsrecht UWG, Telekommunikations- und Telemedienrecht. Entscheidungstabelle. |
| `urhmr-ki-generierter-content-spezial` | Spezialfall KI-generierter Content: keine Schoepfungshoehe ohne menschlichen Beitrag (BGH/EuGH-Linie), Trainingsdaten und § 44b UrhG TDM-Schranke, Pflicht zur Kennzeichnung nach KI-VO Art. 50, Haftung Plattform. Pruefraster. |
| `urhmr-leistungsschutzrecht-presse-spezial` | Spezialfall Leistungsschutzrecht Presseverleger §§ 87f ff. UrhG nach DSM-Reform: Snippet-Lizenz, Aggregator-Plattformen, Vergaberecht. Pruefraster Verlag und Plattform. |

## Arbeitsweg

Für **Urhmr Einfuehrung Rechtsfelder, Urhmr Ki Generierter Content Spezial, Urhmr Leistungsschutzrecht Presse Spezial** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `fachanwalt-urheber-medienrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `urhmr-einfuehrung-rechtsfelder`

**Fokus:** Urheber- und Medienrecht einfuehrend: UrhG, Verwertungsgesellschaften, Persoenlichkeitsrecht, Aeusserungsrecht (Presse-, Rundfunkrecht), Wettbewerbsrecht UWG, Telekommunikations- und Telemedienrecht. Entscheidungstabelle.

# UrhMR: Rechtsfelder

## Spezialwissen: UrhMR: Rechtsfelder
- **Spezialgegenstand:** UrhMR: Rechtsfelder / urhmr einfuehrung rechtsfelder. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** UrhG, UWG.
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
Dieser Skill gehoert zum Plugin `fachanwalt-urheber-medienrecht`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

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

## 2. `urhmr-ki-generierter-content-spezial`

**Fokus:** Spezialfall KI-generierter Content: keine Schoepfungshoehe ohne menschlichen Beitrag (BGH/EuGH-Linie), Trainingsdaten und § 44b UrhG TDM-Schranke, Pflicht zur Kennzeichnung nach KI-VO Art. 50, Haftung Plattform. Pruefraster.

# UrhMR: KI-Content

## Spezialwissen: UrhMR: KI-Content
- **Spezialgegenstand:** UrhMR: KI-Content / urhmr ki generierter content spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KI, BGH, UrhG, TDM, VO, Art. 50.
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
Dieser Skill gehoert zum Plugin `fachanwalt-urheber-medienrecht`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

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

## 3. `urhmr-leistungsschutzrecht-presse-spezial`

**Fokus:** Spezialfall Leistungsschutzrecht Presseverleger §§ 87f ff. UrhG nach DSM-Reform: Snippet-Lizenz, Aggregator-Plattformen, Vergaberecht. Pruefraster Verlag und Plattform.

# UrhMR: Leistungsschutzrecht Presse

## Spezialwissen: UrhMR: Leistungsschutzrecht Presse
- **Spezialgegenstand:** UrhMR: Leistungsschutzrecht Presse / urhmr leistungsschutzrecht presse spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** UrhG, DSM, BGH.
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
Dieser Skill gehoert zum Plugin `fachanwalt-urheber-medienrecht`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

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
