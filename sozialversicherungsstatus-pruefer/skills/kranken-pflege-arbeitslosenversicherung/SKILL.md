---
name: kranken-pflege-arbeitslosenversicherung
description: "Prüft Statusfolgen je Versicherungszweig und vermeidet Gleichsetzung aller Zweige."
---

# Kranken-, Pflege- und Arbeitslosenversicherung

## Fachkern: Kranken-, Pflege- und Arbeitslosenversicherung
- **Spezialgegenstand:** Kranken-, Pflege- und Arbeitslosenversicherung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** SGB IV § 7/§ 7a, SGB VI, SGB III, SGB V, SGB XI, DRV-Statusfeststellung, Beitragsnachforderung, Säumniszuschläge und Lohnsteuer-Schnittstelle.
- **Entscheidende Weiche:** Prüfe Eingliederung, Weisungsrecht, Unternehmerrisiko, Vergütung, Exklusivität, Auftreten am Markt, Sperrminorität und gelebte Praxis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das Sozialversicherungsstatus-Plugin prüft Beschäftigung, Selbständigkeit, Scheinselbständigkeit und Statusfeststellung für Geschäftsführer, Freelancer, Anwälte, Lehrer, Musikschulen, Plattformarbeit und andere Arbeitsformen nach deutscher Sozialversicherungssystematik.

Dieser Skill macht aus **Kranken-, Pflege- und Arbeitslosenversicherung** einen belastbaren Workflow: erst Rolle und Ziel, dann Rechtsanker, tatsächliche Praxis, Dokumente, Risiken, Gegenargumente und verwertbarer Output.

## Rechts- und Quellenanker

- SGB V
- SGB XI
- SGB III
- SGB IV

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Welche Versicherungszweige sind vom Bescheid betroffen?
- Gibt es Sonderregeln, Befreiungen, Vorversicherungen oder freiwillige Versicherung?
- Wie wirken Beiträge und Leistungsansprüche rückwirkend?
- Welche Stelle muss beteiligt werden?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Welche Versicherungszweige sind vom Bescheid betroffen?
- Gibt es Sonderregeln, Befreiungen, Vorversicherungen oder freiwillige Versicherung?
- Wie wirken Beiträge und Leistungsansprüche rückwirkend?
- Welche Stelle muss beteiligt werden?

**Mindest-Output:** Versicherungszweig-Matrix mit Statusfolge, Beitrag und Zuständigkeit.

## Qualitäts- und Risikofilter

- Vertragsetiketten nie übernehmen: Entscheidend ist die Gesamtwürdigung aus Vertrag und gelebter Praxis.
- Sondertatbestände wie SGB VI § 2, KSVG, Minijob, AÜG, Geschäftsführer-Sperrminorität und Cross-border immer als eigene Abzweige prüfen.
- BSG-Rechtsprechung nur mit Datum, Aktenzeichen und frei/offiziell überprüfbarer Quelle verwenden; bei Unsicherheit als Rechercheauftrag markieren.
- Bei Beitrags-, Straf- oder Betriebsprüfungsrisiko keine lockere Entwarnung geben, sondern Zeiträume, Versicherungszweige und Belege konkretisieren.
