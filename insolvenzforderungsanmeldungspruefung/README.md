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
| `kompendium-01-allgemein-bis-workflow-fristen-und` | insolvenzforderungsanmeldungspruefung: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfpr... |
| `kompendium-02-workflow-mandantenko-bis-spezial-inso-fristen` | insolvenzforderungsanmeldungspruefung: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-mandantenkommunikation, workflow-redteam-qualitygate, spezial-inso-fristen-form-und-zustaendigkeit) und bewahrt deren Wo... |
| `kompendium-03-ifap-kommandocenter-bis-ifap-vbuh-pruefung` | insolvenzforderungsanmeldungspruefung: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (ifap-kommandocenter, ifap-pruefentscheidung, ifap-vbuh-pruefung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgab... |
| `kompendium-04-iap-anmeldepruefung-bis-iap-konzernforderung` | insolvenzforderungsanmeldungspruefung: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (iap-anmeldepruefung-bauleiter, iap-aussonderung-absonderung-spezial, iap-konzernforderungen-anfechtung-spezial) und bewahrt deren... |
| `kompendium-05-iap-rangordnung-chec-bis-ifap-beleg-und-urkun` | insolvenzforderungsanmeldungspruefung: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (iap-rangordnung-checkliste, ifap-aktenanlage-batchregister, ifap-beleg-und-urkundencheck) und bewahrt deren Workflows, Normanker,... |
| `kompendium-06-ifap-dubletten-serie-bis-ifap-grund-betrag-zi` | insolvenzforderungsanmeldungspruefung: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (ifap-dubletten-serienforderungen, ifap-formalpruefung-174, ifap-grund-betrag-zinsen) und bewahrt deren Workflows, Normanker, Prüf... |
| `kompendium-07-ifap-intake-kanalche-bis-ifap-nachforderung-m` | insolvenzforderungsanmeldungspruefung: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (ifap-intake-kanalcheck, ifap-masseverbindlichkeit-abgrenzen, ifap-nachforderung-maengelschreiben) und bewahrt deren Workflows, No... |
| `kompendium-08-ifap-nachtraegliche-bis-ifap-quality-gate` | insolvenzforderungsanmeldungspruefung: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (ifap-nachtraegliche-anmeldung-177, ifap-pruefungstermin-176, ifap-quality-gate) und bewahrt deren Workflows, Normanker, Prüfprogr... |
| `kompendium-09-ifap-rang-nachrang-a-bis-ifap-streitige-forde` | insolvenzforderungsanmeldungspruefung: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (ifap-rang-nachrang-absonderung, ifap-schuldnerwiderspruch-184, ifap-streitige-forderung-179-180) und bewahrt deren Workflows, Nor... |
| `kompendium-10-ifap-tabellenauszug-bis-ifap-verteilung-best` | insolvenzforderungsanmeldungspruefung: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (ifap-tabellenauszug-178, ifap-tabellenimport-175, ifap-verteilung-bestrittene-189) und bewahrt deren Workflows, Normanker, Prüfpr... |
| `kompendium-11-spezial-belege-dokum-bis-spezial-betrag-behoe` | insolvenzforderungsanmeldungspruefung: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (spezial-belege-dokumentenmatrix-und-lueckenliste, spezial-bestreiten-mehrparteien-konflikt-und-interessen, spezial-betrag-behoerd... |
| `kompendium-12-spezial-feststellung-bis-spezial-grund-risiko` | insolvenzforderungsanmeldungspruefung: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (spezial-feststellung-internationaler-bezug-und-schnittstellen, spezial-forderungsgrund-rang-und-belegpruefung, spezial-grund-risi... |
| `kompendium-13-spezial-ifap-mandant-bis-spezial-intake-tatbe` | insolvenzforderungsanmeldungspruefung: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (spezial-ifap-mandantenkommunikation-entscheidungsvorlage, spezial-insolvenzforderungsanmeldungspruefung-erstpruefung, spezial-int... |
| `kompendium-14-spezial-kanalcheck-b-bis-spezial-pruefungster` | insolvenzforderungsanmeldungspruefung: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (spezial-kanalcheck-beweislast-und-darlegungslast, spezial-masseverbindlichkeit-sonderfall-und-edge-case, spezial-pruefungstermin-... |
| `kompendium-15-spezial-rang-schrift-bis-spezial-tabellenimpo` | insolvenzforderungsanmeldungspruefung: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (spezial-rang-schriftsatz-brief-und-memo-bausteine, spezial-tabellenauszug-formular-portal-und-einreichung, spezial-tabellenimport... |
| `kompendium-16-spezial-vbuh-verhand-bis-spezial-vbuh-verhand` | insolvenzforderungsanmeldungspruefung: Konsolidiertes Skill-Kompendium 16; bündelt 1 frühere Spezialskills (spezial-vbuh-verhandlung-vergleich-und-eskalation) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-nachforderungen-livequellen-und-rechtsprechungscheck` | Nachforderungen: Livequellen- und Rechtsprechungscheck im Forderungsprüfung: fachlich vertiefter Spezialskill mit Normenradar (InsO/Tabelle/Bestreiten), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse... |
| `spezial-verteilung-red-team-und-qualitaetskontrolle` | Verteilung: Red-Team und Qualitätskontrolle im Forderungsprüfung: fachlich vertiefter Spezialskill mit Normenradar (InsO/Tabelle/Bestreiten), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin insolvenzforderungsanmeldungspruefung: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin insolvenzforderungsanmeldungspruefung: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin insolvenzforderungsanmeldungspruefung: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin insolvenzforderungsanmeldungspruefung: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin insolvenzforderungsanmeldungspruefung: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin insolvenzforderungsanmeldungspruefung: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
