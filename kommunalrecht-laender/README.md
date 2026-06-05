# Kommunalrecht der Länder

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`kommunalrecht-laender`) | [`kommunalrecht-laender.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kommunalrecht-laender.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Kommunalakte Morgenfurt** (`kommunalrecht-rathaus-morgenfurt-buergerentscheid-haushalt`) | [Gesamt-PDF lesen](../testakten/kommunalrecht-rathaus-morgenfurt-buergerentscheid-haushalt/gesamt-pdf/kommunalrecht-rathaus-morgenfurt-buergerentscheid-haushalt_gesamt.pdf) | [`testakte-kommunalrecht-rathaus-morgenfurt-buergerentscheid-haushalt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kommunalrecht-rathaus-morgenfurt-buergerentscheid-haushalt.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin ist die Werkbank für kommunale Selbstverwaltung: Rat, Bürgermeister, Landkreis, Satzung, Gebühren, Haushalt, Bürgerbegehren, Kommunalaufsicht, kommunale Unternehmen und Landesrecht.

## Start

Beginne mit `kommunalrecht-laender-allgemein`. Das Plugin fragt zuerst nach Rolle, Ziel, Frist, Behörde/Gericht/Register, vorhandenen Unterlagen und gewünschtem Output. Danach schlägt es die passenden Spezialskills aus diesem Plugin vor.

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

Automatisch generierte Komplett-Liste aller 29 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kom-001-kaltstart-kommunalrechtsfall` | Kommunalrecht der Länder: Kaltstart Kommunalrechtsfall. Kaltstart Kommunalrechtsfall im Fachgebiet Kommunalrecht der Länder als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |
| `kom-ausschuss-finanzierung-dashboard-bauen` | Kom 094 Ausschuss Finanzierung Erklaeren, Kom 095 Ausschuss Dashboard Bauen, Kom 096 Ausschuss Beteiligung Planen, Kom 097 Ortschaftsrat Landesrecht Routen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrun... |
| `kom-ausschuss-landesrecht-beschluss-bauen` | Kom 087 Ausschuss Landesrecht Routen, Kom 089 Ausschuss Beschluss Bauen, Kom 090 Ausschuss Satzung Redlinen, Kom 091 Ausschuss Gebuehr Kalkulieren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und... |
| `kom-buergermeister-finanzierung-dashboard` | Kom 074 Buergermeister Finanzierung Erklaeren, Kom 075 Buergermeister Dashboard Bauen, Kom 076 Buergermeister Beteiligung Planen, Kom 077 Landrat Landesrecht Routen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und R... |
| `kom-buergermeister-landesrecht-beschluss` | Kom 067 Buergermeister Landesrecht Routen, Kom 069 Buergermeister Beschluss Bauen, Kom 070 Buergermeister Satzung Redlinen, Kom 071 Buergermeister Gebuehr Kalkulieren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und... |
| `kom-einwohnerantrag-petition-haushalt` | Kom 009 Einwohnerantrag Und Petition, Kom 011 Haushalt Und Haushaltssicherung, Kom 012 Kommunales Unternehmen, Kom 013 Oeffentliche Einrichtung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und li... |
| `kom-gemeinderat-gebuehr-aufsichtsbeschwerde` | Kom 041 Gemeinderat Gebuehr Kalkulieren, Kom 042 Gemeinderat Aufsichtsbeschwerde Schrei, Kom 043 Gemeinderat Eilantrag Vorbereiten, Kom 044 Gemeinderat Finanzierung Erklaeren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Be... |
| `kom-kita-satzung-beschluss-bauen-redlinen` | Kom 137 Kita Satzung Landesrecht Routen, Kom 139 Kita Satzung Beschluss Bauen, Kom 140 Kita Satzung Satzung Redlinen, Kom 141 Kita Satzung Gebuehr Kalkulieren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsg... |
| `kom-kita-satzung-dashboard-bauen-beteiligung` | Kom 144 Kita Satzung Finanzierung Erklaeren, Kom 145 Kita Satzung Dashboard Bauen, Kom 146 Kita Satzung Beteiligung Planen, Kom 147 Schultraeger Landesrecht Routen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Re... |
| `kom-kommunalabgabe-gebuehr` | Kom 121 Kommunalabgabe Gebuehr Kalkulieren, Kom 122 Kommunalabgabe Aufsichtsbeschwerde Sch, Kom 123 Kommunalabgabe Eilantrag Vorbereiten, Kom 124 Kommunalabgabe Finanzierung Erklaeren: wählt den konkreten Prüfpfad, trennt Frist, Zuständi... |
| `kom-kommunalaufsicht-finanzierung-dashboard` | Kom 114 Kommunalaufsicht Finanzierung Erklaere, Kom 115 Kommunalaufsicht Dashboard Bauen, Kom 116 Kommunalaufsicht Beteiligung Planen, Kom 127 Strassenreinigung Landesrecht Routen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkei... |
| `kom-kommunalaufsicht-landesrecht-beschluss` | Kom 107 Kommunalaufsicht Landesrecht Routen, Kom 109 Kommunalaufsicht Beschluss Bauen, Kom 110 Kommunalaufsicht Satzung Redlinen, Kom 111 Kommunalaufsicht Gebuehr Kalkulieren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Be... |
| `kom-kommunaler-finanzausgleich-interkommunale` | Kom 016 Kommunaler Finanzausgleich, Kom 017 Interkommunale Zusammenarbeit, Kom 018 Informationsrechte Ratsmitglied, Kom 019 Eilrechtsschutz Kommunalstreit: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrund... |
| `kom-kommunalrecht-bayern-berlin-routen` | Kom 022 Kommunalrecht Bayern Routen, Kom 023 Kommunalrecht Berlin Routen, Kom 024 Kommunalrecht Brandenburg Routen, Kom 025 Kommunalrecht Bremen Routen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlag... |
| `kom-kommunalrecht-mecklenburg-niedersachsen` | Kom 028 Kommunalrecht Mecklenburg Vorpommern R, Kom 029 Kommunalrecht Niedersachsen Routen, Kom 030 Kommunalrecht Nordrhein Westfalen Rout, Kom 031 Kommunalrecht Rheinland Pfalz Routen: wählt den konkreten Prüfpfad, trennt Frist, Zuständ... |
| `kom-kommunalrecht-sachsen-schleswig-holstein` | Kom 034 Kommunalrecht Sachsen Anhalt Routen, Kom 035 Kommunalrecht Schleswig Holstein Route, Kom 036 Kommunalrecht Thueringen Routen, Kom 037 Gemeinderat Landesrecht Routen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Bele... |
| `kom-kreistag-gebuehr-aufsichtsbeschwerde` | Kom 061 Kreistag Gebuehr Kalkulieren, Kom 062 Kreistag Aufsichtsbeschwerde Schreiben, Kom 063 Kreistag Eilantrag Vorbereiten, Kom 064 Kreistag Finanzierung Erklaeren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und... |
| `kom-landrat-gebuehr-aufsichtsbeschwerde` | Kom 081 Landrat Gebuehr Kalkulieren, Kom 082 Landrat Aufsichtsbeschwerde Schreiben, Kom 083 Landrat Eilantrag Vorbereiten, Kom 084 Landrat Finanzierung Erklaeren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rech... |
| `kom-organ-gemeinderat-stadtrat-kreistag` | Kom 003 Organ Und Zustaendigkeit Prüfen, Kom 038 Gemeinderat Zustaendigkeit Prüfen, Kom 048 Stadtrat Zustaendigkeit Prüfen, Kom 058 Kreistag Zustaendigkeit Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rec... |
| `kom-ortschaftsrat-gebuehr-aufsichtsbeschwerde` | Kom 101 Ortschaftsrat Gebuehr Kalkulieren, Kom 102 Ortschaftsrat Aufsichtsbeschwerde Schr, Kom 103 Ortschaftsrat Eilantrag Vorbereiten, Kom 104 Ortschaftsrat Finanzierung Erklaeren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigke... |
| `kom-schultraeger-gebuehr-aufsichtsbeschwerde` | Kom 151 Schultraeger Gebuehr Kalkulieren, Kom 152 Schultraeger Aufsichtsbeschwerde Schre, Kom 153 Schultraeger Eilantrag Vorbereiten, Kom 154 Schultraeger Finanzierung Erklaeren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit,... |
| `kom-stadtrat-finanzierung-dashboard-bauen` | Kom 054 Stadtrat Finanzierung Erklaeren, Kom 055 Stadtrat Dashboard Bauen, Kom 056 Stadtrat Beteiligung Planen, Kom 057 Kreistag Landesrecht Routen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage un... |
| `kom-stadtrat-landesrecht-beschluss-bauen` | Kom 047 Stadtrat Landesrecht Routen, Kom 049 Stadtrat Beschluss Bauen, Kom 050 Stadtrat Satzung Redlinen, Kom 051 Stadtrat Gebuehr Kalkulieren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und lie... |
| `kommunalrecht-laender-kaltstart-triage` | Kommunalrecht der Länder: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe. |
| `kommunalrecht-laender-kom-ausschuss-zustaendigkeit-ortschaftsrat` | Kom Ausschuss Zustaendigkeit Pruefen / Kom Ortschaftsrat Zustaendigkeit Pruefen / Kom Kommunalaufsicht Zustaendigkeit Pruefe / Kom Kommunalabgabe Zustaendigkeit Pruefen / 2 ergänzende Prüffelder: bearbeitet die maßgeblichen Prüffelder, s... |
| `kommunalrecht-laender-kom-feuerwehr-landesrecht-beschluss` | Kom Feuerwehr Landesrecht Routen / Kom Feuerwehr Beschluss Bauen: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |
| `kommunalrecht-laender-kom-gemeinde-stadt-ratssitzung` | Kom Gemeinde Stadt Landkreis Zuordnen / Kom Ratssitzung Tagesordnung / Kom Beschluss Befangenheit / Kom Satzung Entwerfen Pruefen / 2 ergänzende Prüffelder: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt... |
| `kommunalrecht-laender-kom-schultraeger-zustaendigkeit-feuerwehr` | Kom Schultraeger Zustaendigkeit Pruefen / Kom Feuerwehr Zustaendigkeit Pruefen / Kom Kommunalabgaben Pruefen / Kom Kommunalabgabe Landesrecht Routen / 2 ergänzende Prüffelder: bearbeitet die maßgeblichen Prüffelder, setzt den passenden P... |
| `kommunalrecht-laender-kom-strassenreinigung-gebuehr` | Kom Strassenreinigung Gebuehr Kalkulieren / Kom Strassenreinigung Aufsichtsbeschwerde / Kom Strassenreinigung Eilantrag Vorbereite / Kom Strassenreinigung Finanzierung Erklaer / 2 ergänzende Prüffelder: bearbeitet die maßgeblichen Prüffe... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
