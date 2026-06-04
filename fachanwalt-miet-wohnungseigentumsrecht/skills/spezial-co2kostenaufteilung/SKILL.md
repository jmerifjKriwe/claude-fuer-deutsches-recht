---
name: spezial-co2kostenaufteilung
description: "CO2-Kostenaufteilung in Miet- und WEG-Abrechnungen: CO2KostAufG, Wohngebäude-Stufenmodell, Nichtwohngebäude-50/50-Regel, Brennstoffdaten, Emissionsfaktor, Vermieteranteil, Mieterentlastung und Abrechnungsbaustein."
---

# CO2-Kostenaufteilung

## Aufgabe

Dieser Skill rechnet CO2-Kosten nicht als Nebensatz, sondern als eigene Abrechnungsebene. Er verhindert den typischen Fehler, CO2-Kosten einfach vollständig dem Mieter oder stumpf nach Fläche zuzuschlagen.

## Datensatz

Frage ab:

1. Wohngebäude, Nichtwohngebäude oder gemischte Nutzung?
2. Brennstoff, Abrechnungszeitraum, CO2-Kostenanteil aus Lieferantenrechnung.
3. Wohn-/Nutzfläche, Energiekennwert oder Emissionsdaten.
4. Heizkostenabrechnung und Brennstoffrechnung.
5. WEG-Daten: liefert die Verwaltung die für Vermieter nötigen Angaben?

## Rechtslogik

- Wohngebäude: Stufenmodell nach CO2KostAufG anhand Emissionen je Quadratmeter und Jahr.
- Nichtwohngebäude: derzeit grundsätzlich hälftige Aufteilung, solange kein verbindliches Stufenmodell gilt.
- Vermieter darf seinen Anteil nicht über Betriebskosten wieder auf den Mieter umlegen.
- Fehlende Angaben in der Abrechnung führen zu Korrektur- und Einwendungsbedarf.
- Bei WEG muss der vermietende Eigentümer die gemeinschaftlichen Heiz-/CO2-Daten in die mietrechtliche Abrechnung übersetzen.

## Ausgabe

- CO2-Rechenblatt: Gesamtkosten, Mieteranteil, Vermieteranteil.
- Hinweistext für Betriebskostenabrechnung.
- Einwendungsschreiben bei fehlender oder falscher Aufteilung.
- Datenanforderung an WEG-Verwaltung.

## Quellen- und Sicherheitsregel

CO2KostAufG aktuell prüfen. Besonders bei Nichtwohngebäuden keine erfundene Stufenmodellpflicht behaupten.
