---
name: anzeige-anfangsverdacht-anlagenverzeichnis
description: "Anzeige Anfangsverdacht Anlagenverzeichnis im Strafanzeigen-Vorbereitung: prüft konkret Anfangsverdacht strukturieren, Anlagen zu Strafanzeigen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Anzeige Anfangsverdacht Anlagenverzeichnis

## Arbeitsbereich

**Anzeige Anfangsverdacht Anlagenverzeichnis** ordnet den Fall über die tragenden Prüffelder: Anfangsverdacht strukturieren, Anlagen zu Strafanzeigen. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anzeige-anfangsverdacht-152-160-stpo` | Anfangsverdacht strukturieren: zureichende tatsächliche Anhaltspunkte, Ermittlungsauftrag der StA, keine bloße Spekulation. |
| `anzeige-anlagenverzeichnis-hashlog` | Anlagen zu Strafanzeigen: Nummerierung, Hashwerte, Originale, Kopien, Versandnachweis und digitale Kette. |

## Arbeitsweg

- Rolle und Ziel im Strafanzeige Vorbereiter klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `anzeige-anfangsverdacht-152-160-stpo`

**Fokus:** Anfangsverdacht strukturieren: zureichende tatsächliche Anhaltspunkte, Ermittlungsauftrag der StA, keine bloße Spekulation.

# Anfangsverdacht nach §§ 152, 160 StPO

## Einsatz

Für die Kernfrage: Reicht der Sachverhalt überhaupt für eine sinnvolle Anzeige?

## Norm- und Quellenanker

StPO §§ 152 Abs. 2, 160, 158; RiStBV live prüfen.

## Arbeitsfragen

1. Welche Tatsachen tragen welchen Straftatbestand?
2. Welche Lücken kann die Polizei ermitteln?
3. Welche Lücken sind reine Spekulation?

## Output

Anfangsverdachtsmemo und Ermittlungsansatzliste.

## Red Flags

- nur „das kann kein Zufall sein“
- keine Tatzeit
- keine Handlung des Beschuldigten

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 2. `anzeige-anlagenverzeichnis-hashlog`

**Fokus:** Anlagen zu Strafanzeigen: Nummerierung, Hashwerte, Originale, Kopien, Versandnachweis und digitale Kette.

# Anlagenverzeichnis und Hashlog

## Einsatz

Für umfangreiche Anzeigen.

## Norm- und Quellenanker

StPO; ZPO Beweis; DSGVO.

## Arbeitsfragen

1. Welche Anlage belegt welchen Satz?
2. Original oder Kopie?
3. Wie Versand beweisen?

## Output

Anlagenverzeichnis und Hashlog.

## Red Flags

- Beweise ungeordnet
- Originale aus der Hand gegeben
- keine Zuordnung

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.
