---
name: email-eingangsanalyse
description: "Liest den Eingangstext einer E-Mail und identifiziert emotionale Trigger wie Schimpfwoerter, Grossbuchstaben, Ausrufezeichen-Ketten, persoenliche Angriffe, Sarkasmus und Drohgesten. Bewertet den Konfliktgrad als gering, mittel oder hoch."
---

# E-Mail-Eingangsanalyse

Dieser Skill analysiert einen eingegangenen E-Mail-Text systematisch auf emotionale Belastung, unsachliche Formulierungen und potenzielle berufsrechtliche Risiken. Er bildet die Grundlage für alle nachfolgenden Umformulierungsschritte.

## Analyseebenen

Die Eingangsanalyse untersucht den Text auf vier Ebenen: sprachliche Auffälligkeiten (Schimpfwörter, Großbuchstaben, übermäßige Satzzeichen), rhetorische Stilmittel (Sarkasmus, Ironie, Übertreibung), inhaltliche Vorwürfe (Kompetenzabsprache, Unterstellungen, Drohungen) sowie strukturelle Mängel (fehlende sachliche Begründung, reine Emotionsäußerung ohne Kernbotschaft).

## Konfliktgrad-Klassifikation

Der Skill kategorisiert den Konfliktgrad in drei Stufen. Gering bedeutet: einzelne unhöfliche Formulierungen, sachlicher Kern erkennbar, kein persönlicher Angriff. Mittel bedeutet: mehrere emotionale Trigger, Vorwürfe an die Person, Drohgebärde oder Ultimatum. Hoch bedeutet: überwiegend unsachlich, persönliche Herabsetzung, Schimpfwörter oder strafrechtlich relevante Äußerungen.

## Trigger-Kategorien

Die wichtigsten emotionalen Trigger sind: Großschreibung ganzer Wörter oder Sätze (impliziert Schreien), Ausrufezeichen-Ketten (erzeugen aggressiven Ton), direkte persönliche Anreden mit Vorwurf-Charakter ("Sie haben...", "Sie sind..."), implizite oder explizite Drohungen ("Ich werde...", "Das hat Konsequenzen"), Sarkasmus und Ironie (untergraben sachliche Auseinandersetzung) sowie Pauschalurteile ohne Sachverhaltsbezug.

## Berufsrechtlicher Hintergrund

§ 43a Abs. 3 BRAO verpflichtet Rechtsanwälte zur Sachlichkeit in der beruflichen Kommunikation. Die Weiterleitung oder das Zitieren eines unsachlichen Eingangsschreibens ohne Analyse kann dazu verleiten, im eigenen Schreiben denselben Ton zu übernehmen — was berufsrechtlich problematisch ist. Die Eingangsanalyse hilft, eine bewusste Distanz zum emotionalen Gehalt herzustellen.

## Beispiele Vorher/Nachher

**Vorher:** „SIE HABEN MIR NICHT GEANTWORTET!!! Das ist eine Frechheit!!!"
**Nachher (Analyse):** Konfliktgrad hoch. Trigger: Großbuchstaben, Mehrfach-Ausrufezeichen, Vorwurf fehlender Reaktion. Kern: Bitte um Rückmeldung auf ein früheres Schreiben.

**Vorher:** „Ich erwarte sofort eine Erklärung, sonst schalte ich meinen Anwalt ein."
**Nachher (Analyse):** Konfliktgrad mittel. Trigger: Drohgebärde, Ultimatum. Kern: Bitte um Stellungnahme zu einem bestimmten Sachverhalt.

**Vorher:** „Ihre Kollegin hat mir versprochen, dass das erledigt wird. Offenbar sind dort alle unfähig."
**Nachher (Analyse):** Konfliktgrad mittel-hoch. Trigger: Pauschalurteil, Kompetenzabsprache. Kern: Unerfüllte Zusage eines Mitarbeiters; Klärungsbedarf.

## Ausgabeformat

Der Skill gibt aus: (1) Tabellarische Trigger-Liste mit Zitat, Trigger-Typ und Einordnung. (2) Konfliktgrad-Einschätzung (gering/mittel/hoch) mit Begründung. (3) Sachlicher Kerninhalt in einem Satz. (4) Empfehlung, welche weiteren Skills zur Umformulierung einzusetzen sind.
