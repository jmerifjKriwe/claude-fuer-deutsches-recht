---
name: kompendium-07-dsv-forensische-erst-bis-funktionsuebertragun
description: "datenschutzrecht: Konsolidiertes Skill-Kompendium 07; bündelt 10 frühere Spezialskills (dsv-forensische-erstsicherung, dsv-massenbenachrichtigung, dsv-meldekette-auftragsverarbeiter, dsv-meldung-grenzueberschreitend, dsv-meldung-kritis-sektoraufsicht und 5 weitere) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 07 - datenschutzrecht

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `dsv-forensische-erstsicherung` | Steuert die forensische Erstsicherung nach einem Datenschutzvorfall im Zusammenspiel zwischen Mandant, interner IT, externem Forensiker und Anwaltskanzlei. Behandelt: Auswahl und Beauftragung des Forensikers; Mandatsstruktur mit Anwaltsprivileg; Scope; Triage versus tiefe Analyse; Berichtsformate; Kommunikation mit Aufsichtsbehörde; Schnittstellen zur Cyberversicherung. Output: Beauftragungsmuster, Briefing für Forensiker und Steuerungsraster. Abgrenzung: keine eigene forensische Tätigkeit; keine technische Anleitung. |
| `dsv-massenbenachrichtigung` | Steuert die Massenbenachrichtigung tausender oder Millionen Betroffener nach Art. 34 DSGVO. Behandelt: Versandlogistik E-Mail-Welle; Brief-Welle; Push und SMS; Adressqualität; Bounces; Sprachvarianten; Hotline-Dimensionierung; Pressewelle; Hilfsdienste wie Schufa-Auskunft. Output: Versandplan, Skalierungsraster, Q&A-Matrix. Abgrenzung: keine individuelle Benachrichtigung; keine Behördenmeldung. |
| `dsv-meldekette-auftragsverarbeiter` | Steuert die Meldekette in einer Auftragsverarbeiter-Konstellation nach Art. 33 Abs. 2 DSGVO. Behandelt: Meldung des Auftragsverarbeiters an den Verantwortlichen; Form, Frist, Inhalt; Eskalation bei Schweigen oder Verzögerung; AV-Vertragsklauseln nach Art. 28 Abs. 3 lit. f und h DSGVO; Unterauftragsverarbeiter; Vertragsstrafen; Beweissicherungspflichten beim Auftragsverarbeiter. Output: Mustermeldung Auftragsverarbeiter an Verantwortlichen plus Eskalationsschreiben. Abgrenzung: keine Behördenmeldung durch den Auftragsverarbeiter. |
| `dsv-meldung-grenzueberschreitend` | Steuert die Meldung eines Datenschutzvorfalls mit Bezug zu mehreren Mitgliedstaaten oder Drittstaaten. Behandelt: Lead-Authority-Verfahren Art. 56 DSGVO; parallele Meldung an betroffene Behörden; Sprache der Meldung; Drittstaaten-Aufsichten und ihre Meldepflichten (z.B. UK ICO, Schweiz EDÖB); Schnittstelle zu Art. 49 DSGVO-Übermittlungen; Hinweispflichten an US-Aufsichten bei BIPA, CCPA, GLBA. Output: Memo zur Meldelandkarte. Abgrenzung: keine vertiefte US-Beratung. |
| `dsv-meldung-kritis-sektoraufsicht` | Steuert die parallele Meldung an Sektoraufsichten neben der Datenschutzaufsicht. Behandelt: § 8b BSIG für KRITIS; NIS-2-Umsetzung mit erweiterten Meldepflichten; BaFin BAIT/MaRisk für Finanzinstitute; BNetzA für TK- und Postdienste; Meldungen nach § 168 TKG; Konsistenz der Meldetexte; Datenschutzschnittstelle. Output: Memo zur Mehrfachmeldelandschaft. Abgrenzung: keine vertiefte BaFin-Beratung. |
| `dsv-paragraf-203-stgb-berufsgeheimnis` | Bewertet einen Datenschutzvorfall bei Berufsgeheimnisträgern nach § 203 StGB. Behandelt: Ärzte; Rechtsanwälte; Steuerberater; Wirtschaftsprüfer; Psychotherapeuten; Sozialarbeiter; berufsmäßige Gehilfen; mitwirkende Personen nach § 203 Abs. 3 StGB; Reichweite der Schweigepflicht; Verhältnis zur DSGVO; Anzeige- und Benachrichtigungspflichten; Risiken bei Cloud-Auslagerung; berufsrechtliche Folgen. Output: Memo zu Strafbarkeitsrisiko und Pflichten. Abgrenzung: keine berufsrechtliche Verteidigung; keine Strafanzeige. |
| `dsv-pressemitteilung-krisenkommunikation` | Entwirft eine Pressemitteilung und begleitende Krisenkommunikation bei einem Datenschutzvorfall mit öffentlicher Wahrnehmung. Behandelt: rechtliche Pflichten aus Art. 34 Abs. 3 lit. c DSGVO (öffentliche Bekanntmachung); Inhalt; Tonfall; Vermeidung von Selbstbelastung; Abstimmung mit Aufsichtsbehörde; Q&A für Pressestelle; Social-Media-Steuerung. Output: Pressemitteilung mit Q&A. Abgrenzung: keine individuelle Benachrichtigung; keine Pressepressespiegel. |
| `dsv-sammelklagen-praevention` | Entwickelt eine Strategie zur Prävention und Steuerung von Sammelklagen und Massenverfahren nach einer Massendatenpanne. Behandelt: Verbandsklage-Richtlinie; UKlaG; KapMuG-Analogien; Inkasso-Plattformen; anwaltliche Akquise-Wellen; Beweisaufnahme-Risiken bei öffentlicher Bekanntmachung; Vergleichsangebote; Goodwill-Leistungen ohne Anerkenntnis; Schufa-Auskünfte. Output: Strategie-Memo mit Maßnahmen-Roadmap. Abgrenzung: keine konkrete Schadensersatzverteidigung. |
| `dsv-vvt-update-nach-vorfall` | Steuert die Aktualisierung des Verzeichnisses von Verarbeitungstätigkeiten nach Art. 30 DSGVO im Nachgang eines Datenschutzvorfalls. Behandelt: Identifikation der betroffenen Verarbeitungen; Anpassung der technischen und organisatorischen Maßnahmen; neue Risikoeinschätzung; Auftragsverarbeiter-Update; Aufbewahrungsfristen; Verknüpfung mit Vorfallregister Art. 33 Abs. 5. Output: Update-Checkliste mit Pflichtfeldern. Abgrenzung: kein neues VVT; keine DSFA. |
| `funktionsuebertragung-vs-auftragsverarbeitung` | Abgrenzung Funktionsuebertragung gegen Auftragsverarbeitung Art. 28 DSGVO bei Berufsgeheimnistraegern Inkasso Steuerberatung Wirtschaftspruefung und externe Rechtsdienstleistung. Wann handelt der Dritte als eigener Verantwortlicher und wann als Auftragsverarbeiter. § 203 StGB § 43a Abs. 2 BRAO. Output: Pruefraster Rollenzuordnung. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `dsv-forensische-erstsicherung`

