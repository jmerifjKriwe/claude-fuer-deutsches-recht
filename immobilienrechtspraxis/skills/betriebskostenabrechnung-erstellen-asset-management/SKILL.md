---
name: betriebskostenabrechnung-erstellen-asset-management
description: "Betriebskostenabrechnung im Asset- und Property-Management erstellen: Mietvertragsklauseln, BetrKV-Mapping, WEG- oder Objektbuchhaltung, HeizkostenV, CO2KostAufG, Gewerbe-Vorwegabzug, Vorauszahlungskonto, Versand und Belegpaket."
---

# Betriebskostenabrechnung erstellen

## Fachkern: Betriebskostenabrechnung erstellen
- **Spezialgegenstand:** Betriebskostenabrechnung erstellen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB, GBO, WEG, BauGB, ErbbauRG, MaBV, Mietrecht, Grundpfandrechte, Notar-/Registervollzug und öffentlich-rechtliche Lasten.
- **Entscheidende Weiche:** Trenne Eigentum, Besitz, Grundbuchabteilung, Belastung, Fälligkeit, Vollzug, Mängel, Miet-/Nutzungsverhältnis und Finanzierung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe

Dieser Skill erstellt eine vermieterseitige Betriebskostenabrechnung für Immobilienportfolios, Mischobjekte und WEG-Sondereigentum. Er ist für Property Manager, Asset Manager, Rechtsabteilungen und Kanzleien gedacht, die aus Buchhaltung, WEG-Abrechnung, Dienstleisterrechnungen und Mietvertragsdaten eine versandfähige Abrechnung bauen müssen.

## Kaltstart

1. Objektart: Wohnraum, Gewerbe, Mischobjekt, WEG-Sondereigentum, Quartier?
2. Abrechnungsjahr, Mietfläche, Leerstände, Nutzerwechsel, Vorauszahlungen.
3. Mietvertragsklauseln: BetrKV-Verweis, konkrete Kostenliste, Pauschale, Umsatzsteueroption, sonstige Betriebskosten.
4. Datenquellen: Buchhaltung, WEG-Jahresabrechnung, Heizkostenabrechnung, CO2-Angaben, Dienstleisterverträge, Zahlungsbelege.
5. Gewünschtes Ergebnis: Einzelabrechnung, Portfoliomatrix, Mieteranschreiben, Belegepaket, Korrekturworkflow.

## Erstellungsschritte

1. **Umlagegrundlage je Mietvertrag** prüfen. Ohne vertragliche Grundlage keine Nachforderung.
2. **Kostenarten-Mapping** nach BetrKV oder Gewerbemietvertrag: Verwaltung, Instandhaltung und Finanzierungskosten aussondern.
3. **WEG-Daten übersetzen**: Verwalterhonorar, Rücklage und Reparaturen nicht in die Mieterabrechnung übernehmen; umlagefähige Positionen neu schlüsseln.
4. **Gewerbe-Vorwegabzug**: Restaurant, Praxis, Laden, Tiefgarage oder Sondernutzung gesondert prüfen.
5. **Heizkosten** nach HeizkostenV gesondert verarbeiten; Kürzungsrisiken bei fehlender Verbrauchserfassung markieren.
6. **CO2-Kosten** nach CO2KostAufG rechnen; Vermieteranteil herausnehmen.
7. **Vorauszahlungskonto** abgleichen: Soll, Ist, Nutzerwechsel, Guthaben, Nachzahlung.
8. **Versand-Qualitygate**: Zugangsnachweis, Abrechnungsfrist, Belegarchiv, Ansprechpartner.

## Rechenmatrix

| Position | Quelle | Umlagegrundlage | Schlüssel | Betrag brutto/netto | Mieteranteil | Belegstatus |
| --- | --- | --- | --- | --- | --- | --- |
| Grundsteuer | Bescheid | Vertrag/BetrKV | Fläche | [...] | [...] | [...] |
| Versicherung | Police/Rechnung | BetrKV | Fläche/MEA | [...] | [...] | [...] |
| Hausmeister | Vertrag/Stunden | BetrKV anteilig | Fläche | [...] | [...] | Split nötig |
| Heizung | Heizkostenabrechnung | HeizkostenV | Verbrauch/Fläche | [...] | [...] | CO2 prüfen |
| Verwalter | WEG | nicht umlagefähig | - | [...] | 0 | herausnehmen |

## Output

- Abrechnung je Mieter mit Saldo.
- Beleg- und Datenraumindex.
- internes Prüfprotokoll "umlagefähig / nicht umlagefähig / offen".
- separates Schreiben zur Vorauszahlungsanpassung nach § 560 Abs. 4 BGB, wenn Wohnraum betroffen ist.

## Quellenregel

§ 556 BGB, § 556a BGB, BetrKV, HeizkostenV und CO2KostAufG aktuell prüfen. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen.
