# Energierecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`energierecht`) | [`energierecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/energierecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Märkische Reserve Süd — Batteriespeicher Brandenburg/Berlin** (`batteriespeicher-brandenburg-berlin-resilienz`) | [Gesamt-PDF lesen](../testakten/batteriespeicher-brandenburg-berlin-resilienz/gesamt-pdf/batteriespeicher-brandenburg-berlin-resilienz_gesamt.pdf) | [`testakte-batteriespeicher-brandenburg-berlin-resilienz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-batteriespeicher-brandenburg-berlin-resilienz.zip) |
| **Akte Energierecht: Stadtwerke Klotzkette AG – Quartier Hafenbogen** (`energierecht-stadtwerke-quartier`) | [Gesamt-PDF lesen](../testakten/energierecht-stadtwerke-quartier/gesamt-pdf/energierecht-stadtwerke-quartier_gesamt.pdf) | [`testakte-energierecht-stadtwerke-quartier.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-energierecht-stadtwerke-quartier.zip) |
| **Projekt Isarlicht — Kernfusion und Transrapid am Starnberger See** (`kernfusion-transrapid-starnberger-see`) | [Gesamt-PDF lesen](../testakten/kernfusion-transrapid-starnberger-see/gesamt-pdf/kernfusion-transrapid-starnberger-see_gesamt.pdf) | [`testakte-kernfusion-transrapid-starnberger-see.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kernfusion-transrapid-starnberger-see.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Vollständiger Energierechts-Assistent für Stadtwerke, Energieversorger, Wärmewirtschaft, energieintensive Unternehmen, Immobilienwirtschaft, Infrastrukturbetreiber, Contracting, Wasserstoff, E-Mobility, Transaktionen und Projektfinanzierung.

Dieses Plugin ist **vollständig freistehend**. Es erwartet keine anderen Plugins, keine externen Agenten und keine besonderen Repo-Dateien außerhalb seines eigenen Ordners. Wenn ein Anschluss an Register, Behördenportale, E-Mail, beA, Datenraum, Bank, GIS, Tabellen oder Kanzleisoftware fehlt, arbeitet es mit manuellen Uploads oder mit einem gekennzeichneten Simulationsmodus.

## Schnellstart

1. Plugin aktivieren oder die ZIP aus dem Release installieren.
2. Eine neue Sache mit `energierecht-kommandocenter` starten.
3. Mandant, Ziel, Frist, Dokumente und gewünschtes Ergebnis nennen.
4. Bei fehlenden Systemanschlüssen `Simulation` sagen; das Plugin erzeugt dann realistische Testdaten und erklärt, welche echte Schnittstelle später ersetzt werden müsste.
5. Am Ende immer das Qualitätstor ausgeben lassen: offene Annahmen, Fristen, Rechenprüfung, Anlagen, Zuständigkeiten und nächste Schritte.

## Enthaltene Skills

- `energierecht-kommandocenter` - Energierecht-Kommandocenter
- `energierecht-infrastrukturprojekte` - Energieinfrastrukturprojekte
- `energierecht-netz-speicher-zugang` - Netz-, Speicher- und Anschlussregulierung
- `energierecht-energievertraege` - Energieverträge
- `energierecht-vertrieb-marktrollen` - Energievertrieb und Marktrollen
- `energierecht-industriekunden` - Industriekunden und Kostenoptimierung
- `energierecht-eeg-kwkg-erzeugung` - EEG, KWKG und Erzeugung
- `energierecht-waerme-quartier` - Wärme, Quartier und Fernwärme
- `energierecht-emobility-wasserstoff` - E-Mobility, Wasserstoff und Power-to-Gas
- `energierecht-wettbewerb` - Energie und Wettbewerb
- `energierecht-verfahren` - Verwaltungs- und Gerichtsverfahren Energie
- `energierecht-transaktionen-dd` - Energierechtliche Transaktions-Due-Diligence
- `energierecht-projektfinanzierung` - Erneuerbare-Energien-Projektfinanzierung

## Vorlagen

- `assets/templates/energie-mandatskarte.md` - Energierecht-Mandatskarte
- `assets/templates/energie-projektphasenplan.md` - Projektphasenplan Energieinfrastruktur
- `assets/templates/netzanschluss-zugangsmatrix.md` - Netzanschluss- und Zugangsmatrix
- `assets/templates/energieliefervertrag-check.md` - Energieliefervertrag-Check
- `assets/templates/waerme-quartier-playbook.md` - Wärme- und Quartiers-Playbook
- `assets/templates/industrie-umlagen-check.md` - Industrie-Umlagen- und Entlastungscheck
- `assets/templates/eeg-kwkg-foerdermatrix.md` - EEG/KWKG-Fördermatrix
- `assets/templates/vertrieb-marktrollen-map.md` - Vertrieb- und Marktrollenkarte
- `assets/templates/transaktions-dd-energielaw.md` - Energierechtliche DD-Matrix
- `assets/templates/verwaltungsverfahren-energie.md` - Energie-Verfahrensplan
- `assets/templates/wasserstoff-ptg-check.md` - Wasserstoff- und Power-to-Gas-Check
- `assets/templates/energie-wettbewerb-uwg-kartell.md` - Energie-Wettbewerbscheck

## Freistehende Leitplanken

- Keine stillen Verweise auf andere Plugins.
- Keine produktive Rechtsberatung ohne anwaltliche Prüfung.
- Keine echten Mandatsgeheimnisse in ungeprüfte Cloud- oder KI-Umgebungen.
- Keine erfundenen Fundstellen; unsichere Normen und Rechtsprechung werden als Prüfbedarf markiert.
- Zahlen, Fristen, Schwellenwerte und Zuständigkeiten werden sichtbar hergeleitet oder als Annahme gekennzeichnet.
- Ausgabe immer so, dass eine Berufsträgerin oder ein Berufsträger sie sofort prüfen, kürzen, freigeben oder verwerfen kann.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 29 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `er-bess-kaltstart-projektaufnahme` | Batteriespeicherprojekt aufnehmen: Projektgröße, Standort, Netzebene, Betreiberrolle, Fristen, Unterlagen und Zieloutput. |
| `er-fusion-kaltstart-regulierungsweg` | Ordnet Fusionsreaktor-Projekt zwischen Atomrecht, Strahlenschutz, Baurecht, Immissionsschutz und Forschungsförderung. |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | energierecht: Konsolidiertes Skill-Kompendium 01; bündelt 4 frühere Spezialskills (allgemein, workflow-anschluss-skills-router, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanke... |
| `kompendium-02-workflow-mandantenko-bis-energierecht-verfahr` | energierecht: Konsolidiertes Skill-Kompendium 02; bündelt 4 frühere Spezialskills (workflow-mandantenkommunikation, workflow-output-waehlen, workflow-redteam-qualitygate, energierecht-verfahren) und bewahrt deren Workflows, Normanker, Pr... |
| `kompendium-03-spezial-livecheck-fr-bis-ppa-cppa-vertragsspe` | energierecht: Konsolidiertes Skill-Kompendium 03; bündelt 4 frühere Spezialskills (spezial-livecheck-fristennotiz-und-naechster-schritt, spezial-versorger-fristen-form-und-zustaendigkeit, ladeinfrastruktur-spezial-vertragskette, ppa-cppa... |
| `kompendium-04-er-bess-produktsiche-bis-energierecht-eeg-kwk` | energierecht: Konsolidiertes Skill-Kompendium 04; bündelt 4 frühere Spezialskills (er-bess-produktsicherheit-haftung, er-bess-versicherung-und-schadenfall, er-stakeholder-mapping-energie, energierecht-eeg-kwkg-erzeugung) und bewahrt dere... |
| `kompendium-05-energierecht-emobili-bis-energierecht-infrast` | energierecht: Konsolidiertes Skill-Kompendium 05; bündelt 4 frühere Spezialskills (energierecht-emobility-wasserstoff, energierecht-energievertraege, energierecht-industriekunden, energierecht-infrastrukturprojekte) und bewahrt deren Wor... |
| `kompendium-06-energierecht-kommand-bis-energierecht-transak` | energierecht: Konsolidiertes Skill-Kompendium 06; bündelt 4 frühere Spezialskills (energierecht-kommandocenter, energierecht-netz-speicher-zugang, energierecht-projektfinanzierung, energierecht-transaktionen-dd) und bewahrt deren Workflo... |
| `kompendium-07-energierecht-vertrie-bis-er-bess-abfall-recyc` | energierecht: Konsolidiertes Skill-Kompendium 07; bündelt 4 frühere Spezialskills (energierecht-vertrieb-marktrollen, energierecht-waerme-quartier, energierecht-wettbewerb, er-bess-abfall-recycling-rueckbau) und bewahrt deren Workflows,... |
| `kompendium-08-er-bess-abstandsflae-bis-er-bess-bimschg-und` | energierecht: Konsolidiertes Skill-Kompendium 08; bündelt 4 frühere Spezialskills (er-bess-abstandsflaechen-und-layout, er-bess-baurecht-brandenburg, er-bess-behoerdenstrategie, er-bess-bimschg-und-4-bimschv) und bewahrt deren Workflows,... |
| `kompendium-09-er-bess-brandschutz-bis-er-bess-dieselgenera` | energierecht: Konsolidiertes Skill-Kompendium 09; bündelt 4 frühere Spezialskills (er-bess-brandschutz-lithium-ionen, er-bess-co-location-pv-wind, er-bess-datenschutz-video-leitwarte, er-bess-dieselgenerator-notstrom) und bewahrt deren W... |
| `kompendium-10-er-bess-epc-o-and-m-bis-er-bess-kapazitaetsm` | energierecht: Konsolidiertes Skill-Kompendium 10; bündelt 4 frühere Spezialskills (er-bess-epc-o-and-m-vertraege, er-bess-fca-agnes-bnetza, er-bess-finanzierung-bankability, er-bess-kapazitaetsmarkt-grundlast) und bewahrt deren Workflows... |
| `kompendium-11-er-bess-kritis-nis2-bis-er-bess-netzanschlus` | energierecht: Konsolidiertes Skill-Kompendium 11; bündelt 4 frühere Spezialskills (er-bess-kritis-nis2-cyber, er-bess-marktrollen-bilanzkreis, er-bess-naturschutz-artenschutz, er-bess-netzanschluss-hoehe-spannung) und bewahrt deren Workf... |
| `kompendium-12-er-bess-netzentgelte-bis-er-bess-power-qualit` | energierecht: Konsolidiertes Skill-Kompendium 12; bündelt 4 frühere Spezialskills (er-bess-netzentgelte-und-abgaben, er-bess-output-board-paper, er-bess-physische-sicherheit-terror, er-bess-power-quality-emv) und bewahrt deren Workflows,... |
| `kompendium-13-er-bess-ppa-und-merc-bis-er-bess-regelenergie` | energierecht: Konsolidiertes Skill-Kompendium 13; bündelt 4 frühere Spezialskills (er-bess-ppa-und-merchant-risk, er-bess-projektakte-qualitygate, er-bess-rechtsmittel-und-nachbarabwehr, er-bess-regelenergie-systemdienstleistung) und bew... |
| `kompendium-14-er-bess-vergabe-komm-bis-er-fusion-bauleitpla` | energierecht: Konsolidiertes Skill-Kompendium 14; bündelt 4 frühere Spezialskills (er-bess-vergabe-kommunale-stadtwerke, er-bess-wasser-awsv-und-boden, er-einfuehrung-system, er-fusion-bauleitplanung-starnberger-see) und bewahrt deren Wo... |
| `kompendium-15-er-fusion-buergerbet-bis-er-fusion-sicherheit` | energierecht: Konsolidiertes Skill-Kompendium 15; bündelt 4 frühere Spezialskills (er-fusion-buergerbeteiligung-und-politik, er-fusion-foerderung-beihilfe, er-fusion-netzanschluss-und-systemnutzen, er-fusion-sicherheitsnachweis) und bewa... |
| `kompendium-16-er-fusion-strahlensc-bis-er-netzanschluss-pra` | energierecht: Konsolidiertes Skill-Kompendium 16; bündelt 4 frühere Spezialskills (er-fusion-strahlenschutz-neutronen, er-fusion-transrapid-anbindung, er-h2-electrolyseur-foerderung, er-netzanschluss-praesumtion-spezial) und bewahrt dere... |
| `kompendium-17-er-netzentgelte-rech-bis-spezial-anfrage-mehr` | energierecht: Konsolidiertes Skill-Kompendium 17; bündelt 4 frühere Spezialskills (er-netzentgelte-rechtsfragen, er-redispatch-3-0-spezial, er-typ-anfrage-mandanten-routing, spezial-anfrage-mehrparteien-konflikt-und-interessen) und bewah... |
| `kompendium-18-spezial-einfuehrung-bis-spezial-industrie-sc` | energierecht: Konsolidiertes Skill-Kompendium 18; bündelt 4 frühere Spezialskills (spezial-einfuehrung-mandantenkommunikation-entscheidungsvorlage, spezial-energieprojekt-intake-und-regulierungsweiche, spezial-energierecht-erstpruefung-u... |
| `kompendium-19-spezial-kwkg-verhand-bis-spezial-praesumtion` | energierecht: Konsolidiertes Skill-Kompendium 19; bündelt 4 frühere Spezialskills (spezial-kwkg-verhandlung-vergleich-und-eskalation, spezial-netzanschluss-formular-portal-und-einreichung, spezial-netze-risikoampel-und-gegenargumente, sp... |
| `kompendium-20-spezial-projektfinan-bis-spezial-system-bewei` | energierecht: Konsolidiertes Skill-Kompendium 20; bündelt 4 frühere Spezialskills (spezial-projektfinanzierung-compliance-dokumentation-und-akte, spezial-routing-internationaler-bezug-und-schnittstellen, spezial-stadtwerke-tatbestand-bew... |
| `kompendium-21-spezial-transaktione-bis-strompreisbremse-und` | energierecht: Konsolidiertes Skill-Kompendium 21; bündelt 4 frühere Spezialskills (spezial-transaktionen-zahlen-schwellen-und-berechnung, spezial-vertrieb-behoerden-gericht-und-registerweg, spezial-waerme-dokumentenmatrix-und-lueckenlist... |
| `spezial-rechtsquellen-sonderfall-und-edge-case` | Rechtsquellen: Sonderfall und Edge-Case-Prüfung im Plugin energierecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-verfahren-livequellen-und-rechtsprechungscheck` | Verfahren: Livequellen- und Rechtsprechungscheck im Plugin energierecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin energierecht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin energierecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin energierecht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin energierecht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
