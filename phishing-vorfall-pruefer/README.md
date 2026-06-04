# Phishing-Vorfall-Prüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`phishing-vorfall-pruefer`) | [`phishing-vorfall-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/phishing-vorfall-pruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Phishing-Vorfall Mayer ./. Sparkasse Berlin** (`phishing-vorfall-mayer-sparkasse-berlin`) | [Gesamt-PDF lesen](../testakten/phishing-vorfall-mayer-sparkasse-berlin/gesamt-pdf/phishing-vorfall-mayer-sparkasse-berlin_gesamt.pdf) | [`testakte-phishing-vorfall-mayer-sparkasse-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-phishing-vorfall-mayer-sparkasse-berlin.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Plugin für anwaltliche Prüfung von Online-Banking-Phishing, pushTAN-/photoTAN-Vorfällen, Call-ID-Spoofing, gefälschten Bankhotlines, Social Engineering und streitigen Erstattungsansprüchen gegen Zahlungsdienstleister.

Das Plugin arbeitet entlang des typischen Mandats:

1. Intake: Konto, Zahlungsinstrument, Schaden, Autorisierung, Sperr- und Anzeigeverlauf.
2. Rechtsrahmen: § 675u BGB, § 675v BGB, § 675w BGB, § 675l BGB, § 676b BGB und § 55 ZAG.
3. Beweisprüfung: TAN-Dialog, App-Screens, Banklogs, IP-Adressen, Device-Binding, SCA, Transaktionsmonitoring, Warnhinweise.
4. Risikomatrix: nicht autorisierter Zahlungsvorgang, grobe Fahrlässigkeit, Bankpflichtverletzung, Mitverschulden/Quotelung, Ombudsmann oder Klage.
5. Output: Erstbewertung, Bankaufforderung, Ombudsmann-Antrag, Klagegerüst, Beweisantritts- und Log-Anforderung.

## Inhalt

- `skills/phishing-vorfall-pruefen/SKILL.md` - geführter Hauptworkflow.
- `references/rechtsrahmen.md` - Arbeitsrahmen mit amtlichen Normlinks.
- `assets/checklisten/` - Intake, Beweis- und Logmatrix, grobe-Fahrlässigkeit-Ampel.
- `assets/vorlagen/` - Bankaufforderung, Ombudsmann-Antrag, Klagegerüst.
- `scripts/phishing_case_gate.py` - kleines Offline-Gate für strukturierte Fallbewertung.

## Arbeitsprinzip

Das Plugin entscheidet keinen Fall automatisch. Es zwingt zur sauberen Trennung:

- Hat der Kunde den konkreten Zahlungsvorgang autorisiert?
- Liegt ein Einwand aus § 675v BGB vor?
- Was ist bewiesen, was nur behauptet?
- Welche Banklogs müssen verlangt werden?
- Ist Schlichtung, Teilvergleich oder Klage der bessere nächste Schritt?

