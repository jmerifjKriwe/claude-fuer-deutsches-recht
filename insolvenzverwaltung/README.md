# Insolvenzverwaltung - IV-Cockpit

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`insolvenzverwaltung`) | [`insolvenzverwaltung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzverwaltung.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Insolvenzverwaltung – Möbelwerk Havelberg GmbH** (`insolvenzverwaltung-moebelwerk-havelberg-regelverfahren`) | [Gesamt-PDF lesen](../testakten/insolvenzverwaltung-moebelwerk-havelberg-regelverfahren/gesamt-pdf/insolvenzverwaltung-moebelwerk-havelberg-regelverfahren_gesamt.pdf) | [`testakte-insolvenzverwaltung-moebelwerk-havelberg-regelverfahren.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-insolvenzverwaltung-moebelwerk-havelberg-regelverfahren.zip) |
| **Insolvenzverwaltung Nordlicht Handels GmbH** (`insolvenzverwaltung-nordlicht-handels-kiel`) | [Gesamt-PDF lesen](../testakten/insolvenzverwaltung-nordlicht-handels-kiel/gesamt-pdf/insolvenzverwaltung-nordlicht-handels-kiel_gesamt.pdf) | [`testakte-insolvenzverwaltung-nordlicht-handels-kiel.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-insolvenzverwaltung-nordlicht-handels-kiel.zip) |
| **LUMEN Studios GmbH — Insolvenz- und Wirtschaftsstrafverfahren** (`lumen-studios-insolvenz-strafverfahren`) | [Gesamt-PDF lesen](../testakten/lumen-studios-insolvenz-strafverfahren/gesamt-pdf/lumen-studios-insolvenz-strafverfahren_gesamt.pdf) | [`testakte-lumen-studios-insolvenz-strafverfahren.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-lumen-studios-insolvenz-strafverfahren.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Technischer Plugin-Name: `insolvenzverwaltung`.

Großes freistehendes Plugin für die Insolvenzverwaltung aus Sicht des Insolvenzverwalters, vorläufigen Insolvenzverwalters und Sachwalters. Abgebildet sind Regelverfahren, Eröffnungsverfahren, Schutzschirm, Eigenverwaltung, Masseeinsammlung, Massemehrung, Insolvenzanfechtung, Zahlungsklagen nach § 15b InsO, Forderungsanmeldungsprüfung, Tabelle, Anzeige der Masseunzulänglichkeit, Betriebsfortführung, Insolvenzplan, StaRUG-Restrukturierungsplan, Vergleichsrechnung, Berichte, Schlussrechnung und Verteilung.

**Freistehend:** Dieses Plugin enthält eigene Skills, Vorlagen, Quellenhinweise, Vorschau und Testakte. Es verweist nicht auf andere Plugins als Voraussetzung.

## Installation

1. ZIP aus dem Release herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `insolvenzverwaltung.zip` hochladen.
5. Mit einem konkreten Auftrag starten, zum Beispiel: `Starte das Insolvenzverwaltungs-Kommandocenter für diese neue IV-Akte.`

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` enthalten.

#

## Kernmodule

| Modul | Funktion |
| Verfahrenscockpit | Aktenanlage, Rollen, Fristen, Beschlussauswertung, Workstreams und Gerichtskommunikation. |
| Gutachten und Eröffnung | Eröffnungsgründe, Massekostendeckung, Sicherungsmaßnahmen und Empfehlung. |
| Masse und Verwertung | Masseeinsammlung, Massemehrung, Verwertung, Fortführung, Drittschuldner und Vergleich. |
| Ansprüche | Insolvenzanfechtung, § 15b InsO, D&O, Zahlungsanalyse, Klage- und Vergleichspfad. |
| Tabelle | Forderungsanmeldung, Belegprüfung, Rang, Widerspruch, Prüfungstermin und Feststellung. |
| Bericht und Abschluss | Zwischenbericht, Ausschussbericht, Anzeige § 208 InsO, Schlussbericht, Schlussrechnung und Verteilung. |
| Insolvenzplan und StaRUG | IV-integrierte Planwerkstatt mit Sanierungskonzept, Vergleichsrechnung, Gruppen/Klassen, darstellendem und gestaltendem Teil, Anlagen, Abstimmung, Cram-down, Minderheitenschutz und Planvollzug. |

## Skill-Landkarte

| Skill | Zweck |
| `iv-kommandocenter` | Erkennt Verfahrensart, Rolle, rote Schwellen und nächste sichere Aktion. |
| `iv-aktenanlage-verfahrenscockpit` | Legt eine vollständige Verfahrensakte mit Tabellen, Konten und Workstreams an. |
| `iv-eroeffnungsgutachten` | Strukturiert Eröffnungsgrund, Massekostendeckung, Sicherung und Fortführung. |
| `iv-vorlaeufige-verwaltung` | Steuert Zustimmungsvorbehalt, Kasse, Post, Banken und Sofortmaßnahmen. |
| `iv-sicherung-betriebsfortfuehrung` | Baut Wochenplan, Cash-Bridge, Lieferantenampel und Insolvenzgeldpfad. |
| `iv-regelverfahren-eroeffnung` | Ordnet eröffnetes Regelverfahren, Masse, Tabelle, Berichte und Verwertung. |
| `iv-eigenverwaltung-sachwaltung` | Trennt Schuldnerverwaltung, Sachwalterkontrolle, Haftung und Anfechtung. |
| `iv-schutzschirm-270d` | Prüft Bescheinigung, Frist, Planreife und Anzeige der Zahlungsunfähigkeit. |
| `iv-masseeinsammlung` | Sammelt Forderungen, Konten, Herausgabeansprüche, Rückstände und Drittrechte. |
| `iv-massemehrung-asset-realisation` | Entwickelt Verwertungs-, Vergleichs-, Prozess- und Fortführungsoptionen. |
| `iv-anfechtung-129ff` | Prüft Deckung, Vorsatz, Gesellschafterdarlehen, Bargeschäft und Klagepfad. |
| `iv-zahlungsklagen-15b` | Rekonstruiert Insolvenzreife, Zahlungen, Ausnahmen, Schaden und Klage. |
| `iv-forderungsanmeldung-pruefung` | Prüft Forderungsanmeldungen auf Grund, Betrag, Rang, Belege und vbuH. |
| `iv-tabelle-pruefungstermin` | Bereitet Prüfungstermin, Widersprüche, Auszüge und Feststellungsklagen vor. |
| `iv-masseunzulaenglichkeit-208` | Prüft Anzeige, Rang, Zahlungsstopp, Kommunikation und Fortverwaltung. |
| `iv-arbeitsrecht-insolvenzgeld` | Ordnet Löhne, Insolvenzgeld, Kündigungen, Betriebsrat und Personalmaßnahmen. |
| `iv-steuern-sozialversicherung` | Prüft Steuerforderungen, Masseverbindlichkeiten, § 15b-Ausnahmen und SV. |
| `iv-berichte-gericht-glaeubiger` | Erstellt Zwischenberichte, Ausschussberichte, Sachstandsberichte und Beschlussvorlagen. |
| `iv-verteilung-schlussrechnung` | Bereitet Schlussbericht, Schlussrechnung, Verteilung und Nachtragsverteilung vor. |
| `iv-qualitaets-und-plausibilitaetsgate` | Findet Lücken, Widersprüche, Fristen, Rechenfehler und Rollenverwechslungen. |

## IV-integrierte Planwerkstatt

Die Planwerkstatt aus dem freien Plugin ist inhaltlich vollständig auch in diesem Insolvenzverwaltungs-Plugin enthalten. Die Skills tragen hier bewusst den Präfix `iv-plan-`, damit bei paralleler Installation keine Namenskollision mit dem freistehenden Plugin entsteht. Inhaltlich bleibt der Workflow gleich: Intake, Sanierungskonzept, integrierte Planung, Vergleichsrechnung, Insolvenzplan, StaRUG-Plan, Gruppen/Klassen, Anlagen, Abstimmung, Cram-down, Minderheitenschutz, Gericht und Vollzug.

| Skill | Zweck |
| --- | --- |
| `iv-plan-abstimmung-mehrheiten` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-anlagenpaket` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-cramdown-obstruktion` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-darstellender-teil` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-datenraum-register` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-gerichtliche-schritte` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-gestaltender-teil` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-gruppen-klassenbildung` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-insolvenzplan-architektur` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-integrierte-planung` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-kaltstart-interview` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-kommandocenter` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-minderheitenschutz` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-planbetroffene-auswahl` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-planvollzug-monitoring` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-redteam-qualitygate` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-sanierungskonzept` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-sicherheiten-drittsicherheiten` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-stabilisierung-starug` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-stakeholder-kommunikation` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-starug-plan-architektur` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-steuern-bilanz-folgen` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-verfahrenswahl` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |
| `iv-plan-vergleichsrechnung` | Integrierte Planwerkstatt-Funktion für Insolvenzplan und StaRUG aus IV-/Sachwalter-Sicht. |

## Typische Workflows

- Eröffnungsauftrag -> Aktenanlage -> Kassensturz -> Eröffnungsgutachten -> Sicherungsmaßnahmen.
- Eröffnung -> Masseverzeichnis -> Forderungsanmeldungen -> Prüfungstermin -> Berichtstermin.
- Zahlungsjournal -> Insolvenzreife -> § 15b-Matrix -> D&O/Organe -> Klage oder Vergleich.
- OPOS/Konto -> Anfechtungsmatrix -> Anspruchsschreiben -> Klagepfad -> Vergleichsfreigabe.
- Masseprognose -> § 208-Prüfung -> Anzeige -> Rangsteuerung -> Fortverwaltung.
- Planoption -> Sanierungskonzept -> Vergleichsrechnung -> Gruppen/Klassen -> Planentwurf -> Abstimmung -> Planvollzug.
- Verwertung abgeschlossen -> Schlussbericht -> Schlussrechnung -> Verteilungsverzeichnis.

## Enthaltene Vorlagen

- `assets/templates/iv-mandatskarte.md` - Verfahrenskarte mit Gericht, Rolle, Beschluss, Workstreams und roten Schwellen
- `assets/templates/eroeffnungsgutachten-gliederung.md` - Gliederung Eröffnungsgutachten mit Zahlen- und Belegblöcken
- `assets/templates/vorlaeufige-verwaltung-checkliste.md` - Sofortcheck vorläufige Verwaltung und Zustimmungsvorbehalt
- `assets/templates/betriebsfortfuehrung-wochenplan.md` - Betriebsfortführungsplan mit Cash-Bridge und kritischen Lieferanten
- `assets/templates/liquiditaetsstatus-kurzcheck.md` - Kurzer Liquiditäts- und Insolvenzreifecheck für Gutachten und § 15b
- `assets/templates/regelverfahren-eroeffnung.md` - Checkliste nach Eröffnung des Regelverfahrens
- `assets/templates/masseverzeichnis.md` - Masseverzeichnis mit Sicherungsrechten und Realisierungspfad
- `assets/templates/massenachverfolgung.csv` - CSV für Masseeingänge und Forderungsrealisierung
- `assets/templates/verwertung-und-massemehrung.md` - Kosten-Nutzen-Matrix für Verwertung, Prozesse und Vergleiche
- `assets/templates/anfechtungsmatrix-129ff.md` - Anfechtungsmatrix nach §§ 129 ff. InsO
- `assets/templates/anfechtungsschreiben.md` - Anfechtungsschreiben mit Anspruch, Belegen und Vergleichsanker
- `assets/templates/zahlungsklage-15b.md` - Klage- und Prüfmatrix § 15b InsO
- `assets/templates/forderungen-und-tabelle.md` - Forderungsprüfung und Tabellenvermerk
- `assets/templates/tabellenpruefung.csv` - CSV-Struktur für Tabellenprüfung
- `assets/templates/masseunzulaenglichkeit-208.md` - Anzeige der Masseunzulänglichkeit nach § 208 InsO
- `assets/templates/eigenverwaltung-sachwalterbericht.md` - Sachwalterbericht für Eigenverwaltung
- `assets/templates/schutzschirm-270d.md` - Schutzschirmcheck § 270d InsO
- `assets/templates/personal-insolvenzgeld.md` - Personal- und Insolvenzgeldmatrix
- `assets/templates/steuern-sozialversicherung.md` - Steuer- und Sozialversicherungsstatus
- `assets/templates/zwischenbericht.md` - Zwischenbericht an Gericht oder Gläubigerausschuss
- `assets/templates/glaeubigerausschuss-bericht.md` - Gläubigerausschussbericht mit Entscheidungsbedarf
- `assets/templates/schlussbericht-schlussrechnung.md` - Schlussbericht und Schlussrechnung
- `assets/templates/verteilungsverzeichnis.md` - Verteilungsverzeichnis und Quotenberechnung
- `assets/templates/zahlungslauf-freigabe.md` - Freigabeprotokoll für Zahlungsläufe
- `assets/templates/quality-gate.md` - Vor-Versand- und Vor-Entscheidungsprüfung
- `assets/templates/planwerkstatt/` - vollständige Planwerkstatt-Vorlagen für Insolvenzplan, StaRUG, Vergleichsrechnung, Gruppen/Klassen, Anlagen, Cram-down und Planvollzug

## Sicherheitsleitplanken

- Keine gerichtliche, wirtschaftliche oder steuerliche Entscheidung ohne menschliche Letztprüfung.
- Keine echten Mandatsgeheimnisse, Bankzugänge, Gerichtslogins, beA-Zertifikate, Registerzugänge oder personenbezogene Daten in nicht freigegebene Systeme.
- Alle Fristen, Forderungen, Zahlungsflüsse, Tabellenvermerke, Anfechtungsansprüche und Verteilungsrechnungen müssen belegbar sein.
- Wo amtliche Onlinequellen abgefragt werden, werden Abrufdatum, URL, Treffer und Grenzen der Recherche dokumentiert.
- Simulationen sind deutlich als Simulation zu kennzeichnen.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 28 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Insolvenzverwaltung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan... |
| `einstieg-routing` | Nutze dies, wenn Einstieg und Routing im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Ich habe ein neues Thema im Bereich Insolvenzverwaltung.; Welche Unterlagen brauchen Sie?; Welcher Spezialskill passt?. |
| `iv-aktenanlage-iv-plan` | Nutze dies, wenn Iv Aktenanlage Verfahrenscockpit, Iv Plan Verfahrenswahl im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Aktenanlage Verfahrenscockpit, Iv Plan Verfahrenswahl prüfen.; Erstelle eine Arbei... |
| `iv-anfechtung-iv-arbeitsrecht` | Nutze dies, wenn Iv Anfechtung 129Ff, Iv Arbeitsrecht Insolvenzgeld im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Anfechtung 129Ff, Iv Arbeitsrecht Insolvenzgeld prüfen.; Erstelle eine Arbeitsfassung zu... |
| `iv-berichte-iv-masseunzulaenglichkeit` | Nutze dies, wenn Iv Berichte Gericht Glaeubiger, Iv Masseunzulaenglichkeit 208 im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Berichte Gericht Glaeubiger, Iv Masseunzulaenglichkeit 208 prüfen.; Erstelle... |
| `iv-cross-iv-eigenverwaltung` | Nutze dies, wenn Iv Cross Border Assets Trustee Registervollzug, Iv Eigenverwaltung Sachwaltung im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Cross Border Assets Trustee Registervollzug, Iv Eigenverwalt... |
| `iv-eroeffnungsgutachten-iv` | Nutze dies, wenn Iv Eroeffnungsgutachten, Iv Forderungsanmeldung Prüfung im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Eroeffnungsgutachten, Iv Forderungsanmeldung Prüfung prüfen.; Erstelle eine Arbeits... |
| `iv-idw-iv` | Nutze dies, wenn Iv Idw S6 Sanierungsfaehigkeit Gate, Iv Kommandocenter im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Idw S6 Sanierungsfaehigkeit Gate, Iv Kommandocenter prüfen.; Erstelle eine Arbeitsfa... |
| `iv-masseeinsammlung-iv-massemehrung` | Nutze dies, wenn Iv Masseeinsammlung, Iv Massemehrung Asset Realisation im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Masseeinsammlung, Iv Massemehrung Asset Realisation prüfen.; Erstelle eine Arbeitsfa... |
| `iv-plan-iv-plan` | Nutze dies, wenn Iv Plan Abstimmung Mehrheiten, Iv Plan Anlagenpaket im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Plan Abstimmung Mehrheiten, Iv Plan Anlagenpaket prüfen.; Erstelle eine Arbeitsfassung... |
| `iv-plan-iv-plan-02` | Nutze dies, wenn Iv Plan Cramdown Obstruktion, Iv Plan Datenraum Register im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Plan Cramdown Obstruktion, Iv Plan Datenraum Register prüfen.; Erstelle eine Arbei... |
| `iv-plan-iv-plan-03` | Nutze dies, wenn Iv Plan Darstellender Teil, Iv Plan Gerichtliche Schritte im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Plan Darstellender Teil, Iv Plan Gerichtliche Schritte prüfen.; Erstelle eine Arb... |
| `iv-plan-iv-plan-04` | Nutze dies, wenn Iv Plan Gestaltender Teil, Iv Plan Gruppen Klassenbildung im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Plan Gestaltender Teil, Iv Plan Gruppen Klassenbildung prüfen.; Erstelle eine Arb... |
| `iv-plan-iv-plan-05` | Nutze dies, wenn Iv Plan Insolvenzplan Architektur, Iv Plan Minderheitenschutz im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Plan Insolvenzplan Architektur, Iv Plan Minderheitenschutz prüfen.; Erstelle... |
| `iv-plan-iv-plan-06` | Nutze dies, wenn Iv Plan Integrierte Planung, Iv Plan Kommandocenter im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Plan Integrierte Planung, Iv Plan Kommandocenter prüfen.; Erstelle eine Arbeitsfassung... |
| `iv-plan-iv-plan-07` | Nutze dies, wenn Iv Plan Planbetroffene Auswahl, Iv Plan Planvollzug Monitoring im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Plan Planbetroffene Auswahl, Iv Plan Planvollzug Monitoring prüfen.; Erstell... |
| `iv-plan-iv-plan-08` | Nutze dies, wenn Iv Plan Sanierungskonzept, Iv Plan Sicherheiten Drittsicherheiten im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Plan Sanierungskonzept, Iv Plan Sicherheiten Drittsicherheiten prüfen.; E... |
| `iv-plan-iv-plan-09` | Nutze dies, wenn Iv Plan Stabilisierung Starug, Iv Plan Stakeholder Kommunikation im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Plan Stabilisierung Starug, Iv Plan Stakeholder Kommunikation prüfen.; Ers... |
| `iv-plan-iv-plan-10` | Nutze dies, wenn Iv Plan Starug Plan Architektur, Iv Plan Vergleichsrechnung im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Plan Starug Plan Architektur, Iv Plan Vergleichsrechnung prüfen.; Erstelle eine... |
| `iv-plan-iv-steuern` | Nutze dies, wenn Iv Plan Steuern Bilanz Folgen, Iv Steuern Sozialversicherung im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Plan Steuern Bilanz Folgen, Iv Steuern Sozialversicherung prüfen.; Erstelle ei... |
| `iv-plan-kaltstart-interview` | Erstes Mandatsgespräch strukturieren wenn Insolvenzplan oder StaRUG-Verfahren startet und kaum Unterlagen vorliegen. §§ 13 15a 17 InsO §§ 29 42 StaRUG Antragspflichten. Prüfraster: Basisdaten Krisenursachen Gläubigerlandschaft Liquiditae... |
| `iv-plan-redteam-qualitygate` | Insolvenzplan, StaRUG-Plan oder Sanierungskonzept vor Einreichung hart auf Fehler prüfen aus Sicht opponierender Gläubiger, Gericht, Bank und Gläubigerausschuss. §§ 231 245 251 InsO Versagungsgründe. Prüfraster: Vollständigkeit, Sanierun... |
| `iv-qualitaets-iv-schutzschirm` | Nutze dies, wenn Iv Qualitaets Und Plausibilitaetsgate, Iv Schutzschirm 270D im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.; Welche Frist oder Beweislast überseh... |
| `iv-regelverfahren-insolvenzverwalter` | Nutze dies, wenn Iv Regelverfahren Eroeffnung, Spezial Insolvenzverwalter Fristen Form Und Zustaendigkeit im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Regelverfahren Eroeffnung, Spezial Insolvenzverwal... |
| `iv-sicherung-iv-tabelle` | Nutze dies, wenn Iv Sicherung Betriebsfortfuehrung, Iv Tabelle Pruefungstermin im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Sicherung Betriebsfortfuehrung, Iv Tabelle Pruefungstermin prüfen.; Erstelle... |
| `iv-verteilung-iv-vorlaeufige` | Nutze dies, wenn Iv Verteilung Schlussrechnung, Iv Vorlaeufige Verwaltung im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Verteilung Schlussrechnung, Iv Vorlaeufige Verwaltung prüfen.; Erstelle eine Arbei... |
| `iv-zahlungsklagen-insolvenzverwaltungs` | Nutze dies, wenn Iv Zahlungsklagen 15B, Spezial Insolvenzverwaltungs Erstpruefung Und Mandatsziel im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Iv Zahlungsklagen 15B, Spezial Insolvenzverwaltungs Erstpruef... |
| `sicht` | Nutze dies, wenn Spezial Sicht Tatbestand Beweis Und Belege im Plugin Insolvenzverwaltung konkret bearbeitet werden soll. Auslöser: Bitte Spezial Sicht Tatbestand Beweis Und Belege prüfen.; Erstelle eine Arbeitsfassung zu Spezial Sicht T... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
