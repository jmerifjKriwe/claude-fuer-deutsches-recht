---
name: nebenkostenabrechnung-erstellen
description: "Betriebskostenabrechnung erstellen aus Vermieter- und Hausverwaltungssicht: Umlagevereinbarung, BetrKV-Kostenarten, HeizkostenV, CO2KostAufG, Abrechnungsfrist, Vorauszahlungen, Belegpaket, Zugangsnachweis und Versand-Qualitygate."
---

# Betriebskostenabrechnung erstellen

## Ziel

Dieser Skill erstellt keine pauschale Nebenkostenliste, sondern eine belastbare, versandfähige Betriebskostenabrechnung für Wohnraummiete oder gemischt genutzte Objekte. Er trennt streng:

- mietvertragliche Umlagevereinbarung,
- tatsächlich angefallene Gesamtkosten,
- umlagefähige Betriebskosten nach BetrKV,
- nicht umlagefähige Verwaltung, Instandhaltung und Instandsetzung,
- Heiz-/Warmwasserkosten nach HeizkostenV,
- CO2-Kostenaufteilung nach CO2KostAufG,
- Vorauszahlungen und Saldo.

## Kaltstart

Nur diese Punkte abfragen, wenn sie nicht aus der Akte hervorgehen:

1. Abrechnungsjahr und Zugangsziel: Bis wann muss die Abrechnung beim Mieter sein?
2. Wohnraum, Gewerbe oder gemischt genutztes Objekt?
3. Mietvertragliche Betriebskostenklausel: pauschal, Vorauszahlung, Inklusivmiete oder konkrete Kostenliste?
4. Gibt es WEG-Jahresabrechnung, Heizkostenabrechnung, Rechnungen/Zahlungsbelege, Kontoauszüge und Mieter-Vorauszahlungskonto?
5. Sollen Nachforderung, Guthaben, Vorauszahlungsanpassung oder nur ein Entwurf ausgegeben werden?

## Rechts- und Quellenanker

- § 556 BGB: Betriebskostenvereinbarung, Abrechnungszeitraum, Abrechnungsfrist, Einwendungsfrist.
- § 556a BGB: Umlagemaßstab, soweit mietvertraglich nichts anderes gilt.
- § 560 Abs. 4 BGB: Anpassung der Vorauszahlungen nach Abrechnung.
- BetrKV §§ 1 und 2: Betriebskostenbegriff und Kostenarten.
- HeizkostenV §§ 6 bis 12: Verbrauchserfassung, Kostenverteilung und Kürzungsrecht.
- CO2KostAufG: Aufteilung der CO2-Kosten, bei Wohngebäuden regelmäßig Stufenmodell.
- BGH, Urteil vom 09.04.2008 - VIII ZR 84/07: Mindestangaben einer formell ordnungsgemäßen Betriebskostenabrechnung.
- BGH, Urteil vom 12.11.2014 - VIII ZR 112/14: Schätzungen und materielle Fragen kippen nicht automatisch die formelle Ordnung.
- BGH, Urteil vom 09.12.2020 - VIII ZR 118/19: Belegeinsicht umfasst auch Zahlungsbelege.

## Erstellungsworkflow

### 1. Umlagegrundlage

Prüfe zuerst die Mietvertragslage. Ohne Umlagevereinbarung gibt es bei Wohnraum keine Nachforderung auf Betriebskosten. Ein Verweis auf die BetrKV genügt regelmäßig; "sonstige Betriebskosten" müssen als solche erkennbar vereinbart sein und dürfen nicht erst in der Abrechnung erfunden werden.

### 2. Abrechnungsperiode und Frist

- Abrechnungszeitraum höchstens zwölf Monate.
- Abrechnung muss dem Mieter spätestens zwölf Monate nach Ende des Abrechnungszeitraums zugehen.
- Nicht nur Versand, sondern Zugang beweissicher planen: Bote mit Zustellvermerk, Einwurf mit Zeuge, Portalzugang nur bei tragfähiger Vereinbarung und Zugangsnachweis.

