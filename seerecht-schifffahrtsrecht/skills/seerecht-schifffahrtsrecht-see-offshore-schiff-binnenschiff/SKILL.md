---
name: seerecht-schifffahrtsrecht-see-offshore-schiff-binnenschiff
description: "SEE Offshore Schiff Binnenschiff im Plugin Seerecht Schifffahrtsrecht: prüft konkret Offshore-Schiff, Binnenschiff, Kreuzfahrtschiff, Konnossement. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# SEE Offshore Schiff Binnenschiff

## Arbeitsbereich

**SEE Offshore Schiff Binnenschiff** ordnet den Fall über die tragenden Prüffelder: Offshore-Schiff, Binnenschiff, Kreuzfahrtschiff. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `see-073-offshore-schiff-kaufvertrag-scopen` | Offshore-Schiff: Energiekonzern; Offshore-Windparkbetreiber; Drillkontraktoren scopet Kaufvertrag fuer Offshore-Versorgungsschiff (PSV/AHTS) oder Bohrinsel-Tender: Gewaehrleistung; Lastenfreistellung; Eigentumsuebergang (SchRG § 2); Zertifikatsstatus; Escrow-Mechanismus. HGB §§ 476 ff.; MODU-Code IMO; SchRG §§ 8-75; OSPAR-Konvention Nordsee. Output: Kaufvertrag-Review-Matrix und Closing-Conditions. |
| `see-083-binnenschiff-kaufvertrag-scopen` | Binnenschiff: Binnenschiffer; Verladungsunternehmen; Kreditinstitut scopet Kaufvertrag fuer Binnenmotorgueterschiff; Tanker oder Fahrgastschiff: Gewaehrleistung; Lastenfreistellung; Eigentumsuebergang (SchRG § 2); Zertifikatsstatus; Escrow-Mechanismus. BinSchG §§ 1-133; SchRG §§ 1-75 fuer eingetragene Binnenschiffe; BinSchRegO. Output: Kaufvertrag-Review-Matrix und Closing-Conditions. |
| `see-093-kreuzfahrtschiff-kaufvertrag-scopen` | Kreuzfahrtschiff: Kreuzfahrtreeder; Passagier-Charterer; Passagierrechts-Klaeger scopet Kaufvertrag fuer Kreuzfahrtschiff oder grosses Fahrgastschiff: Gewaehrleistung; Lastenfreistellung; Eigentumsuebergang (SchRG § 2); Zertifikatsstatus; Escrow-Mechanismus. HGB §§ 536-556 Befoerderung von Reisenden; Athen-Uebereinkommen 2002; SOLAS Kap. III. Output: Kaufvertrag-Review-Matrix und Closing-Conditions. |
| `see-103-konnossement-kaufvertrag-scopen` | Konnossement: Verfrachter; Ablader; Konnossementsinhaber; finanzierende Bank scopet Kaufvertrag fuer Konnossements-Transaktion (Bill of Lading): Gewaehrleistung; Lastenfreistellung; Eigentumsuebergang (SchRG § 2); Zertifikatsstatus; Escrow-Mechanismus. HGB §§ 513-525 Konnossement; HGB §§ 498-511 Verfrachter-Haftung; Hague-Visby Rules. Output: Kaufvertrag-Review-Matrix und Closing-Conditions. |
| `see-113-charterparty-kaufvertrag-scopen` | Charterparty: Reeder; Time Charterer; Voyage Charterer; Bareboat Charterer scopet Kaufvertrag fuer Gechartertes Seeschiff unter Charterparty: Gewaehrleistung; Lastenfreistellung; Eigentumsuebergang (SchRG § 2); Zertifikatsstatus; Escrow-Mechanismus. HGB §§ 527-569 Reise- und Zeitfrachtvertrag; NYPE 2015; Baltime 2001. Output: Kaufvertrag-Review-Matrix und Closing-Conditions. |

## Arbeitsweg

- Rolle und Ziel im Seerecht Schifffahrtsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `see-073-offshore-schiff-kaufvertrag-scopen`

**Fokus:** Offshore-Schiff: Energiekonzern; Offshore-Windparkbetreiber; Drillkontraktoren scopet Kaufvertrag fuer Offshore-Versorgungsschiff (PSV/AHTS) oder Bohrinsel-Tender: Gewaehrleistung; Lastenfreistellung; Eigentumsuebergang (SchRG § 2); Zertifikatsstatus; Escrow-Mechanismus. HGB §§ 476 ff.; MODU-Code IMO; SchRG §§ 8-75; OSPAR-Konvention Nordsee. Output: Kaufvertrag-Review-Matrix und Closing-Conditions.

# Offshore-Schiff – Kaufvertrag scopen

## Mandantenfall
Ein Investor kauft ein Offshore-Versorgungsschiff (PSV/AHTS) oder Bohrinsel-Tender; Risiken aus Altlasten und Zertifikatsmängeln sind zu identifizieren. Ein Reeder veräußert ein Offshore-Versorgungsschiff (PSV/AHTS) oder Bohrinsel-Tender unter Zeitdruck; Gewährleistungsausschlüsse sind zu prüfen. Eine Bank finanziert den Kauf und möchte Vertragsrisiken kennen.

