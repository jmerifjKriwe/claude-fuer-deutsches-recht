# Megaprompt: fachanwalt-bank-kapitalmarktrecht

> *Achtung: Dies ist ein experimentelles Mega-Prompt-Markdown, das einen kompletten Klotzkette-Plugin in eine einzige Datei zusammenfuehrt. Keine Haftung, keine Gewaehr. Nur zum Ausprobieren der Skills auch ohne Claude Code; keine Rechtsberatung. Vor Verwendung im Mandat anwaltlich pruefen.*
>
> *Caution: This is an experimental Mega-Prompt Markdown that consolidates a full Klotzkette plugin into a single file. No warranty, no liability. For exploration with chat tools that do not run Claude Code only; not legal advice.*

**Verwendung:** Diesen gesamten Text in einen Chat ohne Claude-Code-Integration einfuegen (oder als Datei hochladen). Der Chat-Agent erhaelt damit die gebuendelten Skills dieses Plugins als Kontext. Eine Replikation des vollen Plugin-Verhaltens ist nicht garantiert — der Megaprompt ist eine Best-Effort-Kompression.


## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 72 Skills des Plugins `fachanwalt-bank-kapitalmarktrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Fachanwalt Bank- und Kapitalmarktrecht: ordnet Rolle (Anleger/Kunde, Bank/WPI, BaFin), …
2. **mandat-triage-bank-kapitalmarktrecht** — Bank- oder Kapitalmarktrechts-Mandat trifft ein und muss strukturiert erfasst werden: Sachgebiet Mandantenrolle Sofort-F…
3. **orientierung-fachanwaltschaft-mandat** — Anwalt will Fachanwaltschaft Bank-Kapitalmarktrecht erwerben oder Mandat bearbeiten und braucht Normen-Überblick: KWG ZA…
4. **erstgespraech-mandatsannahme** — Strukturierter Erstgespraechsleitfaden für Bank-, Kapitalmarkt- und Wertpapierrecht: Erfassung der Konstellation, Konfli…
5. **erstpruefung-und-mandatsziel** — Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.
6. **output-waehlen** — Output-Wahl für Fachanwalt Bank- und Kapitalmarktrecht: stimmt Adressat (Anleger/Kunde, Bank/WPI, BaFin), Frist (Widerru…
7. **dokumente-intake** — Dokumentenintake für Fachanwalt Bank- und Kapitalmarktrecht: sortiert Darlehensvertrag, Wertpapierorder, Beratungsprotok…
8. **anschluss-routing** — Anschluss-Routing für Fachanwalt Bank- und Kapitalmarktrecht: wählt den nächsten Spezial-Skill nach Engpass (Widerrufsfr…
9. **bk-bankenfehlberatung-grundzuege** — Bankenfehlberatungs-Anspruch in Grundzuegen: § 280 BGB, anlegergerechte Beratung, anlagegerechte Beratung, MiFID II Geei…
10. **bk-emissionsprospekt-haftung-spezial** — Spezialfall Emissionsprospekthaftung: WpPG, ProspektG, Verantwortliche, Gewaehrleistungserklaerung, fehlerhafte Angaben,…
11. **bk-mifid-suitability-spezial** — Spezialfall MiFID II Geeignetheits- und Angemessenheitspruefung: Anlegerprofil, Ziele, Risikobereitschaft, Verlusttragfa…
12. **anlageberatung-fehlerhaft** — Fachanwalt Bank Kapitalmarktrecht Anlageberatung Fehlerhaft: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizie…
13. **anlageberatungsfehler-pruefen** — Anlageberatungsfehler Pruefen: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer be…
14. **bankaufsicht-erlaubnis-und-vertrieb** — Bankaufsichtliche Erlaubnis-, Vertriebs- und Organisationsrisiken: führt schnell durch Sachverhalt, Rechtsgrundlagen, Be…
15. **bankrecht-buergschaft-auf-erste-anforderung** — Bürgschaft oder Bankgarantie auf erste Anforderung im Mandat prüfen: Zahlungsmechanik, Einwendungen, offensichtlicher Mi…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Fachanwalt Bank- und Kapitalmarktrecht: ordnet Rolle (Anleger/Kunde, Bank/WPI, BaFin), markiert Frist (Widerrufsfrist Verbraucherdarlehen 14 Tage § 355 BGB), wählt Norm (BGB §§ 488/491-505, WpHG, KAGB) und Zuständigkeit (BaFin), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Fachanwalt Bank Kapitalmarktrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `anlageberatung-fehlerhaft` — Anlageberatung Fehlerhaft Cybertrading
- `anlageberatungsfehler-pruefen` — Anlageberatungsfehler Bankrecht Akkreditiv
- `bankaufsicht-erlaubnis-und-vertrieb` — Bankaufsicht Erlaubnis Emissionsprospekt
- `bankrecht-buergschaft-aval-garantie-routing` — Bankrecht Buergschaft Aval Garantieabruf
- `bankrecht-privatbuergschaft-sittenwidrigkeit` — Bankrecht Privatbuergschaft Regress BK
- `bausparvertrag-zinsanpassung-bgh-xi-zr-78-22` — Bausparvertrag Zinsanpassung BGH XI ZR 78 22
- `beratungshaftung-zahlen-schwellen-und-berechnung` — Beratungshaftung Haftung Beweislast BK CUM
- `bk-bankenfehlberatung-grundzuege` — BK Bankenfehlberatung Grundzuege Einfuehrung
- `bk-mifid-suitability-spezial` — BK Mifid BK Prip Erstgespraech Mandatsannahme
- `cum-ex-beihilfe-bgh-1-str-519-20` — CUM EX Beihilfe BGH 1 STR 519 20
- `dispokredit-zinsanpassung-bgh-xi-zr-78-08` — Dispokredit Zinsanpassung BGH XI ZR 78 08
- `einstieg-schnelltriage-fallrouting` — FA Bank Kapitalmarkt BK Bafin Chronologie
- `workflow-fristen-und-risikoampel` — FA Bank Kapitalmarkt Fristen Risiko Mandant
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Fachanwalt Bank Kapitalmarktrecht sind KWG, WpHG, WpIG, ZAG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `mandat-triage-bank-kapitalmarktrecht`

_Bank- oder Kapitalmarktrechts-Mandat trifft ein und muss strukturiert erfasst werden: Sachgebiet Mandantenrolle Sofort-Fristen: V..._

# Bank- oder Kapitalmarktrechts-Mandat trifft ein und muss strukturiert erfasst werden: Sachgebiet Mandantenrolle Sofort-Fristen


## Aktenstart statt Formularstart

Wenn zu **Mandat Triage Schriftsatzkern Substantiierung** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Fachanwalt Bank Kapitalmarktrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; WpIG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Bank- oder Kapitalmarktrechts-Mandat trifft ein und muss strukturiert erfasst werden: Sachgebiet Mandantenrolle Sofort-Fristen. Verjährung §§ 195 199 Abs. 3 BGB 3 Jahre / 10 Jahre. Normen je nach Routing. Prüfraster Sachgebiets-Zuordnung Fristen-Sofort-Check Eskalation Kontosperrung BaFin-Anordnung. Output Mandat-Karte Routing-Empfehlung Handlungsweichen. Abgrenzung zu erstgespraech-mandatsannahme (Vollaufnahme) und fachanwalt-bank-kapitalmarktrecht-orientierung (Überblick).

### Mandat-Triage Bank- und Kapitalmarktrecht

## Ablauf — acht Fragen

### Frage 1 — Mandantenrolle?

- Anleger / Sparer
- Kreditnehmer (Verbraucher / Unternehmer)
- Sicherheitengeber (Bürge Grundschuldgeber)
- Bank / Sparkasse
- Vorstand / Geschäftsleiter Bank
- Compliance Geldwäschebeauftragter
- Aufsicht (BaFin)

### Frage 2 — Sachgebiet?

- Anlageberatungsfehler
- Kapitalmarktinformationshaftung (Falschangaben Ad-hoc)
- Prospekthaftung
- Verbraucherkredit Widerruf § 495 ff. BGB Widerrufsjoker
- Immobilienfinanzierungs-Beratung
- Bank-AGB Kontoführung Kontosperre
- Kontopfändung Pfändungsschutz P-Konto §§ 850k 899 ff. ZPO (Pfändungsschutzkonto seit PKoFoG 01.12.2021 in §§ 899-910 ZPO)
- Kreditsicherheiten Grundschuld Bürgschaft Sicherungsabtretung
- Geldwäsche § 261 StGB AMLA
- BaFin-Aufsicht Sanktionen
- Banken-Restrukturierung / Sanierungsmaßnahmen
- Crypto-Asset MiCAR

### Frage 3 — Akute Eilbedürftigkeit?

- Kontosperre (Geldwäsche-Verdacht oder AGB-Kündigung)
- Kreditkündigung — Verwertung droht
- BaFin-Anordnung sofortige Vollziehung
- Vorläufige Untersagung Geschäftsbetrieb
- Pfändung-Konto wirtschaftliche Existenz
- Klage-Fristablauf Hauptsachefrist nach Schiedsspruch

### Frage 4 — Stand?

- Beratung vor Vertragsschluss
- Vertrag läuft Streit über Leistung
- Außergerichtlicher Schriftwechsel
- Ombudsstelle der Banken läuft (Hemmung Verjährung)
- Klage erhoben
- BaFin-Verfahren
- Strafverfahren Geldwäsche

### Frage 5 — Produktart bei Anlageberatung?

- Aktie Fonds (offen geschlossen)
- Anleihe Zertifikat strukturiertes Produkt
- Schiffsfonds Immobilienfonds Filmfonds
- Lebensversicherung als Anlage
- Swap-Geschäfte
- Crypto-Asset

### Frage 6 — Vertragsbasis?

- Beratungsvertrag konkludent
- Vermögensverwaltungs-Vertrag
- Bank-AGB der konkreten Bank
- Prospekt
- WpHG-Bestätigungen

### Frage 7 — Frist?

- **Verjährung Anlageberatung** drei Jahre Kenntnis / zehn Jahre Beratung § 195 199 BGB
- **Widerrufsjoker** Verbraucherkredit Immobiliendarlehen-Widerruf — Bei fehlerhafter Belehrung verlängerter Widerruf
- **Ombudsstelle** Hemmung Verjährung
- **Strafverfahren Geldwäsche** Verjährung je nach Strafmaß

### Frage 8 — Wirtschaftliche Verhältnisse?

- Hohes Anlagevolumen (Schadenshöhe)
- Berufshaftpflicht Anlageberater
- Versicherer für Bank?
- Rechtsschutz Anleger?

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Anlageberatungsfehler | `anlageberatungsfehler-pruefen` |
| Prospekthaftung | `anlageberatungsfehler-pruefen` plus Prospektfokus |
| Verbraucherkredit Widerruf | (Skill verbraucherkredit-widerruf — perspektivisch) |
| Immobilienkredit | (Skill immobilienkredit-prüfen — perspektivisch) |
| Bank-AGB-Klauselstreit | (Skill agb-banken-pruefen — perspektivisch) |
| Kontosperre | (Skill kontosperre-prüfen — perspektivisch) |
| Geldwäsche-Strafverfahren | weiter an `mandat-triage-strafrecht` plus |
| BaFin-Aufsichtsverfahren | weiter an `mandat-triage-verwaltungsrecht` |
| Pfändung P-Konto | weiter an `forderungsmanagement-klagewerkstatt` |
| Crypto / MiCAR | (Skill micar-compliance — perspektivisch) |

## Mandatsannahme

- **Konflikt-Check** — keine Doppelmandate Bank/Kunde
- **Streitwert** Anlageverlust voll oder Differenzhypothese
- **Sachverständigen-Bedarf** Wertentwicklung Marktwert
- **Versicherungs-Deckung** Anleger-Rechtsschutz

## Eskalation

- **Telefon-Sofort** Kontosperre BaFin Hausdurchsuchung Bank-Mitarbeiter
- **Binnen einer Stunde** Widerrufs-Schreiben bei Fristablauf
- **Heute** Ombudsstellen-Antrag Verzugsschreiben
- **Diese Woche** Klage-Erstentwurf Schadensberechnung

## Ausgabe

- `triage-protokoll-bank-kapital.md`
- Aktenanlage
- Frist im Fristenbuch
- Ombudsstellen-Antrag oder Klage-Empfehlung
- Mandatsvereinbarung
- Empfehlung Folge-Skill

## Quellen

- BGB §§ 195 199 280 311 488 ff. 495 ff. 765 ff.
- WpHG MiFID-II
- VermAnlG WpPG
- StGB § 261
- KWG
- ZPO §§ 850k 899-910 (PKoFoG)
- BGH XI. Zivilsenat — Bond Lehman Ille Kickback

## Vertiefung: Rechtsprechung und erweiterte Triage

### Schluessel-Leitsaetze für Triage Bank-/Kapitalmarktrecht (Stand Mai 2026)

Verifizierte Aktenzeichen mit offener Quelle:

- BGH XI ZR 22/24, Urt. v. 20.5.2025 — Vorfälligkeitsentschädigung intransparente AGB (juris.bundesgerichtshof.de)
- BGH XI ZR 133/24, Urt. v. 21.10.2025 — Referenzzins Prämiensparvertrag (PM Nr. 225/2025)
- BGH VI ZR 183/22, Urt. v. 28.1.2025 — SCHUFA-Meldung / DSGVO-Schadensersatz (juris.bundesgerichtshof.de)
- BGH VI ZR 431/24, Urt. v. 14.10.2025 — SCHUFA Positivdaten / Betrugspraevention (PM Nr. 209/2025)
- EuGH C-26/22, C-64/22, Urt. v. 7.12.2023 — Restschuldbefreiungs-Speicherung max. 6 Monate (curia.europa.eu)
- EuGH C-634/21, Urt. v. 7.12.2023 — SCHUFA-Score als automatisierte Entscheidung Art. 22 DSGVO (curia.europa.eu)
- EuGH C-66/19, Urt. v. 26.3.2020 — Widerrufsbelehrung Kaskadenverweisung (curia.europa.eu)

### Erweiterte Triage-Matrix

| Konstellation | Sofortmassnahme | Folge-Skill |
|---|---|---|
| Widerruf Immobiliendarlehen, Frist laeuft | SOFORT Widerruf erklaeren | `widerrufsjoker-immobiliendarlehen` |
| Anlageberatung, Verjaebrung naht | Ombudsmann SOFORT (hemmt Verjaebrung) | `anlageberatungsfehler-pruefen` |
| Kreditkuendigung ohne § 498-Voraussetzungen | Widerspruch + Feststellungsklage | `fachanwalt-bank-kapitalmarktrecht-kreditkuendigung` |
| SCHUFA-Eintrag rechtswidrig | Loeschungsverlangen Art. 17 DSGVO | `fachanwalt-bank-kapitalmarktrecht-schufa-eintrag` |
| Cybertrading-Betrug, < 8 Wochen | SEPA-Recall SOFORT | `fachanwalt-bank-kapitalmarktrecht-cybertrading-anlagebetrug` |
| MiCA-Stablecoin BaFin-Lizenz | Whitepaper + Antrag vorbereiten | `fachanwalt-bank-kapitalmarktrecht-mica-stablecoin-art-16-bafin` |
| Negativzins-Klausel AGB | AGB-Kontrolle § 307 BGB + Rueckforderung | `anlageberatungsfehler-pruefen` |

### Entscheidungsbaum Verjaebrung

Ist die Verjaebrungsfrist bekannt?
→ NEIN: Datum der Beratung/Schaden + 3 Jahre = § 195 BGB; aber max. 10 Jahre ab Entstehung § 199 Abs. 3 BGB
→ JA und < 6 Monate: Ombudsmann-Antrag zur Hemmung SOFORT; parallel Klageschrift vorbereiten
→ JA und > 10 Jahre: Verjaebrung eingetreten; Sonderfall Arglist § 199 Abs. 3 Nr. 2 BGB pruefen

### Output-Template Triage-Protokoll
**Adressat:** Intern — Tonfall: schnell, strukturiert

```
TRIAGE-PROTOKOLL Bank-/Kapitalmarktrecht
=========================================
Eingangsdatum: [TT.MM.JJJJ]
Mandant: [NAME]
Sachgebiet: [Anlageberatung / Verbraucherkredit / Kreditkuendigung ...]
Sofortfrist: [DATUM + RECHTSGRUNDLAGE]
Verjaebrung: [3 Jahre ab XX.XX.XXXX]
Streitwert: EUR [BETRAG]
Prioritaet: [ROT / GELB / GRUEN]
Folge-Skill: [SKILL-NAME]
Naechster Schritt: [MASSNAHME] bis [DATUM] durch [PERSON]
=========================================
```

## Audit-Hinweis (27.05.2026)

Stand Mai 2026 wurden die Aktenzeichen anhand offener Quellen (juris.bundesgerichtshof.de, dejure.org, curia.europa.eu) verifiziert. Frühere Modellwissen-Platzhalter sind durch belegte Aktenzeichen ersetzt. Vor Versand vom Anwalt erneut zu prüfen.

---

## Skill: `orientierung-fachanwaltschaft-mandat`

_Anwalt will Fachanwaltschaft Bank-Kapitalmarktrecht erwerben oder Mandat bearbeiten und braucht Normen-Überblick: KWG ZAG WpHG WpIG MiFID-II MA..._

# Anwalt will Fachanwaltschaft Bank-Kapitalmarktrecht erwerben oder Mandat bearbeiten und braucht Normen-Überblick


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; WpIG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Anwalt will Fachanwaltschaft Bank-Kapitalmarktrecht erwerben oder Mandat bearbeiten und braucht Normen-Überblick. KWG ZAG WpHG WpIG MiFID-II MAR MiCAR BGB-Verbraucherkreditrecht §§ 491 ff. Normen KWG §§ 1 32 WpHG §§ 63 ff. §§ 491-505 BGB. Prüfraster FAO-Voraussetzungen Mandatstypen Normen-Karte. Output Orientierungs-Leitfaden. Abgrenzung zu allen Einzel-Skills (nur Überblick und Routing).

### Fachanwalt für Bank- und Kapitalmarktrecht — Orientierung

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 60 Fälle in den letzten drei Jahren, davon mindestens 30 streitige.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Bankaufsicht | KWG (Kreditwesengesetz) |
| Zahlungsdienste | ZAG |
| Wertpapierhandel | WpHG WpIG MiFID-II (EU-RL 2014/65) |
| Marktmissbrauch | MAR Marktmissbrauchsverordnung (EU 596/2014) |
| Wertpapierprospekt | Prospekt-VO (EU 2017/1129) WpPG |
| Krypto-Assets | MiCAR (EU 2023/1114) |
| Verbraucherkredit | §§ 491 ff. BGB CCD-Richtlinie |
| Anlageberatung | §§ 31 ff. WpHG (Wohlverhalten Anlageberatung-Documentation) |
| Vermögensanlage | VermAnlG VermAnlVerkProspV |
| KAGB | KAGB Investmentvermögen |
| Geldwäsche | GwG |

## Typische Mandate

- Verbraucherkredit (Widerruf nachträgliche AGB-Prüfung)
- Schadensersatz Anlageberatung Beratungspflicht-Verletzung (Bond-Schiff-Anlagen Lehman-Anlagen Cum-Ex)
- Aufsichtsrechtsverfahren BaFin-Verfahren (Genehmigung Untersagung)
- Krypto-Asset Compliance MiCAR
- M&A im Finanzdienstleistungs-Bereich
- Prospekthaftung
- Insolvenzanfechtung von Kreditrückzahlungen

## Fristen

- **BGB-Widerrufsfrist** 14 Tage bei Fernabsatz und Haustürgeschäft (§§ 312g 355 BGB) — bei fehlender Belehrung verlängert.
- **Beratungshaftung Verjährung** drei Jahre (§ 195 BGB) ab Kenntnis; Höchstfrist zehn Jahre (§ 199 BGB).
- **WpHG-Pflichten** laufende Aufzeichnung.
- **Meldepflichten BaFin** unverzueglich bei meldepflichtigen Ereignissen.
- **MAR Insider-Mitteilung** unverzueglich; Stimmrechtsmitteilungen §§ 33 ff. WpHG vier Handelstage.

## Hauptgerichte

- Landgericht Zivilkammer für Bank- und Kapitalmarktsachen.
- OLG-Spezialsenate.
- BGH XI. Zivilsenat (Bankrecht).
- VG / OVG / BVerwG bei BaFin-Verwaltungsverfahren.
- BaFin selbst als Aufsichtsbehörde.

## Berufsverband

- ARGE Bank- und Kapitalmarktrecht DAV.

## Schnittstellen

- **gesellschaftsrecht** bei M&A und Kapitalmaßnahmen.
- **regulatorisches-recht** bei BaFin-Aufsicht.
- **kanzlei-allgemein** Fristen Versand.
- **insolvenzrecht** bei Anfechtung.

## Vertiefung: Rechtsprechung und aktuelle Linien (Stand Mai 2026)

### Schluessel-Leitsaetze BGH XI. Zivilsenat Bank-/Kapitalmarktrecht (jeweils Volltext in offener Quelle prüfen)

- **BGH XI ZR 22/24** v. 20.5.2025 — Vorfälligkeitsentschädigung Immobiliendarlehen: intransparente AGB-Klausel führt zum Verlust des VFE-Anspruchs. Quelle: juris.bundesgerichtshof.de
- **BGH XI ZR 133/24** v. 21.10.2025 — Referenzzins für Zinsanpassungen in Praemiensparvertraegen (Folgeentscheidung). Quelle: bundesgerichtshof.de PM Nr. 225/2025
- **BGH XI ZR 553/19** 2024 — Stärkung der Rechte von Darlehensnehmern bei Altforderungen (Volltext und Datum vor Versand verifizieren). Quelle: juris.bundesgerichtshof.de

### EuGH-Linien

- **EuGH C-26/22 und C-64/22** v. 7.12.2023 — SCHUFA / Restschuldbefreiung max. 6 Monate Speicherung. Quelle: curia.europa.eu
- **EuGH C-634/21** v. 7.12.2023 — SCHUFA-Score als automatisierte Entscheidung i.S.v. Art. 22 DSGVO. Quelle: curia.europa.eu
- **EuGH C-66/19** v. 26.3.2020 (Kreissparkasse Saarlouis) — Kaskadenverweisung in Widerrufsbelehrung unzulässig. Quelle: curia.europa.eu

### Normen-Ueberblick nach Mandatstyp
| Mandat | Zentralnorm |
|---|---|
| Widerruf Verbraucherkredit | §§ 491, 495, 355 BGB; EGBGB Art. 247 |
| Anlageberatung fehlerhaft | §§ 280, 311 BGB; §§ 63-64 WpHG |
| Prospekthaftung | §§ 9-11 VermAnlG; §§ 21-23 WpPG |
| Kreditkuendigung | §§ 488, 490, 498 BGB |
| BaFin-Aufsicht | §§ 32-35 KWG; §§ 2, 6 WpIG |
| Marktmissbrauch | MAR Art. 14-16 (VO 596/2014) |
| AML/KYC | §§ 2, 10-17 GwG |
| MiCA Stablecoin | MiCA Art. 16-21 VO 2023/1114 |

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Fristen Ueberblick
| Frist | Dauer | Norm |
|---|---|---|
| Verjaebrung Beratungsfehler | 3 Jahre ab Kenntnis | §§ 195, 199 Abs. 1 BGB |
| Absolute Hoechstfrist | 10 Jahre | § 199 Abs. 3 Nr. 1 BGB |
| Widerruf Verbraucherkredit | 14 Tage / bei fehlender Belehrung verlg. | §§ 355, 495 BGB |
| Ombudsmann-Hemmung | bis Verfahrensende + 3 Monate | § 204 Abs. 1 Nr. 4 BGB |
| Stimmrechtsmitteilung WpHG | 4 Handelstage | §§ 33, 35 WpHG |

---

## Skill: `erstgespraech-mandatsannahme`

_Strukturierter Erstgespraechsleitfaden für Bank-, Kapitalmarkt- und Wertpapierrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen: Strukturierter Erstgespraechsl..._

# Strukturierter Erstgespraechsleitfaden für Bank-, Kapitalmarkt- und Wertpapierrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; WpIG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierter Erstgespraechsleitfaden für Bank-, Kapitalmarkt- und Wertpapierrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.

### Erstgespraech und Mandatsannahme im Bank-, Kapitalmarkt- und Wertpapierrecht

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Bank-, Kapitalmarkt- und Wertpapierrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klaeren, Konflikt- und GwG-Pruefung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für Bank-, Kapitalmarkt- und Wertpapierrecht:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klaegerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Anlageberatung, Verbraucherdarlehen, Widerruf, Phishing, AGB-Banken, Geldwaesche
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Klage auf Schadensersatz aus Falschberatung, Widerrufsklage Verbraucherdarlehen). Frist-Alarm an die Vorbereitung weitergeben.

### 2. Konflikt-Pruefung und GwG-Check (5 Min.)

- Konflikt-Check ueber Mandantsystem: Gegnerin, Streitgegenstand, frueherer Mandant?
- GwG-Identifizierung: amtlicher Lichtbildausweis (Ausweisscan), bei juristischer Person Handelsregister-/Transparenzregister-Auszug, ggf. wirtschaftlich Berechtigte/n.
- Risikobewertung (niedrig/mittel/hoch) abhaengig von Mandatscharakter, Bargeld, Auslandsbezug.
- Doku im Mandatsbogen (Pflicht nach §§ 10 ff. GwG i.V.m. § 2 Abs. 1 Nr. 10 GwG für RA-Mandate).

### 3. Vollmacht und Schweigepflichtentbindung

- Allgemeine Prozess-/Aussenvollmacht (BORA, ZPO, FamFG, je nach Fachgebiet).
- Spezielle Vollmachten: ggf. Akteneinsicht Strafakte, KV-Abrechnungsdaten, Sozialdaten (Schweigepflichtentbindung gegenueber Krankenkasse, Arzt, Behörde).
- Bei Eheleuten/GbR/GmbH: einzelvollmachtgebende Person und Vertretungsmacht klaeren.

### 4. Streitwert und Gebührenvereinbarung

Standard-Streitwerte im Bereich Bank-, Kapitalmarkt- und Wertpapierrecht:

- Skizze: Streitwert grob abschaetzen (z.B. Hauptforderung, ggf. + Zinsen, Nebenforderungen).
- RVG-Pauschalrechnung (Berechnungstool im Plugin) oder Stundenhonorarvereinbarung.
- Beratungshilfe-/Prozesskostenhilfe-Antrag pruefen, wenn wirtschaftlich angezeigt.
- Vorschussanforderung nach § 9 RVG.

### 5. Strategie-Erstskizze

Drei Weichen am Ende des Erstgespraechs:

- **Mandat annehmen:** vollstaendig (Pruefung + Schriftsatz) oder begrenzt (nur Pruefung/Gutachten).
- **Verweisen:** wenn Spezialgebiet ausserhalb der Fachanwaltschaft, oertlich unzuständig oder Konflikt.
- **Ablehnen:** offensichtlich aussichtslos, GwG-Hit, Bauchgefuehl-Vorsicht.

## Pflicht-Output am Ende

1. **Mandatsbogen** mit Beteiligten, Konflikt-Check, GwG-Status, Streitwert.
2. **Frist-Liste** (Sofortfristen, Verjährung, Ausschlussfristen, Beweisanforderungs-Fristen).
3. **Anlagenverzeichnis** des uebergebenen Datenraums (Stand erstes Sortieren).
4. **Naechster-Schritt-Plan:** binnen 24/48/72 h, Owner, Output.
5. **Honorarvereinbarung** unterschrieben oder Vorbehalt notiert.

## Relevante Rechtsgrundlagen und Standards

- BORA, BRAO, FAO für Fachanwaltschaft Bank-, Kapitalmarkt- und Wertpapierrecht.
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- §§ 488 ff. BGB, WpHG, KWG, ZAG, GwG, MiFID II, PRIIPs-VO, MaComp (für fachliche Erstpruefung).
- DSGVO und BDSG für den Umgang mit Mandantendaten (Art. 6 DSGVO als Rechtsgrundlage, Art. 9 ggf. Gesundheitsdaten).

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

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Bank-, Kapitalmarkt- und Wertpapierrecht). Handlungs-Sequenz:

