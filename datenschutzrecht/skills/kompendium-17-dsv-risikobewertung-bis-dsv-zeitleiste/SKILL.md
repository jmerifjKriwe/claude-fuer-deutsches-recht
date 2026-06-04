---
name: kompendium-17-dsv-risikobewertung-bis-dsv-zeitleiste
description: "datenschutzrecht: Konsolidiertes Skill-Kompendium 17; bündelt 10 frühere Spezialskills (dsv-risikobewertung-enisa-schweregrad, dsv-risikobewertung-schwellen-art-33-34, dsv-schnelltriage-risiko, dsv-sofortmassnahmen-checkliste, dsv-sozialdaten-sgb und 5 weitere) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 17 - datenschutzrecht

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `dsv-risikobewertung-enisa-schweregrad` | Wendet die ENISA-Methodik Recommendations for a methodology of the assessment of severity of personal data breaches auf einen konkreten Vorfall an. Behandelt: Data Processing Context DPC; Ease of Identification EI; Circumstances of Breach CB; Schweregradformel SE = DPC × EI + CB; vier Stufen Low Medium High Very High; Übersetzung in Meldepflicht Art. 33 und Benachrichtigung Art. 34 DSGVO. Output: quantitative ENISA-Bewertung mit Faktoren und Schwellenwerten. Abgrenzung: keine EDSA-Beispielmethodik; keine Behördenmeldung. |
| `dsv-risikobewertung-schwellen-art-33-34` | Strukturiert die Schwellenwertentscheidung nach Art. 33 und Art. 34 DSGVO als anwaltlichen Entscheidungsbaum. Behandelt: voraussichtlich-kein-Risiko-Schwelle Art. 33 Abs. 1; Meldeschwelle; voraussichtlich-hohes-Risiko Art. 34 Abs. 1; Ausnahmen Art. 34 Abs. 3 (technische Schutzmaßnahmen, nachträgliche Risikominderung, unverhältnismäßiger Aufwand); EDSA-Auslegung; deutsche Praxis. Output: Entscheidungsbaum mit Begründungstexten für jede Verzweigung. Abgrenzung: keine konkrete Meldung; keine ENISA-Quantifizierung. |
| `dsv-schnelltriage-risiko` | Liefert in 15-30 Minuten eine Schnelltriage zum Risiko eines gemeldeten Datenschutzvorfalls als Entscheidungsgrundlage für die 72-Stunden-Meldung. Behandelt: Vertraulichkeits-, Integritäts- und Verfügbarkeitsverletzung; Datenkategorien; Identifizierbarkeit; Anzahl betroffener Personen; Reversibilität; besondere Schutzbedürftigkeit Kinder Patienten Mitarbeiter; Eintrittswahrscheinlichkeit und Schwere; vorläufige Ampel grün gelb rot schwarz. Output: Triage-Memo mit Begründung und Empfehlung Meldung Ja/Nein/Vorsorglich. Abgrenzung: ersetzt nicht die vertiefte Bewertung nach EDSA-Leitlinien und ENISA. |
| `dsv-sofortmassnahmen-checkliste` | Generiert eine priorisierte Sofortmaßnahmen-Checkliste innerhalb der ersten Stunden nach Bekanntwerden eines Datenschutzvorfalls. Behandelt: Eindämmung; Beweissicherung; Zugriffsbeschränkung; Passwort-Reset; Account-Sperrung; Netzwerksegmentierung; forensische Erstsicherung; Benachrichtigung interner Stakeholder; Versicherungsmeldung; Logging-Sicherung; Backups schützen; Pressepolitik; rechtliche Sofortmaßnahmen bei Insider-Tätern oder Strafanzeige. Output: priorisierte Maßnahmenliste mit Verantwortlichen und Zeitvorgaben. Abgrenzung: keine Behördenmeldung; keine vertiefte Forensik. |
| `dsv-sozialdaten-sgb` | Bewertet einen Datenschutzvorfall bei Sozialleistungsträgern, Sozialversicherungen und sozialen Diensten nach den Sondervorschriften der Sozialgesetzbücher. Behandelt: Sozialdatenbegriff § 67 SGB X; Sozialgeheimnis § 35 SGB I; Verhältnis zur DSGVO; Meldepflicht nach § 83a SGB X; besondere Bußgeldvorschriften; Aufsichtsstruktur Bund/Länder. Output: Memo zur Meldepflicht-Doppelspur und Empfehlung. Abgrenzung: keine konkrete Behördenmeldung. |
| `dsv-spezialfaelle-uebersicht` | Liefert eine schnelle Übersicht über häufige Spezialfälle eines Datenschutzvorfalls und verweist auf vertiefte Skills. Behandelt: Ransomware; Insider-Threat; Fehlversand E-Mail/Brief; Endgeräteverlust; verlorener Datenträger; Cloud-Fehlkonfiguration; offene S3-Buckets; kompromittiertes E-Mail-Konto; Phishing-Erfolg; Schatten-IT; kompromittierter Dienstleister; Web-Defacement; Datenleck durch Whistleblower. Output: Übersichts-Matrix mit Erstbewertung und Verweisen auf vertiefte Skills. Abgrenzung: ersetzt nicht die Einzelbewertung. |
| `dsv-stakeholder-mapping` | Kartiert alle internen und externen Stakeholder eines Datenschutzvorfalls inklusive Informationsbedarf, Zeitpunkt und Verantwortlicher. Behandelt: Geschäftsleitung; Datenschutzbeauftragter; IT-Sicherheit; Betriebsrat; Auftragsverarbeiter; gemeinsam Verantwortliche; Cyberversicherung; Aufsichtsbehörde; Strafverfolgungsbehörden; Betroffene; Großkunden mit Vertragsklauseln; Presse; Sozialmedien. Output: Stakeholder-Matrix mit Eskalations- und Informationsplan. Abgrenzung: keine konkreten Schreiben. |
| `dsv-tonfall-krisenkommunikation` | Bestimmt den richtigen Tonfall und die Sprachregelung in der Krisenkommunikation nach einem Datenschutzvorfall. Behandelt: Vermeidung von Verharmlosung; Vermeidung von Panikmache; matter-of-factly; Reasoning vor Conclusion; Vermeidung selbstbelastender Aussagen; keine voreiligen Schuldzuweisungen; Empathie ohne Anerkenntnis; rechtliche Grenzen (§ 824 BGB; § 4 UWG; Art. 5 Abs. 1 lit. a DSGVO). Output: Sprachregel-Leitfaden mit Beispielsätzen Do/Don't. Abgrenzung: keine Pressemitteilung; keine individuelle Benachrichtigung. |
| `dsv-verdacht-vs-festgestellt` | Bewertet, ob der Mandant bereits Kenntnis von einer Verletzung im Sinne Art. 33 Abs. 1 DSGVO hat oder ob noch bloßer Verdacht vorliegt. Behandelt: Abgrenzung Verdacht und Kenntnis; angemessene Sicherheit der Feststellung; Pflicht zur unverzüglichen Aufklärung; Erwägungsgrund 87; Dokumentationspflichten in der Verdachtsphase; Risiko einer verspäteten Meldung. Output: Memo zur Einordnung und Begründung des Fristbeginns. Abgrenzung: keine eigene Meldung; keine Risikobewertung. |
| `dsv-zeitleiste` | Erstellt eine minutiös rekonstruierte Zeitleiste vom Eintritt der Verletzung bis zur Meldung und Benachrichtigung. Behandelt: Eintritt; Erstwahrnehmung; Meldung an Service-Desk; Eingang Datenschutzpostfach; Kenntnisbegriff Art. 33 DSGVO; 72-Stunden-Lauf; Sofortmaßnahmen; Forensik-Beauftragung; Meldung an Aufsichtsbehörde; Benachrichtigung Betroffene; Pressemitteilung; Nachmeldung. Output: tabellarische Zeitleiste mit Quellen und Rechtsfolgen. Abgrenzung: keine Risikobewertung; keine Behördenmeldung im engeren Sinne. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `dsv-risikobewertung-enisa-schweregrad`

