# Megaprompt: umweltschutzverband-verbandsklage

> *Achtung: Dies ist ein experimentelles Mega-Prompt-Markdown, das einen kompletten Klotzkette-Plugin in eine einzige Datei zusammenfuehrt. Keine Haftung, keine Gewaehr. Nur zum Ausprobieren der Skills auch ohne Claude Code; keine Rechtsberatung. Vor Verwendung im Mandat anwaltlich pruefen.*
>
> *Caution: This is an experimental Mega-Prompt Markdown that consolidates a full Klotzkette plugin into a single file. No warranty, no liability. For exploration with chat tools that do not run Claude Code only; not legal advice.*

**Verwendung:** Diesen gesamten Text in einen Chat ohne Claude-Code-Integration einfuegen (oder als Datei hochladen). Der Chat-Agent erhaelt damit die gebuendelten Skills dieses Plugins als Kontext. Eine Replikation des vollen Plugin-Verhaltens ist nicht garantiert — der Megaprompt ist eine Best-Effort-Kompression.


## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 100 Skills des Plugins `umweltschutzverband-verbandsklage`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Umweltschutzverband Verbandsklage: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing …
2. **anerkennung-und-klagebefugnis-pruefen** — Umweltschutzverband Verbandsklage: Anerkennung und Klagebefugnis prüfen. Anerkennung und Klagebefugnis prüfen im Fachgeb…
3. **oeffentlichkeitsarbeit** — Umweltschutzverband Verbandsklage: Öffentlichkeitsarbeit ohne Risiko. Öffentlichkeitsarbeit ohne Risiko im Fachgebiet Um…
4. **einwendungsfrist** — Umweltschutzverband Verbandsklage: Einwendungsfrist und Präklusion. Einwendungsfrist und Präklusion im Fachgebiet Umwelt…
5. **vergleich-und-nebenbestimmungen** — Umweltschutzverband Verbandsklage: Vergleich und Nebenbestimmungen. Vergleich und Nebenbestimmungen im Fachgebiet Umwelt…
6. **aktenauswertung-behoerdenordner** — Umweltschutzverband Verbandsklage: Aktenauswertung Behördenordner. Aktenauswertung Behördenordner im Fachgebiet Umweltsc…
7. **umwrg-anwendungsbereich-routen** — Umweltschutzverband Verbandsklage: UmwRG-Anwendungsbereich routen. UmwRG-Anwendungsbereich routen im Fachgebiet Umweltsc…
8. **artenschutz-fachbeitrag-lesen** — Umweltschutzverband Verbandsklage: Artenschutz-Fachbeitrag lesen. Artenschutz-Fachbeitrag lesen im Fachgebiet Umweltschu…
9. **eilrechtsschutz-gegen-vollzug** — Umweltschutzverband Verbandsklage: Eilrechtsschutz gegen Vollzug. Eilrechtsschutz gegen Vollzug im Fachgebiet Umweltschu…
10. **gutachterfragen-formulieren** — Umweltschutzverband Verbandsklage: Gutachterfragen formulieren. Gutachterfragen formulieren im Fachgebiet Umweltschutzve…
11. **aarhus-argumentationslinie** — Umweltschutzverband Verbandsklage: Aarhus-Argumentationslinie. Aarhus-Argumentationslinie im Fachgebiet Umweltschutzverb…
12. **anfrage-umweltakte-uvp** — Umweltschutzverband Verbandsklage: UIG-Anfrage für Umweltakte. UIG-Anfrage für Umweltakte im Fachgebiet Umweltschutzverb…
13. **bimschg-genehmigung-pruefen** — Umweltschutzverband Verbandsklage: BImSchG-Genehmigung prüfen. BImSchG-Genehmigung prüfen im Fachgebiet Umweltschutzverb…
14. **planfeststellung-angreifen** — Umweltschutzverband Verbandsklage: Planfeststellung angreifen. Planfeststellung angreifen im Fachgebiet Umweltschutzverb…
15. **uvp-pflicht-und-vorpruefung** — Umweltschutzverband Verbandsklage: UVP-Pflicht und Vorprüfung. UVP-Pflicht und Vorprüfung im Fachgebiet Umweltschutzverb…