Alle rechtlichen Bewertungen sind Arbeitsentwürfe und müssen durch eine qualifizierte Person geprüft werden.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | phishing-vorfall-pruefer: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme und A... |
| `kompendium-02-workflow-mandantenko-bis-phishing-tan-verfahr` | phishing-vorfall-pruefer: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-mandantenkommunikation, workflow-redteam-qualitygate, phishing-tan-verfahren-vergleich) und bewahrt deren Workflows, Normanker, Prüfp... |
| `kompendium-03-spezial-klage-friste-bis-phish-banking-trojan` | phishing-vorfall-pruefer: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (spezial-klage-fristennotiz-und-naechster-schritt, spezial-vorfall-fristen-form-und-zustaendigkeit, phish-banking-trojaner-haftung-spezial) und... |
| `kompendium-04-phishing-arbeitnehme-bis-phish-ceo-fraud-konz` | phishing-vorfall-pruefer: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (phishing-arbeitnehmer-haftung, phishing-bgb-675u-haftung, phish-ceo-fraud-konzern-spezial) und bewahrt deren Workflows, Normanker, Prüfprogram... |
| `kompendium-05-phish-incident-triag-bis-phishing-arten-erken` | phishing-vorfall-pruefer: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (phish-incident-triage-bauleiter, phish-meldepflichten-leitfaden, phishing-arten-erkennen) und bewahrt deren Workflows, Normanker, Prüfprogramm... |
| `kompendium-06-phishing-aufsicht-ba-bis-phishing-banking-app` | phishing-vorfall-pruefer: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (phishing-aufsicht-bafin, phishing-bank-strategie, phishing-banking-app-malware) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausg... |
| `kompendium-07-phishing-bea-notfall-bis-phishing-erstkontakt` | phishing-vorfall-pruefer: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (phishing-bea-notfall-anwalt, phishing-bgb-675v-grobfahrlaessig, phishing-erstkontakt-mandant) und bewahrt deren Workflows, Normanker, Prüfprog... |
| `kompendium-08-phishing-faelle-rent-bis-phishing-mit-geschae` | phishing-vorfall-pruefer: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (phishing-faelle-rentner, phishing-kryptowaehrung-recovery, phishing-mit-geschaeftskonto) und bewahrt deren Workflows, Normanker, Prüfprogramme... |
| `kompendium-09-phishing-praevention-bis-phishing-supply-chai` | phishing-vorfall-pruefer: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (phishing-praeventionscheckliste, phishing-strafanzeige-vorbereiten, phishing-supply-chain-bec) und bewahrt deren Workflows, Normanker, Prüfpro... |
| `kompendium-10-phishing-versicherer-bis-phishing-zivilklage` | phishing-vorfall-pruefer: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (phishing-versicherer-cyber, phishing-vorfall-pruefen, phishing-zivilklage-bank) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausg... |
| `kompendium-11-spezial-675u-verhand-bis-spezial-banking-beho` | phishing-vorfall-pruefer: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (spezial-675u-verhandlung-vergleich-und-eskalation, spezial-675w-zahlen-schwellen-und-berechnung, spezial-banking-behoerden-gericht-und-registe... |
| `kompendium-12-spezial-bankpflichte-bis-spezial-bgb-schrifts` | phishing-vorfall-pruefer: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (spezial-bankpflichten-beweislast-und-darlegungslast, spezial-beweislast-mandantenkommunikation-entscheidungsvorlage, spezial-bgb-schriftsatz-b... |
| `kompendium-13-spezial-call-mehrpar-bis-spezial-freistehende` | phishing-vorfall-pruefer: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (spezial-call-mehrparteien-konflikt-und-interessen, spezial-faelle-abschlussprodukt-und-uebergabe, spezial-freistehender-erstpruefung-und-manda... |
| `kompendium-14-spezial-grobe-formul-bis-spezial-phishing-tat` | phishing-vorfall-pruefer: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (spezial-grobe-formular-portal-und-einreichung, spezial-online-risikoampel-und-gegenargumente, spezial-phishing-tatbestand-beweis-und-belege) u... |
| `kompendium-15-spezial-pruefer-doku-bis-spezial-schlichtung` | phishing-vorfall-pruefer: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (spezial-pruefer-dokumentenmatrix-und-lueckenliste, spezial-pushtan-compliance-dokumentation-und-akte, spezial-schlichtung-sonderfall-und-edge-... |
| `kompendium-16-spezial-spoofing-int-bis-spezial-spoofing-int` | phishing-vorfall-pruefer: Konsolidiertes Skill-Kompendium 16; bündelt 1 frühere Spezialskills (spezial-spoofing-internationaler-bezug-und-schnittstellen) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-675v-livequellen-und-rechtsprechungscheck` | 675V: Livequellen- und Rechtsprechungscheck im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-fahrlaessigkeit-red-team-und-qualitaetskontrolle` | Fahrlaessigkeit: Red-Team und Qualitätskontrolle im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin phishing-vorfall-pruefer: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin phishing-vorfall-pruefer: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin phishing-vorfall-pruefer: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin phishing-vorfall-pruefer: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin phishing-vorfall-pruefer: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin phishing-vorfall-pruefer: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
