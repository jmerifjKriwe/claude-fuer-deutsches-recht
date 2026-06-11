# Megaprompt: luftrecht-flughafenrecht

> *Achtung: Dies ist ein experimentelles Mega-Prompt-Markdown, das einen kompletten Klotzkette-Plugin in eine einzige Datei zusammenfuehrt. Keine Haftung, keine Gewaehr. Nur zum Ausprobieren der Skills auch ohne Claude Code; keine Rechtsberatung. Vor Verwendung im Mandat anwaltlich pruefen.*
>
> *Caution: This is an experimental Mega-Prompt Markdown that consolidates a full Klotzkette plugin into a single file. No warranty, no liability. For exploration with chat tools that do not run Claude Code only; not legal advice.*

**Verwendung:** Diesen gesamten Text in einen Chat ohne Claude-Code-Integration einfuegen (oder als Datei hochladen). Der Chat-Agent erhaelt damit die gebuendelten Skills dieses Plugins als Kontext. Eine Replikation des vollen Plugin-Verhaltens ist nicht garantiert — der Megaprompt ist eine Best-Effort-Kompression.


## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 120 Skills des Plugins `luftrecht-flughafenrecht`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Luftrecht und Flughafenrecht: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und e…
2. **aircraft-arrest-airline-finanzielle** — Mandant will Flugzeug im Ausland arrestieren oder auslaendischer Glaeubiger arrestiert in Deutschland. Prueft Cape Town …
3. **airline-dashboard-bauen** — Kanzlei oder Mandant braucht operatives Airline-Dashboard für laufendes Mandat: Genehmigungsstatus Flotte Slots Sicherhe…
4. **airline-finanzielle-leistungsfaehigkei** — LBA prueft finanzielle Leistungsfaehigkeit nach EU-VO 1008/2008 Art. 5 oder Mandant bewertet Insolvenzrisiko einer Flugg…
5. **airline-genehmigung-pruefen** — Airline-Genehmigungsstand ist unklar: Betriebsgenehmigung AOC Streckengenehmigung oder Sonderflugerlaubnis fehlt oder la…
6. **airline-insolvenzrisiko-markieren** — Mandant will Insolvenzrisiko einer Airline fruehzeitig erkennen: sinkende Liquiditaet schlechte Ratings Zahlungsruecksta…
7. **airline-local-dashboard-bauen** — Deutsches Kanzleiteam muss auslaendischen Anwalt für Airline-Mandat briefen: Arrest Insolvenz Cape-Town oder Betriebsgen…
8. **airline-mandantenmemo-schreiben** — Anwalt schreibt Mandantenmemo für Airline zu komplexem Luftrechtsfall: Genehmigungsrisiko Sicherheitsauflage Slot-Verlus…
9. **airline-pfaendung-planen** — Glaeubiger plant Zwangsvollstreckung in Airline-Flugzeug oder Airline wehrt Pfaendung ab. Prueft ZPO §§ 864-871 LuftFzgG…
10. **airline-pfandrecht-pfaendung-planen** — Kreditgeber will Pfandrecht an Airline-Flugzeug bestellen oder bestehender Pfandglaeubigerrang soll gesichert werden. Pr…
11. **airline-register-auswerten** — Mandant will Luftfahrzeugrolle Pfandrechtsregister und Cape-Town-Register einer Airline auswerten. Skill fuehrt struktur…
12. **airline-sicherheitsauflage-bewerten** — Airline erhaelt LuftSiG oder EASA-Auflage nach Inspektion. Prueft LuftSiG §§ 8-9 Sicherheitsprogramm EU-DVO 2015/1998 Fi…
13. **airline-zustaendigkeit-pruefen** — Airline-Mandat: unklar welche Behörde zuständig ist LBA EU-Behörde Landesbehoerde oder auslaendische Luftfahrtbehoerde. …
14. **betriebsgenehmigung-airline** — Airline beantragt Betriebsgenehmigung beim LBA oder bestehende Genehmigung soll geaendert oder widerrufen werden. Prueft…
15. **drohnen-uas-betrieb** — Drohnenbetreiber braucht Betriebsgenehmigung oder Mandant ist nach Drohnenflug-Unfall in Haftungsfragen verwickelt. Prue…

---

## Skill: `kaltstart-triage`

_Luftrecht und Flughafenrecht: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe._

# Luftrecht und Flughafenrecht - Allgemeiner Einstieg

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Luftrecht Flughafenrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Startfragen

1. Wer nutzt das Plugin: Laie, Verband, Kanzlei, Behörde, Unternehmen, Presse, Verwaltung oder Fachabteilung?
2. Welche Entscheidung steht jetzt an und welche Frist läuft?
3. Welche Dokumente liegen vor, welche fehlen und welche Quelle muss live geprüft werden?
4. Welche Behörde, welches Gericht, welches Register oder welcher private Akteur ist betroffen?
5. Soll am Ende ein Antrag, ein Widerspruch, eine Klage-/Eilantragslinie, ein Dashboard, ein Memo oder ein Schreiben entstehen?

## Workflow

1. Sachverhalt in Akte, Normpfad, Zuständigkeit, Frist, Beweis und Ziel zerlegen.
2. Die einschlägige Norm nicht aus dem Gedächtnis final behaupten, sondern als Live-Check gegen amtliche Quelle markieren.
3. Ablehnungs-, Kosten-, Zuständigkeits- und Beweisrisiken offen in einer Ampel führen.
4. Bei Mehr-Ebenen-Recht immer Bund, Land, Kommune, EU/international und Spezialgesetz trennen.
5. Ausgabe mit konkretem nächsten Schritt, offenen Rückfragen und einer kurzen Fassung für Nichtjuristen schließen.

## Typische Ausgaben

- Prüfvermerk mit Normpfad und Live-Check-Liste
- Fristen- und Zuständigkeitsmatrix
- Entwurf für Antrag, Widerspruch, Klagebaustein oder Behördenbrief
- Dashboard-/Tracker-Eintrag mit Status, Risiko und nächster Aktion

## Red Flags

- blindes Zitieren nicht verifizierter Rechtsprechung oder alter Gesetzesstände
- falsche Behörde, falscher Rechtsweg oder unbemerkte Spezialzuständigkeit
- Gebühren-, Frist-, Präklusions-, Geheimschutz-, Datenschutz- oder Drittbetroffenenproblem
- politisch klingende Bewertung ohne saubere Rechtsgrundlage und Beleglogik

## Quellen- und Qualitätsregel

Primär mit amtlichen Gesetzestexten, Behördenhinweisen, Gerichtsentscheidungen mit Datum/Aktenzeichen und frei prüfbaren Quellen arbeiten. Literatur, Datenbanken hinter Paywalls und Fundstellen ohne Nutzerquelle nicht behaupten. Wenn Landesrecht, EU-Recht oder ausländisches Recht berührt ist, den Rechtsstand ausdrücklich live prüfen und die Ausgabe als Arbeitsfassung kennzeichnen.

---

## Skill: `aircraft-arrest-airline-finanzielle`

_Mandant will Flugzeug im Ausland arrestieren oder auslaendischer Glaeubiger arrestiert in Deutschland. Prueft Cape Town Convention Art. 8-10 Aircraft Protocol Remedies IDERA bilaterale Vollstreckungsvertraege und nationales ZPO-Arrestrecht und liefert Arrest-Strategie und Local-Counsel-Briefing-V..._

# Aircraft Arrest International – grenzüberschreitender Flugzeug-Arrest

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: LuftVG; LuftSiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Deutscher Leasinggeber will nach Vertragsbruch des ausländischen Leasingnehmers das Flugzeug bei Zwischenstopp in London arrestieren lassen.
- Ausländischer Gläubiger will Flugzeug einer deutschen Airline bei Landung in New York sichern.
- Airline-Insolvenz: mehrere Gläubiger aus verschiedenen Ländern konkurrieren um Arreste auf die verbliebene Flotte.

## Erste Schritte

1. Aufenthaltsort des Flugzeugs ermitteln: Flugplan ADS-B-Tracking Flughafendaten; Jurisdiktion folgt physischem Standort.
2. Cape Town Convention prüfen: beide Länder Vertragsstaaten? Dann gelten Art. 8-15 Aircraft Protocol für Sicherungsrechte und Remedies.
3. IDERA prüfen: Irrevocable Deregistration and Export Request Authorisation; ermöglicht Entregistrierung ohne Gerichtsverfahren.
4. Lokalen Counsel beauftragen: Arrest-Antrag nach lokaler ZPO; in UK CPR Part 61 in USA Federal Aviation Act.
5. Cape Town Remedies in Insolvenz: Art. 30 Aircraft Protocol; Alternative A (automatische Herausgabe) oder Alternative B (Genehmigungserfordernis).
6. Koordination: deutsche Vollstreckungsmaßnahmen (ZPO §§ 916 ff.) parallel zu internationalem Arrest.

## Rechtsrahmen

