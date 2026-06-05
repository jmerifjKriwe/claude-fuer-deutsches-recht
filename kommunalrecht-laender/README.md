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
| `kom-ausschuss-finanzierung-dashboard-bauen` | KOM Ausschuss Finanzierung Dashboard Bauen: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kom-ausschuss-landesrecht-beschluss-bauen` | KOM Ausschuss Landesrecht Beschluss Bauen: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kom-buergermeister-finanzierung-dashboard` | KOM Buergermeister Finanzierung Dashboard: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kom-buergermeister-landesrecht-beschluss` | KOM Buergermeister Landesrecht Beschluss: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kom-einwohnerantrag-petition-haushalt` | KOM Einwohnerantrag Petition Haushalt: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kom-gemeinderat-gebuehr-aufsichtsbeschwerde` | KOM Gemeinderat Gebuehr Aufsichtsbeschwerde: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kom-kita-satzung-beschluss-bauen-redlinen` | KOM Kita Satzung Beschluss Bauen Redlinen: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kom-kita-satzung-dashboard-bauen-beteiligung` | KOM Kita Satzung Dashboard Bauen Beteiligung: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kom-kommunalabgabe-gebuehr` | KOM Kommunalabgabe Gebuehr: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kom-kommunalaufsicht-finanzierung-dashboard` | KOM Kommunalaufsicht Finanzierung Dashboard: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kom-kommunalaufsicht-landesrecht-beschluss` | KOM Kommunalaufsicht Landesrecht Beschluss: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kom-kommunaler-finanzausgleich-interkommunale` | KOM Kommunaler Finanzausgleich Interkommunale: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kom-kommunalrecht-bayern-berlin-routen` | KOM Kommunalrecht Bayern Berlin Routen: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kom-kommunalrecht-mecklenburg-niedersachsen` | KOM Kommunalrecht Mecklenburg Niedersachsen: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kom-kommunalrecht-sachsen-schleswig-holstein` | KOM Kommunalrecht Sachsen Schleswig Holstein: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kom-kreistag-gebuehr-aufsichtsbeschwerde` | KOM Kreistag Gebuehr Aufsichtsbeschwerde: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kom-landrat-gebuehr-aufsichtsbeschwerde` | KOM Landrat Gebuehr Aufsichtsbeschwerde: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kom-organ-gemeinderat-stadtrat-kreistag` | KOM Organ Gemeinderat Stadtrat Kreistag: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kom-ortschaftsrat-gebuehr-aufsichtsbeschwerde` | KOM Ortschaftsrat Gebuehr Aufsichtsbeschwerde: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kom-schultraeger-gebuehr-aufsichtsbeschwerde` | KOM Schultraeger Gebuehr Aufsichtsbeschwerde: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kom-stadtrat-finanzierung-dashboard-bauen` | KOM Stadtrat Finanzierung Dashboard Bauen: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kom-stadtrat-landesrecht-beschluss-bauen` | KOM Stadtrat Landesrecht Beschluss Bauen: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kommunalrecht-laender-kaltstart-triage` | Kommunalrecht der Länder: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe. |
| `kommunalrecht-laender-kom-ausschuss-zustaendigkeit-ortschaftsrat` | KOM Ausschuss Zustaendigkeit Ortschaftsrat: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kommunalrecht-laender-kom-feuerwehr-landesrecht-beschluss` | KOM Feuerwehr Landesrecht Beschluss: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kommunalrecht-laender-kom-gemeinde-stadt-ratssitzung` | KOM Gemeinde Stadt Ratssitzung: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kommunalrecht-laender-kom-schultraeger-zustaendigkeit-feuerwehr` | KOM Schultraeger Zustaendigkeit Feuerwehr: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kommunalrecht-laender-kom-strassenreinigung-gebuehr` | KOM Strassenreinigung Gebuehr: bündelt 6 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
