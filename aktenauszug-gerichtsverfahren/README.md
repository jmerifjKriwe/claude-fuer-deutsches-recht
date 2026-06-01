# aktenauszug-gerichtsverfahren

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`aktenauszug-gerichtsverfahren`) | [`aktenauszug-gerichtsverfahren.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/aktenauszug-gerichtsverfahren.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

**Version:** 3.2.1
**Autor:** Klotzkette

---

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| Aktenauszug Gerichtsverfahren (`aktenauszug-gerichtsverfahren`) | [aktenauszug-gerichtsverfahren.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/aktenauszug-gerichtsverfahren.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Plugin erscheint in der Plugin-Liste; alle 21 Skills sind sofort verfügbar.
4. Für Updates: neues ZIP herunterladen und Plugin ersetzen.
5. Hinweis: Das Plugin-ZIP muss direkt `.claude-plugin/plugin.json`, `skills/` und `references/` im ZIP-Root enthalten — nicht das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Überblick

Das Plugin `aktenauszug-gerichtsverfahren` generiert strukturierte Aktenauszüge für deutsche Gerichtsverfahren. Es richtet sich an Rechtsanwältinnen und Rechtsanwälte, die sich schnell in ein neues oder übernommenes Mandat einarbeiten müssen.

**Einsatzgebiete:**

- Mandatswechsel und Übernahme von laufenden Verfahren
- Einarbeitung neuer Sachbearbeiter in komplexe Akten
- Vorbereitung auf mündliche Verhandlungen
- Strukturierung umfangreicher Akten vor Beratungsgesprächen
- Erstellung von Mandantenberichten zum Verfahrensstand

**Verfahrensarten:**

- Zivilverfahren (ZPO) inkl. Berufung, Revision, einstweilige Verfügung
- Strafverfahren (StPO) inkl. Revision und Wiederaufnahme
- Verwaltungsverfahren (VwGO) inkl. Berufung und Revision
- Arbeitsgerichtsverfahren (ArbGG) inkl. Urteilsverfahren und Beschlussverfahren
- Sozialgerichtsverfahren (SGG) inkl. Berufung und Eilrechtsschutz

## Skills-Übersicht

| Skill | Zweck |
| --- | --- |
| `aktenauszug-erstellen` | Hauptworkflow: erzeugt alle sechs Bausteine des strukturierten Aktenauszugs aus PDFs und Schriftsätzen |
| `verfahrensidentifikation` | Extrahiert Gericht Kammer Aktenzeichen Streitwert Parteien Instanz und Verfahrensart |
| `einleitungssatz-generator` | Verfasst einen prägnanten ein- bis zweiSatz-Kern des Rechtsstreits mit Hauptnorm |
| `verfahrenszusammenfassung-absatz` | Schreibt zusammenfassenden Absatz mit acht bis zehn Sätzen zu Hintergrund Streitstand prozessualer Lage und nächsten Schritten |
| `sachverhaltschronologie` | Chronologische Bullet-Liste aller wesentlichen außerprozessualen Tatsachen mit Datum und Fundstelle |
| `verfahrenschronologie` | Chronologische Bullet-Liste aller prozessualen Schritte mit hervorgehobenen Fristen |
| `parteivortrag-gegenueberstellung` | Tabelle mit Kläger- und Beklagtenposition zu jedem Streitpunkt |
| `beweismittel-gegenueberstellung` | Tabelle aller Beweisangebote (Zeugen Urkunden Sachverständige) nach Partei und Beweisthema |
| `rechtsargumente-gegenueberstellung` | Tabelle der Rechtsargumente beider Parteien mit Anspruchsgrundlagen Einwendungen Einreden und Rechtsprechungsnachweisen |
| `fristen-und-terminkalender` | Identifiziert und hebt alle prozessrelevanten Fristen und Termine hervor |
| `anlagenverzeichnis-extrakt` | Vollständiges Anlagenverzeichnis aller K-/B-Anlagen mit Inhalt und Fundstelle |
| `schwerpunktthemen-identifikation` | Identifiziert drei bis fünf zentrale Rechtsfragen ohne Erfolgsprognose |
| `neutralitaetspruefung` | Prüft den Aktenauszug auf unzulässige Wertungen und Prognosen und schlägt Korrekturen vor |
| `aktenauszug-strukturpruefung` | Vollständigkeitsprüfung aller sechs Bausteine und Qualitätsgrundsätze |
| `zivilprozess-modus` | ZPO-spezifische Einstellungen für ordentliche Klage Berufung Revision und einstweilige Verfügung |
| `strafprozess-modus` | StPO-spezifische Einstellungen für Anklageverfahren Hauptverhandlung und Revision |
| `verwaltungsprozess-modus` | VwGO-spezifische Einstellungen mit Vorverfahren aufschiebender Wirkung und Berufungszulassung |
| `arbeitsgerichtsverfahren-modus` | ArbGG-spezifische Einstellungen mit Gütetermin KSchG-Dreiwochenfrist und Beschlussverfahren |
| `sozialgerichtsverfahren-modus` | SGG-spezifische Einstellungen mit Widerspruchsverfahren Amtsermittlung und Eilrechtsschutz |
| `anwaltsschriftsatz-stilrichtlinie` | Verbindliche Stilregeln für Sprache Gliederung Nomenklatur und Markdown-Formatierung |

## Methodik

Ausführliche Erläuterung der Methodik unter [references/methodik.md](references/methodik.md).

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Beispielprompt

```
Erstelle einen strukturierten Aktenauszug für das anhängende Verfahren vor dem Landgericht Frankfurt am Main (Az. 3 O 456/23). Die Akte enthält Klageschrift, Klageerwiderung und den Beweisbeschluss vom 15.09.2023. Verwende den Zivilprozess-Modus.
```

## Disclaimer

Dieses Plugin erstellt keine Rechtsberatung und gibt keine Erfolgsprognose ab. Die erstellten Aktenauszüge sind Arbeitsinstrumente, die der Prüfung und Freigabe durch den zuständigen Rechtsanwalt bedürfen. Das Plugin ersetzt nicht die eigene Aktenlektüre.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 50 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aktenauszug-erstellen` | Anwalt oder Paralegal erhaelt Gerichtsakte Schriftsaetze oder PDFs und will strukturierten Aktenauszug erstellen. Sechs Bausteine: Verfahrensidentifikation Einleitungssatz Absatz-Zusammenfassung Sachverhaltschronologie Verfahrenschronolo... |
| `aktenauszug-strukturpruefung` | Fertig erstellten Aktenauszug auf Vollständigkeit prüfen: alle Bausteine vorhanden Fristen hervorgehoben neutrale Sprache. Normen §§ 128-134 253 ZPO. Prüfraster Bausteine-Vollständigkeit Fristen-Markierung Neutralitaets-Check Sprach-Qual... |
| `akzg-aktenauszug-bauleiter` | Bauleiter Aktenauszug fuer Gerichtsverfahren: Sachverhalt, Streitstand, Beweisangebote, Schlussantraege. Pruefraster Vollstaendigkeit fuer Berufung und Revision. |
| `akzg-multiparteienverfahren-konsolidierung-spezial` | Spezialfall Multiparteienverfahren Konsolidierung mehrerer Akten und Streithelfer: Reihenfolge, Querverweise, Streitverkuendung. Pruefraster fuer Hauptaktenfuehrer. |
| `akzg-vertraulichkeit-redaction-spezial` | Spezialfall Vertraulichkeit und Redaction in Aktenauszuegen: Berufsgeheimnis, personenbezogene Daten, Konzerninterna. Pruefraster fuer Akteneinsicht durch Dritte. |
| `akzg-zeitstrahl-checkliste` | Checkliste Zeitstrahl in Aktenauszug: Eingang Klage, Klageerwiderung, Beweisbeschluss, mundliche Verhandlung, Urteil. Pruefraster fuer Rechtsmittelinstanz. |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Aktenauszug Gerichtsverfahren-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren A... |
| `anlagenverzeichnis-extrakt` | Anwalt sucht alle Anlagen K-/B-/AST-/AG-Verweise in der Akte und will Anlagenverzeichnis erstellen. Anlagenbezeichnung Kurzbeschreibung Schriftsatz Blattangabe je Partei. Normen §§ 130 131 ZPO Schriftsatz-Anlagen. Prüfraster Vollständigk... |
| `anwaltsschriftsatz-stilrichtlinie` | Stilrichtlinie für den juristisch sauberen neutralen und für Anwaelte lesbaren Aktenauszug: Sprache Gliederung Nomenklatur Abkuerzungskonventionen Tabellengestaltung und Markdown-Formatierung. Verbindliche Stilregeln für alle Bausteine d... |
| `arbeitsgerichtsverfahren-modus` | Aktenauszug für ArbGG-Verfahren erstellen: Guetetermin Kammerverfahren Urteilsverfahren Beschlussverfahren. KSchG-Dreiwochenfrist § 4 KSchG Berufung § 64 ArbGG Revision § 72 ArbGG. Normen ArbGG §§ 2 54 64 72 KSchG §§ 1 4 9. Prüfraster Fr... |
| `beweismittel-gegenueberstellung` | Anwalt will Beweisangebote aller Parteien uebersichtlich gegenüberstellen: Zeugen Urkunden Sachverständige Parteivernehmung Augenschein. Normen §§ 355-455 ZPO Sachverständigenbeweis Zeugenbeweis. Prüfraster Vollständigkeit Parteizuordnun... |
| `einleitungssatz-generator` | Aktenauszug braucht praegnanten Einleitungssatz: wer streitet mit wem worueber welche Hauptnorm. Juristisch praezise neutral ohne Wertung ohne Erfolgsprognose. Normen §§ 253 304 ZPO. Prüfraster Praegnanz Vollständigkeit Neutralitaet Haup... |
| `fristen-und-terminkalender` | Anwalt will alle prozessrelevanten Fristen und Termine im Aktenauszug hervorheben: Klagefrist Berufungsfrist Begründungsfrist Verkündungstermin Vollziehungsfrist. Normen §§ 222 517 520 548 ZPO. Prüfraster Vollständigkeit Frist-Berechnung... |
| `neutralitaetspruefung` | Prüft einen erstellten Aktenauszug auf unzulässige Wertungen und Erfolgseinschaetzungen und neutralisiert diese. Markiert alle parteiischen Formulierungen Prognosen und Bewertungen und schlaegt neutrale Ersatzformulierungen vor. Sicherhe... |
| `parteivortrag-gegenueberstellung` | Erstellt eine Tabelle mit zwei Spalten (Klaegerseite und Beklagtenseite) für streitige Sachverhaltsangaben Punkt für Punkt. Jeder Streitpunkt wird als eigene Zeile gegenübergestellt. Fundstellen in Schriftsaetzen werden angegeben. Keine... |
| `rechtsargumente-gegenueberstellung` | Erstellt eine tabellarische Gegenüberstellung der Rechtsargumente beider Parteien: Anspruchsgrundlage Einwendungen Einreden Verjährungsthema und Pinpoint-Zitate aus Rechtsprechung (BGH OLG EuGH). Keine Wertung welches Argument ueberzeugt... |
| `sachverhaltschronologie` | Erstellt eine chronologische Bullet-Liste aller wesentlichen außerprozessualen Tatsachen: Vertragsschluss Vorfaelle vorgerichtliche Korrespondenz Schadensereignisse und Behoerdenakte. Datum fett vorangestellt knappe Beschreibung ohne Wer... |
| `schwerpunktthemen-identifikation` | Anwalt braucht schnellen Überblick über drei bis fuenf rechtliche Hauptstreitpunkte des Verfahrens mit Pinpoint-Zitaten ohne Erfolgsprognose. Normen §§ 139 286 ZPO BGH-Leitsaetze. Prüfraster Streitpunkt-Relevanzbewertung Rechtsprechungs-... |
| `sozialgerichtsverfahren-modus` | Aktenauszug für SGG-Verfahren erstellen: Klage Berufung §§ 143 ff. SGG Eilantrag § 86b SGG Widerspruchsverfahren. Amtsermittlungsgrundsatz Sozialversicherungs-Leistungsarten. Normen SGG §§ 51 77 86b 143. Prüfraster SGG-spezifische Friste... |
| `spezial-akten` | Vertiefter Spezial-Skill im Plugin aktenauszug-gerichtsverfahren zu Akten: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-aktenauszug` | Vertiefter Spezial-Skill im Plugin aktenauszug-gerichtsverfahren zu aktenauszug: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-beweismittel` | Vertiefter Spezial-Skill im Plugin aktenauszug-gerichtsverfahren zu Beweismittel: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-einarbeitung` | Vertiefter Spezial-Skill im Plugin aktenauszug-gerichtsverfahren zu Einarbeitung: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-einleitungssatz` | Vertiefter Spezial-Skill im Plugin aktenauszug-gerichtsverfahren zu Einleitungssatz: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-erstellen` | Vertiefter Spezial-Skill im Plugin aktenauszug-gerichtsverfahren zu erstellen: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-gegenueberstellung` | Vertiefter Spezial-Skill im Plugin aktenauszug-gerichtsverfahren zu Gegenüberstellung: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-gerichtsverfahren` | Vertiefter Spezial-Skill im Plugin aktenauszug-gerichtsverfahren zu gerichtsverfahren: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-parteivortraege` | Vertiefter Spezial-Skill im Plugin aktenauszug-gerichtsverfahren zu Parteivortraege: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-rechtsargumente` | Vertiefter Spezial-Skill im Plugin aktenauszug-gerichtsverfahren zu Rechtsargumente: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-sachverhaltschronologie` | Vertiefter Spezial-Skill im Plugin aktenauszug-gerichtsverfahren zu Sachverhaltschronologie: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-schnelle` | Vertiefter Spezial-Skill im Plugin aktenauszug-gerichtsverfahren zu schnelle: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-strukturierter` | Vertiefter Spezial-Skill im Plugin aktenauszug-gerichtsverfahren zu Strukturierter: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-strukturierter-aktenauszug-gerichtsv` | Vertiefter Spezial-Skill im Plugin aktenauszug-gerichtsverfahren zu Strukturierter Aktenauszug Gerichtsverfahren: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-strukturpruefung` | Vertiefter Spezial-Skill im Plugin aktenauszug-gerichtsverfahren zu strukturpruefung: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-tabellarische` | Vertiefter Spezial-Skill im Plugin aktenauszug-gerichtsverfahren zu tabellarische: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-verfahrensgeschichte` | Vertiefter Spezial-Skill im Plugin aktenauszug-gerichtsverfahren zu Verfahrensgeschichte: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-verfahrensidentifikation` | Vertiefter Spezial-Skill im Plugin aktenauszug-gerichtsverfahren zu Verfahrensidentifikation: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-verfahrenszusammenfassung` | Vertiefter Spezial-Skill im Plugin aktenauszug-gerichtsverfahren zu Verfahrenszusammenfassung: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `strafprozess-modus` | Aktenauszug für StPO-Verfahren erstellen: Anklage Hauptverhandlung Revision §§ 333 ff. StPO Wiederaufnahme. Anklageschrift Eroeffnungsbeschluss Beweisantragsrecht Rechtsmittelfristen. Normen StPO §§ 200 203 333 359 BGH-Leitsaetze StPO. P... |
| `verfahrenschronologie` | Erstellt eine chronologische Bullet-Liste aller prozessualen Schritte: Klageeingang Zustellungen Schriftsatzfristen Beweisbeschluesse muendliche Verhandlungen Beweisaufnahme Urteile und Rechtsmittel. Kritische Fristen werden optisch herv... |
| `verfahrensidentifikation` | Extrahiert strukturiert alle Verfahrensstammdaten: Gericht Kammer Aktenzeichen Streitwert Parteien (Klaeger Beklagte Streithelfer mit Anschrift gesetzlicher Vertretung Prozessbevollmaechtigten) Instanz und Verfahrensart (Klage Eilverfahr... |
| `verfahrenszusammenfassung-absatz` | Anwalt will sich schnell in Akte einarbeiten ohne vollständige Lektuere. Acht bis zehn Saetze Hintergrund Streitstand prozessuale Lage anstehende Verfahrenshandlungen. Normen §§ 253 261 ZPO. Prüfraster Vollständigkeit Neutralitaet Versta... |
| `verwaltungsprozess-modus` | Aktenauszug für VwGO-Verfahren erstellen: Anfechtungs- Verpflichtungsklage Berufung § 124 VwGO Revision § 132 VwGO Eilrechtsschutz §§ 80 123 VwGO. Normen VwGO §§ 40 42 80 113 124 132. Prüfraster VwGO-spezifische Fristen Vorverfahren Wide... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin aktenauszug-gerichtsverfahren: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin aktenauszug-gerichtsverfahren: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin aktenauszug-gerichtsverfahren: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin aktenauszug-gerichtsverfahren: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin aktenauszug-gerichtsverfahren: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin aktenauszug-gerichtsverfahren: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin aktenauszug-gerichtsverfahren: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin aktenauszug-gerichtsverfahren: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin aktenauszug-gerichtsverfahren: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin aktenauszug-gerichtsverfahren: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `zivilprozess-modus` | Aktenauszug für ZPO-Verfahren erstellen: ordentliche Klage muendliche Verhandlung Berufung §§ 511 ff. ZPO Revision §§ 542 ff. ZPO einstweilige Verfuegung §§ 935 ff. ZPO. Normen ZPO BGH-Leitsaetze. Prüfraster ZPO-Fristen Instanzenzug Beso... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
