---
name: dokumente-intake
description: "Dokumentenintake für Urteilsbauer/Relationsmacher: sortiert Klage, Klageerwiderung, Beweisaufnahme, prüft Datum, Absender, Frist und Beweiswert (Beweisaufnahme-Ergebnis); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Aktenstart statt Formularstart

Wenn zu **Dokumente Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Urteilsbauer Relationsmacher** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Einsatzlage

Dieser Dokumenten-Intake für **Urteilsbauer Relationsmacher** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `aktenintake-schriftsatz-brief-und-memo-bausteine` — Aktenintake Schriftsatz Brief und Memo Bausteine
- `aktenintake-zivil` — Aktenintake Zivil
- `amts-aktenintake-zivil-anspruchsgrundlagen` — Amts Aktenintake Zivil Anspruchsgrundlagen
- `amts-fristen-form-zustaendigkeit` — Amts Fristen Form Zustaendigkeit
- `anspruchsgrundlagen-pruefen` — Anspruchsgrundlagen Pruefen
- `berufungsfest-beschluss-bauen-beweisbeschluss` — Berufungsfest Beschluss Bauen Beweisbeschluss
- `berufungsfest-pruefen` — Berufungsfest Pruefen
- `beschluss-bauen-zpo` — Beschluss Bauen ZPO
- `beschluss-tatbestand-beweis-und-belege` — Beschluss Tatbestand Beweis und Belege
- `beschluss-tatbestandsmerkmale` — Beschluss Tatbestandsmerkmale
- `beweisbeschluss-vorbereiten` — Beweisbeschluss Vorbereiten
- `beweiswuerdigung-mit-richter-input` — Beweiswuerdigung mit Richter Input
- `beweiswuerdigung-quellenkarte` — Beweiswuerdigung Quellenkarte
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Urteilsbauer Relationsmacher-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: ZPO — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
