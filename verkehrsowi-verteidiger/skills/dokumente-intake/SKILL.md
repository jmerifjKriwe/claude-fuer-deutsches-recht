---
name: dokumente-intake
description: "Dokumentenintake für Verkehrs-OWi-Verteidigung: sortiert Bußgeldbescheid, Anhörungsbogen, Messprotokoll, prüft Datum, Absender, Frist und Beweiswert (Messprotokoll, Rohmessdaten); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Aktenstart statt Formularstart

Wenn zu **Dokumente Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Verkehrsowi Verteidiger** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Einsatzlage

Dieser Dokumenten-Intake für **Verkehrsowi Verteidiger** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `abstand-quellenkarte` — Abstand Quellenkarte
- `akteneinsicht-internationaler-bezug-und-schnittstellen` — Akteneinsicht Internationaler Bezug und Schnittstellen
- `alkohol-compliance-dokumentation-und-akte` — Alkohol Compliance Dokumentation und Akte
- `alkohol-drogen-beweisverwertung` — Alkohol Drogen Beweisverwertung
- `amtsgericht-drogen-interessen-einspruch` — Amtsgericht Drogen Interessen Einspruch
- `anhoerung-verkehrsowi-einspruch-messverfahren` — Anhoerung Verkehrsowi Einspruch Messverfahren
- `bussgeldbescheid-tatbestand-beweis-und-belege` — Bussgeldbescheid Tatbestand Beweis und Belege
- `drogen-mehrparteien-konflikt-und-interessen` — Drogen Mehrparteien Konflikt und Interessen
- `einspruch-dokumentenmatrix-und-lueckenliste` — Einspruch Dokumentenmatrix und Lueckenliste
- `fahrverbot-geschwindigkeit-handy` — Fahrverbot Geschwindigkeit Handy
- `geschwindigkeit-verhandlung-vergleich-und-eskalation` — Geschwindigkeit Verhandlung Vergleich und Eskalation
- `handy-zahlen-schwellen-und-berechnung` — Handy Zahlen Schwellen und Berechnung
- `hauptverhandlung-sonderfall-messakte-messung` — Hauptverhandlung Sonderfall Messakte Messung
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Verkehrsowi Verteidiger-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
