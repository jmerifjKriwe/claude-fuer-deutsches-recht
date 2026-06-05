# Kartellrecht — Marktabgrenzungsprüfung

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`kartellrecht-marktabgrenzung-pruefung`) | [`kartellrecht-marktabgrenzung-pruefung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kartellrecht-marktabgrenzung-pruefung.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Nordstern MedTech Vertrieb - Provision, Buchauszug und Ausgleich** (`handelsvertreterrecht-provisionsausgleich-nordstern-medtech`) | [Gesamt-PDF lesen](../testakten/handelsvertreterrecht-provisionsausgleich-nordstern-medtech/gesamt-pdf/handelsvertreterrecht-provisionsausgleich-nordstern-medtech_gesamt.pdf) | [`testakte-handelsvertreterrecht-provisionsausgleich-nordstern-medtech.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-handelsvertreterrecht-provisionsausgleich-nordstern-medtech.zip) |
| **Zusammenschlusskontrolle GBW / Tannenheim — Bahnbetonschwellen, Bußgeld, ECN+** (`kartell-zusammenschlusskontrolle-bahnbetonschwellen-grosskopf-westfalen`) | [Gesamt-PDF lesen](../testakten/kartell-zusammenschlusskontrolle-bahnbetonschwellen-grosskopf-westfalen/gesamt-pdf/kartell-zusammenschlusskontrolle-bahnbetonschwellen-grosskopf-westfalen_gesamt.pdf) | [`testakte-kartell-zusammenschlusskontrolle-bahnbetonschwellen-grosskopf-westfalen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kartell-zusammenschlusskontrolle-bahnbetonschwellen-grosskopf-westfalen.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Globales Kartellrechts- und Competition-Law-Plugin mit Marktabgrenzung als harter Kernachse: GWB, Art. 101 und Art. 102 AEUV, EU-Fusionskontrolle, Bundeskartellamt, DG Competition, FTC/DOJ, Dawn Raids, Leniency, Private Enforcement, sektorale Deep Dives und vorsichtige Jurisdiktionschecks weltweit.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Zweck

Dieses Prüfwerkzeug analysiert kartellrechtliche Fälle auf juristischer, ökonomischer und methodischer Ebene. Es unterstützt bei:

- **Fusionskontrolle:** FKVO-Verfahren Phase I/II, BKartA-Verfahren, SIEC-Test.
- **Missbrauchsverfahren:** Art. 102 AEUV / §§ 19–20 GWB; Marktbeherrschungsnachweis.
- **Kartellverbot:** Art. 101 AEUV / § 1 GWB; Spürbarkeit, Bagatell-Ausnahme.
- **Globalen Behördenverfahren:** BKartA, Europäische Kommission, FTC/DOJ und nationale Wettbewerbsbehörden mit Local-Counsel-Fragen.
- **Sektorfällen:** Cloud, KI-Foundation-Models, App Stores, AdTech, Pharma, Energie, Telekom, Zahlungsverkehr, Automotive, Logistik, Sport und öffentliche Beschaffung.
- **Behördliche Stellungnahmen:** Stellungnahmen in BKartA- und Kommissionsverfahren.
- **Parteigutachten:** Kritische Würdigung gegnerischer Marktdefinitionen.

## Referenzen

| Datei | Inhalt |
| --- | --- |
| `references/methodik-marktdefinition.md` | Umfassende Darstellung der Marktdefinitions-Methodik (SSNIP, Elastizitäten, Supply-Side, räumlicher Markt, Evidenz) |
| `references/eugh-leitentscheidungen.md` | Chronologische Entscheidungssammlung EuGH/EuG/BGH/BKartA mit Kernsätzen zur Marktdefinition |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Tragende Aussagen müssen vor der Ausgabe anhand amtlicher Normfassungen, Behördenquellen oder frei zugänglicher Rechtsprechung geprüft werden. Das Prüfwerkzeug ersetzt keine eigene anwaltliche Prüfung im Einzelfall. Kartellrechtliche Marktdefinitionen und Behördenzuständigkeiten sind fallabhängig und können sich nach Markt, Transaktionsstruktur und Jurisdiktion ändern.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 59 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `19a-gwb-relative-abuse-economic` | 19A GWB Relative Abuse Economic: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `alleinvertrieb-kundengruppen-alternative` | Alleinvertrieb Kundengruppen Alternative: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `angebotsumstellung-evidenz-flags-red` | Angebotsumstellung Evidenz Flags RED: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `art-aeuv-auswirkungen-marktanteile` | ART Aeuv Auswirkungen Marktanteile: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `art-arbeitsmarkt-no-aeuv-kooperationspruefung` | ART Arbeitsmarkt NO Aeuv Kooperationspruefung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `bietergemeinschaft-vergabekartellrecht-bka` | Bietergemeinschaft Vergabekartellrecht BKA: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `competition-global-kaltstart` | Global Competition Kaltstart: Fachmodul für großes Kartellrecht mit BKartA, DG Competition, FTC/DOJ und internationalen Behörden; prüft welche Jurisdiktionen, Produkte, Märkte, Umsätze, Behörden, Deadlines und Verfahrensarten sofort rele... |
| `competition-litigation-programm-mittelstand` | Competition Litigation Programm Mittelstand: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `cross-border-dawn-raid-gwb-kartellverbot` | Cross Border Dawn Raid GWB Kartellverbot: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `dma-gatekeeper-einkaufskooperation` | DMA Gatekeeper Einkaufskooperation: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `essential-facilities-eu-bekanntmachung` | Essential Facilities EU Bekanntmachung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `eugh-rechtsprechung-beweislast-jurisdiktion` | Eugh Rechtsprechung Beweislast Jurisdiktion: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `foreign-direct-freistellung-art` | Foreign Direct Freistellung ART: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `fusionskontrolle-modus-geoblocking` | Fusionskontrolle Modus Geoblocking: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `healthcare-kartellrecht-horizontal-gvo` | Healthcare Kartellrecht Horizontal GVO: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `information-exchange-informationsaustausch` | Information Exchange Informationsaustausch: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `jurisdiktion-algerien-competition-andorra` | Jurisdiktion Algerien Competition Andorra: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `jurisdiktion-armenien-aserbaidschan` | Jurisdiktion Armenien Aserbaidschan: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `jurisdiktion-australien-competition-bahrain` | Jurisdiktion Australien Competition Bahrain: bündelt 14 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `jurisdiktion-costa-rica-daenemark-competition` | Jurisdiktion Costa Rica Daenemark Competition: bündelt 14 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `jurisdiktion-guatemala-competition-honduras` | Jurisdiktion Guatemala Competition Honduras: bündelt 14 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `jurisdiktion-kasachstan-competition-katar` | Jurisdiktion Kasachstan Competition Katar: bündelt 14 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `jurisdiktion-luxemburg-competition-macau` | Jurisdiktion Luxemburg Competition Macau: bündelt 14 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `jurisdiktion-nepal-competition-neuseeland` | Jurisdiktion Nepal Competition Neuseeland: bündelt 14 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `jurisdiktion-peru-competition-philippinen` | Jurisdiktion Peru Competition Philippinen: bündelt 14 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `jurisdiktion-slowakei-competition-slowenien` | Jurisdiktion Slowakei Competition Slowenien: bündelt 14 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `jurisdiktion-ungarn-competition-uruguay` | Jurisdiktion Ungarn Competition Uruguay: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `jurisdiktion-venezuela-competition-vereinigte` | Jurisdiktion Venezuela Competition Vereinigte: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `jurisdiktion-zimbabwe-zypern-competition-eu` | Jurisdiktion Zimbabwe Zypern Competition EU: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kart-innovationswettbewerb` | Kart Innovationswettbewerb: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kartellrecht-kaltstart-mandat-neu` | Kartellrecht Kaltstart Mandat neu: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `kartellrecht-marktabgrenzung-pruefung-anschluss` | Anschluss: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kartellrecht-marktabgrenzung-pruefung-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `kartellrecht-marktabgrenzung-pruefung-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `kartellrecht-marktabgrenzung-pruefung-output-waehlen` | Output wählen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `kartellrecht-marktabgrenzung-pruefung-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `kartellrecht-marktabgrenzung-pruefung-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `kartellrechtliche-vertragsklausel` | Kartellrechtliche Vertragsklausel: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `ki-preisgestaltung-konsistenzpruefung` | KI Preisgestaltung Konsistenzpruefung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kritische-markt-interessen-marktabgrenzungen` | Kritische Markt Interessen Marktabgrenzungen: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `leniency-marker-margin-squeeze-telekom` | Leniency Marker Margin Squeeze Telekom: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `marktabgrenzung-kontextanalyse-mehrseitige` | Kontextanalyse Mehrseitige: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `minimis-inlandsauswirkung-digital-platforms` | Minimis Inlandsauswirkung Digital Platforms: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `missbrauchsverbot-modus` | Missbrauchsverbot Modus: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `nachfrage-quellenkarte` | Nachfrage Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `paragraf-raeumlicher-ssnip-test` | Paragraf Raeumlicher Ssnip Test: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `predatory-pricing-preisalgorithmen-kollusives` | Predatory Pricing Preisalgorithmen Kollusives: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `private-enforcement-produktmarkt` | Private Enforcement Produktmarkt: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `private-enforcement-rechtsabteilung` | Private Enforcement Rechtsabteilung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `pruefinstanz-franchise-vertrag` | Pruefinstanz Franchise Vertrag: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `rechtsabteilung-gun-informationsaustausch` | Rechtsabteilung GUN Informationsaustausch: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `refusal-to-remedies-zusagen-section-19a` | Refusal TO Remedies Zusagen Section 19A: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `sektor-app-stores-automotive-zulieferketten` | Sektor APP Stores Automotive Zulieferketten: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `sektor-krankenhaus-gesundheitsplattformen` | Sektor Krankenhaus Gesundheitsplattformen: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `sektor-sportligen-medienrechte` | Sektor Sportligen Medienrechte: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `self-preferencing-sep-frand-siec-test-aeuv` | Self Preferencing SEP Frand Siec Test Aeuv: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `spuerbarkeit-zwischenstaatlichkeit-ssnip-test` | Spuerbarkeit Zwischenstaatlichkeit Ssnip Test: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verbandsarbeit-informationsaustausch` | Verbandsarbeit Informationsaustausch: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `vertikale-leitlinien-verweisung-art` | Vertikale Leitlinien Verweisung ART: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
