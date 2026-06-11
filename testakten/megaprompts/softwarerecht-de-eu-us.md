# Megaprompt: softwarerecht-de-eu-us

> *Achtung: Dies ist ein experimentelles Mega-Prompt-Markdown, das einen kompletten Klotzkette-Plugin in eine einzige Datei zusammenfuehrt. Keine Haftung, keine Gewaehr. Nur zum Ausprobieren der Skills auch ohne Claude Code; keine Rechtsberatung. Vor Verwendung im Mandat anwaltlich pruefen.*
>
> *Caution: This is an experimental Mega-Prompt Markdown that consolidates a full Klotzkette plugin into a single file. No warranty, no liability. For exploration with chat tools that do not run Claude Code only; not legal advice.*

**Verwendung:** Diesen gesamten Text in einen Chat ohne Claude-Code-Integration einfuegen (oder als Datei hochladen). Der Chat-Agent erhaelt damit die gebuendelten Skills dieses Plugins als Kontext. Eine Replikation des vollen Plugin-Verhaltens ist nicht garantiert — der Megaprompt ist eine Best-Effort-Kompression.


## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 105 Skills des Plugins `softwarerecht-de-eu-us`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Startet die Softwarerechtsprüfung für Entwicklung, Lizenz, SaaS, Open Source, Arbeitnehmer/Freelancer, EU/US/IP und Stre…
2. **rechtsabteilung-ki-saas-vertrag-werkvertrag** — Rechtsabteilungs-Fachmodul für KI-Code und Trainingsdaten im Lizenzvertrag: AI-assisted coding wird mit Warranty, Audit,…
3. **rechtsabteilung-us-work-made-for-hire-im-deutschen-projekt** — Rechtsabteilungs-Fachmodul für US Work Made for Hire im deutschen Projekt: US-Templates werden auf deutsche Rechteübertr…
4. **rechtsabteilung-data-act-und-cloud-switching-klauseln** — Rechtsabteilungs-Fachmodul für Data Act und Cloud-Switching-Klauseln: Softwareverträge werden auf Datenzugang, Portabili…
5. **rechtsabteilung-developer-ip-open-source-us** — Rechtsabteilungs-Fachmodul für Developer-IP bei deutschen Angestellten: Code-Rechte, Nebenprojekte, Repos und Freelancer…
6. **rechtsabteilung-open-source-copyleft-im-saas-stack** — Rechtsabteilungs-Fachmodul für Open-Source-Copyleft im SaaS-Stack: Komponenten werden in Copyleft, Notice, Patent Grant …
7. **employment-contract-software-engineer-de** — Entwirft Klauseln für deutsche angestellte Softwareingenieure zu § 69b, Nebentätigkeit, OSS, Geheimnissen, Erfindungen u…
8. **computerprogramm-69a-urhg-schutz** — Prüft Schutzgegenstand deutscher Computerprogramme, Ausdruck, Schnittstellen, Dokumentation, Vorbereitungsmaterial und A…
9. **us-software-patent-101** — Prüft US-Patentfähigkeit softwarebezogener Erfindungen nach § 101, abstract idea, practical application und eligibility …
10. **public-procurement-software** — Prüft öffentliche Softwarebeschaffung, EVB-IT, Leistungsbeschreibung, Cloud, Open Source, IT-Sicherheit und Nachprüfungs…
11. **software-mna-dd** — Prüft Software-IP, OSS, Datenschutz, Security, Verträge, Kundenlizenzen, Mitarbeiter/Freelancer und technische Schulden …
12. **trade-secret-misappropriation-code** — Prüft Entwendung von Source Code, Architektur, Roadmap, Kundendaten und Secrets durch Mitarbeiter, Contractor oder Wettb…
13. **software-scope-und-rechtsgebiet-router** — Ordnet ein Softwaremandat in Urheberrecht, Vertragsrecht, Datenschutz, Produktsicherheit, Patente, Open Source und Expor…
14. **secure-development-contract** — Entwirft Security-by-Design-Pflichten in Entwicklungsverträgen: SSDLC, threat modeling, secure coding, tests und remedia…
15. **us-trade-secret-dtsa** — Prüft Software als Trade Secret nach US-Recht: secrecy measures, misappropriation, employee mobility und repository evid…

---

## Skill: `kaltstart-triage`

_Startet die Softwarerechtsprüfung für Entwicklung, Lizenz, SaaS, Open Source, Arbeitnehmer/Freelancer, EU/US/IP und Streit._

