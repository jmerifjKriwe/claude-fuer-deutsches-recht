---
name: kompendium-19-richtlinien-monitor-bis-spezial-bdsg-tatbest
description: "datenschutzrecht: Konsolidiertes Skill-Kompendium 19; bündelt 10 frühere Spezialskills (richtlinien-monitor, ropa-art-30-controller-deutsch-vorlage, ropa-art-30-dsgvo-grundlagen, ropa-bdsg-besondere-art-9-categories, ropa-en-controller-template und 5 weitere) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 19 - datenschutzrecht

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `richtlinien-monitor` | Datenschutzrichtlinien und Unternehmensanweisungen auf Aktualitaet und Konformität monitoren. Art. 24 32 DSGVO TOMs §§ 4 ff. BDSG. Prüfraster: Richtlinienbestand Aenderungsbedarf neue Verarbeitungstätigkeiten gesetzliche Neuerungen Umsetzungsstatus. Output: Monitoring-Bericht Aenderungsliste. Abgrenzung: nicht für erstmalige Richtlinien-Erstellung. |
| `ropa-art-30-controller-deutsch-vorlage` | Vollvorlage fuer das Verzeichnis von Verarbeitungstaetigkeiten des Verantwortlichen nach Art. 30 Abs. 1 DSGVO. Tabellenstruktur mit allen sieben Mindestinhalten, ausgefuelltes Beispiel fuer Personalverwaltung, Mandantenakte, Kontaktformular, CRM. Direkt nutzbare Vorlage fuer Kanzleien und Unternehmen. |
| `ropa-art-30-dsgvo-grundlagen` | Grundlagen des Verzeichnisses von Verarbeitungstaetigkeiten nach Art. 30 DSGVO. Anwendungsbereich, Schwellenwert, Mindestinhalte Controller und Processor, Verhaeltnis zu § 70 BDSG, Vorlagepflicht gegenueber der Aufsichtsbehoerde. Einstiegs-Skill fuer das Records of Processing Activities (RoPA). |
| `ropa-bdsg-besondere-art-9-categories` | RoPA-Besonderheiten bei besonderen Datenkategorien nach Art. 9 DSGVO (Gesundheit, biometrische Daten, Religion, Gewerkschaftszugehoerigkeit), bei Beschaeftigtendaten § 26 BDSG und strafrechtlichen Verurteilungen Art. 10 DSGVO. Erhoehte Anforderungen an Zweckbestimmung, Erforderlichkeit, Rechtsgrundlage und TOMs. |
| `ropa-en-controller-template` | Full English-language template for the Records of Processing Activities (RoPA) of the controller under Article 30(1) GDPR. Seven mandatory contents, cover sheet, three worked examples (HR, client files, CRM with US sub-processor), and a versioning footer. Suitable for German law firms with international clients. |
| `ropa-en-processor-template` | Full English-language template for the Records of Processing Activities (RoPA) of the processor under Article 30(2) GDPR. Four mandatory contents, controller list, processing categories, third-country transfers, sub-processor annex. For hosting providers, payroll, IT outsourcing, and cloud vendors with German clients. |
| `ropa-fuer-ki-anwendungen-besonderheiten` | Besonderheiten des Verzeichnisses von Verarbeitungstaetigkeiten bei KI-Anwendungen: Trainingsdatensaetze, Inferenz, RAG, Prompt-Logs, Fine-Tuning, Vector Stores, automatisierte Entscheidungen (Art. 22 DSGVO), Bezug zur KI-Verordnung. Mit Spaltenerweiterungen und Beispielen fuer LLM-API-Nutzung, Co-Pilot-Tools und KI-gestuetzte Bewerberauswahl. |
| `ropa-konzernumlauf-und-multi-entity` | Verzeichnis von Verarbeitungstaetigkeiten in Konzern- und Multi-Entity-Strukturen. Konzernklausel-Mythos, Rollenverteilung (Verantwortlicher gemeinsam Verantwortlich Auftragsverarbeiter), zentrale vs. dezentrale Pflege, Intercompany-Datenfluesse, BCR-Verweis. Mit Strukturskizze und Vorlage fuer Master-RoPA und Entity-Anhaenge. |
| `spezial-auskunft-behoerden-gericht-und-registerweg` | Auskunft: Behörden-, Gerichts- oder Registerweg im Plugin datenschutzrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-bdsg-tatbestand-beweis-und-belege` | Bdsg: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin datenschutzrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `richtlinien-monitor`

**Frühere Beschreibung:** Datenschutzrichtlinien und Unternehmensanweisungen auf Aktualitaet und Konformität monitoren. Art. 24 32 DSGVO TOMs §§ 4 ff. BDSG. Prüfraster: Richtlinienbestand Aenderungsbedarf neue Verarbeitungstätigkeiten gesetzliche Neuerungen Umsetzungsstatus. Output: Monitoring-Bericht Aenderungsliste. Abgrenzung: nicht für erstmalige Richtlinien-Erstellung.

# Policy-Monitor – Drift-Monitoring Datenschutzerklärung

## Zweck

Zwei Modi: (1) **Sweep-Modus** – regelmäßiger Abgleich aller Datenschutz-Commitment-Flächen gegen aktuelle Verarbeitungspraxis, um Drift zu erkennen. (2) **Direkt-Modus** – für eine konkrete geplante Änderung prüfen, ob und wie die Datenschutzerklärung angepasst werden muss.

Typische Drifts: neue Tracking-Tool-Integration ohne Datenschutzerklärungsupdate, neuer Sub-AV ohne Empfängerlistenaktualisierung, verlängerte Speicherfristen ohne Ankündigung, neue Drittlandtransfers ohne Transfermechanismus in der Erklärung.

## Eingaben

- **Sweep-Modus:** Ausgabenordner aus `CLAUDE.md` (wo DSFAs, AVV-Reviews, Triage-Ergebnisse gespeichert sind), Datenschutzerklärungsquelle (URL oder Datei), Liste aktueller Verarbeitungstätigkeiten
- **Direkt-Modus:** Beschreibung der geplanten Änderung der Verarbeitungspraxis

## Ablauf – Sweep-Modus

1. **Commitment-Inventur.**
   Alle Datenschutz-Commitment-Flächen aus `CLAUDE.md` lesen:
   - Datenschutzerklärung (Haupt-URL / Dokument)
   - CMP / Cookie-Consent-Banner-Konfiguration
   - App-Store Privacy Labels
   - In-Produkt-Einwilligungsflows
   - Sektorspezifische Hinweise (TDDDG, KUG)

2. **Praxis-Inventur.**
   Aktuelle Verarbeitungspraxis aus Ausgaben des Plugins rekonstruieren:
   - Neueste AVV-Reviews (neue Sub-AVs, neue Drittlandtransfers)
   - Neueste DSFA-Ergebnisse (neue Verarbeitungstätigkeiten)
   - Neueste Triage-Ergebnisse (Rechtsgrundlagenänderungen)
   - Aus `CLAUDE.md` bekannte Systemliste und Drittlandsituation

3. **Drift-Analyse.**
   Für jede Commit-Fläche: Ist-Inhalt gegen Praxis-Inventur abgleichen.

   | Commit-Fläche | Praxis-Ist | Erklärung-Ist | Drift? | Schwere |
   |---|---|---|---|---|
   | Datenschutzerklärung – Empfänger | [aktuelle Liste] | [publizierte Liste] | Ja/Nein | 🔴/🟡/🟢 |
   | Cookie-Banner – Kategorien | [aktiv gesetzt] | [angekündigt] | Ja/Nein | … |
   | Speicherfristen | [tatsächlich] | [publiziert] | Ja/Nein | … |
   | Drittlandtransfer-Mechanismus | [aktuell] | [publiziert] | Ja/Nein | … |

4. **Drift-Klassifikation.**
   - 🔴 **Sofortiger Handlungsbedarf:** Verarbeitung erfolgt, die in der Erklärung nicht angekündigt ist → Informationspflicht-Verstoß Art. 13/14 DSGVO, potenziell rechtswidrige Verarbeitung.
   - 🟠 **Hoch:** Wesentliche Erweiterung des Verarbeitungsumfangs nicht reflektiert (z.B. neuer Zweck, neues Empfänger-Land).
   - 🟡 **Mittel:** Aktualisierung empfohlen, keine unmittelbare Rechtswidrigkeit (z.B. neue Formulierung genauer als nötig, aber nicht falsch).
   - 🟢 **Gering:** Kosmetische Anpassung, kein Handlungsdruck.

5. **Änderungsentwürfe.**
   Für jede 🔴- und 🟠-Drift: konkreten Textvorschlag für die Datenschutzerklärung formulieren (nicht als Meta-Kommentar, sondern als fertiger Erklärungstext).

6. **Sweep-Bericht.**
   Zusammenfassung: [N] Drifts, davon [N] 🔴, [N] 🟠, [N] 🟡; Änderungsvorschläge inline; Folgeaktionen.

## Ablauf – Direkt-Modus

1. Geplante Änderung der Verarbeitungspraxis beschreiben lassen.
2. Prüfen: Welche Art. 13/14 DSGVO-Pflichtinformationen sind betroffen?
   - Neue Datenkategorie → Art. 13 Abs. 1 lit. c DSGVO
   - Neuer Zweck → Art. 13 Abs. 1 lit. c DSGVO
   - Neuer Empfänger → Art. 13 Abs. 1 lit. e DSGVO
   - Neue Speicherfrist → Art. 13 Abs. 2 lit. a DSGVO
   - Neues Drittland → Art. 13 Abs. 1 lit. f DSGVO
3. Prüfen: Ändert sich die Rechtsgrundlage (Art. 6/9 DSGVO)? Muss ggf. neue Einwilligung eingeholt werden?
4. Prüfen: Ist eine DSFA erforderlich? (Weiterleitung an `dsfa-erstellung` anbieten)
5. Änderungsentwurf für betroffene Abschnitte der Datenschutzerklärung erstellen.
6. Prüfen: Erfordern App-Store-Labels oder Cookie-Banner-Konfiguration Anpassung?

## Quellen und Zitierweise

Verbindlich nach `../../references/zitierweise.md`.

- Art. 13 DSGVO (Informationspflicht bei Datenerhebung bei Betroffenen)
- Art. 14 DSGVO (Informationspflicht bei Datenerhebung nicht bei Betroffenen)
- Art. 5 Abs. 1 lit. a DSGVO (Transparenzgrundsatz)
- Art. 12 DSGVO (Transparente Information)
- §§ 19, 25 TDDDG (Einwilligung Endgerätezugriff, Cookie-Einwilligung)
- EDSA-Leitlinien 03/2022 zu Dunklen Designmustern (Consent-Flows)
- EDSA-Leitlinien 05/2020 zu Einwilligung
- Paal, in: Paal/Pauly, DSGVO/BDSG, 3. Aufl. 2021, Art. 13 Rn. 1 ff.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ausgabeformat

**Sweep-Modus:**
1. Sweep-Datum und geprüfte Quellen
2. Drift-Tabelle (alle Flächen × alle Dimensionen)
3. Drift-Klassifikation mit Schwere
4. Priorisierte Änderungsvorschläge (druckfertige Textbausteine, keine Kommentare im Erklärungstext)
5. Sweep-Folgeaktionen

**Direkt-Modus:**
1. Betroffene Art. 13/14-Pflichten
2. Rechtsgrundlagen-Check
3. DSFA-Hinweis (falls einschlägig)
4. Änderungsentwurf für Datenschutzerklärung (Textbausteine)

## Beispiel (Direkt-Modus)

**Geplante Änderung:** Das Unternehmen möchte einen neuen Analytics-Anbieter mit Sitz in den USA integrieren (bisher EU-only).

**Analyse:**
- Neue Datenkategorie: Nein (Nutzungsverhalten bereits erfasst).
- Neuer Empfänger (Drittland USA): **Ja** – Art. 13 Abs. 1 lit. f DSGVO (Drittlandtransfer mit Transfermechanismus angeben).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Consent-Management: Ist der Anbieter nur nach Einwilligung aktiv (§ 25 TDDDG)? Dann Cookie-Banner anpassen (neue Kategorie / neuer Anbieter).
- DSFA: `anwendungsfall-triage` empfehlen – bei umfangreichem Tracking ggf. DSFA nach Art. 35 DSGVO erforderlich.

**Änderungsentwurf (Datenschutzerklärung, Abschnitt "Drittlandsübermittlung"):**
> "[Neue Passage] Wir übermitteln Daten an [Anbieter] mit Sitz in den USA. Die Übermittlung erfolgt auf Grundlage von [Transfermechanismus: EU-Standardvertragsklauseln nach Beschluss 2021/914/EU / EU-US Data Privacy Framework]. Eine Transferfolgenabschätzung liegt vor. Weitere Informationen erhalten Sie auf Anfrage bei unserem Datenschutzbeauftragten."

## Risiken / typische Fehler

- **Sweep ohne konfigurierten Ausgabenordner:** Ohne Ordner-Pfad kann der Sweep keine Praxis-Inventur aus Plugin-Ausgaben erstellen; Direkt-Modus bleibt aber ohne Ausgabenordner vollständig nutzbar.
- **Datenschutzerklärungsversion nicht datiert:** Nutzer sollten publizierte Erklärungen immer mit Datum versehen; anderenfalls kann Drift nicht datiert werden.
- **Cookie-Banner ≠ Datenschutzerklärung:** TDDDG-Einwilligung (§ 25 TDDDG) ist unabhängig von der DSGVO-Rechtsgrundlage; eine korrekte Datenschutzerklärung ersetzt nicht den rechtskonformen Cookie-Banner.
- **Stillschweigendes Weglassen veralteter Klauseln:** Wenn eine Verarbeitung eingestellt wird, muss die Datenschutzerklärung aktiv aktualisiert werden – das Fehlen einer Praxis ist kein Automatismus für korrekte Erklärung.
- **Frequenz:** EDSA empfiehlt anlassbezogene Aktualisierung; ein rein jährliches Review ist bei schnell wachsenden Produkten nicht ausreichend.

## Quellen / Updates

Stand: 05/2026. Aktualität prüfen bei Änderungen des TDDDG, neuen EDSA-Leitlinien zu Transparenz und Einwilligung sowie DSK-Orientierungshilfen zu Telemedien.

**Querverweise:**
- `datenschutzrecht/skills/regulierungs-luecken-analyse/SKILL.md` — Eingehende neue Anforderungen vs. Praxis-Drift
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md` — Drittlandtransfer-Passagen in Datenschutzerklärungen
- `datenschutzrecht/skills/anwendungsfall-triage/SKILL.md` — Neue Verarbeitungstätigkeiten identifizieren

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Faktische Updates (Stand 05/2026)

