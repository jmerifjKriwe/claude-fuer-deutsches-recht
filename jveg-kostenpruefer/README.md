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
| `allgemein-workflow-chronologie-fristen` | Nutze dies, wenn Allgemein, Workflow Chronologie Und Belegmatrix, Workflow Fristen Und Risikoampel im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Bitte Allgemein, Workflow Chronologie Und Belegmatrix, Workflow Fri... |
| `anschluss-routing` | Nutze dies, wenn Anschluss-Routing im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Ich habe ein neues Thema im Bereich Jveg Kostenpruefer.; Welche Unterlagen brauchen Sie?; Welcher Spezialskill passt?. |
| `beschwerde-dolmetscher-sonderfall` | Nutze dies, wenn Spezial Beschwerde Internationaler Bezug Und Schnittstellen, Spezial Dolmetscher Sonderfall Und Edge Case, Spezial Dolmetscherkosten Zahlen Schwellen Und Berechnung im Plugin Jveg Kostenpruefer konkret bearbeitet werden... |
| `dokumente-intake` | Nutze dies, wenn Dokumentenintake im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Ich lade Unterlagen hoch.; Was fehlt noch?; Bitte Dokumente sortieren.. |
| `einstieg-routing` | Nutze dies, wenn Einstieg und Routing im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Ich habe ein neues Thema im Bereich Jveg Kostenpruefer.; Welche Unterlagen brauchen Sie?; Welcher Spezialskill passt?. |
| `fahrtkosten-festsetzung-interessen` | Nutze dies, wenn Spezial Fahrtkosten Behörden Gericht Und Registerweg, Spezial Festsetzung Mehrparteien Konflikt Und Interessen, Spezial Freistehender Erstpruefung Und Mandatsziel im Plugin Jveg Kostenpruefer konkret bearbeitet werden so... |
| `gate-beweislast-jveg-quality` | Nutze dies, wenn Spezial Gate Beweislast Und Darlegungslast, Spezial Jveg Tatbestand Beweis Und Belege, Spezial Quality Mandantenkommunikation Entscheidungsvorlage im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Bi... |
| `jveg` | Nutze dies, wenn Workflow Mandantenkommunikation, Workflow Redteam Qualitygate, Jveg Fristen Erloeschen im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.; Welche Fri... |
| `jveg-anspruchsberechtigung-antragsgenerator` | Nutze dies, wenn Jveg Anspruchsberechtigung, Jveg Antragsgenerator, Jveg Dolmetscher Uebersetzer im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Bitte Jveg Anspruchsberechtigung, Jveg Antragsgenerator, Jveg Dolmets... |
| `jveg-dolmetscher-uebersetzer-fahrtkosten` | Nutze dies, wenn Jveg Dolmetscher Uebersetzer Spezial, Jveg Fahrtkosten, Jveg Festsetzung Beschwerde im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Bitte Jveg Dolmetscher Uebersetzer Spezial, Jveg Fahrtkosten, Jve... |
| `jveg-gate-rechenblatt` | Nutze dies, wenn Jveg Quality Gate, Jveg Rechenblatt, Jveg Sachverstaendigenrechnung im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Bitte Jveg Quality Gate, Jveg Rechenblatt, Jveg Sachverstaendigenrechnung prüfen.... |
| `jveg-gerichtsschreiben-jveg-kuerzung-wegfall` | Nutze dies, wenn Jveg Gerichtsschreiben Prüfung, Jveg Kommandocenter, Jveg Kuerzung Wegfall 8A im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Bitte Jveg Gerichtsschreiben Prüfung, Jveg Kommandocenter, Jveg Kuerzun... |
| `jveg-sonstige-aufwendungen-uebernachtung` | Nutze dies, wenn Jveg Sonstige Aufwendungen Belege, Jveg Uebernachtung Aufwand, Jveg Verdienstausfall Haushalt Zeit im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Bitte Jveg Sonstige Aufwendungen Belege, Jveg Uebe... |
| `jveg-vorschuss-kostenrisiko` | Nutze dies, wenn Jveg Vorschuss, Jveg Vorschuss Kostenrisiko Spezial, Jveg Zeugenentschaedigung im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Bitte Jveg Vorschuss, Jveg Vorschuss Kostenrisiko Spezial, Jveg Zeugen... |
| `jveg-zeugenentschaedigung` | Nutze dies, wenn Jveg Zeugenentschaedigung Checkliste, Prüfung Sachverstaendigengutachten Ki Deklaration, Spezial Belegfeste Formular Portal Und Einreichung im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Bitte Jve... |
| `kostenfestsetzung-kostenpruefer` | Nutze dies, wenn Spezial Fristen Compliance Dokumentation Und Akte, Spezial Kostenfestsetzung Belege Und Fristen, Spezial Kostenpruefer Fristen Form Und Zustaendigkeit im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser... |
| `output-waehlen` | Nutze dies, wenn Output wählen im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Bitte Output wählen prüfen.; Erstelle eine Arbeitsfassung zu Output wählen.; Welche Normen und Nachweise brauche ich?. |
| `quellen-livecheck` | Nutze dies, wenn Rechtsquellen-Livecheck im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Welche amtliche Quelle prüfe ich zuerst?; Gibt es aktuelle Rechtsprechung?; Bitte Fundstellen verifizieren.. |
| `rechenprotokolle-fehlerkatalog` | Nutze dies, wenn Rechenprotokolle Fehlerkatalog im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.; Welche Frist oder Beweislast übersehe ich?. |
| `sachverstaendigen-quellenkarte` | Nutze dies, wenn Sachverstaendigen Quellenkarte im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Welche amtliche Quelle prüfe ich zuerst?; Gibt es aktuelle Rechtsprechung?; Bitte Fundstellen verifizieren.. |
| `uebernachtung-verdienstausfall-vorschuss` | Nutze dies, wenn Spezial Uebernachtung Schriftsatz Brief Und Memo Bausteine, Spezial Verdienstausfall Verhandlung Vergleich Und Eskalation, Spezial Vorschuss Risikoampel Und Gegenargumente im Plugin Jveg Kostenpruefer konkret bearbeitet... |
| `uebersetzer-fristennotiz-jveg` | Nutze dies, wenn Spezial Uebersetzer Fristennotiz Und Naechster Schritt, Jveg Sachverstaendigenrechnung Bauleiter, Jveg Aktenstripper im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Bitte Spezial Uebersetzer Friste... |
| `unterlagen-luecken` | Nutze dies, wenn Unterlagen und Lücken im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Ich lade Unterlagen hoch.; Was fehlt noch?; Bitte Dokumente sortieren.. |
| `zeugenentschaedigung` | Nutze dies, wenn Spezial Zeugenentschaedigung Dokumentenmatrix Und Lueckenliste im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Bitte Spezial Zeugenentschaedigung Dokumentenmatrix Und Lueckenliste prüfen.; Erstelle... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
