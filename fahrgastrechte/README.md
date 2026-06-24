# Fahrgastrechte
Wenn du das hier oeffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen pruefen und ein verwertbares Arbeitsprodukt erhalten.

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Dies ist eines von 232 Plugins dieser Sammlung. Jedes Plugin enthält eine Familie zusammenhängender Skills (`SKILL.md`-Dateien), passende Hilfsdateien, Prüfraster, Vorlagen und in vielen Fällen eine eigene Arbeitsakte. Der vorgesehene Hauptweg ist die Installation über den Marketplace, alternativ als einzelnes Plugin-ZIP. Dann läuft das Plugin mit seinen Skills, Werkzeugen und Testdaten in der dafür vorgesehenen Plugin-Umgebung.

Damit das Plugin auch ohne Plugin-Setup brauchbar bleibt, gibt es zusätzlich zwei reine Markdown-Prompts: einen ausführlichen Werkstatt-Prompt und einen kompakten Schnellstart-Prompt. Beide sind einzelne `.md`-Dateien, die man in eine geeignete Arbeitsumgebung ziehen, einfügen oder per Copy-and-Paste verwenden kann.

## Downloads

In dieser Reihenfolge gedacht: zuerst der vorgesehene Plugin-Weg, danach die Markdown-Alternativen, am Schluss die zugehörigen Testakten.

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`fahrgastrechte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fahrgastrechte.zip) |
| Großer Prompt (Werkstatt, Alternative ohne Plugin-Setup) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/fahrgastrechte/fahrgastrechte-werkstatt.md" download><code>fahrgastrechte-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart, höchstens 7500 Zeichen, Spar-Alternative) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/fahrgastrechte/fahrgastrechte-schnellstart.md" download><code>fahrgastrechte-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) |

> Marketplace-Hinweis: Wer mehrere Plugins gleichzeitig will, fügt nicht jedes Plugin einzeln hinzu, sondern den ganzen Marketplace über `marketplace.json` aus dem [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest). Dann sind alle 232 Plugins verfügbar und können einzeln aktiviert werden.
<!-- END direkt-loslegen (autogen) -->

Fahrgastrechte im Eisenbahnverkehr selber geltend machen — VO (EU) 2021/782 plus EVO 2023 plus DB-Beförderungsbedingungen. Tickets erfassen Verspätung oder Zugausfall einordnen Entschädigung berechnen (25/50 Prozent ab 60/120 Minuten) Forderung an die DB Widerspruch gegen die Ablehnung Schlichtungsstelle Reise & Verkehr e.V. (vormals söp) und Klage zum Amtsgericht. Vollmacht für Mitreisende. Katalog typischer DB-Ablehnungsgründe mit Gegenargumenten.

## Installation in der Plugin-Umgebung

1. ZIP herunterladen (Link oben).
2. Plugin-Menü öffnen, `Install from .zip` wählen und die Datei auswählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Worum geht es?

Wer mit der Bahn unterwegs ist und eine Verspätung von mehr als einer Stunde oder einen Zugausfall erleidet, hat einen Entschädigungsanspruch nach Art. 19 VO (EU) 2021/782: 25 Prozent des Fahrpreises ab 60 Minuten Verspätung am Zielort, 50 Prozent ab 120 Minuten. Dieses Plugin deckt den vollständigen Mandatsablauf ab: vom Erfassen der Ticket- und Reisedaten über die Berechnung des Anspruchs, das Forderungsschreiben, den Widerspruch gegen eine Ablehnung, die Schlichtung bis zur Klage vor dem Amtsgericht.

Das Plugin richtet sich an Verbraucher, die ihre Ansprüche selbst durchsetzen wollen, sowie an Anwälte, die Fahrgäste vertreten.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. EuGH-, BGH- und AG-Entscheidungen werden vor jedem Versand über curia.europa.eu, bundesgerichtshof.de oder gesetze-im-internet.de verifiziert.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 14 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anlagen-bauen` | Baut aus den Belegen eines Fahrgastrechte-Mandats ein beA-konformes Anlagenkonvolut. Verwendet zum bestehenden Schriftsatz (Forderungsschreiben Widerspruch Schlichtungsantrag Klage) die Belege Buchungsbestaetigung E-Ticket Verspaetungsbe... |
| `db-ablehnungsgruende-pruefen` | Katalog typischer Ablehnungsgruende des DB-Servicecenters Fahrgastrechte mit Gegenargumenten und Pinpoint auf Art. 18 und 19 und 20 VO (EU) 2021/782 sowie EVO und DB-Befoerderungsbedingungen. Behandelt andere Verbindung als gebucht; Vers... |
| `eigenbefoerderung-und-betreuung-art-18` | Prüfraster für Selbstbefoerderung des Fahrgasts (Art. 18 Abs. 3 Unterabs. 2 VO 2021/782 mit 100-Minuten-Frist) und Hilfeleistungs-Anspruch (Art. 20 VO Verpflegung Hotel Transport) sowie SPNV-Sonderfall § 11 EVO (20-Min-Schwelle Alternati... |
| `einfuehrung-vo-2021-782` | Einfuehrung VO (EU) 2021/782 Fahrgastrechte Eisenbahn. Anwendungsbereich Art. 2 (auch SPNV mit Ausnahmen § 2 EVO), Begriffsbestimmungen Art. 3 (Verspaetung Ankunft Anschluss Zeitfahrkarte), Verzichtsverbot Art. 7, Durchgangsfahrkarten Ar... |
| `entschaedigung-berechnen` | Berechnet die Entschaedigung nach Art. 19 VO (EU) 2021/782. Zwei Stufen 25 Prozent (ab 60 Minuten Endziel-Verspaetung) und 50 Prozent (ab 120 Minuten). DB-Tarif-Pauschalen für BahnCard 100 (10 oder 20 EUR), Deutschlandticket (1.50 EUR mi... |
| `fahrgastrechte-schnellstart` | 'Kompakter Arbeitsmodus für Fahrgastrechte. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.' |
| `forderung-an-db-erste-stufe` | Erstes Forderungsschreiben an das DB-Servicecenter Fahrgastrechte. Erfasst Anspruchsteller (alle Reisenden mit Vollmachten) Anspruchsgrundlage Art. 19 VO 2021/782 plus Art. 18 und Art. 20 sowie ggf. § 11 EVO konkrete Berechnung Frist zur... |
| `kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im Fahrgastrechte-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlaegt passende Fachmodule aus diesem Plugin vor und fuehrt in einen klaren Arbeitsplan. Bei Dokume... |
| `klage-amtsgericht-fahrgast` | Klageentwurf zum Amtsgericht in Fahrgastrechte-Angelegenheiten. Sachliche Zuständigkeit § 23 Nr. 1 GVG bei Streitwert bis zehntausend Euro (i.d.F. seit 01.01.2026). Oertlich wahlweise Abfahrts- oder Zielbahnhof (Art. 7 Nr. 1 lit. b VO 12... |
| `schlichtung-reise-verkehr-anrufen` | Schlichtungsantrag bei der Schlichtungsstelle Reise & Verkehr e.V. (vormals söp) nach erfolgloser Reklamation beim Eisenbahnverkehrsunternehmen. Kostenfrei für Verbraucher nach VSBG. Voraussetzung Vorgerichtliche Geltendmachung beim EVU... |
| `ticket-und-reisedaten-erfassen` | Erfasst die Falldaten aus hochgeladenen Tickets Buchungsbestaetigungen Reservierungen Foto-Belegen für Fahrgastrechte-Mandate. Extrahiert Buchungscode (PNR) Auftragsnummer Reisetag Strecke Operating EVU Ticketart (Flexpreis Sparpreis Sup... |
| `verspaetung-und-anschlussverlust-einordnen` | Ordnet das Stoerungsereignis rechtlich ein: Verspaetung (Art. 19 VO 2021/782 bei mindestens 60 Min Endziel), Zugausfall (Art. 18), verpasster Anschluss unter Durchgangsfahrkarte (Art. 12 Abs. 3) oder Vorverlegung. Differenzierung Fernver... |
| `vollmacht-mitreisende` | Erzeugt Vollmachten für Mitreisende (Familienmitglieder Freunde Reisegruppe) damit ein Hauptansprechpartner deren Fahrgastrechte-Anspruch im Schriftverkehr Schlichtungs- und Gerichtsverfahren mitvertreten kann. Pro Person eigene Vollmach... |
| `widerspruch` | Erstellt einen formellen Widerspruchsbrief gegen die Ablehnung eines Fahrgastrechte-Antrags der Deutschen Bahn oder eines anderen Eisenbahnverkehrsunternehmens. Verwende diesen Skill immer wenn der Nutzer ein Ablehnungsschreiben des DB-S... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
