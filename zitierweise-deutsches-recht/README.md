# Zitierweise deutsches Recht (v4.1)

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`zitierweise-deutsches-recht`) | [`zitierweise-deutsches-recht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/zitierweise-deutsches-recht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Dr. Ottilie Mondsee und die verschwundene R-Besoldung** (`beamtenrecht-richterlaufbahn-besoldung-mondsee`) | [Gesamt-PDF lesen](../testakten/beamtenrecht-richterlaufbahn-besoldung-mondsee/gesamt-pdf/beamtenrecht-richterlaufbahn-besoldung-mondsee_gesamt.pdf) | [`testakte-beamtenrecht-richterlaufbahn-besoldung-mondsee.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-beamtenrecht-richterlaufbahn-besoldung-mondsee.zip) |
| **Zitierweise-Pruefkorpus — Kanzlei Roosendaal Birkenhainer Partners mbB — Kanzleihandbuch v4 mit 100 Fundstellen und Pruefvermerken** (`zitierweise-pruefkorpus-roosendaal-kanzleihandbuch-mit-100-fundstellen-und-pruefvermerken`) | [Gesamt-PDF lesen](../testakten/zitierweise-pruefkorpus-roosendaal-kanzleihandbuch-mit-100-fundstellen-und-pruefvermerken/gesamt-pdf/zitierweise-pruefkorpus-roosendaal-kanzleihandbuch-mit-100-fundstellen-und-pruefvermerken_gesamt.pdf) | [`testakte-zitierweise-pruefkorpus-roosendaal-kanzleihandbuch-mit-100-fundstellen-und-pruefvermerken.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-zitierweise-pruefkorpus-roosendaal-kanzleihandbuch-mit-100-fundstellen-und-pruefvermerken.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Deutsche juristische Hauszitierweise als zuschaltbares Plugin. Fokus: belastbare, überprüfbare Quellen statt schöner, aber nicht verifizierbarer Fundstellen.

## Was ist neu in v4.1

1. **BeckRS-Sperre:** BeckRS-Fundstellen werden nicht mehr aus Modellwissen erzeugt. Sie dürfen nur übernommen werden, wenn der Nutzer sie liefert oder ein lizenzierter Live-Zugriff sie verifiziert.
2. **Literatur-Sperre:** Kommentare, Handbücher, Monographien und Aufsätze werden nicht blind zitiert. Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
3. **Rechtsprechungs-Mindeststandard:** Gericht, Entscheidungsform, Datum und Aktenzeichen sind Pflicht. Wo möglich kommt eine amtliche oder frei zugängliche Quelle dazu.
4. **Keine Palandt-/Pahlen-Aktualzitate:** Der frühere Palandt heißt seit 2022 Grüneberg; historische Altauflagen nur bei konkreter Nutzerquelle.
5. **Prüfvermerk statt Halluzination:** Unverifizierte Entscheidungen werden markiert oder weggelassen, nicht ausgeschmückt.

## Installation in Claude Code

1. ZIP herunterladen.
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/` und `references/` im ZIP-Root enthalten. Nicht das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Routing: klärt, ob ein Text Zitate erzeugen, glätten, prüfen oder sperren soll. |
| `zitierweise-anwenden` | Wendet die Quellenregel v4.1 an: Rechtsprechung nur mit Datum, Aktenzeichen und verifizierbarer Quelle; keine BeckRS-, Kommentar- oder Aufsatz-Blindzitate. |

## Kurzregel

Norm zuerst. Dann verifizierte Rechtsprechung. Literatur nur bei bereitgestellter oder live verifizierter Quelle. Keine BeckRS-, Kommentar- oder Aufsatz-Blindzitate.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | zitierweise-deutsches-recht: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme un... |
| `kompendium-02-workflow-mandantenko-bis-spezial-paywallfreie` | zitierweise-deutsches-recht: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-mandantenkommunikation, workflow-redteam-qualitygate, spezial-paywallfreie-rechtsprechungsbelege) und bewahrt deren Workflows, Nor... |
| `kompendium-03-spezial-rechtsprechu-bis-zitat-eugh-rechtspre` | zitierweise-deutsches-recht: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (spezial-rechtsprechung-fristen-form-und-zustaendigkeit, zit-rechtsprechungszitierung-leitfaden, zitat-eugh-rechtsprechung) und bewahrt dere... |
| `kompendium-04-zitat-rechtsprechung-bis-spezial-aktenzeichen` | zitierweise-deutsches-recht: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (zitat-rechtsprechung-ohne-fundstelle, spezial-zitierweise-fristennotiz-und-naechster-schritt, spezial-aktenzeichen-schriftsatz-brief-und-me... |
| `kompendium-05-spezial-aufsatz-mehr-bis-spezial-blindzitate` | zitierweise-deutsches-recht: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (spezial-aufsatz-mehrparteien-konflikt-und-interessen, spezial-beckrs-zahlen-schwellen-und-berechnung, spezial-blindzitate-internationaler-b... |
| `kompendium-06-spezial-datum-behoer-bis-spezial-gericht-doku` | zitierweise-deutsches-recht: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (spezial-datum-behoerden-gericht-und-registerweg, spezial-entscheidungsform-risikoampel-und-gegenargumente, spezial-gericht-dokumentenmatrix... |
| `kompendium-07-spezial-hauszitierwe-bis-spezial-kommentar-co` | zitierweise-deutsches-recht: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (spezial-hauszitierweise-tatbestand-beweis-und-belege, spezial-juristische-erstpruefung-und-mandatsziel, spezial-kommentar-compliance-dokume... |
| `kompendium-08-spezial-literatur-fo-bis-spezial-lizenziertem` | zitierweise-deutsches-recht: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (spezial-literatur-formular-portal-und-einreichung, spezial-live-beweislast-und-darlegungslast, spezial-lizenziertem-mandantenkommunikation-... |
| `kompendium-09-spezial-verifizierba-bis-zit-gesetzeszitierun` | zitierweise-deutsches-recht: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (spezial-verifizierbarer-verhandlung-vergleich-und-eskalation, spezial-zugriff-sonderfall-und-edge-case, zit-gesetzeszitierung-bauleiter) un... |
| `kompendium-10-zit-internationale-u-bis-zitat-amtliche-samml` | zitierweise-deutsches-recht: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (zit-internationale-urteile-spezial, zit-kommentar-aufsatzzitierung-spezial, zitat-amtliche-sammlung-vs-zeitschrift) und bewahrt deren Workf... |
| `kompendium-11-zitat-archivierungsp-bis-zitat-bag-bfh-bsg-ba` | zitierweise-deutsches-recht: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (zitat-archivierungspflicht, zitat-aufsatz-zeitschrift, zitat-bag-bfh-bsg-bag) und bewahrt deren Workflows, Normanker, Prüfprogramme und Aus... |
| `kompendium-12-zitat-bgh-entscheidu-bis-zitat-gesetz-verordn` | zitierweise-deutsches-recht: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (zitat-bgh-entscheidung, zitat-bverfg-entscheidung, zitat-gesetz-verordnung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausga... |
| `kompendium-13-zitat-haus-zitierreg-bis-zitat-internationale` | zitierweise-deutsches-recht: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (zitat-haus-zitierregel-anpassen, zitat-instanzgerichte-strategisch, zitat-internationale-quellen) und bewahrt deren Workflows, Normanker, P... |
| `kompendium-14-zitat-internet-quell-bis-zitat-leitsatzentsch` | zitierweise-deutsches-recht: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (zitat-internet-quellen, zitat-kommentar-randnummer, zitat-leitsatzentscheidung) und bewahrt deren Workflows, Normanker, Prüfprogramme und A... |
| `kompendium-15-zitat-monografie-han-bis-zitat-verboten-anwal` | zitierweise-deutsches-recht: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (zitat-monografie-handbuch, zitat-streitstand-darstellen, zitat-verboten-anwalt24-beckrs) und bewahrt deren Workflows, Normanker, Prüfprogra... |
| `kompendium-16-zitierweise-anwenden-bis-zitierweise-anwenden` | zitierweise-deutsches-recht: Konsolidiertes Skill-Kompendium 16; bündelt 1 frühere Spezialskills (zitierweise-anwenden) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-nutzerquelle-red-team-und-qualitaetskontrolle` | Nutzerquelle: Red-Team und Qualitätskontrolle im Plugin zitierweise deutsches recht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-quelle-livequellen-und-rechtsprechungscheck` | Quelle: Livequellen- und Rechtsprechungscheck im Plugin zitierweise deutsches recht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin zitierweise-deutsches-recht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin zitierweise-deutsches-recht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin zitierweise-deutsches-recht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin zitierweise-deutsches-recht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin zitierweise-deutsches-recht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin zitierweise-deutsches-recht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