**Frühere Beschreibung:** Steuert die forensische Erstsicherung nach einem Datenschutzvorfall im Zusammenspiel zwischen Mandant, interner IT, externem Forensiker und Anwaltskanzlei. Behandelt: Auswahl und Beauftragung des Forensikers; Mandatsstruktur mit Anwaltsprivileg; Scope; Triage versus tiefe Analyse; Berichtsformate; Kommunikation mit Aufsichtsbehörde; Schnittstellen zur Cyberversicherung. Output: Beauftragungsmuster, Briefing für Forensiker und Steuerungsraster. Abgrenzung: keine eigene forensische Tätigkeit; keine technische Anleitung.

# Forensische Erstsicherung — Beauftragung und Steuerung

## Triage — kläre vor der Bearbeitung

1. Soll der Forensiker durch den Mandanten oder durch die Kanzlei beauftragt werden (Anwaltsprivileg)?
2. Welche Cyberversicherung gibt einen Forensiker vor?
3. Welche Daten sind besonders sensibel und schränken den Scope ein?
4. Welche Sprache muss der Bericht haben — Deutsch oder Englisch für die Behörde?
5. Wer übernimmt die Schnittstelle zur Aufsichtsbehörde?
- Was will der Mandant wirklich erreichen? (Eindämmung; rechtssichere Bewertung; Verteidigungsfähigkeit)

## Rechtsgrundlagen

- **Art. 32 DSGVO** Sicherheit der Verarbeitung.
- **Art. 33 Abs. 3 lit. c DSGVO** Maßnahmenangabe in der Meldung.
- **§ 43a Abs. 2 BRAO** Verschwiegenheit; **§ 53 StPO** Zeugnisverweigerungsrecht.
- **§ 203 StGB** Berufsgeheimnis.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Reichweite des Anwaltsprivilegs bei Cyber-Forensik vor Ausgabe verifizieren.

## Zentrale Normen

Art. 32; Art. 33 Abs. 3 lit. c DSGVO; § 43a Abs. 2 BRAO; § 53 StPO; § 203 StGB.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Beauftragungsraster

Auftraggeber: Kanzlei in Untermandat / Mandant direkt.

Scope: Triage-Bericht 48 h; vertiefte Analyse Wochen 1-4; Schlussbericht.

Lieferobjekte: Sofort-Memo; Zwischenbericht; Schlussbericht; Behörden-tauglicher Kurzbericht.

Vertraulichkeit: NDA; Anwaltsprivileg-Klausel; Aufbewahrung nur in Mandantenakte.

Schnittstellen: Versicherung; Aufsichtsbehörde; Strafverfolgung.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

## 2. `dsv-massenbenachrichtigung`

**Frühere Beschreibung:** Steuert die Massenbenachrichtigung tausender oder Millionen Betroffener nach Art. 34 DSGVO. Behandelt: Versandlogistik E-Mail-Welle; Brief-Welle; Push und SMS; Adressqualität; Bounces; Sprachvarianten; Hotline-Dimensionierung; Pressewelle; Hilfsdienste wie Schufa-Auskunft. Output: Versandplan, Skalierungsraster, Q&A-Matrix. Abgrenzung: keine individuelle Benachrichtigung; keine Behördenmeldung.