**Frühere Beschreibung:** Wendet die ENISA-Methodik Recommendations for a methodology of the assessment of severity of personal data breaches auf einen konkreten Vorfall an. Behandelt: Data Processing Context DPC; Ease of Identification EI; Circumstances of Breach CB; Schweregradformel SE = DPC × EI + CB; vier Stufen Low Medium High Very High; Übersetzung in Meldepflicht Art. 33 und Benachrichtigung Art. 34 DSGVO. Output: quantitative ENISA-Bewertung mit Faktoren und Schwellenwerten. Abgrenzung: keine EDSA-Beispielmethodik; keine Behördenmeldung.

# ENISA-Methodik zur Schweregradbewertung von Datenschutzverletzungen

## Triage — kläre vor der Bearbeitung

1. Welche Verarbeitungskontextstufe (DPC) liegt vor — einfach, behavior, sensitive, oder highly sensitive?
2. Wie leicht sind Betroffene identifizierbar (EI von 0,25 bis 1)?
3. Welche Umstände erhöhen oder mindern das Risiko (CB-Faktoren)?
4. Welche Daten sind besonders schutzbedürftig?
5. Wie ist die quantitative Bewertung zu kommunizieren?
- Was will der Mandant wirklich erreichen? (objektivierte Bewertung; Verteidigung gegen Behörde)

