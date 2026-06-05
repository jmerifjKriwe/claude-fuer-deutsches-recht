---
name: tk-notfall-tk-notrufpflicht
description: "Tk Notfall Und Katastrophenkommunikation, Tk Notrufpflicht 112: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Tk Notfall Und Katastrophenkommunikation, Tk Notrufpflicht 112

## Arbeitsbereich

In diesem Skill wird **Tk Notfall Und Katastrophenkommunikation, Tk Notrufpflicht 112** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-notfall-und-katastrophenkommunikation` | Notfallkommunikation, Resilienz, Priorisierung, Cell Broadcast, Behördenkommunikation und Business Continuity. |
| `tk-notrufpflicht-112` | Notruf 112/110, Standortdaten, Ausfallsicherheit, VoIP, Alarmierung, Unternehmensanschlüsse und Haftungsrisiko. |

## Arbeitsweg

Für **Tk Notfall Und Katastrophenkommunikation, Tk Notrufpflicht 112** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `telekommunikationsrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-notfall-und-katastrophenkommunikation`

**Fokus:** Notfallkommunikation, Resilienz, Priorisierung, Cell Broadcast, Behördenkommunikation und Business Continuity.

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

**Fokus:** Notruf 112/110, Standortdaten, Ausfallsicherheit, VoIP, Alarmierung, Unternehmensanschlüsse und Haftungsrisiko.

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
