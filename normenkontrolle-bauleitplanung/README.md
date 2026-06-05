# Normenkontrolle Bauleitplanung — § 47 VwGO

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`normenkontrolle-bauleitplanung`) | [`normenkontrolle-bauleitplanung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/normenkontrolle-bauleitplanung.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Normenkontrolle B-Plan XV-43d „Spreepark Friedrichshain" — Bürgerinitiative Tannengarten gegen Land Berlin** (`normenkontrolle-bplan-spreepark-friedrichshain-buergerinitiative-tannengarten`) | [Gesamt-PDF lesen](../testakten/normenkontrolle-bplan-spreepark-friedrichshain-buergerinitiative-tannengarten/gesamt-pdf/normenkontrolle-bplan-spreepark-friedrichshain-buergerinitiative-tannengarten_gesamt.pdf) | [`testakte-normenkontrolle-bplan-spreepark-friedrichshain-buergerinitiative-tannengarten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-normenkontrolle-bplan-spreepark-friedrichshain-buergerinitiative-tannengarten.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Plugin für die Prüfung und gerichtliche Anfechtung von **Bebauungsplänen, Flächennutzungsplänen und örtlichen Bauvorschriften** im Normenkontrollverfahren nach § 47 VwGO vor dem **Bayerischen Verwaltungsgerichtshof (BayVGH)** und anderen Oberverwaltungsgerichten.

## Installation

1. Claude Code oder Claude Desktop/Cowork öffnen.
2. **Customize Plugins** bzw. **Personal plugins** wählen.
3. **Install from .zip** und `normenkontrolle-bauleitplanung.zip` hochladen.
4. Mit einem konkreten Auftrag starten, zum Beispiel: `Prüfe diesen Bebauungsplan auf formelle und materielle Fehler.`

Alternativ via Marketplace:

```
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install normenkontrolle-bauleitplanung@claude-fuer-deutsches-recht
```

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

## Normenkontrolle außerhalb der Bauleitplanung

Das Plugin ist nicht nur für Bebauungspläne gedacht. § 47 VwGO kann auch kommunale Satzungen und landesrechtliche Rechtsverordnungen erfassen, soweit das jeweilige Landesrecht die Normenkontrolle eröffnet. Deshalb prüft das Plugin nun ausdrücklich auch Kommunalabgaben-, Beitrags-, Benutzungs-, Friedhofs-, Kita-, Polizei-/Gefahrenabwehr- und sonstige Satzungen sowie die Abgrenzung zur bloßen Inzidentkontrolle im Verfahren gegen einen Einzelbescheid.

## Mandatsperspektive

Anwältin der Antragstellerseite — Eigentümer, Nachbarn, anerkannte Naturschutzverbände, Gemeinden gegen übergeordnete Planung. Schwerpunkt: aus der angegriffenen Satzung die formellen und materiellen Fehler herausarbeiten und vor dem OVG/VGH zur Unwirksamkeitserklärung bringen.

## Aufbau

Der Lebenszyklus eines Normenkontroll-Mandats läuft in vier Phasen:

```
Phase A — Mandat und Zulässigkeit
  └─ Erstgespräch → Statthaftigkeit → Antragsbefugnis → Jahresfrist

Phase B — Verfahrensfehler-Audit (formell)
  └─ Aufstellungsbeschluss → Beteiligungen → Bürgerversammlung
     → Umweltbericht → Planerhaltung §§ 214/215 BauGB

Phase C — Materielle Fehler
  └─ Erforderlichkeit § 1 Abs. 3 → Abwägungsgebot § 1 Abs. 7
     → Stellplätze → Lärm/Immissionsschutz → Artenschutz
     → Anpassung Flächennutzungsplan

Phase D — Verfahren BayVGH/OVG
  └─ Normenkontrollantrag → Eilantrag § 47 Abs. 6 VwGO
     → Mündliche Verhandlung
```

## Enthaltene Skills

### Phase A — Mandat und Zulässigkeit (4 Skills)

| Slug | Beschreibung |
|---|---|
| `mandat-erstgespraech-normenkontrolle` | Erstgespräch, Mandantenbetroffenheit, Erfolgsaussichten-Prognose, Kosten |
| `statthaftigkeit-47-vwgo` | Antragsgegenstand B-Plan/FNP/örtliche Bauvorschrift, Landesrecht im Rang unter Landesgesetz |
| `antragsbefugnis-eigentuemer-nachbar` | § 47 Abs. 2 VwGO Möglichkeitstheorie, Eigentum, abwägungserheblicher Belang, Verbandsklage |
| `jahresfrist-47-abs-2-vwgo` | Fristlauf ab Bekanntmachung, Wiedereinsetzung, Heilung durch ergänzendes Verfahren |

### Phase B — Verfahrensfehler-Audit (5 Skills)

| Slug | Beschreibung |
|---|---|
| `aufstellungsbeschluss-bekanntmachung` | § 2 Abs. 1, § 10 Abs. 3 BauGB Verfahrenskette, Anstoßfunktion |
| `beteiligung-frueh-foermlich` | §§ 3 Abs. 1, 3 Abs. 2, 4 Abs. 1, 4 Abs. 2 BauGB Behörden- und Öffentlichkeitsbeteiligung |
| `buergerversammlung-protokoll-audit` | Erörterungstermin, Behandlung Einwendungen, Vorfestlegungsverbot |
| `umweltbericht-umweltpruefung` | § 2 Abs. 4 BauGB, § 2a BauGB, UVPG-Verzahnung, FFH-Vorprüfung |
| `planerhaltung-214-215-baugb` | Beachtlichkeit, Rügefrist 1 Jahr, ergänzendes Verfahren § 214 Abs. 4 BauGB |

### Phase C — Materielle Fehler (9 Skills)

| Slug | Beschreibung |
|---|---|
| `erforderlichkeit-1-abs-3-baugb` | Planrechtfertigung, städtebauliches Konzept, Gefälligkeitsplanung |
| `abwaegungsgebot-1-abs-7-baugb` | Abwägungsausfall, Abwägungsdefizit, Fehlgewichtung, Disproportionalität |
| `stellplatzsatzung-bay-bauordnung` | Art. 47 BayBO Stellplatzpflicht, Reduzierung durch Satzung, Mobilitätskonzept |
| `immissionsschutz-laerm-bauleitplanung` | DIN 18005, TA Lärm, Trennungsgebot § 50 BImSchG, Schallschutzgutachten-Prüfung |
| `artenschutz-naturschutz-planung` | § 44 BNatSchG saP, FFH-Vorprüfung, Eingriffsregelung § 1a BauGB |
| `anpassungsgebot-flaechennutzungsplan` | § 8 Abs. 2 BauGB Entwicklungsgebot, Parallelverfahren, FNP-Berichtigung |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `festsetzungskatalog-9-baugb-baunvo` | Abschließender § 9-Katalog, BauNVO-Höchstgrenzen, dynamische Verweisungen, Bahnflächen § 38 BauGB |
| `veraenderungssperre-zurueckstellung-14-15-baugb` | § 14 Sperre, § 15 Zurückstellung, Entschädigung § 18, vertraglich-faktische Sperre |

### Phase D — Verfahren BayVGH/OVG (3 Skills)

| Slug | Beschreibung |
|---|---|
| `normenkontrollantrag-schriftsatz` | Aufbau, Antragsformulierung, Begründungsstruktur, Streitwert |
| `einstweilige-anordnung-47-abs-6-vwgo` | Vollzugsfolgenabwägung, Eilbedürftigkeit, Antragsbefugnis im Eilverfahren |
| `muendliche-verhandlung-vgh-strategie` | Vorbereitung, Beweisanträge, Plädoyer, Wirkungsausspruch |

## Vorlagen

- `assets/templates/normenkontrolle-mandatskarte.md` — Übersichtskarte für jedes Normenkontroll-Mandat
- `assets/templates/fehleraudit-checkliste.md` — Systematische Prüfreihenfolge formell vor materiell

## Bedienungshinweis

Das Plugin ist freistehend nutzbar und benötigt keine anderen Plugins des Marketplaces. Für umweltrechtliche Querfragen (FFH, saP, UVP) kann das Plugin `umweltrecht` ergänzend geladen werden, für allgemeine Verwaltungsverfahrensfragen das Plugin `verwaltungsrecht`.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 80 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abwaegungsgebot-1-abs-7-baugb` | Mandant greift Bebauungsplan wegen fehlerhafter Interessenabwaegung an. § 1 Abs. 7 BauGB Abwaegungsgebot. Prüfraster: vier Abwaegungsfehler-Stufen Abwaegungsausfall Abwaegungsdefizit Abwaegungsfehleinschaetzung Abwaegungsdisproportionali... |
| `anfechtung-antragsbefugnis-red` | Anfechtung Antragsbefugnis RED: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `anpassungsgebot-flaechennutzungsplan` | Mandant greift Bebauungsplan an weil er nicht aus dem Flaechennutzungsplan entwickelt wurde. § 8 Abs. 2 BauGB Entwicklungsgebot und Anpassungsgebot. Prüfraster: Entwicklungssaussage des FNP bezogen auf Plangebiet Konflikt FNP-Darstellung... |
| `antragsbefugnis-eigentuemer-nachbar` | Grundstueckseigentuemer oder Nachbar moechte Normenkontrollantrag stellen und fragt ob er antragsbefugt ist. § 47 Abs. 2 S. 1 VwGO Antragsbefugnis Normenkontrolle. Prüfraster: Möglichkeitstheorie als Massstab Eigentuemer im Plangebiet im... |
| `antragsbefugnis-fehlerkatalog` | Antragsbefugnis Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `artenschutz-naturschutz-aufstellungsbeschluss` | Artenschutz Naturschutz Aufstellungsbeschluss: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `artenschutz-naturschutz-planung` | Buerger oder Naturschutzverband greift Bebauungsplan wegen unzureichender Artenschutzprüfung an. § 44 BNatSchG Zugriffsverbote § 45 Abs. 7 BNatSchG Ausnahme. Prüfraster: spezielle artenschutzrechtliche Prüfung (saP) CEF-Massnahmen Eingri... |
| `aufstellungsbeschluss-bekanntmachung` | Mandant prüft ob ein Bebauungsplan an einem Verfahrensfehler beim Aufstellungsbeschluss oder der Bekanntmachung leidet. §§ 2 10 BauGB Verfahrenskette. Prüfraster: Aufstellungsbeschluss ortsuebl. Bekanntmachung § 2 Abs. 1 Beschluss als Sa... |
| `aufstellungsbeschluss-mandantenentscheidun-02` | Aufstellungsbeschluss: Mandantenkommunikation und Entscheidungsvorlage: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `aufstellungsbeschluss-mandantenentscheidung` | Aufstellungsbeschluss Mandantenentscheidung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `bauleitplanung-interessen` | Bauleitplanung: Mehrparteienkonflikt und Interessenmatrix: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `bayvgh-bekanntmachung-beweislast-eilantrag` | Bayvgh Bekanntmachung Beweislast Eilantrag: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `bebauungsplaenen-kommunalabgaben` | Bebauungsplaenen Kommunalabgaben: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `bekanntmachung-beweislast-darlegungslast` | Bekanntmachung: Beweislast, Darlegungslast und Substantiierung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `benutzungssatzung-kommunale-einrichtung` | Benutzungssatzungen kommunaler Einrichtungen: Markthalle, Friedhof, Kita, Bibliothek, Sportanlage, Hausrecht und Grundrechte.; Normanker: VwGO § 47; Kommunalordnungen; Grundrechte; Gebührenrecht; macht § 47 VwGO als allgemeines Satzungs-... |
| `beteiligung-frueh-buergerversammlung` | Beteiligung Frueh Buergerversammlung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `beteiligung-frueh-foermlich` | Mandant greift Bebauungsplan wegen Fehlern in der Buerger- oder Behoerdenbeteiligung an. §§ 3 4 BauGB Beteiligungsverfahren. Prüfraster: fruehzeitige Beteiligung § 3 Abs. 1 foermliche Auslegung § 3 Abs. 2 mindestens 1 Monat Behoerdenbete... |
| `buergerversammlung-protokoll-audit` | Mandant war bei Buergerversammlung und moechte Niederschrift auf Vollständigkeit prüfen. § 3 Abs. 1 BauGB Buergerversammlung Eroerterungstermin. Prüfraster: Einladung Tagesordnung Sitzungsleitung Wortbeitraege sinngemäße Niederschrift Vo... |
| `compliance-dokumentation-aktenvermerk` | Normenkontrolle: Compliance-Dokumentation und Aktenvermerk: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `eilantrag-47-abs-6-ausserhalb-baurecht` | Eilantrag nach § 47 Abs. 6 VwGO außerhalb des Baurechts: schwere Nachteile, wichtige Gründe, Vollzugsfolgen und Antragsstrategie.; Normanker: VwGO § 47 Abs. 6; Grundrechtsbezug; Folgenabwägung; macht § 47 VwGO als allgemeines Satzungs- u... |
| `eilantrag-47-abs-6-vwgo` | Eilantrag nach § 47 Abs. 6 VwGO: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `einstweilige-anordnung-47-abs-6-vwgo` | Mandant hat Normenkontrollantrag eingereicht und moechte Vollzug des Bebauungsplans bis zur Entscheidung stoppen. § 47 Abs. 6 VwGO einstweilige Anordnung. Prüfraster: Vollzugsfolgenabwaegung als Massstab Eilbedürftigkeit Baugenehmigung b... |
| `einstweilige-anordnung-erforderlichkeit-abs` | Einstweilige Anordnung Erforderlichkeit ABS: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `erforderlichkeit-1-abs-3-baugb` | Prüffeld für erforderlichkeit 1 abs 3 baugb: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `festsetzungskatalog-9-baugb-baunvo` | Mandant greift einzelne Festsetzungen im Bebauungsplan als rechtswidrig an. § 9 BauGB abschließender Festsetzungskatalog BauNVO. Prüfraster: Festsetzungen außerhalb des Katalogs unwirksam BauNVO Art und Mass bauliche Nutzung GRZ GFZ Voll... |
| `flaechennutzungsplaenen-normenkontrolle` | Flaechennutzungsplaenen Normenkontrolle: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `immissionsschutz-laerm-bauleitplanung` | Mandant greift Bebauungsplan wegen unzureichendem Schallschutz oder Immissionsschutz an. DIN 18005 TA Laerm § 50 BImSchG. Prüfraster: Orientierungswerte verschiedene Gebietstypen Schallschutzgutachten Methodik Worstcase Trennungsgrundsat... |
| `immissionsschutz-laerm-mandat-erstgespraech` | Immissionsschutz Laerm Mandat Erstgespraech: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `jahresfrist-47-abs-2-vwgo` | Mandant moechte Normenkontrollantrag stellen und Anwalt prüft ob die Jahresfrist noch laeuft. § 47 Abs. 2 S. 1 VwGO Jahresfrist Normenkontrolle. Prüfraster: Fristbeginn ortsuebliche Bekanntmachung § 10 Abs. 3 BauGB fehlerhafte Bekanntmac... |
| `jahresfrist-abs-nkbl-verfahren` | Jahresfrist ABS Nkbl Verfahren: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kommunalabgaben-und-beitragssatzungen` | Kommunalabgaben- und Beitragssatzungen: Gebühren, Beiträge, Fremdenverkehr, Abwasser, Elternbeiträge, Kalkulation und Gleichheitssatz.; Normanker: VwGO § 47; KAG der Länder; Art. 3 GG; Äquivalenz- und Kostendeckungsprinzip; macht § 47 Vw... |
| `mandat-erstgespraech-normenkontrolle` | Grundstueckseigentuemer oder Nachbar kommt wegen Bebauungsplan oder FNP in die Kanzlei. Erstgespraech Normenkontrollmandat. Prüfraster: Mandantenbetroffenheit Antragsbefugnis § 47 Abs. 2 VwGO Antragsfrist Statthaftigkeit Erstprüfung Plan... |
| `mandatsperspektive-quellenkarte` | Mandatsperspektive Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `muendliche-verhandlung-vgh-strategie` | Normenkontrollantrag steht vor muendlicher Verhandlung am VGH oder OVG. Vorbereitung muendliche Verhandlung Normenkontrolle. Prüfraster: Plaedoyer Einleitung Sachverhalt Rechtsausführungen Anträge schriftliche Beweisanträge Ortsbesichtig... |
| `nkbl-abwaegungsfehler-bauleitplanung` | Nkbl Abwaegungsfehler Bauleitplanung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `nkbl-abwaegungsfehler-spezial` | Spezialfall Abwaegungsfehler in der Bauleitplanung: Abwaegungsausfall, -defizit, -fehleinschaetzung, Disproportionalitaet. Pruefraster fuer Klage. |
| `nkbl-bauleitplanung-bauleiter` | Bauleiter Bauleitplanung BauGB: Flaechennutzungsplan, Bebauungsplan, Verfahrensarten, Beteiligung Oeffentlichkeit. Pruefraster fuer Gemeinde und Buergerinitiative. |
| `nkbl-buergerentscheid-buergerbegehren-spezial` | Spezialfall Buergerbegehren und Buergerentscheid in der Bauleitplanung: Landesrecht, Quoren, zulaessige Fragen. Pruefraster fuer Initiative. |
| `nkbl-normenkontrolle-verfahren-leitfaden` | Leitfaden Normenkontrollverfahren § 47 VwGO: Antragsbefugnis, Antragsfrist, Pruefungsumfang. Pruefraster fuer Antragsteller und Gemeinde. |
| `normenkontrollantrag-normenkontrolle` | Normenkontrollantrag Normenkontrolle: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `normenkontrollantrag-schriftsatz` | Normenkontrollantrag gegen Bebauungsplan oder FNP ist zu erstellen. § 47 VwGO Normenkontrollantrag Schriftsatz. Prüfraster: Rubrum Antrag Begründung Zulässigkeit (Statthaftigkeit Befugnis Frist Rechtsschutzbedürfnis) Verfahrensfehler Erf... |
| `normenkontrolle-antragstellervertretung-47vwgo` | Antragstellervertretung: Zahlen, Schwellenwerte und Berechnung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `normenkontrolle-bauleitplanung-abwaegung-formular-portal` | Abwaegung: Formular, Portal und Einreichungslogik: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `normenkontrolle-bauleitplanung-anfechtung-tatbestandsmerkmale` | Anfechtung: Tatbestandsmerkmale, Beweisfragen und Beleglage: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `normenkontrolle-bauleitplanung-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `normenkontrolle-bauleitplanung-bauvorschriften-behoerden` | Bauvorschriften: Behörden-, Gerichts- oder Registerweg: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `normenkontrolle-bauleitplanung-bayvgh-verhandlung-vergleich` | Bayvgh: Verhandlung, Vergleich und Eskalation: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `normenkontrolle-bauleitplanung-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `normenkontrolle-bauleitplanung-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `normenkontrolle-bauleitplanung-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `normenkontrolle-bauleitplanung-fristen-und-risikoampel` | Fristen- und Risikoampel: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `normenkontrolle-bauleitplanung-kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im Normenkontrolle Bauleitplanung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitspl... |
| `normenkontrolle-bauleitplanung-oertlichen-risikoampel` | Oertlichen: Risikoampel, Gegenargumente und Verteidigungslinien: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `normenkontrolle-bauleitplanung-output-waehlen` | Output wählen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `normenkontrolle-bauleitplanung-planerhaltung-internationaler` | Planerhaltung: Internationaler Bezug und Schnittstellen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `normenkontrolle-bauleitplanung-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `normenkontrolle-bauleitplanung-redteam-qualitygate` | Red-Team Qualitygate: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `normenkontrolle-bauleitplanung-umweltbericht-umweltpruefung` | Umweltbericht Umweltpruefung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `normenkontrolle-bauleitplanung-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `normenkontrolle-bauleitplanung-vwgo-schriftsatz-brief-memo` | VwGO: Schriftsatz-, Brief- und Memo-Bausteine: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `normenkontrolle-bebauungsplan-angriffspunkte` | Bebauungsplaenen: Fristen, Form, Zuständigkeit und Rechtsweg: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `normenkontrolle-fnp-inzidentkontrolle` | Flaechennutzungsplaenen: Dokumentenmatrix, Lückenliste und Nachforderung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `normenkontrolle-oder-inzidentkontrolle` | Normenkontrolle oder Inzidentkontrolle: wann § 47 VwGO, wann Anfechtung/Verpflichtung/Feststellung gegen Einzelakt.; Normanker: VwGO §§ 42 und 43 und 47; Rechtsschutzbedürfnis; Bestandskraft; macht § 47 VwGO als allgemeines Satzungs- und... |
| `normenkontrolle-satzungsnormenkontrolle` | Satzungsnormenkontrolle: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `normenkontrolle-satzungsnormenkontrolle-47-vwgo` | Allgemeine Satzungsnormenkontrolle nach § 47 VwGO: kommunale Satzungen, Landesrechtsverordnungen, Landesrechtseröffnung und Abgrenzung zur Inzidentkontrolle.; Normanker: VwGO § 47 Abs. 1 Nr. 2; jeweiliges Landesausführungsgesetz; Kommuna... |
| `normenkontrolle-start-chronologie-fristen` | Start Chronologie Fristen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `planerhaltung-214-215-baugb` | Gemeinde oder Vorhabentraeger prüft ob erkannte Planfehler zur Unwirksamkeit führen oder durch Planerhaltung geheilt werden. §§ 214 215 BauGB Planerhaltung und Ruegefrist. Prüfraster: § 214 Abs. 1 bis 3 beachtliche Fehler § 215 BauGB Rue... |
| `planerhaltung-abwaegung` | Planerhaltung Abwaegung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `planerhaltung-abwaegung-antragsbefugnis` | Planerhaltung, Abwägung und Antragsbefugnis: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `polizeiverordnung-gefahrenabwehrsatzung` | Polizeiverordnung Gefahrenabwehrsatzung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `polizeiverordnung-und-gefahrenabwehrsatzung` | Polizeiverordnungen und Gefahrenabwehrsätze: Normadressat, Bestimmtheit, Verhältnismäßigkeit, Ermächtigungsgrundlage und Eilrechtsschutz.; Normanker: VwGO § 47; Polizei-/Ordnungsrecht der Länder; Art. 2 und 8 und 12 und 14 GG; macht § 47... |
| `pruefung-erstpruefung-und-mandatsziel` | Pruefung: Erstprüfung, Rollenklärung und Mandatsziel: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `rechtsfolge-unwirksamkeit-und-bekanntmachung` | Rechtsfolge der Unwirksamkeit: Allgemeinverbindlichkeit, Veröffentlichung, Folgebescheide, Rückabwicklung und Vertrauensschutz.; Normanker: VwGO § 47 Abs. 5; Landesrecht; VwVfG/Spezialrecht; macht § 47 VwGO als allgemeines Satzungs- und... |
| `red-team-satzung-jenseits-baugb` | Red-Team Satzung jenseits BauGB: Ermächtigungsgrundlage, Zuständigkeit, Verfahren, Bekanntmachung, Bestimmtheit, Gleichheit, Verhältnismäßigkeit.; Normanker: VwGO § 47; Kommunalrecht; Art. 3 und 12 und 14 GG; macht § 47 VwGO als allgemei... |
| `statthaftigkeit-47-vwgo` | Mandant fragt ob Normenkontrollantrag gegen eine bestimmte Planung zulässig ist. § 47 Abs. 1 VwGO Statthaftigkeit Normenkontrolle. Prüfraster: Antragsgegenstand Bebauungsplan § 10 BauGB vorhabenbezogener B-Plan § 12 BauGB § 13a-B-Plan ör... |
| `stellplatzsatzung-bay-bauordnung` | Mandant wendet sich gegen Stellplatzsatzung einer Gemeinde oder deren Anwendung bei Bauantrag. Art. 47 BayBO § 9 Abs. 1 Nr. 4 BauGB Art. 81 BayBO Stellplatzsatzung. Prüfraster: Reduzierung Stellplatzschluessel durch örtliche Bauvorschrif... |
| `umweltbericht-umweltpruefung` | Mandant greift Bebauungsplan wegen unzureichender Umweltprüfung oder fehlendem Umweltbericht an. § 2 Abs. 4 BauGB § 2a BauGB Umweltbericht. Prüfraster: Schutzgueter nach Anhang 1 BauGB Mensch Tiere Pflanzen Boden Wasser Luft Klima Landsc... |
| `veraenderungssperre-zurueckstellung-14-15` | Bauherr oder Investor hat Bauantrag eingereicht aber Gemeinde hat Veraenderungssperre verhaengt und Antrag wird zurückgestellt. §§ 14 15 BauGB. Prüfraster: Aufstellungsbeschluss Voraussetzung § 14 Abs. 1 BauGB Wirkung Dauer 2 plus 1 plus... |
| `vorhabenbezogener-bebauungsplan-12-baugb` | Prüffeld für vorhabenbezogener bebauungsplan 12 baugb: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `vwgo-statthaftigkeit-stellplatzsatzung-bay` | Vwgo Statthaftigkeit Stellplatzsatzung BAY: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
