---
name: kompendium-24-tk-towerco-standortm-bis-tk-traffic-location
description: "telekommunikationsrecht: Konsolidiertes Skill-Kompendium 24; bündelt 2 frühere Spezialskills (tk-towerco-standortmiete, tk-traffic-location-data-privacy) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 24 - telekommunikationsrecht

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `tk-towerco-standortmiete` | Mobilfunkstandorte: Miet-/Gestattungsvertrag, Baurecht, Immissionsschutz, Standortsharing, Rückbau und Eigentümerkonflikt. |
| `tk-traffic-location-data-privacy` | Verkehrsdaten, Standortdaten, Einzelverbindungsnachweis, Abrechnung, Einwilligung, Sicherheit und Löschung. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `tk-towerco-standortmiete`

**Frühere Beschreibung:** Mobilfunkstandorte: Miet-/Gestattungsvertrag, Baurecht, Immissionsschutz, Standortsharing, Rückbau und Eigentümerkonflikt.

# TowerCo und Mobilfunkstandortmiete

## Einsatz

Für TowerCos, Netzbetreiber und Grundstückseigentümer.

## Norm- und Quellenanker

BGB Mietrecht; TKG; Bau-/Immissionsschutzrecht; Frequenzrecht.

## Arbeitsfragen

1. Welche Anlage und Fläche?
2. Welche Genehmigungen und Immissionen?
3. Welche Sharing-/Rückbaupflichten?

## Output

Standortvertrags-Redline und Genehmigungscheck.

## Red Flags

- Rückbau vergessen
- Immissionsnachweis fehlt
- Exklusivklausel kartell-/tk-riskant

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-traffic-location-data-privacy`

**Frühere Beschreibung:** Verkehrsdaten, Standortdaten, Einzelverbindungsnachweis, Abrechnung, Einwilligung, Sicherheit und Löschung.

# Verkehrs- und Standortdaten

## Einsatz

Für Anbieter, Arbeitgeber und Kunden bei sensiblen Nutzungsdaten.

## Norm- und Quellenanker

TKG/TDDDG Telekommunikationsdatenschutz; DSGVO; ePrivacy-Recht live prüfen.

## Arbeitsfragen

1. Welche Datenkategorie?
2. Für welchen Zweck und wie lange?
3. Welche Einwilligung/gesetzliche Grundlage?

## Output

Datenschutz- und Löschkonzept.

## Red Flags

- Standortdaten als normale Kundendaten
- Speicherfrist unklar
- EVN ohne Berechtigung

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
