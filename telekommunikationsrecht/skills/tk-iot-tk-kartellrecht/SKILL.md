---
name: tk-iot-tk-kartellrecht
description: "Tk Iot M2m Sim Karten, Tk Kartellrecht Schnittstelle Gwb Eu: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Tk Iot M2M Sim Karten, Tk Kartellrecht Schnittstelle Gwb Eu

## Arbeitsbereich

In diesem Skill wird **Tk Iot M2M Sim Karten, Tk Kartellrecht Schnittstelle Gwb Eu** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-iot-m2m-sim-karten` | IoT-/M2M-Konnektivität: SIM-Karten, Roaming, Nummerierung, Sicherheit, Datenzugriff, Produkthaftung und Vertragsketten. |
| `tk-kartellrecht-schnittstelle-gwb-eu` | TK-Verträge und Kooperationen mit Kartellrechtsbezug: Open Access, Ausbaukooperation, Exklusivität, Wholesale, Joint Venture. |

## Arbeitsweg

Für **Tk Iot M2M Sim Karten, Tk Kartellrecht Schnittstelle Gwb Eu** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `telekommunikationsrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-iot-m2m-sim-karten`

**Fokus:** IoT-/M2M-Konnektivität: SIM-Karten, Roaming, Nummerierung, Sicherheit, Datenzugriff, Produkthaftung und Vertragsketten.

# IoT, M2M und SIM-Karten

## Einsatz

Für vernetzte Geräte, Flotten, Industrieanlagen und Smart Meter.

## Norm- und Quellenanker

TKG; Cyber-/NIS2-Recht; DSGVO; Produktsicherheitsrecht.

## Arbeitsfragen

1. Welche Geräte und Länder?
2. Welche Daten und Fernzugriffe?
3. Welche Ausfallfolgen?

## Output

IoT-Konnektivitätsmemo und Vertragsklauseln.

## Red Flags

- permanentes Roaming ungeprüft
- Fernzugriff unsicher
- Haftung bei Ausfall ungeklärt

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-kartellrecht-schnittstelle-gwb-eu`

**Fokus:** TK-Verträge und Kooperationen mit Kartellrechtsbezug: Open Access, Ausbaukooperation, Exklusivität, Wholesale, Joint Venture.

# Kartellrechtliche Schnittstelle GWB/EU

## Einsatz

Für Kooperationen, die Infrastruktur effizient machen, aber Wettbewerber ausschließen könnten.

## Norm- und Quellenanker

GWB; AEUV Art. 101/102; TKG; Fusionskontrolle bei Transaktionen.

## Arbeitsfragen

1. Welche Wettbewerber kooperieren?
2. Welche Exklusivität oder Informationsflüsse entstehen?
3. Welche Rechtfertigung/Effizienz?

## Output

Kartell-/TK-Schnittstellenmemo und Clean-Team-Regeln.

## Red Flags

- Gebietsaufteilung
- Preisabsprachen im Wholesale-Kontext
- Exklusivzugang ohne Rechtfertigung

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
