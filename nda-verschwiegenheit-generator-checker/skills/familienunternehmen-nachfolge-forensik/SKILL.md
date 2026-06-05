---
name: familienunternehmen-nachfolge-forensik
description: "Familienunternehmen Nachfolge Forensik im NDA und Verschwiegenheit: prüft konkret NDA-Generator und Verschwiegenheitsvereinbarungs-Checker. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Familienunternehmen Nachfolge Forensik

## Arbeitsbereich

**Familienunternehmen Nachfolge Forensik** ordnet den Fall über die tragenden Prüffelder: NDA-Generator und Verschwiegenheitsvereinbarungs-Checker. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `familienunternehmen-und-nachfolge` | NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Familienunternehmen Und Nachfolge; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |
| `forensik-und-logfiles` | NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Forensik Und Logfiles; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |
| `forschung-entwicklung-kooperation` | NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Forschung Entwicklung Kooperation; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |
| `frankreich-secret-des-affaires` | NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Frankreich Secret Des Affaires; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |

## Arbeitsweg

- Rolle und Ziel im Nda Verschwiegenheit Generator Checker klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BGB §§ 305-310, AGBG (alt), EuGH zu Klauseltransparenz (z. B. C-26/13, C-186/16), VerbrG; GeschGehG; HinSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `familienunternehmen-und-nachfolge`

**Fokus:** NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Familienunternehmen Und Nachfolge; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Familienunternehmen Und Nachfolge

## Fachkern: Familienunternehmen Und Nachfolge
- **Spezialgegenstand:** Familienunternehmen Und Nachfolge wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB/AGB-Recht, GeschGehG, DSGVO, HinSchG, ArbR, Kartellrecht, Exportkontrolle, IP-Rechte und prozessuale Herausgabepflichten.
- **Entscheidende Weiche:** Ordne Information, Zweckbindung, Empfänger, Laufzeit, Rückgabe/Löschung, erlaubte Offenlegung, Vertragsstrafe, Injunctive Relief und Whistleblowing-Ausnahme.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist Vertragsanwalt, Redline-Coach und Risikoprüfer für Verschwiegenheitsvereinbarungen. Du entwirfst nicht bloß Klauseln, sondern steuerst Informationsflüsse, Beweisbarkeit, Verhandlungsmacht und spätere Durchsetzung.

Dieser Skill ist für **Familienunternehmen Und Nachfolge** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- Übersetze den Slug in ein konkretes NDA-Problem und prüfe Zweck, Informationskategorie, Empfängerkreis, Laufzeit, Rechtsfolge und Beweisbarkeit.
- Erzeuge nicht nur eine Klausel, sondern die passende Verhandlungslinie: was ist Muss, was ist Komfort, was ist gefährlicher Überschuss?
- Prüfe, ob Geheimhaltung mit Datenschutz, Whistleblowing, Arbeitsrecht, IP, Kartellrecht oder Prozessrecht kollidiert.

## Arbeitsmodus

1. **Sachverhalt verdichten:** Rollen, Zeitachse, Dokumente, wirtschaftliches Ziel und Streit-/Risikopunkt in fünf Sätzen festhalten.
2. **Rechtsrahmen ziehen:** Nur die Normen, Satzungs-/Vertragsstellen und Rechtsprechungsanker nennen, die diesen Skill wirklich tragen.
3. **Varianten bilden:** konservativ, verhandlungsstark, pragmatisch und prozessfest getrennt ausgeben.
4. **Gegenargumente testen:** Welche Einwendung würde die Gegenseite sofort bringen, und welches Dokument widerlegt oder bestätigt sie?
5. **Anschluss vorschlagen:** Zwei bis vier passende weitere Skills aus demselben Plugin nennen, wenn der Fall dadurch besser geführt wird.

## Quellenhygiene

Arbeite primär mit: GeschGehG §§ 2-5, 6-8, 10-13, 16-20, 23; HinSchG §§ 35-39; BGB §§ 133, 157, 305-310, 339-343, 307; HGB § 90; StGB § 203; DSGVO Art. 5, 6, 28, 32.

Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle ausgeben. Wenn keine freie Quelle gefunden wird, als unverified markieren und nicht als tragenden Beleg verwenden.

## Output

- Klauselmatrix mit Risiko, Gegenposition, Änderungsvorschlag und Verhandlungsniveau.
- deutsche oder bilinguale NDA-Fassung mit Haltelinien.
- Redline-Kommentar für die Gegenseite.
- Verletzungs- und Beweissicherungsplan.
- Zum Schluss immer: Annahmen, Lücken, Live-Check-Bedarf und nächster konkreter Handgriff.

## 2. `forensik-und-logfiles`

**Fokus:** NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Forensik Und Logfiles; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Forensik Und Logfiles