# Kaltstart Softwarerecht

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Softwarerecht De Eu Us** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 69a UrhG` — Computerprogramme.
- `§ 69b UrhG` — Arbeitnehmerprogramme.
- `§ 69c UrhG` — ausschliessliche Rechte.
- `§ 69d UrhG` — bestimmungsgemaesse Benutzung.
- `§ 69e UrhG` — Dekompilierung.
- `§ 31 UrhG` — Einraeumung von Nutzungsrechten.
- `§ 32 UrhG` — angemessene Verguetung.
- `§ 305 BGB` — AGB-Einbeziehung.
- `§ 307 Abs. 1 BGB` — AGB-Inhaltskontrolle.
- `Art. 5 Abs. 1 DSGVO` — Datenschutz bei Softwarebetrieb.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Rechts- und Quellenanker

- UrhG §§ 69a-69g
- BGB Vertragsrecht
- Directive 2009/24/EC
- 17 U.S.C. §§ 101/201
- 35 U.S.C. § 101

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Was ist das Produkt: Individualsoftware, SaaS, Embedded, App, API, KI-Modell, Open-Source-Komponente oder Plattform?
- Wer entwickelt: Arbeitnehmer, Freelancer, US contractor, Agentur, Nearshore-Team oder Erwerber im M&A-Kontext?
- Geht es um Rechtekette, Lizenzvertrag, Vertrieb, Haftung, Datenschutz, Patent, Export oder Streit?
- Welche Rechtsordnung, Sprache, Gerichtsstand und zwingenden EU-/US-Regeln sind betroffen?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Was ist das Produkt: Individualsoftware, SaaS, Embedded, App, API, KI-Modell, Open-Source-Komponente oder Plattform?
- Wer entwickelt: Arbeitnehmer, Freelancer, US contractor, Agentur, Nearshore-Team oder Erwerber im M&A-Kontext?
- Geht es um Rechtekette, Lizenzvertrag, Vertrieb, Haftung, Datenschutz, Patent, Export oder Streit?
- Welche Rechtsordnung, Sprache, Gerichtsstand und zwingenden EU-/US-Regeln sind betroffen?

**Mindest-Output:** Routing-Memo mit Rechtsgebieten, Rollen, Dokumentenlücken, Risikobändern und nächstem Vertrags- oder Prüfpfad.

## Qualitäts- und Risikofilter

- Keine US-, EU- oder deutsche Spezialaussage ohne aktuellen Quellencheck über offizielle Quellen oder verifizierte Nutzerquelle.
- Rechtekette, tatsächliche technische Architektur und Vertragstext immer gemeinsam prüfen; eines allein reicht bei Software fast nie.
- Open Source, AI-Code, Freelancer und Drittland-/US-Bezug immer aktiv suchen, auch wenn die Anfrage nur nach Lizenzvertrag klingt.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen/Docket und frei prüfbarer Quelle nennen; keine BeckRS-/Juris-/Kommentar-Blindzitate.

---

## Skill: `rechtsabteilung-ki-saas-vertrag-werkvertrag`

_Rechtsabteilungs-Fachmodul für KI-Code und Trainingsdaten im Lizenzvertrag: AI-assisted coding wird mit Warranty, Audit, Indemnity und Source-Hygiene geregelt. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Softwarerecht De Eu Us._

# Rechtsabteilung: KI-Code und Trainingsdaten im Lizenzvertrag

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG §§ 69a-g, BGB §§ 433, 535, 535a, 651, EU-RL 2009/24, AGB-Recht, DSGVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Rechtsabteilung: KI-Code und Trainingsdaten im Lizenzvertrag
- **Normen-/Quellenanker:** UrhG §§ 69a ff., BGB, AGB-Recht, DSGVO, TTDSG/TDDDG, Open-Source-Lizenzen, AI Act, Exportkontrolle, US Copyright/Work-for-Hire und Patent-/Trade-Secret-Schnittstellen.
- **Entscheidende Weiche:** Trenne Code-Urheberschaft, Rechtekette, Lizenzmodell, SLA, Datenschutz, Security, Escrow, Open-Source-Compliance und internationale Rechteübertragung.

## Spezialkern: Rechtsabteilung: KI-Code und Trainingsdaten im Lizenzvertrag

- **Konkretes Problem:** AI-assisted coding wird mit Warranty, Audit, Indemnity und Source-Hygiene geregelt.
- **Norm-/Quellenanker:** BGB-Vertragsrecht, UrhG §§ 69a ff., GeschGehG, DSGVO, Data Act, Cyber Resilience Act, Open-Source-Lizenzen, US copyright/work-made-for-hire und Softwarepatent-Schnittstellen.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

AI Act, DSGVO, UrhG, Geschäftsgeheimnisse

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

AI-assisted coding wird mit Warranty, Audit, Indemnity und Source-Hygiene geregelt.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

---

## Skill: `rechtsabteilung-us-work-made-for-hire-im-deutschen-projekt`

_Rechtsabteilungs-Fachmodul für US Work Made for Hire im deutschen Projekt: US-Templates werden auf deutsche Rechteübertragung und moral rights angepasst. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Softwarerecht De Eu Us._

# Rechtsabteilung: US Work Made for Hire im deutschen Projekt

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG §§ 69a-g, BGB §§ 433, 535, 535a, 651, EU-RL 2009/24, AGB-Recht, DSGVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Rechtsabteilung: US Work Made for Hire im deutschen Projekt
- **Normen-/Quellenanker:** UrhG §§ 69a ff., BGB, AGB-Recht, DSGVO, TTDSG/TDDDG, Open-Source-Lizenzen, AI Act, Exportkontrolle, US Copyright/Work-for-Hire und Patent-/Trade-Secret-Schnittstellen.
- **Entscheidende Weiche:** Trenne Code-Urheberschaft, Rechtekette, Lizenzmodell, SLA, Datenschutz, Security, Escrow, Open-Source-Compliance und internationale Rechteübertragung.

## Spezialkern: Rechtsabteilung: US Work Made for Hire im deutschen Projekt

- **Konkretes Problem:** US-Templates werden auf deutsche Rechteübertragung und moral rights angepasst.
- **Norm-/Quellenanker:** BGB-Vertragsrecht, UrhG §§ 69a ff., GeschGehG, DSGVO, Data Act, Cyber Resilience Act, Open-Source-Lizenzen, US copyright/work-made-for-hire und Softwarepatent-Schnittstellen.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

US Copyright Act; deutsches IPR; UrhG

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

US-Templates werden auf deutsche Rechteübertragung und moral rights angepasst.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

---

## Skill: `rechtsabteilung-data-act-und-cloud-switching-klauseln`

_Rechtsabteilungs-Fachmodul für Data Act und Cloud-Switching-Klauseln: Softwareverträge werden auf Datenzugang, Portabilität und Exit-Charges geprüft. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Softwarerecht De Eu Us._

# Rechtsabteilung: Data Act und Cloud-Switching-Klauseln

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG §§ 69a-g, BGB §§ 433, 535, 535a, 651, EU-RL 2009/24, AGB-Recht, DSGVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Rechtsabteilung: Data Act und Cloud-Switching-Klauseln
- **Normen-/Quellenanker:** UrhG §§ 69a ff., BGB, AGB-Recht, DSGVO, TTDSG/TDDDG, Open-Source-Lizenzen, AI Act, Exportkontrolle, US Copyright/Work-for-Hire und Patent-/Trade-Secret-Schnittstellen.
- **Entscheidende Weiche:** Trenne Code-Urheberschaft, Rechtekette, Lizenzmodell, SLA, Datenschutz, Security, Escrow, Open-Source-Compliance und internationale Rechteübertragung.

## Spezialkern: Rechtsabteilung: Data Act und Cloud-Switching-Klauseln

- **Konkretes Problem:** Softwareverträge werden auf Datenzugang, Portabilität und Exit-Charges geprüft.
- **Norm-/Quellenanker:** BGB-Vertragsrecht, UrhG §§ 69a ff., GeschGehG, DSGVO, Data Act, Cyber Resilience Act, Open-Source-Lizenzen, US copyright/work-made-for-hire und Softwarepatent-Schnittstellen.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

VO EU 2023/2854 Data Act; DSGVO; Geschäftsgeheimnisse

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Softwareverträge werden auf Datenzugang, Portabilität und Exit-Charges geprüft.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

---

## Skill: `rechtsabteilung-developer-ip-open-source-us`

_Rechtsabteilungs-Fachmodul für Developer-IP bei deutschen Angestellten: Code-Rechte, Nebenprojekte, Repos und Freelancer-Beiträge werden aufgeklärt. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Softwarerecht De Eu Us._

# Rechtsabteilung: Developer-IP bei deutschen Angestellten

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG §§ 69a-g, BGB §§ 433, 535, 535a, 651, EU-RL 2009/24, AGB-Recht, DSGVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Rechtsabteilung: Developer-IP bei deutschen Angestellten
- **Normen-/Quellenanker:** UrhG §§ 69a ff., BGB, AGB-Recht, DSGVO, TTDSG/TDDDG, Open-Source-Lizenzen, AI Act, Exportkontrolle, US Copyright/Work-for-Hire und Patent-/Trade-Secret-Schnittstellen.
- **Entscheidende Weiche:** Trenne Code-Urheberschaft, Rechtekette, Lizenzmodell, SLA, Datenschutz, Security, Escrow, Open-Source-Compliance und internationale Rechteübertragung.

## Spezialkern: Rechtsabteilung: Developer-IP bei deutschen Angestellten

- **Konkretes Problem:** Code-Rechte, Nebenprojekte, Repos und Freelancer-Beiträge werden aufgeklärt.
- **Norm-/Quellenanker:** BGB-Vertragsrecht, UrhG §§ 69a ff., GeschGehG, DSGVO, Data Act, Cyber Resilience Act, Open-Source-Lizenzen, US copyright/work-made-for-hire und Softwarepatent-Schnittstellen.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

UrhG §§ 69a, 69b; ArbEG nur bei Erfindungen

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Code-Rechte, Nebenprojekte, Repos und Freelancer-Beiträge werden aufgeklärt.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

---

## Skill: `rechtsabteilung-open-source-copyleft-im-saas-stack`

_Rechtsabteilungs-Fachmodul für Open-Source-Copyleft im SaaS-Stack: Komponenten werden in Copyleft, Notice, Patent Grant und SaaS-Trigger getrennt. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Softwarerecht De Eu Us._

# Rechtsabteilung: Open-Source-Copyleft im SaaS-Stack

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG §§ 69a-g, BGB §§ 433, 535, 535a, 651, EU-RL 2009/24, AGB-Recht, DSGVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Rechtsabteilung: Open-Source-Copyleft im SaaS-Stack
- **Normen-/Quellenanker:** UrhG §§ 69a ff., BGB, AGB-Recht, DSGVO, TTDSG/TDDDG, Open-Source-Lizenzen, AI Act, Exportkontrolle, US Copyright/Work-for-Hire und Patent-/Trade-Secret-Schnittstellen.
- **Entscheidende Weiche:** Trenne Code-Urheberschaft, Rechtekette, Lizenzmodell, SLA, Datenschutz, Security, Escrow, Open-Source-Compliance und internationale Rechteübertragung.

## Spezialkern: Rechtsabteilung: Open-Source-Copyleft im SaaS-Stack

- **Konkretes Problem:** Komponenten werden in Copyleft, Notice, Patent Grant und SaaS-Trigger getrennt.
- **Norm-/Quellenanker:** BGB-Vertragsrecht, UrhG §§ 69a ff., GeschGehG, DSGVO, Data Act, Cyber Resilience Act, Open-Source-Lizenzen, US copyright/work-made-for-hire und Softwarepatent-Schnittstellen.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

GPL, AGPL, MIT, Apache; UrhG §§ 69a ff.; US Copyright als Vergleich

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Komponenten werden in Copyleft, Notice, Patent Grant und SaaS-Trigger getrennt.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

---

## Skill: `employment-contract-software-engineer-de`

_Entwirft Klauseln für deutsche angestellte Softwareingenieure zu § 69b, Nebentätigkeit, OSS, Geheimnissen, Erfindungen und Offboarding im Softwarerecht De Eu Us._

# Arbeitsvertrag Software Engineer DE

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG §§ 69a-g, BGB §§ 433, 535, 535a, 651, EU-RL 2009/24, AGB-Recht, DSGVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Arbeitsvertrag Software Engineer DE
- **Normen-/Quellenanker:** UrhG §§ 69a ff., BGB, AGB-Recht, DSGVO, TTDSG/TDDDG, Open-Source-Lizenzen, AI Act, Exportkontrolle, US Copyright/Work-for-Hire und Patent-/Trade-Secret-Schnittstellen.
- **Entscheidende Weiche:** Trenne Code-Urheberschaft, Rechtekette, Lizenzmodell, SLA, Datenschutz, Security, Escrow, Open-Source-Compliance und internationale Rechteübertragung.

## Rechts- und Quellenanker

- UrhG § 69b
- ArbEG
- GeschGehG
- BGB/ArbR

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Welche Aufgaben erzeugen Softwarerechte kraft Arbeitsvertrag?
- Welche private Vorarbeiten und Nebenprojekte müssen offengelegt werden?
- Wie werden OSS-Beiträge, Hackathons, AI tools und private Geräte geregelt?
- Welche Offboarding-Pflichten sichern Repository, Dokumentation und Zugänge?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Welche Aufgaben erzeugen Softwarerechte kraft Arbeitsvertrag?
- Welche private Vorarbeiten und Nebenprojekte müssen offengelegt werden?
- Wie werden OSS-Beiträge, Hackathons, AI tools und private Geräte geregelt?
- Welche Offboarding-Pflichten sichern Repository, Dokumentation und Zugänge?

**Mindest-Output:** Arbeitsvertragsmodul mit IP-, OSS-, Erfindungs-, Confidentiality- und Offboarding-Klauseln.

## Qualitäts- und Risikofilter

- Keine US-, EU- oder deutsche Spezialaussage ohne aktuellen Quellencheck über offizielle Quellen oder verifizierte Nutzerquelle.
- Rechtekette, tatsächliche technische Architektur und Vertragstext immer gemeinsam prüfen; eines allein reicht bei Software fast nie.
- Open Source, AI-Code, Freelancer und Drittland-/US-Bezug immer aktiv suchen, auch wenn die Anfrage nur nach Lizenzvertrag klingt.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen/Docket und frei prüfbarer Quelle nennen; keine BeckRS-/Juris-/Kommentar-Blindzitate.

---

## Skill: `computerprogramm-69a-urhg-schutz`

_Prüft Schutzgegenstand deutscher Computerprogramme, Ausdruck, Schnittstellen, Dokumentation, Vorbereitungsmaterial und Ausschlüsse im Softwarerecht De Eu Us._

# Computerprogramm-Schutz § 69a UrhG

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG §§ 69a-g, BGB §§ 433, 535, 535a, 651, EU-RL 2009/24, AGB-Recht, DSGVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Computerprogramm-Schutz § 69a UrhG
- **Normen-/Quellenanker:** UrhG §§ 69a ff., BGB, AGB-Recht, DSGVO, TTDSG/TDDDG, Open-Source-Lizenzen, AI Act, Exportkontrolle, US Copyright/Work-for-Hire und Patent-/Trade-Secret-Schnittstellen.
- **Entscheidende Weiche:** Trenne Code-Urheberschaft, Rechtekette, Lizenzmodell, SLA, Datenschutz, Security, Escrow, Open-Source-Compliance und internationale Rechteübertragung.

## Rechts- und Quellenanker

- UrhG §§ 69a/69c
- Directive 2009/24/EC Art. 1

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Was ist Ausdruck eines Computerprogramms und was nur Idee, Algorithmus, Logik, Funktion oder Schnittstelle?
- Gibt es Vorbereitungsmaterial mit programmspezifischer späterer Umsetzung?
- Sind GUI, Dokumentation, Datenbank oder API separat zu prüfen?
- Welche Teile müssen im Vertrag ausdrücklich einbezogen werden?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Was ist Ausdruck eines Computerprogramms und was nur Idee, Algorithmus, Logik, Funktion oder Schnittstelle?
- Gibt es Vorbereitungsmaterial mit programmspezifischer späterer Umsetzung?
- Sind GUI, Dokumentation, Datenbank oder API separat zu prüfen?
- Welche Teile müssen im Vertrag ausdrücklich einbezogen werden?

**Mindest-Output:** Schutzgegenstands-Matrix mit Programmteilen, geschützten Elementen, Ausschlüssen und Vertragsfolge.

## Qualitäts- und Risikofilter

- Keine US-, EU- oder deutsche Spezialaussage ohne aktuellen Quellencheck über offizielle Quellen oder verifizierte Nutzerquelle.
- Rechtekette, tatsächliche technische Architektur und Vertragstext immer gemeinsam prüfen; eines allein reicht bei Software fast nie.
- Open Source, AI-Code, Freelancer und Drittland-/US-Bezug immer aktiv suchen, auch wenn die Anfrage nur nach Lizenzvertrag klingt.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen/Docket und frei prüfbarer Quelle nennen; keine BeckRS-/Juris-/Kommentar-Blindzitate.

---

## Skill: `us-software-patent-101`

_Prüft US-Patentfähigkeit softwarebezogener Erfindungen nach § 101, abstract idea, practical application und eligibility guidance im Softwarerecht De Eu Us._

# US Software Patent § 101

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG §§ 69a-g, BGB §§ 433, 535, 535a, 651, EU-RL 2009/24, AGB-Recht, DSGVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: US Software Patent § 101
- **Normen-/Quellenanker:** UrhG §§ 69a ff., BGB, AGB-Recht, DSGVO, TTDSG/TDDDG, Open-Source-Lizenzen, AI Act, Exportkontrolle, US Copyright/Work-for-Hire und Patent-/Trade-Secret-Schnittstellen.
- **Entscheidende Weiche:** Trenne Code-Urheberschaft, Rechtekette, Lizenzmodell, SLA, Datenschutz, Security, Escrow, Open-Source-Compliance und internationale Rechteübertragung.

## Rechts- und Quellenanker

- 35 U.S.C. § 101
- USPTO subject matter eligibility guidance
- MPEP § 2106

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Welches technische Problem löst die Software konkret?
- Ist der Claim nur abstract idea, business method, math oder mental process?
- Welche additional elements integrieren die Idee in practical application?
- Welche Claim-Fassung vermeidet bloßes generic computer implementation?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Welches technische Problem löst die Software konkret?
- Ist der Claim nur abstract idea, business method, math oder mental process?
- Welche additional elements integrieren die Idee in practical application?
- Welche Claim-Fassung vermeidet bloßes generic computer implementation?

**Mindest-Output:** Eligibility-Memo mit Claim-Elementen, § 101-Risiko und Drafting-Hinweisen.

## Qualitäts- und Risikofilter

- Keine US-, EU- oder deutsche Spezialaussage ohne aktuellen Quellencheck über offizielle Quellen oder verifizierte Nutzerquelle.
- Rechtekette, tatsächliche technische Architektur und Vertragstext immer gemeinsam prüfen; eines allein reicht bei Software fast nie.
- Open Source, AI-Code, Freelancer und Drittland-/US-Bezug immer aktiv suchen, auch wenn die Anfrage nur nach Lizenzvertrag klingt.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen/Docket und frei prüfbarer Quelle nennen; keine BeckRS-/Juris-/Kommentar-Blindzitate.

---

## Skill: `public-procurement-software`

_Prüft öffentliche Softwarebeschaffung, EVB-IT, Leistungsbeschreibung, Cloud, Open Source, IT-Sicherheit und Nachprüfungsrisiken im Softwarerecht De Eu Us._

# Vergabe von Software

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 69a UrhG` — Computerprogramme.
- `§ 69b UrhG` — Arbeitnehmerprogramme.
- `§ 69c UrhG` — ausschliessliche Rechte.
- `§ 69d UrhG` — bestimmungsgemaesse Benutzung.
- `§ 69e UrhG` — Dekompilierung.
- `§ 31 UrhG` — Einraeumung von Nutzungsrechten.
- `§ 32 UrhG` — angemessene Verguetung.
- `§ 305 BGB` — AGB-Einbeziehung.
- `§ 307 Abs. 1 BGB` — AGB-Inhaltskontrolle.
- `Art. 5 Abs. 1 DSGVO` — Datenschutz bei Softwarebetrieb.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG §§ 69a-g, BGB §§ 433, 535, 535a, 651, EU-RL 2009/24, AGB-Recht, DSGVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Vergabe von Software
- **Normen-/Quellenanker:** UrhG §§ 69a ff., BGB, AGB-Recht, DSGVO, TTDSG/TDDDG, Open-Source-Lizenzen, AI Act, Exportkontrolle, US Copyright/Work-for-Hire und Patent-/Trade-Secret-Schnittstellen.
- **Entscheidende Weiche:** Trenne Code-Urheberschaft, Rechtekette, Lizenzmodell, SLA, Datenschutz, Security, Escrow, Open-Source-Compliance und internationale Rechteübertragung.

