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
| `vdg-001-kaltstart-verbandsfall-aufnehmen` | Verbraucherschutzverband Durchsetzung: Kaltstart Verbandsfall aufnehmen. Kaltstart Verbandsfall aufnehmen im Fachgebiet Verbraucherschutzverband Durchsetzung als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbei... |
| `vdg-abhilfeklage-vdg-uklag-vdg-uwg-vdg-quorum` | Nutze dies, wenn Vdg 003 Abhilfeklage Oder Musterfeststellung W, Vdg 004 Uklag Unterlassung Gegen Agb, Vdg 005 Uwg Verbraucherinteressen Prüfen, Vdg 006 Quorum Und Betroffenengruppe im Plugin Verbraucherschutzverband Durchsetzung konkret... |
| `vdg-abo-modell-fitnessstudio-sammelfaehigkeit` | Nutze dies, wenn Vdg 070 Abo Modell Risiko Rot Markieren, Vdg 071 Fitnessstudio Sammelfaehigkeit Prüfen, Vdg 072 Fitnessstudio Klageschrift Strukturier, Vdg 073 Fitnessstudio Anspruchsgruppen Bilden im Plugin Verbraucherschutzverband Dur... |
| `vdg-abo-vdg-abo-vdg-abo-vdg-abo` | Nutze dies, wenn Vdg 061 Abo Modell Sammelfaehigkeit Prüfen, Vdg 062 Abo Modell Klageschrift Strukturieren, Vdg 063 Abo Modell Anspruchsgruppen Bilden, Vdg 064 Abo Modell Registertext Schreiben im Plugin Verbraucherschutzverband Durchset... |
| `vdg-abo-vdg-abo-vdg-abo-vdg-abo-02` | Nutze dies, wenn Vdg 065 Abo Modell Betroffenenformular Bauen, Vdg 066 Abo Modell Beweisplan Erstellen, Vdg 067 Abo Modell Vergleich Prüfen, Vdg 068 Abo Modell Umsetzung Ueberwachen im Plugin Verbraucherschutzverband Durchsetzung konkret... |
| `vdg-bankentgelte-kommunikation` | Nutze dies, wenn Vdg 029 Bankentgelte Kommunikation Steuern, Vdg 049 Energiepreiserhoehung Kommunikation St, Vdg 059 Plattform Sperre Kommunikation Steuern, Vdg 069 Abo Modell Kommunikation Steuern im Plugin Verbraucherschutzverband Durc... |
| `vdg-bankentgelte-registertext` | Nutze dies, wenn Vdg 024 Bankentgelte Registertext Schreiben, Vdg 025 Bankentgelte Betroffenenformular Bauen, Vdg 026 Bankentgelte Beweisplan Erstellen, Vdg 027 Bankentgelte Vergleich Prüfen im Plugin Verbraucherschutzverband Durchsetzun... |
| `vdg-bankentgelte-umsetzung-risiko-rot` | Nutze dies, wenn Vdg 028 Bankentgelte Umsetzung Ueberwachen, Vdg 030 Bankentgelte Risiko Rot Markieren, Vdg 041 Energiepreiserhoehung Sammelfaehigkeit, Vdg 042 Energiepreiserhoehung Klageschrift Str im Plugin Verbraucherschutzverband Dur... |
| `vdg-beweismittel-vdg-kommunikation-vdg` | Nutze dies, wenn Vdg 011 Beweismittel Offenlegung Nutzen, Vdg 012 Kommunikation An Verbraucher, Vdg 013 Vergleich Und Austritt Prüfen, Vdg 015 Sachwalterfragen Vorbereiten im Plugin Verbraucherschutzverband Durchsetzung konkret bearbeite... |
| `vdg-energiepreiserhoehung-vdg-vdg` | Nutze dies, wenn Vdg 043 Energiepreiserhoehung Anspruchsgruppen, Vdg 044 Energiepreiserhoehung Registertext Sch, Vdg 045 Energiepreiserhoehung Betroffenenformu, Vdg 046 Energiepreiserhoehung Beweisplan Erste im Plugin Verbraucherschutzve... |
| `vdg-energiepreiserhoehung-vdg-vdg-02` | Nutze dies, wenn Vdg 047 Energiepreiserhoehung Vergleich Pruefe, Vdg 048 Energiepreiserhoehung Umsetzung Ueberw, Vdg 050 Energiepreiserhoehung Risiko Rot Marki, Vdg 051 Plattform Sperre Sammelfaehigkeit Prue im Plugin Verbraucherschutzve... |
| `vdg-erfolgsmonitoring-bankentgelte` | Nutze dies, wenn Vdg 020 Erfolgsmonitoring, Vdg 021 Bankentgelte Sammelfaehigkeit Prüfen, Vdg 022 Bankentgelte Klageschrift Strukturiere, Vdg 023 Bankentgelte Anspruchsgruppen Bilden im Plugin Verbraucherschutzverband Durchsetzung konkre... |
| `vdg-finanzierung-interessenkonflikte` | Nutze dies, wenn Vdg 007 Finanzierung Und Interessenkonflikte, Vdg 008 Verbandsklageregister Vorbereiten, Vdg 009 Klageziele Praezise Schneiden, Vdg 010 Lebenssachverhalt Buendeln im Plugin Verbraucherschutzverband Durchsetzung konkret b... |
| `vdg-fitnessstudio-registertext` | Nutze dies, wenn Vdg 074 Fitnessstudio Registertext Schreiben, Vdg 075 Fitnessstudio Betroffenenformular Baue, Vdg 076 Fitnessstudio Beweisplan Erstellen, Vdg 077 Fitnessstudio Vergleich Prüfen im Plugin Verbraucherschutzverband Durchset... |
| `vdg-fitnessstudio-umsetzung-risiko-rot` | Nutze dies, wenn Vdg 078 Fitnessstudio Umsetzung Ueberwachen, Vdg 080 Fitnessstudio Risiko Rot Markieren, Vdg 081 Reiseveranstalter Sammelfaehigkeit Pru, Vdg 082 Reiseveranstalter Klageschrift Struktu im Plugin Verbraucherschutzverband D... |
| `vdg-fitnessstudio-vdg-reiseveranstalter-vdg` | Nutze dies, wenn Vdg 079 Fitnessstudio Kommunikation Steuern, Vdg 089 Reiseveranstalter Kommunikation Steuer, Vdg 099 Flugportal Kommunikation Steuern, Vdg 002 Klageberechtigung Der Stelle Prüfen im Plugin Verbraucherschutzverband Durchs... |
| `vdg-flugportal-beweisplan-umsetzung` | Nutze dies, wenn Vdg 096 Flugportal Beweisplan Erstellen, Vdg 097 Flugportal Vergleich Prüfen, Vdg 098 Flugportal Umsetzung Ueberwachen, Vdg 101 Bankentgelte Zustimmungsfiktion Serie im Plugin Verbraucherschutzverband Durchsetzung konkre... |
| `vdg-flugportal-klageschrift-anspruchsgruppen` | Nutze dies, wenn Vdg 092 Flugportal Klageschrift Strukturieren, Vdg 093 Flugportal Anspruchsgruppen Bilden, Vdg 094 Flugportal Registertext Schreiben, Vdg 095 Flugportal Betroffenenformular Bauen im Plugin Verbraucherschutzverband Durchs... |
| `vdg-individualklagen-vdg-presse-vdg` | Nutze dies, wenn Vdg 016 Individualklagen Koordinieren, Vdg 017 Presse Und Kampagnenrisiko, Vdg 018 Datenschutz Im Betroffenenpool, Vdg 019 Kosten Und Prozessrisiko im Plugin Verbraucherschutzverband Durchsetzung konkret bearbeitet werde... |
| `vdg-inkasso-vdg-bestellbutton-vdg-probeabo` | Nutze dies, wenn Vdg 102 Inkasso Konzerninkasso Musterfeststellung, Vdg 103 Bestellbutton Uklag Uwg Abmahnung, Vdg 104 Probeabo Widerruf Verbandsstrategie, Vdg 105 Schufa Scoring Dsgvo Verbandsfall im Plugin Verbraucherschutzverband Durc... |
| `vdg-plattform-sperre-anspruchsgruppen-bild` | Nutze dies, wenn Vdg 052 Plattform Sperre Klageschrift Struktur, Vdg 053 Plattform Sperre Anspruchsgruppen Bild, Vdg 054 Plattform Sperre Registertext Schreibe, Vdg 055 Plattform Sperre Betroffenenformular B im Plugin Verbraucherschutzve... |
| `vdg-plattform-sperre-umsetzung-ueberwachen` | Nutze dies, wenn Vdg 056 Plattform Sperre Beweisplan Erstellen, Vdg 057 Plattform Sperre Vergleich Prüfen, Vdg 058 Plattform Sperre Umsetzung Ueberwachen, Vdg 060 Plattform Sperre Risiko Rot Markieren im Plugin Verbraucherschutzverband D... |
| `vdg-reiseveranstalter-vdg-vdg` | Nutze dies, wenn Vdg 083 Reiseveranstalter Anspruchsgruppen Bil, Vdg 084 Reiseveranstalter Registertext Schreib, Vdg 085 Reiseveranstalter Betroffenenformular, Vdg 086 Reiseveranstalter Beweisplan Erstellen im Plugin Verbraucherschutzver... |
| `vdg-reiseveranstalter-vdg-vdg-02` | Nutze dies, wenn Vdg 087 Reiseveranstalter Vergleich Prüfen, Vdg 088 Reiseveranstalter Umsetzung Ueberwache, Vdg 090 Reiseveranstalter Risiko Rot Markieren, Vdg 091 Flugportal Sammelfaehigkeit Prüfen im Plugin Verbraucherschutzverband Du... |
| `vdg-telekommunikationsklausel-registertext` | Nutze dies, wenn Vdg 034 Telekommunikationsklausel Registertext, Vdg 035 Telekommunikationsklausel Betroffenenf, Vdg 036 Telekommunikationsklausel Beweisplan E, Vdg 037 Telekommunikationsklausel Vergleich Pr im Plugin Verbraucherschutzve... |
| `vdg-telekommunikationsklausel-umsetzung` | Nutze dies, wenn Vdg 038 Telekommunikationsklausel Umsetzung Ue, Vdg 039 Telekommunikationsklausel Kommunikatio, Vdg 040 Telekommunikationsklausel Risiko Rot M, Vdg 106 Diesel Differenzschaden Serienfall im Plugin Verbraucherschutzverban... |
| `vdg-umsetzungsverfahren-vdg` | Nutze dies, wenn Vdg 014 Umsetzungsverfahren Planen, Vdg 031 Telekommunikationsklausel Sammelfaehig, Vdg 032 Telekommunikationsklausel Klageschrift, Vdg 033 Telekommunikationsklausel Anspruchsgru im Plugin Verbraucherschutzverband Durchs... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
