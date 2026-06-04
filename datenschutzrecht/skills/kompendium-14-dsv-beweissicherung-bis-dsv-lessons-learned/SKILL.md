---
name: kompendium-14-dsv-beweissicherung-bis-dsv-lessons-learned
description: "datenschutzrecht: Konsolidiertes Skill-Kompendium 14; bündelt 10 frühere Spezialskills (dsv-beweissicherung, dsv-dsfa-update-nach-vorfall, dsv-erstgespraech-vorfallmeldung, dsv-eskalationsmatrix, dsv-interne-dokumentation-art-33-abs-5 und 5 weitere) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 14 - datenschutzrecht

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `dsv-beweissicherung` | Strukturiert die Beweissicherung nach einem Datenschutzvorfall so, dass die Beweismittel in einem späteren Bußgeldverfahren, Strafverfahren oder Zivilprozess verwertbar bleiben. Behandelt: Chain of Custody; Logging-Sicherung; Speicherabbilder; Hashes; Zeugenidentifikation; Dokumentation der Wahrnehmungen; Aufbewahrungsfristen; Datenschutzbeschränkungen bei Mitarbeiterüberwachung; Telekommunikationsgeheimnis. Output: Beweissicherungs-Protokoll mit Checkliste und Übergabeformular. Abgrenzung: keine eigene Forensik; keine Strafanzeige. |
| `dsv-dsfa-update-nach-vorfall` | Aktualisiert die Datenschutz-Folgenabschätzung nach Art. 35 DSGVO im Nachgang eines Datenschutzvorfalls. Behandelt: Erforderlichkeit der DSFA bei voraussichtlich hohem Risiko; Anpassung der Risikoanalyse; Abhilfemaßnahmen; Konsultation der Aufsichtsbehörde nach Art. 36 DSGVO bei verbleibendem hohem Risiko; Verknüpfung mit VVT und Vorfallregister. Output: DSFA-Update-Vorlage mit Pflichtfeldern. Abgrenzung: keine neue DSFA; kein Verfahrensverzeichnis. |
| `dsv-erstgespraech-vorfallmeldung` | Führt das anwaltliche oder DSB-Erstgespräch nach einem gemeldeten Datenschutzvorfall mit Geschäftsleitung oder Fachabteilung. Behandelt: Zeitstrahl der Kenntnisnahme; betroffene Systeme und Verarbeitungen; Datenkategorien und Schutzbedarfsklassen; geschätzte Anzahl betroffener Personen; Auftragsverarbeiter-Konstellation; Konzernbezug Art. 56 DSGVO; bereits eingeleitete Sofortmaßnahmen; Beweissicherung; Pressekontakte; aufsichtsbehördliche Vorkontakte. Output: strukturiertes Gesprächsprotokoll mit Lücken-Liste. Abgrenzung: keine eigene Risikobewertung; keine Behördenmeldung. |
| `dsv-eskalationsmatrix` | Definiert eine Eskalationsmatrix vom Erstmelder über Service-Desk und Datenschutzbeauftragten bis zur Geschäftsleitung und externen Beratern. Behandelt: Schwellenwerte für Eskalation; Erreichbarkeit außerhalb der Bürozeiten; Stellvertreter; Wochenend- und Feiertagsregelung; Eskalationsprotokoll; Ausweichkommunikation bei IT-Ausfall. Output: Matrix mit Stufen und Verantwortlichen plus Erreichbarkeitsplan. Abgrenzung: keine konkrete Stakeholder-Information. |
| `dsv-interne-dokumentation-art-33-abs-5` | Pflegt das interne Vorfallregister nach Art. 33 Abs. 5 DSGVO als Beweisinstrument der Rechenschaftspflicht. Behandelt: Pflichtinhalte Sachverhalt, Auswirkungen, Abhilfemaßnahmen, Bewertung; Verknüpfung mit VVT; Aufbewahrungsfristen; Schnittstelle zu Risikomanagement; Vorlage auf Anforderung der Aufsichtsbehörde; Versionierung. Output: Vorlage Vorfallregister mit Pflichtfeldern. Abgrenzung: kein Verfahrensverzeichnis Art. 30. |
| `dsv-kein-risiko-dokumentation` | Erstellt die interne Dokumentation eines Datenschutzvorfalls, der nicht an die Aufsichtsbehörde gemeldet wird, weil voraussichtlich kein Risiko für die Rechte und Freiheiten besteht. Behandelt: Pflichtangaben nach Art. 33 Abs. 5 DSGVO; Sachverhalt; Auswirkungen; Abhilfemaßnahmen; Begründung der Nichtmeldung; Risikoabwägung mit Faktoren; Aufbewahrungsfristen; Vorlage für Aufsichtsbehörde auf Anforderung. Output: vollständige Dokumentationsvorlage. Abgrenzung: keine Behördenmeldung; keine Benachrichtigung. |
| `dsv-kinderdaten-besondere-schutzbeduerftigkeit` | Bewertet einen Datenschutzvorfall mit Daten von Minderjährigen unter Berücksichtigung der besonderen Schutzbedürftigkeit nach Erwägungsgrund 38 DSGVO. Behandelt: Schulen; Kitas; Vereine; Jugendamt; Online-Dienste mit Altersbezug; Identitätsdiebstahl-Risiko; lebenslange Schadensdauer; Pflicht zur Information der Erziehungsberechtigten. Output: Memo mit Risikohochstufung und Empfehlung zur Benachrichtigung. Abgrenzung: keine konkrete Meldung; keine pädagogische Beratung. |
| `dsv-kommunikationssperre` | Etabliert eine interne und externe Kommunikationssperre nach einem Datenschutzvorfall, um voreilige Aussagen, Beweismittelvernichtung und Sammelklagenrisiken zu vermeiden. Behandelt: Single-Point-of-Contact-Regelung; interne Sprachregelung; Holdingstatement; Kunden-Hotline; Pressekontakte; Mitarbeiterinformation; Betriebsrat-Beteiligung; Sozialmedien. Output: Kommunikationssperre-Memo und Sprachregelung. Abgrenzung: keine Pressemitteilung; keine Krisen-PR. |
| `dsv-lead-authority-konzern` | Bestimmt die federführende Aufsichtsbehörde bei grenzüberschreitender Verarbeitung im Konzern nach Art. 56 DSGVO. Behandelt: Hauptniederlassung; entscheidungsmächtige Stelle; Konzernstruktur; EDSA-Leitlinien zur Lead Authority; Kooperationsverfahren Art. 60 DSGVO; Konsistenzverfahren Art. 63; Meldung an Lead Authority versus parallele Meldung an betroffene Behörden. Output: Memo zur Behördenzuständigkeit mit Begründung. Abgrenzung: keine konkrete Meldung. |
| `dsv-lessons-learned-nachbereitung` | Strukturiert die Lessons-Learned-Nachbereitung eines Datenschutzvorfalls. Behandelt: Post-Mortem-Workshop; Ursachenanalyse Root Cause; Maßnahmenkatalog; Verantwortlichkeiten und Fristen; Update interner Richtlinien; Awareness-Schulung; Übung tabletop oder ernst; Kommunikation an Geschäftsleitung; Erfolgsmessung. Output: Workshop-Leitfaden und Maßnahmen-Tracker. Abgrenzung: keine VVT- oder DSFA-Pflege; keine Bußgeldverteidigung. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `dsv-beweissicherung`

