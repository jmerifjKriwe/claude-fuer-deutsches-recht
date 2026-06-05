---
name: handelskauf-fristenampel-hgb
description: "Nutze dies, wenn Workflow Handelskauf Fristenampel, Workflow Hgb Erstpruefung im Plugin Handelsrecht Hgb konkret bearbeitet werden soll. Auslöser: Bitte Workflow Handelskauf Fristenampel, Workflow Hgb Erstpruefung prüfen.; Erstelle eine Arbeitsfassung zu Workflow Handelskauf Fristenampel, Workflow Hgb Erstpruefung.; Welche Normen und Nachweise brauche ich?."
---

# Workflow Handelskauf Fristenampel, Workflow Hgb Erstpruefung

## Zweck

Dieser Skill ist ein eigenständiger Arbeitsbereich. Er verbindet mehrere sachlich benachbarte Arbeitsmodule. Wähle anhand des Sachverhalts das passende Modul, arbeite dessen Prüfroutine vollständig ab und kombiniere Module nur, wenn der Fall tatsächlich mehrere Themen berührt.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `workflow-handelskauf-fristenampel` | Macht Fristenampel für Rüge, Lieferung, Fixgeschäft, Annahmeverzug, Verjährung und Beweise. |
| `workflow-hgb-erstpruefung` | Prüft in fünf Schritten, ob ein HGB-Fall vorliegt und welche Sonderregeln das BGB überlagern. |

## Arbeitsweg

Für **Workflow Handelskauf Fristenampel, Workflow Hgb Erstpruefung** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `handelsrecht-hgb` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `workflow-handelskauf-fristenampel`

**Fokus:** Macht Fristenampel für Rüge, Lieferung, Fixgeschäft, Annahmeverzug, Verjährung und Beweise.

# Handelskauf-Fristenampel

## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Arbeitsweise

Besonders § 377 HGB, kaufmännische Untersuchungsobliegenheit und Zugang.

## Rechts- und Quellenanker

HGB amtlich prüfen: https://www.gesetze-im-internet.de/hgb/. Je nach Thema außerdem BGB, FamFG, HRV, BeurkG, GmbHG, AktG und EU-/internationales Recht live gegenprüfen.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Kurzvotum
- Register-/Vertrags-/Prozessfahrplan
- Beweis- und Dokumentenliste
- Risikoampel
- Anschluss-Skills


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `workflow-hgb-erstpruefung`

**Fokus:** Prüft in fünf Schritten, ob ein HGB-Fall vorliegt und welche Sonderregeln das BGB überlagern.

# HGB Erstprüfung

## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Arbeitsweise

Kaufmannseigenschaft, Handelsgeschäft, Registerlage, Vertretung und Beweis-/Fristenfolgen erfassen.

## Rechts- und Quellenanker

HGB amtlich prüfen: https://www.gesetze-im-internet.de/hgb/. Je nach Thema außerdem BGB, FamFG, HRV, BeurkG, GmbHG, AktG und EU-/internationales Recht live gegenprüfen.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Kurzvotum
- Register-/Vertrags-/Prozessfahrplan
- Beweis- und Dokumentenliste
- Risikoampel
- Anschluss-Skills


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
