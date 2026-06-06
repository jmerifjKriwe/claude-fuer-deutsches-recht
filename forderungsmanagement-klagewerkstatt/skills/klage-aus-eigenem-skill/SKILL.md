---
name: klage-aus-eigenem-skill
description: "Erstellt eine konkrete Klage aus dem hauseigenen kanzlei-spezifischen Vorlagen-Plugin gegen einen benannten Beklagten. Nimmt Mandantendaten Forderungsgrund Streitwert Belege auf und fuellt die Kanzleivorlage. Pinpoints ZPO 253 Abs. 2 ZPO 130d beA. Liefert DOCX Klage druckfertig."
---

# Klage aus eigenem Skill

Variante von klagevorlage-aus-eigenen-mustern. Hier ist die Vorlage bereits in einem hauseigenen Plugin oder Skill abgelegt und es geht um die konkrete Klagefertigung.

## Daten-Erhebung

| Block | Erhebt |
|---|---|
| Klaeger | Name Anschrift Vertreter |
| Beklagter | Name Anschrift Rechtsform |
| Forderung | Hauptsumme Faelligkeit Verzugsbeginn |
| Anspruchsgrund | Vertrag Lieferung Werk Honorar |
| Belege | Liste mit Anlagen-Nummerierung |
| Streitwert | Hauptsumme Nebenforderungen |
| Gericht | sachlich und oertlich zustaendig pruefen |
| Mandantenfreigabe | Datum Unterschrift |

## Anschluss-Skills

- zustaendigkeitspruefung-mahngericht fuer oertliche Zustaendigkeit
- klage-einreichungslogik fuer Einreichung
- klagefreigabe-belegte-forderung fuer Mandantenvermerk

## Norm-Pinpoints

- ZPO 130d
- ZPO 253 Abs. 2

## Quellen

- [ZPO 253](https://www.gesetze-im-internet.de/zpo/__253.html)
