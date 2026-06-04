---
name: kompendium-18-tk-notfall-und-katas-bis-tk-notrufpflicht-112
description: "telekommunikationsrecht: Konsolidiertes Skill-Kompendium 18; bündelt 2 frühere Spezialskills (tk-notfall-und-katastrophenkommunikation, tk-notrufpflicht-112) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 18 - telekommunikationsrecht

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `tk-notfall-und-katastrophenkommunikation` | Notfallkommunikation, Resilienz, Priorisierung, Cell Broadcast, Behördenkommunikation und Business Continuity. |
| `tk-notrufpflicht-112` | Notruf 112/110, Standortdaten, Ausfallsicherheit, VoIP, Alarmierung, Unternehmensanschlüsse und Haftungsrisiko. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `tk-notfall-und-katastrophenkommunikation`

**Frühere Beschreibung:** Notfallkommunikation, Resilienz, Priorisierung, Cell Broadcast, Behördenkommunikation und Business Continuity.

# Notfall- und Katastrophenkommunikation

## Einsatz

Für Provider und Betreiber kritischer Einrichtungen.

## Norm- und Quellenanker

TKG Sicherheits-/Notfallregeln; BBK/BSI/BNetzA-Vorgaben live prüfen.

## Arbeitsfragen

1. Welche Dienste müssen im Notfall aufrechterhalten werden?
2. Welche Behördenkontakte und Tests?
3. Welche Kunden-/Priorisierungspflichten?

## Output

Notfallkommunikationsplan und Testkalender.

## Red Flags

- Backupstrom fehlt
- Behördenkontakte veraltet
- Cell-Broadcast-Rollen unklar

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-notrufpflicht-112`

**Frühere Beschreibung:** Notruf 112/110, Standortdaten, Ausfallsicherheit, VoIP, Alarmierung, Unternehmensanschlüsse und Haftungsrisiko.

# Notrufpflicht und Ausfallsicherheit

## Einsatz

Für Anbieter und Geschäftskunden, wenn Telefonie, Cloud-PBX oder IoT-Dienst Notruffunktionen beeinflusst.

## Norm- und Quellenanker

TKG Notrufvorschriften live prüfen; Sicherheitsrecht; DSGVO Standortdaten; BSI/NIS2-Schnittstelle.

## Arbeitsfragen

1. Welche Dienste ermöglichen Notrufe?
2. Welche Standort-/Routingdaten werden übermittelt?
3. Welche Ausfall- und Backupstrategie existiert?
4. Welche Kundeninformationen sind nötig?

## Output

Notruf-Compliance-Check, Risikoampel, Vertragsklauseln und Incident-Plan.

## Red Flags

- Cloud-PBX ohne Standortlogik
- Homeoffice-Notruf falsch geroutet
- Ausfallplan fehlt
- Datenschutz blockiert Notruffunktion falsch

## Anschluss-Skills

- tk-cloud-telefonie-voip-compliance
- tk-notfall-und-katastrophenkommunikation

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
