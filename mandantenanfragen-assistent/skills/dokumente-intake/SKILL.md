---
name: dokumente-intake
description: "Dokumentenintake für Mandantenanfragen-Assistent: sortiert Mandantenmail, Kanzleiprofil, Honorarinfo, prüft Datum, Absender, Frist und Beweiswert (Urkunden, Zeugen); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Aktenstart statt Formularstart

Wenn zu **Dokumente Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Mandantenanfragen Assistent** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Einsatzlage

Dieser Dokumenten-Intake für **Mandantenanfragen Assistent** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `anfrage-eingang-parser` — Anfrage Eingang Parser
- `anrede-anwaltskanzleien-bittet` — Anrede Anwaltskanzleien Bittet
- `anrede-uebernehmen` — Anrede Uebernehmen
- `anwaltskanzleien-erstpruefung-und-mandatsziel` — Anwaltskanzleien Erstpruefung und Mandatsziel
- `bietet-fehlerkatalog` — Bietet Fehlerkatalog
- `bittet-internationaler-bezug-und-schnittstellen` — Bittet Internationaler Bezug und Schnittstellen
- `dankt-dsgvo-sonderfall-e-mail` — Dankt DSGVO Sonderfall E Mail
- `dringlichkeitsmarker-einwilligung-hinweis` — Dringlichkeitsmarker Einwilligung Hinweis
- `dsgvo-sonderfall-und-edge-case` — DSGVO Sonderfall und Edge Case
- `e-mail-erstantwort-und-terminrouting` — E Mail Erstantwort und Terminrouting
- `eingehenden-quellenkarte` — Eingehenden Quellenkarte
- `einwilligung-hinweis-datenschutz` — Einwilligung Hinweis Datenschutz
- `einwilligungshinweis-fristennotiz-und-naechster-schritt` — Einwilligungshinweis Fristennotiz und Naechster Schritt
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Mandantenanfragen Assistent-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: DSGVO — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
