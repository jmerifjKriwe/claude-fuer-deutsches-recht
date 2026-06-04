---
name: kompendium-12-notenrelevante-saetz-bis-orange-flaggen-katal
description: "arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 12; bündelt 2 frühere Spezialskills (notenrelevante-saetze-identifizieren, orange-flaggen-katalog) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 12 - arbeitszeugnis-analyse

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `notenrelevante-saetze-identifizieren` | Identifiziert notenrelevante Saetze im Arbeitszeugnis und trennt sie von neutralen Aufgabenbeschreibungen. Anwendungsfall Zeugnis liegt vor und muss für Ampelanalyse vorbereitet werden. Normen § 109 GewO Inhalte eines qualifizierten Zeugnisses BAG-Anforderungen an Vollständigkeit. Kategorisierung Aufgabenbeschreibung Leistungsbeurteilung Verhaltensbeurteilung Schlussformel. Output Kategorisierte Satzliste als Eingabe für satzweise-notenmatrix und Bereichs-Drift-Detektor. Abgrenzung zu zeugnis-ueberblick-extraktion (Kopfdaten) und zeugnisart-erkennung. |
| `orange-flaggen-katalog` | Katalog schwacher positiver Formulierungen im Arbeitszeugnis, die auf Note 3 hindeuten. Umfasst alle Orange-Signale: fehlende Steigerungsadverbien, eingeschränkte Lobesformeln und strukturelle Abschwächungen mit Notentendenz Note 3. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `notenrelevante-saetze-identifizieren`

**Frühere Beschreibung:** Identifiziert notenrelevante Saetze im Arbeitszeugnis und trennt sie von neutralen Aufgabenbeschreibungen. Anwendungsfall Zeugnis liegt vor und muss für Ampelanalyse vorbereitet werden. Normen § 109 GewO Inhalte eines qualifizierten Zeugnisses BAG-Anforderungen an Vollständigkeit. Kategorisierung Aufgabenbeschreibung Leistungsbeurteilung Verhaltensbeurteilung Schlussformel. Output Kategorisierte Satzliste als Eingabe für satzweise-notenmatrix und Bereichs-Drift-Detektor. Abgrenzung zu zeugnis-ueberblick-extraktion (Kopfdaten) und zeugnisart-erkennung.

# Notenrelevante Sätze identifizieren

## V90 Fachkern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Notenrelevante Sätze identifizieren` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


Nicht jeder Satz in einem Arbeitszeugnis ist für die Benotung relevant. Die Aufgabenbeschreibung — also die Schilderung dessen, womit der Arbeitnehmer befasst war — enthält keine Bewertung und ist für die Notenbildung neutral. Erst wenn ein Satz eine Aussage über die Qualität der Aufgabenerfüllung trifft, wird er notenrelevant.

Die vier Hauptkategorien sind: (1) Aufgabenbeschreibung (neutral, deskriptiv), (2) Leistungsbeurteilung (Arbeitsqualität, Arbeitsbereitschaft, Arbeitstempo, Arbeitsmenge, Fachkenntnisse), (3) Verhaltensbeurteilung (soziales Verhalten zu Vorgesetzten, Kollegen, Kunden, Lieferanten) und (4) Schlussformel (Bedauern, Dank, Zukunftswünsche). Leistungs- und Verhaltenssätze sind regelmäßig notenrelevant. Die Schlussformel wird als Signal bewertet, rechtlich aber gesondert behandelt.

Ein besonderer Grenzfall ist die verkürzte Aufgabenbeschreibung: Wenn ein Zeugnis die Aufgaben sehr kurz beschreibt und damit signalisiert, dass der Arbeitnehmer nur geringe Verantwortung hatte — obwohl seine tatsächliche Stellung höher war — kann das ein implizites Abwertungssignal sein. Ebenso ist eine übertrieben lange Aufgabenbeschreibung bei gleichzeitig knapper Leistungsbeurteilung ein Hinweis darauf, dass der Aussteller das Positive bewusst minimiert.

