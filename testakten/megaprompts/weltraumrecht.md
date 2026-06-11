# Megaprompt: weltraumrecht

> *Achtung: Dies ist ein experimentelles Mega-Prompt-Markdown, das einen kompletten Klotzkette-Plugin in eine einzige Datei zusammenfuehrt. Keine Haftung, keine Gewaehr. Nur zum Ausprobieren der Skills auch ohne Claude Code; keine Rechtsberatung. Vor Verwendung im Mandat anwaltlich pruefen.*
>
> *Caution: This is an experimental Mega-Prompt Markdown that consolidates a full Klotzkette plugin into a single file. No warranty, no liability. For exploration with chat tools that do not run Claude Code only; not legal advice.*

**Verwendung:** Diesen gesamten Text in einen Chat ohne Claude-Code-Integration einfuegen (oder als Datei hochladen). Der Chat-Agent erhaelt damit die gebuendelten Skills dieses Plugins als Kontext. Eine Replikation des vollen Plugin-Verhaltens ist nicht garantiert — der Megaprompt ist eine Best-Effort-Kompression.


## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 102 Skills des Plugins `weltraumrecht`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlaegt …
2. **anti-satellite-test-ban-und-orbital-debris-pledge** — Anti-Satellite-Test-Ban und Orbital-Debris-Pledge: zerstoerende ASAT-Tests Voelkerrechtsbewertung UN-Resolutionslinie un…
3. **lunar-heritage-quantenkommunikation-via** — Lunar Heritage: Schutz historischer Mondlandestellen und ihrer Artefakte. Klaert das US One Small Step to Protect Human …
4. **quantenkommunikation-via-satellit** — Quantenkommunikation via Satellit: Quantum Key Distribution QKD-Missionen und Schluesselverteilung uebersatellitisches B…
5. **space-weather-solarsturm-haftung-und-versicherung** — Space Weather Solarsturm und geomagnetische Ereignisse: rechtliche Bewertung von Satellitenausfall Stromnetzausfall GPS-…
6. **commercial-leo-destinations-iss-nachfolge** — Commercial LEO Destinations: rechtliche Architektur kommerzieller Low-Earth-Orbit-Stationen Axiom Orbital Reef Starlab H…
7. **satellitenschwarm-ueber-deutschland-frequenz-kollision** — Mega-Konstellationen (Starlink, OneWeb, IRIS²) über Deutschland – Frequenzinterferenz, Kollisionswarnung, Datenschutz, L…
8. **mondvertrag-ressourcen** — Moon Agreement 1979 – Gemeinsames Erbe der Menschheit, gescheitertes Ressourcenregime, keine Ratifikation durch Raumfahr…
9. **satellitenbetrieb-deutschland** — Genehmigungsverfahren für Satellitenbetrieb aus Deutschland – zuständige Behörden, Versicherungspflichten, laufende Aufs…
10. **haftungsuebereinkommen-absoluter-bodenschaden-und-vers** — Liability Convention 1972 – Art. II–V: Gefährdungshaftung am Boden, Verschuldenshaftung im Weltraum, Anspruchsverfahren …
11. **registrierungsuebereinkommen-register** — Registration Convention 1975 (REG) – Pflichtregistrierung, UN-Register, nationale Register, Jurisdiktion und Kontrolle i…
12. **outer-space-treaty-grundprinzipien-nichtaneignung** — OST 1967 – Art. I–IX: Nichtaneignungsprinzip, nationale Verantwortung nichtstaatlicher Akteure, Konsultationspflicht im …
13. **starlink-oneweb-iris2-und-oeffentliche-beschaffung** — Starlink, OneWeb, IRIS² – öffentliche Beschaffung, Sicherheitsanforderungen, Vergaberecht und strategische Autonomie im …
14. **astronautenrettung-rueckgabe-und-statusfragen** — Rescue Agreement 1968 – Rettungs- und Rückgabepflicht, Botschafter der Menschheit, Status kommerzieller Raumfahrer im We…
15. **frequenzzuteilung-itu-erdbeobachtung** — Frequenzzuteilung für Satelliten – ITU Radio Regulations, BNetzA-Verfahren, Koordinierung, Interferenz-Beschwerden im We…

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlaegt passende Fachmodule aus diesem Plugin vor und fuehrt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext ordnet der Skill das Material eige..._

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Weltraumrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Weltraumrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen. Tragende Normen (WeltraumG, Outer Space Treaty, ESA-Übereinkommen) werden nicht aus Modellwissen finalisiert, sondern über die zugelassenen Live-Quellen geprüft.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Sofortrisiken zuerst markieren** — Fristen, Zustellung, Form, Zuständigkeit, Beweis-, Kosten- und Haftungsrisiken benennen.
2. **Aktenlandkarte bauen** — Welche Dateien sind Original, welche nur Behauptung; was fehlt für einen verwertbaren nächsten Schritt?
3. **Rolle klären** — Mandant, Gegner, Behörde, Gericht, betroffene Stelle; mit welchem Ziel und welcher Reichweite?
4. **Ziel bestimmen** — Prüfung, Entwurf, Antrag, Anmeldung, Schriftsatz, Verteidigung, Dashboard, Memo, Red-Team?
5. **Rechtsquellen trennen** — Normtext, Behördenpraxis, Rechtsprechung, Vertrag, technischer Standard und Praxisroutine getrennt halten.
6. **Fachmodule auswählen** — Drei bis sieben passende Skills aus diesem Plugin nennen mit Begründung, warum sie jetzt nützlich sind.
7. **Erste verwertbare Ausgabe liefern** — Kurze Lagekarte mit nächstem Schritt oder erstem Entwurf, statt einer langen abstrakten Abhandlung.

## Fachlicher Anker — Weltraumrecht

Tragende Anker: WeltraumG, Outer Space Treaty, ESA-Übereinkommen. Tatsächliche Fundstellen werden über dejure.org, openJur, gesetze-im-internet.de, BGH-/BVerfG-/EuGH-/EuG-Datenbank live geprüft und nicht aus Modellwissen finalisiert.

---

## Skill: `anti-satellite-test-ban-und-orbital-debris-pledge`

_Anti-Satellite-Test-Ban und Orbital-Debris-Pledge: zerstoerende ASAT-Tests Voelkerrechtsbewertung UN-Resolutionslinie und kommerzielle Konsequenzen für Operator Versicherer Investoren Lieferanten. Klaert Geltung des Outer Space Treaty bei ASAT Liability Convention Registrierungsfragen Sanktionsre..._

# Anti-Satellite-Test-Ban und Orbital-Debris-Pledge

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Sofortfragen

1. Operator, Lieferant, Investor, Versicherer, Behörde, NGO oder Forschungsinstitut?
2. Operativer Bezug zu betroffenen Orbits, Frequenzen oder Bahnregionen?
3. Geplanter eigener Test, Mitwirkung an einer staatlichen Mission, Beruehrung mit einer der bekannten ASAT-Nationen?
4. Aktuelles Sanktionsregime gegen Russland, Iran, Nordkorea einschlaegig?
5. Versicherungsfall bereits eingetreten oder vorsorgend zu pruefen?

## Voelkerrechtliche Rahmensetzung

- **Outer Space Treaty 1967**: Art. I (freie Nutzung zum Wohl aller), Art. III (UN-Charta Geltung), Art. IV (friedliche Nutzung des Weltraums, Kernwaffenverbot), Art. VI (staatliche Verantwortlichkeit für nichtstaatliche Aktivitaeten), Art. VII (Haftung für Schaeden), Art. IX (gebotene Rücksichtnahme und harmful interference).
- **Liability Convention 1972**: Art. II absolute Haftung für Schaeden auf der Erdoberflaeche; Art. III Verschuldenshaftung für Schaeden im All; Art. V solidarische Haftung mehrerer Startstaaten.
- **Registration Convention 1975**: Art. II Pflicht zur Registrierung, Art. IV Mitteilungspflicht ueber Zustand und Bahn.
- **UN-Generalversammlung Resolution 77/41 vom 07.12.2022**: Ruft alle Staaten auf, sich zu verpflichten, keine zerstoerenden direct-ascent ASAT-Tests durchzufuehren. Ueber 150 Stimmen dafür; Deutschland und EU-Mitgliedstaaten zustimmend.
- **US Vice President Pledge 2022 (April 18)**: einseitige US-Erklaerung, keine zerstoerenden direct-ascent ASAT-Tests durchzufuehren; mittlerweile von mehr als drei Dutzend Staaten uebernommen, darunter Deutschland (Beitritt vorbehaltlich der Verifikation in amtlicher Quelle).

## Nationales und EU-Recht

- **Deutschland**: kein in Kraft gesetztes nationales Weltraumgesetz (Stand 2026 Entwurf vorhanden, Beschluss live verifizieren). Bisherige Genehmigungspraxis ueber Frequenzaufsicht (BNetzA), Aussenwirtschaftsrecht (BAFA, AWG, AWV) und ueber das Allgemeine Polizei- und Ordnungsrecht der Länder bei Bodensegmenten.
- **EU**: Verordnung (EU) 2021/696 ueber das Weltraumprogramm der Union; Mitteilung COM(2023) 9 "EU Space Strategy for Security and Defence" mit ASAT-Klauseln. Verordnungsentwurf zum Weltraumgesetz der EU (COM live verifizieren).
- **EU-Sanktionen Russland**: Art. 2c Verordnung (EU) 833/2014 in der Fassung der Anpassung 2022/879 und Folgeakten — Exportverbot für raumfahrtbezogene Dual-Use-Gueter.

## Operative Folgen für Betreiber

- **Risiko für eigene Satelliten**: ein zerstoerender Test im LEO-Bereich erzeugt Tausende Truemmer (Russlandtest 2021 schuf ueber 1500 trackbare Objekte). Operationale Folgen: Manoeverhauefigkeit, Kollisionsrisiko, hoehere CSpOC Conjunction Data Messages.
- **Versicherung**: Standardklauseln in der TLI-/IOL-Versicherung schliessen oft Kriegsereignisse aus; ASAT-Tests koennten als war/hostile act gewertet werden. Pruefung der Lloyd's Market Association-Klauseln LMA5390 und Folgevarianten.
- **Lieferkette**: Re-Export-Kontrolle, US ITAR/EAR für raumfahrttechnologisches Material, EU Dual-Use-VO 2021/821.
- **Datenfluss**: Befassung mit US Space Force CSpOC, ESOC Space Debris Office und EU SST Konsortium.

## Pruefraster

1. Voelkerrechtliche Pflicht des Mandanten-Staates verletzt?
2. Mandant selbst Partei einer ASAT-Mission oder mittelbar betroffen?
3. Operativer Eingriff in eigene Mission noetig?
4. Versicherungsrechtliche Anzeigepflicht ausgeloest?
5. Sanktionsrechtliche Pruefung (Aufrechterhaltung von Lieferbeziehungen, Re-Export, AWV)?
6. Kommunikationsstrategie (Aufsicht, Versicherer, Investoren, Oeffentlichkeit) festgelegt?

---

## Skill: `lunar-heritage-quantenkommunikation-via`

_Lunar Heritage: Schutz historischer Mondlandestellen und ihrer Artefakte. Klaert das US One Small Step to Protect Human Heritage in Space Act 2020 die Auslegung der Artikel I II und IX OST zur Frage Non-Appropriation und Common Heritage NASA Recommendations to Space-Faring Entities und das ICOMOS..._

# Lunar Heritage und Schutz historischer Mondlandestellen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Sofortfragen

1. Welche Mission und welcher Mondbereich (Mare Tranquillitatis, Mare Imbrium, Suedpol, Far Side)?
2. Beruehrung mit Apollo-, Luna-, Chang E-, Surveyor-, Lunokhod- oder Hakuto-R-Stellen?
3. Mission staatlich, kommerziell oder gemischt?
4. Rechtsordnung des Start- oder Registrierungsstaates?
5. Konflikt mit anderen Akteuren oder Anwoerter auf Schutzzone?

## Voelker- und nationalrechtlicher Rahmen