1. Sofort-Vollmacht und Sofort-Akteneinsicht (per beA, ELSTER, Behördenportal).
2. Antrag auf Wiedereinsetzung (§ 233 ZPO, § 60 VwGO, § 110 AO) als Reserve dokumentieren.
3. Spaeteste-Stunde-Versand-Plan: beA bevorzugt, mit qualifizierter Signatur und Empfangsbekenntnis.
4. Honorarvereinbarung NICHT auf Eilzuschlag verzichten - aber transparent kommunizieren.

### Konstellation B: Komplexer Sachverhalt, Datenraum unsortiert

Mandant uebergibt 200+ Dateien (PDF-Scans, E-Mails, Excel-Listen). Vor jeder fachlichen Bewertung:

1. Datenraum-Index in Excel: Datum, Absender, Empfaenger, Aktenzeichen, kurze Inhaltszeile.
2. Chronologischer Verlauf als Zeitstrahl - Spielraum für Verjährungs- und Ausschlussfristen identifizieren.
3. Loecher im Datenraum gezielt anfordern (Mandantenfragen-Katalog).

### Konstellation C: Interessenkonflikt-Naehe

Frueheres Mandat mit derselben Gegnerin oder gleichem Sachzusammenhang. Pruefung:

1. § 43a Abs. 4 BRAO und § 3 BORA - Sachzusammenhang, nicht nur Personenidentitaet.
2. Einwilligung beider Mandanten in Textform (mit konkreter Beschreibung).
3. Bei Zweifel: Mandat ablehnen und an Kanzleikollegium ueberweisen.

