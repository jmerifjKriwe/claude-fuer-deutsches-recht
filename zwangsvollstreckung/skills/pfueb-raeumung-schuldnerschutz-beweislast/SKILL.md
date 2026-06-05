---
name: pfueb-raeumung-schuldnerschutz-beweislast
description: "Pfueb Raeumung Schuldnerschutz Beweislast im Plugin Zwangsvollstreckung: prüft konkret Pfueb, Raeumung, Schuldnerschutz. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Pfueb Raeumung Schuldnerschutz Beweislast

## Arbeitsbereich

**Pfueb Raeumung Schuldnerschutz Beweislast** ordnet den Fall über die tragenden Prüffelder: Pfueb, Raeumung, Schuldnerschutz. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-pfueb-risikoampel-und-gegenargumente` | Pfueb: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-raeumung-compliance-dokumentation-und-akte` | Raeumung: Compliance-Dokumentation und Aktenvermerk im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-schuldnerschutz-beweislast-und-darlegungslast` | Schuldnerschutz: Beweislast, Darlegungslast und Substantiierung im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

- Rolle und Ziel im Plugin Zwangsvollstreckung §§ 704 ff klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: §§ 704 ff. ZPO; § 802l Kontensuche, Vermögensauskunft, Räumung; § 800 ZPO Notar; § 201 InsO, ZVG, EU-Kontenpfändung VO 655; § 765a Härtefall, Schuldnerschutz — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `spezial-pfueb-risikoampel-und-gegenargumente`

**Fokus:** Pfueb: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Pfueb: Risikoampel, Gegenargumente und Verteidigungslinien

## Spezialwissen: Pfueb: Risikoampel, Gegenargumente und Verteidigungslinien
- **Spezialgegenstand:** Pfueb: Risikoampel, Gegenargumente und Verteidigungslinien / pfueb risikoampel und gegenargumente. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** ZPO, InsO, ZVG, EU, VO.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Pfueb** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Materielle Weichen PfÜB (Pfändungs- und Überweisungsbeschluss)
- **Rechtsgrundlage (§§ 829, 835 ZPO):** Pfändung der Geldforderung des Schuldners gegen Dritten (Drittschuldner) durch Beschluss des Vollstreckungsgerichts; gleichzeitige Überweisung zur Einziehung (§ 835 ZPO).
- **Voraussetzungen (§ 750 ZPO):** Vollstreckungstitel mit vollstreckbarer Ausfertigung, Vollstreckungsklausel, Zustellung an den Schuldner vor Pfändung.
- **Zuständigkeit (§ 828 ZPO):** Funktionell und örtlich das Amtsgericht des Schuldnerwohnsitzes (Rechtspfleger).
- **Wirkung der Pfändung (§ 829 Abs. 3 ZPO):** Pfandrecht ab Zustellung an den Drittschuldner. Verfügungsverbot des Schuldners (§ 829 Abs. 1 S. 1 ZPO). Drittschuldner darf nur an Gläubiger zahlen (sonst Doppelzahlungsrisiko - § 836 BGB i.V.m. § 408 BGB).
- **Drittschuldnererklärung (§ 840 ZPO):** Drittschuldner muss innerhalb von zwei Wochen nach Zustellung erklären, ob und in welcher Höhe er anerkennt; ob andere Pfändungen vorliegen; ob Auseinandersetzungen anhängig sind. Pflichtwidrige Erklärung: Schadensersatz.
- **Pfändungsfreigrenzen (§ 850c ZPO):** Pfändbar nur über dem Freibetrag (alle zwei Jahre angepasste Pfändungsfreigrenzentabelle - Juli 2025 / Juli 2027). Bei Kontopfändung: P-Konto (§§ 850k, 850l ZPO) mit Grundfreibetrag und Erhöhungsbeträgen für Unterhaltspflichten.
- **§ 850c ZPO Tabelle:** Aktueller Grundfreibetrag (Stand 01.07.2025) wird halbjährlich von BMJV bekanntgegeben - immer im Bundesanzeiger / juris.bmj.de prüfen.
- **Erinnerung gegen PfÜB (§ 766 ZPO):** Vollstreckungserinnerung beim Vollstreckungsgericht; keine Frist, aber zügige Erhebung. Klauselgegenklage (§ 768 ZPO) und Vollstreckungsgegenklage (§ 767 ZPO) bei materiellen Einwendungen.
- **Praktiker-Tipp:** Vor PfÜB-Antrag stets Vermögensauskunft (§ 802c ZPO) und § 802l ZPO Kontensuche prüfen, um geeignete Drittschuldner zu identifizieren. Bei mehreren Pfändungen zählt der Rang der Zustellung beim Drittschuldner.

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

## 2. `spezial-raeumung-compliance-dokumentation-und-akte`

**Fokus:** Raeumung: Compliance-Dokumentation und Aktenvermerk im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Raeumung: Compliance-Dokumentation und Aktenvermerk

## Spezialwissen: Raeumung: Compliance-Dokumentation und Aktenvermerk
- **Spezialgegenstand:** Raeumung: Compliance-Dokumentation und Aktenvermerk / raeumung compliance dokumentation und akte. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** ZPO, InsO, ZVG, EU, VO.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Raeumung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Materielle Weichen Räumungsvollstreckung
- **Rechtsgrundlage (§§ 885-885a ZPO):** Zwangsweise Räumung durch Gerichtsvollzieher auf Antrag des Gläubigers nach rechtskräftigem Räumungstitel und Zustellung an den Schuldner.
- **Berliner Modell (§ 885a ZPO):** Eingeschränkte Räumung - Gläubiger ist nur verpflichtet, die Räume zu räumen; das Mobiliar verbleibt in der Wohnung. Der Gläubiger erwirbt nur das Vermieterpfandrecht (§ 562 BGB). Kostengünstiger.
- **Vollständige Räumung (sog. "Frankfurter Modell"):** Gerichtsvollzieher räumt einschließlich Mobiliar und lagert es ein; Lagerung gem. § 885 Abs. 4 ZPO. Schuldner kann Sachen binnen zwei Monaten herausholen, sonst Versteigerung. Höhere Kosten für Gläubiger.
- **Räumungsfrist (§ 721 ZPO):** Auf Antrag des Schuldners kann das Erkenntnisgericht eine Räumungsfrist bis zu einem Jahr gewähren (Verlängerung um 1 Jahr möglich), wenn besondere Härte (Kind, Krankheit, fehlender Ersatzwohnraum).
- **Vollstreckungsschutz (§ 765a ZPO):** Schuldner kann bei Härtefall (Tod, schwere Krankheit, Schwangerschaft) Antrag auf Vollstreckungsschutz stellen. Verzögert die Räumung, gewährt aber Zeit für Ersatzwohnraum. Antrag bei Vollstreckungsgericht.
- **Drei-Wochen-Frist (§ 721 Abs. 3 ZPO):** Verlängerungsantrag der Räumungsfrist drei Wochen vor Ablauf zu stellen.
- **Räumung an Sonn- und Feiertagen:** Grundsätzlich verboten (§ 758a Abs. 4 ZPO); werktags zwischen 21 Uhr und 6 Uhr nur mit Sondergenehmigung.
- **Mietkosten zwischen Kündigung und Räumung:** Schuldner schuldet Nutzungsentschädigung in Höhe der ortsüblichen Miete (§ 546a BGB), nicht den vereinbarten Mietzins.
- **Praktiker-Tipp:** Vor Räumungsklage immer prüfen: Adressaten korrekt (alle Mitmieter im Titel?), Räumlichkeiten genau bezeichnet (Stockwerk, Lage); fehlende Bezeichnungen führen zu Schwierigkeiten beim Gerichtsvollzieher. Kostenkalkulation: vollständige Räumung kann mehrere tausend Euro kosten - Berliner Modell oft wirtschaftlicher.

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

## 3. `spezial-schuldnerschutz-beweislast-und-darlegungslast`

**Fokus:** Schuldnerschutz: Beweislast, Darlegungslast und Substantiierung im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Schuldnerschutz: Beweislast, Darlegungslast und Substantiierung

## Spezialwissen: Schuldnerschutz: Beweislast, Darlegungslast und Substantiierung
- **Spezialgegenstand:** Schuldnerschutz: Beweislast, Darlegungslast und Substantiierung / schuldnerschutz beweislast und darlegungslast. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** ZPO, InsO, ZVG, EU, VO.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Schuldnerschutz** prüfen.
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
