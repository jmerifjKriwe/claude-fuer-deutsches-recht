# Megaprompt: datenschutzrecht

> *Achtung: Dies ist ein experimentelles Mega-Prompt-Markdown, das einen kompletten Klotzkette-Plugin in eine einzige Datei zusammenfuehrt. Keine Haftung, keine Gewaehr. Nur zum Ausprobieren der Skills auch ohne Claude Code; keine Rechtsberatung. Vor Verwendung im Mandat anwaltlich pruefen.*
>
> *Caution: This is an experimental Mega-Prompt Markdown that consolidates a full Klotzkette plugin into a single file. No warranty, no liability. For exploration with chat tools that do not run Claude Code only; not legal advice.*

**Verwendung:** Diesen gesamten Text in einen Chat ohne Claude-Code-Integration einfuegen (oder als Datei hochladen). Der Chat-Agent erhaelt damit die gebuendelten Skills dieses Plugins als Kontext. Eine Replikation des vollen Plugin-Verhaltens ist nicht garantiert — der Megaprompt ist eine Best-Effort-Kompression.


## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 362 Skills des Plugins `datenschutzrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Datenschutzrecht DSGVO/BDSG: ordnet Rolle (Verantwortlicher, Auftragsverarbeiter, Betro…
2. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting im Datenschutzrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und …
3. **dsgvo-erstpruefung-und-mandatsziel** — DSGVO: Erstprüfung, Rollenklärung und Mandatsziel: DSGVO: Erstprüfung, Rollenklärung und Mandatsziel.
4. **anpassen** — Bestehende Datenschutzdokumentation oder Richtlinien an neue Anforderungen oder Verarbeitungstätigkeiten anpassen. Art. …
5. **anwendungsfall-triage** — Datenschutzrechtlichen Sachverhalt einordnen und Bearbeitungsroute bestimmen. Art. 2 3 DSGVO Anwendungsbereich § 1 BDSG.…
6. **art-9-besondere-kategorien** — Bewertet einen Datenschutzvorfall mit besonderen Kategorien personenbezogener Daten nach Art. 9 DSGVO. Behandelt: rassis…
7. **aufnahme-statusinformation** — Erstellt nach einem gemeldeten Datenschutzvorfall eine knappe Statusinformation an Mandant und Datenschutzbeauftragten i…
8. **avv-art-28-dsgvo-grundtatbestand** — Grundtatbestand der Auftragsverarbeitung nach Art. 28 DSGVO. Klaert Rollenzuordnung Verantwortlicher gegen Auftragsverar…
9. **avv-art-28-mindestinhalte-checkliste** — Vollstaendige Pflichtinhalte-Checkliste für einen AVV nach Art. 28 Abs. 3 lit. a bis h DSGVO. Jede der acht Pflichtklaus…
10. **avv-eu-kommission-musterklauseln-2021-915** — EU-Kommissions-Standardvertragsklauseln zwischen Verantwortlichem und Auftragsverarbeiter nach Beschluss (EU) 2021/915 v…
11. **avv-eu-us-data-privacy-framework-bezug** — Behandlung des EU-US Data Privacy Framework (DPF) im AVV. Angemessenheitsbeschluss EU-Kommission vom 10.07.2023 Beschlus…
12. **avv-haftung-risikoallokation-art-82-dsgvo** — Haftungsverteilung Risikoallokation und Haftungscaps im AVV im Lichte von Art. 82 DSGVO. Klaert Aussenhaftung gegenueber…
13. **avv-konzern-und-multi-party-konstellation** — AVV im Konzern und in Multi-Party-Konstellationen. Behandelt Konzern-AVV mit zentraler Group-IT Shared-Service-Center un…
14. **avv-loeschung-rueckgabe-nach-vertragsende** — Pflicht zur Loeschung oder Rueckgabe personenbezogener Daten nach Ende des Auftragsverarbeitungsvertrags gemaess Art. 28…
15. **avv-pruefung** — Auftragsverarbeitungsvertrag nach Art. 28 DSGVO prüfen oder erstellen wenn Dritter Daten im Auftrag verarbeitet. Art. 28…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Datenschutzrecht DSGVO/BDSG: ordnet Rolle (Verantwortlicher, Auftragsverarbeiter, Betroffener), markiert Frist (Art. 33 Meldung 72h), wählt Norm (DSGVO Art. 5/6/13/15/28/32/33/35, BDSG, TTDSG) und Zuständigkeit (BfDI Bund), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Datenschutzrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `anpassen` — Anpassen
- `einstieg-schnelltriage-fallrouting` — Anschluss
- `anwendungsfall-triage` — Anwendungsfall Triage
- `art-9-besondere-kategorien` — ART 9 Besondere Kategorien
- `dsv-art-9-besondere-kategorien` — ART Besondere Aufnahme Statusinformation
- `aufnahme-statusinformation` — Aufnahme Statusinformation
- `auskunft-behoerden-gerichts-registerweg` — Auskunft Behoerden Gerichts Registerweg
- `avv-art-26-joint-controllership-deutsch` — AVV ART 26 Joint Controllership Deutsch
- `avv-art-28-dsgvo-grundtatbestand` — AVV ART 28 DSGVO Grundtatbestand
- `avv-art-28-mindestinhalte-checkliste` — AVV ART 28 Mindestinhalte Checkliste
- `avv-audit-und-kontrollrechte` — AVV Audit und Kontrollrechte
- `avv-cloud-und-subverarbeitung-art-28-iv` — AVV Cloud und Subverarbeitung ART 28 IV
- `avv-eu-kommission-musterklauseln-2021-915` — AVV EU Kommission Musterklauseln 2021 915
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Datenschutzrecht sind Art. 15, Art. 33, Art. 44, BDSG, DSGVO, TDDDG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting im Datenschutzrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig:..._

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Datenschutzrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Datenschutzrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** DSGVO/BDSG/TDDDG – PIA/DPIA, AVV-Review als Verantwortlicher und Auftragsverarbeiter, Auskunftsersuchen Art. 15, Datenpannenmeldung Art. 33/34, Drittlandstransfer Art. 44 ff., US-Transfer mit DPF/SCC/TIA, Behördenpaket, Drift-Monitoring.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
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
- **Primärer Pfad:** `passender-datenschutz-skill` — [warum dieser Arbeitsgang hilft]
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
4. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.

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

### 5. Fachmodule in diesem Plugin

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

Dieses Plugin unterstuetzt Rechtsanwaelte und Datenschutzbeauftragte bei der Bearbeitung datenschutzrechtlicher Mandate nach DSGVO und BDSG. Es deckt den vollstaendigen ab: von der ersten Triage ueber Auftragsverarbeitungsvertraege, Datenschutz-Folgenabschaetzungen und Auskunftsersuchen bis zu Datenpannenmeldungen, Drittlandstransfers, US-Transfer-Dokumentation und der laufenden Richtlinienpflege.

Der Anwendungsbereich umfasst Unternehmen als Verantwortliche (Art. 4 Nr. 7 DSGVO), Auftragsverarbeiter (Art. 4 Nr. 8 DSGVO) und gemeinsam Verantwortliche (Art. 26 DSGVO), sowie den Einsatz von KI-Tools im Kanzleialltag.

## Wann brauchen Sie diese Skill?

- Ein Unternehmen erhaelt ein Auskunftsersuchen nach Art. 15 DSGVO und braucht eine rechtskonforme Antwort.
- Ein Datenschutzbeauftragter muss eine Datenpanne nach Art. 33 DSGVO binnen 72 Stunden an die Aufsichtsbehoerde melden.
- Eine Kanzlei prueft, ob ein IT-Dienstleister einen Auftragsverarbeitungsvertrag nach Art. 28 DSGVO benoetigt.
- Ein Unternehmen will Daten in ein Drittland (USA, Indien) uebertragen und braucht einen Transfer-Impact-Assessment.
- Eine Aufsichtsbehoerde fragt nach US-Transfer, DPF-Listing, SCC, TIA und Schrems-II-Dokumentation.
- Eine Behörde oder Kanzlei prueft, ob KI-Werkzeuge datenschutzkonform eingesetzt werden koennen.

## Fachbegriffe (kurz erklaert)

- **DSGVO** — Datenschutz-Grundverordnung (EU 2016/679); einheitliches EU-Datenschutzrecht für Verarbeitung personenbezogener Daten.
- **BDSG** — Bundesdatenschutzgesetz; ergaenzt die DSGVO im deutschen Recht, insbesondere für Beschaeftigtendatenschutz (§ 26 BDSG).
- **TDDDG** — Telekommunikation-Digitale-Dienste-Datenschutzgesetz; Nachfolger des TTDSG, regelt Cookies und Online-Tracking.
- **AVV** — Auftragsverarbeitungsvertrag nach Art. 28 DSGVO; Pflichtvertrag, wenn ein Dritter Daten im Auftrag verarbeitet.
- **DSFA** — Datenschutz-Folgenabschaetzung (Data Protection Impact Assessment, DPIA) nach Art. 35 DSGVO; Pflicht bei hohem Risiko.
- **Drittland** — Staat ausserhalb des EWR, in den Datentransfers nur unter bestimmten Voraussetzungen zulaessig sind (Art. 44 ff. DSGVO).
- **VVT** — Verzeichnis der Verarbeitungstaetigkeiten nach Art. 30 DSGVO; Dokumentationspflicht für Verantwortliche und Auftragsverarbeiter.
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

## Schritt-für-Schritt: Einstieg ins Plugin

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
- `dsb-bestellungspflicht-pruefung` — Bestellungspflicht für Datenschutzbeauftragten nach Art. 37 DSGVO und § 38 BDSG pruefen.
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

## Quellen und Aktualitaet

- Stand: 05/2026
- DSGVO (EU 2016/679) in der zum Stand-Datum geltenden Fassung
- BDSG in der geltenden Fassung
- TDDDG in der geltenden Fassung
- Standardvertragsklauseln der EU-Kommission (2021/914)
- EU-US Data Privacy Framework-Angemessenheitsbeschluss der EU-Kommission vom 10.07.2023 und offizielle DPF-Participant-Search.

---

## Skill: `dsgvo-erstpruefung-und-mandatsziel`

_DSGVO: Erstprüfung, Rollenklärung und Mandatsziel: DSGVO: Erstprüfung, Rollenklärung und Mandatsziel._

# DSGVO: Erstprüfung, Rollenklärung und Mandatsziel


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO; BDSG; TDDDG; Art. 44 ff — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** DSGVO: Erstprüfung, Rollenklärung und Mandatsziel.

## Spezialwissen: DSGVO: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** DSGVO, BDSG, TDDDG, PIA, DPIA, AVV, Art. 15, Art. 33, Art. 44, US, DPF, SCC.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **DSGVO** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## DSGVO-Erstprüfung: 7-Schritte-Matrix
1. **Personenbezug:** Liegen Daten i.S.d. Art. 4 Nr. 1 vor? Pseudonymisierung ohne Schlüssel = noch personenbezogen (BGH); Anonymisierung technisch oft nicht belastbar.
2. **Rolle:** Verantwortlicher (Art. 4 Nr. 7) — entscheidet über Mittel und Zwecke; Auftragsverarbeiter (Art. 4 Nr. 8) — verarbeitet auf Weisung; Gemeinsame Verantwortliche (Art. 26).
3. **Rechtsgrundlage Art. 6:** Einwilligung (lit. a), Vertrag (lit. b), gesetzliche Pflicht (lit. c), berechtigtes Interesse (lit. f) — letzteres mit LIA.
4. **Besondere Kategorien Art. 9?** Gesundheit, Religion, sexuelle Orientierung, biometrische ID, ethnische Herkunft — eigene Rechtsgrundlage.
5. **DSFA-Pflicht Art. 35?** Bei voraussichtlich hohem Risiko (Profiling, sensible Daten, neue Technologien, Beobachtung öffentl. Bereich).
6. **Drittlandstransfer:** EU/EWR/Adäquanzbeschluss → frei. USA → DPF/SCC + TIA. Sonstige → SCC + TIA.
7. **Ziel:** Compliance-Aufbau, Auskunft beantworten, Datenpanne melden, Behörde verteidigen?

## Trade-off
Einwilligung (Art. 6 Abs. 1 lit. a) ist klar, aber jederzeit widerrufbar (Art. 7 Abs. 3) — bei laufender Verarbeitung problematisch (z. B. KI-Modell-Training). Berechtigtes Interesse (lit. f) ist robuster, aber abwägungsanfällig — dokumentierte LIA (Legitimate Interest Assessment) ist Pflicht.

---

## Skill: `anpassen`

_Bestehende Datenschutzdokumentation oder Richtlinien an neue Anforderungen oder Verarbeitungstätigkeiten anpassen. Art. 5 24 DSGVO Rechenschaftspflicht. Prüfraster: Bestandsaufnahme Lueckenanalyse DSGVO-Anforderungen BDSG-Besonderheiten Anpassungsbedarf. Output: Anpassungsprotokoll ueberarbeitete..._

# Customize – Praxisprofil anpassen

## Eingaben

- Welcher Abschnitt soll geändert werden? (frei formuliert oder Menüauswahl)
- Neuer Wert oder neue Position
- Optional: Beleg für die Änderung (z.B. neues Gerichtsurteil, neue EDSA-Leitlinie, Managemententscheidung)

## Ablauf

1. **Abschnitt identifizieren.** Nutzer nennt, was geändert werden soll. Bei Unklarheit eine strukturierte Liste der änderbaren Bereiche anzeigen:
 - Organisationsdaten (Name, Rechtsform, Standort)
 - Zuständige Aufsichtsbehörde
 - Rolle (Verantwortlicher / Auftragsverarbeiter)
 - Datenschutzbeauftragte·r (Name, intern/extern)
 - Rechtsgrundlagen-Übersicht (Art. 6/9 DSGVO)
 - AVV-Playbook (Klausel-Positionen, Deal-Breaker)
 - Drittlandtransfer-Mechanismen (SCC, DPF, BCR)
 - Systemliste für Betroffenenanfragen
 - DSFA-Format und Auslöser
 - Datenschutzerklärungsangaben
 - Ausgaben-Konfiguration (Ordner, Namenskonvention)
 - Integrations-Einstellungen

2. **Aktuellen Wert zeigen.** Den aktuellen Wert aus `CLAUDE.md` lesen und ausgeben, damit der Nutzer die Änderung klar gegen den Ist-Zustand vergleichen kann.

3. **Änderung vorbereiten.** Neuen Wert formulieren. Bei normativen Änderungen (z.B. neue Aufsichtsbehörde wegen Art. 56 DSGVO) die Rechtsgrundlage der Änderung nennen.

4. **Bestätigung einholen.** Den geplanten Schreibvorgang explizit bestätigen lassen – vor dem Überschreiben.

5. **Schreiben.** `CLAUDE.md` an der betroffenen Stelle aktualisieren. Rest unverändert lassen.

6. **Zusammenfassung.** Was wurde geändert, was blieb unverändert, gibt es Folgeaktionen (z.B. Datenschutzerklärung aktualisieren nach geänderter Systemliste)?

## Quellen und Zitierweise

Verbindlich nach `../../references/zitierweise.md`.

