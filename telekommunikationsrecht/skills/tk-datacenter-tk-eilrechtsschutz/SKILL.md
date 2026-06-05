---
name: tk-datacenter-tk-eilrechtsschutz
description: "Tk Datacenter Connectivity, Tk Eilrechtsschutz Bnetza Beschluss: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Tk Datacenter Connectivity, Tk Eilrechtsschutz Bnetza Beschluss

## Arbeitsbereich

In diesem Skill wird **Tk Datacenter Connectivity, Tk Eilrechtsschutz Bnetza Beschluss** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-datacenter-connectivity` | Rechenzentrumskonnektivität: Carrier Meet-Me, Cross-Connects, SLA, Wegerecht im Gebäude, Datenschutz/Sicherheit und Ausfallhaftung. |
| `tk-eilrechtsschutz-bnetza-beschluss` | Eilrechtsschutz bei Frequenz-, Entgelt-, Zugang-, Nummerierungs- oder Missbrauchsmaßnahmen. |

## Arbeitsweg

Für **Tk Datacenter Connectivity, Tk Eilrechtsschutz Bnetza Beschluss** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `telekommunikationsrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-datacenter-connectivity`

**Fokus:** Rechenzentrumskonnektivität: Carrier Meet-Me, Cross-Connects, SLA, Wegerecht im Gebäude, Datenschutz/Sicherheit und Ausfallhaftung.

# Datacenter Connectivity und Carrier Meet-Me

## Einsatz

Für Rechenzentren, Carrier und Unternehmenskunden.

## Norm- und Quellenanker

BGB; TKG; NIS2/BSI; AGB-Recht.

## Arbeitsfragen

1. Welche Connects und Carrier?
2. Welche Verfügbarkeit und Wartungsfenster?
3. Welche Sicherheitszonen?

## Output

Connectivity-Vertragscheck und Ausfallplan.

## Red Flags

- Cross-Connect ohne klare Verantwortung
- Wartungsfenster zu breit
- Security-Zutritt ungeklärt

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-eilrechtsschutz-bnetza-beschluss`

**Fokus:** Eilrechtsschutz bei Frequenz-, Entgelt-, Zugang-, Nummerierungs- oder Missbrauchsmaßnahmen.

# Eilrechtsschutz gegen BNetzA-Beschluss

## Einsatz

Wenn ein BNetzA-Beschluss sofort wirtschaftlich wirkt.

## Norm- und Quellenanker

VwGO §§ 80, 80a, 123; TKG; VwVfG.

## Arbeitsfragen

1. Hat der Rechtsbehelf aufschiebende Wirkung?
2. Welche irreversiblen Nachteile drohen?
3. Wie wird Interessenabwägung belegt?

## Output

Eilantragsskizze und Anlagenliste.

## Red Flags

- Eilbedürftigkeit nicht belegt
- Hauptsachechancen fehlen
- Dritte nicht beigeladen

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
