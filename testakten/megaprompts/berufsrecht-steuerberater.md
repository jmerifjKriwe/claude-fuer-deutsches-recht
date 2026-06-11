# Megaprompt: berufsrecht-steuerberater

> *Achtung: Dies ist ein experimentelles Mega-Prompt-Markdown, das einen kompletten Klotzkette-Plugin in eine einzige Datei zusammenfuehrt. Keine Haftung, keine Gewaehr. Nur zum Ausprobieren der Skills auch ohne Claude Code; keine Rechtsberatung. Vor Verwendung im Mandat anwaltlich pruefen.*
>
> *Caution: This is an experimental Mega-Prompt Markdown that consolidates a full Klotzkette plugin into a single file. No warranty, no liability. For exploration with chat tools that do not run Claude Code only; not legal advice.*

**Verwendung:** Diesen gesamten Text in einen Chat ohne Claude-Code-Integration einfuegen (oder als Datei hochladen). Der Chat-Agent erhaelt damit die gebuendelten Skills dieses Plugins als Kontext. Eine Replikation des vollen Plugin-Verhaltens ist nicht garantiert — der Megaprompt ist eine Best-Effort-Kompression.


## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 200 Skills des Plugins `berufsrecht-steuerberater`.

## Inhaltsverzeichnis

1. **berufsausuebungsgesellschaft** — Berufsausübungsgesellschaft: vertiefter Berufsrechts-Skill für Steuerberater; prüft Gesellschaftsform, Fremdbeteiligung,…
2. **berufsgericht-und-disziplinarverfahren** — Berufsgericht und Disziplinarverfahren: vertiefter Berufsrechts-Skill für Steuerberater; prüft Einleitung, Verteidigung,…
3. **frist-und-zustaendigkeit-cockpit** — Fristen- und Zuständigkeitscockpit: vertiefter Berufsrechts-Skill für Steuerberater; prüft macht Fristen, Zuständigkeite…
4. **honorar-gebuehren-verguetung** — Honorar, Gebühren und Vergütung: vertiefter Berufsrechts-Skill für Steuerberater; prüft Vergütungsvereinbarung, Gebühren…
5. **it-cloud-ki-und-outsourcing** — IT, Cloud, KI und Outsourcing: vertiefter Berufsrechts-Skill für Steuerberater; prüft Berufsgeheimnis, Datenschutz, Anbi…
6. **quellen-rechtsprechungscheck** — Quellen- und Rechtsprechungscheck: vertiefter Berufsrechts-Skill für Steuerberater; prüft verhindert Blindzitate und zwi…
7. **sitzungs-und-terminvorbereitung** — Sitzungs- und Terminvorbereitung: vertiefter Berufsrechts-Skill für Steuerberater; prüft bereitet Gerichtstermin, Behörd…
8. **verschwiegenheit-geheimnisschutz-werbung** — Verschwiegenheit und Geheimnisschutz: vertiefter Berufsrechts-Skill für Steuerberater; prüft Berufsgeheimnis, Hilfsperso…
9. **zulassung-bestellung-und-register** — Zulassung, Bestellung und Register: vertiefter Berufsrechts-Skill für Steuerberater; prüft Zulassungsvoraussetzungen, Re…
10. **dokumentenintake-und-aktenlog** — Dokumentenintake und Aktenlog: vertiefter Berufsrechts-Skill für Steuerberater; prüft ordnet Uploads, Eingangspost, Akte…
11. **protokoll-und-nachbereitung** — Protokoll und Nachbereitung: vertiefter Berufsrechts-Skill für Steuerberater; prüft sichert Verlauf, Zusagen, Beschlüsse…
12. **red-team-qualitygate** — Red-Team-Qualitygate: vertiefter Berufsrechts-Skill für Steuerberater; prüft prüft Ergebnis auf Fristenfehler, Zuständig…
13. **werbung-und-aussenauftritt** — Werbung und Außenauftritt: vertiefter Berufsrechts-Skill für Steuerberater; prüft Website, Social Media, Briefkopf, Robe…
14. **entscheidungsvorlage** — Entscheidungsvorlage: vertiefter Berufsrechts-Skill für Steuerberater; prüft macht aus der Prüfung eine Entscheidung mit…
15. **kooperation-anderen-mandanten** — Kooperation mit anderen Berufen: vertiefter Berufsrechts-Skill für Steuerberater; prüft Kooperation mit anderen Berufen …

