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

Automatisch generierte Komplett-Liste aller 45 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `eroeffnung-fachanwalt-fao-glaeubigerantrag` | Eroeffnung Fachanwalt FAO Glaeubigerantrag: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `fa-inso-sanierung-quellen-edge-case` | Rechtsquellen: Sonderfall und Edge-Case-Prüfung im Insolvenz- und Sanierungsrecht: fachlich vertiefter Fachmodul mit Normenradar (InsO/StaRUG/IDW-S6), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse u... |
| `fa-schuldschein` | FA Schuldschein: bearbeitet den maßgeblichen Prüfpfad und erzeugt den nächsten belastbaren Output im Mandat. |
| `fachanwalt-insolvenz-sanierungsrecht-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `fachanwalt-insolvenz-sanierungsrecht-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `fachanwalt-insolvenz-sanierungsrecht-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `fachanwalt-insolvenz-sanierungsrecht-output-waehlen` | Output wählen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `fachanwalt-insolvenz-sanierungsrecht-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `fachanwalt-insolvenz-sanierungsrecht-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `glaeubigerantrag-insolvenzanfechtung` | Glaeubigerantrag Insolvenzanfechtung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `glaeubigerverhandlung-sanierung-idw-s6-krypto` | Glaeubigerverhandlung Sanierung IDW S6 Krypto: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `insanw-fortbestehensprognose` | Insanw Fortbestehensprognose: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-insanw-eigenverwaltung-konzerninsolvenz` | Inso Insanw Eigenverwaltung Konzerninsolvenz: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-kommunikation-glaeubiger-p002` | Inso Kommunikation Glaeubiger P002: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-livecheck-fristennotiz-sanierungsrecht` | Inso Livecheck Fristennotiz Sanierungsrecht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p001-ziele-p003c-zustandigkeit-p004a` | Inso P001 Ziele P003c Zustandigkeit P004a: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p003d` | Inso P003d: bearbeitet den maßgeblichen Prüfpfad und erzeugt den nächsten belastbaren Output im Mandat. |
| `inso-p003e-unternehmensgruppe-p004b` | Inso P003e Unternehmensgruppe P004b: bündelt 21 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p004-anwendbarkeit-p036-unpfandbare` | Inso P004 Anwendbarkeit P036 Unpfandbare: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p020-auskunfts-p021-anordnung-p022` | Inso P020 Auskunfts P021 Anordnung P022: bündelt 21 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p040-unterhaltsanspruche-p041-nicht-p042` | Inso P040 Unterhaltsanspruche P041 Nicht P042: bündelt 21 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p054-kosten-p088-vollstreckung-p095` | Inso P054 Kosten P088 Vollstreckung P095: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p061-nichterfullung-p062-verjahrung-p063` | Inso P061 Nichterfullung P062 Verjahrung P063: bündelt 21 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p083-erbschaft-p084-auseinandersetzung` | Inso P083 Erbschaft P084 Auseinandersetzung: bündelt 21 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p092-gesamtschaden-p093-personliche-p227` | Inso P092 Gesamtschaden P093 Personliche P227: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p109-schuldner-p110-p111-verausserung` | Inso P109 Schuldner P110 P111 Verausserung: bündelt 21 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p126` | Inso P126: bearbeitet den maßgeblichen Prüfpfad und erzeugt den nächsten belastbaren Output im Mandat. |
| `inso-p134-unentgeltliche-p135` | Inso P134 Unentgeltliche P135: bündelt 21 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p139-eroffnungsantrag-p147` | Inso P139 Eroffnungsantrag P147: bündelt 21 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p155-steuerrecht-erstgespraech` | Inso P155 Steuerrecht Erstgespraech: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p159-verwertung-p160-besonders-p161` | Inso P159 Verwertung P160 Besonders P161: bündelt 21 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p180-zustandigkeit-p181-umfang-p182` | Inso P180 Zustandigkeit P181 Umfang P182: bündelt 21 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p203-anordnung-p204-rechtsmittel-p205` | Inso P203 Anordnung P204 Rechtsmittel P205: bündelt 21 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p223a-gruppeninterne-p224-rechte-p225` | Inso P223a Gruppeninterne P224 Rechte P225: bündelt 21 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p242-schriftliche-p243-abstimmung-p244` | Inso P242 Schriftliche P243 Abstimmung P244: bündelt 21 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p260-uberwachung-p261-aufgaben-p262` | Inso P260 Uberwachung P261 Aufgaben P262: bündelt 21 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p270f-anordnung-p270g-eigenverwaltung` | Inso P270f Anordnung P270g Eigenverwaltung: bündelt 21 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p279-gegenseitige-p336-vertrag-p043` | Inso P279 Gegenseitige P336 Vertrag P043: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p290-versagung-p291-weggefallen-p292` | Inso P290 Versagung P291 Weggefallen P292: bündelt 21 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p308-annahme-p309-ersetzung-p310-kosten` | Inso P308 Annahme P309 Ersetzung P310 Kosten: bündelt 21 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p335-grundsatz-p337-arbeitsverhaltnis` | Inso P335 Grundsatz P337 Arbeitsverhaltnis: bündelt 21 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-p359-schriftsatzkern-substantiierung` | Inso P359 Schriftsatzkern Substantiierung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `insolvenz-insolvenzanfechtung-insolvenzrecht` | Insolvenzanfechtung Insolvenzrecht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `interessen-verwertung-beweislast-starug` | Interessen Verwertung Beweislast Starug: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `starug-quellenkarte` | Starug Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
