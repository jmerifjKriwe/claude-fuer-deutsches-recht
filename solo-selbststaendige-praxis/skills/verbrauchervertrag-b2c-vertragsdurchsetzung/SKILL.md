---
name: verbrauchervertrag-b2c-vertragsdurchsetzung
description: "Verbrauchervertrag B2C Vertragsdurchsetzung: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verbrauchervertrag B2C Vertragsdurchsetzung

## Arbeitsbereich

Dieser Skill bündelt 8 sachlich verwandte Arbeitsschritte rund um **Verbrauchervertrag B2C Vertragsdurchsetzung** im Plugin Solo-/Selbstständigenpraxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `solo-verbrauchervertrag-b2c` | Solo-Selbstständige: prüft Widerruf, Fernabsatz, Informationspflichten und Preisangaben; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis. |
| `solo-vertragsdurchsetzung-ausland` | Solo-Selbstständige: prüft Inkasso, Gerichtsstand, Mahnverfahren und Beweis; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis. |
| `solo-beratungshaftung` | Solo-Selbstständige: prüft Erwartung, Dokumentation, Disclaimer und Grenzen der Beratung; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis. |
| `solo-geldwaesche-und-sanktionen-mini` | Solo-Selbstständige: sensibilisiert bei ungewöhnlichen Zahlungen, Auslandskunden und Sanktionsrisiken; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis. |
| `solo-produkthaftung-kleinhersteller` | Solo-Selbstständige: prüft Produkt, CE, Warnhinweise, Rückruf und Versicherung; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis. |
| `solo-13-wochen-liquiditaetsplan` | Solo-Selbstständige: erstellt realistischen Cashplan mit Steuern, Versicherungen und Zahlungslücken; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis. |
| `solo-anfaenger-modus` | Solo-Selbstständige: erklärt Begriffe wie Freiberuf, Gewerbe, Rechnung, Umsatzsteuer und Gewinn ohne Fachnebel; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis. |
| `solo-aufbewahrung-loeschung` | Solo-Selbstständige: plant handels-/steuerliche Aufbewahrung und datenschutzrechtliche Löschung; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis. |

## Arbeitsweg

- Rolle und Ziel im Solo-Selbstständigen-Praxis klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: SGB IV § 7a Statusanfrage in jedem Stadium, § 28p Betriebsprüfung 4 Jahre Rückwirkung (10 Jahre bei Vorsatz), UStG § 19 Umsatzgrenze 22.000 EUR / 50.000 EUR.
- Tragende Normen verifizieren: SGB IV § 7 (Scheinselbstständigkeit), SGB VI § 2 Nr. 9 (Rentenversicherungspflicht), UStG §§ 1, 19, EStG §§ 15, 18, GewO § 14, BGB §§ 611, 631, 305 ff., HGB §§ 1, 2, BBG (Beitragsbemessung) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Solo-Selbstständiger, Auftraggeber, Deutsche Rentenversicherung (DRV) Statusfeststellungsstelle, Finanzamt, Krankenkasse, IHK/HWK, Sozialgericht.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Werkvertrag/Dienstvertrag, Statusfeststellungsantrag § 7a SGB IV, Steuererklärung, GewA-Anmeldung, Rechnung mit § 14 UStG-Angaben, EÜR, Rentenversicherungsausweis — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `solo-verbrauchervertrag-b2c`

**Fokus:** Solo-Selbstständige: prüft Widerruf, Fernabsatz, Informationspflichten und Preisangaben; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis.

# Verträge und AGB: Prüft widerruf

## Einsatz

Dieser Skill hilft Solo-Selbstständigen beim Themenfeld **Verträge und AGB**. Schwerpunkt: prüft Widerruf, Fernabsatz, Informationspflichten und Preisangaben. Er sortiert die tatsächlichen Unterlagen, den Handlungsdruck und die wirtschaftliche Folge.

## Arbeitsweise

