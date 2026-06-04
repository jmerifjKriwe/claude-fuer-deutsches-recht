# Bank-Rechtsabteilung

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`bank-rechtsabteilung`) | [`bank-rechtsabteilung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bank-rechtsabteilung.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Märkische Reserve Süd — Batteriespeicher Brandenburg/Berlin** (`batteriespeicher-brandenburg-berlin-resilienz`) | [Gesamt-PDF lesen](../testakten/batteriespeicher-brandenburg-berlin-resilienz/gesamt-pdf/batteriespeicher-brandenburg-berlin-resilienz_gesamt.pdf) | [`testakte-batteriespeicher-brandenburg-berlin-resilienz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-batteriespeicher-brandenburg-berlin-resilienz.zip) |
| **Projekt Nachtfalter — Private Equity Buyout, Schuldschein und NPL-Portfolio** (`private-equity-buyout-schuldschein-npl-heidelberg`) | [Gesamt-PDF lesen](../testakten/private-equity-buyout-schuldschein-npl-heidelberg/gesamt-pdf/private-equity-buyout-schuldschein-npl-heidelberg_gesamt.pdf) | [`testakte-private-equity-buyout-schuldschein-npl-heidelberg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-private-equity-buyout-schuldschein-npl-heidelberg.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Rechtsabteilungs-Plugin für eine mittelgroße deutsche Bank: schnell genug für den internen Ticketkanal, sorgfältig genug für Vorstand, Aufsichtsrat, BaFin, Bundesbank, externe Kanzleien und späteren Aktenrückblick.

Es ist als Inhouse-Cockpit gedacht: nicht nur Bankrecht im engeren Sinn, sondern der ganze Alltag einer Bank-Rechtsabteilung. Aufsichtsrecht, Kredit, Avalrahmen, Bürgschaften, Bankgarantien, Akkreditive, Sanierung, Auslagerung, DORA, Geldwäsche, AGB, Handelsvertreter, Vertrieb, Beschwerden, Organvorlagen, Hauptversammlung, Beteiligungen, Datenschutz, Kanzleisteuerung und Rechnungsreview werden in einen einzigen Routing-Workflow gebracht. Die Spezialerweiterung deckt zusätzlich ZAG-Finanztransfer, PSD2/Open Banking, PSD3/PSR-Vorschau, eWpG, Kryptowertpapierregister, MiCAR, Tokenisierung, Instant Payments und digitale Bankprodukte ab. Der Aufsichtsrechtskern wurde um eine BaFin-/Gesetze-/EUR-Lex-gestützte Arbeitslogik für ZAG, DORA Artikel 16, AnzV, InhKontrollV und CRR erweitert.

## Für wen

| Rolle | Typische Nutzung |
| --- | --- |
| General Counsel / Chefjustiziar | Vorstandsvorlagen, Aufsichtsrat, Eskalation, Kanzleisteuerung |
| Syndikus in Legal | Gutachten, Vertragscheck, Fachbereichsberatung, BaFin-Antworten |
| Compliance / AML / Datenschutz | GwG, Sanktionen, DORA, Richtlinien, Meldungen, Findings |
| Marktfolge / Risk / Workout | Weiterfinanzierung, Stundung, Sanierungsgutachten, Sicherheiten |
| Trade Finance / Firmenkunden | Avale, Kautionsavale, Garantien, Akkreditive, Dokumenteninkasso, Abruf- und Regressfälle |
| Vorstandsreferat | Beschlussvorschläge, Q&A, HV- und Ausschussunterlagen |

## Kaltstart

Beginne mit:

```text
/bank-rechtsabteilung:allgemein
```

Der Einstieg fragt nicht erst einen langen Fragebogen ab, sondern sortiert sofort:

- Was liegt vor?
- Wer braucht das Ergebnis?
- Gibt es eine Frist oder Aufsichtsdruck?
- Ist es Kredit, Aufsicht, Vertrieb, Organ, Vertrag, Datenschutz, Litigation oder Dienstleistersteuerung?
- Welcher Spezial-Skill passt jetzt wirklich?

Wenn nur ein Dokument hochgeladen wird, behandelt der Allgemein-Skill das als Arbeitsauftrag: Fristen erkennen, Material klassifizieren, Risikoampel bauen, passenden Spezial-Skill vorschlagen oder direkt einen ersten verwertbaren Entwurf schreiben.

## Normen- und Quellenhygiene

Das Plugin ist bewusst quellenstrikt. Es soll keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate produzieren. Für tragende Aussagen sind Live-Checks gegen amtliche oder frei zugängliche Quellen vorgesehen, insbesondere:

- Gesetze im Internet: KWG, ZAG, WpHG, GwG, HGB, BGB, AktG.
- BaFin: MaRisk, DORA-Informationen, Merkblätter, Rundschreiben und Aufsichtsmitteilungen.
- Bundesbank, EZB/SSM, EBA und EUR-Lex für europäische Aufsichtsakte und Leitlinien.
- Gerichtsentscheidungen nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier oder amtlicher Quelle.

Siehe auch [`references/QUELLEN.md`](./references/QUELLEN.md).

## Typische Workflows

Die erste Ausbaustufe deckt den Alltag der Rechtsabteilung ab; die zweite Ausbaustufe geht tief in Zahlungsdienste, Geschäftsleiteranzeigen, elektronische Wertpapiere und Tokenisierung.


| Workflow | Start-Skill | Ergebnis |
| --- | --- | --- |
| BaFin-Schreiben liegt vor | `bafin-kommunikation-und-anhoerung` | Antwortarchitektur, Tatsachenmatrix, Freigabekette |
| Cloud-Vertrag soll freigegeben werden | `dora-ict-vertraege-vorfall` | DORA-/Auslagerungscheck, Klausellücken, Exit-Fragen |
| Kreditnehmer braucht Stundung | `stundung-standstill-waiver` | Term Sheet, Conditions, Sicherheiten- und Anfechtungsampel |
| Kunde braucht Kautions- oder Anzahlungsaval | `avalrahmenlinie-kautionsaval-praxis` | Avalfreigabe, Textänderungen, Limit-/Regresscheck |
| Begünstigter zieht Garantie | `garantieabruf-missbrauch-und-zahlungsstopp` | Pay/Hold/Reject-Entscheidung, Eilkommunikation, Regressplan |
| Bürgschaft auf erstes Anfordern liegt vor | `buergschaft-auf-erste-anforderung-bank` | Textauslegung, Abrufprüfung, Missbrauchsampel |
| Firmenkunde braucht Liquiditätsbrücke | `liquiditaetsbruecke-firmenkunde-bankinstrumente` | Instrumentenvergleich Aval, Linie, Factoring, Akkreditiv, Waiver |
| Sanierungsgutachten kommt rein | `sanierungsgutachten-idw-s6-bewertung` | Plausibilitätsreview, Red Flags, Nachforderungsliste |
| Vorstand braucht Vorlage | `vorstandsvorlage-gutachten` | Executive Summary, Optionen, Beschlussvorschlag |
| Kanzleirechnung ist zu hoch | `anwaltliche-rechnungen-review` | Rechnungsprüfung, Rückfragen, Kürzungsvorschlag |
| Handelsvertreter kündigt | `handelsvertreter-vertriebsrecht-bank` | Statusanalyse, Ausgleichsrisiko, Verhandlungsposition |
| AGB sollen geändert werden | `agb-bankrecht-klauselkontrolle` | Klauselampel, bessere Fassung, Rollout-Hinweise |
| Zahlungsmodell ist aufsichtsrechtlich unklar | `zag-bafin-merkblatt-payment-flow-red-team` | Flow-of-Funds, ZAG-Positivkatalog, Ausnahmen, BaFin-Red-Team |
| Kleines Finanzunternehmen will DORA pragmatisch umsetzen | `dora-art16-vereinfachter-ikt-rahmen` | Art.-16-Scope, Governance, Drittparteien, Nachweisordner |
| KWG-Anzeigen laufen quer durch HR, Legal und Vorstandsbüro | `anzv-kwg-anzeigenkalender-bafin-bundesbank` | Anzeigenkalender, Unterlagen, Einreichweg, Nachforderungslog |
| Bankbeteiligung soll erworben oder erhöht werden | `inhkontrollv-bedeutende-beteiligung-bank` | Schwellen, Erwerberkette, Finanzierung, Closing-CP |
| Kredit-/Beteiligungsfall hat Kapital- oder Großkreditfolgen | `crr-kapitalanforderungen-juristenmatrix` | Legal/Risk-Matrix, CRR-Fragen, Vorstandsvorlage |

## Installation in Claude Code / Cowork

1. ZIP aus dem Release herunterladen.
2. In Claude Code / Cowork unter **Customize Plugins** das ZIP installieren.
3. `bank-rechtsabteilung` aktivieren und mit `/bank-rechtsabteilung:allgemein` starten.

> Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/` und `references/` im ZIP-Root enthalten. Nicht das komplette Repository-ZIP aus GitHub verwenden.

## Enthaltene Skills

Die vollständige Skill-Liste wird automatisch am Ende dieser README aktualisiert.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 27 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg und Chefjustiziar-Workflow für die Rechtsabteilung einer mittelgroßen deutschen Bank. Fragt Rolle, Ziel, Fristen, Dokumente, Aufsichtsrisiko, Kreditrisiko, Organbedarf und gewünschten Output ab und routet in passende Bank-Skills. |
| `bankrechtsabteilung-kaltstart-routing` | Kaltstart-Routing für neue Inhouse-Anfragen in einer Bank: Sachgebiet erkennen, Eilbedarf markieren, BaFin-, Vorstand-, Kredit-, Vertrieb-, AGB-, Datenschutz- oder Prozesspfad wählen und genau die nächsten Unterlagen anfordern. |
| `kompendium-01-agb-bankrecht-klause-bis-externe-anwaelte-ste` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 01; bündelt 5 frühere Spezialskills (agb-bankrecht-klauselkontrolle, organhaftung-business-judgment, sanktionsscreening-embargo-bank, crypto-tax-reporting-dac8-car, externe-anwaelte-s... |
| `kompendium-02-garantieabruf-missbr-bis-organwechsel-ssm-ima` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 02; bündelt 5 frühere Spezialskills (garantieabruf-missbrauch-und-zahlungsstopp, garantieprovision-limit-und-risk-weighting, kundenbeschwerde-ombudsmann-bafin, litigation-schlichtung-... |
| `kompendium-03-produktfreigabe-new-bis-anzv-kwg-anzeigenkal` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 03; bündelt 5 frühere Spezialskills (produktfreigabe-new-product-process, restrukturierung-kreditengagement, anwaltliche-rechnungen-review, anzahlungs-gewaehrleistungs-und-erfuellungs... |
| `kompendium-04-app-fraud-social-eng-bis-bafin-pruefung-vor-o` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 04; bündelt 5 frühere Spezialskills (app-fraud-social-engineering-bank, aufsichtsrat-vorlage-bank, avalrahmenlinie-kautionsaval-praxis, bafin-kommunikation-und-anhoerung, bafin-pruefu... |
| `kompendium-05-bankaufsichtsrecht-k-bis-betriebsrat-change-p` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 05; bündelt 5 frühere Spezialskills (bankaufsichtsrecht-kwg-marisk-triage, bankgeheimnis-auskunftsersuchen, banking-as-a-service-white-label, beteiligungserwerb-bank-ma, betriebsrat-c... |
| `kompendium-06-blockchain-settlemen-bis-correspondent-bankin` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 06; bündelt 5 frühere Spezialskills (blockchain-settlement-dvp, buergschaft-auf-erste-anforderung-bank, buergschaft-privatperson-gesellschafter-ehegatte, chargeback-card-schemes-bankr... |
| `kompendium-07-covenant-waiver-cred-bis-datenraum-bank-trans` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 07; bündelt 5 frühere Spezialskills (covenant-waiver-credit-documentation, crr-crd-eigenmittel-large-exposure, crr-kapitalanforderungen-juristenmatrix, darlehensrecht-verbraucher-unte... |
| `kompendium-08-datenschutz-bankgehe-bis-dora-art16-vereinfac` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 08; bündelt 5 frühere Spezialskills (datenschutz-bankgeheimnis, depotrecht-tokenisierte-wertpapiere, dlt-pilot-regime-market-infrastructure, dokumentengeschaeft-akkreditiv-inkasso-sta... |
| `kompendium-09-dora-ict-vertraege-v-bis-ewpg-emission-elektr` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 09; bündelt 5 frühere Spezialskills (dora-ict-vertraege-vorfall, einlagensicherung-kundenhinweise, embedded-finance-kooperation, esg-sustainable-finance, ewpg-emission-elektronische-w... |
| `kompendium-10-ewpg-kryptowertpapie-bis-forbearance-npe-risi` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 10; bündelt 5 frühere Spezialskills (ewpg-kryptowertpapierregister-erlaubnis, ewpg-registerwechsel-registerfehler, fit-proper-eignungsmatrix-deep-dive, fit-proper-organe-mitarbeiter,... |
| `kompendium-11-geldwaesche-krypto-w-bis-gwg-aml-kyc-verdacht` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 11; bündelt 5 frühere Spezialskills (geldwaesche-krypto-wallet-screening, geschaeftsleiter-abberufung-krise, geschaeftsleiter-bestellung-kwg-zag, girokonto-firmenkunden-risk-exit, gwg... |
| `kompendium-12-handelsvertreter-ver-bis-insolvenz-anfechtung` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 12; bündelt 5 frühere Spezialskills (handelsvertreter-vertriebsrecht-bank, hauptversammlung-bank-aktg, iban-name-check-verification-payee, inhkontrollv-bedeutende-beteiligung-bank, in... |
| `kompendium-13-instant-payments-sep-bis-kreditentscheidung-w` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 13; bündelt 5 frühere Spezialskills (instant-payments-sepa-vo, interne-richtlinie-policy-drafting, it-sicherheit-cloud-vertraege, kontokuendigung-sperre-basiskonto, kreditentscheidung... |
| `kompendium-14-kreditsicherheiten-b-bis-marisk-auslagerungen` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 14; bündelt 5 frühere Spezialskills (kreditsicherheiten-bestellung-verwertung, kreditwesengesetz-erlaubnis-inhaberkontrolle, liquiditaetsbruecke-firmenkunde-bankinstrumente, ma-risk-c... |
| `kompendium-15-micar-art-emt-bank-e-bis-notfallplan-krisenko` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 15; bündelt 5 frühere Spezialskills (micar-art-emt-bank-emission, micar-casp-notifikation-bank-art60, micar-whitepaper-marketing-bank, mifid-wphg-anlageberatung, notfallplan-krisenkom... |
| `kompendium-16-operational-resilien-bis-pfandbriefbank-spezi` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 16; bündelt 5 frühere Spezialskills (operational-resilience-concentration-risk, outsourcing-crypto-dlt-node-provider, outsourcing-externe-dienstleister, outsourcing-fintech-bank-as-a-... |
| `kompendium-17-provisionsmodelle-ve-bis-psd3-psr-vorschau-ga` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 17; bündelt 5 frühere Spezialskills (provisionsmodelle-vertrieb-compliance, psd2-fraud-refund-unauthorised-payment, psd2-open-banking-api-xs2a, psd2-sca-strong-customer-authentication... |
| `kompendium-18-rechtsabteilung-dora-bis-rechtsabteilung-schu` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 18; bündelt 5 frühere Spezialskills (rechtsabteilung-dora-auslagerung-bei-kritischem-ict-dienstleiste, rechtsabteilung-ewpg-tokenisierung-und-registerrisiko, rechtsabteilung-npl-verka... |
| `kompendium-19-rechtsmonitoring-ban-bis-sepa-direct-debit-re` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 19; bündelt 5 frühere Spezialskills (rechtsmonitoring-bank, regress-forderungsuebergang-und-sicherheitenfreigabe, sanierungsgutachten-idw-s6-bewertung, schluesselfunktionen-inhaber-fi... |
| `kompendium-20-ssm-bundesbank-aufsi-bis-sustainability-linke` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 20; bündelt 5 frühere Spezialskills (ssm-bundesbank-aufsichtsbrief, stablecoin-payment-usecase-bank, staking-lending-token-bank, stundung-standstill-waiver, sustainability-linked-loan... |
| `kompendium-21-syndizierte-kredite-bis-verwahrung-kryptower` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 21; bündelt 5 frühere Spezialskills (syndizierte-kredite-agent-security-trustee, tokenisierung-security-token-mica-mifid, trade-finance-sanctions-lc-guarantee, travel-rule-krypto-tran... |
| `kompendium-22-vorstandsvorlage-gut-bis-zag-e-geld-institut` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 22; bündelt 5 frühere Spezialskills (vorstandsvorlage-gutachten, wpig-wertpapierinstitut-schnittstelle, zag-agenten-auslagerung-register, zag-ausnahmen-limited-network-commercial-agen... |
| `kompendium-23-zag-erlaubnisanalyse-bis-zag-zahlungsausloese` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 23; bündelt 5 frühere Spezialskills (zag-erlaubnisanalyse-payment-institution, zag-finanztransfergeschaeft-money-remittance, zag-kontoinformationsdienst-ais, zag-negativauskunft-fests... |
| `kompendium-24-zahlungsdienste-zag-bis-zahlungsdienste-zag` | bank-rechtsabteilung: Konsolidiertes Skill-Kompendium 24; bündelt 1 frühere Spezialskills (zahlungsdienste-zag-psd3-psr) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `zag-bafin-merkblatt-payment-flow-red-team` | ZAG-Red-Team nach BaFin-Arbeitslogik: Zahlungsfluss, Positivkatalog, Ausnahmen, E-Geld, Erlaubnis, Registrierung und Anzeigen so prüfen, dass Plattform-, Wallet-, Loyalty-, Agenten- und Embedded-Finance-Modelle nicht falsch freigegeben w... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
