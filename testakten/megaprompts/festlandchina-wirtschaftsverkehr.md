# Megaprompt: festlandchina-wirtschaftsverkehr

> *Achtung: Dies ist ein experimentelles Mega-Prompt-Markdown, das einen kompletten Klotzkette-Plugin in eine einzige Datei zusammenfuehrt. Keine Haftung, keine Gewaehr. Nur zum Ausprobieren der Skills auch ohne Claude Code; keine Rechtsberatung. Vor Verwendung im Mandat anwaltlich pruefen.*
>
> *Caution: This is an experimental Mega-Prompt Markdown that consolidates a full Klotzkette plugin into a single file. No warranty, no liability. For exploration with chat tools that do not run Claude Code only; not legal advice.*

**Verwendung:** Diesen gesamten Text in einen Chat ohne Claude-Code-Integration einfuegen (oder als Datei hochladen). Der Chat-Agent erhaelt damit die gebuendelten Skills dieses Plugins als Kontext. Eine Replikation des vollen Plugin-Verhaltens ist nicht garantiert — der Megaprompt ist eine Best-Effort-Kompression.


## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 101 Skills des Plugins `festlandchina-wirtschaftsverkehr`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Festlandchina Wirtschaftsverkehr: Kaltstart, Aktenlandkarte, Quellenprüfung, Fachmodul-Routing und erste verwertbare Aus…
2. **abschlussmemo-china-deal** — Abschluss-Memo China-Deal: Checkliste für finale Dokumentation vor Signing/Closing, AWV-Meldung, BAFA-Genehmigungen, FDI…
3. **anti-bribery-and-gifts** — Anti-Korruption und Geschenke im China-Geschaeft: FCPA (US) bei US-Nexus, UK Bribery Act, § 299 StGB (DE), chinesisches …
4. **arbitration-hk-siac-ciamac** — Schiedsgerichtsbarkeit für China-Streitigkeiten: CIETAC (China Int'l Economic and Trade Arbitration Commission), ICC mit…
5. **asset-protection-and-cash-repatriation** — Vermögensschutz und Cash-Repatriierung aus China: SAFE-Devisenkontrolle (State Administration of Foreign Exchange), Divi…
6. **automotive-supply-chain** — Automobilzuliefererkette China: Einzelteile und Module aus VR China unter EU-Anti-Dumping-Watch (E-Fahrzeuge), LkSG-Risi…
7. **awg-awv-investitionspruefung** — Investitionsprüfung nach AWG §§ 55 ff. und AWV §§ 55-62a: Sektorenüberblick, Erwerbsschwellen (10/25 Prozent Stimmrechte…
8. **battery-ev-solar-supply-chain** — Batterie-, EV- und Solarlieferketten aus China: EU-Batterie-VO 2023/1542 Sorgfaltspflichten, Carbon-Footprint-Deklaratio…
9. **board-paper-china-risk** — Board-Paper zu China-Risiken: Struktur und Inhalt eines belastbaren China-Risikoberichts für Aufsichtsrat/Vorstand, wese…
10. **capital-controls-and-payments** — Kapitalverkehrskontrollen und Zahlungsverkehr VR China: SAFE-Devisenverwaltungsregeln, grenzüberschreitende Zahlungen in…
11. **ce-kennzeichnung-und-produktsicherheit-china-import-compliance** — CE-Kennzeichnung und Produktsicherheit für China-Importe: EU-VO 2023/988 Produktsicherheits-VO Importeurspflichten, Konf…
12. **china-counterfeit-and-parallel-trade-fair** — Produktpiraterie und Grauimporte aus/über China: Grenzbeschlagnahme EU (EU-VO 608/2013), CNIPA-Enforcement, chinesische …
13. **china-csddd-readiness-whistleblower-channel** — EU CSDDD-Readiness für China-Lieferketten: EU-RL 2024/1760 Anforderungen, Anwendungsbereich und Fristen, Sorgfaltspflich…
14. **china-customs-tariff-origin-preferential-not** — Zolltarif und Ursprungsregeln für Waren aus VR China: KN-Nomenklatur, Ursprungsermittlung (wesentliche Be-/Verarbeitung)…
15. **china-de-risking-nicht-strategie** — Operative Umsetzung der EU/Bundesregierungs-De-risking-Strategie: Abgrenzung De-risking vs. Decoupling, Risikoklassifizi…

---

## Skill: `kaltstart-triage`

_Festlandchina Wirtschaftsverkehr: Kaltstart, Aktenlandkarte, Quellenprüfung, Fachmodul-Routing und erste verwertbare Ausgabe._

# Festlandchina Wirtschaftsverkehr - Allgemeiner Einstieg

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Festlandchina Wirtschaftsverkehr** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Startfragen

1. Was soll entstehen: Verständnis, Gutachten, Vertragsbaustein, Risiko-Dashboard, Unterrichtseinheit, Board-Memo oder Streitstrategie?
2. Welche Quelle liegt vor: Normtext, Vertrag, Handelsdokument, Archivstück, Behördenseite, Schiedsklausel, Register, E-Mail oder Datenraum?
3. Welche Rechtsordnung, Epoche, Institution, Branche oder Gegenpartei ist betroffen?
4. Gibt es Live-Check-Bedarf wegen Tagesrecht, Sanktionen, Exportkontrolle, Behördenpraxis oder aktueller Rechtsprechung?
5. Welche Ausgabe braucht die Nutzerin in welcher Tiefe?

## Kernanker

- Deutsche China-Strategie, EU De-risking, FDI Screening, Anti-Coercion Instrument
- BAFA/EU-Dual-Use, AWG/AWV, Sanktionen, US/EU-China-Exportkontrollschnittstellen
- Lieferkette: LkSG, CSDDD, Forced-Labour-Risiko, Audit, Customs, Trade Defence
- China-spezifisch: Daten/Cybersecurity, IP, JV/WFOE, Tech Transfer, National-Security- und Retaliation-Risiken

---

## Skill: `abschlussmemo-china-deal`

_Abschluss-Memo China-Deal: Checkliste für finale Dokumentation vor Signing/Closing, AWV-Meldung, BAFA-Genehmigungen, FDI-Screening-Clearance, IP-Registrierung, Datenschutz-Compliance (PIPL/DSGVO), LkSG-Risikoanalyse abgeschlossen, Notarielle Beglaubigungen CN, Post-Closing-Obligations. Output: Ab..._

# Abschluss-Memo China-Deal: Signing/Closing-Checkliste

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Abschluss-Memo China-Deal: Signing/Closing-Checkliste
- **Normen-/Quellenanker:** AWG/AWV, EU-Dual-Use, Sanktionen, Zoll/USt, Incoterms, Lieferkette/LkSG/CSDDD, IP-/Know-how-Schutz, Datenschutz/Cybersecurity und lokale China-Compliance live prüfen.
- **Entscheidende Weiche:** Ordne Lieferant, Werk, Datenfluss, Zahlungsweg, Exportgut, politisches Risiko, IP-Leck und Exit-Szenario getrennt.

Begleitet Mandanten und Berater im Wirtschaftsverkehr mit der Volksrepublik China.
Ausgangspunkt ist der konkrete Mandantenfall; Ergebnis ist stets ein verwertbares Arbeitsprodukt.

## Mandantenfall

**Fall 1:** Ein Unternehmen fragt nach konkreten Handlungspflichten im Bereich Abschlussmemo China Deal beim Chinageschaeft.

**Fall 2:** Eine Rechtsabteilung benötigt einen Prüfbericht zu Abschlussmemo China Deal für ein laufendes China-Projekt.

**Fall 3:** Ein Vorstand bittet um ein Board-Paper zu Abschlussmemo China Deal im Kontext der De-risking-Strategie.

## Erste Schritte

1. Sachverhalt und Ziel bestimmen: Was soll im Bereich Abschlussmemo China Deal geprüft/erstellt werden?
2. Relevante Normen identifizieren: AWG §§ 55 ff., AWV §§ 55-62a als Ausgangspunkt.
3. Unterlagen sichten: Verträge, Genehmigungen, Behördenschriftverkehr, interne Richtlinien.
4. Risikoeinschätzung Abschlussmemo China Deal: Kritikalitätsbewertung nach De-risking-Matrix.
5. Maßnahmen priorisieren: Kurzfristige Compliance-Lücken schließen, mittelfristige Strukturmaßnahmen planen.
6. Dokumentation erstellen: Prüfprotokoll, Risikoampel, Handlungsempfehlung.

## Rechtsrahmen

Verbindliches Recht und anerkannte Soft-Law-Quellen für diesen Skill:

- AWG §§ 55 ff.
- AWV §§ 55-62a
- LkSG §§ 3-10
- EU-VO 2019/452
- De-risking-Strategie Bundesregierung 2023: Politisch-strategischer Orientierungsrahmen.
- EU-VO 2019/452: FDI-Kooperationsmechanismus als Referenzrahmen.
- §§ 3-10 LkSG: Lieferkettensorgfaltspflichten als Querschnittspflicht.

Quellen sind getrennt nach deutschem Recht, EU-Recht und chinesischem Recht zu handhaben.
Bei Widersprüchen gilt: Verbindliches Recht geht Soft Law vor; aktueller Stand ist zu prüfen.

## Prüfraster

Schritt für Schritt abzuarbeiten, Ergebnisse dokumentieren:

- Ist Abschlussmemo China Deal-Relevanz für das konkrete Vorhaben gegeben?
- Welche Normen und Behörden sind zuständig?
- Bestehen Genehmigungs- oder Meldepflichten?
- Welche Fristen sind zu beachten?
- Gibt es De-risking- oder Diversifizierungsanforderungen?
- Ist die Dokumentation für Behörden und Investoren belastbar?

## Typische Fallstricke

Aus der Beratungspraxis: Diese Fehler sollten aktiv vermieden werden.

- Abschlussmemo China Deal-Relevanz unterschätzt: Regulierungsrahmen wird zu spät geprüft.
- Fristen versäumt: AWV/BAFA-Fristen sind streng und führen zu Bußgeldern.
- Dokumentationslücken: Behörden und Gerichte verlangen lückenlose Aufzeichnungen.

## Gegenposition

Folgende Gegenargumente sind im Mandantengespräch zu adressieren:

- Behörde (BMWK/BAFA): Behältst du den Ermessensspielraum der Behörde im Blick?
- Vertragspartner China: Welche Interessen und Risikobewertungen hat die chinesische Seite?
- Investoren/Aufsichtsrat: Sind ESG- und Menschenrechts-Anforderungen berücksichtigt?
- Compliance: Wurde auf Exportkontroll- und Sanktions-Risiken geprüft?

## Quellen

Nur frei prüfbare Quellen aus erlaubten Domains. Rechtsprechung nur mit Gericht und Datum.

- [AWG Volltext](https://www.gesetze-im-internet.de/awg_2013/)
- [AWV Volltext](https://www.gesetze-im-internet.de/awv_2013/)
- [BAFA Außenwirtschaft](https://www.bafa.de/DE/Aussenwirtschaft/aussenwirtschaft_node.html)
- [EU-VO 2019/452 EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R0452)
- [LkSG Volltext](https://www.gesetze-im-internet.de/lksg/)
- [BMWK China-Strategie](https://www.bmwk.de/Redaktion/DE/Artikel/Aussenwirtschaft/china-strategie.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 3-10 LkSG
- § 299 StGB
- § 2 LkSG
- § 1 AWG
- § 3 PatG
- § 8 LkSG
- § 4 LkSG
- § 17 AWG
- § 143 MarkenG
- § 3-5 LkSG
- § 5-6 LkSG
- § 5 LkSG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `anti-bribery-and-gifts`

_Anti-Korruption und Geschenke im China-Geschaeft: FCPA (US) bei US-Nexus, UK Bribery Act, § 299 StGB (DE), chinesisches Anti-Korruptionsrecht (Criminal Law Art. 391-396), Geschenke- und Bewirtungsrichtlinien, Red-Flag-Indikatoren, Whistleblower-Schutz, Behördliche Ermittlungen CN. Output: Anti-Br..._

# Anti-Korruption China: FCPA/§ 299 StGB/CN-Recht

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Anti-Korruption China: FCPA/§ 299 StGB/CN-Recht
- **Normen-/Quellenanker:** AWG/AWV, EU-Dual-Use, Sanktionen, Zoll/USt, Incoterms, Lieferkette/LkSG/CSDDD, IP-/Know-how-Schutz, Datenschutz/Cybersecurity und lokale China-Compliance live prüfen.
- **Entscheidende Weiche:** Ordne Lieferant, Werk, Datenfluss, Zahlungsweg, Exportgut, politisches Risiko, IP-Leck und Exit-Szenario getrennt.

Begleitet Mandanten und Berater im Wirtschaftsverkehr mit der Volksrepublik China.
Ausgangspunkt ist der konkrete Mandantenfall; Ergebnis ist stets ein verwertbares Arbeitsprodukt.

## Mandantenfall

**Fall 1:** Ein Unternehmen fragt nach konkreten Handlungspflichten im Bereich Anti Bribery And Gifts beim Chinageschaeft.

**Fall 2:** Eine Rechtsabteilung benötigt einen Prüfbericht zu Anti Bribery And Gifts für ein laufendes China-Projekt.

**Fall 3:** Ein Vorstand bittet um ein Board-Paper zu Anti Bribery And Gifts im Kontext der De-risking-Strategie.

## Erste Schritte

1. Sachverhalt und Ziel bestimmen: Was soll im Bereich Anti Bribery And Gifts geprüft/erstellt werden?
2. Relevante Normen identifizieren: AWG §§ 55 ff., AWV §§ 55-62a als Ausgangspunkt.
3. Unterlagen sichten: Verträge, Genehmigungen, Behördenschriftverkehr, interne Richtlinien.
4. Risikoeinschätzung Anti Bribery And: Kritikalitätsbewertung nach De-risking-Matrix.
5. Maßnahmen priorisieren: Kurzfristige Compliance-Lücken schließen, mittelfristige Strukturmaßnahmen planen.
6. Dokumentation erstellen: Prüfprotokoll, Risikoampel, Handlungsempfehlung.

## Rechtsrahmen

Verbindliches Recht und anerkannte Soft-Law-Quellen für diesen Skill:

- AWG §§ 55 ff.
- AWV §§ 55-62a
- LkSG §§ 3-10
- EU-VO 2019/452
- De-risking-Strategie Bundesregierung 2023: Politisch-strategischer Orientierungsrahmen.
- EU-VO 2019/452: FDI-Kooperationsmechanismus als Referenzrahmen.
- §§ 3-10 LkSG: Lieferkettensorgfaltspflichten als Querschnittspflicht.

Quellen sind getrennt nach deutschem Recht, EU-Recht und chinesischem Recht zu handhaben.
Bei Widersprüchen gilt: Verbindliches Recht geht Soft Law vor; aktueller Stand ist zu prüfen.

## Prüfraster

Schritt für Schritt abzuarbeiten, Ergebnisse dokumentieren:

- Ist Anti Bribery And-Relevanz für das konkrete Vorhaben gegeben?
- Welche Normen und Behörden sind zuständig?
- Bestehen Genehmigungs- oder Meldepflichten?
- Welche Fristen sind zu beachten?
- Gibt es De-risking- oder Diversifizierungsanforderungen?
- Ist die Dokumentation für Behörden und Investoren belastbar?

## Typische Fallstricke

Aus der Beratungspraxis: Diese Fehler sollten aktiv vermieden werden.

- Anti Bribery And-Relevanz unterschätzt: Regulierungsrahmen wird zu spät geprüft.
- Fristen versäumt: AWV/BAFA-Fristen sind streng und führen zu Bußgeldern.
- Dokumentationslücken: Behörden und Gerichte verlangen lückenlose Aufzeichnungen.

## Gegenposition

Folgende Gegenargumente sind im Mandantengespräch zu adressieren:

- Behörde (BMWK/BAFA): Behältst du den Ermessensspielraum der Behörde im Blick?
- Vertragspartner China: Welche Interessen und Risikobewertungen hat die chinesische Seite?
- Investoren/Aufsichtsrat: Sind ESG- und Menschenrechts-Anforderungen berücksichtigt?
- Compliance: Wurde auf Exportkontroll- und Sanktions-Risiken geprüft?

## Quellen

Nur frei prüfbare Quellen aus erlaubten Domains. Rechtsprechung nur mit Gericht und Datum.

- [AWG Volltext](https://www.gesetze-im-internet.de/awg_2013/)
- [AWV Volltext](https://www.gesetze-im-internet.de/awv_2013/)
- [BAFA Außenwirtschaft](https://www.bafa.de/DE/Aussenwirtschaft/aussenwirtschaft_node.html)
- [EU-VO 2019/452 EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R0452)
- [LkSG Volltext](https://www.gesetze-im-internet.de/lksg/)
- [BMWK China-Strategie](https://www.bmwk.de/Redaktion/DE/Artikel/Aussenwirtschaft/china-strategie.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 3-10 LkSG
- § 299 StGB
- § 2 LkSG
- § 1 AWG
- § 3 PatG
- § 8 LkSG
- § 4 LkSG
- § 17 AWG
- § 143 MarkenG
- § 3-5 LkSG
- § 5-6 LkSG
- § 5 LkSG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `arbitration-hk-siac-ciamac`

_Schiedsgerichtsbarkeit für China-Streitigkeiten: CIETAC (China Int'l Economic and Trade Arbitration Commission), ICC mit Sitz außerhalb CN, HKIAC Hongkong, SIAC Singapore, Vollstreckung New Yorker Übereinkommen in CN, Zwangsvollstreckung aus Schiedsspruch in der VR China, Anti-suit Injunctions. O..._

# Schiedsgerichtsbarkeit China: CIETAC/HKIAC/SIAC-Vergleich

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Schiedsgerichtsbarkeit China: CIETAC/HKIAC/SIAC-Vergleich
- **Normen-/Quellenanker:** AWG/AWV, EU-Dual-Use, Sanktionen, Zoll/USt, Incoterms, Lieferkette/LkSG/CSDDD, IP-/Know-how-Schutz, Datenschutz/Cybersecurity und lokale China-Compliance live prüfen.
- **Entscheidende Weiche:** Ordne Lieferant, Werk, Datenfluss, Zahlungsweg, Exportgut, politisches Risiko, IP-Leck und Exit-Szenario getrennt.

Begleitet Mandanten und Berater im Wirtschaftsverkehr mit der Volksrepublik China.
Ausgangspunkt ist der konkrete Mandantenfall; Ergebnis ist stets ein verwertbares Arbeitsprodukt.

## Mandantenfall

**Fall 1:** Ein Unternehmen fragt nach konkreten Handlungspflichten im Bereich Arbitration Hk Siac Ciamac beim Chinageschaeft.

**Fall 2:** Eine Rechtsabteilung benötigt einen Prüfbericht zu Arbitration Hk Siac Ciamac für ein laufendes China-Projekt.

**Fall 3:** Ein Vorstand bittet um ein Board-Paper zu Arbitration Hk Siac Ciamac im Kontext der De-risking-Strategie.

## Erste Schritte

1. Sachverhalt und Ziel bestimmen: Was soll im Bereich Arbitration Hk Siac Ciamac geprüft/erstellt werden?
2. Relevante Normen identifizieren: AWG §§ 55 ff., AWV §§ 55-62a als Ausgangspunkt.
3. Unterlagen sichten: Verträge, Genehmigungen, Behördenschriftverkehr, interne Richtlinien.
4. Risikoeinschätzung Arbitration Hk Siac: Kritikalitätsbewertung nach De-risking-Matrix.
5. Maßnahmen priorisieren: Kurzfristige Compliance-Lücken schließen, mittelfristige Strukturmaßnahmen planen.
6. Dokumentation erstellen: Prüfprotokoll, Risikoampel, Handlungsempfehlung.

## Rechtsrahmen

Verbindliches Recht und anerkannte Soft-Law-Quellen für diesen Skill:

- AWG §§ 55 ff.
- AWV §§ 55-62a
- LkSG §§ 3-10
- EU-VO 2019/452
- De-risking-Strategie Bundesregierung 2023: Politisch-strategischer Orientierungsrahmen.
- EU-VO 2019/452: FDI-Kooperationsmechanismus als Referenzrahmen.
- §§ 3-10 LkSG: Lieferkettensorgfaltspflichten als Querschnittspflicht.

Quellen sind getrennt nach deutschem Recht, EU-Recht und chinesischem Recht zu handhaben.
Bei Widersprüchen gilt: Verbindliches Recht geht Soft Law vor; aktueller Stand ist zu prüfen.

## Prüfraster

Schritt für Schritt abzuarbeiten, Ergebnisse dokumentieren:

- Ist Arbitration Hk Siac-Relevanz für das konkrete Vorhaben gegeben?
- Welche Normen und Behörden sind zuständig?
- Bestehen Genehmigungs- oder Meldepflichten?
- Welche Fristen sind zu beachten?
- Gibt es De-risking- oder Diversifizierungsanforderungen?
- Ist die Dokumentation für Behörden und Investoren belastbar?

## Typische Fallstricke

Aus der Beratungspraxis: Diese Fehler sollten aktiv vermieden werden.

- Arbitration Hk Siac-Relevanz unterschätzt: Regulierungsrahmen wird zu spät geprüft.
- Fristen versäumt: AWV/BAFA-Fristen sind streng und führen zu Bußgeldern.
- Dokumentationslücken: Behörden und Gerichte verlangen lückenlose Aufzeichnungen.

## Gegenposition

Folgende Gegenargumente sind im Mandantengespräch zu adressieren:

- Behörde (BMWK/BAFA): Behältst du den Ermessensspielraum der Behörde im Blick?
- Vertragspartner China: Welche Interessen und Risikobewertungen hat die chinesische Seite?
- Investoren/Aufsichtsrat: Sind ESG- und Menschenrechts-Anforderungen berücksichtigt?
- Compliance: Wurde auf Exportkontroll- und Sanktions-Risiken geprüft?

## Quellen

Nur frei prüfbare Quellen aus erlaubten Domains. Rechtsprechung nur mit Gericht und Datum.

- [AWG Volltext](https://www.gesetze-im-internet.de/awg_2013/)
- [AWV Volltext](https://www.gesetze-im-internet.de/awv_2013/)
- [BAFA Außenwirtschaft](https://www.bafa.de/DE/Aussenwirtschaft/aussenwirtschaft_node.html)
- [EU-VO 2019/452 EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R0452)
- [LkSG Volltext](https://www.gesetze-im-internet.de/lksg/)
- [BMWK China-Strategie](https://www.bmwk.de/Redaktion/DE/Artikel/Aussenwirtschaft/china-strategie.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 3-10 LkSG
- § 299 StGB
- § 2 LkSG
- § 1 AWG
- § 3 PatG
- § 8 LkSG
- § 4 LkSG
- § 17 AWG
- § 143 MarkenG
- § 3-5 LkSG
- § 5-6 LkSG
- § 5 LkSG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `asset-protection-and-cash-repatriation`

_Vermögensschutz und Cash-Repatriierung aus China: SAFE-Devisenkontrolle (State Administration of Foreign Exchange), Dividendenausschüttung aus WFOE, Verrechnungspreise als Repatriierungsinstrument, Cash-Pooling CN-DE, Kapitalrückführung bei Liquidation, Steuern auf Repatriierung (Quellensteuer 10..._

# Vermögensschutz und Cash-Repatriierung China: SAFE und Steuern

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Vermögensschutz und Cash-Repatriierung China: SAFE und Steuern
- **Normen-/Quellenanker:** AWG/AWV, EU-Dual-Use, Sanktionen, Zoll/USt, Incoterms, Lieferkette/LkSG/CSDDD, IP-/Know-how-Schutz, Datenschutz/Cybersecurity und lokale China-Compliance live prüfen.
- **Entscheidende Weiche:** Ordne Lieferant, Werk, Datenfluss, Zahlungsweg, Exportgut, politisches Risiko, IP-Leck und Exit-Szenario getrennt.

Begleitet Mandanten und Berater im Wirtschaftsverkehr mit der Volksrepublik China.
Ausgangspunkt ist der konkrete Mandantenfall; Ergebnis ist stets ein verwertbares Arbeitsprodukt.

## Mandantenfall

**Fall 1:** Ein Unternehmen fragt nach konkreten Handlungspflichten im Bereich Asset Protection And Cash Repatriation beim Chinageschaeft.

**Fall 2:** Eine Rechtsabteilung benötigt einen Prüfbericht zu Asset Protection And Cash Repatriation für ein laufendes China-Projekt.

**Fall 3:** Ein Vorstand bittet um ein Board-Paper zu Asset Protection And Cash Repatriation im Kontext der De-risking-Strategie.

## Erste Schritte

1. Sachverhalt und Ziel bestimmen: Was soll im Bereich Asset Protection And Cash Repatriation geprüft/erstellt werden?
2. Relevante Normen identifizieren: AWG §§ 55 ff., AWV §§ 55-62a als Ausgangspunkt.
3. Unterlagen sichten: Verträge, Genehmigungen, Behördenschriftverkehr, interne Richtlinien.
4. Risikoeinschätzung Asset Protection And: Kritikalitätsbewertung nach De-risking-Matrix.
5. Maßnahmen priorisieren: Kurzfristige Compliance-Lücken schließen, mittelfristige Strukturmaßnahmen planen.
6. Dokumentation erstellen: Prüfprotokoll, Risikoampel, Handlungsempfehlung.

## Rechtsrahmen

Verbindliches Recht und anerkannte Soft-Law-Quellen für diesen Skill:

- AWG §§ 55 ff.
- AWV §§ 55-62a
- LkSG §§ 3-10
- EU-VO 2019/452
- De-risking-Strategie Bundesregierung 2023: Politisch-strategischer Orientierungsrahmen.
- EU-VO 2019/452: FDI-Kooperationsmechanismus als Referenzrahmen.
- §§ 3-10 LkSG: Lieferkettensorgfaltspflichten als Querschnittspflicht.

Quellen sind getrennt nach deutschem Recht, EU-Recht und chinesischem Recht zu handhaben.
Bei Widersprüchen gilt: Verbindliches Recht geht Soft Law vor; aktueller Stand ist zu prüfen.

## Prüfraster

Schritt für Schritt abzuarbeiten, Ergebnisse dokumentieren:

- Ist Asset Protection And-Relevanz für das konkrete Vorhaben gegeben?
- Welche Normen und Behörden sind zuständig?
- Bestehen Genehmigungs- oder Meldepflichten?
- Welche Fristen sind zu beachten?
- Gibt es De-risking- oder Diversifizierungsanforderungen?
- Ist die Dokumentation für Behörden und Investoren belastbar?

## Typische Fallstricke

Aus der Beratungspraxis: Diese Fehler sollten aktiv vermieden werden.

- Asset Protection And-Relevanz unterschätzt: Regulierungsrahmen wird zu spät geprüft.
- Fristen versäumt: AWV/BAFA-Fristen sind streng und führen zu Bußgeldern.
- Dokumentationslücken: Behörden und Gerichte verlangen lückenlose Aufzeichnungen.

## Gegenposition

Folgende Gegenargumente sind im Mandantengespräch zu adressieren:

- Behörde (BMWK/BAFA): Behältst du den Ermessensspielraum der Behörde im Blick?
- Vertragspartner China: Welche Interessen und Risikobewertungen hat die chinesische Seite?
- Investoren/Aufsichtsrat: Sind ESG- und Menschenrechts-Anforderungen berücksichtigt?
- Compliance: Wurde auf Exportkontroll- und Sanktions-Risiken geprüft?

## Quellen

Nur frei prüfbare Quellen aus erlaubten Domains. Rechtsprechung nur mit Gericht und Datum.

- [AWG Volltext](https://www.gesetze-im-internet.de/awg_2013/)
- [AWV Volltext](https://www.gesetze-im-internet.de/awv_2013/)
- [BAFA Außenwirtschaft](https://www.bafa.de/DE/Aussenwirtschaft/aussenwirtschaft_node.html)
- [EU-VO 2019/452 EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R0452)
- [LkSG Volltext](https://www.gesetze-im-internet.de/lksg/)
- [BMWK China-Strategie](https://www.bmwk.de/Redaktion/DE/Artikel/Aussenwirtschaft/china-strategie.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 3-10 LkSG
- § 299 StGB
- § 2 LkSG
- § 1 AWG
- § 3 PatG
- § 8 LkSG
- § 4 LkSG
- § 17 AWG
- § 143 MarkenG
- § 3-5 LkSG
- § 5-6 LkSG
- § 5 LkSG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `automotive-supply-chain`

_Automobilzuliefererkette China: Einzelteile und Module aus VR China unter EU-Anti-Dumping-Watch (E-Fahrzeuge), LkSG-Risikoanalyse Tier-1 bis Tier-n, XUAR-Bezüge (Aluminium, Baumwolle, Polysilizium), Dual-Use-Prüfung Elektronik-ECU, EU-Batterie-VO 2023/1542 Supply Chain Due Diligence. Output: Auto..._

# Automotive-Lieferkette China: Anti-Dumping/LkSG/Batterie-VO

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Automotive-Lieferkette China: Anti-Dumping/LkSG/Batterie-VO
- **Normen-/Quellenanker:** AWG/AWV, EU-Dual-Use, Sanktionen, Zoll/USt, Incoterms, Lieferkette/LkSG/CSDDD, IP-/Know-how-Schutz, Datenschutz/Cybersecurity und lokale China-Compliance live prüfen.
- **Entscheidende Weiche:** Ordne Lieferant, Werk, Datenfluss, Zahlungsweg, Exportgut, politisches Risiko, IP-Leck und Exit-Szenario getrennt.

Begleitet Mandanten und Berater im Wirtschaftsverkehr mit der Volksrepublik China.
Ausgangspunkt ist der konkrete Mandantenfall; Ergebnis ist stets ein verwertbares Arbeitsprodukt.

## Mandantenfall

**Fall 1:** Ein Unternehmen fragt nach konkreten Handlungspflichten im Bereich Automotive Supply Chain beim Chinageschaeft.

**Fall 2:** Eine Rechtsabteilung benötigt einen Prüfbericht zu Automotive Supply Chain für ein laufendes China-Projekt.

**Fall 3:** Ein Vorstand bittet um ein Board-Paper zu Automotive Supply Chain im Kontext der De-risking-Strategie.

## Erste Schritte

1. Sachverhalt und Ziel bestimmen: Was soll im Bereich Automotive Supply Chain geprüft/erstellt werden?
2. Relevante Normen identifizieren: AWG §§ 55 ff., AWV §§ 55-62a als Ausgangspunkt.
3. Unterlagen sichten: Verträge, Genehmigungen, Behördenschriftverkehr, interne Richtlinien.
4. Risikoeinschätzung Automotive Supply Chain: Kritikalitätsbewertung nach De-risking-Matrix.
5. Maßnahmen priorisieren: Kurzfristige Compliance-Lücken schließen, mittelfristige Strukturmaßnahmen planen.
6. Dokumentation erstellen: Prüfprotokoll, Risikoampel, Handlungsempfehlung.

## Rechtsrahmen

Verbindliches Recht und anerkannte Soft-Law-Quellen für diesen Skill:

- AWG §§ 55 ff.
- AWV §§ 55-62a
- LkSG §§ 3-10
- EU-VO 2019/452
- De-risking-Strategie Bundesregierung 2023: Politisch-strategischer Orientierungsrahmen.
- EU-VO 2019/452: FDI-Kooperationsmechanismus als Referenzrahmen.
- §§ 3-10 LkSG: Lieferkettensorgfaltspflichten als Querschnittspflicht.

Quellen sind getrennt nach deutschem Recht, EU-Recht und chinesischem Recht zu handhaben.
Bei Widersprüchen gilt: Verbindliches Recht geht Soft Law vor; aktueller Stand ist zu prüfen.

## Prüfraster

Schritt für Schritt abzuarbeiten, Ergebnisse dokumentieren:

- Ist Automotive Supply Chain-Relevanz für das konkrete Vorhaben gegeben?
- Welche Normen und Behörden sind zuständig?
- Bestehen Genehmigungs- oder Meldepflichten?
- Welche Fristen sind zu beachten?
- Gibt es De-risking- oder Diversifizierungsanforderungen?
- Ist die Dokumentation für Behörden und Investoren belastbar?

## Typische Fallstricke

Aus der Beratungspraxis: Diese Fehler sollten aktiv vermieden werden.

- Automotive Supply Chain-Relevanz unterschätzt: Regulierungsrahmen wird zu spät geprüft.
- Fristen versäumt: AWV/BAFA-Fristen sind streng und führen zu Bußgeldern.
- Dokumentationslücken: Behörden und Gerichte verlangen lückenlose Aufzeichnungen.

## Gegenposition

Folgende Gegenargumente sind im Mandantengespräch zu adressieren:

- Behörde (BMWK/BAFA): Behältst du den Ermessensspielraum der Behörde im Blick?
- Vertragspartner China: Welche Interessen und Risikobewertungen hat die chinesische Seite?
- Investoren/Aufsichtsrat: Sind ESG- und Menschenrechts-Anforderungen berücksichtigt?
- Compliance: Wurde auf Exportkontroll- und Sanktions-Risiken geprüft?

## Quellen

Nur frei prüfbare Quellen aus erlaubten Domains. Rechtsprechung nur mit Gericht und Datum.

- [AWG Volltext](https://www.gesetze-im-internet.de/awg_2013/)
- [AWV Volltext](https://www.gesetze-im-internet.de/awv_2013/)
- [BAFA Außenwirtschaft](https://www.bafa.de/DE/Aussenwirtschaft/aussenwirtschaft_node.html)
- [EU-VO 2019/452 EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R0452)
- [LkSG Volltext](https://www.gesetze-im-internet.de/lksg/)
- [BMWK China-Strategie](https://www.bmwk.de/Redaktion/DE/Artikel/Aussenwirtschaft/china-strategie.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 3-10 LkSG
- § 299 StGB
- § 2 LkSG
- § 1 AWG
- § 3 PatG
- § 8 LkSG
- § 4 LkSG
- § 17 AWG
- § 143 MarkenG
- § 3-5 LkSG
- § 5-6 LkSG
- § 5 LkSG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `awg-awv-investitionspruefung`

_Investitionsprüfung nach AWG §§ 55 ff. und AWV §§ 55-62a: Sektorenüberblick, Erwerbsschwellen (10/25 Prozent Stimmrechte), Anmeldepflicht, Prüffristen, Untersagung, Auflagen, Kooperationspflichten mit EU-Partnern nach EU-VO 2019/452. Fallgruppen KRITIS/Technologie/Medien. Output: AWV-Prüfschema u..._

# AWG/AWV-Investitionsprüfung: Verfahren und Fallgruppen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: AWG/AWV-Investitionsprüfung: Verfahren und Fallgruppen
- **Normen-/Quellenanker:** AWG/AWV, EU-Dual-Use, Sanktionen, Zoll/USt, Incoterms, Lieferkette/LkSG/CSDDD, IP-/Know-how-Schutz, Datenschutz/Cybersecurity und lokale China-Compliance live prüfen.
- **Entscheidende Weiche:** Ordne Lieferant, Werk, Datenfluss, Zahlungsweg, Exportgut, politisches Risiko, IP-Leck und Exit-Szenario getrennt.

Begleitet Mandanten und Berater im Wirtschaftsverkehr mit der Volksrepublik China.
Ausgangspunkt ist der konkrete Mandantenfall; Ergebnis ist stets ein verwertbares Arbeitsprodukt.

## Mandantenfall

**Fall 1:** Ein Unternehmen fragt nach konkreten Handlungspflichten im Bereich Awg Awv Investitionspruefung beim Chinageschaeft.

**Fall 2:** Eine Rechtsabteilung benötigt einen Prüfbericht zu Awg Awv Investitionspruefung für ein laufendes China-Projekt.

**Fall 3:** Ein Vorstand bittet um ein Board-Paper zu Awg Awv Investitionspruefung im Kontext der De-risking-Strategie.

## Erste Schritte

1. Sachverhalt und Ziel bestimmen: Was soll im Bereich Awg Awv Investitionspruefung geprüft/erstellt werden?
2. Relevante Normen identifizieren: AWG §§ 55 ff., AWV §§ 55-62a als Ausgangspunkt.
3. Unterlagen sichten: Verträge, Genehmigungen, Behördenschriftverkehr, interne Richtlinien.
4. Risikoeinschätzung Außenwirtschaftsrecht: Kritikalitätsbewertung nach De-risking-Matrix.
5. Maßnahmen priorisieren: Kurzfristige Compliance-Lücken schließen, mittelfristige Strukturmaßnahmen planen.
6. Dokumentation erstellen: Prüfprotokoll, Risikoampel, Handlungsempfehlung.

## Rechtsrahmen

Verbindliches Recht und anerkannte Soft-Law-Quellen für diesen Skill:

- AWG §§ 55 ff.
- AWV §§ 55-62a
- EU-VO 2019/452
- BMWK-Bescheide Investitionsprüfung
- De-risking-Strategie Bundesregierung 2023: Politisch-strategischer Orientierungsrahmen.
- EU-VO 2019/452: FDI-Kooperationsmechanismus als Referenzrahmen.
- §§ 3-10 LkSG: Lieferkettensorgfaltspflichten als Querschnittspflicht.

Quellen sind getrennt nach deutschem Recht, EU-Recht und chinesischem Recht zu handhaben.
Bei Widersprüchen gilt: Verbindliches Recht geht Soft Law vor; aktueller Stand ist zu prüfen.

## Prüfraster

Schritt für Schritt abzuarbeiten, Ergebnisse dokumentieren:

- Ist Außenwirtschaftsrecht-Relevanz für das konkrete Vorhaben gegeben?
- Welche Normen und Behörden sind zuständig?
- Bestehen Genehmigungs- oder Meldepflichten?
- Welche Fristen sind zu beachten?
- Gibt es De-risking- oder Diversifizierungsanforderungen?
- Ist die Dokumentation für Behörden und Investoren belastbar?

## Typische Fallstricke

Aus der Beratungspraxis: Diese Fehler sollten aktiv vermieden werden.

- Außenwirtschaftsrecht-Relevanz unterschätzt: Regulierungsrahmen wird zu spät geprüft.
- Fristen versäumt: AWV/BAFA-Fristen sind streng und führen zu Bußgeldern.
- Dokumentationslücken: Behörden und Gerichte verlangen lückenlose Aufzeichnungen.

## Gegenposition

Folgende Gegenargumente sind im Mandantengespräch zu adressieren:

- Behörde (BMWK/BAFA): Behältst du den Ermessensspielraum der Behörde im Blick?
- Vertragspartner China: Welche Interessen und Risikobewertungen hat die chinesische Seite?
- Investoren/Aufsichtsrat: Sind ESG- und Menschenrechts-Anforderungen berücksichtigt?
- Compliance: Wurde auf Exportkontroll- und Sanktions-Risiken geprüft?

## Quellen

Nur frei prüfbare Quellen aus erlaubten Domains. Rechtsprechung nur mit Gericht und Datum.

- [AWG Volltext](https://www.gesetze-im-internet.de/awg_2013/)
- [AWV Volltext](https://www.gesetze-im-internet.de/awv_2013/)
- [BAFA Außenwirtschaft](https://www.bafa.de/DE/Aussenwirtschaft/aussenwirtschaft_node.html)
- [EU-VO 2019/452 EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R0452)
- [LkSG Volltext](https://www.gesetze-im-internet.de/lksg/)
- [BMWK China-Strategie](https://www.bmwk.de/Redaktion/DE/Artikel/Aussenwirtschaft/china-strategie.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 3-10 LkSG
- § 299 StGB
- § 2 LkSG
- § 1 AWG
- § 3 PatG
- § 8 LkSG
- § 4 LkSG
- § 17 AWG
- § 143 MarkenG
- § 3-5 LkSG
- § 5-6 LkSG
- § 5 LkSG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `battery-ev-solar-supply-chain`

_Batterie-, EV- und Solarlieferketten aus China: EU-Batterie-VO 2023/1542 Sorgfaltspflichten, Carbon-Footprint-Deklaration, Recycling-Quoten, Solar-Anti-Dumping-Maßnahmen EU, XUAR-Bezug Polysilizium, Critical Raw Materials Act Lithium/Kobalt, LkSG-Risikoanalyse Bergbau. Output: Supply-Chain-Compli..._

# Batterie/EV/Solar-Lieferkette China: Regulierung und Compliance

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Batterie/EV/Solar-Lieferkette China: Regulierung und Compliance
- **Normen-/Quellenanker:** AWG/AWV, EU-Dual-Use, Sanktionen, Zoll/USt, Incoterms, Lieferkette/LkSG/CSDDD, IP-/Know-how-Schutz, Datenschutz/Cybersecurity und lokale China-Compliance live prüfen.
- **Entscheidende Weiche:** Ordne Lieferant, Werk, Datenfluss, Zahlungsweg, Exportgut, politisches Risiko, IP-Leck und Exit-Szenario getrennt.

Begleitet Mandanten und Berater im Wirtschaftsverkehr mit der Volksrepublik China.
Ausgangspunkt ist der konkrete Mandantenfall; Ergebnis ist stets ein verwertbares Arbeitsprodukt.

## Mandantenfall

**Fall 1:** Ein Unternehmen fragt nach konkreten Handlungspflichten im Bereich Battery Ev Solar Supply Chain beim Chinageschaeft.

**Fall 2:** Eine Rechtsabteilung benötigt einen Prüfbericht zu Battery Ev Solar Supply Chain für ein laufendes China-Projekt.

**Fall 3:** Ein Vorstand bittet um ein Board-Paper zu Battery Ev Solar Supply Chain im Kontext der De-risking-Strategie.

## Erste Schritte

1. Sachverhalt und Ziel bestimmen: Was soll im Bereich Battery Ev Solar Supply Chain geprüft/erstellt werden?
2. Relevante Normen identifizieren: AWG §§ 55 ff., AWV §§ 55-62a als Ausgangspunkt.
3. Unterlagen sichten: Verträge, Genehmigungen, Behördenschriftverkehr, interne Richtlinien.
4. Risikoeinschätzung Battery Ev Solar: Kritikalitätsbewertung nach De-risking-Matrix.
5. Maßnahmen priorisieren: Kurzfristige Compliance-Lücken schließen, mittelfristige Strukturmaßnahmen planen.
6. Dokumentation erstellen: Prüfprotokoll, Risikoampel, Handlungsempfehlung.

## Rechtsrahmen

Verbindliches Recht und anerkannte Soft-Law-Quellen für diesen Skill:

- AWG §§ 55 ff.
- AWV §§ 55-62a
- LkSG §§ 3-10
- EU-VO 2019/452
- De-risking-Strategie Bundesregierung 2023: Politisch-strategischer Orientierungsrahmen.
- EU-VO 2019/452: FDI-Kooperationsmechanismus als Referenzrahmen.
- §§ 3-10 LkSG: Lieferkettensorgfaltspflichten als Querschnittspflicht.

Quellen sind getrennt nach deutschem Recht, EU-Recht und chinesischem Recht zu handhaben.
Bei Widersprüchen gilt: Verbindliches Recht geht Soft Law vor; aktueller Stand ist zu prüfen.

## Prüfraster

Schritt für Schritt abzuarbeiten, Ergebnisse dokumentieren:

- Ist Battery Ev Solar-Relevanz für das konkrete Vorhaben gegeben?
- Welche Normen und Behörden sind zuständig?
- Bestehen Genehmigungs- oder Meldepflichten?
- Welche Fristen sind zu beachten?
- Gibt es De-risking- oder Diversifizierungsanforderungen?
- Ist die Dokumentation für Behörden und Investoren belastbar?

## Typische Fallstricke

Aus der Beratungspraxis: Diese Fehler sollten aktiv vermieden werden.

- Battery Ev Solar-Relevanz unterschätzt: Regulierungsrahmen wird zu spät geprüft.
- Fristen versäumt: AWV/BAFA-Fristen sind streng und führen zu Bußgeldern.
- Dokumentationslücken: Behörden und Gerichte verlangen lückenlose Aufzeichnungen.

## Gegenposition

Folgende Gegenargumente sind im Mandantengespräch zu adressieren:

- Behörde (BMWK/BAFA): Behältst du den Ermessensspielraum der Behörde im Blick?
- Vertragspartner China: Welche Interessen und Risikobewertungen hat die chinesische Seite?
- Investoren/Aufsichtsrat: Sind ESG- und Menschenrechts-Anforderungen berücksichtigt?
- Compliance: Wurde auf Exportkontroll- und Sanktions-Risiken geprüft?

## Quellen

Nur frei prüfbare Quellen aus erlaubten Domains. Rechtsprechung nur mit Gericht und Datum.

- [AWG Volltext](https://www.gesetze-im-internet.de/awg_2013/)
- [AWV Volltext](https://www.gesetze-im-internet.de/awv_2013/)
- [BAFA Außenwirtschaft](https://www.bafa.de/DE/Aussenwirtschaft/aussenwirtschaft_node.html)
- [EU-VO 2019/452 EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R0452)
- [LkSG Volltext](https://www.gesetze-im-internet.de/lksg/)
- [BMWK China-Strategie](https://www.bmwk.de/Redaktion/DE/Artikel/Aussenwirtschaft/china-strategie.html)

---

## Skill: `board-paper-china-risk`

_Board-Paper zu China-Risiken: Struktur und Inhalt eines belastbaren China-Risikoberichts für Aufsichtsrat/Vorstand, wesentliche Risikokategorien (Geopolitik/Regulation/Lieferkette/IP/Cyber), De-risking-Fortschritt, AWV-Meldestatus, LkSG-Compliance, ESG-Aspekte. Anforderungen §§ 76/93 AktG Sorgfal..._

# Board-Paper China-Risiken: Struktur und Inhalte für Aufsichtsrat

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Board-Paper China-Risiken: Struktur und Inhalte für Aufsichtsrat
- **Normen-/Quellenanker:** AWG/AWV, EU-Dual-Use, Sanktionen, Zoll/USt, Incoterms, Lieferkette/LkSG/CSDDD, IP-/Know-how-Schutz, Datenschutz/Cybersecurity und lokale China-Compliance live prüfen.
- **Entscheidende Weiche:** Ordne Lieferant, Werk, Datenfluss, Zahlungsweg, Exportgut, politisches Risiko, IP-Leck und Exit-Szenario getrennt.

Begleitet Mandanten und Berater im Wirtschaftsverkehr mit der Volksrepublik China.
Ausgangspunkt ist der konkrete Mandantenfall; Ergebnis ist stets ein verwertbares Arbeitsprodukt.

## Mandantenfall

**Fall 1:** Ein Unternehmen fragt nach konkreten Handlungspflichten im Bereich Board Paper China Risk beim Chinageschaeft.

**Fall 2:** Eine Rechtsabteilung benötigt einen Prüfbericht zu Board Paper China Risk für ein laufendes China-Projekt.

**Fall 3:** Ein Vorstand bittet um ein Board-Paper zu Board Paper China Risk im Kontext der De-risking-Strategie.

## Erste Schritte

1. Sachverhalt und Ziel bestimmen: Was soll im Bereich Board Paper China Risk geprüft/erstellt werden?
2. Relevante Normen identifizieren: AWG §§ 55 ff., AWV §§ 55-62a als Ausgangspunkt.
3. Unterlagen sichten: Verträge, Genehmigungen, Behördenschriftverkehr, interne Richtlinien.
4. Risikoeinschätzung Board Paper China: Kritikalitätsbewertung nach De-risking-Matrix.
5. Maßnahmen priorisieren: Kurzfristige Compliance-Lücken schließen, mittelfristige Strukturmaßnahmen planen.
6. Dokumentation erstellen: Prüfprotokoll, Risikoampel, Handlungsempfehlung.

## Rechtsrahmen

Verbindliches Recht und anerkannte Soft-Law-Quellen für diesen Skill:

- AWG §§ 55 ff.
- AWV §§ 55-62a
- LkSG §§ 3-10
- EU-VO 2019/452
- De-risking-Strategie Bundesregierung 2023: Politisch-strategischer Orientierungsrahmen.
- EU-VO 2019/452: FDI-Kooperationsmechanismus als Referenzrahmen.
- §§ 3-10 LkSG: Lieferkettensorgfaltspflichten als Querschnittspflicht.

Quellen sind getrennt nach deutschem Recht, EU-Recht und chinesischem Recht zu handhaben.
Bei Widersprüchen gilt: Verbindliches Recht geht Soft Law vor; aktueller Stand ist zu prüfen.

## Prüfraster

Schritt für Schritt abzuarbeiten, Ergebnisse dokumentieren:

- Ist Board Paper China-Relevanz für das konkrete Vorhaben gegeben?
- Welche Normen und Behörden sind zuständig?
- Bestehen Genehmigungs- oder Meldepflichten?
- Welche Fristen sind zu beachten?
- Gibt es De-risking- oder Diversifizierungsanforderungen?
- Ist die Dokumentation für Behörden und Investoren belastbar?

## Typische Fallstricke

Aus der Beratungspraxis: Diese Fehler sollten aktiv vermieden werden.

- Board Paper China-Relevanz unterschätzt: Regulierungsrahmen wird zu spät geprüft.
- Fristen versäumt: AWV/BAFA-Fristen sind streng und führen zu Bußgeldern.
- Dokumentationslücken: Behörden und Gerichte verlangen lückenlose Aufzeichnungen.

## Gegenposition

Folgende Gegenargumente sind im Mandantengespräch zu adressieren:

- Behörde (BMWK/BAFA): Behältst du den Ermessensspielraum der Behörde im Blick?
- Vertragspartner China: Welche Interessen und Risikobewertungen hat die chinesische Seite?
- Investoren/Aufsichtsrat: Sind ESG- und Menschenrechts-Anforderungen berücksichtigt?
- Compliance: Wurde auf Exportkontroll- und Sanktions-Risiken geprüft?

## Quellen

Nur frei prüfbare Quellen aus erlaubten Domains. Rechtsprechung nur mit Gericht und Datum.

- [AWG Volltext](https://www.gesetze-im-internet.de/awg_2013/)
- [AWV Volltext](https://www.gesetze-im-internet.de/awv_2013/)
- [BAFA Außenwirtschaft](https://www.bafa.de/DE/Aussenwirtschaft/aussenwirtschaft_node.html)
- [EU-VO 2019/452 EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R0452)
- [LkSG Volltext](https://www.gesetze-im-internet.de/lksg/)
- [BMWK China-Strategie](https://www.bmwk.de/Redaktion/DE/Artikel/Aussenwirtschaft/china-strategie.html)

---

## Skill: `capital-controls-and-payments`

_Kapitalverkehrskontrollen und Zahlungsverkehr VR China: SAFE-Devisenverwaltungsregeln, grenzüberschreitende Zahlungen in CNY, CIPS-System vs. SWIFT, Trade-Financing, L/C bei China-Handel, Zahlungsverzug-Risiken, Bankkorrespondenz-Probleme bei US-Sanktionen. Output: Zahlungsverkehrs-Compliance-Übe..._

# Kapitalverkehrskontrollen China: SAFE/CIPS und Zahlungsrisiken

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Kapitalverkehrskontrollen China: SAFE/CIPS und Zahlungsrisiken
- **Normen-/Quellenanker:** AWG/AWV, EU-Dual-Use, Sanktionen, Zoll/USt, Incoterms, Lieferkette/LkSG/CSDDD, IP-/Know-how-Schutz, Datenschutz/Cybersecurity und lokale China-Compliance live prüfen.
- **Entscheidende Weiche:** Ordne Lieferant, Werk, Datenfluss, Zahlungsweg, Exportgut, politisches Risiko, IP-Leck und Exit-Szenario getrennt.

Begleitet Mandanten und Berater im Wirtschaftsverkehr mit der Volksrepublik China.
Ausgangspunkt ist der konkrete Mandantenfall; Ergebnis ist stets ein verwertbares Arbeitsprodukt.

## Mandantenfall

**Fall 1:** Ein Unternehmen fragt nach konkreten Handlungspflichten im Bereich Capital Controls And Payments beim Chinageschaeft.

**Fall 2:** Eine Rechtsabteilung benötigt einen Prüfbericht zu Capital Controls And Payments für ein laufendes China-Projekt.

**Fall 3:** Ein Vorstand bittet um ein Board-Paper zu Capital Controls And Payments im Kontext der De-risking-Strategie.

## Erste Schritte

1. Sachverhalt und Ziel bestimmen: Was soll im Bereich Capital Controls And Payments geprüft/erstellt werden?
2. Relevante Normen identifizieren: AWG §§ 55 ff., AWV §§ 55-62a als Ausgangspunkt.
3. Unterlagen sichten: Verträge, Genehmigungen, Behördenschriftverkehr, interne Richtlinien.
4. Risikoeinschätzung Capital Controls And: Kritikalitätsbewertung nach De-risking-Matrix.
5. Maßnahmen priorisieren: Kurzfristige Compliance-Lücken schließen, mittelfristige Strukturmaßnahmen planen.
6. Dokumentation erstellen: Prüfprotokoll, Risikoampel, Handlungsempfehlung.

## Rechtsrahmen

Verbindliches Recht und anerkannte Soft-Law-Quellen für diesen Skill:

- AWG §§ 55 ff.
- AWV §§ 55-62a
- LkSG §§ 3-10
- EU-VO 2019/452
- De-risking-Strategie Bundesregierung 2023: Politisch-strategischer Orientierungsrahmen.
- EU-VO 2019/452: FDI-Kooperationsmechanismus als Referenzrahmen.
- §§ 3-10 LkSG: Lieferkettensorgfaltspflichten als Querschnittspflicht.

Quellen sind getrennt nach deutschem Recht, EU-Recht und chinesischem Recht zu handhaben.
Bei Widersprüchen gilt: Verbindliches Recht geht Soft Law vor; aktueller Stand ist zu prüfen.

## Prüfraster

Schritt für Schritt abzuarbeiten, Ergebnisse dokumentieren:

- Ist Capital Controls And-Relevanz für das konkrete Vorhaben gegeben?
- Welche Normen und Behörden sind zuständig?
- Bestehen Genehmigungs- oder Meldepflichten?
- Welche Fristen sind zu beachten?
- Gibt es De-risking- oder Diversifizierungsanforderungen?
- Ist die Dokumentation für Behörden und Investoren belastbar?

## Typische Fallstricke

Aus der Beratungspraxis: Diese Fehler sollten aktiv vermieden werden.

- Capital Controls And-Relevanz unterschätzt: Regulierungsrahmen wird zu spät geprüft.
- Fristen versäumt: AWV/BAFA-Fristen sind streng und führen zu Bußgeldern.
- Dokumentationslücken: Behörden und Gerichte verlangen lückenlose Aufzeichnungen.

## Gegenposition

Folgende Gegenargumente sind im Mandantengespräch zu adressieren:

- Behörde (BMWK/BAFA): Behältst du den Ermessensspielraum der Behörde im Blick?
- Vertragspartner China: Welche Interessen und Risikobewertungen hat die chinesische Seite?
- Investoren/Aufsichtsrat: Sind ESG- und Menschenrechts-Anforderungen berücksichtigt?
- Compliance: Wurde auf Exportkontroll- und Sanktions-Risiken geprüft?

## Quellen

Nur frei prüfbare Quellen aus erlaubten Domains. Rechtsprechung nur mit Gericht und Datum.

- [AWG Volltext](https://www.gesetze-im-internet.de/awg_2013/)
- [AWV Volltext](https://www.gesetze-im-internet.de/awv_2013/)
- [BAFA Außenwirtschaft](https://www.bafa.de/DE/Aussenwirtschaft/aussenwirtschaft_node.html)
- [EU-VO 2019/452 EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R0452)
- [LkSG Volltext](https://www.gesetze-im-internet.de/lksg/)
- [BMWK China-Strategie](https://www.bmwk.de/Redaktion/DE/Artikel/Aussenwirtschaft/china-strategie.html)

---

## Skill: `ce-kennzeichnung-und-produktsicherheit-china-import-compliance`

_CE-Kennzeichnung und Produktsicherheit für China-Importe: EU-VO 2023/988 Produktsicherheits-VO Importeurspflichten, Konformitätsbewertung, Technische Dokumentation, Marktüberwachung (EU-VO 2019/1020), Produkthaftung § 823 BGB und ProdHaftG, Rückrufmanagement. Output: CE-Compliance-Handbuch China-..._

# CE-Kennzeichnung und Produktsicherheit: China-Import-Compliance

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: CE-Kennzeichnung und Produktsicherheit: China-Import-Compliance
- **Normen-/Quellenanker:** AWG/AWV, EU-Dual-Use, Sanktionen, Zoll/USt, Incoterms, Lieferkette/LkSG/CSDDD, IP-/Know-how-Schutz, Datenschutz/Cybersecurity und lokale China-Compliance live prüfen.
- **Entscheidende Weiche:** Ordne Lieferant, Werk, Datenfluss, Zahlungsweg, Exportgut, politisches Risiko, IP-Leck und Exit-Szenario getrennt.

Begleitet Mandanten und Berater im Wirtschaftsverkehr mit der Volksrepublik China.
Ausgangspunkt ist der konkrete Mandantenfall; Ergebnis ist stets ein verwertbares Arbeitsprodukt.

## Mandantenfall

**Fall 1:** Ein Unternehmen fragt nach konkreten Handlungspflichten im Bereich Product Safety And Ce Import beim Chinageschaeft.

**Fall 2:** Eine Rechtsabteilung benötigt einen Prüfbericht zu Product Safety And Ce Import für ein laufendes China-Projekt.

**Fall 3:** Ein Vorstand bittet um ein Board-Paper zu Product Safety And Ce Import im Kontext der De-risking-Strategie.

## Erste Schritte

1. Sachverhalt und Ziel bestimmen: Was soll im Bereich Product Safety And Ce Import geprüft/erstellt werden?
2. Relevante Normen identifizieren: AWG §§ 55 ff., AWV §§ 55-62a als Ausgangspunkt.
3. Unterlagen sichten: Verträge, Genehmigungen, Behördenschriftverkehr, interne Richtlinien.
4. Risikoeinschätzung Product Safety And: Kritikalitätsbewertung nach De-risking-Matrix.
5. Maßnahmen priorisieren: Kurzfristige Compliance-Lücken schließen, mittelfristige Strukturmaßnahmen planen.
6. Dokumentation erstellen: Prüfprotokoll, Risikoampel, Handlungsempfehlung.

## Rechtsrahmen

Verbindliches Recht und anerkannte Soft-Law-Quellen für diesen Skill:

- AWG §§ 55 ff.
- AWV §§ 55-62a
- LkSG §§ 3-10
- EU-VO 2019/452
- De-risking-Strategie Bundesregierung 2023: Politisch-strategischer Orientierungsrahmen.
- EU-VO 2019/452: FDI-Kooperationsmechanismus als Referenzrahmen.
- §§ 3-10 LkSG: Lieferkettensorgfaltspflichten als Querschnittspflicht.

Quellen sind getrennt nach deutschem Recht, EU-Recht und chinesischem Recht zu handhaben.
Bei Widersprüchen gilt: Verbindliches Recht geht Soft Law vor; aktueller Stand ist zu prüfen.

## Prüfraster

Schritt für Schritt abzuarbeiten, Ergebnisse dokumentieren:

- Ist Product Safety And-Relevanz für das konkrete Vorhaben gegeben?
- Welche Normen und Behörden sind zuständig?
- Bestehen Genehmigungs- oder Meldepflichten?
- Welche Fristen sind zu beachten?
- Gibt es De-risking- oder Diversifizierungsanforderungen?
- Ist die Dokumentation für Behörden und Investoren belastbar?

## Typische Fallstricke

Aus der Beratungspraxis: Diese Fehler sollten aktiv vermieden werden.

- Product Safety And-Relevanz unterschätzt: Regulierungsrahmen wird zu spät geprüft.
- Fristen versäumt: AWV/BAFA-Fristen sind streng und führen zu Bußgeldern.
- Dokumentationslücken: Behörden und Gerichte verlangen lückenlose Aufzeichnungen.

## Gegenposition

Folgende Gegenargumente sind im Mandantengespräch zu adressieren:

- Behörde (BMWK/BAFA): Behältst du den Ermessensspielraum der Behörde im Blick?
- Vertragspartner China: Welche Interessen und Risikobewertungen hat die chinesische Seite?
- Investoren/Aufsichtsrat: Sind ESG- und Menschenrechts-Anforderungen berücksichtigt?
- Compliance: Wurde auf Exportkontroll- und Sanktions-Risiken geprüft?

## Quellen

Nur frei prüfbare Quellen aus erlaubten Domains. Rechtsprechung nur mit Gericht und Datum.

- [AWG Volltext](https://www.gesetze-im-internet.de/awg_2013/)
- [AWV Volltext](https://www.gesetze-im-internet.de/awv_2013/)
- [BAFA Außenwirtschaft](https://www.bafa.de/DE/Aussenwirtschaft/aussenwirtschaft_node.html)
- [EU-VO 2019/452 EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R0452)
- [LkSG Volltext](https://www.gesetze-im-internet.de/lksg/)
- [BMWK China-Strategie](https://www.bmwk.de/Redaktion/DE/Artikel/Aussenwirtschaft/china-strategie.html)

---

## Skill: `china-counterfeit-and-parallel-trade-fair`

_Produktpiraterie und Grauimporte aus/über China: Grenzbeschlagnahme EU (EU-VO 608/2013), CNIPA-Enforcement, chinesische Zollregistrierung IP-Rechte, Parallelimporte (Erschöpfung EU vs. CN), Abmahnverfahren DE, Zoll-Alarm-System COPIS, Strafverfolgung Produktpiraterie § 143 MarkenG. Output: Anti-P..._

# Produktpiraterie und Grauimporte China: Grenzbeschlagnahme/CNIPA

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Produktpiraterie und Grauimporte China: Grenzbeschlagnahme/CNIPA
- **Normen-/Quellenanker:** AWG/AWV, EU-Dual-Use, Sanktionen, Zoll/USt, Incoterms, Lieferkette/LkSG/CSDDD, IP-/Know-how-Schutz, Datenschutz/Cybersecurity und lokale China-Compliance live prüfen.
- **Entscheidende Weiche:** Ordne Lieferant, Werk, Datenfluss, Zahlungsweg, Exportgut, politisches Risiko, IP-Leck und Exit-Szenario getrennt.

Begleitet Mandanten und Berater im Wirtschaftsverkehr mit der Volksrepublik China.
Ausgangspunkt ist der konkrete Mandantenfall; Ergebnis ist stets ein verwertbares Arbeitsprodukt.

## Mandantenfall

**Fall 1:** Ein Unternehmen fragt nach konkreten Handlungspflichten im Bereich Counterfeit And Parallel Imports beim Chinageschaeft.

**Fall 2:** Eine Rechtsabteilung benötigt einen Prüfbericht zu Counterfeit And Parallel Imports für ein laufendes China-Projekt.

**Fall 3:** Ein Vorstand bittet um ein Board-Paper zu Counterfeit And Parallel Imports im Kontext der De-risking-Strategie.

## Erste Schritte

1. Sachverhalt und Ziel bestimmen: Was soll im Bereich Counterfeit And Parallel Imports geprüft/erstellt werden?
2. Relevante Normen identifizieren: AWG §§ 55 ff., AWV §§ 55-62a als Ausgangspunkt.
3. Unterlagen sichten: Verträge, Genehmigungen, Behördenschriftverkehr, interne Richtlinien.
4. Risikoeinschätzung Counterfeit And Parallel: Kritikalitätsbewertung nach De-risking-Matrix.
5. Maßnahmen priorisieren: Kurzfristige Compliance-Lücken schließen, mittelfristige Strukturmaßnahmen planen.
6. Dokumentation erstellen: Prüfprotokoll, Risikoampel, Handlungsempfehlung.

## Rechtsrahmen

Verbindliches Recht und anerkannte Soft-Law-Quellen für diesen Skill:

- AWG §§ 55 ff.
- AWV §§ 55-62a
- LkSG §§ 3-10
- EU-VO 2019/452
- De-risking-Strategie Bundesregierung 2023: Politisch-strategischer Orientierungsrahmen.
- EU-VO 2019/452: FDI-Kooperationsmechanismus als Referenzrahmen.
- §§ 3-10 LkSG: Lieferkettensorgfaltspflichten als Querschnittspflicht.

Quellen sind getrennt nach deutschem Recht, EU-Recht und chinesischem Recht zu handhaben.
Bei Widersprüchen gilt: Verbindliches Recht geht Soft Law vor; aktueller Stand ist zu prüfen.

## Prüfraster

Schritt für Schritt abzuarbeiten, Ergebnisse dokumentieren:

- Ist Counterfeit And Parallel-Relevanz für das konkrete Vorhaben gegeben?
- Welche Normen und Behörden sind zuständig?
- Bestehen Genehmigungs- oder Meldepflichten?
- Welche Fristen sind zu beachten?
- Gibt es De-risking- oder Diversifizierungsanforderungen?
- Ist die Dokumentation für Behörden und Investoren belastbar?

## Typische Fallstricke

Aus der Beratungspraxis: Diese Fehler sollten aktiv vermieden werden.

- Counterfeit And Parallel-Relevanz unterschätzt: Regulierungsrahmen wird zu spät geprüft.
- Fristen versäumt: AWV/BAFA-Fristen sind streng und führen zu Bußgeldern.
- Dokumentationslücken: Behörden und Gerichte verlangen lückenlose Aufzeichnungen.

## Gegenposition

Folgende Gegenargumente sind im Mandantengespräch zu adressieren:

- Behörde (BMWK/BAFA): Behältst du den Ermessensspielraum der Behörde im Blick?
- Vertragspartner China: Welche Interessen und Risikobewertungen hat die chinesische Seite?
- Investoren/Aufsichtsrat: Sind ESG- und Menschenrechts-Anforderungen berücksichtigt?
- Compliance: Wurde auf Exportkontroll- und Sanktions-Risiken geprüft?

## Quellen

Nur frei prüfbare Quellen aus erlaubten Domains. Rechtsprechung nur mit Gericht und Datum.

- [AWG Volltext](https://www.gesetze-im-internet.de/awg_2013/)
- [AWV Volltext](https://www.gesetze-im-internet.de/awv_2013/)
- [BAFA Außenwirtschaft](https://www.bafa.de/DE/Aussenwirtschaft/aussenwirtschaft_node.html)
- [EU-VO 2019/452 EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R0452)
- [LkSG Volltext](https://www.gesetze-im-internet.de/lksg/)
- [BMWK China-Strategie](https://www.bmwk.de/Redaktion/DE/Artikel/Aussenwirtschaft/china-strategie.html)

---

## Skill: `china-csddd-readiness-whistleblower-channel`

_EU CSDDD-Readiness für China-Lieferketten: EU-RL 2024/1760 Anforderungen, Anwendungsbereich und Fristen, Sorgfaltspflichten gegenüber eigenen Tätigkeiten und Geschaeftspartnern in CN, Umwelt- und Menschenrechtsindikatoren, Zivilrechtliche Haftung Art. 29 CSDDD, Verhältnis zu LkSG. Output: CSDDD-G..._

# EU CSDDD-Readiness China: Gap-Analyse und Umsetzung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: EU CSDDD-Readiness China: Gap-Analyse und Umsetzung
- **Normen-/Quellenanker:** AWG/AWV, EU-Dual-Use, Sanktionen, Zoll/USt, Incoterms, Lieferkette/LkSG/CSDDD, IP-/Know-how-Schutz, Datenschutz/Cybersecurity und lokale China-Compliance live prüfen.
- **Entscheidende Weiche:** Ordne Lieferant, Werk, Datenfluss, Zahlungsweg, Exportgut, politisches Risiko, IP-Leck und Exit-Szenario getrennt.

Begleitet Mandanten und Berater im Wirtschaftsverkehr mit der Volksrepublik China.
Ausgangspunkt ist der konkrete Mandantenfall; Ergebnis ist stets ein verwertbares Arbeitsprodukt.

## Mandantenfall

**Fall 1:** Ein Unternehmen fragt nach konkreten Handlungspflichten im Bereich Csddd Readiness beim Chinageschaeft.

**Fall 2:** Eine Rechtsabteilung benötigt einen Prüfbericht zu Csddd Readiness für ein laufendes China-Projekt.

**Fall 3:** Ein Vorstand bittet um ein Board-Paper zu Csddd Readiness im Kontext der De-risking-Strategie.

## Erste Schritte

1. Sachverhalt und Ziel bestimmen: Was soll im Bereich Csddd Readiness geprüft/erstellt werden?
2. Relevante Normen identifizieren: AWG §§ 55 ff., AWV §§ 55-62a als Ausgangspunkt.
3. Unterlagen sichten: Verträge, Genehmigungen, Behördenschriftverkehr, interne Richtlinien.
4. Risikoeinschätzung Csddd Readiness: Kritikalitätsbewertung nach De-risking-Matrix.
5. Maßnahmen priorisieren: Kurzfristige Compliance-Lücken schließen, mittelfristige Strukturmaßnahmen planen.
6. Dokumentation erstellen: Prüfprotokoll, Risikoampel, Handlungsempfehlung.

## Rechtsrahmen

Verbindliches Recht und anerkannte Soft-Law-Quellen für diesen Skill:

- AWG §§ 55 ff.
- AWV §§ 55-62a
- LkSG §§ 3-10
- EU-VO 2019/452
- De-risking-Strategie Bundesregierung 2023: Politisch-strategischer Orientierungsrahmen.
- EU-VO 2019/452: FDI-Kooperationsmechanismus als Referenzrahmen.
- §§ 3-10 LkSG: Lieferkettensorgfaltspflichten als Querschnittspflicht.

Quellen sind getrennt nach deutschem Recht, EU-Recht und chinesischem Recht zu handhaben.
Bei Widersprüchen gilt: Verbindliches Recht geht Soft Law vor; aktueller Stand ist zu prüfen.

## Prüfraster

Schritt für Schritt abzuarbeiten, Ergebnisse dokumentieren:

- Ist Csddd Readiness-Relevanz für das konkrete Vorhaben gegeben?
- Welche Normen und Behörden sind zuständig?
- Bestehen Genehmigungs- oder Meldepflichten?
- Welche Fristen sind zu beachten?
- Gibt es De-risking- oder Diversifizierungsanforderungen?
- Ist die Dokumentation für Behörden und Investoren belastbar?

## Typische Fallstricke

Aus der Beratungspraxis: Diese Fehler sollten aktiv vermieden werden.

- Csddd Readiness-Relevanz unterschätzt: Regulierungsrahmen wird zu spät geprüft.
- Fristen versäumt: AWV/BAFA-Fristen sind streng und führen zu Bußgeldern.
- Dokumentationslücken: Behörden und Gerichte verlangen lückenlose Aufzeichnungen.

## Gegenposition

Folgende Gegenargumente sind im Mandantengespräch zu adressieren:

- Behörde (BMWK/BAFA): Behältst du den Ermessensspielraum der Behörde im Blick?
- Vertragspartner China: Welche Interessen und Risikobewertungen hat die chinesische Seite?
- Investoren/Aufsichtsrat: Sind ESG- und Menschenrechts-Anforderungen berücksichtigt?
- Compliance: Wurde auf Exportkontroll- und Sanktions-Risiken geprüft?

## Quellen

Nur frei prüfbare Quellen aus erlaubten Domains. Rechtsprechung nur mit Gericht und Datum.

- [AWG Volltext](https://www.gesetze-im-internet.de/awg_2013/)
- [AWV Volltext](https://www.gesetze-im-internet.de/awv_2013/)
- [BAFA Außenwirtschaft](https://www.bafa.de/DE/Aussenwirtschaft/aussenwirtschaft_node.html)
- [EU-VO 2019/452 EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R0452)
- [LkSG Volltext](https://www.gesetze-im-internet.de/lksg/)
- [BMWK China-Strategie](https://www.bmwk.de/Redaktion/DE/Artikel/Aussenwirtschaft/china-strategie.html)

---

## Skill: `china-customs-tariff-origin-preferential-not`

_Zolltarif und Ursprungsregeln für Waren aus VR China: KN-Nomenklatur, Ursprungsermittlung (wesentliche Be-/Verarbeitung), Präferenzursprung (kein allg. DE-CN-Präferenzabkommen), Ursprungsnachweise, Zollwert (Transaktionswert GATT-Zollwertkodex), Anti-Umgehungsschutz. Output: Ursprungsprüfungsprot..._

# Zolltarif und Warenursprung China: Prüfung und Dokumentation

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Zolltarif und Warenursprung China: Prüfung und Dokumentation
- **Normen-/Quellenanker:** AWG/AWV, EU-Dual-Use, Sanktionen, Zoll/USt, Incoterms, Lieferkette/LkSG/CSDDD, IP-/Know-how-Schutz, Datenschutz/Cybersecurity und lokale China-Compliance live prüfen.
- **Entscheidende Weiche:** Ordne Lieferant, Werk, Datenfluss, Zahlungsweg, Exportgut, politisches Risiko, IP-Leck und Exit-Szenario getrennt.

Begleitet Mandanten und Berater im Wirtschaftsverkehr mit der Volksrepublik China.
Ausgangspunkt ist der konkrete Mandantenfall; Ergebnis ist stets ein verwertbares Arbeitsprodukt.

## Mandantenfall

**Fall 1:** Ein Unternehmen fragt nach konkreten Handlungspflichten im Bereich Customs Tariff Origin China beim Chinageschaeft.

**Fall 2:** Eine Rechtsabteilung benötigt einen Prüfbericht zu Customs Tariff Origin China für ein laufendes China-Projekt.

**Fall 3:** Ein Vorstand bittet um ein Board-Paper zu Customs Tariff Origin China im Kontext der De-risking-Strategie.

## Erste Schritte

1. Sachverhalt und Ziel bestimmen: Was soll im Bereich Customs Tariff Origin China geprüft/erstellt werden?
2. Relevante Normen identifizieren: AWG §§ 55 ff., AWV §§ 55-62a als Ausgangspunkt.
3. Unterlagen sichten: Verträge, Genehmigungen, Behördenschriftverkehr, interne Richtlinien.
4. Risikoeinschätzung Customs Tariff Origin: Kritikalitätsbewertung nach De-risking-Matrix.
5. Maßnahmen priorisieren: Kurzfristige Compliance-Lücken schließen, mittelfristige Strukturmaßnahmen planen.
6. Dokumentation erstellen: Prüfprotokoll, Risikoampel, Handlungsempfehlung.

## Rechtsrahmen

Verbindliches Recht und anerkannte Soft-Law-Quellen für diesen Skill:

- AWG §§ 55 ff.
- AWV §§ 55-62a
- LkSG §§ 3-10
- EU-VO 2019/452
- De-risking-Strategie Bundesregierung 2023: Politisch-strategischer Orientierungsrahmen.
- EU-VO 2019/452: FDI-Kooperationsmechanismus als Referenzrahmen.
- §§ 3-10 LkSG: Lieferkettensorgfaltspflichten als Querschnittspflicht.

Quellen sind getrennt nach deutschem Recht, EU-Recht und chinesischem Recht zu handhaben.
Bei Widersprüchen gilt: Verbindliches Recht geht Soft Law vor; aktueller Stand ist zu prüfen.

## Prüfraster

Schritt für Schritt abzuarbeiten, Ergebnisse dokumentieren:

- Ist Customs Tariff Origin-Relevanz für das konkrete Vorhaben gegeben?
- Welche Normen und Behörden sind zuständig?
- Bestehen Genehmigungs- oder Meldepflichten?
- Welche Fristen sind zu beachten?
- Gibt es De-risking- oder Diversifizierungsanforderungen?
- Ist die Dokumentation für Behörden und Investoren belastbar?

## Typische Fallstricke

Aus der Beratungspraxis: Diese Fehler sollten aktiv vermieden werden.

- Customs Tariff Origin-Relevanz unterschätzt: Regulierungsrahmen wird zu spät geprüft.
- Fristen versäumt: AWV/BAFA-Fristen sind streng und führen zu Bußgeldern.
- Dokumentationslücken: Behörden und Gerichte verlangen lückenlose Aufzeichnungen.

## Gegenposition

Folgende Gegenargumente sind im Mandantengespräch zu adressieren:

- Behörde (BMWK/BAFA): Behältst du den Ermessensspielraum der Behörde im Blick?
- Vertragspartner China: Welche Interessen und Risikobewertungen hat die chinesische Seite?
- Investoren/Aufsichtsrat: Sind ESG- und Menschenrechts-Anforderungen berücksichtigt?
- Compliance: Wurde auf Exportkontroll- und Sanktions-Risiken geprüft?

## Quellen

Nur frei prüfbare Quellen aus erlaubten Domains. Rechtsprechung nur mit Gericht und Datum.

- [AWG Volltext](https://www.gesetze-im-internet.de/awg_2013/)
- [AWV Volltext](https://www.gesetze-im-internet.de/awv_2013/)
- [BAFA Außenwirtschaft](https://www.bafa.de/DE/Aussenwirtschaft/aussenwirtschaft_node.html)
- [EU-VO 2019/452 EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R0452)
- [LkSG Volltext](https://www.gesetze-im-internet.de/lksg/)
- [BMWK China-Strategie](https://www.bmwk.de/Redaktion/DE/Artikel/Aussenwirtschaft/china-strategie.html)

---

## Skill: `china-de-risking-nicht-strategie`

_Operative Umsetzung der EU/Bundesregierungs-De-risking-Strategie: Abgrenzung De-risking vs. Decoupling, Risikoklassifizierung von Lieferanten und Technologien nach Kritikalitäts-Score, AWG/AWV-Sektorenliste, Diversifizierungsfahrplan. Output: De-risking-Fahrplan mit Priorisierungsmatrix und Resso..._

# De-risking statt Decoupling: Strategie und operative Umsetzung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: De-risking statt Decoupling: Strategie und operative Umsetzung
- **Normen-/Quellenanker:** AWG/AWV, EU-Dual-Use, Sanktionen, Zoll/USt, Incoterms, Lieferkette/LkSG/CSDDD, IP-/Know-how-Schutz, Datenschutz/Cybersecurity und lokale China-Compliance live prüfen.
- **Entscheidende Weiche:** Ordne Lieferant, Werk, Datenfluss, Zahlungsweg, Exportgut, politisches Risiko, IP-Leck und Exit-Szenario getrennt.

Begleitet Mandanten und Berater im Wirtschaftsverkehr mit der Volksrepublik China.
Ausgangspunkt ist der konkrete Mandantenfall; Ergebnis ist stets ein verwertbares Arbeitsprodukt.

## Mandantenfall

**Fall 1:** Ein DAX-Konzern will seiner China-Geschaeftsstrategie eine formal belastbare De-risking-Dokumentation geben, die Investoren und Aufsichtsrat überzeugt.

**Fall 2:** Ein Mittelständler fragt, welche seiner China-Lieferanten echte Risiken darstellen und welche unbedenklich weiterlaufen können.

**Fall 3:** Eine Anwaltskanzlei erarbeitet Compliance-Memo zu De-risking für drei Industriemandanten in unterschiedlichen Sektoren.

## Erste Schritte

1. Begriffe klären: De-risking (selektive Risikominderung) vs. Decoupling (Totalentkopplung) nach EU-Kommissionsterminologie.
2. Risikomatrix erstellen: Abhängigkeitsgrad, Substituierbarkeit, sicherheitspolitische Sensitivität je Lieferant/Technologie.
3. Kritikalitätssektoren gemäß AWV-Anlage und KRITIS-Definition des BSI abgleichen.
4. Bestehende JV- und Lieferverträge auf Change-of-Control und Kündigungsklauseln prüfen.
5. De-risking-Fahrplan mit Zeithorizonten 1/3/5 Jahre erstellen.
6. Board-Paper-Vorlage erstellen mit Risiko-Ampel, Maßnahmenplan und KPIs.

## Rechtsrahmen

Verbindliches Recht und anerkannte Soft-Law-Quellen für diesen Skill:

- EU-Kommission Mitteilung 'Ein fairer und nachhaltiger Wirtschaftsansatz gegenüber China' 2023: Konzept De-risking.
- § 55 AWG: Ermächtigungsgrundlage für Beschränkungen im nationalen Sicherheitsinteresse.
- §§ 55-62a AWV: Sektorale Zuständigkeiten und Untersagungsvoraussetzungen.
- Critical Raw Materials Act (EU) 2024 VO: Diversifizierungspflichten für kritische Rohstoffe.
- EU-VO 2019/452 Art. 4: FDI-Screening-Kriterien als Risikoindikatoren.
- § 4 LkSG: Risikomanagement-System als Referenzrahmen für De-risking-Dokumentation.

Quellen sind getrennt nach deutschem Recht, EU-Recht und chinesischem Recht zu handhaben.
Bei Widersprüchen gilt: Verbindliches Recht geht Soft Law vor; aktueller Stand ist zu prüfen.

## Prüfraster

Schritt für Schritt abzuarbeiten, Ergebnisse dokumentieren:

- Welche Produkte/Technologien haben keinen außerchinesischen Substituten?
- Welche Lieferanten sind staatsnah oder unter SAMR-Kontrolle?
- Welcher Anteil des Umsatzes hängt von einem einzigen chinesischen Abnehmer ab?
- Bestehen Transferverpflichtungen für Technologie in JV-Verträgen?
- Sind kritische Rohstoffe (Seltene Erden, Gallium, Germanium) involviert?
- Wie ist der Zeithorizont für Alternativbeschaffung realistisch einzuschätzen?

## Typische Fallstricke

Aus der Beratungspraxis: Diese Fehler sollten aktiv vermieden werden.

- De-risking als Alibi: Rein kosmetische Maßnahmen ohne operative Wirkung schaffen Haftungsrisiken.
- Überregulierung unterschätzt: Zu schnelles Decoupling kann bestehende Verträge brechen und Schadenersatzpflichten auslösen.
- Rohstoffketten ignoriert: Tier-2/Tier-3-Abhängigkeiten werden erst sichtbar, wenn Krise eintritt.

## Gegenposition

Folgende Gegenargumente sind im Mandantengespräch zu adressieren:

- Behörde (BMWK/BAFA): Behältst du den Ermessensspielraum der Behörde im Blick?
- Vertragspartner China: Welche Interessen und Risikobewertungen hat die chinesische Seite?
- Investoren/Aufsichtsrat: Sind ESG- und Menschenrechts-Anforderungen berücksichtigt?
- Compliance: Wurde auf Exportkontroll- und Sanktions-Risiken geprüft?

## Quellen

Nur frei prüfbare Quellen aus erlaubten Domains. Rechtsprechung nur mit Gericht und Datum.

- [BMWK China-Strategie 2023](https://www.bmwk.de/Redaktion/DE/Artikel/Aussenwirtschaft/china-strategie.html)
- [AWG Volltext](https://www.gesetze-im-internet.de/awg_2013/)
- [AWV Volltext](https://www.gesetze-im-internet.de/awv_2013/)
- [EU-VO 2019/452 EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R0452)
- [LkSG Volltext](https://www.gesetze-im-internet.de/lksg/)

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