1. Klär zuerst Tätigkeit, Kundentyp, Bundesland/Ort, Haupt- oder Nebenerwerb, Umsatzgrößen, Fristdruck und vorhandene Dokumente.
2. Trenne Muss-Pflichten von Klugheitsmaßnahmen: Anmeldung, Steuer, Vertrag, Sozialversicherung, Datenschutz, Geldfluss und Beweis.
3. Baue eine Ampel mit Sofortmaßnahme, sauberer Dokumentation, optionaler Optimierung und Punkten für Steuerberater, Anwalt oder Behörde.
4. Formuliere am Ende genau ein brauchbares Artefakt: Checkliste, Mail, Vertragsbaustein, Widerspruchsskizze, Fristenlog, Rechnungstext oder Entscheidungsmemo.

## Ergebnis

- Kurzdiagnose in normalem Deutsch
- To-do-Liste mit Fristen und Belegen
- Risiko-/Geldfolge-Ampel
- konkreter Textbaustein oder Dokumentenplan

## Quellen- und Qualitätsregeln

- Prüfe aktuelle Beträge, Grenzwerte und Fristen in amtlichen Quellen, insbesondere Gesetze im Internet, ELSTER, DRV, KSK, Bundesagentur für Arbeit und BMWK-Existenzgründungsportal.
- Keine Steuer- oder Sozialversicherungsentscheidung ohne Hinweis, welche Angaben geschätzt sind und welche Belege fehlen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Fundlink ausgeben; keine BeckRS-/Juris-/Kommentar-Blindzitate.

## 2. `solo-vertragsdurchsetzung-ausland`

**Fokus:** Solo-Selbstständige: prüft Inkasso, Gerichtsstand, Mahnverfahren und Beweis; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis.

# Internationales und Auslandskunden: Prüft inkasso

## Einsatz

Dieser Skill hilft Solo-Selbstständigen beim Themenfeld **Internationales und Auslandskunden**. Schwerpunkt: prüft Inkasso, Gerichtsstand, Mahnverfahren und Beweis. Er sortiert die tatsächlichen Unterlagen, den Handlungsdruck und die wirtschaftliche Folge.

## Arbeitsweise

1. Klär zuerst Tätigkeit, Kundentyp, Bundesland/Ort, Haupt- oder Nebenerwerb, Umsatzgrößen, Fristdruck und vorhandene Dokumente.
2. Trenne Muss-Pflichten von Klugheitsmaßnahmen: Anmeldung, Steuer, Vertrag, Sozialversicherung, Datenschutz, Geldfluss und Beweis.
3. Baue eine Ampel mit Sofortmaßnahme, sauberer Dokumentation, optionaler Optimierung und Punkten für Steuerberater, Anwalt oder Behörde.
4. Formuliere am Ende genau ein brauchbares Artefakt: Checkliste, Mail, Vertragsbaustein, Widerspruchsskizze, Fristenlog, Rechnungstext oder Entscheidungsmemo.

## Ergebnis

- Kurzdiagnose in normalem Deutsch
- To-do-Liste mit Fristen und Belegen
- Risiko-/Geldfolge-Ampel
- konkreter Textbaustein oder Dokumentenplan

## Quellen- und Qualitätsregeln

- Prüfe aktuelle Beträge, Grenzwerte und Fristen in amtlichen Quellen, insbesondere Gesetze im Internet, ELSTER, DRV, KSK, Bundesagentur für Arbeit und BMWK-Existenzgründungsportal.
- Keine Steuer- oder Sozialversicherungsentscheidung ohne Hinweis, welche Angaben geschätzt sind und welche Belege fehlen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Fundlink ausgeben; keine BeckRS-/Juris-/Kommentar-Blindzitate.

## 3. `solo-beratungshaftung`

**Fokus:** Solo-Selbstständige: prüft Erwartung, Dokumentation, Disclaimer und Grenzen der Beratung; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis.

# Versicherung Haftung und Risiko: Prüft erwartung

## Einsatz

Dieser Skill hilft Solo-Selbstständigen beim Themenfeld **Versicherung Haftung und Risiko**. Schwerpunkt: prüft Erwartung, Dokumentation, Disclaimer und Grenzen der Beratung. Er sortiert die tatsächlichen Unterlagen, den Handlungsdruck und die wirtschaftliche Folge.

## Arbeitsweise

