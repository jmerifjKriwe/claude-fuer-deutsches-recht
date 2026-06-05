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
| `abfall-anlagen-bimschg` | Abfall Anlagen Bimschg im Plugin Umweltrecht: prüft konkret Abfall, Anlagen, Bimschg. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `boden-csddd-csrd-sonderfall` | Boden Csddd CSRD Sonderfall im Plugin Umweltrecht: prüft konkret Boden, Csddd, Csrd. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `bussgeld-quellenkarte` | Bussgeld Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `diligence-greenwashing-beweislast-klimaklagen` | Diligence Greenwashing Beweislast Klimaklagen im Plugin Umweltrecht: prüft konkret Diligence, Greenwashing, Klimaklagen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `esg-greenwashing-klimaklagen-verbandsklage` | ESG Greenwashing Klimaklagen Verbandsklage im Plugin Umweltrecht: prüft konkret Prüffeld für esg greenwashing csrd, Prüffeld für klimaklagen verbandsklage umwrg, Unternehmen ab 1000 Mitarbeitern muss. Liefert priorisierten Output mit Nor... |
| `lieferkettensorgfalt-lksg-red-naturschutz` | Lieferkettensorgfalt Lksg RED Naturschutz im Plugin Umweltrecht: prüft konkret Lieferkettensorgfalt, Lksg, Naturschutz. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `stoerfall-anlagen-transaktionen-dd` | Stoerfall Anlagen Transaktionen DD im Plugin Umweltrecht: prüft konkret Anlagenbetreiber prüft Stoerfallrelevanz betreibt, M&A-Transaktion und Anwalt prüft Umwelt-DD-Risiken im, Buerger Verband oder Unternehmen stellt UIG/IFG-Antrag auf.... |
| `tehg-verfahren-umweltrecht` | Tehg Verfahren Umweltrecht im Plugin Umweltrecht: prüft konkret Tehg, Verfahren, Umweltrechtssache geht in Verwaltungsgericht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `umwelt-umweltrecht-umwrg` | Umwelt Umweltrecht Umwrg im Plugin Umweltrecht: prüft konkret Umwelt, Umweltrecht, Umwrg. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `umweltrecht-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `umweltrecht-bussgeld-emissionshandel-tehg-uwr` | Bussgeld Emissionshandel Tehg UWR im Plugin Umweltrecht: prüft konkret Unternehmen erhaelt Anhoerung oder Bußgeld-Bescheid wegen, Anlagenbetreiber begutachtet Zuteilungsantrag Monitoring, Spezialfall EU-Emissionshandel ETS. Liefert prior... |
| `umweltrecht-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `umweltrecht-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `umweltrecht-immissionsschutz-bimschg` | Immissionsschutz Bimschg im Plugin Umweltrecht: prüft konkret Anlagenbetreiber oder Nachbar, Umweltmandat-Einstieg, Unternehmen plant Bauvorhaben mit naturschutzrechtlichem. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel un... |
| `umweltrecht-mandantenkommunikation-redteam-qualitygate-stoerfall` | Mandantenkommunikation Redteam Qualitygate Stoerfall im Plugin Umweltrecht: prüft konkret Mandantenkommunikation im Plugin umweltrecht, Red-Team Qualitygate im Plugin umweltrecht, Stoerfall. Liefert priorisierten Output mit Norm-Pinpoint... |
| `umweltrecht-output-waehlen` | Output wählen im Plugin Umweltrecht: Diese Output-Weiche für Umweltrecht entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `umweltrecht-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `umweltrecht-start-chronologie-fristen` | Start Chronologie Fristen im Plugin Umweltrecht: prüft konkret Einstieg, Schnelltriage und Fallrouting im Umweltrecht-Plugin, Ziel, Chronologie und Belegmatrix im Plugin umweltrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risik... |
| `umweltrecht-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `umweltrecht-uwr-bundesnaturschutzgesetz-eingriff-co2` | UWR Bundesnaturschutzgesetz Eingriff CO2 im Plugin Umweltrecht: prüft konkret Spezialfall Eingriff in Natur und Landschaft §§ 14 ff, Spezialfall CO2-Emissionshandel TEHG / EU-ETS und Reform, Immissionsschutzrecht Praxis. Liefert priorisi... |
| `uwr-einfuehrung-rechtsquellen` | Umweltrecht einfuehrend: BImSchG, BNatSchG, WHG, KrWG, BBodSchG, USchadG, EU-IED, REACH. Pro Norm Anwendungsbereich, Aufsicht, typische Mandantenfragen. Entscheidungstabelle. |
| `uwr-wasserrechtliche` | UWR Wasserrechtliche im Plugin Umweltrecht: fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |
| `wasser-abfall-circular-umweltrecht-schulung` | Wasser Abfall Circular Umweltrecht Schulung im Plugin Umweltrecht: prüft konkret Wasser, Unternehmen oder Anlagenbetreiber hat Abfall-Frage, Anlagenbetreiber muss Umwelt-Compliance-Schulungen und. Liefert priorisierten Output mit Norm-Pi... |
| `wasser-bodenschutz-uwr-altlasten-bimschg` | Wasser Bodenschutz UWR Altlasten Bimschg im Plugin Umweltrecht: prüft konkret Unternehmen beantragt WHG-Erlaubnis oder hat, Spezialfall Altlastenpruefung, Bauleiter BImSchG-Genehmigung. Liefert priorisierten Output mit Norm-Pinpoints, Ri... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