## Mandanten-Erwartungsmanagement

- Realistische Erfolgs- und Kostenprognose (nicht "Wir gewinnen sicher").
- Verfahrensdauer im Bereich Bank-, Kapitalmarkt- und Wertpapierrecht: Erfahrungswerte nach Instanz.
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

- `vergleichsverhandlung-strategie` (im selben Plugin) für den Fall, dass aussergerichtliche Loesung angestrebt wird.
- `schriftsatzkern-substantiierung` (im selben Plugin) für den Schriftsatzaufbau, wenn Klage/Widerspruch eingereicht wird.
- Kanzlei-Allgemein-Plugin `kanzlei-allgemein` für Konflikt-, GwG- und PEP-Pruefroutinen.

## Vertiefung: Rechtsprechung und Normen

### Zentrale Normen Erstmandat Bank-/Kapitalmarktrecht
- § 2 Abs. 1 Nr. 10 GwG — Rechtsanwaelte als Verpflichtete nach GwG bei bestimmten Taetigkeiten (Kauf/Verkauf Immobilien, Verwaltung Treuhand, Gruendung Gesellschaften)
- §§ 10 ff. GwG — Sorgfaltspflichten: Identifizierung, Abklaerung wirtschaftlich Berechtigter, Risikoanalyse
- §§ 488, 491 ff. BGB — Darlehens- und Verbraucherkredit-Basisnormen für erste Sachverhaltspruefung
- §§ 63, 64, 83 WpHG — Pflichten Anlageberatung (Geeignetheit, Angemessenheit, Protokoll)
- § 43a Abs. 4 BRAO, § 3 BORA — Verbot widerstreitender Interessen