1. Klär zuerst Tätigkeit, Kundentyp, Bundesland/Ort, Haupt- oder Nebenerwerb, Umsatzgrößen, Fristdruck und vorhandene Dokumente.
2. Trenne Muss-Pflichten von Klugheitsmaßnahmen: Anmeldung, Steuer, Vertrag, Sozialversicherung, Datenschutz, Geldfluss und Beweis.
3. Baue eine Ampel mit Sofortmaßnahme, sauberer Dokumentation, optionaler Optimierung und Punkten für Steuerberater, Anwalt oder Behörde.
4. Formuliere am Ende genau ein brauchbares Artefakt: Checkliste, Mail, Vertragsbaustein, Widerspruchsskizze, Fristenlog, Rechnungstext oder Entscheidungsmemo.

## Ergebnis

- Kurzdiagnose in normalem Deutsch
- To-do-Liste mit Fristen und Belegen
- Risiko-/Geldfolge-Ampel
- konkreter Textbaustein oder Dokumentenplan

## Quellen- und Qualitätsregeln

- Prüfe aktuelle Beträge, Grenzwerte und Fristen in amtlichen Quellen, insbesondere Gesetze im Internet, ELSTER, DRV, KSK, Bundesagentur für Arbeit und BMWK-Existenzgründungsportal.
- Keine Steuer- oder Sozialversicherungsentscheidung ohne Hinweis, welche Angaben geschätzt sind und welche Belege fehlen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Fundlink ausgeben; keine BeckRS-/Juris-/Kommentar-Blindzitate.

## 4. `solo-geldwaesche-und-sanktionen-mini`

**Fokus:** Solo-Selbstständige: sensibilisiert bei ungewöhnlichen Zahlungen, Auslandskunden und Sanktionsrisiken; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis.

# Grenzen Compliance und Selbstschutz: Sensibilisiert bei ungewöhnlichen zahlungen

## Einsatz

Dieser Skill hilft Solo-Selbstständigen beim Themenfeld **Grenzen Compliance und Selbstschutz**. Schwerpunkt: sensibilisiert bei ungewöhnlichen Zahlungen, Auslandskunden und Sanktionsrisiken. Er sortiert die tatsächlichen Unterlagen, den Handlungsdruck und die wirtschaftliche Folge.

## Arbeitsweise

1. Klär zuerst Tätigkeit, Kundentyp, Bundesland/Ort, Haupt- oder Nebenerwerb, Umsatzgrößen, Fristdruck und vorhandene Dokumente.
2. Trenne Muss-Pflichten von Klugheitsmaßnahmen: Anmeldung, Steuer, Vertrag, Sozialversicherung, Datenschutz, Geldfluss und Beweis.
3. Baue eine Ampel mit Sofortmaßnahme, sauberer Dokumentation, optionaler Optimierung und Punkten für Steuerberater, Anwalt oder Behörde.
4. Formuliere am Ende genau ein brauchbares Artefakt: Checkliste, Mail, Vertragsbaustein, Widerspruchsskizze, Fristenlog, Rechnungstext oder Entscheidungsmemo.

## Ergebnis

- Kurzdiagnose in normalem Deutsch
- To-do-Liste mit Fristen und Belegen
- Risiko-/Geldfolge-Ampel
- konkreter Textbaustein oder Dokumentenplan

## Quellen- und Qualitätsregeln

- Prüfe aktuelle Beträge, Grenzwerte und Fristen in amtlichen Quellen, insbesondere Gesetze im Internet, ELSTER, DRV, KSK, Bundesagentur für Arbeit und BMWK-Existenzgründungsportal.
- Keine Steuer- oder Sozialversicherungsentscheidung ohne Hinweis, welche Angaben geschätzt sind und welche Belege fehlen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Fundlink ausgeben; keine BeckRS-/Juris-/Kommentar-Blindzitate.

## 5. `solo-produkthaftung-kleinhersteller`

**Fokus:** Solo-Selbstständige: prüft Produkt, CE, Warnhinweise, Rückruf und Versicherung; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis.

# Versicherung Haftung und Risiko: Prüft produkt

## Einsatz

Dieser Skill hilft Solo-Selbstständigen beim Themenfeld **Versicherung Haftung und Risiko**. Schwerpunkt: prüft Produkt, CE, Warnhinweise, Rückruf und Versicherung. Er sortiert die tatsächlichen Unterlagen, den Handlungsdruck und die wirtschaftliche Folge.

