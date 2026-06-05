---
name: strafkammer-strafzumessung
description: "Strafkammer Strafzumessung im Plugin Strafzumessung: prüft konkret Strafkammer, Strafzumessung, Strafzumessungstatsachen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Strafkammer Strafzumessung

## Arbeitsbereich

**Strafkammer Strafzumessung** ordnet den Fall über die tragenden Prüffelder: Strafkammer, Strafzumessung, Strafzumessungstatsachen. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-strafkammer-behoerden-gericht-und-registerweg` | Strafkammer: Behörden-, Gerichts- oder Registerweg im Plugin strafzumessung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-strafzumessung-erstpruefung-und-mandatsziel` | Strafzumessung: Erstprüfung, Rollenklärung und Mandatsziel im Plugin strafzumessung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-strafzumessungstatsachen-vergleich-eskalation` | Strafzumessungstatsachen: Verhandlung, Vergleich und Eskalation im Plugin strafzumessung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

- Rolle und Ziel im Strafzumessung nach deutschem Strafrecht vom Strafbefehl bis zur grossen Strafkammer klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 56; § 49 Regelbeispiele besonders schwerer Fall Verstaendigung; § 257c StPO TOA; § 46a Gesamtstrafe; § 55 JGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `spezial-strafkammer-behoerden-gericht-und-registerweg`

**Fokus:** Strafkammer: Behörden-, Gerichts- oder Registerweg im Plugin strafzumessung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Strafkammer: Behörden-, Gerichts- oder Registerweg

## Spezialwissen: Strafkammer: Behörden-, Gerichts- oder Registerweg
- **Spezialgegenstand:** Strafkammer: Behörden-, Gerichts- oder Registerweg / strafkammer behoerden gericht und registerweg. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** StPO, TOA, JGG, GVG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Strafkammer** prüfen.
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

## Qualitätsanker: Strafrahmen, Schuldprinzip und Gesamtstrafe

- **Verifizierte Rechtsprechungsanker:** BGH, Beschluss vom 14.05.2024 - 6 StR 502/23 zur Strafrahmenlogik/Sperrwirkung und gerechten Schuldstrafe; BGH, Beschluss vom 23.01.2024 - 3 StR 455/23 zum Doppelverwertungsverbot und Begründungsanforderungen; BGH, Beschluss vom 24.04.2024 - 5 StR 123/24 sowie BGH, Beschluss vom 03.06.2025 - 2 StR 333/24 zur nachträglichen Gesamtstrafenbildung, Zäsurwirkung und Härteausgleich.
- **Prüfreihenfolge:** Nie sofort ein „gefühltes Strafmaß“ bilden. Erst Tatbestand und anwendbares Recht, dann Strafrahmen, minder/ besonders schwerer Fall, vertypte Milderung, § 49 StGB, Doppelverwertungsverbot, § 46 StGB, Nebenfolgen, Bewährung, Gesamtstrafe.
- **§ 55-StGB-Disziplin:** Bei Vorverurteilungen immer Tatzeiten, Entscheidungsdaten, Rechtskraft, Vollstreckungsstand, erledigte/nicht erledigte Strafen und Zäsurwirkung als Tabelle verlangen. Unklare Gesamtstrafenlagen nicht glattbügeln, sondern als Risiko mit Alternativen ausgeben.
- **Output-Pflicht:** Strafzumessungsmemo mit Strafrahmenbaum, Zumessungstatsachen pro/contra, Revisionsrisiken und nächstem taktischem Schritt; bei Aktenbezug zusätzlich BZRG-/Urteils-/Vollstreckungsdaten-Lückenliste.

## 2. `spezial-strafzumessung-erstpruefung-und-mandatsziel`

**Fokus:** Strafzumessung: Erstprüfung, Rollenklärung und Mandatsziel im Plugin strafzumessung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Strafzumessung: Erstprüfung, Rollenklärung und Mandatsziel

## Spezialwissen: Strafzumessung: Erstprüfung, Rollenklärung und Mandatsziel
- **Spezialgegenstand:** Strafzumessung: Erstprüfung, Rollenklärung und Mandatsziel / strafzumessung erstpruefung und mandatsziel. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** StPO, TOA, JGG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Strafzumessung** prüfen.
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

## Strafzumessungs-Erstpruefung Bausteine
- **Mandantenrolle und Ziel:**
 - **Beschuldigter / Angeklagter:** Strafmilderung; Bewaehrung; Einstellung; Verstaendigung-Korridor.
 - **Verletzter / Nebenklage § 395 StPO:** Schaden-Wiedergutmachung; angemessene Sanktion.
 - **StA-Mitarbeit (selten Mandat):** Strafmasspruefung Antrag.
 - **Gericht/Schoeffe:** strafrahmen-konforme Entscheidung.
- **Sofort-Checkliste:**
 - Welcher Tatbestand? Strafrahmen abstrakt (Min-Max).
 - Vorstrafen (BZRG-Auszug); Verwertungsverbot § 51 BZRG.
 - Schuldfaehigkeit § 20 StGB / verminderte Schuldfaehigkeit § 21 StGB - Anhaltspunkte fuer Gutachten?
 - Tatschuld (objektive Schwere, subjektive Vorwerfbarkeit) - § 46 I 1 StGB Grundlage.
 - Pruefung Regelbeispiel / besonders schwerer Fall / minderschwerer Fall.
 - Strafrahmenverschiebung § 49 StGB pruefen.
- **Erwartungsspanne kommunizieren:**
 - **Geldstrafe** ueblicher Bereich nach Vergehen, Vorstrafen, Schuld: Zahl der TS; **Tagessatzhoehe** = 1/30 Nettoeinkommen.
 - **Freiheitsstrafe**: idR ab 6 Monaten (§ 47 StGB), Bewaehrungspraxis § 56 StGB.
 - **Nebenfolgen**: Fahrverbot § 44 StGB, Entziehung Fahrerlaubnis § 69 StGB, BZRG-Eintrag, FZR.
- **Mandatsziel-Matrix:** Sachverhalt vs. Beweislage; Beste-Case / Wahrscheinlichster / Worst-Case Strafmass.
- **Strategie:** Gestaendnis vs. Verteidigung; Verstaendigung § 257c StPO; TOA § 46a StGB; Einstellung §§ 153, 153a StPO.
- **Anschluss:** Tatbestand-Belege / Strafmilderung / Bewaehrung / Rechtsmittel.

## Qualitätsanker: Strafrahmen, Schuldprinzip und Gesamtstrafe

- **Verifizierte Rechtsprechungsanker:** BGH, Beschluss vom 14.05.2024 - 6 StR 502/23 zur Strafrahmenlogik/Sperrwirkung und gerechten Schuldstrafe; BGH, Beschluss vom 23.01.2024 - 3 StR 455/23 zum Doppelverwertungsverbot und Begründungsanforderungen; BGH, Beschluss vom 24.04.2024 - 5 StR 123/24 sowie BGH, Beschluss vom 03.06.2025 - 2 StR 333/24 zur nachträglichen Gesamtstrafenbildung, Zäsurwirkung und Härteausgleich.
- **Prüfreihenfolge:** Nie sofort ein „gefühltes Strafmaß“ bilden. Erst Tatbestand und anwendbares Recht, dann Strafrahmen, minder/ besonders schwerer Fall, vertypte Milderung, § 49 StGB, Doppelverwertungsverbot, § 46 StGB, Nebenfolgen, Bewährung, Gesamtstrafe.
- **§ 55-StGB-Disziplin:** Bei Vorverurteilungen immer Tatzeiten, Entscheidungsdaten, Rechtskraft, Vollstreckungsstand, erledigte/nicht erledigte Strafen und Zäsurwirkung als Tabelle verlangen. Unklare Gesamtstrafenlagen nicht glattbügeln, sondern als Risiko mit Alternativen ausgeben.
- **Output-Pflicht:** Strafzumessungsmemo mit Strafrahmenbaum, Zumessungstatsachen pro/contra, Revisionsrisiken und nächstem taktischem Schritt; bei Aktenbezug zusätzlich BZRG-/Urteils-/Vollstreckungsdaten-Lückenliste.

## 3. `spezial-strafzumessungstatsachen-vergleich-eskalation`

**Fokus:** Strafzumessungstatsachen: Verhandlung, Vergleich und Eskalation im Plugin strafzumessung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Strafzumessungstatsachen: Verhandlung, Vergleich und Eskalation

## Spezialwissen: Strafzumessungstatsachen: Verhandlung, Vergleich und Eskalation
- **Spezialgegenstand:** Strafzumessungstatsachen: Verhandlung, Vergleich und Eskalation / strafzumessungstatsachen vergleich eskalation. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** StPO, TOA, JGG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Strafzumessungstatsachen** prüfen.
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

## Strafzumessungstatsachen / Verhandlung Bausteine
- **Verstaendigung § 257c StPO Eckpunkte:**
 - **Inhalt zulaessig:** Strafrahmen-Korridor (Unter- und Obergrenze).
 - **Inhalt unzulaessig:** Schuldspruch verzichtbar; Massregeln § 257c II 3 StPO.
 - **Belehrung § 257c V StPO** als Wirksamkeitsvoraussetzung; Wegfall der Bindung bei neuen erheblichen Umstaenden.
 - **Geschaeftsgrundlage** regelmaessig Gestaendnis Angeklagter; aber Beweisaufnahme nicht ersparbar (BGH-Linie).
- **TOA § 46a StGB:**
 - **Nr. 1:** Wiedergutmachung des Schadens ganz oder ueberwiegend.
 - **Nr. 2:** Ernsthafte Bemuehung um Aussoehnung mit Verletztem.
 - **Folge:** Strafmilderung § 49 StGB / Absehen von Strafe (max. 1 Jahr Freiheitsstrafe / Geldstrafe).
 - **Praxis:** TOA-Vermittlungsstelle einschalten; Vereinbarung schriftlich; Erfuellung dokumentieren.
- **Schadenswiedergutmachung als Strafzumessungstatsache:**
 - Voll: erhebliche Strafmilderung.
 - Teilweise mit Tilgungsplan: dann moderate Milderung; Plan verbindlich machen.
 - Bei Vermoegensdelikten: Einziehung § 73 ff. StGB anrechnen.
- **Verhandlungsspielraum mit StA / Gericht:**
 - Strafmass-Korridor sondieren (Vorgespraech ausserhalb Hauptverhandlung).
 - Einstellung §§ 153, 153a StPO als Alternative.
 - Auflagen § 153a StPO (Schadenswiedergutmachung, Geldzahlung Bussgeld an gemeinnuetzige Einrichtung, gemeinnuetzige Arbeit).
- **Eskalation und Alternativen:**
 - Antrag Hauptverhandlung bei Erfolgsaussicht Beweisaufnahme.
 - Beweisantraege § 244 StPO.
 - Hilfsbeweisantraege bei Bedingung Verurteilung.
 - Schlussvortrag mit Strafmass-Argumentation entlang § 46 StGB.
- **Kompensation bei langer Verfahrensdauer:** Strafabschlag wegen rechtsstaatswidriger Verfahrensdauer Art. 6 EMRK / Art. 20 III GG; BGH-Vollstreckungsloesung (Anrechnung auf Strafe).

## Qualitätsanker: Strafrahmen, Schuldprinzip und Gesamtstrafe

- **Verifizierte Rechtsprechungsanker:** BGH, Beschluss vom 14.05.2024 - 6 StR 502/23 zur Strafrahmenlogik/Sperrwirkung und gerechten Schuldstrafe; BGH, Beschluss vom 23.01.2024 - 3 StR 455/23 zum Doppelverwertungsverbot und Begründungsanforderungen; BGH, Beschluss vom 24.04.2024 - 5 StR 123/24 sowie BGH, Beschluss vom 03.06.2025 - 2 StR 333/24 zur nachträglichen Gesamtstrafenbildung, Zäsurwirkung und Härteausgleich.
- **Prüfreihenfolge:** Nie sofort ein „gefühltes Strafmaß“ bilden. Erst Tatbestand und anwendbares Recht, dann Strafrahmen, minder/ besonders schwerer Fall, vertypte Milderung, § 49 StGB, Doppelverwertungsverbot, § 46 StGB, Nebenfolgen, Bewährung, Gesamtstrafe.
- **§ 55-StGB-Disziplin:** Bei Vorverurteilungen immer Tatzeiten, Entscheidungsdaten, Rechtskraft, Vollstreckungsstand, erledigte/nicht erledigte Strafen und Zäsurwirkung als Tabelle verlangen. Unklare Gesamtstrafenlagen nicht glattbügeln, sondern als Risiko mit Alternativen ausgeben.
- **Output-Pflicht:** Strafzumessungsmemo mit Strafrahmenbaum, Zumessungstatsachen pro/contra, Revisionsrisiken und nächstem taktischem Schritt; bei Aktenbezug zusätzlich BZRG-/Urteils-/Vollstreckungsdaten-Lückenliste.
