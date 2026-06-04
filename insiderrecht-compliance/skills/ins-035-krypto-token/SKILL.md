---
name: ins-035-krypto-token
description: "Prueft Anwendbarkeit von MAR auf Krypto-Token und Asset-Referenced Token: MiCA-Abgrenzung, Insiderrecht fuer Krypto-Assets und Marktmanipulationsverbote."
---

# Krypto-Token und MAR / MiCA – Insiderrecht

## Rechtlicher Rahmen

MAR gilt für Finanzinstrumente nach MiFID II. Krypto-Assets, die keine Finanzinstrumente sind,
fallen grundsätzlich nicht unter MAR. Seit 30.12.2024 gilt jedoch die Verordnung MiCA
(EU) 2023/1114, die eigene Marktmissbrauchsregeln für Krypto-Assets enthält (Art. 87 ff. MiCA),
die MAR für Krypto-Assets nachbilden. Für Token, die als Finanzinstrumente qualifizieren
(Security Tokens), gilt MAR unmittelbar.

Rechtsgrundlagen:
- Art. 87–92 MiCA (Marktmissbrauch): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R1114
- Art. 2 MAR (Anwendungsbereich): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- MiFID II Art. 4 (Finanzinstrument): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014L0065
- BaFin Krypto-Assets: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill klärt, ob ein Krypto-Token unter MAR oder MiCA-Marktmissbrauchsvorschriften
fällt, und entwickelt die entsprechende Compliance-Strategie.

## Arbeitsprogramm

### Schritt 1 – Klassifizierung des Tokens

- Ist der Token ein Finanzinstrument nach MiFID II (Security Token)?
  → Wenn ja: MAR gilt unmittelbar (wie für Aktien oder Anleihen)
- Ist der Token ein Utility Token, Asset-Referenced Token oder E-Money Token?
  → Wenn ja: MiCA gilt (nicht MAR), spezifisch Art. 87–92 MiCA
- Ist der Token ein reiner Nutzungstoken ohne Anlagecharakter?
  → Ggf. weder MAR noch MiCA; rechtliche Qualifikation im Einzelfall erforderlich

### Schritt 2 – MAR-Pflichten für Security Tokens

Wenn MAR anwendbar:
- Art. 7 MAR: Insiderinformations-Definition
- Art. 17 MAR: Ad-hoc-Pflicht (soweit Token an geregeltem Markt gehandelt)
- Art. 14 MAR: Insiderhandelsverbot
- Art. 15 MAR: Marktmanipulationsverbot
- Insiderliste, Directors' Dealings analog

### Schritt 3 – MiCA-Pflichten für Krypto-Assets

Art. 87 MiCA (Insiderhandel):
- Verbot des Handels auf Basis von Insider-Informationen über Krypto-Assets
- Verbot der Weitergabe (Art. 88 MiCA)
- Verbot der Marktmanipulation (Art. 89 MiCA)
Art. 90 MiCA: Verpflichtung zur Veröffentlichung von Insiderinformationen für
  Krypto-Asset-Dienstleister und Emittenten von ARTs/EMTs

### Schritt 4 – Marktmanipulation im Krypto-Bereich

- „Wash Trading" und koordinierte Handelspraktiken zur Preisbeeinflussung
- Social-Media-Manipulation (Pump-and-Dump-Schemata)
- MAR Art. 12 und MiCA Art. 89 (beide verbieten diese Praktiken)

### Schritt 5 – Compliance-Empfehlungen für Token-Emittenten

- Klassifizierung des Tokens rechtlich absichern (externe Kanzlei)
- MiCA-Whitepaper und Pflichten des Token-Emittenten umsetzen
- Compliance-Policy für Trading in eigenen Token durch Mitarbeiter und Insider
- BaFin-Guidance zu Krypto-Assets regelmäßig verfolgen

## Red-Team-Fragen

- Ist die Klassifizierung des Tokens als Finanzinstrument vs. Krypto-Asset rechtssicher?
- Wurden Art. 87–92 MiCA als eigenständige Compliance-Anforderungen implementiert?
- Gibt es Marktmanipulations-Monitoring für den Token?
- Sind die Insiderregeln für Mitarbeiter des Token-Emittenten kommuniziert?

## Ausgabeformat

Erzeuge:
1. Token-Klassifizierungsmatrix (Merkmal × MAR/MiCA/keine Regel)
2. MAR vs. MiCA-Pflichten-Vergleich
3. Compliance-Policy-Entwurf für Token-Insider
4. Marktmanipulations-Monitoring-Framework

Belege ausschließlich mit: eur-lex.europa.eu, bafin.de, gesetze-im-internet.de, dejure.org.
