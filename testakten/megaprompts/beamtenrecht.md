# Megaprompt: beamtenrecht

> *Achtung: Dies ist ein experimentelles Mega-Prompt-Markdown, das einen kompletten Klotzkette-Plugin in eine einzige Datei zusammenfuehrt. Keine Haftung, keine Gewaehr. Nur zum Ausprobieren der Skills auch ohne Claude Code; keine Rechtsberatung. Vor Verwendung im Mandat anwaltlich pruefen.*
>
> *Caution: This is an experimental Mega-Prompt Markdown that consolidates a full Klotzkette plugin into a single file. No warranty, no liability. For exploration with chat tools that do not run Claude Code only; not legal advice.*

**Verwendung:** Diesen gesamten Text in einen Chat ohne Claude-Code-Integration einfuegen (oder als Datei hochladen). Der Chat-Agent erhaelt damit die gebuendelten Skills dieses Plugins als Kontext. Eine Replikation des vollen Plugin-Verhaltens ist nicht garantiert — der Megaprompt ist eine Best-Effort-Kompression.


## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 157 Skills des Plugins `beamtenrecht`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Einstieg, Kaltstart und Fallrouting im Beamtenrecht-Plugin: klärt Status, Dienstherr, Bundesland, Frist, Ziel, Unterlage…
2. **agg-vs-9-bbg-auswahlverfahren** — Skill zum Verhaeltnis von AGG-Diskriminierungsschutz und beamtenrechtlichem Bewerbungsverfahrensanspruch nach § 9 BBG bz…
3. **altersteilzeit-93-bbg-blockmodell** — Skill zur Altersteilzeit der Beamten nach § 93 BBG bzw. § 9 BeamtStG i.V.m. den Landesregelungen. Klaert die zwei Modell…
4. **amtsangemessene-alimentation-bverfg** — Skill zur Pruefung der amtsangemessenen Alimentation der Beamten Richter und Soldaten nach Art. 33 Abs. 5 GG. Skill arbe…
5. **anforderungsprofil-konstitutiv** — Skill zur Unterscheidung konstitutives Anforderungsprofil und deklaratorisches Anforderungsprofil bei der beamtenrechtli…
6. **anlassbeurteilung-vs-regelbeurteilung** — Klaert das Verhaeltnis von Regelbeurteilung und Anlassbeurteilung im Auswahlverfahren des öffentlichen Dienstes. Skill p…
7. **anrechnung-55-beamtvg-mehrere-renten** — Skill zur Anrechnungsregelung von Renten auf die Beamtenversorgung nach § 55 BeamtVG. Klaert das Zusammenwirken der Beam…
8. **auslandsdienstbezuege-bbesg** — Skill zu Auslandsdienstbezuegen im Auswaertigen Dienst und in der Auslandsverwendung. Klaert Auslandszuschlag Kaufkrafta…
9. **auswahlgespraech-dokumentationspflicht** — Skill zu Anforderungen an strukturierte Auswahlgespraeche und Assessment Center im beamtenrechtlichen Auswahlverfahren. …
10. **begrenzte-dienstfaehigkeit-27-bbg** — Skill zur begrenzten Dienstfaehigkeit nach § 27 BBG bzw. § 27 BeamtStG. Klaert die Voraussetzungen für die Reduzierung d…
11. **beihilfe-chronische-krankheit** — Skill zur Beihilfe bei schwerer chronischer Krankheit nach den Beihilfeverordnungen des Bundes und der Länder. Klaert De…
12. **beihilfe-heilbehandlung-ausland** — Skill zur beamtenrechtlichen Beihilfefaehigkeit von Heilbehandlung im Ausland nach BBhV und den Landesbeihilfeverordnung…
13. **beihilfe-implantatfaehige-hoergeraete** — Skill zur Beihilfefaehigkeit von hochwertigen Hilfsmitteln wie implantatfaehigen Hoergeraeten Cochlea-Implantaten elektr…
14. **besoldung-verfassungswidrig-a-besoldung** — Skill zur Geltendmachung verfassungswidriger A-Besoldung im Land. Pruefschema für den Verstoss gegen die amtsangemessene…
15. **beurteilungsbeitrag-heilung-maengel** — Skill zur rechtlichen Pruefung von Beurteilungsbeitraegen Dritter im beamtenrechtlichen Beurteilungsverfahren. Klaert we…

---

## Skill: `kaltstart-triage`

_Einstieg, Kaltstart und Fallrouting im Beamtenrecht-Plugin: klärt Status, Dienstherr, Bundesland, Frist, Ziel, Unterlagen, Anfänger-/Profi-Modus und schlägt passende Fachmodule vor._

# Allgemein

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Beamtenrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Pflichtfragen

- Welcher Status liegt vor: Beamter, Richter, Bewerber, Anwärter, Tarifbeschäftigter, Wahlbeamter oder Mischfall?
- Welcher Dienstherr und welches Bundesland sind betroffen?
- Gibt es einen Bescheid, eine Beurteilung, eine Ausschreibung, einen Auswahlvermerk oder eine Verfügung mit Datum und Zugang?
- Welche Frist läuft und welches Ergebnis soll erreicht werden?
- Welche Unterlagen fehlen noch: Personalakte, Beurteilungsbeiträge, amtsärztliches Gutachten, Berechnungsblatt, Beteiligungsvermerk, Versorgungsauskunft, Beihilfebescheid, PKV-Schreiben, Auswahlvermerk?

## Prüfprogramm

1. **Status und Rechtsquelle:** Bundesrecht, Landesrecht oder Richterrecht trennen; Normen live gegen amtliche Quellen prüfen.
2. **Eingriff und Ziel:** Verwaltungsakt, dienstliche Weisung, Auswahlentscheidung, Realakt oder bloße Kommunikation einordnen.
3. **Materielle Prüfung:** Tatbestand, Ermessen, Beteiligung, Begründung, Gleichbehandlung, Fürsorge und Verhältnismäßigkeit prüfen.
4. **Verfahren:** Anhörung, Akteneinsicht, Frist, Widerspruch, Klageart, Eilrechtsschutz und Glaubhaftmachung klären.
5. **Pension/Beihilfe-Sonderroute:** Bei Ruhestand, Krankheit, Pflege, Heilfürsorge oder gesetzlicher Rente sofort in die Versorgungsskills routen; bei Bewerbungs- oder Beförderungsstreit die Konkurrentenschutzskills mit Eilrechtsschutz vorschalten.
6. **Output:** Eine klare Handlungsempfehlung, einen Entwurf oder eine Risikomatrix erzeugen.

## Erweiterte Spezialrouten

- **Pension und Versorgung:** `pensionierung-gesamtcheck-ruhegehalt-beihilfe-pkv`, `versorgungsakte-dokumentenintake-und-berechnung`, `pension-und-gesetzliche-rente-55-beamtvg`.
- **Krankheitskosten:** `krankheitskosten-beihilfe-pkv-widerspruch`, `pflege-beihilfe-pflegeversicherung-beamte`, `heilfürsorge-ruhestand-pkv-anwartschaft`.
- **Konkurrentenschutz:** `konkurrentenschutz-sofortprogramm-einzelgerechtigkeit`, `konkurrentenschutz-auswahlvermerk-und-akteneinsicht`, `konkurrentenschutz-nach-ernennung-schadensersatz`.

---

## Skill: `agg-vs-9-bbg-auswahlverfahren`

_Skill zum Verhaeltnis von AGG-Diskriminierungsschutz und beamtenrechtlichem Bewerbungsverfahrensanspruch nach § 9 BBG bzw. § 9 BeamtStG. Klaert Anwendbarkeit der AGG-Vorschriften auf Auswahlverfahren der öffentlichen Hand Beweislastregeln Anhörung und Anspruchskonkurrenz zum bewerbungsverfahrensr..._

# AGG und § 9 BBG — Anspruchskonkurrenz im Auswahlverfahren

## Arbeitsbereich

Skill zum Verhaeltnis von AGG-Diskriminierungsschutz und beamtenrechtlichem Bewerbungsverfahrensanspruch nach § 9 BBG bzw. § 9 BeamtStG. Klaert Anwendbarkeit der AGG-Vorschriften auf Auswahlverfahren der öffentlichen Hand Beweislastregeln Anhörung und Anspruchskonkurrenz zum bewerbungsverfahrensrechtlichen Anspruch nach Art. 33 II GG. Behandelt typische Diskriminierungsmerkmale Alter Geschlecht Behinderung Religion ethnische Herkunft. Liefert Pruefraster und Schriftsatzbausteine. Verweist auf schwerbehinderte-bewerber-165-sgb-9. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: Widerspruch 1 Monat (VwGO § 70), Disziplinarverfahren nach BDG, Beihilfeantrag i.d.R. 1 Jahr, Beförderung-Auswahlentscheidung Bewährungsfristen.
- Tragende Normen verifizieren: BeamtStG §§ 3, 4, 21-25, 30, 33-41, BBG, BBesG, BeamtVG, LBG der Länder, GG Art. 33 Abs. 4 und 5, BDG, LDG, VwGO §§ 126 ff., LPVG/BPersVG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Dienstherr (Bund/Land/Kommune), Beamter, Dienstvorgesetzter, Personalrat, Personalvertretung, Disziplinarvorgesetzter, VG, OVG, BVerwG (2. Senat).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Ernennungsurkunde, dienstliche Beurteilung, Konkurrentenklage, Disziplinarverfügung, Versorgungsbescheid, Beihilfeantrag, Personalratsentscheidung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## 1. Zweck und Anwendungsfall

Skill für Mandanten, die im beamtenrechtlichen Auswahlverfahren wegen eines Merkmals des § 1 AGG (Alter, Geschlecht, Behinderung, ethnische Herkunft, Religion, Weltanschauung, sexuelle Identitaet) benachteiligt wurden. Klaert das Zusammenspiel der AGG-Ansprueche mit dem allgemeinen bewerbungsverfahrensrechtlichen Anspruch nach Art. 33 Abs. 2 GG / § 9 BBG.

## 2. Eingaben

- Stellenausschreibung
- Auswahlvermerk und Konkurrentenmitteilung
- Indizien für Diskriminierung (Aeusserungen im Gespraech, Altersgrenzen, geschlechtsbezogene Beurteilungsmaszstaebe)
- Geschlecht, Alter, ggf. Behinderungsstatus des Mandanten

## 3. Ablauf / Checkliste

### a) Anwendbarkeit AGG auf Beamtenverhaeltnisse
- § 24 AGG erstreckt das AGG auf Beamtinnen und Beamte mit Modifikationen.
- AGG findet auch auf Bewerbungsverfahren Anwendung (§ 6 Abs. 1 Satz 2 AGG).

### b) Verhaeltnis zum bewerbungsverfahrensrechtlichen Anspruch
- AGG-Ansprueche stehen neben dem Anspruch aus Art. 33 Abs. 2 GG. Sie schliessen einander nicht aus.
- AGG zielt auf Entschaedigung in Geld; bewerbungsverfahrensrechtlicher Anspruch zielt auf Neuauswahl und gegebenenfalls Schadensersatz.

### c) Beweislast
- § 22 AGG: Indizienbeweis genuegt; der Dienstherr muss bei Indizien beweisen, dass kein Verstoss vorlag.
- Indizien koennen sein: diskriminierende Formulierungen in Stellenausschreibung, statistische Schieflage, Aeusserungen im Auswahlgespraech.

### d) Frist
- Geltendmachung der AGG-Entschaedigung innerhalb von zwei Monaten ab Kenntnis der Benachteiligung (§ 15 Abs. 4 AGG).
- Klagefrist drei Monate ab schriftlicher Geltendmachung (§ 61b ArbGG analog beziehungsweise § 74 VwGO im VerwR).

