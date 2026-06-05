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
| `bestreiten-interessen-betrag` | Bestreiten Interessen Betrag im Plugin Insolvenzforderungsanmeldungspruefung: prüft konkret Belege, Bestreiten, Betrag. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `feststellung-forderungsgrund-rang-grund` | Feststellung Forderungsgrund Rang Grund im Plugin Insolvenzforderungsanmeldungspruefung: prüft konkret Feststellung, Forderungsgrund, Rang und Belegprüfung zur Tabelle, Grund. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel... |
| `forderungsanmeldung-mandantenkommunikation-redteam-qualitygate` | Forderungsanmeldung Mandantenkommunikation Redteam Qualitygate im Plugin Insolvenzforderungsanmeldungspruefung: prüft konkret Mandantenkommunikation im Plugin, Red-Team Qualitygate im Plugin, InsO. Liefert priorisierten Output mit Norm-P... |
| `forderungsanmeldung-vbuh-verhandlung-vergleich-eskalation` | Forderungsanmeldung Vbuh Verhandlung Vergleich Eskalation im Plugin Insolvenzforderungsanmeldungspruefung: fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |
| `iap-anmeldepruefung-bauleiter-aussonderung` | IAP Anmeldepruefung Bauleiter Aussonderung im Plugin Insolvenzforderungsanmeldungspruefung: prüft konkret Bauleiter Pruefung von Insolvenzforderungsanmeldungen, Spezialfall Aussonderung und Absonderung §§ 47 sowie 49 ff, Spezialfall Konz... |
| `iap-rangordnung-ifap-aktenanlage-beleg` | IAP Rangordnung Ifap Aktenanlage Beleg im Plugin Insolvenzforderungsanmeldungspruefung: prüft konkret Checkliste Rangordnung der Insolvenzforderungen § 38 / § 39, Batchregister für Massenverfahren, Belege und Urkunden bei Insolvenzforder... |
| `ifap-dubletten-serienforderungen` | Ifap Dubletten Serienforderungen im Plugin Insolvenzforderungsanmeldungspruefung: prüft konkret Dubletten und Serienforderungen in Insolvenzanmeldungen, Formalprüfung Forderungsanmeldung nach § 174 InsO, Anspruchsgrund Betrag und Zinsen... |
| `ifap-insolvenzforderungsanmeldungspruefung` | Ifap Insolvenzforderungsanmeldungspruefung im Plugin Insolvenzforderungsanmeldungspruefung: prüft konkret Ifap, Insolvenzforderungsanmeldungspruefung, Intake. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schr... |
| `ifap-intake-kanalcheck-masseverbindlichkeit` | Ifap Intake Kanalcheck Masseverbindlichkeit im Plugin Insolvenzforderungsanmeldungspruefung: prüft konkret Eingehende Forderungsanmeldungen kanalübergreifend erfassen, Masseverbindlichkeiten von Insolvenzforderungen abgrenzen, Mängel- un... |
| `ifap-nachtraegliche-anmeldung-pruefungstermin` | Ifap Nachtraegliche Anmeldung Pruefungstermin im Plugin Insolvenzforderungsanmeldungspruefung: prüft konkret Verspätete und nachträgliche Forderungsanmeldungen nach §, Prüfungstermin nach § 176 InsO vorbereiten, Qualitätsgate vor Tabelle... |
| `ifap-pruefentscheidung-vbuh` | Ifap Pruefentscheidung Vbuh im Plugin Insolvenzforderungsanmeldungspruefung: prüft konkret Kommandocenter Insolvenzforderungsanmeldungsprüfung, Prüfentscheidung Forderung festzustellen oder zu bestreiten, Vorsätzlich begangene unerlaubte... |
| `ifap-rang-nachrang-schuldnerwiderspruch` | Ifap Rang Nachrang Schuldnerwiderspruch im Plugin Insolvenzforderungsanmeldungspruefung: prüft konkret Rang Nachrang Absonderung und Aussonderung bei, Schuldnerwiderspruch nach § 184 InsO prüfen und Fristen, Streitige Forderungen nach §§... |
| `ifap-tabellenauszug-tabellenimport-verteilung` | Ifap Tabellenauszug Tabellenimport Verteilung im Plugin Insolvenzforderungsanmeldungspruefung: prüft konkret Tabellenauszug und Feststellungswirkung nach § 178 InsO, Tabelleneintrag und Tabellenimport nach § 175 InsO, Verteilung bei best... |
| `inso-forderungsanmeldung-start-chronologie-fristen` | Inso Forderungsanmeldung Start Chronologie Fristen im Plugin Insolvenzforderungsanmeldungspruefung: prüft konkret Einstieg, Schnelltriage und Fallrouting im, Chronologie und Belegmatrix im Plugin, Fristen- und Risikoampel im Plugin. Lief... |
| `insolvenzforderungsanmeldungspruefung-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `insolvenzforderungsanmeldungspruefung-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `insolvenzforderungsanmeldungspruefung-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `insolvenzforderungsanmeldungspruefung-output-waehlen` | Output wählen im Plugin Insolvenzforderungsanmeldungspruefung: Diese Output-Weiche für Insolvenzforderungsanmeldungspruefung entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nä... |
| `insolvenzforderungsanmeldungspruefung-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `insolvenzforderungsanmeldungspruefung-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `kanalcheck-beweislast-masseverbindlichkeit` | Kanalcheck Beweislast Masseverbindlichkeit im Plugin Insolvenzforderungsanmeldungspruefung: prüft konkret Kanalcheck, Masseverbindlichkeit, Pruefungstermin. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `nachforderungen-quellenkarte` | Nachforderungen Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `rang-tabellenauszug-tabellenimport` | Rang Tabellenauszug Tabellenimport im Plugin Insolvenzforderungsanmeldungspruefung: prüft konkret Rang, Tabellenauszug, Tabellenimport. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `verteilung-fehlerkatalog` | Verteilung Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
