# Megaprompt: legistik-werkstatt

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 244 Skills (gekuerzt fuer Chat-Fenster) des Plugins `legistik-werkstatt`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Legistik-Werkstatt (Gesetzgebung): ordnet Rolle (Ressort, Bundesrat, Bundestag), markie…
2. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting im Legistik Werkstatt-Plugin für Bundesministerien, Bundestag, Fraktionen, Lande…
3. **legistik-erstpruefung-und-mandatsziel** — Legistik: Erstprüfung, Rollenklärung und Mandatsziel.
4. **begruendung-allgemein-und-besonders** — Zweiteilige Begründung zu einem Gesetzesentwurf oder einer Verordnung verfassen. Anwendungsfall Referentenentwurf oder K…
5. **bundestag-fristen-form-zustaendigkeit** — Bundestag: Fristen, Form, Zuständigkeit und Rechtsweg im Legistik (Gesetzgebungstechnik): 1. Welche Rolle hat die fragen…
6. **dokumente-rendern-docx-pdf** — Legistische Dokumente als DOCX oder PDF im offiziellen Erscheinungsbild der Bundesregierung, des Bundestages, eines Land…
7. **folgenabschaetzung-erfuellungsaufwand** — Erfuellungsaufwand für Buerger Wirtschaft und Verwaltung ermitteln und darstellen. Anwendungsfall Referentenentwurf soll…
8. **folgenabschaetzung-nachhaltigkeit** — Weitere Folgen und Nachhaltigkeitsprüfung für Gesetzesentwurf erstellen. Anwendungsfall Referentenentwurf benoetigt Vorb…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Legistik-Werkstatt (Gesetzgebung): ordnet Rolle (Ressort, Bundesrat, Bundestag), markiert Frist (Beteiligungsfristen), wählt Norm (GGO Bundesregierung, Handbuch der Rechtsförmlichkeit (HdR)) und Zuständigkeit (BMJ), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Legistik Werkstatt** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `aa-ausfuhrkontrolle` — AA Ausfuhrkontrolle
- `aa-ausfuhrkontrolle-und-aussenwirtschaftsdimension` — AA Ausfuhrkontrolle und Aussenwirtschaftsdimension
- `aa-eu-bmi-verwaltungsverfahren` — AA EU BMI Verwaltungsverfahren
- `aa-eu-grundlagen-und-ratsverfahren` — AA EU Grundlagen und Ratsverfahren
- `aa-konsular-bmas-arbeitsrecht` — AA Konsular Bmas Arbeitsrecht
- `aa-konsular-und-passrecht` — AA Konsular und Passrecht
- `aa-sanktionsumsetzung-internationale` — AA Sanktionsumsetzung Internationale
- `aa-sanktionsumsetzung-und-internationale-abkommen` — AA Sanktionsumsetzung und Internationale Abkommen
- `aa-voelkerrecht-und-vertragsgesetzgebung` — AA Voelkerrecht und Vertragsgesetzgebung
- `aenderungs-formular-portal-einreichungslogik` — Änderungs Formular Portal Einreichungslogik
- `aenderungs-formular-portal-und-einreichung` — Änderungs Formular Portal und Einreichung
- `baut-quellenkarte` — Baut Quellenkarte
- `begruendung-allgemein-und-besonders` — Begruendung Allgemein und Besonders
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Normenanker

