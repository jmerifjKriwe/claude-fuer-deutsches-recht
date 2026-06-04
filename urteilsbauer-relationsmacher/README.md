# Urteilsbauer und Relationsmacher

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`urteilsbauer-relationsmacher`) | [`urteilsbauer-relationsmacher.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/urteilsbauer-relationsmacher.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Solis Vision X Smartglasses** (`solis-vision-x-smartglasses`) | [Gesamt-PDF lesen](../testakten/solis-vision-x-smartglasses/gesamt-pdf/solis-vision-x-smartglasses_gesamt.pdf) | [`testakte-solis-vision-x-smartglasses.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-solis-vision-x-smartglasses.zip) |
| **Werklohnklage Radarwarner GmbH ./. Schreinmoor Bauträger AG — Rohbaumängel Wohnanlage Spreebogen Plagwitz, Hilfsaufrechnung, Beweiswürdigung SV-Gutachten, Urteil § 313 ZPO** (`urteilsbau-zivilkammer-leipzig-werklohn-radarwarner-relation-mit-beweiswuerdigung-und-urteil`) | [Gesamt-PDF lesen](../testakten/urteilsbau-zivilkammer-leipzig-werklohn-radarwarner-relation-mit-beweiswuerdigung-und-urteil/gesamt-pdf/urteilsbau-zivilkammer-leipzig-werklohn-radarwarner-relation-mit-beweiswuerdigung-und-urteil_gesamt.pdf) | [`testakte-urteilsbau-zivilkammer-leipzig-werklohn-radarwarner-relation-mit-beweiswuerdigung-und-urteil.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-urteilsbau-zivilkammer-leipzig-werklohn-radarwarner-relation-mit-beweiswuerdigung-und-urteil.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Technischer Plugin-Name: `urteilsbauer-relationsmacher`.

Freistehendes Plugin für **Amts-, Land- und Familienrichter sowie Rechtspfleger**. Begleitet von der Aktenintake über die Relation und die Beweiswürdigung mit Richter-Input bis zum fertigen Urteil oder Beschluss inklusive Tenor, Tatbestand, Entscheidungsgründen, Kosten- und Rechtsmittelbelehrung. Erzeugt am Ende ein DOCX nach § 313 ZPO.

## Installation

1. Claude Code oder Claude Desktop/Cowork öffnen.
2. **Customize Plugins** bzw. **Personal plugins** wählen.
3. **Install from .zip** und `urteilsbauer-relationsmacher.zip` hochladen.
4. Mit einem konkreten Auftrag starten, zum Beispiel: `Starte die Relation fuer eine Werklohnklage. Akte liegt vor.`

Alternativ via Marketplace:

```
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install urteilsbauer-relationsmacher@claude-fuer-deutsches-recht
```

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

## Skill-Landkarte

| Skill | Zweck |
| --- | --- |
| `aktenintake-zivil` | Erfasst Parteien, Anträge, Sachverhalt, Streitwert, Anlagen und Lage. |
| `zulaessigkeit-pruefen` | Pruft Statthaftigkeit, Zuständigkeit, Partei- und Prozessfähigkeit, Rechtsschutzbedürfnis. |
| `relation-zivil` | Baut Relation aus Klagegrund und Verteidigung mit Streitstand und Beweislage. |
| `vollrelation-langfassung` | Liefert die ausführliche Vollrelation mit Hilfserwaegungen und Eventualbegründung. |
| `anspruchsgrundlagen-pruefen` | Identifiziert und subsumiert die einschlaegigen Anspruchsgrundlagen. |
| `kollidierende-agb-pruefen` | Loest AGB-Konflikt nach Restguelitgkeits- und Knock-out-Doktrin. |
| `cisg-pruefen` | Pruft CISG-Anwendbarkeit, Anspruechs- und Aufrechnungslage. |
| `internationales-privatrecht` | Klärt anwendbares Recht nach Rom I/II und nationalem IPR. |
| `incoterms-und-gefahruebergang` | Wendet Incoterms 2020 auf Gefahrübergang und Transportkosten an. |
| `dsgvo-rechtswidriges-produkt` | Beurteilt DSGVO-Verstöße durch Produkte mit Datenverarbeitung. |
| `familienrichter-spezifika` | Familienrechtliche Besonderheiten: FamFG-Verfahren, Anhörungspflicht, Vergleichsdruck. |
| `beweisbeschluss-vorbereiten` | Formuliert Beweisthemen, Beweismittel und Beweisanordnung. |
| `beweiswuerdigung-mit-richter-input` | Holt Richter-Input zu Glaubwürdigkeit ein und baut Beweiswürdigung. |
| `tatbestand-zivil-schreiben` | Verfasst Tatbestand mit unstreitigem und streitigem Sachverhalt und Anträgen. |
| `entscheidungsgruende-zivil-schreiben` | Baut Entscheidungsgründe mit Subsumtion und juristischer Begründung. |
| `tenor-bauen-zivil` | Erstellt Tenor mit Hauptsache, Kosten, vorläufiger Vollstreckbarkeit. |
| `kostenentscheidung-bauen` | Berechnet Kostenquote nach §§ 91 ff. ZPO inklusive Vergleichswerten. |
| `vorlaeufige-vollstreckbarkeit` | Setzt Sicherheitsleistung und Abwendungsbefugnis nach §§ 708 ff. ZPO. |
| `rechtsmittelbelehrung-zivil` | Erzeugt korrekte Rechtsmittelbelehrung für Berufung, Beschwerde, Revision. |
| `beschluss-bauen-zpo` | Baut Beschlüsse statt Urteilen, etwa bei einstweiligem Rechtsschutz oder Streitwertfestsetzung. |
| `berufungsfest-pruefen` | Pruft das Urteil auf Berufungsfestigkeit und typische Aufhebungsgründe. |
| `revisionsfest-pruefen` | Pruft Urteil auf revisionsrechtliche Schwachstellen. |
| `dokumente-rendern-urteil-docx` | Rendert das fertige Urteil als DOCX nach § 313 ZPO. |
| `schulung-urteilsbauer` | Trainingsskill zur Einarbeitung neuer Richter und Rechtspfleger. |

## Typische Workflows

- Aktenintake -> Zulässigkeit -> Relation -> Anspruchsgrundlagen -> Beweisbeschluss.
- Beweiswürdigung mit Richter-Input -> Tatbestand -> Entscheidungsgründe -> Tenor.
- Kostenentscheidung -> Vorläufige Vollstreckbarkeit -> Rechtsmittelbelehrung.
- Berufungs-/Revisionsfestigkeit -> DOCX-Rendering nach § 313 ZPO.

## Haftung

Dieses Plugin ist ein Arbeitswerkzeug für die richterliche Praxis. Es ersetzt keine eigene rechtliche Prüfung und keine Beratung durch zugelassene Rechtsanwälte. Die Verantwortung für Tenor, Tatbestand und Entscheidungsgründe bleibt beim Spruchkoerper.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `dokumente-rendern-urteil-docx` | Zivilurteil als DOCX im offiziellen Gerichtslayout rendern: Richter oder Referendar will fertiges Urteil als Dokument ausgeben. Normen: § 313 ZPO (Urteilsinhalt und -form). Prüfraster: Gerichtslayout (Aktenzeichen, Gerichtsbezeichnung, I... |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | urteilsbauer-relationsmacher: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme u... |
| `kompendium-02-spezial-amts-fristen-bis-anspruchsgrundlagen` | urteilsbauer-relationsmacher: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (spezial-amts-fristen-form-und-zustaendigkeit, aktenintake-zivil, anspruchsgrundlagen-pruefen) und bewahrt deren Workflows, Normanker, Prüf... |
| `kompendium-03-berufungsfest-pruefe-bis-beweisbeschluss-vorb` | urteilsbauer-relationsmacher: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (berufungsfest-pruefen, beschluss-bauen-zpo, beweisbeschluss-vorbereiten) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabe... |
| `kompendium-04-beweiswuerdigung-mit-bis-dsgvo-rechtswidriges` | urteilsbauer-relationsmacher: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (beweiswuerdigung-mit-richter-input, cisg-pruefen, dsgvo-rechtswidriges-produkt) und bewahrt deren Workflows, Normanker, Prüfprogramme und... |
| `kompendium-05-entscheidungsgruende-bis-incoterms-und-gefahr` | urteilsbauer-relationsmacher: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (entscheidungsgruende-zivil-schreiben, familienrichter-spezifika, incoterms-und-gefahruebergang) und bewahrt deren Workflows, Normanker, Pr... |
| `kompendium-06-internationales-priv-bis-kostenentscheidung-b` | urteilsbauer-relationsmacher: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (internationales-privatrecht, kollidierende-agb-pruefen, kostenentscheidung-bauen) und bewahrt deren Workflows, Normanker, Prüfprogramme un... |
| `kompendium-07-rechtsmittelbelehrun-bis-revisionsfest-pruefe` | urteilsbauer-relationsmacher: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (rechtsmittelbelehrung-zivil, relation-zivil, revisionsfest-pruefen) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-08-schulung-urteilsbaue-bis-spezial-beschluss-ta` | urteilsbauer-relationsmacher: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (schulung-urteilsbauer, spezial-aktenintake-schriftsatz-brief-und-memo-bausteine, spezial-beschluss-tatbestand-beweis-und-belege) und bewah... |
| `kompendium-09-spezial-entscheidung-bis-spezial-input-compli` | urteilsbauer-relationsmacher: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (spezial-entscheidungsgruende-redaktion, spezial-familienrichter-risikoampel-und-gegenargumente, spezial-input-compliance-dokumentation-und... |
| `kompendium-10-spezial-land-dokumen-bis-spezial-relation-ver` | urteilsbauer-relationsmacher: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (spezial-land-dokumentenmatrix-und-lueckenliste, spezial-rechtspfleger-behoerden-gericht-und-registerweg, spezial-relation-verhandlung-verg... |
| `kompendium-11-spezial-richter-zahl-bis-spezial-tatbestand-f` | urteilsbauer-relationsmacher: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (spezial-richter-zahlen-schwellen-und-berechnung, spezial-richterlicher-hinweis-und-aufklaerung, spezial-tatbestand-formular-portal-und-ein... |
| `kompendium-12-spezial-tatbestandsm-bis-spezial-urteils-erst` | urteilsbauer-relationsmacher: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (spezial-tatbestandsmerkmale-mehrparteien-konflikt-und-interessen, spezial-tenor-internationaler-bezug-und-schnittstellen, spezial-urteils-... |
| `kompendium-13-tatbestand-zivil-sch-bis-urb-mehrere-streitge` | urteilsbauer-relationsmacher: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (tatbestand-zivil-schreiben, tenor-bauen-zivil, urb-mehrere-streitgegenstaende-spezial) und bewahrt deren Workflows, Normanker, Prüfprogram... |
| `kompendium-14-urb-relationstechnik-bis-urb-versaeumnisurtei` | urteilsbauer-relationsmacher: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (urb-relationstechnik-bauleiter, urb-tatbestand-entscheidungsgruende-leitfaden, urb-versaeumnisurteil-einspruch-spezial) und bewahrt deren... |
| `kompendium-15-vollrelation-langfas-bis-zulaessigkeit-pruefe` | urteilsbauer-relationsmacher: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (vollrelation-langfassung, vorlaeufige-vollstreckbarkeit, zulaessigkeit-pruefen) und bewahrt deren Workflows, Normanker, Prüfprogramme und... |
| `spezial-beweiswuerdigung-livequellen-und-rechtsprechungscheck` | Beweiswuerdigung: Livequellen- und Rechtsprechungscheck im Plugin urteilsbauer relationsmacher; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-entscheidungsgruende-red-team-und-qualitaetskontrolle` | Entscheidungsgruende: Red-Team und Qualitätskontrolle im Plugin urteilsbauer relationsmacher; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin urteilsbauer-relationsmacher: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin urteilsbauer-relationsmacher: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin urteilsbauer-relationsmacher: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin urteilsbauer-relationsmacher: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin urteilsbauer-relationsmacher: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin urteilsbauer-relationsmacher: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
