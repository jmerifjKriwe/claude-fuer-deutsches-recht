# Legistik-Werkstatt

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`legistik-werkstatt`) | [`legistik-werkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/legistik-werkstatt.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Elektronisches Pflichtpostfach** (`legistik-pflichtpostfach`) | [Gesamt-PDF lesen](../testakten/legistik-pflichtpostfach/gesamt-pdf/legistik-pflichtpostfach_gesamt.pdf) | [`testakte-legistik-pflichtpostfach.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-legistik-pflichtpostfach.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Vollständige Werkstatt für Legistinnen und Legisten in Bundesministerien, Bundestag, Fraktionen, Oppositionsarbeit, Landesministerien, Landtagen sowie kommunalen und kammerlichen Normgebern. Vom politischen Auftrag über Startbahn, Normhierarchie, Kompetenzprüfung, Normenkartierung und Terminologie zu Referentenentwurf, Kabinettsmappe, Gesetzentwurf aus der Mitte des Bundestages oder Landtages, Änderungsantrag, Entschließungsantrag, Antrag, Formulierungshilfe, Rechtsverordnung und Satzung. Mit Querschnittsprüfungen Verfassungsrecht Europarecht Folgenabschätzung Goldplating Bestimmtheit Zirkelschluss. Erzeugt am Ende ein DOCX und PDF im passenden offiziellen Layout - ministerieller Referentenentwurf-Stil, BT-/Landtagsdrucksachen-Stil oder Arbeitsfassung für Fraktion, Ausschuss und Normgeber.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Was kann das Plugin?

Das Plugin deckt **alle Normebenen** ab:

- Bundesgesetz (Stammgesetz, Mantelgesetz, Änderungsgesetz)
- Landesgesetz
- Rechtsverordnung des Bundes und der Länder (Art. 80 GG, Landesverfassungen)
- Satzungen von Kommunen, Kammern und Hochschulen (Art. 28 Abs. 2 GG, Selbstverwaltung)
- Sekundärrechtsdurchführung und Notifizierung
- parlamentarischer Antrag, Entschließungsantrag, Änderungsantrag und Gesetzentwurf aus der Mitte des Bundestages oder Landtages

Das Plugin arbeitet mit **fünf Startbahnen**:

- Bundesressort / Bundesregierung: Referentenentwurf, Ressortabstimmung, NKR, Kabinett, Bundesrat, Bundestag
- Bundestag / Fraktion / Abgeordnete: Gesetzentwurf aus der Mitte, Änderungsantrag, Antrag, Entschließungsantrag, Ausschussfassung
- Landesressort / Landesregierung: Landesreferentenentwurf, Landesverordnung, Kabinetts- und Landtagsweg
- Landtag / Landtagsfraktion: landesspezifischer Gesetzentwurf, Änderungsantrag, Antrag, Entschließungsantrag
- sonstiger Normgeber: kommunale Satzung, Kammerrecht, Hochschulsatzung, Beschlussvorlage, Bekanntmachung

Das Plugin prüft **immer**:

- Verfassungsrecht (GG, Landesverfassungen, BVerfG-Rechtsprechung)
- Europarecht (Primärrecht, Sekundärrecht, Notifizierung 2015/1535)
- Folgen (Erfüllungsaufwand, Bürokratiekosten, Nachhaltigkeit, KMU-Test)
- Goldplating und Wesentlichkeit
- Bestimmtheit, Terminologie und Zirkelschluss

Am Ende erzeugt es ein **lieferfertiges DOCX und PDF** im offiziellen Layout:

- **Referentenentwurf** (Arial 11pt, Bearbeitungsstand-Kopf, A-F-Vorblatt)
- **BT-Drucksache** (Times New Roman 11pt, Drucksachennummer + Wahlperiode in der Kopfzeile, Sperrsatz für Hauptüberschriften, Anschreiben des Bundeskanzlers)
- **Formulierungshilfe / parlamentarische Vorlage** (für Koalition, Opposition, Ausschuss oder Ministerialzulieferung)
- **Antrag / Entschließungsantrag** (beschlussreif, mit Begründung und Kurzvermerk)
- **Synopse** (dreispaltig)
- **Lesefassung** (konsolidiert nach Inkrafttreten)
- **Kabinettsmappe** (Deckblatt + Anlagenverzeichnis)

## Skill-Tabelle

| Phase | Skill | Zweck |
| --- | --- | --- |
| Auftrag | `legistik-auftragsaufnahme` | Startbahn, Institution, formalen Initiator und Regelungsauftrag übersetzen |
| Normhierarchie | `normhierarchie-routing` | Regierung vs Parlament; Gesetz vs Verordnung vs Satzung vs Antrag; Bund vs Land |
| Kompetenz | `gesetzgebungskompetenz-pruefen` | Art. 70 bis 74 GG, Erforderlichkeit |
| Kompetenz | `verordnungsermaechtigung-art80` | Inhalt Zweck Ausmass nach Art. 80 GG |
| Kompetenz | `satzungskompetenz-pruefen` | Art. 28 Abs. 2 GG, Kammern, Hochschulen |
| Mapping | `normenkartierung` | Verweisnetz und Änderungsstellen |
| Sprache | `terminologie-konsistenz` | Begriffsbrüche aufspüren |
| Sprache | `zirkelschluss-pruefen` | Verweisgraf zykelfrei |
| Entwurf | `referentenentwurf-bauen` | Vollformat des Bundes- oder Landes-Referentenentwurfs |
| Entwurf | `formulierungshilfe-bauen` | Formulierungshilfe, Änderungsantrag, Gesetzentwurf aus der Mitte, Antrag oder Entschließungsantrag |
| Entwurf | `gesetzesentwurf-kabinett` | Kabinettsmappe |
| Entwurf | `begruendung-allgemein-und-besonders` | Teil A I-VII und Teil B |
| Entwurf | `synopse-erstellen` | Dreispaltige Synopse |
| Entwurf | `lesefassung-konsolidiert` | Konsolidierte Fassung nach Inkrafttreten |
| Entwurf | `xml-paralleldarstellung` | LegalDocML.de und eNorm |
| Prüfung | `europarechtskonformitaet` | Primärrecht Sekundärrecht Notifizierung |
| Prüfung | `goldplating-vermeiden` | Überschießende Umsetzung von Unionsrecht |
| Prüfung | `verfassungsmaessigkeit-quercheck` | Grundrechte Verhältnismäßigkeit Bestimmtheit |
| Folgen | `folgenabschaetzung-erfuellungsaufwand` | Erfüllungsaufwand quantifizieren |
| Folgen | `folgenabschaetzung-nachhaltigkeit` | SDGs Klima Generationengerechtigkeit |
| Inkrafttreten | `inkrafttreten-uebergangsrecht` | Zeitpunkt Übergang Verkündung |
| Beteiligung | `verbaendeanhoerung-ressortabstimmung` | Anhörung und Abstimmung |
| Beteiligung | `normenkontrollrat-kmu-check` | NKR-Stellungnahme einholen |
| Lieferung | `dokumente-rendern-docx-pdf` | DOCX und PDF im offiziellen Layout |
| Schulung | `schulung-legistik` | Trainerleitfaden für Schulungen |

Insgesamt **26 Skills**.

## Beispielprojekt - Pflichtpostfachgesetz

Das Repository enthält eine vollständige Arbeitsakte unter `testakten/legistik-pflichtpostfach/`. Sie simuliert den Weg von der politischen Vorgabe (Koalitionsvertrag) zum lieferfertigen Referentenentwurf eines neuen Stammgesetzes über das elektronische Pflichtpostfach für HReg-Gesellschaften und sehr große Online-Plattformen.

So erzeugen Sie die fertigen Dokumente:

```bash
cd claude-fuer-deutsches-recht
python3 legistik-werkstatt/skills/dokumente-rendern-docx-pdf/assets/render.py \
  --format referentenentwurf \
  --eingabe testakten/legistik-pflichtpostfach/eingang \
  --ausgabe testakten/legistik-pflichtpostfach/output

python3 legistik-werkstatt/skills/dokumente-rendern-docx-pdf/assets/render.py \
  --format bt-drucksache \
  --eingabe testakten/legistik-pflichtpostfach/eingang \
  --ausgabe testakten/legistik-pflichtpostfach/output
```

Voraussetzung: `pip install python-docx pyyaml`. Für die PDF-Konvertierung zusätzlich LibreOffice (`soffice`).

## Disclaimer

Dieses Plugin ist ein Werkzeug zur Beschleunigung legistischer Arbeit. Es ersetzt nicht die juristische Prüfung durch verantwortliche Fachreferentinnen und Fachreferenten und nicht die Prüfung durch die Ressortleitung und das Bundesministerium der Justiz im Rahmen der Rechtsförmlichkeitsprüfung.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 30 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `dokumente-rendern-docx-pdf` | Legistische Dokumente als DOCX oder PDF im offiziellen Erscheinungsbild der Bundesregierung, des Bundestages, eines Landes oder eines Landtags rendern. Anwendungsfall fertiger Entwurf soll als lieferfähiges Dokument nach Handbuch der Rec... |
| `kompendium-01-allgemein-bis-spezial-bundestag-fr` | legistik-werkstatt: Konsolidiertes Skill-Kompendium 01; bündelt 8 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel, legw-bmleh-oekolandbau-und-pflanzenschutzrecht, legw-aa-eu-grundl... |
| `kompendium-02-gesetzesentwurf-kabi-bis-legw-bmf-zoll-und-au` | legistik-werkstatt: Konsolidiertes Skill-Kompendium 02; bündelt 8 frühere Spezialskills (gesetzesentwurf-kabinett, legw-aa-voelkerrecht-und-vertragsgesetzgebung, referentenentwurf-bauen, legw-aa-sanktionsumsetzung-und-internationale-abko... |
| `kompendium-03-legw-ressort-bmf-bis-gesetzgebungskompete` | legistik-werkstatt: Konsolidiertes Skill-Kompendium 03; bündelt 8 frühere Spezialskills (legw-ressort-bmf, verbaendeanhoerung-ressortabstimmung, begruendung-allgemein-und-besonders, europarechtskonformitaet, folgenabschaetzung-erfuellung... |
| `kompendium-04-goldplating-vermeide-bis-legw-bmas-sozialvers` | legistik-werkstatt: Konsolidiertes Skill-Kompendium 04; bündelt 8 frühere Spezialskills (goldplating-vermeiden, inkrafttreten-uebergangsrecht, legistik-auftragsaufnahme, legw-aa-ausfuhrkontrolle-und-aussenwirtschaftsdimension, legw-aa-ko... |
| `kompendium-05-legw-bmas-teilhabe-u-bis-legw-bmds-digitale-v` | legistik-werkstatt: Konsolidiertes Skill-Kompendium 05; bündelt 8 frühere Spezialskills (legw-bmas-teilhabe-und-schwerbehindertenrecht-sgb-ix, legw-bmbfsfj-familien-und-elterngeldrecht, legw-bmbfsfj-gleichstellungs-und-antidiskriminierun... |
| `kompendium-06-legw-bmds-it-sicherh-bis-legw-bmftr-hochschul` | legistik-werkstatt: Konsolidiertes Skill-Kompendium 06; bündelt 8 frühere Spezialskills (legw-bmds-it-sicherheit-und-bsig, legw-bmds-ki-verordnung-und-aufsichtsstruktur, legw-bmds-verwaltungsdigitalisierung-und-registermodernisierung, le... |
| `kompendium-07-legw-bmftr-kuenstlic-bis-legw-bmi-auslaender` | legistik-werkstatt: Konsolidiertes Skill-Kompendium 07; bündelt 8 frühere Spezialskills (legw-bmftr-kuenstliche-intelligenz-und-technikregulierung, legw-bmftr-raumfahrt-und-weltraumrecht-wrgg, legw-bmg-arzneimittel-und-medizinprodukterec... |
| `kompendium-08-legw-bmi-bevoelkerun-bis-legw-bmjv-zivilrecht` | legistik-werkstatt: Konsolidiertes Skill-Kompendium 08; bündelt 8 frühere Spezialskills (legw-bmi-bevoelkerungsschutz-und-katastrophenrecht, legw-bmi-oeffentlicher-dienst-und-beamtenrecht, legw-bmi-sicherheits-und-polizeirecht, legw-bmjv... |
| `kompendium-09-legw-bmleh-agrar-und-bis-legw-bmukn-naturschu` | legistik-werkstatt: Konsolidiertes Skill-Kompendium 09; bündelt 8 frühere Spezialskills (legw-bmleh-agrar-und-foerderungsrecht-gak-gap, legw-bmleh-forst-und-jagdrecht, legw-bmleh-lebensmittelrecht-und-futtermittelrecht, legw-bmleh-tiersc... |
| `kompendium-10-legw-bmukn-wasser-un-bis-legw-bmvg-nato-und-s` | legistik-werkstatt: Konsolidiertes Skill-Kompendium 10; bündelt 8 frühere Spezialskills (legw-bmukn-wasser-und-bodenschutzrecht, legw-bmv-luft-und-luftverkehrsrecht, legw-bmv-mobilitaets-und-fuehrerscheinrecht, legw-bmv-schienen-und-bahn... |
| `kompendium-11-legw-bmvg-reserviste-bis-legw-bmwe-wettbewerb` | legistik-werkstatt: Konsolidiertes Skill-Kompendium 11; bündelt 8 frühere Spezialskills (legw-bmvg-reservisten-und-zivilschutzrecht, legw-bmvg-verteidigungstechnologie-export, legw-bmvg-wehrrecht-und-soldatenstatus, legw-bmwe-aussenwirts... |
| `kompendium-12-legw-bmwsb-bau-und-p-bis-legw-bmz-internation` | legistik-werkstatt: Konsolidiertes Skill-Kompendium 12; bündelt 8 frühere Spezialskills (legw-bmwsb-bau-und-planungsrecht-baugb-baunvo, legw-bmwsb-bauproduktenrecht-und-technische-normen, legw-bmwsb-energetische-sanierung-und-geg, legw-b... |
| `kompendium-13-legw-bmz-menschenrec-bis-legw-ressort-bmbfsfj` | legistik-werkstatt: Konsolidiertes Skill-Kompendium 13; bündelt 8 frühere Spezialskills (legw-bmz-menschenrechte-in-lieferketten-lksg, legw-bmz-multilaterale-zusammenarbeit-und-eu, legw-eu-richtlinienumsetzung-spezial, legw-rechtsbereini... |
| `kompendium-14-legw-ressort-bmds-bis-legw-ressort-bmv` | legistik-werkstatt: Konsolidiertes Skill-Kompendium 14; bündelt 8 frühere Spezialskills (legw-ressort-bmds, legw-ressort-bmftr, legw-ressort-bmg, legw-ressort-bmi, legw-ressort-bmjv und 3 weitere) und bewahrt deren Workflows, Normanker,... |
| `kompendium-15-legw-ressort-bmvg-bis-legw-ressortaufgaben` | legistik-werkstatt: Konsolidiertes Skill-Kompendium 15; bündelt 8 frühere Spezialskills (legw-ressort-bmvg, legw-ressort-bmwe, legw-ressort-bmwsb, legw-ressort-bmz, legw-ressort-router und 3 weitere) und bewahrt deren Workflows, Normanke... |
| `kompendium-16-legw-ressortaufgaben-bis-legw-ressortaufgaben` | legistik-werkstatt: Konsolidiertes Skill-Kompendium 16; bündelt 8 frühere Spezialskills (legw-ressortaufgaben-bmds, legw-ressortaufgaben-bmf, legw-ressortaufgaben-bmftr, legw-ressortaufgaben-bmg, legw-ressortaufgaben-bmi und 3 weitere) u... |
| `kompendium-17-legw-ressortaufgaben-bis-legw-rmap-entscheidu` | legistik-werkstatt: Konsolidiertes Skill-Kompendium 17; bündelt 8 frühere Spezialskills (legw-ressortaufgaben-bmv, legw-ressortaufgaben-bmvg, legw-ressortaufgaben-bmwe, legw-ressortaufgaben-bmwsb, legw-ressortaufgaben-bmz und 3 weitere)... |
| `kompendium-18-legw-rmap-evaluierun-bis-lesefassung-konsolid` | legistik-werkstatt: Konsolidiertes Skill-Kompendium 18; bündelt 8 frühere Spezialskills (legw-rmap-evaluierung-und-aenderung, legw-rmap-export-und-systemintegration, legw-rmap-grundlagen, legw-rmap-norm-zu-rulemap, legw-rmap-tatbestand-u... |
| `kompendium-19-normenkartierung-bis-spezial-kabinettsent` | legistik-werkstatt: Konsolidiertes Skill-Kompendium 19; bündelt 8 frühere Spezialskills (normenkartierung, normenkontrollrat-kmu-check, normhierarchie-routing, satzungskompetenz-pruefen, schulung-legistik und 3 weitere) und bewahrt deren... |
| `kompendium-20-spezial-laender-beho-bis-spezial-opposition-r` | legistik-werkstatt: Konsolidiertes Skill-Kompendium 20; bündelt 8 frühere Spezialskills (spezial-laender-behoerden-gericht-und-registerweg, spezial-landtage-schriftsatz-brief-und-memo-bausteine, spezial-legistik-erstpruefung-und-mandatsz... |
| `kompendium-21-spezial-referenten-z-bis-zirkelschluss-pruefe` | legistik-werkstatt: Konsolidiertes Skill-Kompendium 21; bündelt 8 frühere Spezialskills (spezial-referenten-zahlen-schwellen-und-berechnung, spezial-vorlagen-mehrparteien-konflikt-und-interessen, synopse-erstellen, terminologie-konsisten... |
| `spezial-baut-livequellen-und-rechtsprechungscheck` | Baut: Livequellen- und Rechtsprechungscheck im Plugin legistik werkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-entschliessungsantraege-red-team-und-qualitaetskontrolle` | Entschliessungsantraege: Red-Team und Qualitätskontrolle im Plugin legistik werkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin legistik-werkstatt: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin legistik-werkstatt: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin legistik-werkstatt: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin legistik-werkstatt: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin legistik-werkstatt: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin legistik-werkstatt: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
