---
name: klagevorlage-aus-eigenen-mustern
description: "Erstellt aus einem oder mehreren von der Kanzlei hochgeladenen Klagemuster eine wiederverwendbare interne Klage-Vorlage. Extrahiert Variable Platzhalter Mandanten Datum Betrag und kanzlei-typische Formulierungen. Pinpoints ZPO 253 Abs. 2 ZPO 130 Form. Liefert DOCX-Vorlage mit ausgewiesenen Platzhaltern."
---

# Klagevorlage aus eigenen Mustern

Wenn die Kanzlei bewaehrte Klagemuster hat sollen diese nicht durch generische Vorlagen ersetzt werden. Dieser Skill destilliert das Eigene heraus.

## Analyseraster

| Block | Was extrahiert wird | Variablen |
|---|---|---|
| Rubrum | Format Klaeger Beklagter Prozessbevollmaechtigte | [klaeger_name] [klaeger_anschrift] [beklagte_name] [beklagte_anschrift] |
| Anrede Eingangs-Satz | kanzleitypisch | [ggf. Gericht] |
| Antragsformulierung | Wortlaut Standard- und Nebenforderungen | [hauptsumme] [zinsbeginn] [vorgerichtliche_kosten] |
| Streitwertangabe | Position im Schriftsatz | [streitwert] |
| Sachverhalt | typische Gliederung I II III | [vertragsdaten] [pflichtverletzung] [beleg_anlagen] |
| Rechtliche Wuerdigung | Strukturen mit Pinpoints | [anspruchsnorm] [verzugsnorm] |
| Beweis | Form der Beweisangebote | [zeugen] [urkunden] [sv_gutachten] |
| Schluss | Antrag auf Versaeumnisurteil etc | optional |

## Pruefung der Muster

- Sind die Muster aktuell beA-fest ZPO 130d
- Verzugszinsen korrekt B2B neun Prozentpunkte B2C fuenf Prozentpunkte BGB 288
- Pauschale vierzig Euro fuer B2B erwaehnt BGB 288 Abs. 5
- Streitwertangabe enthalten
- Rechtsmittelhinweis weggelassen das ist Sache des Gerichts

## Ausgabeformat

- DOCX mit Platzhaltern in eckigen Klammern
- Begleit-Markdown mit Liste aller Variablen
- Mini-Plugin als ZIP optional fuer wiederholten Einsatz

## Quellen

- [ZPO 253](https://www.gesetze-im-internet.de/zpo/__253.html)
- [ZPO 130d](https://www.gesetze-im-internet.de/zpo/__130d.html)
- [BGB 288](https://www.gesetze-im-internet.de/bgb/__288.html)
