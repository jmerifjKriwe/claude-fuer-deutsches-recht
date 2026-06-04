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

Automatisch generierte Komplett-Liste aller 30 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Bundesnetzagentur-Verfahren-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, erkennt stumme Uploads und schlägt passende Spezial-Skills aus diesem Plugin vor. |
| `kaltstart-bundesnetzagentur-mandat` | Workflow zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Kaltstart Bundesnetzagentur-Mandat. |
| `kompendium-01-anhoerung-auskunftsb-bis-energie-regulierungs` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 01; bündelt 8 frühere Spezialskills (anhoerung-auskunftsbeschluss-fristenplan, digital-services-melde-und-abhilfeverfahren-notice-and-action, eilverfahren-verwaltungsgericht-st... |
| `kompendium-02-energie-regulierungs-bis-energie-regulierungs` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 02; bündelt 8 frühere Spezialskills (energie-regulierungsakte-kwkg-zuschlaege-fristen-und-bescheidana, energie-regulierungsakte-ladesaeulen-elektromobilitaet-fristen-u, energie... |
| `kompendium-03-energie-regulierungs-bis-tk-regulierungsakte` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 03; bündelt 8 frühere Spezialskills (energie-regulierungsakte-redispatch-2-0-fristen-und-bescheidanal, energie-regulierungsakte-regelenergie-fristen-und-bescheidanalys, energie... |
| `kompendium-04-tk-regulierungsakte-bis-verfahren-durchsuchu` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 04; bündelt 8 frühere Spezialskills (tk-regulierungsakte-nummernverwaltung-fristen-und-bescheidanalys, tk-regulierungsakte-rufnummernmissbrauch-fristen-und-bescheidana, verfahr... |
| `kompendium-05-verfahren-eilrechtss-bis-verfahren-verpflicht` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 05; bündelt 8 frühere Spezialskills (verfahren-eilrechtsschutz-80-vwgo, verfahren-festlegungsverfahren-beschlusskammer, verfahren-gebuehren-kosten-bnetza, verfahren-geschaeftsg... |
| `kompendium-06-verfahren-vorstandsv-bis-energie-regulierungs` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 06; bündelt 8 frühere Spezialskills (verfahren-vorstandsvorlage-regulierungsrisiko, verfahren-widerspruch-klage-verwaltungsgericht, zustaendigkeitsradar-energie-telekom-post-ei... |
| `kompendium-07-energie-regulierungs-bis-beschwerde-verbrauch` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 07; bündelt 8 frühere Spezialskills (energie-regulierungsakte-redispatch-2-0-stellungnahme-entwurf, energie-regulierungsakte-regelenergie-stellungnahme-entwurf, tk-regulierungs... |
| `kompendium-08-digital-services-alg-bis-digital-services-onl` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 08; bündelt 8 frühere Spezialskills (digital-services-algorithmen-empfehlungssysteme-dsa, digital-services-aussergerichtliche-streitbeilegungsstelle-dsa, digital-services-dark-... |
| `kompendium-09-digital-services-tra-bis-eisenbahn-entgeltreg` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 09; bündelt 8 frühere Spezialskills (digital-services-transparenzberichte-online-plattformen, digital-services-trusted-flagger-anerkennung, digital-services-vlop-vlose-koordina... |
| `kompendium-10-eisenbahn-kapazitaet-bis-energie-anreizreguli` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 10; bündelt 8 frühere Spezialskills (eisenbahn-kapazitaetskonflikt-fahrplan, eisenbahn-netznutzungsbedingungen, eisenbahn-regulierungsvereinbarung-db-netz-infrago, eisenbahn-se... |
| `kompendium-11-energie-bbplg-leitun-bis-energie-grundversorg` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 11; bündelt 8 frühere Spezialskills (energie-bbplg-leitungsvorhaben, energie-bilanzkreis-gas, energie-bilanzkreis-strom, energie-eeg-netzanschluss-einspeisemanagement, energie-... |
| `kompendium-12-energie-kapazitaetsv-bis-energie-netzanschlus` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 12; bündelt 8 frühere Spezialskills (energie-kapazitaetsvergabe-gas, energie-kwkg-zuschlaege, energie-ladesaeulen-elektromobilitaet, energie-lieferantenwechsel-energie, energie... |
| `kompendium-13-energie-netzentgelte-bis-energie-regulierungs` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 13; bündelt 8 frühere Spezialskills (energie-netzentgelte-gas, energie-netzentgelte-strom, energie-offshore-netzanbindung, energie-redispatch-2-0, energie-regelenergie und 3 we... |
| `kompendium-14-energie-regulierungs-bis-energie-regulierungs` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 14; bündelt 8 frühere Spezialskills (energie-regulierungsakte-anreizregulierung-erloesobergrenze-unte, energie-regulierungsakte-bbplg-leitungsvorhaben-rechtsmittel-che, energie... |
| `kompendium-15-energie-regulierungs-bis-energie-regulierungs` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 15; bündelt 8 frühere Spezialskills (energie-regulierungsakte-eeg-netzanschluss-einspeisemanagement-f, energie-regulierungsakte-eeg-netzanschluss-einspeisemanagement-r, energie... |
| `kompendium-16-energie-regulierungs-bis-energie-regulierungs` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 16; bündelt 8 frühere Spezialskills (energie-regulierungsakte-kapazitaetsvergabe-gas-stellungnahme-en, energie-regulierungsakte-kapazitaetsvergabe-gas-unterlagenanford, energie... |
| `kompendium-17-energie-regulierungs-bis-energie-regulierungs` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 17; bündelt 8 frühere Spezialskills (energie-regulierungsakte-messstellenbetrieb-msbg-smart-meter-rec, energie-regulierungsakte-messstellenbetrieb-msbg-smart-meter-ste, energie... |
| `kompendium-18-energie-regulierungs-bis-energie-regulierungs` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 18; bündelt 8 frühere Spezialskills (energie-regulierungsakte-netzanschluss-strom-rechtsmittel-check, energie-regulierungsakte-netzanschluss-strom-stellungnahme-entwu, energie-... |
| `kompendium-19-energie-regulierungs-bis-energie-regulierungs` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 19; bündelt 8 frühere Spezialskills (energie-regulierungsakte-offshore-netzanbindung-rechtsmittel-che, energie-regulierungsakte-offshore-netzanbindung-stellungnahme-en, energie... |
| `kompendium-20-energie-regulierungs-bis-energie-regulierungs` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 20; bündelt 8 frühere Spezialskills (energie-regulierungsakte-remit-marktmissbrauch-energie-stellungn, energie-regulierungsakte-remit-marktmissbrauch-energie-unterlage, energie... |
| `kompendium-21-energie-regulierungs-bis-livecheck-bnetza-kon` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 21; bündelt 8 frühere Spezialskills (energie-regulierungsakte-wasserstoffnetz-regulierung-rechtsmitte, energie-regulierungsakte-wasserstoffnetz-regulierung-stellungnah, energie... |
| `kompendium-22-post-arbeitsbedingun-bis-post-postgeheimnis` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 22; bündelt 8 frühere Spezialskills (post-arbeitsbedingungen-postmarkt-schnittstelle, post-beschwerde-brief-paket, post-grenzueberschreitende-paketzustellung, post-laufzeitmess... |
| `kompendium-23-post-postlizenz-anze-bis-telekommunikation-en` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 23; bündelt 8 frühere Spezialskills (post-postlizenz-anzeige, post-postmarktregulierung, post-postuniversaldienst, post-zugang-postfachanlage, stellungnahme-und-compliance-akti... |
| `kompendium-24-telekommunikation-fr-bis-telekommunikation-no` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 24; bündelt 8 frühere Spezialskills (telekommunikation-frequenzauktion, telekommunikation-frequenzzuteilung, telekommunikation-glasfaserausbau-mitnutzung, telekommunikation-inh... |
| `kompendium-25-telekommunikation-nu-bis-telekommunikation-sp` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 25; bündelt 8 frühere Spezialskills (telekommunikation-nummernverwaltung, telekommunikation-providerwechsel-minderungsrecht, telekommunikation-roaming-eu-schnittstelle, telekom... |
| `kompendium-26-telekommunikation-st-bis-tk-regulierungsakte` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 26; bündelt 8 frühere Spezialskills (telekommunikation-stoerung-entstoerung-verbraucherrechte, telekommunikation-telekommunikationsgeheimnis, telekommunikation-tk-verbrauchersc... |
| `kompendium-27-tk-regulierungsakte-bis-tk-regulierungsakte` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 27; bündelt 8 frühere Spezialskills (tk-regulierungsakte-frequenzauktion-unterlagenanforderung, tk-regulierungsakte-frequenzzuteilung-rechtsmittel-check, tk-regulierungsakte-fr... |
| `kompendium-28-tk-regulierungsakte-bis-tk-regulierungsakte` | bundesnetzagentur-verfahren: Konsolidiertes Skill-Kompendium 28; bündelt 3 frühere Spezialskills (tk-regulierungsakte-tkg-marktregulierung-betraechtliche-marktm-3, tk-regulierungsakte-tkg-marktregulierung-betraechtliche-marktm-4, tk-regu... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
