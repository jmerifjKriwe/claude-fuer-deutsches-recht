# AGB-Recht-Prüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`agb-recht-pruefer`) | [`agb-recht-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/agb-recht-pruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **BGB BT — Smart-Kühlschrank, digitale Elemente und Reparaturblockade** (`bgb-bt-smart-kuehlschrank-digital-repair-koeln`) | [Gesamt-PDF lesen](../testakten/bgb-bt-smart-kuehlschrank-digital-repair-koeln/gesamt-pdf/bgb-bt-smart-kuehlschrank-digital-repair-koeln_gesamt.pdf) | [`testakte-bgb-bt-smart-kuehlschrank-digital-repair-koeln.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bgb-bt-smart-kuehlschrank-digital-repair-koeln.zip) |
| **Akte Nordstern MedTech Vertrieb - Provision, Buchauszug und Ausgleich** (`handelsvertreterrecht-provisionsausgleich-nordstern-medtech`) | [Gesamt-PDF lesen](../testakten/handelsvertreterrecht-provisionsausgleich-nordstern-medtech/gesamt-pdf/handelsvertreterrecht-provisionsausgleich-nordstern-medtech_gesamt.pdf) | [`testakte-handelsvertreterrecht-provisionsausgleich-nordstern-medtech.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-handelsvertreterrecht-provisionsausgleich-nordstern-medtech.zip) |
| **Akte Vellbruck Robotics GmbH — Roboterflotte AtlasCare / LumaMove / Werkbank C7** (`robotikrecht-roboterflotte-vellbruck-muenchen`) | [Gesamt-PDF lesen](../testakten/robotikrecht-roboterflotte-vellbruck-muenchen/gesamt-pdf/robotikrecht-roboterflotte-vellbruck-muenchen_gesamt.pdf) | [`testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Gigantisches Plugin für deutsches AGB-Recht: Prüfen, Entwerfen, Redlinen, Verhandeln, Rollout und Streitverteidigung von Allgemeinen Geschäftsbedingungen in allen praktischen Varianten.

Das Plugin ist bewusst zweigleisig gebaut:

- **AGB prüfen:** Klauseln zerlegen, Einbeziehung und Transparenz prüfen, §§ 305 bis 310 BGB sauber anwenden, Risiko bewerten, bessere Fassung vorschlagen.
- **AGB entwerfen:** Geschäftsmodell verstehen, Klauselfamilien auswählen, sichere oder bewusst risikobehaftete Fassungen erzeugen, Rollout und Nachweisfähigkeit mitdenken.

## Start

```text
/agb-recht-prüfer:allgemein
```

Der Einstieg fragt zürst nicht zwanzig Dinge ab, sondern klärt die wichtigste Weiche: **prüfen oder entwerfen?** Danach routet er in passende Spezialskills, etwa Verbraucher-AGB, B2B-AGB, Online-Checkout, Preisanpassung, Haftung, Laufzeit, UKlaG, Redline oder konkrete Branchenbedingungen.

## Arbeitsweise

1. Klausel und Vertragstyp erfassen.
2. AGB-Eigenschaft und Einbeziehung prüfen.
3. Überraschung, Mehrdeutigkeit und Transparenz klären.
4. Inhaltskontrolle nach §§ 307 bis 309 BGB und Besonderheiten nach § 310 BGB.
5. Rechtsfolge, Rückabwicklung, UKlaG-/Prozessrisiko prüfen.
6. Bessere Klausel entwerfen: sicher, balanced oder aggressiv mit Warnlabel.
7. Rollout, Versionierung, Nachweisbarkeit und Fachbereichskommunikation erledigen.

## Live-Quellen

Das Plugin soll bei tragenden Aussagen immer die aktülle amtliche Fassung auf **Gesetze im Internet** prüfen, insbesondere BGB §§ 305 bis 310 und UKlaG. Siehe [`references/QUELLEN.md`](./references/QUELLEN.md).

## Typische Ergebnisse

| Bedarf | Ergebnis |
| --- | --- |
| Fremde AGB schnell prüfen | Klauselampel, Risikobegründung, Redline-Kommentar |
| Eigene AGB neu entwerfen | Klauselarchitektur, sichere Fassungen, Fallbacks |
| B2C-Rollout vorbereiten | Checkout-/Einbeziehungscheck, Versionierung, Kundenkommunikation |
| B2B-Verhandlung führen | Playbook mit Must-have, Fallback, No-Go und Argumenten |
| Abmahnung erhalten | Fristenscan, UKlaG-Risiko, modifizierte Unterlassungserklärung |
| Management informieren | kurze Legal Note mit Risiko, Optionen und Empfehlung |

## Enthaltene Skills

Die vollständige Skill-Liste wird automatisch am Ende dieser README aktualisiert.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 283 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abmahnung-reagieren` | Output- und Streit-Skill für Abmahnung Reagieren: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `abnahme-testing` | Klausel-Spezialskill für Abnahme Testing: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `abtretung` | Klausel-Spezialskill für Abtretung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `abtretung-adversarial-test-aenderungsvorbehalt` | Abtretung, Adversarial Test Agb, Aenderungsvorbehalt 308, Agb Arbeitnehmerueberlassung Aueg: Abtretung; Adversarial Test Agb; Aenderungsvorbehalt 308; Agb Arbeitnehmerueberlassung Aueg. Führt Intake, Prüfroutine, Normen-/Quellenradar, Be... |
| `adversarial-test-agb` | Output- und Streit-Skill für Adversarial Test AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `aenderungsvorbehalt-308` | Norm- und Dogmatik-Skill für Änderungsvorbehalt 308: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `agb-anwaltsvertrag-und-allg-mandatsbedingungen` | AGB im Anwaltsvertrag und Allgemeine Mandatsbedingungen. Skill klaert die AGB-rechtliche Pruefung typischer Mandatsbedingungen Verguetungsklauseln Verzugsregelungen Verschwiegenheit Auflagen RVG-konforme Honorarvereinbarungen und Sonderv... |
| `agb-arbeitnehmerueberlassung-aueg` | AGB bei Arbeitnehmerueberlassung (AUeG). Skill klaert die AGB-rechtliche Pruefung der Standardvertraege zwischen Verleiher Entleiher und Leiharbeitnehmer Equal-Pay-Klauseln Branchenzuschlaege Verleihbarkeitsausschluss Vertragsstrafe bei... |
| `agb-begriff-vorformuliert-305` | Norm- und Dogmatik-Skill für AGB Begriff Vorformuliert 305: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `agb-bei-digitalen-produkten-327f-update` | AGB bei digitalen Produkten und § 327f BGB Update-Pflicht. Skill vertieft die AGB-rechtliche Behandlung von Update-Klauseln Aktualisierungspflichten Funktionsanpassungen sowie das Verhaeltnis zur Hauptleistungspflicht. Aktuelle BGH-Folge... |
| `agb-bei-iso-vertraegen-international` | AGB bei internationalen ISO-Vertraegen. Skill behandelt die AGB-rechtliche Pruefung internationaler Vertragsmuster ICC FIDIC ISDA AIA und ihre Anpassung an deutsches Recht. Klaert die Wechselwirkung mit Rom-I und ordre public. Behandelt... |
| `agb-bei-kreditvertraegen-verbraucherdarlehen` | AGB bei Verbraucherdarlehensvertraegen. Skill behandelt AGB im Kontext der §§ 491 ff. BGB Vorvertragliche Information Widerrufsrecht effektiver Jahreszins Sondervorschriften zu Restschuldversicherung Bearbeitungsentgelt Bearbeitungsgebue... |
| `agb-bei-plattformnutzung-app-stores` | AGB bei Plattformnutzung App Stores Apple Google Steam Amazon. Skill klaert die AGB-rechtlichen Kontrollfaktoren der Standardvertraege Marktstellung und Marktmacht (Art. 102 AEUV) sowie das Verhaeltnis zur P2B-Verordnung. Behandelt aktue... |
| `agb-bei-vereinen-und-verbaenden` | AGB bei Vereinen und Verbaenden. Skill klaert die AGB-rechtliche Pruefung von Vereinsbeitrittsbedingungen Beitragsregelungen Ausschlussklauseln und Vereinsstrafen. Behandelt das Spannungsverhaeltnis zwischen Vereinsautonomie (Art. 9 GG)... |
| `agb-bei-versicherungsvertraegen-vvg` | AGB-Kontrolle bei Versicherungsvertraegen (VVG). Skill behandelt das Spannungsverhaeltnis zwischen den Allgemeinen Versicherungsbedingungen (AVB) und § 307 BGB. Klaert das Transparenzgebot Risikoausschluesse Obliegenheitsverletzungen San... |
| `agb-entwurf-kaltstart` | Einstiegs- und Workflow-Skill für AGB Entwurf Kaltstart: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `agb-fuer-vereinsausschluss-und-haftung` | AGB-Klauseln zum Vereinsausschluss und zur Haftung im Verein. Skill klaert die AGB-rechtliche Pruefung von Ausschlussklauseln in Vereinssatzungen und Beitrittsformularen das Verhaeltnis zur Vereinsautonomie und das gerichtliche Pruefrast... |
| `agb-haftung-erfuellungsgehilfen` | AGB-Haftung fuer Erfuellungsgehilfen. Skill klaert die AGB-rechtliche Behandlung von Haftungsausschluessen fuer Erfuellungsgehilfen (§ 278 BGB) und die Wechselwirkung mit § 309 Nr. 7 BGB. Behandelt die BGH-Linie zur unwirksamen Pauschalf... |
| `agb-im-arbeitsvertrag-310-abs-4-vertieft` | Arbeitsvertrags-AGB nach § 310 Abs. 4 BGB. Skill vertieft die AGB-Kontrolle im Arbeitsrecht: Anwendbarkeit der §§ 305 ff. BGB auf vorformulierte Arbeitsvertragsklauseln Sonderregeln fuer Tarifvertraege und Betriebsvereinbarungen. Behande... |
| `agb-im-bankvertrag-sparkassen-und-banken` | AGB-Kontrolle im Bankvertrag. Skill behandelt die Banken-AGB Sparkassen-AGB und Allgemeinen Geschaeftsbedingungen der Volks- und Raiffeisenbanken Klauseln zu Entgelten Aenderungen einseitige Vertragsanpassung BGH-Linie zu Gebuehrenklause... |
| `agb-im-bauvertrag-vob-b-2024` | AGB-Kontrolle der VOB-B im Bauvertrag. Skill klaert die BGH-Linie zur AGB-rechtlichen Behandlung der VOB-B insgesamt und einzelner Klauseln. Behandelt das Privileg der VOB-B unter § 310 Abs. 1 BGB Erlass des § 308 und § 309 BGB bei volls... |
| `agb-im-konzernverbund` | AGB im Konzernverbund. Skill behandelt die AGB-rechtliche Pruefung von Konzernvereinbarungen Service-Level-Agreements zwischen Mutter und Tochter sowie Standardklauseln bei konzerninternen Vertraegen. Aktuelle Themen: Cash-Pooling Cross-... |
| `agb-im-leasingvertrag-fortwirkung` | AGB im Leasingvertrag. Skill klaert AGB-Klauseln in Operating- und Finance-Leasing Verteilung der Sach- und Rechtsgefahr Maengelhaftungs-Drittinanspruchnahme (Drittabtretungsmodell BGH) Restwertabrechnung Andienung Mehrkilometerregelung.... |
| `agb-im-mietrecht-wohnraum-vs-gewerbe` | AGB im Mietrecht: Wohnraum- und Gewerberaummiete. Skill differenziert die AGB-rechtliche Behandlung typischer Mietklauseln Schoenheitsreparaturen Quotenklauseln Endrenovierung Mieterhoehungsvereinbarungen Versetzungsklauseln Anpassungskl... |
| `agb-in-kapitalanlagen-effektenhandel` | AGB im Kapitalanlage- und Effektenhandel. Skill klaert die AGB-rechtliche Pruefung der Allgemeinen Geschaeftsbedingungen fuer Wertpapiergeschaefte (Sonderbedingungen) der Spar- und Tagesgeldbedingungen sowie der Anforderungen aus MiFID I... |
| `agb-leasingvertrag-fortwirkung-schiedsklausel-opt-vertragsstrafe` | Agb Im Leasingvertrag Fortwirkung, Agb Schiedsklausel Opt Out Deutsches Recht, Agb Vertragsstrafe 309 Nr 6, Ergaenzende Vertragsauslegung Bei Agb Luecken, Erganzende Vertragsauslegung Agb Luecke: Agb Im Leasingvertrag Fortwirkung; Agb Sc... |
| `agb-preisanpassung-energie-stromgvv-gasgvv` | AGB-Preisanpassung Energieversorgung StromGVV GasGVV. Skill klaert die rechtlichen Anforderungen an Preisanpassungsklauseln in Energielieferungsvertraegen Grundversorgung (StromGVV GasGVV) und Sonderkundenvertraege. Behandelt EuGH-Linie... |
| `agb-pruefung-kaltstart` | Einstiegs- und Workflow-Skill für AGB Prüfung Kaltstart: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `agb-rechtswahl-schweizer-recht-rom-i` | Rechtswahl Schweizer Recht in AGB als Versuch dem deutschen AGB-Recht zu entkommen. Skill klaert Rom-I-VO Art. 3 freie Rechtswahl Art. 6 zwingender Verbraucherschutz Art. 9 Eingriffsnormen sowie die Pruefung ob §§ 305-310 BGB internation... |
| `agb-risikoklassifizierung-ampel` | Einstiegs- und Workflow-Skill für AGB Risikoklassifizierung Ampel: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `agb-schiedsklausel-opt-out-deutsches-recht` | Schiedsklausel als Opt-out aus dem deutschen AGB-Recht: BGH-Linie zur Wirksamkeit von Schiedsvereinbarungen in AGB. Pruefraster: § 1031 ZPO Schriftform New York Convention 1958 Bruessel-Ia-VO 1215/2012 Art. 25 sowie ordre-public-Vorbehal... |
| `agb-transparenzgebot-307-abs-1-satz-2` | AGB Transparenzgebot § 307 Abs. 1 Satz 2 BGB. Skill arbeitet die BGH-Linie zum Transparenzgebot aus Bestimmtheitserfordernis Verstaendlichkeit Vorhersehbarkeit der Klauselwirkung und Schutz vor verschachtelten Verweisen. Behandelt typisc... |
| `agb-und-242-bgb-eingriffsnorm` | Diskussion um § 242 BGB als Eingriffsnorm im Sinne Art. 9 Rom-I-VO. Skill problematisiert die in der Literatur vereinzelt vertretene These das gesamte AGB-Recht greife international durch weil § 242 BGB ein verbindlicher Grundsatz von Tr... |
| `agb-und-cookie-einwilligung-dsgvo` | AGB und Cookie-Einwilligung nach DSGVO und TTDSG / TDDDG. Skill klaert die Wechselwirkung von AGB-rechtlichen Klauseln und datenschutzrechtlicher Einwilligung Anforderungen an die Einwilligung Differenzierung notwendige Cookies und optio... |
| `agb-und-ipr-art-6-rom-i-verbraucher` | AGB und IPR Art. 6 Rom-I-VO Verbraucherschutz. Skill vertieft die IPR-rechtliche Pruefung der AGB bei Verbrauchervertraegen mit internationalem Bezug. Klaert die Voraussetzungen der ausgerichteten Taetigkeit nach Art. 6 Abs. 1 Buchst. b... |
| `agb-versionierung-aenderungshistorie` | Einstiegs- und Workflow-Skill für AGB Versionierung Änderungshistorie: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `agb-vertragsstrafe-309-nr-6` | AGB-Vertragsstrafe nach § 309 Nr. 6 BGB. Skill vertieft die AGB-rechtliche Behandlung von Vertragsstrafen im B2C und B2B. Klaert Hoechstgrenzen Abgrenzung zu pauschalierten Schadensersatz Sondervorschriften im Arbeitsvertrag (§ 310 Abs.... |
| `agb-werkleistung-vob-b-aktuell` | AGB im Werkvertragsrecht VOB-B in aktueller Fassung. Skill behandelt die VOB-B-Klauseln zur Maengelhaftung Abnahme Sicherheitsleistung und Aenderungsanordnung Klausel-fuer-Klausel-Wirksamkeitspruefung gegen § 307 BGB. BGH-Aktuelles zu §§... |
| `agentur-marketing-agb` | Branchen-Spezialskill für Agentur Marketing AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `allgemein` | Einstiegs- und Workflow-Skill für Allgemein: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `annahmefrist-leistungsfrist-308` | Norm- und Dogmatik-Skill für Annahmefrist Leistungsfrist 308: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `app-agb` | Branchen-Spezialskill für App AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `arbeitsrecht-agb-310-abs4` | Norm- und Dogmatik-Skill für Arbeitsrecht AGB 310 Abs. 4: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `arbeitsrecht-agb-architekten-ingenieur-auditrechte-aufrechnung` | Arbeitsrecht Agb 310 Abs4, Architekten Ingenieur Agb, Auditrechte, Aufrechnung Zurueckbehaltung 309, Automatische Verlaengerung: Arbeitsrecht Agb 310 Abs4; Architekten Ingenieur Agb; Auditrechte; Aufrechnung Zurueckbehaltung 309; Automat... |
| `architekten-ingenieur-agb` | Branchen-Spezialskill für Architekten Ingenieur AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `auditrechte` | Klausel-Spezialskill für Auditrechte: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `aufrechnung-zurueckbehaltung-309` | Norm- und Dogmatik-Skill für Aufrechnung Zurückbehaltung 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `automatische-verlaengerung` | Klausel-Spezialskill für Automatische Verlängerung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `avv-agb-b2b-harte-b2c-b2b2c-backup-datenverlust-bank` | Avv Und Agb Schnittstelle, B2B Harte Fassung, B2C B2B B2B2C Rollencheck, Backup Datenverlust, Bank Agb: Avv Und Agb Schnittstelle; B2B Harte Fassung; B2C B2B B2B2C Rollencheck; Backup Datenverlust; Bank Agb. Führt Intake, Prüfroutine, No... |
| `avv-und-agb-schnittstelle` | Branchen-Spezialskill für AVV und AGB Schnittstelle: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `b2b-harte-fassung` | Output- und Streit-Skill für B2B Harte Fassung: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `b2c-b2b-b2b2c-rollencheck` | Einstiegs- und Workflow-Skill für B2C B2B B2B2C Rollencheck: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `backup-datenverlust` | Klausel-Spezialskill für Backup Datenverlust: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `bank-agb` | Branchen-Spezialskill für Bank AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `bankvertrag-sparkassen-bauvertrag-vob` | Agb Im Bankvertrag Sparkassen Und Banken, Agb Im Bauvertrag Vob B 2024: Agb Im Bankvertrag Sparkassen Und Banken; Agb Im Bauvertrag Vob B 2024. Führt Intake, Prüfroutine, Normen-/Quellenradar, Beweislogik, Outputmuster und Qualitätscheck... |
| `battle-forms-bau-vob-beweislast-zugang-bewertung-rezensionen` | Battle Of Forms Agb Kollision, Bau Vob Agb, Beweislast Und Zugang 309, Bewertung Rezensionen, Bildungs Kurs Agb: Battle Of Forms Agb Kollision; Bau Vob Agb; Beweislast Und Zugang 309; Bewertung Rezensionen; Bildungs Kurs Agb. Führt Intak... |
| `battle-of-forms-agb-kollision` | Norm- und Dogmatik-Skill für Battle of Forms AGB Kollision: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `bau-vob-agb` | Branchen-Spezialskill für Bau VOB/B AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `begriff-vorformuliert-digitalen-produkten-iso-vertraegen` | Agb Begriff Vorformuliert 305, Agb Bei Digitalen Produkten 327F Update, Agb Bei Iso Vertraegen International, Agb Bei Kreditvertraegen Verbraucherdarlehen: Agb Begriff Vorformuliert 305; Agb Bei Digitalen Produkten 327F Update; Agb Bei I... |
| `beweislast-und-zugang-309` | Norm- und Dogmatik-Skill für Beweislast und Zugang 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `bewertung-rezensionen` | Klausel-Spezialskill für Bewertung Rezensionen: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `bildungs-kurs-agb` | Branchen-Spezialskill für Bildungs Kurs AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `blue-pencil-board-agb-bonitaetspruefung-bonus-rabatt-business` | Blue Pencil Und Geltungserhaltende Reduktion, Board Brief Agb, Bonitaetspruefung, Bonus Rabatt, Business Summary Agb: Blue Pencil Und Geltungserhaltende Reduktion; Board Brief Agb; Bonitaetspruefung; Bonus Rabatt; Business Summary Agb. F... |
| `blue-pencil-und-geltungserhaltende-reduktion` | Blue-Pencil-Test und geltungserhaltende Reduktion in AGB-Vertraegen. Skill arbeitet die Methodik aus wann eine teilbare Klausel durch Streichung in einen wirksamen Restbestand zerfaellt und wann dies ausgeschlossen ist. Behandelt die BGH... |
| `board-brief-agb` | Output- und Streit-Skill für Board Brief AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `bonitaetspruefung` | Klausel-Spezialskill für Bonitätsprüfung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `bonus-rabatt` | Klausel-Spezialskill für Bonus Rabatt: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `business-summary-agb` | Output- und Streit-Skill für Business Summary AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `change-request` | Klausel-Spezialskill für Change Reqüst: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `change-request-clickwrap-beweisakte-cloud-hosting-consulting-agb` | Change Request, Clickwrap Beweisakte, Cloud Hosting Agb, Consulting Agb, Crowdfunding Agb: Change Request; Clickwrap Beweisakte; Cloud Hosting Agb; Consulting Agb; Crowdfunding Agb. Führt Intake, Prüfroutine, Normen-/Quellenradar, Beweis... |
| `clickwrap-beweisakte` | Output- und Streit-Skill für Clickwrap Beweisakte: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `cloud-hosting-agb` | Branchen-Spezialskill für Cloud Hosting AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `compliance-sanktionen` | Klausel-Spezialskill für Compliance Sanktionen: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `consulting-agb` | Branchen-Spezialskill für Consulting AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `crowdfunding-agb` | Branchen-Spezialskill für Crowdfunding AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `crypto-exchange-agb` | Branchen-Spezialskill für Crypto Exchange AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `crypto-exchange-darlehen-finanzierung-datenexport-portabilitaet` | Crypto Exchange Agb, Darlehen Finanzierung Agb, Datenexport Portabilitaet, Datenschutzverweise Agb, Definitionen Glossar Agb: Crypto Exchange Agb; Darlehen Finanzierung Agb; Datenexport Portabilitaet; Datenschutzverweise Agb; Definitione... |
| `darlehen-finanzierung-agb` | Branchen-Spezialskill für Darlehen Finanzierung AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `datenexport-portabilitaet` | Klausel-Spezialskill für Datenexport Portabilität: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `datenschutzverweise-agb` | Klausel-Spezialskill für Datenschutzverweise AGB: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `definitionen-glossar-agb` | Output- und Streit-Skill für Definitionen Glossar AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `deutsch-englisch-agb` | Output- und Streit-Skill für Deutsch Englisch AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `deutsch-englisch-digitale-inhalte-handbuch-dokumentenfamilie` | Deutsch Englisch Agb, Digitale Inhalte Services, Dokumentation Handbuch, Dokumentenfamilie Rangfolge, Ecommerce Shop Agb: Deutsch Englisch Agb; Digitale Inhalte Services; Dokumentation Handbuch; Dokumentenfamilie Rangfolge; Ecommerce Sho... |
| `digitale-inhalte-services` | Branchen-Spezialskill für Digitale Inhalte Services: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `dokumentation-handbuch` | Klausel-Spezialskill für Dokumentation Handbuch: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `dokumentenfamilie-rangfolge` | Einstiegs- und Workflow-Skill für Dokumentenfamilie Rangfolge: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `ecommerce-shop-agb` | Branchen-Spezialskill für Ecommerce Shop AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `eigentumsvorbehalt` | Klausel-Spezialskill für Eigentumsvorbehalt: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `eigentumsvorbehalt-einbeziehung-hinweis-online-clickwrap` | Eigentumsvorbehalt, Einbeziehung Hinweis Kenntnisnahme 305, Einbeziehung Online Clickwrap Browsewrap, Einkaufsbedingungen B2B, Einstweilige Verfuegung Agb: Eigentumsvorbehalt; Einbeziehung Hinweis Kenntnisnahme 305; Einbeziehung Online C... |
| `einbeziehung-hinweis-kenntnisnahme-305` | Norm- und Dogmatik-Skill für Einbeziehung Hinweis Kenntnisnahme 305: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `einbeziehung-online-clickwrap-browsewrap` | Norm- und Dogmatik-Skill für Einbeziehung Online Clickwrap Browsewrap: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `einkaufsbedingungen-b2b` | Branchen-Spezialskill für Einkaufsbedingungen B2B: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `einstweilige-verfuegung-agb` | Output- und Streit-Skill für Einstweilige Verfügung AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `energieversorgung-agb` | Branchen-Spezialskill für Energieversorgung AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `energieversorgung-agb-entgelt-nebenkosten-exklusivitaet` | Energieversorgung Agb, Entgelt Nebenkosten Service Fees, Exklusivitaet, Factoring Agb, Fiktive Erklaerung Zustimmung 308: Energieversorgung Agb; Entgelt Nebenkosten Service Fees; Exklusivitaet; Factoring Agb; Fiktive Erklaerung Zustimmun... |
| `entgelt-nebenkosten-service-fees` | Klausel-Spezialskill für Entgelt Nebenkosten Service Fees: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `ergaenzende-vertragsauslegung-bei-agb-luecken` | Ergaenzende Vertragsauslegung bei AGB-Luecken. Skill klaert die BGH-Linie zur Lueckenfuellung wenn AGB-Klauseln unwirksam sind. Behandelt das Verhaeltnis von § 306 Abs. 2 BGB Gesetzesrecht und ergaenzender Vertragsauslegung sowie die Gre... |
| `erganzende-vertragsauslegung-agb-luecke` | Norm- und Dogmatik-Skill für Erganzende Vertragsauslegung AGB Lücke: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `exklusivitaet` | Klausel-Spezialskill für Exklusivität: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `factoring-agb` | Branchen-Spezialskill für Factoring AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `feedback-rechte` | Klausel-Spezialskill für Feedback Rechte: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `fiktive-erklaerung-zustimmung-308` | Norm- und Dogmatik-Skill für Fiktive Erklärung Zustimmung 308: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `fitnessstudio-agb` | Branchen-Spezialskill für Fitnessstudio AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `fitnessstudio-agb-force-majeure-formvorgaben-anzeigen-forschung` | Fitnessstudio Agb, Force Majeure Hoehere Gewalt, Formvorgaben Anzeigen Erklaerungen 309, Forschung Entwicklung Agb, Fragebogen Agb Automation: Fitnessstudio Agb; Force Majeure Hoehere Gewalt; Formvorgaben Anzeigen Erklaerungen 309; Forsc... |
| `force-majeure-hoehere-gewalt` | Klausel-Spezialskill für Force Majeure Höhere Gewalt: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `formulararbeitsvertrag` | Branchen-Spezialskill für Formulararbeitsvertrag: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `formulararbeitsvertrag-haendlervertrag-agb-inhaltskontrolle` | Formulararbeitsvertrag, Haendlervertrag Agb, Inhaltskontrolle 307 Generalklausel, Klausel Checkliste Self Service, Klausel Entwerfen Aggressiv: Formulararbeitsvertrag; Haendlervertrag Agb; Inhaltskontrolle 307 Generalklausel; Klausel Che... |
| `formvorgaben-anzeigen-erklaerungen-309` | Norm- und Dogmatik-Skill für Formvorgaben Anzeigen Erklärungen 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `forschung-entwicklung-agb` | Branchen-Spezialskill für Forschung Entwicklung AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `fragebogen-agb-automation` | Output- und Streit-Skill für Fragebogen AGB Automation: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `franchise-agb` | Branchen-Spezialskill für Franchise AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `franchise-agb-gaming-garantie-beschaffenheit-gerichtsstand` | Franchise Agb, Gaming Agb, Garantie Beschaffenheit, Gerichtsstand, Gesellschaftsrechtliche Satzungen Agb Abgrenzung: Franchise Agb; Gaming Agb; Garantie Beschaffenheit; Gerichtsstand; Gesellschaftsrechtliche Satzungen Agb Abgrenzung. Füh... |
| `gaming-agb` | Branchen-Spezialskill für Gaming AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `garantie-beschaffenheit` | Klausel-Spezialskill für Garantie Beschaffenheit: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `gerichtsstand` | Klausel-Spezialskill für Gerichtsstand: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `gesellschaftsrechtliche-satzungen-agb-abgrenzung` | Norm- und Dogmatik-Skill für Gesellschaftsrechtliche Satzungen AGB Abgrenzung: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `gesetzliches-leitbild-abweichung-307` | Norm- und Dogmatik-Skill für Gesetzliches Leitbild Abweichung 307: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `gesetzliches-leitbild-gewahrleistung-ausschluss-gewerbemiete-agb` | Gesetzliches Leitbild Abweichung 307, Gewahrleistung Ausschluss, Gewerbemiete Agb, Handelsvertreter Agb, Indexierung: Gesetzliches Leitbild Abweichung 307; Gewahrleistung Ausschluss; Gewerbemiete Agb; Handelsvertreter Agb; Indexierung. F... |
| `gewahrleistung-ausschluss` | Klausel-Spezialskill für Gewährleistung Ausschluss: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `gewerbemiete-agb` | Branchen-Spezialskill für Gewerbemiete AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `haendlervertrag-agb` | Branchen-Spezialskill für Haendlervertrag AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `haftung-grobe-fahrlaessigkeit-vorsatz` | Klausel-Spezialskill für Haftung Grobe Fahrlaessigkeit Vorsatz: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `haftung-indirekte-schaeden` | Klausel-Spezialskill für Haftung Indirekte Schaeden: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `haftung-leben-koerper-gesundheit-309` | Norm- und Dogmatik-Skill für Haftung Leben Koerper Gesundheit 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `haftung-sanktionen-grobe-fahrlaessigkeit-indirekte-schaeden` | Compliance Sanktionen, Haftung Grobe Fahrlaessigkeit Vorsatz, Haftung Indirekte Schaeden, Haftung Leben Koerper Gesundheit 309, Haftungscap Summe: Compliance Sanktionen; Haftung Grobe Fahrlaessigkeit Vorsatz; Haftung Indirekte Schaeden;... |
| `haftungscap-summe` | Klausel-Spezialskill für Haftungscap Summe: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `handelsvertreter-agb` | Branchen-Spezialskill für Handelsvertreter AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `indexierung` | Klausel-Spezialskill für Indexierung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `individualabrede-305b` | Norm- und Dogmatik-Skill für Individualabrede 305b: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `individualabrede-305b-individualklage-verteidigung` | Individualabrede 305B, Individualklage Verteidigung, Insolvenzverkauf Agb, Ip Nutzungsrechte, Kardinalpflichten: Individualabrede 305B; Individualklage Verteidigung; Insolvenzverkauf Agb; Ip Nutzungsrechte; Kardinalpflichten. Führt Intak... |
| `individualklage-verteidigung` | Output- und Streit-Skill für Individualklage Verteidigung: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `inhaltskontrolle-307-generalklausel` | Norm- und Dogmatik-Skill für Inhaltskontrolle 307 Generalklausel: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `insolvenzverkauf-agb` | Branchen-Spezialskill für Insolvenzverkauf AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `ip-nutzungsrechte` | Klausel-Spezialskill für IP Nutzungsrechte: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `ipr-art-versionierung-aenderungshistorie-werkleistung-vob` | Agb Und Ipr Art 6 Rom I Verbraucher, Agb Versionierung Aenderungshistorie, Agb Werkleistung Vob B Aktuell, Agentur Marketing Agb, App Agb: Agb Und Ipr Art 6 Rom I Verbraucher; Agb Versionierung Aenderungshistorie; Agb Werkleistung Vob B... |
| `kardinalpflichten` | Klausel-Spezialskill für Kardinalpflichten: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `ki-output-nutzung` | Klausel-Spezialskill für KI Output Nutzung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `ki-service-agb` | Branchen-Spezialskill für KI Service AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `ki-service-kollisionsrecht-ipr-konto-kuendigung-kuendigung` | Ki Service Agb, Kollisionsrecht Ipr Agb, Konto Kündigung Sperre, Kündigung Aus Wichtigem Grund, Kündigung Ordentlich: Ki Service Agb; Kollisionsrecht Ipr Agb; Konto Kündigung Sperre; Kündigung Aus Wichtigem Grund; Kündigung Ordentlich. F... |
| `klausel-checkliste-self-service` | Output- und Streit-Skill für Klausel Checkliste Self Service: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `klausel-entwerfen-aggressiv` | Output- und Streit-Skill für Klausel Entwerfen Aggressiv: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `klausel-entwerfen-balanced` | Output- und Streit-Skill für Klausel Entwerfen Balanced: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `klausel-entwerfen-low-risk` | Output- und Streit-Skill für Klausel Entwerfen Low Risk: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `klausel-entwerfen-low-risk-klauselbibliothek-aufbau` | Klausel Entwerfen Balanced, Klausel Entwerfen Low Risk, Klauselbibliothek Aufbau, Klauselinventar Und Scope, Klauselvarianten Vergleich: Klausel Entwerfen Balanced; Klausel Entwerfen Low Risk; Klauselbibliothek Aufbau; Klauselinventar Un... |
| `klauselbibliothek-aufbau` | Einstiegs- und Workflow-Skill für Klauselbibliothek Aufbau: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `klauselinventar-und-scope` | Einstiegs- und Workflow-Skill für Klauselinventar und Scope: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `klauselvarianten-vergleich` | Output- und Streit-Skill für Klauselvarianten Vergleich: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `klauselverbote-308-systematik` | Norm- und Dogmatik-Skill für Klauselverbote 308 Systematik: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `klauselverbote-309-systematik` | Norm- und Dogmatik-Skill für Klauselverbote 309 Systematik: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `klauselverbote-systematik-klauselverbote-systematik` | Klauselverbote 308 Systematik, Klauselverbote 309 Systematik, Konzernklausel, Msa Rahmenvertrag, Preisanpassung Klausel: Klauselverbote 308 Systematik; Klauselverbote 309 Systematik; Konzernklausel; Msa Rahmenvertrag; Preisanpassung Klau... |
| `kollisionsrecht-ipr-agb` | Einstiegs- und Workflow-Skill für Kollisionsrecht IPR AGB: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `konto-kuendigung-sperre` | Klausel-Spezialskill für Konto Kündigung Sperre: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `konzernklausel` | Klausel-Spezialskill für Konzernklausel: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `kuendigung-aus-wichtigem-grund` | Klausel-Spezialskill für Kündigung Aus Wichtigem Grund: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `kuendigung-ordentlich` | Klausel-Spezialskill für Kündigung Ordentlich: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `kuendigungsfiktion-und-nachfrist-308` | Norm- und Dogmatik-Skill für Kündigungsfiktion und Nachfrist 308: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `kurzfristige-preiserhoehung-309` | Norm- und Dogmatik-Skill für Kurzfristige Preiserhöhung 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `kurzfristige-preiserhoehung-lieferfrist-teillieferung` | Kurzfristige Preiserhöhung 309, Lieferfrist Teillieferung, Agb Anwaltsvertrag Und Allg Mandatsbedingungen, Agb Im Arbeitsvertrag 310 Abs 4 Vertieft: Kurzfristige Preiserhöhung 309; Lieferfrist Teillieferung; Agb Anwaltsvertrag Und Allg M... |
| `lagerbedingungen` | Branchen-Spezialskill für Lagerbedingungen: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `lagerbedingungen-laufzeit-verlaengerung-leasing-agb` | Lagerbedingungen, Laufzeit Verlaengerung 309, Leasing Agb, Leistungsaenderung Produktupdate, Liquidated Damages: Lagerbedingungen; Laufzeit Verlaengerung 309; Leasing Agb; Leistungsaenderung Produktupdate; Liquidated Damages. Führt Intak... |
| `laufzeit-verlaengerung-309` | Norm- und Dogmatik-Skill für Laufzeit Verlängerung 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `leasing-agb` | Branchen-Spezialskill für Leasing AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `legal-note-redline-output` | Einstiegs- und Workflow-Skill für Legal Note Redline Output: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `leistungsaenderung-produktupdate` | Klausel-Spezialskill für Leistungsänderung Produktupdate: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `lieferfrist-teillieferung` | Klausel-Spezialskill für Lieferfrist Teillieferung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `liquidated-damages` | Klausel-Spezialskill für Liquidated Damages: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `logistik-spedition-agb` | Branchen-Spezialskill für Logistik Spedition AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `logistik-spedition-maengelrechte-mahngebuehren-zinsanpassung` | Logistik Spedition Agb, Maengelrechte 309, Mahngebuehren Und Zinsanpassung Agb, Mandanteninterview Agb, Mandantenmail Agb: Logistik Spedition Agb; Maengelrechte 309; Mahngebuehren Und Zinsanpassung Agb; Mandanteninterview Agb; Mandantenm... |
| `maengelrechte-309` | Norm- und Dogmatik-Skill für Mängelrechte 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `mahngebuehren-und-zinsanpassung-agb` | Mahngebuehren und Zinsanpassungsklauseln in AGB. Skill klaert wie hoch Mahngebuehren in AGB sein duerfen Differenzierung erste zweite dritte Mahnung sowie die Wechselwirkung zum Verzugsschaden (§ 280 II 286 BGB). Behandelt automatische Z... |
| `mandanteninterview-agb` | Einstiegs- und Workflow-Skill für Mandanteninterview AGB: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `mandantenmail-agb` | Output- und Streit-Skill für Mandantenmail AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `marketplace-agb` | Branchen-Spezialskill für Marketplace AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `marketplace-agb-mediation-escalation-medizinische-leistungen` | Marketplace Agb, Mediation Escalation, Medizinische Leistungen Agb, Mehrdeutigkeit 305C2, Mehrsprachige Agb Check: Marketplace Agb; Mediation Escalation; Medizinische Leistungen Agb; Mehrdeutigkeit 305C2; Mehrsprachige Agb Check. Führt I... |
| `massenschaden-datenmodell` | Output- und Streit-Skill für Massenschaden Datenmodell: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `massenschaden-datenmodell-rechtsabteilung-haftungsdeckel` | Massenschaden Datenmodell, Rechtsabteilung Haftungsdeckel Für Daten Und Ki Schaeden, Schadenspauschale 309, Abmahnung Reagieren, Abnahme Testing: Massenschaden Datenmodell; Rechtsabteilung Haftungsdeckel Für Daten Und Ki Schaeden; Schade... |
| `mediation-escalation` | Klausel-Spezialskill für Mediation Escalation: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `medizinische-leistungen-agb` | Branchen-Spezialskill für Medizinische Leistungen AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `mehrdeutigkeit-305c2` | Norm- und Dogmatik-Skill für Mehrdeutigkeit 305c2: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `mehrsprachige-agb-check` | Einstiegs- und Workflow-Skill für Mehrsprachige AGB Check: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `mindestabnahme` | Klausel-Spezialskill für Mindestabnahme: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `mindestabnahme-mitwirkungspflichten-nacherfuellung-vorrang` | Mindestabnahme, Mitwirkungspflichten, Nacherfuellung Vorrang, Nda Standardbedingungen, Negative Feststellung Agb: Mindestabnahme; Mitwirkungspflichten; Nacherfuellung Vorrang; Nda Standardbedingungen; Negative Feststellung Agb. Führt Int... |
| `mitwirkungspflichten` | Klausel-Spezialskill für Mitwirkungspflichten: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `msa-rahmenvertrag` | Branchen-Spezialskill für MSA Rahmenvertrag: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `nacherfuellung-vorrang` | Klausel-Spezialskill für Nacherfüllung Vorrang: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `nda-standardbedingungen` | Branchen-Spezialskill für NDA Standardbedingungen: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `negative-feststellung-agb` | Output- und Streit-Skill für Negative Feststellung AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `non-solicitation` | Klausel-Spezialskill für Non Solicitation: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `non-solicitation-norm-live-open-source-parking-mobility-plain` | Non Solicitation, Norm Live Check Gesetze Im Internet, Open Source Komponenten, Parking Mobility Agb, Plain Language Politur: Non Solicitation; Norm Live Check Gesetze Im Internet; Open Source Komponenten; Parking Mobility Agb; Plain Lan... |
| `norm-live-check-gesetze-im-internet` | Einstiegs- und Workflow-Skill für Norm Live Check Gesetze Im Internet: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `open-source-komponenten` | Klausel-Spezialskill für Open Source Komponenten: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `parking-mobility-agb` | Branchen-Spezialskill für Parking Mobility AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `plain-language-politur` | Output- und Streit-Skill für Plain Language Politur: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `plattform-online-gate-rollout-rangfolge-sprache-rechtsabteilung` | Plattform Und Online Checkout, Quality Gate Vor Rollout, Rangfolge Sprache, Rechtsabteilung Preisanpassung Bei Dauervertraegen Nach Energiek, Rechtsabteilung Zustimmungsfiktion Nach Bank Agb Urteil: Plattform Und Online Checkout; Quality... |
| `plattform-und-online-checkout` | Einstiegs- und Workflow-Skill für Plattform und Online Checkout: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `plattformnutzung-app-vereinen-verbaenden` | Agb Bei Plattformnutzung App Stores, Agb Bei Vereinen Und Verbaenden: Agb Bei Plattformnutzung App Stores; Agb Bei Vereinen Und Verbaenden. Führt Intake, Prüfroutine, Normen-/Quellenradar, Beweislogik, Outputmuster und Qualitätscheck zus... |
| `preisanpassung-klausel` | Klausel-Spezialskill für Preisanpassung Klausel: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `product-counsel-feedback-rechte-annahmefrist-leistungsfrist` | Product Counsel Workflow, Feedback Rechte, Annahmefrist Leistungsfrist 308, Kuendigungsfiktion Und Nachfrist 308: Product Counsel Workflow; Feedback Rechte; Annahmefrist Leistungsfrist 308; Kuendigungsfiktion Und Nachfrist 308. Führt Int... |
| `product-counsel-workflow` | Output- und Streit-Skill für Product Counsel Workflow: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `quality-gate-vor-rollout` | Output- und Streit-Skill für Quality Gate Vor Rollout: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `rangfolge-sprache` | Klausel-Spezialskill für Rangfolge Sprache: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `rechtsabteilung-change-control-klauseln-im-konzernvertrag` | Rechtsabteilungs-Spezialskill für Change-Control-Klauseln im Konzernvertrag: Einseitige Leistungs- und Prozessänderungen werden in komplexen Konzern-Frameworks auf Zumutbarkeit und Governance geprüft. Mit Normen, Rechtsprechungsanker, Be... |
| `rechtsabteilung-change-rechtsabteilung-vertragsstrafe` | Rechtsabteilung Change Control Klauseln Im Konzernvertrag, Rechtsabteilung Vertragsstrafe In Einheitspreis Und Liefervertra, Salvatorische Klausel, Salvatorische Klausel Grenzen Rspr, Ueberraschende Klausel 305C: Rechtsabteilung Change C... |
| `rechtsabteilung-haftungsdeckel-fuer-daten-und-ki-schaeden` | Rechtsabteilungs-Spezialskill für Haftungsdeckel für Daten- und KI-Schäden: Liability Caps bei Software, Daten, KI und Outsourcing werden so geprüft, dass Kardinalpflichten und Personenschäden nicht versehentlich abgeschnitten werden. Mi... |
| `rechtsabteilung-preisanpassung-bei-dauervertraegen-nach-energiek` | Rechtsabteilungs-Spezialskill für Preisanpassung bei Dauerverträgen nach Energiekosten-Schock: Preisgleitklauseln werden nach Anlass, Parameter, Transparenz, Kündigungsrecht und Mitteilungsmechanik bewertet. Mit Normen, Rechtsprechungsan... |
| `rechtsabteilung-vertragsstrafe-in-einheitspreis-und-liefervertra` | Rechtsabteilungs-Spezialskill für Vertragsstrafe in Einheitspreis- und Lieferverträgen: Rechtsabteilungen prüfen, ob Bezugsgrößen der Vertragsstrafe die tatsächlich beauftragte Leistung überschießen. Mit Normen, Rechtsprechungsanker, Bel... |
| `rechtsabteilung-zustimmungsfiktion-nach-bank-agb-urteil` | Rechtsabteilungs-Spezialskill für Zustimmungsfiktion nach Bank-AGB-Urteil: Klauseln, die Schweigen oder bloße Weiternutzung als Zustimmung behandeln, werden für Preis- und Leistungsänderungen in B2C und B2B auseinandergenommen. Mit Norme... |
| `rechtsfolge-306-kein-blue-pencil` | Norm- und Dogmatik-Skill für Rechtsfolge 306 Kein Blü Pencil: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `rechtsfolge-kein-rechtsfolgen-rueckabwicklung-rechtswahl-redline` | Rechtsfolge 306 Kein Blue Pencil, Rechtsfolgen Rueckabwicklung Agb, Rechtswahl, Redline Kommentar Agb, Referenznennung: Rechtsfolge 306 Kein Blue Pencil; Rechtsfolgen Rueckabwicklung Agb; Rechtswahl; Redline Kommentar Agb; Referenznennun... |
| `rechtsfolgen-rueckabwicklung-agb` | Norm- und Dogmatik-Skill für Rechtsfolgen Rückabwicklung AGB: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `rechtswahl` | Klausel-Spezialskill für Rechtswahl: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `rechtswahl-schweizer-risikoklassifizierung-ampel` | Agb Rechtswahl Schweizer Recht Rom I, Agb Risikoklassifizierung Ampel, Agb Transparenzgebot 307 Abs 1 Satz 2, Agb Und 242 Bgb Eingriffsnorm, Agb Und Cookie Einwilligung Dsgvo: Agb Rechtswahl Schweizer Recht Rom I; Agb Risikoklassifizieru... |
| `red-team-gegneransicht-agb` | Einstiegs- und Workflow-Skill für Red Team Gegneransicht AGB: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `redline-kommentar-agb` | Output- und Streit-Skill für Redline Kommentar AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `referenznennung` | Klausel-Spezialskill für Referenznennung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `reisebedingungen` | Branchen-Spezialskill für Reisebedingungen: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `reisebedingungen-reseller-agb-risk-acceptance-rollout-mail` | Reisebedingungen, Reseller Agb, Risk Acceptance Memo, Rollout Mail Bestandskunden, Rollout Monitoring Agb: Reisebedingungen; Reseller Agb; Risk Acceptance Memo; Rollout Mail Bestandskunden; Rollout Monitoring Agb. Führt Intake, Prüfrouti... |
| `reseller-agb` | Branchen-Spezialskill für Reseller AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `risk-acceptance-memo` | Output- und Streit-Skill für Risk Acceptance Memo: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `rollout-mail-bestandskunden` | Output- und Streit-Skill für Rollout Mail Bestandskunden: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `rollout-monitoring-agb` | Einstiegs- und Workflow-Skill für Rollout Monitoring AGB: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `ruegeobliegenheit` | Klausel-Spezialskill für Rügeobliegenheit: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `ruegeobliegenheit-saas-agb-schiedsgericht-schriftform-textform` | Ruegeobliegenheit, Saas Agb, Schiedsgericht, Schriftform Textform, Security Incidents: Ruegeobliegenheit; Saas Agb; Schiedsgericht; Schriftform Textform; Security Incidents. Führt Intake, Prüfroutine, Normen-/Quellenradar, Beweislogik, O... |
| `saas-agb` | Branchen-Spezialskill für SaaS AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `salvatorische-klausel` | Klausel-Spezialskill für Salvatorische Klausel: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `salvatorische-klausel-grenzen-rspr` | Salvatorische Klausel: Grenzen und Wirkung. Skill klaert die BGH-Linie zu Salvatorischen Klauseln in AGB-Vertraegen Wirkung der Klausel auf die Unwirksamkeit einzelner Bestimmungen Wechselwirkung mit § 306 BGB. Behandelt Sondervarianten... |
| `schadenspauschale-309` | Norm- und Dogmatik-Skill für Schadenspauschale 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `schiedsgericht` | Klausel-Spezialskill für Schiedsgericht: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `schriftform-textform` | Klausel-Spezialskill für Schriftform Textform: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `security-incidents` | Klausel-Spezialskill für Security Incidents: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `sicherungsrechte` | Klausel-Spezialskill für Sicherungsrechte: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `sicherungsrechte-sla-service-social-media-softwarelizenz-agb` | Sicherungsrechte, Sla Service Credits, Social Media Agb, Softwarelizenz Agb, Sperrung Suspendierung: Sicherungsrechte; Sla Service Credits; Social Media Agb; Softwarelizenz Agb; Sperrung Suspendierung. Führt Intake, Prüfroutine, Normen-/... |
| `sla-service-credits` | Klausel-Spezialskill für SLA Service Credits: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `social-media-agb` | Branchen-Spezialskill für Social Media AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `softwarelizenz-agb` | Branchen-Spezialskill für Softwarelizenz AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `sperrung-suspendierung` | Klausel-Spezialskill für Sperrung Suspendierung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `steuern-umsatzsteuer` | Klausel-Spezialskill für Steürn Umsatzsteür: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `steuern-umsatzsteuer-stummer-upload-subscription-abonnement` | Steuern Umsatzsteuer, Stummer Upload Agb Dokumente, Subscription Abonnement, Subscription Box Agb, Subunternehmer: Steuern Umsatzsteuer; Stummer Upload Agb Dokumente; Subscription Abonnement; Subscription Box Agb; Subunternehmer. Führt I... |
| `stummer-upload-agb-dokumente` | Einstiegs- und Workflow-Skill für Stummer Upload AGB Dokumente: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `subscription-abonnement` | Branchen-Spezialskill für Subscription Abonnement: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `subscription-box-agb` | Branchen-Spezialskill für Subscription Box AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `subunternehmer` | Klausel-Spezialskill für Subunternehmer: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `support-response-telekommunikation-agb-transparenzgebot-uklag` | Support Response Times, Telekommunikation Agb, Transparenzgebot 307, Uklag Unterlassung Verbandsklage, Unterlassungserklaerung Modifizieren: Support Response Times; Telekommunikation Agb; Transparenzgebot 307; Uklag Unterlassung Verbands... |
| `support-response-times` | Klausel-Spezialskill für Support Response Times: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `telekommunikation-agb` | Branchen-Spezialskill für Telekommunikation AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `transparenzgebot-307` | Norm- und Dogmatik-Skill für Transparenzgebot 307: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `ueberraschende-klausel-305c` | Norm- und Dogmatik-Skill für Überraschende Klausel 305c: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `uklag-unterlassung-verbandsklage` | Norm- und Dogmatik-Skill für UKlaG Unterlassung Verbandsklage: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `unterlassungserklaerung-modifizieren` | Output- und Streit-Skill für Unterlassungserklärung Modifizieren: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `unternehmerverkehr-310-abs1` | Norm- und Dogmatik-Skill für Unternehmerverkehr 310 Abs. 1: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `unternehmerverkehr-abs1-schnellcheck-user-content-vdug` | Unternehmerverkehr 310 Abs1, Unternehmerverkehr Schnellcheck, User Content Moderation, Vdug Abhilfeklage Agb Schnittstelle, Verbraucherbesonderheiten 310 Abs3: Unternehmerverkehr 310 Abs1; Unternehmerverkehr Schnellcheck; User Content Mo... |
| `unternehmerverkehr-schnellcheck` | Einstiegs- und Workflow-Skill für Unternehmerverkehr Schnellcheck: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `user-content-moderation` | Klausel-Spezialskill für User Content Moderation: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `vdug-abhilfeklage-agb-schnittstelle` | Norm- und Dogmatik-Skill für VDuG Abhilfeklage AGB Schnittstelle: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `verbraucherbesonderheiten-310-abs3` | Norm- und Dogmatik-Skill für Verbraucherbesonderheiten 310 Abs. 3: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `verbraucherfreundliche-fassung` | Output- und Streit-Skill für Verbraucherfreundliche Fassung: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `verbraucherfreundliche-fassung-verbraucherschutz-schnellcheck` | Verbraucherfreundliche Fassung, Verbraucherschutz Schnellcheck, Vereinsbedingungen, Verfuegbarkeit Wartungsfenster, Verhandlungs Playbook Agb: Verbraucherfreundliche Fassung; Verbraucherschutz Schnellcheck; Vereinsbedingungen; Verfuegbar... |
| `verbraucherschutz-schnellcheck` | Einstiegs- und Workflow-Skill für Verbraucherschutz Schnellcheck: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `vereinsbedingungen` | Branchen-Spezialskill für Vereinsbedingungen: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `verfuegbarkeit-wartungsfenster` | Klausel-Spezialskill für Verfügbarkeit Wartungsfenster: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `vergaberechtliche-vertragsbedingungen` | Branchen-Spezialskill für Vergaberechtliche Vertragsbedingungen: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `vergaberechtliche-vertragsbedingungen-vertragsstrafe` | Vergaberechtliche Vertragsbedingungen, Vertragsstrafe 309, Vertraulichkeit Klausel, Agb Für Vereinsausschluss Und Haftung, Agb Haftung Erfuellungsgehilfen: Vergaberechtliche Vertragsbedingungen; Vertragsstrafe 309; Vertraulichkeit Klause... |
| `verhandlungs-playbook-agb` | Output- und Streit-Skill für Verhandlungs Playbook AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `verjaehrungsverkuerzung` | Klausel-Spezialskill für Verjaehrungsverkürzung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `verjaehrungsverkuerzung-verkaufsbedingungen-b2b-versicherung-avb` | Verjaehrungsverkuerzung, Verkaufsbedingungen B2B, Versicherung Avb, Versionsdiff Agb, Vollmacht Vertretung: Verjaehrungsverkuerzung; Verkaufsbedingungen B2B; Versicherung Avb; Versionsdiff Agb; Vollmacht Vertretung. Führt Intake, Prüfrou... |
| `verkaufsbedingungen-b2b` | Branchen-Spezialskill für Verkaufsbedingungen B2B: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `versicherung-avb` | Branchen-Spezialskill für Versicherung Avb: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `versicherungsvertraegen-vvg-agb-konzernverbund-mietrecht` | Agb Bei Versicherungsvertraegen Vvg, Agb Im Konzernverbund, Agb Im Mietrecht Wohnraum Vs Gewerbe, Agb In Kapitalanlagen Effektenhandel, Agb Preisanpassung Energie Stromgvv Gasgvv: Agb Bei Versicherungsvertraegen Vvg; Agb Im Konzernverbun... |
| `versionsdiff-agb` | Output- und Streit-Skill für Versionsdiff AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `vertragsstrafe-309` | Norm- und Dogmatik-Skill für Vertragsstrafe 309: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `vertraulichkeit-klausel` | Klausel-Spezialskill für Vertraulichkeit Klausel: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `vollmacht-vertretung` | Klausel-Spezialskill für Vollmacht Vertretung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `vorkasse-abschlag-sicherheit` | Klausel-Spezialskill für Vorkasse Abschlag Sicherheit: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `vorkasse-abschlag-wartung-maintenance-website-update-wesentliche` | Vorkasse Abschlag Sicherheit, Wartung Maintenance, Website Update Check, Wesentliche Rechte Pflichten 307, Widerruf Umfeld Agb: Vorkasse Abschlag Sicherheit; Wartung Maintenance; Website Update Check; Wesentliche Rechte Pflichten 307; Wi... |
| `wartung-maintenance` | Branchen-Spezialskill für Wartung Maintenance: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `website-update-check` | Output- und Streit-Skill für Website Update Check: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `wesentliche-rechte-pflichten-307` | Norm- und Dogmatik-Skill für Wesentliche Rechte Pflichten 307: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `widerruf-umfeld-agb` | Klausel-Spezialskill für Widerruf Umfeld AGB: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `wohnraummiete-agb` | Branchen-Spezialskill für Wohnraummiete AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `wohnraummiete-agb-zahlungsdienste-zahlungsmittel-chargeback` | Wohnraummiete Agb, Zahlungsdienste Agb, Zahlungsmittel Chargeback, Zahlungsverzug Mahnkosten: Wohnraummiete Agb; Zahlungsdienste Agb; Zahlungsmittel Chargeback; Zahlungsverzug Mahnkosten. Führt Intake, Prüfroutine, Normen-/Quellenradar,... |
| `zahlungsdienste-agb` | Branchen-Spezialskill für Zahlungsdienste AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `zahlungsmittel-chargeback` | Klausel-Spezialskill für Zahlungsmittel Chargeback: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `zahlungsverzug-mahnkosten` | Klausel-Spezialskill für Zahlungsverzug Mahnkosten: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