- **Cape Town Convention Art. 8**: Gläubigerrechte bei Nichterfüllung; Besitznahme Veräußerung Vermietung.
- **Cape Town Convention Art. 10**: Zusätzliche Remedies in Insolvenz.
- **Aircraft Protocol Art. IX**: Entregistrierung und Verbringung; IDERA als Instrument.
- **Aircraft Protocol Art. XI Alt. A/B**: Insolvenz-Schutzregime; Unterschiede je nach Ratifikationserklärung.
- **ZPO §§ 916-934**: Arrestrecht; Arrestanspruch und Arrestgrund.
- **Montreal Convention Art. 35**: Verjährungsfrist 2 Jahre für Frachtansprüche.
- **Chicago Convention Art. 79**: Zusammenarbeit der Staaten bei Luftfahrt-Streitigkeiten.

## Prüfraster

1. Sind beide Staaten Vertragsstaaten der Cape Town Convention?
2. Ist IDERA korrekt registriert und beim ICAO-Register hinterlegt?
3. Hat der Staat Alternative A oder B erklärt?
4. Besteht Arrestgrund (Fluchtverdacht Veräußerungsabsicht Zahlungsunfähigkeit)?
5. Rangverhältnis der Gläubiger im ICAO-Register?
6. Ist Insolvenzverfahren eröffnet (lex fori concursus)?

## Typische Fallstricke

- IDERA nicht hinterlegt; Entregistrierungsweg entfällt.
- Staat des Flugzeugstandorts hat Cape Town nicht ratifiziert; rein nationales Recht gilt.
- Alternative-B-Staat: kein automatischer Herausgabeanspruch in Insolvenz.
- Parallel laufende nationale Arreste konkurrieren; Prioritätsreihenfolge unklar.

## Quellen

- Cape Town Convention/Aircraft Protocol: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- ICAO Internationales Register: https://www.internationalregistry.aero
- LuftFzgG: https://www.gesetze-im-internet.de/luftfzgg/
- ZPO: https://www.gesetze-im-internet.de/zpo/

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftrecht ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Einschlägige Normen vor Mandatsbearbeitung vollständig auf aktuelle Fassung prüfen.
- Behördenanschreiben stets mit Aktenzeichen und Fristbenennung versehen.
- Klagefristen und Widerspruchsfristen sofort bei Mandatsannahme kalendarisch sichern.
- Bei grenzüberschreitenden Sachverhalten internationalen Normenkonflikt prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Luftrecht sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

---

## Skill: `airline-dashboard-bauen`

_Kanzlei oder Mandant braucht operatives Airline-Dashboard für laufendes Mandat: Genehmigungsstatus Flotte Slots Sicherheitsauflagen Insolvenzrisiko. Skill strukturiert Datenquellen LBA EU-VO 1008/2008 Art. 9 Fluko ICAO-Register und liefert befuellbares Dashboard-Template mit Aktualisierungs-Check..._

# Airline – Dashboard bauen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: LuftVG; LuftSiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Kanzlei betreut Airline dauerhaft und braucht strukturiertes internes Dashboard für Mandatsstatus Fristen und Risiken.
- Insolvenzverwalter übernimmt Airline; braucht sofort strukturierten Überblick über alle relevanten Daten.
- Investor führt Due Diligence durch; Dashboard als Instrument für strukturierte Datenzusammenführung.

## Erste Schritte

1. Sachverhalt präzise strukturieren: Parteien Flugzeuge Behörden Fristen.
2. Einschlägige Normen identifizieren: LuftVG EU-VO 1008/2008 Cape Town Convention InsO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Register.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. Gericht vs. EASA.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Ergebnis dokumentieren: Vermerk mit Ampel-Rating und nächsten Schritten.

## Rechtsrahmen

- **EU-VO 1008/2008 Art. 9**: Laufende Überwachung Betriebsgenehmigung.
- **LuftVG §§ 29-31**: Zuständigkeit LBA und Landesluftfahrtbehörden.
- **LuftFzgG §§ 1-28**: Luftfahrzeugpfandrecht und Vollstreckung.
- **Cape Town Convention Art. 2-10**: Internationale Sicherungsinteressen.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht und Gläubigerrechte.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung und Sicherheitsprogramme.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftVG § 21a**: Wet-Lease-Genehmigung; Voraussetzungen und Befristung.
- **LuftVG § 29d**: Aufsichtsbefugnisse des LBA gegenüber Luftverkehrsunternehmen.
- **EASA Part-OPS ORO.AOC.100**: AOC-Anforderungen; Nachweis technischer und betrieblicher Kompetenz.

## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind Register vollständig abgefragt (LBA AG Braunschweig ICAO)?
3. Laufen Fristen; sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet und dokumentiert?
6. Sind Sicherheitsauflagen bewertet und Widerspruch geprüft?
7. Ist das AOC noch gültig und entspricht es dem aktuellen Streckennetz?
8. Haben sich Eigentümerstruktur oder Hauptsitz geändert (EU-VO 1008/2008 Art. 4)?

## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne Prüfung.
- Wet-Lease ohne gesonderte Genehmigung nach LuftVG § 21a operiert; rückwirkende Sanktion möglich.
- AOC und Betriebsgenehmigung als identisch behandelt; sind rechtlich getrennte Instrumente.

## Vertiefung Dashboard-Struktur

Ein effektives Luftrecht-Dashboard für laufende Mandate umfasst:

- **Fristenmonitor**: Alle laufenden Widerspruchs- Klage- und Registrierungsfristen mit Ampelstatus; automatische Erinnerung 14 Tage vor Ablauf.
- **Behördenstatus**: Aktueller Stand aller laufenden Verfahren (LBA EASA Fluko VG); letzte Aktualisierung sichtbar.
- **Registerstatus**: Luftfahrzeugrolle AG Braunschweig Cape Town; Abfragedatum und Befund.
- **Insolvenz-Frühwarnung**: Finanzkennzahlen der beteiligten Airline; Ratingänderungen; Pressemeldungen.
- **Dokumentenablage**: Bescheide Verträge Gutachten Registerauszüge versioniert und durchsuchbar.

## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Dashboard wöchentlich aktualisieren; veraltete Einträge sind gefährlicher als kein Dashboard.
- Zugriffsrechte klar regeln; Mandantendaten nach DSGVO schützen.
- Automatische Fristen-Erinnerungen per E-Mail aktivieren.
- Dashboard-Vorlage nach Mandantentyp (Airline Flughafen Leasinggeber) anpassen.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

---

## Skill: `airline-finanzielle-leistungsfaehigkei`

_LBA prueft finanzielle Leistungsfaehigkeit nach EU-VO 1008/2008 Art. 5 oder Mandant bewertet Insolvenzrisiko einer Fluggesellschaft. Prueft Nachweispflichten Eigenkapital Versicherung Businessplan LBA-Auflagenpraxis und Fruehwarnindikatoren und liefert Leistungsfaehigkeits-Bewertungs-Vermerk im L..._

# Airline – Finanzielle Leistungsfähigkeit prüfen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: LuftVG; LuftSiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Startup-Airline beantragt Betriebsgenehmigung; LBA fordert Nachweis finanzieller Leistungsfähigkeit nach EU-VO 1008/2008 Art. 5; Mandant fragt welche Unterlagen ausreichen.
- Bestehende Airline erhält LBA-Schreiben über Zweifel an fortlaufender Leistungsfähigkeit nach Art. 9; Mandant hat einen Monat zur Stellungnahme.
- Investor prüft Beteiligung an einer Regionalairline; Due-Diligence-Check der Betriebsgenehmigung und Liquiditätslage.

## Erste Schritte

1. Genehmigungstyp bestimmen: Neugenehmigung (Art. 5) oder laufende Überwachung (Art. 9).
2. Nachweisunterlagen zusammenstellen: Jahresabschluss (geprüft) Eigenkapitalnachweis Versicherungspolice Businessplan inkl. Liquiditätsplanung für mindestens 3 Monate.
3. Mindestkapital prüfen: Art. 5 Abs. 2 gibt Richtwerte; LBA kann höhere Anforderungen stellen je nach Flottengröße und Streckennetz.
4. LBA-Prüfstruktur verstehen: Trigger für Überprüfung sind Verluste Kapitalherabsetzung Lohnrückstände Steuerschulden.
5. Gegenmaßnahmen bei LBA-Zweifeln: sofortige schriftliche Stellungnahme aktualisierter Businessplan Bankbestätigung über Kreditlinie.
6. Insolvenzfrühwarnung dokumentieren: Z-Score-Analyse oder Creditreform-Bericht beifügen.

## Rechtsrahmen