## Rechts- und Quellenanker

- GWB/VgV/UVgO
- EVB-IT
- DSGVO/IT-Sicherheit

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Welche Vertragsart: Kauf, Pflege, Dienstleistung, Erstellung, Cloud oder System?
- Ist die Leistungsbeschreibung produktneutral, funktional und vergabefest?
- Welche EVB-IT-Bausteine passen und welche müssen angepasst werden?
- Welche Eignungs-, Zuschlags- und Datenschutzkriterien sind belastbar?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Welche Vertragsart: Kauf, Pflege, Dienstleistung, Erstellung, Cloud oder System?
- Ist die Leistungsbeschreibung produktneutral, funktional und vergabefest?
- Welche EVB-IT-Bausteine passen und welche müssen angepasst werden?
- Welche Eignungs-, Zuschlags- und Datenschutzkriterien sind belastbar?

**Mindest-Output:** Vergabe-Check mit Verfahrensroute, EVB-IT-Auswahl, Kriterien und Risikoampel.

## Qualitäts- und Risikofilter

- Keine US-, EU- oder deutsche Spezialaussage ohne aktuellen Quellencheck über offizielle Quellen oder verifizierte Nutzerquelle.
- Rechtekette, tatsächliche technische Architektur und Vertragstext immer gemeinsam prüfen; eines allein reicht bei Software fast nie.
- Open Source, AI-Code, Freelancer und Drittland-/US-Bezug immer aktiv suchen, auch wenn die Anfrage nur nach Lizenzvertrag klingt.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen/Docket und frei prüfbarer Quelle nennen; keine BeckRS-/Juris-/Kommentar-Blindzitate.

