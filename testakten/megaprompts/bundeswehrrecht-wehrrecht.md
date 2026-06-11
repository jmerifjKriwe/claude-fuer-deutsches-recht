# Megaprompt: bundeswehrrecht-wehrrecht

> *Achtung: Dies ist ein experimentelles Mega-Prompt-Markdown, das einen kompletten Klotzkette-Plugin in eine einzige Datei zusammenfuehrt. Keine Haftung, keine Gewaehr. Nur zum Ausprobieren der Skills auch ohne Claude Code; keine Rechtsberatung. Vor Verwendung im Mandat anwaltlich pruefen.*
>
> *Caution: This is an experimental Mega-Prompt Markdown that consolidates a full Klotzkette plugin into a single file. No warranty, no liability. For exploration with chat tools that do not run Claude Code only; not legal advice.*

**Verwendung:** Diesen gesamten Text in einen Chat ohne Claude-Code-Integration einfuegen (oder als Datei hochladen). Der Chat-Agent erhaelt damit die gebuendelten Skills dieses Plugins als Kontext. Eine Replikation des vollen Plugin-Verhaltens ist nicht garantiert — der Megaprompt ist eine Best-Effort-Kompression.


## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 82 Skills des Plugins `bundeswehrrecht-wehrrecht`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting im Bundeswehrrecht und Wehrrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen,…
2. **auslandseinsatz-einsatzregeln-beamtenrecht** — Auslandseinsatz Mandat Einsatzregeln: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Q…
3. **beschwerde-besoldung-zulagen-beurteilung** — Beschwerde gegen Beurteilung und Laufbahnentscheidung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und A…
4. **bundesverwaltungsgericht-wehrdienstsenate** — Bundesverwaltungsgericht Wehrdienstsenate: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. No…
5. **dienstunfaehigkeit-entlassung-dienstzeit** — Dienstunfähigkeit Entlassung Zurruhesetzung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. …
6. **eilverfahren-konkurrentenstreit** — Eilverfahren Konkurrentenstreit Wehrdienstsenat: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahm…
7. **einsatzunfall-wehrdienstbeschaedigung** — Einsatzunfall Wehrdienstbeschädigung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Q…
8. **gehorsam-befehl-und-rechtswidriger-befehl** — Gehorsam Befehl und rechtswidriger Befehl: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. No…
9. **kriegsdienstverweigerung-verfahren** — Kriegsdienstverweigerung Verfahren: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Que…
10. **nebentaetigkeit-geschenkannahme-personalakte** — Nebentätigkeit Geschenkannahme Compliance: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. No…
11. **politische-betaetigung-maessigung-neutralitaet** — Politische Betätigung Mäßigung Neutralität: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. N…
12. **presseaeusserung-meinungsfreiheit-soldat** — Presseäußerung Meinungsfreiheit Soldat: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-…
13. **ptbs-einsatzfolge-reservistendienst** — PTBS Einsatzfolge Beweisführung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quelle…
14. **soldatenbeteiligung-vertrauensperson-sbg** — Soldatenbeteiligung Vertrauensperson SBG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Nor…
15. **soldatengesetz-rechtsstellung** — Soldatengesetz Rechtsstellung Grundpflichten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen.…

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting im Bundeswehrrecht und Wehrrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, erkennt stumme Uploads und schlägt passende Fachmodule aus diesem Plugin vor._

# Bundeswehrrecht und Wehrrecht — Allgemein

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Bundeswehrrecht Wehrrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Sofortstart
Dieses Allgemein-Skill ist der Empfangstresen und Projektleiter des Plugins **Bundeswehrrecht und Wehrrecht**. Es soll den Nutzer nicht belehren, sondern schnell arbeitsfähig machen: erst die Lage erfassen, dann den passenden Pfad wählen, dann direkt einen verwertbaren Output erzeugen.

**Plugin-Fokus:** Bundeswehrrecht mit Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung, Wehrpflichtgesetz, Reservistenrecht, Soldatenversorgung, Befehlsrecht, Fürsorge und Rechtsschutz.

## Bei stummem Upload
Wenn der Nutzer nur ein Dokument, Bild, PDF, Vertrag, Bescheid, Tabellenwerk, E-Mail, Registerauszug oder Aktenkonvolut hochlädt, behandle das als Auftrag.

1. **Erkannt:** Dokumentart, Absender, Datum, Aktenzeichen, Beteiligte und Lebenssachverhalt nennen.
2. **Frist zuerst:** Zustellung, Rechtsbehelf, Behördenfrist, Zahlungsziel, Ausschlussfrist oder Verjährungsrisiko markieren.
3. **Einordnung:** Rechtsgebiet, Normengruppe, Behörde/Gericht und Arbeitstyp bestimmen.
4. **Primärer Pfad:** den wahrscheinlich passenden Fachmodul aus diesem Plugin nennen und bei eindeutigem Treffer direkt anwenden.
5. **Nur eine Rückfrage:** nur wenn ohne die Antwort ein falscher nächster Schritt droht.

## Intake in 60 Sekunden
- Wer fragt: Anwalt, Rechtsabteilung, Unternehmen, Patient, Apotheke, Krankenhaus, Verbraucher, Behörde, Soldat, Familie oder Verband?
- Was soll entstehen: Kurzprüfung, Memo, Schriftsatz, Antrag, Anzeige, Stellungnahme, Checkliste, Berechnung, Vertragsklausel, Behördenbrief oder Mandantenübersetzung?
- Was eilt: Frist, Termin, Zustellung, Anhörung, Ausschlussfrist, Verjährung, Bußgeld, Widerruf, Gebührenrisiko oder Verfahrensschritt?
- Welche Unterlagen liegen vor: Verträge, Bescheide, Rechnungen, Tabellen, Registerauszüge, Leitlinien, Formulare, E-Mails, Fotos, Chatverläufe?
- Was ist unsicher: Tatsachen, Zahlen, Zuständigkeit, Rechtslage, technische Daten, Marktdefinition, medizinischer Sachverhalt oder Familien-/Versorgungsverlauf?

## Arbeitsmodus
- **Schnelltriage:** Frist, Risiko, nächster Schritt.
- **Aktenmodus:** Dokumente sortieren, Timeline, Belegmatrix und Lückenliste.
- **Prüfmodus:** Tatbestand, Rechtsfolge, Gegenargumente, Risikoampel.
- **Entwurfsmodus:** Antrag, Schriftsatz, Vertragsklausel, Behördenbrief, Mandantenmail, Vorstandsvorlage.
- **Red-Team:** Ergebnis auf Halluzinationen, Quellen, Fristen, Zuständigkeit, Zahlen und Ton prüfen.

## Passende Einstiegsrouten
| Skill | Wann? |
| --- | --- |
| `soldatengesetz-rechtsstellung-grundpflichten` | Soldatengesetz Rechtsstellung Grundpflichten |
| `pflicht-zum-treuen-dienen-7-sg` | Pflicht zum treuen Dienen § 7 SG |
| `gehorsam-befehl-und-rechtswidriger-befehl` | Gehorsam Befehl und rechtswidriger Befehl |
| `kameradschaft-achtungs-und-vertrauenspflicht` | Kameradschaft Achtungs- und Vertrauenspflicht |
| `politische-betaetigung-maessigung-neutralitaet` | Politische Betätigung Mäßigung Neutralität |
| `nebentaetigkeit-geschenkannahme-compliance` | Nebentätigkeit Geschenkannahme Compliance |
| `dienstzeit-soldat-auf-zeit-berufssoldat-fwdl` | Dienstzeit Soldat auf Zeit Berufssoldat FWDL |
| `ernennung-dienstgrad-laufbahnrecht` | Ernennung Dienstgrad Laufbahnrecht |
| `versetzung-kommandierung-abordnung` | Versetzung Kommandierung Abordnung |
| `beurteilung-konkurrentenstreit-auswahlentscheidung` | Beurteilung Konkurrentenstreit Auswahlentscheidung |
| `wehrbeschwerdeordnung-beschwerde-frist-form` | Wehrbeschwerdeordnung Beschwerde Frist Form |
| `weitere-beschwerde-und-gerichtlicher-antrag-wehrdienstgericht` | Weitere Beschwerde und gerichtlicher Antrag Wehrdienstgericht |
| `truppendienstgericht-zuständigkeit-verfahren` | Truppendienstgericht Zuständigkeit Verfahren |
| `wehrdisziplinarordnung-einfache-disziplinarmassnahme` | Wehrdisziplinarordnung einfache Disziplinarmaßnahme |
| `gerichtliches-disziplinarverfahren-soldat` | Gerichtliches Disziplinarverfahren Soldat |
| `vorläufige-dienstenthebung-einbehaltung-bezuege` | Vorläufige Dienstenthebung Einbehaltung Bezüge |
| `befehl-verweigern-gewissensnot-rechtswidrigkeit` | Befehl verweigern Gewissensnot Rechtswidrigkeit |
| `wehrstrafrecht-fahnenflucht-gehorsamsverweigerung-schnittstelle` | Wehrstrafrecht Fahnenflucht Gehorsamsverweigerung Schnittstelle |
| `einsatzunfall-wehrdienstbeschaedigung` | Einsatzunfall Wehrdienstbeschädigung |
| `soldatenversorgungsgesetz-beschaedigtenversorgung` | Soldatenversorgungsgesetz Beschädigtenversorgung |
| `dienstunfaehigkeit-entlassung-zurruhesetzung` | Dienstunfähigkeit Entlassung Zurruhesetzung |
| `ptbs-einsatzfolge-beweisfuehrung` | PTBS Einsatzfolge Beweisführung |
| `gleichstellung-diskriminierung-soldatinnen-soldaten` | Gleichstellung Diskriminierung Soldatinnen Soldaten |
| `sexuelle-belaestigung-beschwerde-schutzpflicht` | Sexuelle Belästigung Beschwerde Schutzpflicht |
| `mobbing-fürsorgepflicht-bundeswehr` | Mobbing Fürsorgepflicht Bundeswehr |
| `personalakte-einsicht-datenschutz` | Personalakte Einsicht Datenschutz |
| `geheimschutz-sicherheitsueberpruefung-sueg` | Geheimschutz Sicherheitsüberprüfung SÜG |
| `reservistendienst-dienstleistungspflicht` | Reservistendienst Dienstleistungspflicht |
| `wehrpflichtgesetz-spannungs-und-verteidigungsfall` | Wehrpflichtgesetz Spannungs- und Verteidigungsfall |
| `kriegsdienstverweigerung-verfahren` | Kriegsdienstverweigerung Verfahren |
| `wehruebungen-heranziehungsbescheid` | Wehrübungen Heranziehungsbescheid |
| `unterhaltssicherung-reservisten` | Unterhaltssicherung Reservisten |
| `auslandseinsatz-mandat-einsatzregeln` | Auslandseinsatz Mandat Einsatzregeln |
| `statusrechte-im-einsatz-urlaub-betreuung` | Statusrechte im Einsatz Urlaub Betreuung |
| `schadenersatz-regress-dienstunfall-material` | Schadenersatz Regress Dienstunfall Material |

## Aktuelle Anschluss-Skills

Diese Tabelle wird aus dem tatsächlichen Skillbestand des Plugins gebildet. Wenn ein Nutzer nach dem Einstieg weitergeleitet werden soll, nimm bevorzugt diese Namen.

