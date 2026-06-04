# bereicherungs-und-anfechtungsrecht-prüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`bereicherungs-und-anfechtungsrecht-pruefer`) | [`bereicherungs-und-anfechtungsrecht-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bereicherungs-und-anfechtungsrecht-pruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Bereicherungs-Dreiecksverhaeltnis / Doppelverkauf Oldtimer Bischof-Hellberg / Bonn** (`bereicherung-dreiecksverhaeltnis-doppelverkauf-oldtimer-bischof-bonn`) | [Gesamt-PDF lesen](../testakten/bereicherung-dreiecksverhaeltnis-doppelverkauf-oldtimer-bischof-bonn/gesamt-pdf/bereicherung-dreiecksverhaeltnis-doppelverkauf-oldtimer-bischof-bonn_gesamt.pdf) | [`testakte-bereicherung-dreiecksverhaeltnis-doppelverkauf-oldtimer-bischof-bonn.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bereicherung-dreiecksverhaeltnis-doppelverkauf-oldtimer-bischof-bonn.zip) |
| **BGB BT — Holzofen, Lieferkette, Bürgschaft, GoA und Brandschaden** (`bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt`) | [Gesamt-PDF lesen](../testakten/bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt/gesamt-pdf/bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt_gesamt.pdf) | [`testakte-bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Generisches Mechanik-Prüfungs-Plugin zum interaktiven Durchprüfen aller Tatbestandsmerkmale von:

- **Bereicherungsrecht** §§ 812 ff. BGB (Herausgabe ohne Rechtsgrund Erlangtes)
- **Anfechtungsgesetz** (AnfG) — Rückgewähr trotz Rechtsgrund durch benachteiligten Vollstreckungsgläubiger
- **Insolvenzanfechtung** §§ 129–147 InsO — Rückgewähr zur Insolvenzmasse

Kein Rechtsberatungs-Tool. Mechanische Tatbestandsprüfung mit ständigen Warnhinweisen.

---

## Installation

1. Claude Code oder Claude Desktop/Cowork öffnen.
2. **Customize Plugins** bzw. **Personal plugins** wählen.
3. **Install from .zip** und `bereicherungs-und-anfechtungsrecht-pruefer.zip` hochladen.
4. Mit einem konkreten Auftrag starten, zum Beispiel: `Prüfe eine Insolvenzanfechtung gegen einen Lieferanten.`

Alternativ via Marketplace:

```
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install bereicherungs-und-anfechtungsrecht-pruefer@claude-fuer-deutsches-recht
```

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

---

## Kern-Workflow

1. **Triage**: Was ist passiert? Vermögensverschiebung mit oder ohne Rechtsgrund? Insolvenzverfahren eröffnet? Vollstreckungstitel vorhanden?
2. **Weichenstellung**:
   - Kein Rechtsgrund → Bereicherungsrecht (Leistungs- oder Nichtleistungskondiktion)
   - Rechtsgrund + außerhalb Insolvenz + Vollstreckungsgläubiger benachteiligt → AnfG
   - Rechtsgrund + Insolvenzverfahren → InsO-Anfechtung
   - Kombinationen und Konkurrenzen werden gesondert geprüft
3. **Bereicherungsrechtliche Feinsortierung**: Vermögensvorteil, Leistungszweck, Rechtsgrund, Behaltensgrund, Mehrpersonenverhältnis, Saldo, § 818 BGB
4. **Tatbestandsmerkmale pro Pfad**: Definitionen, Belegbedarf, Subsumtion im Vier-Schritt-Schema (Obersatz, Definition, Untersatz, Ergebnis)
5. **Rechtsfolgen, Konkurrenzen, Verjährung, Einreden**
6. **Output**: Klageschrift Bereicherungsklage, Anfechtungsklage (AnfG), Anfechtungsanzeige des Insolvenzverwalters

---

## Skills (98)

### A. Triage / Weichenstellung (6)

| Skill | Inhalt |
|---|---|
| `allgemein` | Einstieg, Routing und Überblick über Bereicherung, AnfG, InsO-Anfechtung und KI-Screening |
| `triage-vermoegensverschiebung-erfassen` | Strukturierte Erfassung: Wer hat was an wen geleistet, Belege, Zeitpunkt |
| `weichenstellung-bereicherung-oder-anfechtung` | Entscheidungsknoten: Rechtsgrund, Insolvenz, Vollstreckungstitel |
| `falsche-wiese-warnung-bereicherung-anfechtung` | Typische Falschverortungen und Systemfehler |
| `parallel-und-konkurrenz-pruefung` | Bereicherungsrecht und Anfechtung nebeneinander |
| `mandatsabbruch-empfehlung-an-fachanwalt-insolvenz` | Komplexitätsindikatoren, Fachanwaltsempfehlung |

### B. Bereicherungsrecht — Dogmatik und Feinsortierung (4)

| Skill | Inhalt |
|---|---|
| `rechtsgrund-und-behaltensgrund-pruefen` | Vermögensvorteil, Zweck, Rechtsgrund und Behaltensgrund sauber trennen |
| `zweckverfehlung-und-kondiktionszweck` | Zweckabrede, Zweckverfehlung, Risikozuweisung, Ausschlussgründe |
| `saldotheorie-rueckabwicklung-nichtiger-vertraege` | Rückabwicklung gegenseitiger Verträge mit Saldo, Schutzkorrekturen, Zug um Zug |
| `nutzungen-verwendungen-gefahrtragung-818` | Nutzungen, Surrogate, Verwendungen, Ersparnisse und Gefahrtragung bei § 818 BGB |

### C. Bereicherungsrecht — 50 zusätzliche Vertiefungs-Skills (50)

| Skill | Inhalt |
|---|---|
| `anspruchsziel-und-rueckabwicklungsarchitektur` | Anspruchsziel und Rückabwicklungsarchitektur: das praktische Rückabwicklungsziel in eine belastbare Anspruchsarchitektur übersetzt werden muss |
| `kondiktionskarte-vollstaendiger-fallaufbau` | Kondiktionskarte: vollständiger Fallaufbau: ein komplexer Fall zuerst als Personen-, Leistungs- und Vermögenskarte erfasst werden muss |
| `vermoegensvergleich-und-nettobetrachtung` | Vermögensvergleich und Nettobetrachtung: der bereicherungsrechtliche Netto-Vorteil statt nur der äußere Zufluss gesucht wird |
| `rechtsgrundmangel-anfang-und-wegfall` | Rechtsgrundmangel: Anfang und Wegfall: Anfangsmangel, späterer Wegfall, Teilmangel und Zweckausfall zeitlich getrennt werden müssen |
| `beweise-und-darlegungslast-bereicherungsrecht` | Beweise und Darlegungslast im Bereicherungsrecht: Darlegung, Beweislast und Belegbedarf anspruchsbezogen geplant werden müssen |
| `condictio-ob-causam-finitam-wegfall-des-rechtsgrundes` | Condictio ob causam finitam: Wegfall des Rechtsgrundes: ein zunächst bestehender Rechtsgrund später entfallen sein kann |
| `condictio-ob-rem-zweckabrede` | Condictio ob rem: Zweckabrede: eine Leistung für einen erkennbar bezweckten Erfolg erbracht wurde |
| `condictio-causa-data-causa-non-secuta` | Causa data causa non secuta: der erwartete Leistungserfolg endgültig nicht eingetreten ist |
| `leistungszweck-bei-vorleistung-und-anzahlung` | Leistungszweck bei Vorleistung und Anzahlung: Anzahlungen, Vorschüsse oder Reservierungsentgelte rückabgewickelt werden sollen |
| `schenkung-leihe-und-unbenannte-zuwendung` | Schenkung, Leihe und unbenannte Zuwendung: unentgeltliche Zuwendung, Nutzungsüberlassung und Zweckbindung auseinanderfallen können |
| `anweisungsfall-deckungs-und-valutaverhaeltnis` | Anweisungsfall: Deckungs- und Valutaverhältnis: ein Zahlungs- oder Leistungsdreieck mit Deckungs- und Valutaverhältnis vorliegt |
| `bankueberweisung-fehlbuchung-und-empfaengerhorizont` | Banküberweisung, Fehlbuchung und Empfängerhorizont: eine Banküberweisung, Fehlbuchung oder Fehlleitung bereicherungsrechtlich zugeordnet werden muss |
| `drittleistung-267-bgb-und-rueckgriff` | Drittleistung nach § 267 BGB und Rückgriff: ein Dritter bewusst auf eine fremde Schuld gezahlt haben könnte |
| `abgetretene-forderung-und-zession` | Abgetretene Forderung und Zession: Abtretung, Zahlung und Forderungsbestand auseinandergehalten werden müssen |
| `zahlung-auf-fremde-schuld-und-putativschuldner` | Zahlung auf fremde Schuld und Putativschuldner: jemand irrtümlich als vermeintlicher Schuldner oder auf fremde Schuld zahlt |
| `zahlstelle-bote-vertreter-und-treuhand` | Zahlstelle, Bote, Vertreter und Treuhand: eine Zwischenperson im Zahlungsweg rechtlich richtig eingeordnet werden muss |
| `insolvenzrisiko-im-dreipersonenverhaeltnis` | Insolvenzrisiko im Dreipersonenverhältnis: ein Direktanspruch im Dreieck faktisch ein Insolvenzrisiko verlagern würde |
| `bereicherungsausgleich-bei-kettenvertraegen` | Bereicherungsausgleich bei Kettenverträgen: Vertrags- oder Lieferketten ohne falschen Durchgriff rückabgewickelt werden müssen |
| `wertersatz-bei-dienstleistung-und-gebrauchsvorteil` | Wertersatz bei Dienstleistung und Gebrauchsvorteil: eine nicht rückgabefähige Dienstleistung oder Nutzung bewertet werden muss |
| `ersparte-aufwendungen-und-lebenshaltung` | Ersparte Aufwendungen und Lebenshaltung: Verbrauch des Erlangten mit ersparten eigenen Ausgaben kollidiert |
| `surrogat-erloes-versicherung-ersatzforderung` | Surrogat, Erlös, Versicherung und Ersatzforderung: an die Stelle des Erlangten ein Ersatzwert getreten sein kann |
| `boesglaeubigkeit-kenntnis-und-819-timing` | Bösgläubigkeit, Kenntnis und § 819 Timing: der Zeitpunkt der Kenntnis über den Umfang der Haftung entscheidet |
| `entreicherung-beweislast-und-substantiierung` | Entreicherung: Beweislast und Substantiierung: § 818 Abs. 3 BGB konkret behauptet oder angegriffen werden muss |
| `verwendungen-auf-das-erlangte` | Verwendungen auf das Erlangte: Aufwendungen auf den erhaltenen Gegenstand als Abzug oder Gegenrecht auftauchen |
| `nutzungen-zinsen-fruechte-gebrauchsvorteile` | Nutzungen, Zinsen, Früchte und Gebrauchsvorteile: Nutzungen und Zinsen ohne Doppelzählung erfasst werden müssen |
| `wertveraenderung-und-stichtag` | Wertveränderung und Bewertungsstichtag: Wertsteigerung, Wertverlust und Bewertungszeitpunkt streitig sind |
| `ebv-und-bereicherungsrecht` | EBV und Bereicherungsrecht: Eigentum, Besitz, Nutzungen und Verwendungen mit §§ 812 ff. BGB konkurrieren |
| `ruecktritt-widerruf-und-bereicherung` | Rücktritt, Widerruf und Bereicherung: Rücktritts- oder Widerrufsfolgen neben Bereicherungsrecht stehen |
| `anfechtung-142-und-rueckabwicklung` | Anfechtung nach § 142 BGB und Rückabwicklung: eine wirksame Anfechtung den Rechtsgrund rückwirkend beseitigt |
| `nichtiger-vertrag-134-138-und-rueckforderung` | Nichtiger Vertrag nach §§ 134 und 138 BGB: Verbots- oder Sittenwidrigkeit die Rückforderung prägt |
| `minderjaehrige-und-schutzwertung` | Minderjährige und Schutzwertung: Minderjährigenschutz durch Wertersatz oder Saldo nicht entwertet werden darf |
| `gesetzesverstoss-und-817-satz-2-vertiefung` | Gesetzesverstoß und § 817 Satz 2 vertieft: § 817 S. 2 BGB nach Normzweck und Schutzrichtung geprüft werden muss |
| `kondiktion-bei-schwarzarbeit-und-illegalitaet` | Kondiktion bei Schwarzarbeit und Illegalität: illegale Austauschverhältnisse bereicherungsrechtlich nicht normalisiert werden dürfen |
| `familien-und-partnerzuwendungen` | Familien- und Partnerzuwendungen: private Zuwendungen zwischen Näheverhältnis, Zweckbindung und Spezialrecht stehen |
| `gesellschaftsrechtliche-zuwendungen` | Gesellschaftsrechtliche Zuwendungen: Gesellschafterleistungen nicht ohne Gesellschaftsrecht rückabgewickelt werden dürfen |
| `arbeitsrechtliche-ueberzahlung` | Arbeitsrechtliche Überzahlung: Arbeitsentgelt überzahlt wurde und Ausschlussfristen oder Entreicherung drohen |
| `miet-und-pachtrechtliche-rueckabwicklung` | Miet- und pachtrechtliche Rückabwicklung: Miete, Pacht, Kaution oder Nutzung ohne Vertrag zurückabgewickelt werden |
| `kredit-darlehen-und-zinsenrueckforderung` | Kredit, Darlehen und Zinsenrückforderung: Darlehenszahlungen, Zinsen oder Entgelte positionengenau geprüft werden müssen |
| `versicherung-und-praemienrueckforderung` | Versicherung und Prämienrückforderung: Prämien und Leistungen im Versicherungsverhältnis zurückgefordert werden |
| `oeffentlich-rechtliche-rueckforderung-abgrenzung` | Öffentlich-rechtliche Rückforderung abgrenzen: Zivilrecht und öffentlich-rechtliche Erstattung auseinanderzuhalten sind |
| `eingriff-in-namen-bild-und-persoenlichkeitswert` | Eingriff in Name, Bild und Persönlichkeitswert: kommerzieller Persönlichkeitswert ohne Zustimmung genutzt wurde |
| `eigentumsnutzung-und-sachenrechtliche-zuweisung` | Eigentumsnutzung und sachenrechtliche Zuweisung: fremdes Eigentum wirtschaftlich genutzt wurde |
| `ip-lizenzanalogie-und-bereicherung` | IP-Lizenzanalogie und Bereicherung: ersparte Lizenz und Schutzrechtsnutzung bereicherungsrechtlich bewertet werden |
| `verfuegung-nichtberechtigter-816-vertiefung` | § 816 BGB vertieft: Verfügung Nichtberechtigter: ein Nichtberechtigter wirksam über fremde Rechte verfügt hat |
| `weitergabe-und-822-verteidigung` | Weitergabe und § 822 BGB Verteidigung: ein erlangter Vorteil unentgeltlich an Dritte weitergegeben wurde |
| `klageantrag-zahlung-herausgabe-zug-um-zug` | Klageantrag: Zahlung, Herausgabe, Zug um Zug: aus der Prüfung ein vollstreckbarer Antrag gebaut werden muss |
| `vergleichsberechnung-und-verhandlungsangebot` | Vergleichsberechnung und Verhandlungsangebot: bereicherungsrechtliche Risiken in einen Vergleichskorridor übersetzt werden |
| `verteidigung-gegen-bereicherungsklage` | Verteidigung gegen Bereicherungsklage: eine Bereicherungsklage systematisch abgewehrt werden soll |
| `mandanteninterview-bereicherungsrecht` | Mandanteninterview Bereicherungsrecht: die Tatsachen für einen Bereicherungsfall erst strukturiert erhoben werden müssen |
| `qualitaetskontrolle-halluzinationsschutz-bereicherungsrecht` | Qualitätskontrolle und Halluzinationsschutz: ein bereicherungsrechtlicher Output auf Scheinsicherheit und Quellenrisiken geprüft wird |

### D. Bereicherungsrecht — Leistungskondiktion §§ 812 ff. BGB (8)

| Skill | Inhalt |
|---|---|
| `leistungskondiktion-grundtatbestand-812-i-1-alt-1` | Grundtatbestand: etwas erlangt, durch Leistung, ohne Rechtsgrund |
| `leistungsbegriff-bewusste-zweckgerichtete-mehrung` | Definition Leistung, Mehrpersonenverhältnisse |
| `condictio-indebiti-813-bgb` | Einredebehaftete Verbindlichkeiten |
| `ausschluss-814-bgb-kenntnis-der-nichtschuld` | Ausschluss bei positiver Kenntnis der Nichtschuld |
| `ausschluss-817-bgb-gesetzes-und-sittenverstoss` | Sperrwirkung bei eigenem Verstoß, Rückausnahmen |
| `umfang-der-herausgabe-818-bgb-und-entreicherung` | Surrogate, Nutzungen, Wertersatz, Entreicherungseinrede |
| `verschaerfte-haftung-819-bgb-bei-bosglaeubigkeit` | Bösgläubigkeit, Rechtshängigkeit, Haftungsfolgen |
| `mehrpersonenverhaeltnisse-direkt-und-durchgriffskondiktion` | Anweisungsfälle, Doppelmangel, Drittleistung |

### E. Bereicherungsrecht — Nichtleistungskondiktion §§ 812 ff. BGB (4)

| Skill | Inhalt |
|---|---|
| `nichtleistungskondiktion-grundtatbestand-812-i-1-alt-2` | Grundtatbestand: in sonstiger Weise erlangt |
| `eingriffskondiktion-zuweisungsgehalt` | Eingriff in Rechtszuweisungsgehalt, IP, Persönlichkeitsrecht |
| `verfuegung-eines-nichtberechtigten-816-bgb` | Entgeltliche und unentgeltliche Verfügung |
| `bereicherung-eines-dritten-822-bgb` | Unentgeltliche Weitergabe an Dritten |

### F. Anfechtungsgesetz — außerhalb Insolvenz (8)

| Skill | Inhalt |
|---|---|
| `anfg-grundtatbestand-und-anfechtungsberechtigte` | § 2 AnfG: Titel, fällige Forderung, Fruchtlosigkeit |
| `anfg-vorsatzanfechtung-3-i` | Benachteiligungsvorsatz und Kenntnis, zehn Jahre |
| `anfg-unentgeltliche-leistung-4` | Unentgeltlichkeit, vier Jahre |
| `anfg-mittelbare-benachteiligung-und-kongruenz` | Kongruente und inkongruente Deckung im AnfG |
| `anfg-fristen-und-anfechtungszeitraum` | Fristen §§ 3 und 4 AnfG, Verjährung |
| `anfg-rechtsfolge-rueckgewaehr-11` | Duldungspflicht, Rückgewähr, Wertersatz |
| `anfg-anfechtungsklage-prozessuales` | Zuständigkeit, Klageantrag, Streitwert, Vollstreckung |
| `anfg-einreden-und-verteidigung-anfechtungsgegner` | Gegenwehr des Anfechtungsgegners |

### G. Insolvenzanfechtung §§ 129–147 InsO (11)

| Skill | Inhalt |
|---|---|
| `inso-grundtatbestand-129-glaeubigerbenachteiligung` | Grundtatbestand: Rechtshandlung, objektive Benachteiligung |
| `inso-kongruente-deckung-130` | Drei Monate, Zahlungsunfähigkeit, Kenntnis |
| `inso-inkongruente-deckung-131` | Nicht beanspruchbare Leistung, Fristen |
| `inso-unmittelbar-nachteilige-rechtshandlungen-132` | § 132 InsO, drei Monate, unmittelbare Nachteiligkeit |
| `inso-vorsatzanfechtung-133` | Benachteiligungsvorsatz, Reform 2017, zehn Jahre, vier Jahre bei Deckung, zwei Jahre § 133 Abs. 4 |
| `inso-unentgeltliche-leistung-134` | Vier Jahre, keine Verschuldenserfordernis |
| `inso-gesellschafterdarlehen-135` | Gesellschafterdarlehen, Drittdarlehen mit Gesellschaftersicherheit, § 135 InsO |
| `inso-bargeschaeft-142` | Bargeschäft, unmittelbarer gleichwertiger Austausch, § 133-Unlauterkeit |
| `inso-rechtsfolge-rueckgewaehr-143-bis-147` | Rückgewähr zur Masse, Wertersatz, Gegenleistung, Verjährung |
| `inso-ki-anfechtungsansprueche-schuldnerakten` | KI-Screening von Schuldnerakten auf Anfechtungskandidaten mit Human-Review-Grenzen |
| `inso-verteidigung-anfechtungsgegner` | Verteidigung gegen Insolvenzanfechtung aus Sicht des Anfechtungsgegners |

### H. Konkurrenzen und Verjährung (3)

| Skill | Inhalt |
|---|---|
| `konkurrenz-bereicherung-vertraglich-deliktisch` | §§ 812 ff. neben Vertrag, Delikt, EBV |
| `konkurrenz-bereicherung-anfechtung-und-vindikation` | § 812 BGB neben AnfG, InsO und § 985 BGB |
| `verjaehrung-bereicherung-anfechtung-fristen` | § 195 BGB, § 15 AnfG, § 146 InsO, absolute Grenzen |

### Output-Skills (4)

| Skill | Inhalt |
|---|---|
| `output-klageschrift-bereicherungsklage` | Muster Klageschrift § 812 BGB |
| `output-anfechtungsklage-anfg` | Muster Anfechtungsklage nach AnfG |
| `output-anfechtungsanzeige-insolvenzverwalter` | Muster Anschreiben Insolvenzverwalter |
| `output-warnhinweis-und-pruefungsdokument` | Pflicht-Header und Warnblock |

---

## Inhaltliche Regeln

- **Keine Rechtsberatung** — jeder Skill endet mit Disclaimer-Block.
- Paragrafen-Format: `§ 812 Abs. 1 S. 1 Alt. 1 BGB`, `§ 133 InsO`, `§ 3 AnfG`.
- Beträge ohne Tausender-Komma.
- Umlaute in Texten ja, in Skill-Slugs nicht.
- Verbotene Einzel-Begriffe: bestimmte Modell- und Produktnamen (siehe CONTRIBUTING.md des Repos).

---

## Lizenz

Apache-2.0 OR MIT

## Autor

Klotzkette


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 29 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Bereicherungs- und Anfechtungsrecht-Prüfer. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen kl... |
| `kompendium-01-anfg-fristen-und-anf-bis-nichtiger-vertrag-13` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 01; bündelt 4 frühere Spezialskills (anfg-fristen-und-anfechtungszeitraum, verjaehrung-bereicherung-anfechtung-fristen, konkurrenz-bereicherung-vertraglich-delik... |
| `kompendium-02-verschaerfte-haftung-bis-anfg-anfechtungsklag` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 02; bündelt 4 frühere Spezialskills (verschaerfte-haftung-819-bgb-bei-bosglaeubigkeit, abgetretene-forderung-und-zession, anfechtung-142-und-rueckabwicklung, anf... |
| `kompendium-03-anfg-einreden-und-ve-bis-anfg-rechtsfolge-rue` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 03; bündelt 4 frühere Spezialskills (anfg-einreden-und-verteidigung-anfechtungsgegner, anfg-grundtatbestand-und-anfechtungsberechtigte, anfg-mittelbare-benachtei... |
| `kompendium-04-anfg-unentgeltliche-bis-anweisungsfall-decku` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 04; bündelt 4 frühere Spezialskills (anfg-unentgeltliche-leistung-4, anfg-vorsatzanfechtung-3-i, anspruchsziel-und-rueckabwicklungsarchitektur, anweisungsfall-de... |
| `kompendium-05-arbeitsrechtliche-ue-bis-bankueberweisung-feh` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 05; bündelt 4 frühere Spezialskills (arbeitsrechtliche-ueberzahlung, ausschluss-814-bgb-kenntnis-der-nichtschuld, ausschluss-817-bgb-gesetzes-und-sittenverstoss,... |
| `kompendium-06-bereicherung-eines-d-bis-boesglaeubigkeit-ken` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 06; bündelt 4 frühere Spezialskills (bereicherung-eines-dritten-822-bgb, bereicherungsausgleich-bei-kettenvertraegen, beweise-und-darlegungslast-bereicherungsrec... |
| `kompendium-07-condictio-causa-data-bis-condictio-ob-rem-zwe` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 07; bündelt 4 frühere Spezialskills (condictio-causa-data-causa-non-secuta, condictio-indebiti-813-bgb, condictio-ob-causam-finitam-wegfall-des-rechtsgrundes, co... |
| `kompendium-08-drittleistung-267-bg-bis-eingriff-in-namen-bi` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 08; bündelt 4 frühere Spezialskills (drittleistung-267-bgb-und-rueckgriff, ebv-und-bereicherungsrecht, eigentumsnutzung-und-sachenrechtliche-zuweisung, eingriff-... |
| `kompendium-09-eingriffskondiktion-bis-falsche-wiese-warnun` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 09; bündelt 4 frühere Spezialskills (eingriffskondiktion-zuweisungsgehalt, entreicherung-beweislast-und-substantiierung, ersparte-aufwendungen-und-lebenshaltung,... |
| `kompendium-10-familien-und-partner-bis-inso-bargeschaeft-14` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 10; bündelt 4 frühere Spezialskills (familien-und-partnerzuwendungen, gesellschaftsrechtliche-zuwendungen, gesetzesverstoss-und-817-satz-2-vertiefung, inso-barge... |
| `kompendium-11-inso-gesellschafterd-bis-inso-ki-anfechtungsa` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 11; bündelt 4 frühere Spezialskills (inso-gesellschafterdarlehen-135, inso-grundtatbestand-129-glaeubigerbenachteiligung, inso-inkongruente-deckung-131, inso-ki-... |
| `kompendium-12-inso-kongruente-deck-bis-inso-unmittelbar-nac` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 12; bündelt 4 frühere Spezialskills (inso-kongruente-deckung-130, inso-rechtsfolge-rueckgewaehr-143-bis-147, inso-unentgeltliche-leistung-134, inso-unmittelbar-n... |
| `kompendium-13-inso-verteidigung-an-bis-ip-lizenzanalogie-un` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 13; bündelt 4 frühere Spezialskills (inso-verteidigung-anfechtungsgegner, inso-vorsatzanfechtung-133, insolvenzrisiko-im-dreipersonenverhaeltnis, ip-lizenzanalog... |
| `kompendium-14-klageantrag-zahlung-bis-konkurrenz-bereicher` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 14; bündelt 4 frühere Spezialskills (klageantrag-zahlung-herausgabe-zug-um-zug, kondiktion-bei-schwarzarbeit-und-illegalitaet, kondiktionskarte-vollstaendiger-fa... |
| `kompendium-15-kredit-darlehen-und-bis-leistungszweck-bei-v` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 15; bündelt 4 frühere Spezialskills (kredit-darlehen-und-zinsenrueckforderung, leistungsbegriff-bewusste-zweckgerichtete-mehrung, leistungskondiktion-grundtatbes... |
| `kompendium-16-mandanteninterview-b-bis-miet-und-pachtrechtl` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 16; bündelt 4 frühere Spezialskills (mandanteninterview-bereicherungsrecht, mandatsabbruch-empfehlung-an-fachanwalt-insolvenz, mehrpersonenverhaeltnisse-direkt-u... |
| `kompendium-17-minderjaehrige-und-s-bis-nutzungen-zinsen-fru` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 17; bündelt 4 frühere Spezialskills (minderjaehrige-und-schutzwertung, nichtleistungskondiktion-grundtatbestand-812-i-1-alt-2, nutzungen-verwendungen-gefahrtragu... |
| `kompendium-18-oeffentlich-rechtlic-bis-rechtsgrund-und-beha` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 18; bündelt 4 frühere Spezialskills (oeffentlich-rechtliche-rueckforderung-abgrenzung, parallel-und-konkurrenz-pruefung, qualitaetskontrolle-halluzinationsschutz... |
| `kompendium-19-rechtsgrundmangel-an-bis-schenkung-leihe-und` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 19; bündelt 4 frühere Spezialskills (rechtsgrundmangel-anfang-und-wegfall, ruecktritt-widerruf-und-bereicherung, saldotheorie-rueckabwicklung-nichtiger-vertraege... |
| `kompendium-20-surrogat-erloes-vers-bis-verfuegung-eines-nic` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 20; bündelt 4 frühere Spezialskills (surrogat-erloes-versicherung-ersatzforderung, triage-vermoegensverschiebung-erfassen, umfang-der-herausgabe-818-bgb-und-entr... |
| `kompendium-21-verfuegung-nichtbere-bis-versicherung-und-pra` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 21; bündelt 4 frühere Spezialskills (verfuegung-nichtberechtigter-816-vertiefung, vergleichsberechnung-und-verhandlungsangebot, vermoegensvergleich-und-nettobetr... |
| `kompendium-22-verteidigung-gegen-b-bis-weitergabe-und-822-v` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 22; bündelt 4 frühere Spezialskills (verteidigung-gegen-bereicherungsklage, verwendungen-auf-das-erlangte, weichenstellung-bereicherung-oder-anfechtung, weiterga... |
| `kompendium-23-wertersatz-bei-diens-bis-zahlung-auf-fremde-s` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 23; bündelt 4 frühere Spezialskills (wertersatz-bei-dienstleistung-und-gebrauchsvorteil, wertveraenderung-und-stichtag, zahlstelle-bote-vertreter-und-treuhand, z... |
| `kompendium-24-zweckverfehlung-und-bis-zweckverfehlung-und` | bereicherungs-und-anfechtungsrecht-pruefer: Konsolidiertes Skill-Kompendium 24; bündelt 1 frühere Spezialskills (zweckverfehlung-und-kondiktionszweck) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `output-anfechtungsanzeige-insolvenzverwalter` | Anschreiben des Insolvenzverwalters an den Anfechtungsgegner erstellen: Rückgewähr nach §§ 129 ff. und § 143 InsO, Tatbestand transaktionsscharf benennen, § 142- und § 144-Hinweise, Zinsen nur bei Verzug oder § 291 BGB, Verjährung § 146... |
| `output-anfechtungsklage-anfg` | Klageschrift für AnfG-Anfechtungsklage des Vollstreckungsgläubigers aufbauen: Rubrum, Duldungsantrag, Begründungsstruktur. Normen: §§ 2 11 13 AnfG. Prüfraster: Antragsformulierung, Begründungsaufbau Anfechtungstatbestand, Streitwertangab... |
| `output-klageschrift-bereicherungsklage` | Klageschrift aus Bereicherungsrecht §§ 812 ff. BGB aufbauen: Klageantrag auf Zahlung oder Herausgabe, ODUE-Schema. Normen: §§ 812 818 BGB, §§ 253 313 ZPO. Prüfraster: Obersatz, Definition, Untersatz, Ergebnis, Streitwert, Beweisangebot.... |
| `output-warnhinweis-und-pruefungsdokument` | Pflicht-Header und Warnblock für alle Prüfungsdokumente generieren: kein Rechtsrat, nur mechanische Prüfung. Normen: BRAO § 3. Prüfraster: Warnhinweis, Haftungsausschluss, Hinweis auf unvollständige Sachverhalte. Output: Standardisierter... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
