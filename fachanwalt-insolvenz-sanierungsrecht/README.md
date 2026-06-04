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

Automatisch generierte Komplett-Liste aller 468 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Fachanwalt Insolvenz Sanierungsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen k... |
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Insolvenz- und Restrukturierungsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen. |
| `fa-inso-drittstaaten-anerkennung-registervollzug` | Fachanwaltlicher Spezialskill für Drittstaateninsolvenz in Deutschland: Anerkennung nach §§ 335 ff., 343 InsO, Inzidentprüfung, office holder, debtor in possession, GmbH-Anteile, Grundbuch, Handelsregister und Nachweispaket. |
| `fa-insolvenz-npl-und-distressed-debt` | Prüft NPL-Kauf, distressed debt, Kreditdienstleister, Gläubigerstellung, Planmehrheiten, Anfechtung und Loan-to-own. |
| `fa-insolvenz-schuldschein-und-lma` | Prüft Schuldschein- und LMA-Finanzierungen in Sanierung, Eigenverwaltung, StaRUG und Insolvenzplan. |
| `fachanwalt-insolvenz-glaeubigerverhandlung-sanierung` | Sanierungs-Verhandlung mit Gläubigern vor und in der Insolvenz nach StaRUG und InsO. Anwendungsfall Schuldner will außergerichtlichen Vergleich oder InsO-Plan mit Gläubigern verhandeln. Normen § 270d InsO Schutzschirm §§ 4-65 StaRUG Rest... |
| `fachanwalt-insolvenz-idw-s6-sanierungskonzept` | Erstellt und prüft Sanierungskonzepte auf IDW-S-6-Niveau aus anwaltlicher Sicht. Führt durch Fortbestehensprognose, Sanierungsfähigkeit, Krisenursachen, Leitbild des sanierten Unternehmens, Maßnahmenpakete, integrierte Planung, kleinere... |
| `fachanwalt-insolvenz-krypto-verwertung` | Workflow-Skill zu fachanwalt insolvenz krypto verwertung. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `fachanwalt-insolvenz-sanierung-starug-plan` | StaRUG-Restrukturierungsplan §§ 4-65 StaRUG. Voraussetzung drohende Zahlungsunfähigkeit § 18 InsO. Plan-Struktur Gruppen Mehrheiten 75 Prozent je Klasse. Cross-class cramdown. Stabilisierungsanordnung § 49 StaRUG. Restrukturierungsbeauft... |
| `fachanwalt-insolvenz-sanierungsrecht-anfechtungsklage-verwalter` | Anfechtungsklage des Insolvenzverwalters nach §§ 129-147 InsO vorbereiten: Tatbestand je Rechtshandlung, § 130/131/133/134/135, Bargeschäft § 142, Rückgewähr § 143, Gegenleistung § 144, Verjährung § 146, Beweislast, KI-Kandidatenmatrix u... |
| `fachanwalt-insolvenz-sanierungsrecht-glaeubigerantrag` | Workflow-Skill zu fachanwalt insolvenz sanierungsrecht glaeubigerantrag. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `fachanwalt-insolvenz-sanierungsrecht-insolvenzanfechtung` | Insolvenzanfechtung nach §§ 129-147 InsO fachanwaltlich prüfen: Verwalter- und Anfechtungsgegnerperspektive, §§ 130/131/133/134/135, Bargeschäft § 142, Rechtsfolgen §§ 143-147, Verjährung § 146, KI-Screening von Schuldnerakten und Grenze... |
| `fachanwalt-insolvenz-sanierungsrecht-orientierung` | Orientierung im Insolvenz- und Sanierungsrecht für Mandate und Fachanwaltschaft nach § 14 FAO. Anwendungsfall Kanzlei will Insolvenzmandat beurteilen oder Anwalt bereitet sich auf FAO-Fachanwaltsprüfung vor. Normen §§ 17-19 InsO Eroeffnu... |
| `fachanwalt-insolvenz-sanierungsrecht-restrukturierungsplan` | Workflow-Skill zu fachanwalt insolvenz sanierungsrecht restrukturierungsplan. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `fachanwalt-insolvenz-sanierungsrecht-schutzschirmverfahren` | Schutzschirmverfahren § 270d InsO Eigenverwaltung in Insolvenz. Vorlaeufige Eigenverwaltung Antrag drohende Zahlungsunfähigkeit. Sachwalter Aufsicht. Schutzschirm 3 Monate bei Voraussetzung Sanierungsfähigkeit. Insolvenz-Plan Vorbereitun... |
| `insanw-anfechtungsmandat-leitfaden` | Leitfaden Anfechtungsmandat fuer Verwalter und Verteidiger: §§ 129 ff. InsO, Vorsatzanfechtung, Bargeschaeftsausnahme. Pruefraster Indizien Kenntnis Glaeubigerbenachteiligung. Mustertext Aufforderungsschreiben und Klageerwiderung. |
| `insanw-eigenverwaltung-schutzschirm-spezial` | Spezialfall Eigenverwaltung und Schutzschirmverfahren §§ 270 ff. InsO: Bescheinigung nach § 270d InsO, Sachwalter, Glaeubigerausschuss, Drittsicherheiten. Pruefraster fuer Bescheinigungsersteller. |
| `insanw-fortbestehensprognose-workflow` | Workflow Fortbestehensprognose IDW S 11 / S 6: Datenraum, Integrierte Planung, Stresstests, Risikoinventur. Pruefraster fuer Geschaeftsleitung und Berater. Anschreiben Bank / Buergschaftsbank / PSD. |
| `insanw-konzerninsolvenz-koordination-spezial` | Spezialfall Konzerninsolvenz §§ 3a ff. InsO: Gruppen-Gerichtsstand, Koordinationsverfahren, Konzern-Anfechtung. Pruefraster fuer mehrstufige Konzerne und auslaendische Tochtergesellschaften. |
| `inso-anfechtung-zahlungsstrom-banken` | Spezialfall Insolvenzanfechtung Zahlungsstrom Banken: Konto-Korrent-Wirkung, Stehenlassen Kontokorrent, Verrechnung mit eigenen Forderungen, § 96 InsO. Pruefraster typischer Bankenfaelle und BGH-Linie 2024 ff. Schriftsatzbausteine. |
| `inso-arbeitnehmer-und-betriebsuebergang` | Arbeitnehmer und Insolvenz: Insolvenzgeld bis 3 Monate, Sozialplan Hoechstgrenzen § 123 InsO, § 113 InsO Kuendigungsmaximum 3 Monate, Betriebsuebergang § 613a BGB im Insolvenz-Asset-Deal. Pruefraster und Mustertexte. Schnittstelle Arbeit... |
| `inso-grenzueberschreitend-eu-eir` | Grenzueberschreitende Insolvenz nach EuInsVO 2015/848 und Abgrenzung zu Drittstaaten: Hauptverfahren, Sekundaerverfahren, COMI, automatische Anerkennung, Verwalterbefugnisse, Drittstaaten-Anerkennung nach §§ 335 ff., 343 InsO und Registe... |
| `inso-grundzuege-verfahrenstypen` | Grundzuege Insolvenz- und Sanierungsverfahrenstypen: Regelinsolvenz, Eigenverwaltung mit oder ohne Schutzschirm, Insolvenzplan, StaRUG-Restrukturierungsplan, Verbraucherinsolvenz. Pro Typ: Schwelle, Antragsrecht, Akteure, Ablauf, typisch... |
| `inso-kommunikation-glaeubiger` | Kommunikation mit Glaeubigern im Insolvenz- und StaRUG-Verfahren: Information, Verhandlung, Vergleichsangebot, Glaeubigerversammlung, Pruefungstermin. Strategie nach Glaeubigergruppen (Bank, Lieferant, Arbeitnehmer, Finanzamt, Sozialvers... |
| `inso-p001-ziele-des-insolvenzverfahrens` | § 1 InsO (Ziele des Insolvenzverfahrens) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p002-amtsgericht-als-insolvenzgericht` | § 2 InsO (Amtsgericht als Insolvenzgericht) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p003-ortliche-zustandigkeit` | § 3 InsO (Örtliche Zuständigkeit) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p003a-gruppen-gerichtsstand` | § 3a InsO (Gruppen-Gerichtsstand) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p003b-fortbestehen-des-gruppen-gerichtsstands` | § 3b InsO (Fortbestehen des Gruppen-Gerichtsstands) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p003c-zustandigkeit-fur-gruppen-folgeverfahren` | § 3c InsO (Zuständigkeit für Gruppen-Folgeverfahren) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p003d-verweisung-an-den-gruppen-gerichtsstand` | § 3d InsO (Verweisung an den Gruppen-Gerichtsstand) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p003e-unternehmensgruppe` | § 3e InsO (Unternehmensgruppe) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p004-anwendbarkeit-der-zivilprozessordnung` | § 4 InsO (Anwendbarkeit der Zivilprozeßordnung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p004a-stundung-der-kosten-des-insolvenzverfahrens` | § 4a InsO (Stundung der Kosten des Insolvenzverfahrens) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p004b-ruckzahlung-und-anpassung-der-gestundeten-betrage` | § 4b InsO (Rückzahlung und Anpassung der gestundeten Beträge) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p004c-aufhebung-der-stundung` | § 4c InsO (Aufhebung der Stundung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p004d-rechtsmittel` | § 4d InsO (Rechtsmittel) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p005-verfahrensgrundsatze` | § 5 InsO (Verfahrensgrundsätze) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p006-sofortige-beschwerde` | § 6 InsO (Sofortige Beschwerde) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p007-weggefallen` | § 7 InsO ist im aktuellen Normtext weggefallen. Der Skill hilft, Altakten, Übergangsfälle und Nachfolgeregelungen ohne falsche Altfassungsübernahme einzuordnen. |
| `inso-p008-zustellungen` | § 8 InsO (Zustellungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p009-offentliche-bekanntmachung` | § 9 InsO (Öffentliche Bekanntmachung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p010-anhorung-des-schuldners` | § 10 InsO (Anhörung des Schuldners) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p010a-vorgesprach` | § 10a InsO (Vorgespräch) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p011-zulassigkeit-des-insolvenzverfahrens` | § 11 InsO (Zulässigkeit des Insolvenzverfahrens) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p012-juristische-personen-des-offentlichen-rechts` | § 12 InsO (Juristische Personen des öffentlichen Rechts) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p013-eroffnungsantrag` | § 13 InsO (Eröffnungsantrag) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p013a-antrag-zur-begrundung-eines-gruppen-gerichtsstands` | § 13a InsO (Antrag zur Begründung eines Gruppen-Gerichtsstands) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p014-antrag-eines-glaubigers` | § 14 InsO (Antrag eines Gläubigers) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p015-antragsrecht-bei-juristischen-personen-und-rechtsfahig` | § 15 InsO (Antragsrecht bei juristischen Personen und rechtsfähigen Personengesellschaften) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p015a-antragspflicht-bei-juristischen-personen-und-rechtsfa` | § 15a InsO (Antragspflicht bei juristischen Personen und rechtsfähigen Personengesellschaften) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p015b-zahlungen-bei-zahlungsunfahigkeit-und-uberschuldung-v` | § 15b InsO (Zahlungen bei Zahlungsunfähigkeit und Überschuldung; Verjährung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p016-eroffnungsgrund` | § 16 InsO (Eröffnungsgrund) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p017-zahlungsunfahigkeit` | § 17 InsO (Zahlungsunfähigkeit) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p018-drohende-zahlungsunfahigkeit` | § 18 InsO (Drohende Zahlungsunfähigkeit) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p019-uberschuldung` | § 19 InsO (Überschuldung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p020-auskunfts-und-mitwirkungspflicht-im-eroffnungsverfahre` | § 20 InsO (Auskunfts- und Mitwirkungspflicht im Eröffnungsverfahren. Hinweis auf Restschuldbefreiung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p021-anordnung-vorlaufiger-massnahmen` | § 21 InsO (Anordnung vorläufiger Maßnahmen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p022-rechtsstellung-des-vorlaufigen-insolvenzverwalters` | § 22 InsO (Rechtsstellung des vorläufigen Insolvenzverwalters) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p022a-bestellung-eines-vorlaufigen-glaubigerausschusses` | § 22a InsO (Bestellung eines vorläufigen Gläubigerausschusses) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p023-bekanntmachung-der-verfugungsbeschrankungen` | § 23 InsO (Bekanntmachung der Verfügungsbeschränkungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p024-wirkungen-der-verfugungsbeschrankungen` | § 24 InsO (Wirkungen der Verfügungsbeschränkungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p025-aufhebung-der-sicherungsmassnahmen` | § 25 InsO (Aufhebung der Sicherungsmaßnahmen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p026-abweisung-mangels-masse` | § 26 InsO (Abweisung mangels Masse) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p026a-vergutung-des-vorlaufigen-insolvenzverwalters` | § 26a InsO (Vergütung des vorläufigen Insolvenzverwalters) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p027-eroffnungsbeschluss` | § 27 InsO (Eröffnungsbeschluß) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p028-aufforderungen-an-die-glaubiger-und-die-schuldner` | § 28 InsO (Aufforderungen an die Gläubiger und die Schuldner) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p029-terminbestimmungen` | § 29 InsO (Terminbestimmungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p030-bekanntmachung-des-eroffnungsbeschlusses` | § 30 InsO (Bekanntmachung des Eröffnungsbeschlusses) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p031-handels-genossenschafts-gesellschafts-partnerschafts-o` | § 31 InsO (Handels-, Genossenschafts-, Gesellschafts-, Partnerschafts- oder Vereinsregister) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p032-grundbuch` | § 32 InsO (Grundbuch) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p033-register-fur-schiffe-und-luftfahrzeuge` | § 33 InsO (Register für Schiffe und Luftfahrzeuge) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p034-rechtsmittel` | § 34 InsO (Rechtsmittel) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p035-begriff-der-insolvenzmasse` | § 35 InsO (Begriff der Insolvenzmasse) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p036-unpfandbare-gegenstande` | § 36 InsO (Unpfändbare Gegenstände) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p037-gesamtgut-bei-gutergemeinschaft` | § 37 InsO (Gesamtgut bei Gütergemeinschaft) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p038-begriff-der-insolvenzglaubiger` | § 38 InsO (Begriff der Insolvenzgläubiger) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p039-nachrangige-insolvenzglaubiger` | § 39 InsO (Nachrangige Insolvenzgläubiger) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p040-unterhaltsanspruche` | § 40 InsO (Unterhaltsansprüche) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p041-nicht-fallige-forderungen` | § 41 InsO (Nicht fällige Forderungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p042-auflosend-bedingte-forderungen` | § 42 InsO (Auflösend bedingte Forderungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p043-haftung-mehrerer-personen` | § 43 InsO (Haftung mehrerer Personen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p044-rechte-der-gesamtschuldner-und-burgen` | § 44 InsO (Rechte der Gesamtschuldner und Bürgen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p044a-gesicherte-darlehen` | § 44a InsO (Gesicherte Darlehen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p045-umrechnung-von-forderungen` | § 45 InsO (Umrechnung von Forderungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p046-wiederkehrende-leistungen` | § 46 InsO (Wiederkehrende Leistungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p047-aussonderung` | § 47 InsO (Aussonderung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p048-ersatzaussonderung` | § 48 InsO (Ersatzaussonderung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p049-abgesonderte-befriedigung-aus-unbeweglichen-gegenstand` | § 49 InsO (Abgesonderte Befriedigung aus unbeweglichen Gegenständen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p050-abgesonderte-befriedigung-der-pfandglaubiger` | § 50 InsO (Abgesonderte Befriedigung der Pfandgläubiger) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p051-sonstige-absonderungsberechtigte` | § 51 InsO (Sonstige Absonderungsberechtigte) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p052-ausfall-der-absonderungsberechtigten` | § 52 InsO (Ausfall der Absonderungsberechtigten) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p053-masseglaubiger` | § 53 InsO (Massegläubiger) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p054-kosten-des-insolvenzverfahrens` | § 54 InsO (Kosten des Insolvenzverfahrens) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p055-sonstige-masseverbindlichkeiten` | § 55 InsO (Sonstige Masseverbindlichkeiten) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p056-bestellung-des-insolvenzverwalters` | § 56 InsO (Bestellung des Insolvenzverwalters) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p056a-glaubigerbeteiligung-bei-der-verwalterbestellung` | § 56a InsO (Gläubigerbeteiligung bei der Verwalterbestellung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p056b-verwalterbestellung-bei-schuldnern-derselben-unterneh` | § 56b InsO (Verwalterbestellung bei Schuldnern derselben Unternehmensgruppe) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p057-wahl-eines-anderen-insolvenzverwalters` | § 57 InsO (Wahl eines anderen Insolvenzverwalters) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p058-aufsicht-des-insolvenzgerichts` | § 58 InsO (Aufsicht des Insolvenzgerichts) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p059-entlassung-des-insolvenzverwalters` | § 59 InsO (Entlassung des Insolvenzverwalters) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p060-haftung-des-insolvenzverwalters` | § 60 InsO (Haftung des Insolvenzverwalters) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p061-nichterfullung-von-masseverbindlichkeiten` | § 61 InsO (Nichterfüllung von Masseverbindlichkeiten) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p062-verjahrung` | § 62 InsO (Verjährung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p063-vergutung-des-insolvenzverwalters` | § 63 InsO (Vergütung des Insolvenzverwalters) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p064-festsetzung-durch-das-gericht` | § 64 InsO (Festsetzung durch das Gericht) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p065-verordnungsermachtigung` | § 65 InsO (Verordnungsermächtigung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p066-rechnungslegung` | § 66 InsO (Rechnungslegung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p067-einsetzung-des-glaubigerausschusses` | § 67 InsO (Einsetzung des Gläubigerausschusses) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p068-wahl-anderer-mitglieder` | § 68 InsO (Wahl anderer Mitglieder) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p069-aufgaben-des-glaubigerausschusses` | § 69 InsO (Aufgaben des Gläubigerausschusses) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p070-entlassung` | § 70 InsO (Entlassung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p071-haftung-der-mitglieder-des-glaubigerausschusses` | § 71 InsO (Haftung der Mitglieder des Gläubigerausschusses) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p072-beschlusse-des-glaubigerausschusses` | § 72 InsO (Beschlüsse des Gläubigerausschusses) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p073-vergutung-der-mitglieder-des-glaubigerausschusses` | § 73 InsO (Vergütung der Mitglieder des Gläubigerausschusses) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p074-einberufung-der-glaubigerversammlung` | § 74 InsO (Einberufung der Gläubigerversammlung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p075-antrag-auf-einberufung` | § 75 InsO (Antrag auf Einberufung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p076-beschlusse-der-glaubigerversammlung` | § 76 InsO (Beschlüsse der Gläubigerversammlung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p077-feststellung-des-stimmrechts` | § 77 InsO (Feststellung des Stimmrechts) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p078-aufhebung-eines-beschlusses-der-glaubigerversammlung` | § 78 InsO (Aufhebung eines Beschlusses der Gläubigerversammlung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p079-unterrichtung-der-glaubigerversammlung` | § 79 InsO (Unterrichtung der Gläubigerversammlung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p080-ubergang-des-verwaltungs-und-verfugungsrechts` | § 80 InsO (Übergang des Verwaltungs- und Verfügungsrechts) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p081-verfugungen-des-schuldners` | § 81 InsO (Verfügungen des Schuldners) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p082-leistungen-an-den-schuldner` | § 82 InsO (Leistungen an den Schuldner) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p083-erbschaft-fortgesetzte-gutergemeinschaft` | § 83 InsO (Erbschaft. Fortgesetzte Gütergemeinschaft) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p084-auseinandersetzung-einer-gesellschaft-oder-gemeinschaf` | § 84 InsO (Auseinandersetzung einer Gesellschaft oder Gemeinschaft) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p085-aufnahme-von-aktivprozessen` | § 85 InsO (Aufnahme von Aktivprozessen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p086-aufnahme-bestimmter-passivprozesse` | § 86 InsO (Aufnahme bestimmter Passivprozesse) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p087-forderungen-der-insolvenzglaubiger` | § 87 InsO (Forderungen der Insolvenzgläubiger) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p088-vollstreckung-vor-verfahrenseroffnung` | § 88 InsO (Vollstreckung vor Verfahrenseröffnung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p089-vollstreckungsverbot` | § 89 InsO (Vollstreckungsverbot) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p090-vollstreckungsverbot-bei-masseverbindlichkeiten` | § 90 InsO (Vollstreckungsverbot bei Masseverbindlichkeiten) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p091-ausschluss-sonstigen-rechtserwerbs` | § 91 InsO (Ausschluß sonstigen Rechtserwerbs) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p092-gesamtschaden` | § 92 InsO (Gesamtschaden) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p093-personliche-haftung-der-gesellschafter` | § 93 InsO (Persönliche Haftung der Gesellschafter) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p094-erhaltung-einer-aufrechnungslage` | § 94 InsO (Erhaltung einer Aufrechnungslage) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p095-eintritt-der-aufrechnungslage-im-verfahren` | § 95 InsO (Eintritt der Aufrechnungslage im Verfahren) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p096-unzulassigkeit-der-aufrechnung` | § 96 InsO (Unzulässigkeit der Aufrechnung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p097-auskunfts-und-mitwirkungspflichten-des-schuldners` | § 97 InsO (Auskunfts- und Mitwirkungspflichten des Schuldners) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p098-durchsetzung-der-pflichten-des-schuldners` | § 98 InsO (Durchsetzung der Pflichten des Schuldners) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p099-postsperre` | § 99 InsO (Postsperre) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p100-unterhalt-aus-der-insolvenzmasse` | § 100 InsO (Unterhalt aus der Insolvenzmasse) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p101-organschaftliche-vertreter-angestellte` | § 101 InsO (Organschaftliche Vertreter. Angestellte) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p102-einschrankung-eines-grundrechts` | § 102 InsO (Einschränkung eines Grundrechts) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p103-wahlrecht-des-insolvenzverwalters` | § 103 InsO (Wahlrecht des Insolvenzverwalters) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p104-fixgeschafte-finanzleistungen-vertragliches-liquidatio` | § 104 InsO (Fixgeschäfte, Finanzleistungen, vertragliches Liquidationsnetting) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p105-teilbare-leistungen` | § 105 InsO (Teilbare Leistungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p106-vormerkung` | § 106 InsO (Vormerkung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p107-eigentumsvorbehalt` | § 107 InsO (Eigentumsvorbehalt) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p108-fortbestehen-bestimmter-schuldverhaltnisse` | § 108 InsO (Fortbestehen bestimmter Schuldverhältnisse) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p109-schuldner-als-mieter-oder-pachter` | § 109 InsO (Schuldner als Mieter oder Pächter) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p110-schuldner-als-vermieter-oder-verpachter` | § 110 InsO (Schuldner als Vermieter oder Verpächter) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p111-verausserung-des-miet-oder-pachtobjekts` | § 111 InsO (Veräußerung des Miet- oder Pachtobjekts) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p112-kundigungssperre` | § 112 InsO (Kündigungssperre) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p113-kundigung-eines-dienstverhaltnisses` | § 113 InsO (Kündigung eines Dienstverhältnisses) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p114-weggefallen` | § 114 InsO ist im aktuellen Normtext weggefallen. Der Skill hilft, Altakten, Übergangsfälle und Nachfolgeregelungen ohne falsche Altfassungsübernahme einzuordnen. |
| `inso-p115-erloschen-von-auftragen` | § 115 InsO (Erlöschen von Aufträgen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p116-erloschen-von-geschaftsbesorgungsvertragen` | § 116 InsO (Erlöschen von Geschäftsbesorgungsverträgen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p117-erloschen-von-vollmachten` | § 117 InsO (Erlöschen von Vollmachten) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p118-auflosung-von-gesellschaften` | § 118 InsO (Auflösung von Gesellschaften) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p119-unwirksamkeit-abweichender-vereinbarungen` | § 119 InsO (Unwirksamkeit abweichender Vereinbarungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p120-kundigung-von-betriebsvereinbarungen` | § 120 InsO (Kündigung von Betriebsvereinbarungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p121-betriebsanderungen-und-vermittlungsverfahren` | § 121 InsO (Betriebsänderungen und Vermittlungsverfahren) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p122-gerichtliche-zustimmung-zur-durchfuhrung-einer-betrieb` | § 122 InsO (Gerichtliche Zustimmung zur Durchführung einer Betriebsänderung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p123-umfang-des-sozialplans` | § 123 InsO (Umfang des Sozialplans) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p124-sozialplan-vor-verfahrenseroffnung` | § 124 InsO (Sozialplan vor Verfahrenseröffnung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p125-interessenausgleich-und-kundigungsschutz` | § 125 InsO (Interessenausgleich und Kündigungsschutz) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p126-beschlussverfahren-zum-kundigungsschutz` | § 126 InsO (Beschlußverfahren zum Kündigungsschutz) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p127-klage-des-arbeitnehmers` | § 127 InsO (Klage des Arbeitnehmers) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p128-betriebsverausserung` | § 128 InsO (Betriebsveräußerung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p129-grundsatz` | § 129 InsO (Grundsatz) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p130-kongruente-deckung` | § 130 InsO (Kongruente Deckung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p131-inkongruente-deckung` | § 131 InsO (Inkongruente Deckung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p132-unmittelbar-nachteilige-rechtshandlungen` | § 132 InsO (Unmittelbar nachteilige Rechtshandlungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p133-vorsatzliche-benachteiligung` | § 133 InsO (Vorsätzliche Benachteiligung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p134-unentgeltliche-leistung` | § 134 InsO (Unentgeltliche Leistung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p135-gesellschafterdarlehen` | § 135 InsO (Gesellschafterdarlehen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p136-stille-gesellschaft` | § 136 InsO (Stille Gesellschaft) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p137-wechsel-und-scheckzahlungen` | § 137 InsO (Wechsel- und Scheckzahlungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p138-nahestehende-personen` | § 138 InsO (Nahestehende Personen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p139-berechnung-der-fristen-vor-dem-eroffnungsantrag` | § 139 InsO (Berechnung der Fristen vor dem Eröffnungsantrag) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p140-zeitpunkt-der-vornahme-einer-rechtshandlung` | § 140 InsO (Zeitpunkt der Vornahme einer Rechtshandlung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p141-vollstreckbarer-titel` | § 141 InsO (Vollstreckbarer Titel) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p142-bargeschaft` | § 142 InsO (Bargeschäft) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p143-rechtsfolgen` | § 143 InsO (Rechtsfolgen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p144-anspruche-des-anfechtungsgegners` | § 144 InsO (Ansprüche des Anfechtungsgegners) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p145-anfechtung-gegen-rechtsnachfolger` | § 145 InsO (Anfechtung gegen Rechtsnachfolger) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p146-verjahrung-des-anfechtungsanspruchs` | § 146 InsO (Verjährung des Anfechtungsanspruchs) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p147-rechtshandlungen-nach-verfahrenseroffnung` | § 147 InsO (Rechtshandlungen nach Verfahrenseröffnung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p148-ubernahme-der-insolvenzmasse` | § 148 InsO (Übernahme der Insolvenzmasse) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p149-wertgegenstande` | § 149 InsO (Wertgegenstände) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p150-siegelung` | § 150 InsO (Siegelung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p151-verzeichnis-der-massegegenstande` | § 151 InsO (Verzeichnis der Massegegenstände) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p152-glaubigerverzeichnis` | § 152 InsO (Gläubigerverzeichnis) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p153-vermogensubersicht` | § 153 InsO (Vermögensübersicht) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p154-niederlegung-in-der-geschaftsstelle` | § 154 InsO (Niederlegung in der Geschäftsstelle) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p155-handels-und-steuerrechtliche-rechnungslegung` | § 155 InsO (Handels- und steuerrechtliche Rechnungslegung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p156-berichtstermin` | § 156 InsO (Berichtstermin) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p157-entscheidung-uber-den-fortgang-des-verfahrens` | § 157 InsO (Entscheidung über den Fortgang des Verfahrens) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p158-massnahmen-vor-der-entscheidung` | § 158 InsO (Maßnahmen vor der Entscheidung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p159-verwertung-der-insolvenzmasse` | § 159 InsO (Verwertung der Insolvenzmasse) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p160-besonders-bedeutsame-rechtshandlungen` | § 160 InsO (Besonders bedeutsame Rechtshandlungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p161-vorlaufige-untersagung-der-rechtshandlung` | § 161 InsO (Vorläufige Untersagung der Rechtshandlung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p162-betriebsverausserung-an-besonders-interessierte` | § 162 InsO (Betriebsveräußerung an besonders Interessierte) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p163-betriebsverausserung-unter-wert` | § 163 InsO (Betriebsveräußerung unter Wert) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p164-wirksamkeit-der-handlung` | § 164 InsO (Wirksamkeit der Handlung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p165-verwertung-unbeweglicher-gegenstande` | § 165 InsO (Verwertung unbeweglicher Gegenstände) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p166-verwertung-beweglicher-gegenstande` | § 166 InsO (Verwertung beweglicher Gegenstände) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p167-unterrichtung-des-glaubigers` | § 167 InsO (Unterrichtung des Gläubigers) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p168-mitteilung-der-verausserungsabsicht` | § 168 InsO (Mitteilung der Veräußerungsabsicht) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p169-schutz-des-glaubigers-vor-einer-verzogerung-der-verwer` | § 169 InsO (Schutz des Gläubigers vor einer Verzögerung der Verwertung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p170-verteilung-des-erloses` | § 170 InsO (Verteilung des Erlöses) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p171-berechnung-des-kostenbeitrags` | § 171 InsO (Berechnung des Kostenbeitrags) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p172-sonstige-verwendung-beweglicher-sachen` | § 172 InsO (Sonstige Verwendung beweglicher Sachen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p173-verwertung-durch-den-glaubiger` | § 173 InsO (Verwertung durch den Gläubiger) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p174-anmeldung-der-forderungen` | § 174 InsO (Anmeldung der Forderungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p175-tabelle` | § 175 InsO (Tabelle) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p176-verlauf-des-prufungstermins` | § 176 InsO (Verlauf des Prüfungstermins) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p177-nachtragliche-anmeldungen` | § 177 InsO (Nachträgliche Anmeldungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p178-voraussetzungen-und-wirkungen-der-feststellung` | § 178 InsO (Voraussetzungen und Wirkungen der Feststellung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p179-streitige-forderungen` | § 179 InsO (Streitige Forderungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p180-zustandigkeit-fur-die-feststellung` | § 180 InsO (Zuständigkeit für die Feststellung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p181-umfang-der-feststellung` | § 181 InsO (Umfang der Feststellung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p182-streitwert` | § 182 InsO (Streitwert) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p183-wirkung-der-entscheidung` | § 183 InsO (Wirkung der Entscheidung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p184-klage-gegen-einen-widerspruch-des-schuldners` | § 184 InsO (Klage gegen einen Widerspruch des Schuldners) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p185-besondere-zustandigkeiten` | § 185 InsO (Besondere Zuständigkeiten) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p186-wiedereinsetzung-in-den-vorigen-stand` | § 186 InsO (Wiedereinsetzung in den vorigen Stand) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p187-befriedigung-der-insolvenzglaubiger` | § 187 InsO (Befriedigung der Insolvenzgläubiger) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p188-verteilungsverzeichnis` | § 188 InsO (Verteilungsverzeichnis) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p189-berucksichtigung-bestrittener-forderungen` | § 189 InsO (Berücksichtigung bestrittener Forderungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p190-berucksichtigung-absonderungsberechtigter-glaubiger` | § 190 InsO (Berücksichtigung absonderungsberechtigter Gläubiger) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p191-berucksichtigung-aufschiebend-bedingter-forderungen` | § 191 InsO (Berücksichtigung aufschiebend bedingter Forderungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p192-nachtragliche-berucksichtigung` | § 192 InsO (Nachträgliche Berücksichtigung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p193-anderung-des-verteilungsverzeichnisses` | § 193 InsO (Änderung des Verteilungsverzeichnisses) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p194-einwendungen-gegen-das-verteilungsverzeichnis` | § 194 InsO (Einwendungen gegen das Verteilungsverzeichnis) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p195-festsetzung-des-bruchteils` | § 195 InsO (Festsetzung des Bruchteils) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p196-schlussverteilung` | § 196 InsO (Schlußverteilung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p197-schlusstermin` | § 197 InsO (Schlußtermin) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p198-hinterlegung-zuruckbehaltener-betrage` | § 198 InsO (Hinterlegung zurückbehaltener Beträge) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p199-uberschuss-bei-der-schlussverteilung` | § 199 InsO (Überschuß bei der Schlußverteilung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p200-aufhebung-des-insolvenzverfahrens` | § 200 InsO (Aufhebung des Insolvenzverfahrens) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p201-rechte-der-insolvenzglaubiger-nach-verfahrensaufhebung` | § 201 InsO (Rechte der Insolvenzgläubiger nach Verfahrensaufhebung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p202-zustandigkeit-bei-der-vollstreckung` | § 202 InsO (Zuständigkeit bei der Vollstreckung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p203-anordnung-der-nachtragsverteilung` | § 203 InsO (Anordnung der Nachtragsverteilung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p204-rechtsmittel` | § 204 InsO (Rechtsmittel) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p205-vollzug-der-nachtragsverteilung` | § 205 InsO (Vollzug der Nachtragsverteilung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p206-ausschluss-von-masseglaubigern` | § 206 InsO (Ausschluß von Massegläubigern) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p207-einstellung-mangels-masse` | § 207 InsO (Einstellung mangels Masse) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p208-anzeige-der-masseunzulanglichkeit` | § 208 InsO (Anzeige der Masseunzulänglichkeit) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p209-befriedigung-der-masseglaubiger` | § 209 InsO (Befriedigung der Massegläubiger) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p210-vollstreckungsverbot` | § 210 InsO (Vollstreckungsverbot) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p210a-insolvenzplan-bei-masseunzulanglichkeit` | § 210a InsO (Insolvenzplan bei Masseunzulänglichkeit) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p211-einstellung-nach-anzeige-der-masseunzulanglichkeit` | § 211 InsO (Einstellung nach Anzeige der Masseunzulänglichkeit) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p212-einstellung-wegen-wegfalls-des-eroffnungsgrunds` | § 212 InsO (Einstellung wegen Wegfalls des Eröffnungsgrunds) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p213-einstellung-mit-zustimmung-der-glaubiger` | § 213 InsO (Einstellung mit Zustimmung der Gläubiger) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p214-verfahren-bei-der-einstellung` | § 214 InsO (Verfahren bei der Einstellung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p215-bekanntmachung-und-wirkungen-der-einstellung` | § 215 InsO (Bekanntmachung und Wirkungen der Einstellung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p216-rechtsmittel` | § 216 InsO (Rechtsmittel) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p217-grundsatz` | § 217 InsO (Grundsatz) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p218-vorlage-des-insolvenzplans` | § 218 InsO (Vorlage des Insolvenzplans) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p219-gliederung-des-plans` | § 219 InsO (Gliederung des Plans) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p220-darstellender-teil` | § 220 InsO (Darstellender Teil) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p221-gestaltender-teil` | § 221 InsO (Gestaltender Teil) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p222-bildung-von-gruppen` | § 222 InsO (Bildung von Gruppen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p223-rechte-der-absonderungsberechtigten` | § 223 InsO (Rechte der Absonderungsberechtigten) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p223a-gruppeninterne-drittsicherheiten` | § 223a InsO (Gruppeninterne Drittsicherheiten) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p224-rechte-der-insolvenzglaubiger` | § 224 InsO (Rechte der Insolvenzgläubiger) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p225-rechte-der-nachrangigen-insolvenzglaubiger` | § 225 InsO (Rechte der nachrangigen Insolvenzgläubiger) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p225a-rechte-der-anteilsinhaber` | § 225a InsO (Rechte der Anteilsinhaber) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p226-gleichbehandlung-der-beteiligten` | § 226 InsO (Gleichbehandlung der Beteiligten) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p227-haftung-des-schuldners` | § 227 InsO (Haftung des Schuldners) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p228-anderung-sachenrechtlicher-verhaltnisse` | § 228 InsO (Änderung sachenrechtlicher Verhältnisse) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p229-vermogensubersicht-ergebnis-und-finanzplan` | § 229 InsO (Vermögensübersicht. Ergebnis- und Finanzplan) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p230-weitere-anlagen` | § 230 InsO (Weitere Anlagen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p231-zuruckweisung-des-plans` | § 231 InsO (Zurückweisung des Plans) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p232-stellungnahmen-zum-plan` | § 232 InsO (Stellungnahmen zum Plan) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p233-aussetzung-von-verwertung-und-verteilung` | § 233 InsO (Aussetzung von Verwertung und Verteilung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p234-niederlegung-des-plans` | § 234 InsO (Niederlegung des Plans) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p235-erorterungs-und-abstimmungstermin` | § 235 InsO (Erörterungs- und Abstimmungstermin) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p236-verbindung-mit-dem-prufungstermin` | § 236 InsO (Verbindung mit dem Prüfungstermin) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p237-stimmrecht-der-insolvenzglaubiger` | § 237 InsO (Stimmrecht der Insolvenzgläubiger) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p238-stimmrecht-der-absonderungsberechtigten-glaubiger` | § 238 InsO (Stimmrecht der absonderungsberechtigten Gläubiger) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p238a-stimmrecht-der-anteilsinhaber` | § 238a InsO (Stimmrecht der Anteilsinhaber) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p238b-stimmrecht-der-berechtigten-aus-gruppeninternen-dritt` | § 238b InsO (Stimmrecht der Berechtigten aus gruppeninternen Drittsicherheiten) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p239-stimmliste` | § 239 InsO (Stimmliste) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p240-anderung-des-plans` | § 240 InsO (Änderung des Plans) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p241-gesonderter-abstimmungstermin` | § 241 InsO (Gesonderter Abstimmungstermin) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p242-schriftliche-abstimmung` | § 242 InsO (Schriftliche Abstimmung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p243-abstimmung-in-gruppen` | § 243 InsO (Abstimmung in Gruppen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p244-erforderliche-mehrheiten` | § 244 InsO (Erforderliche Mehrheiten) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p245-obstruktionsverbot` | § 245 InsO (Obstruktionsverbot) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p245a-schlechterstellung-bei-naturlichen-personen` | § 245a InsO (Schlechterstellung bei natürlichen Personen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p246-zustimmung-nachrangiger-insolvenzglaubiger` | § 246 InsO (Zustimmung nachrangiger Insolvenzgläubiger) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p246a-zustimmung-der-anteilsinhaber` | § 246a InsO (Zustimmung der Anteilsinhaber) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p247-zustimmung-des-schuldners` | § 247 InsO (Zustimmung des Schuldners) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p248-gerichtliche-bestatigung` | § 248 InsO (Gerichtliche Bestätigung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p248a-gerichtliche-bestatigung-einer-planberichtigung` | § 248a InsO (Gerichtliche Bestätigung einer Planberichtigung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p249-bedingter-plan` | § 249 InsO (Bedingter Plan) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p250-verstoss-gegen-verfahrensvorschriften` | § 250 InsO (Verstoß gegen Verfahrensvorschriften) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p251-minderheitenschutz` | § 251 InsO (Minderheitenschutz) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p252-bekanntgabe-der-entscheidung` | § 252 InsO (Bekanntgabe der Entscheidung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p253-rechtsmittel` | § 253 InsO (Rechtsmittel) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p254-allgemeine-wirkungen-des-plans` | § 254 InsO (Allgemeine Wirkungen des Plans) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p254a-rechte-an-gegenstanden-sonstige-wirkungen-des-plans` | § 254a InsO (Rechte an Gegenständen. Sonstige Wirkungen des Plans) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p254b-wirkung-fur-alle-beteiligten` | § 254b InsO (Wirkung für alle Beteiligten) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p255-wiederauflebensklausel` | § 255 InsO (Wiederauflebensklausel) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p256-streitige-forderungen-ausfallforderungen` | § 256 InsO (Streitige Forderungen. Ausfallforderungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p257-vollstreckung-aus-dem-plan` | § 257 InsO (Vollstreckung aus dem Plan) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p258-aufhebung-des-insolvenzverfahrens` | § 258 InsO (Aufhebung des Insolvenzverfahrens) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p259-wirkungen-der-aufhebung` | § 259 InsO (Wirkungen der Aufhebung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p259a-vollstreckungsschutz` | § 259a InsO (Vollstreckungsschutz) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p259b-besondere-verjahrungsfrist` | § 259b InsO (Besondere Verjährungsfrist) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p260-uberwachung-der-planerfullung` | § 260 InsO (Überwachung der Planerfüllung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p261-aufgaben-und-befugnisse-des-insolvenzverwalters` | § 261 InsO (Aufgaben und Befugnisse des Insolvenzverwalters) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p262-anzeigepflicht-des-insolvenzverwalters` | § 262 InsO (Anzeigepflicht des Insolvenzverwalters) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p263-zustimmungsbedurftige-geschafte` | § 263 InsO (Zustimmungsbedürftige Geschäfte) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p264-kreditrahmen` | § 264 InsO (Kreditrahmen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p265-nachrang-von-neuglaubigern` | § 265 InsO (Nachrang von Neugläubigern) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p266-berucksichtigung-des-nachrangs` | § 266 InsO (Berücksichtigung des Nachrangs) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p267-bekanntmachung-der-uberwachung` | § 267 InsO (Bekanntmachung der Überwachung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p268-aufhebung-der-uberwachung` | § 268 InsO (Aufhebung der Überwachung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p269-kosten-der-uberwachung` | § 269 InsO (Kosten der Überwachung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p269a-zusammenarbeit-der-insolvenzverwalter` | § 269a InsO (Zusammenarbeit der Insolvenzverwalter) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p269b-zusammenarbeit-der-gerichte` | § 269b InsO (Zusammenarbeit der Gerichte) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p269c-zusammenarbeit-der-glaubigerausschusse` | § 269c InsO (Zusammenarbeit der Gläubigerausschüsse) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p269d-koordinationsgericht` | § 269d InsO (Koordinationsgericht) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p269e-verfahrenskoordinator` | § 269e InsO (Verfahrenskoordinator) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p269f-aufgaben-und-rechtsstellung-des-verfahrenskoordinator` | § 269f InsO (Aufgaben und Rechtsstellung des Verfahrenskoordinators) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p269g-vergutung-des-verfahrenskoordinators` | § 269g InsO (Vergütung des Verfahrenskoordinators) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p269h-koordinationsplan` | § 269h InsO (Koordinationsplan) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p269i-abweichungen-vom-koordinationsplan` | § 269i InsO (Abweichungen vom Koordinationsplan) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p270-grundsatz` | § 270 InsO (Grundsatz) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p270a-antrag-eigenverwaltungsplanung` | § 270a InsO (Antrag; Eigenverwaltungsplanung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p270b-anordnung-der-vorlaufigen-eigenverwaltung` | § 270b InsO (Anordnung der vorläufigen Eigenverwaltung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p270c-vorlaufiges-eigenverwaltungsverfahren` | § 270c InsO (Vorläufiges Eigenverwaltungsverfahren) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p270d-vorbereitung-einer-sanierung-schutzschirm` | § 270d InsO (Vorbereitung einer Sanierung; Schutzschirm) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p270e-aufhebung-der-vorlaufigen-eigenverwaltung` | § 270e InsO (Aufhebung der vorläufigen Eigenverwaltung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p270f-anordnung-der-eigenverwaltung` | § 270f InsO (Anordnung der Eigenverwaltung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p270g-eigenverwaltung-bei-gruppenangehorigen-schuldnern` | § 270g InsO (Eigenverwaltung bei gruppenangehörigen Schuldnern) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p271-nachtragliche-anordnung` | § 271 InsO (Nachträgliche Anordnung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p272-aufhebung-der-anordnung` | § 272 InsO (Aufhebung der Anordnung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p273-offentliche-bekanntmachung` | § 273 InsO (Öffentliche Bekanntmachung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p274-rechtsstellung-des-sachwalters` | § 274 InsO (Rechtsstellung des Sachwalters) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p275-mitwirkung-des-sachwalters` | § 275 InsO (Mitwirkung des Sachwalters) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p276-mitwirkung-des-glaubigerausschusses` | § 276 InsO (Mitwirkung des Gläubigerausschusses) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p276a-mitwirkung-der-uberwachungsorgane` | § 276a InsO (Mitwirkung der Überwachungsorgane) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p277-anordnung-der-zustimmungsbedurftigkeit` | § 277 InsO (Anordnung der Zustimmungsbedürftigkeit) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p278-mittel-zur-lebensfuhrung-des-schuldners` | § 278 InsO (Mittel zur Lebensführung des Schuldners) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p279-gegenseitige-vertrage` | § 279 InsO (Gegenseitige Verträge) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p280-haftung-insolvenzanfechtung` | § 280 InsO (Haftung. Insolvenzanfechtung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p281-unterrichtung-der-glaubiger` | § 281 InsO (Unterrichtung der Gläubiger) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p282-verwertung-von-sicherungsgut` | § 282 InsO (Verwertung von Sicherungsgut) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p283-befriedigung-der-insolvenzglaubiger` | § 283 InsO (Befriedigung der Insolvenzgläubiger) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p284-insolvenzplan` | § 284 InsO (Insolvenzplan) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p285-masseunzulanglichkeit` | § 285 InsO (Masseunzulänglichkeit) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p286-grundsatz` | § 286 InsO (Grundsatz) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p287-antrag-des-schuldners` | § 287 InsO (Antrag des Schuldners) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p287a-entscheidung-des-insolvenzgerichts` | § 287a InsO (Entscheidung des Insolvenzgerichts) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p287b-erwerbsobliegenheit-des-schuldners` | § 287b InsO (Erwerbsobliegenheit des Schuldners) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p288-bestimmung-des-treuhanders` | § 288 InsO (Bestimmung des Treuhänders) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p289-einstellung-des-insolvenzverfahrens` | § 289 InsO (Einstellung des Insolvenzverfahrens) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p290-versagung-der-restschuldbefreiung` | § 290 InsO (Versagung der Restschuldbefreiung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p291-weggefallen` | § 291 InsO ist im aktuellen Normtext weggefallen. Der Skill hilft, Altakten, Übergangsfälle und Nachfolgeregelungen ohne falsche Altfassungsübernahme einzuordnen. |
| `inso-p292-rechtsstellung-des-treuhanders` | § 292 InsO (Rechtsstellung des Treuhänders) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p293-vergutung-des-treuhanders` | § 293 InsO (Vergütung des Treuhänders) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p294-gleichbehandlung-der-glaubiger` | § 294 InsO (Gleichbehandlung der Gläubiger) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p295-obliegenheiten-des-schuldners` | § 295 InsO (Obliegenheiten des Schuldners) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p295a-obliegenheiten-des-schuldners-bei-selbstandiger-tatig` | § 295a InsO (Obliegenheiten des Schuldners bei selbständiger Tätigkeit) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p296-verstoss-gegen-obliegenheiten` | § 296 InsO (Verstoß gegen Obliegenheiten) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p297-insolvenzstraftaten` | § 297 InsO (Insolvenzstraftaten) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p297a-nachtraglich-bekannt-gewordene-versagungsgrunde` | § 297a InsO (Nachträglich bekannt gewordene Versagungsgründe) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p298-deckung-der-mindestvergutung-des-treuhanders` | § 298 InsO (Deckung der Mindestvergütung des Treuhänders) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p299-vorzeitige-beendigung` | § 299 InsO (Vorzeitige Beendigung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p300-entscheidung-uber-die-restschuldbefreiung` | § 300 InsO (Entscheidung über die Restschuldbefreiung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p300a-neuerwerb-im-laufenden-insolvenzverfahren` | § 300a InsO (Neuerwerb im laufenden Insolvenzverfahren) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p301-wirkung-der-restschuldbefreiung` | § 301 InsO (Wirkung der Restschuldbefreiung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p302-ausgenommene-forderungen` | § 302 InsO (Ausgenommene Forderungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p303-widerruf-der-restschuldbefreiung` | § 303 InsO (Widerruf der Restschuldbefreiung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p303a-eintragung-in-das-schuldnerverzeichnis` | § 303a InsO (Eintragung in das Schuldnerverzeichnis) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p304-grundsatz` | § 304 InsO (Grundsatz) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p305-eroffnungsantrag-des-schuldners` | § 305 InsO (Eröffnungsantrag des Schuldners) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p305a-scheitern-der-aussergerichtlichen-schuldenbereinigung` | § 305a InsO (Scheitern der außergerichtlichen Schuldenbereinigung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p306-ruhen-des-verfahrens` | § 306 InsO (Ruhen des Verfahrens) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p307-zustellung-an-die-glaubiger` | § 307 InsO (Zustellung an die Gläubiger) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p308-annahme-des-schuldenbereinigungsplans` | § 308 InsO (Annahme des Schuldenbereinigungsplans) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p309-ersetzung-der-zustimmung` | § 309 InsO (Ersetzung der Zustimmung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p310-kosten` | § 310 InsO (Kosten) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p311-aufnahme-des-verfahrens-uber-den-eroffnungsantrag` | § 311 InsO (Aufnahme des Verfahrens über den Eröffnungsantrag) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p312bis314-weggefallen` | § 312 bis 314 InsO ist im aktuellen Normtext weggefallen. Der Skill hilft, Altakten, Übergangsfälle und Nachfolgeregelungen ohne falsche Altfassungsübernahme einzuordnen. |
| `inso-p315-ortliche-zustandigkeit` | § 315 InsO (Örtliche Zuständigkeit) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p316-zulassigkeit-der-eroffnung` | § 316 InsO (Zulässigkeit der Eröffnung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p317-antragsberechtigte` | § 317 InsO (Antragsberechtigte) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p318-antragsrecht-beim-gesamtgut` | § 318 InsO (Antragsrecht beim Gesamtgut) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p319-antragsfrist` | § 319 InsO (Antragsfrist) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p320-eroffnungsgrunde` | § 320 InsO (Eröffnungsgründe) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p321-zwangsvollstreckung-nach-erbfall` | § 321 InsO (Zwangsvollstreckung nach Erbfall) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p322-anfechtbare-rechtshandlungen-des-erben` | § 322 InsO (Anfechtbare Rechtshandlungen des Erben) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p323-aufwendungen-des-erben` | § 323 InsO (Aufwendungen des Erben) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p324-masseverbindlichkeiten` | § 324 InsO (Masseverbindlichkeiten) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p325-nachlassverbindlichkeiten` | § 325 InsO (Nachlaßverbindlichkeiten) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p326-anspruche-des-erben` | § 326 InsO (Ansprüche des Erben) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p327-nachrangige-verbindlichkeiten` | § 327 InsO (Nachrangige Verbindlichkeiten) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p328-zuruckgewahrte-gegenstande` | § 328 InsO (Zurückgewährte Gegenstände) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p329-nacherbfolge` | § 329 InsO (Nacherbfolge) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p330-erbschaftskauf` | § 330 InsO (Erbschaftskauf) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p331-gleichzeitige-insolvenz-des-erben` | § 331 InsO (Gleichzeitige Insolvenz des Erben) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p332-verweisung-auf-das-nachlassinsolvenzverfahren` | § 332 InsO (Verweisung auf das Nachlaßinsolvenzverfahren) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p333-antragsrecht-eroffnungsgrunde` | § 333 InsO (Antragsrecht. Eröffnungsgründe) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p334-personliche-haftung-der-ehegatten` | § 334 InsO (Persönliche Haftung der Ehegatten) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p335-grundsatz` | § 335 InsO (Grundsatz) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p336-vertrag-uber-einen-unbeweglichen-gegenstand` | § 336 InsO (Vertrag über einen unbeweglichen Gegenstand) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p337-arbeitsverhaltnis` | § 337 InsO (Arbeitsverhältnis) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p338-aufrechnung` | § 338 InsO (Aufrechnung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p339-insolvenzanfechtung` | § 339 InsO (Insolvenzanfechtung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p340-organisierte-markte-pensionsgeschafte` | § 340 InsO (Organisierte Märkte. Pensionsgeschäfte) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p341-ausubung-von-glaubigerrechten` | § 341 InsO (Ausübung von Gläubigerrechten) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p342-herausgabepflicht-anrechnung` | § 342 InsO (Herausgabepflicht. Anrechnung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p343-anerkennung` | § 343 InsO (Anerkennung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p344-sicherungsmassnahmen` | § 344 InsO (Sicherungsmaßnahmen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p345-offentliche-bekanntmachung` | § 345 InsO (Öffentliche Bekanntmachung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p346-grundbuch` | § 346 InsO (Grundbuch) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p347-nachweis-der-verwalterbestellung-unterrichtung-des-ger` | § 347 InsO (Nachweis der Verwalterbestellung. Unterrichtung des Gerichts) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p348-zustandiges-insolvenzgericht-zusammenarbeit-der-insolv` | § 348 InsO (Zuständiges Insolvenzgericht. Zusammenarbeit der Insolvenzgerichte) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p349-verfugungen-uber-unbewegliche-gegenstande` | § 349 InsO (Verfügungen über unbewegliche Gegenstände) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p350-leistung-an-den-schuldner` | § 350 InsO (Leistung an den Schuldner) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p351-dingliche-rechte` | § 351 InsO (Dingliche Rechte) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p352-unterbrechung-und-aufnahme-eines-rechtsstreits` | § 352 InsO (Unterbrechung und Aufnahme eines Rechtsstreits) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p353-vollstreckbarkeit-auslandischer-entscheidungen` | § 353 InsO (Vollstreckbarkeit ausländischer Entscheidungen) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p354-voraussetzungen-des-partikularverfahrens` | § 354 InsO (Voraussetzungen des Partikularverfahrens) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p355-restschuldbefreiung-insolvenzplan` | § 355 InsO (Restschuldbefreiung. Insolvenzplan) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p356-sekundarinsolvenzverfahren` | § 356 InsO (Sekundärinsolvenzverfahren) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p357-zusammenarbeit-der-insolvenzverwalter` | § 357 InsO (Zusammenarbeit der Insolvenzverwalter) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p358-uberschuss-bei-der-schlussverteilung` | § 358 InsO (Überschuss bei der Schlussverteilung) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `inso-p359-verweisung-auf-das-einfuhrungsgesetz` | § 359 InsO (Verweisung auf das Einführungsgesetz) im Mandat prüfen: Normzweck, Tatbestand, Belege, Rechtsfolge, Fristen, Schnittstellen und sichere Quellenprüfung. |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Insolvenzantrag, Anfechtungsklage, StaRUG-Restrukturierungsantrag: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau. |
| `spezial-antragspflicht-schriftsatz-brief-und-memo-bausteine` | Antragspflicht: Schriftsatz-, Brief- und Memo-Bausteine im Plugin fachanwalt insolvenz sanierungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-berater-red-team-und-qualitaetskontrolle` | Berater: Red-Team und Qualitätskontrolle im Plugin fachanwalt insolvenz sanierungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-chronologie-abschlussprodukt-und-uebergabe` | Chronologie: Abschlussprodukt und Übergabe im Plugin fachanwalt insolvenz sanierungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-eroeffnung-behoerden-gericht-und-registerweg` | Eroeffnung: Behörden-, Gerichts- oder Registerweg im Plugin fachanwalt insolvenz sanierungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-fachanwalt-erstpruefung-und-mandatsziel` | Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Plugin fachanwalt insolvenz sanierungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-fao-dokumentenmatrix-und-lueckenliste` | FAO: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin fachanwalt insolvenz sanierungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-glaeubigerantrag-verhandlung-vergleich-und-eskalation` | Glaeubigerantrag: Verhandlung, Vergleich und Eskalation im Plugin fachanwalt insolvenz sanierungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-inso-risikoampel-und-gegenargumente` | InsO: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin fachanwalt insolvenz sanierungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-insolvenz-tatbestand-beweis-und-belege` | Insolvenz: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin fachanwalt insolvenz sanierungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-insolvenzanfechtung-compliance-dokumentation-und-akte` | Insolvenzanfechtung: Compliance-Dokumentation und Aktenvermerk im Plugin fachanwalt insolvenz sanierungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprü... |
| `spezial-insolvenzrecht-internationaler-bezug-und-schnittstellen` | Insolvenzrecht: Internationaler Bezug und Schnittstellen im Plugin fachanwalt insolvenz sanierungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-krypto-mandantenkommunikation-entscheidungsvorlage` | Krypto: Mandantenkommunikation und Entscheidungsvorlage im Plugin fachanwalt insolvenz sanierungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-livecheck-fristennotiz-und-naechster-schritt` | Livecheck: Fristennotiz und nächster Schritt im Plugin fachanwalt insolvenz sanierungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-rechtsquellen-sonderfall-und-edge-case` | Rechtsquellen: Sonderfall und Edge-Case-Prüfung im Plugin fachanwalt insolvenz sanierungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-restrukturierungsplan-zahlen-schwellen-und-berechnung` | Restrukturierungsplan: Zahlen, Schwellenwerte und Berechnung im Plugin fachanwalt insolvenz sanierungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-sanierungsrecht-fristen-form-und-zustaendigkeit` | Sanierungsrecht: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin fachanwalt insolvenz sanierungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-schnittstellen-mehrparteien-konflikt-und-interessen` | Schnittstellen: Mehrparteienkonflikt und Interessenmatrix im Plugin fachanwalt insolvenz sanierungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-starug-livequellen-und-rechtsprechungscheck` | StaRUG: Livequellen- und Rechtsprechungscheck im Plugin fachanwalt insolvenz sanierungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-steuerrecht-formular-portal-und-einreichung` | Steuerrecht: Formular, Portal und Einreichungslogik im Plugin fachanwalt insolvenz sanierungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-verwertung-beweislast-und-darlegungslast` | Verwertung: Beweislast, Darlegungslast und Substantiierung im Plugin fachanwalt insolvenz sanierungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `starug-spezial-restrukturierungsplan` | StaRUG-Restrukturierungsplan im Detail: Planinhalt, Gruppenbildung, Cross-Class-Cram-Down nach § 26 StaRUG, gerichtliche Bestaetigung. Pruefraster fuer Plan, der nicht alle Glaeubigergruppen umfasst. Schnittstellen zu Insolvenzplan und v... |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlungs-Strategie für Insolvenz- und Restrukturierungsrecht: ZOPA, BATNA, Verhandlungsfenster, Druckmittel, Settlement-Skript, Vergleichsentwurf und prozessuale Absicherung (Protokoll-/Anwaltsvergleich). |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin fachanwalt-insolvenz-sanierungsrecht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin fachanwalt-insolvenz-sanierungsrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin fachanwalt-insolvenz-sanierungsrecht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin fachanwalt-insolvenz-sanierungsrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin fachanwalt-insolvenz-sanierungsrecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin fachanwalt-insolvenz-sanierungsrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin fachanwalt-insolvenz-sanierungsrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin fachanwalt-insolvenz-sanierungsrecht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin fachanwalt-insolvenz-sanierungsrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin fachanwalt-insolvenz-sanierungsrecht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