## Erste Schritte
1. Kaufvertrag sichten: Kaufpreis, Zahlungsplan, Lieferbedingungen fuer Offshore-Versorgungsschiff (PSV/AHTS) oder Bohrinsel-Tender.
2. Lastenuebergang pruefen: werden alle Hypotheken vor Eigentumsuebergang geloescht?
3. SchRG § 2 Eigentumsuebergang: erst Einigung und Eintragung; Zeitplan pruefen.
4. Zertifikatsstatus klaeren: Klasse; ISM; MLC; ISPS; Uebergabe oder Neuausstellung?
5. Gewaehrleistungsklauseln: BGB §§ 433-479 oder as-is-Ausschluss?
6. Escrow-Mechanismus fuer simultane Zahlung und Eigentumsuebergang aufsetzen.

## Rechtsrahmen
- HGB §§ 476 ff.; MODU-Code IMO; SchRG §§ 8-75; OSPAR-Konvention Nordsee; BGB §§ 433-479 Kaufgewaehrleistung; SchRG § 2 Eigentumsuebergang; SchRegO. Dynamic Positioning (DP)-Klasse; NORSOK-Standard; Offshore-Werkvertrag.

## Prüfraster
- Sind alle Hypotheken und Lasten vor Eigentumsuebergang abzuloesen?
- Enthaelt der Kaufvertrag eine umfassende Freistellungsklausel?
- Sind Zertifikate (Klasse/ISM/MLC) als Closing-Bedingungen definiert?
- Ist der Gewaehrleistungsausschluss rechtswirksam?
- Ist Escrow-Mechanismus fuer simultane Transaktion vorgesehen?

## Typische Fallstricke
- Kaeufer haftet mit Offshore-Versorgungsschiff (PSV/AHTS) oder Bohrinsel-Tender fuer Altschulden bis zur Loeschung.
- Gewaehrleistungsausschluss (as-is) deckt keine versteckten Konstruktionsmaengel.
- Zertifikatslücke zwischen Closing und Neuausstellung gefaehrdet Betrieb.

## Output
Kaufvertrag-Review-Matrix und Closing-Conditions-Checkliste fuer Offshore-Versorgungsschiff (PSV/AHTS) oder Bohrinsel-Tender.


## Vertiefung: Wesentliche Kaufvertragsklauseln im Schiffskauf
International dominieren MOA-Standardformulare (Norwegian Saleform 2012; Norwegian Saleform 1993; Nipponsale 1999). Für deutsche Seeschiffe mit HGB-Bezug gelten ergänzend die deutschen Kaufrechtsregeln (BGB §§ 433-479). Bei internationalem Schiffskauf empfiehlt sich die ausdrückliche Rechtswahl (z.B. englisches Recht) im Vertrag, um CISG-Anwendung zu vermeiden.

## Wesentliche Klauseln prüfen
- **Deposit Clause**: Anzahlung (typisch 10%) als Sicherheit; bei Closing verrechenbar; bei Buyer-Default einbehalten.
- **Delivery Condition**: clean class; no outstanding class recommendations; free of encumbrances.
- **Bunker Provision**: aktuelle Bunker werden zum Tagesmarktpreis übernommen; gemessen bei Übergabe.
- **Vessel Documents**: welche Originalzertifikate werden übergeben; welche müssen neu ausgestellt werden?
- **Governing Law and Arbitration**: English Law und LMAA-Schiedsverfahren London ist Marktstandard.

## Risiken und Gegenmaßnahmen
Wesentliche Risiken beim Schiffskauf: Verborgene Hypotheken; ausstehende Klassemängelempfehlungen; unbekannte Schiffsgläubigerrechte; laufende PSC-Banning; auslaufende ISM-/MLC-Zertifikate. Gegenmaßnahmen: umfassende Freistellungsklausel; Kaufpreiseinbehalt als Escrow; Closing-Conditions präzise definieren.


## Checkliste Kaufvertrag-Prüfung
- [ ] Kaufvertrag vollständig vorliegend (Hauptvertrag; Anhänge; Spezifikationen)
- [ ] Kaufpreis und Zahlungsmodalitäten klar geregelt
- [ ] Closing-Bedingungen (Delivery Conditions) präzise definiert
- [ ] Lastenfreistellungsklausel des Verkäufers vollständig
- [ ] Escrow-Mechanismus für simultane Zahlung und Eigentumsübergang geregelt
- [ ] Gewährleistung (BGB §§ 433-479) oder Ausschluss (as-is) klar vereinbart
- [ ] Zertifikate (Klasse; ISM; MLC; ISPS) als Closing-Conditions definiert
- [ ] Rücktrittsrechte und Vertragsstrafen bei Verzögerung geregelt
- [ ] Rechtswahl und Gerichtsstand/Schiedsklausel vereinbart

