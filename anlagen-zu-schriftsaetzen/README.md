# Anlagen zu Schriftsätzen

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`anlagen-zu-schriftsaetzen`) | [`anlagen-zu-schriftsaetzen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/anlagen-zu-schriftsaetzen.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Werkmann ./. K+B — Werklohnklage Lackieranlage Eschweiler — Anlagenkonvolut-Verfahren** (`anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler`) | [Gesamt-PDF lesen](../testakten/anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler/gesamt-pdf/anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler_gesamt.pdf) | [`testakte-anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin ist die Anlagenkanzlei im Kleinen: Es nimmt einen Schriftsatz, einen chaotischen Mandantenordner oder ein schon halb nummeriertes Anlagenpaket und macht daraus eine nachvollziehbare, gerichtstaugliche Anlagenstruktur.

Es hilft besonders dann, wenn nicht einfach „Anlage K1 bis K12“ vorliegt, sondern wenn eine echte Akte lebt: E-Mails mit Anhängen, Scans ohne OCR, Excel-Tabellen, Fotos, Chat-Screenshots, mehrere Vertragsfassungen, fremdsprachige Unterlagen, doppelte Dateien, geschwärzte Drittunterlagen, beA-Grenzen, Verfahrenswechsel und Richterhinweise. Das Plugin führt dann nicht nur eine Nummerierung aus, sondern baut eine Arbeitslogik: Welche Tatsache soll durch welche Anlage belegt werden? Welche Datei gehört wirklich zu K1? Welche Unterlagen sind nur Konvolutbestandteil? Welche Anlage ist zu groß, unleserlich, falsch benannt, doppelt oder im Schriftsatz nicht eingeführt?

## Wofür es gedacht ist

| Situation | Was das Plugin macht | Ergebnis |
| --- | --- | --- |
| Klage/Replik liegt vor, Anlagen sind noch ungeordnet | Schriftsatz lesen, Beweisanker erkennen, K-Nummern vorschlagen, Dateien zuordnen | K1/K2/K3-Reihenfolge, Anlagenverzeichnis, Lückenliste |
| Anlagen sind schon nummeriert, aber niemand traut dem Paket | Prüfmodus: Nummern, Zitate, Dateien, Stempel, Namen, Lesbarkeit und beA-Fähigkeit prüfen | Fehlerprotokoll mit Korrekturplan |
| Mandant liefert Datenraum/ZIP/USB-Stick | Duplikate, Fassungen, Hashes, Dateitypen, Zeitfolge und Relevanz sortieren | Belegmatrix und Nachforderungsliste |
| Eine Anlage ist ein Konvolut | Deckblatt, Untergliederung, interne Seiten-/Dokumentlogik, kurze Erläuterung für Gericht | `Anlage K1` mit `K1.1`, `K1.2`, `K1.3` |
| Elektronische Einreichung steht bevor | Dateinamen, PDF/OCR, Paketgrößen, Anlagenverzeichnis, Prüfvermerk | beA-/ERV-taugliches Versandpaket |

## Der K1-Gedanke

Die erste Anlage ist fast nie nur eine Datei. In großen Verfahren ist `K1` häufig der Orientierungspunkt für das Gericht: Vertrag, Auftrag, Rahmenvereinbarung, Nachtrag, Bestätigungsmail, Protokoll oder Dokumentenfamilie. Das Plugin behandelt `K1` deshalb als Sortierproblem:

1. **Was soll K1 beweisen?** Nicht „alles zum Vertrag“, sondern eine konkrete Tatsache.
2. **Ist K1 Einzelanlage oder Konvolut?** Bei Konvolut: Deckblatt, Reihenfolge, interne Kurzbezeichnungen.
3. **Welche Fassungen gibt es?** Entwurf, unterschriebene Fassung, Scan, OCR-PDF, E-Mail-Anhang, spätere Ergänzung.
4. **Welche Datei ist die gerichtliche Fassung?** Die anderen Fassungen wandern in den internen Hash-/Versionenlog.
5. **Wie wird K1 im Schriftsatz eingeführt?** Der Schriftsatz muss den Tatsachenkern selbst tragen; die Anlage belegt ihn nur.

## Drei Arbeitsmodi

**Auto-Benennung:** Der Schriftsatz enthält noch keine Nummern. Das Plugin liest die Beweisstellen und schlägt die Reihenfolge vor.

**Schriftsatz folgt:** Der Schriftsatz enthält bereits `Anlage K...`-Verweise. Das Plugin sucht die passenden Dateien, erkennt Lücken und meldet Überschüsse.

**Prüfmodus:** Ein fertiges Anlagenpaket wird gegengeprüft: `K7` fehlt, `K12` ist doppelt, `K18` wird im Schriftsatz nie erwähnt, `K23` hat keinen OCR-Text, `K31` enthält ungeschwärzte Drittinformationen.

## Typische Outputs

- Anlagenverzeichnis für Gericht und Kanzleiakte.
- K/B/AST/AG-Nummerierung mit eindeutiger Dateinamenkonvention.
- Konvolutdeckblätter für Sammelanlagen.
- Belegmatrix: Tatsachenbehauptung ↔ Schriftsatzstelle ↔ Anlage ↔ Datei ↔ Status.
- Hash-/Duplikat-/Fassungslog für interne Kontrolle.
- beA-Versandliste mit Paketgrößen, Dateinamen und letzten Prüfpunkten.
- Nachforderungsliste an Mandant oder Sachbearbeitung.
- Berichtigungs- oder Nachreichungsplan nach gerichtlichem Hinweis.

## Wichtig

Anlagen ersetzen keinen Tatsachenvortrag. Wenn eine Behauptung entscheidungserheblich ist, muss sie im Schriftsatz stehen. Die Anlage belegt, erläutert oder vertieft; sie darf nicht der Ort sein, an dem der eigentliche Vortrag versteckt wird.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Besonders wichtige Skills

| Skill | Zweck |
| --- | --- |
| `allgemein` | Kaltstart, Triage, Nummernkreis, Ziel-Schriftsatz, K1-Frage und Routing in die passenden Spezial-Skills. |
| `anlagen-zu-schriftsaetzen` | Hauptworkflow für Auto-Benennung, Schriftsatz-folgt-Modus, Prüfmodus und Reparatur nach Hinweis. |
| `k1-sortierwerkstatt` | Baut aus Vertrag, Nachtrag, Mail, Scan und OCR-Fassung eine klare Leit-Anlage `K1` oder ein K1-Konvolut. |
| `schriftsatz-anlagen-mapping` | Verknüpft Tatsachenvortrag, Schriftsatzstelle, Beweisangebot, Anlage und Datei in einer Belegmatrix. |
| `anlagen-duplikate-versionen-hashlog` | Erkennt Dubletten, Versionen, OCR-Kopien und die maßgebliche gerichtliche Fassung. |
| `bea-paketierung-groessen-und-versandplan` | Plant Dateinamen, Paketgrößen, Teilpakete, Begleitvermerk und Eingangskontrolle. |
| `anlagen-qualitygate-finalcheck` | Letzter strenger Check vor Versand: Nummern, Zitate, Dateien, OCR, Schwärzung, Stempel, Paket. |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 27 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anlagen-qualitygate-finalcheck` | Finaler Red-Team-Check vor Einreichung: Nummern, Schriftsatzverweise, Dateien, Stempel, OCR, Schwärzung, Dateinamen, beA-Paket, Lücken und Begleitvermerk. |
| `anlagen-zu-schriftsaetzen` | Anwalt hat Schriftsatz fertig und muss Anlagen korrekt benennen nummerieren und als PDF-Konvolut aufbereiten. Anlagemanagement gerichtliche Schriftsaetze. Prüfraster: Schriftsatz lesen Beweisstuecke erkennen sortieren beA-konforme Benenn... |
| `kompendium-01-allgemein-bis-workflow-mandantenko` | anlagen-zu-schriftsaetzen: Konsolidiertes Skill-Kompendium 01; bündelt 4 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel, workflow-mandantenkommunikation) und bewahrt deren Workflo... |
| `kompendium-02-workflow-redteam-qua-bis-spezial-gerichtliche` | anlagen-zu-schriftsaetzen: Konsolidiertes Skill-Kompendium 02; bündelt 4 frühere Spezialskills (workflow-redteam-qualitygate, frist-und-eilversand-anlagenpaket, schiedsverfahren-anlagenband-und-datentraeger, spezial-gerichtlichen-fristen... |
| `kompendium-03-spezial-pruefmodus-f-bis-anlagen-aus-mandante` | anlagen-zu-schriftsaetzen: Konsolidiertes Skill-Kompendium 03; bündelt 4 frühere Spezialskills (spezial-pruefmodus-fristennotiz-und-naechster-schritt, anlagen-aus-datenraum-und-sharepoint, anlagen-aus-edv-systemen, anlagen-aus-mandantenm... |
| `kompendium-04-anlagen-bei-berufung-bis-anlagen-duplikate-ve` | anlagen-zu-schriftsaetzen: Konsolidiertes Skill-Kompendium 04; bündelt 4 frühere Spezialskills (anlagen-bei-berufung-revision, anlagen-bei-eilantrag-eu-arrest, anlagen-bilder-screenshots, anlagen-duplikate-versionen-hashlog) und bewahrt... |
| `kompendium-05-anlagen-elektronisch-bis-anlagen-fuer-glaubha` | anlagen-zu-schriftsaetzen: Konsolidiertes Skill-Kompendium 05; bündelt 4 frühere Spezialskills (anlagen-elektronische-dokumente-spezial, anlagen-format-und-dateinamen, anlagen-fuer-bea-versand, anlagen-fuer-glaubhaftmachung) und bewahrt... |
| `kompendium-06-anlagen-haftpflicht-bis-anlagen-prozessual-p` | anlagen-zu-schriftsaetzen: Konsolidiertes Skill-Kompendium 06; bündelt 4 frühere Spezialskills (anlagen-haftpflicht-versicherer, anlagen-konvention-k-b-erlaeutert, anlagen-konvention-mandantenfreundlich, anlagen-prozessual-pruefung-spezi... |
| `kompendium-07-anlagen-quality-chec-bis-anlagen-stempel-und` | anlagen-zu-schriftsaetzen: Konsolidiertes Skill-Kompendium 07; bündelt 4 frühere Spezialskills (anlagen-quality-check-vor-zustellung, anlagen-redaktion-dsgvo-geschgehg, anlagen-schwaerzen-anonymisieren, anlagen-stempel-und-deckblattlogik... |
| `kompendium-08-anlagen-uebergabe-an-bis-anlagen-zur-substant` | anlagen-zu-schriftsaetzen: Konsolidiertes Skill-Kompendium 08; bündelt 4 frühere Spezialskills (anlagen-uebergabe-an-assistenz-und-legal-tech, anlagen-uebersetzungspflicht, anlagen-vorlagepflicht-141-zpo, anlagen-zur-substantiierung-pfli... |
| `kompendium-09-anlagenband-struktur-bis-anlagenmatrix-csv-xl` | anlagen-zu-schriftsaetzen: Konsolidiertes Skill-Kompendium 09; bündelt 4 frühere Spezialskills (anlagenband-strukturieren, anlagenbezug-im-schriftsatz, anlagenkonvolut-konsolidieren, anlagenmatrix-csv-xlsx-aufbau) und bewahrt deren Workf... |
| `kompendium-10-anlagenverzeichnis-g-bis-berufung-beschwerde` | anlagen-zu-schriftsaetzen: Konsolidiertes Skill-Kompendium 10; bündelt 4 frühere Spezialskills (anlagenverzeichnis-gericht-kanzlei-und-intern, anlagenverzeichnis-grundaufbau, bea-paketierung-groessen-und-versandplan, berufung-beschwerde-... |
| `kompendium-11-beweisangebot-anlage-bis-fremdsprachige-anlag` | anlagen-zu-schriftsaetzen: Konsolidiertes Skill-Kompendium 11; bündelt 4 frühere Spezialskills (beweisangebot-anlage-zeugen, emails-chats-screenshots-als-anlagen, excel-tabellen-und-zahlenbeweis, fremdsprachige-anlagen-uebersetzung) und... |
| `kompendium-12-k1-anlagenpaket-aus-bis-mehrparteien-rollen` | anlagen-zu-schriftsaetzen: Konsolidiertes Skill-Kompendium 12; bündelt 4 frühere Spezialskills (k1-anlagenpaket-aus-chaosordner, k1-sortierwerkstatt, massenanlagen-sampling-und-repraesentativitaet, mehrparteien-rollen-und-praefixe) und b... |
| `kompendium-13-nachreichung-bericht-bis-schriftsatz-anlagen` | anlagen-zu-schriftsaetzen: Konsolidiertes Skill-Kompendium 13; bündelt 4 frühere Spezialskills (nachreichung-berichtigung-und-gerichtshinweis, ocr-scan-lesbarkeit-und-beweiswert, original-abschrift-kopie-und-elektronische-fassung, schrif... |
| `kompendium-14-spezial-anlage-red-t-bis-spezial-arial-mandan` | anlagen-zu-schriftsaetzen: Konsolidiertes Skill-Kompendium 14; bündelt 4 frühere Spezialskills (spezial-anlage-red-team-und-qualitaetskontrolle, spezial-anlagen-tatbestand-beweis-und-belege, spezial-anlagenkonvolut-sonderfall-und-edge-ca... |
| `kompendium-15-spezial-baut-beweisl-bis-spezial-excel-schrif` | anlagen-zu-schriftsaetzen: Konsolidiertes Skill-Kompendium 15; bündelt 4 frühere Spezialskills (spezial-baut-beweislast-und-darlegungslast, spezial-benennt-compliance-dokumentation-und-akte, spezial-bereits-abschlussprodukt-und-uebergabe... |
| `kompendium-16-spezial-konform-mehr-bis-spezial-schriftsaetz` | anlagen-zu-schriftsaetzen: Konsolidiertes Skill-Kompendium 16; bündelt 4 frühere Spezialskills (spezial-konform-mehrparteien-konflikt-und-interessen, spezial-konvertiert-zahlen-schwellen-und-berechnung, spezial-oben-formular-portal-und-e... |
| `kompendium-17-spezial-schriftsatz-bis-spezial-word-behoerd` | anlagen-zu-schriftsaetzen: Konsolidiertes Skill-Kompendium 17; bündelt 4 frühere Spezialskills (spezial-schriftsatz-verhandlung-vergleich-und-eskalation, spezial-sortiert-risikoampel-und-gegenargumente, spezial-stempelt-internationaler-b... |
| `kompendium-18-spezial-zuordnung-er-bis-zeitleiste-und-beleg` | anlagen-zu-schriftsaetzen: Konsolidiertes Skill-Kompendium 18; bündelt 2 frühere Spezialskills (spezial-zuordnung-erstpruefung-und-mandatsziel, zeitleiste-und-belegkette) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabem... |
| `spezial-logik-livequellen-und-rechtsprechungscheck` | Logik: Livequellen- und Rechtsprechungscheck im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin anlagen-zu-schriftsaetzen: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin anlagen-zu-schriftsaetzen: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin anlagen-zu-schriftsaetzen: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin anlagen-zu-schriftsaetzen: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin anlagen-zu-schriftsaetzen: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin anlagen-zu-schriftsaetzen: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
