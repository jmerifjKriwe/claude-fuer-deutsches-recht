# Megaprompt: versicherungsrecht

> *Achtung: Dies ist ein experimentelles Mega-Prompt-Markdown, das einen kompletten Klotzkette-Plugin in eine einzige Datei zusammenfuehrt. Keine Haftung, keine Gewaehr. Nur zum Ausprobieren der Skills auch ohne Claude Code; keine Rechtsberatung. Vor Verwendung im Mandat anwaltlich pruefen.*
>
> *Caution: This is an experimental Mega-Prompt Markdown that consolidates a full Klotzkette plugin into a single file. No warranty, no liability. For exploration with chat tools that do not run Claude Code only; not legal advice.*

**Verwendung:** Diesen gesamten Text in einen Chat ohne Claude-Code-Integration einfuegen (oder als Datei hochladen). Der Chat-Agent erhaelt damit die gebuendelten Skills dieses Plugins als Kontext. Eine Replikation des vollen Plugin-Verhaltens ist nicht garantiert — der Megaprompt ist eine Best-Effort-Kompression.


## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 64 Skills des Plugins `versicherungsrecht`.

## Inhaltsverzeichnis

1. **rechtsabteilung-betriebsunterbrechung** — Rechtsabteilungs-Fachmodul für Betriebsunterbrechung und Lieferkettenausfall: Unterbrechungsschaden, Trigger, Wartezeit …
2. **rechtsabteilung-rechtsschutzversicherung-im-massenverfahren** — Rechtsabteilungs-Fachmodul für Rechtsschutzversicherung im Massenverfahren: Deckungsanfrage, Stichentscheid und Erfolgsa…
3. **rechtsabteilung-d-umwelthaftpflicht** — Rechtsabteilungs-Fachmodul für D&O-Deckung bei Organhaftung: Notification, Serienschaden, Selbstbehalt und Ausschlüsse w…
4. **rechtsabteilung-idd-vertrieb-und-provisionskonflikt** — Rechtsabteilungs-Fachmodul für IDD-Vertrieb und Provisionskonflikt: Produktvertrieb wird auf Interessenkonflikte, Dokume…
5. **rechtsabteilung-cyberversicherung-nach-ransomware** — Rechtsabteilungs-Fachmodul für Cyberversicherung nach Ransomware: Deckung, Anzeige, Forensik und Lösegeldklauseln werden…
6. **vvg-versicherung-wohngebaeude-leitungswasser** — Versicherung für fremde Rechnung: wer darf Leistung verlangen, wem stehen Einwendungen entgegen, welche Rolle haben Sich…
7. **vers-fristen-verjaehrung-klagefrist-fallkalender** — Fristen und Ausschlussrisiken im Versicherungsrecht: Fälligkeit, Hemmung, Verjährung, Obliegenheitsfristen, Nachprüfungs…
8. **eiopa-grenzueberschreitender-vertrieb** — Grenzüberschreitender Versicherungsvertrieb: Niederlassungs-/Dienstleistungsfreiheit, Host-/Home-Aufsicht, EIOPA, Passpo…
9. **vers-ombudsmann-versicherungsbetrug** — Eskalationsrouting im Versicherungsrecht: Versicherungsombudsmann, PKV-Ombudsmann, BaFin-Beschwerde, Deckungsklage, eins…
10. **vvg-gefahrerhoehung-mehrfachversicherung** — Gefahrerhöhung vor und nach Vertragsschluss: willentlich/unwillentlich, Anzeige, Kündigung, Leistungsfreiheit und Kausal…
11. **vag-bafin-aufsicht-beschwerde-missstand** — Versicherungsaufsicht nach VAG: BaFin-Beschwerde, Missstandsaufsicht, Produkt-/Vertriebsaufsicht, Solvabilität, Verbrauc…
12. **vers-kaltstart-routing** — Allgemeiner Einstieg ins Versicherungsrecht: Police, Bedingungen, Schadenereignis, Ablehnung, Fristen, Aufsicht, Ombudsm…
13. **lebensversicherung-bezugsrecht-widerruf-aenderung** — Bezugsrechte in Lebens- und Rentenversicherung: widerruflich/unwiderruflich, Scheidung, Erbfall, Sicherungsabtretung, In…
14. **reiseversicherung-ruecktritt-abbruch-krankheit** — Reiserücktritts- und Reiseabbruchversicherung: unerwartete schwere Erkrankung, Stornozeitpunkt, Attest, Vorerkrankung, P…
15. **vvg-anzeigepflicht-ruecktritt-arglist** — § 19 VVG in Leben, BU, PKV und Unfallversicherung: Gesundheitsfragen, Kenntnis, Kausalität, Rücktritt, Kündigung, Vertra…