# Massenbenachrichtigung bei großem Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Welche Adressdaten liegen in welcher Qualität vor?
2. Welche Sprachen müssen abgedeckt werden?
3. Welche Hotline-Kapazität ist erforderlich?
4. Welche Versanddienstleister sind vertraglich gebunden?
5. Welche regulatorischen Anforderungen an Massenversand bestehen (E-Privacy)?
- Was will der Mandant wirklich erreichen? (zuverlässige Erreichung der Betroffenen; saubere Logistik)

## Rechtsgrundlagen

- **Art. 34 Abs. 1 DSGVO** Benachrichtigung.
- **Art. 34 Abs. 2 DSGVO** Pflichtinhalte.
- **Art. 12 Abs. 1 DSGVO** klare einfache Sprache.
- **§ 7 UWG** Werbung im Geschäftsverkehr (nicht anwendbar auf Pflichtinformation).
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu Sammelklagen nach Massendatenpannen vor Ausgabe verifizieren.

## Zentrale Normen

Art. 12 Abs. 1; Art. 34 Abs. 1; Art. 34 Abs. 2; Art. 5 Abs. 2 DSGVO.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Versandplan

Welle 1: E-Mail an alle Adressaten mit valider E-Mail-Adresse — Versand über DSGVO-konformen Dienstleister; Bounce-Handling automatisiert.

Welle 2: Brief an alle Adressaten ohne E-Mail oder mit Bounce — innerhalb von sieben Tagen.

Welle 3: öffentliche Bekanntmachung über Webseite und Pressemeldung — als Auffangnetz.

Hotline: 24/7 in der ersten Woche; 8-20 Uhr ab Woche zwei; mehrsprachig.

Q&A-Matrix: 20-30 Fragen mit abgestimmten Antworten.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-pressemitteilung-krisenkommunikation` deckt Pressekommunikation ab.

## 3. `dsv-meldekette-auftragsverarbeiter`

**Frühere Beschreibung:** Steuert die Meldekette in einer Auftragsverarbeiter-Konstellation nach Art. 33 Abs. 2 DSGVO. Behandelt: Meldung des Auftragsverarbeiters an den Verantwortlichen; Form, Frist, Inhalt; Eskalation bei Schweigen oder Verzögerung; AV-Vertragsklauseln nach Art. 28 Abs. 3 lit. f und h DSGVO; Unterauftragsverarbeiter; Vertragsstrafen; Beweissicherungspflichten beim Auftragsverarbeiter. Output: Mustermeldung Auftragsverarbeiter an Verantwortlichen plus Eskalationsschreiben. Abgrenzung: keine Behördenmeldung durch den Auftragsverarbeiter.

# Meldekette Auftragsverarbeiter — Art. 33 Abs. 2 DSGVO

## Triage — kläre vor der Bearbeitung

1. Wer ist Verantwortlicher und wer Auftragsverarbeiter (klare Abgrenzung)?
2. Liegt ein AV-Vertrag nach Art. 28 Abs. 3 DSGVO vor?
3. Welche Meldefristen sind dort vereinbart (oft kürzer als 72 Stunden)?
4. Sind Unterauftragsverarbeiter beteiligt?
5. Welche Vertragsstrafen oder Schadensersatzklauseln greifen?
- Was will der Mandant wirklich erreichen? (klare Verantwortungsabgrenzung; Schadensersatzansprüche sichern)

## Rechtsgrundlagen

- **Art. 28 Abs. 3 lit. f; h DSGVO** AV-Pflichten.
- **Art. 33 Abs. 2 DSGVO** Meldepflicht des Auftragsverarbeiters.
- **Art. 82 DSGVO** Schadensersatz.
- **§ 280 BGB** Pflichtverletzung.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu Fristberechnung Art. 33 Abs. 1 DSGVO bei Kenntnis nur des Auftragsverarbeiters vor Ausgabe verifizieren.

## Zentrale Normen

Art. 28 Abs. 3; Art. 33 Abs. 2; Art. 82 DSGVO; § 280 BGB.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Muster Meldung Auftragsverarbeiter

Betreff: Meldung einer Verletzung des Schutzes personenbezogener Daten nach Art. 33 Abs. 2 DSGVO.

Sehr geehrte Damen und Herren, gemäß Art. 33 Abs. 2 DSGVO und unserem AV-Vertrag vom [Datum] melden wir Ihnen folgenden Vorfall:

- Datum und Uhrzeit der Kenntnisnahme: [...]
- Beschreibung der Verletzung: [...]
- Betroffene Verarbeitung: [...]
- Geschätzte Anzahl betroffener Datensätze: [...]
- Bereits eingeleitete Sofortmaßnahmen: [...]
- Vorgeschlagene weitere Maßnahmen: [...]
- Ansprechpartner: [...]

Eine Nachmeldung mit weiteren Details folgt unverzüglich nach Abschluss der forensischen Analyse.

Eskalationsschreiben bei Schweigen: Fristsetzung 24 h; danach Vertragsstrafe und Kündigungsandrohung.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-meldung-art-33-pflichtangaben` deckt die Behoerdenmeldung des Verantwortlichen ab.

## 4. `dsv-meldung-grenzueberschreitend`

