# Barrierefreiheit Web Checker

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`barrierefreiheit-web-checker`) | [`barrierefreiheit-web-checker.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/barrierefreiheit-web-checker.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **BFSG-Verstoß Tannenkamp Mode-Versand GmbH — Online-Shop Barrierefreiheit Osnabrück** (`bfsg-online-shop-tannenkamp-mode-versand-osnabrueck`) | [Gesamt-PDF lesen](../testakten/bfsg-online-shop-tannenkamp-mode-versand-osnabrueck/gesamt-pdf/bfsg-online-shop-tannenkamp-mode-versand-osnabrueck_gesamt.pdf) | [`testakte-bfsg-online-shop-tannenkamp-mode-versand-osnabrueck.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bfsg-online-shop-tannenkamp-mode-versand-osnabrueck.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Prüf- und Dokumentationsplugin für digitale Barrierefreiheit von Websites, Webshops, Portalen, Apps und eingebetteten Dokumenten. Es verbindet den rechtlichen Scope-Check mit praktischer Webprüfung: BFSG/BFSGV, BITV 2.0, Web Accessibility Directive, European Accessibility Act, EN 301 549, WCAG, Tastaturbedienung, Screenreader, Formulare, Checkout, PDFs, Barrierefreiheitserklärung und Remediation-Roadmap.

## Was das Plugin gut kann

- Ermitteln, ob eine Website öffentlich-rechtlich, BFSG-relevant, rein intern oder freiwillig zu prüfen ist.
- Einen Audit nach EN 301 549/WCAG-Prüflogik vorbereiten und dokumentieren.
- Tastatur, Fokus, Semantik, Screenreader, Kontrast, Formulare, Checkout und Downloads prüfen.
- Barrierefreiheitserklärung, Feedbackmechanismus und Maßnahmenplan formulieren.
- Agenturen, Entwicklerteams und Compliance-Verantwortliche mit klaren Abnahmekriterien führen.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `allgemein` | Kaltstart, Scope, Ziel, Rolle, Prüfobjekt und Workflow-Routing. |
| `scope-bfsg-bitv-wad` | Prüft, welcher Rechtsrahmen einschlägig ist: BFSG/BFSGV, BITV 2.0, EU-WAD, freiwilliger Standard. |
| `en301549-wcag-pruefplan` | Baut einen Prüfkatalog nach EN 301 549 und WCAG mit A/AA-Prioritäten. |
| `automatisierter-audit-axe-lighthouse` | Ordnet automatisierte Checks ein und warnt vor falscher Sicherheit. |
| `tastatur-fokus-navigation` | Prüft Tastaturbedienbarkeit, Fokusreihenfolge, Skiplinks, Menüs, Modale und Overlays. |
| `screenreader-semantik-aria` | Prüft Struktur, HTML-Semantik, Labels, ARIA, Überschriften, Live-Regionen und Fehlermeldungen. |
| `kontrast-farbe-motion-responsive` | Prüft Kontrast, Farbe ohne Farbcodierung, Reflow, Zoom, Animationen und Bewegung. |
| `formulare-checkout-ecommerce` | Prüft Webshop, Login, Warenkorb, Checkout, Fehlertexte, Zahlung und elektronische Verträge. |
| `pdf-downloads-dokumente` | Prüft PDFs, Downloads, eingebettete Dokumente und Alternativen. |
| `erklaerung-feedback-durchsetzung` | Erstellt Barrierefreiheitserklärung, Feedbackweg und Behörden-/Marktüberwachungsreaktion. |
| `remediation-roadmap-dokumentation` | Baut Maßnahmenplan, Priorisierung, Nachweise, Risikoampel und Re-Test-Protokoll. |
| `agentur-abnahme-vergabe` | Formuliert Lastenheft, Abnahmekriterien und Nachbesserungsanforderungen an Agenturen. |

## Quellenstand

Stand: Mai 2026. Rechtsprechung und Behördenpraxis werden nicht aus Modellwissen zitiert. Technische Standards ändern sich; insbesondere ist zwischen fachlich sinnvoller WCAG-2.2-Prüfung und rechtlich harmonisierten EN-301-549-Anforderungen zu unterscheiden.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | barrierefreiheit-web-checker: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme u... |
| `kompendium-02-workflow-mandantenko-bis-erklaerung-feedback` | barrierefreiheit-web-checker: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-mandantenkommunikation, workflow-redteam-qualitygate, erklaerung-feedback-durchsetzung) und bewahrt deren Workflows, Normanker, P... |
| `kompendium-03-spezial-bfsgv-friste-bis-agentur-abnahme-verg` | barrierefreiheit-web-checker: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (spezial-bfsgv-fristen-form-und-zustaendigkeit, spezial-schulung-fristennotiz-und-naechster-schritt, agentur-abnahme-vergabe) und bewahrt d... |
| `kompendium-04-pdf-formulare-und-fo-bis-bf-kanzleiwebsite-ko` | barrierefreiheit-web-checker: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (pdf-formulare-und-formulare-barrierefrei, automatisierter-audit-axe-lighthouse, bf-kanzleiwebsite-konkret) und bewahrt deren Workflows, No... |
| `kompendium-05-bf-kiosk-und-selbstb-bis-bf-pdf-schriftsaetze` | barrierefreiheit-web-checker: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (bf-kiosk-und-selbstbedienung-spezial, bf-mediendienste-untertitel-spezial, bf-pdf-schriftsaetze-versand) und bewahrt deren Workflows, Norm... |
| `kompendium-06-bfsg-zeitleiste-und-bis-en301549-wcag-pruefp` | barrierefreiheit-web-checker: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (bfsg-zeitleiste-und-pflichten, ecommerce-checkout-pruefung-spezial, en301549-wcag-pruefplan) und bewahrt deren Workflows, Normanker, Prüfp... |
| `kompendium-07-formulare-checkout-e-bis-native-apps-ios-andr` | barrierefreiheit-web-checker: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (formulare-checkout-ecommerce, kontrast-farbe-motion-responsive, native-apps-ios-android-pruefung) und bewahrt deren Workflows, Normanker,... |
| `kompendium-08-pdf-downloads-dokume-bis-schulung-und-rolle-a` | barrierefreiheit-web-checker: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (pdf-downloads-dokumente, remediation-roadmap-dokumentation, schulung-und-rolle-accessibility-champion) und bewahrt deren Workflows, Norman... |
| `kompendium-09-scope-bfsg-bitv-wad-bis-spezial-abnahme-form` | barrierefreiheit-web-checker: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (scope-bfsg-bitv-wad, screenreader-semantik-aria, spezial-abnahme-formular-portal-und-einreichung) und bewahrt deren Workflows, Normanker,... |
| `kompendium-10-spezial-audit-schrif-bis-spezial-bfsg-tatbest` | barrierefreiheit-web-checker: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (spezial-audit-schriftsatz-brief-und-memo-bausteine, spezial-barrierefreiheits-erstpruefung-und-mandatsziel, spezial-bfsg-tatbestand-beweis... |
| `kompendium-11-spezial-bitv-dokumen-bis-spezial-ecommerce-ma` | barrierefreiheit-web-checker: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (spezial-bitv-dokumentenmatrix-und-lueckenliste, spezial-checkout-beweislast-und-darlegungslast, spezial-ecommerce-mandantenkommunikation-e... |
| `kompendium-12-spezial-erklaerung-m-bis-spezial-pdfs-complia` | barrierefreiheit-web-checker: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (spezial-erklaerung-mehrparteien-konflikt-und-interessen, spezial-formulare-zahlen-schwellen-und-berechnung, spezial-pdfs-compliance-dokume... |
| `kompendium-13-spezial-pruefung-son-bis-spezial-rolle-abschl` | barrierefreiheit-web-checker: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (spezial-pruefung-sonderfall-und-edge-case, spezial-roadmap-internationaler-bezug-und-schnittstellen, spezial-rolle-abschlussprodukt-und-ue... |
| `kompendium-14-spezial-scope-behoer-bis-spezial-wcag-risikoa` | barrierefreiheit-web-checker: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (spezial-scope-behoerden-gericht-und-registerweg, spezial-tastatur-verhandlung-vergleich-und-eskalation, spezial-wcag-risikoampel-und-gegen... |
| `kompendium-15-tastatur-fokus-navig-bis-usability-test-mit-b` | barrierefreiheit-web-checker: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (tastatur-fokus-navigation, ueberwachungsstelle-und-rechtsfolgen, usability-test-mit-betroffenen) und bewahrt deren Workflows, Normanker, P... |
| `kompendium-16-wcag-vs-en-301-549-m-bis-wcag-vs-en-301-549-m` | barrierefreiheit-web-checker: Konsolidiertes Skill-Kompendium 16; bündelt 1 frühere Spezialskills (wcag-vs-en-301-549-mapping) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-barrierefreiheit-red-team-und-qualitaetskontrolle` | Barrierefreiheit: Red-Team und Qualitätskontrolle im Plugin barrierefreiheit web checker; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-screenreader-livequellen-und-rechtsprechungscheck` | Screenreader: Livequellen- und Rechtsprechungscheck im Plugin barrierefreiheit web checker; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin barrierefreiheit-web-checker: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin barrierefreiheit-web-checker: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin barrierefreiheit-web-checker: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin barrierefreiheit-web-checker: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin barrierefreiheit-web-checker: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin barrierefreiheit-web-checker: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