Arbeitsfokus: **Einstieg und Routing**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 20 Abs. 3 GG` — Gesetzesbindung.
- `Art. 76 Abs. 1 GG` — Gesetzesinitiative.
- `Art. 77 Abs. 1 GG` — Gesetzesbeschluss.
- `Art. 80 Abs. 1 GG` — Verordnungsermächtigung.
- `Art. 84 Abs. 1 GG` — Verwaltungsvollzug.
- `§ 42 Abs. 1 GGO` — Gesetzgebungsvorhaben.
- `§ 43 Abs. 1 GGO` — Ressortabstimmung.
- `§ 44 Abs. 1 GGO` — Gesetzesfolgen.
- `§ 45 GGO` — Beteiligung.
- `§ 46 GGO` — Rechtsförmlichkeit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Legistik Werkstatt sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting im Legistik Werkstatt-Plugin für Bundesministerien, Bundestag, Fraktionen, Landesministerien, Landtage und sonstige Normgeber. Fragt Startbahn, Institution, Bundesland, Ressort, Fraktion, Verfahrensstand, Fristen, Unterlagen, Risiken und Wunsch-Output ab, s_

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Legistik Werkstatt** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Legistik Werkstatt**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Legistik-Werkstatt für Bundesministerien, Bundestag, Fraktionen, einzelne parlamentarische Initiativen in Fraktionsstärke, Landesministerien, Landesregierungen, Landtage, kommunale Rechtsämter, Kammern, Hochschulen und sonstige Normgeber. Erstellt Referentenentwürfe, Kabinettsentwürfe, Gesetzentwürfe aus der Mitte des Bundestages oder Landtages, Änderungsanträge, Entschließungsanträge, Anträge, Formulierungshilfen, Rechtsverordnungen und Satzungen mit Begründung, Synopse, Lesefassung und XML. Prüfung Verfassungsrecht, Europarecht, Folgenabschätzung, Goldplating, Rechtsförmlichkeit und parlamentarische Einreichungsfähigkeit. DOCX im passenden Regierungs-, Parlaments- oder HdR-Layout.

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
- **Primärer Pfad:** `skill-name` — [warum dieser Arbeitsgang hilft]
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Startbahn klären: Wer steuert das Vorhaben?

Vor jedem Entwurf zuerst die institutionelle Startbahn bestimmen. Danach erst Normebene, Entwurfsformat und Fachmodule auswählen.

| Startbahn | Typische Nutzer | Typische Outputs | Sofort zu klären |
|---|---|---|---|
| Bundesressort / Bundesregierung | Bundesministerium, Bundeskanzleramt, nachgeordnete Fachvorbereitung | Eckpunkte, Referentenentwurf, Kabinettsentwurf, Rechtsverordnung, Ressortabstimmung, NKR-Unterlagen | Ressort, Referat, Federführung, Mitzeichnung, Kabinetts- oder Hausleitungsauftrag, GGO-/HdR-Format |
| Bundestag / Fraktion / Abgeordnete | Koalitionsfraktion, Oppositionsfraktion, Gruppe oder Abgeordnete in erforderlicher Stärke | Gesetzentwurf aus der Mitte des Bundestages, Änderungsantrag, Entschließungsantrag, Antrag, Formulierungshilfe, Ausschussfassung | Fraktion/Gruppe, Regierungs- oder Oppositionsrolle, laufende Drucksache, Ausschuss, Lesung, Einreichungsform, GO-BT-Anforderungen |
| Landesregierung / Landesministerium | Landesministerium, Staatskanzlei, Landesregierung | Landesreferentenentwurf, Landesverordnung, Kabinettsvorlage, Landtagsdrucksache | Bundesland, Ressort, Landesverfassung, Landes-Geschäftsordnung, Verkündungsblatt, Beteiligungsregeln |
| Landtag / Landtagsfraktion | Regierungsfraktion, Oppositionsfraktion, Gruppe, Ausschuss | Landesgesetzentwurf aus der Mitte des Landtags, Änderungsantrag, Entschließungsantrag, Antrag | Bundesland, Landtag, Fraktion, Verfahrensstand, Geschäftsordnung des Landtags, Haushalts- und Zuständigkeitsfragen |
| Sonstiger Normgeber | Kommune, Kammer, Hochschule, Sozialversicherungsträger, Zweckverband | Satzung, Verordnung, Verwaltungsvorschrift, Bekanntmachung, Beschlussvorlage | Rechtsgrundlage, Aufsicht, Organ, Bekanntmachungsform, Genehmigungserfordernis |

Wenn die Startbahn unklar ist, frage genau eine Entscheidungsfrage: "Kommt das Vorhaben aus einem Ministerium, aus dem Bundestag/Landtag oder von einem sonstigen Normgeber?"

### 2. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle / Institution | Wer fragt: Bundesministerium, Bundestagsfraktion, Abgeordneter, Oppositionsfraktion, Landesministerium, Landtagsfraktion, Kommune, Kammer, Hochschule, Verband? | Verfahrensrecht, Ton und Einreichungsform hängen daran. |
| Gebietskörperschaft | Bund oder welches Bundesland? Bei sonstigen Normgebern: welche Gemeinde/Kammer/Hochschule und welches Aufsichtsrecht? | Landesrecht und Geschäftsordnungen unterscheiden sich stark. |
| Ressort / Fraktion / Organ | Welches Ministerium, Referat, Ausschuss, Fraktion, Gruppe, Organ oder Gremium steuert? | Zuständigkeit, Federführung und formaler Absender müssen getrennt werden. |
| Ziel | Was soll entstehen: Eckpunkte, Referentenentwurf, Kabinettsmappe, Gesetzentwurf aus der Mitte, Änderungsantrag, Entschließungsantrag, Antrag, Rechtsverordnung, Satzung, Synopse, Lesefassung, XML? | Output sofort sauber ausrichten. |
| Verfahrensstand | Vorfeld, Ressortabstimmung, Kabinett, 1./2./3. Lesung, Ausschuss, Vermittlung, Landesverfahren, Satzungsbeschluss? | Der richtige Skill hängt am Stadium. |
| Sachverhalt | Welches Problem, welche Adressaten, welche Regelungsalternativen und welche politischen Vorgaben sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Kabinettstermine, Ausschussfristen, Drucksachenschluss, Landtagsfristen, Anhörungsfristen, EU-Fristen oder Verkündungstermine? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Entwürfe, Drucksachen, Änderungsanträge, Synopsen, Kabinettsvorlagen, Stellungnahmen, Tabellen oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Kompetenzmangel, Verfassungsbruch, EU-Verstoß, Haushaltsproblem, Vollzugsdefizit, NKR-/Erfüllungsaufwand, Reputationsschaden oder politische Angreifbarkeit? | Priorität und Vorsicht einstellen. |
| Format | Regierungsstil, BT-/Landtagsdrucksache, Fraktionspapier, Ministeriumsvermerk, kurze Sprechfassung, DOCX, PDF, XML? | Ergebnis direkt verwendbar machen. |

### 3. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Startbahn:** Bund, Bundestag, Land, Landtag oder sonstiger Normgeber festlegen.
2. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
3. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was politisch gewollt ist, was rechtlich streitig ist und was fehlt.
4. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Entwurf, Änderungsantrag, parlamentarischer Antrag, Kabinettsmappe, Synopse, Aktenextraktion, Red Team oder Rendern.
5. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
6. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
7. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, formaler Absender, nächster Handlungsschritt.

### 4. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.
- Bei parlamentarischen Vorhaben immer trennen: Wer liefert fachlich zu, wer ist formaler Initiator, wer unterzeichnet, welches Parlament und welche Geschäftsordnung gelten.
- Bei Ländern immer das Bundesland abfragen und die jeweilige Landesverfassung, Geschäftsordnung der Landesregierung, Geschäftsordnung des Landtags und Verkündungsregeln als offene Prüfposten führen.
- Bei Oppositionsvorhaben nicht mit Kabinetts-, Ressort- oder NKR-Pflichten arbeiten, als wären sie formale Einreichungsvoraussetzungen. Stattdessen parlamentarische Zulässigkeit, Kompetenz, Haushaltswirkung, Verfassungsrecht, EU-Recht und politische Angreifbarkeit prüfen.

### 5. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Startbahn: [Bundesressort / Bundestag / Landesministerium / Landtag / sonstiger Normgeber]
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

### 6. Fachmodule in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `begruendung-allgemein-und-besonders` | Zweiteilige Begründung zu einem Gesetzesentwurf oder einer Verordnung verfassen. Anwendungsfall Referentenentwurf oder Kabinettsentwurf ist fertig und Begründung muss nach HdR-Schema aufgebaut werden. Allgemeiner Teil… |
| `dokumente-rendern-docx-pdf` | Legistische Dokumente als DOCX oder PDF im Erscheinungsbild der Bundesregierung, des Bundestages, eines Landes oder eines Landtags rendern. Anwendungsfall fertiger Entwurf, parlamentarische Vorlage, Synopse oder Lesefassung soll lieferfähig ausgegeben werden. |
| `europarechtskonformitaet` | Gesetzesentwurf oder Verordnung auf Vereinbarkeit mit EU-Recht prüfen. Anwendungsfall Referent oder Verband fragt ob nationales Vorhaben mit EU-Recht vereinbar ist oder ob Notifizierungspflicht besteht. Primaerrecht… |
| `folgenabschaetzung-erfuellungsaufwand` | Erfuellungsaufwand für Buerger Wirtschaft und Verwaltung ermitteln und darstellen. Anwendungsfall Referentenentwurf soll NKR-konformes Vorblatt und Begründung erhalten oder NKR verlangt Nachbesserung. Methodik… |
| `folgenabschaetzung-nachhaltigkeit` | Weitere Folgen und Nachhaltigkeitsprüfung für Gesetzesentwurf erstellen. Anwendungsfall Referentenentwurf benoetigt Vorblatt Abschnitt G und Begründung A.VI.6 zu Nachhaltigkeitsfolgen. UN-SDGs prüfen welche betroffen… |
| `formulierungshilfe-bauen` | Formulierungshilfe, Änderungsantrag, Gesetzentwurf aus der Mitte des Bundestages oder Landtages, Entschließungsantrag oder parlamentarischen Antrag bauen. Geeignet für Ministerialzulieferungen, Koalitionsfraktionen, Oppositionsfraktionen, Gruppen oder Abgeordnete in der erforderlichen Stärke. |
| `gesetzesentwurf-kabinett` | Kabinettsentwurf der Bundesregierung oder Landesregierung aus dem Referentenentwurf nach Ressortabstimmung erstellen. Anwendungsfall Ressortabstimmung und Verbandeanhoerung sind abgeschlossen Kabinettsvorlage muss… |
| `gesetzgebungskompetenz-pruefen` | Gesetzgebungskompetenz nach Art. 70 bis 74 GG prüfen bevor Entwurf aufgesetzt wird. Anwendungsfall Referent oder Verband fragt ob Bund oder Land regelungsbefogt ist. Ausschließliche Bundeskompetenz Art. 71 i.V.m. 73… |
| `goldplating-vermeiden` | Goldplating bei nationaler EU-Richtlinien-Umsetzung identifizieren und bewerten. Anwendungsfall Referentenentwurf setzt EU-Richtlinie um und muss auf ueberschiessende nationale Regelungen über den… |
| `inkrafttreten-uebergangsrecht` | Inkrafttretens- und Übergangsregelung für Gesetze und Verordnungen formulieren. Anwendungsfall Entwurf ist inhaltlich fertig Artikel Inkrafttreten und Übergangsrecht müssen noch ergaenzt werden. Standardformel… |
| `legistik-auftragsaufnahme` | Legistischen Auftrag strukturiert aufnehmen: Startbahn, Bundesland, Ressort, Fraktion, formalen Initiator, Adressaten, Eingriffstiefe, Dringlichkeit, Entwurfstyp und Beteiligte klären. |
| `lesefassung-konsolidiert` | Konsolidierte Lesefassung des geaenderten Stammgesetzes nach Inkrafttreten erstellen. Anwendungsfall Fachreferat Vollzugsbehoerde oder Anwalt will wissen wie das Gesetz nach Änderung aussieht ohne… |
| `normenkartierung` | Alle durch ein legistisches Vorhaben beruehrten Normen kartieren und Änderungsmatrix aufbauen. Anwendungsfall neues Regelungsvorhaben soll vorbereitet werden alle betroffenen Gesetze Verordnungen und Verweisketten… |
| `normenkontrollrat-kmu-check` | Vorlage an Nationalen Normenkontrollrat NKR vorbereiten und KMU-Check durchführen. Anwendungsfall Referentenentwurf muss vor Kabinettsbefassung dem NKR vorgelegt werden. Standard-Kostenmodell SKK Buerokratiekosten.… |
| `normhierarchie-routing` | Richtige Startbahn und Normebene bestimmen: Bundesgesetz, Landesgesetz, Rechtsverordnung, Satzung, Verwaltungsvorschrift, parlamentarischer Antrag oder Entschließungsantrag. |
| `referentenentwurf-bauen` | Vollständigen Referentenentwurf des Bundes oder Landes aufbauen, wenn ein Bundes- oder Landesministerium den Entwurf steuert. Klärt Bundesland, Ressort, GGO oder Landesvorgaben und HdR-/Landesstil. |
| `satzungskompetenz-pruefen` | Satzungskompetenz für Koerperschaften und Anstalten des öffentlichen Rechts prüfen. Anwendungsfall Gemeinde Kammer Hochschule oder Sozialversicherungstraeger will Satzung erlassen und Rechtsgrundlage muss geprüft… |
| `schulung-legistik` | Trainerleitfaden für Legistik-Schulung mit der Arbeitsakte elektronisches Pflichtpostfach. Anwendungsfall Referenten oder Mitarbeiter von Verbanden sollen legistische Kernkompetenz in zwei Tagen Inhouse-Schulung oder… |
| `synopse-erstellen` | Synopse als Dreispalten-Tabelle bisheriges Recht neues Recht Änderungsbefehl erstellen. Anwendungsfall Ressortabstimmung Bundestag oder Bundesrat brauchen vergleichende Darstellung um Änderungen schnell zu erfassen.… |
| `terminologie-konsistenz` | Terminologie-Konsistenz im legistischen Entwurf prüfen und Begriffstabelle aufbauen. Anwendungsfall Entwurf enthaelt neue Legaldefinitionen oder Referent prüft ob Begriffe konsistent verwendet werden und keine… |
| `verbaendeanhoerung-ressortabstimmung` | Verbandeanhoerung und Ressortabstimmung nach GGO steuern und auswerten. Anwendungsfall Referentenentwurf ist fertig und muss Verbaenden und Ressorts zugeleitet werden vor Kabinettsbefassung. Anschreiben Liste zu… |
| `verfassungsmaessigkeit-quercheck` | Querschnittsprüfung Verfassungsmäßigkeit eines Gesetzesentwurfs oder einer Verordnung. Anwendungsfall Entwurf soll vor Ressortabstimmung oder NKR-Vorlage verfassungsrechtlich abgesichert werden oder Verband prüft… |
| `verordnungsermaechtigung-art80` | Verordnungsermaechtigung nach Art. 80 Abs. 1 GG prüfen bevor Rechtsverordnung entworfen wird. Anwendungsfall geplante Rechtsverordnung und Anwalt oder Referent fragt ob Ermaechtigungsgrundlage genuegend bestimmt ist.… |
| `xml-paralleldarstellung` | Maschinenlesbare Paralleldarstellung eines Gesetzesentwurfs in LegalDocML.de oder eNorm-XML erstellen. Anwendungsfall eGesetzgebung BMJ Bundesgesetzblatt online oder automatisierte Weiterverarbeitung erfordert… |
| `zirkelschluss-pruefen` | Zirkelschluesse und kreisfreie Verweisketten im legistischen Entwurf aufspueren. Anwendungsfall Entwurf enthaelt viele Querverweise und soll auf ungewollte Zirkel und tautologische Definitionen geprüft werden. Direkte… |

## Worum geht es?

Die Legistik-Werkstatt ist ein Plugin für Referentinnen und Referenten in Bundesministerien und Landesministerien, für Bundestags- und Landtagsfraktionen, für Oppositionsarbeit, Ausschussarbeit, kommunale und kammerliche Normgeber, Verfassungsrechtlerinnen und Verfassungsrechtler sowie für fachlich zuliefernde Verbände. Sie hilft, Gesetzesentwürfe, Änderungsanträge, Entschließungsanträge, Rechtsverordnungen und Satzungen zu erstellen, zu prüfen und in den jeweils passenden Regierungs- oder Parlamentsprozess einzubringen.

Das Plugin deckt alle Phasen des Gesetzgebungsverfahrens ab: von der Auftragsaufnahme über den Referentenentwurf, die Ressortabstimmung, Verbandeanhoerungen, die Kabinettsreife, Synopsen und Lesefassungen bis zur XML-Paralleldarstellung. Es enthaelt ausserdem Quercheckmodule für Verfassungsmaessigkeit, Europarechtskonformitaet, Erfuellungsaufwand und Goldplating-Vermeidung.

## Wann brauchen Sie diese Skill?

- Ein Referat im Bundesministerium erstellt einen Referentenentwurf und braucht eine strukturierte Auftragsaufnahme mit Regelungszielen.
- Eine Bundestagsfraktion will einen Gesetzentwurf aus der Mitte des Bundestages oder einen Änderungsantrag zu einer laufenden Drucksache bauen.
- Eine Oppositionsfraktion braucht einen formal tragfähigen Antrag, Entschließungsantrag oder Alternativentwurf mit klarer Begründung und Angriffsfestigkeit.
- Ein Landesministerium oder eine Landtagsfraktion arbeitet in einem bestimmten Bundesland und muss Landesverfassung, Landes-Geschäftsordnung, Landtagsverfahren und Verkündungsregeln sauber mitführen.
- Eine Normenkontrollrats-Vorlage muss fristgerecht vorbereitet und mit einem KMU-Check versehen werden.
- Ein Ministerium will einen bestehenden Entwurf auf Verfassungsmaessigkeit und Europarechtskonformitaet prüfen.
- Eine Rechtsverordnung wird entworfen und die Verordnungsermaechtigung nach Art. 80 GG muss geprueft werden.
- Nach Inkrafttreten soll eine konsolidierte Lesefassung des geaenderten Stammgesetzes erstellt werden.

## Fachbegriffe (kurz erklaert)

- **HdR** — Handbuch der Rechtsfoermlichkeit; Leitfaden des Bundesjustizministeriums für die Formulierung von Rechtstexten.
- **GGO** — Gemeinsame Geschäftsordnung der Bundesministerien; regelt Verfahren und Fristen für die Ressortabstimmung.
- **NKR** — Nationaler Normenkontrollrat; unabhaengiges Gremium, das Erfuellungsaufwand und buerokratische Belastungen prüft.
- **Gesetzentwurf aus der Mitte** — Parlamentarische Gesetzesinitiative, die nicht von der Bundesregierung oder Landesregierung, sondern aus dem Parlament kommt; im Bund typischerweise durch eine Fraktion oder Abgeordnete in der erforderlichen Stärke.
- **Formulierungshilfe** — Fachlicher Zuliefertext, häufig aus einem Ministerium, der formal als parlamentarische Vorlage, Änderungsantrag oder Ausschussfassung weiterverwendet werden kann; formaler Initiator und fachlicher Verfasser sind sauber zu trennen.
- **Goldplating** — Ueberimplementierung von EU-Richtlinien: nationale Zusatzanforderungen über das EU-Mindestmass hinaus.
- **Synopse** — Gegenueberststellung von bisherigem Recht, neuem Recht und Änderungsbefehl in einer Dreispalten-Tabelle.
- **LegalDocML** — Maschinenlesbares XML-Format für deutsche Rechtstexte; Standard des Bundesjustizministeriums.
- **Normenkartierung** — Systematische Erfassung aller durch ein Vorhaben beruehrten Normen und ihrer Änderungsbedarfe.
- **Kabinettsentwurf** — Abgestimmter Regierungsentwurf, der dem Kabinett zur Beschlussfassung vorgelegt wird.

## Rechtsgrundlagen

- Art. 70-74 GG (Gesetzgebungskompetenzen Bund und Länder)
- Art. 80 Abs. 1 GG (Verordnungsermaechtigung)
- Art. 76-78 GG (Gesetzgebungsverfahren im Bund)
- Geschäftsordnung des Deutschen Bundestages, insbesondere Vorlagen aus der Mitte des Bundestages
- Landesverfassungen, Geschäftsordnungen der Landesregierungen und Geschäftsordnungen der Landtage
- GGO (Gemeinsame Geschäftsordnung der Bundesministerien)
- Art. 288 AEUV (Wirkung von EU-Verordnungen und Richtlinien)
- Art. 267 AEUV (Vorabentscheidungsverfahren EuGH)

## Schritt-für-Schritt: Einstieg ins Plugin

1. Startbahn klären: Bundesressort, Bundestag, Landesressort, Landtag oder sonstiger Normgeber.
2. Legistischen Auftrag aufnehmen und Regelungsziele klären (`legistik-auftragsaufnahme`).
3. Normhierarchie und Kompetenzgrundlage bestimmen (`normhierarchie-routing`, `gesetzgebungskompetenz-pruefen`).
4. Geeigneten Entwurfstyp auswaehlen: Referentenentwurf, Kabinettsentwurf, Gesetzentwurf aus der Mitte, Änderungsantrag, Antrag, Rechtsverordnung oder Satzung.
5. Quercheck-Module nutzen: Verfassungsmaessigkeit, Europarecht, Goldplating, Erfuellungsaufwand, Rechtsförmlichkeit und parlamentarische Zulässigkeit.
6. Ressortabstimmung, Verbändeanhörung, parlamentarische Einbringung oder Satzungsbeschluss steuern, dann zur lieferfähigen Fassung führen.

## Skill-Tour (was gibt es hier?)

- `legistik-auftragsaufnahme` — Legistischen Auftrag strukturiert aufnehmen und in Regelungsziele umwandeln.
- `normhierarchie-routing` — Richtige Startbahn und Normebene bestimmen: Regierung, Parlament, Gesetz, Verordnung, Satzung oder Antrag.
- `gesetzgebungskompetenz-pruefen` — Gesetzgebungskompetenz nach Art. 70-74 GG prüfen bevor Entwurf aufgesetzt wird.
- `satzungskompetenz-pruefen` — Satzungskompetenz für Koerperschaften und Anstalten des öffentlichen Rechts prüfen.
- `verordnungsermaechtigung-art80` — Verordnungsermaechtigung nach Art. 80 Abs. 1 GG prüfen bevor Rechtsverordnung entworfen wird.
- `referentenentwurf-bauen` — Vollstaendigen Referentenentwurf des Bundes oder Landes aufbauen.
- `gesetzesentwurf-kabinett` — Kabinettsentwurf nach Ressortabstimmung aus dem Referentenentwurf erstellen.
- `formulierungshilfe-bauen` — Formulierungshilfe, Änderungsantrag, Gesetzentwurf aus der Mitte, Entschließungsantrag oder Antrag für Bundestag und Landtage aufbauen.
- `begruendung-allgemein-und-besonders` — Zweiteilige Begruendung zu Gesetzesentwurf oder Verordnung (Allgemeiner Teil, Besonderer Teil) verfassen.
- `verfassungsmaessigkeit-quercheck` — Querschnittspruefung Verfassungsmaessigkeit eines Gesetzesentwurfs oder einer Verordnung.
- `europarechtskonformitaet` — Gesetzesentwurf oder Verordnung auf Vereinbarkeit mit EU-Recht prüfen.
- `goldplating-vermeiden` — Goldplating bei nationaler EU-Richtlinien-Umsetzung identifizieren und bewerten.
- `folgenabschaetzung-erfuellungsaufwand` — Erfuellungsaufwand für Buerger, Wirtschaft und Verwaltung ermitteln und darstellen.
- `folgenabschaetzung-nachhaltigkeit` — Weitere Folgen und Nachhaltigkeitspruefung für Gesetzesentwurf erstellen.
- `normenkontrollrat-kmu-check` — Vorlage an den NKR vorbereiten und KMU-Check durchfuehren.
- `normenkartierung` — Alle durch ein legistisches Vorhaben beruehrten Normen kartieren und Änderungsmatrix aufbauen.
- `terminologie-konsistenz` — Terminologie-Konsistenz im legistischen Entwurf prüfen und Begriffstabelle aufbauen.
- `zirkelschluss-pruefen` — Zirkelschluesse und kreisfreie Verweisketten im legistischen Entwurf aufspueren.
- `inkrafttreten-uebergangsrecht` — Inkrafttretens- und Uebergangsregelungen für Gesetze und Verordnungen formulieren.
- `verbaendeanhoerung-ressortabstimmung` — Verbandeanhoerung und Ressortabstimmung nach GGO steuern und auswerten.
- `synopse-erstellen` — Synopse als Dreispalten-Tabelle (bisheriges Recht, neues Recht, Änderungsbefehl) erstellen.
- `lesefassung-konsolidiert` — Konsolidierte Lesefassung des geaenderten Stammgesetzes nach Inkrafttreten erstellen.
- `xml-paralleldarstellung` — Maschinenlesbare Paralleldarstellung in LegalDocML.de oder eNorm-XML erstellen.
- `dokumente-rendern-docx-pdf` — Legistische Dokumente als DOCX oder PDF im offiziellen HdR-Layout rendern.
- `schulung-legistik` — Trainerleitfaden für Legistik-Fortbildungen mit der Arbeitsakte erstellen.

## Worauf besonders achten

- Kompetenzgrundlage zuerst: Ohne geklarte Gesetzgebungskompetenz nach Art. 70 ff. GG darf kein Entwurf aufgesetzt werden.
- Startbahn sauber halten: Ministerielle Fachzulieferung, formaler parlamentarischer Initiator und politischer Auftraggeber dürfen nicht vermischt werden.
- Landesmodus ernst nehmen: Ohne Bundesland keine verlässliche Aussage zu Landesverfassung, Landtagsgeschäftsordnung, Kabinettsverfahren und Verkündung.
- Goldplating ist politisch und juristisch heikel: Nationale Mehrbelastungen über EU-Mindestanforderungen hinaus müssen explizit begruendet werden.
- NKR-Fristen sind verbindlich: Vorlage muss mit vollstaendigen Erfuellungsaufwands-Angaben rechtzeitig erfolgen.
- Terminologie-Konsistenz ist elementar: Verschiedene Begriffe für dasselbe Konzept können zu Auslegungsstreitigkeiten fuehren.
- Uebergangsrecht nicht vergessen: Altfallregelungen und Bestandsschutz sichern Rechtsicherheit und vermeiden Verfassungsruegen.

## Typische Fehler

- Referentenentwurf ohne Verfassungsmaessigkeits-Check: Entwurf wird in der Ressortabstimmung oder im Parlament wegen Grundrechtsverletzung zurueckgewiesen.
- Bundestags- oder Landtagsinitiative ohne klaren formalen Initiator: Der Text ist fachlich brauchbar, aber nicht einreichungsfähig.
- Landesentwurf nach Bundes-Schablone: Landeszuständigkeiten, Zitierregeln, Verkündungsblatt oder Landtagsformat werden falsch.
- Verordnungsermaechtigung zu unbestimmt: Art. 80 Abs. 1 GG verlangt Inhalt, Zweck und Ausmass — Blankoermaechtigung ist nichtig.
- Goldplating unerkannt: Nationale Umsetzung geht über die Richtlinienpflichten hinaus, ohne dass dies im Entwurf kenntlich gemacht wird.
- Synopse fehlt: Ressortabstimmung und parlamentarische Beratung werden durch fehlende Gegenueberststellung ernsthaft erschwert.
- Inkrafttreten ohne Uebergangsrecht: Adressaten können sich nicht rechtzeitig auf neue Pflichten einstellen.

## Quellen und Aktualitaet

- Stand: 05/2026
- GG (Grundgesetz) in der zum Stand-Datum geltenden Fassung
- GGO (Gemeinsame Geschäftsordnung der Bundesministerien) in der geltenden Fassung
- HdR (Handbuch der Rechtsfoermlichkeit) 3. Auflage des Bundesjustizministeriums
- Geschäftsordnung des Deutschen Bundestages und einschlägige Landtags-Geschäftsordnungen jeweils aktuell prüfen

---

## Skill: `legistik-erstpruefung-und-mandatsziel`

_Legistik: Erstprüfung, Rollenklärung und Mandatsziel._

# Legistik: Erstprüfung, Rollenklärung und Mandatsziel

## Aktenstart statt Formularstart

Wenn zu **Legistik Erstpruefung Und Mandatsziel** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Legistik Werkstatt** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Normenanker

Arbeitsfokus: **Legistik: Erstprüfung, Rollenklärung und Mandatsziel**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 20 Abs. 3 GG` — Gesetzesbindung.
- `Art. 76 Abs. 1 GG` — Gesetzesinitiative.
- `Art. 77 Abs. 1 GG` — Gesetzesbeschluss.
- `Art. 80 Abs. 1 GG` — Verordnungsermächtigung.
- `Art. 84 Abs. 1 GG` — Verwaltungsvollzug.
- `§ 42 Abs. 1 GGO` — Gesetzgebungsvorhaben.
- `§ 43 Abs. 1 GGO` — Ressortabstimmung.
- `§ 44 Abs. 1 GGO` — Gesetzesfolgen.
- `§ 45 GGO` — Beteiligung.
- `§ 46 GGO` — Rechtsförmlichkeit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GGO Ressortbeteiligung i.d.R. 4 Wochen, NKR-Stellungnahme 4 Wochen, Bundesrat 1. Durchgang 6 Wochen / 9 Wochen, Vermittlungsausschuss nach Bedarf.
- Tragende Normen verifizieren: GGO §§ 40-49 (Rechtsetzungsverfahren), Handbuch der Rechtsförmlichkeit (BMJ), NKR-Gesetz, BGleiG, IT-Konsolidierungs-Konzept, eNorm-Standard, GG Art. 76, 77, 78 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Ressort (BMJ und Fachressort), Bundeskanzleramt, Bundesrat, NKR, Bundestagsausschüsse, Bundesregierung, Wissenschaftliche Dienste, Lobbyregister.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Referentenentwurf, BT-Drucksache, Gesetzesfolgenabschätzung, NKR-Stellungnahme, Verbändeanhörungs-Stellungnahme, Synopse, Erfüllungsaufwandsberechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen: Legistik: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** XML.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Legistik** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `begruendung-allgemein-und-besonders`

