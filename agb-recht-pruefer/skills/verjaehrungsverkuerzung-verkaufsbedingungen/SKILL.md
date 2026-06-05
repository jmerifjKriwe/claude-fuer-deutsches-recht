---
name: verjaehrungsverkuerzung-verkaufsbedingungen
description: "Verjaehrungsverkuerzung, Verkaufsbedingungen B2b, Versicherung Avb, Versionsdiff Agb: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Verjaehrungsverkuerzung, Verkaufsbedingungen B2B, Versicherung Avb, Versionsdiff Agb, Vollmacht Vertretung

## Arbeitsbereich

In diesem Skill wird **Verjaehrungsverkuerzung, Verkaufsbedingungen B2B, Versicherung Avb, Versionsdiff Agb, Vollmacht Vertretung** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verjaehrungsverkuerzung` | Klausel-Fachmodul für Verjaehrungsverkürzung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `verkaufsbedingungen-b2b` | Branchen-Fachmodul für Verkaufsbedingungen B2B: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `versicherung-avb` | Branchen-Fachmodul für Versicherung Avb: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `versionsdiff-agb` | Output- und Streit-Skill für Versionsdiff AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `vollmacht-vertretung` | Klausel-Fachmodul für Vollmacht Vertretung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |

## Arbeitsweg

Für **Verjaehrungsverkuerzung, Verkaufsbedingungen B2B, Versicherung Avb, Versionsdiff Agb, Vollmacht Vertretung** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `agb-recht-pruefer` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verjaehrungsverkuerzung`

**Fokus:** Klausel-Fachmodul für Verjaehrungsverkürzung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung.

# Verjaehrungsverkürzung

## Fachkern: Verjaehrungsverkürzung

- **Klauselproblem (Verjaehrungsverkürzung):** prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung.
- **AGB-Weiche:** Einbeziehung (§ 305 BGB), überraschende Klausel (§ 305c BGB), Transparenz (§ 307 Abs. 1 S. 2 BGB), Inhaltskontrolle (§§ 307-309 BGB), Rechtsfolge (§ 306 BGB) und Prozess-/Verbandsrisiko sauber trennen.
- **Beleglogik:** Originalklausel, Vertragsumfeld, Verwendungsnachweis, Verhandlungsspuren, Kundengruppe, Marktstandard und wirtschaftliche Wirkung als Matrix erfassen.
- **Arbeitsprodukt:** Klauselampel, Redline, Ersatzformulierung, Verhandlungsposition und gerichtsfeste Kurzbegründung mit Live-Check amtlicher Normenquellen.

## Minimal-Intake

- Rolle: Verwender, Kunde, Verbraucher, Unternehmer, Plattform, Händler, Verband oder Prozessgegner.
- Klausel: Wortlaut, Fundstelle, Überschrift, Kontext, Version und Einbeziehungsweg.
- Vertrag: Vertragstyp, Hauptleistung, Preis-/Risikomodell, Laufzeit und Vertriebskanal.
- Ziel: Wirksamkeit prüfen, Risiko senken, härter entwerfen, redlinen, verhandeln oder verteidigen.
- Nachweis: Screenshots, Checkout, E-Mail, Angebot, Auftragsbestätigung, Archivversion oder Kundendaten.

## Prüfpfad

1. **Normenstand sichern:** Vor tragenden Aussagen BGB §§ 305 bis 310 auf Gesetze im Internet prüfen; bei Verbandsrisiko UKlaG ergänzen.
2. **Anwendungsbereich:** AGB-Eigenschaft, Einbeziehung, Individualabrede, Verbraucher-/Unternehmerstatus und Sondermaterie klären.
3. **Auslegung:** kundenfeindlichste vertretbare Auslegung, Überraschung, Mehrdeutigkeit und Transparenz prüfen.
4. **Inhaltskontrolle:** § 307 BGB als Grundprüfung, danach einschlägige Klauselverbote aus §§ 308, 309 BGB und § 310 BGB einordnen.
5. **Spezialfokus:** Bei Verjaehrungsverkürzung besonders auf wirtschaftlichen Zweck, versteckte Belastung, Verständlichkeit, Nachweisbarkeit und praxistaugliche Durchführung achten.
6. **Rechtsfolge:** Unwirksamkeit, gesetzliche Ersatzregel, Rückzahlung, Vertragsfortbestand, Prozess- und UKlaG-Risiko prüfen.
7. **Verbesserung:** mindestens eine sichere Ersatzfassung und bei Bedarf eine verhandelbare Fallback-Fassung formulieren.

