---
name: tk-universalservice-tk-verwaltungsrecht
description: "Tk Universalservice Mindestversorgung, Tk Verwaltungsrecht Anfechtung Bnetza: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Tk Universalservice Mindestversorgung, Tk Verwaltungsrecht Anfechtung Bnetza

## Arbeitsbereich

In diesem Skill wird **Tk Universalservice Mindestversorgung, Tk Verwaltungsrecht Anfechtung Bnetza** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-universalservice-mindestversorgung` | Universaldienst/Mindestversorgung mit Telekommunikationsdiensten: Unterversorgung, Anspruch, BNetzA-Verfahren, technische Zumutbarkeit und Alternativen. |
| `tk-verwaltungsrecht-anfechtung-bnetza` | Anfechtung, Verpflichtung oder Eilrechtsschutz gegen BNetzA-Beschlüsse und Nebenbestimmungen. |

## Arbeitsweg

Für **Tk Universalservice Mindestversorgung, Tk Verwaltungsrecht Anfechtung Bnetza** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `telekommunikationsrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-universalservice-mindestversorgung`

**Fokus:** Universaldienst/Mindestversorgung mit Telekommunikationsdiensten: Unterversorgung, Anspruch, BNetzA-Verfahren, technische Zumutbarkeit und Alternativen.

# Universaldienst und Mindestversorgung

## Einsatz

Für Orte, Haushalte oder Unternehmen ohne ausreichende Grundversorgung.

## Norm- und Quellenanker

TKG Universaldienst-/Mindestversorgungsregeln live prüfen; EECC; BNetzA-Verfahren.

## Arbeitsfragen

1. Welche Mindestleistung wird nicht erreicht?
2. Welche Anbieter/Technologien sind verfügbar?
3. Welche BNetzA-Schritte wurden eingeleitet?
4. Ist Übergangslösung möglich?

## Output

Unterversorgungsdossier, BNetzA-Antrag/Beschwerde und Technologievergleich.

## Red Flags

- Breitbandwunsch mit Mindestversorgung verwechselt
- Messung fehlt
- Satellit/Mobilfunk nicht geprüft
- kommunaler Ausbau parallel

## Anschluss-Skills

- tk-beweisplan-messung-stoerung-protokoll
- tk-bundesnetzagentur-verfahren-akteneinsicht-fristen

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-verwaltungsrecht-anfechtung-bnetza`

**Fokus:** Anfechtung, Verpflichtung oder Eilrechtsschutz gegen BNetzA-Beschlüsse und Nebenbestimmungen.

# Anfechtung von BNetzA-Beschlüssen

## Einsatz

Für Unternehmen, die BNetzA-Entscheidungen angreifen oder verteidigen.

## Norm- und Quellenanker

VwGO; TKG; VwVfG; Rechtsbehelfsbelehrung live prüfen.

## Arbeitsfragen

1. Welche Klageart?
2. Welche Frist?
3. Welche aufschiebende Wirkung/Eilstrategie?

## Output

Klage-/Eilantragsgerüst und Fristenplan.

## Red Flags

- falsche Frist
- aufschiebende Wirkung unterstellt
- Tenor nicht vollständig gelesen

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