### e) Rechtsweg
- Verwaltungsgerichte zuständig (§ 40 VwGO). Bei statusrechtlich Beschaeftigten unter AGG ist § 24 AGG zu beachten.

## 4. Quellenpflicht

- Normen: §§ 1, 6, 15, 22, 24 AGG; Art. 33 Abs. 2 GG; § 9 BBG; § 9 BeamtStG; § 40 VwGO.
- EuGH zu Anti-Diskriminierungsrichtlinien (Rahmenrichtlinie und allgemeine Gleichbehandlungsrichtlinie) — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- BVerwG zu Auswahlverfahren und Diskriminierung — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Entschaedigungsschreiben mit Indiziendarstellung.
- Pruefraster Diskriminierungsmerkmale.
- Klageentwurf VG mit Antrag auf Entschaedigung und Neuauswahl.

## 6. Verifizierte Quellenanker

- Art. 33 Abs. 2 GG: Bestenauslese nach Eignung, Befähigung und fachlicher Leistung.
- Art. 74 Abs. 1 Nr. 27 GG und Art. 70 GG: Statusrechtliche Bundeskompetenz, Laufbahn/Besoldung/Versorgung der Länder grundsätzlich Landesrecht.
- BeamtStG und BBG immer nach Dienstherr trennen; Landesbeamtengesetz und Beurteilungsrichtlinien live prüfen.
- BVerwG, 11.10.2016 - 2 C 11.15 als verifizierter Anker zu Art. 33 Abs. 2 GG und Eignungsanforderungen bei Höchstaltersgrenzen.
- Für Spezialfragen der dienstlichen Beurteilung, Anlassbeurteilung, Binnendifferenzierung und Auswahlgespräch keine privaten Datenbankzitate verwenden; konkrete Rechtsprechung nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.

## 7. Beispiel (Kurzfassung)

Bewerberin 54 Jahre, für Stelle "wuenschenswert junges Team" Konkurrenz mit 28-jaehriger Mitbewerberin. Skill liefert Indizienliste für Altersdiskriminierung, AGG-Entschaedigungsforderung und parallel Konkurrenteneilantrag.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 33 GG (hergebrachte Grundsätze des Berufsbeamtentums)
- §§ 7, 8 BeamtStG / § 12 BBG (Ernennung, Voraussetzungen)
- § 31 BeamtStG / § 28 BBG (Probezeit)
- §§ 33-37 BeamtStG (Grundpflichten)
- §§ 47 ff. BeamtStG, BDG (Dienstvergehen, Disziplinarverfahren)
- BBesG (Besoldung)
- BeamtVG (Versorgung)
- § 78 BBG (Fürsorgepflicht)
- VwGO §§ 42, 75, 113 (Verpflichtungsklage, Untätigkeit)
- BLV (Laufbahnverordnung)

### Leitentscheidungen

- BVerfG 2 BvR 1738/12 (Beamtenstreikverbot)
- BVerwG 2 C 32.10 (amtsangemessene Alimentation)
- BVerfG 2 BvL 4/18 (Richterbesoldung)
- BVerwG 2 C 33.20 (Disziplinarmaßnahme Verhältnismäßigkeit)
- BVerwG 2 C 4.18 (Konkurrentenstreitverfahren)

### Anwendung im Skill

- Amtsangemessene Alimentation nach BVerfG 2 BvL 4/18 als verfassungsrechtlicher Mindeststandard.
- Disziplinarmassnahme nach BDG/LDG am Verhaeltnismaessigkeitsgrundsatz messen; Entfernung erfordert schwere Verfehlung.
- Konkurrentenstreitverfahren BVerwG 2 C 4.18: Bewerbungsverfahrensanspruch Art. 33 Abs. 2 GG sichern, vor Ernennung.

---

## Skill: `altersteilzeit-93-bbg-blockmodell`

_Skill zur Altersteilzeit der Beamten nach § 93 BBG bzw. § 9 BeamtStG i.V.m. den Landesregelungen. Klaert die zwei Modelle Teilzeitmodell und Blockmodell die Bezuegehoehe waehrend Aktiv- und Freistellungsphase die Auswirkungen auf das Ruhegehalt und auf den Versorgungsabschlag nach § 14 BeamtVG. B..._

# Altersteilzeit § 93 BBG — Blockmodell und Teilzeitmodell

## Arbeitsbereich

Skill zur Altersteilzeit der Beamten nach § 93 BBG bzw. § 9 BeamtStG i.V.m. den Landesregelungen. Klaert die zwei Modelle Teilzeitmodell und Blockmodell die Bezuegehoehe waehrend Aktiv- und Freistellungsphase die Auswirkungen auf das Ruhegehalt und auf den Versorgungsabschlag nach § 14 BeamtVG. Behandelt die Konstellation Hinausschiebung der Altersgrenze parallele Schwerbehinderung und teilweise Dienstunfaehigkeit waehrend der Altersteilzeit. Liefert Berechnungstabelle und Beratungsraster. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: Widerspruch 1 Monat (VwGO § 70), Disziplinarverfahren nach BDG, Beihilfeantrag i.d.R. 1 Jahr, Beförderung-Auswahlentscheidung Bewährungsfristen.
- Tragende Normen verifizieren: BeamtStG §§ 3, 4, 21-25, 30, 33-41, BBG, BBesG, BeamtVG, LBG der Länder, GG Art. 33 Abs. 4 und 5, BDG, LDG, VwGO §§ 126 ff., LPVG/BPersVG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Dienstherr (Bund/Land/Kommune), Beamter, Dienstvorgesetzter, Personalrat, Personalvertretung, Disziplinarvorgesetzter, VG, OVG, BVerwG (2. Senat).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Ernennungsurkunde, dienstliche Beurteilung, Konkurrentenklage, Disziplinarverfügung, Versorgungsbescheid, Beihilfeantrag, Personalratsentscheidung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## 1. Zweck und Anwendungsfall

Skill für Beamte ab dem 55. Lebensjahr, die ueber Altersteilzeit den gleitenden Uebergang in den Ruhestand wuenschen.

## 2. Eingaben

- Geburtsdatum
- Statusamt und Besoldungsgruppe
- Vorgesehene Modellwahl
- Restdienstzeit bis Regelaltersgrenze
- Schwerbehindertenstatus

## 3. Ablauf / Checkliste

### a) Voraussetzungen
- § 93 BBG (Bund); für Länder entsprechende Vorschriften.
- Mindestalter und Mindestbeschaeftigungsdauer, dienstliche Belange nicht entgegenstehend.

### b) Modelle
- Teilzeitmodell: gleichmäßige Reduzierung der Arbeitszeit ueber die gesamte Altersteilzeit.
- Blockmodell: Arbeitsphase mit voller Arbeitszeit und anschliessende Freistellungsphase.

### c) Bezuege
- Bezuege betragen in der Regel 80 v. H. der Bezuege der entsprechenden Vollzeitbeschaeftigung (Altersteilzeitzuschlag).
- Auswirkungen auf Beihilfe und Heilfürsorge pruefen.

### d) Ruhegehaltfaehigkeit
- Altersteilzeit ist anteilig ruhegehaltfaehig.

### e) Versorgungsabschlag
- Beim Eintritt in den Ruhestand nach Altersteilzeit kein Versorgungsabschlag, soweit die Altersteilzeit bis zur Regelaltersgrenze laeuft. Bei vorzeitigem Antragsruhestand greift Skill `versorgungsabschlag-14-beamtvg`.

### f) Aenderungen waehrend der Altersteilzeit
- Bei eintretender Dienstunfaehigkeit gelten Sondervorschriften zur Beendigung der Altersteilzeit; Restbezuege und Versorgung sind zu bemessen.

## 4. Quellenpflicht

- Normen: § 93 BBG; § 9 BeamtStG i.V.m. Landesrecht; § 6 BeamtVG; § 14 BeamtVG.
- Rspr.: BVerwG zu Altersteilzeit — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Berechnungstabelle Bezuege und Versorgung mit und ohne Altersteilzeit.
- Antrag auf Altersteilzeit.

## 6. Verifizierte Quellenanker

- § 93 BBG (Altersteilzeit Bund) i.V.m. § 9 ArbZV (Arbeitszeitverordnung); landesrechtliche Altersteilzeitvorschriften (BeamtStG enthaelt keine Altersteilzeitnorm; die Länder regeln Altersteilzeit eigenstaendig in ihren Landesbeamtengesetzen).
- § 6 BeamtVG (ruhegehaltfaehige Dienstzeit Altersteilzeit); § 14 BeamtVG (Versorgungsabschlag).
- Altersteilzeitzuschlagsverordnung Bund und landesrechtliche Aequivalente.
- BVerwG zur Altersteilzeit der Beamten — Datum und Az vor Zitat live verifizieren.

## 7. Beispiel (Kurzfassung)

Mandant 57 Jahre, will sechs Jahre Altersteilzeit im Blockmodell (drei Jahre Aktiv, drei Jahre Freistellung). Skill liefert Berechnung Bezuege und Versorgung.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 33 GG (hergebrachte Grundsätze des Berufsbeamtentums)
- §§ 7, 8 BeamtStG / § 12 BBG (Ernennung, Voraussetzungen)
- § 31 BeamtStG / § 28 BBG (Probezeit)
- §§ 33-37 BeamtStG (Grundpflichten)
- §§ 47 ff. BeamtStG, BDG (Dienstvergehen, Disziplinarverfahren)
- BBesG (Besoldung)
- BeamtVG (Versorgung)
- § 78 BBG (Fürsorgepflicht)
- VwGO §§ 42, 75, 113 (Verpflichtungsklage, Untätigkeit)
- BLV (Laufbahnverordnung)

### Leitentscheidungen

- BVerfG 2 BvR 1738/12 (Beamtenstreikverbot)
- BVerwG 2 C 32.10 (amtsangemessene Alimentation)
- BVerfG 2 BvL 4/18 (Richterbesoldung)
- BVerwG 2 C 33.20 (Disziplinarmaßnahme Verhältnismäßigkeit)
- BVerwG 2 C 4.18 (Konkurrentenstreitverfahren)

### Anwendung im Skill

- Amtsangemessene Alimentation nach BVerfG 2 BvL 4/18 als verfassungsrechtlicher Mindeststandard.
- Disziplinarmassnahme nach BDG/LDG am Verhaeltnismaessigkeitsgrundsatz messen; Entfernung erfordert schwere Verfehlung.
- Konkurrentenstreitverfahren BVerwG 2 C 4.18: Bewerbungsverfahrensanspruch Art. 33 Abs. 2 GG sichern, vor Ernennung.

---

## Skill: `amtsangemessene-alimentation-bverfg`

_Skill zur Pruefung der amtsangemessenen Alimentation der Beamten Richter und Soldaten nach Art. 33 Abs. 5 GG. Skill arbeitet das fuenfstufige Pruefungsschema des BVerfG ab mit den Indikatoren Tarifabstand Preisentwicklung Versorgungsempfaenger Vergleich zu anderen Besoldungsgruppen Familienzuschl..._

