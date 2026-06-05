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
| `675u-675w-banking` | 675u 675w Banking im Plugin Phishing Vorfall Pruefer: prüft konkret 675U, 675W, Banking. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `675v-quellenkarte` | 675v Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `arbeitnehmer-haftung-bgb-675u-phish-ceo` | Arbeitnehmer Haftung BGB 675u Phish CEO im Plugin Phishing Vorfall Pruefer: prüft konkret Phishing am Arbeitsplatz, § 675u BGB Haftung des Zahlungsdienstleisters bei nicht, Spezialfall CEO-Fraud im Konzern. Liefert priorisierten Output m... |
| `aufsicht-bafin-bank-strategie-banking-app` | Aufsicht Bafin Bank Strategie Banking APP im Plugin Phishing Vorfall Pruefer: prüft konkret BaFin-Beschwerde gegen Bank bei verweigerter Rueckbuchung, Anschreiben an Bank bei Phishing-Vorfall, Banking-App-Malware (Anubis, Cerberus. Liefe... |
| `bankpflichten-beweislast-bgb` | Bankpflichten Beweislast BGB im Plugin Phishing Vorfall Pruefer: prüft konkret Bankpflichten, Beweislast, BGB. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `bea-notfall-bgb-675v-erstkontakt-mandant` | BEA Notfall BGB 675v Erstkontakt Mandant im Plugin Phishing Vorfall Pruefer: prüft konkret Phishing gegen Anwalts-beA, § 675v Abs, Erstkontakt Mandant nach Phishing-Vorfall. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel un... |
| `call-interessen-faelle-freistehender` | Call Interessen Faelle Freistehender im Plugin Phishing Vorfall Pruefer: prüft konkret Call, Faelle, Freistehender. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `fahrlaessigkeit-fehlerkatalog` | Fahrlaessigkeit Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `grobe-online-phishing` | Grobe Online Phishing im Plugin Phishing Vorfall Pruefer: prüft konkret Grobe, Online, Phishing. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `klage-fristennotiz-vorfall-phish-banking` | Klage Fristennotiz Vorfall Phish Banking im Plugin Phishing Vorfall Pruefer: prüft konkret Klage, Vorfall, Spezialfall Banking-Trojaner und Haftung bei nicht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schr... |
| `phish-incident-meldepflichten-arten-erkennen` | Phish Incident Meldepflichten Arten Erkennen im Plugin Phishing Vorfall Pruefer: prüft konkret Bauleiter Phishing-Incident-Triage, Leitfaden Meldepflichten Phishing, Phishing-Arten erkennen. Liefert priorisierten Output mit Norm-Pinpoint... |
| `phishing-faelle-rentner-kryptowaehrung` | Faelle Rentner Kryptowaehrung im Plugin Phishing Vorfall Pruefer: prüft konkret Phishing bei aelteren Mandanten, Phishing mit Kryptowaehrung, Phishing gegen Geschaeftskonto. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel un... |
| `phishing-praeventionscheckliste-strafanzeige` | Praeventionscheckliste Strafanzeige im Plugin Phishing Vorfall Pruefer: prüft konkret Praeventionscheckliste fuer Kanzleien und Mandanten, Strafanzeige § 263a StGB (Computerbetrug) vorbereiten, Business Email Compromise (BEC), Rechnungs-... |
| `phishing-spoofing-internationaler-bezug-schnittstellen` | Spoofing Internationaler Bezug Schnittstellen im Plugin Phishing Vorfall Pruefer: fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |
| `phishing-tan` | TAN im Plugin Phishing Vorfall Pruefer: prüft konkret Mandantenkommunikation im Plugin phishing-vorfall-pruefer, Red-Team Qualitygate im Plugin phishing-vorfall-pruefer, TAN-Verfahren vergleichen aus Haftungssicht. Liefert priorisierten... |
| `phishing-vorfall-pruefer-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `phishing-vorfall-pruefer-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `phishing-vorfall-pruefer-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `phishing-vorfall-pruefer-output-waehlen` | Output wählen im Plugin Phishing Vorfall Pruefer: Diese Output-Weiche für Phishing Vorfall Prüfer entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `phishing-vorfall-pruefer-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `phishing-vorfall-pruefer-start-chronologie-fristen` | Start Chronologie Fristen im Plugin Phishing Vorfall Pruefer: prüft konkret Einstieg, Schnelltriage und Fallrouting im Phishing Vorfall, Chronologie und Belegmatrix im Plugin, Fristen- und Risikoampel im Plugin phishing-vorfall-pruefer.... |
| `phishing-vorfall-pruefer-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `pushtan-schlichtung-sonderfall` | Pushtan Schlichtung Sonderfall im Plugin Phishing Vorfall Pruefer: prüft konkret Pruefer, Pushtan, Schlichtung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `versicherer-cyber-phishing-vorfall-zivilklage` | Versicherer Cyber Phishing Vorfall Zivilklage im Plugin Phishing Vorfall Pruefer: prüft konkret Cyberversicherung pruefen, Prüft Phishing-Vorfall im Online-Banking oder, Zivilklage gegen Bank wenn Rueckbuchung verweigert. Liefert prioris... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
