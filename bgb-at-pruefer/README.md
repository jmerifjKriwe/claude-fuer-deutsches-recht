# BGB AT Prüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`bgb-at-pruefer`) | [`bgb-at-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bgb-at-pruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Anfechtung / Irrtum — Restaurant-Kette Pohlmann-Ofenkaess, Erbenstraße Leipzig** (`anfechtung-irrtum-restaurant-kette-pohlmann-erbenstrasse-leipzig`) | [Gesamt-PDF lesen](../testakten/anfechtung-irrtum-restaurant-kette-pohlmann-erbenstrasse-leipzig/gesamt-pdf/anfechtung-irrtum-restaurant-kette-pohlmann-erbenstrasse-leipzig_gesamt.pdf) | [`testakte-anfechtung-irrtum-restaurant-kette-pohlmann-erbenstrasse-leipzig.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-anfechtung-irrtum-restaurant-kette-pohlmann-erbenstrasse-leipzig.zip) |
| **Akte BGB AT: Altfränkische Werkstatt** (`bgb-at-altfraenkische-werkstatt`) | [Gesamt-PDF lesen](../testakten/bgb-at-altfraenkische-werkstatt/gesamt-pdf/bgb-at-altfraenkische-werkstatt_gesamt.pdf) | [`testakte-bgb-at-altfraenkische-werkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bgb-at-altfraenkische-werkstatt.zip) |
| **BGB BT — Holzofen, Lieferkette, Bürgschaft, GoA und Brandschaden** (`bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt`) | [Gesamt-PDF lesen](../testakten/bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt/gesamt-pdf/bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt_gesamt.pdf) | [`testakte-bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt.zip) |
| **BGB BT — Smart-Kühlschrank, digitale Elemente und Reparaturblockade** (`bgb-bt-smart-kuehlschrank-digital-repair-koeln`) | [Gesamt-PDF lesen](../testakten/bgb-bt-smart-kuehlschrank-digital-repair-koeln/gesamt-pdf/bgb-bt-smart-kuehlschrank-digital-repair-koeln_gesamt.pdf) | [`testakte-bgb-bt-smart-kuehlschrank-digital-repair-koeln.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bgb-bt-smart-kuehlschrank-digital-repair-koeln.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **BGB AT: Altfränkische Werkstatt** ([`testakten/bgb-at-altfraenkische-werkstatt/`](../testakten/bgb-at-altfraenkische-werkstatt/)).

Direkt-Download als ZIP: [testakte-bgb-at-altfraenkische-werkstatt.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bgb-at-altfraenkische-werkstatt.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

Großes Prüfplugin zum BGB Allgemeiner Teil. Es führt durch Vertragsschluss, Willenserklärungen, Zugang, Auslegung, Geschäftsfähigkeit, Form, Nichtigkeit, Anfechtung, Stellvertretung, Bedingungen, Fristen und Verjährung. Der Formteil ist mit qES, beA, § 130e ZPO und § 46h ArbGG verschaltet. Neu verschaltet sind digitale Elemente, Updatehinweise, App-/Portalzugang, Reparaturverlangen und Right-to-Repair-Fragen als allgemeinzivilrechtlicher Router in BGB-BT, AGB-Recht und Produktrecht. Ziel ist ein schöner, schneller und trotzdem präziser Workflow für Klausur, Ausbildung, Kanzleivermerk und Mandatsarbeit.

Experimentelles Werkzeug. Keine Rechtsberatung, keine Gewähr. Gesetzestext und Rechtsprechung müssen im konkreten Fall geprüft werden. Literatur- oder Kommentarstellen dürfen nur genutzt werden, wenn sie vom Nutzer bereitgestellt wurden oder über eine lizenzierte Quelle live verifiziert sind.

## Schnellstart

/plugin install bgb-at-pruefer@claude-fuer-deutsches-recht

Starte mit dem Skill [allgemein](./skills/allgemein/SKILL.md). Der Einstieg fragt den Fall in einer kompakten Reihenfolge ab, baut eine Themenkarte und schlägt danach die passenden Spezial-Skills vor.

## Was das Plugin besonders gut kann

- aus einem unsortierten BGB-AT-Sachverhalt einen Anspruchsbaum bauen
- Angebot, Annahme, Zugang, Fristen und digitale Erklärungsketten auseinanderziehen
- Minderjährigenfälle mit §§ 104-113 BGB sauber prüfen
- Anfechtung mit Auslegung, Frist, Gegner und Folgen prüfen
- Stellvertretung, Vollmacht, Rechtsschein und § 181 BGB trennen
- Form, Nichtigkeit, Gesetzesverbot, Sittenwidrigkeit und Bedingung als Wirksamkeitsfragen einordnen
- elektronische Form, qES-Zugang, beA-Einreichung und prozessuale Formfiktion auseinanderhalten
- Waren mit digitalen Elementen, Updatehinweise, AGB-Abweichungen und Reparaturverlangen in die richtigen Spezial-Skills routen
- aus dem Ergebnis Gutachten, Mandatsmemo, Schriftsatzbaustein, Rückfragenbrief oder Trainingsfall machen

## Empfohlener Workflow

1. Fallfrage festnageln: Wer will was von wem, und auf welcher Anspruchsebene liegt das Problem?
2. Erklärungskette bauen: Jede Erklärung mit Datum, Kanal, Absender, Empfänger, Zugang und Inhalt erfassen.
3. BGB-AT-Themenkarte erstellen: Geschäftsfähigkeit, Willenserklärung, Vertragsschluss, Auslegung, Form, Nichtigkeit, Anfechtung, Stellvertretung, Bedingung, Fristen.
4. Spezial-Skills laden: Der Allgemein-Skill schlägt zwei bis fünf passende Folge-Skills vor.
5. Arbeitsprodukt wählen: Klausurlösung, Memo, Schriftsatzbaustein, Fristenvermerk oder Training.

## Skill-Auswahl

Die früher sehr lange Einzelskill-Tabelle ist in verdichtete Kompendium-Skills überführt. Nutze für die Auswahl die automatisch gepflegte Übersicht unten; die Kompendien enthalten die früheren Einzelthemen als Unterabschnitte mit ihren Prüfprogrammen, Normankern und Ausgabeformaten.

## Quellen- und Aktualitätsanker

- Aktueller BGB-Gesetzestext: https://www.gesetze-im-internet.de/bgb/
- Interne Struktur: [references/bgb-at-pruefprogramm.md](./references/bgb-at-pruefprogramm.md)
- Rechtsstandsregel: [references/rechtsstand-und-quellen.md](./references/rechtsstand-und-quellen.md)

## Gute Begleiter

- [methodenlehre-buergerliches-recht](../methodenlehre-buergerliches-recht) für Auslegung, Gutachtenstil und Anspruchsdenken.
- [subsumtions-pruefer](../subsumtions-pruefer) für generische Tatbestandsarbeit.
- [schriftform-und-textform-bgb](../schriftform-und-textform-bgb) für tiefe Form-, Textform- und Zugangskonstellationen.
- [bereicherungs-und-anfechtungsrecht-pruefer](../bereicherungs-und-anfechtungsrecht-pruefer) für Rückabwicklung nach unwirksamem Vertrag.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 23 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im BGB-AT-Prüfer. Fragt Fallfrage, Rolle, Anspruchsziel, Tatsachen, Fristen, Erklärungen, Beteiligte und Wunsch-Output ab, baut einen schönen Arbeitsplan und schlägt passende Spezial-Skills au... |
| `bgb-at-output-gutachten-memo-schriftsatz` | Output-Skill für BGB-AT-Ergebnisse: Klausurlösung im Gutachtenstil, praxisnahes Mandatsmemo, Subsumtionsraster und Schriftsatzbaustein — abhängig vom Arbeitsziel und Mandantenkontext strukturiert aufbereitet. |
| `bgb-at-rechtsschein-redteam` | Red-Team-Skill für Rechtsschein-Argumentation im BGB AT: Vollmachtsrechtsschein, Duldungs- und Anscheinsvollmacht nach BGH-Rechtsprechung, Entgegenstehende Argumente prüfen, schwache Rechtsschein-Positionen identifizieren. |
| `kompendium-01-anfechtungsfrist-erk-bis-bedingung-befristung` | bgb-at-pruefer: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (anfechtungsfrist-erklaerung-bestaetigung, annahmefrist-verspaetung-paragraphen-147-149, bedingung-befristung-paragraphen-158-163) und bewahrt deren Work... |
| `kompendium-02-fristen-berechnung-p-bis-ergaenzende-vertrags` | bgb-at-pruefer: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (fristen-berechnung-paragraphen-186-193, cic-vorvertragliche-pflichten-schnittstelle, ergaenzende-vertragsauslegung) und bewahrt deren Workflows, Normank... |
| `kompendium-03-vertragsschluss-antr-bis-invitatio-ad-offeren` | bgb-at-pruefer: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (vertragsschluss-antrag-annahme, abgabe-willenserklaerung, invitatio-ad-offerendum-und-werbung) und bewahrt deren Workflows, Normanker, Prüfprogramme und... |
| `kompendium-04-agb-einbeziehung-sch-bis-anfechtung-routing` | bgb-at-pruefer: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (agb-einbeziehung-schnittstelle-paragraphen-305-310, amtlicher-bgb-zpo-normcheck, anfechtung-routing) und bewahrt deren Workflows, Normanker, Prüfprogram... |
| `kompendium-05-anfechtungsfolgen-pa-bis-auslegung-paragraphe` | bgb-at-pruefer: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (anfechtungsfolgen-paragraphen-142-122, anspruchsaufbau-zivilrecht-bgb-at, auslegung-paragraphen-133-157) und bewahrt deren Workflows, Normanker, Prüfpro... |
| `kompendium-06-auslegung-sachverhal-bis-bgb-at-erklaerungske` | bgb-at-pruefer: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (auslegung-sachverhalt-und-fallfrage, bgb-at-anfechtung-vor-auslegung, bgb-at-erklaerungskette-tableau) und bewahrt deren Workflows, Normanker, Prüfprogr... |
| `kompendium-07-bgb-at-fallaufnahme-bis-bgb-at-minderjaehrig` | bgb-at-pruefer: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (bgb-at-fallaufnahme-und-pruefprogramm, bgb-at-form-und-prozessform, bgb-at-minderjaehrige-fehlsubsumtion) und bewahrt deren Workflows, Normanker, Prüfpr... |
| `kompendium-08-bgb-at-training-fall-bis-duldungs-anscheinsvo` | bgb-at-pruefer: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (bgb-at-training-fallvarianten, digitale-elemente-reparaturrecht-router, duldungs-anscheinsvollmacht) und bewahrt deren Workflows, Normanker, Prüfprogram... |
| `kompendium-09-eigenschaftsirrtum-p-bis-einwilligung-genehmi` | bgb-at-pruefer: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (eigenschaftsirrtum-paragraph-119-2, einseitige-geschaefte-minderjaehrige-paragraph-111, einwilligung-genehmigung-paragraphen-107-bis-109) und bewahrt de... |
| `kompendium-10-elektronische-form-b-bis-erklaerungsbewusstse` | bgb-at-pruefer: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (elektronische-form-bea-qes-formfiktion, elektronischer-zugang-und-plattformen, erklaerungsbewusstsein-und-potentielles-bewusstsein) und bewahrt deren Wo... |
| `kompendium-11-erwerbsgeschaeft-die-bis-geschaeftsfaehigkeit` | bgb-at-pruefer: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (erwerbsgeschaeft-dienst-arbeit-paragraphen-112-113, formnichtigkeit-paragraphen-125-129, geschaeftsfaehigkeit-paragraphen-104-bis-106) und bewahrt deren... |
| `kompendium-12-gesetzesverbot-sitte-bis-handeln-im-fremden-n` | bgb-at-pruefer: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (gesetzesverbot-sittenwidrigkeit-paragraphen-134-138, gutachtenstil-und-klausurtechnik, handeln-im-fremden-namen-offenkundigkeit) und bewahrt deren Workf... |
| `kompendium-13-insichgeschaeft-para-bis-kauf-im-internet-und` | bgb-at-pruefer: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (insichgeschaeft-paragraph-181, irrtumsanfechtung-paragraph-119-1, kauf-im-internet-und-auktionen) und bewahrt deren Workflows, Normanker, Prüfprogramme... |
| `kompendium-14-klausurloesungen-feh-bis-missbrauch-vertretun` | bgb-at-pruefer: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (klausurloesungen-fehlerdiagnose, konsens-dissens-paragraphen-154-155, missbrauch-vertretungsmacht) und bewahrt deren Workflows, Normanker, Prüfprogramme... |
| `kompendium-15-personen-rechtsfaehi-bis-rechtlich-vorteilhaf` | bgb-at-pruefer: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (personen-rechtsfaehigkeit-und-handlungsfaehigkeit, privatautonomie-trennungs-abstraktionsprinzip, rechtlich-vorteilhaft-paragraph-107) und bewahrt deren... |
| `kompendium-16-schweigen-und-erklae-bis-taeuschung-drohung-p` | bgb-at-pruefer: Konsolidiertes Skill-Kompendium 16; bündelt 3 frühere Spezialskills (schweigen-und-erklaerungswert, stellvertretung-routing-paragraphen-164-181, taeuschung-drohung-paragraph-123) und bewahrt deren Workflows, Normanker, Pr... |
| `kompendium-17-taschengeld-paragrap-bis-verfuegung-nichtbere` | bgb-at-pruefer: Konsolidiertes Skill-Kompendium 17; bündelt 3 frühere Spezialskills (taschengeld-paragraph-110, uebermittlungsirrtum-paragraph-120, verfuegung-nichtberechtigter-paragraph-185) und bewahrt deren Workflows, Normanker, Prüfp... |
| `kompendium-18-verjaehrung-grundsch-bis-vollmacht-erteilung` | bgb-at-pruefer: Konsolidiertes Skill-Kompendium 18; bündelt 3 frühere Spezialskills (verjaehrung-grundschema-paragraphen-194-218, vertreter-ohne-vertretungsmacht-paragraphen-177-179, vollmacht-erteilung-umfang-erloeschen) und bewahrt der... |
| `kompendium-19-willenserklaerung-ta-bis-zugang-paragraph-130` | bgb-at-pruefer: Konsolidiertes Skill-Kompendium 19; bündelt 3 frühere Spezialskills (willenserklaerung-tatbestand, wucher-und-ausbeutung-paragraph-138-2, zugang-paragraph-130) und bewahrt deren Workflows, Normanker, Prüfprogramme und Aus... |
| `kompendium-20-zugangsvereitelung-u-bis-zugangsvereitelung-u` | bgb-at-pruefer: Konsolidiertes Skill-Kompendium 20; bündelt 1 frühere Spezialskills (zugangsvereitelung-und-annahmeverweigerung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
