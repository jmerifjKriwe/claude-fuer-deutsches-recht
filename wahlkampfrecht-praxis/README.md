# Wahlkampfrecht Praxis

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`wahlkampfrecht-praxis`) | [`wahlkampfrecht-praxis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/wahlkampfrecht-praxis.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Wahlkampfakte Morgenstadt 2026 - Landesliste, Plakatierung und digitale Lage** (`wahlkampfrecht-landtagswahl-morgenstadt-2026`) | [Gesamt-PDF lesen](../testakten/wahlkampfrecht-landtagswahl-morgenstadt-2026/gesamt-pdf/wahlkampfrecht-landtagswahl-morgenstadt-2026_gesamt.pdf) | [`testakte-wahlkampfrecht-landtagswahl-morgenstadt-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-wahlkampfrecht-landtagswahl-morgenstadt-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein großes Arbeitsplugin für demokratische Wahlkampfteams, Parteien, Kandidierende, Wahlkampfmanagerinnen, Kreisverbände, Landesgeschäftsstellen, Bundeswahlkampfstäbe, Kampagnenagenturen und anwaltliche Berater. Es verbindet Recht, Strategie und tägliche Durchführung: Plakatierung, Infostände, Veranstaltungen, Social Media, Daten, Spenden, Kandidatentraining, Krisenkommunikation, Desinformation, Wahltag und Nachbereitung.

Das Plugin soll Kampagnen handlungsfähiger machen, ohne sie zu verrohen. Es hilft bei klarer Message, schneller Lagearbeit und robustem Ground Game. Gleichzeitig zieht es rote Linien: keine Plakat-Sabotage, keine verdeckte Finanzierung, keine rechtswidrige Datennutzung, keine Desinformation, keine fingierten Accounts, keine Irreführung über Wahlverfahren und keine Nutzung staatlicher Ressourcen für Parteizwecke.

## Kaltstart

Starte mit `wahlkampf-allgemeiner-kaltstart` oder `wahlkampf-ebenen-und-wahlart-router`. Das Plugin fragt zuerst:

1. Welche Wahl: Bundestag, Europawahl, Landtag, Kommunalwahl, Bürgermeister-/Landratswahl, innerparteiliche Vorwahl oder Sonderfall?
2. Welche Rolle: Bundesstrategie, Landeswahlkampf, Kreisverband, Kandidatenteam, Agentur, Rechtsabteilung, Schatzmeisterei, Social-Media-Team oder Ehrenamtliche vor Ort?
3. Was ist der Druck: Plakatgenehmigung, Podium, Social-Media-Krise, Spende, Datenschutz, Desinformation, Schulveranstaltung, Wahltag, Behördenbrief oder Strategieplan?
4. Welche Rechtsordnung: Bund, Land, Kommune, Plattform, Datenschutz, Parteienfinanzierung, Strafrecht, Medienrecht, Versammlungsrecht?
5. Welcher Output: Schlachtplan, Freigabecheck, Behördenbrief, Briefing, Risikoampel, Presse-Q&A, Volunteer-Skript, Fristenkalender oder Incident-Log?

## Leitgedanken

- **Demokratisch kampfstark:** klare Strategie, aber keine Manipulation des Wahlverfahrens und keine organisierte Unwahrheit.
- **Recht und Taktik zusammen:** Ein Plakatstandort ist zugleich Sondernutzung, Verkehrssicherheit, Sichtbarkeit, Ehrenamtslogistik und Konfliktrisiko.
- **Resilienz vor Empörung:** Desinformation wird dokumentiert, priorisiert, entkräftet und bei Plattformen/Behörden sauber eskaliert.
- **Authentische Kandidierende:** Nicht alle Menschen sind Medienprofis. Das Plugin trainiert Verhalten unter Kamera, ohne Persönlichkeiten glattzubügeln.
- **Keine falsche Neutralität:** Amtsträger, öffentliche Einrichtungen, Schulen, Verwaltungen und Wahlorgane werden rechtlich sauber getrennt.

## Typische Workflows

| Lage | Einstiegsskills | Ergebnis |
| --- | --- | --- |
| Bundes- oder Landeswahlkampf planen | `wahlkampf-bundesstrategie-architektur`, `wahlkampf-landeswahlkampf-lagekarte`, `wahlkampf-schlachtenplan-ethik-und-taktik` | Strategiepapier, Phasenplan, Risiko-Board |
| Kreisverband muss Plakate hängen | `wahlkampf-plakatierung-genehmigung`, `wahlkampf-plakatstandorte-matrix`, `wahlkampf-fremdplakate-nicht-anruehren` | Standortliste, Teambriefing, Ordnungsamtsmail |
| Social-Media-Krise | `wahlkampf-rapid-response-room`, `wahlkampf-viraler-clip-notfall`, `wahlkampf-faktencheck-gegenrede` | Krisenlog, Q&A, Antwortleiter |
| Politische Online-Werbung | `wahlkampf-eu-2024-900-politische-werbung`, `wahlkampf-targeting-dsgvo`, `wahlkampf-ad-library-transparenz` | Transparenznotiz, Freigabevermerk, Targeting-Ampel |
| Podium mit problematischem Gegner | `wahlkampf-podium-teilnahmeentscheidung`, `wahlkampf-keine-buehne-aber-nicht-fehlen`, `wahlkampf-kandidatenbriefing-kamera` | Teilnahmevermerk, Sprechzettel, Schutzplan |
| Schulen, Jugend, öffentliche Einrichtungen | `wahlkampf-schulen-und-jugendformate`, `wahlkampf-staatliche-neutralitaet`, `wahlkampf-amtstraeger-ressourcen` | Einladungsschreiben, Neutralitätsprüfung, Rollenabgrenzung |
| Wahltag und Wahlraum | `wahlkampf-wahlraum-propagandaverbot`, `wahlkampf-wahlbeobachtung-und-wahltag`, `wahlkampf-briefwahlkommunikation` | Wahltagskarte, Beobachterbriefing, Eskalationspfad |

## Amtliche und frei prüfbare Startquellen

- [Grundgesetz](https://www.gesetze-im-internet.de/gg/) - insbesondere Art. 5, Art. 21 und Wahlrechtsgrundsätze.
- [Bundeswahlgesetz](https://www.gesetze-im-internet.de/bwahlg/) und [Bundeswahlordnung](https://www.gesetze-im-internet.de/bwo_1985/) für Bundestagswahlen.
- [Europawahlgesetz](https://www.gesetze-im-internet.de/euwg/) und [Europawahlordnung](https://www.gesetze-im-internet.de/euwo_1988/) für Europawahlen.
- [Parteiengesetz](https://www.gesetze-im-internet.de/partg/) für Parteienfinanzierung, Spenden, Rechenschaft und Parteiorganisation.
- [Strafgesetzbuch](https://www.gesetze-im-internet.de/stgb/) zu Wahlstraftaten, Nötigung, Beleidigung, Sachbeschädigung und Urkundenthemen.
- [Wahlprüfungsgesetz](https://www.gesetze-im-internet.de/wahlprg/) für Wahlprüfung nach Bundestagswahlen.
- [Bundeswahlleiterin: Wahlwerbung](https://www.bundeswahlleiterin.de/service/glossar/w/wahlwerbung.html), [unzulässige Wahlpropaganda](https://www.bundeswahlleiterin.de/service/glossar/w/wahlpropaganda-unzulaessige.html) und [Fakten gegen Desinformation](https://www.bundeswahlleiterin.de/bundestagswahlen/2025/fakten-desinformation.html).
- [Deutscher Bundestag: Parteienfinanzierung](https://www.bundestag.de/parlament/praesidium/parteienfinanzierung) und [Parteispenden über 35.000 EUR](https://www.bundestag.de/parteispenden).
- [EU-Kommission: Transparency and targeting of political advertising](https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/democracy-eu-citizenship-anti-corruption/democracy-and-electoral-rights/transparency-and-targeting-political-advertising_en) zur Verordnung (EU) 2024/900, die seit 10. Oktober 2025 voll gilt.
- [DSGVO](https://eur-lex.europa.eu/eli/reg/2016/679/oj) und [BDSG](https://www.gesetze-im-internet.de/bdsg_2018/) für Datenverarbeitung im Wahlkampf.
- Lokale Plakatierungs-, Sondernutzungs- und Veranstaltungsregeln der jeweiligen Gemeinde; diese müssen immer aktuell am konkreten Ort geprüft werden.

## Quellenhygiene

Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugänglicher Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen. Bei Landeswahlrecht, Plakatierungsfristen, Sondernutzung, Schulen und Kommunalrecht zwingend die konkrete Gemeinde und das Bundesland live prüfen.

## Datenschutz und Kampagnensicherheit

Keine echten Wählerdaten, Mitgliederdaten, Spenderlisten, Social-Media-Profile, Gesundheitsdaten, politische Meinungsdaten oder internen Kampagnengeheimnisse in ungeprüfte Systeme laden. Das Plugin ist ein Arbeits- und Demonstrationsrahmen; produktiver Einsatz braucht Datenschutz-, Berufsrechts-, Parteienfinanzierungs- und IT-Sicherheitsprüfung.

## Lizenz

Apache-2.0 OR MIT. Siehe Repository-Stammverzeichnis.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 25 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-wahlkampf-wahlverfah-bis-wahlkampf-ad-library` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 01; bündelt 5 frühere Spezialskills (wahlkampf-wahlverfahren-falschinfo, wahlkampf-wahlvorschlaege-fristen, wahlkampf-agenturvertrag-compliance, wahlkampf-72-stunden-sprint, wahlkamp... |
| `kompendium-02-wahlkampf-aktenplan-bis-wahlkampf-archivieru` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 02; bündelt 5 frühere Spezialskills (wahlkampf-aktenplan-und-beweisarchiv, wahlkampf-amtstraeger-ressourcen, wahlkampf-angriff-auf-wahlleitung-vermeiden, wahlkampf-arbeitsrecht-kampa... |
| `kompendium-03-wahlkampf-asymmetris-bis-wahlkampf-briefkaste` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 03; bündelt 5 frühere Spezialskills (wahlkampf-asymmetrische-demobilisierung, wahlkampf-barrierefreie-und-mehrsprachige-information, wahlkampf-barrierefreiheit-und-inklusion, wahlkam... |
| `kompendium-04-wahlkampf-briefwahlk-bis-wahlkampf-compliance` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 04; bündelt 5 frühere Spezialskills (wahlkampf-briefwahlkommunikation, wahlkampf-buergerdialog-schwierige-fragen, wahlkampf-bundesstrategie-architektur, wahlkampf-community-managemen... |
| `kompendium-05-wahlkampf-cybersiche-bis-wahlkampf-desinforma` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 05; bündelt 5 frühere Spezialskills (wahlkampf-cybersicherheit-kampagne, wahlkampf-datenschutz-folgenabschaetzung-politische-daten, wahlkampf-debattenvorbereitung, wahlkampf-deepfake... |
| `kompendium-06-wahlkampf-ebenen-und-bis-wahlkampf-flooding-g` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 06; bündelt 5 frühere Spezialskills (wahlkampf-ebenen-und-wahlart-router, wahlkampf-ehrenamtliche-schulen, wahlkampf-eu-2024-900-politische-werbung, wahlkampf-faktencheck-gegenrede,... |
| `kompendium-07-wahlkampf-foreign-in-bis-wahlkampf-fremdplaka` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 07; bündelt 5 frühere Spezialskills (wahlkampf-foreign-interference-lage, wahlkampf-foto-im-wahlraum-und-stimmzettel, wahlkampf-fraktion-partei-trennung, wahlkampf-freiwillige-und-au... |
| `kompendium-08-wahlkampf-gegnerkrit-bis-wahlkampf-hausrecht` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 08; bündelt 5 frühere Spezialskills (wahlkampf-gegnerkritik-meinungsfreiheit, wahlkampf-gewerkschaften-verbaende-kirchen, wahlkampf-giveaways-waehlerbestechung, wahlkampf-grossspende... |
| `kompendium-09-wahlkampf-haustuerwa-bis-wahlkampf-kandidaten` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 09; bündelt 5 frühere Spezialskills (wahlkampf-haustuerwahlkampf, wahlkampf-influencer-und-unterstuetzer, wahlkampf-infostand-sondernutzung, wahlkampf-interne-chatdisziplin, wahlkamp... |
| `kompendium-10-wahlkampf-kandidaten-bis-wahlkampf-keine-bueh` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 10; bündelt 5 frühere Spezialskills (wahlkampf-kandidatenbriefing-kamera, wahlkampf-kandidatenteam-intake, wahlkampf-kandidierenden-fuersorge, wahlkampf-kassenpruefung-kreisverband,... |
| `kompendium-11-wahlkampf-koalitions-bis-wahlkampf-lagebild-m` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 11; bündelt 5 frühere Spezialskills (wahlkampf-koalitionssignale-und-rote-linien, wahlkampf-kommunalwahlkampf-groundgame, wahlkampf-kostenversprechen-und-finanzierbarkeit, wahlkampf-... |
| `kompendium-12-wahlkampf-landeslist-bis-wahlkampf-leak-und-h` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 12; bündelt 5 frühere Spezialskills (wahlkampf-landeslisten-und-direktkandidaten, wahlkampf-landesrecht-plakatierung-livecheck, wahlkampf-landeswahlkampf-lagekarte, wahlkampf-lautspr... |
| `kompendium-13-wahlkampf-lokale-bue-bis-wahlkampf-minderjaeh` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 13; bündelt 5 frühere Spezialskills (wahlkampf-lokale-buendnisse-und-listen, wahlkampf-marken-und-fremdlogos, wahlkampf-memes-satire-risiko, wahlkampf-message-house-authentizitaet, w... |
| `kompendium-14-wahlkampf-nachwahl-e-bis-wahlkampf-opposition` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 14; bündelt 5 frühere Spezialskills (wahlkampf-nachwahl-evaluation, wahlkampf-negative-campaigning-grenzen, wahlkampf-newsletter-messenger-sms, wahlkampf-oeffentliche-einrichtungen-n... |
| `kompendium-15-wahlkampf-ordner-und-bis-wahlkampf-plakatstan` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 15; bündelt 5 frühere Spezialskills (wahlkampf-ordner-und-sicherheit, wahlkampf-parteieigenschaft-bundeswahlausschuss, wahlkampf-plakat-vandalismus-beweissicherung, wahlkampf-plakati... |
| `kompendium-16-wahlkampf-plattformm-bis-wahlkampf-presserech` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 16; bündelt 5 frühere Spezialskills (wahlkampf-plattformmeldung-dsa, wahlkampf-podium-teilnahmeentscheidung, wahlkampf-polizei-und-ordnungsamt-kommunikation, wahlkampf-presseanfrage-... |
| `kompendium-17-wahlkampf-rapid-resp-bis-wahlkampf-rumor-cont` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 17; bündelt 5 frühere Spezialskills (wahlkampf-rapid-response-room, wahlkampf-rechenschaftsbericht-vorbereitung, wahlkampf-rechtsfreigabe-gate, wahlkampf-risiko-register, wahlkampf-r... |
| `kompendium-18-wahlkampf-satelliten-bis-wahlkampf-social-med` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 18; bündelt 5 frühere Spezialskills (wahlkampf-satellitenkampagne-durch-verein, wahlkampf-schlachtenplan-ethik-und-taktik, wahlkampf-schulen-und-jugendformate, wahlkampf-sicherheitsl... |
| `kompendium-19-wahlkampf-spendenann-bis-wahlkampf-taegliches` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 19; bündelt 5 frühere Spezialskills (wahlkampf-spendenannahme-pruefung, wahlkampf-sponsoring-parteienrecht, wahlkampf-sprachregelung-schnellkarte, wahlkampf-staatliche-neutralitaet,... |
| `kompendium-20-wahlkampf-targeting-bis-wahlkampf-umgang-mit` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 20; bündelt 5 frühere Spezialskills (wahlkampf-targeting-dsgvo, wahlkampf-tracking-pixel-cookies, wahlkampf-ueberkleben-sachbeschaedigung, wahlkampf-umfragen-und-prognosen, wahlkampf... |
| `kompendium-21-wahlkampf-unterstuet-bis-wahlkampf-versammlun` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 21; bündelt 5 frühere Spezialskills (wahlkampf-unterstuetzungsunterschriften, wahlkampf-urheberrecht-musik-bilder-clips, wahlkampf-veranstaltungslogistik, wahlkampf-vereine-unterstue... |
| `kompendium-22-wahlkampf-viraler-cl-bis-wahlkampf-wahlkampf` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 22; bündelt 5 frühere Spezialskills (wahlkampf-viraler-clip-notfall, wahlkampf-waehlerdaten-und-listen, wahlkampf-wahl-o-mat-und-thesen, wahlkampf-wahlbeobachtung-und-wahltag, wahlka... |
| `kompendium-23-wahlkampf-wahlkampfk-bis-wahlkampf-wahlstraft` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 23; bündelt 5 frühere Spezialskills (wahlkampf-wahlkampfkosten-budget, wahlkampf-wahlprogramm-und-faktencheck, wahlkampf-wahlpruefung-nachwahl, wahlkampf-wahlraum-propagandaverbot, w... |
| `kompendium-24-wahlkampf-wahltag-kr-bis-wahlkampf-war-room-b` | wahlkampfrecht-praxis: Konsolidiertes Skill-Kompendium 24; bündelt 2 frühere Spezialskills (wahlkampf-wahltag-krisenkarte, wahlkampf-war-room-betriebsmodell) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `wahlkampf-allgemeiner-kaltstart` | Wahlkampfrecht Praxis: Kaltstart fuer jede Wahlkampflage mit Routing zu Recht, Strategie, Digital, Plakatierung, Finanzen oder Krise. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
