---
name: workflow-output-waehlen
description: "Output-Auswahl im gewerblichen Rechtsschutz: Welches Ergebnisformat passt zur Aufgabe? Schriftsatz, Memo, Checkliste, Tabelle, Mandantenbrief, Risikoampel, Entwurf, Red-Team. Entscheidungsbaum und Formatbeschreibungen."
---

# Output-Auswahl

## Aufgabe
Dieser Workflow-Skill hilft bei der Entscheidung, welches Output-Format für die aktuelle Aufgabe am besten geeignet ist, und liefert Beschreibungen und Einsatzbereiche der verfügbaren Formate.

## Output-Formate im Überblick

| Format | Wann einsetzen | Typischer Empfänger |
|---|---|---|
| Memo / Prüfvermerk | Rechtliche Einordnung; interne Analyse | Anwalt / Team |
| Mandantenbrief | Information, Entscheidungsvorlage, Abschluss | Mandant |
| Schriftsatz-Gerüst | Klageschrift, EV-Antrag, Schriftsatz | Gericht (extern) |
| Checkliste | Schritt-für-Schritt-Kontrolle; Qualitätsgate | Anwalt / Team |
| Tabelle / Matrix | Vergleich, Übersicht, Belege, Kosten | Intern / Mandant |
| Risikoampel | Schnelle Bewertung; Entscheidungsbasis | Mandant / Anwalt |
| Entwurf | Abmahnung, UE, Vergleich, Bescheid | Gegenseite / Mandant |
| Red-Team-Analyse | Schwächen im eigenen Vortrag identifizieren | Anwalt / Team |
| Fristenplan | Übersicht laufender Fristen | Anwalt / Team |
| Rechtsquellen-Report | Normnachweis; Quellenverifikation | Anwalt |

## Entscheidungsbaum Output-Wahl

```
Aufgabe: Was ist das Ziel?
│
├── Rechtliche Analyse für interne Entscheidung
│       → Memo / Prüfvermerk
│
├── Kommunikation mit Mandant
│   ├── Information über Sachstand → Statusbericht
│   ├── Entscheidung einfordern → Entscheidungsvorlage
│   └── Mandat abschließen → Abschlussbrief
│
├── Gerichtliches Dokument
│   ├── Klage / EV-Antrag → Schriftsatz-Gerüst
│   └── Widerspruch / Beschwerde → Schriftsatz-Gerüst
│
├── Prüfung der eigenen Position
│   └── Schwächen / Gegenargumente → Red-Team-Analyse
│
├── Verwaltung / Prozesssteuerung
│   ├── Fristen kontrollieren → Fristenplan + Risikoampel
│   ├── Dokumente erfassen → Belegmatrix
│   └── Qualitätsgate vor EV → Checkliste
│
└── Normen und Rechtsprechung verifizieren
        → Rechtsquellen-Report
```

## Format-Beschreibungen

### Memo / Prüfvermerk

**Struktur:**
1. Sachverhalt (streitig / unstreitig).
2. Rechtliche Einordnung (Normen, Tatbestand).
3. Prüfung im Gutachtenstil (Obersatz, Definition, Subsumtion, Zwischenergebnis).
4. Handlungsempfehlung (konkret, mit Frist).

**Länge:** 1–3 Seiten für Einzel-Frage; bis 10 Seiten bei komplexen Mandaten.

### Schriftsatz-Gerüst

**Struktur:**
1. Rubrum (Parteien, Gericht, Az.).
2. Klageanträge / Antragsformulierung.
3. Sachverhalt.
4. Rechtliche Würdigung (je Klageantrag).
5. Beweisangebote.
6. Kostenantrag.

### Risikoampel

**Struktur:**
- Ampel: Grün / Gelb / Rot.
- 3–5 Stichpunkte pro Kategorie.
- Empfehlung in einem Satz.

### Checkliste

**Struktur:**
- Überschrift mit Kontext.
- Punkte als Checkboxen (☐).
- Priorität (MUSS / SOLL / KANN).
- Feld für Status / Verantwortlichen.

### Tabelle / Matrix

**Varianten:**
- Prüfmatrix: Punkt | Norm | Tatsache | Beleg | Bewertung | To-do.
- Vergleichstabelle: Option A | Option B | Vor/Nachteil.
- Belegmatrix: Dokument | Datum | Bezug | Vorhanden.

### Red-Team-Analyse

**Struktur:**
- Stärken des eigenen Vortrags.
- Schwächen (Angriffspunkte der Gegenseite).
- Gegenargumente.
- Verbesserungsmaßnahmen.

## Kaltstart
1. Was ist das Ziel der aktuellen Aufgabe?
2. Für wen ist das Ergebnis bestimmt (intern / Mandant / Gericht)?
3. Wie viel Zeit ist verfügbar?
4. Liegt Material vor, das eingearbeitet werden soll?
5. Output: Output-Empfehlung, Format-Muster, Gerüst für das gewählte Format?

## Anschluss-Skills
Nach Wahl des Formats: passenden Spezial- oder Workflow-Skill aufrufen:
- Schriftsatz → `spezial-patg-schriftsatz-brief-und-memo-bausteine`, `gr-abmahnung-workflow`.
- Risikoampel → `spezial-markeng-risikoampel-und-gegenargumente`, `workflow-fristen-und-risikoampel`.
- Red-Team → `workflow-redteam-qualitygate`, `spezial-designverletzung-red-team-und-qualitaetskontrolle`.
- Checkliste → `faevvollzug-neu-008-qualitaetsgate-vor-vollziehung`, `workflow-dokumentenintake`.
- Mandantenbrief → `workflow-mandantenkommunikation`, `spezial-einstweilige-mandantenkommunikation-entscheidungsvorlage`.

## Quellenregel
- Dieser Skill trifft keine inhaltlichen Rechtsentscheidungen.
- Format-Vorschläge basieren auf fachlicher Praxis; Anpassung je Einzelfall.
- Keine BeckRS-, juris- oder Kommentar-Blindzitate aus Modellwissen.
- Annahmen ausdrücklich markieren.

## Was dieser Skill nicht macht
- Keine inhaltliche Rechtsprüfung.
- Kein Ersatz für vollständige Mandantenberatung.
- Kein vollständiger Schriftsatz ohne Eingaben des Nutzers.