### Leitsaetze zum Erstgespräch / Mandat

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Triage-Fragen Bank-/Kapitalmarktrecht — Sofort-Checkliste

Bevor losgelegt wird, klaere folgende Punkte:
1. Ist eine Sofortfrist (Widerruf, Klage, Beschwerde) erkennbar? → Datum notieren, Kalender Alarm.
2. Liegt Verbraucherkredit (§ 491 BGB) oder gewerbliches Mandat vor? → Bestimmt Schutzrechte.
3. Besteht Identitaetsklaerungspflicht nach GwG (wirtschaftlich Berechtigter, PEP-Pruefung)?
4. Existiert ein Interessenkonflikt (§ 43a Abs. 4 BRAO)? → Gegner, Sachzusammenhang, frueheres Mandat.
5. Ist der Streitwert so hoch, dass Prozesskostenrisiko thematisiert werden muss?

### Output-Template Mandatsbogen (Vervollstaendigt)
**Adressat:** Intern, Aktenanlage — Tonfall: praezise-dokumentarisch

```
MANDATSBOGEN Bank-/Kapitalmarktrecht
===========================================
Datum Erstgespraech: [TT.MM.JJJJ]
Mandant (Name/Geb./ADR): [NAME] / [DATUM] / [ANSCHRIFT]
Rolle Mandant: [Anleger / Kreditnehmer / Bank / Sonstiges]
Gegenpartei: [NAME, ANSCHRIFT, ggf. Anwalt]
Sachgebiet: [Anlageberatung / Verbraucherkredit / Widerruf / BaFin ...]
Sachverhaltskern (5 Saetze):
[...]
Ziel Mandant (1 Satz): [...]
Sofortfristen: [Datum] — [Art] — [Rechtsgrundlage]
Verjaebrungsprognose: [3 Jahre ab XX.XX.XXXX / 10 Jahre absolut]
GwG-Identifizierung: [Lichtbildausweis] JA / NEIN; [HR-Auszug] JA / NEIN
Konflikt-Check: JA (sauber) / NEIN (Hinderungsgrund: ...)
Vollmacht: Unterschrieben am [Datum]
Streitwert (Schaetzung): EUR [Betrag]
Honorarvereinbarung: RVG / Stunde EUR [...] / Pauschale EUR [...]
Naechster Schritt: [Owner] bis [Datum]
===========================================
```

---

## Skill: `erstpruefung-und-mandatsziel`

_Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel._

# Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel


## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 Abs. 1 KWG` — Bankgeschaefte.
- `§ 32 Abs. 1 KWG` — Erlaubnispflicht.
- `§ 25a Abs. 1 KWG` — ordnungsgemaesse Geschäftsorganisation.
- `§ 44 Abs. 1 KWG` — Auskunfts- und Pruefungsrechte.
- `§ 1 Abs. 1 ZAG` — Zahlungsdienste.
- `§ 10 Abs. 1 ZAG` — Erlaubnis Zahlungsinstitut.
- `Art. 16 DORA` — vereinfachter IKT-Risikomanagementrahmen.
- `Art. 28 DORA` — IKT-Drittparteienrisiko.
- `§ 675f BGB` — Zahlungsdiensterahmenvertrag.
- `§ 765 BGB` — Bürgschaft.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; WpIG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.

## Spezialwissen: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel
- **Konkreter Gegenstand:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.
- **Normen-/Verfahrensanker:** KWG, ZAG, WpHG, WpIG, MAR, MiFID-II/MiFIR, MiCAR, BGB-Verbraucherkredit, AGB-Recht und BaFin-Verwaltungspraxis.
- **Entscheidende Weiche:** Produkt, Kundentyp, Aufklärung, Geeignetheit, Dokumentation, Erlaubnispflicht, Interessenkonflikt, Prospekt-/Ad-hoc-Risiko und Verjährung auseinanderziehen.
- **Arbeitsprodukt:** Erstelle eine fallbezogene Matrix `Behauptung / Norm / Beleg / Risiko / Gegenargument / nächster Schritt`; keine bloße Wiederholung des allgemeinen Plugin-Workflows.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Fachanwalt** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `output-waehlen`

_Output-Wahl für Fachanwalt Bank- und Kapitalmarktrecht: stimmt Adressat (Anleger/Kunde, Bank/WPI, BaFin), Frist (Widerrufsfrist Verbraucherdarlehen 14 Tage § 355 BGB) und Form auf den Zweck ab — typische Outputs: Klage Falschberatung, Widerruf Darlehensvertrag, BaFin-Beschwerde._

# Output wählen

## Einsatzlage

Diese Output-Weiche für **Fachanwalt Bank Kapitalmarktrecht** entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist.

## Fachlandkarte dieses Plugins

- `anlageberatung-fehlerhaft` — Anlageberatung Fehlerhaft Cybertrading
- `anlageberatungsfehler-pruefen` — Anlageberatungsfehler Bankrecht Akkreditiv
- `bankaufsicht-erlaubnis-und-vertrieb` — Bankaufsicht Erlaubnis Emissionsprospekt
- `bankrecht-buergschaft-aval-garantie-routing` — Bankrecht Buergschaft Aval Garantieabruf
- `bankrecht-privatbuergschaft-sittenwidrigkeit` — Bankrecht Privatbuergschaft Regress BK
- `bausparvertrag-zinsanpassung-bgh-xi-zr-78-22` — Bausparvertrag Zinsanpassung BGH XI ZR 78 22
- `beratungshaftung-zahlen-schwellen-und-berechnung` — Beratungshaftung Haftung Beweislast BK CUM
- `bk-bankenfehlberatung-grundzuege` — BK Bankenfehlberatung Grundzuege Einfuehrung
- `bk-mifid-suitability-spezial` — BK Mifid BK Prip Erstgespraech Mandatsannahme
- `cum-ex-beihilfe-bgh-1-str-519-20` — CUM EX Beihilfe BGH 1 STR 519 20
- `dispokredit-zinsanpassung-bgh-xi-zr-78-08` — Dispokredit Zinsanpassung BGH XI ZR 78 08
- `einstieg-schnelltriage-fallrouting` — FA Bank Kapitalmarkt BK Bafin Chronologie
- `workflow-fristen-und-risikoampel` — FA Bank Kapitalmarkt Fristen Risiko Mandant
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Ergebnistyp bestimmen: Schriftsatz an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen, Mandantenmemo, Risikobericht, Vertragsentwurf, Entscheidungsvorlage, Behörden-Stellungnahme — was braucht der Mandant wirklich?
- Pflichtformate festlegen: Tenor / Antrag / Begründung (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis); konkrete Norm-Pinpoints im Fachanwalt Bank Kapitalmarktrecht (KWG, WpHG, WpIG, ZAG) einarbeiten.
- Adressat-Klarheit: Sprache, Detailtiefe und juristische Vorbildung des Empfängers berücksichtigen; bei Mandant ohne Vorbildung Klartext-Zusammenfassung voranstellen.
- Beweis- und Anlagenstruktur planen (chronologisch, thematisch, K- und B-Anlagen); Bezugnahmen sauber kennzeichnen.
- Quellenfußnoten und Zitierweise sichern; offene Punkte und Annahmen explizit als solche kennzeichnen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `dokumente-intake`