## Output

| Punkt | Befund |
| --- | --- |
| Klauselzweck | ... |
| AGB-Kontrolle | ja/nein/unklar, warum |
| Hauptangriff | ... |
| Verteidigung | ... |
| Risiko | Grün/Gelb/Rot |
| Bessere Fassung | ... |
| offene Tatsachen | ... |

## Qualitätsregeln

- Keine Scheinzitate. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine geltungserhaltende Reduktion als Standardlösung anbieten.
- Bei B2B nicht so tun, als sei alles frei verhandelbar; Transparenz und Leitbild bleiben wichtig.
- Bei B2C streng, verständlich und dokumentationsfähig formulieren.
- Wenn eine Klausel wirtschaftlich gewollt, aber rechtlich riskant ist: Risiko offen labeln und Fallback anbieten.

## Quellenanker

Siehe `references/QUELLEN.md`, `references/PRUEFLOGIK.md` und `references/KLAUSELFAMILIEN.md`.

## 2. `verkaufsbedingungen-b2b`

**Fokus:** Branchen-Fachmodul für Verkaufsbedingungen B2B: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen.

# Verkaufsbedingungen B2B

## Fachkern: Verkaufsbedingungen B2B

- **Klauselproblem (Verkaufsbedingungen B2B):** prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen.
- **AGB-Weiche:** Einbeziehung (§ 305 BGB), überraschende Klausel (§ 305c BGB), Transparenz (§ 307 Abs. 1 S. 2 BGB), Inhaltskontrolle (§§ 307-309 BGB), Rechtsfolge (§ 306 BGB) und Prozess-/Verbandsrisiko sauber trennen.
- **Beleglogik:** Originalklausel, Vertragsumfeld, Verwendungsnachweis, Verhandlungsspuren, Kundengruppe, Marktstandard und wirtschaftliche Wirkung als Matrix erfassen.
- **Arbeitsprodukt:** Klauselampel, Redline, Ersatzformulierung, Verhandlungsposition und gerichtsfeste Kurzbegründung mit Live-Check amtlicher Normenquellen.

## Minimal-Intake

- Rolle: Verwender, Kunde, Verbraucher, Unternehmer, Plattform, Händler, Verband oder Prozessgegner.
- Klausel: Wortlaut, Fundstelle, Überschrift, Kontext, Version und Einbeziehungsweg.
- Vertrag: Vertragstyp, Hauptleistung, Preis-/Risikomodell, Laufzeit und Vertriebskanal.
- Ziel: Wirksamkeit prüfen, Risiko senken, härter entwerfen, redlinen, verhandeln oder verteidigen.
- Nachweis: Screenshots, Checkout, E-Mail, Angebot, Auftragsbestätigung, Archivversion oder Kundendaten.

## Prüfpfad

1. **Normenstand sichern:** Vor tragenden Aussagen BGB §§ 305 bis 310 auf Gesetze im Internet prüfen; bei Verbandsrisiko UKlaG ergänzen.
2. **Anwendungsbereich:** AGB-Eigenschaft, Einbeziehung, Individualabrede, Verbraucher-/Unternehmerstatus und Sondermaterie klären.
3. **Auslegung:** kundenfeindlichste vertretbare Auslegung, Überraschung, Mehrdeutigkeit und Transparenz prüfen.
4. **Inhaltskontrolle:** § 307 BGB als Grundprüfung, danach einschlägige Klauselverbote aus §§ 308, 309 BGB und § 310 BGB einordnen.
5. **Spezialfokus:** Bei Verkaufsbedingungen B2B besonders auf wirtschaftlichen Zweck, versteckte Belastung, Verständlichkeit, Nachweisbarkeit und praxistaugliche Durchführung achten.
6. **Rechtsfolge:** Unwirksamkeit, gesetzliche Ersatzregel, Rückzahlung, Vertragsfortbestand, Prozess- und UKlaG-Risiko prüfen.
7. **Verbesserung:** mindestens eine sichere Ersatzfassung und bei Bedarf eine verhandelbare Fallback-Fassung formulieren.

## Output