## Relevante Rechtsprechung
- BGH zur Gewährleistung beim Schiffskauf; arglistiges Verschweigen von Mängeln.
- BGH zur Wirksamkeit von as-is-Klauseln in Kaufverträgen; Grenzen des Haftungsausschlusses.
- LG Hamburg zu Closing-Bedingungen bei Schiffskäufen; Auslegung von Saleform-Vertragsklauseln.

## Normen im Überblick
- BGB § 433: Kaufvertrag; Pflichten des Verkäufers.
- BGB §§ 434-442: Sachmangel; Rechtsmangel; Haftungsausschluss.
- BGB §§ 437-441: Mängelrechte des Käufers; Nacherfüllung; Rücktritt; Minderung.
- SchRG § 2: Eigentumsübergang nur durch Einigung und Eintragung; nicht durch Kaufvertrag allein.
- SchRG § 19: Löschung der Hypothek durch Löschungsbewilligung des Gläubigers.
- HGB §§ 480-482: Schiffslieferung im Kontext des Handelsrechts.

## Quellen
- SchRG § 2: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- BGB §§ 433-479: https://dejure.org/gesetze/BGB/433.html
- HGB §§ 480 ff.: https://dejure.org/gesetze/HGB/480.html
- openjur Schiffskaufstreit: https://www.openjur.de

## 2. `see-083-binnenschiff-kaufvertrag-scopen`

**Fokus:** Binnenschiff: Binnenschiffer; Verladungsunternehmen; Kreditinstitut scopet Kaufvertrag fuer Binnenmotorgueterschiff; Tanker oder Fahrgastschiff: Gewaehrleistung; Lastenfreistellung; Eigentumsuebergang (SchRG § 2); Zertifikatsstatus; Escrow-Mechanismus. BinSchG §§ 1-133; SchRG §§ 1-75 fuer eingetragene Binnenschiffe; BinSchRegO. Output: Kaufvertrag-Review-Matrix und Closing-Conditions.

# Binnenschiff – Kaufvertrag scopen

## Mandantenfall
Ein Investor kauft ein Binnenmotorgueterschiff; Tanker oder Fahrgastschiff; Risiken aus Altlasten und Zertifikatsmängeln sind zu identifizieren. Ein Reeder veräußert ein Binnenmotorgueterschiff; Tanker oder Fahrgastschiff unter Zeitdruck; Gewährleistungsausschlüsse sind zu prüfen. Eine Bank finanziert den Kauf und möchte Vertragsrisiken kennen.

## Erste Schritte
1. Kaufvertrag sichten: Kaufpreis, Zahlungsplan, Lieferbedingungen fuer Binnenmotorgueterschiff; Tanker oder Fahrgastschiff.
2. Lastenuebergang pruefen: werden alle Hypotheken vor Eigentumsuebergang geloescht?
3. SchRG § 2 Eigentumsuebergang: erst Einigung und Eintragung; Zeitplan pruefen.
4. Zertifikatsstatus klaeren: Klasse; ISM; MLC; ISPS; Uebergabe oder Neuausstellung?
5. Gewaehrleistungsklauseln: BGB §§ 433-479 oder as-is-Ausschluss?
6. Escrow-Mechanismus fuer simultane Zahlung und Eigentumsuebergang aufsetzen.

## Rechtsrahmen
- BinSchG §§ 1-133; SchRG §§ 1-75 fuer eingetragene Binnenschiffe; BinSchRegO; BGB §§ 433-479 Kaufgewaehrleistung; SchRG § 2 Eigentumsuebergang; SchRegO. ADN-Gefahrgut Binnenwasserstrassen; RheinSchPersV; CESNI-Standards.

## Prüfraster
- Sind alle Hypotheken und Lasten vor Eigentumsuebergang abzuloesen?
- Enthaelt der Kaufvertrag eine umfassende Freistellungsklausel?
- Sind Zertifikate (Klasse/ISM/MLC) als Closing-Bedingungen definiert?
- Ist der Gewaehrleistungsausschluss rechtswirksam?
- Ist Escrow-Mechanismus fuer simultane Transaktion vorgesehen?

## Typische Fallstricke
- Kaeufer haftet mit Binnenmotorgueterschiff; Tanker oder Fahrgastschiff fuer Altschulden bis zur Loeschung.
- Gewaehrleistungsausschluss (as-is) deckt keine versteckten Konstruktionsmaengel.
- Zertifikatslücke zwischen Closing und Neuausstellung gefaehrdet Betrieb.

## Output
Kaufvertrag-Review-Matrix und Closing-Conditions-Checkliste fuer Binnenmotorgueterschiff; Tanker oder Fahrgastschiff.


## Vertiefung: Wesentliche Kaufvertragsklauseln im Schiffskauf
International dominieren MOA-Standardformulare (Norwegian Saleform 2012; Norwegian Saleform 1993; Nipponsale 1999). Für deutsche Seeschiffe mit HGB-Bezug gelten ergänzend die deutschen Kaufrechtsregeln (BGB §§ 433-479). Bei internationalem Schiffskauf empfiehlt sich die ausdrückliche Rechtswahl (z.B. englisches Recht) im Vertrag, um CISG-Anwendung zu vermeiden.

