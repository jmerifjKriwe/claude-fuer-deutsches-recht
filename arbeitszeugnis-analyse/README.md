# Arbeitszeugnis-Analyse (Ampelsystem)

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`arbeitszeugnis-analyse`) | [`arbeitszeugnis-analyse.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnis-analyse.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Arbeitszeugnis-Analyse — aus dem blühenden Leben** (`arbeitszeugnis-analyse-bluehendes-leben`) | [Gesamt-PDF lesen](../testakten/arbeitszeugnis-analyse-bluehendes-leben/gesamt-pdf/arbeitszeugnis-analyse-bluehendes-leben_gesamt.pdf) | [`testakte-arbeitszeugnis-analyse-bluehendes-leben.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-arbeitszeugnis-analyse-bluehendes-leben.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin analysiert deutsche Arbeitszeugnisse nach dem Ampelsystem (Rot/Orange/Grün). Es decodiert den Geheimcode der deutschen Zeugnissprache, identifiziert notenrelevante Sätze und klassifiziert sie mit vollständiger Interpretation der versteckten Bewertung.

Das Plugin richtet sich an Arbeitnehmer, die ihr eigenes Zeugnis verstehen oder verbessern wollen, an Rechtsanwälte, die Zeugnisstreitigkeiten begleiten, und an Personalverantwortliche, die Zeugnisse professionell ausstellen oder prüfen möchten.

**Hinweis:** Im Repository liegt ergänzend die Testakte `testakten/arbeitszeugnis-analyse-bluehendes-leben/` mit zehn realistisch ausgearbeiteten Zeugnisfällen. Jede Ausgabe ist ein Analyse-Entwurf zur eigenverantwortlichen Prüfung — kein Ersatz für anwaltliche Beratung im Einzelfall.

## Ampelsystem

Das Ampelsystem klassifiziert jeden notenrelevanten Satz in drei Kategorien:

| Ampel | Bedeutung | Notentendenz |
|---|---|---|
| **Grün** | Starke positive Formulierung, entspricht dem Geheimcode für Note 1 oder Note 2 | Note 1-2 |
| **Orange** | Schwache positive Formulierung, Note 3, oft durch fehlende Steigerungsadverbien oder Einschränkungen | Note 3 |
| **Rot** | Kodierte Negativaussage, entspricht Note 4 oder Note 5, oft scheinbar positiv formuliert | Note 4-5 |

Rote Signale entstehen durch: das Wort "bemüht", Einschränkungen wie "im Wesentlichen", fehlende positionsnahe Erwartungsbausteine wie Integritäts- oder Führungsverhalten, falsche Reihenfolge bei Personengruppen in der Verhaltensbeurteilung oder eine auffällig kühle Schlussformel. Bei der Schlussformel ist strikt zu trennen: starke Signalwirkung im Bewerbungsverkehr, aber kein automatischer einklagbarer Anspruch auf Dank, Bedauern und Wünsche.

## Enthaltene Skills

Die wichtigsten Skills sind alphabetisch geordnet; die vollständige automatisch generierte Liste steht weiter unten:

| Skill | Funktion |
|---|---|
| `/arbeitszeugnis-analyse:ampelsystem-tabellenausgabe` | Standardisiertes Ausgabeformat mit Ampeltabelle (Satz / Ampel / Bewertung / Note / Begründung) |
| `/arbeitszeugnis-analyse:aufforderungsschreiben-arbeitgeber` | Außergerichtliches Berichtigungsverlangen an den Arbeitgeber mit Wortlaut alt/neu pro Streitstelle |
| `/arbeitszeugnis-analyse:azubi-zeugnis-analyse` | Ausbildungszeugnisse nach BBiG: Lernfortschritt, Berufsschule, Praxis, Verhalten |
| `/arbeitszeugnis-analyse:bereichs-drift-detektor` | Erkennt das Schaufenster-Pattern: Spitzensatz und Durchschnittssatz im selben Themenbereich |
| `/arbeitszeugnis-analyse:branchen-spezifische-formulierungen` | Branchenspezifika für Vertrieb, Recht, IT, Pflege und weitere Bereiche |
| `/arbeitszeugnis-analyse:erstgespraech-und-mandatsannahme` | Mandatsannahme mit Dank für das Zeugnis, Anforderung der noch fehlenden Unterlagen, Erstgespräch-Leitfaden |
| `/arbeitszeugnis-analyse:geheimcode-katalog` | Zentraler Referenzkatalog aller Standardformulierungen mit Ampelzuordnung |
| `/arbeitszeugnis-analyse:gesamtnoten-aggregation` | Aggregation der Einzelbewertungen zur gewichteten Gesamtnote |
| `/arbeitszeugnis-analyse:gruen-flaggen-katalog` | Katalog aller grünen Signale: Superlative, vollständige Formeln, Note 1-2 |
| `/arbeitszeugnis-analyse:klage-strategie-zeugnisberichtigung` | Vom Befund zur Klage: Berichtigungsverlangen, Klageantrag, Beweislast, Streitwert |
| `/arbeitszeugnis-analyse:leitende-positionen-zeugnisse` | Führungskräfte-Zeugnisse: Mitarbeiterführung, Strategie, Loyalität |
| `/arbeitszeugnis-analyse:leistungsbeurteilung-analyse` | Arbeitsqualität, Arbeitsbereitschaft, Belastbarkeit, Eigeninitiative |
| `/arbeitszeugnis-analyse:mandantenbericht-zeugnisanalyse` | Ergebnisbericht an den Arbeitnehmer mit Gesamtnote, kritischen Stellen, drei Handlungsoptionen, klarer Empfehlung |
| `/arbeitszeugnis-analyse:muster-arbeitszeugnis-gemischte-noten` | Schulungsmuster mit Schaufenster-Pattern: 1er- und 3er-Sätze gemischt, vollständige Drift-Analyse |
| `/arbeitszeugnis-analyse:muster-arbeitszeugnis-mit-roten-flaggen` | Schulungsbeispiel mit gemischten Bewertungen und vollständiger Analyse |
| `/arbeitszeugnis-analyse:muster-arbeitszeugnis-note-1` | Vollständiges Musterzeugnis Note 1 — alle Bausteine grün |
| `/arbeitszeugnis-analyse:negationen-und-auslassungen-erkennen` | Fehlende Pflichtaussagen als versteckte Negativsignale erkennen |
| `/arbeitszeugnis-analyse:negative-codeworte-katalog` | Erweiterter Katalog negativer Codeworte: Alkohol, Krankheit, Diebstahl, Konflikte, Loyalität |
| `/arbeitszeugnis-analyse:notenrelevante-saetze-identifizieren` | Trennung notenrelevanter Sätze von neutralen Aufgabenbeschreibungen |
| `/arbeitszeugnis-analyse:orange-flaggen-katalog` | Schwache positive Formulierungen, Note 3, fehlende Steigerungen |
| `/arbeitszeugnis-analyse:rechtliche-bewertung-bag-rechtsprechung` | § 109 GewO, BAG-Rechtsprechung, Beweislast, Zeugnisklage |
| `/arbeitszeugnis-analyse:rote-flaggen-katalog` | Klassische Warnsignale: "bemüht", "im Großen und Ganzen", Note 4-5 |
| `/arbeitszeugnis-analyse:satzweise-notenmatrix` | Satz-für-Satz-Notenzuweisung von eins bis fünf mit Themenbereich — Datenbasis für Drift |
| `/arbeitszeugnis-analyse:schlussformel-bewertung` | Bedauern, Dank, Zukunftswünsche — Signalwirkung, Ton und rechtliche Durchsetzbarkeit getrennt |
| `/arbeitszeugnis-analyse:steigerungsadverbien-katalog` | Vollständige Referenzliste der Steigerer mit Notenwirkung — echte, scheinbare und negative Adverbien |
| `/arbeitszeugnis-analyse:verbesserungsvorschlaege-formulieren` | Konkrete Textvorschläge zur Aufwertung von roten und orangen Formulierungen |
| `/arbeitszeugnis-analyse:verhaltensbeurteilung-analyse` | Verhalten zu Vorgesetzten, Kollegen, Kunden; Reihenfolge und Euphemismen |
| `/arbeitszeugnis-analyse:widerspruechliche-bewertungen` | Widersprüche zwischen Leistungs-, Verhaltensteil und Schlussformel |
| `/arbeitszeugnis-analyse:zeugnis-problem-sortieren` | Neuer Einstieg für unsortierte Fragen: Was ist eigentlich das Problem am Zeugnis? |
| `/arbeitszeugnis-analyse:zeugnisart-erkennung` | Qualifiziertes/einfaches Zeugnis, Zwischen-/Endzeugnis, Ausbildungszeugnis |
| `/arbeitszeugnis-analyse:zeugnis-ueberblick-extraktion` | Kopfdaten: Arbeitgeber, Arbeitnehmer, Zeitraum, Position, Unterschrift |
| `/arbeitszeugnis-analyse:zufriedenheitsformel-decodierung` | Fünfstufige Zufriedenheitsformel von Note 1 bis Note 5 |

## Verwendung

Laden Sie das zu analysierende Arbeitszeugnis hoch oder fügen Sie es als Text ein. Starten Sie dann mit dem gewünschten Skill:

```
/arbeitszeugnis-analyse:notenrelevante-saetze-identifizieren

Bitte analysiere das folgende Arbeitszeugnis und identifiziere alle notenrelevanten Sätze mit Ampelzuordnung:

[Zeugnis hier einfügen]
```

Für den vollständigen Mandatsablauf empfiehlt sich die Reihenfolge:
1. `erstgespraech-und-mandatsannahme` — Eingangsbestätigung, Unterlagenanforderung, Erstgespräch
2. `zeugnis-ueberblick-extraktion` — Kopfdaten prüfen
3. `zeugnisart-erkennung` — Zeugnistyp bestimmen
4. `notenrelevante-saetze-identifizieren` — Sätze kategorisieren
5. `steigerungsadverbien-katalog` — Adverbien tabellieren und Notenwirkung bestimmen
6. `satzweise-notenmatrix` — Note eins bis fünf pro Satz mit Themenzuordnung
7. `zufriedenheitsformel-decodierung` — Kernformel decodieren
8. `leistungsbeurteilung-analyse` + `verhaltensbeurteilung-analyse` — Detailanalyse
9. `schlussformel-bewertung` — Schlussformel als Signal und als Rechtsproblem getrennt bewerten
10. `negationen-und-auslassungen-erkennen` — Auslassungen prüfen
11. `negative-codeworte-katalog` — Geheimcodes für Alkohol, Krankheit, Diebstahl, Konflikte, Loyalität prüfen
12. `bereichs-drift-detektor` — Schaufenster-Pattern prüfen
13. `widerspruechliche-bewertungen` — Block-Widersprüche prüfen
14. `ampelsystem-tabellenausgabe` — Gesamttabelle
15. `gesamtnoten-aggregation` — Gesamtnote berechnen, inkl. Drift-Penalty
16. `verbesserungsvorschlaege-formulieren` — Aufwertungs-Rewrites pro Satz
17. `rechtliche-bewertung-bag-rechtsprechung` — rechtliche Einordnung der Befunde
18. `mandantenbericht-zeugnisanalyse` — Ergebnisbericht an den Mandanten mit drei Handlungsoptionen
19. `aufforderungsschreiben-arbeitgeber` — außergerichtliches Berichtigungsverlangen
20. `klage-strategie-zeugnisberichtigung` — bei fruchtlosem Fristablauf zur Klage

## Rechtsgrundlagen

- **§ 109 GewO** — Zeugnisanspruch: Anspruch auf einfaches oder qualifiziertes Zeugnis, Wahrheitspflicht, Wohlwollensgebot
- **§ 16 BBiG** — Zeugnisanspruch für Auszubildende
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Kein Ersatz für anwaltliche Beratung. Für die gerichtliche Geltendmachung eines Zeugnisberichtigungsanspruchs ist die Beauftragung eines Rechtsanwalts empfohlen.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 28 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Steuerung für das Arbeitszeugnis-Analyse-Plugin. Erkennt Zeugnisart, Ziel, Fristen, Rollen und Streitniveau, schlägt passende Spezial-Skills aus diesem Plugin vor und führt vom ersten Upload bis zu Ma... |
| `kompendium-01-workflow-chronologie-bis-workflow-fristen-und` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 01; bündelt 2 frühere Spezialskills (workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-02-rechtliche-bewertung-bis-spezial-arbeitszeugn` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 02; bündelt 2 frühere Spezialskills (rechtliche-bewertung-bag-rechtsprechung, spezial-arbeitszeugnisse-fristen-form-und-zustaendigkeit) und bewahrt deren Workflows, Normanker, Prüfp... |
| `kompendium-03-ampelsystem-tabellen-bis-aufforderungsschreib` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 03; bündelt 2 frühere Spezialskills (ampelsystem-tabellenausgabe, aufforderungsschreiben-arbeitgeber) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-04-azubi-zeugnis-analys-bis-bereichs-drift-detek` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 04; bündelt 2 frühere Spezialskills (azubi-zeugnis-analyse, bereichs-drift-detektor) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-05-branchen-spezifische-bis-erstgespraech-und-ma` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 05; bündelt 2 frühere Spezialskills (branchen-spezifische-formulierungen, erstgespraech-und-mandatsannahme) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-06-geheimcode-katalog-bis-gesamtnoten-aggregat` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 06; bündelt 2 frühere Spezialskills (geheimcode-katalog, gesamtnoten-aggregation) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-07-gruen-flaggen-katalo-bis-klage-strategie-zeug` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 07; bündelt 2 frühere Spezialskills (gruen-flaggen-katalog, klage-strategie-zeugnisberichtigung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-08-leistungsbeurteilung-bis-leitende-positionen` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 08; bündelt 2 frühere Spezialskills (leistungsbeurteilung-analyse, leitende-positionen-zeugnisse) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-09-mandantenbericht-zeu-bis-muster-arbeitszeugni` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 09; bündelt 2 frühere Spezialskills (mandantenbericht-zeugnisanalyse, muster-arbeitszeugnis-gemischte-noten) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-10-muster-arbeitszeugni-bis-muster-arbeitszeugni` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 10; bündelt 2 frühere Spezialskills (muster-arbeitszeugnis-mit-roten-flaggen, muster-arbeitszeugnis-note-1) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-11-negationen-und-ausla-bis-negative-codeworte-k` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 11; bündelt 2 frühere Spezialskills (negationen-und-auslassungen-erkennen, negative-codeworte-katalog) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-12-notenrelevante-saetz-bis-orange-flaggen-katal` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 12; bündelt 2 frühere Spezialskills (notenrelevante-saetze-identifizieren, orange-flaggen-katalog) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-13-rote-flaggen-katalog-bis-satzweise-notenmatri` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 13; bündelt 2 frühere Spezialskills (rote-flaggen-katalog, satzweise-notenmatrix) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-14-schlussformel-bewert-bis-spezial-ampelsystem` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 14; bündelt 2 frühere Spezialskills (schlussformel-bewertung, spezial-ampelsystem-dokumentenmatrix-und-lueckenliste) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgab... |
| `kompendium-15-spezial-analyse-erst-bis-spezial-codeworte-co` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 15; bündelt 2 frühere Spezialskills (spezial-analyse-erstpruefung-und-mandatsziel, spezial-codeworte-compliance-dokumentation-und-akte) und bewahrt deren Workflows, Normanker, Prüfp... |
| `kompendium-16-spezial-deutscher-ta-bis-spezial-geheimcodes` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 16; bündelt 2 frühere Spezialskills (spezial-deutscher-tatbestand-beweis-und-belege, spezial-geheimcodes-schriftsatz-brief-und-memo-bausteine) und bewahrt deren Workflows, Normanker... |
| `kompendium-17-spezial-gruen-behoer-bis-spezial-negative-zah` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 17; bündelt 2 frühere Spezialskills (spezial-gruen-behoerden-gericht-und-registerweg, spezial-negative-zahlen-schwellen-und-berechnung) und bewahrt deren Workflows, Normanker, Prüfp... |
| `kompendium-18-spezial-orange-risik-bis-spezial-schaufenster` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 18; bündelt 2 frühere Spezialskills (spezial-orange-risikoampel-und-gegenargumente, spezial-schaufenster-verhandlung-vergleich-und-eskalation) und bewahrt deren Workflows, Normanker... |
| `kompendium-19-steigerungsadverbien-bis-verbesserungsvorschl` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 19; bündelt 2 frühere Spezialskills (steigerungsadverbien-katalog, verbesserungsvorschlaege-formulieren) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-20-verhaltensbeurteilun-bis-widerspruechliche-be` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 20; bündelt 2 frühere Spezialskills (verhaltensbeurteilung-analyse, widerspruechliche-bewertungen) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-21-zeugnis-problem-sort-bis-zeugnis-ueberblick-e` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 21; bündelt 2 frühere Spezialskills (zeugnis-problem-sortieren, zeugnis-ueberblick-extraktion) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-22-zeugnisart-erkennung-bis-zufriedenheitsformel` | arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 22; bündelt 2 frühere Spezialskills (zeugnisart-erkennung, zufriedenheitsformel-decodierung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-drift-livequellen-und-rechtsprechungscheck` | Drift: Livequellen- und Rechtsprechungscheck im Arbeitszeugnisrecht: fachlich vertiefter Spezialskill mit Normenradar (GewO/BGB/AGG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbar... |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin arbeitszeugnis-analyse: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin arbeitszeugnis-analyse: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin arbeitszeugnis-analyse: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin arbeitszeugnis-analyse: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