---

## Skill: `rechtsabteilung-betriebsunterbrechung`

_Rechtsabteilungs-Fachmodul für Betriebsunterbrechung und Lieferkettenausfall: Unterbrechungsschaden, Trigger, Wartezeit und Mitwirkung werden beweisbar gemacht. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Versicherungsrecht._

# Rechtsabteilung: Betriebsunterbrechung und Lieferkettenausfall

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 VVG` — Versicherungsvertrag.
- `§ 19 VVG` — vorvertragliche Anzeigepflicht.
- `§ 28 VVG` — Obliegenheitsverletzung.
- `§ 86 VVG` — Legalzession.
- `§ 100 VVG` — Haftpflichtversicherung.
- `§ 115 VVG` — Direktanspruch.
- `§ 193 VVG` — Krankenversicherungspflicht.
- `§ 1 VAG` — Anwendungsbereich Versicherungsaufsicht.
- `§ 294 VAG` — Missstandsaufsicht.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialkern: Rechtsabteilung: Betriebsunterbrechung und Lieferkettenausfall

- **Konkretes Problem:** Unterbrechungsschaden, Trigger, Wartezeit und Mitwirkung werden beweisbar gemacht.
- **Norm-/Quellenanker:** einschlägige Spezialnormen des Plugin-Fachgebiets, amtliche Gesetzesfassungen, Behördenpraxis und verifizierte Rechtsprechung mit Datum und Aktenzeichen.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

VVG, AVB, Kausalitätsnachweis

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Unterbrechungsschaden, Trigger, Wartezeit und Mitwirkung werden beweisbar gemacht.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

---

## Skill: `rechtsabteilung-rechtsschutzversicherung-im-massenverfahren`

_Rechtsabteilungs-Fachmodul für Rechtsschutzversicherung im Massenverfahren: Deckungsanfrage, Stichentscheid und Erfolgsaussicht werden taktisch vorbereitet. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Versicherungsrecht._

# Rechtsabteilung: Rechtsschutzversicherung im Massenverfahren

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 VVG` — Versicherungsvertrag.
- `§ 19 VVG` — vorvertragliche Anzeigepflicht.
- `§ 28 VVG` — Obliegenheitsverletzung.
- `§ 86 VVG` — Legalzession.
- `§ 100 VVG` — Haftpflichtversicherung.
- `§ 115 VVG` — Direktanspruch.
- `§ 193 VVG` — Krankenversicherungspflicht.
- `§ 1 VAG` — Anwendungsbereich Versicherungsaufsicht.
- `§ 294 VAG` — Missstandsaufsicht.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialkern: Rechtsabteilung: Rechtsschutzversicherung im Massenverfahren

- **Konkretes Problem:** Deckungsanfrage, Stichentscheid und Erfolgsaussicht werden taktisch vorbereitet.
- **Norm-/Quellenanker:** einschlägige Spezialnormen des Plugin-Fachgebiets, amtliche Gesetzesfassungen, Behördenpraxis und verifizierte Rechtsprechung mit Datum und Aktenzeichen.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

