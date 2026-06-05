---
name: postpetition-transfers-preference-ordinary
description: "Postpetition Transfers Preference Ordinary im Plugin Us Bankruptcy Code: prüft konkret Prueft unauthorized postpetition transfers, ordinary course, court authorization, Prueft ordinary-course. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Postpetition Transfers Preference Ordinary

## Arbeitsbereich

Dieser Skill behandelt **Postpetition Transfers Preference Ordinary** als zusammenhängenden Arbeitsgang im Plugin Us Bankruptcy Code. Im Mittelpunkt steht die Prüfung von Prueft unauthorized postpetition transfers, ordinary course, court authorization und weiteren verwandten Aspekten. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `postpetition-transfers-549` | Prueft unauthorized postpetition transfers, ordinary course, court authorization and recovery. |
| `preference-ordinary-course` | Prueft ordinary-course, contemporaneous exchange, new value and subsequent new value defenses. |
| `preferences-547` | Prueft preferential transfers, 90-day/insider period, antecedent debt, insolvency presumption and defenses. |
| `priority-claims-507` | Prueft priority claims: domestic support, wages, taxes, deposits, grain/fisherman and plan/distribution impact. |

## Arbeitsweg

- Rolle und Ziel im US Bankruptcy Code Title 11: Chapters 7/9/11/12/13/15, Automatic Stay, Claims, DIP, 363 Sales, Plans und Cross-Border klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `postpetition-transfers-549`

**Fokus:** Prueft unauthorized postpetition transfers, ordinary course, court authorization and recovery.

# Postpetition Transfers § 549

## Fachkern: Postpetition Transfers § 549
- **Spezialgegenstand:** Postpetition Transfers § 549 wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Postpetition Transfers § 549** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. § 549
- 11 U.S.C. § 550
- Cash management records


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Transfer after petition?
- Authorized by Code or court?
- Recipient and value?


## Workflow

1. Transfer identify.
2. Authorization check.
3. Recovery and defenses mappen.


## Output

- 549 transfer memo
- Recovery checklist
- Cash control note


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

## 2. `preference-ordinary-course`

**Fokus:** Prueft ordinary-course, contemporaneous exchange, new value and subsequent new value defenses.

# Preference Defense Ordinary Course

## Fachkern: Preference Defense Ordinary Course
- **Spezialgegenstand:** Preference Defense Ordinary Course wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Preference Defense Ordinary Course** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. § 547(c)
- Payment history
- Invoices/ledger


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Payment timing vs historical baseline?
- New value after transfer?
- COD or contemporaneous exchange?


## Workflow

1. Payment data normalize.
2. Defense-by-transfer table.
3. Settlement range.


## Output

- Preference defense memo
- Payment history chart
- New value schedule


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

## 3. `preferences-547`

**Fokus:** Prueft preferential transfers, 90-day/insider period, antecedent debt, insolvency presumption and defenses.

# Preferences § 547

## Fachkern: Preferences § 547
- **Spezialgegenstand:** Preferences § 547 wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Preferences § 547** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. § 547
- 11 U.S.C. § 550
- Payment records


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Transfer date and amount?
- Antecedent debt?
- Creditor improved position?
- Defenses?


## Workflow

1. Preference elements test.
2. Lookback and insider status.
3. Defenses collect.


## Output

- Preference analysis table
- Demand/defense memo
- Settlement range issues


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

## 4. `priority-claims-507`

**Fokus:** Prueft priority claims: domestic support, wages, taxes, deposits, grain/fisherman and plan/distribution impact.

# Priority Claims § 507

## Fachkern: Priority Claims § 507
- **Spezialgegenstand:** Priority Claims § 507 wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Title 11 U.S. Code, Federal Rules of Bankruptcy Procedure, Chapter 7/11/13/15, automatic stay, DIP financing, claims, plan, avoidance, discharge und U.S.-Court-Docket.
- **Entscheidende Weiche:** Bestimme Chapter, Estate Property, Stay-Wirkung, Creditor-Klasse, Court-Order-Bedarf, Timeline und Schnittstelle zu deutschen Assets.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das US-Bankruptcy-Code-Plugin ist ein deutscher Arbeitskompass fuer Title 11: Restrukturierung, Liquidation, Verbraucherinsolvenz, Chapter 11, Subchapter V, Chapter 15, Claims, Automatic Stay, DIP-Finanzierung und distressed transactions.

Dieser Skill macht aus dem Thema **Priority Claims § 507** eine belastbare Arbeitsroute: erst Rolle und Ziel, dann Code-Anker, Tatsachen, Dokumente, Risiken, offene US-Counsel-Fragen und verwertbarer Output. Er ist kein Ersatz für zugelassenen US-Counsel, aber er soll die deutsche Kanzlei, Rechtsabteilung oder den Verlag so vorbereiten, dass US-Counsel sofort mit einer geordneten Akte weiterarbeiten kann.

## Code- und Quellenanker

- 11 U.S.C. § 507
- 11 U.S.C. §§ 1129, 726, 1322
- Claims register


Aktuelle Fassungen, Forms, Fees, Local Rules und Court-Practice immer live über offizielle Quellen prüfen. Keine Modellzitate zu US-Rechtsprechung verwenden, wenn Gericht, Datum, Aktenzeichen/Docket und freie Quelle nicht geprüft sind.

## Intake-Fragen

- Which priority category?
- Amount and documentation?
- Chapter-specific treatment?


## Workflow

1. Priority basis prüfen.
2. Distribution waterfall.
3. Plan treatment and objections markieren.


## Output

- Priority claim matrix
- Distribution memo
- Objection issues


## Tiefencheck für die Akte

Arbeite hier nicht nur abstrakt, sondern als strukturierter US-Counsel-Briefing-Filter:

- Welche Forderung ist secured, priority, administrative, unsecured, contingent, unliquidated oder disputed?
- Welche Unterlagen beweisen Entstehung, Betrag, Fälligkeit, collateral, guarantee und mögliche Einreden?
- Gibt es bar date, amendment risk, claim objection, estimation oder setoff/recoupment?
- Welche Behandlung droht im Plan oder in der Verteilung, und lohnt sich eine aktive objection/negotiation?

**Mindest-Output:** Claims-Tabelle mit Status, Belegen, Rang, Einwendungen, Frist und Plan-/Distribution-Auswirkung.

## Qualitäts- und Risikofilter

- US-Bankruptcy ist Bundesrecht, aber Local Rules, Judges, District Practice und State-Law-Rechte bleiben entscheidend.
- Keine Einreichung, Fristberechnung oder strategische US-Prozessentscheidung ohne zugelassenen US-Bankruptcy-Counsel finalisieren.

- Unklare US-Rechtsfragen werden nicht als sicher verkauft, sondern als Issue List für US-Counsel markiert.
- Zahlen, Fristen, Fees, Formulare und Schwellenwerte werden vor konkreter Verwendung anhand offizieller aktueller Quellen geprüft.