- Art. 56 DSGVO (federführende Aufsichtsbehörde)
- Art. 37 DSGVO, § 38 BDSG (DSB-Benennungspflicht)
- Art. 28 DSGVO (AVV-Mindestanforderungen für Playbook-Änderungen)
- Art. 46, 47, 49 DSGVO (Drittlandtransfer-Mechanismen)
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Beispiel

**Situation:** Das Unternehmen zieht seinen Hauptsitz von Bayern nach Hessen.

**Analyse:**
Die Zuständigkeit der Aufsichtsbehörde richtet sich nach der Hauptniederlassung in der EU, Art. 56 Abs. 1 DSGVO. Mit Umzug nach Hessen wechselt die federführende Aufsichtsbehörde vom Bayerischen Landesamt für Datenschutzaufsicht (BayLDA) zum Hessischen Beauftragten für Datenschutz und Informationsfreiheit (HBDI). Für laufende Aufsichtsverfahren beim BayLDA ist der Wechsel mit Hauptniederlassungsverlegung dem BayLDA mitzuteilen (Art. 60 Abs. 1 DSGVO analog, h.M.).

**Änderung:**
```
Zuständige Aufsichtsbehörde: HBDI (zuvor: BayLDA)
Rechtsgrundlage: Art. 56 Abs. 1 DSGVO
Datum: [Umzugsdatum]
Folgeaktionen: Laufende Verfahren beim BayLDA auf HBDI übertragen; Datenschutzerklärung (Aufsichtsbehördenverweis) aktualisieren; Kontaktdaten HBDI in CLAUDE.md einpflegen.
```

## Risiken / typische Fehler

- **Teilaktualisierung vergessen:** Wer den DSB wechselt, muss auch die Datenschutzerklärung und ggf. das Verarbeitungsverzeichnis (Art. 30 Abs. 1 lit. a DSGVO: Name und Kontakt DSB) aktualisieren.
- **AVV-Playbook ohne Begründung:** Änderungen an Klauselpositionen sollten mit Datum und Anlass dokumentiert werden (Präzedenzfall, Gerichtsurteil, Managemententscheidung), damit spätere Prüfer die Position nachvollziehen können.
- **Integrations-Änderungen ohne Test:** Neue Connector-Einstellung erst nach erfolgreichem Test-Aufruf als ✓ markieren.
- **Überschreiben von Mandats-Ebene:** Wenn Mandat-Arbeitsbereiche aktiviert sind, prüfen, ob die Änderung das Praxisprofil oder nur ein einzelnes Mandat betrifft. Mandat-Ebene überschreibt Praxisprofil nur für dieses Mandat.

## Quellen / Updates

Stand: 05/2026. Bei BDSG-Novellen, neuen BRAO-Regeln oder Aufsichtsbehörden-Neustrukturierungen Skill aktualisieren.

**Querverweise:**
- `datenschutzrecht/skills/datenschutzrecht-kaltstart-interview/SKILL.md` — Vollständige Neukonfiguration
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md` — Drittlandtransfer-Mechanismen im Praxisprofil

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage zu Beginn

1. Was genau soll geändert werden? (Aufsichtsbehörde / AVV-Dealbreaker / Systemliste / DSB)
2. Hat die Änderung Auswirkungen auf andere Dokumente (Datenschutzerklärung, VVT, DSFA)?
3. Liegt ein Beleg (Urteil, EDSA-Leitlinie, Managemententscheidung) für die Änderung vor?
4. Betrifft die Änderung das Praxisprofil oder nur ein einzelnes Mandat?

## Output-Template — Änderungsbestätigung

**Adressat:** Datenschutzbeauftragter / Kanzlei intern — Tonfall: sachlich-strukturiert

```
Praxisprofil-Änderungsprotokoll [DATUM]
Abschnitt: [ABSCHNITT]
Alter Wert: [ALTER WERT]
Neuer Wert: [NEUER WERT]
Beleg/Rechtsgrundlage: [NORM / BESCHLUSS / DATUM]
Folgeaktionen:
- Datenschutzerklaerung aktualisieren: [ja/nein]
- VVT aktualisieren: [ja/nein]
- Aufsichtsbehoerde informieren: [ja/nein]
- Weitere: [...]
Durchgefuehrt von: [SACHBEARBEITER]
```

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 5 DSGVO (Grundsätze der Verarbeitung)
- Art. 6, 9 DSGVO (Rechtsgrundlagen, besondere Datenkategorien)
- Art. 13, 14 DSGVO (Informationspflichten)
- Art. 15 DSGVO (Auskunftsrecht)
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 32 DSGVO (Sicherheit der Verarbeitung)
- Art. 33, 34 DSGVO (Meldepflichten bei Verletzung)
- Art. 82 DSGVO (Schadensersatz)
- Art. 83 DSGVO (Bußgelder)
- §§ 4, 20, 41 BDSG (Aufsicht, Rechtsweg, Strafvorschriften)

### Leitentscheidungen

- EuGH C-300/21 (immaterieller Schaden Art. 82 DSGVO)
- EuGH C-634/21 (automatisierte Bonitätsbewertung Schufa)
- EuGH C-26/22 (Datenschutzbehörden-Befugnisse)
- EuGH C-807/21 (Bußgeldhaftung juristischer Personen)
- BVerfG 1 BvR 16/13 (Recht auf Vergessen I)

### Anwendung im Skill

- Rechtsgrundlage nach Art. 6 DSGVO sauber waehlen; berechtigte Interessen nach Art. 6 Abs. 1 lit. f DSGVO mit dokumentierter Abwaegung.
- Bei Datenpannen die 72-Stunden-Frist nach Art. 33 DSGVO einhalten; Risikoabwaegung Art. 34 DSGVO separat dokumentieren.
- Auskunftsanspruch Art. 15 DSGVO nicht mit Kopie nach Art. 15 Abs. 3 DSGVO verwechseln; EuGH C-307/22 Reichweite beachten.

---

## Skill: `anwendungsfall-triage`

_Datenschutzrechtlichen Sachverhalt einordnen und Bearbeitungsroute bestimmen. Art. 2 3 DSGVO Anwendungsbereich § 1 BDSG. Prüfraster: Anwendungsbereich personenbezogene Daten Verantwortlicher Auftragsverarbeiter Drittland. Output: Triage-Memo Bearbeitungsroute Normenmap. Abgrenzung: Einstieg und T..._

# Datenschutz-Triage neuer Verarbeitungsvorgänge

## Aktenstart statt Formularstart

Wenn zu **Anwendungsfall Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Datenschutzrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Eingaben

- Beschreibung des Verarbeitungsvorgangs (Datenarten, Zweck, Betroffenenkreis)
- Datenkategorien (Art. 4 Nr. 1, Art. 9 DSGVO); Beschäftigtendaten (§ 26 BDSG)?
- Neu erhoben oder Zweckänderung bei vorhandenen Daten (Art. 5 Abs. 1 lit. b DSGVO)?
- Auftragsverarbeiter / Drittland-Übermittlung?
- Automatisierte Entscheidungsfindung (Art. 22 DSGVO)?
- Cookies / Endgerätezugriff (§§ 24 ff. TDDDG)?

## Rechtlicher Rahmen

### Kernvorschriften

- **DSGVO:** Art. 5 (Grundsätze), Art. 6 (Rechtsgrundlagen), Art. 9 (besondere
 Kategorien), Art. 13/14 (Informationspflichten), Art. 17 (Löschrecht), Art. 22
 (automatisierte Entscheidungen), Art. 25 (Privacy by Design/Default), Art. 28 (AVV),
 Art. 30 (Verarbeitungsverzeichnis), Art. 32 (TOM), Art. 35 (DSFA), Art. 44 ff.
 (Drittlandtransfer).
- **BDSG:** § 22 (Gesundheits-/Sozialdaten), § 26 (Beschäftigtendatenschutz), § 38
 (betrieblicher DSB).
- **TDDDG (ehem. TTDSG):** §§ 24 ff. — Einwilligung für Cookies/Endgerätezugriffe.
- **Art. 35 Abs. 4 DSGVO** i. V. m. DSK-Positivliste — nationale Pflichttatbestände.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 — Ungültigkeit EU-US-Privacy-Shield; Standardvertragsklauseln erfordern Transfer
 Impact Assessment; maßgeblich für Art. 44 ff. DSGVO.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 — Automatisiertes Scoring als Entscheidung i. S. d. Art. 22 DSGVO, wenn Dritte
 maßgeblich darauf abstellen; zentral für Triage von KI-/Scoring-Vorhaben.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 — Datenschutzrechtliche Haftung Art. 82 DSGVO; Beweislastverteilung.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 *(Recht auf Vergessen I)* — Datenschutz als Teil des allgemeinen Persönlichkeitsrechts
 (Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG); Abwägung mit Kommunikationsfreiheiten.

### Kommentare

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
 — DSFA-Pflicht, Schwellenwerte, Verhältnis zu nationalen Listen.
- `Simitis/Hornung/Spiecker (Hrsg.), DSGVO, 2. Aufl. 2022, Art. 6 Rn. 30 ff.`
 — Rechtsgrundlagen; berechtigtes Interesse als Auffangtatbestand.
- `Gola (Hrsg.), DSGVO, 3. Aufl. 2022, Art. 22 Rn. 5 ff.`
 — Automatisierte Entscheidungsfindung; Abgrenzung zu Profiling.
- `Paal/Pauly (Hrsg.), DS-GVO BDSG, 3. Aufl. 2021, Art. 25 DSGVO Rn. 7 ff.`
 — Privacy by Design und Privacy by Default als Entwurfspflicht.
- `Ehmann/Selmayr (Hrsg.), DS-GVO, 2. Aufl. 2018, Art. 35 Rn. 25 ff.`
 — Anwendungsbereich der DSFA; Verhältnis zu Art. 5, 25 DSGVO.

## Ablauf

### Schritt 1: Verarbeitungsvorgang klären

Bei vager Beschreibung zuerst nachfragen: Datenkategorien (Art. 9?), Betroffenenkreis
(Beschäftigte → § 26 BDSG!), Zweck, Neu oder Zweckänderung, Auftragsverarbeiter,
automatisierte Entscheidung (Art. 22), Endgerätezugriff (§ 24 TDDDG).

### Schritt 2: Hausinternes DSA-Raster

Konfiguriertes Prüfraster aus CLAUDE.md lesen. Trigger erfüllt → mindestens
**DSA ERFORDERLICH**. Nicht erfüllt → weiter mit Schritt 3.

### Schritt 3: DSFA-Pflichtprüfung (Art. 35 DSGVO)

**Pflichttatbestände (Art. 35 Abs. 3, DSK-Positivliste):**
- Systematische automatisierte Bewertung persönlicher Aspekte inkl. Profiling mit
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Umfangreiche Verarbeitung besonderer Datenkategorien (Art. 9 DSGVO).
- Systematische umfangreiche Überwachung öffentlich zugänglicher Bereiche.

**Starke Indikatoren (kein Pflichttatbestand, aber DSFA dringend empfohlen):**
neue Technologie, Kinderdaten, Zusammenführung getrennter Datensätze,
Diskriminierungspotenzial, Cross-Context-Tracking, verhaltensbasierte Werbung.

Pflichttatbestand erfüllt → **DSFA PFLICHT**. Nur Indikatoren → **DSA ERFORDERLICH**.

### Schritt 4: Datenschutzrichtlinien-Abgleich

Vorhaben gegen konfigurierte Richtlinien prüfen. Typische Konflikte:
Datenkategorie nicht in Richtlinie erfasst; Drittlandweitergabe ohne Grundlage
(Art. 44 ff. DSGVO); Löschfristen (Art. 17) überschritten; Zweckbindung (Art. 5
Abs. 1 lit. b) verletzt; Betroffenenrechte unvollständig.

Direkter Konflikt → **STOPP**. Konflikt muss aufgelöst sein vor Fortführung.

### Schritt 5: Klassifikation und Ausgabe

```
Kurzergebnis: [DSFA PFLICHT / DSA ERFORDERLICH / FREIGABE / STOPP — ein Satz]

VORGANG: [wie verstanden]
KLASSIFIKATION: [...]
Hausinternes DSA-Raster ausgelöst? [Ja / Nein]
DSFA-Pflicht (Art. 35 DSGVO)? [Ja — Tatbestand / Nein / N/A]
Richtlinienkonflikt? [Keiner / Ja — konkreter Konflikt]
Begründung: [1–3 Sätze]
```

*Voraussetzungen bei DSA / DSFA:*

| Anforderung | Verantwortlich | Erledigt? |
|---|---|---|
| Datenschutzprüfung / DSFA (Art. 35 DSGVO) | DSB | ☐ |
| Berechtigtes-Interesse-Abwägung (Art. 6 Abs. 1 lit. f) | DSB / Legal | ☐ |
| DSB-Konsultation (DSFA-Pflichtverfahren) | DSB | ☐ |
| AVV (Art. 28 DSGVO) | Legal | ☐ |
| Richtlinienaktualisierung vor Launch | DSB | ☐ |
| Eintrag Verarbeitungsverzeichnis (Art. 30) | DSB | ☐ |

**Rechtsgrundlage (Art. 6 DSGVO):** [lit. a Einwilligung / lit. b Vertrag /
lit. c rechtliche Verpflichtung / lit. f berechtigte Interessen — oder "unklar"]

Nach Klassifikation immer anbieten: "Soll ich jetzt direkt mit der DSFA beginnen?"

*Bei STOPP:*
Konflikt benennen. Optionen: (A) Vorhaben umgestalten, (B) Richtlinie aktualisieren
(Vereinbarkeit mit Rechtsgrundlage prüfen). Keinen Weg vorschlagen, wenn keiner besteht.

### Schritt 6: Weiterleitung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 KI-Folgenabschätzung erwägen.
- **Beschäftigtendatenschutz:** § 26 BDSG und Mitbestimmung (§§ 87 Abs. 1 Nr. 6,
 94 BetrVG) prüfen.

## Beispiel

**Vorgang:** ML-basiertes Kreditscoring für Bestandskunden; Ergebnis fließt in
automatisierte Kreditentscheidung.

**Klassifikation:** DSFA PFLICHT — Art. 35 Abs. 3 lit. a DSGVO: systematische
automatisierte Bewertung persönlicher Aspekte mit erheblichen Auswirkungen
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
(Schufa-Scoring) reicht es, dass Dritte maßgeblich auf das Scoring abstellen.
DSB-Konsultation und Verarbeitungsverzeichnis-Eintrag (Art. 30) zwingend.

## Risiken und typische Fehler

- **"Anonymisiert" = FREIGABE:** Pseudonymisierte Daten bleiben personenbezogen
 (Art. 4 Nr. 1 DSGVO). Re-Identifikationsrisiko konkret prüfen.
- **"Wir machen das ähnlich":** Bestehende, nie geprüfte Verarbeitungen legitimieren
 keine neue. Bei anderem Umfang/Zweck/Kategorie: neu triagen.
- **"Nur ein Pilot":** Pilot mit echten Personendaten unterliegt denselben Anforderungen.
- **"Der Anbieter regelt Datenschutz":** AVV nach Art. 28 zwingend; Triage bleibt beim
 Verantwortlichen (Art. 4 Nr. 7 DSGVO).
- **Inferred Data übersehen:** Score, Risikoklasse, Präferenz = personenbezogenes Datum.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Quellenpflicht

Jede Klassifikation muss nennen: einschlägige DSGVO-/BDSG-Normen mit Artikel/Absatz,
DSK-Listenfundstelle bei DSFA-Pflicht, einschlägige Rechtsprechung in korrekter
Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

Beispiel Rechtsprechung:
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Beispiel Kommentar:
Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Quellen / Updates

Stand: 05/2026. Aktualität prüfen bei Änderungen der DSK-Blacklist/Whitelist (Art. 35 Abs. 4/5 DSGVO), neuen EDSA-Leitlinien zur DSFA sowie KI-VO-Umsetzungsakten.

**Querverweise:**
- `datenschutzrecht/skills/dsfa-erstellung/SKILL.md` — vollständige DSFA bei positiver Triage
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md` — bei Drittlandbezug in der Triage
- `datenschutzrecht/skills/avv-pruefung/SKILL.md` — bei Auftragsverarbeitung als Verarbeitungsbestandteil

