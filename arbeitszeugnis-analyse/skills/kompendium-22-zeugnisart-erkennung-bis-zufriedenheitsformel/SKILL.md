---
name: kompendium-22-zeugnisart-erkennung-bis-zufriedenheitsformel
description: "arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 22; bündelt 2 frühere Spezialskills (zeugnisart-erkennung, zufriedenheitsformel-decodierung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 22 - arbeitszeugnis-analyse

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `zeugnisart-erkennung` | Unterscheidet qualifiziertes Endzeugnis einfaches Zeugnis Zwischenzeugnis und Ausbildungszeugnis am Beginn jeder Analyse. Anwendungsfall Zeugnis liegt vor und muss bevor Analyse startet der richtigen Zeugnisart zugeordnet werden. Normen § 109 GewO qualifiziertes vs. einfaches Zeugnis § 16 BBiG Ausbildungszeugnis. Prüfraster Inhalt Zeitbezug Position Stichtag Ausstellungsanlass. Output Zeugnisart-Klassifikation mit Erlauterungen zu Inhalt Erwartungshaltung und Interpretationsrahmen für alle Folge-Skills. Abgrenzung zu zeugnis-ueberblick-extraktion (Kopfdaten) und notenrelevante-saetze-identifizieren. |
| `zufriedenheitsformel-decodierung` | Decodiert die fünfstufige Zufriedenheitsformel deutscher Arbeitszeugnisse: von Note 1 bis Note 5. Tabellarische Ampelzuordnung aller Standardformulierungen mit Erklärung der sprachlichen Feinheiten und ihrer rechtlichen Bedeutung. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `zeugnisart-erkennung`

**Frühere Beschreibung:** Unterscheidet qualifiziertes Endzeugnis einfaches Zeugnis Zwischenzeugnis und Ausbildungszeugnis am Beginn jeder Analyse. Anwendungsfall Zeugnis liegt vor und muss bevor Analyse startet der richtigen Zeugnisart zugeordnet werden. Normen § 109 GewO qualifiziertes vs. einfaches Zeugnis § 16 BBiG Ausbildungszeugnis. Prüfraster Inhalt Zeitbezug Position Stichtag Ausstellungsanlass. Output Zeugnisart-Klassifikation mit Erlauterungen zu Inhalt Erwartungshaltung und Interpretationsrahmen für alle Folge-Skills. Abgrenzung zu zeugnis-ueberblick-extraktion (Kopfdaten) und notenrelevante-saetze-identifizieren.

# Zeugnisart-Erkennung

## V90 Fachkern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Zeugnisart-Erkennung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


Die Art des Zeugnisses bestimmt grundlegend, welche Formulierungen erwartet werden, welche Aussagen fehlen dürfen und wie Auslassungen zu interpretieren sind. Ein einfaches Zeugnis enthält per Definition keine Leistungsbeurteilung — das Fehlen dieser Passage ist kein negatives Signal. Ein qualifiziertes Zeugnis hingegen muss Leistung und Verhalten beurteilen; fehlt eine dieser Komponenten, ist das auffällig.

Das Zwischenzeugnis wird ausgestellt, während das Arbeitsverhältnis noch besteht — etwa bei Vorgesetztenwechsel, Versetzung, Elternzeit oder auf ausdrücklichen Wunsch. Es enthält kein Enddatum und keine Schlussformel mit Verabschiedung. Die Formulierungen sind typischerweise im Präsens oder im Perfekt gehalten. Fehlt bei einem Zwischenzeugnis die Zukunftswunschformel, ist das kein Fehler; einige Zeugnisersteller fügen gleichwohl Formulierungen wie "Wir wünschen ihr weiterhin viel Erfolg" ein.

Das Ausbildungszeugnis beurteilt Auszubildende nach BBiG (§ 16 BBiG). Es enthält besondere Abschnitte zu Lernfortschritten, Verhalten im Ausbildungsbetrieb und in der Berufsschule sowie zur praktischen Ausbildungsleistung. Der Bewertungsrahmen ist eigenständig und nicht mit dem von Arbeitnehmer-Zeugnissen identisch.

Führungskräfte-Zeugnisse (leitende Angestellte) haben zusätzliche Erwartungen an Abschnitte zur Mitarbeiterführung, strategischen Verantwortung und Repräsentation des Unternehmens. Fehlen diese Abschnitte bei einer Führungskraft, ist das ein orangefarbenes oder rotes Signal.

## Geheimcode-Regeln

| Zeugnisart | Mindest- und Erwartungsbausteine | Fehlende Bausteine |
|---|---|---|
| Einfaches Zeugnis | Art und Dauer der Tätigkeit | Keine Leistungsaussage erwartet |
| Qualifiziertes Endzeugnis | Art, Dauer, Leistung, Verhalten, Schlussformel | Rotes Signal |
| Zwischenzeugnis | Art, Dauer, Leistung, Verhalten (Präsens) | Kein Enddatum, keine Verabschiedung OK |
| Ausbildungszeugnis | Lernleistung, Berufsschule, Verhalten, Praxis | Nach BBiG-Maßstab |
| Führungskraft (qualifiziert) | Plus Führung, Strategie, Repräsentation | Fehlen = Orange/Rot |

## Beispiele

**Beispiel 1 – Korrekte Zeugnisart-Erkennung:** "Wir stellen dieses Zeugnis auf eigenen Wunsch aus" + kein Enddatum → Zwischenzeugnis auf Wunsch des Arbeitnehmers.

