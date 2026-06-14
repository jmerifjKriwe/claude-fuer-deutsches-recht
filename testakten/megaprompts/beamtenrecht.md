# Megaprompt: beamtenrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 178 Skills (gekuerzt fuer Chat-Fenster) des Plugins `beamtenrecht`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Einstieg, Kaltstart und Fallrouting im Beamtenrecht-Plugin: klärt Status, Dienstherr, Bundesland, Frist, Ziel, Unterlage…
2. **dienstgericht-richter-disziplinar-63-drig** — Skill zum Dienstgericht fuer Richter nach §§ 61 ff. DRiG und den Landesrichtergesetzen. Klaert die Zustaendigkeit des Di…
3. **schwerbehinderte-bewerber-165-sgb-9** — Skill zur Pruefung der Pflichten oeffentlicher Arbeitgeber bei Bewerbungen schwerbehinderter Menschen nach § 165 SGB IX.…
4. **altersteilzeit-93-bbg-blockmodell** — Skill zur Altersteilzeit der Beamten nach § 93 BBG bzw. § 9 BeamtStG i.V.m. den Landesregelungen. Klaert die zwei Modell…
5. **anforderungsprofil-konstitutiv** — Skill zur Unterscheidung konstitutives Anforderungsprofil und deklaratorisches Anforderungsprofil bei der beamtenrechtli…
6. **auswahlgespraech-dokumentationspflicht** — Skill zu Anforderungen an strukturierte Auswahlgespraeche und Assessment Center im beamtenrechtlichen Auswahlverfahren. …
7. **beihilfe-heilbehandlung-ausland** — Skill zur beamtenrechtlichen Beihilfefaehigkeit von Heilbehandlung im Ausland nach BBhV und den Landesbeihilfeverordnung…
8. **beihilfe-implantatfaehige-hoergeraete** — Skill zur Beihilfefaehigkeit von hochwertigen Hilfsmitteln wie implantatfaehigen Hoergeraeten Cochlea-Implantaten elektr…

---

## Skill: `kaltstart-triage`

_Einstieg, Kaltstart und Fallrouting im Beamtenrecht-Plugin: klärt Status, Dienstherr, Bundesland, Frist, Ziel, Unterlagen, Anfänger-/Profi-Modus und schlägt passende Fachmodule vor._

# Allgemein

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Beamtenrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

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

## Skill: `dienstgericht-richter-disziplinar-63-drig`

_Skill zum Dienstgericht fuer Richter nach §§ 61 ff. DRiG und den Landesrichtergesetzen. Klaert die Zustaendigkeit des Dienstgerichts in Statussachen Disziplinarsachen und Versetzungs- und Pruefverfahren die Besetzung des Spruchkoerpers mit beruflichen und ehrenamtlichen Richtern und das Verfahrensrecht in Anlehnung an das BDG. Behandelt die Konstellationen Verfahren gegen Disziplinarmassnahmen Pruefung der richterlichen Unabhaengigkeit nach § 26 DRiG und Antrag auf Aufhebung der Geschaeftsverteilung. Liefert Pruefraster und Schriftsatzbausteine._

# Dienstgericht fuer Richter

## 1. Zweck und Anwendungsfall

Skill fuer Richter, die ein Verfahren beim Dienstgericht fuehren oder verteidigen wollen. Anwendung typisch bei Disziplinarsachen, Pruefverfahren wegen Eingriffen in die richterliche Unabhaengigkeit (§ 26 DRiG) oder Streit um die Geschaeftsverteilung.

## 2. Eingaben

- Beanstandeter Vorgang (Disziplinarverfuegung, Massnahme der Dienstaufsicht, Geschaeftsverteilungsbeschluss)
- Statusamt (Bundes- oder Landesrichter)
- Spruchkoerper-Besetzung
- Antrag im Detail

## 3. Ablauf / Checkliste

