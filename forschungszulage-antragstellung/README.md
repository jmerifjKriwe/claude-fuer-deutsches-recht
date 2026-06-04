# Forschungszulage-Antragstellung

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`forschungszulage-antragstellung`) | [`forschungszulage-antragstellung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/forschungszulage-antragstellung.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Forschungszulage Riedblick Sensorik GmbH** (`forschungszulage-sensorik-startup-taunus`) | [Gesamt-PDF lesen](../testakten/forschungszulage-sensorik-startup-taunus/gesamt-pdf/forschungszulage-sensorik-startup-taunus_gesamt.pdf) | [`testakte-forschungszulage-sensorik-startup-taunus.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-forschungszulage-sensorik-startup-taunus.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Plugin für die steuerliche Forschungsförderung nach dem Forschungszulagengesetz: Fördercheck, BSFZ-Bescheinigung, Projektbeschreibung, FuE-Abgrenzung, Bemessungsgrundlage, Finanzamt-Antrag, Auszahlung, Verlust-/Krisenlage, Dokumentation für Außenprüfung, Kumulierung und Nachbesserung.

Das Plugin ist für Unternehmen, Start-ups, Mittelstand, Steuerberaterinnen, Rechtsanwälte, CFOs und Produkt-/Entwicklungsteams gebaut. Es übersetzt technische Entwicklung in die Sprache, die BSFZ und Finanzamt brauchen: Neuheit, Risiko, systematisches Vorgehen, förderfähige Aufwendungen und saubere Belege. Es kann bewusst zwei Geschwindigkeiten: geführter Modus für Einsteiger und harter Ampel-/Cashflow-Modus für Profis.

## Quellen-Gate

Vor jeder belastbaren Ausgabe live prüfen:

- Forschungszulagengesetz auf `gesetze-im-internet.de`, insbesondere §§ 1 bis 7 und § 10 FZulG.
- BSFZ-Antragsverfahren: zweistufig, erst FuE-Bescheinigung bei der BSFZ, dann Antrag beim Finanzamt.
- BMF-Forschungszulage und BMF-Schreiben vom 07.02.2023, soweit noch nicht durch ein neues finales Schreiben ersetzt.
- Änderungen ab 2026: Bemessungsgrundlagenhöchstbetrag 12 Mio. Euro, 20-%-Pauschale für Gemein- und Betriebskosten bei nach dem 31.12.2025 begonnenen Vorhaben, Eigenleistung 100 Euro pro Stunde bis max. 40 Stunden/Woche.

## Skill-Matrix

| Skill | Wofür? |
| --- | --- |
| `allgemein` | Einstieg, Triage, Förderroute und Projektaufnahme |
| `fz-foerdercheck-kaltstart` | Anspruchsberechtigung, Projektart, Jahre, Risiken, Sofortpotenzial |
| `fz-bsfz-bescheinigung-projektbeschreibung` | BSFZ-Antrag, Vorhabenbeschreibung, technische Neuheit, Risiko |
| `fz-plaedoyer-begruendung-und-verteidigung` | Plädoyer, Begründung und Verteidigung gegenüber BSFZ, Finanzamt, Geschäftsführung, Insolvenzverwaltung oder Einspruchsstelle |
| `fz-fue-definition-frascati-abgrenzung` | Grundlagenforschung, industrielle Forschung, experimentelle Entwicklung |
| `fz-bemessungsgrundlage-2026` | Personal, Eigenleistung, Auftragsforschung, Wirtschaftsgüter, 12-Mio.-Grenze |
| `fz-finanzamt-festsetzung-auszahlung` | Antrag beim Finanzamt, Anrechnung, Auszahlung, Vorauszahlungssenkung |
| `fz-insolvenz-verlust-liquiditaet` | Krise, Verlustjahr, Insolvenz, Forderungs-/Masseblick, Liquidität |
| `fz-dokumentationspaket-betriebspruefung` | Stundenzettel, Projektakte, Kostenbelege, Prüferpaket |
| `fz-kumulierung-beihilfen-agvo` | Doppelförderung, AGVO, andere Zuschüsse, EU/EWR-Auftragsforschung |
| `fz-ablehnung-nachbesserung-einspruch` | BSFZ-Nachforderung, Ablehnung, Finanzamt-Einspruch, Reparatur |
| `fz-roadmap-mehrjahresantrag` | Mehrjahresstrategie, rückwirkende Jahre, Jahreswechsel, Portfolio |

## Typische Startpunkte

| Situation | Start |
| --- | --- |
| "Wir wissen nicht, ob unser Vorhaben FuE ist" | `allgemein` → `fz-foerdercheck-kaltstart` |
| "Wir müssen den BSFZ-Antrag schreiben" | `fz-fue-definition-frascati-abgrenzung` → `fz-bsfz-bescheinigung-projektbeschreibung` |
| "Wir brauchen ein überzeugendes Plädoyer / eine Begründung" | `fz-plaedoyer-begruendung-und-verteidigung` |
| "Wir wollen wissen, wie viel Geld kommt" | `fz-bemessungsgrundlage-2026` → `fz-finanzamt-festsetzung-auszahlung` |
| "Wir sind im Verlust / in der Krise" | `fz-insolvenz-verlust-liquiditaet` |
| "BSFZ fragt nach oder lehnt ab" | `fz-ablehnung-nachbesserung-einspruch` |

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `fz-foerdercheck-kaltstart` | Schneller Fördercheck Forschungszulage in zehn Minuten: Anspruchsberechtigung, FuE-Kategorie nach Frascati, KMU-Status, Personalkosten-Schwelle, Projektjahre, Kostenarten, BSFZ-/Finanzamt-Status, Kumulierung, Ausschlussrisiken und realis... |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | forschungszulage-antragstellung: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramm... |
| `kompendium-02-workflow-mandantenko-bis-spezial-fzulg-friste` | forschungszulage-antragstellung: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-mandantenkommunikation, workflow-redteam-qualitygate, spezial-fzulg-fristen-form-und-zustaendigkeit) und bewahrt deren Workflo... |
| `kompendium-03-spezial-mehrjahresro-bis-forsch-bsfz-pruefung` | forschungszulage-antragstellung: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (spezial-mehrjahresroadmap-fristennotiz-und-naechster-schritt, fz-auftragsforschung-vertragsgestaltung, forsch-bsfz-pruefung-spezial) un... |
| `kompendium-04-fz-betriebspruefung-bis-fz-historie-und-rech` | forschungszulage-antragstellung: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (fz-betriebspruefung-strategie, fz-finanzamt-festsetzung-auszahlung, fz-historie-und-rechtsgrundlagen) und bewahrt deren Workflows, Norm... |
| `kompendium-05-fz-insolvenz-verlust-bis-forsch-projektbeschr` | forschungszulage-antragstellung: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (fz-insolvenz-verlust-liquiditaet, forsch-konzernverbund-forschung-spezial, forsch-projektbeschreibung-bauleiter) und bewahrt deren Work... |
| `kompendium-06-forsch-stundenaufzei-bis-fz-bemessungsgrundla` | forschungszulage-antragstellung: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (forsch-stundenaufzeichnung-leitfaden, fz-ablehnung-nachbesserung-einspruch, fz-bemessungsgrundlage-2026) und bewahrt deren Workflows, N... |
| `kompendium-07-fz-bescheidung-recht-bis-fz-dokumentationspak` | forschungszulage-antragstellung: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (fz-bescheidung-rechtsmittel, fz-bsfz-bescheinigung-projektbeschreibung, fz-dokumentationspaket-betriebspruefung) und bewahrt deren Work... |
| `kompendium-08-fz-fue-abgrenzung-gr-bis-fz-konzern-und-organ` | forschungszulage-antragstellung: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (fz-fue-abgrenzung-grenzfaelle, fz-fue-definition-frascati-abgrenzung, fz-konzern-und-organschaft-spezial) und bewahrt deren Workflows,... |
| `kompendium-09-fz-koordinierung-zwe-bis-fz-personalkosten-un` | forschungszulage-antragstellung: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (fz-koordinierung-zwei-foerderwege, fz-kumulierung-beihilfen-agvo, fz-personalkosten-und-stundennachweis) und bewahrt deren Workflows, N... |
| `kompendium-10-fz-plaedoyer-begruen-bis-fz-start-up-und-pers` | forschungszulage-antragstellung: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (fz-plaedoyer-begruendung-und-verteidigung, fz-roadmap-mehrjahresantrag, fz-start-up-und-personengesellschaft) und bewahrt deren Workflo... |
| `kompendium-11-spezial-abgrenzung-c-bis-spezial-antrag-zahle` | forschungszulage-antragstellung: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (spezial-abgrenzung-compliance-dokumentation-und-akte, spezial-adaptiver-dokumentenmatrix-und-lueckenliste, spezial-antrag-zahlen-schwel... |
| `kompendium-12-spezial-antragstellu-bis-spezial-beihilfen-be` | forschungszulage-antragstellung: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (spezial-antragstellung-tatbestand-beweis-und-belege, spezial-auszahlung-internationaler-bezug-und-schnittstellen, spezial-beihilfen-bew... |
| `kompendium-13-spezial-bemessungsgr-bis-spezial-definition-a` | forschungszulage-antragstellung: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (spezial-bemessungsgrundlage-mehrparteien-konflikt-und-interessen, spezial-bsfz-behoerden-gericht-und-registerweg, spezial-definition-ab... |
| `kompendium-14-spezial-dokumentatio-bis-spezial-foerdercheck` | forschungszulage-antragstellung: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (spezial-dokumentation-mandantenentscheidung, spezial-einspruch-sonderfall-und-edge-case, spezial-foerdercheck-risikoampel-und-gegenargu... |
| `kompendium-15-spezial-forschungszu-bis-spezial-portaltexte` | forschungszulage-antragstellung: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (spezial-forschungszulage-erstpruefung-und-mandatsziel, spezial-insolvenzlage-red-team-und-qualitaetskontrolle, spezial-portaltexte-schr... |
| `kompendium-16-spezial-verlust-form-bis-spezial-zeichenbudge` | forschungszulage-antragstellung: Konsolidiertes Skill-Kompendium 16; bündelt 2 frühere Spezialskills (spezial-verlust-formular-portal-und-einreichung, spezial-zeichenbudgets-verhandlung-vergleich-und-eskalation) und bewahrt deren Workflo... |
| `spezial-finanzamt-livequellen-und-rechtsprechungscheck` | Finanzamt: Livequellen- und Rechtsprechungscheck im Plugin forschungszulage antragstellung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin forschungszulage-antragstellung: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin forschungszulage-antragstellung: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin forschungszulage-antragstellung: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin forschungszulage-antragstellung: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin forschungszulage-antragstellung: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin forschungszulage-antragstellung: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