---

## Skill: `kaltstart-triage`

_Umweltschutzverband Verbandsklage: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe._

# Umweltschutzverband Verbandsklage - Allgemeiner Einstieg

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Umweltschutzverband Verbandsklage** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1922 Abs. 1 BGB` — Gesamtrechtsnachfolge.
- `§ 1937 BGB` — Testament.
- `§ 1942 BGB` — Anfall und Ausschlagung.
- `§ 1953 BGB` — Wirkung der Ausschlagung.
- `§ 1967 BGB` — Erbenhaftung.
- `§ 2032 BGB` — Erbengemeinschaft.
- `§ 2042 BGB` — Auseinandersetzung.
- `§ 2303 BGB` — Pflichtteil.
- `§ 2353 BGB` — Erbschein.
- `§ 352 FamFG` — Erbscheinsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Startfragen

1. Wer nutzt das Plugin: Laie, Verband, Kanzlei, Behörde, Unternehmen, Presse, Verwaltung oder Fachabteilung?
2. Welche Entscheidung steht jetzt an und welche Frist läuft?
3. Welche Dokumente liegen vor, welche fehlen und welche Quelle muss live geprüft werden?
4. Welche Behörde, welches Gericht, welches Register oder welcher private Akteur ist betroffen?
5. Soll am Ende ein Antrag, ein Widerspruch, eine Klage-/Eilantragslinie, ein Dashboard, ein Memo oder ein Schreiben entstehen?

## Workflow

1. Sachverhalt in Akte, Normpfad, Zuständigkeit, Frist, Beweis und Ziel zerlegen.
2. Die einschlägige Norm nicht aus dem Gedächtnis final behaupten, sondern als Live-Check gegen amtliche Quelle markieren.
3. Ablehnungs-, Kosten-, Zuständigkeits- und Beweisrisiken offen in einer Ampel führen.
4. Bei Mehr-Ebenen-Recht immer Bund, Land, Kommune, EU/international und Spezialgesetz trennen.
5. Ausgabe mit konkretem nächsten Schritt, offenen Rückfragen und einer kurzen Fassung für Nichtjuristen schließen.

## Typische Ausgaben

- Prüfvermerk mit Normpfad und Live-Check-Liste
- Fristen- und Zuständigkeitsmatrix
- Entwurf für Antrag, Widerspruch, Klagebaustein oder Behördenbrief
- Dashboard-/Tracker-Eintrag mit Status, Risiko und nächster Aktion

## Red Flags

- blindes Zitieren nicht verifizierter Rechtsprechung oder alter Gesetzesstände
- falsche Behörde, falscher Rechtsweg oder unbemerkte Spezialzuständigkeit
- Gebühren-, Frist-, Präklusions-, Geheimschutz-, Datenschutz- oder Drittbetroffenenproblem
- politisch klingende Bewertung ohne saubere Rechtsgrundlage und Beleglogik

## Quellen- und Qualitätsregel

Primär mit amtlichen Gesetzestexten, Behördenhinweisen, Gerichtsentscheidungen mit Datum/Aktenzeichen und frei prüfbaren Quellen arbeiten. Literatur, Datenbanken hinter Paywalls und Fundstellen ohne Nutzerquelle nicht behaupten. Wenn Landesrecht, EU-Recht oder ausländisches Recht berührt ist, den Rechtsstand ausdrücklich live prüfen und die Ausgabe als Arbeitsfassung kennzeichnen.

---

## Skill: `anerkennung-und-klagebefugnis-pruefen`

_Umweltschutzverband Verbandsklage: Anerkennung und Klagebefugnis prüfen. Anerkennung und Klagebefugnis prüfen im Fachgebiet Umweltschutzverband Verbandsklage als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Umweltverbandsklage._

# Anerkennung Und Klagebefugnis Pruefen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UmwRG; BImSchG; § 47 VwGO, Naturschutz, Klima, Verbandsklage und Eilrechtsschutz — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1922 Abs. 1 BGB` — Gesamtrechtsnachfolge.
- `§ 1937 BGB` — Testament.
- `§ 1942 BGB` — Anfall und Ausschlagung.
- `§ 1953 BGB` — Wirkung der Ausschlagung.
- `§ 1967 BGB` — Erbenhaftung.
- `§ 2032 BGB` — Erbengemeinschaft.
- `§ 2042 BGB` — Auseinandersetzung.
- `§ 2303 BGB` — Pflichtteil.
- `§ 2353 BGB` — Erbschein.
- `§ 352 FamFG` — Erbscheinsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- UmwRG, UVPG, BNatSchG, WHG, BImSchG, BauGB
- § 47 VwGO Normenkontrolle, § 80/123 VwGO Eilrechtsschutz
- Anerkannte Umweltvereinigungen, Beteiligung, Präklusionsfragen
- UIG/Aarhus-Logik und Öffentlichkeitsbeteiligung

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 47 VwG
- § 352 FamFG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `oeffentlichkeitsarbeit`

