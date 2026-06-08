# Grundbuchamt Praxis

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`grundbuchamt-praxis`) | [`grundbuchamt-praxis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/grundbuchamt-praxis.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Haus Altenau - verlorener Grundschuldbrief, Wegerecht und Kaufpreisfälligkeit** (`grundbuchamt-briefgrundschuld-wegerecht-altenau-2026`) | [Gesamt-PDF lesen](../testakten/grundbuchamt-briefgrundschuld-wegerecht-altenau-2026/gesamt-pdf/grundbuchamt-briefgrundschuld-wegerecht-altenau-2026_gesamt.pdf) | [`testakte-grundbuchamt-briefgrundschuld-wegerecht-altenau-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-grundbuchamt-briefgrundschuld-wegerecht-altenau-2026.zip) |
| **Akte Wusterhagen: Mühlenstau, Chaussee und Aufopferung** (`preussisches-landrecht-wusterhagen-muehlenstau-aufopferung`) | [Gesamt-PDF lesen](../testakten/preussisches-landrecht-wusterhagen-muehlenstau-aufopferung/gesamt-pdf/preussisches-landrecht-wusterhagen-muehlenstau-aufopferung_gesamt.pdf) | [`testakte-preussisches-landrecht-wusterhagen-muehlenstau-aufopferung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-preussisches-landrecht-wusterhagen-muehlenstau-aufopferung.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein Grundbuch-Cockpit für alle, die Auszüge lesen, Urkunden grundbuchtauglich nachweisen, Zwischenverfügungen verstehen und Grundbuchvollzug sauber betreiben müssen. Schwerpunkt ist die praktische Leseführung durch Abteilung I, II und III, damit keine Dienstbarkeit, Vormerkung, Rangstelle oder Briefgrundschuld übersehen wird.

## Wofür dieses Plugin da ist

Dieses Plugin ist ein Praxiswerkzeug. Es fragt zuerst die Lage ab, baut dann eine Dokumenten- und Vollzugsmatrix und erzeugt schließlich das konkrete Arbeitsprodukt: Nachreichung, Beanstandungsantwort, Beschwerdegerüst, Mandantenbrief, Checkliste, Fristenlog oder Vertrags-/Urkundenreview. Es ersetzt keine Berufsträgerentscheidung, aber es verhindert, dass ein formeller Nachweis, ein Rang, eine Abteilung-II-Belastung oder eine Registerfolge in der Hektik untergeht.

## Kaltstart

Starte mit dem allgemeinen Skill `grundbuchamt-allgemeiner-kaltstart`. Lade danach möglichst den aktuellen Register- oder Grundbuchauszug, das Gerichtsschreiben, die Anmeldung/Bewilligung, den Vertragsentwurf und vorhandene Anlagen hoch. Das Plugin sortiert erst, dann prüft es.

## Quellen- und Halluzinationsschutz

- Normen werden als Prüfanker verwendet, nicht als Schmuck.
- Rechtsprechung wird nur ausgegeben, wenn Gericht, Datum, Aktenzeichen und ein frei zugänglicher Fundlink geprüft sind.
- Unsichere Register-/Grundbuchstände werden nicht geraten; das Plugin fordert aktuelle Auszüge oder Nachweise an.

## Amtliche Startquellen

- [GBO](https://www.gesetze-im-internet.de/gbo/)
- [GBV](https://www.gesetze-im-internet.de/gbvfg/)
- [FamFG Aufgebotsverfahren](https://www.gesetze-im-internet.de/famfg/)
- [BGB Grundstücksrechte](https://www.gesetze-im-internet.de/bgb/)
- [Justizportal des Bundes und der Länder](https://justiz.de/)

## Typische Ergebnisse

- Prüfmatrix und Vollzugsfahrplan
- Entwurf für Nachreichung oder Antwort an das Gericht/Amt
- Mandantenbrief in normalem Deutsch
- Fristen- und Ranglog
- Beschwerde- oder Eilrechtsschutz-Skizze
- Liste fehlender Originale, Nachweise und Formmängel

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 64 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abteilung-i-eigentum-und-erwerbsgrund` | Prüft Eigentümer, Erwerbsgrund, Erbengemeinschaft, Bruchteile, Gesamthand, eGbR und Voreintragung im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `abteilung-ii-iii-grundschuld-auflassung` | Analysiert Wegerecht, Leitungsrecht, Nießbrauch, Wohnungsrecht, Vormerkung, Sanierungsvermerk, Nacherbfolge und Verfügungsbeschränkung im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbe... |
| `abteilung-iii-grundschuld-hypothek-rang` | Prüft Grundschuld, Hypothek, Rentenschuld, Brief/Buch, Rang, Löschung, Abtretung und Sicherungszweck-Schnittstelle im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `amtshaftung-und-vollzugsfehler` | Ordnet Fehler von Notar, Grundbuchamt, Partei und Bank ohne vorschnelle Schuldzuweisung im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `aufgebotsverfahren-famfg` | Prüft Zuständigkeit, Antragsberechtigung, Glaubhaftmachung, Aufgebotsfrist, öffentliche Bekanntmachung und Beschlussverwertung im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `auflassung-und-eigentumsumschreibung` | Prüft Auflassung, Antrag, Voreintragung, Unbedenklichkeitsbescheinigung, Genehmigungen und Vollzug im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `auflassungsvormerkung-kaufvertrag` | Prüft Vormerkungszweck, Rang, Löschung, Sicherung gegen Zwischenverfügungen und Käufer-/Bankenschutz im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `auslandsurkunden-apostille-baulast-ist` | Prüft Apostille, Legalisation, notarielle Bescheinigung, Übersetzung und Register-/Vertretungsnachweis im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `baulast-ist-nicht-grundbuch` | Erklärt, warum Baulasten nicht im Grundbuch stehen müssen und wie man Baulastenverzeichnis/Grundbuch zusammenliest im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `beschwerde-grundbuchsache` | Prüft Statthaftigkeit, Beschwer, Frist, Abhilfe, Nichtabhilfe und OLG-Vorlage in Grundbuchsachen im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `bestandsverzeichnis-flurstueck-briefrecht` | Prüft Grundstück, Flurstück, Gemarkung, Wirtschaftsart, Zuschreibung, Bestandsteil und Katasterabgleich im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `briefrecht-abtretung-und-loeschung` | Prüft Besitz am Brief, Abtretungserklärung, Löschungsbewilligung, Briefvorlage und Ersatzwege im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `dienstbarkeit-wegerecht-pruefen` | Liest Inhalt, herrschendes/dienendes Grundstück, Ausübungsbereich, Baulast-Schnittstelle und Löschbarkeit im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `elektronischer-rechtsverkehr` | Prüft elektronische Einreichung, notarielle Signatur, Scans, Ausfertigungen und Medienbruchrisiken im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `familiengerichtliche-genehmigung-grundbuch` | Prüft Minderjährige, betreute Personen, Genehmigungsbedürftigkeit, Rechtskraft und Nachweisform im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `finanzierung-und-rangstelle` | Koordiniert Bankauflagen, Rangbescheinigung, Belastungsvollmacht, Zweckerklärung und Auszahlungsvoraussetzungen im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `gbo-antrag-gbr-egbr-genehmigungen` | Prüft GBO-Mechanik aus Antrag, Bewilligung, Eintragungsfähigkeit, Eintragungsreife und Vollzugshindernis im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `gbr-egbr-grundbuch` | Prüft Gesellschaftsregister, Voreintragung, Vertretung, Gesellschafterwechsel und MoPeG-Folgen im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `genehmigungen-landwirtschaft-verkehrswert` | Prüft Grundstücksverkehr, siedlungsrechtliche Genehmigungen, Vorkaufsrechte und Registervollzug im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `grundbuch-grunderwerbsteuer-unbedenklichkeit` | Prüft GrESt-Schnittstelle, Fälligkeitslogik, Ausnahmen und Vollzugshindernis im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `grundbuch-qualitygate-vor-vollzug` | Prüft Antrag, Bewilligung, Rang, Nachweise, Anlagen, Genehmigungen, Urkundenform und Zahlungslogik. |
| `grundbuch-vollzugslog-amtswiderspruch` | Erstellt Fristen-, Rang- und Nachweisliste mit Verantwortlichen, Stand und nächstem Schritt im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `grundbuchamt-amtswiderspruch-und-richtigstellung` | Prüft offensichtliche Unrichtigkeit, Amtswiderspruch, Amtslöschung, Berichtigung und Rechtsschutz im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `grundbuchamt-brief-vs-buchrecht-erklaerung` | Erklärt Mandanten, warum der Briefkörper zählt und warum Kopien nicht reichen im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `grundbuchamt-eilfall-rangverlust-erbbaurecht` | Erarbeitet Sofortplan bei drohendem Rangverlust oder konkurrierendem Antrag im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `grundbuchamt-erbbaurecht-schnittstelle` | Verknüpft Grundstücksgrundbuch, Erbbaugrundbuch, Reallast, Zustimmung und Belastungen im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `grundbuchamt-flurbereinigung-und-umlegung` | Prüft neue Grundstücksbezeichnungen, Surrogation, Rangfortsetzung und Vollzugsnachweise im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `grundbuchamt-gesamtgrundschuld-mithaft` | Prüft Mithaft mehrerer Grundstücke, Pfandfreigabe, Rang und Bankauflagen im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `grundbuchamt-gesellschaftsrechtliche-vertretung` | Prüft Handelsregister, Gesellschafterliste, Geschäftsführer, Prokura, Liquidator und ausländische Vertreter im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `grundbuchamt-insolvenz-auslaendischer-trustee` | Prüft inzidente Anerkennung, Vertretungsmacht, Urkundenform, Übersetzung und Register-/Grundbuchfähigkeit im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `grundbuchamt-kommunikation-konkurrierende` | Formuliert sachliche Anfragen, Nachreichungen, Fristbitten und Beschwerdeankündigungen ohne Vollzug zu gefährden im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `grundbuchamt-konkurrierende-antraege-rangkonflikt` | Prüft, was zu tun ist, wenn Vormerkung, Grundschuld, Pfändung, Insolvenz-/ZVG-Vermerk oder Dienstbarkeit konkurrierend eingehen und der Rang wirtschaftlich entscheidend wird im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-P... |
| `grundbuchamt-maengelmatrix-notariat` | Klassifiziert jedes Hindernis nach Form, Berechtigung, Genehmigung, Rang, Kosten, Steuer und Inhalt im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `grundbuchamt-nichtigkeitsrisiko-kaufvertrags` | Prüft, ob ein möglicher Form-, Genehmigungs-, Vertretungs- oder Verbotsgesetzmangel den Grundbuchvollzug blockiert und wie Zwischenverfügung, Nachgenehmigung oder Rückabwicklung vorbereitet werden im Grundbuchamt Praxis. Liefert priorisi... |
| `grundbuchamt-teilloesung-rangfreigabe` | Prüft Teilflächen, Freigabeerklärung, Rangwirkung, Bankbrief und Vollzug im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `grundbuchamt-verwalterzustimmung-weg` | Prüft Teilungserklärung, Verwalternachweis, Beschluss, Form und Nachreichung im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `grundbuchamt-vollstreckungsunterwerfung` | Prüft § 800 ZPO-Schnittstelle, dingliche Unterwerfung, Klausel und Zustellung im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `grundbuchauszug-due-lesen-abteilung` | Baut eine DD-Tabelle aus Eigentum, Belastungen, Rang, Vollzugshindernissen, offenen Fragen und Deal-Relevanz im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `grundbuchauszug-lesen-abteilung-i-ii-iii` | Erklärt Bestandsverzeichnis, Abteilung I, II und III mit Warnsystem gegen übersehene Dienstbarkeiten, Vormerkungen, Verfügungsbeschränkungen und Rangfallen im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoam... |
| `grundbuchberichtigung-erbfall` | Prüft Erbschein, notarielle Verfügung von Todes wegen, Europäisches Nachlasszeugnis, Grundbuchberichtigung und Kostenfristen im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `grundschuld-bestellung-buchgrundschuld` | Prüft Bewilligung, Rang, Betrag, Zinsen, Nebenleistung, Unterwerfung und Sicherungsabrede im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `grundschuldbrief-verlust-aufgebot` | Führt durch Feststellung des Verlusts, Aufgebotsantrag, Nachweise, Ausschließungsbeschluss, Ersatzbrief/Löschung und Bankkommunikation im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbe... |
| `insolvenzvermerk-zwangsversteigerung-kataster` | Prüft Verfügungsbeschränkung, Zwangsversteigerungsvermerk, Rang, Löschung und Erwerb aus Verfahren im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `kaltstart-routing` | Führt durch Eigentum, Belastungen, Vollzugsziel, Grundbuchbezirk, Urkundentyp, Nachweise, Rang, Fristdruck und Kommunikationsweg mit dem Grundbuchamt. |
| `kataster-liegenschaftskarte-abgleich` | Prüft Flurstücksidentität, Vermessung, Teilung, Vereinigung, Fortführung und Vollzugshindernisse im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `kaufvertrags-check-grundbuch` | Prüft Belastungen, Fälligkeit, Löschung, Vormerkung, Finanzierung, Besitzübergang und Risiken aus Abteilung II im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `leitungsrecht-und-energieanlagen` | Prüft Strom, Wasser, Fernwärme, Telekommunikation, dingliche Sicherung und Rangkonflikte im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `loeschungsbewilligung-bank-nacherbenvermerk` | Checkt Bankformular, Unterschriften, Vertretungsmacht, Briefvorlage, Teillöschung und Verwahrstelle im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `nacherbenvermerk-und-verfuegungsbeschraenkung` | Prüft Vermerk, Zustimmung, Befreiung, Löschung und Erwerberrisiko im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `niessbrauch-wohnungsrecht` | Prüft Berechtigte, Inhalt, Rang, Löschung, Tod, Heimunterbringung, Vermietung und Finanzierungskonflikt im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `notariat-vollzugsauftrag-grundbuch` | Steuert Notarvollzug, Treuhandauflagen, Fälligkeitsmitteilung, Bankunterlagen und Mandantenkommunikation im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `paragraph-gbo-prioritaetsmitteilung` | Prüft öffentliche oder öffentlich beglaubigte Urkunden, Registerauszüge, Erbnachweise, Vollmachten, Auslandsurkunden und Übersetzungen im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbe... |
| `prioritaetsmitteilung-und-rangbescheinigung` | Prüft, wann Rang gesichert ist und wie Notar/Bank/Grundbuchamt die Reihenfolge dokumentieren im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `rangprinzip-und-rangvorbehalt` | Ordnet Rangfolge, Rangrücktritt, Gleichrang, Rangvorbehalt und Prioritätsrisiken im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `reallast-erbbauzins-sanierungsvermerk` | Prüft Inhalt, Anpassung, Rang, Vollstreckbarkeit und Zusammenhang mit Erbbaurechten im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `rechtsprechung-grundbuch-aufgebotsverfahren` | Verlangt bei jeder Entscheidung Gericht, Datum, Aktenzeichen und frei zugänglichen Link, sonst nur als Prüfbedarf ausgeben im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `sanierungsvermerk-und-vorkaufsrechte-kommune` | Prüft Genehmigung, Vorkaufsrecht, Löschung, Bescheinigung und Kaufvertragsvollzug im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `teilflaechenkauf-und-vermessung` | Plant Vormerkung, Messungsanerkennung, Fortführungsnachweis, Rang, Kaufpreisfälligkeit und Umschreibung im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `testamentsvollstrecker-grundbuch-vollmacht` | Prüft Verfügungsbefugnis, Zeugnis, Beschränkungen, Nachweisform und Verkaufsvollzug im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `verlorene-genehmigung-verwalterzustimmung-weg` | Prüft, wie eine verlorene familiengerichtliche, betreuungsgerichtliche, sanierungsrechtliche oder behördliche Genehmigung grundbuchtauglich ersetzt oder erneut beschafft wird im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-... |
| `vollmacht-vorsorgevollmacht-grundbuch` | Prüft notarielle Vollmacht, Ausfertigung, Betreuungs-/Vorsorgevollmacht, Widerruf, Auslandsbezug und Missbrauchsrisiko im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `vorkaufsrecht-wiederkaufsrecht` | Prüft dingliches Recht, Ausübungsfall, Frist, Löschung, Rang und Kaufvertragsgestaltung im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `weg-teilungsgrundbuch-zwischenverfuegung` | Prüft Teilungserklärung, Aufteilungsplan, Abgeschlossenheit, Sonder-/Gemeinschaftseigentum, Sondernutzungsrechte und Grundbuchblätter im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbei... |
| `zwischenverfuegung-paragraph-18-gbo` | Analysiert beanstandete Hindernisse, Behebbarkeit, Rangwahrung, Frist und Antwortstrategie im Grundbuchamt Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
