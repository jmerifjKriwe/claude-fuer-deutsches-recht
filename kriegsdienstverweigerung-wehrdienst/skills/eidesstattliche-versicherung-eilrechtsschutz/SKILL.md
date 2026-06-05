---
name: eidesstattliche-versicherung-eilrechtsschutz
description: "Eidesstattliche Versicherung Eilrechtsschutz im Kriegsdienstverweigerung und Wehrdienst: prüft konkret Prüft, ob eidesstattliche Versicherungen zulässig oder sinnvoll, Prüft § 80 oder § 123 VwGO bei drohendem Dienst an der Waffe, ob Einberufung trotz KDV-Antrag zulässig sein kann. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Eidesstattliche Versicherung Eilrechtsschutz

## Arbeitsbereich

**Eidesstattliche Versicherung Eilrechtsschutz** ordnet den Fall über die tragenden Prüffelder: Prüft, ob eidesstattliche Versicherungen zulässig oder sinnvoll, Prüft § 80 oder § 123 VwGO bei drohendem Dienst an der Waffe. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `eidesstattliche-versicherung` | Prüft, ob eidesstattliche Versicherungen zulässig oder sinnvoll sind. |
| `eilrechtsschutz-drohende-einberufung` | Prüft § 80 oder § 123 VwGO bei drohendem Dienst an der Waffe. |
| `einberufung-nach-antrag` | Prüft, ob Einberufung trotz KDV-Antrag zulässig sein kann. |
| `eingang-und-pk-nachweis` | Sichert Zugang, Aktenzeichen und Fristbeginn für spätere Rechtsschutzschritte. |
| `einstweilige-anordnung-vwgo-123` | Prüft vorläufige Regelung ohne passenden §80-Fall. |

## Arbeitsweg

- Rolle und Ziel im Praxisplugin für Kriegsdienstverweigerung und Wehrdienst aus Gewissensgründen: Art klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GG Art. 4 Abs. 3, KDVG, ZDG, Wehrpflichtgesetz (ausgesetzt), § 12 KDVG, SG §§ 30, 31; Art. 4 Abs; KDVG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `eidesstattliche-versicherung`

**Fokus:** Prüft, ob eidesstattliche Versicherungen zulässig oder sinnvoll sind.

# Eidesstattliche Versicherung Grenzen

## Fachkern: Eidesstattliche Versicherung Grenzen
- **Spezialgegenstand:** Eidesstattliche Versicherung Grenzen; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Prüft Widerspruch, Klage, § 75 VwGO, § 80 VwGO, § 123 VwGO und besondere KDVG-Fristen.

## Fachlicher Kern
Prüft, ob eidesstattliche Versicherungen zulässig oder sinnvoll sind. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

## Sofortfragen
1. Welche Personengruppe liegt vor: ungedient, wehrpflichtig, FWDL, SaZ, Berufssoldat, Reservist, frühere Soldatin/früherer Soldat oder Sonderfall?
2. Gibt es bereits Antrag, Eingangsbestätigung, Personenkennziffer, Musterungsbescheid, BAFzA-Schreiben, Anhörung oder Bescheid?
3. Geht es um Kriegsdienst mit der Waffe als Gewissensproblem oder um Politik, Gesundheit, Angst, Karriere, Familie oder Totalverweigerung?
4. Welche Frist läuft und welcher Nachweis liegt für Zugang oder Bekanntgabe vor?

## Arbeitsgang
1. Status und anwendbare Normen festlegen.
2. Pflichtunterlagen und fehlende Dokumente markieren.
3. Gewissenskern von bloßen Randmotiven trennen.
4. Behördenweg BAPersBw -> BAFzA oder Soldaten-/Reservistenpfad bestimmen.
5. Output knapp, würdig und nachweisbar formulieren.

## Norm- und Quellenanker
WPflG § 19; VwGO/ZPO live prüfen

