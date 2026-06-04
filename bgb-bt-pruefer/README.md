# BGB BT Prüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`bgb-bt-pruefer`) | [`bgb-bt-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bgb-bt-pruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **BGB BT — Holzofen, Lieferkette, Bürgschaft, GoA und Brandschaden** (`bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt`) | [Gesamt-PDF lesen](../testakten/bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt/gesamt-pdf/bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt_gesamt.pdf) | [`testakte-bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt.zip) |
| **BGB BT — Smart-Kühlschrank, digitale Elemente und Reparaturblockade** (`bgb-bt-smart-kuehlschrank-digital-repair-koeln`) | [Gesamt-PDF lesen](../testakten/bgb-bt-smart-kuehlschrank-digital-repair-koeln/gesamt-pdf/bgb-bt-smart-kuehlschrank-digital-repair-koeln_gesamt.pdf) | [`testakte-bgb-bt-smart-kuehlschrank-digital-repair-koeln.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bgb-bt-smart-kuehlschrank-digital-repair-koeln.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Großer BGB-BT-Prüfer für Schuldrecht Besonderer Teil: Kauf, Verbrauchsgüterkauf, Waren mit digitalen Elementen, Updatepflichten, Right-to-Repair-Schnittstellen, Miete, Pacht, Leihe, Darlehen, Dienst, Werk, Bau, Reise, Makler, Auftrag, Geschäftsbesorgung, Bürgschaft, Schuldversprechen, GoA, Bereicherung, Delikt und Rückabwicklung.

Das Plugin ist der Gegenpart zum `bgb-at-pruefer`: Es beginnt bei der Anspruchsfrage und führt dann durch die Vertragstypen und gesetzlichen Schuldverhältnisse des BGB-BT. Es ist für Anfänger verständlich genug, aber hart genug für Kanzleivermerke, Klageentwürfe, Verteidigungslinien und Ausbildung.

## Kaltstart

1. **Wer will was von wem?** Leistung, Zahlung, Unterlassung, Rückzahlung, Schadensersatz oder Herausgabe.
2. **Welcher Lebensbereich?** Kauf, Miete, Werk, Dienst, Auftrag, Bürgschaft, GoA, Bereicherung, Delikt.
3. **Welche Störung?** Mangel, Verzug, Kündigung, Rücktritt, Anfechtung, Nichtigkeit, Aufrechnung, Verjährung, Beweisproblem.
4. **Welches Arbeitsprodukt?** Gutachten, Mandantenbrief, Klageskizze, Anspruchsmatrix, Vergleichsvorschlag, Beweis- und Fristenplan.

## Leitprinzip

Erst Anspruchsgrundlage, dann Tatbestand, dann Rechtsfolge, dann Einwendungen. Keine Sammelwörter wie „irgendwie vertragsähnlich“, wenn eine saubere Reihenfolge möglich ist. Schnittstellen zum BGB AT, AGB-Recht, Bereicherungs- und Anfechtungsrecht sowie Methodenlehre werden aktiv vorgeschlagen.

## Quellenanker

- BGB amtlich/frei: https://www.gesetze-im-internet.de/bgb/
- Kaufvertrag: §§ 433 ff. BGB
- Digitale Produkte und Waren mit digitalen Elementen: §§ 327 ff., 327a, 327e, 327f, 434, 475b, 475c, 475e, 476, 477 BGB
- Miete/Pacht/Leihe/Darlehen/Dienst/Werk: §§ 488 ff., 535 ff., 581 ff., 598 ff., 611 ff., 631 ff. BGB
- Auftrag/Geschäftsbesorgung/GoA/Bürgschaft/Delikt/Bereicherung: §§ 662 ff., 675 ff., 677 ff., 765 ff., 812 ff., 823 ff. BGB
- Right to Repair: Richtlinie (EU) 2024/1799, Umsetzungsstand live prüfen; nicht ungeprüft als bereits vollständig deutsches BGB-Recht behandeln.

## Testakte

Die Demonstrationsakte `bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt` verbindet Kauf, Werk, Bürgschaft, GoA, Bereicherung und Delikt in einem realistisch unordentlichen Mandat.

Die Akte `bgb-bt-smart-kuehlschrank-digital-repair-koeln` ergänzt den modernen Kaufrechtsstrang: vernetzter Kühlschrank, App/Cloud/Firmware, Updatepflicht, § 475b/§ 475c BGB, Beweislast, Verjährung, Reparaturblockade und Right-to-Repair-Schnittstelle.

## Keine Blindzitate

Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und überprüfbarer freier Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatzangaben aus Modellwissen.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 27 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Skill-Routing für BGB-BT-Fälle: Anspruchsziel, Vertragstyp, gesetzliches Schuldverhältnis, Störung, Beweise, Fristen und Output. |
| `kompendium-01-workflow-anfangercoa-bis-workflow-beweislast` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (workflow-anfangercoach-schuldrecht-bt, workflow-anspruchslandkarte, workflow-beweislast-und-belegmatrix) und bewahrt deren Workflows, Normanker, Prüfpro... |
| `kompendium-02-workflow-fristen-rue-bis-bt-fristen-erklaerun` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-fristen-ruecktritt-kuendigung, workflow-vergleich-und-verhandlungsplan, bt-fristen-erklaerungen-zugang) und bewahrt deren Workflows, Normanker,... |
| `kompendium-03-arbeitsnaher-dienstv-bis-bt-vertragsentwurf-m` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (arbeitsnaher-dienstvertrag-bgb, bauvertrag-und-verbraucherbauvertrag, bt-vertragsentwurf-modellvertrag) und bewahrt deren Workflows, Normanker, Prüfprog... |
| `kompendium-04-delikt-vertrag-konku-bis-kaufvertrag-grundsch` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (delikt-vertrag-konkurrenz, dienstvertrag-und-behandlungsvertrag, kaufvertrag-grundschema-paragraph-433) und bewahrt deren Workflows, Normanker, Prüfprog... |
| `kompendium-05-maklervertrag-und-pr-bis-reisevertrag-pauscha` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (maklervertrag-und-provision, mietvertrag-grundschema-paragraph-535, reisevertrag-pauschalreise) und bewahrt deren Workflows, Normanker, Prüfprogramme un... |
| `kompendium-06-vertragstypen-mischv-bis-werkvertrag-grundsch` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (vertragstypen-mischvertrag-router, werkvertrag-abnahme-und-faelligkeit, werkvertrag-grundschema-paragraph-631) und bewahrt deren Workflows, Normanker, P... |
| `kompendium-07-werkvertrag-maengelr-bis-kaufrecht-schadenser` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (werkvertrag-maengelrechte, deliktsrecht-haftung-fuer-verrichtungen-paragraph-831, kaufrecht-schadensersatz-aufwendungsersatz) und bewahrt deren Workflow... |
| `kompendium-08-produzentenhaftung-u-bis-geschaeftsbesorgung` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (produzentenhaftung-und-verkehrssicherung, schadensrecht-paragraphen-249-253, geschaeftsbesorgung-auftrag-mandat) und bewahrt deren Workflows, Normanker,... |
| `kompendium-09-amtlicher-bgb-bt-nor-bis-bereicherungsrecht-e` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (amtlicher-bgb-bt-normcheck, auftrag-und-unentgeltliche-taetigkeit, bereicherungsrecht-entreicherung-und-saldotheorie) und bewahrt deren Workflows, Norma... |
| `kompendium-10-bereicherungsrecht-l-bis-buergschaft-einreden` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (bereicherungsrecht-leistungskondiktion, bereicherungsrecht-nichtleistungskondiktion, buergschaft-einreden-und-akzessorietaet) und bewahrt deren Workflow... |
| `kompendium-11-buergschaft-form-und-bis-darlehen-und-finanzi` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (buergschaft-form-und-verbraucherbuerge, buergschaft-grundschema-paragraph-765, darlehen-und-finanzierung) und bewahrt deren Workflows, Normanker, Prüfpr... |
| `kompendium-12-delikt-organisations-bis-delikt-verkehrspflic` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (delikt-organisationspflicht, delikt-psychische-schaeden, delikt-verkehrspflicht-digital) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausga... |
| `kompendium-13-deliktsrecht-paragra-bis-deliktsrecht-schutzg` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (deliktsrecht-paragraph-823-1, deliktsrecht-paragraph-826-sittenwidrige-schaedigung, deliktsrecht-schutzgesetz-paragraph-823-2) und bewahrt deren Workflo... |
| `kompendium-14-deliktsrecht-sonstig-bis-gesamtschuld-und-reg` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (deliktsrecht-sonstiges-recht, deliktsrecht-tierhalter-und-gebaeude, gesamtschuld-und-regress-bgb-bt) und bewahrt deren Workflows, Normanker, Prüfprogram... |
| `kompendium-15-geschaeftsbesorgung-bis-goa-grundschema-para` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (geschaeftsbesorgung-und-zahlungsdienste, goa-entgegenstehender-wille-paragraphen-678-679, goa-grundschema-paragraph-677) und bewahrt deren Workflows, No... |
| `kompendium-16-kaufrecht-abweichung-bis-kaufrecht-dauerhafte` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 16; bündelt 3 frühere Spezialskills (kaufrecht-abweichungsvereinbarung-objektive-anforderungen-476, kaufrecht-beweislast-verjaehrung-digitale-elemente, kaufrecht-dauerhafte-bereitstellung-d... |
| `kompendium-17-kaufrecht-gefahruebe-bis-kaufrecht-rechtsmang` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 17; bündelt 3 frühere Spezialskills (kaufrecht-gefahruebergang-und-versendung, kaufrecht-nacherfuellung-ruecktritt-minderung, kaufrecht-rechtsmangel-paragraph-435) und bewahrt deren Workflo... |
| `kompendium-18-kaufrecht-right-to-r-bis-kaufrecht-updates-si` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 18; bündelt 3 frühere Spezialskills (kaufrecht-right-to-repair-und-nacherfuellung, kaufrecht-sachmangel-paragraph-434, kaufrecht-updates-sicherheitsupdates-327f-475b) und bewahrt deren Work... |
| `kompendium-19-kaufrecht-ware-mit-d-bis-mietrecht-mangel-min` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 19; bündelt 3 frühere Spezialskills (kaufrecht-ware-mit-digitalen-elementen-475b, leasing-bgb-bt-schnittstelle, mietrecht-mangel-minderung) und bewahrt deren Workflows, Normanker, Prüfprogr... |
| `kompendium-20-pacht-leihe-und-verw-bis-schuldversprechen-sc` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 20; bündelt 3 frühere Spezialskills (pacht-leihe-und-verwahrung, schnittstelle-bgb-at-methodenlehre-agb, schuldversprechen-schuldanerkenntnis) und bewahrt deren Workflows, Normanker, Prüfpr... |
| `kompendium-21-tausch-und-schenkung-bis-verbrauchsgueterkauf` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 21; bündelt 3 frühere Spezialskills (tausch-und-schenkung, unechte-goa-paragraph-687, verbrauchsgueterkauf-digitales) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-22-vergleich-paragraph-bis-werk-dienst-abgrenzu` | bgb-bt-pruefer: Konsolidiertes Skill-Kompendium 22; bündelt 3 frühere Spezialskills (vergleich-paragraph-779, verjaehrung-bgb-bt-spezial, werk-dienst-abgrenzung-erfolg) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemus... |
| `workflow-dokumentenintake` | Dokumenten-Intake für BGB-BT-Mandate: Unterlagen sichten, Aktenstruktur anlegen, Fristen erfassen. |
| `workflow-livequellen-rechtsstand` | Live-Quellencheck für BGB-BT: amtliche Gesetzestexte, Rechtsprechungsdatenbanken, Rechtsstand prüfen. |
| `workflow-output-gutachten-klage-brief` | Output-Workflow: Gutachten, Klage und Brief im BGB BT – Struktur, Stil und Qualitätskontrolle. |
| `workflow-red-team-gegenseite` | Red-Team-Analyse: Gegenseiten-Perspektive für BGB-BT-Mandate einnehmen und Schwachstellen identifizieren. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
