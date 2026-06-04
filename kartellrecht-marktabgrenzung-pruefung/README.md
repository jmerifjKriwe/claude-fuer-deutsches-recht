# Kartellrecht — Marktabgrenzungsprüfung

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`kartellrecht-marktabgrenzung-pruefung`) | [`kartellrecht-marktabgrenzung-pruefung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kartellrecht-marktabgrenzung-pruefung.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Nordstern MedTech Vertrieb - Provision, Buchauszug und Ausgleich** (`handelsvertreterrecht-provisionsausgleich-nordstern-medtech`) | [Gesamt-PDF lesen](../testakten/handelsvertreterrecht-provisionsausgleich-nordstern-medtech/gesamt-pdf/handelsvertreterrecht-provisionsausgleich-nordstern-medtech_gesamt.pdf) | [`testakte-handelsvertreterrecht-provisionsausgleich-nordstern-medtech.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-handelsvertreterrecht-provisionsausgleich-nordstern-medtech.zip) |
| **Zusammenschlusskontrolle GBW / Tannenheim — Bahnbetonschwellen, Bußgeld, ECN+** (`kartell-zusammenschlusskontrolle-bahnbetonschwellen-grosskopf-westfalen`) | [Gesamt-PDF lesen](../testakten/kartell-zusammenschlusskontrolle-bahnbetonschwellen-grosskopf-westfalen/gesamt-pdf/kartell-zusammenschlusskontrolle-bahnbetonschwellen-grosskopf-westfalen_gesamt.pdf) | [`testakte-kartell-zusammenschlusskontrolle-bahnbetonschwellen-grosskopf-westfalen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kartell-zusammenschlusskontrolle-bahnbetonschwellen-grosskopf-westfalen.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Globales Kartellrechts- und Competition-Law-Plugin mit Marktabgrenzung als harter Kernachse: GWB, Art. 101 und Art. 102 AEUV, EU-Fusionskontrolle, Bundeskartellamt, DG Competition, FTC/DOJ, Dawn Raids, Leniency, Private Enforcement, sektorale Deep Dives und vorsichtige Jurisdiktionschecks weltweit.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Zweck

Dieses Prüfwerkzeug analysiert kartellrechtliche Fälle auf juristischer, ökonomischer und methodischer Ebene. Es unterstützt bei:

- **Fusionskontrolle:** FKVO-Verfahren Phase I/II, BKartA-Verfahren, SIEC-Test.
- **Missbrauchsverfahren:** Art. 102 AEUV / §§ 19–20 GWB; Marktbeherrschungsnachweis.
- **Kartellverbot:** Art. 101 AEUV / § 1 GWB; Spürbarkeit, Bagatell-Ausnahme.
- **Globalen Behördenverfahren:** BKartA, Europäische Kommission, FTC/DOJ und nationale Wettbewerbsbehörden mit Local-Counsel-Fragen.
- **Sektorfällen:** Cloud, KI-Foundation-Models, App Stores, AdTech, Pharma, Energie, Telekom, Zahlungsverkehr, Automotive, Logistik, Sport und öffentliche Beschaffung.
- **Behördliche Stellungnahmen:** Stellungnahmen in BKartA- und Kommissionsverfahren.
- **Parteigutachten:** Kritische Würdigung gegnerischer Marktdefinitionen.

## Referenzen

| Datei | Inhalt |
| --- | --- |
| `references/methodik-marktdefinition.md` | Umfassende Darstellung der Marktdefinitions-Methodik (SSNIP, Elastizitäten, Supply-Side, räumlicher Markt, Evidenz) |
| `references/eugh-leitentscheidungen.md` | Chronologische Entscheidungssammlung EuGH/EuG/BGH/BKartA mit Kernsätzen zur Marktdefinition |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Tragende Aussagen müssen vor der Ausgabe anhand amtlicher Normfassungen, Behördenquellen oder frei zugänglicher Rechtsprechung geprüft werden. Das Prüfwerkzeug ersetzt keine eigene anwaltliche Prüfung im Einzelfall. Kartellrechtliche Marktdefinitionen und Behördenzuständigkeiten sind fallabhängig und können sich nach Markt, Transaktionsstruktur und Jurisdiktion ändern.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 30 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `competition-global-kaltstart` | Global Competition Kaltstart: Spezialskill für großes Kartellrecht mit BKartA, DG Competition, FTC/DOJ und internationalen Behörden; prüft welche Jurisdiktionen, Produkte, Märkte, Umsätze, Behörden, Deadlines und Verfahrensarten sofort r... |
| `kartellrecht-kaltstart-mandat-neu` | Workflow zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Kartellrecht Kaltstart Mandat neu. |
| `kompendium-01-allgemein-bis-jurisdiktion-aserbai` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 01; bündelt 14 frühere Spezialskills (allgemein, workflow-anschluss-skills-router, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel, eugh-rechts... |
| `kompendium-02-jurisdiktion-austral-bis-jurisdiktion-china-c` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 02; bündelt 14 frühere Spezialskills (jurisdiktion-australien-competition-authority, jurisdiktion-bahrain-competition-authority, jurisdiktion-bangladesch-competition-... |
| `kompendium-03-jurisdiktion-costa-r-bis-jurisdiktion-grieche` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 03; bündelt 14 frühere Spezialskills (jurisdiktion-costa-rica-competition-authority, jurisdiktion-daenemark-competition-authority, jurisdiktion-deutschland-competitio... |
| `kompendium-04-jurisdiktion-guatema-bis-jurisdiktion-kanada` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 04; bündelt 14 frühere Spezialskills (jurisdiktion-guatemala-competition-authority, jurisdiktion-honduras-competition-authority, jurisdiktion-hongkong-competition-aut... |
| `kompendium-05-jurisdiktion-kasachs-bis-jurisdiktion-litauen` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 05; bündelt 14 frühere Spezialskills (jurisdiktion-kasachstan-competition-authority, jurisdiktion-katar-competition-authority, jurisdiktion-kenia-competition-authorit... |
| `kompendium-06-jurisdiktion-luxembu-bis-jurisdiktion-namibia` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 06; bündelt 14 frühere Spezialskills (jurisdiktion-luxemburg-competition-authority, jurisdiktion-macau-competition-authority, jurisdiktion-madagaskar-competition-auth... |
| `kompendium-07-jurisdiktion-nepal-c-bis-jurisdiktion-paragua` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 07; bündelt 14 frühere Spezialskills (jurisdiktion-nepal-competition-authority, jurisdiktion-neuseeland-competition-authority, jurisdiktion-nicaragua-competition-auth... |
| `kompendium-08-jurisdiktion-peru-co-bis-jurisdiktion-singapu` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 08; bündelt 14 frühere Spezialskills (jurisdiktion-peru-competition-authority, jurisdiktion-philippinen-competition-authority, jurisdiktion-polen-competition-authorit... |
| `kompendium-09-jurisdiktion-slowake-bis-jurisdiktion-ukraine` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 09; bündelt 14 frühere Spezialskills (jurisdiktion-slowakei-competition-authority, jurisdiktion-slowenien-competition-authority, jurisdiktion-spanien-competition-auth... |
| `kompendium-10-jurisdiktion-ungarn-bis-franchise-vertrag-ka` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 10; bündelt 14 frühere Spezialskills (jurisdiktion-ungarn-competition-authority, jurisdiktion-uruguay-competition-authority, jurisdiktion-usa-competition-authority, j... |
| `kompendium-11-kartellrechtliche-ve-bis-19-gwb-behinderungs` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 11; bündelt 14 frühere Spezialskills (kartellrechtliche-vertragsklausel-redline, bussgeldbemessung-unternehmen-verband, geschaeftsleiterhaftung-kartellverstoss, karte... |
| `kompendium-12-19a-gwb-ueberragende-bis-auswirkungen-marktan` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 12; bündelt 14 frühere Spezialskills (19a-gwb-ueberragende-marktuebergreifende-bedeutung, 20-gwb-relative-marktmacht, abuse-of-economic-dependence, algorithmic-collus... |
| `kompendium-13-bietergemeinschaft-v-bis-dma-schnittstelle-ka` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 13; bündelt 14 frühere Spezialskills (bietergemeinschaft-vergabekartellrecht, bka-dgcomp-ftc-doj-routing, cartel-settlement-procedure, competition-board-liability, co... |
| `kompendium-14-dma-und-gatekeeper-m-bis-fusionskontrolle-gwb` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 14; bündelt 14 frühere Spezialskills (dma-und-gatekeeper-markt, einkaufskooperation-nachfragemacht, einstweiliger-rechtsschutz-kartellrecht, elastizitaeten-diversion-... |
| `kompendium-15-fusionskontrolle-mod-bis-joint-venture-full-f` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 15; bündelt 14 frühere Spezialskills (fusionskontrolle-modus, geoblocking-und-kartellrecht-schnittstelle, gesamtbewertung-tragfaehigkeit, gun-jumping-global, handelsv... |
| `kompendium-16-kart-innovationswett-bis-market-definition-20` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 16; bündelt 14 frühere Spezialskills (kart-innovationswettbewerb-spezial, kart-marktanteilsanalyse-leitfaden, kart-marktdefinition-bauleiter, kart-zweiseitige-plattfo... |
| `kompendium-17-marktabgrenzung-kont-bis-presseverlage-plattf` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 17; bündelt 14 frühere Spezialskills (marktabgrenzung-kontextanalyse, mehrseitige-maerkte-plattformen, merger-remedies-global, ministererlaubnis-42-gwb, minority-shar... |
| `kompendium-18-private-enforcement-bis-sektor-adtech-und-di` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 18; bündelt 14 frühere Spezialskills (private-enforcement-damages-global, produktmarkt-angebotsumstellung, produktmarkt-nachfragesubstitution, public-procurement-bid-... |
| `kompendium-19-sektor-app-stores-mo-bis-selektivvertrieb-lux` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 19; bündelt 14 frühere Spezialskills (sektor-app-stores-mobile-oekosysteme, sektor-automotive-zulieferketten-und-oem, sektor-cloud-infrastruktur-hyperscaler, sektor-e... |
| `kompendium-20-self-preferencing-pl-bis-spezial-marktbeherrs` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 20; bündelt 14 frühere Spezialskills (self-preferencing-plattformen, sep-frand-kartellrecht, siec-test-eu-merger-control, siec-test-horizontale-fusion, spezial-aeuv-b... |
| `kompendium-21-spezial-paragraf-ris-bis-vertikal-gvo-2022-72` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 21; bündelt 14 frühere Spezialskills (spezial-paragraf-risikoampel-und-gegenargumente, spezial-raeumlicher-compliance-dokumentation-und-akte, spezial-ssnip-schriftsat... |
| `kompendium-22-vertikale-leitlinien-bis-vollzugsverbot-gun-j` | kartellrecht-marktabgrenzung-pruefung: Konsolidiertes Skill-Kompendium 22; bündelt 3 frühere Spezialskills (vertikale-leitlinien-eu-selektiver-vertrieb-plattformverbote, verweisung-art-4-9-22-fkvo, vollzugsverbot-gun-jumping) und bewahrt... |
| `spezial-nachfrage-livequellen-und-rechtsprechungscheck` | Nachfrage: Livequellen- und Rechtsprechungscheck im Plugin kartellrecht marktabgrenzung pruefung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin kartellrecht-marktabgrenzung-pruefung: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin kartellrecht-marktabgrenzung-pruefung: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin kartellrecht-marktabgrenzung-pruefung: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin kartellrecht-marktabgrenzung-pruefung: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin kartellrecht-marktabgrenzung-pruefung: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
