---
name: patr-software-pr-einfuehrung
description: "Patr Software PR Einfuehrung im Plugin Patentrecherche: prüft konkret Spezialfall Software- und KI-Patentierbarkeit EPA, Einfuehrung Recherchearten Patent, Bereitet Antwort auf Prüfungsbescheid des DPMA nach § 45. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Patr Software PR Einfuehrung

## Arbeitsbereich

Dieser Skill behandelt **Patr Software PR Einfuehrung** als zusammenhängenden Arbeitsgang im Plugin Patentrecherche. Im Mittelpunkt steht die Prüfung von Spezialfall Software- und KI-Patentierbarkeit EPA, Einfuehrung Recherchearten Patent, Bereitet Antwort auf Prüfungsbescheid des DPMA nach § 45. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `patr-software-ki-patentierbarkeit-spezial` | Spezialfall Software- und KI-Patentierbarkeit EPA: Computer-implementierte Erfindung, technischer Beitrag, KI-spezifische Pruefrichtlinien. Pruefraster fuer Anmeldung. |
| `pr-einfuehrung-recherchearten` | Einfuehrung Recherchearten Patent: Patentierbarkeitsrecherche, Freedom-to-Operate, State-of-the-Art, Familien-, Rechtsstand-, Konkurrenz-Monitoring. Pro Art: Ziel, Datenquellen (Espacenet, DEPATIS, USPTO, JPO, KIPO), Aufwand, Output. Entscheidungsmatrix. |
| `pruefungsbescheid-vorbereiten` | Bereitet Antwort auf Prüfungsbescheid des DPMA nach § 45 PatG oder des EPA nach Art. 94 EPUe systematisch vor. Liest den Bescheid und die zitierten Entgegenhaltungen ein. Strukturiert pro Beanstandung: Beanstandung wortlautgetreu zitiert betroffener Anspruch zitierte Entgegenhaltung mit Pinpoint Argumentationsvorschlag (Neuheit-Argument erfinderische Tätigkeit Argument Anspruchsanpassung). Berücksichtigt EPA-Schemata Problem-Solution-Approach und EPA-Hinweise auf clarity (Art. 84 EPUe) added subject-matter (Art. 123(2) EPUe) und unity (Art. 82 EPUe). Liefert Entwurf der Eingabe mit Argumentationsstruktur und Anspruchssatz-Vorschlaegen. Disclaimer Eingabe muss durch Patentanwaeltin gegengelesen und verantwortet werden. |

## Arbeitsweg

- Rolle und Ziel im Patentrecherche und FTO klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: EPÜ R. 36 Teilanmeldung, PatG § 41 Priorität 12 Monate, USPTO Provisional 12 Monate, EPO Recherchebericht typ. 6 Monate.
- Tragende Normen verifizieren: PatG §§ 1, 3, 4, 9, 10, 139, EPÜ Art. 54, 56, 64, 69, 87 ff., Straßburger IPC-Abkommen, PCT, Espacenet-Datenbankzugriff, DEPATISnet-Bedingungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Patentanmelder, Patentanwalt, DPMA-Prüfer, EPO-Examiner, USPTO, WIPO, Wettbewerber.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Recherchebericht, FTO-Gutachten, Patentlandschaftsanalyse, Espacenet/DEPATISnet/Patentscope/PatFT-Ausdruck, IPC-Klassifikationsbaum — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `patr-software-ki-patentierbarkeit-spezial`

**Fokus:** Spezialfall Software- und KI-Patentierbarkeit EPA: Computer-implementierte Erfindung, technischer Beitrag, KI-spezifische Pruefrichtlinien. Pruefraster fuer Anmeldung.

# PatR: Software KI Patentierbarkeit

## Spezialwissen: PatR: Software KI Patentierbarkeit
- **Spezialgegenstand:** PatR: Software KI Patentierbarkeit / patr software ki patentierbarkeit spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KI, EPA.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `pr-einfuehrung-recherchearten`

**Fokus:** Einfuehrung Recherchearten Patent: Patentierbarkeitsrecherche, Freedom-to-Operate, State-of-the-Art, Familien-, Rechtsstand-, Konkurrenz-Monitoring. Pro Art: Ziel, Datenquellen (Espacenet, DEPATIS, USPTO, JPO, KIPO), Aufwand, Output. Entscheidungsmatrix.

