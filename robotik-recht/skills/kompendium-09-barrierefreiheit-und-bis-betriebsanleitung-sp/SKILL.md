---
name: kompendium-09-barrierefreiheit-und-bis-betriebsanleitung-sp
description: "robotik-recht: Konsolidiertes Skill-Kompendium 09; bündelt 6 frühere Spezialskills (barrierefreiheit-und-inklusion-robotik, batterie-ladeinfrastruktur-und-brandschutz, bau-und-inspektionsroboter, beschaeftigtendatenschutz-cobot, betreiber-mitverschulden-und-fehlbedienung und 1 weitere) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 09 - robotik-recht

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `barrierefreiheit-und-inklusion-robotik` | Prüft Barrierefreiheit, Inklusion und diskriminierungsarme Bedienung bei Robotikprodukten und Nutzerinterfaces. |
| `batterie-ladeinfrastruktur-und-brandschutz` | Prüft Batterie, Ladeinfrastruktur, Brandschutz, Transport, Lagerung, Rückruf und Versicherungsfragen bei mobilen Robotern. |
| `bau-und-inspektionsroboter` | Prüft Bau-, Inspektions- und Wartungsroboter: Baustelle, Arbeitsschutz, Drittschäden, Betreiberorganisation und Beweissicherung. |
| `beschaeftigtendatenschutz-cobot` | Prüft Beschäftigtendatenschutz bei Cobots: Leistungsdaten, Standort, Video, Betriebsrat, Zweckbindung und Löschfristen. |
| `betreiber-mitverschulden-und-fehlbedienung` | Prüft Betreiber-Mitverschulden: missachtete Anleitung, fehlende Wartung, Umgehung von Schutzfunktionen, Schulungslücken und Logspuren. |
| `betriebsanleitung-sprache-und-warnhinweise` | Prüft Betriebsanleitung, Sicherheitsinformationen, digitale Anleitung, Sprache, Restgefahren und Verständlichkeit für Zielgruppen. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `barrierefreiheit-und-inklusion-robotik`

**Frühere Beschreibung:** Prüft Barrierefreiheit, Inklusion und diskriminierungsarme Bedienung bei Robotikprodukten und Nutzerinterfaces.

# Barrierefreiheit und Inklusion bei Robotern

## Fachkern: Barrierefreiheit und Inklusion bei Robotern
- **Spezialgegenstand:** Barrierefreiheit und Inklusion bei Robotern wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Service-, Pflege-, Liefer- und Empfangsroboter interagieren mit Menschen unterschiedlicher Fähigkeiten. Das BFSG (Barrierefreiheitsstärkungsgesetz, Umsetzung der EU-RL 2019/882) verlangt seit 28.06.2025 von Herstellern und Dienstleistern bestimmter Produkte und Dienstleistungen Barrierefreiheit. Ergänzt durch das AGG bei Diskriminierung in der Bedienung und durch Art. 5 KI-VO (verbotene Praktiken bei Ausnutzung von Verletzlichkeiten). Dieser Skill prüft Robotikprodukte und ihre Nutzerinterfaces (UI/UX, Sprache, Höhe, Sensorik) auf Barrierefreiheit und Diskriminierungsarmut.

## Wann brauchen Sie diesen Skill / Kaltstart-Fragen

1. **Rolle:** Hersteller eines Roboters mit Endkundenkontakt, Dienstleister mit Robotereinsatz im Publikumsverkehr, Behindertenverband, Antidiskriminierungsstelle.
2. **Produkt:** Pflege-, Service-, Empfangs-, Lieferroboter, Selbstbedienungsterminals mit Robotik-Bestandteilen, Bankautomaten mit Sprachausgabe.
3. **Zielgruppe:** Endverbraucher, Patienten, Mitarbeiter, Schüler, ältere Personen, Menschen mit Sinnes- oder kognitiven Einschränkungen.
4. **Anlass:** Markteinführung, Aufsichtsanfrage Marktüberwachungsbehörde (BMAS), Beschwerde, AGG-Mahnschreiben.
5. **Unterlagen:** Bedienkonzept, UI-Mockups, Sprachausgabe-Skripte, Sensorhöhen, Nutzerstudien.

## Rechtlicher Rahmen

- **BFSG** § 1, § 3: erfasst u. a. Selbstbedienungsterminals, Hardware-Systeme für Verbraucher mit interaktiver Funktion; Pflicht: Wahrnehmbarkeit, Bedienbarkeit, Verständlichkeit, Robustheit (BFSGV); Geltung seit 28.06.2025.
- **EU-RL 2019/882** (European Accessibility Act), national umgesetzt durch BFSG.
- **BFSGV** Anhang 1 detaillierte Anforderungen.
- **EN 301 549** harmonisierte Norm IKT-Barrierefreiheit (zuletzt überarbeitet 2024).
- **AGG** §§ 1, 2 Abs. 1 Nr. 8, 19, 20: Massengeschäfte, Diskriminierung in der Bedienung.
- **KI-VO** Art. 5 Abs. 1 lit. b: Verbot der Ausnutzung der Verletzlichkeit aufgrund Alters, Behinderung, sozialer/wirtschaftlicher Lage.
- **MaschinenVO** VO (EU) 2023/1230 Anhang III Nr. 1.1.6 Ergonomie.
- **UN-BRK** Art. 9 (Zugänglichkeit).

## Workflow Schritt für Schritt

1. **Anwendungsbereich BFSG prüfen.** Verbraucherrobotik oder gewerblich? Übergangsregelungen für Bestandsprodukte beachten.
2. **Wahrnehmbarkeit.** Mehrkanalige Ausgabe (visuell + akustisch + ggf. taktil); Kontraste mindestens WCAG AA; Schriftgrößen skalierbar; Sprachausgabe in Standardsprache.
3. **Bedienbarkeit.** Bedienelemente in Reichweite (Rollstuhl: 80-110 cm Greifhöhe); Tasten taktil unterscheidbar; keine reinen Touch-Interfaces ohne Sprach-Alternative.
4. **Verständlichkeit.** Leichte Sprache; Symbole genormt (DIN 32976, ISO 7001); Vorlesefunktion.
5. **Robustheit.** Kompatibilität mit Hilfsmitteln (Hörgeräte, Screenreader bei vorhandenen Bildschirmen).
6. **KI-VO Art. 5 Check.** Erkennt das System Schutzbedürftigkeit und beeinflusst es das Verhalten? Sprachdialoge auf manipulative Muster prüfen.
7. **Diskriminierungs-Audit.** Spracherkennung über Dialekte, Hautfarben-Erkennung in Kameras (Bias-Test), Personenerkennung im Rollstuhl.
8. **Nutzerstudien** mit Betroffenenverbänden; Iteration.
9. **Konformitätserklärung BFSG**; Marktüberwachung über die zuständigen Landesbehörden.

