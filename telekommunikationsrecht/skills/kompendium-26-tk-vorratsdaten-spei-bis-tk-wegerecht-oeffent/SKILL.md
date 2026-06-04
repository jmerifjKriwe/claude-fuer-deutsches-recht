---
name: kompendium-26-tk-vorratsdaten-spei-bis-tk-wegerecht-oeffent
description: "telekommunikationsrecht: Konsolidiertes Skill-Kompendium 26; bündelt 2 frühere Spezialskills (tk-vorratsdaten-speicherung-eugh-bverfg, tk-wegerecht-oeffentliche-wege) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 26 - telekommunikationsrecht

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `tk-vorratsdaten-speicherung-eugh-bverfg` | Vorratsdatenspeicherung, Quick Freeze, Sicherheitsbehördenanfragen und EuGH/BVerfG-Linie live prüfen. |
| `tk-wegerecht-oeffentliche-wege` | Wegerecht, Mitverlegung, Baustellenkoordination, Zustimmung, Wiederherstellung und Streit mit Straßenbaulastträgern. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `tk-vorratsdaten-speicherung-eugh-bverfg`

**Frühere Beschreibung:** Vorratsdatenspeicherung, Quick Freeze, Sicherheitsbehördenanfragen und EuGH/BVerfG-Linie live prüfen.

# Vorratsdaten und Speicherpflichten

## Einsatz

Für Provider und Betroffene bei Speicher-/Auskunftspflichten.

## Norm- und Quellenanker

TKG/TTDSG/TDDDG; DSGVO; GRCh; GG; EuGH/BVerfG nur verifiziert zitieren.

## Arbeitsfragen

1. Welche Pflicht oder Anfrage liegt vor?
2. Welche Datenart und Eingriffsintensität?
3. Welche aktuelle EuGH/BVerfG-Rechtsprechung ist einschlägig?

## Output

Speicherpflichten-Memo und Behördenantwort.

## Red Flags

- alte Vorratsdatenlage verwendet
- Bestandsdaten/Verkehrsdaten verwechselt
- Richtervorbehalt ungeprüft

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-wegerecht-oeffentliche-wege`

**Frühere Beschreibung:** Wegerecht, Mitverlegung, Baustellenkoordination, Zustimmung, Wiederherstellung und Streit mit Straßenbaulastträgern.

# Wegerecht für öffentliche Wege

## Einsatz

Für Netzbau auf öffentlichen Wegen.

## Norm- und Quellenanker

TKG Wegerechte live prüfen; Straßenrecht Bund/Länder; VwVfG/VwGO.

## Arbeitsfragen

1. Welche Straße/Fläche und welcher Träger?
2. Welche Zustimmung/Anzeige?
3. Welche Nebenbestimmungen und Wiederherstellungspflichten?

## Output

Wegerechtsantrag, Nebenbestimmungscheck und Bauzeitenplan.

## Red Flags

- falscher Straßenbaulastträger
- kommunale Sondernutzung überdehnt
- Wiederherstellungskosten ungeklärt

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
