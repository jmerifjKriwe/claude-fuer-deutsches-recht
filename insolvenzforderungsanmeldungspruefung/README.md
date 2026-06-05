# Insolvenzforderungsanmeldungsprüfung

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`insolvenzforderungsanmeldungspruefung`) | [`insolvenzforderungsanmeldungspruefung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzforderungsanmeldungspruefung.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Insolvenzforderungsanmeldungsprüfung Phoenix Solar Montage GmbH** (`insolvenzforderungsanmeldungspruefung-phoenix-solar`) | [Gesamt-PDF lesen](../testakten/insolvenzforderungsanmeldungspruefung-phoenix-solar/gesamt-pdf/insolvenzforderungsanmeldungspruefung-phoenix-solar_gesamt.pdf) | [`testakte-insolvenzforderungsanmeldungspruefung-phoenix-solar.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-insolvenzforderungsanmeldungspruefung-phoenix-solar.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Cowork-Plugin für die Prüfung von Insolvenzforderungen vom Eingang bis zur Tabellenfeststellung. Es ist ein vollständiger Arbeitsraum für Verwalterbüro, Sachwaltung, Forderungsmanagement und Prozessnachlauf: Anmeldung erfassen, Mängel erkennen, Belege nachfordern, Grund, Betrag und Rang prüfen, Entscheidung dokumentieren, Tabelle befüllen, Prüfungstermin vorbereiten, Bestreiten oder Feststellung ausgeben und streitige Forderungen bis zur Verteilung nachhalten.

## Wofür das Plugin gedacht ist

- Masseneingang von Forderungsanmeldungen per Post, E-Mail, Portalexport, Tabellenliste oder manuellem Upload.
- Formale Prüfung nach § 174 InsO einschließlich Grund, Betrag, Urkunden, elektronischer Anmeldung, vbuH-/Unterhalts-/Steuerstraf-Hinweis und Nachrang.
- Materielle Plausibilisierung anhand Schuldnerbuchhaltung, OPOS, Verträgen, Titeln, Lieferscheinen, Kontoauszügen und bisherigem Verfahrensstand.
- Entscheidungsvorbereitung für Feststellung, Teilbestreiten, vollständiges Bestreiten, Nachforderung, Rangkorrektur, vbuH-Widerspruch und Masse-/Insolvenzforderung-Abgrenzung.
- Tabellenarbeit nach § 175 InsO, Prüfungstermin nach § 176 InsO, nachträgliche Anmeldung nach § 177 InsO, Feststellungswirkung nach § 178 InsO und Streitnachlauf nach §§ 179 bis 181, 184 und 189 InsO.

## Leitprinzip

Das Plugin arbeitet verzeihend, aber nicht schlampig. Es akzeptiert unsaubere Gläubigeranschreiben, unvollständige Belege, widersprüchliche Rechnungsnummern und doppelte Portaleingänge. Es zieht daraus aber nie automatisch eine Feststellung. Fehlende Substanz wird als Mangel, Risiko oder Rückfrage markiert. Jede Tabellenentscheidung bleibt nachvollziehbar: Was ist angemeldet, was ist belegt, was ist bestritten, warum, durch wen und mit welchem nächsten Schritt.

## Typischer Ablauf

1. Intake öffnen: Eingangsstapel, Metadaten, Gläubiger, Frist, Kanal, Dateinamen und Dublettenverdacht erfassen.
2. § 174-Check: Grund, Betrag, Rang, Belege, vbuH-Kennzeichnung und elektronische Form prüfen.
3. Belegkette bilden: Rechnung, Titel, Vertrag, Lieferung, Zahlung, Buchhaltung, offene Restforderung und Rang verbinden.
4. Prüfentscheidung treffen: feststellen, teilweise feststellen, bestreiten, vorläufig zurückstellen oder Nachforderung schreiben.
5. Tabelle füllen: Tabellenimport, Prüfvermerk, Widerspruchsvermerk und Prüfungsterminmappe erzeugen.
6. Nachlauf steuern: Tabellenauszug, Feststellungsklage, Schuldnerwiderspruch, § 189-Verteilung und Wiedervorlagen kontrollieren.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| ifap-kommandocenter | Startet den gesamten Prüfpfad und entscheidet, welcher Arbeitsmodus passt. |
| ifap-intake-kanalcheck | Erfasst Post, E-Mail, Portal, Stapel, Nachzügler und Metadaten. |
| ifap-aktenanlage-batchregister | Baut Register, Prüfnummern, Gläubigerstamm und Eingangsbuch auf. |
| ifap-formalpruefung-174 | Prüft die formalen Mindestangaben nach § 174 InsO. |
| ifap-beleg-und-urkundencheck | Bildet die Belegkette und erkennt fehlende Urkunden. |
| ifap-grund-betrag-zinsen | Prüft Anspruchsgrund, Betrag, Teilzahlungen und Zinslauf. |
| ifap-rang-nachrang-absonderung | Trennt Insolvenzforderung, Nachrang, Sicherheiten und Ausfall. |
| ifap-masseverbindlichkeit-abgrenzen | Erkennt falsch angemeldete Masseforderungen und Abgrenzungsfälle. |
| ifap-vbuh-pruefung | Prüft vbuH, Unterhalt und Steuerstraftat mit Tatsachenbasis. |
| ifap-dubletten-serienforderungen | Erkennt Mehrfachanmeldungen, Serienrechnungen und Vertreterwechsel. |
| ifap-nachforderung-maengelschreiben | Erstellt präzise Beleg- und Substanznachforderungen. |
| ifap-pruefentscheidung | Erstellt Feststellungs-, Teilbestreitens- und Bestreitensvermerke. |
| ifap-tabellenimport-175 | Baut einen gerichtsfesten Tabellenimport nach § 175 InsO. |
| ifap-pruefungstermin-176 | Bereitet Prüfungstermin oder schriftliches Verfahren vor. |
| ifap-nachtraegliche-anmeldung-177 | Steuert verspätete und geänderte Anmeldungen. |
| ifap-tabellenauszug-178 | Erzeugt Tabellenauszug- und Feststellungswirkungs-Ausgaben. |
| ifap-streitige-forderung-179-180 | Führt den Feststellungsklage- und Rechtsstreit-Nachlauf. |
| ifap-schuldnerwiderspruch-184 | Behandelt Schuldnerwiderspruch und Monatsfrist bei titulierten Forderungen. |
| ifap-verteilung-bestrittene-189 | Hält § 189-Nachweise und Rückbehalte für Verteilungen nach. |
| ifap-quality-gate | Prüft Vollständigkeit, Plausibilität, Quellen, Fristen und Audit-Trail. |

## Grenzen

Das Plugin trifft keine unüberprüfte Rechtsentscheidung und ersetzt keine fachliche Prüfung. Bei streitigen Rechtsfragen, Rechtskraft-/Titelthemen, vbuH, Rangverschiebungen, Absonderungsrechten, § 189-Rückbehalten und drohenden Feststellungsklagen verlangt es ausdrücklich menschliche Freigabe.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein-workflow-chronologie-fristen` | Nutze dies, wenn Allgemein, Workflow Chronologie Und Belegmatrix, Workflow Fristen Und Risikoampel im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeitet werden soll. Auslöser: Bitte Allgemein, Workflow Chronologie Und Belegm... |
| `anschluss-routing` | Nutze dies, wenn Anschluss-Routing im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeitet werden soll. Auslöser: Ich habe ein neues Thema im Bereich Insolvenzforderungsanmeldungspruefung.; Welche Unterlagen brauchen Sie?; Wel... |
| `bestreiten-interessen-betrag` | Nutze dies, wenn Spezial Belege Dokumentenmatrix Und Lueckenliste, Spezial Bestreiten Mehrparteien Konflikt Und Interessen, Spezial Betrag Behörden Gericht Und Registerweg im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeite... |
| `dokumente-intake` | Nutze dies, wenn Dokumentenintake im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeitet werden soll. Auslöser: Ich lade Unterlagen hoch.; Was fehlt noch?; Bitte Dokumente sortieren.. |
| `einstieg-routing` | Nutze dies, wenn Einstieg und Routing im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeitet werden soll. Auslöser: Ich habe ein neues Thema im Bereich Insolvenzforderungsanmeldungspruefung.; Welche Unterlagen brauchen Sie?;... |
| `feststellung-forderungsgrund-rang-grund` | Nutze dies, wenn Spezial Feststellung Internationaler Bezug Und Schnittstellen, Spezial Forderungsgrund Rang Und Belegpruefung, Spezial Grund Risikoampel Und Gegenargumente im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeit... |
| `iap-anmeldepruefung-bauleiter-aussonderung` | Nutze dies, wenn Iap Anmeldepruefung Bauleiter, Iap Aussonderung Absonderung Spezial, Iap Konzernforderungen Anfechtung Spezial im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeitet werden soll. Auslöser: Bitte Iap Anmeldepr... |
| `iap-rangordnung-ifap-aktenanlage-ifap-beleg` | Nutze dies, wenn Iap Rangordnung Checkliste, Ifap Aktenanlage Batchregister, Ifap Beleg Und Urkundencheck im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeitet werden soll. Auslöser: Bitte Iap Rangordnung Checkliste, Ifap Ak... |
| `ifap-dubletten-serienforderungen` | Nutze dies, wenn Ifap Dubletten Serienforderungen, Ifap Formalpruefung 174, Ifap Grund Betrag Zinsen im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeitet werden soll. Auslöser: Bitte Ifap Dubletten Serienforderungen, Ifap F... |
| `ifap-insolvenzforderungsanmeldungspruefung` | Nutze dies, wenn Spezial Ifap Mandantenkommunikation Entscheidungsvorlage, Spezial Insolvenzforderungsanmeldungspruefung Erstpruefung, Spezial Intake Tatbestand Beweis Und Belege im Plugin Insolvenzforderungsanmeldungspruefung konkret be... |
| `ifap-intake-kanalcheck-masseverbindlichkeit` | Nutze dies, wenn Ifap Intake Kanalcheck, Ifap Masseverbindlichkeit Abgrenzen, Ifap Nachforderung Maengelschreiben im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeitet werden soll. Auslöser: Ich lade Unterlagen hoch.; Was fe... |
| `ifap-nachtraegliche-anmeldung-pruefungstermin` | Nutze dies, wenn Ifap Nachtraegliche Anmeldung 177, Ifap Pruefungstermin 176, Ifap Quality Gate im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeitet werden soll. Auslöser: Bitte Ifap Nachtraegliche Anmeldung 177, Ifap Pruef... |
| `ifap-pruefentscheidung-vbuh` | Nutze dies, wenn Ifap Kommandocenter, Ifap Pruefentscheidung, Ifap Vbuh Prüfung im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeitet werden soll. Auslöser: Bitte Ifap Kommandocenter, Ifap Pruefentscheidung, Ifap Vbuh Prüfun... |
| `ifap-rang-nachrang-schuldnerwiderspruch` | Nutze dies, wenn Ifap Rang Nachrang Absonderung, Ifap Schuldnerwiderspruch 184, Ifap Streitige Forderung 179 180 im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeitet werden soll. Auslöser: Bitte Ifap Rang Nachrang Absonderu... |
| `ifap-tabellenauszug-tabellenimport-verteilung` | Nutze dies, wenn Ifap Tabellenauszug 178, Ifap Tabellenimport 175, Ifap Verteilung Bestrittene 189 im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeitet werden soll. Auslöser: Bitte Ifap Tabellenauszug 178, Ifap Tabellenimpo... |
| `inso` | Nutze dies, wenn Workflow Mandantenkommunikation, Workflow Redteam Qualitygate, Spezial Inso Fristen Form Und Zustaendigkeit im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeitet werden soll. Auslöser: Was kann hier schiefge... |
| `kanalcheck-beweislast-masseverbindlichkeit` | Nutze dies, wenn Spezial Kanalcheck Beweislast Und Darlegungslast, Spezial Masseverbindlichkeit Sonderfall Und Edge Case, Spezial Pruefungstermin Compliance Dokumentation Und Akte im Plugin Insolvenzforderungsanmeldungspruefung konkret b... |
| `nachforderungen-quellenkarte` | Nutze dies, wenn Nachforderungen Quellenkarte im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeitet werden soll. Auslöser: Welche amtliche Quelle prüfe ich zuerst?; Gibt es aktuelle Rechtsprechung?; Bitte Fundstellen verifiz... |
| `output-waehlen` | Nutze dies, wenn Output wählen im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeitet werden soll. Auslöser: Bitte Output wählen prüfen.; Erstelle eine Arbeitsfassung zu Output wählen.; Welche Normen und Nachweise brauche ich?. |
| `quellen-livecheck` | Nutze dies, wenn Rechtsquellen-Livecheck im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeitet werden soll. Auslöser: Welche amtliche Quelle prüfe ich zuerst?; Gibt es aktuelle Rechtsprechung?; Bitte Fundstellen verifizieren.. |
| `rang-tabellenauszug-tabellenimport` | Nutze dies, wenn Spezial Rang Schriftsatz Brief Und Memo Bausteine, Spezial Tabellenauszug Formular Portal Und Einreichung, Spezial Tabellenimport Zahlen Schwellen Und Berechnung im Plugin Insolvenzforderungsanmeldungspruefung konkret be... |
| `unterlagen-luecken` | Nutze dies, wenn Unterlagen und Lücken im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeitet werden soll. Auslöser: Ich lade Unterlagen hoch.; Was fehlt noch?; Bitte Dokumente sortieren.. |
| `vbuh` | Nutze dies, wenn Spezial Vbuh Verhandlung Vergleich Und Eskalation im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeitet werden soll. Auslöser: Bitte Spezial Vbuh Verhandlung Vergleich Und Eskalation prüfen.; Erstelle eine A... |
| `verteilung-fehlerkatalog` | Nutze dies, wenn Verteilung Fehlerkatalog im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.; Welche Frist oder Beweislast übersehe ich?. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