- **TDDDG (Telekommunikation-Digitale-Dienste-Datenschutz-Gesetz):** Seit 14.05.2024 (loest TTDSG ab); enthaelt §§ 24-25 zur Cookie- und Endgeraetezugriffs-Einwilligung. Quelle: gesetze-im-internet.de/tdddg.
- **EDSA-Guidelines Cookies / Tracking:** EDSA-Guidelines 02/2023 und Aktualisierungen (z.B. Dark Patterns) live ueber edpb.europa.eu pruefen.
- **DSK-Beschluesse (Datenschutzkonferenz Bund-Laender):** Aktuelle DSK-Beschluesse zu Cookies, Drittlandtransfer, KI, Beschaeftigtendatenschutz live ueber datenschutzkonferenz-online.de pruefen.
- **EuGH-Linie Cookies / Einwilligung:** Aktuelle EuGH-Verfahren zur Granularitaet, Freiwilligkeit, Pay-or-OK-Modellen live ueber curia.europa.eu pruefen.
- **DSA-Werbetransparenz:** Datenschutzerklaerung sollte bei Plattformen Hinweise auf DSA-Werbearchiv (Art. 39 DSA) und Empfehlungssysteme (Art. 38 DSA) enthalten.
- **KI-VO Art. 50:** Falls Webseite Chatbot oder KI-generierte Inhalte enthaelt — KI-VO-Transparenzpflichten ab 02.08.2026 in Datenschutzerklaerung / Impressum / Hinweise integrieren.

## Triage zu Beginn

1. Routinemonitor (wöchentlich/monatlich) oder konkreter Anlass (neue Verarbeitung, Systemwechsel)?
2. Welche Dokumente sollen geprüft werden? (Datenschutzerklärung Website / intern / beides)
3. Welche neuen Verarbeitungsvorgänge wurden seit dem letzten Monitor eingeführt?
4. Gibt es EDSA-Leitlinien oder DSK-Beschlüsse, die seit dem letzten Monitor in Kraft getreten sind?

## Output-Template — Monitor-Ergebnis

**Adressat:** DSB / Compliance — Tonfall: sachlich-strukturiert

```
Richtlinien-Monitor [DATUM]
Organisation: [NAME]
Geprüfte Dokumente: [LISTE]

Befunde:
| Nr. | Dokument          | Abweichung / Drift              | Prioritaet | Frist  |
|-----|------------------|----------------------------------|------------|--------|
|  1  | Datenschutzerklärung | Cookie-Liste veraltet (3 neue)  | HOCH       | [DATUM]|
|  2  | Datenschutzerklärung | Empfaenger nicht konkret benannt| MITTEL     | [DATUM]|
|  3  | Interne Richtlinie | KI-Tools noch nicht erwaehnt    | HOCH       | [DATUM]|

Keine Abweichungen: [LISTE GEPRÜFTER BEREICHE]

Empfehlung: Aktualisierung bis [DATUM]
Verantwortlich: [PERSON/ROLLE]
```

## 2. `ropa-art-30-controller-deutsch-vorlage`

**Frühere Beschreibung:** Vollvorlage fuer das Verzeichnis von Verarbeitungstaetigkeiten des Verantwortlichen nach Art. 30 Abs. 1 DSGVO. Tabellenstruktur mit allen sieben Mindestinhalten, ausgefuelltes Beispiel fuer Personalverwaltung, Mandantenakte, Kontaktformular, CRM. Direkt nutzbare Vorlage fuer Kanzleien und Unternehmen.

# RoPA-Vorlage Verantwortlicher (Controller) – Deutsch

## Zweck

Dieser Skill liefert eine ausfuellfertige Vorlage fuer das Verzeichnis von Verarbeitungstaetigkeiten des Verantwortlichen nach Art. 30 Abs. 1 DSGVO. Er enthaelt die Spaltenstruktur, ein Deckblatt, drei vollstaendig befuellte Beispiele und einen Versionierungs-Footer.

## Wann brauchen Sie diesen Skill

- Erstaufbau eines Verarbeitungsverzeichnisses in der Kanzlei oder im Mandantenunternehmen.
- Vorlage gegenueber Aufsichtsbehoerde gemaess Art. 30 Abs. 4 DSGVO.
- Auditvorbereitung; Lueckenanalyse eines bestehenden RoPA.
- Standardisierung mehrerer Standorte oder Mandantengruppen.

## Rechtlicher Rahmen