---

## Skill: `berufsausuebungsgesellschaft`

_Berufsausübungsgesellschaft: vertiefter Berufsrechts-Skill für Steuerberater; prüft Gesellschaftsform, Fremdbeteiligung, Geschäftsführung, Compliance und Register, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung im Berufsrecht Steuerberater._

# Berufsausübungsgesellschaft

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 32 StBerG` — Hilfeleistung in Steuersachen.
- `§ 33 StBerG` — Befugnis der Steuerberater.
- `§ 57 Abs. 1 StBerG` — allgemeine Berufspflichten.
- `§ 57a StBerG` — Werbung.
- `§ 64 StBerG` — Gebühren.
- `§ 67 StBerG` — Handakten.
- `§ 80 AO` — Bevollmaechtigte und Beistand.
- `§ 153 AO` — Berichtigungspflicht.
- `§ 370 AO` — Steuerhinterziehung als Risikogrenze.
- `§ 203 Abs. 1 Nr. 3 StGB` — Verschwiegenheit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; StBerG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Berufsausübungsgesellschaft
- **Normen-/Quellenanker:** StBerG, BOStB, StBVV, AO, GwG, Verschwiegenheit, Interessenkollision, Fristenorganisation und Berufsgerichtsbarkeit.
- **Entscheidende Weiche:** Mandatsannahme, Frist, Erklärung/Berichtigung, Steuerstrafnähe, Gebühren, Kammerkommunikation und Haftungsvermeidung trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** StBerG, BOStB, StBVV, AO, GwG und Kammer-/BStBK-Hinweise live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.

---

## Skill: `berufsgericht-und-disziplinarverfahren`

_Berufsgericht und Disziplinarverfahren: vertiefter Berufsrechts-Skill für Steuerberater; prüft Einleitung, Verteidigung, Maßnahmen, Öffentlichkeit, Beweis und Rechtsmittel, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung im Berufsrecht St..._

# Berufsgericht und Disziplinarverfahren

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 32 StBerG` — Hilfeleistung in Steuersachen.
- `§ 33 StBerG` — Befugnis der Steuerberater.
- `§ 57 Abs. 1 StBerG` — allgemeine Berufspflichten.
- `§ 57a StBerG` — Werbung.
- `§ 64 StBerG` — Gebühren.
- `§ 67 StBerG` — Handakten.
- `§ 80 AO` — Bevollmaechtigte und Beistand.
- `§ 153 AO` — Berichtigungspflicht.
- `§ 370 AO` — Steuerhinterziehung als Risikogrenze.
- `§ 203 Abs. 1 Nr. 3 StGB` — Verschwiegenheit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; StBerG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Berufsgericht und Disziplinarverfahren
- **Normen-/Quellenanker:** StBerG, BOStB, StBVV, AO, GwG, Verschwiegenheit, Interessenkollision, Fristenorganisation und Berufsgerichtsbarkeit.
- **Entscheidende Weiche:** Mandatsannahme, Frist, Erklärung/Berichtigung, Steuerstrafnähe, Gebühren, Kammerkommunikation und Haftungsvermeidung trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** StBerG, BOStB, StBVV, AO, GwG und Kammer-/BStBK-Hinweise live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.

---

## Skill: `frist-und-zustaendigkeit-cockpit`

_Fristen- und Zuständigkeitscockpit: vertiefter Berufsrechts-Skill für Steuerberater; prüft macht Fristen, Zuständigkeiten, Rechtsbehelfe und Vorfristen sofort sichtbar, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung im Berufsrecht Steuer..._