### a) Zustaendigkeit
- § 62 DRiG: Dienstgericht des Bundes fuer Bundesrichter, Dienstgerichte der Laender fuer Landesrichter.
- § 78 DRiG: Disziplinarsachen, Statussachen, Pruefung nach § 26 DRiG.

### b) Besetzung
- Dienstgericht: Drei Berufsrichter, zwei ehrenamtliche Richter (in Disziplinarsachen) bzw. spezifische Besetzung in Statussachen.

### c) Pruefung nach § 26 DRiG
- Pruefung von Massnahmen der Dienstaufsicht, ob die richterliche Unabhaengigkeit beruehrt wird; Pruefraster: Massnahme, Beruehrung der Unabhaengigkeit, Folgen.
- Antrag auf Pruefung in Frist (regelmaessig 3 Monate nach Massnahme).

### d) Disziplinarverfahren
- Verfahren nach BDG in Anlehnung; spezifische Besonderheiten in DRiG und Landesrichtergesetzen.

### e) Geschaeftsverteilung
- Antrag auf Pruefung der Geschaeftsverteilung beim Dienstgericht — siehe Schwester-Skill `geschaeftsverteilung-richter-21e-gvg`.

## 4. Quellenpflicht

- Normen: §§ 26, 61 bis 78 DRiG; Landesrichtergesetze; BDG (entsprechend).
- Rspr.: BGH zum Dienstgericht des Bundes; OLG-Dienstgerichte der Laender — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Antrag an das Dienstgericht.
- Pruefraster nach § 26 DRiG.

## 6. Verifizierte Quellenanker

- Art. 97 GG, Art. 98 GG, Art. 101 GG, § 21e GVG sowie DRiG §§ 25, 26, 39, 61 ff. als Kernnormen.
- BVerfG, 20.09.2016 - 2 BvR 2453/15: Bundesrichterwahl, Art. 95 Abs. 2 GG und Bindung an Art. 33 Abs. 2 GG.
- BVerfG, 11.11.2021 - 2 BvR 1473/20: Dienstaufsicht, Erledigungsdruck und Grenze bei objektiv nicht bewältigbarem Pensum.
- BVerfG, 22.03.2018 - 2 BvR 780/16: Richter auf Zeit und richterliche Unabhängigkeit im organisationsrechtlichen Kontext.
- EuGH, 24.06.2019 - C-619/18 und EuGH, 19.11.2019 - C-585/18, C-624/18, C-625/18 als EU-rechtliche Anker der Justizunabhängigkeit.
- Landesrichterrecht, Dienstgerichte der Länder und Präsidialratsrecht immer landesrechtlich live prüfen.

## 7. Beispiel (Kurzfassung)

Mandant Vorsitzender Richter, Praesidium hat ihm anhaengiges Verfahren entzogen mit Hinweis auf Belastungssituation. Skill liefert Pruefung nach § 26 DRiG und Antrag beim Dienstgericht.

---

## Skill: `schwerbehinderte-bewerber-165-sgb-9`

_Skill zur Pruefung der Pflichten oeffentlicher Arbeitgeber bei Bewerbungen schwerbehinderter Menschen nach § 165 SGB IX. Klaert Einladungspflicht zum Vorstellungsgespraech Pruefpflicht bei interner Besetzung Beruecksichtigung der Eignung Sonderfall offensichtlich fachlich ungeeignet Beteiligung der Schwerbehindertenvertretung nach §§ 178 179 SGB IX und die Indizwirkung von Verstoessen im AGG-Entschaedigungsprozess. Liefert Pruefraster Schriftsatzbausteine fuer Eilantrag Entschaedigungsforderung und Konkurrentenklage._

# Schwerbehinderte Bewerber im oeffentlichen Dienst — § 165 SGB IX

## 1. Zweck und Anwendungsfall