- **Outer Space Treaty 1967**: Art. I freier Zugang aller Staaten zum Mond; Art. II Verbot der nationalen Aneignung; Art. IX gebotene Rücksichtnahme und Vermeidung von harmful interference; Art. VIII Eigentum an Gegenstaenden bleibt beim Eintragungsstaat.
- **Moon Agreement 1979**: Art. 7 Vermeidung von schaedlichen Veraenderungen; Art. 11 Mond als common heritage of mankind. Ratifikation eng (Deutschland nicht; USA nicht; China nicht).
- **Registration Convention 1975**: gegenstaendlicher Schutz registrierter Gegenstaende.
- **US One Small Step to Protect Human Heritage in Space Act** (Public Law 116-275, 31.12.2020): verpflichtet US-Akteure mit NASA-Beteiligung zur Einhaltung der NASA Recommendations to Space-Faring Entities (NASA-SP-2011-1226).
- **NASA Recommendations to Space-Faring Entities (2011)**: Schutzzonen 75 m und 225 m um Apollo-Stellen, je nach Sensitivitaet (Lunar Module, Experimente, Mobile Geraete). Annaeherungsausschluss für staubaufwirbelnde Manoever.
- **Artemis Accords 2020**: Art. 9 Schutz aussergewoehnlich wertvoller Stellen ("outer space heritage"). Bislang ueber 30 Unterzeichnerstaaten (Deutschland Beitritt September 2023; live verifizieren).

## Praktische Schutzpflichten

- **Trajektorienberechnung**: Annaeherung nicht in der Hauptantriebsachse historischer Stellen; mindestens NASA-Standoff einhalten.
- **Plume Impingement**: Berechnung des Triebwerksgaseinflusses auf historische Artefakte; Staub und ballistische Auswuerfe.
- **Sample Collection**: kein Sample von Apollo- oder Luna-Hardware; ausnahmsweise Forschungssampling nur mit NASA / Roscosmos Zustimmung und im Rahmen multilateraler Programme.
- **Datenpunkt-Veroeffentlichung**: Vermeidung von Veroeffentlichungen, die zu unkontrolliertem Sammeltourismus fuehren.

## Kollisionen mit kommerziellen Interessen

- **Wettbewerb um First-Visit-Status** bei Chang E 7/8 und Artemis II-IV.
- **Sammlerwert** historischer Artefakte vs. NASA-Eigentumsrechte (US-Recht: historische Artefakte gelten als US-Bundeseigentum, mit Sondervorschriften für geschenkte Apollo-Materialien).
- **Tourismus**: Wettbewerb zwischen Anbietern um Annaeherungspflicht an Apollo-Stellen.

## Pruefraster

1. Welcher Mondbereich, welche historische Stelle?
2. Welche nationalen und voelkerrechtlichen Vorschriften?
3. Welche NASA-/Artemis-Standoff-Werte?
4. Triebwerks- und Trajektorienanalyse vorhanden?
5. Kommerzielle Annaeherungserlaubnis erforderlich?
6. Versicherung deckt Heritage-Damage?

---

## Skill: `quantenkommunikation-via-satellit`