# Amtsangemessene Alimentation — Pruefschema BVerfG

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: Widerspruch 1 Monat (VwGO § 70), Disziplinarverfahren nach BDG, Beihilfeantrag i.d.R. 1 Jahr, Beförderung-Auswahlentscheidung Bewährungsfristen.
- Tragende Normen verifizieren: BeamtStG §§ 3, 4, 21-25, 30, 33-41, BBG, BBesG, BeamtVG, LBG der Länder, GG Art. 33 Abs. 4 und 5, BDG, LDG, VwGO §§ 126 ff., LPVG/BPersVG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Dienstherr (Bund/Land/Kommune), Beamter, Dienstvorgesetzter, Personalrat, Personalvertretung, Disziplinarvorgesetzter, VG, OVG, BVerwG (2. Senat).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Ernennungsurkunde, dienstliche Beurteilung, Konkurrentenklage, Disziplinarverfügung, Versorgungsbescheid, Beihilfeantrag, Personalratsentscheidung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## 1. Zweck und Anwendungsfall

Skill zur Pruefung, ob die Besoldung eines Beamten oder Richters dem Grundsatz der amtsangemessenen Alimentation aus Art. 33 Abs. 5 GG entspricht. Anwendung beim Widerspruch gegen die monatliche Besoldungsmitteilung mit dem Ziel der verfassungsgerichtlichen Vorlage durch das VG nach Art. 100 Abs. 1 GG.

## 2. Eingaben

- Besoldungsgruppe und Stufenstand
- Familienstand und Anzahl der unterhaltsberechtigten Kinder
- Bundesland oder Bund
- Besoldungsstrukturmaszgesetz / Besoldungstabelle
- Tarifentwicklung TV-L oder TVoeD vergleichbar
- Preisentwicklung Verbraucherpreisindex

## 3. Ablauf / Checkliste

### a) Erste Stufe — Pruefkriterien
- Das BVerfG hat in seiner staendigen Rechtsprechung mehrere Indikatoren etabliert, die im Zusammenwirken eine Vermutung der Unteralimentation begruenden koennen. Genannt werden u. a. Tarifentwicklung im öffentlichen Dienst, Verbraucherpreisindex, Vergleich zur Grundsicherung, Abstand zur naechstniedrigeren Besoldungsgruppe, Familienzuschlag für das dritte und jedes weitere Kind.

### b) Zweite Stufe — Gesamtbetrachtung
- Auf der zweiten Stufe ist eine Gesamtbetrachtung anzustellen, die auch qualitative Aspekte (Statusrelevanz, Mindestabstand zur Grundsicherung, Hergebrachte Grundsaetze) einbezieht.

### c) Dritte Stufe — Rechtfertigung
- Der Gesetzgeber kann Eingriffe nur in engen Grenzen rechtfertigen.

### d) Widerspruch und Rechtsweg
- Widerspruch gegen die monatliche Bezuegemitteilung (laenderspezifisch, ggf. Antrag auf erneute Festsetzung).
- Klage zum VG; Aussetzung des Verfahrens und Vorlage an das BVerfG nach Art. 100 Abs. 1 GG, wenn das VG von der Verfassungswidrigkeit ueberzeugt ist.

### e) Foederalismusreform 2006
- Die Besoldung der Landes- und Kommunalbeamten ist seit der Foederalismusreform Sache der Länder. Daraus folgen unterschiedliche Anpassungspfade. Verfassungswidrigkeit ist landesspezifisch zu pruefen.

## 4. Quellenpflicht

- Normen: Art. 33 Abs. 5, Art. 100 Abs. 1 GG; BBesG; Landesbesoldungsgesetze.
- Rspr.: BVerfG zur amtsangemessenen Alimentation (Leitentscheidungen zu R-Besoldung und A-Besoldung) — Quellenanker unten; konkrete Entscheidung in amtlicher oder freier Quelle prüfen (verbreitet zitierte Entscheidungen mit Aktenzeichen wie "2 BvL 17/09" oder "2 BvL 4/18" im konkreten Mandat in amtlicher Quelle pruefen).
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Widerspruchsschrift gegen Besoldungsfestsetzung.
- Memoraster mit den BVerfG-Indikatoren.
- Vorbereitendes Schreiben für Klage am VG mit Antrag auf Vorlage an das BVerfG.

## 6. Verifizierte Quellenanker

- BVerfG, 05.05.2015 - 2 BvL 17/09 u.a.: R-Besoldung Sachsen-Anhalt; Parameterprüfung zur amtsangemessenen Alimentation.
- BVerfG, 04.05.2020 - 2 BvL 4/18: R-Besoldung Berlin; Mindestabstand und Alimentation.
- BVerfG, 04.05.2020 - 2 BvL 6/17 u.a.: kinderreiche Richterfamilien und Familienzuschlag.
- BVerfG, 17.09.2025 - 2 BvL 20/17 u.a.: Berliner A-Besoldung; Prekaritätsschwelle und Dreischritt.
- Seit der Föderalismusreform 2006 ist Landesbesoldung landesrechtlich zu prüfen; BBesG nur für Bund/Soldaten und fortgeltende Sonderlagen.
- Für Stufen, Auslandsdienstbezüge, Erschwerniszulagen und Mehrarbeit zusätzlich aktuelle Spezialnormen live prüfen; die BVerfG-Linie ersetzt keine Fachnormprüfung.

## 7. Beispiel (Kurzfassung)

R1-Richterin in einem Bundesland mit alter Besoldungstabelle, drei Kinder. Skill liefert Indikatorentabelle, Widerspruchsentwurf mit Antrag auf Vorlage an das BVerfG sowie Hinweis auf laufende Verfahren in der eigenen Besoldungsgruppe.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 33 GG (hergebrachte Grundsätze des Berufsbeamtentums)
- §§ 7, 8 BeamtStG / § 12 BBG (Ernennung, Voraussetzungen)
- § 31 BeamtStG / § 28 BBG (Probezeit)
- §§ 33-37 BeamtStG (Grundpflichten)
- §§ 47 ff. BeamtStG, BDG (Dienstvergehen, Disziplinarverfahren)
- BBesG (Besoldung)
- BeamtVG (Versorgung)
- § 78 BBG (Fürsorgepflicht)
- VwGO §§ 42, 75, 113 (Verpflichtungsklage, Untätigkeit)
- BLV (Laufbahnverordnung)

### Leitentscheidungen

- BVerfG 2 BvR 1738/12 (Beamtenstreikverbot)
- BVerwG 2 C 32.10 (amtsangemessene Alimentation)
- BVerfG 2 BvL 4/18 (Richterbesoldung)
- BVerwG 2 C 33.20 (Disziplinarmaßnahme Verhältnismäßigkeit)
- BVerwG 2 C 4.18 (Konkurrentenstreitverfahren)

### Anwendung im Skill

- Amtsangemessene Alimentation nach BVerfG 2 BvL 4/18 als verfassungsrechtlicher Mindeststandard.
- Disziplinarmassnahme nach BDG/LDG am Verhaeltnismaessigkeitsgrundsatz messen; Entfernung erfordert schwere Verfehlung.
- Konkurrentenstreitverfahren BVerwG 2 C 4.18: Bewerbungsverfahrensanspruch Art. 33 Abs. 2 GG sichern, vor Ernennung.

---

## Skill: `anforderungsprofil-konstitutiv`

_Skill zur Unterscheidung konstitutives Anforderungsprofil und deklaratorisches Anforderungsprofil bei der beamtenrechtlichen Auswahlentscheidung. Klaert wann ein im Anforderungsprofil aufgestelltes Merkmal die Vergleichsbasis verengt und wann es nur als Auslegungshilfe der Beurteilungen dient. Li..._

# Anforderungsprofil — konstitutiv oder deklaratorisch

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: Widerspruch 1 Monat (VwGO § 70), Disziplinarverfahren nach BDG, Beihilfeantrag i.d.R. 1 Jahr, Beförderung-Auswahlentscheidung Bewährungsfristen.
- Tragende Normen verifizieren: BeamtStG §§ 3, 4, 21-25, 30, 33-41, BBG, BBesG, BeamtVG, LBG der Länder, GG Art. 33 Abs. 4 und 5, BDG, LDG, VwGO §§ 126 ff., LPVG/BPersVG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Dienstherr (Bund/Land/Kommune), Beamter, Dienstvorgesetzter, Personalrat, Personalvertretung, Disziplinarvorgesetzter, VG, OVG, BVerwG (2. Senat).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Ernennungsurkunde, dienstliche Beurteilung, Konkurrentenklage, Disziplinarverfügung, Versorgungsbescheid, Beihilfeantrag, Personalratsentscheidung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## 1. Zweck und Anwendungsfall

Skill für Konstellationen, in denen das Anforderungsprofil der Stellenausschreibung Merkmale enthaelt, die den Bewerberkreis einengen (typisch: Sprachzertifikat C1, mehrjaehrige Verwendung in einem Referat, Promotion, Auslandserfahrung, Personalfuehrungserfahrung).

## 2. Eingaben

- Wortlaut der Stellenausschreibung
- Anforderungskatalog mit Trennung "obligatorisch" / "fakultativ" / "wuenschenswert"
- Auswahlvermerk mit Begruendung des Ausschluss
- Stelleninhalt / Aufgabenkatalog der zu besetzenden Stelle

## 3. Ablauf / Checkliste

### a) Konstitutiv oder deklaratorisch
- Konstitutiv (auch: zwingend) ist ein Merkmal, dessen Fehlen ohne weitere Pruefung zum Ausschluss fuehrt. Es engt die Vergleichsgruppe ein.
- Deklaratorisch ist ein Merkmal, das nur die Auslegung der Beurteilung leitet und bei der Bewertung gewichtet wird.

### b) Rechtfertigungsanforderung
- Ein konstitutives Anforderungsprofil ist nur zulaessig, wenn es sachlich gerechtfertigt ist und einen Bezug zur konkreten Aufgabenwahrnehmung hat (BVerwG-Rechtsprechung, konkret vor Zitat frei prüfen).
- Es darf nicht auf einen einzelnen Wunschbewerber zugeschnitten sein. Ein Zuschnittsverdacht ergibt sich aus Indizien (sehr enges Kriterienbuendel, Identitaet mit Vita des Wunschbewerbers, fehlende Vorgeschichte für solche Anforderungen).

### c) Folge eines unzulaessigen Profils
- Die Auswahlentscheidung ist rechtswidrig; das gesamte Verfahren ist neu zu durchlaufen.
- Bei laufendem Auswahlverfahren: einstweilige Anordnung gegen Ernennung des Konkurrenten — Skill `konkurrentenklage-einstweiliger-rechtsschutz`.

### d) Schutz des Wettbewerbsverfahrens
- Auch wenn ein einzelnes Merkmal entfaellt, bleibt der Bestenauslese-Grundsatz erhalten; die uebrigen Anforderungen sind weiter pruefen.

## 4. Quellenpflicht

- Normen: Art. 33 Abs. 2 GG; § 9 BBG; § 9 BeamtStG; §§ 32 ff. BLV.
- Rspr.: BVerwG zum Anforderungsprofil — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Pruefvermerk: Tabelle "Merkmal — konstitutiv ja oder nein — Begruendung — Sachzusammenhang — Rechtsfolge".
- Eilantragsbaustein.

## 6. Verifizierte Quellenanker

- Art. 33 Abs. 2 GG: Bestenauslese nach Eignung, Befähigung und fachlicher Leistung.
- Art. 74 Abs. 1 Nr. 27 GG und Art. 70 GG: Statusrechtliche Bundeskompetenz, Laufbahn/Besoldung/Versorgung der Länder grundsätzlich Landesrecht.
- BeamtStG und BBG immer nach Dienstherr trennen; Landesbeamtengesetz und Beurteilungsrichtlinien live prüfen.
- BVerwG, 11.10.2016 - 2 C 11.15 als verifizierter Anker zu Art. 33 Abs. 2 GG und Eignungsanforderungen bei Höchstaltersgrenzen.
- Für Spezialfragen der dienstlichen Beurteilung, Anlassbeurteilung, Binnendifferenzierung und Auswahlgespräch keine privaten Datenbankzitate verwenden; konkrete Rechtsprechung nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.

