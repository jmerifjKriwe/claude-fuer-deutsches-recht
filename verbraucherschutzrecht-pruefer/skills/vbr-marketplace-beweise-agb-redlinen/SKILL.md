---
name: vbr-marketplace-beweise-agb-redlinen
description: "Vbr 054 Marketplace Beweise Sichern, Vbr 055 Marketplace Agb Redlinen, Vbr 056 Marketplace Beschwerde Schreiben, Vbr 057 Marketplace Schlichtung Waehlen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Vbr 054 Marketplace Beweise Sichern, Vbr 055 Marketplace Agb Redlinen, Vbr 056 Marketplace Beschwerde Schreiben, Vbr 057 Marketplace Schlichtung Waehlen

## Arbeitsbereich

In diesem Skill wird **Vbr 054 Marketplace Beweise Sichern, Vbr 055 Marketplace Agb Redlinen, Vbr 056 Marketplace Beschwerde Schreiben, Vbr 057 Marketplace Schlichtung Waehlen** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vbr-054-marketplace-beweise-sichern` | Verbraucherschutzrecht Prüfer: Marketplace: Beweise sichern. Beweise sichern für Marketplace im Rahmen von Verbraucherschutzrecht Prüfer; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `vbr-055-marketplace-agb-redlinen` | Verbraucherschutzrecht Prüfer: Marketplace: AGB redlinen. AGB redlinen für Marketplace im Rahmen von Verbraucherschutzrecht Prüfer; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `vbr-056-marketplace-beschwerde-schreiben` | Verbraucherschutzrecht Prüfer: Marketplace: Beschwerde schreiben. Beschwerde schreiben für Marketplace im Rahmen von Verbraucherschutzrecht Prüfer; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `vbr-057-marketplace-schlichtung-waehlen` | Verbraucherschutzrecht Prüfer: Marketplace: Schlichtung wählen. Schlichtung wählen für Marketplace im Rahmen von Verbraucherschutzrecht Prüfer; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |

## Arbeitsweg

Für **Vbr 054 Marketplace Beweise Sichern, Vbr 055 Marketplace Agb Redlinen, Vbr 056 Marketplace Beschwerde Schreiben, Vbr 057 Marketplace Schlichtung Waehlen** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `verbraucherschutzrecht-pruefer` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vbr-054-marketplace-beweise-sichern`

**Fokus:** Verbraucherschutzrecht Prüfer: Marketplace: Beweise sichern. Beweise sichern für Marketplace im Rahmen von Verbraucherschutzrecht Prüfer; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Marketplace Beweise Sichern

## Arbeitsauftrag

Marketplace Beweise Sichern wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Verbraucherschutzrecht allgemein: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- BGB-Verbrauchervertragsrecht, Widerruf, digitale Produkte
- UWG, UKlaG, VSBG, PAngV, Fernabsatz, E-Commerce
- Produktsicherheit, Right to Repair, Gewährleistung
- EU-Verbraucherrecht live gegen EUR-Lex/Bundesrecht prüfen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Verbraucherrechte-Ampel
- Anspruchs- und Fristenmatrix
- Anschreiben an Unternehmer/Plattform
- Beweis- und Screenshotplan

## Red-Team-Fragen

- B2C/B2B-Rolle unklar
- Widerrufsfrist/Beweislast falsch gerechnet
- Plattform- und Händlerrolle vermischt
- AGB-Kontrolle ohne Einbeziehungskontrolle

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 2. `vbr-055-marketplace-agb-redlinen`

**Fokus:** Verbraucherschutzrecht Prüfer: Marketplace: AGB redlinen. AGB redlinen für Marketplace im Rahmen von Verbraucherschutzrecht Prüfer; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Marketplace Agb Redlinen

## Arbeitsauftrag

Marketplace Agb Redlinen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Verbraucherschutzrecht allgemein: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- BGB-Verbrauchervertragsrecht, Widerruf, digitale Produkte
- UWG, UKlaG, VSBG, PAngV, Fernabsatz, E-Commerce
- Produktsicherheit, Right to Repair, Gewährleistung
- EU-Verbraucherrecht live gegen EUR-Lex/Bundesrecht prüfen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Verbraucherrechte-Ampel
- Anspruchs- und Fristenmatrix
- Anschreiben an Unternehmer/Plattform
- Beweis- und Screenshotplan

## Red-Team-Fragen

- B2C/B2B-Rolle unklar
- Widerrufsfrist/Beweislast falsch gerechnet
- Plattform- und Händlerrolle vermischt
- AGB-Kontrolle ohne Einbeziehungskontrolle

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 3. `vbr-056-marketplace-beschwerde-schreiben`

