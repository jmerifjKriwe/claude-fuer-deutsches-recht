# Verbraucherschutzrecht Prüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`verbraucherschutzrecht-pruefer`) | [`verbraucherschutzrecht-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verbraucherschutzrecht-pruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Verbraucherakte SmartMeter-Abo** (`verbraucherschutzrecht-smartmeter-abo-plattform`) | [Gesamt-PDF lesen](../testakten/verbraucherschutzrecht-smartmeter-abo-plattform/gesamt-pdf/verbraucherschutzrecht-smartmeter-abo-plattform_gesamt.pdf) | [`testakte-verbraucherschutzrecht-smartmeter-abo-plattform.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verbraucherschutzrecht-smartmeter-abo-plattform.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **Verbraucherakte SmartMeter-Abo** ([`testakten/verbraucherschutzrecht-smartmeter-abo-plattform/`](../testakten/verbraucherschutzrecht-smartmeter-abo-plattform/)).

Direkt-Download als ZIP: [testakte-verbraucherschutzrecht-smartmeter-abo-plattform.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verbraucherschutzrecht-smartmeter-abo-plattform.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

Dieses Plugin prüft verbraucherschützende Vorschriften nicht als lose Sammlung, sondern als Schutzarchitektur: Informationspflicht, Widerruf, AGB-Kontrolle, Gewährleistung, Lauterkeit, Streitbeilegung, Plattform und Durchsetzung.

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

Automatisch generierte Komplett-Liste aller 30 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Verbraucherschutzrecht Prüfer: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Spezialskill-Routing und erste Ausgabe. |
| `kompendium-01-vbr-023-haustuergesc-bis-vbr-053-marketplace` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 01; bündelt 4 frühere Spezialskills (vbr-023-haustuergeschaeft-frist-berechnen, vbr-033-fernabsatz-frist-berechnen, vbr-043-online-shop-frist-berechnen, vbr-053-marketplace-... |
| `kompendium-02-vbr-063-abo-falle-fr-bis-vbr-093-smart-device` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 02; bündelt 4 frühere Spezialskills (vbr-063-abo-falle-frist-berechnen, vbr-073-digitale-inhalte-frist-berechnen, vbr-083-saas-fuer-verbraucher-frist-berechnen, vbr-093-smar... |
| `kompendium-03-vbr-006-agb-klausel-bis-vbr-002-verbraucher` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 03; bündelt 4 frühere Spezialskills (vbr-006-agb-klausel-im-verbrauchervertrag-prue, vbr-016-energievertrag-und-abschlag, vbr-019-gesundheit-und-pflegevertrag, vbr-002-verbr... |
| `kompendium-04-vbr-003-unternehmerr-bis-vbr-007-digitale-pro` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 04; bündelt 4 frühere Spezialskills (vbr-003-unternehmerrolle-und-plattformrolle-pr, vbr-004-informationspflichten-matrix-bauen, vbr-005-widerrufsrecht-und-erloeschen-pruefe... |
| `kompendium-05-vbr-008-waren-mit-di-bis-vbr-011-schlichtung` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 05; bündelt 4 frühere Spezialskills (vbr-008-waren-mit-digitalen-elementen, vbr-009-preisangaben-und-dark-patterns, vbr-010-uwg-irrefuehrung-verbraucherbezug, vbr-011-schlic... |
| `kompendium-06-vbr-012-inkasso-und-bis-vbr-015-reise-und-fl` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 06; bündelt 4 frühere Spezialskills (vbr-012-inkasso-und-mahnung-einordnen, vbr-013-gewaehrleistung-und-garantie-trennen, vbr-014-kaufrecht-reparatur-und-right-to-repai, vbr... |
| `kompendium-07-vbr-017-telekommunik-bis-vbr-021-haustuergesc` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 07; bündelt 4 frühere Spezialskills (vbr-017-telekommunikation-und-laufzeit, vbr-018-finanzdienstleistung-fernabsatz, vbr-020-verbraucherbericht-erzeugen, vbr-021-haustuerge... |
| `kompendium-08-vbr-022-haustuergesc-bis-vbr-026-haustuergesc` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 08; bündelt 4 frühere Spezialskills (vbr-022-haustuergeschaeft-widerruf-formulieren, vbr-024-haustuergeschaeft-beweise-sichern, vbr-025-haustuergeschaeft-agb-redlinen, vbr-0... |
| `kompendium-09-vbr-027-haustuergesc-bis-vbr-030-haustuergesc` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 09; bündelt 4 frühere Spezialskills (vbr-027-haustuergeschaeft-schlichtung-waehlen, vbr-028-haustuergeschaeft-klagepfad-skizzieren, vbr-029-haustuergeschaeft-vergleich-vorsc... |
| `kompendium-10-vbr-031-fernabsatz-a-bis-vbr-035-fernabsatz-a` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 10; bündelt 4 frühere Spezialskills (vbr-031-fernabsatz-anspruch-pruefen, vbr-032-fernabsatz-widerruf-formulieren, vbr-034-fernabsatz-beweise-sichern, vbr-035-fernabsatz-agb... |
| `kompendium-11-vbr-036-fernabsatz-b-bis-vbr-039-fernabsatz-v` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 11; bündelt 4 frühere Spezialskills (vbr-036-fernabsatz-beschwerde-schreiben, vbr-037-fernabsatz-schlichtung-waehlen, vbr-038-fernabsatz-klagepfad-skizzieren, vbr-039-fernab... |
| `kompendium-12-vbr-040-fernabsatz-b-bis-vbr-044-online-shop` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 12; bündelt 4 frühere Spezialskills (vbr-040-fernabsatz-behoerdenmeldung-pruefen, vbr-041-online-shop-anspruch-pruefen, vbr-042-online-shop-widerruf-formulieren, vbr-044-onl... |
| `kompendium-13-vbr-045-online-shop-bis-vbr-048-online-shop` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 13; bündelt 4 frühere Spezialskills (vbr-045-online-shop-agb-redlinen, vbr-046-online-shop-beschwerde-schreiben, vbr-047-online-shop-schlichtung-waehlen, vbr-048-online-shop... |
| `kompendium-14-vbr-049-online-shop-bis-vbr-052-marketplace` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 14; bündelt 4 frühere Spezialskills (vbr-049-online-shop-vergleich-vorschlagen, vbr-050-online-shop-behoerdenmeldung-pruefen, vbr-051-marketplace-anspruch-pruefen, vbr-052-m... |
| `kompendium-15-vbr-054-marketplace-bis-vbr-057-marketplace` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 15; bündelt 4 frühere Spezialskills (vbr-054-marketplace-beweise-sichern, vbr-055-marketplace-agb-redlinen, vbr-056-marketplace-beschwerde-schreiben, vbr-057-marketplace-sch... |
| `kompendium-16-vbr-058-marketplace-bis-vbr-061-abo-falle-an` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 16; bündelt 4 frühere Spezialskills (vbr-058-marketplace-klagepfad-skizzieren, vbr-059-marketplace-vergleich-vorschlagen, vbr-060-marketplace-behoerdenmeldung-pruefen, vbr-0... |
| `kompendium-17-vbr-062-abo-falle-wi-bis-vbr-066-abo-falle-be` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 17; bündelt 4 frühere Spezialskills (vbr-062-abo-falle-widerruf-formulieren, vbr-064-abo-falle-beweise-sichern, vbr-065-abo-falle-agb-redlinen, vbr-066-abo-falle-beschwerde-... |
| `kompendium-18-vbr-067-abo-falle-sc-bis-vbr-070-abo-falle-be` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 18; bündelt 4 frühere Spezialskills (vbr-067-abo-falle-schlichtung-waehlen, vbr-068-abo-falle-klagepfad-skizzieren, vbr-069-abo-falle-vergleich-vorschlagen, vbr-070-abo-fall... |
| `kompendium-19-vbr-071-digitale-inh-bis-vbr-075-digitale-inh` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 19; bündelt 4 frühere Spezialskills (vbr-071-digitale-inhalte-anspruch-pruefen, vbr-072-digitale-inhalte-widerruf-formulieren, vbr-074-digitale-inhalte-beweise-sichern, vbr-... |
| `kompendium-20-vbr-076-digitale-inh-bis-vbr-079-digitale-inh` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 20; bündelt 4 frühere Spezialskills (vbr-076-digitale-inhalte-beschwerde-schreiben, vbr-077-digitale-inhalte-schlichtung-waehlen, vbr-078-digitale-inhalte-klagepfad-skizzier... |
| `kompendium-21-vbr-080-digitale-inh-bis-vbr-084-saas-fuer-ve` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 21; bündelt 4 frühere Spezialskills (vbr-080-digitale-inhalte-behoerdenmeldung-prue, vbr-081-saas-fuer-verbraucher-anspruch-pruefen, vbr-082-saas-fuer-verbraucher-widerruf-f... |
| `kompendium-22-vbr-085-saas-fuer-ve-bis-vbr-088-saas-fuer-ve` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 22; bündelt 4 frühere Spezialskills (vbr-085-saas-fuer-verbraucher-agb-redlinen, vbr-086-saas-fuer-verbraucher-beschwerde-schre, vbr-087-saas-fuer-verbraucher-schlichtung-wa... |
| `kompendium-23-vbr-089-saas-fuer-ve-bis-vbr-092-smart-device` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 23; bündelt 4 frühere Spezialskills (vbr-089-saas-fuer-verbraucher-vergleich-vorsch, vbr-090-saas-fuer-verbraucher-behoerdenmeldung, vbr-091-smart-device-anspruch-pruefen, v... |
| `kompendium-24-vbr-094-smart-device-bis-vbr-097-smart-device` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 24; bündelt 4 frühere Spezialskills (vbr-094-smart-device-beweise-sichern, vbr-095-smart-device-agb-redlinen, vbr-096-smart-device-beschwerde-schreiben, vbr-097-smart-device... |
| `kompendium-25-vbr-098-smart-device-bis-verbraucherrecht-beh` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 25; bündelt 4 frühere Spezialskills (vbr-098-smart-device-klagepfad-skizzieren, vbr-099-smart-device-vergleich-vorschlagen, verbraucherrecht-abo-kuendigung-button, verbrauch... |
| `kompendium-26-verbraucherrecht-dig-bis-verbraucherrecht-pla` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 26; bündelt 4 frühere Spezialskills (verbraucherrecht-digitale-produkte-327-bgb, verbraucherrecht-energie-smartmeter-waerme, verbraucherrecht-finanzdienstleistung-online, ve... |
| `kompendium-27-verbraucherrecht-pre-bis-verbraucherrecht-ver` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 27; bündelt 4 frühere Spezialskills (verbraucherrecht-preisangaben-und-dark-patterns, verbraucherrecht-reise-flug-pauschal, verbraucherrecht-right-to-repair, verbraucherrech... |
| `kompendium-28-verbraucherrecht-war-bis-verbraucherrecht-wid` | verbraucherschutzrecht-pruefer: Konsolidiertes Skill-Kompendium 28; bündelt 2 frühere Spezialskills (verbraucherrecht-waren-mit-digitalen-elementen, verbraucherrecht-widerruf-fernabsatz) und bewahrt deren Workflows, Normanker, Prüfprogra... |
| `vbr-001-kaltstart-verbraucherfall-sortieren` | Verbraucherschutzrecht Prüfer: Kaltstart Verbraucherfall sortieren. Kaltstart Verbraucherfall sortieren im Fachgebiet Verbraucherschutzrecht Prüfer als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