## Aktuelle Rechtsprechung (Ergaenzung v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Output-Template — Triage-Ergebnis

**Adressat:** Datenschutzbeauftragter / Prozessverantwortlicher — Tonfall: sachlich-strukturiert

```
Datenschutz-Triage-Ergebnis [DATUM]
Verarbeitungsvorgang: [BEZEICHNUNG]
Beschreibung: [KURZBESCHREIBUNG]

Einstufung: FREIGABE / DSA ERFORDERLICH / DSFA PFLICHT / STOPP

Rechtsgrundlage: Art. [X] DSGVO [§ BDSG optional]
Verantwortlichkeit: Art. 24 (allein) / Art. 26 (gemeinsam) / Art. 28 (Auftragsverarbeitung)
Drittlandbezug: ja (→ Drittlandprüfung) / nein
DSFA-Pflicht: ja (Grund: [...]) / nein (Begründung: [...])

Naechste Schritte:
1. [AKTION]
2. [AKTION]

Frist: [DATUM]
Verantwortlich: [PERSON / ROLLE]
```

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 5 DSGVO (Grundsätze der Verarbeitung)
- Art. 6, 9 DSGVO (Rechtsgrundlagen, besondere Datenkategorien)
- Art. 13, 14 DSGVO (Informationspflichten)
- Art. 15 DSGVO (Auskunftsrecht)
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 32 DSGVO (Sicherheit der Verarbeitung)
- Art. 33, 34 DSGVO (Meldepflichten bei Verletzung)
- Art. 82 DSGVO (Schadensersatz)
- Art. 83 DSGVO (Bußgelder)
- §§ 4, 20, 41 BDSG (Aufsicht, Rechtsweg, Strafvorschriften)

### Leitentscheidungen

- EuGH C-300/21 (immaterieller Schaden Art. 82 DSGVO)
- EuGH C-634/21 (automatisierte Bonitätsbewertung Schufa)
- EuGH C-26/22 (Datenschutzbehörden-Befugnisse)
- EuGH C-807/21 (Bußgeldhaftung juristischer Personen)
- BVerfG 1 BvR 16/13 (Recht auf Vergessen I)

### Anwendung im Skill

- Rechtsgrundlage nach Art. 6 DSGVO sauber waehlen; berechtigte Interessen nach Art. 6 Abs. 1 lit. f DSGVO mit dokumentierter Abwaegung.
- Bei Datenpannen die 72-Stunden-Frist nach Art. 33 DSGVO einhalten; Risikoabwaegung Art. 34 DSGVO separat dokumentieren.
- Auskunftsanspruch Art. 15 DSGVO nicht mit Kopie nach Art. 15 Abs. 3 DSGVO verwechseln; EuGH C-307/22 Reichweite beachten.

---

## Skill: `art-9-besondere-kategorien`

_Bewertet einen Datenschutzvorfall mit besonderen Kategorien personenbezogener Daten nach Art. 9 DSGVO. Behandelt: rassische/ethnische Herkunft; politische Meinungen; religiöse/weltanschauliche Überzeugungen; Gewerkschaftszugehörigkeit; genetische und biometrische Daten zur eindeutigen Identifizie..._

# Besondere Kategorien Art. 9 DSGVO im Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Liegen Daten im Sinne Art. 9 Abs. 1 DSGVO vor — wenn ja welche konkret?
2. Wie viele Betroffene und welche Mengen?
3. Sind die Daten im Klartext oder verschlüsselt oder pseudonymisiert?
4. Welche besondere Aufsicht (Sektorbehörde) ist zuständig?
5. Welche besondere Bußgeldhöhe droht (Art. 83 Abs. 5 DSGVO)?
- Was will der Mandant wirklich erreichen? (Schadensbegrenzung; rechtskonforme Benachrichtigung)

## Rechtsgrundlagen

- **Art. 9 Abs. 1 DSGVO** Verbot mit Erlaubnisvorbehalt; **Art. 9 Abs. 2 DSGVO** Ausnahmen.
- **Art. 34 Abs. 1 DSGVO** Benachrichtigung bei hohem Risiko — bei Art. 9 regelmäßig zu bejahen.
- **Art. 83 Abs. 5 lit. a DSGVO** verschärfter Bußgeldrahmen bis 20 Mio. EUR oder 4 Prozent.
- **Erwägungsgrund 75 DSGVO** besondere Risiken bei sensiblen Daten.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu Gesundheitsdaten-Leaks und Bußgeldhöhen vor Ausgabe verifizieren.

## Zentrale Normen

Art. 9 Abs. 1; Art. 9 Abs. 2; Art. 34 Abs. 1; Art. 83 Abs. 5 lit. a DSGVO; Erwägungsgrund 75.

## Praxisformulierung — Schutzbedarfsanalyse Art. 9

Welche Kategorie liegt vor; in welcher Form (Klartext / pseudonymisiert / verschlüsselt); welche Anzahl; welche Folgen sind plausibel.

