# Megaprompt: einfache-leichte-sprache-jura

> *Achtung: Dies ist ein experimentelles Mega-Prompt-Markdown, das einen kompletten Klotzkette-Plugin in eine einzige Datei zusammenfuehrt. Keine Haftung, keine Gewaehr. Nur zum Ausprobieren der Skills auch ohne Claude Code; keine Rechtsberatung. Vor Verwendung im Mandat anwaltlich pruefen.*
>
> *Caution: This is an experimental Mega-Prompt Markdown that consolidates a full Klotzkette plugin into a single file. No warranty, no liability. For exploration with chat tools that do not run Claude Code only; not legal advice.*

**Verwendung:** Diesen gesamten Text in einen Chat ohne Claude-Code-Integration einfuegen (oder als Datei hochladen). Der Chat-Agent erhaelt damit die gebuendelten Skills dieses Plugins als Kontext. Eine Replikation des vollen Plugin-Verhaltens ist nicht garantiert — der Megaprompt ist eine Best-Effort-Kompression.


## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 83 Skills des Plugins `einfache-leichte-sprache-jura`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Einfache/Leichte Sprache Jura: ordnet Rolle (Adressat mit Lese-/Lernbeeinträchtigung, A…
2. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting im Einfache Leichte Sprache Jura-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen,…
3. **bauen-fristennotiz-naechster-schritt** — Bauen: Fristennotiz und nächster Schritt im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Pers…
4. **einfache-sprache** — Kanzlei oder Behörde will juristischen Text für normale Buerger verstaendlich machen: Einfache Sprache B1-Niveau zielgru…
5. **experimentelle-schriftsatz-brief-memo-bausteine** — Experimentelle: Schriftsatz-, Brief- und Memo-Bausteine im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat di…
6. **familienrecht-erstgespraech-juristische** — Familienrecht Erstgespraech in Einfacher Sprache: Trennung, Scheidung, Unterhalt, Sorgerecht, Umgang. Vorlage Memo für d…
7. **fristen-form-zustaendigkeit-rechtsweg** — Einfache: Fristen, Form, Zuständigkeit und Rechtsweg im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die f…
8. **glossar-sonderfall-edge-case** — Glossar: Sonderfall und Edge-Case-Prüfung im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Per…
9. **jura-mandantenkommunikation** — Jura: Mandantenkommunikation und Entscheidungsvorlage im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die …
10. **juristische-erstpruefung-rollenklaerung** — Juristische: Erstprüfung, Rollenklärung und Mandatsziel im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat di…
11. **juristische-sicherung** — Beim Vereinfachen juristischer Texte darf kein Rechtsinhalt verloren gehen: Rechte Pflichten Fristen Betraege Rechtsfolg…
12. **juristisches-beweislast-darlegungslast** — Juristisches: Beweislast, Darlegungslast und Substantiierung im Einfache und leichte Sprache im Recht: 1. Welche Rolle h…
13. **kommandocenter** — Kanzlei oder Behörde startet Vereinfachungs-Projekt für juristischen Text: Zielgruppe Modus Rechtsinhalt-Erfassung Workf…
14. **ls-juristisches-glossar-justizportal-pruefen** — Juristisches Glossar für Einfache und Leichte Sprache aufbauen: Schlagwort, Schwerverstaendliche Definition, Variante Ei…
15. **rechtsinhalt-interessen** — Rechtsinhalt: Mehrparteienkonflikt und Interessenmatrix im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat di…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Einfache/Leichte Sprache Jura: ordnet Rolle (Adressat mit Lese-/Lernbeeinträchtigung, Anwalt/Behörde, Übersetzer), markiert Frist (keine harten Fristen), wählt Norm (BGG § 11 Leichte Sprache, UN-BRK Art. 9/21, BFSG) und Zuständigkeit (Behörden mit Verständlichkeit..._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Einfache Leichte Sprache Jura** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `annaeherung-quellenkarte` — Annaeherung Quellenkarte
- `aufenthaltsrecht-mandant` — Aufenthaltsrecht Mandant
- `aufenthaltsrecht-mandant-betreuung` — Aufenthaltsrecht Mandant Betreuung
- `bauen-fristennotiz-naechster-schritt` — Bauen Fristennotiz Naechster Schritt
- `bauen-fristennotiz-und-naechster-schritt` — Bauen Fristennotiz und Naechster Schritt
- `bescheidmodus` — Bescheidmodus
- `bescheidmodus-02` — Bescheidmodus 02
- `betreuung-vormundschaft` — Betreuung Vormundschaft
- `chronologie-und-belegmatrix` — Chronologie und Belegmatrix
- `einfache-sprache` — Einfache Sprache
- `experimentelle-glossar-sonderfall-jura` — Experimentelle Glossar Sonderfall Jura
- `experimentelle-schriftsatz-brief-memo-bausteine` — Experimentelle Schriftsatz Brief Memo Bausteine
- `familienrecht-erstgespraech` — Familienrecht Erstgespraech
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Einfache Leichte Sprache Jura sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Normen & Rechtsprechung

Konkret zu prüfen:

- § 11 SGB I (Verständlichkeit)
- BGG (Behindertengleichstellungsgesetz) § 11
- BITV 2.0 (Barrierefreie Informationstechnik-Verordnung)
- UN-BRK Art. 9, 21

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting im Einfache Leichte Sprache Jura-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill e_

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Einfache Leichte Sprache Jura** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Einfache Leichte Sprache Jura**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Juristische Texte in Einfache Sprache oder Leichte Sprache übertragen: experimentelle Standard-Annäherung, Zielgruppe klären, Rechtsinhalt sichern und Qualitätsgate nutzen.

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
| `elsj-einfache-sprache` | Kanzlei oder Behörde will juristischen Text für normale Buerger verstaendlich machen: Einfache Sprache B1-Niveau zielgruppenorientiert klare Gliederung erklärte Rechtsbegriffe gesicherte Fristen. Normen BGG § 11… |
| `elsj-juristische-sicherung` | Beim Vereinfachen juristischer Texte darf kein Rechtsinhalt verloren gehen: Rechte Pflichten Fristen Betraege Rechtsfolgen Ausnahmen. Normen §§ 133 157 BGB Auslegungspflicht. Prüfraster Rechte-Vollständigkeit… |
| `elsj-kommandocenter` | Kanzlei oder Behörde startet Vereinfachungs-Projekt für juristischen Text: Zielgruppe Modus Rechtsinhalt-Erfassung Workflow-Steuerung Ausgabe. Normen BGG BITV 2.0. Prüfraster Zielgruppen-Identifikation Modus-Auswahl… |
| `elsj-leichte-sprache` | Kanzlei oder Behörde will juristischen Text für Menschen mit Lernschwierigkeiten oder kognitiven Einschraenkungen aufbereiten: Leichte Sprache nach Netzwerk Leichte Sprache A2-Niveau kurze Saetze klare Zeilenstruktur… |
| `elsj-qualitaetsgate` | Fertig erstellte Fassung in Einfacher Sprache oder Leichter Sprache vor Veröffentlichung prüfen. Verstaendlichkeit Gliederung Glossar Zielgruppenpassung juristische Vollständigkeit offene Nutzergruppen-Prüfung. Normen… |

## Worum geht es?

Juristische Texte — Bescheide, Vertraege, Urteile, Merkblaetter — sind für viele Buergerinnen und Buerger schwer verstaendlich. Dieses Plugin unterstuetzt Kanzleien und Behörden dabei, solche Texte in Einfache Sprache (Zielniveau B1) oder Leichte Sprache (Zielniveau A2 gemaess BITV 2.0) zu uebertragen, ohne dabei Rechtsinhalt, Fristen oder Rechtswirkungen zu verlieren.

Das Plugin unterscheidet strikt zwischen Verstaendlichkeit und inhaltlicher Absicherung: Vereinfachungen muessen stets gegen das Original geprueft werden. Das Qualitaetsgate am Ende des Workflows sichert die Konformitaet vor Veroeffentlichung.

## Wann brauchen Sie diese Skill?

- Eine Behörde will Bescheide oder Widerspruchsbeschluesse für Buerger mit eingeschraenkter Lesekompetenz aufbereiten.
- Eine Kanzlei erklaert Mandanten verstaendlich, welche Rechte und Pflichten ein Vertrag begruendet.
- Ein Unternehmen muss seine Datenschutzerklaerung barrierefrei gestalten (BITV 2.0, WCAG 2.1).
- Ein Pflegeheim oder eine Sozialeinrichtung will Heimvertraege in Leichte Sprache uebersetzen.
- Ein Verband prueft, ob sein oeffentlich zugaengliches Rechtsmerkblatt verstaendlich genug ist.

## Fachbegriffe (kurz erklaert)

- **Einfache Sprache** — Schriftsprachliche Vereinfachung auf ca. Niveau B1 des Europaeischen Referenzrahmens; kurze Saetze, gebraeuchliche Woerter, aktive Formulierungen.
- **Leichte Sprache** — Stark vereinfachte Sprache auf Niveau A2 nach BITV 2.0 und dem Regelwerk des Netzwerks Leichte Sprache; standardisierte Regeln zu Wortlaenge, Satzstruktur und Bildunterstuetzung.
- **BITV 2.0** — Barrierefreie-Informationstechnik-Verordnung; verpflichtet öffentliche Stellen zur barrierefreien Gestaltung digitaler Angebote einschliesslich Leichter Sprache.
- **Rechtsinhalt-Sicherung** — Pruefung, dass nach der Vereinfachung keine Rechte, Pflichten, Fristen oder Rechtsfolgen verloren gegangen sind.
- **Qualitaetsgate** — Abschlusspruefung vor Veroeffentlichung: Verstaendlichkeit, Gleichgewicht zum Original, Glossar-Konsistenz, Barrierefreiheit.
- **Zielgruppe** — Definierte Personengruppe (z. B. Menschen mit Lernschwierigkeiten, Buerger ohne Rechtskenntnisse), nach der Schwierigkeitsgrad und Modus gewaehlt werden.

## Rechtsgrundlagen

- § 11 BGG (Barrierefreiheitsgebot öffentlicher Stellen)
- BITV 2.0 — Barrierefreie-Informationstechnik-Verordnung
- § 3 BMAS-Richtlinie zu Leichter Sprache in Behörden
- Art. 7 Abs. 2 DSGVO (Anforderungen an Einwilligungserklaerungen in verstaendlicher Sprache)
- § 305 Abs. 2 BGB (Einbeziehungsvoraussetzungen für AGB — Deutlichkeitsgebot)

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Wer ist die Zielgruppe des vereinfachten Textes?
2. Modus festlegen: Einfache Sprache (B1) oder Leichte Sprache (A2)?
3. Rechtsinhalt erfassen: Alle relevanten Rechte, Pflichten, Fristen und Rechtsfolgen des Originaltexts sichern (Skill `elsj-juristische-sicherung`).
4. Vereinfachung erstellen: Passenden Skill waehlen (`elsj-einfache-sprache` oder `elsj-leichte-sprache`).
5. Qualitaetsgate durchlaufen: Fertige Fassung vor Veroeffentlichung pruefen (`elsj-qualitaetsgate`).

## Skill-Tour (was gibt es hier?)

- `elsj-kommandocenter` — Navigationszentrum: Zielgruppe und Modus klaeren, starten, alle Skills koordinieren.
- `elsj-einfache-sprache` — Juristischen Text auf Einfache Sprache Niveau B1 uebertragen für Buerger ohne Fachkenntnisse.
- `elsj-leichte-sprache` — Juristischen Text auf Leichte Sprache Niveau A2 uebertragen für Menschen mit Lernschwierigkeiten oder kognitiven Einschraenkungen.
- `elsj-juristische-sicherung` — Sicherstellt, dass kein Rechtsinhalt (Rechte, Pflichten, Fristen, Betraege, Rechtsfolgen) bei der Vereinfachung verloren geht.
- `elsj-qualitaetsgate` — Abschlusspruefung der vereinfachten Fassung vor Veroeffentlichung auf Verstaendlichkeit, Glaeubigkeit und Vollstaendigkeit.

## Worauf besonders achten

- Einfache Sprache und Leichte Sprache sind verschiedene Standards mit unterschiedlichen Regelwerken — Modus am Anfang festlegen, nicht waehrend der Bearbeitung wechseln.
- Kein Rechtsinhalt darf durch Vereinfachung verloren gehen: Fristen, Betraege und Rechtsfolgen muessen exakt erhalten bleiben.
- Leichte Sprache erfordert typischerweise die Einbindung von Prueferinnen und Pruefern mit kognitiven Einschraenkungen — das Plugin kann nur den Text liefern, nicht die Pruefung ersetzen.
- Bei Bescheiden und amtlichen Dokumenten gilt: Vereinfachungen sind Informationshilfen, kein rechtsverbindlicher Ersatz des Originaldokuments.
- AGB-Vereinfachungen koennen auf Einbeziehungsfragen nach § 305 BGB wirken — rechtliche Wechselwirkungen bedenken.

## Typische Fehler

- Zielgruppe nicht definiert: Text wird zu stark oder zu wenig vereinfacht, weil unklar ist, für wen er bestimmt ist.
- Rechtsinhalt-Sicherung uebersprungen: Fristen oder Rechtswirkungen gehen in der Vereinfachung unter.
- Einfache und Leichte Sprache verwechselt: Leichte Sprache hat deutlich strengere Regeln (Satzlaenge, Bildunterstuetzung, Glossar).
- Qualitaetsgate nicht durchgefuehrt: Vereinfachter Text wird veroeffentlicht, ohne auf Korrektheit geprueft zu werden.
- Vereinfachung als rechtsverbindlich behandelt: Mandant glaubt, der vereinfachte Text ersetzt das Original.

## Querverweise

- `datenschutzrecht` — DSGVO-Einwilligungen und Datenschutzerklaerungen muessen verstaendlich formuliert sein (Art. 7 Abs. 2 DSGVO).
- `vertragsrecht` — AGB-Einbeziehung nach § 305 BGB erfordert klare, verstaendliche Formulierungen.
- `selbstvertreter-amtsgericht` — Buerger ohne Rechtskenntnisse koennen von vereinfachten Gerichtsdokumenten profitieren.

## Quellen und Aktualitaet

- Stand: 05/2026
- BITV 2.0 in der Fassung vom 21.05.2019
- Gesetzesfassungen zum Stand-Datum
- Regelwerk Leichte Sprache des Netzwerks Leichte Sprache (netzwerk-leichte-sprache.org)
- WCAG 2.1 (Web Content Accessibility Guidelines)

---

## Skill: `bauen-fristennotiz-naechster-schritt`

_Bauen: Fristennotiz und nächster Schritt im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritis..._

# Bauen: Fristennotiz und nächster Schritt

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 241 Abs. 2 BGB` — Rücksichtnahme-, Schutz- und Organisationspflichten.
- `§ 242 BGB` — Treu und Glauben als Korrektiv enger Klausel- und Anspruchsarbeit.
- `§ 280 Abs. 1 BGB` — Pflichtverletzung, Vertretenmuessen, Schaden.
- `§ 286 Abs. 1 BGB` — Verzug und Fristlogik.
- `§ 195 BGB` — regelmäßige Verjährung.
- `§ 199 Abs. 1 BGB` — Beginn der regelmäßigen Verjährung.
- `§ 253 Abs. 2 ZPO` — Bestimmtheit von Antrag und Klagegrund.
- `§ 138 Abs. 1 ZPO` — Wahrheitspflicht und vollstaendiger Tatsachenvortrag.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Bauen: Fristennotiz und nächster Schritt
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Bauen** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 11 BGG
- § 58 VwG
- § 14 BGG
- § 184 GVG
- § 186 GVG
- § 90 SGG
- § 35 VwVfG
- § 37 VwVfG
- § 187 GVG
- § 73 VwG
- § 12a BGG
- § 29 VwVfG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `einfache-sprache`

_Kanzlei oder Behörde will juristischen Text für normale Buerger verstaendlich machen: Einfache Sprache B1-Niveau zielgruppenorientiert klare Gliederung erklärte Rechtsbegriffe gesicherte Fristen. Normen BGG § 11 Leichte Sprache Behindertenrecht BITV 2.0. Prüfraster Satzlaenge Aktiv-Passiv-Balance..._

# Einfache Sprache

Dieses Fachmodul, wenn ein juristischer Text für ein allgemeines Publikum
verständlich werden soll, ohne die Standardsprache vollständig zu verlassen.

## Triage zu Beginn
1. Welche Zielgruppe soll den Text lesen (allgemeines Publikum, Personen mit geringer Lesekompetenz, Verbraucher mit Behördenkontakt)?
2. Welches Medium: Brief, Bescheid, Website, Formular, E-Mail?
3. Darf der Text stark gekürzt werden oder muss der vollständige Rechtsinhalt erhalten bleiben?
4. Gibt es bereits einen Hausstil oder eine Vorlage für Einfache Sprache in der Einrichtung?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 11 BGG — Barrierefreiheit von Bescheiden und öffentlichen Dokumenten
- § 9 EBV — Einfache Sprache in Bescheiden der Erbenberatung
- § 242 BGB — Treu und Glauben als Grundlage des Transparenzgebots
- BITV 2.0 — Barrierefreie-Informationstechnik-Verordnung, Anhang 1 (Verstaendlichkeit digitaler Dokumente)

## Normen & Rechtsprechung

Konkret zu prüfen:

- § 11 SGB I (Verständlichkeit)
- BGG (Behindertengleichstellungsgesetz) § 11
- BITV 2.0 (Barrierefreie Informationstechnik-Verordnung)
- UN-BRK Art. 9, 21

## Output-Template: Einfache-Sprache-Fassung

**Adressat:** Mandant / Buerger — **Tonfall:** klar, direkt, respektvoll

```
### Kurze Antwort

[1-2 Saetze: Das Wichtigste zuerst]

### Was ist passiert?

[Sachverhalt ohne Fachjargon]

### Was bedeutet das für Sie?

[Rechtliche Konsequenzen in verstaendlichen Worten]

### Was koennen Sie jetzt tun?

Option A: [Handlung 1 — Frist: DD.MM.JJJJ]
Option B: [Handlung 2]

### Frist

Wichtig: Bis [DATUM] muessen Sie handeln.
Wenn Sie nichts tun, dann: [Rechtsfolge kurz]

### Schwere Woerter kurz erklaert

- Widerspruch: Sie sagen der Behörde, dass Sie nicht einverstanden sind.
- Verjährung: Nach Ablauf dieser Frist koennen Sie nichts mehr verlangen.
```

## Ziel

Der Text soll schnell beantworten:

- Worum geht es?
- Was bedeutet das für die lesende Person?
- Was muss oder kann sie tun?
- Bis wann?
- Was passiert, wenn sie nichts tut?

## Regeln für die Übertragung

- Stelle die wichtigste Information an den Anfang.
- Verwende klare Überschriften.
- Halte Absätze kurz.
- Schreibe aktiv.
- Nutze Verben statt Substantivierungen.
- Vermeide verschachtelte Sätze.
- Erkläre Fachwörter beim ersten Auftreten.
- Verwende denselben Begriff immer gleich.
- Ersetze Amts- und Kanzleistil durch direkte, respektvolle Sprache.
- Lass Rechtsgrundlagen stehen, wenn sie wichtig sind, aber erkläre ihre
 Bedeutung.

## Juristische Struktur

Für Mandantenbriefe und Verbraucherinformationen verwende bevorzugt:

```markdown
### Kurze Antwort

...

### Was ist passiert?

...

### Was bedeutet das für Sie?

...

### Was können Sie jetzt tun?

...

### Frist

...

### Schwere Wörter kurz erklärt

...
```

## Was nicht passieren darf

- Keine Frist verkürzen oder verlängern.
- Keine Pflicht in eine bloße Empfehlung umformulieren.
- Kein Wahlrecht unterschlagen.
- Keine Ausnahme weglassen, wenn sie praktisch wichtig sein kann.
- Keine ungesicherte Rechtsberatung hinzufügen.
- Keine rechtliche Unsicherheit als sicher darstellen.

## Stilhinweise

Schlecht:

> Gegen den Bescheid kann binnen eines Monats nach Bekanntgabe Widerspruch
> erhoben werden.

Besser:

> Sie können Widerspruch einlegen.
> Dafür haben Sie 1 Monat Zeit.
> Die Frist beginnt, wenn Sie den Bescheid bekommen haben.

## Ausgabe

Gib am Ende eine Mini-Prüfung aus:

| Punkt | Ergebnis |
| --- | --- |
| Zielgruppe genannt | ja/nein |
| Fristen erhalten | ja/nein |
| Rechtsfolgen erhalten | ja/nein |
| schwere Wörter erklärt | ja/nein |
| weiterer Prüfbedarf | kurz |

---

## Skill: `experimentelle-schriftsatz-brief-memo-bausteine`

_Experimentelle: Schriftsatz-, Brief- und Memo-Bausteine im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrenss..._

# Experimentelle: Schriftsatz-, Brief- und Memo-Bausteine

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 241 Abs. 2 BGB` — Rücksichtnahme-, Schutz- und Organisationspflichten.
- `§ 242 BGB` — Treu und Glauben als Korrektiv enger Klausel- und Anspruchsarbeit.
- `§ 280 Abs. 1 BGB` — Pflichtverletzung, Vertretenmuessen, Schaden.
- `§ 286 Abs. 1 BGB` — Verzug und Fristlogik.
- `§ 195 BGB` — regelmäßige Verjährung.
- `§ 199 Abs. 1 BGB` — Beginn der regelmäßigen Verjährung.
- `§ 253 Abs. 2 ZPO` — Bestimmtheit von Antrag und Klagegrund.
- `§ 138 Abs. 1 ZPO` — Wahrheitspflicht und vollstaendiger Tatsachenvortrag.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Experimentelle: Schriftsatz-, Brief- und Memo-Bausteine
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Experimentelle** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `familienrecht-erstgespraech-juristische`

_Familienrecht Erstgespraech in Einfacher Sprache: Trennung, Scheidung, Unterhalt, Sorgerecht, Umgang. Vorlage Memo für den Mandanten: 'Was muessen Sie wissen, was muessen Sie entscheiden?' Sprachlich barrierearm im Einfache/Leichte Sprache Jura: prüft konkret die einschlägigen Tatbestandsmerkmale..._

# ELS-J Familienrecht-Erstgespraech

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BFSG ab 28.06.2025, BITV § 4 Verständlichkeit, BGG § 11 Pflicht zur einfachen Sprache bei Bescheiden auf Antrag.
- Tragende Normen verifizieren: BGG §§ 11, 12a, BITV 2.0 § 4, BFSG, UN-Behindertenrechtskonvention Art. 9 (Zugänglichkeit), EU-RL 2016/2102, DIN SPEC 33429 (Leichte Sprache), Hurraki-/Inclusion Europe-Regeln — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Behörde, Verwaltungsstelle, Übersetzer Leichte Sprache, Prüfgruppe (Selbstvertreter), Sozialverbände (Lebenshilfe, BAGSO), Behindertenbeauftragter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Bescheid in Leichter Sprache, Erklärfilm-Skript, Antragsformular mit Erläuterung, Mandanteninfo, Prozessunterlagen in einfacher Sprache — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen: ELS-J Familienrecht-Erstgespraech
- **Normen-/Quellenanker:** ELS.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** – streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - nur einschlaegige Normen, verifizierte Rechtsprechung und frei pruefbare amtliche Quellen; keine Literatur- oder Datenbankfundstellen erfinden.
3. **Pruefung im Gutachtenstil** – Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** – konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Normen & Rechtsprechung

Konkret zu prüfen:

- § 11 SGB I (Verständlichkeit)
- BGG (Behindertengleichstellungsgesetz) § 11
- BITV 2.0 (Barrierefreie Informationstechnik-Verordnung)
- UN-BRK Art. 9, 21

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen/Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

---

## Skill: `fristen-form-zustaendigkeit-rechtsweg`

_Einfache: Fristen, Form, Zuständigkeit und Rechtsweg im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstuf..._

# Einfache: Fristen, Form, Zuständigkeit und Rechtsweg

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 535 Abs. 1 BGB` — Hauptpflichten des Mietvertrags.
- `§ 536 Abs. 1 BGB` — Minderung.
- `§ 543 Abs. 1 BGB` — ausserordentliche Kuendigung.
- `§ 556 Abs. 1 BGB` — Betriebskostenvereinbarung.
- `§ 556 Abs. 3 BGB` — Abrechnung und Einwendungsfrist.
- `§ 558 Abs. 1 BGB` — Mieterhoehung bis ortsuebliche Vergleichsmiete.
- `§ 559 Abs. 1 BGB` — Modernisierungsmieterhoehung.
- `§ 573 Abs. 1 BGB` — ordentliche Vermieterkuendigung.
- `§ 259 BGB` — Rechnungslegung.
- `§ 2 BetrKV` — Betriebskostenarten.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Einfache: Fristen, Form, Zuständigkeit und Rechtsweg
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Einfache** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `glossar-sonderfall-edge-case`

_Glossar: Sonderfall und Edge-Case-Prüfung im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kriti..._

# Glossar: Sonderfall und Edge-Case-Prüfung

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 241 Abs. 2 BGB` — Rücksichtnahme-, Schutz- und Organisationspflichten.
- `§ 242 BGB` — Treu und Glauben als Korrektiv enger Klausel- und Anspruchsarbeit.
- `§ 280 Abs. 1 BGB` — Pflichtverletzung, Vertretenmuessen, Schaden.
- `§ 286 Abs. 1 BGB` — Verzug und Fristlogik.
- `§ 195 BGB` — regelmäßige Verjährung.
- `§ 199 Abs. 1 BGB` — Beginn der regelmäßigen Verjährung.
- `§ 253 Abs. 2 ZPO` — Bestimmtheit von Antrag und Klagegrund.
- `§ 138 Abs. 1 ZPO` — Wahrheitspflicht und vollstaendiger Tatsachenvortrag.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Glossar: Sonderfall und Edge-Case-Prüfung
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Glossar** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `jura-mandantenkommunikation`

_Jura: Mandantenkommunikation und Entscheidungsvorlage im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstu..._

# Jura: Mandantenkommunikation und Entscheidungsvorlage

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 241 Abs. 2 BGB` — Rücksichtnahme-, Schutz- und Organisationspflichten.
- `§ 242 BGB` — Treu und Glauben als Korrektiv enger Klausel- und Anspruchsarbeit.
- `§ 280 Abs. 1 BGB` — Pflichtverletzung, Vertretenmuessen, Schaden.
- `§ 286 Abs. 1 BGB` — Verzug und Fristlogik.
- `§ 195 BGB` — regelmäßige Verjährung.
- `§ 199 Abs. 1 BGB` — Beginn der regelmäßigen Verjährung.
- `§ 253 Abs. 2 ZPO` — Bestimmtheit von Antrag und Klagegrund.
- `§ 138 Abs. 1 ZPO` — Wahrheitspflicht und vollstaendiger Tatsachenvortrag.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Jura: Mandantenkommunikation und Entscheidungsvorlage
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Jura** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `juristische-erstpruefung-rollenklaerung`

_Juristische: Erstprüfung, Rollenklärung und Mandatsziel im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrenss..._

# Juristische: Erstprüfung, Rollenklärung und Mandatsziel

## Aktenstart statt Formularstart

Wenn zu **Juristische Erstpruefung Rollenklaerung** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Einfache Leichte Sprache Jura** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 5 Abs. 3 Satz 1 GG` — Wissenschaftsfreiheit.
- `Art. 12 Abs. 1 GG` — Berufswahl- und Ausbildungsbezug.
- `Art. 3 Abs. 1 GG` — Gleichbehandlung und Bewertungsfairness.
- `§ 2 HRG` — Aufgaben der Hochschulen.
- `§ 4 HRG` — Freiheit von Forschung, Lehre und Studium.
- `§ 7 HRG` — Ziel des Studiums.
- `§ 15 HRG` — Pruefungen und Leistungspunktsystem.
- `§ 16 HRG` — Pruefungsordnungen.
- `§ 70 Abs. 1 VwGO` — Widerspruchsfrist.
- `§ 123 Abs. 1 VwGO` — Eilrechtsschutz bei Studien-/Pruefungsentscheidungen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Juristische: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Juristische** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `juristische-sicherung`

_Beim Vereinfachen juristischer Texte darf kein Rechtsinhalt verloren gehen: Rechte Pflichten Fristen Betraege Rechtsfolgen Ausnahmen. Normen §§ 133 157 BGB Auslegungspflicht. Prüfraster Rechte-Vollständigkeit Pflichten-Sicherung Fristen-Erhalt Rechtsfolgen-Klarheit Ausnahmen-Abbildung. Output jur..._

# Juristische Sicherung

Dieses Fachmodul vor und nach jeder Übertragung.

## Triage zu Beginn
1. Welche Fristen kommen im Originaltext vor — Datum, Fristbeginn, Fristende, Folgen?
2. Welche Pflichten (Muss-Handlungen) und welche Rechte (Kann-Optionen) sind enthalten?
3. Gibt es Ausnahmen oder Vorbehalte, die praktisch wichtig sein koennen?
4. Sind rechtliche Unsicherheiten oder offene Pruefungen im Originaltext erkennbar?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 58 VwGO — Rechtsbehelfsbelehrung und Fristverlaengerung bei fehlerhafter Belehrung
- § 355 BGB — Widerrufsrecht: Frist, Belehrung, Folgen bei fehlender Belehrung
- § 214 BGB — Wirkung der Verjährung
- § 130 BGB — Zugang als Fristbeginn

## Output-Template: Juristische Sicherungs-Matrix

```

## Juristische Sicherung — Pruefvermerk

Dokument: [TITEL / AKTENZEICHEN]
Geprueft am: [DATUM]

| Kategorie | Original | Erhalten? | Bemerkung |
|---|---|---|---|
| Frist | [Datum/Dauer] | ja/nein | [Fristbeginn, -ende, Folge] |
| Pflicht | [Muss-Handlung] | ja/nein | [Nicht abgeschwaecht?] |
| Recht | [Kann-Option] | ja/nein | [Als Option formuliert?] |
| Risiko | [Rechtsfolge] | ja/nein | [Klar aber nicht drohend?] |
| Ausnahme | [wenn vorhanden] | ja/nein | [Gesondert erklaert?] |
| Unsicherheit | [offene Fragen] | ja/nein | [Nicht als sicher dargestellt?] |

Gesamtbefund: freigabereif / nacharbeiten
Offene Punkte: [...]
```

## Bedeutungs-Matrix

Erstelle eine Tabelle:

| Original | Bedeutung | Muss erhalten bleiben? | Umsetzung |
| --- | --- | --- | --- |
| Frist | Datum, Beginn, Ende, Folge bei Versäumnis | immer | sichtbar und einfach |
| Pflicht | was die Person tun muss | immer | nicht abschwächen |
| Recht | was die Person tun darf oder kann | immer | als Option erklären |
| Risiko | Kosten, Klage, Vollstreckung, Sanktion | immer | klar, aber nicht drohend |
| Ausnahme | wann etwas nicht gilt | wenn praktisch relevant | gesondert erklären |
| Unsicherheit | Streit, fehlende Tatsachen, Prüfung offen | immer | nicht als sicher darstellen |

## Modalwörter sichern

Prüfe jedes Modalwort:

- **muss** bleibt muss.
- **kann** bleibt Möglichkeit.
- **darf** bleibt Erlaubnis.
- **soll** wird nicht automatisch zu muss.
- **unverzüglich** wird nicht einfach zu "bald", sondern erklärt.

## Fristen sichern

Bei jeder Frist:

- Datum nennen, wenn bekannt.
- Fristbeginn nennen.
- Fristende nennen.
- Folge nennen.
- Kontakt nennen, wenn die Person handeln soll.

## Rechtsbegriffe

Ein Rechtsbegriff darf ersetzt werden, wenn die Bedeutung vollständig erhalten
bleibt. Wenn nicht, bleibt der Begriff stehen und wird erklärt.

Beispiele für erklärungsbedürftige Wörter:

- Bescheid
- Widerspruch
- Klage
- Rechtskraft
- Vollstreckung
- Kündigung
- Widerruf
- Anfechtung
- Haftung
- Verjährung

## Prüfvermerk

Gib am Ende einen Vermerk aus:

```markdown

## Juristische Sicherung

- Fristen geprüft: ...
- Rechte und Pflichten geprüft: ...
- Risiken geprüft: ...
- Begriffe erklärt: ...
- Nicht geklärt: ...
```

---

## Skill: `juristisches-beweislast-darlegungslast`

_Juristisches: Beweislast, Darlegungslast und Substantiierung im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfah..._

# Juristisches: Beweislast, Darlegungslast und Substantiierung

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 241 Abs. 2 BGB` — Rücksichtnahme-, Schutz- und Organisationspflichten.
- `§ 242 BGB` — Treu und Glauben als Korrektiv enger Klausel- und Anspruchsarbeit.
- `§ 280 Abs. 1 BGB` — Pflichtverletzung, Vertretenmuessen, Schaden.
- `§ 286 Abs. 1 BGB` — Verzug und Fristlogik.
- `§ 195 BGB` — regelmäßige Verjährung.
- `§ 199 Abs. 1 BGB` — Beginn der regelmäßigen Verjährung.
- `§ 253 Abs. 2 ZPO` — Bestimmtheit von Antrag und Klagegrund.
- `§ 138 Abs. 1 ZPO` — Wahrheitspflicht und vollstaendiger Tatsachenvortrag.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Juristisches: Beweislast, Darlegungslast und Substantiierung
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Juristisches** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `kommandocenter`

_Kanzlei oder Behörde startet Vereinfachungs-Projekt für juristischen Text: Zielgruppe Modus Rechtsinhalt-Erfassung Workflow-Steuerung Ausgabe. Normen BGG BITV 2.0. Prüfraster Zielgruppen-Identifikation Modus-Auswahl Skill-Routing Qualitaetsprüfung. Output Projekt-Plan Skill-Routing. Abgrenzung zu..._

# Kommandocenter

Dieser Einstieg führt in jede Übertragung juristischer Texte in
Einfache Sprache oder Leichte Sprache.

## Triage zu Beginn
1. Einfache Sprache oder Leichte Sprache — Zielgruppe bekannt?
2. Welches Format: Brief, Bescheid, Formular, Website, Flyer, Gerichtsinformation?
3. Darf der Text inhaltlich gekuerzt werden oder muss alles erhalten bleiben?
4. Gibt es einen institutionellen Hausstil oder Pruefgruppen für Leichte Sprache?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 11 BGG — Barrierefreiheit: Behörden muessen Informationen in Leichter Sprache oder Einfacher Sprache bereitstellen
- BITV 2.0 — Barrierefreie-Informationstechnik-Verordnung (gilt für öffentliche Stellen)
- § 43 SGB I — Beratungspflicht sozialrechtlich in verstaendlicher Sprache
- § 58 VwGO — Rechtsbehelfsbelehrung: Klarheit als Wirksamkeitsvoraussetzung

## Normen & Rechtsprechung

Konkret zu prüfen:

- § 11 SGB I (Verständlichkeit)
- BGG (Behindertengleichstellungsgesetz) § 11
- BITV 2.0 (Barrierefreie Informationstechnik-Verordnung)
- UN-BRK Art. 9, 21

## Output-Template: Routing-Entscheidung

**Adressat-Bestimmung:**

| Frage | Antwort |
|---|---|
| Zielgruppe | [Bezeichnung] |
| Modus | Einfache Sprache / Leichte Sprache |
| Format | Brief / Bescheid / Website / Formular |
| Vollstaendigkeit | vollstaendig / Zusammenfassung OK |
| Hausstil vorhanden | ja/nein |
| Pruefgruppe vorhanden | ja/nein |

**Naechster Schritt:** Lade `elsj-einfache-sprache` oder `elsj-leichte-sprache` + immer `elsj-juristische-sicherung`.

## Erste Entscheidung

Frage zuerst:

1. Soll der Text in **Einfache Sprache** oder in **Leichte Sprache**?
2. Wer soll den Text lesen?
3. Was soll die Person danach verstehen oder tun?
4. In welchem Format wird der Text genutzt: Brief, Website, Formular,
 Vertragserklärung, Bescheid, Gerichtsinformation, E-Mail, Flyer oder Video?
5. Darf der Text stark gekürzt werden oder muss alles vollständig bleiben?

Wenn die Nutzerin oder der Nutzer unsicher ist, erkläre knapp:

- Einfache Sprache bleibt näher an Standardsprache.
- Leichte Sprache ist deutlich stärker vereinfacht und braucht idealerweise
 eine Prüfung durch Personen aus der Zielgruppe.

## Workflow

### 1. Ausgangstext sichern

Niemals direkt überschreiben. Arbeite mit vier Ebenen:

- Originaltext,
- Bedeutungs-Matrix,
- verständliche Fassung,
- Prüfprotokoll.

### 2. Bedeutungs-Matrix erstellen

Extrahiere vor der Übertragung:

| Feld | Inhalt |
| --- | --- |
| Wer handelt? | Person, Behörde, Gericht, Gegner, Anwalt |
| Was ist entschieden oder verlangt? | Zahlung, Handlung, Unterlassung, Frist |
| Welche Rechtsfolge droht? | Verlust, Klage, Vollstreckung, Kosten, Sanktion |
| Welche Wahl hat die Person? | zahlen, widersprechen, kündigen, nachfragen |
| Welche Frist gilt? | Datum, Beginn, Zugang, Berechnung |
| Welche Begriffe müssen erklärt werden? | Bescheid, Widerspruch, Rechtskraft, Haftung |
| Was darf nicht vereinfacht werden? | Ausnahme, Voraussetzung, Betrag, Rangfolge |

### 3. Modus wählen

Lade danach:

- `elsj-einfache-sprache`, wenn Einfache Sprache gewünscht ist.
- `elsj-leichte-sprache`, wenn Leichte Sprache gewünscht ist.
- `elsj-juristische-sicherung` immer parallel als Prüfschritt.
- `elsj-qualitaetsgate` vor Herausgabe.

### 4. Rückfragen nur wenn nötig

Stelle höchstens fünf Rückfragen auf einmal. Gute Rückfragen sind:

- Soll die Rechtsgrundlage im Text bleiben oder in eine Box?
- Soll der Text direkt an die betroffene Person gerichtet sein?
- Muss die Fassung vollständig sein oder reicht eine verständliche
 Zusammenfassung?
- Gibt es einen Hausstil für Leichte Sprache?
- Wurde eine Prüfgruppe beauftragt?

### 5. Ausgabe

Liefere bei jedem Ergebnis:

1. **Fassung** in gewähltem Modus.
2. **Kurzprotokoll**, welche juristischen Inhalte erhalten wurden.
3. **Glossar** für schwere Wörter.
4. **Offene Prüfungen**, insbesondere Nutzerprüfung bei Leichter Sprache.

---

## Skill: `ls-juristisches-glossar-justizportal-pruefen`

_Juristisches Glossar für Einfache und Leichte Sprache aufbauen: Schlagwort, Schwerverstaendliche Definition, Variante Einfache Sprache, Variante Leichte Sprache. Pro Eintrag Beispielssatz. Strukturierter CSV-Output und Mustertext für 30 Kernbegriffe im Einfache/Leichte Sprache Jura: prüft konkret..._

# LS: Juristisches Glossar

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BFSG ab 28.06.2025, BITV § 4 Verständlichkeit, BGG § 11 Pflicht zur einfachen Sprache bei Bescheiden auf Antrag.
- Tragende Normen verifizieren: BGG §§ 11, 12a, BITV 2.0 § 4, BFSG, UN-Behindertenrechtskonvention Art. 9 (Zugänglichkeit), EU-RL 2016/2102, DIN SPEC 33429 (Leichte Sprache), Hurraki-/Inclusion Europe-Regeln — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Behörde, Verwaltungsstelle, Übersetzer Leichte Sprache, Prüfgruppe (Selbstvertreter), Sozialverbände (Lebenshilfe, BAGSO), Behindertenbeauftragter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Bescheid in Leichter Sprache, Erklärfilm-Skript, Antragsformular mit Erläuterung, Mandanteninfo, Prozessunterlagen in einfacher Sprache — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen: LS: Juristisches Glossar
- **Normen-/Quellenanker:** CSV, LS.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Normen & Rechtsprechung

Konkret zu prüfen:

- § 11 SGB I (Verständlichkeit)
- BGG (Behindertengleichstellungsgesetz) § 11
- BITV 2.0 (Barrierefreie Informationstechnik-Verordnung)
- UN-BRK Art. 9, 21

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

---

## Skill: `rechtsinhalt-interessen`

_Rechtsinhalt: Mehrparteienkonflikt und Interessenmatrix im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrenss..._

# Rechtsinhalt: Mehrparteienkonflikt und Interessenmatrix

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 241 Abs. 2 BGB` — Rücksichtnahme-, Schutz- und Organisationspflichten.
- `§ 242 BGB` — Treu und Glauben als Korrektiv enger Klausel- und Anspruchsarbeit.
- `§ 280 Abs. 1 BGB` — Pflichtverletzung, Vertretenmuessen, Schaden.
- `§ 286 Abs. 1 BGB` — Verzug und Fristlogik.
- `§ 195 BGB` — regelmäßige Verjährung.
- `§ 199 Abs. 1 BGB` — Beginn der regelmäßigen Verjährung.
- `§ 253 Abs. 2 ZPO` — Bestimmtheit von Antrag und Klagegrund.
- `§ 138 Abs. 1 ZPO` — Wahrheitspflicht und vollstaendiger Tatsachenvortrag.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Rechtsinhalt: Mehrparteienkonflikt und Interessenmatrix
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Rechtsinhalt** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

