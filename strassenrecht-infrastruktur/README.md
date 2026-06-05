# Straßenrecht und Infrastruktur

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`strassenrecht-infrastruktur`) | [`strassenrecht-infrastruktur.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strassenrecht-infrastruktur.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Straßenrechtsakte Auenfeld** (`strassenrecht-ortsdurchfahrt-bruecke-auenfeld`) | [Gesamt-PDF lesen](../testakten/strassenrecht-ortsdurchfahrt-bruecke-auenfeld/gesamt-pdf/strassenrecht-ortsdurchfahrt-bruecke-auenfeld_gesamt.pdf) | [`testakte-strassenrecht-ortsdurchfahrt-bruecke-auenfeld.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strassenrecht-ortsdurchfahrt-bruecke-auenfeld.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin trennt Straßenrecht von Straßenverkehrsrecht: Bau, Widmung, Baulast, Unterhaltung, Sondernutzung, Planfeststellung, Anliegerrechte, Kreuzungen, Umstufung und Straßeninfrastruktur.

## Start

Beginne mit `strassenrecht-infrastruktur-allgemein`. Das Plugin fragt zuerst nach Rolle, Ziel, Frist, Behörde/Gericht/Register, vorhandenen Unterlagen und gewünschtem Output. Danach schlägt es die passenden Spezialskills aus diesem Plugin vor.

## Arbeitsweise

- Es arbeitet mit Akten- und Fristenlogik statt mit Bauchgefühl.
- Es trennt Rechtsgrundlage, Verfahren, Beweis, Kosten, Kommunikation und Eskalation.
- Es soll Nutzerinnen und Nutzer befähigen: verständliche Erklärung, präzise Rückfragen, dann belastbarer Entwurf.
- Rechtsprechung und Gesetzesstände werden nicht halluziniert, sondern als Live-Check über amtliche oder frei zugängliche Quellen markiert.

## Typische Outputs

- Kaltstart-Interview und Aktenlandkarte
- Behörden-, Gerichts- oder Gegneranschreiben
- Widerspruchs-/Klage-/Eilantragsbausteine
- Kosten-, Fristen- und Zuständigkeitsmatrix
- Dashboard/Tracker für laufende Vorgänge
- Kurzfassung für Mandant, Vorstand, Verband, Redaktion oder Bürgerin

## Quellenhygiene

Siehe [`references/QUELLEN.md`](./references/QUELLEN.md). Dieses Plugin gibt keine endgültige Rechtsberatung, sondern robuste Arbeitsfassungen, Prüfpfade und Dokumentationshilfen.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 27 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `str-001-kaltstart-strassenrechtsfall` | Straßenrecht und Infrastruktur: Kaltstart Straßenrechtsfall. Kaltstart Straßenrechtsfall im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |
| `str-autobahn-eilantrag-kostenlast` | STR Autobahn Eilantrag Kostenlast: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `str-autobahn-widmung-planrecht-sondernutzung` | STR Autobahn Widmung Planrecht Sondernutzung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `str-bruecke-dashboard-tunnel-baulast-widmung` | STR Bruecke Dashboard Tunnel Baulast Widmung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `str-bruecke-eilantrag-kostenlast-unterhaltung` | STR Bruecke Eilantrag Kostenlast Unterhaltung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `str-bruecke-widmung-planrecht-sondernutzung` | STR Bruecke Widmung Planrecht Sondernutzung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `str-bundesfernstrasse-landesstrasse` | STR Bundesfernstrasse Landesstrasse: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `str-bundesstrasse-sondernutzung-einwendung` | STR Bundesstrasse Sondernutzung Einwendung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `str-bundesstrasse-unterhaltung-dokumente` | STR Bundesstrasse Unterhaltung Dokumente: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `str-eilrechtsschutz-aktenplan-infrastruktur` | STR Eilrechtsschutz Aktenplan Infrastruktur: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `str-gemeindestrasse-dashboard-ortsdurchfahrt` | STR Gemeindestrasse Dashboard Ortsdurchfahrt: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `str-gemeindestrasse-eilantrag-kostenlast` | STR Gemeindestrasse Eilantrag Kostenlast: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `str-gemeindestrasse-widmung-planrecht` | STR Gemeindestrasse Widmung Planrecht: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `str-kreisstrasse-sondernutzung-einwendung` | STR Kreisstrasse Sondernutzung Einwendung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `str-kreisstrasse-unterhaltung-dokumente` | STR Kreisstrasse Unterhaltung Dokumente: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `str-kreuzungsrecht-strassenausbaubeitrag` | STR Kreuzungsrecht Strassenausbaubeitrag: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `str-landesstrasse-eilantrag-kostenlast` | STR Landesstrasse Eilantrag Kostenlast: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `str-landesstrasse-widmung-planrecht` | STR Landesstrasse Widmung Planrecht: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `str-ortsdurchfahrt-sondernutzung-einwendung` | STR Ortsdurchfahrt Sondernutzung Einwendung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `str-ortsdurchfahrt-unterhaltung-dokumente` | STR Ortsdurchfahrt Unterhaltung Dokumente: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `str-planfeststellung-strasse-plangenehmigung` | STR Planfeststellung Strasse Plangenehmigung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `str-tunnel-sondernutzung-einwendung-bauen` | STR Tunnel Sondernutzung Einwendung Bauen: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strassenrecht-infrastruktur-kaltstart-triage` | Straßenrecht und Infrastruktur: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe. |
| `strassenrecht-infrastruktur-str-autobahn-dashboard-bundesstrasse` | STR Autobahn Dashboard Bundesstrasse: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strassenrecht-infrastruktur-str-baustelle-verkehrsfuehrung` | STR Baustelle Verkehrsfuehrung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strassenrecht-infrastruktur-str-landesstrasse-dashboard` | STR Landesstrasse Dashboard: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strassenrecht-infrastruktur-str-tunnel-unterhaltung-dokumente` | STR Tunnel Unterhaltung Dokumente: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