_Zweiteilige Begründung zu einem Gesetzesentwurf oder einer Verordnung verfassen. Anwendungsfall Referentenentwurf oder Kabinettsentwurf ist fertig und Begründung muss nach HdR-Schema aufgebaut werden. Allgemeiner Teil A Anlass und Ziel B wesentlicher Inhalt C Alternativen D Erfuellungsaufwand E w..._

# Begründung allgemein und besonders

> Eine gute Begründung erleichtert Auslegung und Vollzug, eine schlechte führt zu Streit.

## Aufbau

### Teil A - Allgemeiner Teil

#### A.I. Zielsetzung und Notwendigkeit der Regelungen

Was soll erreicht werden? Warum ist eine Regelung erforderlich?

#### A.II. Wesentlicher Inhalt des Entwurfs

In zehn bis zwanzig Sätzen den Kern des Entwurfs darstellen.

#### A.III. Alternativen

Welche Alternativen wurden erwogen, warum verworfen?

#### A.IV. Gesetzgebungskompetenz

Verweis auf Art. 70 ff. GG bzw. Landeskompetenz. Erforderlichkeitsklausel Art. 72 Abs. 2 GG, falls einschlaegig.

#### A.V. Vereinbarkeit mit dem Recht der Europaeischen Union und mit völkerrechtlichen Verträgen

