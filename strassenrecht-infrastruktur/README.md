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

Beginne mit `allgemein`. Das Plugin fragt zuerst nach Rolle, Ziel, Frist, Behörde/Gericht/Register, vorhandenen Unterlagen und gewünschtem Output. Danach schlägt es die passenden Spezialskills aus diesem Plugin vor.

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
| `allgemein` | Straßenrecht und Infrastruktur: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Spezialskill-Routing und erste Ausgabe. |
| `kompendium-01-str-002-bundesfernst-bis-str-005-umstufung-un` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 01; bündelt 4 frühere Spezialskills (str-002-bundesfernstrasse-oder-landesstrasse, str-003-strassenbaulasttraeger-bestimmen, str-004-widmung-und-einziehung-pruefen, str-005-ums... |
| `kompendium-02-str-006-planfeststel-bis-str-009-sondernutzun` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 02; bündelt 4 frühere Spezialskills (str-006-planfeststellung-strasse, str-007-plangenehmigung-und-uvp, str-008-anliegergebrauch-abgrenzen, str-009-sondernutzungserlaubnis) und... |
| `kompendium-03-str-010-baustelle-un-bis-str-013-rastanlage-u` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 03; bündelt 4 frühere Spezialskills (str-010-baustelle-und-verkehrsfuehrung, str-011-strassenentwaesserung, str-012-bruecke-und-tunnel, str-013-rastanlage-und-nebenbetrieb) und... |
| `kompendium-04-str-014-kreuzungsrec-bis-str-017-schaeden-dur` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 04; bündelt 4 frühere Spezialskills (str-014-kreuzungsrecht-bahn-wasser-strasse, str-015-strassenausbaubeitrag-pruefen, str-016-unterhaltungspflicht-und-winterdienst, str-017-s... |
| `kompendium-05-str-018-eilrechtssch-bis-str-021-autobahn-bau` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 05; bündelt 4 frühere Spezialskills (str-018-eilrechtsschutz-gegen-bau, str-019-aktenplan-infrastruktur, str-020-landesstrassengesetz-livecheck, str-021-autobahn-baulast-pruefe... |
| `kompendium-06-str-022-autobahn-wid-bis-str-025-autobahn-ein` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 06; bündelt 4 frühere Spezialskills (str-022-autobahn-widmung-lesen, str-023-autobahn-planrecht-pruefen, str-024-autobahn-sondernutzung-formulieren, str-025-autobahn-einwendung... |
| `kompendium-07-str-026-autobahn-eil-bis-str-029-autobahn-dok` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 07; bündelt 4 frühere Spezialskills (str-026-autobahn-eilantrag-skizzieren, str-027-autobahn-kostenlast-pruefen, str-028-autobahn-unterhaltung-ruegen, str-029-autobahn-dokument... |
| `kompendium-08-str-030-autobahn-das-bis-str-033-bundesstrass` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 08; bündelt 4 frühere Spezialskills (str-030-autobahn-dashboard-erstellen, str-031-bundesstrasse-baulast-pruefen, str-032-bundesstrasse-widmung-lesen, str-033-bundesstrasse-pla... |
| `kompendium-09-str-034-bundesstrass-bis-str-037-bundesstrass` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 09; bündelt 4 frühere Spezialskills (str-034-bundesstrasse-sondernutzung-formuliere, str-035-bundesstrasse-einwendung-bauen, str-036-bundesstrasse-eilantrag-skizzieren, str-037... |
| `kompendium-10-str-038-bundesstrass-bis-str-041-landesstrass` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 10; bündelt 4 frühere Spezialskills (str-038-bundesstrasse-unterhaltung-ruegen, str-039-bundesstrasse-dokumente-sortieren, str-040-bundesstrasse-dashboard-erstellen, str-041-la... |
| `kompendium-11-str-042-landesstrass-bis-str-045-landesstrass` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 11; bündelt 4 frühere Spezialskills (str-042-landesstrasse-widmung-lesen, str-043-landesstrasse-planrecht-pruefen, str-044-landesstrasse-sondernutzung-formuliere, str-045-lande... |
| `kompendium-12-str-046-landesstrass-bis-str-049-landesstrass` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 12; bündelt 4 frühere Spezialskills (str-046-landesstrasse-eilantrag-skizzieren, str-047-landesstrasse-kostenlast-pruefen, str-048-landesstrasse-unterhaltung-ruegen, str-049-la... |
| `kompendium-13-str-050-landesstrass-bis-str-053-kreisstrasse` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 13; bündelt 4 frühere Spezialskills (str-050-landesstrasse-dashboard-erstellen, str-051-kreisstrasse-baulast-pruefen, str-052-kreisstrasse-widmung-lesen, str-053-kreisstrasse-p... |
| `kompendium-14-str-054-kreisstrasse-bis-str-057-kreisstrasse` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 14; bündelt 4 frühere Spezialskills (str-054-kreisstrasse-sondernutzung-formulieren, str-055-kreisstrasse-einwendung-bauen, str-056-kreisstrasse-eilantrag-skizzieren, str-057-k... |
| `kompendium-15-str-058-kreisstrasse-bis-str-061-gemeindestra` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 15; bündelt 4 frühere Spezialskills (str-058-kreisstrasse-unterhaltung-ruegen, str-059-kreisstrasse-dokumente-sortieren, str-060-kreisstrasse-dashboard-erstellen, str-061-gemei... |
| `kompendium-16-str-062-gemeindestra-bis-str-065-gemeindestra` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 16; bündelt 4 frühere Spezialskills (str-062-gemeindestrasse-widmung-lesen, str-063-gemeindestrasse-planrecht-pruefen, str-064-gemeindestrasse-sondernutzung-formulie, str-065-g... |
| `kompendium-17-str-066-gemeindestra-bis-str-069-gemeindestra` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 17; bündelt 4 frühere Spezialskills (str-066-gemeindestrasse-eilantrag-skizzieren, str-067-gemeindestrasse-kostenlast-pruefen, str-068-gemeindestrasse-unterhaltung-ruegen, str-... |
| `kompendium-18-str-070-gemeindestra-bis-str-073-ortsdurchfah` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 18; bündelt 4 frühere Spezialskills (str-070-gemeindestrasse-dashboard-erstellen, str-071-ortsdurchfahrt-baulast-pruefen, str-072-ortsdurchfahrt-widmung-lesen, str-073-ortsdurc... |
| `kompendium-19-str-074-ortsdurchfah-bis-str-077-ortsdurchfah` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 19; bündelt 4 frühere Spezialskills (str-074-ortsdurchfahrt-sondernutzung-formulier, str-075-ortsdurchfahrt-einwendung-bauen, str-076-ortsdurchfahrt-eilantrag-skizzieren, str-0... |
| `kompendium-20-str-078-ortsdurchfah-bis-str-081-bruecke-baul` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 20; bündelt 4 frühere Spezialskills (str-078-ortsdurchfahrt-unterhaltung-ruegen, str-079-ortsdurchfahrt-dokumente-sortieren, str-080-ortsdurchfahrt-dashboard-erstellen, str-081... |
| `kompendium-21-str-082-bruecke-widm-bis-str-085-bruecke-einw` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 21; bündelt 4 frühere Spezialskills (str-082-bruecke-widmung-lesen, str-083-bruecke-planrecht-pruefen, str-084-bruecke-sondernutzung-formulieren, str-085-bruecke-einwendung-bau... |
| `kompendium-22-str-086-bruecke-eila-bis-str-089-bruecke-doku` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 22; bündelt 4 frühere Spezialskills (str-086-bruecke-eilantrag-skizzieren, str-087-bruecke-kostenlast-pruefen, str-088-bruecke-unterhaltung-ruegen, str-089-bruecke-dokumente-so... |
| `kompendium-23-str-090-bruecke-dash-bis-str-093-tunnel-planr` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 23; bündelt 4 frühere Spezialskills (str-090-bruecke-dashboard-erstellen, str-091-tunnel-baulast-pruefen, str-092-tunnel-widmung-lesen, str-093-tunnel-planrecht-pruefen) und be... |
| `kompendium-24-str-094-tunnel-sonde-bis-str-097-tunnel-koste` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 24; bündelt 4 frühere Spezialskills (str-094-tunnel-sondernutzung-formulieren, str-095-tunnel-einwendung-bauen, str-096-tunnel-eilantrag-skizzieren, str-097-tunnel-kostenlast-p... |
| `kompendium-25-str-098-tunnel-unter-bis-str-099-tunnel-dokum` | strassenrecht-infrastruktur: Konsolidiertes Skill-Kompendium 25; bündelt 2 frühere Spezialskills (str-098-tunnel-unterhaltung-ruegen, str-099-tunnel-dokumente-sortieren) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemu... |
| `str-001-kaltstart-strassenrechtsfall` | Straßenrecht und Infrastruktur: Kaltstart Straßenrechtsfall. Kaltstart Straßenrechtsfall im Fachgebiet Straßenrecht und Infrastruktur als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