- **EU-VO 1008/2008 Art. 5**: Finanzielle Leistungsfähigkeit als Genehmigungsvoraussetzung.
- **EU-VO 1008/2008 Art. 9**: Laufende Überwachung; LBA kann Genehmigung aussetzen oder widerrufen.
- **EU-VO 1008/2008 Art. 9 Abs. 1**: Mitteilungspflicht der Airline bei finanziellen Schwierigkeiten.
- **LuftVG § 20 Abs. 1**: Betriebsgenehmigung als nationale Umsetzungsnorm.
- **InsO §§ 15a 17-18**: Insolvenzantragspflicht; Zahlungsunfähigkeit und drohende Zahlungsunfähigkeit.
- **LuftBO § 9**: Haftpflichtversicherungspflicht; Mindestdeckungssummen.
- **LuftVG § 21a**: Wet-Lease-Genehmigung; Voraussetzungen und Befristung.
- **LuftVG § 29d**: Aufsichtsbefugnisse des LBA gegenüber Luftverkehrsunternehmen.
- **EASA Part-OPS ORO.AOC.100**: AOC-Anforderungen; Nachweis technischer und betrieblicher Kompetenz.

## Prüfraster

1. Erfüllt Jahresabschluss die LBA-Mindestanforderungen (geprüft aktuell)?
2. Ist Eigenkapital ausreichend gemäß Art. 5 Abs. 2?
3. Besteht Haftpflichtversicherung in vorgeschriebener Höhe?
4. Gibt es Steuerschulden Lohnrückstände oder offene Sozialversicherungsbeiträge?
5. Ist Mitteilungspflicht nach Art. 9 Abs. 1 ausgelöst?
6. Sind Frühwarnindikatoren (negativer Cashflow Kreditkündigung) dokumentiert?
7. Ist das AOC noch gültig und entspricht es dem aktuellen Streckennetz?
8. Haben sich Eigentümerstruktur oder Hauptsitz geändert (EU-VO 1008/2008 Art. 4)?

## Typische Fallstricke

- Ungeprüfter Jahresabschluss reicht nicht; LBA besteht auf Wirtschaftsprüfer-Testat.
- Eigenkapital-Mindestbetrag als Einmalnachweis missverstanden; LBA überwacht fortlaufend.
- Mitteilungspflicht nach Art. 9 Abs. 1 übersehen; LBA legt Untätigkeit als Verschleierung aus.
- Businessplan zu optimistisch; LBA lehnt ab und Mandant muss nachlegen.
- Wet-Lease ohne gesonderte Genehmigung nach LuftVG § 21a operiert; rückwirkende Sanktion möglich.
- AOC und Betriebsgenehmigung als identisch behandelt; sind rechtlich getrennte Instrumente.

## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LBA Betriebsgenehmigung: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Einschlägige Normen vor Mandatsbearbeitung vollständig auf aktuelle Fassung prüfen.
- Behördenanschreiben stets mit Aktenzeichen und Fristbenennung versehen.
- Klagefristen und Widerspruchsfristen sofort bei Mandatsannahme kalendarisch sichern.
- Bei grenzüberschreitenden Sachverhalten internationalen Normenkonflikt prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

---

## Skill: `airline-genehmigung-pruefen`

_Airline-Genehmigungsstand ist unklar: Betriebsgenehmigung AOC Streckengenehmigung oder Sonderflugerlaubnis fehlt oder laeuft ab. Prueft EU-VO 1008/2008 LuftVG § 20 EASA EU-VO 965/2012 Part-OPS und Bilateralabkommen und liefert Genehmigungsstatus-Vermerk mit Handlungsbedarf und Fristen im Luftrech..._

# Airline – Genehmigung prüfen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: LuftVG; LuftSiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Airline-Geschäftsführer fragt vor Saisonstart ob alle Genehmigungen vorliegen und keine abgelaufen sind.
- Neue Streckeneröffnung nach Nordamerika; Frage ob bestehende Betriebsgenehmigung abdeckt oder Bilateralabkommen nötig.
- Betriebsgenehmigung erlischt durch Nichterfüllung von Auflagen; was ist zu tun?

## Erste Schritte

1. Sachverhalt präzise strukturieren: Parteien Flugzeuge Behörden Fristen.
2. Einschlägige Normen identifizieren: LuftVG EU-VO 1008/2008 Cape Town Convention InsO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Register.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. Gericht vs. EASA.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Ergebnis dokumentieren: Vermerk mit Ampel-Rating und nächsten Schritten.

## Rechtsrahmen

- **EU-VO 1008/2008 Art. 9**: Laufende Überwachung Betriebsgenehmigung.
- **LuftVG §§ 29-31**: Zuständigkeit LBA und Landesluftfahrtbehörden.
- **LuftFzgG §§ 1-28**: Luftfahrzeugpfandrecht und Vollstreckung.
- **Cape Town Convention Art. 2-10**: Internationale Sicherungsinteressen.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht und Gläubigerrechte.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung und Sicherheitsprogramme.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftVG § 21a**: Wet-Lease-Genehmigung; Voraussetzungen und Befristung.
- **LuftVG § 29d**: Aufsichtsbefugnisse des LBA gegenüber Luftverkehrsunternehmen.
- **EASA Part-OPS ORO.AOC.100**: AOC-Anforderungen; Nachweis technischer und betrieblicher Kompetenz.

## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind Register vollständig abgefragt (LBA AG Braunschweig ICAO)?
3. Laufen Fristen; sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet und dokumentiert?
6. Sind Sicherheitsauflagen bewertet und Widerspruch geprüft?
7. Ist das AOC noch gültig und entspricht es dem aktuellen Streckennetz?
8. Haben sich Eigentümerstruktur oder Hauptsitz geändert (EU-VO 1008/2008 Art. 4)?

## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne Prüfung.
- Wet-Lease ohne gesonderte Genehmigung nach LuftVG § 21a operiert; rückwirkende Sanktion möglich.
- AOC und Betriebsgenehmigung als identisch behandelt; sind rechtlich getrennte Instrumente.

## Vertiefung Genehmigungsrecht

Das luftrechtliche Genehmigungsrecht ist mehrschichtig:

- **Betriebsgenehmigung (EU-VO 1008/2008)**: Konstitutiv für Linienverkehr; Entzug führt zu sofortigem Betriebsverbot.
- **AOC (Air Operator Certificate)**: Technische und betriebliche Voraussetzung; EASA-Zuständigkeit; Nebenbestimmungen beachten.
- **Einzelgenehmigungen**: Nichtplanmäßige Flüge Überflüge fremden Staatsgebiets Sonderlasten erfordern gesonderte Genehmigung.
- **Genehmigungsversagung**: Anfechtungsklage vor VG; aufschiebende Wirkung nach § 80 VwGO als Sofortmaßnahme beantragen.

## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Genehmigungsversagung immer mit Widerspruch und parallelem Eilantrag anfechten.
- Nebenbestimmungen in Genehmigungen sorgfältig lesen; Auflagen können teurer sein als Versagung.
- Genehmigungsvoraussetzungen laufend überwachen; nachträgliche Änderungen melden.
- EU-Recht hat Vorrang; europarechtswidrige Auflagen können gerügt werden.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

---

## Skill: `airline-insolvenzrisiko-markieren`

_Mandant will Insolvenzrisiko einer Airline fruehzeitig erkennen: sinkende Liquiditaet schlechte Ratings Zahlungsrueckstaende. Prueft EU-VO 1008/2008 Art. 9 Fruehwarnindikatoren InsO §§ 15a 17-19 Antragspflicht und Haftungsrisiken Geschaeftsfuehrer und liefert Risikoampel-Bewertung und Geschaeftsf..._

# Airline – Insolvenzrisiko markieren

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: LuftVG; LuftSiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Leasinggeber beobachtet dass Airline Leasingraten verzögert zahlt und Medien über Liquiditätsprobleme berichten; möchte Risikobewertung.
- Airline-Geschäftsführer fragt ab wann Insolvenzantragspflicht entsteht und wie er persönliche Haftung vermeidet.
- Gläubiger-Ausschuss prüft rückwirkend ob Geschäftsführer zu spät Insolvenz angemeldet hat.

## Erste Schritte

1. Sachverhalt präzise strukturieren: Parteien Flugzeuge Behörden Fristen.
2. Einschlägige Normen identifizieren: LuftVG EU-VO 1008/2008 Cape Town Convention InsO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Register.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. Gericht vs. EASA.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Ergebnis dokumentieren: Vermerk mit Ampel-Rating und nächsten Schritten.

## Rechtsrahmen

- **EU-VO 1008/2008 Art. 9**: Laufende Überwachung Betriebsgenehmigung.
- **LuftVG §§ 29-31**: Zuständigkeit LBA und Landesluftfahrtbehörden.
- **LuftFzgG §§ 1-28**: Luftfahrzeugpfandrecht und Vollstreckung.
- **Cape Town Convention Art. 2-10**: Internationale Sicherungsinteressen.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht und Gläubigerrechte.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung und Sicherheitsprogramme.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftVG § 21a**: Wet-Lease-Genehmigung; Voraussetzungen und Befristung.
- **LuftVG § 29d**: Aufsichtsbefugnisse des LBA gegenüber Luftverkehrsunternehmen.
- **EASA Part-OPS ORO.AOC.100**: AOC-Anforderungen; Nachweis technischer und betrieblicher Kompetenz.

## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind Register vollständig abgefragt (LBA AG Braunschweig ICAO)?
3. Laufen Fristen; sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet und dokumentiert?
6. Sind Sicherheitsauflagen bewertet und Widerspruch geprüft?
7. Ist das AOC noch gültig und entspricht es dem aktuellen Streckennetz?
8. Haben sich Eigentümerstruktur oder Hauptsitz geändert (EU-VO 1008/2008 Art. 4)?

## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne Prüfung.
- Wet-Lease ohne gesonderte Genehmigung nach LuftVG § 21a operiert; rückwirkende Sanktion möglich.
- AOC und Betriebsgenehmigung als identisch behandelt; sind rechtlich getrennte Instrumente.

## Vertiefung Insolvenzrecht Luftfahrt

Airline-Insolvenzen erfordern schnelles Handeln:

- **InsO § 15a**: Antragspflicht innerhalb von 3 Wochen nach Eintritt der Zahlungsunfähigkeit; persönliche Haftung des Geschäftsführers.
- **EU-VO 1008/2008 Art. 9**: LBA muss Betriebsgenehmigung widerrufen wenn finanzielle Leistungsfähigkeit nicht mehr gewährleistet; Restrukturierungsplan als Aufschiebungsmittel.
- **InsO § 47**: Aussonderungsrecht des Eigentümers (Leasinggeber); Priorität gegenüber Insolvenzgläubigern.
- **IATA/IOSA**: Kreditversicherung und IATA-Abrechnung (BSP) können bei Insolvenz besondere Regelungen auslösen.

## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Insolvenzfrühzeichen bei Airline-Mandanten laufend beobachten; Bilanzkennzahlen IATA-Rating.
- Antragspflicht nach InsO § 15a läuft ab Kenntnis von Zahlungsunfähigkeit; keine Verzögerung.
- Aussonderungsrechte des Leasinggebers sofort nach Insolvenzantrag anmelden.
- EU-VO 1008/2008 Art. 9: LBA hat eigene Pflicht zur Überwachung; kooperieren.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

---

## Skill: `airline-local-dashboard-bauen`

_Deutsches Kanzleiteam muss auslaendischen Anwalt für Airline-Mandat briefen: Arrest Insolvenz Cape-Town oder Betriebsgenehmigung. Skill erstellt strukturiertes englisches Briefing-Memo mit Sachverhalt deutschem Rechtsrahmen Cape-Town-Status IDERA und konkreten Fragen an Local Counsel im Luftrecht..._

# Airline – Local Counsel briefen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: LuftVG; LuftSiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Deutsche Kanzlei soll Arrest auf Flugzeug einer deutschen Airline in Dubai beantragen; lokaler Anwalt braucht Briefing zu deutschem Pfandrecht und Cape-Town-Status.
- Irischer Leasinggeber gibt deutschem Anwalt Auftrag Local Counsel zu briefen für Herausgabeklage gegen insolvente Airline.
- Insolvenzverwalter beauftragt Kanzlei in London zur Rückholung von Flugzeugen; Briefing zu deutschem Insolvenzrecht und Cape Town nötig.

## Erste Schritte

1. Sachverhalt präzise strukturieren: Parteien Flugzeuge Behörden Fristen.
2. Einschlägige Normen identifizieren: LuftVG EU-VO 1008/2008 Cape Town Convention InsO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Register.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. Gericht vs. EASA.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Ergebnis dokumentieren: Vermerk mit Ampel-Rating und nächsten Schritten.

## Rechtsrahmen

- **EU-VO 1008/2008 Art. 9**: Laufende Überwachung Betriebsgenehmigung.
- **LuftVG §§ 29-31**: Zuständigkeit LBA und Landesluftfahrtbehörden.
- **LuftFzgG §§ 1-28**: Luftfahrzeugpfandrecht und Vollstreckung.
- **Cape Town Convention Art. 2-10**: Internationale Sicherungsinteressen.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht und Gläubigerrechte.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung und Sicherheitsprogramme.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftVG § 21a**: Wet-Lease-Genehmigung; Voraussetzungen und Befristung.
- **LuftVG § 29d**: Aufsichtsbefugnisse des LBA gegenüber Luftverkehrsunternehmen.
- **EASA Part-OPS ORO.AOC.100**: AOC-Anforderungen; Nachweis technischer und betrieblicher Kompetenz.

## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind Register vollständig abgefragt (LBA AG Braunschweig ICAO)?
3. Laufen Fristen; sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet und dokumentiert?
6. Sind Sicherheitsauflagen bewertet und Widerspruch geprüft?
7. Ist das AOC noch gültig und entspricht es dem aktuellen Streckennetz?
8. Haben sich Eigentümerstruktur oder Hauptsitz geändert (EU-VO 1008/2008 Art. 4)?

## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne Prüfung.
- Wet-Lease ohne gesonderte Genehmigung nach LuftVG § 21a operiert; rückwirkende Sanktion möglich.
- AOC und Betriebsgenehmigung als identisch behandelt; sind rechtlich getrennte Instrumente.

## Vertiefung Local-Counsel-Koordination

Bei grenzüberschreitenden Luftrechtsfällen ist die Koordination mit ausländischen Anwälten entscheidend:

- **Informationspaket**: Luftfahrzeugrolle-Auszug Cape-Town-Registerauszug Leasingvertrag AOC-Kopie und Behördenbescheide strukturiert übermitteln.
- **Jurisdiktionsfragen**: Welches Recht gilt für Sicherungsinteresse (Cape Town)? Welches für Betriebsgenehmigung (nationales Recht)? Klare Abgrenzung im Briefing.
- **Fristen synchronisieren**: Unterschiedliche Widerspruchs- und Klagfristen in verschiedenen Rechtsordnungen; gemeinsamen Fristenkalender anlegen.
- **Haftungsfragen**: Local Counsel haftet nach eigenem nationalen Recht; Haftungsfreistellung im Mandat klären.

## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Briefing-Dokument immer auf Englisch und in verständlicher Sprache; kein deutsches Rechtsjargon.
- Zuständigkeit und anwendbares Recht im Briefing klar benennen.
- Honorar- und Haftungsfragen im Vorfeld klären; Engagement-Letter anfordern.
- Regelmäßige Status-Updates vereinbaren; gemeinsamen Fristenkalender führen.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

---

## Skill: `airline-mandantenmemo-schreiben`

_Anwalt schreibt Mandantenmemo für Airline zu komplexem Luftrechtsfall: Genehmigungsrisiko Sicherheitsauflage Slot-Verlust oder Insolvenznaehe. Skill strukturiert Memo nach Sachverhalt Rechtslage Handlungsoptionen Risikobewertung und Empfehlung und liefert fertigen Memo-Baustein mit Nächste-Schrit..._

# Airline – Mandantenmemo schreiben

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: LuftVG; LuftSiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Airline-Vorstand braucht Memo nach LBA-Schreiben zu finanzieller Leistungsfähigkeit; Entscheidungsgrundlage für Vorstandssitzung.
- Airline soll Insolvenz beantragen; Memo an Gesellschafter über Rechtslage Ablauf und Alternativen.
- Audit-Finding Level 1; Memo an Airline-Compliance-Abteilung über sofortigen Handlungsbedarf.

## Erste Schritte

1. Sachverhalt präzise strukturieren: Parteien Flugzeuge Behörden Fristen.
2. Einschlägige Normen identifizieren: LuftVG EU-VO 1008/2008 Cape Town Convention InsO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Register.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. Gericht vs. EASA.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Ergebnis dokumentieren: Vermerk mit Ampel-Rating und nächsten Schritten.

## Rechtsrahmen

- **EU-VO 1008/2008 Art. 9**: Laufende Überwachung Betriebsgenehmigung.
- **LuftVG §§ 29-31**: Zuständigkeit LBA und Landesluftfahrtbehörden.
- **LuftFzgG §§ 1-28**: Luftfahrzeugpfandrecht und Vollstreckung.
- **Cape Town Convention Art. 2-10**: Internationale Sicherungsinteressen.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht und Gläubigerrechte.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung und Sicherheitsprogramme.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftVG § 21a**: Wet-Lease-Genehmigung; Voraussetzungen und Befristung.
- **LuftVG § 29d**: Aufsichtsbefugnisse des LBA gegenüber Luftverkehrsunternehmen.
- **EASA Part-OPS ORO.AOC.100**: AOC-Anforderungen; Nachweis technischer und betrieblicher Kompetenz.

## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind Register vollständig abgefragt (LBA AG Braunschweig ICAO)?
3. Laufen Fristen; sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet und dokumentiert?
6. Sind Sicherheitsauflagen bewertet und Widerspruch geprüft?
7. Ist das AOC noch gültig und entspricht es dem aktuellen Streckennetz?
8. Haben sich Eigentümerstruktur oder Hauptsitz geändert (EU-VO 1008/2008 Art. 4)?

## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne Prüfung.
- Wet-Lease ohne gesonderte Genehmigung nach LuftVG § 21a operiert; rückwirkende Sanktion möglich.
- AOC und Betriebsgenehmigung als identisch behandelt; sind rechtlich getrennte Instrumente.

## Vertiefung Mandantenmemo-Struktur

Ein mandantentaugliches Luftrechtsmemo hat folgende Struktur:

- **Executive Summary** (½ Seite): Sachverhalt in 3 Sätzen; Kernrisiko; empfohlene Sofortmaßnahme.
- **Rechtslage** (1-2 Seiten): Normgrundlage; Behördenpraxis; aktuelle Rechtsprechung; Risikobewertung.
- **Handlungsoptionen**: 2-3 Optionen mit Pro/Contra und Kostenabschätzung; Empfehlung mit Begründung.
- **Zeitplan**: Wichtigste Fristen; geplante Schritte; nächste Entscheidungspunkte.
- **Anlagen**: Relevante Normauszüge; Registerauszüge; Behördenschreiben.

## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Memo immer mit Empfehlung abschließen; Mandant braucht Handlungsanleitung nicht Rechtslehre.
- Risikobewertung mit konkreten Wahrscheinlichkeiten und Schadensszenarien.
- Rechtsprechungsnachweise aus aktuellen BVerwG/BGH-Urteilen; nicht aus Kommentaren allein.
- Executive Summary für Geschäftsführung; technische Details in Anlagen.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

---

## Skill: `airline-pfaendung-planen`

_Glaeubiger plant Zwangsvollstreckung in Airline-Flugzeug oder Airline wehrt Pfaendung ab. Prueft ZPO §§ 864-871 LuftFzgG §§ 22-28 Zwangsversteigerung Arrestantrag ZPO § 917 Cape-Town-Remedies Art. 8 und InsO § 89 Vollstreckungssperre und liefert Pfaendungsplan oder Abwehrstrategie im Luftrecht Fl..._

# Airline – Pfändung planen

## Arbeitsbereich

Glaeubiger plant Zwangsvollstreckung in Airline-Flugzeug oder Airline wehrt Pfaendung ab. Prueft ZPO §§ 864-871 LuftFzgG §§ 22-28 Zwangsversteigerung Arrestantrag ZPO § 917 Cape-Town-Remedies Art. 8 und InsO § 89 Vollstreckungssperre und liefert Pfaendungsplan oder Abwehrstrategie. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: LuftVG; LuftSiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Flugzeugfinanzier hat Pfandrecht und will nach Zahlungsverzug vollstrecken; Flugzeug steht auf Münchner Flughafen.
- Großgläubiger ohne Pfandrecht will Arrest beantragen bevor Airline Flugzeuge ins Ausland verbringt.
- Airline erhält Pfändungs-Beschluss; Mandant will prüfen ob Vollstreckung abgewendet werden kann.

## Erste Schritte

1. Sachverhalt präzise strukturieren: Parteien Flugzeuge Behörden Fristen.
2. Einschlägige Normen identifizieren: LuftVG EU-VO 1008/2008 Cape Town Convention InsO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Register.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. Gericht vs. EASA.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Ergebnis dokumentieren: Vermerk mit Ampel-Rating und nächsten Schritten.

## Rechtsrahmen

- **EU-VO 1008/2008 Art. 9**: Laufende Überwachung Betriebsgenehmigung.
- **LuftVG §§ 29-31**: Zuständigkeit LBA und Landesluftfahrtbehörden.
- **LuftFzgG §§ 1-28**: Luftfahrzeugpfandrecht und Vollstreckung.
- **Cape Town Convention Art. 2-10**: Internationale Sicherungsinteressen.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht und Gläubigerrechte.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung und Sicherheitsprogramme.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftVG § 21a**: Wet-Lease-Genehmigung; Voraussetzungen und Befristung.
- **LuftVG § 29d**: Aufsichtsbefugnisse des LBA gegenüber Luftverkehrsunternehmen.
- **EASA Part-OPS ORO.AOC.100**: AOC-Anforderungen; Nachweis technischer und betrieblicher Kompetenz.

## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind Register vollständig abgefragt (LBA AG Braunschweig ICAO)?
3. Laufen Fristen; sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet und dokumentiert?
6. Sind Sicherheitsauflagen bewertet und Widerspruch geprüft?
7. Ist das AOC noch gültig und entspricht es dem aktuellen Streckennetz?
8. Haben sich Eigentümerstruktur oder Hauptsitz geändert (EU-VO 1008/2008 Art. 4)?

## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne Prüfung.
- Wet-Lease ohne gesonderte Genehmigung nach LuftVG § 21a operiert; rückwirkende Sanktion möglich.
- AOC und Betriebsgenehmigung als identisch behandelt; sind rechtlich getrennte Instrumente.

## Vertiefung Pfändungsrecht

Die Pfändung eines Luftfahrzeugs erfordert besondere Vorbereitung:

- **Standortermittlung**: Aktueller Flugplan (ATC) und Flughafenslotbelegung geben Aufschluss über Standort; Abstimmung mit Flughafenoperator nötig.
- **Arrestantrag**: Zuständiges Gericht am Belegenheitsort; Arrestgrund glaubhaft machen.
- **Betriebsunterbrechung**: Pfändung eines Linienflugzeugs löst Betriebsunterbrechung aus; Schadensersatz bei unberechtigtem Arrest.
- **Cape Town Priorität**: Vor Pfändung ICAO-Register prüfen; vorrangige Sicherungsinteressen können Arrest verhindern.

## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Luftfahrzeug nur pfänden wenn Standort und Verweildauer am Belegenheitsort gesichert.
- Arrestantrag muss Arrestgrund (Eilbedürftigkeit) substantiiert darlegen.
- Betriebsunterbrechung durch Pfändung kann Schadensersatzansprüche auslösen; Abwägung mit Vollstreckungsziel.
- Cape-Town-Register vor Arrestantrag prüfen; vorrangige Berechtigte können Herausgabe verlangen.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

---

## Skill: `airline-pfandrecht-pfaendung-planen`

_Kreditgeber will Pfandrecht an Airline-Flugzeug bestellen oder bestehender Pfandglaeubigerrang soll gesichert werden. Prueft LuftFzgG §§ 1-12 Entstehungsvoraussetzungen Rangordnung Cape-Town-Koordination Notarerfordernis und liefert Pfandrechtsbestellungs-Checkliste und Antragsentwurf AG Braunsch..._

# Airline – Pfandrecht vorbereiten

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: LuftVG; LuftSiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Bank finanziert Flottenerweiterung einer deutschen Regionalairline; will erstrangiges Pfandrecht an 5 neuen Flugzeugen bestellen.
- Zweiter Finanzier will nachrangiges Pfandrecht; Rangfragen mit erstem Finanzier zu klären.
- Flugzeug wird aus Ausland importiert; Pfandrecht im Ursprungsland zu löschen und in Deutschland neu einzutragen.

## Erste Schritte

1. Sachverhalt präzise strukturieren: Parteien Flugzeuge Behörden Fristen.
2. Einschlägige Normen identifizieren: LuftVG EU-VO 1008/2008 Cape Town Convention InsO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Register.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. Gericht vs. EASA.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Ergebnis dokumentieren: Vermerk mit Ampel-Rating und nächsten Schritten.

## Rechtsrahmen

- **EU-VO 1008/2008 Art. 9**: Laufende Überwachung Betriebsgenehmigung.
- **LuftVG §§ 29-31**: Zuständigkeit LBA und Landesluftfahrtbehörden.
- **LuftFzgG §§ 1-28**: Luftfahrzeugpfandrecht und Vollstreckung.
- **Cape Town Convention Art. 2-10**: Internationale Sicherungsinteressen.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht und Gläubigerrechte.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung und Sicherheitsprogramme.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftVG § 21a**: Wet-Lease-Genehmigung; Voraussetzungen und Befristung.
- **LuftVG § 29d**: Aufsichtsbefugnisse des LBA gegenüber Luftverkehrsunternehmen.
- **EASA Part-OPS ORO.AOC.100**: AOC-Anforderungen; Nachweis technischer und betrieblicher Kompetenz.

## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind Register vollständig abgefragt (LBA AG Braunschweig ICAO)?
3. Laufen Fristen; sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet und dokumentiert?
6. Sind Sicherheitsauflagen bewertet und Widerspruch geprüft?
7. Ist das AOC noch gültig und entspricht es dem aktuellen Streckennetz?
8. Haben sich Eigentümerstruktur oder Hauptsitz geändert (EU-VO 1008/2008 Art. 4)?

## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne Prüfung.
- Wet-Lease ohne gesonderte Genehmigung nach LuftVG § 21a operiert; rückwirkende Sanktion möglich.
- AOC und Betriebsgenehmigung als identisch behandelt; sind rechtlich getrennte Instrumente.

