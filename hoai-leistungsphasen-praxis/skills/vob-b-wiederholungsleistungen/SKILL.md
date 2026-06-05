---
name: vob-b-wiederholungsleistungen
description: "Hoai Vob B Schnittstelle, Hoai Wiederholungsleistungen Planungsaenderung, Hoai Zielfindungsphase Bgb 650p 650r: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Hoai Vob B Schnittstelle, Hoai Wiederholungsleistungen Planungsaenderung, Hoai Zielfindungsphase Bgb 650P 650R

## Arbeitsbereich

In diesem Skill wird **Hoai Vob B Schnittstelle, Hoai Wiederholungsleistungen Planungsaenderung, Hoai Zielfindungsphase Bgb 650P 650R** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `hoai-vob-b-schnittstelle` | HOAI-Praxis: prüft Bauverträge, Abnahme, Behinderung, Nachträge und Architektenrolle; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren. |
| `hoai-wiederholungsleistungen-planungsaenderung` | HOAI-Fachfrage: Planungsänderung, Wiederholung von Grundleistungen, § 10 HOAI, Bauherrnanordnung, Textform, geänderte Kostenbasis und Nachtragsvergütung des Planers prüfen. |
| `hoai-zielfindungsphase-bgb-650p-650r` | HOAI-Fachfrage: Zielfindungsphase nach § 650p Abs. 2 BGB, Planungsgrundlage, Kosteneinschätzung, Sonderkündigungsrecht § 650r BGB und Übergang in die eigentliche Planung führen. |

## Arbeitsweg

Für **Hoai Vob B Schnittstelle, Hoai Wiederholungsleistungen Planungsaenderung, Hoai Zielfindungsphase Bgb 650P 650R** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `hoai-leistungsphasen-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `hoai-vob-b-schnittstelle`

**Fokus:** HOAI-Praxis: prüft Bauverträge, Abnahme, Behinderung, Nachträge und Architektenrolle; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren.

# HOAI Querschnitt: Prüft bauverträge

## Einsatz

Dieser Querschnitts-Skill bearbeitet **prüft Bauverträge, Abnahme, Behinderung, Nachträge und Architektenrolle** über alle Leistungsphasen hinweg. Er hält die Projektlogik zusammen, bevor einzelne LPH-Fachmodule vertieft werden.

## Arbeitsweise

1. Klär Rolle, Projektart, Leistungsbild, beauftragte LPH, Vertrag, Honorarvereinbarung und aktuellen Konflikt.
2. Ordne die Unterlagen nach LPH, Planstand, Freigabe, Kostenstand, Terminstand und Beweiswert.
3. Trenne HOAI-Grundleistung, besondere Leistung, Bauvertragsrecht, Vergabe, öffentliches Recht und Haftung.
4. Erzeuge ein knappes, anschlussfähiges Arbeitsprodukt für Bauherr, Planer, Bauunternehmen, Anwalt oder Sachverständigen.

## Ergebnis

- LPH-/Vertragsmatrix
- Risikoregister
- konkreter Text- oder Tabellenbaustein
- nächste Prüfschritte

## Quellen- und Qualitätsregeln

- HOAI-Text, insbesondere § 34 und Anlage 10, live gegen Gesetze im Internet prüfen.
- BGB §§ 650p bis 650t bei Architekten-/Ingenieurverträgen berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und freiem Fundlink; keine Blindzitate.

## 2. `hoai-wiederholungsleistungen-planungsaenderung`

**Fokus:** HOAI-Fachfrage: Planungsänderung, Wiederholung von Grundleistungen, § 10 HOAI, Bauherrnanordnung, Textform, geänderte Kostenbasis und Nachtragsvergütung des Planers prüfen.

# Wiederholungsleistungen Und Planungsänderung

## Einsatz

Nutze diesen Skill, wenn der Bauherr nach Freigabe umplant, die Behörde Auflagen macht, Fördermittel geändert werden oder Fachplaner eine bereits abgeschlossene LPH wieder aufreißen.

## Normanker

- § 10 HOAI: vertragliche Änderung des Leistungsumfangs und Wiederholung von Grundleistungen.
- §§ 650b, 650q BGB: Änderungsmechanik im Architekten-/Ingenieurvertrag entsprechend prüfen.

## Prüfung

1. Ursprünglich beauftragte Leistung und Freigabe feststellen.
2. Änderungsauslöser bestimmen: Bauherr, Behörde, Planungsfehler, Fachplaner, Unternehmer, Fördermittel.
3. Prüfen, ob anrechenbare Kosten, Flächen oder Verrechnungseinheiten betroffen sind.
4. Textformvereinbarung suchen oder nachholen.
5. Wiederholung wegen Planerfehler von vergütbarer Zusatzleistung trennen.

## Output

Erzeuge einen Change-Request mit Ausgangsstand, Änderung, LPH-Betroffenheit, Honorarfolge, Terminfolge und Beweisunterlagen.

## 3. `hoai-zielfindungsphase-bgb-650p-650r`

**Fokus:** HOAI-Fachfrage: Zielfindungsphase nach § 650p Abs. 2 BGB, Planungsgrundlage, Kosteneinschätzung, Sonderkündigungsrecht § 650r BGB und Übergang in die eigentliche Planung führen.

# Zielfindungsphase Nach BGB 650p Und 650r

## Einsatz

Nutze diesen Skill, wenn Projektziele, Bedarf, Kosten und Planung noch nicht feststehen oder der Bauherr nach ersten Skizzen aussteigen will.

## Normanker

- § 650p Abs. 2 BGB: Planungsgrundlage und Kosteneinschätzung, wenn wesentliche Planungs- und Überwachungsziele noch nicht vereinbart sind.
- § 650r BGB: Sonderkündigungsrecht nach Vorlage der Unterlagen.

## Arbeitsgang

1. Klären, ob Ziele schon vereinbart waren oder erst erarbeitet werden sollten.
2. Unterlagen der Zielfindung sammeln: Bedarfsnotiz, Kosteneinschätzung, Varianten, Protokolle.
3. Prüfen, ob die Vorlage den Sonderkündigungsmechanismus auslöst.
4. Belehrung, Frist, Verbraucherrolle und Kündigungszugang prüfen.
5. Vergütung bis zur Kündigung von nicht abgerufener Weiterplanung trennen.

## Output

Ein Zielfindungsprotokoll mit Mindestunterlagen, Kündigungsfenster, Honorarfolge und Textbausteinen für Bauherr oder Planer.