Skill fuer schwerbehinderte oder gleichgestellte Bewerber im oeffentlichen Dienst. Klaert die zwingenden Verfahrenspflichten der oeffentlichen Arbeitgeber, insbesondere die Einladungspflicht und das Zusammenwirken mit Schwerbehindertenvertretung und Gleichstellungsbeauftragten.

## 2. Eingaben

- Schwerbehindertenausweis oder Gleichstellungsbescheid
- Datum der Bewerbung
- Stellenausschreibung
- Akteneinsicht (Auswahlvermerk)
- Information ueber Beteiligung der Schwerbehindertenvertretung
- Absageschreiben

## 3. Ablauf / Checkliste

### a) Einladungspflicht
- § 165 Satz 3 SGB IX: Oeffentliche Arbeitgeber muessen schwerbehinderte Bewerber zum Vorstellungsgespraech einladen, es sei denn, die fachliche Eignung fehlt offensichtlich. "Offensichtlich" eng auszulegen.
- Bei Konzentrationsbewerbungen ueber zentrale Stellen sind die Pflichten nicht gemindert.

### b) Interne Besetzung
- § 165 Sätze 1 und 2 SGB IX: vor externer Ausschreibung Pruefpflicht, ob die Stelle intern mit schwerbehinderten Personen besetzt werden kann (Vermittlungsvorschlag der Bundesagentur fuer Arbeit; interner Aufruf).

### c) Beteiligung Schwerbehindertenvertretung
- § 178 Abs. 2 SGB IX: Unterrichtungs- und Anhoerungsrecht in allen Angelegenheiten, die Schwerbehinderte betreffen, einschliesslich Bewerbungen.
- § 179 SGB IX Behinderungen der Vertrauensperson sanktioniert.
- Verstoss = Verfahrensfehler mit Indizwirkung fuer Diskriminierung.

### d) Eignung
- Schwerbehinderung als solche ist kein Eignungsmangel.
- Eignungsdefizit ist konkret und nachvollziehbar zu begruenden.

### e) Folgen von Verstoessen
- AGG-Entschaedigungsanspruch wegen vermuteter Diskriminierung (§ 22 AGG, § 15 Abs. 2 AGG).
- Bewerbungsverfahrensanspruch verletzt; Anfechtung der Auswahlentscheidung; Konkurrenteneilantrag.

## 4. Quellenpflicht

- Normen: §§ 151, 165, 178, 179 SGB IX; §§ 1, 6, 15, 22 AGG; Art. 33 Abs. 2 GG.
- BAG zu § 165 SGB IX (frueher § 82 SGB IX) — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Pruefraster Verfahrenspflichten oeffentlicher Arbeitgeber.
- AGG-Entschaedigungsschreiben.
- Konkurrenteneilantrag.

## 6. Verifizierte Quellenanker

- Art. 33 Abs. 2 GG: Bestenauslese nach Eignung, Befähigung und fachlicher Leistung.
- Art. 74 Abs. 1 Nr. 27 GG und Art. 70 GG: Statusrechtliche Bundeskompetenz, Laufbahn/Besoldung/Versorgung der Länder grundsätzlich Landesrecht.
- BeamtStG und BBG immer nach Dienstherr trennen; Landesbeamtengesetz und Beurteilungsrichtlinien live prüfen.
- BVerwG, 11.10.2016 - 2 C 11.15 als verifizierter Anker zu Art. 33 Abs. 2 GG und Eignungsanforderungen bei Höchstaltersgrenzen.
- Für Spezialfragen der dienstlichen Beurteilung, Anlassbeurteilung, Binnendifferenzierung und Auswahlgespräch keine privaten Datenbankzitate verwenden; konkrete Rechtsprechung nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.

## 7. Beispiel (Kurzfassung)

Mandant Grad der Behinderung 60 bewirbt sich auf A12-Stelle im Bundesministerium. Wird nicht zum Vorstellungsgespraech eingeladen; Absage ohne Begruendung. Skill liefert Indizienanalyse, AGG-Entschaedigungsschreiben mit Zwei-Monats-Frist und Begruendung des Anordnungsanspruchs fuer Eilantrag.

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

