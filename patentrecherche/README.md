# patentrecherche

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`patentrecherche`) | [`patentrecherche.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/patentrecherche.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **FTO-Recherche Rotorblattheizung — Windsysteme Norderhof AG vs. Vellbruck Energietechnik / EP 3 218 922 B1** (`fto-recherche-windkraft-rotorblattheizung-windsysteme-norderhof-eppendorfer-stadter`) | [Gesamt-PDF lesen](../testakten/fto-recherche-windkraft-rotorblattheizung-windsysteme-norderhof-eppendorfer-stadter/gesamt-pdf/fto-recherche-windkraft-rotorblattheizung-windsysteme-norderhof-eppendorfer-stadter_gesamt.pdf) | [`testakte-fto-recherche-windkraft-rotorblattheizung-windsysteme-norderhof-eppendorfer-stadter.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fto-recherche-windkraft-rotorblattheizung-windsysteme-norderhof-eppendorfer-stadter.zip) |
| **Patentrecht — Erfindungsakten Ravenstein & Moll** (`patentrecht-erfindungsakten-ravenstein-moll`) | [Gesamt-PDF lesen](../testakten/patentrecht-erfindungsakten-ravenstein-moll/gesamt-pdf/patentrecht-erfindungsakten-ravenstein-moll_gesamt.pdf) | [`testakte-patentrecht-erfindungsakten-ravenstein-moll.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-patentrecht-erfindungsakten-ravenstein-moll.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

> Plugin für **Patentanwältinnen und Patentanwälte**, das Claude Cowork agentisch durch die klassischen Patentdatenbanken führt — Espacenet, Google Patents, DPMAregister, DEPATISnet, EPO Register, WIPO PATENTSCOPE, USPTO. Vorrecherche, **keine amtliche Recherche**.

## Hinweis vorab

Dieses Plugin ist **Vorrecherche-Werkzeug** für die Patentanwaltspraxis. Es ersetzt nicht die amtliche Recherche durch DPMA oder EPA und nicht die finale Bewertung durch die Patentanwältin. Treffer können unvollständig sein, falsch klassifiziert sein, in nicht maschinenlesbaren Volltexten verborgen sein oder durch Patentfamilien-Verbindungen verfehlt werden. Die abschließende Recherche muss durch eigene Nachrecherche oder durch Überprüfung der Treffer abgesichert werden.

Das Plugin ist Teil des Repositories [`claude-fuer-deutsches-recht`](../) und wurde mit Hilfe eines KI-Code-Assistenten erstellt; die inhaltliche Verantwortung trägt der Autor (Klotzkette).

## Inhalt

14 Skills, 3 References. Die methodische Grundlage stammt aus den Querschnitts-Plugins [`methodenlehre-buergerliches-recht`](../methodenlehre-buergerliches-recht) und [`zitierweise-deutsches-recht`](../zitierweise-deutsches-recht), die parallel aktiviert sein sollten.

### Skills

| Skill | Funktion |
| --- | --- |
| `patentrecherche-kaltstart-interview` | Setup: Patentanwältin, Mandant, Erfindung, Recherchezweck, Rechtsraum |
| `klassifikation-cpc-ipc` | CPC- und IPC-Klassen für die Recherche bestimmen |
| `agentische-datenbank-recherche` | Master-Skill: agentische Bedienung von Espacenet, Google Patents, DPMAregister, DEPATISnet, EPO Register, WIPO PATENTSCOPE, USPTO |
| `stand-der-technik-recherche` | Vorrecherche für Neuheitsbewertung vor eigener Anmeldung |
| `neuheit-pruefen` | § 3 PatG / Art. 54 EPÜ — Einzeldokument-Vorwegnahme aller Merkmale |
| `erfinderische-taetigkeit-pruefen` | § 4 PatG / Art. 56 EPÜ — Problem-Solution-Approach (EPA-Beschwerdekammern) |
| `freedom-to-operate-recherche` | FTO — Patentverletzungsrisiko aus Drittpatenten vor Markteintritt |
| `patentfamilien-analyse` | INPADOC-Familie — weltweite Patente mit gleichem Prioritätstag |
| `rechtsstand-pruefen` | Anmeldetag, Erteilung, Erlöschen, Einspruch, Nichtigkeit |
| `ueberwachung-konkurrenten` | Monitoring neuer Anmeldungen bestimmter Anmelder oder Klassen |
| `pruefungsbescheid-vorbereiten` | EPA- oder DPMA-Bescheid systematisch entgegnen, Stand-der-Technik-Entgegenhaltungen einordnen |
| `recherchebericht-erstellen` | Formaler Output mit Treffern, Bewertung, Disclaimer |
| `rueckfragen-mandant` | Erfindungsabgrenzung klären — Was ist der wesentliche Lösungsbeitrag |

### References

- `cpc-ipc-klassen-uebersicht.md` — CPC- und IPC-Hauptsektionen, Querverweis-Logik
- `patentdatenbanken-quellen.md` — Datenbanken im Detail (URL, Abdeckung, Stärken, Schwächen, agentische Bedienung)
- `bpatg-und-epa-rspr-leitentscheidungen.md` — Leitentscheidungen Patentanwaltspraxis (BGH X. Senat, BPatG, EPA G-Entscheidungen)

## Setup

Nach Aktivierung des Plugins wird beim ersten Lauf von `patentrecherche-kaltstart-interview` ein Profil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/patentrecherche/CLAUDE.md` angelegt (Kanzlei, Patentanwält:innen, Schwerpunktklassen, typische Mandantenstruktur).

## Pflichtdisclaimer

Jedes Recherche-Ergebnis enthält am Anfang den Disclaimer "**Hinweis zur Recherche** — KI-gestützte Vorrecherche, keine amtliche Recherche, finale Bewertung muss eigenständig abgesichert werden". Skills lassen den Disclaimer nicht weg.

## Verhältnis zum Berufsrecht

Patentanwältinnen sind Berufsgeheimnisträger nach § 203 Abs. 1 Nr. 3 StGB; § 39a PAO regelt die Verschwiegenheit, § 39c PAO regelt die Inanspruchnahme von Dienstleistern. Vor produktivem Einsatz eines KI-Dienstleisters: berufsrechtliche Vorprüfung mit dem Schwester-Plugin [`berufsrecht-ki-vertragspruefung`](../berufsrecht-ki-vertragspruefung) durchführen.

## Lizenz

Apache-2.0 OR MIT. Siehe Repository-Stammverzeichnis.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | patentrecherche: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemus... |
| `kompendium-02-workflow-mandantenko-bis-spezial-agentisch-fr` | patentrecherche: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-mandantenkommunikation, workflow-redteam-qualitygate, spezial-agentisch-fristen-form-und-zustaendigkeit) und bewahrt deren Workflows, Normanke... |
| `kompendium-03-spezial-taetigkeit-f-bis-epo-opposition-strat` | patentrecherche: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (spezial-taetigkeit-fristennotiz-und-naechster-schritt, agentische-datenbank-recherche, epo-opposition-strategie) und bewahrt deren Workflows, Normanker... |
| `kompendium-04-erfinderische-taetig-bis-ki-und-patent-strate` | patentrecherche: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (erfinderische-taetigkeit-pruefen, freedom-to-operate-recherche, ki-und-patent-strategie) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausg... |
| `kompendium-05-klassifikation-cpc-i-bis-patentfamilien-analy` | patentrecherche: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (klassifikation-cpc-ipc, neuheit-pruefen, patentfamilien-analyse) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-06-patr-fto-bericht-lei-bis-patr-recherchestrate` | patentrecherche: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (patr-fto-bericht-leitfaden, patr-patentfamilie-priodatum-spezial, patr-recherchestrategie-bauleiter) und bewahrt deren Workflows, Normanker, Prüfprogra... |
| `kompendium-07-patr-software-ki-pat-bis-pruefungsbescheid-vo` | patentrecherche: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (patr-software-ki-patentierbarkeit-spezial, pr-einfuehrung-recherchearten, pruefungsbescheid-vorbereiten) und bewahrt deren Workflows, Normanker, Prüfpr... |
| `kompendium-08-recherche-strategie-bis-recherchebericht-ers` | patentrecherche: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (recherche-strategie-keywords-und-klassen, recherche-tools-marktuebersicht, recherchebericht-erstellen) und bewahrt deren Workflows, Normanker, Prüfprog... |
| `kompendium-09-rechtsstand-pruefen-bis-spezial-depatisnet-v` | patentrecherche: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (rechtsstand-pruefen, rueckfragen-mandant, spezial-depatisnet-verhandlung-vergleich-und-eskalation) und bewahrt deren Workflows, Normanker, Prüfprogramm... |
| `kompendium-10-spezial-dpmaregister-bis-spezial-erfinderisch` | patentrecherche: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (spezial-dpmaregister-schriftsatz-brief-und-memo-bausteine, spezial-epue-beweislast-und-darlegungslast, spezial-erfinderische-sonderfall-und-edge-case)... |
| `kompendium-11-spezial-espacenet-do-bis-spezial-neuheit-red` | patentrecherche: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (spezial-espacenet-dokumentenmatrix-und-lueckenliste, spezial-google-risikoampel-und-gegenargumente, spezial-neuheit-red-team-und-qualitaetskontrolle) u... |
| `kompendium-12-spezial-patentanwael-bis-spezial-patents-beho` | patentrecherche: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (spezial-patentanwaelte-tatbestand-beweis-und-belege, spezial-patentrecherche-erstpruefung-und-mandatsziel, spezial-patents-behoerden-gericht-und-regist... |
| `kompendium-13-spezial-patg-mandant-bis-spezial-register-zah` | patentrecherche: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (spezial-patg-mandantenkommunikation-entscheidungsvorlage, spezial-problem-abschlussprodukt-und-uebergabe, spezial-register-zahlen-schwellen-und-berechn... |
| `kompendium-14-spezial-stand-intern-bis-spezial-uspto-mehrpa` | patentrecherche: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (spezial-stand-internationaler-bezug-und-schnittstellen, spezial-technik-formular-portal-und-einreichung, spezial-uspto-mehrparteien-konflikt-und-intere... |
| `kompendium-15-spezial-wipo-complia-bis-ueberwachung-konkurr` | patentrecherche: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (spezial-wipo-compliance-dokumentation-und-akte, stand-der-technik-recherche, ueberwachung-konkurrenten) und bewahrt deren Workflows, Normanker, Prüfpro... |
| `kompendium-16-upc-unified-patent-c-bis-upc-unified-patent-c` | patentrecherche: Konsolidiertes Skill-Kompendium 16; bündelt 1 frühere Spezialskills (upc-unified-patent-court-spezial) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `patentrecherche-kaltstart-interview` | Kaltstart-Interview für das Patentrecherche-Plugin. Stellt fest wer recherchiert (Patentanwaeltin Patentanwalt Patentassessor Patentingenieur Recherchekraft) welche Kanzlei und welche Technikgebiete (Mechanik Elektrotechnik Chemie Biotec... |
| `spezial-epo-livequellen-und-rechtsprechungscheck` | EPO: Livequellen- und Rechtsprechungscheck im Plugin patentrecherche; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin patentrecherche: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin patentrecherche: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin patentrecherche: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin patentrecherche: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin patentrecherche: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin patentrecherche: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