**Frühere Beschreibung:** Steuert die Meldung eines Datenschutzvorfalls mit Bezug zu mehreren Mitgliedstaaten oder Drittstaaten. Behandelt: Lead-Authority-Verfahren Art. 56 DSGVO; parallele Meldung an betroffene Behörden; Sprache der Meldung; Drittstaaten-Aufsichten und ihre Meldepflichten (z.B. UK ICO, Schweiz EDÖB); Schnittstelle zu Art. 49 DSGVO-Übermittlungen; Hinweispflichten an US-Aufsichten bei BIPA, CCPA, GLBA. Output: Memo zur Meldelandkarte. Abgrenzung: keine vertiefte US-Beratung.

# Meldung grenzüberschreitender Datenschutzvorfälle — EU und Drittstaaten

## Triage — kläre vor der Bearbeitung

1. In welchen EU-Staaten sind Betroffene?
2. Welche Drittstaaten sind tangiert?
3. Welche Lead Authority ist nach Art. 56 DSGVO zuständig?
4. Welche Drittstaatsaufsichten erfordern parallele Meldung?
5. Welche Sprache verlangt jede Behörde?
- Was will der Mandant wirklich erreichen? (rechtssichere Meldelandkarte; keine vergessene Behörde)

## Rechtsgrundlagen

- **Art. 56 DSGVO** Lead Authority.
- **Art. 60 DSGVO** Kooperation.
- **Art. 33 DSGVO** Meldepflicht.
- **Art. 49 DSGVO** Übermittlungen.
- **UK GDPR; Swiss DSG; CCPA; BIPA** je nach Drittstaatsbezug.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu One-Stop-Shop-Streitigkeiten und Drittstaaten-Anerkennung vor Ausgabe verifizieren.

## Zentrale Normen

Art. 33; Art. 49; Art. 56; Art. 60 DSGVO; UK GDPR; Swiss DSG.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Meldelandkarte

Spalte 1: Land; Spalte 2: Behörde; Spalte 3: Pflicht oder freiwillig; Spalte 4: Frist; Spalte 5: Sprache; Spalte 6: Verantwortlicher intern; Spalte 7: Status.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-lead-authority-konzern` deckt die Bestimmung der federfuehrenden Behoerde ab.

## 5. `dsv-meldung-kritis-sektoraufsicht`

**Frühere Beschreibung:** Steuert die parallele Meldung an Sektoraufsichten neben der Datenschutzaufsicht. Behandelt: § 8b BSIG für KRITIS; NIS-2-Umsetzung mit erweiterten Meldepflichten; BaFin BAIT/MaRisk für Finanzinstitute; BNetzA für TK- und Postdienste; Meldungen nach § 168 TKG; Konsistenz der Meldetexte; Datenschutzschnittstelle. Output: Memo zur Mehrfachmeldelandschaft. Abgrenzung: keine vertiefte BaFin-Beratung.

# Parallele Meldung KRITIS und Sektoraufsicht — BSIG, BaFin, BNetzA, NIS-2

## Triage — kläre vor der Bearbeitung

1. Ist der Mandant KRITIS-Betreiber, NIS-2-pflichtige Einrichtung oder reguliertes Institut?
2. Welche Sektoraufsicht ist zusätzlich zur Datenschutzbehörde zu informieren?
3. Welche Fristen gelten (BSIG, NIS-2, TKG)?
4. Welcher Texte muss konsistent gehalten werden?
5. Welche Aufsicht hat informellen Vorrang?
- Was will der Mandant wirklich erreichen? (rechtssichere Parallel-Meldung; konsistente Aussagen)

## Rechtsgrundlagen

- **§ 8b BSIG** KRITIS-Meldepflicht.
- **NIS-2-Richtlinie** und deutsches Umsetzungsgesetz (Stand prüfen).
- **§ 168 TKG** Sicherheitsvorfälle TK.
- **BaFin BAIT/MaRisk** für Finanzinstitute.
- **Art. 33 DSGVO** Datenschutzmeldung.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; aktuelle Stände zur NIS-2-Umsetzung in Deutschland vor Ausgabe verifizieren.

## Zentrale Normen

Art. 33 DSGVO; § 8b BSIG; § 168 TKG; NIS-2-Richtlinie; BAIT.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Mehrfach-Meldelandschaft

Datenschutz-Spur: zuständige Datenschutzbehörde (Lead-Authority + Land).

BSIG/NIS-2-Spur: BSI Meldestelle.

TK-Spur: BNetzA.

Finanzaufsicht: BaFin.

Texte synchronisiert; Aktenzeichen wechselseitig zitieren.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-meldung-art-33-pflichtangaben` deckt die Datenschutz-Meldung ab.

## 6. `dsv-paragraf-203-stgb-berufsgeheimnis`

**Frühere Beschreibung:** Bewertet einen Datenschutzvorfall bei Berufsgeheimnisträgern nach § 203 StGB. Behandelt: Ärzte; Rechtsanwälte; Steuerberater; Wirtschaftsprüfer; Psychotherapeuten; Sozialarbeiter; berufsmäßige Gehilfen; mitwirkende Personen nach § 203 Abs. 3 StGB; Reichweite der Schweigepflicht; Verhältnis zur DSGVO; Anzeige- und Benachrichtigungspflichten; Risiken bei Cloud-Auslagerung; berufsrechtliche Folgen. Output: Memo zu Strafbarkeitsrisiko und Pflichten. Abgrenzung: keine berufsrechtliche Verteidigung; keine Strafanzeige.