Art. 30 Abs. 1 DSGVO – Pflichtinhalte fuer Verantwortliche:

a) Name und Kontaktdaten des Verantwortlichen, ggf. gemeinsam Verantwortlicher, Vertreter und Datenschutzbeauftragter;
b) Zwecke der Verarbeitung;
c) Beschreibung der Kategorien betroffener Personen und der Kategorien personenbezogener Daten;
d) Kategorien von Empfaengern, gegenueber denen die personenbezogenen Daten offengelegt worden sind oder noch offengelegt werden, einschliesslich Empfaenger in Drittlaendern oder internationalen Organisationen;
e) ggf. Uebermittlungen in ein Drittland oder an eine internationale Organisation, einschliesslich der Angabe des betreffenden Drittlands sowie bei Uebermittlungen gemaess Art. 49 Abs. 1 Unterabs. 2 DSGVO Dokumentierung der geeigneten Garantien;
f) wenn moeglich, vorgesehene Fristen fuer die Loeschung der verschiedenen Datenkategorien;
g) wenn moeglich, allgemeine Beschreibung der TOMs gemaess Art. 32 Abs. 1 DSGVO.

## Ablauf / Checkliste

1. Deckblatt mit Verantwortlicher-Stammdaten anlegen.
2. Pro Geschaeftsprozess eine Zeile.
3. Spalten gemaess Vorlage befuellen.
4. Bei Drittlandtransfer Transferinstrument (SCC, DPF, BCR) eintragen.
5. Loeschfristen konkret, nicht "nach gesetzlichen Vorgaben".
6. TOMs in eigenes Anhangsdokument; im RoPA Verweis.
7. Versionierung am Fuss.
8. Jaehrlicher Review-Termin im Kalender.

## Mustertext / Template

### Deckblatt

```
Verantwortlicher:        [Firmenname / Kanzleiname]
Anschrift:               [...]
Vertreter (Art. 27):     [falls anwendbar]
Datenschutzbeauftragter: [Name, Kontakt]
Aufsichtsbehoerde:       [zustaendige LDI / BfDI]
Erstellt:                [Datum]
Letzte Aenderung:        [Datum]
Version:                 [v1.0]
```

### Tabelle (Pflichtspalten)

| Nr. | Verarbeitungstaetigkeit | Zweck | Rechtsgrundlage | Kategorien Betroffene | Datenkategorien | Empfaengerkategorien | Drittland / Garantie | Loeschfrist | TOM-Verweis |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Personalverwaltung Beschaeftigte | Begruendung, Durchfuehrung und Beendigung des Arbeitsverhaeltnisses | Art. 6 Abs. 1 lit. b DSGVO, § 26 BDSG | Beschaeftigte, Bewerber | Stammdaten, Vertragsdaten, Lohndaten, Krankheitszeiten | Sozialversicherungstraeger, Finanzamt, Lohnbuchhaltungsdienstleister | nein | 10 Jahre nach Ausscheiden (§ 257 HGB, § 147 AO); Bewerberdaten 6 Monate | TOM-Anhang Ziff. 1, 3, 5 |
| 2 | Mandantenakte (Rechtsdienstleistung) | Anbahnung, Durchfuehrung und Abrechnung von Mandaten | Art. 6 Abs. 1 lit. b und f DSGVO; § 50 BRAO | Mandanten, Gegner, Zeugen | Stammdaten, Korrespondenz, Schriftsaetze, Honorardaten | Gerichte, Behoerden, Gegenanwaelte, Versicherer | nein | 6 Jahre nach Mandatsende (§ 50 Abs. 1 BRAO); steuerlich relevante Belege 10 Jahre | TOM-Anhang Ziff. 1, 2, 4, 6 |
| 3 | Kontaktformular Website | Beantwortung von Anfragen | Art. 6 Abs. 1 lit. b oder f DSGVO | Interessenten, Mandanten | Name, E-Mail, Telefon, Anfrageinhalt | Hosting-Dienstleister (AVV) | nein | 6 Monate nach Erledigung | TOM-Anhang Ziff. 1, 5 |
| 4 | CRM Vertrieb | Kundenpflege, Akquise | Art. 6 Abs. 1 lit. b und f DSGVO | Bestandskunden, Interessenten | Stammdaten, Kontakthistorie, Umsatzdaten | CRM-SaaS-Anbieter (USA) | USA – EU-US DPF (Aktiv-Listing dokumentiert in Anhang DPF-Liste) | 3 Jahre nach letztem Kontakt | TOM-Anhang Ziff. 1, 2, 5 |

### Versionierungs-Footer

```
Version 1.0  – Erstanlage   – [Datum, Bearbeiter]
Version 1.1  – [Aenderung]  – [Datum, Bearbeiter]
```

## Typische Fehler

- "Zweck" und "Rechtsgrundlage" vermischt – bitte trennen.
- Empfaengerkategorien als Einzelnamen ("Frau Mueller, Steuerberater") statt Kategorie ("Steuerberatung").
- Drittland nur "USA" ohne Transferinstrument.
- Loeschfristen pauschal "10 Jahre" ohne Differenzierung nach Datenkategorie.
- TOM-Spalte mit vollem Wortlaut der Anlage 32 DSGVO – besser Verweis.
- Kein DSB-Eintrag obwohl Bestellpflicht (§ 38 BDSG) besteht.

## Querverweise

- `ropa-art-30-dsgvo-grundlagen` fuer Rechtsrahmen.
- `ropa-art-30-processor-deutsch-vorlage` fuer Spiegel-Vorlage Processor.
- `ropa-bdsg-besondere-art-9-categories` fuer Gesundheits- und Beschaeftigtendaten.
- `avv-tom-art-32-dsgvo-anlage` fuer TOM-Konzept.
- `drittlandstransfer-pruefung` fuer Art. 44 ff. DSGVO.

## Quellen Stand 06/2026

- VO (EU) 2016/679 (DSGVO), Art. 30 Abs. 1.
- BDSG, § 26 (Beschaeftigtendaten), § 38 (DSB-Pflicht).
- BRAO § 50 (Aktenaufbewahrung).
- HGB § 257, AO § 147 (handels-/steuerrechtliche Aufbewahrung).
- DSK-Kurzpapier Nr. 1 "Verzeichnis von Verarbeitungstaetigkeiten" (Stand 17.12.2018).


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `ropa-art-30-dsgvo-grundlagen`

**Frühere Beschreibung:** Grundlagen des Verzeichnisses von Verarbeitungstaetigkeiten nach Art. 30 DSGVO. Anwendungsbereich, Schwellenwert, Mindestinhalte Controller und Processor, Verhaeltnis zu § 70 BDSG, Vorlagepflicht gegenueber der Aufsichtsbehoerde. Einstiegs-Skill fuer das Records of Processing Activities (RoPA).

# Verzeichnis von Verarbeitungstaetigkeiten – Art. 30 DSGVO Grundlagen

## Zweck

Dieser Skill ordnet das Verzeichnis von Verarbeitungstaetigkeiten (Records of Processing Activities, kurz RoPA) nach Art. 30 DSGVO ein. Er erklaert Pflichtige, Inhalte, Form und Verhaeltnis zu anderen Dokumentationspflichten (DSFA, AVV, RoPA), damit Kanzleien und Datenschutzbeauftragte das richtige Werkzeug fuer das richtige Dokument waehlen.

## Wann brauchen Sie diesen Skill

- Mandant fragt: "Brauchen wir ein Verarbeitungsverzeichnis?"
- Aufsichtsbehoerde verlangt nach Art. 30 Abs. 4 DSGVO Vorlage des Verzeichnisses.
- Audit eines bestehenden Verzeichnisses auf Vollstaendigkeit.
- Erstaufbau eines RoPA in einer Kanzlei, einem Unternehmen oder einer oeffentlichen Stelle.
- Abgrenzung Controller-Verzeichnis (Art. 30 Abs. 1 DSGVO) vs. Processor-Verzeichnis (Art. 30 Abs. 2 DSGVO).

## Rechtlicher Rahmen

### Art. 30 Abs. 1 DSGVO – Verzeichnis des Verantwortlichen (Controller)

Pflichtinhalte:

1. Name und Kontaktdaten des Verantwortlichen, ggf. gemeinsam Verantwortlicher, Vertreter und Datenschutzbeauftragter.
2. Zwecke der Verarbeitung.
3. Beschreibung der Kategorien betroffener Personen und der Kategorien personenbezogener Daten.
4. Kategorien von Empfaengern, denen offengelegt wurde oder noch offengelegt wird.
5. Drittlandtransfer: Empfaengerland und Dokumentation geeigneter Garantien (Art. 46 Abs. 2 DSGVO).
6. Vorgesehene Loeschfristen fuer die verschiedenen Datenkategorien.
7. Allgemeine Beschreibung der technischen und organisatorischen Massnahmen (TOMs) gemaess Art. 32 Abs. 1 DSGVO.

### Art. 30 Abs. 2 DSGVO – Verzeichnis des Auftragsverarbeiters (Processor)

Pflichtinhalte:

1. Name und Kontaktdaten des Auftragsverarbeiters und jedes Verantwortlichen, fuer den er taetig ist, ggf. Vertreter und DSB.
2. Kategorien der im Auftrag jedes Verantwortlichen durchgefuehrten Verarbeitungen.
3. Drittlandtransfer: Empfaengerland und geeignete Garantien.
4. Allgemeine Beschreibung der TOMs (Art. 32 Abs. 1 DSGVO).

### Art. 30 Abs. 3 DSGVO – Schriftform

