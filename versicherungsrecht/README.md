# Versicherungsrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`versicherungsrecht`) | [`versicherungsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/versicherungsrecht.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

Großes, praxisnahes Versicherungsrecht-Plugin für Deckung, Ablehnung, Vertragsgestaltung, Aufsicht und Prozess. Es ist bewusst nicht nur ein Fachanwalts-Lernplugin, sondern ein Arbeitswerkzeug für Kanzlei, Rechtsabteilung, Versicherungsnehmer, Vermittler und Versicherer.

## Was dieses Plugin gut kann

- Deckungsablehnungen und Leistungsprüfung nach VVG zerlegen.
- Lebensversicherung, BU, PKV, Unfall, Rechtsschutz, Kreditversicherung, D&O, Cyber und Sachversicherung mit eigenen Spezial-Skills prüfen.
- BaFin, Ombudsmann, Klage und Vergleich taktisch voneinander trennen.
- Europäische Aufsicht, IDD, Solvency II, DORA und grenzüberschreitenden Vertrieb einordnen.

## Startlogik

Beginne mit dem allgemeinen Skill. Er fragt Rolle, Ziel, Fristen, Unterlagen, Eskalationsniveau und gewünschten Output ab. Danach schlägt er nur die Spezial-Skills vor, die zum Fall passen.

## Quellenhygiene

