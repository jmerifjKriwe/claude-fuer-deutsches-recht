# HOAI Leistungsphasen Praxis

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`hoai-leistungsphasen-praxis`) | [`hoai-leistungsphasen-praxis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/hoai-leistungsphasen-praxis.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Kita Mühlenhof Lichtenrade - HOAI-Leistungsphasen und Bauüberwachung 2026** (`hoai-leistungsphasen-kita-muehlenhof-lichtenrade-2026`) | [Gesamt-PDF lesen](../testakten/hoai-leistungsphasen-kita-muehlenhof-lichtenrade-2026/gesamt-pdf/hoai-leistungsphasen-kita-muehlenhof-lichtenrade-2026_gesamt.pdf) | [`testakte-hoai-leistungsphasen-kita-muehlenhof-lichtenrade-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-hoai-leistungsphasen-kita-muehlenhof-lichtenrade-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein großes Arbeitsplugin für die Leistungsphasen der HOAI. Es begleitet Bauherrinnen, Architekten, Ingenieure, Bauleiter, Bauunternehmen, Subunternehmer, Anwälte, Sachverständige und Projektsteuerer durch die Phasen 1 bis 9: von der Grundlagenermittlung über Planung, Genehmigung, Ausführung, Vergabe und Bauüberwachung bis zur Objektbetreuung.

Die HOAI kennt für Gebäude und Innenräume nach § 34 HOAI neun Leistungsphasen. Dieses Plugin bildet deshalb LPH 1 bis LPH 9 ab; eine zehnte Leistungsphase gibt es in diesem Leistungsbild nicht. Für andere Leistungsbilder wie Freianlagen, Ingenieurbauwerke, Verkehrsanlagen, Tragwerksplanung oder technische Ausrüstung muss das Plugin zunächst auf das richtige HOAI-Leistungsbild routen.

## Kaltstart

Starte mit `hoai-allgemeiner-kaltstart` oder `hoai-leistungsphasen-router`. Lade Vertrag, Angebot, Honorarvereinbarung, Planstände, Protokolle, Kostenstand, Terminplan, Vergabeunterlagen, Baustellenberichte, Mängellisten und Rechnungen hoch. Das Plugin ordnet dann erst, in welcher LPH das Problem hängt, und schlägt die passenden Spezialskills vor.

## Fachfragen-Layer

Neben den LPH-Skills gibt es jetzt einen querliegenden Fachfragen-Layer für die harten Aktenprobleme: anrechenbare Kosten, mitzuverarbeitende Bausubstanz, Honorarzone, Baukostenobergrenze, Stufenbeauftragung, Zielfindungsphase, Verbraucherhinweis, Planungsänderungen, Ausführungsplanungstiefe, Vergabereife, Bieterspiegel, Bauüberwachungstiefe, Rechnungsprüfung, Abnahme/Mängel, Gewährleistungsmanagement, Fachplanerkoordination, Baugrund/Altlasten, SiGeKo/Projektsteuerung, BIM/CDE, Fördermittelbindung, prüffähige Schlussrechnung und Sachverständigenfragen. Der Router schlägt diese Skills zusätzlich zur passenden Leistungsphase vor.

## Leistungsphasen für Gebäude und Innenräume

| LPH | Bezeichnung | Bewertungsanker Gebäude/Innenräume |
| --- | --- | --- |
| 1 | Grundlagenermittlung | 2 % |
| 2 | Vorplanung | 7 % |
| 3 | Entwurfsplanung | 15 % |
| 4 | Genehmigungsplanung | 3 % Gebäude / 2 % Innenräume |
| 5 | Ausführungsplanung | 25 % Gebäude / 30 % Innenräume |
| 6 | Vorbereitung der Vergabe | 10 % Gebäude / 7 % Innenräume |
| 7 | Mitwirkung bei der Vergabe | 4 % Gebäude / 3 % Innenräume |
| 8 | Objektüberwachung, Bauüberwachung und Dokumentation | 32 % |
| 9 | Objektbetreuung | 2 % |

## Typische Ergebnisse

- LPH-Matrix mit Input, Output, Freigabe, Risiko und Nachtrag
- Plan-/Protokoll-/Kostenstand-Check
- Bauüberwachungs- und Mängelmanagement
- Vergabe- und Bieterspiegelprüfung
- Honorar-/Nachtragsnotiz
- Mandantenbrief, Bauherrnupdate oder anwaltlicher Prüfvermerk
- Sachverständigenfragen und Beweisakte für Streitfälle

## Amtliche Startquellen

- [HOAI Gesamtverordnung](https://www.gesetze-im-internet.de/hoai_2013/)
- [HOAI § 34 Gebäude und Innenräume](https://www.gesetze-im-internet.de/hoai_2013/__34.html)
- [HOAI Anlage 10 Gebäude und Innenräume](https://www.gesetze-im-internet.de/hoai_2013/anlage_10.html)
- [HOAI § 7 Honorarvereinbarung](https://www.gesetze-im-internet.de/hoai_2013/__7.html)
- [BGB § 650p Architekten- und Ingenieurvertrag](https://www.gesetze-im-internet.de/bgb/__650p.html)
- [BGB § 650q](https://www.gesetze-im-internet.de/bgb/__650q.html), [§ 650r](https://www.gesetze-im-internet.de/bgb/__650r.html), [§ 650s](https://www.gesetze-im-internet.de/bgb/__650s.html), [§ 650t](https://www.gesetze-im-internet.de/bgb/__650t.html)

## Quellenhygiene

Die HOAI ist nicht mehr das alte zwingende Mindestsatzregime für Neuverträge ab 2021. Honorar, Leistungsumfang und Vertrag müssen sauber getrennt werden. Rechtsprechung wird nur ausgegeben, wenn Gericht, Datum, Aktenzeichen und frei zugänglicher Fundlink geprüft sind.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 50 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `bim-modell-kostenobergrenze-budget-lph` | Nutze dies, wenn Hoai Bim Modell Planstand Cde Haftung, Hoai Kostenobergrenze Budget Haftung, Hoai Lph 01 Haftungsfalle, Hoai Lph 02 Haftungsfalle, Hoai Lph 03 Haftungsfalle im Plugin Hoai Leistungsphasen Praxis konkret bearbeitet werden... |
| `gebaeude-innenraeume-hoai-gerichtsfeste` | Nutze dies, wenn Hoai Gebaeude Innenraeume Anlage 10, Hoai Gerichtsfeste Akte, Hoai Gesamtschuld Bgb 650T im Plugin Hoai Leistungsphasen Praxis konkret bearbeitet werden soll. Auslöser: Bitte Hoai Gebaeude Innenraeume Anlage 10, Hoai Ger... |
| `hoai-allgemeiner-kaltstart` | HOAI-Praxis: führt durch Projektart, Rolle, LPH-Stand, Vertrag, Honorar, Druck und gewünschtes Ergebnis; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren. |
| `hoai-anwaltliche-red-team-runde` | HOAI-Praxis: sucht Fehler, falsche LPH-Zuordnung, fehlende Freigaben und Beleglücken; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren. |
| `hoai-baubesprechung-protokoll-baugrund` | Nutze dies, wenn Hoai Baubesprechung Protokoll, Hoai Baugrund Altlasten Untersuchungsbedarf, Hoai Bauherrnentscheidung Matrix, Hoai Bauunternehmen Perspektive, Hoai Bim Cde Planmanagement im Plugin Hoai Leistungsphasen Praxis konkret bea... |
| `hoai-claim-timeline-dokumentenindex` | Nutze dies, wenn Hoai Claim Timeline, Hoai Dokumentenindex Hoai Akte, Hoai Fachplaner Tga Brandschutz Tragwerk Koordination, Hoai Foerdermittel Baukosten, Hoai Foerdermittel Vergabebindung Rueckforderung im Plugin Hoai Leistungsphasen Pr... |
| `hoai-leistungsphasen-lph-abnahme-anwaltlicher` | Nutze dies, wenn Hoai Leistungsphasen Router, Hoai Lph 01 Abnahme Und Teilabnahme, Hoai Lph 01 Anwaltlicher Pruefvermerk, Hoai Lph 01 Bauherrnfreigabe, Hoai Lph 01 Bim Und Datenraum im Plugin Hoai Leistungsphasen Praxis konkret bearbeite... |
| `hoai-lph-01-red-team-pruefung` | HOAI LPH 1 Grundlagenermittlung: sucht Widersprüche, vergessene Beteiligte, falsche Annahmen und unklare Zuständigkeit; mit Fokus auf Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokume... |
| `hoai-lph-02-red-team-pruefung` | HOAI LPH 2 Vorplanung: sucht Widersprüche, vergessene Beteiligte, falsche Annahmen und unklare Zuständigkeit; mit Fokus auf Grundlagen analysieren, Planungskonzept mit Alternativen, Kostenschätzung, Vorverhandlungen und Entscheidungsgrun... |
| `hoai-lph-03-red-team-pruefung` | HOAI LPH 3 Entwurfsplanung: sucht Widersprüche, vergessene Beteiligte, falsche Annahmen und unklare Zuständigkeit; mit Fokus auf stimmige Entwurfsfassung, Kostenberechnung, Termin-/Objektbeschreibung, Integration der Fachplanung und Bewe... |
| `hoai-lph-04-red-team-pruefung` | HOAI LPH 4 Genehmigungsplanung: sucht Widersprüche, vergessene Beteiligte, falsche Annahmen und unklare Zuständigkeit; mit Fokus auf öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik und Be... |
| `hoai-lph-05-red-team-pruefung` | HOAI LPH 5 Ausführungsplanung: sucht Widersprüche, vergessene Beteiligte, falsche Annahmen und unklare Zuständigkeit; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und... |
| `hoai-lph-06-red-team-pruefung` | HOAI LPH 6 Vorbereitung der Vergabe: sucht Widersprüche, vergessene Beteiligte, falsche Annahmen und unklare Zuständigkeit; mit Fokus auf Mengen, Leistungsverzeichnisse, Schnittstellen, Kostenanschlag und Vergabestruktur und Bewertungsan... |
| `hoai-lph-belegakte-fachplaner-foerdermitte-02` | Nutze dies, wenn Hoai Lph 08 Dokumentation Und Belegakte, Hoai Lph 08 Fachplaner Schnittstellen, Hoai Lph 08 Foerdermittel Und Nachweis, Hoai Lph 08 Genehmigungen Und Auflagen, Hoai Lph 08 Grundleistung Besondere Leistung und 13 weitere... |
| `hoai-lph-belegakte-fachplaner-foerdermittel` | Nutze dies, wenn Hoai Lph 01 Dokumentation Und Belegakte, Hoai Lph 01 Fachplaner Schnittstellen, Hoai Lph 01 Foerdermittel Und Nachweis, Hoai Lph 01 Genehmigungen Und Auflagen, Hoai Lph 01 Grundleistung Besondere Leistung im Plugin Hoai... |
| `hoai-lph-bim-belegakte-fachplaner` | Nutze dies, wenn Hoai Lph 04 Bim Und Datenraum, Hoai Lph 04 Dokumentation Und Belegakte, Hoai Lph 04 Fachplaner Schnittstellen, Hoai Lph 04 Foerdermittel Und Nachweis, Hoai Lph 04 Genehmigungen Und Auflagen und 13 weitere Themen im Plugi... |
| `hoai-lph-bim-belegakte-fachplaner-02` | Nutze dies, wenn Hoai Lph 06 Bim Und Datenraum, Hoai Lph 06 Dokumentation Und Belegakte, Hoai Lph 06 Fachplaner Schnittstellen, Hoai Lph 06 Foerdermittel Und Nachweis, Hoai Lph 06 Genehmigungen Und Auflagen und 13 weitere Themen im Plugi... |
| `hoai-lph-haftungsfalle-lph-lph-lph-lph` | Nutze dies, wenn Hoai Lph 04 Haftungsfalle, Hoai Lph 05 Haftungsfalle, Hoai Lph 06 Haftungsfalle, Hoai Lph 07 Haftungsfalle, Hoai Lph 08 Haftungsfalle im Plugin Hoai Leistungsphasen Praxis konkret bearbeitet werden soll. Auslöser: Bitte... |
| `hoai-lph-kostensteuerung-mandantenbericht` | Nutze dies, wenn Hoai Lph 05 Kostensteuerung, Hoai Lph 05 Mandantenbericht, Hoai Lph 05 Mangel Claim Vorsorge, Hoai Lph 05 Nachtrag Und Change Request, Hoai Lph 05 Oeffentlicher Auftraggeber und 13 weitere Themen im Plugin Hoai Leistungs... |
| `hoai-lph-kostensteuerung-mandantenbericht-02` | Nutze dies, wenn Hoai Lph 07 Kostensteuerung, Hoai Lph 07 Mandantenbericht, Hoai Lph 07 Mangel Claim Vorsorge, Hoai Lph 07 Nachtrag Und Change Request, Hoai Lph 07 Oeffentlicher Auftraggeber im Plugin Hoai Leistungsphasen Praxis konkret... |
| `hoai-lph-kostensteuerung-mandantenbericht-03` | Nutze dies, wenn Hoai Lph 09 Kostensteuerung, Hoai Lph 09 Mandantenbericht, Hoai Lph 09 Mangel Claim Vorsorge, Hoai Lph 09 Nachtrag Und Change Request, Hoai Lph 09 Oeffentlicher Auftraggeber und 13 weitere Themen im Plugin Hoai Leistungs... |
| `hoai-lph-kostensteuerung-mandantenbericht-04` | Nutze dies, wenn Hoai Lph 01 Kostensteuerung, Hoai Lph 01 Mandantenbericht, Hoai Lph 01 Mangel Claim Vorsorge, Hoai Lph 01 Nachtrag Und Change Request, Hoai Lph 01 Oeffentlicher Auftraggeber und 13 weitere Themen im Plugin Hoai Leistungs... |
| `hoai-lph-kostensteuerung-mandantenbericht-05` | Nutze dies, wenn Hoai Lph 03 Kostensteuerung, Hoai Lph 03 Mandantenbericht, Hoai Lph 03 Mangel Claim Vorsorge, Hoai Lph 03 Nachtrag Und Change Request, Hoai Lph 03 Oeffentlicher Auftraggeber und 13 weitere Themen im Plugin Hoai Leistungs... |
| `hoai-lph-outputpaket-planfreigabe` | Nutze dies, wenn Hoai Lph 07 Outputpaket, Hoai Lph 07 Planfreigabe Und Versionierung, Hoai Lph 07 Qualitaetsgate, Hoai Lph 07 Rechnung Und Prueffaehigkeit, Hoai Lph 07 Red Team Prüfung im Plugin Hoai Leistungsphasen Praxis konkret bearbe... |
| `hoai-lph-risikoregister-sachverstaendigen` | Nutze dies, wenn Hoai Lph 04 Risikoregister, Hoai Lph 04 Sachverstaendigen Prüfung, Hoai Lph 04 Schnittstelle Vob Bgb, Hoai Lph 04 Streitfall Vorbereitung, Hoai Lph 04 Terminsteuerung und 13 weitere Themen im Plugin Hoai Leistungsphasen... |
| `hoai-lph-risikoregister-sachverstaendigen-02` | Nutze dies, wenn Hoai Lph 06 Risikoregister, Hoai Lph 06 Sachverstaendigen Prüfung, Hoai Lph 06 Schnittstelle Vob Bgb, Hoai Lph 06 Streitfall Vorbereitung, Hoai Lph 06 Terminsteuerung und 13 weitere Themen im Plugin Hoai Leistungsphasen... |
| `hoai-lph-risikoregister-sachverstaendigen-03` | Nutze dies, wenn Hoai Lph 07 Risikoregister, Hoai Lph 07 Sachverstaendigen Prüfung, Hoai Lph 07 Schnittstelle Vob Bgb, Hoai Lph 07 Streitfall Vorbereitung, Hoai Lph 07 Terminsteuerung im Plugin Hoai Leistungsphasen Praxis konkret bearbei... |
| `hoai-lph-risikoregister-sachverstaendigen-04` | Nutze dies, wenn Hoai Lph 08 Risikoregister, Hoai Lph 08 Sachverstaendigen Prüfung, Hoai Lph 08 Schnittstelle Vob Bgb, Hoai Lph 08 Streitfall Vorbereitung, Hoai Lph 08 Terminsteuerung und 13 weitere Themen im Plugin Hoai Leistungsphasen... |
| `hoai-lph-risikoregister-sachverstaendigen-05` | Nutze dies, wenn Hoai Lph 02 Risikoregister, Hoai Lph 02 Sachverstaendigen Prüfung, Hoai Lph 02 Schnittstelle Vob Bgb, Hoai Lph 02 Streitfall Vorbereitung, Hoai Lph 02 Terminsteuerung und 13 weitere Themen im Plugin Hoai Leistungsphasen... |
| `hoai-lph-vertrag-beauftragungsumfang-lph-lph` | Nutze dies, wenn Hoai Lph 03 Vertrag Und Beauftragungsumfang, Hoai Lph 04 Vertrag Und Beauftragungsumfang, Hoai Lph 05 Vertrag Und Beauftragungsumfang, Hoai Lph 06 Vertrag Und Beauftragungsumfang, Hoai Lph 07 Vertrag Und Beauftragungsumf... |
| `hoai-lph6-lv-lph7-bieterspiegel-lph8-maengel` | Nutze dies, wenn Hoai Lph6 Lv Mengen Massen Vergabereife, Hoai Lph7 Bieterspiegel Aufklaerung Vergaberisiko, Hoai Lph8 Mängel Abnahme Restleistungen, Hoai Lph8 Rechnungspruefung Nachtraege Vob, Hoai Lph8 Ueberwachungstiefe Stichproben im... |
| `hoai-mitzuverarbeitende-bausubstanz` | Nutze dies, wenn Hoai Mitzuverarbeitende Bausubstanz Bestand, Hoai Nachtragsmanagement Planer, Hoai Neun Phasen Ueberblick, Hoai Oeffentliche Vergabe Planerleistungen, Hoai Prueffaehige Schlussrechnung Einwendungen im Plugin Hoai Leistun... |
| `hoai-sigeko-projektsteuerung-abnahmefahrplan` | Nutze dies, wenn Hoai Sigeko Projektsteuerung Besondere Leistungen, Hoai Abnahmefahrplan, Hoai Abschluss Und Lessons Learned, Hoai Andere Leistungsbilder Router, Hoai Anwalt Sachverstaendiger Architekt Dreieck im Plugin Hoai Leistungspha... |
| `hoai-stufenbeauftragung-abruf-subunternehmer` | Nutze dies, wenn Hoai Stufenbeauftragung Abruf Nichtabruf, Hoai Subunternehmer Perspektive, Hoai Teilabnahme Bgb 650S, Hoai Umbau Modernisierung Zuschlag Bestand, Hoai Verbraucherhinweis Honorarvereinbarung im Plugin Hoai Leistungsphasen... |
| `honorarvereinbarung-paragraph-honorarzone` | Nutze dies, wenn Hoai Honorarvereinbarung Paragraph 7 Hoai, Hoai Honorarzone Bewertungspunkte Objektliste, Hoai Ingenieur Perspektive, Hoai Kanzlei Mandatsintake Hoai, Hoai Kostenrahmen Kostenschaetzung Kostenberechnung im Plugin Hoai Le... |
| `lph-anwaltlicher-lph-bauherrnfreigabe-lph-bim` | Nutze dies, wenn Hoai Lph 08 Anwaltlicher Pruefvermerk, Hoai Lph 08 Bauherrnfreigabe, Hoai Lph 08 Bim Und Datenraum im Plugin Hoai Leistungsphasen Praxis konkret bearbeitet werden soll. Auslöser: Bitte Hoai Lph 08 Anwaltlicher Pruefverme... |
| `lph-bim-lph-belegakte-lph-fachplaner-lph` | Nutze dies, wenn Hoai Lph 02 Bim Und Datenraum, Hoai Lph 02 Dokumentation Und Belegakte, Hoai Lph 02 Fachplaner Schnittstellen, Hoai Lph 02 Foerdermittel Und Nachweis, Hoai Lph 02 Genehmigungen Und Auflagen und 13 weitere Themen im Plugi... |
| `lph-haftungsfalle-planerhaftung-grundlagen` | Nutze dies, wenn Hoai Lph 09 Haftungsfalle, Hoai Planerhaftung Grundlagen, Hoai Streitwert Und Schadensbild, Hoai Anrechenbare Kosten Din276 Baukostengruppen, Hoai Lph 08 Abnahme Und Teilabnahme im Plugin Hoai Leistungsphasen Praxis konk... |
| `lph-honorar-lph-input-lph-kommunikation` | Nutze dies, wenn Hoai Lph 01 Honorar Und Prozentwert, Hoai Lph 01 Input Und Zielcheck, Hoai Lph 01 Kommunikation Baustelle Behörde im Plugin Hoai Leistungsphasen Praxis konkret bearbeitet werden soll. Auslöser: Bitte Hoai Lph 01 Honorar... |
| `lph-verbraucher-maengelmanagement-end` | Nutze dies, wenn Hoai Lph 07 Verbraucher Privater Bauherr, Hoai Maengelmanagement End To End, Hoai Mandantenbrief Hoai im Plugin Hoai Leistungsphasen Praxis konkret bearbeitet werden soll. Auslöser: Bitte Hoai Lph 07 Verbraucher Privater... |
| `lph-vertrag-lph-vertrag-hoai-vertragliche` | Nutze dies, wenn Hoai Lph 08 Vertrag Und Beauftragungsumfang, Hoai Lph 09 Vertrag Und Beauftragungsumfang, Hoai Vertragliche Schnittstellen im Plugin Hoai Leistungsphasen Praxis konkret bearbeitet werden soll. Auslöser: Bitte Hoai Lph 08... |
| `lph8-bauueberwachung-altvertrag` | Nutze dies, wenn Lph8 Bauueberwachung Windpark Fundament Turm, Hoai Altvertrag Mindestsatzstreit, Hoai Architektenvertrag Bgb 650P, Hoai Lph 01 Vertrag Und Beauftragungsumfang, Hoai Lph 02 Vertrag Und Beauftragungsumfang im Plugin Hoai L... |
| `lph8-bauueberwachung-bueroneubau-dachdeckung` | Nutze dies, wenn Lph8 Bauueberwachung Bueroneubau Curtain Wall, Lph8 Bauueberwachung Dachdeckung Flachdach Attika, Lph8 Bauueberwachung Deich Hochwasserschutz im Plugin Hoai Leistungsphasen Praxis konkret bearbeitet werden soll. Auslöser... |
| `lph8-bauueberwachung-dokumentenanalyse` | Nutze dies, wenn Lph8 Bauueberwachung Dokumentenanalyse Aufmass, Lph8 Bauueberwachung Doppelhaus Reihenhaus, Lph8 Bauueberwachung Einfamilienhaus Holzbau, Lph8 Bauueberwachung Einfamilienhaus Massiv, Lph8 Bauueberwachung Einkaufszentrum... |
| `lph8-bauueberwachung-klaeranlage-krankenhaus` | Nutze dies, wenn Lph8 Bauueberwachung Klaeranlage Becken Dichtigkeit, Lph8 Bauueberwachung Krankenhaus Rein Raum, Lph8 Bauueberwachung Logistikhalle Bodenplatte, Lph8 Bauueberwachung Maengelmeldung Sap Pm, Lph8 Bauueberwachung Mauerwerk... |
| `lph8-bauueberwachung-lph2` | Nutze dies, wenn Lph8 Bauueberwachung Erdbau Bodenkennwerte, Hoai Lph2 Variantenuntersuchung Wirtschaftlichkeit, Hoai Lph3 Kostenberechnung Budgetalarm, Hoai Lph4 Genehmigungsrisiko Bauantrag Auflagen, Hoai Lph5 Ausfuehrungsplanung Detai... |
| `lph8-bauueberwachung-trockenbau-tunnel` | Nutze dies, wenn Lph8 Bauueberwachung Trockenbau F30 F90, Lph8 Bauueberwachung Tunnel Spritzbeton Vortrieb, Lph8 Bauueberwachung Videoanalyse Tagesbaustelle, Lph8 Bauueberwachung Vob C Din Checklisten, Lph8 Bauueberwachung Wasserwerk Roh... |
| `lph9-gewaehrleistungsmanagement-lph8` | Nutze dies, wenn Hoai Lph9 Gewaehrleistungsmanagement Fristen, Lph8 Bauueberwachung Abnahmeprotokoll Foerder Erp, Lph8 Bauueberwachung Bautagebuch Erp Import, Lph8 Bauueberwachung Bewehrung Verlegekontrolle, Lph8 Bauueberwachung Bruecke... |
| `qualitaetscheck-release-rechnungspruefung` | Nutze dies, wenn Hoai Qualitaetscheck Vor Release, Hoai Rechnungspruefung Architekt, Hoai Sachverstaendigenfragen, Hoai Sonderkuendigung Bgb 650R, Hoai Stufenbeauftragung im Plugin Hoai Leistungsphasen Praxis konkret bearbeitet werden so... |
| `vob-b-wiederholungsleistungen` | Nutze dies, wenn Hoai Vob B Schnittstelle, Hoai Wiederholungsleistungen Planungsaenderung, Hoai Zielfindungsphase Bgb 650P 650R im Plugin Hoai Leistungsphasen Praxis konkret bearbeitet werden soll. Auslöser: Bitte Hoai Vob B Schnittstell... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