_Umweltschutzverband Verbandsklage: Öffentlichkeitsarbeit ohne Risiko. Öffentlichkeitsarbeit ohne Risiko im Fachgebiet Umweltschutzverband Verbandsklage als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Umweltverbandsklage._

# Oeffentlichkeitsarbeit Ohne Risiko

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UmwRG; BImSchG; § 47 VwGO, Naturschutz, Klima, Verbandsklage und Eilrechtsschutz — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1922 Abs. 1 BGB` — Gesamtrechtsnachfolge.
- `§ 1937 BGB` — Testament.
- `§ 1942 BGB` — Anfall und Ausschlagung.
- `§ 1953 BGB` — Wirkung der Ausschlagung.
- `§ 1967 BGB` — Erbenhaftung.
- `§ 2032 BGB` — Erbengemeinschaft.
- `§ 2042 BGB` — Auseinandersetzung.
- `§ 2303 BGB` — Pflichtteil.
- `§ 2353 BGB` — Erbschein.
- `§ 352 FamFG` — Erbscheinsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- UmwRG, UVPG, BNatSchG, WHG, BImSchG, BauGB
- § 47 VwGO Normenkontrolle, § 80/123 VwGO Eilrechtsschutz
- Anerkannte Umweltvereinigungen, Beteiligung, Präklusionsfragen
- UIG/Aarhus-Logik und Öffentlichkeitsbeteiligung

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `einwendungsfrist`

_Umweltschutzverband Verbandsklage: Einwendungsfrist und Präklusion. Einwendungsfrist und Präklusion im Fachgebiet Umweltschutzverband Verbandsklage als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Umweltverbandsklage._

# Einwendungsfrist Und Praeklusion

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UmwRG; BImSchG; § 47 VwGO, Naturschutz, Klima, Verbandsklage und Eilrechtsschutz — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1922 Abs. 1 BGB` — Gesamtrechtsnachfolge.
- `§ 1937 BGB` — Testament.
- `§ 1942 BGB` — Anfall und Ausschlagung.
- `§ 1953 BGB` — Wirkung der Ausschlagung.
- `§ 1967 BGB` — Erbenhaftung.
- `§ 2032 BGB` — Erbengemeinschaft.
- `§ 2042 BGB` — Auseinandersetzung.
- `§ 2303 BGB` — Pflichtteil.
- `§ 2353 BGB` — Erbschein.
- `§ 352 FamFG` — Erbscheinsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- UmwRG, UVPG, BNatSchG, WHG, BImSchG, BauGB
- § 47 VwGO Normenkontrolle, § 80/123 VwGO Eilrechtsschutz
- Anerkannte Umweltvereinigungen, Beteiligung, Präklusionsfragen
- UIG/Aarhus-Logik und Öffentlichkeitsbeteiligung

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `vergleich-und-nebenbestimmungen`