## Rechtsgrundlagen

- **Art. 33 Abs. 1 DSGVO** Meldepflicht.
- **Art. 34 Abs. 1 DSGVO** Benachrichtigung.
- **Erwägungsgrund 75; 76 DSGVO**.
- **ENISA Recommendations for a methodology of the assessment of severity of personal data breaches** (2013, weiterhin in Praxis verwendet).
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Akzeptanz der ENISA-Methodik durch deutsche Aufsichtsbehörden vor Ausgabe verifizieren.

## Zentrale Normen

Art. 33 Abs. 1; Art. 34 Abs. 1; Art. 5 Abs. 2 DSGVO; ENISA-Methodik 2013.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — ENISA-Berechnung

DPC: simple data 1; behavioural data 2; sensitive data 3; highly sensitive data 4.

EI: negligible 0,25; limited 0,5; significant 0,75; maximum 1.

CB: -2 bis +0,5 je nach Umständen (Loss of confidentiality, integrity, availability; malicious intent; etc.).

SE = DPC × EI + CB.

Stufen: SE < 2 Low; 2-3 Medium; 3-4 High; > 4 Very High.

Conclusion: Meldung Art. 33 ab Medium; Benachrichtigung Art. 34 ab High.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-risikobewertung-edsa-leitlinie` ergaenzt um qualitative Beispielfallgruppen.

## 2. `dsv-risikobewertung-schwellen-art-33-34`

**Frühere Beschreibung:** Strukturiert die Schwellenwertentscheidung nach Art. 33 und Art. 34 DSGVO als anwaltlichen Entscheidungsbaum. Behandelt: voraussichtlich-kein-Risiko-Schwelle Art. 33 Abs. 1; Meldeschwelle; voraussichtlich-hohes-Risiko Art. 34 Abs. 1; Ausnahmen Art. 34 Abs. 3 (technische Schutzmaßnahmen, nachträgliche Risikominderung, unverhältnismäßiger Aufwand); EDSA-Auslegung; deutsche Praxis. Output: Entscheidungsbaum mit Begründungstexten für jede Verzweigung. Abgrenzung: keine konkrete Meldung; keine ENISA-Quantifizierung.

# Schwellenwerte Art. 33 und Art. 34 DSGVO — Entscheidungsbaum

## Triage — kläre vor der Bearbeitung

1. Liegt überhaupt eine Verletzung des Schutzes personenbezogener Daten nach Art. 4 Nr. 12 DSGVO vor?
2. Welche Wahrscheinlichkeit eines Risikos für Rechte und Freiheiten besteht?
3. Welche Schwere des Risikos ist plausibel?
4. Greift eine Ausnahme nach Art. 34 Abs. 3 DSGVO?
5. Welche Begründung trägt die Behörde wahrscheinlich mit?
- Was will der Mandant wirklich erreichen? (sichere Entscheidung; nachprüfbare Begründung)

## Rechtsgrundlagen

- **Art. 4 Nr. 12 DSGVO** Definition Verletzung.
- **Art. 33 Abs. 1 DSGVO** Meldeschwelle.
- **Art. 34 Abs. 1 DSGVO** Benachrichtigungsschwelle.
- **Art. 34 Abs. 3 DSGVO** Ausnahmen.
- **Erwägungsgrund 75; 76; 85; 86 DSGVO**.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Auslegung Art. 34 Abs. 3 lit. a DSGVO (Verschlüsselung) und lit. c (unverhältnismäßiger Aufwand) vor Ausgabe verifizieren.

## Zentrale Normen

Art. 4 Nr. 12; Art. 33 Abs. 1; Art. 34 Abs. 1; Art. 34 Abs. 3 DSGVO; Erwägungsgrund 75; 76; 85; 86.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Entscheidungsbaum

Frage 1: Verletzung im Sinne Art. 4 Nr. 12? Nein → Dokumentation reicht. Ja → Frage 2.

Frage 2: Voraussichtlich kein Risiko? Ja → keine Meldung; Dokumentation Art. 33 Abs. 5. Nein → Meldung Art. 33.

Frage 3: Voraussichtlich hohes Risiko? Nein → keine Benachrichtigung. Ja → Frage 4.

Frage 4: Art. 34 Abs. 3 DSGVO Ausnahme? Ja → öffentliche Bekanntmachung statt individueller Benachrichtigung. Nein → individuelle Benachrichtigung.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-risikobewertung-edsa-leitlinie` und `dsv-risikobewertung-enisa-schweregrad` liefern die methodische Tiefe.

