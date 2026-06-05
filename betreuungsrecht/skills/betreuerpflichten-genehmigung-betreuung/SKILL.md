---
name: betreuerpflichten-genehmigung-betreuung
description: "Betreuerpflichten Genehmigung Betreuung im Plugin Betreuungsrecht: prüft konkret Betreuerpflichten, Genehmigung und Berichtswesen, Betreuung, Betreuungsrechtliche. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Betreuerpflichten Genehmigung Betreuung

## Arbeitsbereich

**Betreuerpflichten Genehmigung Betreuung** ordnet den Fall über die tragenden Prüffelder: Betreuerpflichten, Genehmigung und Berichtswesen, Betreuung. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-betreuerpflichten-genehmigung-und-bericht` | Betreuerpflichten, Genehmigung und Berichtswesen: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-betreuung-mehrparteien-konflikt-und-interessen` | Betreuung: Mehrparteienkonflikt und Interessenmatrix im Plugin betreuungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-betreuungsrechtliche-erstpruefung-und-mandatsziel` | Betreuungsrechtliche: Erstprüfung, Rollenklärung und Mandatsziel im Plugin betreuungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

- Rolle und Ziel im Betreuungsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BtOG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `spezial-betreuerpflichten-genehmigung-und-bericht`

**Fokus:** Betreuerpflichten, Genehmigung und Berichtswesen: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output.

# Betreuerpflichten, Genehmigung und Berichtswesen

## Aufgabe
Dieser Skill ersetzt einen zu groben Spezial-Slot durch einen konkreten Fachim Plugin `betreuungsrecht`. Kontext des Plugins: Betreuungsrechtliche Skills für Jahresbericht, Vermögensverzeichnis, Genehmigungspflichten, Kontoanalyse und Verdachtsverträge nach BtOG und BGB.

Er arbeitet nicht lexikalisch, sondern fallbezogen: Er trennt zuerst Rollen, Ziel, Fristen, Zuständigkeiten und Belege, prüft dann die fachlichen Weichen und liefert ein Ergebnis, mit dem weitergearbeitet werden kann.

## Einstieg
Wenn Material vorliegt, nutze es zuerst. Frage nur nach, was für die nächste Entscheidung fehlt:

1. Wer handelt in welcher Rolle und gegen wen?
2. Welches praktische Ziel soll erreicht werden?
3. Welche Fristen, Termine, Zustellungen, Schwellenwerte oder Sanktionen stehen im Raum?
4. Welche Unterlagen, Daten, Registerauszüge, Bescheide, Verträge, Screenshots oder sonstigen Belege liegen vor?
5. Soll der Output intern, für Mandantschaft, Behörde, Gericht, Gegnerseite oder Gremium formuliert werden?

## Arbeitsworkflow
1. **Sortieren:** Sachverhalt, Dokumente und offene Punkte in eine knappe Fallmatrix bringen.
2. **Rechtsrahmen:** Einschlägige Normen, Zuständigkeiten, Verfahren, Fristen und formelle Anforderungen live prüfen, soweit Aktualität tragend ist.
3. **Materielle Weichen:** Die Kernfragen zu **Betreuerpflichten, Genehmigung und Berichtswesen** mit Tatbestandsmerkmalen, Belegen, Gegenargumenten und typischen Praxisfehlern abarbeiten.
4. **Risikoampel:** Ergebnis in Grün/Gelb/Rot mit Begründung, Unsicherheiten und Beweisbedarf einordnen.
5. **Anschluss:** Passende weitere Skills desselben Plugins vorschlagen, wenn Spezialprüfung, Schriftsatz, Tabelle, Brief oder Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- Kurzbild in fünf Sätzen: Lage, Ziel, Frist, Risiko, nächster Schritt.
- Prüfmatrix mit Punkt, Norm/Quelle, Tatsachen, Beleg, Bewertung, To-do.
- Konkreter Textbaustein oder Arbeitsprodukt passend zur Lage: Memo, Mandantenbrief, Behörden-/Gerichtsschreiben, Checkliste, Tabelle oder Verhandlungsagenda.
- Keine Scheingenauigkeit: Annahmen, Lücken und Live-Check-Bedarf offen markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwenden, wenn die Nutzerin oder der Nutzer den Text selbst bereitstellt; dann nicht als frei verifizierte Quelle ausgeben.

## 2. `spezial-betreuung-mehrparteien-konflikt-und-interessen`

**Fokus:** Betreuung: Mehrparteienkonflikt und Interessenmatrix im Plugin betreuungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Betreuung: Mehrparteienkonflikt und Interessenmatrix

## Spezialwissen: Betreuung: Mehrparteienkonflikt und Interessenmatrix
- **Spezialgegenstand:** Betreuung: Mehrparteienkonflikt und Interessenmatrix / betreuung mehrparteien konflikt und interessen. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BtOG, BGB.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Betreuung** prüfen.
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

## 3. `spezial-betreuungsrechtliche-erstpruefung-und-mandatsziel`

**Fokus:** Betreuungsrechtliche: Erstprüfung, Rollenklärung und Mandatsziel im Plugin betreuungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Betreuungsrechtliche: Erstprüfung, Rollenklärung und Mandatsziel

## Spezialwissen: Betreuungsrechtliche: Erstprüfung, Rollenklärung und Mandatsziel
- **Spezialgegenstand:** Betreuungsrechtliche: Erstprüfung, Rollenklärung und Mandatsziel / betreuungsrechtliche erstpruefung und mandatsziel. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BtOG, BGB, BtO.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Betreuungsrechtliche** prüfen.
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