VVG, ARB, BGH-Linie live prüfen

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Deckungsanfrage, Stichentscheid und Erfolgsaussicht werden taktisch vorbereitet.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

---

## Skill: `rechtsabteilung-d-umwelthaftpflicht`

_Rechtsabteilungs-Fachmodul für D&O-Deckung bei Organhaftung: Notification, Serienschaden, Selbstbehalt und Ausschlüsse werden für Vorstand/AR bewertet. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Versicherungsrecht._

# Rechtsabteilung: D&O-Deckung bei Organhaftung

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 VVG` — Versicherungsvertrag.
- `§ 19 VVG` — vorvertragliche Anzeigepflicht.
- `§ 28 VVG` — Obliegenheitsverletzung.
- `§ 86 VVG` — Legalzession.
- `§ 100 VVG` — Haftpflichtversicherung.
- `§ 115 VVG` — Direktanspruch.
- `§ 193 VVG` — Krankenversicherungspflicht.
- `§ 1 VAG` — Anwendungsbereich Versicherungsaufsicht.
- `§ 294 VAG` — Missstandsaufsicht.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialkern: Rechtsabteilung: D&O-Deckung bei Organhaftung

- **Konkretes Problem:** Notification, Serienschaden, Selbstbehalt und Ausschlüsse werden für Vorstand/AR bewertet.
- **Norm-/Quellenanker:** einschlägige Spezialnormen des Plugin-Fachgebiets, amtliche Gesetzesfassungen, Behördenpraxis und verifizierte Rechtsprechung mit Datum und Aktenzeichen.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

VVG, GmbHG § 43, AktG § 93, Claims-made-AVB

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Notification, Serienschaden, Selbstbehalt und Ausschlüsse werden für Vorstand/AR bewertet.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

---

## Skill: `rechtsabteilung-idd-vertrieb-und-provisionskonflikt`

_Rechtsabteilungs-Fachmodul für IDD-Vertrieb und Provisionskonflikt: Produktvertrieb wird auf Interessenkonflikte, Dokumentation und Aufsicht geprüft. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Versicherungsrecht._

# Rechtsabteilung: IDD-Vertrieb und Provisionskonflikt

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 VVG` — Versicherungsvertrag.
- `§ 19 VVG` — vorvertragliche Anzeigepflicht.
- `§ 28 VVG` — Obliegenheitsverletzung.
- `§ 86 VVG` — Legalzession.
- `§ 100 VVG` — Haftpflichtversicherung.
- `§ 115 VVG` — Direktanspruch.
- `§ 193 VVG` — Krankenversicherungspflicht.
- `§ 1 VAG` — Anwendungsbereich Versicherungsaufsicht.
- `§ 294 VAG` — Missstandsaufsicht.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialkern: Rechtsabteilung: IDD-Vertrieb und Provisionskonflikt

- **Konkretes Problem:** Produktvertrieb wird auf Interessenkonflikte, Dokumentation und Aufsicht geprüft.
- **Norm-/Quellenanker:** einschlägige Spezialnormen des Plugin-Fachgebiets, amtliche Gesetzesfassungen, Behördenpraxis und verifizierte Rechtsprechung mit Datum und Aktenzeichen.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

IDD, GewO § 34d, VVG Beratungsdokumentation

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Produktvertrieb wird auf Interessenkonflikte, Dokumentation und Aufsicht geprüft.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

---

## Skill: `rechtsabteilung-cyberversicherung-nach-ransomware`

_Rechtsabteilungs-Fachmodul für Cyberversicherung nach Ransomware: Deckung, Anzeige, Forensik und Lösegeldklauseln werden als Krisenfahrplan geprüft. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Versicherungsrecht._

