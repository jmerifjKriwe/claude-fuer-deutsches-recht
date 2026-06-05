---
name: br-ki-vertragspruefung-fristen-risiko-mandant
description: "BR KI Vertragspruefung Fristen Risiko Mandant im Plugin Berufsrecht Ki Vertragspruefung: prüft konkret Fristen- und Risikoampel im Plugin, Mandantenkommunikation im Plugin, Red-Team Qualitygate im Plugin. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# BR KI Vertragspruefung Fristen Risiko Mandant

## Arbeitsbereich

Dieser Skill behandelt **BR KI Vertragspruefung Fristen Risiko Mandant** als zusammenhängenden Arbeitsgang im Plugin Berufsrecht Ki Vertragspruefung. Im Mittelpunkt steht die Prüfung von Fristen- und Risikoampel im Plugin, Mandantenkommunikation im Plugin, Red-Team Qualitygate im Plugin. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin berufsrecht-ki-vertragspruefung: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin berufsrecht-ki-vertragspruefung: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin berufsrecht-ki-vertragspruefung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |

## Arbeitsweg

- Rolle und Ziel im Berufsrecht Ki Vertragspruefung klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 43e BRAO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `workflow-fristen-und-risikoampel`

**Fokus:** Fristen- und Risikoampel im Plugin berufsrecht-ki-vertragspruefung: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.

# Fristen- und Risikoampel

## Aufgabe
Dieses Modul bearbeitet: Fristen- und Risikoampel im Plugin berufsrecht-ki-vertragspruefung: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen..

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

## Berufsrecht-KI-typische Risiken
- **§ 203 StGB**: Strafrechtliche Schweigepflichtverletzung — Freiheitsstrafe bis 1 Jahr oder Geldstrafe; Antragsdelikt § 205 StGB.
- **§ 43a Abs. 2 BRAO / § 43e BRAO**: Berufsrechtliche Verschwiegenheit, anwaltsgerichtliche Maßnahmen § 113 BRAO bis Ausschluss aus der Anwaltschaft.
- **DSGVO**: Art. 33 Datenpannenmeldung 72h, Bußgelder bis 20 Mio. EUR / 4 %.
- **KI-VO**: Schulungspflicht Art. 4 KI-VO seit 02.02.2025; Verbotene Praktiken Art. 5 (z. B. Social Scoring) — bis 35 Mio. EUR / 7 %.
- **Haftung**: zivilrechtliche Haftung gegenüber Mandantschaft (§§ 280, 611, 675 BGB), Anwaltshaftpflicht § 51 BRAO.

## Ampelkriterien
- **Rot**: Mandantendaten in nicht AVV-bewehrtes KI-Tool eingeführt; US-Cloud ohne TIA; Verstoß § 203 StGB sichtbar; aktuelle Beschwerde Rechtsanwaltskammer.
- **Gelb**: AVV vorhanden, aber TOM-Anlage fehlt; KI-Tool ohne dokumentierte Klassifizierung; Schulungsnachweis Art. 4 KI-VO offen.
- **Grün**: AVV + TOM + ggf. SCC + TIA; dokumentierte KI-Klassifizierung; Schulung; intern verabschiedete KI-Richtlinie.

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

**Fokus:** Mandantenkommunikation im Plugin berufsrecht-ki-vertragspruefung: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin berufsrecht-ki-vertragspruefung: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

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

## Berufsrechtskonforme Mandantenkommunikation (Kanzlei-intern bei KI-Tool-Prüfung)
- **Adressat:** Kanzleileitung / Partnerschaft / IT-Leitung / DSB.
- **Sachstand kurz:** Tool, Anbieter, Hosting, geplanter Einsatzbereich, betroffene Datenarten.
- **Bewertung:** Schweigepflicht (§ 203 StGB, § 43e BRAO bzw. § 62a StBerG, § 50a WPO, § 26a BNotO), AVV-Vollständigkeit, Drittlandstransfer (DPF/SCC/TIA).
- **Empfehlung:** Freigabe ja/nein/bedingt mit konkreten Auflagen (z. B. "ohne Mandantendaten", "nur intern", "nach Nachverhandlung AVV-Klausel X").
- **Risikoampel:** Rot/Gelb/Grün mit Begründung.
- **Frist und Verantwortlicher:** wer entscheidet final, wann.

## Externe Mandantenkommunikation (wenn KI-Einsatz im Mandat erfolgt)
- **Aufklärungstextbaustein für Mandatsvereinbarung** mit Hinweis auf KI-Nutzung, Anbieter, Datenfluss.
- **Ggf. Einwilligungsformular** bei besonders sensiblen Datenarten oder fehlender Anonymisierung.

## Praxis-Tipp
Die berufsrechtliche Aufklärungspflicht über KI-Einsatz wird in Rechtsprechung und Standesvertretung noch diskutiert — vorsichtig sein und im Zweifel transparent kommunizieren. Die berufsrechtliche KI-Debatte zur KI-Nutzung in Kanzleien (frei zugänglich auf anwaltverein.de) gibt eine Orientierung, ist aber nicht bindend.

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

**Fokus:** Red-Team Qualitygate im Plugin berufsrecht-ki-vertragspruefung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin berufsrecht-ki-vertragspruefung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

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

## Red-Team-Prüfpunkte Berufsrecht-KI
1. **Schweigepflicht-Trias:** § 203 StGB + § 43a Abs. 2 / § 43e BRAO (bzw. § 62a StBerG, § 50a WPO, § 26a BNotO) + AVV Art. 28 DSGVO — alle drei adressiert?
2. **Mitwirkenden-Klausel:** Wurde § 203 Abs. 4 StGB im AVV ausdrücklich umgesetzt? Verpflichtung des Anbieter-Personals?
3. **Datenkategorien:** Werden tatsächlich Mandantendaten verarbeitet? Selbst Metadaten (Mandantenname, Aktenzeichen, Verfahrensart) können Schweigepflicht-relevant sein.
4. **Drittlandstransfer:** Bei US-Cloud DPF-Status (zum Zeitpunkt der Prüfung), SCC-Modul, TIA dokumentiert? Cloud Act-Risiko beschrieben?
5. **Konkretisierung:** Welches konkrete KI-Tool, welche konkrete Funktion? Pauschalfreigaben sind berufsrechtlich nicht haltbar.
6. **Aufklärung Mandant:** Falls erforderlich (Sensibelheit, Marktstandards): Hinweis in Mandatsvereinbarung oder gesondertes Schreiben?
7. **Halluzinations-Check:** Keine erfundenen BGH-Az. (Zivilrechtsweg) oder AnwG-Entscheidungen; keine Vermischung BRAO/BGB/StGB.

## Praxis-Tipp
Die zentrale Empfehlung für KI-Vertragsprüfung bei Berufsträgern: Kategorisiere zuerst die Datenarten (a) keine Mandantendaten, b) anonymisierte/pseudonymisierte Mandantendaten, c) identifizierbare Mandantendaten). Für (c) reicht Standard-AVV nicht — es braucht zusätzlich die Mitwirkenden-Verpflichtung nach § 203 Abs. 4 StGB und ggf. Mandanteneinwilligung. Default für (c) bei US-Cloud: nicht freigeben.

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