---

## Skill: `software-mna-dd`

_Prüft Software-IP, OSS, Datenschutz, Security, Verträge, Kundenlizenzen, Mitarbeiter/Freelancer und technische Schulden im Deal im Softwarerecht De Eu Us._

# Software M&A Due Diligence

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 69a UrhG` — Computerprogramme.
- `§ 69b UrhG` — Arbeitnehmerprogramme.
- `§ 69c UrhG` — ausschliessliche Rechte.
- `§ 69d UrhG` — bestimmungsgemaesse Benutzung.
- `§ 69e UrhG` — Dekompilierung.
- `§ 31 UrhG` — Einraeumung von Nutzungsrechten.
- `§ 32 UrhG` — angemessene Verguetung.
- `§ 305 BGB` — AGB-Einbeziehung.
- `§ 307 Abs. 1 BGB` — AGB-Inhaltskontrolle.
- `Art. 5 Abs. 1 DSGVO` — Datenschutz bei Softwarebetrieb.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG §§ 69a-g, BGB §§ 433, 535, 535a, 651, EU-RL 2009/24, AGB-Recht, DSGVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Software M&A Due Diligence
- **Normen-/Quellenanker:** UrhG §§ 69a ff., BGB, AGB-Recht, DSGVO, TTDSG/TDDDG, Open-Source-Lizenzen, AI Act, Exportkontrolle, US Copyright/Work-for-Hire und Patent-/Trade-Secret-Schnittstellen.
- **Entscheidende Weiche:** Trenne Code-Urheberschaft, Rechtekette, Lizenzmodell, SLA, Datenschutz, Security, Escrow, Open-Source-Compliance und internationale Rechteübertragung.

## Rechts- und Quellenanker

- UrhG/PatG/GeschGehG
- DSGVO
- BGB Verträge

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Welche Produkte generieren Wert und welche Rechtekette trägt sie?
- Welche Entwickler, Freelancer, Acquisitions und OSS-Komponenten sind kritisch?
- Welche Kundenverträge begrenzen Assignments, change of control oder Audit?
- Welche Red Flags brauchen SPA guarantees, indemnities, holdback oder remediation CP?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Welche Produkte generieren Wert und welche Rechtekette trägt sie?
- Welche Entwickler, Freelancer, Acquisitions und OSS-Komponenten sind kritisch?
- Welche Kundenverträge begrenzen Assignments, change of control oder Audit?
- Welche Red Flags brauchen SPA guarantees, indemnities, holdback oder remediation CP?

**Mindest-Output:** Software-DD-Report mit Red Flags, Evidence, SPA-Klauseln und Closing Conditions.

## Qualitäts- und Risikofilter

- Keine US-, EU- oder deutsche Spezialaussage ohne aktuellen Quellencheck über offizielle Quellen oder verifizierte Nutzerquelle.
- Rechtekette, tatsächliche technische Architektur und Vertragstext immer gemeinsam prüfen; eines allein reicht bei Software fast nie.
- Open Source, AI-Code, Freelancer und Drittland-/US-Bezug immer aktiv suchen, auch wenn die Anfrage nur nach Lizenzvertrag klingt.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen/Docket und frei prüfbarer Quelle nennen; keine BeckRS-/Juris-/Kommentar-Blindzitate.

---

## Skill: `trade-secret-misappropriation-code`

_Prüft Entwendung von Source Code, Architektur, Roadmap, Kundendaten und Secrets durch Mitarbeiter, Contractor oder Wettbewerber im Softwarerecht De Eu Us._

# Trade Secret Misappropriation Code

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 69a UrhG` — Computerprogramme.
- `§ 69b UrhG` — Arbeitnehmerprogramme.
- `§ 69c UrhG` — ausschliessliche Rechte.
- `§ 69d UrhG` — bestimmungsgemaesse Benutzung.
- `§ 69e UrhG` — Dekompilierung.
- `§ 31 UrhG` — Einraeumung von Nutzungsrechten.
- `§ 32 UrhG` — angemessene Verguetung.
- `§ 305 BGB` — AGB-Einbeziehung.
- `§ 307 Abs. 1 BGB` — AGB-Inhaltskontrolle.
- `Art. 5 Abs. 1 DSGVO` — Datenschutz bei Softwarebetrieb.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG §§ 69a-g, BGB §§ 433, 535, 535a, 651, EU-RL 2009/24, AGB-Recht, DSGVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Trade Secret Misappropriation Code
- **Normen-/Quellenanker:** UrhG §§ 69a ff., BGB, AGB-Recht, DSGVO, TTDSG/TDDDG, Open-Source-Lizenzen, AI Act, Exportkontrolle, US Copyright/Work-for-Hire und Patent-/Trade-Secret-Schnittstellen.
- **Entscheidende Weiche:** Trenne Code-Urheberschaft, Rechtekette, Lizenzmodell, SLA, Datenschutz, Security, Escrow, Open-Source-Compliance und internationale Rechteübertragung.