_Quantenkommunikation via Satellit: Quantum Key Distribution QKD-Missionen und Schluesselverteilung uebersatellitisches Backbone. Klaert die Pflichten nach BSI-Gesetz NIS2-RL Geheimschutz-Verordnung GHB sowie ITU-Frequenzkoordination und Exportkontrolle (Wassenaar Arrangement EU Dual-Use VO 2021/8..._

# Quantenkommunikation via Satellit

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Sofortfragen

1. Welche Rolle: Betreiber, Bodenstationsbetreiber, Forschungsinstitut, KRITIS-Sektor-Anwender oder Aufsichtsbehoerde?
2. Welche Schluessellaenge und welcher Protokollstandard (BB84, B92, E91)?
3. Welche Frequenzbaender (Free-Space-Optical-Communication ueblich; Funklink für Klassisch-Channel)?
4. Welcher Sicherheitsstufe (VS-NfD, VS-Vertraulich, GEHEIM)?
5. Welche internationale Reichweite (CN/US-Export, EU-Konsortium)?

## Rechtsrahmen

- **BSI-Gesetz (BSIG)** insbesondere §§ 8a-8b (KRITIS-Pflichten) und § 8c (KRITIS-Dachgesetz) iVm KRITIS-DachG-Entwurf 2023. Quantum-Backbone als IT-Infrastruktur kritischer Versorgungssektoren ist regelmaessig KRITIS-pflichtig.
- **NIS2-Richtlinie (EU) 2022/2555**: Umsetzung in DE durch NIS2-Umsetzungsgesetz (NIS2UmsuCG, in Kraft live verifizieren). Pflichten zur Risikomanagement, Vorfallmeldung 24/72 Stunden, Aufsicht durch BSI.
- **Sicherheitsueberpruefungsgesetz (SUeG)** und **Geheimschutzhandbuch (GHB)**: bei Beschaeftigten mit VS-Berechtigung.
- **VS-NfD-Bestimmungen** für raumfahrtbezogene Verschluesselungstechnologie.
- **Wassenaar Arrangement** und **EU Dual-Use-Verordnung (EU) 2021/821**: Quantum-Schluesselverteilungssysteme sind unter Position 5A002 (Information Security) und Position 5A004 (Quantum Computing) listenpflichtig.
- **Telekommunikationsgesetz (TKG)** § 165 zur Sicherheit von Telekommunikationsnetzen.
- **DSGVO** Art. 32 zur Sicherheit der Verarbeitung.
- **ITU Radio Regulations**: Frequenzkoordinierung für Klassisch-Channel (Tracking, Telemetry, Command, Daten-Downlink).

## Architektur und Pflichtenmatrix

- **Space Segment**: QKD-Payload (z. B. Polarisationskorrelation), Pointing-System, Klassisch-Funktion für Schluesselauthentifikation.
- **Ground Segment**: Optische Bodenstation, Wetterabhaengigkeit, Sichtbarkeitsfenster.
- **Key Management System**: Schluesselverwertung in symmetrischer Krypto (AES-256 oder kuenftige PQC-Algorithmen).
- **Trusted Node Architecture**: in EuroQCI mehrstufiges Vertrauensmodell.
- **Sicherheitsanforderungen**: Common Criteria EAL 4+ als Minimum; bei GEHEIM-Stufe EAL 6+.

## Beweissicherung im Zwischenfall

- **Side-Channel-Angriffe** (Photon-Number-Splitting, Bright-Light-Injection): protokollarisch dokumentieren.
- **Trojan-Horse-Attacks**: Hardware-Side-Channel-Analyse vorhalten.
- **Forensik**: Roh-Photonenstatistik archivieren (mind. 12 Monate, idealerweise gesamte Missionsdauer).
- **Meldepflichten**: BSI nach NIS2; Bundesnetzagentur nach TKG § 168; bei VS-Vorfall MAD/BND-Koordination.

## Versicherbarkeit

- TLI-/IOL-Versicherung mit Sondersummen für kryptografische Payloads.
- Cyber-Cover-Klauseln pruefen (oft Ausschluss bei staatlich gesponserten Angriffen).
- Lloyd's LMA5403 als haufige Cyber-Ausschlussklausel.

## Pruefraster

1. KRITIS-Pflicht ausgeloest? — § 8a BSIG.
2. NIS2-Pflichten (Vorfallmeldung 24/72h, Risikomanagement)?
3. Exportkontrolle (BAFA, Dual-Use-VO)?
4. Sicherheitsueberpruefung der Mitarbeiter?
5. Frequenzlizenz BNetzA?
6. Versicherung deckt Cyber + kryptografischer Schaden?
7. Schluesselmanagement nach BSI TR-02102?

---

## Skill: `space-weather-solarsturm-haftung-und-versicherung`

_Space Weather Solarsturm und geomagnetische Ereignisse: rechtliche Bewertung von Satellitenausfall Stromnetzausfall GPS-Stoerung und Funkausfall. Klaert das Verhaeltnis Force-Majeure zu Naturereignis-Klauseln in Versicherungs- und Lieferketten-Vertraegen NOAA SWPC und ESA SSA-Warnungen Pflicht zu..._

# Space Weather: Solarsturm-Haftung und Versicherung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Sofortfragen

1. Rolle: Satellitenbetreiber, Energieversorger, TK-Anbieter, Luftfahrtgesellschaft, Versicherer, Aufsichtsbehoerde?
2. Welches Ereignis (CME-Ankunftsdatum, Kp-Index, F10.7 Solar Flux)?
3. Schadensumfang (Satellitenausfall, Bahnsenkung durch erhoehte Atmosphaere, Stromausfall, GPS-Drift)?
4. Versicherungsschutz und Anzeigeobliegenheiten?
5. KRITIS-Sektor betroffen?

## Wissenschaftlich-rechtliche Klassifikation

- **NOAA G-Skala (G1 bis G5)** und **R-Skala** (Radioblackouts) als Standardklassifizierung.
- **Carrington-Ereignis 1859** geschaetzte G5+ — historisches Maximum.
- **Quebec-Blackout 13.03.1989** G5 — Hydro-Quebec-Netz 9 Std. ausgefallen, 6 Mio. Menschen ohne Strom.
- **Halloween-Storms Oktober/November 2003** G5 — Satellitenausfall (z. B. ADEOS-2), GPS-Drift, Luftfahrtumleitungen.
- **Gannon Storm Mai 2024** G5 — starke Aurora bis ins Mittelmeer; Starlink reduzierte Hoehe, mehrere kommerzielle Satelliten temporaer ausser Betrieb.

## Vertrags- und Versicherungsrecht

- **Force-Majeure-Klauseln**: hauptstreit, ob Solarsturm als hoehere Gewalt qualifiziert. Argumente pro: nicht beherrschbar, nicht versicherbar im Vollumfang. Argumente contra: vorhersehbar via NOAA SWPC und ESA SSA mit Vorlauf bis zu 72 Stunden, Mitigation moeglich (Safe-Mode, Bahnkorrektur, Stromnetzdrosselung).
- **Versicherungsklauseln**: Lloyd's LMA5390 (TLI) und Folgevarianten beinhalten Naturereignisse als Deckungsfall, schliessen aber "wilful misconduct" und unzureichende Mitigation aus. Bei Solarsturm idR Deckung wenn Warnung vom Betreiber befolgt wurde.
- **Cyber-vs-Naturklauseln**: Klare Trennung; geomagnetisch induzierte Stromschwankungen sind Naturereignisse, kein Cyber-Vorfall.
- **Sublimits**: oft 25-50 Mio. Euro für geomagnetisch induzierte Schaeden je Versicherer-Einheit.

## KRITIS und NIS2

- **§ 8a BSIG**: Betreiber Kritischer Infrastrukturen Energie und Telekommunikation muessen Vorkehrungen gegen Space Weather als Naturgefahr treffen (Stellungnahme BSI 2022, Az im Digitalisat verifizieren).
- **NIS2-Richtlinie**: Risikomanagement umfasst geophysikalische Ereignisse; Vorfallmeldung bei betrieblicher Stoerung.
- **EnWG § 11**: Pflicht der Netzbetreiber zur Aufrechterhaltung; spezifische Vorgaben der BNetzA zur Reservehaltung gegen geomagnetisch induzierte Stroeme (GIC) live verifizieren.

## Luftfahrt

- **ICAO Annex 3 Amendment 78 (2018)**: Pflicht zur Space-Weather-Information bei Luftverkehrsdiensten.
- **EUROCONTROL Space Weather Service**: Echtzeit-Warnungen.
- **Polare Routen**: Umleitungspflicht bei hoher Strahlenexposition (R3-R5).

## Pruefraster

1. Ereignisklassifikation (G/R-Skala, F10.7)?
2. Welche Vorwarnung hat NOAA SWPC / ESA SSA gegeben? Vorlauf?
3. Hat der Betreiber Mitigation eingeleitet (Safe-Mode, Bahnkorrektur, Netzdrosselung)?
4. Schadensbild Schaden konkret (Satellit, Netz, GPS, TK)?
5. Versicherungsschutz, Sublimit, Wartefrist?
6. KRITIS- oder NIS2-Meldepflicht ausgeloest?
7. Force-Majeure-Klausel in welcher Fassung?

---

## Skill: `commercial-leo-destinations-iss-nachfolge`

_Commercial LEO Destinations: rechtliche Architektur kommerzieller Low-Earth-Orbit-Stationen Axiom Orbital Reef Starlab Haven-1 als ISS-Nachfolge. Klaert NASA-Commercial-LEO-Programme Phase 2 Vertragsarchitektur Space Act Agreement Service Level Agreements zwischen Modul-Eigentuemer Crew-Provider..._

# Commercial LEO Destinations - ISS-Nachfolge

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Sofortfragen

1. Rolle: Crew-Provider, Cargo-Provider, Modul-Eigentuemer, Endnutzer, Versicherer, Investor, staatliche Stelle?
2. Welche Plattform: Axiom Station, Orbital Reef, Starlab, Haven-1 oder europaeische Loesung?
3. Vertragsmodell: NASA Space Act Agreement, ESA-Beteiligung, kommerzielle Direktbeziehung?
4. Welche Nutzung: bemannte Forschung, In-Space-Manufacturing, Tourismus, Wartungs-/Service-Mission?
5. Welche Mikrogravitations- oder Vakuum-Anforderungen?

## NASA Commercial LEO Destinations Program

- **Phase 1 (2021-2023)**: Funded Space Act Agreements (SAA) mit Axiom Space, Blue Origin (Orbital Reef), Voyager Space (Starlab), Nanoracks.
- **Phase 2 (2024-2026)**: Wettbewerb um Anchor-Customer-Status; NASA als Ankerkunde mit bestimmten Crew-Anteilen.
- **NASA Crew-Anchor-Pflicht**: zwei NASA-Crewmitglieder dauerhaft, vier mit Rotation, bis zu sieben mit Erweiterung.
- **ISS-Deorbit 2030/31**: NASA Authorization Act 2022 mit Deorbit-Plan; SpaceX-Vertrag 2024 für USDV (U.S. Deorbit Vehicle).

## Vertragsarchitektur

### Eigentumsstruktur
- Modul- und Stationsbetreiber haelt Eigentum (z. B. Axiom an seinen Modulen).
- Crew-Provider (SpaceX Crew Dragon, Boeing Starliner kuenftig auch andere) als eigene Vertragslinie.
- Cargo-Provider (SpaceX Cargo Dragon, Sierra Space Dream Chaser, Northrop Cygnus).
- Forschungsnutzer durch dedizierte SLAs.

### Vertragstypen
- **Hauptvertrag NASA SAA**: vergibt Ankerkunden-Status.
- **Operator-Customer-Agreement (OCA)**: Service Level für Bahnkorrektur, Lebenserhaltungssystem, Crew-Pflege.
- **Module Hosting Agreement (MHA)**: Anbringung externer Module.
- **Payload Hosting Agreement (PHA)**: temporaere Experimente an Bord.
- **Tourism-Vertrag**: spezifische Haftung-, Versicherungs- und Verzichtsklauseln.

### Anwendbares Recht
- **Voelkerrecht**: Outer Space Treaty Art. VIII (Eigentum am Modul bleibt beim Registrierungsstaat), Liability Convention Art. III (Verschuldenshaftung im All).
- **Nationales US-Recht**: 51 U.S.C. § 50901 ff. für kommerzielle Raumfahrt; Reciprocal Waivers of Claims (Cross-Waiver) zwingend in NASA SAAs.
- **EU/Deutschland**: ESA-Konvention 1975 für ESA-Module; spaetere Beteiligung am US-Marktrecht.

## IP-Schutz an Bord

- **Patentrechtliche Fragen**: Erfindungen an Bord der Station werden nach Recht des Eintragungsstaates des Moduls bewertet (Art. VIII OST).
- **CIS-Erfindungen** (Crewmember-Inventions in Space): Sondervorschriften je nach Crew-Heimatstaat.
- **US 35 U.S.C. § 105**: Erfindungen an Bord eines US-Raumfahrzeugs gelten als in den USA gemacht.
- **Forschungsdaten**: Lizenzierung an Forschungsuniversitaeten und Pharmafirmen mit ueblicherweise mehrjaehrigen Embargo-Klauseln.

## Versicherbarkeit

- Bahnkorrektur-Versicherung (Stationkeeping).
- Crew-Verletzung-Versicherung (Cross-Waiver schliesst US-Government-Hauptklagen aus; nicht aber Dritte).
- Cargo-Verlust.
- Modul-Verlust.
- Liability gegenueber anderen Operatoren (Konjunktionsereignis).
- Lloyd's LMA-Klauseln für Spacelegal-Risiken.

## Pruefraster

1. Vertragsstuktur (NASA SAA, OCA, MHA, PHA)?
2. Anwendbares Recht (US, ESA-Mitgliedstaat, gemischt)?
3. Cross-Waiver beruecksichtigt?
4. IP-Schutz und Lizenzkette geklaert?
5. Versicherbarkeit aller Risikoschichten?
6. Exportkontrolle (ITAR / EAR / EU Dual-Use)?
7. Crew-Anforderungen (Medizincheck, Versicherbarkeit, Schadensersatz)?

---

## Skill: `satellitenschwarm-ueber-deutschland-frequenz-kollision`

_Mega-Konstellationen (Starlink, OneWeb, IRIS²) über Deutschland – Frequenzinterferenz, Kollisionswarnung, Datenschutz, Lichtverschmutzung im Weltraumrecht._

# Weltraumrecht: Satellitenschwarm über Deutschland: Frequenz-, Kollisions- und Datenschutzrisiken

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Aufgabe und Einsatzbereich

Bearbeite **Satellitenschwarm über Deutschland: Frequenz-, Kollisions- und Datenschutzrisiken** im Bereich Weltraumrecht. Er strukturiert die praktische Lage, prüft einschlägige Normen des internationalen und nationalen Rechts und liefert verwertbare Ergebnisse für Betreiber, Behörden, Investoren, Kanzleien und Compliance-Beauftragte.

## Thematischer Kontext

- Mega-Konstellationen: Starlink, OneWeb, Amazon Kuiper, IRIS²
- Frequenzinterferenz-Risiken: ITU-Koordinierung, BNetzA-Zuständigkeit
- Kollisionswarnung: Space Traffic Management, IADC-Guidelines
- Datenschutz: DSGVO bei Erdbeobachtung über Deutschland
- Lichtverschmutzung: astronomische Einwendungen, Nachbarrecht

## Einschlägige Normen und Regelwerke

- **ITU Radio Regulations Art. 9**: Koordinierungspflicht bei Frequenzinterferenz
- **BNetzA**: Nationale Frequenzbehörde; Interferenzbeschwerden
- **IADC Debris Mitigation Guidelines**: Kollisionsvermeidung für Konstellationsbetreiber
- **DSGVO Art. 6**: Rechtsgrundlage für Erdbeobachtungsdaten
- **EU 2021/696 SST**: Space Surveillance and Tracking: Kollisionswarnung
- **UNCOPUOS LTS Guidelines**: Guideline 2, 4: Kurzfristige Kollisionsvermeidung

## Kaltstart in 6 Fragen

1. **Rolle**: Wer handelt – Betreiber, Investor, Behörde, Kanzlei, Versicherer, Universität, Verlag, Betroffene?
2. **Aufgabentyp**: Prüfung, Entwurf, Genehmigung, Compliance, Streit, Due Diligence oder Dokumentation?
3. **Unterlagen**: Welche Dokumente liegen vor – Vertrag, Lizenz, Registerauszug, technische Spezifikation, Gutachten, Normtext?
4. **Rechtsordnung**: Deutsches Recht, EU-Recht, US-Recht, Völkerrecht – oder Kombination?
5. **Fristen**: Welche Genehmigungsfristen, ITU-Koordinierungsfristen, Vertragsoptionen oder Behördenfristen laufen?
6. **Ergebnisformat**: Memo, Ampelmatrix, Klauselentwurf, Behördenbrief, Board-Vorlage oder Fristenkalender?

## Prüfprogramm

1. **Frequenzinterferenz**: ITU-Koordinierungspflicht prüfen; BNetzA-Beschwerdeverfahren kennen
2. **Kollisionsrisiko**: IADC-Leitlinien, ESA Space Debris Office-Daten, STM-Protokolle
3. **DSGVO-Compliance**: Personenbezogene Daten aus Erdbeobachtung über Deutschland: DSFA erforderlich?
4. **Lichtverschmutzung**: Astronomische Nutzungseinschränkungen; keine direkte Rechtsnorm, aber Abwägungsgebot
5. **Debris-Mitigation-Plan**: 25-Jahres-Regel; 5-Jahres-Regel für LEO nach neuem IADC-Standard
6. **Notfallkommunikation**: Kollisionswarnprotokoll: Wer informiert wen?

## Normencheck: Schicht für Schicht

### Völkerrecht
- Outer Space Treaty 1967 (OST): Art. I, II, VI, VII, VIII, IX
- Liability Convention 1972 (LIAB): Art. II–V (Haftungsregime)
- Registration Convention 1975 (REG): Registrierungspflichten
- Rescue Agreement 1968 (ARRA): Rettung und Rückgabe
- Ggf. Moon Agreement 1979 (MA): Ressourcen, Umwelt

### EU-Recht
- EU Space Programme Regulation (EU) 2021/696: Galileo, Copernicus, IRIS², SST
- EU Dual-Use-Verordnung (EU) 2021/821: Exportkontrolle Raumfahrtgüter
- NIS2-Richtlinie 2022/2555: Cybersicherheit kritischer Infrastruktur
- DSGVO (EU) 2016/679: Personenbezogene Daten (Erdbeobachtung, Tracking)

### Deutsches Recht
- LuftVG (Luftverkehrsgesetz): https://www.gesetze-im-internet.de/luftvg/
- Geplanter Raumfahrtgesetzentwurf BMWK
- BAFA Exportkontrolle: ITAR-Listung, EAR, EU-Dual-Use
- BSI-Gesetz, KRITIS-Verordnung

### Soft Law und Guidelines
- UNCOPUOS Long-Term Sustainability Guidelines (LTS 2018)
- Artemis Accords (2020, 37+ Unterzeichner)
- IADC Debris Mitigation Guidelines

## Typische Fallen

- **Keine universelle Norm**: Lichtverschmutzung ist rechtlich nicht geregelt; Abwägung über Abwägungsgebot
- **ITU priority rule**: Erster Anmelder hat Schutzprivileg; spätere Systeme müssen koordinieren
- **Datenschutz vs. Sicherheit**: Erdbeobachtungsdaten können sicherheitsrelevant sein; Ausnahmen prüfen
- **Debris-Plan unverbindlich**: IADC-Leitlinien sind Soft Law; keine Durchsetzung ohne nationales Recht
- **Zuständigkeit ungeklärt**: Wer ist für Kollisionswarnungen in Deutschland zuständig?

## Qualitätssicherung

- Keine Scheingenauigkeit: Wenn Normstand, Ratifikationsstatus oder Rechtsprechung unklar sind, Live-Check vorschlagen.
- Quellen nur nach Verifikation zitieren: UNOOSA, EUR-Lex, Gesetze-im-Internet, BAFA, ESA, BNetzA.
- Tatsachen, Annahmen, Wertungen und offene Beweisfragen immer getrennt führen.
- Zuständigkeit, Form, Frist, Beweislast, Vollzug und Rechtsbehelf immer getrennt ausgeben.
- Startstaat, Registerstaat, Betreiber, Missionskontrolle, Versicherer immer separat identifizieren.

## Output-Formate

- Frequenz-Interferenz-Analyse mit BNetzA-Verfahrenshinweisen
- Debris-Mitigation-Plan-Prüfung für Konstellationsbetreiber
- DSGVO-Compliance-Check für Erdbeobachtungsdaten
- STM-Protokoll-Empfehlung
- Behördenbrief an BNetzA bei Interferenz

## Quellen und Normen

- ITU Radio Regulations: https://www.itu.int/en/ITU-R/terrestrial/broadcast/Pages/Regulations.aspx
- BNetzA Frequenzen: https://www.bundesnetzagentur.de/DE/Fachthemen/Telekommunikation/Frequenzen/start.html
- IADC Debris Mitigation Guidelines: https://www.iadc-home.org/documents_public/view/id/82
- EU Space Programme Regulation SST: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0696
- UNCOPUOS LTS Guidelines: https://www.unoosa.org/oosa/en/ourwork/topics/long-term-sustainability-of-outer-space-activities.html
- DSGVO: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679

---

## Skill: `mondvertrag-ressourcen`

_Moon Agreement 1979 – Gemeinsames Erbe der Menschheit, gescheitertes Ressourcenregime, keine Ratifikation durch Raumfahrtnationen im Weltraumrecht._

# Weltraumrecht: Mondvertrag: Ressourcen-Governance und politische Akzeptanz

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Aufgabe und Einsatzbereich

Bearbeite **Mondvertrag: Ressourcen-Governance und politische Akzeptanz** im Bereich Weltraumrecht. Er strukturiert die praktische Lage, prüft einschlägige Normen des internationalen und nationalen Rechts und liefert verwertbare Ergebnisse für Betreiber, Behörden, Investoren, Kanzleien und Compliance-Beauftragte.

## Thematischer Kontext

- Moon Agreement 1979 (MA) – ambitioniertestes und gescheitertstes Weltraumdokument
- Art. 11: Mond und Ressourcen als gemeinsames Erbe der Menschheit
- Fehlendes internationales Ressourcenregime als zentrales Problem
- Keine Ratifikation durch USA, Russland, China, EU-Staaten
- Verhältnis zu Artemis Accords und ILRS-Programm

## Einschlägige Normen und Regelwerke

- **MA Art. 11 Abs. 1**: Gemeinsames Erbe der Menschheit – keine Eigentumsrechte
- **MA Art. 11 Abs. 3**: Explorations- und Nutzungsfreiheit; kommerzielle Extraktion erst nach Regime
- **MA Art. 11 Abs. 5**: Pflicht zur Schaffung eines internationalen Ressourcenregimes
- **MA Art. 7**: Schutz der Mondumwelt
- **MA Art. 14**: Staatliche Verantwortung für nichtstaatliche Aktivitäten
- **US SPACE Act 2015**: Ressourceneigentum ohne Gebietsanspruch – Gegenentwurf zum MA
- **Luxemburger Space Resources Law 2017**: EU-paralleles Ressourcenrechtsmodell

## Kaltstart in 6 Fragen

1. **Rolle**: Wer handelt – Betreiber, Investor, Behörde, Kanzlei, Versicherer, Universität, Verlag, Betroffene?
2. **Aufgabentyp**: Prüfung, Entwurf, Genehmigung, Compliance, Streit, Due Diligence oder Dokumentation?
3. **Unterlagen**: Welche Dokumente liegen vor – Vertrag, Lizenz, Registerauszug, technische Spezifikation, Gutachten, Normtext?
4. **Rechtsordnung**: Deutsches Recht, EU-Recht, US-Recht, Völkerrecht – oder Kombination?
5. **Fristen**: Welche Genehmigungsfristen, ITU-Koordinierungsfristen, Vertragsoptionen oder Behördenfristen laufen?
6. **Ergebnisformat**: Memo, Ampelmatrix, Klauselentwurf, Behördenbrief, Board-Vorlage oder Fristenkalender?

## Prüfprogramm

1. **Vertragsstatus**: Ist der betreffende Staat MA-Ratifizierer? Wenn nein → nur OST Art. II relevant
2. **Aktivitätstyp**: Erkundung (frei) vs. Ressourcenextraktion (MA-Regime erforderlich, aber inexistent)?
3. **Nationales Ressourcenrecht**: SPACE Act, Luxemburger Gesetz oder nationales Äquivalent anwendbar?
4. **Artemis Accords**: Hat Staat unterzeichnet? Safety Zones und Interoperabilitätspflichten prüfen
5. **Umweltpflichten**: Art. 7 MA und Planetary Protection (OST Art. IX, COSPAR Policy) berücksichtigen
6. **Zukunftsszenario**: Bei MA-Regime-Entstehung: Investitionsschutz, Eigentumsrechte, Konzessionsmodell?

## Normencheck: Schicht für Schicht

### Völkerrecht
- Outer Space Treaty 1967 (OST): Art. I, II, VI, VII, VIII, IX
- Liability Convention 1972 (LIAB): Art. II–V (Haftungsregime)
- Registration Convention 1975 (REG): Registrierungspflichten
- Rescue Agreement 1968 (ARRA): Rettung und Rückgabe
- Ggf. Moon Agreement 1979 (MA): Ressourcen, Umwelt

### EU-Recht
- EU Space Programme Regulation (EU) 2021/696: Galileo, Copernicus, IRIS², SST
- EU Dual-Use-Verordnung (EU) 2021/821: Exportkontrolle Raumfahrtgüter
- NIS2-Richtlinie 2022/2555: Cybersicherheit kritischer Infrastruktur
- DSGVO (EU) 2016/679: Personenbezogene Daten (Erdbeobachtung, Tracking)

### Deutsches Recht
- LuftVG (Luftverkehrsgesetz): https://www.gesetze-im-internet.de/luftvg/
- Geplanter Raumfahrtgesetzentwurf BMWK
- BAFA Exportkontrolle: ITAR-Listung, EAR, EU-Dual-Use
- BSI-Gesetz, KRITIS-Verordnung

### Soft Law und Guidelines
- UNCOPUOS Long-Term Sustainability Guidelines (LTS 2018)
- Artemis Accords (2020, 37+ Unterzeichner)
- IADC Debris Mitigation Guidelines

## Typische Fallen

- **MA nicht ratifiziert ≠ MA irrelevant**: Als Soft-Law-Quelle und für Auslegung von OST Art. II diskutiert
- **Gemeinsames Erbe ≠ Verbot**: Art. 11 erlaubt Erkundung; blockiert nur kommerzielle Extraktion ohne Regime
- **Sicherheitszonen ohne Rechtsgrundlage**: Artemis Accords-Zonen binden nur Unterzeichner; kein universelles Recht
- **Doppelstandard**: Staat kann OST ratifiziert haben, aber nationales Gesetz erlaubt Ressourceneigentum

## Qualitätssicherung

- Keine Scheingenauigkeit: Wenn Normstand, Ratifikationsstatus oder Rechtsprechung unklar sind, Live-Check vorschlagen.
- Quellen nur nach Verifikation zitieren: UNOOSA, EUR-Lex, Gesetze-im-Internet, BAFA, ESA, BNetzA.
- Tatsachen, Annahmen, Wertungen und offene Beweisfragen immer getrennt führen.
- Zuständigkeit, Form, Frist, Beweislast, Vollzug und Rechtsbehelf immer getrennt ausgeben.
- Startstaat, Registerstaat, Betreiber, Missionskontrolle, Versicherer immer separat identifizieren.

## Output-Formate

- Normvergleichsmatrix: MA vs. OST vs. Artemis Accords vs. nationales Recht
- Ressourcenrechts-Gutachten für Mondmission oder Asteroiden-Projekt
- Investitionsrisiko-Memo: Rechtslage bei MA-Regime-Entstehung
- Compliance-Checkliste für Mondprogramm-Beteiligte

## Quellen und Normen

- Moon Agreement 1979: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/moon-agreement.html
- Artemis Accords: https://www.nasa.gov/artemis-accords/
- US SPACE Act 2015: https://www.congress.gov/bill/114th-congress/house-bill/2262
- Luxemburger Space Resources Law: https://gouvernement.lu/en/actualites/toutes_actualites/communiques/2017/07-juillet/14-loi-espace.html
- UNOOSA Ratifikationsstatus: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/status/index.html

---

## Skill: `satellitenbetrieb-deutschland`

_Genehmigungsverfahren für Satellitenbetrieb aus Deutschland – zuständige Behörden, Versicherungspflichten, laufende Aufsicht im Weltraumrecht._

# Weltraumrecht: Satellitenbetrieb aus Deutschland: Genehmigung, Versicherung, Aufsicht

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Aufgabe und Einsatzbereich

Bearbeite **Satellitenbetrieb aus Deutschland: Genehmigung, Versicherung, Aufsicht** im Bereich Weltraumrecht. Er strukturiert die praktische Lage, prüft einschlägige Normen des internationalen und nationalen Rechts und liefert verwertbare Ergebnisse für Betreiber, Behörden, Investoren, Kanzleien und Compliance-Beauftragte.

## Thematischer Kontext

- Genehmigungspflicht für Satellitenbetrieb aus deutschem Staatsgebiet
- Zuständige Behörden: BMWK, DLR, BNetzA, BAFA, Landesluftfahrtbehörden
- Versicherungspflichten: dritte Haftpflicht (Third Party Liability)
- Frequenzzuteilung und ITU-Koordinierung durch BNetzA
- Laufende Aufsicht und Berichtspflichten

## Einschlägige Normen und Regelwerke

- **LuftVG § 1 Abs. 2**: Ggf. anwendbar auf Weltraumfahrzeuge
- **Raumfahrtgesetzentwurf BMWK**: Genehmigungsverfahren, Versicherung, Aufsicht
- **OST Art. VI**: Staatliche Verantwortung für Betreiber
- **ITU Radio Regulations**: Frequenzzuteilung und Koordinierung
- **BNetzA**: Nationale Frequenzbehörde
- **EU 2021/696**: EU-Weltraumprogramm-Anforderungen
- **BAFA AWG/AWV**: Exportkontrolle für Satellitentechnik

## Kaltstart in 6 Fragen

1. **Rolle**: Wer handelt – Betreiber, Investor, Behörde, Kanzlei, Versicherer, Universität, Verlag, Betroffene?
2. **Aufgabentyp**: Prüfung, Entwurf, Genehmigung, Compliance, Streit, Due Diligence oder Dokumentation?
3. **Unterlagen**: Welche Dokumente liegen vor – Vertrag, Lizenz, Registerauszug, technische Spezifikation, Gutachten, Normtext?
4. **Rechtsordnung**: Deutsches Recht, EU-Recht, US-Recht, Völkerrecht – oder Kombination?
5. **Fristen**: Welche Genehmigungsfristen, ITU-Koordinierungsfristen, Vertragsoptionen oder Behördenfristen laufen?
6. **Ergebnisformat**: Memo, Ampelmatrix, Klauselentwurf, Behördenbrief, Board-Vorlage oder Fristenkalender?

## Prüfprogramm

1. **Genehmigungspflicht prüfen**: Welche Aktivitäten benötigen Erlaubnis? BMWK, BAFA, BNetzA getrennt prüfen
2. **Behördenzuständigkeit klären**: BMWK für Weltraum, BNetzA für Frequenzen, BAFA für Dual-Use
3. **Versicherungsanforderungen**: Third Party Liability, Launch-Versicherung, In-Orbit-Versicherung
4. **ITU-Koordinierung starten**: Frequenzanmeldung 3–7 Jahre vor Start; BNetzA als nationaler Kontakt
5. **Registrierungspflicht**: Deutsches Register (geplant) + UN-Register über UNOOSA
6. **Laufende Compliance**: Betriebsberichte, Frequenznutzungsnachweise, Versicherungsnachweis

## Normencheck: Schicht für Schicht

### Völkerrecht
- Outer Space Treaty 1967 (OST): Art. I, II, VI, VII, VIII, IX
- Liability Convention 1972 (LIAB): Art. II–V (Haftungsregime)
- Registration Convention 1975 (REG): Registrierungspflichten
- Rescue Agreement 1968 (ARRA): Rettung und Rückgabe
- Ggf. Moon Agreement 1979 (MA): Ressourcen, Umwelt

### EU-Recht
- EU Space Programme Regulation (EU) 2021/696: Galileo, Copernicus, IRIS², SST
- EU Dual-Use-Verordnung (EU) 2021/821: Exportkontrolle Raumfahrtgüter
- NIS2-Richtlinie 2022/2555: Cybersicherheit kritischer Infrastruktur
- DSGVO (EU) 2016/679: Personenbezogene Daten (Erdbeobachtung, Tracking)

### Deutsches Recht
- LuftVG (Luftverkehrsgesetz): https://www.gesetze-im-internet.de/luftvg/
- Geplanter Raumfahrtgesetzentwurf BMWK
- BAFA Exportkontrolle: ITAR-Listung, EAR, EU-Dual-Use
- BSI-Gesetz, KRITIS-Verordnung

### Soft Law und Guidelines
- UNCOPUOS Long-Term Sustainability Guidelines (LTS 2018)
- Artemis Accords (2020, 37+ Unterzeichner)
- IADC Debris Mitigation Guidelines

## Typische Fallen

- **Fehlende Gesetzesgrundlage**: Bis zum Inkrafttreten des Weltraumgesetzes: behördliche Ermessensacts
- **Mehrfachzuständigkeit**: BMWK, BNetzA, BAFA, Landesbehörde – Koordinationsaufwand
- **Versicherungslücke**: Kein Pflichttarif; Betreiber können unterversichert operieren
- **ITAR-Sperrung**: US-Komponenten erfordern separate ITAR-Genehmigung (DSP-5)
- **ITU-Fristversäumnis**: Zu späte Frequenzanmeldung kann Missionsstart unmöglich machen

## Qualitätssicherung

- Keine Scheingenauigkeit: Wenn Normstand, Ratifikationsstatus oder Rechtsprechung unklar sind, Live-Check vorschlagen.
- Quellen nur nach Verifikation zitieren: UNOOSA, EUR-Lex, Gesetze-im-Internet, BAFA, ESA, BNetzA.
- Tatsachen, Annahmen, Wertungen und offene Beweisfragen immer getrennt führen.
- Zuständigkeit, Form, Frist, Beweislast, Vollzug und Rechtsbehelf immer getrennt ausgeben.
- Startstaat, Registerstaat, Betreiber, Missionskontrolle, Versicherer immer separat identifizieren.

## Output-Formate

- Genehmigungsfahrplan mit Behörden und Fristen
- Versicherungsmatrix (Launch, In-Orbit, TPL)
- ITU-Koordinierungsplan
- Behördenbriefe an BMWK, BNetzA, BAFA
- Compliance-Kalender für laufenden Betrieb

## Quellen und Normen

- LuftVG: https://www.gesetze-im-internet.de/luftvg/
- BNetzA Frequenzen: https://www.bundesnetzagentur.de/DE/Fachthemen/Telekommunikation/Frequenzen/start.html
- BAFA Exportkontrolle: https://www.bafa.de/DE/Aussenwirtschaft/Exportkontrolle/exportkontrolle_node.html
- EU Space Programme Regulation: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0696
- ITU Radio Regulations: https://www.itu.int/en/ITU-R/terrestrial/broadcast/Pages/Regulations.aspx
- UNOOSA: https://www.unoosa.org/

---

## Skill: `haftungsuebereinkommen-absoluter-bodenschaden-und-vers`

_Liability Convention 1972 – Art. II–V: Gefährdungshaftung am Boden, Verschuldenshaftung im Weltraum, Anspruchsverfahren im Weltraumrecht._

# Weltraumrecht: Haftungsübereinkommen: Absoluter Bodenschaden und Verschuldenshaftung im All

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Aufgabe und Einsatzbereich

Bearbeite **Haftungsübereinkommen: Absoluter Bodenschaden und Verschuldenshaftung im All** im Bereich Weltraumrecht. Er strukturiert die praktische Lage, prüft einschlägige Normen des internationalen und nationalen Rechts und liefert verwertbare Ergebnisse für Betreiber, Behörden, Investoren, Kanzleien und Compliance-Beauftragte.

## Thematischer Kontext

- Liability Convention 1972 (LIAB) – duales Haftungsregime
- Art. II: Absolute Haftung für Bodenschäden (verschuldensunabhängig)
- Art. III: Verschuldenshaftung für Schäden im Weltraum
- Art. V: Gesamtschuldnerschaft mehrerer Startstaaten
- Regressansprüche des Staates gegen private Betreiber
- 1-Jahres-Ausschlussfrist und diplomatischer Anspruchsweg

## Einschlägige Normen und Regelwerke

- **LIAB Art. I**: Definitionen: Schaden, Weltraumobjekt, Startstaat
- **LIAB Art. II**: Absolute Haftung am Boden – verschuldensunabhängig
- **LIAB Art. III**: Verschuldenshaftung im Weltraum
- **LIAB Art. IV**: Klagehäufung bei mehreren Startstaaten
- **LIAB Art. V**: Gesamtschuldnerschaft – interner Ausgleich nach Verschuldensgrad
- **LIAB Art. VI**: Entlastung bei grober Fahrlässigkeit des Geschädigten
- **LIAB Art. VIII–XVII**: Anspruchsverfahren: diplomatisch, Ausschlussfrist 1 Jahr
- **OST Art. VII**: Haftungsverpflichtung der Startstaaten

## Kaltstart in 6 Fragen

1. **Rolle**: Wer handelt – Betreiber, Investor, Behörde, Kanzlei, Versicherer, Universität, Verlag, Betroffene?
2. **Aufgabentyp**: Prüfung, Entwurf, Genehmigung, Compliance, Streit, Due Diligence oder Dokumentation?
3. **Unterlagen**: Welche Dokumente liegen vor – Vertrag, Lizenz, Registerauszug, technische Spezifikation, Gutachten, Normtext?
4. **Rechtsordnung**: Deutsches Recht, EU-Recht, US-Recht, Völkerrecht – oder Kombination?
5. **Fristen**: Welche Genehmigungsfristen, ITU-Koordinierungsfristen, Vertragsoptionen oder Behördenfristen laufen?
6. **Ergebnisformat**: Memo, Ampelmatrix, Klauselentwurf, Behördenbrief, Board-Vorlage oder Fristenkalender?

## Prüfprogramm

1. **Schadenslokalisierung**: Boden/Luftfahrzeug → Art. II; Weltraum → Art. III
2. **Startstaat bestimmen**: Wer hat gestartet, Startanlage bereitgestellt oder Start aus Gebiet veranlasst?
3. **Mehrere Startstaaten**: Gesamtschuldnerschaft nach Art. V; Ausgleichsregress
4. **Verschuldensnachweis**: Art. III: Telemetrie, Missionslogs, technische Dokumentation sichern
5. **Entlastungscheck**: Art. VI: Hat Geschädigter zum Schaden beigetragen?
6. **Frist**: 1-Jahres-Ausschlussfrist ab Schadenskenntnis; diplomatischen Anspruchsweg vorbereiten
7. **Versicherung**: Deckt nationale Mindestversicherung Haftungsrahmen? Regressvereinbarung vorhanden?

## Normencheck: Schicht für Schicht

### Völkerrecht
- Outer Space Treaty 1967 (OST): Art. I, II, VI, VII, VIII, IX
- Liability Convention 1972 (LIAB): Art. II–V (Haftungsregime)
- Registration Convention 1975 (REG): Registrierungspflichten
- Rescue Agreement 1968 (ARRA): Rettung und Rückgabe
- Ggf. Moon Agreement 1979 (MA): Ressourcen, Umwelt

### EU-Recht
- EU Space Programme Regulation (EU) 2021/696: Galileo, Copernicus, IRIS², SST
- EU Dual-Use-Verordnung (EU) 2021/821: Exportkontrolle Raumfahrtgüter
- NIS2-Richtlinie 2022/2555: Cybersicherheit kritischer Infrastruktur
- DSGVO (EU) 2016/679: Personenbezogene Daten (Erdbeobachtung, Tracking)

### Deutsches Recht
- LuftVG (Luftverkehrsgesetz): https://www.gesetze-im-internet.de/luftvg/
- Geplanter Raumfahrtgesetzentwurf BMWK
- BAFA Exportkontrolle: ITAR-Listung, EAR, EU-Dual-Use
- BSI-Gesetz, KRITIS-Verordnung

### Soft Law und Guidelines
- UNCOPUOS Long-Term Sustainability Guidelines (LTS 2018)
- Artemis Accords (2020, 37+ Unterzeichner)
- IADC Debris Mitigation Guidelines

## Typische Fallen

- **Trümmer sind Weltraumobjekte**: Abgebrannte Raketenstufen, Satelliten-Debris – Startstaat haftet weiterhin
- **Anspruch nur staatlich**: Private müssen ihren Staat einschalten; kein direktes Klagerecht
- **1-Jahres-Frist ist absolut**: Keine Heilung durch spätere Kenntnis; Sorgfaltspflicht bei Schadensdokumentation
- **Versicherungslücke**: Ohne Pflichtversicherung exponiert Betreiber den Staat voll
- **Art. III-Beweislast**: Kollision ohne Verschuldensnachweis – Anspruch scheitert technisch

## Qualitätssicherung

- Keine Scheingenauigkeit: Wenn Normstand, Ratifikationsstatus oder Rechtsprechung unklar sind, Live-Check vorschlagen.
- Quellen nur nach Verifikation zitieren: UNOOSA, EUR-Lex, Gesetze-im-Internet, BAFA, ESA, BNetzA.
- Tatsachen, Annahmen, Wertungen und offene Beweisfragen immer getrennt führen.
- Zuständigkeit, Form, Frist, Beweislast, Vollzug und Rechtsbehelf immer getrennt ausgeben.
- Startstaat, Registerstaat, Betreiber, Missionskontrolle, Versicherer immer separat identifizieren.

## Output-Formate

- Haftungsmatrix (Art. II vs. Art. III, Startstaat, Betreiber, Versicherer)
- Schadensfall-Memo mit Tatbestandsprüfung und Fristen
- Versicherungsanforderungen für Launch Services Agreement
- Staatlicher Regressentwurf gegen privaten Betreiber
- Behördenkommunikation zur Anspruchsanmeldung

## Quellen und Normen

- LIAB 1972: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/liability-convention.html
- OST 1967: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/outerspacetreaty.html
- UNOOSA Vertragsstaaten: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/status/index.html
- ESA Legal Framework: https://www.esa.int/About_Us/Law_at_ESA/ESA_s_legal_framework
- BMWK Weltraumgesetz: https://www.bmwk.de/

---

## Skill: `registrierungsuebereinkommen-register`

_Registration Convention 1975 (REG) – Pflichtregistrierung, UN-Register, nationale Register, Jurisdiktion und Kontrolle im Weltraumrecht._

# Weltraumrecht: Registrierungsübereinkommen: Register, Staat, Zuständigkeit, Kontrolle

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Aufgabe und Einsatzbereich

Bearbeite **Registrierungsübereinkommen: Register, Staat, Zuständigkeit, Kontrolle** im Bereich Weltraumrecht. Er strukturiert die praktische Lage, prüft einschlägige Normen des internationalen und nationalen Rechts und liefert verwertbare Ergebnisse für Betreiber, Behörden, Investoren, Kanzleien und Compliance-Beauftragte.

## Thematischer Kontext

- Registration Convention 1975 (REG) – Pflicht zur Registrierung
- Nationale Register und UN-Register beim Generalsekretär
- Registerstaat = Jurisdiktion und Kontrolle (OST Art. VIII)
- Transfer of Registry und Eigentumswechsel
- Fehlendes deutsches Weltraumregister als Risiko

## Einschlägige Normen und Regelwerke

- **REG Art. I**: Definitionen: Registerstaat, Weltraumobjekt
- **REG Art. II**: Pflicht zur nationalen Registrierung
- **REG Art. III**: Meldung an UN-Generalsekretär mit Pflichtangaben
- **REG Art. IV**: Zeitpunkt: 'as soon as practicable'
- **OST Art. VIII**: Jurisdiktion und Kontrolle beim Registerstaat
- **UNGA Res. 62/101**: Transfer of Registry – Verfahren bei Eigentümer-/Betreiberwechsel

## Kaltstart in 6 Fragen

1. **Rolle**: Wer handelt – Betreiber, Investor, Behörde, Kanzlei, Versicherer, Universität, Verlag, Betroffene?
2. **Aufgabentyp**: Prüfung, Entwurf, Genehmigung, Compliance, Streit, Due Diligence oder Dokumentation?
3. **Unterlagen**: Welche Dokumente liegen vor – Vertrag, Lizenz, Registerauszug, technische Spezifikation, Gutachten, Normtext?
4. **Rechtsordnung**: Deutsches Recht, EU-Recht, US-Recht, Völkerrecht – oder Kombination?
5. **Fristen**: Welche Genehmigungsfristen, ITU-Koordinierungsfristen, Vertragsoptionen oder Behördenfristen laufen?
6. **Ergebnisformat**: Memo, Ampelmatrix, Klauselentwurf, Behördenbrief, Board-Vorlage oder Fristenkalender?

## Prüfprogramm

1. **Registerstaat bestimmen**: Welcher Staat hat gestartet oder veranlasst? Mehrere → Einigung notwendig
2. **Nationaler Register-Check**: Hat Registerstaat ein nationales Register? Ist Objekt eingetragen?
3. **UN-Register-Check**: https://www.unoosa.org/oosa/en/ourwork/spacelaw/registers – Objekt gemeldet?
4. **Pflichtangaben**: Startdatum, Bahnparameter, Funktion – vollständig und aktuell?
5. **Transfer-of-Registry**: Plant Betreiber Eigentümer-/Betreiberwechsel? Resolution 62/101 beachten
6. **Jurisdiktionsfolgen**: Strafrecht, Arbeitsschutz, Produkthaftung an Bord klären
7. **Deorbit-Meldung**: Missionsende → Registeraktualisierung als Best Practice

## Normencheck: Schicht für Schicht

### Völkerrecht
- Outer Space Treaty 1967 (OST): Art. I, II, VI, VII, VIII, IX
- Liability Convention 1972 (LIAB): Art. II–V (Haftungsregime)
- Registration Convention 1975 (REG): Registrierungspflichten
- Rescue Agreement 1968 (ARRA): Rettung und Rückgabe
- Ggf. Moon Agreement 1979 (MA): Ressourcen, Umwelt

### EU-Recht
- EU Space Programme Regulation (EU) 2021/696: Galileo, Copernicus, IRIS², SST
- EU Dual-Use-Verordnung (EU) 2021/821: Exportkontrolle Raumfahrtgüter
- NIS2-Richtlinie 2022/2555: Cybersicherheit kritischer Infrastruktur
- DSGVO (EU) 2016/679: Personenbezogene Daten (Erdbeobachtung, Tracking)

### Deutsches Recht
- LuftVG (Luftverkehrsgesetz): https://www.gesetze-im-internet.de/luftvg/
- Geplanter Raumfahrtgesetzentwurf BMWK
- BAFA Exportkontrolle: ITAR-Listung, EAR, EU-Dual-Use
- BSI-Gesetz, KRITIS-Verordnung

### Soft Law und Guidelines
- UNCOPUOS Long-Term Sustainability Guidelines (LTS 2018)
- Artemis Accords (2020, 37+ Unterzeichner)
- IADC Debris Mitigation Guidelines

## Typische Fallen

- **Doppelregistrierung**: Zwei Startstaaten tragen dasselbe Objekt ein → Jurisdiktionskonflikt
- **Keine Registrierung**: Objekt ohne UN-Meldung unsichtbar; Haftungszuordnung bei Kollision ungeklärt
- **Veraltete Bahnparameter**: Geänderte Umlaufbahn nicht gemeldet → Debris-Tracking erschwert
- **CubeSat-Swarms**: Massenstart mit 100+ Satelliten – Registrierungsaufwand erheblich
- **Nutzlast vs. Träger**: Separate oder kombinierte Registrierung von Trägerrakete und Nutzlast?

## Qualitätssicherung

- Keine Scheingenauigkeit: Wenn Normstand, Ratifikationsstatus oder Rechtsprechung unklar sind, Live-Check vorschlagen.
- Quellen nur nach Verifikation zitieren: UNOOSA, EUR-Lex, Gesetze-im-Internet, BAFA, ESA, BNetzA.
- Tatsachen, Annahmen, Wertungen und offene Beweisfragen immer getrennt führen.
- Zuständigkeit, Form, Frist, Beweislast, Vollzug und Rechtsbehelf immer getrennt ausgeben.
- Startstaat, Registerstaat, Betreiber, Missionskontrolle, Versicherer immer separat identifizieren.

## Output-Formate

- Registerprüfung mit UN-Register-Abgleich
- Registerantrag-Checkliste für Startstaat
- Transfer-of-Registry-Memo
- Jurisdiktionsanalyse für Raumstationen, Nutzlasten, Servicemissionen
- Registerauszug-Zusammenfassung für Due Diligence

## Quellen und Normen

- REG 1975: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/registration-convention.html
- UN-Online-Register: https://www.unoosa.org/oosa/en/ourwork/spacelaw/registers/index.html
- UNGA Res. 62/101: https://www.unoosa.org/res/oosadoc/data/resolutions/2007/general_assembly_62nd_session/res_6262_101_html/A_RES_62_101E.pdf
- OST Art. VIII: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/outerspacetreaty.html
- BMWK Weltraumgesetz: https://www.bmwk.de/

---

## Skill: `outer-space-treaty-grundprinzipien-nichtaneignung`

_OST 1967 – Art. I–IX: Nichtaneignungsprinzip, nationale Verantwortung nichtstaatlicher Akteure, Konsultationspflicht im Weltraumrecht._

# Weltraumrecht: Outer Space Treaty: Grundprinzipien, Nichtaneignung und nationale Verantwortung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Aufgabe und Einsatzbereich

Bearbeite **Outer Space Treaty: Grundprinzipien, Nichtaneignung und nationale Verantwortung** im Bereich Weltraumrecht. Er strukturiert die praktische Lage, prüft einschlägige Normen des internationalen und nationalen Rechts und liefert verwertbare Ergebnisse für Betreiber, Behörden, Investoren, Kanzleien und Compliance-Beauftragte.

## Thematischer Kontext

- Outer Space Treaty 1967 als Grundgesetz des Weltraumrechts
- Art. I: Freiheit der Erkundung und Nutzung für alle Menschheit
- Art. II: Nichtaneignungsprinzip – kein staatlicher Hoheitsanspruch
- Art. VI: Staatliche Verantwortung für nichtstaatliche Akteure (Private)
- Art. VII: Haftung des Startstaats
- Art. VIII: Jurisdiktion und Kontrolle des Registerstaats
- Art. IX: Konsultationspflicht und Planetary Protection

## Einschlägige Normen und Regelwerke

- **OST Art. I**: Weltraum frei für alle; kein nationales Monopol
- **OST Art. II**: Keine Aneignung durch Hoheitsanspruch, Nutzung oder Besetzung
- **OST Art. VI**: Staatliche Verantwortung und Aufsicht über nichtstaatliche Akteure
- **OST Art. VII**: Haftung des Startstaats für Schäden
- **OST Art. VIII**: Jurisdiktion und Kontrolle beim Registerstaat
- **OST Art. IX**: Konsultationspflicht bei schädlicher Beeinflussung
- **US SPACE Act 2015**: Ressourceneigentum ohne Gebietsanspruch
- **LuftVG § 1 Abs. 2**: Notlösung für Weltraumaktivitäten ohne eigenständiges Weltraumgesetz

## Kaltstart in 6 Fragen

1. **Rolle**: Wer handelt – Betreiber, Investor, Behörde, Kanzlei, Versicherer, Universität, Verlag, Betroffene?
2. **Aufgabentyp**: Prüfung, Entwurf, Genehmigung, Compliance, Streit, Due Diligence oder Dokumentation?
3. **Unterlagen**: Welche Dokumente liegen vor – Vertrag, Lizenz, Registerauszug, technische Spezifikation, Gutachten, Normtext?
4. **Rechtsordnung**: Deutsches Recht, EU-Recht, US-Recht, Völkerrecht – oder Kombination?
5. **Fristen**: Welche Genehmigungsfristen, ITU-Koordinierungsfristen, Vertragsoptionen oder Behördenfristen laufen?
6. **Ergebnisformat**: Memo, Ampelmatrix, Klauselentwurf, Behördenbrief, Board-Vorlage oder Fristenkalender?

## Prüfprogramm

1. **Aktivitätskategorie**: Erkundung, Ressourcenextraktion, Kommunikation, Militär, Tourismus bestimmen
2. **Staatsebene**: Welcher Staat ist 'appropriate State' nach Art. VI? Startstaat nach LIAB Art. I lit. c
3. **Nichtaneignungs-Check**: Beinhaltet Aktivität territoriale Ansprüche oder Exklusivrechte?
4. **Ressourcenrecht**: Gilt nationales Ressourcengesetz (US, Luxemburg, VAE)? Widerspruch zu Art. II?
5. **Genehmigungspflicht**: Hat Heimatstaat ein Weltraumgesetz? Was gilt ohne?
6. **Konsultationspflicht**: Könnte Aktivität andere Vertragsstaaten schädlich beeinflussen (Art. IX)?
7. **Haftungskette**: OST Art. VII → LIAB Art. II–V – wer haftet wem gegenüber?

## Normencheck: Schicht für Schicht

### Völkerrecht
- Outer Space Treaty 1967 (OST): Art. I, II, VI, VII, VIII, IX
- Liability Convention 1972 (LIAB): Art. II–V (Haftungsregime)
- Registration Convention 1975 (REG): Registrierungspflichten
- Rescue Agreement 1968 (ARRA): Rettung und Rückgabe
- Ggf. Moon Agreement 1979 (MA): Ressourcen, Umwelt

### EU-Recht
- EU Space Programme Regulation (EU) 2021/696: Galileo, Copernicus, IRIS², SST
- EU Dual-Use-Verordnung (EU) 2021/821: Exportkontrolle Raumfahrtgüter
- NIS2-Richtlinie 2022/2555: Cybersicherheit kritischer Infrastruktur
- DSGVO (EU) 2016/679: Personenbezogene Daten (Erdbeobachtung, Tracking)

### Deutsches Recht
- LuftVG (Luftverkehrsgesetz): https://www.gesetze-im-internet.de/luftvg/
- Geplanter Raumfahrtgesetzentwurf BMWK
- BAFA Exportkontrolle: ITAR-Listung, EAR, EU-Dual-Use
- BSI-Gesetz, KRITIS-Verordnung

### Soft Law und Guidelines
- UNCOPUOS Long-Term Sustainability Guidelines (LTS 2018)
- Artemis Accords (2020, 37+ Unterzeichner)
- IADC Debris Mitigation Guidelines

## Typische Fallen

- **Private ≠ Staat**: Art. II bindet nur Staaten; Private können nach nationalem Recht Ressourceneigentum erwerben
- **Mehrfache Startstaaten**: Gesamtschuldnerschaft bei internationalem Start; Versicherungskoordination notwendig
- **Fehlende Aufsicht**: Art. VI verlangt 'continuing supervision' – ohne Weltraumgesetz schutzlos exponiert
- **Soft Law ≠ Bindung**: Artemis Accords, COPUOS-Guidelines sind kein Vertragsrecht
- **Historische Auslegung**: OST wurde für staatliche Raumfahrt entworfen; NewSpace fällt in Regelungslücken

## Qualitätssicherung

- Keine Scheingenauigkeit: Wenn Normstand, Ratifikationsstatus oder Rechtsprechung unklar sind, Live-Check vorschlagen.
- Quellen nur nach Verifikation zitieren: UNOOSA, EUR-Lex, Gesetze-im-Internet, BAFA, ESA, BNetzA.
- Tatsachen, Annahmen, Wertungen und offene Beweisfragen immer getrennt führen.
- Zuständigkeit, Form, Frist, Beweislast, Vollzug und Rechtsbehelf immer getrennt ausgeben.
- Startstaat, Registerstaat, Betreiber, Missionskontrolle, Versicherer immer separat identifizieren.

## Output-Formate

- OST-Normanalyse mit Artikel-zu-Artikel-Prüfung
- Nichtaneignungs-Gutachten für Ressourcenprojekte
- Genehmigungsfahrplan für nichtstaatliche Betreiber (Art. VI)
- Haftungsmemo Startstaat / Registerstaat / Betreiber
- Vertragsklausel zur OST-Compliance (Art. VI/VIII)

## Quellen und Normen

- OST 1967: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/outerspacetreaty.html
- UNOOSA Vertragsstaaten: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/status/index.html
- US SPACE Act 2015: https://www.congress.gov/bill/114th-congress/house-bill/2262
- Luxemburger Space Resources Law: https://gouvernement.lu/en/actualites/toutes_actualites/communiques/2017/07-juillet/14-loi-espace.html
- LuftVG: https://www.gesetze-im-internet.de/luftvg/
- UNOOSA COPUOS: https://www.unoosa.org/oosa/en/ourwork/copuos/index.html

---

## Skill: `starlink-oneweb-iris2-und-oeffentliche-beschaffung`

_Starlink, OneWeb, IRIS² – öffentliche Beschaffung, Sicherheitsanforderungen, Vergaberecht und strategische Autonomie im Weltraumrecht._

# Weltraumrecht: Starlink, OneWeb, IRIS² und öffentliche Beschaffung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Aufgabe und Einsatzbereich

Bearbeite das Thema **Starlink, OneWeb, IRIS² und öffentliche Beschaffung** im Bereich Weltraumrecht und Raumfahrtrecht. Er strukturiert die praktische Lage, identifiziert einschlägige Normen des internationalen, europäischen und deutschen Rechts und liefert verwertbare Ergebnisse für Betreiber, Behörden, Investoren, Kanzleien und Compliance-Beauftragte.

## Thematischer Schwerpunkt

Das Rechtsgebiet berührt folgende Kernthemen: Satelliteninternet-Dienste (LEO-Konstellationen). Relevante Normen: Vergaberecht, Sicherheitsanforderungen, strategische Autonomie.

## Kaltstart in 6 Fragen

1. **Rolle**: Wer handelt – Betreiber, Investor, Behörde, Kanzlei, Versicherer, Universität, Verlag oder Betroffene?
2. **Aufgabentyp**: Geht es um Prüfung, Entwurf, Genehmigung, Compliance, Streitbeilegung, Due Diligence oder Dokumentation?
3. **Unterlagen**: Welche Dokumente liegen vor – Vertrag, Lizenz, Registerauszug, technische Spezifikation, Gutachten, Normtext?
4. **Rechtsordnung**: Deutsches Recht, EU-Recht, US-Recht, Völkerrecht – einzeln oder kombiniert?
5. **Fristen**: Welche Genehmigungsfristen, ITU-Koordinierungsfristen, Vertragsoptionen oder Behördenfristen laufen aktuell?
6. **Ergebnisformat**: Memo, Ampelmatrix, Klauselentwurf, Behördenbrief, Board-Vorlage, Fristenkalender oder Checkliste?

## Einschlägige Normen und Regelwerke

### Internationales Weltraumrecht
- **OST 1967** Art. I–IX: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/outerspacetreaty.html
- **Liability Convention 1972** Art. II–V: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/liability-convention.html
- **Registration Convention 1975**: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/registration-convention.html
- **Rescue Agreement 1968**: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/rescueagreement.html
- **UNCOPUOS LTS Guidelines 2018**: https://www.unoosa.org/oosa/en/ourwork/topics/long-term-sustainability-of-outer-space-activities.html
- **Artemis Accords 2020**: https://www.nasa.gov/artemis-accords/

### EU-Recht
- **EU Space Programme Regulation (EU) 2021/696**: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0696
- **EU Dual-Use-Verordnung (EU) 2021/821**: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821
- **NIS2-Richtlinie 2022/2555**: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2555
- **DSGVO (EU) 2016/679**: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679

### Deutsches Recht
- **LuftVG**: https://www.gesetze-im-internet.de/luftvg/
- **BAFA Exportkontrolle / AWG**: https://www.bafa.de/DE/Aussenwirtschaft/Exportkontrolle/exportkontrolle_node.html
- **BNetzA Frequenzrecht**: https://www.bundesnetzagentur.de/DE/Fachthemen/Telekommunikation/Frequenzen/start.html
- **Raumfahrtgesetzentwurf BMWK**: https://www.bmwk.de/

## Prüfprogramm

1. **Sachverhaltserfassung**: Tatsachen von Annahmen und Wertungen trennen; offene Beweisfragen notieren.
2. **Normenebene bestimmen**: Völkerrecht (OST, LIAB, REG) → EU-Recht → deutsches Recht → Soft Law.
3. **Startstaat/Registerstaat/Betreiber trennen**: Jeder Akteur hat unterschiedliche Rechte und Pflichten.
4. **Genehmigungsebene prüfen**: Welche Behörde (BMWK, DLR, BNetzA, BAFA, LBA) ist zuständig?
5. **Haftungsebene**: LIAB-Regime (absolut am Boden, Verschulden im All); Versicherungsdeckung prüfen.
6. **Exportkontrolle**: ITAR/EAR/EU-Dual-Use; BAFA-Genehmigungspflicht für technische Unterlagen?
7. **Fristen kalendarisieren**: ITU-Koordinierung (3–7 Jahre), nationale Genehmigungsfristen, Vertragsoptionen.
8. **Cybersecurity und Datenschutz**: NIS2, BSI-KRITIS, DSGVO – soweit einschlägig.
9. **Quellenverifikation**: Nur UNOOSA, EUR-Lex, Gesetze-im-Internet, BAFA, ESA, BNetzA als Primärquellen.
10. **Ergebnis strukturieren**: Zuständigkeit, Form, Frist, Beweislast, Vollzug und Rechtsbehelf getrennt ausgeben.

## Typische Fallen

- **Fehlende Gesetzesgrundlage**: Deutschland hat kein eigenständiges Weltraumgesetz; LuftVG-Analogie ist unsicher.
- **Mehrfachzuständigkeit**: BMWK, DLR, BNetzA, BAFA, Landesbehörden – Koordinationsaufwand unterschätzt.
- **ITAR als Überraschung**: US-Technologieanteile können Exportkontrolle auf gesamten Satelliten ausdehnen.
- **ITU-Fristen**: Frequenzanmeldung muss 3–7 Jahre vor Start beginnen; zu spätes Handeln kann Mission blockieren.
- **Soft Law ≠ Bindung**: UNCOPUOS LTS Guidelines, Artemis Accords, IADC Debris Mitigation sind Empfehlungen.
- **Staatshaftungsrisiko ohne Regress**: Ohne Weltraumgesetz kann Staat Haftung nach LIAB nicht an Betreiber weiterreichen.
- **Keine Scheingenauigkeit**: Wenn Normstand, Ratifikationsstatus oder Rechtsprechung unklar sind, Live-Check formulieren.
- **Jurisdiktionskonflikt**: Registerstaat, Tätigkeitsstaat und Geschädigter-Staat können verschiedene Rechtsordnungen beanspruchen.

## Qualitätssicherung

- Tatsachen, Annahmen, Wertungen und offene Beweisfragen immer getrennt führen.
- Zuständigkeit, Form, Frist, Beweislast, Vollzug und Rechtsbehelf immer getrennt ausgeben.
- Startstaat, Registerstaat, Betreiber, Missionskontrolle und Versicherer immer separat identifizieren.
- Quellen nur nach Verifikation zitieren; keine Sekundärbehauptungen ohne Primärquellencheck.
- Bei fehlendem Normstand oder unklarer Rechtsprechung: Live-Check als nächsten Schritt formulieren.
- Operative Handlungsempfehlung immer mitliefern; juristisch korrekte Antwort ohne Handlungsorientierung ist ungenügend.

## Output-Formate

- **Rechtsgutachten / Legal Opinion** mit normierten Prüfungsschritten
- **Ampelmatrix / Risikocockpit** mit Handlungsempfehlungen
- **Genehmigungsfahrplan** mit Behörden und Fristen
- **Vertragsklausel-Entwurf** für einschlägige Vertragstypen
- **Behördenbrief / Antragsschreiben** an BMWK, BNetzA, BAFA
- **Board-Memo** für Entscheidungsgremien
- **Compliance-Checkliste** für laufenden Betrieb
- **Fristenkalender** mit ITU, Genehmigung, Versicherung, Vertragsoptionen

## Quellen und Normen

- OST 1967: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/outerspacetreaty.html
- LIAB 1972: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/liability-convention.html
- REG 1975: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/registration-convention.html
- ARRA 1968: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/rescueagreement.html
- EU Space Programme Regulation: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0696
- EU Dual-Use-VO: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821
- NIS2: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2555
- LuftVG: https://www.gesetze-im-internet.de/luftvg/
- BAFA: https://www.bafa.de/DE/Aussenwirtschaft/Exportkontrolle/exportkontrolle_node.html
- ESA Legal Framework: https://www.esa.int/About_Us/Law_at_ESA/ESA_s_legal_framework
- UNOOSA: https://www.unoosa.org/
- BNetzA: https://www.bundesnetzagentur.de/DE/Fachthemen/Telekommunikation/Frequenzen/start.html
- ITU Radio Regulations: https://www.itu.int/en/ITU-R/terrestrial/broadcast/Pages/Regulations.aspx

---

## Skill: `astronautenrettung-rueckgabe-und-statusfragen`

_Rescue Agreement 1968 – Rettungs- und Rückgabepflicht, Botschafter der Menschheit, Status kommerzieller Raumfahrer im Weltraumrecht._

# Weltraumrecht: Astronautenrettung: Rückgabe und Statusfragen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Aufgabe und Einsatzbereich

Bearbeite **Astronautenrettung: Rückgabe und Statusfragen** im Bereich Weltraumrecht. Er strukturiert die praktische Lage, prüft einschlägige Normen des internationalen und nationalen Rechts und liefert verwertbare Ergebnisse für Betreiber, Behörden, Investoren, Kanzleien und Compliance-Beauftragte.

## Thematischer Kontext

- Rescue Agreement 1968 (ARRA) – völkerrechtliche Rettungspflicht
- Rückgabepflicht für Astronauten und Weltraumobjekte
- Status kommerzieller Raumfahrerinnen (Spaceflight Participants)
- ISS-Sonderregeln (IGA 1998) und Evakuierungspläne
- Kostenerstattung und Exportkontrolle bei Rettungsausrüstung

## Einschlägige Normen und Regelwerke

- **ARRA Art. 1**: Notlandesituation: Meldepflicht an Startstaat und UN-Generalsekretär
- **ARRA Art. 2**: Rettungspflicht auf eigenem Gebiet und hoher See
- **ARRA Art. 3**: Rückgabepflicht: unverzüglich und sicher
- **ARRA Art. 4**: Rückgabe von Weltraumobjekten; Kostenerstattung
- **ISS IGA 1998**: Detaillierte Rettungs- und Evakuierungsregelungen für ISS
- **FAA Commercial Space**: Begriff 'Spaceflight Participant' vs. 'Crew' vs. 'Astronaut'

## Kaltstart in 6 Fragen

1. **Rolle**: Wer handelt – Betreiber, Investor, Behörde, Kanzlei, Versicherer, Universität, Verlag, Betroffene?
2. **Aufgabentyp**: Prüfung, Entwurf, Genehmigung, Compliance, Streit, Due Diligence oder Dokumentation?
3. **Unterlagen**: Welche Dokumente liegen vor – Vertrag, Lizenz, Registerauszug, technische Spezifikation, Gutachten, Normtext?
4. **Rechtsordnung**: Deutsches Recht, EU-Recht, US-Recht, Völkerrecht – oder Kombination?
5. **Fristen**: Welche Genehmigungsfristen, ITU-Koordinierungsfristen, Vertragsoptionen oder Behördenfristen laufen?
6. **Ergebnisformat**: Memo, Ampelmatrix, Klauselentwurf, Behördenbrief, Board-Vorlage oder Fristenkalender?

## Prüfprogramm

1. **Notlandungsort**: Eigenem Staatsgebiet, Ausland, hohe See, Antarktis – unterschiedliche Regime
2. **Staatsangehörigkeit**: Startstaat und Wohnsitzstaat klären; Kooperationspflichten bestimmen
3. **Statusklärung**: Astronaut, Crew oder Spaceflight Participant? Vertragsregelung prüfen
4. **Rettungskosten**: Wer trägt Kosten? Kostenerstattungsvereinbarung mit Startstaat vorhanden?
5. **Weltraumobjekte**: Trümmer mitgelandet? Rückgabe- und Entsorgungsanweisungen klären
6. **ISS-Sonderregeln**: IGA 1998 und NASA-Notfallplan bei ISS-Vorfällen konsultieren

## Normencheck: Schicht für Schicht

### Völkerrecht
- Outer Space Treaty 1967 (OST): Art. I, II, VI, VII, VIII, IX
- Liability Convention 1972 (LIAB): Art. II–V (Haftungsregime)
- Registration Convention 1975 (REG): Registrierungspflichten
- Rescue Agreement 1968 (ARRA): Rettung und Rückgabe
- Ggf. Moon Agreement 1979 (MA): Ressourcen, Umwelt

### EU-Recht
- EU Space Programme Regulation (EU) 2021/696: Galileo, Copernicus, IRIS², SST
- EU Dual-Use-Verordnung (EU) 2021/821: Exportkontrolle Raumfahrtgüter
- NIS2-Richtlinie 2022/2555: Cybersicherheit kritischer Infrastruktur
- DSGVO (EU) 2016/679: Personenbezogene Daten (Erdbeobachtung, Tracking)

### Deutsches Recht
- LuftVG (Luftverkehrsgesetz): https://www.gesetze-im-internet.de/luftvg/
- Geplanter Raumfahrtgesetzentwurf BMWK
- BAFA Exportkontrolle: ITAR-Listung, EAR, EU-Dual-Use
- BSI-Gesetz, KRITIS-Verordnung

### Soft Law und Guidelines
- UNCOPUOS Long-Term Sustainability Guidelines (LTS 2018)
- Artemis Accords (2020, 37+ Unterzeichner)
- IADC Debris Mitigation Guidelines

## Typische Fallen

- **Tourismusstatus**: Kein klarer ARRA-Schutz für Passagiere ohne spezifische Vereinbarung
- **Souveränitätskonflikte**: Rettungsmaßnahmen auf fremdem Staatsgebiet können Souveränitätsfragen aufwerfen
- **Kosten ohne Vereinbarung**: Ohne vorab vereinbarte Kostenerstattungsklausel entstehen Streitigkeiten
- **Gefährliche Trümmer**: Nuklear/biologisch kontaminierte Objekte: Startstaat gibt Anweisungen, kein Selbsttätigwerden
- **ITAR-Kommunikationsgeräte**: Rettungskoordination kann durch US-Exportkontrolle gehindert werden

## Qualitätssicherung

- Keine Scheingenauigkeit: Wenn Normstand, Ratifikationsstatus oder Rechtsprechung unklar sind, Live-Check vorschlagen.
- Quellen nur nach Verifikation zitieren: UNOOSA, EUR-Lex, Gesetze-im-Internet, BAFA, ESA, BNetzA.
- Tatsachen, Annahmen, Wertungen und offene Beweisfragen immer getrennt führen.
- Zuständigkeit, Form, Frist, Beweislast, Vollzug und Rechtsbehelf immer getrennt ausgeben.
- Startstaat, Registerstaat, Betreiber, Missionskontrolle, Versicherer immer separat identifizieren.

## Output-Formate

- Rettungsprotokoll-Checkliste für Missionskontrolle
- Status-Memo für kommerzielle Raumfahrerinnen
- Kostenerstattungsklausel für Launch Services Agreement
- IGA/MOU-Analyse für ISS-Missionen
- Behördenkommunikations-Vorlage (ARRA Art. 1 Meldung)

## Quellen und Normen

- ARRA 1968: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/rescueagreement.html
- ISS IGA 1998: https://www.nasa.gov/mission_pages/station/structure/elements/iss_agreement.html
- FAA Commercial Space: https://www.faa.gov/space
- ESA ISS Framework: https://www.esa.int/About_Us/Law_at_ESA/ESA_s_legal_framework
- LuftVG: https://www.gesetze-im-internet.de/luftvg/

---

## Skill: `frequenzzuteilung-itu-erdbeobachtung`

_Frequenzzuteilung für Satelliten – ITU Radio Regulations, BNetzA-Verfahren, Koordinierung, Interferenz-Beschwerden im Weltraumrecht._

# Weltraumrecht: Frequenzzuteilung: ITU, Bundesnetzagentur und Interferenz

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Aufgabe und Einsatzbereich

Bearbeite das Thema **Frequenzzuteilung: ITU, Bundesnetzagentur und Interferenz** im Bereich Weltraumrecht und Raumfahrtrecht. Er strukturiert die praktische Lage, identifiziert einschlägige Normen des internationalen, europäischen und deutschen Rechts und liefert verwertbare Ergebnisse für Betreiber, Behörden, Investoren, Kanzleien und Compliance-Beauftragte.

## Thematischer Schwerpunkt

Das Rechtsgebiet berührt folgende Kernthemen: ITU-Frequenzkoordination, BNetzA-Zuteilung, Interferenz-Beschwerden. Relevante Normen: ITU Radio Regulations, TKG, BNetzA-Frequenzplan.

## Kaltstart in 6 Fragen

1. **Rolle**: Wer handelt – Betreiber, Investor, Behörde, Kanzlei, Versicherer, Universität, Verlag oder Betroffene?
2. **Aufgabentyp**: Geht es um Prüfung, Entwurf, Genehmigung, Compliance, Streitbeilegung, Due Diligence oder Dokumentation?
3. **Unterlagen**: Welche Dokumente liegen vor – Vertrag, Lizenz, Registerauszug, technische Spezifikation, Gutachten, Normtext?
4. **Rechtsordnung**: Deutsches Recht, EU-Recht, US-Recht, Völkerrecht – einzeln oder kombiniert?
5. **Fristen**: Welche Genehmigungsfristen, ITU-Koordinierungsfristen, Vertragsoptionen oder Behördenfristen laufen aktuell?
6. **Ergebnisformat**: Memo, Ampelmatrix, Klauselentwurf, Behördenbrief, Board-Vorlage, Fristenkalender oder Checkliste?

## Einschlägige Normen und Regelwerke

### Internationales Weltraumrecht
- **OST 1967** Art. I–IX: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/outerspacetreaty.html
- **Liability Convention 1972** Art. II–V: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/liability-convention.html
- **Registration Convention 1975**: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/registration-convention.html
- **Rescue Agreement 1968**: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/rescueagreement.html
- **UNCOPUOS LTS Guidelines 2018**: https://www.unoosa.org/oosa/en/ourwork/topics/long-term-sustainability-of-outer-space-activities.html
- **Artemis Accords 2020**: https://www.nasa.gov/artemis-accords/

### EU-Recht
- **EU Space Programme Regulation (EU) 2021/696**: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0696
- **EU Dual-Use-Verordnung (EU) 2021/821**: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821
- **NIS2-Richtlinie 2022/2555**: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2555
- **DSGVO (EU) 2016/679**: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679

### Deutsches Recht
- **LuftVG**: https://www.gesetze-im-internet.de/luftvg/
- **BAFA Exportkontrolle / AWG**: https://www.bafa.de/DE/Aussenwirtschaft/Exportkontrolle/exportkontrolle_node.html
- **BNetzA Frequenzrecht**: https://www.bundesnetzagentur.de/DE/Fachthemen/Telekommunikation/Frequenzen/start.html
- **Raumfahrtgesetzentwurf BMWK**: https://www.bmwk.de/

## Prüfprogramm

1. **Sachverhaltserfassung**: Tatsachen von Annahmen und Wertungen trennen; offene Beweisfragen notieren.
2. **Normenebene bestimmen**: Völkerrecht (OST, LIAB, REG) → EU-Recht → deutsches Recht → Soft Law.
3. **Startstaat/Registerstaat/Betreiber trennen**: Jeder Akteur hat unterschiedliche Rechte und Pflichten.
4. **Genehmigungsebene prüfen**: Welche Behörde (BMWK, DLR, BNetzA, BAFA, LBA) ist zuständig?
5. **Haftungsebene**: LIAB-Regime (absolut am Boden, Verschulden im All); Versicherungsdeckung prüfen.
6. **Exportkontrolle**: ITAR/EAR/EU-Dual-Use; BAFA-Genehmigungspflicht für technische Unterlagen?
7. **Fristen kalendarisieren**: ITU-Koordinierung (3–7 Jahre), nationale Genehmigungsfristen, Vertragsoptionen.
8. **Cybersecurity und Datenschutz**: NIS2, BSI-KRITIS, DSGVO – soweit einschlägig.
9. **Quellenverifikation**: Nur UNOOSA, EUR-Lex, Gesetze-im-Internet, BAFA, ESA, BNetzA als Primärquellen.
10. **Ergebnis strukturieren**: Zuständigkeit, Form, Frist, Beweislast, Vollzug und Rechtsbehelf getrennt ausgeben.

## Typische Fallen

- **Fehlende Gesetzesgrundlage**: Deutschland hat kein eigenständiges Weltraumgesetz; LuftVG-Analogie ist unsicher.
- **Mehrfachzuständigkeit**: BMWK, DLR, BNetzA, BAFA, Landesbehörden – Koordinationsaufwand unterschätzt.
- **ITAR als Überraschung**: US-Technologieanteile können Exportkontrolle auf gesamten Satelliten ausdehnen.
- **ITU-Fristen**: Frequenzanmeldung muss 3–7 Jahre vor Start beginnen; zu spätes Handeln kann Mission blockieren.
- **Soft Law ≠ Bindung**: UNCOPUOS LTS Guidelines, Artemis Accords, IADC Debris Mitigation sind Empfehlungen.
- **Staatshaftungsrisiko ohne Regress**: Ohne Weltraumgesetz kann Staat Haftung nach LIAB nicht an Betreiber weiterreichen.
- **Keine Scheingenauigkeit**: Wenn Normstand, Ratifikationsstatus oder Rechtsprechung unklar sind, Live-Check formulieren.
- **Jurisdiktionskonflikt**: Registerstaat, Tätigkeitsstaat und Geschädigter-Staat können verschiedene Rechtsordnungen beanspruchen.

## Qualitätssicherung

- Tatsachen, Annahmen, Wertungen und offene Beweisfragen immer getrennt führen.
- Zuständigkeit, Form, Frist, Beweislast, Vollzug und Rechtsbehelf immer getrennt ausgeben.
- Startstaat, Registerstaat, Betreiber, Missionskontrolle und Versicherer immer separat identifizieren.
- Quellen nur nach Verifikation zitieren; keine Sekundärbehauptungen ohne Primärquellencheck.
- Bei fehlendem Normstand oder unklarer Rechtsprechung: Live-Check als nächsten Schritt formulieren.
- Operative Handlungsempfehlung immer mitliefern; juristisch korrekte Antwort ohne Handlungsorientierung ist ungenügend.

## Output-Formate

- **Rechtsgutachten / Legal Opinion** mit normierten Prüfungsschritten
- **Ampelmatrix / Risikocockpit** mit Handlungsempfehlungen
- **Genehmigungsfahrplan** mit Behörden und Fristen
- **Vertragsklausel-Entwurf** für einschlägige Vertragstypen
- **Behördenbrief / Antragsschreiben** an BMWK, BNetzA, BAFA
- **Board-Memo** für Entscheidungsgremien
- **Compliance-Checkliste** für laufenden Betrieb
- **Fristenkalender** mit ITU, Genehmigung, Versicherung, Vertragsoptionen

## Quellen und Normen

- OST 1967: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/outerspacetreaty.html
- LIAB 1972: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/liability-convention.html
- REG 1975: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/registration-convention.html
- ARRA 1968: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/rescueagreement.html
- EU Space Programme Regulation: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0696
- EU Dual-Use-VO: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821
- NIS2: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2555
- LuftVG: https://www.gesetze-im-internet.de/luftvg/
- BAFA: https://www.bafa.de/DE/Aussenwirtschaft/Exportkontrolle/exportkontrolle_node.html
- ESA Legal Framework: https://www.esa.int/About_Us/Law_at_ESA/ESA_s_legal_framework
- UNOOSA: https://www.unoosa.org/
- BNetzA: https://www.bundesnetzagentur.de/DE/Fachthemen/Telekommunikation/Frequenzen/start.html
- ITU Radio Regulations: https://www.itu.int/en/ITU-R/terrestrial/broadcast/Pages/Regulations.aspx

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

