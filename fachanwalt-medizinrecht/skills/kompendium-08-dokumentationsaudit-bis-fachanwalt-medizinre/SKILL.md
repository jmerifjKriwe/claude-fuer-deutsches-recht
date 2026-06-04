---
name: kompendium-08-dokumentationsaudit-bis-fachanwalt-medizinre
description: "fachanwalt-medizinrecht: Konsolidiertes Skill-Kompendium 08; bündelt 6 frühere Spezialskills (dokumentationsaudit-630f, einwilligungsunfaehigkeit-ablehnung, erezept-falschmedikation, erstgespraech-mandatsannahme, fachanwalt-medizinrecht-aufklaerungsfehler und 1 weitere) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 08 - fachanwalt-medizinrecht

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `dokumentationsaudit-630f` | Dokumentationsaudit § 630f: moderner Medizinrechts-Skill für Behandlungsakte auditieren, Lücken, nachträgliche Änderungen, Metadaten und Beweisvermutung. Mit Haftung, Aufklärung, Behördenweg, Beweislogik und Quellencheck. |
| `einwilligungsunfaehigkeit-ablehnung` | Einwilligungsunfähigkeit und Ablehnung: moderner Medizinrechts-Skill für Therapieablehnung, natürliche Wille, Zwangsbehandlung, Betreuungsgericht und Klinikalltag. Mit Haftung, Aufklärung, Behördenweg, Beweislogik und Quellencheck. |
| `erezept-falschmedikation` | E-Rezept und Falschmedikation: moderner Medizinrechts-Skill für E-Rezept, Medikationsliste, Wechselwirkung, Apotheken-/Arztfehler und Nachweisführung. Mit Haftung, Aufklärung, Behördenweg, Beweislogik und Quellencheck. |
| `erstgespraech-mandatsannahme` | Erstgespraeach und Mandatsannahme im Arzthaftungs- Berufs- und Vertragsarztrecht: Anwendungsfall Patient oder Arzt meldet sich mit unstrukturiertem Sachverhalt zu Behandlungsfehler Approbationsproblem oder KV-Streit. § 630a BGB Behandlungsvertrag, § 43a BRAO Interessenkonflikte, § 3a RVG Honorar. Prüfraster Konstellation einordnen Arzthaftung Berufsrecht oder Vertragsarztrecht, Interessenkonflikt-Check, Vollmacht einholen, Streitwert und Gebührenvereinbarung, Fristen-Erstprognose. Output Mandats-Aufnahmeprotokoll mit Einordnung Sofortmassnahmen und Handlungsweichen. Abgrenzung zu Mandat-Triage-Medizinrecht und zu Erstgespraeach-Strafrecht. |
| `fachanwalt-medizinrecht-aufklaerungsfehler` | Workflow-Skill zu fachanwalt medizinrecht aufklaerungsfehler. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `fachanwalt-medizinrecht-behandlungsfehler-pruefen` | Behandlungsfehler §§ 630a 630h BGB Verletzung medizinischer Standard. Diagnosefehler Therapiefehler Befunderhebungsfehler Hygienefehler. Beweisregeln § 630h BGB Vermutung Kausalität bei grobem Behandlungsfehler § 630h Abs. 5 BGB Befunderhebungsfehler Dokumentationsmangel. Schadensersatzanspruch §§ 280 823 BGB Schmerzensgeld § 253 BGB. Verjährung drei Jahre § 195 BGB ab Kenntnis 30 Jahre Hoechstfrist. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `dokumentationsaudit-630f`

**Frühere Beschreibung:** Dokumentationsaudit § 630f: moderner Medizinrechts-Skill für Behandlungsakte auditieren, Lücken, nachträgliche Änderungen, Metadaten und Beweisvermutung. Mit Haftung, Aufklärung, Behördenweg, Beweislogik und Quellencheck.

# Dokumentationsaudit § 630f

## Fachkern: Dokumentationsaudit § 630f
- **Spezialgegenstand:** Dokumentationsaudit § 630f wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB §§ 630a ff., SGB V, ärztliches Berufsrecht, GOÄ/EBM, MPDG/MDR, AMG, Krankenhausrecht, Vertragsarztrecht und Arzthaftungsprozess.
- **Entscheidende Weiche:** Trenne Behandlungsfehler, Aufklärung, Dokumentation, Kausalität, Beweislast, Sozialleistungsbezug, Zulassung und Haftpflichtdeckung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Nutze diesen Skill im Plugin **Fachanwalt Medizinrecht**, wenn der Fall genau in diese Lage führt. Ziel ist keine allgemeine Belehrung, sondern ein steuerbarer Arbeitsweg mit Dokumentenlogik, Risikoampel, nächstem Schritt und sauberem Quellencheck.

**Fokus:** Behandlungsakte auditieren, Lücken, nachträgliche Änderungen, Metadaten und Beweisvermutung.

## Kaltstart-Fragen

- Welche Rolle liegt vor: Patient, Arzt, Klinik, Hersteller, Sponsor, KV, Kasse oder Behörde?
- Welche Maßnahme, welches Produkt, welches Datum und welcher Rechtsstand sind entscheidend?
- Gibt es Aufklärung, Einwilligung, Studien-/Registerunterlagen, Produktinformationen oder Meldebelege?
- Geht es um Prävention, Anspruch, Verteidigung, Erstattung, Behörde oder gerichtliche Durchsetzung?

## Prüf- und Arbeitslogik

- **Rechtsanker:** § 630f BGB, § 630h Abs. 3 BGB, DSGVO, ePA und gerichtliche Beweiswürdigung.
- **Tatsachenanker:** Behandlungs-/Therapiedatum, Rollen, Behandlungsdokumente, Aufklärung, Einwilligung, Freigaben, Befunde, Meldebelege, Beweiswert und offene Lücken trennen.
- **Risikoebenen:** Haftung, Berufsrecht, Datenschutz, Vergütung, Frist, Eskalation, Reputationsrisiko und Governance getrennt ausgeben.
- **Gegenposition:** die beste plausible Gegenansicht formulieren und sagen, welche Unterlage sie trägt oder entkräftet.
- **Entscheidung:** einen Minimalpfad für heute und einen robusten Hauptpfad für die nächsten Arbeitstage vorschlagen.

## Typische Fehlerquellen

- Innovative Medizin ist nicht automatisch Standard und nicht automatisch experimentell; Zeitpunkt und Datenlage sind zu trennen.
- Produkt-, Behandlungs-, Organisations- und Aufklärungsfehler nicht vermischen.
- Bei neuen EU-Regeln Übergangsfristen und nationale Durchführung gesondert prüfen.
- Gesundheitsdaten, Genomdaten und Patientengeheimnisse nur datensparsam verarbeiten.

## Output

- Mandats-/Fallvermerk mit Normenroute und Quellenstand.
- Dokumentenmatrix mit Lücken und Beweiswert.
- Risikoampel Haftung/Regulierung/Datenschutz/Erstattung.
- Nächster Schriftsatz-, Behörden- oder Mandantenkommunikationsbaustein.

