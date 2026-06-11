# Megaprompt: gewerblicher-rechtsschutz

> *Achtung: Dies ist ein experimentelles Mega-Prompt-Markdown, das einen kompletten Klotzkette-Plugin in eine einzige Datei zusammenfuehrt. Keine Haftung, keine Gewaehr. Nur zum Ausprobieren der Skills auch ohne Claude Code; keine Rechtsberatung. Vor Verwendung im Mandat anwaltlich pruefen.*
>
> *Caution: This is an experimental Mega-Prompt Markdown that consolidates a full Klotzkette plugin into a single file. No warranty, no liability. For exploration with chat tools that do not run Claude Code only; not legal advice.*

**Verwendung:** Diesen gesamten Text in einen Chat ohne Claude-Code-Integration einfuegen (oder als Datei hochladen). Der Chat-Agent erhaelt damit die gebuendelten Skills dieses Plugins als Kontext. Eine Replikation des vollen Plugin-Verhaltens ist nicht garantiert — der Megaprompt ist eine Best-Effort-Kompression.


## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 62 Skills des Plugins `gewerblicher-rechtsschutz`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Gewerblicher Rechtsschutz (allgemein): ordnet Rolle (Schutzrechtsinhaber, Verletzer, Ko…
2. **mandat-triage-gewerblicher-rechtsschutz** — Neues Mandat im gewerblichen Rechtsschutz: Anwalt klaert welches Sachgebiet und welche Skills benoetigt werden. Eingangs…
3. **gw-einfuehrung-gw-einstweilige-mandat-triage** — Einführung in die Rechtsschutzwege des gewerblichen Rechtsschutzes: Überblick über Verfahrensarten, Zuständigkeiten, Han…
4. **gewerblicher-erstpruefung-und-mandatsziel** — Erstprüfung und Mandatszielbestimmung im gewerblichen Rechtsschutz: strukturiertes Erstgespräch, Rollen- und Interessenk…
5. **abmahnung-urheberrecht-erfindungsmeldung** — Urheber oder Lizenznehmer erhielt unerlaubte Nutzung (Bild Text Video) oder Mandant erhielt Abmahnung wegen Urheberrecht…
6. **erfindungsmeldung-aufnahme** — Mitarbeiter meldet eine Erfindung oder Unternehmen prüft eingegangene Erfindungsmeldung. ArbnErfG Arbeitnehmererfindungs…
7. **fto-triage-gewerblicher-rechtsschutz-mandat** — Unternehmen will Produkt einführen oder Technologie einsetzen und fragt: Verletzen wir fremde Patente? Freedom-to-Operat…
8. **ip-klausel-pruefung** — Anwalt prüft Vertrag auf IP-Klauseln (Übertragung Lizenz Inhaberschaft Freistellung) oder Mandant fragt nach Risiken. IP…
9. **mandat-arbeitsbereich** — Kanzlei mit mehreren Mandanten im gewerblichen Rechtsschutz muss Kontext zwischen Mandaten strikt trennen. Mandatsverwal…
10. **markenrecherche** — Unternehmen oder Mandant plant neue Marke oder Produktname und fragt: Bestehen Kollisionsrisiken mit aelteren Marken? Ma…
11. **schutzrechts-portfolio-schutzschrift** — Unternehmen oder Kanzlei muss IP-Portfolio verwalten und anstehende Fristen im Blick behalten. Schutzrechtsportfolio-Ver…
12. **schutzschrift-eilverfuegung** — Mandant hat Abmahnung oder Verletzungsschreiben erhalten und befürchtet einstweilige Verfuegung ohne Anhörung. § 945a ZP…
13. **start-chronologie-fristen** — Einstieg, Schnelltriage und Fallrouting im Gewerblicher Rechtsschutz-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Ris…
14. **streitwert-igr-berechnen** — Anwalt muss Streitwert für IP-Verletzungsklage oder einstweilige Verfuegung im gewerblichen Rechtsschutz festlegen. Stre…
15. **takedown-anweisung-unterlassungsverlangen** — Rechteinhaber findet urheberrechtsverletzende Inhalte online oder erhielt selbst eine Meldung als Hostprovider. Notice-a…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Gewerblicher Rechtsschutz (allgemein): ordnet Rolle (Schutzrechtsinhaber, Verletzer, Konkurrent), markiert Frist (Markenwiderspruch 3 Monate), wählt Norm (MarkenG, PatG, GeschmMG, GebrMG, UrhG, UWG) und Zuständigkeit (DPMA), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Gewerblicher Rechtsschutz** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `abmahnung-compliance-dokumentation-und-akte` — Abmahnung Compliance Dokumentation und Akte
- `abmahnung-urheberrecht-erfindungsmeldung` — Abmahnung Urheberrecht Erfindungsmeldung
- `anmeldung-spezial-compliance-euipo` — Anmeldung Spezial Compliance Euipo
- `anpassen` — Anpassen
- `compliance-mandantenkommunikation-entscheidungsvorlage` — Compliance Mandantenkommunikation Entscheidungsvorlage
- `dpma-fristen-form-und-zustaendigkeit` — Dpma Fristen Form und Zustaendigkeit
- `erfindungsmeldung-aufnahme` — Erfindungsmeldung Aufnahme
- `euipo-dokumentenmatrix-und-lueckenliste` — Euipo Dokumentenmatrix und Lueckenliste
- `evvollzug-auslandszustellung-ev-abmahnung` — Evvollzug Auslandszustellung EV Abmahnung
- `evvollzug-neu-001-einstweilige-verfuegung-vollziehung-frist` — Evvollzug NEU 001 Einstweilige Verfuegung Vollziehung Frist
- `evvollzug-neu-002-urteilsverfuegung-beschlussverfuegung-und-zust` — Evvollzug NEU 002 Urteilsverfuegung Beschlussverfuegung und Zust
- `evvollzug-neu-004-bea-zustellung-einstweiliger-rechtsschutz-risi` — Evvollzug NEU 004 BEA Zustellung Einstweiliger Rechtsschutz Risi
- `evvollzug-neu-005-ordnungsmittelantrag-vollstreckung-unterlassun` — Evvollzug NEU 005 Ordnungsmittelantrag Vollstreckung Unterlassun
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Gewerblicher Rechtsschutz sind UWG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `mandat-triage-gewerblicher-rechtsschutz`

