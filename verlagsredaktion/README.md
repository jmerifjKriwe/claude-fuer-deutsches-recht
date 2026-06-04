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
| `allgemein` | Cooler Einstieg, stummer Upload, Morgenlage und Skill-Routing. |
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
| `allgemein` | Cooler Einstieg fuer das Verlagsredaktion-Plugin: stummer Upload, Morgenlage, Eingangskorb, Fristen, Rechteampel, Manuskriptstatus und Routing zu den Verlagsdesk-Skills. |
| `kompendium-01-workflow-chronologie-bis-spezial-fachliche-fr` | verlagsredaktion: Konsolidiertes Skill-Kompendium 01; bündelt 5 frühere Spezialskills (workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel, verl-abstimmung-mit-autor-feedback-kanal, projektplan-fristen-heftplanung, spe... |
| `kompendium-02-verl-mahnung-an-auto-bis-buchprojekt-kapitelk` | verlagsredaktion: Konsolidiertes Skill-Kompendium 02; bündelt 5 frühere Spezialskills (verl-mahnung-an-autor-zahlung-frist, honorar-vertrag-royalties-triage, verl-honorarvertrag-templates-und-abweichungen, verl-haftungsfreistellung-autor... |
| `kompendium-03-verl-vorschuss-pruef-bis-bildrechte-grafiken` | verlagsredaktion: Konsolidiertes Skill-Kompendium 03; bündelt 5 frühere Spezialskills (verl-vorschuss-pruefung-buecher, ai-einsatz-transparenz-datenschutz, autorenkommunikation-email, barrierefreiheit-epub-pdf, bildrechte-grafiken-tabell... |
| `kompendium-04-eingangskorb-triage-bis-kommentar-aktualisie` | verlagsredaktion: Konsolidiertes Skill-Kompendium 04; bündelt 5 frühere Spezialskills (eingangskorb-triage, entscheidungsmonitor-rechtsstand, fremdtext-plagiat-uebernahmecheck, knowledge-base-faq-kundenservice, kommentar-aktualisierung-r... |
| `kompendium-05-lektorat-struktur-re-bis-produktionsuebergabe` | verlagsredaktion: Konsolidiertes Skill-Kompendium 05; bündelt 5 frühere Spezialskills (lektorat-struktur-redaktion, manuskriptaufnahme-materialinventar, marketing-presse-social, metadaten-seo-klappentext, produktionsuebergabe-checkliste)... |
| `kompendium-06-qualitaetsgate-verla-bis-sachbearbeiterinnen` | verlagsredaktion: Konsolidiertes Skill-Kompendium 06; bündelt 5 frühere Spezialskills (qualitaetsgate-verlag, quellen-zitate-fundstellencheck, rechtecheck-urhg-verlg, rohmanuskript-anschubhilfe, sachbearbeiterinnen-cockpit) und bewahrt d... |
| `kompendium-07-sales-katalog-vlb-bu-bis-spezial-buchprojekte` | verlagsredaktion: Konsolidiertes Skill-Kompendium 07; bündelt 5 frühere Spezialskills (sales-katalog-vlb-buchhandel, satzfahne-korrekturlauf, spezial-autorenkommunikation-compliance-dokumentation-und-akte, spezial-bildrechte-zahlen-schwe... |
| `kompendium-08-spezial-eingangskorb-bis-spezial-rechtecheck` | verlagsredaktion: Konsolidiertes Skill-Kompendium 08; bündelt 5 frühere Spezialskills (spezial-eingangskorb-risikoampel-und-gegenargumente, spezial-heftplanung-mehrparteien-konflikt-und-interessen, spezial-juristische-tatbestand-beweis-u... |
| `kompendium-09-spezial-redaktion-sc-bis-sprachlektorat-stil` | verlagsredaktion: Konsolidiertes Skill-Kompendium 09; bündelt 5 frühere Spezialskills (spezial-redaktion-schriftsatz-brief-und-memo-bausteine, spezial-satzfahnen-formular-portal-und-einreichung, spezial-verlage-dokumentenmatrix-und-lueck... |
| `kompendium-10-verl-abstimmung-mit-bis-verl-audio-transkrip` | verlagsredaktion: Konsolidiertes Skill-Kompendium 10; bündelt 5 frühere Spezialskills (verl-abstimmung-mit-lektorat-format, verl-abstimmung-mit-produktion-satz-druck, verl-abstimmung-mit-rechtsabteilung-pruefung, verl-abstimmung-mit-vert... |
| `kompendium-11-verl-aussagensicherh-bis-verl-formatvorlage-c` | verlagsredaktion: Konsolidiertes Skill-Kompendium 11; bündelt 5 frühere Spezialskills (verl-aussagensicherheit-pruefung, verl-buchprojekt-bauleiter, verl-email-konvolute-zu-fachbeitrag, verl-eskalation-bei-deadline-konflikt, verl-formatv... |
| `kompendium-12-verl-fussnoten-quell-bis-verl-honorarrechnung` | verlagsredaktion: Konsolidiertes Skill-Kompendium 12; bündelt 5 frühere Spezialskills (verl-fussnoten-quellen-konsolidierung, verl-glossar-konsistenz-pruefung, verl-grammatik-konsistenzcheck, verl-handschrift-und-altdoc-digitalisieren, v... |
| `kompendium-13-verl-ideenpool-und-p-bis-verl-konferenzmitsch` | verlagsredaktion: Konsolidiertes Skill-Kompendium 13; bündelt 5 frühere Spezialskills (verl-ideenpool-und-priorisierung, verl-impressum-pflicht-und-pruefung, verl-interview-roh-zu-magazinbeitrag, verl-jourfix-vorbereiten-protokoll, verl-... |
| `kompendium-14-verl-loeschpflicht-u-bis-verl-online-kommenta` | verlagsredaktion: Konsolidiertes Skill-Kompendium 14; bündelt 5 frühere Spezialskills (verl-loeschpflicht-und-archivierung-fachzs, verl-loseblattwerk-spezial, verl-manuskript-merkwuerdige-formate-rettung, verl-newsletter-redaktion-jur, v... |
| `kompendium-15-verl-podcast-zu-zeit-bis-verl-redaktionelle-r` | verlagsredaktion: Konsolidiertes Skill-Kompendium 15; bündelt 5 frühere Spezialskills (verl-podcast-zu-zeitschriftenbeitrag, verl-powerpoint-verwurstung-zu-text, verl-pressetext-rechtsthemen, verl-rechtschreibung-amtlich-aktuell, verl-re... |
| `kompendium-16-verl-redaktionsmemo-bis-verl-roh-research-zu` | verlagsredaktion: Konsolidiertes Skill-Kompendium 16; bündelt 5 frühere Spezialskills (verl-redaktionsmemo-jahresplanung, verl-redaktionssitzung-vorbereiten, verl-relationslinien-pruefung-im-aufsatz, verl-richtigstellung-online-print, ve... |
| `kompendium-17-verl-rueckruf-fehler-bis-verl-stilbruch-stilc` | verlagsredaktion: Konsolidiertes Skill-Kompendium 17; bündelt 5 frühere Spezialskills (verl-rueckruf-fehlerbeitrag-spaet-erkannt, verl-screenshot-pdf-ocr-redaktion, verl-social-media-rechtsfachzeitschrift, verl-statusbericht-an-verlagsle... |
| `kompendium-18-verl-tantieme-abrech-bis-verl-vlb-katalog-pfl` | verlagsredaktion: Konsolidiertes Skill-Kompendium 18; bündelt 5 frühere Spezialskills (verl-tantieme-abrechnung-jaehrlich, verl-themenscout-rechtsentwicklung, verl-trend-radar-rechtsgebiete, verl-vergleichsverhandlung-mit-autor, verl-vlb... |
| `kompendium-19-verl-webinar-vorbere-bis-verlagsredaktion` | verlagsredaktion: Konsolidiertes Skill-Kompendium 19; bündelt 5 frühere Spezialskills (verl-webinar-vorbereitung-fachbeitrag, verl-zeitschriftenartikel-leitfaden, verl-zitierweise-pruefung-zeitschrift-jus-njw, verl-zweitverwertungsrechte... |
| `kompendium-20-zeitschriften-heftpl-bis-zeitschriften-heftpl` | verlagsredaktion: Konsolidiertes Skill-Kompendium 20; bündelt 1 frühere Spezialskills (zeitschriften-heftplanung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-metadaten-red-team-und-qualitaetskontrolle` | Metadaten: Red-Team und Qualitätskontrolle im Plugin verlagsredaktion; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-zitate-livequellen-und-rechtsprechungscheck` | Zitate: Livequellen- und Rechtsprechungscheck im Plugin verlagsredaktion; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin verlagsredaktion: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin verlagsredaktion: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin verlagsredaktion: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin verlagsredaktion: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin verlagsredaktion: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
