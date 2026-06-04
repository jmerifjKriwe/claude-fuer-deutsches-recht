---
name: ins-006-handelsverbot-art14
description: "Prueft Insiderhandelsverbot nach Art. 14 MAR, abgrenzt Wissen von Absicht, analysiert Safe-Harbour-Ausnahmen und stellt Verteidigungsdokumentation sicher."
---

# Insiderhandelsverbot nach Art. 14 MAR

## Rechtlicher Rahmen

Art. 14 VO (EU) 596/2014 (MAR) verbietet drei Verhaltensweisen: (1) den Erwerb oder die
Veräußerung von Finanzinstrumenten auf der Basis von Insiderinformationen (Insider Trading),
(2) die Empfehlung oder Verleitung Dritter zu solchen Geschäften (Tipping), (3) die unzulässige
Offenlegung von Insiderinformationen. Das Verbot gilt für jeden, der über Insiderinformationen
verfügt, unabhängig davon, wie er die Information erlangt hat (Primär- und Sekundärinsider).
Strafbewehrt durch § 119 WpHG (bis zu 5 Jahre Freiheitsstrafe).

Rechtsgrundlagen:
- Art. 14 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- Art. 8, 9, 10 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- § 119 WpHG: https://www.gesetze-im-internet.de/wphg/__119.html
- BaFin-Emittentenleitfaden Kap. II: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill prüft, ob eine konkrete Transaktion oder Empfehlung gegen Art. 14 MAR verstößt,
und erstellt die Verteidigungsdokumentation für den Fall einer BaFin-Anfrage oder eines
Ermittlungsverfahrens. Er unterscheidet zwischen dem objektiven Tatbestand und den subjektiven
Elementen sowie den verfügbaren Safe-Harbour-Ausnahmen.

## Arbeitsprogramm

### Schritt 1 – Objektiver Tatbestand (Art. 8 MAR)

- Hat die handelnde Person zum Zeitpunkt der Transaktion über eine Insiderinformation verfügt?
- Handelt es sich um ein Finanzinstrument, auf das sich die Insiderinformation bezieht
  (oder ein verbundenes Derivat)?
- Wurde die Transaktion auf der Basis der Insiderinformation getätigt? (Kausalitätselement)
- Gilt auch für: Stornierung oder Änderung bestehender Aufträge auf der Basis von
  Insiderinformationen.

### Schritt 2 – Abgrenzung: Art. 9 MAR Safe Harbour

Prüfe, ob eine der Ausnahmen greift:
a) Legitime Ausübung regulärer Aufgaben: Transaktion war Teil der normalen Geschäftstätigkeit
   (z. B. Market Maker, Liquiditätssicherung)
b) Beschlossene Transaktion vor Erlangen der Insiderinformation (Art. 9 Abs. 3 MAR)
c) Rückkaufprogramm oder Kursstabilisierung nach DVO (EU) 2016/1052
d) Monetäre Politik, Staatsschulden, Klimapolitik (Art. 9 Abs. 2 MAR)
→ Für jeden Safe-Harbour-Tatbestand: Nachweis des relevanten Sachverhalts mit Zeitstempel.

### Schritt 3 – Tipping (Art. 10 MAR)

- Wurde die Insiderinformation an eine andere Person weitergegeben?
- Erfolgte die Weitergabe im Rahmen normaler Berufsausübung (z. B. Anwalt an Mandant,
  IR-Abteilung an Analyst im Rahmen von Market Sounding)?
- Wenn nein: Verstoß gegen Art. 10 MAR, ggf. auch Art. 14 lit. c MAR.

### Schritt 4 – Strafrecht (§ 119 WpHG)

- Tatbestand § 119 WpHG prüfen (vorsätzlich): Erwerb, Veräußerung, Empfehlung, Offenlegung
- Leichtfertigkeitsttatbestand § 119 Abs. 3 WpHG beachten
- Behördenkoordination: BaFin-Marktüberwachung meldet an Staatsanwaltschaft bei Verdacht

### Schritt 5 – Verteidigungsdokumentation

Erstelle für jede verdachtsauslösende Transaktion:
- Zeitstrahl: Wann hatte Person Kenntnis von der Insiderinformation? Wann wurde Transaktion
  beschlossen und ausgeführt?
- Handelsplan oder -strategie vor der Insiderinformation (z. B. Spar-/Investitionsplan)
- Nachweis, dass Entscheidung vor Kenntnis getroffen wurde
- Belege für Safe-Harbour-Tatbestand (falls zutreffend)

## Red-Team-Fragen

- Hatte die handelnde Person tatsächlich Zugang zur Insiderinformation?
- Kann der Kausalzusammenhang zwischen Insiderinformation und Transaktion widerlegt werden?
- Liegt ein Safe-Harbour-Tatbestand vor, und ist dieser lückenlos dokumentiert?
- Wurde die Transaktion auf der Basis eines vorgefassten Handelsplans ausgeführt?
- Wurde Tipping (Weitergabe an Dritte) ausgeschlossen oder sachgemäß dokumentiert?
- Gibt es Trading-Anomalien vor der Ad-hoc-Veröffentlichung, die BaFin-Aufmerksamkeit erregen?

## Ausgabeformat

Erzeuge:
1. Transaktions-Prüfprotokoll (Zeitstrahl, Wissensstand, Kausalitätsanalyse)
2. Safe-Harbour-Prüfmatrix
3. Verteidigungsmemo (für BaFin-Anfrage oder Ermittlungsverfahren)
4. Empfehlungen für Handelsüberwachung und Pre-Clearance-Verfahren

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, curia.europa.eu,
bgh.de, dejure.org, openjur.de.