## 3. `dsv-schnelltriage-risiko`

**Frühere Beschreibung:** Liefert in 15-30 Minuten eine Schnelltriage zum Risiko eines gemeldeten Datenschutzvorfalls als Entscheidungsgrundlage für die 72-Stunden-Meldung. Behandelt: Vertraulichkeits-, Integritäts- und Verfügbarkeitsverletzung; Datenkategorien; Identifizierbarkeit; Anzahl betroffener Personen; Reversibilität; besondere Schutzbedürftigkeit Kinder Patienten Mitarbeiter; Eintrittswahrscheinlichkeit und Schwere; vorläufige Ampel grün gelb rot schwarz. Output: Triage-Memo mit Begründung und Empfehlung Meldung Ja/Nein/Vorsorglich. Abgrenzung: ersetzt nicht die vertiefte Bewertung nach EDSA-Leitlinien und ENISA.

# Schnelltriage Risikoeinschätzung nach Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Welche Schutzziele sind verletzt — Vertraulichkeit, Integrität, Verfügbarkeit?
2. Welche Datenkategorien und welcher Personenkreis sind betroffen?
3. Sind besondere Kategorien nach Art. 9 DSGVO oder strafrechtsrelevante Daten nach Art. 10 DSGVO beteiligt?
4. Ist die Verletzung eingrenzbar oder breitet sie sich aus?
5. Wie viel Zeit bleibt bis zum Ende der 72-Stunden-Frist?
- Was will der Mandant wirklich erreichen? (schnelle Entscheidung; rechtssichere Begründung der Nichtmeldung)

## Rechtsgrundlagen

- **Art. 33 Abs. 1 Satz 1 DSGVO** Meldepflicht außer wenn voraussichtlich kein Risiko.
- **Art. 33 Abs. 5 DSGVO** Dokumentation auch bei Nichtmeldung.
- **Art. 34 Abs. 1 DSGVO** Benachrichtigung bei voraussichtlich hohem Risiko.
- **Erwägungsgrund 75 DSGVO** Risikofaktoren.
- **Erwägungsgrund 76 DSGVO** Wahrscheinlichkeit und Schwere des Risikos.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Schwelle voraussichtlich kein Risiko und zur Beweislast bei Nichtmeldung vor Ausgabe verifizieren.

## Zentrale Normen

Art. 4 Nr. 12; Art. 33 Abs. 1; Art. 33 Abs. 5; Art. 34 Abs. 1 DSGVO; Erwägungsgrund 75; Erwägungsgrund 76.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Schnelltriage-Raster

Schutzzielverletzung: V/I/V mit kurzer Begründung.

Datenkategorien: normale / besondere Art. 9 / strafrechtsrelevant Art. 10 / Berufsgeheimnis § 203 StGB.

Personenkreis und Anzahl: geschätzter Bereich; Identifizierbarkeit ja/nein.

Reversibilität: vollständig wiederherstellbar / teilweise / irreversibel.

Schwere: gering / mittel / hoch / sehr hoch — mit Reasoning.

Wahrscheinlichkeit: gering / mittel / hoch.

Ampelvorschlag: 🟢 keine Meldung / 🟡 Vorsorglich melden / 🔴 melden / ⚫ zusätzlich Art. 34.

Begründung: drei bis fünf Sätze für die Akte.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

## 4. `dsv-sofortmassnahmen-checkliste`

**Frühere Beschreibung:** Generiert eine priorisierte Sofortmaßnahmen-Checkliste innerhalb der ersten Stunden nach Bekanntwerden eines Datenschutzvorfalls. Behandelt: Eindämmung; Beweissicherung; Zugriffsbeschränkung; Passwort-Reset; Account-Sperrung; Netzwerksegmentierung; forensische Erstsicherung; Benachrichtigung interner Stakeholder; Versicherungsmeldung; Logging-Sicherung; Backups schützen; Pressepolitik; rechtliche Sofortmaßnahmen bei Insider-Tätern oder Strafanzeige. Output: priorisierte Maßnahmenliste mit Verantwortlichen und Zeitvorgaben. Abgrenzung: keine Behördenmeldung; keine vertiefte Forensik.

