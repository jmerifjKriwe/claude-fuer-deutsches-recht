---
name: deal-intake
description: "Neues Transaktionsmandat strukturiert aufnehmen aus E-Mail, Teaser, NDA, Term Sheet, Teams-Message oder DR-Einladung. Anwendungsfall: Erster Mandantenkontakt oder Deal-Beauftragung eingetroffen. Normen: BRAO § 43a, GwG §§ 10 ff. (KYC), WpHG/MAR Insider-Register. Prüfraster: Parteienerfassung, Dea"
---

# Deal-Intake

## Aktenstart statt Formularstart

Wenn zu **Deal Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Corporate Kanzlei** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Deal-Intake

- **Corporate-Aufgabe (Deal-Intake):** Erster Mandantenkontakt oder Deal-Beauftragung eingetroffen.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Deal-Intake und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das aus Sicht der Gesellschaft, Geschäftsführung, Gesellschafter oder Inhouse-Rechtsabteilung."
- "Mach daraus eine Beschlussvorlage, Partnernotiz, Mandantenmail oder Organunterlage."
- "Welche Register-, Beschluss-, Compliance- oder Fristpunkte fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst die Gesellschaftsakte selbst angelegt, die Mandatsrolle bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/corporate-kanzlei:corporate-kanzlei-kommandocenter` oder `/corporate-kanzlei:corporate-kanzlei-matter-file`. Wenn der Nutzer nur eine Kurzfassung für interne Abstimmung will, arbeite bewusst kürzer und liefere keine lange Prüfarchitektur.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/corporate-kanzlei/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Gesellschaft, Rechtsform, Rolle, Organstatus, Beschluss-/Registerlage, Frist, gewünschter Output und ob börsen-, konzern- oder regulierungsrelevante Bezüge bestehen.

Benötigte Unterlagen:
- Mandats-/Gesellschaftsprofil, Organigramm, Rollenmatrix und Eskalationskette.
- Kommunikationskanäle, Vertraulichkeitsstufen, Review-Gates und Beschlusskalender.
- Vorlagen für Board Paper, Beschlussvorlage, Statusbericht und Billing Narrative.

Arbeite mit diesen Variablen: `gesellschaft`, `rolle`, `organ`, `beschlussdatum`, `registerstand`, `frist_oder_closing`, `materiality_threshold`, `owner`, `source_tag`.

## Workflow
1. **Corporate-Kontext fixieren.** Bestimme Gesellschaft, Rechtsform, Organrolle, Anlass, Beschluss-/Registerstand und Entscheidungsempfänger. Wenn Rolle oder Rechtsform fehlen, frage genau eine Rückfrage; bei Fristdruck arbeite mit `[Annahme - prüfen]` weiter.
2. **Quellen inventarisieren.** Liste Dokumente mit Datum, Version, Quelle, Register-/Urkunden-ID und Vertraulichkeitsstufe. Markiere Uploads als `[Mandant]`, Register als `[Register]`, Gerichts-/Behördenquellen als `[Primärquelle]` und Modellwissen als `[Modellwissen - prüfen]`.
3. **Organ- und Kompetenzebene trennen.** Unterscheide Geschäftsführung/Vorstand, Gesellschafterversammlung/Hauptversammlung, Aufsichtsrat/Beirat, Konzernleitung, Notar und Registergericht.
4. **Materiality-Schwelle setzen.** Fehlt eine Vorgabe, arbeite mit Ampel: Nichtigkeit/Unwirksamkeit, Anfechtungs-/Haftungsrisiko, Registerhindernis, Zustimmungserfordernis, Housekeeping.
5. **Normenprüfung durchführen.** Prüfe die unten genannten Normgruppen bezogen auf den konkreten Corporate-Schritt: Zuständigkeit, Form, Frist, Mehrheit, Vollmacht, Registerfähigkeit, Haftung und Beweisquelle.
6. **Belegkette bauen.** Jede wesentliche Aussage braucht Quelle, Dokument, Fundstelle und Unsicherheitsmarker. Keine Fundstelle erfinden. Wenn Registerauszug, BGH-/EuGH-Entscheidung oder Behördenpraxis nicht abrufbar ist, steht `[zu verifizieren]`.
7. **Risikomatrix erstellen.** Gib pro Punkt aus: Sachverhalt, Rechtsfrage, Norm, Subsumtion, Risikoampel, Rechtsfolge, empfohlene Aktion, Owner, Deadline und Folge-Skill.
8. **Draft oder Review-Gate wählen.** Wenn die Tatsachen reichen, liefere den gewünschten Output. Wenn nicht, liefere eine Information-Request-Liste oder eine Partner-/Organvorlage mit genau den offenen Entscheidungen.
9. **Hand-off vorbereiten.** Überführe Findings in Beschlussentwurf, Board Paper, Registeranmeldung, SPA-Markup, CP-Tracker, Mandantenmail oder Closing Bible. Verweise auf den konkreten Anschluss-Skill unten.
10. **Abschlusskontrolle.** Prüfe: keine ungeprüften Aktenzeichen, keine BeckRS-Blindzitate, keine automatische Außenkommunikation, keine vertraulichen Informationen außerhalb des Need-to-know-Kreises.

## Prüfraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Corporate-Schritt gesellschaftsrechtlich wirksam, registerfähig, organschaftlich vertretbar und für die Mandatsseite praktisch umsetzbar ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird: Gesellschaft, Organmitglied, Gesellschafter, Investor, Käufer, Verkäufer oder Konzernmutter. Ist die Rolle unklar, darf kein parteilicher Beschluss-, Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Zuständigkeit, Form und Corporate Authority.** Bei Anteils-, Beschluss- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Mehrheit, Form und Registerlage zu prüfen. Relevanter Kern:
- BRAO § 43a, BORA § 3 und BRAO § 49b für Verschwiegenheit, Konflikt und Honorar.
- GwG §§ 10 ff. für Mandatsannahme und wirtschaftlich Berechtigte.
- DSGVO Art. 5, 6, 25 und 32 für Datenminimierung, Rollen und Sicherheit.
- BGB §§ 611a, 675 und 280 für Beratungs- und Haftungsrahmen.

**3. Organpflichten und Business Judgment.** Bei Geschäftsleitungs-, Aufsichtsrats- oder Beiratsentscheidungen ist zu fragen, ob die Entscheidung auf angemessener Informationsgrundlage, ohne sachfremde Interessen und zum Wohl der Gesellschaft vorbereitet ist. Für Organverantwortung: BGH, 21.04.1997 - II ZR 175/95, ARAG/Garmenbeck, https://dejure.org/1997,161 `[dejure.org]`.

**4. Register- und Gesellschafterlistenlogik.** Bei GmbH-Anteilen, Einziehung, Vollmachtskette oder Beschlussfähigkeit ist § 16 GmbHG gesondert zu prüfen. Zur Legitimationswirkung der Gesellschafterliste: BGH, 20.11.2018 - II ZR 12/17, https://dejure.org/2018,47817 `[BGH-Datenbank/dejure.org]`.

**5. Vollzugshindernisse.** Wenn Fusionskontrolle, AWV/FDI, MAR, GwG, Sanktionen, Bankzustimmung, Satzungszustimmung oder branchenspezifische Genehmigungen berührt sind, muss das Ergebnis lauten: Anmeldung erforderlich? Vollzugsverbot? Registerhindernis? Beschlussmangel? Long-Stop-Date gefährdet? Bußgeld-, Nichtigkeits- oder Haftungsfolge?

**6. Subsumtion.** Subsumtion erfolgt dokumentennah. Beispiel: `§ 15 GmbHG notarielle Form erfüllt?` nur bejahen, wenn Entwurf/Urkunde/Notarbestätigung vorliegt. `§ 46 GmbHG Zustimmung erforderlich?` nur bejahen, wenn Satzung, Geschäftsordnung und Maßnahme geprüft sind.

**Zwischenergebnis:** Formuliere als Ampel: grün mit Beleg, gelb mit offener Information, rot mit Handlungssperre. Rot bedeutet im Corporate-Kontext: nicht beschließen, nicht anmelden, nicht signieren, nicht closen oder nicht extern versenden, bevor Partner, Organ oder Spezialist freigegeben hat.

## Output-Module
- **Corporate-Vermerk:** Kurzbild, Sachverhalt, Normen, Subsumtion, Risikoampel, Empfehlung.
- **Beschluss-/Board-Paper-Modul:** Zuständigkeit, Beschlussvorschlag, Informationsgrundlage, BJR-Dokumentation, Anlagenliste.
- **Issue List:** Finding, Quelle, Risiko, Rechtsfolge, Register-/Vertragsfolge, Owner, Deadline.
- **Information Request:** konkrete Fragen an Mandant, Organ, Notar, Registerteam, Steuerberater oder Gegenseite.
- **Matter-Update:** kurzer Eintrag für `history.md` und ggf. Frist-/Owner-Eintrag für `fristen.yaml`.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen und Zitierregel
Nutze nur frei prüfbare Quellen oder vom Nutzer bereitgestellte/lizenzierte Quellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und Link auf `dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu` oder `eur-lex.europa.eu`. Keine BeckRS-Alleinzitate, keine anwalt24-Belege, keine erfundenen Randnummern. Quellen-Tags: `[Mandant]`, `[Register]`, `[BGH-Datenbank]`, `[dejure.org]`, `[EUR-Lex]`, `[Web-Recherche - prüfen]`, `[Modellwissen - prüfen]`.