_Umweltschutzverband Verbandsklage: Vergleich und Nebenbestimmungen. Vergleich und Nebenbestimmungen im Fachgebiet Umweltschutzverband Verbandsklage als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Umweltverbandsklage._

# Vergleich Und Nebenbestimmungen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UmwRG; BImSchG; § 47 VwGO, Naturschutz, Klima, Verbandsklage und Eilrechtsschutz — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1922 Abs. 1 BGB` — Gesamtrechtsnachfolge.
- `§ 1937 BGB` — Testament.
- `§ 1942 BGB` — Anfall und Ausschlagung.
- `§ 1953 BGB` — Wirkung der Ausschlagung.
- `§ 1967 BGB` — Erbenhaftung.
- `§ 2032 BGB` — Erbengemeinschaft.
- `§ 2042 BGB` — Auseinandersetzung.
- `§ 2303 BGB` — Pflichtteil.
- `§ 2353 BGB` — Erbschein.
- `§ 352 FamFG` — Erbscheinsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- UmwRG, UVPG, BNatSchG, WHG, BImSchG, BauGB
- § 47 VwGO Normenkontrolle, § 80/123 VwGO Eilrechtsschutz
- Anerkannte Umweltvereinigungen, Beteiligung, Präklusionsfragen
- UIG/Aarhus-Logik und Öffentlichkeitsbeteiligung

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `aktenauswertung-behoerdenordner`

_Umweltschutzverband Verbandsklage: Aktenauswertung Behördenordner. Aktenauswertung Behördenordner im Fachgebiet Umweltschutzverband Verbandsklage als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Umweltverbandsklage._

# Aktenauswertung Behördenordner

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UmwRG; BImSchG; § 47 VwGO, Naturschutz, Klima, Verbandsklage und Eilrechtsschutz — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1922 Abs. 1 BGB` — Gesamtrechtsnachfolge.
- `§ 1937 BGB` — Testament.
- `§ 1942 BGB` — Anfall und Ausschlagung.
- `§ 1953 BGB` — Wirkung der Ausschlagung.
- `§ 1967 BGB` — Erbenhaftung.
- `§ 2032 BGB` — Erbengemeinschaft.
- `§ 2042 BGB` — Auseinandersetzung.
- `§ 2303 BGB` — Pflichtteil.
- `§ 2353 BGB` — Erbschein.
- `§ 352 FamFG` — Erbscheinsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- UmwRG, UVPG, BNatSchG, WHG, BImSchG, BauGB
- § 47 VwGO Normenkontrolle, § 80/123 VwGO Eilrechtsschutz
- Anerkannte Umweltvereinigungen, Beteiligung, Präklusionsfragen
- UIG/Aarhus-Logik und Öffentlichkeitsbeteiligung

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 47 VwG
- § 352 FamFG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `umwrg-anwendungsbereich-routen`

_Umweltschutzverband Verbandsklage: UmwRG-Anwendungsbereich routen. UmwRG-Anwendungsbereich routen im Fachgebiet Umweltschutzverband Verbandsklage als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Umweltverbandsklage._

# Umwrg Anwendungsbereich Routen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UmwRG; BImSchG; § 47 VwGO, Naturschutz, Klima, Verbandsklage und Eilrechtsschutz — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1922 Abs. 1 BGB` — Gesamtrechtsnachfolge.
- `§ 1937 BGB` — Testament.
- `§ 1942 BGB` — Anfall und Ausschlagung.
- `§ 1953 BGB` — Wirkung der Ausschlagung.
- `§ 1967 BGB` — Erbenhaftung.
- `§ 2032 BGB` — Erbengemeinschaft.
- `§ 2042 BGB` — Auseinandersetzung.
- `§ 2303 BGB` — Pflichtteil.
- `§ 2353 BGB` — Erbschein.
- `§ 352 FamFG` — Erbscheinsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- UmwRG, UVPG, BNatSchG, WHG, BImSchG, BauGB
- § 47 VwGO Normenkontrolle, § 80/123 VwGO Eilrechtsschutz
- Anerkannte Umweltvereinigungen, Beteiligung, Präklusionsfragen
- UIG/Aarhus-Logik und Öffentlichkeitsbeteiligung

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `artenschutz-fachbeitrag-lesen`

