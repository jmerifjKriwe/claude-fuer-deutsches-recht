---
name: frist-stunden-kosten-haftung
description: "Frist 48 Stunden Bekanntgabe, Kosten Haftung Und Versicherung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Frist 48 Stunden Bekanntgabe, Kosten Haftung Und Versicherung

## Arbeitsbereich

In diesem Skill wird **Frist 48 Stunden Bekanntgabe, Kosten Haftung Und Versicherung** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `frist-48-stunden-bekanntgabe` | Berechnet die versammlungsrechtliche 48-Stunden-Frist bis zur Bekanntgabe oder Einladung und markiert Landesabweichungen. |
| `kosten-haftung-und-versicherung` | Prüft Kosten, Gebühren, Schäden, Haftung, Versicherung und Regress rund um Versammlungen. |

## Arbeitsweg

Für **Frist 48 Stunden Bekanntgabe, Kosten Haftung Und Versicherung** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `versammlungsrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `frist-48-stunden-bekanntgabe`

**Fokus:** Berechnet die versammlungsrechtliche 48-Stunden-Frist bis zur Bekanntgabe oder Einladung und markiert Landesabweichungen.

# Die 48 Stunden laufen oft vor der Bekanntgabe

## Worum es geht
Prüfe immer, ob die Frist vor Einladung, Bekanntgabe oder Durchführung läuft. Bundes-VersG, Berlin, NRW und Bayern knüpfen typischerweise an Bekanntgabe oder Einladung an, aber Landesrecht bleibt maßgeblich.

## Kaltstartfragen
1. In welchem Bundesland und an welchem genauen Ort soll die Versammlung stattfinden?
2. Geht es um eine öffentliche Versammlung unter freiem Himmel, einen Aufzug, eine Innenversammlung, eine private Zusammenkunft oder eine Mischform?
3. Wann soll die Versammlung stattfinden und wann soll oder wurde sie öffentlich bekannt gemacht?
4. Welche Behörde, Polizei, E-Mail, Onlineformular oder welcher Bescheid liegt bereits vor?
5. Was ist das konkrete Ziel: Anzeige erstellen, Behördeneinwand beantworten, Auflage prüfen, Eilantrag vorbereiten oder Durchführung absichern?

## Arbeitsweise
Samstage, Sonn- und Feiertage können je nach Landesrecht anders behandelt werden. Nutze daher den Landesskill und markiere Unsicherheit bis zur amtlichen Quelle.

## Rechtslogik
- Ausgangspunkt ist Art. 8 GG: friedliche Versammlung ohne Waffen, grundsätzlich ohne Erlaubnis.
- Für Versammlungen unter freiem Himmel greifen Bundes- oder Landesversammlungsgesetze; die Anzeige ist keine Genehmigung.
- Beschränkungen brauchen eine tragfähige Rechtsgrundlage, konkrete Tatsachen, unmittelbare Gefahr und Verhältnismäßigkeit.
- Kooperation ist sinnvoll, aber kein Verzicht auf Ort, Zeit, Thema oder Modalitäten der Versammlung.

## Output
Output: Fristtabelle mit Anzeigezeitpunkt, frühester Bekanntgabe, spätester Anzeige, Eilfalloption und Dokumentationshinweis.

## Qualitätsgate
- Wurde das richtige Landesrecht verwendet?
- Ist die zuständige Behörde oder Polizeidienststelle konkret benannt?
- Sind Frist, Bekanntgabe und Eil- oder Spontanfall sauber getrennt?
- Werden Grundrechtsposition und praktische Sicherheitsbelange zusammen gedacht?
- Sind alle Formulierungen knapp, belegbar und ohne unnötige Selbstbeschränkung?


## Quellen- und Aktualitätsregel
- Bundesrecht und Landesrecht live prüfen; im Zweifel zuerst `offizielle-quellen-livecheck` verwenden.
- Rechtsprechung nur zitieren, wenn Gericht, Entscheidungsform, Datum, Aktenzeichen und eine frei zugängliche Quelle vorliegen.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.
- Bei Behördenformularen immer die konkrete Stadt, den Landkreis oder das Land prüfen, weil Zuständigkeit und Portale stark abweichen.

## 2. `kosten-haftung-und-versicherung`

**Fokus:** Prüft Kosten, Gebühren, Schäden, Haftung, Versicherung und Regress rund um Versammlungen.

# Kosten nicht überschätzen, Haftung nicht ignorieren

## Worum es geht
Kläre, ob Gebühren erhoben werden dürfen, ob Sondernutzung betroffen ist, wer für Schäden haftet und welche Versicherung oder Vereinsstruktur existiert.

## Kaltstartfragen
1. In welchem Bundesland und an welchem genauen Ort soll die Versammlung stattfinden?
2. Geht es um eine öffentliche Versammlung unter freiem Himmel, einen Aufzug, eine Innenversammlung, eine private Zusammenkunft oder eine Mischform?
3. Wann soll die Versammlung stattfinden und wann soll oder wurde sie öffentlich bekannt gemacht?
4. Welche Behörde, Polizei, E-Mail, Onlineformular oder welcher Bescheid liegt bereits vor?
5. Was ist das konkrete Ziel: Anzeige erstellen, Behördeneinwand beantworten, Auflage prüfen, Eilantrag vorbereiten oder Durchführung absichern?

## Arbeitsweise
Trenne Polizeikosten, Verwaltungsgebühren, Mietkosten, Technik, Reinigung, Schäden durch Dritte und eigene Pflichtverletzung.

## Rechtslogik
- Ausgangspunkt ist Art. 8 GG: friedliche Versammlung ohne Waffen, grundsätzlich ohne Erlaubnis.
- Für Versammlungen unter freiem Himmel greifen Bundes- oder Landesversammlungsgesetze; die Anzeige ist keine Genehmigung.
- Beschränkungen brauchen eine tragfähige Rechtsgrundlage, konkrete Tatsachen, unmittelbare Gefahr und Verhältnismäßigkeit.
- Kooperation ist sinnvoll, aber kein Verzicht auf Ort, Zeit, Thema oder Modalitäten der Versammlung.

## Output
Output: Kosten- und Haftungsampel.

## Qualitätsgate
- Wurde das richtige Landesrecht verwendet?
- Ist die zuständige Behörde oder Polizeidienststelle konkret benannt?
- Sind Frist, Bekanntgabe und Eil- oder Spontanfall sauber getrennt?
- Werden Grundrechtsposition und praktische Sicherheitsbelange zusammen gedacht?
- Sind alle Formulierungen knapp, belegbar und ohne unnötige Selbstbeschränkung?


## Quellen- und Aktualitätsregel
- Bundesrecht und Landesrecht live prüfen; im Zweifel zuerst `offizielle-quellen-livecheck` verwenden.
- Rechtsprechung nur zitieren, wenn Gericht, Entscheidungsform, Datum, Aktenzeichen und eine frei zugängliche Quelle vorliegen.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.
- Bei Behördenformularen immer die konkrete Stadt, den Landkreis oder das Land prüfen, weil Zuständigkeit und Portale stark abweichen.
