# Informationsfreiheit und Presseauskunft

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`informationsfreiheit-presseauskunft`) | [`informationsfreiheit-presseauskunft.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/informationsfreiheit-presseauskunft.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **IFG-/Presseauskunftsakte Hafenstadt** (`informationsfreiheit-presseauskunft-klinikdaten-hafenstadt`) | [Gesamt-PDF lesen](../testakten/informationsfreiheit-presseauskunft-klinikdaten-hafenstadt/gesamt-pdf/informationsfreiheit-presseauskunft-klinikdaten-hafenstadt_gesamt.pdf) | [`testakte-informationsfreiheit-presseauskunft-klinikdaten-hafenstadt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-informationsfreiheit-presseauskunft-klinikdaten-hafenstadt.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin ist das Cockpit für Menschen, Journalistinnen, Kanzleien, NGOs und Unternehmen, die amtliche Informationen bekommen wollen, ohne an Zuständigkeitsnebel, Gebührenbescheiden oder Ausweichantworten hängen zu bleiben.

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
| `allgemein` | Informationsfreiheit und Presseauskunft: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Spezialskill-Routing und erste Ausgabe. |
| `ifg-001-kaltstart-informationsbegehren-sortier` | Informationsfreiheit und Presseauskunft: Kaltstart Informationsbegehren sortieren. Kaltstart Informationsbegehren sortieren im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und A... |
| `kompendium-01-ifg-006-fristenkalen-bis-ifg-048-ifggebv-gebu` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 01; bündelt 4 frühere Spezialskills (ifg-006-fristenkalender-und-untaetigkeitstrack, ifg-038-ifg-bund-zustaendigkeit-pruefen, ifg-039-ifg-bund-frist-setzen, ifg-048-ifg... |
| `kompendium-02-ifg-049-ifggebv-gebu-bis-ifg-069-vig-lebensmi` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 02; bündelt 4 frühere Spezialskills (ifg-049-ifggebv-gebuehren-frist-setzen, ifg-058-uig-umweltinformation-zustaendigkeit-p, ifg-059-uig-umweltinformation-frist-setzen,... |
| `kompendium-03-ifg-078-landespresse-bis-ifg-089-transparenzg` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 03; bündelt 4 frühere Spezialskills (ifg-078-landespressegesetz-zustaendigkeit-prue, ifg-079-landespressegesetz-frist-setzen, ifg-088-transparenzgesetz-zustaendigkeit-p... |
| `kompendium-04-ifg-098-archivrecht-bis-ifg-003-bundesbehoer` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 04; bündelt 4 frühere Spezialskills (ifg-098-archivrecht-zustaendigkeit-pruefen, ifg-099-archivrecht-frist-setzen, ifg-002-ifg-oder-presseauskunft-richtig-routen, ifg-0... |
| `kompendium-05-ifg-004-kein-ifg-im-bis-ifg-008-personenbezo` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 05; bündelt 4 frühere Spezialskills (ifg-004-kein-ifg-im-land-ersatzwege-finden, ifg-005-kostenrisiko-und-gebuehrenankuendigung, ifg-007-drittbeteiligung-bei-betriebsge... |
| `kompendium-06-ifg-009-uig-und-umwe-bis-ifg-012-presseanfrag` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 06; bündelt 4 frühere Spezialskills (ifg-009-uig-und-umweltinformationen-abgrenzen, ifg-010-vig-und-verbraucherinformationen-nutze, ifg-011-akteneinsicht-oder-auskunft-... |
| `kompendium-07-ifg-013-ablehnungsbe-bis-ifg-016-gebuehrenbes` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 07; bündelt 4 frühere Spezialskills (ifg-013-ablehnungsbescheid-in-angriffspunkte-z, ifg-014-widerspruch-gegen-ifg-ablehnung, ifg-015-verpflichtungsklage-und-eilrechtss... |
| `kompendium-08-ifg-017-informations-bis-ifg-020-veroeffentli` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 08; bündelt 4 frühere Spezialskills (ifg-017-informationszugang-bei-beliehenen-priv, ifg-018-parlaments-und-rechnungshofgrenzen, ifg-019-sicherheitsinteressen-und-gehei... |
| `kompendium-09-ifg-021-informations-bis-ifg-024-informations` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 09; bündelt 4 frühere Spezialskills (ifg-021-informationszugang-baden-wuerttemberg, ifg-022-informationszugang-bayern-livecheck, ifg-023-informationszugang-berlin-livec... |
| `kompendium-10-ifg-025-informations-bis-ifg-028-informations` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 10; bündelt 4 frühere Spezialskills (ifg-025-informationszugang-bremen-livecheck, ifg-026-informationszugang-hamburg-livecheck, ifg-027-informationszugang-hessen-livech... |
| `kompendium-11-ifg-029-informations-bis-ifg-032-informations` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 11; bündelt 4 frühere Spezialskills (ifg-029-informationszugang-niedersachsen-livec, ifg-030-informationszugang-nordrhein-westfalen, ifg-031-informationszugang-rheinlan... |
| `kompendium-12-ifg-033-informations-bis-ifg-036-informations` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 12; bündelt 4 frühere Spezialskills (ifg-033-informationszugang-sachsen-livecheck, ifg-034-informationszugang-sachsen-anhalt-live, ifg-035-informationszugang-schleswig-... |
| `kompendium-13-ifg-037-ifg-bund-ant-bis-ifg-042-ifg-bund-dri` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 13; bündelt 4 frühere Spezialskills (ifg-037-ifg-bund-antrag-formulieren, ifg-040-ifg-bund-kosten-deckeln, ifg-041-ifg-bund-schwaerzung-angreifen, ifg-042-ifg-bund-drit... |
| `kompendium-14-ifg-043-ifg-bund-wid-bis-ifg-046-ifg-bund-tra` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 14; bündelt 4 frühere Spezialskills (ifg-043-ifg-bund-widerspruch-bauen, ifg-044-ifg-bund-klage-vorbereiten, ifg-045-ifg-bund-presseantwort-nachfassen, ifg-046-ifg-bund... |
| `kompendium-15-ifg-047-ifggebv-gebu-bis-ifg-052-ifggebv-gebu` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 15; bündelt 4 frühere Spezialskills (ifg-047-ifggebv-gebuehren-antrag-formulieren, ifg-050-ifggebv-gebuehren-kosten-deckeln, ifg-051-ifggebv-gebuehren-schwaerzung-angre... |
| `kompendium-16-ifg-053-ifggebv-gebu-bis-ifg-056-ifggebv-gebu` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 16; bündelt 4 frühere Spezialskills (ifg-053-ifggebv-gebuehren-widerspruch-bauen, ifg-054-ifggebv-gebuehren-klage-vorbereiten, ifg-055-ifggebv-gebuehren-presseantwort-n... |
| `kompendium-17-ifg-057-uig-umweltin-bis-ifg-062-uig-umweltin` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 17; bündelt 4 frühere Spezialskills (ifg-057-uig-umweltinformation-antrag-formulier, ifg-060-uig-umweltinformation-kosten-deckeln, ifg-061-uig-umweltinformation-schwaer... |
| `kompendium-18-ifg-063-uig-umweltin-bis-ifg-066-uig-umweltin` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 18; bündelt 4 frühere Spezialskills (ifg-063-uig-umweltinformation-widerspruch-baue, ifg-064-uig-umweltinformation-klage-vorbereite, ifg-065-uig-umweltinformation-press... |
| `kompendium-19-ifg-067-vig-lebensmi-bis-ifg-071-vig-lebensmi` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 19; bündelt 4 frühere Spezialskills (ifg-067-vig-lebensmittel-und-produkte-antrag-f, ifg-068-vig-lebensmittel-und-produkte-zustaend, ifg-070-vig-lebensmittel-und-produk... |
| `kompendium-20-ifg-072-vig-lebensmi-bis-ifg-075-vig-lebensmi` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 20; bündelt 4 frühere Spezialskills (ifg-072-vig-lebensmittel-und-produkte-drittanh, ifg-073-vig-lebensmittel-und-produkte-widerspr, ifg-074-vig-lebensmittel-und-produk... |
| `kompendium-21-ifg-076-vig-lebensmi-bis-ifg-081-landespresse` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 21; bündelt 4 frühere Spezialskills (ifg-076-vig-lebensmittel-und-produkte-tracking, ifg-077-landespressegesetz-antrag-formulieren, ifg-080-landespressegesetz-kosten-de... |
| `kompendium-22-ifg-082-landespresse-bis-ifg-085-landespresse` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 22; bündelt 4 frühere Spezialskills (ifg-082-landespressegesetz-drittanhoerung-begl, ifg-083-landespressegesetz-widerspruch-bauen, ifg-084-landespressegesetz-klage-vorb... |
| `kompendium-23-ifg-086-landespresse-bis-ifg-091-transparenzg` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 23; bündelt 4 frühere Spezialskills (ifg-086-landespressegesetz-tracking-aktualisie, ifg-087-transparenzgesetz-antrag-formulieren, ifg-090-transparenzgesetz-kosten-deck... |
| `kompendium-24-ifg-092-transparenzg-bis-ifg-095-transparenzg` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 24; bündelt 4 frühere Spezialskills (ifg-092-transparenzgesetz-drittanhoerung-begle, ifg-093-transparenzgesetz-widerspruch-bauen, ifg-094-transparenzgesetz-klage-vorber... |
| `kompendium-25-ifg-096-transparenzg-bis-ifg-097-archivrecht` | informationsfreiheit-presseauskunft: Konsolidiertes Skill-Kompendium 25; bündelt 2 frühere Spezialskills (ifg-096-transparenzgesetz-tracking-aktualisier, ifg-097-archivrecht-antrag-formulieren) und bewahrt deren Workflows, Normanker, Prü... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
