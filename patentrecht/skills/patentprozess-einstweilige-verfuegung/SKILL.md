---
name: patentprozess-einstweilige-verfuegung
description: "Patentprozess Einstweilige Verfuegung De Upc, Patentprozess Experten Und Sachverstaendige, Patentprozess Kostensicherheit Und Budget: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Patentprozess Einstweilige Verfuegung De Upc, Patentprozess Experten Und Sachverstaendige, Patentprozess Kostensicherheit Und Budget

## Arbeitsbereich

In diesem Skill wird **Patentprozess Einstweilige Verfuegung De Upc, Patentprozess Experten Und Sachverstaendige, Patentprozess Kostensicherheit Und Budget** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `patentprozess-einstweilige-verfuegung-de-upc` | Plant einstweiligen Rechtsschutz in Patentverletzungssachen vor deutschen Gerichten und UPC: Dringlichkeit, Schutzrechtsbestand, Verletzungsnachweis, Schutzschrift, Sicherheitsleistung und Vollziehung. |
| `patentprozess-experten-und-sachverstaendige` | Plant technische Expertenarbeit in Patentverfahren: Privatgutachten, gerichtliche Sachverständige, Parteigutachten, Experimente, Reproduzierbarkeit, Befragung und Schwachstellenanalyse. |
| `patentprozess-kostensicherheit-und-budget` | Erstellt Kosten- und Risikoüberblick für Patentstreitigkeiten: Gerichtskosten, Anwalt, Patentanwalt, Sachverständige, Übersetzungen, Sicherheitsleistung, UPC-/Auslandsbudget und Vergleichswert. |

## Arbeitsweg

Für **Patentprozess Einstweilige Verfuegung De Upc, Patentprozess Experten Und Sachverstaendige, Patentprozess Kostensicherheit Und Budget** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `patentrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `patentprozess-einstweilige-verfuegung-de-upc`

**Fokus:** Plant einstweiligen Rechtsschutz in Patentverletzungssachen vor deutschen Gerichten und UPC: Dringlichkeit, Schutzrechtsbestand, Verletzungsnachweis, Schutzschrift, Sicherheitsleistung und Vollziehung.

# Patentprozess: Einstweilige Verfügung DE/UPC

## Aufgabe

Eilverfahren mit deutscher und UPC-Perspektive.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Kenntniszeitpunkte und Dringlichkeitsverlust rekonstruieren.**
2. **Rechtsbestandssicherheit und Verletzungsbeweis getrennt prüfen.**
3. **Schutzschrift/Protective Letter und Vergleichsfenster abwägen.**
4. **Antrag, Anlagen, Glaubhaftmachung und Geheimnisschutz strukturieren.**
5. **Vollziehung, Sicherheitsleistung und Kommunikation vorbereiten.**


## Prüfmatrix

| Ebene | Prüffrage | Ergebnis |
| --- | --- | --- |
| Schutzrecht | Welche Anspruchsfassung, welcher Status, welche Priorität und welche Territorien? | Register live prüfen; Annahmen markieren. |
| Technik | Welche Merkmale, Varianten, Ausführungsformen und Belege sind wirklich tragend? | Merkmalsgliederung/Claim Chart. |
| Verfahren | Welches Forum, welche Frist, welche Sprache, welche Verfahrensart? | Forum- und Fristenampel. |
| Rechtsbestand | Welche Angriffe tragen realistisch und welche Belege fehlen? | Invalidity-/Opposition-Map. |
| Strategie | Was ist wirtschaftlich sinnvoll: Angriff, Verteidigung, Design-around, Lizenz, Vergleich? | Handlungsempfehlung. |

## Output

Erzeuge je nach Auftrag:

- PI Go/No-go.
- Evidence Affidavit Plan.
- Protective Letter Points.
- Hearing Outline.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.

## 2. `patentprozess-experten-und-sachverstaendige`

**Fokus:** Plant technische Expertenarbeit in Patentverfahren: Privatgutachten, gerichtliche Sachverständige, Parteigutachten, Experimente, Reproduzierbarkeit, Befragung und Schwachstellenanalyse.

# Patentprozess: Experten und Sachverständige

## Aufgabe

Technische Evidenz gerichts- und verhandlungsfest machen.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Beweisfrage in technische Testhypothese übersetzen.**
2. **Geeignete Expertise und Unabhängigkeit prüfen.**
3. **Testdesign, Dokumentation und Reproduzierbarkeit sichern.**
4. **Gegenexperten- und Cross-Examination-Fragen vorbereiten.**
5. **Ergebnis in Claim Chart und Schriftsatzlogik übertragen.**


## Prüfmatrix

| Ebene | Prüffrage | Ergebnis |
| --- | --- | --- |
| Schutzrecht | Welche Anspruchsfassung, welcher Status, welche Priorität und welche Territorien? | Register live prüfen; Annahmen markieren. |
| Technik | Welche Merkmale, Varianten, Ausführungsformen und Belege sind wirklich tragend? | Merkmalsgliederung/Claim Chart. |
| Verfahren | Welches Forum, welche Frist, welche Sprache, welche Verfahrensart? | Forum- und Fristenampel. |
| Rechtsbestand | Welche Angriffe tragen realistisch und welche Belege fehlen? | Invalidity-/Opposition-Map. |
| Strategie | Was ist wirtschaftlich sinnvoll: Angriff, Verteidigung, Design-around, Lizenz, Vergleich? | Handlungsempfehlung. |

## Output

Erzeuge je nach Auftrag:

- Expert Brief.
- Test Protocol.
- Weakness Questions.
- Hearing Prep Sheet.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.

## 3. `patentprozess-kostensicherheit-und-budget`

**Fokus:** Erstellt Kosten- und Risikoüberblick für Patentstreitigkeiten: Gerichtskosten, Anwalt, Patentanwalt, Sachverständige, Übersetzungen, Sicherheitsleistung, UPC-/Auslandsbudget und Vergleichswert.

# Patentprozess: Kosten, Sicherheit und Budget

## Aufgabe

Budgetfähigkeit und Prozessökonomie vor Patentdurchsetzung oder Verteidigung.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Forum, Streitwert, technische Komplexität und Dauer einschätzen.**
2. **Interne/externe Kostenblöcke erfassen.**
3. **Sicherheitsleistung, Kostenerstattung und Vollziehungsrisiken prüfen.**
4. **Szenarien: PI, Hauptsache, Rechtsmittel, Vergleich bilden.**
5. **Mandantenfähiges Kosten-/Nutzen-Memo liefern.**


## Prüfmatrix

| Ebene | Prüffrage | Ergebnis |
| --- | --- | --- |
| Schutzrecht | Welche Anspruchsfassung, welcher Status, welche Priorität und welche Territorien? | Register live prüfen; Annahmen markieren. |
| Technik | Welche Merkmale, Varianten, Ausführungsformen und Belege sind wirklich tragend? | Merkmalsgliederung/Claim Chart. |
| Verfahren | Welches Forum, welche Frist, welche Sprache, welche Verfahrensart? | Forum- und Fristenampel. |
| Rechtsbestand | Welche Angriffe tragen realistisch und welche Belege fehlen? | Invalidity-/Opposition-Map. |
| Strategie | Was ist wirtschaftlich sinnvoll: Angriff, Verteidigung, Design-around, Lizenz, Vergleich? | Handlungsempfehlung. |

## Output

Erzeuge je nach Auftrag:

- Litigation Budget Table.
- Scenario Cost Memo.
- Security Checklist.
- Board Decision Note.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.
