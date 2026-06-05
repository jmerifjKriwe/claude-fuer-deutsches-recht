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
| `anwaltlicher-pruefvermerk-bauherrnfreigabe` | Hoai Anwaltlicher Pruefvermerk / Hoai Bauherrnfreigabe / Hoai Bim Datenraum: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |
| `bim-datenraum-dokumentation-belegakte` | Hoai Bim Datenraum / Hoai Dokumentation Belegakte / Hoai Fachplaner Schnittstellen / Hoai Foerdermittel Nachweis / 14 weitere Module: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den näch... |
| `bim-datenraum-dokumentation-belegakte-02` | Hoai Bim Datenraum / Hoai Dokumentation Belegakte / Hoai Fachplaner Schnittstellen / Hoai Foerdermittel Nachweis / 14 weitere Module: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den näch... |
| `bim-modell-kostenobergrenze-budget-lph` | Hoai Bim Modell Planstand Cde Haftung, Hoai Kostenobergrenze Budget Haftung, Hoai Lph 01 Haftungsfalle, Hoai Lph 02 Haftungsfalle: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den näch... |
| `dokumentation-belegakte-fachplaner` | Hoai Dokumentation Belegakte / Hoai Fachplaner Schnittstellen / Hoai Foerdermittel Nachweis / Hoai Genehmigungen Auflagen / 14 weitere Module: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt... |
| `gebaeude-innenraeume-hoai-gerichtsfeste` | Hoai Gebaeude Innenraeume Anlage 10, Hoai Gerichtsfeste Akte, Hoai Gesamtschuld Bgb 650t: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `hoai-anwaltliche-red-team-runde` | HOAI-Praxis: sucht Fehler, falsche LPH-Zuordnung, fehlende Freigaben und Beleglücken; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren. |
| `hoai-baubesprechung-protokoll-baugrund` | Hoai Baubesprechung Protokoll, Hoai Baugrund Altlasten Untersuchungsbedarf, Hoai Bauherrnentscheidung Matrix, Hoai Bauunternehmen Perspektive: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und lief... |
| `hoai-claim-timeline-dokumentenindex` | Hoai Claim Timeline, Hoai Dokumentenindex Hoai Akte, Hoai Fachplaner Tga Brandschutz Tragwerk Koordination, Hoai Foerdermittel Baukosten: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert d... |
| `hoai-kaltstart-routing` | HOAI-Praxis: führt durch Projektart, Rolle, LPH-Stand, Vertrag, Honorar, Druck und gewünschtes Ergebnis; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren. |
| `hoai-kostensteuerung-mandanten-mangel-claim-03` | Hoai Kostensteuerung / Hoai Mandantenbericht / Hoai Mangel Claim Vorsorge / Hoai Nachtrag Change Request / 14 weitere Module: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten bel... |
| `hoai-kostensteuerung-mandanten-mangel-claim-04` | Hoai Kostensteuerung / Hoai Mandantenbericht / Hoai Mangel Claim Vorsorge / Hoai Nachtrag Change Request / 14 weitere Module: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten bel... |
| `hoai-kostensteuerung-mandanten-mangel-nachtrag` | Hoai Kostensteuerung / Hoai Mandantenbericht / Hoai Mangel Claim Vorsorge / Hoai Nachtrag Change Request / 1 weitere Module: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten bela... |
| `hoai-leistungsphasen-lph-abnahme-anwaltlicher` | Hoai Leistungsphasen Router, Hoai Lph 01 Abnahme Und Teilabnahme, Hoai Lph 01 Anwaltlicher Pruefvermerk, Hoai Lph 01 Bauherrnfreigabe: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den... |
| `hoai-lph-01-red-team-pruefung` | HOAI LPH 1 Grundlagenermittlung: sucht Widersprüche, vergessene Beteiligte, falsche Annahmen und unklare Zuständigkeit; mit Fokus auf Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokume... |
| `hoai-lph-02-red-team-pruefung` | HOAI LPH 2 Vorplanung: sucht Widersprüche, vergessene Beteiligte, falsche Annahmen und unklare Zuständigkeit; mit Fokus auf Grundlagen analysieren, Planungskonzept mit Alternativen, Kostenschätzung, Vorverhandlungen und Entscheidungsgrun... |
| `hoai-lph-03-red-team-pruefung` | HOAI LPH 3 Entwurfsplanung: sucht Widersprüche, vergessene Beteiligte, falsche Annahmen und unklare Zuständigkeit; mit Fokus auf stimmige Entwurfsfassung, Kostenberechnung, Termin-/Objektbeschreibung, Integration der Fachplanung und Bewe... |
| `hoai-lph-04-red-team-pruefung` | HOAI LPH 4 Genehmigungsplanung: sucht Widersprüche, vergessene Beteiligte, falsche Annahmen und unklare Zuständigkeit; mit Fokus auf öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik und Be... |
| `hoai-lph-05-red-team-pruefung` | HOAI LPH 5 Ausführungsplanung: sucht Widersprüche, vergessene Beteiligte, falsche Annahmen und unklare Zuständigkeit; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und... |
| `hoai-lph-06-red-team-pruefung` | HOAI LPH 6 Vorbereitung der Vergabe: sucht Widersprüche, vergessene Beteiligte, falsche Annahmen und unklare Zuständigkeit; mit Fokus auf Mengen, Leistungsverzeichnisse, Schnittstellen, Kostenanschlag und Vergabestruktur und Bewertungsan... |
| `hoai-lph-belegakte-fachplaner-foerdermittel` | Hoai Lph 01 Dokumentation Und Belegakte, Hoai Lph 01 Fachplaner Schnittstellen, Hoai Lph 01 Foerdermittel Und Nachweis, Hoai Lph 01 Genehmigungen Und Auflagen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsg... |
| `hoai-lph-bim-belegakte-fachplaner` | Hoai Lph 04 Bim Und Datenraum, Hoai Lph 04 Dokumentation Und Belegakte, Hoai Lph 04 Fachplaner Schnittstellen, Hoai Lph 04 Foerdermittel Und Nachweis: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage... |
| `hoai-lph-kostensteuerung-mandantenbericht` | Hoai Lph 05 Kostensteuerung, Hoai Lph 05 Mandantenbericht, Hoai Lph 05 Mangel Claim Vorsorge, Hoai Lph 05 Nachtrag Und Change Request: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den... |
| `hoai-lph-outputpaket-planfreigabe` | Hoai Lph 07 Outputpaket, Hoai Lph 07 Planfreigabe Und Versionierung, Hoai Lph 07 Qualitaetsgate, Hoai Lph 07 Rechnung Und Prueffaehigkeit: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert... |
| `hoai-lph-risikoregister-sachverstaendigen` | Hoai Lph 04 Risikoregister, Hoai Lph 04 Sachverstaendigen Prüfung, Hoai Lph 04 Schnittstelle Vob Bgb, Hoai Lph 04 Streitfall Vorbereitung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert... |
| `hoai-lph6-lv-lph7-bieterspiegel-lph8-maengel` | Hoai Lph6 Lv Mengen Massen Vergabereife, Hoai Lph7 Bieterspiegel Aufklaerung Vergaberisiko, Hoai Lph8 Maengel Abnahme Restleistungen, Hoai Lph8 Rechnungspruefung Nachtraege Vob: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit,... |
| `hoai-mitzuverarbeitende-bausubstanz` | Hoai Mitzuverarbeitende Bausubstanz Bestand, Hoai Nachtragsmanagement Planer, Hoai Neun Phasen Ueberblick, Hoai Oeffentliche Vergabe Planerleistungen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage... |
| `hoai-sigeko-projektsteuerung-abnahmefahrplan` | Hoai Sigeko Projektsteuerung Besondere Leistungen, Hoai Abnahmefahrplan, Hoai Abschluss Und Lessons Learned, Hoai Andere Leistungsbilder Router: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und li... |
| `hoai-stufenbeauftragung-abruf-subunternehmer` | Hoai Stufenbeauftragung Abruf Nichtabruf, Hoai Subunternehmer Perspektive, Hoai Teilabnahme Bgb 650s, Hoai Umbau Modernisierung Zuschlag Bestand: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und l... |
| `honorar-prozentwert-input-zielcheck` | Hoai Honorar Prozentwert / Hoai Input Zielcheck / Hoai Kommunikation Baustelle Behoerde: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |
| `honorarvereinbarung-paragraph-honorarzone` | Hoai Honorarvereinbarung Paragraph 7 Hoai, Hoai Honorarzone Bewertungspunkte Objektliste, Hoai Ingenieur Perspektive, Hoai Kanzlei Mandatsintake Hoai: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage... |
| `kostensteuerung-mandantenbericht-mangel-claim` | Hoai Kostensteuerung / Hoai Mandantenbericht / Hoai Mangel Claim Vorsorge / Hoai Nachtrag Change Request / 14 weitere Module: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten bel... |
| `lph-haftungsfalle-planerhaftung-grundlagen` | Hoai Lph 09 Haftungsfalle, Hoai Planerhaftung Grundlagen, Hoai Streitwert Und Schadensbild, Hoai Anrechenbare Kosten Din276 Baukostengruppen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefe... |
| `lph-verbraucher-maengelmanagement-end` | Hoai Lph 07 Verbraucher Privater Bauherr, Hoai Maengelmanagement End To End, Hoai Mandantenbrief Hoai: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `lph4-bis-lph8-haftungsfallen` | Hoai Haftungsfalle / Hoai Haftungsfalle / Hoai Haftungsfalle / Hoai Haftungsfalle / 1 weitere Module: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |
| `lph8-bauueberwachung-altvertrag` | Lph8 Bauueberwachung Windpark Fundament Turm, Hoai Altvertrag Mindestsatzstreit, Hoai Architektenvertrag Bgb 650p, Hoai Lph 01 Vertrag Und Beauftragungsumfang: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsg... |
| `lph8-bauueberwachung-bueroneubau-dachdeckung` | Lph8 Bauueberwachung Bueroneubau Curtain Wall, Lph8 Bauueberwachung Dachdeckung Flachdach Attika, Lph8 Bauueberwachung Deich Hochwasserschutz: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und lief... |
| `lph8-bauueberwachung-dokumentenanalyse` | Lph8 Bauueberwachung Dokumentenanalyse Aufmass, Lph8 Bauueberwachung Doppelhaus Reihenhaus, Lph8 Bauueberwachung Einfamilienhaus Holzbau, Lph8 Bauueberwachung Einfamilienhaus Massiv: wählt den konkreten Prüfpfad, trennt Frist, Zuständigk... |
| `lph8-bauueberwachung-klaeranlage-krankenhaus` | Lph8 Bauueberwachung Klaeranlage Becken Dichtigkeit, Lph8 Bauueberwachung Krankenhaus Rein Raum, Lph8 Bauueberwachung Logistikhalle Bodenplatte, Lph8 Bauueberwachung Maengelmeldung Sap Pm: wählt den konkreten Prüfpfad, trennt Frist, Zust... |
| `lph8-bauueberwachung-lph2` | Lph8 Bauueberwachung Erdbau Bodenkennwerte, Hoai Lph2 Variantenuntersuchung Wirtschaftlichkeit, Hoai Lph3 Kostenberechnung Budgetalarm, Hoai Lph4 Genehmigungsrisiko Bauantrag Auflagen: wählt den konkreten Prüfpfad, trennt Frist, Zuständi... |
| `lph8-bauueberwachung-trockenbau-tunnel` | Lph8 Bauueberwachung Trockenbau F30 F90, Lph8 Bauueberwachung Tunnel Spritzbeton Vortrieb, Lph8 Bauueberwachung Videoanalyse Tagesbaustelle, Lph8 Bauueberwachung Vob C Din Checklisten: wählt den konkreten Prüfpfad, trennt Frist, Zuständi... |
| `lph9-gewaehrleistungsmanagement-lph8` | Hoai Lph9 Gewaehrleistungsmanagement Fristen, Lph8 Bauueberwachung Abnahmeprotokoll Foerder Erp, Lph8 Bauueberwachung Bautagebuch Erp Import, Lph8 Bauueberwachung Bewehrung Verlegekontrolle: wählt den konkreten Prüfpfad, trennt Frist, Zu... |
| `qualitaetscheck-release-rechnungspruefung` | Hoai Qualitaetscheck Vor Release, Hoai Rechnungspruefung Architekt, Hoai Sachverstaendigenfragen, Hoai Sonderkuendigung Bgb 650r: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächs... |
| `risikoregister-sachverstaendigen-pruefung` | Hoai Risikoregister / Hoai Sachverstaendigen Pruefung / Hoai Schnittstelle Vob BGB / Hoai Streitfall Vorbereitung / 14 weitere Module: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den näc... |
| `risikoregister-sachverstaendigen-pruefung-02` | Hoai Risikoregister / Hoai Sachverstaendigen Pruefung / Hoai Schnittstelle Vob BGB / Hoai Streitfall Vorbereitung / 1 weitere Module: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den näch... |
| `risikoregister-sachverstaendigen-pruefung-03` | Hoai Risikoregister / Hoai Sachverstaendigen Pruefung / Hoai Schnittstelle Vob BGB / Hoai Streitfall Vorbereitung / 14 weitere Module: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den näc... |
| `risikoregister-sachverstaendigen-pruefung-04` | Hoai Risikoregister / Hoai Sachverstaendigen Pruefung / Hoai Schnittstelle Vob BGB / Hoai Streitfall Vorbereitung / 14 weitere Module: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den näc... |
| `vertrag-beauftragungsumfang` | Hoai Vertrag Beauftragungsumfang / Hoai Vertrag Beauftragungsumfang / Hoai Vertrag Beauftragungsumfang / Hoai Vertrag Beauftragungsumfang / 1 weitere Module: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfp... |
| `vertrag-beauftragungsumfang-vertragliche` | Hoai Vertrag Beauftragungsumfang / Hoai Vertrag Beauftragungsumfang / Hoai Vertragliche Schnittstellen: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |
| `vob-b-wiederholungsleistungen` | Hoai Vob B Schnittstelle, Hoai Wiederholungsleistungen Planungsaenderung, Hoai Zielfindungsphase Bgb 650p 650r: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Ou... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
