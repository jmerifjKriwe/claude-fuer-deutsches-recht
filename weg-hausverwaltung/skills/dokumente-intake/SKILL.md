---
name: dokumente-intake
description: "Dokumentenintake für WEG/Hausverwaltung: sortiert TE/GO, Versammlungsprotokoll, Wirtschaftsplan, prüft Datum, Absender, Frist und Beweiswert (Beschlusssammlung, Versammlungsprotokoll); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Aktenstart statt Formularstart

Wenn zu **Dokumente Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Weg Hausverwaltung** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Einsatzlage

Dieser Dokumenten-Intake für **Weg Hausverwaltung** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `abrechnung-ist-plan-mieterschnittstelle` — Abrechnung IST Plan Mieterschnittstelle
- `anwalt-amtsgericht-gewerbe-restaurant` — Anwalt Amtsgericht Gewerbe Restaurant
- `bad-umbau-barrierefreie-einladung-bauliche` — BAD Umbau Barrierefreie Einladung Bauliche
- `bad-umbau-bodengleiche-dusche-sondereigentum` — BAD Umbau Bodengleiche Dusche Sondereigentum
- `barrierefreie-einladung-protokoll-versammlung` — Barrierefreie Einladung Protokoll Versammlung
- `bauliche-veraenderung-aufzug-treppenlift-20` — Bauliche Veraenderung Aufzug Treppenlift 20
- `bauliche-veraenderungen-20-weg` — Bauliche Veraenderungen 20 WEG
- `bauliche-veraenderungen-beirat-controlling` — Bauliche Veraenderungen Beirat Controlling
- `beirat-controlling-verwalter` — Beirat Controlling Verwalter
- `beschlussanfechtung-risiko` — Beschlussanfechtung Risiko
- `beschlusssammlung-betriebskosten-interessen` — Beschlusssammlung Betriebskosten Interessen
- `beschlusssammlung-protokoll` — Beschlusssammlung Protokoll
- `beschlusssammlung-protokoll-beschlussvorlagen` — Beschlusssammlung Protokoll Beschlussvorlagen
- `einstieg-routing` — Einstieg Routing
- `output-waehlen` — Output Waehlen

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Eigentümerversammlungsprotokoll, Beschlusssammlung, Jahresabrechnung, Wirtschaftsplan, Verwaltervertrag, Teilungserklärung, Gemeinschaftsordnung.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die WEG-Hausverwaltung-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: WEG §§ 9a, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 44, 45, 46, 47, BGB §§ 535 ff., HOAI, BetrKV — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Verwalter, Eigentümergemeinschaft, Verwaltungsbeirat, AG der Belegenheit, Handwerker, Vorverwalter prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an WEG-Eigentümer.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