| Skill | Wann einsetzen? |
| --- | --- |
| `aerztliche-begutachtung-dienstfaehigkeit` | Ärztliche Begutachtung Dienstfähigkeit: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinaro... |
| `akteneinsicht-wbo-wdo` | Akteneinsicht WBO WDO: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehr... |
| `arbeitsrecht-zivile-bundeswehrbeschaeftigte` | Arbeitsrecht zivile Bundeswehrbeschäftigte: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszipli... |
| `ausbildung-studium-bundeswehr-rueckforderung-ausbildungskosten` | Ausbildung Studium Bundeswehr Rückforderung Ausbildungskosten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeor... |
| `auslandseinsatz-mandat-einsatzregeln` | Auslandseinsatz Mandat Einsatzregeln: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarord... |
| `beamtenrecht-bundeswehrverwaltung-abgrenzung` | Beamtenrecht Bundeswehrverwaltung Abgrenzung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszip... |
| `befehl-verweigern-gewissensnot-rechtswidrigkeit` | Befehl verweigern Gewissensnot Rechtswidrigkeit: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdis... |
| `beschwerde-fristen-sofortcheck` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Beschwerde Fristen Sofortcheck. |
| `beschwerde-gegen-beurteilung-und-laufbahnentscheidung` | Beschwerde gegen Beurteilung und Laufbahnentscheidung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, W... |
| `besoldung-zulagen-auslandsverwendungszuschlag` | Besoldung Zulagen Auslandsverwendungszuschlag: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszi... |
| `beurteilung-konkurrentenstreit-auswahlentscheidung` | Beurteilung Konkurrentenstreit Auswahlentscheidung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehr... |
| `bundesverwaltungsgericht-wehrdienstsenate` | Bundesverwaltungsgericht Wehrdienstsenate: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplin... |
| `dienstunfaehigkeit-entlassung-zurruhesetzung` | Dienstunfähigkeit Entlassung Zurruhesetzung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszipl... |
| `dienstzeit-soldat-auf-zeit-berufssoldat-fwdl` | Dienstzeit Soldat auf Zeit Berufssoldat FWDL: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszip... |
| `disziplinarverfahren-intake` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Disziplinarverfahren Intake. |
| `eilverfahren-konkurrentenstreit-wehrdienstsenat` | Eilverfahren Konkurrentenstreit Wehrdienstsenat: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdis... |
| `einsatz-unfall-versorgung-dokumentenplan` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Einsatz Unfall Versorgung Dokumentenplan. |
| `einsatzunfall-wehrdienstbeschaedigung` | Einsatzunfall Wehrdienstbeschädigung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarord... |
| `entlassung-auf-eigenen-antrag` | Entlassung auf eigenen Antrag: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 20... |
| `ernennung-dienstgrad-laufbahnrecht` | Ernennung Dienstgrad Laufbahnrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnu... |
| `extremismus-verdachtsfall-sicherheitsrecht` | Extremismus Verdachtsfall Sicherheitsrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszipli... |
| `fristenkalender-bundeswehrrecht` | Fristenkalender Bundeswehrrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung... |
| `geheimschutz-sicherheitsueberpruefung-sueg` | Geheimschutz Sicherheitsüberprüfung SÜG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinar... |
| `gehorsam-befehl-und-rechtswidriger-befehl` | Gehorsam Befehl und rechtswidriger Befehl: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplin... |
| `gerichtliches-disziplinarverfahren-soldat` | Gerichtliches Disziplinarverfahren Soldat: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplin... |
| `gleichstellung-diskriminierung-soldatinnen-soldaten` | Gleichstellung Diskriminierung Soldatinnen Soldaten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Weh... |
| `impfpflicht-tauglichkeit-musterung` | Impfpflicht Tauglichkeit Musterung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnu... |
| `kaltstart-bundeswehrrecht` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Kaltstart Bundeswehrrecht. |
| `kameradschaft-achtungs-und-vertrauenspflicht` | Kameradschaft Achtungs- und Vertrauenspflicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszi... |
| `kriegsdienstverweigerung-verfahren` | Kriegsdienstverweigerung Verfahren: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnu... |
| `livecheck-sg-wbo-wdo-wpflg-svg` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Livecheck SG WBO WDO WPflG SVG. |
| `mandantenbrief-soldat-verstaendlich` | Mandantenbrief Soldat verständlich: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnu... |
| `mobbing-fürsorgepflicht-bundeswehr` | Mobbing Fürsorgepflicht Bundeswehr: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnu... |
| `nebentaetigkeit-geschenkannahme-compliance` | Nebentätigkeit Geschenkannahme Compliance: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplin... |
| `output-beschwerde-antrag-stellungnahme` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Output Beschwerde Antrag Stellungnahme. |
| `personalakte-einsicht-datenschutz` | Personalakte Einsicht Datenschutz: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnun... |
| `personalvertretung-zivile-beschaeftigte-schnittstelle` | Personalvertretung zivile Beschäftigte Schnittstelle: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, We... |
| `pflicht-zum-treuen-dienen-7-sg` | Pflicht zum treuen Dienen § 7 SG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung... |
| `politische-betaetigung-maessigung-neutralitaet` | Politische Betätigung Mäßigung Neutralität: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszipli... |
| `presseaeusserung-meinungsfreiheit-soldat` | Presseäußerung Meinungsfreiheit Soldat: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinaro... |
| `ptbs-einsatzfolge-beweisfuehrung` | PTBS Einsatzfolge Beweisführung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung... |
| `rechtsbeistand-im-disziplinarverfahren` | Rechtsbeistand im Disziplinarverfahren: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinaro... |
| `red-team-bundeswehr-beschwerde` | Red-Team Bundeswehr-Beschwerde: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2... |
| `reservistendienst-dienstleistungspflicht` | Reservistendienst Dienstleistungspflicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplina... |
| `sanitaetsdienst-heilfürsorge` | Sanitätsdienst Heilfürsorge: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025... |
| `schadenersatz-regress-dienstunfall-material` | Schadenersatz Regress Dienstunfall Material: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszipl... |
| `sexuelle-belaestigung-beschwerde-schutzpflicht` | Sexuelle Belästigung Beschwerde Schutzpflicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszi... |
| `social-media-soldat-dienstpflichten` | Social Media Soldat Dienstpflichten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordn... |
| `soldatenbeteiligung-vertrauensperson-sbg` | Soldatenbeteiligung Vertrauensperson SBG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplina... |
| `soldatengesetz-rechtsstellung-grundpflichten` | Soldatengesetz Rechtsstellung Grundpflichten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszip... |
| `soldatenversorgungsgesetz-beschaedigtenversorgung` | Soldatenversorgungsgesetz Beschädigtenversorgung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdi... |
| `status-soldat-beamter-zivilbeschaeftigter-klaeren` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Status Soldat Beamter Zivilbeschäftigter klären. |
| `statusrechte-im-einsatz-urlaub-betreuung` | Statusrechte im Einsatz Urlaub Betreuung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplina... |
| `trennungsgeld-umzugskosten-reisekosten` | Trennungsgeld Umzugskosten Reisekosten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinaro... |
| `truppendienstgericht-zuständigkeit-verfahren` | Truppendienstgericht Zuständigkeit Verfahren: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszip... |
| `unterhaltssicherung-reservisten` | Unterhaltssicherung Reservisten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung... |
| `versetzung-kommandierung-abordnung` | Versetzung Kommandierung Abordnung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnu... |
| `vorläufige-dienstenthebung-einbehaltung-bezuege` | Vorläufige Dienstenthebung Einbehaltung Bezüge: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisz... |
| `wehrbeschwerdeordnung-beschwerde-frist-form` | Wehrbeschwerdeordnung Beschwerde Frist Form: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszipl... |
| `wehrdisziplinarordnung-einfache-disziplinarmassnahme` | Wehrdisziplinarordnung einfache Disziplinarmaßnahme: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Weh... |
| `wehrpflicht-wehrdienst-reservist-routing` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Wehrpflicht Wehrdienst Reservist Routing. |
| `wehrpflichtgesetz-spannungs-und-verteidigungsfall` | Wehrpflichtgesetz Spannungs- und Verteidigungsfall: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehr... |
| `wehrstrafrecht-fahnenflucht-gehorsamsverweigerung-schnittstelle` | Wehrstrafrecht Fahnenflucht Gehorsamsverweigerung Schnittstelle: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerde... |
| `wehruebungen-heranziehungsbescheid` | Wehrübungen Heranziehungsbescheid: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnun... |
| `weitere-beschwerde-und-gerichtlicher-antrag-wehrdienstgericht` | Weitere Beschwerde und gerichtlicher Antrag Wehrdienstgericht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeor... |
| `widerruf-ernennung-arglistige-taeuschung` | Widerruf Ernennung arglistige Täuschung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinar... |

<!-- END ACTUAL-SKILL-ROUTING -->

---

## Skill: `auslandseinsatz-einsatzregeln-beamtenrecht`

_Auslandseinsatz Mandat Einsatzregeln: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG im Bundeswehrrecht..._

# Auslandseinsatz – Mandat und Einsatzregeln

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Auslandseinsatz – Mandat und Einsatzregeln
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Worum geht es konkret

Bewaffnete Auslandseinsätze deutscher Streitkräfte unterliegen einem dreistufigen Regelwerk: völkerrechtliches Mandat (UN-Resolution, NATO-Beschluss, EU-Operationsplan), konstitutiver Zustimmungsbeschluss des Bundestages (Parlamentsbeteiligungsgesetz) und Einsatzregeln (Rules of Engagement, ROE). Der Skill ordnet die Rechtsgrundlagen, prüft Befehlsverbindlichkeit innerhalb des Mandats und führt durch Statusfragen (NATO-Truppenstatut, SOFA-Abkommen).

## Wann dieses Modul hilft / Kaltstart-Fragen

- Welcher konkrete Einsatz (KFOR, EUFOR, EUTM, UNIFIL, Sea Guardian, Counter Daesh, neuere Mandate)?
- Welche Verwendung im Einsatz (Truppe, Stab, Beobachter, Ausbildung)?
- Welche Frage steht (Befehlsverbindlichkeit, ROE-Reichweite, Status, Versorgung, Strafverfolgung im Gastland)?
- Liegt ein konkreter Vorfall vor (Waffeneinsatz, Verletzung, ziviler Schaden)?
- Welche nationalen Caveats sind formuliert?
- Welche Statusabkommen gelten (SOFA, NATO SOFA, Memorandum of Understanding)?

## Rechtlicher Rahmen

- Art. 87a, 87 II GG: Streitkräfteeinsatz nur zur Verteidigung und in den vom GG ausdrücklich zugelassenen Fällen.
- BVerfG zur Out-of-Area-Rechtsprechung – ständige Rechtsprechung zur Bundestagsbeteiligung.
- Parlamentsbeteiligungsgesetz (ParlBG) – konstitutive Zustimmung des Bundestages.
- Bundestagsmandat in konkreter Drucksache – Mandatsumfang, Stärke, Aufgaben.
- § 63c SG: Besonderer Auslandseinsatz – Anknüpfungspunkt für Versorgung.
- ROE (Rules of Engagement): rechtsverbindliche Befehlsstufen für Anwendung militärischer Gewalt.
- NATO-Truppenstatut (BGBl. II 1961 S. 1190) und Zusatzabkommen.
- Humanitäres Völkerrecht: Genfer Abkommen I–IV und Zusatzprotokolle I/II.
- Völkerstrafgesetzbuch (VStGB) und Wehrstrafgesetz.

## / Schritt für Schritt

1. **Mandatsstatus prüfen.** Bundestagsdrucksache mit Beschluss, Geltungsdauer, Mandatsstärke, Aufgabenbeschreibung.
2. **Völkerrechtliche Grundlage** verifizieren (UN-Resolution, NATO-Beschluss, EU-CSDP-Mandat).
3. **Einsatzregeln (ROE)** durch nationalen Befehl konkretisieren – Caveats? Gewaltanwendungsschwellen?
4. **Konkreten Vorfall einordnen.**
 - Innerhalb ROE und Mandat: rechtmäßig.
 - Außerhalb: unverbindlicher Befehl, ggf. § 11 II SG / VStGB.
5. **Statusrechtliche Folgen.** Welche Gerichtsbarkeit (Deutschland nach NATO SOFA / Entsendestaatprinzip)?
6. **Versorgungsfolgen.** § 81a SVG Einsatzunfall.
7. **Wehrbeauftragter und parlamentarische Kontrolle** bei Unstimmigkeiten.

## Trade-off-Matrix

| Konstellation | Strategie |
| --- | --- |
| Befehl innerhalb ROE | Ausführung, ggf. interner Vermerk |
| Zweifel an Mandatskonformität | Remonstration, Bestätigung schriftlich |
| Zivile Opfer | Sofortmeldung, Tatsachensicherung, internationaler Ermittlungsstandard |
| Strafverfahren Gastland | NATO SOFA-Klausel: ggf. deutsche Gerichtsbarkeit |

## Praxistipps

- Mandatsdrucksache muss vor Verwendung gelesen sein – Caveats begrenzen Befehlsumfang.
- ROE sind häufig vertraulich – Verteidigung erfordert Schutzanordnung beim Truppendienstgericht.
- Sofortmeldung bei Waffeneinsatz: Tatsachensicherung, Munitionsverbrauch, Personenkreis, GPS-Daten.
- Bei zivilen Verletzungen Beweisarbeit nach humanitärem Völkerrecht: Tatortbericht, ärztliche Versorgung, Dokumentation.
- NATO-Truppenstatut – primäre Gerichtsbarkeit häufig beim Entsendestaat; aber Gastland kann Vorrang reklamieren.

## Mustertexte

**Schriftliche Remonstration im Einsatz:**
"Herr [Dienstgrad], ich melde Bedenken gegen den Befehl, [...] zu tun. Nach Mandat [Drucksache] und den geltenden ROE Ziff. [...] ist diese Verwendung nicht gedeckt. Ich bitte um Bestätigung und um Mitteilung der Anordnung der nächsthöheren Befehlsebene."

**Sachverhaltsmeldung nach Waffeneinsatz:**
"Bericht zum Vorfall vom [Datum/Uhrzeit] in [Ort]. Beteiligte: [...]. Ablauf: [...]. Munitionsverbrauch: [...]. ROE-Stufe: [...]. Begründung der Lagebeurteilung: [...]. Anlagen: GPS-Track, Funkprotokoll, Zeugenangaben."

## Typische Fehler

- Befehl ausgeführt, obwohl außerhalb Mandat / ROE – Risiko nach § 19/20 WStG und VStGB.
- Caveats nicht beachtet (zB nur "non-combat training" erlaubt).
- Sofortmeldung verzögert – Beweismittel verloren.
- NATO SOFA-Gerichtsbarkeitsfrage übersehen – Mandant unter Gastlandsgerichtsbarkeit.
- Versorgungsrechtliche Folgen nicht parallel dokumentiert (§ 81a SVG).

## Quellen Stand 06/2026

- ParlBG – Volltext gesetze-im-internet.de.
- Bundestagsmandate – Drucksachen (bundestag.de).
- BVerfG Out-of-Area-Rechtsprechung – ständige Rechtsprechung.
- NATO-Truppenstatut – BGBl. II 1961 S. 1190 ff., aktuelle Fassung und Zusatzabkommen.
- Genfer Abkommen I–IV und Zusatzprotokolle – BGBl. II 1954, 1990.
- VStGB – Volltext gesetze-im-internet.de.
- ROE: nur nach Vorlage durch Mandanten oder Gericht, nicht aus Modellwissen.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 5 GG
- § 81a SVG
- § 81e SVG
- § 27 SVG
- § 9a BBesG
- § 5 SVG
- Art. 4 GG
- § 5 WStG
- § 81 SVG
- § 70 BBesG
- Art. 12a GG
- § 22 SÜG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `beschwerde-besoldung-zulagen-beurteilung`

_Beschwerde gegen Beurteilung und Laufbahnentscheidung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG i..._

# Beschwerde gegen Beurteilung und Laufbahnentscheidung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Beschwerde gegen Beurteilung und Laufbahnentscheidung
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Worum geht es konkret

Die Beurteilung (planmäßig oder Anlassbeurteilung) und die darauf gestützte Laufbahnentscheidung (Beförderung, Verwendungsentscheidung, Auswahlentscheidung) sind die Grundlage der Karriere des Soldaten. Beide sind im WBO-Weg anfechtbar (§ 1 WBO). Der Skill ordnet Beurteilungssystematik, Beschwerdegegenstände und Eilrechtsschutz im Konkurrentenstreit.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Welche Beurteilung (planmäßig, Anlass, Probezeit)?
- Welcher Beurteiler (erster, zweiter, Höher- oder Endbeurteiler)?
- Welche konkrete Wertung wird angegriffen (Einzelmerkmale, Gesamtwertung, Verwendungsempfehlung)?
- Wann eröffnet, wann zugegangen (Frist § 6 WBO)?
- Ist parallel ein Konkurrentenstreit anhängig (Beförderung, Dienstposten)?
- Welcher Vergleichsmaßstab steht zur Verfügung (Vergleichsgruppe, Quotenregelung)?

## Rechtlicher Rahmen

- § 27 SG: Beurteilung als dienstliche Bewertung der Eignung, Befähigung und fachlichen Leistung.
- Laufbahnrecht: Soldatenlaufbahnverordnung (SLV) – Voraussetzungen für Beförderung, Verwendung, Wechsel.
- Beurteilungsbestimmungen Bundeswehr – periodisch fortgeschrieben.
- Art. 33 II GG: Bestenauslese – Anspruch auf leistungsbezogene Auswahl.
- § 1 WBO: Beschwerderecht – auch gegen Beurteilung und Auswahlentscheidung.
- § 21 WBO: Erstinstanzliche Zuständigkeit BVerwG bei Maßnahme höherer Vorgesetzter (oft im Konkurrentenstreit).
- BVerwG-Rspr. zu Beurteilungsspielraum und Plausibilitätskontrolle – ständige Rechtsprechung.

## / Schritt für Schritt

1. **Beurteilung und Anlass dokumentieren.** Eröffnungsdatum, Beurteilerkette, Vergleichsgruppe.
2. **Fehler identifizieren.**
 - Formaler Fehler (falsche Beurteilerkette, fehlende Eröffnung),
 - Sachlicher Fehler (Verwertungsverbote, Hörensagen, falsche Tatsachenbasis),
 - Bewertungsfehler (Plausibilitätslücke, Maßstabsverstöße),
 - Quotenfehler (falsche Vergleichsgruppe).
