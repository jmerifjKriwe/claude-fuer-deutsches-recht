---
name: dokumente-intake
description: "Dokumentenintake für Fachanwalt Versicherungsrecht: sortiert Versicherungsschein, AVB, Schadensanzeige, prüft Datum, Absender, Frist und Beweiswert (Schadensbilder, SV-Gutachten Schaden); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Aktenstart statt Formularstart

Wenn zu **Dokumente Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Fachanwalt Versicherungsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Einsatzlage

Dieser Dokumenten-Intake für **Fachanwalt Versicherungsrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `berufsunfaehigkeit-paragraf-172-vvg` — Berufsunfaehigkeit Paragraf 172 VVG
- `versr-bu-anerkennt-was-spezial` — BU Anerkennt Leistungspruefung
- `cyber-loesegeld-sanktionsrecht` — Cyber Loesegeld Versr Deckungsanfrage
- `versr-d-o-claims-made-ausschluesse` — D O Spezialfall Deckungsklage Leitfaden
- `deckungsklage-mehrparteien-konflikt-und-interessen` — Deckungsklage Interessen Deckungspruefung
- `versr-deckungsprozess-215-vvg-beweislast` — Deckungsprozess VVG Einfuehrung Themen
- `do-deckungsabwehr` — DO Deckungsabwehr Lebensversicherung
- `erstgespraech-mandatsannahme` — Erstgespraech Mandatsannahme
- `einstieg-schnelltriage-fallrouting` — FA Versicherungsrecht Start Chronologie Fristen
- `erstpruefung-und-mandatsziel` — Fachanwalt Kanzlei Krankenversicherung
- `fehlerkatalog` — Fehlerkatalog
- `gebaeudeversicherung-paragraf-86-vvg` — Gebaeudeversicherung Paragraf 86 VVG
- `haftpflicht-paragraf-100-vvg` — Haftpflicht Paragraf 100 VVG
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Fachanwalt Versicherungsrecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: VAG, VVG — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
