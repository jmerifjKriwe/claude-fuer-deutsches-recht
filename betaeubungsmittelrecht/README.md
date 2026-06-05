# Betäubungsmittelrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`betaeubungsmittelrecht`) | [`betaeubungsmittelrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/betaeubungsmittelrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **BtM-Akte** (`betaeubungsmittelrecht-apotheke-substitution-festival`) | [Gesamt-PDF lesen](../testakten/betaeubungsmittelrecht-apotheke-substitution-festival/gesamt-pdf/betaeubungsmittelrecht-apotheke-substitution-festival_gesamt.pdf) | [`testakte-betaeubungsmittelrecht-apotheke-substitution-festival.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-betaeubungsmittelrecht-apotheke-substitution-festival.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin behandelt BtM nicht nur strafrechtlich: Verkehrsfähigkeit, Verschreibung, Apotheke, ärztliche Praxis, Erlaubnis, Strafverteidigung, Therapie, Cannabis-Schnittstelle und Compliance werden getrennt geführt.

## Start

Beginne mit `betaeubungsmittelrecht-allgemein`. Das Plugin fragt zuerst nach Rolle, Ziel, Frist, Behörde/Gericht/Register, vorhandenen Unterlagen und gewünschtem Output. Danach schlägt es die passenden Spezialskills aus diesem Plugin vor.

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
| `betaeubungsmittelrecht-kaltstart-triage` | Betäubungsmittelrecht: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe. |
| `btm-001-kaltstart-fall` | Betäubungsmittelrecht: Kaltstart BtM-Fall. Kaltstart BtM-Fall im Fachgebiet Betäubungsmittelrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |
| `btm-amphetamin-bauen-akteneinsicht` | Btm 058 Amphetamin Compliance Bauen, Btm 059 Amphetamin Akteneinsicht Vorbereiten, Btm 060 Amphetamin Mandantenbrief Schreiben, Btm 061 Mdma Stoff Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundl... |
| `btm-amphetamin-sichern-einlassung-planen` | Btm 054 Amphetamin Beweis Sichern, Btm 055 Amphetamin Einlassung Planen, Btm 056 Amphetamin Therapiepfad Prüfen, Btm 057 Amphetamin Erlaubnis Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage u... |
| `btm-aufklaerungshilfe-btmg-kcang-medcang-abgrenzen-neue` | Aufklaerungshilfe Btmg / Kcang Medcang Abgrenzen / Neue Psychoaktive Stoffe / Durchsuchung Beschlagnahme: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |
| `btm-cannabis-mandantenbrief-kokain-stoff` | Btm 030 Cannabis Mandantenbrief Schreiben, Btm 031 Kokain Stoff Prüfen, Btm 032 Kokain Menge Einordnen, Btm 033 Kokain Strafrahmen Routen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert... |
| `btm-cannabis-menge-strafrahmen-routen-sichern` | Btm 022 Cannabis Menge Einordnen, Btm 023 Cannabis Strafrahmen Routen, Btm 024 Cannabis Beweis Sichern, Btm 025 Cannabis Einlassung Planen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert... |
| `btm-cannabis-therapiepfad-erlaubnis-bauen` | Btm 026 Cannabis Therapiepfad Prüfen, Btm 027 Cannabis Erlaubnis Prüfen, Btm 028 Cannabis Compliance Bauen, Btm 029 Cannabis Akteneinsicht Vorbereiten: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage... |
| `btm-fentanyl-bauen-akteneinsicht-vorbereiten` | Btm 078 Fentanyl Compliance Bauen, Btm 079 Fentanyl Akteneinsicht Vorbereiten, Btm 080 Fentanyl Mandantenbrief Schreiben, Btm 081 Methadon Stoff Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlag... |
| `btm-fentanyl-sichern-einlassung-planen` | Btm 074 Fentanyl Beweis Sichern, Btm 075 Fentanyl Einlassung Planen, Btm 076 Fentanyl Therapiepfad Prüfen, Btm 077 Fentanyl Erlaubnis Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefe... |
| `btm-heroin-mandantenbrief-amphetamin-stoff` | Btm 050 Heroin Mandantenbrief Schreiben, Btm 051 Amphetamin Stoff Prüfen, Btm 052 Amphetamin Menge Einordnen, Btm 053 Amphetamin Strafrahmen Routen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage un... |
| `btm-heroin-menge-strafrahmen-routen-sichern` | Btm 042 Heroin Menge Einordnen, Btm 043 Heroin Strafrahmen Routen, Btm 044 Heroin Beweis Sichern, Btm 045 Heroin Einlassung Planen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den näc... |
| `btm-heroin-therapiepfad-erlaubnis-bauen` | Btm 046 Heroin Therapiepfad Prüfen, Btm 047 Heroin Erlaubnis Prüfen, Btm 048 Heroin Compliance Bauen, Btm 049 Heroin Akteneinsicht Vorbereiten: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und lie... |
| `btm-internationaler-versand-betriebspruefung-apotheke-einfacher` | Internationaler Versand / Betriebspruefung Apotheke / Einfacher Sprache / Cannabis Stoff Pruefen: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |
| `btm-kokain-bauen-akteneinsicht-vorbereiten` | Btm 038 Kokain Compliance Bauen, Btm 039 Kokain Akteneinsicht Vorbereiten, Btm 040 Kokain Mandantenbrief Schreiben, Btm 041 Heroin Stoff Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und li... |
| `btm-kokain-sichern-einlassung-planen` | Btm 034 Kokain Beweis Sichern, Btm 035 Kokain Einlassung Planen, Btm 036 Kokain Therapiepfad Prüfen, Btm 037 Kokain Erlaubnis Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den n... |
| `btm-mdma-mandantenbrief-fentanyl-stoff-menge` | Btm 070 Mdma Mandantenbrief Schreiben, Btm 071 Fentanyl Stoff Prüfen, Btm 072 Fentanyl Menge Einordnen, Btm 073 Fentanyl Strafrahmen Routen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefer... |
| `btm-mdma-menge-strafrahmen-routen-sichern` | Btm 062 Mdma Menge Einordnen, Btm 063 Mdma Strafrahmen Routen, Btm 064 Mdma Beweis Sichern, Btm 065 Mdma Einlassung Planen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten be... |
| `btm-mdma-therapiepfad-erlaubnis-bauen` | Btm 066 Mdma Therapiepfad Prüfen, Btm 067 Mdma Erlaubnis Prüfen, Btm 068 Mdma Compliance Bauen, Btm 069 Mdma Akteneinsicht Vorbereiten: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den... |
| `btm-medizinalcannabis-beweis-sichern-einlassung-planen` | Medizinalcannabis Beweis Sichern / Medizinalcannabis Einlassung Planen / Medizinalcannabis Therapiepfad Pruefen / Medizinalcannabis Erlaubnis Pruefen: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den n... |
| `btm-medizinalcannabis-compliance-bauen-akteneinsicht-vorber` | Medizinalcannabis Compliance Bauen / Medizinalcannabis Akteneinsicht Vorber: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |
| `btm-methadon-mandantenbrief-medizinalcannabis` | Btm 090 Methadon Mandantenbrief Schreiben, Btm 091 Medizinalcannabis Stoff Prüfen, Btm 092 Medizinalcannabis Menge Einordnen, Btm 093 Medizinalcannabis Strafrahmen Routen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege... |
| `btm-methadon-menge-strafrahmen-routen-sichern` | Btm 082 Methadon Menge Einordnen, Btm 083 Methadon Strafrahmen Routen, Btm 084 Methadon Beweis Sichern, Btm 085 Methadon Einlassung Planen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert... |
| `btm-methadon-therapiepfad-erlaubnis-bauen` | Btm 086 Methadon Therapiepfad Prüfen, Btm 087 Methadon Erlaubnis Prüfen, Btm 088 Methadon Compliance Bauen, Btm 089 Methadon Akteneinsicht Vorbereiten: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage... |
| `btm-rezept-btmvv-arztpraxis-compliance-apotheke-dokumentation` | Rezept Btmvv / Arztpraxis Compliance / Apotheke Dokumentation / Therapie Statt Strafe: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |
| `btm-stoff-anlage-pruefen-nicht-geringe-menge-handeltreiben` | Stoff Anlage Pruefen / Nicht Geringe Menge Livecheck / Handeltreiben Besitz / Einfuhr Ausfuhr Durchfuhr: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |
| `btm-u-haft-sache-einziehung-wertersatz-jugendliche-fahrerlaubnis` | U Haft Sache / Einziehung Wertersatz / Jugendliche / Fahrerlaubnis: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