_Umweltschutzverband Verbandsklage: Artenschutz-Fachbeitrag lesen. Artenschutz-Fachbeitrag lesen im Fachgebiet Umweltschutzverband Verbandsklage als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Umweltverbandsklage._

# Artenschutz Fachbeitrag Lesen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UmwRG; BImSchG; § 47 VwGO, Naturschutz, Klima, Verbandsklage und Eilrechtsschutz — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1922 Abs. 1 BGB` — Gesamtrechtsnachfolge.
- `§ 1937 BGB` — Testament.
- `§ 1942 BGB` — Anfall und Ausschlagung.
- `§ 1953 BGB` — Wirkung der Ausschlagung.
- `§ 1967 BGB` — Erbenhaftung.
- `§ 2032 BGB` — Erbengemeinschaft.
- `§ 2042 BGB` — Auseinandersetzung.
- `§ 2303 BGB` — Pflichtteil.
- `§ 2353 BGB` — Erbschein.
- `§ 352 FamFG` — Erbscheinsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- UmwRG, UVPG, BNatSchG, WHG, BImSchG, BauGB
- § 47 VwGO Normenkontrolle, § 80/123 VwGO Eilrechtsschutz
- Anerkannte Umweltvereinigungen, Beteiligung, Präklusionsfragen
- UIG/Aarhus-Logik und Öffentlichkeitsbeteiligung

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 47 VwG
- § 352 FamFG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `eilrechtsschutz-gegen-vollzug`

_Umweltschutzverband Verbandsklage: Eilrechtsschutz gegen Vollzug. Eilrechtsschutz gegen Vollzug im Fachgebiet Umweltschutzverband Verbandsklage als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Umweltverbandsklage._

# Eilrechtsschutz Gegen Vollzug

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UmwRG; BImSchG; § 47 VwGO, Naturschutz, Klima, Verbandsklage und Eilrechtsschutz — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1922 Abs. 1 BGB` — Gesamtrechtsnachfolge.
- `§ 1937 BGB` — Testament.
- `§ 1942 BGB` — Anfall und Ausschlagung.
- `§ 1953 BGB` — Wirkung der Ausschlagung.
- `§ 1967 BGB` — Erbenhaftung.
- `§ 2032 BGB` — Erbengemeinschaft.
- `§ 2042 BGB` — Auseinandersetzung.
- `§ 2303 BGB` — Pflichtteil.
- `§ 2353 BGB` — Erbschein.
- `§ 352 FamFG` — Erbscheinsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- UmwRG, UVPG, BNatSchG, WHG, BImSchG, BauGB
- § 47 VwGO Normenkontrolle, § 80/123 VwGO Eilrechtsschutz
- Anerkannte Umweltvereinigungen, Beteiligung, Präklusionsfragen
- UIG/Aarhus-Logik und Öffentlichkeitsbeteiligung

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `gutachterfragen-formulieren`

_Umweltschutzverband Verbandsklage: Gutachterfragen formulieren. Gutachterfragen formulieren im Fachgebiet Umweltschutzverband Verbandsklage als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Umweltverbandsklage._

# Gutachterfragen Formulieren

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UmwRG; BImSchG; § 47 VwGO, Naturschutz, Klima, Verbandsklage und Eilrechtsschutz — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1922 Abs. 1 BGB` — Gesamtrechtsnachfolge.
- `§ 1937 BGB` — Testament.
- `§ 1942 BGB` — Anfall und Ausschlagung.
- `§ 1953 BGB` — Wirkung der Ausschlagung.
- `§ 1967 BGB` — Erbenhaftung.
- `§ 2032 BGB` — Erbengemeinschaft.
- `§ 2042 BGB` — Auseinandersetzung.
- `§ 2303 BGB` — Pflichtteil.
- `§ 2353 BGB` — Erbschein.
- `§ 352 FamFG` — Erbscheinsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- UmwRG, UVPG, BNatSchG, WHG, BImSchG, BauGB
- § 47 VwGO Normenkontrolle, § 80/123 VwGO Eilrechtsschutz
- Anerkannte Umweltvereinigungen, Beteiligung, Präklusionsfragen
- UIG/Aarhus-Logik und Öffentlichkeitsbeteiligung

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `aarhus-argumentationslinie`