3. **Frist sichern.** § 6 WBO: 1 Monat ab Eröffnung. Fristwahrende Beschwerde mit Vorbehalt der Begründung möglich.
4. **Akteneinsicht.** Personalakte, andere Beurteilungen (anonymisierte Auswertung), Quotenmatrix.
5. **Konkurrentenstreit.**
 - Eilantrag § 21 WBO i.V.m. § 80a VwGO entsprechend, wenn Beförderung anderer droht.
 - Schutzschrift zum BVerwG bei höchstrangiger Auswahl.
6. **Beschwerdeschrift.** Konkrete Rüge der Beurteilungsfehler, Anträge auf Aufhebung und Neubeurteilung.
7. **Mündliche Verhandlung.** Bei Truppendienstgericht häufig; persönliches Erscheinen.

## Trade-off-Matrix

| Konstellation | Strategie |
| --- | --- |
| Klar fehlerhafte Tatsachen | Beweisangebote, Zeugenliste |
| Plausibilitätsfehler | Plausibilitätskontrolle nach BVerwG-Rspr. |
| Drohende Beförderung Mitbewerber | Eilantrag § 21 WBO mit Beförderungsstopp |
| Reine Bemessungsfrage | Beschwerde, ohne Eilrechtsschutz |
| Quotenproblem | Vergleichsgruppe und Maßstab angreifen |

## Praxistipps

- Beurteilungen sind nur eingeschränkt überprüfbar – Spielraum der Beurteiler. Fokus auf formelle und Plausibilitätsfehler.
- Eröffnungstermin Pflicht – ohne Eröffnung läuft die Frist nicht.
- Personalakte spiegelt die Auswahlerwägungen wider – zwingende Einsicht vor Eilrechtsschutz.
- Schutzschrift beim BVerwG vor Beförderungsterminen anderer – häufig nur wenige Wochen Reaktionszeit.
- Maßstabsfragen erfordern Vergleichsgruppe – ohne diese kein Erfolg im Konkurrentenstreit.

## Mustertexte

**Beschwerde gegen Beurteilung:**
"Gegen die mir am [Datum] eröffnete Beurteilung lege ich fristwahrend Beschwerde nach § 1 WBO ein. Ich beantrage: 1. Aufhebung der Beurteilung. 2. Neuerstellung durch [...]. 3. Einsicht in die Vergleichsgruppe und die Quotenmatrix. Begründung folgt nach Akteneinsicht. Rügen u.a.: a) fehlerhafte Tatsachenfeststellung in [...]. b) Plausibilitätslücke zwischen Einzel- und Gesamtwertung. c) Vergleichsgruppe nicht ordnungsgemäß gebildet."

**Eilantrag § 21 WBO Konkurrentenstreit:**
"An das Bundesverwaltungsgericht, Wehrdienstsenat. Es wird beantragt: Im Wege der einstweiligen Anordnung die Antragsgegnerin zu verpflichten, den Dienstposten [Bezeichnung] vorläufig nicht mit Mitbewerber [Name] zu besetzen, bis über die Beschwerde meines Mandanten rechtskräftig entschieden ist. Anordnungsgrund: drohende Beförderung am [Datum]. Anordnungsanspruch: fehlerhafte Auswahlentscheidung."

## Typische Fehler

- Eröffnungsdatum nicht dokumentiert – Frist unsicher.
- Akteneinsicht erst nach Beschwerdeeinlegung – Rügen lückenhaft.
- Schutzschrift im Konkurrentenstreit zu spät – Beförderung erfolgt vor Eilbeschluss.
- Plausibilitätsangriff ohne Vergleichsmaßstab.
- Verwaltungsgerichtsweg gewählt – WBO ist exklusiv.

## Quellen Stand 06/2026

- § 27 SG, Soldatenlaufbahnverordnung – Volltexte gesetze-im-internet.de.
- Beurteilungsbestimmungen Bundeswehr – aktuelle Fassung beim BMVg.
- Art. 33 II GG; BVerfG zu Bestenauslese – ständige Rechtsprechung.
- BVerwG Wehrdienstsenate – ständige Rechtsprechung zu Beurteilungsspielraum und Plausibilitätskontrolle (Az. nach Verifikation).
- WBO §§ 1, 6, 17, 21 – Volltext gesetze-im-internet.de.

---

## Skill: `bundesverwaltungsgericht-wehrdienstsenate`

_Bundesverwaltungsgericht Wehrdienstsenate: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG im Bundeswehr..._

# Bundesverwaltungsgericht – Wehrdienstsenate

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Bundesverwaltungsgericht – Wehrdienstsenate
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Worum geht es konkret

Die Wehrdienstsenate des BVerwG (1. und 2. Wehrdienstsenat) entscheiden über Rechtsmittel aus WDO und WBO sowie über erstinstanzliche Anträge in eng begrenzten Fällen (insbesondere Konkurrentenstreit gegen Maßnahmen höherer Vorgesetzter, § 21 WBO). Sie sind die höchste Instanz im Wehrdienstrecht und legen die Auslegung von SG, WBO, WDO maßgebend fest. Der Skill ordnet ein, wann das BVerwG Wehrdienstsenat zuständig ist und wie das Verfahren abläuft.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Liegt eine Entscheidung des Truppendienstgerichts vor? Berufung oder Revision?
- Geht es um eine Maßnahme eines höheren Vorgesetzten (BMVg, Inspekteur, Kommandeur höherer Ebene) – § 21 WBO erste Instanz?
- Welche Frist läuft (1 Monat ab Zustellung des TDG-Urteils; bei § 21 WBO erste Instanz: 1 Monat ab Beschwerdebescheid)?
- Streitwert/Bedeutung der Sache – Revisionszulassungsgründe?
- Eilbedürfnis (vorläufige Maßnahmen § 25 WBO entsprechend)?
- Soll grundsätzliche Rechtsfrage durch BVerwG geklärt werden?

## Rechtlicher Rahmen

- § 21 WBO: Erstinstanzliche Zuständigkeit des BVerwG bei Maßnahmen höherer Vorgesetzter (Bundesminister, Inspekteure).
- § 23a WDO: Berufung gegen TDG-Urteile in disziplinargerichtlichen Sachen.
- §§ 124 ff. VwGO i.V.m. §§ 19 ff. WBO: Verfahren vor dem BVerwG bei wehrbeschwerderechtlichen Streitsachen.
- §§ 132 ff. VwGO: Revisionszulassungsgründe – grundsätzliche Bedeutung, Divergenz, Verfahrensfehler.
- § 80a VwGO: Vorläufige Maßnahmen im Eilrechtsschutz.
- § 50 SG: Verlust der Rechte als Soldat – höchstrichterliche Klärung beim BVerwG.

## / Schritt für Schritt

1. **Rechtsmittelart bestimmen.** Berufung in WDO-Sachen (§ 23a WDO); Antrag auf gerichtliche Entscheidung in § 21 WBO-Sachen; Beschwerde gegen Beschluss des TDG.
2. **Frist sichern.** 1 Monat ab Zustellung des TDG-Urteils bzw. des Beschwerdebescheids.
3. **Anwaltspflicht.** Vor dem BVerwG besteht Vertretungszwang durch Rechtsanwalt nach § 67 IV VwGO entsprechend.
4. **Schriftsatz.** Tatsachenvortrag, rechtliche Würdigung, konkrete Anträge, Beweisangebote (Zeugen, Urkunden, Sachverständige).
5. **Zulassungsgründe.** Bei Revision: grundsätzliche Bedeutung, Divergenz, Verfahrensmangel substantiieren.
6. **Eilantrag prüfen.** Bei drohender Vollziehung – einstweilige Anordnung gegen Versetzung, Konkurrentenstreit, vorläufige Dienstenthebung.
7. **Mündliche Verhandlung** oft erforderlich; schriftliches Verfahren möglich.
8. **Urteil/Beschluss** mit Bindungswirkung; ggf. Verfassungsbeschwerde zum BVerfG (Art. 93 I Nr. 4a GG).

## Trade-off-Matrix

| Ausgangslage | BVerwG erste Instanz § 21 WBO | TDG-Berufungsweg |
| --- | --- | --- |
| Maßnahme BMVg/Inspekteur | Direkt BVerwG | nicht statthaft |
| TDG-Urteil mit Maßnahme | – | Berufung § 23a WDO |
| Konkurrentenstreit höhere Ebene | § 21 WBO + Eilantrag | – |
| Grundsatzfrage | Revision § 132 VwGO | – |

## Praxistipps

- BVerwG entscheidet streng nach Akten – Tatsachenvortrag in den vorinstanzlichen Schriftsätzen muss bereits präzise sein.
- "Ständige Rechtsprechung" der Wehrdienstsenate ist hochrelevant – Auswertung der BVerwG-Datenbank Pflicht. Konkrete Az. nur nach Verifikation zitieren.
- Anwaltspflicht ab BVerwG-Verfahren – Selbstvertretung des Soldaten unzulässig.
- Bei § 21 WBO-Verfahren: keine Vorbefassung des Truppendienstgerichts – Sprung in die Bundesgerichtsbarkeit.
- Eilanträge mit konkreter Glaubhaftmachung der Eilbedürftigkeit (zB Versetzung in zwei Wochen).

## Mustertexte

**Berufungsschrift im disziplinargerichtlichen Verfahren:**
"An das Bundesverwaltungsgericht, Wehrdienstsenat. Gegen das Urteil des Truppendienstgerichts [Süd/Nord], Az. [...], vom [Datum], zugestellt am [Datum], lege ich Berufung nach § 23a WDO ein. Es wird beantragt, das Urteil aufzuheben und [...]. Begründung folgt fristgerecht binnen [Frist]."

**Antrag § 21 WBO erste Instanz:**
"Gegen die Maßnahme des [Bundesministers/Inspekteurs/...] vom [Datum], zugegangen am [Datum], beantrage ich nach § 21 WBO i.V.m. § 17 WBO gerichtliche Entscheidung. Es wird beantragt: 1. Die Maßnahme aufzuheben. 2. Den Antragsgegner zu verpflichten, [...]. 3. Aussetzung der Vollziehung."

## Typische Fehler

- Frist 1 Monat versäumt – Zustellungsdatum ungeprüft.
- Selbstvertretung ohne Anwalt – Schriftsatz wird als unzulässig zurückgewiesen.
- Revisionszulassungsgründe nicht substantiiert.
- Tatsachenvortrag erst beim BVerwG nachgeholt – Präklusion droht.
- Verwechslung von erstinstanzlicher Zuständigkeit nach § 21 WBO und Berufungsweg nach § 23a WDO.

## Quellen Stand 06/2026

- WBO §§ 17, 21 – Volltext gesetze-im-internet.de.
- WDO § 23a – Volltext gesetze-im-internet.de.
- VwGO §§ 67, 80a, 124 ff., 132 – Volltext gesetze-im-internet.de.
- BVerwG Wehrdienstsenate – ständige Rechtsprechung; Entscheidungsdatenbank des BVerwG (bverwg.de).
- Geschäftsverteilung BVerwG – jährlich publiziert.
- Keine Kommentarstellen aus Modellwissen.

---

## Skill: `dienstunfaehigkeit-entlassung-dienstzeit`

_Dienstunfähigkeit Entlassung Zurruhesetzung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG im Bundeswe..._

# Dienstunfähigkeit – Entlassung und Zurruhesetzung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Dienstunfähigkeit – Entlassung und Zurruhesetzung
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Worum geht es konkret

Verliert der Soldat seine Dienstfähigkeit, führt dies zu unterschiedlichen Folgen je nach Statusgruppe: Soldat auf Zeit – Entlassung; Berufssoldat – Zurruhesetzung mit Ruhegehalt nach BeamtVG/SVG. Maßstab ist die Wehrdienstfähigkeit (Tauglichkeitsgrade T1–T5) und die spezifische Verwendungsfähigkeit. Der Skill ordnet medizinische Begutachtung, Verfahren der Statusentscheidung, Versorgung und Rechtsbehelfe.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Status: Berufssoldat, Soldat auf Zeit, FWDL?
- Diagnose, Behandlung, Heilungsperspektive?
- Vorläufige oder dauernde Dienstunfähigkeit?
- Bisherige Begutachtungen (Truppenarzt, Bundeswehrkrankenhaus, fachärztlich)?
- Steht Wiedereingliederung im Raum (Begrenzte Dienstfähigkeit)?
- Welche Versorgungsfolgen (Ruhegehalt, Beschädigtenversorgung)?

## Rechtlicher Rahmen

- § 44 III SG: Dienstunfähigkeit des Berufssoldaten – Zurruhesetzung.
- § 55 II SG: Entlassung des Soldaten auf Zeit wegen Dienstunfähigkeit.
- § 47 SG: Begrenzte Dienstfähigkeit (analog BeamtStG).
- § 18 SVG i.V.m. BeamtVG: Ruhegehalt des Berufssoldaten.
- §§ 81 ff. SVG: Beschädigtenversorgung bei WDB-Kausalität.
- ZDv A-1340/1 (ärztliche Begutachtung) – nur nach Vorlage.
- Tauglichkeitsgrade T1–T5 nach Wehrmedizinischer Dienstvorschrift.
- WBO-Beschwerderecht und § 17 WBO Verfahren.

## / Schritt für Schritt

1. **Sachstand klären.** Diagnose, Behandlungsplan, Verlauf, Prognose.
2. **Begutachtung.** Truppenarzt - BwKrhs - Spezialist. Eigenes Gutachten möglich.
3. **Statusfolge prüfen.**
 - Berufssoldat: Zurruhesetzung § 44 III SG plus Ruhegehalt.
 - Soldat auf Zeit: Entlassung § 55 II SG plus ggf. Übergangsgebührnisse.
 - Begrenzte Dienstfähigkeit: § 47 SG analog – Weiterverwendung mit reduzierter Belastung.
4. **WDB-Frage.** Ist die Dienstunfähigkeit Folge einer Wehrdienstbeschädigung / eines Einsatzunfalls? Wenn ja: § 81 ff. SVG-Versorgung zusätzlich.
5. **Verfahrensgang.** Anhörung des Soldaten, Stellungnahme, ärztliche Kontrolluntersuchung, Verfügung mit Rechtsbehelfsbelehrung.
6. **Beschwerde** § 1 WBO – 1 Monat. Eilantrag bei vorläufiger Maßnahme.
7. **Versorgungsrechnung.** Mindestversorgung, Ruhegehaltssatz nach Dienstzeit, Erhöhung bei Dienstbeschädigung.
8. **Wiedereingliederung** parallel: Reha, Berufsförderungsdienst (BFD).

## Trade-off-Matrix

