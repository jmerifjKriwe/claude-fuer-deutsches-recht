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
| `autonomous-driving-interessen-grossprojekt` | Autonomous Driving Interessen Grossprojekt im Verkehrs- und Infrastrukturrecht: prüft konkret Autonomous, Driving, Grossprojekt. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `foerderung-vergabe-ladeinfrastruktur` | Foerderung Vergabe Ladeinfrastruktur im Verkehrs- und Infrastrukturrecht: prüft konkret Foerderrecht und Vergabe für Verkehrsinfrastruktur-Projekte, Ladeinfrastruktur für Elektromobilitaet rechtlich begleiten, Planfeststellung für Strass... |
| `infrastruktur-foerderung-nachhaltige` | Infrastruktur Foerderung Nachhaltige im Verkehrs- und Infrastrukturrecht: prüft konkret Foerderprogramme Verkehrsinfrastruktur uebersichtlich, Nachhaltige Bahninfrastruktur und Emissionen, Planfeststellung in Grundzuegen. Liefert prioris... |
| `infrastrukturrecht-intake-ladeinfrastruktur` | Intake Ladeinfrastruktur im Verkehrs- und Infrastrukturrecht: prüft konkret Infrastrukturrecht, Intake, Ladeinfrastruktur. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `livecheck-sonderfall-mobilitaetsprojekt` | Livecheck Sonderfall Mobilitaetsprojekt im Verkehrs- und Infrastrukturrecht: prüft konkret Livecheck, Mobilitätsprojekt-Intake mit Rechtsweg-, Förder- und Beteiligungsweiche, Mobilitaetsprojekt. Liefert priorisierten Output mit Norm-Pinp... |
| `parkraum-planfeststellung-strassenbahn` | Parkraum Planfeststellung Strassenbahn im Verkehrs- und Infrastrukturrecht: prüft konkret Parkraum, Planfeststellung, Strassenbahn. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `parkraumbewirtschaftung-verkehr` | Parkraumbewirtschaftung Verkehr im Verkehrs- und Infrastrukturrecht: prüft konkret Parkraumbewirtschaftung, Parkraumbewirtschaftung kommunalrechtlich gestalten und, Planfeststellung und Großprojektsteuerung. Liefert priorisierten Output... |
| `schulwegsicherheit-sondernutzung-strassenbahn` | Schulwegsicherheit Sondernutzung Strassenbahn im Verkehrs- und Infrastrukturrecht: prüft konkret Schulwegsicherheit rechtlich verbessern oder Amtshaftung, Sondernutzung öffentlicher Strassenflaechen beantragen und, Strassenbahn- und OEPN... |
| `strassenrecht-verkehrs-verkehrswende` | Strassenrecht Verkehrs Verkehrswende im Verkehrs- und Infrastrukturrecht: prüft konkret Strassenrecht, Verkehrs, Verkehrswende. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `verkehr-infrastruktur-fristen-risiko-mandant` | Infrastruktur Fristen Risiko Mandant im Verkehrs- und Infrastrukturrecht: prüft konkret Fristen- und Risikoampel im Plugin, Mandantenkommunikation im Plugin verkehr-infrastrukturrecht, Red-Team Qualitygate im Plugin verkehr-infrastruktur... |
| `verkehr-infrastruktur-rechtsquellen-beweislast-darlegungslast` | Rechtsquellen: Quellenprüfung; Beweislast, Darlegungslast und Substantiierung: Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `verkehr-infrastrukturrecht-anschluss-router` | Anschluss Router im Verkehrs- und Infrastrukturrecht: prüft konkret Einstieg, Schnelltriage und Fallrouting im Verkehr, Anschluss-Skills Router im Plugin verkehr-infrastrukturrecht, Chronologie und Belegmatrix im Plugin. Liefert priorisi... |
| `verkehr-infrastrukturrecht-autonomous-driving` | Autonomous Driving im Verkehrs- und Infrastrukturrecht: prüft konkret Zentrales Steuerungsmodul Verkehrs- und Infrastrukturrecht, Autonomes Fahren und Strassenrecht, Spezialfall Buergerentscheid zur Strassenbahn oder Stadtbahn. Liefert p... |
| `verkehr-infrastrukturrecht-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `verkehr-infrastrukturrecht-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `verkehr-infrastrukturrecht-output-waehlen` | Output wählen im Verkehrs- und Infrastrukturrecht: Diese Output-Weiche für Verkehr Infrastrukturrecht entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `verkehr-infrastrukturrecht-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `verkehr-infrastrukturrecht-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `verkehr-quellenkarte` | Verkehr Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `verkehrsplanung-verfahren-vertragsmodell` | Verkehrsplanung Verfahren Vertragsmodell im Verkehrs- und Infrastrukturrecht: prüft konkret Verkehrsplanung, Anhoerung, Widerspruch, Klage und Eilverfahren im Verkehrsinfrastrukturrecht vor. Liefert priorisierten Output mit Norm-Pinpoint... |
| `verkehrsplanung-verkehrswende` | Verkehrsplanung Verkehrswende im Verkehrs- und Infrastrukturrecht: prüft konkret Verkehrsplanung rechtlich begleiten, Verkehrswende-Massnahmen rechtssicher gestalten, Wirtschaftsverkehr und Lieferverkehr in der Stadt rechtlich. Liefert p... |
| `vi-rechtsquellen-uebersicht` | Rechtsquellen Verkehrs- und Infrastrukturrecht: BFStrG, PBefG, AEG, EnWG-Trasse, BImSchG, BNatSchG, WHG, VwVfG, UVPG. Pro Norm: Anwendungsbereich, Verfahrensart, Aufsicht. Entscheidungstabelle fuer ein konkretes Infrastrukturvorhaben. |
| `vifr-aeg-bahnrecht-deutschlandticket` | Vifr AEG Bahnrecht Deutschlandticket im Verkehrs- und Infrastrukturrecht: prüft konkret Leitfaden AEG und Bahnrecht, Spezialfall Deutschlandticket und Tarifrecht OePNV, Spezialfall Luftverkehrsrecht und Flughafenausbau. Liefert priorisie... |
| `vifr-planfeststellung` | Vifr Planfeststellung im Verkehrs- und Infrastrukturrecht: fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
