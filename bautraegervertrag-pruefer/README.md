# Bauträgervertrag-Prüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`bautraegervertrag-pruefer`) | [`bautraegervertrag-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bautraegervertrag-pruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Bauträgervertrag Birkenpfuhl — Verbraucherprüfung Quendel / Übelacker-Strohmeyer** (`bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung`) | [Gesamt-PDF lesen](../testakten/bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung/gesamt-pdf/bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung_gesamt.pdf) | [`testakte-bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Eigenes Plugin für die verbraucherseitige Prüfung deutscher Bauträgerverträge über Wohnungen, Häuser, Tiefgaragenstellplätze und Sondernutzungsrechte. Das Plugin arbeitet aus Sicht der Käuferin oder des Käufers: Es soll einen Notarentwurf, eine beurkundete Urkunde oder eine chaotische Mandatsakte so auswerten, dass MaBV-Zahlungen, Sicherheiten, AGB-Klauseln, Baubeschreibung, Abnahme, Teilungserklärung, Eigentumssicherung und Verhandlungsstrategie nicht nebeneinander liegen bleiben, sondern in ein belastbares Mandatsprodukt münden.

Der Kern ist aus dem langen Bauträgervertrag-Prüfer-Skill übernommen und fachlich verdichtet. Der ursprüngliche One-Shot-Gedanke bleibt erhalten: Wenn ein Vertrag oder Aktenordner vorliegt, startet die Prüfung aus dem Dokument heraus, bildet zuerst einen Fall-Fingerabdruck und stellt nur solche Rückfragen, ohne die die Bewertung objektiv falsch würde. Daneben sind die Arbeitsabschnitte als eigene Skills vorhanden, damit Claude Code/Cowork gezielt den passenden Teil laden kann.

## Wofür dieses Plugin gedacht ist

- Vorprüfung eines Bauträgervertragsentwurfs vor dem Notartermin aus Verbrauchersicht.
- Prüfung einer bereits beurkundeten Urkunde, wenn Raten, Baufortschritt, Sonderwünsche, Abnahme oder Schlussrate streitig werden.
- Aufbereitung einer Mandantenakte mit Teilungserklärung, Baubeschreibung, Ratenplan, Freistellungserklärung, Baugrund-/Technikunterlagen und E-Mail-Verkehr.
- Erstellung eines Drei-Dokumente-Pakets: kurzes Mandantenanschreiben, ausführliches Mandantengutachten und außergerichtliches Aufforderungsschreiben an Bauträger/Notariat mit konkreten Änderungsfassungen.

## Arbeitsweise

1. **Fall-Fingerabdruck:** Urkunde, Parteien, Einheit, Projekt, Preis, Ratenplan, Sicherheiten, Baubeschreibung, Teilungserklärung, Technik, WEG-Organisation und Streitstand werden aus der Akte gezogen.
2. **Pflicht-Prüfblock:** § 650u/§ 650v BGB, § 650m Abs. 2 BGB, §§ 3, 7, 12 MaBV, §§ 305 ff. BGB, Abnahme Gemeinschaftseigentum, Schlussrate und Eigentumssicherung werden immer zuerst geprüft.
3. **Klauselmatrix:** Jede problematische Klausel wird mit Originalwortlaut, Risiko, Normanker, Rechtsprechungsanker, Gegenargument und gewünschter Neufassung erfasst.
4. **Drei-Dokumente-Ausgabe:** Das Ergebnis wird nicht als lose Stichwortliste stehen gelassen, sondern in ausformulierte, verwendbare Texte überführt.

## Quellenhygiene

Rechtsprechung wird nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle verwendet. Zulässige Startquellen sind insbesondere offizielle Bundes-/Landesgerichtsseiten, `rechtsprechung-im-internet.de`, `rechtsinformationen.bund.de`, `dejure.org` und `openjur.de`. BeckRS-, juris-, Kommentar- und Aufsatzfundstellen werden nicht als Beleg zitiert.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code oder Cowork → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Bei einer Prüfung zusätzlich die Testakte oder eigene Vertragsunterlagen als PDF/DOCX/Markdown hochladen.