# Patentrecherche: Arten

## Spezialwissen: Patentrecherche: Arten
- **Spezialgegenstand:** Patentrecherche: Arten / pr einfuehrung recherchearten. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DEPATIS, USPTO, JPO, KIPO.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `pruefungsbescheid-vorbereiten`

**Fokus:** Bereitet Antwort auf Prüfungsbescheid des DPMA nach § 45 PatG oder des EPA nach Art. 94 EPUe systematisch vor. Liest den Bescheid und die zitierten Entgegenhaltungen ein. Strukturiert pro Beanstandung: Beanstandung wortlautgetreu zitiert betroffener Anspruch zitierte Entgegenhaltung mit Pinpoint Argumentationsvorschlag (Neuheit-Argument erfinderische Tätigkeit Argument Anspruchsanpassung). Berücksichtigt EPA-Schemata Problem-Solution-Approach und EPA-Hinweise auf clarity (Art. 84 EPUe) added subject-matter (Art. 123(2) EPUe) und unity (Art. 82 EPUe). Liefert Entwurf der Eingabe mit Argumentationsstruktur und Anspruchssatz-Vorschlaegen. Disclaimer Eingabe muss durch Patentanwaeltin gegengelesen und verantwortet werden.

# prüfungsbescheid-vorbereiten

## Zweck

Wenn DPMA oder EPA einen **Prüfungsbescheid** erlässt, muss die Patentanwältin innerhalb der gesetzten Frist (typisch 4 Monate, verlängerbar) antworten. Dieses Skill strukturiert die Antwort.

## Rechtsrahmen

- **§ 45 PatG.** DPMA-Prüfungsbescheid.
- **§ 47 PatG.** Anhörung.
- **Art. 94 Abs. 3 EPÜ + Regel 71(3) EPÜ.** EPA-Prüfungsbescheid.
- **Häufige EPA-Beanstandungen:**
 - **Art. 54 EPÜ** — Neuheit
 - **Art. 56 EPÜ** — Erfinderische Tätigkeit
 - **Art. 84 EPÜ** — Klarheit (clarity) und Stütze in der Beschreibung
 - **Art. 123(2) EPÜ** — Verbot der Erweiterung über den ursprünglichen Offenbarungsgehalt (added subject-matter)
 - **Art. 82 EPÜ** — Einheitlichkeit (unity of invention)
 - **Art. 83 EPÜ** — Ausführbarkeit (sufficiency of disclosure)
 - **Art. 76(1) EPÜ** — bei Teilanmeldungen: keine Erweiterung der Stammanmeldung
- **DPMA-Beanstandungen** sind inhaltlich vergleichbar, formal sparsamer.

## Eingaben

- **Prüfungsbescheid** als PDF / Volltext.
- **Anmeldungsunterlagen** in der eingereichten Fassung (Ansprüche, Beschreibung, Zeichnungen).
- **Zitierte Entgegenhaltungen** (X / Y / A im EPA-Bescheid; D1, D2, … in den EPA-Sprachregeln).
- **Bereits geführte Korrespondenz** (vorheriger Bescheid, vorherige Antwort).
- **Frist** für die Antwort.

## Ablauf

### Schritt 1: Bescheid lesen und strukturieren

Jede Beanstandung als eigene Position erfassen:

```
Beanstandung 1: Art. 54 EPUe / Anspruch 1
 D1 = EP 3 456 789 A1, Siemens AG
 Pinpoint: Anspruch 1, Abs. [0023], Fig. 1
 Argument der Prüfungsabteilung: alle Merkmale von Anspruch 1 sind in D1 offenbart.

Beanstandung 2: Art. 56 EPUe / Anspruch 2
 D1 + D2 (US 2020/0123456)
 Argument: ausgehend von D1 würde der Fachmann mit Anregung aus D2 zur beanspruchten Lösung gelangen.

Beanstandung 3: Art. 84 EPUe / Anspruch 3
 Argument: Merkmal "im Wesentlichen" ist unklar.

Beanstandung 4: Art. 123(2) EPUe / Beschreibung Abs. [0034]
 Argument: Änderung gegenüber urspruenglich eingereichter Fassung unzulässig erweitert.
```