## Quellen- und Aktualitätsgate

Vor tragenden Aussagen live prüfen: amtliche Normfassung, zuständige Behörde/Institution, frei zugängliche Rechtsprechung nur mit Gericht, Datum und Aktenzeichen. Keine BeckRS-/juris-/Kommentar-Blindzitate. Bei dynamischen Medizin-, EU-, Berufsrechts- und Vergütungsfragen immer den Stand des konkreten Tages nennen.

## Nützliche Startquellen

- BGB §§ 630a ff.: https://www.gesetze-im-internet.de/bgb/__630a.html
- BGB § 630h: https://www.gesetze-im-internet.de/bgb/__630h.html
- Product Liability Directive EU 2024/2853: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024L2853

## 2. `einwilligungsunfaehigkeit-ablehnung`

**Frühere Beschreibung:** Einwilligungsunfähigkeit und Ablehnung: moderner Medizinrechts-Skill für Therapieablehnung, natürliche Wille, Zwangsbehandlung, Betreuungsgericht und Klinikalltag. Mit Haftung, Aufklärung, Behördenweg, Beweislogik und Quellencheck.

# Einwilligungsunfähigkeit und Ablehnung

## Fachkern: Einwilligungsunfähigkeit und Ablehnung
- **Spezialgegenstand:** Einwilligungsunfähigkeit und Ablehnung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB §§ 630a ff., SGB V, ärztliches Berufsrecht, GOÄ/EBM, MPDG/MDR, AMG, Krankenhausrecht, Vertragsarztrecht und Arzthaftungsprozess.
- **Entscheidende Weiche:** Trenne Behandlungsfehler, Aufklärung, Dokumentation, Kausalität, Beweislast, Sozialleistungsbezug, Zulassung und Haftpflichtdeckung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Nutze diesen Skill im Plugin **Fachanwalt Medizinrecht**, wenn der Fall genau in diese Lage führt. Ziel ist keine allgemeine Belehrung, sondern ein steuerbarer Arbeitsweg mit Dokumentenlogik, Risikoampel, nächstem Schritt und sauberem Quellencheck.

**Fokus:** Therapieablehnung, natürliche Wille, Zwangsbehandlung, Betreuungsgericht und Klinikalltag.

## Kaltstart-Fragen

- Welche Rolle liegt vor: Patient, Arzt, Klinik, Hersteller, Sponsor, KV, Kasse oder Behörde?
- Welche Maßnahme, welches Produkt, welches Datum und welcher Rechtsstand sind entscheidend?
- Gibt es Aufklärung, Einwilligung, Studien-/Registerunterlagen, Produktinformationen oder Meldebelege?
- Geht es um Prävention, Anspruch, Verteidigung, Erstattung, Behörde oder gerichtliche Durchsetzung?

## Prüf- und Arbeitslogik

- **Rechtsanker:** BGB Betreuung, FamFG, §§ 630d/e BGB, Grundrechte und Dokumentation.
- **Tatsachenanker:** Behandlungs-/Therapiedatum, Rollen, Behandlungsdokumente, Aufklärung, Einwilligung, Freigaben, Befunde, Meldebelege, Beweiswert und offene Lücken trennen.
- **Risikoebenen:** Haftung, Berufsrecht, Datenschutz, Vergütung, Frist, Eskalation, Reputationsrisiko und Governance getrennt ausgeben.
- **Gegenposition:** die beste plausible Gegenansicht formulieren und sagen, welche Unterlage sie trägt oder entkräftet.
- **Entscheidung:** einen Minimalpfad für heute und einen robusten Hauptpfad für die nächsten Arbeitstage vorschlagen.

## Typische Fehlerquellen

- Innovative Medizin ist nicht automatisch Standard und nicht automatisch experimentell; Zeitpunkt und Datenlage sind zu trennen.
- Produkt-, Behandlungs-, Organisations- und Aufklärungsfehler nicht vermischen.
- Bei neuen EU-Regeln Übergangsfristen und nationale Durchführung gesondert prüfen.
- Gesundheitsdaten, Genomdaten und Patientengeheimnisse nur datensparsam verarbeiten.

## Output

- Mandats-/Fallvermerk mit Normenroute und Quellenstand.
- Dokumentenmatrix mit Lücken und Beweiswert.
- Risikoampel Haftung/Regulierung/Datenschutz/Erstattung.
- Nächster Schriftsatz-, Behörden- oder Mandantenkommunikationsbaustein.

## Quellen- und Aktualitätsgate

Vor tragenden Aussagen live prüfen: amtliche Normfassung, zuständige Behörde/Institution, frei zugängliche Rechtsprechung nur mit Gericht, Datum und Aktenzeichen. Keine BeckRS-/juris-/Kommentar-Blindzitate. Bei dynamischen Medizin-, EU-, Berufsrechts- und Vergütungsfragen immer den Stand des konkreten Tages nennen.

## Nützliche Startquellen

- BGB §§ 630a ff.: https://www.gesetze-im-internet.de/bgb/__630a.html
- BGB § 630h: https://www.gesetze-im-internet.de/bgb/__630h.html
- Product Liability Directive EU 2024/2853: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024L2853

## 3. `erezept-falschmedikation`

**Frühere Beschreibung:** E-Rezept und Falschmedikation: moderner Medizinrechts-Skill für E-Rezept, Medikationsliste, Wechselwirkung, Apotheken-/Arztfehler und Nachweisführung. Mit Haftung, Aufklärung, Behördenweg, Beweislogik und Quellencheck.

# E-Rezept und Falschmedikation

## Fachkern: E-Rezept und Falschmedikation
- **Spezialgegenstand:** E-Rezept und Falschmedikation wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB §§ 630a ff., SGB V, ärztliches Berufsrecht, GOÄ/EBM, MPDG/MDR, AMG, Krankenhausrecht, Vertragsarztrecht und Arzthaftungsprozess.
- **Entscheidende Weiche:** Trenne Behandlungsfehler, Aufklärung, Dokumentation, Kausalität, Beweislast, Sozialleistungsbezug, Zulassung und Haftpflichtdeckung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Nutze diesen Skill im Plugin **Fachanwalt Medizinrecht**, wenn der Fall genau in diese Lage führt. Ziel ist keine allgemeine Belehrung, sondern ein steuerbarer Arbeitsweg mit Dokumentenlogik, Risikoampel, nächstem Schritt und sauberem Quellencheck.

**Fokus:** E-Rezept, Medikationsliste, Wechselwirkung, Apotheken-/Arztfehler und Nachweisführung.

## Kaltstart-Fragen

- Welche Rolle liegt vor: Patient, Arzt, Klinik, Hersteller, Sponsor, KV, Kasse oder Behörde?
- Welche Maßnahme, welches Produkt, welches Datum und welcher Rechtsstand sind entscheidend?
- Gibt es Aufklärung, Einwilligung, Studien-/Registerunterlagen, Produktinformationen oder Meldebelege?
- Geht es um Prävention, Anspruch, Verteidigung, Erstattung, Behörde oder gerichtliche Durchsetzung?