## Rechts- und Quellenanker

- GeschGehG
- DTSA bei US-Bezug
- Arbeits-/Vertragsrecht

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Welche Information ist konkret geheim und geschützt?
- Welche angemessenen Geheimhaltungsmaßnahmen bestanden?
- Wie erfolgte Zugriff, Download, Kopie, Weitergabe oder Nutzung?
- Welche forensischen und prozessualen Schritte sind nötig?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Welche Information ist konkret geheim und geschützt?
- Welche angemessenen Geheimhaltungsmaßnahmen bestanden?
- Wie erfolgte Zugriff, Download, Kopie, Weitergabe oder Nutzung?
- Welche forensischen und prozessualen Schritte sind nötig?

**Mindest-Output:** Trade-Secret-Claim-Paket mit Secret-ID, Maßnahmen, Timeline und Relief.

## Qualitäts- und Risikofilter

- Keine US-, EU- oder deutsche Spezialaussage ohne aktuellen Quellencheck über offizielle Quellen oder verifizierte Nutzerquelle.
- Rechtekette, tatsächliche technische Architektur und Vertragstext immer gemeinsam prüfen; eines allein reicht bei Software fast nie.
- Open Source, AI-Code, Freelancer und Drittland-/US-Bezug immer aktiv suchen, auch wenn die Anfrage nur nach Lizenzvertrag klingt.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen/Docket und frei prüfbarer Quelle nennen; keine BeckRS-/Juris-/Kommentar-Blindzitate.

