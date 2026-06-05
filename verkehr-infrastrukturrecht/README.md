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
| `autonomous-driving-interessen-grossprojekt` | Autonomous Driving Interessen Grossprojekt: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `foerderung-vergabe-ladeinfrastruktur` | Foerderung Vergabe Ladeinfrastruktur: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `infrastruktur-foerderung-nachhaltige` | Infrastruktur Foerderung Nachhaltige: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `infrastrukturrecht-intake-ladeinfrastruktur` | Intake Ladeinfrastruktur: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `livecheck-sonderfall-mobilitaetsprojekt` | Livecheck Sonderfall Mobilitaetsprojekt: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `parkraum-planfeststellung-strassenbahn` | Parkraum Planfeststellung Strassenbahn: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `parkraumbewirtschaftung-verkehr` | Parkraumbewirtschaftung Verkehr: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `schulwegsicherheit-sondernutzung-strassenbahn` | Schulwegsicherheit Sondernutzung Strassenbahn: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strassenrecht-verkehrs-verkehrswende` | Strassenrecht Verkehrs Verkehrswende: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verkehr-infrastruktur-fristen-risiko-mandant` | Infrastruktur Fristen Risiko Mandant: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verkehr-infrastruktur-rechtsquellen-beweislast-darlegungslast` | Rechtsquellen: Quellenprüfung; Beweislast, Darlegungslast und Substantiierung: Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `verkehr-infrastrukturrecht-anschluss-router` | Anschluss Router: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verkehr-infrastrukturrecht-autonomous-driving` | Autonomous Driving: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verkehr-infrastrukturrecht-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `verkehr-infrastrukturrecht-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `verkehr-infrastrukturrecht-output-waehlen` | Output wählen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `verkehr-infrastrukturrecht-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `verkehr-infrastrukturrecht-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `verkehr-quellenkarte` | Verkehr Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `verkehrsplanung-verfahren-vertragsmodell` | Verkehrsplanung Verfahren Vertragsmodell: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verkehrsplanung-verkehrswende` | Verkehrsplanung Verkehrswende: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `vi-rechtsquellen-uebersicht` | Rechtsquellen Verkehrs- und Infrastrukturrecht: BFStrG, PBefG, AEG, EnWG-Trasse, BImSchG, BNatSchG, WHG, VwVfG, UVPG. Pro Norm: Anwendungsbereich, Verfahrensart, Aufsicht. Entscheidungstabelle fuer ein konkretes Infrastrukturvorhaben. |
| `vifr-aeg-bahnrecht-deutschlandticket` | Vifr AEG Bahnrecht Deutschlandticket: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `vifr-planfeststellung` | Vifr Planfeststellung: bearbeitet den maßgeblichen Prüfpfad und erzeugt den nächsten belastbaren Output im Mandat. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
