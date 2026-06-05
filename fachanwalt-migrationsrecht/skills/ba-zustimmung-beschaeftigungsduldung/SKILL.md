---
name: ba-zustimmung-beschaeftigungsduldung
description: "Ba Zustimmung Beschaeftigung, Beschaeftigungsduldung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ba Zustimmung Beschaeftigung, Beschaeftigungsduldung

## Arbeitsbereich

In diesem Skill wird **Ba Zustimmung Beschaeftigung, Beschaeftigungsduldung** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-ba-zustimmung-beschaeftigung` | BA-Zustimmung Beschäftigung: Fachmodul im Migrationsrecht; prüft Zustimmungserfordernis, Vorrang/Arbeitsbedingungen, Ausnahmen; mit deutschem Recht, EU/EMRK/GFK, Belegen, Fristen und Quellencheck. |
| `spezial-beschaeftigungsduldung` | Beschäftigungsduldung: Fachmodul im Migrationsrecht; prüft Beschäftigungszeiten, Lebensunterhalt, Identität, Straffreiheit; mit deutschem Recht, EU/EMRK/GFK, Belegen, Fristen und Quellencheck. |

## Arbeitsweg

Für **Ba Zustimmung Beschaeftigung, Beschaeftigungsduldung** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `fachanwalt-migrationsrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-ba-zustimmung-beschaeftigung`

**Fokus:** BA-Zustimmung Beschäftigung: Fachmodul im Migrationsrecht; prüft Zustimmungserfordernis, Vorrang/Arbeitsbedingungen, Ausnahmen; mit deutschem Recht, EU/EMRK/GFK, Belegen, Fristen und Quellencheck.

# BA-Zustimmung Beschäftigung

## Aufgabe
Fachmodul im Plugin `fachanwalt-migrationsrecht`. Er bearbeitet: prüft Zustimmungserfordernis, Vorrang/Arbeitsbedingungen, Ausnahmen.

## Einstieg
1. Wer ist betroffen, wer fragt, und welches konkrete Ziel besteht?
2. Welche Staatsangehörigkeit/Gebietszuordnung, welcher Aufenthaltsort und welcher aktuelle Status liegen vor?
3. Welche Frist oder welches Eilrisiko entscheidet den Fall?
4. Welche Unterlagen beweisen Identität, Status, Familie, Arbeit, Ausbildung, Schutzgrund oder Gesundheit?
5. Soll das Ergebnis auf Deutsch, in einfacher Sprache oder zusätzlich auf Spanisch ausgegeben werden?

## Prüfraster
1. **Status und Ziel:** Ist der passende Titel/Schutz-/Rechtsbehelfspfad richtig gewählt?
2. **Tatbestand:** Normmerkmale, Ausnahmen, Ermessen, Versagungsgründe und Gegenargumente.
3. **EU/EMRK/GFK:** Unionsrechtliche oder menschenrechtliche Ebene prüfen, wenn sie den Fall tragen kann.
4. **Staatenbezug:** Herkunfts-, Transit- und Zielstaat nur mit aktuellen Quellen bewerten; keine statischen Sicherheitsannahmen.
5. **Beweis:** Dokumente, Urkunden, Übersetzungen, Atteste, Länderquellen und digitale Belege sauber trennen.
6. **Taktik:** Antrag, Nachreichung, Fristverlängerung, Eilantrag, Klage, Vergleich, Behördenkommunikation.

## Output
- Kurzlage und Risikoampel.
- Prüfmatrix: Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- Direkt nutzbarer Textbaustein für Behörde, Gericht, Arbeitgeber oder Mandant.
- Anschluss-Skills innerhalb dieses Plugins.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 2. `spezial-beschaeftigungsduldung`

**Fokus:** Beschäftigungsduldung: Fachmodul im Migrationsrecht; prüft Beschäftigungszeiten, Lebensunterhalt, Identität, Straffreiheit; mit deutschem Recht, EU/EMRK/GFK, Belegen, Fristen und Quellencheck.

# Beschäftigungsduldung

## Aufgabe
Fachmodul im Plugin `fachanwalt-migrationsrecht`. Er bearbeitet: prüft Beschäftigungszeiten, Lebensunterhalt, Identität, Straffreiheit.

## Einstieg
1. Wer ist betroffen, wer fragt, und welches konkrete Ziel besteht?
2. Welche Staatsangehörigkeit/Gebietszuordnung, welcher Aufenthaltsort und welcher aktuelle Status liegen vor?
3. Welche Frist oder welches Eilrisiko entscheidet den Fall?
4. Welche Unterlagen beweisen Identität, Status, Familie, Arbeit, Ausbildung, Schutzgrund oder Gesundheit?
5. Soll das Ergebnis auf Deutsch, in einfacher Sprache oder zusätzlich auf Spanisch ausgegeben werden?

## Prüfraster
1. **Status und Ziel:** Ist der passende Titel/Schutz-/Rechtsbehelfspfad richtig gewählt?
2. **Tatbestand:** Normmerkmale, Ausnahmen, Ermessen, Versagungsgründe und Gegenargumente.
3. **EU/EMRK/GFK:** Unionsrechtliche oder menschenrechtliche Ebene prüfen, wenn sie den Fall tragen kann.
4. **Staatenbezug:** Herkunfts-, Transit- und Zielstaat nur mit aktuellen Quellen bewerten; keine statischen Sicherheitsannahmen.
5. **Beweis:** Dokumente, Urkunden, Übersetzungen, Atteste, Länderquellen und digitale Belege sauber trennen.
6. **Taktik:** Antrag, Nachreichung, Fristverlängerung, Eilantrag, Klage, Vergleich, Behördenkommunikation.

## Output
- Kurzlage und Risikoampel.
- Prüfmatrix: Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- Direkt nutzbarer Textbaustein für Behörde, Gericht, Arbeitgeber oder Mandant.
- Anschluss-Skills innerhalb dieses Plugins.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.
