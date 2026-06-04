---
name: kompendium-06-workflow-weg-anfecht-bis-spezial-wohnungseige
description: "fachanwalt-miet-wohnungseigentumsrecht: Konsolidiertes Skill-Kompendium 06; bündelt 10 frühere Spezialskills (workflow-weg-anfechtung-start, workflow-weg-eigentuemer-intake, workflow-weg-protokoll-nachbereiten, workflow-weg-versammlung-vorbereiten, workflow-whatsapp-email-beweis und 5 weitere) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 06 - fachanwalt-miet-wohnungseigentumsrecht

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `workflow-weg-anfechtung-start` | WEG-Anfechtung-Start: Workflow-Skill für Miet- und WEG-Recht; prüft Anfechtungsziel, Kläger, Fristen, Beklagte, Beschlussmangel; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output. |
| `workflow-weg-eigentuemer-intake` | WEG-Eigentümer-Intake: Workflow-Skill für Miet- und WEG-Recht; klärt Beschluss, Gemeinschaft, Verwalter, Teilungserklärung, Fristen und Ziel; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output. |
| `workflow-weg-protokoll-nachbereiten` | WEG-Protokoll nachbereiten: Workflow-Skill für Miet- und WEG-Recht; prüft Beschlusswortlaut, Verkündung, Sammlung, Fristen und Fehler; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output. |
| `workflow-weg-versammlung-vorbereiten` | Eigentümerversammlung vorbereiten: Workflow-Skill für Miet- und WEG-Recht; macht Einladung, TOPs, Beschlussvorschläge und Mehrheiten praxistauglich; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output. |
| `workflow-whatsapp-email-beweis` | WhatsApp-/E-Mail-Beweis: Workflow-Skill für Miet- und WEG-Recht; wertet informelle Nachrichten für Zugang, Kenntnis, Fristen und Einigungen aus; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output. |
| `beschlussanfechtung-spezial-fristen` | Beschlussanfechtung nach § 44 WEG spezial: Klagefrist 1 Monat, Begruendungsfrist 2 Monate ab Beschluss, formale Fehler vs. materielle Mangelhaftigkeit, ausschliesslich Eigentuemerklage nicht Mieter. Pruefraster und Klageaufbau. Routet in fachanwalt-miet-wohnungseigentumsrecht-weg-beschlussanfechtung. |
| `spezial-abrechnungsfrist-nachforderung` | Abrechnungsfrist und Nachforderung aus Betriebskosten: § 556 Abs. 3 BGB, Zugang, Jahresfrist, Vermieter-Nichtvertretenmüssen, Guthaben, Korrekturen, WEG-Verzögerung, Gewerberaumabweichungen und Prozessstrategie. |
| `spezial-erhalt-fristennotiz-und-naechster-schritt` | Erhalt: Fristennotiz und nächster Schritt im Miet- und WEG-Recht: fachlich vertiefter Spezialskill mit Normenradar (BGB/WEG/BetrKV/GEG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |
| `spezial-fristlose-kuendigung-stoerung` | Fristlose Kündigung wegen Störung: Spezial-Skill im Miet- und Wohnungseigentumsrecht; ordnet Abmahnung, Pflichtverletzung, Wiederholung, Beweise und Interessenabwägung; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt. |
| `spezial-wohnungseigentumsrecht-fristen-form-und-zustaendigkeit` | Wohnungseigentumsrecht: Fristen, Form, Zuständigkeit und Rechtsweg im Miet- und WEG-Recht: fachlich vertiefter Spezialskill mit Normenradar (BGB/WEG/BetrKV/GEG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `workflow-weg-anfechtung-start`

**Frühere Beschreibung:** WEG-Anfechtung-Start: Workflow-Skill für Miet- und WEG-Recht; prüft Anfechtungsziel, Kläger, Fristen, Beklagte, Beschlussmangel; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output.

# WEG-Anfechtung-Start

## V90 Fachkern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `WEG-Anfechtung-Start` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Dieser Workflow-Skill macht den Einstieg in `fachanwalt-miet-wohnungseigentumsrecht` leichter. Schwerpunkt: prüft Anfechtungsziel, Kläger, Fristen, Beklagte, Beschlussmangel.

## Kaltstart
Arbeite zuerst mit vorhandenen Unterlagen. Frage nur, was die nächste Entscheidung verändert:
1. Rolle und Ziel der fragenden Person.
2. Objekt und Rechtsverhältnis: Wohnraum, Gewerberaum, WEG, Hausverwaltung oder Mischfall.
3. Frist, Zugang, Termin oder Eilrisiko.
4. Vorhandene Belege und fehlende Schlüsselunterlagen.
5. Gewünschter Output: Erklärung, Tabelle, Brief, Beschluss, Schriftsatz oder Verhandlungsplan.

## Arbeitsworkflow
1. **Kurzlage:** Falltyp, Frist, Risiko, Unterlagen und Ziel in fünf Zeilen.
2. **Weichen:** Zwei bis fünf entscheidende Fragen isolieren; keine Vollprüfung ohne Anlass.
3. **Belege:** Dokumente, Fotos, Nachrichten, Rechnungen und Protokolle verwerten; Lückenliste erzeugen.
4. **Recht:** Normen aus BGB, WEG, BetrKV, HeizkostenV, GEG/CO2KostAufG nur in aktueller Fassung verwenden.
5. **Anschluss:** Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
6. **Output:** Handlungsfähiges Ergebnis mit nächstem Schritt, Frist und Verantwortlichem.

## Qualitätsmaßstab
- Für Laien klar erklären, welche Gefahr besteht und was heute zu tun ist.
- Für Berufsanfänger sichtbar machen, welche Anspruchsgrundlage, Beweislast und Frist den Fall trägt.
- Für erfahrene Nutzer knapp bleiben und auf den entscheidenden Streitpunkt zielen.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 2. `workflow-weg-eigentuemer-intake`

**Frühere Beschreibung:** WEG-Eigentümer-Intake: Workflow-Skill für Miet- und WEG-Recht; klärt Beschluss, Gemeinschaft, Verwalter, Teilungserklärung, Fristen und Ziel; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output.

# WEG-Eigentümer-Intake

## V90 Fachkern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `WEG-Eigentümer-Intake` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Dieser Workflow-Skill macht den Einstieg in `fachanwalt-miet-wohnungseigentumsrecht` leichter. Schwerpunkt: klärt Beschluss, Gemeinschaft, Verwalter, Teilungserklärung, Fristen und Ziel.

## Kaltstart
Arbeite zuerst mit vorhandenen Unterlagen. Frage nur, was die nächste Entscheidung verändert:
1. Rolle und Ziel der fragenden Person.
2. Objekt und Rechtsverhältnis: Wohnraum, Gewerberaum, WEG, Hausverwaltung oder Mischfall.
3. Frist, Zugang, Termin oder Eilrisiko.
4. Vorhandene Belege und fehlende Schlüsselunterlagen.
5. Gewünschter Output: Erklärung, Tabelle, Brief, Beschluss, Schriftsatz oder Verhandlungsplan.

## Arbeitsworkflow
1. **Kurzlage:** Falltyp, Frist, Risiko, Unterlagen und Ziel in fünf Zeilen.
2. **Weichen:** Zwei bis fünf entscheidende Fragen isolieren; keine Vollprüfung ohne Anlass.
3. **Belege:** Dokumente, Fotos, Nachrichten, Rechnungen und Protokolle verwerten; Lückenliste erzeugen.
4. **Recht:** Normen aus BGB, WEG, BetrKV, HeizkostenV, GEG/CO2KostAufG nur in aktueller Fassung verwenden.
5. **Anschluss:** Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
6. **Output:** Handlungsfähiges Ergebnis mit nächstem Schritt, Frist und Verantwortlichem.

## Qualitätsmaßstab
- Für Laien klar erklären, welche Gefahr besteht und was heute zu tun ist.
- Für Berufsanfänger sichtbar machen, welche Anspruchsgrundlage, Beweislast und Frist den Fall trägt.
- Für erfahrene Nutzer knapp bleiben und auf den entscheidenden Streitpunkt zielen.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 3. `workflow-weg-protokoll-nachbereiten`

**Frühere Beschreibung:** WEG-Protokoll nachbereiten: Workflow-Skill für Miet- und WEG-Recht; prüft Beschlusswortlaut, Verkündung, Sammlung, Fristen und Fehler; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output.

# WEG-Protokoll nachbereiten

## V90 Fachkern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `WEG-Protokoll nachbereiten` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Dieser Workflow-Skill macht den Einstieg in `fachanwalt-miet-wohnungseigentumsrecht` leichter. Schwerpunkt: prüft Beschlusswortlaut, Verkündung, Sammlung, Fristen und Fehler.

## Kaltstart
Arbeite zuerst mit vorhandenen Unterlagen. Frage nur, was die nächste Entscheidung verändert:
1. Rolle und Ziel der fragenden Person.
2. Objekt und Rechtsverhältnis: Wohnraum, Gewerberaum, WEG, Hausverwaltung oder Mischfall.
3. Frist, Zugang, Termin oder Eilrisiko.
4. Vorhandene Belege und fehlende Schlüsselunterlagen.
5. Gewünschter Output: Erklärung, Tabelle, Brief, Beschluss, Schriftsatz oder Verhandlungsplan.

## Arbeitsworkflow
1. **Kurzlage:** Falltyp, Frist, Risiko, Unterlagen und Ziel in fünf Zeilen.
2. **Weichen:** Zwei bis fünf entscheidende Fragen isolieren; keine Vollprüfung ohne Anlass.
3. **Belege:** Dokumente, Fotos, Nachrichten, Rechnungen und Protokolle verwerten; Lückenliste erzeugen.
4. **Recht:** Normen aus BGB, WEG, BetrKV, HeizkostenV, GEG/CO2KostAufG nur in aktueller Fassung verwenden.
5. **Anschluss:** Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
6. **Output:** Handlungsfähiges Ergebnis mit nächstem Schritt, Frist und Verantwortlichem.

## Qualitätsmaßstab
- Für Laien klar erklären, welche Gefahr besteht und was heute zu tun ist.
- Für Berufsanfänger sichtbar machen, welche Anspruchsgrundlage, Beweislast und Frist den Fall trägt.
- Für erfahrene Nutzer knapp bleiben und auf den entscheidenden Streitpunkt zielen.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 4. `workflow-weg-versammlung-vorbereiten`

**Frühere Beschreibung:** Eigentümerversammlung vorbereiten: Workflow-Skill für Miet- und WEG-Recht; macht Einladung, TOPs, Beschlussvorschläge und Mehrheiten praxistauglich; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output.

# Eigentümerversammlung vorbereiten

## V90 Fachkern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Eigentümerversammlung vorbereiten` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Dieser Workflow-Skill macht den Einstieg in `fachanwalt-miet-wohnungseigentumsrecht` leichter. Schwerpunkt: macht Einladung, TOPs, Beschlussvorschläge und Mehrheiten praxistauglich.

## Kaltstart
Arbeite zuerst mit vorhandenen Unterlagen. Frage nur, was die nächste Entscheidung verändert:
1. Rolle und Ziel der fragenden Person.
2. Objekt und Rechtsverhältnis: Wohnraum, Gewerberaum, WEG, Hausverwaltung oder Mischfall.
3. Frist, Zugang, Termin oder Eilrisiko.
4. Vorhandene Belege und fehlende Schlüsselunterlagen.
5. Gewünschter Output: Erklärung, Tabelle, Brief, Beschluss, Schriftsatz oder Verhandlungsplan.

## Arbeitsworkflow
1. **Kurzlage:** Falltyp, Frist, Risiko, Unterlagen und Ziel in fünf Zeilen.
2. **Weichen:** Zwei bis fünf entscheidende Fragen isolieren; keine Vollprüfung ohne Anlass.
3. **Belege:** Dokumente, Fotos, Nachrichten, Rechnungen und Protokolle verwerten; Lückenliste erzeugen.
4. **Recht:** Normen aus BGB, WEG, BetrKV, HeizkostenV, GEG/CO2KostAufG nur in aktueller Fassung verwenden.
5. **Anschluss:** Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
6. **Output:** Handlungsfähiges Ergebnis mit nächstem Schritt, Frist und Verantwortlichem.

## Qualitätsmaßstab
- Für Laien klar erklären, welche Gefahr besteht und was heute zu tun ist.
- Für Berufsanfänger sichtbar machen, welche Anspruchsgrundlage, Beweislast und Frist den Fall trägt.
- Für erfahrene Nutzer knapp bleiben und auf den entscheidenden Streitpunkt zielen.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 5. `workflow-whatsapp-email-beweis`

**Frühere Beschreibung:** WhatsApp-/E-Mail-Beweis: Workflow-Skill für Miet- und WEG-Recht; wertet informelle Nachrichten für Zugang, Kenntnis, Fristen und Einigungen aus; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output.

# WhatsApp-/E-Mail-Beweis

## V90 Fachkern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `WhatsApp-/E-Mail-Beweis` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Dieser Workflow-Skill macht den Einstieg in `fachanwalt-miet-wohnungseigentumsrecht` leichter. Schwerpunkt: wertet informelle Nachrichten für Zugang, Kenntnis, Fristen und Einigungen aus.

## Kaltstart
Arbeite zuerst mit vorhandenen Unterlagen. Frage nur, was die nächste Entscheidung verändert:
1. Rolle und Ziel der fragenden Person.
2. Objekt und Rechtsverhältnis: Wohnraum, Gewerberaum, WEG, Hausverwaltung oder Mischfall.
3. Frist, Zugang, Termin oder Eilrisiko.
4. Vorhandene Belege und fehlende Schlüsselunterlagen.
5. Gewünschter Output: Erklärung, Tabelle, Brief, Beschluss, Schriftsatz oder Verhandlungsplan.

## Arbeitsworkflow
1. **Kurzlage:** Falltyp, Frist, Risiko, Unterlagen und Ziel in fünf Zeilen.
2. **Weichen:** Zwei bis fünf entscheidende Fragen isolieren; keine Vollprüfung ohne Anlass.
3. **Belege:** Dokumente, Fotos, Nachrichten, Rechnungen und Protokolle verwerten; Lückenliste erzeugen.
4. **Recht:** Normen aus BGB, WEG, BetrKV, HeizkostenV, GEG/CO2KostAufG nur in aktueller Fassung verwenden.
5. **Anschluss:** Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
6. **Output:** Handlungsfähiges Ergebnis mit nächstem Schritt, Frist und Verantwortlichem.

## Qualitätsmaßstab
- Für Laien klar erklären, welche Gefahr besteht und was heute zu tun ist.
- Für Berufsanfänger sichtbar machen, welche Anspruchsgrundlage, Beweislast und Frist den Fall trägt.
- Für erfahrene Nutzer knapp bleiben und auf den entscheidenden Streitpunkt zielen.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 6. `beschlussanfechtung-spezial-fristen`

**Frühere Beschreibung:** Beschlussanfechtung nach § 44 WEG spezial: Klagefrist 1 Monat, Begruendungsfrist 2 Monate ab Beschluss, formale Fehler vs. materielle Mangelhaftigkeit, ausschliesslich Eigentuemerklage nicht Mieter. Pruefraster und Klageaufbau. Routet in fachanwalt-miet-wohnungseigentumsrecht-weg-beschlussanfechtung.

# Beschlussanfechtung: Spezialdetails

## V90 Fachkern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Beschlussanfechtung: Spezialdetails` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Beschlussanfechtung: Spezialdetails
- **Spezialgegenstand:** Beschlussanfechtung: Spezialdetails / beschlussanfechtung spezial fristen. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** WEG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieser Skill gehoert zum Plugin `fachanwalt-miet-wohnungseigentumsrecht`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Skill nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 7. `spezial-abrechnungsfrist-nachforderung`

**Frühere Beschreibung:** Abrechnungsfrist und Nachforderung aus Betriebskosten: § 556 Abs. 3 BGB, Zugang, Jahresfrist, Vermieter-Nichtvertretenmüssen, Guthaben, Korrekturen, WEG-Verzögerung, Gewerberaumabweichungen und Prozessstrategie.

# Abrechnungsfrist/Nachforderung

## V90 Fachkern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Abrechnungsfrist/Nachforderung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Dieser Skill prüft, ob eine Nachforderung aus einer Betriebskostenabrechnung zeitlich noch durchsetzbar ist. Er ist besonders wichtig bei verspäteter WEG-Abrechnung, Postproblemen, Korrekturabrechnungen und Prozessfällen, in denen die Gegenseite nur "zu spät" ruft.

## Prüfschritte

1. Abrechnungszeitraum bestimmen: Beginn, Ende, Nutzerwechsel, Leerstand.
2. Fristende berechnen: spätestens zwölf Monate nach Ende des Abrechnungszeitraums bei Wohnraum.
3. Zugang beweisen: Einwurf, Bote, Zustellnachweis, E-Mail nur bei tragfähiger Vereinbarung/Kommunikationslage.
4. Formelle Mindestangaben innerhalb der Frist prüfen. Eine bloße Zahlenwolke wahrt die Frist nicht.
5. Korrektur unterscheiden:
   - zugunsten des Mieters grundsätzlich möglich,
   - zulasten des Mieters nach Fristablauf nur, wenn der Vermieter die Verspätung nicht zu vertreten hat.
6. WEG-Sonderfall: Verzögerung durch die GdWE/Hausverwaltung kann relevant sein, entlastet den vermietenden Eigentümer aber nicht automatisch. Nachweise zur Anforderung, Erinnerung und Verzögerungsursache sammeln.
7. Gewerberaum: Vertragslage prüfen; § 556 Abs. 3 BGB gilt unmittelbar für Wohnraum, kann aber vertraglich übernommen oder abweichend geregelt sein.

## Entscheidungsbaum

| Frage | Ja | Nein |
| --- | --- | --- |
| Abrechnung fristgerecht zugegangen? | Nachforderung weiter prüfen | Nachforderung regelmäßig ausgeschlossen |
| Abrechnung formell ordnungsgemäß? | materielle Prüfung | keine Fälligkeit der Nachforderung |
| Korrektur nach Frist zulasten Mieter? | nur bei Nichtvertretenmüssen | ausgeschlossen |
| Guthaben des Mieters? | auszahlen/aufrechnen prüfen | Nachforderung/Saldo prüfen |

## Ausgabe

- Fristenrechner mit konkreten Daten.
- Zugangsnachweis-Ampel.
- Schreiben: Einwand "Nachforderung ausgeschlossen" oder Vermieterbegründung "nicht zu vertreten".
- Prozessbaustein zur Darlegungs- und Beweislast.

## Quellen- und Sicherheitsregel

§ 556 Abs. 3 BGB aktuell prüfen. BGH, Urteil vom 12.11.2014 - VIII ZR 112/14 als Zugangswarnung nur mit frei prüfbarer Quelle verwenden. Keine Blindfundstellen.

## 8. `spezial-erhalt-fristennotiz-und-naechster-schritt`

**Frühere Beschreibung:** Erhalt: Fristennotiz und nächster Schritt im Miet- und WEG-Recht: fachlich vertiefter Spezialskill mit Normenradar (BGB/WEG/BetrKV/GEG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

# Erhalt: Fristennotiz und nächster Schritt

## V90 Fachkern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erhalt: Fristennotiz und nächster Schritt` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Erhalt: Fristennotiz und nächster Schritt
- **Spezialgegenstand:** Erhalt: Fristennotiz und nächster Schritt / spezial erhalt fristennotiz und naechster schritt. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** FAO, BGB, WEG, BetrKV.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Erhalt** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 9. `spezial-fristlose-kuendigung-stoerung`

**Frühere Beschreibung:** Fristlose Kündigung wegen Störung: Spezial-Skill im Miet- und Wohnungseigentumsrecht; ordnet Abmahnung, Pflichtverletzung, Wiederholung, Beweise und Interessenabwägung; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt.

# Fristlose Kündigung wegen Störung

## V90 Fachkern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fristlose Kündigung wegen Störung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Spezialskill im Plugin `fachanwalt-miet-wohnungseigentumsrecht`. Er bearbeitet: ordnet Abmahnung, Pflichtverletzung, Wiederholung, Beweise und Interessenabwägung.

## Kaltstart
1. Welche Seite wird vertreten und welches Ergebnis soll erreicht werden?
2. Welche Norm-/Vertrags-/Beschlussgrundlage ist wahrscheinlich einschlägig?
3. Welche Tatsachen sind unstreitig, welche streitig, welche fehlen?
4. Welche Frist, Form, Zuständigkeit oder Beweislast kann den Fall kippen?
5. Welche Unterlagen belegen den Kern: Vertrag, Nachtrag, Beschluss, Protokoll, Abrechnung, Fotos, Messungen, Kontoauszüge, Mails?

## Prüfraster
1. **Rechtsverhältnis abgrenzen:** Wohnraummiete, Gewerberaum, WEG, Verwaltung, Nachbar-/Ordnungsrecht oder Schnittstelle.
2. **Tatbestand:** Anspruchsgrundlage, Einwendung, Gegenrecht und Rechtsfolge sauber trennen.
3. **Form und Frist:** Zugang, Text-/Schriftform, Beschlussfristen, Abrechnungsfristen, Verjährung.
4. **Beweis:** Darlegungslast, Substantiierung, Beweisangebot, Sachverständigenbedarf.
5. **Taktik:** Sofortmaßnahme, Verhandlung, Vergleich, Klage/Eilantrag, Kostenrisiko.
6. **Ergebnis:** Ampel mit Begründung und konkretem nächsten Arbeitsschritt.

## Output
- Prüfvermerk mit Normen und Belegen.
- Lückenliste der fehlenden Tatsachen.
- Entwurf für Mandantenmail, Gegenseitenschreiben, Beschlussvorschlag oder Schriftsatzbaustein.
- Anschluss-Skills, wenn WEG/Miete/Betriebskosten/GEG/Prozessrecht tiefer laufen muss.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 10. `spezial-wohnungseigentumsrecht-fristen-form-und-zustaendigkeit`

**Frühere Beschreibung:** Wohnungseigentumsrecht: Fristen, Form, Zuständigkeit und Rechtsweg im Miet- und WEG-Recht: fachlich vertiefter Spezialskill mit Normenradar (BGB/WEG/BetrKV/GEG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

# Wohnungseigentumsrecht: Fristen, Form, Zuständigkeit und Rechtsweg

## V90 Fachkern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Wohnungseigentumsrecht: Fristen, Form, Zuständigkeit und Rechtsweg` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Wohnungseigentumsrecht: Fristen, Form, Zuständigkeit und Rechtsweg
- **Spezialgegenstand:** Wohnungseigentumsrecht: Fristen, Form, Zuständigkeit und Rechtsweg / spezial wohnungseigentumsrecht fristen form und zustaendigkeit. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** FAO, BGB, WEG, BetrKV.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Wohnungseigentumsrecht** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.