_Dokumentenintake für Fachanwalt Bank- und Kapitalmarktrecht: sortiert Darlehensvertrag, Wertpapierorder, Beratungsprotokoll, prüft Datum, Absender, Frist und Beweiswert (Beratungsprotokoll, Geeignetheitsprüfung); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO._

# Dokumentenintake

## Aktenstart statt Formularstart

Wenn zu **Dokumente Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Fachanwalt Bank Kapitalmarktrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Einsatzlage

Dieser Dokumenten-Intake für **Fachanwalt Bank Kapitalmarktrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `anlageberatung-fehlerhaft` — Anlageberatung Fehlerhaft Cybertrading
- `anlageberatungsfehler-pruefen` — Anlageberatungsfehler Bankrecht Akkreditiv
- `bankaufsicht-erlaubnis-und-vertrieb` — Bankaufsicht Erlaubnis Emissionsprospekt
- `bankrecht-buergschaft-aval-garantie-routing` — Bankrecht Buergschaft Aval Garantieabruf
- `bankrecht-privatbuergschaft-sittenwidrigkeit` — Bankrecht Privatbuergschaft Regress BK
- `bausparvertrag-zinsanpassung-bgh-xi-zr-78-22` — Bausparvertrag Zinsanpassung BGH XI ZR 78 22
- `beratungshaftung-zahlen-schwellen-und-berechnung` — Beratungshaftung Haftung Beweislast BK CUM
- `bk-bankenfehlberatung-grundzuege` — BK Bankenfehlberatung Grundzuege Einfuehrung
- `bk-mifid-suitability-spezial` — BK Mifid BK Prip Erstgespraech Mandatsannahme
- `cum-ex-beihilfe-bgh-1-str-519-20` — CUM EX Beihilfe BGH 1 STR 519 20
- `dispokredit-zinsanpassung-bgh-xi-zr-78-08` — Dispokredit Zinsanpassung BGH XI ZR 78 08
- `einstieg-schnelltriage-fallrouting` — FA Bank Kapitalmarkt BK Bafin Chronologie
- `workflow-fristen-und-risikoampel` — FA Bank Kapitalmarkt Fristen Risiko Mandant
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Fachanwalt Bank Kapitalmarktrecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: KWG, WpHG, WpIG, ZAG — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `anschluss-routing`

_Anschluss-Routing für Fachanwalt Bank- und Kapitalmarktrecht: wählt den nächsten Spezial-Skill nach Engpass (Widerrufsfrist Verbraucherdarlehen 14 Tage § 355 BGB, Darlehensvertrag, Wertpapierorder, Beratungsprotokoll), dokumentiert Router-Entscheidung mit Begründung._

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Bank Kapitalmarktrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `anlageberatung-fehlerhaft` — Anlageberatung Fehlerhaft Cybertrading
- `anlageberatungsfehler-pruefen` — Anlageberatungsfehler Bankrecht Akkreditiv
- `bankaufsicht-erlaubnis-und-vertrieb` — Bankaufsicht Erlaubnis Emissionsprospekt
- `bankrecht-buergschaft-aval-garantie-routing` — Bankrecht Buergschaft Aval Garantieabruf
- `bankrecht-privatbuergschaft-sittenwidrigkeit` — Bankrecht Privatbuergschaft Regress BK
- `bausparvertrag-zinsanpassung-bgh-xi-zr-78-22` — Bausparvertrag Zinsanpassung BGH XI ZR 78 22
- `beratungshaftung-zahlen-schwellen-und-berechnung` — Beratungshaftung Haftung Beweislast BK CUM
- `bk-bankenfehlberatung-grundzuege` — BK Bankenfehlberatung Grundzuege Einfuehrung
- `bk-mifid-suitability-spezial` — BK Mifid BK Prip Erstgespraech Mandatsannahme
- `cum-ex-beihilfe-bgh-1-str-519-20` — CUM EX Beihilfe BGH 1 STR 519 20
- `dispokredit-zinsanpassung-bgh-xi-zr-78-08` — Dispokredit Zinsanpassung BGH XI ZR 78 08
- `einstieg-schnelltriage-fallrouting` — FA Bank Kapitalmarkt BK Bafin Chronologie
- `workflow-fristen-und-risikoampel` — FA Bank Kapitalmarkt Fristen Risiko Mandant
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Bank Kapitalmarktrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `bk-bankenfehlberatung-grundzuege`

_Bankenfehlberatungs-Anspruch in Grundzuegen: § 280 BGB, anlegergerechte Beratung, anlagegerechte Beratung, MiFID II Geeignetheit, Aufklaerung Provision (Kick-back): Bankenfehlberatungs-Anspruch in Grundzuegen: § 280 BGB, anlegergerechte Beratung, anlagegere..._

# Bankenfehlberatungs-Anspruch in Grundzuegen: § 280 BGB, anlegergerechte Beratung, anlagegerechte Beratung, MiFID II Geeignetheit, Aufklaerung Provision (Kick-back)


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; WpIG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Bankenfehlberatungs-Anspruch in Grundzuegen: § 280 BGB, anlegergerechte Beratung, anlagegerechte Beratung, MiFID II Geeignetheit, Aufklaerung Provision (Kick-back). Beweislastumkehr nach BGH XI ZR. Pruefraster für Mandant.

### BK: Bankenfehlberatung

## Spezialwissen: BK: Bankenfehlberatung
- **Normen-/Quellenanker:** BGB, II, BGH, XI, ZR, BK.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zuständige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

---

## Skill: `bk-emissionsprospekt-haftung-spezial`

_Spezialfall Emissionsprospekthaftung: WpPG, ProspektG, Verantwortliche, Gewaehrleistungserklaerung, fehlerhafte Angaben, Schaden, Kausalitaet: Spezialfall Emissionsprospekthaftung: WpPG, ProspektG, Verantwortliche, Gewaehrleistungserklaerung, fehlerhafte An..._

# Spezialfall Emissionsprospekthaftung: WpPG, ProspektG, Verantwortliche, Gewaehrleistungserklaerung, fehlerhafte Angaben, Schaden, Kausalitaet


## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 Abs. 1 KWG` — Bankgeschaefte.
- `§ 32 Abs. 1 KWG` — Erlaubnispflicht.
- `§ 25a Abs. 1 KWG` — ordnungsgemaesse Geschäftsorganisation.
- `§ 44 Abs. 1 KWG` — Auskunfts- und Pruefungsrechte.
- `§ 1 Abs. 1 ZAG` — Zahlungsdienste.
- `§ 10 Abs. 1 ZAG` — Erlaubnis Zahlungsinstitut.
- `Art. 16 DORA` — vereinfachter IKT-Risikomanagementrahmen.
- `Art. 28 DORA` — IKT-Drittparteienrisiko.
- `§ 675f BGB` — Zahlungsdiensterahmenvertrag.
- `§ 765 BGB` — Bürgschaft.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; WpIG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Spezialfall Emissionsprospekthaftung: WpPG, ProspektG, Verantwortliche, Gewaehrleistungserklaerung, fehlerhafte Angaben, Schaden, Kausalitaet. Klagewege, Kapitalanleger-Musterverfahrensgesetz KapMuG, Insolvenz des Emittenten. Pruefraster.

### BK: Prospekthaftung

## Spezialwissen: BK: Prospekthaftung
- **Normen-/Quellenanker:** WpPG, ProspektG, KapMuG, BK.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zuständige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

---

## Skill: `bk-mifid-suitability-spezial`

_Spezialfall MiFID II Geeignetheits- und Angemessenheitspruefung: Anlegerprofil, Ziele, Risikobereitschaft, Verlusttragfaehigkeit: Spezialfall MiFID II Geeignetheits- und Angemessenheitspruefung: Anlegerprofil, Ziele, Risikobereitschaft, Verlusttragfaehigkei..._

# Spezialfall MiFID II Geeignetheits- und Angemessenheitspruefung: Anlegerprofil, Ziele, Risikobereitschaft, Verlusttragfaehigkeit


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; WpIG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Spezialfall MiFID II Geeignetheits- und Angemessenheitspruefung: Anlegerprofil, Ziele, Risikobereitschaft, Verlusttragfaehigkeit. Pflichten bei Robo-Advisor, ESG-Praeferenzen seit August 2022. Dokumentation, Reklamation, Aufsichtsanfrage.

### BK: MiFID-Geeignetheit