## Wesentliche Klauseln prüfen
- **Deposit Clause**: Anzahlung (typisch 10%) als Sicherheit; bei Closing verrechenbar; bei Buyer-Default einbehalten.
- **Delivery Condition**: clean class; no outstanding class recommendations; free of encumbrances.
- **Bunker Provision**: aktuelle Bunker werden zum Tagesmarktpreis übernommen; gemessen bei Übergabe.
- **Vessel Documents**: welche Originalzertifikate werden übergeben; welche müssen neu ausgestellt werden?
- **Governing Law and Arbitration**: English Law und LMAA-Schiedsverfahren London ist Marktstandard.

## Risiken und Gegenmaßnahmen
Wesentliche Risiken beim Schiffskauf: Verborgene Hypotheken; ausstehende Klassemängelempfehlungen; unbekannte Schiffsgläubigerrechte; laufende PSC-Banning; auslaufende ISM-/MLC-Zertifikate. Gegenmaßnahmen: umfassende Freistellungsklausel; Kaufpreiseinbehalt als Escrow; Closing-Conditions präzise definieren.


## Checkliste Kaufvertrag-Prüfung
- [ ] Kaufvertrag vollständig vorliegend (Hauptvertrag; Anhänge; Spezifikationen)
- [ ] Kaufpreis und Zahlungsmodalitäten klar geregelt
- [ ] Closing-Bedingungen (Delivery Conditions) präzise definiert
- [ ] Lastenfreistellungsklausel des Verkäufers vollständig
- [ ] Escrow-Mechanismus für simultane Zahlung und Eigentumsübergang geregelt
- [ ] Gewährleistung (BGB §§ 433-479) oder Ausschluss (as-is) klar vereinbart
- [ ] Zertifikate (Klasse; ISM; MLC; ISPS) als Closing-Conditions definiert
- [ ] Rücktrittsrechte und Vertragsstrafen bei Verzögerung geregelt
- [ ] Rechtswahl und Gerichtsstand/Schiedsklausel vereinbart

## Relevante Rechtsprechung
- BGH zur Gewährleistung beim Schiffskauf; arglistiges Verschweigen von Mängeln.
- BGH zur Wirksamkeit von as-is-Klauseln in Kaufverträgen; Grenzen des Haftungsausschlusses.
- LG Hamburg zu Closing-Bedingungen bei Schiffskäufen; Auslegung von Saleform-Vertragsklauseln.

## Normen im Überblick
- BGB § 433: Kaufvertrag; Pflichten des Verkäufers.
- BGB §§ 434-442: Sachmangel; Rechtsmangel; Haftungsausschluss.
- BGB §§ 437-441: Mängelrechte des Käufers; Nacherfüllung; Rücktritt; Minderung.
- SchRG § 2: Eigentumsübergang nur durch Einigung und Eintragung; nicht durch Kaufvertrag allein.
- SchRG § 19: Löschung der Hypothek durch Löschungsbewilligung des Gläubigers.
- HGB §§ 480-482: Schiffslieferung im Kontext des Handelsrechts.

## Quellen
- SchRG § 2: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- BGB §§ 433-479: https://dejure.org/gesetze/BGB/433.html
- HGB §§ 480 ff.: https://dejure.org/gesetze/HGB/480.html
- openjur Schiffskaufstreit: https://www.openjur.de

## 3. `see-093-kreuzfahrtschiff-kaufvertrag-scopen`

**Fokus:** Kreuzfahrtschiff: Kreuzfahrtreeder; Passagier-Charterer; Passagierrechts-Klaeger scopet Kaufvertrag fuer Kreuzfahrtschiff oder grosses Fahrgastschiff: Gewaehrleistung; Lastenfreistellung; Eigentumsuebergang (SchRG § 2); Zertifikatsstatus; Escrow-Mechanismus. HGB §§ 536-556 Befoerderung von Reisenden; Athen-Uebereinkommen 2002; SOLAS Kap. III. Output: Kaufvertrag-Review-Matrix und Closing-Conditions.

# Kreuzfahrtschiff – Kaufvertrag scopen

## Mandantenfall
Ein Investor kauft ein Kreuzfahrtschiff oder grosses Fahrgastschiff; Risiken aus Altlasten und Zertifikatsmängeln sind zu identifizieren. Ein Reeder veräußert ein Kreuzfahrtschiff oder grosses Fahrgastschiff unter Zeitdruck; Gewährleistungsausschlüsse sind zu prüfen. Eine Bank finanziert den Kauf und möchte Vertragsrisiken kennen.