## Prüf- und Arbeitslogik

- **Rechtsanker:** SGB V, Apothekenrecht, §§ 630a ff. BGB, § 823 BGB, Dokumentation und ePA-Schnittstellen.
- **Tatsachenanker:** Behandlungs-/Therapiedatum, Rollen, Behandlungsdokumente, Aufklärung, Einwilligung, Freigaben, Befunde, Meldebelege, Beweiswert und offene Lücken trennen.
- **Risikoebenen:** Haftung, Berufsrecht, Datenschutz, Vergütung, Frist, Eskalation, Reputationsrisiko und Governance getrennt ausgeben.
- **Gegenposition:** die beste plausible Gegenansicht formulieren und sagen, welche Unterlage sie trägt oder entkräftet.
- **Entscheidung:** einen Minimalpfad für heute und einen robusten Hauptpfad für die nächsten Arbeitstage vorschlagen.

## Typische Fehlerquellen

- Innovative Medizin ist nicht automatisch Standard und nicht automatisch experimentell; Zeitpunkt und Datenlage sind zu trennen.
- Produkt-, Behandlungs-, Organisations- und Aufklärungsfehler nicht vermischen.
- Bei neuen EU-Regeln Übergangsfristen und nationale Durchführung gesondert prüfen.
- Gesundheitsdaten, Genomdaten und Patientengeheimnisse nur datensparsam verarbeiten.

## Output

- Mandats-/Fallvermerk mit Normenroute und Quellenstand.
- Dokumentenmatrix mit Lücken und Beweiswert.
- Risikoampel Haftung/Regulierung/Datenschutz/Erstattung.
- Nächster Schriftsatz-, Behörden- oder Mandantenkommunikationsbaustein.

## Quellen- und Aktualitätsgate

Vor tragenden Aussagen live prüfen: amtliche Normfassung, zuständige Behörde/Institution, frei zugängliche Rechtsprechung nur mit Gericht, Datum und Aktenzeichen. Keine BeckRS-/juris-/Kommentar-Blindzitate. Bei dynamischen Medizin-, EU-, Berufsrechts- und Vergütungsfragen immer den Stand des konkreten Tages nennen.

## Nützliche Startquellen

- BMG ePA für alle: https://www.bundesgesundheitsministerium.de/themen/digitalisierung/elektronische-patientenakte/epa-fuer-alle
- BfArM DiGA: https://www.bfarm.de/DE/Medizinprodukte/Aufgaben/DiGA-und-DiPA/DiGA/_node.html
- EHDS Regulation EU 2025/327: https://eur-lex.europa.eu/eli/reg/2025/327/oj/

## 4. `erstgespraech-mandatsannahme`

**Frühere Beschreibung:** Erstgespraeach und Mandatsannahme im Arzthaftungs- Berufs- und Vertragsarztrecht: Anwendungsfall Patient oder Arzt meldet sich mit unstrukturiertem Sachverhalt zu Behandlungsfehler Approbationsproblem oder KV-Streit. § 630a BGB Behandlungsvertrag, § 43a BRAO Interessenkonflikte, § 3a RVG Honorar. Prüfraster Konstellation einordnen Arzthaftung Berufsrecht oder Vertragsarztrecht, Interessenkonflikt-Check, Vollmacht einholen, Streitwert und Gebührenvereinbarung, Fristen-Erstprognose. Output Mandats-Aufnahmeprotokoll mit Einordnung Sofortmassnahmen und Handlungsweichen. Abgrenzung zu Mandat-Triage-Medizinrecht und zu Erstgespraeach-Strafrecht.

# Erstgespraech und Mandatsannahme im Arzthaftungs-, Berufs- und Vertragsarztrecht

## Fachkern: Erstgespraech und Mandatsannahme im Arzthaftungs-, Berufs- und Vertragsarztrecht
- **Spezialgegenstand:** Erstgespraech und Mandatsannahme im Arzthaftungs-, Berufs- und Vertragsarztrecht wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB §§ 630a ff., SGB V, ärztliches Berufsrecht, GOÄ/EBM, MPDG/MDR, AMG, Krankenhausrecht, Vertragsarztrecht und Arzthaftungsprozess.
- **Entscheidende Weiche:** Trenne Behandlungsfehler, Aufklärung, Dokumentation, Kausalität, Beweislast, Sozialleistungsbezug, Zulassung und Haftpflichtdeckung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wann dieser Skill greift

- Neue Anfrage aus dem Bereich Arzthaftungs-, Berufs- und Vertragsarztrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klaeren, Konflikt- und GwG-Pruefung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster fuer Arzthaftungs-, Berufs- und Vertragsarztrecht:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klaegerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Behandlungsfehler, Aufklaerung, Sozialrecht/SGB V, Praxisuebernahme, MBO-AE
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Arzthaftungsklage, Klage Sozialgericht (KV-/MDK-Streit), Berufsrechtsbeschwerde). Frist-Alarm an die Vorbereitung weitergeben.

### 2. Konflikt-Pruefung und GwG-Check (5 Min.)

- Konflikt-Check ueber Mandantsystem: Gegnerin, Streitgegenstand, frueherer Mandant?
- GwG-Identifizierung: amtlicher Lichtbildausweis (Ausweisscan), bei juristischer Person Handelsregister-/Transparenzregister-Auszug, ggf. wirtschaftlich Berechtigte/n.
- Risikobewertung (niedrig/mittel/hoch) abhaengig von Mandatscharakter, Bargeld, Auslandsbezug.
- Doku im Mandatsbogen (Pflicht nach §§ 10 ff. GwG i.V.m. § 2 Abs. 1 Nr. 10 GwG fuer RA-Mandate).

### 3. Vollmacht und Schweigepflichtentbindung

- Allgemeine Prozess-/Aussenvollmacht (BORA, ZPO, FamFG, je nach Fachgebiet).
- Spezielle Vollmachten: ggf. Akteneinsicht Strafakte, KV-Abrechnungsdaten, Sozialdaten (Schweigepflichtentbindung gegenueber Krankenkasse, Arzt, Behoerde).
- Bei Eheleuten/GbR/GmbH: einzelvollmachtgebende Person und Vertretungsmacht klaeren.

### 4. Streitwert und Gebuehrenvereinbarung

Standard-Streitwerte im Bereich Arzthaftungs-, Berufs- und Vertragsarztrecht:

- Skizze: Streitwert grob abschaetzen (z.B. Hauptforderung, ggf. + Zinsen, Nebenforderungen).
- RVG-Pauschalrechnung (Berechnungstool im Plugin) oder Stundenhonorarvereinbarung.
- Beratungshilfe-/Prozesskostenhilfe-Antrag pruefen, wenn wirtschaftlich angezeigt.
- Vorschussanforderung nach § 9 RVG.

### 5. Strategie-Erstskizze

Drei Weichen am Ende des Erstgespraechs:

- **Mandat annehmen:** vollstaendig (Pruefung + Schriftsatz) oder begrenzt (nur Pruefung/Gutachten).
- **Verweisen:** wenn Spezialgebiet ausserhalb der Fachanwaltschaft, oertlich unzustaendig oder Konflikt.
- **Ablehnen:** offensichtlich aussichtslos, GwG-Hit, Bauchgefuehl-Vorsicht.

## Pflicht-Output am Ende

1. **Mandatsbogen** mit Beteiligten, Konflikt-Check, GwG-Status, Streitwert.
2. **Frist-Liste** (Sofortfristen, Verjaehrung, Ausschlussfristen, Beweisanforderungs-Fristen).
3. **Anlagenverzeichnis** des uebergebenen Datenraums (Stand erstes Sortieren).
4. **Naechster-Schritt-Plan:** binnen 24/48/72 h, Owner, Output.
5. **Honorarvereinbarung** unterschrieben oder Vorbehalt notiert.

## Relevante Rechtsgrundlagen und Standards

- BORA, BRAO, FAO fuer Fachanwaltschaft Arzthaftungs-, Berufs- und Vertragsarztrecht.
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- §§ 630a ff. BGB, MBO-AE, SGB V, MPDG, GOAE, BAEO (fuer fachliche Erstpruefung).
- DSGVO und BDSG fuer den Umgang mit Mandantendaten (Art. 6 DSGVO als Rechtsgrundlage, Art. 9 ggf. Gesundheitsdaten).

## Typische Fehler im Erstgespraech

- Frist uebersehen, weil Mandantin sie nicht selber genannt hat (immer aus jedem Schreiben Frist herausziehen).
- Konflikt-Check nur nach Personennamen, nicht nach Sachzusammenhang (gleiche Liegenschaft, gleicher Sachverhalt).
- Vollmachtsumfang unklar -> spaeter Streit mit Mandantin ueber Befugnisse.
- Honorarvereinbarung muendlich -> Beweisnot bei Streitwert-/Honorar-Streit.
- GwG: kein Lichtbildausweis erfasst, kein Aktenvermerk ueber Risikobewertung.

## Praxis-Checkliste

- [ ] Personalien und Rolle aller Beteiligten erfasst
- [ ] Konflikt-Check durchgefuehrt
- [ ] GwG: Identifizierung + Risikobewertung notiert
- [ ] Allgemeine Vollmacht unterschrieben
- [ ] Speziale Vollmacht / Entbindungserklaerung (wo noetig) unterschrieben
- [ ] Streitwert geschaetzt
- [ ] Honorarvereinbarung unterschrieben oder ausdruecklich auf RVG verwiesen
- [ ] Fristenliste angelegt und in Kalender eingetragen
- [ ] Mandatsbogen vollstaendig
- [ ] Naechster-Schritt-Plan dem Mandanten kommuniziert (E-Mail-Zusammenfassung)


## Konkrete Praxis-Konstellationen

### Konstellation A: Eilbeduerftigkeit

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Arzthaftungs-, Berufs- und Vertragsarztrecht). Handlungs-Sequenz:

1. Sofort-Vollmacht und Sofort-Akteneinsicht (per beA, ELSTER, Behoerdenportal).
2. Antrag auf Wiedereinsetzung (§ 233 ZPO, § 60 VwGO, § 110 AO) als Reserve dokumentieren.
3. Spaeteste-Stunde-Versand-Plan: beA bevorzugt, mit qualifizierter Signatur und Empfangsbekenntnis.
4. Honorarvereinbarung NICHT auf Eilzuschlag verzichten - aber transparent kommunizieren.

### Konstellation B: Komplexer Sachverhalt, Datenraum unsortiert

Mandant uebergibt 200+ Dateien (PDF-Scans, E-Mails, Excel-Listen). Vor jeder fachlichen Bewertung:

1. Datenraum-Index in Excel: Datum, Absender, Empfaenger, Aktenzeichen, kurze Inhaltszeile.
2. Chronologischer Verlauf als Zeitstrahl - Spielraum fuer Verjaehrungs- und Ausschlussfristen identifizieren.
3. Loecher im Datenraum gezielt anfordern (Mandantenfragen-Katalog).

### Konstellation C: Interessenkonflikt-Naehe

Frueheres Mandat mit derselben Gegnerin oder gleichem Sachzusammenhang. Pruefung:

1. § 43a Abs. 4 BRAO und § 3 BORA - Sachzusammenhang, nicht nur Personenidentitaet.
2. Einwilligung beider Mandanten in Textform (mit konkreter Beschreibung).
3. Bei Zweifel: Mandat ablehnen und an Kanzleikollegium ueberweisen.

## Mandanten-Erwartungsmanagement

- Realistische Erfolgs- und Kostenprognose (nicht "Wir gewinnen sicher").
- Verfahrensdauer im Bereich Arzthaftungs-, Berufs- und Vertragsarztrecht: Erfahrungswerte nach Instanz.
- Vergleichschance vs. streitiges Urteil als Option offen halten.
- Schriftliche Zusammenfassung des Erstgespraechs binnen 48 h.

## Honorarvereinbarung - Best Practices

- RVG-Basis als Default, Stundenhonorar nur mit gesondertem Hinweis nach § 3a RVG.
- Erfolgshonorar nur in den engen Grenzen § 4a RVG.
- Vorschuss in Hoehe der voraussichtlichen 1. Instanz.
- Klarstellung: Auslagen-Pauschale, USt, Reisekosten, Sachverstaendigenkosten gesondert.
- Bei PKH/Beratungshilfe-Mandant: schriftliche Belehrung, dass eigene Beitraege moeglich sind.

## Mandatsbogen-Muster (Mindestinhalt)

- Mandant (Name, Geburtsdatum, Anschrift, Telefon, E-Mail)
- Gegner (Name, Anschrift, ggf. anwaltliche Vertretung)
- Kurzbeschreibung Sachverhalt (5-10 Saetze)
- Ziel des Mandats (eine Zeile)
- Strittige Fragen (bullet)
- Geprueft: Konflikt - GwG - Vollmacht
- Streitwert (Schaetzung)
- Honorarvereinbarung (RVG/Stunde/Pauschale)
- Frist-Liste
- Aktenanlage Datum
- Naechster-Schritt

## Cross-Refs

- `vergleichsverhandlung-strategie` (im selben Plugin) fuer den Fall, dass aussergerichtliche Loesung angestrebt wird.
- `schriftsatzkern-substantiierung` (im selben Plugin) fuer den Schriftsatzaufbau, wenn Klage/Widerspruch eingereicht wird.
- Kanzlei-Allgemein-Plugin `kanzlei-allgemein` fuer Konflikt-, GwG- und PEP-Pruefroutinen.

## Vertiefung — Normenkette und Rechtsprechung Erstgespräch Medizinrecht

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normenkette Erstgespräch / Mandatsannahme

