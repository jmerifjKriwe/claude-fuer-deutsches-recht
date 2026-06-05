# Einfache und Leichte Sprache für juristische Texte

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`einfache-leichte-sprache-jura`) | [`einfache-leichte-sprache-jura.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/einfache-leichte-sprache-jura.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

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
| `annaeherung-quellenkarte` | Annaeherung Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `bauen-fristennotiz-naechster-schritt` | Bauen: Fristennotiz und nächster Schritt im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung,... |
| `einfache-leichte-experimentelle-schriftsatz-brief-memo-bausteine` | Experimentelle: Schriftsatz-, Brief- und Memo-Bausteine im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Fri... |
| `einfache-leichte-jura-mandantenkommunikation` | Jura: Mandantenkommunikation und Entscheidungsvorlage im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist... |
| `einfache-leichte-juristische-erstpruefung-rollenklaerung` | Juristische: Erstprüfung, Rollenklärung und Mandatsziel im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Fri... |
| `einfache-leichte-klaeren-compliance-dokumentation-aktenvermerk` | Klaeren: Compliance-Dokumentation und Aktenvermerk im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Z... |
| `einfache-leichte-ls-juristisches-glossar-justizportal-pruefen` | LS Juristisches Glossar Justizportal Pruefen im Einfache und leichte Sprache im Recht: prüft konkret Juristisches Glossar fuer Einfache und Leichte Sprache, Spezialfall Justizportal in Leichte Sprache pruefen, Spezialfall Strafprozess-Re... |
| `einfache-leichte-sichern-internationaler-bezug-schnittstellen` | Sichern: Internationaler Bezug und Schnittstellen im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zu... |
| `einfache-leichte-sprache-dokumentenmatrix-lueckenliste` | Sprache: Dokumentenmatrix, Lückenliste und Nachforderung im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Fr... |
| `einfache-leichte-sprache-jura-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `einfache-leichte-sprache-jura-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Einfache und leichte Sprache im Recht: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten od... |
| `einfache-leichte-sprache-jura-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `einfache-leichte-sprache-jura-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `einfache-leichte-sprache-jura-fristen-und-risikoampel` | Fristen- und Risikoampel im Einfache und leichte Sprache im Recht: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder... |
| `einfache-leichte-sprache-jura-kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im Einfache Leichte Sprache Jura-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitspla... |
| `einfache-leichte-sprache-jura-mandantenkommunikation` | Mandantenkommunikation im Einfache und leichte Sprache im Recht: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Be... |
| `einfache-leichte-sprache-jura-output-waehlen` | Output wählen im Einfache und leichte Sprache im Recht: Diese Output-Weiche für Einfache Leichte Sprache Jura entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `einfache-leichte-sprache-jura-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `einfache-leichte-sprache-jura-redteam-qualitygate` | Red-Team Qualitygate: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `einfache-leichte-sprache-jura-standard` | Standard: Verhandlung, Vergleich und Eskalation im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zust... |
| `einfache-leichte-sprache-jura-texte` | Texte: Tatbestandsmerkmale, Beweisfragen und Beleglage im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Fris... |
| `einfache-leichte-sprache-jura-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `einfache-leichte-uebertragen-behoerden-gerichts-registerweg` | Uebertragen: Behörden-, Gerichts- oder Registerweg im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Z... |
| `einfache-leichte-zielgruppe-zahlen-schwellenwerte-berechnung` | Zielgruppe: Zahlen, Schwellenwerte und Berechnung im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zu... |
| `elsj-aufenthaltsrecht-mandant` | Aufenthaltsrechtliche Mandantenkommunikation: AufenthG, Asyl, Familiennachzug. Anschreiben Auslaenderbehoerde Begleitschreiben fuer Mandanten. Vorlage Bescheid-Erklaerung. |
| `elsj-aufenthaltsrecht-mandant-betreuung` | Elsj Aufenthaltsrecht Mandant Betreuung im Einfache und leichte Sprache im Recht: prüft konkret Aufenthaltsrechtliche Mandantenkommunikation, Mandanten in Betreuung oder Vormundschaft, Kanzlei oder Behoerde will juristischen Text für nor... |
| `elsj-bescheidmodus` | Bescheide einfach erlaeutern: typische Bescheide (Bafoeg, Wohngeld, Arbeitsamt-Eingliederungsmassnahme, Steuerbescheid). Vorlage Adressaten-Erklaerung mit 'Was sagt der Bescheid? Was muessen Sie tun? Bis wann? Was passiert sonst?'. |
| `elsj-bescheidmodus-02` | Elsj Bescheidmodus 02 im Einfache und leichte Sprache im Recht: prüft konkret Einfache, Bescheide einfach erlaeutern, Kanzlei oder Behoerde startet Vereinfachungs-Projekt für. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel... |
| `elsj-betreuung-vormundschaft` | Mandanten in Betreuung oder Vormundschaft: spezifische Regeln BGB §§ 1814 ff., Beruecksichtigung Wuensche § 1821, Genehmigungspflichten. Sprache muss die Person selbst erreichen. Vorlage Anschreiben Betreuter. |
| `elsj-einfache-sprache` | Kanzlei oder Behoerde will juristischen Text für normale Buerger verstaendlich machen: Einfache Sprache B1-Niveau zielgruppenorientiert klare Gliederung erklärte Rechtsbegriffe gesicherte Fristen. Normen BGG § 11 Leichte Sprache Behinder... |
| `elsj-familienrecht-erstgespraech` | Familienrecht Erstgespraech in Einfacher Sprache: Trennung, Scheidung, Unterhalt, Sorgerecht, Umgang. Vorlage Memo fuer den Mandanten: 'Was muessen Sie wissen, was muessen Sie entscheiden?' Sprachlich barrierearm. |
| `elsj-familienrecht-erstgespraech-juristische` | Elsj Familienrecht Erstgespraech Juristische im Einfache und leichte Sprache im Recht: prüft konkret Familienrecht Erstgespraech in Einfacher Sprache, Beim Vereinfachen juristischer Texte darf kein Rechtsinhalt, Mandantenkommunikation in... |
| `elsj-juristische-sicherung` | Beim Vereinfachen juristischer Texte darf kein Rechtsinhalt verloren gehen: Rechte Pflichten Fristen Betraege Rechtsfolgen Ausnahmen. Normen §§ 133 157 BGB Auslegungspflicht. Prüfraster Rechte-Vollständigkeit Pflichten-Sicherung Fristen-... |
| `elsj-kommandocenter` | Kanzlei oder Behoerde startet Vereinfachungs-Projekt für juristischen Text: Zielgruppe Modus Rechtsinhalt-Erfassung Workflow-Steuerung Ausgabe. Normen BGG BITV 2.0. Prüfraster Zielgruppen-Identifikation Modus-Auswahl Skill-Routing Qualit... |
| `elsj-kommunikation-mandant` | Mandantenkommunikation in Einfacher Sprache: Telefon-Leitfaden, E-Mail-Templates, schriftliche Information ueber das Verfahren. Pruefliste: Verstehen Sie das? Brauchen Sie eine Wiederholung? Notizen fuer den naechsten Termin. |
| `elsj-leichte-sprache` | Kanzlei oder Behoerde will juristischen Text für Menschen mit Lernschwierigkeiten oder kognitiven Einschraenkungen aufbereiten: Leichte Sprache nach Netzwerk Leichte Sprache A2-Niveau kurze Saetze klare Zeilenstruktur erklärte Woerter. N... |
| `elsj-leichte-sprache-mietrecht` | Elsj Leichte Sprache Mietrecht im Einfache und leichte Sprache im Recht: prüft konkret Kanzlei oder Behoerde will juristischen Text für Menschen, Wohnungsmietrecht in einfacher Sprache fuer Mieter, Qualitaetspruefung Einfache/Leichte Spr... |
| `elsj-mietrecht-kuendigungserklaerung` | Wohnungsmietrecht in einfacher Sprache fuer Mieter: Kuendigung erklaert (Frist, Form, Schriftform § 568 BGB), Schonfristzahlung § 569 Abs. 3 BGB, Mieterhoehung, Betriebskostenabrechnung. Mandantenformularsatz. |
| `elsj-pruefkriterien-fuer-qualitaet` | Qualitaetspruefung Einfache/Leichte Sprache: Pruefliste mit Wortlaenge, Satzlaenge, Verbquote, Fremdwortquote, Anteil Aktiv-/Passivsaetze. Empfehlung Tools (LIX-Index, Hohenheimer Verstaendlichkeitsindex). |
| `elsj-qualitaetsgate` | Fertig erstellte Fassung in Einfacher Sprache oder Leichter Sprache vor Veröffentlichung prüfen. Verstaendlichkeit Gliederung Glossar Zielgruppenpassung juristische Vollständigkeit offene Nutzergruppen-Prüfung. Normen BITV 2.0 BGG § 11 N... |
| `elsj-qualitaetsgate-rechtsnormen-einfach` | Elsj Qualitaetsgate Rechtsnormen Einfach im Einfache und leichte Sprache im Recht: prüft konkret Fertig erstellte Fassung in Einfacher Sprache oder Leichter, Rechtsnormen in Einfacher/Leichter Sprache wiedergeben, Satzbau-Regeln. Liefert... |
| `elsj-rechtsnormen-einfach` | Rechtsnormen in Einfacher/Leichter Sprache wiedergeben: § 17 InsO wird zu 'Eine Firma muss Insolvenz anmelden, wenn sie ihre Rechnungen nicht mehr bezahlen kann. Das gilt drei Wochen nach dem Tag, an dem klar wurde, dass kein Geld da ist... |
| `elsj-satzbau-regeln` | Satzbau-Regeln: maximal ein Komma pro Satz in Einfacher Sprache, ueberhaupt keine Kommata in Leichter Sprache, kurze Saetze, aktive Formulierung, Subjekt vor Praedikat. Vermeidung Passiv, Substantivketten, Genitiv. |
| `elsj-sozialgerichtsverfahren` | Sozialgerichtsverfahren in Einfacher Sprache: Klageeinreichung Niederschrift § 90 SGG, kein Anwaltszwang, ehrenamtliche Richter. Vorlage Mandanteninformation 'Was passiert vor dem Sozialgericht'. |
| `elsj-sozialgerichtsverfahren-strafverfahren` | Elsj Sozialgerichtsverfahren Strafverfahren im Einfache und leichte Sprache im Recht: prüft konkret Sozialgerichtsverfahren in Einfacher Sprache, Strafverfahren in Einfacher Sprache fuer Beschuldigte, Bauen. Liefert priorisierten Output... |
| `elsj-strafverfahren-beschuldigter` | Strafverfahren in Einfacher Sprache fuer Beschuldigte: Belehrung § 136 StPO, Rechte des Beschuldigten, Akteneinsicht, Wahlverteidiger/Pflichtverteidiger. Pflichtbelehrung in einfacher Sprache (BVerfG 2 BvR 1568/19). |
| `elsj-uebersetzungsablauf` | Standardablauf Uebersetzung: 1. Original lesen, 2. Kernaussage extrahieren, 3. Satz fuer Satz uebertragen, 4. Pruefen gegen Pruefliste, 5. mit Zielgruppe gegenpruefen. Empfehlung: parallele Textspalten Original/Uebersetzung. |
| `elsj-uebersetzungsablauf-wortebene-haus` | Elsj Uebersetzungsablauf Wortebene Haus im Einfache und leichte Sprache im Recht: prüft konkret Standardablauf Uebersetzung, Hauseigenes Glossar, Zielgruppen erkennen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und näch... |
| `elsj-wortebene-haus-glossar` | Hauseigenes Glossar: typische juristische Begriffe und deren Uebersetzungen. Beispiele: 'Beklagter' = 'die Person, gegen die geklagt wird'; 'Frist' = 'Zeitraum, in dem etwas getan werden muss'. Aufnahme in Kanzlei-Wiki. |
| `elsj-zielgruppen-erkennen` | Zielgruppen erkennen: Einfache Sprache fuer geringe Lesekompetenz (B1), Leichte Sprache fuer Menschen mit Lernschwierigkeiten oder geringer Deutsch-Kenntnis. Wahl der richtigen Stufe pro Mandant/Adressat. Pruefraster und Beispiele. |
| `experimentelle-glossar-sonderfall-jura` | Experimentelle Glossar Sonderfall Jura im Einfache und leichte Sprache im Recht: prüft konkret Experimentelle, Glossar, Jura. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `fristen-form-zustaendigkeit-rechtsweg` | Einfache: Fristen, Form, Zuständigkeit und Rechtsweg im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist,... |
| `glossar-sonderfall-edge-case` | Glossar: Sonderfall und Edge-Case-Prüfung im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung... |
| `juristische-juristisches-beweislast-klaeren` | Juristische Juristisches Beweislast Klaeren im Einfache und leichte Sprache im Recht: prüft konkret Juristische, Juristisches, Klaeren. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `juristisches-beweislast-darlegungslast` | Juristisches: Beweislast, Darlegungslast und Substantiierung im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welch... |
| `leichte-qualitaetsgate-rechtsinhalt` | Qualitaetsgate Rechtsinhalt im Einfache und leichte Sprache im Recht: prüft konkret Leichte, Qualitaetsgate, Rechtsinhalt. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `leichte-sprache-jura-fristen-risiko-mandant` | Fristen Risiko Mandant im Einfache und leichte Sprache im Recht: prüft konkret Fristen- und Risikoampel im Plugin, Mandantenkommunikation im Plugin, Red-Team Qualitygate im Plugin einfache-leichte-sprache-jura. Liefert priorisierten Outp... |
| `leichte-sprache-jura-ls-bescheid-chronologie` | LS Bescheid Chronologie im Einfache und leichte Sprache im Recht: prüft konkret Einstieg, Schnelltriage und Fallrouting im Einfache Leichte Sprache, Bescheid in Leichte Sprache uebersetzen Workflow, Chronologie und Belegmatrix im Plugin.... |
| `leichte-sprache-qualitaetsgate-verstaendlichkeit` | Qualitaetsgate: Fehlerbremse; Formular, Portal und Einreichungslogik: prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `leichte-sprache-zielgruppe-zahlen-schwellen-berechnung` | Zielgruppe Zahlen Schwellen Berechnung im Einfache und leichte Sprache im Recht: fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |
| `ls-bescheid-uebersetzen-workflow` | Bescheid in Leichte Sprache uebersetzen Workflow: Originalbescheid, Kernaussagen extrahieren, je Aussage 1 kurzer Satz, Pruefung mit Zielgruppen-Vertreter, Layout (Bilder, Schriftgroesse), Pruefsiegel. Routet in einfache-leichte-sprache-... |
| `ls-juristisches-glossar-bauen` | Juristisches Glossar fuer Einfache und Leichte Sprache aufbauen: Schlagwort, Schwerverstaendliche Definition, Variante Einfache Sprache, Variante Leichte Sprache. Pro Eintrag Beispielssatz. Strukturierter CSV-Output und Mustertext fuer 3... |
| `ls-justizportal-pruefen-spezial` | Spezialfall Justizportal in Leichte Sprache pruefen: Bayerisches Justizportal, JustizOnline, beA-Frontend. Konkrete Verbesserungsvorschlaege fuer Navigation, Wegleitsysteme, Antragsformulare. Pruefraster nach Inclusion Europe Regeln. |
| `ls-strafprozess-rechte-erklaeren-spezial` | Spezialfall Strafprozess-Rechte in Leichte Sprache erklaeren: § 136 StPO Belehrung, Recht zur Aussage und zum Schweigen, Pflichtverteidiger, Akteneinsicht. Mustertext und Pruefsiegel. Bedeutung fuer JVA-Insassen und Migrantinnen. |
| `nutzen-fehlerkatalog` | Nutzen Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `rechtsinhalt-interessen` | Rechtsinhalt: Mehrparteienkonflikt und Interessenmatrix im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Fri... |
| `risikoampel-gegenargumente` | Leichte: Risikoampel, Gegenargumente und Verteidigungslinien im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welch... |
| `sichern-sprache-standard` | Sichern Sprache Standard im Einfache und leichte Sprache im Recht: prüft konkret Sichern, Sprache, Standard. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `texte-uebertragen-zielgruppe-sprachniveau` | Texte Uebertragen Zielgruppe Sprachniveau im Einfache und leichte Sprache im Recht: prüft konkret Texte, Uebertragen, Zielgruppe, Sprachniveau und gesicherter Rechtsinhalt. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und... |
| `zielgruppe-sprachniveau-rechtsinhalt` | Zielgruppe, Sprachniveau und gesicherter Rechtsinhalt: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
