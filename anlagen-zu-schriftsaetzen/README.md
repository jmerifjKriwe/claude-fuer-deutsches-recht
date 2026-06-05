# Anlagen zu Schriftsätzen

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`anlagen-zu-schriftsaetzen`) | [`anlagen-zu-schriftsaetzen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/anlagen-zu-schriftsaetzen.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Werkmann ./. K+B — Werklohnklage Lackieranlage Eschweiler — Anlagenkonvolut-Verfahren** (`anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler`) | [Gesamt-PDF lesen](../testakten/anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler/gesamt-pdf/anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler_gesamt.pdf) | [`testakte-anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin ist die Anlagenkanzlei im Kleinen: Es nimmt einen Schriftsatz, einen chaotischen Mandantenordner oder ein schon halb nummeriertes Anlagenpaket und macht daraus eine nachvollziehbare, gerichtstaugliche Anlagenstruktur.

Es hilft besonders dann, wenn nicht einfach „Anlage K1 bis K12“ vorliegt, sondern wenn eine echte Akte lebt: E-Mails mit Anhängen, Scans ohne OCR, Excel-Tabellen, Fotos, Chat-Screenshots, mehrere Vertragsfassungen, fremdsprachige Unterlagen, doppelte Dateien, geschwärzte Drittunterlagen, beA-Grenzen, Verfahrenswechsel und Richterhinweise. Das Plugin führt dann nicht nur eine Nummerierung aus, sondern baut eine Arbeitslogik: Welche Tatsache soll durch welche Anlage belegt werden? Welche Datei gehört wirklich zu K1? Welche Unterlagen sind nur Konvolutbestandteil? Welche Anlage ist zu groß, unleserlich, falsch benannt, doppelt oder im Schriftsatz nicht eingeführt?

## Wofür es gedacht ist

| Situation | Was das Plugin macht | Ergebnis |
| --- | --- | --- |
| Klage/Replik liegt vor, Anlagen sind noch ungeordnet | Schriftsatz lesen, Beweisanker erkennen, K-Nummern vorschlagen, Dateien zuordnen | K1/K2/K3-Reihenfolge, Anlagenverzeichnis, Lückenliste |
| Anlagen sind schon nummeriert, aber niemand traut dem Paket | Prüfmodus: Nummern, Zitate, Dateien, Stempel, Namen, Lesbarkeit und beA-Fähigkeit prüfen | Fehlerprotokoll mit Korrekturplan |
| Mandant liefert Datenraum/ZIP/USB-Stick | Duplikate, Fassungen, Hashes, Dateitypen, Zeitfolge und Relevanz sortieren | Belegmatrix und Nachforderungsliste |
| Eine Anlage ist ein Konvolut | Deckblatt, Untergliederung, interne Seiten-/Dokumentlogik, kurze Erläuterung für Gericht | `Anlage K1` mit `K1.1`, `K1.2`, `K1.3` |
| Elektronische Einreichung steht bevor | Dateinamen, PDF/OCR, Paketgrößen, Anlagenverzeichnis, Prüfvermerk | beA-/ERV-taugliches Versandpaket |

## Der K1-Gedanke

Die erste Anlage ist fast nie nur eine Datei. In großen Verfahren ist `K1` häufig der Orientierungspunkt für das Gericht: Vertrag, Auftrag, Rahmenvereinbarung, Nachtrag, Bestätigungsmail, Protokoll oder Dokumentenfamilie. Das Plugin behandelt `K1` deshalb als Sortierproblem:

1. **Was soll K1 beweisen?** Nicht „alles zum Vertrag“, sondern eine konkrete Tatsache.
2. **Ist K1 Einzelanlage oder Konvolut?** Bei Konvolut: Deckblatt, Reihenfolge, interne Kurzbezeichnungen.
3. **Welche Fassungen gibt es?** Entwurf, unterschriebene Fassung, Scan, OCR-PDF, E-Mail-Anhang, spätere Ergänzung.
4. **Welche Datei ist die gerichtliche Fassung?** Die anderen Fassungen wandern in den internen Hash-/Versionenlog.
5. **Wie wird K1 im Schriftsatz eingeführt?** Der Schriftsatz muss den Tatsachenkern selbst tragen; die Anlage belegt ihn nur.

## Drei Arbeitsmodi

**Auto-Benennung:** Der Schriftsatz enthält noch keine Nummern. Das Plugin liest die Beweisstellen und schlägt die Reihenfolge vor.

**Schriftsatz folgt:** Der Schriftsatz enthält bereits `Anlage K...`-Verweise. Das Plugin sucht die passenden Dateien, erkennt Lücken und meldet Überschüsse.

**Prüfmodus:** Ein fertiges Anlagenpaket wird gegengeprüft: `K7` fehlt, `K12` ist doppelt, `K18` wird im Schriftsatz nie erwähnt, `K23` hat keinen OCR-Text, `K31` enthält ungeschwärzte Drittinformationen.

## Typische Outputs

- Anlagenverzeichnis für Gericht und Kanzleiakte.
- K/B/AST/AG-Nummerierung mit eindeutiger Dateinamenkonvention.
- Konvolutdeckblätter für Sammelanlagen.
- Belegmatrix: Tatsachenbehauptung ↔ Schriftsatzstelle ↔ Anlage ↔ Datei ↔ Status.
- Hash-/Duplikat-/Fassungslog für interne Kontrolle.
- beA-Versandliste mit Paketgrößen, Dateinamen und letzten Prüfpunkten.
- Nachforderungsliste an Mandant oder Sachbearbeitung.
- Berichtigungs- oder Nachreichungsplan nach gerichtlichem Hinweis.

## Wichtig

Anlagen ersetzen keinen Tatsachenvortrag. Wenn eine Behauptung entscheidungserheblich ist, muss sie im Schriftsatz stehen. Die Anlage belegt, erläutert oder vertieft; sie darf nicht der Ort sein, an dem der eigentliche Vortrag versteckt wird.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Besonders wichtige Skills

| Skill | Zweck |
| --- | --- |
| `allgemein` | Kaltstart, Triage, Nummernkreis, Ziel-Schriftsatz, K1-Frage und Routing in die passenden Spezial-Skills. |
| `anlagen-zu-schriftsaetzen` | Hauptworkflow für Auto-Benennung, Schriftsatz-folgt-Modus, Prüfmodus und Reparatur nach Hinweis. |
| `k1-sortierwerkstatt` | Baut aus Vertrag, Nachtrag, Mail, Scan und OCR-Fassung eine klare Leit-Anlage `K1` oder ein K1-Konvolut. |
| `schriftsatz-anlagen-mapping` | Verknüpft Tatsachenvortrag, Schriftsatzstelle, Beweisangebot, Anlage und Datei in einer Belegmatrix. |
| `anlagen-duplikate-versionen-hashlog` | Erkennt Dubletten, Versionen, OCR-Kopien und die maßgebliche gerichtliche Fassung. |
| `bea-paketierung-groessen-und-versandplan` | Plant Dateinamen, Paketgrößen, Teilpakete, Begleitvermerk und Eingangskontrolle. |
| `anlagen-qualitygate-finalcheck` | Letzter strenger Check vor Versand: Nummern, Zitate, Dateien, OCR, Schwärzung, Stempel, Paket. |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 97 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Anlagen Zu Schriftsaetzen-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbei... |
| `anlage-red-anlagen-anlagenkonvolut-sonderfall-arial` | Spezial Anlage Red Team Und Qualitaetskontrolle, Spezial Anlagen Tatbestand Beweis Und Belege, Spezial Anlagenkonvolut Sonderfall Und Edge Case, Spezial Arial Mandantenkommunikation Entscheidungsvorlage: Spezial Anlage Red Team Und Quali... |
| `anlagen-an-assistenz-uebersetzungspflicht-vorlagepflicht-zpo` | Anlagen Übergabe An Assistenz Und Legal Tech, Anlagen Uebersetzungspflicht, Anlagen Vorlagepflicht 141 Zpo, Anlagen Zur Substantiierung Pflicht: Anlagen Übergabe An Assistenz Und Legal Tech; Anlagen Uebersetzungspflicht; Anlagen Vorlagep... |
| `anlagen-aus-datenraum-und-sharepoint` | Überführt Datenraum-/SharePoint-/DMS-Exporte in Anlagenlogik: Pfade, Versionen, Berechtigungen, Exportzeitpunkt, Index und gerichtliche Fassung. |
| `anlagen-aus-edv-systemen` | Anlagen aus IT-Systemen (ERP-Auszuege, Datenbankexporte, Logdateien): Beweiskraft, Manipulationsschutz, Hashverfahren, Begleitvermerk Erstellung. Empfehlung: Export mit Zeitstempel, Hashprotokoll, ggf. Sachverstaendigenanhoerung Authenti... |
| `anlagen-aus-mandantenmaterial` | Mandantenmaterial in Anlagen umwandeln: Posteingang, E-Mails, PDFs, Vertraege, Rechnungen, Korrespondenz. Markiert geschwaerzte Stellen, prueft Vollstaendigkeit, schlaegt sinnvolle Kuerzungen vor. Erkennt vertrauliche Inhalte, die fuer d... |
| `anlagen-bei-berufung-revision` | Anlagen in Berufung und Revision: bisheriges Anlagenverzeichnis uebernehmen oder neu nummerieren? Empfehlung: Berufungsklaegeranlagen als BK1, BK2 ..., Berufungsbeklagter BB1, BB2 ... Revisionsanlagen sind ueblich nur ergaenzend; Schwerp... |
| `anlagen-bei-eilantrag-eu-arrest` | Anlagen fuer einstweilige Verfuegung und Arrest: Glaubhaftmachung § 294 ZPO durch Anlagen, eidesstattliche Versicherung als Anlage, parate Beweismittel. Hohe Anforderungen Vollstaendigkeit. Output Standard-Anlagensatz fuer wettbewerbsrec... |
| `anlagen-berufung-revision-eilantrag-eu-bilder-screenshots` | Anlagen Bei Berufung Revision, Anlagen Bei Eilantrag Eu Arrest, Anlagen Bilder Screenshots, Anlagen Duplikate Versionen Hashlog: Anlagen Bei Berufung Revision; Anlagen Bei Eilantrag Eu Arrest; Anlagen Bilder Screenshots; Anlagen Duplikat... |
| `anlagen-bilder-screenshots` | Bilder und Screenshots als Anlagen: Beweiskraft, Manipulationsanfaelligkeit, EXIF-Daten, Metadaten. Empfehlung: Original und Vergroesserung beifuegen, EXIF-Export anhaengen, Standortdaten transparent machen. Bei Screenshots: voller Brows... |
| `anlagen-check-zustellung-redaktion-dsgvo-schwaerzen-stempel` | Anlagen Quality Check Vor Zustellung, Anlagen Redaktion Dsgvo Geschgehg, Anlagen Schwaerzen Anonymisieren, Anlagen Stempel Und Deckblattlogik: Anlagen Quality Check Vor Zustellung; Anlagen Redaktion Dsgvo Geschgehg; Anlagen Schwaerzen An... |
| `anlagen-duplikate-versionen-hashlog` | Erkennt doppelte Dateien, verschiedene Fassungen desselben Dokuments, OCR-Kopien, E-Mail-Anhänge und manipulativ wirkende Metadatenbrüche; erzeugt ein Hash- und Versionenprotokoll. |
| `anlagen-elektronische-dokumente-format-dateinamen-bea-versand` | Anlagen Elektronische Dokumente Spezial, Anlagen Format Und Dateinamen, Anlagen Für Bea Versand, Anlagen Für Glaubhaftmachung: Anlagen Elektronische Dokumente Spezial; Anlagen Format Und Dateinamen; Anlagen Für Bea Versand; Anlagen Für G... |
| `anlagen-elektronische-dokumente-spezial` | Spezialfall elektronische Dokumente als Anlage: ERVV-Vorgaben, qualifizierte elektronische Signatur, Datei-Format-Whitelist nach ERVV, maximale Groesse, beA-Vorgaben, Container-PDF. Pruefraster und Mustertexte fuer Eingang bei Gericht. |
| `anlagen-format-und-dateinamen` | Format und Dateinamen fuer Anlagen: K-01_2024-03-12_Mietvertrag.pdf. Maschinenlesbar, sortierbar, beA-kompatibel. Maximal 3 Ebenen Unterordner, keine Sonderzeichen, keine Umlaute in Dateinamen, durchgehend kleingeschrieben. |
| `anlagen-fuer-bea-versand` | Anlagen fuer beA-Versand vorbereiten: PDF/A-konform, max. zulaessige Dateigroesse beachten, OCR ueber Scans laufen lassen, korrekt strukturiertes XJustiz-Begleitformular. Liste der Anlagen pro Schriftsatz mit Pruefsumme. Verhindert wiede... |
| `anlagen-fuer-glaubhaftmachung` | Spezialworkflow für Eilverfahren: Anlagen, eidesstattliche Versicherung, Screenshots, E-Mails, Fotos und Glaubhaftmachungsdichte nach § 294 ZPO ordnen. |
| `anlagen-haftpflicht-versicherer` | Anlagen-Pflicht gegenueber Haftpflichtversicherer (Berufshaftpflicht, Hausratversicherung, KFZ): welche Anlagen muessen mit Schadenanzeige eingereicht werden, was der Versicherer im Regulierungsverfahren erwartet. Pruefraster aus § 31 VV... |
| `anlagen-konvention-k-b-erlaeutert` | Konvention erklaert und korrekt eingesetzt: K-Anlagen Klaeger, B-Anlagen Beklagter, ZN-Anlagen Zeugen, GA-Anlagen Gutachten, AS-Anlagen Anlagenband. Wann Klein-/Grosschreibung, wann Bindestrich. Wechselt sauber, wenn der Mandant im Vorpr... |
| `anlagen-konvention-mandantenfreundlich` | Anlagen-Konvention mandantenfreundlich: durchlaufende Nummerierung K1 / K2 / K3 ff. fuer Klaegerseite, B1 / B2 / B3 ff. fuer Beklagtenseite, Anlagenbaender, Inhaltsverzeichnis, beA-konforme PDF-Bezeichnung. Mustertext fuer Anlagenverzeic... |
| `anlagen-prozessual-pruefung-spezial` | Spezialfall prozessuale Anlagenpruefung: keine Substantiierung durch blossen Anlagenverweis (BGH-Linie), eigener Vortrag noch im Schriftsatz erforderlich, Tatsachenkern aus Anlage in den Text uebernehmen. Pruefraster und Korrektur-Bauste... |
| `anlagen-quality-check-vor-zustellung` | Quality-Check fuer Anlagenpaket vor Zustellung: Vollstaendigkeit (alle Bezuege im Schriftsatz haben passende Anlage), Lesbarkeit (OCR, kein Schwarzbalken), Schwaerzung (DSGVO und Mandantengeheimnisse), Format (PDF/A wo gefordert). Pruefl... |
| `anlagen-qualitygate-finalcheck` | Finaler Red-Team-Check vor Einreichung: Nummern, Schriftsatzverweise, Dateien, Stempel, OCR, Schwärzung, Dateinamen, beA-Paket, Lücken und Begleitvermerk. |
| `anlagen-redaktion-dsgvo-geschgehg` | Prüft Anlagen vor Einreichung auf personenbezogene Daten, Geschäftsgeheimnisse, Drittmandate, Schwärzungsbedarf und Redaktionsprotokoll. |
| `anlagen-schwaerzen-anonymisieren` | Anlagen schwaerzen und anonymisieren: personenbezogene Daten unbeteiligter Dritter (Mitarbeiter, Kunden, Patienten) entfernen, Kontonummern bis auf letzte 3 Ziffern schwaerzen, Geburtsdaten redigieren, soweit nicht streitrelevant. Mat2-... |
| `anlagen-stempel-und-deckblattlogik` | Legt fest, wie Anlagenstempel, Konvolutdeckblätter, Unteranlagen und Seiten-/Dokumentbezeichnungen aussehen müssen, damit Gericht und Gegner nicht suchen müssen. |
| `anlagen-uebergabe-an-assistenz-und-legal-tech` | Erzeugt klare Arbeitsanweisungen für Kanzleiteam, Assistenz, Legal Tech oder externen Dienstleister: was umbenennen, scannen, stempeln, schwärzen, prüfen. |
| `anlagen-uebersetzungspflicht` | Fremdsprachige Anlagen: Uebersetzungspflicht § 184 GVG. Beglaubigte oder einfache Uebersetzung? Gericht kann Uebersetzung verlangen oder Ablehnung der Beruecksichtigung androhen. Empfehlung: bei zentralen Urkunden beglaubigte Uebersetzun... |
| `anlagen-vorlagepflicht-141-zpo` | Anordnung der Urkundenvorlage nach § 142 ZPO und § 421 ZPO: wann kann das Gericht die Vorlage einer Urkunde anordnen, wann hat ein Beweisfuehrer Anspruch auf Vorlage durch den Gegner. Pruefraster, Antragsformulierung und Folgen Nichtvorl... |
| `anlagen-zu-schriftsaetzen` | Anwalt hat Schriftsatz fertig und muss Anlagen korrekt benennen nummerieren und als PDF-Konvolut aufbereiten. Anlagemanagement gerichtliche Schriftsaetze. Prüfraster: Schriftsatz lesen Beweisstuecke erkennen sortieren beA-konforme Benenn... |
| `anlagen-zur-substantiierung-pflicht` | Anlagen ersetzen keine Substantiierung im Schriftsatz: 'wegen der weiteren Einzelheiten wird auf Anlage K5 verwiesen' ist nicht ausreichend (BGH X ZR 39/16). Pruefraster: Welche Behauptung wird substanziiert, welche durch Anlage nur bele... |
| `anlagenband-strukturieren` | Anlagenband strukturieren: Trennblaetter, Inhaltsverzeichnis, Reihenfolge nach Schriftsatzbezug, durchgehende Foliierung. Anweisung fuer Kanzleimitarbeiter zur physischen oder elektronischen Erstellung. Fuer beA-Versand zusaetzlich ein d... |
| `anlagenband-strukturieren-anlagenbezug-anlagenkonvolut` | Anlagenband Strukturieren, Anlagenbezug Im Schriftsatz, Anlagenkonvolut Konsolidieren, Anlagenmatrix Csv Xlsx Aufbau: Anlagenband Strukturieren; Anlagenbezug Im Schriftsatz; Anlagenkonvolut Konsolidieren; Anlagenmatrix Csv Xlsx Aufbau. F... |
| `anlagenbezug-im-schriftsatz` | Wie Anlagen im Schriftsatz richtig eingefuehrt werden: 'Beweis: Vorlage der Anlage K1' oder 'wie sich aus Anlage K3 ergibt'. Erste Erwaehnung mit Kurztitel und Datum, danach nur K1, K2 ... Vermeidet sprachliche Fehler bei mehrfachem Bezug. |
| `anlagenkonvolut-konsolidieren` | Anlagenkonvolut aus Mandanten-ZIP konsolidieren: Duplikate ueber Hashvergleich erkennen, gleiche Vertraege in unterschiedlichen Fassungen identifizieren, sortieren nach Datum und Thema, Lueckenanalyse (welcher Vertrag wird im Schriftsatz... |
| `anlagenmatrix-csv-xlsx-aufbau` | Entwirft eine robuste Anlagenmatrix für große Verfahren mit Dok-ID, Nummernkreisen, Schriftsatzstelle, Beweiszweck, Quelle, Hash, Status, Datenschutz und Nachreichung. |
| `anlagenverzeichnis-gericht-kanzlei-und-intern` | Erstellt getrennte Anlagenverzeichnisse: schlank für Gericht, ausführlicher für Kanzlei und technisch mit Dateipfad, Hash, Quelle und Bearbeitungsstatus. |
| `anlagenverzeichnis-grundaufbau` | Anlagenverzeichnis nach deutscher Anwaltsuebung aufbauen: K1, K2, K3 ... fuer Klaegerseite, B1, B2 ... fuer Beklagtenseite. Kurztitel, Datum, Funktion (Beweismittel zu welcher Behauptung), Fundstelle im Schriftsatz. Loest Doppel-Nummerie... |
| `anlagenverzeichnis-kanzlei-grundaufbau-bea-paketierung-berufung` | Anlagenverzeichnis Gericht Kanzlei Und Intern, Anlagenverzeichnis Grundaufbau, Bea Paketierung Groessen Und Versandplan, Berufung Beschwerde Und Neue Anlagen: Anlagenverzeichnis Gericht Kanzlei Und Intern; Anlagenverzeichnis Grundaufbau;... |
| `baut-beweislast-benennt-bereits-excel` | Spezial Baut Beweislast Und Darlegungslast, Spezial Benennt Compliance Dokumentation Und Akte, Spezial Bereits Abschlussprodukt Und Übergabe, Spezial Excel Schriftsatz Brief Und Memo Bausteine: Spezial Baut Beweislast Und Darlegungslast;... |
| `bea-paketierung-groessen-und-versandplan` | Plant elektronische Anlagenpakete für beA/ERV: Dateinamen, Reihenfolge, Paketgrößen, PDF/OCR, Nachsendungen, Begleitvermerk und finaler Versandcheck. |
| `berufung-beschwerde-und-neue-anlagen` | Prüft Anlagen in Rechtsmittelverfahren: Übernahme alter Nummern, neue Anlagen, § 531 ZPO-Risiken, Verweis auf Vorinstanz und Synchronisation. |
| `beweisangebot-anlage-emails-chats-excel-tabellen-fremdsprachige` | Beweisangebot Anlage Zeugen, Emails Chats Screenshots Als Anlagen, Excel Tabellen Und Zahlenbeweis, Fremdsprachige Anlagen Uebersetzung: Beweisangebot Anlage Zeugen; Emails Chats Screenshots Als Anlagen; Excel Tabellen Und Zahlenbeweis;... |
| `beweisangebot-anlage-zeugen` | Zeugenbeweis korrekt ueber Anlagen unterstuetzen: schriftliche Zeugenaussagen sind keine Anlagen-Beweismittel im Strengbeweis, koennen aber als praeprozessuale Information dienen. Anlagen, die die Glaubhaftigkeit stuetzen (Chatverlauf, E... |
| `emails-chats-screenshots-als-anlagen` | Macht aus EML/MSG, Chatverläufen und Screenshots gerichtstaugliche Anlagen mit Headern, Kontext, Exportlogik, Vollständigkeitswarnung und Beweiszweck. |
| `excel-tabellen-und-zahlenbeweis` | Bereitet XLSX/CSV als Anlage auf: Ausdruck, Summenlogik, Formelrisiko, Quelldaten, Rechenweg, PDF-Fassung und Anlagenbezug im Schriftsatz. |
| `fremdsprachige-anlagen-uebersetzung` | Prüft fremdsprachige Anlagen: Relevanz, Übersetzungsbedarf, beglaubigte oder Arbeitsübersetzung, Auszug statt Vollübersetzung, Kosten und Schriftsatzanker. |
| `frist-und-eilversand-anlagenpaket` | Minimalpfad bei drohender Frist: welche Anlagen müssen jetzt mit, welche können nachgereicht, welche Risiken müssen im Schriftsatz offen gehalten werden. |
| `haftpflicht-versicherer-konvention-k-konvention` | Anlagen Haftpflicht Versicherer, Anlagen Konvention K B Erlaeutert, Anlagen Konvention Mandantenfreundlich, Anlagen Prozessual Prüfung Spezial: Anlagen Haftpflicht Versicherer; Anlagen Konvention K B Erlaeutert; Anlagen Konvention Mandan... |
| `k1-anlagenpaket-aus-chaosordner` | Aus einem Mandantenordner mit beliebigen Dateinamen die erste Anlagenstaffel K1 bis K20 bilden: priorisieren, umbenennen, Lücken markieren, Rückfragen ausgeben. |
| `k1-anlagenpaket-k1-sortierwerkstatt-massenanlagen-sampling` | K1 Anlagenpaket Aus Chaosordner, K1 Sortierwerkstatt, Massenanlagen Sampling Und Repraesentativitaet, Mehrparteien Rollen Und Praefixe: K1 Anlagenpaket Aus Chaosordner; K1 Sortierwerkstatt; Massenanlagen Sampling Und Repraesentativitaet;... |
| `k1-sortierwerkstatt` | K1-Leitanlage sortieren: Vertrag, Auftrag, Nachtrag, E-Mail-Anhang, Scan, OCR-Fassung und spätere Ergänzungen zu einer gerichtstauglichen Anlage K1 oder einem K1-Konvolut ordnen. |
| `konform-interessen-konvertiert-oben-schriftsaetzen` | Spezial Konform Mehrparteien Konflikt Und Interessen, Spezial Konvertiert Zahlen Schwellen Und Berechnung, Spezial Oben Formular Portal Und Einreichung, Spezial Schriftsaetzen Dokumentenmatrix Und Lueckenliste: Spezial Konform Mehrpartei... |
| `massenanlagen-sampling-und-repraesentativitaet` | Hilft bei Tausenden gleichartiger Dokumente: Auswahl, repräsentative Beispiele, Nachreichungsvorbehalt, Anlagenband und Substantiierungsgrenze. |
| `mehrparteien-rollen-und-praefixe` | Entwirft Nummernkreise bei Streitgenossen, Nebenintervention, Widerklage, Drittwiderklage, selbständigem Beweisverfahren und parallelen Verfahren. |
| `nachreichung-berichtigung-ocr-scan-original-abschrift-anlagen` | Nachreichung Berichtigung Und Gerichtshinweis, Ocr Scan Lesbarkeit Und Beweiswert, Original Abschrift Kopie Und Elektronische Fassung, Schriftsatz Anlagen Mapping: Nachreichung Berichtigung Und Gerichtshinweis; Ocr Scan Lesbarkeit Und Be... |
| `nachreichung-berichtigung-und-gerichtshinweis` | Plant die Reparatur eines Anlagenpakets nach gerichtlichem Hinweis, Rüge der Gegenseite, falscher Anlage, fehlender Datei oder versehentlicher Einreichung. |
| `ocr-scan-lesbarkeit-und-beweiswert` | Prüft gescannte Anlagen auf Lesbarkeit, OCR-Durchsuchbarkeit, Seitenreihenfolge, abgeschnittene Ränder, schiefe Scans und Beweiswertprobleme. |
| `original-abschrift-kopie-und-elektronische-fassung` | Klären, wann Original, beglaubigte Abschrift, einfache Kopie, Scan, elektronisches Dokument oder Ausdruck als Anlage sinnvoll oder erforderlich ist. |
| `pruefmodus-fristennotiz-datenraum-sharepoint-edv-systemen` | Spezial Pruefmodus Fristennotiz Und Naechster Schritt, Anlagen Aus Datenraum Und Sharepoint, Anlagen Aus Edv Systemen, Anlagen Aus Mandantenmaterial: Spezial Pruefmodus Fristennotiz Und Naechster Schritt; Anlagen Aus Datenraum Und Sharep... |
| `schiedsverfahren-anlagenband-und-datentraeger` | Plant Anlagenbände im Schiedsverfahren: mehrere Originale, USB-Sticks, PDF-Bundles, Index, Hashliste, Verfahrensanordnung und parallele elektronische Struktur. |
| `schriftsatz-anlagen-mapping` | Schriftsatzstellen, Tatsachenbehauptungen, Beweisangebote und Anlagen in eine Matrix bringen; erkennt fehlende, doppelte und nur scheinbar belegte Anlagen. |
| `spezial-anlage-red-team-und-qualitaetskontrolle` | Anlage: Red-Team und Qualitätskontrolle im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-anlagen-tatbestand-beweis-und-belege` | Anlagen: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-anlagenkonvolut-sonderfall-und-edge-case` | Anlagenkonvolut: Sonderfall und Edge-Case-Prüfung im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-arial-mandantenkommunikation-entscheidungsvorlage` | Entscheidet Stempelbild, Deckblatt, Anlagenverzeichnis und Mandantenfreigabe so, dass die Anlage optisch und logisch eindeutig ist. |
| `spezial-baut-beweislast-und-darlegungslast` | Prüft, ob die Anlage eine konkrete Darlegung trägt oder nur einen pauschalen Anlagenverweis kaschiert; trennt Tatsachenvortrag, Beweisangebot und bloße Hintergrundunterlage. |
| `spezial-benennt-compliance-dokumentation-und-akte` | Benennt: Compliance-Dokumentation und Aktenvermerk im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-bereits-abschlussprodukt-und-uebergabe` | Bereits: Abschlussprodukt und Übergabe im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-excel-schriftsatz-brief-und-memo-bausteine` | Macht Tabellenanlagen im Schriftsatz verständlich: Zahlenkern, Rechenweg, PDF-Ausdruck, Anlagenzitat und kurze Erläuterung. |
| `spezial-gerichtlichen-fristen-form-und-zustaendigkeit` | Gerichtlichen: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-konform-mehrparteien-konflikt-und-interessen` | Konform: Mehrparteienkonflikt und Interessenmatrix im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-konvertiert-zahlen-schwellen-und-berechnung` | Prüft PDF-Konvertierung, Dateigrößen, Seitenzahlen, OCR und technische Schwellen vor Versand. |
| `spezial-logik-livequellen-und-rechtsprechungscheck` | Logik: Livequellen- und Rechtsprechungscheck im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-oben-formular-portal-und-einreichung` | Prüft, wie Anlagen technisch eingereicht werden: beA, ERV, Portal, Datenträger, mehrere Teilpakete, Begleitvermerk und Eingangsprüfung. |
| `spezial-pruefmodus-fristennotiz-und-naechster-schritt` | Validiert ein vorhandenes Anlagenpaket und gibt eine kurze Fristennotiz plus nächste Handlung aus. |
| `spezial-schriftsaetzen-dokumentenmatrix-und-lueckenliste` | Baut aus Schriftsatz und Dateiliste eine Matrix mit Tatsachen, Belegen, fehlenden Anlagen und Nachforderungen. |
| `spezial-schriftsatz-sortiert-stempelt-word` | Spezial Schriftsatz Verhandlung Vergleich Und Eskalation, Spezial Sortiert Risikoampel Und Gegenargumente, Spezial Stempelt Internationaler Bezug Und Schnittstellen, Spezial Word Behörden Gericht Und Registerweg: Spezial Schriftsatz Verh... |
| `spezial-schriftsatz-verhandlung-vergleich-und-eskalation` | Schriftsatz: Verhandlung, Vergleich und Eskalation im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-sortiert-risikoampel-und-gegenargumente` | Sortiert: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-stempelt-internationaler-bezug-und-schnittstellen` | Stempelt: Internationaler Bezug und Schnittstellen im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-word-behoerden-gericht-und-registerweg` | Bereitet Word-, PDF- und Scan-Anlagen für Gerichts- oder Behördenwege vor: Konvertierung, Lesezeichen, PDF/A, Dateiname, Deckblatt. |
| `spezial-zuordnung-erstpruefung-und-mandatsziel` | Zuordnung: Erstprüfung, Rollenklärung und Mandatsziel im Plugin anlagen zu schriftsaetzen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-allgemein-chronologie-belegmatrix-fristen-risikoampel` | Allgemein, Workflow Chronologie Und Belegmatrix, Workflow Fristen Und Risikoampel, Workflow Mandantenkommunikation: Allgemein; Workflow Chronologie Und Belegmatrix; Workflow Fristen Und Risikoampel; Workflow Mandantenkommunikation. Führt... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin anlagen-zu-schriftsaetzen: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin anlagen-zu-schriftsaetzen: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin anlagen-zu-schriftsaetzen: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin anlagen-zu-schriftsaetzen: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin anlagen-zu-schriftsaetzen: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin anlagen-zu-schriftsaetzen: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin anlagen-zu-schriftsaetzen: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin anlagen-zu-schriftsaetzen: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-frist-eilversand-schiedsverfahren-anlagenband` | Workflow Redteam Qualitygate, Frist Und Eilversand Anlagenpaket, Schiedsverfahren Anlagenband Und Datentraeger, Spezial Gerichtlichen Fristen Form Und Zustaendigkeit: Workflow Redteam Qualitygate; Frist Und Eilversand Anlagenpaket; Schie... |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin anlagen-zu-schriftsaetzen: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin anlagen-zu-schriftsaetzen: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `zeitleiste-und-belegkette` | Baut aus Anlagen eine Chronologie und zeigt zu jedem Ereignis, welcher Beleg trägt, welcher nur plausibilisiert und welcher fehlt. |
| `zuordnung-zeitleiste-belegkette` | Spezial Zuordnung Erstpruefung Und Mandatsziel, Zeitleiste Und Belegkette: Spezial Zuordnung Erstpruefung Und Mandatsziel; Zeitleiste Und Belegkette. Führt Intake, Prüfroutine, Normen-/Quellenradar, Beweislogik, Outputmuster und Qualität... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
