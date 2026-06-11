---
name: dokumente-intake
description: "Dokumentenintake für Geldwäscheprävention AML/KYC: sortiert KYC-Akte, Risk Assessment, Compliance-Manual, prüft Datum, Absender, Frist und Beweiswert (Dokumente wirtschaftlich Berechtigter, Transaction Logs); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Aktenstart statt Formularstart

Wenn zu **Dokumente Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Geldwaeschepraevention Aml Kyc** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Einsatzlage

Dieser Dokumenten-Intake für **Geldwaeschepraevention Aml Kyc** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `aml-kryptotransaktionen-mica-spezial` — AML Kryptotransaktionen Mica Spezial
- `aml-kyc-start-chronologie-fristen` — AML KYC Start Chronologie Fristen
- `aml-trade-based-money-laundering-spezial` — AML Trade Based Money Laundering Spezial
- `aml-verdachtsmeldung-fiu-leitfaden` — AML Verdachtsmeldung FIU Leitfaden
- `awareness-zahlen-schwellen-und-berechnung` — Awareness Zahlen Schwellen und Berechnung
- `behoerdenverfahren-schriftsatz-brief-und-memo-bausteine` — Behoerdenverfahren Schriftsatz Brief und Memo Bausteine
- `geldwaesche-audit-internal-datenqualitaet` — Geldwaesche Audit Internal Datenqualitaet
- `geldwaesche-behoerdenverfahren` — Geldwaesche Behoerdenverfahren
- `geldwaesche-bussgeld-reputation` — Geldwaesche Bussgeld Reputation
- `geldwaesche-datenqualitaet-register` — Geldwaesche Datenqualitaet Register
- `geldwaesche-gruppenweite-compliance` — Geldwaesche Gruppenweite Compliance
- `geldwaesche-immobilien-gueterhaendler` — Geldwaesche Immobilien Gueterhaendler
- `geldwaesche-krypto-zahlungsdienstleister` — Geldwaesche Krypto Zahlungsdienstleister
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Geldwaeschepraevention Aml Kyc-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: GwG — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
