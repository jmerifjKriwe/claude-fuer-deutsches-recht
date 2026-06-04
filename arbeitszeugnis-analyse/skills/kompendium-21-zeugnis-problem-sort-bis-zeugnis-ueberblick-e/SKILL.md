---
name: kompendium-21-zeugnis-problem-sort-bis-zeugnis-ueberblick-e
description: "arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 21; bündelt 2 frühere Spezialskills (zeugnis-problem-sortieren, zeugnis-ueberblick-extraktion) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 21 - arbeitszeugnis-analyse

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `zeugnis-problem-sortieren` | Allgemeiner Startskill fuer Arbeitszeugnisse, wenn der Nutzer nur ein komisches Gefuehl, ein PDF, einen Screenshot oder eine unsortierte Frage hat. Klaert Problem, Zeugnisart, Ziel, Frist, Kontext, Belege und naechsten Arbeitsweg. |
| `zeugnis-ueberblick-extraktion` | Extrahiert Kopfdaten aus deutschen Arbeitszeugnissen für Mandatsanlage und Analysestart. Anwendungsfall Zeugnis wurde hochgeladen und Basisdaten sollen für Akte und Analyse erfasst werden. Normen § 109 GewO Pflichtinhalt § 16 BBiG Ausbildungszeugnis. Prüfraster Arbeitgeber Arbeitnehmer Beschaeftigungszeitraum Position Ausstellungsdatum Unterschriftsberechtigte Vollständigkeit. Output Strukturiertes Kopfdatenblatt mit Vollständigkeitsprüfung und Zeugnisart-Einordnung als Eingabe für alle Folge-Analyse-Skills. Abgrenzung zu zeugnisart-erkennung und notenrelevante-saetze-identifizieren. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `zeugnis-problem-sortieren`

**Frühere Beschreibung:** Allgemeiner Startskill fuer Arbeitszeugnisse, wenn der Nutzer nur ein komisches Gefuehl, ein PDF, einen Screenshot oder eine unsortierte Frage hat. Klaert Problem, Zeugnisart, Ziel, Frist, Kontext, Belege und naechsten Arbeitsweg.

# Zeugnisproblem Sortieren

## V90 Fachkern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Zeugnisproblem Sortieren` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Dieser Skill ist der Einstieg, wenn noch nicht klar ist, ob das Zeugnis schlecht ist, nur kuehl klingt, taktisch nachverhandelt werden soll oder rechtlich angegriffen werden muss.

## Vier Pflichtbausteine

1. Ziel klaeren: Was soll entschieden, geprueft, entworfen, verbessert oder verhandelt werden?
2. Kontext sichern: Rolle, Frist, Dokumente, Beteiligte, Vorgeschichte und Belege.
3. Grenzen setzen: keine Blindzitate, keine erfundenen Tatsachen, keine ungewollten Zugestaendnisse.
4. Ausgabeformat bestimmen: Memo, Tabelle, Schriftsatz, Brief, Beschluss, TOP, Checkliste oder Red-Team-Liste.

## Zeugnis-spezifische Ersttriage (vor jeder Detailprüfung)

- **Anspruchsgrundlage:** § 109 GewO (qualifiziertes wohlwollendes Zeugnis), für Arbeiter zusätzlich § 630 BGB.
- **Notenstufen-Matrix nach BAG ständiger Rechtsprechung:**
  - Note 1: "stets zur vollsten Zufriedenheit"
  - Note 2: "stets zur vollen Zufriedenheit"
  - Note 3: "zur vollen Zufriedenheit" (ohne "stets")
  - Note 4: "zur Zufriedenheit" / "war stets bemüht"
  - Note 5: "im Wesentlichen / im Großen und Ganzen zur Zufriedenheit"
- **Wahrheit und Wohlwollen:** § 109 Abs. 2 GewO (kein Geheimcode, keine Doppeldeutigkeit). Beweislast: bis Note 3 trägt **Arbeitnehmer** die Beweislast für bessere Note; ab Note 4 (befriedigend) trägt **Arbeitgeber** die Beweislast für die schlechtere Beurteilung (BAG ständige Rechtsprechung).
- **Geheimcode-Warnsignale:** "bemüht", "im Wesentlichen", fehlende Steigerungen, falsche Reihenfolge ("Kollegen und Vorgesetzte" statt "Vorgesetzten, Kollegen"), kühle Schlussformel ohne Bedauern/Dank/Erfolgswünsche, Auslassung relevanter Aufgabenbereiche.
- **Fristen:** Verfall des Zeugnisanspruchs nach Verwirkung (ca. 10 Monate nach Beendigung, abhängig vom Einzelfall) und ggf. tarifvertragliche Ausschlussfristen.

## Trade-off-Hinweis

Bei Note 3 versus Note 2 trägt der Arbeitnehmer die Beweislast. Wer auf "stets zur vollen Zufriedenheit" klagt ohne Beurteilungsbeiträge, Beurteilungsbögen oder Zeugen, verliert prozessual. Lieber **Vergleichsweise** in der Güteverhandlung: Note 2 plus warme Schlussformel als Standardpaket.

## Workflow

1. Material erfassen und sichtbar zwischen Tatsache, Behauptung und Bewertung trennen.
2. Eilige Punkte vorziehen (Verwirkung, tarifvertragliche Ausschlussfristen).
3. Schwachstellen und Gegenargumente benennen (Beweislage, Beurteilungsbeiträge).
4. Passende Folge-Skills aus demselben Plugin vorschlagen.
5. Einen verwendbaren Output liefern und offene Punkte mit `[noch klaeren]` markieren.

