# selbstvertreter-amtsgericht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`selbstvertreter-amtsgericht`) | [`selbstvertreter-amtsgericht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/selbstvertreter-amtsgericht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Selbstvertreter Amtsgericht — Küchentisch Kaufpreis** (`selbstvertreter-amtsgericht-kuechentisch-kaufpreis`) | [Gesamt-PDF lesen](../testakten/selbstvertreter-amtsgericht-kuechentisch-kaufpreis/gesamt-pdf/selbstvertreter-amtsgericht-kuechentisch-kaufpreis_gesamt.pdf) | [`testakte-selbstvertreter-amtsgericht-kuechentisch-kaufpreis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-selbstvertreter-amtsgericht-kuechentisch-kaufpreis.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

## Für wen?

- Sie wollen eine Geldforderung bis zur Wertgrenze des § 23 Nr. 1 GVG einklagen (seit 01.01.2026: **10.000 EUR**, Anhebung von 5.000 EUR durch das Justizstandort-Stärkungsgesetz).
- Sie sind verklagt worden und wollen sich selbst verteidigen.
- Sie wollen Mietsachen, Reisemängel, Familienunterhalt oder andere AG-typische Streitigkeiten betreiben.
- Sie wollen vor einer möglichen Mandatierung verstehen, was rechtlich passiert.

## Was kann das Plugin?

Es liefert Skills zu:

- **Anfänger-Workflow**: geführter Modus mit kleinen Schritten, einfacher Sprache, Frist zuerst und klarer nächster Handlung.
- **Sanity-Check**: letzte Ampelprüfung vor Klage, Klageerwiderung, Replik, Termin, Vergleich oder Rechtsmittel.
- **Rechtsprechungschat**: Rechtsprechung finden, verstehen, nicht überdehnen und gerichtstauglich zitieren.
- **Zulassungsgrenzen-Check**: AG/LG-Zuständigkeit, § 23 GVG, § 495a ZPO, § 511 ZPO, Berufung und Anwaltszwang.
- **Zuständigkeit**: Sachlich (§ 23 GVG, § 23a-c GVG), örtlich (§§ 12 ff. ZPO), Verbrauchergerichtsstand (§ 29c ZPO).
- **Vor-Klage-Vorbereitung**: Erfolgsaussichten-Check, Anspruchsgrundlage finden, Verjährung prüfen, außergerichtliche Mahnung, Mahnverfahren, Beweismittel sammeln, Kostenrisiko berechnen.
- **Klageschrift erstellen**: Pflichtbestandteile, bestimmter Antrag, Tatsachenvortrag, Beweisangebote, Anlagen, Streitwert, vereinfachtes Verfahren § 495a ZPO.
- **Einreichung**: Mein Justizpostfach (MJP), § 130a ZPO elektronisch, Papierform, Fax-Grenzen, Rechtsantragsstelle, Versand durch Dritte (Risiko!), Gerichtskostenvorschuss.
- **PKH und Beratungshilfe**: Antrag, Ablehnung, Ratenzahlung, Beratungshilfe vor Klage.
- **Klageerwiderung**: Fristen, Checkliste, substantiiertes Bestreiten, Einreden, Widerklage, Säumnis vermeiden.
- **Replik, Duplik, Hinweise nach § 139 ZPO**, nachgereichter Schriftsatz, Wiedereinsetzung.
- **Beweis**: Beweislast, Zeuge, Urkunde, Sachverständiger, Augenschein, Parteivernehmung, eidesstattliche Versicherung, Folgen fehlenden Beweises.
- **Termin**: Ladung, Vorbereitung, Säumnis im Termin, Verhalten im Saal, Vergleich nach § 278 II ZPO.
- **Fristen**: Berechnung, eigenes Fristenbuch, Zustellung als Fristbeginn, Fristverlängerung.
- **Urteil und Rechtsmittel**: Verkündung, Urteilsprüfung, Berufung zum LG (Wertgrenze § 511 ZPO), Zulassung bei niedrigem Streitwert, Rechtsmittelfrist.
- **Vollstreckung-Querverweise**: Rechtskraft, Vollstreckungsklausel, Verweis auf separaten Substitutionsagenten für die Zwangsvollstreckung.
- **Spezielles**: Video-Verhandlung § 128a ZPO, Dolmetscher § 185 GVG, Kostenfestsetzung, typische Laien-Fehler, wann es sich lohnt, doch einen Anwalt einzuschalten.

## Sprache und Ton

- Sie-Form. Einfache, klare Sätze. Fachbegriffe werden beim ersten Vorkommen in einer Skill in 1-2 Sätzen erklärt.
- Direkte Schritt-fuer-Schritt-Anleitungen.
- Ehrlicher Hinweis, wo verifiziert werden muss (Reform-Lage, Aktenzeichen, Fundstellen).

## Was das Plugin **nicht** macht