**Frühere Beschreibung:** Strukturiert die Beweissicherung nach einem Datenschutzvorfall so, dass die Beweismittel in einem späteren Bußgeldverfahren, Strafverfahren oder Zivilprozess verwertbar bleiben. Behandelt: Chain of Custody; Logging-Sicherung; Speicherabbilder; Hashes; Zeugenidentifikation; Dokumentation der Wahrnehmungen; Aufbewahrungsfristen; Datenschutzbeschränkungen bei Mitarbeiterüberwachung; Telekommunikationsgeheimnis. Output: Beweissicherungs-Protokoll mit Checkliste und Übergabeformular. Abgrenzung: keine eigene Forensik; keine Strafanzeige.

# Beweissicherung nach Datenschutzvorfall — Chain of Custody

## Triage — kläre vor der Bearbeitung

1. Welche Systeme und Speichermedien sind potenziell Beweismittel?
2. Gibt es Hinweise auf einen Innentäter und damit besondere Anforderungen an die Vertraulichkeit?
3. Liegt Telekommunikationsgeheimnis nach § 3 TTDSG vor?
4. Welche Aufbewahrungsfristen gelten für die Logs?
5. Wer übernimmt die forensische Sicherung — interne IT oder externer Forensiker?
- Was will der Mandant wirklich erreichen? (gerichtsverwertbare Beweise; saubere Akte; spätere Verteidigung)

