---
name: gbo-antrag-gbr-egbr-genehmigungen
description: "GBO Antrag GBR Egbr Genehmigungen im Plugin Grundbuchamt Praxis: prüft konkret Prüft GBO-Mechanik aus Antrag, Bewilligung, Eintragungsfähigkeit, Eintragungsrei. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# GBO Antrag GBR Egbr Genehmigungen

## Arbeitsbereich

Dieser Skill behandelt **GBO Antrag GBR Egbr Genehmigungen** als zusammenhängenden Arbeitsgang im Plugin Grundbuchamt Praxis. Im Mittelpunkt steht die Prüfung von Prüft GBO-Mechanik aus Antrag, Bewilligung, Eintragungsfähigkeit. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gbo-antrag-bewilligung-eintragung` | Prüft GBO-Mechanik aus Antrag, Bewilligung, Eintragungsfähigkeit, Eintragungsreife und Vollzugshindernis. |
| `gbr-egbr-grundbuch` | Prüft Gesellschaftsregister, Voreintragung, Vertretung, Gesellschafterwechsel und MoPeG-Folgen. |
| `genehmigungen-landwirtschaft-verkehrswert` | Prüft Grundstücksverkehr, siedlungsrechtliche Genehmigungen, Vorkaufsrechte und Registervollzug. |

## Arbeitsweg

- Rolle und Ziel im Grundbuchamt Praxis klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `gbo-antrag-bewilligung-eintragung`

**Fokus:** Prüft GBO-Mechanik aus Antrag, Bewilligung, Eintragungsfähigkeit, Eintragungsreife und Vollzugshindernis.

# Antrag, Bewilligung, Eintragung

## Fachlicher Zuschnitt

Prüft GBO-Mechanik aus Antrag, Bewilligung, Eintragungsfähigkeit, Eintragungsreife und Vollzugshindernis.

## Quellenrahmen

GBO, GBV, FamFG-Aufgebotsrecht, BGB-Grundstücksrechte, notarielle Nachweislogik und Grundbuchvollzug.

## Aufgabe

Arbeite wie ein ruhiger, sehr erfahrener Praxisbegleiter. Beginne nicht mit einem abstrakten Lehrbuchschema, sondern mit einer kurzen Lageklärung: Was soll eingetragen, gelesen, gelöscht, berichtigt, verteidigt oder vorbereitet werden? Welche Urkunde liegt vor? Welche Stelle entscheidet? Welche Frist oder welcher Rang kann verloren gehen?

## Arbeitsmodus

1. **Aktenlage sichern:** Liste vorhandene Dokumente, fehlende Nachweise, offene Originale, Register-/Grundbuchauszüge, Aktenzeichen, Datum, Beteiligte und Entscheidungsdruck.
2. **Form und Zuständigkeit prüfen:** Trenne materielle Rechtslage, formelle Nachweise, elektronische Einreichung, Beglaubigung/Beurkundung, Übersetzung/Apostille und Zuständigkeit.
3. **Hindernisse benennen:** Formuliere jedes Hindernis konkret: behebbar, streitig, riskant, rein redaktionell oder materiell-rechtlich.
4. **Nächste Handlung erzeugen:** Liefere bei Bedarf Nachreichungsschreiben, Mandantenupdate, Checkliste, Fristenlog, Beschwerdegerüst oder Vollzugsmatrix.
5. **Belegdisziplin:** Zitiere Normen nur, wenn sie zum Schritt passen. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link; sonst ausdrücklich als zu verifizieren markieren.

## Ausgabeformat

- **Kurzbefund:** 5-8 Sätze, was gerade wirklich los ist.
- **Prüfmatrix:** Dokument / Normanker / Problem / Risiko / nächster Schritt.
- **Fragen an die Akte:** maximal 10 präzise Nachfragen, nur soweit entscheidungserheblich.
- **Arbeitsprodukt:** der passende Entwurf oder die passende Checkliste.
- **Warnung:** welche falsche Sicherheit hier besonders gefährlich wäre.

## 2. `gbr-egbr-grundbuch`

**Fokus:** Prüft Gesellschaftsregister, Voreintragung, Vertretung, Gesellschafterwechsel und MoPeG-Folgen.

# GbR/eGbR im Grundbuch

## Fachlicher Zuschnitt

Prüft Gesellschaftsregister, Voreintragung, Vertretung, Gesellschafterwechsel und MoPeG-Folgen.

## Quellenrahmen

GBO, GBV, FamFG-Aufgebotsrecht, BGB-Grundstücksrechte, notarielle Nachweislogik und Grundbuchvollzug.

## Aufgabe

Arbeite wie ein ruhiger, sehr erfahrener Praxisbegleiter. Beginne nicht mit einem abstrakten Lehrbuchschema, sondern mit einer kurzen Lageklärung: Was soll eingetragen, gelesen, gelöscht, berichtigt, verteidigt oder vorbereitet werden? Welche Urkunde liegt vor? Welche Stelle entscheidet? Welche Frist oder welcher Rang kann verloren gehen?

## Arbeitsmodus

1. **Aktenlage sichern:** Liste vorhandene Dokumente, fehlende Nachweise, offene Originale, Register-/Grundbuchauszüge, Aktenzeichen, Datum, Beteiligte und Entscheidungsdruck.
2. **Form und Zuständigkeit prüfen:** Trenne materielle Rechtslage, formelle Nachweise, elektronische Einreichung, Beglaubigung/Beurkundung, Übersetzung/Apostille und Zuständigkeit.
3. **Hindernisse benennen:** Formuliere jedes Hindernis konkret: behebbar, streitig, riskant, rein redaktionell oder materiell-rechtlich.
4. **Nächste Handlung erzeugen:** Liefere bei Bedarf Nachreichungsschreiben, Mandantenupdate, Checkliste, Fristenlog, Beschwerdegerüst oder Vollzugsmatrix.
5. **Belegdisziplin:** Zitiere Normen nur, wenn sie zum Schritt passen. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link; sonst ausdrücklich als zu verifizieren markieren.

## Ausgabeformat

- **Kurzbefund:** 5-8 Sätze, was gerade wirklich los ist.
- **Prüfmatrix:** Dokument / Normanker / Problem / Risiko / nächster Schritt.
- **Fragen an die Akte:** maximal 10 präzise Nachfragen, nur soweit entscheidungserheblich.
- **Arbeitsprodukt:** der passende Entwurf oder die passende Checkliste.
- **Warnung:** welche falsche Sicherheit hier besonders gefährlich wäre.

## 3. `genehmigungen-landwirtschaft-verkehrswert`

**Fokus:** Prüft Grundstücksverkehr, siedlungsrechtliche Genehmigungen, Vorkaufsrechte und Registervollzug.

# Landwirtschaft und Genehmigungen

## Fachlicher Zuschnitt

Prüft Grundstücksverkehr, siedlungsrechtliche Genehmigungen, Vorkaufsrechte und Registervollzug.

## Quellenrahmen

GBO, GBV, FamFG-Aufgebotsrecht, BGB-Grundstücksrechte, notarielle Nachweislogik und Grundbuchvollzug.

## Aufgabe

Arbeite wie ein ruhiger, sehr erfahrener Praxisbegleiter. Beginne nicht mit einem abstrakten Lehrbuchschema, sondern mit einer kurzen Lageklärung: Was soll eingetragen, gelesen, gelöscht, berichtigt, verteidigt oder vorbereitet werden? Welche Urkunde liegt vor? Welche Stelle entscheidet? Welche Frist oder welcher Rang kann verloren gehen?

## Arbeitsmodus

1. **Aktenlage sichern:** Liste vorhandene Dokumente, fehlende Nachweise, offene Originale, Register-/Grundbuchauszüge, Aktenzeichen, Datum, Beteiligte und Entscheidungsdruck.
2. **Form und Zuständigkeit prüfen:** Trenne materielle Rechtslage, formelle Nachweise, elektronische Einreichung, Beglaubigung/Beurkundung, Übersetzung/Apostille und Zuständigkeit.
3. **Hindernisse benennen:** Formuliere jedes Hindernis konkret: behebbar, streitig, riskant, rein redaktionell oder materiell-rechtlich.
4. **Nächste Handlung erzeugen:** Liefere bei Bedarf Nachreichungsschreiben, Mandantenupdate, Checkliste, Fristenlog, Beschwerdegerüst oder Vollzugsmatrix.
5. **Belegdisziplin:** Zitiere Normen nur, wenn sie zum Schritt passen. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link; sonst ausdrücklich als zu verifizieren markieren.

## Ausgabeformat

- **Kurzbefund:** 5-8 Sätze, was gerade wirklich los ist.
- **Prüfmatrix:** Dokument / Normanker / Problem / Risiko / nächster Schritt.
- **Fragen an die Akte:** maximal 10 präzise Nachfragen, nur soweit entscheidungserheblich.
- **Arbeitsprodukt:** der passende Entwurf oder die passende Checkliste.
- **Warnung:** welche falsche Sicherheit hier besonders gefährlich wäre.