Schriftlich oder elektronisch. In der Praxis: Excel, Datenbank, RoPA-Software, Word-Dokument. Wichtig: aktuell halten, datierte Versionen.

### Art. 30 Abs. 4 DSGVO – Vorlagepflicht

Auf Anforderung der Aufsichtsbehoerde vorzulegen.

### Art. 30 Abs. 5 DSGVO – Ausnahme fuer KMU

Unternehmen oder Einrichtungen mit weniger als 250 Mitarbeitern sind grundsaetzlich befreit, **es sei denn**:

- die Verarbeitung birgt ein Risiko fuer Rechte und Freiheiten;
- die Verarbeitung erfolgt nicht nur gelegentlich;
- die Verarbeitung umfasst besondere Datenkategorien (Art. 9 DSGVO) oder Daten ueber strafrechtliche Verurteilungen (Art. 10 DSGVO).

In der Praxis: praktisch jede Kanzlei, jede Arztpraxis, jedes HR-System eines Mittelstaendlers erfuellt mindestens einen Ausnahmegrund. Die KMU-Ausnahme ist daher weitgehend Theorie.

### § 70 BDSG – RoPA fuer Bundesbehoerden

Fuer Bundesbehoerden im Anwendungsbereich der JI-Richtlinie (Polizei und Justiz) gilt § 70 BDSG mit eigenen Mindestinhalten.

## Ablauf / Checkliste

1. **Rollenklaerung:** Ist die Stelle Verantwortlicher, gemeinsam Verantwortlicher (Art. 26 DSGVO), Auftragsverarbeiter (Art. 28 DSGVO) oder mehreres zugleich?
2. **Pflichtenpruefung:** Greift Art. 30 Abs. 5 DSGVO oder ist Verzeichnis ohnehin Pflicht?
3. **Inventar:** Welche Verarbeitungstaetigkeiten gibt es? Faustregel: pro Geschaeftsprozess eine Zeile.
4. **Mindestinhalte erfassen:** je nach Rolle 7 (Controller) oder 4 (Processor) Felder.
5. **Drittlandtransfer:** separate Spalte; Verweis auf SCC, BCR, DPF, Angemessenheitsbeschluss.
6. **Loeschfristen:** konkrete Fristen, nicht "nach gesetzlichen Vorgaben".
7. **TOM-Referenz:** Verweis auf TOM-Konzept; nicht jede Massnahme im RoPA wiederholen.
8. **Versionierung:** Datierte Snapshots fuer Audit-Trail.
9. **Review-Zyklus:** jaehrlich oder bei wesentlicher Aenderung.

## Mustertext / Template

Tabellenkopf (Controller):

| Lfd. Nr. | Verarbeitungstaetigkeit | Zweck | Rechtsgrundlage | Kategorien Betroffene | Datenkategorien | Empfaengerkategorien | Drittland / Garantie | Loeschfrist | TOM-Verweis |
|---|---|---|---|---|---|---|---|---|---|

Tabellenkopf (Processor):

| Lfd. Nr. | Auftraggeber | Verarbeitungskategorie | Drittland / Garantie | TOM-Verweis |
|---|---|---|---|---|

Konkrete Vorlagen liefern die Skills:

- `ropa-art-30-controller-deutsch-vorlage`
- `ropa-art-30-processor-deutsch-vorlage`
- `ropa-en-controller-template`
- `ropa-en-processor-template`

## Typische Fehler

- KMU-Ausnahme bejaht, obwohl regelmaessige Personalverarbeitung erfolgt.
- TOM-Spalte mit "Verschluesselung" abgespeist – zu pauschal, Aufsichtsbehoerde fordert Konkretion.
- Drittlandtransfer nicht erfasst, obwohl SaaS in den USA gehostet wird.
- Empfaengerkategorien fehlen oder werden mit Einzelempfaengern verwechselt.
- Kein Versionsstand; bei Audit unklar, welcher Stand zum Pruefzeitpunkt galt.
- Loeschfristen pauschal "10 Jahre"; ohne Differenzierung nach Datenkategorie.
- Doppelte Pflege RoPA / DSFA / TOM-Konzept ohne Querverweise.

## Querverweise

- `dsfa-erstellung` fuer hochrisikobehaftete Verarbeitungen.
- `avv-art-28-dsgvo-grundtatbestand` fuer Processor-Vertraege.
- `drittlandstransfer-pruefung` fuer Art. 44 ff. DSGVO.
- `dsb-bestellungspflicht-pruefung` fuer DSB-Verantwortlichkeiten.

## Quellen Stand 06/2026

- VO (EU) 2016/679 (DSGVO), insbesondere Art. 30, Erwaegungsgrund 13, 82.
- BDSG, insbesondere § 70 fuer Bundesbehoerden.
- EDSA: Position Paper on Article 30(5) GDPR (vom 19.04.2018).
- Konferenz der unabhaengigen Datenschutzaufsichtsbehoerden des Bundes und der Laender (DSK): Kurzpapier Nr. 1 "Verzeichnis von Verarbeitungstaetigkeiten" (Stand 17.12.2018).


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `ropa-bdsg-besondere-art-9-categories`

**Frühere Beschreibung:** RoPA-Besonderheiten bei besonderen Datenkategorien nach Art. 9 DSGVO (Gesundheit, biometrische Daten, Religion, Gewerkschaftszugehoerigkeit), bei Beschaeftigtendaten § 26 BDSG und strafrechtlichen Verurteilungen Art. 10 DSGVO. Erhoehte Anforderungen an Zweckbestimmung, Erforderlichkeit, Rechtsgrundlage und TOMs.

# RoPA bei besonderen Datenkategorien – Art. 9 DSGVO, § 26 BDSG, Art. 10 DSGVO

## Zweck

Dieser Skill behandelt die erhoehten Dokumentationsanforderungen im Verzeichnis von Verarbeitungstaetigkeiten bei besonderen Datenkategorien nach Art. 9 DSGVO (sensitive Daten), Beschaeftigtendaten nach § 26 BDSG und Daten ueber strafrechtliche Verurteilungen oder Straftaten nach Art. 10 DSGVO. Solche Verarbeitungen brechen die KMU-Ausnahme nach Art. 30 Abs. 5 DSGVO und ziehen ueblicherweise eine DSFA-Pflicht (Art. 35 DSGVO) nach sich.

## Wann brauchen Sie diesen Skill

- Arztpraxis, Krankenhaus, Pflegedienst, Apotheke baut RoPA auf.
- Personalabteilung dokumentiert Krankheitstage, BEM-Daten, Schwerbehindertenstatus.
- Kanzlei verarbeitet Mandantendaten mit Bezug zu Gesundheit, Religion, sexueller Orientierung, Strafverfahren.
- Versicherer dokumentiert Gesundheits- oder Schadendaten.
- Verein dokumentiert religioese oder gewerkschaftliche Zugehoerigkeit der Mitglieder.
- Biometrische Verfahren (Fingerprint-Login, Gesichtserkennung) im Einsatz.

## Rechtlicher Rahmen

### Art. 9 Abs. 1 DSGVO – Verbotsprinzip

Verarbeitung ist verboten, soweit sie ergibt:

- rassische und ethnische Herkunft,
- politische Meinungen,
- religioese oder weltanschauliche Ueberzeugungen,
- Gewerkschaftszugehoerigkeit,
- genetische Daten,
- biometrische Daten zur eindeutigen Identifizierung,
- Gesundheitsdaten,
- Daten zum Sexualleben oder der sexuellen Orientierung.

### Art. 9 Abs. 2 DSGVO – Ausnahmen

Verarbeitung zulaessig u. a. bei: ausdruecklicher Einwilligung (lit. a), Arbeitsrecht und Sozialrecht (lit. b), lebenswichtigem Interesse (lit. c), Vereinen und Religionsgemeinschaften (lit. d), oeffentlich gemachten Daten (lit. e), Rechtsanspruechen (lit. f), erhebliches oeffentliches Interesse (lit. g), Gesundheits- und Sozialfuersorge (lit. h), oeffentliche Gesundheit (lit. i), Archiv-/Forschungs-/Statistikzwecke (lit. j).

### § 26 BDSG – Beschaeftigtendaten

§ 26 BDSG bleibt nach Aufhebung durch BVerfG-Rechtsprechung und nachfolgende Gesetzgebung als Rechtsgrundlage praeskriptiv relevant; daneben kommen Kollektivvereinbarungen (§ 26 Abs. 4 BDSG) und Einwilligung (§ 26 Abs. 2 BDSG) in Betracht.

### § 22 BDSG

§ 22 BDSG regelt die Verarbeitung besonderer Datenkategorien zu im oeffentlichen Interesse liegenden Zwecken, fuer Beschaeftigungszwecke, fuer praeventive Medizin u. a.; § 22 Abs. 2 BDSG verlangt **spezifische TOMs**, die im RoPA dokumentiert werden muessen.

### Art. 10 DSGVO

Daten ueber strafrechtliche Verurteilungen und Straftaten duerfen nur unter behoerdlicher Aufsicht oder aufgrund nationalen Rechts verarbeitet werden.

## Ablauf / Checkliste

