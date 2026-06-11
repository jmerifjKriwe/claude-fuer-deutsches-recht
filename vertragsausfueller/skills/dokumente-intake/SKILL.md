---
name: dokumente-intake
description: "Dokumentenintake für Vertragsausfüller: sortiert Vertragsentwurf, Mustervertrag, Anlagen, prüft Datum, Absender, Frist und Beweiswert (Verhandlungs-Korrespondenz); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Aktenstart statt Formularstart

Wenn zu **Dokumente Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Vertragsausfueller** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Einsatzlage

Dieser Dokumenten-Intake für **Vertragsausfueller** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `altvertraege-dokumentenmatrix-und-lueckenliste` — Altvertraege Dokumentenmatrix und Lueckenliste
- `altvertrag-nachziehen` — Altvertrag Nachziehen
- `ausdruecklicher-fristennotiz-und-naechster-schritt` — Ausdruecklicher Fristennotiz und Naechster Schritt
- `batch-modus-docx-stripper-einfuehrung` — Batch Modus Docx Stripper Einfuehrung
- `bsag-mietvertrag-klauselentscheidung` — Bsag Mietvertrag Klauselentscheidung
- `changes-beweislast-docx-erkennen` — Changes Beweislast Docx Erkennen
- `clean-output` — Clean Output
- `docx-stripper` — Docx Stripper
- `docx-tatbestand-beweis-und-belege` — Docx Tatbestand Beweis und Belege
- `einfuehrung-prozess` — Einfuehrung Prozess
- `erkennen-schriftsatz-brief-und-memo-bausteine` — Erkennen Schriftsatz Brief und Memo Bausteine
- `erzeugen-red-fassungen-sonderfall-felder` — Erzeugen RED Fassungen Sonderfall Felder
- `fassungen-sonderfall-und-edge-case` — Fassungen Sonderfall und Edge Case
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Mustervertrag, Termsheet, Klauselkatalog, Altvertrag, Vertragsentwurf mit Track Changes.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Vertragsausfüller (Lückenschluss in Verträgen)-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: BGB §§ 133, 157, 305–310, 311b, 311c, 433, 488, 535, 631, 651a, 765, AGB-Recht, NachwG, FormularG — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Vertragspartner, Rechtsabteilung, Notar bei Formerfordernis prüfen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
