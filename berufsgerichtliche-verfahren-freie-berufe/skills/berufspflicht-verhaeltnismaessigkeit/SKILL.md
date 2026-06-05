---
name: berufspflicht-verhaeltnismaessigkeit
description: "Berufspflicht Verhaeltnismaessigkeit im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Berufspflicht und Verhältnismäßigkeit (Präventions- und, Berufspflicht und Verhältnismäßigkeit (Verteidigungs- und, Berufsrecht KI-Nutzung (Präventions- und Organisationspaket), Berufsrecht KI-Nutzung (Verteidigungs- und Kammerantwort). Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Berufspflicht Verhaeltnismaessigkeit

## Arbeitsbereich

Dieser Skill behandelt **Berufspflicht Verhaeltnismaessigkeit** als zusammenhängenden Arbeitsgang im Berufsgerichtliche Verfahren freier Berufe. Im Mittelpunkt steht die Prüfung von Berufspflicht und Verhältnismäßigkeit (Präventions- und, Berufspflicht und Verhältnismäßigkeit (Verteidigungs- und, Berufsrecht KI-Nutzung (Präventions- und Organisationspaket) und weiteren verwandten Aspekten. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `berufspflicht-und-verhaeltnismaessigkeit-praevention` | Berufspflicht und Verhältnismäßigkeit (Präventions- und Organisationspaket): steuert Pflichtverletzung, Schuld, Sanktion, Wiederholungsgefahr und mildere Mittel mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt. |
| `berufspflicht-und-verhaeltnismaessigkeit-verteidigung` | Berufspflicht und Verhältnismäßigkeit (Verteidigungs- und Kammerantwort): steuert Pflichtverletzung, Schuld, Sanktion, Wiederholungsgefahr und mildere Mittel mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt. |
| `berufsrecht-ki-nutzung-praevention` | Berufsrecht KI-Nutzung (Präventions- und Organisationspaket): steuert KI-Einsatz in Kanzlei/Praxis, Mandatsdaten, Kontrolle, Transparenz und Dokumentation mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt. |
| `berufsrecht-ki-nutzung-verteidigung` | Berufsrecht KI-Nutzung (Verteidigungs- und Kammerantwort): steuert KI-Einsatz in Kanzlei/Praxis, Mandatsdaten, Kontrolle, Transparenz und Dokumentation mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt. |

## Arbeitsweg

- Rolle und Ziel im Berufsgerichtliche Verfahren Freie Berufe klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO §§ 113 ff., BNotO §§ 95 ff., StBerG §§ 89 ff., WPO §§ 67 ff., AnwGH, BGH (Anwaltssenat) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `berufspflicht-und-verhaeltnismaessigkeit-praevention`

**Fokus:** Berufspflicht und Verhältnismäßigkeit (Präventions- und Organisationspaket): steuert Pflichtverletzung, Schuld, Sanktion, Wiederholungsgefahr und mildere Mittel mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt.

# Berufspflicht und Verhältnismäßigkeit: Präventions- und Organisationspaket

## Fachkern: Berufspflicht und Verhältnismäßigkeit: Präventions- und Organisationspaket
- **Spezialgegenstand:** Berufspflicht und Verhältnismäßigkeit: Präventions- und Organisationspaket wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Berufspflicht und Verhältnismäßigkeit: Präventions- und Organisationspaket** im Bereich **Berufsgerichtliche Verfahren Freie Berufe**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** Pflichtverletzung, Schuld, Sanktion, Wiederholungsgefahr und mildere Mittel - Präventions- und Organisationspaket

## Sofortsortierung

1. Beteiligte, Rolle und Kommunikationskanal klären: Verbraucher, Behörde, Kammer, Gericht, Plattform, Bank, Kammer oder Verfahrensgegner.
2. Fristen, Zustellungen, Aktenzeichen, Anhörungen, Mahnungen, Bescheide und Vollstreckungsdrohungen zuerst isolieren.
3. Zahlungen, Anerkenntnisse, Aussagen gegenüber Polizei/Behörde/Kammer und irreversible Handlungen als rote Zone markieren.
4. Fehlende Belege konkret nachfordern: Vertrag, Rechnung, AGB, Screenshot, Sendungsnummer, Bescheid, Protokoll, Vollmacht, Zustellnachweis.
5. Den kleinsten sicheren nächsten Schritt formulieren, bevor ein großer Streit eröffnet wird.

## Prüfprogramm

- **Normen- und Quellenanker:** Berufsgesetze, Verfassungsrecht Art. 12 GG, Verhältnismäßigkeit und Sanktionspraxis live prüfen
- **Tatsachenmatrix:** sichere Tatsachen, streitige Tatsachen, fehlende Dokumente und Beweisrisiken getrennt ausgeben.
- **Kommunikationsstrategie:** sachlich, knapp, fristwahrend; keine unnötigen Zusatzinformationen, keine vorschnellen Schuldanerkenntnisse.
- **Gegenposition:** die stärkste plausible Gegenseite darstellen und sagen, welche Unterlage oder Norm sie trägt oder entkräftet.
- **Entscheidungspfad:** sofort handeln, nachfordern, zahlen unter Vorbehalt, widersprechen, Beschwerde, Rechtsbehelf, Vergleich oder professionelle Hilfe.

## Typische Stolperstellen

- Kammerpost nicht wie normale Korrespondenz behandeln.
- Mandatsgeheimnis, Selbstbelastung und Versicherungsmeldung getrennt prüfen.
- Sofortvollzug, Zulassung und Reputationsschaden als eigene Risikoebenen führen.

## Arbeitsprodukte

Erzeuge Organisationsanweisung, Checkliste, Schulung, Vorlagen, Eskalationslogik und Nachweisordner; immer mit Fristenblatt, Belegmatrix, Risikoampel und nächstem Schriftsatzbaustein.

## Prompts, die dieser Skill stellen soll

- Welche Kammer/Aufsicht handelt?
- Geht es um Anhörung, Rüge, Anschuldigung, Zulassungsmaßnahme oder Rechtsmittel?

## Quellenhygiene

Keine erfundenen Fundstellen, keine BeckRS-/juris-Blindzitate. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei Behörden-, Berufs-, Verbraucher- und Verfahrensrecht zuerst die aktuelle amtliche Normfassung und die zuständige öffentliche Stelle prüfen.

## 2. `berufspflicht-und-verhaeltnismaessigkeit-verteidigung`

**Fokus:** Berufspflicht und Verhältnismäßigkeit (Verteidigungs- und Kammerantwort): steuert Pflichtverletzung, Schuld, Sanktion, Wiederholungsgefahr und mildere Mittel mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt.

# Berufspflicht und Verhältnismäßigkeit: Verteidigungs- und Kammerantwort

## Fachkern: Berufspflicht und Verhältnismäßigkeit: Verteidigungs- und Kammerantwort
- **Spezialgegenstand:** Berufspflicht und Verhältnismäßigkeit: Verteidigungs- und Kammerantwort wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Berufspflicht und Verhältnismäßigkeit: Verteidigungs- und Kammerantwort** im Bereich **Berufsgerichtliche Verfahren Freie Berufe**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** Pflichtverletzung, Schuld, Sanktion, Wiederholungsgefahr und mildere Mittel - Verteidigungs- und Kammerantwort

## Sofortsortierung

1. Beteiligte, Rolle und Kommunikationskanal klären: Verbraucher, Behörde, Kammer, Gericht, Plattform, Bank, Kammer oder Verfahrensgegner.
2. Fristen, Zustellungen, Aktenzeichen, Anhörungen, Mahnungen, Bescheide und Vollstreckungsdrohungen zuerst isolieren.
3. Zahlungen, Anerkenntnisse, Aussagen gegenüber Polizei/Behörde/Kammer und irreversible Handlungen als rote Zone markieren.
4. Fehlende Belege konkret nachfordern: Vertrag, Rechnung, AGB, Screenshot, Sendungsnummer, Bescheid, Protokoll, Vollmacht, Zustellnachweis.
5. Den kleinsten sicheren nächsten Schritt formulieren, bevor ein großer Streit eröffnet wird.

## Prüfprogramm

- **Normen- und Quellenanker:** Berufsgesetze, Verfassungsrecht Art. 12 GG, Verhältnismäßigkeit und Sanktionspraxis live prüfen
- **Tatsachenmatrix:** sichere Tatsachen, streitige Tatsachen, fehlende Dokumente und Beweisrisiken getrennt ausgeben.
- **Kommunikationsstrategie:** sachlich, knapp, fristwahrend; keine unnötigen Zusatzinformationen, keine vorschnellen Schuldanerkenntnisse.
- **Gegenposition:** die stärkste plausible Gegenseite darstellen und sagen, welche Unterlage oder Norm sie trägt oder entkräftet.
- **Entscheidungspfad:** sofort handeln, nachfordern, zahlen unter Vorbehalt, widersprechen, Beschwerde, Rechtsbehelf, Vergleich oder professionelle Hilfe.

## Typische Stolperstellen

- Kammerpost nicht wie normale Korrespondenz behandeln.
- Mandatsgeheimnis, Selbstbelastung und Versicherungsmeldung getrennt prüfen.
- Sofortvollzug, Zulassung und Reputationsschaden als eigene Risikoebenen führen.

## Arbeitsprodukte

Erzeuge Stellungnahme, Akteneinsicht, Bestreiten, Einordnung, Entlastung, Wiedergutmachung und Sanktionsabwehr; immer mit Fristenblatt, Belegmatrix, Risikoampel und nächstem Schriftsatzbaustein.

## Prompts, die dieser Skill stellen soll

- Welche Kammer/Aufsicht handelt?
- Geht es um Anhörung, Rüge, Anschuldigung, Zulassungsmaßnahme oder Rechtsmittel?

## Quellenhygiene

Keine erfundenen Fundstellen, keine BeckRS-/juris-Blindzitate. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei Behörden-, Berufs-, Verbraucher- und Verfahrensrecht zuerst die aktuelle amtliche Normfassung und die zuständige öffentliche Stelle prüfen.

## 3. `berufsrecht-ki-nutzung-praevention`

**Fokus:** Berufsrecht KI-Nutzung (Präventions- und Organisationspaket): steuert KI-Einsatz in Kanzlei/Praxis, Mandatsdaten, Kontrolle, Transparenz und Dokumentation mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt.

# Berufsrecht KI-Nutzung: Präventions- und Organisationspaket

## Fachkern: Berufsrecht KI-Nutzung: Präventions- und Organisationspaket
- **Spezialgegenstand:** Berufsrecht KI-Nutzung: Präventions- und Organisationspaket wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Berufsrecht KI-Nutzung: Präventions- und Organisationspaket** im Bereich **Berufsgerichtliche Verfahren Freie Berufe**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** KI-Einsatz in Kanzlei/Praxis, Mandatsdaten, Kontrolle, Transparenz und Dokumentation - Präventions- und Organisationspaket

## Sofortsortierung

1. Beteiligte, Rolle und Kommunikationskanal klären: Verbraucher, Behörde, Kammer, Gericht, Plattform, Bank, Kammer oder Verfahrensgegner.
2. Fristen, Zustellungen, Aktenzeichen, Anhörungen, Mahnungen, Bescheide und Vollstreckungsdrohungen zuerst isolieren.
3. Zahlungen, Anerkenntnisse, Aussagen gegenüber Polizei/Behörde/Kammer und irreversible Handlungen als rote Zone markieren.
4. Fehlende Belege konkret nachfordern: Vertrag, Rechnung, AGB, Screenshot, Sendungsnummer, Bescheid, Protokoll, Vollmacht, Zustellnachweis.
5. Den kleinsten sicheren nächsten Schritt formulieren, bevor ein großer Streit eröffnet wird.

## Prüfprogramm

- **Normen- und Quellenanker:** BRAO/BORA bzw. Berufsrecht, DSGVO, StGB § 203, AI-Act-Schnittstellen und Kammerhinweise live prüfen
- **Tatsachenmatrix:** sichere Tatsachen, streitige Tatsachen, fehlende Dokumente und Beweisrisiken getrennt ausgeben.
- **Kommunikationsstrategie:** sachlich, knapp, fristwahrend; keine unnötigen Zusatzinformationen, keine vorschnellen Schuldanerkenntnisse.
- **Gegenposition:** die stärkste plausible Gegenseite darstellen und sagen, welche Unterlage oder Norm sie trägt oder entkräftet.
- **Entscheidungspfad:** sofort handeln, nachfordern, zahlen unter Vorbehalt, widersprechen, Beschwerde, Rechtsbehelf, Vergleich oder professionelle Hilfe.

## Typische Stolperstellen

- Kammerpost nicht wie normale Korrespondenz behandeln.
- Mandatsgeheimnis, Selbstbelastung und Versicherungsmeldung getrennt prüfen.
- Sofortvollzug, Zulassung und Reputationsschaden als eigene Risikoebenen führen.

## Arbeitsprodukte

Erzeuge Organisationsanweisung, Checkliste, Schulung, Vorlagen, Eskalationslogik und Nachweisordner; immer mit Fristenblatt, Belegmatrix, Risikoampel und nächstem Schriftsatzbaustein.

## Prompts, die dieser Skill stellen soll

- Welche Kammer/Aufsicht handelt?
- Geht es um Anhörung, Rüge, Anschuldigung, Zulassungsmaßnahme oder Rechtsmittel?

## Quellenhygiene

Keine erfundenen Fundstellen, keine BeckRS-/juris-Blindzitate. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei Behörden-, Berufs-, Verbraucher- und Verfahrensrecht zuerst die aktuelle amtliche Normfassung und die zuständige öffentliche Stelle prüfen.

## 4. `berufsrecht-ki-nutzung-verteidigung`

**Fokus:** Berufsrecht KI-Nutzung (Verteidigungs- und Kammerantwort): steuert KI-Einsatz in Kanzlei/Praxis, Mandatsdaten, Kontrolle, Transparenz und Dokumentation mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Arbeitsprodukt.

# Berufsrecht KI-Nutzung: Verteidigungs- und Kammerantwort

## Fachkern: Berufsrecht KI-Nutzung: Verteidigungs- und Kammerantwort
- **Spezialgegenstand:** Berufsrecht KI-Nutzung: Verteidigungs- und Kammerantwort wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BRAO/BORA, BNotO, StBerG/BOStB, WPO/BS WP, PAO/BOPA, RDG/RVG, Kammerverfahren, Berufsgerichtsbarkeit und Verwaltungsrechtsschutz.
- **Entscheidende Weiche:** Bestimme Berufsgruppe, Pflichtnorm, Kammerzuständigkeit, Anhörung, Verteidigungsziel, Sanktion, Sofortmaßnahme und Reputationsschutz.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Berufsrecht KI-Nutzung: Verteidigungs- und Kammerantwort** im Bereich **Berufsgerichtliche Verfahren Freie Berufe**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** KI-Einsatz in Kanzlei/Praxis, Mandatsdaten, Kontrolle, Transparenz und Dokumentation - Verteidigungs- und Kammerantwort

## Sofortsortierung

1. Beteiligte, Rolle und Kommunikationskanal klären: Verbraucher, Behörde, Kammer, Gericht, Plattform, Bank, Kammer oder Verfahrensgegner.
2. Fristen, Zustellungen, Aktenzeichen, Anhörungen, Mahnungen, Bescheide und Vollstreckungsdrohungen zuerst isolieren.
3. Zahlungen, Anerkenntnisse, Aussagen gegenüber Polizei/Behörde/Kammer und irreversible Handlungen als rote Zone markieren.
4. Fehlende Belege konkret nachfordern: Vertrag, Rechnung, AGB, Screenshot, Sendungsnummer, Bescheid, Protokoll, Vollmacht, Zustellnachweis.
5. Den kleinsten sicheren nächsten Schritt formulieren, bevor ein großer Streit eröffnet wird.

## Prüfprogramm

- **Normen- und Quellenanker:** BRAO/BORA bzw. Berufsrecht, DSGVO, StGB § 203, AI-Act-Schnittstellen und Kammerhinweise live prüfen
- **Tatsachenmatrix:** sichere Tatsachen, streitige Tatsachen, fehlende Dokumente und Beweisrisiken getrennt ausgeben.
- **Kommunikationsstrategie:** sachlich, knapp, fristwahrend; keine unnötigen Zusatzinformationen, keine vorschnellen Schuldanerkenntnisse.
- **Gegenposition:** die stärkste plausible Gegenseite darstellen und sagen, welche Unterlage oder Norm sie trägt oder entkräftet.
- **Entscheidungspfad:** sofort handeln, nachfordern, zahlen unter Vorbehalt, widersprechen, Beschwerde, Rechtsbehelf, Vergleich oder professionelle Hilfe.

## Typische Stolperstellen

- Kammerpost nicht wie normale Korrespondenz behandeln.
- Mandatsgeheimnis, Selbstbelastung und Versicherungsmeldung getrennt prüfen.
- Sofortvollzug, Zulassung und Reputationsschaden als eigene Risikoebenen führen.

## Arbeitsprodukte

Erzeuge Stellungnahme, Akteneinsicht, Bestreiten, Einordnung, Entlastung, Wiedergutmachung und Sanktionsabwehr; immer mit Fristenblatt, Belegmatrix, Risikoampel und nächstem Schriftsatzbaustein.

## Prompts, die dieser Skill stellen soll

- Welche Kammer/Aufsicht handelt?
- Geht es um Anhörung, Rüge, Anschuldigung, Zulassungsmaßnahme oder Rechtsmittel?

## Quellenhygiene

Keine erfundenen Fundstellen, keine BeckRS-/juris-Blindzitate. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei Behörden-, Berufs-, Verbraucher- und Verfahrensrecht zuerst die aktuelle amtliche Normfassung und die zuständige öffentliche Stelle prüfen.
