---
name: quellenhygiene-rechtsprechungsanker-und-bughunt
description: "Quellen- und Bug-Hunt-Skill für Bauträgervertragsprüfungen: verifiziert Normenstand, BGH-/OLG-Rechtsprechung, MaBV-Zitate, AGB-Folgen, § 650u/§ 650v BGB, § 650m Abs. 2 BGB, Abnahme- und Schlussratenanker und verhindert BeckRS-/juris-Blindzitate."
---

# Quellenhygiene, Rechtsprechungsanker und Bug-Hunt

## Zweck

Dieser Skill wird vor jeder Ausgabe geladen, die Rechtsprechung, Normen oder eine harte Verhandlungsposition enthält. Er verhindert Blindzitate und typische Bauträgerrechtsfehler.

## Zulässige Quellen

Nutze für Rechtsprechung offizielle Gerichtsseiten, `rechtsprechung-im-internet.de`, `rechtsinformationen.bund.de`, Landesrechtsprechungsportale, `dejure.org` oder `openjur.de`. Nutze für Normen `gesetze-im-internet.de`, Bundesgesetzblatt und Landesrechtportale. Zitiere keine BeckRS-, juris-, Kommentar- oder Zeitschriftenfundstellen als Beleg.

## Normenanker für den Kontrolllauf

§§ 305-310, 306, 307, 308 Nr. 4, 309 Nr. 12, 309 Nr. 15, 311b, 315, 320, 633-641, 650j, 650k Abs. 2/3, 650m Abs. 2, 650n, 650u, 650v, 883, 925 BGB; §§ 3, 7, 12 MaBV; § 17 Abs. 2a BeurkG; § 57 BeurkG; WEG; ZPO nur bei Klageausgabe.

## Bug-Hunt

Vor Ausgabe kontrollieren:

- Wurde § 650m Abs. 1 BGB versehentlich als Bauträger-Hauptregel benutzt? Bei Bauträgern ist Abs. 1 durch § 650u Abs. 2 BGB ausgeschlossen; Abs. 2 bleibt relevant.
- Wurde § 650k Abs. 1 BGB fälschlich als automatische Einbeziehung der vorvertraglichen Baubeschreibung genutzt? Bei Bauträgern über § 650u Abs. 2 BGB ausgeschlossen; Abs. 2/3 bleiben wichtig.
- Wurde MaBV § 7 mit „Vertragssumme plus 5 %“ verwechselt? Nicht behaupten.
- Wurde eine unwirksame AGB-Klausel geltungserhaltend reduziert? Regelfolge § 306 BGB.
- Wurde Abnahme Gemeinschaftseigentum mit Sondereigentumsabnahme vermischt?
- Wurde Schlussrate trotz offener Protokollmängel als fällig behandelt?
- Wurde Verbraucherstatus wegen Gewerbeeinheit oder Kapitalanlage vorschnell verneint?
- Enthält jeder Befund Fallanker statt Standardformel?

## Ausgabe

Ergänze am Ende der Analyse einen knappen Quellen- und Selbstprüfungsvermerk: geprüfte Normen, verifizierte Entscheidungen, nicht verifizierte Prüfhinweise, bewusst nicht verwendete Fundstellen.
