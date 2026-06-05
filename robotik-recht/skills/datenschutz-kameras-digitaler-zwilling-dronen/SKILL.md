---
name: datenschutz-kameras-digitaler-zwilling-dronen
description: "Datenschutz Kameras Digitaler Zwilling Dronen im Robotik- und KI-Recht: prüft konkret Prüft Kameras, Lidar, Mikrofone, Tiefensensoren und Umgebungsdaten von Robotern. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Datenschutz Kameras Digitaler Zwilling Dronen

## Arbeitsbereich

Dieser Skill behandelt **Datenschutz Kameras Digitaler Zwilling Dronen** als zusammenhängenden Arbeitsgang im Robotik- und KI-Recht. Im Mittelpunkt steht die Prüfung von Prüft Kameras, Lidar, Mikrofone und weiteren verwandten Aspekten. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `datenschutz-kameras-und-sensorik` | Prüft Kameras, Lidar, Mikrofone, Tiefensensoren und Umgebungsdaten von Robotern nach DSGVO und BDSG. |
| `digitaler-zwilling-und-simulation` | Prüft digitalen Zwilling, Simulation, Validierung, virtuelle Inbetriebnahme und Beweiswert für Konformität und Haftung. |
| `dronen-und-robotik-schnittstelle` | Prüft Drohnen als Robotik-Schnittstelle: EU-UAS-Regeln, Kamera, autonome Funktionen, Haftung und Einsatzplanung. |
| `dsfa-fuer-robotik` | Erstellt Datenschutz-Folgenabschätzung für Roboter mit Sensorik, Telemetrie, KI-Auswertung oder vulnerablen Nutzergruppen. |

## Arbeitsweg

- Rolle und Ziel im Robotik- und KI-Recht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: KI-VO Geltungsbeginn 02.08.2026 für Hochrisiko (Art. 6 Anhang III), Verbote ab 02.02.2025, Maschinen-VO 20.01.2027, ProdHaftRL-Umsetzung 09.12.2026, KI-VO Art. 73 schwerwiegender Vorfall innerhalb 15 Tagen.
- Tragende Normen verifizieren: EU KI-VO (VO 2024/1689) Art. 6, 8-15, 16, 26, 50, 73, 99, Maschinenverordnung 2023/1230, Produkthaftungs-Richtlinie 2024/2853, BGB §§ 823, 831, ProdHaftG, EU NIS2-RL 2022/2555, EU CRA — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Hersteller, Importeur, Händler, Betreiber, Endnutzer, Marktüberwachungsbehörde (BMAS/BNetzA/BMDV), benannte Stelle (Notified Body), KI-Aufsicht (BNetzA-Stelle).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Konformitätserklärung, technische Dokumentation Anhang IV KI-VO, Risikomanagement-System Art. 9, Datengovernance-Konzept Art. 10, FAT/SAT-Protokoll, Betriebsanleitung, CE-Kennzeichnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `datenschutz-kameras-und-sensorik`

**Fokus:** Prüft Kameras, Lidar, Mikrofone, Tiefensensoren und Umgebungsdaten von Robotern nach DSGVO und BDSG.


# Datenschutz Sensorik

## Fachkern: Datenschutz Sensorik
- **Spezialgegenstand:** Datenschutz Sensorik wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Fachmodul im Plugin `robotik-recht`. Nutze ihn, wenn der Fall Robotik, autonome oder teilautonome Maschinen, integrierte KI, Sensorik, Remote-Updates, Mensch-Roboter-Interaktion, Produktsicherheit, Haftung, Datenschutz, Cybersecurity oder Robotikverträge berührt.

## Start

Kläre knapp:

1. **Rolle:** Hersteller, Anbieter, Integrator, Importeur, Händler, Betreiber, Deployer, Wartung, Versicherer, Behörde oder Geschädigte Person.
2. **Produkt:** Industrieroboter, Cobot, AMR/AGV, Service-, Pflege-, Medizin-, Haushalts-, Agrar-, Sicherheits-, Liefer- oder Sonderrobotik.
3. **Ziel:** Freigabe, CE-Akte, Behördenantwort, Vertragsprüfung, Incident, Rückruf, Haftungsmemo, Datenschutzprüfung, Cyberprüfung, Klage/Verteidigung oder Vorstandsvorlage.
4. **Dringlichkeit:** Unfall, Verletzung, Datenpanne, Cyberangriff, Marktüberwachung, Rückruf, Kundenstillstand, Frist oder nur Prävention.
5. **Unterlagen:** Anleitung, Risikobeurteilung, EU-Konformitätserklärung, technische Dokumentation, Logs, Softwarestände, Verträge, DSFA, SBOM, Wartungsprotokolle, E-Mails.

