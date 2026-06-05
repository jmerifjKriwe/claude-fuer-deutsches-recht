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

Beginne mit `strassenverkehrsrecht-stvo-allgemein`. Das Plugin fragt zuerst nach Rolle, Ziel, Frist, Behörde/Gericht/Register, vorhandenen Unterlagen und gewünschtem Output. Danach schlägt es die passenden Spezialskills aus diesem Plugin vor.

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
| `strassenverkehrsrecht-stvo-kaltstart-triage` | Straßenverkehrsrecht StVO: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe. |
| `strassenverkehrsrecht-stvo-stv-bussgeldschnittstelle-owig` | Stv Bussgeldschnittstelle OWiG / Stv Haltverbot Bussgeld Abgrenzen / Stv Tempo Bussgeld Abgrenzen / Stv Fahrradstrasse Bussgeld Abgrenzen: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten bela... |
| `strassenverkehrsrecht-stvo-stv-busspur-bussgeld-bewohnerparken` | Stv Busspur Bussgeld Abgrenzen / Stv Bewohnerparken Bussgeld Abgrenzen / Stv Lieferzone Bussgeld Abgrenzen / Stv Ladezone Bussgeld Abgrenzen: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten b... |
| `strassenverkehrsrecht-stvo-stv-parken-halten-ausnahmegenehmigung` | Stv Parken Halten Abschleppen / Stv Ausnahmegenehmigung Beantragen / Stv Radverkehr Schutzstreifen / Stv E Scooter Mikromobilitaet: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastbaren... |
| `strassenverkehrsrecht-stvo-stv-schulstrasse-behoerde-karte` | Stv Schulstrasse Behoerde Anschreiben / Stv Schulstrasse Karte Bauen: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |
| `strassenverkehrsrecht-stvo-stv-schwertransport-erlaubnis` | Stv Schwertransport Erlaubnis / Stv Fahrerlaubnis Schnittstelle / Stv Mpu Fahreignung / Stv Fahrtenbuchauflage: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |
| `strassenverkehrsrecht-stvo-stv-tempo-risiko-fahrradstrasse-regel` | Stv Tempo Risiko Erklaeren / Stv Fahrradstrasse Regel Pruefen / Stv Fahrradstrasse Zeichen Auslegen / Stv Fahrradstrasse Anordnung Angreifen: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten b... |
| `strassenverkehrsrecht-stvo-stv-widerspruch-gegen-eilrechtsschutz` | Stv Widerspruch Gegen Verkehrszeichen / Stv Eilrechtsschutz Verkehrszeichen / Stv Kommunikation Strassenverkehrsbeho / Stv Haltverbot Regel Pruefen: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den näc... |
| `stv-001-kaltstart-stvo-fall` | Straßenverkehrsrecht StVO: Kaltstart StVO-Fall. Kaltstart StVO-Fall im Fachgebiet Straßenverkehrsrecht StVO als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |
| `stv-bewohnerparken-eilrechtsschutz-behoerde` | Stv 067 Bewohnerparken Eilrechtsschutz Planen, Stv 068 Bewohnerparken Behörde Anschreiben, Stv 069 Bewohnerparken Karte Bauen, Stv 070 Bewohnerparken Risiko Erklaeren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und... |
| `stv-bewohnerparken-zeichen-anordnung` | Stv 062 Bewohnerparken Zeichen Auslegen, Stv 063 Bewohnerparken Anordnung Angreifen, Stv 064 Bewohnerparken Antrag Schreiben, Stv 065 Bewohnerparken Beweis Sichern: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Re... |
| `stv-busspur-anordnung-antrag-schreiben` | Stv 053 Busspur Anordnung Angreifen, Stv 054 Busspur Antrag Schreiben, Stv 055 Busspur Beweis Sichern, Stv 057 Busspur Eilrechtsschutz Planen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und lief... |
| `stv-busspur-behoerde-karte-bauen-risiko` | Stv 058 Busspur Behörde Anschreiben, Stv 059 Busspur Karte Bauen, Stv 060 Busspur Risiko Erklaeren, Stv 061 Bewohnerparken Regel Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert de... |
| `stv-fahrradstrasse-antrag-sichern` | Stv 044 Fahrradstrasse Antrag Schreiben, Stv 045 Fahrradstrasse Beweis Sichern, Stv 047 Fahrradstrasse Eilrechtsschutz Planen, Stv 048 Fahrradstrasse Behörde Anschreiben: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege... |
| `stv-fahrradstrasse-karte-risiko-erklaeren` | Stv 049 Fahrradstrasse Karte Bauen, Stv 050 Fahrradstrasse Risiko Erklaeren, Stv 051 Busspur Regel Prüfen, Stv 052 Busspur Zeichen Auslegen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefer... |
| `stv-gefahrenstelle-melden-schulweg` | Stv 013 Gefahrenstelle Melden, Stv 014 Schulweg Und Verkehrsberuhigung, Stv 015 Baustellenverkehrsrecht, Stv 016 Blaulicht Und Sonderrechte: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefer... |
| `stv-haltverbot-eilrechtsschutz-behoerde` | Stv 027 Haltverbot Eilrechtsschutz Planen, Stv 028 Haltverbot Behörde Anschreiben, Stv 029 Haltverbot Karte Bauen, Stv 030 Haltverbot Risiko Erklaeren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage... |
| `stv-haltverbot-zeichen-anordnung-angreifen` | Stv 022 Haltverbot Zeichen Auslegen, Stv 023 Haltverbot Anordnung Angreifen, Stv 024 Haltverbot Antrag Schreiben, Stv 025 Haltverbot Beweis Sichern: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage un... |
| `stv-ladezone-antrag-sichern-eilrechtsschutz` | Stv 084 Ladezone Antrag Schreiben, Stv 085 Ladezone Beweis Sichern, Stv 087 Ladezone Eilrechtsschutz Planen, Stv 088 Ladezone Behörde Anschreiben: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und... |
| `stv-ladezone-karte-risiko-erklaeren` | Stv 089 Ladezone Karte Bauen, Stv 090 Ladezone Risiko Erklaeren, Stv 091 Schulstrasse Regel Prüfen, Stv 092 Schulstrasse Zeichen Auslegen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert... |
| `stv-lieferzone-regel-zeichen-auslegen` | Stv 071 Lieferzone Regel Prüfen, Stv 072 Lieferzone Zeichen Auslegen, Stv 073 Lieferzone Anordnung Angreifen, Stv 074 Lieferzone Antrag Schreiben: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und... |
| `stv-lieferzone-risiko-ladezone-regel-zeichen` | Stv 080 Lieferzone Risiko Erklaeren, Stv 081 Ladezone Regel Prüfen, Stv 082 Ladezone Zeichen Auslegen, Stv 083 Ladezone Anordnung Angreifen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefer... |
| `stv-lieferzone-sichern-eilrechtsschutz-planen` | Stv 075 Lieferzone Beweis Sichern, Stv 077 Lieferzone Eilrechtsschutz Planen, Stv 078 Lieferzone Behörde Anschreiben, Stv 079 Lieferzone Karte Bauen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage u... |
| `stv-schulstrasse-anordnung-antrag-schreiben` | Stv 093 Schulstrasse Anordnung Angreifen, Stv 094 Schulstrasse Antrag Schreiben, Stv 095 Schulstrasse Beweis Sichern, Stv 097 Schulstrasse Eilrechtsschutz Planen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rech... |
| `stv-schulstrasse-bussgeld-verkehrszeichen` | Stv 096 Schulstrasse Bussgeld Abgrenzen, Stv 002 Verkehrszeichen Lesen, Stv 003 Verkehrsrechtliche Anordnung Prüfen, Stv 004 Tempozone Und Beschilderung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundla... |
| `stv-tempo-regel-zeichen-auslegen-anordnung` | Stv 031 Tempo 30 Regel Prüfen, Stv 032 Tempo 30 Zeichen Auslegen, Stv 033 Tempo 30 Anordnung Angreifen, Stv 034 Tempo 30 Antrag Schreiben: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert... |
| `stv-tempo-sichern-eilrechtsschutz-planen` | Stv 035 Tempo 30 Beweis Sichern, Stv 037 Tempo 30 Eilrechtsschutz Planen, Stv 038 Tempo 30 Behörde Anschreiben, Stv 039 Tempo 30 Karte Bauen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefe... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
