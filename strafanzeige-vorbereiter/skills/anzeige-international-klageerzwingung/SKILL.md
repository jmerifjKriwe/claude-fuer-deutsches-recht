---
name: anzeige-international-klageerzwingung
description: "Anzeige International Klageerzwingung im Strafanzeigen-Vorbereitung: prüft konkret Internationale Sachverhalte, Nach Einstellung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Anzeige International Klageerzwingung

## Arbeitsbereich

**Anzeige International Klageerzwingung** ordnet den Fall über die tragenden Prüffelder: Internationale Sachverhalte, Nach Einstellung. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anzeige-international-eu-158-3` | Internationale Sachverhalte: Tatort, Zuständigkeit, Europol/Interpol nicht direkt, ausländische Behörden, Übersetzungen und Beweise. |
| `anzeige-klageerzwingung-172-stpo` | Nach Einstellung: Beschwerde, Klageerzwingung, Fristen, Verletztenstellung und anwaltliche Schwelle. |

## Arbeitsweg

- Rolle und Ziel im Strafanzeige Vorbereiter klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `anzeige-international-eu-158-3`

**Fokus:** Internationale Sachverhalte: Tatort, Zuständigkeit, Europol/Interpol nicht direkt, ausländische Behörden, Übersetzungen und Beweise.

# Internationale Anzeigen und EU-Bezug

## Einsatz

Für grenzüberschreitenden Betrug, IP, Cyber, Lieferketten.

## Norm- und Quellenanker

StPO §§ 3 ff., 158; EU-Rechtshilfe; IRG.

## Arbeitsfragen

1. Wo liegt Tatort/Erfolg?
2. Welche Beweise im Ausland?
3. Welche Sprache/Übersetzung?

## Output

Internationales Anzeige-Routing.

## Red Flags

- ausländische Behörde falsch
- Beweise nicht übersetzt
- Zuständigkeit unklar

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 2. `anzeige-klageerzwingung-172-stpo`

**Fokus:** Nach Einstellung: Beschwerde, Klageerzwingung, Fristen, Verletztenstellung und anwaltliche Schwelle.

# Klageerzwingung § 172 StPO

## Einsatz

Für Verletzte nach Einstellung.

## Norm- und Quellenanker

StPO §§ 171, 172; OLG-Verfahren.

## Arbeitsfragen

1. Ist der Antragsteller verletzt?
2. Welche Frist?
3. Welche Begründungstiefe?

## Output

Klageerzwingungs-Check.

## Red Flags

- Frist verpasst
- kein Verletzter
- Sachverhalt nicht vollständig

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.