## Prüfspur

- Baue zuerst eine **Rollenmatrix**. Robotikfälle kippen oft daran, wer rechtlich Hersteller, Anbieter, Betreiber oder bloßer Zulieferer ist.
- Prüfe dann **parallel**: Maschinenrecht/Produktsicherheit, KI-VO, Produkthaftung, Datenschutz, Cybersecurity, Data Act, sektorspezifisches Recht und Vertrag.
- Trenne sichere Tatsachen, technische Annahmen und Rechtsbewertung. Markiere jede nicht belegte technische Annahme sichtbar.
- Arbeite mit einer **Ampel**: Rot = sofort handeln; Gelb = Unterlagen/Rückfragen; Grün = derzeit tragfähig, aber live zu verifizieren.
- Bei Rechtsprechung und aktuellen Normen: keine Paywall-Fundstellen, keine erfundenen Aktenzeichen; live über amtliche/freie Quellen prüfen.

## Spezifischer Fokus

Dieser Skill fokussiert: **Prüft Kameras, Lidar, Mikrofone, Tiefensensoren und Umgebungsdaten von Robotern nach DSGVO und BDSG.**

Quellen-/Normenanker: DSGVO Art. 5, 6, 9, 25, 32, 35; BDSG.

## Ergebnisformat

Liefere je nach Auftrag eines der folgenden Formate:

- **Kurzvermerk** mit Ergebnis, Begründung, Risikoampel und offenen Fragen.
- **Rückfragenliste** an Technik/QM/IT-Security/Datenschutz/Vertrieb.
- **Dokumentenmatrix** mit vorhandenen und fehlenden Nachweisen.
- **Behörden- oder Mandantenentwurf** mit vorsichtiger Sprache und Quellenhinweisen.
- **Red-Team-Check** mit Gegenargumenten, Worst Case und nächstem Schritt.

Schlage am Ende passende Anschluss-Skills aus `robotik-recht` vor. Wenn Datenschutz, KI-VO, IT-Recht, Medizinrecht, Arbeitsrecht oder Vertragsrecht überwiegt, nenne zusätzlich das passende Nachbarplugin.

## 2. `digitaler-zwilling-und-simulation`

**Fokus:** Prüft digitalen Zwilling, Simulation, Validierung, virtuelle Inbetriebnahme und Beweiswert für Konformität und Haftung.


# Digitaler Zwilling und Simulation

## Fachkern: Digitaler Zwilling und Simulation
- **Spezialgegenstand:** Digitaler Zwilling und Simulation wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Fachmodul im Plugin `robotik-recht`. Nutze ihn, wenn der Fall Robotik, autonome oder teilautonome Maschinen, integrierte KI, Sensorik, Remote-Updates, Mensch-Roboter-Interaktion, Produktsicherheit, Haftung, Datenschutz, Cybersecurity oder Robotikverträge berührt.

## Start

Kläre knapp:

1. **Rolle:** Hersteller, Anbieter, Integrator, Importeur, Händler, Betreiber, Deployer, Wartung, Versicherer, Behörde oder Geschädigte Person.
2. **Produkt:** Industrieroboter, Cobot, AMR/AGV, Service-, Pflege-, Medizin-, Haushalts-, Agrar-, Sicherheits-, Liefer- oder Sonderrobotik.
3. **Ziel:** Freigabe, CE-Akte, Behördenantwort, Vertragsprüfung, Incident, Rückruf, Haftungsmemo, Datenschutzprüfung, Cyberprüfung, Klage/Verteidigung oder Vorstandsvorlage.
4. **Dringlichkeit:** Unfall, Verletzung, Datenpanne, Cyberangriff, Marktüberwachung, Rückruf, Kundenstillstand, Frist oder nur Prävention.
5. **Unterlagen:** Anleitung, Risikobeurteilung, EU-Konformitätserklärung, technische Dokumentation, Logs, Softwarestände, Verträge, DSFA, SBOM, Wartungsprotokolle, E-Mails.

## Prüfspur

- Baue zuerst eine **Rollenmatrix**. Robotikfälle kippen oft daran, wer rechtlich Hersteller, Anbieter, Betreiber oder bloßer Zulieferer ist.
- Prüfe dann **parallel**: Maschinenrecht/Produktsicherheit, KI-VO, Produkthaftung, Datenschutz, Cybersecurity, Data Act, sektorspezifisches Recht und Vertrag.
- Trenne sichere Tatsachen, technische Annahmen und Rechtsbewertung. Markiere jede nicht belegte technische Annahme sichtbar.
- Arbeite mit einer **Ampel**: Rot = sofort handeln; Gelb = Unterlagen/Rückfragen; Grün = derzeit tragfähig, aber live zu verifizieren.
- Bei Rechtsprechung und aktuellen Normen: keine Paywall-Fundstellen, keine erfundenen Aktenzeichen; live über amtliche/freie Quellen prüfen.

