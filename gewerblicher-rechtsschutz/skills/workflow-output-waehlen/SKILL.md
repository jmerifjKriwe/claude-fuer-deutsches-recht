---
name: workflow-output-waehlen
description: "Output-Auswahl im Plugin gewerblicher-rechtsschutz: Welches Outputformat passt zur Aufgabe? Entscheidungshilfe für Memo, Checkliste, Schriftsatz, Tabelle, Fristenplan, Ampel, Entwurf oder Red-Team. Qualitätsstandards für jeden Outputtyp."
---

# Workflow: Output-Format wählen

## Zweck

Dieser Skill hilft beim **Auswählen des richtigen Outputformats** im Plugin `gewerblicher-rechtsschutz`. Das Ergebnis einer rechtlichen Analyse kann in vielen Formaten ausgegeben werden – nicht jedes Format passt zu jeder Aufgabe. Dieser Skill stellt sicher, dass das Ergebnis in der Form geliefert wird, die operativ am nützlichsten ist.

Mandatsbezug: Anwalt fragt: Soll ich das als Memo oder als Checkliste ausgeben? Mandant fragt: Ich brauche das für den Vorstand – was ist das beste Format? Kanzleimitarbeiter: Ich brauche eine Übersicht, keine langen Texte.

## Entscheidungsmatrix: Format nach Verwendungszweck

| Verwendungszweck | Empfohlenes Format | Alternativen |
|---|---|---|
| Anwalt prüft Fall intern | Memo im Gutachtenstil | Checkliste |
| Mandant entscheidet | Entscheidungsvorlage (Optionen-Tabelle) | Memo |
| Vorstandspräsentation | Tabelle + Kurzfazit | Ampel-Übersicht |
| Schriftsatz einreichen | Formaler Schriftsatz-Entwurf | – |
| Frist überwachen | Fristenplan | Checkliste |
| Abmahnung versenden | Abmahnschreiben-Entwurf | – |
| Reaktion auf Abmahnung | Checkliste + Entscheidungsvorlage | Memo |
| Qualitätssicherung | Red-Team-Protokoll | Checkliste |
| Überblick verschaffen | Ampel-Tabelle | Zusammenfassung |
| Beweissicherung | Belegmatrix-Tabelle | Checkliste |
| Mandantenbrief | Brief-Template | Memo |

## Outputtypen und Qualitätsstandards

### Typ 1 – Rechtliches Memo (Gutachtenstil)

**Einsatz:** Interne Prüfung; Anwalt beurteilt Rechtslage.

**Struktur:**
1. Sachverhalt (Tatsachen, streitig/unstreitig)
2. Rechtliche Prüfung (Obersatz, Definition, Subsumtion, Ergebnis)
3. Ergebnis (Kurzfazit + Empfehlung)
4. Quellen (mit Gericht/Datum/AZ/Link)

**Qualitätsstandard:**
- Keine Scheingenauigkeit.
- Offene Punkte markieren.
- Keine BeckRS-Blindzitate.

### Typ 2 – Checkliste

**Einsatz:** Praktische Durchführung (Abmahnung versenden, EV vollziehen).

**Struktur:**
- Nummerierte oder kategorisierte Punkte.
- Je Punkt: Aktion + Verantwortlicher + Status (offen/erledigt).
- Kritische Punkte hervorheben.

**Qualitätsstandard:**
- Vollständig (kein wesentlicher Punkt fehlt).
- Aktionsformulierungen (was TUN, nicht was ist).

### Typ 3 – Schriftsatz-Entwurf

**Einsatz:** EV-Antrag, Klageschrift, Widerspruch.

**Struktur:**
- Rubrum (Parteien, Gericht, AZ)
- Antrag (präziser Tenor)
- Begründung (Sachverhalt + Rechtliches)
- Anlagen-Verzeichnis

**Qualitätsstandard:**
- Tenor präzise; nicht zu weit.
- Rechtliche Begründung mit Normen und Rechtsprechung.
- Anlagen vollständig aufgelistet.

### Typ 4 – Tabelle / Matrix

**Einsatz:** Übersicht (Schutzrechte, Fristen, Parteien, Verletzungshandlungen).

**Struktur:**
- Spalten: Einheit (Norm, Partei, Frist, Risiko).
- Zeilen: Einzelne Elemente.
- Ampelfarben wo sinnvoll.

**Qualitätsstandard:**
- Konsistente Spaltenköpfe.
- Keine inhaltlichen Lücken in wesentlichen Zeilen.

### Typ 5 – Fristenplan

**Einsatz:** Mandantenübergabe; Mandatsübergabe; Kanzleiintern.

**Struktur:**
- Frist / Auslöser / Fristende / Restzeit / Ampel / Nächster Schritt.

**Qualitätsstandard:**
- Nur verifizierte Fristen eintragen.
- Fristende berechnet (nicht geschätzt).

### Typ 6 – Risikoampel

**Einsatz:** Schnelle Lageeinschätzung; Vorstandsinfo.

**Struktur:**
- Farbkodierung Grün/Gelb/Rot mit kurzer Begründung.
- Gesamtampel + Einzelampeln je Aspekt.

**Qualitätsstandard:**
- Begründung für jede Ampelfarbe.
- Keine unreflektierten Grün-Ampeln bei unklaren Lagen.

### Typ 7 – Abmahnschreiben / Brief

**Einsatz:** Kommunikation nach außen.

**Struktur:**
- Briefkopf, Datum, Betreffzeile.
- Klar strukturierter Hauptteil.
- Konkreter Handlungsaufruf.

**Qualitätsstandard:**
- Formvoraussetzungen je nach Rechtsgebiet (§ 13 UWG, § 97a UrhG).
- Keine unangemessene Drohung; sachliche Tonalität.

### Typ 8 – Red-Team-Protokoll

**Einsatz:** Qualitätssicherung vor Versand.

**Struktur:**
- Stärken / Schwachstellen / Gegenargumente / Empfehlung.

**Qualitätsstandard:**
- Keine blinden Flecken; systematische Gegenargumentprüfung.

## Auswahl-Shortcut

```
OUTPUTFORMAT-KURZWAHL

Wenn Adressat = interner Anwalt → Memo oder Checkliste
Wenn Adressat = Mandant → Entscheidungsvorlage oder Brief
Wenn Adressat = Gericht / Behörde → Schriftsatz-Entwurf
Wenn Zeitdruck + Überblick → Ampel + Kurzfazit
Wenn Kontrolle vor Versand → Red-Team-Protokoll
Wenn Frist-Überblick → Fristenplan
Wenn Beweissicherung → Belegmatrix
```

## Quellenregel

- Dieser Skill ist ein Prozess-Skill; keine externen Quellen nötig.
- Inhaltliche Outputs folgen den Quellenregeln des jeweiligen Themen-Skills.

## Anschluss-Skills

- `workflow-mandantenkommunikation` – Mandantenkommunikation
- `spezial-freedom-schriftsatz-brief-und-memo-bausteine` – Schriftsatz-Bausteine
- `workflow-redteam-qualitygate` – Red-Team-Prüfung
- `spezial-compliance-mandantenkommunikation-entscheidungsvorlage` – Entscheidungsvorlage
