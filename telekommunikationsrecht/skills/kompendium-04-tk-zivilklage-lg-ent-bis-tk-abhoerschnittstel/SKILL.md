---
name: kompendium-04-tk-zivilklage-lg-ent-bis-tk-abhoerschnittstel
description: "telekommunikationsrecht: Konsolidiertes Skill-Kompendium 04; bündelt 2 frühere Spezialskills (tk-zivilklage-lg-entgelt-schadensersatz, tk-abhoerschnittstellen-sicherheitsbehoerden) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 04 - telekommunikationsrecht

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `tk-zivilklage-lg-entgelt-schadensersatz` | Zivilrechtliche TK-Klagen: Entgeltforderungen, Rückzahlung, Schadensersatz, SLA, AGB, Minderung und Verbraucher-/Businessstreit. |
| `tk-abhoerschnittstellen-sicherheitsbehoerden` | TK-Überwachung, Schnittstellen, Auskunftsersuchen, Bestandsdaten, Verkehrsdaten, Strafverfolgung und Geheimnisschutz. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `tk-zivilklage-lg-entgelt-schadensersatz`

**Frühere Beschreibung:** Zivilrechtliche TK-Klagen: Entgeltforderungen, Rückzahlung, Schadensersatz, SLA, AGB, Minderung und Verbraucher-/Businessstreit.

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

**Frühere Beschreibung:** TK-Überwachung, Schnittstellen, Auskunftsersuchen, Bestandsdaten, Verkehrsdaten, Strafverfolgung und Geheimnisschutz.

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