## Erste Schritte
1. Kaufvertrag sichten: Kaufpreis, Zahlungsplan, Lieferbedingungen fuer Kreuzfahrtschiff oder grosses Fahrgastschiff.
2. Lastenuebergang pruefen: werden alle Hypotheken vor Eigentumsuebergang geloescht?
3. SchRG § 2 Eigentumsuebergang: erst Einigung und Eintragung; Zeitplan pruefen.
4. Zertifikatsstatus klaeren: Klasse; ISM; MLC; ISPS; Uebergabe oder Neuausstellung?
5. Gewaehrleistungsklauseln: BGB §§ 433-479 oder as-is-Ausschluss?
6. Escrow-Mechanismus fuer simultane Zahlung und Eigentumsuebergang aufsetzen.

## Rechtsrahmen
- HGB §§ 536-556 Befoerderung von Reisenden; Athen-Uebereinkommen 2002; SOLAS Kap. III; BGB §§ 433-479 Kaufgewaehrleistung; SchRG § 2 Eigentumsuebergang; SchRegO. ISPS-Code Hafen-Sicherheit; SOLAS Kap. II-2 Brandschutz; MLC Passagierschiffe.

## Prüfraster
- Sind alle Hypotheken und Lasten vor Eigentumsuebergang abzuloesen?
- Enthaelt der Kaufvertrag eine umfassende Freistellungsklausel?
- Sind Zertifikate (Klasse/ISM/MLC) als Closing-Bedingungen definiert?
- Ist der Gewaehrleistungsausschluss rechtswirksam?
- Ist Escrow-Mechanismus fuer simultane Transaktion vorgesehen?

## Typische Fallstricke
- Kaeufer haftet mit Kreuzfahrtschiff oder grosses Fahrgastschiff fuer Altschulden bis zur Loeschung.
- Gewaehrleistungsausschluss (as-is) deckt keine versteckten Konstruktionsmaengel.
- Zertifikatslücke zwischen Closing und Neuausstellung gefaehrdet Betrieb.

## Output
Kaufvertrag-Review-Matrix und Closing-Conditions-Checkliste fuer Kreuzfahrtschiff oder grosses Fahrgastschiff.


## Vertiefung: Wesentliche Kaufvertragsklauseln im Schiffskauf
International dominieren MOA-Standardformulare (Norwegian Saleform 2012; Norwegian Saleform 1993; Nipponsale 1999). Für deutsche Seeschiffe mit HGB-Bezug gelten ergänzend die deutschen Kaufrechtsregeln (BGB §§ 433-479). Bei internationalem Schiffskauf empfiehlt sich die ausdrückliche Rechtswahl (z.B. englisches Recht) im Vertrag, um CISG-Anwendung zu vermeiden.

## Wesentliche Klauseln prüfen
- **Deposit Clause**: Anzahlung (typisch 10%) als Sicherheit; bei Closing verrechenbar; bei Buyer-Default einbehalten.
- **Delivery Condition**: clean class; no outstanding class recommendations; free of encumbrances.
- **Bunker Provision**: aktuelle Bunker werden zum Tagesmarktpreis übernommen; gemessen bei Übergabe.
- **Vessel Documents**: welche Originalzertifikate werden übergeben; welche müssen neu ausgestellt werden?
- **Governing Law and Arbitration**: English Law und LMAA-Schiedsverfahren London ist Marktstandard.

## Risiken und Gegenmaßnahmen
Wesentliche Risiken beim Schiffskauf: Verborgene Hypotheken; ausstehende Klassemängelempfehlungen; unbekannte Schiffsgläubigerrechte; laufende PSC-Banning; auslaufende ISM-/MLC-Zertifikate. Gegenmaßnahmen: umfassende Freistellungsklausel; Kaufpreiseinbehalt als Escrow; Closing-Conditions präzise definieren.


## Checkliste Kaufvertrag-Prüfung
- [ ] Kaufvertrag vollständig vorliegend (Hauptvertrag; Anhänge; Spezifikationen)
- [ ] Kaufpreis und Zahlungsmodalitäten klar geregelt
- [ ] Closing-Bedingungen (Delivery Conditions) präzise definiert
- [ ] Lastenfreistellungsklausel des Verkäufers vollständig
- [ ] Escrow-Mechanismus für simultane Zahlung und Eigentumsübergang geregelt
- [ ] Gewährleistung (BGB §§ 433-479) oder Ausschluss (as-is) klar vereinbart
- [ ] Zertifikate (Klasse; ISM; MLC; ISPS) als Closing-Conditions definiert
- [ ] Rücktrittsrechte und Vertragsstrafen bei Verzögerung geregelt
- [ ] Rechtswahl und Gerichtsstand/Schiedsklausel vereinbart

## Relevante Rechtsprechung
- BGH zur Gewährleistung beim Schiffskauf; arglistiges Verschweigen von Mängeln.
- BGH zur Wirksamkeit von as-is-Klauseln in Kaufverträgen; Grenzen des Haftungsausschlusses.
- LG Hamburg zu Closing-Bedingungen bei Schiffskäufen; Auslegung von Saleform-Vertragsklauseln.