## 7. Beispiel (Kurzfassung)

Stelle Referatsleiterin im BMI A16. Konstitutiv gefordert: Promotion im öffentlichen Recht, Auslandserfahrung in einem englischsprachigen Land, einschlaegige Personalfuehrungserfahrung in mindestens zwei Bundesministerien. Skill liefert Argument: Profil ist passgenau auf eine bestimmte Person zugeschnitten, daher unzulaessig.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 33 GG (hergebrachte Grundsätze des Berufsbeamtentums)
- §§ 7, 8 BeamtStG / § 12 BBG (Ernennung, Voraussetzungen)
- § 31 BeamtStG / § 28 BBG (Probezeit)
- §§ 33-37 BeamtStG (Grundpflichten)
- §§ 47 ff. BeamtStG, BDG (Dienstvergehen, Disziplinarverfahren)
- BBesG (Besoldung)
- BeamtVG (Versorgung)
- § 78 BBG (Fürsorgepflicht)
- VwGO §§ 42, 75, 113 (Verpflichtungsklage, Untätigkeit)
- BLV (Laufbahnverordnung)

### Leitentscheidungen

- BVerfG 2 BvR 1738/12 (Beamtenstreikverbot)
- BVerwG 2 C 32.10 (amtsangemessene Alimentation)
- BVerfG 2 BvL 4/18 (Richterbesoldung)
- BVerwG 2 C 33.20 (Disziplinarmaßnahme Verhältnismäßigkeit)
- BVerwG 2 C 4.18 (Konkurrentenstreitverfahren)

### Anwendung im Skill

- Amtsangemessene Alimentation nach BVerfG 2 BvL 4/18 als verfassungsrechtlicher Mindeststandard.
- Disziplinarmassnahme nach BDG/LDG am Verhaeltnismaessigkeitsgrundsatz messen; Entfernung erfordert schwere Verfehlung.
- Konkurrentenstreitverfahren BVerwG 2 C 4.18: Bewerbungsverfahrensanspruch Art. 33 Abs. 2 GG sichern, vor Ernennung.

---

## Skill: `anlassbeurteilung-vs-regelbeurteilung`

_Klaert das Verhaeltnis von Regelbeurteilung und Anlassbeurteilung im Auswahlverfahren des öffentlichen Dienstes. Skill pruef Beurteilungsstichtag Aktualitaet der Beurteilungsgrundlage und Vergleichbarkeit der konkurrierenden Beurteilungen. Behandelt die Konstellation einer Konkurrentensituation i..._

# Anlassbeurteilung vs. Regelbeurteilung — Aktualitaet und Vergleichbarkeit

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: Widerspruch 1 Monat (VwGO § 70), Disziplinarverfahren nach BDG, Beihilfeantrag i.d.R. 1 Jahr, Beförderung-Auswahlentscheidung Bewährungsfristen.
- Tragende Normen verifizieren: BeamtStG §§ 3, 4, 21-25, 30, 33-41, BBG, BBesG, BeamtVG, LBG der Länder, GG Art. 33 Abs. 4 und 5, BDG, LDG, VwGO §§ 126 ff., LPVG/BPersVG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Dienstherr (Bund/Land/Kommune), Beamter, Dienstvorgesetzter, Personalrat, Personalvertretung, Disziplinarvorgesetzter, VG, OVG, BVerwG (2. Senat).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Ernennungsurkunde, dienstliche Beurteilung, Konkurrentenklage, Disziplinarverfügung, Versorgungsbescheid, Beihilfeantrag, Personalratsentscheidung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## 1. Zweck und Anwendungsfall

Skill für den haeufigen Streit, ob die Auswahlentscheidung auf einer ausreichend aktuellen, miteinander vergleichbaren Beurteilungsgrundlage beruht. Zwei zentrale Konstellationen: (a) Mandant hat alte Regelbeurteilung, Konkurrent eine frische Anlassbeurteilung; (b) Mandant hat juengere Anlassbeurteilung, Konkurrent steht in Regelbeurteilung. Skill liefert die Argumentationsbausteine.

## 2. Eingaben

- Beurteilungsstichtag der Regelbeurteilung des Dienstherrn (typisch dreijaehriger Turnus, laenderspezifisch)
- Datum der letzten Beurteilung Mandant und letzter Beurteilung des Konkurrenten
- Beurteilungsrichtlinie des Dienstherrn (Behörden-RL, ZBR, VwV)
- Konkurrentenmitteilung samt Auswahlvermerk

## 3. Ablauf / Checkliste

### a) Aktualitaetsgrenze
- Eine Beurteilung gilt nach staendiger Rechtsprechung des BVerwG nur eine begrenzte Zeit als hinreichend aktuell. Faustregel: rund drei Jahre, Einzelfall pruefen. Bei Aelterer Regelbeurteilung ist eine Anlassbeurteilung in der Regel geboten.

### b) Anlassbeurteilung als Pflicht oder Verbot
- Pflicht: wenn seit der letzten Beurteilung relevanter Zeitraum verstrichen ist oder eine wesentliche Veraenderung der Verwendung eingetreten ist.
- Unzulaessig oder problematisch: wenn die Anlassbeurteilung zu einer Ungleichbehandlung der Konkurrenten fuehrt, weil nur einer eine neue Beurteilung erhaelt.

### c) Vergleichbarkeit
- Gleicher Beurteilungsmaszstab, gleicher Beurteilungszeitraum, gleiche Beurteilungsskala — sonst Auswahlfehler.
- Bei unterschiedlichen Beurteilungssystemen (z. B. nach Wechsel zwischen Bund und Land) ist eine "Umsetzungsbetrachtung" erforderlich; ständige Rechtsprechung, konkret vor Zitat frei prüfen.

### d) Beurteilungszeitraum
- Kein nahtloser Anschluss erforderlich, aber Luecke darf nicht groesser sein als der Regelturnus.
- Beurteilungen ueber sehr kurzen Zeitraum (unter sechs Monaten) sind in der Regel angreifbar; Substanz im Beurteilungszeitraum nicht gegeben.

### e) Verwertbarkeit
- Eine in einem anderen Auswahlverfahren erstellte Anlassbeurteilung kann im neuen Verfahren grundsaetzlich herangezogen werden, sofern weiterhin aktuell und vergleichbar.

## 4. Quellenpflicht

- Normen: §§ 21, 22 BBG; § 18 BLV; Beurteilungsrichtlinien des Bundes oder des jeweiligen Landes.
- Rspr.: BVerwG zur Aktualitaet und Vergleichbarkeit von Beurteilungen — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Pruefvermerk in Memoform mit Spalten "Aktualitaet — Vergleichbarkeit — Massstab — Spielraum".
- Schriftsatzbaustein "Begruendung Anordnungsanspruch" für Konkurrenteneilantrag.

## 6. Verifizierte Quellenanker

- Art. 33 Abs. 2 GG: Bestenauslese nach Eignung, Befähigung und fachlicher Leistung.
- Art. 74 Abs. 1 Nr. 27 GG und Art. 70 GG: Statusrechtliche Bundeskompetenz, Laufbahn/Besoldung/Versorgung der Länder grundsätzlich Landesrecht.
- BeamtStG und BBG immer nach Dienstherr trennen; Landesbeamtengesetz und Beurteilungsrichtlinien live prüfen.
- BVerwG, 11.10.2016 - 2 C 11.15 als verifizierter Anker zu Art. 33 Abs. 2 GG und Eignungsanforderungen bei Höchstaltersgrenzen.
- Für Spezialfragen der dienstlichen Beurteilung, Anlassbeurteilung, Binnendifferenzierung und Auswahlgespräch keine privaten Datenbankzitate verwenden; konkrete Rechtsprechung nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.

## 7. Beispiel (Kurzfassung)

Regelbeurteilung Mandant Stichtag vor 4 Jahren, Bewertung "uebertrifft die Anforderungen". Konkurrentin erhielt vor drei Monaten Anlassbeurteilung mit der gleichen Endnote. Skill liefert Argument: entweder Anlassbeurteilung auch für Mandant erforderlich oder Auswahlvergleich auf Basis veralteter Regelbeurteilung unzulaessig — Auswahlentscheidung aufzuheben.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 33 GG (hergebrachte Grundsätze des Berufsbeamtentums)
- §§ 7, 8 BeamtStG / § 12 BBG (Ernennung, Voraussetzungen)
- § 31 BeamtStG / § 28 BBG (Probezeit)
- §§ 33-37 BeamtStG (Grundpflichten)
- §§ 47 ff. BeamtStG, BDG (Dienstvergehen, Disziplinarverfahren)
- BBesG (Besoldung)
- BeamtVG (Versorgung)
- § 78 BBG (Fürsorgepflicht)
- VwGO §§ 42, 75, 113 (Verpflichtungsklage, Untätigkeit)
- BLV (Laufbahnverordnung)

### Leitentscheidungen

- BVerfG 2 BvR 1738/12 (Beamtenstreikverbot)
- BVerwG 2 C 32.10 (amtsangemessene Alimentation)
- BVerfG 2 BvL 4/18 (Richterbesoldung)
- BVerwG 2 C 33.20 (Disziplinarmaßnahme Verhältnismäßigkeit)
- BVerwG 2 C 4.18 (Konkurrentenstreitverfahren)

### Anwendung im Skill

- Amtsangemessene Alimentation nach BVerfG 2 BvL 4/18 als verfassungsrechtlicher Mindeststandard.
- Disziplinarmassnahme nach BDG/LDG am Verhaeltnismaessigkeitsgrundsatz messen; Entfernung erfordert schwere Verfehlung.
- Konkurrentenstreitverfahren BVerwG 2 C 4.18: Bewerbungsverfahrensanspruch Art. 33 Abs. 2 GG sichern, vor Ernennung.

---

## Skill: `anrechnung-55-beamtvg-mehrere-renten`

_Skill zur Anrechnungsregelung von Renten auf die Beamtenversorgung nach § 55 BeamtVG. Klaert das Zusammenwirken der Beamtenversorgung mit gesetzlicher Rente Altersrente Erwerbsminderungsrente sowie Renten aus berufsstaendischer oder zwischenstaatlicher Versorgung. Behandelt das Verhaeltnis zum Ho..._

# Anrechnung Renten nach § 55 BeamtVG

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: Widerspruch 1 Monat (VwGO § 70), Disziplinarverfahren nach BDG, Beihilfeantrag i.d.R. 1 Jahr, Beförderung-Auswahlentscheidung Bewährungsfristen.
- Tragende Normen verifizieren: BeamtStG §§ 3, 4, 21-25, 30, 33-41, BBG, BBesG, BeamtVG, LBG der Länder, GG Art. 33 Abs. 4 und 5, BDG, LDG, VwGO §§ 126 ff., LPVG/BPersVG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Dienstherr (Bund/Land/Kommune), Beamter, Dienstvorgesetzter, Personalrat, Personalvertretung, Disziplinarvorgesetzter, VG, OVG, BVerwG (2. Senat).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Ernennungsurkunde, dienstliche Beurteilung, Konkurrentenklage, Disziplinarverfügung, Versorgungsbescheid, Beihilfeantrag, Personalratsentscheidung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## 1. Zweck und Anwendungsfall

Skill für Versorgungsempfaenger, die neben der Beamtenversorgung Renten aus der gesetzlichen Rentenversicherung, einer berufsstaendischen Versorgungseinrichtung oder einer auslaendischen Versorgung beziehen.