## Trade-off-Matrix

| Anforderung | Strenge Auslegung | Pragmatik | Empfehlung |
|---|---|---|---|
| Sprachausgabe + Display | beides immer | nur wenn Hauptkanal | beides bei Verbraucherrobotern Standard |
| Höhenverstellbare Bedienoberfläche | mechanisch | nur Software-Anpassung | mindestens Software-Skalierung; mechanisch wenn machbar |
| Leichte Sprache | überall | nur Pflichtinformationen | Pflichtinformationen + häufige Dialoge in leichter Sprache |
| Bias-Tests | breit | nur Hauptmerkmale | Test gegen Trainings-/Test-Disjunktion mit demografisch ausgewogenem Set |

## Praxistipps

- **Co-Design** mit Behindertenverbänden früh, nicht erst zum Test.
- **Falsch-Positiv-Bias** der Personenerkennung dokumentieren – sonst KI-VO/AGG-Risiko.
- **Sturzgefahr** durch Roboter im Bewegungsraum berücksichtigen (Sehbehinderung).
- **Sprachbefehle** als gleichwertige Alternative zur Touch-Bedienung.
- **Hörgerätekompatibel**: Induktionsschleife oder Bluetooth-LE-Audio.

## Mustertexte

**Auszug Konformitätserklärung BFSG:**

> Der Hersteller [Firma] erklärt, dass das Produkt [Modell, Seriennummer] die Anforderungen des BFSG und der BFSGV erfüllt. Angewandte Normen: EN 301 549:2024, DIN EN 17161. Die technische Dokumentation wird gemäß § 23 BFSG zehn Jahre vorgehalten.

**UI-Designprinzip (Auszug Spezifikation):**

> Alle sicherheitsrelevanten Bestätigungen erfolgen sowohl visuell (Kontrast 7:1) als auch akustisch (Sprachausgabe, Lautstärke vom Nutzer einstellbar). Sprachdialoge werden in deutscher Standard- und leichter Sprache angeboten. Reaktionszeit-Erwartungen werden nicht durch zeitliche Drucksetzung (Countdown) erzwungen – Nutzer mit motorischen Einschränkungen erhalten mindestens das Dreifache der Standardzeit.

## Typische Fehler

- **Reine Touch-UI** ohne haptische/sprachliche Alternative.
- **KI-Spracherkennung** nur auf Standardsprache trainiert.
- **Höhenfixierung** der Bedienoberfläche zu hoch für Rollstuhlfahrer.
- **Personenerkennung** bricht bei Rollstuhl- oder Rollator-Nutzern.
- **AGG-Risiko**: Roboter ignoriert Personen aufgrund von Größe oder Hautfarbe (Bias).

## Querverweise

- `datensatzqualitaet-und-bias-hri`
- `betriebsanleitung-sprache-und-warnhinweise`
- `biometrie-emotion-und-personenerkennung`

## Quellen Stand 06/2026

- BFSG; BFSGV.
- RL (EU) 2019/882.
- EN 301 549:2024; DIN EN 17161.
- VO (EU) 2024/1689 (KI-VO), Art. 5.
- AGG §§ 1, 19, 20.
- UN-BRK Art. 9.
- Live-Verifikation auf bmas.de, eur-lex.europa.eu, antidiskriminierungsstelle.de; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.

## 2. `batterie-ladeinfrastruktur-und-brandschutz`

**Frühere Beschreibung:** Prüft Batterie, Ladeinfrastruktur, Brandschutz, Transport, Lagerung, Rückruf und Versicherungsfragen bei mobilen Robotern.

# Batterie, Ladeinfrastruktur und Brandschutz bei mobilen Robotern

## Fachkern: Batterie, Ladeinfrastruktur und Brandschutz bei mobilen Robotern
- **Spezialgegenstand:** Batterie, Ladeinfrastruktur und Brandschutz bei mobilen Robotern wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Mobile Roboter (AMR, AGV, Liefer-, Reinigungs-, Mähroboter) werden überwiegend mit Lithium-Ionen-Akkus betrieben. Die Folge: erhebliche Anforderungen aus der Batterie-VO (EU) 2023/1542, dem Gefahrgutrecht (ADR/UN 38.3), dem vorbeugenden Brandschutz (Landesbauordnungen, Sachversicherer-Bedingungen VdS), der ProdSG/MaschinenVO sowie spezifische Pflichten bei Rückruf und Versicherung. Dieser Skill ordnet die Schichten und gibt praxisnahe Vorlagen für Lagerkonzept und Rückruf.

## Wann brauchen Sie diesen Skill / Kaltstart-Fragen

1. **Rolle:** Hersteller, Importeur, Distributor, Betreiber, Versicherer, Feuerwehr, Berufsgenossenschaft.
2. **Zellchemie:** Li-Ion (NMC, LFP), Festkörper, Bleisäure, NiMH; Spannung, Kapazität (kWh)?
3. **Lebenszyklus-Phase:** Entwicklung, Inverkehrbringen, Betrieb, Wartung, Defekt, Rücknahme.
4. **Anlass:** Brandvorfall, Versicherer-Audit, neue Lagerhalle, Rückrufentscheidung, Transportgenehmigung.
5. **Unterlagen:** Batterie-Datenblatt, Zertifikate UN 38.3, Sicherheitsdatenblatt, Konformitätserklärung, Versicherungsbedingungen, VdS-Auflagen.

## Rechtlicher Rahmen

- **Batterie-VO** VO (EU) 2023/1542; gestaffeltes Inkrafttreten, Kennzeichnungspflichten ab 18.08.2026, CE für bestimmte Batteriekategorien.
- **MaschinenVO** VO (EU) 2023/1230 als Gesamtmaschine; Schnittstelle zur Batterie als Komponente.
- **ProdSG** allgemeine Produktsicherheit; **GPSR** VO (EU) 2023/988 seit 13.12.2024 Geltung.
- **CRA** VO (EU) 2024/2847 bei vernetztem Batterie-Management-System.
- **ADR** Gefahrgutrecht (UN 3480 Li-Ionen, UN 3481 Li-Ionen mit Ausrüstung), UN-Tests 38.3.
- **Landesbauordnungen / Verkaufsstättenverordnungen / IndBauR** Brandabschnitte, Löschanlagen.
- **VdS-Bedingungen** (VdS 3103, VdS 3856) zu Li-Ion-Lagerung.
- **ProdHaftG / VO (EU) 2024/2853** Produkthaftung, § 823 BGB.

## Workflow Schritt für Schritt

