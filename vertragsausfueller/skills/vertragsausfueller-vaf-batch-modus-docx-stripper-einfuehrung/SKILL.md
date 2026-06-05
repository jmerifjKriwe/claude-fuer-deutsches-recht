---
name: vertragsausfueller-vaf-batch-modus-docx-stripper-einfuehrung
description: "VAF Batch Modus Docx Stripper Einfuehrung im Plugin Vertragsausfueller: prüft konkret Batch-Modus fuer Konzernvertraege, DOCX-Vorlage in strukturierten Text zerlegen, Einfuehrung Prozess Vertragsausfueller. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# VAF Batch Modus Docx Stripper Einfuehrung

## Arbeitsbereich

Dieser Skill behandelt **VAF Batch Modus Docx Stripper Einfuehrung** als zusammenhängenden Arbeitsgang im Plugin Vertragsausfueller. Im Mittelpunkt steht die Prüfung von Batch-Modus fuer Konzernvertraege, DOCX-Vorlage in strukturierten Text zerlegen, Einfuehrung Prozess Vertragsausfueller. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vaf-batch-modus-konzern` | Batch-Modus fuer Konzernvertraege: viele aehnliche Vertraege mit wechselnden Parteien und Werten, Massendatenimport CSV/XLSX, Plausibilitaetsregel-Set, Output 1 PDF pro Datensatz. Quality Gate und Reviewer-Sample. |
| `vaf-docx-stripper` | DOCX-Vorlage in strukturierten Text zerlegen: Anwendungsfall Word-Vertragsdokument muss in Absätze, Tabellen, Klauseln, Platzhalter, Anlagen und Signaturblöcke zerlegt werden ohne Originaldatei zu überschreiben. §§ 305 ff. BGB Klauselstruktur, Schriftform-Erfordernisse. Prüfraster DOCX-Zustand prüfen passwortgeschützt oder beschädigt, Track-Changes sichtbar machen, Platzhalter-Typen erkennen, Tabellenstruktur extrahieren. Output strukturiertes Dokumentinventar mit Klausel-Index und Platzhalter-Liste. Abgrenzung zu Template-Erkennung für Vertragstyp-Erkennung und zu Feldinventar. |
| `vaf-einfuehrung-prozess` | Einfuehrung Prozess Vertragsausfueller: vom Mandanteninterview ueber Variableninventar zum Template, Klauselentscheidung, Plausibilitaetscheck, Quality Gate. Schaubild und Reihenfolge der Sub-Skills. |

## Arbeitsweg

- Rolle und Ziel im Vertragsausfüller (Lückenschluss in Verträgen) klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: Vertragsspezifisch; § 195 BGB Regelverjährung 3 Jahre, § 14 BGB-InfoV Widerrufsfrist 14 Tage, EuGH-Vorgaben zu Klausel-Transparenz.
- Tragende Normen verifizieren: BGB §§ 133, 157, 305-310 (AGB-Kontrolle), 311b, 311c, 433, 488, 535, 631, 651a, 765, NachwG, FormularG, AGG (Diskriminierungsverbot) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Vertragspartner, Rechtsabteilung, Notar bei Formerfordernis, Datenschutzbeauftragter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Mustervertrag, Termsheet, Klauselkatalog, Altvertrag, Vertragsentwurf mit Track Changes, AGB-Prüfraster — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `vaf-batch-modus-konzern`

**Fokus:** Batch-Modus fuer Konzernvertraege: viele aehnliche Vertraege mit wechselnden Parteien und Werten, Massendatenimport CSV/XLSX, Plausibilitaetsregel-Set, Output 1 PDF pro Datensatz. Quality Gate und Reviewer-Sample.

# VAF: Batch-Modus Konzern

## Spezialwissen: VAF: Batch-Modus Konzern
- **Spezialgegenstand:** VAF: Batch-Modus Konzern / vaf batch modus konzern. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** CSV, XLSX, PDF, VAF.
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
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

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

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `vaf-docx-stripper`

**Fokus:** DOCX-Vorlage in strukturierten Text zerlegen: Anwendungsfall Word-Vertragsdokument muss in Absätze, Tabellen, Klauseln, Platzhalter, Anlagen und Signaturblöcke zerlegt werden ohne Originaldatei zu überschreiben. §§ 305 ff. BGB Klauselstruktur, Schriftform-Erfordernisse. Prüfraster DOCX-Zustand prüfen passwortgeschützt oder beschädigt, Track-Changes sichtbar machen, Platzhalter-Typen erkennen, Tabellenstruktur extrahieren. Output strukturiertes Dokumentinventar mit Klausel-Index und Platzhalter-Liste. Abgrenzung zu Template-Erkennung für Vertragstyp-Erkennung und zu Feldinventar.

# DOCX-Stripper


## Triage zu Beginn

1. Ist das DOCX vollständig abrufbar oder beschädigt/passwortgeschützt?
2. Enthält das Dokument Track-Changes-Markierungen die berücksichtigt werden müssen?
3. Gibt es strukturierte Platzhalter (eckige Klammern, XXX, TBD) oder nur unstrukturierte Freitextfelder?
4. Sind Tabellen vorhanden die als Feldinventar extrahiert werden sollen?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- §§ 133, 157 BGB — Vertragsauslegung (Auslegung nach Treu und Glauben)
- § 305c Abs. 2 BGB — Unklarheitenregel (gilt für Platzhalter-Auslegung)
- § 416 ZPO — Beweiskraft von Privaturkunden

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Aufgabe

Der Skill macht aus Word-Dokumenten ein bearbeitbares Vertragsmodell. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. Absätze, Überschriften, Listen, Tabellen, Fußnoten, Platzhalter und Anlagenhinweise extrahieren.
2. Platzhalter in eckigen Klammern, leere Linien, wiederkehrende Begriffe und Optionsklauseln erkennen.
3. Originaldatei unangetastet lassen und jeden Extrakt mit Dateiname, Stand und Quelle kennzeichnen.
4. Bei beschädigten oder gescannten Dateien einen OCR- oder manuellen Nachfasspfad anbieten.

## Ausgabe

- Vertragsdatenmatrix
- Rückfragenliste
- Ausfüllprotokoll
- Entwurfs- oder Prüfvermerk
- klare Stopper vor Track Changes, falls noch keine ausdrückliche Bestätigung vorliegt

## Leitplanken

- Originaldateien werden nie überschrieben.
- Track Changes, Redline oder Vergleichsfassung nur nach ausdrücklicher Rückfrage und Bestätigung.
- Offene Werte bleiben sichtbar; sie werden nicht erfunden.
- Juristische Wahlentscheidungen werden erklärt und protokolliert.

<!-- AUDIT 27.05.2026: BGH VII ZR 213/07 (14.01.2010) WRONG_TOPIC – tatsächliches Thema ist Verjährung der Rückforderung von Mangelbeseitigungsvorschüssen, NJW 2010, 1195 (nicht Urkundenauslegung, nicht NJW 2010, 1283). Verifiziert auf dejure.org (https://dejure.org/2010,781). Eintrag korrigiert. -->

## 3. `vaf-einfuehrung-prozess`

**Fokus:** Einfuehrung Prozess Vertragsausfueller: vom Mandanteninterview ueber Variableninventar zum Template, Klauselentscheidung, Plausibilitaetscheck, Quality Gate. Schaubild und Reihenfolge der Sub-Skills.

# VAF: Prozess einfuehrend

## Spezialwissen: VAF: Prozess einfuehrend
- **Spezialgegenstand:** VAF: Prozess einfuehrend / vaf einfuehrung prozess. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** VAF.
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
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

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

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