Conclusion: bei Art. 9-Daten im Klartext regelmäßig Meldung Art. 33 und Benachrichtigung Art. 34; Begründung schriftlich für die Akte.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-paragraf-203-stgb-berufsgeheimnis` deckt strafrechtliche Geheimnistraeger ab.
- `dsv-sozialdaten-sgb` deckt Sozialdaten ab.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 5 DSGVO (Grundsätze der Verarbeitung)
- Art. 6, 9 DSGVO (Rechtsgrundlagen, besondere Datenkategorien)
- Art. 13, 14 DSGVO (Informationspflichten)
- Art. 15 DSGVO (Auskunftsrecht)
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 32 DSGVO (Sicherheit der Verarbeitung)
- Art. 33, 34 DSGVO (Meldepflichten bei Verletzung)
- Art. 82 DSGVO (Schadensersatz)
- Art. 83 DSGVO (Bußgelder)
- §§ 4, 20, 41 BDSG (Aufsicht, Rechtsweg, Strafvorschriften)

### Leitentscheidungen

- EuGH C-300/21 (immaterieller Schaden Art. 82 DSGVO)
- EuGH C-634/21 (automatisierte Bonitätsbewertung Schufa)
- EuGH C-26/22 (Datenschutzbehörden-Befugnisse)
- EuGH C-807/21 (Bußgeldhaftung juristischer Personen)
- BVerfG 1 BvR 16/13 (Recht auf Vergessen I)

### Anwendung im Skill

- Rechtsgrundlage nach Art. 6 DSGVO sauber waehlen; berechtigte Interessen nach Art. 6 Abs. 1 lit. f DSGVO mit dokumentierter Abwaegung.
- Bei Datenpannen die 72-Stunden-Frist nach Art. 33 DSGVO einhalten; Risikoabwaegung Art. 34 DSGVO separat dokumentieren.
- Auskunftsanspruch Art. 15 DSGVO nicht mit Kopie nach Art. 15 Abs. 3 DSGVO verwechseln; EuGH C-307/22 Reichweite beachten.

---

## Skill: `aufnahme-statusinformation`

_Erstellt nach einem gemeldeten Datenschutzvorfall eine knappe Statusinformation an Mandant und Datenschutzbeauftragten in Fließtextform. Behandelt: Vorgangsbezeichnung; Zeitpunkt der Kenntnisnahme; Eingang Service-Desk und Datenschutzpostfach; Sachverhaltskurzfassung; 72-Stunden-Endpunkt als Datu..._

# Datenschutzvorfall — Erstaufnahme als Statusinformation

## Aktenstart statt Formularstart

Wenn zu **Aufnahme Statusinformation** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Datenschutzrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Triage — kläre vor der Bearbeitung

1. Wann genau wurde der Vorfall durch wen bemerkt und an welche interne Stelle gemeldet?
2. Welche Datenkategorien und welcher Personenkreis sind potenziell betroffen?
3. Ist der 72-Stunden-Lauf nach Art. 33 Abs. 1 DSGVO bereits angestoßen oder läuft er noch?
4. Welche Sofortmaßnahmen wurden bereits getroffen und welche stehen aus?
5. Wer ist Empfänger der Statusinformation — Geschäftsleitung, Datenschutzbeauftragter, Vorstand, externer Berater?
- Was will der Mandant wirklich erreichen? (Lagebild, Entscheidungsgrundlage Meldung, Eskalation, Dokumentation)

## Rechtsgrundlagen

- **Art. 33 Abs. 1 DSGVO** Meldepflicht binnen 72 Stunden ab Kenntniserlangung an die zuständige Aufsichtsbehörde.
- **Art. 33 Abs. 5 DSGVO** Dokumentationspflicht jedes Vorfalls unabhängig von der Meldepflicht.
- **Art. 34 DSGVO** Benachrichtigung der betroffenen Personen bei voraussichtlich hohem Risiko.
- **§ 42 BDSG** Strafvorschriften bei vorsätzlicher unbefugter Offenlegung.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht des Verantwortlichen.

## Aktuelle Rechtsprechung

Rechtsprechung wird nicht aus Modellwissen zitiert; aktuelle Entscheidungen des EuGH und BGH zur Auslegung der 72-Stunden-Frist und zum Kenntnisbegriff sind vor Ausgabe über die unten genannten Quellen zu verifizieren.

## Zentrale Normen

Art. 4 Nr. 12; Art. 33 Abs. 1; Art. 33 Abs. 3; Art. 33 Abs. 5; Art. 34 Abs. 1 DSGVO; § 42 BDSG.

## Praxisformulierung — Statusinformation (Stilreferenz Fließtext)

Vorgang: kurze sprechende Bezeichnung des Vorfalls.

Kenntnisnahme: Wer hat wann was durch welche Wahrnehmung erkannt — Reasoning vor Conclusion.

Eingang Service-Desk: Zeitpunkt und Ticketnummer mit kurzer Begründung der Zuordnung.

Eingang Datenschutzpostfach: Zeitpunkt der formalen Weiterleitung an die Datenschutzorganisation.

Sachverhalt: drei bis fünf Sätze; was ist passiert; welche Systeme; welche Datenkategorien; welcher Personenkreis.

72-Stunden-Endpunkt: konkretes Datum und Uhrzeit mit Bezug auf den Kenntnisnahmezeitpunkt.

Ampelstatus: 🟢 unkritisch / 🟡 beobachtet / 🔴 meldepflichtig / ⚫ benachrichtigungspflichtig — mit kurzer Erläuterung.

Aktuelle Einschätzung: technische und organisatorische Lage; eingrenzbar oder nicht.

Bewertung: Wahrscheinlichkeit eines Risikos für die Rechte und Freiheiten; Reasoning vor Conclusion.

Meldepflicht Art. 33: ja / nein / noch offen mit Begründung.

Informationspflicht Art. 34: ja / nein / noch offen mit Begründung.

Nächster Schritt: konkret, mit Verantwortlichem und Zeitpunkt.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 5 DSGVO (Grundsätze der Verarbeitung)
- Art. 6, 9 DSGVO (Rechtsgrundlagen, besondere Datenkategorien)
- Art. 13, 14 DSGVO (Informationspflichten)
- Art. 15 DSGVO (Auskunftsrecht)
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 32 DSGVO (Sicherheit der Verarbeitung)
- Art. 33, 34 DSGVO (Meldepflichten bei Verletzung)
- Art. 82 DSGVO (Schadensersatz)
- Art. 83 DSGVO (Bußgelder)
- §§ 4, 20, 41 BDSG (Aufsicht, Rechtsweg, Strafvorschriften)

### Leitentscheidungen

- EuGH C-300/21 (immaterieller Schaden Art. 82 DSGVO)
- EuGH C-634/21 (automatisierte Bonitätsbewertung Schufa)
- EuGH C-26/22 (Datenschutzbehörden-Befugnisse)
- EuGH C-807/21 (Bußgeldhaftung juristischer Personen)
- BVerfG 1 BvR 16/13 (Recht auf Vergessen I)

### Anwendung im Skill

- Rechtsgrundlage nach Art. 6 DSGVO sauber waehlen; berechtigte Interessen nach Art. 6 Abs. 1 lit. f DSGVO mit dokumentierter Abwaegung.
- Bei Datenpannen die 72-Stunden-Frist nach Art. 33 DSGVO einhalten; Risikoabwaegung Art. 34 DSGVO separat dokumentieren.
- Auskunftsanspruch Art. 15 DSGVO nicht mit Kopie nach Art. 15 Abs. 3 DSGVO verwechseln; EuGH C-307/22 Reichweite beachten.

---

## Skill: `avv-art-28-dsgvo-grundtatbestand`

_Grundtatbestand der Auftragsverarbeitung nach Art. 28 DSGVO. Klaert Rollenzuordnung Verantwortlicher gegen Auftragsverarbeiter wenn ein Dienstleister personenbezogene Daten im fremden Auftrag verarbeitet. Wann gilt Art. 28 wann Art. 26 wann Funktionsuebertragung. Output: Pruefvermerk zur Rollenzu..._

# Auftragsverarbeitung Art. 28 DSGVO – Grundtatbestand

## Zweck / Purpose

Strukturierte Pruefung, ob ein Vertragsverhaeltnis dem Grundtatbestand der Auftragsverarbeitung nach Art. 28 DSGVO unterfaellt und damit ein Auftragsverarbeitungsvertrag (AVV / Data Processing Agreement, DPA) abzuschliessen ist. Purpose (EN): Determine whether a contractual relationship triggers Art. 28 GDPR data processing on behalf of a controller and therefore requires a DPA.

## Wann dieses Modul hilft

- Mandant bezieht einen IT-/Cloud-/SaaS-Dienst und ist unsicher, ob AVV erforderlich ist.
- Mandant ist Anbieter und prueft, ob er als Auftragsverarbeiter einzustufen ist.
- Es bestehen Zweifel, ob nicht stattdessen Art. 26 DSGVO (gemeinsame Verantwortlichkeit) oder eine eigenstaendige Verantwortlichkeit (Funktionsuebertragung, separate Verantwortliche) vorliegt.
- Eine Aufsichtsbehoerde fragt nach Rollenzuordnung im Verarbeitungsverzeichnis (Art. 30 DSGVO).

## Rechtlicher Rahmen

- Art. 4 Nr. 7 DSGVO: Verantwortlicher entscheidet ueber Zwecke und Mittel.
- Art. 4 Nr. 8 DSGVO: Auftragsverarbeiter verarbeitet im Auftrag des Verantwortlichen.
- Art. 28 Abs. 1 DSGVO: Auswahl nur solcher Auftragsverarbeiter, die hinreichende Garantien bieten.
- Art. 28 Abs. 3 DSGVO: AVV in Schriftform oder elektronisch; Mindestinhalte lit. a bis h.
- Art. 28 Abs. 10 DSGVO: Eigenstaendige Verantwortlichkeit des Auftragsverarbeiters bei Ueberschreiten der Weisungen.
- Art. 29 DSGVO: Weisungsgebundenheit der Verarbeitung.
- § 62 BDSG: Spezialnormen für öffentliche Stellen.
- EDSA-Leitlinien 07/2020 zur Abgrenzung Verantwortlicher / Auftragsverarbeiter (angenommen 07.07.2021).

## Ablauf / Checkliste

1. **Sachverhalt erfassen.**
 - Welche personenbezogenen Daten werden verarbeitet?
 - Welcher Akteur entscheidet ueber Zweck (Wozu?) und Mittel (Wie?)?
 - Gibt es Weisungsmoeglichkeiten und Weisungsrechte?
 - Welchen wirtschaftlichen Vorteil zieht jeder Akteur aus der Verarbeitung?

2. **Drei-Stufen-Test für Rollenzuordnung.**

 | Frage | Indiz für Auftragsverarbeitung | Indiz gegen Auftragsverarbeitung |
 |---|---|---|
 | Wer legt Zweck fest? | Verantwortlicher allein | Dienstleister mitbestimmend |
 | Wer legt wesentliche Mittel fest? | Verantwortlicher | Dienstleister bestimmt Architektur und Datenlogik |
 | Eigene Datennutzung des Dienstleisters? | Nein, nur weisungsgebunden | Ja, für eigene Zwecke (Werbung, KI-Training, Statistik) |
 | Wirtschaftliches Interesse | Verantwortlicher | Dienstleister hat eigenes Interesse an Daten |
 | Berufsbild | Reiner Auftragnehmer | Eigene Rechtsdienstleistung, Berufstraegerstellung |

3. **Negativabgrenzung.**
 - **Funktionsuebertragung:** Bei Berufsgeheimnistraegern (Steuerberater, Rechtsanwaelte, Aerzte), Inkassodienstleistern und Wirtschaftspruefern ist die Rollenzuordnung wegen § 203 StGB und § 43a Abs. 2 BRAO besonders kritisch (Querverweis: funktionsuebertragung-vs-auftragsverarbeitung).
 - **Gemeinsame Verantwortlichkeit (Art. 26 DSGVO):** Wenn beide Akteure gemeinsam ueber Zwecke und Mittel entscheiden – EuGH C-210/16 Wirtschaftsakademie, EuGH C-40/17 Fashion ID, EuGH C-25/17 Zeugen Jehovas.
 - **Getrennte Verantwortlichkeit:** Wenn jeder Akteur dieselben Daten für eigene Zwecke mit eigener Rechtsgrundlage verarbeitet.

4. **Rechtsfolge feststellen.**
 - Auftragsverarbeitung bejaht: AVV-Pflicht nach Art. 28 Abs. 3 DSGVO.
 - Keine Verarbeitung im Auftrag, sondern Art. 26 DSGVO: Joint-Controller-Vereinbarung (Querverweis: avv-art-26-joint-controllership-deutsch).
 - Funktionsuebertragung: Eigener Vertragstyp, ggf. Datenuebermittlungsklausel und Geheimhaltungsvereinbarung statt AVV.

5. **Dokumentation.**
 - Im Verarbeitungsverzeichnis Art. 30 DSGVO: Rolle eintragen.
 - AVV als Anlage zum Hauptvertrag oder eigenstaendig.

## Mustertext / Template

Praeambel-Klausel für einen AVV nach Art. 28 DSGVO:

> "Der Auftraggeber (im Folgenden 'Verantwortlicher' im Sinne des Art. 4 Nr. 7 DSGVO) beauftragt den Auftragnehmer (im Folgenden 'Auftragsverarbeiter' im Sinne des Art. 4 Nr. 8 DSGVO) mit der Verarbeitung personenbezogener Daten im Auftrag und nach Weisung des Verantwortlichen. Gegenstand, Dauer, Art und Zweck der Verarbeitung, die Art der personenbezogenen Daten sowie die Kategorien betroffener Personen sind in Anlage 1 abschliessend beschrieben. Der Auftragsverarbeiter verarbeitet die personenbezogenen Daten ausschliesslich auf dokumentierte Weisung des Verantwortlichen, soweit nicht eine Verarbeitungspflicht nach Unionsrecht oder dem Recht der Mitgliedstaaten besteht; in diesem Fall teilt der Auftragsverarbeiter dem Verantwortlichen diese rechtliche Verpflichtung vor der Verarbeitung mit, sofern das betreffende Recht eine solche Mitteilung nicht wegen eines wichtigen öffentlichen Interesses verbietet."

## Typische Drafting-Fehler

- AVV abgeschlossen, obwohl tatsaechlich Art. 26 DSGVO (gemeinsame Verantwortlichkeit) gegeben ist – falsche Rollenzuordnung wird durch AVV nicht geheilt.
- Pauschalverweis auf "Datenschutz" statt konkreter Mindestinhalte nach Art. 28 Abs. 3 lit. a bis h DSGVO.
- AVV mit Berufstraegern ohne Beruecksichtigung von § 203 StGB.
- Vermischung mit allgemeinen Geheimhaltungsklauseln; AVV-Pflichten sind eigenstaendig.
- AVV erst nach Verarbeitungsbeginn abgeschlossen (Art. 28 Abs. 9 DSGVO Form).

## Quellen Stand 06/2026

- DSGVO Art. 4 Nr. 7, Nr. 8, Art. 28, Art. 29.
- BDSG § 62.
- EDSA-Leitlinien 07/2020 zur Abgrenzung Verantwortlicher / Auftragsverarbeiter (Final 07.07.2021); abrufbar ueber edpb.europa.eu.
- EuGH C-25/17 (Zeugen Jehovas) – verifiziertes Aktenzeichen; Volltext ueber curia.europa.eu pruefen.
- EuGH C-210/16 (Wirtschaftsakademie / Fanpages) – Aktenzeichen verifiziert.
- EuGH C-40/17 (Fashion ID) – Aktenzeichen verifiziert.
- Verbindlich zur Zitierweise: `../../../references/zitierweise.md`.
- Kommentar-, Handbuch- und Aufsatzfundstellen nur, wenn der Mandant die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 5 DSGVO (Grundsätze der Verarbeitung)
- Art. 6, 9 DSGVO (Rechtsgrundlagen, besondere Datenkategorien)
- Art. 13, 14 DSGVO (Informationspflichten)
- Art. 15 DSGVO (Auskunftsrecht)
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 32 DSGVO (Sicherheit der Verarbeitung)
- Art. 33, 34 DSGVO (Meldepflichten bei Verletzung)
- Art. 82 DSGVO (Schadensersatz)
- Art. 83 DSGVO (Bußgelder)
- §§ 4, 20, 41 BDSG (Aufsicht, Rechtsweg, Strafvorschriften)

### Leitentscheidungen

- EuGH C-300/21 (immaterieller Schaden Art. 82 DSGVO)
- EuGH C-634/21 (automatisierte Bonitätsbewertung Schufa)
- EuGH C-26/22 (Datenschutzbehörden-Befugnisse)
- EuGH C-807/21 (Bußgeldhaftung juristischer Personen)
- BVerfG 1 BvR 16/13 (Recht auf Vergessen I)

### Anwendung im Skill

- Rechtsgrundlage nach Art. 6 DSGVO sauber waehlen; berechtigte Interessen nach Art. 6 Abs. 1 lit. f DSGVO mit dokumentierter Abwaegung.
- Bei Datenpannen die 72-Stunden-Frist nach Art. 33 DSGVO einhalten; Risikoabwaegung Art. 34 DSGVO separat dokumentieren.
- Auskunftsanspruch Art. 15 DSGVO nicht mit Kopie nach Art. 15 Abs. 3 DSGVO verwechseln; EuGH C-307/22 Reichweite beachten.

---

## Skill: `avv-art-28-mindestinhalte-checkliste`

_Vollstaendige Pflichtinhalte-Checkliste für einen AVV nach Art. 28 Abs. 3 lit. a bis h DSGVO. Jede der acht Pflichtklauseln mit Sollformulierung Fallback-Position und Auditfrage. Geeignet für das Drafting eines neuen AVV oder das Auditing eines bestehenden AVV. Output: Klausel-für-Klausel-Pruefra..._

# AVV-Mindestinhalte nach Art. 28 Abs. 3 DSGVO – Klauselcheckliste

## Zweck / Purpose

Pflichtinhalte-Checkliste für Auftragsverarbeitungsvertraege nach Art. 28 Abs. 3 DSGVO – Klausel für Klausel mit Soll-Position, Fallback und Pruefkriterium. Purpose (EN): Mandatory-content checklist for DPAs under Art. 28 (3) GDPR, clause by clause.

## Wann dieses Modul hilft

- Beim Drafting eines neuen AVV ist sicherzustellen, dass alle acht Pflichtinhalte vollstaendig sind.
- Beim Auditing eines vorgelegten AVV ist zu pruefen, ob jede Pflichtklausel ihren Mindestanforderungen genuegt.
- Bei Aufsichtsbehoerden-Pruefungen ist der vollstaendige Pflichtkatalog nachweisbar zu dokumentieren.

## Rechtlicher Rahmen

- Art. 28 Abs. 3 Satz 1 DSGVO: Vertrag oder anderes Rechtsinstrument in Schriftform, einschliesslich elektronisch.
- Art. 28 Abs. 3 Satz 2 DSGVO: Gegenstand und Dauer, Art und Zweck der Verarbeitung, Datenkategorien und Kategorien Betroffener, Pflichten und Rechte des Verantwortlichen.
- Art. 28 Abs. 3 Satz 2 lit. a bis h DSGVO: Acht Pflichtklauseln.

## Ablauf / Checkliste

### Rahmenangaben (Art. 28 Abs. 3 Satz 2 DSGVO)

| Pflichtangabe | Pruefkriterium |
|---|---|
| Gegenstand der Verarbeitung | Konkret benannt, nicht "Datenschutz allgemein" |
| Dauer | Vertragslaufzeit, ggf. Verlaengerung |
| Art und Zweck | Operative Funktion und Geschaeftszweck |
| Art der personenbezogenen Daten | Datenarten katalogisiert (Stammdaten, Verkehrsdaten, Inhaltsdaten, besondere Kategorien Art. 9 DSGVO) |
| Kategorien Betroffener | Mitarbeitende, Mandanten, Kinder, Patienten etc. |
| Pflichten und Rechte des Verantwortlichen | Mindestens Weisungsrechte, Kontrollrechte, Beendigungsrechte |

### Die acht Pflichtklauseln (Art. 28 Abs. 3 Satz 2 lit. a bis h DSGVO)

**lit. a – Weisungsgebundenheit.** Verarbeitung nur auf dokumentierte Weisung des Verantwortlichen, einschliesslich Drittlandtransfer. Auditfrage: Wer fuehrt das Weisungsregister?

**lit. b – Vertraulichkeit.** Personen, die zur Verarbeitung befugt sind, haben sich zur Vertraulichkeit verpflichtet oder unterliegen einer angemessenen gesetzlichen Verschwiegenheitspflicht. Auditfrage: Liegen Vertraulichkeitserklaerungen vor?

**lit. c – Technische und organisatorische Massnahmen (TOM, Art. 32 DSGVO).** Auftragsverarbeiter trifft alle erforderlichen Massnahmen nach Art. 32 DSGVO. Auditfrage: TOM-Anlage aktuell und konkret? (Querverweis: avv-tom-art-32-dsgvo-anlage)

**lit. d – Sub-Auftragsverarbeiter (Art. 28 Abs. 2 und Abs. 4 DSGVO).** Einsatz nur mit allgemeiner oder besonderer schriftlicher Genehmigung; bei allgemeiner Genehmigung Informationspflicht ueber geplanten Wechsel. Auditfrage: Aktuelle Liste vorhanden? Widerspruchsfrist angemessen?

**lit. e – Unterstuetzung Betroffenenrechte (Art. 12 bis 23 DSGVO).** Geeignete technische und organisatorische Massnahmen, um Erfuellung der Betroffenenrechte zu unterstuetzen (Auskunft, Loeschung, Berichtigung, Datenuebertragbarkeit). Auditfrage: SLA für Betroffenenanfragen?

**lit. f – Unterstuetzung Art. 32 bis 36 DSGVO.** Unterstuetzung bei TOM, Meldepflicht (Art. 33 DSGVO), Benachrichtigung Betroffener (Art. 34 DSGVO), DSFA (Art. 35 DSGVO), Konsultation Aufsichtsbehoerde (Art. 36 DSGVO). Auditfrage: Meldewege definiert?

**lit. g – Loeschung oder Rueckgabe.** Nach Wahl des Verantwortlichen alle personenbezogenen Daten loeschen oder zurueckgeben nach Ende des Auftrags, ausser gesetzliche Aufbewahrungspflichten. Auditfrage: Format der Rueckgabe definiert? (Querverweis: avv-loeschung-rueckgabe-nach-vertragsende)

**lit. h – Audit und Nachweis.** Alle erforderlichen Informationen zum Nachweis bereitstellen; Ueberpruefungen einschliesslich Inspektionen durch Verantwortlichen oder Pruefer ermoeglichen. Auditfrage: Frequenz, Form, Kosten geregelt? (Querverweis: avv-audit-und-kontrollrechte)

## Mustertext / Template

Konsolidierte Pflichtklausel-Liste (Kurzform für Vertragsanlage):

```
§ X Pflichten des Auftragsverarbeiters
(1) Weisungsgebundenheit (Art. 28 Abs. 3 lit. a DSGVO).
(2) Vertraulichkeit (Art. 28 Abs. 3 lit. b DSGVO).
(3) Technische und organisatorische Massnahmen gemaess Anlage TOM (Art. 28 Abs. 3 lit. c i.V.m. Art. 32 DSGVO).
(4) Sub-Auftragsverarbeiter nach Massgabe von § Y (Art. 28 Abs. 3 lit. d i.V.m. Abs. 2 und Abs. 4 DSGVO).
(5) Unterstuetzung bei Betroffenenrechten (Art. 28 Abs. 3 lit. e DSGVO).
(6) Unterstuetzung bei Sicherheit, Meldepflicht, Benachrichtigung, DSFA, Vorabkonsultation (Art. 28 Abs. 3 lit. f DSGVO).
(7) Rueckgabe oder Loeschung nach Vertragsende gemaess Anlage Loeschkonzept (Art. 28 Abs. 3 lit. g DSGVO).
(8) Audit- und Kontrollrechte gemaess § Z (Art. 28 Abs. 3 lit. h DSGVO).
```

## Typische Drafting-Fehler

- Rahmenangaben fehlen oder sind zu allgemein ("Daten unserer Kunden").
- lit. a wird auf "Vertragserfuellung" reduziert ohne Weisungsregister.
- lit. b wird mit allgemeiner Geheimhaltungsklausel verwechselt; spezifische Vertraulichkeit für Verarbeitungsbefugte fehlt.
- TOM-Anlage (lit. c) ist Marketingbroschuere statt konkrete Massnahmen.
- lit. d laesst Sub-AV-Wechsel ohne Widerspruchsfrist zu.
- lit. e ohne SLA und ohne Kostenregelung.
- lit. g ohne klare Wahlmoeglichkeit (Loeschung oder Rueckgabe) und ohne Format.
- lit. h verweist auf Zertifikate, ohne eigenes Audit-Recht zuzulassen.

## Quellen Stand 06/2026

- Art. 28 Abs. 3 DSGVO – Pflichtinhalte des Vertrags.
- Art. 28 Abs. 2, Abs. 4 DSGVO – Sub-Auftragsverarbeiter.
- Art. 28 Abs. 9 DSGVO – Schriftform inklusive elektronisch.
- Art. 29 DSGVO – Weisungsgebundenheit.
- EDSA-Leitlinien 07/2020 – Final 07.07.2021; abrufbar ueber edpb.europa.eu.
- Zitierweise: `../../../references/zitierweise.md`.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 5 DSGVO (Grundsätze der Verarbeitung)
- Art. 6, 9 DSGVO (Rechtsgrundlagen, besondere Datenkategorien)
- Art. 13, 14 DSGVO (Informationspflichten)
- Art. 15 DSGVO (Auskunftsrecht)
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 32 DSGVO (Sicherheit der Verarbeitung)
- Art. 33, 34 DSGVO (Meldepflichten bei Verletzung)
- Art. 82 DSGVO (Schadensersatz)
- Art. 83 DSGVO (Bußgelder)
- §§ 4, 20, 41 BDSG (Aufsicht, Rechtsweg, Strafvorschriften)

### Leitentscheidungen

- EuGH C-300/21 (immaterieller Schaden Art. 82 DSGVO)
- EuGH C-634/21 (automatisierte Bonitätsbewertung Schufa)
- EuGH C-26/22 (Datenschutzbehörden-Befugnisse)
- EuGH C-807/21 (Bußgeldhaftung juristischer Personen)
- BVerfG 1 BvR 16/13 (Recht auf Vergessen I)

### Anwendung im Skill

- Rechtsgrundlage nach Art. 6 DSGVO sauber waehlen; berechtigte Interessen nach Art. 6 Abs. 1 lit. f DSGVO mit dokumentierter Abwaegung.
- Bei Datenpannen die 72-Stunden-Frist nach Art. 33 DSGVO einhalten; Risikoabwaegung Art. 34 DSGVO separat dokumentieren.
- Auskunftsanspruch Art. 15 DSGVO nicht mit Kopie nach Art. 15 Abs. 3 DSGVO verwechseln; EuGH C-307/22 Reichweite beachten.

---

## Skill: `avv-eu-kommission-musterklauseln-2021-915`

_EU-Kommissions-Standardvertragsklauseln zwischen Verantwortlichem und Auftragsverarbeiter nach Beschluss (EU) 2021/915 vom 04.06.2021. Diese Klauseln sind nicht zu verwechseln mit den Drittlands-SCC nach Beschluss (EU) 2021/914. Anwendungsbereich Aufbau und Verwendung als Mustervertragsanlage. Ou..._

# EU-Kommissions-Standardvertragsklauseln Controller-Processor (Beschluss (EU) 2021/915)

## Zweck / Purpose

Anwendung und Aufbau der EU-Kommissions-Standardvertragsklauseln zwischen Verantwortlichem und Auftragsverarbeiter nach Beschluss (EU) 2021/915 vom 04.06.2021. Diese Klauseln decken den AVV nach Art. 28 DSGVO ab und sind nicht zu verwechseln mit den Drittland-SCC nach Beschluss (EU) 2021/914. Purpose (EN): EU Commission standard contractual clauses between controller and processor under Decision (EU) 2021/915 of 04 June 2021.

## Wann dieses Modul hilft

- Mandant moechte einen vorgefertigten, von der EU-Kommission gebilligten AVV-Vertragssatz verwenden.
- Aufsichtsbehoerde fragt, warum der eigene AVV nicht den EU-Musterklauseln folgt.
- Es ist abzugrenzen, dass die "SCC" hier nicht die Drittland-SCC nach Beschluss (EU) 2021/914 sind.

## Rechtlicher Rahmen

- Beschluss (EU) 2021/915 der Kommission vom 04.06.2021 ueber Standardvertragsklauseln zwischen Verantwortlichen und Auftragsverarbeitern gemaess Art. 28 Abs. 7 DSGVO und Art. 29 Abs. 7 EU-Verordnung 2018/1725.
- Veroeffentlichung im Amtsblatt der EU L 199/18 vom 07.06.2021.
- Art. 28 Abs. 6 DSGVO: Verantwortlicher und Auftragsverarbeiter koennen die SCC nach Abs. 7 oder Abs. 8 verwenden – Vorteil: Klauseln gelten "as is", keine Einzelpruefung gegen Art. 28 Abs. 3 noetig, soweit unveraendert.
- Art. 28 Abs. 7 DSGVO: Kommission erlaesst die SCC; Art. 28 Abs. 8 DSGVO: Aufsichtsbehoerden koennen eigene SCC erlassen.

## Ablauf / Checkliste

1. **Abgrenzung pruefen.**
 - Beschluss (EU) 2021/915 = AVV Verantwortlicher zu Auftragsverarbeiter im EWR-Binnenkontext.
 - Beschluss (EU) 2021/914 = Drittlandtransfer-SCC (vier Module: C2C, C2P, P2P, P2C); in Kraft seit 27.06.2021.
 - Beide koennen nebeneinander verwendet werden, wenn Auftragsverarbeiter im Drittland sitzt.

2. **Struktur des Beschluss (EU) 2021/915.**
 - Klausel 1 Zweck und Anwendungsbereich.
 - Klausel 2 Unveraenderlichkeit (Klauseln nicht abaendern, aber ergaenzen).
 - Klausel 3 Auslegung.
 - Klausel 4 Hierarchie (Vorrang vor anderen vertraglichen Bestimmungen).
 - Klausel 5 Verarbeitungstaetigkeiten (Anhang I).
 - Klausel 6 Beschreibung der Verarbeitung (Anhang I).
 - Klausel 7 Pflichten der Parteien (Art. 28 Abs. 3 lit. a bis h DSGVO).
 - Klausel 8 Sub-Auftragsverarbeiter (Anhang IV).
 - Klausel 9 Internationale Datenuebermittlung (Verweis auf SCC Beschluss (EU) 2021/914).
 - Klausel 10 Unterstuetzung des Verantwortlichen.
 - Klausel 11 Beendigung.
 - Anhang II TOM, Anhang III Liste Sub-AV, Anhang IV Liste der Verarbeitungstaetigkeiten.

3. **Auswahl und Ausfuellung.**
 - Klauseln 1 bis 11 unveraendert uebernehmen.
 - Anhaenge konkret befuellen: keine Pauschalformulierungen.
 - Bei Konzern-/Multi-Party-Konstellationen ggf. Beitrittsmechanik (Docking Clause analog Beschluss 2021/914).

4. **Begrenzung.**
 - Die Klauseln decken Art. 28 DSGVO ab, nicht Art. 26 (Joint Control) und nicht Art. 13/14 (Informationspflichten).
 - Sie ersetzen keine Drittland-SCC; wenn Daten aus dem EWR herausfliessen, muessen zusaetzlich die SCC nach Beschluss (EU) 2021/914 abgeschlossen werden.

## Mustertext / Template

Bezugnahme-Klausel zur Inkorporation des Beschluss (EU) 2021/915 in den Hauptvertrag:

> "Soweit der Auftragnehmer für den Auftraggeber personenbezogene Daten im Sinne des Art. 4 Nr. 1 DSGVO als Auftragsverarbeiter im Sinne des Art. 4 Nr. 8 DSGVO verarbeitet, gelten erganzend zum Hauptvertrag die Standardvertragsklauseln der EU-Kommission gemaess Durchfuehrungsbeschluss (EU) 2021/915 vom 04.06.2021 in der jeweils geltenden Fassung. Die Klauseln 1 bis 11 des Beschluss (EU) 2021/915 werden ohne Aenderung uebernommen; die Anhaenge I bis IV sind als Anlagen 1 bis 4 zu dieser Vereinbarung beigefuegt und integraler Bestandteil der Vereinbarung. Im Fall eines Widerspruchs zwischen einer Bestimmung des Hauptvertrags und einer Klausel des Beschluss (EU) 2021/915 gehen die Klauseln des Beschluss (EU) 2021/915 vor."

## Typische Drafting-Fehler

- Verwechslung mit Beschluss (EU) 2021/914 (Drittland-SCC).
- Klauseln werden im Text geaendert (Klausel 2 verbietet das ausdruecklich).
- Anhaenge bleiben leer oder enthalten Verweise statt konkreter Inhalte.
- Inkorporation nur "soweit anwendbar" – das schwaecht die Bindungswirkung.
- Es wird vergessen, dass die SCC nach Beschluss (EU) 2021/915 nicht im Verhaeltnis Verantwortlicher / Verantwortlicher gelten (dafür waeren die C2C-Module aus Beschluss 2021/914 zu verwenden, allerdings nur bei Drittlandbezug).

## Quellen Stand 06/2026

- Durchfuehrungsbeschluss (EU) 2021/915 der Kommission vom 04.06.2021, ABl. L 199/18 vom 07.06.2021 – verifiziert.
- Durchfuehrungsbeschluss (EU) 2021/914 der Kommission vom 04.06.2021, ABl. L 199/31 vom 07.06.2021 – in Kraft seit 27.06.2021 – verifiziert.
- Art. 28 Abs. 6 bis 8 DSGVO.
- Zitierweise: `../../../references/zitierweise.md`.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 5 DSGVO (Grundsätze der Verarbeitung)
- Art. 6, 9 DSGVO (Rechtsgrundlagen, besondere Datenkategorien)
- Art. 13, 14 DSGVO (Informationspflichten)
- Art. 15 DSGVO (Auskunftsrecht)
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 32 DSGVO (Sicherheit der Verarbeitung)
- Art. 33, 34 DSGVO (Meldepflichten bei Verletzung)
- Art. 82 DSGVO (Schadensersatz)
- Art. 83 DSGVO (Bußgelder)
- §§ 4, 20, 41 BDSG (Aufsicht, Rechtsweg, Strafvorschriften)

### Leitentscheidungen

- EuGH C-300/21 (immaterieller Schaden Art. 82 DSGVO)
- EuGH C-634/21 (automatisierte Bonitätsbewertung Schufa)
- EuGH C-26/22 (Datenschutzbehörden-Befugnisse)
- EuGH C-807/21 (Bußgeldhaftung juristischer Personen)
- BVerfG 1 BvR 16/13 (Recht auf Vergessen I)

### Anwendung im Skill

- Rechtsgrundlage nach Art. 6 DSGVO sauber waehlen; berechtigte Interessen nach Art. 6 Abs. 1 lit. f DSGVO mit dokumentierter Abwaegung.
- Bei Datenpannen die 72-Stunden-Frist nach Art. 33 DSGVO einhalten; Risikoabwaegung Art. 34 DSGVO separat dokumentieren.
- Auskunftsanspruch Art. 15 DSGVO nicht mit Kopie nach Art. 15 Abs. 3 DSGVO verwechseln; EuGH C-307/22 Reichweite beachten.

---

## Skill: `avv-eu-us-data-privacy-framework-bezug`

_Behandlung des EU-US Data Privacy Framework (DPF) im AVV. Angemessenheitsbeschluss EU-Kommission vom 10.07.2023 Beschluss (EU) 2023/1795. Anforderungen an Selbstzertifizierung Pruefung der Listung Fallback ueber SCC 2021/914 und Transfer Impact Assessment. Output: AVV-Klauselbausteine für DPF und..._

# EU-US Data Privacy Framework (DPF) im AVV

## Zweck / Purpose

Behandlung des EU-US Data Privacy Frameworks im AVV inklusive Selbstzertifizierungspruefung und SCC-Fallback. Purpose (EN): Treatment of the EU-US Data Privacy Framework in DPAs, including self-certification check and SCC fallback.

## Wann dieses Modul hilft

- US-Anbieter wird als Auftragsverarbeiter beauftragt oder eingebunden.
- Pruefung, ob Anbieter unter dem EU-US Data Privacy Framework selbstzertifiziert ist.
- Vertragsklausel für DPF-Nutzung und SCC-Fallback ist erforderlich.
- Aufsichtsbehoerde fragt nach Drittlandtransfer-Absicherung.

## Rechtlicher Rahmen

- Durchfuehrungsbeschluss (EU) 2023/1795 der Kommission vom 10.07.2023 ueber die Angemessenheit des Schutzniveaus personenbezogener Daten nach dem EU-US Data Privacy Framework – verifiziert.
- Art. 45 DSGVO – Angemessenheitsbeschluss.
- Art. 46 DSGVO – Geeignete Garantien (SCC, BCR) als Fallback.
- Art. 49 DSGVO – Ausnahmen für bestimmte Faelle.
- Executive Order 14086 vom 07.10.2022 – US-Schutzgarantien (signal intelligence safeguards, DPRC).
- EuGH C-311/18 (Schrems II) – verifiziert: Vorgaengerregelung Privacy Shield für unwirksam erklaert.

## Ablauf / Checkliste

1. **Selbstzertifizierung pruefen.**
 - Liste pruefen ueber dataprivacyframework.gov.
 - Status: aktiv ("Active") versus inaktiv ("Inactive Participant").
 - Geltungsbereich der Selbstzertifizierung: HR-Daten und/oder Non-HR-Daten?
 - Im Listing für den konkreten Datentypus zertifiziert?

2. **Vertragsabsicherung.**
 - DPF-Selbstzertifizierung des Anbieters wird im AVV ausdruecklich referenziert.
 - SCC nach Beschluss (EU) 2021/914 als Fallback für den Fall, dass der Anbieter die Selbstzertifizierung verliert oder das DPF unwirksam wird.
 - Transfer Impact Assessment auch bei DPF-Nutzung empfohlen, weil DPF politisch und rechtlich angreifbar bleibt (Schrems-Linie).

3. **Sub-AV-Kette pruefen.**
 - Sub-AV des US-Anbieters mit weiterem US-Standort oder Drittland?
 - Eigene DPF-Selbstzertifizierung jedes US-Sub-AV erforderlich.
 - Fuer Nicht-US-Drittland-Sub-AV: SCC oder anderer Transfermechanismus.

4. **Monitoring.**
 - DPF-Listing periodisch (mindestens jaehrlich) ueberpruefen.
 - Pruefung vor jedem Vertragsschluss und vor wesentlicher Vertragsverlaengerung.

5. **Eskalation.**
 - Bei Suspendierung der DPF-Listung: sofortige Aktivierung des SCC-Fallback.
 - Bei Unwirksamkeitserklaerung des DPF durch EuGH (analog Schrems II): umfassende Transferpruefung neu.

## Mustertext / Template

DPF-und-Fallback-Klausel:

> "§ X Drittlandtransfer in die Vereinigten Staaten
>
> (1) Soweit der Auftragsverarbeiter personenbezogene Daten in die Vereinigten Staaten uebermittelt oder dort verarbeitet, erfolgt die Uebermittlung primaer auf Grundlage des Durchfuehrungsbeschlusses (EU) 2023/1795 der Kommission vom 10.07.2023 (EU-US Data Privacy Framework). Der Auftragsverarbeiter sichert zu, dass er gemaess dem Data Privacy Framework wirksam selbstzertifiziert ist und die zertifizierten Datenkategorien die unter diesem Vertrag uebermittelten Daten umfassen.
>
> (2) Der Auftragsverarbeiter teilt dem Verantwortlichen jede Aenderung oder Suspendierung seiner DPF-Selbstzertifizierung unverzueglich, spaetestens innerhalb von zehn (10) Kalendertagen, schriftlich mit.
>
> (3) Fuer den Fall, dass die DPF-Selbstzertifizierung des Auftragsverarbeiters endet, ausgesetzt wird oder der Angemessenheitsbeschluss (EU) 2023/1795 ganz oder teilweise unwirksam wird, gelten ab dem Zeitpunkt des Eintritts und ohne weitere Erklaerung der Parteien die EU-Standardvertragsklauseln gemaess Durchfuehrungsbeschluss (EU) 2021/914 der Kommission vom 04.06.2021, Modul 2 (Verantwortlicher an Auftragsverarbeiter), mit den in Anlage 6 dargestellten Auswahl- und Anhangsfestlegungen.
>
> (4) Unabhaengig vom DPF fuehrt der Auftragsverarbeiter auf Verlangen des Verantwortlichen ein Transfer Impact Assessment nach den EDSA-Empfehlungen 01/2020 durch und stellt das Ergebnis innerhalb von dreissig (30) Kalendertagen zur Verfuegung.
>
> (5) Setzt der Auftragsverarbeiter Sub-Auftragsverarbeiter in den Vereinigten Staaten ein, gelten die Absaetze (1) bis (4) entsprechend; im Sub-AV-Verzeichnis ist der DPF-Status jedes US-Sub-AV anzugeben."

## Typische Drafting-Fehler

- Verweis auf DPF ohne tatsaechliche Pruefung des Anbieter-Listings.
- DPF ohne SCC-Fallback im Vertrag – bei Ausfall sofortige Kuendigungspflicht.
- US-Sub-AV ohne eigene DPF-Pruefung.
- TIA nicht durchgefuehrt mit der Begruendung "DPF deckt alles ab" – aufsichtsbehoerdliche Erwartung, dass auch unter DPF eine Risikobetrachtung erfolgt.
- Veraltete Verweise auf Privacy Shield – seit Schrems II (EuGH C-311/18) unwirksam.
- DPF-Listing nur einmal geprueft, keine periodische Kontrolle.

## Quellen Stand 06/2026

- Durchfuehrungsbeschluss (EU) 2023/1795 vom 10.07.2023, ABl. L 231/118 vom 20.09.2023 – verifiziert.
- Durchfuehrungsbeschluss (EU) 2021/914 vom 04.06.2021, ABl. L 199/31 – verifiziert.
- Art. 45, Art. 46, Art. 49 DSGVO.
- US Executive Order 14086 vom 07.10.2022.
- EuGH C-311/18 (Schrems II) – verifiziert; Volltext ueber curia.europa.eu.
- EDSA-Empfehlungen 01/2020 (Version 2.0 Juni 2021).
- DPF-Listing ueber dataprivacyframework.gov pruefen.
- Zitierweise: `../../../references/zitierweise.md`.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 5 DSGVO (Grundsätze der Verarbeitung)
- Art. 6, 9 DSGVO (Rechtsgrundlagen, besondere Datenkategorien)
- Art. 13, 14 DSGVO (Informationspflichten)
- Art. 15 DSGVO (Auskunftsrecht)
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 32 DSGVO (Sicherheit der Verarbeitung)
- Art. 33, 34 DSGVO (Meldepflichten bei Verletzung)
- Art. 82 DSGVO (Schadensersatz)
- Art. 83 DSGVO (Bußgelder)
- §§ 4, 20, 41 BDSG (Aufsicht, Rechtsweg, Strafvorschriften)

### Leitentscheidungen

- EuGH C-300/21 (immaterieller Schaden Art. 82 DSGVO)
- EuGH C-634/21 (automatisierte Bonitätsbewertung Schufa)
- EuGH C-26/22 (Datenschutzbehörden-Befugnisse)
- EuGH C-807/21 (Bußgeldhaftung juristischer Personen)
- BVerfG 1 BvR 16/13 (Recht auf Vergessen I)

### Anwendung im Skill

- Rechtsgrundlage nach Art. 6 DSGVO sauber waehlen; berechtigte Interessen nach Art. 6 Abs. 1 lit. f DSGVO mit dokumentierter Abwaegung.
- Bei Datenpannen die 72-Stunden-Frist nach Art. 33 DSGVO einhalten; Risikoabwaegung Art. 34 DSGVO separat dokumentieren.
- Auskunftsanspruch Art. 15 DSGVO nicht mit Kopie nach Art. 15 Abs. 3 DSGVO verwechseln; EuGH C-307/22 Reichweite beachten.

---

## Skill: `avv-haftung-risikoallokation-art-82-dsgvo`

_Haftungsverteilung Risikoallokation und Haftungscaps im AVV im Lichte von Art. 82 DSGVO. Klaert Aussenhaftung gegenueber Betroffenen Innenregress zwischen Verantwortlichem und Auftragsverarbeiter sowie zulaessige und unzulaessige vertragliche Begrenzungen. Output: Klausel-Bausteine für Innen- und..._

# AVV-Haftung und Risikoallokation – Art. 82 DSGVO

## Zweck / Purpose

Verteilung der DSGVO-Haftungsrisiken zwischen Verantwortlichem und Auftragsverarbeiter; Trennung von Aussenhaftung gegenueber Betroffenen und Innenregress; Grenzen vertraglicher Haftungsbegrenzungen. Purpose (EN): Liability allocation between controller and processor under Article 82 GDPR.

## Wann dieses Modul hilft

- Haftungscaps im AVV werden verhandelt.
- Mandant hat Schadensersatzanspruch gegen den Vertragspartner zu pruefen.
- Aussenhaftung gegenueber einem Betroffenen ist eingetreten und der Innenregress steht an.
- Mandant beziffert das Restrisiko für ein Cyber-Versicherungsdeckungsgespraech.

## Rechtlicher Rahmen

- Art. 82 Abs. 1 DSGVO: Jeder, der wegen eines Verstosses gegen die DSGVO einen materiellen oder immateriellen Schaden erlitten hat, hat Anspruch auf Schadenersatz gegen den Verantwortlichen oder den Auftragsverarbeiter.
- Art. 82 Abs. 2 DSGVO: Verantwortlicher haftet für den Schaden, den eine seiner Verarbeitungen verursacht hat. Auftragsverarbeiter haftet, wenn er gegen speziell ihm auferlegte Pflichten verstossen hat oder Weisungen des Verantwortlichen widersprochen oder ueberschritten hat.
- Art. 82 Abs. 3 DSGVO: Befreiung, wenn nachgewiesen wird, dass der Schaden in keiner Weise zu vertreten ist.
- Art. 82 Abs. 4 DSGVO: Gesamtschuldnerische Haftung mehrerer Verantwortlicher / Auftragsverarbeiter, wenn an demselben Verarbeitungsvorgang beteiligt.
- Art. 82 Abs. 5 DSGVO: Innenregress nach Mass des Verschuldensanteils.
- Art. 28 Abs. 10 DSGVO: Bei Ueberschreiten der Weisungen wird Auftragsverarbeiter zum Verantwortlichen.
- EuGH-Linie zu Art. 82 DSGVO: Konkrete Aktenzeichen vor Zitat ueber curia.europa.eu verifizieren; aus dem Modellwissen wird kein Aktenzeichen zitiert.

## Ablauf / Checkliste

1. **Aussenhaftung mappen.**
 - Wer ist gegenueber Betroffenen Anspruchsgegner? Verantwortlicher allein, Auftragsverarbeiter, beide?
 - Gesamtschuld nach Art. 82 Abs. 4 DSGVO bei gemeinsamer Beteiligung am Verarbeitungsvorgang.

2. **Innenregress regeln.**
 - Mass nach Art. 82 Abs. 5 DSGVO: anteilige Verantwortung.
 - Beweislast: jede Partei muss ihren Pflichtenkreis dokumentieren.
 - Vertragliche Vereinbarung darf den gesetzlichen Innenregress nicht ausschliessen, aber konkretisieren (Pauschalierung, Schadensobergrenzen).

3. **Cap-Diskussion.**
 - Aussenhaftung kann nicht durch Vertrag zwischen Verantwortlichem und Auftragsverarbeiter zu Lasten des Betroffenen begrenzt werden.
 - Innenregress-Cap zulaessig, soweit nicht gegen § 307 BGB (AGB), Vorsatz und grobe Fahrlaessigkeit nicht ausschliessbar.
 - Branchenuebliche Caps: 12-Monats-Honorar, oft mit Sub-Cap für Datenschutzverletzungen.

4. **Versicherung.**
 - Cyber-Versicherung des Auftragsverarbeiters: Deckungssumme, Selbstbehalt, Geltungsbereich.
 - Pflicht zur Vorlage des Versicherungsnachweises (Versicherungsbestaetigung).
 - DSGVO-Bussgelder regelmaessig versicherungsausschluss.

5. **Sub-AV-Kette.**
 - Haftung in der Kette wird durch Art. 28 Abs. 4 DSGVO durchgereicht.
 - Primaerer Auftragsverarbeiter haftet weiter für Sub-AV.
 - Regress des primaeren Auftragsverarbeiters gegen Sub-AV vertraglich zu sichern.

## Mustertext / Template

Haftungsklausel:

> "§ X Haftung
>
> (1) Die Parteien haften gegenueber Betroffenen nach Massgabe des Art. 82 DSGVO. Diese gesetzliche Haftung wird durch die nachstehenden vertraglichen Regelungen zur Innenhaftung nicht beruehrt.
>
> (2) Im Innenverhaeltnis tragen Verantwortlicher und Auftragsverarbeiter den Schaden im Verhaeltnis ihres jeweiligen Verschuldensanteils. Hat ein Auftragsverarbeiter den vollen Schadenersatz an einen Betroffenen geleistet, steht ihm gegen den Verantwortlichen ein Regressanspruch in Hoehe des Verschuldensanteils des Verantwortlichen zu (Art. 82 Abs. 5 DSGVO).
>
> (3) Die Haftung des Auftragsverarbeiters gegenueber dem Verantwortlichen aus oder im Zusammenhang mit diesem Vertrag, einschliesslich Regressansprueche nach Absatz (2), ist auf einen Betrag von [BETRAG] EUR pro Schadensfall und insgesamt auf [BETRAG] EUR pro Kalenderjahr begrenzt. Die Begrenzung gilt nicht bei Vorsatz und grober Fahrlaessigkeit sowie nicht für Schaeden aus der Verletzung des Lebens, des Koerpers oder der Gesundheit.
>
> (4) Der Auftragsverarbeiter haelt waehrend der Vertragslaufzeit eine Cyber-Haftpflichtversicherung mit einer Deckungssumme von mindestens [BETRAG] EUR pro Schadensfall und mindestens [BETRAG] EUR pro Versicherungsjahr vor. Der Versicherungsnachweis wird dem Verantwortlichen jaehrlich unaufgefordert vorgelegt.
>
> (5) DSGVO-Bussgelder, die einer Partei direkt durch eine Aufsichtsbehoerde auferlegt werden, traegt diese Partei selbst. Im Innenverhaeltnis besteht ein Erstattungsanspruch nur, soweit das Bussgeld auf einer schuldhaften Pflichtverletzung der anderen Partei beruht.
>
> (6) Der Auftragsverarbeiter haftet für das Verhalten seiner Sub-Auftragsverarbeiter in dem Umfang wie für eigenes Verhalten (Art. 28 Abs. 4 DSGVO)."

## Typische Drafting-Fehler

- Vollstaendige Haftungsfreistellung des Auftragsverarbeiters – nicht zulaessig wegen Art. 82 Abs. 2 DSGVO.
- Cap auch für Vorsatz und grobe Fahrlaessigkeit – AGB-rechtlich unwirksam (§ 309 Nr. 7 BGB).
- Pauschale Uebernahme aller Aussenhaftungsrisiken – wirtschaftlich unrealistisch ohne Versicherung.
- Bussgelder-Regress ohne Bezug zur konkreten Pflichtverletzung – Art. 83 DSGVO Sanktionscharakter spricht gegen pauschalen Regress.
- Versicherungsnachweis nicht eingefordert.
- Sub-AV-Haftung nicht thematisiert.

## Quellen Stand 06/2026

- Art. 82, Art. 28 Abs. 4, Art. 28 Abs. 10, Art. 83 DSGVO.
- § 307, § 309 Nr. 7 BGB (AGB-rechtliche Schranken).
- EuGH-Linie zu Art. 82 DSGVO: konkrete Aktenzeichen vor Zitat ueber curia.europa.eu verifizieren; keine Aktenzeichen aus dem Modellwissen.
- Zitierweise: `../../../references/zitierweise.md`.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 5 DSGVO (Grundsätze der Verarbeitung)
- Art. 6, 9 DSGVO (Rechtsgrundlagen, besondere Datenkategorien)
- Art. 13, 14 DSGVO (Informationspflichten)
- Art. 15 DSGVO (Auskunftsrecht)
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 32 DSGVO (Sicherheit der Verarbeitung)
- Art. 33, 34 DSGVO (Meldepflichten bei Verletzung)
- Art. 82 DSGVO (Schadensersatz)
- Art. 83 DSGVO (Bußgelder)
- §§ 4, 20, 41 BDSG (Aufsicht, Rechtsweg, Strafvorschriften)

### Leitentscheidungen

- EuGH C-300/21 (immaterieller Schaden Art. 82 DSGVO)
- EuGH C-634/21 (automatisierte Bonitätsbewertung Schufa)
- EuGH C-26/22 (Datenschutzbehörden-Befugnisse)
- EuGH C-807/21 (Bußgeldhaftung juristischer Personen)
- BVerfG 1 BvR 16/13 (Recht auf Vergessen I)

### Anwendung im Skill

- Rechtsgrundlage nach Art. 6 DSGVO sauber waehlen; berechtigte Interessen nach Art. 6 Abs. 1 lit. f DSGVO mit dokumentierter Abwaegung.
- Bei Datenpannen die 72-Stunden-Frist nach Art. 33 DSGVO einhalten; Risikoabwaegung Art. 34 DSGVO separat dokumentieren.
- Auskunftsanspruch Art. 15 DSGVO nicht mit Kopie nach Art. 15 Abs. 3 DSGVO verwechseln; EuGH C-307/22 Reichweite beachten.

---

## Skill: `avv-konzern-und-multi-party-konstellation`

_AVV im Konzern und in Multi-Party-Konstellationen. Behandelt Konzern-AVV mit zentraler Group-IT Shared-Service-Center und konzernweiter Liste der Auftragsverarbeiter. Klaert die Frage ob Konzern als Einheit auftritt oder jede Gesellschaft eigenstaendig. Output: Konzern-AVV-Klauselgeruest mit Beit..._

# AVV im Konzern und in Multi-Party-Konstellationen

## Zweck / Purpose

Strukturierung von Auftragsverarbeitungsvertraegen in Konzernverbuenden und Multi-Party-Konstellationen, in denen mehrere Konzerngesellschaften gemeinsam Auftraggeber oder gemeinsam Auftragnehmer sind. Purpose (EN): How to structure DPAs in corporate group setups and multi-party constellations.

## Wann dieses Modul hilft

- Konzernmutter und mehrere Toechter beziehen denselben Cloud-Dienst und sollen unter einem Vertragsschirm liegen.
- Konzernweite Shared-Service-Center (HR, IT, Payroll) verarbeiten Daten anderer Konzerngesellschaften.
- Ein Konsortium oder Joint Venture nimmt gemeinsam Dienstleistungen in Anspruch.
- Es ist abzuklaeren, ob nicht stattdessen Konzern-BCR (Art. 47 DSGVO) oder eine Joint-Controller-Vereinbarung (Art. 26 DSGVO) erforderlich ist.

## Rechtlicher Rahmen

- Art. 28 DSGVO – auch im Konzern keine Privilegierung; jede juristische Person ist eigenstaendige Verantwortliche.
- Erwaegungsgrund 48 DSGVO – Berechtigtes Interesse an konzerninternem Datenaustausch für interne Verwaltungszwecke.
- Erwaegungsgrund 36 DSGVO – Niederlassung und Verantwortlichkeit im Konzern.
- Art. 26 DSGVO – Joint Controller, falls gemeinsame Zweckentscheidung.
- Art. 47 DSGVO – Verbindliche interne Datenschutzvorschriften (BCR).
- § 26 BDSG – Beschaeftigtendatenschutz bei konzerninternem HR-Transfer.

## Ablauf / Checkliste

1. **Konzernstruktur erfassen.**
 - Mutter, Toechter, Schwestern, Gemeinschaftsunternehmen.
 - Wer ist Vertragspartner des Dienstleisters?
 - Wer ist tatsaechlicher Verantwortlicher für die Daten?

2. **Vertragsstrukturen vergleichen.**

 | Struktur | Beschreibung | Anwendungsfall |
 |---|---|---|
 | Hauptvertrag der Mutter mit Beitrittsmechanik | Mutter unterzeichnet, Toechter treten bei | Konzernlizenz Cloud-Dienst |
 | Rahmen-AVV mit Einzelbestellungen | Jede Gesellschaft schliesst eigenen AVV unter Rahmen ab | Multi-Country-Rollout |
 | Multilateraler AVV | Alle Konzerngesellschaften unterzeichnen gemeinsam | Wenige Gesellschaften, hohe Datenkritikalitaet |
 | Konzern-AVV (intra-group) | Mutter ist Auftragsverarbeiter für Toechter (Shared Service) | Group-IT, Group-HR, Group-Finance |

3. **Rollenmix klaeren.**
 - Mutter als Auftragsverarbeiterin der Toechter setzt voraus, dass die Mutter weisungsgebunden ist.
 - Wenn die Mutter eigenstaendige Konzernzwecke verfolgt (Konzernsteuerung, Reporting), liegt regelmaessig Art. 26 DSGVO oder eigene Verantwortlichkeit vor.
 - EuGH C-498/16 (Wirtschaftsakademie / Fanpages) – verifiziert: weite Auslegung gemeinsamer Verantwortlichkeit.

4. **Drittlandbezug pruefen.**
 - Konzern weltweit – BCR nach Art. 47 DSGVO oder SCC nach Beschluss (EU) 2021/914 für jede Konzerngesellschaft im Drittland.
 - DPF nur für US-Konzerngesellschaften mit aktiver Selbstzertifizierung.

5. **Beitrittsmechanik (Docking Clause).**
 - Vergleichbar dem Mechanismus in den EU-SCC nach Beschluss (EU) 2021/914.
 - Beitritt durch Unterzeichnung einer Beitrittsanlage.
 - Wirkung: Beitretende Gesellschaft wird Vertragspartei mit allen Rechten und Pflichten.

## Mustertext / Template

Konzern-AVV-Klauseln (Auszug):

> "Praeambel
>
> Diese Vereinbarung wird zwischen dem Auftragsverarbeiter und [Muttergesellschaft] als koordinierender Konzerngesellschaft geschlossen. Weitere Konzerngesellschaften im Sinne des § 15 AktG koennen dieser Vereinbarung durch Unterzeichnung der Beitrittsanlage (Anlage 5) beitreten. Mit Wirkung der Beitrittsanlage ist die beitretende Konzerngesellschaft Verantwortliche im Sinne dieser Vereinbarung; ihre Rechte und Pflichten richten sich nach den Bestimmungen dieser Vereinbarung.
>
> § 1 Verarbeitungstaetigkeiten
>
> Die Verarbeitung erfolgt für jede Konzerngesellschaft im Umfang der jeweils mit dieser geschlossenen Bestellung. Anlage 1 (Beschreibung der Verarbeitung) wird je Konzerngesellschaft befuellt.
>
> § 2 Weisungsrechte und Weisungsregister
>
> Jede Konzerngesellschaft erteilt Weisungen ausschliesslich für die sie betreffenden Verarbeitungen. Konzernweit gueltige Weisungen werden vom Konzern-Datenschutzbeauftragten dokumentiert. Der Auftragsverarbeiter fuehrt für jede Konzerngesellschaft ein eigenes Weisungsregister.
>
> § 3 Konzerngesamtleitung und Kommunikation
>
> Die Muttergesellschaft uebt für die beigetretenen Konzerngesellschaften die Funktion der zentralen Anlaufstelle aus, soweit dies mit der jeweiligen Konzerngesellschaft schriftlich vereinbart ist. Die Pflichten und Rechte aus Art. 28 DSGVO bestehen unabhaengig davon im Verhaeltnis Auftragsverarbeiter zu jeweiliger Konzerngesellschaft fort.
>
> § 4 Beitritt und Austritt von Konzerngesellschaften
>
> (1) Beitritt: Die Beitrittsanlage ist von der beitretenden Konzerngesellschaft und dem Auftragsverarbeiter zu unterzeichnen.
> (2) Austritt: Eine Konzerngesellschaft kann ihre Teilnahme mit einer Frist von drei Monaten zum Quartalsende beenden; die Pflichten aus § 9 (Loeschung/Rueckgabe) gelten entsprechend."

## Typische Drafting-Fehler

- Annahme einer "Konzernprivilegierung" – existiert in der DSGVO nicht.
- Eine einzige Vertragspartei "im Namen aller Konzerngesellschaften" ohne Vollmacht oder Beitrittsmechanik.
- Konzern-Shared-Service als pauschal "Auftragsverarbeitung" eingestuft, obwohl die Mutter eigene Konzernzwecke verfolgt – tatsaechlich Art. 26 oder eigene Verantwortlichkeit.
- Drittlandbezug einer Konzerngesellschaft uebersehen.
- Beitrittsanlage ohne Pflicht zur Information des Dienstleisters – Versionierungschaos.

## Quellen Stand 06/2026

- DSGVO Art. 28, Art. 26, Art. 47 sowie ErwGr. 36 und 48.
- BDSG § 26.
- EuGH C-498/16 (Wirtschaftsakademie) – verifiziert; Volltext ueber curia.europa.eu.
- EDSA-Leitlinien 07/2020 zur Abgrenzung Verantwortlicher / Auftragsverarbeiter (Final 07.07.2021).
- EU-Kommission Beschluss (EU) 2021/914 mit Docking Clause (Klausel 7).
- Zitierweise: `../../../references/zitierweise.md`.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 5 DSGVO (Grundsätze der Verarbeitung)
- Art. 6, 9 DSGVO (Rechtsgrundlagen, besondere Datenkategorien)
- Art. 13, 14 DSGVO (Informationspflichten)
- Art. 15 DSGVO (Auskunftsrecht)
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 32 DSGVO (Sicherheit der Verarbeitung)
- Art. 33, 34 DSGVO (Meldepflichten bei Verletzung)
- Art. 82 DSGVO (Schadensersatz)
- Art. 83 DSGVO (Bußgelder)
- §§ 4, 20, 41 BDSG (Aufsicht, Rechtsweg, Strafvorschriften)

### Leitentscheidungen

- EuGH C-300/21 (immaterieller Schaden Art. 82 DSGVO)
- EuGH C-634/21 (automatisierte Bonitätsbewertung Schufa)
- EuGH C-26/22 (Datenschutzbehörden-Befugnisse)
- EuGH C-807/21 (Bußgeldhaftung juristischer Personen)
- BVerfG 1 BvR 16/13 (Recht auf Vergessen I)

### Anwendung im Skill

- Rechtsgrundlage nach Art. 6 DSGVO sauber waehlen; berechtigte Interessen nach Art. 6 Abs. 1 lit. f DSGVO mit dokumentierter Abwaegung.
- Bei Datenpannen die 72-Stunden-Frist nach Art. 33 DSGVO einhalten; Risikoabwaegung Art. 34 DSGVO separat dokumentieren.
- Auskunftsanspruch Art. 15 DSGVO nicht mit Kopie nach Art. 15 Abs. 3 DSGVO verwechseln; EuGH C-307/22 Reichweite beachten.

---

## Skill: `avv-loeschung-rueckgabe-nach-vertragsende`

_Pflicht zur Loeschung oder Rueckgabe personenbezogener Daten nach Ende des Auftragsverarbeitungsvertrags gemaess Art. 28 Abs. 3 lit. g DSGVO. Wahlrecht des Verantwortlichen Format und Nachweis Aufbewahrungsausnahmen sowie Backup- und Logfile-Behandlung. Output: Loeschkonzept-Klausel und Loeschpro..._

# Loeschung und Rueckgabe nach Vertragsende – Art. 28 Abs. 3 lit. g DSGVO

## Zweck / Purpose

Strukturierung des Endphase-Managements im AVV: Wahlrecht des Verantwortlichen, Formate, Fristen, Nachweise und Aufbewahrungsausnahmen. Purpose (EN): End-of-contract data return and deletion under Article 28 (3) (g) GDPR.

## Wann dieses Modul hilft

- Vertragsende eines AVV steht bevor oder ist eingetreten.
- Es ist zu klaeren, ob Loeschung oder Rueckgabe verlangt wird.
- Gesetzliche Aufbewahrungspflichten kollidieren mit Loeschanforderungen.
- Backups, Logfiles oder forensische Kopien sind zu behandeln.

## Rechtlicher Rahmen

- Art. 28 Abs. 3 lit. g DSGVO: "alle personenbezogenen Daten nach Abschluss der Erbringung der Verarbeitungsleistungen nach Wahl des Verantwortlichen entweder loescht oder zurueckgibt, sofern nicht nach dem Unionsrecht oder dem Recht der Mitgliedstaaten eine Verpflichtung zur Speicherung der personenbezogenen Daten besteht".
- Art. 17 DSGVO: Recht auf Loeschung.
- Art. 5 Abs. 1 lit. e DSGVO: Speicherbegrenzung.
- § 257 HGB, § 147 AO, § 50 BDSG, § 11 BORA – steuer-, handels- und berufsrechtliche Aufbewahrungspflichten.

## Ablauf / Checkliste

1. **Wahlrecht ausueben.**
 - Verantwortlicher entscheidet: Loeschung, Rueckgabe oder eine Kombination (z. B. Rueckgabe aktiver Daten, Loeschung der Kopien).
 - Wahl muss vor Ende der Verarbeitungsleistungen kommuniziert werden – Vertrag sieht typischerweise 30 Kalendertage vor.

2. **Format definieren.**
 - Strukturierte, gaengige und maschinenlesbare Formate (CSV, JSON, XML) analog Art. 20 DSGVO.
 - Verschluesselter Transport.
 - Datentraegerformat oder API-Endpunkt definieren.

3. **Loeschmethodik.**
 - Loeschstandards: DIN 66399, NIST SP 800-88 Rev. 1.
 - Backups: Loeschung in der naechsten regulaeren Backup-Rotation oder gezielte Loeschung.
 - Logfiles: Aufbewahrungspflicht versus Datensparsamkeit abwaegen.

4. **Aufbewahrungsausnahmen.**
 - § 257 HGB, § 147 AO: 10 Jahre, 6 Jahre.
 - § 50 BDSG: bis Zweckerreichung beendet.
 - § 195 BGB i.V.m. § 199 BGB: Verjährungsablauf abwarten.
 - Sicherstellen: Aufbewahrungsdaten sind separiert, zugriffsbeschraenkt und nicht weiter verarbeitet (Sperrung).

5. **Nachweis.**
 - Loeschprotokoll mit Datum, Bestand, Methode, verantwortlicher Person.
 - Unterschrift durch den Auftragsverarbeiter.
 - Bei Sub-AV: Loeschnachweise aller Sub-AV in der Kette.

## Mustertext / Template

Klausel zu Loeschung und Rueckgabe:

> "§ X Beendigung der Verarbeitung
>
> (1) Nach Beendigung der Erbringung der Verarbeitungsleistungen entscheidet der Verantwortliche innerhalb von dreissig (30) Kalendertagen, ob die personenbezogenen Daten zurueckgegeben oder geloescht werden sollen. Der Verantwortliche kann für verschiedene Datenbestaende unterschiedliche Optionen waehlen.
>
> (2) Bei Wahl der Rueckgabe uebergibt der Auftragsverarbeiter die personenbezogenen Daten innerhalb von dreissig (30) Kalendertagen in einem strukturierten, gaengigen und maschinenlesbaren Format an einen vom Verantwortlichen benannten Empfaenger. Die Uebertragung erfolgt verschluesselt nach dem Stand der Technik.
>
> (3) Bei Wahl der Loeschung loescht der Auftragsverarbeiter die personenbezogenen Daten innerhalb von dreissig (30) Kalendertagen vollstaendig und unwiederbringlich. Backups werden in der naechsten regulaeren Backup-Rotation, spaetestens jedoch innerhalb von neunzig (90) Kalendertagen, ueberschrieben oder geloescht. Die Loeschung erfolgt nach DIN 66399 mindestens nach Schutzklasse 2.
>
> (4) Soweit Unionsrecht oder Recht eines Mitgliedstaats die weitere Speicherung der personenbezogenen Daten vorschreibt (insbesondere § 257 HGB, § 147 AO), bleibt der Auftragsverarbeiter berechtigt, die betroffenen Datensaetze für die gesetzliche Aufbewahrungsdauer in einem zugriffsbeschraenkten, ausschliesslich der Erfuellung der gesetzlichen Pflicht dienenden Bereich vorzuhalten. Der Auftragsverarbeiter dokumentiert Datenart, Rechtsgrundlage und Aufbewahrungsdauer und loescht die Daten unverzueglich nach Ablauf der Aufbewahrungspflicht.
>
> (5) Der Auftragsverarbeiter dokumentiert die Loeschung oder Rueckgabe in einem schriftlichen Protokoll, das dem Verantwortlichen innerhalb von zehn (10) Kalendertagen nach Abschluss der Massnahme vorzulegen ist. Das Protokoll enthaelt Datum, Datenarten, Mengenangaben, Loeschmethode und die verantwortliche Person.
>
> (6) Der Auftragsverarbeiter veranlasst, dass jeder Sub-Auftragsverarbeiter die Pflichten aus diesem Paragraphen entsprechend erfuellt und legt dem Verantwortlichen die Loeschnachweise der Sub-Auftragsverarbeiter auf Verlangen vor."

## Typische Drafting-Fehler

- Kein Wahlrecht des Verantwortlichen ("Daten werden geloescht") – das verletzt Art. 28 Abs. 3 lit. g DSGVO.
- Kein definiertes Format der Rueckgabe – faktische Vendor-Lock-in-Wirkung.
- Aufbewahrungspflichten nicht beruecksichtigt – Konflikt mit § 257 HGB, § 147 AO.
- Backups vergessen.
- Kein Loeschprotokoll und kein Nachweis.
- Sub-AV-Kette nicht erfasst.

## Quellen Stand 06/2026

- Art. 28 Abs. 3 lit. g, Art. 17, Art. 5 Abs. 1 lit. e DSGVO.
- § 257 HGB, § 147 AO, § 50 BDSG, § 11 BORA.
- DIN 66399 – Vernichtung von Datentraegern.
- NIST SP 800-88 Rev. 1 – Guidelines for Media Sanitization.
- Zitierweise: `../../../references/zitierweise.md`.

---

## Skill: `avv-pruefung`

_Auftragsverarbeitungsvertrag nach Art. 28 DSGVO prüfen oder erstellen wenn Dritter Daten im Auftrag verarbeitet. Art. 28 DSGVO AVV-Pflicht § 62 BDSG. Prüfraster: Pflichtinhalte Art. 28 Abs. 3 Weisungsgebundenheit Subauftragsverarbeiter Rückgabe Lösung Audits. Output: AVV-Prüfmemo oder Vertragsent..._

# AVV-Review – Auftragsverarbeitungsvertrag Art. 28 DSGVO

## Eingaben

- AVV-Dokument (Datei oder Paste)
- Richtung (optional): "Wir sind AV" oder "Wir sind Verantwortlicher" – sonst automatische Erkennung
- Optional: Liste bekannter Sub-AVs des Anbieters
- Optional: Land der Datenverarbeitung / Hosting-Region

## Ablauf

1. **Richtungserkennung.** Wer ist "Auftraggeber" / "Verantwortlicher", wer "Auftragnehmer" / "Auftragsverarbeiter" im vorgelegten Dokument? Parteienbezeichnung, Weisungsklauseln und Haftungsstruktur prüfen. Bei Unklarheit fragen.

2. **Art. 28 DSGVO Pflichtklausel-Check.** Jede gesetzlich vorgeschriebene Klausel prüfen:

 | Art. 28 Abs. 3 DSGVO | Pflichtinhalt | Status |
 |---|---|---|
 | lit. a | Weisungsgebundenheit + Weisungsregister | ✓ / ⚠️ / ✗ |
 | lit. b | Vertraulichkeitsverpflichtung verarbeitendes Personal | ✓ / ⚠️ / ✗ |
 | lit. c | Technisch-organisatorische Maßnahmen (TOM) nach Art. 32 DSGVO | ✓ / ⚠️ / ✗ |
 | lit. d | Sub-Auftragsverarbeiter-Regelung (allgemeine oder spezifische Genehmigung) | ✓ / ⚠️ / ✗ |
 | lit. e | Unterstützung bei Betroffenenrechten | ✓ / ⚠️ / ✗ |
 | lit. f | Unterstützung bei Art. 32–36 DSGVO (DSFA, Datenpanne, Vorab-Konsultation) | ✓ / ⚠️ / ✗ |
 | lit. g | Löschung oder Rückgabe nach Vertragsende | ✓ / ⚠️ / ✗ |
 | lit. h | Audit-Recht und Nachweispflichten | ✓ / ⚠️ / ✗ |

3. **Playbook-Abgleich.** Jede Klausel mit der eigenen Standardposition aus `CLAUDE.md` vergleichen:
 - ✅ Standardposition = akzeptabel
 - ⚠️ Fallback-Position = bedingt akzeptabel, mit Bedingungen
 - 🔴 Unter Playbook-Minimum = nicht akzeptabel, Redline-Vorschlag

4. **Sub-Auftragsverarbeiter-Prüfung.**
 - Allgemeine vs. spezifische Genehmigung (Art. 28 Abs. 2 DSGVO)?
 - Wechselbenachrichtigungsfrist vorhanden? (Praxis: 4 Wochen; kürzer = Einspruchsrecht faktisch ausgehöhlt)
 - Haftungsüberleitung auf Sub-AV in gleichem Umfang (Art. 28 Abs. 4 DSGVO)?
 - Liste der Sub-AVs verfügbar / aktuell?
 - Sub-AVs in Drittländern? → Weiterleitung zu Schritt 5 (TIA).

5. **Drittlandtransfer-Check (TIA).**
 - Werden Daten außerhalb EU/EWR verarbeitet oder zugänglich gemacht?
 - Welcher Transfermechanismus: EU-SCC (Beschluss 2021/914), DPF, BCR, Art. 49 Abs. 1 DSGVO Ausnahmen?
 - EU-SCC: Modul korrekt (AV-zu-AV, Verantwortlicher-zu-AV)? Technische Anlage befüllt?
 - DPF: Anbieter auf DPF-Liste eingetragen (data.privacyframework.gov)? `[Modellwissen – prüfen, da DPF ggf. geändert]`
 - TIA nach EDSA-Empfehlungen 01/2020 erforderlich? (Ja, wenn SCC ohne zusätzliche Schutzmaßnahmen nicht ausreichen)
 - Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

6. **Redline-Vorschläge.** Für jede 🔴-Klausel konkreten Änderungsvorschlag formulieren – in Vertragssprache, nicht als Memo-Kommentar.

7. **Bewertungstabelle und Empfehlung.**
 - Gesamt-Risikobewertung: 🔴 Blockend / 🟠 Hoch / 🟡 Mittel / 🟢 Gering
 - Empfehlung: Unterzeichnen / Mit Redlines unterzeichnen / Ablehnen / Eskalieren

## Quellen und Zitierweise

Verbindlich nach `../../references/zitierweise.md`.

- Art. 28 DSGVO (Auftragsverarbeitung, Mindestinhalt AVV)
- Art. 28 Abs. 2 DSGVO (Sub-Auftragsverarbeiter)
- Art. 28 Abs. 4 DSGVO (Haftungsüberleitung Sub-AV)
- Art. 32 DSGVO (TOM)
- Art. 44–49 DSGVO (Drittlandtransfer)
- Beschluss 2021/914/EU (EU-SCC, neue Standardvertragsklauseln)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- EDSA-Empfehlungen 01/2020 zur Transferfolgenabschätzung (TIA), Stand 2022
- EDSA-Leitlinien 07/2022 zu Zertifizierungen als Transfermechanismus
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Schantz, in: Simitis/Hornung/Spiecker, Datenschutzrecht, 1. Aufl. 2019, Art. 28 Rn. 1 ff.
- Werkmeister, in: Gola, DSGVO, 2. Aufl. 2018, Art. 28 Rn. 1 ff.
- Plath, in: Plath, DSGVO/BDSG, 3. Aufl. 2021, Art. 28 Rn. 1 ff.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — AVV eines KI-Anbieters für Kanzlei pruefen | Pruefschema Art. 28 DSGVO; Template unten |
| Variante A — AVV des Anbieters nicht verhandelbar | Risikoanalyse dokumentieren; Mandantenhinweis erwaegen |
| Variante B — eigene AVV als Auftragsverarbeiter erstellen | Umgekehrte Perspektive; eigene Pflichten aus Art. 28 Abs. 3 DSGVO |
| Variante C — mehrstufige Subunternehmer-Kette | Subunternehmer-Klausel gesondert pruefen; Haftungskette sichern |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Beispiel (Gutachtenstil)

**Sachverhalt:** Ein SaaS-Anbieter aus den USA legt einen AVV vor. Daten werden auf AWS-Servern in der EU (Frankfurt) sowie auf Support-Systemen in den USA verarbeitet.

**Analyse Sub-AV-Klausel:**
Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

**Redline-Vorschlag:**
> "Der Auftragsverarbeiter informiert den Verantwortlichen mindestens **30 (dreißig)** Tage im Voraus über geplante Änderungen an der Sub-Auftragsverarbeiter-Liste. Innerhalb dieser Frist kann der Verantwortliche Einspruch erheben. Bei berechtigtem Einspruch, den der Auftragsverarbeiter nicht durch zumutbare technische oder organisatorische Maßnahmen ausräumen kann, ist der Verantwortliche zur außerordentlichen Kündigung berechtigt."

**Analyse Drittlandtransfer (USA, Support-Systeme):**
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
1. Rechtslage im Empfängerland (USA: FISA Section 702, EO 14086 – PPD-28-Nachfolger) `[Modellwissen – prüfen]`
2. Praktische Wahrscheinlichkeit des Zugriffs (Support-Systeme mit Personalbezug: mittel)
3. Zusätzliche Schutzmaßnahmen erforderlich? (Empfehlung: Pseudonymisierung Support-Daten, Zugriffsprotokolle)

## Risiken / typische Fehler

- **Richtungsverwechslung:** Falsches SCC-Modul hat keine Schutzwirkung. Art. 28 Abs. 4 DSGVO setzt voraus, dass Sub-AV-Kette rechtswirksam abgesichert ist.
- **Veraltete SCC:** Altes SCC-Muster (2001/497/EG, 2004/915/EG) ist seit 27.09.2021 nicht mehr für neue Verträge verwendbar; bestehende Altverträge waren bis 27.12.2022 umzustellen (§ 46 Abs. 5 DSGVO-Beschluss). `[Modellwissen – aktuellen Status prüfen]`
- **DPF-Validität:** Das EU-US Data Privacy Framework steht unter politischem Vorbehalt (vgl. Schrems II zur Vorgänger-Regelung). DPF-Eintrag auf data.privacyframework.gov vor Unterschrift prüfen.
- **TIA nur Formalie:** Eine TIA muss ehrliche Risikobewertung enthalten. Pauschal "Risiko akzeptabel" ohne Begründung genügt Art. 28 DSGVO und den EDSA-Empfehlungen 01/2020 nicht.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- **Berufsgeheimnisträger:** Bei Mandanten-AVVs (Kanzleien, Ärzte) muss der AVV § 203 StGB und § 43a Abs. 2 BRAO berücksichtigen – unzureichende Vertraulichkeitsklausel kann Strafbarkeit begründen.

## Quellen / Updates

Stand: 05/2026. Aktualität prüfen bei neuen EDSA-Leitlinien zur Auftragsverarbeitung, Änderungen des SCC-Beschlusses 2021/914/EU oder neuen DPF-Entwicklungen.

**Hinweis EDSA-Leitlinien zur Auftragsverarbeitung:** Der EDSA hat Leitlinien zur Abgrenzung von Verantwortlichen und Auftragsverarbeitern veröffentlicht (EDSA, Leitlinien 07/2020 zur Abgrenzung Verantwortlicher/Auftragsverarbeiter, angenommen 07.07.2021). Diese sind bei der Richtungserkennung (Schritt 1) und bei der Prüfung der Pflichtklauseln verbindlich heranzuziehen. Insbesondere: Wer weisungsgebunden und ohne eigenen Entscheidungsspielraum verarbeitet, ist Auftragsverarbeiter; eigenständige Zwecksetzung begründet Mit-Verantwortlichkeit (Art. 26 DSGVO). `[Modellwissen – aktuellen EDSA-Leitlinienstand auf edpb.europa.eu prüfen]`

**Querverweise:**
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md` — Vollständige TIA-Methodik und SCC-Modul-Auswahl-Matrix
- `datenschutzrecht/skills/dsfa-erstellung/SKILL.md` — DSFA bei Hochrisiko-AVV-Konstellationen

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Faktische Updates (Stand 05/2026)