## Normen im Überblick
- BGB § 433: Kaufvertrag; Pflichten des Verkäufers.
- BGB §§ 434-442: Sachmangel; Rechtsmangel; Haftungsausschluss.
- BGB §§ 437-441: Mängelrechte des Käufers; Nacherfüllung; Rücktritt; Minderung.
- SchRG § 2: Eigentumsübergang nur durch Einigung und Eintragung; nicht durch Kaufvertrag allein.
- SchRG § 19: Löschung der Hypothek durch Löschungsbewilligung des Gläubigers.
- HGB §§ 480-482: Schiffslieferung im Kontext des Handelsrechts.

## Quellen
- SchRG § 2: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- BGB §§ 433-479: https://dejure.org/gesetze/BGB/433.html
- HGB §§ 480 ff.: https://dejure.org/gesetze/HGB/480.html
- openjur Schiffskaufstreit: https://www.openjur.de

## 4. `see-103-konnossement-kaufvertrag-scopen`

**Fokus:** Konnossement: Verfrachter; Ablader; Konnossementsinhaber; finanzierende Bank scopet Kaufvertrag fuer Konnossements-Transaktion (Bill of Lading): Gewaehrleistung; Lastenfreistellung; Eigentumsuebergang (SchRG § 2); Zertifikatsstatus; Escrow-Mechanismus. HGB §§ 513-525 Konnossement; HGB §§ 498-511 Verfrachter-Haftung; Hague-Visby Rules. Output: Kaufvertrag-Review-Matrix und Closing-Conditions.

# Konnossement – Kaufvertrag scopen

## Mandantenfall
Ein Investor kauft ein Konnossements-Transaktion (Bill of Lading); Risiken aus Altlasten und Zertifikatsmängeln sind zu identifizieren. Ein Reeder veräußert ein Konnossements-Transaktion (Bill of Lading) unter Zeitdruck; Gewährleistungsausschlüsse sind zu prüfen. Eine Bank finanziert den Kauf und möchte Vertragsrisiken kennen.

## Erste Schritte
1. Kaufvertrag sichten: Kaufpreis, Zahlungsplan, Lieferbedingungen fuer Konnossements-Transaktion (Bill of Lading).
2. Lastenuebergang pruefen: werden alle Hypotheken vor Eigentumsuebergang geloescht?
3. SchRG § 2 Eigentumsuebergang: erst Einigung und Eintragung; Zeitplan pruefen.
4. Zertifikatsstatus klaeren: Klasse; ISM; MLC; ISPS; Uebergabe oder Neuausstellung?
5. Gewaehrleistungsklauseln: BGB §§ 433-479 oder as-is-Ausschluss?
6. Escrow-Mechanismus fuer simultane Zahlung und Eigentumsuebergang aufsetzen.

## Rechtsrahmen
- HGB §§ 513-525 Konnossement; HGB §§ 498-511 Verfrachter-Haftung; Hague-Visby Rules; BGB §§ 433-479 Kaufgewaehrleistung; SchRG § 2 Eigentumsuebergang; SchRegO. Hamburg Rules Art. 5 Haftungsmassstab; Rotterdam Rules (nicht in Kraft); UCP 600 Akkreditiv.

## Prüfraster
- Sind alle Hypotheken und Lasten vor Eigentumsuebergang abzuloesen?
- Enthaelt der Kaufvertrag eine umfassende Freistellungsklausel?
- Sind Zertifikate (Klasse/ISM/MLC) als Closing-Bedingungen definiert?
- Ist der Gewaehrleistungsausschluss rechtswirksam?
- Ist Escrow-Mechanismus fuer simultane Transaktion vorgesehen?

## Typische Fallstricke
- Kaeufer haftet mit Konnossements-Transaktion (Bill of Lading) fuer Altschulden bis zur Loeschung.
- Gewaehrleistungsausschluss (as-is) deckt keine versteckten Konstruktionsmaengel.
- Zertifikatslücke zwischen Closing und Neuausstellung gefaehrdet Betrieb.

## Output
Kaufvertrag-Review-Matrix und Closing-Conditions-Checkliste fuer Konnossements-Transaktion (Bill of Lading).


## Vertiefung: Wesentliche Kaufvertragsklauseln im Schiffskauf
International dominieren MOA-Standardformulare (Norwegian Saleform 2012; Norwegian Saleform 1993; Nipponsale 1999). Für deutsche Seeschiffe mit HGB-Bezug gelten ergänzend die deutschen Kaufrechtsregeln (BGB §§ 433-479). Bei internationalem Schiffskauf empfiehlt sich die ausdrückliche Rechtswahl (z.B. englisches Recht) im Vertrag, um CISG-Anwendung zu vermeiden.

## Wesentliche Klauseln prüfen
- **Deposit Clause**: Anzahlung (typisch 10%) als Sicherheit; bei Closing verrechenbar; bei Buyer-Default einbehalten.
- **Delivery Condition**: clean class; no outstanding class recommendations; free of encumbrances.
- **Bunker Provision**: aktuelle Bunker werden zum Tagesmarktpreis übernommen; gemessen bei Übergabe.
- **Vessel Documents**: welche Originalzertifikate werden übergeben; welche müssen neu ausgestellt werden?
- **Governing Law and Arbitration**: English Law und LMAA-Schiedsverfahren London ist Marktstandard.