## Arbeitsweise

1. Klär zuerst Tätigkeit, Kundentyp, Bundesland/Ort, Haupt- oder Nebenerwerb, Umsatzgrößen, Fristdruck und vorhandene Dokumente.
2. Trenne Muss-Pflichten von Klugheitsmaßnahmen: Anmeldung, Steuer, Vertrag, Sozialversicherung, Datenschutz, Geldfluss und Beweis.
3. Baue eine Ampel mit Sofortmaßnahme, sauberer Dokumentation, optionaler Optimierung und Punkten für Steuerberater, Anwalt oder Behörde.
4. Formuliere am Ende genau ein brauchbares Artefakt: Checkliste, Mail, Vertragsbaustein, Widerspruchsskizze, Fristenlog, Rechnungstext oder Entscheidungsmemo.

## Ergebnis

- Kurzdiagnose in normalem Deutsch
- To-do-Liste mit Fristen und Belegen
- Risiko-/Geldfolge-Ampel
- konkreter Textbaustein oder Dokumentenplan

## Quellen- und Qualitätsregeln

- Prüfe aktuelle Beträge, Grenzwerte und Fristen in amtlichen Quellen, insbesondere Gesetze im Internet, ELSTER, DRV, KSK, Bundesagentur für Arbeit und BMWK-Existenzgründungsportal.
- Keine Steuer- oder Sozialversicherungsentscheidung ohne Hinweis, welche Angaben geschätzt sind und welche Belege fehlen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Fundlink ausgeben; keine BeckRS-/Juris-/Kommentar-Blindzitate.

## 6. `solo-13-wochen-liquiditaetsplan`

**Fokus:** Solo-Selbstständige: erstellt realistischen Cashplan mit Steuern, Versicherungen und Zahlungslücken; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis.

# Pricing Liquidität und Wachstum: Erstellt realistischen cashplan mit steuern

## Einsatz

Dieser Skill hilft Solo-Selbstständigen beim Themenfeld **Pricing Liquidität und Wachstum**. Schwerpunkt: erstellt realistischen Cashplan mit Steuern, Versicherungen und Zahlungslücken. Er sortiert die tatsächlichen Unterlagen, den Handlungsdruck und die wirtschaftliche Folge.

## Arbeitsweise

1. Klär zuerst Tätigkeit, Kundentyp, Bundesland/Ort, Haupt- oder Nebenerwerb, Umsatzgrößen, Fristdruck und vorhandene Dokumente.
2. Trenne Muss-Pflichten von Klugheitsmaßnahmen: Anmeldung, Steuer, Vertrag, Sozialversicherung, Datenschutz, Geldfluss und Beweis.
3. Baue eine Ampel mit Sofortmaßnahme, sauberer Dokumentation, optionaler Optimierung und Punkten für Steuerberater, Anwalt oder Behörde.
4. Formuliere am Ende genau ein brauchbares Artefakt: Checkliste, Mail, Vertragsbaustein, Widerspruchsskizze, Fristenlog, Rechnungstext oder Entscheidungsmemo.

## Ergebnis

- Kurzdiagnose in normalem Deutsch
- To-do-Liste mit Fristen und Belegen
- Risiko-/Geldfolge-Ampel
- konkreter Textbaustein oder Dokumentenplan

## Quellen- und Qualitätsregeln

- Prüfe aktuelle Beträge, Grenzwerte und Fristen in amtlichen Quellen, insbesondere Gesetze im Internet, ELSTER, DRV, KSK, Bundesagentur für Arbeit und BMWK-Existenzgründungsportal.
- Keine Steuer- oder Sozialversicherungsentscheidung ohne Hinweis, welche Angaben geschätzt sind und welche Belege fehlen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Fundlink ausgeben; keine BeckRS-/Juris-/Kommentar-Blindzitate.

## 7. `solo-anfaenger-modus`

**Fokus:** Solo-Selbstständige: erklärt Begriffe wie Freiberuf, Gewerbe, Rechnung, Umsatzsteuer und Gewinn ohne Fachnebel; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis.

# Kaltstart und Orientierung: Erklärt begriffe wie freiberuf

## Einsatz