- **EDSA Guidelines 07/2020 zu Verantwortlichen und Auftragsverarbeitern:** Final-Version verbindliche Auslegungshilfe; bei der Rollenzuordnung beruecksichtigen. Quelle: edpb.europa.eu.
- **EDSA Stellungnahme 22/2024 zu Auftragsverarbeitern und Sub-AV:** Aktuelle Stellungnahmen zur Sub-Verarbeiter-Kette und zur Verantwortlichkeit live ueber edpb.europa.eu pruefen.
- **EuGH-Linie zu Art. 82 DSGVO Mit-Haftung:** Verantwortlicher und Auftragsverarbeiter haften gesamtschuldnerisch nach Massgabe ihrer jeweiligen Pflichtverletzungen (Art. 82 Abs. 4 DSGVO). Konkrete Aktenzeichen vor Zitat ueber curia.europa.eu pruefen.
- **EU-US-DPF-Status:** Vor jedem US-AVV-Abschluss DPF-Listing des Anbieters ueber dataprivacyframework.gov verifizieren. SCC bleiben als Fallback im AVV vorzusehen.
- **KI-Anbieter-AVV:** Bei KI-/LLM-Diensten muessen AVV-Klauseln zusaetzlich zu Art. 28 DSGVO Trainings-Verbote, Output-Verwertung, Modellaenderungen, Logging und KI-VO-Pflichten regeln. Verweis: ki-anbieter-pruefung (Plugin ki-governance).
- **NIS-2-Lieferkette (Art. 21 NIS-2-RL):** Auftraggeber wichtiger / besonders wichtiger Einrichtungen muessen Cyber-Risiken in der Lieferkette beruecksichtigen — AVV mit IT-/Cloud-Dienstleistern entsprechend erweitern.

