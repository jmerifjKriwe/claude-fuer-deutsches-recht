---
name: kompendium-20-tk-routerfreiheit-en-bis-tk-rufnummernmissbra
description: "telekommunikationsrecht: Konsolidiertes Skill-Kompendium 20; bündelt 2 frühere Spezialskills (tk-routerfreiheit-endgeraete, tk-rufnummernmissbrauch-abschaltung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 20 - telekommunikationsrecht

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `tk-routerfreiheit-endgeraete` | Routerfreiheit, Netzabschlusspunkt, Endgerätefreiheit, Providerrouter, Konfigurationsdaten, Glasfaser-ONT und Gewährleistung/Sicherheit. |
| `tk-rufnummernmissbrauch-abschaltung` | Rufnummernmissbrauch, Ping-Anrufe, Spam, Mehrwertdienste, Abschaltung, Rechnungslegungs-/Inkassoverbot und Beschwerde. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `tk-routerfreiheit-endgeraete`

**Frühere Beschreibung:** Routerfreiheit, Netzabschlusspunkt, Endgerätefreiheit, Providerrouter, Konfigurationsdaten, Glasfaser-ONT und Gewährleistung/Sicherheit.

# Routerfreiheit und Endgeräte

## Einsatz

Für Streit, ob der Kunde eigenen Router/ONT nutzen darf oder Provider technische Vorgaben macht.

## Norm- und Quellenanker

TKG Endgerätefreiheit/Netzabschlusspunkt live prüfen; BGB; Produktsicherheits-/Cyberrecht; BNetzA-Festlegungen.

## Arbeitsfragen

1. Wo liegt der passive Netzabschlusspunkt?
2. Welche Zugangsdaten/Konfigurationsdaten muss Anbieter bereitstellen?
3. Welche Sicherheits- oder Supportargumente sind tragfähig?
4. Welche Folgen hat eigener Router für Störung/Gewährleistung?

## Output

Routerfreiheits-Memo, Providerbrief, technische Fragenliste und Verbraucher-/Businessvariante.

## Red Flags

- ONT als Providerhoheit behauptet
- Konfigurationsdaten fehlen
- Störung vorschnell dem Kundenrouter zugeschrieben
- Sicherheitsargument ohne Normbasis

## Anschluss-Skills

- tk-stoerung-minderung-ausfallentschaedigung
- tk-glasfaser-hausanschluss-wegerecht

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-rufnummernmissbrauch-abschaltung`

**Frühere Beschreibung:** Rufnummernmissbrauch, Ping-Anrufe, Spam, Mehrwertdienste, Abschaltung, Rechnungslegungs-/Inkassoverbot und Beschwerde.

# Rufnummernmissbrauch, Abschaltung und Inkassoverbot

## Einsatz

Für Verbraucherbeschwerden und Anbieterabwehr gegen Missbrauchsmaßnahmen.

## Norm- und Quellenanker

TKG Missbrauchsaufsicht/Nummerierung; UWG; BNetzA-Verbraucherschutz.

## Arbeitsfragen

1. Welche Nummer, Kampagne und Rechnung ist betroffen?
2. Welche Missbrauchstatsachen sind belegt?
3. Welche BNetzA-Maßnahme oder Beschwerde läuft?

## Output

Missbrauchsdossier, Beschwerde/Abwehr und Rechnungsprüfung.

## Red Flags

- Kundenbeschwerden nicht gesichert
- Inkasso trotz Verbot
- Callcenter-Kette unklar

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