1. **Identifikation:** Welche der oben genannten Kategorien faellt an? Pruefe sowohl direkte Erhebung als auch Rueckschluss (z. B. Fotos koennen ethnische oder gesundheitliche Hinweise enthalten).
2. **Rechtsgrundlage:** Doppelte Rechtsgrundlage erforderlich – Art. 6 Abs. 1 DSGVO **und** Art. 9 Abs. 2 DSGVO bzw. § 26 oder § 22 BDSG.
3. **Erforderlichkeit:** strenger Massstab; pruefe Alternativen (Pseudonymisierung, Aggregation).
4. **DSFA-Pruefung:** Art. 35 Abs. 3 lit. b DSGVO – DSFA in der Regel obligatorisch bei umfangreicher Verarbeitung besonderer Kategorien.
5. **TOMs:** § 22 Abs. 2 BDSG fordert spezifische Massnahmen (Pseudonymisierung, Zugriffsbeschraenkung, Auditing, Schulung).
6. **RoPA-Eintrag:** zusaetzliche Spalte oder Markierung "Art. 9 DSGVO" mit Verweis auf Rechtsgrundlage und DSFA.
7. **Loeschfristen:** restriktiv; Gesundheitsdaten oft 10 Jahre (§ 630f Abs. 3 BGB Patientenakte), aber nicht laenger.

## Mustertext / Template

### Zusatzspalten fuer besondere Datenkategorien

| Verarbeitung | Datenkategorie (Art. 9) | Doppelte Rechtsgrundlage | DSFA-Verweis | Spezifische TOMs (§ 22 Abs. 2 BDSG) |
|---|---|---|---|---|
| Patientenakte | Gesundheitsdaten | Art. 6 Abs. 1 lit. b + Art. 9 Abs. 2 lit. h DSGVO; § 22 Abs. 1 Nr. 1 lit. b BDSG | DSFA-Ziff. 3 | Rollenbasierter Zugriff, Pseudonymisierung Forschungsdatensatz, Verschluesselung at-rest |
| BEM-Verfahren | Gesundheitsdaten Beschaeftigte | Art. 6 Abs. 1 lit. c + Art. 9 Abs. 2 lit. b DSGVO; § 26 Abs. 3 BDSG | DSFA-Ziff. 7 | Getrennte Akte, eingeschraenkter Personenkreis, dokumentierter Zugriff |
| Glaubensbekenntnis Lohnsteuer | Religioese Ueberzeugung | Art. 6 Abs. 1 lit. c + Art. 9 Abs. 2 lit. b DSGVO; § 39 EStG | DSFA-Ziff. 9 | Zugriff nur Lohnbuchhaltung, kein CRM-Sync |
| Biometrischer Zutritt | Biometrische Daten | Art. 6 Abs. 1 lit. f + Art. 9 Abs. 2 lit. a DSGVO (Einwilligung) | DSFA-Ziff. 11 | Lokale Speicherung Template, kein Bild, Loeschung bei Austritt |

### Erweiterung Versionierungs-Footer

Zusatzhinweis: "Diese Verarbeitung beinhaltet besondere Kategorien personenbezogener Daten. DSFA-Pflicht und § 22 Abs. 2 BDSG sind beachtet."

## Typische Fehler

- Nur Art. 6 DSGVO geprueft, Art. 9 DSGVO uebersehen.
- Schwerbehindertenstatus aus dem Personalstammdatensatz ohne gesonderte Markierung als Gesundheitsdatum gefuehrt.
- Biometrie-Login ohne ausdrueckliche Einwilligung und ohne Alternative.
- Keine DSFA, obwohl umfangreiche Gesundheitsdatenverarbeitung.
- "Sensible Daten" pauschal eingetragen ohne konkrete Kategorie.
- TOMs nach Art. 32 statt nach § 22 Abs. 2 BDSG (zusaetzliche Anforderungen).
- Religionszugehoerigkeit aus Lohnsteuerklasse abgeleitet und ungesichert im allgemeinen HR-System.

## Querverweise

- `ropa-art-30-dsgvo-grundlagen` fuer Basis.
- `ropa-art-30-controller-deutsch-vorlage` fuer Basisvorlage.
- `dsfa-erstellung` fuer Art. 35 DSGVO.
- `mitarbeiter-datenschutz-26-bdsg` (falls vorhanden) fuer Beschaeftigtenkontext.
- `avv-tom-art-32-dsgvo-anlage` fuer TOM-Anhang.

## Quellen Stand 06/2026

- VO (EU) 2016/679 (DSGVO), Art. 9, Art. 10, Art. 30, Art. 35.
- BDSG, §§ 22, 26.
- BGB § 630f (Patientenakte).
- EStG § 39 (Lohnsteuermerkmale).
- EDSA: Leitlinien 03/2019 zur Verarbeitung personenbezogener Daten durch Videoeinrichtungen (Version 2.0 vom 29.01.2020).
- BVerfG, Beschluss vom 11.11.2020 – 1 BvR 3214/15 (Antiterrordatei-Folgeentscheidung) – bei Anpassung des § 22 BDSG sinngemaess beachten; vor Zitierung amtliche Fundstelle pruefen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 5. `ropa-en-controller-template`

**Frühere Beschreibung:** Full English-language template for the Records of Processing Activities (RoPA) of the controller under Article 30(1) GDPR. Seven mandatory contents, cover sheet, three worked examples (HR, client files, CRM with US sub-processor), and a versioning footer. Suitable for German law firms with international clients.

# Records of Processing Activities (RoPA) – Controller Template (English)

## Purpose

This skill provides a ready-to-use English-language template for the Records of Processing Activities (RoPA) of a controller pursuant to Article 30(1) GDPR. It is intended for German law firms, in-house counsel, and data protection officers who need to provide a RoPA in English to international clients, US group entities, or supervisory authorities in cross-border investigations.

## When you need this skill

- A multinational client requires an English-language RoPA.
- A US parent company asks for the EU subsidiary's processing records.
- A supervisory authority requests the RoPA in English in a cross-border case.
- A vendor audit (SOC 2, ISO 27001) reviews the RoPA.
- A first-time build of a RoPA in an internationally facing organisation.

## Legal framework

Article 30(1) GDPR requires the controller to maintain a record containing:

a) the name and contact details of the controller and, where applicable, the joint controller, the controller's representative, and the Data Protection Officer;
b) the purposes of the processing;
c) a description of the categories of data subjects and of the categories of personal data;
d) the categories of recipients to whom the personal data have been or will be disclosed, including recipients in third countries or international organisations;
e) where applicable, transfers of personal data to a third country or an international organisation, including the identification of that third country or international organisation and, in the case of transfers referred to in the second subparagraph of Article 49(1), the documentation of suitable safeguards;
f) where possible, the envisaged time limits for erasure of the different categories of data;
g) where possible, a general description of the technical and organisational measures referred to in Article 32(1) GDPR.

Article 30(3) requires written or electronic form; Article 30(4) makes the RoPA available to the supervisory authority on request; Article 30(5) provides a narrow SME exemption that rarely applies in practice.

## Workflow / Checklist

1. Fill in the cover sheet with controller details, representative (if applicable), and DPO.
2. One row per processing activity (one business process = one row).
3. Populate the seven mandatory columns.
4. For third-country transfers, identify the transfer tool (Adequacy Decision, SCCs, BCRs, DPF).
5. State retention periods concretely; avoid "as required by law".
6. Keep TOMs in a separate annex; reference only.
7. Add a versioning footer.
8. Schedule annual review.

## Template

### Cover Sheet

```
Controller:               [Company / Firm Name]
Address:                  [...]
Representative (Art. 27): [if applicable]
Data Protection Officer:  [Name, contact]
Supervisory Authority:    [competent DPA]
Created:                  [date]
Last amended:             [date]
Version:                  [v1.0]
```

### Table (mandatory columns)

| No. | Processing activity | Purpose | Legal basis | Categories of data subjects | Categories of personal data | Categories of recipients | Third country / safeguards | Retention period | TOM reference |
|---|---|---|---|---|---|---|---|---|---|
| 1 | HR administration | Establishment, performance, and termination of employment | Art. 6(1)(b) GDPR; Sec. 26 BDSG | Employees, applicants | Master data, contract data, payroll, sick leave | Social security, tax authority, payroll provider | none | 10 years after termination (Sec. 257 HGB, Sec. 147 AO); applicants 6 months | TOM Annex 1, 3, 5 |
| 2 | Client matter administration | Engagement, performance, and billing of legal services | Art. 6(1)(b) and (f) GDPR; Sec. 50 BRAO | Clients, opposing parties, witnesses | Master data, correspondence, briefs, fee data | Courts, authorities, opposing counsel, insurers | none | 6 years after end of mandate (Sec. 50(1) BRAO); tax-relevant documents 10 years | TOM Annex 1, 2, 4, 6 |
| 3 | Website contact form | Responding to inquiries | Art. 6(1)(b) or (f) GDPR | Prospective clients | Name, email, phone, message | Hosting provider (DPA in place) | none | 6 months after closure | TOM Annex 1, 5 |
| 4 | CRM sales | Customer relationship, business development | Art. 6(1)(b) and (f) GDPR | Existing customers, prospects | Master data, contact history, revenue data | CRM SaaS provider (USA) | USA – EU-US Data Privacy Framework (active listing on file, see DPF Annex) | 3 years after last contact | TOM Annex 1, 2, 5 |

### Versioning footer

```
Version 1.0 – Initial draft – [date, author]
Version 1.1 – [change]      – [date, author]
```

## Common mistakes

- Mixing "purpose" and "legal basis" in one column.
- Listing individual recipients ("Ms. Smith, accountant") instead of categories ("Tax advisory firms").
- Stating "USA" without naming the transfer tool.
- Generic retention "10 years" without differentiation by data category.
- Copying the full Art. 32 wording into the TOM column instead of referring to a TOM annex.
- Failing to list a DPO where one is mandatory under Sec. 38 BDSG.

## Cross-references

