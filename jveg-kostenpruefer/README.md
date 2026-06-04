# JVEG-Kostenprüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`jveg-kostenpruefer`) | [`jveg-kostenpruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/jveg-kostenpruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte JVEG Zeugenentschädigung – Dr. Sophia Berger / LG Tübingen** (`jveg-zeugin-berger-lg-tuebingen`) | [Gesamt-PDF lesen](../testakten/jveg-zeugin-berger-lg-tuebingen/gesamt-pdf/jveg-zeugin-berger-lg-tuebingen_gesamt.pdf) | [`testakte-jveg-zeugin-berger-lg-tuebingen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-jveg-zeugin-berger-lg-tuebingen.zip) |
| **Akte LG Regensburg — Sieglinger gegen Burgwald Energietechnik GmbH** (`sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger`) | [Gesamt-PDF lesen](../testakten/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger/gesamt-pdf/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger_gesamt.pdf) | [`testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Cowork-Plugin zur Prüfung von Kosten, Vorschüssen, Entschädigungen und Vergütungen nach dem Justizvergütungs- und -entschädigungsgesetz. Es ist auf echte Aktenarbeit zugeschnitten: Unterlagen strippen, Anspruchsart erkennen, JVEG-Positionen rechnen, Belege prüfen, Gerichtsschreiben angreifen oder bestätigen und am Ende ein belastbares Schreiben samt Rechenprotokoll erzeugen.

Die Beispielakte enthält den Fall der Zeugin Sophia Berger vor dem Landgericht Tübingen, Az. 7 O 118/23, mit Vorschussantrag, Gerichtsschreiben, anwaltlichem Schriftsatz und Word-Abschrift.

## Was das Plugin prüft

- Vorschuss nach § 3 JVEG
- Geltendmachung, Erlöschen, Wiedereinsetzung und Verjährung
- Fahrtkosten nach § 5 JVEG
- Tagegeld und Übernachtung nach § 6 JVEG
- sonstige notwendige Aufwendungen nach § 7 JVEG
- Zeugenentschädigung nach §§ 19 bis 22 JVEG
- Sachverständigen-, Dolmetscher- und Übersetzervergütung
- Kürzungs- und Wegfallrisiken nach § 8a JVEG
- Festsetzungs-, Beschwerde- und Ergänzungsschreiben

## Grundworkflow

1. Akte hochladen: Ladung, Antrag, Gerichtsschreiben, Belege, Rechnung oder Schriftsatz.
2. Rolle bestimmen: Zeuge, Sachverständiger, Dolmetscher, Übersetzer, Dritter oder ehrenamtlicher Richter.
3. Frist und Belehrung prüfen.
4. Jede Kostenposition mit Norm, Beleg und Rechenweg erfassen.
5. Kappungen und Doppelposten prüfen.
6. Beleglücken freundlich als Rückfragen ausgeben.
7. Rechenblatt, Prüfbericht und passendes Gerichtsschreiben erzeugen.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| jveg-kommandocenter | Startet die JVEG-Kostenprüfung, trennt Rolle, Anspruchsart, Frist, Belege, Rechenweg und gewünschten Output. |
| jveg-aktenstripper | Liest Gerichtsschreiben, Anträge, Rechnungen, Belege und Kostenfestsetzungsunterlagen in eine prüfbare JVEG-Datenmatrix aus. |
| jveg-anspruchsberechtigung | Kläert, ob Zeuge, Dritter, Sachverständiger, Dolmetscher, Übersetzer, Protokollperson oder ehrenamtlicher Richter betroffen ist. |
| jveg-fristen-erloeschen | Prüft Geltendmachung, Drei-Monats-Frist, Belehrung, Wiedereinsetzung, Verjährung und sichere Fristennotizen. |
| jveg-vorschuss | Prüft Vorschussanträge nach § 3 JVEG mit Schwerpunkt erhebliche Fahrtkosten, Übernachtung und Teilleistungen. |
| jveg-zeugenentschaedigung | Rechnet und plausibilisiert Zeugenentschädigung nach §§ 19 bis 22 JVEG. |
| jveg-fahrtkosten | Prüft Bahn, Flug, eigenes Kfz, Kilometerpauschale, Parkkosten, Auslandsanreise und Wirtschaftlichkeit. |
| jveg-uebernachtung-aufwand | Prüft Tagegeld, notwendige Übernachtung, BRKG-Anknüpfung, Belege und gerichtliche Obergrenzen. |
| jveg-verdienstausfall-haushalt-zeit | Trennt Verdienstausfall, Haushaltsführungsnachteile und Zeitversäumnis, damit keine Doppelberechnung entsteht. |
| jveg-sonstige-aufwendungen-belege | Prüft sonstige notwendige bare Auslagen, Begleitpersonen, Vertretung, Kopien, Dateien und Belegfähigkeit. |
| jveg-sachverstaendigenrechnung | Prüft Sachverständigenvergütung: Honorargruppe, erforderliche Zeit, Reisezeit, Nebenkosten, § 8a-Risiken und Vorschussüberlauf. |
| jveg-dolmetscher-uebersetzer | Prüft Dolmetscher- und Übersetzervergütung, Stundensatz, Zeilen-/Textumfang, Reisezeiten und Sprach-/Terminlogik. |
| jveg-kuerzung-wegfall-8a | Findet Kürzungs- und Wegfallrisiken: Verwertbarkeit, Hinweisobliegenheit, Befangenheit, Vorschussüberschreitung und Mängel. |
| jveg-gerichtsschreiben-pruefung | Prüft Gerichtsschreiben und Kostenbeamtenargumente auf Tatbestandsfehler, Ermessensfehler, Beleganforderungen und Antwortbedarf. |
| jveg-rechenblatt | Erstellt ein prüfbares Rechenblatt mit Norm, Eingabewert, Kappung, Beleg, Rechenschritt und Ergebnis. |
| jveg-antragsgenerator | Erzeugt Vorschuss-, Nachzahlungs-, Festsetzungs- und Ergänzungsschreiben mit Anlagen- und Belegliste. |
| jveg-festsetzung-beschwerde | Führt durch gerichtliche Festsetzung, Erinnerung/Beschwerdeprüfung, Beschwer, Frist und knappe Angriffsmittel. |
| jveg-quality-gate | Letzte Prüfung vor Versand: Normstand, Mathematik, Belege, keine Doppelposten, Fristen, Ton und eindeutiger Antrag. |

## Beispiel Berger

Die Beispielakte bildet einen realistisch aussehenden Vorschussstreit ab: Barcelona nach Tübingen, 2.500 km Hin- und Rückfahrt, zwei Übernachtungen, geltend gemachter Verdienstausfall und gerichtliche Ablehnung des Vorschusses wegen angeblich fehlender Bedürftigkeit. Das Plugin markiert insbesondere, dass § 3 JVEG bei erheblichen Fahrtkosten und sonstigen Aufwendungen ansetzt und die Kostenpositionen getrennt nach Erstattungsfähigkeit, Vorschussfähigkeit und Belegstatus geprüft werden müssen.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | jveg-kostenpruefer: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabe... |
| `kompendium-02-workflow-mandantenko-bis-jveg-fristen-erloesc` | jveg-kostenpruefer: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-mandantenkommunikation, workflow-redteam-qualitygate, jveg-fristen-erloeschen) und bewahrt deren Workflows, Normanker, Prüfprogramme und Au... |
| `kompendium-03-spezial-fristen-comp-bis-spezial-kostenpruefe` | jveg-kostenpruefer: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (spezial-fristen-compliance-dokumentation-und-akte, spezial-kostenfestsetzung-belege-und-fristen, spezial-kostenpruefer-fristen-form-und-zustaendigke... |
| `kompendium-04-spezial-uebersetzer-bis-jveg-aktenstripper` | jveg-kostenpruefer: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (spezial-uebersetzer-fristennotiz-und-naechster-schritt, jveg-sachverstaendigenrechnung-bauleiter, jveg-aktenstripper) und bewahrt deren Workflows, N... |
| `kompendium-05-jveg-anspruchsberech-bis-jveg-dolmetscher-ueb` | jveg-kostenpruefer: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (jveg-anspruchsberechtigung, jveg-antragsgenerator, jveg-dolmetscher-uebersetzer) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemu... |
| `kompendium-06-jveg-dolmetscher-ueb-bis-jveg-festsetzung-bes` | jveg-kostenpruefer: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (jveg-dolmetscher-uebersetzer-spezial, jveg-fahrtkosten, jveg-festsetzung-beschwerde) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausga... |
| `kompendium-07-jveg-gerichtsschreib-bis-jveg-kuerzung-wegfal` | jveg-kostenpruefer: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (jveg-gerichtsschreiben-pruefung, jveg-kommandocenter, jveg-kuerzung-wegfall-8a) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemus... |
| `kompendium-08-jveg-quality-gate-bis-jveg-sachverstaendig` | jveg-kostenpruefer: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (jveg-quality-gate, jveg-rechenblatt, jveg-sachverstaendigenrechnung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-09-jveg-sonstige-aufwen-bis-jveg-verdienstausfal` | jveg-kostenpruefer: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (jveg-sonstige-aufwendungen-belege, jveg-uebernachtung-aufwand, jveg-verdienstausfall-haushalt-zeit) und bewahrt deren Workflows, Normanker, Prüfprog... |
| `kompendium-10-jveg-vorschuss-bis-jveg-zeugenentschaed` | jveg-kostenpruefer: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (jveg-vorschuss, jveg-vorschuss-kostenrisiko-spezial, jveg-zeugenentschaedigung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemus... |
| `kompendium-11-jveg-zeugenentschaed-bis-spezial-belegfeste-f` | jveg-kostenpruefer: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (jveg-zeugenentschaedigung-checkliste, pruefung-sachverstaendigengutachten-ki-deklaration, spezial-belegfeste-formular-portal-und-einreichung) und be... |
| `kompendium-12-spezial-beschwerde-i-bis-spezial-dolmetscherk` | jveg-kostenpruefer: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (spezial-beschwerde-internationaler-bezug-und-schnittstellen, spezial-dolmetscher-sonderfall-und-edge-case, spezial-dolmetscherkosten-zahlen-schwelle... |
| `kompendium-13-spezial-fahrtkosten-bis-spezial-freistehende` | jveg-kostenpruefer: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (spezial-fahrtkosten-behoerden-gericht-und-registerweg, spezial-festsetzung-mehrparteien-konflikt-und-interessen, spezial-freistehender-erstpruefung-... |
| `kompendium-14-spezial-gate-beweisl-bis-spezial-quality-mand` | jveg-kostenpruefer: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (spezial-gate-beweislast-und-darlegungslast, spezial-jveg-tatbestand-beweis-und-belege, spezial-quality-mandantenkommunikation-entscheidungsvorlage)... |
| `kompendium-15-spezial-uebernachtun-bis-spezial-vorschuss-ri` | jveg-kostenpruefer: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (spezial-uebernachtung-schriftsatz-brief-und-memo-bausteine, spezial-verdienstausfall-verhandlung-vergleich-und-eskalation, spezial-vorschuss-risikoa... |
| `kompendium-16-spezial-zeugenentsch-bis-spezial-zeugenentsch` | jveg-kostenpruefer: Konsolidiertes Skill-Kompendium 16; bündelt 1 frühere Spezialskills (spezial-zeugenentschaedigung-dokumentenmatrix-und-lueckenliste) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-rechenprotokolle-red-team-und-qualitaetskontrolle` | Rechenprotokolle: Red-Team und Qualitätskontrolle im Plugin jveg kostenpruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-sachverstaendigen-livequellen-und-rechtsprechungscheck` | Sachverstaendigen: Livequellen- und Rechtsprechungscheck im Plugin jveg kostenpruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin jveg-kostenpruefer: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin jveg-kostenpruefer: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin jveg-kostenpruefer: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin jveg-kostenpruefer: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin jveg-kostenpruefer: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin jveg-kostenpruefer: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