§ 630g BGB (Einsichtsrecht Patientenakte) → §§ 10, 11 GwG (Identifizierungspflicht RA-Mandat) → §§ 43a, 45 BRAO (Interessenkonflikt, Verschwiegenheit) → §§ 3, 3a RVG (Vergütungsvereinbarung, Stundenhonorar) → § 9 RVG (Vorschuss) → §§ 195, 199 BGB (Verjährung im Mandat sichern) → § 204 BGB (Hemmung: Klage, Mahnbescheid, Schlichtungsantrag § 278 BGB analog)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 5. `fachanwalt-medizinrecht-aufklaerungsfehler`

**Frühere Beschreibung:** Workflow-Skill zu fachanwalt medizinrecht aufklaerungsfehler. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen.

# Aufklärungsfehler

## Fachkern: Aufklärungsfehler
- **Spezialgegenstand:** Aufklärungsfehler wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB §§ 630a ff., SGB V, ärztliches Berufsrecht, GOÄ/EBM, MPDG/MDR, AMG, Krankenhausrecht, Vertragsarztrecht und Arzthaftungsprozess.
- **Entscheidende Weiche:** Trenne Behandlungsfehler, Aufklärung, Dokumentation, Kausalität, Beweislast, Sozialleistungsbezug, Zulassung und Haftpflichtdeckung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Kaltstart-Rückfragen

1. Welcher Eingriff war Gegenstand der Aufklärung — Operation, invasive Diagnostik, Medikamentengabe, Off-Label-Use?
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Wer hat aufgeklärt — Operateur, anderer Arzt, qualifizierte Mitarbeiter? Lagen Aufklärungsbögen unterschrieben vor?
4. Welche Risiken wurden besprochen oder unterlassen — eingriffsspezifische Risiken, Alternativen, Nachbehandlung?
5. Welcher Schaden ist eingetreten und ist er von der unterlassenen Aufklärung umfasst?
6. Sprachliche Barrieren — wurde ein Dolmetscher eingesetzt oder ein fremdsprachiger Bogen ausgehändigt?
7. Handelte es sich um eine Eilsituation — liegt mutmaßliche Einwilligung gemäß § 630d Abs. 1 Satz 4 BGB in Betracht?
8. Kann der Mandant plausibel einen Entscheidungskonflikt schildern — konkrete Gründe, warum er bei richtiger Aufklärung nicht oder anders entschieden hätte?

## Anspruchsgrundlagen

- Aufklärungspflicht § 630e Abs. 1 BGB — über sämtliche für die Einwilligung wesentlichen Umstände, insbesondere Art, Umfang, Durchführung, zu erwartende Folgen, Risiken, Notwendigkeit, Dringlichkeit, Eignung, Erfolgsaussichten der Maßnahme und Alternativen.
- Form § 630e Abs. 2 BGB — mündlich, persönlich durch den Behandelnden oder eine Person mit notwendiger Ausbildung, rechtzeitig vor dem Eingriff so dass Patient wohlüberlegt entscheiden kann. Schriftliche Bögen ergänzen aber ersetzen Gespräch nicht.
- Rechtzeitigkeit — bei stationären Operationen Vortag oder davor; bei ambulanten Eingriffen zumindest am Tag selbst aber vor Beginn der Vorbereitung.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Selbstbestimmungsaufklärung: ihre Verletzung führt zur Rechtswidrigkeit der Behandlung und damit Haftung für jeden eingetretenen Schaden (§§ 823 Abs. 1, 280 BGB).
- Beweislast § 630h Abs. 2 BGB — Behandelnder muss Aufklärung und wirksame Einwilligung darlegen und beweisen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Mutmaßliche Einwilligung § 630d Abs. 1 Satz 4 BGB: bei Notfall und fehlender Einwilligungsfähigkeit nach dem mutmaßlichen Willen handeln.

### BGH-Rechtsprechung (Stand Mai 2026)

- BGH 21.01.2025 — VI ZR 204/22 (VI. Zivilsenat): Beweislast für hypothetische Einwilligung trägt nach § 630h Abs. 2 Satz 2 BGB der Behandelnde, nicht der Patient; der Patient muss lediglich plausibel einen Entscheidungskonflikt darlegen. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=21.01.2025&Aktenzeichen=VI+ZR+204/22
- BGH 25.11.2025 — VI ZR 165/23: Weitere Vertiefung zur hypothetischen Einwilligung. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=25.11.2025&Aktenzeichen=VI+ZR+165/23

Weitere Entscheidungen vor Ausgabe in dejure.org / openjur.de live verifizieren.

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Beweislast und Verteidigungsstrategie

| Frage | Beweislast |
|---|---|
| Aufklärung erfolgt | Behandelnder § 630h Abs. 2 |
| Inhalt der Aufklärung | Behandelnder |
| Rechtzeitigkeit | Behandelnder |
| Hypothetische Einwilligung | Behandelnder (Behauptungslast) + Arzt substantiiert + plausibler Entscheidungskonflikt Patient |
| Verständnis Patient | Behandelnder im Zweifel |
| Folgenkausalität | Patient — eingetretene Folge muss eine sein die aufzuklären gewesen wäre |
| Sprachkompetenz | Behandelnder — Dolmetscher eingesetzt oder dokumentiert? |

## Prüfschema

| Nr. | Prüfschritt | Norm | Kernfrage |
|---|---|---|---|
| 1 | Einwilligungsbedürftige Maßnahme | § 630d BGB | Eingriff in Körper oder Gesundheit? |
| 2 | Inhalt Aufklärungspflicht | § 630e Abs. 1 BGB | Diagnose, Verlauf, Folgen, Risiken, Alternativen alle genannt? |
| 3 | Person des Aufklärenden | § 630e Abs. 2 Nr. 1 BGB | Arzt mit notwendiger Ausbildung, idealerweise Operateur? |
| 4 | Zeitpunkt Rechtzeitigkeit | § 630e Abs. 2 Nr. 2 BGB | Stationär: Vortag? Ambulant: am Tag selbst? |
| 5 | Verständlichkeit, Sprache | § 630e Abs. 2 Nr. 3 BGB | Dolmetscher? Fremdsprachiger Bogen? |
| 6 | Schriftlicher Bogen als Ergänzung | § 630h Abs. 2 BGB | Individualisiert oder Standardformular? |
| 7 | Beweislast Aufklärung | § 630h Abs. 2 BGB | Arzt muss Aufklärung beweisen |
| 8 | Kausalität | BGH 21.01.2025 — VI ZR 204/22 | Eingetretene Folge ist von nicht aufgeklärtem Risiko umfasst; hypothetische Einwilligung — Beweislast beim Arzt |
| 9 | Hypothetische Einwilligung | § 630h Abs. 2 S. 2 BGB; BGH 21.01.2025 — VI ZR 204/22 | Patient muss plausiblen Entscheidungskonflikt darlegen; Beweis trägt der Behandelnde |
| 10 | Schadensumfang | §§ 249, 253 BGB | Alle Folgen der rechtswidrigen Behandlung |

## Häufige Aufklärungsmängel