# § 203 StGB Berufsgeheimnis im Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Welcher Berufsgeheimnisträger ist betroffen?
2. Wurde das Geheimnis offenbart oder unbefugt zugänglich gemacht?
3. Lag Vorsatz oder Fahrlässigkeit vor?
4. Sind mitwirkende Personen nach § 203 Abs. 3 StGB beteiligt — Cloud-Anbieter, Praxisverwaltungssystem?
5. Welche Schweigepflichtsentbindung der Betroffenen liegt vor?
- Was will der Mandant wirklich erreichen? (Strafbarkeitsrisiko vermeiden; Berufszulassung sichern)

## Rechtsgrundlagen

- **§ 203 Abs. 1 StGB** Verletzung von Privatgeheimnissen.
- **§ 203 Abs. 3 Satz 2 StGB** mitwirkende Personen.
- **§ 203 Abs. 4 StGB** Offenbarungstatbestände.
- **Art. 33 DSGVO** Meldepflicht (zusätzlich zur strafrechtlichen Bewertung).
- **§ 43a Abs. 2 BRAO** anwaltliche Verschwiegenheit.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Reichweite des § 203 Abs. 3 Satz 2 StGB bei IT-Dienstleistern vor Ausgabe verifizieren.

## Zentrale Normen

§ 203 Abs. 1; § 203 Abs. 3; § 203 Abs. 4 StGB; Art. 33 DSGVO; § 43a Abs. 2 BRAO.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Strafbarkeitsraster

Tathandlung: Offenbaren / unbefugt Zugänglichmachen.

Täterkreis: § 203 Abs. 1 StGB Katalog; § 203 Abs. 3 mitwirkende Personen.

Schuld: Vorsatz / Fahrlässigkeit (§ 203 Abs. 1 setzt Vorsatz voraus; fahrlässige Offenbarung nicht strafbar, aber berufsrechtlich relevant).

Berufsrecht: zusätzliche Meldung an Kammer; Disziplinarverfahren möglich.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-art-9-besondere-kategorien` deckt sensible Daten ab.
- `dsv-sozialdaten-sgb` deckt Sozialdaten ab.

## 7. `dsv-pressemitteilung-krisenkommunikation`

**Frühere Beschreibung:** Entwirft eine Pressemitteilung und begleitende Krisenkommunikation bei einem Datenschutzvorfall mit öffentlicher Wahrnehmung. Behandelt: rechtliche Pflichten aus Art. 34 Abs. 3 lit. c DSGVO (öffentliche Bekanntmachung); Inhalt; Tonfall; Vermeidung von Selbstbelastung; Abstimmung mit Aufsichtsbehörde; Q&A für Pressestelle; Social-Media-Steuerung. Output: Pressemitteilung mit Q&A. Abgrenzung: keine individuelle Benachrichtigung; keine Pressepressespiegel.

# Pressemitteilung und Krisenkommunikation bei Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Ist die öffentliche Bekanntmachung Pflicht (Art. 34 Abs. 3 lit. c) oder freiwillig?
2. Welche Medien sind bereits aktiv und welche Fragen kommen?
3. Welcher Tonfall passt zum Mandanten (Konzern, Mittelstand, Praxis)?
4. Welche Aussagen müssen mit Behörde und Versicherer abgestimmt werden?
5. Welche Social-Media-Kanäle erfordern eigene Botschaften?
- Was will der Mandant wirklich erreichen? (Vertrauenserhalt; keine Selbstbelastung; Sammelklagen-Schutz)

## Rechtsgrundlagen

- **Art. 34 Abs. 1 DSGVO** Benachrichtigung Betroffener.
- **Art. 34 Abs. 3 lit. c DSGVO** öffentliche Bekanntmachung als Ersatz.
- **Art. 5 Abs. 1 lit. a DSGVO** Transparenz.
- **§ 824 BGB** Kreditgefährdung.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu Sammelklagen und immateriellen Schadensersatzansprüchen nach öffentlicher Bekanntmachung vor Ausgabe verifizieren.

## Zentrale Normen

Art. 5 Abs. 1 lit. a; Art. 34 Abs. 1; Art. 34 Abs. 3 lit. c DSGVO; § 824 BGB.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Pressemitteilung-Bausteine

Headline: sachlich; keine Schuldzuweisung; keine Verharmlosung.

Lead: Was, wann, wer, wie viele.

Body: Welche Maßnahmen wurden bereits getroffen; welche Empfehlungen für Betroffene; welche Anlaufstelle (Hotline, E-Mail); welche Behördenkommunikation läuft.

Tonfall: matter-of-factly; verantwortungsbewusst; ohne unverbindliche Beruhigung.

Q&A: zehn bis fünfzehn Standardfragen mit abgestimmten Antworten für Pressestelle und Hotline.

Sperrfristen: erst nach Information der Betroffenen oder gleichzeitig veröffentlichen.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-kommunikationssperre` deckt die internen Sprachregelungen ab.
- `dsv-benachrichtigung-art-34-betroffene` deckt die individuelle Benachrichtigung ab.

