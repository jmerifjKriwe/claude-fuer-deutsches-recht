# Verbraucherschutzverband Durchsetzung

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`verbraucherschutzverband-durchsetzung`) | [`verbraucherschutzverband-durchsetzung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verbraucherschutzverband-durchsetzung.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Verbandsakte Abo-Falle** (`verbraucherschutzverband-abo-falle-sammelklage`) | [Gesamt-PDF lesen](../testakten/verbraucherschutzverband-abo-falle-sammelklage/gesamt-pdf/verbraucherschutzverband-abo-falle-sammelklage_gesamt.pdf) | [`testakte-verbraucherschutzverband-abo-falle-sammelklage.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verbraucherschutzverband-abo-falle-sammelklage.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin arbeitet aus Sicht einer klageberechtigten Stelle: es sortiert Massenphänomene, Betroffenendaten, Anspruchsgruppen, Klageart, Finanzierung, Registerkommunikation, Vergleich und Umsetzung.

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

Automatisch generierte Komplett-Liste aller 28 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Verbraucherschutzverband Durchsetzung: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Spezialskill-Routing und erste Ausgabe. |
| `kompendium-01-vdg-014-umsetzungsve-bis-vdg-033-telekommunik` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 01; bündelt 4 frühere Spezialskills (vdg-014-umsetzungsverfahren-planen, vdg-031-telekommunikationsklausel-sammelfaehig, vdg-032-telekommunikationsklausel-klageschrif... |
| `kompendium-02-vdg-034-telekommunik-bis-vdg-037-telekommunik` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 02; bündelt 4 frühere Spezialskills (vdg-034-telekommunikationsklausel-registertext, vdg-035-telekommunikationsklausel-betroffenenf, vdg-036-telekommunikationsklausel... |
| `kompendium-03-vdg-038-telekommunik-bis-vdg-106-diesel-diffe` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 03; bündelt 4 frühere Spezialskills (vdg-038-telekommunikationsklausel-umsetzung-ue, vdg-039-telekommunikationsklausel-kommunikatio, vdg-040-telekommunikationsklausel... |
| `kompendium-04-vdg-029-bankentgelte-bis-vdg-069-abo-modell-k` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 04; bündelt 4 frühere Spezialskills (vdg-029-bankentgelte-kommunikation-steuern, vdg-049-energiepreiserhoehung-kommunikation-st, vdg-059-plattform-sperre-kommunikatio... |
| `kompendium-05-vdg-079-fitnessstudi-bis-vdg-002-klageberecht` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 05; bündelt 4 frühere Spezialskills (vdg-079-fitnessstudio-kommunikation-steuern, vdg-089-reiseveranstalter-kommunikation-steuer, vdg-099-flugportal-kommunikation-ste... |
| `kompendium-06-vdg-003-abhilfeklage-bis-vdg-006-quorum-und-b` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 06; bündelt 4 frühere Spezialskills (vdg-003-abhilfeklage-oder-musterfeststellung-w, vdg-004-uklag-unterlassung-gegen-agb, vdg-005-uwg-verbraucherinteressen-pruefen,... |
| `kompendium-07-vdg-007-finanzierung-bis-vdg-010-lebenssachve` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 07; bündelt 4 frühere Spezialskills (vdg-007-finanzierung-und-interessenkonflikte, vdg-008-verbandsklageregister-vorbereiten, vdg-009-klageziele-praezise-schneiden, v... |
| `kompendium-08-vdg-011-beweismittel-bis-vdg-015-sachwalterfr` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 08; bündelt 4 frühere Spezialskills (vdg-011-beweismittel-offenlegung-nutzen, vdg-012-kommunikation-an-verbraucher, vdg-013-vergleich-und-austritt-pruefen, vdg-015-sa... |
| `kompendium-09-vdg-016-individualkl-bis-vdg-019-kosten-und-p` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 09; bündelt 4 frühere Spezialskills (vdg-016-individualklagen-koordinieren, vdg-017-presse-und-kampagnenrisiko, vdg-018-datenschutz-im-betroffenenpool, vdg-019-kosten... |
| `kompendium-10-vdg-020-erfolgsmonit-bis-vdg-023-bankentgelte` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 10; bündelt 4 frühere Spezialskills (vdg-020-erfolgsmonitoring, vdg-021-bankentgelte-sammelfaehigkeit-pruefen, vdg-022-bankentgelte-klageschrift-strukturiere, vdg-023... |
| `kompendium-11-vdg-024-bankentgelte-bis-vdg-027-bankentgelte` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 11; bündelt 4 frühere Spezialskills (vdg-024-bankentgelte-registertext-schreiben, vdg-025-bankentgelte-betroffenenformular-bauen, vdg-026-bankentgelte-beweisplan-erst... |
| `kompendium-12-vdg-028-bankentgelte-bis-vdg-042-energiepreis` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 12; bündelt 4 frühere Spezialskills (vdg-028-bankentgelte-umsetzung-ueberwachen, vdg-030-bankentgelte-risiko-rot-markieren, vdg-041-energiepreiserhoehung-sammelfaehig... |
| `kompendium-13-vdg-043-energiepreis-bis-vdg-046-energiepreis` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 13; bündelt 4 frühere Spezialskills (vdg-043-energiepreiserhoehung-anspruchsgruppen, vdg-044-energiepreiserhoehung-registertext-sch, vdg-045-energiepreiserhoehung-bet... |
| `kompendium-14-vdg-047-energiepreis-bis-vdg-051-plattform-sp` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 14; bündelt 4 frühere Spezialskills (vdg-047-energiepreiserhoehung-vergleich-pruefe, vdg-048-energiepreiserhoehung-umsetzung-ueberw, vdg-050-energiepreiserhoehung-ris... |
| `kompendium-15-vdg-052-plattform-sp-bis-vdg-055-plattform-sp` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 15; bündelt 4 frühere Spezialskills (vdg-052-plattform-sperre-klageschrift-struktur, vdg-053-plattform-sperre-anspruchsgruppen-bild, vdg-054-plattform-sperre-register... |
| `kompendium-16-vdg-056-plattform-sp-bis-vdg-060-plattform-sp` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 16; bündelt 4 frühere Spezialskills (vdg-056-plattform-sperre-beweisplan-erstellen, vdg-057-plattform-sperre-vergleich-pruefen, vdg-058-plattform-sperre-umsetzung-ueb... |
| `kompendium-17-vdg-061-abo-modell-s-bis-vdg-064-abo-modell-r` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 17; bündelt 4 frühere Spezialskills (vdg-061-abo-modell-sammelfaehigkeit-pruefen, vdg-062-abo-modell-klageschrift-strukturieren, vdg-063-abo-modell-anspruchsgruppen-b... |
| `kompendium-18-vdg-065-abo-modell-b-bis-vdg-068-abo-modell-u` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 18; bündelt 4 frühere Spezialskills (vdg-065-abo-modell-betroffenenformular-bauen, vdg-066-abo-modell-beweisplan-erstellen, vdg-067-abo-modell-vergleich-pruefen, vdg-... |
| `kompendium-19-vdg-070-abo-modell-r-bis-vdg-073-fitnessstudi` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 19; bündelt 4 frühere Spezialskills (vdg-070-abo-modell-risiko-rot-markieren, vdg-071-fitnessstudio-sammelfaehigkeit-pruefen, vdg-072-fitnessstudio-klageschrift-struk... |
| `kompendium-20-vdg-074-fitnessstudi-bis-vdg-077-fitnessstudi` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 20; bündelt 4 frühere Spezialskills (vdg-074-fitnessstudio-registertext-schreiben, vdg-075-fitnessstudio-betroffenenformular-baue, vdg-076-fitnessstudio-beweisplan-er... |
| `kompendium-21-vdg-078-fitnessstudi-bis-vdg-082-reiseveranst` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 21; bündelt 4 frühere Spezialskills (vdg-078-fitnessstudio-umsetzung-ueberwachen, vdg-080-fitnessstudio-risiko-rot-markieren, vdg-081-reiseveranstalter-sammelfaehigke... |
| `kompendium-22-vdg-083-reiseveranst-bis-vdg-086-reiseveranst` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 22; bündelt 4 frühere Spezialskills (vdg-083-reiseveranstalter-anspruchsgruppen-bil, vdg-084-reiseveranstalter-registertext-schreib, vdg-085-reiseveranstalter-betroff... |
| `kompendium-23-vdg-087-reiseveranst-bis-vdg-091-flugportal-s` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 23; bündelt 4 frühere Spezialskills (vdg-087-reiseveranstalter-vergleich-pruefen, vdg-088-reiseveranstalter-umsetzung-ueberwache, vdg-090-reiseveranstalter-risiko-rot... |
| `kompendium-24-vdg-092-flugportal-k-bis-vdg-095-flugportal-b` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 24; bündelt 4 frühere Spezialskills (vdg-092-flugportal-klageschrift-strukturieren, vdg-093-flugportal-anspruchsgruppen-bilden, vdg-094-flugportal-registertext-schrei... |
| `kompendium-25-vdg-096-flugportal-b-bis-vdg-101-bankentgelte` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 25; bündelt 4 frühere Spezialskills (vdg-096-flugportal-beweisplan-erstellen, vdg-097-flugportal-vergleich-pruefen, vdg-098-flugportal-umsetzung-ueberwachen, vdg-101-... |
| `kompendium-26-vdg-102-inkasso-konz-bis-vdg-105-schufa-scori` | verbraucherschutzverband-durchsetzung: Konsolidiertes Skill-Kompendium 26; bündelt 4 frühere Spezialskills (vdg-102-inkasso-konzerninkasso-musterfeststellung, vdg-103-bestellbutton-uklag-uwg-abmahnung, vdg-104-probeabo-widerruf-verbandss... |
| `vdg-001-kaltstart-verbandsfall-aufnehmen` | Verbraucherschutzverband Durchsetzung: Kaltstart Verbandsfall aufnehmen. Kaltstart Verbandsfall aufnehmen im Fachgebiet Verbraucherschutzverband Durchsetzung als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbei... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