# Fristen- und Zuständigkeitscockpit

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 32 StBerG` — Hilfeleistung in Steuersachen.
- `§ 33 StBerG` — Befugnis der Steuerberater.
- `§ 57 Abs. 1 StBerG` — allgemeine Berufspflichten.
- `§ 57a StBerG` — Werbung.
- `§ 64 StBerG` — Gebühren.
- `§ 67 StBerG` — Handakten.
- `§ 80 AO` — Bevollmaechtigte und Beistand.
- `§ 153 AO` — Berichtigungspflicht.
- `§ 370 AO` — Steuerhinterziehung als Risikogrenze.
- `§ 203 Abs. 1 Nr. 3 StGB` — Verschwiegenheit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; StBerG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Fristen- und Zuständigkeitscockpit
- **Normen-/Quellenanker:** StBerG, BOStB, StBVV, AO, GwG, Verschwiegenheit, Interessenkollision, Fristenorganisation und Berufsgerichtsbarkeit.
- **Entscheidende Weiche:** Mandatsannahme, Frist, Erklärung/Berichtigung, Steuerstrafnähe, Gebühren, Kammerkommunikation und Haftungsvermeidung trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** StBerG, BOStB, StBVV, AO, GwG und Kammer-/BStBK-Hinweise live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.

---

## Skill: `honorar-gebuehren-verguetung`

_Honorar, Gebühren und Vergütung: vertiefter Berufsrechts-Skill für Steuerberater; prüft Vergütungsvereinbarung, Gebührenrecht, Vorschuss, Erfolgshonorargrenzen und Rechnung, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung im Berufsrecht S..._

# Honorar, Gebühren und Vergütung

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 32 StBerG` — Hilfeleistung in Steuersachen.
- `§ 33 StBerG` — Befugnis der Steuerberater.
- `§ 57 Abs. 1 StBerG` — allgemeine Berufspflichten.
- `§ 57a StBerG` — Werbung.
- `§ 64 StBerG` — Gebühren.
- `§ 67 StBerG` — Handakten.
- `§ 80 AO` — Bevollmaechtigte und Beistand.
- `§ 153 AO` — Berichtigungspflicht.
- `§ 370 AO` — Steuerhinterziehung als Risikogrenze.
- `§ 203 Abs. 1 Nr. 3 StGB` — Verschwiegenheit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; StBerG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Honorar, Gebühren und Vergütung
- **Normen-/Quellenanker:** StBerG, BOStB, StBVV, AO, GwG, Verschwiegenheit, Interessenkollision, Fristenorganisation und Berufsgerichtsbarkeit.
- **Entscheidende Weiche:** Mandatsannahme, Frist, Erklärung/Berichtigung, Steuerstrafnähe, Gebühren, Kammerkommunikation und Haftungsvermeidung trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** StBerG, BOStB, StBVV, AO, GwG und Kammer-/BStBK-Hinweise live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.

---

## Skill: `it-cloud-ki-und-outsourcing`

_IT, Cloud, KI und Outsourcing: vertiefter Berufsrechts-Skill für Steuerberater; prüft Berufsgeheimnis, Datenschutz, Anbieterprüfung, Logging und No-Training-Klauseln, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung im Berufsrecht Steuerbe..._