---

## Skill: `software-scope-und-rechtsgebiet-router`

_Ordnet ein Softwaremandat in Urheberrecht, Vertragsrecht, Datenschutz, Produktsicherheit, Patente, Open Source und Export ein im Softwarerecht De Eu Us._

# Scope- und Rechtsgebietsrouter

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG §§ 69a-g, BGB §§ 433, 535, 535a, 651, EU-RL 2009/24, AGB-Recht, DSGVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Scope- und Rechtsgebietsrouter
- **Normen-/Quellenanker:** UrhG §§ 69a ff., BGB, AGB-Recht, DSGVO, TTDSG/TDDDG, Open-Source-Lizenzen, AI Act, Exportkontrolle, US Copyright/Work-for-Hire und Patent-/Trade-Secret-Schnittstellen.
- **Entscheidende Weiche:** Trenne Code-Urheberschaft, Rechtekette, Lizenzmodell, SLA, Datenschutz, Security, Escrow, Open-Source-Compliance und internationale Rechteübertragung.

## Rechts- und Quellenanker

- UrhG §§ 69a-69g
- BGB
- DSGVO
- CRA
- Data Act

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Welche Module, Daten, Schnittstellen, Dokumentation, Modelle und Third-Party-Assets gehören zur Software?
- Welche Nutzung wird erlaubt: install, access, reproduce, modify, distribute, sublicense, host oder train?
- Welche Regulierung hängt am Einsatz: personenbezogene Daten, Security, AI, Medizin, Finanzen, Industrie oder Behörden?
- Welche Rechtsfragen sind Vorfragen für den Vertrag und welche können als Issue List offenbleiben?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Welche Module, Daten, Schnittstellen, Dokumentation, Modelle und Third-Party-Assets gehören zur Software?
- Welche Nutzung wird erlaubt: install, access, reproduce, modify, distribute, sublicense, host oder train?
- Welche Regulierung hängt am Einsatz: personenbezogene Daten, Security, AI, Medizin, Finanzen, Industrie oder Behörden?
- Welche Rechtsfragen sind Vorfragen für den Vertrag und welche können als Issue List offenbleiben?

