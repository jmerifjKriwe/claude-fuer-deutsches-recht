---
name: unterlagen-luecken
description: "Nutze dies, wenn Unterlagen und Lücken im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeitet werden soll. Auslöser: Ich lade Unterlagen hoch.; Was fehlt noch?; Bitte Dokumente sortieren.."
---

# Unterlagen und Lücken

## Einsatzlage

Nutze diesen Skill, wenn im Bereich **Insolvenzforderungsanmeldungspruefung** ein Fall noch sortiert, Dokumente eingeordnet, Quellen geprüft oder der nächste Arbeitsweg gewählt werden muss. Der Skill soll nicht allgemein reden, sondern schnell in den passenden Fachpfad führen.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Workflow Chronologie Workflow Fristen
- `feststellung-forderungsgrund-rang-grund` — Feststellung Forderungsgrund Rang Grund
- `iap-anmeldepruefung-bauleiter-aussonderung-absonderung` — Iap Anmeldepruefung Bauleiter Aussonderung Absonderung
- `iap-rangordnung-ifap-aktenanlage-ifap-beleg` — Iap Rangordnung Ifap Aktenanlage Ifap Beleg
- `ifap-dubletten-serienforderungen-formalpruefung-grund-betrag` — Ifap Dubletten Serienforderungen Formalpruefung Grund Betrag
- `ifap-insolvenzforderungsanmeldungspruefung-intake` — Ifap Insolvenzforderungsanmeldungspruefung Intake
- `ifap-intake-kanalcheck-masseverbindlichkeit-abgrenzen` — Ifap Intake Kanalcheck Masseverbindlichkeit Abgrenzen
- `ifap-nachtraegliche-anmeldung-pruefungstermin-gate` — Ifap Nachtraegliche Anmeldung Pruefungstermin Gate
- `ifap-pruefentscheidung-vbuh` — Ifap Pruefentscheidung Vbuh
- `ifap-rang-nachrang-schuldnerwiderspruch-streitige-forderung` — Ifap Rang Nachrang Schuldnerwiderspruch Streitige Forderung
- `ifap-tabellenauszug-tabellenimport-verteilung-bestrittene` — Ifap Tabellenauszug Tabellenimport Verteilung Bestrittene
- `kanalcheck-beweislast-masseverbindlichkeit-sonderfall` — Kanalcheck Beweislast Masseverbindlichkeit Sonderfall
- `rang-tabellenauszug-tabellenimport` — Rang Tabellenauszug Tabellenimport
- `vbuh` — Vbuh

## Arbeitsweg

- Fehlende Tatsachen von fehlenden Belegen trennen.
- Für jedes fehlende Dokument sagen, wofür es gebraucht wird und welche Ersatzbelege möglich sind.
- Priorität nach Frist, Beweislast, materieller Voraussetzung und taktischem Nutzen setzen.
- Lücken nicht verstecken: sie werden als Arbeitsauftrag formuliert.

## Output

Lückenliste mit Priorität, Beweiszweck, Beschaffungsweg, Frist und Ersatznachweis.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Skill passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