## Output
- Statusampel.
- Unterlagen- und Fristenliste.
- nächster Schriftsatz oder nächste Verfahrenshandlung.
- Warnhinweis, falls der Fall in Totalverweigerung, bloße Politik oder Disziplinarrisiko kippt.

## Rote Linien
Fristen, Zustellung und Dokumenttyp prüfen, bevor Widerspruch, Klage oder Eilantrag vorgeschlagen werden.

## Anschluss-Skills
- `kriegsdienstverweigerung-wehrdienst-allgemein` für Kaltstart und Routing.
- `qualitaetsgate-vor-ausgabe` vor belastbarer Ausgabe.
- `rechtsprechung-livecheck` bei Gerichtsargumentation.

## Quellen- und Aktualitätsregel
- Aktuelle Fassung von GG, KDVG, WPflG, SG und VwGO in amtlichen Quellen prüfen.
- BAFzA-Hinweise zum Antragsweg, zur hohen Antragslast und zu § 13 KDVG n. F. berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Link nennen.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.

## 2. `eilrechtsschutz-drohende-einberufung`

**Fokus:** Prüft § 80 oder § 123 VwGO bei drohendem Dienst an der Waffe.

# Eilrechtsschutz bei Einberufung

## Fachkern: Eilrechtsschutz bei Einberufung
- **Spezialgegenstand:** Eilrechtsschutz bei Einberufung; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Prüft Widerspruch, Klage, § 75 VwGO, § 80 VwGO, § 123 VwGO und besondere KDVG-Fristen.

## Fachlicher Kern
Prüft § 80 oder § 123 VwGO bei drohendem Dienst an der Waffe. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

## Sofortfragen
1. Welche Personengruppe liegt vor: ungedient, wehrpflichtig, FWDL, SaZ, Berufssoldat, Reservist, frühere Soldatin/früherer Soldat oder Sonderfall?
2. Gibt es bereits Antrag, Eingangsbestätigung, Personenkennziffer, Musterungsbescheid, BAFzA-Schreiben, Anhörung oder Bescheid?
3. Geht es um Kriegsdienst mit der Waffe als Gewissensproblem oder um Politik, Gesundheit, Angst, Karriere, Familie oder Totalverweigerung?
4. Welche Frist läuft und welcher Nachweis liegt für Zugang oder Bekanntgabe vor?

## Arbeitsgang
1. Status und anwendbare Normen festlegen.
2. Pflichtunterlagen und fehlende Dokumente markieren.
3. Gewissenskern von bloßen Randmotiven trennen.
4. Behördenweg BAPersBw -> BAFzA oder Soldaten-/Reservistenpfad bestimmen.
5. Output knapp, würdig und nachweisbar formulieren.

## Norm- und Quellenanker
KDVG §§ 3, 11, 13; VwGO §§ 80, 123

## Output
- Statusampel.
- Unterlagen- und Fristenliste.
- nächster Schriftsatz oder nächste Verfahrenshandlung.
- Warnhinweis, falls der Fall in Totalverweigerung, bloße Politik oder Disziplinarrisiko kippt.

## Rote Linien
Fristen, Zustellung und Dokumenttyp prüfen, bevor Widerspruch, Klage oder Eilantrag vorgeschlagen werden.

## Anschluss-Skills
- `kriegsdienstverweigerung-wehrdienst-allgemein` für Kaltstart und Routing.
- `qualitaetsgate-vor-ausgabe` vor belastbarer Ausgabe.
- `rechtsprechung-livecheck` bei Gerichtsargumentation.

## Quellen- und Aktualitätsregel
- Aktuelle Fassung von GG, KDVG, WPflG, SG und VwGO in amtlichen Quellen prüfen.
- BAFzA-Hinweise zum Antragsweg, zur hohen Antragslast und zu § 13 KDVG n. F. berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Link nennen.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.

## 3. `einberufung-nach-antrag`

**Fokus:** Prüft, ob Einberufung trotz KDV-Antrag zulässig sein kann.

# Einberufung nach Antrag

