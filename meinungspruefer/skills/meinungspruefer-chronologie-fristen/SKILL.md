---
name: meinungspruefer-chronologie-fristen
description: "Chronologie Fristen im Plugin Meinungspruefer: prüft konkret Chronologie und Belegmatrix im Plugin meinungspruefer, Fristen- und Risikoampel im Plugin meinungspruefer. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Chronologie Fristen

## Arbeitsbereich

Dieser Skill behandelt **Chronologie Fristen** als zusammenhängenden Arbeitsgang im Plugin Meinungspruefer. Im Mittelpunkt steht die Prüfung von Chronologie und Belegmatrix im Plugin meinungspruefer, Fristen- und Risikoampel im Plugin meinungspruefer. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin meinungspruefer: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin meinungspruefer: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |

## Arbeitsweg

- Rolle und Ziel im Meinungsprüfer für Äußerungsrecht: Meinung oder Tatsache, Beleidigung, üble Nachrede, Verleumdung, § 188 StGB, Art klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 188 StGB, Art. 5 GG, Art. 10 EMRK, Art. 11 GRCh, EGMR — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `workflow-chronologie-und-belegmatrix`

**Fokus:** Chronologie und Belegmatrix im Plugin meinungspruefer: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen.

# Chronologie und Belegmatrix

## Aufgabe
Dieser Prüffeld baut zu einer streitigen Äußerung eine vollständige Chronologie und Belegmatrix: Veröffentlichung, Reichweite, Reaktionen, Kenntniserlangung des Betroffenen, anwaltliche Schritte, Plattform-Meldungen.

## Pflicht-Daten Äußerungsrecht
- **Erstveröffentlichung:** Datum, Uhrzeit, Plattform, URL, Verfasser, Reichweite (Followerzahl, Reach).
- **Folge-/Spiegelveröffentlichungen:** Retweets, Shares, Crossposts, Presseübernahme -- jede zählt eigenständig (sog. "Hop-Doktrin"; jedes Verbreiten eigener Anspruch).
- **Erstveröffentlichung-Backup:** Wayback Machine, Archive.today, eigene Screenshots mit Datum/Uhrzeit-Stempel.
- **Kenntniserlangung Betroffener** (für Eilfristen Verfügungsgrund): wann wurde Betroffener informiert?
- **Plattform-Meldung (DSA Art. 16):** Datum, Inhalts-URL, Meldungstext, Plattform-Antwort.
- **Außergerichtliche Aufforderung:** Datum Abmahnung, Frist, Antwort.
- **Gerichtliche Schritte:** Antrag eV, Verfügungsbeschluss, Termin.

## Belegmatrix
- Datum | Ereignis | URL/Quelle | Screenshots | Norm-Anker (Art. 5 GG; § 823 BGB; §§ 185 ff. StGB) | Folge / Frist | offene Frage.

## Eilfristen-Hinweis
- Verfügungsgrund regelmäßig nur ca. 4 Wochen ab Kenntnis (Selbstwiderlegungsdoktrin; OLG-spezifisch prüfen). Frist beginnt mit positiver Kenntnis, nicht bei bloßer Möglichkeit der Kenntnis.

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

## 2. `workflow-fristen-und-risikoampel`

**Fokus:** Fristen- und Risikoampel im Plugin meinungspruefer: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.

# Fristen- und Risikoampel

## Aufgabe
Dieser Prüffeld markiert in äußerungsrechtlichen Mandaten typische Fristen und Eskalationsrisiken: Eilantrag auf Unterlassung, Gegendarstellung, DSA/Plattform-Beschwerde, presserechtliche Auseinandersetzung.

## Äußerungsrechtliche Fristen
- **Einstweilige Verfügung (§§ 935 ff., 940 ZPO):** Verfügungsgrund regelmäßig nur ca. 4 Wochen nach Kenntnis (Selbstwiderlegungsdoktrin der OLG; siehe LG/OLG Köln-/Hamburger-Linie; bitte aktuelle OLG-Rechtsprechung prüfen).
- **Gegendarstellung:** unverzüglich, idR binnen 14 Tagen, spätestens drei Monate nach Veröffentlichung (so etwa § 11 HmbPresseG; Landespressegesetze unterschiedlich -- aktuell prüfen!).
- **DSA-Beschwerde (Art. 16 DSA, VO (EU) 2022/2065):** keine starre Frist, aber Plattform muss zeitnah ohne ungebührliche Verzögerung entscheiden.
- **Verjährung Schadensersatz/Geldentschädigung:** § 195 BGB drei Jahre ab Kenntnis (§ 199 BGB).
- **Straftatbestände §§ 185-187 StGB:** Strafantrag § 194 StGB binnen drei Monaten ab Kenntnis (§ 77b StGB).

## Risikoampel-Logik
- **Rot:** Eilrisiko (Fristverlust für eV), strafrechtliche Anzeige droht, Reichweitenexplosion.
- **Gelb:** Schadensersatzansprüche im Raum, aber noch keine Fristen am Auslaufen.
- **Grün:** Klärung mit Plattform/Verlag im Dialog, keine akute Frist.

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
