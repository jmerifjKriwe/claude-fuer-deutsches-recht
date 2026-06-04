---
name: kompendium-01-allgemein-bis-dsv-sanktion-beschlu
description: "datenschutzrecht: Konsolidiertes Skill-Kompendium 01; bündelt 10 frühere Spezialskills (allgemein, workflow-anschluss-skills-router, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel, workflow-mandantenkommunikation und 5 weitere) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 01 - datenschutzrecht

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Datenschutzrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Spezial-Skills oder stellt genau eine gezielte Rückfrage. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin datenschutzrecht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin datenschutzrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin datenschutzrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin datenschutzrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin datenschutzrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin datenschutzrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `dsv-rechtsprechung-immaterieller-schaden-bgh-olg` | Analysiert die deutsche Rechtsprechung zum immateriellen Schadensersatz nach Art. 82 DSGVO im Lichte der EuGH-Vorgaben. Behandelt: BGH-Entscheidungen zur Substantiierung; OLG-Linien zur Bagatellschwelle; OLG-Entscheidungen zur Beweislast bei Kontrollverlust; LG-Streuung bei Datenleck-Massenklagen; Schmerzensgeldgrößen; Kausalitäts-anforderungen. Output: Rechtsprechungs-Übersicht mit Begründungslinien. Abgrenzung: keine konkrete Verteidigung. |
| `datenschutz-bussgeldverfahren-art-83-dsgvo-verteidigung` | Bußgeldverteidigung nach Art. 83 DSGVO bis 4 Prozent Jahresumsatz oder 20 Mio. EUR. EDSA-Leitlinien 04/2022 zur Bemessung. Sieben-Fragen-Diagnose: Anhörung oder Bußgeldbescheid, Aufsichtsbehörde, Norm DSGVO/BDSG, Bezugsumsatz, Vorwurf, Verschulden, Maßnahmenlage. Schritt-für-Schritt: Akteneinsicht, keine vorschnelle Stellungnahme, dynamische Geldbemessung, EDSA-Methodik, § 41 BDSG, OWiG/StPO-Verfahrensgarantien. Einspruch nach § 67 OWiG binnen zwei Wochen. EuGH C-807/21 Deutsche Wohnen und C-683/21: Unternehmensgeldbuße ohne Identifizierung einer natürlichen Person, aber nicht ohne Vorsatz oder Fahrlässigkeit. Mustertexte Einspruch, Stellungnahme, Erledigungsvorschlag. Abgrenzung: keine zivilrechtliche Schadensersatzabwehr. |
| `dsv-sanktion-beschlussverfahren-72-owig` | Datenschutzrecht-Brückenskill: Beschlussverfahren § 72 OWiG: Schriftliche Erledigung per Beschluss prüfen, wenn Tatsachen und Verfahrenslage dafür taugen. Spezialskill für Datenschutz-Sanktionsverfahren, Bußgeldverteidigung, Aufsichtsbehördenkommunikation und gerichtlichen Rechtsschutz. Bei ernstem Behörden- oder Bußgelddruck Spezialplugin datenschutz-sanktionsverfahren-verteidigung laden. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `allgemein`

**Frühere Beschreibung:** Einstieg, Schnelltriage und Workflow-Routing im Datenschutzrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Spezial-Skills oder stellt genau eine gezielte Rückfrage.

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Spezial-Skills dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.



# Datenschutzrecht — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Datenschutzrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** DSGVO/BDSG/TDDDG – PIA/DPIA, AVV-Review als Verantwortlicher und Auftragsverarbeiter, Auskunftsersuchen Art. 15, Datenpannenmeldung Art. 33/34, Drittlandstransfer Art. 44 ff., US-Transfer mit DPF/SCC/TIA, Behördenpaket, Drift-Monitoring.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Spezial-Skill aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. **Nur eine Rückfrage:** Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

**Was du bei stummem Upload nicht machst:**

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

**Antwortformat bei stummem Upload:**