_Umweltschutzverband Verbandsklage: Aarhus-Argumentationslinie. Aarhus-Argumentationslinie im Fachgebiet Umweltschutzverband Verbandsklage als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Umweltverbandsklage._

# Aarhus Argumentationslinie

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UmwRG; BImSchG; § 47 VwGO, Naturschutz, Klima, Verbandsklage und Eilrechtsschutz — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1922 Abs. 1 BGB` — Gesamtrechtsnachfolge.
- `§ 1937 BGB` — Testament.
- `§ 1942 BGB` — Anfall und Ausschlagung.
- `§ 1953 BGB` — Wirkung der Ausschlagung.
- `§ 1967 BGB` — Erbenhaftung.
- `§ 2032 BGB` — Erbengemeinschaft.
- `§ 2042 BGB` — Auseinandersetzung.
- `§ 2303 BGB` — Pflichtteil.
- `§ 2353 BGB` — Erbschein.
- `§ 352 FamFG` — Erbscheinsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- UmwRG, UVPG, BNatSchG, WHG, BImSchG, BauGB
- § 47 VwGO Normenkontrolle, § 80/123 VwGO Eilrechtsschutz
- Anerkannte Umweltvereinigungen, Beteiligung, Präklusionsfragen
- UIG/Aarhus-Logik und Öffentlichkeitsbeteiligung

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 47 VwG
- § 352 FamFG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `anfrage-umweltakte-uvp`

_Umweltschutzverband Verbandsklage: UIG-Anfrage für Umweltakte. UIG-Anfrage für Umweltakte im Fachgebiet Umweltschutzverband Verbandsklage als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Umweltverbandsklage._

# Uig Anfrage Fuer Umweltakte

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UmwRG; BImSchG; § 47 VwGO, Naturschutz, Klima, Verbandsklage und Eilrechtsschutz — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1922 Abs. 1 BGB` — Gesamtrechtsnachfolge.
- `§ 1937 BGB` — Testament.
- `§ 1942 BGB` — Anfall und Ausschlagung.
- `§ 1953 BGB` — Wirkung der Ausschlagung.
- `§ 1967 BGB` — Erbenhaftung.
- `§ 2032 BGB` — Erbengemeinschaft.
- `§ 2042 BGB` — Auseinandersetzung.
- `§ 2303 BGB` — Pflichtteil.
- `§ 2353 BGB` — Erbschein.
- `§ 352 FamFG` — Erbscheinsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- UmwRG, UVPG, BNatSchG, WHG, BImSchG, BauGB
- § 47 VwGO Normenkontrolle, § 80/123 VwGO Eilrechtsschutz
- Anerkannte Umweltvereinigungen, Beteiligung, Präklusionsfragen
- UIG/Aarhus-Logik und Öffentlichkeitsbeteiligung

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 47 VwG
- § 352 FamFG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `bimschg-genehmigung-pruefen`

_Umweltschutzverband Verbandsklage: BImSchG-Genehmigung prüfen. BImSchG-Genehmigung prüfen im Fachgebiet Umweltschutzverband Verbandsklage als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Umweltverbandsklage._

