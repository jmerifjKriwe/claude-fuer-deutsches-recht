---
name: tk-anschlussbereitstellung-tk
description: "Tk Anschlussbereitstellung Verzug, Tk Behoerdenkommunikation Kooperationsstrategie: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Tk Anschlussbereitstellung Verzug, Tk Behoerdenkommunikation Kooperationsstrategie

## Arbeitsbereich

In diesem Skill wird **Tk Anschlussbereitstellung Verzug, Tk Behoerdenkommunikation Kooperationsstrategie** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-anschlussbereitstellung-verzug` | Bereitstellung von Festnetz-, Glasfaser-, Mobilfunk- oder Business-Anschluss: Terminversäumnis, Verzug, Entschädigung, Rücktritt, Ersatzlösung und Beweis. |
| `tk-behoerdenkommunikation-kooperationsstrategie` | Kommunikationsstrategie gegenüber der Bundesnetzagentur: kooperativ, präzise, aktenfest, geheimnisschonend und entscheidungsorientiert. |

## Arbeitsweg

Für **Tk Anschlussbereitstellung Verzug, Tk Behoerdenkommunikation Kooperationsstrategie** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `telekommunikationsrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-anschlussbereitstellung-verzug`

**Fokus:** Bereitstellung von Festnetz-, Glasfaser-, Mobilfunk- oder Business-Anschluss: Terminversäumnis, Verzug, Entschädigung, Rücktritt, Ersatzlösung und Beweis.

# Anschlussbereitstellung und Verzug

## Einsatz

Für Fälle, in denen ein Anschluss nicht kommt, Technikertermine platzen oder der Anbieter zwischen Tiefbau, Hausverwaltung und Netzbetreiber verweist.

## Norm- und Quellenanker

TKG Kundenschutz §§ 51 ff. live prüfen; BGB §§ 280, 286, 323; ZPO; BNetzA-Verbraucherinformationen.

## Arbeitsfragen

1. Was wurde vertraglich zugesagt und bis wann?
2. Welche Termine wurden versäumt und wer hat sie bestätigt?
3. Ist Verbraucher- oder Geschäftskundenrecht betroffen?
4. Welche Ersatzkosten sind entstanden?

## Output

Verzugsfahrplan, Entschädigungsforderung, Rücktrittsoption und Belegmatrix.

## Red Flags

- Termin nur telefonisch vereinbart
- Hausanschluss/Tarifaktivierung verwechselt
- Verbraucherentschädigung und SLA nicht getrennt
- Mitwirkungspflicht des Kunden unklar

## Anschluss-Skills

- tk-stoerung-minderung-ausfallentschaedigung
- tk-glasfaser-hausanschluss-wegerecht

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-behoerdenkommunikation-kooperationsstrategie`

**Fokus:** Kommunikationsstrategie gegenüber der Bundesnetzagentur: kooperativ, präzise, aktenfest, geheimnisschonend und entscheidungsorientiert.

# Behördenkommunikation mit BNetzA

## Einsatz

Für regulierte Unternehmen und Beschwerdegegner.

## Norm- und Quellenanker

VwVfG; TKG; Geschäftsgeheimnisgesetz; Compliance-Dokumentation.

## Arbeitsfragen

1. Was ist Ziel der Kommunikation?
2. Welche Fakten sind gesichert?
3. Welche Geheimnisse sind zu markieren?

## Output

Kommunikationsleitfaden und Antwortentwurf.

## Red Flags

- zu viel freiwillige Information
- unklare Zusagen
- keine Aktennotiz

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
