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

<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **Werkmann ./. K+B — Werklohnklage Lackieranlage Eschweiler — Anlagenkonvolut-Verfahren** (`anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler`) | [Gesamt-PDF lesen](../testakten/anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler/gesamt-pdf/anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

Zuordnung von Anlagen zu gerichtlichen Schriftsätzen. Sortiert PDF/Word/Excel nach Schriftsatz-Logik (Klage/Erwiderung/Replik), konvertiert nach PDF, vergibt K/B/AST/AG, stempelt oben rechts in Arial 12, beA-tauglich, mit Konvolut. Modi: Auto-Benennung, Schriftsatz folgt, Prüfmodus.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Anlagen zu Schriftsätzen (`anlagen-zu-schriftsaetzen`, dieses Plugin) | [anlagen-zu-schriftsaetzen.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/anlagen-zu-schriftsaetzen.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `anlagen-zu-schriftsaetzen` | Zuordnung von Anlagen zu gerichtlichen Schriftsätzen. Liest den Schriftsatz (Klage/Klageerwiderung/Replik), erkennt vorhandene Beweisstücke, sortiert nach Schriftsatz-Logik, konvertiert alles nach PDF, benennt nach … |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 50 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Anlagen Zu Schriftsaetzen-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbei... |
| `anlagen-aus-edv-systemen` | Anlagen aus IT-Systemen (ERP-Auszuege, Datenbankexporte, Logdateien): Beweiskraft, Manipulationsschutz, Hashverfahren, Begleitvermerk Erstellung. Empfehlung: Export mit Zeitstempel, Hashprotokoll, ggf. Sachverstaendigenanhoerung Authenti... |
| `anlagen-aus-mandantenmaterial` | Mandantenmaterial in Anlagen umwandeln: Posteingang, E-Mails, PDFs, Vertraege, Rechnungen, Korrespondenz. Markiert geschwaerzte Stellen, prueft Vollstaendigkeit, schlaegt sinnvolle Kuerzungen vor. Erkennt vertrauliche Inhalte, die fuer d... |
| `anlagen-bei-berufung-revision` | Anlagen in Berufung und Revision: bisheriges Anlagenverzeichnis uebernehmen oder neu nummerieren? Empfehlung: Berufungsklaegeranlagen als BK1, BK2 ..., Berufungsbeklagter BB1, BB2 ... Revisionsanlagen sind ueblich nur ergaenzend; Schwerp... |
| `anlagen-bei-eilantrag-eu-arrest` | Anlagen fuer einstweilige Verfuegung und Arrest: Glaubhaftmachung § 294 ZPO durch Anlagen, eidesstattliche Versicherung als Anlage, parate Beweismittel. Hohe Anforderungen Vollstaendigkeit. Output Standard-Anlagensatz fuer wettbewerbsrec... |
| `anlagen-bilder-screenshots` | Bilder und Screenshots als Anlagen: Beweiskraft, Manipulationsanfaelligkeit, EXIF-Daten, Metadaten. Empfehlung: Original und Vergroesserung beifuegen, EXIF-Export anhaengen, Standortdaten transparent machen. Bei Screenshots: voller Brows... |
| `anlagen-elektronische-dokumente-spezial` | Spezialfall elektronische Dokumente als Anlage: ERVV-Vorgaben, qualifizierte elektronische Signatur, Datei-Format-Whitelist nach ERVV, maximale Groesse, beA-Vorgaben, Container-PDF. Pruefraster und Mustertexte fuer Eingang bei Gericht. |
| `anlagen-format-und-dateinamen` | Format und Dateinamen fuer Anlagen: K-01_2024-03-12_Mietvertrag.pdf. Maschinenlesbar, sortierbar, beA-kompatibel. Maximal 3 Ebenen Unterordner, keine Sonderzeichen, keine Umlaute in Dateinamen, durchgehend kleingeschrieben. |
| `anlagen-fuer-bea-versand` | Anlagen fuer beA-Versand vorbereiten: PDF/A-konform, max. zulaessige Dateigroesse beachten, OCR ueber Scans laufen lassen, korrekt strukturiertes XJustiz-Begleitformular. Liste der Anlagen pro Schriftsatz mit Pruefsumme. Verhindert wiede... |
| `anlagen-haftpflicht-versicherer` | Anlagen-Pflicht gegenueber Haftpflichtversicherer (Berufshaftpflicht, Hausratversicherung, KFZ): welche Anlagen muessen mit Schadenanzeige eingereicht werden, was der Versicherer im Regulierungsverfahren erwartet. Pruefraster aus § 31 VV... |
| `anlagen-konvention-k-b-erlaeutert` | Konvention erklaert und korrekt eingesetzt: K-Anlagen Klaeger, B-Anlagen Beklagter, ZN-Anlagen Zeugen, GA-Anlagen Gutachten, AS-Anlagen Anlagenband. Wann Klein-/Grosschreibung, wann Bindestrich. Wechselt sauber, wenn der Mandant im Vorpr... |
| `anlagen-konvention-mandantenfreundlich` | Anlagen-Konvention mandantenfreundlich: durchlaufende Nummerierung K1 / K2 / K3 ff. fuer Klaegerseite, B1 / B2 / B3 ff. fuer Beklagtenseite, Anlagenbaender, Inhaltsverzeichnis, beA-konforme PDF-Bezeichnung. Mustertext fuer Anlagenverzeic... |
| `anlagen-prozessual-pruefung-spezial` | Spezialfall prozessuale Anlagenpruefung: keine Substantiierung durch blossen Anlagenverweis (BGH-Linie), eigener Vortrag noch im Schriftsatz erforderlich, Tatsachenkern aus Anlage in den Text uebernehmen. Pruefraster und Korrektur-Bauste... |
| `anlagen-quality-check-vor-zustellung` | Quality-Check fuer Anlagenpaket vor Zustellung: Vollstaendigkeit (alle Bezuege im Schriftsatz haben passende Anlage), Lesbarkeit (OCR, kein Schwarzbalken), Schwaerzung (DSGVO und Mandantengeheimnisse), Format (PDF/A wo gefordert). Pruefl... |
| `anlagen-schwaerzen-anonymisieren` | Anlagen schwaerzen und anonymisieren: personenbezogene Daten unbeteiligter Dritter (Mitarbeiter, Kunden, Patienten) entfernen, Kontonummern bis auf letzte 3 Ziffern schwaerzen, Geburtsdaten redigieren, soweit nicht streitrelevant. Mat2-... |
| `anlagen-uebersetzungspflicht` | Fremdsprachige Anlagen: Uebersetzungspflicht § 184 GVG. Beglaubigte oder einfache Uebersetzung? Gericht kann Uebersetzung verlangen oder Ablehnung der Beruecksichtigung androhen. Empfehlung: bei zentralen Urkunden beglaubigte Uebersetzun... |
| `anlagen-vorlagepflicht-141-zpo` | Anordnung der Urkundenvorlage nach § 142 ZPO und § 421 ZPO: wann kann das Gericht die Vorlage einer Urkunde anordnen, wann hat ein Beweisfuehrer Anspruch auf Vorlage durch den Gegner. Pruefraster, Antragsformulierung und Folgen Nichtvorl... |
| `anlagen-zu-schriftsaetzen` | Anwalt hat Schriftsatz fertig und muss Anlagen korrekt benennen nummerieren und als PDF-Konvolut aufbereiten. Anlagemanagement gerichtliche Schriftsaetze. Prüfraster: Schriftsatz lesen Beweisstuecke erkennen sortieren beA-konforme Benenn... |
| `anlagen-zur-substantiierung-pflicht` | Anlagen ersetzen keine Substantiierung im Schriftsatz: 'wegen der weiteren Einzelheiten wird auf Anlage K5 verwiesen' ist nicht ausreichend (BGH X ZR 39/16). Pruefraster: Welche Behauptung wird substanziiert, welche durch Anlage nur bele... |
| `anlagenband-strukturieren` | Anlagenband strukturieren: Trennblaetter, Inhaltsverzeichnis, Reihenfolge nach Schriftsatzbezug, durchgehende Foliierung. Anweisung fuer Kanzleimitarbeiter zur physischen oder elektronischen Erstellung. Fuer beA-Versand zusaetzlich ein d... |
| `anlagenbezug-im-schriftsatz` | Wie Anlagen im Schriftsatz richtig eingefuehrt werden: 'Beweis: Vorlage der Anlage K1' oder 'wie sich aus Anlage K3 ergibt'. Erste Erwaehnung mit Kurztitel und Datum, danach nur K1, K2 ... Vermeidet sprachliche Fehler bei mehrfachem Bezug. |
| `anlagenkonvolut-konsolidieren` | Anlagenkonvolut aus Mandanten-ZIP konsolidieren: Duplikate ueber Hashvergleich erkennen, gleiche Vertraege in unterschiedlichen Fassungen identifizieren, sortieren nach Datum und Thema, Lueckenanalyse (welcher Vertrag wird im Schriftsatz... |
| `anlagenverzeichnis-grundaufbau` | Anlagenverzeichnis nach deutscher Anwaltsuebung aufbauen: K1, K2, K3 ... fuer Klaegerseite, B1, B2 ... fuer Beklagtenseite. Kurztitel, Datum, Funktion (Beweismittel zu welcher Behauptung), Fundstelle im Schriftsatz. Loest Doppel-Nummerie... |
| `beweisangebot-anlage-zeugen` | Zeugenbeweis korrekt ueber Anlagen unterstuetzen: schriftliche Zeugenaussagen sind keine Anlagen-Beweismittel im Strengbeweis, koennen aber als praeprozessuale Information dienen. Anlagen, die die Glaubhaftigkeit stuetzen (Chatverlauf, E... |
| `spezial-alles` | Vertiefter Spezial-Skill im Plugin anlagen-zu-schriftsaetzen zu alles: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-anlagen` | Vertiefter Spezial-Skill im Plugin anlagen-zu-schriftsaetzen zu anlagen: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-baut-anlagenkonvolut` | Vertiefter Spezial-Skill im Plugin anlagen-zu-schriftsaetzen zu baut Anlagenkonvolut: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-bea` | Vertiefter Spezial-Skill im Plugin anlagen-zu-schriftsaetzen zu beA: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-benennt` | Vertiefter Spezial-Skill im Plugin anlagen-zu-schriftsaetzen zu benennt: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-benennt-bea` | Vertiefter Spezial-Skill im Plugin anlagen-zu-schriftsaetzen zu benennt beA: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-excel` | Vertiefter Spezial-Skill im Plugin anlagen-zu-schriftsaetzen zu Excel: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-gerichtlichen` | Vertiefter Spezial-Skill im Plugin anlagen-zu-schriftsaetzen zu gerichtlichen: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-konvertiert` | Vertiefter Spezial-Skill im Plugin anlagen-zu-schriftsaetzen zu konvertiert: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-konvertiert-alles-pdf` | Vertiefter Spezial-Skill im Plugin anlagen-zu-schriftsaetzen zu konvertiert alles PDF: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-logik` | Vertiefter Spezial-Skill im Plugin anlagen-zu-schriftsaetzen zu Logik: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-pdf` | Vertiefter Spezial-Skill im Plugin anlagen-zu-schriftsaetzen zu PDF: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-pruefmodus-bereits-zugeordnete-anlag` | Vertiefter Spezial-Skill im Plugin anlagen-zu-schriftsaetzen zu Prüfmodus bereits zugeordnete Anlagen: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-schriftsaetzen` | Vertiefter Spezial-Skill im Plugin anlagen-zu-schriftsaetzen zu schriftsaetzen: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-schriftsatz` | Vertiefter Spezial-Skill im Plugin anlagen-zu-schriftsaetzen zu Schriftsatz: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-sortiert` | Vertiefter Spezial-Skill im Plugin anlagen-zu-schriftsaetzen zu Sortiert: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-stempelt-oben-anlage-arial` | Vertiefter Spezial-Skill im Plugin anlagen-zu-schriftsaetzen zu stempelt oben Anlage Arial: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-word` | Vertiefter Spezial-Skill im Plugin anlagen-zu-schriftsaetzen zu Word: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-zuordnung` | Vertiefter Spezial-Skill im Plugin anlagen-zu-schriftsaetzen zu Zuordnung: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-zuordnung-anlagen-gerichtlichen-schr` | Vertiefter Spezial-Skill im Plugin anlagen-zu-schriftsaetzen zu Zuordnung Anlagen gerichtlichen Schriftsaetzen: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin anlagen-zu-schriftsaetzen: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin anlagen-zu-schriftsaetzen: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin anlagen-zu-schriftsaetzen: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin anlagen-zu-schriftsaetzen: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin anlagen-zu-schriftsaetzen: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin anlagen-zu-schriftsaetzen: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin anlagen-zu-schriftsaetzen: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin anlagen-zu-schriftsaetzen: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin anlagen-zu-schriftsaetzen: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin anlagen-zu-schriftsaetzen: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
