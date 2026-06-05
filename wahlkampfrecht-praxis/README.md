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
| `wahlkampf-aktenplan-beweisarchiv-amtstraeger` | Wahlkampf Aktenplan Beweisarchiv Amtstraeger: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-asymmetrische-demobilisierung` | Wahlkampf Asymmetrische Demobilisierung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-briefwahlkommunikation` | Wahlkampf Briefwahlkommunikation: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-cybersicherheit-kampagne` | Wahlkampf Cybersicherheit Kampagne: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-ebenen-wahlart-ehrenamtliche` | Wahlkampf Ebenen Wahlart Ehrenamtliche: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-foreign-interference-foto-wahlraum` | Wahlkampf Foreign Interference Foto Wahlraum: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-gegnerkritik-meinungsfreiheit` | Wahlkampf Gegnerkritik Meinungsfreiheit: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-haustuerwahlkampf-influencer` | Wahlkampf Haustuerwahlkampf Influencer: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-kaltstart-routing` | Wahlkampfrecht Praxis: Kaltstart fuer jede Wahlkampflage mit Routing zu Recht, Strategie, Digital, Plakatierung, Finanzen oder Krise. |
| `wahlkampf-kandidatenbriefing-kamera` | Wahlkampf Kandidatenbriefing Kamera: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-koalitionssignale-kommunalwahlkampf` | Wahlkampf Koalitionssignale Kommunalwahlkampf: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-landeslisten-direktkandidaten` | Wahlkampf Landeslisten Direktkandidaten: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-lokale-buendnisse-marken-fremdlogos` | Wahlkampf Lokale Buendnisse Marken Fremdlogos: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-nachwahl-evaluation-negative` | Wahlkampf Nachwahl Evaluation Negative: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-ordner-sicherheit-parteieigenschaft` | Wahlkampf Ordner Sicherheit Parteieigenschaft: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-plattformmeldung-dsa-podium` | Wahlkampf Plattformmeldung DSA Podium: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-rapid-response-rechenschaftsbericht` | Wahlkampf Rapid Response Rechenschaftsbericht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-satellitenkampagne-durch` | Wahlkampf Satellitenkampagne Durch: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-spendenannahme-sponsoring` | Wahlkampf Spendenannahme Sponsoring: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-targeting-dsgvo-tracking-pixel` | Wahlkampf Targeting DSGVO Tracking Pixel: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-unterstuetzungsunterschriften` | Wahlkampf Unterstuetzungsunterschriften: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-viraler-clip-waehlerdaten-listen` | Wahlkampf Viraler Clip Waehlerdaten Listen: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-wahlkampfkosten-budget-wahlprogramm` | Wahlkampf Wahlkampfkosten Budget Wahlprogramm: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-wahltag-war` | Wahlkampf Wahltag WAR: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wahlkampf-wahlverfahren-falschinfo` | Wahlkampf Wahlverfahren Falschinfo: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
