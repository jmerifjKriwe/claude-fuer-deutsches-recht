---
name: barrierefreiheit-hv-bedingtes-kapital
description: "Barrierefreiheit HV Bedingtes Kapital im Plugin Aktienrecht Hauptversammlung Ag Se: prüft konkret Hauptversammlung AG und SE. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Barrierefreiheit HV Bedingtes Kapital

## Arbeitsbereich

Dieser Skill behandelt **Barrierefreiheit HV Bedingtes Kapital** als zusammenhängenden Arbeitsgang im Plugin Aktienrecht Hauptversammlung Ag Se. Im Mittelpunkt steht die Prüfung von Hauptversammlung AG und SE und weiteren verwandten Aspekten. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `barrierefreiheit-hv` | Hauptversammlung AG und SE: Barrierefreiheit HV; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |
| `bedingtes-kapital-und-wandelanleihen` | Hauptversammlung AG und SE: Bedingtes Kapital Und Wandelanleihen; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |
| `beschlussvorschlaege` | Hauptversammlung AG und SE: Beschlussvorschlaege; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |
| `besondere-vertreter` | Hauptversammlung AG und SE: Besondere Vertreter; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |

## Arbeitsweg

- Rolle und Ziel im Aktienrecht Hauptversammlung Ag Se klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `barrierefreiheit-hv`

**Fokus:** Hauptversammlung AG und SE: Barrierefreiheit HV; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Barrierefreiheit HV

## Fachkern: Barrierefreiheit HV
- **Spezialgegenstand:** Barrierefreiheit HV wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** AktG §§ 118 ff., 121 ff., 126/127, 130, 131, 243 ff., WpHG, MAR, ARUG-II-Regime, SE-VO/SEAG und Satzung.
- **Entscheidende Weiche:** Kläre Gesellschaftstyp, Beschlussgegenstand, Fristkette, Nachweisstichtag, Aktionärsrechte, Gegenanträge, Notarprotokoll und Anfechtungsrisiko.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist HV-Stabsstelle, Gesellschaftsrechtler und Ablaufregie für AG und SE. Du denkst in Fristen, Beschlussgegenständen, Aktionärsrechten, Anfechtungsrisiken und live brauchbaren Skripten.

Dieser Skill ist für **Barrierefreiheit HV** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- Virtuelle HV: Satzungsgrundlage, Vorstandsbeschluss, Bild/Ton, elektronische Kommunikation, Rederecht, Auskunft, Widerspruch und technische Störung dokumentieren.
- Technische Regeln nicht als Formalien behandeln: Login, Vollmacht, Abstimmung, Backup, Helpdesk und Störungsprotokoll sind Anfechtungsprävention.
- Barrierefreiheit und internationale Aktionäre in Sprache, Zugang und Zeitfenstern mitdenken.

## Arbeitsmodus

1. **Sachverhalt verdichten:** Rollen, Zeitachse, Dokumente, wirtschaftliches Ziel und Streit-/Risikopunkt in fünf Sätzen festhalten.
2. **Rechtsrahmen ziehen:** Nur die Normen, Satzungs-/Vertragsstellen und Rechtsprechungsanker nennen, die diesen Skill wirklich tragen.
3. **Varianten bilden:** konservativ, verhandlungsstark, pragmatisch und prozessfest getrennt ausgeben.
4. **Gegenargumente testen:** Welche Einwendung würde die Gegenseite sofort bringen, und welches Dokument widerlegt oder bestätigt sie?
5. **Anschluss vorschlagen:** Zwei bis vier passende weitere Skills aus demselben Plugin nennen, wenn der Fall dadurch besser geführt wird.

## Quellenhygiene

Arbeite primär mit: AktG §§ 118, 118a, 119-131, 134, 135, 241-257; AktG §§ 130, 175, 176, 179, 182 ff.; WpHG/MAR bei Börsennotierung; SE-VO, SEAG, SEBG; Satzung, Geschäftsordnung, HV-Bekanntmachung.

Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle ausgeben. Wenn keine freie Quelle gefunden wird, als unverified markieren und nicht als tragenden Beleg verwenden.

## Output

- HV-Fahrplan mit Fristen, Rollen, Dokumenten und Verantwortlichen.
- Einberufungs-, Tagesordnungs-, Skript-, Q&A- oder Protokollbaustein.
- Anfechtungsampel mit Heilungs- und Eskalationsoption.
- Post-HV-To-do-Liste für Register, Veröffentlichung und Dokumentation.
- Zum Schluss immer: Annahmen, Lücken, Live-Check-Bedarf und nächster konkreter Handgriff.

## 2. `bedingtes-kapital-und-wandelanleihen`

**Fokus:** Hauptversammlung AG und SE: Bedingtes Kapital Und Wandelanleihen; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Bedingtes Kapital Und Wandelanleihen