## 8. `dsv-sammelklagen-praevention`

**Frühere Beschreibung:** Entwickelt eine Strategie zur Prävention und Steuerung von Sammelklagen und Massenverfahren nach einer Massendatenpanne. Behandelt: Verbandsklage-Richtlinie; UKlaG; KapMuG-Analogien; Inkasso-Plattformen; anwaltliche Akquise-Wellen; Beweisaufnahme-Risiken bei öffentlicher Bekanntmachung; Vergleichsangebote; Goodwill-Leistungen ohne Anerkenntnis; Schufa-Auskünfte. Output: Strategie-Memo mit Maßnahmen-Roadmap. Abgrenzung: keine konkrete Schadensersatzverteidigung.

# Sammelklagen-Prävention nach Massendatenpanne

## Triage — kläre vor der Bearbeitung

1. Welche Größenordnung Betroffener und welche Datenkategorien?
2. Welche Inkasso-Plattformen oder Verbraucherzentralen sind erfahrungsgemäß aktiv?
3. Welche Vergleichsangebote sind versicherungstechnisch gedeckt?
4. Welche Aussagen im Anschreiben können Sammelklagen befeuern?
5. Welche Aussagen mindern das Risiko ohne Selbstbelastung?
- Was will der Mandant wirklich erreichen? (Schadensbegrenzung; Verfahrensökonomie; Markenschutz)

## Rechtsgrundlagen

- **Art. 82 DSGVO** Schadensersatzanspruch.
- **Verbandsklagen-Richtlinie EU 2020/1828** und VDuG.
- **§ 1 UKlaG** Unterlassungsklagengesetz.
- **§ 309 BGB** AGB-Klauselverbote.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu BGH/EuGH-Urteilen zum immateriellen Schadensersatz und zu Massenverfahren vor Ausgabe verifizieren.

## Zentrale Normen

Art. 82 DSGVO; § 1 UKlaG; VDuG; § 309 BGB; Verbandsklagen-Richtlinie 2020/1828.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Roadmap

Phase 1 vor Versand: Wortwahl prüfen; Goodwill-Pakete schnüren; Pressepolitik abstimmen.

Phase 2 erste Welle Anwaltsschreiben: einheitliche Antwortlinie; Standard-Schriftsätze; Substantiierungsanforderungen einhalten.

Phase 3 Klagewelle: Streitwerte zusammenführen; Verfahrenskonzentration prüfen; Vergleichsstrategie.

Phase 4 Verbands- oder Sammelklage: Musterverfahren; Streithilfe; Pressepolitik.

Goodwill: pauschale Kulanzpakete (z.B. Schufa-Auskunft, Identitätsschutz) ohne Anerkenntnis der Pflicht.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-schadensersatz-art-82` deckt die zivilrechtliche Verteidigung ab.
- `dsv-rechtsprechung-immaterieller-schaden-bgh-olg` deckt die Rechtsprechungsanalyse ab.

## 9. `dsv-vvt-update-nach-vorfall`

**Frühere Beschreibung:** Steuert die Aktualisierung des Verzeichnisses von Verarbeitungstätigkeiten nach Art. 30 DSGVO im Nachgang eines Datenschutzvorfalls. Behandelt: Identifikation der betroffenen Verarbeitungen; Anpassung der technischen und organisatorischen Maßnahmen; neue Risikoeinschätzung; Auftragsverarbeiter-Update; Aufbewahrungsfristen; Verknüpfung mit Vorfallregister Art. 33 Abs. 5. Output: Update-Checkliste mit Pflichtfeldern. Abgrenzung: kein neues VVT; keine DSFA.

# Aktualisierung des Verfahrensverzeichnisses nach Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Welche VVT-Einträge sind durch den Vorfall berührt?
2. Welche TOM müssen aktualisiert werden?
3. Sind neue Auftragsverarbeiter hinzugekommen (Forensiker, Hotline)?
4. Welche Aufbewahrungsfristen ändern sich (Logs, Vorfallakten)?
5. Wer pflegt das VVT und genehmigt die Änderung?
- Was will der Mandant wirklich erreichen? (Rechenschaftspflicht erfüllen; Bußgeldverteidigung; saubere Audit-Spur)

## Rechtsgrundlagen

- **Art. 30 DSGVO** VVT.
- **Art. 32 DSGVO** TOM.
- **Art. 33 Abs. 5 DSGVO** Vorfallregister.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.
- **Art. 24 DSGVO** Verantwortung.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Vorlagepflicht des VVT auf Behördenanforderung vor Ausgabe verifizieren.

## Zentrale Normen

Art. 5 Abs. 2; Art. 24; Art. 30; Art. 32; Art. 33 Abs. 5 DSGVO.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Update-Checkliste

Schritt 1: Vorfall einer Verarbeitung VVT-ID zuordnen.

Schritt 2: TOM-Liste aktualisieren — was war wirksam, was nicht, was wurde nachgerüstet.

Schritt 3: Risikobewertung in VVT überarbeiten.

Schritt 4: Auftragsverarbeiter-Eintrag pflegen — neue Subunternehmer dokumentieren.

Schritt 5: Aufbewahrungsfristen anpassen; Vorfallakte mit Aufbewahrungsende eintragen.

Schritt 6: Versionsstand mit Datum und Bearbeiter speichern; alte Version revisionssicher archivieren.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-dsfa-update-nach-vorfall` deckt die Datenschutz-Folgenabschätzung ab.
- `dsv-interne-dokumentation-art-33-abs-5` deckt das Vorfallregister ab.