1. **Zellklassifizierung.** Energie pro Zelle und Pack, Chemie, Brandverhalten (Thermal Runaway).
2. **Konformität.** Batterie-VO, MaschinenVO, ggf. CRA, UN 38.3 Transportsicherheit.
3. **Brandschutzkonzept.** Trennung Lager und Betrieb, Brandlasten, Sprinkler/Inertgas, Quarantäne-Container für defekte Akkus.
4. **Lade-/Ruheorte.** Idealerweise im Außenbereich oder eigenem Brandabschnitt; Trennung von hochbelegten Bereichen.
5. **Wartung.** Periodische Kapazitäts- und Innenwiderstandsmessung; Austauschintervalle; Logging.
6. **Transport.** ADR-Klassifizierung, Verpackung, Begleitdokumente.
7. **Rückruf-Vorbereitung.** Wenn Defektmuster erkennbar: Vigilanz-Meldung, Markträcknahme; nach Safety-Gate-Portal.
8. **Versicherung.** VdS-Auflagen früh klären; Selbstbehalt bei Li-Ion oft erheblich.
9. **Entsorgung.** Annahmeverpflichtung, Rücknahmesystem Batterie-VO Art. 54 ff.

## Trade-off-Matrix

| Frage | Sicher | Wirtschaftlich | Empfehlung |
|---|---|---|---|
| Lagerkapazität pro Brandabschnitt | gering | hoch | nach VdS 3103 abstufen; großzügig dimensionieren |
| Inert-Löschanlage | teuer, sicher | konventionell | bei großen Lägern Inert; sonst Wasser-Mist mit Detektion |
| Zellchemie | LFP (sicherer) | NMC (höhere Energie) | für stationäre/sicherheitssensible Anwendungen LFP bevorzugen |
| Cloud-Telemetrie BMS | proaktiv, Datenschutzrisiko | offline, blinder Fleck | hybrid: Telemetrie nur sicherheitsrelevant, datensparsam |

## Praxistipps

- **Quarantäne-Container** mit Sandfüllung für defekte Akkus.
- **Frühwarnindikatoren BMS**: Temperatur, Innenwiderstand, Spannungsdrift; Schwellwerte protokollieren.
- **Feuerwehr informieren** vor Erstbetrieb; Übungen.
- **Sachverständige (Brandschutz, VdS)** einbinden.
- **Logistik**: ADR-Schulung der Fahrer; Sicherheitsdatenblatt im LKW.

## Mustertexte

**Lagerordnung Li-Ion (Auszug):**

> 1. Lagerung ausschließlich im Brandabschnitt "Akku-Lager Halle 7" gemäß Brandschutzkonzept Stand [Datum].
> 2. Maximale Lagermenge: 250 kWh nominale Energie.
> 3. Defekte oder geblähte Zellen werden unverzüglich im Quarantäne-Container Stellplatz Q1 isoliert. Verständigung der Sicherheitsfachkraft binnen 15 Minuten.
> 4. Ladeplätze: ausschließlich an gekennzeichneten Stationen; nie über Nacht ohne automatische Trennung.
> 5. Brandschutzeinrichtungen: Rauchmelder, Wärmemelder, Wassernebellöschanlage, Brandfrüherkennung über BMS-Telemetrie.

**Rückrufankündigung (Auszug):**

> Nach Hinweisen auf erhöhte Thermal-Runaway-Quote bei Serie [XYZ] zwischen [Produktionsdatum von/bis] rufen wir die betroffenen Akku-Packs zurück. Bitte stellen Sie den Betrieb der betroffenen Roboter unverzüglich ein und kontaktieren Sie uns über [Hotline]. Wir senden eine ADR-konforme Versandbox und stellen einen Austausch-Akku binnen 5 Werktagen bereit.

## Typische Fehler

- **Lagerung von Li-Ion bei sonstiger Lagerware** ohne Brandabschnitt.
- **Ladestationen in Fluchtwegen** – LBO-Verstoß.
- **Kein Rückrufprozess** vorab definiert – im Ernstfall Eskalation.
- **Versicherer nicht informiert** bei neuer Lagermenge – Deckungsausschluss.
- **ADR-Verstöße** beim Versand defekter Zellen.

## Querverweise

- `ce-zeichen-fehlgebrauch-und-abmahnung`
- `cra-produkt-mit-digitalen-elementen`
- `allgemein`

## Quellen Stand 06/2026

- VO (EU) 2023/1542 (Batterie-VO).
- VO (EU) 2023/1230 (MaschinenVO).
- VO (EU) 2023/988 (GPSR).
- VO (EU) 2024/2847 (CRA).
- ADR 2025; UN 38.3.
- Landesbauordnungen; IndBauR; VdS 3103, VdS 3856.
- VO (EU) 2024/2853 (neue ProdHaftRL); § 823 BGB.
- Live-Verifikation auf eur-lex.europa.eu, baua.de, vds.de; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.

## 3. `bau-und-inspektionsroboter`

**Frühere Beschreibung:** Prüft Bau-, Inspektions- und Wartungsroboter: Baustelle, Arbeitsschutz, Drittschäden, Betreiberorganisation und Beweissicherung.

# Bau- und Inspektionsroboter

## Fachkern: Bau- und Inspektionsroboter
- **Spezialgegenstand:** Bau- und Inspektionsroboter wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Bau- und Inspektionsroboter (Vermessungs-Roboter, Mauerwerks-, 3D-Druck-, Schweiß-, Tunnel-Inspektion, Rohrleitungs-Crawler, Drohnen-Vermessung, Fassaden-Reinigungsroboter) bewegen sich in einem Spannungsfeld zwischen BaustellV/SiGeKo, MaschinenVO, Arbeitsschutzrecht, Bauvertragsrecht (VOB/B), Versicherungsrecht und – bei Drittschäden – allgemeinem Deliktsrecht (§ 823 BGB) sowie Verkehrssicherungspflichten. Dieser Skill ordnet die Pflichten der Akteure (Bauherr, Generalunternehmer, Subunternehmer, Verleiher des Roboters), liefert Vorlagen für Baustellenanweisungen und gibt Hilfen zur Beweissicherung bei Vorfällen.

## Wann brauchen Sie diesen Skill / Kaltstart-Fragen

