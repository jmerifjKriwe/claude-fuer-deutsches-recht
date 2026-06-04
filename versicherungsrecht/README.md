# Versicherungsrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`versicherungsrecht`) | [`versicherungsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/versicherungsrecht.zip) |

### Demonstrations-Akten

Dieses Plugin hat derzeit keine eigene Demonstrations-Akte. Es arbeitet mit hochgeladenen Policen, Bescheiden, Verträgen, Messprotokollen, Behördenbriefen und Aktenauszügen.

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

Automatisch generierte Komplett-Liste aller 60 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `betriebshaftpflicht-versicherungsfall-serienschaden` | Betriebshaftpflichtversicherung: Personen-/Sachschaden, Vermögensfolgeschaden, Serienschadenklausel, Nachhaftung, Ausschlüsse und Abwehrdeckung. |
| `betriebsunterbrechung-sachschaden-trigger` | Betriebsunterbrechungsversicherung: versicherter Sachschaden als Trigger, Unterbrechungsschaden, Mehrkosten, Unterversicherung, Kausalität und Zeitraum. |
| `bu-abstrakte-konkrete-verweisung` | Abstrakte/konkrete Verweisung in der BU: Lebensstellung, Ausbildung, Erfahrung, Einkommen, Arbeitsmarkt und tatsächliche Tätigkeit sauber prüfen. |
| `bu-berufsbild-50-prozent-substantiierung` | Berufsunfähigkeitsversicherung: konkretes Berufsbild, prägende Tätigkeiten, Zeitanteile, gesundheitliche Einschränkungen und 50-Prozent-Grenze substantiiert darstellen. |
| `bu-nachpruefung-anerkenntnis-leistungseinstellung` | BU-Nachprüfung: Anerkenntnis, Gesundheitsverbesserung, Berufswechsel, Mitwirkung, Fristen, Beweislast und Angriff auf Leistungseinstellung. |
| `cyberversicherung-ransomware-sanktionsrecht` | Cyberversicherung bei Ransomware, Datenabfluss, Betriebsunterbrechung, Lösegeld, Forensik, Sanktionsrecht, DORA/NIS2-Schnittstelle und Obliegenheiten. |
| `d-o-claims-made-innenhaftung-43-gmbhg` | D&O-Versicherung: Claims-made-Prinzip, Pflichtverletzung, Innenhaftung, Ausschlüsse, Wissentlichkeit, Abwehrkosten und Side-A/B/C-Strukturen. |
| `datenschutz-schweigepflicht-gesundheitsdaten` | Gesundheitsdaten im Versicherungsmandat: Schweigepflichtentbindung, DSGVO, Datensparsamkeit, Arztanfragen, Gutachter, PKV/BU/Unfall und Aktenführung. |
| `deckungsprozess-zustaendigkeit-215-vvg` | Deckungsprozess gegen Versicherer: Anspruchsgrundlage, Klageantrag, örtliche Zuständigkeit § 215 VVG, Beweislast, Streitwert, Feststellungs-/Leistungsklage. |
| `direktanspruch-pflichtversicherung-115-vvg` | Direktanspruch gegen Haftpflichtversicherer: Pflichtversicherung, Geschädigter, Insolvenz, Kfz, Berufshaftpflicht, Deckungsgrenzen und Einwendungen. |
| `dora-cyber-ikt-versicherer` | DORA-Compliance für Versicherer/Vermittler: IKT-Risikomanagement, Ausgliederung, Incident Reporting, Register of Information und Drittanbietersteuerung. |
| `eiopa-grenzueberschreitender-vertrieb` | Grenzüberschreitender Versicherungsvertrieb: Niederlassungs-/Dienstleistungsfreiheit, Host-/Home-Aufsicht, EIOPA, Passporting, Verbraucherbeschwerden und Sprach-/Informationspflichten. |
| `elementarschaden-starkregen-ueberschwemmung` | Elementarschadenversicherung: Überschwemmung, Rückstau, Starkregen, Grundwasser, Erdrutsch, Ausschlüsse und technische Schadenursache. |
| `gewerbe-betriebsschliessung-infektionsschutz` | Betriebsschließungsversicherung: behördliche Verfügung, Krankheitserregerklauseln, dynamische/statische Verweisung, Teilschließung, Umsatzausfall und Vergleich. |
| `hausrat-einbruchdiebstahl-entschaedigungsgrenze` | Hausratversicherung bei Einbruchdiebstahl, Raub, Trickdiebstahl, Wertsachen, Außenversicherung, Unterversicherung und Stehlgutliste. |
| `idd-vertrieb-beratung-dokumentation` | Versicherungsvertrieb: Beratungspflichten, Geeignetheit, Beratungsdokumentation, Provision, Makler/Vertreter, Onlineabschluss und Haftung. |
| `internationales-versicherungsprogramm-master-local-policy` | Master Policy, Local Policy, admitted/non-admitted insurance, Claims Handling und internationale Deckungskoordination prüfen. |
| `kfz-haftpflicht-regress-alkohol-flucht` | Kfz-Haftpflichtversicherung: Außenregulierung, Innenregress, Obliegenheitsverletzung, Alkohol, Unfallflucht, Fahrerlaubnis und Regresshöchstgrenzen. |
| `kfz-kasko-grobe-fahrlaessigkeit-entwendung` | Kfz-Kaskoversicherung: Entwendung, Unfall, Wild, Alkohol, grobe Fahrlässigkeit, Obliegenheiten, Wiederbeschaffungswert und Sachverständigenstreit. |
| `krankentagegeld-berufsunfaehigkeit-abgrenzung` | Krankentagegeldversicherung: Arbeitsunfähigkeit, Berufsunfähigkeit, Leistungseinstellung, Nachweis, PKV-Schnittstelle und existenzielle Liquidität. |
| `kreditausfallversicherung-warenkredit-forderungsausfall` | Kreditausfall-/Warenkreditversicherung: Limit, Forderungsausfall, Insolvenztatbestand, Obliegenheiten, Selbstbehalt, Factoring-Schnittstelle und Regress. |
| `kreditversicherung-obliegenheiten-limit-pruefung` | Kreditversicherung im laufenden Debitorenmanagement: Limite, Überfälligkeiten, Risikoinformationen, Inkassostart, Meldungen und Streit um Leistungsfreiheit. |
| `lebensversicherung-bezugsrecht-widerruf-aenderung` | Bezugsrechte in Lebens- und Rentenversicherung: widerruflich/unwiderruflich, Scheidung, Erbfall, Sicherungsabtretung, Insolvenz, Änderungserklärung und Auszahlungsstreit. |
| `lebensversicherung-rueckkaufswert-abschlusskosten-widerspruch` | Rückkaufswert, Abschlusskosten, Kündigung, Beitragsfreistellung und Altvertrags-Widerspruch in Lebens- und Rentenversicherung prüfen. |
| `lebensversicherung-ueberschussbeteiligung-bewertungsreserven` | Überschussbeteiligung, Schlussüberschuss, Bewertungsreserven und Informationsrechte in Lebensversicherung und Rentenversicherung verständlich prüfen. |
| `nachhaltigkeit-taxonomie-sfdr-versicherungsprodukt` | Nachhaltigkeits- und ESG-Angaben bei Versicherungsanlageprodukten: Taxonomie, SFDR, Greenwashing, Produktfreigabe und Vertrieb. |
| `private-krankenversicherung-beitragsanpassung-treuhaender` | Private Krankenversicherung: Beitragsanpassung, Treuhänder, Begründungsschreiben, Tarifwechsel, Auskunft und Rückforderungsrisiken prüfen. |
| `pkv-kostenerstattung-medizinische-notwendigkeit` | PKV-Leistungsprüfung: medizinische Notwendigkeit, Gebührenrecht, Heilbehandlung, Hilfsmittel, Psychotherapie, Arzneimittel und Kürzungsschreiben. |
| `produkthaftpflicht-rueckrufkosten` | Produkthaftpflichtversicherung: Produktfehler, Personenschaden, Rückruf, Austauschkosten, Rückrufkostenversicherung und internationale Lieferketten. |
| `rechtsschutz-deckungszusage-stichentscheid` | Rechtsschutzversicherung: Deckungsanfrage, Erfolgsaussicht, Mutwilligkeit, Stichentscheid, Schiedsgutachten, Gebühren und Mandatskommunikation. |
| `rechtsschutz-erfolgsaussicht-mutwilligkeit` | Rechtsschutzversicherung: Ablehnung wegen fehlender Erfolgsaussicht oder Mutwilligkeit angreifen, ohne das Hauptmandat zu gefährden. |
| `rechtsschutz-vorvertraglichkeit-schadenereignis` | Rechtsschutzversicherung: zeitliche Einordnung des Rechtsschutzfalls, Dauerverstoß, Beratungsrechtsschutz, Wartezeit und Vorvertraglichkeit. |
| `reiseversicherung-ruecktritt-abbruch-krankheit` | Reiserücktritts- und Reiseabbruchversicherung: unerwartete schwere Erkrankung, Stornozeitpunkt, Attest, Vorerkrankung, Pandemie, Angehörige und Kreditkartenversicherung. |
| `restschuldversicherung-widerruf-kopplung-verbraucherdarlehen` | Restschuldversicherung bei Verbraucherdarlehen: Kopplung, Widerruf, Beratung, Kosten, Arbeitslosigkeit/Arbeitsunfähigkeit/Tod und Bankvertrieb prüfen. |
| `rueckversicherung-cut-through-und-fronting` | Rückversicherung, Fronting-Strukturen, Captives, Cut-through-Klauseln und Insolvenzrisiken rechtlich einordnen. |
| `sachverstaendigenverfahren-versicherung` | Sachverständigenverfahren: Obmann, Gutachterauftrag, Bindungswirkung, Kosten, Beweiswert und Schnittstelle zum Prozess. |
| `solvency-ii-scr-orsa-aufsichtsrecht` | Solvency-II-Aufsichtsrahmen: Eigenmittel, SCR/MCR, ORSA, Governance, Ausgliederung und BaFin-Kommunikation für Versicherer und Gruppen. |
| `subrogation-regress-86-vvg` | Legalzession und Regress des Versicherers: Forderungsübergang, Quotenvorrecht, Beweissicherung, Vergleich, Regressabwehr und Verjährung. |
| `transportversicherung-ware-lagerung` | Transportversicherung: Güterschaden, Verlust, Lagerung, Incoterms, multimodaler Transport, Regress gegen Frachtführer und Versicherungswert. |
| `umwelthaftpflicht-umweltschadenversicherung` | Umwelthaftpflichtversicherung und Umweltschadenversicherung: Kontamination, Sanierung, öffentlich-rechtliche Verfügung, Eigenschaden, Drittanspruch und Ausschlüsse. |
| `unfallversicherung-invaliditaet-fristen-gliedertaxe` | Private Unfallversicherung: Unfallbegriff, Invalidität, ärztliche Feststellung, Fristen, Gliedertaxe, Mitwirkung von Krankheiten und Progression. |
| `vag-bafin-aufsicht-beschwerde-missstand` | Versicherungsaufsicht nach VAG: BaFin-Beschwerde, Missstandsaufsicht, Produkt-/Vertriebsaufsicht, Solvabilität, Verbraucherschutz und Grenzen individueller Leistungserzwingung. |
| `vergleich-abfindung-entschaedigungsquittung` | Vergleich mit Versicherern: Abfindungserklärung, Erledigungsklausel, Nachschäden, Regress, Steuer, Kosten und Widerruf/Anfechtung. |
| `vers-allgemeiner-kaltstart` | Allgemeiner Einstieg ins Versicherungsrecht: Police, Bedingungen, Schadenereignis, Ablehnung, Fristen, Aufsicht, Ombudsmann und Klageweg strukturiert erfassen und passende Spezial-Skills vorschlagen. |
| `vers-deckungsablehnung-redteam` | Deckungsablehnung des Versicherers zerlegen: Risikoausschluss, Obliegenheit, Kausalität, grobe Fahrlässigkeit, Arglist, Beweislast und Vergleichsfenster systematisch prüfen. |
| `vers-dokumentenintake-police-avb-nachtraege` | Dokumentenintake für Versicherungsakten: Versicherungsschein, AVB, Nachträge, Beratungsdokumentation, Schadenanzeige, Gutachten, Korrespondenz und Ablehnung in eine Aktenmatrix überführen. |
| `vers-fristen-verjaehrung-klagefrist-fallkalender` | Fristen und Ausschlussrisiken im Versicherungsrecht: Fälligkeit, Hemmung, Verjährung, Obliegenheitsfristen, Nachprüfungsfristen, Gutachtenfristen und prozessuale Termine sicher verwalten. |
| `vers-ombudsmann-bafin-beschwerde-klageweg` | Eskalationsrouting im Versicherungsrecht: Versicherungsombudsmann, PKV-Ombudsmann, BaFin-Beschwerde, Deckungsklage, einstweiliger Rechtsschutz und Vergleichsdruck sauber unterscheiden. |
| `versicherungsbetrug-verdachtsfall-kooperation-strafrecht` | Versicherungsrechtlicher Umgang mit Betrugsverdacht: Auskunft, Leistungsprüfung, Strafanzeige, Datenschutz, Zivilprozess und Verteidigungsrisiken. |
| `versicherungsmakler-haftung-deckungsluecke` | Maklerhaftung wegen fehlerhafter Risikoanalyse, unzureichender Beratung, fehlender Umdeckung oder Deckungslücke prüfen. |
| `versicherungsprodukt-agb-klauselkontrolle` | AVB-Klauseln nach Transparenz, Überraschung, unangemessener Benachteiligung und VVG-Leitbild prüfen. |
| `versicherungssumme-unterversicherung-taxwert` | Versicherungssumme, Unterversicherung, gleitender Neuwert, Taxe, Summenausgleich und Vorsorgeversicherung prüfen. |
| `vvg-anzeigepflicht-19-ruecktritt-kuendigung-anpassung` | § 19 VVG in Leben, BU, PKV und Unfallversicherung: Gesundheitsfragen, Kenntnis, Kausalität, Rücktritt, Kündigung, Vertragsanpassung, Arglist und Belehrungsfehler prüfen. |
| `vvg-arglist-taeuschung-anfechtung` | Arglistanfechtung nach § 22 VVG/BGB § 123: Gesundheitsangaben, Schadenhergang, Vorschäden, subjektives Element, Indizien und Gegenbeweis. |
| `vvg-falligkeit-14-abschlagszahlung` | Fälligkeit des Versicherungsanspruchs, Ermittlungsdauer, Abschlagszahlung, Verzug und taktische Beschleunigung bei großen Schäden. |
| `vvg-gefahrerhoehung-23-27` | Gefahrerhöhung vor und nach Vertragsschluss: willentlich/unwillentlich, Anzeige, Kündigung, Leistungsfreiheit und Kausalitätsprüfung in Sach-, Haftpflicht- und Personenversicherungen. |
| `vvg-mehrfachversicherung-78` | Mehrfachversicherung und Doppelversicherung: Innenausgleich, Anzeige, Überversicherung, Regress und Taktik bei mehreren Versicherern. |
| `vvg-obliegenheit-28-quotelung-kausalitaet` | § 28 VVG nach Eintritt des Versicherungsfalls: Anzeige, Aufklärung, Rettung, Mitwirkung, Kausalitätsgegenbeweis, Vorsatz/grobe Fahrlässigkeit und Quotierung. |
| `vvg-versicherung-fuer-fremde-43-48` | Versicherung für fremde Rechnung: wer darf Leistung verlangen, wem stehen Einwendungen entgegen, welche Rolle haben Sicherungsnehmer, Leasinggeber, Mieter, Subunternehmer und Konzernunternehmen? |
| `wohngebaeude-leitungswasser-sturm-hagel-brand` | Wohngebäudeversicherung: Leitungswasser, Sturm/Hagel, Brand, Elementarschaden, grobe Fahrlässigkeit, Obliegenheiten und Sanierungskosten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
