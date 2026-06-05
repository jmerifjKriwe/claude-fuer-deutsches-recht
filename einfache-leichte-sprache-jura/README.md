# Einfache und Leichte Sprache für juristische Texte

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`einfache-leichte-sprache-jura`) | [`einfache-leichte-sprache-jura.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/einfache-leichte-sprache-jura.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Juristischer Mandantenbrief in Einfacher und Leichter Sprache** (`einfache-leichte-sprache-jura-mandantenbrief`) | [Gesamt-PDF lesen](../testakten/einfache-leichte-sprache-jura-mandantenbrief/gesamt-pdf/einfache-leichte-sprache-jura-mandantenbrief_gesamt.pdf) | [`testakte-einfache-leichte-sprache-jura-mandantenbrief.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-einfache-leichte-sprache-jura-mandantenbrief.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Plugin für die Übertragung juristischer Texte in **Einfache
Sprache** oder **Leichte Sprache**. Es richtet sich an Kanzleien, Behörden,
Beratungsstellen, Legal-Design-Teams und alle, die rechtliche Informationen
verständlich, respektvoll und rechtlich belastbar erklären müssen.

## Showcase-Hinweis

Dieses Plugin ist ein Experiment und ein Showcase. Es ist ein Versuch, sich der
Ergebnisrichtung von Einfacher Sprache und Leichter Sprache anzunähern, ohne
eine Standardprüfung oder Konformitätsaussage zu behaupten. Make of this what
you will, dear users: Ihr müsst selbst beurteilen, ob Verfahren, Sprache und
Ergebnis für eure Zielgruppe, euer Medium und euren Rechtstext passen. You are
on your own.

## Zwei Modi

| Modus | Ziel |
| --- | --- |
| Einfache Sprache | Standardsprache bleibt erkennbar. Fachsprache wird erklärt. Der Text wird klarer, kürzer, besser gegliedert und zielgruppenorientiert. |
| Leichte Sprache | Deutlich stärkere Vereinfachung. Kurze Sätze, klare Zeilen, viel Orientierung, erklärtes Fachwort, möglichst eine Aussage pro Satz. Eine Prüfung durch Personen aus der Zielgruppe wird empfohlen. |

## Workflow

1. Ausgangstext hochladen oder einfügen.
2. Zielgruppe, Anlass, Medium und gewünschte Tiefe klären.
3. Juristische Bedeutungen sichern: Rechte, Pflichten, Fristen, Beträge,
   Rechtsfolgen, Zuständigkeiten und Handlungsoptionen.
4. Modus wählen: Einfache Sprache oder Leichte Sprache.
5. Übertragung erstellen.
6. Glossar und Warnhinweise ergänzen.
7. Qualitätsgate laufen lassen.
8. Bei Leichter Sprache: Nutzerprüfung als offenen Schritt markieren, wenn sie
   nicht tatsächlich erfolgt ist.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `elsj-kommandocenter` | steuert Intake, Moduswahl, Zielgruppe, Rechtsinhalt und Ausgabeformat |
| `elsj-einfache-sprache` | überträgt juristische Texte in Einfache Sprache |
| `elsj-leichte-sprache` | überträgt juristische Texte in Leichte Sprache |
| `elsj-juristische-sicherung` | verhindert Bedeutungsverlust bei Rechten, Pflichten, Fristen und Rechtsfolgen |
| `elsj-qualitaetsgate` | prüft Verständlichkeit, Struktur, Glossar, Ton und rechtliche Vollständigkeit |

## Hilfsskript

```bash
python einfache-leichte-sprache-jura/scripts/verstaendlichkeitscheck.py \
  testakten/einfache-leichte-sprache-jura-mandantenbrief/02_einfache_sprache.md \
  --mode einfache
```

Das Skript ist kein Normprüfer. Es findet typische Warnsignale:
lange Sätze, sehr lange Wörter, Passiv-Kandidaten, Nominalstil und fehlende
Orientierungselemente.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 70 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Einfache Leichte Sprache Jura-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren A... |
| `allgemein-ls-bescheid-workflow-chronologie` | Nutze dies, wenn Allgemein, Ls Bescheid Uebersetzen Workflow, Workflow Chronologie Und Belegmatrix im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Allgemein, Ls Bescheid Uebersetzen Workflow, Workf... |
| `annaeherung-quellenkarte` | Nutze dies, wenn Annaeherung Quellenkarte im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Welche amtliche Quelle prüfe ich zuerst?; Gibt es aktuelle Rechtsprechung?; Bitte Fundstellen verifizieren.. |
| `anschluss-routing` | Nutze dies, wenn Anschluss-Routing im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Ich habe ein neues Thema im Bereich Einfache Leichte Sprache Jura.; Welche Unterlagen brauchen Sie?; Welcher Spezialskil... |
| `bauen-fristennotiz-naechster-schritt` | Nutze dies, wenn Bauen: Fristennotiz und nächster Schritt im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Bauen: Fristennotiz und nächster Schritt prüfen.; Erstelle eine Arbeitsfassung zu Bauen: Fr... |
| `chronologie-und-belegmatrix` | Nutze dies, wenn Chronologie und Belegmatrix im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Chronologie und Belegmatrix prüfen.; Erstelle eine Arbeitsfassung zu Chronologie und Belegmatrix.; Welch... |
| `dokumente-intake` | Nutze dies, wenn Dokumentenintake im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Ich lade Unterlagen hoch.; Was fehlt noch?; Bitte Dokumente sortieren.. |
| `einfache` | Nutze dies, wenn Einfache: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Einfache: Fristen, Form, Zuständigkeit und Rechtsweg prüfen.; Erstelle eine Arb... |
| `einfache-elsj-bescheidmodus-elsj` | Nutze dies, wenn Spezial Einfache Fristen Form Und Zustaendigkeit, Elsj Bescheidmodus, Elsj Kommandocenter im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Spezial Einfache Fristen Form Und Zustaend... |
| `einstieg-routing` | Nutze dies, wenn Einstieg und Routing im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Ich habe ein neues Thema im Bereich Einfache Leichte Sprache Jura.; Welche Unterlagen brauchen Sie?; Welcher Spezials... |
| `elsj-aufenthaltsrecht-mandant` | Aufenthaltsrechtliche Mandantenkommunikation: AufenthG, Asyl, Familiennachzug. Anschreiben Auslaenderbehoerde Begleitschreiben fuer Mandanten. Vorlage Bescheid-Erklaerung. |
| `elsj-aufenthaltsrecht-mandant-betreuung` | Nutze dies, wenn Elsj Aufenthaltsrecht Mandant, Elsj Betreuung Vormundschaft, Elsj Einfache Sprache im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Elsj Aufenthaltsrecht Mandant, Elsj Betreuung Vor... |
| `elsj-bescheidmodus` | Bescheide einfach erlaeutern: typische Bescheide (Bafoeg, Wohngeld, Arbeitsamt-Eingliederungsmassnahme, Steuerbescheid). Vorlage Adressaten-Erklaerung mit 'Was sagt der Bescheid? Was muessen Sie tun? Bis wann? Was passiert sonst?'. |
| `elsj-betreuung-vormundschaft` | Mandanten in Betreuung oder Vormundschaft: spezifische Regeln BGB §§ 1814 ff., Beruecksichtigung Wuensche § 1821, Genehmigungspflichten. Sprache muss die Person selbst erreichen. Vorlage Anschreiben Betreuter. |
| `elsj-einfache-sprache` | Kanzlei oder Behoerde will juristischen Text für normale Buerger verstaendlich machen: Einfache Sprache B1-Niveau zielgruppenorientiert klare Gliederung erklärte Rechtsbegriffe gesicherte Fristen. Normen BGG § 11 Leichte Sprache Behinder... |
| `elsj-familienrecht-erstgespraech` | Familienrecht Erstgespraech in Einfacher Sprache: Trennung, Scheidung, Unterhalt, Sorgerecht, Umgang. Vorlage Memo fuer den Mandanten: 'Was muessen Sie wissen, was muessen Sie entscheiden?' Sprachlich barrierearm. |
| `elsj-familienrecht-erstgespraech-juristische` | Nutze dies, wenn Elsj Familienrecht Erstgespraech, Elsj Juristische Sicherung, Elsj Kommunikation Mandant im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Elsj Familienrecht Erstgespraech, Elsj Juri... |
| `elsj-juristische-sicherung` | Beim Vereinfachen juristischer Texte darf kein Rechtsinhalt verloren gehen: Rechte Pflichten Fristen Betraege Rechtsfolgen Ausnahmen. Normen §§ 133 157 BGB Auslegungspflicht. Prüfraster Rechte-Vollständigkeit Pflichten-Sicherung Fristen-... |
| `elsj-kommandocenter` | Kanzlei oder Behoerde startet Vereinfachungs-Projekt für juristischen Text: Zielgruppe Modus Rechtsinhalt-Erfassung Workflow-Steuerung Ausgabe. Normen BGG BITV 2.0. Prüfraster Zielgruppen-Identifikation Modus-Auswahl Skill-Routing Qualit... |
| `elsj-kommunikation-mandant` | Mandantenkommunikation in Einfacher Sprache: Telefon-Leitfaden, E-Mail-Templates, schriftliche Information ueber das Verfahren. Pruefliste: Verstehen Sie das? Brauchen Sie eine Wiederholung? Notizen fuer den naechsten Termin. |
| `elsj-leichte-sprache` | Kanzlei oder Behoerde will juristischen Text für Menschen mit Lernschwierigkeiten oder kognitiven Einschraenkungen aufbereiten: Leichte Sprache nach Netzwerk Leichte Sprache A2-Niveau kurze Saetze klare Zeilenstruktur erklärte Woerter. N... |
| `elsj-leichte-sprache-mietrecht` | Nutze dies, wenn Elsj Leichte Sprache, Elsj Mietrecht Kuendigungserklaerung, Elsj Pruefkriterien Für Qualitaet im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Elsj Leichte Sprache, Elsj Mietrecht K... |
| `elsj-mietrecht-kuendigungserklaerung` | Wohnungsmietrecht in einfacher Sprache fuer Mieter: Kuendigung erklaert (Frist, Form, Schriftform § 568 BGB), Schonfristzahlung § 569 Abs. 3 BGB, Mieterhoehung, Betriebskostenabrechnung. Mandantenformularsatz. |
| `elsj-pruefkriterien-fuer-qualitaet` | Qualitaetspruefung Einfache/Leichte Sprache: Pruefliste mit Wortlaenge, Satzlaenge, Verbquote, Fremdwortquote, Anteil Aktiv-/Passivsaetze. Empfehlung Tools (LIX-Index, Hohenheimer Verstaendlichkeitsindex). |
| `elsj-qualitaetsgate` | Fertig erstellte Fassung in Einfacher Sprache oder Leichter Sprache vor Veröffentlichung prüfen. Verstaendlichkeit Gliederung Glossar Zielgruppenpassung juristische Vollständigkeit offene Nutzergruppen-Prüfung. Normen BITV 2.0 BGG § 11 N... |
| `elsj-qualitaetsgate-rechtsnormen-einfach` | Nutze dies, wenn Elsj Qualitaetsgate, Elsj Rechtsnormen Einfach, Elsj Satzbau Regeln im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.; Welche Frist oder... |
| `elsj-rechtsnormen-einfach` | Rechtsnormen in Einfacher/Leichter Sprache wiedergeben: § 17 InsO wird zu 'Eine Firma muss Insolvenz anmelden, wenn sie ihre Rechnungen nicht mehr bezahlen kann. Das gilt drei Wochen nach dem Tag, an dem klar wurde, dass kein Geld da ist... |
| `elsj-satzbau-regeln` | Satzbau-Regeln: maximal ein Komma pro Satz in Einfacher Sprache, ueberhaupt keine Kommata in Leichter Sprache, kurze Saetze, aktive Formulierung, Subjekt vor Praedikat. Vermeidung Passiv, Substantivketten, Genitiv. |
| `elsj-sozialgerichtsverfahren` | Sozialgerichtsverfahren in Einfacher Sprache: Klageeinreichung Niederschrift § 90 SGG, kein Anwaltszwang, ehrenamtliche Richter. Vorlage Mandanteninformation 'Was passiert vor dem Sozialgericht'. |
| `elsj-sozialgerichtsverfahren-strafverfahren` | Nutze dies, wenn Elsj Sozialgerichtsverfahren, Elsj Strafverfahren Beschuldigter, Spezial Bauen Fristennotiz Und Naechster Schritt im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Elsj Sozialgericht... |
| `elsj-strafverfahren-beschuldigter` | Strafverfahren in Einfacher Sprache fuer Beschuldigte: Belehrung § 136 StPO, Rechte des Beschuldigten, Akteneinsicht, Wahlverteidiger/Pflichtverteidiger. Pflichtbelehrung in einfacher Sprache (BVerfG 2 BvR 1568/19). |
| `elsj-uebersetzungsablauf` | Standardablauf Uebersetzung: 1. Original lesen, 2. Kernaussage extrahieren, 3. Satz fuer Satz uebertragen, 4. Pruefen gegen Pruefliste, 5. mit Zielgruppe gegenpruefen. Empfehlung: parallele Textspalten Original/Uebersetzung. |
| `elsj-uebersetzungsablauf-wortebene-haus` | Nutze dies, wenn Elsj Uebersetzungsablauf, Elsj Wortebene Haus Glossar, Elsj Zielgruppen Erkennen im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Elsj Uebersetzungsablauf, Elsj Wortebene Haus Gloss... |
| `elsj-wortebene-haus-glossar` | Hauseigenes Glossar: typische juristische Begriffe und deren Uebersetzungen. Beispiele: 'Beklagter' = 'die Person, gegen die geklagt wird'; 'Frist' = 'Zeitraum, in dem etwas getan werden muss'. Aufnahme in Kanzlei-Wiki. |
| `elsj-zielgruppen-erkennen` | Zielgruppen erkennen: Einfache Sprache fuer geringe Lesekompetenz (B1), Leichte Sprache fuer Menschen mit Lernschwierigkeiten oder geringer Deutsch-Kenntnis. Wahl der richtigen Stufe pro Mandant/Adressat. Pruefraster und Beispiele. |
| `experimentelle` | Nutze dies, wenn Experimentelle: Schriftsatz-, Brief- und Memo-Bausteine im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Experimentelle: Schriftsatz-, Brief- und Memo-Bausteine prüfen.; Erstelle ei... |
| `experimentelle-glossar-sonderfall-jura` | Nutze dies, wenn Spezial Experimentelle Schriftsatz Brief Und Memo Bausteine, Spezial Glossar Sonderfall Und Edge Case, Spezial Jura Mandantenkommunikation Entscheidungsvorlage im Plugin Einfache Leichte Sprache Jura konkret bearbeitet w... |
| `fristen-risikoampel-mandantenkommunikation` | Nutze dies, wenn Workflow Fristen Und Risikoampel, Workflow Mandantenkommunikation, Workflow Redteam Qualitygate im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team... |
| `fristen-und-risikoampel` | Nutze dies, wenn Fristen- und Risikoampel im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Fristen- und Risikoampel prüfen.; Erstelle eine Arbeitsfassung zu Fristen- und Risikoampel.; Welche Normen... |
| `glossar-sonderfall-edge-case` | Nutze dies, wenn Glossar: Sonderfall und Edge-Case-Prüfung im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Glossar: Sonderfall und Edge-Case-Prüfung prüfen.; Erstelle eine Arbeitsfassung zu Glossar... |
| `jura` | Nutze dies, wenn Jura: Mandantenkommunikation und Entscheidungsvorlage im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Jura: Mandantenkommunikation und Entscheidungsvorlage prüfen.; Erstelle eine A... |
| `juristische` | Nutze dies, wenn Juristische: Erstprüfung, Rollenklärung und Mandatsziel im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Juristische: Erstprüfung, Rollenklärung und Mandatsziel prüfen.; Erstelle ei... |
| `juristische-juristisches-beweislast-klaeren` | Nutze dies, wenn Spezial Juristische Erstpruefung Und Mandatsziel, Spezial Juristisches Beweislast Und Darlegungslast, Spezial Klaeren Compliance Dokumentation Und Akte im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden so... |
| `juristisches-beweislast-darlegungslast` | Nutze dies, wenn Juristisches: Beweislast, Darlegungslast und Substantiierung im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Juristisches: Beweislast, Darlegungslast und Substantiierung prüfen.; E... |
| `klaeren` | Nutze dies, wenn Klaeren: Compliance-Dokumentation und Aktenvermerk im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Ich lade Unterlagen hoch.; Was fehlt noch?; Bitte Dokumente sortieren.. |
| `leichte` | Nutze dies, wenn Leichte: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Leichte: Risikoampel, Gegenargumente und Verteidigungslinien prüfen.; E... |
| `leichte-qualitaetsgate-rechtsinhalt` | Nutze dies, wenn Spezial Leichte Risikoampel Und Gegenargumente, Spezial Qualitaetsgate Formular Portal Und Einreichung, Spezial Rechtsinhalt Mehrparteien Konflikt Und Interessen im Plugin Einfache Leichte Sprache Jura konkret bearbeitet... |
| `ls-bescheid-uebersetzen-workflow` | Bescheid in Leichte Sprache uebersetzen Workflow: Originalbescheid, Kernaussagen extrahieren, je Aussage 1 kurzer Satz, Pruefung mit Zielgruppen-Vertreter, Layout (Bilder, Schriftgroesse), Pruefsiegel. Routet in einfache-leichte-sprache-... |
| `ls-juristisches-glossar-bauen` | Juristisches Glossar fuer Einfache und Leichte Sprache aufbauen: Schlagwort, Schwerverstaendliche Definition, Variante Einfache Sprache, Variante Leichte Sprache. Pro Eintrag Beispielssatz. Strukturierter CSV-Output und Mustertext fuer 3... |
| `ls-juristisches-ls-justizportal-ls` | Nutze dies, wenn Ls Juristisches Glossar Bauen, Ls Justizportal Prüfen Spezial, Ls Strafprozess Rechte Erklaeren Spezial im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Ls Juristisches Glossar Baue... |
| `ls-justizportal-pruefen-spezial` | Spezialfall Justizportal in Leichte Sprache pruefen: Bayerisches Justizportal, JustizOnline, beA-Frontend. Konkrete Verbesserungsvorschlaege fuer Navigation, Wegleitsysteme, Antragsformulare. Pruefraster nach Inclusion Europe Regeln. |
| `ls-strafprozess-rechte-erklaeren-spezial` | Spezialfall Strafprozess-Rechte in Leichte Sprache erklaeren: § 136 StPO Belehrung, Recht zur Aussage und zum Schweigen, Pflichtverteidiger, Akteneinsicht. Mustertext und Pruefsiegel. Bedeutung fuer JVA-Insassen und Migrantinnen. |
| `mandantenkommunikation` | Nutze dies, wenn Mandantenkommunikation im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Mandantenkommunikation prüfen.; Erstelle eine Arbeitsfassung zu Mandantenkommunikation.; Welche Normen und Na... |
| `nutzen-fehlerkatalog` | Nutze dies, wenn Nutzen Fehlerkatalog im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.; Welche Frist oder Beweislast übersehe ich?. |
| `output-waehlen` | Nutze dies, wenn Output wählen im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Output wählen prüfen.; Erstelle eine Arbeitsfassung zu Output wählen.; Welche Normen und Nachweise brauche ich?. |
| `qualitaetsgate` | Nutze dies, wenn Qualitaetsgate: Formular, Portal und Einreichungslogik im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.; Welche Frist oder Beweislast üb... |
| `quellen-livecheck` | Nutze dies, wenn Rechtsquellen-Livecheck im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Welche amtliche Quelle prüfe ich zuerst?; Gibt es aktuelle Rechtsprechung?; Bitte Fundstellen verifizieren.. |
| `rechtsinhalt-interessen` | Nutze dies, wenn Rechtsinhalt: Mehrparteienkonflikt und Interessenmatrix im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Rechtsinhalt: Mehrparteienkonflikt und Interessenmatrix prüfen.; Erstelle ei... |
| `redteam-qualitygate` | Nutze dies, wenn Red-Team Qualitygate im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.; Welche Frist oder Beweislast übersehe ich?. |
| `sichern` | Nutze dies, wenn Sichern: Internationaler Bezug und Schnittstellen im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Sichern: Internationaler Bezug und Schnittstellen prüfen.; Erstelle eine Arbeitsfa... |
| `sichern-sprache-standard` | Nutze dies, wenn Spezial Sichern Internationaler Bezug Und Schnittstellen, Spezial Sprache Dokumentenmatrix Und Lueckenliste, Spezial Standard Verhandlung Vergleich Und Eskalation im Plugin Einfache Leichte Sprache Jura konkret bearbeite... |
| `sprache` | Nutze dies, wenn Sprache: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Ich lade Unterlagen hoch.; Was fehlt noch?; Bitte Dokumente sortieren.. |
| `standard` | Nutze dies, wenn Standard: Verhandlung, Vergleich und Eskalation im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Standard: Verhandlung, Vergleich und Eskalation prüfen.; Erstelle eine Arbeitsfassun... |
| `texte` | Nutze dies, wenn Texte: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Texte: Tatbestandsmerkmale, Beweisfragen und Beleglage prüfen.; Erstelle eine... |
| `texte-uebertragen-zielgruppe-sprachniveau` | Nutze dies, wenn Spezial Texte Tatbestand Beweis Und Belege, Spezial Uebertragen Behörden Gericht Und Registerweg, Spezial Zielgruppe Sprachniveau Rechtsinhalt im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslö... |
| `uebertragen` | Nutze dies, wenn Uebertragen: Behörden-, Gerichts- oder Registerweg im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Uebertragen: Behörden-, Gerichts- oder Registerweg prüfen.; Erstelle eine Arbeits... |
| `unterlagen-luecken` | Nutze dies, wenn Unterlagen und Lücken im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Ich lade Unterlagen hoch.; Was fehlt noch?; Bitte Dokumente sortieren.. |
| `zielgruppe` | Nutze dies, wenn Spezial Zielgruppe Zahlen Schwellen Und Berechnung im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Spezial Zielgruppe Zahlen Schwellen Und Berechnung prüfen.; Erstelle eine Arbeits... |
| `zielgruppe-02` | Nutze dies, wenn Zielgruppe: Zahlen, Schwellenwerte und Berechnung im Plugin Einfache Leichte Sprache Jura konkret bearbeitet werden soll. Auslöser: Bitte Zielgruppe: Zahlen, Schwellenwerte und Berechnung prüfen.; Erstelle eine Arbeitsfa... |
| `zielgruppe-sprachniveau-rechtsinhalt` | Zielgruppe, Sprachniveau und gesicherter Rechtsinhalt: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
