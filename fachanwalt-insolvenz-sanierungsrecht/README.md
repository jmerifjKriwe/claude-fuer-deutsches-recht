# Fachanwalt Insolvenz- und Sanierungsrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fachanwalt-insolvenz-sanierungsrecht`) | [`fachanwalt-insolvenz-sanierungsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-insolvenz-sanierungsrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Großbach Druckguss & Präzision GmbH & Co. KG — Schutzschirm und StaRUG-Optionen** (`starug-schutzschirm-grossbach-druckguss-erfurt`) | [Gesamt-PDF lesen](../testakten/starug-schutzschirm-grossbach-druckguss-erfurt/gesamt-pdf/starug-schutzschirm-grossbach-druckguss-erfurt_gesamt.pdf) | [`testakte-starug-schutzschirm-grossbach-druckguss-erfurt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-starug-schutzschirm-grossbach-druckguss-erfurt.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Plugin Fachanwalt für Insolvenz- und Sanierungsrecht nach FAO § 14 (idF nach Aufnahme StaRUG-Bereiche). Orientierung, Gläubigerantrag, Restrukturierungsplan StaRUG, Insolvenzanfechtung. Schnittstellen zum Plugin `insolvenzrecht` (operativ) und `steuerrecht-anwalt-und-berater`.

## InsO-Paragraphen-Navigator

Dieses Plugin enthält nun zu jedem aktuell im amtlichen InsO-Wortlaut geführten Paragraphen einen eigenen `inso-p...`-Skill. Der Navigator ist für die tägliche Fachanwaltsarbeit gedacht: Er führt nicht abstrakt durch die Insolvenzordnung, sondern fragt pro Norm nach Rolle, Verfahrensstand, Belegen, Fristen, Rechtsfolge, Gegenargumenten und dem nächsten verwertbaren Arbeitsergebnis.

Besonders hilfreich ist das bei Akten, in denen viele Ebenen gleichzeitig laufen: Eröffnungsantrag, Sicherungsmaßnahmen, Massezuordnung, Anfechtung, Forderungsprüfung, Insolvenzplan, Eigenverwaltung, Verbraucherinsolvenz, Nachlassinsolvenz oder internationales Insolvenzrecht. Weggefallene Vorschriften sind bewusst als Altfassungs- und Übergangsrechtsanker enthalten, damit alte Akten und ältere Rechtsprechung nicht versehentlich auf heutige Fälle übertragen werden.