# Sofortmaßnahmen-Checkliste nach Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Ist der Angriff oder das Leck noch aktiv oder bereits gestoppt?
2. Sind Backups intakt und vom kompromittierten System getrennt?
3. Gibt es Hinweise auf einen Innentäter — dann besondere Vorsicht bei Account-Sperrungen wegen Beweismittelvernichtung?
4. Greift eine Strafanzeigepflicht oder ein Strafanzeigeinteresse?
5. Welche Verträge mit Auftragsverarbeitern oder Cyberversicherern verlangen Sofortmeldungen?
- Was will der Mandant wirklich erreichen? (Schadensbegrenzung; Beweissicherung; Compliance-Dokumentation)

## Rechtsgrundlagen

- **Art. 32 DSGVO** Pflicht zu angemessenen technischen und organisatorischen Maßnahmen einschließlich Wiederherstellungsfähigkeit.
- **Art. 33 Abs. 3 lit. c DSGVO** Angabe der ergriffenen oder vorgeschlagenen Maßnahmen in der Meldung.
- **Art. 5 Abs. 1 lit. f DSGVO** Integrität und Vertraulichkeit.
- **§ 42 BDSG** Strafvorschriften.
- **§ 274 StGB** Urkundenunterdrückung; **§ 303a StGB** Datenveränderung.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; aktuelle Entscheidungen zu Beweisverwertungsverboten bei eilig getroffenen Maßnahmen vor Ausgabe verifizieren.

## Zentrale Normen

Art. 5 Abs. 1 lit. f; Art. 32; Art. 33 Abs. 3 lit. c DSGVO; § 42 BDSG; §§ 274; 303a StGB.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Sofortmaßnahmen Priorität 1 bis 4

Priorität 1 (sofort, 0-1 h):
- Eindämmung — System isolieren oder Account sperren ohne Beweisvernichtung.
- Beweissicherung — Logs einfrieren; Speicherabbild ziehen lassen.
- Interner Alarm — DSB, Geschäftsleitung, IT-Sicherheit.
- Versicherer kontaktieren falls Cyberpolice vorhanden.

Priorität 2 (1-6 h):
- Forensiker beauftragen.
- Passwort- und Token-Reset für betroffene Konten.
- Backups vom Netz trennen.
- Kommunikationssperre bis zur Lagebeurteilung.

Priorität 3 (6-24 h):
- Detaillierte Bestandsaufnahme der betroffenen Verarbeitungen.
- Auftragsverarbeiter informieren.
- Risikoabwägung Art. 33 / Art. 34 DSGVO einleiten.

Priorität 4 (24-72 h):
- Meldung an Aufsichtsbehörde vorbereiten und absenden.
- Strafanzeige bei Insider-Verdacht prüfen.
- Pressemitteilung und Kundenkommunikation vorbereiten.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

## 5. `dsv-sozialdaten-sgb`

**Frühere Beschreibung:** Bewertet einen Datenschutzvorfall bei Sozialleistungsträgern, Sozialversicherungen und sozialen Diensten nach den Sondervorschriften der Sozialgesetzbücher. Behandelt: Sozialdatenbegriff § 67 SGB X; Sozialgeheimnis § 35 SGB I; Verhältnis zur DSGVO; Meldepflicht nach § 83a SGB X; besondere Bußgeldvorschriften; Aufsichtsstruktur Bund/Länder. Output: Memo zur Meldepflicht-Doppelspur und Empfehlung. Abgrenzung: keine konkrete Behördenmeldung.

# Sozialdaten im Datenschutzvorfall — SGB I und SGB X

## Triage — kläre vor der Bearbeitung

1. Liegen Sozialdaten im Sinne § 67 SGB X vor?
2. Welche Stelle ist Verantwortlicher — Sozialleistungsträger, Krankenkasse, Berufsgenossenschaft?
3. Welche Aufsicht ist zuständig (Bundesbeauftragte oder Landesbeauftragte)?
4. Welche Meldewege überschneiden sich (DSGVO und SGB)?
5. Welche besonderen Strafvorschriften greifen (§ 85 SGB X)?
- Was will der Mandant wirklich erreichen? (Doppelmeldung sauber abwickeln; berufs- und beamtenrechtliche Folgen vermeiden)

## Rechtsgrundlagen

- **§ 35 SGB I** Sozialgeheimnis.
- **§ 67 SGB X** Definitionen.
- **§ 83a SGB X** Meldung Datenschutzverletzungen.
- **§ 85 SGB X** Bußgeldvorschriften.
- **Art. 33 DSGVO** allgemeine Meldepflicht.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zum Verhältnis § 83a SGB X zu Art. 33 DSGVO vor Ausgabe verifizieren.

## Zentrale Normen

§ 35; § 67; § 83a; § 85 SGB X; § 35 SGB I; Art. 33 DSGVO.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Doppelspur Meldung

DSGVO-Spur: Meldung an Aufsichtsbehörde (BfDI bei Bundesbehörde oder zuständige Landesbehörde).