## Triage-Frage (Entscheidungsbaum AVV)

```
Prüfungsrichtung?
 Eingehender AVV (wir sind Verantwortlicher) → Prüfe: Weisungsrecht vollständig?
 Ausgehender AVV (wir sind Auftragsverarbeiter) → Prüfe: Pflichten Art. 28 Abs. 3 vollständig?
 Unklar → Richtungserkennung über Parteienbezeichnung und Weisungsklausel

Drittlandbezug?
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Nein → kein TIA erforderlich

Sub-AVs mit Drittlandexposure?
 Ja → Art. 28 Abs. 4 DSGVO: Pflichten vollständig übergeleitet?
 Nein → nur Listenpflicht und Wechselbenachrichtigung prüfen
```
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Output-Template — AVV-Review-Ergebnis

**Adressat:** Datenschutzbeauftragter / Rechtsabteilung — Tonfall: sachlich-juristisch

```
AVV-Review [DATUM]
Dokument: [BEZEICHNUNG, VERSION]
Richtung: Verantwortlicher / Auftragsverarbeiter
Gesamt-Risiko: ROT / ORANGE / GELB / GRUEN

Pflichtklausel-Status (Art. 28 Abs. 3 DSGVO):
| Buchstabe | Inhalt | Status | Kommentar |
|-----------|----------------------------|--------|-----------|
| lit. a | Weisungsgebundenheit | | |
| lit. b | Vertraulichkeit | | |
| lit. c | TOM Art. 32 DSGVO | | |
| lit. d | Sub-AV-Regelung | | |
| lit. e | Unterstuetzung Betr.-R. | | |
| lit. f | Unterstuetzung Art. 32-36 | | |
| lit. g | Loeschung/Rueckgabe | | |
| lit. h | Audit-Recht | | |

Drittlandtransfer: ja / nein
TIA erforderlich: ja / nein
Empfehlung: Unterzeichnen / Mit Redlines / Ablehnen
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