1. **Rolle:** Bauherr, Generalunternehmer, Subunternehmer, Verleiher des Roboters, Hersteller, SiGeKo, Versicherer, Geschädigter.
2. **Robotertyp:** 3D-Druck-Roboter Beton, Mauer-Robot, Tunnel-Inspektion, Brücken-Inspektion, Schweißroboter, Demontage-Roboter mit Hochdruckwasserstrahl.
3. **Standort:** Baustelle mit weiteren Gewerken, Tunnel, Brücke, Hochhaus, Industriestandort, öffentlicher Raum.
4. **Anlass:** Inverkehrbringen, Mietvertrag, Vorfall (Personenschaden, Sachbeschädigung am Bauwerk Dritter, Schaden am Baugrund), Schiedsverfahren, Versicherungsregress.
5. **Unterlagen:** Risikobeurteilung, SiGePlan, Bauvertrag, Liefer- und Mietverträge, Wartungs- und Inspektionsprotokolle, Telematik-Logs, Versicherungspolicen.

## Rechtlicher Rahmen

- **MaschinenVO** VO (EU) 2023/1230 für Inverkehrbringen ab 20.01.2027 (vorher Maschinen-RL 2006/42/EG).
- **BaustellV** § 3 Koordinator (SiGeKo); RAB 31 (Regeln zum Arbeitsschutz auf Baustellen).
- **ArbSchG, BetrSichV, BauStellV, BGV/DGUV**: zu Baurobotik einschlägige Sicherheitsregelungen.
- **VOB/B** § 4 Ausführung, § 13 Mängelansprüche; ergänzend BGB Werkvertragsrecht §§ 631 ff., insb. § 633 Sach- und Rechtsmangel.
- **§ 823 BGB / § 836 BGB / § 906 BGB** für Drittschäden, Immissionen, Lärm, Erschütterungen.
- **ProdHaftG / VO (EU) 2024/2853** Hersteller, ggf. Quasi-Hersteller des Integrators.
- **KI-VO** bei autonomer Wahrnehmung; bei sicherheitskritischer Erkennung ggf. Hochrisiko Anhang III KI-VO.

## Workflow Schritt für Schritt

1. **Rollenmatrix.** Wer ist Hersteller, wer Integrator, wer Vermieter, wer Betreiber, wer Bauherr? Wer haftet im Außenverhältnis?
2. **Risikobeurteilung baustellenspezifisch.** Neben der Hersteller-Risikobeurteilung eine baustellenbezogene Beurteilung mit SiGeKo; Aufstellort, Bewegungsradius, Notabschaltung, Vandalismusrisiko.
3. **Koordination mit anderen Gewerken.** Schichtpläne, Sperrzonen, Lichtsignal, Funkkanäle, Eskalation.
4. **Drittschutz.** Absperrung; bei Außeneinsatz Verkehrssicherung; Lärm- und Erschütterungsmessungen vorab.
5. **Versicherung.** Bau-Betriebshaftpflicht prüfen; spezielle Robotik-Klausel; Selbstbehalt; Übermittlung der Risikoinformationen vor Einsatz.
6. **Vertragliche Pflichten.** Lieferverträge: Performance-Aufrüstung, Service-Level, Ersatzgeräte; Mietverträge: Wartungsstand, Übergabeprotokoll mit Fotos und Logauszug.
7. **Beweissicherung bei Vorfällen.** Logs unverzüglich sichern (Schreibsperre, Hash), Fotos, Augenzeugen, Notarprotokoll falls nötig, Sachverständiger zur Sicherung.
8. **Kommunikation.** Pressemeldung nur abgestimmt; gegenüber Polizei/Behörden sachlich und faktenbasiert.

## Trade-off-Matrix

| Spannungsfeld | Konservativ | Aggressiv | Empfehlung |
|---|---|---|---|
| Sperrzone | groß | knapp | Sperrzone ausreichend für Worst-Case-Bewegung plus Reaktionszeit |
| Telematik-Daten an Bauherr | offen | restriktiv | Live-Dashboard für Sicherheit, datensparsam für Performance |
| Personalbesetzung | Operator vor Ort | Remote | Bei autonomem Betrieb mind. ein Operator im 30-Sekunden-Eingriff |
| Mietzeitraum kurz | flexibel, höhere Kosten | lang, billiger | bei häufigem Standortwechsel kurz, bei einem Großprojekt lang |

## Praxistipps

- **SiGeKo früh einbeziehen** – auch bei Sub-Sub-Verträgen.
- **Wartungsplan dokumentieren** – Lückenlosigkeit ist Beweismittel.
- **Notfallübung** je Standort.
- **DSGVO bei Kamera-Sensorik**: Hinweisschild und Speicher-Konzept.
- **Klimaeinflüsse**: Sensoren unter Regen/Schnee unzuverlässig – Stilllegungsschwellen festlegen.

## Mustertexte

**Baustellenanweisung (Auszug):**

> Für den Einsatz des Roboters Typ Z auf Baustelle [BV-Nr.] gilt: Aufstellbereich gemäß Anlage 1 markiert (rot). Während Betriebs in diesem Bereich kein anderes Gewerk; Sperrgitter und Warnleuchten. Notabschaltung am Bediengerät und an drei festen Pulten. Im Vorfeld jedes Einsatzes Logauslese und Sichtkontrolle dokumentieren. Ansprechpartner Operator: Hr. Müller (+49…); Ansprechpartner SiGeKo: Fr. Schulz (+49…).

**Vertragsklausel (Mietvertrag Roboter):**

> Der Vermieter stellt den Roboter in einem MaschinenVO-konformen Zustand zur Verfügung; die EU-Konformitätserklärung, die Risikobeurteilung und die Betriebsanleitung in deutscher Sprache sind Bestandteil dieses Vertrages. Der Mieter stellt sicher, dass nur unterwiesenes Personal den Roboter bedient. Bei Vorfall mit Personenschaden hat der Mieter binnen 24 Stunden alle Logs und Wartungsprotokolle zu sichern und dem Vermieter zur Verfügung zu stellen.

## Typische Fehler

- **Hersteller-Risikobeurteilung als Baustellen-Beurteilung** verwendet.
- **Keine Sperrzone**, sondern nur visuelle Markierung.
- **SiGeKo nicht eingebunden** bei kurzem Einsatz.
- **Logs überschrieben** nach 24 h – Beweisverlust.
- **Wartung extern, aber ohne Übergabeprotokoll**.

## Querverweise

- `arbeitsschutz-betrsichv-robotik`
- `betreiber-mitverschulden-und-fehlbedienung`
- `deliktische-haftung-paragraph-823-bgb`

## Quellen Stand 06/2026

- VO (EU) 2023/1230 (MaschinenVO).
- BaustellV; RAB 31; ArbSchG; BetrSichV.
- VOB/B; BGB §§ 631 ff., §§ 823 ff.
- VO (EU) 2024/2853 (neue ProdHaftRL).
- VO (EU) 2024/1689 (KI-VO).
- Live-Verifikation auf baua.de, bundesanzeiger.de, eur-lex.europa.eu; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.

