---
name: bericht-aussenhandel-intrastat-battg
description: "Bericht Aussenhandel Intrastat Battg: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bericht Aussenhandel Intrastat Battg

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Bericht Aussenhandel Intrastat Battg** im Plugin Berichtspflichten Erlediger. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bericht-aussenhandel-intrastat-ahstatg` | Intrastat/Außenhandelsstatistik: Eingänge/Versendungen, Schwellen, Warennummer, Ursprungsland, Lieferbedingung und Korrekturmeldung. |
| `bericht-battg-batterieregister-mengen` | Batterierecht: Registrierung, Geräte-/Industriebatterien, Rücknahme, Mengenmeldung, neue EU-Batterieverordnung-Schnittstelle. |
| `bericht-baugenehmigung-baustatistik` | Baustatistik und Bauunterlagen: Genehmigung, Baubeginn, Fertigstellung, Nutzfläche, Kosten und Statistikbogen. |

## Arbeitsweg

- Rolle und Ziel im Berichtspflichten (Audit/Compliance/Steuer) klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: HGB § 325 Offenlegung 12 Monate, GwG-Risikoanalyse jährlich, LkSG-Bericht 4 Monate nach Geschäftsjahr, CSRD Berichtsjahre gestaffelt 2024 ff..
- Tragende Normen verifizieren: HGB §§ 264, 289, 290, 315, AktG §§ 90, 91, 161 (Erklärung zur Unternehmensführung), DCGK, GwG § 6 Risikoanalyse / § 9 jährlich, LkSG §§ 3, 10, NIS2 Art. 23, CSRD-Umsetzung, DSGVO Art. 30 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Vorstand, Aufsichtsrat, Wirtschaftsprüfer, Geldwäschebeauftragter, Datenschutzbeauftragter, BaFin, BAFA (LkSG), Steuerprüfer.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Lagebericht, CSRD-Nachhaltigkeitsbericht, GwG-Risikoanalyse, LkSG-Bericht, Compliance-Bericht, Aufsichtsratsbericht, Datenschutz-Tätigkeitsbericht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `bericht-aussenhandel-intrastat-ahstatg`

**Fokus:** Intrastat/Außenhandelsstatistik: Eingänge/Versendungen, Schwellen, Warennummer, Ursprungsland, Lieferbedingung und Korrekturmeldung.

# Außenhandel und Intrastat

## Einsatz

Für Unternehmen mit EU-Warenverkehr.

## Norm- und Quellenanker

AHStatG; EU-Intrastat-Regeln; Warenverzeichnis; BStatG.

## Arbeitsfragen

1. Welche Schwelle überschritten?
2. Welche Warennummer und Transaktionsart?
3. Welche Korrektur nötig?

## Output

Intrastat-Meldematrix und Korrekturplan.

## Red Flags

- Dienstleistung statt Ware
- Warennummer geraten
- Schwelle nicht überwacht

## Arbeitsstil

Berichtspflichten werden wie kleine Verfahren behandelt: Rechtsgrundlage lesen, Pflichtenträger und Schwelle prüfen, Datenquelle sichern, nur erforderliche Daten melden, Vier-Augen-Freigabe dokumentieren, Versandnachweis ablegen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 2. `bericht-battg-batterieregister-mengen`

**Fokus:** Batterierecht: Registrierung, Geräte-/Industriebatterien, Rücknahme, Mengenmeldung, neue EU-Batterieverordnung-Schnittstelle.

# Batterierecht und Mengenmeldung

## Einsatz

Für Unternehmen, die Batterien beilegen, importieren oder vertreiben.

## Norm- und Quellenanker

BattG; EU-Batterieverordnung; Stiftung ear/UBA-Hinweise live prüfen.

## Arbeitsfragen

1. Welche Batterieart?
2. Wer ist Hersteller/Vertreiber?
3. Welche Mengen und Rücknahmepflichten?

## Output

Batterie-Melde- und Rücknahmematrix.

## Red Flags

- Knopfzellen im Produkt vergessen
- Auslandshersteller ohne Bevollmächtigten
- EU-Reform nicht geprüft

## Arbeitsstil

Berichtspflichten werden wie kleine Verfahren behandelt: Rechtsgrundlage lesen, Pflichtenträger und Schwelle prüfen, Datenquelle sichern, nur erforderliche Daten melden, Vier-Augen-Freigabe dokumentieren, Versandnachweis ablegen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 3. `bericht-baugenehmigung-baustatistik`

**Fokus:** Baustatistik und Bauunterlagen: Genehmigung, Baubeginn, Fertigstellung, Nutzfläche, Kosten und Statistikbogen.

# Baugenehmigung und Baustatistik

## Einsatz

Für Unternehmen, die bauen, umbauen oder Nutzungen ändern.

## Norm- und Quellenanker

- Hochbaustatistikgesetz (HBauStatG) und BStatG für Erhebungszweck, Auskunftspflicht und Datenschutz der Baustatistik.
- Landesbauordnung und Bauvorlagenverordnung des konkreten Bundeslandes für Genehmigung, Anzeige, Nutzungsänderung, Baubeginn und Fertigstellung.
- BauGB/BauNVO nur ziehen, wenn planungsrechtliche Zulässigkeit, Gebietstyp oder Befreiung betroffen ist.
- Statistikbogen und Bauportal des Landes live prüfen; die Formularlogik unterscheidet sich praktisch.

## Arbeitsfragen

1. Neubau, Umbau, Erweiterung, Nutzungsänderung, Abbruch, verfahrensfrei oder genehmigungspflichtig?
2. Welche Bauherrn-/Entwurfsverfasser-/Unternehmensdaten dürfen in die Statistik und welche gehören nur in Bauvorlagen?
3. Welche Flächen/Kosten: Nutzfläche, Wohnfläche, Bruttorauminhalt, Baukosten, Energieart, Gebäudeart?
4. Welche Landesfristen für Baubeginnsanzeige, Fertigstellungsanzeige, Prüfbescheinigungen und Abnahmen?
5. Sind Statistikbogen, Baugenehmigung, Förderantrag und steuerliche Aktivierung konsistent?

## Output

Bau-Berichtspaket mit Genehmigungsstatus, Statistikbogen, Landesbauportal-Check, Kosten-/Flächenabgleich, Baubeginn-/Fertigstellungsfristen und Zuständigkeitsmatrix.

## Red Flags

- Nutzungsänderung vergessen
- Kosten falsch abgegrenzt
- Baubeginn nicht angezeigt

## Arbeitsstil

Berichtspflichten werden wie kleine Verfahren behandelt: Rechtsgrundlage lesen, Pflichtenträger und Schwelle prüfen, Datenquelle sichern, nur erforderliche Daten melden, Vier-Augen-Freigabe dokumentieren, Versandnachweis ablegen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.