Skill für Beamte ab dem 55. Lebensjahr, die über Altersteilzeit den gleitenden Uebergang in den Ruhestand wuenschen.

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
- Teilzeitmodell: gleichmäßige Reduzierung der Arbeitszeit über die gesamte Altersteilzeit.
- Blockmodell: Arbeitsphase mit voller Arbeitszeit und anschliessende Freistellungsphase.

### c) Bezuege
- Bezuege betragen in der Regel 80 v. H. der Bezuege der entsprechenden Vollzeitbeschaeftigung (Altersteilzeitzuschlag).
- Auswirkungen auf Beihilfe und Heilfürsorge prüfen.

### d) Ruhegehaltfaehigkeit
- Altersteilzeit ist anteilig ruhegehaltfaehig.

### e) Versorgungsabschlag
- Beim Eintritt in den Ruhestand nach Altersteilzeit kein Versorgungsabschlag, soweit die Altersteilzeit bis zur Regelaltersgrenze laeuft. Bei vorzeitigem Antragsruhestand greift Skill `versorgungsabschlag-14-beamtvg`.

### f) Änderungen waehrend der Altersteilzeit
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
- Altersteilzeitzuschlagsverordnung Bund und landesrechtliche Äquivalente.
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
- Disziplinarmassnahme nach BDG/LDG am Verhältnismäßigkeitsgrundsatz messen; Entfernung erfordert schwere Verfehlung.
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
- Konstitutiv (auch: zwingend) ist ein Merkmal, dessen Fehlen ohne weitere Prüfung zum Ausschluss fuehrt. Es engt die Vergleichsgruppe ein.
- Deklaratorisch ist ein Merkmal, das nur die Auslegung der Beurteilung leitet und bei der Bewertung gewichtet wird.

### b) Rechtfertigungsanforderung
- Ein konstitutives Anforderungsprofil ist nur zulässig, wenn es sachlich gerechtfertigt ist und einen Bezug zur konkreten Aufgabenwahrnehmung hat (BVerwG-Rechtsprechung, konkret vor Zitat frei prüfen).
- Es darf nicht auf einen einzelnen Wunschbewerber zugeschnitten sein. Ein Zuschnittsverdacht ergibt sich aus Indizien (sehr enges Kriterienbuendel, Identitaet mit Vita des Wunschbewerbers, fehlende Vorgeschichte für solche Anforderungen).

### c) Folge eines unzulaessigen Profils
- Die Auswahlentscheidung ist rechtswidrig; das gesamte Verfahren ist neu zu durchlaufen.
- Bei laufendem Auswahlverfahren: einstweilige Anordnung gegen Ernennung des Konkurrenten — Skill `konkurrentenklage-einstweiliger-rechtsschutz`.

### d) Schutz des Wettbewerbsverfahrens
- Auch wenn ein einzelnes Merkmal entfaellt, bleibt der Bestenauslese-Grundsatz erhalten; die uebrigen Anforderungen sind weiter prüfen.

## 4. Quellenpflicht

- Normen: Art. 33 Abs. 2 GG; § 9 BBG; § 9 BeamtStG; §§ 32 ff. BLV.
- Rspr.: BVerwG zum Anforderungsprofil — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Prüfvermerk: Tabelle "Merkmal — konstitutiv ja oder nein — Begruendung — Sachzusammenhang — Rechtsfolge".
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
- Disziplinarmassnahme nach BDG/LDG am Verhältnismäßigkeitsgrundsatz messen; Entfernung erfordert schwere Verfehlung.
- Konkurrentenstreitverfahren BVerwG 2 C 4.18: Bewerbungsverfahrensanspruch Art. 33 Abs. 2 GG sichern, vor Ernennung.

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
- Wesentliche Aussagen sind so zu dokumentieren, dass eine gerichtliche Kontrolle möglich ist. Reine Punkthebel ohne Begruendung genügen nicht.
- Die Dokumentation muss im Auswahlvermerk verarbeitet werden.