# IT, Cloud, KI und Outsourcing

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 32 StBerG` — Hilfeleistung in Steuersachen.
- `§ 33 StBerG` — Befugnis der Steuerberater.
- `§ 57 Abs. 1 StBerG` — allgemeine Berufspflichten.
- `§ 57a StBerG` — Werbung.
- `§ 64 StBerG` — Gebühren.
- `§ 67 StBerG` — Handakten.
- `§ 80 AO` — Bevollmaechtigte und Beistand.
- `§ 153 AO` — Berichtigungspflicht.
- `§ 370 AO` — Steuerhinterziehung als Risikogrenze.
- `§ 203 Abs. 1 Nr. 3 StGB` — Verschwiegenheit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; StBerG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: IT, Cloud, KI und Outsourcing
- **Normen-/Quellenanker:** StBerG, BOStB, StBVV, AO, GwG, Verschwiegenheit, Interessenkollision, Fristenorganisation und Berufsgerichtsbarkeit.
- **Entscheidende Weiche:** Mandatsannahme, Frist, Erklärung/Berichtigung, Steuerstrafnähe, Gebühren, Kammerkommunikation und Haftungsvermeidung trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** StBerG, BOStB, StBVV, AO, GwG und Kammer-/BStBK-Hinweise live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.

---

## Skill: `quellen-rechtsprechungscheck`

_Quellen- und Rechtsprechungscheck: vertiefter Berufsrechts-Skill für Steuerberater; prüft verhindert Blindzitate und zwingt zu amtlich oder frei prüfbaren Quellen, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung im Berufsrecht Steuerberater._

# Quellen- und Rechtsprechungscheck

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 32 StBerG` — Hilfeleistung in Steuersachen.
- `§ 33 StBerG` — Befugnis der Steuerberater.
- `§ 57 Abs. 1 StBerG` — allgemeine Berufspflichten.
- `§ 57a StBerG` — Werbung.
- `§ 64 StBerG` — Gebühren.
- `§ 67 StBerG` — Handakten.
- `§ 80 AO` — Bevollmaechtigte und Beistand.
- `§ 153 AO` — Berichtigungspflicht.
- `§ 370 AO` — Steuerhinterziehung als Risikogrenze.
- `§ 203 Abs. 1 Nr. 3 StGB` — Verschwiegenheit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; StBerG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Quellen- und Rechtsprechungscheck
- **Normen-/Quellenanker:** StBerG, BOStB, StBVV, AO, GwG, Verschwiegenheit, Interessenkollision, Fristenorganisation und Berufsgerichtsbarkeit.
- **Entscheidende Weiche:** Mandatsannahme, Frist, Erklärung/Berichtigung, Steuerstrafnähe, Gebühren, Kammerkommunikation und Haftungsvermeidung trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** StBerG, BOStB, StBVV, AO, GwG und Kammer-/BStBK-Hinweise live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.

---

## Skill: `sitzungs-und-terminvorbereitung`

_Sitzungs- und Terminvorbereitung: vertiefter Berufsrechts-Skill für Steuerberater; prüft bereitet Gerichtstermin, Behördenkontakt, Kammertermin oder Verhandlungstag vor, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung im Berufsrecht Steue..._

# Sitzungs- und Terminvorbereitung

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 32 StBerG` — Hilfeleistung in Steuersachen.
- `§ 33 StBerG` — Befugnis der Steuerberater.
- `§ 57 Abs. 1 StBerG` — allgemeine Berufspflichten.
- `§ 57a StBerG` — Werbung.
- `§ 64 StBerG` — Gebühren.
- `§ 67 StBerG` — Handakten.
- `§ 80 AO` — Bevollmaechtigte und Beistand.
- `§ 153 AO` — Berichtigungspflicht.
- `§ 370 AO` — Steuerhinterziehung als Risikogrenze.
- `§ 203 Abs. 1 Nr. 3 StGB` — Verschwiegenheit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; StBerG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Sitzungs- und Terminvorbereitung
- **Normen-/Quellenanker:** StBerG, BOStB, StBVV, AO, GwG, Verschwiegenheit, Interessenkollision, Fristenorganisation und Berufsgerichtsbarkeit.
- **Entscheidende Weiche:** Mandatsannahme, Frist, Erklärung/Berichtigung, Steuerstrafnähe, Gebühren, Kammerkommunikation und Haftungsvermeidung trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** StBerG, BOStB, StBVV, AO, GwG und Kammer-/BStBK-Hinweise live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.

---

## Skill: `verschwiegenheit-geheimnisschutz-werbung`

_Verschwiegenheit und Geheimnisschutz: vertiefter Berufsrechts-Skill für Steuerberater; prüft Berufsgeheimnis, Hilfspersonen, IT-Dienstleister, Auslagerung und Aktenzugriff, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung im Berufsrecht St..._

# Verschwiegenheit und Geheimnisschutz

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 32 StBerG` — Hilfeleistung in Steuersachen.
- `§ 33 StBerG` — Befugnis der Steuerberater.
- `§ 57 Abs. 1 StBerG` — allgemeine Berufspflichten.
- `§ 57a StBerG` — Werbung.
- `§ 64 StBerG` — Gebühren.
- `§ 67 StBerG` — Handakten.
- `§ 80 AO` — Bevollmaechtigte und Beistand.
- `§ 153 AO` — Berichtigungspflicht.
- `§ 370 AO` — Steuerhinterziehung als Risikogrenze.
- `§ 203 Abs. 1 Nr. 3 StGB` — Verschwiegenheit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; StBerG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Verschwiegenheit und Geheimnisschutz
- **Normen-/Quellenanker:** StBerG, BOStB, StBVV, AO, GwG, Verschwiegenheit, Interessenkollision, Fristenorganisation und Berufsgerichtsbarkeit.
- **Entscheidende Weiche:** Mandatsannahme, Frist, Erklärung/Berichtigung, Steuerstrafnähe, Gebühren, Kammerkommunikation und Haftungsvermeidung trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** StBerG, BOStB, StBVV, AO, GwG und Kammer-/BStBK-Hinweise live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.

