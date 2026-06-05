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
| `anhoerung-auskunftsbeschluss-digital-services` | Anhoerung Auskunftsbeschluss Fristenplan, Digital Services Melde Und Abhilfeverfahren Notice And Action, Eilverfahren Verwaltungsgericht Strategie, Energie Regulierungsakte Bbplg Leitungsvorhaben Fristen Und Besc: wählt den konkreten Prü... |
| `bundesnetzagentur-verfahren-kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im Bundesnetzagentur-Verfahren-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, erkennt stumme Uploads und schlägt passende Fachmodule aus diesem Plugin vor. |
| `digital-services-algorithmen` | Digital Services Algorithmen Empfehlungssysteme Dsa, Digital Services Aussergerichtliche Streitbeilegungsstelle Dsa, Digital Services Dark Patterns Dsa Schnittstelle, Digital Services Datenzugang Forscher Dsa: wählt den konkreten Prüfpfa... |
| `eilrechtsschutz-vwgo-festlegungsverfahren` | Verfahren Eilrechtsschutz 80 Vwgo, Verfahren Festlegungsverfahren Beschlusskammer, Verfahren Gebuehren Kosten Bnetza, Verfahren Geschaeftsgeheimnisse Im Verwaltungsverfahren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Bel... |
| `eisenbahn-digital-services-trusted-flagger` | Digital Services Transparenzberichte Online Plattformen, Digital Services Trusted Flagger Anerkennung, Digital Services Vlop Vlose Koordination Eu Kommission, Eisenbahn Anreizsetzung Schiene: wählt den konkreten Prüfpfad, trennt Frist, Z... |
| `eisenbahn-kapazitaetskonflikt-fahrplan` | Eisenbahn Kapazitaetskonflikt Fahrplan, Eisenbahn Netznutzungsbedingungen, Eisenbahn Regulierungsvereinbarung Db Netz Infrago, Eisenbahn Serviceeinrichtungen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgr... |
| `energie-bbplg-leitungsvorhaben-bilanzkreis` | Energie Bbplg Leitungsvorhaben, Energie Bilanzkreis Gas, Energie Bilanzkreis Strom, Energie Eeg Netzanschluss Einspeisemanagement: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den näch... |
| `energie-kapazitaetsvergabe-gas-kwkg` | Energie Kapazitaetsvergabe Gas, Energie Kwkg Zuschlaege, Energie Ladesaeulen Elektromobilitaet, Energie Lieferantenwechsel Energie: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den näc... |
| `energie-netzentgelte-gas-strom-offshore` | Energie Netzentgelte Gas, Energie Netzentgelte Strom, Energie Offshore Netzanbindung, Energie Redispatch 2 0: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `energie-regulierungsakte-anreizregulierung` | Energie Regulierungsakte Anreizregulierung Erloesobergrenze Unte, Energie Regulierungsakte Bbplg Leitungsvorhaben Rechtsmittel Che, Energie Regulierungsakte Bbplg Leitungsvorhaben Stellungnahme En, Energie Regulierungsakte Bbplg Leitungs... |
| `energie-regulierungsakte-bilanzkreis-strom` | Energie Regulierungsakte Bilanzkreis Gas Fristen Und Bescheidana, Energie Regulierungsakte Bilanzkreis Strom Fristen Und Bescheida, Energie Regulierungsakte Grosshandelsdaten Transparenz Fristen U, Energie Regulierungsakte Kapazitaetsver... |
| `energie-regulierungsakte-eeg-netzanschluss` | Energie Regulierungsakte Eeg Netzanschluss Einspeisemanagement F, Energie Regulierungsakte Eeg Netzanschluss Einspeisemanagement R, Energie Regulierungsakte Eeg Netzanschluss Einspeisemanagement S, Energie Regulierungsakte Eeg Netzanschl... |
| `energie-regulierungsakte-kapazitaetsvergabe` | Energie Regulierungsakte Kapazitaetsvergabe Gas Stellungnahme En, Energie Regulierungsakte Kapazitaetsvergabe Gas Unterlagenanford, Energie Regulierungsakte Kwkg Zuschlaege Rechtsmittel Check, Energie Regulierungsakte Kwkg Zuschlaege Unt... |
| `energie-regulierungsakte-kwkg-ladesaeulen` | Energie Regulierungsakte Kwkg Zuschlaege Fristen Und Bescheidana, Energie Regulierungsakte Ladesaeulen Elektromobilitaet Fristen U, Energie Regulierungsakte Nabeg Planfeststellung Fristen Und Besc, Energie Regulierungsakte Netzanschluss... |
| `energie-regulierungsakte-messstellenbetrieb` | Energie Regulierungsakte Messstellenbetrieb Msbg Smart Meter Rec, Energie Regulierungsakte Messstellenbetrieb Msbg Smart Meter Ste, Energie Regulierungsakte Messstellenbetrieb Msbg Smart Meter Unt, Energie Regulierungsakte Nabeg Planfest... |
| `energie-regulierungsakte-netzanschluss-strom` | Energie Regulierungsakte Netzanschluss Strom Rechtsmittel Check, Energie Regulierungsakte Netzanschluss Strom Stellungnahme Entwu, Energie Regulierungsakte Netzanschluss Strom Unterlagenanforderu, Energie Regulierungsakte Netzentgelte Ga... |
| `energie-regulierungsakte-offshore` | Energie Regulierungsakte Offshore Netzanbindung Rechtsmittel Che, Energie Regulierungsakte Offshore Netzanbindung Stellungnahme En, Energie Regulierungsakte Offshore Netzanbindung Unterlagenanford, Energie Regulierungsakte Redispatch 2 0... |
| `energie-regulierungsakte-redispatch` | Energie Regulierungsakte Redispatch 2 0 Fristen Und Bescheidanal, Energie Regulierungsakte Regelenergie Fristen Und Bescheidanalys, Energie Regulierungsakte Remit Marktmissbrauch Energie Fristen U, Energie Regulierungsakte Unbundling Ent... |
| `energie-regulierungsakte-remit` | Energie Regulierungsakte Remit Marktmissbrauch Energie Stellungn, Energie Regulierungsakte Remit Marktmissbrauch Energie Unterlage, Energie Regulierungsakte Unbundling Entflechtung Rechtsmittel Ch, Energie Regulierungsakte Unbundling Ent... |
| `energie-regulierungsakte-tk` | Energie Regulierungsakte Redispatch 2 0 Stellungnahme Entwurf, Energie Regulierungsakte Regelenergie Stellungnahme Entwurf, Tk Regulierungsakte Frequenzauktion Stellungnahme Entwurf, Tk Regulierungsakte Frequenzzuteilung Stellungnahme En... |
| `energie-regulierungsakte-wasserstoffnetz` | Energie Regulierungsakte Wasserstoffnetz Regulierung Rechtsmitte, Energie Regulierungsakte Wasserstoffnetz Regulierung Stellungnah, Energie Regulierungsakte Wasserstoffnetz Regulierung Unterlagena, Energie Remit Marktmissbrauch Energie:... |
| `kaltstart-bundesnetzagentur-mandat` | Kaltstart Bundesnetzagentur-Mandat: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `post-arbeitsbedingungen-postmarkt-beschwerde` | Post Arbeitsbedingungen Postmarkt Schnittstelle, Post Beschwerde Brief Paket, Post Grenzueberschreitende Paketzustellung, Post Laufzeitmessung Qualitaet: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundla... |
| `post-postlizenz-anzeige-postmarktregulierung` | Post Postlizenz Anzeige, Post Postmarktregulierung, Post Postuniversaldienst, Post Zugang Postfachanlage: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `telekommunikation-frequenzauktion` | Telekommunikation Frequenzauktion, Telekommunikation Frequenzzuteilung, Telekommunikation Glasfaserausbau Mitnutzung, Telekommunikation Inhouse Verkabelung Gebaeudenetze: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege... |
| `telekommunikation-nummernverwaltung` | Telekommunikation Nummernverwaltung, Telekommunikation Providerwechsel Minderungsrecht, Telekommunikation Roaming Eu Schnittstelle, Telekommunikation Routerfreiheit Endgeraete: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, B... |
| `telekommunikation-stoerung` | Telekommunikation Stoerung Entstoerung Verbraucherrechte, Telekommunikation Telekommunikationsgeheimnis, Telekommunikation Tk Verbraucherschlichtung, Telekommunikation Tkg Marktregulierung Betraechtliche Marktmacht: wählt den konkreten P... |
| `tk-regulierungsakte-frequenzauktion` | Tk Regulierungsakte Frequenzauktion Unterlagenanforderung, Tk Regulierungsakte Frequenzzuteilung Rechtsmittel Check, Tk Regulierungsakte Frequenzzuteilung Unterlagenanforderung, Tk Regulierungsakte Nummernverwaltung Rechtsmittel Check: w... |
| `tk-regulierungsakte-tk-akteneinsicht` | Tk Regulierungsakte Nummernverwaltung Fristen Und Bescheidanalys, Tk Regulierungsakte Rufnummernmissbrauch Fristen Und Bescheidana, Verfahren Akteneinsicht Drittbeteiligte, Verfahren Auskunftsersuchen Bnetza Beantworten: wählt den konkre... |
| `tk-regulierungsakte-tk-aktenzugang` | Tk Regulierungsakte Nummernverwaltung Stellungnahme Entwurf, Tk Regulierungsakte Rufnummernmissbrauch Stellungnahme Entwurf, Aktenzugang Geschaeftsgeheimnisse Schwaerzung, Beschwerde Verbraucher Unternehmen Verband: wählt den konkreten P... |
| `tk-regulierungsakte-tkg-marktregulierung` | Tk Regulierungsakte Tkg Marktregulierung Betraechtliche Marktm 3, Tk Regulierungsakte Tkg Marktregulierung Betraechtliche Marktm 4, Tk Regulierungsakte Tkg Marktregulierung Betraechtliche Marktmac: wählt den konkreten Prüfpfad, trennt Fr... |
| `vorstandsvorlage-regulierungsrisiko` | Verfahren Vorstandsvorlage Regulierungsrisiko, Verfahren Widerspruch Klage Verwaltungsgericht, Zustaendigkeitsradar Energie Telekom Post Eisenbahn Digitales, Energie Regulierungsakte Bilanzkreis Gas Stellungnahme Entwurf: wählt den konkr... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