## Ausgabe

| Punkt | Befund | Risiko | Naechster Schritt |
| --- | --- | --- | --- |
| ... | ... | ... | ... |

## Qualitaetsgate

Ist die Antwort handlungsorientiert, knapp, respektvoll, belegnah und ohne erfundene Quellen? Sind Fristen und offene Tatsachen sichtbar? Ist der naechste Schritt eindeutig?


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `zeugnis-ueberblick-extraktion`

**Frühere Beschreibung:** Extrahiert Kopfdaten aus deutschen Arbeitszeugnissen für Mandatsanlage und Analysestart. Anwendungsfall Zeugnis wurde hochgeladen und Basisdaten sollen für Akte und Analyse erfasst werden. Normen § 109 GewO Pflichtinhalt § 16 BBiG Ausbildungszeugnis. Prüfraster Arbeitgeber Arbeitnehmer Beschaeftigungszeitraum Position Ausstellungsdatum Unterschriftsberechtigte Vollständigkeit. Output Strukturiertes Kopfdatenblatt mit Vollständigkeitsprüfung und Zeugnisart-Einordnung als Eingabe für alle Folge-Analyse-Skills. Abgrenzung zu zeugnisart-erkennung und notenrelevante-saetze-identifizieren.

# Zeugnis-Überblick und Kopfdaten-Extraktion

## V90 Fachkern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Zeugnis-Überblick und Kopfdaten-Extraktion` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


Dieser Skill liest ein deutsches Arbeitszeugnis und extrahiert systematisch alle Kopfdaten, bevor die inhaltliche Analyse beginnt. Vollständige Kopfdaten sind Voraussetzung für jede weitere Bewertung, da fehlende Angaben bereits eigenständige Hinweise auf die Qualität des Zeugnisses liefern können.

Ein qualifiziertes Zeugnis nach § 109 Abs. 1 Satz 3 GewO muss Angaben zu Art und Dauer der Tätigkeit sowie zu Leistung und Verhalten enthalten. Das einfache Zeugnis beschränkt sich auf Art und Dauer. Die Unterscheidung ist für die Erwartungshaltung an die Formulierungen entscheidend: Bei einem einfachen Zeugnis fehlt die Leistungsbeurteilung bewusst und ist kein negativer Hinweis.

Beim Aussteller ist zu prüfen, ob die Firma korrekt bezeichnet ist, ob ein Briefkopf vorhanden ist und ob Ort und Datum plausibel sind. Das Datum des Zeugnisses darf nicht vor dem letzten Arbeitstag liegen (bei Endzeugnis). Bei Zwischenzeugnissen wird kein Enddatum angegeben — die fehlende Angabe ist kein Fehler.

Die Unterschrift muss von einer zeichnungsberechtigten Person stammen. In der Regel sind das Geschäftsführer, Personalabteilungsleiter oder bevollmächtigte HR-Manager. Eine Unterschrift durch einen hierarchisch tiefer stehenden Mitarbeiter als den beurteilten Arbeitnehmer ist ein rotes Signal. Fehlt die Unterschrift ganz oder ist sie unleserlich ohne Namensangabe, kann das Zeugnis anfechtbar sein.

## Geheimcode-Regeln

| Merkmal | Bedeutung | Ampel |
|---|---|---|
| Unterschrift rangniederer Person | Verdeckte Abwertung der Stellung | Rot |
| Kein Briefkopf / kein Stempel | Formfehler, möglicherweise anfechtbar | Orange |
| Datum weit nach Austritt | Zeigt Widerstand oder Nachlässigkeit | Orange |
| Vollständige Angaben, ranghöhere Unterschrift | Erwartungskonformes Zeugnis | Grün |
| Beschäftigungszeitraum weicht von Vertrag ab | Klärungsbedarf | Orange |

## Beispiele

**Beispiel 1 – Vollständige Kopfdaten (Grün):** "Frau Sabine Müller, geboren am 12. März 1985, war vom 1. April 2018 bis zum 31. März 2024 in unserem Unternehmen als Abteilungsleiterin Marketing tätig." — Alle Pflichtangaben vorhanden.

**Beispiel 2 – Fehlende Positionsangabe (Orange):** "Herr Thomas Braun war von 2019 bis 2023 bei uns beschäftigt." — Keine Positionsbezeichnung, kein vollständiges Datum.

**Beispiel 3 – Unterschrift Sachbearbeiter (Rot):** Unterschrift eines HR-Sachbearbeiters für einen ausscheidenden Abteilungsleiter — hierarchisches Missverhältnis signalisiert Abwertung.

**Beispiel 4 – Datum vor Austritt (Orange):** Ausstellungsdatum liegt drei Monate vor dem angegebenen letzten Arbeitstag — formale Unstimmigkeit.

**Beispiel 5 – Zwischenzeugnis ohne Enddatum (Grün):** Kein Enddatum bei einem als Zwischenzeugnis bezeichneten Dokument — korrekt und unauffällig.

## Ausgabeformat

Der Skill gibt eine strukturierte Übersichtstabelle aus mit den Feldern: Arbeitgeber (Name, Rechtsform, Ort), Arbeitnehmer (Name, ggf. Geburtsdatum), Beschäftigungszeitraum (Von–Bis oder "Zwischenzeugnis"), Position/Tätigkeit, Ausstellungsdatum, Unterschriftsberechtigte(r) (Name, Titel), Zeugnisart (einfach/qualifiziert/Zwischen-/Endzeugnis). Unter der Tabelle folgt ein Hinweis auf erkannte Vollständigkeitsmängel.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
