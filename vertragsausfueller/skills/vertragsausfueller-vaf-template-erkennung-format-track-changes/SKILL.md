---
name: vertragsausfueller-vaf-template-erkennung-format-track-changes
description: "VAF Template Erkennung Format Track Changes im Plugin Vertragsausfueller: prüft konkret Vertragsvorlage und Altvertrag erkennen und analysieren, Template-Format und Quelle, Track Changes und Redline nur nach ausdrücklicher. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# VAF Template Erkennung Format Track Changes

## Arbeitsbereich

Dieser Skill behandelt **VAF Template Erkennung Format Track Changes** als zusammenhängenden Arbeitsgang im Plugin Vertragsausfueller. Im Mittelpunkt steht die Prüfung von Vertragsvorlage und Altvertrag erkennen und analysieren, Template-Format und Quelle, Track Changes und Redline nur nach ausdrücklicher. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vaf-template-erkennung` | Vertragsvorlage und Altvertrag erkennen und analysieren: Anwendungsfall Anwalt oder Mandant gibt unbekannte Vorlage oder alten Vertrag ein und Skill soll Vertragstyp Klauselstruktur Pflichtfelder und Wahlklauseln identifizieren. §§ 433 ff. BGB Kaufvertrag, §§ 535 ff. BGB Mietvertrag, §§ 611a ff. BGB Arbeitsvertrag. Prüfraster AGB vs. Individualvertrag, Sprache, strukturierte vs. unstrukturierte Platzhalter, Vertragstyp-Einordnung. Output Vorlage-Analyse mit Vertragstyp, Klauselliste und Pflichtfeld-Map. Abgrenzung zu DOCX-Stripper für rohe Textzerlegung und zu Feldinventar. |
| `vaf-template-format-und-source` | Template-Format und Quelle: Word-DOCX mit Formularfeldern, Markdown mit Platzhaltern, PDF AcroForm, Excel mit Variablenliste. Pro Format: Vor- und Nachteile, Migration, Backup. Pflicht zu sauberer Versionierung. |
| `vaf-track-changes-nur-nach-frage` | Track Changes und Redline nur nach ausdrücklicher Bestätigung erstellen: Anwendungsfall überarbeiteter Vertrag soll als Track-Changes-Fassung ausgegeben werden; Skill fragt vorher explizit nach Bestätigung. §§ 145 ff. BGB Änderungsverhandlung, §§ 305 ff. BGB AGB-Transparenz. Prüfraster ausdrückliche Bestätigung vorhanden, saubere Ausgangsfassung nach Quality Gate vorhanden, Ausgangspunkt für Änderungsmarkierung definiert, Kommentierung materiell relevanter Änderungen. Output Track-Changes-Fassung oder ablehnende Weiterleitung zu Clean-Output. Abgrenzung zu Redline-QA für Prüfung und zu Clean-Output. |

## Arbeitsweg

- Rolle und Ziel im Vertragsausfüller (Lückenschluss in Verträgen) klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: Vertragsspezifisch; § 195 BGB Regelverjährung 3 Jahre, § 14 BGB-InfoV Widerrufsfrist 14 Tage, EuGH-Vorgaben zu Klausel-Transparenz.
- Tragende Normen verifizieren: BGB §§ 133, 157, 305-310 (AGB-Kontrolle), 311b, 311c, 433, 488, 535, 631, 651a, 765, NachwG, FormularG, AGG (Diskriminierungsverbot) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Vertragspartner, Rechtsabteilung, Notar bei Formerfordernis, Datenschutzbeauftragter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Mustervertrag, Termsheet, Klauselkatalog, Altvertrag, Vertragsentwurf mit Track Changes, AGB-Prüfraster — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `vaf-template-erkennung`

**Fokus:** Vertragsvorlage und Altvertrag erkennen und analysieren: Anwendungsfall Anwalt oder Mandant gibt unbekannte Vorlage oder alten Vertrag ein und Skill soll Vertragstyp Klauselstruktur Pflichtfelder und Wahlklauseln identifizieren. §§ 433 ff. BGB Kaufvertrag, §§ 535 ff. BGB Mietvertrag, §§ 611a ff. BGB Arbeitsvertrag. Prüfraster AGB vs. Individualvertrag, Sprache, strukturierte vs. unstrukturierte Platzhalter, Vertragstyp-Einordnung. Output Vorlage-Analyse mit Vertragstyp, Klauselliste und Pflichtfeld-Map. Abgrenzung zu DOCX-Stripper für rohe Textzerlegung und zu Feldinventar.

# Template-Erkennung


## Triage zu Beginn

1. Welcher Vertragstyp liegt vor — Kauf, Miete, Werk, Dienstleistung, Lizenz, Arbeitsvertrag?
2. Ist die Vorlage ein AGB-Formular oder ein Individualvertrag?
3. In welcher Sprache ist die Vorlage — deutsch, englisch, zweisprachig?
4. Gibt es strukturierte Platzhalter ([...], XXX, TBD) oder nur unstrukturierten Freitext?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- §§ 433, 535, 631, 611 BGB — Kauf, Miete, Werk, Dienst (Vertragstypen)
- § 305 BGB — AGB-Einbeziehung
- § 305c Abs. 2 BGB — Unklarheitenregel (gegen Verwender)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Aufgabe

Der Skill klassifiziert den Vertrag und trennt Fixtext von Variablen. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. Vertragstyp, Parteien, Gegenstand, Leistung, Entgelt, Laufzeit, Kündigung, Haftung, Anlagen und Signaturen erkennen.
2. Fixe Stammdaten des Verwenders von variablen Mandatsdaten trennen.
3. Wahlklauseln als Entscheidungspunkte markieren, nicht stillschweigend streichen.
4. Feldnamen normalisieren, damit Term Sheet und Vorlage zusammengeführt werden können.

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

## 2. `vaf-template-format-und-source`

**Fokus:** Template-Format und Quelle: Word-DOCX mit Formularfeldern, Markdown mit Platzhaltern, PDF AcroForm, Excel mit Variablenliste. Pro Format: Vor- und Nachteile, Migration, Backup. Pflicht zu sauberer Versionierung.

# VAF: Template-Format und Quelle

## Spezialwissen: VAF: Template-Format und Quelle
- **Spezialgegenstand:** VAF: Template-Format und Quelle / vaf template format und source. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DOCX/PDF/Vorlagenlogik sind Technik. Rechtlich je nach Vertrag BGB §§ 145 ff., 241, 280, 305 ff., 311; einschlägige Formvorschriften; bei Einreichung ZPO/beA-Vorgaben; bei Verbrauchern §§ 312 ff., 355 ff. BGB live prüfen.
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

## 3. `vaf-track-changes-nur-nach-frage`

**Fokus:** Track Changes und Redline nur nach ausdrücklicher Bestätigung erstellen: Anwendungsfall überarbeiteter Vertrag soll als Track-Changes-Fassung ausgegeben werden; Skill fragt vorher explizit nach Bestätigung. §§ 145 ff. BGB Änderungsverhandlung, §§ 305 ff. BGB AGB-Transparenz. Prüfraster ausdrückliche Bestätigung vorhanden, saubere Ausgangsfassung nach Quality Gate vorhanden, Ausgangspunkt für Änderungsmarkierung definiert, Kommentierung materiell relevanter Änderungen. Output Track-Changes-Fassung oder ablehnende Weiterleitung zu Clean-Output. Abgrenzung zu Redline-QA für Prüfung und zu Clean-Output.

# Track Changes nur nach Frage


## Triage zu Beginn

1. Hat der Nutzer ausdrücklich (und mit "Ja" bestätigt) eine Track-Changes- oder Redline-Fassung gewünscht?
2. Liegt eine saubere Ausgangsfassung vor (Clean-Entwurf nach Quality Gate)?
3. Ist klar, welche Version als Ausgangspunkt für die Änderungsmarkierungen dient?
4. Sollen alle Änderungen kommentiert werden oder nur materiell relevante?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 241 Abs. 2 BGB — Rücksichtnahmepflicht (Transparenz in Vertragsverhandlungen)
- § 123 BGB — Anfechtung wegen Täuschung (bei verdeckten Änderungen)
- § 3 BRAO — anwaltliche Sorgfaltspflicht

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Aufgabe

Der Skill setzt die ausdrückliche Nachfragepflicht durch. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. Immer fragen: Soll ich zusätzlich eine Track-Changes- oder Redline-Fassung erstellen?
2. Ohne Ja keine Änderungsfassung erzeugen.
3. Bei Ja Ausgangsdokument, Zielentwurf und Änderungslog trennen.
4. Änderungen erklärbar halten und keine verdeckten materiellen Änderungen einbauen.

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
