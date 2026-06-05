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

Beginne mit `verbraucherschutzverband-durchsetzung-allgemein`. Das Plugin fragt zuerst nach Rolle, Ziel, Frist, Behörde/Gericht/Register, vorhandenen Unterlagen und gewünschtem Output. Danach schlägt es die passenden Spezialskills aus diesem Plugin vor.

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
| `vdg-001-kaltstart-verbandsfall-aufnehmen` | Verbraucherschutzverband Durchsetzung: Kaltstart Verbandsfall aufnehmen. Kaltstart Verbandsfall aufnehmen im Fachgebiet Verbraucherschutzverband Durchsetzung als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbei... |
| `vdg-abo-modell-fitnessstudio-sammelfaehigkeit` | Vdg 070 Abo Modell Risiko Rot Markieren, Vdg 071 Fitnessstudio Sammelfaehigkeit Prüfen, Vdg 072 Fitnessstudio Klageschrift Strukturier, Vdg 073 Fitnessstudio Anspruchsgruppen Bilden: wählt den konkreten Prüfpfad, trennt Frist, Zuständigk... |
| `vdg-bankentgelte-kommunikation` | Vdg 029 Bankentgelte Kommunikation Steuern, Vdg 049 Energiepreiserhoehung Kommunikation St, Vdg 059 Plattform Sperre Kommunikation Steuern, Vdg 069 Abo Modell Kommunikation Steuern: wählt den konkreten Prüfpfad, trennt Frist, Zuständigke... |
| `vdg-bankentgelte-registertext` | Vdg 024 Bankentgelte Registertext Schreiben, Vdg 025 Bankentgelte Betroffenenformular Bauen, Vdg 026 Bankentgelte Beweisplan Erstellen, Vdg 027 Bankentgelte Vergleich Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Bel... |
| `vdg-bankentgelte-umsetzung-risiko-rot` | Vdg 028 Bankentgelte Umsetzung Ueberwachen, Vdg 030 Bankentgelte Risiko Rot Markieren, Vdg 041 Energiepreiserhoehung Sammelfaehigkeit, Vdg 042 Energiepreiserhoehung Klageschrift Str: wählt den konkreten Prüfpfad, trennt Frist, Zuständigk... |
| `vdg-erfolgsmonitoring-bankentgelte` | Vdg 020 Erfolgsmonitoring, Vdg 021 Bankentgelte Sammelfaehigkeit Prüfen, Vdg 022 Bankentgelte Klageschrift Strukturiere, Vdg 023 Bankentgelte Anspruchsgruppen Bilden: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und... |
| `vdg-finanzierung-interessenkonflikte` | Vdg 007 Finanzierung Und Interessenkonflikte, Vdg 008 Verbandsklageregister Vorbereiten, Vdg 009 Klageziele Praezise Schneiden, Vdg 010 Lebenssachverhalt Buendeln: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rec... |
| `vdg-fitnessstudio-registertext` | Vdg 074 Fitnessstudio Registertext Schreiben, Vdg 075 Fitnessstudio Betroffenenformular Baue, Vdg 076 Fitnessstudio Beweisplan Erstellen, Vdg 077 Fitnessstudio Vergleich Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit,... |
| `vdg-fitnessstudio-umsetzung-risiko-rot` | Vdg 078 Fitnessstudio Umsetzung Ueberwachen, Vdg 080 Fitnessstudio Risiko Rot Markieren, Vdg 081 Reiseveranstalter Sammelfaehigkeit Pru, Vdg 082 Reiseveranstalter Klageschrift Struktu: wählt den konkreten Prüfpfad, trennt Frist, Zuständi... |
| `vdg-flugportal-beweisplan-umsetzung` | Vdg 096 Flugportal Beweisplan Erstellen, Vdg 097 Flugportal Vergleich Prüfen, Vdg 098 Flugportal Umsetzung Ueberwachen, Vdg 101 Bankentgelte Zustimmungsfiktion Serie: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und... |
| `vdg-flugportal-klageschrift-anspruchsgruppen` | Vdg 092 Flugportal Klageschrift Strukturieren, Vdg 093 Flugportal Anspruchsgruppen Bilden, Vdg 094 Flugportal Registertext Schreiben, Vdg 095 Flugportal Betroffenenformular Bauen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit... |
| `vdg-plattform-sperre-anspruchsgruppen-bild` | Vdg 052 Plattform Sperre Klageschrift Struktur, Vdg 053 Plattform Sperre Anspruchsgruppen Bild, Vdg 054 Plattform Sperre Registertext Schreibe, Vdg 055 Plattform Sperre Betroffenenformular B: wählt den konkreten Prüfpfad, trennt Frist, Z... |
| `vdg-plattform-sperre-umsetzung-ueberwachen` | Vdg 056 Plattform Sperre Beweisplan Erstellen, Vdg 057 Plattform Sperre Vergleich Prüfen, Vdg 058 Plattform Sperre Umsetzung Ueberwachen, Vdg 060 Plattform Sperre Risiko Rot Markieren: wählt den konkreten Prüfpfad, trennt Frist, Zuständi... |
| `vdg-telekommunikationsklausel-registertext` | Vdg 034 Telekommunikationsklausel Registertext, Vdg 035 Telekommunikationsklausel Betroffenenf, Vdg 036 Telekommunikationsklausel Beweisplan E, Vdg 037 Telekommunikationsklausel Vergleich Pr: wählt den konkreten Prüfpfad, trennt Frist, Z... |
| `vdg-telekommunikationsklausel-umsetzung` | Vdg 038 Telekommunikationsklausel Umsetzung Ue, Vdg 039 Telekommunikationsklausel Kommunikatio, Vdg 040 Telekommunikationsklausel Risiko Rot M, Vdg 106 Diesel Differenzschaden Serienfall: wählt den konkreten Prüfpfad, trennt Frist, Zustä... |
| `vdg-umsetzungsverfahren` | Vdg 014 Umsetzungsverfahren Planen, Vdg 031 Telekommunikationsklausel Sammelfaehig, Vdg 032 Telekommunikationsklausel Klageschrift, Vdg 033 Telekommunikationsklausel Anspruchsgru: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit... |
| `verbraucherschutzverband-durchsetzung-kaltstart-triage` | Verbraucherschutzverband Durchsetzung: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe. |
| `verbraucherverband-abhilfeklage-musterfeststellung-w-uklag` | Abhilfeklage Musterfeststellung W / Uklag Unterlassung Gegen Agb / Uwg Verbraucherinteressen Pruefen / Quorum Betroffenengruppe: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten... |
| `verbraucherverband-abo-modell-betroffenenformular-beweisplan` | Abo Modell Betroffenenformular Bauen / Abo Modell Beweisplan Erstellen / Abo Modell Vergleich Pruefen / Abo Modell Umsetzung Ueberwachen: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den... |
| `verbraucherverband-abo-modell-sammelfaehigkeit-klageschrift` | Abo Modell Sammelfaehigkeit Pruefen / Abo Modell Klageschrift Strukturieren / Abo Modell Anspruchsgruppen Bilden / Abo Modell Registertext Schreiben: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und... |
| `verbraucherverband-beweismittel-offenlegung-nutzen-kommunikation` | Beweismittel Offenlegung Nutzen / Kommunikation Verbraucher / Vergleich Austritt Pruefen / Sachwalterfragen Vorbereiten: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten belastba... |
| `verbraucherverband-energiepreiserhoehung-anspruchsgruppen` | Energiepreiserhoehung Anspruchsgruppen / Energiepreiserhoehung Registertext Sch / Energiepreiserhoehung Betroffenenformu / Energiepreiserhoehung Beweisplan Erste: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden... |
| `verbraucherverband-energiepreiserhoehung-vergleich-pruefe` | Energiepreiserhoehung Vergleich Pruefe / Energiepreiserhoehung Umsetzung Ueberw / Energiepreiserhoehung Risiko Rot Marki / Plattform Sperre Sammelfaehigkeit Prue: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden... |
| `verbraucherverband-fitnessstudio-kommunikation-steuern` | Fitnessstudio Kommunikation Steuern / Reiseveranstalter Kommunikation Steuer / Flugportal Kommunikation Steuern / Klageberechtigung Stelle Pruefen: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und er... |
| `verbraucherverband-individualklagen-koordinieren-presse` | Individualklagen Koordinieren / Presse Kampagnenrisiko / Datenschutz Betroffenenpool / Kosten Prozessrisiko: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |
| `verbraucherverband-inkasso-konzerninkasso-musterfeststellung` | Inkasso Konzerninkasso Musterfeststellung / Bestellbutton Uklag Uwg Abmahnung / Probeabo Widerruf Verbandsstrategie / Schufa Scoring DSGVO Verbandsfall: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad u... |
| `verbraucherverband-reiseveranstalter-anspruchsgruppen-bil` | Reiseveranstalter Anspruchsgruppen Bil / Reiseveranstalter Registertext Schreib / Reiseveranstalter Betroffenenformular / Reiseveranstalter Beweisplan Erstellen: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden P... |
| `verbraucherverband-reiseveranstalter-vergleich-pruefen-umsetzung` | Reiseveranstalter Vergleich Pruefen / Reiseveranstalter Umsetzung Ueberwache / Reiseveranstalter Risiko Rot Markieren / Flugportal Sammelfaehigkeit Pruefen: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpf... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