## Fachkern: Einberufung nach Antrag
- **Spezialgegenstand:** Einberufung nach Antrag; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Ordnet Behördenrollen, Musterung, Registrierung, Zuleitung, Anhörung, Anerkennung und Ablehnung.

## Fachlicher Kern
Prüft, ob Einberufung trotz KDV-Antrag zulässig sein kann. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

## Sofortfragen
1. Welche Personengruppe liegt vor: ungedient, wehrpflichtig, FWDL, SaZ, Berufssoldat, Reservist, frühere Soldatin/früherer Soldat oder Sonderfall?
2. Gibt es bereits Antrag, Eingangsbestätigung, Personenkennziffer, Musterungsbescheid, BAFzA-Schreiben, Anhörung oder Bescheid?
3. Geht es um Kriegsdienst mit der Waffe als Gewissensproblem oder um Politik, Gesundheit, Angst, Karriere, Familie oder Totalverweigerung?
4. Welche Frist läuft und welcher Nachweis liegt für Zugang oder Bekanntgabe vor?

## Arbeitsgang
1. Status und anwendbare Normen festlegen.
2. Pflichtunterlagen und fehlende Dokumente markieren.
3. Gewissenskern von bloßen Randmotiven trennen.
4. Behördenweg BAPersBw -> BAFzA oder Soldaten-/Reservistenpfad bestimmen.
5. Output knapp, würdig und nachweisbar formulieren.

## Norm- und Quellenanker
KDVG §§ 3, 13

## Output
- Statusampel.
- Unterlagen- und Fristenliste.
- nächster Schriftsatz oder nächste Verfahrenshandlung.
- Warnhinweis, falls der Fall in Totalverweigerung, bloße Politik oder Disziplinarrisiko kippt.

## Rote Linien
Keine schematische Antwort geben; die konkrete Gewissenslage, der Status und die aktuelle Rechtslage müssen sichtbar geprüft werden.

## Anschluss-Skills
- `kriegsdienstverweigerung-wehrdienst-allgemein` für Kaltstart und Routing.
- `qualitaetsgate-vor-ausgabe` vor belastbarer Ausgabe.
- `rechtsprechung-livecheck` bei Gerichtsargumentation.

## Quellen- und Aktualitätsregel
- Aktuelle Fassung von GG, KDVG, WPflG, SG und VwGO in amtlichen Quellen prüfen.
- BAFzA-Hinweise zum Antragsweg, zur hohen Antragslast und zu § 13 KDVG n. F. berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Link nennen.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.

## 4. `eingang-und-pk-nachweis`

**Fokus:** Sichert Zugang, Aktenzeichen und Fristbeginn für spätere Rechtsschutzschritte.

# Eingangsnachweis sichern

## Fachkern: Eingangsnachweis sichern
- **Spezialgegenstand:** Eingangsnachweis sichern; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Ordnet Behördenrollen, Musterung, Registrierung, Zuleitung, Anhörung, Anerkennung und Ablehnung.

## Fachlicher Kern
Sichert Zugang, Aktenzeichen und Fristbeginn für spätere Rechtsschutzschritte. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

## Sofortfragen
1. Welche Personengruppe liegt vor: ungedient, wehrpflichtig, FWDL, SaZ, Berufssoldat, Reservist, frühere Soldatin/früherer Soldat oder Sonderfall?
2. Gibt es bereits Antrag, Eingangsbestätigung, Personenkennziffer, Musterungsbescheid, BAFzA-Schreiben, Anhörung oder Bescheid?
3. Geht es um Kriegsdienst mit der Waffe als Gewissensproblem oder um Politik, Gesundheit, Angst, Karriere, Familie oder Totalverweigerung?
4. Welche Frist läuft und welcher Nachweis liegt für Zugang oder Bekanntgabe vor?

## Arbeitsgang
1. Status und anwendbare Normen festlegen.
2. Pflichtunterlagen und fehlende Dokumente markieren.
3. Gewissenskern von bloßen Randmotiven trennen.
4. Behördenweg BAPersBw -> BAFzA oder Soldaten-/Reservistenpfad bestimmen.
5. Output knapp, würdig und nachweisbar formulieren.

