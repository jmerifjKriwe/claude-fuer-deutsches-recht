# Verkehrs- und Infrastrukturrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`verkehr-infrastrukturrecht`) | [`verkehr-infrastrukturrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verkehr-infrastrukturrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Märkische Reserve Süd — Batteriespeicher Brandenburg/Berlin** (`batteriespeicher-brandenburg-berlin-resilienz`) | [Gesamt-PDF lesen](../testakten/batteriespeicher-brandenburg-berlin-resilienz/gesamt-pdf/batteriespeicher-brandenburg-berlin-resilienz_gesamt.pdf) | [`testakte-batteriespeicher-brandenburg-berlin-resilienz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-batteriespeicher-brandenburg-berlin-resilienz.zip) |
| **Projekt Isarlicht — Kernfusion und Transrapid am Starnberger See** (`kernfusion-transrapid-starnberger-see`) | [Gesamt-PDF lesen](../testakten/kernfusion-transrapid-starnberger-see/gesamt-pdf/kernfusion-transrapid-starnberger-see_gesamt.pdf) | [`testakte-kernfusion-transrapid-starnberger-see.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kernfusion-transrapid-starnberger-see.zip) |
| **Akte Verkehrs- und Infrastrukturrecht: Straßenbahn Linie 7, Ladezonen und Schulwegsicherheit** (`verkehr-infrastrukturrecht-strassenbahn-ladezonen`) | [Gesamt-PDF lesen](../testakten/verkehr-infrastrukturrecht-strassenbahn-ladezonen/gesamt-pdf/verkehr-infrastrukturrecht-strassenbahn-ladezonen_gesamt.pdf) | [`testakte-verkehr-infrastrukturrecht-strassenbahn-ladezonen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verkehr-infrastrukturrecht-strassenbahn-ladezonen.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Vollständiger Assistent für Verkehrsplanung, Infrastrukturprojekte, Elektromobilität, Straßenbahn, Sondernutzung, Parkraumbewirtschaftung, Liefer- und Ladezonen, Verkehrswende, Schulwegsicherheit, Fördermittel und Vergabe.

Dieses Plugin ist **vollständig freistehend**. Es erwartet keine anderen Plugins, keine externen Agenten und keine besonderen Repo-Dateien außerhalb seines eigenen Ordners. Wenn ein Anschluss an Register, Behördenportale, E-Mail, beA, Datenraum, Bank, GIS, Tabellen oder Kanzleisoftware fehlt, arbeitet es mit manuellen Uploads oder mit einem gekennzeichneten Simulationsmodus.

## Schnellstart

1. Plugin aktivieren oder die ZIP aus dem Release installieren.
2. Eine neue Sache mit `verkehr-infrastrukturrecht-kommandocenter` starten.
3. Mandant, Ziel, Frist, Dokumente und gewünschtes Ergebnis nennen.
4. Bei fehlenden Systemanschlüssen `Simulation` sagen; das Plugin erzeugt dann realistische Testdaten und erklärt, welche echte Schnittstelle später ersetzt werden müsste.
5. Am Ende immer das Qualitätstor ausgeben lassen: offene Annahmen, Fristen, Rechenprüfung, Anlagen, Zuständigkeiten und nächste Schritte.

## Enthaltene Skills

- `verkehr-infrastrukturrecht-kommandocenter` - Verkehrs- und Infrastruktur-Kommandocenter
- `verkehr-infrastrukturrecht-verkehrsplanung` - Verkehrsplanung und Projektstrategie
- `verkehr-infrastrukturrecht-planfeststellung` - Planfeststellung und Abwägung
- `verkehr-infrastrukturrecht-strassenbahn` - Straßenbahn- und ÖPNV-Projekte
- `verkehr-infrastrukturrecht-ladeinfrastruktur` - Ladeinfrastruktur und Elektromobilität
- `verkehr-infrastrukturrecht-sondernutzung` - Sondernutzung, Widmung und Straßenrecht
- `verkehr-infrastrukturrecht-parkraumbewirtschaftung` - Parkraumbewirtschaftung
- `verkehr-infrastrukturrecht-wirtschaftsverkehr` - Wirtschaftsverkehr, Liefer- und Ladezonen
- `verkehr-infrastrukturrecht-verkehrswende` - Verkehrswende und Verkehrsberuhigung
- `verkehr-infrastrukturrecht-schulwegsicherheit` - Schulwegsicherheit
- `verkehr-infrastrukturrecht-verfahren` - Verkehrsrechtliche Verfahren und Streit
- `verkehr-infrastrukturrecht-foerderung-vergabe` - Förderung und Vergabe Infrastruktur

## Vorlagen

- `assets/templates/verkehr-mandatskarte.md` - Verkehrs- und Infrastruktur-Mandatskarte
- `assets/templates/infrastruktur-projektfahrplan.md` - Infrastruktur-Projektfahrplan
- `assets/templates/planfeststellung-abwaegungsmatrix.md` - Planfeststellungs- und Abwägungsmatrix
- `assets/templates/strassenbahn-workstream-plan.md` - Straßenbahn-Workstream-Plan
- `assets/templates/ladeinfrastruktur-check.md` - Ladeinfrastruktur-Check
- `assets/templates/sondernutzung-erlaubnis.md` - Sondernutzung und Straßenrecht
- `assets/templates/parkraumkonzept.md` - Parkraumbewirtschaftungskonzept
- `assets/templates/liefer-ladeflaechen-konzept.md` - Liefer- und Ladeflächenkonzept
- `assets/templates/verkehrswende-massnahmenplan.md` - Verkehrswende-Maßnahmenplan
- `assets/templates/schulwegsicherheit-check.md` - Schulwegsicherheitscheck
- `assets/templates/verkehrsverfahren-fristen.md` - Verkehrs-Verfahrens- und Fristenplan
- `assets/templates/foerderung-vergabe-matrix.md` - Förder- und Vergabematrix

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
| `kompendium-01-allgemein-bis-workflow-chronologie` | verkehr-infrastrukturrecht: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-anschluss-skills-router, workflow-chronologie-und-belegmatrix) und bewahrt deren Workflows, Normanker, Prüfprogramme und... |
| `kompendium-02-workflow-fristen-und-bis-workflow-redteam-qua` | verkehr-infrastrukturrecht: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-fristen-und-risikoampel, workflow-mandantenkommunikation, workflow-redteam-qualitygate) und bewahrt deren Workflows, Normanker, Prü... |
| `kompendium-03-spezial-verkehrsplan-bis-vertragsmodell-stras` | verkehr-infrastrukturrecht: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (spezial-verkehrsplanung-fristen-form-und-zustaendigkeit, verkehr-infrastrukturrecht-verfahren, vertragsmodell-strasse-app-spezial) und bewah... |
| `kompendium-04-spezial-parkraumbewi-bis-spezial-planfeststel` | verkehr-infrastrukturrecht: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (spezial-parkraumbewirtschaftung-formular-portal-und-einreichung, verkehr-infrastrukturrecht-parkraumbewirtschaftung, spezial-planfeststellun... |
| `kompendium-05-verkehr-infrastruktu-bis-buergerentscheid-str` | verkehr-infrastrukturrecht: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (verkehr-infrastrukturrecht-kommandocenter, autonomous-driving-strassenrecht, buergerentscheid-strassenbahn-spezial) und bewahrt deren Workfl... |
| `kompendium-06-infrastruktur-foerde-bis-planfeststellung-gru` | verkehr-infrastrukturrecht: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (infrastruktur-foerderung-uebersicht, nachhaltige-bahninfrastruktur-emissionen, planfeststellung-grundzuege) und bewahrt deren Workflows, Nor... |
| `kompendium-07-spezial-autonomous-c-bis-spezial-grossprojekt` | verkehr-infrastrukturrecht: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (spezial-autonomous-compliance-dokumentation-und-akte, spezial-driving-mehrparteien-konflikt-und-interessen, spezial-grossprojekt-zahlen-schw... |
| `kompendium-08-spezial-infrastruktu-bis-spezial-ladeinfrastr` | verkehr-infrastrukturrecht: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (spezial-infrastrukturrecht-tatbestand-beweis-und-belege, spezial-intake-mandantenkommunikation-entscheidungsvorlage, spezial-ladeinfrastrukt... |
| `kompendium-09-spezial-livecheck-so-bis-spezial-mobilitaetsp` | verkehr-infrastrukturrecht: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (spezial-livecheck-sonderfall-und-edge-case, spezial-mobilitaetsprojekt-intake, spezial-mobilitaetsprojekt-red-team-und-qualitaetskontrolle)... |
| `kompendium-10-spezial-parkraum-sch-bis-spezial-strassenbahn` | verkehr-infrastrukturrecht: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (spezial-parkraum-schriftsatz-brief-und-memo-bausteine, spezial-planfeststellung-dokumentenmatrix-und-lueckenliste, spezial-strassenbahn-risi... |
| `kompendium-11-spezial-strassenrech-bis-spezial-verkehrswend` | verkehr-infrastrukturrecht: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (spezial-strassenrecht-internationaler-bezug-und-schnittstellen, spezial-verkehrs-erstpruefung-und-mandatsziel, spezial-verkehrswende-verhand... |
| `kompendium-12-verkehr-infrastruktu-bis-verkehr-infrastruktu` | verkehr-infrastrukturrecht: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (verkehr-infrastrukturrecht-foerderung-vergabe, verkehr-infrastrukturrecht-ladeinfrastruktur, verkehr-infrastrukturrecht-planfeststellung) un... |
| `kompendium-13-verkehr-infrastruktu-bis-verkehr-infrastruktu` | verkehr-infrastrukturrecht: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (verkehr-infrastrukturrecht-schulwegsicherheit, verkehr-infrastrukturrecht-sondernutzung, verkehr-infrastrukturrecht-strassenbahn) und bewahr... |
| `kompendium-14-verkehr-infrastruktu-bis-verkehr-infrastruktu` | verkehr-infrastrukturrecht: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (verkehr-infrastrukturrecht-verkehrsplanung, verkehr-infrastrukturrecht-verkehrswende, verkehr-infrastrukturrecht-wirtschaftsverkehr) und bew... |
| `kompendium-15-vifr-aeg-bahnrecht-l-bis-vifr-luftverkehrsrec` | verkehr-infrastrukturrecht: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (vifr-aeg-bahnrecht-leitfaden, vifr-deutschlandticket-tarifrecht-spezial, vifr-luftverkehrsrecht-flughafen-spezial) und bewahrt deren Workflo... |
| `kompendium-16-vifr-planfeststellun-bis-vifr-planfeststellun` | verkehr-infrastrukturrecht: Konsolidiertes Skill-Kompendium 16; bündelt 1 frühere Spezialskills (vifr-planfeststellung-strasse-bauleiter) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-rechtsquellen-beweislast-und-darlegungslast` | Rechtsquellen: Beweislast, Darlegungslast und Substantiierung im Plugin verkehr infrastrukturrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-verkehr-livequellen-und-rechtsprechungscheck` | Verkehr: Livequellen- und Rechtsprechungscheck im Plugin verkehr infrastrukturrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `vi-rechtsquellen-uebersicht` | Rechtsquellen Verkehrs- und Infrastrukturrecht: BFStrG, PBefG, AEG, EnWG-Trasse, BImSchG, BNatSchG, WHG, VwVfG, UVPG. Pro Norm: Anwendungsbereich, Verfahrensart, Aufsicht. Entscheidungstabelle fuer ein konkretes Infrastrukturvorhaben. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin verkehr-infrastrukturrecht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin verkehr-infrastrukturrecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin verkehr-infrastrukturrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin verkehr-infrastrukturrecht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin verkehr-infrastrukturrecht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