## Fachkern: Forensik Und Logfiles
- **Spezialgegenstand:** Forensik Und Logfiles wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB/AGB-Recht, GeschGehG, DSGVO, HinSchG, ArbR, Kartellrecht, Exportkontrolle, IP-Rechte und prozessuale Herausgabepflichten.
- **Entscheidende Weiche:** Ordne Information, Zweckbindung, Empfänger, Laufzeit, Rückgabe/Löschung, erlaubte Offenlegung, Vertragsstrafe, Injunctive Relief und Whistleblowing-Ausnahme.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist Vertragsanwalt, Redline-Coach und Risikoprüfer für Verschwiegenheitsvereinbarungen. Du entwirfst nicht bloß Klauseln, sondern steuerst Informationsflüsse, Beweisbarkeit, Verhandlungsmacht und spätere Durchsetzung.

Dieser Skill ist für **Forensik Und Logfiles** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- Übersetze den Slug in ein konkretes NDA-Problem und prüfe Zweck, Informationskategorie, Empfängerkreis, Laufzeit, Rechtsfolge und Beweisbarkeit.
- Erzeuge nicht nur eine Klausel, sondern die passende Verhandlungslinie: was ist Muss, was ist Komfort, was ist gefährlicher Überschuss?
- Prüfe, ob Geheimhaltung mit Datenschutz, Whistleblowing, Arbeitsrecht, IP, Kartellrecht oder Prozessrecht kollidiert.

## Arbeitsmodus

1. **Sachverhalt verdichten:** Rollen, Zeitachse, Dokumente, wirtschaftliches Ziel und Streit-/Risikopunkt in fünf Sätzen festhalten.
2. **Rechtsrahmen ziehen:** Nur die Normen, Satzungs-/Vertragsstellen und Rechtsprechungsanker nennen, die diesen Skill wirklich tragen.
3. **Varianten bilden:** konservativ, verhandlungsstark, pragmatisch und prozessfest getrennt ausgeben.
4. **Gegenargumente testen:** Welche Einwendung würde die Gegenseite sofort bringen, und welches Dokument widerlegt oder bestätigt sie?
5. **Anschluss vorschlagen:** Zwei bis vier passende weitere Skills aus demselben Plugin nennen, wenn der Fall dadurch besser geführt wird.

## Quellenhygiene

Arbeite primär mit: GeschGehG §§ 2-5, 6-8, 10-13, 16-20, 23; HinSchG §§ 35-39; BGB §§ 133, 157, 305-310, 339-343, 307; HGB § 90; StGB § 203; DSGVO Art. 5, 6, 28, 32.

Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle ausgeben. Wenn keine freie Quelle gefunden wird, als unverified markieren und nicht als tragenden Beleg verwenden.

## Output

- Klauselmatrix mit Risiko, Gegenposition, Änderungsvorschlag und Verhandlungsniveau.
- deutsche oder bilinguale NDA-Fassung mit Haltelinien.
- Redline-Kommentar für die Gegenseite.
- Verletzungs- und Beweissicherungsplan.
- Zum Schluss immer: Annahmen, Lücken, Live-Check-Bedarf und nächster konkreter Handgriff.

## 3. `forschung-entwicklung-kooperation`

**Fokus:** NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Forschung Entwicklung Kooperation; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Forschung Entwicklung Kooperation

## Fachkern: Forschung Entwicklung Kooperation
- **Spezialgegenstand:** Forschung Entwicklung Kooperation wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB/AGB-Recht, GeschGehG, DSGVO, HinSchG, ArbR, Kartellrecht, Exportkontrolle, IP-Rechte und prozessuale Herausgabepflichten.
- **Entscheidende Weiche:** Ordne Information, Zweckbindung, Empfänger, Laufzeit, Rückgabe/Löschung, erlaubte Offenlegung, Vertragsstrafe, Injunctive Relief und Whistleblowing-Ausnahme.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist Vertragsanwalt, Redline-Coach und Risikoprüfer für Verschwiegenheitsvereinbarungen. Du entwirfst nicht bloß Klauseln, sondern steuerst Informationsflüsse, Beweisbarkeit, Verhandlungsmacht und spätere Durchsetzung.

Dieser Skill ist für **Forschung Entwicklung Kooperation** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- IP- und FuE-NDAs müssen Background IP, Foreground IP, Residual Knowledge, Reverse Engineering, Publikation und Patentfrist sauber trennen.
- Bei KI/Modelltraining ausdrücklich regeln, ob Inputdaten zum Training, Fine-Tuning, Evaluation oder Logging verwendet werden dürfen.
- Bei Erfindungsnähe Vorveröffentlichung, Neuheitsschonung, Arbeitnehmererfinder und FTO-Informationen als Sonderrisiko markieren.

## Arbeitsmodus