### 3. Kostenarten-Matrix

Erzeuge eine Tabelle:

| Kostenart | Beleg | Zeitraum | Umlagefähig? | Schlüssel | Herauszurechnen |
| --- | --- | --- | --- | --- | --- |
| Grundsteuer | Bescheid | Jahr | ja, wenn vereinbart | Fläche/Vertrag | Nachzahlungen für andere Jahre erläutern |
| Wasser/Abwasser | Rechnung/Zähler | Jahr | ja | Verbrauch/Fläche | Leerstand prüfen |
| Hausmeister | Vertrag/Stunden | Jahr | nur Betrieb, nicht Reparatur/Verwaltung | Vertrag/Fläche | Reparaturanteile |
| Gartenpflege | Rechnung | Jahr | ja | Vertrag/Fläche | Neuanlage/Umgestaltung |
| Versicherung | Police/Rechnung | Jahr | Sach-/Haftpflicht ja | Vertrag/Fläche | Rechtsschutz/Verwaltung |
| Heizung/Warmwasser | Heizkostenabrechnung | Jahr | ja | HeizkostenV | CO2-Anteil, Kürzungsrecht |

### 4. Verteilerschlüssel

- Vertraglicher Schlüssel vor gesetzlichem Auffangmaßstab.
- Wenn nichts vereinbart ist: Wohnfläche nach § 556a Abs. 1 BGB, soweit Verbrauch oder Verursachung nicht erfasst wird.
- Heizkosten/Warmwasser nicht in die allgemeine Flächenlogik ziehen: HeizkostenV gesondert rechnen.
- Gemischt genutzte Objekte: Gewerbe-Vorwegabzug nur, wenn die Gewerbenutzung Mehrkosten verursacht oder der Vertrag/die Sachlage dies trägt; keine automatische Sonderbelastung ohne Begründung.

### 5. Heizkosten, Warmwasser und CO2

- Prüfen, ob Messgeräte fernablesbar sind und ob unterjährige Verbrauchsinformationen relevant sind.
- Verbrauchsanteil nach HeizkostenV grundsätzlich zwischen 50 und 70 Prozent.
- Bei Verstößen gegen HeizkostenV Kürzungsrecht nach § 12 HeizkostenV markieren.
- CO2-Kosten nicht als normale Brennstoffkosten ungeprüft vollständig auf den Mieter legen. Für Wohngebäude Stufe ermitteln; bei Nichtwohngebäuden aktuelle Sonderregel und Rechtsstand live prüfen.

### 6. Vorauszahlungen und Saldo

- Nur tatsächlich geschuldete und geleistete Vorauszahlungen für den Abrechnungszeitraum abziehen.
- Mieterwechsel taggenau abgrenzen.
- Guthaben und Nachforderung klar ausweisen.
- Anpassung der Vorauszahlungen nach § 560 Abs. 4 BGB separat erklären, nicht versteckt in die Abrechnung schreiben.

## Versand-Qualitygate

Vor Versand zwingend ausgeben:

1. formelle Mindestangaben vollständig,
2. alle Kostenarten mit Beleg und Umlagegrundlage,
3. Heizkosten/CO2 gesondert geprüft,
4. Vorauszahlungen gegen Mietkonto abgeglichen,
5. Nachforderung durch Zugangsnachweis abgesichert,
6. Belege kurzfristig einsichtsfähig,
7. Anschreiben mit Einwendungsfrist und Belegeinsichtshinweis.

## Output

- fertige Abrechnung als Tabelle,
- Begleitschreiben an den Mieter,
- Belegverzeichnis,
- Rechenkontrollblatt,
- Vorauszahlungsanpassung als separates Schreiben,
- Lückenliste, wenn die Abrechnung noch nicht versandfähig ist.

## Quellenregel

Normen live auf gesetze-im-internet.de prüfen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.