# Rechtsabteilung: Cyberversicherung nach Ransomware

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 VVG` — Versicherungsvertrag.
- `§ 19 VVG` — vorvertragliche Anzeigepflicht.
- `§ 28 VVG` — Obliegenheitsverletzung.
- `§ 86 VVG` — Legalzession.
- `§ 100 VVG` — Haftpflichtversicherung.
- `§ 115 VVG` — Direktanspruch.
- `§ 193 VVG` — Krankenversicherungspflicht.
- `§ 1 VAG` — Anwendungsbereich Versicherungsaufsicht.
- `§ 294 VAG` — Missstandsaufsicht.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialkern: Rechtsabteilung: Cyberversicherung nach Ransomware

- **Konkretes Problem:** Deckung, Anzeige, Forensik und Lösegeldklauseln werden als Krisenfahrplan geprüft.
- **Norm-/Quellenanker:** einschlägige Spezialnormen des Plugin-Fachgebiets, amtliche Gesetzesfassungen, Behördenpraxis und verifizierte Rechtsprechung mit Datum und Aktenzeichen.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

VVG, AVB Cyber, Obliegenheiten, DSGVO/NIS2

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Deckung, Anzeige, Forensik und Lösegeldklauseln werden als Krisenfahrplan geprüft.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

---

## Skill: `vvg-versicherung-wohngebaeude-leitungswasser`

_Versicherung für fremde Rechnung: wer darf Leistung verlangen, wem stehen Einwendungen entgegen, welche Rolle haben Sicherungsnehmer, Leasinggeber, Mieter, Subunternehmer und Konzernunternehmen? im Versicherungsrecht._

# Versicherung für fremde Rechnung §§ 43–48 VVG

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 VVG` — Versicherungsvertrag.
- `§ 19 VVG` — vorvertragliche Anzeigepflicht.
- `§ 28 VVG` — Obliegenheitsverletzung.
- `§ 86 VVG` — Legalzession.
- `§ 100 VVG` — Haftpflichtversicherung.
- `§ 115 VVG` — Direktanspruch.
- `§ 193 VVG` — Krankenversicherungspflicht.
- `§ 1 VAG` — Anwendungsbereich Versicherungsaufsicht.
- `§ 294 VAG` — Missstandsaufsicht.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
VVG §§ 43–48, 44, 45; BGB Abtretung/Einziehung; ZPO Prozessführungsbefugnis.

## Red Flags

- Leasingobjekt beschädigt
- Bank als Sicherungsnehmer
- Konzernpolice mit Tochtergesellschaft
- versicherte Person will direkt klagen

## Anschluss-Skills

- transportversicherung-ware-lagerung
- direktanspruch-pflichtversicherung-115-vvg

---

## Skill: `vers-fristen-verjaehrung-klagefrist-fallkalender`

_Fristen und Ausschlussrisiken im Versicherungsrecht: Fälligkeit, Hemmung, Verjährung, Obliegenheitsfristen, Nachprüfungsfristen, Gutachtenfristen und prozessuale Termine sicher verwalten im Versicherungsrecht._

# Fristenkalender für Versicherungsfälle

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 VVG` — Versicherungsvertrag.
- `§ 19 VVG` — vorvertragliche Anzeigepflicht.
- `§ 28 VVG` — Obliegenheitsverletzung.
- `§ 86 VVG` — Legalzession.
- `§ 100 VVG` — Haftpflichtversicherung.
- `§ 115 VVG` — Direktanspruch.
- `§ 193 VVG` — Krankenversicherungspflicht.
- `§ 1 VAG` — Anwendungsbereich Versicherungsaufsicht.
- `§ 294 VAG` — Missstandsaufsicht.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
VVG §§ 14, 15, 28, 31, 215; BGB §§ 195, 199, 203, 204; ZPO; spartenspezifische AVB-Fristen.

## Red Flags

- Ablehnung liegt Monate zurück
- Verhandlungen nur telefonisch
- Invalidität oder Berufsunfähigkeit nicht fristgerecht substantiiert
- Ombudsmann als Hemmung überschätzt

## Anschluss-Skills

- deckungsprozess-zuständigkeit-215-vvg
- unfallversicherung-invaliditaet-fristen-gliedertaxe

---

## Skill: `eiopa-grenzueberschreitender-vertrieb`

_Grenzüberschreitender Versicherungsvertrieb: Niederlassungs-/Dienstleistungsfreiheit, Host-/Home-Aufsicht, EIOPA, Passporting, Verbraucherbeschwerden und Sprach-/Informationspflichten im Versicherungsrecht._

# EIOPA und grenzüberschreitender Versicherungsvertrieb

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 VVG` — Versicherungsvertrag.
- `§ 19 VVG` — vorvertragliche Anzeigepflicht.
- `§ 28 VVG` — Obliegenheitsverletzung.
- `§ 86 VVG` — Legalzession.
- `§ 100 VVG` — Haftpflichtversicherung.
- `§ 115 VVG` — Direktanspruch.
- `§ 193 VVG` — Krankenversicherungspflicht.
- `§ 1 VAG` — Anwendungsbereich Versicherungsaufsicht.
- `§ 294 VAG` — Missstandsaufsicht.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
VAG; IDD; Solvency II; EIOPA-Veröffentlichungen live prüfen; Rom-I/Brüssel-Ia bei Vertrag und Gerichtsstand.

