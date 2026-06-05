---
name: weg-abrechnung
description: "WEG Abrechnung im Plugin Immobilienrechtspraxis: fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output."
---

# WEG Abrechnung

## Arbeitsbereich

**WEG Abrechnung** priorisiert Aktenlage, Fristen, Zuständigkeit, Beweislast und gewünschten Output. Die Prüfung beginnt beim sachtragenden Prüffeld und endet mit einem verwertbaren Arbeitsergebnis.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `weg-abrechnung-mieterschnittstelle-datenpaket` | Datenpaket WEG-Abrechnung zu Mietern: übersetzt Jahresabrechnung, Einzelabrechnung, Wirtschaftsplan, Heizkosten, CO2-Daten und Belege in eine mietrechtlich brauchbare Betriebskostenabrechnung; mit Abrechnungsspitze, nicht umlagefähigen Positionen und Eigentümerkommunikation. |

## Arbeitsweg

- Rolle und Ziel im Immobilienrechtspraxis klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BGB §§ 535-577a, BetrKV, WEG §§ 24, 25, 27, BGB §§ 558, 558a, 558b, 573, 573c — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `weg-abrechnung-mieterschnittstelle-datenpaket`

**Fokus:** Datenpaket WEG-Abrechnung zu Mietern: übersetzt Jahresabrechnung, Einzelabrechnung, Wirtschaftsplan, Heizkosten, CO2-Daten und Belege in eine mietrechtlich brauchbare Betriebskostenabrechnung; mit Abrechnungsspitze, nicht umlagefähigen Positionen und Eigentümerkommunikation.

# WEG-Abrechnung als Mieterdatenpaket

## Fachkern: WEG-Abrechnung als Mieterdatenpaket
- **Spezialgegenstand:** WEG-Abrechnung als Mieterdatenpaket wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB, GBO, WEG, BauGB, ErbbauRG, MaBV, Mietrecht, Grundpfandrechte, Notar-/Registervollzug und öffentlich-rechtliche Lasten.
- **Entscheidende Weiche:** Trenne Eigentum, Besitz, Grundbuchabteilung, Belastung, Fälligkeit, Vollzug, Mängel, Miet-/Nutzungsverhältnis und Finanzierung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe

Dieser Skill hilft, wenn ein vermietender Wohnungseigentümer seine WEG-Unterlagen bekommt und daraus eine Betriebskostenabrechnung für den Mieter erstellen muss. Er verhindert, dass interne WEG-Kosten unbesehen in das Mietverhältnis rutschen.

## Trennung

- **GdWE/Eigentümer**: Nachschüsse und Vorschussanpassungen aus § 28 Abs. 2 WEG.
- **Vermieter/Mieter**: Betriebskosten nach Mietvertrag, BetrKV, HeizkostenV, CO2KostAufG und § 556 BGB.
- **Hausverwaltung**: Datenlieferantin, nicht automatisch mietrechtliche Abrechnungsstelle.

## Datenanforderung an WEG-Verwaltung

1. Gesamt- und Einzelabrechnung.
2. Verteilungsschlüssel je Kostenart.
3. Rechnungen und Zahlungsbelege.
4. Heizkostenabrechnung mit Nutzerwechseln.
5. CO2-Daten aus Brennstoffrechnung.
6. Tätigkeits-/Stundenlisten für Hausmeister.
7. Liste nicht umlagefähiger Kosten: Verwalter, Rücklage, Reparaturen, Prozesskosten, Bank-/Finanzierungskosten.

## Übersetzungstabelle

| WEG-Unterlage | Mietrechtliche Nutzung | Risiko |
| --- | --- | --- |
| Einzelabrechnung | Ausgangsdaten | enthält nicht umlagefähige Positionen |
| Wirtschaftsplan | Vorauszahlungsprognose | keine Jahresabrechnung |
| Beschluss § 28 WEG | Zahlungspflicht Eigentümer | nicht Zahlungspflicht Mieter |
| Vermögensbericht | Transparenz WEG | nicht in Betriebskostenabrechnung |
| Heizkostenanlage | Mieterabrechnung | HeizkostenV/CO2 prüfen |

## Output

- Datenpaket-Checkliste für Verwaltung.
- Mietrechtliche Übernahmematrix.
- Entwurf Betriebskostenabrechnung aus WEG-Daten.
- Schreiben an Eigentümer: welche Positionen nicht umgelegt werden dürfen.

## Quellenregel

§ 28 WEG, § 556 BGB, BetrKV, HeizkostenV und CO2KostAufG aktuell prüfen. WEG-Rechtsprechung zu Abrechnungsspitzen nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen.