## 10. `funktionsuebertragung-vs-auftragsverarbeitung`

**Frühere Beschreibung:** Abgrenzung Funktionsuebertragung gegen Auftragsverarbeitung Art. 28 DSGVO bei Berufsgeheimnistraegern Inkasso Steuerberatung Wirtschaftspruefung und externe Rechtsdienstleistung. Wann handelt der Dritte als eigener Verantwortlicher und wann als Auftragsverarbeiter. § 203 StGB § 43a Abs. 2 BRAO. Output: Pruefraster Rollenzuordnung.

# Funktionsuebertragung versus Auftragsverarbeitung

## Zweck / Purpose

Abgrenzung zwischen Funktionsuebertragung (eigene Verantwortlichkeit des Dritten) und Auftragsverarbeitung nach Art. 28 DSGVO bei Berufsgeheimnistraegern und externen Dienstleistern, die typischerweise eine eigene Berufstraegerstellung haben (Steuerberater, Wirtschaftspruefer, Rechtsanwaelte, Inkassodienstleister, Aerzte). Purpose (EN): Demarcation between "Funktionsuebertragung" (functional transfer with own controllership) and Article 28 GDPR processing on behalf, in particular for professionals bound by professional secrecy.

## Wann brauchen Sie diesen Skill

- Mandant beauftragt einen Steuerberater, Wirtschaftspruefer, Rechtsanwalt, Arzt oder Inkassodienstleister.
- Eine Kanzlei oder Arztpraxis stellt sich die Frage, ob mit externen Dienstleistern (z. B. Schreibbuero, externe IT, Steuerbuero) ein AVV oder ein anderer Vertragstyp zu schliessen ist.
- Es ist § 203 StGB relevant.

## Rechtlicher Rahmen

- Art. 28 DSGVO – Auftragsverarbeitung.
- Art. 4 Nr. 7 DSGVO – Verantwortlicher.
- EDSA-Leitlinien 07/2020 zur Abgrenzung Verantwortlicher / Auftragsverarbeiter (Final 07.07.2021).
- § 203 StGB – Verletzung von Privatgeheimnissen einschliesslich Sonderregel Abs. 3 zu mitwirkenden Personen seit 09.11.2017.
- § 43a Abs. 2 BRAO – Verschwiegenheitspflicht des Rechtsanwalts.
- § 57 Abs. 1 StBerG – Pflichten des Steuerberaters.
- § 43 Abs. 1 WPO – Pflichten des Wirtschaftspruefers.
- § 11 BORA – Mitwirkende Personen.

## Ablauf / Checkliste

1. **Berufstraegerstellung erkennen.**
   - Hat der Dritte eine eigene Berufstraegerstellung mit gesetzlicher Verschwiegenheitspflicht?
   - Erbringt er eine Berufsleistung, die der Mandant nicht selbst erbringen koennte?
   - Beispiele: Steuerberatung, Rechtsdienstleistung, Wirtschaftspruefung, aerztliche Behandlung, Inkasso (RDG).

2. **Eigene Zweck-Mittel-Entscheidung pruefen.**
   - Entscheidet der Dritte ueber Methode und Inhalt seiner Berufsleistung autonom?
   - Steuerberater entscheidet ueber Buchungsmethode, Rechtsanwalt ueber Argumentationsstrategie, Arzt ueber Diagnoseverfahren.
   - Dann: Eigene Verantwortlichkeit, Funktionsuebertragung.

3. **Konstellationen.**

   | Konstellation | Einordnung | Vertragstyp |
   |---|---|---|
   | Steuerberater erstellt Buchhaltung fuer Mandant | Funktionsuebertragung | Steuerberatungsvertrag, ggf. C2C-Datenuebermittlungsregelung |
   | Rechtsanwalt vertritt Mandant | Funktionsuebertragung | Mandatsvertrag |
   | Wirtschaftspruefer prueft Jahresabschluss | Funktionsuebertragung | Pruefungsvertrag |
   | Inkassodienstleister treibt Forderungen ein | Funktionsuebertragung (typisch) | Inkassovertrag |
   | Arzt behandelt Patient | Funktionsuebertragung | Behandlungsvertrag § 630a BGB |
   | Externe IT betreut Kanzlei-IT mit Datenzugang | regelmaessig Auftragsverarbeitung Art. 28 | AVV plus § 203 Abs. 3 StGB |
   | Externes Schreibbuero schreibt Diktate | Auftragsverarbeitung Art. 28 | AVV plus § 203 Abs. 3 StGB |
   | Cloud-Speicher fuer Mandantenakten | Auftragsverarbeitung Art. 28 | AVV plus § 203 Abs. 3 StGB |

