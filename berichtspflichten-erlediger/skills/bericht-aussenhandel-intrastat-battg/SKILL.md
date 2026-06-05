---
name: bericht-aussenhandel-intrastat-battg
description: "Bericht Aussenhandel Intrastat Ahstatg, Bericht Battg Batterieregister Mengen, Bericht Baugenehmigung Baustatistik: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Bericht Aussenhandel Intrastat Ahstatg, Bericht Battg Batterieregister Mengen, Bericht Baugenehmigung Baustatistik

## Arbeitsbereich

In diesem Skill wird **Bericht Aussenhandel Intrastat Ahstatg, Bericht Battg Batterieregister Mengen, Bericht Baugenehmigung Baustatistik** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bericht-aussenhandel-intrastat-ahstatg` | Intrastat/Außenhandelsstatistik: Eingänge/Versendungen, Schwellen, Warennummer, Ursprungsland, Lieferbedingung und Korrekturmeldung. |
| `bericht-battg-batterieregister-mengen` | Batterierecht: Registrierung, Geräte-/Industriebatterien, Rücknahme, Mengenmeldung, neue EU-Batterieverordnung-Schnittstelle. |
| `bericht-baugenehmigung-baustatistik` | Baustatistik und Bauunterlagen: Genehmigung, Baubeginn, Fertigstellung, Nutzfläche, Kosten und Statistikbogen. |

## Arbeitsweg

Für **Bericht Aussenhandel Intrastat Ahstatg, Bericht Battg Batterieregister Mengen, Bericht Baugenehmigung Baustatistik** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `berichtspflichten-erlediger` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


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