## Rechtsgrundlagen

- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.
- **Art. 32 DSGVO** angemessene Sicherheitsmaßnahmen.
- **Art. 33 Abs. 5 DSGVO** Dokumentationspflicht.
- **§ 26 BDSG** Mitarbeiterdatenverarbeitung.
- **§ 3 TTDSG** Fernmeldegeheimnis.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu Beweisverwertungsverboten bei verdeckter Mitarbeiterkontrolle vor Ausgabe verifizieren.

## Zentrale Normen

Art. 5 Abs. 2; Art. 32; Art. 33 Abs. 5 DSGVO; § 26 BDSG; § 3 TTDSG.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Chain-of-Custody-Protokoll

Asset-ID; Beschreibung; Sicherungszeitpunkt; sichernde Person; Übergabezeitpunkt; übernehmende Person; Hashwert vor/nach Sicherung; Aufbewahrungsort; Zugriffsberechtigte; Zweck der Sicherung; Rechtsgrundlage der Verarbeitung der gesicherten Daten.

Logging: Welche Log-Quellen wurden eingefroren? Welche Retention war eingestellt? Welche Lücken gibt es?

Zeugen: Wer hat wann was wahrgenommen — in eigenen Worten und mit Zeitstempel protokollieren.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

## 2. `dsv-dsfa-update-nach-vorfall`

**Frühere Beschreibung:** Aktualisiert die Datenschutz-Folgenabschätzung nach Art. 35 DSGVO im Nachgang eines Datenschutzvorfalls. Behandelt: Erforderlichkeit der DSFA bei voraussichtlich hohem Risiko; Anpassung der Risikoanalyse; Abhilfemaßnahmen; Konsultation der Aufsichtsbehörde nach Art. 36 DSGVO bei verbleibendem hohem Risiko; Verknüpfung mit VVT und Vorfallregister. Output: DSFA-Update-Vorlage mit Pflichtfeldern. Abgrenzung: keine neue DSFA; kein Verfahrensverzeichnis.

# Datenschutz-Folgenabschätzung nach Datenschutzvorfall aktualisieren

## Triage — kläre vor der Bearbeitung

1. Gab es bisher eine DSFA für die betroffene Verarbeitung?
2. Welche Risiken haben sich realisiert oder offenbart?
3. Welche Abhilfemaßnahmen sind nachhaltig wirksam?
4. Bleibt nach Maßnahmen ein hohes Risiko bestehen?
5. Ist Konsultation Art. 36 DSGVO erforderlich?
- Was will der Mandant wirklich erreichen? (rechtskonforme Fortführung der Verarbeitung; Behördenkonsens)

## Rechtsgrundlagen

- **Art. 35 DSGVO** DSFA.
- **Art. 36 DSGVO** vorherige Konsultation.
- **Art. 32 DSGVO** TOM.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.
- **BfDI- und LDA-DSFA-Listen** (Black- und Whitelist).

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu Anforderungen an die DSFA-Aktualisierung nach Vorfall vor Ausgabe verifizieren.

## Zentrale Normen

Art. 5 Abs. 2; Art. 32; Art. 35; Art. 36 DSGVO.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — DSFA-Update-Felder

