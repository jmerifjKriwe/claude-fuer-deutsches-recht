---
name: belegchaos-strukturieren-nachtraegliche
description: "Verbraucherinsolvenz Belegchaos Strukturieren, Verbraucherinsolvenz Nachtraegliche Glaeubiger, Verbraucherinsolvenz Pfaendungsschutzkonto: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Verbraucherinsolvenz Belegchaos Strukturieren, Verbraucherinsolvenz Nachtraegliche Glaeubiger, Verbraucherinsolvenz Pfaendungsschutzkonto

## Arbeitsbereich

In diesem Skill wird **Verbraucherinsolvenz Belegchaos Strukturieren, Verbraucherinsolvenz Nachtraegliche Glaeubiger, Verbraucherinsolvenz Pfaendungsschutzkonto** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verbraucherinsolvenz-belegchaos-strukturieren` | Schuldnerberatungsstelle: Strukturierung des Belegchaos. Skill liefert die Methodik wie Schuldnerberater die ungeordneten Belege Mahnungen Vollstreckungsbescheide Inkassobriefe und Bankauszuege des Schuldners in eine geordnete Glaeubiger- und Forderungsliste ueberfuehren. Liefert Checkliste und Vorlagenstruktur. |
| `verbraucherinsolvenz-nachtraegliche-glaeubiger` | Verbraucherinsolvenz: Nachtraegliche Glaeubiger nach Restschuldbefreiung. Skill klaert ob nicht angemeldete Glaeubiger nach Erteilung der Restschuldbefreiung noch Anspruch geltend machen koennen § 301 InsO und Ausnahmen § 302 InsO. Liefert Pruefraster. |
| `verbraucherinsolvenz-pfaendungsschutzkonto` | Verbraucherinsolvenz: Pfaendungsschutzkonto P-Konto. Skill klaert die rechtliche Konstruktion des Pfaendungsschutzkontos nach §§ 850k 850l ZPO Grundfreibetraege Erhoehungsbetraege Antrag und Beweisfuehrung sowie Wechselwirkung mit Insolvenzverfahren. Liefert Pruefraster. |

## Arbeitsweg

Für **Verbraucherinsolvenz Belegchaos Strukturieren, Verbraucherinsolvenz Nachtraegliche Glaeubiger, Verbraucherinsolvenz Pfaendungsschutzkonto** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `verbraucherinsolvenz-schuldenbereinigung` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verbraucherinsolvenz-belegchaos-strukturieren`

**Fokus:** Schuldnerberatungsstelle: Strukturierung des Belegchaos. Skill liefert die Methodik wie Schuldnerberater die ungeordneten Belege Mahnungen Vollstreckungsbescheide Inkassobriefe und Bankauszuege des Schuldners in eine geordnete Glaeubiger- und Forderungsliste ueberfuehren. Liefert Checkliste und Vorlagenstruktur.

# Verbraucherinsolvenz Belegchaos Strukturieren

## Fachkern: Verbraucherinsolvenz Belegchaos Strukturieren
- **Spezialgegenstand:** Verbraucherinsolvenz Belegchaos Strukturieren; dieser Skill beginnt mit der Sachfrage und liefert eine konkrete Lösung statt bloßer Orientierung.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Skill fuer Schuldnerberatungsstellen zur Strukturierung des Belegchaos.

## Ausgangslage

- Schuldner bringt Plastiktueten / Schuhkartons mit ungeordneten Unterlagen.
- Belege oft jahrealt, teils nicht mehr lesbar.
- Glaeubiger zum Teil unbekannt oder Mehrfacheintraege durch Inkasso-Kette.

## Workflow

### Schritt 1: Sortieren in Kategorien
- Forderungen (Mahnungen, Rechnungen, Vollstreckungsbescheide).
- Vertraege (Mietvertrag, Kreditvertrag, Telefonvertrag).
- Behoerden (Finanzamt, Krankenkasse, Sozialamt).
- Konten (Bankauszuege, Sparbuecher).
- Einkommen (Gehaltsabrechnungen, Sozialleistungen).
- Sonstiges (Schriftverkehr, Notizen).

### Schritt 2: Glaeubigerliste anlegen
- Pro Glaeubiger eine Zeile.
- Spalten: Name, Adresse, Hauptforderung, Zinsen, Kosten, Aktenzeichen, Datum letzter Vollstreckungsakt.
- Inkasso-Ketten zusammenfuehren (Originalglaeubiger -> Inkasso 1 -> Inkasso 2).

### Schritt 3: Auskunft einholen
- Schufa-Selbstauskunft (kostenfrei).
- Schuldnerverzeichnis bei Vollstreckungsgerichten.
- Bankkonten-Abfrage.
- Anfrage an bekannte Glaeubiger nach aktuellem Forderungsstand.

### Schritt 4: Forderungen pruefen
- Verjaehrung (§§ 195, 199 BGB; vollstreckbare Titel 30 Jahre § 197 BGB).
- Bestreitbare Forderungen.
- Doppelte Forderungen.

### Schritt 5: Vermoegen erfassen
- Bankkonten, Sparbuecher, Lebensversicherungen, Bausparvertraege.
- Hausrat, Pkw, ggf. Immobilien.
- Pfaendungsfreies Einkommen.

