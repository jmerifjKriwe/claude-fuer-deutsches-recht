# Megaprompt: preussisches-allgemeines-landrecht-pralr

> *Achtung: Dies ist ein experimentelles Mega-Prompt-Markdown, das einen kompletten Klotzkette-Plugin in eine einzige Datei zusammenfuehrt. Keine Haftung, keine Gewaehr. Nur zum Ausprobieren der Skills auch ohne Claude Code; keine Rechtsberatung. Vor Verwendung im Mandat anwaltlich pruefen.*
>
> *Caution: This is an experimental Mega-Prompt Markdown that consolidates a full Klotzkette plugin into a single file. No warranty, no liability. For exploration with chat tools that do not run Claude Code only; not legal advice.*

**Verwendung:** Diesen gesamten Text in einen Chat ohne Claude-Code-Integration einfuegen (oder als Datei hochladen). Der Chat-Agent erhaelt damit die gebuendelten Skills dieses Plugins als Kontext. Eine Replikation des vollen Plugin-Verhaltens ist nicht garantiert — der Megaprompt ist eine Best-Effort-Kompression.


## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 199 Skills des Plugins `preussisches-allgemeines-landrecht-pralr`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — PrALR: Kaltstart, Quellenlage, Textzeugenvergleich, Fachmodul-Routing und erste verwertbare rechtsgeschichtliche Ausgabe…
2. **aufopferung-fortwirkung-bgb-und-polizei** — Aufopferungsanspruch — Fortwirkung im BGB und im modernen Polizei- und Ordnungsrecht. Skill behandelt die heute lebende …
3. **aufopferung-historische-faelle** — Aufopferungsanspruch Einleitung §§ 74-75 ALR — historische Faelle Pockenimpfungsschaeden und Sonderopfer-Lehre. Skill be…
4. **aufopferung-historische-faelle-pockenimpfung** — Aufopferungsanspruch Einleitung §§ 74-75 ALR — historische Faelle Pockenimpfungsschaeden und Sonderopfer-Lehre. Skill be…
5. **bereicherungsrecht-im-alr-condictiones** — Ungerechtfertigte Bereicherung im ALR. Skill behandelt die roemische condictiones-Systematik im ALR die condictio indebi…
6. **sklavenrecht-alr-ii-5-196-197** — Sklavenrecht im ALR — die beruehmten Bestimmungen ALR II 5 §§ 196 ff. zur Nichtanerkennung der Sklaverei in Preussen. Sk…
7. **sklavenrecht-rechtsvergleich** — Rechtsvergleich Sklavenrecht — Preussen ALR vs. England Somerset 1772 vs. Frankreich Code Noir 1685/1716. Skill arbeitet…
8. **sklavenrecht-rechtsvergleich-somerset-code-noir** — Rechtsvergleich Sklavenrecht — Preussen ALR vs. England Somerset 1772 vs. Frankreich Code Noir 1685/1716. Skill arbeitet…
9. **strafprozess-willensmaengel** — Strafprozess im ALR — Inquisitionsverfahren. Skill behandelt das Inquisitionsprinzip die Folter-Aufhebung Friedrichs II.…
10. **zwitterrecht-alr-ii-1-19-bis-22** — Zwitterrecht nach ALR — das beruehmte preussische Sonderrecht der Wahlmoeglichkeit. ALR II 1 §§ 19 bis 22 regelte das Ge…
11. **zinsobergrenze-und-wuchertatbestand** — Zinsobergrenze und Wuchertatbestand im ALR. Skill behandelt die historische Zinsobergrenze (centesima usura 12 Prozent o…
12. **sklaverei-aufhebung-edikte-1807** — Aufhebung der Sklaverei und der Erbuntertaenigkeit in Preussen — vom ALR ueber das Oktoberedikt 1807 bis zum Gesetz 1857…
13. **sklaverei-aufhebung-und-edikte-1807-1857** — Aufhebung der Sklaverei und der Erbuntertaenigkeit in Preussen — vom ALR ueber das Oktoberedikt 1807 bis zum Gesetz 1857…
14. **strafprozess-und-inquisition** — Strafprozess im ALR — Inquisitionsverfahren. Skill behandelt das Inquisitionsprinzip die Folter-Aufhebung Friedrichs II.…
15. **zinsobergrenze-wuchertatbestand** — Zinsobergrenze und Wuchertatbestand im ALR. Skill behandelt die historische Zinsobergrenze (centesima usura 12 Prozent o…

---

## Skill: `kaltstart-triage`

_PrALR: Kaltstart, Quellenlage, Textzeugenvergleich, Fachmodul-Routing und erste verwertbare rechtsgeschichtliche Ausgabe._

# PrALR - Allgemeiner Einstieg

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Preussisches Allgemeines Landrecht Pralr** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

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

## Startfragen

1. Welche Quelle liegt vor: Scan, OCR, PDF, Transkription, Sekundärtext, Urteil oder Aktenvermerk?
2. Welches Jahr, welcher Band, welcher Teil, welcher Titel und welcher Paragraph sind sicher?
3. Geht es um historische Erklärung, heutige Fortwirkung, Dogmengeschichte, Unterricht oder Schriftsatzargument?
4. Welcher Ort und welches Jahr sind für den Sachverhalt maßgeblich?
5. Brauchen wir einen Live-Check, weil heutiges Recht, Landesrecht oder Rechtsprechung betroffen ist?

## Prüfroutine

1. **Textzeuge sichern:** Ausgabe, Druck, Band, Seite/Scan, OCR-Fassung und Fundstelle erfassen.
2. **Systemstelle finden:** Einleitung, Teil, Titel, Paragraph und Nachbarvorschriften bestimmen.
3. **Geltung trennen:** historisch geltendes Recht, subsidiäre Anwendung, lokale Abweichung und heutige Fortwirkung unterscheiden.
4. **Begriffe entschlüsseln:** alte Orthographie, ständische Begriffe und heutige Übersetzung offenlegen.
5. **Anachronismus prüfen:** moderne Kategorien nur als Vergleich verwenden, nicht in den Normtext hineinlesen.
6. **Output bauen:** Quellenmatrix, Kurzvermerk, Gutachtenbaustein, Unterrichtsfolie oder Schriftsatzpassage erstellen.

---

## Skill: `aufopferung-fortwirkung-bgb-und-polizei`

_Aufopferungsanspruch — Fortwirkung im BGB und im modernen Polizei- und Ordnungsrecht. Skill behandelt die heute lebende ungeschriebene Anspruchsgrundlage die spezialgesetzlichen Sondervorschriften (POG IfSG OEG StVG) und die Subsidiaritaet. Liefert Pruefraster im Preußisches Allgemeines Landrecht..._

# Pralr Aufopferung Fortwirkung Bgb Und Polizei

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: historisch — Verjährung nach ALR-Vorschriften (z. B. 30-jährige actio); heutige Anwendung über Art. 184 ff. EGBGB und § 195 BGB.
- Tragende Normen verifizieren: ALR Einleitung §§ 1-100, Erster Teil (Personen-/Sachenrecht), Zweiter Teil (Personenstand, Familie, Erbrecht), Allgemeine Gerichtsordnung; abgelöst durch BGB (1900), aber dogmenhistorisch fortwirkend — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Rechtshistoriker, Lehrstühle, Restitutionsverfahren mit Altrecht-Bezug, Boden- und Erbschaftsstreite mit historischer Wurzel.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Rechtsvergleichende Stellungnahme, ALR-Auszug aus historischer Edition, dogmatische Untersuchung, Restitutionsgutachten, Erbschaftsgutachten — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Heute lebender Aufopferungsanspruch

- Ungeschriebenes Rechtsinstitut auf der Grundlage Einl. §§ 74-75 ALR.
- BGH staendige Rspr. seit BGHZ 9 Seite 83.

## Spezialgesetze (vorrangig)

- POG / PolG der Länder — Polizeischadensentschaedigung.
- **SGB XIV (Soziales Entschaedigungsrecht)** — in Kraft seit 01.01.2024. Bündelt das frühere BVG (Bundesversorgungsgesetz), das OEG (Opferentschädigungsgesetz) und die Impfschadensversorgung aus IfSG §§ 60 ff. zu einem einheitlichen sozialen Entschaedigungsrecht. Für Altfaelle / Uebergangsregelungen weiter BVG/OEG/IfSG live verifizieren.
- StVG §§ 7 ff. — Halterhaftung.

## Subsidiaritaet

- Aufopferungsanspruch tritt zurueck, wenn Spezialgesetz greift.
- Aufopferung dient als "Auffangtatbestand" für rechtmäßige Eingriffe ohne Spezialgesetz.

## Typische heutige Faelle

- Verletzung eines Unbeteiligten beim polizeilichen Einsatz (Schussschaden Polizeischaden).
- Vermoegensentzug durch hoheitliche Massnahme.
- Frueh-Impfungsfaelle vor sozialer Entschaedigung — heute SGB XIV.

## Abgrenzung Art. 14 III GG

- Eigentumsentziehung -> Enteignung mit Art. 14 III GG.
- Sonstige Eingriffe -> Aufopferung.

## Abgrenzung Art. 34 GG

- Rechtswidriges Verhalten -> Amtshaftung.
- Rechtmäßiges Verhalten -> Aufopferung.

## Pruefraster

1. Hoheitlicher Eingriff?
2. Rechtmaessig oder rechtswidrig?
3. Spezialgesetz greift?
4. Aufopferung subsidiaer?
5. Sonderopfer-Schwelle?

---

## Skill: `aufopferung-historische-faelle`

_Aufopferungsanspruch Einleitung §§ 74-75 ALR — historische Faelle Pockenimpfungsschaeden und Sonderopfer-Lehre. Skill behandelt die Pockenimpfungspflicht des 19. Jahrhunderts (Reichsimpfgesetz 1874) und die rechtshistorische Linie zur heutigen Impfschadensversorgung nach IfSG. Liefert Quellenmatrix._

# Pralr Aufopferung Historische Faelle Pockenimpfung

## Historischer Hintergrund

- Pockenimpfpflicht ab Mitte 19. Jh. in einzelnen Staaten Preussens.
- Reichsimpfgesetz 08.04.1874 fuehrte Pflichtimpfung gegen Pocken reichsweit ein.
- Bei Impfschaeden Ansprueche der Geschaedigten auf Aufopferungsentschaedigung.

## Aufopferungsanspruch

- Anker: Einl. §§ 74-75 ALR.
- "Sonderopfer" — der Buerger erbringt eine Sonderlast für die Allgemeinheit (Schutz gegen Seuchen).
- Entschaedigung verlangt rechtshistorisch zuerst die rechtliche Anerkennung des Eingriffs.

## Frueheste Klagen

- Preussische Gerichte erkannten erste Aufopferungsansprueche im Zusammenhang mit der Impfung.
- Erlass des Preussischen Innenministers (Daten und Inhalte vor Zitat verifizieren).

## Fortwirkung im 20. Jahrhundert

- BGHZ 9 Seite 83 — Aufopferungsanspruch im Polizeischadensfall.
- Reichsversorgungsgesetz und spaetere Reform.
- Heute IfSG §§ 60 ff. für Impfschaeden.

## Pruefraster

1. Hoheitliche Massnahme im Allgemeininteresse?
2. Sonderbelastung des Einzelnen?
3. Spezialgesetz greift (IfSG, POG)?
4. Allgemeiner Aufopferungsanspruch subsidiaer?
5. Quellenstellen Einl. §§ 74-75 ALR; BGHZ 9.

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

---

## Skill: `aufopferung-historische-faelle-pockenimpfung`

_Aufopferungsanspruch Einleitung §§ 74-75 ALR — historische Faelle Pockenimpfungsschaeden und Sonderopfer-Lehre. Skill behandelt die Pockenimpfungspflicht des 19. Jahrhunderts (Reichsimpfgesetz 1874) und die rechtshistorische Linie zur heutigen Impfschadensversorgung nach IfSG. Liefert Quellenmatr..._

# Pralr Aufopferung Historische Faelle Pockenimpfung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: historisch — Verjährung nach ALR-Vorschriften (z. B. 30-jährige actio); heutige Anwendung über Art. 184 ff. EGBGB und § 195 BGB.
- Tragende Normen verifizieren: ALR Einleitung §§ 1-100, Erster Teil (Personen-/Sachenrecht), Zweiter Teil (Personenstand, Familie, Erbrecht), Allgemeine Gerichtsordnung; abgelöst durch BGB (1900), aber dogmenhistorisch fortwirkend — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Rechtshistoriker, Lehrstühle, Restitutionsverfahren mit Altrecht-Bezug, Boden- und Erbschaftsstreite mit historischer Wurzel.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Rechtsvergleichende Stellungnahme, ALR-Auszug aus historischer Edition, dogmatische Untersuchung, Restitutionsgutachten, Erbschaftsgutachten — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Historischer Hintergrund

- Pockenimpfpflicht ab Mitte 19. Jh. in einzelnen Staaten Preussens.
- Reichsimpfgesetz 08.04.1874 fuehrte Pflichtimpfung gegen Pocken reichsweit ein.
- Bei Impfschaeden Ansprueche der Geschaedigten auf Aufopferungsentschaedigung.

## Aufopferungsanspruch

- Anker: Einl. §§ 74-75 ALR.
- "Sonderopfer" — der Buerger erbringt eine Sonderlast für die Allgemeinheit (Schutz gegen Seuchen).
- Entschaedigung verlangt rechtshistorisch zuerst die rechtliche Anerkennung des Eingriffs.

## Frueheste Klagen

- Preussische Gerichte erkannten erste Aufopferungsansprueche im Zusammenhang mit der Impfung.
- Erlass des Preussischen Innenministers (Daten und Inhalte vor Zitat verifizieren).

## Fortwirkung im 20. Jahrhundert

- BGHZ 9 Seite 83 — Aufopferungsanspruch im Polizeischadensfall.
- Reichsversorgungsgesetz und spaetere Reform.
- Heute IfSG §§ 60 ff. für Impfschaeden.

## Pruefraster

1. Hoheitliche Massnahme im Allgemeininteresse?
2. Sonderbelastung des Einzelnen?
3. Spezialgesetz greift (IfSG, POG)?
4. Allgemeiner Aufopferungsanspruch subsidiaer?
5. Quellenstellen Einl. §§ 74-75 ALR; BGHZ 9.

---

## Skill: `bereicherungsrecht-im-alr-condictiones`

_Ungerechtfertigte Bereicherung im ALR. Skill behandelt die roemische condictiones-Systematik im ALR die condictio indebiti die condictio sine causa die condictio ob rem die condictio ob iniustam causam und die Fortwirkung in §§ 812-822 BGB. Liefert Quellenmatrix im Preußisches Allgemeines Landrec..._

# Pralr Bereicherungsrecht Im Alr Condictiones

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: historisch — Verjährung nach ALR-Vorschriften (z. B. 30-jährige actio); heutige Anwendung über Art. 184 ff. EGBGB und § 195 BGB.
- Tragende Normen verifizieren: ALR Einleitung §§ 1-100, Erster Teil (Personen-/Sachenrecht), Zweiter Teil (Personenstand, Familie, Erbrecht), Allgemeine Gerichtsordnung; abgelöst durch BGB (1900), aber dogmenhistorisch fortwirkend — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Rechtshistoriker, Lehrstühle, Restitutionsverfahren mit Altrecht-Bezug, Boden- und Erbschaftsstreite mit historischer Wurzel.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Rechtsvergleichende Stellungnahme, ALR-Auszug aus historischer Edition, dogmatische Untersuchung, Restitutionsgutachten, Erbschaftsgutachten — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## ALR-Bereicherungsrecht

- ALR uebernimmt im wesentlichen die roemisch-rechtliche Lehre der condictiones.
- ALR I 16 §§ 1 ff. zur ungerechtfertigten Bereicherung.

## Typen

### Condictio indebiti
- Rueckforderung des irrtuemlich Gezahlten.

### Condictio sine causa
- Zuwendung ohne Rechtsgrund.

### Condictio ob rem
- Erwartete Gegenleistung blieb aus.

### Condictio ob iniustam causam
- Zuwendung wegen sittenwidrigem Geschaeft.

## Fortwirkung BGB

- § 812 BGB allgemeine Bereicherung.
- §§ 813-815 BGB Sonderfaelle.
- § 817 BGB sittenwidriger Erwerb.
- §§ 818-822 BGB Folgen.

## ALR vs. BGB

- ALR mehr kasuistisch.
- BGB-Generalklausel mit Aufgliederung.

## Pruefraster

1. Etwas erlangt?
2. Auf Kosten eines anderen?
3. Ohne Rechtsgrund?
4. Wertersatz oder Herausgabe?

---

## Skill: `sklavenrecht-alr-ii-5-196-197`

_Sklavenrecht im ALR — die beruehmten Bestimmungen ALR II 5 §§ 196 ff. zur Nichtanerkennung der Sklaverei in Preussen. Skill behandelt den Wortlaut der Schluesselparagraphen die Wirkung Sklavenstatus bei Grenzuebertritt zu enden die Frage nach einer 1-Jahres-Frist (mit kritischer Auseinandersetzun..._

# Sklavenrecht im ALR — ALR II 5 §§ 196 ff.

## Norm und Kontext

ALR Zweiter Teil, Fuenfter Titel (Vom Gesinde) enthaelt mehrere Bestimmungen zum Status auslaendischer Sklaven, die nach Preussen gelangen. Sie zaehlen zu den beruehmten Stellen des ALR und werden in der Diskussion um das "free soil"-Prinzip Europas regelmaessig zitiert.

### Schluesselparagraphen (Wortlaut sinngemaess)

- **ALR II 5 § 196**: "Sklaverei soll in den koeniglichen Staaten nicht geduldet werden."
- **ALR II 5 § 197**: "Sklaven, welche aus auswaertigen Ländern in die koeniglichen Staaten gebracht werden, sind, sobald sie die Grenze ueberschreiten, für frei zu erklaeren."
- **ALR II 5 § 198 ff.**: ergaenzende Regelungen zu Pflichten der ehemaligen Herrschaft und zum spaeteren Aufenthaltsstatus.

Wortlaut vor konkretem Zitat im Digitalisat (z. B. opinioiuris.de, Universitaetsbibliothek-Digitalisate) live verifizieren — die Paragraphennummerierung weicht zwischen Editionen 1794/1804 leicht ab.

## Rechtsfolge

- Eintritt in das Staatsgebiet **eo ipso** beendet den Sklavenstatus.
- Der frueher Versklavte wird ab Grenzuebertritt **frei** im Sinne des preussischen Personenrechts.
- Eigentumsansprueche des frueheren Herrn am Menschen sind in Preussen rechtlich nicht durchsetzbar.
- Die ehemalige Herrschaft hat allenfalls vertragliche Restansprueche (z. B. ueber Reisekosten Hausrat) — aber keine personenrechtliche Verfuegungsbefugnis.

## Die "1-Jahres-Frist"

In der Diskussion (auch bei juristischen Laien) taucht haeufig die Vorstellung auf, der Sklavenstatus erloesche erst nach **einem Jahr Aufenthalt**. Dies ist im ALR **so nicht niedergelegt** — die Befreiung wirkt nach §§ 196/197 sofort mit Grenzuebertritt.

Moegliche Quellen dieser Vorstellung:
- **Verwechselung mit dem englischen Common Law**: dort wurde im Somerset-Fall (Court of King's Bench, **22.06.1772**, Lord Mansfield) entschieden, dass Sklaven auf englischem Boden frei seien. Eine ausdrueckliche Jahresfrist gab es dort ebenfalls nicht.
- **Verwechselung mit dem franzoesischen Code Noir und der "freie Luft"-Klausel** im Edit de juin 1716 (geaendert 1738), wo eine **Drei-Jahres-Frist** für Reisende mit Sklaven aus den Kolonien zentral war, vor deren Ablauf der Sklavenstatus erhalten blieb. Diese Frist wirkte gegenlaeufig zum spaeteren ALR.
- **Anlage und Aufenthaltsregelung**: Im ALR gab es Bestimmungen zur **gesinderechtlichen Bindung** des frueher Versklavten an die ehemalige Herrschaft als Dienender. Diese gesinderechtliche Bindung war typischerweise auf **ein Jahr** angelegt (Jahresvertrag des Gesindes). Daraus mag der "1-Jahres"-Eindruck stammen — er bezieht sich aber auf die **gesinderechtliche Folgebindung**, nicht auf den Sklavenstatus selbst.

Im Ergebnis: Der Sklavenstatus erlischt im ALR **sofort** mit Grenzuebertritt. Eine etwaige Jahresfrist betrifft nur die gesinderechtliche Anschlussbindung nach altem Dienstrecht.

## Rechtshistorische Bedeutung

Die ALR-Norm wirkte als **rechtspolitische Demonstration** — Preussen als aufgeklaerter Staat im europaeischen Konzert. Sie war zugleich **praktisch begrenzt**: die Zahl der tatsaechlich nach Preussen gelangten Sklaven war gering, und die Regelung wurde im 19. Jahrhundert in einzelnen Faellen tatsaechlich angewendet (z. B. bei mit ihren Herrschaften reisenden Bediensteten aus den Karibik-Kolonien oder den nordamerikanischen Suedstaaten).

Spaetere Akte:
- **Edikt zur Aufhebung der Erbuntertaenigkeit** (sog. Oktoberedikt vom **09.10.1807**) hob die preussische Gutsuntertaenigkeit auf — innerpreussische "Leibeigenschaft" entfaellt.
- **Gesetz vom 09.03.1857**: Bestaetigung und Schaerfung des Verbots der Sklaverei.

## Verhaeltnis zu BGB / GG / Voelkerrecht

- **Art. 1 Abs. 1 GG, Art. 2 Abs. 2 GG**: Menschenwuerde und koerperliche Unversehrtheit als heutige Anker.
- **§ 138 Abs. 1 BGB**: ein Sklaverei-Vertrag ist sittenwidrig und nichtig.
- **Art. 4 EMRK**: Verbot der Sklaverei.
- **§ 233 StGB**: Menschenhandel.

## Pruefraster

1. Historische Fragestellung oder lebende Frage?
2. Quelle: ALR II 5 §§ 196 ff. (Wortlaut im Digitalisat verifizieren).
3. Sofortwirkung der Befreiung bei Grenzuebertritt klar darstellen.
4. "1-Jahres-Frist" kritisch einordnen (Verwechslung mit Code Noir oder mit gesinderechtlicher Anschlussbindung).
5. Heutige Norm (Art. 1 GG, § 138 BGB, § 233 StGB, Art. 4 EMRK).

---

## Skill: `sklavenrecht-rechtsvergleich`

_Rechtsvergleich Sklavenrecht — Preussen ALR vs. England Somerset 1772 vs. Frankreich Code Noir 1685/1716. Skill arbeitet die drei wichtigsten europaeischen Linien aus den Wirkungsmechanismus (sofortige Befreiung vs. Fristenkonstrukt) und die rechtsgeschichtliche Linie zur Abolition. Liefert Synopse._

# Rechtsvergleich Sklavenrecht — Preussen, England, Frankreich

## Preussen — ALR 1794

- ALR II 5 §§ 196 ff. (vor Zitat verifizieren): "Sklaverei soll in den koeniglichen Staaten nicht geduldet werden."
- **Sofortige Befreiung** bei Grenzuebertritt.
- Keine ausdrueckliche Fristenkonstruktion.

## England — Common Law

### Somerset's Case 1772
- **Somerset v. Stewart**, Court of King's Bench, **22.06.1772**, Lord Mansfield als Vorsitzender Richter.
- Sachverhalt: James Somerset, in den USA versklavter Schwarzer, wurde von seinem Herrn nach London gebracht. Er entkam, wurde wieder gefangen und sollte zwecks Wiederverkaufs nach Jamaika verbracht werden. Habeas-Corpus-Antrag fuehrte zur Entscheidung.
- Lord Mansfield: "The state of slavery is of such a nature, that it is incapable of being introduced on any reasons, moral or political, but only by positive law" — und positives englisches Recht erlaubte Sklaverei nicht.
- Sofortige Freilassung.

### Slavery Abolition Act 1833
- Abschaffung der Sklaverei im Empire (mit Uebergangsregeln und Entschaedigung der Sklavenhalter).

## Frankreich — Code Noir und freie-Luft-Klausel

### Code Noir 1685 (Louis XIV)
- Kolonialordnung für die franzoesischen Kolonien (Karibik, La Reunion, Louisiana).
- Sklaverei in den Kolonien gesetzlich geregelt.
- Im Mutterland Frankreich grundsaetzlich keine Sklaverei (Tradition "Le sol de France affranchit l'esclave qui le touche").

### Edit du Roi de Juin 1716
- Erlaubt die zeitweilige Mitnahme von Sklaven aus den Kolonien nach Frankreich zwecks Erziehung in Religion oder Beruf — Sklavenstatus bleibt **für maximal drei Jahre** erhalten.
- Im Anschluss Befreiung.

### Declaration du Roi 1738
- Praezisierung — verschaerfte Registrierungspflicht.

### Decret 04.02.1794 / Decret 27.04.1848
- 1794: Erstmals Abschaffung in den Kolonien (durch die Franzoesische Revolution).
- 1802: Wiedereinfuehrung durch Napoleon.
- **1848**: Endgueltige Abschaffung durch das Decret du Gouvernement Provisoire (Victor Schoelcher).

## USA (Vergleichsblick)

- **13. Zusatzartikel** zur US-Verfassung **18.12.1865**: Abschaffung der Sklaverei.
- Dred Scott v. Sandford (1857): vor 1865 verneinte der Supreme Court Schwarzen die Buergerschaft — Aufhebung durch den Buergerkrieg und 13./14./15. Amendment.

## Synopse — Wann erlischt der Sklavenstatus?

| Rechtsordnung | Wirkung | Frist |
|---|---|---|
| Preussen ALR 1794 | Sofort | Keine |
| England Common Law (Somerset 1772) | Sofort | Keine |
| Frankreich Code Noir 1685 / Edit 1716 | Aufschiebend | 3 Jahre (Edit 1716) |
| Niederlande (uebersee) | Verschieden je Provinz | — |
| Spanien (Kolonien) | Spaet, Las Siete Partidas | Lange Sklaverei |

## Bedeutung für das ALR

- ALR steht in **eindeutig befreiender Tradition** zusammen mit England.
- Frankreich-Modell (Edit 1716) mit Aufschub kennen die deutschen Staaten **nicht**.

## Pruefraster

1. Welche Rechtsordnung?
2. Wann hat der Status geendet?
3. Ausnahmeregelungen (Edit 1716)?
4. Beweisfragen?
5. Aktuelle voelkerrechtliche Bezuege.

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

---

## Skill: `sklavenrecht-rechtsvergleich-somerset-code-noir`

_Rechtsvergleich Sklavenrecht — Preussen ALR vs. England Somerset 1772 vs. Frankreich Code Noir 1685/1716. Skill arbeitet die drei wichtigsten europaeischen Linien aus den Wirkungsmechanismus (sofortige Befreiung vs. Fristenkonstrukt) und die rechtsgeschichtliche Linie zur Abolition. Liefert Synop..._

# Rechtsvergleich Sklavenrecht — Preussen, England, Frankreich

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

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: historisch — Verjährung nach ALR-Vorschriften (z. B. 30-jährige actio); heutige Anwendung über Art. 184 ff. EGBGB und § 195 BGB.
- Tragende Normen verifizieren: ALR Einleitung §§ 1-100, Erster Teil (Personen-/Sachenrecht), Zweiter Teil (Personenstand, Familie, Erbrecht), Allgemeine Gerichtsordnung; abgelöst durch BGB (1900), aber dogmenhistorisch fortwirkend — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Rechtshistoriker, Lehrstühle, Restitutionsverfahren mit Altrecht-Bezug, Boden- und Erbschaftsstreite mit historischer Wurzel.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Rechtsvergleichende Stellungnahme, ALR-Auszug aus historischer Edition, dogmatische Untersuchung, Restitutionsgutachten, Erbschaftsgutachten — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Preussen — ALR 1794

- ALR II 5 §§ 196 ff. (vor Zitat verifizieren): "Sklaverei soll in den koeniglichen Staaten nicht geduldet werden."
- **Sofortige Befreiung** bei Grenzuebertritt.
- Keine ausdrueckliche Fristenkonstruktion.

## England — Common Law

### Somerset's Case 1772
- **Somerset v. Stewart**, Court of King's Bench, **22.06.1772**, Lord Mansfield als Vorsitzender Richter.
- Sachverhalt: James Somerset, in den USA versklavter Schwarzer, wurde von seinem Herrn nach London gebracht. Er entkam, wurde wieder gefangen und sollte zwecks Wiederverkaufs nach Jamaika verbracht werden. Habeas-Corpus-Antrag fuehrte zur Entscheidung.
- Lord Mansfield: "The state of slavery is of such a nature, that it is incapable of being introduced on any reasons, moral or political, but only by positive law" — und positives englisches Recht erlaubte Sklaverei nicht.
- Sofortige Freilassung.

### Slavery Abolition Act 1833
- Abschaffung der Sklaverei im Empire (mit Uebergangsregeln und Entschaedigung der Sklavenhalter).

## Frankreich — Code Noir und freie-Luft-Klausel

### Code Noir 1685 (Louis XIV)
- Kolonialordnung für die franzoesischen Kolonien (Karibik, La Reunion, Louisiana).
- Sklaverei in den Kolonien gesetzlich geregelt.
- Im Mutterland Frankreich grundsaetzlich keine Sklaverei (Tradition "Le sol de France affranchit l'esclave qui le touche").

### Edit du Roi de Juin 1716
- Erlaubt die zeitweilige Mitnahme von Sklaven aus den Kolonien nach Frankreich zwecks Erziehung in Religion oder Beruf — Sklavenstatus bleibt **für maximal drei Jahre** erhalten.
- Im Anschluss Befreiung.

### Declaration du Roi 1738
- Praezisierung — verschaerfte Registrierungspflicht.

### Decret 04.02.1794 / Decret 27.04.1848
- 1794: Erstmals Abschaffung in den Kolonien (durch die Franzoesische Revolution).
- 1802: Wiedereinfuehrung durch Napoleon.
- **1848**: Endgueltige Abschaffung durch das Decret du Gouvernement Provisoire (Victor Schoelcher).

## USA (Vergleichsblick)

- **13. Zusatzartikel** zur US-Verfassung **18.12.1865**: Abschaffung der Sklaverei.
- Dred Scott v. Sandford (1857): vor 1865 verneinte der Supreme Court Schwarzen die Buergerschaft — Aufhebung durch den Buergerkrieg und 13./14./15. Amendment.

## Synopse — Wann erlischt der Sklavenstatus?

| Rechtsordnung | Wirkung | Frist |
|---|---|---|
| Preussen ALR 1794 | Sofort | Keine |
| England Common Law (Somerset 1772) | Sofort | Keine |
| Frankreich Code Noir 1685 / Edit 1716 | Aufschiebend | 3 Jahre (Edit 1716) |
| Niederlande (uebersee) | Verschieden je Provinz | — |
| Spanien (Kolonien) | Spaet, Las Siete Partidas | Lange Sklaverei |

## Bedeutung für das ALR

- ALR steht in **eindeutig befreiender Tradition** zusammen mit England.
- Frankreich-Modell (Edit 1716) mit Aufschub kennen die deutschen Staaten **nicht**.

## Pruefraster

1. Welche Rechtsordnung?
2. Wann hat der Status geendet?
3. Ausnahmeregelungen (Edit 1716)?
4. Beweisfragen?
5. Aktuelle voelkerrechtliche Bezuege.

---

## Skill: `strafprozess-willensmaengel`

_Strafprozess im ALR — Inquisitionsverfahren. Skill behandelt das Inquisitionsprinzip die Folter-Aufhebung Friedrichs II. 1740 die Beweismittel Indizienbeweis Folterabbau und die Reform durch die rheinische Strafprozessordnung 1849 mit Schwurgericht. Liefert Quellenmatrix im Preußisches Allgemeine..._

# Pralr Strafprozess Und Inquisition

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 StGB` — Keine Strafe ohne Gesetz.
- `§ 15 StGB` — Vorsatz/Fahrlaessigkeit.
- `§ 16 Abs. 1 StGB` — Tatbestandsirrtum.
- `§ 17 StGB` — Verbotsirrtum.
- `§ 46 Abs. 1 StGB` — Strafzumessung.
- `§ 152 Abs. 2 StPO` — Legalitaetsprinzip/Anfangsverdacht.
- `§ 160 Abs. 2 StPO` — Ermittlung auch entlastender Umstaende.
- `§ 244 Abs. 2 StPO` — Aufklaerungspflicht.
- `§ 261 StPO` — freie richterliche Beweiswuerdigung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: historisch — Verjährung nach ALR-Vorschriften (z. B. 30-jährige actio); heutige Anwendung über Art. 184 ff. EGBGB und § 195 BGB.
- Tragende Normen verifizieren: ALR Einleitung §§ 1-100, Erster Teil (Personen-/Sachenrecht), Zweiter Teil (Personenstand, Familie, Erbrecht), Allgemeine Gerichtsordnung; abgelöst durch BGB (1900), aber dogmenhistorisch fortwirkend — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Rechtshistoriker, Lehrstühle, Restitutionsverfahren mit Altrecht-Bezug, Boden- und Erbschaftsstreite mit historischer Wurzel.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Rechtsvergleichende Stellungnahme, ALR-Auszug aus historischer Edition, dogmatische Untersuchung, Restitutionsgutachten, Erbschaftsgutachten — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Inquisitionsprinzip

- Untersuchungsrichter ermittelt von Amts wegen.
- Verteidigung erst spaet im Verfahren.
- ALR II 20 — Strafverfahren.

## Folter

- Friedrich II. hob die Folter 1740 in Preussen ab (Cabinets-Order).
- Konkrete Massnahmen 1754.
- Restbestimmungen formell erst spaeter.

## Beweismittel

- Gestaendnis als "regina probationum".
- Zeugenbeweis.
- Urkunden.
- Indizienbeweis (in der Praxis weitergehend).

## Reform 1849

- Rheinische Strafprozessordnung mit Schwurgericht.
- Oeffentlichkeit Muendlichkeit Anklageprinzip.
- Vorbild für die preussische Strafprozessordnung 1851 und die Reichs-StPO 1877.

## Fortwirkung

- Heutige StPO 1877.
- Schwurgericht abgeschafft 1924.
- Schoeffengericht heute.

## Pruefraster

1. Welche Periode?
2. Welches Verfahrensprinzip?
3. Welche Beweisregel?

---

## Skill: `zwitterrecht-alr-ii-1-19-bis-22`

_Zwitterrecht nach ALR — das beruehmte preussische Sonderrecht der Wahlmoeglichkeit. ALR II 1 §§ 19 bis 22 regelte das Geschlecht der Zwitter (Hermaphroditen): Eltern bestimmen Geschlecht bis 18 Jahre danach Wahlrecht des Betroffenen. Skill behandelt Norm Inhalt rechtshistorische Bedeutung und die..._

# Pralr Zwitterrecht Alr Ii 1 19 Bis 22

## Norm

ALR II 1 §§ 19 bis 22 — die wahrscheinlich beruehmteste Detailregelung des ALR und ein viel zitiertes Kuriosum.

### § 19 ALR II 1
"Wenn Zwitter geboren werden, so bestimmen die Eltern das Geschlecht, in welchem sie erzogen werden sollen."

### § 20 ALR II 1
"Jedoch steht solchen Zwittern nach zuruecksgelegtem 18. Jahre die Wahl frei, welchem Geschlechte sie sich beizaehlen wollen."

### § 21 ALR II 1
"Nach dieser Wahl werden ihre Rechte kuenftig beurteilt."

### § 22 ALR II 1
"Sind aber Rechte eines Dritten von dem Geschlechte des vermeintlichen Zwitters abhaengig, so kann auf dessen Antrag der Spruch der Sachverstaendigen erfordert werden."

## Rechtshistorische Bedeutung

- Beleg für den kasuistischen Anspruch des ALR — selbst seltenste Konstellationen geregelt.
- Aufgeklaerter Charakter: Wahlrecht des Volljaehrigen, nicht nur fremdbestimmt durch Eltern oder Aerzte.
- Sachverstaendigenkompetenz: Aerzte werden im Streit gehoert.

## Aufhebung

- BGB 1900 enthielt keine Sondernorm zum intersexuellen Status.
- Geschlechtsstatus war jahrzehntelang nur "Mann" oder "Frau" im Personenstand.
- Erst PStG-Reform 2013: Eintragung Geschlecht "offen lassen" moeglich.
- BVerfG 1 BvR 2019/16 vom 10.10.2017 (sogenannte "Dritte Option") — Recht auf positiven Personenstandseintrag jenseits von "maennlich" und "weiblich".
- Personenstandsrecht-Reform 22.12.2018 — Eintrag "divers".

## Wiederentdeckung

- In der modernen Diskussion um Intersexualitaet wird ALR-Norm als bemerkenswert frueh anerkennendes Beispiel zitiert.
- Norm ist humaner und individueller als das BGB-System des Personenstandsrechts vor 2013/2017/2018.

## Pruefraster

1. Geschichtswissenschaft oder lebendes Recht?
2. Vergleich zu modernem Personenstandsrecht.
3. § 22 PStG (Eintrag) heute.

---

## Skill: `zinsobergrenze-und-wuchertatbestand`

_Zinsobergrenze und Wuchertatbestand im ALR. Skill behandelt die historische Zinsobergrenze (centesima usura 12 Prozent oder 6 Prozent) Sondervorschriften beim fenus nauticum und das Verhaeltnis zum heutigen Wucherrecht § 138 II BGB und § 291 StGB. Liefert Quellenmatrix im Preußisches Allgemeines..._

# Pralr Zinsobergrenze Und Wuchertatbestand

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: historisch — Verjährung nach ALR-Vorschriften (z. B. 30-jährige actio); heutige Anwendung über Art. 184 ff. EGBGB und § 195 BGB.
- Tragende Normen verifizieren: ALR Einleitung §§ 1-100, Erster Teil (Personen-/Sachenrecht), Zweiter Teil (Personenstand, Familie, Erbrecht), Allgemeine Gerichtsordnung; abgelöst durch BGB (1900), aber dogmenhistorisch fortwirkend — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Rechtshistoriker, Lehrstühle, Restitutionsverfahren mit Altrecht-Bezug, Boden- und Erbschaftsstreite mit historischer Wurzel.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Rechtsvergleichende Stellungnahme, ALR-Auszug aus historischer Edition, dogmatische Untersuchung, Restitutionsgutachten, Erbschaftsgutachten — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## ALR-Zinsobergrenze

- Allgemein 5 oder 6 Prozent pro Jahr (regional unterschiedlich).
- Bei besonderen Geschaeften Sondergrenzen.
- ALR I 11 / I 13.

## Fenus nauticum

- Seedarlehen mit hoeheren Zinsen.
- Sondervorschrift, vgl. Skill `rom-123-fenus-nauticum-seedarlehen` im roemisches-recht-Plugin.

## Wuchertatbestand

- ALR II 20 — Wucher als Strafdelikt.
- Heute § 291 StGB.

## Fortwirkung

- BGB § 138 Abs. 2 BGB — Wucher-Sittenwidrigkeit.
- § 291 StGB Wucherstrafrecht.
- BGH-Linie: Zinssatz mehr als doppelt ueber dem marktueblichen Satz indiziert Wucher.

## Pruefraster

1. Vereinbarter Zinssatz?
2. Marktueblicher Vergleich?
3. Wuchertatbestand?

---

## Skill: `sklaverei-aufhebung-edikte-1807`

_Aufhebung der Sklaverei und der Erbuntertaenigkeit in Preussen — vom ALR ueber das Oktoberedikt 1807 bis zum Gesetz 1857. Skill ordnet die Edikte chronologisch ein klaert das Verhaeltnis von Sklaverei und Erbuntertaenigkeit und zeigt die rechtshistorische Linie zum Reichsgesetz und zum BGB. Liefe_

# Aufhebung Sklaverei und Erbuntertaenigkeit in Preussen 1794-1857

## Begriffliche Trennung

- **Sklaverei**: Person ist als res Eigentum eines anderen.
- **Erbuntertaenigkeit / Gutsuntertaenigkeit / Leibeigenschaft**: persönliche Bindung der baeuerlichen Bevoelkerung an einen Grundherrn mit Bewegungs-, Heirats- und Berufsbeschraenkungen, aber ohne Eigentumsstellung des Herrn am Menschen.

Beide Institute werden umgangssprachlich vermengt, sind rechtshistorisch aber zu trennen.

## ALR 1794

- ALR II 5 §§ 196 ff. (vor Zitat verifizieren): Sklaverei in Preussen nicht geduldet; sofortige Befreiung bei Grenzuebertritt.
- ALR II 7 (Bauernstand): Gutsuntertaenigkeit der baeuerlichen Bevoelkerung als reale Lebenslage Preussens. Modifikation, aber keine Aufhebung.

## Oktoberedikt 09.10.1807

- "Edikt den erleichterten Besitz und den freien Gebrauch des Grundeigenthums sowie die persönlichen Verhaeltnisse der Land-Bewohner betreffend" — bekannt als **Stein-Hardenbergsches Oktoberedikt**.
- Inhalt: Aufhebung der Erbuntertaenigkeit der Bauern in Preussen mit Wirkung **St. Martini 1810**.
- Wirkung: Bauern werden persoenlich frei; Berufswahl und Eheschliessung frei; Mobilitaet hergestellt.
- Inhaltlich: Frondienste und Reallasten bleiben zunaechst, werden in Folge-Edikten abgeloest.

## Folge-Edikte

- **Regulierungsedikt 14.09.1811**: Loesung der gutsherrlichen Lasten gegen Entschaedigung.
- **Gemeinheitsteilungsordnung 1821**: Aufteilung der Allmenden und Gemeinheiten.
- **Ablooesungsordnung 1850**: vollstaendige Beseitigung der Restlasten.

## Gesetz vom 09.03.1857

- Bestaetigung des Sklavereiverbots reichseinheitlich (in Preussen).
- Klarstellung gegenueber den Auswanderungs- und Einwanderungsverhaeltnissen.
- Reaktion auch auf die internationale Diskussion (Abolition USA 1865, England 1833).

## Reichsweite Folge

- Reichsverfassung 1871 — kein Sklavereirecht.
- BGB 1900 — Personenrecht ohne Sklavenstatus; § 138 BGB sittenwidrig.
- Reichsgesetze gegen Menschenhandel ab 19. Jh.

## Heute

- Art. 1, 2 GG.
- Art. 4 EMRK.
- §§ 232-233a StGB Menschenhandel und Sklaverei.
- UN-Slavery Convention 1926, ergaenzendes Uebereinkommen 1956.

## Pruefraster

1. Welche Norm welcher Epoche?
2. Sklaverei oder Erbuntertaenigkeit (begriffliche Trennung!)?
3. Welches Folge-Edikt einschlaegig?
4. Heutige Aequivalenz?

---

## Skill: `sklaverei-aufhebung-und-edikte-1807-1857`

_Aufhebung der Sklaverei und der Erbuntertaenigkeit in Preussen — vom ALR ueber das Oktoberedikt 1807 bis zum Gesetz 1857. Skill ordnet die Edikte chronologisch ein klaert das Verhaeltnis von Sklaverei und Erbuntertaenigkeit und zeigt die rechtshistorische Linie zum Reichsgesetz und zum BGB. Liefe_

# Aufhebung Sklaverei und Erbuntertaenigkeit in Preussen 1794-1857

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: historisch — Verjährung nach ALR-Vorschriften (z. B. 30-jährige actio); heutige Anwendung über Art. 184 ff. EGBGB und § 195 BGB.
- Tragende Normen verifizieren: ALR Einleitung §§ 1-100, Erster Teil (Personen-/Sachenrecht), Zweiter Teil (Personenstand, Familie, Erbrecht), Allgemeine Gerichtsordnung; abgelöst durch BGB (1900), aber dogmenhistorisch fortwirkend — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Rechtshistoriker, Lehrstühle, Restitutionsverfahren mit Altrecht-Bezug, Boden- und Erbschaftsstreite mit historischer Wurzel.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Rechtsvergleichende Stellungnahme, ALR-Auszug aus historischer Edition, dogmatische Untersuchung, Restitutionsgutachten, Erbschaftsgutachten — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Begriffliche Trennung

- **Sklaverei**: Person ist als res Eigentum eines anderen.
- **Erbuntertaenigkeit / Gutsuntertaenigkeit / Leibeigenschaft**: persönliche Bindung der baeuerlichen Bevoelkerung an einen Grundherrn mit Bewegungs-, Heirats- und Berufsbeschraenkungen, aber ohne Eigentumsstellung des Herrn am Menschen.

Beide Institute werden umgangssprachlich vermengt, sind rechtshistorisch aber zu trennen.

## ALR 1794

- ALR II 5 §§ 196 ff. (vor Zitat verifizieren): Sklaverei in Preussen nicht geduldet; sofortige Befreiung bei Grenzuebertritt.
- ALR II 7 (Bauernstand): Gutsuntertaenigkeit der baeuerlichen Bevoelkerung als reale Lebenslage Preussens. Modifikation, aber keine Aufhebung.

## Oktoberedikt 09.10.1807

- "Edikt den erleichterten Besitz und den freien Gebrauch des Grundeigenthums sowie die persönlichen Verhaeltnisse der Land-Bewohner betreffend" — bekannt als **Stein-Hardenbergsches Oktoberedikt**.
- Inhalt: Aufhebung der Erbuntertaenigkeit der Bauern in Preussen mit Wirkung **St. Martini 1810**.
- Wirkung: Bauern werden persoenlich frei; Berufswahl und Eheschliessung frei; Mobilitaet hergestellt.
- Inhaltlich: Frondienste und Reallasten bleiben zunaechst, werden in Folge-Edikten abgeloest.

## Folge-Edikte

- **Regulierungsedikt 14.09.1811**: Loesung der gutsherrlichen Lasten gegen Entschaedigung.
- **Gemeinheitsteilungsordnung 1821**: Aufteilung der Allmenden und Gemeinheiten.
- **Ablooesungsordnung 1850**: vollstaendige Beseitigung der Restlasten.

## Gesetz vom 09.03.1857

- Bestaetigung des Sklavereiverbots reichseinheitlich (in Preussen).
- Klarstellung gegenueber den Auswanderungs- und Einwanderungsverhaeltnissen.
- Reaktion auch auf die internationale Diskussion (Abolition USA 1865, England 1833).

## Reichsweite Folge

- Reichsverfassung 1871 — kein Sklavereirecht.
- BGB 1900 — Personenrecht ohne Sklavenstatus; § 138 BGB sittenwidrig.
- Reichsgesetze gegen Menschenhandel ab 19. Jh.

## Heute

- Art. 1, 2 GG.
- Art. 4 EMRK.
- §§ 232-233a StGB Menschenhandel und Sklaverei.
- UN-Slavery Convention 1926, ergaenzendes Uebereinkommen 1956.

## Pruefraster

1. Welche Norm welcher Epoche?
2. Sklaverei oder Erbuntertaenigkeit (begriffliche Trennung!)?
3. Welches Folge-Edikt einschlaegig?
4. Heutige Aequivalenz?

---

## Skill: `strafprozess-und-inquisition`

_Strafprozess im ALR — Inquisitionsverfahren. Skill behandelt das Inquisitionsprinzip die Folter-Aufhebung Friedrichs II. 1740 die Beweismittel Indizienbeweis Folterabbau und die Reform durch die rheinische Strafprozessordnung 1849 mit Schwurgericht. Liefert Quellenmatrix._

# Pralr Strafprozess Und Inquisition

## Inquisitionsprinzip

- Untersuchungsrichter ermittelt von Amts wegen.
- Verteidigung erst spaet im Verfahren.
- ALR II 20 — Strafverfahren.

## Folter

- Friedrich II. hob die Folter 1740 in Preussen ab (Cabinets-Order).
- Konkrete Massnahmen 1754.
- Restbestimmungen formell erst spaeter.

## Beweismittel

- Gestaendnis als "regina probationum".
- Zeugenbeweis.
- Urkunden.
- Indizienbeweis (in der Praxis weitergehend).

## Reform 1849

- Rheinische Strafprozessordnung mit Schwurgericht.
- Oeffentlichkeit Muendlichkeit Anklageprinzip.
- Vorbild für die preussische Strafprozessordnung 1851 und die Reichs-StPO 1877.

## Fortwirkung

- Heutige StPO 1877.
- Schwurgericht abgeschafft 1924.
- Schoeffengericht heute.

## Pruefraster

1. Welche Periode?
2. Welches Verfahrensprinzip?
3. Welche Beweisregel?

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 StGB` — Keine Strafe ohne Gesetz.
- `§ 15 StGB` — Vorsatz/Fahrlaessigkeit.
- `§ 16 Abs. 1 StGB` — Tatbestandsirrtum.
- `§ 17 StGB` — Verbotsirrtum.
- `§ 46 Abs. 1 StGB` — Strafzumessung.
- `§ 152 Abs. 2 StPO` — Legalitaetsprinzip/Anfangsverdacht.
- `§ 160 Abs. 2 StPO` — Ermittlung auch entlastender Umstaende.
- `§ 244 Abs. 2 StPO` — Aufklaerungspflicht.
- `§ 261 StPO` — freie richterliche Beweiswuerdigung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Powersprint-Vertiefung

- **Quellenarbeit:** Vor einer Aussage die betroffene ALR-Stelle mit Teil, Titel und Paragraph aus der 1794er oder 1804er Fassung festhalten; Abweichungen zwischen Fassungen nur behaupten, wenn sie am Text belegt sind.
- **Historische Funktion:** Erkläre, ob `Pralr Strafprozess Und Inquisition` eher ständische Ordnung, Kameralstaat, Privatrechtsdogmatik, Polizeirecht oder frühe Verfahrensrationalisierung abbildet.
- **Moderner Vergleich:** Stelle die heutige Parallele nur als Vergleich daneben, etwa BGB, ZPO, FamFG, StGB/StPO oder öffentliches Recht; niemals so tun, als gelte ALR-Recht noch unmittelbar.
- **Output:** Liefere eine Mini-Synopse `ALR-Regel / historisches Problem / heutige Vergleichsnorm / didaktischer Nutzen / offene Quellenprüfung`.

---

## Skill: `zinsobergrenze-wuchertatbestand`

_Zinsobergrenze und Wuchertatbestand im ALR. Skill behandelt die historische Zinsobergrenze (centesima usura 12 Prozent oder 6 Prozent) Sondervorschriften beim fenus nauticum und das Verhaeltnis zum heutigen Wucherrecht § 138 II BGB und § 291 StGB. Liefert Quellenmatrix._

# Pralr Zinsobergrenze Und Wuchertatbestand

## ALR-Zinsobergrenze

- Allgemein 5 oder 6 Prozent pro Jahr (regional unterschiedlich).
- Bei besonderen Geschaeften Sondergrenzen.
- ALR I 11 / I 13.

## Fenus nauticum

- Seedarlehen mit hoeheren Zinsen.
- Sondervorschrift, vgl. Skill `rom-123-fenus-nauticum-seedarlehen` im roemisches-recht-Plugin.

## Wuchertatbestand

- ALR II 20 — Wucher als Strafdelikt.
- Heute § 291 StGB.

## Fortwirkung

- BGB § 138 Abs. 2 BGB — Wucher-Sittenwidrigkeit.
- § 291 StGB Wucherstrafrecht.
- BGH-Linie: Zinssatz mehr als doppelt ueber dem marktueblichen Satz indiziert Wucher.

## Pruefraster

1. Vereinbarter Zinssatz?
2. Marktueblicher Vergleich?
3. Wuchertatbestand?

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

## Powersprint-Vertiefung

- **Quellenarbeit:** Vor einer Aussage die betroffene ALR-Stelle mit Teil, Titel und Paragraph aus der 1794er oder 1804er Fassung festhalten; Abweichungen zwischen Fassungen nur behaupten, wenn sie am Text belegt sind.
- **Historische Funktion:** Erkläre, ob `Pralr Zinsobergrenze Und Wuchertatbestand` eher ständische Ordnung, Kameralstaat, Privatrechtsdogmatik, Polizeirecht oder frühe Verfahrensrationalisierung abbildet.
- **Moderner Vergleich:** Stelle die heutige Parallele nur als Vergleich daneben, etwa BGB, ZPO, FamFG, StGB/StPO oder öffentliches Recht; niemals so tun, als gelte ALR-Recht noch unmittelbar.
- **Output:** Liefere eine Mini-Synopse `ALR-Regel / historisches Problem / heutige Vergleichsnorm / didaktischer Nutzen / offene Quellenprüfung`.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