## 2. Eingaben

- Versorgungsbescheid mit Bruttobezuegen
- Rentenbescheide aller Versorgungstraeger
- Art der Renten (Altersrente, Witwerrente, EM-Rente, betriebliche Versorgung)
- Datum des Rentenbeginns

## 3. Ablauf / Checkliste

### a) Grundprinzip
- Die Summe aus Beamtenversorgung und anrechenbarer Rente darf eine Hoechstgrenze nicht uebersteigen. Die Hoechstgrenze entspricht im Regelfall den ruhegehaltfaehigen Dienstbezuegen nach einer fiktiven Hoechstdienstzeit.

### b) Anrechenbare Renten
- Gesetzliche Rente einschliesslich Anteile aus Kindererziehungszeiten.
- Hinterbliebenenrenten ggf. anteilig.
- Auslaendische Renten (EU-Mitgliedstaaten) sind nach EuGH-Rechtsprechung zu beruecksichtigen — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Berufsstaendische Versorgung (Aerztekammer, Rechtsanwaltskammer) grundsaetzlich anrechenbar, soweit beamtengleicher Ursprung.

### c) Nicht anrechenbar
- Renten aus privater Lebens- oder Rentenversicherung.
- Renten, die ohne Bezug zum Beamtenverhaeltnis aus eigenen Beitraegen finanziert wurden, in dem Umfang nicht.

### d) Hinausgeschobener Versorgungsbeginn
- Beim Hinausschieben des Eintritts in den Ruhestand entfallen Anrechnungen anteilig.

## 4. Quellenpflicht

- Normen: § 55 BeamtVG; landesrechtliche Aequivalente; Verordnung EG 883/2004 (Soziale Sicherheit).
- Rspr.: BVerwG und EuGH zu § 55 BeamtVG — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Berechnung der Hoechstgrenze und der Anrechnungsbetraege.
- Antragsschreiben bei Nichtanrechnung pflichtiger Bestandteile.

## 6. Verifizierte Quellenanker

- BeamtVG und jeweiliges Landesversorgungsrecht sauber trennen; Versorgung ist bei Landesbeamten seit der Föderalismusreform grundsätzlich Landesrecht.
- BVerfG, 27.09.2005 - 2 BvR 1387/02: Versorgungsänderungsrecht und Alimentationsprinzip als verfassungsrechtlicher Anker.
- BVerfG, 20.03.2007 - 2 BvL 11/04: Versorgung aus dem letzten Amt und Wartefrist.
- BVerwG, 25.10.2018 - 2 C 33.17 sowie BVerwG, 30.10.2018 - 2 C 32.17 als verifizierte Anker für Besoldungs-/Versorgungsvorlagen; Reichweite auf konkrete Versorgungsfrage jeweils prüfen.
- Konkrete Berechnung nie aus Modellwissen: Bescheid, Dienstzeiten, Ruhensnormen, Rentenbescheide und Landesrecht in Tabelle nachziehen.

## 7. Beispiel (Kurzfassung)

Pensionierter Studiendirektor erhaelt Altersrente aus zehn Jahren Lehrertaetigkeit vor Verbeamtung und zusaetzlich eine schwedische Tjaenstepension. Skill liefert Hoechstgrenzenberechnung und EuGH-konforme Beruecksichtigung der EU-Rente.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 33 GG (hergebrachte Grundsätze des Berufsbeamtentums)
- §§ 7, 8 BeamtStG / § 12 BBG (Ernennung, Voraussetzungen)
- § 31 BeamtStG / § 28 BBG (Probezeit)
- §§ 33-37 BeamtStG (Grundpflichten)
- §§ 47 ff. BeamtStG, BDG (Dienstvergehen, Disziplinarverfahren)
- BBesG (Besoldung)
- BeamtVG (Versorgung)
- § 78 BBG (Fürsorgepflicht)
- VwGO §§ 42, 75, 113 (Verpflichtungsklage, Untätigkeit)
- BLV (Laufbahnverordnung)

### Leitentscheidungen

- BVerfG 2 BvR 1738/12 (Beamtenstreikverbot)
- BVerwG 2 C 32.10 (amtsangemessene Alimentation)
- BVerfG 2 BvL 4/18 (Richterbesoldung)
- BVerwG 2 C 33.20 (Disziplinarmaßnahme Verhältnismäßigkeit)
- BVerwG 2 C 4.18 (Konkurrentenstreitverfahren)

### Anwendung im Skill

- Amtsangemessene Alimentation nach BVerfG 2 BvL 4/18 als verfassungsrechtlicher Mindeststandard.
- Disziplinarmassnahme nach BDG/LDG am Verhaeltnismaessigkeitsgrundsatz messen; Entfernung erfordert schwere Verfehlung.
- Konkurrentenstreitverfahren BVerwG 2 C 4.18: Bewerbungsverfahrensanspruch Art. 33 Abs. 2 GG sichern, vor Ernennung.

---

## Skill: `auslandsdienstbezuege-bbesg`

_Skill zu Auslandsdienstbezuegen im Auswaertigen Dienst und in der Auslandsverwendung. Klaert Auslandszuschlag Kaufkraftausgleich Mietzuschuss Auslandskinderzuschlag Bewertung der Auslandsdienstpostenkategorie und Bezuege bei Hardship-Posten. Behandelt das Verhaeltnis zur Bundesbesoldung und die B..._

# Auslandsdienstbezuege nach BBesG

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: Widerspruch 1 Monat (VwGO § 70), Disziplinarverfahren nach BDG, Beihilfeantrag i.d.R. 1 Jahr, Beförderung-Auswahlentscheidung Bewährungsfristen.
- Tragende Normen verifizieren: BeamtStG §§ 3, 4, 21-25, 30, 33-41, BBG, BBesG, BeamtVG, LBG der Länder, GG Art. 33 Abs. 4 und 5, BDG, LDG, VwGO §§ 126 ff., LPVG/BPersVG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Dienstherr (Bund/Land/Kommune), Beamter, Dienstvorgesetzter, Personalrat, Personalvertretung, Disziplinarvorgesetzter, VG, OVG, BVerwG (2. Senat).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Ernennungsurkunde, dienstliche Beurteilung, Konkurrentenklage, Disziplinarverfügung, Versorgungsbescheid, Beihilfeantrag, Personalratsentscheidung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## 1. Zweck und Anwendungsfall

Skill für Beamte im Auswaertigen Dienst, in Auslandsentsendung der Bundespolizei, der Bundeswehr und in zwischenstaatlichen oder ueberstaatlichen Einrichtungen (NATO, EU, UN). Klaert Auslandsdienstbezuege, Kaufkraftausgleich, Auslandszuschlag, Mietzuschuss und Auslandskinderzuschlag.

## 2. Eingaben

- Auslandsdienststelle und Posten-Kategorisierung
- Familienstand und Anzahl Kinder am Dienstort und im Inland
- Mietvertrag am Dienstort, Mietniveau
- Schulbesuch der Kinder (öffentliche oder private Auslandsschule)
- Hardship-Stufe des Postens

## 3. Ablauf / Checkliste

### a) Auslandszuschlag (§ 53 BBesG)
- Hoehe abhaengig von Posten-Kategorie, Familienstand, Dienststellung.
- Pruefung der korrekten Eingruppierung des Mandanten.

### b) Mietzuschuss (§ 54 BBesG)
- Mietzuschuss für den Anteil der Miete, der einen Selbstbehalt uebersteigt.
- Berechnung in Anlehnung an Mietniveau-Tabellen des Auswaertigen Amtes.

### c) Auslandskinderzuschlag (§ 56 BBesG)
- Pauschale je Kind am Dienstort, ggf. erhoeht in Ländern mit hohen Schul- oder Lebenshaltungskosten.
- Auslandsschulgeld erstattungsfaehig nach Rahmenbedingungen.

### d) Kaufkraftausgleich (§ 55 BBesG)
- Berechnet auf Basis der Indizes des Statistischen Bundesamtes je Auslandsdienstort; Ausgleich der Kaufkraftunterschiede.

### e) Hardship und Auslandsverwendungszuschlag
- Bei Posten mit besonderen Belastungen (Sicherheitslage, klimatische Bedingungen) zusaetzliche Zuschlaege; Auslandsverwendungszuschlagsverordnung.

### f) Beendigung Auslandsverwendung
- Rueckkehrregelung, Tropentauglichkeit, gesundheitliche Pruefung; ggf. Anschlussverwendung.

## 4. Quellenpflicht

- Normen: §§ 52 bis 56 BBesG; Auslandsverwendungszuschlagsverordnung; einschlaegige Erlasse AA und BMF.
- Rspr.: BVerwG zu Auslandsbezuegen — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Berechnungstabelle Auslandsbezuege.
- Antragsschreiben für Mietzuschuss oder Kaufkraftausgleich.

## 6. Verifizierte Quellenanker

- BVerfG, 05.05.2015 - 2 BvL 17/09 u.a.: R-Besoldung Sachsen-Anhalt; Parameterprüfung zur amtsangemessenen Alimentation.
- BVerfG, 04.05.2020 - 2 BvL 4/18: R-Besoldung Berlin; Mindestabstand und Alimentation.
- BVerfG, 04.05.2020 - 2 BvL 6/17 u.a.: kinderreiche Richterfamilien und Familienzuschlag.
- BVerfG, 17.09.2025 - 2 BvL 20/17 u.a.: Berliner A-Besoldung; Prekaritätsschwelle und Dreischritt.
- Seit der Föderalismusreform 2006 ist Landesbesoldung landesrechtlich zu prüfen; BBesG nur für Bund/Soldaten und fortgeltende Sonderlagen.
- Für Stufen, Auslandsdienstbezüge, Erschwerniszulagen und Mehrarbeit zusätzlich aktuelle Spezialnormen live prüfen; die BVerfG-Linie ersetzt keine Fachnormprüfung.

## 7. Beispiel (Kurzfassung)

Mandant ist Referent Botschaft Tokio, verheiratet, zwei Kinder. Auslandszuschlag Stufe falsch berechnet, Mietzuschuss nicht voll bemessen. Skill liefert Korrekturantrag mit Berechnung.

---

## Skill: `auswahlgespraech-dokumentationspflicht`

_Skill zu Anforderungen an strukturierte Auswahlgespraeche und Assessment Center im beamtenrechtlichen Auswahlverfahren. Klaert die Dokumentationspflicht das Erfordernis gleicher Bedingungen für alle Bewerber die Beweislast bei Gespraechsfehlern und den Stellenwert eines Auswahlgespraechs gegenueb..._

# Auswahlgespraech — Dokumentationspflicht und Verfahrensfehler

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: Widerspruch 1 Monat (VwGO § 70), Disziplinarverfahren nach BDG, Beihilfeantrag i.d.R. 1 Jahr, Beförderung-Auswahlentscheidung Bewährungsfristen.
- Tragende Normen verifizieren: BeamtStG §§ 3, 4, 21-25, 30, 33-41, BBG, BBesG, BeamtVG, LBG der Länder, GG Art. 33 Abs. 4 und 5, BDG, LDG, VwGO §§ 126 ff., LPVG/BPersVG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Dienstherr (Bund/Land/Kommune), Beamter, Dienstvorgesetzter, Personalrat, Personalvertretung, Disziplinarvorgesetzter, VG, OVG, BVerwG (2. Senat).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Ernennungsurkunde, dienstliche Beurteilung, Konkurrentenklage, Disziplinarverfügung, Versorgungsbescheid, Beihilfeantrag, Personalratsentscheidung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## 1. Zweck und Anwendungsfall