Bezug zu Primärrecht (EUV / AEUV / Charta), Sekundärrecht (RL / VO), EuGH-Rechtsprechung. Notifizierungspflicht 2015/1535?

#### A.VI. Gesetzesfolgen

- A.VI.1. Rechts- und Verwaltungsvereinfachung
- A.VI.2. Nachhaltigkeitsaspekte (SDG-Bezug)
- A.VI.3. Haushaltsausgaben ohne Erfüllungsaufwand
- A.VI.4. Erfüllungsaufwand (Bürger / Wirtschaft / Verwaltung)
- A.VI.5. Weitere Kosten
- A.VI.6. Weitere Gesetzesfolgen (gleichstellungspolitisch, demografisch, geschlechtsspezifisch, oekologisch)

#### A.VII. Befristung, Evaluierung

#### A.VIII. Vereinbarkeit mit den Zielen des Klimaschutzgesetzes

### Teil B - Besonderer Teil

Pro Artikel und pro Paragraf:

- Was wird geändert?
- Warum?
- Wie ist die Änderung zu verstehen (Auslegungshinweise)?
- Welche bestehende Rechtsprechung war Hintergrund?
- Welche Auslegungsfragen sind absehbar?

**Beispiel - Zu Artikel 1 Nummer 2 (Paragraf 33a HGB - neu):**

