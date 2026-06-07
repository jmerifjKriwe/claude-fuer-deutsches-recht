---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Zitierweise Deutsches Recht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `aufsatz-interessen-beckrs-blindzitate` — Aufsatz Interessen Beckrs Blindzitate
- `datum-entscheidungsform-spezial-gericht` — Datum Entscheidungsform Gericht
- `hauszitierweise-juristische-kommentar` — Hauszitierweise Juristische Kommentar
- `literatur-live-beweislast-lizenziertem` — Literatur Live Beweislast Lizenziertem
- `rechtsprechung-zit-rechtsprechungszitierung-zitat-eugh` — Rechtsprechung Zit Rechtsprechungszitierung Zitat Eugh
- `verifizierbarer-zugriff-sonderfall-zit-gesetzeszitierung` — Verifizierbarer Zugriff Sonderfall Zit Gesetzeszitierung
- `zit-gesetzeszitierung-bauleiter` — Zit Gesetzeszitierung Bauleiter
- `zit-internationale-urteile-spezial` — Zit Internationale Urteile Spezial
- `zit-internationale-zit-kommentar-zitat-amtliche` — Zit Internationale Zit Kommentar Zitat Amtliche
- `zit-kommentar-aufsatzzitierung-spezial` — Zit Kommentar Aufsatzzitierung Spezial
- `zit-rechtsprechungszitierung-leitfaden` — Zit Rechtsprechungszitierung Leitfaden
- `zitat-amtliche-sammlung-vs-zeitschrift` — Zitat Amtliche Sammlung Vs Zeitschrift
- `zitat-archivierungspflicht` — Zitat Archivierungspflicht

## Regelungs- und Quellenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 130 Nr. 6 ZPO` — Schriftsatzverantwortung und Signatur.
- `§ 130a Abs. 1 ZPO` — elektronische Einreichung.
- `§ 138 Abs. 1 ZPO` — Wahrheitspflicht.
- `§ 253 Abs. 2 ZPO` — bestimmter Vortrag und Antrag.
- `§ 313 Abs. 3 ZPO` — Darstellung der Entscheidungsgruende.
- `§ 540 Abs. 1 ZPO` — Berufungsurteil und Bezugnahmen.
- `§ 267 Abs. 1 StPO` — Urteilsgruende im Strafurteil.
- `§ 117 Abs. 2 VwGO` — Entscheidungsgruende im Verwaltungsprozess.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Ergebnis sichten: Welche Zitierweise Deutsches Recht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Zitierweise deutsches Recht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