1. Beschreibung der Verarbeitung mit Bezug auf VVT.
2. Bewertung der Notwendigkeit und Verhältnismäßigkeit.
3. Bewertung der Risiken — vorher und nachher.
4. Geplante Maßnahmen — vor und nach Vorfall.
5. Konsultation der Aufsichtsbehörde nach Art. 36 DSGVO erforderlich ja/nein mit Begründung.
6. Stellungnahme des Datenschutzbeauftragten.
7. Versionsstand mit Datum und Bearbeiter.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-vvt-update-nach-vorfall` deckt das VVT ab.

## 3. `dsv-erstgespraech-vorfallmeldung`

**Frühere Beschreibung:** Führt das anwaltliche oder DSB-Erstgespräch nach einem gemeldeten Datenschutzvorfall mit Geschäftsleitung oder Fachabteilung. Behandelt: Zeitstrahl der Kenntnisnahme; betroffene Systeme und Verarbeitungen; Datenkategorien und Schutzbedarfsklassen; geschätzte Anzahl betroffener Personen; Auftragsverarbeiter-Konstellation; Konzernbezug Art. 56 DSGVO; bereits eingeleitete Sofortmaßnahmen; Beweissicherung; Pressekontakte; aufsichtsbehördliche Vorkontakte. Output: strukturiertes Gesprächsprotokoll mit Lücken-Liste. Abgrenzung: keine eigene Risikobewertung; keine Behördenmeldung.

# Erstgespräch nach gemeldetem Datenschutzvorfall — Fragenkatalog

## Triage — kläre vor der Bearbeitung

1. Wer nimmt am Erstgespräch teil — Geschäftsleitung, DSB, IT-Leitung, externer Forensiker, Versicherer?
2. Liegt eine schriftliche Vorfallmeldung vor oder erfolgt sie mündlich?
3. Ist der Vorfall bereits öffentlich oder droht öffentliche Wahrnehmung?
4. Ist eine Cyberversicherung im Spiel und welche Meldepflichten bestehen dort?
5. Gibt es einen Auftragsverarbeitervertrag oder eine gemeinsame Verantwortlichkeit?
- Was will der Mandant wirklich erreichen? (Lagebild, Meldepflichtprüfung, Bußgeldverteidigung, Haftungsminimierung)

## Rechtsgrundlagen

- **Art. 33 Abs. 1 DSGVO** Meldepflicht binnen 72 Stunden.
- **Art. 33 Abs. 2 DSGVO** Meldepflicht des Auftragsverarbeiters an den Verantwortlichen.
- **Art. 28 Abs. 3 lit. f DSGVO** Unterstützungspflicht des Auftragsverarbeiters.
- **Art. 56 DSGVO** Federführende Aufsichtsbehörde bei grenzüberschreitender Verarbeitung.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu Kenntnisbegriff Art. 33 Abs. 1 DSGVO und Reichweite der Meldepflicht des Auftragsverarbeiters vor Ausgabe verifizieren.

## Zentrale Normen

Art. 4 Nr. 12; Art. 28; Art. 33; Art. 34; Art. 56 DSGVO; § 42 BDSG.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Fragenblöcke

Zeitstrahl: Wann wurde was durch wen wahrgenommen — minutengenau wenn möglich.

Betroffene Verarbeitungen: Welche Verarbeitungstätigkeiten nach VVT sind tangiert?

Datenkategorien: Art. 9 DSGVO, Art. 10 DSGVO, Sozialdaten, Berufsgeheimnis § 203 StGB, Kinderdaten?

Personenkreis: Mitarbeiter, Kunden, Patienten, Mandanten, Schüler — geschätzte Anzahl.

Auftragsverarbeiter: Liegt AV-Vertrag vor; wer hat zuerst Kenntnis erlangt?

Konzernbezug: Hauptniederlassung in welchem EU-Mitgliedstaat?

Sofortmaßnahmen: Welche technischen und organisatorischen Schritte sind bereits erfolgt?

Beweissicherung: Logs, Images, Zeugen, Chain of Custody.

Externe Kommunikation: Presse, Kunden, Aufsichtsbehörde bereits angesprochen?

Versicherung: Cyberpolice; Meldepflicht-Trigger?

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

## 4. `dsv-eskalationsmatrix`

**Frühere Beschreibung:** Definiert eine Eskalationsmatrix vom Erstmelder über Service-Desk und Datenschutzbeauftragten bis zur Geschäftsleitung und externen Beratern. Behandelt: Schwellenwerte für Eskalation; Erreichbarkeit außerhalb der Bürozeiten; Stellvertreter; Wochenend- und Feiertagsregelung; Eskalationsprotokoll; Ausweichkommunikation bei IT-Ausfall. Output: Matrix mit Stufen und Verantwortlichen plus Erreichbarkeitsplan. Abgrenzung: keine konkrete Stakeholder-Information.

# Eskalationsmatrix Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Welche Schwellenwerte rechtfertigen welche Eskalationsstufe?
2. Welche Erreichbarkeit ist außerhalb der Bürozeiten gewährleistet?
3. Wer entscheidet über externe Eskalation (Anwalt, Versicherung, Behörde)?
4. Welche Ausweichkommunikation gilt bei IT-Ausfall (Mobilfunk, persönlich, Pager)?
5. Wer dokumentiert die Eskalationsentscheidung?
- Was will der Mandant wirklich erreichen? (klare Entscheidungswege; keine Eskalation läuft ins Leere)

## Rechtsgrundlagen

- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.
- **Art. 24 DSGVO** Verantwortung des Verantwortlichen.
- **Art. 32 DSGVO** technische und organisatorische Maßnahmen.
- **Art. 33 Abs. 1 DSGVO** Meldepflicht binnen 72 Stunden.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; aktuelle Bußgeldfälle wegen verspäteter Meldung infolge Eskalationsversagen vor Ausgabe verifizieren.

## Zentrale Normen

Art. 5 Abs. 2; Art. 24; Art. 32; Art. 33 Abs. 1 DSGVO.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Eskalationsstufen

Stufe 1: Erstmelder → Service-Desk (innerhalb 30 Minuten).
Stufe 2: Service-Desk → DSB / IT-Sicherheit (innerhalb 1 Stunde).
Stufe 3: DSB → Geschäftsleitung und Anwalt (innerhalb 4 Stunden).
Stufe 4: Geschäftsleitung → Cyberversicherung und Aufsichtsbehörde (innerhalb 24 Stunden ab Kenntnisnahme).
Stufe 5: Pressemitteilung und Mitarbeiter-Information (nach Lagebeurteilung).

Erreichbarkeit: Hauptkontakt + zwei Stellvertreter je Stufe; 24/7-Rufbereitschaft definieren.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

## 5. `dsv-interne-dokumentation-art-33-abs-5`

**Frühere Beschreibung:** Pflegt das interne Vorfallregister nach Art. 33 Abs. 5 DSGVO als Beweisinstrument der Rechenschaftspflicht. Behandelt: Pflichtinhalte Sachverhalt, Auswirkungen, Abhilfemaßnahmen, Bewertung; Verknüpfung mit VVT; Aufbewahrungsfristen; Schnittstelle zu Risikomanagement; Vorlage auf Anforderung der Aufsichtsbehörde; Versionierung. Output: Vorlage Vorfallregister mit Pflichtfeldern. Abgrenzung: kein Verfahrensverzeichnis Art. 30.

# Interne Dokumentation Art. 33 Abs. 5 DSGVO — Vorfallregister

## Triage — kläre vor der Bearbeitung

1. Wer pflegt das Register — DSB, IT-Sicherheit, Compliance?
2. Welches System (Excel, GRC-Tool, DMS)?
3. Welche Aufbewahrungsfrist gilt im Unternehmen?
4. Welche Schnittstellen zu VVT, DSFA, ISMS bestehen?
5. Wer hat Zugriff?
- Was will der Mandant wirklich erreichen? (Rechenschaftspflicht erfüllen; Bußgeldverteidigung)

## Rechtsgrundlagen

- **Art. 33 Abs. 5 DSGVO** Dokumentationspflicht.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.
- **Art. 30 DSGVO** VVT.
- **Art. 24 DSGVO** Verantwortung.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Aufbewahrungsdauer und Vorlagepflicht vor Ausgabe verifizieren.

## Zentrale Normen

Art. 5 Abs. 2; Art. 24; Art. 30; Art. 33 Abs. 5 DSGVO.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Pflichtfelder Vorfallregister

Vorfall-ID; Datum Kenntnisnahme; Datum Eintritt; Kategorie (V/I/V); Sachverhalt; betroffene Verarbeitung VVT-ID; Datenarten; Anzahl Betroffener; Folgen; ergriffene Maßnahmen; Bewertung Art. 33; Bewertung Art. 34; Meldedatum; Aktenzeichen Aufsichtsbehörde; verantwortlicher Bearbeiter; Status; Aufbewahrung bis.

Versionierung: jede Änderung mit Datum und Bearbeiter; alte Versionen revisionssicher.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-vvt-update-nach-vorfall` deckt die Aktualisierung des VVT ab.