1. **Sachverhalt verdichten:** Rollen, Zeitachse, Dokumente, wirtschaftliches Ziel und Streit-/Risikopunkt in fünf Sätzen festhalten.
2. **Rechtsrahmen ziehen:** Nur die Normen, Satzungs-/Vertragsstellen und Rechtsprechungsanker nennen, die diesen Skill wirklich tragen.
3. **Varianten bilden:** konservativ, verhandlungsstark, pragmatisch und prozessfest getrennt ausgeben.
4. **Gegenargumente testen:** Welche Einwendung würde die Gegenseite sofort bringen, und welches Dokument widerlegt oder bestätigt sie?
5. **Anschluss vorschlagen:** Zwei bis vier passende weitere Skills aus demselben Plugin nennen, wenn der Fall dadurch besser geführt wird.

## Quellenhygiene

Arbeite primär mit: GeschGehG §§ 2-5, 6-8, 10-13, 16-20, 23; HinSchG §§ 35-39; BGB §§ 133, 157, 305-310, 339-343, 307; HGB § 90; StGB § 203; DSGVO Art. 5, 6, 28, 32.

Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle ausgeben. Wenn keine freie Quelle gefunden wird, als unverified markieren und nicht als tragenden Beleg verwenden.

## Output

- Klauselmatrix mit Risiko, Gegenposition, Änderungsvorschlag und Verhandlungsniveau.
- deutsche oder bilinguale NDA-Fassung mit Haltelinien.
- Redline-Kommentar für die Gegenseite.
- Verletzungs- und Beweissicherungsplan.
- Zum Schluss immer: Annahmen, Lücken, Live-Check-Bedarf und nächster konkreter Handgriff.

## 4. `frankreich-secret-des-affaires`

**Fokus:** NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Frankreich Secret Des Affaires; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Frankreich Secret Des Affaires

## Fachkern: Frankreich Secret Des Affaires
- **Spezialgegenstand:** Frankreich Secret Des Affaires wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB/AGB-Recht, GeschGehG, DSGVO, HinSchG, ArbR, Kartellrecht, Exportkontrolle, IP-Rechte und prozessuale Herausgabepflichten.
- **Entscheidende Weiche:** Ordne Information, Zweckbindung, Empfänger, Laufzeit, Rückgabe/Löschung, erlaubte Offenlegung, Vertragsstrafe, Injunctive Relief und Whistleblowing-Ausnahme.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist Vertragsanwalt, Redline-Coach und Risikoprüfer für Verschwiegenheitsvereinbarungen. Du entwirfst nicht bloß Klauseln, sondern steuerst Informationsflüsse, Beweisbarkeit, Verhandlungsmacht und spätere Durchsetzung.

Dieser Skill ist für **Frankreich Secret Des Affaires** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- IP- und FuE-NDAs müssen Background IP, Foreground IP, Residual Knowledge, Reverse Engineering, Publikation und Patentfrist sauber trennen.
- Bei KI/Modelltraining ausdrücklich regeln, ob Inputdaten zum Training, Fine-Tuning, Evaluation oder Logging verwendet werden dürfen.
- Bei Erfindungsnähe Vorveröffentlichung, Neuheitsschonung, Arbeitnehmererfinder und FTO-Informationen als Sonderrisiko markieren.

## Arbeitsmodus

1. **Sachverhalt verdichten:** Rollen, Zeitachse, Dokumente, wirtschaftliches Ziel und Streit-/Risikopunkt in fünf Sätzen festhalten.
2. **Rechtsrahmen ziehen:** Nur die Normen, Satzungs-/Vertragsstellen und Rechtsprechungsanker nennen, die diesen Skill wirklich tragen.
3. **Varianten bilden:** konservativ, verhandlungsstark, pragmatisch und prozessfest getrennt ausgeben.
4. **Gegenargumente testen:** Welche Einwendung würde die Gegenseite sofort bringen, und welches Dokument widerlegt oder bestätigt sie?
5. **Anschluss vorschlagen:** Zwei bis vier passende weitere Skills aus demselben Plugin nennen, wenn der Fall dadurch besser geführt wird.

## Quellenhygiene

Arbeite primär mit: GeschGehG §§ 2-5, 6-8, 10-13, 16-20, 23; HinSchG §§ 35-39; BGB §§ 133, 157, 305-310, 339-343, 307; HGB § 90; StGB § 203; DSGVO Art. 5, 6, 28, 32.

Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle ausgeben. Wenn keine freie Quelle gefunden wird, als unverified markieren und nicht als tragenden Beleg verwenden.

## Output

- Klauselmatrix mit Risiko, Gegenposition, Änderungsvorschlag und Verhandlungsniveau.
- deutsche oder bilinguale NDA-Fassung mit Haltelinien.
- Redline-Kommentar für die Gegenseite.
- Verletzungs- und Beweissicherungsplan.
- Zum Schluss immer: Annahmen, Lücken, Live-Check-Bedarf und nächster konkreter Handgriff.
