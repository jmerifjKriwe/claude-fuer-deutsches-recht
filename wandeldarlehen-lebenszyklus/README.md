# Wandeldarlehen-Lebenszyklus

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`wandeldarlehen-lebenszyklus`) | [`wandeldarlehen-lebenszyklus.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/wandeldarlehen-lebenszyklus.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Nebelstern Ventures - Berliner VC-Pipeline, Wandeldarlehen und Follow-on-Chaos** (`venture-capital-geber-nebelstern-portfolio-berlin`) | [Gesamt-PDF lesen](../testakten/venture-capital-geber-nebelstern-portfolio-berlin/gesamt-pdf/venture-capital-geber-nebelstern-portfolio-berlin_gesamt.pdf) | [`testakte-venture-capital-geber-nebelstern-portfolio-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-venture-capital-geber-nebelstern-portfolio-berlin.zip) |
| **Wandeldarlehen-Lebenszyklus (Sonnenglas Solartechnologie UG)** (`wandeldarlehen-beispielcase`) | [Gesamt-PDF lesen](../testakten/wandeldarlehen-beispielcase/gesamt-pdf/wandeldarlehen-beispielcase_gesamt.pdf) | [`testakte-wandeldarlehen-beispielcase.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-wandeldarlehen-beispielcase.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Vollständiger Workflow-Assistent für den Lebenszyklus eines Wandeldarlehens bei GmbH und UG (haftungsbeschränkt) — von der ersten Mandatsbesprechung über Vertragsgestaltung (bilingual DE/EN oder einsprachig DE), Beurkundungsprüfung, Wandelereignisse und Wandlungsberechnung bis zum Cap-Table-Update, Gesellschafterbeschluss und Handelsregisteranmeldung durch den Notar.

## Lebenszyklus-Visualisierung

```
Phase A — Erstellung
  └─ Mandat-Triage → Parteien erfassen → Konditionen → Wandlungsmechanik
     → Rangrücktritt → Vertragserstellung (bilingual / einsprachig)
     → Vertraulichkeit und Sprachklausel

Phase B — Beurkundung und Unterzeichnung
  └─ Beurkundungserfordernis → Form (Textform/Schriftform/Notariell)
     → Formfehler-Heilungs-Timeline → DocuSign-Unterzeichnung
     → Gesellschafterbeschluss (Absicht) → KYC/AML

Phase C — Wandelereignisse und Wandlungsberechnung
  └─ Eingang Wandlungserklärung → Trigger-Dispatcher → Trigger-Prüfung
     (Qualified Financing / Maturity / Liquidation) → Wandlungspreis-Berechnung
     → Cap-Table Pre/Post → Dokumente-Extraktion
     → Ausschluss-Prüfung → Mehrere WD → Kommunikation

Phase D — Gesellschafterbeschluss und Notar
  └─ Gesellschafterversammlung einberufen → Beschluss Kapitalerhöhung
     → Sacheinlagebericht → Notar-Paket → Gesellschafterliste
     → HR-Anmeldung → Post-Eintragung-Checkliste
```

## Skills nach Phasen

### Phase A — Erstellung (8 Skills)

| Slug | Beschreibung |
|---|---|
| `mandat-triage-wandeldarlehen` | Erstgespräch: Rechtsform, Beteiligte, Wandelereignisse, Sprachen-Stack |
| `parteien-erfassen` | Gesellschaft, Gesellschafterinnen, Darlehensgeber, KYC, Vertretungsmacht |
| `darlehenshoehe-konditionen` | Darlehensbetrag, Laufzeit, Zinssatz, Auszahlung, Bankverbindung |
| `wandlungsmechanik-konzipieren` | Cap, Discount, Trigger-Logik, Wandlungsformel, MFN, Pro-rata |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `bilinguale-vertragserstellung` | Vollständiger Vertrag DE/EN zweispaltig, Sprachklausel |
| `einsprachige-vertragsfassung-de` | Einsprachige DE-Fassung, identischer materieller Inhalt |
| `vertraulichkeit-und-sprachklausel` | § 8 Vertraulichkeit, Sprachklausel, DIS-Schiedsklausel, salvatorische Klausel |

### Phase B — Beurkundung und Unterzeichnung (6 Skills)

| Slug | Beschreibung |
|---|---|
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `textform-vs-schriftform-vs-notariell` | § 126b/§ 126/§ 128 BGB, Formstufen, DocuSign-Praxis |
| `formfehler-heilungs-timeline` | Form-Stufen § 126b/§ 126/§ 128 BGB, Heilung durch nachfolgende Beurkundung § 15 Abs. 4 S. 2 GmbHG, Insolvenz-Risiko-Fenster |
| `unterzeichnung-elektronisch-docusign` | Authentifizierung, Audit Trail, zehn Jahre Archivierung § 147 AO |
| `gesellschafterbeschluss-vorbereiten` | Grundsatzbeschluss Kapitalerhöhungsbereitschaft, § 51 GmbHG |
| `kyc-aml-geldwaesche` | GwG KYC, wirtschaftlich Berechtigte, PEP, Sanktionslisten EU/OFAC/UN |

### Phase C — Wandelereignisse und Wandlungsberechnung (11 Skills)

| Slug | Beschreibung |
|---|---|
| `wandelereignis-eingang` | Eingang Wandlungserklärung, Vier-Augen-Prüfung, Eingangsbestätigung |
| `wandelereignis-trigger-dispatcher` | Master-Logik bei parallelen Triggern, Prioritäts-Regelung, Cap-Table-Simulation, MFN-Kaskade |
| `wandlungspruefung-trigger-qualified-financing` | Schwellentest, MIN-Methode Cap/Discount/Rundenpreis |
| `wandlungspruefung-trigger-maturity` | Laufzeitablauf, Fall-back-Bewertung, Wahlrecht Lender |
| `wandlungspruefung-trigger-liquidation` | Exit/Trade Sale/IPO, Liquidationspräferenz, Wahlrecht |
| `wandlungspreis-berechnung` | Vollständige Formel, Aufrundung § 5 GmbHG, Kapitalrücklage § 272 HGB |
| `cap-table-update-pre-post` | Pre-Money und Post-Money Cap-Table, Verwässerungsdarstellung |
| `dokumenten-upload-extraktion` | Term Sheet, SPA, IRA: relevante Zahlen extrahieren |
| `wandlungsausschluss-pruefung` | Verfristung, Verjährung, Verwirkung, Verzicht |
| `mehrere-wandeldarlehen-parallel` | Stack-Order, MFN, gleichzeitige Wandlung, kombinierter Cap-Table |
| `wandlung-kommunikation-paketverteilung` | Lender, Gesellschaft, Steuerberater, Buchhaltung informieren |

### Phase D — Gesellschafterbeschluss und Notar (7 Skills)

| Slug | Beschreibung |
|---|---|
| `gesellschafterversammlung-einberufen` | Einberufung, § 51 GmbHG, Ladungsfristen, Vollmacht, Notartermin |
| `gesellschafterbeschluss-kapitalerhoehung` | Beschluss Kapitalerhöhung gegen Sacheinlage, § 53 Abs. 2 GmbHG |
| `sacheinlagebericht-werthaltigkeit` | Werthaltigkeit Forderung, Differenzhaftung § 9 GmbHG, IDW RS HFA 42 |
| `notar-paket-uebermittlung` | Vollständigkeitscheckliste, Notar-Briefing, § 57 GmbHG-Anmeldung |
| `gesellschafterliste-aktualisieren` | § 40 GmbHG, Gutglaubenswirkung § 16 GmbHG, Transparenzregister |
| `handelsregisteranmeldung-kapitalerhoehung` | § 57 GmbHG, Bearbeitungsdauer, Beanstandungsgründe, § 19 GwG |
| `post-eintragung-checkliste` | Bestätigung, Steuer (§ 20 UmwStG), Sperrfrist § 22 UmwStG, Abschluss-Memo |

## Rechtsgrundlagen

| Bereich | Normen |
|---|---|
| GmbH-Gesellschaftsrecht | GmbHG §§ 1, 5, 5a, 15, 40, 46, 49–51, 53–57, 78 |
| Insolvenzrecht | InsO §§ 17, 19, 38, 39, 44, 15a, 15b |
| Zivilrecht / Form | BGB §§ 126, 126b, 128, 130, 194 ff., 311, 314, 397, 398, 488 ff. |
| Geldwäscherecht | GwG §§ 1–3, 10–13, 19, 43, 47, 56 |
| Handelsrecht | Normtext, Register-/Gesetzesquellen, bereitgestellte Materialien |
| Steuerrecht | UmwStG §§ 20, 22; EStG § 17; AO § 147 |
| Elektronische Signatur | eIDAS-VO 910/2014; Art. 26 ff. |
| Schiedsgerichtsbarkeit | DIS-Schiedsordnung 2018 |

## Verwendungsbeispiel

**Einstiegs-Prompt:**

> "Ich möchte ein Wandeldarlehen aufsetzen — was brauchst du von mir?"

Das Plugin startet mit `mandat-triage-wandeldarlehen` und führt durch:
1. Rechtsform und Parteien klären
2. Konditionen und Wandlungsmechanik festlegen
3. Vertrag erstellen (bilingual DE/EN oder nur DE)
4. Beurkundungserfordernis prüfen
5. DocuSign-Unterzeichnung koordinieren
6. Bei Wandlungsereignis: Trigger prüfen, Preis berechnen, Cap-Table aktualisieren
7. Gesellschafterbeschluss und Notarpaket erstellen
8. Handelsregisteranmeldung begleiten

## Wichtiger Hinweis

Alle Texte dienen als Arbeitshilfe für die anwaltliche Praxis. Sie ersetzen keine rechtliche Beratung im Einzelfall. Jeder Skill verweist auf die maßgebliche Rechtsprechung (BGH/OLG mit Aktenzeichen und Datum). Änderungen in GmbHG, InsO, UmwStG oder GwG sind einzuarbeiten (Stand: 05/2026).

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 28 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Wandeldarlehen Lebenszyklus-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arb... |
| `kompendium-01-workflow-chronologie-bis-workflow-fristen-und` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 01; bündelt 2 frühere Spezialskills (workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemu... |
| `kompendium-02-spezial-lebenszyklus-bis-bilinguale-vertragse` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 02; bündelt 2 frühere Spezialskills (spezial-lebenszyklus-fristen-form-und-zustaendigkeit, bilinguale-vertragserstellung) und bewahrt deren Workflows, Normanker, Prüfprogramme... |
| `kompendium-03-einsprachige-vertrag-bis-spezial-vertragserst` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 03; bündelt 2 frühere Spezialskills (einsprachige-vertragsfassung-de, spezial-vertragserstellung-behoerden-gericht-und-registerweg) und bewahrt deren Workflows, Normanker, Prüf... |
| `kompendium-04-vertraulichkeit-und-bis-beurkundungserforder` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 04; bündelt 2 frühere Spezialskills (vertraulichkeit-und-sprachklausel, beurkundungserfordernis-pruefung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-05-cap-table-update-pre-bis-darlehenshoehe-kondi` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 05; bündelt 2 frühere Spezialskills (cap-table-update-pre-post, darlehenshoehe-konditionen) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-06-dokumenten-upload-ex-bis-formfehler-heilungs` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 06; bündelt 2 frühere Spezialskills (dokumenten-upload-extraktion, formfehler-heilungs-timeline) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-07-gesellschafterbeschl-bis-gesellschafterbeschl` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 07; bündelt 2 frühere Spezialskills (gesellschafterbeschluss-kapitalerhoehung, gesellschafterbeschluss-vorbereiten) und bewahrt deren Workflows, Normanker, Prüfprogramme und Au... |
| `kompendium-08-gesellschafterliste-bis-gesellschafterversam` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 08; bündelt 2 frühere Spezialskills (gesellschafterliste-aktualisieren, gesellschafterversammlung-einberufen) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabem... |
| `kompendium-09-handelsregisteranmel-bis-kyc-aml-geldwaesche` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 09; bündelt 2 frühere Spezialskills (handelsregisteranmeldung-kapitalerhoehung, kyc-aml-geldwaesche) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-10-mandat-triage-wandel-bis-mehrere-wandeldarleh` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 10; bündelt 2 frühere Spezialskills (mandat-triage-wandeldarlehen, mehrere-wandeldarlehen-parallel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-11-notar-paket-uebermit-bis-parteien-erfassen` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 11; bündelt 2 frühere Spezialskills (notar-paket-uebermittlung, parteien-erfassen) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-12-post-eintragung-chec-bis-rangruecktritt-formu` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 12; bündelt 2 frühere Spezialskills (post-eintragung-checkliste, rangruecktritt-formulieren) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-13-sacheinlagebericht-w-bis-spezial-begleitet-er` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 13; bündelt 2 frühere Spezialskills (sacheinlagebericht-werthaltigkeit, spezial-begleitet-erstpruefung-und-mandatsziel) und bewahrt deren Workflows, Normanker, Prüfprogramme un... |
| `kompendium-14-spezial-bilingual-sc-bis-spezial-einsprachig` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 14; bündelt 2 frühere Spezialskills (spezial-bilingual-schriftsatz-brief-und-memo-bausteine, spezial-einsprachig-verhandlung-vergleich-und-eskalation) und bewahrt deren Workflo... |
| `kompendium-15-spezial-gmbh-risikoa-bis-spezial-vollstaendig` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 15; bündelt 2 frühere Spezialskills (spezial-gmbh-risikoampel-und-gegenargumente, spezial-vollstaendigen-tatbestand-beweis-und-belege) und bewahrt deren Workflows, Normanker, P... |
| `kompendium-16-spezial-wandeldarleh-bis-spezial-wandelereign` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 16; bündelt 2 frühere Spezialskills (spezial-wandeldarlehens-dokumentenmatrix-und-lueckenliste, spezial-wandelereignisse-zahlen-schwellen-und-berechnung) und bewahrt deren Work... |
| `kompendium-17-spezial-wandlungsaus-bis-textform-vs-schriftf` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 17; bündelt 2 frühere Spezialskills (spezial-wandlungsausloeser-cap-und-discount, textform-vs-schriftform-vs-notariell) und bewahrt deren Workflows, Normanker, Prüfprogramme un... |
| `kompendium-18-unterzeichnung-elekt-bis-wandelereignis-einga` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 18; bündelt 2 frühere Spezialskills (unterzeichnung-elektronisch-docusign, wandelereignis-eingang) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-19-wandelereignis-trigg-bis-wandlung-kommunikati` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 19; bündelt 2 frühere Spezialskills (wandelereignis-trigger-dispatcher, wandlung-kommunikation-paketverteilung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgab... |
| `kompendium-20-wandlungsausschluss-bis-wandlungsmechanik-ko` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 20; bündelt 2 frühere Spezialskills (wandlungsausschluss-pruefung, wandlungsmechanik-konzipieren) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-21-wandlungspreis-berec-bis-wandlungspruefung-tr` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 21; bündelt 2 frühere Spezialskills (wandlungspreis-berechnung, wandlungspruefung-trigger-liquidation) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-22-wandlungspruefung-tr-bis-wandlungspruefung-tr` | wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 22; bündelt 2 frühere Spezialskills (wandlungspruefung-trigger-maturity, wandlungspruefung-trigger-qualified-financing) und bewahrt deren Workflows, Normanker, Prüfprogramme un... |
| `spezial-beurkundungspruefung-livequellen-check` | Beurkundungspruefung: Livequellen- und Rechtsprechungscheck im Plugin wandeldarlehen lebenszyklus; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin wandeldarlehen-lebenszyklus: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin wandeldarlehen-lebenszyklus: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin wandeldarlehen-lebenszyklus: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin wandeldarlehen-lebenszyklus: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