## Red Flags

- ausländische Aufsicht als BaFin-Ersatz missverstanden
- Gerichtsstandsklausel gegenüber Verbrauchern unwirksam
- Pflichtinformationen nur englisch
- Passporting nicht geprüft

## Anschluss-Skills

- vag-bafin-aufsicht-beschwerde-missstand
- deckungsprozess-zuständigkeit-215-vvg

---

## Skill: `vers-ombudsmann-versicherungsbetrug`

_Eskalationsrouting im Versicherungsrecht: Versicherungsombudsmann, PKV-Ombudsmann, BaFin-Beschwerde, Deckungsklage, einstweiliger Rechtsschutz und Vergleichsdruck sauber unterscheiden im Versicherungsrecht._

# Ombudsmann, BaFin-Beschwerde oder Klage?

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 VVG` — Versicherungsvertrag.
- `§ 19 VVG` — vorvertragliche Anzeigepflicht.
- `§ 28 VVG` — Obliegenheitsverletzung.
- `§ 86 VVG` — Legalzession.
- `§ 100 VVG` — Haftpflichtversicherung.
- `§ 115 VVG` — Direktanspruch.
- `§ 193 VVG` — Krankenversicherungspflicht.
- `§ 1 VAG` — Anwendungsbereich Versicherungsaufsicht.
- `§ 294 VAG` — Missstandsaufsicht.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
VVG §§ 214 ff., § 215; VAG Aufsicht; ZPO; Ombudsmann-Verfahrensordnungen live prüfen; BaFin-Verbraucherbeschwerde.

## Red Flags

- BaFin als Leistungsgericht missverstanden
- Ombudsmann bei hohem Streitwert ungeeignet
- Klagefrist/Verjährung läuft parallel
- PKV-Ombudsmann und Versicherungsombudsmann verwechselt

## Anschluss-Skills

- deckungsprozess-zuständigkeit-215-vvg
- rechtsschutz-deckungszusage-stichentscheid

---

## Skill: `vvg-gefahrerhoehung-mehrfachversicherung`

_Gefahrerhöhung vor und nach Vertragsschluss: willentlich/unwillentlich, Anzeige, Kündigung, Leistungsfreiheit und Kausalitätsprüfung in Sach-, Haftpflicht- und Personenversicherungen im Versicherungsrecht._

# Gefahrerhöhung §§ 23–27 VVG

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 VVG` — Versicherungsvertrag.
- `§ 19 VVG` — vorvertragliche Anzeigepflicht.
- `§ 28 VVG` — Obliegenheitsverletzung.
- `§ 86 VVG` — Legalzession.
- `§ 100 VVG` — Haftpflichtversicherung.
- `§ 115 VVG` — Direktanspruch.
- `§ 193 VVG` — Krankenversicherungspflicht.
- `§ 1 VAG` — Anwendungsbereich Versicherungsaufsicht.
- `§ 294 VAG` — Missstandsaufsicht.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
VVG §§ 23–27, 81; BGB §§ 133, 157; AVB.

