---
name: foreign-creditor-fraudulent-lbo-transfers
description: "Foreign Creditor Fraudulent LBO Transfers im Plugin Us Bankruptcy Code: prüft konkret Fuehrt deutsche Gläubiger durch US-Bankruptcy, Prueft leveraged buyout fraudulent-transfer exposure, solvency, reasonably equiv. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Foreign Creditor Fraudulent LBO Transfers

## Arbeitsbereich

**Foreign Creditor Fraudulent LBO Transfers** ordnet den Fall über die tragenden Prüffelder: Fuehrt deutsche Gläubiger durch US-Bankruptcy, Prueft leveraged buyout fraudulent-transfer exposure, solvency. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `foreign-creditor-german-client` | Fuehrt deutsche Gläubiger durch US-Bankruptcy: notice, claim, stay, contract, committee, plan vote and distributions. |
| `fraudulent-lbo` | Prueft leveraged buyout fraudulent-transfer exposure, solvency, reasonably equivalent value and lender/recipient targets. |
| `fraudulent-transfers-548` | Prueft actual and constructive fraudulent transfers, two-year lookback, value, insolvency and insider transactions. |
| `free-clear-sale-363f` | Prueft sale free and clear of interests, liens attaching to proceeds, consent, bona fide dispute and statutory bases. |

## Arbeitsweg

- Rolle und Ziel im US Bankruptcy Code Title 11: Chapters 7/9/11/12/13/15, Automatic Stay, Claims, DIP, 363 Sales, Plans und Cross-Border klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `foreign-creditor-german-client`

**Fokus:** Fuehrt deutsche Gläubiger durch US-Bankruptcy: notice, claim, stay, contract, committee, plan vote and distributions.

# Foreign Creditor German Client

## Fachkern: Foreign Creditor German Client
- **Spezialgegenstand:** Foreign Creditor German Client wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Foreign Creditor German Client** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. §§ 362, 501, 1126
- U.S. Courts forms
- Case docket/PACER


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- What notice received?
- Claim type and amount?
- Need local counsel?
- Contract or shipment pending?


## Workflow

1. Notice translate.
2. Claim and deadline map.
3. Stay-safe communication plan.


## Output

- German creditor memo
- Proof-of-claim checklist
- Plan voting note


## Tiefencheck für die Akte

Arbeite hier nicht nur abstrakt, sondern als strukturierter US-Counsel-Briefing-Filter:

- Welches ausländische Verfahren soll anerkannt werden und ist der foreign representative sauber legitimiert?
- Welche Tatsachen tragen COMI, establishment, foreign main/nonmain proceeding und notice?
- Welche relief wird sofort gebraucht: stay, discovery, asset turnover, cooperation, entrustment oder injunction?
- Gibt es public-policy, due-process, Datenschutz- oder Konzernstrukturthemen, die US-Counsel vorab kennen muss?

**Mindest-Output:** Chapter-15-Paket mit COMI-Belegen, Vertreterlegitimation, Relief-Liste und Notice-Plan.

## Qualitäts- und Risikofilter

- US-Bankruptcy ist Bundesrecht, aber Local Rules, Judges, District Practice und State-Law-Rechte bleiben entscheidend.
- Keine Einreichung, Fristberechnung oder strategische US-Prozessentscheidung ohne zugelassenen US-Bankruptcy-Counsel finalisieren.

- Unklare US-Rechtsfragen werden nicht als sicher verkauft, sondern als Issue List für US-Counsel markiert.
- Zahlen, Fristen, Fees, Formulare und Schwellenwerte werden vor konkreter Verwendung anhand offizieller aktueller Quellen geprüft.

## 2. `fraudulent-lbo`

**Fokus:** Prueft leveraged buyout fraudulent-transfer exposure, solvency, reasonably equivalent value and lender/recipient targets.

# Fraudulent Conveyance LBO

## Fachkern: Fraudulent Conveyance LBO
- **Spezialgegenstand:** Fraudulent Conveyance LBO wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Fraudulent Conveyance LBO** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. §§ 544, 548, 550
- State fraudulent transfer law
- Deal and solvency files


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Transaction structure?
- Solvency at closing?
- Who received value?


## Workflow

1. Funds flow map.
2. Solvency and value evidence.
3. Targets and defenses.


## Output

- LBO avoidance memo
- Funds-flow table
- Solvency evidence list


## Tiefencheck für die Akte

Arbeite hier nicht nur abstrakt, sondern als strukturierter US-Counsel-Briefing-Filter:

- Welche Zahlung, Übertragung oder Sicherheit liegt in welchem lookback period und zugunsten welcher Partei?
- War die Leistung antecedent debt, new value, ordinary course, contemporaneous exchange oder insider-bezogen?
- Welche State-law- oder bankruptcy-law avoidance route ist realistisch und wer trägt praktisch die Beweislast?
- Welche Verteidigungsakten fehlen noch: invoices, payment history, shipment logs, solvency material, board papers?