SGB-Spur: zusätzliche Pflichten nach § 83a SGB X; ggf. Aufsicht durch Sozialministerium.

Berichtsformate parallel halten; Konsistenz beachten.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-art-9-besondere-kategorien` deckt Gesundheitsdaten ab.
- `dsv-paragraf-203-stgb-berufsgeheimnis` deckt aerztliches Geheimnis ab.

## 6. `dsv-spezialfaelle-uebersicht`

**Frühere Beschreibung:** Liefert eine schnelle Übersicht über häufige Spezialfälle eines Datenschutzvorfalls und verweist auf vertiefte Skills. Behandelt: Ransomware; Insider-Threat; Fehlversand E-Mail/Brief; Endgeräteverlust; verlorener Datenträger; Cloud-Fehlkonfiguration; offene S3-Buckets; kompromittiertes E-Mail-Konto; Phishing-Erfolg; Schatten-IT; kompromittierter Dienstleister; Web-Defacement; Datenleck durch Whistleblower. Output: Übersichts-Matrix mit Erstbewertung und Verweisen auf vertiefte Skills. Abgrenzung: ersetzt nicht die Einzelbewertung.

# Spezialfälle Datenschutzvorfall — Übersicht für die Triage

## Triage — kläre vor der Bearbeitung

1. Welcher Spezialfall liegt vor und welche Sofortmaßnahmen prägt das?
2. Liegt ein typischer Mehrfach-Trigger vor (Ransomware = V+I+V)?
3. Welche besondere Sektoraufsicht ist betroffen (KRITIS, Finanzen, Gesundheit)?
4. Welche typischen Bußgeldhebel sind aus der Praxis bekannt?
5. Welche typischen Beweisprobleme prägen den Fall?
- Was will der Mandant wirklich erreichen? (schneller Überblick; passende vertiefte Skills wählen)

## Rechtsgrundlagen

- **Art. 32 DSGVO** Sicherheit der Verarbeitung.
- **Art. 33 DSGVO** Meldepflicht.
- **Art. 34 DSGVO** Benachrichtigung.
- **§ 8b BSIG** Meldepflicht KRITIS.
- **NIS-2-UmsuCG** (sofern in Kraft) zusätzliche Meldepflichten.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; aktuelle Ransomware-Bußgeldbescheide und Sammelklagen wegen Datenleck vor Ausgabe verifizieren.

## Zentrale Normen

Art. 32; Art. 33; Art. 34 DSGVO; § 8b BSIG.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Spezialfall-Matrix

Ransomware → V+I+V; Lösegeldverbot prüfen; KRITIS-Meldung.
Insider-Threat → Beweissicherung diskret; Strafanzeige prüfen; Mitbestimmung beachten.
Fehlversand → Empfänger kontaktieren; Vernichtungsbestätigung einholen.
Endgeräteverlust → Verschlüsselungsnachweis; Remote-Wipe protokollieren.
Cloud-Fehlkonfiguration → Konfigurationsänderung; Logs; CSP-AV-Pflichten.
Kompromittiertes E-Mail-Konto → Tokens widerrufen; Mailregeln prüfen; Phishing-Welle erwarten.
Dienstleisterleck → AV-Vertrag prüfen; Meldekette Art. 33 Abs. 2 DSGVO.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

## 7. `dsv-stakeholder-mapping`

**Frühere Beschreibung:** Kartiert alle internen und externen Stakeholder eines Datenschutzvorfalls inklusive Informationsbedarf, Zeitpunkt und Verantwortlicher. Behandelt: Geschäftsleitung; Datenschutzbeauftragter; IT-Sicherheit; Betriebsrat; Auftragsverarbeiter; gemeinsam Verantwortliche; Cyberversicherung; Aufsichtsbehörde; Strafverfolgungsbehörden; Betroffene; Großkunden mit Vertragsklauseln; Presse; Sozialmedien. Output: Stakeholder-Matrix mit Eskalations- und Informationsplan. Abgrenzung: keine konkreten Schreiben.

# Stakeholder-Mapping nach Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Welche Vertragsbeziehungen verlangen frühzeitige Information (Banken, Großkunden, Auftragsverarbeiter)?
2. Welche Aufsichtsbehörde ist primär, welche zusätzlich (Sektoraufsicht BaFin, BSI § 8b BSIG)?
3. Ist der Konzern grenzüberschreitend tätig — Lead-Authority nach Art. 56 DSGVO?
4. Gibt es Betriebsrat und welche Beteiligungsrechte?
5. Welche Sozialmedien-Kanäle hat der Mandant?
- Was will der Mandant wirklich erreichen? (kein Stakeholder vergessen; keine Doppelkommunikation)

## Rechtsgrundlagen

- **Art. 26 DSGVO** gemeinsam Verantwortliche.
- **Art. 28 DSGVO** Auftragsverarbeiter.
- **Art. 33 DSGVO** Meldepflicht.
- **Art. 56 DSGVO** federführende Aufsichtsbehörde.
- **§ 8b BSIG** Meldepflicht bei kritischen Infrastrukturen.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Abgrenzung gemeinsam Verantwortlicher und reiner Auftragsverarbeitung vor Ausgabe verifizieren.

## Zentrale Normen

Art. 26; Art. 28; Art. 33; Art. 56 DSGVO; § 8b BSIG; § 109 TKG.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Stakeholder-Matrix-Spalten

Stakeholder; Rolle; Pflicht oder freiwillig; Zeitpunkt; Verantwortlicher intern; Format der Information; abgestimmte Kernbotschaft; Eskalationsstufe.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

## 8. `dsv-tonfall-krisenkommunikation`

**Frühere Beschreibung:** Bestimmt den richtigen Tonfall und die Sprachregelung in der Krisenkommunikation nach einem Datenschutzvorfall. Behandelt: Vermeidung von Verharmlosung; Vermeidung von Panikmache; matter-of-factly; Reasoning vor Conclusion; Vermeidung selbstbelastender Aussagen; keine voreiligen Schuldzuweisungen; Empathie ohne Anerkenntnis; rechtliche Grenzen (§ 824 BGB; § 4 UWG; Art. 5 Abs. 1 lit. a DSGVO). Output: Sprachregel-Leitfaden mit Beispielsätzen Do/Don't. Abgrenzung: keine Pressemitteilung; keine individuelle Benachrichtigung.

# Tonfall und Sprache in der Krisenkommunikation nach Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Welche Zielgruppe wird angesprochen (Betroffene, Presse, Mitarbeiter, Großkunden)?
2. Welcher Markenton ist beim Mandanten etabliert?
3. Welche Aussagen sind faktenfest belegbar?
4. Welche Aussagen wären selbstbelastend im Bußgeldverfahren?
5. Welche Aussagen wären zivilrechtlich riskant?
- Was will der Mandant wirklich erreichen? (Vertrauenserhalt; keine Selbstbelastung; keine Sammelklagen-Munition)

## Rechtsgrundlagen

- **Art. 12 Abs. 1 DSGVO** klare einfache Sprache.
- **Art. 34 Abs. 2 DSGVO** Inhalt der Benachrichtigung.
- **Art. 5 Abs. 1 lit. a DSGVO** Transparenz.
- **§ 824 BGB** Kreditgefährdung.
- **§ 4 UWG** Mitbewerberschutz.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu Wortlaut-Streitigkeiten in Massendatenpannen vor Ausgabe verifizieren.

## Zentrale Normen

Art. 5 Abs. 1 lit. a; Art. 12 Abs. 1; Art. 34 Abs. 2 DSGVO; § 824 BGB; § 4 UWG.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Do/Don't

Do: konkrete Beschreibung des Vorfalls; konkrete Folgen; konkrete Empfehlungen; respektvolle Anrede; Hotline.

Don't: Pauschalentschuldigungen ohne Bezug; Schuldzuweisungen an Dritte ohne Beleg; Versprechungen Es-kann-nicht-mehr-passieren; juristische Wertungen wie kein-Risiko ohne Beleg.

Empathie ohne Anerkenntnis: Wir bedauern den Vorfall; wir verstehen Ihre Sorge; wir prüfen alle erforderlichen Schritte.

Reasoning vor Conclusion: erst Beschreibung der Lage; dann Bewertung; dann Empfehlung.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-pressemitteilung-krisenkommunikation` deckt die Pressemitteilung ab.
- `dsv-benachrichtigung-art-34-betroffene` deckt das Anschreiben ab.