| Punkt | Befund |
| --- | --- |
| Klauselzweck | ... |
| AGB-Kontrolle | ja/nein/unklar, warum |
| Hauptangriff | ... |
| Verteidigung | ... |
| Risiko | Grün/Gelb/Rot |
| Bessere Fassung | ... |
| offene Tatsachen | ... |

## Qualitätsregeln

- Keine Scheinzitate. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine geltungserhaltende Reduktion als Standardlösung anbieten.
- Bei B2B nicht so tun, als sei alles frei verhandelbar; Transparenz und Leitbild bleiben wichtig.
- Bei B2C streng, verständlich und dokumentationsfähig formulieren.
- Wenn eine Klausel wirtschaftlich gewollt, aber rechtlich riskant ist: Risiko offen labeln und Fallback anbieten.

## Quellenanker

Siehe `references/QUELLEN.md`, `references/PRUEFLOGIK.md` und `references/KLAUSELFAMILIEN.md`.

## 3. `versicherung-avb`

**Fokus:** Branchen-Fachmodul für Versicherung Avb: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen.

# Versicherung Avb

## Fachkern: Versicherung Avb

- **Klauselproblem (Versicherung Avb):** prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen.
- **AGB-Weiche:** Einbeziehung (§ 305 BGB), überraschende Klausel (§ 305c BGB), Transparenz (§ 307 Abs. 1 S. 2 BGB), Inhaltskontrolle (§§ 307-309 BGB), Rechtsfolge (§ 306 BGB) und Prozess-/Verbandsrisiko sauber trennen.
- **Beleglogik:** Originalklausel, Vertragsumfeld, Verwendungsnachweis, Verhandlungsspuren, Kundengruppe, Marktstandard und wirtschaftliche Wirkung als Matrix erfassen.
- **Arbeitsprodukt:** Klauselampel, Redline, Ersatzformulierung, Verhandlungsposition und gerichtsfeste Kurzbegründung mit Live-Check amtlicher Normenquellen.

## Minimal-Intake

- Rolle: Verwender, Kunde, Verbraucher, Unternehmer, Plattform, Händler, Verband oder Prozessgegner.
- Klausel: Wortlaut, Fundstelle, Überschrift, Kontext, Version und Einbeziehungsweg.
- Vertrag: Vertragstyp, Hauptleistung, Preis-/Risikomodell, Laufzeit und Vertriebskanal.
- Ziel: Wirksamkeit prüfen, Risiko senken, härter entwerfen, redlinen, verhandeln oder verteidigen.
- Nachweis: Screenshots, Checkout, E-Mail, Angebot, Auftragsbestätigung, Archivversion oder Kundendaten.

## Prüfpfad

1. **Normenstand sichern:** Vor tragenden Aussagen BGB §§ 305 bis 310 auf Gesetze im Internet prüfen; bei Verbandsrisiko UKlaG ergänzen.
2. **Anwendungsbereich:** AGB-Eigenschaft, Einbeziehung, Individualabrede, Verbraucher-/Unternehmerstatus und Sondermaterie klären.
3. **Auslegung:** kundenfeindlichste vertretbare Auslegung, Überraschung, Mehrdeutigkeit und Transparenz prüfen.
4. **Inhaltskontrolle:** § 307 BGB als Grundprüfung, danach einschlägige Klauselverbote aus §§ 308, 309 BGB und § 310 BGB einordnen.
5. **Spezialfokus:** Bei Versicherung Avb besonders auf wirtschaftlichen Zweck, versteckte Belastung, Verständlichkeit, Nachweisbarkeit und praxistaugliche Durchführung achten.
6. **Rechtsfolge:** Unwirksamkeit, gesetzliche Ersatzregel, Rückzahlung, Vertragsfortbestand, Prozess- und UKlaG-Risiko prüfen.
7. **Verbesserung:** mindestens eine sichere Ersatzfassung und bei Bedarf eine verhandelbare Fallback-Fassung formulieren.

## Output

| Punkt | Befund |
| --- | --- |
| Klauselzweck | ... |
| AGB-Kontrolle | ja/nein/unklar, warum |
| Hauptangriff | ... |
| Verteidigung | ... |
| Risiko | Grün/Gelb/Rot |
| Bessere Fassung | ... |
| offene Tatsachen | ... |