## Spezialwissen: BK: MiFID-Geeignetheit
- **Normen-/Quellenanker:** II, ESG, BK.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zuständige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

---

## Skill: `anlageberatung-fehlerhaft`

_Fachanwalt Bank Kapitalmarktrecht Anlageberatung Fehlerhaft: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Bank Kapitalmarktrecht Anlageberatung Fehlerhaft: ordnet Normen, Nutzerangab..._

# Fachanwalt Bank Kapitalmarktrecht Anlageberatung Fehlerhaft: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; WpIG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt Bank Kapitalmarktrecht Anlageberatung Fehlerhaft: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung.

### Anlageberatung fehlerhaft

## Kaltstart-Rückfragen

1. Welches Anlageprodukt wurde empfohlen (Aktie, Anleihe, Zertifikat, geschlossener Fonds, Schiffsfonds, Immobilienfonds)?
2. Wann erfolgte die Beratung und wann wurde der Erwerb getätigt? Liegt eine Geeignetheitserklärung § 64 Abs. 4 WpHG (bis 02.01.2018: Beratungsprotokoll § 34 Abs. 2a WpHG aF) vor?
3. Welche Risikoklasse hat der Mandant in seinem WpHG-Bogen angegeben? Wurde Risikobereitschaft und Anlageziel erfragt?
4. Hat die Bank über Rückvergütungen (Kick-backs) oder Innenprovisionen aufgeklärt?
5. Wie hoch ist der eingetretene Schaden (Erwerbsschaden, entgangener Gewinn)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Anspruchsgrundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Anleger- und anlagegerechte Beratung — Pflicht zur vollständigen, richtigen und verständlichen Information.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Anspruchsgrundlage: §§ 280 Abs. 1, 311 Abs. 2 BGB i.V.m. Beratungsvertrag (Schadensersatz wegen Pflichtverletzung).
- Bei Vorsatz oder Sittenwidrigkeit zusätzlich § 826 BGB und § 31 BGB für Organhaftung.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Beweislast und Frist

- Anleger trägt Darlegungs- und Beweislast für Beratungsfehler und Schaden.
- Bank trägt Beweislast für rechtzeitige und ordnungsgemäße Aufklärung.
- Bei festgestellter Pflichtverletzung wird Ursächlichkeit für Anlageentscheidung vermutet (Vermutung aufklärungsrichtigen Verhaltens).
- Verjährung Regelfrist § 195 BGB drei Jahre ab Kenntnis Schaden und Schädiger; Höchstfrist zehn Jahre § 199 Abs. 3 Nr. 1 BGB ab Anspruchsentstehung.

## Prüfschema

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

```
1. Beratungssituation (Beratungsvertrag konkludent?)
2. Pflicht zu anleger- und anlagegerechter Beratung
3. Aufklaerungsmaengel identifizieren
 - Risikoaufklaerung
 - Rueckverguetung/Kick-back
 - Innenprovision >= 15%
 - Totalverlustrisiko (geschlossene Fonds)
4. Geeignetheitserklaerung § 64 Abs. 4 WpHG analysieren (bzw. § 34 Abs. 2a WpHG aF bis 02.01.2018)
5. Schaden berechnen (Erwerbsschaden + entgangener Gewinn)
6. Verjährung pruefen (3 Jahre Kenntnis / 10 Jahre Hoechstfrist)
```

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — fehlerhafte Anlageberatung ruegen und Schadensersatz fordern | Anspruchsschreiben nach Schreibvorlage unten |
| Variante A — Verjährung droht | Verjährungshemmung (Klage/Verhandlungsaufnahme) sofort; keine Aussergerichts-Zeit |
| Variante B — Bank zeigt Einigungsbereitschaft | Aussergerichtliche Einigung bevorzugen; schnellere Auszahlung |
| Variante C — Schadenshoehe unklar | Stufenklage oder Feststellungsklage als Alternative |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schreibvorlage Anspruchsschreiben

```
Sehr geehrte Damen und Herren,

namens und in Vollmacht unserer Mandantschaft machen wir Schadensersatz
wegen fehlerhafter Anlageberatung aus dem Beratungsvertrag vom [Datum]
und §§ 280 Abs. 1 311 Abs. 2 BGB geltend.

Unsere Mandantschaft erwarb am [Datum] auf Empfehlung Ihres Hauses das
Anlageprodukt [Produktbezeichnung WKN/ISIN] zu einem Erwerbspreis von
EUR [Betrag].

Beratungsfehler liegen in folgenden Punkten:
1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 510/07 Beschl. v. 20.01.2009 Rn. 12 ff.)
2. unterlassene Aufklaerung ueber Innenprovision von [...] Prozent
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. anlegerunabhaengige Empfehlung trotz Risikoklasse [...]

Wir fordern Sie auf bis [Datum vier Wochen] Zug um Zug gegen Rueckgabe
der Wertpapiere den Erwerbspreis EUR [Betrag] zuzueglich entgangener
Gewinn in Hoehe von EUR [Betrag] zu erstatten.

Andernfalls werden wir Klage erheben.

Mit freundlichen Gruessen
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Übergabe

- Bei Ablehnung: Klage am Sitz der Bank bzw. Wohnsitz des Anlegers § 32b ZPO bei kapitalanlegerrechtlichem Musterverfahren prüfen.
- Verjährungsfrist im Aktenkalender notieren — Hemmung durch Verhandlungen § 203 BGB sichern.
- Bei Vergleichsverhandlungen Hemmungsschriftverkehr dokumentieren.

## Vertiefung: Leitsaetze und Workflow-Ergaenzung

### Triage — Bevor losgelegt wird, klaere:

1. Wann fand die Beratung statt? → Verjaebrung 3 Jahre ab Kenntnis + max. 10 Jahre absolut.
2. Liegt Beratungsprotokoll (§ 83 WpHG / § 34 WpHG aF) oder Geeignetheitserklaerung (§ 64 WpHG) vor? → Fehlende Dokumentation = Beweisschwaeche Bank.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
5. Schadenshoehe: Differenzhypothese oder negatives Interesse berechnen?

### Ergaenzende Leitsaetze
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Schritt-für-Schritt-Anlageberatungsfehler
1. **Mandantengespräch:** Produkt, Datum Beratung, Risikoprofil, Verlusthoehe dokumentieren.
2. **Beratungsprotokoll anfordern** (§ 83 WpHG, § 64 Abs. 4 WpHG): 3-Tage-Frist auf Herausgabe.
3. **Pruefung Kickbacks:** Bank-interne Vertriebsprovision vom Emittenten = aufklaerungspflichtig.
4. **Schadensberechnung:** Eingesetztes Kapital minus aktueller Wert + entgangene 4 %-Verzinsung.
5. **Ausforderungsschreiben** an Bank mit 4-Wochen-Frist, Schadensaufstellung, Klageandrohung.
6. **Ombudsmann** einschalten (hemmt Verjaebrung § 204 BGB).
7. **Klage** bei Ablehnung: LG (§ 23 GVG Streitwert ab EUR 5.000).

---

## Skill: `anlageberatungsfehler-pruefen`

_Anlageberatungsfehler Pruefen: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Anlageberatungsfehler Pruefen: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer..._

# Anlageberatungsfehler Pruefen: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; WpIG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Anlageberatungsfehler Pruefen: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung.

### Anlageberatungsfehler prüfen

## Mandantenfragen — Kaltstart

1. **Wann fand das Beratungsgespräch statt?** — Verjährung 3 Jahre ab Kenntnis (§ 199 Abs. 1 BGB) + max. 10 Jahre § 199 Abs. 3 BGB; Verjährung ist häufigster Ablehnungsgrund.
2. **Welches Produkt wurde empfohlen?** — Fondsanteile, Zertifikate, geschlossener Fonds, Swap, ETF; bestimmt Haftungsgrundlage.
3. **Liegt ein Beratungsprotokoll vor?** — MiFID-II Pflicht seit 2018 (§ 83 WpHG); fehlende Protokoll-Übersendung = Beweisschwäche Bank.
4. **Welches Risikoprofil wurde erhoben?** — Anlegergerechte Beratung verlangt Abgleich Risikoprofil mit Produkteinstufung.
5. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
6. **Wie hoch ist der tatsächliche Verlust?** — Eingesetztes Kapital minus aktueller Wert; Differenzhypothese oder negatives Interesse.
7. **Liegt die Schaden-Realisierung erst in jüngster Zeit vor?** — Verjährungsfrist beginnt mit grober Kenntnis, nicht mit objektivem Eintritt.
8. **Hat die Bank eine Stellungnahme oder Kulanz-Angebot gemacht?** — Verhandlungsposition einschätzen; Verjährungshemmung bei Verhandlungen § 203 BGB.

## Rechtlicher Rahmen

### Primärnormen

| Norm | Inhalt |
|---|---|
| § 280 Abs. 1 BGB | Schadensersatz aus Pflichtverletzung des Beratungsvertrags |
| § 311 Abs. 2 BGB | c.i.c.: Pflichten aus vorvertraglichem Verhältnis |
| § 241 Abs. 2 BGB | Rücksichtnahmepflichten |
| § 249 BGB | Differenzhypothese: Schaden = Differenz hypothetischer Verlauf ohne Pflichtverletzung |
| § 254 BGB | Mitverschulden: Eigenverantwortung des Anlegers |
| §§ 195, 199 BGB | Verjährung: 3 Jahre ab Kenntnis / 10 Jahre absolut |
| § 63 WpHG | Angemessenheitsprüfung (execution only) |
| § 64 WpHG | Geeignetheitsprüfung (Beratung): Kunde, Anlageziele, finanzielle Situation, Kenntnisse |
| § 83 WpHG | Beratungsprotokoll-Pflicht |

Die zentrale Linie der BGH-Rspr. (XI. ZS) ist die Pflicht zur anlegergerechten und anlagegerechten Beratung (st. Rspr. seit "Bond" — konkrete Aktenzeichen, Datum und Randnummer vor Versand in juris.bundesgerichtshof.de oder dejure.org verifizieren).

Das Fundament aller Beratungshaftungs-Fälle:

**Anlegergerecht** bedeutet:
- Wissensstand (Erfahrungen mit Finanzprodukten)
- Risikobereitschaft (Risikoklasse)
- Anlageziele (Altersvorsorge, Kapitalerhalt, Rendite, Liquidität)
- Finanzielle Verhältnisse (Vermögen, Verbindlichkeiten, Einkommen)

**Anlagegerecht** bedeutet:
- Funktionsweise des Produkts
- Risiken (Kapitalverlust, Rendite, Wechselkurs, Liquidität, Emittent)
- Kostenstruktur (Ausgabeaufschlag, laufende Kosten, Performance-Fee)
- Steuerliche Wirkung

Kick-back-/Provisionsoffenlegungspflicht ist st. Rspr. des XI. ZS des BGH (Aktenzeichen, Datum und Randnummer vor Versand in offener Quelle verifizieren):

- Bank muss über **alle Vertriebsvergütungen** aufklären, die sie vom Emittenten/Produktanbieter erhält
- Aufklärung muss vor Investition erfolgen
- Konkret-individualisierte Offenlegung (nicht nur abstrakt)
- Eigeninteresse der Bank begründet Interessenkonflikt → aufklärungsbedürftig

### Leitentscheidungen (Stand Mai 2026)

Vor Versand jeweils Volltext in offener Quelle (juris.bundesgerichtshof.de, dejure.org, openjur.de, curia.europa.eu) aufrufen:

| Gericht | Aktenzeichen | Datum | Kernaussage | Offene Quelle |
|---|---|---|---|---|
| BGH XI. ZS | XI ZR 22/24 | 20.5.2025 | Verbraucherdarlehen Immobilien: AGB-Klausel zur Vorfälligkeitsentschädigung muss Berechnung transparent darstellen; intransparente Klausel führt zum Verlust des Anspruchs auf Vorfälligkeitsentschädigung | juris.bundesgerichtshof.de |
| BGH XI. ZS | XI ZR 133/24 | 21.10.2025 | Referenzzins für Zinsanpassungen in Prämiensparverträgen (Folgeentscheidung) | bundesgerichtshof.de PM Nr. 225/2025 |
| BGH XI. ZS | XI ZR 553/19 | 2024 | Stärkung der Rechte von Darlehensnehmern bei Altforderungen — Volltext und Datum vor Versand verifizieren | juris.bundesgerichtshof.de |

Hinweis: Es gibt keine Praejudizienbindung im deutschen Recht (Ausnahme § 31 BVerfGG). BGH-Linien werden zitiert als Auslegungshilfe, nicht als verbindliches Recht.

## Prüfschema Anlageberatungsfehler

| Schritt | Prüfpunkt | Norm | Risiko bei Fehler |
|---|---|---|---|
| 1 | Beratungsvertrag (konkludent oder schriftlich)? | § 280 BGB | Ohne Vertrag nur c.i.c. |
| 2 | Risikoprofil erhoben und dokumentiert? | § 64 WpHG | Bank-Gegenbeweis möglich |
| 3 | Anlegergerecht (Wissensstand, Risikobereitschaft, Anlageziel, Finanzlage)? | § 64 WpHG; st. Rspr. BGH XI. ZS | Pflichtverletzung |
| 4 | Anlagegerecht (Produktstruktur, Risiken, Kosten)? | § 64 WpHG; st. Rspr. BGH XI. ZS | Pflichtverletzung |
| 5 | Kick-back-/Vertriebsvergütung aufgeklärt? | st. Rspr. BGH XI. ZS (Aktenzeichen vor Versand verifizieren) | Aufklärungsfehler |
| 6 | Beratungsprotokoll erstellt und übergeben? | § 83 WpHG | Beweisschwäche Bank |
| 7 | Kausalitäts-Vermutung "Verhalten gegen guten Rat"? | st. Rspr. BGH XI. ZS (Aktenzeichen vor Versand verifizieren) | Bank-Gegenbeweis nötig |
| 8 | Schadenshöhe berechnet? | § 249 BGB | Klageinhalt |
| 9 | Mitverschulden § 254 BGB? | § 254 BGB | Quotelung des Schadensersatzes |
| 10 | Verjährung geprüft? | §§ 195, 199 BGB | Klage abgewiesen bei Verjährung |

## Beweislast und Darlegungslast

| Thema | Beweislast |
|---|---|
| Inhalt des Beratungsgesprächs | Bank (MiFID-II Protokoll; bei fehlendem Protokoll: Vermutung zu Lasten Bank) |
| Risikoprofil-Erhebung | Bank |
| Aufklärung über Kickbacks | Bank |
| Kausalitäts-Vermutung "Verhalten gegen guten Rat" | st. Rspr. BGH XI. ZS — Vermutung beweisbeladenes Verhalten; Bank muss Gegenbeweis führen |
| Schadenshöhe | Anleger (§ 287 ZPO: Schätzung zulässig) |
| Mitverschulden | Bank |
| Verjährung | Bank |

## Schadensberechnung

### Methode 1 — Differenzhypothese (§ 249 BGB)

```
Schaden = Vermögenslage mit Pflichtverletzung
 ./. Vermögenslage ohne Pflichtverletzung