"Mit Paragraf 33a HGB wird die Pflicht zur Vorhaltung eines elektronischen Pflichtpostfachs eingeführt. Adressaten sind alle im Handelsregister eingetragenen Unternehmen sowie Unternehmen, die nach Artikel 33 DSA als sehr große Online-Plattform (VLOP) oder sehr große Online-Suchmaschine (VLOSE) eingestuft sind. Die Norm konkretisiert die seit der ZPO-Reform 2024 bestehenden Zustellverpflichtungen. ... Die Auswahl der Adressaten über den DSA-Schwellenwert von 45 Millionen Nutzern stellt sicher, dass die Pflicht keine kleinen und mittleren Unternehmen überraschend trifft. ..."

## Stilfragen

- Vergangenheitsform vermeiden, Praesens verwenden
- Keine politischen Bewertungen ("ist dringend notwendig"), nur sachliche Begründung
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine überfluessigen Floskeln

## Prüfliste

- [ ] Teil A.I bis A.VIII vollständig
- [ ] Teil B für jeden geänderten Paragrafen
- [ ] Rechtsprechung zitiert wo passend
- [ ] Erfüllungsaufwand mit Zahlen
- [ ] EU-Bezug und Notifizierung adressiert

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§ 39 VwVfG (Begruendungspflicht Verwaltungsakt) — § 41 VwVfG (Heilung von Begruendungsmaengeln) — § 76 GGO (Begruendung Referentenentwurf) — §§ 1-4 UVPG (Umwelt-Begruendungspflichten) — § 35 BauGB (Begruendung Abwaegungsergebnis Bauleitplanung)

