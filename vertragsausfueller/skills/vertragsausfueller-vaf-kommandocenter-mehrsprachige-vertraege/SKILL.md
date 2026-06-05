---
name: vertragsausfueller-vaf-kommandocenter-mehrsprachige-vertraege
description: "VAF Kommandocenter Mehrsprachige Vertraege im Plugin Vertragsausfueller: prüft konkret Vertragsausfüller Kommandocenter starten, Spezialfall mehrsprachige Vertraege deutsch / englisch, Bauleiter Platzhalterlogik. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# VAF Kommandocenter Mehrsprachige Vertraege

## Arbeitsbereich

Dieser Skill behandelt **VAF Kommandocenter Mehrsprachige Vertraege** als zusammenhängenden Arbeitsgang im Plugin Vertragsausfueller. Im Mittelpunkt steht die Prüfung von Vertragsausfüller Kommandocenter starten, Spezialfall mehrsprachige Vertraege deutsch / englisch, Bauleiter Platzhalterlogik. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vaf-kommandocenter` | Vertragsausfüller Kommandocenter starten: Anwendungsfall Anwalt oder Mandant möchte Vertrag ausfüllen und gibt Eingabe-Dokument an; Skill erkennt Vorlage Altvertrag Term Sheet oder Freitext und leitet in richtigen Workflow. Vertragsrecht §§ 145 ff. BGB, § 3a RVG Vergütung. Prüfraster Eingabedokument-Typ erkennen, Ausgabeziel Clean-Entwurf oder Redline klären, Track-Changes-Bestätigung einholen, Vertragstyp bestimmen. Output Deal-Start-Karte mit Weiterleitung zum Fachmodul. Abgrenzung zu Template-Erkennung für Vorlage-Analyse und zu Rückfrageninterview. |
| `vaf-mehrsprachige-vertraege-spezial` | Spezialfall mehrsprachige Vertraege deutsch / englisch: massgebliche Sprache, paralleler Aufbau, Uebersetzungsfehler. Pruefraster fuer internationale Mandate. |
| `vaf-platzhalterlogik-bauleiter` | Bauleiter Platzhalterlogik: Variablen, Pflichtfelder, optionale Bloecke, Konditionalen. Pruefraster fuer Templatebau und Fehlerquellen. |

## Arbeitsweg

- Rolle und Ziel im Vertragsausfüller (Lückenschluss in Verträgen) klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: Vertragsspezifisch; § 195 BGB Regelverjährung 3 Jahre, § 14 BGB-InfoV Widerrufsfrist 14 Tage, EuGH-Vorgaben zu Klausel-Transparenz.
- Tragende Normen verifizieren: BGB §§ 133, 157, 305-310 (AGB-Kontrolle), 311b, 311c, 433, 488, 535, 631, 651a, 765, NachwG, FormularG, AGG (Diskriminierungsverbot) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Vertragspartner, Rechtsabteilung, Notar bei Formerfordernis, Datenschutzbeauftragter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Mustervertrag, Termsheet, Klauselkatalog, Altvertrag, Vertragsentwurf mit Track Changes, AGB-Prüfraster — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `vaf-kommandocenter`

**Fokus:** Vertragsausfüller Kommandocenter starten: Anwendungsfall Anwalt oder Mandant möchte Vertrag ausfüllen und gibt Eingabe-Dokument an; Skill erkennt Vorlage Altvertrag Term Sheet oder Freitext und leitet in richtigen Workflow. Vertragsrecht §§ 145 ff. BGB, § 3a RVG Vergütung. Prüfraster Eingabedokument-Typ erkennen, Ausgabeziel Clean-Entwurf oder Redline klären, Track-Changes-Bestätigung einholen, Vertragstyp bestimmen. Output Deal-Start-Karte mit Weiterleitung zum Fachmodul. Abgrenzung zu Template-Erkennung für Vorlage-Analyse und zu Rückfrageninterview.

# Kommandocenter


## Triage zu Beginn

1. Was ist das Eingabedokument — Word-Vorlage, Altvertrag, Term Sheet, E-Mail oder Freitext?
2. Was ist das Ausgabeziel — Clean-Entwurf, Redline, Track Changes oder nur Ausfüllprotokoll?
3. Soll ein bestehender Vertrag ergänzt oder ein neuer erstellt werden?
4. Welche Parteien und welcher Vertragstyp (Kauf, Miete, Werk, Dienstleistung)?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- §§ 145 ff. BGB — Vertragsschluss (Angebot und Annahme)
- § 167 ff. BGB — Vollmacht (Vertretungsbefugnis prüfen)
- § 305 BGB — AGB-Einbeziehung
- § 177 BGB — Genehmigung schwebend unwirksamer Verträge

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Aufgabe

Der Skill steuert den gesamten von Upload bis neuem Vertragsentwurf. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. Eingänge trennen: Vorlage, Altvertrag, Term Sheet, handschriftliche Notizen, E-Mail und Datenliste.
2. Ausgabeziel klären: neuer Clean-Vertrag, Ausfüllprotokoll, Rückfragenliste, Redline oder Track-Changes-Fassung.
3. Vor jeder Redline- oder Track-Changes-Ausgabe ausdrücklich fragen und ohne Bestätigung nur Clean-Entwurf oder Änderungsprotokoll erstellen.
4. Nächste Schritte nach Risiko, Datenlücken und Dokumentqualität priorisieren.

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

## 2. `vaf-mehrsprachige-vertraege-spezial`

**Fokus:** Spezialfall mehrsprachige Vertraege deutsch / englisch: massgebliche Sprache, paralleler Aufbau, Uebersetzungsfehler. Pruefraster fuer internationale Mandate.

# VAF: Mehrsprachige Vertraege

## Spezialwissen: VAF: Mehrsprachige Vertraege
- **Spezialgegenstand:** VAF: Mehrsprachige Vertraege / vaf mehrsprachige vertraege spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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

## 3. `vaf-platzhalterlogik-bauleiter`

**Fokus:** Bauleiter Platzhalterlogik: Variablen, Pflichtfelder, optionale Bloecke, Konditionalen. Pruefraster fuer Templatebau und Fehlerquellen.

# VAF: Platzhalterlogik Bauleiter

## Spezialwissen: VAF: Platzhalterlogik Bauleiter
- **Spezialgegenstand:** VAF: Platzhalterlogik Bauleiter / vaf platzhalterlogik bauleiter. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** VAF, BGH, BVerfG.
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
