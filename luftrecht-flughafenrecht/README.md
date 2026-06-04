# Luftrecht und Flughafenrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`luftrecht-flughafenrecht`) | [`luftrecht-flughafenrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/luftrecht-flughafenrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Luftrechtsakte** (`luftrecht-airline-insolvenz-flugzeugpfand-flughafen`) | [Gesamt-PDF lesen](../testakten/luftrecht-airline-insolvenz-flugzeugpfand-flughafen/gesamt-pdf/luftrecht-airline-insolvenz-flugzeugpfand-flughafen_gesamt.pdf) | [`testakte-luftrecht-airline-insolvenz-flugzeugpfand-flughafen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-luftrecht-airline-insolvenz-flugzeugpfand-flughafen.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin deckt ziviles und öffentliches Luftrecht ab: Luftfahrzeug, Flughafen, Betriebsgenehmigung, LBA, Luftsicherheit, Slots, Flugzeugfinanzierung, Registerpfandrechte, Pfändung, Airline-Krise und internationale Bezüge.

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

Automatisch generierte Komplett-Liste aller 26 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Luftrecht und Flughafenrecht: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Spezialskill-Routing und erste Ausgabe. |
| `kompendium-01-luft-003-lba-zustaen-bis-luft-051-registerpfa` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 01; bündelt 5 frühere Spezialskills (luft-003-lba-zustaendigkeit-pruefen, luft-021-airline-zustaendigkeit-pruefen, luft-031-flughafen-zustaendigkeit-pruefen, luft-041-flugzeugleas... |
| `kompendium-02-luft-061-ersatzteill-bis-luft-101-slot-zustae` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 02; bündelt 5 frühere Spezialskills (luft-061-ersatzteillager-zustaendigkeit-pruefen, luft-071-drohne-zustaendigkeit-pruefen, luft-081-luftfracht-zustaendigkeit-pruefen, luft-091-... |
| `kompendium-03-luft-111-bodenabfert-bis-luft-006-pfaendung-f` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 03; bündelt 5 frühere Spezialskills (luft-111-bodenabfertigung-zustaendigkeit-pruefe, luft-002-luftvg-anwendungsbereich, luft-004-flugzeugrolle-und-register, luft-005-luftfahrzeug... |
| `kompendium-04-luft-007-aircraft-ar-bis-luft-011-slots-und-k` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 04; bündelt 5 frühere Spezialskills (luft-007-aircraft-arrest-international, luft-008-airline-finanzielle-leistungsfaehigkei, luft-009-betriebsgenehmigung-airline, luft-010-flugha... |
| `kompendium-05-luft-012-luftsicherh-bis-luft-016-passagierre` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 05; bündelt 5 frühere Spezialskills (luft-012-luftsicherheit-luftsig, luft-013-zuverlaessigkeitsueberpruefung, luft-014-drohnen-uas-betrieb, luft-015-gefahrgut-luftfracht, luft-01... |
| `kompendium-06-luft-017-fluglaerm-u-bis-luft-022-airline-reg` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 06; bündelt 5 frühere Spezialskills (luft-017-fluglaerm-und-anwohner, luft-018-insolvenz-fluggesellschaft, luft-019-leasing-und-cape-town-bezuege, luft-020-aviation-dashboard, luf... |
| `kompendium-07-luft-023-airline-pfa-bis-luft-027-airline-ins` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 07; bündelt 5 frühere Spezialskills (luft-023-airline-pfandrecht-vorbereiten, luft-024-airline-pfaendung-planen, luft-025-airline-genehmigung-pruefen, luft-026-airline-sicherheits... |
| `kompendium-08-luft-028-airline-loc-bis-luft-033-flughafen-p` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 08; bündelt 5 frühere Spezialskills (luft-028-airline-local-counsel-briefen, luft-029-airline-dashboard-bauen, luft-030-airline-mandantenmemo-schreiben, luft-032-flughafen-registe... |
| `kompendium-09-luft-034-flughafen-p-bis-luft-038-flughafen-l` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 09; bündelt 5 frühere Spezialskills (luft-034-flughafen-pfaendung-planen, luft-035-flughafen-genehmigung-pruefen, luft-036-flughafen-sicherheitsauflage-bewerten, luft-037-flughafe... |
| `kompendium-10-luft-039-flughafen-d-bis-luft-044-flugzeuglea` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 10; bündelt 5 frühere Spezialskills (luft-039-flughafen-dashboard-bauen, luft-040-flughafen-mandantenmemo-schreiben, luft-042-flugzeugleasing-register-auswerten, luft-043-flugzeug... |
| `kompendium-11-luft-045-flugzeuglea-bis-luft-049-flugzeuglea` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 11; bündelt 5 frühere Spezialskills (luft-045-flugzeugleasing-genehmigung-pruefen, luft-046-flugzeugleasing-sicherheitsauflage-bew, luft-047-flugzeugleasing-insolvenzrisiko-markie... |
| `kompendium-12-luft-050-flugzeuglea-bis-luft-055-registerpfa` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 12; bündelt 5 frühere Spezialskills (luft-050-flugzeugleasing-mandantenmemo-schreibe, luft-052-registerpfandrecht-register-auswerten, luft-053-registerpfandrecht-pfandrecht-vorber... |
| `kompendium-13-luft-056-registerpfa-bis-luft-060-registerpfa` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 13; bündelt 5 frühere Spezialskills (luft-056-registerpfandrecht-sicherheitsauflage, luft-057-registerpfandrecht-insolvenzrisiko-mar, luft-058-registerpfandrecht-local-counsel-bri... |
| `kompendium-14-luft-062-ersatzteill-bis-luft-066-ersatzteill` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 14; bündelt 5 frühere Spezialskills (luft-062-ersatzteillager-register-auswerten, luft-063-ersatzteillager-pfandrecht-vorbereiten, luft-064-ersatzteillager-pfaendung-planen, luft-... |
| `kompendium-15-luft-067-ersatzteill-bis-luft-072-drohne-regi` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 15; bündelt 5 frühere Spezialskills (luft-067-ersatzteillager-insolvenzrisiko-markie, luft-068-ersatzteillager-local-counsel-briefen, luft-069-ersatzteillager-dashboard-bauen, luf... |
| `kompendium-16-luft-073-drohne-pfan-bis-luft-077-drohne-inso` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 16; bündelt 5 frühere Spezialskills (luft-073-drohne-pfandrecht-vorbereiten, luft-074-drohne-pfaendung-planen, luft-075-drohne-genehmigung-pruefen, luft-076-drohne-sicherheitsaufl... |
| `kompendium-17-luft-078-drohne-loca-bis-luft-083-luftfracht` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 17; bündelt 5 frühere Spezialskills (luft-078-drohne-local-counsel-briefen, luft-079-drohne-dashboard-bauen, luft-080-drohne-mandantenmemo-schreiben, luft-082-luftfracht-register-... |
| `kompendium-18-luft-084-luftfracht-bis-luft-088-luftfracht` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 18; bündelt 5 frühere Spezialskills (luft-084-luftfracht-pfaendung-planen, luft-085-luftfracht-genehmigung-pruefen, luft-086-luftfracht-sicherheitsauflage-bewerten, luft-087-luftf... |
| `kompendium-19-luft-089-luftfracht-bis-luft-094-acc3-pfaend` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 19; bündelt 5 frühere Spezialskills (luft-089-luftfracht-dashboard-bauen, luft-090-luftfracht-mandantenmemo-schreiben, luft-092-acc3-register-auswerten, luft-093-acc3-pfandrecht-v... |
| `kompendium-20-luft-095-acc3-genehm-bis-luft-099-acc3-dashbo` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 20; bündelt 5 frühere Spezialskills (luft-095-acc3-genehmigung-pruefen, luft-096-acc3-sicherheitsauflage-bewerten, luft-097-acc3-insolvenzrisiko-markieren, luft-098-acc3-local-cou... |
| `kompendium-21-luft-100-acc3-mandan-bis-luft-105-slot-genehm` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 21; bündelt 5 frühere Spezialskills (luft-100-acc3-mandantenmemo-schreiben, luft-102-slot-register-auswerten, luft-103-slot-pfandrecht-vorbereiten, luft-104-slot-pfaendung-planen,... |
| `kompendium-22-luft-106-slot-sicher-bis-luft-110-slot-mandan` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 22; bündelt 5 frühere Spezialskills (luft-106-slot-sicherheitsauflage-bewerten, luft-107-slot-insolvenzrisiko-markieren, luft-108-slot-local-counsel-briefen, luft-109-slot-dashboa... |
| `kompendium-23-luft-112-bodenabfert-bis-luft-116-bodenabfert` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 23; bündelt 5 frühere Spezialskills (luft-112-bodenabfertigung-register-auswerten, luft-113-bodenabfertigung-pfandrecht-vorbereite, luft-114-bodenabfertigung-pfaendung-planen, luf... |
| `kompendium-24-luft-117-bodenabfert-bis-luft-119-bodenabfert` | luftrecht-flughafenrecht: Konsolidiertes Skill-Kompendium 24; bündelt 3 frühere Spezialskills (luft-117-bodenabfertigung-insolvenzrisiko-marki, luft-118-bodenabfertigung-local-counsel-briefen, luft-119-bodenabfertigung-dashboard-bauen) u... |
| `luft-001-kaltstart-luftrechtsmandat` | 'Mandant erscheint erstmals mit Luftrechtsfall: Airline-Insolvenz Flugzeugbeschlagnahme Slot-Verlust oder Planfeststellungsklage. Klaert Zustaendigkeit LBA vs. Landesbehoerde vs. Gericht sichert Fristen LuftVG §§ 20 ff. und EU-Recht und... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
