# Zitierweise deutsches Recht (v4.1)

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`zitierweise-deutsches-recht`) | [`zitierweise-deutsches-recht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/zitierweise-deutsches-recht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Dr. Ottilie Mondsee und die verschwundene R-Besoldung** (`beamtenrecht-richterlaufbahn-besoldung-mondsee`) | [Gesamt-PDF lesen](../testakten/beamtenrecht-richterlaufbahn-besoldung-mondsee/gesamt-pdf/beamtenrecht-richterlaufbahn-besoldung-mondsee_gesamt.pdf) | [`testakte-beamtenrecht-richterlaufbahn-besoldung-mondsee.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-beamtenrecht-richterlaufbahn-besoldung-mondsee.zip) |
| **Zitierweise-Pruefkorpus — Kanzlei Roosendaal Birkenhainer Partners mbB — Kanzleihandbuch v4 mit 100 Fundstellen und Pruefvermerken** (`zitierweise-pruefkorpus-roosendaal-kanzleihandbuch-mit-100-fundstellen-und-pruefvermerken`) | [Gesamt-PDF lesen](../testakten/zitierweise-pruefkorpus-roosendaal-kanzleihandbuch-mit-100-fundstellen-und-pruefvermerken/gesamt-pdf/zitierweise-pruefkorpus-roosendaal-kanzleihandbuch-mit-100-fundstellen-und-pruefvermerken_gesamt.pdf) | [`testakte-zitierweise-pruefkorpus-roosendaal-kanzleihandbuch-mit-100-fundstellen-und-pruefvermerken.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-zitierweise-pruefkorpus-roosendaal-kanzleihandbuch-mit-100-fundstellen-und-pruefvermerken.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Deutsche juristische Hauszitierweise als zuschaltbares Plugin. Fokus: belastbare, überprüfbare Quellen statt schöner, aber nicht verifizierbarer Fundstellen.

## Was ist neu in v4.1

1. **BeckRS-Sperre:** BeckRS-Fundstellen werden nicht mehr aus Modellwissen erzeugt. Sie dürfen nur übernommen werden, wenn der Nutzer sie liefert oder ein lizenzierter Live-Zugriff sie verifiziert.
2. **Literatur-Sperre:** Kommentare, Handbücher, Monographien und Aufsätze werden nicht blind zitiert. Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
3. **Rechtsprechungs-Mindeststandard:** Gericht, Entscheidungsform, Datum und Aktenzeichen sind Pflicht. Wo möglich kommt eine amtliche oder frei zugängliche Quelle dazu.
4. **Keine Palandt-/Pahlen-Aktualzitate:** Der frühere Palandt heißt seit 2022 Grüneberg; historische Altauflagen nur bei konkreter Nutzerquelle.
5. **Prüfvermerk statt Halluzination:** Unverifizierte Entscheidungen werden markiert oder weggelassen, nicht ausgeschmückt.

## Installation in Claude Code

1. ZIP herunterladen.
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/` und `references/` im ZIP-Root enthalten. Nicht das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `zitierweise-deutsches-recht-allgemein` | Einstieg, Schnelltriage und Routing: klärt, ob ein Text Zitate erzeugen, glätten, prüfen oder sperren soll. |
| `zitierweise-anwenden` | Wendet die Quellenregel v4.1 an: Rechtsprechung nur mit Datum, Aktenzeichen und verifizierbarer Quelle; keine BeckRS-, Kommentar- oder Aufsatz-Blindzitate. |

## Kurzregel

Norm zuerst. Dann verifizierte Rechtsprechung. Literatur nur bei bereitgestellter oder live verifizierter Quelle. Keine BeckRS-, Kommentar- oder Aufsatz-Blindzitate.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 70 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aufsatz-interessen` | Aufsatz: Mehrparteienkonflikt und Interessenmatrix: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `aufsatz-interessen-beckrs-blindzitate` | Aufsatz Mehrparteien Konflikt Und Interessen, Beckrs Zahlen Schwellen Und Berechnung, Blindzitate Internationaler Bezug Und Schnittstellen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert... |
| `datum-entscheidungsform-spezial-gericht` | Datum Behörden Gericht Und Registerweg, Entscheidungsform Risikoampel Und Gegenargumente, Gericht Dokumentenmatrix Und Lueckenliste: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nä... |
| `gericht-dokumentenmatrix-und-lueckenliste` | Gericht: Dokumentenmatrix, Lückenliste und Nachforderung: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `hauszitierweise-juristische-kommentar` | Hauszitierweise Tatbestand Beweis Und Belege, Juristische Erstpruefung Und Mandatsziel, Kommentar Compliance Dokumentation Und Akte: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nä... |
| `literatur-live-beweislast-lizenziertem` | Literatur Formular Portal Und Einreichung, Live Beweislast Und Darlegungslast, Lizenziertem Mandantenkommunikation Entscheidungsvorlage: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert de... |
| `live-beweislast-darlegungslast` | Live: Beweislast, Darlegungslast und Substantiierung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `nutzerquelle-fehlerkatalog` | Nutzerquelle Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `paywallfreie-rechtsprechungsbelege` | Paywallfreie, prüfbare Rechtsprechungsbelege ohne Blindzitate: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `quelle-quellenkarte` | Quelle Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `rechtsprechung-zit-rechtsprechungszitierung` | Rechtsprechung Fristen Form Und Zustaendigkeit, Zit Rechtsprechungszitierung Leitfaden, Zitat Eugh Rechtsprechung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren... |
| `verifizierbarer-zugriff-sonderfall-zit` | Verifizierbarer Verhandlung Vergleich Und Eskalation, Zugriff Sonderfall Und Edge Case, Zit Gesetzeszitierung Bauleiter: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belas... |
| `zit-gesetzeszitierung-bauleiter` | Bauleiter Gesetzeszitierung in Schriftsatz und Memo: Norm, Absatz, Satz, Halbsatz, Nummer, Buchstabe. Pruefraster fuer einheitliche Schreibweise. |
| `zit-internationale-urteile-spezial` | Spezialfall Zitierung internationaler Urteile EuGH EGMR sowie Common-Law-Urteile: ECLI, Neutral Citation, Public Domain. Pruefraster fuer internationale Mandate. |
| `zit-internationale-zit-kommentar-zitat` | Zit Internationale Urteile Spezial, Zit Kommentar Aufsatzzitierung Spezial, Zitat Amtliche Sammlung Vs Zeitschrift: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbare... |
| `zit-kommentar-aufsatzzitierung-spezial` | Spezialfall Kommentar- und Aufsatzzitierung: Bearbeiter, Randnummer, Auflagenjahr, Zeitschrift, Heft, Seite. Pruefraster fuer wissenschaftliches Schreiben. |
| `zit-rechtsprechungszitierung-leitfaden` | Leitfaden Rechtsprechungszitierung BGH BVerfG EuGH: Gericht, Entscheidungsform, Datum, Aktenzeichen, frei pruefbarer Link dejure.org / openjur.de. Pruefraster fuer Memos. |
| `zitat-amtliche-sammlung-vs-zeitschrift` | Amtliche Sammlung vs. Zeitschrift: Reihenfolge der Fundstellen. Amtliche Sammlung (BGHZ, BVerfGE) hat Vorrang, dann Parallelfundstelle Zeitschrift (NJW, JZ, ZIP). Beispiel BGHZ 240 S. 1 = NJW 2024 S. 1832. |
| `zitat-archivierungspflicht` | Archivierungspflicht der zitierten Quelle: Screenshot mit Datum, PDF-Abruf, archive.org-Backup. Wichtig bei Schriftsaetzen, weil Online-Quellen veraendert werden. Empfehlung Kanzleiprozess. |
| `zitat-archivierungspflicht-aufsatz` | Zitat Archivierungspflicht, Zitat Aufsatz Zeitschrift, Zitat Bag Bfh Bsg Bag: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `zitat-aufsatz-zeitschrift` | Aufsatz in juristischer Zeitschrift nur bei vorliegendem Beitrag zitieren: Verfasser, Titel, Zeitschrift, Jahr, Heft/Seite und Pinpoint aus Nutzerquelle oder Live-Zugriff übernehmen. Keine Aufsatzfundstellen aus Modellwissen. |
| `zitat-bag-bfh-bsg-bag` | Fachgerichtsbarkeit zitieren: BAG, BFH, BSG, BVerwG, BGH. Format Senat, Datum, Aktenzeichen, amtliche Sammlung sowie Parallel-Fundstelle. Beispiel BAG, Urt. v. 12.09.2023 9 AZR 372 aus 22, BAGE 178 S. 199 = NZA 2023 S. 1521. |
| `zitat-bgh-entscheidung` | BGH-Entscheidung korrekt zitieren: Senat, Datum, Aktenzeichen, Fundstelle. Beispiel BGH, Urt. v. 11.04.2024 III ZR 168 aus 23, BGHZ 240 S. 1 = NJW 2024 S. 1832. Bei wichtiger Linie: Vor- und Folgeentscheidungen ergaenzen. |
| `zitat-bgh-entscheidung-bverfg-gesetz` | Zitat Bgh Entscheidung, Zitat Bverfg Entscheidung, Zitat Gesetz Verordnung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `zitat-bverfg-entscheidung` | BVerfG-Entscheidung zitieren: Senatsnummer, Datum, Aktenzeichen, BVerfGE, ggf. Kammerbeschluss. BVerfGE-Band und Seitenzahl nur übernehmen, wenn sie amtlich oder frei verifizierbar sind; andernfalls mit Gericht, Entscheidungsform, Datum... |
| `zitat-eugh-rechtsprechung` | EuGH-Rechtsprechung zitieren: Urt./Beschl., Datum, Rs. C-Nummer, Parteinamen, ECLI. Beispiel EuGH, Urt. v. 04.07.2019 - C-377/17, Kommission/Deutschland, ECLI:EU:C:2019:562. Bei Generalanwalts-Schlussantraegen: GA-Anfang. |
| `zitat-gesetz-verordnung` | Gesetz/Verordnung zitieren: Norm-Bezeichnung, ggf. § und Absatz. Beispiel § 17 InsO, § 311 Abs. 2 BGB, Art. 26 DSGVO. Bei zeitlicher Bezugnahme: § X i. d. F. v. JJJJ. |
| `zitat-haus-zitierregel-anpassen` | Kanzlei-Hauszitierweise anpassen: Excel-Vorlage Beck/NJW vs. Hartung/Roemermann v4. Empfehlung: konsistente Regel pro Kanzlei, in den Schriftsatz-Templates verankern. Output: Hauszitierregel-Dokument. |
| `zitat-haus-zitierregel-instanzgerichte` | Zitat Haus Zitierregel Anpassen, Zitat Instanzgerichte Strategisch, Zitat Internationale Quellen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `zitat-instanzgerichte-strategisch` | Instanzgerichts-Entscheidungen strategisch zitieren: OLG-Entscheidungen, LG-Entscheidungen. Wann sinnvoll: Tendenzen, Lokal-Linien, Fehlen BGH-Rechtsprechung. Vermeiden: AG-Entscheidungen ausser bei sehr engen Fragen. |
| `zitat-internationale-quellen` | Internationale Quellen: EuGH, EGMR, Common-Law-Faelle (in IPR-Kontext). Format mit ECLI bzw. Neutral Citation. Beispiel EGMR, Urt. v. 23.01.2024 - Nr. 12345/22, ECLI:CE:ECHR:2024:0123JUD001234522. |
| `zitat-internet-quellen` | Internet-Quellen zitieren: Stand, URL, Abrufdatum. Bevorzugt: dejure.org, openjur.de, bundesgerichtshof.de, bundesverfassungsgericht.de, eur-lex. Vermeiden: anwalt24.de, BeckRS allein als einzige Fundstelle. |
| `zitat-internet-quellen-kommentar-randnummer` | Zitat Internet Quellen, Zitat Kommentar Randnummer, Zitat Leitsatzentscheidung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `zitat-kommentar-randnummer` | Kommentar mit Bearbeiter und Randnummer nur bei vorliegender Nutzerquelle oder lizenziertem Live-Zugriff zitieren: Bearbeiter, Werk, aktuelle Auflage/Stand, Norm, Randnummer. Keine Kommentar-Rn. aus Modellwissen. |
| `zitat-leitsatzentscheidung` | Leitsatz-Entscheidung mit Leitsatz zitieren: BGH, Urt. ..., Leitsatz 1 lautet: ... Original-Leitsatz im Wortlaut, dann Begruendung mit Rn. Format fuer Schriftsatz und Memo. |
| `zitat-monografie-handbuch` | Monografie oder Handbuch nur bei vorliegender Quelle zitieren: Verfasser/Bearbeiter, Titel, Auflage/Stand, Jahr, Kapitel/Norm, Seite/Rn. Keine Handbuchfundstellen aus Modellwissen. |
| `zitat-monografie-handbuch-streitstand` | Zitat Monografie Handbuch, Zitat Streitstand Darstellen, Zitat Verboten Anwalt24 Beckrs: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `zitat-rechtsprechung-fristennotiz-naechster` | Zitat Rechtsprechung Ohne Fundstelle, Zitierweise Fristennotiz Und Naechster Schritt, Aktenzeichen Schriftsatz Brief Und Memo Bausteine: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert de... |
| `zitat-rechtsprechung-ohne-fundstelle` | Rechtsprechung ohne amtliche/freie Fundstelle behandeln: Gericht Datum Aktenzeichen sichern, freie Quelle suchen, Datenbanknummern nur als Nutzerquelle/Lizenzfund vermerken und nicht als tragenden Ersatz verwenden. |
| `zitat-streitstand-darstellen` | Streitstand in Memo/Schriftsatz darstellen: h. M. (Rechtsprechung BGH + ueberwiegende Literatur), Gegenmeinung (Verfasser + Stellenangabe), eigene Loesung. Format mit klarer Position. |
| `zitat-verboten-anwalt24-beckrs` | Verbotene Zitate vermeiden: anwalt24.de (kein primaerer Rechtsstand), BeckRS allein (interne Beck-Online-ID), 'lawblog'-Eintraege. Speziell bei Schriftsaetzen: Gericht prueft Originalquelle. Empfehlung: immer dejure.org oder Originalents... |
| `zitierweise-aktenzeichen-schriftsatz-brief-memo-bausteine` | Aktenzeichen: Schriftsatz-, Brief- und Memo-Bausteine: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `zitierweise-anwenden` | Wende deutsche juristische Hauszitierweise v4.1 an. Rechtsprechung nur mit Gericht Entscheidungsform Datum Az. Aktenzeichen und verifizierbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate. Literatur nur bei Nutzerq... |
| `zitierweise-anwenden-02` | Zitierweise Anwenden: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `zitierweise-beckrs-zahlen-schwellenwerte-berechnung` | Beckrs: Zahlen, Schwellenwerte und Berechnung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `zitierweise-blindzitate-internationaler-bezug-schnittstellen` | Blindzitate: Internationaler Bezug und Schnittstellen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `zitierweise-datum-behoerden-gerichts-registerweg` | Datum: Behörden-, Gerichts- oder Registerweg: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `zitierweise-de-recht-start-chronologie-fristen` | Kaltstart, Chronologie, Belegmatrix und Fristenampel, ...: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `zitierweise-deutsches-recht-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `zitierweise-deutsches-recht-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `zitierweise-deutsches-recht-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `zitierweise-deutsches-recht-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `zitierweise-deutsches-recht-fristen-und-risikoampel` | Fristen- und Risikoampel: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `zitierweise-deutsches-recht-kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im Zitierweise Deutsches Recht-Plugin. Setzt v4.1 durch: Rechtsprechung nur mit Datum, Aktenzeichen und verifizierbarer Quelle; keine BeckRS-, Kommentar- oder Aufsatz-Blindzitate. Fragt Ziel, Quell... |
| `zitierweise-deutsches-recht-mandantenkommunikation` | Mandantenkommunikation: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `zitierweise-deutsches-recht-output-waehlen` | Output wählen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `zitierweise-deutsches-recht-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `zitierweise-deutsches-recht-redteam-qualitygate` | Red-Team Qualitygate: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `zitierweise-deutsches-recht-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `zitierweise-entscheidungsform-gericht-datum-az` | Entscheidungsform: Risikoampel, Gegenargumente und Verteidigungslinien: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `zitierweise-fristennotiz-naechster-schritt` | Zitierweise: Fristennotiz und nächster Schritt: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `zitierweise-hauszitierweise-tatbestandsmerkmale-beweisfragen` | Hauszitierweise: Tatbestandsmerkmale, Beweisfragen und Beleglage: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `zitierweise-juristische-erstpruefung-rollenklaerung-mandatsziel` | Juristische: Erstprüfung, Rollenklärung und Mandatsziel: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `zitierweise-kommentar-compliance-dokumentation-aktenvermerk` | Kommentar: Compliance-Dokumentation und Aktenvermerk: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `zitierweise-literatur-formular-portal-einreichungslogik` | Literatur: Formular, Portal und Einreichungslogik: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `zitierweise-lizenziertem-mandantenkommunikation` | Lizenziertem: Mandantenkommunikation und Entscheidungsvorlage: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `zitierweise-mandantenkommunikation-redteam-qualitygate` | Mandantenkommunikation, Redteam Qualitygate, Paywallfreie Rechtsprechungsbelege: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `zitierweise-rechtsprechung-fristen-form-zustaendigkeit-rechtsweg` | Rechtsprechung: Fristen, Form, Zuständigkeit und Rechtsweg: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `zitierweise-verifizierbarer-verhandlung-vergleich-eskalation` | Verifizierbarer: Verhandlung, Vergleich und Eskalation: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `zugriff-sonderfall-edge-case` | Zugriff: Sonderfall und Edge-Case-Prüfung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
