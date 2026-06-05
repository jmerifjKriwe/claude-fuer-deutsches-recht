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
| `agb-bankrecht-organhaftung-business` | AGB Bankrecht Organhaftung Business: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `app-fraud-aufsichtsrat-vorlage` | APP Fraud Aufsichtsrat Vorlage: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `bank-rechtsabteilung-kaltstart-triage` | Agb Bankrecht Klauselkontrolle, Anwaltliche Rechnungen Review, App Fraud Social Engineering Bank, Aufsichtsrat Vorlage Bank: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten b... |
| `bankaufsichtsrecht-kwg-bankgeheimnis` | Bankaufsichtsrecht KWG Bankgeheimnis: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `bankrechtsabteilung-kaltstart-routing` | Kaltstart-Routing für neue Inhouse-Anfragen in einer Bank: Sachgebiet erkennen, Eilbedarf markieren, BaFin-, Vorstand-, Kredit-, Vertrieb-, AGB-, Datenschutz- oder Prozesspfad wählen und genau die nächsten Unterlagen anfordern. |
| `blockchain-settlement-buergschaft-erste` | Blockchain Settlement Buergschaft Erste: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `covenant-waiver-crr-crd-kapitalanforderungen` | Covenant Waiver CRR CRD Kapitalanforderungen: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `datenschutz-bankgeheimnis-depotrecht` | Datenschutz Bankgeheimnis Depotrecht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `dora-ict-einlagensicherung-kundenhinweise` | Dora ICT Einlagensicherung Kundenhinweise: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `ewpg-kryptowertpapierregister-registerwechsel` | Ewpg Kryptowertpapierregister Registerwechsel: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `garantieabruf-missbrauch-garantieprovision` | Garantieabruf Missbrauch Garantieprovision: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `geldwaesche-krypto-geschaeftsleiter` | Geldwaesche Krypto Geschaeftsleiter: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `handelsvertreter-vertriebsrecht` | Handelsvertreter Vertriebsrecht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `instant-payments-interne-richtlinie-it` | Instant Payments Interne Richtlinie IT: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kreditsicherheiten-bestellung` | Kreditsicherheiten Bestellung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `micar-art-emt-casp-notifikation-whitepaper` | Micar ART EMT Casp Notifikation Whitepaper: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `outsourcing-operational-resilience-crypto-dlt` | Outsourcing Operational Resilience Crypto DLT: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `produktfreigabe-new-restrukturierung` | Produktfreigabe NEW Restrukturierung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `psd2-provisionsmodelle-vertrieb-fraud-refund` | Psd2 Provisionsmodelle Vertrieb Fraud Refund: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `rechtsabteilung-dora-auslagerung-ewpg` | Dora Auslagerung Ewpg: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `rechtsmonitoring-bank-regress` | Rechtsmonitoring Bank Regress: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `ssm-bundesbank-stablecoin-payment-staking` | SSM Bundesbank Stablecoin Payment Staking: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `syndizierte-kredite-tokenisierung-security` | Syndizierte Kredite Tokenisierung Security: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `zag-bafin-merkblatt-payment-flow-red-team` | ZAG-Red-Team nach BaFin-Arbeitslogik: Zahlungsfluss, Positivkatalog, Ausnahmen, E-Geld, Erlaubnis, Registrierung und Anzeigen so prüfen, dass Plattform-, Wallet-, Loyalty-, Agenten- und Embedded-Finance-Modelle nicht falsch freigegeben w... |
| `zag-erlaubnisanalyse` | ZAG Erlaubnisanalyse: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `zag-vorstandsvorlage-gutachten-wpig` | ZAG Vorstandsvorlage Gutachten Wpig: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `zahlungsdienste-zag` | Zahlungsdienste ZAG: bearbeitet den maßgeblichen Prüfpfad und erzeugt den nächsten belastbaren Output im Mandat. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