- Pauschale Aufklärungsbögen ohne individuelles Gespräch.
- Aufklärung durch nicht qualifiziertes Personal (Pflegekraft, Assistenzarzt ohne notwendige Ausbildung).
- Zeitlich zu nah am Eingriff (am Operationstisch, nach Praemedikation).
- Fehlende Aufklärung über Behandlungsalternativen (konservative Therapie, andere OP-Methode).
- Fehlende Aufklärung über typische schwerwiegende Risiken auch wenn selten.
- Sprach- oder Verständnisbarrieren nicht überbrückt.
- Keine Aufklärung über neue/experimentelle Methode mit weniger Erfahrung.

## Schreibvorlage Anspruchsanmeldung Aufklärungsfehler

```
An die [Klinik / Versicherer der Klinik]

Schadensanmeldung — Aufklaerungsfehler nach §§ 630e 630h BGB

I. Sachverhalt
Eingriff am [Datum] zwecks [Behandlungsziel]. Aufklaerung erfolgte
am [Datum Uhrzeit] durch [Behandler]. Es wurden keine bzw.
unzureichende Hinweise gegeben auf:
1. Eingriffsspezifisches Risiko [Bezeichnung]
2. Behandlungsalternativen [konservative Therapie / anderes Verfahren]
3. Notwendigkeit und Dringlichkeit
4. Folgen bei Nichtbehandlung

Die schriftliche Dokumentation ist unzureichend — der Aufklaerungs-
bogen ist Standardformular ohne individuelle Eintragungen.

II. Rechtliche Bewertung
Die Behandlung ist mangels wirksamer Einwilligung als rechtswidriger
Eingriff in die koerperliche Unversehrtheit § 823 Abs. 1 BGB
einzuordnen. Beweislast fuer ordnungsgemaesse Aufklaerung traegt
gemaess § 630h Abs. 2 BGB die Klinik.

III. Hypothetische Einwilligung
Die hypothetische Einwilligung wird vorsorglich bestritten. Bei
ordnungsgemaesser Aufklaerung haette die Patientin / der Patient
sich in einen plausiblen Entscheidungskonflikt befunden, weil
[konkret: weniger invasive Alternativen, Familienruecksprache,
beruflicher Termin, religioese Ueberzeugungen].

IV. Schaden
- Primaerschaden:   [Folge des Risikos das eingetreten ist]
- Schmerzensgeld:   EUR ____
- Heilbehandlung:   EUR ____
- Verdienstausfall: EUR ____

V. Forderung
Anerkennung dem Grunde nach binnen vier Wochen, Vorschuss EUR ____.
Verjaehrungsverzichtserklaerung erbeten bis [Datum + 12 Monate].

Anlagen:
- Aufklaerungsbogen Kopie
- Behandlungsdokumentation
- aerztliche Atteste Folgeschaeden
- Vollmacht

[Unterschrift, Anwalt]
```

## Fristen und Verjährung

| Frist | Dauer | Norm |
|---|---|---|
| Regelverjährung | 3 Jahre ab Jahresende der Kenntnis | §§ 195, 199 Abs. 1 BGB |
| Absolute Höchstfrist | 30 Jahre ab Verletzungshandlung | § 199 Abs. 2 BGB |
| Hemmung Schlichtung | Während Laufzeit | § 204 Abs. 1 Nr. 4 BGB |
| Verhandlungshemmung | Während laufender Verhandlungen | § 203 BGB |

## Typische Gegenargumente und Reaktion

| Einwand Arzt | Reaktion Patient |
|---|---|
| Hypothetische Einwilligung — Patient hätte ohnehin zugestimmt | Beweislast für hypothetische Einwilligung trägt der Arzt: BGH 21.01.2025 — VI ZR 204/22; Patient muss nur plausiblen Entscheidungskonflikt darlegen |
| Eilsituation — mutmaßliche Einwilligung | § 630d Abs. 1 Satz 4 BGB: Eilsituation muss dokumentiert sein; Grenze bei planbaren Eingriffen |
| Standardbogen ersetzt Gespräch | § 630e Abs. 2 BGB — Bogen ergänzt, ersetzt aber nicht das individuelle Aufklärungsgespräch |
| Begleitperson hat zugestimmt | Eigene Einwilligung des einwilligungsfähigen Patienten erforderlich; Begleitperson kann nur ergänzen |

## Streitwert und Kosten

- Schmerzensgeld bei rechtswidriger Körperverletzung ohne Behandlungsfehler: 3.000–50.000 EUR je nach Schwere.
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
- Sachverständige zum Aufklärungsstandard: 5.000–15.000 EUR.
- LG-Kosten bei 20.000 EUR: ca. 979 EUR.
- RVG Anwalt bei 20.000 EUR: ca. 2.000 EUR netto.

## Übergabe

- Bei Ablehnung Klage; gerichtliches Sachverständigengutachten zum Aufklärungsstandard.
- Bei vermutetem Behandlungsfehler zusätzlich Skill `fachanwalt-medizinrecht-behandlungsfehler-pruefen`.
- Schlichtungsverfahren bei Ärztekammer parallel möglich.
- Verjährungsverzicht einholen bei laufenden Verhandlungen.

## Quellen

- BGB §§ 630c, 630d, 630e, 630h, 823, 253, 249
- BGH 21.01.2025 — VI ZR 204/22 (Beweislast hypothetische Einwilligung): https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=21.01.2025&Aktenzeichen=VI+ZR+204/22
- BGH 25.11.2025 — VI ZR 165/23 (Vertiefung hypothetische Einwilligung): https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=25.11.2025&Aktenzeichen=VI+ZR+165/23
- Weitere Rechtsprechung vor Ausgabe in dejure.org / openjur.de live verifizieren.
- Literatur nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle; keine Kommentar-, Handbuch- oder Aufsatzblindzitate.
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.

<!-- AUDIT 27.05.2026
Datum 28.01.2014 fuer ein 2015-AZ unmoeglich (chronologischer Widerspruch).
Ersatz: BGH VI ZR 323/04 (13.06.2006, BGHZ 168, 103) — verifiziert auf dejure.org;
betrifft Aufklaerungspflicht bei Neulandmethode (Robodoc-Operation), inhaltlich passend.
-->

## 6. `fachanwalt-medizinrecht-behandlungsfehler-pruefen`

**Frühere Beschreibung:** Behandlungsfehler §§ 630a 630h BGB Verletzung medizinischer Standard. Diagnosefehler Therapiefehler Befunderhebungsfehler Hygienefehler. Beweisregeln § 630h BGB Vermutung Kausalität bei grobem Behandlungsfehler § 630h Abs. 5 BGB Befunderhebungsfehler Dokumentationsmangel. Schadensersatzanspruch §§ 280 823 BGB Schmerzensgeld § 253 BGB. Verjährung drei Jahre § 195 BGB ab Kenntnis 30 Jahre Hoechstfrist.

# Behandlungsfehler prüfen

## Fachkern: Behandlungsfehler prüfen
- **Spezialgegenstand:** Behandlungsfehler prüfen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB §§ 630a ff., SGB V, ärztliches Berufsrecht, GOÄ/EBM, MPDG/MDR, AMG, Krankenhausrecht, Vertragsarztrecht und Arzthaftungsprozess.
- **Entscheidende Weiche:** Trenne Behandlungsfehler, Aufklärung, Dokumentation, Kausalität, Beweislast, Sozialleistungsbezug, Zulassung und Haftpflichtdeckung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Kaltstart-Rückfragen