Skill für Bewerber, die im Auswahlverfahren ein strukturiertes Auswahlgespraech absolviert haben und dessen Ergebnis als entscheidungstragenden Bestandteil beanstanden moechten. Anwendung neben `konkurrentenschutz-bestenauslese-art-33-ii-gg` und `anforderungsprofil-konstitutiv-deklaratorisch`.

## 2. Eingaben

- Einladung zum Auswahlgespraech (Wortlaut, Datum, Dauer)
- Protokoll oder Niederschrift des Gespraechs
- Besetzung der Auswahlkommission
- Fragenliste, falls strukturiert
- Bewertungsbogen und Punktverteilung
- Auswahlvermerk und Gewichtung gegenueber Beurteilung

## 3. Ablauf / Checkliste

### a) Stellenwert
- Vorrang der dienstlichen Beurteilung. Auswahlgespraech ist Hilfskriterium, das insbesondere bei gleicher Eignung Differenzierung ermoeglicht (BVerwG-Rechtsprechung, konkret vor Zitat frei prüfen).
- Bei alleiniger Stuetzung der Auswahl auf das Gespraech ist die Auswahlentscheidung in der Regel rechtswidrig.

### b) Strukturierung und Gleichbehandlung
- Gleiche Kernfragen für alle Bewerber, gleiche Zeitbudgets, gleiche Bewertungskriterien.
- Wechsel der Kommissionsbesetzung waehrend des Verfahrens fuehrt regelmaessig zu Verfahrensfehler.

### c) Dokumentationspflicht
- Wesentliche Aussagen sind so zu dokumentieren, dass eine gerichtliche Kontrolle moeglich ist. Reine Punkthebel ohne Begruendung genuegen nicht.
- Die Dokumentation muss im Auswahlvermerk verarbeitet werden.

### d) Befangenheit
- Mitwirkung eines mit dem ausgewaehlten Konkurrenten in besonderer Naehe stehenden Kommissionsmitglieds (z. B. langjaeriger Vorgesetzter) ist zu pruefen; § 21 VwVfG entsprechend.
- Nichtbestellung einer Schwerbehindertenvertretung oder Gleichstellungsbeauftragten, wenn Pflichtteilnahme bestand, ist Verfahrensfehler.

### e) Beweislast
- Im Eilverfahren genuegt Glaubhaftmachung der Verfahrensfehler. Das Gericht zieht den Verwaltungsvorgang bei.

## 4. Quellenpflicht

- Normen: Art. 33 Abs. 2 GG; § 9 BBG; §§ 32 ff. BLV; § 21 VwVfG; § 178 ff. SGB IX (Schwerbehindertenvertretung).
- Rspr.: BVerwG zur Bedeutung und Grenzen des Auswahlgespraechs — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Pruefraster Verfahrensfehler.
- Eilantragsbaustein "Anordnungsanspruch — Gespraechsfehler".

## 6. Verifizierte Quellenanker

- Art. 33 Abs. 2 GG: Bestenauslese nach Eignung, Befähigung und fachlicher Leistung.
- Art. 74 Abs. 1 Nr. 27 GG und Art. 70 GG: Statusrechtliche Bundeskompetenz, Laufbahn/Besoldung/Versorgung der Länder grundsätzlich Landesrecht.
- BeamtStG und BBG immer nach Dienstherr trennen; Landesbeamtengesetz und Beurteilungsrichtlinien live prüfen.
- BVerwG, 11.10.2016 - 2 C 11.15 als verifizierter Anker zu Art. 33 Abs. 2 GG und Eignungsanforderungen bei Höchstaltersgrenzen.
- Für Spezialfragen der dienstlichen Beurteilung, Anlassbeurteilung, Binnendifferenzierung und Auswahlgespräch keine privaten Datenbankzitate verwenden; konkrete Rechtsprechung nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.

## 7. Beispiel (Kurzfassung)

Konkurrentensituation um A15-Stelle. Auswahlgespraech entscheidet, da Beurteilungen gleich. Mandant ruegt: unterschiedliche Fragenkataloge, kein Protokoll, Kommissionsmitglied war im Vorjahr Vorgesetzter der Konkurrentin. Skill liefert Anordnungsanspruch für einstweilige Anordnung.

---

## Skill: `begrenzte-dienstfaehigkeit-27-bbg`

_Skill zur begrenzten Dienstfaehigkeit nach § 27 BBG bzw. § 27 BeamtStG. Klaert die Voraussetzungen für die Reduzierung der Arbeitszeit anstatt Versetzung in den Ruhestand das Verhaeltnis zu § 26 BBG Dienstunfaehigkeit die Bezuegehoehe bei begrenzter Dienstfaehigkeit und die Auswirkungen auf die V..._

# Begrenzte Dienstfaehigkeit nach § 27 BBG

## Arbeitsbereich

Skill zur begrenzten Dienstfaehigkeit nach § 27 BBG bzw. § 27 BeamtStG. Klaert die Voraussetzungen für die Reduzierung der Arbeitszeit anstatt Versetzung in den Ruhestand das Verhaeltnis zu § 26 BBG Dienstunfaehigkeit die Bezuegehoehe bei begrenzter Dienstfaehigkeit und die Auswirkungen auf die Versorgungsanwartschaft. Behandelt das praktische Vorgehen amtsaerztliches Gutachten Pruefung anderweitiger Verwendung Beruecksichtigung der Belange des Beamten. Liefert Pruefraster und Schriftsatzbausteine. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: Widerspruch 1 Monat (VwGO § 70), Disziplinarverfahren nach BDG, Beihilfeantrag i.d.R. 1 Jahr, Beförderung-Auswahlentscheidung Bewährungsfristen.
- Tragende Normen verifizieren: BeamtStG §§ 3, 4, 21-25, 30, 33-41, BBG, BBesG, BeamtVG, LBG der Länder, GG Art. 33 Abs. 4 und 5, BDG, LDG, VwGO §§ 126 ff., LPVG/BPersVG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Dienstherr (Bund/Land/Kommune), Beamter, Dienstvorgesetzter, Personalrat, Personalvertretung, Disziplinarvorgesetzter, VG, OVG, BVerwG (2. Senat).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Ernennungsurkunde, dienstliche Beurteilung, Konkurrentenklage, Disziplinarverfügung, Versorgungsbescheid, Beihilfeantrag, Personalratsentscheidung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## 1. Zweck und Anwendungsfall

Skill für Beamte, deren Dienstfaehigkeit eingeschraenkt, aber nicht vollstaendig verloren ist. Anwendung als milderer Eingriff im Verhaeltnis zur Versetzung in den Ruhestand nach § 26 BBG.

## 2. Eingaben

- Amtsaerztliches Gutachten
- Dienstpostenbeschreibung
- Vorgesehene Verwendung (anderer Dienstposten?)
- Stellungnahme des Mandanten

## 3. Ablauf / Checkliste

### a) Voraussetzungen § 27 BBG
- Beamter ist nicht vollstaendig dienstunfaehig.
- Restliche Dienstleistung ist mit mindestens 50 v. H. der Arbeitszeit moeglich.
- Andersweitige Verwendung im Sinne § 26 Abs. 2 BBG ist zu pruefen.

### b) Verhaeltnis zu § 26 BBG
- § 27 BBG ist die mildere Maszahme; Vorrang vor Versetzung in den Ruhestand.
- Dienstherr ist verpflichtet, die Moeglichkeit der begrenzten Dienstfaehigkeit zu pruefen.

### c) Bezuege
- Bezuege werden anteilig der herabgesetzten Arbeitszeit gezahlt; ggf. Ausgleichszahlung nach den landesrechtlichen Vorschriften.

### d) Versorgungsanwartschaft
- Die Zeit der begrenzten Dienstfaehigkeit ist anteilig ruhegehaltfaehig.
- Sondervorschriften zur Hochrechnung bei spaeterer Versetzung in den Ruhestand.

### e) Verfahrensschritte
- Amtsaerztliches Gutachten.
- Anhörung Mandant.
- Bescheid; Rechtsschutz Widerspruch und Klage.

## 4. Quellenpflicht

- Normen: § 27 BBG; § 27 BeamtStG i.V.m. Landesrecht; § 26 BBG.
- Rspr.: BVerwG zur begrenzten Dienstfaehigkeit — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Antrag oder Widerspruch.
- Berechnung der reduzierten Bezuege und Versorgungsfolgen.

## 6. Verifizierte Quellenanker

- § 45 BBG (begrenzte Dienstfaehigkeit Bund); § 27 BeamtStG i.V.m. Landesrecht.
- § 44 BBG (Dienstunfaehigkeit) als Vergleichsmassstab; § 6 BeamtVG (anteilige Ruhegehaltfaehigkeit).
- Vorrang der milderen Massnahme: anderweitige Verwendung und begrenzte Dienstfaehigkeit vor Ruhestandsversetzung.
- BVerwG zur begrenzten Dienstfaehigkeit und zur Pruefungspflicht anderweitiger Verwendung — Datum und Az vor Zitat live verifizieren.

## 7. Beispiel (Kurzfassung)

Mandantin Polizeikommissarin mit Bandscheibenleiden, Innen- statt Streifendienst denkbar. Dienstherr will Ruhestand verfuegen. Skill liefert Antrag auf begrenzte Dienstfaehigkeit und Pruefraster anderweitiger Verwendung.

---

## Skill: `beihilfe-chronische-krankheit`

_Skill zur Beihilfe bei schwerer chronischer Krankheit nach den Beihilfeverordnungen des Bundes und der Länder. Klaert Definition chronische Krankheit Belastungsgrenze und Eigenbehalt Befreiung von Zuzahlungen Pflegestufe und Pflegegrad sowie Verhaeltnis zur privaten Krankenversicherung. Behandelt..._

# Beihilfe bei chronischer Krankheit

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: Widerspruch 1 Monat (VwGO § 70), Disziplinarverfahren nach BDG, Beihilfeantrag i.d.R. 1 Jahr, Beförderung-Auswahlentscheidung Bewährungsfristen.
- Tragende Normen verifizieren: BeamtStG §§ 3, 4, 21-25, 30, 33-41, BBG, BBesG, BeamtVG, LBG der Länder, GG Art. 33 Abs. 4 und 5, BDG, LDG, VwGO §§ 126 ff., LPVG/BPersVG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Dienstherr (Bund/Land/Kommune), Beamter, Dienstvorgesetzter, Personalrat, Personalvertretung, Disziplinarvorgesetzter, VG, OVG, BVerwG (2. Senat).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Ernennungsurkunde, dienstliche Beurteilung, Konkurrentenklage, Disziplinarverfügung, Versorgungsbescheid, Beihilfeantrag, Personalratsentscheidung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## 1. Zweck und Anwendungsfall

Skill für Beihilfeberechtigte mit schwerer chronischer Krankheit, die wegen hoher und wiederkehrender Behandlungskosten Befreiung von Eigenbehalten und besondere Beihilfeleistungen geltend machen wollen.

## 2. Eingaben

- Aerztliche Bescheinigung "schwerwiegend chronisch krank" nach Chroniker-Richtlinie
- Liste der laufenden Behandlungen und Medikamente
- Jahresbeihilfeauswertung
- Einkommen des Beihilfeberechtigten

## 3. Ablauf / Checkliste

### a) Definition schwerwiegend chronisch krank
- Definition orientiert sich an der Chroniker-Richtlinie des Gemeinsamen Bundesausschusses: regelmäßige Behandlung wegen derselben Krankheit ueber mindestens ein Jahr, mindestens einmal pro Quartal, mit bestimmten Schweregradkriterien.

