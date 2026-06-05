---
name: tk-zugangsregulierung-tk-zusammenschaltung
description: "Tk Zugangsregulierung Vorleistung, Tk Zusammenschaltung Interconnection: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Tk Zugangsregulierung Vorleistung, Tk Zusammenschaltung Interconnection

## Arbeitsbereich

In diesem Skill wird **Tk Zugangsregulierung Vorleistung, Tk Zusammenschaltung Interconnection** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-zugangsregulierung-vorleistung` | Zugang zu Netzen, Vorleistungsprodukten, TAL/Bitstrom, Glasfaser, Nichtdiskriminierung und technische Schnittstellen. |
| `tk-zusammenschaltung-interconnection` | Zusammenschaltung, Terminierung, IP-Interconnection, Qualität, Entgelte und Streitbeilegung. |

## Arbeitsweg

Für **Tk Zugangsregulierung Vorleistung, Tk Zusammenschaltung Interconnection** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `telekommunikationsrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-zugangsregulierung-vorleistung`

**Fokus:** Zugang zu Netzen, Vorleistungsprodukten, TAL/Bitstrom, Glasfaser, Nichtdiskriminierung und technische Schnittstellen.

# Zugangsregulierung und Vorleistungen

## Einsatz

Für Wettbewerber, die Zugang brauchen, oder Netzbetreiber, die Zugangspflichten erfüllen müssen.

## Norm- und Quellenanker

TKG Zugangsregulierung; BNetzA-Standardangebote; GWB/AEUV.

## Arbeitsfragen

1. Welcher Zugang wird verlangt?
2. Ist Pflicht, freiwilliger Open Access oder Vertrag betroffen?
3. Welche technischen/kommerziellen Bedingungen sind streitig?

## Output

Zugangsantrag/Stellungnahme und Konditionenmatrix.

## Red Flags

- Nichtdiskriminierung nicht belegt
- technische Schnittstelle unklar
- Vertraulichkeit überdehnt

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-zusammenschaltung-interconnection`

**Fokus:** Zusammenschaltung, Terminierung, IP-Interconnection, Qualität, Entgelte und Streitbeilegung.

# Zusammenschaltung und Interconnection

## Einsatz

Für Netzbetreiber, MVNOs und Diensteanbieter bei Interconnection-Konflikten.

## Norm- und Quellenanker

TKG Zusammenschaltung; EECC; BNetzA-Streitbeilegung.

## Arbeitsfragen

1. Welche Netze/Dienste werden verbunden?
2. Welche technischen Spezifikationen und Entgelte gelten?
3. Welche Störung/Verweigerung liegt vor?

## Output

Interconnection-Matrix, Streitbeilegungsantrag und SLA-Check.

## Red Flags

- technische und rechtliche Ebene vermischt
- Terminierungsentgelt veraltet
- QoS nicht gemessen

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