**Mindest-Output:** Avoidance-Analyse mit Transferliste, Zeitachse, Defenses, Vergleichswert und Litigation-Risiko.

## Qualitäts- und Risikofilter

- US-Bankruptcy ist Bundesrecht, aber Local Rules, Judges, District Practice und State-Law-Rechte bleiben entscheidend.
- Keine Einreichung, Fristberechnung oder strategische US-Prozessentscheidung ohne zugelassenen US-Bankruptcy-Counsel finalisieren.

- Unklare US-Rechtsfragen werden nicht als sicher verkauft, sondern als Issue List für US-Counsel markiert.
- Zahlen, Fristen, Fees, Formulare und Schwellenwerte werden vor konkreter Verwendung anhand offizieller aktueller Quellen geprüft.

## 3. `fraudulent-transfers-548`

**Fokus:** Prueft actual and constructive fraudulent transfers, two-year lookback, value, insolvency and insider transactions.

# Fraudulent Transfers § 548

## Fachkern: Fraudulent Transfers § 548
- **Spezialgegenstand:** Fraudulent Transfers § 548 wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Fraudulent Transfers § 548** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. § 548
- 11 U.S.C. § 550
- State fraudulent transfer law interface


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- What transfer/obligation?
- Actual intent badges?
- Reasonably equivalent value?
- Financial condition?


## Workflow

1. Transfer timeline.
2. Value and insolvency evidence.
3. State-law and § 544 overlay markieren.


## Output

- Fraudulent-transfer memo
- Badges table
- Recovery target list


## Tiefencheck für die Akte

Arbeite hier nicht nur abstrakt, sondern als strukturierter US-Counsel-Briefing-Filter:

- Welche Zahlung, Übertragung oder Sicherheit liegt in welchem lookback period und zugunsten welcher Partei?
- War die Leistung antecedent debt, new value, ordinary course, contemporaneous exchange oder insider-bezogen?
- Welche State-law- oder bankruptcy-law avoidance route ist realistisch und wer trägt praktisch die Beweislast?
- Welche Verteidigungsakten fehlen noch: invoices, payment history, shipment logs, solvency material, board papers?

**Mindest-Output:** Avoidance-Analyse mit Transferliste, Zeitachse, Defenses, Vergleichswert und Litigation-Risiko.

## Qualitäts- und Risikofilter

- US-Bankruptcy ist Bundesrecht, aber Local Rules, Judges, District Practice und State-Law-Rechte bleiben entscheidend.
- Keine Einreichung, Fristberechnung oder strategische US-Prozessentscheidung ohne zugelassenen US-Bankruptcy-Counsel finalisieren.

- Unklare US-Rechtsfragen werden nicht als sicher verkauft, sondern als Issue List für US-Counsel markiert.
- Zahlen, Fristen, Fees, Formulare und Schwellenwerte werden vor konkreter Verwendung anhand offizieller aktueller Quellen geprüft.

## 4. `free-clear-sale-363f`

**Fokus:** Prueft sale free and clear of interests, liens attaching to proceeds, consent, bona fide dispute and statutory bases.

# Free and Clear Sale § 363(f)

## Fachkern: Free and Clear Sale § 363(f)
- **Spezialgegenstand:** Free and Clear Sale § 363(f) wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Free and Clear Sale § 363(f)** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. § 363(f)
- 11 U.S.C. § 363(m)
- Sale order practice


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- What interests attach?
- Which § 363(f) ground for each?
- Good-faith purchaser issues?


## Workflow

1. Interest/lien schedule bauen.
2. Basis per interest prüfen.
3. Order language and appeal risk markieren.


## Output

- Free-and-clear matrix
- Sale order issue list
- Appeal-risk memo


## Tiefencheck für die Akte

Arbeite hier nicht nur abstrakt, sondern als strukturierter US-Counsel-Briefing-Filter:

- Ist ein § 363 sale wirklich schneller und besser als plan sale, workout oder going-concern financing?
- Welche assets, liens, cure amounts, executory contracts, approvals und buyer protections sind betroffen?
- Sind bidding procedures, break-up fee, credit bid, adequate notice und good-faith finding sauber vorbereitet?
- Welche deutschen Beteiligten brauchen Übersetzung: Käufer, Verkäufer, Kreditgeber, Betriebsrat, Datenschutz, Kartellrecht?

**Mindest-Output:** Sale-Chart mit assets, liens, bidder protections, objections, approvals und closing deliverables.

## Qualitäts- und Risikofilter

- US-Bankruptcy ist Bundesrecht, aber Local Rules, Judges, District Practice und State-Law-Rechte bleiben entscheidend.
- Keine Einreichung, Fristberechnung oder strategische US-Prozessentscheidung ohne zugelassenen US-Bankruptcy-Counsel finalisieren.

- Unklare US-Rechtsfragen werden nicht als sicher verkauft, sondern als Issue List für US-Counsel markiert.
- Zahlen, Fristen, Fees, Formulare und Schwellenwerte werden vor konkreter Verwendung anhand offizieller aktueller Quellen geprüft.