1. Welche Behandlung (Diagnose, Therapie, Operation, Pflege) und welcher Behandler (Vertrags-, Anstaltsarzt, Krankenhaus)? Datum, Klinik, behandelnde Personen?
2. Welche gesundheitlichen Folgen — Primärschaden, Folgeschäden, dauerhafte Beeinträchtigung, Tod?
3. Wurde die Behandlungsdokumentation angefordert (§ 630g BGB) und liegt sie vollständig vor?
4. Gibt es bereits ein MDK-Gutachten, ein Schlichtungsverfahren bei der Ärztekammer oder ein außergerichtliches Gutachten?
5. Wann hat der Patient bzw. seine Erben Kenntnis vom möglichen Behandlungsfehler und vom Schädiger erlangt (Verjährungsbeginn § 199 BGB)?
6. Liegt ein Befunderhebungsfehler vor — welche Untersuchung wurde unterlassen und was hätte sie wahrscheinlich ergeben?
7. War ein Anfänger am Werk — hatte er die erforderliche Ausbildung für den Eingriff?
8. Besteht der Verdacht auf ein voll beherrschbares Risiko (Hygiene, Gerätepflege, Lagerung, Sterilität)?

## Anspruchsgrundlagen

- Behandlungsvertrag § 630a Abs. 1 BGB — Dienstvertrag besonderer Art; Pflicht zur Behandlung nach den allgemein anerkannten fachlichen Standards § 630a Abs. 2 BGB.
- Pflichtverletzung — Behandlungsfehler liegt bei Abweichung vom medizinischen Standard zum Behandlungszeitpunkt vor (ex-ante-Maßstab).
- Schadensersatz § 280 Abs. 1 BGB i. V. m. § 630a BGB; deliktisch § 823 Abs. 1 BGB (Körper, Gesundheit); Schmerzensgeld § 253 Abs. 2 BGB.
- Beweislastregeln § 630h BGB:
  - § 630h Abs. 1: Voll beherrschbares Risiko (Hygiene, Geräte) — Vermutung des Behandlungsfehlers bei Schadenseintritt.
  - § 630h Abs. 3: Fehlende Dokumentation pflichtgemäßer Maßnahmen — Vermutung des Nichtdurchführens.
  - § 630h Abs. 4: Fehlende Befähigung (Anfänger-Operateur ohne ausreichende Erfahrung) — Vermutung Behandlungsfehler.
  - § 630h Abs. 5 Satz 1: Bei grobem Behandlungsfehler Kausalitätsvermutung für Primärschaden.
  - § 630h Abs. 5 Satz 2: Bei Befunderhebungsmangel mit hinreichend wahrscheinlichem positivem Befund Beweislastumkehr für Kausalität.
- Verjährung § 195 BGB drei Jahre ab Schluss des Jahres mit Kenntnis von Schaden und Schädiger (§ 199 Abs. 1 BGB); absolut 30 Jahre § 199 Abs. 2 BGB bei Verletzung Körper Gesundheit Leben Freiheit.

### Schlüsselentscheidungen BGH (Stand Mai 2026)

- BGH 21.01.2025 — VI ZR 204/22: Behandelnder trägt Darlegungs- und Beweislast für hypothetische Einwilligung nach § 630h Abs. 2 Satz 2 BGB. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=21.01.2025&Aktenzeichen=VI+ZR+204/22
- BGH 25.11.2025 — VI ZR 51/24: Krankenhaushaftung bei unzureichend organisiertem ärztlichen Nachtdienst. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=25.11.2025&Aktenzeichen=VI+ZR+51/24
- BGH 25.11.2025 — VI ZR 165/23: Weitere Konkretisierung hypothetische Einwilligung. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=25.11.2025&Aktenzeichen=VI+ZR+165/23

Weitere Entscheidungen vor Ausgabe in dejure.org / openjur.de mit Gericht, Datum, Aktenzeichen und tragender Aussage verifizieren.

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Beweislast — Übersicht

| Anspruchsmerkmal | Grundsatz | Ausnahme nach § 630h BGB |
|---|---|---|
| Behandlungsfehler | Patient | Vermutung bei voll beherrschbarem Risiko § 630h Abs. 1 |
| Pflicht zur Befundung | Patient | Dokumentationsmangel § 630h Abs. 3 |
| Anfängerfehler | Patient | Vermutung § 630h Abs. 4 |
| Kausalität Primärschaden | Patient | Beweislastumkehr grob § 630h Abs. 5 Satz 1 |
| Kausalität Befunderhebungsfehler | Patient | § 630h Abs. 5 Satz 2 wenn Befund hinreichend wahrscheinlich war |
| Folgeschaden | Patient | § 287 ZPO Beweismaß abgesenkt |

## Fehlertypen und Beweiskonsequenzen

| Fehlertyp | Beschreibung | Beweislastfolge |
|---|---|---|
| Diagnostischer Fehler | Befund falsch erhoben oder falsch gedeutet | Patient beweist; bei Befunderhebungsfehler § 630h Abs. 5 Satz 2 |
| Therapeutischer Fehler | Falsche Indikation, Methode, Durchführung | Patient beweist; bei grobem Fehler § 630h Abs. 5 Satz 1 |
| Hygiene/Geräte | Voll beherrschbares Risiko | Beweislastumkehr § 630h Abs. 1 |
| Dokumentationsmangel | Kein Nachweis durchgeführter Maßnahmen | Vermutung § 630h Abs. 3 |
| Anfänger ohne Erfahrung | Eingriff ohne ausreichende Übung | Vermutung § 630h Abs. 4 |
| Organisationsfehler | Fehlende Apparate, schlechte Koordination | Patient; bei voll beherrschbarem Risiko Umkehr |

## Verfahrens-Roadmap

1. Behandlungsdokumentation einfordern (§ 630g BGB) — vollständig, ggf. mit Bilddateien, Laborwerten, Pflegeprotokollen.
2. Außergerichtliches Privatgutachten oder MDK-Gutachten (kostenfrei) oder Ärztekammer-Schlichtungsverfahren (ebenfalls kostenfrei, Hemmung § 204 BGB).
3. Bei Bestätigung Behandlungsfehler: Geltendmachung außergerichtlich; Verjährungsverzicht einholen.
4. Bei Ablehnung Klage Land- oder Amtsgericht je Streitwert.
5. Gerichtliches Sachverständigengutachten und ggf. Obergutachten.

## Schreibvorlage Anforderung Behandlungsdokumentation § 630g BGB

