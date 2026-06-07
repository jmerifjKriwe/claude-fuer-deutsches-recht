---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Zitierweise Deutsches Recht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

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

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Zitierweise Deutsches Recht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Autor.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