## Spezifischer Fokus

Dieser Skill fokussiert: **Prüft digitalen Zwilling, Simulation, Validierung, virtuelle Inbetriebnahme und Beweiswert für Konformität und Haftung.**

Quellen-/Normenanker: Maschinenverordnung, KI-VO, Beweisrecht.

## Ergebnisformat

Liefere je nach Auftrag eines der folgenden Formate:

- **Kurzvermerk** mit Ergebnis, Begründung, Risikoampel und offenen Fragen.
- **Rückfragenliste** an Technik/QM/IT-Security/Datenschutz/Vertrieb.
- **Dokumentenmatrix** mit vorhandenen und fehlenden Nachweisen.
- **Behörden- oder Mandantenentwurf** mit vorsichtiger Sprache und Quellenhinweisen.
- **Red-Team-Check** mit Gegenargumenten, Worst Case und nächstem Schritt.

Schlage am Ende passende Anschluss-Skills aus `robotik-recht` vor. Wenn Datenschutz, KI-VO, IT-Recht, Medizinrecht, Arbeitsrecht oder Vertragsrecht überwiegt, nenne zusätzlich das passende Nachbarplugin.

## 3. `dronen-und-robotik-schnittstelle`

**Fokus:** Prüft Drohnen als Robotik-Schnittstelle: EU-UAS-Regeln, Kamera, autonome Funktionen, Haftung und Einsatzplanung.


# Drohnen und Robotik

## Fachkern: Drohnen und Robotik
- **Spezialgegenstand:** Drohnen und Robotik wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Fachmodul im Plugin `robotik-recht`. Nutze ihn, wenn der Fall Robotik, autonome oder teilautonome Maschinen, integrierte KI, Sensorik, Remote-Updates, Mensch-Roboter-Interaktion, Produktsicherheit, Haftung, Datenschutz, Cybersecurity oder Robotikverträge berührt.

## Start

Kläre knapp:

1. **Rolle:** Hersteller, Anbieter, Integrator, Importeur, Händler, Betreiber, Deployer, Wartung, Versicherer, Behörde oder Geschädigte Person.
2. **Produkt:** Industrieroboter, Cobot, AMR/AGV, Service-, Pflege-, Medizin-, Haushalts-, Agrar-, Sicherheits-, Liefer- oder Sonderrobotik.
3. **Ziel:** Freigabe, CE-Akte, Behördenantwort, Vertragsprüfung, Incident, Rückruf, Haftungsmemo, Datenschutzprüfung, Cyberprüfung, Klage/Verteidigung oder Vorstandsvorlage.
4. **Dringlichkeit:** Unfall, Verletzung, Datenpanne, Cyberangriff, Marktüberwachung, Rückruf, Kundenstillstand, Frist oder nur Prävention.
5. **Unterlagen:** Anleitung, Risikobeurteilung, EU-Konformitätserklärung, technische Dokumentation, Logs, Softwarestände, Verträge, DSFA, SBOM, Wartungsprotokolle, E-Mails.

## Prüfspur

- Baue zuerst eine **Rollenmatrix**. Robotikfälle kippen oft daran, wer rechtlich Hersteller, Anbieter, Betreiber oder bloßer Zulieferer ist.
- Prüfe dann **parallel**: Maschinenrecht/Produktsicherheit, KI-VO, Produkthaftung, Datenschutz, Cybersecurity, Data Act, sektorspezifisches Recht und Vertrag.
- Trenne sichere Tatsachen, technische Annahmen und Rechtsbewertung. Markiere jede nicht belegte technische Annahme sichtbar.
- Arbeite mit einer **Ampel**: Rot = sofort handeln; Gelb = Unterlagen/Rückfragen; Grün = derzeit tragfähig, aber live zu verifizieren.
- Bei Rechtsprechung und aktuellen Normen: keine Paywall-Fundstellen, keine erfundenen Aktenzeichen; live über amtliche/freie Quellen prüfen.

## Spezifischer Fokus

Dieser Skill fokussiert: **Prüft Drohnen als Robotik-Schnittstelle: EU-UAS-Regeln, Kamera, autonome Funktionen, Haftung und Einsatzplanung.**

Quellen-/Normenanker: EU-UAS, Luftverkehrsrecht, DSGVO, Produkthaftung.

## Ergebnisformat

Liefere je nach Auftrag eines der folgenden Formate:

- **Kurzvermerk** mit Ergebnis, Begründung, Risikoampel und offenen Fragen.
- **Rückfragenliste** an Technik/QM/IT-Security/Datenschutz/Vertrieb.
- **Dokumentenmatrix** mit vorhandenen und fehlenden Nachweisen.
- **Behörden- oder Mandantenentwurf** mit vorsichtiger Sprache und Quellenhinweisen.
- **Red-Team-Check** mit Gegenargumenten, Worst Case und nächstem Schritt.

Schlage am Ende passende Anschluss-Skills aus `robotik-recht` vor. Wenn Datenschutz, KI-VO, IT-Recht, Medizinrecht, Arbeitsrecht oder Vertragsrecht überwiegt, nenne zusätzlich das passende Nachbarplugin.

## 4. `dsfa-fuer-robotik`

**Fokus:** Erstellt Datenschutz-Folgenabschätzung für Roboter mit Sensorik, Telemetrie, KI-Auswertung oder vulnerablen Nutzergruppen.


# DSFA für Robotik

## Fachkern: DSFA für Robotik
- **Spezialgegenstand:** DSFA für Robotik wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Fachmodul im Plugin `robotik-recht`. Nutze ihn, wenn der Fall Robotik, autonome oder teilautonome Maschinen, integrierte KI, Sensorik, Remote-Updates, Mensch-Roboter-Interaktion, Produktsicherheit, Haftung, Datenschutz, Cybersecurity oder Robotikverträge berührt.

## Start

Kläre knapp:

1. **Rolle:** Hersteller, Anbieter, Integrator, Importeur, Händler, Betreiber, Deployer, Wartung, Versicherer, Behörde oder Geschädigte Person.
2. **Produkt:** Industrieroboter, Cobot, AMR/AGV, Service-, Pflege-, Medizin-, Haushalts-, Agrar-, Sicherheits-, Liefer- oder Sonderrobotik.
3. **Ziel:** Freigabe, CE-Akte, Behördenantwort, Vertragsprüfung, Incident, Rückruf, Haftungsmemo, Datenschutzprüfung, Cyberprüfung, Klage/Verteidigung oder Vorstandsvorlage.
4. **Dringlichkeit:** Unfall, Verletzung, Datenpanne, Cyberangriff, Marktüberwachung, Rückruf, Kundenstillstand, Frist oder nur Prävention.
5. **Unterlagen:** Anleitung, Risikobeurteilung, EU-Konformitätserklärung, technische Dokumentation, Logs, Softwarestände, Verträge, DSFA, SBOM, Wartungsprotokolle, E-Mails.

## Prüfspur

- Baue zuerst eine **Rollenmatrix**. Robotikfälle kippen oft daran, wer rechtlich Hersteller, Anbieter, Betreiber oder bloßer Zulieferer ist.
- Prüfe dann **parallel**: Maschinenrecht/Produktsicherheit, KI-VO, Produkthaftung, Datenschutz, Cybersecurity, Data Act, sektorspezifisches Recht und Vertrag.
- Trenne sichere Tatsachen, technische Annahmen und Rechtsbewertung. Markiere jede nicht belegte technische Annahme sichtbar.
- Arbeite mit einer **Ampel**: Rot = sofort handeln; Gelb = Unterlagen/Rückfragen; Grün = derzeit tragfähig, aber live zu verifizieren.
- Bei Rechtsprechung und aktuellen Normen: keine Paywall-Fundstellen, keine erfundenen Aktenzeichen; live über amtliche/freie Quellen prüfen.

## Spezifischer Fokus

Dieser Skill fokussiert: **Erstellt Datenschutz-Folgenabschätzung für Roboter mit Sensorik, Telemetrie, KI-Auswertung oder vulnerablen Nutzergruppen.**

Quellen-/Normenanker: DSGVO Art. 35, 36; Aufsichtsbehörden-Leitlinien.

## Ergebnisformat

Liefere je nach Auftrag eines der folgenden Formate:

- **Kurzvermerk** mit Ergebnis, Begründung, Risikoampel und offenen Fragen.
- **Rückfragenliste** an Technik/QM/IT-Security/Datenschutz/Vertrieb.
- **Dokumentenmatrix** mit vorhandenen und fehlenden Nachweisen.
- **Behörden- oder Mandantenentwurf** mit vorsichtiger Sprache und Quellenhinweisen.
- **Red-Team-Check** mit Gegenargumenten, Worst Case und nächstem Schritt.

Schlage am Ende passende Anschluss-Skills aus `robotik-recht` vor. Wenn Datenschutz, KI-VO, IT-Recht, Medizinrecht, Arbeitsrecht oder Vertragsrecht überwiegt, nenne zusätzlich das passende Nachbarplugin.