Vor verbindlichen Aussagen prüft der jeweilige Skill den aktuellen Gesetzeswortlaut und verlangt für Rechtsprechung Gericht, Datum, Aktenzeichen und möglichst eine frei zugängliche amtliche oder gerichtliche Quelle. Literatur- und Datenbankfundstellen werden nicht aus Modellwissen behauptet.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `fachanwalt-insolvenz-sanierungsrecht-orientierung` | FAO § 14, InsO, StaRUG, EuInsVO, Quellenprüfung. |
| `fachanwalt-insolvenz-sanierungsrecht-glaeubigerantrag` | Gläubigerantrag § 14 InsO, Forderungs- und Insolvenzgrundsglaubhaftmachung. |
| `fachanwalt-insolvenz-sanierungsrecht-restrukturierungsplan` | Restrukturierungsplan StaRUG, Gruppenbildung, gerichtliche Planbestätigung. |
| `fachanwalt-insolvenz-sanierungsrecht-insolvenzanfechtung` | Anfechtungstatbestände §§ 129 ff. InsO (Schenkungs-, Vorsatz-, Deckungsanfechtung). |
| `inso-p001-...` bis `inso-p359-...` | Paragraphen-Navigator zur aktuellen Insolvenzordnung: pro InsO-Norm ein eigener Workflow mit Beleg-, Fristen-, Risiko- und Quellenprüfung. |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 30 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-allgemein-bis-inso-p126-beschlussv` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 01; bündelt 21 frühere Spezialskills (allgemein, insanw-fortbestehensprognose-workflow, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel, workflo... |
| `kompendium-02-inso-p139-berechnung-bis-inso-p356-sekundarin` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 02; bündelt 21 frühere Spezialskills (inso-p139-berechnung-der-fristen-vor-dem-eroffnungsantrag, inso-p147-rechtshandlungen-nach-verfahrenseroffnung, inso-p157-entsche... |
| `kompendium-03-spezial-livecheck-fr-bis-fa-insolvenz-schulds` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 03; bündelt 21 frühere Spezialskills (spezial-livecheck-fristennotiz-und-naechster-schritt, spezial-sanierungsrecht-fristen-form-und-zustaendigkeit, inso-p104-fixgesch... |
| `kompendium-04-fachanwalt-insolvenz-bis-inso-p003d-verweisun` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 04; bündelt 21 frühere Spezialskills (fachanwalt-insolvenz-glaeubigerverhandlung-sanierung, fachanwalt-insolvenz-idw-s6-sanierungskonzept, fachanwalt-insolvenz-krypto-... |
| `kompendium-05-inso-p003e-unternehm-bis-inso-p019-uberschuld` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 05; bündelt 21 frühere Spezialskills (inso-p003e-unternehmensgruppe, inso-p004b-ruckzahlung-und-anpassung-der-gestundeten-betrage, inso-p004c-aufhebung-der-stundung, i... |
| `kompendium-06-inso-p020-auskunfts-bis-inso-p039-nachrangig` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 06; bündelt 21 frühere Spezialskills (inso-p020-auskunfts-und-mitwirkungspflicht-im-eroffnungsverfahre, inso-p021-anordnung-vorlaufiger-massnahmen, inso-p022-rechtsste... |
| `kompendium-07-inso-p040-unterhalts-bis-inso-p059-entlassung` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 07; bündelt 21 frühere Spezialskills (inso-p040-unterhaltsanspruche, inso-p041-nicht-fallige-forderungen, inso-p042-auflosend-bedingte-forderungen, inso-p044-rechte-de... |
| `kompendium-08-inso-p061-nichterful-bis-inso-p082-leistungen` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 08; bündelt 21 frühere Spezialskills (inso-p061-nichterfullung-von-masseverbindlichkeiten, inso-p062-verjahrung, inso-p063-vergutung-des-insolvenzverwalters, inso-p064... |
| `kompendium-09-inso-p083-erbschaft-bis-inso-p108-fortbesteh` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 09; bündelt 21 frühere Spezialskills (inso-p083-erbschaft-fortgesetzte-gutergemeinschaft, inso-p084-auseinandersetzung-einer-gesellschaft-oder-gemeinschaf, inso-p085-a... |
| `kompendium-10-inso-p109-schuldner-bis-inso-p133-vorsatzlic` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 10; bündelt 21 frühere Spezialskills (inso-p109-schuldner-als-mieter-oder-pachter, inso-p110-schuldner-als-vermieter-oder-verpachter, inso-p111-verausserung-des-miet-o... |
| `kompendium-11-inso-p134-unentgeltl-bis-inso-p158-massnahmen` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 11; bündelt 21 frühere Spezialskills (inso-p134-unentgeltliche-leistung, inso-p135-gesellschafterdarlehen, inso-p136-stille-gesellschaft, inso-p137-wechsel-und-scheckz... |
| `kompendium-12-inso-p159-verwertung-bis-inso-p179-streitige` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 12; bündelt 21 frühere Spezialskills (inso-p159-verwertung-der-insolvenzmasse, inso-p160-besonders-bedeutsame-rechtshandlungen, inso-p161-vorlaufige-untersagung-der-re... |
| `kompendium-13-inso-p180-zustandigk-bis-inso-p202-zustandigk` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 13; bündelt 21 frühere Spezialskills (inso-p180-zustandigkeit-fur-die-feststellung, inso-p181-umfang-der-feststellung, inso-p182-streitwert, inso-p183-wirkung-der-ents... |
| `kompendium-14-inso-p203-anordnung-bis-inso-p223-rechte-der` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 14; bündelt 21 frühere Spezialskills (inso-p203-anordnung-der-nachtragsverteilung, inso-p204-rechtsmittel, inso-p205-vollzug-der-nachtragsverteilung, inso-p206-ausschl... |
| `kompendium-15-inso-p223a-gruppenin-bis-inso-p241-gesonderte` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 15; bündelt 21 frühere Spezialskills (inso-p223a-gruppeninterne-drittsicherheiten, inso-p224-rechte-der-insolvenzglaubiger, inso-p225-rechte-der-nachrangigen-insolvenz... |
| `kompendium-16-inso-p242-schriftlic-bis-inso-p259a-vollstrec` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 16; bündelt 21 frühere Spezialskills (inso-p242-schriftliche-abstimmung, inso-p243-abstimmung-in-gruppen, inso-p244-erforderliche-mehrheiten, inso-p245-obstruktionsver... |
| `kompendium-17-inso-p260-uberwachun-bis-inso-p270e-aufhebung` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 17; bündelt 21 frühere Spezialskills (inso-p260-uberwachung-der-planerfullung, inso-p261-aufgaben-und-befugnisse-des-insolvenzverwalters, inso-p262-anzeigepflicht-des-... |
| `kompendium-18-inso-p270f-anordnung-bis-inso-p288-bestimmung` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 18; bündelt 21 frühere Spezialskills (inso-p270f-anordnung-der-eigenverwaltung, inso-p270g-eigenverwaltung-bei-gruppenangehorigen-schuldnern, inso-p271-nachtragliche-a... |
| `kompendium-19-inso-p290-versagung-bis-inso-p307-zustellung` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 19; bündelt 21 frühere Spezialskills (inso-p290-versagung-der-restschuldbefreiung, inso-p291-weggefallen, inso-p292-rechtsstellung-des-treuhanders, inso-p293-vergutung... |
| `kompendium-20-inso-p308-annahme-de-bis-inso-p333-antragsrec` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 20; bündelt 21 frühere Spezialskills (inso-p308-annahme-des-schuldenbereinigungsplans, inso-p309-ersetzung-der-zustimmung, inso-p310-kosten, inso-p312bis314-weggefalle... |
| `kompendium-21-inso-p335-grundsatz-bis-inso-p358-uberschuss` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 21; bündelt 21 frühere Spezialskills (inso-p335-grundsatz, inso-p337-arbeitsverhaltnis, inso-p338-aufrechnung, inso-p339-insolvenzanfechtung, inso-p340-organisierte-ma... |
| `kompendium-22-inso-p359-verweisung-bis-vergleichsverhandlun` | fachanwalt-insolvenz-sanierungsrecht: Konsolidiertes Skill-Kompendium 22; bündelt 20 frühere Spezialskills (inso-p359-verweisung-auf-das-einfuhrungsgesetz, schriftsatzkern-substantiierung, spezial-antragspflicht-schriftsatz-brief-und-mem... |
| `spezial-rechtsquellen-sonderfall-und-edge-case` | Rechtsquellen: Sonderfall und Edge-Case-Prüfung im Insolvenz- und Sanierungsrecht: fachlich vertiefter Spezialskill mit Normenradar (InsO/StaRUG/IDW-S6), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbrems... |
| `spezial-starug-livequellen-und-rechtsprechungscheck` | StaRUG: Livequellen- und Rechtsprechungscheck im Insolvenz- und Sanierungsrecht: fachlich vertiefter Spezialskill mit Normenradar (InsO/StaRUG/IDW-S6), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin fachanwalt-insolvenz-sanierungsrecht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin fachanwalt-insolvenz-sanierungsrecht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin fachanwalt-insolvenz-sanierungsrecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin fachanwalt-insolvenz-sanierungsrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin fachanwalt-insolvenz-sanierungsrecht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin fachanwalt-insolvenz-sanierungsrecht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