| Status | Folge | Versorgung |
| --- | --- | --- |
| Berufssoldat dauerhaft unfähig | Zurruhesetzung § 44 III SG | Ruhegehalt § 18 SVG + ggf. WDB |
| SaZ dauerhaft unfähig | Entlassung § 55 II SG | Übergangsgebührnisse, BFD |
| Begrenzt dienstfähig | Weiterverwendung § 47 SG | volles Gehalt mit Reduzierung |
| WDB-bedingt | Zusätzlich SVG-Versorgung | Beschädigtenrente |

## Praxistipps

- Begutachtung möglichst durch Spezialisten – Truppenärzte sind Generalisten.
- "Verwendungsfähigkeit für besondere Auslandseinsätze" ist Sonderkriterium – Tauglichkeit T2 reicht häufig nicht.
- Vor Zurruhesetzung Wiedereingliederung versuchen (§ 47 SG analog) – Erhalt des Status hat erhebliche Versorgungsvorteile.
- Ruhegehalt setzt 5 Dienstjahre voraus (§ 4 BeamtVG entsprechend) – darunter Mindestversorgung oder Anrechnung in gesetzliche Rente.
- WDB-Kausalität verdoppelt häufig die Versorgungsbasis (Schadenausgleich + Grundversorgung).

## Mustertexte

**Stellungnahme zum Zurruhesetzungsverfahren:**
"Zur beabsichtigten Zurruhesetzung nehme ich wie folgt Stellung: 1. Diagnose, Therapie und Prognose siehe ärztliche Berichte Anl. 1–3. 2. Begrenzte Dienstfähigkeit nach § 47 SG ist möglich; vorgeschlagen wird Verwendung [...]. 3. Hilfsweise: Zurruhesetzung mit gleichzeitiger WDB-Feststellung nach § 81 SVG, weil die Dienstunfähigkeit Folge des Einsatzes [...] vom [Datum] ist."

**WBO-Beschwerde gegen Entlassungsverfügung:**
"Gegen die Entlassungsverfügung vom [Datum] lege ich fristwahrend Beschwerde ein. Rügen: 1. Begutachtung lückenhaft – Spezialgutachten nicht eingeholt. 2. Begrenzte Dienstfähigkeit (§ 47 SG analog) nicht geprüft. 3. WDB-Kausalität übersehen – § 81 SVG-Verfahren parallel einzuleiten. Antrag: Aufhebung der Entlassungsverfügung, hilfsweise Zurruhesetzung mit Anerkennung der WDB."

## Typische Fehler

- Truppenärztliche Beurteilung pauschal akzeptiert.
- Begrenzte Dienstfähigkeit nicht geprüft – sofortige Zurruhesetzung statt Erhalt des Status.
- WDB-Kausalität getrennt vom Statusverfahren prüfen – Versorgungslücke.
- Übergangsgebührnisse SaZ nicht beantragt.
- Frist § 6 WBO verpasst.

## Quellen Stand 06/2026

- §§ 44, 47, 55 SG – Volltext gesetze-im-internet.de.
- SVG, BeamtVG – Volltexte gesetze-im-internet.de.
- ZDv A-1340/1 – nur nach Vorlage.
- BVerwG Wehrdienstsenate – ständige Rechtsprechung zur Dienstunfähigkeit (Az. nach Verifikation).
- BAPersBw – Verwaltungspraxis und Formulare.
- Versorgungsmedizinische Grundsätze – BMAS.

---

## Skill: `eilverfahren-konkurrentenstreit`

_Eilverfahren Konkurrentenstreit Wehrdienstsenat: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG im Bund..._

# Eilverfahren – Konkurrentenstreit vor dem Wehrdienstsenat

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Eilverfahren – Konkurrentenstreit vor dem Wehrdienstsenat
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Worum geht es konkret

Beim Konkurrentenstreit geht es um die Auswahl zwischen mehreren Soldaten für einen begrenzten Dienstposten oder eine Beförderung. Da die Beförderung des Konkurrenten irreversible Folgen schafft, ist Eilrechtsschutz nötig. Der Skill ordnet Anordnungsanspruch und -grund, die Frist, das Verhältnis zur Hauptsache und die Besonderheiten beim BVerwG-Wehrdienstsenat (§ 21 WBO).

## Wann dieses Modul hilft / Kaltstart-Fragen

- Welche Auswahlentscheidung (Dienstposten, Beförderung, Verwendung)?
- Wer ist Mitbewerber (Name, Vergleichsbeurteilung)?
- Welche Stelle hat entschieden (BMVg, Inspekteur, BAPersBw)?
- Wann steht die Ausführung (Beförderungsappell, Übernahme Dienstposten) bevor?
- Bisheriger Verfahrensstand (Mitteilung Konkurrentenmitteilung, BAPersBw-Auswahlvermerk)?
- Bereits Beschwerde eingelegt? Schutzschrift abgelegt?

## Rechtlicher Rahmen

- Art. 33 II GG: Bestenauslese – Auswahl nach Eignung, Befähigung, fachlicher Leistung.
- § 1 WBO: Beschwerderecht.
- § 17 WBO: Antrag auf gerichtliche Entscheidung beim TDG.
- § 21 WBO: BVerwG-Wehrdienstsenat erste Instanz bei höchstrangiger Maßnahme.
- § 80a VwGO entsprechend: Vorläufige Maßnahmen.
- BVerwG-Rspr. zum Konkurrentenrechtsschutz – ständige Rechtsprechung (Konkurrentenmitteilung, Eilantrag, Beförderungsstopp).
- §§ 27, 28 SG: Beurteilung und Auswahlentscheidung.
- BVerfG zum effektiven Rechtsschutz vor Beförderung – ständige Rechtsprechung.

## / Schritt für Schritt

1. **Konkurrentenmitteilung sichern.** Vorab-Information durch Dienststelle ist Pflicht – Mandant muss reagieren können.
2. **Frist berechnen.** § 6 WBO: 1 Monat ab Mitteilung; aber im Konkurrentenstreit faktisch kürzer (Beförderungstermin).
3. **Akteneinsicht.** Personalakte und Vergleichsbeurteilungen (anonymisiert) anfordern, ggf. nach § 99 VwGO entsprechend Eilvorlage.
4. **Schutzschrift.** Beim TDG/BVerwG mit Beförderungsstopp.
5. **Eilantrag.**
 - § 21 WBO: bei höherer Vorgesetzten-Entscheidung BVerwG.
 - § 17 WBO: TDG für andere Maßnahmen.
6. **Anordnungsanspruch begründen.** Beurteilungsfehler, fehlerhafte Vergleichsgruppenbildung, fehlende Auswahlentscheidungsbegründung.
7. **Anordnungsgrund.** Drohende Beförderung des Mitbewerbers an konkretem Datum.
8. **Hauptsache anschließend.** Beschwerde und gerichtliche Entscheidung in der Sache.

## Trade-off-Matrix

| Konstellation | Eilrechtsschutz beim | Frist |
| --- | --- | --- |
| Beförderung durch Inspekteur/BMVg | BVerwG § 21 WBO | extrem kurz |
| Verwendung Dienstposten Bataillon | TDG § 17 WBO | 2 Wochen nach Beschwerdebescheid |
| Konkurrentenmitteilung vor BAPersBw | Beschwerde + ggf. Eilantrag | 1 Monat |
| Beförderung bereits vollzogen | Hauptsache (Anfechtung der Beförderung) | – |

## Praxistipps

- Konkurrentenmitteilung muss klar erkennbar sein – Mandant hat Anspruch auf Information nach BVerwG-Rspr.
- Beförderungstermine in der Bw sind häufig "Beförderungsappelle" zu festen Daten – Eilantrag mind. 2 Wochen vorher.
- Schutzschrift beim BVerwG sichert Fristen und legt den Sachverhalt vorab dar.
- Akteneinsicht in Vergleichsbeurteilungen erfolgt anonymisiert – Auswahlvermerk ist häufig der Schlüssel.
- Erforderlich: konkrete Plausibilitätsfehler benennen, nicht nur "ungerecht".

## Mustertexte

**Schutzschrift beim BVerwG:**
"An das Bundesverwaltungsgericht, Wehrdienstsenat. Vorsorgliche Schutzschrift im Konkurrentenstreit gegen die voraussichtliche Beförderung von [Name] zum [Dienstgrad] zum [Datum]. Mein Mandant beabsichtigt, gegen die Auswahlentscheidung Beschwerde nach § 1 WBO einzulegen und Eilantrag § 21 WBO zu stellen. Anlagen: 1. Konkurrentenmitteilung. 2. Beurteilung Mandant. 3. Vorläufige Rügen."

**Eilantrag § 21 WBO:**
"Es wird beantragt, im Wege der einstweiligen Anordnung die Antragsgegnerin zu verpflichten, den Dienstposten [Bezeichnung] / die Beförderung zu [Dienstgrad] nicht vorzunehmen, bis über die Beschwerde des Antragstellers vom [Datum] rechtskräftig entschieden ist. Anordnungsgrund: am [Datum] steht der Beförderungsappell mit Ernennung des Mitbewerbers an. Anordnungsanspruch: fehlerhafte Auswahlentscheidung wegen [...]."

## Typische Fehler

- Konkurrentenmitteilung nicht erkannt – Frist verstreicht.
- Schutzschrift fehlt – Eilantrag kommt zu spät.
- Plausibilitätsfehler nicht konkret benannt – Antrag scheitert.
- Falsches Gericht (TDG statt BVerwG bei höherrangiger Maßnahme).
- Anordnungsgrund nicht ausreichend (drohende Beförderung muss konkret terminiert sein).

## Quellen Stand 06/2026

- Art. 33 II GG.
- WBO §§ 1, 6, 17, 21 – Volltext gesetze-im-internet.de.
- §§ 27, 28 SG; SLV – Volltexte gesetze-im-internet.de.
- BVerwG Wehrdienstsenate – ständige Rechtsprechung zum Konkurrentenrechtsschutz (Az. nach Verifikation).
- BVerfG zu effektivem Rechtsschutz vor Beförderung – ständige Rechtsprechung; Volltexte bundesverfassungsgericht.de.
- VwGO §§ 80a, 99, 123 entsprechend.

---

## Skill: `einsatzunfall-wehrdienstbeschaedigung`

_Einsatzunfall Wehrdienstbeschädigung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG im Bundeswehrrecht..._

# Einsatzunfall und Wehrdienstbeschädigung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Einsatzunfall und Wehrdienstbeschädigung
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Worum geht es konkret

Der Einsatzunfall ist eine besonders qualifizierte Form der Wehrdienstbeschädigung: Schädigung während eines besonderen Auslandseinsatzes oder einer gleichgestellten Verwendung (§ 81a SVG). Folge sind höhere Leistungen, insbesondere eine einmalige Entschädigung nach Einsatzversorgungs-Verbesserungsgesetz und besondere Berufsförderungsansprüche. Der Skill ordnet die Voraussetzungen, dokumentiert die Tatfeststellung und führt durch das Verwaltungsverfahren.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Welcher konkrete Einsatz (KFOR, EUFOR, Resolute Support, Sea Guardian, EUTM, sonstige Mission)?
- Welche Verwendung (Truppe, Kontingent, Beobachter, Stab, NATO/EU)?
- Was war das auslösende Ereignis – Gefecht, Anschlag, Unfall, dienstliche Tätigkeit im Lager?
- Sofortige Meldung an Vorgesetzten erfolgt?
- Welche ärztlichen Befunde liegen vor (truppenärztlich, im Einsatzland, in Deutschland)?
- Ist die Verwendung als besonderer Einsatz nach § 63c SG anerkannt?

## Rechtlicher Rahmen

- § 81 SVG: Wehrdienstbeschädigung (Grundtatbestand).
- § 81a SVG: Einsatzunfall – Schädigung durch oder bei einem besonderen Auslandseinsatz (§ 63c SG) oder einer dem Wehrdienst eigentümlichen Gefahr.
- § 81e SVG: Einmalige Entschädigung – bis 150.000 Euro bei GdS 50 v.H. und mehr (Einsatzversorgungs-Verbesserungsgesetz).
- § 81b SVG: Erweiterte Heilbehandlung und Pflege.
- § 63c SG: Definition des besonderen Auslandseinsatzes.
- Bundestagsmandat: Anlage zur jeweiligen Bundestagsbeteiligung – Voraussetzung für Anerkennung als besonderer Einsatz.
- §§ 102 ff. SVG: Verwaltungsverfahren.
- Versorgungsmedizinische Grundsätze (VMG).
- Beweismaß: Vollbeweis Schädigung, Wahrscheinlichkeit der Kausalität.

## / Schritt für Schritt

1. **Einsatzstatus klären.** Bundestagsmandat? Einsatz nach § 63c SG anerkannt? OPLAN/Einsatzbefehl beibringen.
2. **Ereignisdokumentation.** Unfallmeldung, Funkspruch, Sanitätsbuch, Patientenkarte, Kameradenbericht, ggf. JET (Joint Operations Centre Logs).
3. **Medizinische Befundkette.** Erstversorgung Einsatzland → Repatriierung → Bundeswehrkrankenhaus → Reha → Privatarzt.
4. **Kausalität herausarbeiten.** Direkte Kampfhandlung? "Eigentümliche Gefahr" des Einsatzlandes (Tropen, Sprengfallen, Verkehr, psychische Belastung)?
5. **Antrag auf Anerkennung als Einsatzunfall** beim BAPersBw mit allen Belegen.
6. **Begutachtung** durch versorgungsmedizinische Stelle; eigene Stellungnahme/Gegengutachten.
7. **GdS-Festsetzung** – ab 50 v.H. einmalige Entschädigung § 81e SVG; gestaffelt.
8. **Berufsförderung.** §§ 4 ff. SVG i.V.m. einsatzversorgungsrechtlichen Regelungen.
9. **Widerspruch** § 70 ff. VwGO entsprechend – 1 Monat. Klage Sozialgericht/Verwaltungsgericht.

## Trade-off-Matrix

| Konstellation | Strategie A | Strategie B |
| --- | --- | --- |
| Klare Kampfverletzung | Sofortantrag, hohe einmalige Entschädigung | Eilentscheidung beantragen |
| Krankheit nach Tropenaufenthalt | Tropenmedizinisches Gutachten | Indizien aus Einsatzberichten |
| PTBS Jahre später | Belastungsanamnese, Zeugen, Tagebücher | Spezialgutachten Psychotraumatologie |
| Unfall im Lager / nicht Kampfhandlung | "Eigentümliche Gefahr" begründen | reguläre WDB statt Einsatzunfall |

## Praxistipps