## Vertiefung Pfandrechtsrecht

Das Luftfahrzeugpfandrecht verbindet nationales Sachenrecht mit dem internationalen Cape-Town-System:

- **Rangkonflikt**: Nationales Pfandrecht (LuftFzgG) und Cape-Town-Sicherungsinteresse können konkurrieren; Priorität richtet sich nach Eintragungsdatum im jeweiligen Register.
- **Vollstreckung**: Pfandrechtsverwertung erfolgt durch öffentliche Versteigerung; ZPO § 864 regelt den besonderen Vollstreckungsweg für Luftfahrzeuge.
- **Internationaler Arrest**: Luftfahrzeug kann im Ausland nach nationalen Regeln oder Cape-Town-Mechanismus arretiert werden; Koordination mit Local Counsel erforderlich.

## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Rangkonflikt zwischen nationalem Pfandrecht und Cape-Town-Sicherungsinteresse muss vor Vertragsschluss geklärt werden.
- Pfandrechtslöschung nach Tilgung der gesicherten Forderung unverzüglich veranlassen.
- Bei Pfandrecht auf Triebwerke (als Zubehör) gesonderte Eintragung prüfen.
- Internationale Kreditgeber verlangen regelmäßig Cape-Town-Eintragung als Bedingung.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

---

## Skill: `airline-register-auswerten`

_Mandant will Luftfahrzeugrolle Pfandrechtsregister und Cape-Town-Register einer Airline auswerten. Skill fuehrt strukturierte Registerabfrage LBA LuftVG § 64 AG Braunschweig LuftFzgG und ICAO-Register durch und liefert Registerauszugs-Auswertungs-Bericht mit Eigentuemerstruktur und Belastungen im..._

# Airline – Register auswerten

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: LuftVG; LuftSiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Finanzierer prüft vor Flugzeugfinanzierung ob auf der gesamten Flotte einer Airline Pfandrechte oder internationale Sicherungsinteressen lasten.
- Rechtsanwalt übernimmt Mandat nach Airline-Insolvenz; braucht vollständige Übersicht Flotte und Belastungen.
- Käufer will Airline erwerben; Due-Diligence verlangt vollständigen Registercheck.

## Erste Schritte

1. Sachverhalt präzise strukturieren: Parteien Flugzeuge Behörden Fristen.
2. Einschlägige Normen identifizieren: LuftVG EU-VO 1008/2008 Cape Town Convention InsO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Register.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. Gericht vs. EASA.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Ergebnis dokumentieren: Vermerk mit Ampel-Rating und nächsten Schritten.

## Rechtsrahmen

- **EU-VO 1008/2008 Art. 9**: Laufende Überwachung Betriebsgenehmigung.
- **LuftVG §§ 29-31**: Zuständigkeit LBA und Landesluftfahrtbehörden.
- **LuftFzgG §§ 1-28**: Luftfahrzeugpfandrecht und Vollstreckung.
- **Cape Town Convention Art. 2-10**: Internationale Sicherungsinteressen.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht und Gläubigerrechte.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung und Sicherheitsprogramme.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftVG § 21a**: Wet-Lease-Genehmigung; Voraussetzungen und Befristung.
- **LuftVG § 29d**: Aufsichtsbefugnisse des LBA gegenüber Luftverkehrsunternehmen.
- **EASA Part-OPS ORO.AOC.100**: AOC-Anforderungen; Nachweis technischer und betrieblicher Kompetenz.

## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind Register vollständig abgefragt (LBA AG Braunschweig ICAO)?
3. Laufen Fristen; sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet und dokumentiert?
6. Sind Sicherheitsauflagen bewertet und Widerspruch geprüft?
7. Ist das AOC noch gültig und entspricht es dem aktuellen Streckennetz?
8. Haben sich Eigentümerstruktur oder Hauptsitz geändert (EU-VO 1008/2008 Art. 4)?

## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne Prüfung.
- Wet-Lease ohne gesonderte Genehmigung nach LuftVG § 21a operiert; rückwirkende Sanktion möglich.
- AOC und Betriebsgenehmigung als identisch behandelt; sind rechtlich getrennte Instrumente.

## Vertiefung Registerrecht

Die Registerauswertung ist Grundlage jeder luftrechtlichen Due-Diligence-Prüfung:

- **Luftfahrzeugrolle (LBA)**: Enthält Halter Eigentümer Kennzeichen und Belastungen; Abruf online beim LBA möglich.
- **AG Braunschweig (Pfandrechtsregister)**: Führt alle eingetragenen Pfandrechte an deutschen Luftfahrzeugen; Rangfolge nach Eintragungsdatum.
- **ICAO International Registry (Cape Town)**: Enthält internationale Sicherungsinteressen; Suche nach Luftfahrzeugkennzeichen und MSN.
- **Registerauszug Aktualität**: Stets aktuellen Auszug anfordern; veraltete Auszüge führen zu Haftungsrisiken.

## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Alle drei Register (LBA-Rolle AG Braunschweig Cape Town) stets parallel abfragen.
- Registerauszüge mit Datum versehen und in Mandantenakte archivieren.
- Änderungen im Register sofort melden; Unterlassung kann Haftung auslösen.
- Bei Kauf oder Leasingübernahme immer Registerhistorie der letzten 10 Jahre prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

---

## Skill: `airline-sicherheitsauflage-bewerten`

_Airline erhaelt LuftSiG oder EASA-Auflage nach Inspektion. Prueft LuftSiG §§ 8-9 Sicherheitsprogramm EU-DVO 2015/1998 Findings-Kategorien Level 1/2/Observation Verhaeltnismaessigkeit und Widerspruchsmoeglichkeit und liefert Auflagen-Bewertungs-Vermerk und Muster-Stellungnahme mit Corrective Actio..._

# Airline – Sicherheitsauflage bewerten

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: LuftVG; LuftSiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- LuftSiG-Inspektionsbericht listet 12 Findings für Airline-Sicherheitsprogramm; Mandant muss innerhalb 30 Tagen antworten.
- EASA-Audit ergibt Level-1-Finding (schwerwiegend); sofortiger Betriebsstopp bis zur Behebung droht.
- Neue EU-DVO-Anforderung tritt in Kraft; Airline braucht Gap-Analysis und Umsetzungsplan.

## Erste Schritte

1. Sachverhalt präzise strukturieren: Parteien Flugzeuge Behörden Fristen.
2. Einschlägige Normen identifizieren: LuftVG EU-VO 1008/2008 Cape Town Convention InsO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Register.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. Gericht vs. EASA.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Ergebnis dokumentieren: Vermerk mit Ampel-Rating und nächsten Schritten.

## Rechtsrahmen

- **EU-VO 1008/2008 Art. 9**: Laufende Überwachung Betriebsgenehmigung.
- **LuftVG §§ 29-31**: Zuständigkeit LBA und Landesluftfahrtbehörden.
- **LuftFzgG §§ 1-28**: Luftfahrzeugpfandrecht und Vollstreckung.
- **Cape Town Convention Art. 2-10**: Internationale Sicherungsinteressen.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht und Gläubigerrechte.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung und Sicherheitsprogramme.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftVG § 21a**: Wet-Lease-Genehmigung; Voraussetzungen und Befristung.
- **LuftVG § 29d**: Aufsichtsbefugnisse des LBA gegenüber Luftverkehrsunternehmen.
- **EASA Part-OPS ORO.AOC.100**: AOC-Anforderungen; Nachweis technischer und betrieblicher Kompetenz.

## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind Register vollständig abgefragt (LBA AG Braunschweig ICAO)?
3. Laufen Fristen; sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet und dokumentiert?
6. Sind Sicherheitsauflagen bewertet und Widerspruch geprüft?
7. Ist das AOC noch gültig und entspricht es dem aktuellen Streckennetz?
8. Haben sich Eigentümerstruktur oder Hauptsitz geändert (EU-VO 1008/2008 Art. 4)?

## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne Prüfung.
- Wet-Lease ohne gesonderte Genehmigung nach LuftVG § 21a operiert; rückwirkende Sanktion möglich.
- AOC und Betriebsgenehmigung als identisch behandelt; sind rechtlich getrennte Instrumente.

## Vertiefung Sicherheitsauflagen

Sicherheitsauflagen im Luftrecht müssen auf Verhältnismäßigkeit und Rechtsgrundlage überprüft werden:

- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung ist standardisierte Sicherheitsauflage; Ablehnungsbescheid ist anfechtbar.
- **EU-VO 300/2008**: Sicherheitsprogramme für Flughafen und Luftverkehrsunternehmen; Abweichung von Standard-Maßnahme bedarf Gleichwertigkeitsnachweis.
- **Verhältnismäßigkeit**: BVerfG-Rechtsprechung zu Grundrechtseingriffen; Einschränkung der Berufsfreiheit (Art. 12 GG) nur durch geeignete erforderliche und angemessene Maßnahme.
- **Eilrechtsschutz**: § 80 Abs. 5 VwGO bei sofortigem Vollzug; Interessenabwägung Sicherheitsinteresse vs. Eingriff.

## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Jede Sicherheitsauflage auf Rechtsgrundlage und Verhältnismäßigkeit prüfen.
- Zuverlässigkeitsüberprüfung nach LuftSiG hat eigenen Verwaltungsrechtsweg; gesondert anfechten.
- Sicherheitsprogramm-Abweichungen rechtzeitig mit Behörde abstimmen.
- Bei EU-Reisenden datenschutzrechtliche Aspekte der Überprüfung beachten (DSGVO).

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

---

## Skill: `airline-zustaendigkeit-pruefen`

_Airline-Mandat: unklar welche Behörde zuständig ist LBA EU-Behörde Landesbehoerde oder auslaendische Luftfahrtbehoerde. Prueft EU-VO 1008/2008 Art. 4 Aufsichtsstaat LuftVG §§ 29-31 EASA und bilaterale Abkommen und liefert Zuständigkeits-Vermerk mit korrektem Antragsadressaten im Luftrecht Flughaf..._

# Airline – Zuständigkeit prüfen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: LuftVG; LuftSiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Airline mit Hauptsitz Hamburg betreibt Verbindung nach Wien; österreichische Behörde beanstandet; Mandant fragt welche Behörde zuständig ist.
- Tochtergesellschaft eines US-Konzerns registriert in Deutschland; Frage ob LBA oder FAA für AOC zuständig.
- Airline möchte Strecke nach Nordafrika eröffnen; Bilateralabkommen Deutschland-Marokko unbekannt.

## Erste Schritte

1. Sachverhalt präzise strukturieren: Parteien Flugzeuge Behörden Fristen.
2. Einschlägige Normen identifizieren: LuftVG EU-VO 1008/2008 Cape Town Convention InsO.
3. Register prüfen: LBA-Luftfahrzeugrolle AG-Braunschweig-Pfandrechtsregister ICAO-Register.
4. Zuständigkeit klären: LBA vs. Landesbehörde vs. Gericht vs. EASA.
5. Fristen sichern: Widerspruch (1 Monat) Klage (1 Monat) Insolvenzantrag (3/6 Wochen).
6. Ergebnis dokumentieren: Vermerk mit Ampel-Rating und nächsten Schritten.

## Rechtsrahmen

- **EU-VO 1008/2008 Art. 9**: Laufende Überwachung Betriebsgenehmigung.
- **LuftVG §§ 29-31**: Zuständigkeit LBA und Landesluftfahrtbehörden.
- **LuftFzgG §§ 1-28**: Luftfahrzeugpfandrecht und Vollstreckung.
- **Cape Town Convention Art. 2-10**: Internationale Sicherungsinteressen.
- **InsO §§ 15a 17-19 47 50**: Insolvenzantragspflicht und Gläubigerrechte.
- **LuftSiG §§ 7-9**: Zuverlässigkeitsüberprüfung und Sicherheitsprogramme.
- **VwGO §§ 68 74 80**: Widerspruch Klage aufschiebende Wirkung.
- **LuftVG § 21a**: Wet-Lease-Genehmigung; Voraussetzungen und Befristung.
- **LuftVG § 29d**: Aufsichtsbefugnisse des LBA gegenüber Luftverkehrsunternehmen.
- **EASA Part-OPS ORO.AOC.100**: AOC-Anforderungen; Nachweis technischer und betrieblicher Kompetenz.

## Prüfraster

1. Ist zuständige Behörde korrekt adressiert?
2. Sind Register vollständig abgefragt (LBA AG Braunschweig ICAO)?
3. Laufen Fristen; sind alle gesichert?
4. Besteht Cape-Town-Registrierung mit IDERA?
5. Ist Insolvenzrisiko bewertet und dokumentiert?
6. Sind Sicherheitsauflagen bewertet und Widerspruch geprüft?
7. Ist das AOC noch gültig und entspricht es dem aktuellen Streckennetz?
8. Haben sich Eigentümerstruktur oder Hauptsitz geändert (EU-VO 1008/2008 Art. 4)?

## Typische Fallstricke

- Falsche Behörde adressiert; Frist läuft unbemerkt ab.
- Cape-Town-Register nicht abgefragt; internationale Belastungen unerkannt.
- Insolvenzfrühzeichen ignoriert; Antragspflicht ausgelöst ohne Reaktion.
- Sicherheitsauflage als verhältnismäßig hingenommen ohne Prüfung.
- Wet-Lease ohne gesonderte Genehmigung nach LuftVG § 21a operiert; rückwirkende Sanktion möglich.
- AOC und Betriebsgenehmigung als identisch behandelt; sind rechtlich getrennte Instrumente.

## Vertiefung Zuständigkeit

Die Zuständigkeitsfrage ist bei luftrechtlichen Mandaten häufig das erste Hindernis. Folgende Abgrenzungen sind besonders fehlerträchtig:

- **LBA vs. Landesluftfahrtbehörde**: Das LBA ist für bundesrechtliche Aufgaben zuständig (Betriebsgenehmigung AOC Register); Landesbehörden überwachen den regionalen Luftverkehr und Kleinflugplätze.
- **EASA vs. nationale Behörde**: Seit Inkrafttreten der EASA-Basisverordnung (VO 2018/1139) hat EASA Direktzuständigkeit für Zulassungen von Luftfahrzeugen und Organisationen; das LBA bleibt für betriebliche Zulassungen zuständig.
- **Verwaltungsgericht vs. Zivilgericht**: Bescheide einer Luftfahrtbehörde sind vor dem VG anzufechten; privatrechtliche Ansprüche (Leasingstreit Schaden) gehören vor die Zivilgerichte.

## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- Cape Town Convention: https://www.unidroit.org/instruments/security-interests/aircraft-protocol/
- InsO: https://www.gesetze-im-internet.de/inso/
- EASA: https://www.easa.europa.eu/en/document-library/regulations
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Zuständigkeitsirrtümer sind die häufigste Fehlerquelle in luftrechtlichen Mandaten; immer zuerst klären.
- Sowohl LBA als auch Landesbehörde können Bescheide erlassen; Abgrenzung nach Sachmaterie.
- Bei europäischen Sachverhalten immer prüfen ob EASA-Direktzuständigkeit besteht (VO 2018/1139).
- Zeitpunkt der Behördenentscheidung dokumentieren; Fristbeginn ab Zustellung des Bescheids.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

---

## Skill: `betriebsgenehmigung-airline`

_Airline beantragt Betriebsgenehmigung beim LBA oder bestehende Genehmigung soll geaendert oder widerrufen werden. Prueft EU-VO 1008/2008 Art. 3-9 Genehmigungsvoraussetzungen AOC Hauptniederlassung EU-Eigentumskontrolle und liefert Antragsunterlagen-Checkliste und Widerrufsabwehr-Baustein im Luftr..._

# Betriebsgenehmigung Airline – Antrag, Änderung und Widerruf

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: LuftVG; LuftSiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Neugründung einer deutschen Charterflugesellschaft; Gesellschafter fragen was für die Betriebsgenehmigung beim LBA benötigt wird und wie lange das Verfahren dauert.
- Bestehende Airline möchte Streckennetz erweitern; LBA prüft ob bestehende Genehmigung gilt oder Änderungsantrag nötig.
- LBA leitet Widerrufsverfahren ein nach Meldung über Zahlungsschwierigkeiten; Airline hat 6 Wochen zur Stellungnahme.

## Erste Schritte

1. Betriebsgenehmigungspflicht prüfen: EU-VO 1008/2008 Art. 3 gilt für alle gewerblichen Luftverkehrsunternehmen mit Hauptniederlassung in EU.
2. Genehmigungsvoraussetzungen prüfen: Hauptniederlassung in Deutschland (Art. 4 Abs. 1 lit. b) AOC EU-Eigentumskontrolle (Art. 4 Abs. 1 lit. f) finanzielle Leistungsfähigkeit (Art. 5) guter Leumund (Art. 7).
3. Antragsunterlagen zusammenstellen: Gesellschaftsvertrag Gesellschafterliste AOC Businessplan Versicherungsnachweis Eigenkapitalnachweis.
4. LBA-Antrag einreichen: Bearbeitungszeit typisch 3-6 Monate; enge Koordination mit AOC-Verfahren.
5. Auflagen überwachen: Genehmigung kann mit Auflagen verbunden sein.
6. Widerrufsabwehr: sofortige Stellungnahme bei Art.-9-Schreiben; Sanierungsplan und Bankbürgschaft anbieten.

## Rechtsrahmen