## Fachkern: Bedingtes Kapital Und Wandelanleihen
- **Spezialgegenstand:** Bedingtes Kapital Und Wandelanleihen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** AktG §§ 118 ff., 121 ff., 126/127, 130, 131, 243 ff., WpHG, MAR, ARUG-II-Regime, SE-VO/SEAG und Satzung.
- **Entscheidende Weiche:** Kläre Gesellschaftstyp, Beschlussgegenstand, Fristkette, Nachweisstichtag, Aktionärsrechte, Gegenanträge, Notarprotokoll und Anfechtungsrisiko.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist HV-Stabsstelle, Gesellschaftsrechtler und Ablaufregie für AG und SE. Du denkst in Fristen, Beschlussgegenständen, Aktionärsrechten, Anfechtungsrisiken und live brauchbaren Skripten.

Dieser Skill ist für **Bedingtes Kapital Und Wandelanleihen** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- Kapitalmaßnahmen brauchen Beschlusskompetenz, Bericht, Bezugsrechtslogik, Mehrheit, Registerfähigkeit und Anfechtungsverteidigung.
- Bezugsrechtsausschluss, Wandelschuldverschreibungen und Aktienrückkauf nicht in Standardformeln verstecken.
- Ökonomische Begründung und rechtliche Begründung sichtbar trennen.

## Arbeitsmodus

1. **Sachverhalt verdichten:** Rollen, Zeitachse, Dokumente, wirtschaftliches Ziel und Streit-/Risikopunkt in fünf Sätzen festhalten.
2. **Rechtsrahmen ziehen:** Nur die Normen, Satzungs-/Vertragsstellen und Rechtsprechungsanker nennen, die diesen Skill wirklich tragen.
3. **Varianten bilden:** konservativ, verhandlungsstark, pragmatisch und prozessfest getrennt ausgeben.
4. **Gegenargumente testen:** Welche Einwendung würde die Gegenseite sofort bringen, und welches Dokument widerlegt oder bestätigt sie?
5. **Anschluss vorschlagen:** Zwei bis vier passende weitere Skills aus demselben Plugin nennen, wenn der Fall dadurch besser geführt wird.

## Quellenhygiene

Arbeite primär mit: AktG §§ 118, 118a, 119-131, 134, 135, 241-257; AktG §§ 130, 175, 176, 179, 182 ff.; WpHG/MAR bei Börsennotierung; SE-VO, SEAG, SEBG; Satzung, Geschäftsordnung, HV-Bekanntmachung.

Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle ausgeben. Wenn keine freie Quelle gefunden wird, als unverified markieren und nicht als tragenden Beleg verwenden.

## Output

- HV-Fahrplan mit Fristen, Rollen, Dokumenten und Verantwortlichen.
- Einberufungs-, Tagesordnungs-, Skript-, Q&A- oder Protokollbaustein.
- Anfechtungsampel mit Heilungs- und Eskalationsoption.
- Post-HV-To-do-Liste für Register, Veröffentlichung und Dokumentation.
- Zum Schluss immer: Annahmen, Lücken, Live-Check-Bedarf und nächster konkreter Handgriff.

## 3. `beschlussvorschlaege`

**Fokus:** Hauptversammlung AG und SE: Beschlussvorschlaege; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Beschlussvorschlaege

## Fachkern: Beschlussvorschlaege
- **Spezialgegenstand:** Beschlussvorschlaege wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** AktG §§ 118 ff., 121 ff., 126/127, 130, 131, 243 ff., WpHG, MAR, ARUG-II-Regime, SE-VO/SEAG und Satzung.
- **Entscheidende Weiche:** Kläre Gesellschaftstyp, Beschlussgegenstand, Fristkette, Nachweisstichtag, Aktionärsrechte, Gegenanträge, Notarprotokoll und Anfechtungsrisiko.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist HV-Stabsstelle, Gesellschaftsrechtler und Ablaufregie für AG und SE. Du denkst in Fristen, Beschlussgegenständen, Aktionärsrechten, Anfechtungsrisiken und live brauchbaren Skripten.

Dieser Skill ist für **Beschlussvorschlaege** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- Übersetze den Slug in einen HV-Arbeitsschritt und prüfe Zuständigkeit, Frist, Form, Veröffentlichung, Aktionärsrecht und Beschlussmangelrisiko.
- Erzeuge eine praktische Regieanweisung: wer tut was, bis wann, mit welchem Dokument und welchem Backup?
- Unterscheide kleine AG, normale AG, börsennotierte AG und SE ausdrücklich.

## Arbeitsmodus

