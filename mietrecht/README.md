# Mietrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`mietrecht`) | [`mietrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/mietrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Mietstreit Tannenkamp / Strassburger Immobilien GmbH — Altbau Leipzig-Plagwitz, Modernisierung und Mietminderung** (`mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp`) | [Gesamt-PDF lesen](../testakten/mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp/gesamt-pdf/mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp_gesamt.pdf) | [`testakte-mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Mietrecht für Mieter und Vermieter sowie Wohnungseigentumsrecht mit ausschließlich amtlichen Mietspiegel-Quellen pro Bundesland und für Top- und Universitätsstädte. Workflows für Datenerhebung, Mieterhöhungs-Widerspruch, Mietsenkungsverlangen, Nebenkostenprüfung, Mieteranfragen, Kündigung, Kaution, WEG-Beschlussklage und Klageentwurf Amtsgericht.

## Rechtsstand und Quellen-Gate

Für aktuelle Mietrechts- und WEG-Fragen zuerst `/mietrecht:rechtsstand-mai-2026-faktenbank` laden. Der Skill enthält geprüfte freie Anker zu Mietpreisbremse, Modernisierung, Steckersolargeräten, virtueller Eigentümerversammlung, Verwalterabberufung, WEG-baulichen Veränderungen und Störerhaftung.

