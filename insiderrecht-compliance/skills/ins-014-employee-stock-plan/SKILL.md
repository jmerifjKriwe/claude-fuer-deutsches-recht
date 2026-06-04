---
name: ins-014-employee-stock-plan
description: "Prueft Mitarbeiteraktienprogramme (ESOP, LTIP, RSU) auf insiderrechtliche Risiken: Closed Periods, Handelsverbote, automatische Plaene und Befreiungsmoeglichkeiten."
---

# Mitarbeiteraktienprogramme (ESOP / LTIP / RSU) – Insiderrechtliche Risiken

## Rechtlicher Rahmen

Aktienbasierte Vergütungsinstrumente (ESOP, LTIP, RSU, Aktienoptionen) unterliegen MAR-Pflichten,
wenn sie zum Kauf oder Verkauf von Finanzinstrumenten des Emittenten berechtigen oder verpflichten.
Entscheidend ist, ob die Ausübung oder Zuteilung in eine Closed Period oder eine Phase mit
Insiderinformation fällt. Safe-Harbour-Regelungen existieren für vorgefasste Pläne (Art. 9 MAR).

Rechtsgrundlagen:
- Art. 9, 14, 19 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- DVO (EU) 2016/1052 (Rückkaufprogramme, analog): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R1052
- § 119 WpHG: https://www.gesetze-im-internet.de/wphg/__119.html
- BaFin-Emittentenleitfaden Kap. V: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill prüft, ob die Ausübung von Mitarbeiteraktienoptionen, RSU-Vestings oder anderen
Programmtransaktionen in einer Closed Period oder Insiderphase liegt, und bestimmt, ob ein
Safe Harbour oder eine Befreiung greift.

## Arbeitsprogramm

### Schritt 1 – Programmstruktur analysieren

- Welche Art von Instrument: Option (Ausübungsrecht), RSU (automatische Zuteilung),
  LTIP (leistungsabhängige Zuteilung)?
- Gibt es Ermessensspielraum bei der Ausübung (→ dann: MAR-Prüfung notwendig)?
- Ist die Zuteilung oder Ausübung automatisch und nach Plan ohne individuelle Entscheidung
  des Mitarbeiters?

### Schritt 2 – Closed-Period-Prüfung (Art. 19 Abs. 11 MAR)

- Liegt der Ausübungs-/Zuteilungstermin in einer Closed Period (30 Tage vor Jahres-/
  Halbjahresabschluss-Veröffentlichung)?
- Für PDMRs: Handelsverbot gilt auch für Ausübung von Optionen in Closed Period
- Für reguläre Mitarbeiter: Kein gesetzliches Closed-Period-Verbot, aber Insiderhandelsverbot
  nach Art. 14 MAR bei Vorliegen von Insiderinformation

### Schritt 3 – Insiderhandels-Prüfung (Art. 8, 14 MAR)

- Hat der Mitarbeiter zum Zeitpunkt der Ausübung Zugang zu einer Insiderinformation?
- Gilt für alle Mitarbeiter, nicht nur PDMRs
- Bei automatischen Plans ohne Mitarbeiter-Ermessen: Kausalitätselement des Art. 8 MAR
  fehlt i.d.R. → kein Verstoß

### Schritt 4 – Safe Harbour für vorgefasste Pläne (Art. 9 Abs. 3 MAR)

Safe Harbour greift, wenn:
a) Mitarbeiter hatte vor Erlangen der Insiderinformation einen schriftlichen Plan zur
   Ausübung abgeschlossen (z. B. automatischer Ausübungsplan nach Vesting-Datum)
b) Plan sieht keine Änderungsmöglichkeit für den Mitarbeiter vor
c) Keine diskretionären Handlungen nach Beginn der Insiderphasee
→ Plan-Dokumentation vor Beginn der Insiderphase muss vorliegen.

### Schritt 5 – Empfehlungen für Programmgestaltung

- Einrichtung automatischer Ausübungspläne (pre-arranged plans) für RSUs und Optionen
- Ausübungsfenster nur in eröffneten Trading Windows
- Pre-Clearance-Pflicht für diskretionäre Ausübungen
- Regelmäßige Schulung der Programmteilnehmer

## Red-Team-Fragen

- Fallen Vesting-Termine regelmäßig in Closed Periods?
- Wurden Mitarbeiter mit Insiderkenntnissen auf das Ausübungsverbot hingewiesen?
- Gibt es vorgefasste Pläne, die den Safe Harbour nach Art. 9 Abs. 3 MAR begründen?
- Ist die Unterscheidung zwischen PDMRs (Closed-Period-Verbot) und sonstigen Mitarbeitern
  (nur Insiderhandelsverbot) sauber implementiert?
- Wird das Programm regelmäßig auf insiderrechtliche Risiken überprüft?

## Ausgabeformat

Erzeuge:
1. Programm-Risikomatrix: Instrument × Closed Period × Insiderstatus × Safe Harbour
2. Safe-Harbour-Plan-Vorlage (vorgefasster Ausübungsplan)
3. Mitarbeiter-Belehrungsschreiben (Insiderrecht und Aktienplan)
4. Compliance-Empfehlungen für Programmüberarbeitung

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.