## Norm- und Quellenanker
KDVG § 2; VwGO § 75

## Output
- Statusampel.
- Unterlagen- und Fristenliste.
- nächster Schriftsatz oder nächste Verfahrenshandlung.
- Warnhinweis, falls der Fall in Totalverweigerung, bloße Politik oder Disziplinarrisiko kippt.

## Rote Linien
Keine schematische Antwort geben; die konkrete Gewissenslage, der Status und die aktuelle Rechtslage müssen sichtbar geprüft werden.

## Anschluss-Skills
- `kriegsdienstverweigerung-wehrdienst-allgemein` für Kaltstart und Routing.
- `qualitaetsgate-vor-ausgabe` vor belastbarer Ausgabe.
- `rechtsprechung-livecheck` bei Gerichtsargumentation.

## Quellen- und Aktualitätsregel
- Aktuelle Fassung von GG, KDVG, WPflG, SG und VwGO in amtlichen Quellen prüfen.
- BAFzA-Hinweise zum Antragsweg, zur hohen Antragslast und zu § 13 KDVG n. F. berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Link nennen.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.

## 5. `einstweilige-anordnung-vwgo-123`

**Fokus:** Prüft vorläufige Regelung ohne passenden §80-Fall.

# Einstweilige Anordnung § 123

## Fachkern: Einstweilige Anordnung § 123
- **Spezialgegenstand:** Einstweilige Anordnung § 123; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Prüft Widerspruch, Klage, § 75 VwGO, § 80 VwGO, § 123 VwGO und besondere KDVG-Fristen.

## Fachlicher Kern
Prüft vorläufige Regelung ohne passenden §80-Fall. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

## Sofortfragen
1. Welche Personengruppe liegt vor: ungedient, wehrpflichtig, FWDL, SaZ, Berufssoldat, Reservist, frühere Soldatin/früherer Soldat oder Sonderfall?
2. Gibt es bereits Antrag, Eingangsbestätigung, Personenkennziffer, Musterungsbescheid, BAFzA-Schreiben, Anhörung oder Bescheid?
3. Geht es um Kriegsdienst mit der Waffe als Gewissensproblem oder um Politik, Gesundheit, Angst, Karriere, Familie oder Totalverweigerung?
4. Welche Frist läuft und welcher Nachweis liegt für Zugang oder Bekanntgabe vor?

## Arbeitsgang
1. Status und anwendbare Normen festlegen.
2. Pflichtunterlagen und fehlende Dokumente markieren.
3. Gewissenskern von bloßen Randmotiven trennen.
4. Behördenweg BAPersBw -> BAFzA oder Soldaten-/Reservistenpfad bestimmen.
5. Output knapp, würdig und nachweisbar formulieren.

## Norm- und Quellenanker
VwGO § 123

## Output
- Statusampel.
- Unterlagen- und Fristenliste.
- nächster Schriftsatz oder nächste Verfahrenshandlung.
- Warnhinweis, falls der Fall in Totalverweigerung, bloße Politik oder Disziplinarrisiko kippt.

## Rote Linien
Fristen, Zustellung und Dokumenttyp prüfen, bevor Widerspruch, Klage oder Eilantrag vorgeschlagen werden.

## Anschluss-Skills
- `kriegsdienstverweigerung-wehrdienst-allgemein` für Kaltstart und Routing.
- `qualitaetsgate-vor-ausgabe` vor belastbarer Ausgabe.
- `rechtsprechung-livecheck` bei Gerichtsargumentation.

## Quellen- und Aktualitätsregel
- Aktuelle Fassung von GG, KDVG, WPflG, SG und VwGO in amtlichen Quellen prüfen.
- BAFzA-Hinweise zum Antragsweg, zur hohen Antragslast und zu § 13 KDVG n. F. berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Link nennen.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.