## Qualitätsregeln

- Keine Scheinzitate. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine geltungserhaltende Reduktion als Standardlösung anbieten.
- Bei B2B nicht so tun, als sei alles frei verhandelbar; Transparenz und Leitbild bleiben wichtig.
- Bei B2C streng, verständlich und dokumentationsfähig formulieren.
- Wenn eine Klausel wirtschaftlich gewollt, aber rechtlich riskant ist: Risiko offen labeln und Fallback anbieten.

## Quellenanker

Siehe `references/QUELLEN.md`, `references/PRUEFLOGIK.md` und `references/KLAUSELFAMILIEN.md`.

## 4. `versionsdiff-agb`

**Fokus:** Output- und Streit-Skill für Versionsdiff AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen.

# Versionsdiff AGB

## Fachkern: Versionsdiff AGB

- **Klauselproblem (Versionsdiff AGB):** macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen.
- **AGB-Weiche:** Einbeziehung (§ 305 BGB), überraschende Klausel (§ 305c BGB), Transparenz (§ 307 Abs. 1 S. 2 BGB), Inhaltskontrolle (§§ 307-309 BGB), Rechtsfolge (§ 306 BGB) und Prozess-/Verbandsrisiko sauber trennen.
- **Beleglogik:** Originalklausel, Vertragsumfeld, Verwendungsnachweis, Verhandlungsspuren, Kundengruppe, Marktstandard und wirtschaftliche Wirkung als Matrix erfassen.
- **Arbeitsprodukt:** Klauselampel, Redline, Ersatzformulierung, Verhandlungsposition und gerichtsfeste Kurzbegründung mit Live-Check amtlicher Normenquellen.

## Minimal-Intake

- Rolle: Verwender, Kunde, Verbraucher, Unternehmer, Plattform, Händler, Verband oder Prozessgegner.
- Klausel: Wortlaut, Fundstelle, Überschrift, Kontext, Version und Einbeziehungsweg.
- Vertrag: Vertragstyp, Hauptleistung, Preis-/Risikomodell, Laufzeit und Vertriebskanal.
- Ziel: Wirksamkeit prüfen, Risiko senken, härter entwerfen, redlinen, verhandeln oder verteidigen.
- Nachweis: Screenshots, Checkout, E-Mail, Angebot, Auftragsbestätigung, Archivversion oder Kundendaten.

## Prüfpfad

1. **Normenstand sichern:** Vor tragenden Aussagen BGB §§ 305 bis 310 auf Gesetze im Internet prüfen; bei Verbandsrisiko UKlaG ergänzen.
2. **Anwendungsbereich:** AGB-Eigenschaft, Einbeziehung, Individualabrede, Verbraucher-/Unternehmerstatus und Sondermaterie klären.
3. **Auslegung:** kundenfeindlichste vertretbare Auslegung, Überraschung, Mehrdeutigkeit und Transparenz prüfen.
4. **Inhaltskontrolle:** § 307 BGB als Grundprüfung, danach einschlägige Klauselverbote aus §§ 308, 309 BGB und § 310 BGB einordnen.
5. **Spezialfokus:** Bei Versionsdiff AGB besonders auf wirtschaftlichen Zweck, versteckte Belastung, Verständlichkeit, Nachweisbarkeit und praxistaugliche Durchführung achten.
6. **Rechtsfolge:** Unwirksamkeit, gesetzliche Ersatzregel, Rückzahlung, Vertragsfortbestand, Prozess- und UKlaG-Risiko prüfen.
7. **Verbesserung:** mindestens eine sichere Ersatzfassung und bei Bedarf eine verhandelbare Fallback-Fassung formulieren.

## Output

| Punkt | Befund |
| --- | --- |
| Klauselzweck | ... |
| AGB-Kontrolle | ja/nein/unklar, warum |
| Hauptangriff | ... |
| Verteidigung | ... |
| Risiko | Grün/Gelb/Rot |
| Bessere Fassung | ... |
| offene Tatsachen | ... |

## Qualitätsregeln

- Keine Scheinzitate. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine geltungserhaltende Reduktion als Standardlösung anbieten.
- Bei B2B nicht so tun, als sei alles frei verhandelbar; Transparenz und Leitbild bleiben wichtig.
- Bei B2C streng, verständlich und dokumentationsfähig formulieren.
- Wenn eine Klausel wirtschaftlich gewollt, aber rechtlich riskant ist: Risiko offen labeln und Fallback anbieten.

