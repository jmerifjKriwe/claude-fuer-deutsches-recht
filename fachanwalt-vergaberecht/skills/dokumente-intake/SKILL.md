---
name: dokumente-intake
description: "Dokumentenintake für Fachanwalt Vergaberecht: sortiert Vergabeunterlagen, Angebot, Wertungsvermerk, prüft Datum, Absender, Frist und Beweiswert (Submissionsprotokoll, Vergabeakten); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Aktenstart statt Formularstart

Wenn zu **Dokumente Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Fachanwalt Vergaberecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Einsatzlage

Dieser Dokumenten-Intake für **Fachanwalt Vergaberecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `aufklaerung` — Aufklaerung
- `ausschluss-bieter-paragraf-124-gwb` — Ausschluss Bieter Paragraf 124 GWB
- `bieterstrategie-go-eforms-ted-eignung` — Bieterstrategie GO Eforms TED Eignung
- `eignungskriterien-paragraf-122-gwb` — Eignungskriterien Paragraf 122 GWB
- `eu-schwelle-vergabeordnung-richtlinie-2014-24` — EU Schwelle Vergabeordnung Richtlinie 2014 24
- `facto` — Facto
- `facto-vergabe` — Facto Vergabe
- `it-sicherheits-konzessionsvergabe-konzvgv` — IT Sicherheits Konzessionsvergabe Konzvgv
- `kaltstart-triage` — Kaltstart Triage
- `konzvgv-rahmenvereinbarung-international` — Konzvgv Rahmenvereinbarung International
- `mandantenpadlet-vergabe-triage-vergaberecht` — Mandantenpadlet Vergabe Triage Vergaberecht
- `nachpruefungsverfahren-paragraf-160-gwb` — Nachpruefungsverfahren Paragraf 160 GWB
- `nebenabrede-paragraf-58-vgv` — Nebenabrede Paragraf 58 VGV
- `einstieg-routing` — Einstieg Routing
- `output-waehlen` — Output Waehlen

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Fachanwalt Vergaberecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Bieter.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