Konkret:
Eingesetztes Kapital inkl. Ausgabeaufschlag: EUR [Betrag]
Aktueller Rücknahme-/Verkaufswert: ./. EUR [Betrag]
Entgangene Alternativrendite: ./. EUR [4% × Betrag × Jahre]
Gezahlter Ausgabeaufschlag / Kosten: + EUR [Betrag]
Schadensumme: EUR [Netto]
```

### Methode 2 — Negatives Interesse (Rückabwicklung)

```
Anleger gibt Anlage-Gegenstand zurück
und erhält:
- Eingesetztes Kapital zurück
- Entgangene Alternativrendite (typisch 4 % p.a. — konkret darzulegen
 durch alternative Anlageform; nicht aus Modellwissen pauschalisieren,
 sondern Vergleichsanlage nachvollziehbar belegen)
- Anwaltskosten aus Verzug
```

### Typische Schadenspositionen

| Position | Berechnungsgrundlage |
|---|---|
| Kursverlust | Kaufkurs ./. aktueller Kurs × Stückzahl |
| Ausgabeaufschlag | Direkt aus Abrechnung |
| Entgangene Alternativrendite | Marktübliche Alternative (z.B. Bundesanleihe, Tagesgeld); konkrete Vergleichsanlage darlegen, nicht pauschal annehmen |
| Wertpapierkredit-Zinsen | Wenn kreditfinanziert + Zinsbelastung |
| Anwaltskosten | § 249 BGB als Verzugsschaden |

## Spezialthemen

### Geschlossene Fonds (Schiffsfonds, Filmfonds, Windkraftfonds)

- Prospekthaftung im engeren Sinne: §§ 9 VermAnlG, 21 WpPG
- Prospekthaftung im weiteren Sinne nach BGB: Verletzung von Aufklärungspflichten
- Linie der BGH-Rspr. (II./XI./III. Senate je nach Konstellation): konkrete Aktenzeichen, Datum, Randnummer vor Versand in offener Quelle verifizieren

### Lehman / Zertifikate-Linie

- Aufklärungspflicht über Emittentenrisiko war obligatorisch
- Rating allein genügte nicht
- "Investment-Grade" schließt Aufklärungspflicht nicht aus
- Aktenzeichen XI. ZS BGH vor Versand verifizieren

### Swap-Linie (CMS Spread Ladder)

- Aufklärungspflicht über anfänglichen negativen Marktwert (strukturierter Nachteil für Kunden)
- Eigeninteresse der Bank offenzulegen
- Wert der Information für Anleger: erheblich
- Aktenzeichen XI. ZS BGH vor Versand verifizieren

## Außergerichtliche Vorgehensweise

### Schritt 1 — Außergerichtliches Schreiben

```
[Kanzlei] [Ort, Datum]

[Bank / Vermögensverwalter]
[Anschrift]

Anlageberatungsfehler — Schadensersatz gemäss § 280 BGB

Sehr geehrte Damen und Herren,

namens und in Vollmacht meiner Mandantschaft mache ich
Schadensersatzansprüche wegen Verletzung von Beratungs-
pflichten aus dem Beratungsgespräch vom [Datum] geltend.

Beratungsfehler:
1. [Keine anlegergerechte Beratung: Risikoprofil
 konservativ, empfohlenes Produkt hochriskant]
2. [Keine Aufklärung über Rückvergütungen in Höhe von
 EUR [Betrag] (ca. [x] % des Anlagevolumens)]
3. [Unzureichende Risikoaufklärung bzgl. Totalverlust]

Schadenshöhe:
Investiertes Kapital: EUR [Betrag]
Aktueller Wert: ./. EUR [Betrag]
Entgangene Rendite: ./. EUR [4% × Betrag × Jahre]
Gesamtschaden: EUR [Summe]

Ich fordere Sie auf, den Schaden bis zum [Datum + 4 Wochen]
zu erstatten. Anderenfalls erhebe ich Klage.

