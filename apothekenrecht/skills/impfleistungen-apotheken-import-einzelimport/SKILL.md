---
name: impfleistungen-apotheken-import-einzelimport
description: "Impfleistungen Apotheken Import Einzelimport im Plugin Apothekenrecht: prüft konkret Impfleistungen in Apotheken, Import Einzelimport § 73 AMG, Inhaberwechsel Kauf Apothekenbetrieb. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Impfleistungen Apotheken Import Einzelimport

## Arbeitsbereich

Dieser Skill behandelt **Impfleistungen Apotheken Import Einzelimport** als zusammenhängenden Arbeitsgang im Plugin Apothekenrecht. Im Mittelpunkt steht die Prüfung von Impfleistungen in Apotheken, Import Einzelimport § 73 AMG, Inhaberwechsel Kauf Apothekenbetrieb. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `impfleistungen-in-apotheken` | Impfleistungen in Apotheken: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `import-einzelimport-73-amg` | Import Einzelimport § 73 AMG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `inhaberwechsel-kauf-apothekenbetrieb` | Inhaberwechsel Kauf Apothekenbetrieb: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |

## Arbeitsweg

- Rolle und Ziel im Super-Plugin für Apothekenrecht: Betriebserlaubnis, ApBetrO, Versand, E-Rezept, BtM, Retaxation, Aufsicht und Compliance klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `impfleistungen-in-apotheken`

**Fokus:** Impfleistungen in Apotheken: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Impfleistungen in Apotheken

## Fachkern: Impfleistungen in Apotheken
- **Spezialgegenstand:** Impfleistungen in Apotheken. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Impfleistungen in Apotheken** im Bereich **Apothekenrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Apothekenrecht zwischen ApoG, ApBetrO, AMG, AMPreisV, SGB V, HWG, BtMG, Datenschutz, Aufsicht, Versandhandel, E-Rezept und Apothekenpraxis.

## Startfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfschema, Risikoampel, Fragenliste, Dokumentenanforderung, Entwurfsbausteine und nächster Handlungsschritt. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

## 2. `import-einzelimport-73-amg`

**Fokus:** Import Einzelimport § 73 AMG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Import Einzelimport § 73 AMG

## Fachkern: Import Einzelimport § 73 AMG
- **Spezialgegenstand:** Import Einzelimport § 73 AMG. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Einzelimport von Arzneimitteln aus dem Ausland gemäss § 73 Abs. 3 AMG. Anwendungsfall: ein in Deutschland nicht zugelassenes Arzneimittel ist im Einzelfall medizinisch erforderlich (z. B. seltene Erkrankungen, Engpässe, Spezialpräparate). Apotheke darf das Präparat im individuellen Einzelfall auf ärztliche Verschreibung importieren und abgeben. Reimport (§ 129 SGB V, Bonusregelung) ist abzugrenzen.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Patient hat seltenes Arzneimittel, das in D nicht zugelassen, im Ausland aber verfügbar ist.
- Engpass eines in D zugelassenen Arzneimittels — § 79 AMG Versorgungsmangel parallel prüfen.
- Onkologisches Medikament, das in D noch nicht zugelassen, aber in den USA verkehrsfähig ist.
- Aufsicht beanstandet eingerichtete Import-Pipeline als Quasi-Versandhandel.

Eingaben:
- Ärztliche Verschreibung mit Begründung (Indikation, Erfolglosigkeit Inland-Therapie).
- Lieferantennachweis aus Herkunftsland (Apotheke, Grosshandel, AM-Hersteller).
- Verkehrsfähigkeitsnachweis (Zulassung im Herkunftsland).
- Patientenanamnese.
- Krankenkassen-Kostenzusage (sofern beantragt).

## Rechtlicher Rahmen

- **§ 73 Abs. 1 AMG:** Grundsätzliches Verbringungsverbot.
- **§ 73 Abs. 3 AMG:** Einzelimport durch Apotheke auf ärztliche Verschreibung — nur in geringen Mengen, bezogen auf den individuellen Patientenbedarf.
- **§ 73 Abs. 4 AMG:** Klinische Prüfung / Compassionate Use (vom Anwender zu verifizieren — Sonderverordnung).
- **§ 21 AMG:** Zulassungspflicht in D.
- **§ 79 AMG:** Versorgungsmangel-Befreiung durch BMG (Sonderregelung).
- **AM-HandelsVO (AMHandV)** für Import-Dokumentation.
- BfArM-Bekanntmachungen zu Einzelimport.
- BSG, staend. Rspr. zur Erstattung importierter Arzneimittel durch GKV.

## / Schritt für Schritt

1. **Indikationsprüfung:** Erfolgloser Inlandstherapieversuch dokumentiert; oder nicht zugelassen, aber dringend benötigt.
2. **Verkehrsfähigkeit Herkunftsland:** Zulassungsnachweis aus EU-Mitgliedstaat (FDA/Schweiz/UK), Übersetzung in Deutsch sicherheitshalber.
3. **Bezug:** Apotheke bestellt direkt bei ausländischer Apotheke oder ausländischem Hersteller. Grosshandelsbezug nur bei Hersteller mit Vertriebslizenz.
4. **Menge:** Nur individueller Patientenbedarf, nicht auf Lager. Mengenbeschränkung beachten — keine Vorratshaltung.
5. **Dokumentation:** Rezept, Lieferschein, Apothekensystem-Vermerk, Beratungsprotokoll.
6. **Erstattung:** GKV vorab Kostenzusage einholen; sonst kein Erstattungsanspruch.
7. **Zollabwicklung:** Bei Drittstaat-Import Zollformalitäten; AMHandV beachten.
8. **Beratung Patient:** Anwendung, Nebenwirkungen — ggf. Beipackzettel-Übersetzung.

