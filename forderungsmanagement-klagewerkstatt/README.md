# Forderungsmanagement — Klagewerkstatt

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`forderungsmanagement-klagewerkstatt`) | [`forderungsmanagement-klagewerkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/forderungsmanagement-klagewerkstatt.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Inkasso-Zahlungsklage ModeFuchs** (`inkasso-zahlungsklage-modefuchs`) | [Gesamt-PDF lesen](../testakten/inkasso-zahlungsklage-modefuchs/gesamt-pdf/inkasso-zahlungsklage-modefuchs_gesamt.pdf) | [`testakte-inkasso-zahlungsklage-modefuchs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-inkasso-zahlungsklage-modefuchs.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

**Generalisierter Klage-Assistent für Inkasso- und Forderungsmanagement-Klagen mit eigenem Plugin-Generator.** Aus eigenen Mustern eine hauseigene Standardvorlage destillieren, online die Zuständigkeit prüfen, die Klage erzeugen und als sofort installierbares Mini-Plugin verpacken. Neu hinzu kommt ein direkter Inkasso-Zahlungsklage-Ersteller mit Mahnvorlauf, Anspruchs-Gatekeeper und der harten Regel: nur klare, fällige und belegte Ansprüche einklagen.

---

---

## Was ist drin

Drei Skills, gedacht als Lernlauf-+-Laufzeit-Paar plus direkter Inkasso-Klageassistent:

| Skill | Zweck |
| --- | --- |
| `klagevorlage-aus-eigenen-mustern` | **Lernlauf**: frisst eigene Klagemuster, Urteile, Kommentare, Aufsätze, Formatvorlagen; destilliert die hauseigene Standardklage-Vorlage; sammelt den Sachverhalt; **prüft online die Zuständigkeit** (justizadressen.nrw.de, justiz.de); liefert die Klage und erzeugt zusätzlich ein eigenes installierbares **Mini-Plugin als ZIP**. |
| `klage-aus-eigenem-skill` | **Laufzeit**: setzt voraus, dass das im Lernlauf erzeugte Mini-Plugin installiert ist. Nimmt nur noch Sachverhalt und Beklagtenadresse, prüft erneut online die Zuständigkeit, befüllt die Hausvorlage. Keine erneute Extraktion. |
| `inkasso-zahlungsklage-ersteller` | **Direktlauf**: liest Forderungsakte, Mahnungen, Abtretung, Inkassoschreiben, Teilzahlungen, Mahnbescheid/Widerspruch und vorhandene Klagen; erstellt Mahnchronologie, Anspruchsmatrix und Gerichtsortprüfung; nimmt nur grüne Positionen in den Klageentwurf. Bezahlte Hauptforderungen werden rot geblockt. |

Alle Klage-Skills führen **bei jedem Lauf** die Online-Zuständigkeitsprüfung über [justizadressen.nrw.de](https://www.justizadressen.nrw.de/de/justiz/suche) und das [bundesweite Justizportal](https://www.justiz.de/onlinedienste/gerichtsverzeichnis_und_orga/index.php) durch.

## Inkasso-Zahlungsklage-Ersteller

Der neue Direktlauf ist für Fälle gedacht, in denen eine Forderungsakte schon einen Mahn- oder Inkassoverlauf enthält. Er prüft vor der Klage:

- Rechnung, Fälligkeit, Lieferung/Leistung und Abtretung.
- Mahnvorlauf mit Zugang, Fristen und Beträgen.
- Zahlungseingänge, Teilzahlungen, Erfüllung und interne Kenntnis.
- Mahnkosten, Verzugszinsen, Inkassokosten und Mahnverfahrenskosten einzeln.
- Gerichtsort mit aktueller ladungsfähiger Anschrift.

Die ModeFuchs-Testakte unter [`testakten/inkasso-zahlungsklage-modefuchs/`](../testakten/inkasso-zahlungsklage-modefuchs/) ist der Referenzfall: Hauptforderung 698,00 EUR bezahlt vor Klageeinreichung, Nebenforderungen 99,84 EUR streitig. Erwartung: Hauptforderung rot, Nebenforderungen gelb, keine automatische Klage über 797,84 EUR. Direktdownload siehe Sofort-Download-Sektion oben.

## Plugin-Generator

Aus den extrahierten Hausregeln und der Standardvorlage packt der Skill ein eigenes, in Claude Code direkt installierbares ZIP:

```bash
python scripts/plugin_aus_hausregeln.py \
  --kanzlei "Kanzlei Mustermann" \
  --vorlage assets/vorlagen-leer/standardklage.md \
  --regeln  /pfad/hausregeln.json \
  --ziel    /pfad/klagewerkstatt-mustermann.zip
```

Layout des erzeugten Plugins:

```
klagewerkstatt-<slug>/
  .claude-plugin/plugin.json
  skills/klage-erstellen/SKILL.md
  assets/vorlage/standardklage.md
  references/hausregeln.json
  references/belegmuster.md
  references/anlagenliste.md
  references/zustaendigkeit-quellen.md
  README.md
```

Der erzeugte Skill enthält die Hausregeln fest verdrahtet und führt weiterhin die **Online-Zuständigkeitsprüfung** als Pflichtschritt aus.

## Ergebnisformate

- **DOCX** über `office/docx` (`Klage-<Beklagte>-<YYYYMMDD>.docx`) und **Markdown-Spiegel**.
- **Anlage Zuständigkeitsprüfung** mit Online-Quelle und Abrufdatum.
- **HTML-Padlet** (`assets/padlet/klage-padlet.html`) — single-file, autark, Live-Vorschau, speichert in `localStorage`, exportiert/importiert JSON.
- **Memo** im Gutachtenstil — nur auf ausdrückliche Anfrage.

## Online-Zuständigkeit (Pflicht in jedem Lauf)

1. **Sachlich** rechnerisch: ≤ 10.000 EUR → AG (§ 23 Nr. 1 GVG i. d. F. seit 1.1.2026); > 10.000 EUR → LG (§ 71 GVG); Sondertatbestände beachten (insbes. Wohnraummietsachen AG ohne Streitwertgrenze, § 23 Nr. 2a GVG).
2. **Örtlich** rechtlich: §§ 12, 13 ZPO Allgemeiner Gerichtsstand, § 29 ZPO Erfüllungsort, § 29c ZPO Verbraucherverträge, § 38 ZPO Gerichtsstandsvereinbarung; grenzüberschreitend Brüssel Ia VO 1215/2012.
3. **Online-Adressrecherche**: `justizadressen.nrw.de` (PLZ/Ort) und bundesweit `justiz.de`; Quelle und Abrufdatum dokumentieren.
4. BeA-SAFE-ID: aus dem beA-Adressbuch zu ergänzen.

## Leitentscheidungen (Auswahl, siehe `references/rechtsprechung/INDEX.md`)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 25 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `klage-aus-eigenem-skill` | Kanzlei hat hauseigenes Klage-Plugin (klagewerkstatt-kanzlei) installiert und will damit Klagen aus eigenem Sachverhalt erstellen. Laufzeit-Variante Klagewerkstatt. Prüfraster: Sachverhalt Beklagtenadresse Zuständigkeit §§ 12 13 29 29c Z... |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | forderungsmanagement-klagewerkstatt: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprog... |
| `kompendium-02-workflow-mandantenko-bis-fmkw-mahnverfahren-b` | forderungsmanagement-klagewerkstatt: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-mandantenkommunikation, workflow-redteam-qualitygate, fmkw-mahnverfahren-bauleiter) und bewahrt deren Workflows, Normanker... |
| `kompendium-03-spezial-mahnverfahre-bis-forderung-aus-werkve` | forderungsmanagement-klagewerkstatt: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (spezial-mahnverfahren-beweislast-und-darlegungslast, spezial-zustaendigkeitspruefung-fristen-form-und-zustaendigkeit, forderung-aus... |
| `kompendium-04-bgb-zpo-forderungsno-bis-fmkw-titulierung-str` | forderungsmanagement-klagewerkstatt: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (bgb-zpo-forderungsnormcheck, fmkw-saumselig-streitig-erfahrung-spezial, fmkw-titulierung-streckung-leitfaden) und bewahrt deren Wor... |
| `kompendium-05-fmkw-verbraucherklag-bis-forderung-arzthonora` | forderungsmanagement-klagewerkstatt: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (fmkw-verbraucherklage-cookies-rdg-spezial, forderung-anwaltshonorar-rvg, forderung-arzthonorar-goae) und bewahrt deren Workflows, N... |
| `kompendium-06-forderung-gegen-gese-bis-forderung-im-ausland` | forderungsmanagement-klagewerkstatt: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (forderung-gegen-gesellschafter-13-gmbhg, forderung-gegen-insolventen-schuldner, forderung-im-ausland-vollstrecken) und bewahrt dere... |
| `kompendium-07-forderung-mietruckst-bis-forderung-zwangsvoll` | forderungsmanagement-klagewerkstatt: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (forderung-mietruckstand-zahlungsklage, forderung-verbraucher-erleichterungen, forderung-zwangsvollstreckung-ueberblick) und bewahrt... |
| `kompendium-08-forderungsmanagement-bis-klagevorlage-aus-eig` | forderungsmanagement-klagewerkstatt: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (forderungsmanagement-aufnahme, inkasso-zahlungsklage-ersteller, klagevorlage-aus-eigenen-mustern) und bewahrt deren Workflows, Norm... |
| `kompendium-09-mahnbescheid-online-bis-spezial-anspruchs-sc` | forderungsmanagement-klagewerkstatt: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (mahnbescheid-online-mb, mahnung-aussergerichtlich-stufenmodell, spezial-anspruchs-schriftsatz-brief-und-memo-bausteine) und bewahrt... |
| `kompendium-10-spezial-belegte-comp-bis-spezial-fmkw-mandant` | forderungsmanagement-klagewerkstatt: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (spezial-belegte-compliance-dokumentation-und-akte, spezial-faellige-zahlen-schwellen-und-berechnung, spezial-fmkw-mandantenkommunik... |
| `kompendium-11-spezial-forderungen-bis-spezial-gatekeeper-v` | forderungsmanagement-klagewerkstatt: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (spezial-forderungen-mehrparteien-konflikt-und-interessen, spezial-forderungsmanagement-tatbestand-beweis-und-belege, spezial-gateke... |
| `kompendium-12-spezial-inkasso-risi-bis-spezial-klagefreigab` | forderungsmanagement-klagewerkstatt: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (spezial-inkasso-risikoampel-und-gegenargumente, spezial-klage-formular-portal-und-einreichung, spezial-klagefreigabe-belegte-forder... |
| `kompendium-13-spezial-klagewerksta-bis-spezial-saumselig-so` | forderungsmanagement-klagewerkstatt: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (spezial-klagewerkstatt-erstpruefung-und-mandatsziel, spezial-mahnvorlauf-dokumentenmatrix-und-lueckenliste, spezial-saumselig-sonde... |
| `kompendium-14-spezial-werden-inter-bis-urkundenprozess-prue` | forderungsmanagement-klagewerkstatt: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (spezial-werden-internationaler-bezug-und-schnittstellen, spezial-zahlungsklage-behoerden-gericht-und-registerweg, urkundenprozess-p... |
| `kompendium-15-verjaehrung-pruefen-bis-zahlungsklage-erstel` | forderungsmanagement-klagewerkstatt: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (verjaehrung-pruefen, vollstreckungsbescheid-und-folgen, zahlungsklage-erstellen) und bewahrt deren Workflows, Normanker, Prüfprogra... |
| `kompendium-16-zinsberechnung-288-b-bis-zinsberechnung-288-b` | forderungsmanagement-klagewerkstatt: Konsolidiertes Skill-Kompendium 16; bündelt 1 frühere Spezialskills (zinsberechnung-288-bgb) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-freigegeben-red-team-und-qualitaetskontrolle` | Freigegeben: Red-Team und Qualitätskontrolle im Plugin forderungsmanagement klagewerkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-klare-livequellen-und-rechtsprechungscheck` | Klare: Livequellen- und Rechtsprechungscheck im Plugin forderungsmanagement klagewerkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin forderungsmanagement-klagewerkstatt: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin forderungsmanagement-klagewerkstatt: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin forderungsmanagement-klagewerkstatt: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin forderungsmanagement-klagewerkstatt: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin forderungsmanagement-klagewerkstatt: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin forderungsmanagement-klagewerkstatt: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
