---
name: bericht-arbeitsunfall-dguv-audit-trail
description: "Bericht Arbeitsunfall Dguv, Bericht Audit Trail Freigabe, Bericht Auskunftspflicht Bstatg 15: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Bericht Arbeitsunfall Dguv, Bericht Audit Trail Freigabe, Bericht Auskunftspflicht Bstatg 15

## Arbeitsbereich

In diesem Skill wird **Bericht Arbeitsunfall Dguv, Bericht Audit Trail Freigabe, Bericht Auskunftspflicht Bstatg 15** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bericht-arbeitsunfall-dguv` | Arbeitsunfall/Berufskrankheit melden: Drei-Tage-Regel, Unfallanzeige, Betriebsrat, Fachkraft, Berufsgenossenschaft und Dokumentation. |
| `bericht-audit-trail-freigabe` | Audit-Trail für Meldungen: Version, Quelle, Berechnung, Prüfung, Freigabe, Versand und Korrekturhistorie. |
| `bericht-auskunftspflicht-bstatg-15` | Amtliche Erhebungen verstehen: Auskunftspflicht, Stichprobe, elektronische Meldung, Fristverlängerung, Geheimhaltung und Grenzen der Datenanforderung. |

## Arbeitsweg

Für **Bericht Arbeitsunfall Dguv, Bericht Audit Trail Freigabe, Bericht Auskunftspflicht Bstatg 15** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `berichtspflichten-erlediger` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bericht-arbeitsunfall-dguv`

**Fokus:** Arbeitsunfall/Berufskrankheit melden: Drei-Tage-Regel, Unfallanzeige, Betriebsrat, Fachkraft, Berufsgenossenschaft und Dokumentation.

# Arbeitsunfallanzeige DGUV

## Einsatz

Für Betriebe nach Arbeitsunfall.

## Norm- und Quellenanker

SGB VII; DGUV-Vorgaben live prüfen; ArbSchG.

## Arbeitsfragen

1. Welche Verletzung/Arbeitsunfähigkeit?
2. Welche BG/Unfallkasse?
3. Welche Ursachenmaßnahmen?

## Output

Unfallanzeige und Maßnahmenprotokoll.

## Red Flags

- Unfall vertuscht
- Zeugen nicht dokumentiert
- Arbeitsschutzmaßnahmen fehlen

## Arbeitsstil

Berichtspflichten werden wie kleine Verfahren behandelt: Rechtsgrundlage lesen, Pflichtenträger und Schwelle prüfen, Datenquelle sichern, nur erforderliche Daten melden, Vier-Augen-Freigabe dokumentieren, Versandnachweis ablegen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 2. `bericht-audit-trail-freigabe`

**Fokus:** Audit-Trail für Meldungen: Version, Quelle, Berechnung, Prüfung, Freigabe, Versand und Korrekturhistorie.

# Audit-Trail und Vier-Augen-Freigabe

## Einsatz

Für belastbare Nachvollziehbarkeit.

## Norm- und Quellenanker

- GoBD für steuerlich relevante Aufzeichnungen: Nachvollziehbarkeit, Nachprüfbarkeit, Unveränderbarkeit, Verfahrensdokumentation.
- HGB §§ 238, 257 und AO §§ 146, 147 als Grundlogik für Bücher, Aufzeichnungen und Aufbewahrung, soweit die Meldung buchführungs-/steuerrelevant ist.
- DSGVO Art. 5 Abs. 2, Art. 24, Art. 30, Art. 32 für Rechenschaft, Rollen, TOM und Verarbeitungsverzeichnis, wenn personenbezogene Daten im Bericht stecken.
- Fachrechtliche Nachweispflichten gehen vor: BEHG, KrWG/NachwV, MiLoG, ArbSchG, GEG, Statistikrecht, Zoll/AWV jeweils gesondert prüfen.

## Arbeitsfragen

1. Wer hat welche Daten aus welcher Primärquelle entnommen: ERP, Lohnbuchhaltung, Messstelle, Laborbericht, Steuerkonto, Behördenbescheid?
2. Welche Rechenschritte wurden vorgenommen, und ist jede Formel/Umrechnung versioniert?
3. Wer hat fachlich geprüft, wer rechtlich freigegeben, wer versandt?
4. Welche Korrektur wurde warum ausgelöst: Behördenrückfrage, Fehlerfund, neue Datenquelle, Fristverlängerung?
5. Ist der Versandnachweis beweisbar: Portalquittung, beA/EGVP, ELSTER-Protokoll, DEHSt-Aktenzeichen, Einschreiben, Behördenmail?

## Output

Audit-Trail-Template mit Version, Datenquelle, Berechnung, Prüfer, Freigeber, Versandweg, Behördenzeichen, Korrekturgrund und Aufbewahrungsfrist.

## Red Flags

- Excel überschrieben
- keine Freigabe
- Korrektur nicht dokumentiert
- Freigabe durch dieselbe Person, die die Daten erstellt hat
- Portalquittung fehlt, obwohl die Meldung fristkritisch ist
- Korrektur löscht den alten Stand statt ihn nachvollziehbar zu versionieren

## Arbeitsstil

Berichtspflichten werden wie kleine Verfahren behandelt: Rechtsgrundlage lesen, Pflichtenträger und Schwelle prüfen, Datenquelle sichern, nur erforderliche Daten melden, Vier-Augen-Freigabe dokumentieren, Versandnachweis ablegen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 3. `bericht-auskunftspflicht-bstatg-15`

**Fokus:** Amtliche Erhebungen verstehen: Auskunftspflicht, Stichprobe, elektronische Meldung, Fristverlängerung, Geheimhaltung und Grenzen der Datenanforderung.

# Amtliche Statistik und Auskunftspflicht § 15 BStatG

## Einsatz

Für Schreiben von Statistikämtern, die plötzlich Zahlen, Beschäftigtenstrukturen, Produktion oder Umsätze verlangen.

## Norm- und Quellenanker

BStatG §§ 15, 16; jeweilige Statistikverordnung oder Einzelstatistikgesetz; VwVfG; OWiG.

## Arbeitsfragen

1. Welche Erhebung und Rechtsgrundlage steht im Schreiben?
2. Ist das Unternehmen auskunftspflichtig oder nur freiwillig befragt?
3. Welche Daten sind exakt verlangt und welche nicht?
4. Kann Fristverlängerung oder Klärung beantragt werden?

## Output

Statistik-Anforderungsauswertung, Datenliste, Fristverlängerungsschreiben und Abgabe-Check.

## Red Flags

- Rechtsgrundlage fehlt
- Daten werden über die Frage hinaus geliefert
- Schätzung ohne Kennzeichnung
- Geheimhaltungsbedenken nicht adressiert

## Arbeitsstil

Berichtspflichten werden wie kleine Verfahren behandelt: Rechtsgrundlage lesen, Pflichtenträger und Schwelle prüfen, Datenquelle sichern, nur erforderliche Daten melden, Vier-Augen-Freigabe dokumentieren, Versandnachweis ablegen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.