## Ausgabe

Markdown-Datei "Begruendung.md".

## Anschluss

`synopse-erstellen`.

---

## Skill: `bundestag-fristen-form-zustaendigkeit`

_Bundestag: Fristen, Form, Zuständigkeit und Rechtsweg im Legistik (Gesetzgebungstechnik): 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist..._

# Bundestag: Fristen, Form, Zuständigkeit und Rechtsweg

## Normenanker

Arbeitsfokus: **Bundestag: Fristen, Form, Zuständigkeit und Rechtsweg**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 5 Abs. 1 DSGVO` — Datenschutzgrundsätze.
- `Art. 6 Abs. 1 DSGVO` — Rechtsgrundlage.
- `Art. 22 DSGVO` — automatisierte Entscheidungen.
- `Art. 35 DSGVO` — Datenschutz-Folgenabschätzung.
- `§ 3 OZG` — Nutzerkonten/Portalverbund live prüfen.
- `§ 5 EGovG` — elektronische Aktenführung live prüfen.
- `Art. 3 KI-VO` — Begriffe.
- `Art. 6 KI-VO` — Hochrisiko-Systeme.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Bundestag: Fristen, Form, Zuständigkeit und Rechtsweg
- **Normen-/Quellenanker:** XML.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Bundestag** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `dokumente-rendern-docx-pdf`

_Legistische Dokumente als DOCX oder PDF im offiziellen Erscheinungsbild der Bundesregierung, des Bundestages, eines Landes oder eines Landtags rendern. Anwendungsfall fertiger Entwurf soll als lieferfähiges Dokument nach Handbuch der Rechtsfoermlichkeit HdR oder landesspezifischem Format ausgegeb..._

# Dokumente rendern - DOCX und PDF im offiziellen HdR-Layout

## Normenanker

Arbeitsfokus: **Dokumente rendern - DOCX und PDF im offiziellen HdR-Layout**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 20 Abs. 3 GG` — Gesetzesbindung.
- `Art. 76 Abs. 1 GG` — Gesetzesinitiative.
- `Art. 77 Abs. 1 GG` — Gesetzesbeschluss.
- `Art. 80 Abs. 1 GG` — Verordnungsermächtigung.
- `Art. 84 Abs. 1 GG` — Verwaltungsvollzug.
- `§ 42 Abs. 1 GGO` — Gesetzgebungsvorhaben.
- `§ 43 Abs. 1 GGO` — Ressortabstimmung.
- `§ 44 Abs. 1 GGO` — Gesetzesfolgen.
- `§ 45 GGO` — Beteiligung.
- `§ 46 GGO` — Rechtsförmlichkeit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Wann verwenden

Dieser Skill wird **am Ende** des Legistik-Workflows aufgerufen, wenn aus den strukturierten Markdown-Bausteinen der vorgelagerten Skills (Auftrag, Normentext, Begründung, Synopse) ein **lieferfähiges Dokument** im offiziellen Erscheinungsbild erstellt werden soll.

Vier Hauptformate:

