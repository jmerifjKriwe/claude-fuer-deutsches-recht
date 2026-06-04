---
name: kompendium-19-tk-nummerierung-rufn-bis-tk-open-ran-lieferke
description: "telekommunikationsrecht: Konsolidiertes Skill-Kompendium 19; bündelt 2 frühere Spezialskills (tk-nummerierung-rufnummernzuteilung, tk-open-ran-lieferketten) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 19 - telekommunikationsrecht

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `tk-nummerierung-rufnummernzuteilung` | Rufnummernzuteilung, Nutzung, Entzug, Mehrwertdienste, geografische Nummern, 0800/0900, M2M und Nummernportierung. |
| `tk-open-ran-lieferketten` | Open-RAN-/Netzkomponenten: Lieferkette, Sicherheit, Interoperabilität, Ausfall, Exportkontrolle und kritische Komponenten. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `tk-nummerierung-rufnummernzuteilung`

**Frühere Beschreibung:** Rufnummernzuteilung, Nutzung, Entzug, Mehrwertdienste, geografische Nummern, 0800/0900, M2M und Nummernportierung.

# Nummerierung und Rufnummernzuteilung

## Einsatz

Für Anbieter und Dienste, deren Geschäftsmodell an Rufnummern hängt.

## Norm- und Quellenanker

TKG Nummerierungsrecht; BNetzA-Nummernpläne/Verfügungen live prüfen.

## Arbeitsfragen

1. Welche Nummernart und Nutzungsbedingung?
2. Ist Nutzung zweckgerecht?
3. Droht Entzug oder Abschaltung?

## Output

Nummernrechtsmemo und BNetzA-Antrag/Antwort.

## Red Flags

- Nummernart falsch
- Werbung/Missbrauch droht
- Zuteilungsinhaber und Nutzer verwechselt

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-open-ran-lieferketten`

**Frühere Beschreibung:** Open-RAN-/Netzkomponenten: Lieferkette, Sicherheit, Interoperabilität, Ausfall, Exportkontrolle und kritische Komponenten.

# Open RAN und Lieferketten

## Einsatz

Für Netzmodernisierung und Vendor-Management.

## Norm- und Quellenanker

TKG; NIS2/BSI; IT-Sicherheitsgesetz; Außenwirtschaftsrecht; Vertragsrecht.

## Arbeitsfragen

1. Welche Komponenten und Lieferanten?
2. Welche Sicherheits-/Zertifizierungsanforderungen?
3. Welche Exit- und Interoperabilitätsrechte?

## Output

Lieferketten-Risikomemo und Vertragsklauseln.

## Red Flags

- Vendor Lock-in trotz Open RAN
- Sicherheitsnachweise fehlen
- Exportkontrollrisiko

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