- `ropa-art-30-dsgvo-grundlagen` for the German-language framework.
- `ropa-en-processor-template` for the processor counterpart.
- `ropa-konzernumlauf-und-multi-entity` for multi-entity groups.
- `dpa-en-template-controller-processor` for English DPA templates.
- `tia-en-template-full` for the English Transfer Impact Assessment template.

## Sources as of 06/2026

- Regulation (EU) 2016/679 (GDPR), in particular Article 30(1), Recitals 13 and 82.
- BDSG (German Federal Data Protection Act), Sec. 26, 38.
- BRAO (Federal Lawyers' Act), Sec. 50.
- HGB Sec. 257; AO Sec. 147.
- DSK Short Paper No. 1 "Records of Processing Activities" (Status 17 December 2018).
- EDPB Position Paper on Article 30(5) GDPR (19 April 2018).


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 6. `ropa-en-processor-template`

**Frühere Beschreibung:** Full English-language template for the Records of Processing Activities (RoPA) of the processor under Article 30(2) GDPR. Four mandatory contents, controller list, processing categories, third-country transfers, sub-processor annex. For hosting providers, payroll, IT outsourcing, and cloud vendors with German clients.

# Records of Processing Activities (RoPA) – Processor Template (English)

## Purpose

This skill provides a ready-to-use English-language template for the Records of Processing Activities of a processor pursuant to Article 30(2) GDPR. Unlike the controller record, only four mandatory contents apply. Intended for cloud providers, IT outsourcing companies, payroll bureaus, hosting providers, printing services, external DPOs, and law firms acting in a processor role.

## When you need this skill

- An English-speaking processor builds its first RoPA.
- A multinational client requests a copy of the processor's records.
- Audit (SOC 2, ISO 27001, supervisory authority) requires English-language documentation.
- A law firm performs processor functions for a client (e.g. payroll, document management, eDiscovery hosting).

## Legal framework

Article 30(2) GDPR requires each processor and, where applicable, the processor's representative, to maintain a record containing:

a) the name and contact details of the processor or processors and of each controller on behalf of which the processor is acting, and, where applicable, of the controller's or the processor's representative, and the Data Protection Officer;
b) the categories of processing carried out on behalf of each controller;
c) where applicable, transfers of personal data to a third country or an international organisation, including the identification of that third country or international organisation and, in the case of transfers referred to in the second subparagraph of Article 49(1), the documentation of suitable safeguards;
d) where possible, a general description of the technical and organisational measures referred to in Article 32(1) GDPR.

One row per controller. Multiple processing categories can be grouped where TOMs are identical.

## Workflow / Checklist

1. Cover sheet with processor details.
2. Maintain a controller list (each customer relationship).
3. Per controller, describe processing categories (not individual activities).
4. Identify third-country transfers and the applicable transfer instrument.
5. Reference a TOM annex; do not repeat Art. 32 wording.
6. Maintain a separate sub-processor annex (Art. 28(4) GDPR) showing transfer chains.
7. Add versioning footer.

## Template

### Cover Sheet

```
Processor:                [Company name]
Address:                  [...]
Representative (Art. 27): [if applicable]
Data Protection Officer:  [Name, contact]
Created:                  [date]
Last amended:             [date]
Version:                  [v1.0]
```

### Table (mandatory columns)

| No. | Controller | Categories of processing | Third country / safeguards | TOM reference |
|---|---|---|---|---|
| 1 | [Client A GmbH] | Hosting of accounting software, backups, patch management | none | TOM Annex A |
| 2 | [Client B AG] | Payroll processing, wage tax filings, social security filings | none | TOM Annex A |
| 3 | [Client C KG] | Email hosting, spam filtering | USA – sub-processor (SCCs + TIA in Annex B) | TOM Annex A |
| 4 | [Client D e.V.] | Membership administration, direct debit collection | none | TOM Annex A |

### Sub-processor annex

| Sub-processor | Location | Service | Transfer tool |
|---|---|---|---|
| [Hyperscaler Cloud] | USA | Infrastructure as a Service | EU-US DPF (active listing on file in Annex B) |
| [Email filter service] | Ireland | Spam filtering | EU/EEA – no transfer safeguards required |
| [Backup provider] | Germany | Offsite backup | EU/EEA – no transfer safeguards required |

### Versioning footer

```
Version 1.0 – Initial draft – [date, author]
Version 1.1 – [change]      – [date, author]
```

## Common mistakes

- Confusing "categories of processing" (processor view) with "purpose" (controller responsibility).
- Omitting sub-processors that introduce third-country transfers.
- Maintaining redundant TOM descriptions per controller where the operational baseline is uniform.
- Missing the controller's DPO contact.
- Copying the full text of Article 32 into the TOM column instead of referencing a TOM annex.
- Overlooking second-tier sub-processor transfers (e.g. when a sub-processor uses a sub-sub-processor in the USA).

## Cross-references

- `ropa-art-30-dsgvo-grundlagen` for the German framework.
- `ropa-en-controller-template` for the controller counterpart.
- `dpa-en-template-controller-processor` for English DPA template.
- `dpa-en-tom-annex-template` for the TOM annex.
- `tia-en-template-full` for the English Transfer Impact Assessment.

## Sources as of 06/2026

- Regulation (EU) 2016/679 (GDPR), Article 30(2), Article 28.
- DSK Short Paper No. 1 "Records of Processing Activities" (Status 17 December 2018).
- DSK Short Paper No. 13 "Processor Agreements" (Status 16 January 2018).
- EDPB Guidelines 07/2020 on the concepts of controller and processor in the GDPR (adopted 7 July 2021).


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 7. `ropa-fuer-ki-anwendungen-besonderheiten`

**Frühere Beschreibung:** Besonderheiten des Verzeichnisses von Verarbeitungstaetigkeiten bei KI-Anwendungen: Trainingsdatensaetze, Inferenz, RAG, Prompt-Logs, Fine-Tuning, Vector Stores, automatisierte Entscheidungen (Art. 22 DSGVO), Bezug zur KI-Verordnung. Mit Spaltenerweiterungen und Beispielen fuer LLM-API-Nutzung, Co-Pilot-Tools und KI-gestuetzte Bewerberauswahl.

# RoPA fuer KI-Anwendungen – Besonderheiten

## Zweck

Dieser Skill behandelt die zusaetzlichen Pflichtinhalte und Risiko-Markierungen, die das Verzeichnis von Verarbeitungstaetigkeiten bei KI-Anwendungen abbilden muss. Die DSGVO-Vorgaben in Art. 30 DSGVO werden nicht ersetzt, aber durch KI-spezifische Fragestellungen erweitert: Trainingsdaten, Modellzweck, Vector Stores, Prompt- und Output-Logs, Drittlandtransfer ueber LLM-Anbieter, automatisierte Entscheidungsfindung nach Art. 22 DSGVO, sowie das Zusammenspiel mit der KI-Verordnung (KI-VO, VO (EU) 2024/1689).

## Wann brauchen Sie diesen Skill

- Mandant fuehrt LLM-API (z. B. fuer interne Assistenten, Chatbots, Code-Generierung) ein.
- HR setzt KI-Tools zur Vorauswahl ein.
- Fachabteilung nutzt RAG-Architektur mit unternehmenseigenen Daten.
- KI-Modelle werden auf personenbezogenen Daten **trainiert oder feinabgestimmt**.
- Vector-Datenbank mit Embeddings personenbezogener Dokumente.
- Pruefung: greift Art. 22 DSGVO (automatisierte Entscheidung)?

## Rechtlicher Rahmen

### DSGVO

- Art. 30 DSGVO bleibt Pflicht; zusaetzliche Inhalte ergeben sich aus DSFA und Transparenzpflichten.
- Art. 22 DSGVO: Verbot ausschliesslich automatisierter Einzelentscheidungen mit rechtlicher Wirkung; Ausnahmen Abs. 2; Schutzmassnahmen Abs. 3.
- Art. 35 DSGVO: DSFA-Pflicht bei systematischer und umfassender Bewertung (Profiling), bei neuen Technologien.
- Art. 13/14 DSGVO: Informationspflichten zu Logik, Tragweite und Auswirkungen automatisierter Entscheidungen.
- Art. 32 DSGVO: TOMs an KI-Risiken anpassen (Model Theft, Prompt Injection, Data Leakage).
- Art. 5 DSGVO: Datenminimierung, Speicherbegrenzung – besonders kritisch bei Trainingsdaten.

### KI-Verordnung (VO (EU) 2024/1689)

- Gilt seit 02.08.2024 stufenweise. Verbote ab 02.02.2025, GPAI-Pflichten ab 02.08.2025, Hochrisiko-Systeme ab 02.08.2026 (Annex III).
- HR-KI (Bewerberauswahl, Leistungsbewertung) ist nach Annex III Nr. 4 hochrisikobehaftet.
- Anbieter und Betreiber muessen Dokumentationspflichten (Art. 11, Art. 26 KI-VO) erfuellen – das ergaenzt das DSGVO-RoPA.

### EDSA-Leitlinien und EU-AI-Office

- EDPB Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models (verabschiedet 17.12.2024) – referenzieren, nicht aus Modellwissen zitieren.

## Ablauf / Checkliste