**Mindest-Output:** Mandatslandkarte mit Modul-/Rechte-/Regulierungs-Matrix.

## Qualitäts- und Risikofilter

- Keine US-, EU- oder deutsche Spezialaussage ohne aktuellen Quellencheck über offizielle Quellen oder verifizierte Nutzerquelle.
- Rechtekette, tatsächliche technische Architektur und Vertragstext immer gemeinsam prüfen; eines allein reicht bei Software fast nie.
- Open Source, AI-Code, Freelancer und Drittland-/US-Bezug immer aktiv suchen, auch wenn die Anfrage nur nach Lizenzvertrag klingt.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen/Docket und frei prüfbarer Quelle nennen; keine BeckRS-/Juris-/Kommentar-Blindzitate.

---

## Skill: `secure-development-contract`

_Entwirft Security-by-Design-Pflichten in Entwicklungsverträgen: SSDLC, threat modeling, secure coding, tests und remediation im Softwarerecht De Eu Us._

# Secure Development Contract

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 69a UrhG` — Computerprogramme.
- `§ 69b UrhG` — Arbeitnehmerprogramme.
- `§ 69c UrhG` — ausschliessliche Rechte.
- `§ 69d UrhG` — bestimmungsgemaesse Benutzung.
- `§ 69e UrhG` — Dekompilierung.
- `§ 31 UrhG` — Einraeumung von Nutzungsrechten.
- `§ 32 UrhG` — angemessene Verguetung.
- `§ 305 BGB` — AGB-Einbeziehung.
- `§ 307 Abs. 1 BGB` — AGB-Inhaltskontrolle.
- `Art. 5 Abs. 1 DSGVO` — Datenschutz bei Softwarebetrieb.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG §§ 69a-g, BGB §§ 433, 535, 535a, 651, EU-RL 2009/24, AGB-Recht, DSGVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Secure Development Contract
- **Normen-/Quellenanker:** UrhG §§ 69a ff., BGB, AGB-Recht, DSGVO, TTDSG/TDDDG, Open-Source-Lizenzen, AI Act, Exportkontrolle, US Copyright/Work-for-Hire und Patent-/Trade-Secret-Schnittstellen.
- **Entscheidende Weiche:** Trenne Code-Urheberschaft, Rechtekette, Lizenzmodell, SLA, Datenschutz, Security, Escrow, Open-Source-Compliance und internationale Rechteübertragung.

## Rechts- und Quellenanker

- CRA
- NIS-2
- ISO/SOC nur wenn vereinbart

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Welche Security-Anforderungen sind deliverable und prüfbar?
- Wer macht threat modeling, code scanning, dependency updates und penetration tests?
- Welche vulnerabilities blockieren Abnahme oder Release?
- Wie werden disclosure, patch windows und support geregelt?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Welche Security-Anforderungen sind deliverable und prüfbar?
- Wer macht threat modeling, code scanning, dependency updates und penetration tests?
- Welche vulnerabilities blockieren Abnahme oder Release?
- Wie werden disclosure, patch windows und support geregelt?

**Mindest-Output:** Secure-Development-Klauselpaket mit SSDLC, Tests, Akzeptanz und Patchpflichten.

## Qualitäts- und Risikofilter

- Keine US-, EU- oder deutsche Spezialaussage ohne aktuellen Quellencheck über offizielle Quellen oder verifizierte Nutzerquelle.
- Rechtekette, tatsächliche technische Architektur und Vertragstext immer gemeinsam prüfen; eines allein reicht bei Software fast nie.
- Open Source, AI-Code, Freelancer und Drittland-/US-Bezug immer aktiv suchen, auch wenn die Anfrage nur nach Lizenzvertrag klingt.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen/Docket und frei prüfbarer Quelle nennen; keine BeckRS-/Juris-/Kommentar-Blindzitate.

---

## Skill: `us-trade-secret-dtsa`

_Prüft Software als Trade Secret nach US-Recht: secrecy measures, misappropriation, employee mobility und repository evidence im Softwarerecht De Eu Us._

# US Trade Secret DTSA Software

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 69a UrhG` — Computerprogramme.
- `§ 69b UrhG` — Arbeitnehmerprogramme.
- `§ 69c UrhG` — ausschliessliche Rechte.
- `§ 69d UrhG` — bestimmungsgemaesse Benutzung.
- `§ 69e UrhG` — Dekompilierung.
- `§ 31 UrhG` — Einraeumung von Nutzungsrechten.
- `§ 32 UrhG` — angemessene Verguetung.
- `§ 305 BGB` — AGB-Einbeziehung.
- `§ 307 Abs. 1 BGB` — AGB-Inhaltskontrolle.
- `Art. 5 Abs. 1 DSGVO` — Datenschutz bei Softwarebetrieb.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG §§ 69a-g, BGB §§ 433, 535, 535a, 651, EU-RL 2009/24, AGB-Recht, DSGVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: US Trade Secret DTSA Software
- **Normen-/Quellenanker:** UrhG §§ 69a ff., BGB, AGB-Recht, DSGVO, TTDSG/TDDDG, Open-Source-Lizenzen, AI Act, Exportkontrolle, US Copyright/Work-for-Hire und Patent-/Trade-Secret-Schnittstellen.
- **Entscheidende Weiche:** Trenne Code-Urheberschaft, Rechtekette, Lizenzmodell, SLA, Datenschutz, Security, Escrow, Open-Source-Compliance und internationale Rechteübertragung.

