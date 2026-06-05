---
name: japan-jpo-kanada-cipo-loeschung-widerruf
description: "Japan Patentrecht Jpo Ip High Court, Kanada Patentrecht Cipo Federal Court, Löschung Widerruf Nichtigkeit Global Route: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Japan Patentrecht Jpo Ip High Court, Kanada Patentrecht Cipo Federal Court, Löschung Widerruf Nichtigkeit Global Route

## Arbeitsbereich

In diesem Skill wird **Japan Patentrecht Jpo Ip High Court, Kanada Patentrecht Cipo Federal Court, Löschung Widerruf Nichtigkeit Global Route** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `japan-patentrecht-jpo-ip-high-court` | Strukturiert japanische Patentfragen: J-PlatPat, JPO-Prüfung, Opposition/Invalidation Trial, Korrektur, IP High Court, Übersetzung und lokale Vertretung. |
| `kanada-patentrecht-cipo-federal-court` | Prüft kanadische Patentfragen: CIPO-Recherche und Prosecution, Patent Appeal Board, Re-examination, Federal Court, PM(NOC)-Schnittstellen und bilinguale Local-Counsel-Fragen. |
| `loeschung-widerruf-nichtigkeit-global-route` | Koordiniert Rechtsbestandsangriffe international: EPA-Einspruch, UPC-Revocation, deutsche Nichtigkeit, UK revocation, US PTAB, Kanada, Japan, Schweiz, Türkei und Israel. |

## Arbeitsweg

Für **Japan Patentrecht Jpo Ip High Court, Kanada Patentrecht Cipo Federal Court, Löschung Widerruf Nichtigkeit Global Route** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `patentrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `japan-patentrecht-jpo-ip-high-court`

**Fokus:** Strukturiert japanische Patentfragen: J-PlatPat, JPO-Prüfung, Opposition/Invalidation Trial, Korrektur, IP High Court, Übersetzung und lokale Vertretung.

# Japan: JPO und IP High Court

## Aufgabe

Japan-spezifische Prosecution- und Rechtsbestandsroute mit Übersetzungs- und Vertreterbedarf.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **J-PlatPat/JPO-Daten mit Patentfamilie abgleichen.**
2. **Anspruchs- und Übersetzungsrisiken markieren.**
3. **Opposition, Invalidation Trial und Correction Trial trennen.**
4. **IP High Court/Verletzungsgericht nur als lokale Counsel Route behandeln.**
5. **Japanisches Claim Chart für Counsel vorbereiten.**


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

- Japan Patent Status Note.
- JPO Trial Decision Tree.
- Translation Risk List.
- Local Counsel Bundle.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.

## 2. `kanada-patentrecht-cipo-federal-court`

**Fokus:** Prüft kanadische Patentfragen: CIPO-Recherche und Prosecution, Patent Appeal Board, Re-examination, Federal Court, PM(NOC)-Schnittstellen und bilinguale Local-Counsel-Fragen.

# Kanada: CIPO, Federal Court und Patentstreit

## Aufgabe

Kanadisches Patentrecht als eigener Markt, nicht als US-Anhang.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Kanadische Anmeldung, Priorität und Status über CIPO prüfen.**
2. **Patentfähigkeit und Anspruchsform mit lokalen Besonderheiten markieren.**
3. **Re-examination, Impeachment/Validity und Federal-Court-Route unterscheiden.**
4. **Pharma/PM(NOC)-Bezug gesondert abfragen.**
5. **Local Counsel Brief mit Unterlagen und Fristen erstellen.**


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

- Canada Patent Checklist.
- CIPO Register Tasks.
- Federal Court Route Memo.
- Local Counsel Questions.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.

## 3. `loeschung-widerruf-nichtigkeit-global-route`

**Fokus:** Koordiniert Rechtsbestandsangriffe international: EPA-Einspruch, UPC-Revocation, deutsche Nichtigkeit, UK revocation, US PTAB, Kanada, Japan, Schweiz, Türkei und Israel.

# Löschung, Widerruf, Nichtigkeit: globale Route

## Aufgabe

Globaler Rechtsbestandsangriff mit Kosten-/Timing- und Settlement-Logik.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Patentfamilie und relevante Länder filtern.**
2. **Angriffsgründe pro Forum mappen.**
3. **Fristen, Standing, Kosten und Beweisbedarf vergleichen.**
4. **Parallelverfahren und Estoppel-/Präklusionsrisiken markieren.**
5. **Master-Zeitplan mit Entscheidungsfenstern erstellen.**


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

- Global Invalidity Roadmap.
- Forum Comparison Table.
- Prior Art Package.
- Settlement Leverage Memo.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.
