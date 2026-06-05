---
name: fortbestehensprognose-fbp-bankenkommunikation-waiver-integrierte
description: "FBP Bankenkommunikation Waiver Integrierte im Plugin Fortbestehensprognose: prüft konkret Spezialfall Bankenkommunikation und Waiver / Standstill bei, Bauleiter integrierte Planung GuV, Bilanz, Cashflow fuer IDW S 11. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# FBP Bankenkommunikation Waiver Integrierte

## Arbeitsbereich

**FBP Bankenkommunikation Waiver Integrierte** ordnet den Fall über die tragenden Prüffelder: Spezialfall Bankenkommunikation und Waiver / Standstill bei, Bauleiter integrierte Planung GuV, Bilanz. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `fbp-bankenkommunikation-waiver-spezial` | Spezialfall Bankenkommunikation und Waiver / Standstill bei drohender Zahlungsunfaehigkeit: Konsortium, Sicherheitenpool, MAC-Klausel. Pruefraster fuer Geschaeftsleitung und Treuhaender. |
| `fbp-integrierte-planung-bauleiter` | Bauleiter integrierte Planung GuV, Bilanz, Cashflow fuer IDW S 11. Pruefraster fuer Planungsschritte, Annahmen, Sensitivitaeten. Mustertext Annahmenverzeichnis. |
| `fbp-stresstest-szenarien-leitfaden` | Leitfaden Stresstest- und Szenarien-Aufbau fuer Fortbestehensprognose: Basis-, Stress- und Worst-Case, KPIs, Trigger fuer Massnahmen. Pruefraster fuer Beraterhand und Geschaeftsleitung. |

## Arbeitsweg

- Rolle und Ziel im Fortbestehensprognose (§ 19 InsO) klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: IDW S 11 12-Monats-Prognose ab Stichtag, § 15a InsO 6 Wochen bei Überschuldung, Drei-Wochen-Liquiditätsstockungs-Test, jährliche Aktualisierung.
- Tragende Normen verifizieren: InsO § 19 Abs. 2 (zweistufige Prüfung), IDW S 11 (Anforderungen), IDW PS 800, HGB § 252 Abs. 1 Nr. 2 (Going Concern), BGH II ZR 296/05 (Drei-Wochen-Lücke), StaRUG §§ 1, 102 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Restrukturierungsberater, IV (falls beauftragt), Bank, Gesellschafter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Fortbestehensprognose-Bericht, Integrierte Planung (P&L, BS, CF) 12+ Monate, Stresstest-Szenarien, Sanierungskonzept IDW S 6, Sanierungsgutachten, GF-Erklärung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `fbp-bankenkommunikation-waiver-spezial`

**Fokus:** Spezialfall Bankenkommunikation und Waiver / Standstill bei drohender Zahlungsunfaehigkeit: Konsortium, Sicherheitenpool, MAC-Klausel. Pruefraster fuer Geschaeftsleitung und Treuhaender.

# FBP: Bankenkommunikation Waiver

## Spezialwissen: FBP: Bankenkommunikation Waiver
- **Spezialgegenstand:** FBP: Bankenkommunikation Waiver / fbp bankenkommunikation waiver spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** MAC, FBP.
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
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

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

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `fbp-integrierte-planung-bauleiter`

**Fokus:** Bauleiter integrierte Planung GuV, Bilanz, Cashflow fuer IDW S 11. Pruefraster fuer Planungsschritte, Annahmen, Sensitivitaeten. Mustertext Annahmenverzeichnis.

# FBP: Integrierte Planung Bauleiter

## Spezialwissen: FBP: Integrierte Planung Bauleiter
- **Spezialgegenstand:** FBP: Integrierte Planung Bauleiter / fbp integrierte planung bauleiter. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** GuV, IDW, FBP, BGH, BVerfG.
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
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

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

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `fbp-stresstest-szenarien-leitfaden`

**Fokus:** Leitfaden Stresstest- und Szenarien-Aufbau fuer Fortbestehensprognose: Basis-, Stress- und Worst-Case, KPIs, Trigger fuer Massnahmen. Pruefraster fuer Beraterhand und Geschaeftsleitung.

# FBP: Stresstest-Szenarien

## Spezialwissen: FBP: Stresstest-Szenarien
- **Spezialgegenstand:** FBP: Stresstest-Szenarien / fbp stresstest szenarien leitfaden. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** FBP.
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
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

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

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