## 4. `beschaeftigtendatenschutz-cobot`

**Frühere Beschreibung:** Prüft Beschäftigtendatenschutz bei Cobots: Leistungsdaten, Standort, Video, Betriebsrat, Zweckbindung und Löschfristen.

# Beschäftigtendatenschutz bei Cobot-Einsatz

## Fachkern: Beschäftigtendatenschutz bei Cobot-Einsatz
- **Spezialgegenstand:** Beschäftigtendatenschutz bei Cobot-Einsatz wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Cobots erfassen regelmäßig Beschäftigtendaten: Pickrate je Schicht, Standortdaten innerhalb des Arbeitsplatzes, biometrische Marker (Hand-, Körpererkennung), ggf. Videoschnitt zur Sicherheit. Dazu kommt Cloud-Telemetrie für Predictive Maintenance. Das berührt DSGVO, § 26 BDSG (a. F.; nach EuGH C-34/21 "Hauptpersonalrat Hessen" eingeschränkt), den Beschäftigtendatenschutz-Entwurf (Bundesgesetzgebung in Vorbereitung), § 87 Abs. 1 Nr. 6 BetrVG und Art. 22, 35 DSGVO. Dieser Skill liefert Prüfschema, Betriebsvereinbarungsklauseln und Datenschutzhinweise.

## Wann brauchen Sie diesen Skill / Kaltstart-Fragen

1. **Rolle:** Arbeitgeber, Datenschutzbeauftragter, Betriebsrat, Beschäftigte/r, Aufsichtsbehörde.
2. **Cobot-Modell:** Welche Sensoren? Welche Daten werden lokal/Cloud verarbeitet? Anbieter im EWR oder Drittland?
3. **Zweck:** Sicherheit (PFL/SSM), Wartung, Leistungssteuerung, Schichtplanung, individuelle Mitarbeiterauswertung?
4. **Bestehende BV** zu Mitarbeiterüberwachung?
5. **Anlass:** Erstinbetriebnahme, Beschwerde Mitarbeiter, Anfrage Aufsichtsbehörde, Audit, Anti-Diskriminierungsfall.

## Rechtlicher Rahmen

- **DSGVO** Art. 5, 6, 9, 13, 14, 22, 25, 32, 35.
- **§ 26 BDSG** in seinem nach EuGH C-34/21 verbleibenden Anwendungsbereich; bundesgesetzliche Reform des Beschäftigtendatenschutzes seit 2024/2025 im Gesetzgebungsverfahren.
- **BetrVG** § 87 Abs. 1 Nr. 6 (Einführung und Anwendung technischer Einrichtungen zur Überwachung), Nr. 7 Arbeits- und Gesundheitsschutz, § 80 Mitwirkungsrechte, § 90 Unterrichtung.
- **KI-VO** Art. 26 Abs. 7 Information der Beschäftigten und Betriebsräte bei Einsatz von Hochrisiko-KI am Arbeitsplatz; Art. 5 Verbote (insb. Emotionserkennung am Arbeitsplatz, Art. 5 Abs. 1 lit. f ab 02.02.2025).
- **MaschinenVO** VO (EU) 2023/1230 und ArbSchG für Sicherheits-Sensorik.

## Workflow Schritt für Schritt

1. **Datenkatalog.** Welche Daten entstehen (Sensor, Kamera, Audio, Vibration, Bedien-Logs)? Welche sind personenbezogen oder personenbeziehbar? Welche sind besonderer Kategorien (Art. 9 DSGVO)?
2. **Zweckbindung.** Pro Datenkategorie konkreten Zweck definieren; "Allzweck-Telemetrie" ist nicht zulässig.
3. **Rechtsgrundlage.** Für jeden Zweck: § 26 BDSG / Art. 6 Abs. 1 lit. b/c/f DSGVO / Kollektivvereinbarung Art. 88 DSGVO + § 26 Abs. 4 BDSG.
4. **DSFA Art. 35 DSGVO** bei systematischer Überwachung am Arbeitsplatz; Konsultation des DSB.
5. **Betriebsrat.** Mitbestimmung § 87 Abs. 1 Nr. 6 BetrVG; Betriebsvereinbarung mit klaren Zweck-, Erforderlichkeits-, Löschungs-, Auswertungsregeln.
6. **Technische Datenminimierung.** On-device-Aggregation; keine Roh-Videos in Cloud; Hashes statt Klartext.
7. **KI-VO-Pflichten.** Information der Beschäftigten und des Betriebsrats vor Inbetriebnahme; Verbot Emotionserkennung am Arbeitsplatz.
8. **Auftragsverarbeitung** Art. 28 DSGVO mit Cloud-Anbieter; bei Drittland: Standardvertragsklauseln, TIA.
9. **Auskunfts- und Löschpflichten** Art. 15, 17 DSGVO; klare Prozesse.

## Trade-off-Matrix

| Daten | Sicherheits-Zweck | HR-Zweck (Leistung) | Empfehlung |
|---|---|---|---|
| Bewegungsdaten Cobot-Arm | erforderlich, dauerhaft | nicht erforderlich | dauerhaft für Safety, aggregiert für HR (oder gar nicht) |
| Standort Mitarbeiter relativ zum Cobot | nur sicherheitskritisch | grds. unzulässig | Ereignisspeicher bei Annäherungsalarm, sonst gelöscht |
| Schicht-Performance | nicht erforderlich | mit BV möglich | nur aggregiert (Team-Ebene), Löschfrist 90 Tage |
| Bild/Video | nur sicherheitsrelevant | grds. unzulässig | Ereignisspeicher, on-device Blur |

## Praxistipps

- **Trennung Safety / HR** durch Datenarchitektur: getrennte Pipelines, getrennte Zugriffsrechte.
- **Kein Permanent-Video** im Cobot-Bereich.
- **Schichtleitung darf nicht** Echtzeit-Leistungsdaten einzelner Mitarbeiter sehen.
- **Mitarbeiter informieren** (Art. 13 DSGVO) bei Inbetriebnahme und bei Änderungen.
- **Anti-Diskriminierungs-Check**: keine Auswertung nach geschützten Merkmalen.

## Mustertexte

**Klausel Betriebsvereinbarung (Auszug):**

> § 4 Datenarten und Zwecke
> 1. Die im Cobot Typ Y erhobenen Bewegungs- und Sensordaten dienen ausschließlich der Sicherheit (Power-and-Force-Limiting, Speed-and-Separation-Monitoring) sowie der Wartung. Eine personenbezogene Leistungsauswertung erfolgt nicht.
> 2. Aggregierte Schicht-Performance-Daten werden nur auf Team-Ebene (mindestens 5 Personen) ausgewertet und nach spätestens 90 Tagen gelöscht.
> 3. Verstöße gegen diese Zweckbindung führen zur sofortigen Aussetzung des Einsatzes nach § 23 Abs. 3 BetrVG.