## Quellenanker

Siehe `references/QUELLEN.md`, `references/PRUEFLOGIK.md` und `references/KLAUSELFAMILIEN.md`.

## 5. `vollmacht-vertretung`

**Fokus:** Klausel-Fachmodul für Vollmacht Vertretung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung.

# Vollmacht Vertretung

## Fachkern: Vollmacht Vertretung

- **Klauselproblem (Vollmacht Vertretung):** prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung.
- **AGB-Weiche:** Einbeziehung (§ 305 BGB), überraschende Klausel (§ 305c BGB), Transparenz (§ 307 Abs. 1 S. 2 BGB), Inhaltskontrolle (§§ 307-309 BGB), Rechtsfolge (§ 306 BGB) und Prozess-/Verbandsrisiko sauber trennen.
- **Beleglogik:** Originalklausel, Vertragsumfeld, Verwendungsnachweis, Verhandlungsspuren, Kundengruppe, Marktstandard und wirtschaftliche Wirkung als Matrix erfassen.
- **Arbeitsprodukt:** Klauselampel, Redline, Ersatzformulierung, Verhandlungsposition und gerichtsfeste Kurzbegründung mit Live-Check amtlicher Normenquellen.

## Minimal-Intake

- Rolle: Verwender, Kunde, Verbraucher, Unternehmer, Plattform, Händler, Verband oder Prozessgegner.
- Klausel: Wortlaut, Fundstelle, Überschrift, Kontext, Version und Einbeziehungsweg.
- Vertrag: Vertragstyp, Hauptleistung, Preis-/Risikomodell, Laufzeit und Vertriebskanal.
- Ziel: Wirksamkeit prüfen, Risiko senken, härter entwerfen, redlinen, verhandeln oder verteidigen.
- Nachweis: Screenshots, Checkout, E-Mail, Angebot, Auftragsbestätigung, Archivversion oder Kundendaten.

## Prüfpfad

1. **Normenstand sichern:** Vor tragenden Aussagen BGB §§ 305 bis 310 auf Gesetze im Internet prüfen; bei Verbandsrisiko UKlaG ergänzen.
2. **Anwendungsbereich:** AGB-Eigenschaft, Einbeziehung, Individualabrede, Verbraucher-/Unternehmerstatus und Sondermaterie klären.
3. **Auslegung:** kundenfeindlichste vertretbare Auslegung, Überraschung, Mehrdeutigkeit und Transparenz prüfen.
4. **Inhaltskontrolle:** § 307 BGB als Grundprüfung, danach einschlägige Klauselverbote aus §§ 308, 309 BGB und § 310 BGB einordnen.
5. **Spezialfokus:** Bei Vollmacht Vertretung besonders auf wirtschaftlichen Zweck, versteckte Belastung, Verständlichkeit, Nachweisbarkeit und praxistaugliche Durchführung achten.
6. **Rechtsfolge:** Unwirksamkeit, gesetzliche Ersatzregel, Rückzahlung, Vertragsfortbestand, Prozess- und UKlaG-Risiko prüfen.
7. **Verbesserung:** mindestens eine sichere Ersatzfassung und bei Bedarf eine verhandelbare Fallback-Fassung formulieren.

## Output

| Punkt | Befund |
| --- | --- |
| Klauselzweck | ... |
| AGB-Kontrolle | ja/nein/unklar, warum |
| Hauptangriff | ... |
| Verteidigung | ... |
| Risiko | Grün/Gelb/Rot |
| Bessere Fassung | ... |
| offene Tatsachen | ... |

## Qualitätsregeln

- Keine Scheinzitate. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine geltungserhaltende Reduktion als Standardlösung anbieten.
- Bei B2B nicht so tun, als sei alles frei verhandelbar; Transparenz und Leitbild bleiben wichtig.
- Bei B2C streng, verständlich und dokumentationsfähig formulieren.
- Wenn eine Klausel wirtschaftlich gewollt, aber rechtlich riskant ist: Risiko offen labeln und Fallback anbieten.

## Quellenanker

Siehe `references/QUELLEN.md`, `references/PRUEFLOGIK.md` und `references/KLAUSELFAMILIEN.md`.
