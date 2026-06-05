---
name: tk-towerco-tk-traffic
description: "Tk Towerco Standortmiete, Tk Traffic Location Data Privacy: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Tk Towerco Standortmiete, Tk Traffic Location Data Privacy

## Arbeitsbereich

In diesem Skill wird **Tk Towerco Standortmiete, Tk Traffic Location Data Privacy** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-towerco-standortmiete` | Mobilfunkstandorte: Miet-/Gestattungsvertrag, Baurecht, Immissionsschutz, Standortsharing, Rückbau und Eigentümerkonflikt. |
| `tk-traffic-location-data-privacy` | Verkehrsdaten, Standortdaten, Einzelverbindungsnachweis, Abrechnung, Einwilligung, Sicherheit und Löschung. |

## Arbeitsweg

Für **Tk Towerco Standortmiete, Tk Traffic Location Data Privacy** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `telekommunikationsrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-towerco-standortmiete`

**Fokus:** Mobilfunkstandorte: Miet-/Gestattungsvertrag, Baurecht, Immissionsschutz, Standortsharing, Rückbau und Eigentümerkonflikt.

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

**Fokus:** Verkehrsdaten, Standortdaten, Einzelverbindungsnachweis, Abrechnung, Einwilligung, Sicherheit und Löschung.

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
