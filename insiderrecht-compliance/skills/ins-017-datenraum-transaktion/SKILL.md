---
name: ins-017-datenraum-transaktion
description: "Sichert Datenraum-Prozesse in Transaktionen (M&A, Anleihe, Kapitalerhoehung) gegen Insiderrecht-Risiken: Zugangskontrolle, Protokollierung und Exit-Management."
---

# Datenraum-Management in Transaktionen – Insiderrechtliche Anforderungen

## Rechtlicher Rahmen

Der Zugang zu einem virtuellen Datenraum in M&A- oder Kapitalmarkttransaktionen begründet
regelmäßig eine Insiderinformation für die Zugangsberechtigten. Art. 10 und 18 MAR setzen
strenge Anforderungen an Informationskreis-Kontrolle, Protokollierung und Belehrung. Der
Emittent bleibt verantwortlich für MAR-Compliance aller Datenraum-Nutzer.

Rechtsgrundlagen:
- Art. 10, 18 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- Art. 17 Abs. 4 MAR (Aufschub): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- § 119 WpHG: https://www.gesetze-im-internet.de/wphg/__119.html
- BaFin-Emittentenleitfaden Kap. III: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill erstellt die Governance für Datenräume in kapitalmarktrelevanten Transaktionen
und stellt sicher, dass alle Zugangsberechtigten korrekt als Insider behandelt werden.

## Arbeitsprogramm

### Schritt 1 – Datenraum-Governance-Struktur

- Benenne einen Datenraum-Administrator (i.d.R. M&A-Kanzlei oder Investmentbank)
- Definiere Zugriffsebenen (Stufe 1: Non-Insider-Informationen, Stufe 2: Insiderinformationen)
- Führe separate Insiderlisten für jede Zugriffsebene
- Beauftrage Datenraum-Anbieter mit aktiviertem Zugangsprotokoll (Wer hat wann welche
  Dokumente geöffnet/heruntergeladen?)

### Schritt 2 – Aufnahme in Insiderliste bei Zugriffserteilung

- Jeder Nutzer der Insiderinformations-Ebene wird unverzüglich in die Insiderliste aufgenommen
- Belehrung vor Zugriffserteilung (schriftlich, mit Zeitstempel)
- Bestätigung des Nutzers, Belehrung empfangen zu haben

### Schritt 3 – Need-to-Know-Prinzip

- Zugriffserteilung nur für Personen, deren Rolle die Information erfordert
- Regelmäßige Überprüfung der Zugriffsberechtigungen (mind. bei jedem Meilenstein)
- Sofortige Zugangssperrung bei Ausscheiden aus dem Prozess

### Schritt 4 – Exit-Management

Nach Abschluss des Prozesses (Signing, Closing, Abbruch):
- Schließung des Datenraums für alle Nutzer
- Archivierung der Zugangsprotokolle (5 Jahre)
- Bestätigung der Datenvernichtung von allen externen Parteien einholen
- Insiderlisten-Eintrag: Austrittsdatum für alle Nutzer eintragen

### Schritt 5 – Aufschub-Integration

- Datenraum-Zugang und Aufschub nach Art. 17 Abs. 4 MAR sind parallel zu führen
- Bei Leak: Sofortmaßnahmen (Skill ins-011) aktivieren
- Bei Abbruch der Transaktion: Insiderinformation erlischt nur, wenn kein legitimes Interesse
  mehr an Aufschub besteht; Compliance prüft neuen Status der Information

## Red-Team-Fragen

- Sind alle Datenraum-Nutzer in der Insiderliste erfasst?
- Wurden alle Nutzer vor Zugriffserteilung belehrt?
- Wird das Need-to-Know-Prinzip bei jeder Zugriffserteilung geprüft?
- Sind Zugangsprotokolle vollständig und unveränderbar gespeichert?
- Wurden externe Parteien zur Datenvernichtung verpflichtet?
- Ist der Zusammenhang zwischen Datenraum-Zugang und Aufschubakte dokumentiert?

## Ausgabeformat

Erzeuge:
1. Datenraum-Governance-Policy
2. Zugriffsebenen-Matrix (Dokument × Stufe × Nutzerkreis)
3. Belehrungsvorlage für Datenraum-Nutzer
4. Exit-Checkliste (Datenraum-Schließung)

Belege ausschließlich mit: eur-lex.europa.eu, bafin.de, gesetze-im-internet.de, dejure.org.
