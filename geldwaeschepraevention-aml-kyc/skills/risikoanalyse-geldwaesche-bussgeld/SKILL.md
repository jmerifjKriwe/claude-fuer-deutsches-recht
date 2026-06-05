---
name: risikoanalyse-geldwaesche-bussgeld
description: "Risikoanalyse Geldwaesche Bussgeld im Plugin Geldwaeschepraevention Aml Kyc: prüft konkret Risikoanalyse, Strukturierung von Bußgeldriskien Geschäftsleiterhaftung, Sanktionsscreening von Kunden Transaktionen und Beteiligten. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Risikoanalyse Geldwaesche Bussgeld

## Arbeitsbereich

Dieser Skill behandelt **Risikoanalyse Geldwaesche Bussgeld** als zusammenhängenden Arbeitsgang im Plugin Geldwaeschepraevention Aml Kyc. Im Mittelpunkt steht die Prüfung von Risikoanalyse, Strukturierung von Bußgeldriskien Geschäftsleiterhaftung, Sanktionsscreening von Kunden Transaktionen und Beteiligten. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-risikoanalyse-fristen-form-und-zustaendigkeit` | Risikoanalyse: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin geldwaeschepraevention aml kyc; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `geldwaesche-bussgeld-reputation` | Strukturierung von Bußgeldriskien Geschäftsleiterhaftung und Reputationsschaeden bei GwG-Verstoessen. Anwendungsfall Bußgeldbescheid nach GwG ist eingegangen oder negative Berichterstattung droht. Normen § 52 GwG Bußgelder bis 5 Mio EUR oder 10 Prozent Jahresumsatz § 130 OWiG Aufsichtspflichtverletzung. Prüfraster Bußgeldrisko Geschäftsleitungsverantwortung Pressekommunikation Kundenkommunikation Remediation Schadensbegrenzung. Output Massnahmenplan mit Widerspruchsstrategie PR-Linie Remediation-Nachweis und Haftungsabsicherung. Abgrenzung zu geldwäsche-behoerdenverfahren und geldwäsche-audit-internal-revision. |
| `geldwaesche-sanktionsscreening` | Sanktionsscreening von Kunden Transaktionen und Beteiligten gegen EU-US- und UN-Sanktionslisten. Anwendungsfall neues Geschäft soll abgeschlossen oder Transaktion freigegeben werden. Normen EU-Verordnungen 2580/2001 881/2002 Russland-VO 833/2014 269/2014 OFAC-SDN-Liste. Prüfraster Namensscreening Alias-Screening Eigentuems-Kontrolle Embargo-Check Trefferlog False-Positive-Bewertung. Output Screening-Protokoll mit Trefferliste False-Positive-Begründung Freigabe oder Meldepflicht. Abgrenzung zu geldwäsche-pep-hochrisikoland und geldwäsche-transaktionsmonitoring. |

## Arbeitsweg

- Rolle und Ziel im Geldwäscheprävention (AML/KYC) klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: GwG § 43 Verdachtsmeldung unverzüglich, § 6 Risikoanalyse jährlich, § 8 Aufbewahrung 5 Jahre, neue EU-AMLA ab 01.07.2025 operativ.
- Tragende Normen verifizieren: GwG §§ 1-59, EU-Geldwäsche-RL (5. und 6. AML), EU AML-Paket 2024 (VO 2024/1624, RL 2024/1640, AMLA-VO), KWG, ZAG, BörsG, BaFin-AuA, FATF-Empfehlungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Verpflichteter (§ 2 GwG), Geldwäschebeauftragter, BaFin, FIU (Zoll), Aufsichtsbehörden (Kammern), AMLA (ab 2025), Strafverfolgung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Risikoanalyse, KYC-Akte, Verdachtsmeldung an FIU, Schulungsdokumentation, Geldwäschebeauftragter-Bestellung, BaFin-Meldungen, Sanktionslisten-Check — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `spezial-risikoanalyse-fristen-form-und-zustaendigkeit`

**Fokus:** Risikoanalyse: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin geldwaeschepraevention aml kyc; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Risikoanalyse: Fristen, Form, Zuständigkeit und Rechtsweg

## Spezialwissen: Risikoanalyse: Fristen, Form, Zuständigkeit und Rechtsweg
- **Spezialgegenstand:** Risikoanalyse: Fristen, Form, Zuständigkeit und Rechtsweg / risikoanalyse fristen form und zustaendigkeit. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** AML, KYC, GwG, UBO, PEP, FIU.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Risikoanalyse** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 2. `geldwaesche-bussgeld-reputation`

**Fokus:** Strukturierung von Bußgeldriskien Geschäftsleiterhaftung und Reputationsschaeden bei GwG-Verstoessen. Anwendungsfall Bußgeldbescheid nach GwG ist eingegangen oder negative Berichterstattung droht. Normen § 52 GwG Bußgelder bis 5 Mio EUR oder 10 Prozent Jahresumsatz § 130 OWiG Aufsichtspflichtverletzung. Prüfraster Bußgeldrisko Geschäftsleitungsverantwortung Pressekommunikation Kundenkommunikation Remediation Schadensbegrenzung. Output Massnahmenplan mit Widerspruchsstrategie PR-Linie Remediation-Nachweis und Haftungsabsicherung. Abgrenzung zu geldwäsche-behoerdenverfahren und geldwäsche-audit-internal-revision.

# Bußgeld, Haftung und Reputation

## Triage zu Beginn
1. Liegt ein BaFin-Bußgeldverfahren, eine Staatsanwaltschaftliche Ermittlung oder eine Presseanfrage vor?
2. Wer ist verantwortliche Person: Geldwäschebeauftragter, Geschaeftsfuehrer oder Verwaltungsrat?
3. Welche Remediation-Massnahmen wurden bereits eingeleitet?
4. Gibt es eine externe Kommunikations- oder PR-Strategie fuer den Reputationsschaden?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 56 GwG — Bußgeldtatbestaende (bis 5 Mio. EUR oder 10 % des Jahresumsatzes bei Kreditinstituten)
- § 57 GwG — Veroeffentlichung von Massnahmen (Naming and Shaming)
- § 30 OWiG — Verbandsgeldbusse
- § 130 OWiG — Aufsichtspflichtverletzung durch Geschaeftsleiter

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill bearbeitet Recht, Compliance, Kommunikation und Nachbesserung in kritischen AML-Lagen.

## Wann verwenden

- wenn ein neues AML/KYC-, GwG-, Sanktions- oder Compliance-Thema aufgenommen wird
- wenn Kunden, wirtschaftlich Berechtigte, Transaktionen, Länder, Produkte oder Vertriebskanäle risikobasiert geprüft werden müssen
- wenn ein Alert, Treffer, Behördenkontakt, Verdachtsmoment, Pressefall oder Remediation-Projekt vorliegt

## Arbeitsweise

1. **Rolle und Pflichtenkreis klären.** Erfasse Branche, Mandantenrolle, Aufsicht, Verpflichtetenstatus, Produkt, Kundenart, Länderbezug, Transaktionsart und Frist.
2. **Daten sauber ziehen.** Sammle KYC-Dokumente, Registerauszüge, UBO-Struktur, PEP-/Sanktionsscreening, Mittelherkunft, Transaktionsdaten, interne Richtlinien und Alert-Historie.
3. **Quellenstand protokollieren.** Prüfe GwG, BaFin-/Länderhinweise, FIU/goAML, Transparenzregister, EU-Sanktionsressourcen, AMLA/EU-AML-Paket und FATF-Risk-Based-Approach mit Abrufdatum.
4. **Risikobasiert entscheiden.** Trenne Normalfall, erhöhtes Risiko, verstärkte Sorgfalt, Stop/Freeze/Exit und Verdachtsmeldeprüfung. Keine automatische Freigabe bei Datenlücken.
5. **Verzeihend nachziehen.** Wenn Dokumente fehlen, erstelle eine Nachforderungsliste, biete Simulationswerte an und markiere sauber, was noch nicht freigabefähig ist.
6. **Arbeitsprodukt liefern.** Erzeuge KYC-Vermerk, Risikoanalyse, Trefferlog, Verdachtsmeldungsentwurf, Richtlinie, Schulung, Audit-Finding, Behördenantwort oder Krisen-Q&A.
7. **Qualitätstor.** Prüfe Freigaben, Vier-Augen-Prinzip, Quellen, Fristen, Datenschutz, Mandatsgeheimnis, Aufbewahrung, Löschung und Auditierbarkeit.

## Rückfragen, wenn unklar

- Welche Branche, Rolle und Aufsichtszuständigkeit hat der Mandant?
- Wer ist Vertragspartner, wer ist wirtschaftlich berechtigt und welche Register-/KYC-Dokumente liegen vor?
- Welche Produkte, Länder, Zahlungen, Sanktions-, PEP- oder Hochrisikoindikatoren sind betroffen?
- Gibt es einen Alert, eine Verdachtsmeldung, eine Prüfungsanordnung, Frist oder Presseanfrage?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?

## Ausgabeformat

- Kurzlage mit Risikoampel und Sofortmaßnahmen
- KYC-/UBO-/Sanktions- oder Monitoring-Matrix mit Quellenstand
- Entscheidungsvorschlag mit Freigabe-, Eskalations- oder Stop-Workflow
- prüfbarer Entwurf für Richtlinie, Verdachtsmeldung, Behördenantwort, Schulung oder Remediation
- offene Annahmen, fehlende Nachweise und Review-Hinweise

## Typische Fehler vermeiden

- Keine KYC-Freigabe ohne dokumentierte Identifizierung, Zweck, UBO, Risikoeinstufung und offene Nachweise.
- Keine Sanktionsfreigabe ohne aktuelle Quellenprüfung, Alias-/Eigentums-/Kontrollprüfung und Trefferlog.
- Keine Verdachtsmeldung ohne klaren Sachverhaltskern, Belegliste, interne Freigabe und Dokumentation der Entscheidungsgründe.
- Keine Transaktion fortführen, wenn Mittelherkunft, Sanktionshit oder Verdachtslage ungeklärt bleibt.
- Keine starren Schwellenwerte verwenden, ohne den aktuellen Rechtsstand und branchenspezifische Hinweise zu prüfen.
- Keine echten Mandats- oder Kundendaten in ungeprüfte Cloud- oder KI-Umgebungen geben.

## 3. `geldwaesche-sanktionsscreening`

**Fokus:** Sanktionsscreening von Kunden Transaktionen und Beteiligten gegen EU-US- und UN-Sanktionslisten. Anwendungsfall neues Geschäft soll abgeschlossen oder Transaktion freigegeben werden. Normen EU-Verordnungen 2580/2001 881/2002 Russland-VO 833/2014 269/2014 OFAC-SDN-Liste. Prüfraster Namensscreening Alias-Screening Eigentuems-Kontrolle Embargo-Check Trefferlog False-Positive-Bewertung. Output Screening-Protokoll mit Trefferliste False-Positive-Begründung Freigabe oder Meldepflicht. Abgrenzung zu geldwäsche-pep-hochrisikoland und geldwäsche-transaktionsmonitoring.

# Sanktionslistenprüfung und Embargoabgleich

## Triage zu Beginn
1. Welche Sanktionslisten sollen geprueft werden: EU, OFAC, UN, nationale Listen?
2. Liegt ein True-Hit oder ein False-Positive vor — und welche Dokumentation gibt es bereits?
3. Sind Eigentuems- oder Kontrollbeziehungen zum Sanctioned Entity zu pruefen?
4. Gibt es eine Transaktionssperr-Pflicht oder eine Verdachtsmeldepflicht ausloesende Treffer?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- Art. 2 EU-VO 2580/2001 — Einfrierungspflicht: sofortige Sperrung bei Sanktionstreffer
- § 25h KWG — Geldwaesche- und Betrugsverhinderung in Kreditinstituten: Screeningpflicht
- Art. 4 EU-VO 269/2014 (Russlandsanktionen) — aktuelle Sanktionsregeln
- § 18 AWG — Strafbarkeit bei Verstoss gegen Ausfuhrverbote und Embargos

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill bearbeitet AML/KYC mit Sanktions-Compliance und dokumentiert Trefferentscheidungen.

## Wann verwenden

- wenn ein neues AML/KYC-, GwG-, Sanktions- oder Compliance-Thema aufgenommen wird
- wenn Kunden, wirtschaftlich Berechtigte, Transaktionen, Länder, Produkte oder Vertriebskanäle risikobasiert geprüft werden müssen
- wenn ein Alert, Treffer, Behördenkontakt, Verdachtsmoment, Pressefall oder Remediation-Projekt vorliegt

## Arbeitsweise

1. **Rolle und Pflichtenkreis klären.** Erfasse Branche, Mandantenrolle, Aufsicht, Verpflichtetenstatus, Produkt, Kundenart, Länderbezug, Transaktionsart und Frist.
2. **Daten sauber ziehen.** Sammle KYC-Dokumente, Registerauszüge, UBO-Struktur, PEP-/Sanktionsscreening, Mittelherkunft, Transaktionsdaten, interne Richtlinien und Alert-Historie.
3. **Quellenstand protokollieren.** Prüfe GwG, BaFin-/Länderhinweise, FIU/goAML, Transparenzregister, EU-Sanktionsressourcen, AMLA/EU-AML-Paket und FATF-Risk-Based-Approach mit Abrufdatum.
4. **Risikobasiert entscheiden.** Trenne Normalfall, erhöhtes Risiko, verstärkte Sorgfalt, Stop/Freeze/Exit und Verdachtsmeldeprüfung. Keine automatische Freigabe bei Datenlücken.
5. **Verzeihend nachziehen.** Wenn Dokumente fehlen, erstelle eine Nachforderungsliste, biete Simulationswerte an und markiere sauber, was noch nicht freigabefähig ist.
6. **Arbeitsprodukt liefern.** Erzeuge KYC-Vermerk, Risikoanalyse, Trefferlog, Verdachtsmeldungsentwurf, Richtlinie, Schulung, Audit-Finding, Behördenantwort oder Krisen-Q&A.
7. **Qualitätstor.** Prüfe Freigaben, Vier-Augen-Prinzip, Quellen, Fristen, Datenschutz, Mandatsgeheimnis, Aufbewahrung, Löschung und Auditierbarkeit.

## Rückfragen, wenn unklar

- Welche Branche, Rolle und Aufsichtszuständigkeit hat der Mandant?
- Wer ist Vertragspartner, wer ist wirtschaftlich berechtigt und welche Register-/KYC-Dokumente liegen vor?
- Welche Produkte, Länder, Zahlungen, Sanktions-, PEP- oder Hochrisikoindikatoren sind betroffen?
- Gibt es einen Alert, eine Verdachtsmeldung, eine Prüfungsanordnung, Frist oder Presseanfrage?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?

## Ausgabeformat

- Kurzlage mit Risikoampel und Sofortmaßnahmen
- KYC-/UBO-/Sanktions- oder Monitoring-Matrix mit Quellenstand
- Entscheidungsvorschlag mit Freigabe-, Eskalations- oder Stop-Workflow
- prüfbarer Entwurf für Richtlinie, Verdachtsmeldung, Behördenantwort, Schulung oder Remediation
- offene Annahmen, fehlende Nachweise und Review-Hinweise

## Typische Fehler vermeiden

- Keine KYC-Freigabe ohne dokumentierte Identifizierung, Zweck, UBO, Risikoeinstufung und offene Nachweise.
- Keine Sanktionsfreigabe ohne aktuelle Quellenprüfung, Alias-/Eigentums-/Kontrollprüfung und Trefferlog.
- Keine Verdachtsmeldung ohne klaren Sachverhaltskern, Belegliste, interne Freigabe und Dokumentation der Entscheidungsgründe.
- Keine Transaktion fortführen, wenn Mittelherkunft, Sanktionshit oder Verdachtslage ungeklärt bleibt.
- Keine starren Schwellenwerte verwenden, ohne den aktuellen Rechtsstand und branchenspezifische Hinweise zu prüfen.
- Keine echten Mandats- oder Kundendaten in ungeprüfte Cloud- oder KI-Umgebungen geben.