## 6. `dsv-kein-risiko-dokumentation`

**Frühere Beschreibung:** Erstellt die interne Dokumentation eines Datenschutzvorfalls, der nicht an die Aufsichtsbehörde gemeldet wird, weil voraussichtlich kein Risiko für die Rechte und Freiheiten besteht. Behandelt: Pflichtangaben nach Art. 33 Abs. 5 DSGVO; Sachverhalt; Auswirkungen; Abhilfemaßnahmen; Begründung der Nichtmeldung; Risikoabwägung mit Faktoren; Aufbewahrungsfristen; Vorlage für Aufsichtsbehörde auf Anforderung. Output: vollständige Dokumentationsvorlage. Abgrenzung: keine Behördenmeldung; keine Benachrichtigung.

# Kein-Risiko-Dokumentation nach Art. 33 Abs. 5 DSGVO

## Triage — kläre vor der Bearbeitung

1. Auf welchen Tatsachen beruht die Einschätzung kein Risiko?
2. Welche Risikoabmilderung war vor dem Vorfall wirksam (Verschlüsselung, Pseudonymisierung)?
3. Welche Anzahl Betroffener und welche Datenkategorien?
4. Welche Aufbewahrungsfrist gilt für die Dokumentation?
5. Wer prüft die Dokumentation mit (DSB, Anwalt)?
- Was will der Mandant wirklich erreichen? (Beweislast bei Nichtmeldung erfüllen; Bußgeldverteidigung)