### Schritt 2: Pro Beanstandung Strategie wählen

#### Bei Art. 54 (Neuheit)

- Wenn Pinpoint der Prüfungsabteilung **richtig**: Anspruch beschränken (Merkmale aus der Beschreibung aufnehmen, die in D1 nicht offenbart sind). Über `neuheit-pruefen` neue Merkmalsanalyse machen.
- Wenn Pinpoint **falsch**: argumentieren, dass das Merkmal in D1 nicht offenbart ist. Beleg über Verweis auf den genauen Wortlaut von D1.
- **Auswahlerfindung** ggf. argumentieren (T 198/84, T 279/89), wenn der Anspruch einen Sub-Bereich aus einem in D1 offenbarten Bereich auswählt.

#### Bei Art. 56 (Erfinderische Tätigkeit)

- **Closest Prior Art** der Prüfungsabteilung akzeptieren oder begründet bestreiten.
- **Objektive technische Aufgabe** neu / präziser formulieren (häufig hat die Prüfungsabteilung zu allgemein formuliert).
- **Could-Would** widerlegen: keine Anregung in D1 oder D2, gegen die beanspruchte Lösung gerichtetes Vorurteil, unerwartete Wirkung. Sekundärindizien einsetzen, aber **nicht** als Hauptargument (T 1212/01).
- Wenn Argumente nicht tragen: Anspruch beschränken oder Auxiliary Requests (Hilfsanträge) formulieren.

#### Bei Art. 84 (Klarheit)

- **Unklare Begriffe** definieren oder ersetzen (z. B. "im Wesentlichen" → konkrete Toleranz "±5 %").
- **Stütze in der Beschreibung** zeigen — auf Stellen der Beschreibung verweisen.

#### Bei Art. 123(2) (Added Subject-Matter)

- **Goldstandard** (G 2/10): jede Änderung muss in der ursprünglich eingereichten Anmeldung **unmittelbar und eindeutig** offenbart sein.
- Geänderte Stelle auf ursprünglichen Offenbarungsgehalt zurückführen (Pinpoint auf ursprünglich eingereichten Text).
- Wenn nicht möglich: Änderung zurücknehmen, Anspruch anders formulieren.

#### Bei Art. 82 (Einheitlichkeit)

- Argumentieren, dass die unterschiedlichen Ansprüche durch eine **gemeinsame erfinderische Idee** (single inventive concept) verbunden sind.
- Wenn nicht: **Teilanmeldung** (§ 39 PatG / Art. 76 EPÜ) erwägen, bevor die Stammanmeldung erteilt wird.

#### Bei Art. 83 (Ausführbarkeit)

- Zusätzliche Ausführungsbeispiele in der Beschreibung markieren (keine Erweiterung über Art. 123(2)).
- Falls Erfindung tatsächlich nicht ausführbar offenbart ist: kritisch — Anmeldung möglicherweise nicht haltbar.

### Schritt 3: Anspruchssatz-Vorschläge

- **Hauptantrag** (main request): neue Anspruchsfassung, die alle Beanstandungen ausräumt.
- **Hilfsanträge** (auxiliary requests): in EPA-Praxis empfohlen — gestaffelt enger formulierte Fassungen. Erstes Hilfsantrags-Set: nur leichte Einschränkungen. Zweites Hilfsantrags-Set: enger. Drittes: noch enger.
- **Hilfsanträge dokumentieren**, damit die Patentanwältin sie nur freischalten muss.

### Schritt 4: Entwurf der Eingabe

Aufbau der Eingabe an die Prüfungsabteilung:

```
Sehr geehrte Damen und Herren,

namens und in Vollmacht der Anmelderin nehmen wir zu dem Prüfungsbescheid
vom [Datum] wie folgt Stellung. Beigefuegt sind neue Anspruchsfassungen
(Hauptantrag und Hilfsanträge 1-3).

I. Allgemeines
 [Bezugnahme, Änderungen im Überblick]

II. Zu den einzelnen Beanstandungen

 1. Art. 54 EPUe, Anspruch 1
 [Argument, Pinpoint, ggf. Anspruchsbeschraenkung]

 2. Art. 56 EPUe, Anspruch 1
 Problem-Solution-Approach:
 Closest Prior Art: D1 (EP 3 456 789 A1)
 Objektive technische Aufgabe: [neu / präzisiert]
 Could-Would-Analyse: [Argument]
 Sekundaerindizien: [optional]

 3. Art. 84 EPUe, Anspruch 3
 [Klarstellung, neue Anspruchsfassung]

 4. Art. 123(2) EPUe, Beschreibung Abs. [0034]
 [Änderung zurückgenommen / auf urspruenglichen Offenbarungsgehalt zurückgeführt]

III. Anspruchsfassungen
 Hauptantrag - Ansprueche 1-15
 Hilfsantrag 1 - Ansprueche 1-12
 Hilfsantrag 2 - Ansprueche 1-10
 Hilfsantrag 3 - Ansprueche 1-7

IV. Wir beantragen
 Erteilung des Patents auf Grundlage des Hauptantrags, hilfsweise auf
 Grundlage des jeweils nächsten Hilfsantrags.

Mit freundlichen Grüßen
[Patentanwältin]
```

### Schritt 5: Frist-Tracking

- **EPA:** 4 Monate ab Zustellung. Verlängerung um 2 Monate möglich (Art. 132 EPÜ + R. 132 EPÜ). Versäumte Frist: Weiterbehandlungsantrag (Art. 121 EPÜ), Wiedereinsetzung (Art. 122 EPÜ).
- **DPMA:** Frist nach § 45 PatG, in der Regel 2-4 Monate. Verlängerung möglich.

## Hinweise

- **EPA-typische Argumente:** "No pointer in D1 to D2", "D1 teaches away from the claimed solution", "unexpected technical effect".
- **Hilfsanträge** sollten so formuliert sein, dass sie inhaltlich noch sinnvoll bleiben — keine Überengung, die das Patent wirtschaftlich wertlos macht.
- **Auxiliary Requests** sind im EPA-Verfahren Standard. Im DPMA-Verfahren formal nicht zwingend, aber inhaltlich übernehmbar.
- **Bei Anhörung** (§ 47 PatG / Art. 116 EPÜ): die Eingabe ist die schriftliche Grundlage. Hilfsanträge müssen vorab eingereicht werden.

## Disclaimer

> **Hinweis zum Bescheid.** Dieser Entwurf zur Beantwortung des Prüfungsbescheids ist eine KI-gestützte Vorarbeit. Die Argumentationsstruktur und die Anspruchsentwuerfe müssen durch die Patentanwältin vor Absendung sorgfaeltig gegengelesen werden. Insbesondere die Bewertung der erfinderischen Tätigkeit und die Wahl der Hilfsantragsabstufungen erfordern individuelle Bewertung. Diese Vorbereitung ersetzt nicht die anwaltliche Verantwortung gegenüber Amt und Mandant.

## Triage-Fragen bei Pruefungsbescheid

Bevor die Antwort auf den Pruefungsbescheid formuliert wird, klaere:
1. Welche Einwaende werden geltend gemacht — Neuheit, erfinderische Taetigkeit, mangelnde Klarheit (Art. 84 EPU/§ 34 PatG) oder Offenbarung (Art. 83 EPU/§ 35 PatG)?
2. Laeuft die 4-Monats-EPA-Frist (verlängerbar um 2 Monate) noch, oder ist eine Fristverlängerung erforderlich?
3. Wurden Hilfsantraege vorbereitet (abgestufter Schutzbereich fuer den Fall, dass Hauptantrag nicht haltbar)?
4. Sind alle in der Entgegenhaltung genannten Merkmale korrekt in der Anspruchsanalyse beruecksichtigt?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> **EPA, Erweiterte Beschwerdekammer, G 2/21 (Plausibilitaet):** Die technische Wirkung, auf die eine erfinderische Taetigkeit gestuetzt wird, muss in der Anmeldung plausibel offenbart sein; spaetere Versuchsbelege koennen die Plausibilitaet ersetzen, wenn der Fachmann den Effekt nachtraeglich als glaubhaft bestaetigt ansehen kann.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