## 9. `dsv-verdacht-vs-festgestellt`

**Frühere Beschreibung:** Bewertet, ob der Mandant bereits Kenntnis von einer Verletzung im Sinne Art. 33 Abs. 1 DSGVO hat oder ob noch bloßer Verdacht vorliegt. Behandelt: Abgrenzung Verdacht und Kenntnis; angemessene Sicherheit der Feststellung; Pflicht zur unverzüglichen Aufklärung; Erwägungsgrund 87; Dokumentationspflichten in der Verdachtsphase; Risiko einer verspäteten Meldung. Output: Memo zur Einordnung und Begründung des Fristbeginns. Abgrenzung: keine eigene Meldung; keine Risikobewertung.

# Verdacht versus festgestellte Verletzung — Kenntnisbegriff Art. 33 DSGVO

## Triage — kläre vor der Bearbeitung

1. Worauf basiert der Verdacht — Logeintrag, Anruf, Drittmeldung, Pressebericht?
2. Welche internen Prüfungen wurden bereits durchgeführt?
3. Liegen objektive Anhaltspunkte für eine Verletzung vor oder reine Spekulation?
4. Wie lange dauert die Aufklärung voraussichtlich?
5. Welche Sofortmaßnahmen sind während der Aufklärung sinnvoll?
- Was will der Mandant wirklich erreichen? (Rechtssicherheit beim Fristbeginn; keine voreilige Falschmeldung)