## Rechtsgrundlagen

- **Art. 33 Abs. 5 DSGVO** Dokumentationspflicht für jeden Vorfall.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.
- **Erwägungsgrund 85 DSGVO** Voraussichtlich-kein-Risiko-Ausnahme.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Beweislastverteilung bei Nichtmeldung vor Ausgabe verifizieren.

## Zentrale Normen

Art. 33 Abs. 5; Art. 5 Abs. 2 DSGVO; Erwägungsgrund 85.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Inhaltsraster

1. Sachverhalt: was ist passiert; wann; in welchem System.
2. Auswirkungen: welche Datenkategorien; welche Betroffenenanzahl; welche Identifizierbarkeit.
3. Risikoabwägung: Faktoren mit Reasoning vor Conclusion; warum voraussichtlich kein Risiko.
4. Abhilfemaßnahmen: was wurde getan; was wird getan; bis wann.
5. Verzicht auf Meldung: begründete Conclusion mit Bezug auf Risikobewertung.
6. Verzicht auf Benachrichtigung: begründete Conclusion zu Art. 34 DSGVO.
7. Aufbewahrung: drei Jahre Mindestempfehlung; im Verfahrensverzeichnis verlinken.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-interne-dokumentation-art-33-abs-5` deckt die Dokumentation auch fuer gemeldete Faelle ab.

## 7. `dsv-kinderdaten-besondere-schutzbeduerftigkeit`

**Frühere Beschreibung:** Bewertet einen Datenschutzvorfall mit Daten von Minderjährigen unter Berücksichtigung der besonderen Schutzbedürftigkeit nach Erwägungsgrund 38 DSGVO. Behandelt: Schulen; Kitas; Vereine; Jugendamt; Online-Dienste mit Altersbezug; Identitätsdiebstahl-Risiko; lebenslange Schadensdauer; Pflicht zur Information der Erziehungsberechtigten. Output: Memo mit Risikohochstufung und Empfehlung zur Benachrichtigung. Abgrenzung: keine konkrete Meldung; keine pädagogische Beratung.

# Kinderdaten im Datenschutzvorfall — besondere Schutzbedürftigkeit

## Triage — kläre vor der Bearbeitung

1. Wie alt sind die betroffenen Kinder und Jugendlichen?
2. Welche Datenkategorien sind betroffen (Schule, Gesundheit, Wohnort)?
3. Wer ist Adressat der Benachrichtigung — Kind, Erziehungsberechtigte, Einrichtung?
4. Liegt eine besondere Schutzbeziehung vor (Schule, Klinik, Jugendamt)?
5. Welche Aufsicht ist neben Datenschutzbehörde involviert (Schulaufsicht, Jugendamt)?
- Was will der Mandant wirklich erreichen? (rechtskonforme Information ohne Sekundärschäden)

## Rechtsgrundlagen

- **Art. 8 DSGVO** besondere Anforderungen Kinder.
- **Erwägungsgrund 38 DSGVO** besondere Schutzbedürftigkeit.
- **Art. 34 Abs. 2 DSGVO** klare und einfache Sprache.
- **§ 22 BDSG** Verarbeitung besonderer Kategorien.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu Bußgeldverschärfungen bei Kinderdaten und Informationspflichten gegenüber Erziehungsberechtigten vor Ausgabe verifizieren.

## Zentrale Normen

Art. 8; Art. 34 Abs. 2 DSGVO; Erwägungsgrund 38; § 22 BDSG.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Sonderaspekte Kinderdaten

Sprache: doppelte Adressierung — Erziehungsberechtigte und altersgerecht Kind.

Risikohochstufung: Identitätsdiebstahl wirkt lebenslang; Reputation wirkt früh; daher regelmäßig hohes Risiko.

Schnittstellen: Schulaufsicht, Jugendamt, Kinder- und Jugendpsychiatrische Dienste je nach Kontext einbeziehen.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-art-9-besondere-kategorien` deckt Gesundheitsdaten und sensible Kategorien ab.

