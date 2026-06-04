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

Automatisch generierte Komplett-Liste aller 29 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `hoai-allgemeiner-kaltstart` | HOAI-Praxis: führt durch Projektart, Rolle, LPH-Stand, Vertrag, Honorar, Druck und gewünschtes Ergebnis; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren. |
| `hoai-anwaltliche-red-team-runde` | HOAI-Praxis: sucht Fehler, falsche LPH-Zuordnung, fehlende Freigaben und Beleglücken; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren. |
| `hoai-lph-01-red-team-pruefung` | HOAI LPH 1 Grundlagenermittlung: sucht Widersprüche, vergessene Beteiligte, falsche Annahmen und unklare Zuständigkeit; mit Fokus auf Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokume... |
| `hoai-lph-02-red-team-pruefung` | HOAI LPH 2 Vorplanung: sucht Widersprüche, vergessene Beteiligte, falsche Annahmen und unklare Zuständigkeit; mit Fokus auf Grundlagen analysieren, Planungskonzept mit Alternativen, Kostenschätzung, Vorverhandlungen und Entscheidungsgrun... |
| `hoai-lph-03-red-team-pruefung` | HOAI LPH 3 Entwurfsplanung: sucht Widersprüche, vergessene Beteiligte, falsche Annahmen und unklare Zuständigkeit; mit Fokus auf stimmige Entwurfsfassung, Kostenberechnung, Termin-/Objektbeschreibung, Integration der Fachplanung und Bewe... |
| `hoai-lph-04-red-team-pruefung` | HOAI LPH 4 Genehmigungsplanung: sucht Widersprüche, vergessene Beteiligte, falsche Annahmen und unklare Zuständigkeit; mit Fokus auf öffentlich-rechtlich genehmigungsfähige Unterlagen, Anträge, Behördenabstimmung und Auflagenlogik und Be... |
| `hoai-lph-05-red-team-pruefung` | HOAI LPH 5 Ausführungsplanung: sucht Widersprüche, vergessene Beteiligte, falsche Annahmen und unklare Zuständigkeit; mit Fokus auf durcharbeitete ausführungsreife Planung, Detailpläne, Koordination der Fachplaner und Fortschreibung und... |
| `hoai-lph-06-red-team-pruefung` | HOAI LPH 6 Vorbereitung der Vergabe: sucht Widersprüche, vergessene Beteiligte, falsche Annahmen und unklare Zuständigkeit; mit Fokus auf Mengen, Leistungsverzeichnisse, Schnittstellen, Kostenanschlag und Vergabestruktur und Bewertungsan... |
| `kompendium-01-lph8-bauueberwachung-bis-lph8-bauueberwachung` | hoai-leistungsphasen-praxis: Konsolidiertes Skill-Kompendium 01; bündelt 18 frühere Spezialskills (lph8-bauueberwachung-erdbau-bodenkennwerte, hoai-lph2-variantenuntersuchung-wirtschaftlichkeit, hoai-lph3-kostenberechnung-budgetalarm, ho... |
| `kompendium-02-lph8-bauueberwachung-bis-lph8-bauueberwachung` | hoai-leistungsphasen-praxis: Konsolidiertes Skill-Kompendium 02; bündelt 18 frühere Spezialskills (lph8-bauueberwachung-dokumentenanalyse-aufmass, lph8-bauueberwachung-doppelhaus-reihenhaus, lph8-bauueberwachung-einfamilienhaus-holzbau,... |
| `kompendium-03-lph8-bauueberwachung-bis-lph8-bauueberwachung` | hoai-leistungsphasen-praxis: Konsolidiertes Skill-Kompendium 03; bündelt 18 frühere Spezialskills (lph8-bauueberwachung-klaeranlage-becken-dichtigkeit, lph8-bauueberwachung-krankenhaus-rein-raum, lph8-bauueberwachung-logistikhalle-bodenp... |
| `kompendium-04-lph8-bauueberwachung-bis-hoai-vertragliche-sc` | hoai-leistungsphasen-praxis: Konsolidiertes Skill-Kompendium 04; bündelt 18 frühere Spezialskills (lph8-bauueberwachung-trockenbau-f30-f90, lph8-bauueberwachung-tunnel-spritzbeton-vortrieb, lph8-bauueberwachung-videoanalyse-tagesbaustell... |
| `kompendium-05-hoai-bim-modell-plan-bis-hoai-lph-08-bim-und` | hoai-leistungsphasen-praxis: Konsolidiertes Skill-Kompendium 05; bündelt 18 frühere Spezialskills (hoai-bim-modell-planstand-cde-haftung, hoai-kostenobergrenze-budget-haftung, hoai-lph-01-haftungsfalle, hoai-lph-02-haftungsfalle, hoai-lp... |
| `kompendium-06-hoai-lph-08-dokument-bis-hoai-lph-08-red-team` | hoai-leistungsphasen-praxis: Konsolidiertes Skill-Kompendium 06; bündelt 18 frühere Spezialskills (hoai-lph-08-dokumentation-und-belegakte, hoai-lph-08-fachplaner-schnittstellen, hoai-lph-08-foerdermittel-und-nachweis, hoai-lph-08-genehm... |
| `kompendium-07-hoai-lph-08-risikore-bis-hoai-lph-09-kommunik` | hoai-leistungsphasen-praxis: Konsolidiertes Skill-Kompendium 07; bündelt 18 frühere Spezialskills (hoai-lph-08-risikoregister, hoai-lph-08-sachverstaendigen-pruefung, hoai-lph-08-schnittstelle-vob-bgb, hoai-lph-08-streitfall-vorbereitung... |
| `kompendium-08-hoai-lph-09-kostenst-bis-hoai-sachverstaendig` | hoai-leistungsphasen-praxis: Konsolidiertes Skill-Kompendium 08; bündelt 18 frühere Spezialskills (hoai-lph-09-kostensteuerung, hoai-lph-09-mandantenbericht, hoai-lph-09-mangel-claim-vorsorge, hoai-lph-09-nachtrag-und-change-request, hoa... |
| `kompendium-09-hoai-sigeko-projekts-bis-hoai-gesamtschuld-bg` | hoai-leistungsphasen-praxis: Konsolidiertes Skill-Kompendium 09; bündelt 18 frühere Spezialskills (hoai-sigeko-projektsteuerung-besondere-leistungen, hoai-abnahmefahrplan, hoai-abschluss-und-lessons-learned, hoai-andere-leistungsbilder-r... |
| `kompendium-10-hoai-honorarvereinba-bis-hoai-lph-01-kommunik` | hoai-leistungsphasen-praxis: Konsolidiertes Skill-Kompendium 10; bündelt 18 frühere Spezialskills (hoai-honorarvereinbarung-paragraph-7-hoai, hoai-honorarzone-bewertungspunkte-objektliste, hoai-ingenieur-perspektive, hoai-kanzlei-mandats... |
| `kompendium-11-hoai-lph-01-kostenst-bis-hoai-lph-02-bauherrn` | hoai-leistungsphasen-praxis: Konsolidiertes Skill-Kompendium 11; bündelt 18 frühere Spezialskills (hoai-lph-01-kostensteuerung, hoai-lph-01-mandantenbericht, hoai-lph-01-mangel-claim-vorsorge, hoai-lph-01-nachtrag-und-change-request, hoa... |
| `kompendium-12-hoai-lph-02-bim-und-bis-hoai-lph-02-rechnung` | hoai-leistungsphasen-praxis: Konsolidiertes Skill-Kompendium 12; bündelt 18 frühere Spezialskills (hoai-lph-02-bim-und-datenraum, hoai-lph-02-dokumentation-und-belegakte, hoai-lph-02-fachplaner-schnittstellen, hoai-lph-02-foerdermittel-u... |
| `kompendium-13-hoai-lph-02-risikore-bis-hoai-lph-03-kommunik` | hoai-leistungsphasen-praxis: Konsolidiertes Skill-Kompendium 13; bündelt 18 frühere Spezialskills (hoai-lph-02-risikoregister, hoai-lph-02-sachverstaendigen-pruefung, hoai-lph-02-schnittstelle-vob-bgb, hoai-lph-02-streitfall-vorbereitung... |
| `kompendium-14-hoai-lph-03-kostenst-bis-hoai-lph-04-bauherrn` | hoai-leistungsphasen-praxis: Konsolidiertes Skill-Kompendium 14; bündelt 18 frühere Spezialskills (hoai-lph-03-kostensteuerung, hoai-lph-03-mandantenbericht, hoai-lph-03-mangel-claim-vorsorge, hoai-lph-03-nachtrag-und-change-request, hoa... |
| `kompendium-15-hoai-lph-04-bim-und-bis-hoai-lph-04-rechnung` | hoai-leistungsphasen-praxis: Konsolidiertes Skill-Kompendium 15; bündelt 18 frühere Spezialskills (hoai-lph-04-bim-und-datenraum, hoai-lph-04-dokumentation-und-belegakte, hoai-lph-04-fachplaner-schnittstellen, hoai-lph-04-foerdermittel-u... |
| `kompendium-16-hoai-lph-04-risikore-bis-hoai-lph-05-kommunik` | hoai-leistungsphasen-praxis: Konsolidiertes Skill-Kompendium 16; bündelt 18 frühere Spezialskills (hoai-lph-04-risikoregister, hoai-lph-04-sachverstaendigen-pruefung, hoai-lph-04-schnittstelle-vob-bgb, hoai-lph-04-streitfall-vorbereitung... |
| `kompendium-17-hoai-lph-05-kostenst-bis-hoai-lph-06-bauherrn` | hoai-leistungsphasen-praxis: Konsolidiertes Skill-Kompendium 17; bündelt 18 frühere Spezialskills (hoai-lph-05-kostensteuerung, hoai-lph-05-mandantenbericht, hoai-lph-05-mangel-claim-vorsorge, hoai-lph-05-nachtrag-und-change-request, hoa... |
| `kompendium-18-hoai-lph-06-bim-und-bis-hoai-lph-06-rechnung` | hoai-leistungsphasen-praxis: Konsolidiertes Skill-Kompendium 18; bündelt 18 frühere Spezialskills (hoai-lph-06-bim-und-datenraum, hoai-lph-06-dokumentation-und-belegakte, hoai-lph-06-fachplaner-schnittstellen, hoai-lph-06-foerdermittel-u... |
| `kompendium-19-hoai-lph-06-risikore-bis-hoai-lph-07-kommunik` | hoai-leistungsphasen-praxis: Konsolidiertes Skill-Kompendium 19; bündelt 18 frühere Spezialskills (hoai-lph-06-risikoregister, hoai-lph-06-sachverstaendigen-pruefung, hoai-lph-06-schnittstelle-vob-bgb, hoai-lph-06-streitfall-vorbereitung... |
| `kompendium-20-hoai-lph-07-kostenst-bis-hoai-mandantenbrief` | hoai-leistungsphasen-praxis: Konsolidiertes Skill-Kompendium 20; bündelt 18 frühere Spezialskills (hoai-lph-07-kostensteuerung, hoai-lph-07-mandantenbericht, hoai-lph-07-mangel-claim-vorsorge, hoai-lph-07-nachtrag-und-change-request, hoa... |
| `kompendium-21-hoai-mitzuverarbeite-bis-hoai-zielfindungspha` | hoai-leistungsphasen-praxis: Konsolidiertes Skill-Kompendium 21; bündelt 18 frühere Spezialskills (hoai-mitzuverarbeitende-bausubstanz-bestand, hoai-nachtragsmanagement-planer, hoai-neun-phasen-ueberblick, hoai-oeffentliche-vergabe-plane... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
