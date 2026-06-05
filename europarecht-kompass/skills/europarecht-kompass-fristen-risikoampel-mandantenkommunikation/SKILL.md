---
name: europarecht-kompass-fristen-risikoampel-mandantenkommunikation
description: "Fristen Risikoampel Mandantenkommunikation im Europarecht: prüft konkret Fristen- und Risikoampel im Plugin europarecht-kompass, Mandantenkommunikation im Plugin europarecht-kompass, Red-Team Qualitygate im Plugin europarecht-kompass. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Fristen Risikoampel Mandantenkommunikation

## Arbeitsbereich

**Fristen Risikoampel Mandantenkommunikation** ordnet den Fall über die tragenden Prüffelder: Fristen- und Risikoampel im Plugin europarecht-kompass, Mandantenkommunikation im Plugin europarecht-kompass, Red-Team Qualitygate im Plugin europarecht-kompass. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin europarecht-kompass: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin europarecht-kompass: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin europarecht-kompass: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |

## Arbeitsweg

- Rolle und Ziel im Europarecht (allgemein) klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: AEUV Art. 263 Nichtigkeitsklage 2 Monate, Art. 265 Untätigkeitsklage 2 Monate, Art. 267 Vorlage jederzeit, Vertragsverletzungsverfahren Art. 258 unbefristet.
- Tragende Normen verifizieren: EUV, AEUV (insb. Art. 4, 5, 18, 20, 21, 34, 49, 56, 101, 102, 107, 108, 263, 267, 288, 340), GRCh, EU-VO (Beispiele 2016/679 DSGVO, 2024/1689 KI-VO, 139/2004 FKVO), EU-Richtlinien, EuGH-Rechtsprechung — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: EU-Kommission, Rat, Europäisches Parlament, EuGH, EuG, Mitgliedstaaten, nationale Gerichte (Vorlage Art. 267 AEUV), Bundesregierung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Vorlagebeschluss Art. 267 AEUV, Nichtigkeitsklage, Beschwerde an EU-KOM, Stellungnahme im Vertragsverletzungsverfahren, Notifizierung, EuGH-Urteilsbeleg — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `workflow-fristen-und-risikoampel`

**Fokus:** Fristen- und Risikoampel im Plugin europarecht-kompass: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.

# Fristen- und Risikoampel

## Aufgabe
Dieses Modul bearbeitet: Fristen- und Risikoampel im Plugin europarecht-kompass: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Unionsrechtliche Fristen (Ampelraster)

- **Rot — 2 Monate ab Bekanntgabe:** Nichtigkeitsklage natürlicher/juristischer Personen gegen Unionsakte (Art. 263 Abs. 6 AEUV); zuzüglich 10 Tage Entfernungspauschale (Art. 51 VerfO EuG/EuGH).
- **Rot — angemessene Zeit:** Untätigkeitsklage Art. 265 AEUV nach erfolgloser Aufforderung an das Organ binnen 2 Monaten.
- **Rot — Vorabentscheidungsersuchen Art. 267 AEUV:** Für letztinstanzliche Gerichte regelmäßig Vorlagepflicht (CILFIT/Consorzio-Kriterien). Frist gibt es nicht — aber Verzögerungsrisiko und Haftungsfragen prüfen.
- **Rot — Eilvorabentscheidung:** PPU/eilbedürftiges Verfahren (Art. 107 VerfO EuGH) bei Freiheitsentziehung, Sorgerecht, drohender Vollziehung.
- **Gelb — Vertragsverletzungsverfahren Art. 258 AEUV:** Aufforderungsschreiben, begründete Stellungnahme, Klage — Fristen werden von Kommission gesetzt (regelmäßig 2 Monate).
- **Gelb — Beihilfen:** Anmeldepflicht Art. 108 Abs. 3 AEUV (Stand-Still); Rückforderung 10-Jahres-Frist (Art. 17 VO 2015/1589).
- **Praxis-Tipp:** Direkte Wirkung und Vorrang sind nicht "Frist", sondern Argumentationsanker — gegen nationale Norm immer unionsrechtskonforme Auslegung zuerst, dann Anwendungsvorrang (EuGH C-6/64 Costa/ENEL).

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 2. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin europarecht-kompass: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin europarecht-kompass: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 3. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin europarecht-kompass: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin europarecht-kompass: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.
