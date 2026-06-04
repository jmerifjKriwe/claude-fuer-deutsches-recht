# Zwangsvollstreckung

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`zwangsvollstreckung`) | [`zwangsvollstreckung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/zwangsvollstreckung.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Vollstreckungsmappe Sparkasse Niederrhein gegen Mueller** (`vollstreckungsmappe-mueller-sparkasse-niederrhein`) | [Gesamt-PDF lesen](../testakten/vollstreckungsmappe-mueller-sparkasse-niederrhein/gesamt-pdf/vollstreckungsmappe-mueller-sparkasse-niederrhein_gesamt.pdf) | [`testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein.zip) |
| **Zwangsvollstreckung Mietrückstand und Raeumung — Eppendorfer Altbau Grewenig — Vollstreckungsmappe Zweite Runde** (`zwangsvollstreckung-mietruekstand-und-raeumung-eppendorfer-altbau-grewenig-vollstreckungsmappe-zweite-runde`) | [Gesamt-PDF lesen](../testakten/zwangsvollstreckung-mietruekstand-und-raeumung-eppendorfer-altbau-grewenig-vollstreckungsmappe-zweite-runde/gesamt-pdf/zwangsvollstreckung-mietruekstand-und-raeumung-eppendorfer-altbau-grewenig-vollstreckungsmappe-zweite-runde_gesamt.pdf) | [`testakte-zwangsvollstreckung-mietruekstand-und-raeumung-eppendorfer-altbau-grewenig-vollstreckungsmappe-zweite-runde.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-zwangsvollstreckung-mietruekstand-und-raeumung-eppendorfer-altbau-grewenig-vollstreckungsmappe-zweite-runde.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Cowork-Plugin für die Zwangsvollstreckung nach §§ 704 ff. ZPO aus allen Titelarten. Es ist ein vollständiger Arbeitsraum für Gläubigeranwalt, Inkasso, Hausverwaltung, Kreditbearbeitung und Insolvenzverwaltung: Titel prüfen, Klausel besorgen, Zustellung organisieren, Mahn- oder Vollstreckungsbescheid online beantragen, PfÜB gegen Bank, Arbeitgeber, Mieter oder Finanzamt entwerfen, Kontensuche § 802l ZPO und Vermögensauskunft beim Gerichtsvollzieher steuern, Mobiliar- und Räumungsaufträge erteilen, aus notarieller Urkunde § 800 ZPO oder Tabellenauszug § 201 InsO vollstrecken, ZVG-Antrag stellen und Schuldnerschutz auf Erinnerung, Vollstreckungsschutz und P-Konto-Bescheinigung beantworten.

## Wofür das Plugin gedacht ist

- Vollstreckung aus allen Titelarten nach § 794 ZPO: Urteil, Versäumnisurteil, Anerkenntnisurteil, Vollstreckungsbescheid, Prozessvergleich, notarielle Unterwerfungsurkunde § 794 Abs. 1 Nr. 5 ZPO, Anwaltsvergleich, Kostenfestsetzungsbeschluss und Tabellenauszug § 201 InsO.
- Mahn- und Vollstreckungsbescheid online über das zentrale Mahnportal (Barcode-Datensatz, EGVP, beA, beN).
- Forderungspfändung nach §§ 829, 835 ZPO gegen Bank (Lohn- oder Kontokonto), Arbeitgeber (§ 850 ZPO mit Tabelle 1.7.2025), Mieter (§ 851b ZPO) und Finanzamt (Erstattungsansprüche).
- Kontensuche § 802l ZPO über das Bundeszentralamt für Steuern und Vermögensauskunft beim zuständigen Gerichtsvollzieher nach § 802c ZPO.
- Mobiliarvollstreckung und Räumungsauftrag § 885 ZPO (vollständig oder Berliner Modell) beim Gerichtsvollzieher.
- Grundstücksvollstreckung aus notarieller Grundschuldurkunde § 800 ZPO: Zwangsversteigerungsantrag § 15 ZVG, Beitrittsantrag, Sicherungs- vs. Eigentümergrundschuld, Rangverhältnisse.
- Insolvenz-Folgevollstreckung aus Tabellenauszug § 201 InsO nach Aufhebung des Verfahrens (Restschuldbefreiungsantrag pendent oder versagt).
- Schuldnerschutz: Erinnerung § 766 ZPO, Vollstreckungsschutz § 765a ZPO, P-Konto-Bescheinigung § 850k ZPO, Räumungsvollstreckungsschutz § 765a ZPO, Drittwiderspruchsklage § 771 ZPO.
- Reform-Stand 2026/2027: ZVollstrDigitG (BT-Drs. 21/4815, Bundestag 19.3.2026 beschlossen). Inkrafttreten Hauptteile 1.10.2026 (neue ZVFV-Formulare, § 829 Abs. 5 ZPO n.F. mit XML-Antrag als führender Form), Kreditinstitute-Pflicht zum sicheren Übermittlungsweg ab 1.10.2027 (§ 173 Abs. 2 Nr. 1 ZPO n.F., eBO/§ 130a Abs. 4 ZPO). § 840 ZPO erlaubt zusätzlich die Drittschuldnererklärung per Post.

## Leitprinzip

Das Plugin arbeitet titelorientiert und drittschuldnerorientiert. Es prüft erst, ob der Titel die richtige Maßnahme trägt (vollstreckbare Ausfertigung, Klausel, Zustellung, Wartefrist, Sicherheitsleistung), dann, ob der Drittschuldner der richtige Ansprechpartner ist (Sitz, Zustellungsweg, Erklärungspflicht, Auskunftsrecht). Erst danach erzeugt es Schriftsätze. Vollstreckungsschutz, P-Konto und Drittwiderspruch werden nicht als Hindernis behandelt, sondern als parallel zu führender Strang mit eigener Aktenlage. Reform-Übergänge (ZVollstrDigitG) werden datumsabhängig gesteuert: bis 30.9.2026 alte ZVFV, ab 1.10.2026 neue ZVFV-Formulare, ab 1.10.2027 sicherer Übermittlungsweg für Kreditinstitute Pflicht.

## Typischer Ablauf

1. Kommandocenter öffnen: Titelart, Schuldner, Drittschuldner, Forderungshöhe, Zustand der Klausel und Zustellung erfassen.
2. Titel-Klausel-Zustellung prüfen: vollstreckbare Ausfertigung, Klausel § 724 ZPO, Zustellungsnachweis § 750 ZPO, Wartefrist § 798 ZPO bei notarieller Urkunde, Sicherheitsleistung.
3. Vorfeld-Recherche: Vermögensauskunft beim Gerichtsvollzieher, Kontensuche § 802l ZPO über BZSt, Schuldnerverzeichnis § 882c ZPO.
4. Maßnahme wählen: PfÜB Bank/Arbeitgeber/Mieter/Finanzamt, Mobiliarvollstreckung, Räumung § 885 ZPO, ZVG-Antrag oder Tabellenauszug § 201 InsO.
5. Schriftsatz erzeugen: ZVFV-Formular (alt bis 30.9.2026 / neu ab 1.10.2026), Drittschuldnerzustellung organisieren, § 840-Erklärung anfordern.
6. Schuldnerseite begleiten: Erinnerung, Vollstreckungsschutz, P-Konto-Sockel berechnen, Drittwiderspruch prüfen.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| zv-kommandocenter | Startet die Zwangsvollstreckung und entscheidet, welche Maßnahme und welcher Skill passt. |
| zv-titel-klausel-zustellung | Prüft vollstreckbare Ausfertigung, Klausel § 724 ZPO und Zustellungsnachweis § 750 ZPO. |
| zv-mahnbescheid-online | Erstellt den Antrag auf Mahnbescheid über das zentrale Mahnportal mit Barcode-Datensatz und EGVP. |
| zv-vollstreckungsbescheid-folge | Steuert Vollstreckungsbescheid, Klausel, Zustellung und Übergang zur Zwangsvollstreckung. |
| zv-pfueb-bank | Entwirft Pfändungs- und Überweisungsbeschluss gegen Bankguthaben mit P-Konto-Behandlung. |
| zv-pfueb-arbeitsentgelt | Pfändet Arbeitseinkommen § 850 ZPO mit Tabelle 1.7.2025, Unterhalts- und Privilegrang. |
| zv-pfueb-mieter-finanzamt | Pfändet Mietzinsforderungen § 851b ZPO und Erstattungsansprüche gegen das Finanzamt. |
| zv-vermoegensauskunft-gv | Beauftragt den Gerichtsvollzieher mit Vermögensauskunft § 802c ZPO und Schuldnerverzeichnis. |
| zv-kontensuche-drittschuldner | Steuert die Kontensuche § 802l ZPO über das Bundeszentralamt für Steuern. |
| zv-notarielle-urkunde-grundschuld | Vollstreckt aus notarieller Grundschuldurkunde § 800 ZPO inkl. Kündigung § 1193 BGB. |
| zv-zvg-antrag-glaeubiger | Stellt Zwangsversteigerungs- und Beitrittsantrag § 15 ZVG aus Gläubigersicht. |
| zv-tabellenauszug-201-inso | Vollstreckt aus Tabellenauszug § 201 InsO nach Aufhebung des Insolvenzverfahrens. |
| zv-mobiliar-gv-auftrag | Erteilt Mobiliarvollstreckungs- und Sachpfändungsauftrag (auch Krypto-Hardware-Wallets). |
| zv-raeumung-885 | Führt Räumungsvollstreckung § 885 ZPO inkl. Berliner Modell und Vollstreckungsschutz. |
| zv-abwehr-schuldner | Erstellt Erinnerung § 766 ZPO, Vollstreckungsschutz § 765a ZPO und Drittwiderspruch § 771 ZPO. |
| zv-vollstreckungsschutz-haertefall-765a | Vertiefter Härtefall-Schutz § 765a ZPO (Suizidgefahr, Schwangerschaft, Obdachlosigkeit, Trauerfall); Antragsformular mit Glaubhaftmachung. **NEU** |
| zv-eu-kontenpfaendung-655-2014 | Europäische Kontenpfändung VO (EU) 655/2014 — grenzüberschreitende vorläufige Sicherung von Bankkonten in der EU (außer Dänemark). **NEU** |
| zv-pfaendungstabelle-2025 | Hält die Pfändungstabelle 1.7.2025 bis 30.6.2026 nach § 850c ZPO bereit. Auto-Warnung des Rechners ab 1.6.2026. |
| zv-elektronische-zustellung-2027 | Steuert sicheren Übermittlungsweg für Kreditinstitute ab 1.10.2027 (ZVollstrDigitG). |

## Werkzeug

`werkzeuge/pfaendungsrechner.py` berechnet den pfändbaren Betrag nach § 850c ZPO mit der Tabelle 1.7.2025 bis 30.6.2026 (BGBl. 2025 I Nr. 110 vom 11.4.2025). Hartcodierte Eckwerte: Grundfreibetrag 1.555,00 EUR, Erhöhung erste Unterhaltspflicht 585,23 EUR, jede weitere bis zur 5. Person 326,04 EUR, Vollpfändungsgrenze 4.766,99 EUR, P-Konto-Sockel 1.560,00 EUR. Pfändbarkeitsquote nach § 850c Abs. 3 ZPO unterhaltsabhängig (7/10 / 5/10 / 4/10 / 3/10 / 2/10 / 1/10). CLI: `python pfaendungsrechner.py --netto 4200 --unterhalt 3` gibt den pfändbaren Betrag, den verbleibenden P-Konto-Sockel und die Tabellenherleitung aus.

## Reform ZVollstrDigitG 2026/2027

| Datum | Was ändert sich |
| --- | --- |
| bis 30.9.2026 | Alte ZVFV-Formulare bleiben gültig, § 829 ZPO unverändert. |
| ab 1.10.2026 | Neue ZVFV-Formulare verbindlich, § 829 Abs. 5 ZPO n.F.: XML-Datensatz wird führend. |
| ab 1.10.2027 | Kreditinstitute müssen sicheren Übermittlungsweg vorhalten (§ 173 Abs. 2 Nr. 1 ZPO n.F., eBO/§ 130a Abs. 4 ZPO). § 840 ZPO-Erklärung weiterhin per Post zulässig. |

## Grenzen

Das Plugin trifft keine unüberprüfte Vollstreckungsentscheidung und ersetzt keine fachliche Prüfung. Bei streitigen Rechtsfragen (Klauselgegenklage § 768 ZPO, Vollstreckungsabwehrklage § 767 ZPO, Drittwiderspruch § 771 ZPO), bei Räumung mit Härtefall, bei ZVG-Anträgen mit Rangstreit und bei grenzüberschreitender Vollstreckung (EU-Kontenpfändungsverordnung Nr. 655/2014, EU-Zustellungs-VO 2020/1784) verlangt es ausdrücklich menschliche Freigabe. Reform-Übergänge ZVollstrDigitG sind datumsabhängig gesteuert und müssen bei jedem Antrag gegen das tatsächliche Inkrafttretensdatum laut BGBl-Verkündung gegengeprüft werden.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | zwangsvollstreckung: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgab... |
| `kompendium-02-workflow-mandantenko-bis-spezial-mahn-fristen` | zwangsvollstreckung: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-mandantenkommunikation, workflow-redteam-qualitygate, spezial-mahn-fristen-form-und-zustaendigkeit) und bewahrt deren Workflows, Normanker... |
| `kompendium-03-spezial-mahnbescheid-bis-zv-kontensuche-dritt` | zwangsvollstreckung: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (spezial-mahnbescheid-fristennotiz-und-naechster-schritt, zv-titel-klausel-zustellung, zv-kontensuche-drittschuldner) und bewahrt deren Workflows, N... |
| `kompendium-04-zv-pfueb-mieter-fina-bis-spezial-arbeit-schri` | zwangsvollstreckung: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (zv-pfueb-mieter-finanzamt, spezial-802l-verhandlung-vergleich-und-eskalation, spezial-arbeit-schriftsatz-brief-und-memo-bausteine) und bewahrt dere... |
| `kompendium-05-spezial-bank-behoerd-bis-spezial-inso-interna` | zwangsvollstreckung: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (spezial-bank-behoerden-gericht-und-registerweg, spezial-haertefall-mandantenkommunikation-entscheidungsvorlage, spezial-inso-internationaler-bezug-... |
| `kompendium-06-spezial-kontenpfaend-bis-spezial-online-absch` | zwangsvollstreckung: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (spezial-kontenpfaendung-formular-portal-und-einreichung, spezial-notar-mehrparteien-konflikt-und-interessen, spezial-online-abschlussprodukt-und-ue... |
| `kompendium-07-spezial-pfueb-risiko-bis-spezial-schuldnersch` | zwangsvollstreckung: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (spezial-pfueb-risikoampel-und-gegenargumente, spezial-raeumung-compliance-dokumentation-und-akte, spezial-schuldnerschutz-beweislast-und-darlegungs... |
| `kompendium-08-spezial-vermoegensau-bis-spezial-vollstreckun` | zwangsvollstreckung: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (spezial-vermoegensauskunft-zahlen-schwellen-und-berechnung, spezial-vollstreckungsbescheid-dokumentenmatrix-und-lueckenliste, spezial-vollstreckung... |
| `kompendium-09-spezial-zpo-tatbesta-bis-zv-abwehr-schuldner` | zwangsvollstreckung: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (spezial-zpo-tatbestand-beweis-und-belege, spezial-zwangsvollstreckung-erstpruefung-und-mandatsziel, zv-abwehr-schuldner) und bewahrt deren Workflow... |
| `kompendium-10-zv-elektronische-zus-bis-zv-kommandocenter` | zwangsvollstreckung: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (zv-elektronische-zustellung-2027, zv-eu-kontenpfaendung-655-2014, zv-kommandocenter) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausg... |
| `kompendium-11-zv-mahnbescheid-onli-bis-zv-notarielle-urkund` | zwangsvollstreckung: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (zv-mahnbescheid-online, zv-mobiliar-gv-auftrag, zv-notarielle-urkunde-grundschuld) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgab... |
| `kompendium-12-zv-pfaendungstabelle-bis-zv-pfueb-bank` | zwangsvollstreckung: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (zv-pfaendungstabelle-2025, zv-pfueb-arbeitsentgelt, zv-pfueb-bank) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-13-zv-raeumung-885-bis-zv-vermoegensauskunf` | zwangsvollstreckung: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (zv-raeumung-885, zv-tabellenauszug-201-inso, zv-vermoegensauskunft-gv) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-14-zv-vollstreckungsbes-bis-zv-zvg-antrag-glaeub` | zwangsvollstreckung: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (zv-vollstreckungsbescheid-folge, zv-vollstreckungsschutz-haertefall-765a, zv-zvg-antrag-glaeubiger) und bewahrt deren Workflows, Normanker, Prüfpro... |
| `kompendium-15-zwv-pfaendung-konto-bis-zwv-vollstreckungsti` | zwangsvollstreckung: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (zwv-pfaendung-konto-arbeitseinkommen-leitfaden, zwv-vollstreckungsschutz-billigkeit-spezial, zwv-vollstreckungstitel-bauleiter) und bewahrt deren W... |
| `kompendium-16-zwv-zwangsversteiger-bis-zwv-zwangsversteiger` | zwangsvollstreckung: Konsolidiertes Skill-Kompendium 16; bündelt 1 frühere Spezialskills (zwv-zwangsversteigerung-grundstueck-spezial) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-765a-red-team-und-qualitaetskontrolle` | 765A: Red-Team und Qualitätskontrolle im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-kontensuche-livequellen-und-rechtsprechungscheck` | Kontensuche: Livequellen- und Rechtsprechungscheck im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin zwangsvollstreckung: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin zwangsvollstreckung: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin zwangsvollstreckung: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin zwangsvollstreckung: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin zwangsvollstreckung: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin zwangsvollstreckung: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
