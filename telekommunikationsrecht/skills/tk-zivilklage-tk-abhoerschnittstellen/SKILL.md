---
name: tk-zivilklage-tk-abhoerschnittstellen
description: "Tk Zivilklage Lg Entgelt Schadensersatz, Tk Abhoerschnittstellen Sicherheitsbehoerden: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Tk Zivilklage Lg Entgelt Schadensersatz, Tk Abhoerschnittstellen Sicherheitsbehoerden

## Arbeitsbereich

In diesem Skill wird **Tk Zivilklage Lg Entgelt Schadensersatz, Tk Abhoerschnittstellen Sicherheitsbehoerden** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-zivilklage-lg-entgelt-schadensersatz` | Zivilrechtliche TK-Klagen: Entgeltforderungen, Rückzahlung, Schadensersatz, SLA, AGB, Minderung und Verbraucher-/Businessstreit. |
| `tk-abhoerschnittstellen-sicherheitsbehoerden` | TK-Überwachung, Schnittstellen, Auskunftsersuchen, Bestandsdaten, Verkehrsdaten, Strafverfolgung und Geheimnisschutz. |

## Arbeitsweg

Für **Tk Zivilklage Lg Entgelt Schadensersatz, Tk Abhoerschnittstellen Sicherheitsbehoerden** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `telekommunikationsrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-zivilklage-lg-entgelt-schadensersatz`

**Fokus:** Zivilrechtliche TK-Klagen: Entgeltforderungen, Rückzahlung, Schadensersatz, SLA, AGB, Minderung und Verbraucher-/Businessstreit.

# Zivilklage: Entgelt, Schaden, Vertrag

## Einsatz

Für Vertragsstreit ohne unmittelbaren BNetzA-Bescheid.

## Norm- und Quellenanker

BGB; ZPO; TKG Kundenschutz; AGB-Recht.

## Arbeitsfragen

1. Welche Anspruchsgrundlage?
2. Welche Rechnung/Leistung ist streitig?
3. Welche Beweise?

## Output

Klage-/Klageerwiderungsgerüst und Streitwert.

## Red Flags

- Regulierungsfrage als Vorfrage ungeklärt
- Rechnungsdaten fehlen
- AGB nicht einbezogen

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-abhoerschnittstellen-sicherheitsbehoerden`

**Fokus:** TK-Überwachung, Schnittstellen, Auskunftsersuchen, Bestandsdaten, Verkehrsdaten, Strafverfolgung und Geheimnisschutz.

# Überwachungsschnittstellen und Behördenauskünfte

## Einsatz

Für Provider, die rechtmäßig kooperieren müssen, aber keine Daten zu viel herausgeben dürfen.

## Norm- und Quellenanker

TKG; TKÜV; StPO; Polizeirecht; Datenschutzrecht.

## Arbeitsfragen

1. Welche Behörde und welcher Rechtsgrund?
2. Welche Datenkategorie?
3. Welche Form-/Anordnungsvoraussetzung?

## Output

Behördenanfrage-Check und Herausgabeprotokoll.

## Red Flags

- informelle Anfrage
- falsche Datenkategorie
- keine Dokumentation

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
