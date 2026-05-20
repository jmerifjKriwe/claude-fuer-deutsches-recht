# Zitierweise deutsches Recht (v3.0)

Deutsche juristische Hauszitierweise als zuschaltbares Plugin. Pragmatische Repository-Konvention für Schriftsätze, Memos und Mandantenkommunikation — bewusst getrennt von wissenschaftlicher Notation. Rspr. mit `Az.`-Marker, Datum, Aktenzeichen, Fundstelle, Randnummer. Bearbeiter-Kommentar mit `in:`, Einzelautorenkommentar ohne `in:`. Monographien mit Verlag. `Diss.` und `Habil.` mit Hochschulort. Materialien mit Pinpoint und Link. Reihenfolge erst Gerichtshierarchie, dann chronologisch oder relevanzsortiert.

## Was ist neu in v3.0

Diese Auflage konsolidiert elf Korrekturpunkte gegenüber v2.x:

1. **`Az.`-Marker** ist Pflichtbestandteil vor jedem Aktenzeichen.
2. **Kommentar-Schemata** sauber getrennt — Bearbeiter-Kommentar (`Bearbeiter, in: Werk, …`) und Einzelautorenkommentar (`Verfasser, Werk, …` ohne `in:`).
3. **Großkommentare vs. Kurz-/Handkommentare** als zwei getrennte Tabellen. Grüneberg ist ein Kurz-/Handkommentar, kein Großkommentar.
4. **`Diss.` und `Habil.`** sind Pflichtmarker bei Dissertationen und Habilitationen, jeweils mit dem Ort der Hochschule.
5. **Materialien** mit explizitem Schema: Herausgeber, Titel, Datum oder Stand, Fundstelle, Pinpoint, ggf. URL.
6. **Reihenfolge mehrerer Rspr.-Belege** — erst Gerichtshierarchie (BVerfG → EuGH/EGMR → BGH/BAG/BSG/BFH/BVerwG → OLG/LAG/LSG/FG/OVG → LG/ArbG/SG/VG → AG), dann innerhalb derselben Ebene chronologisch absteigend.
7. **Relevanzsortierung** als ausdrückliche Alternative zur Chronologie — dokumentintern konsistent.
8. **Aufsätze** haben dauerhaften Wert. Sie tragen Dogmatik, Theorie, Rechtsphilosophie, soziale Gerechtigkeit und Gleichbehandlung — nicht „nur" aktuelle oder rechtsökonomische Fragen.
9. **„h. M." und „Mindermeinung"** sind pragmatische Sprechweisen, keine wissenschaftlichen Wertungskategorien. Keine Stigmatisierung abweichender Auffassungen.
10. **Typografie** unterscheidet pragmatische Repository-Konvention von wissenschaftlicher Notation. Beides ist legitim, dokumentintern konsistent.
11. **Verlag** bei Monographien und Festschriften.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Zitierweise deutsches Recht (`zitierweise-deutsches-recht`, dieses Plugin) | [zitierweise-deutsches-recht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/zitierweise-deutsches-recht.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus „Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `zitierweise-anwenden` | Wendet die Hauszitierweise v3.0 auf jede juristische Quelle an — Rspr. mit `Az.`-Marker, Bearbeiter-/Einzelautorenkommentar, Verlag, `Diss.`/`Habil.`-Pflicht, Materialien-Pinpoint, Reihenfolge nach Hierarchie + Chronologie/Relevanz, Palandt-Pflichtnachfrage. |

## Pragmatik vs. Wissenschaft

Diese Hauszitierweise ist eine pragmatische Repository-Konvention. Wissenschaftliche Alternativen (vollständige Erstzitierung, Titel im Beleg, ausgeschriebene Vornamen, ausführliche Verlags- und Ortsangaben) sind legitim — innerhalb desselben Dokuments konsistent durchhalten.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.