- **EU-VO 1008/2008 Art. 3**: Pflicht zur Betriebsgenehmigung für EU-Luftfahrtunternehmen.
- **EU-VO 1008/2008 Art. 4**: Genehmigungsvoraussetzungen; Hauptniederlassung EU-Eigentum guter Leumund.
- **EU-VO 1008/2008 Art. 5**: Finanzielle Leistungsfähigkeit.
- **EU-VO 1008/2008 Art. 7**: Anforderungen an Zuverlässigkeit.
- **EU-VO 1008/2008 Art. 9**: Laufende Überwachung und Widerruf.
- **LuftVG § 20**: Nationale Umsetzung der Betriebsgenehmigungspflicht.
- **VwVfG §§ 48-49**: Rücknahme und Widerruf von Verwaltungsakten.
- **LuftVG § 21a**: Wet-Lease-Genehmigung; Voraussetzungen und Befristung.
- **LuftVG § 29d**: Aufsichtsbefugnisse des LBA gegenüber Luftverkehrsunternehmen.
- **EASA Part-OPS ORO.AOC.100**: AOC-Anforderungen; Nachweis technischer und betrieblicher Kompetenz.

## Prüfraster

1. Besteht Hauptniederlassung in Deutschland?
2. Liegt AOC vor oder wird parallel beantragt?
3. Erfüllt EU-Eigentümerkontrolle (mindestens 50 % EU-Eigentümer)?
4. Sind finanzielle Leistungsfähigkeit und Versicherung nachgewiesen?
5. Haben Geschäftsführer guten Leumund?
6. Wurden Auflagen aus letztem Bescheid erfüllt?
7. Ist das AOC noch gültig und entspricht es dem aktuellen Streckennetz?
8. Haben sich Eigentümerstruktur oder Hauptsitz geändert (EU-VO 1008/2008 Art. 4)?

## Typische Fallstricke

- AOC-Antrag nicht koordiniert mit Betriebsgenehmigungsantrag; LBA wartet auf AOC.
- EU-Eigentümerkontrolle nicht erfüllt: Mehrheitseigner aus Drittland; Genehmigung scheitert.
- Businessplan unvollständig; LBA verlangt Nachbesserung.
- Widerruf trotz laufender Sanierung; kein Eilantrag § 80 VwGO gestellt.
- Wet-Lease ohne gesonderte Genehmigung nach LuftVG § 21a operiert; rückwirkende Sanktion möglich.
- AOC und Betriebsgenehmigung als identisch behandelt; sind rechtlich getrennte Instrumente.

## Vertiefung Genehmigungsrecht

Das luftrechtliche Genehmigungsrecht ist mehrschichtig:

- **Betriebsgenehmigung (EU-VO 1008/2008)**: Konstitutiv für Linienverkehr; Entzug führt zu sofortigem Betriebsverbot.
- **AOC (Air Operator Certificate)**: Technische und betriebliche Voraussetzung; EASA-Zuständigkeit; Nebenbestimmungen beachten.
- **Einzelgenehmigungen**: Nichtplanmäßige Flüge Überflüge fremden Staatsgebiets Sonderlasten erfordern gesonderte Genehmigung.
- **Genehmigungsversagung**: Anfechtungsklage vor VG; aufschiebende Wirkung nach § 80 VwGO als Sofortmaßnahme beantragen.

## Quellen

- EU-VO 1008/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R1008
- LBA: https://www.lba.de/DE/Luftfahrtunternehmen/Genehmigungen/GenehmigungLU.html
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- VwVfG: https://www.gesetze-im-internet.de/vwvfg/
- EASA: https://www.easa.europa.eu/en/document-library/regulations

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Airline-Betrieb und Betriebsgenehmigung ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Genehmigungsversagung immer mit Widerspruch und parallelem Eilantrag anfechten.
- Nebenbestimmungen in Genehmigungen sorgfältig lesen; Auflagen können teurer sein als Versagung.
- Genehmigungsvoraussetzungen laufend überwachen; nachträgliche Änderungen melden.
- EU-Recht hat Vorrang; europarechtswidrige Auflagen können gerügt werden.

### Dokumentationspflichten

Für Mandate im Bereich Airline-Betrieb und Betriebsgenehmigung sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

---

## Skill: `drohnen-uas-betrieb`

_Drohnenbetreiber braucht Betriebsgenehmigung oder Mandant ist nach Drohnenflug-Unfall in Haftungsfragen verwickelt. Prueft EU-VO 2019/947 Betriebskategorien Open/Specific/Certified LuftVG § 21a Registrierungspflicht LBA Versicherungspflicht EU-VO 785/2004 und liefert Genehmigungs-Checkliste und H..._

# Drohnen und UAS-Betrieb – Genehmigung, Registrierung und Haftung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: LuftVG; LuftSiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Filmproduktionsfirma will kommerziellen Drohnenflug über Menschenansammlung durchführen; fragt nach notwendiger Genehmigung und Versicherung.
- Landwirt setzt Drohnen zur Feldbesprühung ein; LBA hat Betrieb ohne EASA-Zertifizierung beanstandet.
- Drohne kollidiert mit Kleinhubschrauber; Versicherung und Haftungsfragen stehen im Raum.

## Erste Schritte

1. Betriebskategorie bestimmen: Open (max. 25 kg keine Genehmigung Unterklassen A1/A2/A3) Specific (Risikoanalyse LBA-Genehmigung) oder Certified (Zulassungspflicht wie Flugzeug).
2. Registrierungspflicht prüfen: LBA-Registrierung für Drohnen ab 250 g Abfluggewicht oder mit Kamera.
3. Flugverbotszonen prüfen: Lufträume um Flughäfen Naturschutzgebiete Bahnanlagen.
4. EASA-Kompetenznachweis: Open-Kategorie A2 erfordert Online-Training; Specific braucht Operational Authorisation oder STS.
5. Versicherungspflicht: EU-VO 785/2004 gilt auch für unbemannte Luftfahrzeuge ab 20 kg.
6. Haftung bei Unfall: Halter-Haftung nach LuftVG § 33 (Gefährdungshaftung).

## Rechtsrahmen

- **EU-VO 2019/947 Art. 4-6**: Betriebskategorien Open/Specific/Certified.
- **EU-VO 2019/947 Art. 14**: Registrierungspflicht; LBA zuständig.
- **Delegierte VO EU 2019/945**: Technische Anforderungen an UAS-Klassen C0-C6.
- **LuftVG § 21a**: UAS-Betrieb im deutschen Luftraum.
- **LuftVG § 33**: Gefährdungshaftung des Luftfahrzeughalters; gilt auch für UAS.
- **EU-VO 785/2004**: Versicherungspflicht für Luftfahrzeuge; Mindestdeckungssummen.
- **BNatSchG § 44**: Naturschutz-Flugverbote.
- **LuftVG § 21e**: Nationales UAS-Register; Registrierungspflicht ab 250 g.
- **LuftVO § 21b**: Betriebsverbote und Beschränkungszonen; Kontrollluftraum.
- **EASA Easy Access Rules for UAS**: Konsolidierte Fassung aller UAS-Verordnungen.

## Prüfraster

1. In welche Betriebskategorie fällt der geplante Einsatz?
2. Ist Drohne korrekt beim LBA registriert?
3. Liegt EASA-Kompetenznachweis des Piloten vor?
4. Sind alle Flugverbotszonen geprüft?
5. Besteht ausreichende Haftpflichtversicherung?
6. Wurde LBA-Betriebsgenehmigung (Specific) korrekt beantragt?
7. Ist Betriebskategorie (offen/spezifisch/zertifiziert) korrekt eingestuft (EU-VO 2019/947 Art. 5)?
8. Liegt für spezifische Kategorie ein genehmigter SORA-Risikoplan vor?

## Typische Fallstricke

- Open-Kategorie angenommen obwohl kommerzieller Flug über Menschen Specific erfordert.
- Registrierungspflicht vergessen; Drohne ohne Registrierung ist Ordnungswidrigkeit.
- Versicherung nur für Personenschäden nicht für Sachschäden am Drittflugzeug.
- Naturschutzgebiet nicht überprüft; Einsatz illegal.
- Drohne über 250 g nicht im UAS-Register eingetragen; Bußgeld nach LuftVG § 58.
- Betriebszone ohne LBA-Genehmigung überflogen; Strafbarkeit nach § 315a StGB.

## Quellen

- EU-VO 2019/947: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019R0947
- Delegierte VO 2019/945: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019R0945
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- EASA Drohnen: https://www.easa.europa.eu/en/domains/civil-drones-rpas
- LBA UAS: https://www.lba.de/DE/Drohnen/Drohnen_node.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Drohnen und UAS-Betrieb ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Einschlägige Normen vor Mandatsbearbeitung vollständig auf aktuelle Fassung prüfen.
- Behördenanschreiben stets mit Aktenzeichen und Fristbenennung versehen.
- Klagefristen und Widerspruchsfristen sofort bei Mandatsannahme kalendarisch sichern.
- Bei grenzüberschreitenden Sachverhalten internationalen Normenkonflikt prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Drohnen und UAS-Betrieb sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

