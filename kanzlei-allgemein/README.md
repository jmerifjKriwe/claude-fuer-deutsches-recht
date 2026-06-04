# Kanzlei-Allgemein-Plugin

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`kanzlei-allgemein`) | [`kanzlei-allgemein.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kanzlei-allgemein.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Kanzlei-Allgemein-Plugin** (`kanzlei-allgemein-alltag`) | [Gesamt-PDF lesen](../testakten/kanzlei-allgemein-alltag/gesamt-pdf/kanzlei-allgemein-alltag_gesamt.pdf) | [`testakte-kanzlei-allgemein-alltag.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kanzlei-allgemein-alltag.zip) |
| **Akte LG Regensburg — Sieglinger gegen Burgwald Energietechnik GmbH** (`sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger`) | [Gesamt-PDF lesen](../testakten/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger/gesamt-pdf/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger_gesamt.pdf) | [`testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip) |
| **Klingenhain Musikschule / DRV-Statusprüfung** (`statusfeststellung-drv-musikschule-gf-freelancer-klingenhain`) | [Gesamt-PDF lesen](../testakten/statusfeststellung-drv-musikschule-gf-freelancer-klingenhain/gesamt-pdf/statusfeststellung-drv-musikschule-gf-freelancer-klingenhain_gesamt.pdf) | [`testakte-statusfeststellung-drv-musikschule-gf-freelancer-klingenhain.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-statusfeststellung-drv-musikschule-gf-freelancer-klingenhain.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Technischer Plugin-Name: `kanzlei-allgemein`.

Eigenständiges großes Kanzlei-Plugin für den gesamten Arbeitszyklus einer Kanzlei. **Mit v11.0.0 wurden die Skills des früheren `kanzlei-cowork`-Plugins vollständig in `kanzlei-allgemein` integriert** — Fristenbuch, Timesheet, RVG-Rechnung, Versand-Vor-Check, beA-Versand-Prüfung, Posteingang/Postausgang, Mandantenakte, Aktenbestandspflege, Honorar-Mahnwesen, Mandantenbriefe, Geburtstage, Weihnachtskarten und Sekretariats-Tagesbrief.

Das Plugin deckt: edles Cowork-Kommandocenter, Nachtblau/Silber/Orange-Look, Eingang, Intake, freundliche Menüführung, Mandatsannahme, Geldwäscheprüfung, KYC, PEP-Check, Kontoblatt, Schreib-Canvas, Klage- und Replik-Turbo, Vertragsentwurf, Rechtsprechungsrecherche, Handelsregisterabruf, Qualitätsgate, Konfliktcheck, Aktenanlage, Fristen, Action-Items, beA-Nachrichtenjournal, elektronisches Empfangsbekenntnis, Kanzleikalender, HR, Urlaub, Krankheit, Payroll-Vorbereitung, granulare Zeiterfassung mit Narrative, Mandatsvereinbarung, Honorar, GoBD-nahe Rechnungsvorbereitung, Geschäftskonto, offene Posten, Zahlungseingangs-Matching, E-Rechnung, XRechnung, ZUGFeRD, UStVA-Vorbereitung, Simulation, Output und Versandkontrolle.

Es ist **nicht** auf Großkanzleien beschränkt. Der Name meint den großen Kanzlei-Workflow: vom ersten Eingang bis zum versandfertigen Ergebnis.

## Installation

1. ZIP herunterladen.
2. Claude Code oder Claude Desktop öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `kanzlei-allgemein.zip` hochladen.
5. In einer neuen Unterhaltung mit einem typischen Auftrag starten, etwa: "Starte das volle Kanzlei-Workflow-Plugin für diese neue Nachricht."

Wichtig: Nicht das komplette Repository-ZIP hochladen. Das Upload-ZIP muss direkt `.claude-plugin/plugin.json`, `skills/` und `assets/` im ZIP-Root enthalten; `references/` ist optional, falls ein Plugin Referenzen mitliefert.

#

## Was das Plugin abbildet

| Phase | Skill | Zweck |
| --- | --- | --- |
| Kommandocenter | `kanzlei-allgemein-kommandocenter` | Ein-Satz-Schnellstart, Workflow-Routing, Freigabeampel, nächste beste Aktion und nur die nötigsten Rückfragen |
| Look and Feel | `kanzlei-allgemein-look-and-feel` | Cowork-taugliches Designsystem mit Statuskarten, Dashboard, Freigabeampel und Nachtblau/Silber/Orange-Tonwelt |
| Kanzleiprofil | `kanzlei-allgemein-kaltstart` | Kanzleikonventionen, Aktenzeichen, Kanäle, Fristenlogik, Honorarstandard, Versandregeln |
| Freundlicher Copilot | `kanzlei-allgemein-freundlicher-copilot` | Verzeihende Menüführung, kurze Hinweise, Nachziehmodus, Substanzcheck für junge Anwältinnen und Anwälte |
| Integrationen | `kanzlei-allgemein-integrationen-simulation` | Word, Outlook, beA, Fax, Messenger, DMS, Fristenkalender, Buchhaltung prüfen, anschließen oder simulieren |
| Mandatsannahme/GwG | `kanzlei-allgemein-mandatsannahme-gwg` | Mandatsannahme, KYC, Kataloggeschäft, Identifizierung, wirtschaftlich Berechtigte, PEP, Verdachtsfall, Kontoblatt, Mandatsvereinbarung und BRAK-nahe Dokumentation |
| Schreib-Canvas | `kanzlei-allgemein-schreibcanvas` | Padlet-ähnliches Arbeitsbrett für Entwürfe, Tatsachen, Beweise, Anlagen, Fristen, Versand und Rechnung |
| Qualitätsgate | `kanzlei-allgemein-qualitaetsgate-hardening` | Schnellcheck, Normal- und Profi-Prüfung für Substanz, Beweise, Anlagen, Fristen, Versand, Vertrag und Rechnung |
| Schriftsatz-Turbo | `kanzlei-allgemein-schriftsatz-turbo` | Klage, Replik, Antrag oder Schriftsatzantwort samt Antrag, Sachverhalt, Beweisen, Anlagen und beA-Versand vorbereiten |
| Rechtsprechung | `kanzlei-allgemein-rechtsprechungsrecherche` | Amtliche Bundes- und Länderdatenbanken, OpenJur/dejure-Ergänzung, Fundstellenregister, Verwertungsnotiz und Akten-/Online-Ablage |
| Vertragsentwurf | `kanzlei-allgemein-vertragsentwurf` | Vertragsentwürfe aus Mandantenangaben, Term Sheet oder Vorlage mit Klauselstruktur, Risiken und Registercheck |
| Handelsregister | `kanzlei-allgemein-handelsregisterabruf` | Handelsregisterabruf über offizielle Registerquellen für Partei, Vertretung, Vertrag, Klage und Anlagenprotokoll |
| Eingang | `kanzlei-allgemein-intake` | Brief, Fax, beA, E-Mail, SMS, iMessage, WhatsApp, Telegram, Teams, Screenshot und sonstige Eingänge strukturieren |
| beA-Journal | `kanzlei-allgemein-bea-journal` | Nachrichtenjournal einsehen, Screenshot sichern, eingegangene und versandte beA-Nachrichten als ZIP archivieren, entpacken, EB-Workflow anbieten |
| Akte | `kanzlei-allgemein-akte` | Mandat anlegen, Konfliktcheck, Datenschutz, GwG, Mandatsumfang, Aktenstruktur |
| Aktenzeichen | `kanzlei-allgemein-aktenzeichen` | Eigene Aktenzeichen mit Gericht, Behörde, Gegner, Versicherung und Mandant verknüpfen |
| Fristen | `kanzlei-allgemein-fristen-monitor` | Fristen, Vorfristen, Action-Items und Wiedervorlagen aus Akteninhalt ableiten |
| Kanzleikalender | `kanzlei-allgemein-kanzleikalender` | Termine, Fristen, beA, Postlauf, Urlaub, Krankheit, Payroll, UStVA und Jour fixe zusammenführen |
| HR | `kanzlei-allgemein-hr-personal` | Mitarbeiterstamm, Arbeitsverträge, Onboarding, Offboarding, Rollen, Bonus, Gratifikation und interne Abstimmung |
| Abwesenheiten | `kanzlei-allgemein-abwesenheiten-urlaub` | Urlaub, Krankmeldungen, Fehlzeiten, Resturlaub, Vertretung und Kalenderkonflikte verwalten |
| Lohn/SV | `kanzlei-allgemein-lohn-sv` | Lohnabrechnung, Sozialversicherung, ELStAM, Lohnsteuer, Minijobs, Bonus und Gratifikation für Fachsysteme vorbereiten |
| Tagespost | `kanzlei-allgemein-postlauf` | Täglicher 11-Uhr-Postlauf mit Eingang, Fristen, Aufgaben, Versandbedarf |
| Zeit | `kanzlei-allgemein-zeitnarrative` | Stündliche Zeiterinnerung, Narrative und Aktenzuordnung |
| Mandatsvereinbarung | `kanzlei-allgemein-mandatsvereinbarung` | Mandatsvereinbarung, Haftungsbegrenzung, Honorarvereinbarung, Vollmacht |
| Output | `kanzlei-allgemein-output-versand` | Schriftsatz, Brief, E-Mail, Messenger, Fax, beA, Versandkontrolle |
| Rechnung | `kanzlei-allgemein-rechnung` | Rechnungsvorbereitung nach RVG oder Honorarvereinbarung, Auslagen, Timesheet, GoBD-Protokoll |
| Buchhaltung/Konten | `kanzlei-allgemein-buchhaltung-konten` | Geschäftskonto, offene Posten, Zahlungseingänge, Rechnungsalter, Bankmatching, Klärfälle, Mahnwesen und DATEV-ähnliche Übergabe |
| E-Rechnung | `kanzlei-allgemein-erechnung` | XRechnung als strukturiertes XML, ZUGFeRD als PDF/A-3 mit eingebettetem XML, Validierung und Archivierung |
| UStVA | `kanzlei-allgemein-ustva-buchhaltung` | Ausgangsrechnungen, Eingangsrechnungen, Betriebsausgaben, Vorsteuer, UStVA-Vorbereitung und ELSTER-Übergabe |
| UStVA-Simulation | `kanzlei-allgemein-ustva-simulation` | ELSTER-Ausfall oder fehlender Anschluss: Simulation, manueller Eingabebogen, XML-Upload-Prüfung oder Steuerberater-Paket |
| Simulation | `kanzlei-allgemein-kanzleitag-simulation` | Acht-Stunden-Kanzleitag beschleunigt oder in Echtzeit mit simulierten Integrationen durchspielen |
| Automationen | `kanzlei-allgemein-automationen` | Vorschläge für stündliche Zeiterinnerung, tägliche Postrunde und Ordner-Monitoring |

## Cowork-/Sekretariats-Skills (fusioniert aus `kanzlei-cowork`)

| Skill | Zweck |
| --- | --- |
| `aktenbestand-pflege` | Laufende Pflege des Aktenbestands — Aktualisierung Status (laufend/ruhend/abgeschlossen), Mandatsende mit Schlussrechnung, Archivierung nach Aufbewahrungspflicht |
| `bea-versand-pruefen` | Prüft den beA-Versand nach §§ 130a ZPO; 32d StPO; 65d SGG; 55a VwGO; 52d FGO sowie § 31a BRAO; sicherer Übermittlungsweg, qeS-Optionen, EB-Logik |
| `fristenbuch-fuehren` | Zentrales Fristenbuch mit Haupt- und Vorfristen, Berechnung nach ZPO/StPO/SGG/FGO/VwGO/FamFG/AO/BGB; Vier-Tages-Fiktion PostModG seit 1.1.2025 |
| `geburtstage-feiertage` | Mandanten- und Geschäftspartner-Geburtstagsverteiler, Firmenjubiläen, formell-warme Glückwunsch-Vorlagen |
| `kanzlei-cowork-kaltstart-interview` | Kaltstart-Interview für das Cowork-Profil der Kanzlei (Profil, Rechtsgebiete, Sekretariat, Aktenstruktur, beA-Profil, Versandregeln) |
| `mahnwesen-honorar` | Mahnwesen Honorarforderungen — Stufen Zahlungserinnerung, erste/zweite/dritte Mahnung nach § 286 BGB, Klagedrohung |
| `mandantenakte-anlegen` | Mandantenakte nach Kanzleikonvention — Stammdaten, Vollmacht, Mandatsumfang, Konflikt § 43a IV BRAO/§ 3 BORA, Art. 13 DSGVO, GwG-Identifizierung |
| `mandantenbrief-vorlagen` | Standardvorlagen Mandantenbrief — Anrede, Bezug, Sachstand, Empfehlung, nächste Schritte, Frist, Kostenhinweis, Berufsbezeichnung |
| `posteingang-ausgang` | Postein- und Postausgangsbuch — Empfangstag (Fristbeginn), Absender, Akte, Aktion; Versandbuch mit beA/Brief/Fax/E-Mail |
| `rechnungserstellung-rvg` | Honorarrechnungen nach RVG (Anlage 1 VV RVG, Anlage 2 Gebührentabelle) oder Honorarvereinbarung; Pflichtangaben § 10 RVG |
| `sekretariats-tagesbrief` | Tagesbrief mit Fristen heute und nächste Woche, Vorfristen, Posteingang Vortag, Wiedervorlagen, Termine, beA-Eingang |
| `timesheet-aktenzeitung` | Zeiterfassung pro Mandat (Aktenzeitung) in 6-Minuten-Blöcken, Abrechenbarkeit, Honorarsatz, Reports |
| `versand-vor-check` | Pflicht-Pre-Check vor Versand — Dokumentidentität, Unterschrift, Adressat, Anlagen, Versandweg, qeS bei beA |
| `weihnachtskarten` | Weihnachtskartenverteiler — postalisch oder digital, formell-zurückhaltend bis persönlich, Drucklisten |

## Sicherheitsleitplanken

Dieses Plugin ist eine Experimentier- und Arbeitsstruktur. Es ersetzt keine Kanzleisoftware, keinen Fristenkalender und keine anwaltliche Letztprüfung.

Besonders wichtig:

- **beA-Versand nur nach ausdrücklicher Einzelbestätigung.**
- **Bei beA-Connect Nachrichtenjournal einsehen, Screenshot sichern, jede eingegangene und versandte Nachricht als ZIP herunterladen oder exportieren, entpacken und ablegen.**
- **Elektronisches Empfangsbekenntnis nur nach ausdrücklicher Freigabe vorbereiten oder abgeben.**
- **Software-Token, PIN, Zertifikatsdateien und Passwörter nicht in Chat, Skill, Markdown, Log oder Akte speichern.**
- Wenn ein Nutzer trotzdem einen PIN oder Token im Chat nennt: nicht wiederholen, nicht protokollieren, Löschung oder Austausch empfehlen.
- Versand über beA, Fax, Messenger oder E-Mail immer mit Versandprotokoll und Verantwortlichem dokumentieren.
- Fristen nie nur vom Modell führen lassen. Das Plugin erzeugt Prüf- und Vorschlagslisten, die in einen berufsrechtlich geeigneten Fristenkalender übertragen und kontrolliert werden müssen.
- Mandatsannahme nie nur "gefühlt" durchführen. Konfliktcheck, GwG-Anwendbarkeit, Identifizierung, wirtschaftlich Berechtigte, PEP-/Hochrisiko-Prüfung, Honorar, Kontoblatt und Annahmeentscheidung müssen dokumentiert werden.
- Ausweiskopien, Registerauszüge, Transparenzregisterdaten und GwG-Vermerke nur geschützt ablegen. Keine Ausweisnummern, sensiblen Dokumente oder Verdachtsdetails unnötig in Chat, Logs oder ungeschützte Markdown-Dateien kopieren.
- Verdachtsmeldungen, goAML, Unstimmigkeitsmeldungen und Mandatsablehnungen werden nur vorbereitet und zur Berufsträger-Freigabe vorgelegt, nicht automatisch ausgelöst.
- Rechnungen nie automatisch finalisieren, versenden oder buchen. Das Plugin erzeugt Rechnungsdatenblatt, GoBD-Protokoll und E-Rechnungsdatenblatt; Freigabe, technische Validierung und Buchung bleiben beim Nutzer oder Fachsystem.
- Geschäftskonto und Buchhaltung nur nach Freigabe anbinden oder simulieren. Keine Bankzugangsdaten, TANs, PINs oder API-Secrets im Chat speichern. Zahlungsaufträge, endgültige Buchungen und DATEV-Übertragungen nicht still ausführen.
- XRechnung wird als strukturiertes XML behandelt. ZUGFeRD wird als PDF/A-3-Hybrid mit eingebettetem XML behandelt; PDF und XML müssen konsistent sein.
- UStVA wird nur vorbereitet oder simuliert. Elektronische Übermittlung, Steuerberatung, Buchung und Fristenkontrolle bleiben bei Nutzer, Steuerkanzlei oder Fachsystem.
- Für ELSTER gilt: Ein frei erzeugtes PDF oder Markdown-Dokument ist keine echte UStVA-Abgabe. Ein Eingabebogen kann bei manueller Online-Erfassung helfen; XML-Upload nur mit passendem, validiertem ELSTER/ERiC-Datensatz oder Fachsoftware.
- HR, Urlaub, Krankheit und Payroll enthalten sensible Beschäftigtendaten. Diagnosen nicht erfassen, Lohn- und SV-Meldungen nicht still übermitteln, Fachsystem- oder Steuerkanzlei-Übergabe klar markieren.
- Kanzleikalender ist ein Koordinationswerkzeug. Verbindliche Fristenkontrolle, Lohnabrechnung und Steueranmeldungen bleiben in den zuständigen Fachsystemen.
- Klage, Replik, Vertrag und Handelsregisterabruf laufen durch ein Qualitätsgate. Das Plugin darf Entwürfe beschleunigen, aber nicht ohne Freigabe versenden oder als gerichtsfertig garantieren.
- Rechtsprechungsrecherche bevorzugt amtliche Volltexte der Bundesgerichte und Länder. OpenJur und dejure.org sind Ergänzungsquellen; jede Fundstelle braucht Quelle, URL, Abrufdatum, Aktenzeichen/ECLI, Rn./Seite und Aktualitätscheck.
- Handelsregisterdaten aus offiziellen Quellen abrufen und mit Quelle, Zeitstempel und Dokumentart protokollieren.
- Wenn Word, Outlook, beA, Fax, Messenger, DMS, Fristenkalender oder Buchhaltung nicht angeschlossen sind, fragt das Plugin, ob angeschlossen oder simuliert werden soll.
- Der freundliche Copilot darf Hinweise geben, soll aber nicht nerven: kurz, konkret, verzeihend und mit Nachziehmodus.
- Mandatsgeheimnis, § 203 StGB, § 43e BRAO, DSGVO, BORA, Aufbewahrungspflichten und Beschlagnahmeschutz bleiben beim Nutzer.

## Vorschau: Startbild

```text
Kanzlei-Allgemein-Plugin gestartet

| Akte | Ampel | Frist | Nächste Aktion |
| --- | --- | --- | --- |
| offen | GELB | offen | Eingang einordnen und Workflow wählen |

Tonwelt: Nachtblau für Aktenarbeit, Silber für Ablage, Orange für Entscheidungen.

1. Kommandocenter: Ziel erkennen, Ampel setzen, nächste drei Schritte
2. Workflow starten: Mandatsannahme, Post, Klage, Replik, Vertrag, Rechnung oder Simulation
3. Freigabegrenzen zeigen: nicht versenden, nicht annehmen, nicht buchen, nicht melden
```

## Ordner und Vorlagen

Das Plugin bringt Markdown-Vorlagen mit:

- `assets/templates/mandatsblatt-vorlage.md`
- `assets/templates/cowork-designsystem.md`
- `assets/templates/cowork-dashboard.md`
- `assets/templates/cowork-statuskarte.md`
- `assets/templates/cowork-freigabekarte.md`
- `assets/templates/workflow-kommandocenter.md`
- `assets/templates/workflow-schnellstartkarte.md`
- `assets/templates/workflow-freigabeampel.md`
- `assets/templates/workflow-naechste-beste-aktion.md`
- `assets/templates/mandatsannahme-gwg-start.md`
- `assets/templates/gwg-anwendbarkeit-kataloggeschaeft.md`
- `assets/templates/gwg-identifizierung-und-dokumente.md`
- `assets/templates/gwg-risikobewertung-mandat.md`
- `assets/templates/gwg-pep-sanktionen-transparenzregister.md`
- `assets/templates/gwg-verdachtsfall-entscheidungsvermerk.md`
- `assets/templates/mandatskontoblatt.md`
- `assets/templates/mandatsvereinbarung-ki-datenschutz-hinweis.md`
- `assets/templates/freundlicher-copilot-hinweise.md`
- `assets/templates/schreibcanvas.md`
- `assets/templates/qualitaetsgate-checkliste.md`
- `assets/templates/schriftsatz-turbo-geruest.md`
- `assets/templates/klage-replik-pruefmatrix.md`
- `assets/templates/anlagenverzeichnis-schriftsatz.md`
- `assets/templates/rechtsprechungsrecherche-suchplan.md`
- `assets/templates/rechtsprechungsfundstellen-register.md`
- `assets/templates/rechtsprechungsablage-protokoll.md`
- `assets/templates/rechtsprechungsmonitor.md`
- `assets/templates/vertragsentwurf-playbook.md`
- `assets/templates/vertragsrisiken-matrix.md`
- `assets/templates/handelsregisterabruf-protokoll.md`
- `assets/templates/integrationsstatus-und-simulation.md`
- `assets/templates/kanzleitag-simulation.md`
- `assets/templates/bea-nachrichtenjournal.md`
- `assets/templates/fristen-und-action-register.md`
- `assets/templates/zeit-narrative-ledger.md`
- `assets/templates/rechnungsdatenblatt.md`
- `assets/templates/erechnung-datenblatt.md`
- `assets/templates/gobd-rechnungsprotokoll.md`
- `assets/templates/buchhaltung-kontoauszug.md`
- `assets/templates/offene-posten-debitoren.md`
- `assets/templates/zahlungseingang-matching.md`
- `assets/templates/mahn-und-klaerfallregister.md`
- `assets/templates/datev-uebergabe-simulation.md`
- `assets/templates/eingangsrechnungen-register.md`
- `assets/templates/ustva-vorbereitungsblatt.md`
- `assets/templates/ustva-elster-simulation.md`
- `assets/templates/ustva-elster-eingabebogen.md`
- `assets/templates/ustva-xml-upload-pruefung.md`
- `assets/templates/ustva-steuerberater-paket.md`
- `assets/templates/personalstammblatt.md`
- `assets/templates/hr-onboarding-offboarding.md`
- `assets/templates/lohnabrechnung-vorbereitung.md`
- `assets/templates/abwesenheiten-register.md`
- `assets/templates/kanzleikalender.md`
- `assets/templates/jour-fixe-protokoll.md`
- `assets/templates/postlauf-journal.md`
- `assets/templates/output-versandprotokoll.md`

Diese Dateien sind bewusst textbasiert, damit sie in jeder Umgebung lesbar sind. Wenn die Laufzeit echte Automationen, lokale Ordnerüberwachung oder Kalender-Connectoren unterstützt, nutzt der Skill diese nur nach ausdrücklicher Zustimmung.

## Empfohlene Begleitplugins

Das Plugin funktioniert allein. Für fachliche Ausarbeitung sind je nach Mandat zusätzlich hilfreich:

- `prozessrecht` für gerichtliche Schriftsätze und Fristenlogik.
- (Hinweis: Das frühere Plugin `kanzlei-cowork` ist seit v11.0.0 vollständig in dieses Plugin fusioniert. Externe Verweise auf `kanzlei-cowork` zeigen jetzt auf `kanzlei-allgemein`.)
- `zitierweise-deutsches-recht` und `methodenlehre-buergerliches-recht` für juristische Ausgabequalität.
- Rechtsgebietsplugins wie `arbeitsrecht`, `vertragsrecht`, `fachanwalt-sozialrecht`, `steuerrecht-anwalt-und-berater`, `insolvenzrecht`.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Das Plugin bildet Arbeitsabläufe und Sicherheitsgatter ab. Es ersetzt keine Fristenkontrolle durch Berufsträger, keine Kanzleisoftware und keine Prüfung der Zulässigkeit konkreter Kommunikation im Einzelfall.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 28 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Kanzlei Allgemein-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan.... |
| `kanzlei-allgemein-kaltstart` | Kaltstart des Kanzlei-Allgemein-Plugins und Erfassung des Kanzleiprofils. Anwendungsfall erstes Oeffnen des Plugins oder Kanzlei will Stammprofil neu einrichten. Abfrageraster Kanzleiprofil Aktenzeichen-Konvention Eingangskanale Integrat... |
| `kanzlei-allgemein-output-versand` | Steuert Output und Versand für Schriftsatz Brief E-Mail Fax beA SMS Messenger Teams und Mandantenportal. Fragt vor beA-Versand ausdrücklich nach Freigabe warnt vor PIN Token und Geheimnissen und dokumentiert Journal Screenshot ZIP-Archiv... |
| `kanzlei-cowork-kaltstart-interview` | Kaltstart-Interview für das generische Kanzlei-Cowork-Plugin. Erfragt Kanzleiprofil (Solo / Sozietaet / GmbH / Partnerschaft) Rechtsgebiete-Mix Sekretariat (vorhanden Stellen) Aktenstruktur-Konvention beA-Profil Versandwege Buchhaltungss... |
| `kompendium-01-kanzlei-allgemein-re-bis-fristenbuch-fuehren` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 01; bündelt 2 frühere Spezialskills (kanzlei-allgemein-rechtsprechungsrecherche, fristenbuch-fuehren) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-02-kanzlei-allgemein-fr-bis-kanzlei-allgemein-ve` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 02; bündelt 2 frühere Spezialskills (kanzlei-allgemein-fristen-monitor, kanzlei-allgemein-vertragsentwurf) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-03-kanzlei-allgemein-lo-bis-kanzlei-allgemein-re` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 03; bündelt 2 frühere Spezialskills (kanzlei-allgemein-lohn-sv, kanzlei-allgemein-rechnung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-04-kanzlei-allgemein-us-bis-kanzlei-allgemein-us` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 04; bündelt 2 frühere Spezialskills (kanzlei-allgemein-ustva-buchhaltung, kanzlei-allgemein-ustva-simulation) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-05-aktenbestand-pflege-bis-bea-versand-pruefen` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 05; bündelt 2 frühere Spezialskills (aktenbestand-pflege, bea-versand-pruefen) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-06-geburtstage-feiertag-bis-kanzlei-allgemein-ab` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 06; bündelt 2 frühere Spezialskills (geburtstage-feiertage, kanzlei-allgemein-abwesenheiten-urlaub) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-07-kanzlei-allgemein-ak-bis-kanzlei-allgemein-ak` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 07; bündelt 2 frühere Spezialskills (kanzlei-allgemein-akte, kanzlei-allgemein-aktenzeichen) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-08-kanzlei-allgemein-au-bis-kanzlei-allgemein-be` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 08; bündelt 2 frühere Spezialskills (kanzlei-allgemein-automationen, kanzlei-allgemein-bea-journal) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-09-kanzlei-allgemein-bu-bis-kanzlei-allgemein-er` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 09; bündelt 2 frühere Spezialskills (kanzlei-allgemein-buchhaltung-konten, kanzlei-allgemein-erechnung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-10-kanzlei-allgemein-fr-bis-kanzlei-allgemein-ha` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 10; bündelt 2 frühere Spezialskills (kanzlei-allgemein-freundlicher-copilot, kanzlei-allgemein-handelsregisterabruf) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-11-kanzlei-allgemein-hr-bis-kanzlei-allgemein-in` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 11; bündelt 2 frühere Spezialskills (kanzlei-allgemein-hr-personal, kanzlei-allgemein-intake) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-12-kanzlei-allgemein-in-bis-kanzlei-allgemein-ka` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 12; bündelt 2 frühere Spezialskills (kanzlei-allgemein-integrationen-simulation, kanzlei-allgemein-kanzleikalender) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-13-kanzlei-allgemein-ka-bis-kanzlei-allgemein-ko` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 13; bündelt 2 frühere Spezialskills (kanzlei-allgemein-kanzleitag-simulation, kanzlei-allgemein-kommandocenter) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-14-kanzlei-allgemein-lo-bis-kanzlei-allgemein-ma` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 14; bündelt 2 frühere Spezialskills (kanzlei-allgemein-look-and-feel, kanzlei-allgemein-mandatsannahme-gwg) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-15-kanzlei-allgemein-ma-bis-kanzlei-allgemein-po` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 15; bündelt 2 frühere Spezialskills (kanzlei-allgemein-mandatsvereinbarung, kanzlei-allgemein-postlauf) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-16-kanzlei-allgemein-qu-bis-kanzlei-allgemein-sc` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 16; bündelt 2 frühere Spezialskills (kanzlei-allgemein-qualitaetsgate-hardening, kanzlei-allgemein-schreibcanvas) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-17-kanzlei-allgemein-sc-bis-kanzlei-allgemein-ze` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 17; bündelt 2 frühere Spezialskills (kanzlei-allgemein-schriftsatz-turbo, kanzlei-allgemein-zeitnarrative) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-18-ki-arbeitsauftrag-br-bis-mahnwesen-honorar` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 18; bündelt 2 frühere Spezialskills (ki-arbeitsauftrag-briefing, mahnwesen-honorar) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-19-mandantenakte-anlege-bis-mandantenbrief-vorla` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 19; bündelt 2 frühere Spezialskills (mandantenakte-anlegen, mandantenbrief-vorlagen) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-20-posteingang-ausgang-bis-sekretariats-tagesbr` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 20; bündelt 2 frühere Spezialskills (posteingang-ausgang, sekretariats-tagesbrief) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-21-timesheet-aktenzeitu-bis-umgang-mit-ki-vorwur` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 21; bündelt 2 frühere Spezialskills (timesheet-aktenzeitung, umgang-mit-ki-vorwurf-bei-sachverstaendigengutachten) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-22-versand-vor-check-bis-weihnachtskarten` | kanzlei-allgemein: Konsolidiertes Skill-Kompendium 22; bündelt 2 frühere Spezialskills (versand-vor-check, weihnachtskarten) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `rechnungserstellung-rvg` | Erstellt Honorarrechnungen nach RVG (Anlage 1 VV RVG Anlage 2 RVG Gebührentabelle) oder nach Honorarvereinbarung mit Stundensatz. Pflichtangaben § 10 RVG (Aktenzeichen Mandant Gegenstand der Tätigkeit Verguetungstatbestaende Stundensaetz... |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin kanzlei-allgemein: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