## Hand-Off zu anderen Skills
Nach diesem Skill weiter mit:
- `/corporate-kanzlei:corporate-kanzlei-matter-file` - wenn Gesellschaftsprofil, Workstreams, Fristen und Dokumentenlog in eine laufende Akte geschrieben werden sollen.
- `/corporate-kanzlei:corporate-kanzlei-kommandocenter` - wenn mehrere Corporate-Workstreams konkurrieren und der nächste Primärpfad neu bestimmt werden muss.
- `/corporate-kanzlei:corporate-kanzlei-steps-plan-pmo` - wenn Termine, Beschlüsse, CPs, Freigaben und Owner in einen belastbaren Plan müssen.
- `/corporate-kanzlei:corporate-kanzlei-datenraum-aufbau` - wenn Dokumente, Datenraumlücken oder Clean-Room-Fragen der nächste Engpass sind.

## Was dieser Arbeitsgang nicht macht
- Er ersetzt keine Partner-, Organ- oder Mandantenentscheidung über Beschluss, Signing, Registeranmeldung oder Closing.
- Er führt keine automatische Außenkommunikation an Gegenseite, Behörde, Notar, Registergericht, Datenraumteilnehmer oder Mandant aus.
- Er behauptet keine Registerlage, Behördenpraxis oder Rechtsprechung ohne prüfbare Quelle.
- Er vermischt nicht Corporate-Befund, Vertragsrisiko und wirtschaftliche Bewertung; diese Ebenen bleiben getrennt.
- Er trifft keine steuerliche, kartellrechtliche, sanktionsrechtliche oder ausländische Rechtsaussage final ohne Spezialisten-Review.
- Er behandelt vertrauliche Daten nur innerhalb des Need-to-know-Kreises und markiert sensible Informationen für Clean-Room oder Insiderlisten.

## Berufsrechtliche Hinweise
Vor Mandatsarbeit sind Interessenkonflikte nach § 43a BRAO und § 3 BORA, Verschwiegenheit nach § 43a Abs. 2 BRAO, Vergütungsrahmen nach § 49b BRAO und GwG-Sorgfaltspflichten zu beachten. Bei personenbezogenen Daten gelten DSGVO Art. 5, 6, 25 und 32. Bei Drittakten, Datenräumen, Akteneinsicht oder Clean-Room-Material ist der Zweckbindungsrahmen zu prüfen; Material aus einem Mandat darf nicht stillschweigend in ein anderes Mandat übernommen werden.

## Bisheriger Skill-Kern, integriert und weiterzuverwenden

### Deal-Intake

## Triage — klaere zu Beginn

1. Welche Art Transaktion: Share Deal, Asset Deal, Merger, Squeeze-Out, IPO, Carve-Out?
2. Mandant: Kaeufer oder Verkaefer? (Perspektive des Skill-Aufrufs)
3. Gibt es bereits ein NDA / Confidentiality Agreement? Falls nein: sofort anlegen.
4. Sind Insiderinformationen im Spiel? → MAR-Pflichten prüfen (WpHG § 13); Insider-Log anlegen.
5. Konfliktpruefung: Bestehende Mandate aller Parteien und Affiliates checken.
6. GwG-CDD: Wirtschaftlich Berechtigte, PEP, Sanktionen — vor erster Mandatstaetigkeit.
7. Jurisdiktionen: Nur Deutschland oder multinational (dann zusaetzliche Praxis-Regeln)?

## Zentrale Normen

- **§§ 43, 45 BRAO** — Interessenkollision und Verschwiegenheitspflicht; Pflicht zur Konfliktpruefung
- **§§ 2, 10-17 GwG** — Geldwaeschepraevention; CDD vor Annahme; wirtschaftlich Berechtigter
- **Art. 18 MAR / § 13 WpHG** — Insiderliste; Ad-Hoc-Pflicht; Marktmissbrauch; vertrauliche Behandlung
- **§§ 3-5 BORA** — Berufspflichten; Interessenwiderstreit; Need-to-know
- **§ 675 BGB** — Mandate als Dienstvertrag; Pflicht zur vollstaendigen Information des Mandanten

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Deal-Intake-Checkliste

### A. Erste Informationen sichern

| Punkt | Inhalt | Status |
|---|---|---|
| Parteien | Kaeufer, Verkaefer, Zielgesellschaft (vollstaendige Firmennamen, Sitz, Rechtsform) | |
| Deal-Typ | Share Deal / Asset Deal / Merger / IPO / Squeeze-Out | |
| Jurisdiktionen | Hauptsitz, Tochtergesellschaften, Governing Law SPA | |
| Zeitplan | Signing-Ziel; Long Stop Date; exklusive Phase | |
| Volumen | Transaktionsvolumen; EV/Equity Value — vertraulich | |
| Berater-Team | Investmentbank, Steuerberater, andere Kanzleien | |
| Ansprechpartner | Name, Funktion, E-Mail, Mobilnummer | |