## Red Flags

- bloße Wertsteigerung als Gefahrerhöhung verkauft
- Nutzungsänderung nicht kausal
- Versicherer kannte die Änderung
- AVB verschieben gesetzliche Wertungen unangemessen

## Anschluss-Skills

- wohngebaeude-leitungswasser-sturm-hagel-brand
- kfz-kasko-grobe-fahrlaessigkeit-entwendung

---

## Skill: `vag-bafin-aufsicht-beschwerde-missstand`

_Versicherungsaufsicht nach VAG: BaFin-Beschwerde, Missstandsaufsicht, Produkt-/Vertriebsaufsicht, Solvabilität, Verbraucherschutz und Grenzen individueller Leistungserzwingung im Versicherungsrecht._

# VAG/BaFin-Aufsicht: Beschwerde und Missstand

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 VVG` — Versicherungsvertrag.
- `§ 19 VVG` — vorvertragliche Anzeigepflicht.
- `§ 28 VVG` — Obliegenheitsverletzung.
- `§ 86 VVG` — Legalzession.
- `§ 100 VVG` — Haftpflichtversicherung.
- `§ 115 VVG` — Direktanspruch.
- `§ 193 VVG` — Krankenversicherungspflicht.
- `§ 1 VAG` — Anwendungsbereich Versicherungsaufsicht.
- `§ 294 VAG` — Missstandsaufsicht.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
VAG; BaFin-Aufsichtsrecht; VVG §§ 214 ff.; EU Solvency II/IDD; VwVfG/VwGO nur falls eigener Verwaltungsakt.

## Red Flags

- BaFin soll Einzelfallzahlung anordnen
- Datenschutz/Geschäftsgeheimnisse unnötig breit eingereicht
- Verjährung parallel unbeachtet
- Beschwerde emotional statt prüfbar

## Anschluss-Skills

- vers-ombudsmann-bafin-beschwerde-klageweg
- idd-vertrieb-beratung-dokumentation

---

## Skill: `vers-kaltstart-routing`

_Allgemeiner Einstieg ins Versicherungsrecht: Police, Bedingungen, Schadenereignis, Ablehnung, Fristen, Aufsicht, Ombudsmann und Klageweg strukturiert erfassen und passende Fachmodule vorschlagen._

# Versicherungsrecht: Kaltstart, Rollenklärung und Triage

## Aktenstart statt Formularstart

Wenn zu **Vers Kaltstart Routing** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Versicherungsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 VVG` — Versicherungsvertrag.
- `§ 19 VVG` — vorvertragliche Anzeigepflicht.
- `§ 28 VVG` — Obliegenheitsverletzung.
- `§ 86 VVG` — Legalzession.
- `§ 100 VVG` — Haftpflichtversicherung.
- `§ 115 VVG` — Direktanspruch.
- `§ 193 VVG` — Krankenversicherungspflicht.
- `§ 1 VAG` — Anwendungsbereich Versicherungsaufsicht.
- `§ 294 VAG` — Missstandsaufsicht.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
VVG §§ 1, 6, 14, 15, 19, 28, 86, 115, 125–129, 150 ff., 172 ff., 192 ff., 215; VAG; BGB; ZPO; DSGVO; BaFin- und Ombudsmannwege.

## Red Flags

- AVB-Fassung ungeklärt
- Ablehnung ohne vollständige Begründung
- Frist- oder Ausschlussklausel im Kleingedruckten
- Gesundheitsdaten ohne saubere Einwilligungs-/Schweigepflichtentbindung

## Anschluss-Skills

- vvg-anzeigepflicht-19-ruecktritt-kuendigung-anpassung
- vvg-obliegenheit-28-quotelung-kausalitaet
- deckungsprozess-zuständigkeit-215-vvg

