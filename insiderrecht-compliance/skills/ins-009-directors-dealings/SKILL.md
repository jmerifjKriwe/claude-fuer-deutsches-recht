---
name: ins-009-directors-dealings
description: "Prueft und dokumentiert Eigengeschaefte von Fuehrungskraeften (PDMRs) und nahestehenden Personen nach Art. 19 MAR: Schwellen, Meldefristen, Closed Periods und Ausnahmen."
---

# Directors' Dealings nach Art. 19 MAR

## Rechtlicher Rahmen

Art. 19 VO (EU) 596/2014 (MAR) verpflichtet Personen mit Führungsaufgaben (PDMRs) und ihnen
nahestehende Personen, Eigengeschäfte in Finanzinstrumenten des Emittenten zu melden. Die
Meldepflicht besteht ab einem kumulierten Jahresvolumen von 20.000 EUR (Opt-in bis 200.000 EUR
möglich). Frist: 3 Geschäftstage. Closed Periods: 30 Tage vor Bekanntgabe von Halbjahres- oder
Jahresabschlüssen. DVO (EU) 2016/523 legt das Meldeformat fest.

Rechtsgrundlagen:
- Art. 19 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- DVO (EU) 2016/523 (Meldeformat): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0523
- § 119 WpHG: https://www.gesetze-im-internet.de/wphg/__119.html
- BaFin-Emittentenleitfaden Kap. V: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill stellt sicher, dass alle meldepflichtigen Eigengeschäfte vollständig, fristgerecht
und im korrekten Format der BaFin gemeldet und veröffentlicht werden. Er deckt die Personen-
abgrenzung (PDMR / nahestehende Person), die Schwellenberechnung, Closed Periods und die
Ausnahmen ab.

## Arbeitsprogramm

### Schritt 1 – Personenkreis bestimmen

PDMRs (Persons Discharging Managerial Responsibilities):
- Vorstandsmitglieder, Aufsichtsratsmitglieder, leitende Angestellte mit regelmäßigem Zugang
  zu Insiderinformationen und Befugnis zu wesentlichen Managemententscheidungen

Nahestehende Personen (Art. 3 Abs. 1 Nr. 26 MAR):
- Ehe-/Lebenspartner, unterhaltsberechtigte Kinder, Verwandte seit ≥1 Jahr im gemeinsamen
  Haushalt
- Juristische Personen unter Kontrolle des PDMR oder nahestehender Person

### Schritt 2 – Meldepflichtige Transaktionen und Schwelle

Meldepflichtige Geschäfte:
- Kauf, Verkauf, Leerverkauf, Tausch, Schenkung, Erbschaft, Ausübung von Optionen und Bezugs-
  rechten in Aktien, Anleihen, Derivaten des Emittenten
Schwelle: 20.000 EUR kumuliert im Kalenderjahr → erste Meldung wenn erreicht, danach
  jede weitere Transaktion meldepflichtig (kein neues Jahresreset bis Jahresende)

### Schritt 3 – Frist und Format

- Meldung innerhalb von 3 Geschäftstagen nach Transaktion
- Meldung an BaFin UND Emittenten (Art. 19 Abs. 2 MAR)
- Emittent veröffentlicht innerhalb von 3 Geschäftstagen nach Eingang (§ 119 WpHG)
- Format: DVO (EU) 2016/523-konformes Formular mit Pflichtfeldern (Name, Position, Art des
  Instruments, Art der Transaktion, Datum, Preis, Volumen)

### Schritt 4 – Closed Periods (Art. 19 Abs. 11 MAR)

- 30 Tage vor Bekanntgabe des Halbjahres- oder Jahresabschlusses: kein Handel
- Emittent muss PDMR über Closed-Period-Termine schriftlich informieren
- Ausnahmen: außergewöhnliche Umstände (dringende finanzielle Notlage), auf Antrag beim Emittenten

### Schritt 5 – Interne Pre-Clearance

Empfehlen (nicht gesetzlich zwingend, aber Best Practice):
- PDMR beantragt Freigabe beim Compliance-Officer vor jeder Transaktion
- Compliance prüft: kein Insiderstatus, keine Closed Period, keine offene Insiderinformation
- Schriftliche Freigabe oder Verweigerung mit Begründung
- Aufbewahrung 5 Jahre

## Red-Team-Fragen

- Sind alle PDMRs und nahestehenden Personen identifiziert und informiert?
- Wurden alle meldepflichtigen Instrumente (nicht nur Aktien!) erfasst?
- Wird die 20.000-EUR-Schwelle korrekt auf Jahresbasis kumuliert?
- Werden Closed Periods rechtzeitig kommuniziert?
- Werden Pre-Clearance-Entscheidungen schriftlich dokumentiert?
- Erfolgt die Meldung an BaFin und Emittent binnen 3 Geschäftstagen?
- Veröffentlicht der Emittent die Meldungen rechtzeitig?
- Werden Derivate und indirekte Transaktionen (über nahestehende Personen) erfasst?

## Ausgabeformat

Erzeuge:
1. PDMR-Transaktionsmeldung (DVO 2016/523-konformes Formular)
2. Closed-Period-Kalender (aktuelles Geschäftsjahr)
3. Pre-Clearance-Antragsformular
4. Compliance-Matrix: PDMR × Transaktion × Meldestatus

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org,
openjur.de.