## Risiken und Gegenmaßnahmen
Wesentliche Risiken beim Schiffskauf: Verborgene Hypotheken; ausstehende Klassemängelempfehlungen; unbekannte Schiffsgläubigerrechte; laufende PSC-Banning; auslaufende ISM-/MLC-Zertifikate. Gegenmaßnahmen: umfassende Freistellungsklausel; Kaufpreiseinbehalt als Escrow; Closing-Conditions präzise definieren.


## Checkliste Kaufvertrag-Prüfung
- [ ] Kaufvertrag vollständig vorliegend (Hauptvertrag; Anhänge; Spezifikationen)
- [ ] Kaufpreis und Zahlungsmodalitäten klar geregelt
- [ ] Closing-Bedingungen (Delivery Conditions) präzise definiert
- [ ] Lastenfreistellungsklausel des Verkäufers vollständig
- [ ] Escrow-Mechanismus für simultane Zahlung und Eigentumsübergang geregelt
- [ ] Gewährleistung (BGB §§ 433-479) oder Ausschluss (as-is) klar vereinbart
- [ ] Zertifikate (Klasse; ISM; MLC; ISPS) als Closing-Conditions definiert
- [ ] Rücktrittsrechte und Vertragsstrafen bei Verzögerung geregelt
- [ ] Rechtswahl und Gerichtsstand/Schiedsklausel vereinbart

## Relevante Rechtsprechung
- BGH zur Gewährleistung beim Schiffskauf; arglistiges Verschweigen von Mängeln.
- BGH zur Wirksamkeit von as-is-Klauseln in Kaufverträgen; Grenzen des Haftungsausschlusses.
- LG Hamburg zu Closing-Bedingungen bei Schiffskäufen; Auslegung von Saleform-Vertragsklauseln.

## Normen im Überblick
- BGB § 433: Kaufvertrag; Pflichten des Verkäufers.
- BGB §§ 434-442: Sachmangel; Rechtsmangel; Haftungsausschluss.
- BGB §§ 437-441: Mängelrechte des Käufers; Nacherfüllung; Rücktritt; Minderung.
- SchRG § 2: Eigentumsübergang nur durch Einigung und Eintragung; nicht durch Kaufvertrag allein.
- SchRG § 19: Löschung der Hypothek durch Löschungsbewilligung des Gläubigers.
- HGB §§ 480-482: Schiffslieferung im Kontext des Handelsrechts.

## Quellen
- SchRG § 2: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- BGB §§ 433-479: https://dejure.org/gesetze/BGB/433.html
- HGB §§ 480 ff.: https://dejure.org/gesetze/HGB/480.html
- openjur Schiffskaufstreit: https://www.openjur.de

## 5. `see-113-charterparty-kaufvertrag-scopen`

**Fokus:** Charterparty: Reeder; Time Charterer; Voyage Charterer; Bareboat Charterer scopet Kaufvertrag fuer Gechartertes Seeschiff unter Charterparty: Gewaehrleistung; Lastenfreistellung; Eigentumsuebergang (SchRG § 2); Zertifikatsstatus; Escrow-Mechanismus. HGB §§ 527-569 Reise- und Zeitfrachtvertrag; NYPE 2015; Baltime 2001. Output: Kaufvertrag-Review-Matrix und Closing-Conditions.

# Charterparty – Kaufvertrag scopen

## Mandantenfall
Ein Investor kauft ein Gechartertes Seeschiff unter Charterparty; Risiken aus Altlasten und Zertifikatsmängeln sind zu identifizieren. Ein Reeder veräußert ein Gechartertes Seeschiff unter Charterparty unter Zeitdruck; Gewährleistungsausschlüsse sind zu prüfen. Eine Bank finanziert den Kauf und möchte Vertragsrisiken kennen.

## Erste Schritte
1. Kaufvertrag sichten: Kaufpreis, Zahlungsplan, Lieferbedingungen fuer Gechartertes Seeschiff unter Charterparty.
2. Lastenuebergang pruefen: werden alle Hypotheken vor Eigentumsuebergang geloescht?
3. SchRG § 2 Eigentumsuebergang: erst Einigung und Eintragung; Zeitplan pruefen.
4. Zertifikatsstatus klaeren: Klasse; ISM; MLC; ISPS; Uebergabe oder Neuausstellung?
5. Gewaehrleistungsklauseln: BGB §§ 433-479 oder as-is-Ausschluss?
6. Escrow-Mechanismus fuer simultane Zahlung und Eigentumsuebergang aufsetzen.

## Rechtsrahmen
- HGB §§ 527-569 Reise- und Zeitfrachtvertrag; NYPE 2015; Baltime 2001; BGB §§ 433-479 Kaufgewaehrleistung; SchRG § 2 Eigentumsuebergang; SchRegO. Hire vs. Freight; Off-Hire-Regime; Sub-Charter; ISM-Verantwortung Bareboat.