- Keine Garantie, dass Sie gewinnen.
- Keine anwaltliche Mandatsführung. Bei komplexen Fällen, hohem Risiko, Landgericht, Familiengericht, Berufung oder unklarer Zustellung empfiehlt das Plugin deutlich Rechtsantragsstelle, Beratungshilfe, PKH oder Anwalt — siehe Skill `wann-doch-anwalt-grenzfaelle`.
- Keine Zwangsvollstreckung. Dafür existiert ein separater Substitutionsagent.

## Einstieg

Starten Sie mit `anfaenger-workflow-amtsgericht`, wenn Sie geführt werden möchten. Nutzen Sie `orientierung-selbstvertreter-amtsgericht`, wenn Sie nur eine schnelle Triage wollen, und `sanity-check-selbstvertretung-amtsgericht`, bevor etwas an das Gericht geht.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 30 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Selbstvertreter-Amtsgericht-Plugin. Fragt Erfahrungslevel, Rolle, Ziel, Fristen, Streitwert, Gericht, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Pl... |
| `kompendium-01-anfaenger-workflow-a-bis-fristbeginn-zustellu` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (anfaenger-workflow-amtsgericht, rechtsprechungschat-amtsgericht, fristbeginn-zustellung-protokollieren) und bewahrt deren Workflows, Norman... |
| `kompendium-02-fristen-berechnen-18-bis-fristverlaengerung-a` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (fristen-berechnen-187-188-bgb, fristen-buch-fuehren-laien, fristverlaengerung-antrag-225-zpo) und bewahrt deren Workflows, Normanker, Prüfp... |
| `kompendium-03-klage-vereinfachtes-bis-mahnverfahren-688-ff` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (klage-vereinfachtes-verfahren-495a-zpo, klageerwiderung-fristen-274-zpo, mahnverfahren-688-ff-zpo-vor-klage) und bewahrt deren Workflows, N... |
| `kompendium-04-oertliche-zustaendig-bis-rechtsmittelfrist-51` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (oertliche-zustaendigkeit-12-37-zpo, online-verfahren-11-buch-zpo-experimentell, rechtsmittelfrist-517-zpo) und bewahrt deren Workflows, Nor... |
| `kompendium-05-sachliche-zustaendig-bis-wiedereinsetzung-fri` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (sachliche-zustaendigkeit-amtsgericht-23-gvg, verjaehrungsfrist-pruefen-195-bgb, wiedereinsetzung-frist-233-zpo) und bewahrt deren Workflows... |
| `kompendium-06-vollstreckungsklause-bis-anlagen-formatieren` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (vollstreckungsklausel-724-zpo, einreichung-papierform-mit-abschriften, anlagen-formatieren-k1-k2-pdf-amtsgericht) und bewahrt deren Workflo... |
| `kompendium-07-anspruchsgrundlage-f-bis-augenscheinsbeweis-3` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (anspruchsgrundlage-finden-laienhilfe, anwaltszwang-pruefen-78-zpo, augenscheinsbeweis-371-zpo) und bewahrt deren Workflows, Normanker, Prüf... |
| `kompendium-08-ausnahmen-streitwert-bis-beratungshilfe-ausse` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (ausnahmen-streitwertgrenze-23-nr-2-gvg, aussergerichtliche-mahnung-286-bgb, beratungshilfe-aussergerichtlich-brh) und bewahrt deren Workflo... |
| `kompendium-09-berufung-amtsgericht-bis-beweislast-grundrege` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (berufung-amtsgericht-511-zpo, berufungs-zulassung-niedrig-streitwert, beweislast-grundregel-wer-was) und bewahrt deren Workflows, Normanker... |
| `kompendium-10-beweismittel-vorab-s-bis-dolmetscher-185-gvg` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (beweismittel-vorab-sammeln-checkliste, dokumenten-erzeugung-pdf-laien-amtsgericht, dolmetscher-185-gvg) und bewahrt deren Workflows, Norman... |
| `kompendium-11-duplik-nach-replik-bis-einreden-aktiv-gelte` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (duplik-nach-replik, eidesstattliche-versicherung-294-zpo, einreden-aktiv-geltend-machen) und bewahrt deren Workflows, Normanker, Prüfprogra... |
| `kompendium-12-einreichung-130a-zpo-bis-einreichung-mein-jus` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (einreichung-130a-zpo-elektronisch-buerger, einreichung-fax-und-grenzen, einreichung-mein-justizpostfach-mjp-2024) und bewahrt deren Workflo... |
| `kompendium-13-einreichung-rechtsan-bis-gerichtskostenvorsch` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (einreichung-rechtsantragsstelle-selbst, gegnerische-vollstreckung-abwehr, gerichtskostenvorschuss-12-gkg) und bewahrt deren Workflows, Norm... |
| `kompendium-14-kein-beweis-folgen-l-bis-klage-zusammenstelle` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (kein-beweis-folgen-laienwarnung, klage-streitwert-angabe-3-zpo, klage-zusammenstellen-komplettes-bundle-amtsgericht) und bewahrt deren Work... |
| `kompendium-15-klageerwiderung-chec-bis-klageschrift-anlagen` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (klageerwiderung-checkliste-alle-punkte, klageerwiderung-replik-anlagen-b1-b2-fortlaufend, klageschrift-anlagen-bezeichnen) und bewahrt dere... |
| `kompendium-16-klageschrift-anschre-bis-klageschrift-beweisa` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 16; bündelt 3 frühere Spezialskills (klageschrift-anschreiben-an-gericht-laien, klageschrift-antrag-bestimmt-formulieren, klageschrift-beweisangebote-einbauen-373-zpo) und bewa... |
| `kompendium-17-klageschrift-pflicht-bis-kostenfestsetzung-10` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 17; bündelt 3 frühere Spezialskills (klageschrift-pflichtbestandteile-253-zpo, klageschrift-tatsachenvortrag-strukturieren, kostenfestsetzung-103-104-zpo) und bewahrt deren Wor... |
| `kompendium-18-kostenrisiko-streitw-bis-muendliche-verhandlu` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 18; bündelt 3 frühere Spezialskills (kostenrisiko-streitwert-berechnen-gkg, ladung-termin-216-zpo, muendliche-verhandlung-akten-griffbereit) und bewahrt deren Workflows, Norman... |
| `kompendium-19-nachgereichter-schri-bis-parteivernehmung-445` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 19; bündelt 3 frühere Spezialskills (nachgereichter-schriftsatz-296a-zpo, orientierung-selbstvertreter-amtsgericht, parteivernehmung-445-ff-zpo) und bewahrt deren Workflows, No... |
| `kompendium-20-pkh-bewilligung-able-bis-prozesskostenhilfe-p` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 20; bündelt 3 frühere Spezialskills (pkh-bewilligung-ablehnung-folgen, pkh-ratenzahlung-bewilligung, prozesskostenhilfe-pkh-114-zpo) und bewahrt deren Workflows, Normanker, Prü... |
| `kompendium-21-replik-auf-klageerwi-bis-sachverstaendigenbew` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 21; bündelt 3 frühere Spezialskills (replik-auf-klageerwiderung-systematik, richterlicher-hinweis-139-zpo-reaktion, sachverstaendigenbeweis-402-zpo) und bewahrt deren Workflows... |
| `kompendium-22-saeumnis-im-termin-3-bis-sanity-check-selbstv` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 22; bündelt 3 frühere Spezialskills (saeumnis-im-termin-330-zpo, saeumnis-vermeiden-330-ff-zpo, sanity-check-selbstvertretung-amtsgericht) und bewahrt deren Workflows, Normanke... |
| `kompendium-23-substantiiertes-best-bis-terminvorbereitung-c` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 23; bündelt 3 frühere Spezialskills (substantiiertes-bestreiten-138-iv-zpo, tatbestand-zerlegen-anspruchspruefung-laien, terminvorbereitung-checkliste) und bewahrt deren Workfl... |
| `kompendium-24-typische-laien-fehle-bis-urteil-pruefen-313-z` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 24; bündelt 3 frühere Spezialskills (typische-laien-fehler, urkundenbeweis-415-ff-zpo, urteil-pruefen-313-zpo) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabe... |
| `kompendium-25-urteil-rechtskraft-7-bis-verbrauchergerichtss` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 25; bündelt 3 frühere Spezialskills (urteil-rechtskraft-705-zpo, urteilsverkuendung-310-zpo, verbrauchergerichtsstand-29c-zpo) und bewahrt deren Workflows, Normanker, Prüfprogr... |
| `kompendium-26-vergleich-richtervor-bis-video-verhandlung-12` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 26; bündelt 3 frühere Spezialskills (vergleich-richtervorschlag-278-ii-zpo, verhalten-gerichtssaal-laienleitfaden, video-verhandlung-128a-zpo) und bewahrt deren Workflows, Norm... |
| `kompendium-27-vorabklaerung-erfolg-bis-widerklage-33-zpo` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 27; bündelt 3 frühere Spezialskills (vorabklaerung-erfolgsaussichten-selbstcheck, wann-doch-anwalt-grenzfaelle, widerklage-33-zpo) und bewahrt deren Workflows, Normanker, Prüfp... |
| `kompendium-28-zeugenbeweis-373-ff-bis-zurechnungsproblem-v` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 28; bündelt 3 frühere Spezialskills (zeugenbeweis-373-ff-zpo, zulassungsgrenzen-check-amtsgericht, zurechnungsproblem-versand-durch-dritte) und bewahrt deren Workflows, Normank... |
| `kompendium-29-zwangsvollstreckung-bis-zwangsvollstreckung` | selbstvertreter-amtsgericht: Konsolidiertes Skill-Kompendium 29; bündelt 1 frühere Spezialskills (zwangsvollstreckung-querverweis-substitutionsagent) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