[Rechtsanwalt/-anwaeltin, Fachanwalt für Bank- und
Kapitalmarktrecht]
```

## Verjährung

| Fristtyp | Dauer | Beginn | Rechtsgrundlage |
|---|---|---|---|
| Regelfrist | 3 Jahre | 31.12. des Jahres der Kenntnis | §§ 195, 199 Abs. 1 BGB |
| Absolute Höchstfrist | 10 Jahre | Beratungszeitpunkt | § 199 Abs. 3 Nr. 1 BGB |
| Hemmung durch Verhandlungen | Bis Ende der Verhandlungen | Beginn Verhandlung | § 203 BGB |
| Hemmung durch Klage | Bis Rechtskraft | Klageeingang | § 204 BGB |

**Kenntnis**: grobe Kenntnis der anspruchsbegründenden Umstände; bei Spezialwissen der Bank: späterer Fristbeginn möglich.

## Streitwert und Kosten

- **Streitwert**: Schadensumme + entgangene Zinsen = klageweiser Gesamtanspruch.
- **LG-Zuständigkeit**: ab 5.000 EUR Streitwert § 23 GVG; Bankrecht-Fälle fast immer LG.
- **Kostenrisiko**: Bei 100.000 EUR Streitwert: ca. 7.000 EUR Gerichtsgebühren (3 Instanzen); Anwalt nach RVG.
- **Ombudsstelle**: kostenfrei, hemmt Verjährung; Empfehlung als erste Stufe wenn Bank ggf. verhandlungsbereit.

## Anschluss-Skills

- `widerrufsjoker-immobiliendarlehen` — bei kombinierten Darlehens- und Beratungsfehlern
- `fachanwalt-bank-kapitalmarktrecht-cybertrading-anlagebetrug` — bei betrügerischen Plattformen
- `fachanwalt-bank-kapitalmarktrecht-kreditkuendigung-490-bgb` — bei Kreditkündigung nach Verlust

## Quellen (Stand Mai 2026)

- BGB §§ 195, 199, 249, 254, 280, 311
- WpHG §§ 63, 64, 83
- VermAnlG § 9; WpPG § 21
- MiFID-II Richtlinie 2014/65/EU
- PRIIPs-VO (EU) Nr. 1286/2014 — KID-Pflicht für verpackte Anlageprodukte
- Aktuelle Aktenzeichen (Volltext jeweils vor Versand prüfen in juris.bundesgerichtshof.de, dejure.org, openjur.de, curia.europa.eu):
 - BGH XI ZR 22/24, Urt. v. 20.5.2025 — Vorfälligkeitsentschädigung intransparente AGB
 - BGH XI ZR 133/24, Urt. v. 21.10.2025 — Referenzzins Prämiensparvertrag
 - LG Nürnberg-Fürth, Urt. v. 21.2.2025 — PRIIPs-KID Gesamtrisikoindikator bei offenem Immobilienfonds (nicht rechtskräftig; instanzgerichtlich)
- Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; nicht aus Modellwissen.

<!-- AUDIT 27.05.2026 bundle_021
-->

---

## Skill: `bankaufsicht-erlaubnis-und-vertrieb`

_Bankaufsichtliche Erlaubnis-, Vertriebs- und Organisationsrisiken: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output: Bankaufsichtliche Erlaubnis-, Vertriebs- und Organisationsrisiken: führt s..._

# Bankaufsichtliche Erlaubnis-, Vertriebs- und Organisationsrisiken: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output.


## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 Abs. 1 KWG` — Bankgeschaefte.
- `§ 32 Abs. 1 KWG` — Erlaubnispflicht.
- `§ 25a Abs. 1 KWG` — ordnungsgemaesse Geschäftsorganisation.
- `§ 44 Abs. 1 KWG` — Auskunfts- und Pruefungsrechte.
- `§ 1 Abs. 1 ZAG` — Zahlungsdienste.
- `§ 10 Abs. 1 ZAG` — Erlaubnis Zahlungsinstitut.
- `Art. 16 DORA` — vereinfachter IKT-Risikomanagementrahmen.
- `Art. 28 DORA` — IKT-Drittparteienrisiko.
- `§ 675f BGB` — Zahlungsdiensterahmenvertrag.
- `§ 765 BGB` — Bürgschaft.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; WpIG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Bankaufsichtliche Erlaubnis-, Vertriebs- und Organisationsrisiken: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output.

### Bankaufsichtliche Erlaubnis-, Vertriebs- und Organisationsrisiken

## Einstieg
Wenn Material vorliegt, nutze es zuerst. Frage nur nach, was für die nächste Entscheidung fehlt:

1. Wer handelt in welcher Rolle und gegen wen?
2. Welches praktische Ziel soll erreicht werden?
3. Welche Fristen, Termine, Zustellungen, Schwellenwerte oder Sanktionen stehen im Raum?
4. Welche Unterlagen, Daten, Registerauszüge, Bescheide, Verträge, Screenshots oder sonstigen Belege liegen vor?
5. Soll der Output intern, für Mandantschaft, Behörde, Gericht, Gegnerseite oder Gremium formuliert werden?

## Arbeitsworkflow
1. **Sortieren:** Sachverhalt, Dokumente und offene Punkte in eine knappe Fallmatrix bringen.
2. **Rechtsrahmen:** Einschlägige Normen, Zuständigkeiten, Verfahren, Fristen und formelle Anforderungen live prüfen, soweit Aktualität tragend ist.
3. **Materielle Weichen:** Die Kernfragen zu **Bankaufsichtliche Erlaubnis-, Vertriebs- und Organisationsrisiken** mit Tatbestandsmerkmalen, Belegen, Gegenargumenten und typischen Praxisfehlern abarbeiten.
4. **Risikoampel:** Ergebnis in Grün/Gelb/Rot mit Begründung, Unsicherheiten und Beweisbedarf einordnen.
5. **Anschluss:** Passende weitere Skills desselben Plugins vorschlagen, wenn Spezialprüfung, Schriftsatz, Tabelle, Brief oder Verhandlungsstrategie sinnvoll ist.

## Aufsichtsrechtlicher Präzisionskern

Wenn Zahlungsdienst, Cloud/IKT, Organanzeige, Beteiligungserwerb oder Kapitalfolge betroffen ist, den Skill `bk-aufsicht-zag-dora-inhkontrolle-crr-arbeitskern` zuschalten. Er trennt ZAG-Erlaubnis/Ausnahmen, DORA Artikel 16 und Art. 28 bis 30, KWG-Anzeigen nach AnzV, Inhaberkontrolle und CRR-Folgen. In Mandaten immer zweigleisig formulieren: gegenüber Aufsicht kooperativ und vollständig, gegenüber Gegner/Gericht beweis- und haftungsbewusst ohne unnötige Selbstbezichtigung.

---

## Skill: `bankrecht-buergschaft-auf-erste-anforderung`

_Bürgschaft oder Bankgarantie auf erste Anforderung im Mandat prüfen: Zahlungsmechanik, Einwendungen, offensichtlicher Missbrauch, einstweiliger Rechtsschutz, Rückforderung und Regress: Bürgschaft oder Bankgarantie auf erste Anforderung im Mandat prüfen: Za..._

# Bürgschaft oder Bankgarantie auf erste Anforderung im Mandat prüfen: Zahlungsmechanik, Einwendungen, offensichtlicher Missbrauch, einstweiliger Rechtsschutz, Rückforderung und Regress.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; WpIG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Bürgschaft oder Bankgarantie auf erste Anforderung im Mandat prüfen: Zahlungsmechanik, Einwendungen, offensichtlicher Missbrauch, einstweiliger Rechtsschutz, Rückforderung und Regress.

### Bürgschaft auf erste Anforderung

## Prüfaufbau

1. **Dokumenttyp:** Bürgschaft, Garantie, Schuldversprechen, Standby LC oder unklarer Mischtext.
2. **Erstes Anfordern:** ausdrücklich vereinbart oder nur behauptet?
3. **Abrufformalien:** Frist, Person, Betrag, Erklärung, Dokumente, Original.
4. **Einwendungen:** formale Mängel, fehlende Vertretung, Laufzeit, Betrag, evidenter Missbrauch.
5. **Eilrechtsschutz:** wer muss gegen wen was beantragen?
6. **Nachprozess:** Rückforderung, Regress, Schadensersatz, Vergleich.

## Normen und Belege

- §§ 765 ff. BGB bei Bürgschaft.
- §§ 780, 781 BGB bei selbständigem Zahlungsversprechen.
- §§ 305 ff. BGB bei Formulartexten.
- § 242 BGB für Missbrauchseinwand.
- ZPO für einstweilige Verfügung und Vollziehung.

Rechtsprechung nur nach Live-Check mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier Quelle verwenden. Keine BeckRS-/Juris-Blindzitate.

## Ergebnis

Liefere:

- Zahlungs-/Abwehrampel.
- Fristenplan.
- Entwurf an Bank/Begünstigten/Kunden.
- Eilantrags-Skizze.
- Beweismatrix.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 82 DSGVO
- § 64 WpHG
- § 263 StGB
- § 4b FinDAG
- § 31 BDSG
- § 44 KWG
- § 10 ZAG
- § 1 KWG
- § 32 KWG
- § 25a KWG
- § 1 ZAG
- Art. 22 DSGVO

### Leitentscheidungen

- BGH XI ZR 22/24
- BGH XI ZR 133/24
- EuGH C-26/22
- EuGH C-634/21
- BGH VI ZR 183/22

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