### B. Compliance-Checks

| Check | Ergebnis | Datum |
|---|---|---|
| Konfliktpruefung (§ 43a BRAO) | Frei / Konflikt: [Beschreibung] | |
| GwG-CDD | Wirtschaftl. Berechtigter identifiziert; PEP: Ja/Nein; Sanktionen: Frei | |
| Insider-Prüfung (MAR) | Insiderinformation: Ja/Nein; Insider-Log angelegt: Ja/Nein | |
| Clean-Room-Anforderung | Ja/Nein; wenn Ja: Clean-Team-Protokoll | |
| NDA unterzeichnet | Datum; Parteien | |

## Schritt-für-Schritt-Workflow

1. **Erstgesprach / Erstkontakt** — Deal-Parameter erfassen; Vertraulichkeit sicherstellen
2. **Konfliktpruefung** — alle Parteien und bekannte Affiliates im Konfliktsystem prüfen; Senior Partner entscheidet
3. **GwG-CDD anlegen** — Identifizierung wirtschaftlich Berechtigter; PEP-Check; Mittelherkunft
4. **Insider-Log anlegen** — bei borsennotierter Gesellschaft: MAR-konformes Insider-Log; Need-to-know-Liste
5. **Akte anlegen** — Deal-Name, Matter-Nummer, Aktenstruktur, Zugriffsrechte
6. **IRL aufstellen** — erste Information Request List nach Workstreams
7. **Teamzusammenstellung** — federführender Partner, Senior Associate, Junior; Budget-Freigabe
8. **NDA sichern** — falls nicht vorhanden: Standardform schicken; kein Informationsaustausch vorher
9. **Kick-Off-Call** — Agenda, Zeitplan, Workstreams, erste Informationslieferung

## Entscheidungsbaum: Insider-Pflichten

```
Zielgesellschaft borsennotiert oder Konzernteil einer Boersengesellschaft?
 → Ja: Insiderinformation vorhanden?
 → Ja: Insider-Log anlegen (Art. 18 MAR); Ad-Hoc ggf. erforderlich
 → Vertraulichkeit von Mandant einfordern (NDA/MAR-Pflicht)
 → Nein: laufend pruefen; Transaktionsbekanntgabe kann Insiderinformation werden
 → Nein: GwG-Standard-CDD; keine MAR-Pflichten im engeren Sinne
 → aber: Marktmanipulation (Art. 12 MAR) auch bei nicht-borsennotierten moeglich
```

## Output-Template Deal-Karte

**Adressat:** Deal-Team intern — Tonfall praegnant, strukturiert

```
DEAL-KARTE
Deal-Name: [CODENAME]
Matter-Nr.: [NUMMER]
Datum: [DATUM]
Vertraulichkeit: [Streng vertraulich / Need-to-know]

PARTEIEN:
Kaeufer: [NAME, Sitz, Rechtsform]
Verkaefer: [NAME, Sitz, Rechtsform]
Zielgesellschaft: [NAME, Sitz, HRB-Nr., Rechtsform]

DEAL-TYP: [Share Deal / Asset Deal / Merge / IPO]
TRANSAKTIONSVOLUMEN: ca. [EUR] (streng vertraulich)
GOVERNING LAW: [Deutsches Recht / Englisches Recht]

TIMELINE:
Signing-Ziel: [DATUM]
Closing-Ziel: [DATUM]
Long Stop Date: [DATUM]

COMPLIANCE-STATUS:
Konfliktpruefung: [Frei | Konflikt: ...]
GwG-CDD: [Vollstaendig | Ausstehend: ...]
Insider-Log: [Angelegt | Nicht erforderlich]

DEAL-TEAM:
Federf. Partner: [NAME]
Senior Associate: [NAME]
Junior: [NAME]
Budget: [EUR]

NÄCHSTE AKTION: [konkrete Aktion] — Verantwortlich: [Name] — Frist: [Datum]
```

## Rote Schwellen

- Konfliktpruefung nicht vor Mandatsannahme → § 43a BRAO; sofortige Niederlegung; Schadensersatz
- Insiderinformation ohne Log und Vertraulichkeitssicherung → Art. 14 MAR; Bussgeld
- GwG-CDD unvollstaendig → § 17 GwG; Ordnungswidrigkeit; Behördenverfahren
- NDA nicht unterzeichnet vor Informationsaustausch → vertrauliche Daten ungeschuetzt
- Akte ohne Zugriffsschutz → Clean-Room-Erfordernis missachtet

## Quellen

- §§ 43, 43a, 45 BRAO; §§ 2-17 GwG; Art. 18 MAR; § 13 WpHG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Literatur nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle; keine Kommentarblindzitate.