Besondere Aufmerksamkeit verdienen Sätze, die scheinbar deskriptiv sind, aber Bewertungen einschließen. "Er war stets bereit, Überstunden zu leisten" klingt nach Beschreibung, ist aber eine Leistungsaussage über Einsatzbereitschaft. "Sie bearbeitete sämtliche Aufgaben eigenverantwortlich" beschreibt Arbeitsweise und ist eine verdeckte Leistungsbeurteilung.

## Geheimcode-Regeln

| Satztyp | Notenrelevant? | Ampel-Analyse |
|---|---|---|
| Aufgabenbeschreibung (rein deskriptiv) | Nein | Keine Ampelzuordnung |
| Leistungsaussage mit Qualitätsmerkmal | Ja | Ampel nach Formulierung |
| Verhaltensaussage zu Dritten | Ja | Ampel nach Formulierung und Reihenfolge |
| Schlussformel (Dank, Bedauern, Wünsche) | Signalrelevant | Ampel nach Ton; Anspruch gesondert prüfen |
| Satz mit impliziter Bewertung | Ja | Ampel nach Gesamttendenz |
| Kurze Aufgabenbeschreibung trotz hoher Stellung | Grenzfall | Orange |

## Beispiele

**Beispiel 1 – Rein deskriptiv (nicht notenrelevant):** "Frau Weber war in unserem Haus als Projektmanagerin tätig und verantwortete die Koordination externer Dienstleister." — Keine Qualitätsaussage.

**Beispiel 2 – Leistungsbeurteilung (notenrelevant):** "Sie erledigte alle ihr übertragenen Aufgaben stets zu unserer vollsten Zufriedenheit." — Kernbeurteilungssatz, Note 1, Grün.

**Beispiel 3 – Verhaltensbeurteilung (notenrelevant):** "Ihr Verhalten gegenüber Vorgesetzten und Kollegen war einwandfrei." — Reihenfolge und Qualifikationswort bestimmen Ampelfarbe.

**Beispiel 4 – Implizite Bewertung (notenrelevant):** "Herr Schmidt war stets bemüht, seine Aufgaben pünktlich abzuliefern." — Scheinbar positiv, tatsächlich rotes Signal durch "bemüht".

**Beispiel 5 – Schlussformel (signalrelevant):** Fehlen des Bedauerns über das Ausscheiden — mögliches Distanzsignal trotz positiver Leistungsformulierungen; rechtlich nicht automatisch einklagbar.

## Ausgabeformat

Jeder Satz des Zeugnisses wird in einer Tabelle klassifiziert: Satz (Kurzform) | Kategorie (Aufgabe/Leistung/Verhalten/Schluss) | Notenrelevant (Ja/Nein) | Weitergeleitet an Skill (z. B. leistungsbeurteilung-analyse). Notenrelevante Sätze werden im Anschluss an die zuständigen Analyse-Skills weitergegeben.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 2. `orange-flaggen-katalog`

**Frühere Beschreibung:** Katalog schwacher positiver Formulierungen im Arbeitszeugnis, die auf Note 3 hindeuten. Umfasst alle Orange-Signale: fehlende Steigerungsadverbien, eingeschränkte Lobesformeln und strukturelle Abschwächungen mit Notentendenz Note 3.

# Orange-Flaggen-Katalog

## V90 Fachkern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Orange-Flaggen-Katalog` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


Orange Flaggen sind Formulierungen, die zwar positiv klingen, aber deutlich unterhalb der Spitzennote liegen. Sie deuten auf eine befriedigende bis ausreichende Leistung hin — also Note 3, in manchen Kontexten auch Note 3 zu 4. Orange Signale sind besonders wichtig zu erkennen, weil sie bei flüchtiger Lektüre als gut erscheinen, in der Praxis aber eine mittelmäßige Beurteilung darstellen.