1. **Referentenentwurf** (ministeriell, serifenlos Arial 11pt, "der Bundesregierung" im Kopf, Bearbeitungsstand-Hinweis, A-F-Vorblatt, Artikelgesetz, Begründung Teil A und B)
2. **Gesetzesentwurf der Bundesregierung** (BT-Drucksachen-Look, Times New Roman 11pt, "Drucksache XX/YYYY", "Deutscher Bundestag - XX. Wahlperiode", Sperrsatz-Überschriften, Anschreiben des Bundeskanzlers)
3. **Parlamentarische Vorlage** (Gesetzentwurf aus der Mitte, Änderungsantrag, Antrag oder Entschließungsantrag; BT- oder Landtagsformat nach Verfahrensstand)
4. **Formulierungshilfe** (fachliche Zulieferung, kuerzer, ohne Drucksachen-Mantel, eingerueckter Änderungstext)

Plus Hilfsformate:

5. **Spaltensynopse** dreispaltig (geltend / Änderung / Begründung)
6. **Lesefassung konsolidiert** (Artikelgesetz nach Inkrafttreten)
7. **Kabinettsmappe-Deckblatt**

## Layout-Eckdaten nach Handbuch der Rechtsförmlichkeit

### Referentenentwurf (ministerieller Hausstil)

- Schrift: **Arial 11pt** (serifenlos)
- Zeilenabstand 1.15
- Rand: links 2.5 cm, rechts 2.0 cm, oben/unten 2.0 cm
- Seitenkopf: zentriert `- N -` (Seitennummer in Gedankenstrichen)
- Fußzeile: leer oder Bearbeitungsstand-Datum
- Kopfzeile Seite 1: rechtsbuendig "Bearbeitungsstand: TT.MM.JJJJ HH:MM"
- Titel zentriert fett: "Referentenentwurf"
- Untertitel zentriert: "des Bundesministeriums für ..."
- Haupttitel zentriert fett: "Entwurf eines Gesetzes zur ..."
- Kurztitel in Klammern: "(Kurzbezeichnung - Abkürzung)"
- Datumsplatzhalter "Vom ..."

### BT-Drucksachen-Layout (Gesetzentwurf der Bundesregierung)

- Schrift: **Times New Roman 11pt** (Serife)
- Zeilenabstand 1.15
- Seitenkopf wechselnd (gerade/ungerade): links/rechts "Drucksache XX/YYYY" bzw. "Deutscher Bundestag - XX. Wahlperiode", Mitte `- N -`
- Sperrsatz für Hauptüberschriften: `I n h a l t s u e b e r s i c h t`
- Anschreiben Bundeskanzler in Briefkopf-Format
- Anlagen: Begründung (Anlage 1), Stellungnahme NKR (Anlage 2), Stellungnahme Bundesrat (Anlage 3), Gegenaeusserung (Anlage 4)

### Gemeinsame Strukturen

- Vorblatt: A. Problem und Ziel - B. Lösung - C. Alternativen - D. Haushaltsausgaben ohne Erfüllungsaufwand - E. Erfüllungsaufwand (E.1 Bürger - E.2 Wirtschaft - E.3 Verwaltung) - F. Weitere Kosten
- Artikelgesetz: "Artikel 1 (Änderung des XYZ-Gesetzes)" fett, Einleitungssatz mit Stammgesetz + letzte Änderung BGBl-Fundstelle
- Gliederungsebenen: 1. / 2. / 3. -> a) b) c) -> aa) bb) cc) -> aaa) bbb) ccc)
- Änderungsbefehle: Anführungszeichen kursiv: *"... wird durch ... ersetzt"*
- Absatzbezeichnung in Klammern: (1), (2), (3)
- Begründung Teil A (Allgemeiner Teil) Roemisch I-VII: I. Zielsetzung und Notwendigkeit - II. Wesentlicher Inhalt - III. Alternativen - IV. Gesetzgebungskompetenz - V. Vereinbarkeit mit EU-Recht - VI. Gesetzesfolgen - VII. Befristung und Evaluierung
- Begründung Teil B (Besonderer Teil): "Zu Artikel X" - "Zu Nummer Y" - "Zu Buchstabe Z"

## Eingabeschema

Der Eingabeordner enthält:

```
projekt/
 metadaten.yaml # Titel, Kurztitel, Federfuehrung, Bearbeitungsstand, Drucksachennummer, Wahlperiode
 vorblatt.md # A bis F mit den ueblichen Abschnitten
 gesetzestext.md # Artikel 1 ... Artikel N (Inkrafttreten)
 begruendung-a.md # I bis VII
 begruendung-b.md # Zu Artikel X / Zu Nummer Y
 synopse.csv # Spalten: geltend | aenderung | begruendung
 anlagen/ # NKR, Bundesrat, Gegenaeusserung (optional, als md)
```

## Beispielaufruf

```bash
python3 skills/dokumente-rendern-docx-pdf/assets/render.py \
 --format referentenentwurf \
 --eingabe testakten/legistik-pflichtpostfach/ \
 --ausgabe testakten/legistik-pflichtpostfach/output/
```

Ausgabe: `Referentenentwurf-Pflichtpostfachgesetz.docx` (und `.pdf` wenn `soffice` installiert).

## Qualitätsprüfung vor Abgabe

- Schriftart und -groesse korrekt
- Sperrsatz nur für Hauptüberschriften ("Inhaltsübersicht", "Begründung")
- Änderungsbefehle durchgaengig kursiv und in Anführungszeichen
- Vorblatt vollständig A-F
- Begründung Teil A vollständig I-VII
- Kopf-/Fußzeile auf jeder Seite
- Keine überschießenden Begriffe in der Sache (Goldplating siehe Skill goldplating-vermeiden)
- Keine Mehrwert-Steuer-Komma-Zahlen im Fliesstext - immer Punkt verwenden oder ausschreiben

## Verwandte Skills

- `referentenentwurf-bauen` - liefert die Markdown-Bausteine für das Vorblatt und den Artikeltext
- `gesetzesentwurf-kabinett` - liefert die Kabinettsmappe als zusätzliches Deckblatt
- `formulierungshilfe-bauen` - liefert Formulierungshilfe, Änderungsantrag, Gesetzentwurf aus der Mitte, Antrag oder Entschließungsantrag
- `synopse-erstellen` - liefert die dreispaltige CSV für die Synopse
- `begruendung-allgemein-und-besonders` - liefert die Begründung Teil A und Teil B

## Technische Standards & Qualitätsanforderungen

- DOCX ist Arbeits- und Austauschformat; PDF ist Liefer- und Lesefassung. Wenn ein bestimmtes Portal, Parlament oder Haus eine andere Vorgabe macht, geht diese vor.
- Für Bundesentwürfe HdR, GGO und Vorgaben der E-Gesetzgebung beachten; für Länder die jeweilige Landesvorlage, Landtagsvorgaben und Verkündungsregeln abfragen.
- Bei PDF-Ausgabe Sichtprüfung durchführen: Seitenköpfe, Drucksachennummer, Wahlperiode, Sperrsatz, Seitenumbruch, Tabellenbreiten, Fußnoten und Anlagenverzeichnis.
- Keine gerichtlichen ERVV-Anforderungen ungeprüft auf Gesetzgebungsdokumente übertragen. Nur verwenden, wenn der konkrete Abgabeweg tatsächlich elektronischer Rechtsverkehr ist.
- Bei Archiv- oder Veröffentlichungsanforderungen prüfen, ob PDF/A, Barrierefreiheit, maschinenlesbare XML-Fassung oder zusätzliche Metadaten verlangt sind.

