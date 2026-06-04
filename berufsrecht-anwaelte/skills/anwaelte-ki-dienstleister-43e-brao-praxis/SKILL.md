---
name: anwaelte-ki-dienstleister-43e-brao-praxis
description: "Anwaltlicher KI-Dienstleister nach § 43e BRAO: Consumer-Tool, Enterprise-Tool, Kanzleiinfrastruktur und Einzelmandats-Tool trennen; Erforderlichkeit, Verschwiegenheit, § 203 StGB, No-Training, Drittstaat, Mandanteninformation und Kanzleivermerk praxisnah prüfen."
---

# KI-Dienstleister nach § 43e BRAO in der Praxis

## Fachkern: KI-Dienstleister nach § 43e BRAO in der Praxis
- **Spezialgegenstand:** KI-Dienstleister nach § 43e BRAO in der Praxis; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BRAO, BORA, FAO, RVG, RDG, GwG, beA, Verschwiegenheit, Interessenkollision und Anwaltsgerichtsbarkeit.
- **Entscheidende Weiche:** Pflichtnorm, Mandatsrolle, Verschulden, Kammerverfahren, Reputationsrisiko, Rechtsbehelf und milderes Organisationsmittel trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Startfrage

Behandle KI nicht als Zauberwort, sondern als Dienstleisterfrage: Wer bekommt welches Mandatsgeheimnis, zu welchem Zweck, auf welcher Vertragsgrundlage, mit welchen technischen Spuren und mit welcher anwaltlichen Endkontrolle?

## Sofort-Triage

| Konstellation | Berufsrechtlicher Ausgangspunkt | Arbeitshypothese |
|---|---|---|
| Öffentliches Consumer-Frontend ohne berufsspezifische Bindung | § 43a Abs. 2 BRAO, § 2 BORA, § 203 StGB | Keine Mandatsgeheimnisse eingeben; nur anonymisiert, abstrahiert oder synthetisch arbeiten. |
| Bewusst beauftragter Fach- oder Enterprise-Dienstleister | § 43e BRAO, § 203 Abs. 4 StGB | Offenlegung kann zulässig sein, wenn sie für die Dienstleistung erforderlich ist und die Vertrags-/Sicherheitskette trägt. |
| Allgemeine Kanzleiinfrastruktur | § 43e Abs. 1 bis 4 BRAO | Regelmäßig kein Einzelmandats-Einwilligungsmodell, aber Tool-Freigabe, Teamregeln und Aktenvermerk nötig. |
| Tool unmittelbar für ein konkretes Einzelmandat | § 43e Abs. 5 BRAO zusätzlich prüfen | Mandantenentscheidung, Aufklärung und Einwilligung sauber dokumentieren. |
| Eigene Kanzlei-Oberfläche/API auf fremdem Modell | § 43e BRAO plus KI-VO-Rollenprüfung | Kanzlei kann organisatorisch stärker in Anbieter-/Betreiberpflichten rutschen. |

## Prüfprogramm

1. **Datenfluss zeichnen.** Welche Daten gehen an Anbieter, Subunternehmer, Logs, Support, Sicherheitsmonitoring, Telemetrie, Modellbetrieb, Backup und Abrechnung?
2. **Erforderlichkeit bestimmen.** Es geht nicht darum, ob KI allgemein nützlich ist, sondern ob diese konkrete Offenlegung für diese konkrete Dienstleistung nötig ist.
3. **Vertrag prüfen.** Textform, Verschwiegenheit gegenüber jedermann, strafrechtliche Belehrung, Kenntnisnahme nur soweit nötig, Subunternehmerzustimmung, Weiterverpflichtung, Löschung, Audit und Incident-Kette.
4. **No-Training absichern.** Mandatsdaten dürfen nicht zur Modellverbesserung, Produktanalyse oder allgemeinen Trainingsdatengewinnung genutzt werden, wenn dafür keine tragfähige berufsrechtliche Grundlage besteht.
5. **Drittstaat sauber trennen.** DSGVO-Transfermechanik ersetzt nicht den berufsrechtlichen Geheimnisschutz. § 43e Abs. 4 BRAO verlangt eine eigene Vergleichbarkeitsprüfung.
6. **Anwaltliche Endverantwortung festhalten.** KI-Output ist Entwurfsmaterial. Zitate, Fristen, Rechtsprechung, Subsumtion und taktische Empfehlungen werden berufsträgerseitig geprüft.

## Ampel

- **Grün:** Anbieter ist bewusst beauftragt, §-43e-Vertrag ist vollständig, No-Training eindeutig, Subunternehmer kontrolliert, EU/EWR oder geprüfter Drittstaat, Endkontrolle organisiert.
- **Gelb:** Vertrag ist grundsätzlich brauchbar, aber Telemetrie, Supportzugriffe, Subunternehmer, Löschfristen oder Mandanteninformation sind unklar.
- **Rot:** Public Tool mit Mandatsdaten, Training/Produktverbesserung mit Aktenmaterial, unkontrollierte Drittstaatkette, keine Textformverpflichtung oder keine anwaltliche Endkontrolle.

## Output

Erstelle einen Kanzleivermerk mit:

- Toolrolle und Datenflussdiagramm in Worten
- §-43e-Erforderlichkeitsnotiz
- Vertragslückenliste
- No-Training-/Telemetrie-Vermerk
- Drittstaat- und Subunternehmermatrix
- Entscheidung: freigeben, nur anonymisiert nutzen, nachverhandeln oder sperren

Schalte bei Vertragsdetails das Plugin `berufsrecht-ki-vertragspruefung` zu.
