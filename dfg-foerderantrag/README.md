# DFG-Förderantrag

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`dfg-foerderantrag`) | [`dfg-foerderantrag.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/dfg-foerderantrag.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

Plugin für die praktische Antragstellung bei der Deutschen Forschungsgemeinschaft: Sachbeihilfe, elan-Formalia, Projektbeschreibung, Finanzplan, Forschungsdaten, Ethik-/KI-Check, Reviewer-Perspektive, Wiedereinreichung und strategische Entscheidung zwischen kleinem schnellen Antrag und großem Prestigeprojekt.

Der Stil ist bewusst nicht bürokratisch. Das Plugin fragt zuerst: Was ist wissenschaftlich stark, was ist realistisch förderbar, was kann schneller entschieden werden und wo ist der große Antrag zwar verführerisch, aber prozessual zäher? Es arbeitet adaptiv: Anfänger bekommen eine geführte Mini-Roadmap; erfahrene Antragsteller bekommen direkt Red-Team, Kürzungsrisiko und Programmstrategie.

## Quellen-Gate

Vor jeder belastbaren Ausgabe aktuelle DFG-Seiten prüfen:

- DFG Sachbeihilfe: themenoffene Einzelförderung, Neuanträge jederzeit, Fortsetzungsanträge spätestens 6 Monate vor Mittelverbrauch.
- DFG Begutachtung: grundsätzlich zwei Gutachten; bei Anträgen bis 200.000 Euro kann ausnahmsweise ein aussagekräftiges externes Gutachten reichen.
- Reinhart-Koselleck-Projekte: 500.000 bis 1,25 Mio. Euro für fünf Jahre in Stufen von 250.000 Euro; nur für herausragende, besonders innovative oder risikobehaftete Projekte, die nicht in normale Verfahren passen.
- DFG-Merkblätter, elan-Vorlagen, fachzuständige Ansprechpersonen und aktuelle Vordruckstände immer live gegen `dfg.de` prüfen.

## Schnellstart

```text
/dfg-foerderantrag:allgemein
```

Der Allgemein-Skill führt in 60 Sekunden durch: Forschungsfrage, Förderprogramm, Summe, Tempo, Zielgruppe der Begutachtung, Vorarbeiten, Risiken, Daten-/Ethikthemen und gewünschtes Ergebnis.

Typische Startpunkte:

| Situation | Start |
| --- | --- |
| "Ich habe nur eine Forschungsidee" | `dfg-foerderantrag-allgemein` → Mini-Roadmap und Minimalprojekt |
| "Sachbeihilfe oder größer?" | `dfg-foerderstrategie-schnell-oder-gross` |
| "Entwurf liegt vor" | `dfg-reviewer-red-team` → danach Text- und Finanzskills |
| "Ablehnung liegt vor" | `dfg-wiedereinreichung-nach-ablehnung` |

## Skill-Matrix

| Skill | Wofür? |
| --- | --- |
| `dfg-foerderantrag-allgemein` | Einstieg, Triage, Programmroute und erster Arbeitsplan |
| `dfg-foerderstrategie-schnell-oder-gross` | Entscheidung: kleiner schneller Antrag, normale Sachbeihilfe, Koselleck oder anderes Programm |
| `dfg-sachbeihilfe-elan-formalia` | Sachbeihilfe, elan, Anlagen, Vordrucklogik, formales Gate |
| `dfg-bis-200k-begutachtung-light` | Kleine/mittlere Anträge so bauen, dass sie schnell, klar und begutachtbar sind |
| `dfg-koselleck-500k-125m` | Koselleck-Check: 500.000 bis 1,25 Mio. Euro, Risiko, Profil, Vertrauensvorschuss |
| `dfg-projektbeschreibung-arbeitsprogramm` | Forschungsfrage, Stand der Forschung, Ziele, Arbeitspakete, Meilensteine |
| `dfg-finanzplan-module-personal-geraete` | Personal, Geräte, Reisen, Workshops, Mercator Fellow, Chancengleichheit, Budgetbegründung |
| `dfg-reviewer-red-team` | Gutachterperspektive, Angriffsflächen, Kürzungsrisiken, Ablehnungsgründe |
| `dfg-wiedereinreichung-nach-ablehnung` | Ablehnung auswerten, Gutachten ernst nehmen, Neuaufstellung |
| `dfg-ki-ethik-forschungsdaten` | KI-Nutzung, Vertraulichkeit, Forschungsdatenmanagement, Ethik und Datenschutz |

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 70 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anfaenger-antraege-dfg` | Anfaenger Antraege DFG im DFG-Förderantragstellung: prüft konkret Anfaenger, Antraege, DFG. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `dfg-bis-200k-begutachtung-light` | Kleine und mittlere DFG-Anträge bis 200.000 Euro begutachtungsfreundlich bauen: klare Kernfrage, schlanker Finanzplan, ein Gutachten möglich, schnelle Lesbarkeit, Fortsetzungsfähigkeit. |
| `dfg-eigenanteil-und-grundausstattung` | Eigenanteil und Grundausstattung der Hochschule sauber von DFG-Foerderung abgrenzen: Was muss die Hochschule stellen (Buero, Standardrechner, Sekretariat, Bibliothek), was darf die DFG finanzieren (projektspezifische Geraete, Personal ue... |
| `dfg-eigene-vorarbeiten-darstellen` | Eigene Vorarbeiten in DFG-Antrag richtig darstellen: bisher publizierte Ergebnisse, eigene Methodik-Beitraege, Pilotdaten. Reviewer-Perspektive: Anknuepfungsfaehigkeit pruefen, keine Selbstplagiat-Pruefung. Mustertext fuer 2-Seiten-Kapitel. |
| `dfg-erstantragsteller-besondere-checks` | Erstantragsteller-Spezialcheck: Promotion abgeschlossen, gute eigene Vorarbeit (Publikationen Erst- und Letztautor), Anbindung an erfahrene Person ohne Co-Antragstellung wenn moeglich, Lebenslauf mit Eltern- und Pflegezeiten transparent,... |
| `dfg-finanzplan-module-personal-geraete` | DFG-Finanzplan und Modulbegründung erstellen: Personal, Geräte, Verbrauchsmittel, Reisen, Workshops, Mercator Fellow, Chancengleichheit, Öffentlichkeitsarbeit, Kostenlogik und Kürzungsabwehr. |
| `dfg-foerderantrag-adaptive-dokumentenmatrix-lueckenliste` | Adaptive: Dokumentenmatrix, Lückenliste und Nachforderung im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustell... |
| `dfg-foerderantrag-anfaenger-risikoampel-gegenargumente` | Anfaenger: Risikoampel, Gegenargumente und Verteidigungslinien im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zu... |
| `dfg-foerderantrag-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `dfg-foerderantrag-antraege-zahlen-schwellenwerte-berechnung` | Antraege: Zahlen, Schwellenwerte und Berechnung im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwe... |
| `dfg-foerderantrag-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im DFG-Förderantragstellung: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Belege lie... |
| `dfg-foerderantrag-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `dfg-foerderantrag-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `dfg-foerderantrag-elan-formular-portal-einreichungslogik` | Elan: Formular, Portal und Einreichungslogik im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle... |
| `dfg-foerderantrag-erstantrag-projektlogik` | Foerderantragssteller: Tatbestandsmerkmale, Beweisfragen und Beleglage im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche F... |
| `dfg-foerderantrag-ethik-abschlussprodukt-uebergabe` | Ethik: Abschlussprodukt und Übergabe im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlun... |
| `dfg-foerderantrag-finanzplan-mandantenkommunikation` | Finanzplan: Mandantenkommunikation und Entscheidungsvorlage im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zuste... |
| `dfg-foerderantrag-fristen-und-risikoampel` | Fristen- und Risikoampel im DFG-Förderantragstellung: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Belege liegen... |
| `dfg-foerderantrag-fuehrung-schriftsatz-brief-memo-bausteine` | Fuehrung: Schriftsatz-, Brief- und Memo-Bausteine im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Sch... |
| `dfg-foerderantrag-grosse-compliance-dokumentation-aktenvermerk` | Grosse: Compliance-Dokumentation und Aktenvermerk im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Sch... |
| `dfg-foerderantrag-kaltstart-triage` | Adaptiver Einstieg, Schnelltriage und Fallrouting im DFG-Förderantrag-Plugin. Führt Anfänger mit maximal sechs Fragen, fordert Profis mit Go/No-Go und Reviewer-Risiken, klärt Forschungsfrage, Programmroute, Antragssumme, Tempo, Vorarbeit... |
| `dfg-foerderantrag-kleine-verhandlung-vergleich-eskalation` | Kleine: Verhandlung, Vergleich und Eskalation im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwell... |
| `dfg-foerderantrag-mandantenkommunikation` | Mandantenkommunikation im DFG-Förderantragstellung: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Belege liegen b... |
| `dfg-foerderantrag-mandantenkommunikation-redteam-qualitygate` | Mandantenkommunikation Redteam Qualitygate im DFG-Förderantragstellung: prüft konkret Mandantenkommunikation im Plugin dfg-foerderantrag, Red-Team Qualitygate im Plugin dfg-foerderantrag, Forschungsdaten. Liefert priorisierten Output mit... |
| `dfg-foerderantrag-output-waehlen` | Output wählen im DFG-Förderantragstellung: Diese Output-Weiche für Dfg Foerderantrag entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `dfg-foerderantrag-profi-behoerden-gerichts-registerweg` | Profi: Behörden-, Gerichts- oder Registerweg im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle... |
| `dfg-foerderantrag-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `dfg-foerderantrag-redteam-qualitygate` | Red-Team Qualitygate: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `dfg-foerderantrag-sachbeihilfe-fristen-form-zustaendigkeit` | Sachbeihilfe: Fristen, Form, Zuständigkeit und Rechtsweg im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellu... |
| `dfg-foerderantrag-start-chronologie-fristen` | Start Chronologie Fristen im DFG-Förderantragstellung: prüft konkret Adaptiver Einstieg, Schnelltriage und Fallrouting im DFG-Förderantrag-Plugin, Chronologie und Belegmatrix im Plugin dfg-foerderantrag, Fristen- und Risikoampel im Plugi... |
| `dfg-foerderantrag-strategien-internationaler-bezug` | Strategien: Internationaler Bezug und Schnittstellen im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung,... |
| `dfg-foerderantrag-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `dfg-foerderstrategie-schnell-oder-gross` | Strategischer DFG-Router: entscheidet zwischen kleiner schneller Sachbeihilfe, normalem Antrag über 200.000 Euro, Koselleck ab 500.000 Euro oder anderem DFG-Programm. Enthält Spatz-in-der-Hand-Logik, Kürzungsrisiko, Begutachtungsdichte u... |
| `dfg-grossgeraete-und-cluster-antrag` | Grossgeraete und Cluster-Geraete in DFG-Antrag: Geraete ab 50.000 Euro mit zusaetzlicher Wirtschaftlichkeit, Auslastungsplan, technische Anschlussbedingungen, Wartungsvertrag, Folgekosten. Eigene Geraetekommission der DFG. Pruefraster fu... |
| `dfg-grundsystem-foerderlinien` | Grundsystem der DFG-Foerderlinien einfuehrend erklaeren: Sachbeihilfe (Einzelantrag), Emmy Noether, Heisenberg, Reinhart Koselleck, SFB, GRK, Forschergruppen, Schwerpunktprogramme. Pro Linie: Zielgruppe, Hoehe, Dauer, Antragsweg, Begutac... |
| `dfg-internationale-kooperation-aufbau` | Internationale Kooperation in DFG-Antrag aufbauen: D-A-CH-Lead-Agency-Verfahren (DACH, SNF, FWF), Bilateral mit DFG-Partnerorganisationen (NSF, JSPS, ISF, NSFC). Kooperationszusagen, Mittelverteilung, Hauptantragsteller, Co-Antragsteller... |
| `dfg-ki-ethik-forschungsdaten` | DFG-Antrag auf KI-Nutzung, Ethik, Datenschutz, Forschungsdatenmanagement und gute wissenschaftliche Praxis prüfen. Behandelt Vertraulichkeit in Begutachtung, Datenmanagementplan, sensible Daten, Open Access und Nachnutzung. |
| `dfg-kollegen-review-organisieren` | Kollegen-Review eines DFG-Antrags strukturiert organisieren: 2 erfahrene Profs aus dem Fach plus 1 Methodik-Kollege, Briefing-Mail, Review-Raster (Originalitaet, Arbeitsprogramm, Finanzplan, Vorarbeiten), 1-Wochen-Frist. Output Vorlage B... |
| `dfg-koselleck-500k-125m` | Reinhart-Koselleck-Projekt prüfen und entwerfen: 500.000 Euro bis 1.250.000 Euro, 5 Jahre, Stufen von 250.000 Euro, außergewöhnliches Profil, positives Risiko, Vertrauensvorschuss, Abgrenzung zur Sachbeihilfe. |
| `dfg-koselleck-500k-praeregistrierung` | Koselleck 500k Praeregistrierung im DFG-Förderantragstellung: prüft konkret Reinhart-Koselleck-Projekt prüfen und entwerfen, Praeregistrierung und Replikationsstudien im DFG-Antrag, DFG-Projektbeschreibung und Arbeitsprogramm ausarbeiten... |
| `dfg-praeregistrierung-replication-studies` | Praeregistrierung und Replikationsstudien im DFG-Antrag: Hypothesen ex ante festlegen, registered reports, OSF-Praeregistrierung, Replikationsplaene als eigenstaendiges Vorhaben. DFG-Statement to scientific integrity. Vorteile fuer Revie... |
| `dfg-projektbeschreibung-arbeitsprogramm` | DFG-Projektbeschreibung und Arbeitsprogramm ausarbeiten: Forschungslücke, Stand der Forschung, Ziele, Hypothesen, Methoden, Arbeitspakete, Meilensteine, Risiken, Forschungsdaten und verwertbare Antragssprache. |
| `dfg-publikationsstrategie-projekt` | Publikationsstrategie fuer das beantragte Projekt: realistische Zahl Publikationen, geplante Zeitschriften mit Impact und Open-Access-Status, DFG-Open-Access-Politik, Praeprints, Datenpublikation. Im Antrag muss Publikationsplan zu Arbei... |
| `dfg-replikationskrise-statistik-spezial` | Spezialfall Statistikabschnitt nach Replikationskrise: a-priori-Power-Analyse, Effektgroessenschaetzung, Vorab-Festlegung Hypothesen, Korrektur fuer multiple Testung, Sensitivitaetsanalysen. Pruefraster fuer Reviewer-Akzeptanz. |
| `dfg-reviewer-red-team` | DFG-Antrag aus Gutachterperspektive red-teamen: Originalität, Machbarkeit, Arbeitsprogramm, Qualifikation, Umfeld, Bias-Risiken, Kürzungsargumente, Ablehnungsrisiken und Verbesserungsplan. |
| `dfg-sachbeihilfe-elan-formalia` | DFG-Sachbeihilfe und elan-Formalia prüfen: Antragsberechtigung, Module, Vordrucke, Anlagen, Seitenlogik, Fachzuordnung, Fortsetzungsantrag, internationale Kooperation, formale Einreichungsreife. |
| `dfg-software-veroeffentlichung-spezial` | Spezialfall Software als Forschungsergebnis: DFG-Hinweise zur Open-Source-Veroeffentlichung, Lizenzwahl (MIT, BSD, Apache-2.0, GPL), Zenodo-DOI, Reproducibility. Pruefraster und Mustertext fuer Software-Sektion im Arbeitsprogramm. |
| `dfg-software-veroeffentlichung-tieforschung` | Software Veroeffentlichung Tieforschung im DFG-Förderantragstellung: prüft konkret Spezialfall Software als Forschungsergebnis, Tierversuchsethik-Pflichten in DFG-Antraegen, DFG-Ablehnung, Gutachten und Entscheidung auswerten. Liefert pr... |
| `dfg-tieforschung-ethik-pflichten` | Tierversuchsethik-Pflichten in DFG-Antraegen: 3R-Prinzip (Replace, Reduce, Refine), TierSchG, TierSchVersV, Tierversuchsantrag bei der Behoerde parallel zur DFG. DFG-Senatskommission fuer tierexperimentelle Forschung. Ethik-Sektion im An... |
| `dfg-wiedereinreichung-nach-ablehnung` | DFG-Ablehnung, Gutachten und Entscheidung auswerten: tragende Kritik extrahieren, Verteidigungsreflex vermeiden, Wiedereinreichung planen, Antrag umbauen, Anschreiben und Änderungsmatrix erstellen. |
| `dfg-zeitplan-und-meilensteine` | Antragszeitplan vom ersten Skizzen-Entwurf bis zur Einreichung in elan strukturieren: 6 Monate vorher Themenfindung, 4 Monate vorher Literaturrecherche und Arbeitsprogramm, 3 Monate vorher Finanzplan, 6 Wochen vorher Kollegenreview, 2 Wo... |
| `dfg-zwischen-und-abschlussbericht` | Zwischen- und Abschlussbericht systematisch vorbereiten: Berichtsraster der DFG, Soll-Ist-Abgleich Arbeitsprogramm, Publikationen, Personal, Geraete, Mittelabfluss. Abschlussbericht ist gleichzeitig Bewertungsbasis fuer Folgeantrag. Typi... |
| `eigene-vorarbeiten-erstantragsteller` | Eigene Vorarbeiten Erstantragsteller im DFG-Förderantragstellung: prüft konkret Eigene Vorarbeiten in DFG-Antrag richtig darstellen, Erstantragsteller-Spezialcheck, DFG-Finanzplan und Modulbegründung erstellen. Liefert priorisierten Outp... |
| `elan-ethik-finanzplan` | Elan Ethik Finanzplan im DFG-Förderantragstellung: prüft konkret Elan, Ethik, Finanzplan. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `erstpruefung-rollenklaerung-mandatsziel` | DFG: Erstprüfung, Rollenklärung und Mandatsziel im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwe... |
| `foerderantragssteller-formalia-red-fuehrung` | Foerderantragssteller Formalia RED Fuehrung im DFG-Förderantragstellung: prüft konkret Foerderantragssteller, Formalia, Fuehrung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `foerderstrategie-schnell-grossgeraete-cluster` | Foerderstrategie Schnell Grossgeraete Cluster im DFG-Förderantragstellung: prüft konkret Strategischer DFG-Router, Grossgeraete und Cluster-Geraete in DFG-Antrag, Grundsystem der DFG-Foerderlinien einfuehrend erklaeren. Liefert priorisie... |
| `formalia-fehlerkatalog` | Formalia Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `forschungsdaten-fristennotiz-naechster` | Forschungsdaten: Fristennotiz und nächster Schritt im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Sc... |
| `grosse-kleine-koselleck-interessen` | Grosse Kleine Koselleck Interessen im DFG-Förderantragstellung: prüft konkret Grosse, Kleine, Koselleck. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `internationale-kooperation-ki-ethik-kollegen` | Internationale Kooperation KI Ethik Kollegen im DFG-Förderantragstellung: prüft konkret Internationale Kooperation in DFG-Antrag aufbauen, DFG-Antrag auf KI-Nutzung, Ethik, Datenschutz. Liefert priorisierten Output mit Norm-Pinpoints, Ri... |
| `koselleck-interessen` | Koselleck: Mehrparteienkonflikt und Interessenmatrix im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung,... |
| `profi-reviewer-beweislast-strategien` | Profi Reviewer Beweislast Strategien im DFG-Förderantragstellung: prüft konkret Profi, Reviewer, Strategien. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `publikationsstrategie-projekt` | Publikationsstrategie Projekt im DFG-Förderantragstellung: prüft konkret Publikationsstrategie fuer das beantragte Projekt, Spezialfall Statistikabschnitt nach Replikationskrise, DFG-Sachbeihilfe und elan-Formalia prüfen. Liefert prioris... |
| `reviewer-beweislast-darlegungslast` | Reviewer: Beweislast, Darlegungslast und Substantiierung im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellu... |
| `sachbeihilfe-bis-200k-eigenanteil` | Sachbeihilfe BIS 200k Eigenanteil im DFG-Förderantragstellung: prüft konkret Sachbeihilfe, Kleine und mittlere DFG-Anträge bis 200.000 Euro, Eigenanteil und Grundausstattung der Hochschule sauber von. Liefert priorisierten Output mit Nor... |
| `schnelle-quellenkarte` | Schnelle Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `team-sonderfall` | Team Sonderfall im DFG-Förderantragstellung: fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |
| `team-sonderfall-edge-case` | Team: Sonderfall und Edge-Case-Prüfung im DFG-Förderantragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahl... |
| `zeitplan-meilensteine-zwischen` | Zeitplan Meilensteine Zwischen im DFG-Förderantragstellung: prüft konkret Antragszeitplan vom ersten Skizzen-Entwurf bis zur, Zwischen- und Abschlussbericht systematisch vorbereiten, Adaptive. Liefert priorisierten Output mit Norm-Pinpoi... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
