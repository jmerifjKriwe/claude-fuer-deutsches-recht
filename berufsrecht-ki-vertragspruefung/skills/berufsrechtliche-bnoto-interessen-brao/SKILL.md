---
name: berufsrechtliche-bnoto-interessen-brao
description: "Berufsrechtliche Bnoto Interessen BRAO im Plugin Berufsrecht Ki Vertragspruefung: prüft konkret Berufsrechtliche, Bnoto, Brao. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Berufsrechtliche Bnoto Interessen BRAO

## Arbeitsbereich

**Berufsrechtliche Bnoto Interessen BRAO** ordnet den Fall über die tragenden Prüffelder: Berufsrechtliche, Bnoto, Brao. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-berufsrechtliche-erstpruefung-und-mandatsziel` | Berufsrechtliche: Erstprüfung, Rollenklärung und Mandatsziel im Plugin berufsrecht ki vertragspruefung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-bnoto-mehrparteien-konflikt-und-interessen` | Bnoto: Mehrparteienkonflikt und Interessenmatrix im Plugin berufsrecht ki vertragspruefung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-brao-zahlen-schwellen-und-berechnung` | Brao: Zahlen, Schwellenwerte und Berechnung im Plugin berufsrecht ki vertragspruefung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

- Rolle und Ziel im Berufsrecht Ki Vertragspruefung klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 43e BRAO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `spezial-berufsrechtliche-erstpruefung-und-mandatsziel`

**Fokus:** Berufsrechtliche: Erstprüfung, Rollenklärung und Mandatsziel im Plugin berufsrecht ki vertragspruefung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Berufsrechtliche: Erstprüfung, Rollenklärung und Mandatsziel

## Spezialwissen: Berufsrechtliche: Erstprüfung, Rollenklärung und Mandatsziel
- **Spezialgegenstand:** Berufsrechtliche: Erstprüfung, Rollenklärung und Mandatsziel / berufsrechtliche erstpruefung und mandatsziel. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** AI, WP, BRAO, StBerG, WPO, PAO, BNotO, KI.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Berufsrechtliche KI-Prüfung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Berufsrechtliche Erstprüfung: 6-Schritte-Diagnose
1. **Berufsstand bestimmen:** Anwalt → BRAO, StB → StBerG, WP → WPO, Notar → BNotO, Patentanwalt → PAO. Bei interdisziplinärer Kanzlei alle einschlägigen Normen.
2. **Tool identifizieren:** Welches konkrete Produkt? Welche Funktion (Recherche, Drafting, Mandantenkommunikation, Übersetzung)? Welche Datenflüsse?
3. **Datenkategorien klassifizieren:** (a) keine Mandantendaten, (b) anonymisiert/pseudonymisiert, (c) identifizierbar — Default für (c) restriktiv.
4. **Hosting prüfen:** EU/EWR vs. Drittstaat (insb. USA). Bei US-Cloud: DPF-Mitgliedschaft, SCC-Modul, TIA.
5. **Vertragsprüfung:** Hauptvertrag, AVV (Art. 28 DSGVO), Mitwirkenden-Verpflichtung § 203 Abs. 4 StGB, SCC, TIA.
6. **Mandatsziel klären:** Sofort-Freigabe? Bedingte Freigabe mit Auflagen? Sperrung? Kanzlei-Richtlinie nachjustieren?

## Trade-off
Schnelle Freigabe vs. berufsrechtliche Absicherung: bei knapper Zeit konservativ "vorläufig nicht freigeben" und parallel Detailprüfung, statt überstürzte Freigabe mit späterem Rückruf. § 203 StGB und § 43e BRAO sind strict liability — Vorsatz ist nicht erforderlich.

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

## 2. `spezial-bnoto-mehrparteien-konflikt-und-interessen`

**Fokus:** Bnoto: Mehrparteienkonflikt und Interessenmatrix im Plugin berufsrecht ki vertragspruefung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Bnoto: Mehrparteienkonflikt und Interessenmatrix

## Spezialwissen: Bnoto: Mehrparteienkonflikt und Interessenmatrix
- **Spezialgegenstand:** Bnoto: Mehrparteienkonflikt und Interessenmatrix / bnoto mehrparteien konflikt und interessen. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** AI, WP, BRAO, StBerG, WPO, PAO, BNotO, KI.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Bnoto** prüfen.
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

## 3. `spezial-brao-zahlen-schwellen-und-berechnung`

**Fokus:** Brao: Zahlen, Schwellenwerte und Berechnung im Plugin berufsrecht ki vertragspruefung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Brao: Zahlen, Schwellenwerte und Berechnung

## Spezialwissen: Brao: Zahlen, Schwellenwerte und Berechnung
- **Spezialgegenstand:** Brao: Zahlen, Schwellenwerte und Berechnung / brao zahlen schwellen und berechnung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** AI, WP, BRAO, StBerG, WPO, PAO, BNotO, KI.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **BRAO** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Zentrale Schwellen und Sanktionen
- **§ 43e BRAO** (Inanspruchnahme von Dienstleistungen — Schweigepflicht): Verpflichtung des Dienstleisters zur Verschwiegenheit; Verstoß ist Pflichtwidrigkeit, anwaltsgerichtlich verfolgt nach §§ 113 ff. BRAO.
- **§ 113 BRAO**: Verweisung, Geldbuße bis 25.000 EUR, befristetes Berufsverbot bis 5 Jahre, Ausschließung aus der Anwaltschaft.
- **§ 50 BRAO** (Aktenführung): 6 Jahre Aufbewahrungspflicht nach Beendigung des Auftrags; bei elektronischer Ablage gleicher Sorgfaltsmaßstab.
- **§ 51 BRAO** (Berufshaftpflicht): Mindestversicherungssumme 250.000 EUR je Versicherungsfall, jährliche Mindestleistung das Vierfache. KI-bedingte Pflichtverletzungen sind grundsätzlich gedeckt, wenn nicht ausgeschlossen.
- **§ 203 StGB** (Verletzung von Privatgeheimnissen): Freiheitsstrafe bis 1 Jahr oder Geldstrafe; Abs. 4 — qualifizierte Tatbestände bis 5 Jahre.

## Schwellen in anderen Berufsordnungen
- **§ 62a StBerG** (Steuerberater — Inanspruchnahme Dienstleistungen mit Geheimnisbezug): Ahndung nach § 89 StBerG; bei vorsätzlichem Verstoß auch berufsgerichtlich.
- **§ 50a WPO** (Wirtschaftsprüfer): Verschwiegenheitserstreckung auf Dienstleister; § 64 WPO-Sanktionen.
- **§ 26a BNotO**: Notare; Sanktion über § 50 BNotO.
- **§ 39c PAO**: Patentanwälte; Sanktion über § 80 PAO.

## Berechnungs-Trade-off
Berufshaftpflicht wird typischerweise nach Sozietätsgröße und Schadensvolumen kalkuliert; KI-Einsatz erhöht die Schadensanfälligkeit, kann aber durch Hinweispflicht (Aufklärung des Mandanten) abgemildert werden. Versicherer fragen zunehmend nach Tool-Inventar; falsche Angabe kann Leistungsfreiheit auslösen (§ 19 VVG).

## Bußgeldrahmen DSGVO (parallel anwendbar)
Bei DSGVO-Verstoß durch KI-Einsatz: bis **20 Mio. EUR oder 4 % weltweiter Konzernumsatz** (Art. 83 Abs. 5). KI-VO addiert bei verbotenen Praktiken bis **35 Mio. EUR oder 7 % weltweiter Konzernumsatz** (Art. 99 Abs. 3 KI-VO).

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