**Mitarbeiterinformation Art. 13 DSGVO (Auszug):**

> Verantwortlicher: [Firma]. Kontakt DSB: [E-Mail]. Im Cobot-Arbeitsplatz X werden zu Sicherheits- und Wartungszwecken Bewegungsdaten des Cobots sowie ereignisbezogen Annäherungsdaten Ihres Aufenthalts im Schutzraum erhoben. Rechtsgrundlage: § 26 BDSG i. V. m. Art. 6 Abs. 1 lit. b/f DSGVO und Betriebsvereinbarung vom [Datum]. Speicherdauer: 7 Tage (Sicherheit); 90 Tage aggregiert (Wartung). Empfänger: [Cloud-Anbieter] als Auftragsverarbeiter im EWR. Ihre Rechte: Art. 15-22 DSGVO; Beschwerde bei [zuständige Aufsichtsbehörde].

## Typische Fehler

- **Permanent-Video** für Sicherheit – unverhältnismäßig.
- **Telemetrie an Hersteller** ohne AVV.
- **Emotionserkennung** als Bedienkomfort – seit 02.02.2025 nach Art. 5 KI-VO verboten am Arbeitsplatz.
- **BV nicht aktualisiert** bei Software-Update mit neuen Funktionen.
- **Schicht-Performance individualisiert** – Mitbestimmung verletzt.

## Querverweise

- `arbeitsschutz-betrsichv-robotik`
- `datenminimierung-edge-cloud`
- `biometrie-emotion-und-personenerkennung`

## Quellen Stand 06/2026

- DSGVO; BDSG § 26.
- BetrVG § 87 Abs. 1 Nr. 6, 7; § 80; § 90.
- VO (EU) 2024/1689 (KI-VO), Art. 5, Art. 26 Abs. 7.
- EuGH, Urteil vom 30. März 2023, Rs. C-34/21 - Hauptpersonalrat Hessen, ECLI:EU:C:2023:270.
- Live-Verifikation auf bfdi.bund.de, edpb.europa.eu, eur-lex.europa.eu; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.

## 5. `betreiber-mitverschulden-und-fehlbedienung`

**Frühere Beschreibung:** Prüft Betreiber-Mitverschulden: missachtete Anleitung, fehlende Wartung, Umgehung von Schutzfunktionen, Schulungslücken und Logspuren.

# Betreiber-Mitverschulden und Fehlbedienung

## Fachkern: Betreiber-Mitverschulden und Fehlbedienung
- **Spezialgegenstand:** Betreiber-Mitverschulden und Fehlbedienung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Wenn ein Roboter Schäden anrichtet, hängt die Haftungsverteilung wesentlich davon ab, ob der Betreiber die Anleitung beachtet, Wartung dokumentiert, Schutzfunktionen aktiv gelassen und Personal geschult hat. Aus Sicht des Herstellers ist Mitverschulden des Betreibers oft die einzige Möglichkeit, der vollen ProdHaftG-Haftung zu entgehen. Aus Sicht des Betreibers (oder seines Geschädigten) wird umgekehrt geprüft, ob der Hersteller seinen Pflichten zur "vernünftigerweise vorhersehbaren Fehlanwendung" (Art. 6 MaschinenVO; § 3 ProdSG; Art. 9 KI-VO) genügt hat. Dieser Skill liefert das Prüfschema, eine Indizienliste und Vorlagen für Schriftsätze.

## Wann brauchen Sie diesen Skill / Kaltstart-Fragen

1. **Rolle:** Hersteller-Verteidigung, Betreiber-Anspruchsdurchsetzung, Versicherer, Geschädigter, Sachverständiger.
2. **Vorfall:** Personenschaden, Sachschaden, Produktionsausfall, Datenpanne durch Fehlbedienung.
3. **Robotertyp und Schutzkonzept:** Welche Schutzfunktionen sind vorhanden, welche aktiv im Vorfall?
4. **Schulungs- und Wartungsstand:** Aktuell? Dokumentiert?
5. **Unterlagen:** Anleitung, Risikobeurteilung, Wartungsprotokolle, Schulungsnachweise, Logs, Fotos, Zeugenaussagen, Vorfallbericht.

## Rechtlicher Rahmen

- **§ 254 BGB** Mitverschulden.
- **§ 6 Abs. 1 ProdHaftG** Haftungsausschluss; **§ 6 Abs. 3 ProdHaftG** Mitverschulden.
- **VO (EU) 2024/2853** (neue ProdHaftRL, Geltung 09.12.2026): Art. 13 Abs. 2 Beweiserleichterungen; Art. 11 Haftungsbefreiung des Wirtschaftsakteurs.
- **MaschinenVO** VO (EU) 2023/1230 Anhang III Nr. 1.7 Information, Nr. 1.1.2(c) vernünftigerweise vorhersehbare Fehlanwendung.
- **KI-VO** Art. 9 Abs. 4: Risikomanagement muss vorhersehbare Missbrauchsfälle (Foreseeable Misuse) abdecken.
- **§ 823 BGB** Verkehrssicherungspflichten beider Seiten.
- **ArbSchG**, **BetrSichV** Betreiberpflichten zur Unterweisung und Wartung.

## Workflow Schritt für Schritt

1. **Tatsachen sammeln** chronologisch; nicht bewerten, sondern fixieren.
2. **Logs auswerten.** Wer hat wann welche Funktion benutzt? Wurde ein Schutzkreis gebrückt? Welche Software-Version?
3. **Anleitung prüfen** auf konkrete Warnungen und Pflichten: Wartungsintervalle, Schulungserfordernisse, bestimmungsgemäße Verwendung.
4. **Vorhersehbarkeit der Fehlanwendung.** Wurde sie in der Risikobeurteilung des Herstellers berücksichtigt? Falls nein: Hersteller-Pflichtverletzung.
5. **Betreiberorganisation.** § 130 OWiG-Analyse: Aufsichtspflicht-Verletzung? Verantwortliche Person benannt?
6. **Mitarbeiter-Verhalten.** Schulungsstand, Unterweisungsnachweise; Anweisungslage; Druck/Stress als Erklärungsfaktor.
7. **Mitverschuldensquote.** Vorschlag erarbeiten unter Berücksichtigung BGH-Rspr. zu § 254 BGB; ggf. gestuft (Vollverschulden Betreiber 100 %, anteilig 30/70, etc.).
8. **Schriftsatz / Memo.** Trennung Tatsachen, technische Bewertung, rechtliche Würdigung; Sachverständigenbeweis vorschlagen.