Keine BeckRS-, juris-, Kommentar- oder Aufsatzzitate aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier Quelle; Mietspiegel nur aus amtlicher kommunaler Quelle oder der mitgelieferten Mietspiegel-Referenz.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `allgemein` | Einstieg, Triage und Workflow-Routing im Plugin. Fragt Rolle (Vermieter/Mieter/WEG/Verwalter), Ziel, Fristen, Unterlagen und Risiken ab und schlägt passende Spezial-Skills vor. Bei stummem Upload reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, schlägt den passenden Spezial-Skill vor oder stellt genau eine gezielte Rückfrage. |
| `eigenbedarfskuendigung-erstellen` | Vermietersicht — entwerfe eine ordentliche Kündigung wegen Eigenbedarfs nach § 573 Abs. 2 Nr. 2 BGB. Prüfroutine deckt berechtigtes Interesse (Eigennutzung Familienangehörige Haushaltsangehörige) konkrete Begründ… |
| `klageentwurf-amtsgericht` | Beide Rollen — entwirf eine Klageschrift zum Amtsgericht in einer Mietsache. Sachliche Zuständigkeit für Wohnraummietsachen nach § 23 Nr. 2a GVG ohne Rücksicht auf den Streitwert; bei Geschäftsraummiete allgemeine… |
| `lage-und-ausstattung-erheben` | Strukturierte Datenerhebung für die Einordnung in den Mietspiegel — Adresse Baujahr Wohnfläche Bad Küche Heizung Wohnungsausstattung Gebäudeausstattung. Erfasst alle Merkmale die in qualifizierten Mietspiegeln als… |
| `mahnung-zahlungsverzug-mieter` | Vermietersicht — verfasse Mahnung und ggf. fristlose Kündigung bei Zahlungsverzug des Mieters. Prüfroutine deckt Verzug nach § 286 BGB Fälligkeit der Miete (§ 556b Abs. 1 BGB) Mahnschreiben Aufrechnungsverbot frist… |
| `mandat-triage-mietrecht` | Strukturierte Eingangs-Abfrage für mietrechtliche Mandate. Klärt Mandantenrolle (Vermieter/Mieter/WEG-Eigentümer/Verwalter), Gegenstand (Wohnraum/Gewerbe/WEG) und Sachgebiet (Kündigung, Mieterhöhung, Mietminderung, Modernisierung, Nebenkosten, Mietkaution, Eigenbedarf, Räumung, WEG-Beschluss, WEG-Hausgeld). Fristen-Sofort-Check (§ 573c BGB, § 721 ZPO, § 45 WEG, § 558b BGB). Eskalations-Pfad bei laufenden Fristen. |
| `mieteranfragen-beantworten` | Vermieter- und Hausverwaltungssicht — beantworte Mieteranfragen sachlich und ehrlich. Deckt typische Themen ab (Mietminderung Mangelanzeige Modernisierungsankündigung Schönheitsreparaturen Hausordnung Kaution Eigenb… |
| `mieterhoehung-pruefen-widersprechen` | Mietersicht — prüfe ein Mieterhöhungsverlangen nach ortsüblicher Vergleichsmiete (§§ 558 ff. BGB) auf Form Frist Kappungsgrenze Begründung und entwirf bei Bedarf eine Zustimmungsverweigerung oder Teilzustimmung. P… |
| `mieterhoehungsverlangen-erstellen` | Vermietersicht — verfasse ein Mieterhöhungsverlangen auf ortsübliche Vergleichsmiete (§ 558a BGB) in Textform mit ordnungsgemäßer Begründung (Mietspiegel Sachverständigengutachten oder drei Vergleichswohnungen).… |
| `mietkaution-rueckforderung` | Mietersicht — Workflow zur Rückforderung der Mietkaution nach Beendigung des Mietverhältnisses. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Prüfung mit Gericht, Datum und Aktenzeichen. |
| `mietpreisueberhoehung-wistrg-1954-mietwucher` | Dreistufige Prüfung überhöhter Wohnraummiete: Mietpreisbremse, § 5 WiStrG 1954 als Ordnungswidrigkeit und § 291 StGB als Straftat; mit Mietspiegel-, Beweis-, Rückforderungs- und Behördenpfad. |
| `mietsenkungsverlangen` | Mietersicht — prüfe eine laufende oder bei Vertragsschluss vereinbarte Miete auf Mietpreisbremse (§§ 556d ff. BGB), § 5 WiStrG 1954 (Mietpreisüberhöhung) und § 291 StGB (Mietwucher). Erzeugt ein… |
| `mietspiegel-quellen` | Verweist auf die mitgelieferte Referenz references/mietspiegel-quellen.md mit ausschließlich amtlichen Mietspiegel-Quellen (Bundesländer Top-Städte Universitätsstädte). Nutze diese Referenz immer wenn die ortsüb… |
| `nebenkostenabrechnung-erstellen` | Vermieter- und Hausverwaltungssicht — Workflow für rechtssichere Betriebskostenabrechnungen nach § 556 BGB und BetrKV. Deckt Abrechnungszeitraum Zugangsfrist (zwölf Monate) Umlagefähigkeit Verteilerschlüssel Heizk… |
| `nebenkostenabrechnung-pruefen` | Mietersicht — prüfe eine Betriebskostenabrechnung auf Form (§ 556 Abs. 3 BGB) Frist (Zugang innerhalb von zwölf Monaten nach Abrechnungszeitraum) Umlagefähigkeit nach BetrKV Verteilerschlüssel rechnerische Richtig… |
| `rechtsstand-mai-2026-faktenbank` | Quellen-Gate: Mietpreisbremse, Modernisierung, Steckersolargeräte, virtuelle Eigentümerversammlung, Verwalterabberufung, WEG-bauliche Veränderung und freie BGH-/Normquellen |
| `weg-beschluss-anfechten` | WEG-Sicht — Prüfraster für die Beschlussanfechtung in der Wohnungseigentümergemeinschaft nach §§ 44 ff. WEG (Reform 2020). Beschluss-, Anfechtungs-, Nichtigkeits- und Feststellungsklage. Prüft formelle Mängel (Ladung, Tagesordnung, Beschlussfähigkeit, Mehrheit, Stimmrechtsausschluss) und materielle Mängel (ordnungsmäßige Verwaltung, Treu und Glauben). Klagefrist ein Monat ab Beschluss (§ 45 WEG). |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `amtlichen-amtsgericht-sonderfall` | Amtlichen Amtsgericht Sonderfall: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `bundesland-datenerhebung-grossstadt` | Bundesland Datenerhebung Grossstadt: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `erstellung-fehlerkatalog` | Erstellung Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `klageentwurf-amtsgericht-miet-gewerbemiete` | Klageentwurf Amtsgericht Miet Gewerbemiete: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `lage-ausstattung-mahnung-zahlungsverzug` | Lage Ausstattung Mahnung Zahlungsverzug: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `miet-kuendigungsschutz-mietminderung` | Miet Kuendigungsschutz Mietminderung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `mieter-mieteranfragen-mandantenentscheidung` | Mieter Mieteranfragen Mandantenentscheidung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `mieterhoehung-widersprechen` | Mieterhoehung Widersprechen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `mietpreisueberhoehung-wistrg` | Mietpreisueberhoehung Wistrg: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `mietrecht-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `mietrecht-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `mietrecht-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `mietrecht-mandantenkommunikation-redteam-qualitygate-vermieter` | Mandantenkommunikation Redteam Qualitygate Vermieter: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `mietrecht-mietsenkungsverlangen-international` | Mietsenkungsverlangen International: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `mietrecht-output-waehlen` | Output wählen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `mietrecht-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `mietrecht-start-chronologie-fristen` | Start Chronologie Fristen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `mietrecht-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `mr-betriebskostenabrechnung-mr` | MR Betriebskostenabrechnung MR: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `mr-einfuehrung-klageentwurf-beweislast` | MR Einfuehrung Klageentwurf Beweislast: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `nebenkostenabrechnung-erstellen-faktenbank` | Nebenkostenabrechnung Erstellen Faktenbank: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `nebenkostenpruefung-prozessstrategie` | Nebenkostenpruefung Prozessstrategie: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `universitaetsstaedte-quellenkarte-check` | Universitaetsstaedte Quellenkarte Check: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `widerspruch-interessen` | Widerspruch Interessen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