Das zentrale Merkmal oranger Formulierungen ist das Fehlen von Steigerungsadverbien: "zur vollen Zufriedenheit" (ohne "stets") ist Orange; "gute Fachkenntnisse" (ohne "sehr gute" oder "hervorragende") ist Orange; "engagiert" (ohne "stets" oder "außerordentlich") ist Orange. Das Muster ist stets gleich: Die positive Grundaussage ist vorhanden, aber die Steigerung fehlt.

Weitere orange Signale entstehen durch einschränkende Adverbien, die die Leistung relativieren: "überwiegend", "in der Regel", "im Allgemeinen" oder "meistens". Diese Wörter klingen nach einer Erläuterung, sind aber in der Zeugnispraxis als Einschränkungen kodiert, die eine Note-3-Beurteilung markieren.

Orange Signale treten auch strukturell auf: Ein Zeugnis, das alle Bausteine enthält, aber keinen einzigen Superlativ und kein einziges "stets" verwendet, ist in seiner Gesamtheit orange — eine befriedigende Gesamtbeurteilung ohne herausragende Einzelaspekte.

## Geheimcode-Regeln

| Orange-Flagge-Formulierung | Bedeutung | Notentendenz |
|---|---|---|
| "zur vollen Zufriedenheit" (ohne "stets") | Note 3 | Orange |
| "gute Auffassungsgabe" (ohne Steigerung) | Befriedigende Intelligenz | Orange |
| "engagiert" (ohne Adverb) | Mäßiges Engagement | Orange |
| "überwiegend ordnungsgemäß" | Einschränkung auf Note 3 | Orange |
| "in der Regel zuverlässig" | Gelegentliche Unzuverlässigkeit | Orange |
| "hat sich in das Team integriert" | Keine besonderen sozialen Stärken | Orange |
| Schlussformel nur aus Dank + Wunsch | Fehlendes Bedauern; Signal, kein automatischer Anspruch | Orange |
| "war mit seinen Aufgaben vertraut" | Keine besondere Expertise | Orange |
| "hat die übertragenen Aufgaben erfüllt" | Minimum ohne Übererfüllung | Orange |

## Beispiele

**Beispiel 1 – Klassisches "zur vollen Zufriedenheit":** "Frau Peters erfüllte ihre Aufgaben stets zur vollen Zufriedenheit." — "Vollen" ohne "vollsten" → Note 2. Ohne "stets": "zur vollen Zufriedenheit" → Note 3, Orange.

**Beispiel 2 – Fehlende Steigerung bei Fachkenntnissen:** "Herr Zimmer verfügt über gute Fachkenntnisse, die er in seiner täglichen Arbeit einsetzte." — "Gut" ohne "sehr gut" oder "hervorragend" → Orange.

**Beispiel 3 – Einschränkungsadverb:** "Sie erledigte ihre Aufgaben überwiegend selbstständig und termingerecht." — "Überwiegend" als Einschränkung → Orange, Note 3.

**Beispiel 4 – Orange Schlussformel:** "Wir danken Herrn König für seine Mitarbeit und wünschen ihm für die Zukunft alles Gute." — Vorhanden: Dank und Wunsch. Fehlend: Bedauern. Das ist kühl bis mittelwertig, aber als Anspruch nur mit Einzelfallkontext zu führen.

**Beispiel 5 – Integration statt Teamstärke:** "Frau Bauer hat sich gut in unser Team integriert und war kollegial." — Integration als passive Formulierung statt aktiver Teamstärke → Orange.

## Ausgabeformat

Der Skill listet alle orange Signale mit Zitat, Signaltyp (fehlende Steigerung/Einschränkungsadverb/strukturelle Abschwächung) und Notentendenz. Er gibt außerdem an, welche Formulierung stattdessen eine grüne Bewertung ergeben hätte.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