- Bundestagsmandate sind nicht statisch – ein Einsatz kann anerkannt oder nicht anerkannt sein. Aktuelle Mandatsliste prüfen.
- "Eigentümliche Gefahr" reicht aus – kein Direkttreffer erforderlich. Verkehrsunfall auf Patrouille, Malariainfektion, Hitzschlag im Lager fallen darunter.
- Einmalige Entschädigung § 81e SVG ist neben Rente und Heilbehandlung möglich.
- Bei kritischen Diagnosen Reha- und Pflegeleistungen früh beantragen (§ 81b SVG).
- Vertraulichkeit der Einsatzberichte: Schwärzungen sind häufig – beantragen Sie nur die relevanten Teile.

## Mustertexte

**Antrag auf Anerkennung als Einsatzunfall:**
"Beim BAPersBw beantrage ich die Anerkennung eines Einsatzunfalls nach § 81a SVG sowie Leistungen nach § 81e SVG. Sachverhalt: Mein Mandant war im Rahmen des Einsatzes [Bezeichnung] vom [Datum bis] in [Einsatzland] eingesetzt. Am [Datum] erlitt er [Diagnose] durch [Ereignis]. Beweismittel: 1. Einsatzbefehl/OPLAN-Auszug, 2. Sanitätsbuch (Anl. 2), 3. Berichte BwKrhs [...] (Anl. 3–5), 4. Zeugen Stbsf [Name], Hptm [Name]."

**Widerspruch gegen Ablehnung des Einsatzunfallstatus:**
"Der Bescheid ordnet die Schädigung als reguläre WDB ein. Tatsächlich liegt ein Einsatzunfall im Sinne des § 81a SVG vor: 1. Bundestagsmandat [Drucksache] erfasste die Verwendung. 2. Die Schädigung ist eine eigentümliche Gefahr des Einsatzes, weil [...]. 3. Die Versorgungsmedizinischen Grundsätze begründen einen GdS von [%]."

## Typische Fehler

- Reguläre WDB beantragen, obwohl Einsatzunfall einschlägig wäre.
- Bundestagsmandat nicht beigebracht – Anerkennung als besonderer Einsatz scheitert.
- Kausalität nur behauptet, nicht mit Zeugen/Berichten belegt.
- Einmalige Entschädigung § 81e SVG nicht ausdrücklich beantragt.
- GdS unter 50 v.H. akzeptiert, obwohl Folgeschäden den Wert erhöhen.

## Quellen Stand 06/2026

- SVG §§ 81, 81a, 81b, 81e – Volltext gesetze-im-internet.de.
- SG § 63c – Volltext gesetze-im-internet.de.
- Bundestagsmandate – Drucksachen des Deutschen Bundestages, einsehbar bei bundestag.de.
- Versorgungsmedizinische Grundsätze – BMAS.
- BSG/BVerwG zu § 81a SVG – ständige Rechtsprechung; Az. nach Verifikation.

---

## Skill: `gehorsam-befehl-und-rechtswidriger-befehl`

_Gehorsam Befehl und rechtswidriger Befehl: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG im Bundeswehr..._

# Gehorsam, Befehl und rechtswidriger Befehl

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Gehorsam, Befehl und rechtswidriger Befehl
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Worum geht es konkret

Der Soldat schuldet nach § 11 SG Gehorsam gegenüber dienstlichen Befehlen seines Vorgesetzten. Der Befehl ist eine Anweisung zu einem bestimmten Verhalten, die mit dem Anspruch auf Gehorsam erteilt wird (§ 2 Nr. 2 WStG). Die Gehorsamspflicht endet jedoch dort, wo Strafrecht, Menschenwürde oder dienstlicher Zweck verletzt würden. Der Skill ordnet die Konstellation ein und führt durch Remonstration, Befehlsverweigerung und Verteidigung in einem etwaigen WStG- oder WDO-Verfahren.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Wortlaut des Befehls? Mündlich oder schriftlich, vor Zeugen?
- Wer ist Vorgesetzter (truppendienstlich, fachlich, kraft Dienstgrad)?
- Welcher Befehlsinhalt – Routine, gefährlich, ehrverletzend, möglicherweise strafrechtsrelevant?
- Bereits ausgeführt, verweigert, remonstriert?
- Liegt ein Strafverfahren nach WStG oder ein WDO-Vorgang vor?
- Gibt es Einsatzbefehle (Auslandseinsatz, Mandatsgrenzen)?

## Rechtlicher Rahmen

- § 11 I SG: Pflicht zum Gehorsam – Befehle nach besten Kräften vollständig, gewissenhaft und unverzüglich ausführen.
- § 11 I 3 SG: Gehorsam entfällt, wenn Menschenwürde verletzt würde oder Befehl nicht zu dienstlichen Zwecken erteilt ist.
- § 11 II SG: Strafrechtliche Grenze – kein Gehorsam, wenn Ausführung eine Straftat begehen würde, die der Soldat erkennt oder nach den ihm bekannten Umständen offensichtlich ist.
- § 2 Nr. 2, §§ 19–22 WStG: Begriff des Befehls, Ungehorsam, Gehorsamsverweigerung, Befehl als Rechtfertigung/Entschuldigung.
- § 5 WStG: Handeln auf Befehl als Schuldausschließungsgrund.
- §§ 32 ff. WDO: Disziplinarverfahren bei Ungehorsam.
- § 22 WBO: Pflicht zur Befehlsausführung trotz Beschwerde (aufschiebende Wirkung nur ausnahmsweise).

## / Schritt für Schritt

1. **Befehl präzise rekonstruieren.** Wortlaut, Zeitpunkt, Vorgesetzter, Zeugen, Begleitumstände dokumentieren. Schriftliche Bestätigung verlangen, wenn möglich.
2. **Pflichtenkollision prüfen.** Ist der Befehl
 (a) rechtmäßig und verbindlich,
 (b) rechtswidrig, aber verbindlich (auszuführen mit Beschwerde) oder
 (c) unverbindlich (zu verweigern: Menschenwürde, Strafrecht, fehlender dienstlicher Zweck)?
3. **Remonstrieren.** Bei Zweifeln: Bedenken gegenüber dem Vorgesetzten melden, Bestätigung verlangen, Rechtsgrundlage erfragen. Pflicht zur Remonstration ergibt sich aus § 11 II SG analog und der ständigen Rechtsprechung der Truppendienstkammern und Wehrdienstsenate.
4. **Entscheidung treffen.**
 - Bei strafrechtlicher Offensichtlichkeit: Verweigerung, schriftliche Begründung.
 - Bei nicht offensichtlicher Strafrechtswidrigkeit: Ausführung und parallele Beschwerde.
 - Bei Menschenwürdeverstoß: Verweigerung, sofortige Meldung an höhere Stelle.
5. **Beweissicherung.** Zeugen benennen, Sprechfunkmitschnitt, Befehlsprotokoll, eigene Notiz mit Datum/Uhrzeit.
6. **Rechtsbeistand.** Bei Strafanzeige oder WDO-Vorgang sofort Verteidiger einschalten; § 90 WDO Anwesenheitsrecht.

## Trade-off-Matrix

| Situation | Befehl ausführen | Befehl verweigern |
| --- | --- | --- |
| Routinebefehl, leichte Zweifel | Ja, Beschwerde im Nachgang | Risiko § 19 WStG Ungehorsam |
| Mögliche Körperverletzung | Nur nach Remonstration | Bei Offensichtlichkeit: Pflicht zu verweigern |
| Menschenwürdeverletzung | Nie | Pflicht zur Verweigerung § 11 SG |
| Auslandseinsatz mandatswidrig | Sofortige Meldung an höhere Ebene | Verweigerung mit Berufung auf Mandatsgrenzen |

## Praxistipps

- Remonstrieren bedeutet nicht ablehnen. Es ist ein gestuftes Verfahren: Bedenken äußern, Befehl wiederholen lassen, dann erst Verweigerung.
- Befehl ist nicht nur das laute "Befehl!", sondern jede dienstliche Anweisung mit Befolgungsanspruch – auch per E-Mail oder Funkspruch.
- Beweislast: Der Vorgesetzte trägt die Beweislast für die Erteilung des Befehls und seine Dienstlichkeit; der Soldat für entlastende Umstände (§§ 19 ff. WStG).
- Wer einen offensichtlich strafrechtsrelevanten Befehl ausführt, kann sich nicht auf § 5 WStG berufen, wenn die Rechtswidrigkeit erkennbar war (Nürnberger Tradition – Befehlsnotstand kein Generalfreibrief).
- Im Auslandseinsatz Mandatsgrenzen (Bundestagsbeschluss, Rules of Engagement) kennen – Befehl außerhalb des Mandats ist nicht verbindlich.

## Mustertexte

**Remonstration mündlich vor Zeugen:**
"Herr [Dienstgrad], ich melde Bedenken gegen den Befehl, [...] zu tun. Ich sehe die Gefahr, dass dadurch [§ ... StGB / Menschenwürdeverstoß / Mandatsgrenze] verletzt würde. Bitte bestätigen Sie den Befehl unter Angabe der Rechtsgrundlage."

**Schriftliche Befehlsverweigerung:**
"Den am [Datum/Uhrzeit] durch Hauptmann [Name] erteilten Befehl, [...], habe ich nicht ausgeführt. Grund: Der Befehl verletzt nach meiner aufgrund der bekannten Umstände erkennbaren Beurteilung [§ ... StGB / die Menschenwürde des Betroffenen / das Einsatzmandat]. Ich berufe mich auf § 11 II SG."

## Typische Fehler

- Befehl pauschal "rechtswidrig" nennen ohne konkrete Norm – führt zur disziplinaren Festlegung als unbegründete Verweigerung.
- Remonstration unterlassen – wer ohne vorherige Remonstration verweigert, riskiert § 19 WStG, auch wenn der Befehl im Ergebnis rechtswidrig war.
- Ausführen und nachträglich Beschwerde nach WBO einlegen, wenn der Befehl strafrechtsrelevant war – schützt nicht vor eigener Strafbarkeit.
- Mündliche Befehlserteilung ohne Zeugen ungesichert lassen – Beweisnot.
- Berufung auf "Gewissensnot" ohne KDV-Antrag bei generalisierter Ablehnung jeder Befehlsausführung.

## Quellen Stand 06/2026

- § 11 SG, §§ 19–22 WStG, § 5 WStG – Volltext gesetze-im-internet.de.
- BVerwG Wehrdienstsenate – ständige Rechtsprechung zu Remonstration, offensichtlicher Strafrechtswidrigkeit und § 11 II SG (Az. nur nach Verifikation in BVerwG-Entscheidungsdatenbank).
- BVerfG zum Gewissensschutz von Soldaten – ständige Rechtsprechung (Volltexte: bundesverfassungsgericht.de).
- Truppendienstgerichte – Rechtsprechung in WDO-Verfahren (Az. nur generisch; konkrete Fundstellen nur nach Live-Recherche).
- Bundeswehr-interne Vorschriften (ZDv, A-Vorschrift) nur nach Mandantenvorlage, nicht aus Modellwissen.

---

## Skill: `kriegsdienstverweigerung-verfahren`

_Kriegsdienstverweigerung Verfahren: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG im Bundeswehrrecht W..._

# Kriegsdienstverweigerung – Verfahren

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Kriegsdienstverweigerung – Verfahren
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Worum geht es konkret

Das Recht auf Kriegsdienstverweigerung aus Gewissensgründen ist in Art. 4 III GG verankert. Soldaten, Wehrpflichtige, Reservisten und Bewerber können das Recht in Anspruch nehmen. Verfahren und Voraussetzungen regelt das Kriegsdienstverweigerungsgesetz (KDVG). Anerkannte Verweigerer leisten Dienst nach dem Zivildienstgesetz (für Wehrpflichtige in einer Spannungs-/Verteidigungslage) oder werden aus dem Wehrdienst entlassen (Soldaten). Der Skill ordnet Antragsweg, Gewissensprüfung und Folgen.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Aktueller Status (Wehrpflichtiger, Reservist, Soldat auf Zeit, Berufssoldat, FWDL)?
- Beweggründe (religiös, ethisch, weltanschaulich, politisch-moralisch)?
- Bisherige Vorgänge (frühere Anträge, Verfahren beim Bundesamt für Familie und zivilgesellschaftliche Aufgaben/BAFzA bzw. Vorgängerbehörden)?
- Ist die Verweigerung absolut oder bezogen auf einen bestimmten Konflikt (sog. Situationsverweigerung)?
- Welche Frist (zB Zeitsoldat während des Wehrdienstverhältnisses, Bewerber vor Einstellung)?
- Welche dienstliche Lage (Heranziehung, Einsatzbefehl, Übung)?

## Rechtlicher Rahmen

- Art. 4 III GG: Niemand darf gegen sein Gewissen zum Kriegsdienst mit der Waffe gezwungen werden.
- KDVG: Verfahren der Anerkennung als Kriegsdienstverweigerer.
- § 1 KDVG: Recht der Verweigerung.
- § 2 KDVG: Schriftlicher Antrag, Begründung, persönliche Anhörung.
- § 5 KDVG: Anerkennungsverfahren – Anhörung durch die zuständige Stelle.
- § 7 KDVG: Wirkung der Anerkennung – Entlassung des Soldaten oder Wegfall der Heranziehung.
- BVerfGE zu Art. 4 III GG: Gewissensentscheidung ist verbindlich, wenn ernsthaft, sittlich begründet und absolut.
- § 1 WPflG i.V.m. KDVG: Wehrpflichtige.
- § 1 SG i.V.m. KDVG: Soldaten und Reservisten.

## / Schritt für Schritt

1. **Statusbestimmung.** Antragsweg differenziert je nach Status. Soldat: Antrag beim Vorgesetzten, weiter ans BAFzA / Wehrdienstrechtsamt. Reservist: vor Heranziehung. Wehrpflichtiger: bei Musterung oder im Wehrdienst.
2. **Antragsschrift.** Schriftlich, persönlich verfasst, Begründung der Gewissensentscheidung. Lebensgeschichte, prägende Erfahrungen, ethische/religiöse Grundlagen, Folgen für eigene Lebensführung.
3. **Beweismittel.** Zeugenangaben, Zertifikate (Friedensdienst, religiöse Tätigkeit), persönliche Korrespondenz.
4. **Anhörung.** Persönliche Anhörung Pflicht. Recht auf Beistand. Fragen zur Genese der Entscheidung, Glaubhaftigkeit, Konsistenz.
5. **Bescheid abwarten.** Bei Anerkennung: Entlassung des Soldaten (§ 7 KDVG), Wegfall der Heranziehung des Reservisten / Wehrpflichtigen.
6. **Rechtsbehelfe.** Widerspruch, Klage Verwaltungsgericht (KDVG-Verfahren ist Verwaltungsverfahren, kein WBO-Verfahren).
7. **Folgen für Versorgung.** Anerkennung schließt Heilfürsorge und WDB-Ansprüche aus dienstzeitabhängigen Verlusten ein – Einzelfall prüfen.

## Trade-off-Matrix

