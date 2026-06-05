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
| `case-gegen-grundbuchanalyse` | Case Gegen Grundbuchanalyse im Plugin Immobilienrechtspraxis: prüft konkret Case, Gegen, Grundbuchanalyse. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `case-management-grundbuchanalyse-immo` | Case Management Grundbuchanalyse Immo im Plugin Immobilienrechtspraxis: prüft konkret Fallmanagement für Immobilienrechtsmandate, Grundbuchauszug analysieren, Aufteilungsplan WEG. Liefert priorisierten Output mit Norm-Pinpoints, Risikoam... |
| `immo-bauliche-veraenderung-energieausweis` | Immo Bauliche Veraenderung Energieausweis im Plugin Immobilienrechtspraxis: prüft konkret Bauliche Veraenderung im WEG nach § 20 WEG (Reform 2020), Energieausweis, Gewerbliche Mieter in der Insolvenz. Liefert priorisierten Output mit Nor... |
| `immo-bauvertrag-vob-kaufvertrag-grundstueck` | Immo Bauvertrag VOB Kaufvertrag Grundstueck im Plugin Immobilienrechtspraxis: prüft konkret Bauvertrag nach VOB-B oder BGB §§ 650a ff, Grundstueckskaufvertrag pruefen, Mietkaufvertrag. Liefert priorisierten Output mit Norm-Pinpoints, Ris... |
| `immo-grundschuld-bestellung-makler-honorar` | Immo Grundschuld Bestellung Makler Honorar im Plugin Immobilienrechtspraxis: prüft konkret Grundschuldbestellung, Maklervertrag und Honorar, Wohnungseigentumsrecht Grundlagen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel... |
| `immo-immobilienrechtliche-live-beweislast` | Immo Immobilienrechtliche Live Beweislast im Plugin Immobilienrechtspraxis: prüft konkret Immo, Immobilienrechtliche, Live. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `immo-zwangsversteigerung-frist-naechster` | Immo Zwangsversteigerung Frist Naechster im Plugin Immobilienrechtspraxis: prüft konkret Zwangsversteigerung Verfahren, Immobilienrechtspraxis, Rechtsabteilungen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem... |
| `immobilienrechtspraxis-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `immobilienrechtspraxis-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `immobilienrechtspraxis-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `immobilienrechtspraxis-mandant-redteam-gate` | Mandant Redteam Gate im Plugin Immobilienrechtspraxis: prüft konkret Mandantenkommunikation im Plugin immobilienrechtspraxis, Red-Team Qualitygate im Plugin immobilienrechtspraxis, Rechtsprechung. Liefert priorisierten Output mit Norm-Pi... |
| `immobilienrechtspraxis-output-waehlen` | Output wählen im Plugin Immobilienrechtspraxis: Diese Output-Weiche für Immobilienrechtspraxis entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `immobilienrechtspraxis-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `immobilienrechtspraxis-start-chronologie-fristen` | Start Chronologie Fristen im Plugin Immobilienrechtspraxis: prüft konkret Einstieg, Schnelltriage und Fallrouting im, Chronologie und Belegmatrix im Plugin immobilienrechtspraxis, Fristen- und Risikoampel im Plugin immobilienrechtspraxis... |
| `immobilienrechtspraxis-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `immor-bauvertrag-vob-erbbaurecht-vertrag` | Immor Bauvertrag VOB Erbbaurecht Vertrag im Plugin Immobilienrechtspraxis: prüft konkret Leitfaden Bauvertrag VOB-B und BGB-Bauvertrag §§ 650a ff, Spezialfall Erbbaurechtsvertrag, Bauleiter Grundstueckskaufvertrag. Liefert priorisierten... |
| `immor-bodenrichtwert-betriebskostenabrechnung` | Immor Bodenrichtwert Betriebskostenabrechnung im Plugin Immobilienrechtspraxis: prüft konkret Spezialfall Bodenrichtwert und Bewertung im Erb- und, Betriebskostenabrechnung im Asset- und Property-Management, Betriebskostenabrechnung im I... |
| `klauselschutz-vertragserstellung` | Klauselschutz Vertragserstellung im Plugin Immobilienrechtspraxis: prüft konkret Klauselschutz, Vertragserstellung, Vertragspruefung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `management-mieteranfragen-interessen` | Management Mieteranfragen Interessen im Plugin Immobilienrechtspraxis: prüft konkret Management, Mieteranfragen, Musterbasierte. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `mieteranfragen-bearbeitung-projekt` | Mieteranfragen Bearbeitung Projekt im Plugin Immobilienrechtspraxis: prüft konkret Mieteranfragen im Immobilienportfolio bearbeiten, Projektmethodik für Immobilienrechtsprojekte, Sachverhalt in Immobilienrechtsstreitigkeiten ermitteln. L... |
| `playbook-quellenkarte` | Playbook Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `pruefung-fehlerkatalog` | Prüfung Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `sachverhaltsermittlung-verifikation` | Sachverhaltsermittlung Verifikation im Plugin Immobilienrechtspraxis: prüft konkret Sachverhaltsermittlung, Verifikation, Werkzeuge. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `vertragserstellung-musterbasiert` | Vertragserstellung Musterbasiert im Plugin Immobilienrechtspraxis: prüft konkret Immobilienrechtliche Vertraege auf Musterbasis erstellen, Immobilienrechtliche Vertraege nach standardisiertem, Immobilien Share Deal Grunderwerbsteuer §§ 1... |
| `weg-abrechnung` | WEG Abrechnung im Plugin Immobilienrechtspraxis: fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
