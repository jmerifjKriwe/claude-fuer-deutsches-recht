---
name: dokumententyp-beschluesse
description: "Erkennt Beschluesse: Gesellschafterbeschluesse, Aufsichtsratsbeschluesse, Hauptversammlungsbeschluesse, Vorstandsbeschluesse. Erfasst Beschlussdatum, beschliessende Organe, Beschlussgegenstand und Formerfordernis."
---

> **Hinweis:** Plugin `status-navigator-step-plan`, Dokumentenverarbeitung
> ohne Normen-Anker. Rechtliche Pruefung bleibt anwaltliche Aufgabe.

# Dokumententyp Gesellschafterbeschluesse

## Rolle und Fokus
Erkennt Beschluesse als Dokumentenklasse. Gesellschafterbeschluss, Aufsichtsrats-, Hauptversammlungs-, Vorstandsbeschluss. Erfasst Beschlussdatum, beschliessende Organe, Beschlussgegenstand und Formerfordernis.

## Vorgehen

1. **Beschluss-Identifikation** — Ueberschrift, Einberufungs-/Versammlungs-Bezug, Beschlussformel, Unterschriften.
2. **Organ und Beschlussfaehigkeit** — Welches Organ, welche Mehrheit erforderlich, welche tatsaechlich abgegeben.
3. **Gegenstand katalogisieren** — Geschaeftsfuehrer-Bestellung, Kapitalerhoehung, Zustimmung zu Geschaeft mit Verweis auf Vertragsklausel.
4. **Formerfordernis pruefen** — Notarielle Beurkundung (§ 53 GmbHG), schriftlich, Beschluss im Umlaufverfahren, Stimmboten.
5. **Querverweis auf zustimmungspflichtiges Geschaeft** — Welcher Vertrag baut auf dem Beschluss auf?

## Anwendungsbeispiel
Gesellschafterbeschluss vom 17.10.2025: Zustimmung zum Senior-Darlehensvertrag NordCap und zur Bestellung der Sicherheiten. Beschluss vorhanden, aber Schriftform statt Umlaufbeschluss mit Originalunterschriften aller Gesellschafter — Form steht in der GmbH-Satzung § 11 (verlangt notarielles Protokoll fuer Sicherheitenbestellung > 50 Mio EUR). Klaerungsbedarf.

## Output-Module
- Eintrag in Reiter 2 mit Typ-Tag Beschluss
- Querverweis auf zustimmungspflichtige Vertraege (Reiter 2 Anmerkungsspalte)
- Hinweisliste an `unterschriftspruefung` und ggf. Reiter 3 wenn Form fragwuerdig

## Grenzen
- **Keine rechtliche Wirksamkeitspruefung.** Subsumtion bleibt anwaltliche Aufgabe.
- **Hinweise, keine Befunde.** Markierungen muessen anwaltlich verifiziert werden.
- **Datenschutz und Berufsrecht.** Nutzung nur mit System, das DSGVO, § 203 StGB und §§ 43a, 43e BRAO erfuellt.