## Rechtsgrundlagen

- **Art. 33 Abs. 1 DSGVO** Meldung ab Kenntniserlangung.
- **Erwägungsgrund 87 DSGVO** unverzügliche Feststellung mit angemessener Sicherheit.
- **Art. 33 Abs. 5 DSGVO** Dokumentationspflicht auch in der Verdachtsphase.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu Maßstäben angemessener Sicherheit der Feststellung und Reichweite der Aufklärungspflicht vor Ausgabe verifizieren.

## Zentrale Normen

Art. 33 Abs. 1; Art. 33 Abs. 5; Art. 5 Abs. 2 DSGVO; Erwägungsgrund 87.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Einordnungsraster

Phase Verdacht: kein Fristbeginn; Dokumentation der eingeleiteten Aufklärungsschritte.

Phase qualifizierte Kenntnis: Fristbeginn 72 Stunden; Festlegung des Zeitpunkts.

Maßstab: ein verständiger Verantwortlicher würde von einer Verletzung ausgehen — Reasoning zuerst dann Conclusion.

Dokumentationsbausteine: was wurde wann wahrgenommen; welche Prüfungen wurden eingeleitet; welche Ergebnisse haben den Verdacht zur Kenntnis verdichtet.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

## 10. `dsv-zeitleiste`

**Frühere Beschreibung:** Erstellt eine minutiös rekonstruierte Zeitleiste vom Eintritt der Verletzung bis zur Meldung und Benachrichtigung. Behandelt: Eintritt; Erstwahrnehmung; Meldung an Service-Desk; Eingang Datenschutzpostfach; Kenntnisbegriff Art. 33 DSGVO; 72-Stunden-Lauf; Sofortmaßnahmen; Forensik-Beauftragung; Meldung an Aufsichtsbehörde; Benachrichtigung Betroffene; Pressemitteilung; Nachmeldung. Output: tabellarische Zeitleiste mit Quellen und Rechtsfolgen. Abgrenzung: keine Risikobewertung; keine Behördenmeldung im engeren Sinne.

# Zeitleiste des Datenschutzvorfalls — minutiöse Rekonstruktion

## Triage — kläre vor der Bearbeitung

1. Aus welchen Quellen lässt sich der Zeitstrahl rekonstruieren — Logs, E-Mails, Tickets, Aussagen?
2. Welche Zeitstempel sind in welcher Zeitzone protokolliert?
3. Wann genau hat der Verantwortliche im Sinne Art. 33 DSGVO Kenntnis erlangt?
4. Wann beginnt der 72-Stunden-Lauf — Erstwahrnehmung oder qualifizierte Kenntnis?
5. Gibt es Lücken, die durch Zeugenaussagen geschlossen werden müssen?
- Was will der Mandant wirklich erreichen? (verteidigungsfähige Zeitachse; Begründung Fristbeginn)

## Rechtsgrundlagen

- **Art. 33 Abs. 1 DSGVO** Kenntnisbegriff und 72-Stunden-Frist.
- **Erwägungsgrund 87 DSGVO** unverzügliche Feststellung.
- **Art. 33 Abs. 4 DSGVO** schrittweise Übermittlung.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Auslegung Kenntnisbegriff und zum Beginn der 72-Stunden-Frist vor Ausgabe verifizieren.

## Zentrale Normen

Art. 33 Abs. 1; Art. 33 Abs. 4; Art. 5 Abs. 2 DSGVO; Erwägungsgrund 87.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Zeitleisten-Spalten

Datum/Uhrzeit (Zeitzone); Ereignis; Quelle; Akteur; Rechtsfolge; Anmerkungen; Beweismittel.

Wichtig: Kenntnisbegriff sauber dokumentieren — ein bloßer Verdacht oder Hinweis löst noch nicht den Fristlauf aus; maßgeblich ist die qualifizierte Kenntnis im Sinne Erwägungsgrund 87.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.