## Trade-off-Matrix

| Argument Hersteller | Pro | Contra | Gegenstrategie Betreiber |
|---|---|---|---|
| Anleitung nicht befolgt | klar dokumentiert | "Anleitung war 250 Seiten, intransparent" | KISS-Prinzip; Quick-Start-Guide |
| Schutzfunktion deaktiviert | Logspur sichtbar | "Werkseitig deaktiviert" / "vom Servicetechniker" | Verantwortlichkeitsketten dokumentieren |
| Mitarbeiter unqualifiziert | Schulungsnachweise fehlen | "Hersteller hat keine Schulung angeboten" | Schulungsangebot vertraglich vereinbaren |
| Wartung versäumt | Lücke im Plan | "Hersteller-Service nicht verfügbar" | SLA prüfen; Wartungstickets archivieren |

## Praxistipps

- **Logs sofort sichern** (Schreibsperre, Hash) – nicht überschreiben lassen.
- **Brücken/Bypässe** physisch fotografieren.
- **Schulungsnachweise** mit Datum und Unterschrift; nicht nur Listenhaken.
- **Wartungsverträge** auf SLA prüfen; bei verspäteter Wartung des Herstellers ist Mitverschulden des Betreibers reduziert.
- **Sachverständiger** mit Robotik-Erfahrung wählen, nicht nur Maschinenbau-Generalist.

## Mustertexte

**Auszug Klageschrift Geschädigter (Replik auf Mitverschuldensvortrag):**

> Soweit die Beklagte einwendet, der Kläger habe Schutzfunktionen umgangen, ist dies sachlich unzutreffend. Ausweislich des Wartungsprotokolls vom 12.03.2026 (Anlage K12) wurde die Schutzfunktion durch die von der Beklagten beauftragte Service-Firma am 10.03.2026 deaktiviert und nicht wieder aktiviert. Die Verantwortung hierfür trifft den Hersteller im Wege der Erfüllungsgehilfenhaftung § 278 BGB. Die "vernünftigerweise vorhersehbare Fehlanwendung" gemäß Art. 6 MaschinenVO umfasste zudem den hier vorliegenden Fall; die Risikobeurteilung der Beklagten (Anlage K7, S. 23) selbst weist hierauf hin, ohne hinreichende Gegenmaßnahmen vorzusehen.

**Vermerkpassage Versicherer (Anteil 30/70):**

> Nach Auswertung der Logs (Hash-protokolliert am 02.04.2026 durch Sachverständigen Dipl.-Ing. M.) erscheint eine Quote 30 % Geschädigter / 70 % Hersteller angemessen. Mitverschuldenstragend: nicht aktualisierte Software-Version am Betreiber-Cobot trotz vom Hersteller bereitgestelltem OTA-Update; herstellerseits jedoch fehlende Hinweisplicht-Erfüllung gemäß Art. 9 Abs. 4 KI-VO bei der konkret aufgetretenen Konstellation.

## Typische Fehler

- **Anleitung als "Schutzwall"** für Hersteller, ohne deren tatsächliche Lesbarkeit zu prüfen.
- **Wartungslücken pauschal** dem Betreiber zugerechnet, obwohl Hersteller-Service nicht verfügbar war.
- **Logs nicht gesichert** – Beweismittel ist überschrieben.
- **"Vernünftigerweise vorhersehbare Fehlanwendung"** unterschätzt im Hersteller-Risikomanagement.
- **§ 130 OWiG-Verantwortlicher** nicht benannt – Betreiberorganisation angreifbar.

## Querverweise

- `deliktische-haftung-paragraph-823-bgb`
- `beweislast-und-offenlegung-produkthaftung`
- `arbeitsschutz-betrsichv-robotik`

## Quellen Stand 06/2026

- § 254 BGB; § 823 BGB; § 278 BGB.
- ProdHaftG § 6.
- VO (EU) 2024/2853 (neue ProdHaftRL), Art. 11, 13.
- VO (EU) 2023/1230 (MaschinenVO), Art. 6, Anhang III.
- VO (EU) 2024/1689 (KI-VO), Art. 9.
- ArbSchG; BetrSichV; § 130 OWiG.
- Live-Verifikation auf eur-lex.europa.eu, bundesgerichtshof.de, dejure.org; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.

## 6. `betriebsanleitung-sprache-und-warnhinweise`

**Frühere Beschreibung:** Prüft Betriebsanleitung, Sicherheitsinformationen, digitale Anleitung, Sprache, Restgefahren und Verständlichkeit für Zielgruppen.

# Betriebsanleitung, Sprache und Warnhinweise

## Fachkern: Betriebsanleitung, Sprache und Warnhinweise
- **Spezialgegenstand:** Betriebsanleitung, Sprache und Warnhinweise wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Die Betriebsanleitung ist ein Sicherheitsbauteil im juristischen Sinn: Fehler in Sprache, Verständlichkeit, Vollständigkeit oder Warnhinweisen lösen Konstruktions- oder Instruktionsfehler nach § 1 ProdHaftG, § 823 BGB und neuer Produkthaftungs-RL (EU) 2024/2853 aus. Die MaschinenVO VO (EU) 2023/1230 erlaubt erstmals **digitale** Anleitungen unter Bedingungen (Art. 10 Abs. 7 sowie Anhang III Nr. 1.7.4) – ein Paradigmenwechsel. Bei KI-Funktionen verlangt Art. 13 KI-VO eine Gebrauchsanweisung mit besonderem Inhalt. Dieser Skill prüft Anleitung und Warnhinweise auf Compliance und Haftungsrobustheit.

## Wann brauchen Sie diesen Skill / Kaltstart-Fragen

1. **Rolle:** Hersteller, Importeur, technischer Redakteur, Marktüberwachung, Anwalt im Haftungsstreit.
2. **Produkt:** Industrieroboter, Cobot, Service-Roboter, Verbraucher-Robotik (z. B. Saugroboter).
3. **Zielgruppe:** Fachkraft, Endverbraucher, Pflegekraft, Patient, behindertengerecht?
4. **Sprache:** Welche Amtssprachen des Inverkehrbringens?
5. **Format:** Papier, PDF, Online, AR-/VR-Anleitung; Anleitung auf dem Roboter selbst?

## Rechtlicher Rahmen