1. **KI-Inventur:** Welche KI-Funktionen sind im Einsatz? Anbieter, Modell, Hostingort.
2. **Datentyp-Mapping:** Sind personenbezogene Daten in Eingaben, Trainingsdaten, Embeddings, Logs oder Outputs?
3. **Rolle pruefen:** Verantwortlicher fuer welche Daten? Auftragsverarbeiter? Joint Controllership mit KI-Anbieter?
4. **Rechtsgrundlage:** Art. 6 DSGVO; bei besonderen Datenkategorien Art. 9; bei Beschaeftigten § 26 BDSG; bei Web-Scraping kritisch zu pruefen.
5. **Drittlandtransfer:** Hosting in USA/UK? DPF-Listing, SCC, TIA.
6. **Art. 22 DSGVO:** Trifft das System Entscheidungen mit rechtlicher Wirkung?
7. **DSFA:** typischerweise Pflicht; in RoPA verlinken.
8. **TOM-Erweiterung:** Prompt-Filterung, Output-Filter, Logging-Limits, Model-Isolation, kein Training auf Mandantendaten.
9. **KI-VO-Bezug:** Falls Hochrisiko, KI-VO-Dokumentation referenzieren.
10. **Loeschfristen:** insbesondere fuer Prompt-Logs und Vector-Embeddings.

## Mustertext / Template

### Erweiterte RoPA-Zeilen fuer KI-Anwendungen

| Nr. | KI-Anwendung | Zweck | Rechtsgrundlage | Datenkategorien (Input/Training/Output) | Anbieter / Hosting | Drittland / Garantie | Art. 22 DSGVO einschlaegig? | DSFA-Verweis | KI-VO-Status | Spezifische TOMs | Loeschfristen Logs |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Interner Chat-Assistent (LLM-API) | Mitarbeitersupport, Wissensabfragen | Art. 6 Abs. 1 lit. f DSGVO | Input: Prompts (kann pers. Daten enthalten); Training: keines; Output: Antworten | [Anbieter] US-Region | USA – DPF aktiv (Anhang); zusaetzlich SCC Modul 2 + TIA | nein | DSFA-Ziff. 4 | nicht Hochrisiko | Prompt-Filter, kein Training-Opt-in, Logging 30 Tage | 30 Tage |
| 2 | RAG-System Mandantendokumente | Anwaltliche Recherche | Art. 6 Abs. 1 lit. b und f DSGVO; § 50 BRAO | Input: Mandantenakten (Vector-DB); Output: Zitatpassagen | On-Premises / private Cloud DE | nein | nein | DSFA-Ziff. 5 | nicht Hochrisiko | Mandanten-Mandant-Trennung, Verschluesselung, Berufsgeheimnis-Schutz | Loeschung mit Mandatsende |
| 3 | HR-Vorauswahl Bewerber | Sichtung Bewerbungsdokumente | Art. 6 Abs. 1 lit. b + § 26 BDSG; **menschliche Letztentscheidung** | Input: Bewerbungsunterlagen; Output: Empfehlung | [Anbieter] DE | nein | Ja **mit menschlicher Letztentscheidung** (Art. 22 Abs. 2 lit. b) | DSFA-Ziff. 8 | Hochrisiko (Annex III Nr. 4) | Bias-Tests, Logging, Erklaerbarkeit, Beschwerdeweg | Loeschung 6 Monate nach Absage |
| 4 | Feinabstimmung Modell auf Branchendaten | Verbesserung Produktantworten | Art. 6 Abs. 1 lit. f DSGVO | Training: pseudonymisierte Branchendaten | DE | nein | nein | DSFA-Ziff. 9 | GPAI-Bezug | Pseudonymisierung vor Training, Loeschanfragen-Prozess | Modellversion 2 Jahre |

### Anhang: KI-spezifische TOMs

- Prompt-Klassifikation (PII-Erkennung) vor Versand an LLM.
- Output-Filter gegen Re-Identifizierung.
- Verbot Training-Opt-out durchsetzen (Auswahl entsprechender Tarife).
- Modell-Isolation (kein Cross-Tenant-Training).
- Logging-Limit; rollenbasierter Zugriff auf Logs.
- Vector-Store-Verschluesselung at-rest; Loeschmechanismus fuer Embeddings.
- Schulung Mitarbeiter zu Prompt-Hygiene.

## Typische Fehler

- "KI-Nutzung" als eine Zeile pauschal eingetragen – fehlende Differenzierung Input / Training / Output.
- Drittlandtransfer ueber LLM-Anbieter uebersehen, weil "kein Datenexport" gedacht wurde.
- Art. 22 DSGVO uebersehen, weil "der Mensch entscheidet final" behauptet wird, ohne dass dies tatsaechlich nachweisbar ist (Stichwort: rubber stamp).
- DSFA fehlt; nur Art. 30 RoPA gepflegt.
- Prompt-Logs unbegrenzt aufbewahrt.
- KI-VO-Hochrisiko-Status nicht festgehalten.
- Trainingsdaten aus Mandantenakten – Berufsgeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB) verletzt.
- Webscraping-Trainingsdaten ohne Rechtsgrundlage.

## Querverweise

- `ropa-art-30-dsgvo-grundlagen` fuer Basis.
- `ropa-art-30-controller-deutsch-vorlage` fuer Grundvorlage.
- `dsfa-erstellung` fuer Art. 35 DSGVO.
- `mandantendaten-ki` (in `kanzleifuehrung-und-mandat` Plugin) fuer berufsrechtliche Seite.
- `ki-vo-ai-act-pruefer` (in `ki-vo` Plugin) fuer KI-Verordnung.
- `tia-template-deutsch-vollvorlage` fuer Transferpruefung.

## Quellen Stand 06/2026

- VO (EU) 2016/679 (DSGVO), Art. 5, 6, 9, 13, 14, 22, 30, 32, 35.
- VO (EU) 2024/1689 (KI-VO / AI Act).
- BDSG, § 26.
- BRAO § 43a Abs. 2; § 50; StGB § 203.
- EDPB Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models (verabschiedet 17.12.2024).
- DSK: Hambacher Erklaerung zur Kuenstlichen Intelligenz (03.04.2019) und Folgepapiere.

## 8. `ropa-konzernumlauf-und-multi-entity`

**Frühere Beschreibung:** Verzeichnis von Verarbeitungstaetigkeiten in Konzern- und Multi-Entity-Strukturen. Konzernklausel-Mythos, Rollenverteilung (Verantwortlicher gemeinsam Verantwortlich Auftragsverarbeiter), zentrale vs. dezentrale Pflege, Intercompany-Datenfluesse, BCR-Verweis. Mit Strukturskizze und Vorlage fuer Master-RoPA und Entity-Anhaenge.

# RoPA im Konzern und in Multi-Entity-Strukturen

## Zweck

Dieser Skill behandelt das Verzeichnis von Verarbeitungstaetigkeiten in Konzernen und mehrgliedrigen Unternehmensgruppen. Er klaert, dass es **kein Konzernprivileg** im Datenschutzrecht gibt, ordnet Rollenverteilung und Datenfluesse zwischen Gruppenunternehmen und liefert eine Struktur fuer Master-RoPA mit Entity-Anhaengen.

## Wann brauchen Sie diesen Skill

- Konzernweiter RoPA-Roll-out (Mutter- und Tochtergesellschaften).
- Shared-Service-Center fuer HR, IT, Buchhaltung, Recht (typischerweise Processor-Konstellation).
- Intercompany Data Transfer Agreements (IDTA, hier deutscher Begriff: konzerninterne Datentransfer-Vereinbarung).
- Binding Corporate Rules (BCR) im Aufbau.
- M&A-Due-Diligence (Datenschutz-DD).
- Pruefung durch Aufsichtsbehoerde mit Bezug zu mehreren Konzernunternehmen.

## Rechtlicher Rahmen

### Kein Konzernprivileg

Die DSGVO kennt **kein Konzernprivileg** (Erwaegungsgrund 48 erlaubt nur ein **berechtigtes Interesse** an konzerninterner Datenuebermittlung im Rahmen von Art. 6 Abs. 1 lit. f DSGVO; keine pauschale Freistellung). Jede Datenuebermittlung zwischen rechtlich selbststaendigen Konzernunternehmen ist eine Uebermittlung im Sinne der DSGVO und braucht eine Rechtsgrundlage.

### Rollenverteilung

- **Verantwortlicher (Art. 4 Nr. 7 DSGVO):** entscheidet ueber Zwecke und Mittel.
- **Gemeinsam Verantwortliche (Art. 26 DSGVO):** gemeinsame Festlegung; Joint-Controllership-Vereinbarung erforderlich.
- **Auftragsverarbeiter (Art. 28 DSGVO):** im Auftrag, weisungsgebunden; AVV erforderlich.

Konzerninterne Shared-Service-Center sind typischerweise Auftragsverarbeiter (z. B. IT-Service-GmbH). HR-Daten an Mutter zur Karriereplanung koennen Joint-Controllership begruenden.

### Drittlandtransfer im Konzern

Konzerninterne Uebermittlungen in Drittlaender unterliegen Art. 44 ff. DSGVO. Loesungen:

- BCR (Art. 47 DSGVO) – aufwendig, aber genehmigungsfaehig.
- SCC (Beschluss (EU) 2021/914) zwischen den konzernzugehoerigen Stellen.
- Angemessenheitsbeschluss (z. B. EU-US DPF fuer US-Tochter im DPF).

### EDSA-Leitlinien

EDPB Guidelines 07/2020 on the concepts of controller and processor in the GDPR (verabschiedet 07.07.2021) – grundlegend zur Rollenklaerung.

## Ablauf / Checkliste

