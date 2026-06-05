---
name: anlage-red-anlagen-anlagenkonvolut-sonderfall
description: "Anlage RED Anlagen Anlagenkonvolut Sonderfall im Plugin Anlagen Zu Schriftsaetzen: prüft konkret Anlage, Anlagen, Anlagenkonvolut, Entscheidet Stempelbild. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Anlage RED Anlagen Anlagenkonvolut Sonderfall

## Arbeitsbereich

**Anlage RED Anlagen Anlagenkonvolut Sonderfall** ordnet den Fall über die tragenden Prüffelder: Anlage, Anlagen, Anlagenkonvolut. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-anlage-red-team-und-qualitaetskontrolle` | Anlage: Red-Team und Qualitätskontrolle im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-anlagen-tatbestand-beweis-und-belege` | Anlagen: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-anlagenkonvolut-sonderfall-und-edge-case` | Anlagenkonvolut: Sonderfall und Edge-Case-Prüfung im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-arial-mandantenkommunikation-entscheidungsvorlage` | Entscheidet Stempelbild, Deckblatt, Anlagenverzeichnis und Mandantenfreigabe so, dass die Anlage optisch und logisch eindeutig ist. |

## Arbeitsweg

- Rolle und Ziel im Anlagen Zu Schriftsaetzen klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `spezial-anlage-red-team-und-qualitaetskontrolle`

**Fokus:** Anlage: Red-Team und Qualitätskontrolle im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Anlage: Red-Team und Qualitätskontrolle



## Spezialwissen: Anlage: Red-Team und Qualitätskontrolle
- **Konkreter Gegenstand:** Anlage: Red-Team und Qualitätskontrolle im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung..
- **Normen-/Verfahrensanker:** ZPO/StPO/VwGO/ArbGG/SGG je nach Verfahren, beA-/ERV-Anforderungen, Anlagenlogik, Beweisangebot, Schwärzung und Dateiorganisation.
- **Entscheidende Weiche:** Anlage nur aufnehmen, wenn sie eine konkrete Behauptung trägt; Nummerierung, Fundstelle, Dateiname, OCR, Schwärzung und Versandfähigkeit müssen zusammenpassen.
- **Arbeitsprodukt:** Erstelle eine fallbezogene Matrix `Behauptung / Norm / Beleg / Risiko / Gegenargument / nächster Schritt`; keine bloße Wiederholung des allgemeinen Plugin-Workflows.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Anlage** prüfen.
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

## 2. `spezial-anlagen-tatbestand-beweis-und-belege`

**Fokus:** Anlagen: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Anlagen: Tatbestandsmerkmale, Beweisfragen und Beleglage



## Spezialwissen: Anlagen: Tatbestandsmerkmale, Beweisfragen und Beleglage
- **Konkreter Gegenstand:** Anlagen: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung..
- **Normen-/Verfahrensanker:** ZPO/StPO/VwGO/ArbGG/SGG je nach Verfahren, beA-/ERV-Anforderungen, Anlagenlogik, Beweisangebot, Schwärzung und Dateiorganisation.
- **Entscheidende Weiche:** Anlage nur aufnehmen, wenn sie eine konkrete Behauptung trägt; Nummerierung, Fundstelle, Dateiname, OCR, Schwärzung und Versandfähigkeit müssen zusammenpassen.
- **Arbeitsprodukt:** Erstelle eine fallbezogene Matrix `Behauptung / Norm / Beleg / Risiko / Gegenargument / nächster Schritt`; keine bloße Wiederholung des allgemeinen Plugin-Workflows.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Anlagen** prüfen.
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

## 3. `spezial-anlagenkonvolut-sonderfall-und-edge-case`

**Fokus:** Anlagenkonvolut: Sonderfall und Edge-Case-Prüfung im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Anlagenkonvolut: Sonderfall und Edge-Case-Prüfung



## Spezialwissen: Anlagenkonvolut: Sonderfall und Edge-Case-Prüfung
- **Konkreter Gegenstand:** Anlagenkonvolut: Sonderfall und Edge-Case-Prüfung im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung..
- **Normen-/Verfahrensanker:** ZPO/StPO/VwGO/ArbGG/SGG je nach Verfahren, beA-/ERV-Anforderungen, Anlagenlogik, Beweisangebot, Schwärzung und Dateiorganisation.
- **Entscheidende Weiche:** Anlage nur aufnehmen, wenn sie eine konkrete Behauptung trägt; Nummerierung, Fundstelle, Dateiname, OCR, Schwärzung und Versandfähigkeit müssen zusammenpassen.
- **Arbeitsprodukt:** Erstelle eine fallbezogene Matrix `Behauptung / Norm / Beleg / Risiko / Gegenargument / nächster Schritt`; keine bloße Wiederholung des allgemeinen Plugin-Workflows.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Anlagenkonvolut** prüfen.
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

