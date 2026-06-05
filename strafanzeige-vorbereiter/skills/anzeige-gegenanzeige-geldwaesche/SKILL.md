---
name: anzeige-gegenanzeige-geldwaesche
description: "Anzeige Gegenanzeige Geldwaesche im Strafanzeigen-Vorbereitung: prüft konkret Risiko der Gegenanzeige wegen falscher Verdächtigung, Verleumdung, Nötigung, Dat. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Anzeige Gegenanzeige Geldwaesche

## Arbeitsbereich

Dieser Skill behandelt **Anzeige Gegenanzeige Geldwaesche** als zusammenhängenden Arbeitsgang im Strafanzeigen-Vorbereitung. Im Mittelpunkt steht die Prüfung von Risiko der Gegenanzeige wegen falscher Verdächtigung, Verleumdung, Nötigung. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anzeige-gegenanzeige-risiko` | Risiko der Gegenanzeige wegen falscher Verdächtigung, Verleumdung, Nötigung, Datenschutzverstoß oder Prozessbetrug. |
| `anzeige-geldwaesche-261` | Geldwäscheverdacht: Tatertrag, Verschleierung, Transaktionen, GwG-Verdachtsmeldung vs Strafanzeige. |

## Arbeitsweg

- Rolle und Ziel im Strafanzeige Vorbereiter klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `anzeige-gegenanzeige-risiko`

**Fokus:** Risiko der Gegenanzeige wegen falscher Verdächtigung, Verleumdung, Nötigung, Datenschutzverstoß oder Prozessbetrug.

# Gegenanzeige-Risiko

## Einsatz

Für konfliktgeladene Anzeigen.

## Norm- und Quellenanker

StGB §§ 164, 186, 187, 240, 263; DSGVO.

## Arbeitsfragen

1. Welche Gegenbehauptungen zu erwarten?
2. Welche eigene Schwachstelle?
3. Welche Formulierung minimiert Risiko?

## Output

Gegenanzeigen-Risikovermerk.

## Red Flags

- eigene Rolle verschwiegen
- Beweise manipuliert
- Dritte diffamiert

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 2. `anzeige-geldwaesche-261`

**Fokus:** Geldwäscheverdacht: Tatertrag, Verschleierung, Transaktionen, GwG-Verdachtsmeldung vs Strafanzeige.

# Geldwäsche § 261 StGB

## Einsatz

Für Unternehmen mit verdächtigen Zahlungsflüssen.

## Norm- und Quellenanker

StGB § 261; GwG; FIU/goAML; StPO.

## Arbeitsfragen

1. Welche Vortat/Quelle?
2. Welche Transaktion?
3. Besteht GwG-Meldepflicht?

## Output

Geldwäsche-Routing Anzeige/FIU.

## Red Flags

- FIU-Meldung durch Anzeige ersetzt
- Tipping-off Risiko
- eigene Rolle unklar

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.