**Fokus:** Verbraucherschutzrecht Prüfer: Marketplace: Beschwerde schreiben. Beschwerde schreiben für Marketplace im Rahmen von Verbraucherschutzrecht Prüfer; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Marketplace Beschwerde Schreiben

## Arbeitsauftrag

Marketplace Beschwerde Schreiben wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Verbraucherschutzrecht allgemein: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- BGB-Verbrauchervertragsrecht, Widerruf, digitale Produkte
- UWG, UKlaG, VSBG, PAngV, Fernabsatz, E-Commerce
- Produktsicherheit, Right to Repair, Gewährleistung
- EU-Verbraucherrecht live gegen EUR-Lex/Bundesrecht prüfen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Verbraucherrechte-Ampel
- Anspruchs- und Fristenmatrix
- Anschreiben an Unternehmer/Plattform
- Beweis- und Screenshotplan

## Red-Team-Fragen

- B2C/B2B-Rolle unklar
- Widerrufsfrist/Beweislast falsch gerechnet
- Plattform- und Händlerrolle vermischt
- AGB-Kontrolle ohne Einbeziehungskontrolle

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.

## 4. `vbr-057-marketplace-schlichtung-waehlen`

**Fokus:** Verbraucherschutzrecht Prüfer: Marketplace: Schlichtung wählen. Schlichtung wählen für Marketplace im Rahmen von Verbraucherschutzrecht Prüfer; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen.

# Marketplace Schlichtung Waehlen

## Arbeitsauftrag

Marketplace Schlichtung Waehlen wird nicht als abstraktes Schema beantwortet, sondern als Arbeitsgang im Bereich Verbraucherschutzrecht allgemein: erst Zuständigkeit und Normpfad, dann Tatsachen und Belege, dann Fristen und taktische Option, danach ein verwertbarer Output.

## Einstieg ohne Leerlauf

1. Rolle klären: antragstellende Person, Behörde, Verband, Unternehmen, Anwalt, Gericht, Presse, Betroffene oder Projektträger.
2. Ziel festlegen: Auskunft, Bescheidprüfung, Gestaltung, Verteidigung, Klage/Eilrechtsschutz, Dashboard, Vertrags-/Registerprüfung oder Entscheidungsvermerk.
3. Dokumente einsammeln: Bescheid, Antrag, Vertrag, Registerauszug, Haushaltsstelle, Behördenmail, Foto/Scan, Zeitachse, Fristen und bisherige Kommunikation.
4. Rechtsstand als Live-Check markieren, wenn Landesrecht, EU-Recht, internationale Regeln, Gebührenordnungen oder aktuelle Rechtsprechung betroffen sind.

## Norm- und Quellenanker

- BGB-Verbrauchervertragsrecht, Widerruf, digitale Produkte
- UWG, UKlaG, VSBG, PAngV, Fernabsatz, E-Commerce
- Produktsicherheit, Right to Repair, Gewährleistung
- EU-Verbraucherrecht live gegen EUR-Lex/Bundesrecht prüfen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Typische Artefakte

- Verbraucherrechte-Ampel
- Anspruchs- und Fristenmatrix
- Anschreiben an Unternehmer/Plattform
- Beweis- und Screenshotplan

## Red-Team-Fragen

- B2C/B2B-Rolle unklar
- Widerrufsfrist/Beweislast falsch gerechnet
- Plattform- und Händlerrolle vermischt
- AGB-Kontrolle ohne Einbeziehungskontrolle

## Ausgabeformat

- **Kurzbefund:** ein Absatz, der die Lage und den nächsten Schritt verständlich macht.
- **Arbeitsmatrix:** Norm, Tatsache, Beleg, Risiko, offener Punkt, nächster Schritt.
- **Entwurf:** Antrag, Schreiben, Vermerk, Widerspruch, Klagebaustein, Dashboard-Zeile oder Checkliste nach Bedarf.
- **Quellenblock:** nur amtliche/frei prüfbare Quellen oder vom Nutzer bereitgestellte Quellen; keine Blindzitate, keine BeckRS-/juris-Behauptungen ohne Nutzerquelle.

## Qualitätsregel

Wenn etwas nur wahrscheinlich ist, als wahrscheinlich kennzeichnen. Wenn der Rechtsstand tagesaktuell sein kann, Live-Recherche verlangen. Wenn die Akte widersprüchlich ist, den Widerspruch stehen lassen und daraus eine Entscheidungsvorlage bauen.