### b) Befreiung von Eigenbehalten
- Reduzierung der Belastungsgrenze auf 1 v. H. der jaehrlichen Bruttoeinkuenfte (statt 2 v. H.).
- Antrag bei der Beihilfestelle, jaehrlich.

### c) Beihilfefaehigkeit von Therapien
- Pruefung der Beihilfefaehigkeit von Heilbehandlungen, Heilmitteln, Hilfsmitteln, Verbrauchsmaterialien (z. B. Blutzuckermessgeraete, CGM-Sensoren).

### d) Pflegegrad
- Bei Eintritt von Pflegebeduerftigkeit Antrag auf Beihilfe zu Pflege nach den Beihilfeverordnungen i.V.m. SGB XI.

### e) Verhaeltnis zur PKV
- PKV und Beihilfe sind aufeinander abzustimmen; Versicherungsbedingungen der PKV pruefen.

## 4. Quellenpflicht

- Normen: BBhV (Bund); landesrechtliche Beihilfeverordnungen; Chroniker-Richtlinie GBA; SGB V; SGB XI.
- Rspr.: BVerwG zu Eigenbehaltsbefreiung und chronischer Krankheit — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Antrag auf Reduzierung der Belastungsgrenze.
- Pruefraster Behandlung — Beihilfefaehigkeit — Eigenbehalt.

## 6. Verifizierte Quellenanker

- BBhV; Chroniker-Richtlinie des Gemeinsamen Bundesausschusses (G-BA) vom 22.01.2004 in jeweils geltender Fassung.
- SGB V (Belastungsgrenze und chronisch krank); SGB XI (Pflegebeduerftigkeit) ergaenzend zur Beihilfe.
- Landesrechtliche Beihilfeverordnungen mit eigenen Eigenbehaltsregelungen.
- BVerwG zur Eigenbehaltsbefreiung bei schwerwiegender chronischer Erkrankung — Az vor Zitat live verifizieren.

## 7. Beispiel (Kurzfassung)

Mandantin Multiple Sklerose, monatliche Immunmodulatoren, Krankengymnastik, Hilfsmittel. Skill liefert Antrag auf Befreiung von Eigenbehalten und Pruefung der Beihilfefaehigkeit des Spezialmedikaments.

---

## Skill: `beihilfe-heilbehandlung-ausland`

_Skill zur beamtenrechtlichen Beihilfefaehigkeit von Heilbehandlung im Ausland nach BBhV und den Landesbeihilfeverordnungen. Klaert die Konstellationen geplante Behandlung im EU-Ausland Notfallbehandlung Beihilfehoehe und Begrenzung auf das Inlandsniveau Beihilfe bei Reha im Ausland und Auslandsdi..._

# Beihilfe Heilbehandlung im Ausland

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: Widerspruch 1 Monat (VwGO § 70), Disziplinarverfahren nach BDG, Beihilfeantrag i.d.R. 1 Jahr, Beförderung-Auswahlentscheidung Bewährungsfristen.
- Tragende Normen verifizieren: BeamtStG §§ 3, 4, 21-25, 30, 33-41, BBG, BBesG, BeamtVG, LBG der Länder, GG Art. 33 Abs. 4 und 5, BDG, LDG, VwGO §§ 126 ff., LPVG/BPersVG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Dienstherr (Bund/Land/Kommune), Beamter, Dienstvorgesetzter, Personalrat, Personalvertretung, Disziplinarvorgesetzter, VG, OVG, BVerwG (2. Senat).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Ernennungsurkunde, dienstliche Beurteilung, Konkurrentenklage, Disziplinarverfügung, Versorgungsbescheid, Beihilfeantrag, Personalratsentscheidung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## 1. Zweck und Anwendungsfall

Skill für Beihilfeberechtigte, die eine Behandlung im Ausland in Anspruch nehmen wollen oder genommen haben und deren Erstattungsfaehigkeit klaeren wollen.

## 2. Eingaben

- Behandlungsland und Behandlungsart
- Rechnungen / Heilkostenbelege
- Indikation und aerztliche Notwendigkeit
- Vorabgenehmigung des Beihilfeberechtigten ja/nein
- Beihilfeverordnung Bund oder Land

## 3. Ablauf / Checkliste

### a) Grundregel
- Beihilfefaehigkeit nur bei medizinisch notwendiger und wirtschaftlicher Heilbehandlung. Bei Auslandsbehandlung Begrenzung der Erstattung auf das Niveau, das bei vergleichbarer Behandlung im Inland angefallen waere.

### b) Notfallbehandlung
- Bei medizinischen Notfaellen im Ausland keine Vorabgenehmigung erforderlich; Erstattung ohne Begrenzung auf Inlandsniveau moeglich, soweit nachvollziehbar notwendig.

### c) Geplante Behandlung im EU-Ausland
- Patientenrichtlinie 2011/24/EU: grenzueberschreitende Behandlung in der EU/im EWR ist nach Massgabe der nationalen Vorschriften erstattungsfaehig.
- Ggf. Vorabgenehmigung sinnvoll, um Unsicherheit zu vermeiden.

### d) Auslandsdienstbezuege
- Bei Auslandsverwendung ist Beihilfe regelmaessig nur für Restkosten nach Auslandsdienstkrankenversicherung zu beanspruchen.

### e) Rehabilitation im Ausland
- Reha im Ausland regelmaessig nur erstattungsfaehig, wenn ein vergleichbares Inlandsangebot fehlt oder die Maszahme im Einzelfall medizinisch erforderlich ist.

## 4. Quellenpflicht

- Normen: BBhV (Bund); landesrechtliche Beihilfeverordnungen; Richtlinie 2011/24/EU (Patientenrechte in der grenzueberschreitenden Gesundheitsversorgung).
- Rspr.: EuGH zur EU-Patientenrichtlinie; BVerwG zur Beihilfe im Ausland — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Antrag auf Beihilfe mit Rechnungen und aerztlicher Begruendung.
- Pruefraster Beihilfefaehigkeit im Ausland.

## 6. Verifizierte Quellenanker

- Richtlinie 2011/24/EU vom 09.03.2011 (Patientenrechte in der grenzueberschreitenden Gesundheitsversorgung).
- EuGH, 23.10.2003 - C-56/01 (Inizan); EuGH, 16.05.2006 - C-372/04 (Watts); EuGH, 19.04.2007 - C-444/05 (Stamatelaki).
- BBhV; landesrechtliche Beihilfeverordnungen; Auslandsdienstkrankenversicherungsregelungen.
- BVerwG zur Beihilfefaehigkeit von Auslandsbehandlungen — Datum und Az vor Zitat live verifizieren.

## 7. Beispiel (Kurzfassung)

Mandant laesst Hueftgelenkoperation in einer Wiener Klinik durchfuehren; Rechnung 18.500 Euro. Skill liefert Pruefung der Beihilfefaehigkeit nach Patientenrichtlinie und Begrenzung auf Inlandsniveau.

---

## Skill: `beihilfe-implantatfaehige-hoergeraete`

_Skill zur Beihilfefaehigkeit von hochwertigen Hilfsmitteln wie implantatfaehigen Hoergeraeten Cochlea-Implantaten elektronischen Sehhilfen orthopaedischen Spezialschuhen und Prothesen. Klaert das Erstattungsmodell unter der BBhV und den Landesvorschriften die Festbetragsregelung den medizinischen..._

# Beihilfe Spezialhilfsmittel — Hoergeraete Cochlea-Implantat Sehhilfen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: Widerspruch 1 Monat (VwGO § 70), Disziplinarverfahren nach BDG, Beihilfeantrag i.d.R. 1 Jahr, Beförderung-Auswahlentscheidung Bewährungsfristen.
- Tragende Normen verifizieren: BeamtStG §§ 3, 4, 21-25, 30, 33-41, BBG, BBesG, BeamtVG, LBG der Länder, GG Art. 33 Abs. 4 und 5, BDG, LDG, VwGO §§ 126 ff., LPVG/BPersVG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Dienstherr (Bund/Land/Kommune), Beamter, Dienstvorgesetzter, Personalrat, Personalvertretung, Disziplinarvorgesetzter, VG, OVG, BVerwG (2. Senat).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Ernennungsurkunde, dienstliche Beurteilung, Konkurrentenklage, Disziplinarverfügung, Versorgungsbescheid, Beihilfeantrag, Personalratsentscheidung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## 1. Zweck und Anwendungsfall

Skill für Beihilfeberechtigte, denen die Beihilfestelle bei der Erstattung hochwertiger Hilfsmittel die volle Kostenerstattung verweigert hat. Anwendung typischerweise bei Hoergeraeten oberhalb des Festbetrags und bei Cochlea-Implantat-Folgekosten.

## 2. Eingaben

- Aerztliche Verordnung Hilfsmittel
- Kostenvoranschlag des Hilfsmittelerbringers
- Beihilfebescheid mit Begruendung der Teilablehnung
- Anlage zur Beihilfeverordnung (z. B. Anlage 6 BBhV)
- Audiogramm oder vergleichbarer Funktionsnachweis

## 3. Ablauf / Checkliste

### a) Beihilfefaehigkeit dem Grunde nach
- Hilfsmittel ist beihilfefaehig, wenn medizinisch notwendig und in der Anlage der Beihilfeverordnung gelistet oder gleichgestellt.
- Anlage 6 BBhV gibt Festbetraege für typische Hilfsmittel vor.

### b) Festbetrag und Mehrkosten
- Erstattung bis zum Festbetrag.
- Mehrkosten beihilfefaehig nur bei besonderer medizinischer Notwendigkeit (z. B. hochgradige Schwerhoerigkeit, berufliche Erfordernisse, Kombination mit Cochlea-Implantat).

### c) Medizinische Notwendigkeit
- Aerztliche Begruendung und audiologischer Nachweis, dass das gewuenschte Geraet erforderlich ist und einfachere Hilfsmittel nicht ausreichen (BVerwG-Rechtsprechung, konkret vor Zitat frei prüfen).

### d) Verfahren
- Widerspruch gegen Beihilfebescheid; Klage zum VG; Aussetzungsantrag bei drohender hoher Belastung.
- Im Eilrechtsschutz vorläufige Erstattung nur bei akutem Versorgungsbedarf.

### e) Cochlea-Implantat
- Nachsorge mit Sprachprozessoren und Wartung beihilfefaehig in regelmäßigen Abstaenden; Streit oft um die Generation des Prozessors.

## 4. Quellenpflicht

- Normen: BBhV (insbesondere Anlage 6); landesrechtliche Beihilfeverordnungen.
- Rspr.: BVerwG zur Beihilfefaehigkeit hochwertiger Hilfsmittel — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Widerspruchsschrift mit medizinischer Begruendung.
- Antrag auf Erstattung in voller Hoehe.

## 6. Verifizierte Quellenanker

- BBhV insbesondere Anlage 6 (Hilfsmittel und Festbetraege); landesrechtliche Beihilfeverordnungen mit eigenen Hilfsmittelverzeichnissen.
- Festbetragsregelung als Regelgrenze; medizinische Notwendigkeit als Massstab für beihilfefaehige Mehrkosten.
- BVerwG zur Beihilfefaehigkeit hochwertiger Hilfsmittel und zur Pruefung medizinischer Notwendigkeit — Datum und Az vor Zitat live verifizieren.
- Hilfsmittelrichtlinie des G-BA und einschlaegige HNO- und audiologische Leitlinien als Begruendungsgrundlage.

## 7. Beispiel (Kurzfassung)

