# Ordnungswidrigkeitenrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`ordnungswidrigkeitenrecht`) | [`ordnungswidrigkeitenrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/ordnungswidrigkeitenrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **OWiG-Akte** (`ordnungswidrigkeitenrecht-bussgeldmix-gewerbe-datenschutz-tier`) | [Gesamt-PDF lesen](../testakten/ordnungswidrigkeitenrecht-bussgeldmix-gewerbe-datenschutz-tier/gesamt-pdf/ordnungswidrigkeitenrecht-bussgeldmix-gewerbe-datenschutz-tier_gesamt.pdf) | [`testakte-ordnungswidrigkeitenrecht-bussgeldmix-gewerbe-datenschutz-tier.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ordnungswidrigkeitenrecht-bussgeldmix-gewerbe-datenschutz-tier.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin ist das allgemeine Betriebssystem für Bußgeldsachen, nicht nur Verkehr: OWiG-Verfahren, Fachordnungswidrigkeiten, Anhörung, Bußgeldbescheid, Einspruch, Akteneinsicht, Amtsgericht und Rechtsbeschwerde.

## Start

Beginne mit `ordnungswidrigkeitenrecht-allgemein`. Das Plugin fragt zuerst nach Rolle, Ziel, Frist, Behörde/Gericht/Register, vorhandenen Unterlagen und gewünschtem Output. Danach schlägt es die passenden Spezialskills aus diesem Plugin vor.

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
| `ordnungswidrigkeitenrecht-kaltstart-triage` | Ordnungswidrigkeitenrecht: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe. |
| `ordnungswidrigkeitenrecht-owi-akteneinsicht-beantragen` | Owi Akteneinsicht Beantragen / Owi Verjaehrung Unterbrechung / Owi Zustaendige Verwaltungsbehoerde / Owi Opportunitaet Einstellung: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastbaren... |
| `ordnungswidrigkeitenrecht-owi-aussenwirtschaft-gerichtstermin` | Owi Aussenwirtschaft Gerichtstermin Vorber / Owi Aussenwirtschaft Rechtsbeschwerde Prue: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |
| `ordnungswidrigkeitenrecht-owi-baurecht-frist-strassenverkehr` | Owi Baurecht Frist Pruefen / Owi Strassenverkehr Frist Pruefen / Owi Aussenwirtschaft Frist Pruefen / Owi Bussgeldbescheid Pruefen: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastbaren... |
| `ordnungswidrigkeitenrecht-owi-baurecht-mandantenbrief` | Owi Baurecht Mandantenbrief Schreiben / Owi Strassenverkehr Tatbestand Zerlegen / Owi Strassenverkehr Akteneinsicht Schreibe / Owi Strassenverkehr Einspruch Begruenden: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad... |
| `ordnungswidrigkeitenrecht-owi-datenschutzbussgeld-beweis` | Owi Datenschutzbussgeld Beweis Ruegen / Owi Datenschutzbussgeld Verjaehrung Berech / Owi Datenschutzbussgeld Gerichtstermin Vor / Owi Datenschutzbussgeld Rechtsbeschwerde P: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prü... |
| `ordnungswidrigkeitenrecht-owi-datenschutzbussgeld-tatbestand` | Owi Datenschutzbussgeld Tatbestand Zerlege / Owi Datenschutzbussgeld Akteneinsicht Schr / Owi Datenschutzbussgeld Einspruch Begruend / Owi Datenschutzbussgeld Einstellung Anrege: bearbeitet die maßgeblichen Prüffelder, setzt den passende... |
| `ordnungswidrigkeitenrecht-owi-einspruch-fristgerecht` | Owi Einspruch Fristgerecht Einlegen / Owi Beschlussverfahren OWiG / Owi Jugendliche Verfahren / Owi Datenschutzbussgeld Frist Pruefen: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastba... |
| `ordnungswidrigkeitenrecht-owi-lebensmittelrecht-einspruch` | Owi Lebensmittelrecht Einspruch Begruenden / Owi Lebensmittelrecht Einstellung Anregen / Owi Lebensmittelrecht Beweis Ruegen / Owi Lebensmittelrecht Verjaehrung Berechne: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpf... |
| `ordnungswidrigkeitenrecht-owi-lebensmittelrecht-gerichtstermin` | Owi Lebensmittelrecht Gerichtstermin Vorbe / Owi Lebensmittelrecht Rechtsbeschwerde Pru / Owi Lebensmittelrecht Mandantenbrief Schre / Owi Tierschutz Tatbestand Zerlegen: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpf... |
| `ordnungswidrigkeitenrecht-owi-umwelt-rechtsbeschwerde` | Owi Umwelt Rechtsbeschwerde Pruefen / Owi Umwelt Mandantenbrief Schreiben / Owi Lebensmittelrecht Tatbestand Zerlegen / Owi Lebensmittelrecht Akteneinsicht Schrei: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und... |
| `owi-001-kaltstart-bussgeldverfahren` | Ordnungswidrigkeitenrecht: Kaltstart Bußgeldverfahren. Kaltstart Bußgeldverfahren im Fachgebiet Ordnungswidrigkeitenrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |
| `owi-amtsgericht-hauptverhandlung` | Owi 015 Amtsgericht Hauptverhandlung, Owi 017 Rechtsbeschwerde Prüfen, Owi 018 Kostenentscheidung Angreifen, Owi 020 Owig In Einfacher Sprache: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und lie... |
| `owi-aussenwirtschaft-einspruch-einstellung` | Owi 094 Aussenwirtschaft Einspruch Begruenden, Owi 095 Aussenwirtschaft Einstellung Anregen, Owi 096 Aussenwirtschaft Beweis Ruegen, Owi 097 Aussenwirtschaft Verjaehrung Berechnen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkei... |
| `owi-baurecht-ruegen-verjaehrung-berechnen` | Owi 076 Baurecht Beweis Ruegen, Owi 077 Baurecht Verjaehrung Berechnen, Owi 078 Baurecht Gerichtstermin Vorbereiten, Owi 079 Baurecht Rechtsbeschwerde Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgr... |
| `owi-baurecht-zerlegen-akteneinsicht-schreiben` | Owi 071 Baurecht Tatbestand Zerlegen, Owi 073 Baurecht Akteneinsicht Schreiben, Owi 074 Baurecht Einspruch Begruenden, Owi 075 Baurecht Einstellung Anregen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrun... |
| `owi-datenschutzbussgeld-mandantenbrief-abgabe` | Owi 030 Datenschutzbussgeld Mandantenbrief Sch, Owi 014 Abgabe An Staatsanwaltschaft, Owi 002 Tatbestand Fachgesetz Finden, Owi 003 Anhoerung Richtig Behandeln: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechts... |
| `owi-gewerberecht-frist-umwelt` | Owi 032 Gewerberecht Frist Prüfen, Owi 042 Umwelt Owi Frist Prüfen, Owi 052 Lebensmittelrecht Frist Prüfen, Owi 062 Tierschutz Owi Frist Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und li... |
| `owi-gewerberecht-mandantenbrief-umwelt` | Owi 040 Gewerberecht Mandantenbrief Schreiben, Owi 041 Umwelt Owi Tatbestand Zerlegen, Owi 043 Umwelt Owi Akteneinsicht Schreiben, Owi 044 Umwelt Owi Einspruch Begruenden: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege... |
| `owi-gewerberecht-ruegen-verjaehrung-berechnen` | Owi 036 Gewerberecht Beweis Ruegen, Owi 037 Gewerberecht Verjaehrung Berechnen, Owi 038 Gewerberecht Gerichtstermin Vorbereite, Owi 039 Gewerberecht Rechtsbeschwerde Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Bele... |
| `owi-gewerberecht-zerlegen-akteneinsicht` | Owi 031 Gewerberecht Tatbestand Zerlegen, Owi 033 Gewerberecht Akteneinsicht Schreiben, Owi 034 Gewerberecht Einspruch Begruenden, Owi 035 Gewerberecht Einstellung Anregen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Beleg... |
| `owi-strassenverkehr-einstellung-ruegen` | Owi 085 Strassenverkehr Einstellung Anregen, Owi 086 Strassenverkehr Beweis Ruegen, Owi 087 Strassenverkehr Verjaehrung Berechnen, Owi 088 Strassenverkehr Gerichtstermin Vorbere: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit,... |
| `owi-strassenverkehr-rechtsbeschwerde` | Owi 089 Strassenverkehr Rechtsbeschwerde Pruef, Owi 090 Strassenverkehr Mandantenbrief Schreib, Owi 091 Aussenwirtschaft Tatbestand Zerlegen, Owi 093 Aussenwirtschaft Akteneinsicht Schreib: wählt den konkreten Prüfpfad, trennt Frist, Zus... |
| `owi-tierschutz-akteneinsicht-einspruch` | Owi 063 Tierschutz Owi Akteneinsicht Schreiben, Owi 064 Tierschutz Owi Einspruch Begruenden, Owi 065 Tierschutz Owi Einstellung Anregen, Owi 066 Tierschutz Owi Beweis Ruegen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Bel... |
| `owi-tierschutz-verjaehrung-gerichtstermin` | Owi 067 Tierschutz Owi Verjaehrung Berechnen, Owi 068 Tierschutz Owi Gerichtstermin Vorberei, Owi 069 Tierschutz Owi Rechtsbeschwerde Pruefe, Owi 070 Tierschutz Owi Mandantenbrief Schreibe: wählt den konkreten Prüfpfad, trennt Frist, Zus... |
| `owi-umwelt-einstellung-ruegen-verjaehrung` | Owi 045 Umwelt Owi Einstellung Anregen, Owi 046 Umwelt Owi Beweis Ruegen, Owi 047 Umwelt Owi Verjaehrung Berechnen, Owi 048 Umwelt Owi Gerichtstermin Vorbereiten: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rech... |
| `owi-unternehmen-verbandsgeldbusse` | Owi 010 Unternehmen Und Verbandsgeldbusse, Owi 011 Aufsichtspflichtverletzung 130 Owig, Owi 012 Einziehung Und Verfall Prüfen, Owi 013 Nebenfolgen Und Register: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechts... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
