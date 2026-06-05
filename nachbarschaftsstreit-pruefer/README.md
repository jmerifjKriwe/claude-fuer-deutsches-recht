# Nachbarschaftsstreit-Prüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`nachbarschaftsstreit-pruefer`) | [`nachbarschaftsstreit-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/nachbarschaftsstreit-pruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Nachbarschaftsstreit Rosengartenstraße** (`nachbarschaftsstreit-horrorfall-rosengarten`) | [Gesamt-PDF lesen](../testakten/nachbarschaftsstreit-horrorfall-rosengarten/gesamt-pdf/nachbarschaftsstreit-horrorfall-rosengarten_gesamt.pdf) | [`testakte-nachbarschaftsstreit-horrorfall-rosengarten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-nachbarschaftsstreit-horrorfall-rosengarten.zip) |
| **Akte Wusterhagen: Mühlenstau, Chaussee und Aufopferung** (`preussisches-landrecht-wusterhagen-muehlenstau-aufopferung`) | [Gesamt-PDF lesen](../testakten/preussisches-landrecht-wusterhagen-muehlenstau-aufopferung/gesamt-pdf/preussisches-landrecht-wusterhagen-muehlenstau-aufopferung_gesamt.pdf) | [`testakte-preussisches-landrecht-wusterhagen-muehlenstau-aufopferung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-preussisches-landrecht-wusterhagen-muehlenstau-aufopferung.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Plugin für Nachbarrecht und eskalierte Grundstückskonflikte: Überbau, Überhang, Äste und Wurzeln, Grenzbäume, Einfriedung, Zaun, Mauer, Hecke, Immissionen, Vertiefung, drohender Einsturz, Notweg, Hammerschlags- und Leiterrecht, Beweissicherung, Aufforderungsschreiben, einstweilige Verfügung, Klage und Vergleich.

**Keine Rechtsberatung.** Das Plugin erzeugt strukturierte Prüfungen, Entwürfe und Workflows zur anwaltlichen Kontrolle. Landesnachbarrecht, Baumschutzsatzungen, Bebauungspläne und örtliche Satzungen müssen im konkreten Fall geprüft werden.

## Start

```
/nachbarschaftsstreit-pruefer:allgemein
```

Der Einstieg fragt in kurzer Zeit ab: Grundstücke, Grenze, Bundesland, Streitgegenstand, Gefahr, Beweislage, bisherige Schreiben, gewünschter Ton und Ziel. Danach routet er zu den Spezialskills.

## Skills (20)

| Skill | Zweck |
|---|---|
| `allgemein` | Schöner Einstieg, Fristen-/Gefahrenscan, Routing und Arbeitsplan |
| `nachbarrecht-kaltstart-triage` | Erstaufnahme des Konflikts mit Bundesland, Grundstück, Beteiligten und Risiko |
| `akten-und-grundstuecksaufnahme` | Grundbuch, Liegenschaftskarte, Baulast, Dienstbarkeit, Fotos und Chronologie erfassen |
| `anspruchslandkarte-bgb-nachbarrecht` | Anspruchsgrundlagen nach BGB und Landesrecht sortieren |
| `ueberbau-pruefung` | Überbau nach §§ 912-916 BGB, Widerspruch, Duldung, Rente, Abkauf |
| `ueberhang-aeste-wurzeln` | Überhängende Äste, Wurzeln, Fristsetzung, Selbsthilfe nach § 910 BGB |
| `grenzbaum-und-grenzanlage` | Grenzbaum, Grenzsträucher und gemeinschaftliche Grenzanlagen §§ 921-923 BGB |
| `einfriedung-zaun-mauer-hecke` | Zaun, Mauer, Hecke, Kosten, Standort, Ortsüblichkeit und Landesrecht |
| `immissionen-laerm-geruch-rauch-licht` | Geräusche, Gerüche, Rauch, Licht, Erschütterungen, § 906 BGB |
| `vertiefung-baugrube-stuetzverlust` | Baugrube, Unterfangung, Stütze des Nachbargrundstücks, § 909 BGB |
| `drohender-einsturz-gefahranlage` | Gefährliche Anlagen und Einsturzrisiken, §§ 907, 908 BGB |
| `notweg-zufahrt-wegerecht` | Notweg, Zufahrt, Grunddienstbarkeit, Baulast, §§ 917, 918 BGB |
| `hammerschlags-und-leiterrecht` | Betreten des Nachbargrundstücks für Bau-/Instandhaltungsarbeiten nach Landesrecht |
| `landesnachbarrecht-router` | Bundesland auswählen und landesrechtliche Prüfmodule planen |
| `beweissicherung-ortstermin-fotos` | Ortstermin, Fotoplan, Messpunkte, Sachverständige und selbständiges Beweisverfahren |
| `selbsthilfe-und-eskalationsgrenzen` | Was darf man selbst tun, was nicht, und wann drohen Besitz-/Eigentumsverletzungen? |
| `aufforderungsschreiben-nachbar` | Sachliches, druckvolles Anspruchs- und Fristsetzungsschreiben |
| `einstweilige-verfuegung-und-klage` | Eilrechtsschutz, Unterlassung, Beseitigung, Duldung, Feststellung, Streitwert |
| `vergleich-mediation-nachbarschaftsfrieden` | Vergleich, Nutzungsregelung, Rückschnittplan, Kosten- und Zugangslösung |
| `horrorfall-aktenauswertung` | Große unordentliche Nachbarschaftsakte auswerten und in Arbeitsstränge zerlegen |

## Quellenstand

Stand: 05/2026. Kernnormen: BGB §§ 903, 906-923, 823, 862, 1004; Landesnachbarrechtsgesetze und kommunale Satzungen nach Bundesland/Gemeinde.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anspruchslandkarte-bgb-aufforderungsschreiben` | Anspruchslandkarte BGB Aufforderungsschreiben im Nachbarschaftsstreit: prüft konkret Anspruchslandkarte für Nachbarschaftsstreit erstellen, Aufforderungsschreiben im Nachbarschaftsstreit erstellen, Beweissicherung im Nachbarrechtsfall pl... |
| `aufforderung-beweise-red-grenzbaum` | Aufforderung Beweise RED Grenzbaum im Nachbarschaftsstreit: prüft konkret Aufforderung, Beweise, Grenzbaum. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `drohender-einsturz-einfriedung-zaun` | Drohender Einsturz Einfriedung Zaun im Nachbarschaftsstreit: prüft konkret Gefährliche Anlagen und drohenden Gebäudeeinsturz prüfen, Einfriedung, Zaun, Mauer. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schr... |
| `fristennotiz-naechster-ueberbau-akten` | Fristennotiz Naechster Ueberbau Akten im Nachbarschaftsstreit: prüft konkret Pruefer, Ueberbau, Grundstücks- und Aktenaufnahme im Nachbarrechtsfall. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `grenzbaum-grenzanlage-hammerschlags` | Grenzbaum Grenzanlage Hammerschlags im Nachbarschaftsstreit: prüft konkret Grenzbaum, Grenzstrauch und gemeinschaftliche Grenzanlagen prüfen, Hammerschlags- und Leiterrecht prüfen, Große. Liefert priorisierten Output mit Norm-Pinpoints,... |
| `hammerschlagsrecht-hecke-immissionen` | Hammerschlagsrecht Hecke Immissionen im Nachbarschaftsstreit: prüft konkret Hammerschlagsrecht, Hecke, Immissionen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `immissionen-laerm-landesnachbarrecht` | Immissionen Laerm Landesnachbarrecht im Nachbarschaftsstreit: prüft konkret Nachbarliche Immissionen prüfen, Bundesland-Router für Landesnachbarrecht, Spezialfall Grenzbebauung und Ueberhang § 910 BGB /. Liefert priorisierten Output mit... |
| `kaltstart-abschlussprodukt-und-uebergabe` | Kaltstart: Einstieg und Routing; Abschlussprodukt und Übergabe: klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `klage-beweislast-nachbarrecht` | Klage Beweislast Nachbarrecht im Nachbarschaftsstreit: prüft konkret Klage, Nachbarrecht, Nachbarschaftsstreit. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `laermimmissionen-mediation-vorrang` | Laermimmissionen Mediation Vorrang im Nachbarschaftsstreit: prüft konkret Spezialfall Laermimmissionen TA Laerm und LAI-Hinweise, Leitfaden Mediation und obligatorisches Gueteverfahren §, Bauleiter Uebersicht Nachbarrecht. Liefert priori... |
| `mauer-quellenkarte` | Mauer Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `nachbarrecht-kaltstart-triage` | Erstaufnahme eines Nachbarrechtsfalls: Beteiligte, Grundstücke, Bundesland, Grenze, Streitgegenstand, Gefahr, Fristen, Beweise, bisherige Eskalation und Ziel klären; danach in die passenden Fachmodule routen. |
| `nachbarschaftsstreit-fristen-risiko-mandant` | Fristen Risiko Mandant im Nachbarschaftsstreit: prüft konkret Fristen- und Risikoampel im Plugin, Mandantenkommunikation im Plugin, Red-Team Qualitygate im Plugin nachbarschaftsstreit-pruefer. Liefert priorisierten Output mit Norm-Pinpoi... |
| `nachbarschaftsstreit-pruefer-anschluss-router` | Anschluss Router im Nachbarschaftsstreit: prüft konkret Einstieg, Schnelltriage und Fallrouting im Nachbarschaftsstreit-Prüfer, Anschluss-Skills Router im Plugin, Chronologie und Belegmatrix im Plugin. Liefert priorisierten Output mit No... |
| `nachbarschaftsstreit-pruefer-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `nachbarschaftsstreit-pruefer-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `nachbarschaftsstreit-pruefer-output-waehlen` | Output wählen im Nachbarschaftsstreit: Diese Output-Weiche für Nachbarschaftsstreit Prüfer entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `nachbarschaftsstreit-pruefer-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `nachbarschaftsstreit-pruefer-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `notweg-ueberhang-sonderfall-edge` | Notweg Ueberhang Sonderfall Edge im Nachbarschaftsstreit: prüft konkret Notweg, Ueberhang, Vergleich. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `notweg-zufahrt-selbsthilfe-eskalationsgrenzen` | Notweg Zufahrt Selbsthilfe Eskalationsgrenzen im Nachbarschaftsstreit: prüft konkret Notweg, Zufahrt und Wegerecht prüfen, Selbsthilfe im Nachbarrecht prüfen, Aeste. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächst... |
| `ueberbau-ueberhang-aeste-mediation` | Ueberbau Ueberhang Aeste Mediation im Nachbarschaftsstreit: prüft konkret Überbau nach §§ 912-916 BGB prüfen, Überhängende Äste, eindringende Wurzeln, Laub. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `vertiefung-baugrube` | Vertiefung Baugrube im Nachbarschaftsstreit: fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |
| `vertiefung-interessen-wurzeln-zaun` | Vertiefung Interessen Wurzeln Zaun im Nachbarschaftsstreit: prüft konkret Vertiefung, Wurzeln, Zaun. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