4. **§ 203 Abs. 3 StGB beachten (nur bei Auftragsverarbeitung erforderlich).**
   - Mitwirkende Personen muessen zur Verschwiegenheit verpflichtet sein.
   - Berufstraeger muss "im erforderlichen Umfang" offenbaren duerfen.
   - Schriftliche Verpflichtung der mitwirkenden Personen ratsam.
   - § 11 BORA fuer Rechtsanwaelte; entsprechende Regeln fuer Steuerberater und Aerzte.

5. **Datenfluss-Vertrag bei Funktionsuebertragung.**
   - Kein AVV erforderlich (Dritter ist eigener Verantwortlicher).
   - Aber Datenuebermittlungsklausel im Mandatsvertrag empfohlen (Rechtsgrundlage Art. 6 Abs. 1 lit. b DSGVO und ggf. Art. 9 Abs. 2 lit. f DSGVO).
   - Informationspflichten Art. 13/14 DSGVO bei beiden Akteuren.

## Mustertext / Template

A) Klausel im Mandatsvertrag bei Funktionsuebertragung (Steuerberater oder Rechtsanwalt):

> "§ Y Datenschutz
>
> (1) Auftraggeber und [Berufstraeger] verarbeiten personenbezogene Daten jeweils als eigene Verantwortliche im Sinne von Art. 4 Nr. 7 DSGVO. Eine Auftragsverarbeitung im Sinne von Art. 28 DSGVO liegt nicht vor.
>
> (2) Der Auftraggeber uebermittelt [Berufstraeger] die zur Mandatsbearbeitung erforderlichen personenbezogenen Daten auf Grundlage von Art. 6 Abs. 1 lit. b DSGVO und – soweit besondere Kategorien personenbezogener Daten betroffen sind – Art. 9 Abs. 2 lit. f DSGVO. [Berufstraeger] verarbeitet die Daten ausschliesslich im Rahmen der gesetzlichen Berufspflichten unter Wahrung der Verschwiegenheitspflicht aus [§ 43a Abs. 2 BRAO / § 57 Abs. 1 StBerG / § 43 Abs. 1 WPO].
>
> (3) Die Informationspflichten gemaess Art. 13 und 14 DSGVO erfuellt jede Partei eigenstaendig gegenueber ihren jeweiligen Betroffenen.
>
> (4) Soweit [Berufstraeger] zur Erbringung der Berufsleistung externe Dienstleister einsetzt, die nicht selbst Berufstraeger im Sinne des § 203 Abs. 1 StGB sind, werden diese gemaess § 203 Abs. 3 StGB i.V.m. [§ 11 BORA / entsprechender Berufsregel] zur Verschwiegenheit verpflichtet."

B) Klausel zur Verpflichtung mitwirkender Personen bei Auftragsverarbeitung:

> "§ Z Verschwiegenheitspflicht des Auftragsverarbeiters (§ 203 Abs. 3 StGB)
>
> (1) Der Auftragsverarbeiter und alle bei ihm zur Verarbeitung der berufsgeheimnisgeschuetzten Daten befugten Personen sind nach Massgabe des § 203 Abs. 3 Satz 2 StGB zur Verschwiegenheit ueber die zur Kenntnis gelangten Tatsachen verpflichtet. Die Verpflichtung wirkt ueber das Ende des Vertragsverhaeltnisses hinaus fort.
>
> (2) Der Auftragsverarbeiter dokumentiert die Verschwiegenheitsverpflichtung seiner Mitarbeiter schriftlich und legt sie dem Verantwortlichen auf Verlangen vor.
>
> (3) Ein Verstoss gegen die Verschwiegenheitspflicht stellt eine wesentliche Pflichtverletzung dar, die den Verantwortlichen zur ausserordentlichen Kuendigung berechtigt; eine etwaige strafrechtliche Verantwortlichkeit nach § 203 StGB bleibt unberuehrt."

## Typische Drafting-Fehler

- Berufstraeger (Steuerberater, Anwalt, Arzt) als Auftragsverarbeiter eingestuft – Funktionsuebertragung uebersehen.
- Externe IT oder Schreibbuero ohne AVV beschaeftigt – § 203 StGB-Strafbarkeitsrisiko.
- Keine Verpflichtung mitwirkender Personen nach § 203 Abs. 3 StGB.
- Informationspflichten Art. 13/14 DSGVO nicht beruecksichtigt.
- Cloud-Speicher fuer Mandantenakten ohne AVV oder ohne § 203-Klausel.

## Querverweise

- `datenschutzrecht/skills/avv-art-28-dsgvo-grundtatbestand/SKILL.md`
- `datenschutzrecht/skills/avv-rolemix-getrennt-vs-gemeinsam-verantwortlich/SKILL.md`
- `datenschutzrecht/skills/dpa-en-controller-controller-tmpl/SKILL.md`

## Quellen Stand 06/2026

- Art. 4 Nr. 7, Art. 6 Abs. 1, Art. 9 Abs. 2, Art. 28 DSGVO.
- § 203 StGB (Verletzung von Privatgeheimnissen).
- § 43a Abs. 2 BRAO; § 11 BORA.
- § 57 Abs. 1 StBerG; § 43 Abs. 1 WPO.
- EDSA-Leitlinien 07/2020 (Final 07.07.2021), edpb.europa.eu.
- Zitierweise: `../../../references/zitierweise.md`.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
