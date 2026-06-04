# Fortbestehensprognose

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fortbestehensprognose`) | [`fortbestehensprognose.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fortbestehensprognose.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Fortbestehensprognose Paragrafix GmbH** (`fortbestehensprognose-paragrafix-gmbh`) | [Gesamt-PDF lesen](../testakten/fortbestehensprognose-paragrafix-gmbh/gesamt-pdf/fortbestehensprognose-paragrafix-gmbh_gesamt.pdf) | [`testakte-fortbestehensprognose-paragrafix-gmbh.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fortbestehensprognose-paragrafix-gmbh.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Fortbestehensprognose nach § 19 Abs. 2 InsO als Geschäftsführer-Selbstdokumentation. Prüfablauf Bilanzstatus Annahmen Plausibilisierung 12-Monats-Liquidität. Sanierungsbausteine harte Patronatserklärung Comfortletter Gesellschafterdarlehen Rangrücktritt Stundung Forderungsverzicht. IDW S 11 S 6 StaRUG. Funktioniert allein; empfohlene Begleitplugins liquiditätsplanung (wochenbasierte Liquidität) und insolvenzrecht (§ 17 § 18 InsO Antragspflicht).

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `annahmen-belastbarkeit-plausibilisieren` | Plausibilisiert die in `annahmen-sammeln-fortfuehrung` gesammelten Annahmen. Prüfraster Konsistenz mit Vergangenheit (BWA SuSa Jahresabschluss) Marktentwicklung (Branche makroekonomisch) Konsistenz untereinander (Ums… |
| `annahmen-sammeln-fortfuehrung` | Sammelt die Annahmen die der Geschäftsführer der Fortbestehensprognose zu Grunde legt. Umsatzentwicklung Kostenentwicklung Personalkostenentwicklung Investitionen Working-Capital Saisonalität Auftragsbestand Kunden… |
| `ausloesendes-ereignis-erfassen` | Erfasst den Anlass der Fortbestehensprognose. Typische Auslöser sind Hinweis des Steuerberaters nach § 102 StaRUG Hinweis des Wirtschaftsprüfers Bekanntwerden negativen Eigenkapitals Bilanzaufstellung mit negativem … |
| `bilanzieller-status-aufnehmen` | Nimmt die bilanzielle Ausgangslage auf — Aktiva Passiva Eigenkapital nach HGB-Stichtagsbilanz. Prüfraster bilanzielle Überschuldung (Aktiva kleiner als Passiva). Erfasst stille Reserven und stille Lasten Sonderposte… |
| `comfortletter-weich-erzeugen` | Erzeugt einen Comfortletter — eine weiche Erklärung des Patrons oder Mutterunternehmens das Tochterunternehmen zu unterstützen. Im Gegensatz zur harten externen Patronatserklärung ist der Comfortletter nicht rechts… |
| `forderungsverzicht-besserungsschein` | Erzeugt eine Forderungsverzichtsvereinbarung mit Besserungsschein. Gläubiger verzichtet auf Forderung — bei Wiedererstarken der Zahlungsfähigkeit der Schuldnerin lebt die Forderung wieder auf. Effekt im insolvenzrec… |
| `fortbestehensprognose-zusammenfuehren` | Führt alle Bausteine zusammen — bilanzieller Status Annahmen Plausibilisierung 12-Monats-Liquidität Sensitivitätsszenarien — und bewertet ob die Fortbestehensprognose nach § 19 Abs. 2 InsO positiv ist. Massstab ueb… |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `fortbestehensprognose-kaltstart-interview` | Kaltstart-Interview für das Fortbestehensprognose-Plugin. Stellt fest wer das Plugin nutzt (Geschäftsführer / Vorstand / Gesellschafter mit Eigenverantwortung / Finanzleiter mit Mandat) wer der Anwaltliche und steu… |
| `liquiditaet-12-monate` | Erstellt die rollierende Zwölf-Monats-Liquiditätsvorschau auf Basis der plausibilisierten Annahmen. Pro Woche oder pro Monat Aufstellung der Einzahlungen und Auszahlungen Anfangsbestand Endbestand Linieverbleib. Pru… |
| `patronatserklaerung-extern-hart-erzeugen` | Erzeugt eine harte externe Patronatserklärung des Gesellschafters (oder eines Dritten) zugunsten der Gesellschaft. Erfasst Patron Begueneten Höhe Bedingungen Laufzeit Insolvenzfeste Klausel. Zur Berücksichtigung im… |
| `prognose-dokumentation-stichtag` | Abschließende Selbstdokumentation der Fortbestehensprognose zum konkreten Stichtag. Enthält Ausgangslage Annahmen Plausibilisierung Liquidität Szenarien Sanierungsbausteine mit Belegen Gesamtergebnis. Dient als Bel… |
| `sanierungsbausteine-vorschlagen` | Wenn die Fortbestehensprognose ohne Maßnahmen negativ oder knapp positiv ist schlägt dieser Skill konkrete Sanierungsbausteine vor. Auswahl Patronatserklärung hart Comfortletter Gesellschafterdarlehen mit Rangrück… |
| `stundungsanfrage-glaeubiger` | Erzeugt Stundungsanfragen an Gläubiger (Lieferanten Bank Vermieter Steueramt Sozialversicherungsträger). Erfasst pro Gläubiger Forderungshöhe Fälligkeit Stundungswunsch (neue Fälligkeit Ratenzahlung Tilgungspaus… |
| `wenn-prognose-negativ-naechste-schritte` | Wenn die Fortbestehensprognose negativ ausfällt — Eskalations- und Pflichtenkatalog für den Geschäftsleiter. Antragspflicht § 15a InsO sechs Wochen bei Überschuldung drei Wochen bei Zahlungsunfähigkeit. Zahlungsv… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `fortbestehensprognose-kaltstart-interview` | Kaltstart-Interview für das Fortbestehensprognose-Plugin. Stellt fest wer das Plugin nutzt (Geschäftsführer / Vorstand / Gesellschafter mit Eigenverantwortung / Finanzleiter mit Mandat) wer der Anwaltliche und steuerliche Ansprechpartner... |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | fortbestehensprognose: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausg... |
| `kompendium-02-workflow-mandantenko-bis-spezial-geschaeftsfu` | fortbestehensprognose: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-mandantenkommunikation, workflow-redteam-qualitygate, spezial-geschaeftsfuehrer-fristen-form-und-zustaendigkeit) und bewahrt deren Workf... |
| `kompendium-03-spezial-negativer-fr-bis-forderungsverzicht-b` | fortbestehensprognose: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (spezial-negativer-fristennotiz-und-naechster-schritt, ausloesendes-ereignis-erfassen, forderungsverzicht-besserungsschein) und bewahrt deren Work... |
| `kompendium-04-prognose-dokumentati-bis-annahmen-belastbarke` | fortbestehensprognose: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (prognose-dokumentation-stichtag, stundungsanfrage-glaeubiger, annahmen-belastbarkeit-plausibilisieren) und bewahrt deren Workflows, Normanker, Pr... |
| `kompendium-05-annahmen-sammeln-for-bis-comfortletter-weich` | fortbestehensprognose: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (annahmen-sammeln-fortfuehrung, bilanzieller-status-aufnehmen, comfortletter-weich-erzeugen) und bewahrt deren Workflows, Normanker, Prüfprogramme... |
| `kompendium-06-fbp-bankenkommunikat-bis-fbp-stresstest-szena` | fortbestehensprognose: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (fbp-bankenkommunikation-waiver-spezial, fbp-integrierte-planung-bauleiter, fbp-stresstest-szenarien-leitfaden) und bewahrt deren Workflows, Norma... |
| `kompendium-07-fbp-zahlungsunfaehig-bis-fp-cash-flow-modell` | fortbestehensprognose: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (fbp-zahlungsunfaehigkeit-ueberschuldungsabgrenzung-spezial, fortbestehensprognose-zusammenfuehren, fp-cash-flow-modell-spezial) und bewahrt deren... |
| `kompendium-08-fp-dokumentation-ger-bis-fp-zeitraum-und-szen` | fortbestehensprognose: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (fp-dokumentation-gerichtsfaehigkeit-spezial, fp-einfuehrung-pflicht-und-zweck, fp-zeitraum-und-szenarien-praxis) und bewahrt deren Workflows, Nor... |
| `kompendium-09-gesellschafterdarleh-bis-patronatserklaerung` | fortbestehensprognose: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (gesellschafterdarlehen-rangruecktritt, liquiditaet-12-monate, patronatserklaerung-extern-hart-erzeugen) und bewahrt deren Workflows, Normanker, P... |
| `kompendium-10-sanierungsbausteine-bis-spezial-bilanzstatus` | fortbestehensprognose: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (sanierungsbausteine-vorschlagen, spezial-annahmen-behoerden-gericht-und-registerweg, spezial-bilanzstatus-risikoampel-und-gegenargumente) und bew... |
| `kompendium-11-spezial-comfortlette-bis-spezial-forderungsve` | fortbestehensprognose: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (spezial-comfortletter-internationaler-bezug-und-schnittstellen, spezial-eskalation-sonderfall-und-edge-case, spezial-forderungsverzicht-mandanten... |
| `kompendium-12-spezial-fortbestehen-bis-spezial-inso-tatbest` | fortbestehensprognose: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (spezial-fortbestehensdokumentation-insolvenzrecht, spezial-fortbestehensprognose-erstpruefung-und-mandatsziel, spezial-inso-tatbestand-beweis-und... |
| `kompendium-13-spezial-liquiditaet-bis-spezial-plausibilisi` | fortbestehensprognose: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (spezial-liquiditaet-zahlen-schwellen-und-berechnung, spezial-patronatserklaerung-mehrparteien-konflikt-und-interessen, spezial-plausibilisierung-... |
| `kompendium-14-spezial-rangruecktri-bis-spezial-selbstdokume` | fortbestehensprognose: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (spezial-rangruecktritt-formular-portal-und-einreichung, spezial-sanierungsbausteine-compliance-dokumentation-und-akte, spezial-selbstdokumentatio... |
| `kompendium-15-spezial-starug-bewei-bis-spezial-zwoelf-verha` | fortbestehensprognose: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (spezial-starug-beweislast-und-darlegungslast, spezial-stundung-red-team-und-qualitaetskontrolle, spezial-zwoelf-verhandlung-vergleich-und-eskalat... |
| `kompendium-16-wenn-prognose-negati-bis-wenn-prognose-negati` | fortbestehensprognose: Konsolidiertes Skill-Kompendium 16; bündelt 1 frühere Spezialskills (wenn-prognose-negativ-naechste-schritte) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-monats-livequellen-und-rechtsprechungscheck` | Monats: Livequellen- und Rechtsprechungscheck im Plugin fortbestehensprognose; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin fortbestehensprognose: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin fortbestehensprognose: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin fortbestehensprognose: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin fortbestehensprognose: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin fortbestehensprognose: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin fortbestehensprognose: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
