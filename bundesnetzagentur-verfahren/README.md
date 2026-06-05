# Bundesnetzagentur-Verfahren

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`bundesnetzagentur-verfahren`) | [`bundesnetzagentur-verfahren.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bundesnetzagentur-verfahren.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Märkische Reserve Süd — Batteriespeicher Brandenburg/Berlin** (`batteriespeicher-brandenburg-berlin-resilienz`) | [Gesamt-PDF lesen](../testakten/batteriespeicher-brandenburg-berlin-resilienz/gesamt-pdf/batteriespeicher-brandenburg-berlin-resilienz_gesamt.pdf) | [`testakte-batteriespeicher-brandenburg-berlin-resilienz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-batteriespeicher-brandenburg-berlin-resilienz.zip) |
| **Projekt Isarlicht — Kernfusion und Transrapid am Starnberger See** (`kernfusion-transrapid-starnberger-see`) | [Gesamt-PDF lesen](../testakten/kernfusion-transrapid-starnberger-see/gesamt-pdf/kernfusion-transrapid-starnberger-see_gesamt.pdf) | [`testakte-kernfusion-transrapid-starnberger-see.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kernfusion-transrapid-starnberger-see.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Großes Regulierungs-Plugin für anwaltliche Arbeit mit der Bundesnetzagentur in Energie, Telekommunikation, Post, Eisenbahn und Digital Services.

## Wofür dieses Plugin da ist
Anwaltliche Verfahren mit der Bundesnetzagentur: Zuständigkeit, Beschlusskammern, Konsultationen, Auskünfte, Bußgelder, Beschwerden, Energie-, TK-, Post-, Eisenbahn- und DSA-Regulierung.

Das Plugin ist als Arbeitswerkzeug gedacht: Es startet mit einem Kaltstart-Interview, sortiert Unterlagen, prüft Fristen und routet dann in Spezial-Skills. Es soll Anfänger an die Hand nehmen und Profis schnell zu belastbaren Outputs bringen.

## Typischer Workflow
1. **Allgemein-Skill starten:** Rolle, Ziel, Frist, Unterlagen und gewünschtes Ergebnis klären.
2. **Dokumente einlesen:** Verträge, Bescheide, Rechnungen, Tabellen, Registerdaten, Behördenpost oder Screenshots strukturieren.
3. **Spezial-Skill wählen:** Das Plugin schlägt den passenden Skill vor und erklärt, welches Ergebnis damit entsteht.
4. **Live-Quellen prüfen:** Normtext, Behördenseite, EU-Text, Formular oder frei zugängliche Rechtsprechung aktualisieren.
5. **Output erzeugen:** Memo, Antrag, Stellungnahme, Vertragsklausel, Berechnung, Checkliste oder Mandantenbrief.
6. **Red-Team:** Fristen, Zuständigkeit, Zahlen, Quellen und Gegenargumente kontrollieren.

## Quellenanker
- Amtliche Gesetzestexte: gesetze-im-internet.de.
- EU-Recht: EUR-Lex und amtliche Kommissionsseiten.
- Behördenpraxis: zuständige Bundes-/Landesbehörden, Bundesnetzagentur, BaFin, BfArM, G-BA, BKartA oder Länderstellen je nach Thema.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei/amtlich prüfbarer Quelle.

## Skill-Schwerpunkte
| Gruppe | Inhalt |
| --- | --- |
| Einstieg und Workflow | Kaltstart, Dokumentenintake, Fristen, Quellencheck, Output-Wahl, Red-Team |
| Materielle Prüfung | Tatbestände, Ausnahmen, Schwellen, Beweislast, Berechnungen, Rechtsfolgen |
| Verfahren und Kommunikation | Anträge, Anhörungen, Beschwerden, Schriftsätze, Behördenkontakt, Mandantenkommunikation |
| Spezialthemen | Branchen-, Vertrags-, Gebühren-, Aufsichts-, EU- und Edge-Case-Prüfungen |

## Quellen- und Halluzinationsschutz
Dieses Plugin soll keine nicht prüfbaren Fundstellen produzieren. Bei unsicherer oder dynamischer Rechtslage wird der Live-Quellencheck ausdrücklich vorgeschaltet.

## Lizenz
Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 32 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anhoerung-auskunftsbeschluss-digital-services` | Anhoerung Auskunftsbeschluss Digital Services: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `bundesnetzagentur-verfahren-kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im Bundesnetzagentur-Verfahren-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, erkennt stumme Uploads und schlägt passende Fachmodule aus diesem Plugin vor. |
| `digital-services-algorithmen` | Digital Services Algorithmen: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `eilrechtsschutz-vwgo-festlegungsverfahren` | Eilrechtsschutz Vwgo Festlegungsverfahren: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `eisenbahn-digital-services-trusted-flagger` | Eisenbahn Digital Services Trusted Flagger: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `eisenbahn-kapazitaetskonflikt-fahrplan` | Eisenbahn Kapazitaetskonflikt Fahrplan: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `energie-bbplg-leitungsvorhaben-bilanzkreis` | Energie Bbplg Leitungsvorhaben Bilanzkreis: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `energie-kapazitaetsvergabe-gas-kwkg` | Energie Kapazitaetsvergabe GAS Kwkg: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `energie-netzentgelte-gas-strom-offshore` | Energie Netzentgelte GAS Strom Offshore: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `energie-regulierungsakte-anreizregulierung` | Energie Regulierungsakte Anreizregulierung: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `energie-regulierungsakte-bilanzkreis-strom` | Energie Regulierungsakte Bilanzkreis Strom: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `energie-regulierungsakte-eeg-netzanschluss` | Energie Regulierungsakte EEG Netzanschluss: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `energie-regulierungsakte-kapazitaetsvergabe` | Energie Regulierungsakte Kapazitaetsvergabe: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `energie-regulierungsakte-kwkg-ladesaeulen` | Energie Regulierungsakte Kwkg Ladesaeulen: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `energie-regulierungsakte-messstellenbetrieb` | Energie Regulierungsakte Messstellenbetrieb: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `energie-regulierungsakte-netzanschluss-strom` | Energie Regulierungsakte Netzanschluss Strom: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `energie-regulierungsakte-offshore` | Energie Regulierungsakte Offshore: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `energie-regulierungsakte-redispatch` | Energie Regulierungsakte Redispatch: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `energie-regulierungsakte-remit` | Energie Regulierungsakte Remit: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `energie-regulierungsakte-tk` | Energie Regulierungsakte TK: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `energie-regulierungsakte-wasserstoffnetz` | Energie Regulierungsakte Wasserstoffnetz: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kaltstart-bundesnetzagentur-mandat` | Kaltstart Bundesnetzagentur-Mandat: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `post-arbeitsbedingungen-postmarkt-beschwerde` | Post Arbeitsbedingungen Postmarkt Beschwerde: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `post-postlizenz-anzeige-postmarktregulierung` | Post Postlizenz Anzeige Postmarktregulierung: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `telekommunikation-frequenzauktion` | Telekommunikation Frequenzauktion: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `telekommunikation-nummernverwaltung` | Telekommunikation Nummernverwaltung: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `telekommunikation-stoerung` | Telekommunikation Stoerung: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `tk-regulierungsakte-frequenzauktion` | TK Regulierungsakte Frequenzauktion: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `tk-regulierungsakte-tk-akteneinsicht` | TK Regulierungsakte TK Akteneinsicht: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `tk-regulierungsakte-tk-aktenzugang` | TK Regulierungsakte TK Aktenzugang: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `tk-regulierungsakte-tkg-marktregulierung` | TK Regulierungsakte TKG Marktregulierung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `vorstandsvorlage-regulierungsrisiko` | Vorstandsvorlage Regulierungsrisiko: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