> Hinweis: Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. Nicht das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 15 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abnahme-gemeinschaftseigentum-schlussrate-und-maengelrechte` | Abnahmeprüfung im Bauträgervertrag: Sondereigentum, Gemeinschaftseigentum, Vertreter- und Sachverständigenabnahme, Erstverwalter, Schlussrate, § 640 BGB, §§ 633 ff. BGB, § 3 Abs. 2 MaBV, Verjährungsbeginn, Beweislast und BGH-Linie 2023/2... |
| `agb-klauselkontrolle-beweislast-und-tatsachenbestaetigung` | AGB-Klauselkontrolle im Bauträgervertrag: prüft § 307 BGB, § 308 Nr. 4 BGB, § 309 Nr. 12 und Nr. 15 BGB, pauschale Tatsachenbestätigungen, Beweislastverschiebungen, Änderungsrechte, Haftungsbegrenzungen, Ausschlussfristen und geltungserh... |
| `baubeschreibung-bausoll-und-wohnflaeche` | Baubeschreibung und Bausoll im Bauträgervertrag: prüft § 650j BGB, § 650k Abs. 2/3 BGB, Art. 249 EGBGB, beurkundete Anlagen, Wohnflächenmethode, DIN/ART-Verweise, Bemusterung, Renderings, Showroom-Zusagen und Unklarheiten zulasten des Ba... |
| `bauzeit-verzug-vertragsstrafe-und-hoehere-gewalt` | Bauzeit- und Verzugsprüfung beim Bauträgervertrag: verbindlicher Fertigstellungstermin, Bezugsfertigkeit, Bauablaufstörungen, höhere Gewalt, Lieferengpässe, Wiederanlaufzuschläge, Vertragsstrafe, Schadensersatz und bauablaufbezogene Darl... |
| `beurkundung-verbraucherfrist-notar-und-bezugsurkunden` | Beurkundungs- und Notarprüfung beim Bauträgervertrag: § 311b BGB, § 17 Abs. 2a BeurkG, Zwei-Wochen-Frist, Bezugsurkunden, Anlagen, Vollmachten, Belehrung, Notaranderkonto, Serienprojekt und notarielle Vollzugsrisiken. |
| `eigentumssicherung-vormerkung-lastenfreistellung-und-insolvenz` | Eigentumssicherung beim Bauträgervertrag: Auflassungsvormerkung, Rang, Lastenfreistellung, Globalgrundschuld, Pfandfreigabe, Finanzierungsvollmacht, Insolvenz der Projektgesellschaft, Vormerkungsfreigabe und Schutz des Erwerbers vor Zahl... |
| `fall-fingerabdruck-und-schnelltriage` | Fall-Fingerabdruck für Bauträgerakten: extrahiert Urkunde, Verkäufer, Verbraucherrolle, Wohnung/Haus/Stellplatz, Kaufpreis, Raten, Sicherheiten, Baubeschreibung, Teilungserklärung, Technik, Baufortschritt und Streitstand, bevor eine rote... |
| `hoai-technik-baugrund-und-objektueberwachung` | Technischer Realitätscheck im Bauträgerprojekt: HOAI-Leistungsphasen als Prüfraster, Objektüberwachung, Baugrund, Baugrube, Altlasten, Kampfmittel, Grundwasser, Schallschutz, Brandschutz, Feuchteschutz, Energie, TGA, Aufzug, Tiefgarage u... |
| `mabv-ratenplan-sicherheiten-und-notaranderkonto` | MaBV-Prüfung aus Erwerbersicht: § 3 Abs. 1 MaBV-Fälligkeitsvoraussetzungen, sieben Teilbeträge, § 7-MaBV-Alternative, § 12 MaBV, § 650v BGB, 5-%-Sicherheit nach § 650m Abs. 2 BGB, Reservierungs- und Sonderwunschzahlungen sowie Notarander... |
| `quellenhygiene-rechtsprechungsanker-und-bughunt` | Quellen- und Bug-Hunt-Skill für Bauträgervertragsprüfungen: verifiziert Normenstand, BGH-/OLG-Rechtsprechung, MaBV-Zitate, AGB-Folgen, § 650u/§ 650v BGB, § 650m Abs. 2 BGB, Abnahme- und Schlussratenanker und verhindert BeckRS-/juris-Blin... |
| `sonderwuensche-preisanpassung-und-ausstattungswahl` | Sonderwünsche, Bemusterung und Preisanpassung im Bauträgervertrag: prüft Vorauszahlung, MaBV-Einordnung, Ausstattungswahl, Beratungsstunden, Lieferbarkeit, einseitige Materialänderung, nachträgliche öffentlich-rechtliche Anforderungen un... |
| `streit-ruecktritt-klage-und-selbstvornahme` | Eskalation nach Beurkundung des Bauträgervertrags: Zahlungszurückbehaltung, Rücktritt, Minderung, Nacherfüllung, Selbstvornahme, Vorschussklage, Feststellung, einstweiliger Besitzübergang, Schlussrate, Insolvenz und Klagezielmatrix. |
| `verhandlung-drei-dokumente-paket` | Drei-Dokumente-Ausgabe für Bauträgervertragsprüfung: ausformuliertes Mandantenanschreiben, ausführliches Mandantengutachten und außergerichtliches Aufforderungsschreiben an Bauträger/Notar mit konkreten Änderungsfassungen und Gegenargume... |
| `wohnungseigentum-teilungserklaerung-und-erstverwalter` | WEG- und Teilungserklärungsprüfung beim Bauträgerprojekt: Sondereigentum, Gemeinschaftseigentum, Sondernutzungsrechte, Untergemeinschaften, Kostenverteilung, Erstverwalter, Wartungsverträge, Änderungsvollmachten und Zustimmungspflichten... |
| `workflow-one-shot-verbraucherpruefung` | One-Shot-Workflow für die verbraucherseitige Prüfung eines deutschen Bauträgervertrags: startet aus Vertrags-PDF, DOCX, Markdown oder Aktenordner ohne Rückfragenkaskade, bildet den Fall-Fingerabdruck, prüft MaBV, § 650u/§ 650v BGB, § 650... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt als Datei herunterladen** (empfohlen): [`bautraegervertrag-pruefer-megaprompt.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bautraegervertrag-pruefer-megaprompt.md) (37 KB) — Release-Asset, wird vom Browser als Datei gespeichert.
- Im Browser ansehen: [`bautraegervertrag-pruefer.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/bautraegervertrag-pruefer.md) — wird als Text gerendert, nicht heruntergeladen.
- Im Repo: [`testakten/megaprompts/bautraegervertrag-pruefer.md`](../testakten/megaprompts/bautraegervertrag-pruefer.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->
