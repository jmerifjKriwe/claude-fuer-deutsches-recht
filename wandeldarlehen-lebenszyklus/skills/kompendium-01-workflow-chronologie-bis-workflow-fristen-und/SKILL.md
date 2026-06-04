---
name: kompendium-01-workflow-chronologie-bis-workflow-fristen-und
description: "wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 01; bündelt 2 frühere Spezialskills (workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 01 - wandeldarlehen-lebenszyklus

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin wandeldarlehen-lebenszyklus: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin wandeldarlehen-lebenszyklus: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `workflow-chronologie-und-belegmatrix`

**Frühere Beschreibung:** Chronologie und Belegmatrix im Plugin wandeldarlehen-lebenszyklus: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen.

# Chronologie und Belegmatrix

## Aufgabe
Dieser Workflow-Skill ordnet alle Lebenszyklus-Daten eines Wandeldarlehens chronologisch: Term Sheet, Closing, Auszahlung, Zinszahlungen, Trigger-Ereignisse (Folge-Runde, Maturity, Insolvenz), Wandlung, Eintragung.

## Pflicht-Timeline Wandeldarlehen
- **Term-Sheet-Datum** und -Verbindlichkeitsumfang.
- **Closing / Unterzeichnung CLA**.
- **Auszahlungsdatum** (regelmäßig auf Sperrkonto / Treuhand, dann Freigabe an Gesellschaft).
- **Zinszahlung / Zinslauf** (oft endfällig "PIK -- Payment in Kind").
- **Maturity-Datum** (12-36 Monate).
- **Trigger-Ereignis Folge-Runde:** Datum der qualifizierten Finanzierungsrunde; Term-Sheet-Vorstellung beim Investor.
- **Kapitalerhöhungsbeschluss** (§ 55 GmbHG / § 182 AktG) -- Notartermin mit Vorlauf 1-2 Wochen.
- **Eintragung im Handelsregister.**
- **Insolvenz-Trigger:** Antragspflicht §  15a InsO (3 Wochen Zahlungsunfähigkeit, 6 Wochen Überschuldung); ggf. Rangrücktritt-Erklärung vor Insolvenz nachweisen.

## Belegmatrix
- Datum | Ereignis | Vertragsstelle / Beschluss / Bescheid | Norm-Anker | Steuerfolge (KapSt § 43 EStG, § 17 EStG) | Relevanz | offene Frage.

## Anti-Muster
- Unklare Datum-Reihenfolge bei Maturity, Folge-Runde und Insolvenzantragspflicht -> kann zu Anfechtbarkeit nach §§ 129 ff. InsO führen.
- Notartermin zu knapp vor Maturity -> Wandlung verfehlt; Auseinandersetzung über Cap und Discount.

## Kaltstart
Wenn Material vorliegt, arbeite zuerst mit dem Material. Stelle nur Rückfragen, die für die nächste Weiche nötig sind:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 2. `workflow-fristen-und-risikoampel`

**Frühere Beschreibung:** Fristen- und Risikoampel im Plugin wandeldarlehen-lebenszyklus: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.

# Fristen- und Risikoampel

## Aufgabe
Dieser Workflow-Skill markiert in Wandeldarlehens-Mandaten typische Fristen und Eskalationspunkte: Maturity, Wandlungsfristen, Notartermin, Insolvenzgefahr (Rangrücktritt erforderlich?), KapSt-Anmeldungen.

## Fristen Wandeldarlehen
- **Maturity (Laufzeit):** 12-36 Monate marktüblich; Vorlaufzeit für Wandlung oder Rückzahlung 3-6 Monate einplanen.
- **Wandlungstrigger Closing Folge-Runde:** Notartermin mit Vorlauf 1-2 Wochen; Beschluss Kapitalerhöhung (§ 55 GmbHG / § 182 AktG) vorbereiten.
- **Kapitalertragsteuer:** § 43 EStG -- Anmeldung und Abführung der KapSt durch Schuldner der Zinsen unverzüglich nach Zufluss.
- **Sachkapitalerhöhung mit Werthaltigkeitsbescheinigung:** Notartermin und Bescheinigung Wirtschaftsprüfer.
- **Insolvenzantragspflicht (§ 15a InsO):** 3 Wochen bei Zahlungsunfähigkeit, 6 Wochen bei Überschuldung. Rangrücktritt (§ 39 Abs. 2 InsO) muss vorab vereinbart und qualifiziert sein.

## Risikoampel
- **Rot:** Maturity erreicht ohne Wandlung oder Verlängerung; Insolvenzgefahr ohne Rangrücktritt; KapSt-Pflicht versäumt.
- **Gelb:** Folge-Runde verzögert sich; Bewertungs-Cap zu eng, droht Verwässerung der Gründer; SAFE-Strukturen ohne DE-Anpassung.
- **Grün:** Term Sheet verbindlich, Notar terminiert, Cap Table simuliert.

## Anti-Muster
- Wandeldarlehen mit Sicherungsabrede ohne Rangrücktritt -- Insolvenzfeste Strukturierung fehlt.
- "We Are SAFE" 1:1 nach US-Vorlage ohne Notar-/GmbH-Form -- nicht durchsetzbar.

## Kaltstart
Wenn Material vorliegt, arbeite zuerst mit dem Material. Stelle nur Rückfragen, die für die nächste Weiche nötig sind:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.
