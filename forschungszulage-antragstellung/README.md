# Forschungszulage-Antragstellung

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`forschungszulage-antragstellung`) | [`forschungszulage-antragstellung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/forschungszulage-antragstellung.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

Plugin für die steuerliche Forschungsförderung nach dem Forschungszulagengesetz: Fördercheck, BSFZ-Bescheinigung, Projektbeschreibung, FuE-Abgrenzung, Bemessungsgrundlage, Finanzamt-Antrag, Auszahlung, Verlust-/Krisenlage, Dokumentation für Außenprüfung, Kumulierung und Nachbesserung.

Das Plugin ist für Unternehmen, Start-ups, Mittelstand, Steuerberaterinnen, Rechtsanwälte, CFOs und Produkt-/Entwicklungsteams gebaut. Es übersetzt technische Entwicklung in die Sprache, die BSFZ und Finanzamt brauchen: Neuheit, Risiko, systematisches Vorgehen, förderfähige Aufwendungen und saubere Belege. Es kann bewusst zwei Geschwindigkeiten: geführter Modus für Einsteiger und harter Ampel-/Cashflow-Modus für Profis.

## Quellen-Gate

Vor jeder belastbaren Ausgabe live prüfen:

- Forschungszulagengesetz auf `gesetze-im-internet.de`, insbesondere §§ 1 bis 7 und § 10 FZulG.
- BSFZ-Antragsverfahren: zweistufig, erst FuE-Bescheinigung bei der BSFZ, dann Antrag beim Finanzamt.
- BMF-Forschungszulage und BMF-Schreiben vom 07.02.2023, soweit noch nicht durch ein neues finales Schreiben ersetzt.
- Änderungen ab 2026: Bemessungsgrundlagenhöchstbetrag 12 Mio. Euro, 20-%-Pauschale für Gemein- und Betriebskosten bei nach dem 31.12.2025 begonnenen Vorhaben, Eigenleistung 100 Euro pro Stunde bis max. 40 Stunden/Woche.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Forschungszulage-Antragstellung (`forschungszulage-antragstellung`) | [forschungszulage-antragstellung.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/forschungszulage-antragstellung.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version.

### Installation

1. ZIP herunterladen.
2. Claude Code oder Cowork → **Customize Plugins** → **Install from .zip**.
3. In einer neuen Unterhaltung starten mit:

```text
/forschungszulage-antragstellung:allgemein
```

## Skill-Matrix

| Skill | Wofür? |
| --- | --- |
| `allgemein` | Einstieg, Triage, Förderroute und Projektaufnahme |
| `fz-foerdercheck-kaltstart` | Anspruchsberechtigung, Projektart, Jahre, Risiken, Sofortpotenzial |
| `fz-bsfz-bescheinigung-projektbeschreibung` | BSFZ-Antrag, Vorhabenbeschreibung, technische Neuheit, Risiko |
| `fz-fue-definition-frascati-abgrenzung` | Grundlagenforschung, industrielle Forschung, experimentelle Entwicklung |
| `fz-bemessungsgrundlage-2026` | Personal, Eigenleistung, Auftragsforschung, Wirtschaftsgüter, 12-Mio.-Grenze |
| `fz-finanzamt-festsetzung-auszahlung` | Antrag beim Finanzamt, Anrechnung, Auszahlung, Vorauszahlungssenkung |
| `fz-insolvenz-verlust-liquiditaet` | Krise, Verlustjahr, Insolvenz, Forderungs-/Masseblick, Liquidität |
| `fz-dokumentationspaket-betriebspruefung` | Stundenzettel, Projektakte, Kostenbelege, Prüferpaket |
| `fz-kumulierung-beihilfen-agvo` | Doppelförderung, AGVO, andere Zuschüsse, EU/EWR-Auftragsforschung |
| `fz-ablehnung-nachbesserung-einspruch` | BSFZ-Nachforderung, Ablehnung, Finanzamt-Einspruch, Reparatur |
| `fz-roadmap-mehrjahresantrag` | Mehrjahresstrategie, rückwirkende Jahre, Jahreswechsel, Portfolio |

## Typische Startpunkte

| Situation | Start |
| --- | --- |
| "Wir wissen nicht, ob unser Vorhaben FuE ist" | `allgemein` → `fz-foerdercheck-kaltstart` |
| "Wir müssen den BSFZ-Antrag schreiben" | `fz-fue-definition-frascati-abgrenzung` → `fz-bsfz-bescheinigung-projektbeschreibung` |
| "Wir wollen wissen, wie viel Geld kommt" | `fz-bemessungsgrundlage-2026` → `fz-finanzamt-festsetzung-auszahlung` |
| "Wir sind im Verlust / in der Krise" | `fz-insolvenz-verlust-liquiditaet` |
| "BSFZ fragt nach oder lehnt ab" | `fz-ablehnung-nachbesserung-einspruch` |

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 50 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Adaptiver Einstieg, Mandatsklärung und Routing im Forschungszulage-Plugin. Führt Einsteiger, Technikteams, CFOs und Steuerberater unterschiedlich, klärt Unternehmen, FuE-Vorhaben, Wirtschaftsjahre, BSFZ-Status, Finanzamt-Antrag, Liquidit... |
| `fz-ablehnung-nachbesserung-einspruch` | Ablehnung oder Nachforderung bei Forschungszulage strukturiert bearbeiten: BSFZ-Rückfrage, negative Bescheinigung, BSFZ-Widerspruch, Finanzamt-Kürzung, Einspruch nach AO, neue Tatsachen, Beleg- und Textreparatur, Klage Finanzgericht als... |
| `fz-auftragsforschung-vertragsgestaltung` | Auftragsforschung im Sinne § 3 Abs. 4 FZulG: Auftraggeber-Auftragnehmer-Konstellation, Pflichten des Auftraggebers (Risikotragung, Verwertung), foerderfaehige Quote 60 oder 70 Prozent der vereinbarten Vergueng. Pruefraster Vertragsgestal... |
| `fz-bemessungsgrundlage-2026` | Bemessungsgrundlage Forschungszulage ab 2026 belastbar berechnen: eigene FuE-Personalkosten, Eigenleistung 100 Euro je Stunde, Auftragsforschung 70 Prozent EU/EWR, AfA für Wirtschaftsgüter, 20-Prozent-Gemeinkostenpauschale, 12-Mio-Cap, K... |
| `fz-bescheidung-rechtsmittel` | Bescheidung Forschungszulage: Bescheinigungsbescheid BSFZ und Festsetzungsbescheid Finanzamt sind zwei getrennte Verwaltungsakte. Rechtsmittelketten: BSFZ-Widerspruch dann Verpflichtungsklage; Finanzamt-Einspruch dann Klage Finanzgericht... |
| `fz-betriebspruefung-strategie` | Strategie bei Betriebspruefung mit Schwerpunkt Forschungszulage: Vorbereitung, Selbstanzeige bei Fehlern (auch wenn keine Steuerstraftat), Argumentationspakete, Schlussbesprechung. Pruefraster: Stundennachweise, Auftragsforschungsvertrae... |
| `fz-bsfz-bescheinigung-projektbeschreibung` | BSFZ-Antrag und FuE-Projektbeschreibung praxistauglich erstellen: Portaltexte mit Zeichenbudgets, Ausgangsproblem, Stand der Technik, Neuheit, technisches Risiko, systematisches Vorgehen, Arbeitspakete, Prüferlogik, Anti-Floskel-Regeln u... |
| `fz-dokumentationspaket-betriebspruefung` | Dokumentationspaket Forschungszulage prüfungsfest aufbauen: Projektakte mit BSFZ-Antrag und Bescheid, Stundenaufzeichnung je Mitarbeiter Tag Vorhaben, Personalkostenbeleg aus Lohnabrechnung, Auftragsforschungsbeleg mit Vertrag und Rechnu... |
| `fz-finanzamt-festsetzung-auszahlung` | Forschungszulage beim Finanzamt beantragen, festsetzen und auszahlen lassen: ELSTER-Antrag, Vorlage der BSFZ-Bescheinigung, Forschungszulagenbescheid, Anrechnung auf Einkommen- oder Körperschaftsteuer, Auszahlung eines Überschusses, Vora... |
| `fz-foerdercheck-kaltstart` | Schneller Fördercheck Forschungszulage in zehn Minuten: Anspruchsberechtigung, FuE-Kategorie nach Frascati, KMU-Status, Personalkosten-Schwelle, Projektjahre, Kostenarten, BSFZ-/Finanzamt-Status, Kumulierung, Ausschlussrisiken und realis... |
| `fz-fue-abgrenzung-grenzfaelle` | FuE-Definition Grenzfaelle nach Frascati-Manual und FZulG: Neuheit und Unsicherheit, Routinearbeiten gegen Versuch und Irrtum. Beispielszenarien Software-Entwicklung, klinische Studien, Produktoptimierung, Reverse Engineering. Pruefraste... |
| `fz-fue-definition-frascati-abgrenzung` | FuE-Definition für die Forschungszulage praxisnah prüfen: Grundlagenforschung, industrielle Forschung, experimentelle Entwicklung, Frascati-Kriterien (Neuheit, Schöpferisch, Ungewissheit, Systematik, Reproduzierbarkeit), AGVO-Definitione... |
| `fz-historie-und-rechtsgrundlagen` | Historie und Rechtsgrundlagen der steuerlichen Forschungszulage einfuehrend: FZulG seit 2020, Wachstumschancengesetz 2024 mit Erhoehung auf 10 Mio. Euro Bemessungsgrundlage, KMU-Bonus 5 Mio. Euro. Verhaeltnis zu Projektfoerderung (Bund,... |
| `fz-insolvenz-verlust-liquiditaet` | Forschungszulage in Verlust-, Krisen- und Insolvenzlagen als Liquiditätshebel nutzen: Auszahlung statt bloßer Steuerersparnis, Vorauszahlungssenkung, Massezugehörigkeit, Antragsbefugnis Geschäftsleitung oder Insolvenzverwaltung, Aufrechn... |
| `fz-konzern-und-organschaft-spezial` | Spezialfall Konzern und Organschaft: Zurechnung von FuE-Aktivitaeten zwischen Mutter und Tochter, Auftragsforschung im Konzernverbund, Verrechnungspreise mit Fremdvergleich, KMU-Status bei Konzernzugehoerigkeit nach KMU-Empfehlung 2003 3... |
| `fz-koordinierung-zwei-foerderwege` | Koordinierung Forschungszulage mit anderen Foerderwegen: keine Doppelfoerderung derselben Kosten, aber Kombination ueber Modulgrenze hinweg (ZIM, IGF, Horizon Europe, Landesfoerderung). Pruefraster fuer Kostentrennung, Buchhaltung, Besch... |
| `fz-kumulierung-beihilfen-agvo` | Kumulierung Forschungszulage mit anderen Förderungen und Beihilfen sauber prüfen: AGVO Art. 25, EU/EWR-Auftragsforschung, ZIM, BMBF-Programme, Landesprogramme, De-minimis-Nähe, Horizon, Doppelförderung, Nachweis- und Abzugslogik. Mit Kum... |
| `fz-personalkosten-und-stundennachweis` | Foerderfaehige Personalkosten der Forschungszulage: Bruttoarbeitslohn plus Arbeitgeberanteile, Stundenpauschale 70 Euro Eigenunternehmer, Auftragsforschung 60 Prozent (KMU 70 Prozent). Stundennachweissystem: tagesgenau, Aufgabenbezug, Pl... |
| `fz-roadmap-mehrjahresantrag` | Mehrjahresstrategie Forschungszulage: BSFZ-Bescheinigung für mehrjährige Vorhaben, jährliche Aktualisierung der Stundenaufzeichnung und Projektakte, Folgeanträge knapp halten, Roadmap-Pflege, Liquiditätsplanung über Wirtschaftsjahre, rüc... |
| `fz-start-up-und-personengesellschaft` | Start-up- und Personengesellschafts-Konstellation Forschungszulage: GmbH und Co KG, atypisch stille Beteiligung, Mitunternehmerschaft, Verluste in Anfangsjahren mit Zulage als Liquiditaetshebel. Beispielrechnungen, typische Pruefpunkte.... |
| `spezial-abgrenzung` | Vertiefter Spezial-Skill im Plugin forschungszulage-antragstellung zu Abgrenzung: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-adaptiver` | Vertiefter Spezial-Skill im Plugin forschungszulage-antragstellung zu adaptiver: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-adaptiver-foerdercheck` | Vertiefter Spezial-Skill im Plugin forschungszulage-antragstellung zu adaptiver Fördercheck: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-antrag` | Vertiefter Spezial-Skill im Plugin forschungszulage-antragstellung zu Antrag: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-antragstellung` | Vertiefter Spezial-Skill im Plugin forschungszulage-antragstellung zu antragstellung: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-antragstellung-fzulg` | Vertiefter Spezial-Skill im Plugin forschungszulage-antragstellung zu Antragstellung FZulG: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-auszahlung` | Vertiefter Spezial-Skill im Plugin forschungszulage-antragstellung zu Auszahlung: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-bemessungsgrundlage` | Vertiefter Spezial-Skill im Plugin forschungszulage-antragstellung zu Bemessungsgrundlage: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-bemessungsgrundlage-2026` | Vertiefter Spezial-Skill im Plugin forschungszulage-antragstellung zu Bemessungsgrundlage 2026: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-bsfz` | Vertiefter Spezial-Skill im Plugin forschungszulage-antragstellung zu BSFZ: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-einspruch-mehrjahresroadmap` | Vertiefter Spezial-Skill im Plugin forschungszulage-antragstellung zu Einspruch Mehrjahresroadmap: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-finanzamt` | Vertiefter Spezial-Skill im Plugin forschungszulage-antragstellung zu Finanzamt: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-foerdercheck` | Vertiefter Spezial-Skill im Plugin forschungszulage-antragstellung zu Fördercheck: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-forschungszulage` | Vertiefter Spezial-Skill im Plugin forschungszulage-antragstellung zu forschungszulage: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-fue` | Vertiefter Spezial-Skill im Plugin forschungszulage-antragstellung zu FuE: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-fzulg` | Vertiefter Spezial-Skill im Plugin forschungszulage-antragstellung zu FZulG: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-portaltexte` | Vertiefter Spezial-Skill im Plugin forschungszulage-antragstellung zu Portaltexte: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-portaltexte-zeichenbudgets` | Vertiefter Spezial-Skill im Plugin forschungszulage-antragstellung zu Portaltexte Zeichenbudgets: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-verlust` | Vertiefter Spezial-Skill im Plugin forschungszulage-antragstellung zu Verlust: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-zeichenbudgets` | Vertiefter Spezial-Skill im Plugin forschungszulage-antragstellung zu Zeichenbudgets: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin forschungszulage-antragstellung: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin forschungszulage-antragstellung: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin forschungszulage-antragstellung: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin forschungszulage-antragstellung: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin forschungszulage-antragstellung: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin forschungszulage-antragstellung: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin forschungszulage-antragstellung: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin forschungszulage-antragstellung: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin forschungszulage-antragstellung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin forschungszulage-antragstellung: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