## Zentrale Normen und Standards

HdR — GGO — Art. 76-78 GG — GO-BT oder Landtags-GO — Landesverfassung und Verkündungsrecht — LegalDocML.de/eNorm soweit gefordert — PDF/A-Standard ISO 19005 nur bei konkreter Archivvorgabe

---

## Skill: `folgenabschaetzung-erfuellungsaufwand`

_Erfuellungsaufwand für Buerger Wirtschaft und Verwaltung ermitteln und darstellen. Anwendungsfall Referentenentwurf soll NKR-konformes Vorblatt und Begründung erhalten oder NKR verlangt Nachbesserung. Methodik Leitfaden BMJ BMI Statistisches Bundesamt Fallzahlen Bearbeitungszeit Lohnsatz. Pro Vor..._

# Folgenabschätzung - Erfüllungsaufwand

## Normenanker

Arbeitsfokus: **Folgenabschätzung - Erfüllungsaufwand**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 44 Abs. 1 GGO` — Darstellung der Gesetzesfolgen.
- `§ 44 Abs. 4 GGO` — Erfüllungsaufwand.
- `§ 45 GGO` — Beteiligung betroffener Kreise.
- `§ 46 GGO` — Rechtsförmlichkeit.
- `Art. 20 Abs. 3 GG` — Rechtsbindung.
- `Art. 80 Abs. 1 GG` — Bestimmtheit bei Verordnungsermächtigungen.
- `§ 7 Abs. 1 BHO` — Wirtschaftlichkeit bei Vollzugskosten.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Methodik

Leitfaden zur Ermittlung und Darstellung des Erfüllungsaufwands (BMJ / BMI / DESTATIS, Stand laufend aktualisiert).

## Drei Adressaten

### Bürger
Aufwand: Lese-, Antrags-, Beleg-Pflichten. Bemessung: Zeitkosten (oft 28 EUR/h Standard).

### Wirtschaft
Aufwand: betriebliche Umsetzung, IT-Anpassung, Dokumentation, Prüfung. Bemessung: Lohnkosten plus Sachkosten plus einmalige Umstellungskosten.

### Verwaltung
Aufwand: Personal, IT, Sachmittel. Bemessung: Vollkostenrechnung des Bundes / Landes / Gemeinde.

## Ermittlung

1. **Fallzahlen ermitteln**: wie viele Adressaten? Wie oft pro Jahr?
2. **Pro Fall Bearbeitungszeit**: in Minuten oder Stunden
3. **Lohnsatz**: nach DESTATIS oder geschätzt
4. **Multiplikation**

Beispiel:

| Vorschrift | Adressat | Fallzahl/Jahr | Bearbeitungszeit | Lohnsatz | Erfüllungsaufwand/Jahr |
|---|---|---|---|---|---|
| Paragraf 33a HGB neu | Unternehmen | 1.4 Mio | 30 min/Fall einmalig | 41 EUR/h | 28.7 Mio EUR (einmalig) |
| Paragraf 33a HGB neu | Unternehmen | 1.4 Mio | 5 min/Jahr | 41 EUR/h | 4.8 Mio EUR p.a. |

## Bagatellschwelle

Wenn Erfüllungsaufwand unter 1 Mio EUR p.a. - in der Regel "kein nennenswerter Aufwand". Dennoch dokumentieren.

## KMU-Prüfung

Wenn KMU betroffen: Prüfung Verhältnismaessigkeit. Ggf. Schwellenwerte einführen, ggf. Übergangsregelungen, ggf. Ausnahmen.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 44a, 62 GGO (Erfuellungsaufwand-Berechnung, Folgenabschaetzung) — §§ 1-4 SKMBericht (Statistisches Bundesamt, Standardkosten-Modell) — Art. 5 Abs. 4 EUV (EU-Verhältnismäßigkeit) — § 39a VwVfG (Vorwegbegruendung bei Massenverfahren)

## Ausgabe

Tabelle plus Beschreibung in Vorblatt-Abschnitt E und in Begründung-Abschnitt A.VI.4.

## Anschluss

`folgenabschaetzung-nachhaltigkeit`, `normenkontrollrat-kmu-check`.

---

## Skill: `folgenabschaetzung-nachhaltigkeit`

_Weitere Folgen und Nachhaltigkeitsprüfung für Gesetzesentwurf erstellen. Anwendungsfall Referentenentwurf benoetigt Vorblatt Abschnitt G und Begründung A.VI.6 zu Nachhaltigkeitsfolgen. UN-SDGs prüfen welche betroffen Bewertung positiv neutral negativ. Demografiecheck Wirkung auf aeltere Buerger F..._

# Folgenabschätzung - Nachhaltigkeit

> Was bewirkt das Vorhaben jenseits des unmittelbaren Regelungsziels?

## Prüfdimensionen

### A - Nachhaltigkeit nach UN-SDG

17 Sustainable Development Goals der UN, Resolution 70/1 von 2015. Pro Vorhaben Prüfung:

- SDG 1 Keine Armut - betroffen ja/nein, positiv/negativ
- SDG 3 Gesundheit
- SDG 4 Bildung
- SDG 5 Geschlechtergleichheit
- SDG 8 Würdige Arbeit
- SDG 10 Weniger Ungleichheit
- SDG 13 Klimaschutz
- SDG 16 Frieden, Gerechtigkeit, starke Institutionen

### B - Demografiecheck

- aeltere Bürger
- Kinder und Jugendliche
- Familien
- Single-Haushalte

### C - Gleichstellungspolitischer Check

- Wirkung auf Frauen vs. Männer
- Care-Arbeit
- Equal Pay
- Gewaltschutz

### D - Klimacheck

Klimaschutzgesetz Paragraf 13. Wirkung auf Treibhausgasemissionen direkt und indirekt.

### E - Soziale Folgen

- Inklusion behinderte Menschen
- Migration / Integration
- Armut / Wohnungslosigkeit

### F - Wirkung auf laendliche Räume

- gleichwertige Lebensverhältnisse Art. 72 Abs. 2 GG

### G - Wirkung auf KMU

(Querverweis `normenkontrollrat-kmu-check`)

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 3-6 UVPG (Umweltvertraeglichkeitspruefung) — Art. 20a GG (Staatsziel Umweltschutz) — §§ 4-6 KSG (Klimaschutzziele, Sektorziele) — DNK Deutsche Nachhaltigkeitsstrategie — § 65 GGO (Nachhaltigkeitspruefung in Begruendung)

## Ausgabe

Folgenmatrix als Tabelle plus Text für Vorblatt G und Begründung A.VI.6.

## Anschluss

`inkrafttreten-uebergangsrecht`.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

