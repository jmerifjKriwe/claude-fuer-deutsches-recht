# Straßenverkehrsrecht StVO

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`strassenverkehrsrecht-stvo`) | [`strassenverkehrsrecht-stvo.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strassenverkehrsrecht-stvo.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **StVO-Akte Schulstraße/Lieferzone** (`strassenverkehrsrecht-stvo-schulstrasse-lieferzone`) | [Gesamt-PDF lesen](../testakten/strassenverkehrsrecht-stvo-schulstrasse-lieferzone/gesamt-pdf/strassenverkehrsrecht-stvo-schulstrasse-lieferzone_gesamt.pdf) | [`testakte-strassenverkehrsrecht-stvo-schulstrasse-lieferzone.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strassenverkehrsrecht-stvo-schulstrasse-lieferzone.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin erklärt und prüft das Verhalten im Straßenverkehr und die behördliche Verkehrssteuerung: StVO, StVG, FeV, Zeichen, Anordnungen, Sondernutzungsschnittstellen, Ausnahmegenehmigung und Rechtsschutz.

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
| `allgemein` | Straßenverkehrsrecht StVO: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Spezialskill-Routing und erste Ausgabe. |
| `kompendium-01-stv-017-bussgeldschn-bis-stv-046-fahrradstras` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 01; bündelt 4 frühere Spezialskills (stv-017-bussgeldschnittstelle-owig, stv-026-haltverbot-bussgeld-abgrenzen, stv-036-tempo-30-bussgeld-abgrenzen, stv-046-fahrradstrasse-bussg... |
| `kompendium-02-stv-056-busspur-buss-bis-stv-086-ladezone-bus` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 02; bündelt 4 frühere Spezialskills (stv-056-busspur-bussgeld-abgrenzen, stv-066-bewohnerparken-bussgeld-abgrenzen, stv-076-lieferzone-bussgeld-abgrenzen, stv-086-ladezone-bussg... |
| `kompendium-03-stv-096-schulstrasse-bis-stv-004-tempozone-un` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 03; bündelt 4 frühere Spezialskills (stv-096-schulstrasse-bussgeld-abgrenzen, stv-002-verkehrszeichen-lesen, stv-003-verkehrsrechtliche-anordnung-pruefen, stv-004-tempozone-und-... |
| `kompendium-04-stv-005-parken-halte-bis-stv-008-e-scooter-un` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 04; bündelt 4 frühere Spezialskills (stv-005-parken-halten-abschleppen, stv-006-ausnahmegenehmigung-beantragen, stv-007-radverkehr-und-schutzstreifen, stv-008-e-scooter-und-mikr... |
| `kompendium-05-stv-009-schwertransp-bis-stv-012-fahrtenbucha` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 05; bündelt 4 frühere Spezialskills (stv-009-schwertransport-und-erlaubnis, stv-010-fahrerlaubnis-schnittstelle, stv-011-mpu-und-fahreignung, stv-012-fahrtenbuchauflage) und bew... |
| `kompendium-06-stv-013-gefahrenstel-bis-stv-016-blaulicht-un` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 06; bündelt 4 frühere Spezialskills (stv-013-gefahrenstelle-melden, stv-014-schulweg-und-verkehrsberuhigung, stv-015-baustellenverkehrsrecht, stv-016-blaulicht-und-sonderrechte)... |
| `kompendium-07-stv-018-widerspruch-bis-stv-021-haltverbot-r` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 07; bündelt 4 frühere Spezialskills (stv-018-widerspruch-gegen-verkehrszeichen, stv-019-eilrechtsschutz-verkehrszeichen, stv-020-kommunikation-mit-strassenverkehrsbeho, stv-021-... |
| `kompendium-08-stv-022-haltverbot-z-bis-stv-025-haltverbot-b` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 08; bündelt 4 frühere Spezialskills (stv-022-haltverbot-zeichen-auslegen, stv-023-haltverbot-anordnung-angreifen, stv-024-haltverbot-antrag-schreiben, stv-025-haltverbot-beweis-... |
| `kompendium-09-stv-027-haltverbot-e-bis-stv-030-haltverbot-r` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 09; bündelt 4 frühere Spezialskills (stv-027-haltverbot-eilrechtsschutz-planen, stv-028-haltverbot-behoerde-anschreiben, stv-029-haltverbot-karte-bauen, stv-030-haltverbot-risik... |
| `kompendium-10-stv-031-tempo-30-reg-bis-stv-034-tempo-30-ant` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 10; bündelt 4 frühere Spezialskills (stv-031-tempo-30-regel-pruefen, stv-032-tempo-30-zeichen-auslegen, stv-033-tempo-30-anordnung-angreifen, stv-034-tempo-30-antrag-schreiben)... |
| `kompendium-11-stv-035-tempo-30-bew-bis-stv-039-tempo-30-kar` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 11; bündelt 4 frühere Spezialskills (stv-035-tempo-30-beweis-sichern, stv-037-tempo-30-eilrechtsschutz-planen, stv-038-tempo-30-behoerde-anschreiben, stv-039-tempo-30-karte-baue... |
| `kompendium-12-stv-040-tempo-30-ris-bis-stv-043-fahrradstras` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 12; bündelt 4 frühere Spezialskills (stv-040-tempo-30-risiko-erklaeren, stv-041-fahrradstrasse-regel-pruefen, stv-042-fahrradstrasse-zeichen-auslegen, stv-043-fahrradstrasse-ano... |
| `kompendium-13-stv-044-fahrradstras-bis-stv-048-fahrradstras` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 13; bündelt 4 frühere Spezialskills (stv-044-fahrradstrasse-antrag-schreiben, stv-045-fahrradstrasse-beweis-sichern, stv-047-fahrradstrasse-eilrechtsschutz-planen, stv-048-fahrr... |
| `kompendium-14-stv-049-fahrradstras-bis-stv-052-busspur-zeic` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 14; bündelt 4 frühere Spezialskills (stv-049-fahrradstrasse-karte-bauen, stv-050-fahrradstrasse-risiko-erklaeren, stv-051-busspur-regel-pruefen, stv-052-busspur-zeichen-auslegen... |
| `kompendium-15-stv-053-busspur-anor-bis-stv-057-busspur-eilr` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 15; bündelt 4 frühere Spezialskills (stv-053-busspur-anordnung-angreifen, stv-054-busspur-antrag-schreiben, stv-055-busspur-beweis-sichern, stv-057-busspur-eilrechtsschutz-plane... |
| `kompendium-16-stv-058-busspur-beho-bis-stv-061-bewohnerpark` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 16; bündelt 4 frühere Spezialskills (stv-058-busspur-behoerde-anschreiben, stv-059-busspur-karte-bauen, stv-060-busspur-risiko-erklaeren, stv-061-bewohnerparken-regel-pruefen) u... |
| `kompendium-17-stv-062-bewohnerpark-bis-stv-065-bewohnerpark` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 17; bündelt 4 frühere Spezialskills (stv-062-bewohnerparken-zeichen-auslegen, stv-063-bewohnerparken-anordnung-angreifen, stv-064-bewohnerparken-antrag-schreiben, stv-065-bewohn... |
| `kompendium-18-stv-067-bewohnerpark-bis-stv-070-bewohnerpark` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 18; bündelt 4 frühere Spezialskills (stv-067-bewohnerparken-eilrechtsschutz-planen, stv-068-bewohnerparken-behoerde-anschreiben, stv-069-bewohnerparken-karte-bauen, stv-070-bewo... |
| `kompendium-19-stv-071-lieferzone-r-bis-stv-074-lieferzone-a` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 19; bündelt 4 frühere Spezialskills (stv-071-lieferzone-regel-pruefen, stv-072-lieferzone-zeichen-auslegen, stv-073-lieferzone-anordnung-angreifen, stv-074-lieferzone-antrag-sch... |
| `kompendium-20-stv-075-lieferzone-b-bis-stv-079-lieferzone-k` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 20; bündelt 4 frühere Spezialskills (stv-075-lieferzone-beweis-sichern, stv-077-lieferzone-eilrechtsschutz-planen, stv-078-lieferzone-behoerde-anschreiben, stv-079-lieferzone-ka... |
| `kompendium-21-stv-080-lieferzone-r-bis-stv-083-ladezone-ano` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 21; bündelt 4 frühere Spezialskills (stv-080-lieferzone-risiko-erklaeren, stv-081-ladezone-regel-pruefen, stv-082-ladezone-zeichen-auslegen, stv-083-ladezone-anordnung-angreifen... |
| `kompendium-22-stv-084-ladezone-ant-bis-stv-088-ladezone-beh` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 22; bündelt 4 frühere Spezialskills (stv-084-ladezone-antrag-schreiben, stv-085-ladezone-beweis-sichern, stv-087-ladezone-eilrechtsschutz-planen, stv-088-ladezone-behoerde-ansch... |
| `kompendium-23-stv-089-ladezone-kar-bis-stv-092-schulstrasse` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 23; bündelt 4 frühere Spezialskills (stv-089-ladezone-karte-bauen, stv-090-ladezone-risiko-erklaeren, stv-091-schulstrasse-regel-pruefen, stv-092-schulstrasse-zeichen-auslegen)... |
| `kompendium-24-stv-093-schulstrasse-bis-stv-097-schulstrasse` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 24; bündelt 4 frühere Spezialskills (stv-093-schulstrasse-anordnung-angreifen, stv-094-schulstrasse-antrag-schreiben, stv-095-schulstrasse-beweis-sichern, stv-097-schulstrasse-e... |
| `kompendium-25-stv-098-schulstrasse-bis-stv-099-schulstrasse` | strassenverkehrsrecht-stvo: Konsolidiertes Skill-Kompendium 25; bündelt 2 frühere Spezialskills (stv-098-schulstrasse-behoerde-anschreiben, stv-099-schulstrasse-karte-bauen) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausga... |
| `stv-001-kaltstart-stvo-fall` | Straßenverkehrsrecht StVO: Kaltstart StVO-Fall. Kaltstart StVO-Fall im Fachgebiet Straßenverkehrsrecht StVO als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
