# Umweltrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`umweltrecht`) | [`umweltrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/umweltrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Märkische Reserve Süd — Batteriespeicher Brandenburg/Berlin** (`batteriespeicher-brandenburg-berlin-resilienz`) | [Gesamt-PDF lesen](../testakten/batteriespeicher-brandenburg-berlin-resilienz/gesamt-pdf/batteriespeicher-brandenburg-berlin-resilienz_gesamt.pdf) | [`testakte-batteriespeicher-brandenburg-berlin-resilienz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-batteriespeicher-brandenburg-berlin-resilienz.zip) |
| **Projekt Isarlicht — Kernfusion und Transrapid am Starnberger See** (`kernfusion-transrapid-starnberger-see`) | [Gesamt-PDF lesen](../testakten/kernfusion-transrapid-starnberger-see/gesamt-pdf/kernfusion-transrapid-starnberger-see_gesamt.pdf) | [`testakte-kernfusion-transrapid-starnberger-see.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kernfusion-transrapid-starnberger-see.zip) |
| **Akte Umweltrecht: Industrieanlage — Genehmigung, Emissionshandel, Altlast und Transaktion** (`umweltrecht-industrieanlage-genehmigung`) | [Gesamt-PDF lesen](../testakten/umweltrecht-industrieanlage-genehmigung/gesamt-pdf/umweltrecht-industrieanlage-genehmigung_gesamt.pdf) | [`testakte-umweltrecht-industrieanlage-genehmigung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-umweltrecht-industrieanlage-genehmigung.zip) |
| **Umweltverbandsakte Moorbach** (`umweltschutzverband-windpark-moorbach-umwrg`) | [Gesamt-PDF lesen](../testakten/umweltschutzverband-windpark-moorbach-umwrg/gesamt-pdf/umweltschutzverband-windpark-moorbach-umwrg_gesamt.pdf) | [`testakte-umweltschutzverband-windpark-moorbach-umwrg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-umweltschutzverband-windpark-moorbach-umwrg.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Vollständiger Umweltrechts-Assistent für Anlagenbetreiber, Verbände, Investoren, Kommunen und öffentliche Hand: Emissionshandel, Immissionsschutz, Abfall, Wasser, Boden, Naturschutz, Umweltinformation, Verfahren, Sanktionen und Transaktionen.

Dieses Plugin ist **vollständig freistehend**. Es erwartet keine anderen Plugins, keine externen Agenten und keine besonderen Repo-Dateien außerhalb seines eigenen Ordners. Wenn ein Anschluss an Register, Behördenportale, E-Mail, beA, Datenraum, Bank, GIS, Tabellen oder Kanzleisoftware fehlt, arbeitet es mit manuellen Uploads oder mit einem gekennzeichneten Simulationsmodus.

## Schnellstart

1. Plugin aktivieren oder die ZIP aus dem Release installieren.
2. Eine neue Sache mit `umweltrecht-kommandocenter` starten.
3. Mandant, Ziel, Frist, Dokumente und gewünschtes Ergebnis nennen.
4. Bei fehlenden Systemanschlüssen `Simulation` sagen; das Plugin erzeugt dann realistische Testdaten und erklärt, welche echte Schnittstelle später ersetzt werden müsste.
5. Am Ende immer das Qualitätstor ausgeben lassen: offene Annahmen, Fristen, Rechenprüfung, Anlagen, Zuständigkeiten und nächste Schritte.

## Enthaltene Skills

- `umweltrecht-kommandocenter` - Umweltrecht-Kommandocenter
- `umweltrecht-emissionshandel-tehg` - Emissionshandel und TEHG
- `umweltrecht-immissionsschutz-bimschg` - Immissionsschutz und BImSchG
- `umweltrecht-stoerfall-anlagen` - Störfall, Anlagenbetrieb und Betreiberpflichten
- `umweltrecht-abfall-circular-economy` - Abfallrecht und Circular Economy
- `umweltrecht-wasser-bodenschutz` - Wasser- und Bodenschutzrecht
- `umweltrecht-naturschutz-artenschutz` - Naturschutz und Artenschutz
- `umweltrecht-umweltinformation-uig-ifg` - Umweltinformation nach UIG und IFG
- `umweltrecht-verfahren` - Umweltrechtliche Verwaltungs- und Gerichtsverfahren
- `umweltrecht-bussgeld-sanktionen` - Bußgeld, Sanktionen und Anhörung
- `umweltrecht-transaktionen-dd` - Umweltrechtliche Transaktions-Due-Diligence
- `umweltrecht-compliance-schulung` - Compliance, Beauftragte und Schulung
- `klimaklagen-verbandsklage-umwrg` - Klimaklagen, Verbandsklage UmwRG, EGMR Klima-Seniorinnen
- `lksg-csddd-lieferkettensorgfalt` - Lieferkettensorgfalt LkSG und CSDDD-Richtlinie (EU) 2024/1760
- `esg-greenwashing-csrd` - ESG-Greenwashing, CSRD-Umsetzung, ESRS, UWG-Werbung

## Vorlagen

- `assets/templates/umwelt-mandatskarte.md` - Umweltrecht-Mandatskarte
- `assets/templates/tehg-zuteilung-check.md` - TEHG-Zuteilungs- und Sanktionscheck
- `assets/templates/bimschg-genehmigungsfahrplan.md` - BImSchG-Genehmigungsfahrplan
- `assets/templates/stoerfall-anlagenmatrix.md` - Störfall- und Anlagenpflichtenmatrix
- `assets/templates/abfall-circular-matrix.md` - Abfall- und Circular-Economy-Matrix
- `assets/templates/wasser-boden-pruefplan.md` - Wasser- und Boden-Prüfplan
- `assets/templates/naturschutz-artenschutz-check.md` - Naturschutz- und Artenschutzcheck
- `assets/templates/uig-ifg-verfahren.md` - UIG/IFG-Verfahrenskarte
- `assets/templates/umweltverfahren-fristen.md` - Umwelt-Verfahrens- und Fristenplan
- `assets/templates/bussgeld-verteidigungsplan.md` - Bußgeld-Verteidigungsplan Umwelt
- `assets/templates/umwelt-dd-grid.md` - Umwelt-DD-Grid
- `assets/templates/schulung-beauftragte-plan.md` - Schulungs- und Beauftragtenplan

## Freistehende Leitplanken

- Keine stillen Verweise auf andere Plugins.
- Keine produktive Rechtsberatung ohne anwaltliche Prüfung.
- Keine echten Mandatsgeheimnisse in ungeprüfte Cloud- oder KI-Umgebungen.
- Keine erfundenen Fundstellen; unsichere Normen und Rechtsprechung werden als Prüfbedarf markiert.
- Zahlen, Fristen, Schwellenwerte und Zuständigkeiten werden sichtbar hergeleitet oder als Annahme gekennzeichnet.
- Ausgabe immer so, dass eine Berufsträgerin oder ein Berufsträger sie sofort prüfen, kürzen, freigeben oder verwerfen kann.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | umweltrecht: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-02-workflow-mandantenko-bis-spezial-stoerfall-fr` | umweltrecht: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-mandantenkommunikation, workflow-redteam-qualitygate, spezial-stoerfall-fristennotiz-und-naechster-schritt) und bewahrt deren Workflows, Normanker... |
| `kompendium-03-spezial-tehg-fristen-bis-umweltrecht-verfahre` | umweltrecht: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (spezial-tehg-fristen-form-und-zustaendigkeit, spezial-verfahren-verhandlung-vergleich-und-eskalation, umweltrecht-verfahren) und bewahrt deren Workflows, N... |
| `kompendium-04-umweltrecht-bussgeld-bis-uwr-emissionshandel` | umweltrecht: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (umweltrecht-bussgeld-sanktionen, umweltrecht-emissionshandel-tehg, uwr-emissionshandel-ets-spezial) und bewahrt deren Workflows, Normanker, Prüfprogramme u... |
| `kompendium-05-esg-greenwashing-csr-bis-lksg-csddd-lieferket` | umweltrecht: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (esg-greenwashing-csrd, klimaklagen-verbandsklage-umwrg, lksg-csddd-lieferkettensorgfalt) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabem... |
| `kompendium-06-spezial-abfall-dokum-bis-spezial-bimschg-tatb` | umweltrecht: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (spezial-abfall-dokumentenmatrix-und-lueckenliste, spezial-anlagen-abschlussprodukt-und-uebergabe, spezial-bimschg-tatbestand-beweis-und-belege) und bewahrt... |
| `kompendium-07-spezial-boden-behoer-bis-spezial-csrd-sonderf` | umweltrecht: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (spezial-boden-behoerden-gericht-und-registerweg, spezial-csddd-mandantenkommunikation-entscheidungsvorlage, spezial-csrd-sonderfall-und-edge-case) und bewa... |
| `kompendium-08-spezial-diligence-co-bis-spezial-klimaklagen` | umweltrecht: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (spezial-diligence-compliance-dokumentation-und-akte, spezial-greenwashing-beweislast-und-darlegungslast, spezial-klimaklagen-mehrparteien-konflikt-und-inte... |
| `kompendium-09-spezial-lieferketten-bis-spezial-naturschutz` | umweltrecht: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (spezial-lieferkettensorgfalt-formular-portal-und-einreichung, spezial-lksg-red-team-und-qualitaetskontrolle, spezial-naturschutz-schriftsatz-brief-und-memo... |
| `kompendium-10-spezial-umwelt-zahle-bis-spezial-umwrg-intern` | umweltrecht: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (spezial-umwelt-zahlen-schwellen-und-berechnung, spezial-umweltrecht-erstpruefung-und-mandatsziel, spezial-umwrg-internationaler-bezug-und-schnittstellen) u... |
| `kompendium-11-spezial-wasser-risik-bis-umweltrecht-complian` | umweltrecht: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (spezial-wasser-risikoampel-und-gegenargumente, umweltrecht-abfall-circular-economy, umweltrecht-compliance-schulung) und bewahrt deren Workflows, Normanker... |
| `kompendium-12-umweltrecht-immissio-bis-umweltrecht-natursch` | umweltrecht: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (umweltrecht-immissionsschutz-bimschg, umweltrecht-kommandocenter, umweltrecht-naturschutz-artenschutz) und bewahrt deren Workflows, Normanker, Prüfprogramm... |
| `kompendium-13-umweltrecht-stoerfal-bis-umweltrecht-umweltin` | umweltrecht: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (umweltrecht-stoerfall-anlagen, umweltrecht-transaktionen-dd, umweltrecht-umweltinformation-uig-ifg) und bewahrt deren Workflows, Normanker, Prüfprogramme u... |
| `kompendium-14-umweltrecht-wasser-b-bis-uwr-bimschg-genehmig` | umweltrecht: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (umweltrecht-wasser-bodenschutz, uwr-altlasten-pruefung-spezial, uwr-bimschg-genehmigung-bauleiter) und bewahrt deren Workflows, Normanker, Prüfprogramme un... |
| `kompendium-15-uwr-bundesnaturschut-bis-uwr-immissionsschutz` | umweltrecht: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (uwr-bundesnaturschutzgesetz-eingriff-spezial, uwr-co2-emissionshandel-spezial, uwr-immissionsschutz-praxis) und bewahrt deren Workflows, Normanker, Prüfpro... |
| `kompendium-16-uwr-wasserrechtliche-bis-uwr-wasserrechtliche` | umweltrecht: Konsolidiertes Skill-Kompendium 16; bündelt 1 frühere Spezialskills (uwr-wasserrechtliche-erlaubnis-leitfaden) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-bussgeld-livequellen-und-rechtsprechungscheck` | Bussgeld: Livequellen- und Rechtsprechungscheck im Plugin umweltrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `uwr-einfuehrung-rechtsquellen` | Umweltrecht einfuehrend: BImSchG, BNatSchG, WHG, KrWG, BBodSchG, USchadG, EU-IED, REACH. Pro Norm Anwendungsbereich, Aufsicht, typische Mandantenfragen. Entscheidungstabelle. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin umweltrecht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin umweltrecht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin umweltrecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin umweltrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin umweltrecht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin umweltrecht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
