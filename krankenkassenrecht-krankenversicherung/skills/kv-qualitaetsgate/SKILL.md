---
name: kv-qualitaetsgate
description: "Kv 080 Qualitaetsgate Krankenversicherungsakte: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Kv 080 Qualitaetsgate Krankenversicherungsakte

## Arbeitsbereich

In diesem Skill wird **Kv 080 Qualitaetsgate Krankenversicherungsakte** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-080-qualitaetsgate-krankenversicherungsakte` | Qualitätssicherung und Schlusscheck für Krankenversicherungsakte: vollständige Unterlagenprüfung, Fristen, Rechtswegerklärung, Dokumentationslücken und Handlungsempfehlungen. |

## Arbeitsweg

Für **Kv 080 Qualitaetsgate Krankenversicherungsakte** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `krankenkassenrecht-krankenversicherung` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-080-qualitaetsgate-krankenversicherungsakte`

**Fokus:** Qualitätssicherung und Schlusscheck für Krankenversicherungsakte: vollständige Unterlagenprüfung, Fristen, Rechtswegerklärung, Dokumentationslücken und Handlungsempfehlungen.

# Qualitätsgate: Krankenversicherungsakte

## Skill-Zweck

Dieser Skill fungiert als **Schlusscheck** für jeden Fall im Krankenversicherungsrecht: Vollständigkeit der Unterlagen, offene Fristen, lückenlose Dokumentation, Normencheck und Handlungsempfehlung für den nächsten Schritt.

## Rechtlicher Rahmen

- Alle relevanten Normen des SGB V, SGB X, SGG, VVG und SGB IX (je nach Fall)
- BSG-Grundsätze: Vollbeweis, Kausalität, Beweislast
- DSGVO Art. 5 (Datenschutzgrundsätze): Integrität und Korrektheit der Akte

## Qualitätsgate-Checkliste

| Prüfpunkt | Erfüllt? | Maßnahme bei Fehlen |
|-----------|---------|---------------------|
| Diagnose mit ICD-10 belegt | ✓/✗ | Arztbrief nachfordern |
| Anspruchsgrundlage klar benannt | ✓/✗ | Normzitat ergänzen |
| Fristen berechnet und dokumentiert | ✓/✗ | Fristenplan erstellen |
| MDK-Gutachten vorhanden und geprüft | ✓/✗ | Akteneinsicht anfordern |
| Widerspruchsfrist gesichert | ✓/✗ | Fristwahrenden Widerspruch sofort |
| Gegenbeweis/Gegengutachten organisiert | ✓/✗ | Arzt-Briefing vorbereiten |
| Rechtsweg festgelegt (SGG/ZPO) | ✓/✗ | Zuständiges Gericht prüfen |
| Datenschutz beachtet | ✓/✗ | DSGVO-Konformität sicherstellen |

## Prüfprogramm

### Schritt 1 – Unterlagencheck
- Ärztliche Unterlagen: aktueller Arztbrief (nicht älter als 6 Monate), relevante Vorbefunde
- GKV: Ablehnungsbescheid vollständig? Begründung klar? Rechtsbehelfsbelehrung vorhanden?
- PKV: Tarifbedingungen, Versicherungsschein, letzte Beitragsabrechnung
- MDK-Gutachten: liegt vor? Eingesehen? Inhaltlich analysiert?

### Schritt 2 – Normencheck
- Welche Norm ist die Anspruchsgrundlage? (z.B. § 33 SGB V, § 192 VVG)
- BSG-/BGH-Rechtsprechung zur Norm aktuell geprüft?
- G-BA-Richtlinie einschlägig? (z.B. Hilfsmittel-RL, AM-RL, HM-RL)

### Schritt 3 – Fristen sichern
- Widerspruchsfrist: 1 Monat ab Bekanntgabe (§ 84 SGG); berechnet?
- Klagefrist: 1 Monat nach Widerspruchsbescheid (§ 87 SGG)
- PKV-Verjährung: 3 Jahre (§ 195 BGB); wann beginnt sie?
- Beitragsverjährung GKV: 4 Jahre (§ 25 SGB IV)

### Schritt 4 – Beweislage
- Vollbeweis für Anspruchsvoraussetzungen gesichert?
- Kausalität zwischen Erkrankung und Leistungsbedarf dokumentiert?
- Beweislastumkehr geprüft? (grober Behandlungsfehler → § 630h Abs. 5 BGB)

### Schritt 5 – Handlungsempfehlung
- Sofortmaßnahme: Frist wahren, Unterlagen anfordern, Eilantrag
- Mittelfristig: Widerspruch begründen, Gegengutachten organisieren
- Langfristig: Klage vorbereiten, SG-Sachverständigen beantragen
- Eskalationspfad: Widerspruch → Klage SG → Berufung LSG → Revision BSG

## Typische Fallen

- **Qualitätsgate zu spät**: Erst nach Fristablauf alle Unterlagen zusammen → Wiedereinsetzung prüfen aber schwierig.
- **Vollbeweis durch Zweifel geschwächt**: Ein ungeklärtes medizinisches Detail → BSG-Maßstab genau anwenden; teilweise reicht Wahrscheinlichkeit.
- **Mehrere Fristen gleichzeitig laufend**: Bei Widerspruch zu mehreren Bescheiden → separater Fristenkalender.
- **Keine Übergabe an Anwalt**: Komplexe Fälle ohne Anwalt riskieren Formfehler; Beratungshilfe nutzen.

## Output-Formate

- Qualitätssicherungs-Protokoll (je Fall)
- Fristen-Übersichtskalender
- Unterlagen-Vollständigkeitsliste
- Normen-Referenz-Übersicht
- Handlungsempfehlungs-Zusammenfassung

## Quellen

- [SGB V – Gesamtüberblick](https://www.gesetze-im-internet.de/sgb_5/)
- [SGG – Sozialgerichtsgesetz](https://www.gesetze-im-internet.de/sgg/)
- [§ 84 SGG – Widerspruchsfrist](https://www.gesetze-im-internet.de/sgg/__84.html)
- [BSG Entscheidungssuche](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [G-BA Richtlinien](https://www.g-ba.de/richtlinien/)
- [dejure.org SGB V](https://dejure.org/gesetze/SGB_V)
- [openjur.de – Sozialrecht](https://openjur.de)