1. **Strukturkarte:** Liste aller Konzerngesellschaften mit Sitz, Rechtsform, taetigem Personal, Datenkategorien.
2. **Rollen-Mapping:** Wer ist fuer welchen Datenfluss Controller, Joint Controller oder Processor?
3. **Master-RoPA:** zentrales Dokument fuer gruppenuebergreifende Prozesse (Konzern-HR, Konzern-CRM, Konzern-Compliance).
4. **Entity-Anhaenge:** pro Gesellschaft eigene Tabelle mit Spezifika.
5. **Intercompany-Vertraege:** AVV oder Joint-Controllership-Vereinbarung verlinken.
6. **BCR-Status:** wenn vorhanden, in jedem Entity-RoPA als Garantie referenzieren; sonst SCC.
7. **Pflegemodell:** zentraler Datenschutzkoordinator oder dezentrale DSB?

## Mustertext / Template

### Master-RoPA-Deckblatt

```
Konzern:                  [Mutter AG]
Konzernweite DSB:         [Name, Kontakt]
Geltungsbereich:          [Liste der Tochtergesellschaften, EU/EWR + Drittlaender]
Konzerninterne Garantie:  [BCR genehmigt YYYY-MM-DD durch Lead-Behoerde XY] oder [SCC-Rahmenvertrag YYYY]
Erstellt:                 [Datum]
Letzte Aenderung:         [Datum]
Version:                  [v1.0]
```

### Master-Tabelle (gruppenuebergreifende Prozesse)

| Nr. | Prozess | Verantwortlicher | Gemeinsam Verantwortliche | Auftragsverarbeiter im Konzern | Datenfluss | Garantie |
|---|---|---|---|---|---|---|
| 1 | Konzern-Identity-Provider | Mutter AG (DE) | – | IT-Service-GmbH (DE) | Mitarbeiter aller Entities -> IdP | AVV |
| 2 | Konzernweite Compliance-Hotline | Mutter AG (DE) und Tochter Inc. (US) | Joint-Controllership Vereinbarung vom YYYY | Hotline-Provider (Dritter) | Hinweise aus allen Standorten | SCC + TIA; US-Tochter im EU-US DPF |
| 3 | Talent-Pool / Karriereplattform | Mutter AG | Toechter EU/EWR | – | HR-Daten weltweit | BCR (genehmigt YYYY) |
| 4 | Konzern-CRM | Mutter AG | – | Vertriebs-GmbH (DE) | Kundendaten EU -> Konzernzentrale | AVV |

### Entity-Anhang (pro Tochter)

```
Tochter:               [Name, Sitz, Rechtsform]
Lokal Verantwortlicher: [...]
Lokal DSB:             [...]
Lokale Aufsichtsbehoerde: [...]
Lokale Prozesse:       [Tabelle entsprechend Controller-Vorlage]
Bezug zu Master-RoPA:  [Prozessnummern oben]
```

### Datenflussdiagramm (textuell)

```
DE (Mutter)  <--AVV-->  IT-Service-GmbH (DE)
DE (Mutter)  <--Joint Controllership-->  US (Tochter im DPF)
DE (Mutter)  <--BCR-->  IN (Tochter)
DE (Mutter)  <--SCC-->  BR (Tochter, kein Angemessenheitsbeschluss)
```

## Typische Fehler

- "Konzernprivileg" angenommen; keine eigene Rechtsgrundlage dokumentiert.
- Shared-Service-Center als Controller behandelt, obwohl weisungsgebunden -> Joint Controllership statt AVV unzutreffend gewaehlt.
- BCR vorhanden, aber im RoPA nicht referenziert.
- Intercompany-Datenfluesse nicht erfasst; nur lokale Prozesse dokumentiert.
- US-Konzerntochter als "EU-nahe" behandelt – DPF-Status nicht geprueft.
- M&A: Datenschutz-DD ohne Sichtung des RoPA der Target-Gesellschaft.
- Doppelte Pflege: Master-RoPA und Entity-RoPA divergieren; kein Versionsabgleich.

## Querverweise

- `ropa-art-30-dsgvo-grundlagen` fuer Basis.
- `avv-konzern-und-multi-party-konstellation` fuer Vertragsseite.
- `avv-art-26-joint-controllership-deutsch` fuer Joint Controllership.
- `bcr-binding-corporate-rules` (falls Skill existiert) fuer BCR-Verfahren.
- `tia-template-deutsch-vollvorlage` fuer Transferpruefung.

## Quellen Stand 06/2026

- VO (EU) 2016/679 (DSGVO), Art. 4 Nr. 7, Art. 26, Art. 28, Art. 30, Art. 44–47, Erwaegungsgrund 48.
- Durchfuehrungsbeschluss (EU) 2021/914 der Kommission vom 04.06.2021 (SCC).
- EDPB Guidelines 07/2020 on the concepts of controller and processor in the GDPR (verabschiedet 07.07.2021).
- EDPB Working Document on Approval Procedure for BCR (zuletzt aktualisiert 2022).
- DSK-Kurzpapier Nr. 1 "Verzeichnis von Verarbeitungstaetigkeiten" (Stand 17.12.2018).


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 9. `spezial-auskunft-behoerden-gericht-und-registerweg`

**Frühere Beschreibung:** Auskunft: Behörden-, Gerichts- oder Registerweg im Plugin datenschutzrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Auskunft: Behörden-, Gerichts- oder Registerweg

## Spezialwissen: Auskunft: Behörden-, Gerichts- oder Registerweg
- **Spezialgegenstand:** Auskunft: Behörden-, Gerichts- oder Registerweg / spezial auskunft behoerden gericht und registerweg. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DSGVO, BDSG, TDDDG, PIA, DPIA, AVV, Art. 15, Art. 33, Art. 44, US, DPF, SCC.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Auskunft DSGVO** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Auskunftsanspruch Art. 15 DSGVO — Behörden- und Gerichtswege
- **Erstantrag** direkt an Verantwortlichen — Frist 1 Monat (Art. 12 Abs. 3 DSGVO), Verlängerung um 2 Monate bei Komplexität.
- **Datenkopie** Art. 15 Abs. 3 DSGVO; erste Kopie kostenlos, weitere mit Verwaltungskosten zulässig (EuGH C-307/22 zur Reichweite).
- **Identitätsprüfung** Art. 12 Abs. 6 — bei begründeten Zweifeln; nicht überzogen handhaben.
- **Verweigerung:**
  - **Art. 12 Abs. 5 lit. b DSGVO:** offenkundig missbräuchlich.
  - **§ 34 BDSG:** Ausnahmen (z. B. Datenverbleib bei Berufsgeheimnisträgern, Strafverfolgung).
- **Beschwerdewege:**
  - **Beschwerde Aufsicht Art. 77 DSGVO:** zuständige Landesdatenschutzbehörde oder BfDI.
  - **Klage gegen Verantwortlichen Art. 79 DSGVO:** ZG mit Streitwert-Zuständigkeit; ggf. § 29c ZPO Verbraucher.
  - **Klage gegen Aufsicht Art. 78 DSGVO:** VG-Klage.
- **EuGH-Rechtsprechung:** C-487/21 (Österreichische Datenschutzbehörde): Auskunftsanspruch erstreckt sich auf konkrete Empfänger (nicht nur Empfängerkategorien), wenn diese identifiziert werden können.

## Praxis-Tipp
Bei unvollständiger Auskunft frühzeitig nachhaken und konkret benennen, was fehlt (Empfänger, Speicherdauer, Herkunft, Logik bei automatisierten Entscheidungen). Pauschale Beschwerde "Auskunft unvollständig" wird oft zurückgewiesen — präzise Nachforderung erhöht Erfolgsaussichten.

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

## 10. `spezial-bdsg-tatbestand-beweis-und-belege`

**Frühere Beschreibung:** Bdsg: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin datenschutzrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Bdsg: Tatbestandsmerkmale, Beweisfragen und Beleglage

## Spezialwissen: Bdsg: Tatbestandsmerkmale, Beweisfragen und Beleglage
- **Spezialgegenstand:** Bdsg: Tatbestandsmerkmale, Beweisfragen und Beleglage / spezial bdsg tatbestand beweis und belege. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DSGVO, BDSG, TDDDG, PIA, DPIA, AVV, Art. 15, Art. 33, Art. 44, US, DPF, SCC.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **BDSG** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## BDSG-relevante Tatbestände und Beweisfragen
- **§ 26 BDSG (Beschäftigtendaten):** Erforderlichkeit für Begründung/Durchführung/Beendigung Arbeitsverhältnis; Beweislast Arbeitgeber. Bei Aufdeckung von Straftaten Abs. 1 S. 2 — dokumentierter Verdacht erforderlich.
- **§ 22 BDSG (besondere Datenkategorien):** Verarbeitung Art. 9 DSGVO-Daten (Gesundheit, Religion etc.) nur mit zusätzlicher Rechtsgrundlage des BDSG; nationale Erlaubnis-Norm + DSGVO-Rechtsgrundlage erforderlich.
- **§ 24 BDSG (Verarbeitung zu anderen Zwecken):** Zweckänderung bei nichtöffentlichen Stellen — Abwägung Interessen.
- **§ 38 BDSG (DSB-Bestellungspflicht):** ab 20 Personen mit ständiger Personendatenverarbeitung; Verstoß: § 43 BDSG Bußgeld.
- **Beweismittel:** Verzeichnis Art. 30 DSGVO, AVV, Schulungsnachweise, Logfiles, E-Mail-Verkehr, Betriebsvereinbarungen.

## Praxis-Tipp
Bei Verstoß gegen § 26 BDSG ist die zentrale Beweisfrage immer: "Erforderlich für was genau?" Pauschale Verweise auf "Zwecke des Arbeitsverhältnisses" tragen nicht — der konkrete Anlass und die Geeignetheit der Mittel müssen dokumentierbar sein. BAG 27.07.2017, 2 AZR 681/16 zur Verwertbarkeit von Keylogger-Daten als Leitorientierung.

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
