---
name: dpmaregister-epue-beweislast-erfinderische
description: "Dpmaregister Epue Beweislast Erfinderische im Plugin Patentrecherche: prüft konkret Dpmaregister, Epue, Erfinderische. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Dpmaregister Epue Beweislast Erfinderische

## Arbeitsbereich

**Dpmaregister Epue Beweislast Erfinderische** ordnet den Fall über die tragenden Prüffelder: Dpmaregister, Epue, Erfinderische. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-dpmaregister-schriftsatz-brief-und-memo-bausteine` | Dpmaregister: Schriftsatz-, Brief- und Memo-Bausteine im Plugin patentrecherche; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-epue-beweislast-und-darlegungslast` | Epue: Beweislast, Darlegungslast und Substantiierung im Plugin patentrecherche; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-erfinderische-sonderfall-und-edge-case` | Erfinderische: Sonderfall und Edge-Case-Prüfung im Plugin patentrecherche; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

- Rolle und Ziel im Patentrecherche und FTO klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: EPÜ R. 36 Teilanmeldung, PatG § 41 Priorität 12 Monate, USPTO Provisional 12 Monate, EPO Recherchebericht typ. 6 Monate.
- Tragende Normen verifizieren: PatG §§ 1, 3, 4, 9, 10, 139, EPÜ Art. 54, 56, 64, 69, 87 ff., Straßburger IPC-Abkommen, PCT, Espacenet-Datenbankzugriff, DEPATISnet-Bedingungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Patentanmelder, Patentanwalt, DPMA-Prüfer, EPO-Examiner, USPTO, WIPO, Wettbewerber.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Recherchebericht, FTO-Gutachten, Patentlandschaftsanalyse, Espacenet/DEPATISnet/Patentscope/PatFT-Ausdruck, IPC-Klassifikationsbaum — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `spezial-dpmaregister-schriftsatz-brief-und-memo-bausteine`

**Fokus:** Dpmaregister: Schriftsatz-, Brief- und Memo-Bausteine im Plugin patentrecherche; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Dpmaregister: Schriftsatz-, Brief- und Memo-Bausteine

## Spezialwissen: Dpmaregister: Schriftsatz-, Brief- und Memo-Bausteine
- **Spezialgegenstand:** Dpmaregister: Schriftsatz-, Brief- und Memo-Bausteine / dpmaregister schriftsatz brief und memo bausteine. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EPO/WIPO/USPTO/DPMA sind Patentämter, INPADOC/CPC/IPC/Espacenet/DEPATISnet Recherchedatenbanken, FTO eine Arbeitsmethode — keine Rechtsquellen. Tragende Normen je nach Frage: PatG §§ 1–5 (Schutzfähigkeit, Neuheit), § 4 (erfinderische Tätigkeit), §§ 9, 10 (Schutzwirkung), §§ 34, 35, 37 (Anmeldung, Prioritäten), §§ 81 ff. (Nichtigkeit); EPÜ Art. 52–57 (Patentierbarkeit), Art. 54 (Neuheit), Art. 56 (erfinderische Tätigkeit), Art. 69 (Schutzbereich), Art. 87 ff. (Priorität); PCT Art. 1 ff.; UPCA. Quellen über DPMAregister, EPO Register, USPTO PatFT, WIPO Patentscope und WIPO Lex live prüfen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Dpmaregister** prüfen.
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

## 2. `spezial-epue-beweislast-und-darlegungslast`

**Fokus:** Epue: Beweislast, Darlegungslast und Substantiierung im Plugin patentrecherche; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Epue: Beweislast, Darlegungslast und Substantiierung

## Spezialwissen: Epue: Beweislast, Darlegungslast und Substantiierung
- **Spezialgegenstand:** Epue: Beweislast, Darlegungslast und Substantiierung / epue beweislast und darlegungslast. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EPO/WIPO/USPTO/DPMA sind Patentämter, INPADOC/CPC/IPC/Espacenet/DEPATISnet Recherchedatenbanken, FTO eine Arbeitsmethode — keine Rechtsquellen. Tragende Normen je nach Frage: PatG §§ 1–5 (Schutzfähigkeit, Neuheit), § 4 (erfinderische Tätigkeit), §§ 9, 10 (Schutzwirkung), §§ 34, 35, 37 (Anmeldung, Prioritäten), §§ 81 ff. (Nichtigkeit); EPÜ Art. 52–57 (Patentierbarkeit), Art. 54 (Neuheit), Art. 56 (erfinderische Tätigkeit), Art. 69 (Schutzbereich), Art. 87 ff. (Priorität); PCT Art. 1 ff.; UPCA. Quellen über DPMAregister, EPO Register, USPTO PatFT, WIPO Patentscope und WIPO Lex live prüfen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Epue** prüfen.
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

## 3. `spezial-erfinderische-sonderfall-und-edge-case`

**Fokus:** Erfinderische: Sonderfall und Edge-Case-Prüfung im Plugin patentrecherche; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Erfinderische: Sonderfall und Edge-Case-Prüfung

## Spezialwissen: Erfinderische: Sonderfall und Edge-Case-Prüfung
- **Spezialgegenstand:** Erfinderische: Sonderfall und Edge-Case-Prüfung / erfinderische sonderfall und edge case. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EPO/WIPO/USPTO/DPMA sind Patentämter, INPADOC/CPC/IPC/Espacenet/DEPATISnet Recherchedatenbanken, FTO eine Arbeitsmethode — keine Rechtsquellen. Tragende Normen je nach Frage: PatG §§ 1–5 (Schutzfähigkeit, Neuheit), § 4 (erfinderische Tätigkeit), §§ 9, 10 (Schutzwirkung), §§ 34, 35, 37 (Anmeldung, Prioritäten), §§ 81 ff. (Nichtigkeit); EPÜ Art. 52–57 (Patentierbarkeit), Art. 54 (Neuheit), Art. 56 (erfinderische Tätigkeit), Art. 69 (Schutzbereich), Art. 87 ff. (Priorität); PCT Art. 1 ff.; UPCA. Quellen über DPMAregister, EPO Register, USPTO PatFT, WIPO Patentscope und WIPO Lex live prüfen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Erfinderische** prüfen.
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
