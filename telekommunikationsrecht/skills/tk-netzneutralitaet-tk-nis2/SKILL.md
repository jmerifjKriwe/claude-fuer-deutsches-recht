---
name: tk-netzneutralitaet-tk-nis2
description: "Tk Netzneutralitaet Zero Rating Throttling, Tk Nis2 Kritis Bsi Schnittstelle: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Tk Netzneutralitaet Zero Rating Throttling, Tk Nis2 Kritis Bsi Schnittstelle

## Arbeitsbereich

In diesem Skill wird **Tk Netzneutralitaet Zero Rating Throttling, Tk Nis2 Kritis Bsi Schnittstelle** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-netzneutralitaet-zero-rating-throttling` | Netzneutralität: Zero-Rating, Priorisierung, Drosselung, Spezialdienste, Traffic Management und Beschwerde-/Abmahnrisiken. |
| `tk-nis2-kritis-bsi-schnittstelle` | NIS2/KRITIS/BSI-Anforderungen für TK-Unternehmen, Rechenzentren, Managed Services und kritische Kommunikation. |

## Arbeitsweg

Für **Tk Netzneutralitaet Zero Rating Throttling, Tk Nis2 Kritis Bsi Schnittstelle** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `telekommunikationsrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-netzneutralitaet-zero-rating-throttling`

**Fokus:** Netzneutralität: Zero-Rating, Priorisierung, Drosselung, Spezialdienste, Traffic Management und Beschwerde-/Abmahnrisiken.

# Netzneutralität, Zero-Rating und Drosselung

## Einsatz

Für Anbieterprodukte und Beschwerden, wenn Datenverkehr unterschiedlich behandelt wird.

## Norm- und Quellenanker

EU-Verordnung 2015/2120; TKG; BEREC-Leitlinien live prüfen; UWG/GWB-Schnittstelle.

## Arbeitsfragen

1. Welche Verkehrsbehandlung unterscheidet wen oder was?
2. Ist sie technisch notwendig, diskriminierend oder tariflich gesteuert?
3. Gibt es Spezialdienst oder Netzmanagement?
4. Welche BNetzA-/BEREC-Linie ist live zu prüfen?

## Output

Netzneutralitätsprüfung, Produkt-Redline, BNetzA-Risiko und Kundenkommunikation.

## Red Flags

- Marketingtarif vor Rechtsprüfung
- Drosselung nach App-Kategorie
- Spezialdienst ohne Kapazitätsnachweis
- BEREC-Leitlinien nicht geprüft

## Anschluss-Skills

- tk-eu-eecc-router
- tk-missbrauchsaufsicht-sonderkartellrecht

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-nis2-kritis-bsi-schnittstelle`

**Fokus:** NIS2/KRITIS/BSI-Anforderungen für TK-Unternehmen, Rechenzentren, Managed Services und kritische Kommunikation.

# NIS2, KRITIS und BSI-Schnittstelle

## Einsatz

Für Unternehmen, die TK- oder digitale Infrastruktur betreiben.

## Norm- und Quellenanker

NIS2; BSI-Gesetz; TKG; DORA bei Finanzkunden.

## Arbeitsfragen

1. Ist die Einheit erfasst?
2. Welche technischen und organisatorischen Maßnahmen?
3. Welche Leitungsorganpflichten?

## Output

NIS2-Gap-Analyse und Maßnahmenplan.

## Red Flags

- Schwellenwerte ungeprüft
- Geschäftsführung nicht eingebunden
- Lieferkette vergessen

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