| Konstellation | Antrag stellen | Alternative |
| --- | --- | --- |
| Reine Gewissensnot | Anerkennung KDVG | Befehlsverweigerung im Einzelfall (§ 11 II SG) |
| Situationsverweigerung | KDVG nicht statthaft (Rspr. eng) | Versetzung, Entlassung auf Antrag |
| Zeitsoldat vor Vertragsende | Anerkennung + Entlassung | Antrag § 55 SG |
| Reservist heranziehbar | KDVG vor Heranziehung | Widerspruch gegen Heranziehung |

## Praxistipps

- Antragsbegründung muss "absolute" Verweigerung dokumentieren – Situationsablehnung führt häufig zur Ablehnung.
- BVerfG: Innere Konsistenz und Glaubhaftigkeit reichen – kein "Beweis" des Gewissens, aber überzeugende Darlegung.
- Bei Soldaten ist die Wirkung primär die Entlassung; während des Verfahrens grundsätzlich kein Anspruch auf Dienstbefreiung – aber Einsatzbefreiung möglich (Einzelfall).
- Bei Soldaten auf Zeit kann Rückforderung der Ausbildungskosten drohen – Skill "ausbildung-studium-bundeswehr-rueckforderung-ausbildungskosten" parallel prüfen.
- Anhörung schriftlich vorbereiten, ggf. Probeanhörung mit Anwalt durchgehen.

## Mustertexte

**KDV-Antrag eines Soldaten:**
"Hiermit erkläre ich gemäß Art. 4 III GG, § 1 KDVG, dass ich den Kriegsdienst mit der Waffe aus Gewissensgründen verweigere. Persönliche Begründung: 1. Lebensgeschichte: [...]. 2. Entwicklung der Gewissensentscheidung: [...]. 3. Konsequenzen für meine Lebensführung: [...]. 4. Bekenntnisse / Mitgliedschaften: [...]. Ich beantrage die Anerkennung als Kriegsdienstverweigerer sowie meine Entlassung aus dem Soldatenverhältnis (§ 7 KDVG)."

**Beistand-Vollmacht für Anhörung:**
"Ich bevollmächtige Herrn/Frau [Name] als Beistand zur Teilnahme an der mündlichen Anhörung nach § 5 KDVG. Der Beistand ist zur Akteneinsicht und zur Stellung von Anträgen befugt."

## Typische Fehler

- Antragsschrift formelhaft / Textbaustein – Anhörung deckt Unglaubhaftigkeit auf.
- Situationsverweigerung als KDV – wird regelmäßig abgelehnt.
- Folgen Versorgung/Ausbildungskostenrückforderung nicht bedacht.
- Anhörung ohne Beistand – ungeschickte Antworten begründen Ablehnung.
- KDV als reine Strategie zur Entlassung – Glaubhaftigkeit wird kritisch geprüft, Risiko Rückforderung.

## Quellen Stand 06/2026

- Art. 4 III GG.
- KDVG – Volltext gesetze-im-internet.de.
- BVerfG zu Art. 4 III GG – ständige Rechtsprechung; Volltexte bundesverfassungsgericht.de.
- BVerwG zur Gewissensentscheidung – ständige Rechtsprechung (Az. nach Verifikation).
- BAFzA – Verwaltungspraxis und Verfahrensmerkblatt (bafza.de).

## Spezialplugin

Für KDV-Fälle ab 2026, insbesondere Antrag über BAPersBw, § 13 KDVG n. F., aktive Soldaten, Reservisten, Untätigkeit und Gewissensbegründung, vorrangig das Spezialplugin `kriegsdienstverweigerung-wehrdienst` verwenden. Dieser Skill bleibt als Routing im Bundeswehrrecht erhalten.

---

## Skill: `nebentaetigkeit-geschenkannahme-personalakte`

_Nebentätigkeit Geschenkannahme Compliance: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG im Bundeswehr..._

# Nebentätigkeit und Geschenkannahme – Compliance des Soldaten

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Nebentätigkeit und Geschenkannahme – Compliance des Soldaten
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Worum geht es konkret

Soldaten dürfen Nebentätigkeiten nur eingeschränkt und nur nach vorheriger Genehmigung ausüben (§ 20 SG). Die Annahme von Belohnungen, Geschenken und sonstigen Vorteilen ist nach § 19 SG grundsätzlich verboten. Der Skill ordnet die Genehmigungspflichten, prüft Versagungsgründe, dokumentiert Compliance-Verstöße und schützt vor strafrechtlichen Konsequenzen (§§ 331 ff. StGB Vorteilsannahme/Bestechlichkeit).

## Wann dieses Modul hilft / Kaltstart-Fragen

- Welche Tätigkeit (selbständig, abhängig, ehrenamtlich)?
- Art der Vergütung, Zeitumfang, dienstlicher Zusammenhang?
- Geschenk: von wem, Anlass, Wert?
- Bereits Genehmigung erteilt oder versagt?
- Verfahren eingeleitet (Anhörung, Strafanzeige § 331 ff. StGB)?
- Funktion des Soldaten (Beschaffung, Auftragsvergabe, militärischer Dienst)?

## Rechtlicher Rahmen

- § 19 SG: Verbot der Annahme von Belohnungen, Geschenken und sonstigen Vorteilen in Bezug auf das Amt – Zustimmung der obersten Dienstbehörde erforderlich.
- § 20 SG: Nebentätigkeiten – Genehmigungspflicht; Versagungsgründe.
- § 21 SG: Anzeigepflichtige Nebentätigkeiten.
- § 21a SG: Nebentätigkeit nach Beendigung des Dienstverhältnisses (Karenzzeit).
- §§ 331–337 StGB: Vorteilsannahme und Bestechlichkeit von Amtsträgern.
- Vergaberecht: Schnittstelle BAAINBw / Beschaffung.
- ZDv A-2614/1 (Nebentätigkeit) – nur nach Vorlage.
- BHO-Geschenkrichtlinien.

## / Schritt für Schritt

1. **Tätigkeit oder Geschenk klassifizieren.** Selbständig, Anstellung, Ehrenamt, einmalige Aufmerksamkeit, regelmäßige Zuwendung?
2. **Genehmigungsbedarf prüfen.** Pflicht-Anzeige oder Pflicht-Genehmigung?
3. **Versagungsgründe nach § 20 SG prüfen:**
 - Wesentliche Beeinträchtigung dienstlicher Pflichten,
 - Konkurrenz zum Dienstherrn,
 - Beeinträchtigung der Unparteilichkeit,
 - Sittenwidrigkeit.
4. **Schriftlicher Antrag** mit Tätigkeitsbeschreibung, Zeitaufwand, Vergütung, Auftraggeber.
5. **Geschenkannahme:** Sofortmeldung an Vorgesetzten, Schriftliche Anzeige, ggf. Rückgabe oder Hinterlegung.
6. **Compliance-Folgen.** Strafanzeige (§ 331/332 StGB), WDO-Verfahren parallel.
7. **Karenzzeit nach Dienstende** (§ 21a SG) für Beschaffungs- und Führungspositionen.

## Trade-off-Matrix

| Situation | Vorgehen |
| --- | --- |
| Bagatelle (Kaffee, Werbeartikel) | Anzeige, ggf. nicht genehmigungspflichtig |
| Einladung Industrievertreter | Schriftliche Genehmigung; alternativ Ablehnung |
| Tätigkeit als Reservist-Berater | Genehmigung mit Auflagen |
| Politisches Mandat | § 36 SG (Wahlrecht) – Sonderregelung |
| Nach Pension Beschaffung-Beratungsfirma | § 21a SG-Karenzzeit prüfen |

## Praxistipps

- Geschenkrückgabe innerhalb von 24 Stunden plus schriftliche Meldung – schützt vor § 331 StGB.
- Geringfügigkeitsgrenze nicht justiziabel im Sinne von "geringer Schaden" – Compliance-Regel: bei Zweifel anzeigen.
- Bei Beschaffungspositionen besondere Aufmerksamkeit – Vermutungsregel der Befangenheit.
- Vortrag bei Industriekonferenz nur mit Genehmigung; Honorar in Bundeskasse oder mit Auflagen.
- Karenzzeit nach Dienstende kann 5 Jahre erreichen (Schnittstelle § 105 BBG entsprechend).

## Mustertexte

**Genehmigungsantrag Nebentätigkeit:**
"Ich beantrage Genehmigung folgender Nebentätigkeit: 1. Art: [...]. 2. Auftraggeber: [...]. 3. Zeitaufwand: [...] Std/Monat. 4. Vergütung: [...] EUR. 5. Dienstlicher Bezug: keiner / [Erklärung]. 6. Beeinträchtigung dienstlicher Aufgaben: ausgeschlossen, weil [...]. Es wird zugesichert, dass Versagungsgründe nach § 20 III SG nicht vorliegen."

**Geschenkanzeige:**
"Hiermit zeige ich an, dass mir am [Datum] von [Person/Firma] anlässlich [...] ein [Gegenstand/Geldwert] im geschätzten Wert von [...] EUR angeboten wurde. Ich habe die Annahme [abgelehnt / vorbehaltlich der Genehmigung entgegengenommen]. Ich beantrage Entscheidung nach § 19 SG."

## Typische Fehler

- "Kleine Aufmerksamkeit" formlos angenommen – § 331 StGB-Risiko.
- Nebentätigkeit ohne Antrag aufgenommen – Disziplinarmaßnahme.
- Karenzzeit nach Dienstende ignoriert – Versorgungseingriff möglich.
- Industriekonferenz-Honorar versteckt – Compliance-Verstoß.
- Vermengung von zulässiger ehrenamtlicher Tätigkeit mit anzeigepflichtiger Nebentätigkeit.

## Quellen Stand 06/2026

- §§ 19, 20, 21, 21a SG – Volltext gesetze-im-internet.de.
- §§ 331–337 StGB – Volltext gesetze-im-internet.de.
- BVerwG Wehrdienstsenate – ständige Rechtsprechung zu § 20 SG.
- BGH-Rechtsprechung zur Amtsträgereigenschaft des Soldaten – ständige Rechtsprechung.
- ZDv A-2614/1 (Nebentätigkeit) – nur nach Vorlage durch Mandanten.

---

## Skill: `politische-betaetigung-maessigung-neutralitaet`

_Politische Betätigung Mäßigung Neutralität: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG im Bundesweh..._

# Politische Betätigung – Mäßigungsgebot und Neutralität

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Politische Betätigung – Mäßigungsgebot und Neutralität
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Worum geht es konkret

§ 15 SG bindet den Soldaten an ein Mäßigungs- und Neutralitätsgebot. Während des Dienstes ist jede Werbung für oder gegen politische Richtungen untersagt; außerhalb des Dienstes hat sich der Soldat so zu mäßigen, dass das Vertrauen in seine Pflichterfüllung und die Achtung in seiner dienstlichen Stellung nicht ernsthaft beeinträchtigt werden. Der Skill ordnet die Grenze zwischen Meinungsfreiheit (Art. 5 GG) und § 15 SG, insbesondere im Social-Media-Zeitalter.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Welche Äußerung (mündlich, schriftlich, Social Media, Versammlungsteilnahme)?
- Ort und Zeit (im Dienst, außer Dienst, Uniform getragen?)?
- Adressatenkreis (geschlossener Kreis, halböffentlich, öffentlich, viral)?
- Politische Richtung (verfassungswidrige Parteien? Gewaltverherrlichung? Diskriminierung?)?
- Liegt bereits ein Hinweis, eine Anhörung, ein Vorgang vor?
- Gibt es Schnittstellen zu § 7 SG (Treuepflicht), § 8 SG (Demokratie), § 17 SG (Achtungspflicht)?

## Rechtlicher Rahmen

- § 15 I SG: Politische Betätigung im Dienst – Verbot.
- § 15 II SG: Mäßigungsgebot außer Dienst – Vertrauensbeeinträchtigung verboten.
- § 7 SG: Treuepflicht zur fdGO.
- § 8 SG: Eintreten für demokratische Grundordnung.
- § 17 SG: Achtungs- und Vertrauenswürdigkeit.
- Art. 5 GG: Meinungs- und Pressefreiheit – Grundrechtsausstrahlung.
- BVerfG zu Soldaten und politischer Meinungsfreiheit – ständige Rechtsprechung zur Verhältnismäßigkeit.
- BVerwG Wehrdienstsenate – ständige Rechtsprechung zur Auslegung von § 15 SG, häufig zugespitzt bei Social-Media-Posts und Reichsbürger-/Extremismusnähe.

## / Schritt für Schritt

1. **Äußerung präzise dokumentieren.** Wortlaut, Datum, Plattform, Reichweite, Uniform, Dienstbezug.
2. **Kontext einordnen.** Dienstlicher oder außerdienstlicher Rahmen? Geschlossener oder offener Kreis?
3. **Inhaltsprüfung.**
 - Werbung für politische Richtung im Dienst → § 15 I SG.
 - Außer Dienst: Vertrauensbeeinträchtigung? Achtungswürdigkeit § 17 SG?
 - Treuepflicht § 7/8 SG bei verfassungswidrigen oder extremistischen Inhalten.
4. **Verfahrensstufe.** Innerdienstliche Belehrung – einfache Disziplinarmaßnahme – gerichtliches Disziplinarverfahren – ggf. Entlassung nach § 55 V SG.
5. **Verteidigungsbausteine.**
 - Art. 5 GG-Würdigung,
 - keine Identifizierbarkeit als Soldat,
 - bloße Faktendarstellung statt politischer Werbung,
 - Rückzug, Löschung, Distanzierung.
6. **Anhörung.** Schweigen bis Akteneinsicht.
7. **Bei Extremismusverdacht** parallel: sicherheitsrechtliche Verfahren, MAD-Beteiligung, Sicherheitsüberprüfung (SÜG).

## Trade-off-Matrix

| Äußerung | Risiko |
| --- | --- |
| Wahlplakat im Garten, ohne Uniform | gering |
| Social-Media-Post mit Foto in Uniform | hoch |
| Teilnahme an Demonstration mit fdGO-feindlichem Charakter | sehr hoch (§§ 7, 8 SG) |
| Like / Share eines extremistischen Beitrags | mittel-hoch (Indiz für Gesinnung) |

## Praxistipps

- Uniform bei privater politischer Betätigung tabu – Vertrauensbeeinträchtigung praktisch immer angenommen.
- Reichweite ist wichtig: 5000 Follower wirken wie eine Versammlung – Mäßigungsgebot greift.
- Distanzierung und Löschung können in der Verteidigung helfen, beseitigen aber nicht die Tatbestandsverwirklichung.
- Mitgliedschaft in extremistischen Organisationen → § 7 SG + § 8 SG, oft Entlassungsgrund.
- Whistleblowing zu Missständen – andere Bewertung: § 13 SG Wahrheitspflicht und § 14 SG Verschwiegenheit, ggf. Wehrbeauftragter (Art. 45b GG).