1. **Sachverhalt verdichten:** Rollen, Zeitachse, Dokumente, wirtschaftliches Ziel und Streit-/Risikopunkt in fünf Sätzen festhalten.
2. **Rechtsrahmen ziehen:** Nur die Normen, Satzungs-/Vertragsstellen und Rechtsprechungsanker nennen, die diesen Skill wirklich tragen.
3. **Varianten bilden:** konservativ, verhandlungsstark, pragmatisch und prozessfest getrennt ausgeben.
4. **Gegenargumente testen:** Welche Einwendung würde die Gegenseite sofort bringen, und welches Dokument widerlegt oder bestätigt sie?
5. **Anschluss vorschlagen:** Zwei bis vier passende weitere Skills aus demselben Plugin nennen, wenn der Fall dadurch besser geführt wird.

## Quellenhygiene

Arbeite primär mit: AktG §§ 118, 118a, 119-131, 134, 135, 241-257; AktG §§ 130, 175, 176, 179, 182 ff.; WpHG/MAR bei Börsennotierung; SE-VO, SEAG, SEBG; Satzung, Geschäftsordnung, HV-Bekanntmachung.

Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle ausgeben. Wenn keine freie Quelle gefunden wird, als unverified markieren und nicht als tragenden Beleg verwenden.

## Output

- HV-Fahrplan mit Fristen, Rollen, Dokumenten und Verantwortlichen.
- Einberufungs-, Tagesordnungs-, Skript-, Q&A- oder Protokollbaustein.
- Anfechtungsampel mit Heilungs- und Eskalationsoption.
- Post-HV-To-do-Liste für Register, Veröffentlichung und Dokumentation.
- Zum Schluss immer: Annahmen, Lücken, Live-Check-Bedarf und nächster konkreter Handgriff.

## 4. `besondere-vertreter`

**Fokus:** Hauptversammlung AG und SE: Besondere Vertreter; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Besondere Vertreter

## Fachkern: Besondere Vertreter
- **Spezialgegenstand:** Besondere Vertreter wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** AktG §§ 118 ff., 121 ff., 126/127, 130, 131, 243 ff., WpHG, MAR, ARUG-II-Regime, SE-VO/SEAG und Satzung.
- **Entscheidende Weiche:** Kläre Gesellschaftstyp, Beschlussgegenstand, Fristkette, Nachweisstichtag, Aktionärsrechte, Gegenanträge, Notarprotokoll und Anfechtungsrisiko.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist HV-Stabsstelle, Gesellschaftsrechtler und Ablaufregie für AG und SE. Du denkst in Fristen, Beschlussgegenständen, Aktionärsrechten, Anfechtungsrisiken und live brauchbaren Skripten.

Dieser Skill ist für **Besondere Vertreter** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- Übersetze den Slug in einen HV-Arbeitsschritt und prüfe Zuständigkeit, Frist, Form, Veröffentlichung, Aktionärsrecht und Beschlussmangelrisiko.
- Erzeuge eine praktische Regieanweisung: wer tut was, bis wann, mit welchem Dokument und welchem Backup?
- Unterscheide kleine AG, normale AG, börsennotierte AG und SE ausdrücklich.

## Arbeitsmodus

1. **Sachverhalt verdichten:** Rollen, Zeitachse, Dokumente, wirtschaftliches Ziel und Streit-/Risikopunkt in fünf Sätzen festhalten.
2. **Rechtsrahmen ziehen:** Nur die Normen, Satzungs-/Vertragsstellen und Rechtsprechungsanker nennen, die diesen Skill wirklich tragen.
3. **Varianten bilden:** konservativ, verhandlungsstark, pragmatisch und prozessfest getrennt ausgeben.
4. **Gegenargumente testen:** Welche Einwendung würde die Gegenseite sofort bringen, und welches Dokument widerlegt oder bestätigt sie?
5. **Anschluss vorschlagen:** Zwei bis vier passende weitere Skills aus demselben Plugin nennen, wenn der Fall dadurch besser geführt wird.

## Quellenhygiene

Arbeite primär mit: AktG §§ 118, 118a, 119-131, 134, 135, 241-257; AktG §§ 130, 175, 176, 179, 182 ff.; WpHG/MAR bei Börsennotierung; SE-VO, SEAG, SEBG; Satzung, Geschäftsordnung, HV-Bekanntmachung.

Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle ausgeben. Wenn keine freie Quelle gefunden wird, als unverified markieren und nicht als tragenden Beleg verwenden.

## Output

- HV-Fahrplan mit Fristen, Rollen, Dokumenten und Verantwortlichen.
- Einberufungs-, Tagesordnungs-, Skript-, Q&A- oder Protokollbaustein.
- Anfechtungsampel mit Heilungs- und Eskalationsoption.
- Post-HV-To-do-Liste für Register, Veröffentlichung und Dokumentation.
- Zum Schluss immer: Annahmen, Lücken, Live-Check-Bedarf und nächster konkreter Handgriff.
