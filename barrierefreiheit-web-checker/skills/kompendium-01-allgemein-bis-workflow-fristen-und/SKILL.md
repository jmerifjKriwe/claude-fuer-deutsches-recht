---
name: kompendium-01-allgemein-bis-workflow-fristen-und
description: "barrierefreiheit-web-checker: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 01 - barrierefreiheit-web-checker

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `allgemein` | Kaltstart, Scope und Workflow-Routing für digitale Barrierefreiheit. Fragt Website App Webshop öffentliche Stelle BFSG BITV EN 301 549 WCAG Zielgruppe Audit-Tiefe und Output ab, schlägt passende Skills vor und startet mit Prüfplan. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin barrierefreiheit-web-checker: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin barrierefreiheit-web-checker: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `allgemein`

**Frühere Beschreibung:** Kaltstart, Scope und Workflow-Routing für digitale Barrierefreiheit. Fragt Website App Webshop öffentliche Stelle BFSG BITV EN 301 549 WCAG Zielgruppe Audit-Tiefe und Output ab, schlägt passende Skills vor und startet mit Prüfplan.

# Barrierefreiheit Web Checker — Allgemein

Arbeite wie ein ruhiger Accessibility-Lead mit juristischem Radar. Erst klären, welcher Rechtsrahmen überhaupt gilt, dann prüfen, was Nutzerinnen und Nutzer tatsächlich bedienen können, dann dokumentieren.

## Kaltstart

**Kurzbild**
- Prüfobjekt: Website / Webshop / Portal / App / PDF / Intranet
- Betreiber: öffentliche Stelle / Unternehmen B2C / B2B / Verein / Kanzlei / Kommune
- Zweck: Audit / Relaunch / Abmahnungsreaktion / Behördenanfrage / Vergabe / Agenturabnahme
- Maßstab: BFSG/BFSGV / BITV 2.0 / EN 301 549 / WCAG / freiwillig
- Output: Prüfbericht / Maßnahmenplan / Barrierefreiheitserklärung / Entwickler-Tickets / Management-Memo

## Routing

| Situation | Skill |
| --- | --- |
| Unklar, ob Pflicht besteht | `scope-bfsg-bitv-wad` |
| Prüfkatalog und Stichprobe bauen | `en301549-wcag-pruefplan` |
| Scanner-Ergebnisse einordnen | `automatisierter-audit-axe-lighthouse` |
| Navigation/Fokus problematisch | `tastatur-fokus-navigation` |
| Screenreader/ARIA/Semantik | `screenreader-semantik-aria` |
| Kontrast, Zoom, Motion | `kontrast-farbe-motion-responsive` |
| Shop, Login, Checkout | `formulare-checkout-ecommerce` |
| PDFs und Downloads | `pdf-downloads-dokumente` |
| Erklärung und Feedbackweg | `erklaerung-feedback-durchsetzung` |
| Roadmap und Nachweise | `remediation-roadmap-dokumentation` |
| Agentur/Lastenheft/Abnahme | `agentur-abnahme-vergabe` |

## Mindestantwort

Wenn Angaben fehlen, stelle höchstens eine Rückfrage. Wenn der Nutzer eine URL oder Screenshots liefert, beginne mit Scope, sichtbaren Risiken und einem Prüfplan.

## Quellenregel

Bei Rechtsstandfragen zuerst `references/rechtsstand-mai-2026.md` beachten. Keine Bußgeld-, Behörden- oder Standardbehauptung ohne aktuelle Quelle.

## 2. `workflow-chronologie-und-belegmatrix`

**Frühere Beschreibung:** Chronologie und Belegmatrix im Plugin barrierefreiheit-web-checker: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen.

# Chronologie und Belegmatrix

## Aufgabe
Dieser Workflow-Skill für `barrierefreiheit-web-checker` Chronologie und Belegmatrix im Plugin barrierefreiheit-web-checker: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## 3. `workflow-fristen-und-risikoampel`

**Frühere Beschreibung:** Fristen- und Risikoampel im Plugin barrierefreiheit-web-checker: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.

# Fristen- und Risikoampel

## Aufgabe
Dieser Workflow-Skill für `barrierefreiheit-web-checker` Fristen- und Risikoampel im Plugin barrierefreiheit-web-checker: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Barrierefreiheit-typische Fristen
- **BFSG**: Geltung seit **28.06.2025** für neue Produkte/Dienstleistungen; Selbstbedienungsterminals **Übergang bis 27.06.2040** (§ 38 BFSG).
- **BFSGV** (Verordnung): konkretisiert technische Anforderungen.
- **Marktüberwachung** § 19 BFSG: Behörde kann Mängelbeseitigung anordnen, Vertrieb untersagen.
- **Bußgeld § 37 BFSG**: bis **100.000 EUR**.
- **Schlichtung § 21 BFSG**: Verbraucherschlichtungsstelle bei der Schlichtungsstelle des Bundes; vor Klage zumeist obligatorische Schlichtung.

## Ampelkriterien
- **Rot**: BFSG-Pflicht erkannt, aber Produkt/Dienst seit 28.06.2025 ohne Konformität; behördliche Anordnung; Klage/Schlichtung anhängig.
- **Gelb**: WCAG-2.1-AA-Konformität nicht systematisch geprüft, kein Accessibility Statement, fehlende Konformitätserklärung (§ 6 BFSG, Art. 12 EU-Richtlinie 2019/882).
- **Grün**: Konformitätserklärung vorliegt, regelmäßige Tests (automatisch + manuell), AS (Accessibility Statement) öffentlich, Kontakt nach § 14 BFSG benannt.

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
