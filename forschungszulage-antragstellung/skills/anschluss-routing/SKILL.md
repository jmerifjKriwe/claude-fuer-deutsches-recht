---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Forschungszulage Antragstellung** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `abgrenzung-adaptiver-antrag` — Abgrenzung Adaptiver Antrag
- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `antragstellung-auszahlung-beihilfen-beweislast` — Antragstellung Auszahlung Beihilfen Beweislast
- `bemessungsgrundlage-interessen-bsfz-definition` — Bemessungsgrundlage Interessen Bsfz Definition
- `forsch-bsfz-pruefung-spezial` — Forsch Bsfz Prüfung Spezial
- `forsch-konzernverbund-forschung-spezial` — Forsch Konzernverbund Forschung Spezial
- `forsch-projektbeschreibung-bauleiter` — Forsch Projektbeschreibung Bauleiter
- `forsch-stundenaufzeichnung-fz-ablehnung-bemessungsgrundlage` — Forsch Stundenaufzeichnung Fz Ablehnung Bemessungsgrundlage
- `forsch-stundenaufzeichnung-leitfaden` — Forsch Stundenaufzeichnung Leitfaden
- `forschungszulage-insolvenzlage-red-portaltexte` — Forschungszulage Insolvenzlage Red Portaltexte
- `fz-ablehnung-nachbesserung-einspruch` — Fz Ablehnung Nachbesserung Einspruch
- `fz-auftragsforschung-vertragsgestaltung` — Fz Auftragsforschung Vertragsgestaltung
- `fz-bemessungsgrundlage-2026` — Fz Bemessungsgrundlage 2026
- `fz-bescheidung-fz-bsfz-fz-dokumentationspaket` — Fz Bescheidung Fz Bsfz Fz Dokumentationspaket

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 FZulG` — Anspruchsberechtigung.
- `§ 2 Abs. 1 FZulG` — begünstigte Forschungs- und Entwicklungsvorhaben.
- `§ 3 FZulG` — förderfähige Aufwendungen und Bemessungsgrundlage.
- `§ 4 FZulG` — Hoehe der Forschungszulage.
- `§ 5 FZulG` — Antrag auf Forschungszulage.
- `§ 6 FZulG` — Bescheinigung.
- `§ 7 FZulG` — Kumulierung mit anderen Förderungen/Beihilfen.
- `§ 10 FZulG` — Festsetzung und Leistung.
- `§ 12 FZulG` — Anwendung der Abgabenordnung.
- `§ 90 Abs. 1 AO` — Mitwirkung und Belegordnung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Ergebnis sichten: Welche Forschungszulage Antragstellung-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Forschungszulage FZulG.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
