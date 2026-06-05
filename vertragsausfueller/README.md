# Vertragsausfüller

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`vertragsausfueller`) | [`vertragsausfueller.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/vertragsausfueller.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Cowork-Plugin für workflowgestütztes Ausfüllen von Vertragsvorlagen und Altverträgen. Ein Nutzer lädt eine Word-Vorlage, einen alten Vertrag, ein Term Sheet oder Freitextdaten hoch. Das Plugin strippt das Dokument, erkennt Felder und Klauseln, fragt fehlende Daten ab, mappt Term-Sheet-Daten auf Vertragsfelder und erstellt daraus einen neuen Vertragsentwurf.

Der BSAG-Mietvertrag und das Term Sheet Kiosk Huckelriede sind als Beispielakte eingebunden.

## Installation

1. Claude Code oder Claude Desktop/Cowork öffnen.
2. **Customize Plugins** bzw. **Personal plugins** wählen.
3. **Install from .zip** und `vertragsausfueller.zip` hochladen.
4. Mit einem konkreten Auftrag starten, zum Beispiel: `Fülle diesen Mietvertrag mit den Daten aus dem Term Sheet aus.`

Alternativ via Marketplace:

```
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install vertragsausfueller@claude-fuer-deutsches-recht
```

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json`, `skills/` und `assets/` enthalten.

## Workflow

1. Vorlage oder alten Vertrag hochladen.
2. Dokument strippen: Absätze, Tabellen, Platzhalter, Klauseln, Anlagen und Signaturen erkennen.
3. Term Sheet, E-Mail oder Freitextdaten danebenlegen.
4. Feldinventar und Mapping erzeugen.
5. Fehlende Daten freundlich abfragen oder als offene Platzhalter markieren.
6. Clean-Vertrag erstellen.
7. Nur auf ausdrückliche Nachfrage zusätzlich Track Changes oder Redline vorbereiten.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| vaf-kommandocenter | steuert den gesamten Workflow von Upload bis neuem Vertragsentwurf. |
| vaf-docx-stripper | macht aus Word-Dokumenten ein bearbeitbares Vertragsmodell. |
| vaf-template-erkennung | klassifiziert den Vertrag und trennt Fixtext von Variablen. |
| vaf-feldinventar | baut die zentrale Datenmatrix für den Vertrag. |
| vaf-termsheet-mapping | überführt wirtschaftliche Eckdaten in Vertragsklauseln. |
| vaf-rueckfrageninterview | füllt Datenlücken ohne den Nutzer zu überfordern. |
| vaf-bsag-mietvertrag | setzt den Huckelriede-Term-Sheet-Fall in die BSAG-Vorlage um. |
| vaf-klauselentscheidung | verhindert stilles Auswählen riskanter Optionen. |
| vaf-plausibilitaetscheck | härtet den Entwurf vor Versand oder Verhandlung. |
| vaf-clean-output | liefert den ersten belastbaren Vertragsentwurf. |
| vaf-track-changes-nur-nach-frage | setzt die ausdrückliche Nachfragepflicht durch. |
| vaf-redline-qa | kontrolliert Änderungsfassungen vor Herausgabe. |
| vaf-altvertrag-nachziehen | macht aus alten Verträgen neue Entwürfe. |
| vaf-quality-gate | ist die letzte Schleuse vor Vertragserzeugung. |

## BSAG-Beispiel

Die Beispielakte enthält die Word-Vorlage `BSAG-Mietvertrag-Vorlage.docx` und das Term Sheet `BSAG-TermSheet-Kiosk-Huckelriede - Kopie.docx`. Der Spezialskill `vaf-bsag-mietvertrag` mappt daraus insbesondere Mieter, Mietobjekt, Nutzung, Fläche, Miete, Nebenkosten, Kaution, Mietbeginn, Laufzeit, Optionen, Indexierung, Umsatzsteuer, Öffnungszeiten, Konkurrenzschutz, Sortiment, Fettabscheider, Werbung und Versicherung.

## Track-Changes-Regel

Das Plugin erzeugt keine Track-Changes- oder Redline-Fassung stillschweigend. Es fragt immer ausdrücklich: Soll zusätzlich eine Track-Changes- oder Redline-Fassung erstellt werden? Ohne Bestätigung bleibt es bei Clean-Entwurf, Änderungslog und Ausfüllprotokoll.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `changes-beweislast-docx-erkennen` | Changes Beweislast Docx Erkennen im Plugin Vertragsausfueller: prüft konkret Changes, Docx, Erkennen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `erzeugen-red-fassungen-sonderfall-felder` | Erzeugen RED Fassungen Sonderfall Felder im Plugin Vertragsausfueller: prüft konkret Erzeugen, Fassungen, Felder. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `fuehren-interessen-mappen-nachfrage` | Fuehren Interessen Mappen Nachfrage im Plugin Vertragsausfueller: prüft konkret Fuehren, Mappen, Nachfrage. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `neue-rueckfragen-strippen` | Neue Rueckfragen Strippen im Plugin Vertragsausfueller: prüft konkret Neue, Rueckfragen, Strippen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `sheets-quellenkarte` | Sheets Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `term-track-vertraege` | Term Track Vertraege im Plugin Vertragsausfueller: prüft konkret Term, Track, Vertraege. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `vaf-clean-output` | Sauberen finalen Vertragsentwurf mit Ausfüllprotokoll erstellen: Anwendungsfall alle Felder sind ausgefüllt und Quality Gate hat grüne Ampel ergeben; nun wird bereinigte Clean-Version für Unterschrift oder Versand erstellt. §§ 125 ff. BG... |
| `vaf-plausibilitaetscheck-termsheet` | VAF Plausibilitaetscheck Termsheet im Plugin Vertragsausfueller: prüft konkret Plausibilitätsprüfung vor Vertragsausgabe, Term Sheet auf Vertragsfelder mappen, Altvertraege. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel un... |
| `vaf-versionierung` | VAF Versionierung im Plugin Vertragsausfueller: fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |
| `vertragsausfueller-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `vertragsausfueller-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `vertragsausfueller-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `vertragsausfueller-mandantenkommunikation-redteam-qualitygate` | Mandantenkommunikation Redteam Qualitygate im Plugin Vertragsausfueller: prüft konkret Mandantenkommunikation im Plugin vertragsausfueller, Red-Team Qualitygate im Plugin vertragsausfueller, Ausdruecklicher. Liefert priorisierten Output... |
| `vertragsausfueller-output-waehlen` | Output wählen im Plugin Vertragsausfueller: Diese Output-Weiche für Vertragsausfueller entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `vertragsausfueller-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `vertragsausfueller-start-chronologie-fristen` | Start Chronologie Fristen im Plugin Vertragsausfueller: prüft konkret Einstieg, Schnelltriage und Fallrouting im Vertragsausfueller-Plugin, Chronologie und Belegmatrix im Plugin vertragsausfueller, Fristen- und Risikoampel im Plugin vert... |
| `vertragsausfueller-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `vertragsausfueller-vaf-batch-modus-docx-stripper-einfuehrung` | VAF Batch Modus Docx Stripper Einfuehrung im Plugin Vertragsausfueller: prüft konkret Batch-Modus fuer Konzernvertraege, DOCX-Vorlage in strukturierten Text zerlegen, Einfuehrung Prozess Vertragsausfueller. Liefert priorisierten Output m... |
| `vertragsausfueller-vaf-bsag-mietvertrag-klauselentscheidung` | VAF Bsag Mietvertrag Klauselentscheidung im Plugin Vertragsausfueller: prüft konkret BSAG-Kiosk-Mietvertrag ausfüllen, Wahlklauseln und Klauselalternativen im Vertrag entscheiden, Spezialfall Rahmenvertrag im Konzern anpassen ohne. Liefe... |
| `vertragsausfueller-vaf-feldinventar-fragebogen-input` | VAF Feldinventar Fragebogen Input im Plugin Vertragsausfueller: prüft konkret Feldinventar für Vertragsgenerator erstellen, Leitfaden Fragebogen-Input fuer Vertragsausfueller, Spezialfall fremdsprachige und bilinguale Vertraege. Liefert... |
| `vertragsausfueller-vaf-kommandocenter-mehrsprachige-vertraege` | VAF Kommandocenter Mehrsprachige Vertraege im Plugin Vertragsausfueller: prüft konkret Vertragsausfüller Kommandocenter starten, Spezialfall mehrsprachige Vertraege deutsch / englisch, Bauleiter Platzhalterlogik. Liefert priorisierten Ou... |
| `vertragsausfueller-vaf-quality-gate-redline-qa` | VAF Quality Gate Redline QA im Plugin Vertragsausfueller: prüft konkret Quality Gate vor Vertragsausgabe, Redline und Track-Changes-Fassung prüfen, Rückfrageninterview für fehlende Vertragsdaten führen. Liefert priorisierten Output mit N... |
| `vertragsausfueller-vaf-template-erkennung-format-track-changes` | VAF Template Erkennung Format Track Changes im Plugin Vertragsausfueller: prüft konkret Vertragsvorlage und Altvertrag erkennen und analysieren, Template-Format und Quelle, Track Changes und Redline nur nach ausdrücklicher. Liefert prior... |
| `vorlagen-vertragsausfueller-vaf-altvertrag` | Vorlagen Vertragsausfueller VAF Altvertrag im Plugin Vertragsausfueller: prüft konkret Vorlagen, Vertragsausfueller, Altvertrag auf neue Vorlage nachziehen und aktualisieren. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel u... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
