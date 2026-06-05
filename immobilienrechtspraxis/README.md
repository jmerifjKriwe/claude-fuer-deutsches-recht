# Immobilienrechtspraxis

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`immobilienrechtspraxis`) | [`immobilienrechtspraxis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/immobilienrechtspraxis.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Grundstückskauf / Baulast / Mehrfamilienhaus Rosenmündl — Stuttgart-Ost** (`grundstueckskauf-baulast-mehrfamilienhaus-rosenmuendl-stuttgart-ost`) | [Gesamt-PDF lesen](../testakten/grundstueckskauf-baulast-mehrfamilienhaus-rosenmuendl-stuttgart-ost/gesamt-pdf/grundstueckskauf-baulast-mehrfamilienhaus-rosenmuendl-stuttgart-ost_gesamt.pdf) | [`testakte-grundstueckskauf-baulast-mehrfamilienhaus-rosenmuendl-stuttgart-ost.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-grundstueckskauf-baulast-mehrfamilienhaus-rosenmuendl-stuttgart-ost.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Werkzeuge für immobilienrechtliche Rechtsabteilungen — musterbasierte Vertragserstellung mit Klauselschutz; Vertragsprüfung gegen Playbook; Grundbuchanalyse; Sachverhaltsermittlung; Mieteranfragen mit BGH-Verankerung; Case Management; projektbasierte Arbeitsweise mit AVV-Prüfung.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `case-management` | KI-gestütztes Case Management für immobilienrechtliche Vorgänge. Pro Fall werden Akte Korrespondenz Verträge Schriftsätze und Fristen strukturiert dokumentiert und fortgeschrieben. Erzeugt Fallübersicht in Markd… |
| `grundbuchanalyse` | Strukturierte Auswertung großer Mengen Grundbuchdaten — Grundbuchauszüge Flurkarten Baulastenverzeichnis Altlastenkataster. Extrahiert pro Objekt Eigentümerkette Belastungen in Abteilung II und III Rang Löschungse… |
| `mieteranfragen-bearbeitung` | Bearbeitet eingehende mietrechtliche Anfragen — Mietmängelanzeigen Kündigungen Mieterhöhungsverlangen Widersprüche nach § 574 BGB Betriebskosten-Einwendungen Untervermietungsanfragen — und erstellt fundierte Antwo… |
| `projekt-arbeitsweise` | Strukturierte Projekt- und Ordnerarbeit für immobilienrechtliche Rechtsabteilungen statt freihändigem Prompting. Pro Mandat oder Objekt entsteht ein Projekt-Ordner mit fixierten Vorgaben — Playbook Musterverträge K… |
| `sachverhaltsermittlung` | Unterstützt Inhouse-Juristen bei der zeitraubendsten Phase eines Vorgangs — der Sachverhaltsermittlung. Statt sofort den vollen Sachverhalt zu fordern, führt der Skill einen strukturierten Frageprozess in mehreren S… |
| `vertragserstellung-musterbasiert` | Erstellt immobilienrechtliche Verträge strikt auf Basis hausinterner Musterverträge und Term Sheets. Kernregel ist Klauselschutz — vorgegebene Musterklauseln werden NICHT umformuliert. KI füllt nur markierte Platzh… |
| `vertragspruefung-playbook` | Prüft externe Immobilienverträge gegen das hauseigene Playbook der Rechtsabteilung. Drei Ausgaben — Ampelmatrix nach Klauselkatalog, Redline-Empfehlung als chirurgische Tracked Changes und Business-Memo für das Ass… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 25 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein-workflow-chronologie-fristen` | Nutze dies, wenn Allgemein, Workflow Chronologie Und Belegmatrix, Workflow Fristen Und Risikoampel im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Bitte Allgemein, Workflow Chronologie Und Belegmatrix, Workflow... |
| `anschluss-routing` | Nutze dies, wenn Anschluss-Routing im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Ich habe ein neues Thema im Bereich Immobilienrechtspraxis.; Welche Unterlagen brauchen Sie?; Welcher Spezialskill passt?. |
| `case-gegen-grundbuchanalyse` | Nutze dies, wenn Spezial Case Internationaler Bezug Und Schnittstellen, Spezial Gegen Verhandlung Vergleich Und Eskalation, Spezial Grundbuchanalyse Zahlen Schwellen Und Berechnung im Plugin Immobilienrechtspraxis konkret bearbeitet werd... |
| `case-management-grundbuchanalyse-immo` | Nutze dies, wenn Case Management, Grundbuchanalyse, Immo Aufteilungsplan Weg im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Bitte Case Management, Grundbuchanalyse, Immo Aufteilungsplan Weg prüfen.; Erstelle e... |
| `dokumente-intake` | Nutze dies, wenn Dokumentenintake im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Ich lade Unterlagen hoch.; Was fehlt noch?; Bitte Dokumente sortieren.. |
| `einstieg-routing` | Nutze dies, wenn Einstieg und Routing im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Ich habe ein neues Thema im Bereich Immobilienrechtspraxis.; Welche Unterlagen brauchen Sie?; Welcher Spezialskill passt?. |
| `immo-bauliche-veraenderung-energieausweis` | Nutze dies, wenn Immo Bauliche Veraenderung Weg, Immo Energieausweis, Immo Gewerbliche Mieter Konkurs im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Bitte Immo Bauliche Veraenderung Weg, Immo Energieausweis, I... |
| `immo-bauvertrag-vob-kaufvertrag-grundstueck` | Nutze dies, wenn Immo Bauvertrag Vob B, Immo Kaufvertrag Grundstueck, Immo Mietkaufvertrag im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Bitte Immo Bauvertrag Vob B, Immo Kaufvertrag Grundstueck, Immo Mietkau... |
| `immo-grundschuld-bestellung-makler-honorar` | Nutze dies, wenn Immo Grundschuld Bestellung, Immo Makler Honorar, Immo Wohnungseigentum Grundlagen im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Bitte Immo Grundschuld Bestellung, Immo Makler Honorar, Immo W... |
| `immo-immobilienrechtliche-live-beweislast` | Nutze dies, wenn Spezial Immo Abschlussprodukt Und Übergabe, Spezial Immobilienrechtliche Tatbestand Beweis Und Belege, Spezial Live Beweislast Und Darlegungslast im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser:... |
| `immo-zwangsversteigerung-frist-naechster` | Nutze dies, wenn Immo Zwangsversteigerung Verfahren, Spezial Immobilienrechtspraxis Frist Naechster Schritt, Spezial Rechtsabteilungen Fristen Form Und Zustaendigkeit im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslö... |
| `immor-bauvertrag-vob-erbbaurecht-vertrag` | Nutze dies, wenn Immor Bauvertrag Vob Bgb Leitfaden, Immor Erbbaurecht Vertrag Spezial, Immor Grundstueckskaufvertrag Bauleiter im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Bitte Immor Bauvertrag Vob Bgb Lei... |
| `immor-bodenrichtwert-betriebskostenabrechnung` | Nutze dies, wenn Immor Bodenrichtwert Bewertung Spezial, Betriebskostenabrechnung Erstellen Asset Management, Betriebskostenabrechnung Prüfen Asset Management im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Bit... |
| `klauselschutz-vertragserstellung` | Nutze dies, wenn Spezial Klauselschutz Behörden Gericht Und Registerweg, Spezial Vertragserstellung Risikoampel Und Gegenargumente, Spezial Vertragspruefung Schriftsatz Brief Und Memo Bausteine im Plugin Immobilienrechtspraxis konkret be... |
| `management-mieteranfragen-interessen` | Nutze dies, wenn Spezial Management Formular Portal Und Einreichung, Spezial Mieteranfragen Mehrparteien Konflikt Und Interessen, Spezial Musterbasierte Dokumentenmatrix Und Lueckenliste im Plugin Immobilienrechtspraxis konkret bearbeite... |
| `mandantenkommunikation-redteam-qualitygate` | Nutze dies, wenn Workflow Mandantenkommunikation, Workflow Redteam Qualitygate, Spezial Rechtsprechung Mandantenentscheidung im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red... |
| `mieteranfragen-bearbeitung-projekt` | Nutze dies, wenn Mieteranfragen Bearbeitung, Projekt Arbeitsweise, Sachverhaltsermittlung im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Bitte Mieteranfragen Bearbeitung, Projekt Arbeitsweise, Sachverhaltsermi... |
| `output-waehlen` | Nutze dies, wenn Output wählen im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Bitte Output wählen prüfen.; Erstelle eine Arbeitsfassung zu Output wählen.; Welche Normen und Nachweise brauche ich?. |
| `playbook-quellenkarte` | Nutze dies, wenn Playbook Quellenkarte im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Welche amtliche Quelle prüfe ich zuerst?; Gibt es aktuelle Rechtsprechung?; Bitte Fundstellen verifizieren.. |
| `pruefung-fehlerkatalog` | Nutze dies, wenn Prüfung Fehlerkatalog im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.; Welche Frist oder Beweislast übersehe ich?. |
| `quellen-livecheck` | Nutze dies, wenn Rechtsquellen-Livecheck im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Welche amtliche Quelle prüfe ich zuerst?; Gibt es aktuelle Rechtsprechung?; Bitte Fundstellen verifizieren.. |
| `sachverhaltsermittlung-verifikation` | Nutze dies, wenn Spezial Sachverhaltsermittlung Compliance Dokumentation Und Akte, Spezial Verifikation Sonderfall Und Edge Case, Spezial Werkzeuge Erstpruefung Und Mandatsziel im Plugin Immobilienrechtspraxis konkret bearbeitet werden s... |
| `unterlagen-luecken` | Nutze dies, wenn Unterlagen und Lücken im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Ich lade Unterlagen hoch.; Was fehlt noch?; Bitte Dokumente sortieren.. |
| `vertragserstellung-musterbasiert` | Nutze dies, wenn Vertragserstellung Musterbasiert, Vertragspruefung Playbook, Immo Share Deal Grunderwerbsteuer im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Bitte Vertragserstellung Musterbasiert, Vertragspr... |
| `weg-abrechnung` | Nutze dies, wenn Weg Abrechnung Mieterschnittstelle Datenpaket im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Bitte Weg Abrechnung Mieterschnittstelle Datenpaket prüfen.; Erstelle eine Arbeitsfassung zu Weg Ab... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