# Bimschg Genehmigung Pruefen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UmwRG; BImSchG; § 47 VwGO, Naturschutz, Klima, Verbandsklage und Eilrechtsschutz — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1922 Abs. 1 BGB` — Gesamtrechtsnachfolge.
- `§ 1937 BGB` — Testament.
- `§ 1942 BGB` — Anfall und Ausschlagung.
- `§ 1953 BGB` — Wirkung der Ausschlagung.
- `§ 1967 BGB` — Erbenhaftung.
- `§ 2032 BGB` — Erbengemeinschaft.
- `§ 2042 BGB` — Auseinandersetzung.
- `§ 2303 BGB` — Pflichtteil.
- `§ 2353 BGB` — Erbschein.
- `§ 352 FamFG` — Erbscheinsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- UmwRG, UVPG, BNatSchG, WHG, BImSchG, BauGB
- § 47 VwGO Normenkontrolle, § 80/123 VwGO Eilrechtsschutz
- Anerkannte Umweltvereinigungen, Beteiligung, Präklusionsfragen
- UIG/Aarhus-Logik und Öffentlichkeitsbeteiligung

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `planfeststellung-angreifen`

_Umweltschutzverband Verbandsklage: Planfeststellung angreifen. Planfeststellung angreifen im Fachgebiet Umweltschutzverband Verbandsklage als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Umweltverbandsklage._

# Planfeststellung Angreifen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UmwRG; BImSchG; § 47 VwGO, Naturschutz, Klima, Verbandsklage und Eilrechtsschutz — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1922 Abs. 1 BGB` — Gesamtrechtsnachfolge.
- `§ 1937 BGB` — Testament.
- `§ 1942 BGB` — Anfall und Ausschlagung.
- `§ 1953 BGB` — Wirkung der Ausschlagung.
- `§ 1967 BGB` — Erbenhaftung.
- `§ 2032 BGB` — Erbengemeinschaft.
- `§ 2042 BGB` — Auseinandersetzung.
- `§ 2303 BGB` — Pflichtteil.
- `§ 2353 BGB` — Erbschein.
- `§ 352 FamFG` — Erbscheinsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- UmwRG, UVPG, BNatSchG, WHG, BImSchG, BauGB
- § 47 VwGO Normenkontrolle, § 80/123 VwGO Eilrechtsschutz
- Anerkannte Umweltvereinigungen, Beteiligung, Präklusionsfragen
- UIG/Aarhus-Logik und Öffentlichkeitsbeteiligung

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `uvp-pflicht-und-vorpruefung`

_Umweltschutzverband Verbandsklage: UVP-Pflicht und Vorprüfung. UVP-Pflicht und Vorprüfung im Fachgebiet Umweltschutzverband Verbandsklage als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Umweltverbandsklage._

# Uvp Pflicht Und Vorpruefung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UmwRG; BImSchG; § 47 VwGO, Naturschutz, Klima, Verbandsklage und Eilrechtsschutz — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1922 Abs. 1 BGB` — Gesamtrechtsnachfolge.
- `§ 1937 BGB` — Testament.
- `§ 1942 BGB` — Anfall und Ausschlagung.
- `§ 1953 BGB` — Wirkung der Ausschlagung.
- `§ 1967 BGB` — Erbenhaftung.
- `§ 2032 BGB` — Erbengemeinschaft.
- `§ 2042 BGB` — Auseinandersetzung.
- `§ 2303 BGB` — Pflichtteil.
- `§ 2353 BGB` — Erbschein.
- `§ 352 FamFG` — Erbscheinsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- UmwRG, UVPG, BNatSchG, WHG, BImSchG, BauGB
- § 47 VwGO Normenkontrolle, § 80/123 VwGO Eilrechtsschutz
- Anerkannte Umweltvereinigungen, Beteiligung, Präklusionsfragen
- UIG/Aarhus-Logik und Öffentlichkeitsbeteiligung

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