## Mustertexte

**Stellungnahme zur Anhörung:**
"Zur Anhörung vom [Datum] nehme ich wie folgt Stellung: Die in Bezug genommene Äußerung erfolgte außerhalb des Dienstes, ohne Uniform und ohne dienstlichen Bezug. Sie ist von der Meinungsfreiheit aus Art. 5 GG gedeckt. Eine Vertrauensbeeinträchtigung iSd § 15 II SG liegt nicht vor, weil [...]. Hilfsweise: Der Mandant hat die Äußerung am [Datum] entfernt und sich distanziert."

**Beratungshinweis an Soldatenmandant:**
"Ich rate dringend: 1. Keine politischen Posts in Uniform oder mit Bundeswehr-Bezug. 2. Keine Teilnahme an Versammlungen, die verfassungswidrigen Inhalten dienen. 3. Likes/Shares zählen als Äußerung. 4. Private Accounts mit dienstlichem Namen vermeiden."

## Typische Fehler

- "Privater Account" als Schutzbehauptung – Reichweite und Identifikationsmerkmale entscheiden.
- Like-/Share-Bagatellisierung – wird als Äußerung gewertet.
- Sofortige Einlassung zur Sache in der Anhörung.
- Verwechslung von Treuepflicht (§ 7 SG) und Mäßigungsgebot (§ 15 SG).
- Distanzierung erst nach Beginn des Verfahrens – Glaubhaftigkeit fraglich.

## Quellen Stand 06/2026

- § 15 SG – Volltext gesetze-im-internet.de.
- Art. 5 GG.
- BVerfG zu Meinungsfreiheit von Soldaten – ständige Rechtsprechung; Volltexte bundesverfassungsgericht.de.
- BVerwG Wehrdienstsenate – ständige Rechtsprechung zu § 15 SG und Social Media (Az. nach Verifikation).
- Wehrbeauftragter – Jahresberichte zu Extremismusfällen (bundestag.de/wehrbeauftragter).
- ZDv A-2630/1 (innere Führung) – nur nach Vorlage.

---

## Skill: `presseaeusserung-meinungsfreiheit-soldat`

_Presseäußerung Meinungsfreiheit Soldat: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG im Bundeswehrrec..._

# Presseäußerung und Meinungsfreiheit des Soldaten

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Presseäußerung und Meinungsfreiheit des Soldaten
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Worum geht es konkret

Der Soldat genießt die Meinungsfreiheit aus Art. 5 GG, die jedoch durch die soldatischen Pflichten aus dem SG eingeschränkt ist: Wahrheitspflicht (§ 13 SG), Verschwiegenheit (§ 14 SG), Mäßigungsgebot (§ 15 SG), Achtungs- und Vertrauenswürdigkeit (§ 17 SG). Presse- und Medienäußerungen sind ein häufiger Konfliktbereich: Interviews, Leserbriefe, Beiträge in Sozialen Medien, Bücher und Podcasts. Der Skill ordnet Genehmigungspflicht, Inhaltsgrenzen und Folgen.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Art der Äußerung (Interview, Buch, Blog, Podcast, Social Media)?
- Inhalt (allgemeinpolitisch, dienstlich, Personal, Geheimschutz, Einsatz)?
- Genehmigung der Dienststelle eingeholt?
- Erkennbarkeit als Soldat (Name, Dienstgrad, Uniform, Truppenteil)?
- Reichweite der Veröffentlichung?
- Schon Reaktion der Dienststelle (Anhörung, Disziplinarvorgang)?

## Rechtlicher Rahmen

- Art. 5 I, II GG: Meinungs- und Pressefreiheit; Schranken der allgemeinen Gesetze.
- § 10 IV SG: Vorgesetzter darf keine politische Werbung ausüben (Spiegelnorm).
- § 13 SG: Wahrheitspflicht in dienstlichen Erklärungen.
- § 14 SG: Verschwiegenheit über dienstliche Angelegenheiten.
- § 15 SG: Mäßigung im politischen Bereich.
- § 17 II SG: Achtungs- und Vertrauenswürdigkeit auch außer Dienst.
- § 18 SG: Genehmigungspflichten für veröffentlichte dienstliche Mitteilungen.
- ZDv A-2630/1 (Innere Führung) – nur nach Vorlage.

## / Schritt für Schritt

1. **Inhalt klassifizieren.** Privatmeinung, dienstliche Information, geheimhaltungspflichtige Information, politisches Statement?
2. **Genehmigungspflicht prüfen.** § 14 SG/§ 18 SG: Dienstliche Angelegenheiten benötigen Zustimmung.
3. **Identifikationsgrad messen.** Klarname, Uniform, Truppenteil – verstärkt Bindung an SG-Pflichten.
4. **Risikoanalyse.** Welche Pflicht ist potenziell verletzt? Mehrere parallel möglich.
5. **Veröffentlichungsmuster.**
 - Wahrheitsgemäß, faktenbasiert, ohne dienstliche Bewertung: in der Regel zulässig.
 - Politische Werbung mit Bundeswehrbezug: hoch riskant.
 - Innerdienstliche Missstände öffentlich: § 14 SG vs. Wehrbeauftragter parallel.
6. **Strategie im Konflikt.** Sofortige Distanzierung, Löschung, Berichtigung. Schriftliche Stellungnahme.
7. **Verfahrensgang.** Disziplinarmaßnahme einfacher Art, gerichtliches Disziplinarverfahren, ggf. WStG bei Geheimschutzverletzung.

## Trade-off-Matrix

| Äußerung | Privater Charakter | Risiko |
| --- | --- | --- |
| Buch über Einsatz, mit BMVg-Freigabe | Genehmigt | gering |
| Interview ohne Freigabe zur Personalpolitik | Dienstlich | hoch |
| Wehrbeauftragten kontaktieren | Geschützt nach WBeauftrG | gering |
| Anonym leaken | Geheimschutz | sehr hoch |

## Praxistipps

- Wer Veröffentlichungen plant: vorab Pressestelle / Vorgesetzten konsultieren, Freigabe schriftlich.
- Wehrbeauftragter (Art. 45b GG) ist privilegierter Kommunikationsweg – schützt vor § 14 SG.
- "Privates" Buch über Einsatz ist regelmäßig dienstlich – § 14 SG erfasst auch Erinnerungen mit Geheimnischarakter.
- Klarname-Posting mit Dienstgrad/Uniformbild: gilt als dienstliche Erklärung, § 13 SG anwendbar.
- Distanzierung nach Veröffentlichung kann Maßnahme mildern, aber nicht ausschließen.

## Mustertexte

**Genehmigungsantrag für Medienauftritt:**
"Sehr geehrte Damen und Herren, ich beabsichtige am [Datum] ein Interview mit [Medium] zum Thema [...]. Inhalt der geplanten Aussagen: [Stichworte]. Ich bitte um Genehmigung nach § 18 SG sowie um Mitteilung etwaiger Auflagen. Beigefügt sind die voraussichtlichen Antworten in schriftlicher Form."

**Stellungnahme zur Anhörung wegen Presseäußerung:**
"Die in Bezug genommene Äußerung erfolgte außerhalb des Dienstes, ohne Uniform und ohne Bezug auf konkrete dienstliche Tatsachen. Sie ist von Art. 5 GG gedeckt. § 14 SG steht nicht entgegen, weil ausschließlich öffentliche, nicht geheimhaltungspflichtige Informationen wiedergegeben wurden. Hilfsweise hat der Mandant die Äußerung am [Datum] entfernt und sich distanziert."

## Typische Fehler

- Dienstliche Inhalte ohne Freigabe öffentlich – auch bei "Privatcharakter" des Mediums.
- Whistleblowing direkt an Presse statt erst Wehrbeauftragten – verliert Schutzwirkung.
- Klarname-Postings mit Dienstgradkennzeichnung unterschätzen.
- Geheimschutzrechtliche Folgen (Strafanzeige § 353b StGB, § 11 SÜG) übersehen.
- Distanzierungserklärung erst nach Bekanntwerden – Glaubhaftigkeit fraglich.

## Quellen Stand 06/2026

- Art. 5 GG.
- §§ 13, 14, 15, 17, 18 SG – Volltext gesetze-im-internet.de.
- BVerfG zu Meinungsfreiheit von Soldaten – ständige Rechtsprechung; Volltexte bundesverfassungsgericht.de.
- BVerwG Wehrdienstsenate zu § 17 SG – ständige Rechtsprechung (Az. nach Verifikation).
- WBeauftrG – Volltext gesetze-im-internet.de.
- § 353b StGB, SÜG – Volltext gesetze-im-internet.de.

---

## Skill: `ptbs-einsatzfolge-reservistendienst`

_PTBS Einsatzfolge Beweisführung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG im Bundeswehrrecht Wehr..._

# PTBS als Einsatzfolge – Beweisführung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: PTBS als Einsatzfolge – Beweisführung
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Worum geht es konkret

Die posttraumatische Belastungsstörung (PTBS) ist eine anerkannte psychische Erkrankung, die durch Extremereignisse im Einsatz ausgelöst werden kann (ICD-10 F43.1, ICD-11 6B40). Im Versorgungsrecht der Bundeswehr ist PTBS als Wehrdienstbeschädigung/Einsatzunfall anerkannt, wenn der Kausalzusammenhang nach den Versorgungsmedizinischen Grundsätzen wahrscheinlich gemacht ist. Der Skill ordnet Diagnose, Belastungsanamnese, Gutachten und Verfahren.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Welche Diagnose (ICD-Code) wurde gestellt? Welche Fachärzte (Bundeswehrkrankenhaus, Vertragsarzt)?
- Welches Belastungsereignis (Gefecht, Anschlag, Tod von Kameraden, Verletzung Zivilist, Unfall, Bedrohung)?
- Zeitliche Lücke zwischen Belastung und Diagnose?
- Sekundärfolgen (Depression, Suchterkrankung, Suizidalität, Erwerbsunfähigkeit)?
- Versicherungsmedizinische Bewertung schon erfolgt? GdS festgesetzt?
- Streitiger Punkt: Diagnose, Kausalität oder GdS-Höhe?

## Rechtlicher Rahmen

- § 81 SVG: Wehrdienstbeschädigung, einschließlich psychischer Schäden.
- § 81a SVG: Einsatzunfall – PTBS als Folge des Einsatzgeschehens.
- § 81e SVG: Einmalige Entschädigung bei GdS 50 v.H. und mehr.
- § 81b SVG: Erweiterte Heilbehandlung, Pflege.
- Versorgungsmedizinische Grundsätze (VMG) – Bewertung psychischer Störungen.
- ICD-10 F43.1, ICD-11 6B40 – diagnostische Standards.
- BSG-Rechtsprechung zur Kausalität psychischer Schäden – ständige Rechtsprechung.
- Schnittstelle § 1 SGB IX (Teilhabe), Heilfürsorge der Bw.

## / Schritt für Schritt

1. **Diagnose sichern.** Facharzt für Psychiatrie/Psychotherapie oder Psychotraumatologie; ICD-Code; Symptomerfassung (Intrusionen, Vermeidung, Hyperarousal, kognitive Veränderungen).
2. **Belastungsanamnese.** Einsatzberichte, OPLAN, Kameradenberichte, eigene Tagebücher, ggf. Funkprotokolle.
3. **Kausalkette aufbauen.** Belastungsereignis -> Symptombeginn -> Chronifizierung. Auch verzögerte PTBS (delayed-onset) anerkannt.
4. **Antrag** beim BAPersBw auf Anerkennung als WDB/Einsatzunfall mit allen Befunden.
5. **Begutachtung.** Vorzugsweise traumatherapeutisch erfahrener Gutachter. Eigene Stellungnahme/Gegengutachten.
6. **GdS-Bewertung.** Nach VMG: Belastungssymptome, soziale/berufliche Funktionseinschränkung.
7. **Berufsförderung und Reha** parallel beantragen (BFD/SVG).
8. **Widerspruch und Klage** bei Unterbewertung (1 Monat).

## Trade-off-Matrix

| Konstellation | Strategie |
| --- | --- |
| Klares Kampfereignis, akute Symptome | Sofortantrag mit Befunden |
| Delayed-onset Jahre später | Belastungsanamnese plus Zeugen plus Tagebücher |
| Komorbide Depression/Sucht | Differenzialdiagnose; Mitverursachung |
| Diagnose abgelehnt | Zweitgutachten; spezialisiertes Zentrum |
| GdS zu niedrig | VMG-konforme Substantiierung |

## Praxistipps

- BVerwG/BSG: Wahrscheinlichkeitsmaß genügt. Vollbeweis nur der Schädigung (Diagnose) und der haftungsbegründenden Tatsache (Einsatzereignis).
- Bundeswehr eigene Trauma-Zentren (BwKrhs Berlin, Hamburg, Westerstede). Gutachten dort ist nicht zwingend bindend.
- Tagebücher und Briefe aus dem Einsatz sind häufig stärkste Beweismittel.
- Suizidversuch oder -tod als Folge der PTBS: Hinterbliebenenversorgung (§ 88 SVG) kann ausgelöst werden.
- BFD-Berufsförderung kombiniert mit Heilfürsorge – Reha vor Rente.

## Mustertexte

**Antrag auf Anerkennung PTBS als Einsatzunfall:**
"Beim BAPersBw beantrage ich die Anerkennung einer PTBS (ICD-10 F43.1) als Einsatzunfall nach § 81a SVG. Belastungsereignis: Einsatz [Bezeichnung], [Datum/Ereignis]. Diagnose: durch Dr. [Name], BwKrhs [Standort], am [Datum]. Symptome: [...]. Beweismittel: 1. ärztlicher Bericht. 2. Einsatzbefehl / OPLAN-Auszug. 3. Kameradenbericht Stbsf [Name]. 4. Tagebuch des Mandanten. Beantragt werden: GdS 50 v.H. nach VMG, einmalige Entschädigung § 81e SVG, Heilbehandlung § 81b SVG."

**Widerspruch gegen Ablehnung:**
"Die Ablehnung stützt sich auf fehlende Kausalität. Tatsächlich genügt nach BSG-Rechtsprechung Wahrscheinlichkeit. Die Symptomatik begann zeitnah zum Einsatzereignis (Sept. [Jahr]). Delayed-onset-PTBS ist nach VMG ausdrücklich anerkannt. Es wird ein traumatherapeutisches Gutachten beantragt; vorgeschlagen werden Dr. [Name] oder das Trauma-Zentrum [...]."

## Typische Fehler

- Belastungsereignis pauschal, nicht datiert/dokumentiert.
- Diagnose von nicht spezialisiertem Arzt – verteidigungsschwach im Widerspruch.
- Komorbide Diagnosen unterschätzen – mindern den GdS.
- VMG-Tabelle nicht zitiert – Bewertung scheint pauschal.
- § 81e SVG-Einmalentschädigung nicht ausdrücklich beantragt.

