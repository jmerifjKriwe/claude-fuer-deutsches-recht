# patentrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`patentrecht`) | [`patentrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/patentrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Schnellverschluss S-14: Sensorhalter, Gebrauchsmusterabzweigung und Messeoffenbarung** (`gebrauchsmusterrecht-schnellverschluss-sensorhalter`) | [Gesamt-PDF lesen](../testakten/gebrauchsmusterrecht-schnellverschluss-sensorhalter/gesamt-pdf/gebrauchsmusterrecht-schnellverschluss-sensorhalter_gesamt.pdf) | [`testakte-gebrauchsmusterrecht-schnellverschluss-sensorhalter.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gebrauchsmusterrecht-schnellverschluss-sensorhalter.zip) |
| **Patentrecht — Erfindungsakten Ravenstein & Moll** (`patentrecht-erfindungsakten-ravenstein-moll`) | [Gesamt-PDF lesen](../testakten/patentrecht-erfindungsakten-ravenstein-moll/gesamt-pdf/patentrecht-erfindungsakten-ravenstein-moll_gesamt.pdf) | [`testakte-patentrecht-erfindungsakten-ravenstein-moll.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-patentrecht-erfindungsakten-ravenstein-moll.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

> Großes Arbeitsplugin für Patentanwältinnen, Rechtsanwälte, Patentabteilungen und technische Gründerteams. Es führt vom rohen Erfindungsgedanken über Anspruchsentwurf, Recherche, Anmeldung, Prüfung, Freedom-to-Operate, Abmahnung, Lizenzvertrag, Einspruch und Nichtigkeit bis zur belastbaren Mandantenkommunikation.

## Wofür dieses Plugin gedacht ist

Das Plugin ist nicht nur eine Recherchehilfe. Es ist der Mandatsarbeitsplatz für Patentrecht:

- **Erfindung aufnehmen:** technische Lehre, Problem, Lösung, Ausführungsformen, Offenbarungsrisiken und fehlende Zeichnungen sauber einsammeln.
- **Anmeldung vorbereiten:** Anspruch 1, Unteransprüche, Beschreibung, Bezugszeichenliste, Figurenlogik, Alternativausführungen und Rückfragen strukturieren.
- **Patentfähigkeit prüfen:** Neuheit und erfinderische Tätigkeit nach PatG und EPÜ mit Merkmalsgliederung, nächstliegendem Stand der Technik und Aufgaben-Lösungs-Ansatz.
- **Recherche steuern:** gezielte Übergabe an das Spezialplugin [`patentrecherche`](../patentrecherche) für Espacenet, DPMAregister, DEPATISnet, EPO Register, WIPO PATENTSCOPE und weitere Datenbanken.
- **Verletzung und FTO prüfen:** Schutzbereich, wortsinngemäße Verwirklichung, Äquivalenz, Registerstand, Territory, Rechtsbestand und Design-around.
- **Abmahnung verteidigen:** Fristen, Unterlassung, Auskunft, Rückruf, Schadensersatz, negative Feststellung, Schutzschrift, Vergleichsfenster.
- **Verträge prüfen:** Patentlizenz, Exclusivity, Territory, Field of Use, Sublicensing, Improvements, Know-how, Royalties, Audit, Termination und DE/EN-Klauselrisiken.
- **Bestand angreifen oder verteidigen:** EPA-Einspruch, deutsche Nichtigkeitsklage, Beschränkung, Hilfsanträge, Fristen und Beweismittel.

## Arbeitsstil

Der Einstiegsskill fragt nicht lehrbuchartig alles ab, sondern sortiert den Fall sofort nach Dringlichkeit, Materiallage und Ziel. Bei Dokumentenupload ohne Begleittext erkennt er Fristen, Aktenart und Primärpfad. Danach schlägt er die passenden Spezialskills vor oder arbeitet direkt weiter.

## Quellen- und Zitierhygiene

- Normen und Behördeninformationen werden bevorzugt aus offiziellen Quellen geprüft: Patentgesetz auf Gesetze-im-Internet, DPMA-Informationen, DPMAregister/DEPATISnet, EPO/EPA Legal Texts, EPO Register, Espacenet, WIPO PATENTSCOPE und amtliche Gerichtsquellen.
- Rechtsprechung wird nur ausgegeben, wenn Gericht, Entscheidungsdatum, Aktenzeichen und eine frei zugängliche oder amtliche Fundstelle verifiziert sind.
- Keine BeckRS-/juris-/Paywall-Fundstellen erfinden oder als eigene Quelle verwenden.
- Wenn eine Bewertung von aktueller Amts- oder Registerlage abhängt, muss live nachgesehen werden.

## Verhältnis zu anderen Plugins

- [`patentrecherche`](../patentrecherche): tiefe Datenbankrecherche, CPC/IPC, Patentfamilien, Registerstand, Recherchebericht.
- [`gewerblicher-rechtsschutz`](../gewerblicher-rechtsschutz) und [`fachanwalt-gewerblicher-rechtsschutz`](../fachanwalt-gewerblicher-rechtsschutz): Marken, Designs, UWG, Verletzungsprozess und IP-Kollisionslagen.
- [`zitierweise-deutsches-recht`](../zitierweise-deutsches-recht): saubere Nachweise und Rechtsprechungszitate.
- [`word-legal-ai-plugin-and-skill-for-german-lawyers`](../word-legal-ai-plugin-and-skill-for-german-lawyers): Schriftsatz-, Gutachten-, Vertrags- und Mandantenbriefstil.

## Kern-Workflow

1. **Material erfassen:** Upload, Fristen, Beteiligte, Schutzrechte, Produkt/Verfahren, Technikfeld, Zielterritorien.
2. **Primärfrage festlegen:** Anmeldung, Recherche, FTO, Verletzung, Lizenz, Prüfungsbescheid, Einspruch/Nichtigkeit.
3. **Technische Lehre zerlegen:** Merkmale, Varianten, Wirkungen, Problem, Lösung, Zeichnungen, Bezugszeichen.
4. **Rechts- und Registerlage sichern:** Anmeldetag, Priorität, Veröffentlichung, Erteilung, Einspruch, Jahresgebühren, Validierungen, Rechtsstand.
5. **Spezialskill starten:** passende Skills aus diesem Plugin und bei Recherchebedarf aus `patentrecherche`.
6. **Output bauen:** Claim Draft, Merkmalsgliederung, Rechercheauftrag, Claim Chart, Risikomemo, Antwortentwurf, Lizenz-Redline oder Fristenplan.
7. **Red Team:** offene Tatsachen, technische Unschärfen, Fristen, Quellen, Gegenargumente, Mandantenrückfragen.

## Kernskills und neue internationale Module

Die folgende Tabelle nennt die ursprünglichen Kernskills. Die vollständige, automatisch generierte Liste steht direkt darunter und enthält jetzt auch UPC, PCT, USA, Kanada, Japan, Schweiz, UK, Türkei, Israel sowie Patentprozess/Eilrechtsschutz/Revocation.

| Skill | Funktion |
| --- | --- |
| `allgemein` | Einstieg, Triage und Workflow-Routing für jedes Patentrechtsmandat |
| `patentrecht-kaltstart-interview` | kurzes Mandatsprofil und wiederverwendbare Fallarchitektur |
| `erfindungsmeldung-aufnahme-und-rueckfragen` | rohe Erfindung, Offenbarung, technische Lehre und Rückfragen erfassen |
| `patentanmeldung-anspruchsentwurf` | Anspruch 1, Unteransprüche und Varianten vorbereiten |
| `beschreibung-und-zeichnungen-pruefen` | Beschreibung, Figuren, Bezugszeichen und Offenbarungsstütze prüfen |
| `neuheit-und-erfinderische-taetigkeit` | Merkmalsanalyse, Einzeldokumentprüfung, Aufgaben-Lösungs-Ansatz |
| `stand-der-technik-recherche-workflow` | Rechercheauftrag und Übergabe an `patentrecherche` |
| `gebrauchsmuster-oder-patent-route` | Patent, Gebrauchsmuster, EP/PCT, Geheimhaltung oder defensive Veröffentlichung abwägen |
| `pruefungsbescheid-dpma-epa-erwiderung` | Beanstandungen zerlegen und Erwiderung vorbereiten |
| `freedom-to-operate-und-schutzbereich` | FTO, Schutzbereich, Rechtsstand und Design-around |
| `abmahnung-patentverletzung-verteidigung` | Abmahnung, Fristen, Unterlassung, Schutzschrift, Vergleich |
| `patentverletzung-claim-chart` | claim chart für Verletzung oder Nichtverletzung |
| `vorbenutzungsrecht-paragraph-12-patg` | Vorbenutzungsrecht, Beweisführung und Risikostrategie |
| `patentlizenzvertrag-review` | Lizenzvertragsprüfung, Red Flags und Verhandlungspositionen |
| `patentlizenzvertrag-de-en-drafting` | zweisprachige Lizenzklauseln und Term-Sheet-Umsetzung |
| `erfinderbenennung-und-arbeitnehmererfindung` | Erfinderstatus, Arbeitnehmererfindung und Vergütungsschnittstellen |
| `einspruch-epa-und-nichtigkeit-bpatg` | EPA-Einspruch und Nichtigkeitsklage strategisch vorbereiten |
| `rechtsstand-register-und-fristen` | Register, Fristen, Jahresgebühren, Validierung, Einspruchs- und Klagefenster |
| `patentportfolio-und-technikstrategie` | Portfolio, Schutzzaun, Wettbewerbsmonitoring und Produktroadmap |
| `patentrecht-redteam-qualitygate` | Qualitätskontrolle für alle patentrechtlichen Outputs |

## Internationaler und prozessualer Ausbau

Neu hinzugekommen sind Skills für internationale Patentstrategie und Patentstreitigkeiten: UPC-Verletzung und Revocation, UPC-Eilverfahren, EPO-Einspruch/Beschwerde, PCT-Nationalphasen, US/UK/Kanada/Japan/Schweiz/Türkei/Israel, globale Rechtsbestandsangriffe, Schutzschrift/Protective Letter, Besichtigung, Auskunft/Rechnungslegung, Claim Construction DE/EN, Patentvergleich/Cross-License, Expertenarbeit und Prozessbudget.

Jeder dieser Skills arbeitet mit derselben Grundregel: Registerstand und lokale Verfahrensfragen live prüfen; ausländisches Recht als Arbeitsstruktur und Counsel-Briefing behandeln, nicht als scheinbar endgültige lokale Rechtsauskunft.

## Pflicht-Disclaimer im Output

Jedes externe Ergebnis enthält knapp: KI-gestützte Vorprüfung; keine amtliche Recherche; Register- und Rechtsstand sind live zu verifizieren; technische Bewertung setzt vollständige Unterlagen voraus.

## Lizenz

Apache-2.0 OR MIT. Siehe Repository-Stammverzeichnis.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 23 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Patentrecht-Plugin. Erkennt Patentanmeldung, Erfindungsmeldung, Recherche, FTO, Abmahnung, Lizenz, Einspruch, Nichtigkeit, Register- und Fristenfragen; schlägt passende Spezialskills aus di... |
| `kompendium-01-stand-der-technik-re-bis-rechtsabteilung-upc` | patentrecht: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (stand-der-technik-recherche-workflow, patr2-anmeldeverfahren-bauleiter, rechtsabteilung-upc-eilverfahren-und-deutsche-parallelstrategie) und bewahrt deren... |
| `kompendium-02-rechtsstand-register-bis-patentanmeldung-ansp` | patentrecht: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (rechtsstand-register-und-fristen, spezial-patentanmeldung-fristen-form-und-zustaendigkeit, patentanmeldung-anspruchsentwurf) und bewahrt deren Workflows, N... |
| `kompendium-03-patentlizenzvertrag-bis-spezial-anspruchsent` | patentrecht: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (patentlizenzvertrag-de-en-drafting, patentlizenzvertrag-review, spezial-anspruchsentwurf-dokumentenmatrix-und-lueckenliste) und bewahrt deren Workflows, No... |
| `kompendium-04-patentprozess-auskun-bis-abmahnung-patentverl` | patentrecht: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (patentprozess-auskunft-rechnungslegung-schadensersatz, patentportfolio-und-technikstrategie, abmahnung-patentverletzung-verteidigung) und bewahrt deren Wor... |
| `kompendium-05-beschreibung-und-zei-bis-epo-epue-einspruch-b` | patentrecht: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (beschreibung-und-zeichnungen-pruefen, einspruch-epa-und-nichtigkeit-bpatg, epo-epue-einspruch-beschwerde-beschraenkung) und bewahrt deren Workflows, Norman... |
| `kompendium-06-erfinderbenennung-un-bis-freedom-to-operate-u` | patentrecht: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (erfinderbenennung-und-arbeitnehmererfindung, erfindungsmeldung-aufnahme-und-rueckfragen, freedom-to-operate-und-schutzbereich) und bewahrt deren Workflows,... |
| `kompendium-07-gebrauchsmuster-oder-bis-israel-patentrecht-i` | patentrecht: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (gebrauchsmuster-oder-patent-route, internationaler-patentrechts-und-laendercheck, israel-patentrecht-ilpo-opposition-revocation) und bewahrt deren Workflow... |
| `kompendium-08-japan-patentrecht-jp-bis-loeschung-widerruf-n` | patentrecht: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (japan-patentrecht-jpo-ip-high-court, kanada-patentrecht-cipo-federal-court, loeschung-widerruf-nichtigkeit-global-route) und bewahrt deren Workflows, Norma... |
| `kompendium-09-neuheit-und-erfinder-bis-patentprozess-claim` | patentrecht: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (neuheit-und-erfinderische-taetigkeit, patentprozess-besichtigung-beweissicherung, patentprozess-claim-construction-de-en) und bewahrt deren Workflows, Norm... |
| `kompendium-10-patentprozess-einstw-bis-patentprozess-kosten` | patentrecht: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (patentprozess-einstweilige-verfuegung-de-upc, patentprozess-experten-und-sachverstaendige, patentprozess-kostensicherheit-und-budget) und bewahrt deren Wor... |
| `kompendium-11-patentprozess-negati-bis-patentsettlement-und` | patentrecht: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (patentprozess-negative-feststellungsklage, patentprozess-schutzschrift-und-caveat, patentsettlement-und-cross-license-litigation) und bewahrt deren Workflo... |
| `kompendium-12-patentverletzung-cla-bis-patr2-patentverletzu` | patentrecht: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (patentverletzung-claim-chart, patr2-arbeitnehmererfindung-leitfaden, patr2-patentverletzungsklage-spezial) und bewahrt deren Workflows, Normanker, Prüfprog... |
| `kompendium-13-patr2-zwangslizenz-s-bis-pruefungsbescheid-dp` | patentrecht: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (patr2-zwangslizenz-spezial, pct-laenderstrategie-und-nationalphasen, pruefungsbescheid-dpma-epa-erwiderung) und bewahrt deren Workflows, Normanker, Prüfpro... |
| `kompendium-14-rechtsabteilung-empl-bis-rechtsabteilung-free` | patentrecht: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (rechtsabteilung-employee-invention-im-konzernprojekt, rechtsabteilung-frand-verteidigung-bei-sep-abmahnung, rechtsabteilung-freedom-to-operate-vor-product-... |
| `kompendium-15-rechtsabteilung-prop-bis-spezial-erfindungsau` | patentrecht: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (rechtsabteilung-proportionalitaet-der-unterlassung-139-patg, schweiz-patentrecht-bundespatentgericht, spezial-erfindungsaufnahme-tatbestand-beweis-und-bele... |
| `kompendium-16-spezial-patentrechts-bis-uk-patentrecht-paten` | patentrecht: Konsolidiertes Skill-Kompendium 16; bündelt 3 frühere Spezialskills (spezial-patentrechts-erstpruefung-und-mandatsziel, tuerkei-patentrecht-turkpatent-ip-courts, uk-patentrecht-patents-court-ipec-ukipo) und bewahrt deren Wor... |
| `kompendium-17-upc-einstweilige-mas-bis-upc-widerruf-und-wid` | patentrecht: Konsolidiertes Skill-Kompendium 17; bündelt 3 frühere Spezialskills (upc-einstweilige-massnahmen, upc-verletzung-und-rechtsbestand, upc-widerruf-und-widerklage-revocation) und bewahrt deren Workflows, Normanker, Prüfprogramm... |
| `kompendium-18-us-patent-law-pto-pt-bis-vorbenutzungsrecht-p` | patentrecht: Konsolidiertes Skill-Kompendium 18; bündelt 3 frühere Spezialskills (us-patent-law-pto-ptab, us-patent-litigation-district-court-itc, vorbenutzungsrecht-paragraph-12-patg) und bewahrt deren Workflows, Normanker, Prüfprogramm... |
| `patentrecht-kaltstart-interview` | Kaltstart-Interview für Patentrechtsmandate. Erstellt ein kurzes Profil zu Mandant, Technik, Ziel, Territorien, Fristen, Dokumentenlage, Risiko und gewünschtem Output; speichert keine Geheimnisse, sondern strukturiert die nächsten Skills. |
| `patentrecht-redteam-qualitygate` | Red-Team- und Qualitätsgate für patentrechtliche Outputs: prüft Fristen, Registerstand, Anspruchsfassung, technische Annahmen, Quellen, Beweise, Zitierhygiene, offene Tatsachen und Mandantenrisiken. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin patentrecht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin patentrecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