_Neues Mandat im gewerblichen Rechtsschutz: Anwalt klaert welches Sachgebiet und welche Skills benoetigt werden. Eingangs-Triage IP-Recht. Prüfraster: Mandantenrolle (Schutzrechtsinhaber Verletzer Lizenznehmer) Sachgebiet (Marke Patent Design Urheber UWG) Sofort-Fristen (einstweilige Verfuegung Dr..._

# Mandat-Triage Gewerblicher Rechtsschutz

## Aktenstart statt Formularstart

Wenn zu **Mandat Triage Gewerblicher Rechtsschutz** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Gewerblicher Rechtsschutz** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Ablauf — sieben Fragen

### Frage 1 — Mandantenrolle?

- Schutzrechts-Inhaber (offensiv)
- Verletzer (defensiv)
- Mitbewerber (UWG)
- Lizenznehmer / Lizenzgeber
- Designer / Erfinder / Künstler
- Plattform-Betreiber

### Frage 2 — Schutzrechts-Art?

- Marke (Wortmarke Bildmarke Wort-Bild-Kombination 3D Hörmarke)
- Patent / Gebrauchsmuster
- Design / Geschmacksmuster
- Urheberrecht
- Verwertungs-Schutz / GEMA / VG Wort / VG Bild-Kunst
- Wettbewerbsrecht (UWG)
- Lauterkeitsrecht
- Geschäftsgeheimnisse (GeschGehG)
- Domain-Recht

### Frage 3 — Vorgang?

- Schutzrechts-Anmeldung
- Verletzungs-Verfahren (offensiv defensiv)
- Lizenz-Verhandlung
- Lizenz-Streit
- Löschungsverfahren (DPMA EUIPO)
- Einspruch
- Nichtigkeits-Klage Patent
- Open-Source-Compliance
- FTO (Freedom-to-Operate)
- Abmahnung erhalten / vorzubereiten
- Zoll-Beschlagnahme (TRIPS)

### Frage 4 — Akute Eilbedürftigkeit?

- **Einstweilige Verfügung** zugestellt / erlassen
- **Abmahnung** mit kurzer Frist
- **Messe / Produkt-Launch** binnen Tagen
- **Anhörung beim Patentamt**
- **Dringlichkeit** für eigenes EV-Verfahren — typisch ein Monat ab Kenntnis (München) bzw. zwei Monate (Hamburg)
- **Zollbeschlagnahme** läuft

### Frage 5 — Schutzrechts-Status?

- Angemeldet / registriert (mit Aktenzeichen Datum)
- Schutzrechts-Inhaber identifiziert
- Lizenzkette geklärt
- Aktiv-/Passivlegitimation

### Frage 6 — Frist?

- **EV-Dringlichkeit** Senat-Spezifisch (München ein Monat Hamburg / Berlin zwei Monate Frankfurt ein bis zwei Monate Düsseldorf länger)
- **Klage-Frist nach EV-Erlass** § 926 ZPO Aufforderung
- **Markenanmeldung-Prioritätsfrist** sechs Monate § 34 MarkenG
- **Patent-Prioritätsfrist** zwölf Monate Art. 4 PVÜ
- **Widerspruch Marken** drei Monate § 42 MarkenG
- **Patent-Einspruch** neun Monate § 59 PatG
- **Nichtigkeitsklage Marken** vier Monate nach Eintragung; danach jederzeit aber Verwirkung
- **Verjährung Verletzungs-Schadensersatz** sechs Jahre § 21 MarkenG bzw. drei Jahre § 195 BGB Standard

### Frage 7 — Wirtschaftliche Verhältnisse?

- Schutzrecht-Wert
- Versicherungs-Deckung (selten — Spezial-Versicherung gewerblicher Rechtsschutz)
- Streitwert hoch
- Sicherheitsleistung erforderlich bei EV
- Honorarvereinbarung statt RVG fast immer

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Markenrecherche | `markenrecherche` |
| Markenanmeldung DPMA | `markenanmeldung-dpma` |
| Schutzrechts-Portfolio | `schutzrechts-portfolio` |
| Erfindungsmeldung Aufnahme | `erfindungsmeldung-aufnahme` |
| FTO Freedom to Operate | `fto-triage` |
| IP-Klausel Vertrag | `ip-klausel-pruefung` |
| Open Source Prüfung | `open-source-pruefung` |
| Verletzungs-Triage | `verletzungs-triage` |
| Abmahnung Urheber | `abmahnung-urheberrecht` |
| Takedown-Anweisung | `takedown-anweisung` |
| Unterlassungsverlangen | `unterlassungsverlangen` |
| Streitwert-Bestimmung | `streitwert-igr-berechnen` |
| UWG-Wettbewerbsrecht | (Skill uwg-verstoss-pruefen — perspektivisch) |
| Patent-Nichtigkeit | (Skill patent-nichtigkeit — perspektivisch) |
| Geschäftsgeheimnis GeschGehG | (Skill geschäftsgeheimnis — perspektivisch) |

## Mandatsannahme

- **Konflikt-Check** sehr strikt — bei Mitbewerbern in selber Branche schwierig
- **Streitwert** typisch sechs- bis siebenstellig
- **Honorarvereinbarung** RVG häufig nicht ausreichend
- **Sachverständigen-Bedarf** technisch bei Patent / Design

## Eskalation

- **Telefon-Sofort** einstweilige Verfügung erlassen Zollbeschlagnahme
- **Binnen einer Stunde** Schutzschrift erforderlich Dringlichkeit verstreicht
- **Heute** Abmahnung vorbereiten Markenrecherche
- **Diese Woche** Anmeldung DPMA Schutzschrift gemäß § 945a ZPO

## Ausgabe

- `triage-protokoll-igr.md`
- Aktenanlage
- Frist im Fristenbuch (EV-Dringlichkeit hoch priorisiert)
- Streitwert-Vorabschätzung
- Senat-Empfehlung bei Konkurrenzzuständigkeit
- Mandatsvereinbarung mit Honorarvereinbarung
- Empfehlung Folge-Skill

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellen

- MarkenG PatG GebrMG DesignG UrhG GeschGehG UWG
- ZPO §§ 921 945a 926 940
- GKG §§ 39 47 51
- BGH I. Zivilsenat X. Zivilsenat
- Ingerl/Rohnke MarkenG
- Benkard PatG
- Koehler/Feddersen UWG

---

## Skill: `gw-einfuehrung-gw-einstweilige-mandat-triage`

_Einführung in die Rechtsschutzwege des gewerblichen Rechtsschutzes: Überblick über Verfahrensarten, Zuständigkeiten, Handlungsoptionen und Weichen bei Marken-, Patent-, Design-, Urheber- und Lauterkeitsverletzungen. Erstes Orientierungsgespräch und Triage im Gewerblicher Rechtsschutz._

# GewR: Einführung – Rechtsschutzwege im Überblick

## Aktenstart statt Formularstart

Wenn zu **Gw Einfuehrung Gw Einstweilige Mandat Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Gewerblicher Rechtsschutz** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck und Mandatsbezug

Liefert eine **strukturierte Einführung in die Rechtsschutzwege des gewerblichen Rechtsschutzes** und dient als erstes Orientierungsgespräch. Er sortiert den Sachverhalt nach Rechtsgebiet, Verfahrensart und strategischer Priorität und zeigt, welche konkreten Handlungsoptionen offenstehen. Er ist der Ausgangspunkt vor dem Einsatz spezialisierter Skills.

Mandatsbezug: Mandant kommt mit einem IP-Problem, weiß aber nicht, ob er klagen, abmahnen, anmelden oder nur prüfen lassen soll. Oder: Anwalt übernimmt neues Mandat und braucht eine erste systematische Einordnung.

## Überblick: Materielle Rechtsgebiete

### 1. Markenrecht (MarkenG, EUTMR)

- **Schutzgegenstand:** Kennzeichen (Wort, Bild, 3D, Ton, Farbe) mit Unterscheidungskraft.
- **Eingetragene Marke:** DPMA (national), EUIPO (EU), WIPO/Madrid (international).
- **Nicht eingetragene Rechte:** Unternehmenskennzeichen (§ 5 MarkenG), geografische Angaben (§ 126 ff. MarkenG).
- **Kernverletzungen:** Verwechslungsgefahr (§ 14 Abs. 2 Nr. 2 MarkenG), Ausnutzung/Beeinträchtigung bekannter Marke (Nr. 3).

### 2. Patentrecht und Gebrauchsmuster (PatG, GebrMG)

- **Schutzgegenstand:** Technische Erfindungen (Patent) oder Gebrauchsmuster (ohne Prüfung).
- **Anmeldewege:** DPMA, EPA, PCT (international).
- **Kernverletzungen:** Benutzung der geschützten Lehre (§ 9 PatG).
- **Arbeitnehmererfindungen:** ArbnErfG – besondere Pflichten des Arbeitgebers.

### 3. Designrecht (DesignG, GGV)

- **Schutzgegenstand:** Äußere Erscheinungsform eines Erzeugnisses (Formgebung).
- **Eingetragen:** DPMA, EUIPO.
- **Nicht eingetragenes Gemeinschaftsgeschmacksmuster:** 3-Jahres-Schutz, entsteht automatisch.
- **Kernverletzungen:** Herstellung identischer/ähnlicher Produkte (§ 38 DesignG).

### 4. Urheberrecht (UrhG)

- **Schutzgegenstand:** Werke der Literatur, Wissenschaft, Kunst; entsteht ohne Anmeldung.
- **Schutzrechte:** Urheberpersönlichkeitsrechte, Verwertungsrechte (§§ 15 ff. UrhG).
- **Kernverletzungen:** Unerlaubte Vervielfältigung (§ 16 UrhG), öffentliche Zugänglichmachung (§ 19a UrhG).
- **Besonderheit:** Lichtbildwerke, Datenbankwerke, Computerprogramme.

### 5. Lauterkeitsrecht (UWG)

- **Schutzgegenstand:** Lauter Wettbewerb; kein Ausschließlichkeitsrecht.
- **Anspruchsberechtigte:** Mitbewerber, Verbände (§ 8 Abs. 3 UWG).
- **Kerntatbestände:** Irreführung (§§ 5, 5a UWG), Nachahmung (§ 4 Nr. 3 UWG), Rechtsbruch (§ 3a UWG).

## Überblick: Verfahrensarten und Rechtsschutzwege

### Außergerichtlich

| Verfahren | Beschreibung | Ziel |
|---|---|---|
| Abmahnung | Aufforderung zur Unterlassung mit Unterlassungserklärung | Schnelle Einigung ohne Gericht |
| Schutzschrift | Präventive Gegendarstellung beim ZSSR | Beschlussverfügung verhindern |
| Unterlassungserklärung | Modifizierte oder vollständige Annahme | Wiederholungsgefahr ausräumen |
| DPMA-Widerspruch | Gegen eingetragene Marke (§ 42 MarkenG) | Marke löschen |
| EUIPO-Widerspruch | Gegen Unionsmarke (Art. 46 EUTMR) | Unionsmarke anfechten |

### Gerichtlicher Eilrechtsschutz

| Verfahren | Norm | Beschreibung |
|---|---|---|
| Einstweilige Verfügung (Beschluss) | §§ 935, 937 Abs. 2 ZPO | Sofortiger Unterlassungstitel ohne mündliche Verhandlung |
| Einstweilige Verfügung (Urteil) | §§ 935, 922 ZPO | EV nach mündlicher Verhandlung |
| Arrest | § 916 ZPO | Sicherung von Geldforderungen |

### Ordentliches Gerichtsverfahren

| Verfahren | Beschreibung |
|---|---|
| Unterlassungsklage | Dauerhafter Unterlassungstitel |
| Schadensersatzklage | Ersatz eingetretener Schäden |
| Auskunftsklage | Informationserzwingung (§ 140b PatG, § 19 MarkenG) |
| Lizenzbereitschaftserklärung (FRAND) | Kartellrechtlicher Sonderweg bei SEP |

### Verwaltungsverfahren (Amtsverfahren)

| Verfahren | Zuständigkeit | Beschreibung |
|---|---|---|
| DPMA-Widerspruch/Löschung | DPMA | Marke anfechten |
| DPMA-Nichtigkeitsverfahren | DPMA | Patent/Design anfechten |
| BPatG-Beschwerde | Bundespatentgericht | Gegen DPMA-Entscheidung |
| EUIPO-Widerspruch/Löschung | EUIPO | Unionsmarke anfechten |
| WIPO-UDRP | WIPO | Domain-Name-Streit |

## Kaltstart-Triage in 5 Schritten

### Schritt 1 – Schutzrecht identifizieren
- Liegt ein eingetragenes Schutzrecht vor (Marke, Patent, Design)?
- Liegt ein nicht eingetragenes Recht vor (Urheberrecht, Unternehmenskennzeichen, GGM)?
- Oder handelt es sich um einen UWG-Anspruch ohne Schutzrecht?

### Schritt 2 – Verfahrensziel klären
- Unterlassung (sofort)? → Abmahnung, EV.
- Schadensersatz? → Auskunft, dann Klage.
- Schutzrecht vernichten? → Widerspruch, Löschungsantrag.
- Eigene Position sichern? → Freedom-to-Operate, Schutzschrift.

### Schritt 3 – Dringlichkeit einschätzen
- Verletzung akut und fortlaufend? → Sofortige EV-Vorbereitung.
- Verletzung entdeckt, nicht mehr akut? → Abmahnung, dann ggf. Klage.
- Droht Verletzung erst? → Schutzschrift, Unterlassungsklage wegen Erstbegehungsgefahr.

### Schritt 4 – Beweislage prüfen
- Schutzrechtsurkunde, Registerauszug vorhanden?
- Verletzungsnachweis (Screenshot, Kaufbeleg, Zeuge) vorhanden?
- Eidesstattliche Versicherung möglich?

### Schritt 5 – Ressourcen und Kosten einschätzen
- Streitwert schätzen → Gerichts- und Anwaltskosten grob ermitteln.
- Kostenrisiko bei Verlust?
- Eigene Kostentragung vs. Kostenerstattung bei Obsiegen?

## Weichenentscheidung: Welcher Skill als nächstes?

| Situation | Empfohlener Skill |
|---|---|
| EV-Antrag vorbereiten | `gewr-einstweilige-verfuegung-eilverfahren-spezial` |
| UWG-Abmahnung | `gewr-uwg-abmahnung-checkliste` |
| Markenanmeldung | `gewr-markenanmeldung-bauleiter` |
| Markenrecherche | `markenrecherche` |
| Patentverletzung prüfen | `fto-triage` |
| Vollzug EV | `evvollzug-neu-001` |
| Erstgespräch strukturieren | `gewerblicher-rechtsschutz-kaltstart-interview` |

## Anschluss-Skills

- `mandat-triage-gewerblicher-rechtsschutz` – Vertiefte Mandatstriage
- `verletzungs-triage` – IP-Verletzung Erstentscheidung
- `workflow-kaltstart-und-routing` – Kaltstart-Router
- `allgemein` – Plugin-Übersicht

---

## Skill: `gewerblicher-erstpruefung-und-mandatsziel`

_Erstprüfung und Mandatszielbestimmung im gewerblichen Rechtsschutz: strukturiertes Erstgespräch, Rollen- und Interessenklärung, Schutzrechtslandschaft, Falltypisierung und Zieldefinition für anwaltliche Mandate in IP- und Wettbewerbssachen im Gewerblicher Rechtsschutz._

# Spezial: Erstprüfung und Mandatsziel im Gewerblichen Rechtsschutz

## Aktenstart statt Formularstart

Wenn zu **Gewerblicher Erstpruefung Und Mandatsziel** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Gewerblicher Rechtsschutz** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck und Mandatsbezug

Strukturiert die **Erstprüfung und Mandatszieldefinition** bei neuen IP- und Wettbewerbsschutzmandaten. Er hilft dem Anwalt, in kurzer Zeit ein klares Bild der Situation, der Rollen, der einschlägigen Schutzrechtslandschaft und des konkreten Mandatsziels zu gewinnen – als Grundlage für alle weiteren Verfahrensschritte.

Mandatsbezug: Mandant ruft an und sagt „Jemand verletzt unsere Marke" oder „Wir haben eine Abmahnung erhalten" oder „Wir wollen unser Patent durchsetzen". Dieser Skill sorgt dafür, dass das Erstgespräch produktiv ist und alle relevanten Informationen erfasst werden.

## Erstgesprächsstruktur: Sechs Dimensionen

### Dimension 1 – Wer ist der Mandant?

- Name, Rechtsform, Branche, Größe des Unternehmens.
- Inhouse-Rechtsabteilung oder rein externe Beratung?
- IP-Kenntnisstand: Hat Mandant schon IP-Verfahren geführt?
- Entscheider: Wer trifft die Entscheidung (Geschäftsführer, Patentmanager, Vorstand)?
- Interessenkonflikt: Gibt es bestehende Mandate mit verwandten Unternehmen?

### Dimension 2 – Was ist das Problem?

| Problem-Kategorie | Typische Merkmale | Erstreaktion |
|---|---|---|
| Verletzung eigener Schutzrechte | Wettbewerber nutzt Marke/Patent/Design | Verletzungsprüfung, Abmahnung, EV |
| Abmahnung empfangen | Schutzrecht eines Dritten, Frist läuft | Reaktionsprüfung, UE, Schutzschrift |
| Schutzrecht sichern | Neuanmeldung, Portfolio-Aufbau | Anmeldeberatung, Klassen, Register |
| Freedom to Operate | Markteinführung geplant | FTO-Analyse, Patentrecherche |
| Vertragsstreit IP | Lizenz, Übertragung, Verletzung | Vertragsanalyse, Kündigung, Schadensersatz |
| Behördenverfahren | Widerspruch, Löschung, Einspruch | Verfahrensführung DPMA/EUIPO/EPA |

### Dimension 3 – Welche Schutzrechte sind betroffen?

Zu prüfende Schutzrechte:
- **Marken:** Nationale (DPMA), EU (EUIPO), international (WIPO/Madrid), nicht eingetragene Kennzeichen (§ 5 MarkenG).
- **Patente:** DPMA, EPA, PCT; Gebrauchsmuster; ArbnErfG.
- **Designs:** DPMA-Design, Gemeinschaftsgeschmacksmuster (EUIPO), nicht eingetragenes GGM.
- **Urheberrecht:** Werke, Datenbanken, Computerprogramme – entsteht ohne Anmeldung.
- **UWG-Ansprüche:** Ohne Schutzrecht; Mitbewerberverhältnis erforderlich.
- **Geschäftsgeheimnisse:** GeschGehG; angemessene Geheimhaltungsmaßnahmen prüfen.

### Dimension 4 – Was ist das Mandatsziel?

Mögliche Ziele (können kombiniert sein):

| Ziel | Instrument |
|---|---|
| Verletzung stoppen (sofort) | EV, Abmahnung |
| Verletzung dauerhaft verhindern | Unterlassungsurteil, Abschlussvereinbarung |
| Schadensersatz erhalten | Auskunft, Schadensersatzklage |
| Schutzrecht vernichten | Widerspruch, Nichtigkeitsklage, Löschungsantrag |
| Eigenes Schutzrecht absichern | Anmeldung, Verlängerung, Verteidigung |
| Markteinführung absichern (FTO) | Freedom-to-Operate-Analyse |
| Lizenzverhältnis klären | Vertragsberatung, FRAND-Analyse |
| Kosten minimieren | Vergleich, modifizierte UE |

### Dimension 5 – Welche Fristen sind kritisch?

- **Sofortiger Handlungsbedarf:** Abmahnfrist läuft ab (heute? morgen?), EV-Vollziehungsfrist.
- **Mittelfristige Fristen:** DPMA-Widerspruch, EUIPO-Widerspruch, Einspruch EPA.
- **Langfristige Fristen:** Jahresgebühren, Verjährung, Markenverlängerung.
- Frist immer als erste Information in Mandatsnotiz.

### Dimension 6 – Welche Unterlagen liegen vor?

**Sofort benötigte Unterlagen:**
- [ ] Schutzrechtsurkunde / Registerauszug (Marke, Patent, Design).
- [ ] Verletzungsnachweis (Screenshot, Kaufbeleg, Messeprotokoll).
- [ ] Abmahnschreiben (falls empfangen): vollständiger Text.
- [ ] Korrespondenz mit Gegenseite.
- [ ] Frühere anwaltliche Stellungnahmen oder Gutachten.
- [ ] Lizenzverträge, wenn Lizenzlage komplex.

**Noch zu beschaffen:**
- [ ] Aktueller Registerauszug DPMA/EUIPO/Patentrolle.
- [ ] Eidesstattliche Versicherung des Mandanten.
- [ ] Screenshots mit Metadaten.

## Risikoampel bei der Erstprüfung

### Grün (Soforthandlung vertretbar)

- Schutzrecht eingetragen und valide.
- Verletzung eindeutig und belegt.
- Dringlichkeit noch gegeben (Kenntnis < 4 Wochen).
- Keine offensichtlichen Einwendungen der Gegenseite.
→ Abmahnung oder EV unverzüglich vorbereiten.

### Gelb (Weitere Klärung erforderlich)

- Schutzrecht vorhanden, aber Gültigkeitsfragen offen.
- Verletzung plausibel, aber noch nicht vollständig belegt.
- Zeitlage noch komfortabel.
→ Weitere Recherche; Mandantenrückfragen; dann Entscheidung.

### Rot (Vorsicht geboten)

- Schutzrecht ungültig, abgelaufen oder streitig.
- Verletzungshandlung zweifelhaft.
- Missbrauchsverdacht (§ 8c UWG).
- Dringlichkeit möglicherweise schon selbst widerlegt.
→ Kein sofortiger Schritt ohne vertiefte Prüfung; Risiken dem Mandanten klar darstellen.

## Mandatsnotiz-Vorlage (Erstgespräch)

```
MANDATSNOTIZ – ERSTGESPRÄCH
Datum: _______________
Anwalt: _______________
Mandant: _______________ Kontakt: _______________

Problem-Kategorie: _______________
Betroffenes Schutzrecht: _______________
Verletzungshandlung: _______________
Gegenseite: _______________
Kritische Frist: _______________ (bis: _______________)

Mandatsziel: _______________
Risikoampel: Grün / Gelb / Rot
Empfohlene nächste Schritte:
1. _______________
2. _______________
3. _______________

Fehlende Unterlagen: _______________
Nächster Termin: _______________
```

## Abgrenzung: Was dieser Arbeitsgang nicht macht

- Kein Ersatz für die Vertiefung in Fachmodule (EV-Antrag, Abmahnung, Anmeldung).
- Keine abschließende rechtliche Beurteilung ohne Normtext- und Rechtsprechungs-Prüfung.
- Keine Festlegung auf eine Handlungsoption ohne Mandantenentscheidung.

## Anschluss-Skills

- `mandat-triage-gewerblicher-rechtsschutz` – Vertiefte Triage
- `gewerblicher-rechtsschutz-kaltstart-interview` – Kaltstart-Interview
- `gw-einfuehrung-rechtsschutzwege` – Überblick Rechtsschutzwege
- `verletzungs-triage` – IP-Verletzung Erstentscheidung

---

## Skill: `abmahnung-urheberrecht-erfindungsmeldung`

_Urheber oder Lizenznehmer erhielt unerlaubte Nutzung (Bild Text Video) oder Mandant erhielt Abmahnung wegen Urheberrechtsverletzung. § 97a UrhG Abmahnung und Unterlassung. Prüfraster: modifizierte Unterlassungserklärung Deckelung Abmahnkosten § 97a Abs. 3 UrhG im privaten Bereich Filesharing-Prax..._

# Urheberrechtliche Abmahnung – § 97a UrhG

## Arbeitsbereich

Urheber oder Lizenznehmer erhielt unerlaubte Nutzung (Bild Text Video) oder Mandant erhielt Abmahnung wegen Urheberrechtsverletzung. § 97a UrhG Abmahnung und Unterlassung. Prüfraster: modifizierte Unterlassungserklärung Deckelung Abmahnkosten § 97a Abs. 3 UrhG im privaten Bereich Filesharing-Praxis Lizenzanalogie § 97 Abs. 2 UrhG Schadensersatz. Output: Abmahnungsentwurf oder Reaktions-Memo auf erhaltene Abmahnung. Abgrenzung zu unterlassungsverlangen (MarkenG UWG PatG) und verletzungs-triage (Erstentscheidung). Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Behandelt das urheberrechtliche Abmahnverfahren nach § 97a UrhG
als notwendige Voraussetzung für die gerichtliche Geltendmachung von
Unterlassungs- und Schadensersatzansprüchen (§§ 97, 97a UrhG). Er deckt
sowohl die Gläubigerperspektive (Abmahnung verfassen, Unterlassungserklärung
einfordern) als auch die Schuldnerperspektive (Abmahnung prüfen, modifizierte
Unterlassungserklärung abgeben) ab. Schwerpunkte sind die formalen
Mindestanforderungen an die Abmahnung (§ 97a Abs. 2 UrhG), die Kostendeckelung
im privaten Bereich (§ 97a Abs. 3 UrhG) und die Berechnung des
Schadensersatzes nach der Lizenzanalogie (§ 97 Abs. 2 Satz 3 UrhG) –
insbesondere in Filesharing-Fällen.

Mandatsbezug: Abgemahnter Privatnutzer erhält Filesharing-Abmahnung; Rechteinhaber
möchte eigene Werke schützen; Streit über Höhe der Abmahnkosten und des Schadensersatzes.

## Eingaben

1. **Abmahngegenstand** – Welches Werk (Buch, Musik, Film, Foto, Software)?
 Wer ist Rechteinhaber (Urheber, Verwerter, Lizenznehmer mit Klagerecht)?
2. **Verletzungshandlung** – Öffentliche Zugänglichmachung (§ 19a UrhG) via
 Filesharing (BitTorrent, eDonkey), Download, Hosting? Zeitpunkt und Umfang?
3. **Personenkreis** – Privat- oder Unternehmensnutzer (für § 97a Abs. 3 UrhG
 maßgeblich)?
4. **IP-Adressdaten** – Gerichtlicher Auskunftsanspruch nach § 101 Abs. 9 UrhG
 beim Provider bereits erwirkt? Zuordnung zur Person gesichert?
5. **Vorangegangene Abmahnungen** – Wiederholungsgefahr bereits durch frühere
 Verletzung begründet?
6. **Empfangene Abmahnung** – Volltext, Absender, Frist, Forderungshöhe,
 beigefügte Unterlassungserklärung.

## Rechtlicher Rahmen

### Zentrale Normen

- **§ 97 UrhG** – Unterlassungs- und Schadensersatzanspruch bei Urheberrechts-
 verletzungen; § 97 Abs. 2 UrhG: Schadensersatz auch im Wege der Lizenzanalogie
 (Satz 3) oder nach tatsächlichem Schaden (Satz 1) oder Gewinnherausgabe
 (Satz 2, str.).
- **§ 97a Abs. 1 UrhG** – Abmahnung als notwendige Voraussetzung für
 Unterlassungsklage; Pflicht des Abmahnenden zur inhaltlichen Korrektheit.
- **§ 97a Abs. 2 UrhG** – Mindestinhalt: Abgemahnter, Rechteinhaber,
 Verletzungshandlung, geltend gemachter Anspruch, Kosten.
- **§ 97a Abs. 3 UrhG** – Kostendeckelung bei privater Erstnutzung auf 100 €
 Gegenstandswert (Erstattungsfähigkeit der Abmahnkosten auf diesen Betrag
 begrenzt), wenn Verstoß nicht im geschäftlichen Verkehr und keine erheblichen
 Rechtsverletzung vorliegt (§ 97a Abs. 3 Satz 1 Nr. 1 und 2 UrhG).
- **§ 97a Abs. 4 UrhG** – Kosten einer unberechtigten Abmahnung trägt der
 Abmahner; Gegenanspruch des Abgemahnten.
- **§ 101 UrhG** – Auskunftsanspruch gegen Verletzer und Provider (§ 101 Abs. 9
 UrhG: gerichtliche Anordnung erforderlich); Drittauskunft bei Filesharing.
- **§ 19a UrhG** – Recht der öffentlichen Zugänglichmachung; Filesharing erfüllt
 diesen Tatbestand durch das Anbieten im Peer-to-Peer-Netzwerk.
- **§ 44b UrhG** – Text und Data Mining (seit 2021); für Abmahnpraxis nicht
 unmittelbar relevant, aber bei KI-generierten Inhalten zu beachten.

### Leitentscheidungen

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 "Tannöd": Zur Lizenzanalogie bei Filesharing: Der Rechteinhaber kann als
 Mindestschadensersatz den Betrag verlangen, den eine vernünftige Partei als
 angemessene Vergütung für die Gestattung der Nutzung vereinbart hätte;
 Filesharing ermöglicht unbegrenzte Verbreitung, was bei der Lizenzberechnung
 zu berücksichtigen ist; einzelne Downloads rechtfertigen einen Pauschalbetrag,
 da genaue Feststellung der Schadenshöhe nicht möglich ist (§ 287 ZPO).

2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 "Tauschbörse III": Zur Störerhaftung des Anschlussinhabers: Der Anschluss-
 inhaber haftet als Störer für Urheberrechtsverletzungen über seinen Anschluss,
 wenn er Prüfungspflichten verletzt hat (Sicherung des WLAN, Belehrung von
 Familienmitgliedern); sekundäre Darlegungslast des Anschlussinhabers zur
 Benennung möglicher alternativer Täter.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Ablauf

### Für den Abmahnenden (Rechteinhaber)

1. **Rechteinhaberschaft prüfen** – Urheber (§ 7 UrhG), Rechteinhaber durch
 Übertragung (§ 31 UrhG), ausschließlicher Lizenznehmer mit Klagerecht?

2. **Verletzungshandlung dokumentieren** – Screenshot mit Zeitstempel, IP-Adresse,
 Portname, Dateiname; ggf. Privatgutachter für Filesharing-Fälle; Nachweis
 des Anmeldetags (§ 32 Abs. 1 MarkenG – hier: Veröffentlichungsdatum des Werks).

3. **Auskunft einholen (§ 101 Abs. 9 UrhG)** – Antrag beim Landgericht am
 Sitz des Providers auf gerichtliche Anordnung; Frist zur Datenspeicherung
 beachten (Vorratsdaten vs. Verbindungsdaten).

4. **Abmahnung verfassen (§ 97a Abs. 2 UrhG)** – Pflichtinhalt: Bezeichnung des
 Verletzers, des Rechteinhabers, der verletzten Rechte, der Verletzungshandlung,
 der geltend gemachten Ansprüche, der Abmahnkosten; konkrete und strafbewehrte
 Unterlassungserklärung beifügen; angemessene Reaktionsfrist setzen (i. d. R.
 7–14 Tage, ggf. kürzer bei dringlichen Fällen).

5. **Frist überwachen** – Bei Nichtreaktion oder unzureichender Erklärung:
 einstweilige Verfügung beim LG (§§ 935, 940 ZPO); Dringlichkeit beachten
 (Monatsfrist ab Kenntnis der Verletzung bei Verfügungen, h. M.).

6. **Schadensersatz geltend machen** – Lizenzanalogie (§ 97 Abs. 2 Satz 3 UrhG);
 Schätzung nach § 287 ZPO; Tabellen für übliche Lizenzgebühren (MFM-Tabelle
 für Fotos; GEMA-Tarife für Musik; BGH-Rspr. für Filesharing, vgl.
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Für den Abgemahnten (Schuldner)

1. **Abmahnung prüfen** – Formelle Anforderungen § 97a Abs. 2 UrhG erfüllt?
 Rechteinhaberschaft glaubhaft? Verletzungshandlung konkret beschrieben?

2. **Kostendeckelung § 97a Abs. 3 UrhG prüfen** – Privater Bereich? Erstmalige
 Verletzung? Kein erheblicher Verstoß? Wenn ja: Abmahnkosten auf Erstattung
 von Kosten aus 100 € Gegenstandswert begrenzt.

3. **Modifizierte Unterlassungserklärung abgeben** – Inhaltlich vollständig (alle
 zukünftigen gleichartigen Verletzungshandlungen erfassen; Dreier, § 97a Rn. 12);
 ohne Anerkenntnis der Rechtsverletzung und der Kostenforderung; Vertragsstrafe
 nach Hamburger Brauch (konkrete Summe nach billigem Ermessen).

4. **Kosten verhandeln** – Lizenzanalogie begründen oder anfechten; bei Filesharing
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

5. **Verjährung beachten** – § 102 UrhG i. V. m. §§ 195, 199 BGB: 3-Jahres-
 Regelverjährung; Beginn mit Kenntnis (§ 199 Abs. 1 BGB); 10-Jahres-Maximal-
 frist ab Verletzungshandlung (§ 199 Abs. 3 Nr. 1 BGB).

## Beispiel

*Sachverhalt:* Privatperson P erhält Abmahnung wegen angeblicher Beteiligung
an einer Filesharing-Tauschbörse für einen Spielfilm; Forderung: 956 € Abmahnkosten
+ 500 € Schadensersatz.

*Verteidigungsmemo (Gutachtenstil):*

**Kostendeckelung:** P ist Privatperson und die Verletzung war nach Darstellung
des Abmahners einmalig (kein Wiederholungsfall, kein erheblicher Verstoß).
Die Abmahnkosten sind daher nach § 97a Abs. 3 Satz 1 UrhG auf die Erstattung
aus einem Gegenstandswert von 100 € begrenzt (Dreier, in: Dreier/Schulze, UrhG,
7. Aufl. 2022, § 97a Rn. 12). Aus 100 € Gegenstandswert ergibt sich nach dem
RVG für eine 1,3-Gebühr (Nr. 2300 VV RVG) ein Erstattungsbetrag von ca. 27,30 €
(zzgl. Auslagenpauschale); die geltend gemachten 956 € sind insoweit überhöht.

**Schadensersatz:** 500 € nach Lizenzanalogie ist bei einem Spielfilm vertretbar
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
kann P durch sekundäre Darlegungslast auf alternative Täter (Familienmitglieder)
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Empfehlung:** Modifizierte Unterlassungserklärung ohne Schuldanerkenntnis abgeben;
Kosten auf Deckelungsbetrag reduzieren; Schadensersatz verhandeln.

*(Reber, in: Schricker/Löwenheim, UrhR, 6. Aufl. 2020, § 97a Rn. 25.)*

## Risiken und typische Fehler

- **Unzureichende Unterlassungserklärung:** Zu enge Erklärung beseitigt Wiederholungs-
 gefahr nicht; Rechteinhaber kann sofort klagen (Reber, § 97a Rn. 25).
- **Fristen bei einstweiliger Verfügung:** Dringlichkeit entfällt, wenn Rechteinhaber
 mehr als 4–6 Wochen (je nach OLG-Praxis) nach Kenntnis zuwartete, ohne zu
 handeln.
- **Sekundäre Darlegungslast:** Pauschales Bestreiten genügt nicht (BGH
 "Tauschbörse III"); P muss konkret darlegen, wer sonst Zugang hatte.
- **IP-Adresszuordnung fehlerhaft:** Gutachtlich belegte Zuordnung angreifen;
 Richtigkeit der Ermittlung durch Privatgutachter in Frage stellen.
- **Deckelung bei erheblichem Verstoß ausgeschlossen:** § 97a Abs. 3 Satz 2
 UrhG; bei massenhaftem Uploading oder gewerblichem Kontext greift die
 Deckelung nicht.
- **Berufsrecht und Datenschutz:** § 43a Abs. 2 BRAO, § 203 StGB; Mandantendaten
 (insb. IP-Adressen) unterliegen der Verschwiegenheit.
- **Verjährung:** § 102 UrhG, §§ 195, 199 BGB; bei Unkenntnis beginnt Frist nicht
 zu laufen, aber 10-Jahres-Maximallust ab Verletzung (§ 199 Abs. 3 Nr. 1 BGB).

## Quellenpflicht

Alle Aussagen zu Abmahnvoraussetzungen, Kostendeckelung und Lizenzanalogie nach
`references/zitierweise.md`. BGH-Rspr. zur Störerhaftung und sekundären
Darlegungslast ist dynamisch; neuere Entscheidungen (insb. BGH seit 2018) immer
auch auf veränderte Rechtslage (Haftungsprivileg § 8 TMG a. F. → § 7 ff. DDG)
hin prüfen. Bei Streit über Deckelungsvoraussetzungen h. M. und Gegenauffassung
kenntlich machen.

## Triage-Fragen vor Urheberrechts-Abmahnung

Bevor die Abmahnung versandt wird, klaere:
1. Ist das urheberrechtlich geschuetzte Werk klar identifiziert und der Schutzbestand unstreitig (§ 2 I UrhG — Schoepfungshoehe)?
2. Handelt es sich um eine Privatperson (§ 97a III UrhG — Deckelung EUR 1.000) oder einen gewerblichen Verletzer?
3. Ist der Rechteinhaber eindeutig der Mandant (Werkvertrag, Arbeitsvertrag, Rechteabtretung)?
4. Ist die Verletzungshandlung noch andauernd oder bereits beendet (Wiederholungsgefahr vs. Erstbegehungsgefahr)?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

<!-- AUDIT 27.05.2026
Task: Bundle 031 / Halluzinations-Reparatur
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Korrektur: GRUR 2016, 176 → GRUR 2016, 191 (alle 3 Fundstellen). Verifiziert via dejure.org.
-->

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 97a UrhG
- § 97 UrhG
- § 8c UWG
- § 14 MarkenG
- § 42 MarkenG
- § 8 UWG
- § 13 UWG
- § 26 MarkenG
- § 9 PatG
- § 66 MarkenG
- § 8 MarkenG
- § 6 ArbnErfG

### Leitentscheidungen

- BGH I ZR 153/16
- BGH I ZR 82/99
- BGH I ZR 20/07
- BGH X ZR 171/12

---

## Skill: `erfindungsmeldung-aufnahme`

_Mitarbeiter meldet eine Erfindung oder Unternehmen prüft eingegangene Erfindungsmeldung. ArbnErfG Arbeitnehmererfindungsgesetz. Prüfraster: Neuheit erfinderische Tätigkeit technischer Charakter EPUe Schutzfähigkeit Arbeitnehmererfindung Inanspruchnahme vs. Freistellung Frist 4 Monate § 6 ArbnErfG..._

# Erfindungseingang — Erstprüfung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

Wenn der Nutzer keine Erfindungsmeldung eingereicht hat, werden folgende Angaben in einem Durchgang abgefragt:

1. **Was ist die Erfindung?** Beschreibung in eigenen Worten — was sie tut, wie sie funktioniert, was die Kernidee ist.
2. **Welches Problem wird gelöst?** Was war zuvor nicht möglich oder mangelhaft?
3. **Worin liegt der Unterschied zum Stand der Technik?** Was haben andere bisher gemacht, und was macht diese Erfindung anders?
4. **Wer hat erfunden, und wann?** Namen, Arbeitsverhältnis (Arbeitnehmer/Freier Mitarbeiter?), ungefähres Entstehungsdatum.
5. **Wurde die Erfindung bereits offenbart?** Publikation, Messe, Konferenz, Angebot, öffentliches Repository, Kundendemonstration (auch unter NDA). Wenn ja: wann und wie.
6. **Wird die Erfindung bereits genutzt oder ist sie geplant?** In Produktion, im Pilotbetrieb, auf der Roadmap oder noch auf dem Papier?
7. **Welches Technologiegebiet?** Software, Hardware, Mechanik, Biotechnologie, KI/ML, Chemie, Medizinprodukt etc.

Bei formeller Erfindungsmeldung (IDF oder Unternehmensformular): Felder daraus entnehmen, nur Fehlende erfragen.

## Rechtlicher Rahmen

### Kernvorschriften

- **§§ 1–5 PatG** — Patentierbarkeitsvoraussetzungen: Neuheit (§ 3), erfinderische Tätigkeit (§ 4), gewerbliche Anwendbarkeit (§ 5)
- **Art. 52–57 EPÜ** — Patentierbarkeit im europäischen Patentsystem; technischer Charakter als Voraussetzung; Art. 56 EPÜ erfinderische Tätigkeit (Aufgabe-Lösungs-Ansatz)
- **§§ 5–12 ArbnErfG** — Meldepflicht (§ 5), Inanspruchnahme durch den Arbeitgeber (§ 6 Abs. 1: Frist 4 Monate), unbeschränkte vs. beschränkte Inanspruchnahme; Vergütungspflicht (§§ 9 ff. ArbnErfG)
- **§ 3 Abs. 1 PatG** — Absolutes Neuheitserfordernis: jede Offenbarung vor dem Anmeldetag ist neuheitsschädlich; eine Schonfrist für Vorveröffentlichungen gilt im deutschen und europäischen Patentrecht nicht
- **§§ 1–3 GebrMG** — Gebrauchsmuster als schnellerer Schutzrechtsweg (keine erfinderische Tätigkeit im gleichen Maßstab, aber Neuheit + erfinderischer Schritt erforderlich)
- **§ 26 GeschGehG** — Geschäftsgeheimnis als Alternative bei mangelnder Erkennbarkeit der Verletzung

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Kommentare

- Benkard/Melullis, PatG, 12. Aufl. 2023, § 3 Rn. 1 ff. (Neuheitsbegriff, Stand der Technik)
- Bartenbach/Volz, ArbnErfG, 6. Aufl. 2019, § 5 Rn. 1 ff. (Meldepflicht und Form) und § 9 Rn. 1 ff. (Vergütung)
- Mes, PatG/GebrMG, 5. Aufl. 2020, § 1 Rn. 20 ff. (technischer Charakter, Software- und KI-Erfindungen)
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ablauf

### Schritt 1: Meldung aufnehmen

Vorliegende Erfindungsmeldung vollständig lesen. Fehlen Angaben: Rückfragen gemäß Abschnitt "Eingaben" in einem Durchgang stellen. Unvollständige Meldungen nicht screenen — ein Screening von "einer neuen KI-Lösung für X" ohne technische Substanz ist schlechter als kein Screening.

**Arbeitnehmererfindung prüfen:** Wenn der Erfinder Arbeitnehmer ist, zunächst klären: Handelt es sich um eine Diensterfindung (§ 4 Abs. 2 ArbnErfG: Entstehung aus dem Arbeitverhältnis oder wesentlich auf betriebliche Erfahrungen/Tätigkeiten beruhend)? Wenn ja: Meldepflicht nach § 5 ArbnErfG auslösen und Inanspruchnahmefrist (4 Monate, § 6 Abs. 1) dokumentieren.

### Schritt 2: Sechs Prüfungsschirme

Jeden Schirm in der Reihenfolge abarbeiten. Ergebnis je Schirm: `✓ grün`, `🟡 unklar — Klärungsbedarf`, `🔴 Rote Flagge`.

#### Schirm 1: Neuheitssignale (§ 3 PatG, Art. 54 EPÜ)

**Rote Flaggen (🔴):**
- "Wir haben [bekannte Technik] auf [neues Gebiet] angewandt" — Anwendung bekannter Methoden ohne technische Besonderheit
- "Wettbewerber machen etwas Ähnliches" — Beschreibung selbst stellt Neuheit in Frage
- Merkmal findet sich bereits in öffentlich zugänglichen Produkten, Publikationen oder Patenten

**Grüne Flaggen (✓):**
- Neuer **Mechanismus** — nicht nur neue Anwendung, sondern neue technische Wirkungsweise
- Neue **Kombination** mit unerwartetem Ergebnis
- Lösung eines bisher ungelösten Problems mit spezifischer technischer Lehre

#### Schirm 2: Erfinderische Tätigkeit (§ 4 PatG, Art. 56 EPÜ)

EPA-Prüfungsansatz: Aufgabe-Lösungs-Ansatz. Würde ein Fachmann ausgehend vom nächstliegenden Stand der Technik und der zugrunde liegenden technischen Aufgabe zur beanspruchten Lösung gelangen?

**Rote Flaggen (🔴):**
- Kombinieren bekannter Elemente auf vorhersehbare Weise (predictable combination)
- Routinemäßige Optimierung bekannter Parameter ohne überraschenden Effekt
- "Obvious to try" — eine aus wenigen naheliegenden Alternativen ohne Hindernis

**Grüne Flaggen (✓):**
- Stand der Technik lehrte vom Lösungsweg ab (teaching away)
- Unerwarteter technischer Effekt (surprising effect)
- Langbekanntes Problem, das trotz Bemühungen bisher ungelöst geblieben ist

#### Schirm 3: Technischer Charakter und Schutzfähigkeit (Art. 52 EPÜ, § 1 PatG)

Software, KI/ML und Geschäftsmethoden: Nicht per se ausgeschlossen, aber technischer Charakter muss vorliegen. EPA: "technical character" — weitgehend jeder Bezug zur Technik genügt; Abgrenzung gilt auf der Ebene der erfinderischen Tätigkeit.

**Rote Flaggen (🔴):**
- Reine Geschäftsmethode ohne technische Umsetzung
- Mathematischer Algorithmus ohne technische Anwendung
- Ablauf menschlicher Tätigkeiten ohne computergestützte oder physische Komponente
- KI-Invention: Schutzbegehren richtet sich allein auf Funktion (empfehlen, klassifizieren, vorhersagen) ohne konkrete technische Mittel

**Grüne Flaggen (✓):**
- Technische Verbesserung des Computers selbst (Architektur, Sicherheit, Effizienz)
- Technische Mittel werden konkret beschrieben, nicht nur Ergebnisse beansprucht
- Einbettung in technisches Gebiet (Bildverarbeitung, Signalübertragung, Steuerung)

#### Schirm 4: Neuheitsschädliche Vorveröffentlichung / Fristen (§ 3 PatG)

Im deutschen und europäischen Patentrecht gilt **absolutes Neuheitserfordernis**: jede öffentliche Zugänglichmachung vor dem Anmeldetag ist neuheitsschädlich. Eine Schonfrist für Vorveröffentlichungen gilt nicht.

**Ausnahme:** § 3 Abs. 5 PatG (Ausstellungsprioritätsprinzip) und Art. 55 EPÜ (offensichtlicher Missbrauch oder Ausstellungsprivileg) — sehr eng, nicht als Sicherheitsnetz einplanen.

Kategorisierung:

**🔴 Wahrscheinlich neuheitsschädlich:**
- Öffentliche Veröffentlichung, Verkauf, Angebot, Messedemonstration, öffentliches Repository **vor dem Anmeldetag**
- Preprint, Konferenzbeitrag, Social-Media-Post, Blogbeitrag mit technischem Inhalt

**🟡 Fristdruck:**
- Veröffentlichung liegt vor, Anmeldung noch nicht erfolgt — **sofortiger Handlungsbedarf**

**✓ Unbedenklich:**
- Keine Offenbarung außerhalb vertraulicher Kanäle
- Kundenpräsentation unter NDA (Sorgfalt: NDA-Reichweite prüfen)

Konkret erfragen: Konferenzbeiträge (auch eingereicht, nicht nur angenommen), Preprints, öffentliche Repositories, Messeauftritte, Angebote an Kunden, Investorenpräsentationen ohne NDA.

#### Schirm 5: Erkennbarkeit einer Verletzung (Detectability)

Ist eine Verletzung am Markt erkennbar? Server-seitige Algorithmen, interne Fertigungsschritte und reine Datenverarbeitungsmethoden ohne erkennbare Außenwirkung sind schwer durchzusetzen.

**🔴 Geringe Erkennbarkeit:**
- Server-seitiger Algorithmus ohne erkennbares Ausgabemuster
- Internes Fertigungsverfahren (z. B. neuer Ätzschritt in Halbleiterproduktion)
- Trainings-Methodik für ML-Modell — nur durch aufwendige Tests erahnbar

Bei geringer Erkennbarkeit: Abwägung Patent vs. Geschäftsgeheimnis nach GeschGehG vornehmen. Wer die Entscheidung in der Praxis trifft: gemäß Unternehmensrichtlinie / Mandatsprofil.

**✓ Hohe Erkennbarkeit:**
- Konsumentenprodukt mit sichtbaren Merkmalen
- Veröffentlichte API, Protokoll, SDK
- Physischer Mechanismus in verteiltem Produkt

#### Schirm 6: Strategischer Wert

Passt die Erfindung zur Schutzrechtsstrategie des Unternehmens? Prüfung anhand des Mandatsprofils:

- **Offensiv (Durchsetzungsportfolio):** Ist der Anspruch breit und assertionsfähig?
- **Defensiv (Freedom to Operate):** Schützt die Anmeldung eine relevante Technologie?
- **Lizenz-/Erlösmodell:** Ist die Erfindung lizenzierbar und wer würde zahlen?
- **Kerntechnologie vs. Peripherie:** Kern hat höheren Wert.
- **Wettbewerbslandschaft:** In patentintensiven Sektoren (Pharma, Halbleiter) frühzeitig anmelden.

### Schritt 3: Erfindungsprüfungsvermerk erstellen

Format:

> **Erfindungsprüfungsvermerk — [Titel der Erfindung]**
>
> **Ergebnis: [WEITERVERFOLGEN / KLÄREN / ABLEHNEN]**
>
> *[Ein Satz — Begründung im Klartext.]*
>
> ---
>
> ### Prüfungsergebnisse
>
> | Prüfschirm | Ergebnis | Anmerkung |
> |---|---|---|
> | Neuheitssignale | [✓ / 🟡 / 🔴] | [einzeiliger Grund] |
> | Erfinderische Tätigkeit | [✓ / 🟡 / 🔴] | [einzeiliger Grund] |
> | Technischer Charakter | [✓ / 🟡 / 🔴] | [einzeiliger Grund] |
> | Vorveröffentlichung / Fristen | [✓ / 🟡 / 🔴] | [einzeiliger Grund + Daten] |
> | Erkennbarkeit | [✓ / 🟡 / 🔴] | [einzeiliger Grund] |
> | Strategischer Wert | [✓ / 🟡 / 🔴] | [Bezug zum Mandatsprofil] |
>
> ---
>
> ### Offene Punkte
>
> - [Frage / Klärungsbedarf]
>
> ### Nächste Schritte
>
> 1. **Patentrecherche beauftragen** — Suchanfrage für Patentanwalt mit Anspruchskonzepten, Erfindernamen, IPC-Klasse und bekannten Referenzen.
> 2. **Rückfrage an Erfinder** — Klärung offener Punkte zu [konkreten Punkten].
> 3. **An Patentanwalt übergeben** — bei Grenzfragen zum technischen Charakter oder zur Schutzstrategie.
> 4. **Ablehnen und Dankesschreiben** — Begründung archivieren.
> 5. **Geschäftsgeheimnis-Route** — Hinweis an zuständige Stelle gemäß GeschGehG.

### Schritt 4: Arbeitnehmererfindung — Pflichtprozess

Wenn der Erfinder Arbeitnehmer ist:

- **§ 5 ArbnErfG — Meldepflicht:** Erfinder hat unverzüglich zu melden. Form: schriftlich, Beschreibung der Erfindung, Entstehungsumstände.
- **§ 6 Abs. 1 ArbnErfG — Inanspruchnahmefrist:** Arbeitgeber hat **4 Monate** ab Eingang der Meldung, um unbeschränkt oder beschränkt in Anspruch zu nehmen. Frist läuft automatisch; Untätigkeit gilt als Freigabe.
- **§§ 9 ff. ArbnErfG — Vergütungspflicht:** Bei Inanspruchnahme entsteht Vergütungsanspruch. Bemessung nach den Richtlinien für die Vergütung von Arbeitnehmererfindungen im privaten Dienst (1959/zuletzt geändert). Faktoren: Erfindungswert, Anteilsfaktor, Mitarbeiterstellung.
- Frist im Vermerk dokumentieren und in das Fristenkontrollsystem des Mandanten eintragen.

## Beispiel

**Eingabe:** "Neuer Cache-Algorithmus auf Basis eines erlernten Modells anstelle von LRU; im ersten Quartal dieses Jahres entwickelt, noch nicht veröffentlicht, Prototyp intern im Staging."

**Ergebnis (Beispiel):**

> **Erfindungsprüfungsvermerk — Lernbasierter Cache-Algorithmus**
>
> **Ergebnis: WEITERVERFOLGEN** — Neuheit und technischer Charakter sind prima facie gegeben; keine neuheitsschädliche Vorveröffentlichung erkennbar; strategische Relevanz in Abhängigkeit vom Mandatsprofil prüfen.
>
> | Prüfschirm | Ergebnis | Anmerkung |
> |---|---|---|
> | Neuheitssignale | 🟡 | Mechanismus neu, aber verwandte Literatur (ML-Caching) vorhanden — Recherche erforderlich |
> | Erfinderische Tätigkeit | 🟡 | Unerwarteter Effizienzgewinn behauptet — durch Recherche zu belegen |
> | Technischer Charakter | ✓ | Konkrete technische Verbesserung der Cache-Verwaltung |
> | Vorveröffentlichung | ✓ | Keine Offenbarung, intern und vertraulich |
> | Erkennbarkeit | 🟡 | Server-seitig: Abwägung Patent vs. Geschäftsgeheimnis empfohlen |
> | Strategischer Wert | 🟡 | Abhängig vom Mandatsprofil |

## Risiken und typische Fehler

- **Neuheitsschädliche Vorveröffentlichung übersehen:** Jede öffentliche Zugänglichmachung vor Anmeldetag zerstört die Patentierbarkeit weltweit (außer engen Ausnahmefällen). Eine Schonfrist für Vorveröffentlichungen gilt nicht.
- **ArbnErfG-Fristen versäumen:** Die 4-Monats-Inanspruchnahmefrist (§ 6 Abs. 1 ArbnErfG) läuft automatisch. Nicht im Fristenbuch eingetragen = Freigabe der Erfindung.
- **Patentierbarkeit bestätigen:** Die Skill trifft keine Patentierbarkeitsaussage. "Besteht die Erstprüfung" ist nicht "patentierbar".
- **Erkennbarkeitsfrage ignorieren:** Ein Patent auf eine nicht erkennbare Verletzungsform veröffentlicht das Know-how ohne Durchsetzungsmöglichkeit.
- **KI/Software-Erfindungen: technischen Charakter unterschätzen:** Der EPA bewertet technischen Charakter weit; nicht vorschnell ablehnen.

## Quellenpflicht

Jede Aussage zu Neuheit, erfinderischer Tätigkeit oder Vergütung muss auf konkreten Normen oder Entscheidungen beruhen. Pflichtquellen in jedem Vermerk:

- **Gesetzestext:** § 3, § 4, § 5 PatG; §§ 5, 6, 9 ff. ArbnErfG; Art. 52–56 EPÜ
- **Rechtsprechung:** mindestens eine BGH-Entscheidung zur Neuheit oder erfinderischen Tätigkeit
- **Kommentar:** Benkard PatG oder Bartenbach/Volz ArbnErfG mit § und Randnummer
- Alle Quellen mit Fundstelle zitieren. Modellannahmen als `[Modellwissen — verifizieren]` kennzeichnen.

## Triage-Fragen bei Erfindungsmeldung

Bevor die Erfindung aufgenommen und bewertet wird, klaere:
1. Liegt eine Diensterfindung (§ 4 ArbnErfG — Arbeitgeber hat Inanspruchnahmerecht) oder eine Freierfindung vor?
2. Laeuft die 4-Monats-Frist des § 6 I ArbnErfG für die Inanspruchnahme bereits?
3. Gibt es neuheitsschaedliche Vorveröffentlichungen (Veroeffentlichung vor Anmeldedatum)?
4. Besteht technischer Charakter im Sinne des EPÜ Art. 52 (Software: loest technisches Problem auf technischem Weg)?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

<!-- AUDIT 27.05.2026
Task: Bundle 031 / Halluzinations-Reparatur
Korrektur: Zitat aus "Aktuelle Rechtsprechung"-Block entfernt (bei Zweifel loeschen).
-->

---

## Skill: `fto-triage-gewerblicher-rechtsschutz-mandat`

_Unternehmen will Produkt einführen oder Technologie einsetzen und fragt: Verletzen wir fremde Patente? Freedom-to-Operate-Analyse FTO. Prüfraster: Recherche Espacenet DPMApaplus EP-Datenbank sperrende DE- und EP-Patente. Ergebnis Recherchepaket für Patentanwalt kein FTO-Gutachten. Output: Recherc..._

# Freedom-to-Operate-Triage (FTO)

## Aktenstart statt Formularstart

Wenn zu **Fto Triage Gewerblicher Rechtsschutz Mandat** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Gewerblicher Rechtsschutz** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Produkt-/Technologiebeschreibung (so detailliert wie möglich: technische Merkmale, Funktionsweise, Materialien, Verfahren)
- Zielmarkt / Vertriebsgebiet (Deutschland, EU, weltweit)
- Schlüsselwörter / Technologieklassifikation (IPC/CPC-Klassen, falls bekannt)
- Geplantes Markteinführungsdatum
- Ggf. bereits bekannte Patente (Wettbewerber)
- Relevanter Stand der Technik (falls vorhanden)

## Ablauf

### 1. Technologie charakterisieren

Produktbeschreibung in technische Merkmale übersetzen:
- Hauptfunktion / Kernerfindung
- Unterscheidungsmerkmale gegenüber bekanntem Stand der Technik
- Schlüsselkomponenten und ihre Funktion
- Verfahrensschritte (bei Verfahrenspatenten)
- Mögliche IPC/CPC-Klassifikationen (International Patent Classification / Cooperative Patent Classification)

Vorschlag für Suchstrategie aus Merkmalen entwickeln. `[prüfen]` – Klassifikation und Merkmalsdefinition mit Fachmann abstimmen.

### 2. Patentrecherche durchführen

**Pflicht-Datenbanken:**

| Datenbank | URL | Umfang |
|---|---|---|
| Espacenet | worldwide.espacenet.com | Weltweite Patente; DE, EP, WO; Volltextsuche |
| DPMApaplus | depatisnet.dpma.de | Deutsche Patente und Gebrauchsmuster (DE); amtliche DPMA-Datenbank |
| Google Patents | patents.google.com | Ergänzende Suche; maschinelle Übersetzungen |

**Für EP-Patente mit DE-Wirkung:**
- EP-Patent nach Erteilung und Validierung in DE gültig → nationale Verletzungsklage vor deutschen Gerichten möglich (LG Düsseldorf, LG München I, LG Mannheim)
- Prüfung, ob nationales DE-Patent oder EP-Validierung vorliegt

**Suchstrategie:**

```
Schritt 1 – Keyword-Suche: Technologiebegriffe in Titel, Abstract, Ansprüchen
Schritt 2 – IPC/CPC-Klassensuche: Klassifikation + Keyword-Filter
Schritt 3 – Anmeldersuche: Bekannte Wettbewerber als Inhaber
Schritt 4 – Zitationsanalyse: Von gefundenen relevanten Patenten rückwärts zitieren
Schritt 5 – Familiensuche: Internationaler Schutzumfang von Kernpatenten
```

### 3. Gefundene Patente analysieren

Für jedes potenziell sperrende Patent:

**Formelle Prüfung:**
- Status: In Kraft / erloschen / nichtig / anhängig? (DPMA-Register, Espacenet Legal Status)
- Inhaberschaft: Wer ist aktueller Inhaber? Lizenzbereitschaft?
- Prioritätsdatum, Anmeldetag, Erteilungstag
- Ablaufdatum (max. 20 Jahre ab Anmeldetag, § 16 Abs. 1 PatG; ggf. SPC-Verlängerung in Pharma/Pflanzenschutz nach VO (EG) 469/2009)
- Jahresgebühren bezahlt? (DPMA-Register)

**Sachliche Prüfung (Triage-Ebene):**
- Anspruch 1 lesen (Hauptanspruch bestimmt Schutzbereich)
- Wesentliche Merkmale des Anspruchs identifizieren
- Abgleich mit Produktmerkmalen: Fallen alle Merkmale des Anspruchs in das Produkt?

**Relevanzbewertung:**

🔴 **Blocking:** Alle Merkmale des Anspruchs im Produkt vorhanden; Patent in Kraft; keine eindeutige Äquivalenzlücke; anwaltliche FTO-Analyse dringend erforderlich vor Markteinführung.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

🟡 **Mittel:** Einige Überschneidungen; erhebliche Merkmale nicht vorhanden; Design-around möglich; patentanwaltliche Prüfung empfohlen.

🟢 **Niedrig:** Nur entfernte Ähnlichkeit; Schutzbereich klar nicht getroffen; verbleibende Unsicherheiten für anwaltliche Einschätzung vermerken.

### 4. Lizenz- und Design-around-Optionen

Falls 🔴/🟠-Ergebnisse:
- **Lizenzierung:** Patentinhaber identifizieren; Lizenzbereitschaft einschätzen (FRAND-Verpflichtungen bei SEPs prüfen)
- **Design-around:** Welches Merkmal könnte technisch vermieden werden ohne Funktionsverlust?
- **Nichtigkeitsangriff:** Gibt es Stand der Technik, der Neuheit oder erfinderische Tätigkeit des Patents zerstört? (§ 21 Abs. 1 PatG; Nichtigkeitsklage vor BPatG)
- **Prioritätsrecherche:** Ältere Veröffentlichungen des Anmelders als potenziellen Stand der Technik prüfen

### 5. Recherchebericht erstellen

## Quellen und Zitierweise

Zitierweise nach `../references/zitierweise.md`.

**Normen:** §§ 9, 14, 16, 21 PatG; § 14 GebrMG; VO (EG) 469/2009 (SPC-VO Pharma); Art. 64 EPÜ (nationale Wirkung EP-Patent).

**Leitentscheidungen:**
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Kraßer/Ann, Patentrecht, 7. Aufl. 2016, § 33 Rn. 45 ff. (Schutzbereichsbestimmung). `[Modellwissen – prüfen; neuere Auflage verwenden falls verfügbar]`
- Schulte/Moufang, PatG, 10. Aufl. 2017, § 14 Rn. 95 ff. (Äquivalenzlehre).

## Beispiel (Gutachtenstil – Auszug)

**Produkt:** Neue Fertigungsmethode für Halbleiterbauteile mit bestimmter Schichtabfolge

**Gefundenes Patent:** EP 3 456 789 B1, Inhaber: TechCorp SE, in Kraft (Jahresgebühren bezahlt bis 2028), Ablauf 2033.

**Anspruch 1 (vereinfacht):** Verfahren zur Herstellung eines Halbleiterbauteils, umfassend: (a) Aufbringen einer Siliziumschicht, (b) Dotierung mit Phosphor, (c) thermische Aushärtung bei 800–900 °C.

**Merkmalsabgleich:**

| Anspruchsmerkmal | Im Produkt vorhanden? | Anmerkung |
|---|---|---|
| (a) Siliziumschicht | Ja | identisch |
| (b) Phosphordotierung | Ja | identisch |
| (c) Thermische Aushärtung 800–900 °C | Fraglich | Produkt verwendet 850 °C – innerhalb des Bereichs `[prüfen]` |

**Ergebnis:** 🔴 **Blocking.** Alle Merkmale zumindest prima facie im Produkt vorhanden. Keine Äquivalenzlücke erkennbar. Patentanwaltliche FTO-Analyse vor Markteinführung zwingend erforderlich.

## Risiken / typische Fehler

- **Nur DE-Patente prüfen:** EP-Patente mit DE-Validierung haben volle nationale Wirkung; EPO-Datenbank ist Pflicht.
- **Status nicht prüfen:** Erloschene Patente (nicht bezahlte Jahresgebühren, Nichtigerklärung) sind kein Hindernis mehr; DPMA-Register auf aktuellen Status prüfen.
- **SPC-Verlängerungen übersehen:** In Pharma- und Pflanzenschutzbereich können Ergänzende Schutzzertifikate (SPC) die Schutzdauer um bis zu 5 Jahre verlängern.
- **Kein FTO-Gutachten:** Diese Triage ersetzt kein formelles FTO-Gutachten durch einen Patentanwalt; bei 🔴/🟠-Ergebnissen ist patentanwaltliche Einschaltung zwingend.
- **Äquivalenz ist Recht, nicht Technik:** Die Äquivalenzprüfung erfordert rechtliche Wertung (BGH "Pemetrexed"); nicht dem Ingenieur überlassen.
- **Geheimhaltung:** Technologiebeschreibungen sind vertraulich (§ 43a Abs. 2 BRAO; Geschäftsgeheimnis § 2 GeschGehG); nur intern und über gesicherte Kanäle verarbeiten.

---

## Skill: `ip-klausel-pruefung`

_Anwalt prüft Vertrag auf IP-Klauseln (Übertragung Lizenz Inhaberschaft Freistellung) oder Mandant fragt nach Risiken. IP-Klauseln Vertragsrecht. Prüfraster: Übertragung Inhaberschaft Lizenzgewaehrung exklusiv/nicht-exklusiv Gewährleistung Freistellung Reichweite. Output: IP-Klausel-Prüfbericht mi..._

# IP-Klausel-Prüfung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- **Vertragsdokument:** Dateilink, eingefügter Text oder Beschreibung.
- **Vertragstyp:** Arbeitsvertrag, Dienstvertrag (freier Mitarbeiter), Werkvertrag/SOW, Lizenzvertrag (ein- oder ausgehend), Kooperationsvertrag, MSA, M&A-Nebenabrede, sonstige.
- **Position des Mandanten:** Rechtegebend (Lizenzgeber / Übertrager) oder Rechteempfangend (Lizenznehmer / Erwerber) oder beides.
- **Rechtsordnung des Vertrags:** Welches Recht ist vereinbart?

## Rechtlicher Rahmen

### Kernvorschriften

- **§§ 11–24 UrhG** — Urheberpersönlichkeitsrechte (unveräußerlich; § 14 UrhG Entstellungsschutz)
- **§ 29 UrhG** — Urheberrecht ist nicht übertragbar; nur Einräumung von Nutzungsrechten (§§ 31 ff. UrhG) möglich
- **§§ 31–44 UrhG** — Einräumung von Nutzungsrechten: einfaches vs. ausschließliches Nutzungsrecht (§ 31 Abs. 1), Übertragung von Nutzungsrechten (§ 34), Unterlizenzen (§ 35), Zweckübertragungslehre (§ 31 Abs. 5)
- **§§ 43, 69b UrhG** — Urheberrecht an Computerprogrammen bei Arbeitsverhältnissen: Nutzungsrechte beim Arbeitgeber kraft Gesetzes (§ 69b Abs. 1)
- **§§ 15–22 PatG** — Übertragung und Lizenzierung von Patenten; Vindikationsanspruch; Miterfinderschaft
- **§§ 27–31 MarkenG** — Übertragung und Lizenzierung von Marken
- **§§ 1–4 GeschGehG** — Geschäftsgeheimnis: Voraussetzungen, angemessene Schutzmaßnahmen
- **§§ 4, 5 ArbnErfG** — Zuordnung von Arbeitnehmererfindungen (Patent-/Gebrauchsmusterrechte beim Arbeitgeber nach Inanspruchnahme)
- **§§ 433 ff., 311, 280 BGB** — Gewährleistungs- und Haftungsregelungen bei Rechtsmängeln

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Kommentare

- Leistner, in: Schricker/Löwenheim, UrhG, 6. Aufl. 2020, § 31 Rn. 1 (Nutzungsrechte, Übertragbarkeit)
- Spindler, in: Schricker/Löwenheim, UrhG, 6. Aufl. 2020, § 29 Rn. 1 (Nicht-Übertragbarkeit des Urheberrechts)
- Melullis, in: Benkard, PatG, 12. Aufl. 2023, § 15 Rn. 1 (Patentübertragung und -lizenz)
- Ingerl/Rohnke, MarkenG, 3. Aufl. 2010, § 27 Rn. 1 (Markenübertragung – Doppelautoren-Kommentar)
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ablauf

### Schritt 1: Orientierung

Vertrag einmal vollständig lesen. Antworten auf folgende Fragen:

| Frage | Antwort |
|---|---|
| Vertragstyp? | Arbeitsvertrag / Dienstvertrag / Werkvertrag-SOW / Lizenzvertrag ein- oder ausgehend / Kooperation / Sonstiges |
| Position des Mandanten bei IP? | Rechtegebend / -empfangend / beides |
| Vertragspartner? | Name und Einschätzung — Einzelperson, Startup, Großunternehmen |
| Steht Vergütung für IP gesondert? | Arbeitsentgelt, Werkhonorar, Lizenzgebühr, Vorauszahlung, keine |
| Anwendbares Recht? | Welche Rechtsordnung; ist das Mandatsprofil betroffen? |

Bei Unklarheit über die IP-Position (Kooperationsvertrag, beidseitige Rechteeinräumung): nachfragen.

### Schritt 2: Prüfung der Rechteübertragungsklauseln (höchste Priorität)

Bei Arbeitsverträgen, Dienstverträgen und Werkverträgen, wo der Mandant IP des Vertragspartners erwerben soll, zunächst folgende Punkte prüfen:

**A — Urheber- und Leistungsschutzrechte:**
- § 29 UrhG: Urheberrecht ist nicht übertragbar. Möglich ist nur die Einräumung von Nutzungsrechten (§§ 31 ff. UrhG). Eine Klausel, die "das Urheberrecht überträgt", ist rechtlich ungenau und erreicht das Ziel nicht.
- § 31 Abs. 1 UrhG: Unterschied zwischen einfachem (nicht ausschließlichem) und ausschließlichem Nutzungsrecht — ausschließliches Nutzungsrecht erlaubt Klage auf eigenem Namen, einfaches nicht.
- § 31 Abs. 5 UrhG (Zweckübertragungslehre): Im Zweifel werden nur für den Vertragszweck unbedingt erforderliche Rechte eingeräumt. Umfang muss explizit definiert sein.
- Urheberpersönlichkeitsrechte (§§ 12–14 UrhG) sind unveräußerlich; lediglich Verzichtserklärungen oder Nichtausübungsabreden (im Rahmen des § 138 BGB) möglich.

**B — Patente und Gebrauchsmuster:**
- Bei Arbeitnehmern: Nutzungsrechte entstehen nach Inanspruchnahme gemäß § 6 ArbnErfG beim Arbeitgeber automatisch.
- Bei freien Mitarbeitern: Ausdrückliche schriftliche Abtretung (§ 15 PatG) erforderlich. Zukunftsbezogene Abtretungsklauseln (noch nicht entstandene Patente) sind zulässig.

**C — Klauselsprache prüfen:**
- Aktuelle Einräumung: "räumt hiermit ein" ist stärker als "verpflichtet sich einzuräumen" (Leistungspflicht vs. dingliche Wirkung)
- Umfang: Alle für die Leistung relevanten Nutzungsarten einschließlich unbekannter Nutzungsarten (§ 31a UrhG) — explizit regeln, wenn gewollt
- Unterlizenzen: Klausel für die Berechtigung zur Unterlizenzierung (§ 35 UrhG) prüfen
- Vorbestehende IP: Welche Rechte des Auftragnehmers sind explizit ausgenommen?

Wenn wesentliche Punkte fehlen oder unklar sind: am Anfang des Vermerks mit 🔴 oder 🟠 kennzeichnen und Änderungsvorschlag beifügen.

### Schritt 3: Klausel-für-Klausel-Prüfung

Für jede IP-relevante Klausel einen Prüfblock erstellen:

```markdown
### [Abschnitt X.X]: [Klauselbezeichnung]

**Was sie sagt:** [Zusammenfassung in eigenen Worten, ein bis zwei Sätze]

**Marktstandard (für diesen Vertragstyp, diese Position, dieses Recht):**
[kurze Referenz]

**Risiko:** 🔴 Kritisch | 🟠 Hoch | 🟡 Mittel | 🟢 Niedrig

**Warum es darauf ankommt:** [ein bis zwei Sätze — was schief geht, wenn die Klausel so bleibt]

**Änderungsvorschlag (soweit erforderlich):**
> "[konkrete Ersatzformulierung]"

**Entscheidungsvorbehalt:** [Bei subjektiven Zuordnungsfragen: anwaltliche Prüfung empfehlen, Argumente pro/contra aufzeigen]
```

Zu prüfende Klauseltypen:

- **Rechteeinräumung / Urheberrechtsklausel** — Wer bekommt welche Nutzungsrechte?
- **Eigentumsklausel an Arbeitsergebnissen** — Abgrenzung Diensterfindung / freie Erfindung / Werk
- **Verbesserungen und Ableitungen** — Wer gehört Verbesserungen an vorbestehendem IP? Wer derivate Werke?
- **Hintergrund-IP vs. Vordergrund-IP** — Ist vorbestehendes IP klar definiert und für den Vertragszweck lizenziert?
- **Lizenzgewährungen** — Umfang, Ausschließlichkeit, Territorium, Verwendungszweck (field of use), Sublizenzierbarkeit, Laufzeit, Kündigungsgründe, Vergütung
- **IP-Gewährleistungen** — Nichtverstoß gegen Drittrechte, Verfügungsberechtigung, Originalität des Werkes
- **IP-Freistellungen** — Umfang, Cap, Verfahren, Ausschlüsse (Modifikationen durch den anderen Teil, ungenehmigte Nutzungen)
- **Open-Source-Erklärungen** — Angaben zu eingebetteten OSS-Komponenten; GPL/LGPL/AGPL-Risiken
- **Marken** — Nutzungsrechte an Marken des anderen Teils, Qualitätskontrolle bei Lizenzen (§ 30 Abs. 2 MarkenG)
- **Geschäftsgeheimnisse** — Behandlung von GeschGehG-Material, angemessene Schutzmaßnahmen (§ 2 Nr. 1 lit. b GeschGehG), Rückgabe nach Vertragsende

**Schweregrad-Kalibrierung:**

| Stufe | Bedeutung |
|---|---|
| 🔴 Kritisch | Nicht unterzeichnen ohne Korrektur. Fehlende Rechteeinräumung wo sie erforderlich ist. Unbeschränkte Lizenz wo beschränkte gewollt ist. Exklusive Einräumung wo nicht exklusiv gewollt. |
| 🟠 Hoch | Stark nachverhandeln; eskalieren wenn keine Bewegung. Unklarer Umfang, fehlendes Urheberpersönlichkeitsrecht-Waiver, fehlende further-assurance-Klausel. |
| 🟡 Mittel | Im ersten Durchgang pushen; akzeptieren wenn letzter offener Punkt. Sprachlich ungenau, Überlebenszeitraum kürzer als Standard. |
| 🟢 Niedrig | Vermerken, kein Kapital einsetzen. Stilistische Abweichung ohne inhaltliche Auswirkung. |

### Schritt 4: Klausel-übergreifende Konsistenzprüfung

IP-Klauseln scheitern als System. Prüfen:

- **Passt die Lizenzgewährung zum Umfang des lizenzierten Rechts?** (Lizenz zur "Nutzung" ist enger als Lizenz zur "Nutzung, Bearbeitung und Erstellung abgeleiteter Werke".)
- **Decken die Gewährleistungen ab, was die Lizenz umfasst?** (Gewährleistung nur für Patente bei einer Lizenz, die auch Urheberrecht und Geschäftsgeheimnisse umfasst, hinterlässt Lücken.)
- **Deckt die Freistellung was die Gewährleistung verspricht?** (Gewährleistung ohne Freistellung ist ein Versprechen ohne Rechtsbehelf.)
- **Zieht Kündigung die Lizenz zurück?** (Oder überlebt eine bezahlte Lizenz die Kündigung? Beides vertretbar — Frage ist, ob es der Absicht entspricht.)
- **Stimmt die IP-Regelung in diesem Vertrag mit verbundenen SOW, Bestellformularen oder Nebenbriefen überein?** Konflikte kennzeichnen.

### Schritt 5: Rechtsordnungshinweis

IP-Regelungen sind rechtsordnungsabhängig. Kennzeichnen wenn relevant:

- **Urheberpersönlichkeitsrechte:** In Deutschland (und EU) grundsätzlich unveräußerlich (§§ 12–14 UrhG). Nur Nichtausübungsabreden möglich. Bei grenzüberschreitenden Verträgen ist das anwendbare Recht zu klären, da ausländische Rechtsordnungen abweichende Regelungen kennen können.
- **§ 69b UrhG:** Computerprogramme: Bei Arbeitsverhältnissen Nutzungsrechte kraft Gesetzes beim Arbeitgeber — explizite Einräumung für das Sicherheitsgefühl in der Due Diligence aber sinnvoll.
- **Zweckübertragungslehre (§ 31 Abs. 5 UrhG):** Gilt im deutschen Recht automatisch; Common-Law-Jurisdiktionen kennen keine vergleichbare Restriktion.
- **KI-generierte Werke:** Nach deutschem Recht ist Schutzvoraussetzung eine menschliche Schöpfung (§ 2 Abs. 2 UrhG — persönliche geistige Schöpfung). Rein KI-generierte Werke ohne menschlichen schöpferischen Beitrag sind nicht urheberrechtsschutzfähig; eine Rechteübertragungsklausel kann nur Rechte übertragen, die bestehen. Wenn KI-Einsatz wahrscheinlich (Softwareentwicklung, Content, Design): 🟠 Hoch — KI-Nutzungsoffenbarungspflicht und Regelung über KI-Anteile empfehlen.

### Schritt 6: Vermerk zusammenstellen

Format:

```markdown
[ARBEITSERGEBNIS-KOPFZEILE — gemäß Mandatsprofil]

### IP-Klausel-Prüfung: [Vertragspartner] — [Vertragstyp]

**Geprüft:** [Datum]
**Position bei IP:** [Rechtegebend / -empfangend / beides]
**Anwendbares Recht:** [Rechtsordnung]

---

## Ergebnis

[Zwei Sätze. Hält die IP-Zuordnung stand? Was muss zuerst geändert werden?]

**Befunde:** [N]🔴 [N]🟠 [N]🟡 [N]🟢

**Genehmigung erforderlich von:** [Name, gemäß Mandatsprofil]

---

## Rechteübertragungsprüfung

[✅ Unbedenklich | ⚠️ Lücke vorhanden — siehe oben]

---

## Klauseln nach Schweregrad

[Alle Klauselblöcke aus Schritt 3, gruppiert Kritisch → Niedrig]

---

## Klausel-übergreifende Konsistenz

[Befunde aus Schritt 4]

---

## Rechtsordnungshinweis

[Befunde aus Schritt 5]

---

## Weiterleitungshinweise

[Wer genehmigt; was löst automatische Eskalation aus]
```

## Beispiel

**Eingabe:** Werkvertrag mit einem freien Softwareentwickler, der "alle Urheberrechte an den Arbeitsergebnissen überträgt".

**Befund (Auszug):**

> ### Abschnitt 5.1: Rechteübertragungsklausel
>
> **Was sie sagt:** "Der Auftragnehmer überträgt alle Urheberrechte an den Arbeitsergebnissen auf den Auftraggeber."
>
> **Marktstandard:** Einräumung ausschließlicher Nutzungsrechte in allen bekannten und unbekannten Nutzungsarten.
>
> **Risiko:** 🔴 Kritisch
>
> **Warum es darauf ankommt:** Urheberrecht ist nach § 29 UrhG nicht übertragbar. Die Klausel erreicht das angestrebte Ziel nicht. In einer Due-Diligence-Prüfung wird dies auffallen.
>
> **Änderungsvorschlag:**
> "Der Auftragnehmer räumt dem Auftraggeber hiermit das ausschließliche, räumlich, zeitlich und inhaltlich unbeschränkte Nutzungsrecht an allen im Rahmen dieses Vertrags erstellten Arbeitsergebnissen ein, einschließlich des Rechts zur Bearbeitung und Weiterübertragung sowie zur Einräumung von Unterlizenzen."

## Risiken und typische Fehler

- **§ 29 UrhG übersehen:** "Übertragung des Urheberrechts" ist deutschrechtlich unwirksam — nur Nutzungsrechtseinräumung möglich.
- **Zweckübertragungslehre nicht beachtet:** Zu eng gefasste Klauseln schränken spätere Nutzungsarten ein (z. B. keine Streaming-Rechte wenn nur "Vervielfältigung" lizenziert).
- **Urheberpersönlichkeitsrechte ignorieren:** Nichtausübungsabrede vergessen → Risiko späterer Unterlassungsansprüche des Urhebers bei Entstellungen.
- **KI-generierte Werke:** Unklar ob urheberrechtsschutzfähig; Abtretungsklausel ohne KI-Offenbarungspflicht ist Blindflug.
- **Arbeitnehmererfindungen:** Ohne formelle Inanspruchnahme nach § 6 ArbnErfG bleiben Patentrechte beim Erfinder — trotz Vertragsklausel.

## Quellenpflicht

Jede Klauselaussage muss auf eine Norm oder Entscheidung gestützt sein. Pflichtquellen:

- **Gesetze:** §§ 29, 31, 31a, 35, 69b UrhG; §§ 15, 22 PatG; § 27 MarkenG; ArbnErfG
- **Rechtsprechung:** mindestens eine BGH-Entscheidung zur Zweckübertragungslehre oder Nutzungsrechtsreichweite
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Modellannahmen als `[Modellwissen — verifizieren]` kennzeichnen; keine stillen Ergänzungen aus dem Modellwissen ohne Hinweis.

## Triage-Fragen vor IP-Klausel-Pruefung

Bevor die Klauselanalyse beginnt, klaere:
1. Handelt es sich um eine Nutzungsrechtseinraeumung (§ 31 UrhG) oder eine unzulaessige "Uebertragung des Urheberrechts" (§ 29 UrhG)?
2. Sind kuenftige Nutzungsarten von der Einraeumung erfasst (§ 31a UrhG — Schriftformerfordernis, Widerrufsrecht)?
3. Besteht eine Arbeitnehmererfindungs-Komponente (§ 69b UrhG Software, ArbnErfG) die separate Regelung erfordert?
4. Ist die Zweckuebertragungslehre (§ 31 V UrhG) bei zu engen Klauseln zu beachten?

## Aktuelle Rechtsprechung

<!-- AUDIT 27.05.2026: 4 halluzinierte Leitentscheidungen geprüft und bereinigt.
Frontmatter unverändert. Kein Commit. Bearbeiter: Halluzinations-Reparatur-Pipeline. -->

---

## Skill: `mandat-arbeitsbereich`

_Kanzlei mit mehreren Mandanten im gewerblichen Rechtsschutz muss Kontext zwischen Mandaten strikt trennen. Mandatsverwaltung IP-Kanzlei. Prüfraster: Anlegen Auflisten Wechseln Schließen oder Trennen des aktiven Mandats Mandantenkontext für alle Folge-Skills. Output: aktives Mandat gesetzt und bes..._

# Mandatsarbeitsbereich

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

Befehlsargument (erstes Token):

- `neu <kurzzeichen>` — neuen Mandatsarbeitsbereich anlegen
- `liste` — alle Mandate mit Status und aktivem Mandat anzeigen
- `wechseln <kurzzeichen>` — aktives Mandat umstellen
- `schliessen <kurzzeichen>` — Mandat archivieren
- `kein` — von jedem Mandat trennen, auf Praxisebene arbeiten

## Rechtlicher Rahmen

### Berufsrechtliche Rahmenbedingungen

- **§ 43a Abs. 2 BRAO** — Verschwiegenheitspflicht des Rechtsanwalts; Mandatsgeheimnis; Grundlage der Mandatskontexttrennung
- **§ 43a Abs. 4 BRAO** — Verbot der Vertretung widerstreitender Interessen (Interessenkonflikt); Mandate müssen getrennt geführt werden
- **§ 203 Abs. 1 Nr. 3 StGB** — Verletzung von Privatgeheimnissen durch Rechtsanwälte; strafrechtliche Absicherung der Vertraulichkeit
- **§ 50 BRAO** — Aufbewahrungspflichten für Handakten (mind. 5 Jahre); Archivierung schließt Mandatsarbeitsbereiche nicht; Löschung ist ausgeschlossen
- **§ 2 BORA** — Berufsrechtliche Pflichten; Grundsatz der anwaltlichen Unabhängigkeit

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Kommentare

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Feuerich/Weyland/Böhnlein, BRAO, 10. Aufl. 2022, § 50 Rn. 1 ff. (Handaktenaufbewahrung)

## Ablauf

### Schritt 1: Vorbedingung prüfen

Praxiskonfigurationsdatei lesen. Falls `Mandatsarbeitsbereiche: ✗` (Standardeinstellung für Inhouse-Teams):

> Mandatsarbeitsbereiche sind deaktiviert — Sie sind als Inhouse-Praxis mit einem Mandanten konfiguriert; das Plugin arbeitet automatisch auf Praxisebene. Wenn Sie tatsächlich über mehrere externe Mandate hinweg arbeiten, führen Sie das Erstkonfigurationsgespräch erneut aus und wählen Sie die Kanzlei-Einstellung. Andernfalls benötigen Sie `/gewerblicher-rechtsschutz:gewerblicher-rechtsschutz-mandat-arbeitsbereich` nicht.

Kein Fehler — der deaktivierte Zustand ist der erwartete für Inhouse-Nutzer.

### Schritt 2: Befehlsverarbeitung

Auf das erste Token des Arguments dispatchen.

---

#### Befehl `neu <kurzzeichen>`

1. Prüfen, ob das Kurzzeichen nicht bereits in `mandate/<kurzzeichen>/` oder `mandate/_archiv/<kurzzeichen>/` vorhanden ist. Bei Kollision: anderen Namen wählen lassen.
2. Aufnahmeinterview durchführen (in einem Durchgang):
 - **Mandant** — vertretene Partei oder interne Geschäftseinheit
 - **Gegenpartei** — andere Seite (kann mehrere umfassen; kann "unbekannter Drittverletzer" bei Watch-Treffern sein)
 - **Mandatstyp** — für gewerblichen Rechtsschutz: Markenschutz / Markenverletzung / Schutzrechtsübertragung / Patentverletzung / FTO-Gutachten / IP-Klauselprüfung / OSS-Compliance / Portfolioverwaltung / Störerhaftung / Sonstiges
 - **Vertraulichkeitsstufe** — standard | erhöht | Clean-Team (erhöht bei besonderer Sensibilität, Clean-Team häufig bei FTO-Gutachten und Patentkäufen)
 - **Wesentliche Tatsachen** — 2–5 Sätze: Worum geht es, wer sind die Beteiligten, was steht auf dem Spiel
 - **Mandatsspezifische Abweichungen von der Standardposition** (z. B. "Mandant wünscht nur schriftliche Kommunikation", "Gegenpartei ist Geschäftspartner — maßvoller Ton")
 - **Verbundene Mandate** — Kurzzeichen zusammenhängender Mandate
3. `mandate/<kurzzeichen>/mandat.md` mit der unten angegebenen Vorlage schreiben.
4. `mandate/<kurzzeichen>/verlauf.md` mit einem einzigen Eröffnungseintrag anlegen.
5. Leere `mandate/<kurzzeichen>/notizen.md` anlegen.
6. **Nicht** automatisch zum neuen Mandat wechseln. Fragen: "Möchten Sie jetzt zu `<kurzzeichen>` wechseln?"

---

#### Befehl `liste`

`mandate/*/mandat.md` aufzählen. Aus jeder Datei Status und Kurzzeichen entnehmen. Tabelle ausgeben:

| Kurzzeichen | Mandant | Mandatstyp | Status | Eröffnet | Aktiv |
|---|---|---|---|---|---|

Aktives Mandat mit `*` markieren. `_archiv/*` unter gesonderter Überschrift "Archivierte Mandate" anführen.

---

#### Befehl `wechseln <kurzzeichen>`

1. Prüfen, ob `mandate/<kurzzeichen>/mandat.md` vorhanden. Falls nicht: `neu <kurzzeichen>` anbieten.
2. `Aktives Mandat:`-Zeile in der Praxiskonfigurationsdatei auf `<kurzzeichen>` aktualisieren.
3. Dem Nutzer die mandat.md-Zusammenfassung zeigen, damit er das richtige Mandat bestätigen kann.

---

#### Befehl `schliessen <kurzzeichen>`

1. `mandate/<kurzzeichen>/` auf Existenz prüfen.
2. "Geschlossen"-Eintrag mit aktuellem Datum an `mandate/<kurzzeichen>/verlauf.md` anhängen.
3. `mandate/<kurzzeichen>/` nach `mandate/_archiv/<kurzzeichen>/` verschieben.
4. War das geschlossene Mandat das aktive Mandat: `Aktives Mandat:` auf `kein — nur Praxisebene` setzen.

---

#### Befehl `kein`

`Aktives Mandat:` in der Praxiskonfigurationsdatei auf `kein — nur Praxisebene` setzen. Bestätigung an den Nutzer.

## Parteien

**Mandant:** [Name]
**Gegenpartei:** [Name(n)]

## Mandatstyp

[Markenschutz / Markenverletzung / FTO-Gutachten / Patentverletzung / IP-Klauselprüfung / OSS-Compliance / Portfolioverwaltung / Störerhaftung / Sonstiges — mit einzeiliger Begründung]

## Wesentliche Tatsachen

[2–5 Sätze. Worum geht es. Wer sind die Beteiligten. Was steht auf dem Spiel. Was macht dieses Mandat vom Standard abweichend.]

## Mandatsspezifische Abweichungen

*Jede Abweichung von der Praxisstandposition, die nur für dieses Mandat gilt.*

- [z. B. "Durchsetzungsstrategie: hier maßvoll, obwohl Hausstandard aggressiv — Gegenpartei ist wichtiger Handelspartner."]
- [z. B. "Genehmigung für Abmahnungen: zusätzliche Freigabe durch Mandant erforderlich."]
- [z. B. "Clean-Team: Mandatsakten auch bei aktiviertem mandatsübergreifendem Kontext nicht lesbar."]

## Verbundene Mandate

- [kurzzeichen — einzeilige Begründung]

## Vertraulichkeitshinweise

[Bei erhöhter oder Clean-Team-Stufe: warum. Wer darf die Mandatsakten einsehen. Ob mandatsübergreifender Kontext zulässig ist.]
```

### Vorlage `verlauf.md`

```markdown
### Verlauf: [Mandant] — [Kurzbeschreibung]

Nur-Anhänge-Ereignisprotokoll. Neuestes oben.

---

## [JJJJ-MM-TT] — Mandat eröffnet

Aufnahme abgeschlossen. Kurzzeichen: `[kurzzeichen]`. Status: aktiv.
[Ggf. initialer Kontext — z. B. "Eröffnet nach Watch-Treffer auf `APEXLEAF` in Klasse 25."]
```

## Beispiel

**Eingabe:** `/gewerblicher-rechtsschutz:gewerblicher-rechtsschutz-mandat-arbeitsbereich neu bmw-marke-2026`

**Verarbeitung:**
Kurzzeichen prüfen → Aufnahmeinterview starten → `mandat.md` erstellen → `verlauf.md` mit Eröffnungseintrag anlegen → Nutzer fragen, ob zum neuen Mandat gewechselt werden soll.

**Ausgabe (Auszug):**

> Mandatsarbeitsbereich `bmw-marke-2026` angelegt.
>
> | Kurzzeichen | Mandant | Mandatstyp | Status | Eröffnet |
> |---|---|---|---|---|
> | bmw-marke-2026 | BMW AG | Markenschutz | aktiv | 2025-07-15 |
>
> Möchten Sie jetzt zu `bmw-marke-2026` wechseln?

## Risiken und typische Fehler

- **Interessenkonflikte nicht erkennen:** Diese Skill führt keine Interessenkonfliktprüfung durch — das ist Aufgabe des Anwalts und der Kanzlei. Die Aufnahme erfasst nur, was der Nutzer angibt.
- **Archivierung ist keine Löschung:** Geschlossene Mandate bleiben lesbar (§ 50 BRAO — Aufbewahrungspflicht mindestens 5 Jahre). Retention-Policy ist außerhalb des Skill-Umfangs.
- **Mandatsübergreifender Kontext standardmäßig aus:** Die Praxiskonfiguration hat ein `Mandatsübergreifender Kontext:`-Flag. Standardmäßig `aus` — Skill A im Mandat X liest niemals Dateien aus Mandat Y. Das ist die Vertraulichkeitsgarantie.
- **Kurzzeichen-Kollision mit Archiv:** Wird ein Kurzzeichen wiederverwendet, das im Archiv liegt, wird das archivierte Mandat unter `_archiv/<kurzzeichen>/` bewahrt; das neue erhält einen anderen Namen.

## Quellenpflicht

Alle Aussagen zu Vertraulichkeit, Aufbewahrung und Interessenkonflikten müssen auf konkreten Normen beruhen:

- **§ 43a BRAO** (Verschwiegenheit), **§ 43a Abs. 4 BRAO** (widerstreitende Interessen), **§ 203 StGB** (Verletzung von Privatgeheimnissen), **§ 50 BRAO** (Handaktenaufbewahrung)
- Modellannahmen als `[Modellwissen — verifizieren]` kennzeichnen.

## Triage-Fragen bei Mandatseröffnung

Bevor das Mandat angelegt wird, klaere:
1. Ist ein Interessenkonflikt-Check (§ 43a IV BRAO) durchgefuehrt worden?
2. Sind die wesentlichen Mandatsdaten vollstaendig (Mandant, Gegner, Rechtsgebiet, Streitgegenstand)?
3. Wurde der Mandant ueber Honorar und Kostenrisiko aufgeklaert (§ 49b BRAO, § 34 RVG)?
4. Laeuft bereits eine Frist (z.B. Widerspruchsfrist Marke, Abmahnungsfrist), die sofort ins Fristenbuch muss?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

<!-- AUDIT 27.05.2026
Task: Bundle 031 / Halluzinations-Reparatur
Korrektur: Zitat aus "Aktuelle Rechtsprechung"-Block entfernt (bei Zweifel loeschen).
-->

---

## Skill: `markenrecherche`

_Unternehmen oder Mandant plant neue Marke oder Produktname und fragt: Bestehen Kollisionsrisiken mit aelteren Marken? Markenrecherche vor Anmeldung. Prüfraster: Identitäts- und Aehnlichkeitsprüfung DPMAregister EUIPO eSearch+ WIPO Global Brand DB Warenklassen. Ergebnis Recherchepaket für anwaltli..._

# Markenrecherche (Clearance)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Zu prüfendes Zeichen (Wort, Bildmarke, kombiniertes Zeichen, Slogan, Farbe, Form)
- Gewünschte Waren- und Dienstleistungsklassen (Nizza-Klassifikation, 12. Ausgabe)
- Zielländer / Zieljurisdiktionen (DE, EU/EUTM, international/Madrid)
- Verwendungskontext und Branche
- Geplanter Anmeldetag (relevant für Priorität)
- Ggf. bereits bekannte Voreintragungen

## Ablauf

### 1. Zeichen qualifizieren

Art des Zeichens bestimmen und Schutzfähigkeit vorprüfen:

| Zeichenart | Schutzfähigkeitshinweis |
|---|---|
| Wortmarke (Fantasiebegriff) | i. d. R. schutzfähig; Prüfung auf absolute Schutzhindernisse |
| Wortmarke (beschreibend) | Schutzhindernis § 8 Abs. 2 Nr. 2 MarkenG; Art. 7 Abs. 1 lit. c UMV; Verkehrsdurchsetzung möglich |
| Bildmarke / Logo | Schutz für bildliche Gestaltung; Wortbestandteile separat prüfen |
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
| Dreidimensionale Marke | Funktionale Formen vom Schutz ausgeschlossen (§ 3 Abs. 2 MarkenG) |

Absolute Schutzhindernisse prüfen (§ 8 MarkenG; Art. 7 UMV): Fehlende Unterscheidungskraft, beschreibende Angaben, täuschende Angaben, Gattungsbezeichnungen.

### 2. Datenbankrecherche durchführen

**Pflicht-Datenbanken:**

| Datenbank | URL | Zweck | Jurisdiktion |
|---|---|---|---|
| DPMAregister | register.dpma.de | Nationale DE-Marken; Wort-/Bildsuche | Deutschland |
| EUIPO eSearch+ | euipo.europa.eu/eSearch | Unionsmarken (EUTM); auch ältere IR-Marken mit EU-Wirkung | EU |
| WIPO Global Brand DB | branddb.wipo.int | Internationale Registrierungen (Madrid-System); Protokollmarken | International |

**Ergänzende Recherche:**
- Gemeinsame Datenbank EPA/DPMA (für Gemeinschaftsmarken mit nationaler Wirkung)
- Handelsregister (Unternehmensbezeichnungen als relative Schutzhindernisse)
- Domainregistrierungen (nicht Markenrecht, aber Abmahn- und Verwechslungsrisiko)
- Unregistrierte Kennzeichen / bekannte Marken (§ 4 Nr. 3 MarkenG)

**Suchstrategie:**
1. **Identitätssuche:** exaktes Zeichen suchen
2. **Phonetische Ähnlichkeit:** Klangähnliche Schreibweisen (z. B. APEXBLATT / APEX BLATT / APEXBLAT)
3. **Visuelle Ähnlichkeit:** Bei Bildmarken ähnliche Gestaltungen
4. **Konzeptionelle Ähnlichkeit:** Sinnverwandte Begriffe (z. B. BLATT / LEAF)
5. **Klassenschwerpunkt:** Identische und benachbarte Klassen

### 3. Kollidierende Zeichen analysieren – Verwechslungsfaktoren

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Faktoren der Verwechslungsgefahr (§ 9 Abs. 1 Nr. 2 MarkenG; Art. 8 Abs. 1 lit. b UMV):**

| Faktor | Erhöht Verwechslungsgefahr | Verringert Verwechslungsgefahr |
|---|---|---|
| Zeichenähnlichkeit | Klang, Schriftbild oder Bedeutung ähnlich | Deutliche Unterschiede in allen Ebenen |
| Waren-/Dienstleistungsähnlichkeit | Identische oder eng verwandte Klassen | Unterschiedliche Branchen/Zielgruppen |
| Kennzeichnungskraft | Starke inhärente oder erworbene Unterscheidungskraft | Schwache, beschreibende Marke |
| Verkehrskreis | Allgemeinheit, geringere Aufmerksamkeit | Fachkreise, hohe Aufmerksamkeit |
| Aufmerksamkeitsgrad | Niedrigpreisig, impulsiv | Hochpreisig, sorgfältige Kaufentscheidung |

**Zeichenähnlichkeit – Detailprüfung:**
- Klangliche Ähnlichkeit: Vokal- und Silbenstruktur, Akzentuierung, dominierender Bestandteil
- Schriftbildliche Ähnlichkeit: Buchstabenfolge, Länge, Groß-/Kleinschreibung
- Konzeptionelle Ähnlichkeit: Bedeutungsgehalt; bei Fantasiebegriffen ohne Bedeutung entfällt dieser Aspekt
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 4. Risikobewertung erstellen

Jede kollidierende Voreintragung mit Ampelfarbe bewerten:

🔴 **Blocking (hohes Risiko):** Identische oder sehr ähnliche Marke in identischen/ähnlichen Klassen; starke Kennzeichnungskraft; anwaltliche Empfehlung: Anmeldung ohne Umgestaltung nicht empfehlenswert.

🟠 **Hoch:** Ähnliche Marke; Verwechslungsgefahr nicht ausschließbar; Abstandsvergrößerung prüfen; Anmeldeentscheidung nach anwaltlicher Würdigung.

🟡 **Mittel:** Einige Ähnlichkeiten; Verwechslungsgefahr zweifelhaft; Recherche nach weiteren Belegen; ggf. Koexistenzvereinbarung möglich.

🟢 **Niedrig:** Nur entfernte Ähnlichkeit; Klassen-/Warenabstand deutlich; geringe Risiken verbleiben; für abschließende Beurteilung Anwalt erforderlich.

### 5. Ausgabe erstellen

Recherchebericht mit:
- Zusammenfassung der verwendeten Datenbanken und Rechercheparameter
- Tabelle der gefundenen kollidierenden Zeichen (mit Registernummern, Inhabern, Klassen, Bewertung)
- Analyse der Top-3-Risikotreffer im Gutachtenstil
- Offene Fragen für Anwalt
- Entscheidungsbaum

## Quellen und Zitierweise

Zitierweise nach `../references/zitierweise.md`.

**Normen:** §§ 4, 5, 8, 9, 14, 26 MarkenG; Art. 7, 8 VO (EU) 2017/1001 (UMV).

**Leitentscheidungen:**
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Ingerl/Rohnke, MarkenG, 3. Aufl. 2010, § 9 Rn. 165 ff.; § 14 Rn. 345 ff. `[Modellwissen – prüfen; neuere Rspr. beachten]`
- Ströbele/Hacker/Thiering, MarkenG, 13. Aufl. 2021, § 9 Rn. 95 ff.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Beispiel (Gutachtenstil)

**Geplantes Zeichen:** NORDBLATT, angemeldet für Kl. 25 (Bekleidung), Kl. 35 (Einzelhandel)

**Recherche DPMAregister:** Treffer: "NORDBLATT" (DPMA-Reg.-Nr. 30 2015 053 422), Inhaber: N.N. GmbH, Kl. 25, Status: eingetragen.

**Analyse:**

*Zeichenähnlichkeit:* Klangliche, schriftbildliche und konzeptionelle Identität (identische Wortmarke). Höchste Ähnlichkeitsstufe.

*Waren-/Dienstleistungsähnlichkeit:* Kl. 25 identisch.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

🔴 **Bewertung: Blocking.** Identische Eintragung in identischer Klasse. Anmeldung unter diesem Zeichen nicht empfehlenswert ohne Abstandsvergrößerung oder vorherige Freigabe durch Inhaber.

## Risiken / typische Fehler

- **Nur DPMA prüfen:** Unionsmarken haben automatisch Wirkung in Deutschland; EUIPO-Recherche ist Pflicht.
- **Klassen zu eng ansetzen:** Ähnliche Waren in Nachbarklassen können Verwechslungsgefahr begründen; nicht nur Wunschklassen, sondern auch benachbarte prüfen.
- **Benutzungsschonfrist ignorieren:** Ältere Marken, die nicht ernsthaft benutzt werden (§ 26 MarkenG), können auf Löschungsantrag angegriffen werden; eingetragene, aber nichtbenutzte Marken sind kein absolutes Hindernis.
- **Unregistrierte Rechte übersehen:** Firmennamen (§ 5 Abs. 2 MarkenG), Werktitel (§ 5 Abs. 3 MarkenG), bekannte Marken (§ 4 Nr. 3 MarkenG) schützen auch ohne Eintragung.
- **Dieses Ergebnis ist kein Freigabegutachten:** Die Bewertung ist eine Erste-Triage. Eine abschließende Freigabeentscheidung erfordert anwaltliche Prüfung; für wichtige Marken kommt ein formelles Gutachten in Betracht.

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `schutzrechts-portfolio-schutzschrift`

_Unternehmen oder Kanzlei muss IP-Portfolio verwalten und anstehende Fristen im Blick behalten. Schutzrechtsportfolio-Verwaltung. Prüfraster: Eintragungen Verlaengerungen Jahresgebühren Benutzungsnachweise Fristkalender. Output: Fristenkalender und Portfolio-Audit mit Luecken Verfall und Benutzung..._

# IP-Portfolio-Verwaltung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

Befehlsargument:

- `--bericht [--tage N]` — Fristen im Berichtsfenster (Standard: 90 Tage)
- `--hinzufuegen` — neues Schutzrecht interaktiv erfassen
- `--aktualisieren` — Amtshandlung, Gebührenzahlung oder Statusänderung erfassen
- `--prüfung` — umfassende Portfolioprüfung
- (kein Argument) — entspricht `--bericht`

## Rechtlicher Rahmen

### Kernvorschriften — Fristen und Verlängerungen

**Marken:**
- **§ 47 Abs. 1 MarkenG** — Schutzdauer: 10 Jahre ab Anmeldetag, danach jeweils weitere 10 Jahre
- **§ 47 Abs. 3 MarkenG** — Verlängerung durch Zahlung der Verlängerungsgebühr; Schonfrist 6 Monate mit Zuschlag (§ 7 PatKostG)
- **Art. 53 UMV (Unionsmarkenverordnung EU 2017/1001)** — Schutzdauer Unionsmarke 10 Jahre; Verlängerung beim EUIPO
- **Art. 7 MMA / Regel 30 GAFO** — Madrid-System: 10-jährige internationale Registrierung; Verlängerung beim WIPO; individuelle Wirkungsländer-Fristen beachten
- **§ 26 MarkenG** — Benutzungszwang; nach 5 Jahren Löschungsrisiko bei ernsthafter Nichtbenutzung (§ 49 MarkenG)

**Patente:**
- **§ 17 PatG** — Patentlaufzeit: 20 Jahre ab Anmeldetag; Aufrechterhaltung durch jährliche Jahresgebühren (§ 17 Abs. 1 i. V. m. PatKostG Anlage)
- **§ 20 Abs. 1 Nr. 3 PatG** — Erlöschen bei Nichtzahlung der Jahresgebühr
- **§ 17 Abs. 2 PatG** — Schonfrist: 6 Monate mit Zuschlag
- **Regel 51 EPÜ / Art. 86 EPÜ** — EP-Patent: Jahresgebühren beim nationalen Amt ab dem 3. Jahr nach Anmeldetag; Nationalisierung innerhalb von 31 Monaten (PCT)
- **§ 13 GebrMG** — Gebrauchsmuster: Schutzdauer 3 Jahre ab Anmeldetag, verlängerbar auf max. 10 Jahre (je +3/+2 Jahre)

**Designs:**
- **§ 27 DesignG** — Schutzdauer: 5 Jahre ab Anmeldetag, verlängerbar bis max. 25 Jahre in 5-Jahres-Schritten
- **Art. 12 GGV (Gemeinschaftsgeschmacksverordnung EU 6/2002)** — Eingetragenes Gemeinschaftsgeschmacksmuster (EGGM): 5 Jahre ab Anmeldedatum, verlängerbar bis max. 25 Jahre

**Urheberrecht:**
- **§ 64 UrhG** — Schutzfrist: 70 Jahre nach Tod des Urhebers; keine aktive Verlängerung erforderlich
- **§§ 70–72 UrhG** — Verwandte Schutzrechte: abweichende Fristen

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Kommentare

- Ingerl/Rohnke, MarkenG, 3. Aufl. 2010, § 47 Rn. 1 ff. (Schutzdauer und Verlängerung), § 49 Rn. 1 ff. (Löschung wegen Nichtbenutzung)
- Benkard/Rogge, PatG, 12. Aufl. 2023, § 17 Rn. 1 ff. (Laufzeit und Jahresgebühren)
- Eichmann/Jestaedt/Fink/Meiser, DesignG, 6. Aufl. 2019, § 27 Rn. 1 ff. (Schutzdauer und Verlängerung)

## Ablauf

### Modus 1: Initialisierung (bei leerem Register oder `--neu`)

1. Quelle bestimmen: IP-Verwaltungssystem angebunden (Anaqua, Dennemeyer, Patronas, CPA Global)? Falls ja: Portfolio über Integration beziehen. Falls nein: Tabelle / Export anfordern oder interaktiv durchführen.
2. Für jedes Schutzrecht Fristen berechnen (Regeln unten). `nächste_fristen` mit den zwei bis drei nächsten Fälligkeiten befüllen.
3. Register schreiben. Zusammenfassung ausgeben:

```
Portfolio-Register initialisiert.

Schutzrechte: [N]
 Marken: [N] ([N eingetragen] / [N angemeldet])
 Patente: [N] ([N erteilt] / [N angemeldet])
 Designs: [N]
 Domains: [N]

Fristen berechnet: [N]
Anwaltlich verwaltet / Zuständigkeit TBD: [N] — mit Korrespondenzanwalt bestätigen
Unbekannt (Daten fehlen): [N] — vor Verlassen auf Berichte ergänzen

`--bericht` ausführen für Übersicht.
```

### Modus 2: Bericht (`--bericht [--tage N]`)

Standard: 90 Tage. Berechnete Fristen vor Berichtserstellung für jedes Schutzrecht aktualisieren.

Ausgabe (Arbeitsergebnis-Kopfzeile voranstellen):

```
IP-PORTFOLIO-FRISTENBERICHT — [Datum]
[Unternehmensname] — Fenster: nächste [N] Tage

🔴 ERLOSCHEN / IN SCHONFRIST ([N])
 [ID] / [Behörde] / [Typ] / [Bezeichnung]
 [Handlung] — ursprünglich fällig [Datum], Schonfrist endet [Datum]
 Status: [schonfrist / erloschen]

⏰ FÄLLIG INNERHALB [N] TAGE ([N])
 [ID] / [Behörde] / [Typ] / [Bezeichnung]
 [Handlung] — fällig [Datum]
 Grundlage: [z. B. "10. Jahrestag der Anmeldung, § 47 Abs. 1 MarkenG"]
 [Anwalt: Kanzlei / Aktenzeichen — falls vorhanden]

🟡 BEVORSTEHEND (über 30 Tage, innerhalb [N] Tage)
 [Liste]

🌐 ANWALTLICH VERWALTET ([N])
 [ID] / [Behörde] — verwaltet von [Korrespondenzanwalt]; direkt bestätigen
 [ID] / [Behörde] — kein Korrespondenzanwalt eingetragen; mit --aktualisieren ergänzen

❓ UNBEKANNT ([N])
 [ID] — fehlendes [Feld]; Frist nicht berechenbar
 Vor Verlassen auf diesen Bericht mit [DPMA / EUIPO / WIPO] abgleichen.

ZUSAMMENFASSUNG
 Schutzrechte gesamt: [N]
 Fristen im Fenster: [N]
 Letzte Portfolioprüfung: [Datum]
```

Schlusssatz: *"Aus Portfolio-Register berechnet. Jede Frist vor Handlung gegen DPMA DPMAdirektplus, EUIPO eSearch, WIPO Madrid Monitor oder das jeweilige Behördenregister verifizieren."*

### Modus 3: Hinzufügen (`--hinzufuegen`)

Interaktive Erfassung eines neuen Schutzrechts. Abfragen:

1. Typ (Marke / Patent / Gebrauchsmuster / Design / Urheberrecht / Domain)
2. Behörde / Jurisdiktion (DPMA, EUIPO, WIPO Madrid, EPO, national)
3. Bezeichnung / Erfindungstitel
4. Inhaber (eingetragene Rechtsperson — relevant für Validitätsprüfungen und Zuordnung)
5. Schlüsseldaten (je nach Typ: Anmelde-, Eintragungstag, Erteilungstag, Prioritätstag, Ablaufdatum)
6. Aktenzeichen(n)
7. Klassen / Ansprüche (Nizza-Klassen für Marken; IPC/CPC für Patente)
8. Quelle — wird im IP-Verwaltungssystem unter einer Aktennummer geführt?
9. Externer Patentanwalt / Korrespondenzanwalt falls vorhanden
10. Fachbereich-Zuständiger im Unternehmen

Nach Erfassung: Fristen nach den Regeln oben berechnen. Falls Jurisdiktion nicht eingebaut: `eigene_regeln`-Flow (unten).

**Eigene Regeln für unbekannte Jurisdiktionen:**

> Für [Jurisdiktion] / [Typ] sind die Aufrechterhaltungsregeln nicht eingebaut. Bitte angeben:
>
> 1. Welche Ereignisse sind fristen-relevant? (Verlängerung alle N Jahre? Jahresgebühren jährlich? Benutzungsnachweise? Sonstiges?)
> 2. Was löst das Fälligkeitsdatum aus — Anmelde-, Eintragungstag, nationaler Phase-Eintritt, etwas anderes?
> 3. Gibt es eine Schonfrist? Mit welchem Zuschlag?
> 4. Verwaltet ein Korrespondenzanwalt dieses Schutzrecht?

Unter `eigene_regeln:` speichern; auf zukünftige Schutzrechte dieser Jurisdiktion anwenden.

### Modus 4: Aktualisieren (`--aktualisieren`)

**Entscheidungs-Gate vor Statusänderung:** Bevor eine Amtshandlung oder Gebührenzahlung als "eingereicht" erfasst wird — falls der Nutzer kein Rechtsanwalt ist:

> Das Erfassen einer Marken­verlängerung, Jahresgebühr oder Gebrauchsmuster­verlängerung als "eingereicht" hat Konsequenzen. Wenn die Erfassung falsch ist — versäumtes Fristdatum, falsche Gebührenhöhe, fehlender Nachweis — verschiebt sich die Frist nicht und das Schutzrecht kann erlöschen. Haben Sie die Handlung mit dem zuständigen Patentanwalt oder Korrespondenzanwalt bestätigt (oder über DPMA DPMAdirektplus / EUIPO / WIPO überprüft)? Wenn ja: weiter. Wenn nein:
>
> - Noch nicht als eingereicht erfassen.
> - Folgendes zum Anwalt/Korrespondenzanwalt: Schutzrechts-ID, Behörde, Fristtyp, was das IP-Verwaltungssystem zeigt, was Ihrer Überzeugung nach eingereicht wurde und wann, und die Quelle dieser Überzeugung.

Kein `status: eingereicht` ohne ausdrückliches Ja über dieses Gate.

**Teilmodi:**

- **Manuelle Aktualisierung:** "Wir haben die Verlängerung von TM-DPMA-001 am 3. Juli eingereicht, Nachweis beigefügt." → Entsprechende Frist auf `status: eingereicht`, `eingereichtes_datum` setzen; nächste Frist im Lebenszyklus berechnen.
- **Statusänderung:** "Bitte TM-EUIPO-004 als aufgegeben markieren." → `status` aktualisieren, `nächste_fristen` leeren, Datum notieren.
- **IP-System-Abgleich:** Falls Anaqua / Dennemeyer / CPA Global angebunden: aktuellen Datenstand ziehen, abgleichen. Abweichungen kennzeichnen — System of Record gewinnt.

### Modus 5: Portfolioprüfung (`--prüfung`)

Umfassende Gesundheitsprüfung über die nächsten Monatsfristen hinaus:

**Fristenhygiene**
- Fristen derzeit in `schonfrist`-Status? (Handlung möglich, aber Zuschlag anfallend.)
- Erloschenene Schutzrechte, die nicht als aufgegeben / gelöscht markiert sind? Entweder wiederbeleben oder Status aktualisieren.
- Schutzrechte ohne berechnete `nächste_fristen`? Fehlende Daten oder unbekannte Jurisdiktion.

**Eintragungslücken**
- Markenanmeldungen älter als 18 Monate noch `angemeldet`? Amtsstatus prüfen — ggf. Beanstandungen zu beantworten.
- Patentanmeldungen älter als 4 Jahre noch `angemeldet`? Prüfungsstand prüfen.

**Benutzung (Marken)**
- §-49-MarkenG-Risiko: Marken, deren Verlängerung näher rückt und für die `benutzung_nachgewiesen: false` oder unklar? Die Verlängerung erfordert keine Benutzungsnachweise, aber der Löschungsanspruch Dritter entsteht nach 5 Jahren ernsthafter Nichtbenutzung. Benutzungsaudit vor Verlängerungsentscheidung empfehlen.

**Inhaberhygiene**
- Schutzrechte, bei denen `inhaber` keine aktive Gesellschaft ist (Umfirmierung, Verschmelzung, Spaltung)? Ggf. Umschreibung beim Amt (§ 28 MarkenG; § 30 PatG) erforderlich.
- Inhaberbezeichnungen inkonsistent über Schutzrechte hinweg? Für Bereinigung kennzeichnen.

**Ablaufhorizont (24 Monate)**
- Patente, die in 24 Monaten auslaufen? Auch ohne Jahresgebühr-Frist geschäftsrelevant — Produktplanung, Fortsetzungsstrategie, Lizenzierungsfenster.

**Nicht überwachte Schutzrechte**
- Eingetragene Marken, die nicht im Watch-Service des Mandatsprofils aufgeführt sind? Als Lücke für anwaltliche Entscheidung markieren.

Ausgabeformat:

```
IP-PORTFOLIOPRÜFUNG — [Datum]

FRISTENHYGIENE
 In Schonfrist: [N] — sofortige Handlung vermeidet Erlöschen
 Erloschen (nicht als aufgegeben markiert): [N] — Status bestätigen
 Fehlende Fristenberechnung: [N] — Daten ergänzen oder anwaltlich verwalten markieren

EINTRAGUNGSLÜCKEN
 Markenanmeldungen > 18 Monate anhängig: [Liste]
 Patentanmeldungen > 4 Jahre anhängig: [Liste]

BENUTZUNG (MARKEN)
 § 49 MarkenG — Löschungsrisiko bei anhängenden Verlängerungen und unklarer Benutzung: [Liste]

INHABER
 Schutzrechte mit nicht aktiver/unklarer Inhaberbezeichnung: [N]
 Inhaber-Bezeichnungsinkonsistenzen: [Liste]

ABLAUFHORIZONT (24 MONATE)
 Ablaufende Patente: [Liste]

MARKEN-WATCH
 Eingetragene Marken nicht im Watch-Service: [Liste]

EMPFOHLENE MASSNAHMEN
 1. [höchste Priorität]
 2. [etc.]
```

## Beispiel

**Eingabe:** `/gewerblicher-rechtsschutz:schutzrechts-portfolio` (kein Argument)

**Ausgabe (Auszug):**

> IP-PORTFOLIO-FRISTENBERICHT — 2025-07-15
> Fenster: nächste 90 Tage
>
> ⏰ FÄLLIG INNERHALB 90 TAGE (2)
> TM-DPMA-012 / DPMA / Marke / ALPHAWAVE
> Verlängerung § 47 Abs. 1 MarkenG — fällig 2025-08-20
> Grundlage: 10. Jahrestag der Eintragung
>
> PAT-EP-003 / EPO / Patent / Verfahren zur Datenübertragung
> Jahresgebühr Jahr 5 — fällig 2025-09-01
> Grundlage: Art. 86 EPÜ; Zahlung beim nationalen Amt (DPMA)
>
> *Berechnungen aus Portfolio-Register. Vor Handlung gegen DPMA DPMAdirektplus / EUIPO eSearch / WIPO Madrid Monitor verifizieren.*

## Risiken und typische Fehler

- **Berechnete Frist ist nicht die amtliche Frist:** Das Register ist eine Arbeitskopie; das Behördenregister ist die Quelle der Wahrheit. Eine falsch eingetragene Frist erzeugt falsches Sicherheitsgefühl.
- **Schonfrist als Normalzustand:** Schonfristgebühren sind Zusatzkosten; regelmäßige Nutzung der Schonfrist ist Ineffizienz, nicht Praxis.
- **Benutzungszwang übersehen:** § 26 MarkenG — Marke ohne ernsthafte Benutzung nach 5 Jahren löschbar (§ 49 MarkenG). Portfolio-Verlängerung setzt keine Benutzungsprüfung voraus — aber das Löschungsrisiko entsteht trotzdem.
- **Inhaberumbenennung/-umschreibung vergessen:** Nach Umfirmierung oder Umstrukturierung müssen Schutzrechte beim Amt umgeschrieben werden, sonst entstehen Validitätsrisiken.
- **PCT-Nationale-Phase-Fristen:** 30/31-Monatsfrist (Regel 22.1 PCT) ist hart — kein Wiedereinsetzen bei Versäumnis in den meisten Ländern.

## Quellenpflicht

Alle Fristenangaben müssen auf konkreten Normen beruhen. Pflichtquellen:

- **Gesetze:** § 47 MarkenG, § 17 PatG, § 13 GebrMG, § 27 DesignG; Art. 53 UMV; Art. 12 GGV; Art. 86 EPÜ; PatKostG
- **Rechtsprechung:** mindestens eine BGH-Entscheidung zu Markenfristen oder Jahresgebühren
- **Kommentar:** Ingerl/Rohnke MarkenG oder Benkard PatG mit § und Randnummer
- Modellannahmen als `[Modellwissen — verifizieren]` kennzeichnen.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `schutzschrift-eilverfuegung`

_Mandant hat Abmahnung oder Verletzungsschreiben erhalten und befürchtet einstweilige Verfuegung ohne Anhörung. § 945a ZPO Schutzschrift ZSER. Prüfraster: Hinterlegung zentrales elektronisches Schutzschriftenregister § 945a ZPO Sachverhalt Gegenrede Glaubhaftmachung eidesstattliche Versicherung We..._

# Schutzschrift gegen Eilverfügung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schritt 1 — Anwendungsbereich

### Wann sinnvoll?

- **Nach Abmahnung** Schadensersatz oder Unterlassungs-Forderung mit Frist
- **Nach Schreiben eines Mitbewerbers** mit Drohung
- **Vor einem Branchen-Event** wo Mitbewerber EV beantragen könnte
- **Bei Marken-Wechsel-Strategie** mit erwartetem Widerstand

### Wann nicht sinnvoll?

- Bei eindeutig zugestandenem Verstoß — kontraproduktiv
- Bei rein theoretischem Risiko — Aufwand verschwendet
- Bei bereits eingereichtem EV-Antrag

## Schritt 2 — Schutzschrift-Register § 945a ZPO

### Zentralregister

- **Bundes-Elektronisches Schutzschriftenregister** (BESR)
- Alle Gerichte greifen darauf zu
- Bei EV-Antrag prüft das Gericht das Register

### Hinterlegung

- Pflicht-Hinterlegung im Register § 945a Abs. 2 ZPO
- Anwalts-Einreichung per beA möglich
- Kosten-Begründung — keine Gebühr für Hinterlegung selbst, aber Bearbeitungs-Aufwand

### Gültigkeit

- **Sechs Monate**
- Verlängerungs-Möglichkeit bei fortbestehender Bedrohung

## Schritt 3 — Aufbau

### Briefkopf

- Mandant als potenziell Antragsgegner
- Bevollmächtigter Anwalt

### Empfänger

- "An die Gerichte" (typisch)
- Konkrete Gerichte können benannt werden

### Betreff

- "Schutzschrift gemäß § 945a ZPO"
- Bezug auf erwarteten Antragsteller und Streitgegenstand

### Sachverhalt

- Aus Mandanten-Sicht erläutert
- Vorzeit-Geschehen
- Bisheriger Schriftwechsel mit potenziellem Antragsteller
- Eigene Bewertung der Sach- und Rechtslage

### Rechtliche Gegenrede

- Erwartete Anträge des Antragstellers
- Argumentation gegen Anspruchsgrundlage
- Argumentation gegen Eilbedürftigkeit
- Argumentation gegen Sicherungs-Anspruch

### Antrag

```
Es wird beantragt:

1. Der Antrag der [potenzielle Antragstellerin] wird abgelehnt.

2. Hilfsweise: Über den Antrag wird mündlich verhandelt
 und der Anhörung der Schutzschrift-Einreicherin
 Gelegenheit gegeben.

3. Höchst hilfsweise: Bei Erlass einer einstweiligen
 Verfügung wird Sicherheit Leistung in angemessener
 Höhe angeordnet.
```

## Schritt 4 — Glaubhaftmachung

### Eidesstattliche Versicherung

- Mandanten-eidesstattliche Versicherung zu Sachverhalts-Komponenten
- Inhaltlich auf Tatsachen beschränken nicht Wertung
- Vor-Anwalt-Beglaubigung

### Urkunds-Beweis

- Vertragsunterlagen
- Schriftverkehr
- Lieferungs-Belege

### Sachverständige

- Sachverständigen-Gutachten beifügen wenn vorhanden

## Schritt 5 — Argumentations-Linien

### Bei Marken-Streit

- Eigene Marken-Rechte
- Verbraucher-Verständnis konkret-bezogen
- Keine Verwechslungs-Gefahr
- Erschöpfungs-Grundsatz § 24 MarkenG

### Bei UWG-Streit

- Aussage nicht irreführend
- Vergleichende Werbung zulässig § 6 UWG
- Keine Marktverhaltens-Verstöße

### Bei Patent-Streit

- Patent möglicherweise nicht rechtsbeständig
- Nichtigkeits-Klage parallel
- Keine Verletzung — kein wortgleich gleichwertig

### Bei Persönlichkeitsrecht-Streit

- Meinungsfreiheit Art. 5 GG
- Tatsachenbehauptung wahr
- Berechtigtes Interesse

## Schritt 6 — Senatsauswahl

### Bei Konkurrenzzuständigkeit

- Mehrere Gerichte können zuständig sein
- Strategische Senatswahl
- Antragsteller wählt das für ihn günstigste Gericht

### Schutzschrift-Strategie

- Schutzschriften bei allen plausiblen Gerichten hinterlegen
- BESR macht das einheitlich möglich

## Schritt 7 — Eilbedürftigkeit angreifen

### Dringlichkeits-Indizien

- **Zeitablauf** zwischen Kenntnisnahme des Verstoßes und EV-Antrag
- München: typisch ein Monat
- Hamburg / Berlin: zwei Monate
- Frankfurt: ein bis zwei Monate
- Düsseldorf: länger toleriert

### Argument bei Eilbedürftigkeits-Verstoß

- Schutzschrift dokumentiert Verzögerung
- Bei Verfahrens-Beginn vorzeigen

## Schritt 8 — Antrag auf Sicherheitsleistung

### § 921 ZPO

- Bei EV-Erlass Sicherheitsleistung anordnen
- Höhe nach Ermessen typisch erheblicher Bruchteil des Streit-Volumens
- Schutz vor missbräuchlicher EV

### Begründung

- Wirtschaftliche Folgen Mandant
- Mögliche Schadensersatz-Rückforderung bei Aufhebung

## Schritt 9 — Praktische Schritte

1. **Drohungs-Analyse** — wer könnte EV beantragen wann wofür?
2. **Sachverhalts-Aufnahme** mit Mandant
3. **Argumentations-Linie** rechtlich
4. **Eidesstattliche Versicherung** vorbereiten
5. **Schutzschrift-Entwurf**
6. **Mandanten-Freigabe**
7. **Hinterlegung beim BESR** per beA

## Schritt 10 — Gegen-Schutzschrift / Reaktion auf Schutzschrift

### Wenn Schutzschrift des Mitbewerbers vorliegt

- Bei eigenem EV-Antrag bedacht reagieren
- Argumente entgegnen
- Ggf. Antrag direkt mit mündlicher Verhandlung

## Schritt 11 — Form-Anforderungen

- **Elektronisch** über beA
- **PDF/A-Format**
- **Anlagen** als separate Dokumente

## Schritt 12 — Kostenrisiko

### Bei nicht-Eintreten EV-Antrag

- Aufwand vergeblich aber häufig sinnvoll als Vorsichtsmaßnahme

### Bei Eintreten EV-Antrag mit Schutzschrift-Erfolg

- Kosten typisch dem Antragsteller
- Eigene Anwaltskosten kann Mandant erstatten erhalten

## Ausgabe

- `schutzschrift-{az}.md` strukturiert
- Eidesstattliche Versicherung Vorlage
- Argumentations-Linie sortiert
- Hinterlegungs-Dokumentation BESR
- Frist im Fristenbuch (sechs Monate Gültigkeit)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellen

- ZPO §§ 921 935 945a
- MarkenG § 24
- UWG § 6
- BGH I. Zivilsenat
- Koehler/Bornkamm/Feddersen UWG
- Ingerl/Rohnke MarkenG

<!-- AUDIT 27.05.2026: Bundle 032 Halluzinations-Reparatur
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
-->

---

## Skill: `start-chronologie-fristen`

_Einstieg, Schnelltriage und Fallrouting im Gewerblicher Rechtsschutz-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigen..._

# Gewerblicher Rechtsschutz — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Gewerblicher Rechtsschutz**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Gewerblicher Rechtsschutz – DPMA/EUIPO-Markenrecherche und -anmeldung, Freedom-to-Operate, Patentscreening, UWG- und Urheberrechts-Abmahnung (Versand und Reaktion), Open-Source-Compliance, IP-Klausel-Review, Schutzrechts-Fristen.

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
| `abmahnung-urheberrecht` | Urheber oder Lizenznehmer erhielt unerlaubte Nutzung (Bild Text Video) oder Mandant erhielt Abmahnung wegen Urheberrechtsverletzung. § 97a UrhG Abmahnung und Unterlassung. Prüfraster: modifizierte… |
| `erfindungsmeldung-aufnahme` | Mitarbeiter meldet eine Erfindung oder Unternehmen prüft eingegangene Erfindungsmeldung. ArbnErfG Arbeitnehmererfindungsgesetz. Prüfraster: Neuheit erfinderische Tätigkeit technischer Charakter EPUe Schutzfähigkeit… |
| `fto-triage` | Unternehmen will Produkt einführen oder Technologie einsetzen und fragt: Verletzen wir fremde Patente? Freedom-to-Operate-Analyse FTO. Prüfraster: Recherche Espacenet DPMApaplus EP-Datenbank sperrende DE- und… |
| `gewerblicher-rechtsschutz-anpassen` | Kanzlei moechte ihr gewerbliches-Rechtsschutz-Profil nachjustieren ohne das gesamte Ersteinrichtungsinterview zu wiederholen. Profil-Update Gewerblicher Rechtsschutz. Prüfraster: Durchsetzungsstrategie… |
| `gewerblicher-rechtsschutz-kaltstart-interview` | Kanzlei oder Unternehmen richtet das gewerbliche-Rechtsschutz-Plugin zum ersten Mal ein und muss Profil und Strategie hinterlegen. Ersteinrichtung Gewerblicher Rechtsschutz. Prüfraster: Kanzleiprofil… |
| `gewerblicher-rechtsschutz-mandat-arbeitsbereich` | Kanzlei mit mehreren Mandanten im gewerblichen Rechtsschutz muss Kontext zwischen Mandaten strikt trennen. Mandatsverwaltung IP-Kanzlei. Prüfraster: Anlegen Auflisten Wechseln Schließen oder Trennen des aktiven Mandats… |
| `ip-klausel-pruefung` | Anwalt prüft Vertrag auf IP-Klauseln (Übertragung Lizenz Inhaberschaft Freistellung) oder Mandant fragt nach Risiken. IP-Klauseln Vertragsrecht. Prüfraster: Übertragung Inhaberschaft Lizenzgewaehrung… |
| `mandat-triage-gewerblicher-rechtsschutz` | Neues Mandat im gewerblichen Rechtsschutz: Anwalt klaert welches Sachgebiet und welche Skills benoetigt werden. Eingangs-Triage IP-Recht. Prüfraster: Mandantenrolle (Schutzrechtsinhaber Verletzer Lizenznehmer)… |
| `markenanmeldung-dpma` | Mandant moechte eine Marke beim DPMA anmelden oder Widerspruch gegen eine eingetragene Marke einlegen. §§ 32 ff. MarkenG Markenanmeldung. Prüfraster: Nizza-Klassifikation Anmeldegebühren absolute Eintragungshindernisse… |
| `markenrecherche` | Unternehmen oder Mandant plant neue Marke oder Produktname und fragt: Bestehen Kollisionsrisiken mit aelteren Marken? Markenrecherche vor Anmeldung. Prüfraster: Identitäts- und Aehnlichkeitsprüfung DPMAregister EUIPO… |
| `open-source-pruefung` | Unternehmen will Software ausliefern oder als Open Source veroffentlichen und fragt nach Lizenz-Compliance. Open-Source-Lizenz-Compliance. Prüfraster: Manifest SBOM Repository Copyleft-Pflichten Lizenzkompatibilitaet… |
| `schutzrechts-portfolio` | Unternehmen oder Kanzlei muss IP-Portfolio verwalten und anstehende Fristen im Blick behalten. Schutzrechtsportfolio-Verwaltung. Prüfraster: Eintragungen Verlaengerungen Jahresgebühren Benutzungsnachweise… |
| `schutzschrift-eilverfuegung` | Mandant hat Abmahnung oder Verletzungsschreiben erhalten und befürchtet einstweilige Verfuegung ohne Anhörung. § 945a ZPO Schutzschrift ZSER. Prüfraster: Hinterlegung zentrales elektronisches Schutzschriftenregister… |
| `streitwert-igr-berechnen` | Anwalt muss Streitwert für IP-Verletzungsklage oder einstweilige Verfuegung im gewerblichen Rechtsschutz festlegen. Streitwertbemessung MarkenG PatG UWG UrhG. Prüfraster: Senatspraxis OLG Hamburg LG Frankfurt LG… |
| `takedown-anweisung` | Rechteinhaber findet urheberrechtsverletzende Inhalte online oder erhielt selbst eine Meldung als Hostprovider. Notice-and-Take-Down §§ 7 ff. TMG/DDG DSA Art. 16. Prüfraster: Meldung an Hostprovider Stoererhaftung DSA… |
| `unterlassungsverlangen` | Schutzrechtsinhaber will Verletzung abmahnen oder hat selbst Abmahnung erhalten. Abmahnung Unterlassung MarkenG PatG UrhG UWG. Prüfraster: Abmahnungsentwurf modifizierte Unterlassungserklärung Streitwert Kostenansatz… |
| `verletzungs-triage` | Mandant sieht IP-Verletzung oder hat Verletzungsschreiben erhalten und fragt: Was ist zu tun? Verletzungs-Triage gewerblicher Rechtsschutz. Prüfraster: Marke § 14 MarkenG Patent § 9 PatG Urheber § 97 UrhG Wettbewerb §… |

## Worum geht es?

Der gewerbliche Rechtsschutz umfasst die Gesamtheit der Schutzrechte für gewerblich verwertbare Immaterialgueter: Marken (MarkenG, EUTMR), Patente (PatG, EPUe), Gebrauchsmuster (GebrMG), Designs (DesignG), Urheberrechte (UrhG), Wettbewerbsrecht (UWG) sowie deren Durchsetzung und Abwehr. Das Plugin unterstuetzt Kanzleien und IP-Abteilungen beim gesamten Mandatsablauf — von der Markenrecherche ueber die Freedom-to-Operate-Analyse und Anmeldung bis hin zu Abmahnung, Schutzschrift und Verletzungsklage.

Dieses Plugin richtet sich an auf IP-Recht spezialisierte Kanzleien und an Unternehmensjuristen, die Schutzrechte anmelden, verwalten und durchsetzen.

## Wann brauchen Sie diese Skill?

- Ein Mandant plant eine neue Marke oder ein neues Produkt und fragt, ob er fremde Schutzrechte verletzt.
- Eine Abmahnung wegen Marken-, Patent-, Urheber- oder UWG-Verletzung ist eingegangen und erfordert sofortige Reaktion.
- Ein Mitarbeiter meldet eine betriebliche Erfindung und es ist zu klaeren, ob das Unternehmen sie in Anspruch nehmen soll.
- Ein Open-Source-Anteil in der Software soll auf Copyleft-Pflichten geprueft werden.
- Das IP-Portfolio muss auf anstehende Fristen (Jahresgebuehren, Benutzungsnachweis, Verlaengerung) ueberprueft werden.

## Fachbegriffe (kurz erklaert)

- **Freedom-to-Operate (FTO)** — Pruefung, ob ein geplantes Produkt oder Verfahren fremde Patentrechte verletzt.
- **Nizza-Klassifikation** — internationales System zur Einteilung von Waren und Dienstleistungen für Markeneintragungen (45 Klassen).
- **Modifizierte Unterlassungserklaerung** — auf den konkreten Verletzungsfall beschraenkte Unterlassungsverpflichtung; vermeidet eine zu weite Verpflichtung.
- **Schutzschrift** — praeventive Gegendarstellung, die im Zentralen Schutzschriftenregister (ZSSR) hinterlegt wird, um bei einer einstweiligen Verfuegung angehoert zu werden (§ 945a ZPO).
- **Copyleft** — Lizenzbedingung (z.B. GPL), die vorschreibt, dass abgeleitete Werke unter denselben Lizenzbedingungen veroeffentlicht werden muessen.
- **ArbnErfG** — Arbeitnehmererfindungsgesetz; regelt Inanspruchnahme, Verguetung und Freistellung betrieblicher Erfindungen.

## Rechtsgrundlagen

- §§ 3 ff. MarkenG — Markenschutz; § 8 MarkenG absolute Eintragungshindernisse
- §§ 9 ff. PatG — Patentschutz und Verletzungshandlungen
- § 14 MarkenG — Verletzung von Markenrechten
- § 97 UrhG — Unterlassung und Schadensersatz bei Urheberrechtsverletzung
- § 97a UrhG — Abmahnung und Kostenobergrenze im privaten Bereich
- §§ 8 ff. UWG — Ansprueche bei unlauterem Wettbewerb
- §§ 6 ff. ArbnErfG — Inanspruchnahme und Freistellung von Arbeitnehmererfindungen
- § 945a ZPO — Schutzschriften und Zentrales Schutzschriftenregister

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Schutzrechtsinhaber, Verletzer, Lizenznehmer oder Dritter?
2. Phase des Mandats bestimmen: Schutzrecht noch nicht vorhanden (Anmeldung/Recherche), bereits vorhanden (Verteidigung/Enforcement) oder Portfolio-Verwaltung?
3. Passenden Skill auswaehlen (siehe Skill-Tour unten).
4. Eilfristen pruefen: Bei einstweiligen Verfuegungen gilt strenge Dringlichkeitsanforderung; Schutzschrift vor Gerichtsbeschluss hinterlegen.
5. Anschluss-Skill bestimmen: Nach Verletzungs-Triage entweder Abmahnung/Unterlassungsverlangen oder Schutzschrift/Verteidigung.

## Skill-Tour (was gibt es hier?)

- `gewerblicher-rechtsschutz-kaltstart-interview` — Ersteinrichtung des Plugins: Kanzleiprofil, Schutzrechtsportfolio und Durchsetzungsstrategie hinterlegen.
- `gewerblicher-rechtsschutz-anpassen` — Kanzleiprofil nachjustieren ohne vollstaendiges Erstinterview zu wiederholen.
- `gewerblicher-rechtsschutz-mandat-arbeitsbereich` — Mandatsverwaltung: aktives Mandat anlegen, wechseln und schliessen.
- `mandat-triage-gewerblicher-rechtsschutz` — Eingangs-Triage: Sachgebiet, Mandantenrolle, Sofort-Fristen und Gerichtsauswahl klaeren.
- `verletzungs-triage` — Erste Einordnung: ignorieren, Abmahnung, einstweilige Verfuegung oder Klage?
- `markenrecherche` — Kollisionsrisiken vor Marken- oder Produktname-Anmeldung im DPMA/EUIPO/WIPO pruefe.
- `markenanmeldung-dpma` — Markenanmeldung beim DPMA oder Widerspruch gegen eingetragene Marken.
- `fto-triage` — Freedom-to-Operate: Recherche auf sperrende Patente vor Produkteinfuehrung.
- `erfindungsmeldung-aufnahme` — Arbeitnehmererfindung aufnehmen und ueber Inanspruchnahme oder Freistellung entscheiden.
- `open-source-pruefung` — Copyleft-Pflichten und Lizenzkompatibilitaet für Softwareprojekte pruefen.
- `ip-klausel-pruefung` — Vertragliche IP-Klauseln (Uebertragung, Lizenz, Freistellung) auf Risiken pruefen.
- `unterlassungsverlangen` — Abmahnungsschreiben oder Optionsmemo bei erhaltener Abmahnung erstellen.
- `abmahnung-urheberrecht` — Urheberrechtliche Abmahnung versenden oder auf erhaltene Abmahnung reagieren.
- `schutzschrift-eilverfuegung` — Praeventive Schutzschrift im ZSSR hinterlegen (§ 945a ZPO).
- `schutzrechts-portfolio` — IP-Portfolio verwalten: Fristen, Jahresgebuehren, Benutzungsnachweise im Ueberblick.
- `streitwert-igr-berechnen` — Streitwert für IP-Verletzungsklage und einstweilige Verfuegung berechnen.
- `takedown-anweisung` — Notice-and-Takedown an Hostprovider nach DDG/DSA oder Gegendarstellung erstellen.

## Worauf besonders achten

- **Dringlichkeit bei einstweiligen Verfuegungen**: Wer zu lange wartet, verliert den Dringlichkeitsgrund; typisch sind zwei bis vier Wochen nach Kenntnis der Verletzung.
- **Modifizierte Unterlassungserklaerung**: Eine zu weit gefasste Unterwerfung verpflichtet den Mandanten ueber den konkreten Fall hinaus; sorgfaeltige Formulierung ist zwingend.
- **Gerichtsstandswahl**: Bei Marken- und UWG-Verletzungen stehen Hamburg, Frankfurt, Muenchen I und Duesseldorf zur Wahl; die Senatspraxis zu Streitwerten und Dringlichkeit unterscheidet sich erheblich.
- **ArbnErfG-Frist**: Der Arbeitgeber hat ab Meldung einer Arbeitnehmererfindung vier Monate Frist, um sie in Anspruch zu nehmen oder freizugeben (§ 6 ArbnErfG); Versaeumnis fuehrt zur freien Erfindung.
- **OSS-Copyleft-Risiken**: Copyleft-Komponenten koennen dazu fuehren, dass proprietaerer Quellcode offengelegt werden muss; Pruefung vor Produktrelease ist essential.

## Typische Fehler

- Passivlegitimation nicht geprueft: Bei Lizenzketten und mehrstufiger Distribution ist zu klaeren, wer eigentlich anspruchspflichtig ist.
- Abmahnung ohne Streitwertangabe verschickt: Fuehrt zu Diskussionen ueber Kostenerstattung und schaecht die Druckwirkung.
- Schutzschrift vergessen: Ohne hinterlegte Schutzschrift ergeht eine einstweilige Verfuegung ohne Anhörung; Rechtsverlust ist praktisch nicht mehr heilbar.
- Vorbenutzungsrecht nach § 12 PatG nicht geprueft: Wer eine Technologie schon vor dem Anmeldetag des Patents benutzt hat, kann eine Freilizenz genessen — dieser Einwand wird oft ueversehen.
- Notice-and-Takedown an falschen Adressaten gerichtet: DSA Art. 16 richtet sich an Hostprovider, nicht an den unmittelbaren Verletzer; Verwechslung verzoegert den Takedown.

## Quellen und Aktualitaet

- Stand: 05/2026
- MarkenG, PatG, UrhG, UWG, DesignG, GebrMG in geltender Fassung
- VO (EU) 2017/1001 (EUTMR) in geltender Fassung
- ArbnErfG in geltender Fassung
- DDG (Digitale-Dienste-Gesetz) und DSA (VO (EU) 2022/2065) in geltender Fassung

---

## Skill: `streitwert-igr-berechnen`

_Anwalt muss Streitwert für IP-Verletzungsklage oder einstweilige Verfuegung im gewerblichen Rechtsschutz festlegen. Streitwertbemessung MarkenG PatG UWG UrhG. Prüfraster: Senatspraxis OLG Hamburg LG Frankfurt LG Muenchen I LG Duesseldorf wirtschaftlicher Wert des Schutzrechts Marktstaerke Eilverf..._

# Streitwert im Gewerblichen Rechtsschutz berechnen

## Arbeitsbereich

Anwalt muss Streitwert für IP-Verletzungsklage oder einstweilige Verfuegung im gewerblichen Rechtsschutz festlegen. Streitwertbemessung MarkenG PatG UWG UrhG. Prüfraster: Senatspraxis OLG Hamburg LG Frankfurt LG Muenchen I LG Duesseldorf wirtschaftlicher Wert des Schutzrechts Marktstaerke Eilverfuegungs-Reduktion Streitgegenstand Streitwertherabsetzung § 51 GKG § 12 UWG. Output: Streitwertbegründung und Kostenberechnung. Abgrenzung zu mandat-triage-gewerblicher-rechtsschutz (Ersteinschaetzung) und verletzungs-triage. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Schutzrecht (Marke Patent Design Geschmacksmuster Urheber Sortenschutz)
- Wirtschaftliche Bedeutung (Umsatz Marktanteil Branchenstellung)
- Verletzungs-Charakter (Umfang Dauer schuldhaft Eile)
- Klage-Anträge (Unterlassung Auskunft Schadensersatz Vernichtung Rückruf)
- Eilverfahren oder Hauptsache
- Sitz der Parteien
- Bisherige Korrespondenz

## Schritt 1 — Wert des Schutzrechts

### Marke § 51 GKG

- **Aufbau-Investitionen** und Marketing-Aufwendungen
- **Marktstellung** der Marke
- **Lizenz-Einkünfte** wenn vorhanden
- **Wettbewerbsschutz** Bedeutung in der Branche
- Typische Spannweite EUR 50000 bis EUR 1000000

### Patent

- **Branchenüblicher Lizenzsatz** mal jährlicher Umsatz mal verbleibende Laufzeit
- **Forschungs- und Entwicklungs-Kosten**
- **Marktbedeutung** in der Branche
- Typisch hoher Wert — sechs- bis siebenstellig

### Design / Gebrauchsmuster

- Geringerer Wert typisch — EUR 25000 bis EUR 500000
- Hängt von Umsatz mit dem geschützten Design ab

### Urheber

- **Wert des Werks** und seines Umsatz-Potenzials
- Bei Filesharing EUR 1000 nach § 97a Abs. 3 UrhG bei Verbrauchern Standard
- Bei gewerblicher Verwendung deutlich höher

### UWG-Unterlassungsklage

- **Wirtschaftliches Interesse** des Verletzten
- Typischer Streitwert EUR 30000 bis EUR 200000 je nach Schwere
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt 2 — Eilverfahren-Reduktion

- Allgemein: **etwa ein Drittel bis Halb** des Hauptsachewerts
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Begründung: vorläufige Sicherung
- Bei Klage in der Hauptsache Streitwert hoch — nach Vergleich auch hoch
- Bei Reduktion Wert der Begründungs-Schritte einkalkulieren

## Schritt 3 — Streitwertherabsetzung § 51 Abs. 5 GKG / § 12 UWG

### Bei UWG-Verfahren § 12 UWG

- Auf Antrag bei wirtschaftlich-existenzbedrohlicher Belastung
- **Streitwertbegünstigung** auf Antrag — Anwalt muss Antrag stellen
- Anwendung bei kleinem / mittelständischem Verletzer

### Bei GRUR § 51 Abs. 5 GKG

- Vergleichbare Norm

## Schritt 4 — Kumulation verschiedener Klage-Anträge

- **Unterlassung** Hauptantrag — höchster Wert
- **Auskunft** typisch 10 Prozent des Unterlassungs-Werts
- **Vernichtung** vergleichbar oder geringer
- **Rückruf** vergleichbar
- **Schadensersatz** konkrete Forderung
- Kumulative Wertfestsetzung bei mehreren Anträgen mit § 39 GKG
- Senatspraxis kann unterschiedlich sein — typisch nicht alle einzelnen Werte addiert

## Schritt 5 — Senatspraxis-Tabelle (typisch)

### LG Hamburg / OLG Hamburg

- Marke: gerne hoher Streitwert bei bekannten Marken EUR 100000+
- UWG: typisch EUR 30000 bis 100000
- Lizenz-Streit: nach Lizenz-Wert

### LG Frankfurt / OLG Frankfurt

- Marke: konservativer als Hamburg
- Wettbewerb: typisch EUR 25000 bis 100000

### LG München I / OLG München

- Patent-Streit häufig EUR 250000 bis Millionen
- Design: konservativ

### LG Düsseldorf / OLG Düsseldorf

- **Patent-Senat-Praxis** zentral
- Patent typisch sechs- bis siebenstellig
- Wettbewerb mittlere Spannweite

## Schritt 6 — Berufungs- und Revisions-Streitwert

- **Berufung** Streitwert des Berufungs-Antrags § 47 GKG
- **Revision** nur bei Streitwert über EUR 20000 zugelassen (§ 26 EGZPO) oder bei rechtlich relevanter Frage
- **Nichtzulassungsbeschwerde** OLG-Streitwert plus EUR 20000

## Schritt 7 — Sicherheitsleistung

### § 709 ZPO (Hauptsache)

- Vollstreckung gegen Sicherheitsleistung
- Höhe typisch 110 oder 120 Prozent des Vollstreckungs-Volumens

### § 940 ZPO (Einstweilige Verfügung)

- Sicherheitsleistung zur Schadensabsicherung
- Höhe ermessen — meist Bruchteil des Hauptsache-Volumens

## Schritt 8 — Strategische Aspekte

| Konstellation | Strategie |
|---|---|
| Verletzer klein — Streitwert begünstigt | § 12 UWG Antrag stellen |
| Hauptsache nach EV | Wertabgleich — keine Bevorzugung wegen frühere EV |
| Mehrere Verletzungs-Akte | Einheitlicher Streitwert oder einzeln? |
| Streit über Anwaltskosten | Streitwert beeinflusst Gebühren |
| EuGVVO Vollstreckung im Ausland | Streitwert im Heimatstaat klar machen |

## Schritt 9 — Praktische Schritte

1. Schutzrecht-Wert kalkulieren (Lizenz-Analogie Marketing-Aufwand Marktstellung)
2. Verletzungs-Umfang dokumentieren
3. Verfahrensart wählen Eile vs. Hauptsache
4. Senat-Wahl bei Konkurrenzzuständigkeit (Gerichtsstands-Auswahl strategisch)
5. § 12 UWG Antrag prüfen wenn Verletzer-Existenz gefährdet

## Ausgabe

- `streitwert-bewertung.md` mit Berechnungsschritten
- Tabelle für die einzelnen Anträge
- Begründung gegenüber Gericht für gewählten Streitwert
- Vergleichs-Werte aus aktuellen Senatsentscheidungen
- Bei § 12 UWG-Antrag: Begründung mit Bilanzen Umsatz

## Quellen

- GKG §§ 39 47 48 51
- UWG § 12
- ZPO §§ 709 940
- EGZPO § 26
- BGH I. Zivilsenat (GRUR-Sachen)
- GRUR / GRUR-RR Senatsentscheidungen
- Hefermehl/Köhler/Bornkamm UWG
- Köhler/Feddersen UWG
- Ingerl/Rohnke MarkenG
- Benkard PatG

## Triage-Fragen bei Streitwert-Berechnung

Bevor der Streitwert festgesetzt wird, klaere:
1. Handelt es sich um ein UWG-Verfahren (§ 12 II UWG — Antragsgebundenheit), Markenrecht oder Patentrecht?
2. Wird einstweiliger Rechtsschutz (Gegenstandswert = 50-100 % des Hauptsachewerts) oder Hauptsacheklage beantragt?
3. Welchen wirtschaftlichen Wert hat das Unterlassungsbegehren — Umsatz des Verletzers, Bedeutung der Marke/des Patents?
4. Gibt es Vergleichswerte aus OLG-Beschluessen für aehnliche Faelle (GRUR-RR, WRP)?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Audit-Hinweis (27.05.2026)

Im Halluzinations-Audit 2026-05-27 wurden in diesem Skill folgende
Aktenzeichen geprueft und korrigiert:
- BGH I ZR 20/07 (NOT_FOUND: Aktenzeichen nicht in dejure nachweisbar): ersetzt durch verifizierte Entscheidung BGH X ZR 171/12 vom 13.11.2013 (Einkaufskuehltasche), GRUR 2014, 206 (Quelle: dejure.org/2013,31771)

---

## Skill: `takedown-anweisung-unterlassungsverlangen`

_Rechteinhaber findet urheberrechtsverletzende Inhalte online oder erhielt selbst eine Meldung als Hostprovider. Notice-and-Take-Down §§ 7 ff. TMG/DDG DSA Art. 16. Prüfraster: Meldung an Hostprovider Stoererhaftung DSA Meldeformular Gegendarstellung. Output: Meldungs-Entwurf oder Gegendarstellungs..._

# Notice-and-Take-Down / Meldeverfahren

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

Befehlsargument:
- `--senden` + Kontext oder Pfad zur Meldungsunterlage
- `--reagieren` + Pfad zur oder eingefügte eingegangene Meldung
- `--gegenvorstellung` + Kontext
- (kein Argument) → fragen: "Sollen wir eine Meldung senden, auf eine eingegangene reagieren oder eine Gegenvorstellung formulieren?"

## Rechtlicher Rahmen

### Kernvorschriften

**Haftung des Hostproviders / Vermittlerdienstleister:**
- **§ 7 Abs. 1 DDG / § 7 Abs. 1 TMG (§ 10 TMG a.F.)** — Kein Hostprovider ist verpflichtet, gespeicherte Inhalte zu überwachen; erst nach Kenntnis von konkreter Rechtsverletzung entsteht Handlungspflicht (Reaktionspflicht nach BGH-Rspr.)
- **§ 10 DDG / § 10 TMG** — Haftungsprivileg für Hostprovider: Haftung erst bei Kenntnis und Nichtentfernen nach Hinweis (Notice-and-Take-Down-Mechanismus)
- **Art. 16 DSA (Digital Services Act, EU 2022/2065)** — Meldeverfahren für Plattformen mit mehr als 45 Mio. monatlichen Nutzern in der EU; einheitliches Meldeformular-Format; Reaktionspflicht; Beschwerdemechanismus
- **Art. 17 DSA** — Begründungspflicht der Plattform bei Inhaltsmoderation; Gegenvorstellungsrecht
- **§ 97 UrhG** — Unterlassungs- und Schadensersatzanspruch bei Urheberrechtsverletzung; Grundlage für Abmahnung

**Störerhaftung:**
- Störerhaftung: Wer willentlich und adäquat kausal zur Rechtsverletzung eines Dritten beiträgt, haftet als Störer auf Unterlassung (nicht Schadensersatz). Prüfungspflichten müssen zumutbar sein.
- **§ 8 DDG** — Durchleitungsdienstleister: kein Haftungsprivileg-Verlust bei bloßer Durchleitung; keine Überwachungspflicht

**NetzDG / weitere:**
- **§§ 1–3 NetzDG** — Plattformpflichten bei Hassrede und sonstigen strafbaren Inhalten; spezialgesetzliche Entfernungspflicht unabhängig vom allgemeinen Notice-and-Take-Down

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Kommentare

- Köhler, in: Köhler/Bornkamm/Feddersen, UWG, 43. Aufl. 2025, § 8 Rn. 2.1 (Unterlassungsanspruch; Störerhaftung)
- Leistner/Ohst, in: Schricker/Löwenheim, UrhG, 6. Aufl. 2020, § 97 Rn. 1 (Unterlassung und Schadensersatz)
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ablauf

### Modus `--senden`: Meldung an Hostprovider / Plattform

#### Schritt 1: Geschütztes Werk identifizieren

> Um eine Meldung zu formulieren, werden folgende Angaben benötigt:
>
> - **Bezeichnung / Beschreibung des Werkes** — was ist es (Software, Bild, Text, Video, Audio)?
> - **Rechtsinhaber** — wem gehören die Rechte? Eigentümer, ausschließlicher Nutzungsrechtinhaber, oder Auftraggeber nach § 69b UrhG (Arbeitnehmer-Softwarewerk)?
> - **Nachweis der Rechtsinhaberschaft** — Urheberschaft, Lizenz, Auftrag
> - **Frühere Lizenzen** — wurde die beanstandete Nutzung jemals gestattet (Vertrag, Creative-Commons-Lizenz, stillschweigende Erlaubnis)?

Rechtsinhaberschaft und Verfügungsberechtigung sind die ersten Punkte, die ein Hostprovider und ein Gericht prüfen.

#### Schritt 2: Verletzungsmaterial und Fundort identifizieren

> - **Plattform / Diensteanbieter** — YouTube, Instagram, GitHub, Amazon, ein Webhoster etc.
> - **URL(s)** — konkrete, direkte Links zum beanstandeten Inhalt
> - **Beschreibung** — was ist die Verletzung (identische Kopie, wesentlich ähnlich, abgeleitetes Werk ohne Lizenz)?
> - **Beweissicherung** — Screenshot mit sichtbarer URL und Zeitstempel; ggf. Web-Archivierung (archive.org)

§ 97 UrhG und das Notice-and-Take-Down-System verlangen hinreichend genaue Bezeichnung, damit der Diensteanbieter den Inhalt auffinden und beurteilen kann.

#### Schritt 3: Zulässigkeitsprüfung (Freie Nutzung, Schranken)

Vor der Meldung sind Urheberrechtsschranken zu prüfen. Eine Meldung auf schrankengemäße Nutzungen schädigt den Diensteanbieter und kann Schadensersatzansprüche (§ 826 BGB, § 97a Abs. 4 UrhG analog) auslösen.

Prüfen nach §§ 44a ff. UrhG:

- **§ 51 UrhG — Zitat:** Kritik, Rezension, wissenschaftliche Auseinandersetzung — legitim, wenn Zitatzweck erkennbar und Umfang verhältnismäßig
- **§ 49 UrhG — Presseprivileg:** Übernahme von Tagesaktualitäten; eng begrenzt
- **§ 44a UrhG — Vorübergehende Vervielfältigungen:** Technisch-funktionale Zwischenspeicherung
- **§ 60a ff. UrhG — Bildung und Wissenschaft:** Unterricht, Wissenschaft, öffentliche Einrichtungen; begrenzt
- **§ 24 UrhG — Freie Benutzung (aufgehoben):** Seit 7.6.2021 durch Unionsrecht ersetzt; Parodie, Karikatur, Pastiche jetzt über § 51a UrhG

Wenn Schrankennutzung **wahrscheinlich oder zweifelhaft**: Entwurf stoppen, an Rechtsanwalt verweisen. Eine Meldung auf geschützte Meinungsäußerungen ist das genaue Szenario, das zu einer Gegenreaktion berechtigt.

#### Schritt 4: Guter Glaube und Vertretungsberechtigung

- Ist der Nutzer der Rechtsinhaber oder von ihm bevollmächtigt?
- Wurde die Nutzung direkt geprüft (nicht nur aus zweiter Hand)?
- Wurden bestehende Lizenzen und Gestattungen überprüft?

Wenn ja auf alle Punkte: Guter Glaube ist begründbar.

#### Schritt 5: Meldung formulieren

Erforderliche Elemente (nach BGH-Rspr. und DSA Art. 16):

1. **Identifikation der Rechtsinhaberin** — Name, Adresse, E-Mail; Bevollmächtigter falls zutreffend
2. **Bezeichnung des geschützten Werkes** — Titel, Typ, ggf. Registrierungsnummer (Urheberrecht entsteht formfrei nach § 7 UrhG; Registrierung ist kein Anspruchsvoraussetzung)
3. **Genaue Fundort-URL(s)** des beanstandeten Inhalts
4. **Beschreibung der Verletzung** — worin konkret die Verletzung besteht
5. **Erklärung guten Glaubens** — keine Berechtigung der Nutzung durch Inhaber, seinen Bevollmächtigten oder das Gesetz
6. **Genauigkeitserklärung** — Angaben sind nach bestem Wissen zutreffend
7. **Bitte um Entfernung**

DSA Art. 16 Plattformen: Meldung über das behördlich bereitgestellte Formular oder den plattformeigenen Meldepfad einreichen. Plattform ist zur Bestätigung und Begründung verpflichtet (Art. 17 DSA).

#### Schritt 6: Warnhinweis vor Versand

```
┌─────────────────────────────────────────────────────────────┐
│ VOR DEM VERSAND DIESER MELDUNG │
├─────────────────────────────────────────────────────────────┤
│ │
│ Eine Notice-and-Take-Down-Meldung hat unmittelbare │
│ rechtliche Wirkung. Unberechtigt eingereichte Meldungen │
│ können Schadensersatzansprüche des Diensteanbieters │
│ oder des betroffenen Nutzers auslösen (§§ 823, 826 BGB; │
│ Art. 17 Abs. 8 DSA für Missbrauch des Meldeverfahrens). │
│ │
│ Vor dem Versand bestätigen: │
│ │
│ 1. Sie sind Rechtsinhaber oder bevollmächtigt. │
│ 2. Die beanstandete Nutzung ist nicht gestattet — │
│ Lizenzen, Schranken und Gestattungen wurden │
│ geprüft. │
│ 3. Schranken (§§ 44a ff. UrhG, insb. Zitat § 51, │
│ Parodie § 51a) sind nicht einschlägig. │
│ 4. Die versendende Person hat Genehmigung gemäß │
│ Mandatsprofil. │
│ │
│ Genehmigung gemäß Mandatsprofil: [Genehmigende Person] │
│ │
└─────────────────────────────────────────────────────────────┘
```

### Modus `--reagieren`: Eingegangene Meldung triagieren

Der eigene Inhalt wurde von einer Plattform entfernt oder ein Diensteanbieter hat eine Meldung übermittelt.

#### Schritt 1: Meldung lesen

Extrahieren:

- **Absender** — Entität, Unterzeichner, ggf. anwaltliche Vertretung
- **Diensteanbieter** — welche Plattform hat informiert?
- **Beanstandetes Werk** — was behauptet der Absender als sein Recht?
- **Unser Inhalt** — welche URL(s) / welcher Inhalt wurde beanstandet?
- **Datum** der Meldung und ggf. Entfernung
- **Formelle Vollständigkeit** — enthält die Meldung alle erforderlichen Elemente? (Fehler erhöhen die Möglichkeit einer Gegenvorstellung)

#### Schritt 2: Bewertung

- **Liegt eine Lizenz vor?** Vertraglich, stillschweigend, Creative Commons, vorherige Einigung
- **Greift eine Schranke?** Zitat (§ 51 UrhG), Parodie/Pastiche (§ 51a UrhG), Bildung (§ 60a ff. UrhG)
- **Hat die Meldung formelle Mängel?** Fehlende Elemente, fehlende Genehmigungserklärung, unklare Rechtsinhaberschaft? Mangelhafte Meldungen sind keine ordnungsgemäßen Meldungen; die Plattform darf trotzdem handeln — aber das Durchsetzungsrisiko des Absenders steigt.
- **Hat die Plattform ordnungsgemäß reagiert?** Wurde uns nach Art. 17 DSA eine Begründung übermittelt?
- **Absender-Glaubwürdigkeit:** Wiederholte Meldungen auf vergleichbare Inhalte? Erkennbares Muster von Overblocking?

#### Schritt 3: Vier Optionen präsentieren

**A — Entfernung akzeptieren**
- Wenn: Meldung berechtigt oder Aufwand des Widerspruchs unverhältnismäßig
- Abwägung: Inhalt bleibt offline; SEO-Effekt; Sperren-Konto-Risiko bei Plattformen mit Wiederholungssystem
- Nächster Schritt: Vorgang dokumentieren; keine Gegenvorstellungs-Frist versäumen

**B — Gegenvorstellung einlegen**
- Wenn: guter Glaube, dass Inhalt rechtmäßig war — Lizenz, Schranke, fehlendes Eigentumsrecht des Absenders
- Abwägung: Inhalt bleibt gesperrt bis Plattform entscheidet; bei DSA: Beschwerdemechanismus (Art. 20) und außergerichtliche Beilegung (Art. 21) verfügbar; Eskalationsrisiko
- Nächster Schritt: `/gewerblicher-rechtsschutz:takedown-anweisung --gegenvorstellung`

**C — Absender direkt kontaktieren**
- Wenn: Spielraum für einvernehmliche Lösung (Lizenzierung, Namensnennung, Teilentfernung)
- Abwägung: Inhalt bleibt gesperrt während der Gespräche; Vertraulichkeit von Verhandlungen beachten (§ 278 ZPO-Analogie)
- Nächster Schritt: Anschreiben an Absender; Gegenvorstellung bis Einigung zurückstellen

**D — Ignorieren / auf anderem Weg verfolgen**
- Wenn: Schaden gering, kein Interesse an Gerichtsstand-Einräumung, Absender separat adressieren
- Abwägung: Inhalt bleibt gesperrt; § 97 UrhG kann ggf. beim Absender selbst geltend gemacht werden bei unberechtigter Meldung

Empfehlung mit zwei Sätzen Begründung.

#### Schritt 4: Triagierungsvermerk schreiben

```markdown
[ARBEITSERGEBNIS-KOPFZEILE]

### Eingegangene Meldung — Triagierung

**Kurzzeichen:** [kurzzeichen]
**Eingegangen:** [JJJJ-MM-TT]
**Plattform:** [Name]

## Die Meldung

**Absender:** [Entität, Unterzeichner, Anwaltsbüro falls vorhanden]
**Beanstandetes Werk:** [Titel, Beschreibung]
**Unser Inhalt:** [URLs / Identifikatoren]
**Datum der Entfernung:** [JJJJ-MM-TT]
**Formelle Vollständigkeit der Meldung:** [ja / nein — fehlende Elemente auflisten]

## Bewertung

**Lizenz / Genehmigungscheck:** [Ergebnis]
**Schrankenprüfung (§§ 51, 51a, 60a ff. UrhG):** [Ergebnis — jede Schranke + Schluss; `[SME VERIFIZIEREN]`]
**Formelle Mängel der Meldung:** [Liste oder keine]
**DSA-Begründung durch Plattform:** [erhalten / nicht erhalten]
**Absender-Glaubwürdigkeit:** [Einschätzung]

## Optionen

### A. Entfernung akzeptieren
### B. Gegenvorstellung
### C. Absender kontaktieren
### D. Ignorieren

**Empfehlung:** [A/B/C/D] — [zwei Sätze] — `[SME VERIFIZIEREN: Anwalt bestätigt vor Ausführung]`

## Fristen

- **Beschwerdefrist DSA Art. 20:** 6 Monate nach Entscheidung der Plattform
- **Außergerichtliche Beilegung DSA Art. 21:** Verfügbar bei nicht-gütlicher Einigung
- **Vertragliche Fristen mit Plattform:** [prüfen]

## Sofortmaßnahmen

- [ ] Beweissicherung des beanstandeten Inhalts durchgeführt — [ja/nein]
- [ ] Geschäftliche Auswirkung bewertet — [ja/nein]
- [ ] Mandat im Verlaufsprotokoll erfasst — [ja/nein/TBD]
- [ ] Rechtsanwalt beauftragt — [wer]
```

### Modus `--gegenvorstellung`: Gegenvorstellung an Plattform

#### Schritt 1: Voraussetzungen prüfen

- Inhalt wurde aufgrund einer Meldung (nicht aufgrund von AGB-Verstoß) entfernt
- Es besteht guter Glaube, dass die Entfernung unberechtigt war (Lizenz, Schranke, fehlende Rechtsinhaberschaft des Absenders)
- Entscheidung wurde bewusst getroffen — nicht reaktiv

#### Schritt 2: Gegenvorstellung formulieren

Erforderliche Elemente:

1. **Identifikation des betroffenen Inhalts** — URL des entfernten Inhalts
2. **Erklärung des guten Glaubens** — Inhalt war rechtmäßig, weil: [Lizenz / Schranke / fehlendes Recht des Absenders]
3. **Begründung** — konkrete Darlegung
4. **Antrag auf Wiederherstellung**
5. **Kontaktdaten**

Bei DSA-Plattformen: Beschwerdemechanismus nach Art. 20 DSA nutzen; ggf. außergerichtliche Streitbeilegung nach Art. 21 DSA.

#### Schritt 3: Warnhinweis vor Versand

```
┌─────────────────────────────────────────────────────────────┐
│ VOR DEM VERSAND DIESER GEGENVORSTELLUNG │
├─────────────────────────────────────────────────────────────┤
│ │
│ Eine Gegenvorstellung bestreitet die Berechtigung │
│ der ursprünglichen Meldung und kann den Absender zu │
│ rechtlichen Schritten veranlassen. │
│ │
│ • Bei Eskalation durch den Absender: Klage auf │
│ Unterlassung oder Schadensersatz nach § 97 UrhG │
│ möglich. │
│ │
│ • DSA Art. 20: Beschwerde bei Plattform möglich. │
│ Art. 21: Außergerichtliche Streitbeilegung verfügbar. │
│ │
│ Vor dem Versand bestätigen: │
│ 1. Guter Glaube besteht — Lizenz, Schranke oder │
│ fehlendes Recht des Absenders ist konkret │
│ benennbar. │
│ 2. Anwalt hat diese Gegenvorstellung vor dem │
│ Versand geprüft. │
│ 3. Genehmigung gemäß Mandatsprofil liegt vor. │
│ │
│ Genehmigung gemäß Mandatsprofil: [Genehmigende Person] │
│ │
└─────────────────────────────────────────────────────────────┘
```

## Beispiel

**Eingabe:** `/gewerblicher-rechtsschutz:takedown-anweisung --senden` — Fotograf meldet unerlaubte Nutzung seines Fotos auf einer Nachrichtenwebsite.

**Auszug Meldungsentwurf:**

> An: [Name Diensteanbieter / Hostprovider]
> Betreff: Meldung einer Urheberrechtsverletzung nach § 7 Abs. 2 DDG
>
> Sehr geehrte Damen und Herren,
>
> ich bin Rechtsinhaber / bevollmächtigte Vertreterin für folgendes urheberrechtlich geschütztes Werk:
> Fotografie "[Bildtitel]", aufgenommen am [Datum], Urheber [Name] (§ 7 UrhG).
>
> Dieses Werk wird auf Ihrer Plattform ohne Genehmigung genutzt unter:
> [URL]
>
> Die Nutzung ist weder durch mich noch durch Dritte gestattet. Schranken nach §§ 44a ff. UrhG greifen nach Prüfung nicht ein. Ich bitte um unverzügliche Entfernung des genannten Inhalts.
>
> Ich erkläre nach bestem Wissen und Gewissen, dass die vorstehenden Angaben zutreffend sind und ich berechtigt bin, im Namen des Rechtsinhabers zu handeln.
>
> [Kontaktdaten / Unterschrift]

## Risiken und typische Fehler

- **Schrankenprüfung versäumen:** Meldungen auf zitiergeschützte Kritik, Parodien oder Unterrichtsmaterial sind unzulässig und können Gegenansprüche auslösen.
- **Unklare Rechtsinhaberschaft:** Meldung ohne Nachweis der Berechtigung scheitert beim Hostprovider und erzeugt Haftungsrisiken.
- **DSA-Pflichten übersehen:** Große Plattformen (Very Large Online Platforms nach Art. 33 DSA) sind zu förmlichen Reaktionen und Begründungen verpflichtet; diese Pflichten können eingefordert werden.
- **Gegenvorstellung ohne Anwaltsrat:** Die Gegenvorstellung bestreitet die Meldung; eine unbegründete Gegenvorstellung kann zur eigenen Unterlassungsklage führen.
- **NetzDG-Spezialregeln vergessen:** Bei Hassrede und strafbaren Inhalten gelten §§ 1–3 NetzDG mit eigenem Melde- und Entfernungsregime.

## Quellenpflicht

Alle Aussagen zu Haftung, Schranken und Verfahren müssen belegbar sein:

- **Gesetze:** §§ 7, 10 DDG (entspr. TMG); §§ 51, 51a, 97 UrhG; Art. 16, 17, 20, 21 DSA; §§ 1–3 NetzDG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Kommentar:** Spindler/Schuster eMedienR oder Köhler/Bornkamm/Feddersen UWG mit § und Randnummer
- Modellannahmen als `[Modellwissen — verifizieren]` kennzeichnen.

## Triage-Fragen vor Takedown

Bevor der Takedown ausgeloest wird, klaere:
1. Liegt eine klare Rechtsverletzung vor oder handelt es sich um Kritik/Parodie/Satire (urheberrechtliche Schranke)?
2. Ist der Rechteinhaber klar identifiziert und ist der Einreicher zur Meldung berechtigt?
3. Ist die Plattform eine Very Large Online Platform (VLOP) nach DSA Art. 33 (Pflicht zu foermlicehem Notice-and-Action-Verfahren)?
4. Wurde das NetzDG geprueft (§§ 1-3 NetzDG) für strafbare Inhalte mit eigenen Loeschfristen?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> **DSA (EU) 2022/2065, Art. 16/17 (Digital Services Act):** Hosting-Dienstleister muessen wirksame und zugaengliche Melde- und Abhilfemechanismen einrichten; bei VLOP gelten verstaerkte Transparenz- und Reaktionspflichten; Verstoss kann zu Bussgeldern bis 6 % des globalen Jahresumsatzes fuehren.

<!-- AUDIT 27.05.2026: Bundle 032 Halluzinations-Reparatur
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
-->

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