**Beispiel 2 – Einfaches Zeugnis korrekt interpretiert:** Zeugnis ohne jede Leistungsbeurteilung und ohne Verhaltensabschnitt, aber mit explizitem Hinweis "einfaches Zeugnis" oder keine Bewertungsformulierungen — nicht als Abwertung zu lesen.

**Beispiel 3 – Fehlendes Verhalten bei Endzeugnis (Orange):** Qualifiziertes Zeugnis mit Leistungsbeurteilung, aber ohne Verhaltensabschnitt gegenüber Kollegen/Kunden — Auslassung ist auffällig.

**Beispiel 4 – Ausbildungszeugnis ohne Berufsschulangabe (Orange):** Bei einem BBiG-Zeugnis fehlt die Beurteilung des schulischen Teils komplett, obwohl Schule und Betrieb im Sachverhalt eine tragende Rolle spielen — erwarteter Baustein fehlt.

## Ausgabeformat

Der Skill gibt zunächst die erkannte Zeugnisart aus (mit Begründung) und listet dann die erwarteten Bausteine mit dem Status "vorhanden / fehlend / unerwartet". Auf dieser Basis justiert er den Interpretationsrahmen für alle nachgelagerten Analyse-Skills.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 2. `zufriedenheitsformel-decodierung`

**Frühere Beschreibung:** Decodiert die fünfstufige Zufriedenheitsformel deutscher Arbeitszeugnisse: von Note 1 bis Note 5. Tabellarische Ampelzuordnung aller Standardformulierungen mit Erklärung der sprachlichen Feinheiten und ihrer rechtlichen Bedeutung.

# Zufriedenheitsformel-Decodierung

## V90 Fachkern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Zufriedenheitsformel-Decodierung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


Die Zufriedenheitsformel ist das Herzstück des deutschen Arbeitszeugnisses. Sie ist die am häufigsten verwendete und am stärksten kodierte Formulierung — und für Laien oft kaum von einer guten Note zu unterscheiden. Vier Worte können den Unterschied zwischen einer Eins und einer Vier ausmachen.

Die fünfstufige Skala folgt einem präzisen Steigerungssystem, das auf den Wörtern "stets" (immer, ohne Ausnahme), "vollsten" (Superlativ) und "vollen" (Positiv) beruht. Jede Stufe unterscheidet sich von der nächsten durch das Fehlen eines Wortes oder dessen Abschwächung. Wer diese Abstufungen nicht kennt, liest eine Note-4-Formulierung als positiv — genau das ist der Geheimcode der Zeugnissprache.

Wichtig: Die Formel erscheint selten isoliert. Sie ist oft Teil eines längeren Satzes, der auch Arbeitsbereitschaft und Fachkenntnisse umfasst. Der Gesamtsatz ist nach seiner schwächsten Komponente zu beurteilen. "Ihre Fachkenntnisse und ihre stets überzeugende Arbeitsweise überzeugten uns; die Ergebnisse entsprachen unseren Erwartungen" — die schwache Schlusskomponente zieht die Note herunter.

Verstärker und Abschwächer können die Grundformel verändern: Adverbien wie "jederzeit", "durchweg" oder "in jeder Hinsicht" können als positive Verstärker wirken. Einschränkungen wie "im Wesentlichen", "in aller Regel" oder "soweit beurteilt werden konnte" schwächen die Formel deutlich ab.

## Geheimcode-Regeln

| Formel | Note | Ampel |
|---|---|---|
| "stets zur vollsten Zufriedenheit" | Note 1 | Grün |
| "stets zur vollen Zufriedenheit" | Note 2 | Grün |
| "zur vollen Zufriedenheit" | Note 3 | Orange |
| "zur Zufriedenheit" | Note 4 | Rot |
| "im Großen und Ganzen zur Zufriedenheit" | Note 5 | Rot |
| "hat unsere Erwartungen erfüllt" | Note 4 (Ersatzformel) | Rot |
| "stets zu unserer vollsten und uneingeschränkten Zufriedenheit" | Note 1 (verstärkt) | Grün |
| "zur vollen Zufriedenheit, soweit beurteilt werden konnte" | Note 3-4 abgeschwächt | Rot |

## Beispiele

**Beispiel 1 – Note 1 (Grün):** "Frau Schäfer erledigte alle ihr übertragenen Aufgaben stets zu unserer vollsten Zufriedenheit." — Vollständige Maximalformel, keine Einschränkungen.

**Beispiel 2 – Note 2 (Grün):** "Die ihr anvertrauten Aufgaben erledigte sie stets zu unserer vollen Zufriedenheit." — Fehlt "vollsten", aber "stets" bleibt erhalten, daher Note 2.

**Beispiel 3 – Note 3 (Orange):** "Herr Bergmann erfüllte seine Aufgaben zur vollen Zufriedenheit." — Kein "stets" → Abschwächung auf Note 3.

**Beispiel 4 – Note 4 (Rot):** "Herr Fischer erledigte seine Aufgaben zur Zufriedenheit." — Weder "stets" noch "vollsten" → Note 4.

**Beispiel 5 – Note 5 (Rot):** "Sie hat ihre Aufgaben im Großen und Ganzen zu unserer Zufriedenheit erledigt." — Einschränkung durch "im Großen und Ganzen" → Note 5.

## Ausgabeformat

Der Skill gibt die erkannte Formel im Wortlaut aus, ordnet sie der Note zu (Note 1 bis Note 5), zeigt die Ampelfarbe und erklärt das entscheidende sprachliche Merkmal. Bei mehreren Zufriedenheitsformeln im Zeugnis (Leistung und Verhalten getrennt) werden beide separat ausgewiesen.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
