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
| `allgemein` | Einstieg, Schnelltriage und Routing: klärt, ob ein Text Zitate erzeugen, glätten, prüfen oder sperren soll. |
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
| `aktenzeichen` | Nutze dies bei Aktenzeichen: Schriftsatz-, Brief- und Memo-Bausteine: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `allgemein` | Einstieg, Schnelltriage und Fallrouting im Zitierweise Deutsches Recht-Plugin. Setzt v4.1 durch: Rechtsprechung nur mit Datum, Aktenzeichen und verifizierbarer Quelle; keine BeckRS-, Kommentar- oder Aufsatz-Blindzitate. Fragt Ziel, Quell... |
| `allgemein-workflow-chronologie-fristen` | Nutze dies bei Allgemein, Chronologie Und Belegmatrix, Fristen Und Risikoampel, ...: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nächsten belastbaren Arbeitsschritt. |
| `anschluss-routing` | Nutze dies zum Einstieg in Anschluss-Routing: klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `aufsatz-interessen` | Nutze dies bei Aufsatz: Mehrparteienkonflikt und Interessenmatrix: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `aufsatz-interessen-beckrs-blindzitate` | Nutze dies bei Aufsatz Mehrparteien Konflikt Und Interessen, Beckrs Zahlen Schwellen Und Berechnung, Blindzitate Internationaler Bezug Und Schnittstellen: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und li... |
| `beckrs` | Nutze dies bei Beckrs: Zahlen, Schwellenwerte und Berechnung: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `blindzitate` | Nutze dies bei Blindzitate: Internationaler Bezug und Schnittstellen: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `chronologie-und-belegmatrix` | Nutze dies bei Chronologie und Belegmatrix: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `datum` | Nutze dies bei Datum: Behörden-, Gerichts- oder Registerweg: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `datum-entscheidungsform-spezial-gericht` | Nutze dies bei Datum Behörden Gericht Und Registerweg, Entscheidungsform Risikoampel Und Gegenargumente, Gericht Dokumentenmatrix Und Lueckenliste: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert d... |
| `dokumente-intake` | Nutze dies für Unterlagen zu Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `einstieg-routing` | Nutze dies zum Einstieg in Einstieg und Routing: klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `entscheidungsform` | Nutze dies bei Entscheidungsform: Risikoampel, Gegenargumente und Verteidigungslinien: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `fristen-und-risikoampel` | Nutze dies bei Fristen- und Risikoampel: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `gericht-dokumentenmatrix-und-lueckenliste` | Nutze dies für Unterlagen zu Gericht: Dokumentenmatrix, Lückenliste und Nachforderung: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `hauszitierweise` | Nutze dies bei Hauszitierweise: Tatbestandsmerkmale, Beweisfragen und Beleglage: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `hauszitierweise-juristische-kommentar` | Nutze dies bei Hauszitierweise Tatbestand Beweis Und Belege, Juristische Erstpruefung Und Mandatsziel, Kommentar Compliance Dokumentation Und Akte: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert d... |
| `juristische` | Nutze dies bei Juristische: Erstprüfung, Rollenklärung und Mandatsziel: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `kommentar` | Nutze dies bei Kommentar: Compliance-Dokumentation und Aktenvermerk: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `literatur` | Nutze dies bei Literatur: Formular, Portal und Einreichungslogik: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `literatur-live-beweislast-lizenziertem` | Nutze dies bei Literatur Formular Portal Und Einreichung, Live Beweislast Und Darlegungslast, Lizenziertem Mandantenkommunikation Entscheidungsvorlage: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefe... |
| `live-beweislast-darlegungslast` | Nutze dies bei Live: Beweislast, Darlegungslast und Substantiierung: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `lizenziertem` | Nutze dies bei Lizenziertem: Mandantenkommunikation und Entscheidungsvorlage: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `mandantenkommunikation` | Nutze dies bei Mandantenkommunikation: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `nutzerquelle-fehlerkatalog` | Nutze dies als Fehlerbremse bei Nutzerquelle Fehlerkatalog: prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `output-waehlen` | Nutze dies bei Output wählen: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `paywallfreie` | Nutze dies bei Mandantenkommunikation, Redteam Qualitygate, Paywallfreie Rechtsprechungsbelege: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nächsten belastbaren Arbeitsschritt. |
| `paywallfreie-rechtsprechungsbelege` | Paywallfreie, prüfbare Rechtsprechungsbelege ohne Blindzitate: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `quelle-quellenkarte` | Nutze dies zur Quellenprüfung bei Quelle Quellenkarte: Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `quellen-livecheck` | Nutze dies zur Quellenprüfung bei Rechtsquellen-Livecheck: Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `rechtsprechung` | Nutze dies bei Rechtsprechung: Fristen, Form, Zuständigkeit und Rechtsweg: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `rechtsprechung-zit-rechtsprechungszitierung` | Nutze dies bei Rechtsprechung Fristen Form Und Zustaendigkeit, Zit Rechtsprechungszitierung Leitfaden, Zitat Eugh Rechtsprechung: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nächsten belast... |
| `redteam-qualitygate` | Nutze dies als Fehlerbremse bei Red-Team Qualitygate: prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `unterlagen-luecken` | Nutze dies für Unterlagen zu Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `verifizierbarer` | Nutze dies bei Verifizierbarer: Verhandlung, Vergleich und Eskalation: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `verifizierbarer-zugriff-sonderfall-zit` | Nutze dies bei Verifizierbarer Verhandlung Vergleich Und Eskalation, Zugriff Sonderfall Und Edge Case, Zit Gesetzeszitierung Bauleiter: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nächsten... |
| `zit-gesetzeszitierung-bauleiter` | Bauleiter Gesetzeszitierung in Schriftsatz und Memo: Norm, Absatz, Satz, Halbsatz, Nummer, Buchstabe. Pruefraster fuer einheitliche Schreibweise. |
| `zit-internationale-urteile-spezial` | Spezialfall Zitierung internationaler Urteile EuGH EGMR sowie Common-Law-Urteile: ECLI, Neutral Citation, Public Domain. Pruefraster fuer internationale Mandate. |
| `zit-internationale-zit-kommentar-zitat` | Nutze dies bei Zit Internationale Urteile Spezial, Zit Kommentar Aufsatzzitierung Spezial, Zitat Amtliche Sammlung Vs Zeitschrift: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nächsten belas... |
| `zit-kommentar-aufsatzzitierung-spezial` | Spezialfall Kommentar- und Aufsatzzitierung: Bearbeiter, Randnummer, Auflagenjahr, Zeitschrift, Heft, Seite. Pruefraster fuer wissenschaftliches Schreiben. |
| `zit-rechtsprechungszitierung-leitfaden` | Leitfaden Rechtsprechungszitierung BGH BVerfG EuGH: Gericht, Entscheidungsform, Datum, Aktenzeichen, frei pruefbarer Link dejure.org / openjur.de. Pruefraster fuer Memos. |
| `zitat-amtliche-sammlung-vs-zeitschrift` | Amtliche Sammlung vs. Zeitschrift: Reihenfolge der Fundstellen. Amtliche Sammlung (BGHZ, BVerfGE) hat Vorrang, dann Parallelfundstelle Zeitschrift (NJW, JZ, ZIP). Beispiel BGHZ 240 S. 1 = NJW 2024 S. 1832. |
| `zitat-archivierungspflicht` | Archivierungspflicht der zitierten Quelle: Screenshot mit Datum, PDF-Abruf, archive.org-Backup. Wichtig bei Schriftsaetzen, weil Online-Quellen veraendert werden. Empfehlung Kanzleiprozess. |
| `zitat-archivierungspflicht-aufsatz` | Nutze dies bei Zitat Archivierungspflicht, Zitat Aufsatz Zeitschrift, Zitat Bag Bfh Bsg Bag: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nächsten belastbaren Arbeitsschritt. |
| `zitat-aufsatz-zeitschrift` | Aufsatz in juristischer Zeitschrift nur bei vorliegendem Beitrag zitieren: Verfasser, Titel, Zeitschrift, Jahr, Heft/Seite und Pinpoint aus Nutzerquelle oder Live-Zugriff übernehmen. Keine Aufsatzfundstellen aus Modellwissen. |
| `zitat-bag-bfh-bsg-bag` | Fachgerichtsbarkeit zitieren: BAG, BFH, BSG, BVerwG, BGH. Format Senat, Datum, Aktenzeichen, amtliche Sammlung sowie Parallel-Fundstelle. Beispiel BAG, Urt. v. 12.09.2023 9 AZR 372 aus 22, BAGE 178 S. 199 = NZA 2023 S. 1521. |
| `zitat-bgh-entscheidung` | BGH-Entscheidung korrekt zitieren: Senat, Datum, Aktenzeichen, Fundstelle. Beispiel BGH, Urt. v. 11.04.2024 III ZR 168 aus 23, BGHZ 240 S. 1 = NJW 2024 S. 1832. Bei wichtiger Linie: Vor- und Folgeentscheidungen ergaenzen. |
| `zitat-bgh-entscheidung-bverfg-gesetz` | Nutze dies bei Zitat Bgh Entscheidung, Zitat Bverfg Entscheidung, Zitat Gesetz Verordnung: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nächsten belastbaren Arbeitsschritt. |
| `zitat-bverfg-entscheidung` | BVerfG-Entscheidung zitieren: Senatsnummer, Datum, Aktenzeichen, BVerfGE, ggf. Kammerbeschluss. BVerfGE-Band und Seitenzahl nur übernehmen, wenn sie amtlich oder frei verifizierbar sind; andernfalls mit Gericht, Entscheidungsform, Datum... |
| `zitat-eugh-rechtsprechung` | EuGH-Rechtsprechung zitieren: Urt./Beschl., Datum, Rs. C-Nummer, Parteinamen, ECLI. Beispiel EuGH, Urt. v. 04.07.2019 - C-377/17, Kommission/Deutschland, ECLI:EU:C:2019:562. Bei Generalanwalts-Schlussantraegen: GA-Anfang. |
| `zitat-gesetz-verordnung` | Gesetz/Verordnung zitieren: Norm-Bezeichnung, ggf. § und Absatz. Beispiel § 17 InsO, § 311 Abs. 2 BGB, Art. 26 DSGVO. Bei zeitlicher Bezugnahme: § X i. d. F. v. JJJJ. |
| `zitat-haus-zitierregel-anpassen` | Kanzlei-Hauszitierweise anpassen: Excel-Vorlage Beck/NJW vs. Hartung/Roemermann v4. Empfehlung: konsistente Regel pro Kanzlei, in den Schriftsatz-Templates verankern. Output: Hauszitierregel-Dokument. |
| `zitat-haus-zitierregel-instanzgerichte` | Nutze dies bei Zitat Haus Zitierregel Anpassen, Zitat Instanzgerichte Strategisch, Zitat Internationale Quellen: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nächsten belastbaren Arbeitsschr... |
| `zitat-instanzgerichte-strategisch` | Instanzgerichts-Entscheidungen strategisch zitieren: OLG-Entscheidungen, LG-Entscheidungen. Wann sinnvoll: Tendenzen, Lokal-Linien, Fehlen BGH-Rechtsprechung. Vermeiden: AG-Entscheidungen ausser bei sehr engen Fragen. |
| `zitat-internationale-quellen` | Internationale Quellen: EuGH, EGMR, Common-Law-Faelle (in IPR-Kontext). Format mit ECLI bzw. Neutral Citation. Beispiel EGMR, Urt. v. 23.01.2024 - Nr. 12345/22, ECLI:CE:ECHR:2024:0123JUD001234522. |
| `zitat-internet-quellen` | Internet-Quellen zitieren: Stand, URL, Abrufdatum. Bevorzugt: dejure.org, openjur.de, bundesgerichtshof.de, bundesverfassungsgericht.de, eur-lex. Vermeiden: anwalt24.de, BeckRS allein als einzige Fundstelle. |
| `zitat-internet-quellen-kommentar-randnummer` | Nutze dies bei Zitat Internet Quellen, Zitat Kommentar Randnummer, Zitat Leitsatzentscheidung: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nächsten belastbaren Arbeitsschritt. |
| `zitat-kommentar-randnummer` | Kommentar mit Bearbeiter und Randnummer nur bei vorliegender Nutzerquelle oder lizenziertem Live-Zugriff zitieren: Bearbeiter, Werk, aktuelle Auflage/Stand, Norm, Randnummer. Keine Kommentar-Rn. aus Modellwissen. |
| `zitat-leitsatzentscheidung` | Leitsatz-Entscheidung mit Leitsatz zitieren: BGH, Urt. ..., Leitsatz 1 lautet: ... Original-Leitsatz im Wortlaut, dann Begruendung mit Rn. Format fuer Schriftsatz und Memo. |
| `zitat-monografie-handbuch` | Monografie oder Handbuch nur bei vorliegender Quelle zitieren: Verfasser/Bearbeiter, Titel, Auflage/Stand, Jahr, Kapitel/Norm, Seite/Rn. Keine Handbuchfundstellen aus Modellwissen. |
| `zitat-monografie-handbuch-streitstand` | Nutze dies bei Zitat Monografie Handbuch, Zitat Streitstand Darstellen, Zitat Verboten Anwalt24 Beckrs: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nächsten belastbaren Arbeitsschritt. |
| `zitat-rechtsprechung-fristennotiz-naechster` | Nutze dies bei Zitat Rechtsprechung Ohne Fundstelle, Zitierweise Fristennotiz Und Naechster Schritt, Aktenzeichen Schriftsatz Brief Und Memo Bausteine: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefe... |
| `zitat-rechtsprechung-ohne-fundstelle` | Rechtsprechung ohne amtliche/freie Fundstelle behandeln: Gericht Datum Aktenzeichen sichern, freie Quelle suchen, Datenbanknummern nur als Nutzerquelle/Lizenzfund vermerken und nicht als tragenden Ersatz verwenden. |
| `zitat-streitstand-darstellen` | Streitstand in Memo/Schriftsatz darstellen: h. M. (Rechtsprechung BGH + ueberwiegende Literatur), Gegenmeinung (Verfasser + Stellenangabe), eigene Loesung. Format mit klarer Position. |
| `zitat-verboten-anwalt24-beckrs` | Verbotene Zitate vermeiden: anwalt24.de (kein primaerer Rechtsstand), BeckRS allein (interne Beck-Online-ID), 'lawblog'-Eintraege. Speziell bei Schriftsaetzen: Gericht prueft Originalquelle. Empfehlung: immer dejure.org oder Originalents... |
| `zitierweise` | Nutze dies bei Zitierweise Anwenden: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nächsten belastbaren Arbeitsschritt. |
| `zitierweise-anwenden` | Wende deutsche juristische Hauszitierweise v4.1 an. Rechtsprechung nur mit Gericht Entscheidungsform Datum Az. Aktenzeichen und verifizierbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate. Literatur nur bei Nutzerq... |
| `zitierweise-fristennotiz-naechster-schritt` | Nutze dies bei Zitierweise: Fristennotiz und nächster Schritt: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `zugriff-sonderfall-edge-case` | Nutze dies bei Zugriff: Sonderfall und Edge-Case-Prüfung: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
