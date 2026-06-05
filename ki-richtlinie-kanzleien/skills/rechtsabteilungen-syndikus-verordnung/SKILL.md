---
name: rechtsabteilungen-syndikus-verordnung
description: "Rechtsabteilungen Syndikus Verordnung im Plugin Ki Richtlinie Kanzleien: prüft konkret Rechtsabteilungen, Syndikus, Verordnung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Rechtsabteilungen Syndikus Verordnung

## Arbeitsbereich

**Rechtsabteilungen Syndikus Verordnung** ordnet den Fall über die tragenden Prüffelder: Rechtsabteilungen, Syndikus, Verordnung. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-rechtsabteilungen-risikoampel-und-gegenargumente` | Rechtsabteilungen: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin ki richtlinie kanzleien; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-syndikus-schriftsatz-brief-und-memo-bausteine` | Syndikus: Schriftsatz-, Brief- und Memo-Bausteine im Plugin ki richtlinie kanzleien; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-verordnung-mehrparteien-konflikt-und-interessen` | Verordnung: Mehrparteienkonflikt und Interessenmatrix im Plugin ki richtlinie kanzleien; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

- Rolle und Ziel im Ki Richtlinie Kanzleien klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; DSGVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `spezial-rechtsabteilungen-risikoampel-und-gegenargumente`

**Fokus:** Rechtsabteilungen: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin ki richtlinie kanzleien; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Rechtsabteilungen: Risikoampel, Gegenargumente und Verteidigungslinien

## Spezialwissen: Rechtsabteilungen: Risikoampel, Gegenargumente und Verteidigungslinien
- **Spezialgegenstand:** Rechtsabteilungen: Risikoampel, Gegenargumente und Verteidigungslinien / rechtsabteilungen risikoampel und gegenargumente. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KI, BRAO, BORA, DSGVO, BRAK, DAV.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Rechtsabteilungen Kanzlei-KI** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Risikoampel Rechtsabteilung Syndikus-KI-Einsatz
- **Syndikusspezifika:** Syndikusrechtsanwalt nach § 46 BRAO; Schweigepflicht über Unternehmensgeheimnisse (Konkurrentenschutz, Insider-Informationen, M&A-Verhandlungen).
- **Konfliktfeld:** KI-Tools können Unternehmensdaten in Anbieter-Infrastruktur laden — § 17 UWG / § 4 GeschGehG (Geschäftsgeheimnisschutz) plus § 43a BRAO.
- **§ 87 Abs. 1 Nr. 6 BetrVG:** Bei größeren Unternehmen Betriebsratsbeteiligung — KI-Tool, das Verhaltens-/Leistungsdaten erfasst, ist mitbestimmungspflichtig.
- **Compliance-Schnittstelle:** Kartellrecht (z. B. Kommunikation mit Konkurrenz), Geldwäsche (§ 2 GwG), Sanktionsrecht — KI darf keine kritischen Informationen leaken.

## Risikoampel
- **Rot:** KI-Tool für M&A-/Compliance-Beratung ohne AVV, ohne Verschwiegenheits-Verpflichtung, mit US-Cloud ohne DPF/SCC/TIA.
- **Gelb:** KI-Tool freigegeben, aber Schulung der Syndikus-Anwälte fehlt; Betriebsrat nicht beteiligt.
- **Grün:** Tool-Whitelist mit AVV + Mitwirkenden-Verpflichtung § 203 Abs. 4 StGB + Betriebsvereinbarung + dokumentierter Schulungsnachweis.

## Gegenargumente bei Vorwurf der Pflichtverletzung
- "Wir haben Tool X freigegeben mit Auflage Y" — Whitelist und Auflagen müssen schriftlich dokumentiert sein.
- "Mitarbeitender hat Auflagen missachtet" — Schulungsnachweis + verpflichtende Kenntnisnahme.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 2. `spezial-syndikus-schriftsatz-brief-und-memo-bausteine`

**Fokus:** Syndikus: Schriftsatz-, Brief- und Memo-Bausteine im Plugin ki richtlinie kanzleien; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Syndikus: Schriftsatz-, Brief- und Memo-Bausteine

## Spezialwissen: Syndikus: Schriftsatz-, Brief- und Memo-Bausteine
- **Spezialgegenstand:** Syndikus: Schriftsatz-, Brief- und Memo-Bausteine / syndikus schriftsatz brief und memo bausteine. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KI, BRAO, BORA, DSGVO, BRAK, DAV.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Syndikus-KI-Memo** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Memo-Bausteine Syndikus-KI-Richtlinie
- **Memo "Tool-Freigabe an Unternehmensleitung"** mit Aufbau:
 1. Anlass + Hintergrund
 2. Geprüfte Tools mit Klassifizierung KI-VO/DSGVO
 3. Vertragsprüfung (AVV, SCC, DPF, TIA)
 4. Empfehlung mit Risikoampel
 5. Vorgeschlagene Auflagen (z. B. "ohne Mandantendaten in Strafrecht-Mandaten")
 6. Inkrafttreten
- **Brief "Aufklärung Mandant über KI-Nutzung"** mit:
 1. Transparenz über Tool-Nutzung
 2. Datenarten und -fluss
 3. Sicherheitsmaßnahmen (TOM)
 4. ggf. Einwilligungs-Option
 5. Widerspruchsmöglichkeit
- **Schriftsatz "Verteidigung gegen Aufsichtsbeschwerde"** mit:
 1. Sachverhalt aus Mandantenperspektive
 2. Eigene Risikomatrix
 3. Konformitätsnachweis (Whitelist, Schulung, AVV)
 4. Hinweis auf DAV/BRAK-Hinweise
 5. Bitte um Einstellung

## Praxis-Tipp
Memo an Unternehmensleitung: zuerst eine Seite mit Executive Summary + Risikoampel + Empfehlung; erst auf den Folgeseiten die Detailbegründung. Geschäftsleitung entscheidet auf Basis des ersten Absatzes — wer alle Details auf Seite 1 packt, verliert die Entscheidung im Rauschen.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 3. `spezial-verordnung-mehrparteien-konflikt-und-interessen`

**Fokus:** Verordnung: Mehrparteienkonflikt und Interessenmatrix im Plugin ki richtlinie kanzleien; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Verordnung: Mehrparteienkonflikt und Interessenmatrix

## Spezialwissen: Verordnung: Mehrparteienkonflikt und Interessenmatrix
- **Spezialgegenstand:** Verordnung: Mehrparteienkonflikt und Interessenmatrix / verordnung mehrparteien konflikt und interessen. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KI, BRAO, BORA, DSGVO, BRAK, DAV.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Verordnung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.