```
An [Klinik / Arztpraxis]

Sehr geehrte Damen und Herren,

namens und in Vollmacht der Patientin / des Patienten [Name geboren
am Datum] in Behandlung bei Ihnen vom [Datum] bis [Datum] fordern
wir hiermit auf

innerhalb von 14 Tagen vollstaendig und unverzueglich

die vollstaendige Behandlungsdokumentation § 630g BGB zu uebersenden
insbesondere

- Aufnahme- und Entlassungsberichte
- Operationsberichte mit Anaesthesieprotokoll
- Pflegedokumentation
- Befundberichte aller diagnostischen Massnahmen
- Bildgebung (Roentgen CT MRT mit Originaldaten DICOM)
- Laborwerte vollstaendig
- Medikationsplaene
- Aufklaerungsboegen
- Konsilberichte

In Kopie. Etwaige Kosten werden uebernommen § 630g Abs. 2 Satz 2 BGB.

Mit kollegialen Gruessen
[Unterschrift, Anwalt]
Anlage: Vollmacht
```

## Schreibvorlage außergerichtliche Anspruchsanmeldung

```
An die [Haftpflichtversicherung der Klinik / des Arztes]

Schadensanmeldung Behandlungsfehler vom [Datum]

I. Sachverhalt der Behandlung
Patientin / Patient [Name, Geburtsdatum] befand sich vom [Datum]
bis [Datum] in stationaerer / ambulanter Behandlung.
[Diagnose, Anlass, Behandlungsverlauf, Komplikation]

II. Behandlungsfehler
1. Verstoss gegen medizinischen Standard § 630a Abs. 2 BGB:
   [Konkrete Massnahme / Unterlassung, Abweichung vom Standard]

2. Befunderhebungsfehler § 630h Abs. 5 Satz 2 BGB:
   Unterlassen der Untersuchung [X]; ein positiver Befund war
   hinreichend wahrscheinlich; Beweislastumkehr greift.

3. Voll beherrschbares Risiko § 630h Abs. 1 BGB (falls anwendbar):
   [Hygienemangel / Geraetedefekt] — Vermutung des Fehlers.

III. Schaeden
- Primaerschaden:      [Verletzung / Gesundheitsschaden]
- Folgeschaeden:       [Funktionseinschraenkung dauerhaft]
- Schmerzensgeld:      EUR ____ (Tabellen-Referenz)
- Heilbehandlung:      EUR ____
- Verdienstausfall:    EUR ____
- Haushaltsfuehrung:   EUR ____ / Monat
- Vermehrte Beduerfn.: EUR ____ / Monat (§ 843 BGB)
- Beerdigungskosten:   EUR ____ (§ 844 Abs. 1 BGB bei Tod)
- Unterhaltsschaden:   EUR ____ / Monat (§ 844 Abs. 2 BGB)

IV. Forderung
Anerkennung dem Grunde nach und Vorschuss EUR ____
binnen vier Wochen.

V. Verjaehrung
Wir bitten um Verjaehrungsverzichtserklaerung bis [Datum + 12 Monate].

Anlagen: Behandlungsdokumentation, aerztl. Atteste, Vollmacht

[Unterschrift]
```

## Fristen und Verjährung

| Frist | Dauer | Norm |
|---|---|---|
| Regelverjährung | 3 Jahre ab Jahresende der Kenntnis | §§ 195, 199 Abs. 1 BGB |
| Absolute Höchstfrist | 30 Jahre ab Verletzungshandlung | § 199 Abs. 2 BGB |
| Schlichtungsverfahren Hemmung | Während Laufzeit | § 204 Abs. 1 Nr. 4 BGB |
| Dokumentation Aufbewahrung | 10 Jahre (Behandler-Pflicht) | § 630f Abs. 3 BGB |
| GKV-Regressanspruch | 3 Jahre | § 116 SGB X |
| Strafverfolgungsverjährung (§ 229 StGB) | 5 Jahre | § 78 Abs. 3 Nr. 4 StGB |

## Typische Gegenargumente und Reaktion

| Einwand | Reaktion |
|---|---|
| Schaden liegt im allgemeinen Behandlungsrisiko | Sachverständiger klärt Abgrenzung; ex-ante-Maßstab entscheidend |
| Keine Kausalität nachweisbar | Bei grobem Fehler § 630h Abs. 5 Satz 1 BGB: Beweislastumkehr; bei Befunderhebungsfehler Abs. 5 Satz 2 |
| Patient nicht compliant | § 254 BGB Mitverschulden; reduziert Anspruch, hebt ihn nicht auf |
| Zwei Sachverständige widersprechen sich | Obergutachten; Qualifikation des SV hinterfragen; Verfahrensrecht § 411a ZPO |
| Verjährung eingetreten | § 199 Abs. 2 BGB 30-Jahres-Frist prüfen; bei verstecktem Fehler Kenntnisbeginn später |

## Streitwert und Kosten

- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
- Haushaltsführungsschaden: 8–14 EUR/h × ausgefallene Stunden; Kapitalisierung bei dauerhaft.
- Verdienstausfall Selbstständige: Betriebsgewinn × ausgefallene Zeit; Nachweis durch EStV.
- LG-Kosten bei 80.000 EUR Streitwert: ca. 3.000 EUR Gerichtskosten erste Instanz.
- RVG Anwalt: 1,3-fache VG + 1,2-fache TG; ca. 5.500 EUR netto bei 80.000 EUR.
- MDK-Gutachten: kostenfrei (GKV beauftragt); Privatgutachten 5.000–20.000 EUR.

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Grobes Verschulden offensichtlich | Direktklage; Beweislastumkehr § 630h Abs. 5 als Argument |
| Sachverhalt unklar | Schlichtung Ärztekammer (kostenfrei, Sachverständiger); MDK-Gutachten GKV |
| GKV-Patient | GKV informieren § 66 SGB V; MDK; Regressinteresse nutzen |
| Verjährung in 3 Monaten | Sofort Klage oder Güteantrag; Verjährungsverzicht verhandeln |
| Tod | Erbenklage; Schmerzensgeld vererbt (§ 253 BGB); Unterhaltsschaden Hinterbliebene |

## Übergabe

- Bei Ablehnung Klage; Skill `behandlungsfehler-anspruch-pruefen` für vollständigen Aufbau.
- Bei Tötung: Erbenklage und Beerdigungskosten § 844 Abs. 1 BGB, Unterhaltsschaden § 844 Abs. 2 BGB.
- Bei strafrechtlichem Aspekt parallel `fachanwalt-strafrecht-akteneinsicht-beantragen`.
- Anschluss bei Aufklärungsversäumnissen Skill `fachanwalt-medizinrecht-aufklaerungsfehler`.

## Quellen

- BGB §§ 195, 199, 253, 280, 630a–630h, 823, 843, 844
- ZPO §§ 286, 287
- SGB X § 116; SGB V § 66
- BGH 21.01.2025 — VI ZR 204/22: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=21.01.2025&Aktenzeichen=VI+ZR+204/22
- BGH 25.11.2025 — VI ZR 51/24: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=25.11.2025&Aktenzeichen=VI+ZR+51/24
- BGH 25.11.2025 — VI ZR 165/23: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=25.11.2025&Aktenzeichen=VI+ZR+165/23
- Literatur nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle; keine Kommentar-, Handbuch- oder Aufsatzblindzitate.