## 8. `dsv-kommunikationssperre`

**Frühere Beschreibung:** Etabliert eine interne und externe Kommunikationssperre nach einem Datenschutzvorfall, um voreilige Aussagen, Beweismittelvernichtung und Sammelklagenrisiken zu vermeiden. Behandelt: Single-Point-of-Contact-Regelung; interne Sprachregelung; Holdingstatement; Kunden-Hotline; Pressekontakte; Mitarbeiterinformation; Betriebsrat-Beteiligung; Sozialmedien. Output: Kommunikationssperre-Memo und Sprachregelung. Abgrenzung: keine Pressemitteilung; keine Krisen-PR.

# Kommunikationssperre nach Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Ist der Vorfall bereits öffentlich oder droht öffentliche Wahrnehmung in Stunden oder Tagen?
2. Wer ist Single Point of Contact für Anfragen?
3. Welche Betriebsratspflichten bestehen bei Mitarbeiterinformation?
4. Welche Verträge verpflichten zu Vorabinformationen an Großkunden?
5. Welche Aufsichtsbehörde ist zuständig und welche eigene Pressepolitik hat sie?
- Was will der Mandant wirklich erreichen? (Ordnung im Chaos; keine voreiligen Festlegungen)

## Rechtsgrundlagen

- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.
- **Art. 34 Abs. 2 DSGVO** Inhalt der Benachrichtigung — kein Übermaß und keine voreiligen Festlegungen.
- **§ 87 Abs. 1 Nr. 1 BetrVG** Mitbestimmung Ordnung des Betriebs.
- **§ 80 Abs. 1 BetrVG** Aufgaben des Betriebsrats.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; aktuelle Entscheidungen zu Auskunftsansprüchen Betroffener im laufenden Vorfall vor Ausgabe verifizieren.

## Zentrale Normen

Art. 5 Abs. 2; Art. 34 Abs. 2 DSGVO; § 80; § 87 Abs. 1 Nr. 1 BetrVG.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Sprachregelung Holdingstatement

Wir prüfen derzeit einen Vorfall im Bereich [Bezeichnung]. Datenschutz und Sicherheit unserer Kunden haben für uns höchste Priorität. Sobald belastbare Erkenntnisse vorliegen, informieren wir die zuständige Aufsichtsbehörde und die Betroffenen entsprechend den gesetzlichen Anforderungen. Bis dahin bitten wir um Verständnis, dass wir keine Spekulationen kommentieren.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

## 9. `dsv-lead-authority-konzern`

**Frühere Beschreibung:** Bestimmt die federführende Aufsichtsbehörde bei grenzüberschreitender Verarbeitung im Konzern nach Art. 56 DSGVO. Behandelt: Hauptniederlassung; entscheidungsmächtige Stelle; Konzernstruktur; EDSA-Leitlinien zur Lead Authority; Kooperationsverfahren Art. 60 DSGVO; Konsistenzverfahren Art. 63; Meldung an Lead Authority versus parallele Meldung an betroffene Behörden. Output: Memo zur Behördenzuständigkeit mit Begründung. Abgrenzung: keine konkrete Meldung.

# Federführende Aufsichtsbehörde im Konzern — Art. 56 DSGVO

## Triage — kläre vor der Bearbeitung

