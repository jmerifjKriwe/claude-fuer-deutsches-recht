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
| `str-autobahn-eilantrag-kostenlast` | Str 026 Autobahn Eilantrag Skizzieren, Str 027 Autobahn Kostenlast Prüfen, Str 028 Autobahn Unterhaltung Ruegen, Str 029 Autobahn Dokumente Sortieren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage... |
| `str-autobahn-widmung-planrecht-sondernutzung` | Str 022 Autobahn Widmung Lesen, Str 023 Autobahn Planrecht Prüfen, Str 024 Autobahn Sondernutzung Formulieren, Str 025 Autobahn Einwendung Bauen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und l... |
| `str-bruecke-dashboard-tunnel-baulast-widmung` | Str 090 Bruecke Dashboard Erstellen, Str 091 Tunnel Baulast Prüfen, Str 092 Tunnel Widmung Lesen, Str 093 Tunnel Planrecht Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den näch... |
| `str-bruecke-eilantrag-kostenlast-unterhaltung` | Str 086 Bruecke Eilantrag Skizzieren, Str 087 Bruecke Kostenlast Prüfen, Str 088 Bruecke Unterhaltung Ruegen, Str 089 Bruecke Dokumente Sortieren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und... |
| `str-bruecke-widmung-planrecht-sondernutzung` | Str 082 Bruecke Widmung Lesen, Str 083 Bruecke Planrecht Prüfen, Str 084 Bruecke Sondernutzung Formulieren, Str 085 Bruecke Einwendung Bauen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefe... |
| `str-bundesfernstrasse-landesstrasse` | Str 002 Bundesfernstrasse Oder Landesstrasse, Str 003 Strassenbaulasttraeger Bestimmen, Str 004 Widmung Und Einziehung Prüfen, Str 005 Umstufung Und Teileinziehung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Re... |
| `str-bundesstrasse-sondernutzung-einwendung` | Str 034 Bundesstrasse Sondernutzung Formuliere, Str 035 Bundesstrasse Einwendung Bauen, Str 036 Bundesstrasse Eilantrag Skizzieren, Str 037 Bundesstrasse Kostenlast Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Beleg... |
| `str-bundesstrasse-unterhaltung-dokumente` | Str 038 Bundesstrasse Unterhaltung Ruegen, Str 039 Bundesstrasse Dokumente Sortieren, Str 040 Bundesstrasse Dashboard Erstellen, Str 041 Landesstrasse Baulast Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und... |
| `str-eilrechtsschutz-aktenplan-infrastruktur` | Str 018 Eilrechtsschutz Gegen Bau, Str 019 Aktenplan Infrastruktur, Str 020 Landesstrassengesetz Livecheck, Str 021 Autobahn Baulast Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefer... |
| `str-gemeindestrasse-dashboard-ortsdurchfahrt` | Str 070 Gemeindestrasse Dashboard Erstellen, Str 071 Ortsdurchfahrt Baulast Prüfen, Str 072 Ortsdurchfahrt Widmung Lesen, Str 073 Ortsdurchfahrt Planrecht Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rech... |
| `str-gemeindestrasse-eilantrag-kostenlast` | Str 066 Gemeindestrasse Eilantrag Skizzieren, Str 067 Gemeindestrasse Kostenlast Prüfen, Str 068 Gemeindestrasse Unterhaltung Ruegen, Str 069 Gemeindestrasse Dokumente Sortieren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit,... |
| `str-gemeindestrasse-widmung-planrecht` | Str 062 Gemeindestrasse Widmung Lesen, Str 063 Gemeindestrasse Planrecht Prüfen, Str 064 Gemeindestrasse Sondernutzung Formulie, Str 065 Gemeindestrasse Einwendung Bauen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege... |
| `str-kreisstrasse-sondernutzung-einwendung` | Str 054 Kreisstrasse Sondernutzung Formulieren, Str 055 Kreisstrasse Einwendung Bauen, Str 056 Kreisstrasse Eilantrag Skizzieren, Str 057 Kreisstrasse Kostenlast Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege u... |
| `str-kreisstrasse-unterhaltung-dokumente` | Str 058 Kreisstrasse Unterhaltung Ruegen, Str 059 Kreisstrasse Dokumente Sortieren, Str 060 Kreisstrasse Dashboard Erstellen, Str 061 Gemeindestrasse Baulast Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und R... |
| `str-kreuzungsrecht-strassenausbaubeitrag` | Str 014 Kreuzungsrecht Bahn Wasser Strasse, Str 015 Strassenausbaubeitrag Prüfen, Str 016 Unterhaltungspflicht Und Winterdienst, Str 017 Schaeden Durch Strasse: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechts... |
| `str-landesstrasse-eilantrag-kostenlast` | Str 046 Landesstrasse Eilantrag Skizzieren, Str 047 Landesstrasse Kostenlast Prüfen, Str 048 Landesstrasse Unterhaltung Ruegen, Str 049 Landesstrasse Dokumente Sortieren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege... |
| `str-landesstrasse-widmung-planrecht` | Str 042 Landesstrasse Widmung Lesen, Str 043 Landesstrasse Planrecht Prüfen, Str 044 Landesstrasse Sondernutzung Formuliere, Str 045 Landesstrasse Einwendung Bauen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Re... |
| `str-ortsdurchfahrt-sondernutzung-einwendung` | Str 074 Ortsdurchfahrt Sondernutzung Formulier, Str 075 Ortsdurchfahrt Einwendung Bauen, Str 076 Ortsdurchfahrt Eilantrag Skizzieren, Str 077 Ortsdurchfahrt Kostenlast Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Be... |
| `str-ortsdurchfahrt-unterhaltung-dokumente` | Str 078 Ortsdurchfahrt Unterhaltung Ruegen, Str 079 Ortsdurchfahrt Dokumente Sortieren, Str 080 Ortsdurchfahrt Dashboard Erstellen, Str 081 Bruecke Baulast Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rec... |
| `str-planfeststellung-strasse-plangenehmigung` | Str 006 Planfeststellung Strasse, Str 007 Plangenehmigung Und Uvp, Str 008 Anliegergebrauch Abgrenzen, Str 009 Sondernutzungserlaubnis: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den... |
| `str-tunnel-sondernutzung-einwendung-bauen` | Str 094 Tunnel Sondernutzung Formulieren, Str 095 Tunnel Einwendung Bauen, Str 096 Tunnel Eilantrag Skizzieren, Str 097 Tunnel Kostenlast Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und l... |
| `strassenrecht-infrastruktur-kaltstart-triage` | Straßenrecht und Infrastruktur: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe. |
| `strassenrecht-infrastruktur-str-autobahn-dashboard-bundesstrasse` | Str Autobahn Dashboard Erstellen / Str Bundesstrasse Baulast Pruefen / Str Bundesstrasse Widmung Lesen / Str Bundesstrasse Planrecht Pruefen: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt... |
| `strassenrecht-infrastruktur-str-baustelle-verkehrsfuehrung` | Str Baustelle Verkehrsfuehrung / Str Strassenentwaesserung / Str Bruecke Tunnel / Str Rastanlage Nebenbetrieb: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |
| `strassenrecht-infrastruktur-str-landesstrasse-dashboard` | Str Landesstrasse Dashboard Erstellen / Str Kreisstrasse Baulast Pruefen / Str Kreisstrasse Widmung Lesen / Str Kreisstrasse Planrecht Pruefen: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeug... |
| `strassenrecht-infrastruktur-str-tunnel-unterhaltung-dokumente` | Str Tunnel Unterhaltung Ruegen / Str Tunnel Dokumente Sortieren: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
