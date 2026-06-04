# ZVG-Zwangsverwaltung - Verwalter-Cockpit

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`zwangsverwaltung-zvg`) | [`zwangsverwaltung-zvg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/zwangsverwaltung-zvg.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Zwangsverwaltung Büro- und Geschäftshaus "Friedrichshöfe"** (`zwangsverwaltung-friedrichshoefe-berlin`) | [Gesamt-PDF lesen](../testakten/zwangsverwaltung-friedrichshoefe-berlin/gesamt-pdf/zwangsverwaltung-friedrichshoefe-berlin_gesamt.pdf) | [`testakte-zwangsverwaltung-friedrichshoefe-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-zwangsverwaltung-friedrichshoefe-berlin.zip) |
| **Zwangsverwaltung ZVG – Mietshaus Parkstraße 18, Leipzig** (`zwangsverwaltung-zvg-mietshaus-parkstrasse`) | [Gesamt-PDF lesen](../testakten/zwangsverwaltung-zvg-mietshaus-parkstrasse/gesamt-pdf/zwangsverwaltung-zvg-mietshaus-parkstrasse_gesamt.pdf) | [`testakte-zwangsverwaltung-zvg-mietshaus-parkstrasse.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-zwangsverwaltung-zvg-mietshaus-parkstrasse.zip) |
| **ZVG-Versteigerung Eppendorf-Altbau** (`zwangsverwaltung-zvg-versteigerung-eppendorf-altbau`) | [Gesamt-PDF lesen](../testakten/zwangsverwaltung-zvg-versteigerung-eppendorf-altbau/gesamt-pdf/zwangsverwaltung-zvg-versteigerung-eppendorf-altbau_gesamt.pdf) | [`testakte-zwangsverwaltung-zvg-versteigerung-eppendorf-altbau.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-zwangsverwaltung-zvg-versteigerung-eppendorf-altbau.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Technischer Plugin-Name: `zwangsverwaltung-zvg`.

Großes freistehendes Plugin für Zwangsverwalter nach ZVG und ZwVwV sowie für die Schnittstelle zur Zwangsversteigerung. Abgebildet sind Bestellung, Beschlagnahme, Besitzerlangung, Objektaufnahme, Miet- und Pachtverwaltung, Mieteinzug, Betriebskosten, Versicherungen, öffentliche Lasten, Treuhandkonto, Berichtswesen, Rechnungslegung, Verteilung, Räumungs- und Besitzkonflikte, ZVG-Portal-Recherche, Bieterangebotsbewertung und Teilnahme an Versteigerungsterminen.

**Freistehend:** Dieses Plugin enthält eigene Skills, Vorlagen, Quellenhinweise, Vorschau und Testakte. Es verweist nicht auf andere Plugins als Voraussetzung.

## Installation

1. ZIP aus dem Release herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `zwangsverwaltung-zvg.zip` hochladen.
5. Mit einem konkreten Auftrag starten, zum Beispiel: `Starte das ZVG-Kommandocenter für dieses Mietshaus.`

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` enthalten.

#

## Kernmodule

| Modul | Funktion |
| Anordnung und Besitz | Bestellung, Bestallung, Beschlagnahmeumfang, Besitzerlangung und Objektaufnahme. |
| Objektbetrieb | Mieter, Pächter, Betriebskosten, Hausgeld, Instandhaltung, Gefahrensicherung und Versicherungen. |
| Finanzen | Treuhandkonto, Soll-Ist-Abgleich, Mieteinzug, Vorschuss, Belege und Kassenbuch. |
| Berichte | Besitzerlangungsbericht, Monatsbericht, gerichtliche Entscheidungsvorlage und Auskunft. |
| Rechnung und Verteilung | Jahresrechnung, Schlussrechnung, Endabrechnung, § 155 ZVG-Verteilung. |
| Konflikte | Räumung, Kündigung, Zutritt, Schuldnerhausstand, Insolvenzschnittstelle und Versteigerung. |
| Versteigerung | ZVG-Portal-Suche, Bekanntmachung, Gutachten, geringstes Gebot, Sicherheitsleistung, Bietlimit und Terminvorbereitung. |

## Skill-Landkarte

| Skill | Zweck |
| `zvg-kommandocenter` | Startet Zwangsverwaltung mit Objekt, Beteiligten, Beschluss und Sofortmaßnahmen. |
| `zvg-aktenanlage-objektcockpit` | Legt Objektakte, Rent Roll, Lastenregister, Konto und Berichtswesen an. |
| `zvg-bestellung-beschlagnahme` | Prüft Anordnung, Beschlagnahmeumfang, Ausweis, Rang und Gerichtsvorgaben. |
| `zvg-besitzuebernahme` | Organisiert Besitznahme, Protokoll, Schlüssel, Zustand, Mobilien und Sofortgefahren. |
| `zvg-miet-und-pachtverwaltung` | Verwaltet Miet- und Pachtverträge, Zahlstellen, Vorausverfügungen und Kautionen. |
| `zvg-mieteinzug-rueckstaende` | Treibt Mieten ein, matcht Zahlungen, mahnt und bereitet Klagen vor. |
| `zvg-betriebskosten-hausgeld` | Steuert Betriebskosten, Hausgeld, Dienstleister, Abrechnung und Liquidität. |
| `zvg-instandhaltung-sicherung` | Prüft Verkehrssicherung, Notmaßnahmen, Instandhaltung, Zustimmung und Budget. |
| `zvg-versicherungen-gefahren` | Sichert Gebäudeversicherung, Haftpflicht, Beitragsrückstände und Schadensfälle. |
| `zvg-oeffentliche-lasten` | Erfasst Grundsteuer, Gebühren, Lasten, Rang und Zahlungsplan. |
| `zvg-konten-kassenfuehrung` | Führt Treuhandkonto, Soll-Ist, Belege, Vorschüsse und Kassenbuch. |
| `zvg-berichtswesen-gericht` | Erstellt Besitzerlangungsbericht, Sachstandsbericht, Monatsnotiz und Gerichtsvorlage. |
| `zvg-rechnungslegung` | Erstellt Jahresrechnung, Schlussrechnung, Endabrechnung und Belegpaket. |
| `zvg-verteilungsplan-155` | Bereitet Verteilung der Nutzungen, Ausgaben, Gläubigerzahlungen und Gerichtskosten vor. |
| `zvg-glaeubiger-schuldner-kommunikation` | Formuliert klare Schreiben an Schuldner, Gläubiger, Mieter, Behörden und Gericht. |
| `zvg-raeumung-kuendigung` | Prüft Kündigung, Räumung, Schuldnerwohnräume, Mieterrechte und Eskalation. |
| `zvg-insolvenz-schnittstelle` | Koordiniert ZVG mit Insolvenzverfahren, IV, Absonderungsrechten und Massefragen. |
| `zvg-verkauf-versteigerung-schnittstelle` | Hält Schnittstelle zur Zwangsversteigerung, Werterhalt, Besichtigung und Erlöslogik. |
| `zvg-portal-recherche` | Recherchiert Zwangsversteigerungstermine im amtlichen ZVG-Portal und dokumentiert Suchparameter, Treffer und Grenzen. |
| `zvg-bieterangebot-bewertung` | Bewertet Versteigerungsobjekte und Bieterangebote mit Verkehrswert, geringstem Gebot, Lasten, Mietlage, Sanierung und Bietlimit. |
| `zvg-versteigerungsteilnahme` | Bereitet die Teilnahme am Versteigerungstermin mit Sicherheitsleistung, Legitimation, Bietstrategie und Nachbereitung vor. |
| `zvg-simulation-training` | Simuliert einen kompletten Zwangsverwaltungstag mit echten Fallakten-Artefakten. |
| `zvg-quality-gate` | Prüft Beschluss, Konto, Rent Roll, Belege, Berichte, Verteilung und Rollen. |

## Typische Workflows

- Bestellung -> Beschlusscheck -> Besitzerlangung -> Mieterinformation -> Treuhandkonto.
- Rent Roll -> Mieteinzug -> Rückstände -> Mahnung/Klage -> Gerichtssachstand.
- Objektmangel -> Gefahrensicherung -> Versicherung -> Kostenvoranschlag -> Gerichtsvorlage.
- Kontoauszug -> Buchführung -> Jahresrechnung -> Belegpaket -> Auskunft.
- Überschuss -> Rücklagencheck -> § 155 ZVG-Verteilungsplan -> Auszahlung.
- Aufhebung -> Schlussrechnung -> Endabrechnung -> Übergabe.
- ZVG-Portal -> Trefferprotokoll -> Gutachten/Grundbuch/Mietlage -> Bieterangebot -> Bietlimit -> Termincheck.

## Enthaltene Vorlagen

- `assets/templates/zvg-objektkarte.md` - Objektkarte für ZVG-Verfahren
- `assets/templates/bestellungs-und-beschlagnahmecheck.md` - Beschluss- und Beschlagnahmeprüfung
- `assets/templates/besitzuebernahme-protokoll.md` - Besitzübernahme und Objektaufnahme
- `assets/templates/mieterliste-rent-roll.md` - Rent Roll und Vertragsübersicht
- `assets/templates/mieteinzug-rueckstaende.md` - Mieteinzug und Rückstandsmatrix
- `assets/templates/betriebskosten-hausgeld.md` - Betriebskosten und Hausgeld
- `assets/templates/instandhaltung-gefahrensicherung.md` - Instandhaltung und Verkehrssicherung
- `assets/templates/versicherung-und-lasten.md` - Versicherungs- und Lastenregister
- `assets/templates/konto-kassenbuch.md` - Treuhandkonto und Kassenbuch
- `assets/templates/monatsbericht-gericht.md` - Monats- oder Sachstandsbericht ans Gericht
- `assets/templates/rechnungslegung.md` - Jahresrechnung, Schlussrechnung und Endabrechnung
- `assets/templates/verteilungsplan-155.md` - Verteilungsplan nach § 155 ZVG
- `assets/templates/schuldner-glaeubiger-kommunikation.md` - Kommunikationsbausteine
- `assets/templates/raeumung-kuendigung.md` - Räumungs- und Kündigungsprüfung
- `assets/templates/insolvenz-schnittstelle.md` - Schnittstelle ZVG und Insolvenzverfahren
- `assets/templates/zvg-portal-rechercheprotokoll.md` - ZVG-Portal-Suche und Trefferprotokoll
- `assets/templates/bieterangebot-bewertung.md` - Bewertung von Versteigerungsangeboten und Bietlimit
- `assets/templates/versteigerungsteilnahme-checkliste.md` - Terminvorbereitung für Bieter
- `assets/templates/schlussrechnung-aufhebung.md` - Aufhebung, Schlussrechnung und Endabrechnung
- `assets/templates/simulationstag.md` - Simulierter ZVG-Arbeitstag
- `assets/templates/quality-gate.md` - ZVG-Vorversandprüfung

## Sicherheitsleitplanken

- Keine gerichtliche, wirtschaftliche oder steuerliche Entscheidung ohne menschliche Letztprüfung.
- Keine echten Mandatsgeheimnisse, Bankzugänge, Gerichtslogins, beA-Zertifikate, Registerzugänge oder personenbezogene Daten in nicht freigegebene Systeme.
- Alle Fristen, Forderungen, Zahlungsflüsse, Tabellenvermerke, Anfechtungsansprüche und Verteilungsrechnungen müssen belegbar sein.
- Wo amtliche Onlinequellen abgefragt werden, werden Abrufdatum, URL, Treffer und Grenzen der Recherche dokumentiert.
- Simulationen sind deutlich als Simulation zu kennzeichnen.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | zwangsverwaltung-zvg: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausga... |
| `kompendium-02-workflow-redteam-qua-bis-zvg-oeffentliche-las` | zwangsverwaltung-zvg: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-redteam-qualitygate, spezial-beschlagnahme-fristen-form-und-zustaendigkeit, zvg-oeffentliche-lasten) und bewahrt deren Workflows, Normank... |
| `kompendium-03-spezial-berichte-sch-bis-spezial-besitz-dokum` | zwangsverwaltung-zvg: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (spezial-berichte-schriftsatz-brief-und-memo-bausteine, spezial-beschlagnahme-mietverwaltung-start, spezial-besitz-dokumentenmatrix-und-lueckenlist... |
| `kompendium-04-spezial-bieterangebo-bis-spezial-oeffentliche` | zwangsverwaltung-zvg: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (spezial-bieterangebote-compliance-dokumentation-und-akte, spezial-mieten-risikoampel-und-gegenargumente, spezial-oeffentliche-mandantenkommunikati... |
| `kompendium-05-spezial-quality-form-bis-spezial-rechnungsleg` | zwangsverwaltung-zvg: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (spezial-quality-formular-portal-und-einreichung, spezial-recherche-zahlen-schwellen-und-berechnung, spezial-rechnungslegung-internationaler-bezug-... |
| `kompendium-06-spezial-treuhandkont-bis-spezial-versteigerun` | zwangsverwaltung-zvg: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (spezial-treuhandkonto-behoerden-gericht-und-registerweg, spezial-versteigerung-tatbestand-beweis-und-belege, spezial-versteigerungsteilnahme-mehrp... |
| `kompendium-07-spezial-verteilung-v-bis-zvg-aktenanlage-obje` | zwangsverwaltung-zvg: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (spezial-verteilung-verhandlung-vergleich-und-eskalation, spezial-zwangsverwaltung-erstpruefung-und-mandatsziel, zvg-aktenanlage-objektcockpit) und... |
| `kompendium-08-zvg-berichtswesen-ge-bis-zvg-bestellung-besch` | zwangsverwaltung-zvg: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (zvg-berichtswesen-gericht, zvg-besitzuebernahme, zvg-bestellung-beschlagnahme) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemu... |
| `kompendium-09-zvg-betriebskosten-h-bis-zvg-glaeubiger-schul` | zwangsverwaltung-zvg: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (zvg-betriebskosten-hausgeld, zvg-bieterangebot-bewertung, zvg-glaeubiger-schuldner-kommunikation) und bewahrt deren Workflows, Normanker, Prüfprog... |
| `kompendium-10-zvg-insolvenz-schnit-bis-zvg-kommandocenter` | zwangsverwaltung-zvg: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (zvg-insolvenz-schnittstelle, zvg-instandhaltung-sicherung, zvg-kommandocenter) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemu... |
| `kompendium-11-zvg-konten-kassenfue-bis-zvg-mieteinzug-rueck` | zwangsverwaltung-zvg: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (zvg-konten-kassenfuehrung, zvg-miet-und-pachtverwaltung, zvg-mieteinzug-rueckstaende) und bewahrt deren Workflows, Normanker, Prüfprogramme und Au... |
| `kompendium-12-zvg-portal-recherche-bis-zvg-raeumung-kuendig` | zwangsverwaltung-zvg: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (zvg-portal-recherche, zvg-quality-gate, zvg-raeumung-kuendigung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-13-zvg-rechnungslegung-bis-zvg-verkauf-versteig` | zwangsverwaltung-zvg: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (zvg-rechnungslegung, zvg-simulation-training, zvg-verkauf-versteigerung-schnittstelle) und bewahrt deren Workflows, Normanker, Prüfprogramme und A... |
| `kompendium-14-zvg-versicherungen-g-bis-zvg-verteilungsplan` | zwangsverwaltung-zvg: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (zvg-versicherungen-gefahren, zvg-versteigerungsteilnahme, zvg-verteilungsplan-155) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausga... |
| `kompendium-15-zwvw-anordnung-zwang-bis-zwvw-mietverhaeltnis` | zwangsverwaltung-zvg: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (zwvw-anordnung-zwangsverwaltung-bauleiter, zwvw-kostenrechnung-verwalter-spezial, zwvw-mietverhaeltnis-bestand-leitfaden) und bewahrt deren Workfl... |
| `kompendium-16-zwvw-versteigerung-v-bis-zwvw-versteigerung-v` | zwangsverwaltung-zvg: Konsolidiertes Skill-Kompendium 16; bündelt 1 frühere Spezialskills (zwvw-versteigerung-vs-verwaltung-spezial) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-gate-red-team-und-qualitaetskontrolle` | Gate: Red-Team und Qualitätskontrolle im Plugin zwangsverwaltung zvg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-portal-livequellen-und-rechtsprechungscheck` | Portal: Livequellen- und Rechtsprechungscheck im Plugin zwangsverwaltung zvg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin zwangsverwaltung-zvg: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin zwangsverwaltung-zvg: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin zwangsverwaltung-zvg: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin zwangsverwaltung-zvg: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin zwangsverwaltung-zvg: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin zwangsverwaltung-zvg: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
