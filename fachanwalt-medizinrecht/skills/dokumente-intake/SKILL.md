---
name: dokumente-intake
description: "Dokumentenintake für Fachanwalt Medizinrecht: sortiert Behandlungsvertrag, Patientenakte, Aufklärungsbogen, prüft Datum, Absender, Frist und Beweiswert (Patientenakte, SV-Gutachten Arzthaftung); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Aktenstart statt Formularstart

Wenn zu **Dokumente Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Fachanwalt Medizinrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Einsatzlage

Dieser Dokumenten-Intake für **Fachanwalt Medizinrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `aerzte-quellenkarte` — Aerzte Quellenkarte
- `aerztewerbung-innovative-therapie` — Aerztewerbung Innovative Amnog Millionen
- `anaesthesie-hochrisiko-aufklaerung` — Anaesthesie Hochrisiko Approbation Digitales
- `apothekenrecht-arzneimittel-paragraf-78-amg` — Apothekenrecht Arzneimittel Paragraf 78 AMG
- `apothekenrecht-mehrparteien-konflikt-und-interessen` — Apothekenrecht Interessen Aufklaerung
- `arzthaftung-aufklaerung-bgb` — Arzthaftung Aufklaerung BGB
- `atmp-chain-of-identity` — Atmp Chain Classification
- `atmp-pharmakovigilanz-rmp` — Atmp Pharmakovigilanz Aufklaerungsfehler
- `aufklaerungsfehler` — Aufklaerungsfehler Behandlungsfehler
- `aufklaerungspflicht-paragraf-630e-bgb` — Aufklaerungspflicht Paragraf 630e BGB
- `behandlungsfehler-paragraf-630h-bgb` — Behandlungsfehler Paragraf 630h BGB
- `berufsrecht-verhandlung-vergleich-und-eskalation` — Berufsrecht BGB Einwilligung Sonderfall
- `beweislast-hightech-medizin` — Beweislast Hightech Biobank Consent
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Fachanwalt Medizinrecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: BGB, MPDG, SGB V, §§ 630a ff — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
