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
| `dpmaregister-epue-beweislast-erfinderische` | Dpmaregister Epue Beweislast Erfinderische im Plugin Patentrecherche: prüft konkret Dpmaregister, Epue, Erfinderische. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `epo-quellenkarte` | Epo Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `erfinderische-taetigkeit-freedom-to-ki-patent` | Erfinderische Taetigkeit Freedom TO KI Patent im Plugin Patentrecherche: prüft konkret Prüft erfinderische Tätigkeit nach § 4 PatG und Art, Freedom-to-Operate-Recherche (FTO) vor Markteintritt eines, Spezialfall KI-Erfindungen Patent-Str... |
| `espacenet-google-neuheit-red` | Espacenet Google Neuheit RED im Plugin Patentrecherche: prüft konkret Espacenet, Google, Neuheit. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `klassifikation-cpc-neuheit-patentfamilien` | Klassifikation CPC Neuheit Patentfamilien im Plugin Patentrecherche: prüft konkret CPC- und IPC-Klassifikation für Patentrecherche bestimmen, Prüft Neuheit nach § 3 PatG und Art, Patentfamilien-Analyse über INPADOC und. Liefert priorisie... |
| `patentanwaelte-patentrecherche-patents` | Patentanwaelte Patentrecherche Patents im Plugin Patentrecherche: prüft konkret Patentanwaelte, Patentrecherche, Patents. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `patentrecherche-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `patentrecherche-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `patentrecherche-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `patentrecherche-kaltstart-interview` | Kaltstart-Interview für das Patentrecherche-Plugin. Stellt fest wer recherchiert (Patentanwaeltin Patentanwalt Patentassessor Patentingenieur Recherchekraft) welche Kanzlei und welche Technikgebiete (Mechanik Elektrotechnik Chemie Biotec... |
| `patentrecherche-mandantenkommunikation-redteam-qualitygate` | Mandantenkommunikation Redteam Qualitygate im Plugin Patentrecherche: prüft konkret Mandantenkommunikation im Plugin patentrecherche, Red-Team Qualitygate im Plugin patentrecherche, Agentisch. Liefert priorisierten Output mit Norm-Pinpoi... |
| `patentrecherche-output-waehlen` | Output wählen im Plugin Patentrecherche: Diese Output-Weiche für Patentrecherche entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `patentrecherche-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `patentrecherche-start-chronologie-fristen` | Start Chronologie Fristen im Plugin Patentrecherche: prüft konkret Einstieg, Schnelltriage und Fallrouting im Patentrecherche-Plugin, Chronologie und Belegmatrix im Plugin patentrecherche, Fristen- und Risikoampel im Plugin patentrecherc... |
| `patentrecherche-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `patg-problem-register` | Patg Problem Register im Plugin Patentrecherche: prüft konkret Patg, Problem, Register. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `patr-fto-bericht-patentfamilie-priodatum` | Patr FTO Bericht Patentfamilie Priodatum im Plugin Patentrecherche: prüft konkret Leitfaden Freedom-to-Operate-Bericht, Spezialfall Patentfamilie und Prioritaetsdatum, Bauleiter Patentrecherche-Strategie. Liefert priorisierten Output mit... |
| `patr-software-pr-einfuehrung` | Patr Software PR Einfuehrung im Plugin Patentrecherche: prüft konkret Spezialfall Software- und KI-Patentierbarkeit EPA, Einfuehrung Recherchearten Patent, Bereitet Antwort auf Prüfungsbescheid des DPMA nach § 45. Liefert priorisierten O... |
| `recherche-strategie-tools-marktuebersicht` | Recherche Strategie Tools Marktuebersicht im Plugin Patentrecherche: prüft konkret Recherche-Strategie Keywords und Klassifikationen, Marktuebersicht Recherche-Tools, Formaler Recherchebericht für den Mandanten oder die Akte. Liefert pri... |
| `rueckfragen-mandant-depatisnet` | Rueckfragen Mandant Depatisnet im Plugin Patentrecherche: prüft konkret Prüft Rechtsstand eines Patents oder einer Anmeldung im, Generiert Rückfragen an den Mandanten wenn das vorgelegte, Depatisnet. Liefert priorisierten Output mit Norm... |
| `stand-technik-uspto-interessen` | Stand Technik Uspto Interessen im Plugin Patentrecherche: prüft konkret Stand, Technik, USPTO. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `taetigkeit-fristennotiz-agentische-datenbank` | Taetigkeit Fristennotiz Agentische Datenbank im Plugin Patentrecherche: prüft konkret Taetigkeit, Agentische Patentdatenbank-Recherche, EPO-Einspruch (Opposition) Strategie. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel un... |
| `upc-unified` | UPC Unified im Plugin Patentrecherche: fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |
| `wipo-stand-technik-ueberwachung-konkurrenten` | Wipo Stand Technik Ueberwachung Konkurrenten im Plugin Patentrecherche: prüft konkret Wipo, Recherche Stand der Technik vor eigener Patentanmeldung, Laufende Überwachung neuer Patentanmeldungen von. Liefert priorisierten Output mit Norm-... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