## 4. `spezial-arial-mandantenkommunikation-entscheidungsvorlage`

**Fokus:** Entscheidet Stempelbild, Deckblatt, Anlagenverzeichnis und Mandantenfreigabe so, dass die Anlage optisch und logisch eindeutig ist.

# Stempelbild und Entscheidungsvorlage

## Zweck

Der Skill fokussiert die scheinbar kleinen Dinge: Arial-12-Stempel, Position, Deckblatt und die Frage, was der Mandant vor Einreichung freigeben muss.

## Mindestinput

- Musteranlage.
- Nummernkreis.
- Freigabebedarf.

## Arbeitsablauf

1. Definiere Stempel und Deckblatt.
2. Prüfe Lesbarkeit nach Stempel.
3. Formuliere Mandantenfreigabe mit Risiken.

## Ausgabe

- Stempelspezifikation.
- Freigabevermerk.
- Korrekturliste.

## Typische Fehler, die du aktiv suchst

- Unklare Anlagenfunktion: Die Datei existiert, aber niemand sagt, welche Tatsache sie beweist.
- Nummerierung folgt dem Ordner, nicht dem Schriftsatz.
- Der Schriftsatz versteckt entscheidenden Vortrag in der Anlage.
- Dateiname, Stempel oder Anlagenverzeichnis widersprechen einander.

## Anschluss-Skills

- `anlagen-zu-schriftsaetzen` für den Hauptworkflow.
- `anlagen-qualitygate-finalcheck` vor Versand.
- `schriftsatz-anlagen-mapping` für Belegmatrix und Lückenliste.

## Quellen- und Vorsichtsregel

Bei tragenden Aussagen zu Form, elektronischer Einreichung oder prozessualer Verwertbarkeit aktuelle amtliche Quellen prüfen: ZPO, BRAO, ERVV, ERVB und gerichtliche Hinweise. Keine BeckRS-/juris-/Literatur-Blindzitate. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle nennen.


## Vertiefter Anlagen-Workflow

Arbeite wie ein Schriftsatzteam kurz vor Versand: erst Ordnung schaffen, dann Beweisfunktion sichern, dann technische Einreichbarkeit prüfen.

1. **Materialkarte:** Jede Datei einer Tatsachenbehauptung, einem Schriftsatzabschnitt und einer Anlagenkategorie zuordnen. Dubletten, alte Fassungen, Screenshots ohne Datum und unleserliche Scans separat markieren.
2. **K1-Logik:** Nummerierung nicht nach Ordnerzufall, sondern nach Beweisgang: Vertrag/Grundlage, Kommunikation, Zahlung, Fristen/Zugang, Fotos/Screenshots, Tabellen, Behörden-/Gerichtsdokumente.
3. **Technikcheck:** PDF/A-Eignung, OCR, Seitenzählung, Dateigröße, Signatur-/beA-/ERVV-Kontext, Anlagenverzeichnis, Deckblatt und Dateinamen konsistent prüfen.
4. **Prozessrisiko:** Nichts Entscheidendes nur in der Anlage verstecken. Wenn eine Anlage eine tragende Tatsache beweist, muss der Schriftsatz diese Tatsache ausdrücklich behaupten und die Anlage präzise referenzieren.
5. **Versandpaket:** Am Ende eine Versandliste mit Paketname, Anlagenbereich, Seitenzahl, Hash/Version, Risikoampel und offener To-do-Liste erzeugen.

## Ergebnisqualität

- Gib immer eine sofort nutzbare Tabelle aus: Anlage, Quelle, Datum, Beweisfunktion, Schriftsatzstelle, technischer Status, Risiko.
- Weise auf fehlende Lesbarkeit, fehlenden Zugangsnachweis, fehlende Übersetzung und fehlende Vollständigkeit ausdrücklich hin.
- Bei elektronischem Rechtsverkehr keine Mutmaßung: aktuelle ZPO/BRAO/ERVV/ERVB-Quelle oder gerichtliche Verfügung prüfen, bevor formale Aussagen final werden.
