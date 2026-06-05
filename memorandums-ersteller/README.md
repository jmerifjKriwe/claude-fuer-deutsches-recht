# Memorandums-Ersteller

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`memorandums-ersteller`) | [`memorandums-ersteller.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/memorandums-ersteller.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Grenzüberschreitender Asset-Deal Volkenrath Energie SE / Pipeline Northsea Ltd.** (`memorandum-grenzueberschreitender-asset-deal-volkenrath-energie`) | [Gesamt-PDF lesen](../testakten/memorandum-grenzueberschreitender-asset-deal-volkenrath-energie/gesamt-pdf/memorandum-grenzueberschreitender-asset-deal-volkenrath-energie_gesamt.pdf) | [`testakte-memorandum-grenzueberschreitender-asset-deal-volkenrath-energie.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-memorandum-grenzueberschreitender-asset-deal-volkenrath-energie.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Wandelt Mandantenunterlagen in ein juristisches Memorandum mit Vier-Teile-Gliederung — Sachverhalt mit Quellenreferenz; Ein-Satz-Fragen; Ein-Satz-Antworten; rechtliche Ausführungen mit Pinpoint-Zitierung. Optional Piercing-Questions. Rechtsgebietsneutral.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `memorandums-ersteller` | Erzeugt aus heterogenen Mandantenunterlagen ein professionelles juristisches Memorandum mit Vier-Teile-Gliederung — Sachverhalt mit lückenloser Quellenreferenzierung; Fragestellung als Ein-Satz-Fragen; Antworten als … |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `antworten-interessen-ausfuehrungen-fragen` | Antworten Interessen Ausfuehrungen Fragen im Memorandum-Erstellung: prüft konkret Antworten, Ausfuehrungen, Fragen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `due-diligence-ergebnis-handlungsempfehlung` | DUE Diligence Ergebnis Handlungsempfehlung im Memorandum-Erstellung: prüft konkret Memo Rechtsteil einer Due Diligence, Ergebnis und Handlungsempfehlung trennen, Memo fuer Mandanten unterscheidet sich vom internen Memo. Liefert priorisie... |
| `gliederung-mandantenunterlagen-memorandum` | Gliederung Mandantenunterlagen Memorandum im Memorandum-Erstellung: prüft konkret Gliederung, Mandantenunterlagen, Memorandum. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `haftungsrisiko-rechtsanwalt-board-pack` | Haftungsrisiko Rechtsanwalt Board Pack im Memorandum-Erstellung: prüft konkret Internes Memo zur Haftungspruefung, Spezialfall Memo als Bestandteil eines Board-Packs, Internes Compliance-Vorfall-Memo. Liefert priorisierten Output mit Nor... |
| `juristisches-questions-fristennotiz` | Juristisches Questions Fristennotiz im Memorandum-Erstellung: prüft konkret Juristisches, Questions, Vertragsentscheidungs-Memo. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `laenge-formate-mandantenfreundliche-fassung` | Laenge Formate Mandantenfreundliche Fassung im Memorandum-Erstellung: prüft konkret Memo-Laenge an Komplexitaet anpassen, Spezialfall mandantenfreundliche Fassung eines juristischen, Bauleiter Memo-Typen. Liefert priorisierten Output mit... |
| `mandantenanfrage-schnell` | Mandantenanfrage Schnell im Memorandum-Erstellung: prüft konkret Schnell-Memo zu eingehender Mandantenanfrage, Rechtsmittel-Memo, Erstellt ein professionelles juristisches Memorandum aus. Liefert priorisierten Output mit Norm-Pinpoints,... |
| `memo-zitierung-mandantenkommunikation-entscheidungsvorlage` | Memo Zitierung Mandantenkommunikation Entscheidungsvorlage im Memorandum-Erstellung: fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |
| `memorandums-ersteller-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `memorandums-ersteller-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `memorandums-ersteller-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `memorandums-ersteller-mandantenkommunikation-redteam` | Mandantenkommunikation Redteam im Memorandum-Erstellung: prüft konkret Mandantenkommunikation im Plugin memorandums-ersteller, Red-Team Qualitygate im Plugin memorandums-ersteller, Fristen und Sofortmassnahmen vor dem juristischen Inhalt... |
| `memorandums-ersteller-output-waehlen` | Output wählen im Memorandum-Erstellung: Diese Output-Weiche für Memorandums Ersteller entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `memorandums-ersteller-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `memorandums-ersteller-start-chronologie-fristen` | Start Chronologie Fristen im Memorandum-Erstellung: prüft konkret Einstieg, Schnelltriage und Fallrouting im Memorandums, Chronologie und Belegmatrix im Plugin memorandums-ersteller, Fristen- und Risikoampel im Plugin memorandums-erstell... |
| `memorandums-ersteller-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `optional-beweislast-piercing-sonderfall` | Optional Beweislast Piercing Sonderfall im Memorandum-Erstellung: prüft konkret Optional, Piercing, Rechtliche. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `pinpoint-fehlerkatalog` | Pinpoint Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `prozessstrategie-klageerhebung-gutachtenstil` | Prozessstrategie Klageerhebung Gutachtenstil im Memorandum-Erstellung: prüft konkret Memo zur Prozessstrategie vor Klageerhebung, Pruefungsabschnitt im Gutachtenstil, Quellenzitate im Memo nach deutscher Hauszitierweise v4. Liefert prior... |
| `quellenreferenz-quellenkarte` | Quellenreferenz Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `rechtsfortbildung-bgh-rechtsfragen` | Rechtsfortbildung BGH Rechtsfragen im Memorandum-Erstellung: prüft konkret Memo zu aktueller BGH-Entscheidung, Rechtsfragen praezise formulieren, Leitfaden Research- und Quellen-Tracking fuer Memos. Liefert priorisierten Output mit Norm-... |
| `rechtsgebietsneutral-sachverhalt-satz` | Rechtsgebietsneutral Sachverhalt Satz im Memorandum-Erstellung: prüft konkret Rechtsgebietsneutral, Sachverhalt, Satz. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `sachverhalt-fixieren-vier-teile` | Sachverhalt Fixieren Vier Teile im Memorandum-Erstellung: prüft konkret Sachverhalt sauber fixieren, Vier-Teile-Memo aufbauen, Memo zu grenzueberschreitenden Faellen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächs... |
| `teile-vier-wandelt` | Teile Vier Wandelt im Memorandum-Erstellung: prüft konkret Teile, Vier, Wandelt. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
