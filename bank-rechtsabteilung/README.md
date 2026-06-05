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
| **Meridian MedTech: Insiderrecht, Ad-hoc und M&A-Leak** (`insiderrecht-meridian-medtech-ad-hoc-ma-leak`) | [Gesamt-PDF lesen](../testakten/insiderrecht-meridian-medtech-ad-hoc-ma-leak/gesamt-pdf/insiderrecht-meridian-medtech-ad-hoc-ma-leak_gesamt.pdf) | [`testakte-insiderrecht-meridian-medtech-ad-hoc-ma-leak.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-insiderrecht-meridian-medtech-ad-hoc-ma-leak.zip) |
| **Akte Rotorwerk: Maschinenleasing, Restwert und Insolvenzgerücht** (`leasingrecht-maschinenfleet-restwert-insolvenz`) | [Gesamt-PDF lesen](../testakten/leasingrecht-maschinenfleet-restwert-insolvenz/gesamt-pdf/leasingrecht-maschinenfleet-restwert-insolvenz_gesamt.pdf) | [`testakte-leasingrecht-maschinenfleet-restwert-insolvenz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-leasingrecht-maschinenfleet-restwert-insolvenz.zip) |
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
| `agb-bankrecht-organhaftung-business` | AGB Bankrecht Organhaftung Business im Plugin Bank Rechtsabteilung: prüft konkret AGB-Recht für Banken, Organhaftung und Business Judgment Rule in der Bank, Sanktionsscreening und Embargo in der Bank, Krypto-Steuerreporting. Liefert prio... |
| `app-fraud-aufsichtsrat-vorlage` | APP Fraud Aufsichtsrat Vorlage im Plugin Bank Rechtsabteilung: prüft konkret APP-Fraud, PushTAN und Social Engineering aus Bankensicht prüfen, Aufsichtsrats- und Ausschussvorlagen einer Bank vorbereiten, Avalrahmen und Kautionsaval in de... |
| `bank-rechtsabteilung-kaltstart-triage` | Agb Bankrecht Klauselkontrolle, Anwaltliche Rechnungen Review, App Fraud Social Engineering Bank, Aufsichtsrat Vorlage Bank: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten b... |
| `bankaufsichtsrecht-kwg-bankgeheimnis` | Bankaufsichtsrecht KWG Bankgeheimnis im Plugin Bank Rechtsabteilung: prüft konkret Bankaufsichtsrechtliche Ersttriage nach KWG und MaRisk, Auskunftsersuchen an Banken prüfen, White-Label-Banking juristisch strukturieren, Beteiligungserwe... |
| `bankrechtsabteilung-kaltstart-routing` | Kaltstart-Routing für neue Inhouse-Anfragen in einer Bank: Sachgebiet erkennen, Eilbedarf markieren, BaFin-, Vorstand-, Kredit-, Vertrieb-, AGB-, Datenschutz- oder Prozesspfad wählen und genau die nächsten Unterlagen anfordern. |
| `blockchain-settlement-buergschaft-erste` | Blockchain Settlement Buergschaft Erste im Plugin Bank Rechtsabteilung: prüft konkret Blockchain-Settlement und Delivery-versus-Payment prüfen, Bürgschaft oder Garantie auf erste Anforderung aus, Privatpersonen-, Gesellschafter- und Eheg... |
| `covenant-waiver-crr-crd-kapitalanforderungen` | Covenant Waiver CRR CRD Kapitalanforderungen im Plugin Bank Rechtsabteilung: prüft konkret Covenant Waiver und Kreditdokumentation tief prüfen, CRR-, CRD- und Großkredit-Schnittstelle für Juristen, CRR-Juristenmatrix für Bank-Legal. Lief... |
| `datenschutz-bankgeheimnis-depotrecht` | Datenschutz Bankgeheimnis Depotrecht im Plugin Bank Rechtsabteilung: prüft konkret Datenschutz, Bankgeheimnis und Mandatsgeheimnis in der Bank, Depotrecht und tokenisierte Wertpapiere prüfen, DLT Pilot Regime für Marktinfrastrukturen prü... |
| `dora-ict-einlagensicherung-kundenhinweise` | Dora ICT Einlagensicherung Kundenhinweise im Plugin Bank Rechtsabteilung: prüft konkret DORA-IKT-Verträge und IKT-Vorfälle, Einlagensicherung und Kundenhinweise, Embedded-Finance-Kooperationen prüfen, ESG und Sustainable Finance in der B... |
| `ewpg-kryptowertpapierregister-registerwechsel` | Ewpg Kryptowertpapierregister Registerwechsel im Plugin Bank Rechtsabteilung: prüft konkret Kryptowertpapierregisterführung nach eWpG und KWG prüfen, Registerwechsel, Registerfehler und Anlegerrechte bei elektronischen, Fit-and-Proper-Ei... |
| `garantieabruf-missbrauch-garantieprovision` | Garantieabruf Missbrauch Garantieprovision im Plugin Bank Rechtsabteilung: prüft konkret Abruf aus Bankgarantie, Aval oder Bürgschaft auf erstes Anfordern im Eilfall ste, Aval- und Garantiegeschäft wirtschaftlich-juristisch steuern, Kund... |
| `geldwaesche-krypto-geschaeftsleiter` | Geldwaesche Krypto Geschaeftsleiter im Plugin Bank Rechtsabteilung: prüft konkret Krypto-AML und Wallet-Screening für Banken prüfen, Abberufung, Suspendierung oder Ressortentzug von Geschäftsleitern in, Geschäftsleiterbestellung nach KWG... |
| `handelsvertreter-vertriebsrecht` | Handelsvertreter Vertriebsrecht im Plugin Bank Rechtsabteilung: prüft konkret Handelsvertreter- und Vertriebsrecht für Banken, Hauptversammlung einer Bank rechtlich vorbereiten, Verification of Payee und IBAN-Name-Check prüfen, Inhaberko... |
| `instant-payments-interne-richtlinie-it` | Instant Payments Interne Richtlinie IT im Plugin Bank Rechtsabteilung: prüft konkret Instant Payments und SEPA-Echtzeitüberweisungen prüfen, Interne Richtlinien und Policies für Banken entwerfen, IT-Sicherheit und Cloud-Verträge einer Ba... |
| `kreditsicherheiten-bestellung` | Kreditsicherheiten Bestellung im Plugin Bank Rechtsabteilung: prüft konkret Kreditsicherheiten bestellen, prüfen und verwerten, KWG-Erlaubnis, Erlaubniserweiterung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächste... |
| `micar-art-emt-casp-notifikation-whitepaper` | Micar ART EMT Casp Notifikation Whitepaper im Plugin Bank Rechtsabteilung: prüft konkret ART- und EMT-Emission nach MiCAR für Banken prüfen, MiCAR-CASP-Notifikation für Banken nach Art, MiCAR-Whitepaper und Marketing für Kryptowerte prüf... |
| `outsourcing-operational-resilience-crypto-dlt` | Outsourcing Operational Resilience Crypto DLT im Plugin Bank Rechtsabteilung: prüft konkret Operational Resilience und Konzentrationsrisiken bei, Crypto-/DLT-Dienstleister und Node Provider auslagern, Externe Dienstleister außerhalb rein... |
| `produktfreigabe-new-restrukturierung` | Produktfreigabe NEW Restrukturierung im Plugin Bank Rechtsabteilung: prüft konkret New Product Process einer Bank, Restrukturierung eines Kreditengagements steuern, Anwaltliche Rechnungen und Kanzlei-Budgets reviewen, Anzahlungs-. Liefer... |
| `psd2-provisionsmodelle-vertrieb-fraud-refund` | Psd2 Provisionsmodelle Vertrieb Fraud Refund im Plugin Bank Rechtsabteilung: prüft konkret Provisionsmodelle und Vertriebscompliance prüfen, Unautorisierte Zahlung und Refund nach PSD2/BGB prüfen, Open-Banking- und XS2A-Schnittstellen pr... |
| `rechtsabteilung-dora-auslagerung-ewpg` | Dora Auslagerung Ewpg im Plugin Bank Rechtsabteilung: prüft konkret Rechtsabteilungs-Fachmodul für DORA-Auslagerung bei, Rechtsabteilungs-Fachmodul für eWpG-Tokenisierung und, Rechtsabteilungs-Fachmodul für NPL-Verkauf mit Datenschutz, R... |
| `rechtsmonitoring-bank-regress` | Rechtsmonitoring Bank Regress im Plugin Bank Rechtsabteilung: prüft konkret Rechtsmonitoring für Banken einrichten, Regress nach Bürgschafts-, Aval- oder Garantiezahlung prüfen, Eingehende Sanierungsgutachten nach IDW S 6 aus. Liefert pr... |
| `ssm-bundesbank-stablecoin-payment-staking` | SSM Bundesbank Stablecoin Payment Staking im Plugin Bank Rechtsabteilung: prüft konkret SSM-, EZB- und Bundesbank-Aufsichtsbriefe für Institute einordnen, Stablecoin-Zahlungsusecase für Banken prüfen, Staking. Liefert priorisierten Outpu... |
| `syndizierte-kredite-tokenisierung-security` | Syndizierte Kredite Tokenisierung Security im Plugin Bank Rechtsabteilung: prüft konkret Syndizierte Kredite, Facility Agent und Security Trustee prüfen, Tokenisierung und Security Token einordnen, Trade Finance. Liefert priorisierten Ou... |
| `zag-bafin-merkblatt-payment-flow-red-team` | ZAG-Red-Team nach BaFin-Arbeitslogik: Zahlungsfluss, Positivkatalog, Ausnahmen, E-Geld, Erlaubnis, Registrierung und Anzeigen so prüfen, dass Plattform-, Wallet-, Loyalty-, Agenten- und Embedded-Finance-Modelle nicht falsch freigegeben w... |
| `zag-erlaubnisanalyse` | ZAG Erlaubnisanalyse im Plugin Bank Rechtsabteilung: prüft konkret ZAG-Erlaubnisanalyse für Zahlungsinstitute, Finanztransfergeschäft und Money Remittance nach ZAG prüfen, Kontoinformationsdienst nach ZAG und PSD2 prüfen, ZAG-Negativausk... |
| `zag-vorstandsvorlage-gutachten-wpig` | ZAG Vorstandsvorlage Gutachten Wpig im Plugin Bank Rechtsabteilung: prüft konkret Vorstandsvorlage und juristisches Gutachten für eine Bank, WpIG-Schnittstellen prüfen, wenn Bankgruppe, Wertpapierinstitut. Liefert priorisierten Output mi... |
| `zahlungsdienste-zag` | Zahlungsdienste ZAG im Plugin Bank Rechtsabteilung: fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
