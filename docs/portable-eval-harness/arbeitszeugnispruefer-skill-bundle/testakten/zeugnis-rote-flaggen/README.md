# Test-Zeugnis mit roten Flaggen (Note 4)

Eingabe fuer den Skill. Erwarteter Output: Gesamtnote 4, multiple rote Flaggen
erkannt, Berichtigungsempfehlung vorhanden.

## Zeugnis-Volltext

> **Beispiel GmbH | Beispielstrasse 5 | 20000 Beispielstadt**
>
> **Arbeitszeugnis**
>
> Herr Thomas Beispiel war vom 1. Januar 2020 bis zum 30. Juni 2024 als Vertriebsmitarbeiter beschaeftigt.
>
> **Leistungsbeurteilung:** Herr Beispiel verfuegt ueber ausreichende Fachkenntnisse. Er war stets bemueht, die ihm uebertragenen Aufgaben zur vollen Zufriedenheit zu erledigen.
>
> **Verhaltensbeurteilung:** Gegenueber Kollegen und Vorgesetzten verhielt sich Herr Beispiel korrekt. Er zeichnete sich durch eine direkte Kommunikationsweise aus.
>
> **Schlussformel:** Wir danken Herrn Beispiel fuer seine Mitarbeit und wuenschen ihm fuer die Zukunft alles Gute.

## Erwartete Befunde

- "ausreichende Fachkenntnisse" - Note 4-5 (rot)
- "stets bemueht" - Note 4 (rot)
- "korrekt" allein (ohne stets/einwandfrei) - Note 4 (orange/rot)
- "direkte Kommunikationsweise" - Code fuer schwierig im Umgang
- Reihenfolge "Kollegen und Vorgesetzten" statt "Vorgesetzten und Kollegen" (rot)
- Schlussformel ohne Bedauern, ohne herzlichen Dank, ohne berufliche/persoenliche Zukunftswuensche
- Schweigen zu Kunden trotz Vertriebsjob (rot — Auslassung)
