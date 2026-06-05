---
name: anzeige-bankrott-bedrohung
description: "Anzeige Bankrott Bedrohung im Strafanzeigen-Vorbereitung: prüft konkret Bankrott und Buchführungsdelikte, Bedrohung anzeigen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Anzeige Bankrott Bedrohung

## Arbeitsbereich

**Anzeige Bankrott Bedrohung** ordnet den Fall über die tragenden Prüffelder: Bankrott und Buchführungsdelikte, Bedrohung anzeigen. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anzeige-bankrott-283` | Bankrott und Buchführungsdelikte: Vermögensverschiebung, Buchführung, Krise, Gläubigerbenachteiligung und Insolvenzakten. |
| `anzeige-bedrohung-241` | Bedrohung anzeigen: Inhalt, Ernstlichkeit, Adressat, Beweise, Schutzmaßnahmen. |

## Arbeitsweg

- Rolle und Ziel im Strafanzeige Vorbereiter klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `anzeige-bankrott-283`

**Fokus:** Bankrott und Buchführungsdelikte: Vermögensverschiebung, Buchführung, Krise, Gläubigerbenachteiligung und Insolvenzakten.

# Bankrott § 283 StGB

## Einsatz

Für wirtschaftsstrafrechtliche Anzeigen im Krisenfall.

## Norm- und Quellenanker

StGB §§ 283 ff.; InsO; HGB Buchführung.

## Arbeitsfragen

1. Welche Krise?
2. Welche Handlung?
3. Welche Belege?

## Output

Bankrott-Anzeigememo.

## Red Flags

- Krise nicht nachweisbar
- Unterlagen illegal beschafft
- bloßer Verdacht

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 2. `anzeige-bedrohung-241`

**Fokus:** Bedrohung anzeigen: Inhalt, Ernstlichkeit, Adressat, Beweise, Schutzmaßnahmen.

# Bedrohung § 241 StGB

## Einsatz

Für Drohungen per Chat, Mail, Telefon oder persönlich.

## Norm- und Quellenanker

StGB § 241; GewSchG; Polizeirecht.

## Arbeitsfragen

1. Welche Drohung wörtlich?
2. Gegen wen?
3. Welche Beweise?

## Output

Bedrohungsanzeige und Schutzplan.

## Red Flags

- Drohung paraphrasiert
- akute Gefahr nicht gemeldet
- Chat gelöscht

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.