## Quellen Stand 06/2026

- SVG §§ 81, 81a, 81b, 81e – Volltext gesetze-im-internet.de.
- VMG (Versorgungsmedizinische Grundsätze) – BMAS-Publikation.
- ICD-10 F43.1, ICD-11 6B40 – WHO-Veröffentlichungen.
- BSG zu Kausalität psychischer Schäden – ständige Rechtsprechung.
- BAPersBw – Verwaltungspraxis.
- Bundeswehrkrankenhäuser – Standorte und Fachabteilungen (bundeswehr.de).

---

## Skill: `soldatenbeteiligung-vertrauensperson-sbg`

_Soldatenbeteiligung Vertrauensperson SBG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG im Bundeswehrr..._

# Soldatenbeteiligung – Vertrauensperson nach SBG

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Soldatenbeteiligung – Vertrauensperson nach SBG
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Worum geht es konkret

Das Soldatenbeteiligungsgesetz (SBG) regelt die Mitbestimmung und Mitwirkung der Soldaten durch Vertrauenspersonen. Die Vertrauensperson ist das Pendant zum Personalrat – jedoch mit eingeschränkten Befugnissen wegen der besonderen Stellung des Soldaten. Sie ist zu wesentlichen personalrelevanten und sozialen Entscheidungen anzuhören oder mitbestimmungspflichtig zu beteiligen. Der Skill ordnet Wahl, Aufgaben und Beteiligungstatbestände.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Welche Vertrauenspersonsebene (Kompanie, Bataillon, Regiment, Heimatschutz)?
- Welche Maßnahme steht im Raum (Versetzung, Strafmaßnahme, Beurteilung, Urlaubsregelung, Arbeitszeit)?
- Wurde die Vertrauensperson tatsächlich beteiligt? Anhörung vor Entscheidung?
- Liegt eine Beteiligungspflicht oder ein bloßes Anhörungsrecht vor?
- Ist eine Wahlanfechtung im Raum?
- Steht ein Bezug zu Mobbing, sexueller Belästigung oder Gleichstellung?

## Rechtlicher Rahmen

- §§ 2 ff. SBG: Wahl der Vertrauensperson – allgemeine, freie, gleiche, geheime Wahl in der Kompanie / vergleichbaren Teileinheit.
- § 18 SBG: Allgemeine Aufgaben der Vertrauensperson – Vertretung der Soldaten in Angelegenheiten des Innendienstes, der Ausbildung, der Fürsorge.
- § 23 SBG: Beteiligungsrechte – Mitwirkung in personalrelevanten Entscheidungen (Versetzung, Beurteilung etc.).
- § 24 SBG: Mitbestimmungsrechte in sozialen und innerdienstlichen Angelegenheiten.
- § 25 SBG: Verfahren der Beteiligung – Anhörung vor der Entscheidung.
- § 32 SBG: Wahlanfechtung.
- Schnittstelle Gesamtvertrauenspersonenausschuss beim BMVg.
- SBG/Frauenförderung: Gleichstellungsbeauftragte (§ 19 SoldGleiG).

## / Schritt für Schritt

1. **Beteiligungsebene zuordnen.** Welche Vertrauensperson ist zuständig (Kompanie/Bataillon/höhere Ebene)?
2. **Maßnahme einordnen.**
 - Anhörung (§ 23 SBG)?
 - Mitwirkung (§ 24 SBG)?
 - Mitbestimmung mit Einigungsstellenverfahren?
3. **Verfahrensgang dokumentieren.** Wann wurde die Vertrauensperson informiert, gehört, ggf. zugestimmt oder widersprochen?
4. **Beteiligungsfehler rügen.** Fehlende oder verspätete Beteiligung führt zur Aufhebung der Maßnahme im WBO-Verfahren.
5. **Schutz der Vertrauensperson.** § 9 SBG i.V.m. § 8 BetrVG entsprechend – kein Benachteiligungsverbot.
6. **Wahlanfechtung** §§ 32 ff. SBG – 12 Tage ab Bekanntgabe.
7. **Beschwerdeweg WBO** für Soldaten, deren Recht auf ordnungsgemäße Beteiligung verletzt wurde.

## Trade-off-Matrix

| Maßnahme | Beteiligungspflicht | Rechtsfolge bei Verstoß |
| --- | --- | --- |
| Versetzung mit Standortwechsel | Anhörung § 23 SBG | aufhebbar im WBO |
| Urlaubsplanung | Mitwirkung | korrigierbar |
| Disziplinarmaßnahme einfacher Art | Anhörung individuell | unabhängig vom SBG |
| Ausbildungsplan | Mitbestimmung soziale Angelegenheit | Maßnahme aussetzbar |

## Praxistipps

- Vertrauensperson hat Sitzungsanspruch und Freistellungsrecht. Vorgesetzter darf nicht zur Eile drängen.
- "Beteiligung" ist nicht Zustimmung – aber gehörte Bedenken sind in der Entscheidung zu würdigen.
- Bei strukturellen Problemen (Mobbing, Diskriminierung): Vertrauensperson informieren, ggf. Wehrbeauftragten einschalten.
- Wahlanfechtungsfrist 12 Tage ist sehr kurz – Mandant frühzeitig instruieren.
- Vertrauensperson erscheint in WBO-Verfahren als Beistand möglich (entsprechend § 90 WDO).

## Mustertexte

**Beanstandung fehlender Beteiligung:**
"Die [Maßnahme: Versetzung/Beurteilung/...] vom [Datum] wurde ohne ordnungsgemäße Beteiligung der Vertrauensperson nach § 23 SBG getroffen. Dies ist ein wesentlicher Verfahrensfehler. Ich beantrage daher die Aufhebung der Maßnahme und Wiederherstellung des status quo ante."

**Antrag der Vertrauensperson auf Einsicht in den Vorgang:**
"In der Personalsache des Soldaten [Name] beantrage ich als Vertrauensperson Akteneinsicht nach § 25 SBG, um zur beabsichtigten Maßnahme [...] Stellung nehmen zu können. Eine Stellungnahme erfolgt binnen einer Woche nach Akteneinsicht."

## Typische Fehler

- Beteiligung nach Entscheidung statt vor Entscheidung – Verfahrensmangel.
- Nur informelle Information statt formaler Beteiligung.
- Vertrauensperson nicht zum schriftlichen Bekanntgeben einbezogen.
- Fristen der Wahlanfechtung verpasst.
- Verwechslung mit Personalrat (BPersVG) – beide Gremien arbeiten parallel für unterschiedliche Statusgruppen.

## Quellen Stand 06/2026

- SBG – Volltext gesetze-im-internet.de.
- SoldGleiG – Volltext gesetze-im-internet.de.
- BVerwG Wehrdienstsenate – Rechtsprechung zur Beteiligungspflicht (Az. nach Verifikation).
- Wehrbeauftragter des Deutschen Bundestages – Jahresberichte (bundestag.de/wehrbeauftragter).
- Keine Kommentar- oder Aufsatzfundstellen aus Modellwissen.

---

## Skill: `soldatengesetz-rechtsstellung`

_Soldatengesetz Rechtsstellung Grundpflichten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG im Bundesw..._

# Soldatengesetz – Rechtsstellung und Grundpflichten

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Soldatengesetz – Rechtsstellung und Grundpflichten
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Worum geht es konkret

Das Soldatengesetz (SG) regelt das öffentlich-rechtliche Dienst- und Treueverhältnis des Soldaten zum Bund. Es definiert Status, Grundpflichten und Grundrechte des Soldaten. Anders als beim Beamten besteht keine Verwaltungsgerichtsbarkeit nach VwGO als Regelweg, sondern primär WBO-Beschwerdeweg und Truppendienstgericht. Der Skill ordnet ein, welche Pflicht aus dem SG einschlägig ist und welcher Rechtsweg eröffnet ist.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Status des Mandanten: Berufssoldat, Soldat auf Zeit (SaZ), freiwillig Wehrdienstleistender (FWDL), Reservist im Wehrdienstverhältnis?
- Welche Pflicht ist im Raum (§§ 7–17a SG)? Treuepflicht, Gehorsam, Wahrheitspflicht, Kameradschaft, Achtungs- und Vertrauenswürdigkeit, Mäßigung?
- Liegt bereits ein Hinweis, eine Anhörung, ein Disziplinarvorgang oder eine Beschwerde vor?
- Welche Frist läuft (WBO 1 Monat ab Kenntnis, WDO Verjährung)?
- Gibt es einen Bezug zu einer politischen oder presseöffentlichen Äußerung?

## Rechtlicher Rahmen

- § 6 SG: Staatsbürgerliche Rechte des Soldaten – Grundrechtsgenuss mit Einschränkungen.
- § 7 SG: Treuepflicht zur freiheitlichen demokratischen Grundordnung.
- § 8 SG: Eintreten für die demokratische Grundordnung (auch außerdienstlich).
- § 10 SG: Pflichten des Vorgesetzten (Fürsorge, Vorbildlichkeit, Aufsicht).
- § 11 SG: Gehorsam – Befehl nur in Grenzen der Menschenwürde, des Strafrechts und der dienstlichen Zwecke.
- § 12 SG: Kameradschaft.
- § 13 SG: Wahrheitspflicht in dienstlichen Angelegenheiten.
- § 14 SG: Verschwiegenheitspflicht.
- § 15 SG: Politische Betätigung – Mäßigungsgebot.
- § 17 SG: Verhalten im und außer Dienst – Achtungs- und Vertrauenswürdigkeit.
- § 17a SG: Gesundes Erscheinungsbild, Uniform.
- Rechtsschutz: WBO (Beschwerde, weitere Beschwerde, Antrag auf gerichtliche Entscheidung), WDO (Disziplinarverfahren).

## / Schritt für Schritt

1. **Status klären.** Berufssoldat oder SaZ? Datum der Ernennung, Dienstzeitende, Dienstgrad, Truppenteil, Disziplinarvorgesetzter.
2. **Pflichtenkollision identifizieren.** Welche Norm aus §§ 7–17a SG ist tangiert? Gegebenenfalls mehrere parallel (Mäßigung § 15 + Achtungswürdigkeit § 17).
3. **Sachverhalt minutengenau ordnen.** Wer hat wann was gesagt/getan, vor welchem Personenkreis (innerdienstlich, halböffentlich, öffentlich, social media)?
4. **Verfahrenslage prüfen.** Liegt schon ein disziplinargerichtliches Vorermittlungsverfahren vor (§ 92 WDO)? Anhörung erfolgt? Aussagebereitschaft?
5. **Frist setzen.** WBO-Beschwerde 1 Monat (§ 6 WBO), weitere Beschwerde 2 Wochen, Antrag auf gerichtliche Entscheidung 2 Wochen.
6. **Rechtsweg festlegen.** Truppendienstgericht (WBO/WDO), BVerwG Wehrdienstsenat (Revision/höhere Sache), Verwaltungsgericht ausnahmsweise (rein verwaltungsrechtliche Sachen ohne soldatischen Bezug, Versorgung).
7. **Dokumentenanforderung.** Personalakte (Einsicht § 29 SG), Beurteilungen, Disziplinarvorgänge, Befehl/Weisung schriftlich, Zeugenliste.

## Trade-off-Matrix

| Konflikt | Option A | Option B |
| --- | --- | --- |
| Treuepflicht vs. Meinungsfreiheit | Schweigen, Verfahren abwarten | Stellungnahme mit Rechtsbeistand |
| Befehl ausführen vs. Gehorsamsverweigerung | Befehl ausführen, danach Remonstration | Verweigerung mit Berufung auf § 11 II SG |
| Beschwerde sofort vs. erst Akteneinsicht | Frist sichern (Schutzschrift) | Akteneinsicht + qualifizierte Beschwerde |
| Disziplinar vs. WBO | WBO bei Maßnahme einfacher Art | Mündliche Verhandlung Truppendienstgericht |

## Praxistipps

- Frist 1 Monat ab Kenntnis ist absolut. Eine vorsorgliche Beschwerde mit dem Vorbehalt der Begründung sichert die Frist.
- Anhörung nach § 32 WDO immer wahrnehmen, aber zur Sache keine Spontanäußerung; schriftliche Stellungnahme.
- Personalakteneinsicht (§ 29 SG) ist kostenlos und voraussetzungsfrei. Nutzen Sie sie vor jeder Verteidigungsschrift.
- Politische Äußerungen außer Dienst nicht pauschal harmlos – § 15 II SG erfasst auch private Social-Media-Posts.
- Kameradschaftspflicht (§ 12) hat Drittschutzfunktion – Verstoß kann disziplinar- und strafrechtlich relevant sein.

## Mustertexte

**Frist sichernde Beschwerde nach WBO:**
"Sehr geehrte Damen und Herren, namens und im Auftrag meines Mandanten erhebe ich gegen die [Maßnahme] vom [Datum], zugegangen am [Datum], hiermit fristwahrend Beschwerde nach § 1 WBO. Die Begründung wird nach Akteneinsicht nachgereicht. Ich beantrage, mir die vollständige Vorgangsakte zur Einsicht zu überlassen."

**Remonstration bei Zweifel an der Rechtmäßigkeit:**
"Herr [Dienstgrad], ich melde Bedenken gegen den Befehl vom [Zeitpunkt] aus folgenden Gründen: [...]. Ich bitte um Bestätigung des Befehls und um Mitteilung der Rechtsgrundlage. Bis dahin werde ich den Befehl nicht ausführen, soweit dies mit der Dienstaufgabe vereinbar ist."

## Typische Fehler

- Sofort-Erklärung in der Anhörung ohne Akteneinsicht – führt zu Festlegung auf nachteilige Sachverhaltsfassung.
- Verwechslung von einfacher Disziplinarmaßnahme (Disziplinarvorgesetzter) und gerichtlicher Maßnahme (Truppendienstgericht).
- Übersehen, dass § 15 SG auch außerdienstliche Äußerungen erfassen kann.
- WBO-Frist versäumt, weil Zugang nicht dokumentiert.
- Verwaltungsgerichtsweg nach VwGO gewählt, obwohl WBO-Weg eröffnet und verbindlich ist.

## Quellen Stand 06/2026

- Soldatengesetz (SG) in der jeweils geltenden Fassung – Volltext: gesetze-im-internet.de.
- Wehrbeschwerdeordnung (WBO) – Volltext: gesetze-im-internet.de.
- Wehrdisziplinarordnung (WDO) in der ab 2025 geltenden Fassung.
- BVerwG, Wehrdienstsenate – ständige Rechtsprechung zu §§ 7, 11, 15, 17 SG (Az. nur nach Live-Verifikation in der BVerwG-Datenbank).
- Keine Kommentarstellen aus Modellwissen zitieren; Scherer/Alff/Poretschkin und Walz/Eichen nur bei konkretem Lizenzzugriff.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