- **MaschinenVO** VO (EU) 2023/1230 Anhang III Nr. 1.7 Information und Warnhinweise; Art. 10 Abs. 7 zur digitalen Form; Geltung ab 20.01.2027.
- **Maschinen-RL 2006/42/EG** (Übergang bis 19.01.2027) verlangt Anleitung in Amtssprachen des Mitgliedstaats des Inverkehrbringens.
- **ProdSG / GPSR** VO (EU) 2023/988: Information für Verbraucher.
- **ProdHaftG / VO (EU) 2024/2853 (neu)**: Instruktionsfehler als Produktfehler.
- **§ 823 BGB**: ständige Rspr. des BGH zu Instruktionspflichten (Hersteller muss vor Gefahren in vernünftigerweise vorhersehbarer Verwendung warnen).
- **KI-VO** Art. 13 Transparenz; Art. 26 Abs. 1 Pflichten der Betreiber, Anleitung zu beachten; Art. 50 Transparenz bei interaktiven KI-Systemen.
- **GS-Zeichen / TÜV** ProdSG § 21 als ergänzendes Qualitätssignal.
- **Sprachenregime**: Amtssprache des Mitgliedstaats; in Deutschland deutsch (zumindest für Sicherheits- und Warninhalte).

## Workflow Schritt für Schritt

1. **Zielgruppenanalyse.** Fachkraft oder Endverbraucher? Sprachniveau, Vorbildung, Sinneseinschränkungen.
2. **Inhalt nach Anhang III Nr. 1.7 MaschinenVO**: Identifikation, Beschreibung, bestimmungsgemäße Verwendung, Restrisiken, Aufstellung/Anschluss, Bedienung, Wartung, Außerbetriebnahme, Schaltpläne, Lärm-/Vibrationsemissionen.
3. **KI-spezifischer Inhalt** Art. 13 Abs. 3 KI-VO: Identität Anbieter, Zweck, Leistungsmerkmale, Genauigkeit/Robustheit/Sicherheit-Grenzen, Human-Oversight-Maßnahmen, Lebensdauer, Wartung.
4. **Restrisiken explizit benennen.** Risikobeurteilung als Anhang oder zusammengefasst.
5. **Warnhinweise** nach ANSI Z535 / ISO 3864 / ISO 7010: Signalwort (GEFAHR/WARNUNG/VORSICHT/HINWEIS) + Pictogramm + Folge + Vermeidung.
6. **Digitale Anleitung** Anhang III Nr. 1.7.4 MaschinenVO: Verfügbarkeit per QR/URL, Auffindbarkeit für 10 Jahre, papierne Sicherheitsinformationen "free of charge upon request" mind. zwei Jahre nach Inverkehrbringen.
7. **Sprache** der einschlägigen Amtssprache des MS des Inverkehrbringens; Sicherheitsinhalte vor allem.
8. **Verständlichkeitstest** mit Probanden der Zielgruppe; bei Verbraucherprodukten Lesetest auf Schulniveau 8.
9. **Versionierung** und Archivierung; Anleitung ist Teil der technischen Dokumentation 10 Jahre (Art. 11 MaschinenVO; Art. 18 KI-VO).

## Trade-off-Matrix

| Frage | Konservativ | Modern | Empfehlung |
|---|---|---|---|
| Papier-Anleitung | immer | nur digital | bei MaschinenVO-Geltung digital + Sicherheits-Auszug Papier |
| Sprachen | nur Amtssprache | nur Englisch | nur Amtssprache; English ergänzend |
| Warnsymbole | viele | wenige Schlüsselbilder | nach Risiko priorisieren |
| Online-Updates | jährlich | rolling | Versionsstand sichtbar; alte Versionen auffindbar |

## Praxistipps

- **Quick-Start-Card** in jeder Sprache der Hauptmärkte; Sicherheitskern in einer Seite.
- **AR-Overlay** für Wartung – aber Papier-Notfallseite immer.
- **Übersetzung** durch Fachübersetzer mit Sicherheitskenntnis – nicht maschinell ohne Review.
- **Symbol-Glossar** als Pull-Out.
- **Akustische Warnung** bei interaktiver Robotik – Sprache zusätzlich zu Display.

## Mustertexte

**Warnhinweis (ANSI Z535/ISO 3864 Format):**

> WARNUNG. Quetschgefahr durch Cobot-Arm. Nicht in den Bewegungsraum greifen, solange die LED grün leuchtet. Bei Wartung Schlüsselschalter auf "Service"; nur autorisiertes Personal.

**Auszug digitale Anleitung – Hinweis auf Papier-Auszug:**

> Diese Anleitung ist digital unter https://[…]/manuals/[Seriennummer] in der jeweils gültigen Fassung verfügbar. Sicherheitsinformationen sind in gedruckter Form Bestandteil der Lieferung. Auf schriftliche Anforderung an [Adresse] senden wir Ihnen innerhalb von zwei Jahren nach Inverkehrbringen eine vollständige Papierfassung kostenfrei zu (Art. 10 Abs. 7 MaschinenVO).

**KI-Transparenz (Art. 13 Abs. 3 KI-VO, Auszug):**

> Das im Roboter integrierte KI-System "VisionCobot 3" dient der Hinderniserkennung im Cobot-Arbeitsraum. Trainingsdatenbasis: 2,8 Mio. annotierte Frames in den in Anlage B genannten Kontexten. Bekannte Genauigkeitsgrenzen: bei Gegenlicht über 80.000 Lux Recall-Reduktion um bis zu 12 %. Menschliche Kontrolle: jederzeitiges Not-Halt per Schlüssel; Override via Operator-Konsole. Lebensdauer-Garantie: 5 Jahre.

## Typische Fehler

- **Unverständliche Sprache** durch wörtliche Maschinenübersetzung.
- **Risikobeurteilung als alleinige Informationsquelle**; Anleitung nicht abgeleitet.
- **Pauschale Warnungen** ("Vorsicht! Achtung!") ohne konkrete Folge/Vermeidung.
- **Sprachversion fehlt** in einem Mitgliedstaat.
- **Digitale Anleitung** ohne Auffindbarkeit nach 10 Jahren – Hersteller-Pflichtverletzung.

## Querverweise

- `ce-zeichen-fehlgebrauch-und-abmahnung`
- `betreiber-mitverschulden-und-fehlbedienung`
- `barrierefreiheit-und-inklusion-robotik`

## Quellen Stand 06/2026

- VO (EU) 2023/1230 (MaschinenVO), Art. 10, 11, Anhang III Nr. 1.7.
- RL 2006/42/EG (bis 19.01.2027).
- VO (EU) 2023/988 (GPSR).
- VO (EU) 2024/1689 (KI-VO), Art. 13, 18, 26, 50.
- VO (EU) 2024/2853 (neue ProdHaftRL).
- ProdHaftG; § 823 BGB.
- ISO 3864; ISO 7010; ANSI Z535.
- Live-Verifikation auf eur-lex.europa.eu, baua.de, bsi.bund.de; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.