## Prüfraster
- Sind alle Hypotheken und Lasten vor Eigentumsuebergang abzuloesen?
- Enthaelt der Kaufvertrag eine umfassende Freistellungsklausel?
- Sind Zertifikate (Klasse/ISM/MLC) als Closing-Bedingungen definiert?
- Ist der Gewaehrleistungsausschluss rechtswirksam?
- Ist Escrow-Mechanismus fuer simultane Transaktion vorgesehen?

## Typische Fallstricke
- Kaeufer haftet mit Gechartertes Seeschiff unter Charterparty fuer Altschulden bis zur Loeschung.
- Gewaehrleistungsausschluss (as-is) deckt keine versteckten Konstruktionsmaengel.
- Zertifikatslücke zwischen Closing und Neuausstellung gefaehrdet Betrieb.

## Output
Kaufvertrag-Review-Matrix und Closing-Conditions-Checkliste fuer Gechartertes Seeschiff unter Charterparty.


## Vertiefung: Wesentliche Kaufvertragsklauseln im Schiffskauf
International dominieren MOA-Standardformulare (Norwegian Saleform 2012; Norwegian Saleform 1993; Nipponsale 1999). Für deutsche Seeschiffe mit HGB-Bezug gelten ergänzend die deutschen Kaufrechtsregeln (BGB §§ 433-479). Bei internationalem Schiffskauf empfiehlt sich die ausdrückliche Rechtswahl (z.B. englisches Recht) im Vertrag, um CISG-Anwendung zu vermeiden.

## Wesentliche Klauseln prüfen
- **Deposit Clause**: Anzahlung (typisch 10%) als Sicherheit; bei Closing verrechenbar; bei Buyer-Default einbehalten.
- **Delivery Condition**: clean class; no outstanding class recommendations; free of encumbrances.
- **Bunker Provision**: aktuelle Bunker werden zum Tagesmarktpreis übernommen; gemessen bei Übergabe.
- **Vessel Documents**: welche Originalzertifikate werden übergeben; welche müssen neu ausgestellt werden?
- **Governing Law and Arbitration**: English Law und LMAA-Schiedsverfahren London ist Marktstandard.

## Risiken und Gegenmaßnahmen
Wesentliche Risiken beim Schiffskauf: Verborgene Hypotheken; ausstehende Klassemängelempfehlungen; unbekannte Schiffsgläubigerrechte; laufende PSC-Banning; auslaufende ISM-/MLC-Zertifikate. Gegenmaßnahmen: umfassende Freistellungsklausel; Kaufpreiseinbehalt als Escrow; Closing-Conditions präzise definieren.


## Checkliste Kaufvertrag-Prüfung
- [ ] Kaufvertrag vollständig vorliegend (Hauptvertrag; Anhänge; Spezifikationen)
- [ ] Kaufpreis und Zahlungsmodalitäten klar geregelt
- [ ] Closing-Bedingungen (Delivery Conditions) präzise definiert
- [ ] Lastenfreistellungsklausel des Verkäufers vollständig
- [ ] Escrow-Mechanismus für simultane Zahlung und Eigentumsübergang geregelt
- [ ] Gewährleistung (BGB §§ 433-479) oder Ausschluss (as-is) klar vereinbart
- [ ] Zertifikate (Klasse; ISM; MLC; ISPS) als Closing-Conditions definiert
- [ ] Rücktrittsrechte und Vertragsstrafen bei Verzögerung geregelt
- [ ] Rechtswahl und Gerichtsstand/Schiedsklausel vereinbart

## Relevante Rechtsprechung
- BGH zur Gewährleistung beim Schiffskauf; arglistiges Verschweigen von Mängeln.
- BGH zur Wirksamkeit von as-is-Klauseln in Kaufverträgen; Grenzen des Haftungsausschlusses.
- LG Hamburg zu Closing-Bedingungen bei Schiffskäufen; Auslegung von Saleform-Vertragsklauseln.

## Normen im Überblick
- BGB § 433: Kaufvertrag; Pflichten des Verkäufers.
- BGB §§ 434-442: Sachmangel; Rechtsmangel; Haftungsausschluss.
- BGB §§ 437-441: Mängelrechte des Käufers; Nacherfüllung; Rücktritt; Minderung.
- SchRG § 2: Eigentumsübergang nur durch Einigung und Eintragung; nicht durch Kaufvertrag allein.
- SchRG § 19: Löschung der Hypothek durch Löschungsbewilligung des Gläubigers.
- HGB §§ 480-482: Schiffslieferung im Kontext des Handelsrechts.

## Quellen
- SchRG § 2: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- BGB §§ 433-479: https://dejure.org/gesetze/BGB/433.html
- HGB §§ 480 ff.: https://dejure.org/gesetze/HGB/480.html
- openjur Schiffskaufstreit: https://www.openjur.de