- **Erkannt:** [Materialart, Absender/Aktenzeichen falls sichtbar]
- **Frist zuerst:** [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- **Einordnung:** [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- **Primärer Pfad:** `passender-datenschutz-skill` — [warum dieser Skill hilft]
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Spezial-Skills vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Spezial-Skill.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Spezial-Skills in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `anwendungsfall-triage` | Datenschutzrechtlichen Sachverhalt einordnen und Bearbeitungsroute bestimmen. Art. 2 3 DSGVO Anwendungsbereich § 1 BDSG. Prüfraster: Anwendungsbereich personenbezogene Daten Verantwortlicher Auftragsverarbeiter… |
| `avv-pruefung` | Auftragsverarbeitungsvertrag nach Art. 28 DSGVO prüfen oder erstellen wenn Dritter Daten im Auftrag verarbeitet. Art. 28 DSGVO AVV-Pflicht § 62 BDSG. Prüfraster: Pflichtinhalte Art. 28 Abs. 3 Weisungsgebundenheit… |
| `datenpanne-meldung` | Datenpanne nach Art. 33 34 DSGVO melden wenn Sicherheitsverletzung personenbezogener Daten vorliegt. Art. 33 34 DSGVO Meldepflichten § 65 BDSG. Prüfraster: Meldepflicht 72-Stunden-Frist Schwere Risikobewertung… |
| `datenschutzrecht-anpassen` | Bestehende Datenschutzdokumentation oder Richtlinien an neue Anforderungen oder Verarbeitungstätigkeiten anpassen. Art. 5 24 DSGVO Rechenschaftspflicht. Prüfraster: Bestandsaufnahme Lueckenanalyse DSGVO-Anforderungen… |
| `datenschutzrecht-kaltstart-interview` | Neues Datenschutzmandat durch strukturiertes Erstgespraech aufnehmen. Art. 5 6 DSGVO Grundsaetze § 26 BDSG Beschaeftigtendaten. Prüfraster: Verarbeitungszweck Datenarten betroffene Personen Empfaenger… |
| `datenschutzrecht-mandat-arbeitsbereich` | Datenschutzrechtliches Mandat strukturieren und Arbeitsbereich abgrenzen. Art. 5 24 DSGVO §§ 1 ff. BDSG. Prüfraster: Mandatsumfang Zuständigkeiten Fristen Risikostufe externe Datenschutzberatung. Output:… |
| `drittlandstransfer-pruefung` | Datentransfer in Drittlaender außerhalb EU und EWR auf Zulässigkeit prüfen. Art. 44 ff. DSGVO Kapitel V Drittlandstransfer. Prüfraster: Angemessenheitsbeschluss SCC BCR Schrems-II-Folgen Transfer Impact Assessment… |
| `us-transfer-tia-dokumentation` | US-Drittlandtransfer mit EU-US Data Privacy Framework, DPF-Listing, Schrems-I/II-Historie, SCC/BCR-Ausweichpfad, Transfer Impact Assessment, supplementary measures und Review-Kalender dokumentieren. |
| `standardvertragsklauseln-scc-paket` | Standardvertragsklauseln vorbereiten: Modul 1-4 wählen, Annex I-III ausfüllen, Subprozessoren, TOMs, AVV-Schnittstelle, TIA-Andockung und Unterzeichnungspaket erstellen. |
| `drittlandtransfer-behoerdenpaket-output` | Aus Transferregister, DPF/SCC/TIA, TOMs und Subprozessoren ein druckreifes Paket samt Antwortentwurf für deutsche Datenschutzaufsichtsbehörden bauen. |
| `dsb-bestellungspflicht-pruefung` | Bestellungspflicht für Datenschutzbeauftragten prüfen. Art. 37 DSGVO § 38 BDSG Bestellungspflicht. Prüfraster: Schwellenwerte Art. 37 Abs. 1 Betriebsgroe Verarbeitungsart Pflichtbestellung freiwillige Bestellung.… |
| `dsfa-erstellung` | Datenschutz-Folgenabschaetzung nach Art. 35 DSGVO durchführen wenn hohes Risiko für Betroffene vorliegt. Art. 35 36 DSGVO DSFA § 67 BDSG. Prüfraster: Risikobewertung Verarbeitungsbeschreibung Notwendigkeit… |
| `dsgvo-auskunft` | Auskunftsersuchen nach Art. 15 DSGVO prüfen und beantworten wenn Betroffener Auskunft verlangt. Art. 15 12 DSGVO Betroffenenrechte. Prüfraster: Identitätsnachweis Vollständigkeitsprüfung Auskunftsinhalt Fristen… |
| `dsgvo-auskunft-antwort` | DSGVO-Auskunftsantwort an Betroffenen vollständig und rechtskonform gestalten. Art. 15 12 Abs. 3 DSGVO Antwortpflicht. Prüfraster: Antwortinhalt Format Fristen Klarheit Weglassungsgründe Begleitschreiben. Output:… |
| `joint-controller-vereinbarung` | Joint-Controller-Vereinbarung nach Art. 26 DSGVO erstellen wenn zwei oder mehr Verantwortliche gemeinsam entscheiden. Art. 26 DSGVO Gemeinsame Verantwortlichkeit. Prüfraster: gemeinsame Zwecke und Mittel… |
| `ki-verordnung-compliance` | KI-Systeme auf Anforderungen der KI-VO und Datenschutz prüfen. KI-VO Risikoklassen Art. 5 9 DSGVO Einwilligung. Prüfraster: Risikoklasse Verbote Hochrisiko-KI Dokumentationspflichten DSGVO-Schnittmengen… |
| `mandantendaten-ki` | Datenschutzkonforme Verwendung von Mandantendaten beim Einsatz von KI-Tools in der Kanzlei prüfen. Art. 5 6 DSGVO BRAO § 43a Verschwiegenheit. Prüfraster: Rechtsgrundlage Zweckbindung Vertraulichkeit Anwaltsprivileg… |
| `regulierungs-luecken-analyse` | Regulatorische Luecken im Datenschutzrecht identifizieren und Handlungsoptionen aufzeigen. Art. 5 6 24 DSGVO BDSG. Prüfraster: Bestandsaufnahme bestehender Massnahmen Soll-Ist-Abgleich Lueckenbewertung Prioritaeten.… |
| `richtlinien-monitor` | Datenschutzrichtlinien und Unternehmensanweisungen auf Aktualitaet und Konformität monitoren. Art. 24 32 DSGVO TOMs §§ 4 ff. BDSG. Prüfraster: Richtlinienbestand Aenderungsbedarf neue Verarbeitungstätigkeiten… |
| `verarbeitungsverzeichnis-vvt-generator` | Verzeichnis der Verarbeitungstätigkeiten nach Art. 30 DSGVO erstellen oder aktualisieren. Art. 30 DSGVO VVT-Pflicht. Prüfraster: Pflichtangaben Art. 30 Abs. 1 Verantwortlicher Zweck Kategorien Empfaenger Fristen… |

## Worum geht es?

Dieses Plugin unterstuetzt Rechtsanwaelte und Datenschutzbeauftragte bei der Bearbeitung datenschutzrechtlicher Mandate nach DSGVO und BDSG. Es deckt den vollstaendigen Workflow ab: von der ersten Triage ueber Auftragsverarbeitungsvertraege, Datenschutz-Folgenabschaetzungen und Auskunftsersuchen bis zu Datenpannenmeldungen, Drittlandstransfers, US-Transfer-Dokumentation und der laufenden Richtlinienpflege.

Der Anwendungsbereich umfasst Unternehmen als Verantwortliche (Art. 4 Nr. 7 DSGVO), Auftragsverarbeiter (Art. 4 Nr. 8 DSGVO) und gemeinsam Verantwortliche (Art. 26 DSGVO), sowie den Einsatz von KI-Tools im Kanzleialltag.

## Wann brauchen Sie diese Skill?

- Ein Unternehmen erhaelt ein Auskunftsersuchen nach Art. 15 DSGVO und braucht eine rechtskonforme Antwort.
- Ein Datenschutzbeauftragter muss eine Datenpanne nach Art. 33 DSGVO binnen 72 Stunden an die Aufsichtsbehoerde melden.
- Eine Kanzlei prueft, ob ein IT-Dienstleister einen Auftragsverarbeitungsvertrag nach Art. 28 DSGVO benoetigt.
- Ein Unternehmen will Daten in ein Drittland (USA, Indien) uebertragen und braucht einen Transfer-Impact-Assessment.
- Eine Aufsichtsbehoerde fragt nach US-Transfer, DPF-Listing, SCC, TIA und Schrems-II-Dokumentation.
- Eine Behoerde oder Kanzlei prueft, ob KI-Werkzeuge datenschutzkonform eingesetzt werden koennen.

## Fachbegriffe (kurz erklaert)

- **DSGVO** — Datenschutz-Grundverordnung (EU 2016/679); einheitliches EU-Datenschutzrecht fuer Verarbeitung personenbezogener Daten.
- **BDSG** — Bundesdatenschutzgesetz; ergaenzt die DSGVO im deutschen Recht, insbesondere fuer Beschaeftigtendatenschutz (§ 26 BDSG).
- **TDDDG** — Telekommunikation-Digitale-Dienste-Datenschutzgesetz; Nachfolger des TTDSG, regelt Cookies und Online-Tracking.
- **AVV** — Auftragsverarbeitungsvertrag nach Art. 28 DSGVO; Pflichtvertrag, wenn ein Dritter Daten im Auftrag verarbeitet.
- **DSFA** — Datenschutz-Folgenabschaetzung (Data Protection Impact Assessment, DPIA) nach Art. 35 DSGVO; Pflicht bei hohem Risiko.
- **Drittland** — Staat ausserhalb des EWR, in den Datentransfers nur unter bestimmten Voraussetzungen zulaessig sind (Art. 44 ff. DSGVO).
- **VVT** — Verzeichnis der Verarbeitungstaetigkeiten nach Art. 30 DSGVO; Dokumentationspflicht fuer Verantwortliche und Auftragsverarbeiter.
- **DSB** — Datenschutzbeauftragter; Pflichtposition nach Art. 37 DSGVO und § 38 BDSG ab bestimmten Schwellenwerten.

## Rechtsgrundlagen

- Art. 5 DSGVO (Grundsaetze der Verarbeitung)
- Art. 6 DSGVO (Rechtmaessigkeit der Verarbeitung)
- Art. 12-23 DSGVO (Betroffenenrechte)
- Art. 26 DSGVO (Joint Controller)
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 30 DSGVO (Verzeichnis der Verarbeitungstaetigkeiten)
- Art. 33-34 DSGVO (Meldepflicht bei Datenpannen)
- Art. 35-36 DSGVO (Datenschutz-Folgenabschaetzung)
- Art. 37-39 DSGVO (Datenschutzbeauftragter)
- Art. 44-49 DSGVO (Drittlandstransfer)
- § 26 BDSG (Beschaeftigtendatenschutz)
- § 38 BDSG (Pflicht zur Bestellung eines DSB)

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Verantwortlicher, Auftragsverarbeiter oder gemeinsam Verantwortlicher?
2. Sachverhalt einordnen und Bearbeitungsroute bestimmen (Skill `anwendungsfall-triage`).
3. Mandat strukturieren und Arbeitsbereich abgrenzen (`datenschutzrecht-kaltstart-interview` oder `datenschutzrecht-mandat-arbeitsbereich`).
4. Passenden Fachskill auswaehlen (z. B. AVV, DSFA, Drittlandstransfer, Datenpanne).
5. Eilfristen pruefen: Datenpannenmeldung 72-Stunden-Frist, Auskunftspflicht einen Monat ab Ersuchen.

## Skill-Tour (was gibt es hier?)

- `anwendungsfall-triage` — Datenschutzrechtlichen Sachverhalt einordnen und Bearbeitungsroute bestimmen.
- `datenschutzrecht-kaltstart-interview` — Neues Datenschutzmandat durch strukturiertes Erstgespraech aufnehmen.
- `datenschutzrecht-mandat-arbeitsbereich` — Datenschutzrechtliches Mandat strukturieren und Arbeitsbereich abgrenzen.
- `datenschutzrecht-anpassen` — Bestehende Datenschutzdokumentation oder Richtlinien an neue Anforderungen anpassen.
- `avv-pruefung` — Auftragsverarbeitungsvertrag nach Art. 28 DSGVO pruefen oder erstellen.
- `joint-controller-vereinbarung` — Joint-Controller-Vereinbarung nach Art. 26 DSGVO erstellen, wenn zwei oder mehr Verantwortliche gemeinsam entscheiden.
- `dsfa-erstellung` — Datenschutz-Folgenabschaetzung nach Art. 35 DSGVO durchfuehren bei hohem Risiko.
- `datenpanne-meldung` — Datenpanne nach Art. 33 und 34 DSGVO melden bei Sicherheitsverletzung personenbezogener Daten.
- `dsgvo-auskunft` — Auskunftsersuchen nach Art. 15 DSGVO pruefen und Bearbeitungsstrategie bestimmen.
- `dsgvo-auskunft-antwort` — DSGVO-Auskunftsantwort an Betroffenen vollstaendig und rechtskonform gestalten.
- `drittlandstransfer-pruefung` — Datentransfer in Drittlaender ausserhalb EU und EWR auf Zulaessigkeit pruefen.
- `us-transfer-tia-dokumentation` — US-Transfer mit DPF, SCC/BCR-Ausweichpfad, TIA und ergänzenden Maßnahmen dokumentieren.
- `standardvertragsklauseln-scc-paket` — SCC-Modulwahl, Annex I-III, Subprozessoren und TOMs behördenfest vorbereiten.
- `drittlandtransfer-behoerdenpaket-output` — Deckvermerk, Anlagenverzeichnis, Behördenantwort und Maßnahmenplan ausgeben.
- `dsb-bestellungspflicht-pruefung` — Bestellungspflicht fuer Datenschutzbeauftragten nach Art. 37 DSGVO und § 38 BDSG pruefen.
- `verarbeitungsverzeichnis-vvt-generator` — Verzeichnis der Verarbeitungstaetigkeiten nach Art. 30 DSGVO erstellen oder aktualisieren.
- `ki-verordnung-compliance` — KI-Systeme auf Anforderungen der KI-VO und Datenschutz gemeinsam pruefen.
- `mandantendaten-ki` — Datenschutzkonforme Verwendung von Mandantendaten beim Einsatz von KI-Tools in der Kanzlei pruefen.
- `regulierungs-luecken-analyse` — Regulatorische Luecken im Datenschutzrecht identifizieren und Handlungsoptionen aufzeigen.
- `richtlinien-monitor` — Datenschutzrichtlinien und Unternehmensanweisungen auf Aktualitaet und Konformitaet monitoren.

## Worauf besonders achten

- Datenpannenmeldung nach Art. 33 DSGVO hat eine 72-Stunden-Frist ab Kenntnisnahme — keine Verzoegerung durch interne Abstimmungsrunden.
- Drittlandstransfer ohne Rechtsgrundlage (Angemessenheitsbeschluss oder Standardvertragsklauseln) ist ein bussgeldrelevanter Verstoss.
- Auftragsverarbeitungsvertraege muessen vor Beginn der Verarbeitung vorliegen — nicht erst nach Vertragsschluss.
- § 26 BDSG-Beschaeftigtendatenschutz hat engere Grenzen als die DSGVO-Generalklausel — gesondert pruefen.
- Cookies und Tracking unterliegen zusaetzlich dem TDDDG — einwilligungspflichtige Dienste nicht mit Art. 6 Abs. 1 lit. f DSGVO rechtfertigen.

## Typische Fehler

- Auftragsverarbeitungsvertrag fehlt: Unternehmen gibt Daten an Cloud-Anbieter weiter ohne AVV nach Art. 28 DSGVO.
- DSFA-Pflicht verkannt: Hochrisiko-Verarbeitung (z. B. Profilbildung, Scoring) wird ohne Folgenabschaetzung gestartet.
- Auskunftsantwort unvollstaendig: Betroffener erhaelt keine Information ueber Empfaenger oder Speicherdauer.
- Drittlandstransfer nach Schrems II nicht geprueft: Alte Safe-Harbor- oder Privacy-Shield-Grundlage wird weiter verwendet.
- DSB-Bestellungspflicht nicht erkannt: Unternehmen beschaeftigt mehr als 20 Personen mit Datenverarbeitung, bestellt aber keinen DSB.

## Querverweise

- `ki-vo-ai-act-pruefer` — KI-Systeme im Datenschutzkontext; DSGVO und KI-VO ueberschneiden sich bei Hochrisiko-KI.
- `regulatorisches-recht` — Sektorzeitige Datenschutzanforderungen fuer Finanzunternehmen (MaRisk, DORA).
- `vertragsrecht` — AVV und Datenschutzklauseln in Lieferanten- und SaaS-Vertraegen.
- `einfache-leichte-sprache-jura` — DSGVO verlangt verstaendliche Einwilligungserklaerungen und Datenschutzhinweise.

## Quellen und Aktualitaet

- Stand: 05/2026
- DSGVO (EU 2016/679) in der zum Stand-Datum geltenden Fassung
- BDSG in der geltenden Fassung
- TDDDG in der geltenden Fassung
- Standardvertragsklauseln der EU-Kommission (2021/914)
- EU-US Data Privacy Framework-Angemessenheitsbeschluss der EU-Kommission vom 10.07.2023 und offizielle DPF-Participant-Search.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `workflow-anschluss-skills-router`

**Frühere Beschreibung:** Anschluss-Skills Router im Plugin datenschutzrecht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor.

# Anschluss-Skills Router

## Aufgabe
Dieser Workflow-Skill für `datenschutzrecht` Anschluss-Skills Router im Plugin datenschutzrecht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

## Kaltstart
Wenn Material vorliegt, arbeite zuerst mit dem Material. Stelle nur Rückfragen, die für die nächste Weiche nötig sind:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 3. `workflow-chronologie-und-belegmatrix`

**Frühere Beschreibung:** Chronologie und Belegmatrix im Plugin datenschutzrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen.

# Chronologie und Belegmatrix

## Aufgabe
Dieser Workflow-Skill für `datenschutzrecht` Chronologie und Belegmatrix im Plugin datenschutzrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

## Kaltstart
Wenn Material vorliegt, arbeite zuerst mit dem Material. Stelle nur Rückfragen, die für die nächste Weiche nötig sind:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 4. `workflow-fristen-und-risikoampel`

**Frühere Beschreibung:** Fristen- und Risikoampel im Plugin datenschutzrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.

# Fristen- und Risikoampel

## Aufgabe
Dieser Workflow-Skill für `datenschutzrecht` Fristen- und Risikoampel im Plugin datenschutzrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

## Kaltstart
Wenn Material vorliegt, arbeite zuerst mit dem Material. Stelle nur Rückfragen, die für die nächste Weiche nötig sind:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Datenschutz-typische Fristen
- **Art. 33 DSGVO** – Meldung Datenpanne an Aufsichtsbehörde: **72 Stunden** ab Kenntnis.
- **Art. 34 DSGVO** – Benachrichtigung Betroffener: **unverzüglich** bei hohem Risiko.
- **Art. 12 Abs. 3 DSGVO** – Antwort auf Betroffenenanfragen (Art. 15 ff.): **1 Monat**, ggf. Verlängerung um zwei Monate.
- **Art. 36 DSGVO** – Vorherige Konsultation Aufsichtsbehörde bei DSFA mit hohem Restrisiko, Antwort der Behörde **8 Wochen** (verlängerbar).
- **Bußgeldrahmen**: Art. 83 Abs. 5 DSGVO bis **20 Mio. EUR oder 4 %** weltweiter Jahresumsatz.

## Ampelkriterien
- **Rot**: 72-Std-Frist (Art. 33) läuft, Bußgeldbescheid zugestellt, behördliche Anordnung, Drittlandstransfer ohne Garantien Art. 44 ff.
- **Gelb**: DSFA fehlt für ein bekanntes Hochrisiko-Verfahren, AVV unvollständig, Verzeichnis Art. 30 nicht aktuell.
- **Grün**: Rechtsgrundlage Art. 6/9 dokumentiert, Verzeichnis Art. 30 aktuell, DSFA durchgeführt, AVV + TOM vorhanden.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 5. `workflow-mandantenkommunikation`

**Frühere Beschreibung:** Mandantenkommunikation im Plugin datenschutzrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Aufgabe
Dieser Workflow-Skill für `datenschutzrecht` Mandantenkommunikation im Plugin datenschutzrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

## Kaltstart
Wenn Material vorliegt, arbeite zuerst mit dem Material. Stelle nur Rückfragen, die für die nächste Weiche nötig sind:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Mandantenkommunikation Datenschutz
- **Anrede + Bezug:** "In Sachen [Mandant] / Ihre datenschutzrechtliche Anfrage"
- **Sachstand kurz:** welche Daten, welche Rolle (Verantwortlich Art. 4 Nr. 7 / Auftragsverarbeiter Art. 4 Nr. 8), welche Rechtsgrundlage Art. 6/9 DSGVO einschlägig.
- **Empfehlung:** zentral umsetzbarer nächster Schritt (z. B. "DSFA durchführen, AVV nachverhandeln, Aufsichtsbehörde melden, Betroffene benachrichtigen").
- **Risikoampel** mit Bezug auf konkrete Bußgeldhöhe (Art. 83 Abs. 4: 10 Mio./2 %; Abs. 5: 20 Mio./4 %).
- **Frist:** insb. 72 Stunden (Art. 33), 1 Monat (Art. 12 Abs. 3), 13 Monate (Art. 17 Vergessen) konkret nennen.
- **Kostenhinweis:** RVG/Honorarvereinbarung.
- **Datenschutz-Hinweis intern:** keine Mandantendaten in unverschlüsselter E-Mail; bei Bedarf verschlüsselter Versand oder Datenraum.

## Praxis-Tipp
Bei Betroffenenanfragen die Mandantschaft frühzeitig über die Antwortpflicht aufklären — der häufigste Fehler ist Ablehnung "wir geben keine Daten heraus" ohne Rechtsgrundlage. Das löst regelmäßig Beschwerde bei der Aufsichtsbehörde und Bußgeldverfahren aus. Antwortverweigerung nur nach Art. 12 Abs. 5 (Missbrauch) oder § 34 BDSG (gesetzliche Ausnahme).

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 6. `workflow-output-waehlen`

**Frühere Beschreibung:** Output wählen im Plugin datenschutzrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung.

# Output wählen

## Aufgabe
Dieser Workflow-Skill für `datenschutzrecht` Output wählen im Plugin datenschutzrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

## Kaltstart
Wenn Material vorliegt, arbeite zuerst mit dem Material. Stelle nur Rückfragen, die für die nächste Weiche nötig sind:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Outputformen Datenschutz
- **Auskunftsentwurf nach Art. 15 DSGVO** mit Datenkopie, Empfängerliste, Speicherdauer, Widerspruchsrechten.
- **DSFA-Bericht** nach Art. 35 DSGVO mit Bewertungsmethodik, Risiken, Schutzmaßnahmen, Restrisikobewertung.
- **AVV-Redline** nach Art. 28 Abs. 3 DSGVO mit Markierungen für TOM-Anlage, Subunternehmer, Audit-Rechte.
- **Meldung nach Art. 33 DSGVO** (Datenpanne) — Standardformular der zuständigen Aufsichtsbehörde verwenden (BfDI / LfD-Portal).
- **Benachrichtigung der Betroffenen** nach Art. 34 DSGVO mit klarer Sprache, Beschreibung, Kontakt DSB.
- **Datenschutzhinweise** nach Art. 13/14 DSGVO mit allen Pflichtangaben.
- **Drittlandstransfer-Doku**: SCC-Modul-Auswahl + TIA + ggf. supplementary measures.

## Praxis-Tipp
Bei einer Datenpannenmeldung nach Art. 33 stets das Online-Meldeformular der zuständigen Behörde (z. B. BfDI-Meldeportal, LDI NRW-Formular) verwenden und parallel intern eine Aktennotiz mit Zeitlinie führen — die 72-Stunden-Frist verläuft schnell, eine spätere Rekonstruktion ist mühsam.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 7. `workflow-redteam-qualitygate`

**Frühere Beschreibung:** Red-Team Qualitygate im Plugin datenschutzrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieser Workflow-Skill für `datenschutzrecht` Red-Team Qualitygate im Plugin datenschutzrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

## Kaltstart
Wenn Material vorliegt, arbeite zuerst mit dem Material. Stelle nur Rückfragen, die für die nächste Weiche nötig sind:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Red-Team-Prüfpunkte Datenschutz
1. **Rollenklarheit:** Verantwortlicher (Art. 4 Nr. 7) vs. Auftragsverarbeiter (Art. 4 Nr. 8) vs. gemeinsame Verantwortlichkeit (Art. 26) klar?
2. **Rechtsgrundlage:** Art. 6 DSGVO einzeln benannt (Buchstaben a-f), nicht pauschal? Bei besonderen Datenkategorien Art. 9 zusätzlich?
3. **Drittlandstransfer:** DPF-Status zum Zeitpunkt der Prüfung gecheckt, SCC-Modul richtig, TIA dokumentiert?
4. **Fristen:** Art. 33 (72h), Art. 12 Abs. 3 (1 Monat), Art. 17 (Vergessen unverzüglich) richtig benannt?
5. **Beschäftigtendaten:** § 26 BDSG vs. Art. 88 DSGVO i.V.m. Tarifvertrag oder Betriebsvereinbarung?
6. **Verzeichnis Art. 30:** vollständig (Verantwortlicher + Auftragsverarbeiter)?
7. **Cookies/Tracking:** § 25 TDDDG (Einwilligung) vs. Art. 6 DSGVO (Verarbeitung) klar getrennt?
8. **Halluzinations-Check:** Keine erfundenen Aufsichtsbehörden-Stellungnahmen, keine BeckRS-Az. ohne Live-Quelle.

## Praxis-Tipp
Häufiger Fehler in der DSGVO-Beratung: Vermischung von TDDDG-Einwilligung (Endgerätezugriff, § 25 TDDDG) und DSGVO-Rechtsgrundlage (Verarbeitung pbD nach Art. 6). Beide sind kumulativ erforderlich für werbliche Cookies — Einwilligung nach TDDDG ersetzt nicht die Rechtsgrundlage nach DSGVO.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 8. `dsv-rechtsprechung-immaterieller-schaden-bgh-olg`

**Frühere Beschreibung:** Analysiert die deutsche Rechtsprechung zum immateriellen Schadensersatz nach Art. 82 DSGVO im Lichte der EuGH-Vorgaben. Behandelt: BGH-Entscheidungen zur Substantiierung; OLG-Linien zur Bagatellschwelle; OLG-Entscheidungen zur Beweislast bei Kontrollverlust; LG-Streuung bei Datenleck-Massenklagen; Schmerzensgeldgrößen; Kausalitäts-anforderungen. Output: Rechtsprechungs-Übersicht mit Begründungslinien. Abgrenzung: keine konkrete Verteidigung.

# Rechtsprechung BGH und OLG zum immateriellen Schaden Art. 82 DSGVO

## Triage — kläre vor der Bearbeitung

1. Welche Sachverhaltskonstellation liegt vor (Kontrollverlust; Phishing-Folge; Identitätsdiebstahl)?
2. Welche OLG-Region ist relevant?
3. Welche EuGH-Entscheidungen sind seit C-300/21 ergangen?
4. Welche Schmerzensgeldgrößen werden zugesprochen?
5. Welche Beweisanforderungen stellt das Gericht?
- Was will der Mandant wirklich erreichen? (rechtssichere Argumentation; passende Präzedenzen)

## Rechtsgrundlagen

- **Art. 82 DSGVO** Schadensersatz.
- **EuGH C-300/21 Österreichische Post** Auslegung Schadensbegriff.
- **EuGH C-687/21 Saturn** geringe Schwelle für Schadenseintritt.
- **EuGH C-456/22 Gemeinde Ummendorf** keine Bagatellgrenze für Schaden, aber Substantiierung erforderlich.
- **BGH VI ZR-Rechtsprechung** zur immateriellen Schadenshöhe.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; jede zitierte Entscheidung vor Ausgabe über bundesgerichtshof.de; openjur.de; eur-lex.europa.eu verifizieren mit Aktenzeichen Datum und Tenor.

## Zentrale Normen

Art. 82 DSGVO; § 253 Abs. 2 BGB; EuGH C-300/21; C-687/21; C-456/22.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Übersichtsraster

Spalte 1: Aktenzeichen und Gericht; Spalte 2: Datum; Spalte 3: Sachverhaltstyp; Spalte 4: Schadenshöhe zugesprochen; Spalte 5: tragende Argumente; Spalte 6: Quelle.

Verifikationsschritt: vor jeder Zitation prüfen — wegen Quellenregel keine Zitate aus Modellwissen.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-schadensersatz-art-82` deckt die konkrete Verteidigung ab.

## 9. `datenschutz-bussgeldverfahren-art-83-dsgvo-verteidigung`

**Frühere Beschreibung:** Bußgeldverteidigung nach Art. 83 DSGVO bis 4 Prozent Jahresumsatz oder 20 Mio. EUR. EDSA-Leitlinien 04/2022 zur Bemessung. Sieben-Fragen-Diagnose: Anhörung oder Bußgeldbescheid, Aufsichtsbehörde, Norm DSGVO/BDSG, Bezugsumsatz, Vorwurf, Verschulden, Maßnahmenlage. Schritt-für-Schritt: Akteneinsicht, keine vorschnelle Stellungnahme, dynamische Geldbemessung, EDSA-Methodik, § 41 BDSG, OWiG/StPO-Verfahrensgarantien. Einspruch nach § 67 OWiG binnen zwei Wochen. EuGH C-807/21 Deutsche Wohnen und C-683/21: Unternehmensgeldbuße ohne Identifizierung einer natürlichen Person, aber nicht ohne Vorsatz oder Fahrlässigkeit. Mustertexte Einspruch, Stellungnahme, Erledigungsvorschlag. Abgrenzung: keine zivilrechtliche Schadensersatzabwehr.

# Datenschutz-Bußgeldverfahren — Verteidigung nach Art. 83 DSGVO

## Zweck

Dieser Skill verteidigt den Mandanten im Bußgeldverfahren wegen DSGVO-Verstoß — von der Anhörung bis zum Einspruch nach § 67 OWiG und zum gerichtlichen Verfahren. Ziel ist die Vermeidung des Bußgeldbescheids, hilfsweise die Reduzierung der Geldbuße nach Art. 83 Abs. 2 DSGVO und den EDSA-Leitlinien 04/2022.

Terminologie sauber halten: Das ist kein Zivilprozess und keine Anklage im engeren strafprozessualen Sinn. Die Stationen heißen regelmäßig Anhörung, Bußgeldbescheid, Einspruch, Zwischenverfahren, Abgabe über die Staatsanwaltschaft an das zuständige Gericht, Hauptverhandlung oder Beschlussverfahren, Rechtsbeschwerde. Parallel können aufsichtsbehördliche Anordnungen nach Art. 58 Abs. 2 DSGVO verwaltungsgerichtlich anzugreifen sein.

## Wann brauchen Sie diesen Skill / Kaltstart-Fragen

Sie brauchen den Skill, sobald die Aufsichtsbehörde förmlich ein Bußgeldverfahren eingeleitet hat: Anhörung nach § 55 OWiG, Bußgeldbescheid nach § 65 OWiG oder laufende Einspruchsfrist nach § 67 OWiG.

Sieben-Fragen-Diagnose:

1. **Anhörung oder Bußgeldbescheid?** Andere Strategie pro Stand: Vor Bescheid Argumentationsspielraum, nach Bescheid Einspruchsfrist zwei Wochen ab Zustellung.
2. **Welche Aufsichtsbehörde?** Landesaufsicht oder BfDI? Federführend nach Art. 56 DSGVO (One-Stop-Shop)?
3. **Welche Norm wird verletzt?** Art. 5, 6, 9, 13, 14, 15, 17, 25, 28, 30, 32, 33, 34, 35, 37 DSGVO — und welche Sanktionsstufe Art. 83 Abs. 4 (10 Mio./2 Prozent) oder Art. 83 Abs. 5/6 (20 Mio./4 Prozent)?
4. **Bezugsumsatz:** Welcher Konzernumsatz wird zugrundegelegt — Mandantengesellschaft oder Mutter? EuGH C-807/21 Deutsche Wohnen relevant.
5. **Welche Vorwerfung?** Konkrete Handlung oder Unterlassen? Welcher Zeitraum?
6. **Verschulden:** Vorsatz, Fahrlässigkeit? Welche Organisation, welcher DSB, welche TOM?
7. **Maßnahmenlage:** Welche TOM Art. 32, welche DSFA Art. 35, welcher AVV Art. 28 lagen vor und sind dokumentiert?
8. **Parallelspur Art. 58 DSGVO?** Geht es nur um Geldbuße oder auch um Untersagung, Löschungsanordnung, Auskunftsauflage, Datenübermittlungsstopp oder sonstige aufsichtsbehördliche Maßnahme?

## Rechtlicher Rahmen

- **Art. 83 DSGVO** Bußgeldrahmen. Abs. 4 bis 10 Mio. EUR oder 2 Prozent. Abs. 5/6 bis 20 Mio. EUR oder 4 Prozent. Der jeweils höhere Wert gilt.
- **Art. 83 Abs. 2 DSGVO** Kriterien: Art, Schwere, Dauer, Vorsatz/Fahrlässigkeit, Schadensminderung, Verantwortlichkeit, Vorbelastung, Zusammenarbeit, Datenkategorien, Bekanntwerden, frühere Anordnungen, Zertifizierungen, finanzielle Vorteile.
- **EuGH C-807/21 Deutsche Wohnen** (Urteil 05.12.2023): Geldbuße gegen juristische Personen unmittelbar möglich, ohne dass eine natürliche Person identifiziert werden muss; erforderlich bleibt ein vorsätzlicher oder fahrlässiger Verstoß.
- **EuGH C-683/21 Nacionalinis visuomenės sveikatos centras** (Urteil 05.12.2023): Verantwortlichen-/Auftragsverarbeiterrollen, gemeinsame Verantwortlichkeit und Sanktionierbarkeit müssen unionsrechtlich sauber bestimmt werden; auch hier keine verschuldensunabhängige Geldbuße.
- **EDSA, Leitlinien 04/2022** zur Berechnung von Geldbußen (Final version 24.05.2023): harmonisierte Bemessungsmethodik, Startbetrag, Schweregrad, Umsatz-/Unternehmensgröße, erschwerende und mildernde Umstände, Höchstbetrag, Effektivität/Verhältnismäßigkeit/Abschreckung.
- **§ 41 BDSG** Anwendung OWiG.
- **§ 67 OWiG** Einspruch binnen zwei Wochen ab Zustellung.
- **§ 68 OWiG i.V.m. § 41 Abs. 1 BDSG** Gerichtliche Zuständigkeit: grundsätzlich Amtsgericht; bei festgesetzter DSGVO-Geldbuße über 100.000 EUR entscheidet nach § 41 BDSG das Landgericht.
- **§ 69 OWiG** Zwischenverfahren: Behörde prüft Rücknahme/Aufrechterhaltung; bei Aufrechterhaltung Übersendung über die Staatsanwaltschaft an das Gericht. Nach § 41 Abs. 2 BDSG kann die Staatsanwaltschaft nur mit Zustimmung der Aufsichtsbehörde einstellen.
- **§ 71 OWiG** Hauptverhandlung nach zulässigem Einspruch, sinngemäße Anwendung strafprozessualer Regeln.
- **§ 72 OWiG** Beschlussverfahren, wenn dafür die gesetzlichen Voraussetzungen vorliegen.
- **§ 73 OWiG** Anwesenheit/Entbindung des Betroffenen in der Hauptverhandlung, nicht der Name der Verhandlung selbst.
- **§ 79 OWiG** Rechtsbeschwerde.
- **§ 20 BDSG** Verwaltungsrechtsweg für Art.-78-Streitigkeiten gegen Aufsichtsbehörden; ausdrücklich nicht für Bußgeldverfahren. Relevant für Art.-58-Anordnungen, nicht für die Geldbuße selbst.

## Mandantenfuehrung Schritt-fuer-Schritt

1. **Zuerst: Frist sichern.** Einspruchsfrist nach § 67 I OWiG zwei Wochen ab Zustellung — sofort im Fristenkalender, Wiedereinsetzungspruefung bei Saeumnis.
2. **Akteneinsicht beantragen.** § 49 OWiG i.V.m. § 147 StPO. Erst danach Strategie.
3. **NICHT vorschnell Stellungnahme.** Auch nicht "kooperativ" Daten nachschieben — kann den Vorwurf verschaerfen.
4. **Prüfen: Zuständigkeit und Verfahrensweg.** § 41 BDSG-Sonderzuständigkeit bei Geldbußen über 100.000 EUR beachten; Bußgeldspur nicht mit verwaltungsgerichtlicher Art.-58-Spur vermischen.
5. **Prüfen: Bemessung nach EDSA 04/2022.** Prüfen, ob die Aufsicht die Methodik sauber angewendet hat. Bezugsumsatz richtig? Schweregrad richtig? Mildernde Umstände berücksichtigt?
6. **Verschuldensfrage:** Hat die Aufsicht Vorsatz oder Fahrlässigkeit konkret begründet? Nach EuGH C-807/21 muss kein Organ oder Beschäftigter namentlich identifiziert werden, aber ein schuldhafter Unternehmensverstoß muss tragfähig dargelegt sein.
7. **Einspruch einlegen.** Auch nur fristwahrend, Begründung nach Akteneinsicht.
8. **Erledigungsgespräch erwägen.** Insbesondere bei Erstverstoß, dokumentierter Selbstmeldung Art. 33, nachweislichem Maßnahmenplan und vertretbarer Bemessungskorrektur.

## Trade-off-Matrix

| Variante | Vorteil | Nachteil |
|---|---|---|
| Voller Einspruch + gerichtliches Verfahren | Sachprüfung, keine Bindung an Behördenbewertung | Hauptverhandlung/Öffentlichkeit, Kosten- und Reputationsrisiko |
| Beschlussverfahren § 72 OWiG anstreben | Schnelle, schriftliche Erledigung möglich | Nur bei passendem Verfahrensstand und Einverständnis-/Widerspruchslage sinnvoll |
| Einspruchsrücknahme nach Akteneinsicht/Termin | Begrenzung weiterer Risiken | Bestandskraft, kein Einfluss mehr |
| Selbstmeldung + Kooperation vor Bescheid | Bußgeldmilderung Art. 83 Abs. 2 lit. c/f/h DSGVO möglich | Selbstbelastungs- und Scope-Erweiterungsrisiko |
| Verschuldens-Bestreitung EuGH C-807/21/C-683/21 | Kernargument gegen schematische Unternehmenshaftung | Nur stark, wenn Compliance-Organisation, TOMs und Eskalationslogik belegbar sind |
| Verwaltungsgerichtliche Abwehr Art. 58 DSGVO | Stoppt/prüft Auflagen, Untersagungen, Löschungs- oder Transferanordnungen | Andere Fristen, anderer Rechtsweg, keine automatische Lösung des Bußgeldverfahrens |

## Mustertexte

### Einspruch (fristwahrend)

> An die [Aufsichtsbehörde]
> Aktenzeichen: [Az]
>
> Gegen den Bußgeldbescheid vom [Datum], zugestellt am [Datum], wird in vollem Umfang Einspruch eingelegt.
>
> Die Begruendung erfolgt nach Akteneinsicht.
>
> Wir beantragen Akteneinsicht in den vollstaendigen Vorgang nach § 49 OWiG in Verbindung mit § 147 StPO.

### Stellungnahme Anhörung — Strukturvorschlag

> 1. Verfahrensrechtliche Rügen (Zuständigkeit, Anhörung, Akteneinsicht).
> 2. Tatbestand (DSGVO-Norm konkret, Subsumtion mit Belegen).
> 3. Verschulden (EuGH C-807/21 — konkrete Pflichtverletzung des Unternehmens? Welche Organisation, welche Maßnahmen lagen vor?).
> 4. Bemessung nach EDSA 04/2022 (Bezugsumsatz, Schritte 1-5).
> 5. Mildernde Umstände Art. 83 Abs. 2 DSGVO (Maßnahmen, Kooperation, kein Vorteil, keine Vorbelastung).
> 6. Antrag: Einstellung; hilfsweise Verwarnung nach Art. 58 II b DSGVO; hilfsweise Reduzierung auf [Betrag].

### Erledigungsvorschlag (Anhörung)

> Sehr geehrte Damen und Herren,
>
> ohne Anerkennung einer Rechtspflicht und unter Beibehaltung sämtlicher Verteidigungsrechte schlägt unsere Mandantin folgende einvernehmliche Erledigung vor:
>
> 1. Umsetzung eines Maßnahmenplans bis [Datum] (Anlage).
> 2. Geldbuße [Betrag] in [Raten].
> 3. Verzicht auf Veröffentlichung der Entscheidung mit Namensnennung.
>
> Mit freundlichen Gruessen

## Typische Fehler

- Einspruchsfrist § 67 OWiG verpasst, weil Bescheid an alte Anschrift zugestellt.
- Verschuldensfrage nicht konkret gepruefte EuGH C-807/21 — Unternehmen muss vorsaetzlich oder fahrlaessig gehandelt haben, nicht eine namentlich benannte natuerliche Person.
- EDSA-Schritte unkommentiert akzeptiert.
- Vergleich ohne Vorbehalt der Verteidigungsrechte.
- Konzernumsatz-Bezugsfrage nicht angegriffen (Mandantengesellschaft vs Mutter).

**Was triggert die Aufsichtsbehörde besonders zur Höchststrafe?** Wiederholungstäter, Verletzung Art.-9-Daten, fehlende DSB-Bestellung trotz § 38 BDSG, fehlender AVV Art. 28 DSGVO, fehlende DSFA Art. 35 DSGVO.

## Querverweise

- `datenschutz-mandantenkommunikation-aufsichtsbehoerde`
- `datenschutz-datenpanne-art-33-34-72h-incident-response`
- `datenschutz-schadensersatz-art-82-dsgvo-gerichtsstreit`
- `datenschutz-erstgespraech-mandantenmatrix-7-fragen`

## Quellen Stand 06/2026

- DSGVO Art. 5, 6, 25, 32, 33, 35, 37, 58, 83.
- BDSG § 38, § 41, § 43.
- OWiG § 46, § 49, § 55, § 65, § 67, § 69, § 73, § 79.
- StPO § 147.
- EuGH C-807/21 Deutsche Wohnen, Urteil 05.12.2023.
- EDSA, Leitlinien 04/2022 zur Berechnung der Geldbussen nach DSGVO, Version 1.0, angenommen 24.05.2023.
- Keine Aufsatzfundstellen aus Modellwissen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 10. `dsv-sanktion-beschlussverfahren-72-owig`

**Frühere Beschreibung:** Datenschutzrecht-Brückenskill: Beschlussverfahren § 72 OWiG: Schriftliche Erledigung per Beschluss prüfen, wenn Tatsachen und Verfahrenslage dafür taugen. Spezialskill für Datenschutz-Sanktionsverfahren, Bußgeldverteidigung, Aufsichtsbehördenkommunikation und gerichtlichen Rechtsschutz. Bei ernstem Behörden- oder Bußgelddruck Spezialplugin datenschutz-sanktionsverfahren-verteidigung laden.

# Beschlussverfahren § 72 OWiG

## Aufgabe

Schriftliche Erledigung per Beschluss prüfen, wenn Tatsachen und Verfahrenslage dafür taugen.

Dieser Skill arbeitet als Brücke im allgemeinen Plugin `datenschutzrecht`. Er darf nicht austauschbar antworten: immer zuerst Verfahrensstand, Behörde, Frist, Rechtsweg, Beweisstand und gewünschtes Arbeitsprodukt klären.

## Kaltstart-Fragen

1. Welches Schreiben oder welcher Verfahrensschritt liegt vor: informelle Anfrage, Art.-58-Auskunftsverlangen, Anhörung, Bußgeldbescheid, Einspruch, gerichtliches Bußgeldverfahren, Art.-58-Anordnung, Verwaltungsgericht oder Rechtsmittel?
2. Welche Behörde handelt: Landesdatenschutzaufsicht, BfDI, kirchliche Datenschutzaufsicht, federführende EU-Aufsicht oder andere Spezialaufsicht?
3. Wer ist Adressat und in welcher Rolle: Verantwortlicher, Auftragsverarbeiter, gemeinsame Verantwortliche, Konzernmutter, Tochter, öffentliche Stelle oder natürliche Person?
4. Welche Frist läuft und wie wurde zugestellt oder bekanntgegeben?
5. Welche Tatsachen sind durch Akte, Logs, Verträge, DSFA, TOM, AVV, DSB-Vermerk oder Zeugen belegbar?
6. Soll die Ausgabe Akteneinsicht, Fristverlängerung, Stellungnahme, Einspruch, Klage, Eilantrag, Terminsmappe oder Management-Briefing sein?

## Rechtsanker

- Art. 83 DSGVO
- § 41 BDSG
- §§ 49, 55, 65, 67, 68, 69, 71, 72, 73, 79 OWiG
- § 147 StPO

## Arbeitsprogramm

1. **Spur trennen.** Bußgeld nach Art. 83 DSGVO/§ 41 BDSG/OWiG ist nicht dasselbe wie Verwaltungsrechtsschutz gegen Art.-58-Anordnungen nach § 20 BDSG. Parallelspuren getrennt führen.
2. **Frist sichern.** Einspruchs- und Rechtsbehelfsfristen sofort mit Zustellnachweis notieren; weiche Behördenfristen separat behandeln.
3. **Akteneinsicht und Beweisstand.** Keine endgültige Tatsachenstellungnahme ohne Akteneinsicht, wenn ein Bußgeldverfahren erkennbar ist. Technische Behauptungen anhand Logs, Systemarchitektur und Verantwortlichkeiten prüfen.
4. **Materiell prüfen.** DSGVO-Norm, Verantwortlichenrolle, Pflichtverletzung, Vorsatz/Fahrlässigkeit, Art.-83-Bemessung oder Art.-58-Ermessensausübung sauber subsumieren.
5. **Taktisch schreiben.** Kooperativ, aber geschützt: keine unnötigen Schuldeingeständnisse, keine nicht belegten Behauptungen, keine Vermischung von Datenschutzberatung und Verteidigung.
6. **Nächsten Schritt auswerfen.** Immer mit Risikoampel, konkreten Unterlagen, Freigabeentscheidung und empfohlenen Anschlussskills schließen.

## Typische Fehler, die der Skill vermeiden muss

- Bußgeldverfahren als normales Verwaltungsverfahren behandeln.
- Art.-58-Anordnung und Bußgeldbescheid in denselben Rechtsweg werfen.
- "Anklage" sagen, wo es im OWiG um Bußgeldbescheid, Einspruch, Zwischenverfahren und gerichtliche Hauptverhandlung geht.
- § 73 OWiG als Bezeichnung der mündlichen Verhandlung missverstehen; die Hauptverhandlung steht in § 71 OWiG.
- EuGH C-807/21 als verschuldenslose Unternehmenshaftung lesen. Das ist falsch: keine Identifizierung einer natürlichen Person nötig, aber Vorsatz oder Fahrlässigkeit bleibt nötig.
- Rechtsprechung oder Behördenpraxis ohne live verifizierbare Quelle zitieren.

## Output

Verteidigungsbaustein für OWiG-Verfahren mit Akteneinsicht, Einspruch, Beweisthemen und Terminstrategie.

## Übergabe an das Spezialplugin

Bei substanziellem Bußgeld-, Art.-58- oder Gerichtsrisiko lade zusätzlich `datenschutz-sanktionsverfahren-verteidigung` und dort insbesondere `kaltstart-verfahrensstand-und-mandatsziel`, `akteneinsicht-49-owig-147-stpo`, `zustaendigkeit-amtsgericht-landgericht-41-bdsg`, `art-83-abs-2-kriterien-einzeln` und `art-58-anordnung-verwaltungsakt`.


## Quellen- und Verifikationsregel

- Normen vor Ausgabe live prüfen, besonders DSGVO Art. 58, 78 und 83, BDSG § 20 und § 41 sowie OWiG §§ 49, 55, 65, 67, 68, 69, 71, 72, 73 und 79.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und offizieller oder frei zugänglicher Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.
- EuGH C-807/21 und C-683/21 nur mit sauberer Kernaussage nutzen: unmittelbare Unternehmensgeldbuße ja; verschuldenslose Haftung nein.
- Wenn ein Punkt nicht verifiziert ist, als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