Normtexte werden aus amtlichen Quellen geprüft. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle verwendet. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. Nicht das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 64 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `betriebshaftpflicht-versicherungsfall-serienschaden` | Betriebshaftpflichtversicherung: Personen-/Sachschaden, Vermögensfolgeschaden, Serienschadenklausel, Nachhaftung, Ausschlüsse und Abwehrdeckung im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächs... |
| `betriebsunterbrechung-sachschaden-trigger` | Betriebsunterbrechungsversicherung: versicherter Sachschaden als Trigger, Unterbrechungsschaden, Mehrkosten, Unterversicherung, Kausalität und Zeitraum im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel u... |
| `bu-abstrakte-konkrete-verweisung` | Abstrakte/konkrete Verweisung in der BU: Lebensstellung, Ausbildung, Erfahrung, Einkommen, Arbeitsmarkt und tatsächliche Tätigkeit sauber prüfen im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und näch... |
| `bu-berufsbild-bu-nachpruefung-datenschutz` | Berufsunfähigkeitsversicherung: konkretes Berufsbild, prägende Tätigkeiten, Zeitanteile, gesundheitliche Einschränkungen und 50-Prozent-Grenze substantiiert darstellen im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoint... |
| `bu-nachpruefung-anerkenntnis-leistungseinstellung` | BU-Nachprüfung: Anerkenntnis, Gesundheitsverbesserung, Berufswechsel, Mitwirkung, Fristen, Beweislast und Angriff auf Leistungseinstellung im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem A... |
| `cyberversicherung-ransomware-d-o` | Cyberversicherung bei Ransomware, Datenabfluss, Betriebsunterbrechung, Lösegeld, Forensik, Sanktionsrecht, DORA/NIS2-Schnittstelle und Obliegenheiten im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und... |
| `d-o-claims-made-innenhaftung-43-gmbhg` | D&O-Versicherung: Claims-made-Prinzip, Pflichtverletzung, Innenhaftung, Ausschlüsse, Wissentlichkeit, Abwehrkosten und Side-A/B/C-Strukturen im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem... |
| `datenschutz-schweigepflicht-gesundheitsdaten` | Gesundheitsdaten im Versicherungsmandat: Schweigepflichtentbindung, DSGVO, Datensparsamkeit, Arztanfragen, Gutachter, PKV/BU/Unfall und Aktenführung im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und... |
| `deckungsprozess-vvg-rechtsabteilung` | Deckungsprozess gegen Versicherer: Anspruchsgrundlage, Klageantrag, örtliche Zuständigkeit § 215 VVG, Beweislast, Streitwert, Feststellungs-/Leistungsklage im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoamp... |
| `direktanspruch-pflichtversicherung-eiopa` | Direktanspruch gegen Haftpflichtversicherer: Pflichtversicherung, Geschädigter, Insolvenz, Kfz, Berufshaftpflicht, Deckungsgrenzen und Einwendungen im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und n... |
| `dora-cyber-abfindung-entschaedigungsquittung` | DORA-Compliance für Versicherer/Vermittler: IKT-Risikomanagement, Ausgliederung, Incident Reporting, Register of Information und Drittanbietersteuerung im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel u... |
| `eiopa-grenzueberschreitender-vertrieb` | Grenzüberschreitender Versicherungsvertrieb: Niederlassungs-/Dienstleistungsfreiheit, Host-/Home-Aufsicht, EIOPA, Passporting, Verbraucherbeschwerden und Sprach-/Informationspflichten im Versicherungsrecht. Liefert priorisierten Output m... |
| `elementarschaden-starkregen-ueberschwemmung` | Elementarschadenversicherung: Überschwemmung, Rückstau, Starkregen, Grundwasser, Erdrutsch, Ausschlüsse und technische Schadenursache im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeit... |
| `gewerbe-betriebsschliessung-infektionsschutz` | Betriebsschließungsversicherung: behördliche Verfügung, Krankheitserregerklauseln, dynamische/statische Verweisung, Teilschließung, Umsatzausfall und Vergleich im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risik... |
| `hausrat-einbruchdiebstahl-idd-vertrieb` | Hausratversicherung bei Einbruchdiebstahl, Raub, Trickdiebstahl, Wertsachen, Außenversicherung, Unterversicherung und Stehlgutliste im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitss... |
| `idd-vertrieb-beratung-dokumentation` | Versicherungsvertrieb: Beratungspflichten, Geeignetheit, Beratungsdokumentation, Provision, Makler/Vertreter, Onlineabschluss und Haftung im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Ar... |
| `internationales-versicherungsprogramm-master-local-policy` | Master Policy, Local Policy, admitted/non-admitted insurance, Claims Handling und internationale Deckungskoordination prüfen im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `kfz-haftpflicht-kasko-grobe-krankentagegeld` | Kfz-Haftpflichtversicherung: Außenregulierung, Innenregress, Obliegenheitsverletzung, Alkohol, Unfallflucht, Fahrerlaubnis und Regresshöchstgrenzen im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und n... |
| `kfz-kasko-grobe-fahrlaessigkeit-entwendung` | Kfz-Kaskoversicherung: Entwendung, Unfall, Wild, Alkohol, grobe Fahrlässigkeit, Obliegenheiten, Wiederbeschaffungswert und Sachverständigenstreit im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und näc... |
| `krankentagegeld-berufsunfaehigkeit-abgrenzung` | Krankentagegeldversicherung: Arbeitsunfähigkeit, Berufsunfähigkeit, Leistungseinstellung, Nachweis, PKV-Schnittstelle und existenzielle Liquidität im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nä... |
| `kreditausfallversicherung-warenkredit` | Kreditausfall-/Warenkreditversicherung: Limit, Forderungsausfall, Insolvenztatbestand, Obliegenheiten, Selbstbehalt, Factoring-Schnittstelle und Regress im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel... |
| `kreditversicherung-obliegenheiten-limit-pruefung` | Kreditversicherung im laufenden Debitorenmanagement: Limite, Überfälligkeiten, Risikoinformationen, Inkassostart, Meldungen und Streit um Leistungsfreiheit im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoamp... |
| `lebensversicherung-bezugsrecht-widerruf-aenderung` | Bezugsrechte in Lebens- und Rentenversicherung: widerruflich/unwiderruflich, Scheidung, Erbfall, Sicherungsabtretung, Insolvenz, Änderungserklärung und Auszahlungsstreit im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoi... |
| `lebensversicherung-rueckkaufswert` | Rückkaufswert, Abschlusskosten, Kündigung, Beitragsfreistellung und Altvertrags-Widerspruch in Lebens- und Rentenversicherung prüfen im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeits... |
| `lebensversicherung-ueberschussbeteiligung-bewertungsreserven` | Überschussbeteiligung, Schlussüberschuss, Bewertungsreserven und Informationsrechte in Lebensversicherung und Rentenversicherung verständlich prüfen im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und... |
| `nachhaltigkeit-taxonomie-sfdr-versicherungsprodukt` | Nachhaltigkeits- und ESG-Angaben bei Versicherungsanlageprodukten: Taxonomie, SFDR, Greenwashing, Produktfreigabe und Vertrieb im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `pkv-kostenerstattung-private` | PKV-Leistungsprüfung: medizinische Notwendigkeit, Gebührenrecht, Heilbehandlung, Hilfsmittel, Psychotherapie, Arzneimittel und Kürzungsschreiben im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und näch... |
| `private-krankenversicherung-beitragsanpassung-treuhaender` | Private Krankenversicherung: Beitragsanpassung, Treuhänder, Begründungsschreiben, Tarifwechsel, Auskunft und Rückforderungsrisiken prüfen im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Ar... |
| `produkthaftpflicht-rueckrufkosten` | Produkthaftpflichtversicherung: Produktfehler, Personenschaden, Rückruf, Austauschkosten, Rückrufkostenversicherung und internationale Lieferketten im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und n... |
| `rechtsabteilung-betriebsunterbrechung` | Rechtsabteilungs-Fachmodul für Betriebsunterbrechung und Lieferkettenausfall: Unterbrechungsschaden, Trigger, Wartezeit und Mitwirkung werden beweisbar gemacht. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption... |
| `rechtsabteilung-cyberversicherung-nach-ransomware` | Rechtsabteilungs-Fachmodul für Cyberversicherung nach Ransomware: Deckung, Anzeige, Forensik und Lösegeldklauseln werden als Krisenfahrplan geprüft. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Versicher... |
| `rechtsabteilung-d-umwelthaftpflicht` | Rechtsabteilungs-Fachmodul für D&O-Deckung bei Organhaftung: Notification, Serienschaden, Selbstbehalt und Ausschlüsse werden für Vorstand/AR bewertet. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Versic... |
| `rechtsabteilung-idd-vertrieb-und-provisionskonflikt` | Rechtsabteilungs-Fachmodul für IDD-Vertrieb und Provisionskonflikt: Produktvertrieb wird auf Interessenkonflikte, Dokumentation und Aufsicht geprüft. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Versiche... |
| `rechtsabteilung-rechtsschutzversicherung-im-massenverfahren` | Rechtsabteilungs-Fachmodul für Rechtsschutzversicherung im Massenverfahren: Deckungsanfrage, Stichentscheid und Erfolgsaussicht werden taktisch vorbereitet. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im V... |
| `rechtsschutz-deckungszusage-erfolgsaussicht` | Rechtsschutzversicherung: Deckungsanfrage, Erfolgsaussicht, Mutwilligkeit, Stichentscheid, Schiedsgutachten, Gebühren und Mandatskommunikation im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächst... |
| `rechtsschutz-erfolgsaussicht-mutwilligkeit` | Rechtsschutzversicherung: Ablehnung wegen fehlender Erfolgsaussicht oder Mutwilligkeit angreifen, ohne das Hauptmandat zu gefährden im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitss... |
| `rechtsschutz-vorvertraglichkeit-schadenereignis` | Rechtsschutzversicherung: zeitliche Einordnung des Rechtsschutzfalls, Dauerverstoß, Beratungsrechtsschutz, Wartezeit und Vorvertraglichkeit im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem... |
| `reiseversicherung-ruecktritt-abbruch-krankheit` | Reiserücktritts- und Reiseabbruchversicherung: unerwartete schwere Erkrankung, Stornozeitpunkt, Attest, Vorerkrankung, Pandemie, Angehörige und Kreditkartenversicherung im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoin... |
| `restschuldversicherung-widerruf` | Restschuldversicherung bei Verbraucherdarlehen: Kopplung, Widerruf, Beratung, Kosten, Arbeitslosigkeit/Arbeitsunfähigkeit/Tod und Bankvertrieb prüfen im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und... |
| `rueckversicherung-cut-through-und-fronting` | Rückversicherung, Fronting-Strukturen, Captives, Cut-through-Klauseln und Insolvenzrisiken rechtlich einordnen im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `sachverstaendigenverfahren-versicherung` | Sachverständigenverfahren: Obmann, Gutachterauftrag, Bindungswirkung, Kosten, Beweiswert und Schnittstelle zum Prozess im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `solvency-ii-scr-orsa-aufsichtsrecht` | Solvency-II-Aufsichtsrahmen: Eigenmittel, SCR/MCR, ORSA, Governance, Ausgliederung und BaFin-Kommunikation für Versicherer und Gruppen im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbei... |
| `subrogation-regress-transportversicherung` | Legalzession und Regress des Versicherers: Forderungsübergang, Quotenvorrecht, Beweissicherung, Vergleich, Regressabwehr und Verjährung im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbe... |
| `transportversicherung-ware-lagerung` | Transportversicherung: Güterschaden, Verlust, Lagerung, Incoterms, multimodaler Transport, Regress gegen Frachtführer und Versicherungswert im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem... |
| `umwelthaftpflicht-umweltschadenversicherung` | Umwelthaftpflichtversicherung und Umweltschadenversicherung: Kontamination, Sanierung, öffentlich-rechtliche Verfügung, Eigenschaden, Drittanspruch und Ausschlüsse im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, R... |
| `unfallversicherung-invaliditaet-vers` | Private Unfallversicherung: Unfallbegriff, Invalidität, ärztliche Feststellung, Fristen, Gliedertaxe, Mitwirkung von Krankheiten und Progression im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und näch... |
| `vag-bafin-aufsicht-beschwerde-missstand` | Versicherungsaufsicht nach VAG: BaFin-Beschwerde, Missstandsaufsicht, Produkt-/Vertriebsaufsicht, Solvabilität, Verbraucherschutz und Grenzen individueller Leistungserzwingung im Versicherungsrecht. Liefert priorisierten Output mit Norm-... |
| `vergleich-abfindung-entschaedigungsquittung` | Vergleich mit Versicherern: Abfindungserklärung, Erledigungsklausel, Nachschäden, Regress, Steuer, Kosten und Widerruf/Anfechtung im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitssch... |
| `vers-deckungsablehnung-redteam` | Deckungsablehnung des Versicherers zerlegen: Risikoausschluss, Obliegenheit, Kausalität, grobe Fahrlässigkeit, Arglist, Beweislast und Vergleichsfenster systematisch prüfen. |
| `vers-dokumentenintake-police-avb-nachtraege` | Dokumentenintake für Versicherungsakten: Versicherungsschein, AVB, Nachträge, Beratungsdokumentation, Schadenanzeige, Gutachten, Korrespondenz und Ablehnung in eine Aktenmatrix überführen. |
| `vers-fristen-verjaehrung-klagefrist-fallkalender` | Fristen und Ausschlussrisiken im Versicherungsrecht: Fälligkeit, Hemmung, Verjährung, Obliegenheitsfristen, Nachprüfungsfristen, Gutachtenfristen und prozessuale Termine sicher verwalten im Versicherungsrecht. Liefert priorisierten Outpu... |
| `vers-kaltstart-routing` | Allgemeiner Einstieg ins Versicherungsrecht: Police, Bedingungen, Schadenereignis, Ablehnung, Fristen, Aufsicht, Ombudsmann und Klageweg strukturiert erfassen und passende Fachmodule vorschlagen. |
| `vers-ombudsmann-versicherungsbetrug` | Eskalationsrouting im Versicherungsrecht: Versicherungsombudsmann, PKV-Ombudsmann, BaFin-Beschwerde, Deckungsklage, einstweiliger Rechtsschutz und Vergleichsdruck sauber unterscheiden im Versicherungsrecht. Liefert priorisierten Output m... |
| `versicherungsbetrug-verdachtsfall-kooperation-strafrecht` | Versicherungsrechtlicher Umgang mit Betrugsverdacht: Auskunft, Leistungsprüfung, Strafanzeige, Datenschutz, Zivilprozess und Verteidigungsrisiken im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und näc... |
| `versicherungsmakler-haftung-deckungsluecke` | Maklerhaftung wegen fehlerhafter Risikoanalyse, unzureichender Beratung, fehlender Umdeckung oder Deckungslücke prüfen im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `versicherungsprodukt-agb-betriebshaftpflicht` | AVB-Klauseln nach Transparenz, Überraschung, unangemessener Benachteiligung und VVG-Leitbild prüfen im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `versicherungssumme-unterversicherung-taxwert` | Versicherungssumme, Unterversicherung, gleitender Neuwert, Taxe, Summenausgleich und Vorsorgeversicherung prüfen im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `vvg-anzeigepflicht-ruecktritt-arglist` | § 19 VVG in Leben, BU, PKV und Unfallversicherung: Gesundheitsfragen, Kenntnis, Kausalität, Rücktritt, Kündigung, Vertragsanpassung, Arglist und Belehrungsfehler prüfen im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoin... |
| `vvg-arglist-taeuschung-anfechtung` | Arglistanfechtung nach § 22 VVG/BGB § 123: Gesundheitsangaben, Schadenhergang, Vorschäden, subjektives Element, Indizien und Gegenbeweis im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arb... |
| `vvg-falligkeit-14-abschlagszahlung` | Fälligkeit des Versicherungsanspruchs, Ermittlungsdauer, Abschlagszahlung, Verzug und taktische Beschleunigung bei großen Schäden im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitssch... |
| `vvg-gefahrerhoehung-mehrfachversicherung` | Gefahrerhöhung vor und nach Vertragsschluss: willentlich/unwillentlich, Anzeige, Kündigung, Leistungsfreiheit und Kausalitätsprüfung in Sach-, Haftpflicht- und Personenversicherungen im Versicherungsrecht. Liefert priorisierten Output mi... |
| `vvg-obliegenheit-28-quotelung-kausalitaet` | § 28 VVG nach Eintritt des Versicherungsfalls: Anzeige, Aufklärung, Rettung, Mitwirkung, Kausalitätsgegenbeweis, Vorsatz/grobe Fahrlässigkeit und Quotierung im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoam... |
| `vvg-versicherung-wohngebaeude-leitungswasser` | Versicherung für fremde Rechnung: wer darf Leistung verlangen, wem stehen Einwendungen entgegen, welche Rolle haben Sicherungsnehmer, Leasinggeber, Mieter, Subunternehmer und Konzernunternehmen? im Versicherungsrecht. Liefert priorisiert... |
| `wohngebaeude-leitungswasser-sturm-hagel-brand` | Wohngebäudeversicherung: Leitungswasser, Sturm/Hagel, Brand, Elementarschaden, grobe Fahrlässigkeit, Obliegenheiten und Sanierungskosten im Versicherungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arb... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