---

## Skill: `lebensversicherung-bezugsrecht-widerruf-aenderung`

_Bezugsrechte in Lebens- und Rentenversicherung: widerruflich/unwiderruflich, Scheidung, Erbfall, Sicherungsabtretung, Insolvenz, Änderungserklärung und Auszahlungsstreit im Versicherungsrecht._

# Lebensversicherung: Bezugsrecht, Widerruf, Änderung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 VVG` — Versicherungsvertrag.
- `§ 19 VVG` — vorvertragliche Anzeigepflicht.
- `§ 28 VVG` — Obliegenheitsverletzung.
- `§ 86 VVG` — Legalzession.
- `§ 100 VVG` — Haftpflichtversicherung.
- `§ 115 VVG` — Direktanspruch.
- `§ 193 VVG` — Krankenversicherungspflicht.
- `§ 1 VAG` — Anwendungsbereich Versicherungsaufsicht.
- `§ 294 VAG` — Missstandsaufsicht.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
VVG §§ 150–171, besonders §§ 159, 160; BGB Erbrecht/Abtretung; InsO; FamFG/Nachlass.

## Red Flags

- alte Ehegattenbezeichnung
- Sicherungsabtretung an Bank
- Erben verwechseln Nachlass und Bezugsrecht
- unwirksame Änderung kurz vor Tod

## Anschluss-Skills

- lebensversicherung-rueckkaufswert-abschlusskosten-widerspruch
- subrogation-regress-86-vvg

---

## Skill: `reiseversicherung-ruecktritt-abbruch-krankheit`

_Reiserücktritts- und Reiseabbruchversicherung: unerwartete schwere Erkrankung, Stornozeitpunkt, Attest, Vorerkrankung, Pandemie, Angehörige und Kreditkartenversicherung im Versicherungsrecht._

# Reiseversicherung: Rücktritt, Abbruch, Krankheit

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 VVG` — Versicherungsvertrag.
- `§ 19 VVG` — vorvertragliche Anzeigepflicht.
- `§ 28 VVG` — Obliegenheitsverletzung.
- `§ 86 VVG` — Legalzession.
- `§ 100 VVG` — Haftpflichtversicherung.
- `§ 115 VVG` — Direktanspruch.
- `§ 193 VVG` — Krankenversicherungspflicht.
- `§ 1 VAG` — Anwendungsbereich Versicherungsaufsicht.
- `§ 294 VAG` — Missstandsaufsicht.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
VVG allgemein; AVB Reise; BGB Reisevertragsrecht §§ 651a ff.; Datenschutz Gesundheitsdaten.

## Red Flags

- Attest zu pauschal
- Storno zu spät
- Vorerkrankung als Ausschluss behauptet
- Kreditkartenversicherung mit Reiseveranstalter verwechselt

## Anschluss-Skills

- datenschutz-schweigepflicht-gesundheitsdaten
- vers-fristen-verjaehrung-klagefrist-fallkalender

---

## Skill: `vvg-anzeigepflicht-ruecktritt-arglist`

_§ 19 VVG in Leben, BU, PKV und Unfallversicherung: Gesundheitsfragen, Kenntnis, Kausalität, Rücktritt, Kündigung, Vertragsanpassung, Arglist und Belehrungsfehler prüfen im Versicherungsrecht._

# Vorvertragliche Anzeigepflicht § 19 VVG

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Norm- und Quellenanker

VVG §§ 19–22, 194; BGB § 123; AVB; DSGVO/Gesundheitsdaten; ZPO Beweislast.

## Red Flags

- Versicherer springt sofort zu Arglist
- Gesundheitsfrage zu weit oder mehrdeutig
- Maklernotiz widerspricht Antrag
- Kausalität zwischen Anzeigeverstoß und Schaden unklar

## Anschluss-Skills

- vvg-arglist-taeuschung-anfechtung
- bu-berufsbild-50-prozent-substantiierung

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