1. Welche Hauptniederlassung hat die Verantwortliche im EU-Sinn?
2. Wer trifft die Verarbeitungsentscheidungen tatsächlich?
3. Welche Mitgliedstaaten sind betroffen?
4. Gibt es eine deutsche Tochter mit eigener Aufsichtsbehörde?
5. Ist eine parallele Meldung an mehrere Behörden ratsam?
- Was will der Mandant wirklich erreichen? (richtige Behörde; Vermeidung von Doppelverfahren)

## Rechtsgrundlagen

- **Art. 56 DSGVO** federführende Aufsichtsbehörde.
- **Art. 60 DSGVO** Kooperation.
- **Art. 63 DSGVO** Konsistenz.
- **Art. 4 Nr. 16 DSGVO** Hauptniederlassung.
- **EDSA-Leitlinien zur Bestimmung der Lead Authority**.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu EuGH-Entscheidungen zur Auslegung Art. 56 DSGVO vor Ausgabe verifizieren.

## Zentrale Normen

Art. 4 Nr. 16; Art. 56; Art. 60; Art. 63 DSGVO.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Bestimmungsraster

1. Hauptniederlassung identifizieren.
2. Entscheidungsmacht prüfen — wer steuert die Verarbeitung?
3. Lead Authority benennen; weitere betroffene Behörden auflisten.
4. Meldung an Lead Authority; informierende Mitteilung an deutsche Behörde, wenn deutsche Niederlassung beteiligt.
5. Sprachpolitik: Lead Authority erhält Meldung in deren Amtssprache.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-meldung-bfdi` und `dsv-meldung-<land>` decken konkrete Einreichung ab.

## 10. `dsv-lessons-learned-nachbereitung`

**Frühere Beschreibung:** Strukturiert die Lessons-Learned-Nachbereitung eines Datenschutzvorfalls. Behandelt: Post-Mortem-Workshop; Ursachenanalyse Root Cause; Maßnahmenkatalog; Verantwortlichkeiten und Fristen; Update interner Richtlinien; Awareness-Schulung; Übung tabletop oder ernst; Kommunikation an Geschäftsleitung; Erfolgsmessung. Output: Workshop-Leitfaden und Maßnahmen-Tracker. Abgrenzung: keine VVT- oder DSFA-Pflege; keine Bußgeldverteidigung.

# Lessons Learned und Nachbereitung Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Wer nimmt am Post-Mortem teil (Just Culture sicherstellen)?
2. Welche Wahrheits-Suche-Kultur ist möglich (No-Blame)?
3. Welche Ursachenanalyse-Methode (5-Why; Ishikawa) passt?
4. Welcher Maßnahmen-Tracker wird verwendet?
5. Wer überwacht die Umsetzung mit Fristen?
- Was will der Mandant wirklich erreichen? (echte Verbesserung; Bußgeldmilderung; Compliance-Reife)

## Rechtsgrundlagen

- **Art. 24 DSGVO** Verantwortung.
- **Art. 32 DSGVO** TOM.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.
- **Art. 33 Abs. 5 DSGVO** Dokumentation.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu Bußgeldmilderungen bei nachweislicher Lessons-Learned-Umsetzung vor Ausgabe verifizieren.

## Zentrale Normen

Art. 5 Abs. 2; Art. 24; Art. 32; Art. 33 Abs. 5 DSGVO.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Workshop-Ablauf

1. Eröffnung — Ziel; Just Culture; Vertraulichkeit.
2. Zeitleiste rekonstruieren — minutiös.
3. Ursachenanalyse — 5-Why oder Ishikawa.
4. Maßnahmen ableiten — technisch und organisatorisch.
5. Verantwortlichkeiten und Fristen festlegen.
6. Schulung und Awareness planen.
7. Übungstermin Tabletop in sechs Monaten festsetzen.
8. Erfolgsmessung definieren — KPIs.
9. Bericht an Geschäftsleitung mit klarem Maßnahmenstatus.
10. Anonymisierte Lessons-Learned-Notiz für Branchenaustausch (optional).

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-vvt-update-nach-vorfall` und `dsv-dsfa-update-nach-vorfall` decken die Compliance-Aktualisierung ab.
- `dsv-bussgeldverteidigung-art-83` deckt die Verteidigung ab.
