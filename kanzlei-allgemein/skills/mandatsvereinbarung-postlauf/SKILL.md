---
name: mandatsvereinbarung-postlauf
description: "Mandatsvereinbarung Postlauf im Plugin Kanzlei Allgemein: prüft konkret Erstellt Mandatsvereinbarung Vollmacht Datenschutzhinweis, Führt den täglichen Postlauf ideal um 11 Uhr. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Mandatsvereinbarung Postlauf

## Arbeitsbereich

**Mandatsvereinbarung Postlauf** ordnet den Fall über die tragenden Prüffelder: Erstellt Mandatsvereinbarung Vollmacht Datenschutzhinweis, Führt den täglichen Postlauf ideal um 11 Uhr. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kanzlei-allgemein-mandatsvereinbarung` | Erstellt Mandatsvereinbarung Vollmacht Datenschutzhinweis Honorarvereinbarung und Vorschuss. Anwendungsfall neues Mandat soll foermlich begründet werden mit allen Pflichtdokumenten nach BRAO. Normen § 3a RVG Honorarvereinbarung § 49b BRAO Verbot Erfolgshonorar Art. 13 DSGVO § 43a BRAO Verschwiegenheit. Prüfraster Mandatsumfang RVG vs. Stundensatz Haftungsbegrenzung Vorschuss Rechtsschutzversicherer KI-Hinweis berufsrechtliche Punkte. Output Mandatsvereinbarungsentwurf Vollmacht Datenschutzhinweis Honorarblatt mit Markierung offener Prüfpunkte. Abgrenzung zu kanzlei-allgemein-mandatsannahme-gwg und kanzlei-allgemein-akte. |
| `kanzlei-allgemein-postlauf` | Führt den täglichen Postlauf ideal um 11 Uhr. Prüft neue Eingänge beA-Journal Fristen Action-Items nicht zugeordnete Akten Versandbedarf EB und Rückfragen. Erstellt ein Postlauf-Journal und übergibt an Akten Fristen Output Zeit und Rechnung. |

## Arbeitsweg

- Rolle und Ziel im Kanzlei Allgemein klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StAG §§ 4, 5, 8-17, 25, 27, 30; DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `kanzlei-allgemein-mandatsvereinbarung`

**Fokus:** Erstellt Mandatsvereinbarung Vollmacht Datenschutzhinweis Honorarvereinbarung und Vorschuss. Anwendungsfall neues Mandat soll foermlich begründet werden mit allen Pflichtdokumenten nach BRAO. Normen § 3a RVG Honorarvereinbarung § 49b BRAO Verbot Erfolgshonorar Art. 13 DSGVO § 43a BRAO Verschwiegenheit. Prüfraster Mandatsumfang RVG vs. Stundensatz Haftungsbegrenzung Vorschuss Rechtsschutzversicherer KI-Hinweis berufsrechtliche Punkte. Output Mandatsvereinbarungsentwurf Vollmacht Datenschutzhinweis Honorarblatt mit Markierung offener Prüfpunkte. Abgrenzung zu kanzlei-allgemein-mandatsannahme-gwg und kanzlei-allgemein-akte.

# Mandatsvereinbarung und Honorarstart

## Zweck

Dieser Skill bereitet Mandatsvereinbarung, Vollmacht, Datenschutzhinweis und Honorarunterlagen vor.

## Bausteine

- Mandatsumfang und ausgeschlossene Tätigkeiten.
- Vollmacht.
- Datenschutzhinweis.
- Honorargrundlage: RVG, Stundenhonorar, Pauschale, Beratungshonorar.
- Vorschuss.
- Haftungsbegrenzung, sofern zulässig und gewünscht.
- Rechtsschutzversicherung und Deckungsanfrage.
- KI-Einsatz-Hinweis und Verweis auf Datenschutzhinweise.
- GwG-Mitwirkung, Identifizierung und Dokumentationspflichten, soweit einschlägig.
- Kündigung und Mandatsbeendigung.

## Haftungsbegrenzung

Immer als prüfpflichtig markieren:

- individuelle Vereinbarung oder AGB-Klausel,
- gesetzliche Mindestanforderungen,
- Versicherungssumme,
- Transparenz,
- keine versteckte Beschränkung.

## Ablauf

1. Mandatsart und Mandatsumfang klären.
2. Honorarweg auswählen.
3. Pflichtinformationen abfragen.
4. Mandatsannahme- und GwG-Status aus `kanzlei-allgemein-mandatsannahme-gwg` übernehmen.
5. Entwurf erzeugen.
6. Prüfpunkte markieren.
7. Freigabe durch Berufsträger verlangen.

## KI- und Datenschutzhinweise

Der Entwurf soll einen knappen, transparenten Hinweis enthalten, dass die Kanzlei technische Hilfsmittel einschließlich KI-gestützter Systeme zur Strukturierung, Recherche, Entwurfsunterstützung, Qualitätskontrolle, Fristen- und Aktenorganisation einsetzen kann. Nicht behaupten, dass bestimmte Anbieter, Schutzmaßnahmen oder Drittlandtransfers geprüft sind, wenn das nicht aktenkundig ist. Auf die Datenschutzhinweise der Kanzlei verweisen.

## GwG-Hinweise

Wenn das Mandat GwG-relevant ist, in Mandatsvereinbarung oder Begleitschreiben aufnehmen:

- Mitwirkung bei Identifizierung.
- Angaben zu auftretenden Personen und wirtschaftlich Berechtigten.
- Nachweise zu Register, Vertretung und Mittelherkunft, soweit erforderlich.
- Dokumentation und Aufbewahrung nach gesetzlichen Pflichten.

## Ausgabe

- Mandatsvereinbarung als Markdown-Entwurf.
- Vollmachtstext.
- Datenschutzhinweis.
- KI- und Datenschutzbaustein aus `assets/templates/mandatsvereinbarung-ki-datenschutz-hinweis.md`.
- Honorarblatt.
- Liste offener Entscheidungen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `kanzlei-allgemein-postlauf`

**Fokus:** Führt den täglichen Postlauf ideal um 11 Uhr. Prüft neue Eingänge beA-Journal Fristen Action-Items nicht zugeordnete Akten Versandbedarf EB und Rückfragen. Erstellt ein Postlauf-Journal und übergibt an Akten Fristen Output Zeit und Rechnung.

# Postlauf um 11 Uhr


## Triage zu Beginn
1. Sind neue Eingaenge seit dem letzten Postlauf zu verarbeiten (Brief, beA, E-Mail, Fax, Messenger)?
2. Gibt es fristwaehrende Dokumente im Posteingang (Klageschrift, Bescheide, Urteile mit EB-Pflicht)?
3. Muss das beA-Journal aktualisiert werden (neue Nachrichten, ZIP-Export, EB-Entscheidungen)?
4. Welche offenen Action-Items aus dem letzten Postlauf sind noch ausstehend?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 173 ZPO — Zeitpunkt der beA-Zustellung: Eingang im Empfangspostfach
- § 174 Abs. 4 ZPO — Elektronisches Empfangsbekenntnis: Datum massgebend fuer Fristbeginn
- Art. 7 PostModG — Vier-Tages-Zustellungsfiktion seit 01.01.2025
- § 51 BRAO — Haftung bei Organisationspflichtverletzung im Postlauf

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill bildet die tägliche Kanzleipost ab. Er ist für den manuellen Aufruf oder für eine Umgebung mit Automationen gedacht.

## Ablauf

1. Neue Eingänge seit dem letzten Postlauf erfassen.
2. Bei beA-Connect das Nachrichtenjournal öffnen, einsehen, Screenshot sichern und `kanzlei-allgemein-bea-journal` starten.
3. Jede neue beA-Nachricht als ZIP-Archiv exportieren oder herunterladen, entpacken und der Akte zuordnen.
4. Jede seit dem letzten Lauf versandte beA-Nachricht im Journal prüfen, als ZIP sichern und entpacken.
5. Elektronische Empfangsbekenntnisse erkennen und EB-anbieten.
6. Nicht zugeordnete Eingänge an `kanzlei-allgemein-intake` geben.
7. Fristen heute, morgen und diese Woche anzeigen.
8. Action-Items nach Verantwortlichen gruppieren.
9. Versandbedarf prüfen.
10. Rückfragen an Mandant, Gericht, Gegner oder intern sammeln.
11. Zeiteinträge für Postbearbeitung vorschlagen.

## Ausgabe

`assets/templates/postlauf-journal.md` verwenden.

## Automationshinweis

Wenn die Umgebung Automationen unterstützt, den Nutzer fragen:

> Soll ich eine tägliche Erinnerung um 11 Uhr für den Postlauf einrichten?

Ohne Automationsunterstützung eine manuelle Checkliste erzeugen.
