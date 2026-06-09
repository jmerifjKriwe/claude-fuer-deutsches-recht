---
name: einstieg-routing
description: "Einstieg, Triage und Routing für Fachanwalt Miet- und Wohnungseigentumsrecht: ordnet Rolle (Mieter, Vermieter, WEG-Eigentümer), markiert Frist (§ 573c BGB Kündigung), wählt Norm (BGB §§ 535-580a, WEG, BetrKV, HeizkostenV) und Zuständigkeit (Amtsgericht Belegenheit (Miete + WEG)), leitet zum passe..."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Fachanwalt Miet Wohnungseigentumsrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `einstieg-schnelltriage-fallrouting` — Abschlusskontrolle WEG Anschluss Router
- `antennen-satellitenschuessel` — Antennen Satellitenschuessel Aufrechnung
- `workflow-bauliche-veraenderung-routing` — Bauliche Veraenderung Betriebskosten
- `baurecht-schnittstelle-miete` — Baurecht Schnittstelle Belegeinsicht
- `beschlussanfechtung-spezial-fristen` — Beschlussanfechtung Abrechnungsfrist
- `betriebskostenverordnung-anlage-3` — Betriebskostenverordnung Anlage 3
- `betrkv-mehrparteien-konflikt-und-interessen` — Betrkv Interessen BGB Co2kostenaufteilung
- `workflow-dokumentenstapel-sortieren` — Dokumentenstapel Sortieren First Year
- `eigenbedarf-personenkreis` — Eigenbedarf Personenkreis Energieausweis
- `steuer-schnittstelle-vermietung` — Fachanwalt Steuer Schnittstelle Erstgespraech
- `gartenpflege-baumfaellung` — Gartenpflege Baumfaellung Gewerberaum
- `workflow-geg-waermepumpe-routing` — GEG Waermepumpe Gerichtstermin Vorbereitung
- `gewerberaum-umsatzmiete` — Gewerberaum Umsatzmiete Gewerberaummiete
- `dokumente-intake` — Dokumente Intake
- `output-waehlen` — Output Waehlen

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Fachanwalt Miet Wohnungseigentumsrecht sind GEG, WEG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