### d) Befangenheit
- Mitwirkung eines mit dem ausgewaehlten Konkurrenten in besonderer Naehe stehenden Kommissionsmitglieds (z. B. langjaeriger Vorgesetzter) ist zu prüfen; § 21 VwVfG entsprechend.
- Nichtbestellung einer Schwerbehindertenvertretung oder Gleichstellungsbeauftragten, wenn Pflichtteilnahme bestand, ist Verfahrensfehler.

### e) Beweislast
- Im Eilverfahren genuegt Glaubhaftmachung der Verfahrensfehler. Das Gericht zieht den Verwaltungsvorgang bei.

## 4. Quellenpflicht

- Normen: Art. 33 Abs. 2 GG; § 9 BBG; §§ 32 ff. BLV; § 21 VwVfG; § 178 ff. SGB IX (Schwerbehindertenvertretung).
- Rspr.: BVerwG zur Bedeutung und Grenzen des Auswahlgespraechs — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Prüfraster Verfahrensfehler.
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

Skill für Beihilfeberechtigte, die eine Behandlung im Ausland in Anspruch nehmen wollen oder genommen haben und deren Erstattungsfaehigkeit klären wollen.

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
- Bei medizinischen Notfaellen im Ausland keine Vorabgenehmigung erforderlich; Erstattung ohne Begrenzung auf Inlandsniveau möglich, soweit nachvollziehbar notwendig.

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
- Prüfraster Beihilfefaehigkeit im Ausland.

## 6. Verifizierte Quellenanker

- Richtlinie 2011/24/EU vom 09.03.2011 (Patientenrechte in der grenzueberschreitenden Gesundheitsversorgung).
- EuGH, 23.10.2003 - C-56/01 (Inizan); EuGH, 16.05.2006 - C-372/04 (Watts); EuGH, 19.04.2007 - C-444/05 (Stamatelaki).
- BBhV; landesrechtliche Beihilfeverordnungen; Auslandsdienstkrankenversicherungsregelungen.
- BVerwG zur Beihilfefaehigkeit von Auslandsbehandlungen — Datum und Az vor Zitat live verifizieren.

## 7. Beispiel (Kurzfassung)

Mandant lässt Hueftgelenkoperation in einer Wiener Klinik durchfuehren; Rechnung 18.500 Euro. Skill liefert Prüfung der Beihilfefaehigkeit nach Patientenrichtlinie und Begrenzung auf Inlandsniveau.

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
- Antrag auf Erstattung in voller Höhe.

## 6. Verifizierte Quellenanker

- BBhV insbesondere Anlage 6 (Hilfsmittel und Festbetraege); landesrechtliche Beihilfeverordnungen mit eigenen Hilfsmittelverzeichnissen.
- Festbetragsregelung als Regelgrenze; medizinische Notwendigkeit als Maßstab für beihilfefaehige Mehrkosten.
- BVerwG zur Beihilfefaehigkeit hochwertiger Hilfsmittel und zur Prüfung medizinischer Notwendigkeit — Datum und Az vor Zitat live verifizieren.
- Hilfsmittelrichtlinie des G-BA und einschlaegige HNO- und audiologische Leitlinien als Begruendungsgrundlage.

## 7. Beispiel (Kurzfassung)

Mandant beidseitige Schwerhoerigkeit; HNO empfiehlt Geraet mit Bluetooth und Spezialakustik für Berufstaetigkeit als Richter (Verhandlung in großen Saelen). Kostenvoranschlag 5.800 Euro, Festbetrag 1.500 Euro. Skill liefert Widerspruch mit Begruendung der Mehrkosten als medizinisch notwendig.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