## Rechts- und Quellenanker

- Defend Trade Secrets Act
- State trade secret law
- NDAs

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Welche Informationen sind tatsächlich geheim und wirtschaftlich wertvoll?
- Welche Schutzmaßnahmen existieren: access control, logging, NDAs, need-to-know?
- Wie wurde der Code entnommen, kopiert oder genutzt?
- Welche einstweiligen Maßnahmen und forensischen Schritte sind nötig?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Welche Informationen sind tatsächlich geheim und wirtschaftlich wertvoll?
- Welche Schutzmaßnahmen existieren: access control, logging, NDAs, need-to-know?
- Wie wurde der Code entnommen, kopiert oder genutzt?
- Welche einstweiligen Maßnahmen und forensischen Schritte sind nötig?

**Mindest-Output:** Trade-Secret-Paket mit Secret-ID, Maßnahmen, Misappropriation-Timeline und Evidence Hold.

## Qualitäts- und Risikofilter

- Keine US-, EU- oder deutsche Spezialaussage ohne aktuellen Quellencheck über offizielle Quellen oder verifizierte Nutzerquelle.
- Rechtekette, tatsächliche technische Architektur und Vertragstext immer gemeinsam prüfen; eines allein reicht bei Software fast nie.
- Open Source, AI-Code, Freelancer und Drittland-/US-Bezug immer aktiv suchen, auch wenn die Anfrage nur nach Lizenzvertrag klingt.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen/Docket und frei prüfbarer Quelle nennen; keine BeckRS-/Juris-/Kommentar-Blindzitate.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