## Werkzeuge

- Excel-Tabelle "Glaeubigerliste".
- Excel-Tabelle "Vermoegensaufstellung".
- Excel-Tabelle "Einkommensberechnung".
- Standardformbriefe an Glaeubiger.
- Verschluesselte Datenablage.

## Aktenfuehrung

- Eigene Mandatsakte mit Originalen / Kopien.
- Versionierung der Vermoegens- und Schuldenliste.
- Datenschutz: DSGVO Art. 30 Verzeichnis von Verarbeitungstaetigkeiten.

## Pruefraster

1. Belege vollstaendig?
2. Glaeubigerliste sauber?
3. Verjaehrungspruefung erfolgt?
4. Vermoegensaufstellung erstellt?
5. Einkommensberechnung erstellt?

## Output

- Strukturierte Mandatsakte.
- Glaeubigerliste.
- Vermoegensaufstellung.
- Einkommensberechnung.
- Schuldenbereinigungsplan-Entwurf.

## 2. `verbraucherinsolvenz-nachtraegliche-glaeubiger`

**Fokus:** Verbraucherinsolvenz: Nachtraegliche Glaeubiger nach Restschuldbefreiung. Skill klaert ob nicht angemeldete Glaeubiger nach Erteilung der Restschuldbefreiung noch Anspruch geltend machen koennen § 301 InsO und Ausnahmen § 302 InsO. Liefert Pruefraster.

# Verbraucherinsolvenz Nachtraegliche Glaeubiger

## Fachkern: Verbraucherinsolvenz Nachtraegliche Glaeubiger
- **Spezialgegenstand:** Verbraucherinsolvenz Nachtraegliche Glaeubiger; dieser Skill beginnt mit der Sachfrage und liefert eine konkrete Lösung statt bloßer Orientierung.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Skill fuer nachtraeglich auftauchende Glaeubiger.

## Norm

- § 301 InsO: Wirkung der Restschuldbefreiung gegenueber allen Glaeubigern.
- § 302 InsO: Ausnahmen.

## Wirkung

- Restschuldbefreiung wirkt auch fuer Glaeubiger, die ihre Forderung nicht angemeldet haben.

## Ausnahmen § 302 InsO

### Nr. 1: Arglistig verschwiegen
- Schuldner hat die Forderung in der Vermoegensaufstellung arglistig nicht angegeben.

### Nr. 2: Vorsaetzliche unerlaubte Handlung
- Forderung aus vorsaetzlicher unerlaubter Handlung (§§ 823 ff. BGB).

### Nr. 3: Unterhaltsforderungen
- Unterhalt fuer Zeitraum vor Insolvenzverfahren.

### Nr. 4: Geldstrafen Geldbussen
- Geldstrafen und Geldbussen.

## Pruefraster

1. Forderung angemeldet?
2. Wenn nicht: Aussnahme nach § 302 InsO?
3. Vorsatz / Arglist?
4. Verjaehrung?

## Output

- Memo Glaeubigeranfrage nach Restschuldbefreiung.
- Schriftsatzbaustein.

## 3. `verbraucherinsolvenz-pfaendungsschutzkonto`

**Fokus:** Verbraucherinsolvenz: Pfaendungsschutzkonto P-Konto. Skill klaert die rechtliche Konstruktion des Pfaendungsschutzkontos nach §§ 850k 850l ZPO Grundfreibetraege Erhoehungsbetraege Antrag und Beweisfuehrung sowie Wechselwirkung mit Insolvenzverfahren. Liefert Pruefraster.

# Verbraucherinsolvenz Pfaendungsschutzkonto

## Fachkern: Verbraucherinsolvenz Pfaendungsschutzkonto
- **Spezialgegenstand:** Verbraucherinsolvenz Pfaendungsschutzkonto; dieser Skill beginnt mit der Sachfrage und liefert eine konkrete Lösung statt bloßer Orientierung.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Skill fuer Pfaendungsschutzkonto.

## Norm

- §§ 850k, 850l ZPO.
- Pfaendungsfreigrenzen-Bekanntmachung jaehrlich neu.

## Grundfreibetrag

- Aktueller Grundfreibetrag 2024: 1.499,99 Euro/Monat (live im Mandat verifizieren).
- Erhoehungsbetraege fuer Unterhaltsverpflichtungen.

## Erhoehungsbetraege

- Pro unterhaltsberechtigte Person ca. 560 Euro/Monat (live verifizieren).
- Sozialleistungsbezug komplett geschuetzt.
- Kindergeld vollstaendig geschuetzt.

## Antrag

- Bei der Bank: Umwandlung in P-Konto.
- Bescheinigung der Beratungsstelle ueber Unterhaltslast.
- Vollstreckungsgericht bei besonderem Bedarf.

## Wechselwirkung Insolvenzverfahren

- P-Konto-Schutz neben Insolvenzverfahren.
- Nicht Schuldnerkonto wechseln, sondern bestehendes Konto umwandeln.

## Pruefraster

1. P-Konto eingerichtet?
2. Grundfreibetrag korrekt?
3. Erhoehungsbetraege beantragt?
4. Bankkommunikation?

## Output

- Antragsvorlage.
- Pruefraster.
