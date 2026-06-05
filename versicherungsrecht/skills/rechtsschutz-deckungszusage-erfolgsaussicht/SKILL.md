---
name: rechtsschutz-deckungszusage-erfolgsaussicht
description: "Rechtsschutz Deckungszusage Erfolgsaussicht im Plugin Versicherungsrecht: prüft konkret Rechtsschutzversicherung, Reiserücktritts- und Reiseabbruchversicherung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Rechtsschutz Deckungszusage Erfolgsaussicht

## Arbeitsbereich

**Rechtsschutz Deckungszusage Erfolgsaussicht** ordnet den Fall über die tragenden Prüffelder: Rechtsschutzversicherung, Reiserücktritts- und Reiseabbruchversicherung. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `rechtsschutz-deckungszusage-stichentscheid` | Rechtsschutzversicherung: Deckungsanfrage, Erfolgsaussicht, Mutwilligkeit, Stichentscheid, Schiedsgutachten, Gebühren und Mandatskommunikation. |
| `rechtsschutz-erfolgsaussicht-mutwilligkeit` | Rechtsschutzversicherung: Ablehnung wegen fehlender Erfolgsaussicht oder Mutwilligkeit angreifen, ohne das Hauptmandat zu gefährden. |
| `reiseversicherung-ruecktritt-abbruch-krankheit` | Reiserücktritts- und Reiseabbruchversicherung: unerwartete schwere Erkrankung, Stornozeitpunkt, Attest, Vorerkrankung, Pandemie, Angehörige und Kreditkartenversicherung. |

## Arbeitsweg

- Rolle und Ziel im Versicherungsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `rechtsschutz-deckungszusage-stichentscheid`

**Fokus:** Rechtsschutzversicherung: Deckungsanfrage, Erfolgsaussicht, Mutwilligkeit, Stichentscheid, Schiedsgutachten, Gebühren und Mandatskommunikation.

# Rechtsschutz: Deckungszusage und Stichentscheid

## Einsatz

Der Skill ist für Anwälte und Mandanten, wenn die RSV die Finanzierung des Rechtsstreits blockiert.

## Norm- und Quellenanker

VVG §§ 125–129, besonders § 128; ARB; RVG; ZPO.

## Arbeitsfragen

1. Welcher Rechtsschutzbereich und welcher Versicherungsfall?
2. Welche Erfolgsaussichten und Mutwilligkeitsargumente nennt der Versicherer?
3. Ist Stichentscheid oder Schiedsgutachten vorgesehen?
4. Welche Gebühren/Deckungskomponenten sind beantragt?

## Output

Deckungsanfrage, Stichentscheid-Entwurf, Kostenmatrix und RSV-Erwiderung.

## Red Flags

- Versicherungsfall falsch datiert
- Vorvertraglichkeit nicht geprüft
- Stichentscheid zu spät
- Kostenpositionen unvollständig

## Anschluss-Skills

- rechtsschutz-vorvertraglichkeit-schadenereignis
- rechtsschutz-erfolgsaussicht-mutwilligkeit

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `rechtsschutz-erfolgsaussicht-mutwilligkeit`

**Fokus:** Rechtsschutzversicherung: Ablehnung wegen fehlender Erfolgsaussicht oder Mutwilligkeit angreifen, ohne das Hauptmandat zu gefährden.

# Rechtsschutz: Erfolgsaussicht und Mutwilligkeit

## Einsatz

Der Skill baut einen nüchternen, finanzierungsfähigen Prospekt für die RSV.

## Norm- und Quellenanker

VVG § 128; ARB; ZPO Prozesskostenlogik analog nur vorsichtig; RVG.

## Arbeitsfragen

1. Welche Tatsachen und Beweise tragen den Hauptanspruch?
2. Welche Gegenargumente sind ernsthaft, welche nur vorgeschoben?
3. Ist Kosten-Nutzen-Verhältnis mutwillig oder wirtschaftlich plausibel?
4. Kann ein Teilrechtsschutz sinnvoll sein?

## Output

Erfolgsaussichtsmemo, Mutwilligkeitsabwehr, Teildeckungsantrag und Mandantenrisiko.

## Red Flags

- Hauptsache zu optimistisch dargestellt
- Kostenrisiko nicht beziffert
- Teilklage/Teilrechtsschutz vergessen
- RSV als Gegner im Hauptstreit vermischt

## Anschluss-Skills

- rechtsschutz-deckungszusage-stichentscheid
- vergleich-abfindung-entschaedigungsquittung

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `reiseversicherung-ruecktritt-abbruch-krankheit`

**Fokus:** Reiserücktritts- und Reiseabbruchversicherung: unerwartete schwere Erkrankung, Stornozeitpunkt, Attest, Vorerkrankung, Pandemie, Angehörige und Kreditkartenversicherung.

# Reiseversicherung: Rücktritt, Abbruch, Krankheit

## Einsatz

Der Skill hilft bei typischen Reiseablehnungen, in denen Atteste, Vorerkrankungen und Stornofristen streiten.

## Norm- und Quellenanker

VVG allgemein; AVB Reise; BGB Reisevertragsrecht §§ 651a ff.; Datenschutz Gesundheitsdaten.

## Arbeitsfragen

1. Welches versicherte Ereignis löste Rücktritt/Abbruch aus?
2. War die Erkrankung unerwartet und schwer im Sinne der AVB?
3. Wann wurde gebucht, diagnostiziert, storniert?
4. Welche Kosten sind ersatzfähig?

## Output

Reise-Deckungsmemo, Attestanforderung, Stornokostenmatrix und Versichererantwort.

## Red Flags

- Attest zu pauschal
- Storno zu spät
- Vorerkrankung als Ausschluss behauptet
- Kreditkartenversicherung mit Reiseveranstalter verwechselt

## Anschluss-Skills

- datenschutz-schweigepflicht-gesundheitsdaten
- vers-fristen-verjaehrung-klagefrist-fallkalender

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