Dieser Skill hilft Solo-Selbstständigen beim Themenfeld **Kaltstart und Orientierung**. Schwerpunkt: erklärt Begriffe wie Freiberuf, Gewerbe, Rechnung, Umsatzsteuer und Gewinn ohne Fachnebel. Er sortiert die tatsächlichen Unterlagen, den Handlungsdruck und die wirtschaftliche Folge.

## Arbeitsweise

1. Klär zuerst Tätigkeit, Kundentyp, Bundesland/Ort, Haupt- oder Nebenerwerb, Umsatzgrößen, Fristdruck und vorhandene Dokumente.
2. Trenne Muss-Pflichten von Klugheitsmaßnahmen: Anmeldung, Steuer, Vertrag, Sozialversicherung, Datenschutz, Geldfluss und Beweis.
3. Baue eine Ampel mit Sofortmaßnahme, sauberer Dokumentation, optionaler Optimierung und Punkten für Steuerberater, Anwalt oder Behörde.
4. Formuliere am Ende genau ein brauchbares Artefakt: Checkliste, Mail, Vertragsbaustein, Widerspruchsskizze, Fristenlog, Rechnungstext oder Entscheidungsmemo.

## Ergebnis

- Kurzdiagnose in normalem Deutsch
- To-do-Liste mit Fristen und Belegen
- Risiko-/Geldfolge-Ampel
- konkreter Textbaustein oder Dokumentenplan

## Quellen- und Qualitätsregeln

- Prüfe aktuelle Beträge, Grenzwerte und Fristen in amtlichen Quellen, insbesondere Gesetze im Internet, ELSTER, DRV, KSK, Bundesagentur für Arbeit und BMWK-Existenzgründungsportal.
- Keine Steuer- oder Sozialversicherungsentscheidung ohne Hinweis, welche Angaben geschätzt sind und welche Belege fehlen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Fundlink ausgeben; keine BeckRS-/Juris-/Kommentar-Blindzitate.

## 8. `solo-aufbewahrung-loeschung`

**Fokus:** Solo-Selbstständige: plant handels-/steuerliche Aufbewahrung und datenschutzrechtliche Löschung; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis.

# Datenschutz IT und Website: Plant handels-/steuerliche aufbewahrung und datenschutzrechtliche löschung

## Einsatz

Dieser Skill hilft Solo-Selbstständigen beim Themenfeld **Datenschutz IT und Website**. Schwerpunkt: plant handels-/steuerliche Aufbewahrung und datenschutzrechtliche Löschung. Er sortiert die tatsächlichen Unterlagen, den Handlungsdruck und die wirtschaftliche Folge.

## Arbeitsweise

1. Klär zuerst Tätigkeit, Kundentyp, Bundesland/Ort, Haupt- oder Nebenerwerb, Umsatzgrößen, Fristdruck und vorhandene Dokumente.
2. Trenne Muss-Pflichten von Klugheitsmaßnahmen: Anmeldung, Steuer, Vertrag, Sozialversicherung, Datenschutz, Geldfluss und Beweis.
3. Baue eine Ampel mit Sofortmaßnahme, sauberer Dokumentation, optionaler Optimierung und Punkten für Steuerberater, Anwalt oder Behörde.
4. Formuliere am Ende genau ein brauchbares Artefakt: Checkliste, Mail, Vertragsbaustein, Widerspruchsskizze, Fristenlog, Rechnungstext oder Entscheidungsmemo.

## Ergebnis

- Kurzdiagnose in normalem Deutsch
- To-do-Liste mit Fristen und Belegen
- Risiko-/Geldfolge-Ampel
- konkreter Textbaustein oder Dokumentenplan

## Quellen- und Qualitätsregeln

- Prüfe aktuelle Beträge, Grenzwerte und Fristen in amtlichen Quellen, insbesondere Gesetze im Internet, ELSTER, DRV, KSK, Bundesagentur für Arbeit und BMWK-Existenzgründungsportal.
- Keine Steuer- oder Sozialversicherungsentscheidung ohne Hinweis, welche Angaben geschätzt sind und welche Belege fehlen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Fundlink ausgeben; keine BeckRS-/Juris-/Kommentar-Blindzitate.
