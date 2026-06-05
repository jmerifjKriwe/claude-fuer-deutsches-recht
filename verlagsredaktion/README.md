# Verlagsredaktion

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`verlagsredaktion`) | [`verlagsredaktion.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verlagsredaktion.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Auerbach Soundworks / Nordlicht in Beton** (`urheberrecht-musik-ki-songstreit-auerbach`) | [Gesamt-PDF lesen](../testakten/urheberrecht-musik-ki-songstreit-auerbach/gesamt-pdf/urheberrecht-musik-ki-songstreit-auerbach_gesamt.pdf) | [`testakte-urheberrecht-musik-ki-songstreit-auerbach.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-urheberrecht-musik-ki-songstreit-auerbach.zip) |
| **Akte Lilienfeld Verlag: Fachbuch, E-Book-Bundle, Remittenden und Preisbindungsabmahnung** (`verlagsrecht-buchpreisbindung-fachverlag-lilienfeld`) | [Gesamt-PDF lesen](../testakten/verlagsrecht-buchpreisbindung-fachverlag-lilienfeld/gesamt-pdf/verlagsrecht-buchpreisbindung-fachverlag-lilienfeld_gesamt.pdf) | [`testakte-verlagsrecht-buchpreisbindung-fachverlag-lilienfeld.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verlagsrecht-buchpreisbindung-fachverlag-lilienfeld.zip) |
| **Verlagsredaktion Morgenlage Fachverlag** (`verlagsredaktion-morgenlage-fachverlag`) | [Gesamt-PDF lesen](../testakten/verlagsredaktion-morgenlage-fachverlag/gesamt-pdf/verlagsredaktion-morgenlage-fachverlag_gesamt.pdf) | [`testakte-verlagsredaktion-morgenlage-fachverlag.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verlagsredaktion-morgenlage-fachverlag.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein Verlagsdesk für juristische und fachliche Verlage: Eingangskorb, Manuskriptaufnahme, Redaktion, Rechtecheck, Zitat- und Fundstellenkontrolle, Autor:innenkommunikation, Heftplanung, Buchprojektsteuerung, Satzfahnen, Metadaten, Marketingtexte, Produktionsübergabe und Qualitätstor.

Der erste Bildschirm soll sich für eine Sachbearbeiterin so anfühlen: Alles liegt durcheinander im Postfach, aber das Plugin macht daraus sofort eine Morgenlage, eine Prioritätenliste und den nächsten verwendbaren Arbeitsschritt.

## Installation

1. ZIP herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `verlagsredaktion.zip` hochladen.

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json`, `skills/` und `references/` enthalten.

## Was das Plugin gut können soll

- Aus einer unordentlichen Inbox eine Tagesübersicht machen.
- Manuskripte, Diktate, Folien, Screenshots, Tabellen und Autor:innenmails inventarisieren.
- Rohmanuskripte als Anschubhilfe erstellen, ohne fremde Texte zu kopieren.
- Vorhandene Texte strukturieren, kürzen, glätten und auf Widersprüche prüfen.
- Zitate, Fundstellen, Randnummern und Quellenstatus transparent markieren.
- Rechtefragen zu UrhG, Verlagsgesetz, Bildrechten, Tabellen und Fremdmaterialien als Ampel vorbereiten.
- Autor:innen freundlich, knapp und verbindlich anschreiben.
- Heft-, Buch- und Online-First-Workflows in Aufgaben und Fristen übersetzen.
- Klappentexte, Vorschauen, Metadaten und Marketingtexte aus dem Manuskript ableiten.
- Satzfahnen und Korrekturläufe steuern.
- KI-Einsatz, Datenschutz und Vertraulichkeit konservativ dokumentieren.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `verlagsredaktion-allgemein` | Cooler Einstieg, stummer Upload, Morgenlage und Skill-Routing. |
| `sachbearbeiterinnen-cockpit` | Persönliches Arbeitscockpit für Sachbearbeitung, Redaktion und Herstellung. |
| `eingangskorb-triage` | Mails, Dateien, Screenshots und Fristen in Prioritäten verwandeln. |
| `projektplan-fristen-heftplanung` | Projektplan für Heft, Online-Beitrag, Buchkapitel oder Kommentarupdate. |
| `manuskriptaufnahme-materialinventar` | Materialinventar mit Herkunft, Nutzbarkeit, Lücken und Rechteampel. |
| `verlagsredaktion` | Klassischer Rohmanuskript-/Editionsassistent. |
| `rohmanuskript-anschubhilfe` | Aus Material ein erstes, klar markiertes Rohmanuskript bauen. |
| `lektorat-struktur-redaktion` | Gliederung, Dramaturgie, Kürzung, Redundanz- und Widerspruchsprüfung. |
| `sprachlektorat-stil-tonalitaet` | Ton, Satzbau, Lesbarkeit, Verlagssprache, Zielgruppe. |
| `quellen-zitate-fundstellencheck` | Zitat- und Quellenhygiene ohne erfundene Literatur. |
| `rechtecheck-urhg-verlg` | Urheberrecht, Verlagsgesetz, Nutzungsrechte, Zitatrecht und Zweitveröffentlichung. |
| `bildrechte-grafiken-tabellen` | Bilder, Screenshots, Tabellen, Grafiken, Diagramme und Credits prüfen. |
| `fremdtext-plagiat-uebernahmecheck` | Fremdtext, KI-Text, Copy-Paste und Paraphrase-Risiken markieren. |
| `autorenkommunikation-email` | Autor:innenmails, Erinnerungen, Freigaben, Nachforderungen. |
| `honorar-vertrag-royalties-triage` | Vertrags-/Honorar-/Royalty-Fragen für redaktionelle Vorprüfung. |
| `metadaten-seo-klappentext` | Titel, Untertitel, Abstract, Schlagworte, VLB-/Web-Metadaten, Klappentext. |
| `zeitschriften-heftplanung` | Hefte, Rubriken, Deadlines, Online-first, Fahnen und Umbruch koordinieren. |
| `buchprojekt-kapitelkoordination` | Kapitel, Autor:innen, Register, Abbildungen, Vorwort und Produktionsstand. |
| `kommentar-aktualisierung-randnummern` | Kommentarupdates, Randnummern, Nachweise, Rechtsstandsvermerk. |
| `entscheidungsmonitor-rechtsstand` | Entscheidungen und Gesetzesänderungen als Aktualisierungsanlass erfassen. |
| `satzfahne-korrekturlauf` | Fahnenprüfung, Korrekturzeichen, Umbruch, Freigabe und letzte Checks. |
| `barrierefreiheit-epub-pdf` | Alt-Texte, Überschriftenlogik, Tabellenzugänglichkeit, EPUB/PDF-Check. |
| `marketing-presse-social` | Vorschau, Newsletter, Social Copy, Presseinfo und Nutzenargumente. |
| `sales-katalog-vlb-buchhandel` | Vertriebskurztext, Katalogdaten, Buchhandelsargumente, Zielgruppen. |
| `knowledge-base-faq-kundenservice` | FAQ und interne Wissensbasis für Vertrieb, Support und Redaktion. |
| `ai-einsatz-transparenz-datenschutz` | KI-Einsatz, Vertraulichkeit, DSGVO, Rechte und Freigabe dokumentieren. |
| `produktionsuebergabe-checkliste` | Übergabe an Herstellung, Satz, Online, Marketing, Vertrieb und Archiv. |
| `qualitaetsgate-verlag` | Schlussprüfung vor Autor:innenversand, Satz, Onlinegang oder Druck. |

## Quellenregel

- Keine Kommentar-, Handbuch-, Aufsatz- oder Datenbankfundstellen aus Modellwissen.
- Literatur nur aus Nutzerquelle, frei zugänglicher Quelle oder lizenziertem Live-Zugriff.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Fremdtexte niemals wörtlich übernehmen, außer der Nutzer verlangt ein zulässiges kurzes Zitat mit sauberer Quellenangabe und Zweck.
- Bei Verlagstexten immer trennen: Autor:innenmaterial, Redaktionstext, Fremdquelle, KI-Vorschlag und offene Lücke.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 28 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `eingangskorb-heftplanung-interessen` | Eingangskorb Heftplanung Interessen im Verlagsredaktion (Recht): prüft konkret Eingangskorb, Heftplanung, Juristische, Manuskript. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `eingangskorb-triage-entscheidungsmonitor` | Eingangskorb Triage Entscheidungsmonitor im Verlagsredaktion (Recht): prüft konkret Sortiert einen Verlags-Eingangskorb aus Mails, Manuskripten, Fahnen, Bildern. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem S... |
| `lektorat-struktur-manuskriptaufnahme` | Lektorat Struktur Manuskriptaufnahme im Verlagsredaktion (Recht): prüft konkret Redigiert Struktur, Argumentationsgang, Gliederung, Kuerzung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `metadaten-fehlerkatalog` | Metadaten Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `qualitaetsgate-verlag-quellen-zitate` | Qualitaetsgate Verlag Quellen Zitate im Verlagsredaktion (Recht): prüft konkret Schlusspruefung fuer Verlagsoutputs vor Autor, Prueft Quellen, Zitate, Randnummern. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem... |
| `redaktion-satzfahnen-verlage-verlagsdesk` | Redaktion Satzfahnen Verlage Verlagsdesk im Verlagsredaktion (Recht): prüft konkret Redaktion, Satzfahnen, Verlage, Verlagsdesk. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `sales-katalog-satzfahne-korrekturlauf` | Sales Katalog Satzfahne Korrekturlauf im Verlagsredaktion (Recht): prüft konkret Bereitet Vertriebs-, Katalog-, VLB- und Buchhandelsdaten mit Zielgruppen, Verkau. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem... |
| `verl-abstimmung` | Verl Abstimmung im Verlagsredaktion (Recht): prüft konkret Chronologie und Belegmatrix im Plugin verlagsredaktion, Fristen- und Risikoampel im Plugin verlagsredaktion, Strukturiert die laufende Kommunikation mit Autorin, Erstellt Projekt... |
| `verl-abstimmung-lektorat-produktion-satz` | Verl Abstimmung Lektorat Produktion Satz im Verlagsredaktion (Recht): prüft konkret Klaert Lektorats- und Redaktionsstandards, Klaert die Schnittstelle zur Produktion, Inhouse-Legal-Check vor Veroeffentlichung, Briefing fuer Vertrieb und... |
| `verl-aussagensicherheit-buchprojekt-bauleiter` | Verl Aussagensicherheit Buchprojekt Bauleiter im Verlagsredaktion (Recht): prüft konkret Prueft im Manuskript jede tragende Aussage darauf ob sie so, Bauleiter juristisches Buchprojekt, Verwertet einen E-Mail-Wechsel als Sachverhaltsquel... |
| `verl-fussnoten-quellen-glossar-konsistenz` | Verl Fussnoten Quellen Glossar Konsistenz im Verlagsredaktion (Recht): prüft konkret Konsolidiert den Fussnotenapparat eines Manuskripts, Prueft Glossar und Begriffskonsistenz quer durch Reihen, Prueft Grammatik und Stilkonsistenz im Man... |
| `verl-ideenpool-priorisierung-impressum` | Verl Ideenpool Priorisierung Impressum im Verlagsredaktion (Recht): prüft konkret Verwaltet einen Ideen-Backlog der Verlagsredaktion mit, Zus, Impressumspflicht und Pruefung im Verlag, Macht aus einem Interview-Transkript eine drucktaugl... |
| `verl-loeschpflicht-archivierung-loseblattwerk` | Verl Loeschpflicht Archivierung Loseblattwerk im Verlagsredaktion (Recht): prüft konkret Loeschpflicht und Archivierung bei juristischer, Spezialfall Loseblattwerk, Rettet Manuskripte aus DOCX-/Markdown-/LaTeX-Mix, alten Word97-Dateien u... |
| `verl-mahnung-an-honorar-vertrag` | Verl Mahnung AN Honorar Vertrag im Verlagsredaktion (Recht): prüft konkret Mahnung an Autor bei Rueckforderung von Vorschuss oder, Triage fuer Autor, Honorarvertragstemplates fuer juristische Werke, Haftungsfreistellung zwischen Autor un... |
| `verl-podcast-zeitschriftenbeitrag-powerpoint` | Verl Podcast Zeitschriftenbeitrag Powerpoint im Verlagsredaktion (Recht): prüft konkret Nutzt einen juristischen Podcast als Zitat- und, Macht aus einer schlechten Vortrags-PPT einen, Pressetext zu Rechtsthemen, Prueft die amtliche deuts... |
| `verl-redaktionsmemo-jahresplanung` | Verl Redaktionsmemo Jahresplanung im Verlagsredaktion (Recht): prüft konkret Erstellt das Jahresheft-Planungsmemo einer juristischen, Bereitet eine juristische Redaktionssitzung vor, Prueft die logischen Relationslinien eines juristische... |
| `verl-rueckruf-fehlerbeitrag-screenshot-pdf` | Verl Rueckruf Fehlerbeitrag Screenshot PDF im Verlagsredaktion (Recht): prüft konkret Rueckruf bei spaet erkanntem Fehlerbeitrag, Fuehrt einen sauberen OCR-fuer gescannte PDFs und, Social-Media-Beitrag fuer juristische Fachzeitschrift, S... |
| `verl-tantieme-abrechnung-themenscout` | Verl Tantieme Abrechnung Themenscout im Verlagsredaktion (Recht): prüft konkret Jaehrliche Tantieme-Abrechnung fuer Autoren juristischer, Identifiziert Trends in, Beobachtet rechtsgebietsuebergreifende Trends, ESG. Liefert priorisierten... |
| `verl-vorschuss-ai-einsatz` | Verl Vorschuss AI Einsatz im Verlagsredaktion (Recht): prüft konkret Vorschusspruefung fuer Buchprojekte, Dokumentiert KI-Einsatz, Vertraulichkeit, Datenschutz. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Sc... |
| `verl-webinar-vorbereitung` | Verl Webinar Vorbereitung im Verlagsredaktion (Recht): prüft konkret Webinar-Vorbereitung als Fachbeitrag-Sequel, Leitfaden Zeitschriftenartikel, Prueft die Zitierweise in Manuskripten gegen die jeweiligen, Zweitverwertungsrechte und Neb... |
| `verlagsredaktion-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `verlagsredaktion-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `verlagsredaktion-kaltstart-triage` | Cooler Einstieg fuer das Verlagsredaktion-Plugin: stummer Upload, Morgenlage, Eingangskorb, Fristen, Rechteampel, Manuskriptstatus und Routing zu den Verlagsdesk-Skills. |
| `verlagsredaktion-output-waehlen` | Output wählen im Verlagsredaktion (Recht): Diese Output-Weiche für Verlagsredaktion entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `verlagsredaktion-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `verlagsredaktion-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `zeitschriften-heftplanung` | Zeitschriften Heftplanung im Verlagsredaktion (Recht): fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |
| `zitate-quellenkarte` | Zitate Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