---

## Skill: `zulassung-bestellung-und-register`

_Zulassung, Bestellung und Register: vertiefter Berufsrechts-Skill für Steuerberater; prüft Zulassungsvoraussetzungen, Register, Kammerdaten, Meldepflichten und Widerrufsrisiken, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung im Berufsrec..._

# Zulassung, Bestellung und Register

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 32 StBerG` — Hilfeleistung in Steuersachen.
- `§ 33 StBerG` — Befugnis der Steuerberater.
- `§ 57 Abs. 1 StBerG` — allgemeine Berufspflichten.
- `§ 57a StBerG` — Werbung.
- `§ 64 StBerG` — Gebühren.
- `§ 67 StBerG` — Handakten.
- `§ 80 AO` — Bevollmaechtigte und Beistand.
- `§ 153 AO` — Berichtigungspflicht.
- `§ 370 AO` — Steuerhinterziehung als Risikogrenze.
- `§ 203 Abs. 1 Nr. 3 StGB` — Verschwiegenheit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; StBerG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Zulassung, Bestellung und Register
- **Normen-/Quellenanker:** StBerG, BOStB, StBVV, AO, GwG, Verschwiegenheit, Interessenkollision, Fristenorganisation und Berufsgerichtsbarkeit.
- **Entscheidende Weiche:** Mandatsannahme, Frist, Erklärung/Berichtigung, Steuerstrafnähe, Gebühren, Kammerkommunikation und Haftungsvermeidung trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** StBerG, BOStB, StBVV, AO, GwG und Kammer-/BStBK-Hinweise live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.

---

## Skill: `dokumentenintake-und-aktenlog`

_Dokumentenintake und Aktenlog: vertiefter Berufsrechts-Skill für Steuerberater; prüft ordnet Uploads, Eingangspost, Aktenbestandteile und fehlende Unterlagen, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung im Berufsrecht Steuerberater._

# Dokumentenintake und Aktenlog

## Aktenstart statt Formularstart

Wenn zu **Dokumentenintake Und Aktenlog** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Berufsrecht Steuerberater** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 32 StBerG` — Hilfeleistung in Steuersachen.
- `§ 33 StBerG` — Befugnis der Steuerberater.
- `§ 57 Abs. 1 StBerG` — allgemeine Berufspflichten.
- `§ 57a StBerG` — Werbung.
- `§ 64 StBerG` — Gebühren.
- `§ 67 StBerG` — Handakten.
- `§ 80 AO` — Bevollmaechtigte und Beistand.
- `§ 153 AO` — Berichtigungspflicht.
- `§ 370 AO` — Steuerhinterziehung als Risikogrenze.
- `§ 203 Abs. 1 Nr. 3 StGB` — Verschwiegenheit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; StBerG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Dokumentenintake und Aktenlog
- **Normen-/Quellenanker:** StBerG, BOStB, StBVV, AO, GwG, Verschwiegenheit, Interessenkollision, Fristenorganisation und Berufsgerichtsbarkeit.
- **Entscheidende Weiche:** Mandatsannahme, Frist, Erklärung/Berichtigung, Steuerstrafnähe, Gebühren, Kammerkommunikation und Haftungsvermeidung trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** StBerG, BOStB, StBVV, AO, GwG und Kammer-/BStBK-Hinweise live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.

