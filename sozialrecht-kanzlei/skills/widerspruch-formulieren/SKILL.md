---
name: widerspruch-formulieren
description: Entwirft einen begruendeten Widerspruch gegen einen Sozialleistungsbescheid nach § 84 SGG (Widerspruchsfrist ein Monat ab Bekanntgabe — bei fehlender Rechtsbehelfsbelehrung ein Jahr nach § 66 Abs. 2 SGG). Aus der Bescheidanalyse uebernommene formelle und materielle Angriffspunkte werden in Standardstruktur gegossen (Rubrum Antrag Begruendung Anlagenverzeichnis). Inkludiert hilfsweisen Antrag auf Aussetzung der Vollziehung nach § 86a SGG und Antrag auf Akteneinsicht nach § 25 SGB X.
---

# Widerspruch formulieren (Sozialrecht)

## Eingaben

- Analyseprotokoll aus `bescheidanalyse`.
- Mandantenakte mit Belegen.
- Bescheid im Original.

## Struktur

### 1. Rubrum

- Mandant mit Anschrift Geburtsdatum (sozialrechtlich relevant).
- Anwalt mit Adresse beA-/EGVP-Adresse Aktenzeichen.
- Empfangsbehörde mit Adresse.
- Bezug: Az der Behörde Bescheid vom (Datum).

### 2. Antrag

- "Hiermit lege ich gegen den Bescheid vom (Datum), Az (...), Widerspruch ein und beantrage:
  1. den angefochtenen Bescheid aufzuheben;
  2. (oder) den Bescheid abzuändern und mir Leistungen in voller Höhe zuzuerkennen;
  3. hilfsweise Aussetzung der Vollziehung nach § 86a SGG;
  4. Akteneinsicht in die Verwaltungsakte gemäß § 25 SGB X."

### 3. Begründung

Aus dem Analyseprotokoll übernehmen:

- Formelle Mangel zuerst (Anhörung Begründungs- und Rechtsbehelfsbelehrungsfehler).
- Materielle Mangel sortiert nach Erfolgsaussicht.
- Subsumtion zur konkreten Anspruchsgrundlage.
- Rechtsprechung mit Pinpoint (BSG-Urteile mit Az und Rn).
- Vorgreiflichkeit von Verfassungs- und Unionsrecht falls einschlägig.

### 4. Beweis- und Anlagenverzeichnis

Verweis auf den Skill `anlagen-erstellen`. Anlagen W1 W2 W3 mit Inhaltsbeschreibung.

### 5. Form und Frist

- **Frist** ein Monat ab Bekanntgabe (§ 84 Abs. 1 SGG).
- **Bei fehlender Rechtsbehelfsbelehrung** ein Jahr (§ 66 Abs. 2 SGG).
- **Form** schriftlich oder zur Niederschrift bei der Behörde.
- **Versand** über beA (RA-Pflicht seit 01.01.2022) oder EGVP. Eingang am Tag der Übertragung.

### 6. Vorfrist im Fristenbuch

Drei Tage vor Fristablauf Vorfrist setzen über den Skill `fristenbuch-sozialrecht`.

## Ausgabe

- `widerspruch-<az>-<datum>.docx` und Markdown-Spiegel.
- Eintrag im Fristenbuch.
- Eintrag im Postausgang.

## Versand-Check

Vor Versand der Skill `versand-vor-check` aus dem Plugin `kanzlei-allgemein`. Prüft PDF Inhalt Signatur Empfängeradresse und Anlagenvollständigkeit.

## Hinweis Aussetzung der Vollziehung

Bei Bescheiden über Aufhebung Rückforderung Sanktion: Widerspruch hat keine aufschiebende Wirkung wenn die Behörde die sofortige Vollziehung angeordnet hat oder das Gesetz sie vorsieht (§ 86a Abs. 2 SGG). Hilfsantrag auf Aussetzung der Vollziehung an die Behörde — bei Ablehnung Eilantrag § 86b SGG ans Sozialgericht (siehe Skill `eilantrag-sozialrecht`).

## Triage — kläre vor dem Widerspruchsentwurf

1. Frist gewahrt? — ein Monat ab Bekanntgabe (§ 84 SGG); bei fehlender Rechtsbehelfsbelehrung ein Jahr (§ 66 Abs. 2 SGG)
2. Liegt Analyseprotokoll aus `bescheidanalyse` vor? — Voraussetzung für substantiierte Begründung
3. Ist aufschiebende Wirkung erforderlich? — bei sofortiger Vollziehung Antrag auf Aussetzung (§ 86a SGG), sonst Eilantrag (§ 86b SGG)
4. Akteneinsicht bereits beantragt (§ 25 SGB X)? — Begründung kann nachgereicht werden, Frist muss gehalten werden
5. Beweisanträge formuliert? — insbesondere bei medizinischen Fragen Gutachter-Antrag vorbereiten

## Aktuelle Rechtsprechung

- BSG, Urt. v. 11.06.2003 - B 5 RJ 28/02 R, SozR 4-1500 § 84 Nr. 1 Rn. 16 — Der Widerspruch muss innerhalb der Monatsfrist des § 84 Abs. 1 SGG eingelegt werden; eine Begründung ist nicht innerhalb dieser Frist erforderlich — sie kann nachgereicht werden. Auf die rechtzeitige Einlegung kommt es an.
- BSG, Urt. v. 10.03.2011 - B 3 P 3/10 R, SozR 4-1500 § 63 Nr. 5 Rn. 21 — Nach § 63 SGB X sind dem Widerspruchsführer die notwendigen Aufwendungen zu erstatten, wenn sein Widerspruch Erfolg hat und er anwaltlich vertreten war; die Notwendigkeit anwaltlicher Vertretung ist in rechtlich komplexen Sozialrechtsfällen regelmäßig gegeben.
- BSG, Urt. v. 29.11.2017 - B 14 AS 42/16 R, SozR 4-4200 § 33 Nr. 7 Rn. 19 — Formelle Mängel des Bescheids (fehlende Anhörung § 24 SGB X, unzureichende Begründung § 35 SGB X) sind eigenständige Widerspruchsgründe; das Widerspruchsverfahren ist kein bloßes Nachprüfungsverfahren, sondern verpflichtet die Behörde zur vollständigen Überprüfung.
- BSG, Urt. v. 07.11.2006 - B 7b AS 8/06 R, SozR 4-4200 § 22 Nr. 1 Rn. 18 — Bei Widersprüchen gegen Sanktions- oder Aufhebungsbescheide im SGB II ist besonders auf die Auseinandersetzung mit dem Anhörungsgebot nach § 24 SGB X zu achten; eine Nachholung der Anhörung im Widerspruchsverfahren ist zwar möglich (§ 41 SGB X), heilt aber nicht automatisch alle Mängel.

## Kommentarliteratur

- Kasseler Kommentar Sozialversicherungsrecht, Steinwedel § 84 SGG Rn. 1 ff. (Widerspruchsfrist, Form)
- Hauck/Noftz SGB X, § 63 Rn. 1 ff. (Kostenerstattung im Widerspruchsverfahren)