## Trade-off-Matrix

| Fallgruppe | § 73 III AMG | Reimport (§ 129 SGB V) | Versorgungsmangel § 79 AMG |
|---|---|---|---|
| Erforderlichkeit | individueller Bedarf | gleiches Arzneimittel günstiger | nationaler Engpass |
| Zulassung in D | nein | ja, gleiches Präparat | ja |
| Erstattung GKV | Einzelfallzusage | grds. ja, mit Bonus | über BMG-Anordnung |
| Risiko Apotheke | mittel (Doku) | gering | gering |
| Lieferquelle | jede EU/Drittland | EU-Reimporteur | je nach BMG |

## Praxistipps

- Reimport (Bonus-Reimport § 129 SGB V) ist **kein** § 73 III AMG-Fall — gleiches Präparat, parallele Vertriebswege.
- Kostenzusage GKV stets vor Bestellung anfordern; sonst Risiko, dass Apotheke auf Kosten sitzenbleibt.
- Bei Drittstaaten-Import (USA, Schweiz) Vermerk auf Echtheit + Zulassung des Herkunftslandes — gefälschte Arzneimittel sind Risiko.
- Cannabis-Sonderfall: BfArM-Bekanntmachungen prüfen; Einzelimport von Cannabis-Blüten ist eigenes Regime.
- Hospizmedizin, seltene Erkrankungen: Patientenorganisationen führen oft Bezugslisten anerkannter Lieferapotheken.

## Mustertexte

### Antrag Kostenzusage an Krankenkasse (Auszug)
"Sehr geehrte Damen und Herren, hiermit beantragen wir für unsere Versicherte [Initialen, Geb.-Datum] die Kostenzusage zum Einzelimport des Arzneimittels [Name, Stärke, Menge] gemäss § 73 Abs. 3 AMG. Indikation: [Krankheit, ICD-10]. Inland-Therapieversuche waren erfolglos / nicht möglich, da kein zugelassenes Präparat verfügbar ist (vgl. Ablehnung [Datum] / ärztliches Gutachten Anlage [Nr.]). Verkehrsfähigkeit im Herkunftsland: [Land, Zulassungsnummer]. Wir bitten um Kostenzusage bis [Frist], um die Versorgung sicherzustellen."

### Dokumentation Einzelimport (Vorlage)
"Patient: [Initialen] / Rezept-Nr.: [...] / Arzneimittel: [...] / Herkunftsland + Hersteller: [...] / Bezugsapotheke / Grosshandel: [...] / Importdatum: [...] / Menge: [individuell] / Indikation: [ICD-10] / Kostenzusage GKV: [Az + Datum] / Abgabedatum: [...] / Apotheker:in: [...]"

## Typische Fehler

- Vorratshaltung importierter Präparate — Anschein eines Quasi-Versandhandels, Aufsicht beanstandet.
- Kostenzusage nicht eingeholt; Patient zahlt privat oder Apotheke bleibt auf Kosten sitzen.
- Verkehrsfähigkeit Herkunftsland nicht dokumentiert — bei späterer Kontrolle nicht belegbar.
- BtM-Einzelimport (eigene Regelung) nicht beachtet — Sonderverfahren über Bundesopiumstelle erforderlich.
- Cannabis-Einzelimport nicht über BfArM angemeldet — Sonderregime ignoriert.

## Querverweise

- `arzneimittelabgabe-verschreibungspflicht` (allgemein)
- `lieferengpaesse-austausch-dokumentation` (Engpass)
- `cannabis-medizinalcannabis-abgabe-dokumentation` (Cannabis-Sonderfall)
- `arzneimittelrisiken-rueckruf-chargenrueckverfolgung` (Sicherheit)
- `preisbindung-arzneimittel-ampreisv` (Preisrelevanz)
- `rechnung-retaxation-krankenkasse` (GKV-Abrechnung)

## Quellen Stand 06/2026

- AMG §§ 21, 73, 79; AMHandV.
- BfArM und Bundesopiumstelle — Bekanntmachungen zum Einzelimport (vom Anwender zu verifizieren).
- BSG, staend. Rspr. zur Kostenübernahme nicht zugelassener Arzneimittel.
- ABDA-Hinweise zum Einzelimport (vom Anwender zu verifizieren).
- Zollvorschriften für Drittstaaten-Import (BfArM-Merkblatt).

## 3. `inhaberwechsel-kauf-apothekenbetrieb`

**Fokus:** Inhaberwechsel Kauf Apothekenbetrieb: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Inhaberwechsel Kauf Apothekenbetrieb

## Fachkern: Inhaberwechsel Kauf Apothekenbetrieb
- **Spezialgegenstand:** Inhaberwechsel Kauf Apothekenbetrieb. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Inhaberwechsel Kauf Apothekenbetrieb** im Bereich **Apothekenrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Apothekenrecht zwischen ApoG, ApBetrO, AMG, AMPreisV, SGB V, HWG, BtMG, Datenschutz, Aufsicht, Versandhandel, E-Rezept und Apothekenpraxis.

## Startfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfschema, Risikoampel, Fragenliste, Dokumentenanforderung, Entwurfsbausteine und nächster Handlungsschritt. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?