---

## Skill: `protokoll-und-nachbereitung`

_Protokoll und Nachbereitung: vertiefter Berufsrechts-Skill für Steuerberater; prüft sichert Verlauf, Zusagen, Beschlüsse, Auflagen und nächste Wiedervorlagen, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung im Berufsrecht Steuerberater._

# Protokoll und Nachbereitung

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 32 StBerG` — Hilfeleistung in Steuersachen.
- `§ 33 StBerG` — Befugnis der Steuerberater.
- `§ 57 Abs. 1 StBerG` — allgemeine Berufspflichten.
- `§ 57a StBerG` — Werbung.
- `§ 64 StBerG` — Gebühren.
- `§ 67 StBerG` — Handakten.
- `§ 80 AO` — Bevollmaechtigte und Beistand.
- `§ 153 AO` — Berichtigungspflicht.
- `§ 370 AO` — Steuerhinterziehung als Risikogrenze.
- `§ 203 Abs. 1 Nr. 3 StGB` — Verschwiegenheit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; StBerG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Protokoll und Nachbereitung
- **Normen-/Quellenanker:** StBerG, BOStB, StBVV, AO, GwG, Verschwiegenheit, Interessenkollision, Fristenorganisation und Berufsgerichtsbarkeit.
- **Entscheidende Weiche:** Mandatsannahme, Frist, Erklärung/Berichtigung, Steuerstrafnähe, Gebühren, Kammerkommunikation und Haftungsvermeidung trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** StBerG, BOStB, StBVV, AO, GwG und Kammer-/BStBK-Hinweise live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.

---

## Skill: `red-team-qualitygate`

_Red-Team-Qualitygate: vertiefter Berufsrechts-Skill für Steuerberater; prüft prüft Ergebnis auf Fristenfehler, Zuständigkeitsfehler, Scheinpräzision und Ton, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung im Berufsrecht Steuerberater._

# Red-Team-Qualitygate

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 32 StBerG` — Hilfeleistung in Steuersachen.
- `§ 33 StBerG` — Befugnis der Steuerberater.
- `§ 57 Abs. 1 StBerG` — allgemeine Berufspflichten.
- `§ 57a StBerG` — Werbung.
- `§ 64 StBerG` — Gebühren.
- `§ 67 StBerG` — Handakten.
- `§ 80 AO` — Bevollmaechtigte und Beistand.
- `§ 153 AO` — Berichtigungspflicht.
- `§ 370 AO` — Steuerhinterziehung als Risikogrenze.
- `§ 203 Abs. 1 Nr. 3 StGB` — Verschwiegenheit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; StBerG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Red-Team-Qualitygate
- **Normen-/Quellenanker:** StBerG, BOStB, StBVV, AO, GwG, Verschwiegenheit, Interessenkollision, Fristenorganisation und Berufsgerichtsbarkeit.
- **Entscheidende Weiche:** Mandatsannahme, Frist, Erklärung/Berichtigung, Steuerstrafnähe, Gebühren, Kammerkommunikation und Haftungsvermeidung trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** StBerG, BOStB, StBVV, AO, GwG und Kammer-/BStBK-Hinweise live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.

---

## Skill: `werbung-und-aussenauftritt`

_Werbung und Außenauftritt: vertiefter Berufsrechts-Skill für Steuerberater; prüft Website, Social Media, Briefkopf, Robe, Titel, Rankings und Sachlichkeit, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung im Berufsrecht Steuerberater._