Mandant beidseitige Schwerhoerigkeit; HNO empfiehlt Geraet mit Bluetooth und Spezialakustik für Berufstaetigkeit als Richter (Verhandlung in grossen Saelen). Kostenvoranschlag 5.800 Euro, Festbetrag 1.500 Euro. Skill liefert Widerspruch mit Begruendung der Mehrkosten als medizinisch notwendig.

---

## Skill: `besoldung-verfassungswidrig-a-besoldung`

_Skill zur Geltendmachung verfassungswidriger A-Besoldung im Land. Pruefschema für den Verstoss gegen die amtsangemessene Alimentation in der A-Besoldung unter Beruecksichtigung des Mindestabstandsgebots zum sozialhilferechtlichen Grundsicherungsniveau. Behandelt die Konstellationen Familienzuschl..._

# Verfassungswidrige A-Besoldung — Mindestabstandsgebot und Geltendmachung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: Widerspruch 1 Monat (VwGO § 70), Disziplinarverfahren nach BDG, Beihilfeantrag i.d.R. 1 Jahr, Beförderung-Auswahlentscheidung Bewährungsfristen.
- Tragende Normen verifizieren: BeamtStG §§ 3, 4, 21-25, 30, 33-41, BBG, BBesG, BeamtVG, LBG der Länder, GG Art. 33 Abs. 4 und 5, BDG, LDG, VwGO §§ 126 ff., LPVG/BPersVG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Dienstherr (Bund/Land/Kommune), Beamter, Dienstvorgesetzter, Personalrat, Personalvertretung, Disziplinarvorgesetzter, VG, OVG, BVerwG (2. Senat).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Ernennungsurkunde, dienstliche Beurteilung, Konkurrentenklage, Disziplinarverfügung, Versorgungsbescheid, Beihilfeantrag, Personalratsentscheidung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## 1. Zweck und Anwendungsfall

Skill für Beamte und Richter, die geltend machen wollen, dass ihre Besoldung in der A-Skala (insb. niedrigere Besoldungsgruppen A4 bis A9 mit unterhaltsberechtigten Kindern) das verfassungsrechtliche Mindestabstandsgebot zur Grundsicherung nicht einhaelt. Anwendung neben `amtsangemessene-alimentation-bverfg` und `familienzuschlag-drittes-kind-bverfg`.

## 2. Eingaben

- Besoldungsgruppe und Stufe
- Anzahl der unterhaltsberechtigten Kinder
- Bundesland
- Datum der letzten Anpassung
- Vergleichsberechnung Grundsicherung (Regelbedarf, Wohnen, Heizung) im Haushalt

## 3. Ablauf / Checkliste

### a) Mindestabstand zur Grundsicherung
- Das BVerfG verlangt einen wirksamen Abstand zwischen der Besoldung der untersten Besoldungsgruppen und dem sozialhilferechtlichen Grundsicherungsniveau (gemessen am SGB II / SGB XII unter Beruecksichtigung von Regelbedarfen, Unterkunfts- und Heizkosten und Kinderbedarfen).
- Faustregel: ca. 15 Prozent oberhalb des Grundsicherungsniveaus. Im Einzelfall pruefen.

### b) Familienzuschlag für Mehrkinderfamilien
- Familienzuschlag für das dritte und jedes weitere Kind hat eine zentrale Rolle. Bei zu niedrigem Zuschlag verstoesst die Besoldung gegen Art. 33 Abs. 5 GG — siehe Schwester-Skill `familienzuschlag-drittes-kind-bverfg`.

### c) Geltendmachung zeitnah
- Wichtige BVerfG-Bedingung: Der Beamte muss seinen Anspruch zeitnah im laufenden Haushaltsjahr geltend machen (Widerspruch). Ohne zeitnahe Geltendmachung kein Nachzahlungsanspruch für vergangene Jahre.

### d) Verfahrenslage
- Widerspruch gegen die monatliche Bezuegemitteilung.
- Klage zum VG, ggf. Aussetzung und Vorlage nach Art. 100 Abs. 1 GG.
- Anschluss an Pilotverfahren ratsam.

## 4. Quellenpflicht

- Normen: Art. 33 Abs. 5, Art. 100 Abs. 1 GG; BBesG; Landesbesoldungsgesetze; SGB II / SGB XII (zur Grundsicherungsberechnung).
- Rspr.: BVerfG zur A-Besoldung — Quellenanker unten; konkrete Entscheidung in amtlicher oder freier Quelle prüfen.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Widerspruchsschrift mit Berechnungsanlage.
- Pruefraster Mindestabstandsgebot.

## 6. Verifizierte Quellenanker

- BVerfG, 05.05.2015 - 2 BvL 17/09 u.a.: R-Besoldung Sachsen-Anhalt; Parameterprüfung zur amtsangemessenen Alimentation.
- BVerfG, 04.05.2020 - 2 BvL 4/18: R-Besoldung Berlin; Mindestabstand und Alimentation.
- BVerfG, 04.05.2020 - 2 BvL 6/17 u.a.: kinderreiche Richterfamilien und Familienzuschlag.
- BVerfG, 17.09.2025 - 2 BvL 20/17 u.a.: Berliner A-Besoldung; Prekaritätsschwelle und Dreischritt.
- Seit der Föderalismusreform 2006 ist Landesbesoldung landesrechtlich zu prüfen; BBesG nur für Bund/Soldaten und fortgeltende Sonderlagen.
- Für Stufen, Auslandsdienstbezüge, Erschwerniszulagen und Mehrarbeit zusätzlich aktuelle Spezialnormen live prüfen; die BVerfG-Linie ersetzt keine Fachnormprüfung.

## 7. Beispiel (Kurzfassung)

Polizeimeister A7 Stufe 4, Ehepartner ohne Erwerbseinkommen, vier Kinder. Skill liefert Berechnung Grundsicherungsniveau im Vergleich zu Brutto- und Nettobesoldung, Widerspruchsentwurf mit zeitnaher Geltendmachung.

---

## Skill: `beurteilungsbeitrag-heilung-maengel`

_Skill zur rechtlichen Pruefung von Beurteilungsbeitraegen Dritter im beamtenrechtlichen Beurteilungsverfahren. Klaert wer einen Beitrag liefern muss wann ein fehlender Beitrag die Beurteilung rechtswidrig macht und wie eine fehlende Heranziehung im Verfahren geheilt werden kann. Behandelt die Kon..._

# Beurteilungsbeitrag — Pflicht, Mangel, Heilung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: Widerspruch 1 Monat (VwGO § 70), Disziplinarverfahren nach BDG, Beihilfeantrag i.d.R. 1 Jahr, Beförderung-Auswahlentscheidung Bewährungsfristen.
- Tragende Normen verifizieren: BeamtStG §§ 3, 4, 21-25, 30, 33-41, BBG, BBesG, BeamtVG, LBG der Länder, GG Art. 33 Abs. 4 und 5, BDG, LDG, VwGO §§ 126 ff., LPVG/BPersVG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Dienstherr (Bund/Land/Kommune), Beamter, Dienstvorgesetzter, Personalrat, Personalvertretung, Disziplinarvorgesetzter, VG, OVG, BVerwG (2. Senat).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Ernennungsurkunde, dienstliche Beurteilung, Konkurrentenklage, Disziplinarverfügung, Versorgungsbescheid, Beihilfeantrag, Personalratsentscheidung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## 1. Zweck und Anwendungsfall

Skill für Mandanten, deren dienstliche Beurteilung ohne Einbindung eines frueheren oder parallelen Dienstvorgesetzten erstellt wurde, obwohl dieser im Beurteilungszeitraum die Leistung des Beamten beobachten konnte. Typisch: Abordnung in andere Behörde, Wechsel des Vorgesetzten, Erziehungs- oder Pflegezeit, Auslandsverwendung.

## 2. Eingaben

- Verlauf des Beurteilungszeitraums (Verwendungen, Vorgesetzte)
- Beurteilungsrichtlinie / VwV des Dienstherrn
- Beurteilung selbst (Volltext mit Begruendungsteil)
- Vermerk ueber Beurteilungsgespraech
- Hinweise auf Heranziehung oder Nichtheranziehung von Drittbeitraegen

## 3. Ablauf / Checkliste

### a) Wer hat Beurteilungsbeitraege zu liefern?
- Frueherer Dienstvorgesetzter bei Versetzung waehrend des Beurteilungszeitraums.
- Vorgesetzter der Abordnungsbehoerde.
- Vorgesetzter bei Teilzeit-Mehrfachverwendung.
- Bei Personalrats- oder Gleichstellungsfreistellung: kein Beitrag aus dieser Taetigkeit, aber Beruecksichtigung der Tatsache der Freistellung mit Benachteiligungsverbot.

### b) Form
- Schriftlicher Beitrag, mit Unterschrift des Beitragenden, dem Beurteiler vor Erstellung der Beurteilung vorzulegen, in der Personalakte zu dokumentieren.
- Beitrag muss zeitnah zum Beurteilungszeitraum gefertigt sein.

### c) Maengel und Heilung
- Fehlender Beitrag macht die Beurteilung in der Regel rechtswidrig.
- Heilung durch nachgeholten Beitrag und Neuerstellung oder ergaenzende Plausibilisierung der Beurteilung waehrend des laufenden Verfahrens nur unter engen Voraussetzungen — BVerwG-Rechtsprechung, konkret vor Zitat frei prüfen.
- Heilung nach Abschluss des Auswahlverfahrens grundsaetzlich nicht moeglich, wenn dadurch der Ausgang sich aendern koennte.

### d) Geltendmachung im Eilverfahren
- Mangel der Beurteilung ist Anordnungsanspruch im Konkurrenteneilantrag.
- Hilfsweise Antrag auf Anordnung der Neuerstellung der Beurteilung.

## 4. Quellenpflicht

- Normen: §§ 21, 22 BBG; § 18 BLV; einschlaegige Beurteilungsrichtlinien (BMI-VwV, Länder-VwV).
- Rspr.: BVerwG zur Funktion und Notwendigkeit von Beurteilungsbeitraegen — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Anfechtungsantrag gegen Beurteilung mit Begruendung.
- Schriftsatzbaustein "Anordnungsanspruch — Beurteilungsbeitragsmangel" für den Konkurrenteneilantrag.

## 6. Verifizierte Quellenanker

- Art. 33 Abs. 2 GG: Bestenauslese nach Eignung, Befähigung und fachlicher Leistung.
- Art. 74 Abs. 1 Nr. 27 GG und Art. 70 GG: Statusrechtliche Bundeskompetenz, Laufbahn/Besoldung/Versorgung der Länder grundsätzlich Landesrecht.
- BeamtStG und BBG immer nach Dienstherr trennen; Landesbeamtengesetz und Beurteilungsrichtlinien live prüfen.
- BVerwG, 11.10.2016 - 2 C 11.15 als verifizierter Anker zu Art. 33 Abs. 2 GG und Eignungsanforderungen bei Höchstaltersgrenzen.
- Für Spezialfragen der dienstlichen Beurteilung, Anlassbeurteilung, Binnendifferenzierung und Auswahlgespräch keine privaten Datenbankzitate verwenden; konkrete Rechtsprechung nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.

## 7. Beispiel (Kurzfassung)

Mandantin war im Beurteilungszeitraum 18 Monate abgeordnet. Der dortige Dienststellenleiter lieferte keinen Beitrag, der Heimatbeurteiler stuetzte sich allein auf eigene Eindruecke ueber den verbliebenen Zeitraum. Skill liefert Argument: Beurteilung ist rechtswidrig wegen fehlenden Beurteilungsbeitrags; Nachholung mit Neuerstellung erforderlich.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

