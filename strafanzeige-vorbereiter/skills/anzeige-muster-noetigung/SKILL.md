---
name: anzeige-muster-noetigung
description: "Anzeige Muster Noetigung im Strafanzeigen-Vorbereitung: prüft konkret Erzeugt eine nüchterne Strafanzeige mit optionalem, Anlagen, Beweism, Nötigung prüfen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Anzeige Muster Noetigung

## Arbeitsbereich

**Anzeige Muster Noetigung** ordnet den Fall über die tragenden Prüffelder: Erzeugt eine nüchterne Strafanzeige mit optionalem, Anlagen, Beweism. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anzeige-muster-strafanzeige-generator` | Erzeugt eine nüchterne Strafanzeige mit optionalem Strafantrag, Anlagen, Beweismatrix und Risikoformulierungen. |
| `anzeige-noetigung-240` | Nötigung prüfen: Gewalt/Drohung, empfindliches Übel, Verwerflichkeit, legitime Anzeigeandrohung vs. Missbrauch. |

## Arbeitsweg

- Rolle und Ziel im Strafanzeige Vorbereiter klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `anzeige-muster-strafanzeige-generator`

**Fokus:** Erzeugt eine nüchterne Strafanzeige mit optionalem Strafantrag, Anlagen, Beweismatrix und Risikoformulierungen.

# Muster-Strafanzeige Generator

## Einsatz

Für Fälle, die nach Red-Team wirklich angezeigt werden sollen.

## Norm- und Quellenanker

StPO § 158; StGB § 77b; betroffene Straftatbestände.

## Arbeitsfragen

1. Welche Tatbestände nur als Verdacht?
2. Welche Anlagen?
3. Welche Ermittlungsanregungen?

## Output

fertiger Anzeigeentwurf.

## Red Flags

- Täter sicher behauptet ohne Beweis
- Antrag vergessen
- Anlagen fehlen

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 2. `anzeige-noetigung-240`

**Fokus:** Nötigung prüfen: Gewalt/Drohung, empfindliches Übel, Verwerflichkeit, legitime Anzeigeandrohung vs. Missbrauch.

# Nötigung § 240 StGB

## Einsatz

Für Drucksituationen.

## Norm- und Quellenanker

StGB § 240; BGB/Arbeitsrecht als Kontext.

## Arbeitsfragen

1. Welches Mittel?
2. Welcher Zweck?
3. Warum verwerflich?

## Output

Nötigungsprüfung und Anzeigeentwurf.

## Red Flags

- jede harte Verhandlung als Nötigung
- legitime Rechtsverfolgung verkannt
- Mittel-Zweck fehlt

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.