# Werbung und Außenauftritt

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 32 StBerG` — Hilfeleistung in Steuersachen.
- `§ 33 StBerG` — Befugnis der Steuerberater.
- `§ 57 Abs. 1 StBerG` — allgemeine Berufspflichten.
- `§ 57a StBerG` — Werbung.
- `§ 64 StBerG` — Gebühren.
- `§ 67 StBerG` — Handakten.
- `§ 80 AO` — Bevollmaechtigte und Beistand.
- `§ 153 AO` — Berichtigungspflicht.
- `§ 370 AO` — Steuerhinterziehung als Risikogrenze.
- `§ 203 Abs. 1 Nr. 3 StGB` — Verschwiegenheit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; StBerG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Werbung und Außenauftritt
- **Normen-/Quellenanker:** StBerG, BOStB, StBVV, AO, GwG, Verschwiegenheit, Interessenkollision, Fristenorganisation und Berufsgerichtsbarkeit.
- **Entscheidende Weiche:** Mandatsannahme, Frist, Erklärung/Berichtigung, Steuerstrafnähe, Gebühren, Kammerkommunikation und Haftungsvermeidung trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** StBerG, BOStB, StBVV, AO, GwG und Kammer-/BStBK-Hinweise live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.

---

## Skill: `entscheidungsvorlage`

_Entscheidungsvorlage: vertiefter Berufsrechts-Skill für Steuerberater; prüft macht aus der Prüfung eine Entscheidung mit Optionen, Risiken und Empfehlung, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung im Berufsrecht Steuerberater._

# Entscheidungsvorlage

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 32 StBerG` — Hilfeleistung in Steuersachen.
- `§ 33 StBerG` — Befugnis der Steuerberater.
- `§ 57 Abs. 1 StBerG` — allgemeine Berufspflichten.
- `§ 57a StBerG` — Werbung.
- `§ 64 StBerG` — Gebühren.
- `§ 67 StBerG` — Handakten.
- `§ 80 AO` — Bevollmaechtigte und Beistand.
- `§ 153 AO` — Berichtigungspflicht.
- `§ 370 AO` — Steuerhinterziehung als Risikogrenze.
- `§ 203 Abs. 1 Nr. 3 StGB` — Verschwiegenheit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; StBerG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Entscheidungsvorlage
- **Normen-/Quellenanker:** StBerG, BOStB, StBVV, AO, GwG, Verschwiegenheit, Interessenkollision, Fristenorganisation und Berufsgerichtsbarkeit.
- **Entscheidende Weiche:** Mandatsannahme, Frist, Erklärung/Berichtigung, Steuerstrafnähe, Gebühren, Kammerkommunikation und Haftungsvermeidung trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** StBerG, BOStB, StBVV, AO, GwG und Kammer-/BStBK-Hinweise live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.

---

## Skill: `kooperation-anderen-mandanten`

_Kooperation mit anderen Berufen: vertiefter Berufsrechts-Skill für Steuerberater; prüft Kooperation mit anderen Berufen im Berufsrecht für Steuerberater, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nächste Handlung im Berufsrecht Steuerberater._

# Kooperation mit anderen Berufen

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 32 StBerG` — Hilfeleistung in Steuersachen.
- `§ 33 StBerG` — Befugnis der Steuerberater.
- `§ 57 Abs. 1 StBerG` — allgemeine Berufspflichten.
- `§ 57a StBerG` — Werbung.
- `§ 64 StBerG` — Gebühren.
- `§ 67 StBerG` — Handakten.
- `§ 80 AO` — Bevollmaechtigte und Beistand.
- `§ 153 AO` — Berichtigungspflicht.
- `§ 370 AO` — Steuerhinterziehung als Risikogrenze.
- `§ 203 Abs. 1 Nr. 3 StGB` — Verschwiegenheit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; StBerG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Kooperation mit anderen Berufen
- **Normen-/Quellenanker:** StBerG, BOStB, StBVV, AO, GwG, Verschwiegenheit, Interessenkollision, Fristenorganisation und Berufsgerichtsbarkeit.
- **Entscheidende Weiche:** Mandatsannahme, Frist, Erklärung/Berichtigung, Steuerstrafnähe, Gebühren, Kammerkommunikation und Haftungsvermeidung trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** StBerG, BOStB, StBVV, AO, GwG und Kammer-/BStBK-Hinweise live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

