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
| `berichte-beschlagnahme-mietverwaltung-besitz` | Berichte Beschlagnahme Mietverwaltung Besitz im Zwangsverwaltung (ZVG): prüft konkret Berichte, Beschlagnahme, Besitzergreifung und Mietverwaltung zum Verfahrensstart, Besitz. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel... |
| `beschlagnahme-oeffentliche-lasten` | Beschlagnahme Oeffentliche Lasten im Zwangsverwaltung (ZVG): prüft konkret Red-Team Qualitygate im Plugin zwangsverwaltung-zvg, Beschlagnahme, Öffentliche Lasten und grundstuecksbezogene Abgaben in der. Liefert priorisierten Output mit N... |
| `betriebskosten-hausgeld-bieterangebot` | Betriebskosten Hausgeld Bieterangebot im Zwangsverwaltung (ZVG): prüft konkret Betriebskosten Hausgeld und laufende Objektkosten in der, Bewertet Zwangsversteigerungsobjekte aus Investorensicht, Schriftwechsel in der Zwangsverwaltung mit... |
| `bieterangebote-mieten-oeffentliche` | Bieterangebote Mieten Oeffentliche im Zwangsverwaltung (ZVG): prüft konkret Bieterangebote, Mieten, Oeffentliche. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `insolvenz-schnittstelle-instandhaltung` | Insolvenz Schnittstelle Instandhaltung im Zwangsverwaltung (ZVG): prüft konkret Schnittstelle Zwangsverwaltung und Insolvenz bei Insolvenz, Instandhaltung Sicherung und Gefahrenabwehr am, Kommandocenter für Zwangsverwaltung — Triage und... |
| `konten-kassenfuehrung-miet-pachtverwaltung` | Konten Kassenfuehrung Miet Pachtverwaltung im Zwangsverwaltung (ZVG): prüft konkret Kontenführung und Buchführung des Treuhandkontos in der, Miet- und Pachtverwaltung in der Zwangsverwaltung, Mieteinzug und Rückstandsbehandlung in der Zw... |
| `portal-quellenkarte` | Portal Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `quality-recherche-rechnungslegung` | Quality Recherche Rechnungslegung im Zwangsverwaltung (ZVG): prüft konkret Quality, Recherche, Rechnungslegung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `treuhandkonto-versteigerung` | Treuhandkonto Versteigerung im Zwangsverwaltung (ZVG): prüft konkret Treuhandkonto, Versteigerung, Versteigerungsteilnahme. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `versicherungen-gefahren-zvg` | Versicherungen Gefahren ZVG im Zwangsverwaltung (ZVG): prüft konkret Versicherungsschutz und Gefahrenabwehr am, Vorbereitung der Teilnahme am Zwangsversteigerungstermin, Verteilungsplan nach § 155 ZVG für die Auszahlung von. Liefert prio... |
| `verteilung-zwangsverwaltung-aktenanlage` | Verteilung Zwangsverwaltung Aktenanlage im Zwangsverwaltung (ZVG): prüft konkret Verteilung, Zwangsverwaltung, Aktenanlage und Objektcockpit für den Zwangsverwalter nach. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und n... |
| `zvg-berichtswesen-besitzuebernahme-bestellung` | Berichtswesen Besitzuebernahme Bestellung im Zwangsverwaltung (ZVG): prüft konkret Berichterstattung an das Vollstreckungsgericht in der, Besitzerlangung über das Zwangsverwaltungsobjekt nach § 150, Prüft Bestellungsbeschluss und Beschla... |
| `zvg-recherche-quality-gate-raeumung` | Recherche Quality Gate Raeumung im Zwangsverwaltung (ZVG): prüft konkret Recherche von Zwangsversteigerungsterminen im amtlichen, Quality Gate für Zwangsverwaltung vor Versand oder, Räumung Kündigung und Besitzkonflikte in der. Liefert p... |
| `zvg-rechnungslegung-simulation-training` | Rechnungslegung Simulation Training im Zwangsverwaltung (ZVG): prüft konkret Jahresrechnung und Schlussrechnung des Zwangsverwalters, Simulation und Training für Zwangsverwaltung mit einem, Schnittstelle zwischen laufender Zwangsverwaltu... |
| `zwangsverwaltung-zvg-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `zwangsverwaltung-zvg-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `zwangsverwaltung-zvg-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `zwangsverwaltung-zvg-gate-fehlerkatalog` | Gate Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `zwangsverwaltung-zvg-output-waehlen` | Output wählen im Zwangsverwaltung (ZVG): Diese Output-Weiche für Zwangsverwaltung Zvg entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `zwangsverwaltung-zvg-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `zwangsverwaltung-zvg-start-chronologie-fristen` | Start Chronologie Fristen im Zwangsverwaltung (ZVG): prüft konkret Einstieg, Schnelltriage und Fallrouting im Zwangsverwaltung ZVG-Plugin, Chronologie und Belegmatrix im Plugin zwangsverwaltung-zvg, Fristen- und Risikoampel im Plugin zwa... |
| `zwangsverwaltung-zvg-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `zwvw-anordnung-zwangsverwaltung` | Zwvw Anordnung Zwangsverwaltung im Zwangsverwaltung (ZVG): prüft konkret Bauleiter Anordnung Zwangsverwaltung ZVG, Spezialfall Kostenrechnung des Zwangsverwalters ZwVwV, Leitfaden Bestand der Mietverhaeltnisse in Zwangsverwaltung. Liefer... |
| `zwvw-versteigerung` | Zwvw Versteigerung im Zwangsverwaltung (ZVG): fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
