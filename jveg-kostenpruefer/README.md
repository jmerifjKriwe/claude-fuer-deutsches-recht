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
| `beschwerde-dolmetscher-sonderfall` | Beschwerde Dolmetscher Sonderfall im JVEG-Kostenprüfung: prüft konkret Beschwerde, Dolmetscher, Dolmetscherkosten. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `fahrtkosten-festsetzung-interessen` | Fahrtkosten Festsetzung Interessen im JVEG-Kostenprüfung: prüft konkret Fahrtkosten, Festsetzung, Freistehender. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `gate-beweislast-jveg-quality` | Gate Beweislast Jveg Quality im JVEG-Kostenprüfung: prüft konkret Gate, JVEG, Quality. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `gerichtsschreiben-kuerzung-wegfall` | Gerichtsschreiben Kuerzung Wegfall im JVEG-Kostenprüfung: prüft konkret Gerichtsschreiben zur JVEG-Kostenkuerzung rechtlich prüfen, Navigationszentrum für alle JVEG-Kostenprüfer-Skills, Kuerzung oder Wegfall der JVEG-Verguetung nach § 8a... |
| `jveg-anspruchsberechtigung-antragsgenerator` | Anspruchsberechtigung Antragsgenerator im JVEG-Kostenprüfung: prüft konkret Anspruchsberechtigung nach JVEG prüfen, Antrag auf gerichtliche Kostenfestsetzung nach JVEG, Verguetung für gerichtliche Dolmetscher und Übersetzer nach. Liefert... |
| `jveg-dolmetscher-uebersetzer-fahrtkosten` | Dolmetscher Uebersetzer Fahrtkosten im JVEG-Kostenprüfung: prüft konkret Spezialfall Dolmetscher- und Uebersetzerverguetung JVEG, Fahrtkosten nach JVEG berechnen, Beschwerde gegen JVEG-Kostenfestsetzungsbeschluss einlegen. Liefert priori... |
| `jveg-gate-rechenblatt` | Gate Rechenblatt im JVEG-Kostenprüfung: prüft konkret Qualitaets-Gate für JVEG-Kostenberechnungen, JVEG-Verguetungsberechnung in strukturiertem Rechenblatt, Sachverständigenrechnung nach JVEG prüfen oder erstellen. Liefert priorisierten... |
| `jveg-kostenpruefer-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `jveg-kostenpruefer-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `jveg-kostenpruefer-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `jveg-kostenpruefer-output-waehlen` | Output wählen im JVEG-Kostenprüfung: Diese Output-Weiche für Jveg Kostenpruefer entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `jveg-kostenpruefer-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `jveg-kostenpruefer-start-chronologie-fristen` | Start Chronologie Fristen im JVEG-Kostenprüfung: prüft konkret Einstieg, Schnelltriage und Fallrouting im JVEG Kostenpruefer-Plugin, Chronologie und Belegmatrix im Plugin jveg-kostenpruefer, Fristen- und Risikoampel im Plugin jveg-kosten... |
| `jveg-kostenpruefer-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `jveg-sonstige-aufwendungen-uebernachtung` | Sonstige Aufwendungen Uebernachtung im JVEG-Kostenprüfung: prüft konkret Sonstige Aufwendungen nach § 7 JVEG prüfen und belegen, Übernachtungs- und Verpflegungskosten nach JVEG berechnen, Verdienstausfall und Zeitversaeumnis nach §§ 20 f... |
| `jveg-vorschuss-kostenrisiko` | Vorschuss Kostenrisiko im JVEG-Kostenprüfung: prüft konkret Vorschuss auf JVEG-Verguetung beantragen, Spezialfall Vorschuss und Kostenrisiko § 17 JVEG, Zeugenentschaedigung nach JVEG berechnen. Liefert priorisierten Output mit Norm-Pinpo... |
| `jveg-zeugenentschaedigung` | Zeugenentschaedigung im JVEG-Kostenprüfung: prüft konkret Checkliste Zeugenentschaedigung JVEG, KI-Deklaration in Sachverständigengutachten prüfen, Belegfeste. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Sch... |
| `jveg-zeugenentschaedigung-antrag` | Zeugenentschaedigung Antrag im JVEG-Kostenprüfung: fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |
| `kostenfestsetzung-kostenpruefer` | Kostenfestsetzung Kostenpruefer im JVEG-Kostenprüfung: prüft konkret Fristen, Kostenfestsetzung mit Belegen, Fristen und Erinnerung, Kostenpruefer. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `mandantenkommunikation-redteam-qualitygate` | Mandantenkommunikation Redteam Qualitygate im JVEG-Kostenprüfung: prüft konkret Mandantenkommunikation im Plugin jveg-kostenpruefer, Red-Team Qualitygate im Plugin jveg-kostenpruefer, Antragsfristen nach JVEG prüfen. Liefert priorisierte... |
| `rechenprotokolle-fehlerkatalog` | Rechenprotokolle Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `sachverstaendigen-quellenkarte` | Sachverstaendigen Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `uebernachtung-verdienstausfall-vorschuss` | Uebernachtung Verdienstausfall Vorschuss im JVEG-Kostenprüfung: prüft konkret Uebernachtung, Verdienstausfall, Vorschuss. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `uebersetzer-fristennotiz-jveg` | Uebersetzer Fristennotiz Jveg im JVEG-Kostenprüfung: prüft konkret Uebersetzer, Bauleiter Sachverstaendigenrechnung JVEG, JVEG-relevante Daten aus Gerichtsakten und. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächst... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
