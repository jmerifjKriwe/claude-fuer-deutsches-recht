# Megaprompt: bautraegervertrag-pruefer

## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 30 Skills des Plugins `bautraegervertrag-pruefer`.

## Inhaltsverzeichnis

1. **workflow-one-shot-verbraucherpruefung** — One-Shot-Workflow für die verbraucherseitige Prüfung eines deutschen Bauträgervertrags: startet aus Vertrag oder Aktenor…
2. **fall-fingerabdruck-und-schnelltriage** — Fall-Fingerabdruck für Bauträgerakten: extrahiert Urkunde, Verkäufer, Verbraucherrolle, Einheit, Kaufpreis, Raten, Siche…
3. **hoai-technik-baugrund-und-objektueberwachung** — Technischer Realitätscheck im Bauträgerprojekt: HOAI-Leistungsphasen als Prüfraster, Baugrund, Objektüberwachung, anerka…
4. **bauzeit-verzug-vertragsstrafe-und-hoehere-gewalt** — Bauzeit- und Verzugsprüfung beim Bauträgervertrag: verbindlicher Termin, Bezugsfertigkeit, vollständige Fertigstellung, …
5. **quellenhygiene-rechtsprechungsanker-und-bughunt** — Quellen- und Bug-Hunt-Skill für Bauträgervertragsprüfungen: verifiziert Normenstand, BGH-/OLG-Rechtsprechung, MaBV, AGB,…
6. **verhandlung-drei-dokumente-paket** — Drei-Dokumente-Ausgabe für Bauträgervertragsprüfung: Mandantenanschreiben, klauselorientiertes Gutachten und Schreiben a…
7. **eigentumssicherung-vormerkung-lastenfreistellung-und-insolvenz** — Eigentumssicherung beim Bauträgervertrag: Auflassungsvormerkung, Rang, Lastenfreistellung, Globalgrundschuld, Pfandfreig…
8. **verzugsschadenspositionen-berechnung-und-zinsen** — Berechnet Verzugsschäden beim verspäteten Bauträgerprojekt: Ersatzwohnung, Umzug, Lager, Bereitstellungszinsen, doppelte…
9. **din-anerkannte-regeln-technik-und-standardwechsel** — Prüft technische Standards im Bauträgervertrag: DIN-Normen, anerkannte Regeln der Technik, Stand der Technik, Stand von …
10. **notarhaftung-belehrung-und-streitverkuendung** — Prüft notarielle Amtspflichten im Bauträgervertrag: § 17 BeurkG, § 14 BNotO, § 19 BNotO, MaBV-/AGB-Klauselkontrolle, Pre…
11. **wohnungseigentum-teilungserklaerung-und-erstverwalter** — WEG- und Teilungserklärungsprüfung beim Bauträgerprojekt: Sondereigentum, Gemeinschaftseigentum, Sondernutzungsrechte, U…
12. **geschaeftsfuehrer-architekt-und-bautenstandshaftung** — Prüft Drittansprüche bei Bauträgerprojekten: Geschäftsführerhaftung nach § 823 Abs. 2 BGB i.V.m. § 3/§ 7 MaBV, § 263 StG…
13. **abnahme-gemeinschaftseigentum-schlussrate-und-maengelrechte** — Abnahmeprüfung im Bauträgervertrag: Sondereigentum, Gemeinschaftseigentum, Vertreter-/Sachverständigenabnahme, Erstverwa…
14. **sonderwuensche-preisanpassung-und-ausstattungswahl** — Sonderwünsche und Bemusterung im Bauträgervertrag: prüft Form, MaBV-Einordnung, Vorauszahlung, Ausstattungswahl, Mehr-/M…
15. **unwirksame-abnahmeklauseln-dreissig-jahre-und-nachholung** — Prüft unwirksame Abnahmeklauseln im Bauträgervertrag: Erstverwalter, Sachverständige, Erwerbervertreter, Nachzügler, § 6…

---

## Skill: `workflow-one-shot-verbraucherpruefung`

_One-Shot-Workflow für die verbraucherseitige Prüfung eines deutschen Bauträgervertrags: startet aus Vertrag oder Aktenordner, bildet Fall-Fingerabdruck, prüft MaBV, § 650u/§ 650v BGB, § 650m Abs. 2 BGB, AGB, Bausoll, Abnahme, WEG, Insolvenzpfad und erzeugt drei fertige Dokumente._

# One-Shot-Verbraucherprüfung Bauträgervertrag

## Gegenstand

Dieser Skill ist der Gesamtworkflow für Verbraucher, die einen deutschen Bauträgervertrag über Wohnung, Haus, Stellplatz, Keller, Sondernutzungsrecht oder Erbbaurecht prüfen lassen wollen. Er beginnt mit der konkreten Urkunde und endet nicht bei einer Ampel, sondern bei drei verwendbaren Texten: Mandantenanschreiben, Mandantengutachten und Schreiben an Bauträger/Notar.

## Sofortstart aus der Akte

Wenn PDF, DOCX, Markdown, OCR-Text, Scan oder Aktenordner vorliegt, werte zuerst die Akte aus. Frage nicht allgemein nach Rolle oder Ziel, wenn Urkunde, Mailverkehr oder Vertragsentwurf das bereits zeigen. Rückfragen kommen gebündelt am Ende des ersten Durchgangs und nur zu Punkten, ohne die eine Bewertung objektiv schief würde.

## Prüfspur

1. Vertragsstatus: Entwurf, beurkundet, vor erster Rate, Bauphase, vor Abnahme, nach Abnahme, Schlussrate, Insolvenzsignal, Klage.
2. Käuferrolle: Verbraucher, Eigennutzung, private Kapitalanlage, gemischte Nutzung; Gewerbeeinheit nicht vorschnell als Unternehmerfall behandeln.
3. Gegenstand: Einheit, Miteigentumsanteil, Stellplatz, Keller, Sondernutzungsrechte, Wohnfläche, Teilungserklärung, Bauabschnitt.
4. Zahlungen: Kaufpreis, Reservierungsentgelt, Sonderwünsche, MaBV-Raten, Schlussrate, Notaranderkonto, Finanzierungsvollmacht.
5. Sicherheiten: Vormerkung, Lastenfreistellung, § 650m Abs. 2 BGB, § 7 MaBV, Freigabemechanik, Insolvenzpfad.
6. Bausoll: Baubeschreibung, Pläne, Bemusterung, Wohnflächenmethode, Energie, Schall, Brand, Feuchte, anerkannte Regeln der Technik.
7. Abnahme: Sondereigentum, Gemeinschaftseigentum, Erstverwalter/Sachverständiger, Nachzügler, Verjährungsbeginn, Schlussrate.
8. WEG: Kostenkreise, Untergemeinschaften, Wartungsverträge, Änderungsvollmachten, Erstverwalter.
9. Streit: Zurückbehaltung, Besitzübergabe, Nacherfüllung, Vorschuss, Feststellung, Rücktritt nur nach Vormerkungsrisiko.

## Normenanker

Prüfe mindestens §§ 305-310, 306, 307, 308 Nr. 4, 309 Nr. 1, Nr. 2 lit. a, Nr. 8, Nr. 12, Nr. 15, 311b, 313, 315, 320, 323, 346 ff., 633-641, 642, 643, 650i, 650j, 650k Abs. 2/3, 650m Abs. 2, 650n, 650u, 650v, 812, 817, 818, 823 Abs. 2, 883, 925 BGB; §§ 3, 7, 12 MaBV; § 17 BeurkG; §§ 103, 106 InsO; WEG, soweit Gemeinschaftseigentum betroffen ist.

## Rechtsprechungsanker nur nach Live-Prüfung

Aktuelle BGH-Anker: VII ZR 68/24 und VII ZR 108/24 zur Abnahme des Gemeinschaftseigentums und Verjährung; VII ZR 88/25 zur Schlussrate bei vollständiger Fertigstellung; V ZR 91/25 zu Zustimmungspflichten bei Änderungen der Teilungserklärung. Verwende sie nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## Pflichtausgabe

1. **Mandantenanschreiben:** klare Handlungsempfehlung: unterschreiben, nachverhandeln, Zahlung stoppen, Nachweise verlangen, Abnahme verweigern oder Prozess vorbereiten.
2. **Mandantengutachten:** klauselorientiert mit Originalstelle, Fallanker, Norm, Risiko, Gegenargument, Antwort und konkreter Neufassung.
3. **Aufforderungsschreiben:** ruhig, präzise, mit Frist, konkreter Änderung, Dokumentenliste und Zahlungs-/Abnahmevorbehalt.

## Fehlerbremse

Keine DIN-Konformität mit anerkannten Regeln der Technik gleichsetzen. Bezugsfertigkeit nicht mit vollständiger Fertigstellung verwechseln. § 650l BGB beim beurkundeten Bauträgervertrag nicht als Widerrufshebel verkaufen. Baugruppen-GbR nicht nach MaBV prüfen. Rücktritt nie empfehlen, ohne Vormerkung, Auflassung und Lastenfreistellung zu sichern.

---

## Skill: `fall-fingerabdruck-und-schnelltriage`

_Fall-Fingerabdruck für Bauträgerakten: extrahiert Urkunde, Verkäufer, Verbraucherrolle, Einheit, Kaufpreis, Raten, Sicherheiten, Baubeschreibung, Teilungserklärung, Technik, Baufortschritt, Abnahme- und Streitstand vor jeder Ampel._

# Fall-Fingerabdruck und Schnelltriage

## Zweck

Dieser Skill verhindert abstrakte Bauträgerkritik. Jede rote, orange oder grüne Bewertung muss aus der konkreten Akte folgen: Urkunde, Einheit, Betrag, Rate, Bauabschnitt, Bauteil, Anlagenstand, E-Mail oder Zahlungsaufforderung.

## Erfassungstabelle

| Feld | Konkret aus der Akte ziehen |
| --- | --- |
| Urkunde | UR-Nr., Notar, Datum, Entwurf/Beurkundung, Bezugsurkunden, Anlagenstand, Verbraucherfrist |
| Verkäufer | Bauträger, Projektgesellschaft, Konzern, Geschäftsführung, Vollmachten, Globalfinanzierer |
| Käufer | Verbraucherstatus, Eigennutzung, Kapitalanlage, Finanzierungsdruck, Makler-/Reservierungsvorgeschichte |
| Grundstück | Grundbuch, Rang, Flurstück, Bauabschnitt, Grundpfandrechte, Baulasten, Erschließung |
| Einheit | Wohnung/Haus, Nummer, Geschoss, Keller, Stellplatz, Sondernutzungsrecht, Wohnfläche, Planstand |
| Preis | Gesamtpreis, Stellplatz, Reservierung, Sonderwünsche, Erschließung, Hausanschlüsse, Preisanpassung |
| Zahlungen | § 3-MaBV-Raten, § 7-Modell, Schlussrate, Bautenstandsmitteilungen, Zahlungsaufforderungen |
| Sicherheiten | Vormerkung, Lastenfreistellung, § 650m-Sicherheit, Bürgschaft, Notaranderkonto, Freigabe |
| Bausoll | Baubeschreibung, Pläne, Prospekt/Rendering, Bemusterung, Technikwerte, Unterlagen nach § 650n BGB |
| WEG | Teilungserklärung, Gemeinschaftsordnung, Kostenkreise, Erstverwalter, Wartungsverträge |
| Streitstand | Vor Notar, Rate, Bauverzug, Mangel, Abnahme, Schlussrate, Insolvenz, Rücktritt/Klage |

## Normenanker

§§ 13, 14, 305c Abs. 2, 306, 307, 308 Nr. 4, 309 Nr. 12, 309 Nr. 15, 311b, 315, 320, 640, 641, 650j, 650k Abs. 2/3, 650m Abs. 2, 650n, 650u, 650v, 883, 925 BGB; §§ 3, 7, 12 MaBV; § 17 BeurkG.

## Triage-Logik

- Vor Beurkundung: Frist, Anlagen, AGB, Raten, Sicherheiten, Bausoll, Änderungsrechte.
- Vor Zahlung: allgemeine und besondere MaBV-Fälligkeit, § 650m, Bautenstand, Besichtigungsrecht.
- Während Bau: Bauzeit, Sonderwünsche, Standardänderungen, technische Nachweise, Stillstand.
- Vor Abnahme: wesentliche Mängel, Protokoll, Gemeinschaftseigentum, Schlussrate, Unterlagen.
- Krise: Vormerkung, § 103/§ 106 InsO, Bürgschaft, Geschäftsführer-/Notar-/Architektenhaftung.

## Ausgabe

Gib zuerst eine Fallkarte aus. Danach folgt die Prüfung. Wenn ein Befund nicht auf Klausel, Betrag, Datum, Bauteil, Rate oder Dokument zurückgeführt werden kann, ist er noch nicht reif.

---

## Skill: `hoai-technik-baugrund-und-objektueberwachung`

_Technischer Realitätscheck im Bauträgerprojekt: HOAI-Leistungsphasen als Prüfraster, Baugrund, Objektüberwachung, anerkannte Regeln der Technik, Schall, Brand, Feuchte, Energie, Tiefgarage, Aufzug und Unterlagen nach § 650n BGB._

# HOAI, Technik, Baugrund und Objektüberwachung

## Prüfgegenstand

Ein juristisch glatter Bauträgervertrag kann technisch unkontrollierbar sein. Dieser Skill prüft Baugrund, Technik, Objektüberwachung, Dokumentation und den Mindeststandard des Werks.

## Normenanker

§ 280 BGB, § 311 Abs. 2 BGB, § 633 Abs. 1 und Abs. 2 BGB, § 634 Nr. 1-4 BGB, § 635 BGB, § 637 BGB, § 640 BGB, § 641 BGB, § 650j BGB, § 650k Abs. 2 und Abs. 3 BGB, § 650n BGB, § 650p BGB, § 650u BGB; Art. 249 EGBGB; § 34 HOAI und Anlage 10.1 HOAI als Prüfraster; Landesbauordnungen und GEG nur nach konkreter Projektlage.

## Prüffelder

- Baugrundgutachten, Grundwasser, Wasserhaltung, Altlasten, Kampfmittel, Entsorgung.
- Abdichtung, Tiefgarage, Hebeanlage, Entwässerung, Lüftung, Aufzug, Brandschutz.
- Ausführungsplanung, Objektüberwachung, Bautagebuch, Mängeltracking, Revisionsunterlagen.
- Schall-, Wärme-, Feuchte- und Brandschutz als Bausoll, nicht nur als öffentlich-rechtliche Mindestbehauptung.
- Käufer-Sachverständiger für Bautenstand, Sonderwünsche, Abnahme und Schlussrate.

## Technikmaßstab

Die HOAI begründet nicht automatisch Käuferansprüche gegen Planer. Sie ist aber ein gutes Raster, um zu prüfen, ob Planung und Überwachung überhaupt nachvollziehbar organisiert sind. Anerkannte Regeln der Technik bleiben eigenständiger Mindeststandard; bloße DIN-Nennung reicht nicht.

## Output

Erstelle eine Technik- und Dokumentenliste: Bauteil, fehlender Nachweis, Risiko, verlangtes Dokument, Zeitpunkt der Herausgabe, Konsequenz für Zahlung oder Abnahme.

---

## Skill: `bauzeit-verzug-vertragsstrafe-und-hoehere-gewalt`

_Bauzeit- und Verzugsprüfung beim Bauträgervertrag: verbindlicher Termin, Bezugsfertigkeit, vollständige Fertigstellung, bauablaufbezogene Darlegung, Pandemie/Lieferketten/Wetter, § 313 BGB, Vertragsstrafe und Schadensersatz._

# Bauzeit, Verzug, Vertragsstrafe und höhere Gewalt

## Prüfgegenstand

Dieser Skill prüft, ob der Bauträger einen echten Fertigstellungstermin schuldet oder ob Frist- und Störungsklauseln den Termin entwerten. Der Fokus liegt auf beweisbarer Bauablaufstörung statt pauschaler Krisenerzählung.

## Normenanker

§§ 271, 280 Abs. 1/2, 286 Abs. 2 Nr. 1 und Abs. 4, 287, 289, 291, 305c Abs. 2, 307, 309 Nr. 5, Nr. 7, Nr. 12, 313, 339-341, 640, 641, 642, 643, 650k Abs. 3, 650u BGB; § 3 Abs. 2 MaBV; §§ 287, 308 ZPO.

## Bauablaufbezogene Darlegung

Der Bauträger muss konkret erklären: Soll-Bauablauf, betroffenes Gewerk, Ereignis, Dauer, Folgegewerke, Ausweichmöglichkeiten, Wiederanlaufzeit und Auswirkung auf den Endtermin. Allgemeine Hinweise auf Pandemie, Lieferketten, Personal, Wetter, Nachunternehmer oder Versorger reichen nicht.

## Klauselprüfung

- „Voraussichtlich“ oder „angestrebt“ entwertet den Termin.
- Zusätzliche Mahnpflichten trotz kalendarischem Termin sind an § 307 BGB zu messen.
- § 313 BGB scheidet regelmäßig aus, wenn die behauptete Krise bei Vertragsschluss schon bekannt war.
- Vertragliche Fristverlängerungen müssen Anlass, Nachweis und Dauer begrenzen.

## Vertragsstrafe und Schaden

Vertragsstrafe und Verzugsschaden bei Interessenidentität anrechnen (§ 341 Abs. 2 i.V.m. § 340 Abs. 2 BGB). Weiteren Schaden nicht durch pauschale Exklusivität abschneiden.

## Output

Erstelle Terminmatrix, Hindernisprüfung, Schadensliste und ein Aufforderungsschreiben, das konkrete Bauablaufdarlegung verlangt.

---

## Skill: `quellenhygiene-rechtsprechungsanker-und-bughunt`

_Quellen- und Bug-Hunt-Skill für Bauträgervertragsprüfungen: verifiziert Normenstand, BGH-/OLG-Rechtsprechung, MaBV, AGB, § 650u/§ 650v BGB, § 650m Abs. 2 BGB, Abnahme, Schlussrate und verhindert BeckRS-/juris-Blindzitate._

# Quellenhygiene, Rechtsprechungsanker und Bug-Hunt

## Zweck

Dieser Skill wird vor jeder harten Ausgabe geladen. Er verhindert Blindzitate, falsche Normanker und typische Bauträgerrechtsfehler.

## Zulässige Quellen

Für Normen: `gesetze-im-internet.de`, Bundesgesetzblatt, Landesrechtportale. Für Rechtsprechung: offizielle Gerichtsseiten, Rechtsprechungsportal des Bundes, Landesrechtsprechungsdatenbanken, `dejure.org` oder `openjur.de`. Keine BeckRS-/juris-/Kommentar-/Aufsatzfundstellen als Beleg verwenden.

## Normenanker für Kontrolllauf

§§ 305-310, 306, 307, 308 Nr. 4, 309 Nr. 1, Nr. 2 lit. a, Nr. 8, Nr. 12, Nr. 15, 311b, 313, 315, 320, 633-641, 634a, 650i, 650j, 650k Abs. 2/3, 650m Abs. 2, 650n, 650u, 650v, 812, 817, 818, 823 Abs. 2, 883, 925 BGB; §§ 3, 7, 12 MaBV; § 17 BeurkG; §§ 103, 106 InsO.

## Bug-Hunt

- DIN-Norm nicht als anerkannte Regel der Technik behandeln.
- Vollständige Fertigstellung nicht mit Bezugsfertigkeit oder bloßer Abnahmereife verwechseln.
- § 650l BGB-Widerruf nicht für beurkundete Bauträgerverträge annehmen.
- § 650m Abs. 1 BGB nicht als Bauträger-Hauptregel nutzen; Abs. 2 bleibt relevant.
- Baugruppen-GbR nicht mit MaBV-Ratenplan prüfen.
- Beweislast-/Empfangsbestätigung mit § 309 Nr. 12 lit. a/b BGB, nicht mit § 309 Nr. 15 BGB begründen.
- Schlussrate trotz offener Außenanlagen/Protokollmängel nicht vorschnell fällig stellen.
- Rücktritt nicht ohne Vormerkungs- und Insolvenzfolgen empfehlen.

## Ausgabe

Am Ende jeder Analyse: geprüfte Normen, verifizierte Entscheidungen, ungeklärte Prüfhinweise, bewusst nicht verwendete Fundstellen.

---

## Skill: `verhandlung-drei-dokumente-paket`

_Drei-Dokumente-Ausgabe für Bauträgervertragsprüfung: Mandantenanschreiben, klauselorientiertes Gutachten und Schreiben an Bauträger/Notar mit MaBV-, AGB-, Abnahme-, Preisanpassungs-, Bausoll- und Sicherheitsforderungen._

# Verhandlung und Drei-Dokumente-Paket

## Prüfgegenstand

Dieser Skill verwandelt die Prüfung in verwendbare Texte. Er ist zu laden, wenn das Ergebnis an Mandant, Bauträger oder Notar gehen soll.

## Normenanker

§§ 133, 157, 242, 305, 306, 307, 308 Nr. 4, 309 Nr. 1, Nr. 2 lit. a, Nr. 12, Nr. 15, 311b, 313, 315, 320, 633, 634, 635, 637, 640, 641, 650j, 650k Abs. 2 und Abs. 3, 650m Abs. 2, 650n, 650u, 650v, 817, 818, 883 BGB; §§ 3, 7, 12 MaBV; § 17 BeurkG; §§ 5, 9a, 10, 20 WEG.

## Dokument 1: Mandantenanschreiben

Schreibe kurz und entscheidungsorientiert: Was ist jetzt zu tun? Beurkunden, warten, zahlen, zurückbehalten, abnehmen, verweigern, Nachweise verlangen oder Klage vorbereiten? Benenne Unterlagen, Fristen, Beträge und rote Punkte. Keine falsche Hoffnung auf 14-Tage-Widerruf beim beurkundeten Bauträgervertrag.

## Dokument 2: Mandantengutachten

Gliedere nach Vertragsabschnitten. Für jeden Befund: Originalwortlaut, Normanker, wirtschaftliche Wirkung, Gegenargument, Antwort, Empfehlung, Neufassung. Baue Spezialthemen ein: Preisanpassung, anerkannte Regeln der Technik, § 650n-Unterlagen, 30-Jahres-Linie bei unwirksamer Abnahme, Schlussrate, Bauablaufdarlegung.

## Dokument 3: Schreiben an Bauträger/Notar

Formuliere höflich-fest. Verlange Streichung oder Korrektur konkreter Klauseln, Nachreichung bestimmter Anlagen, Aussetzung von Zahlung/Beurkundung/Abnahme, Klarstellung der Sicherheit und Freigabe. Bei Notar nicht drohen, sondern Amtspflichten sachlich ansprechen.

## Qualitätsgate

Jede Forderung nennt Klausel, Rate, Betrag, Datum, Einheit, Bauteil oder Dokument. Keine leeren Sätze wie „rechtssicherer formulieren“.

---

## Skill: `eigentumssicherung-vormerkung-lastenfreistellung-und-insolvenz`

_Eigentumssicherung beim Bauträgervertrag: Auflassungsvormerkung, Rang, Lastenfreistellung, Globalgrundschuld, Pfandfreigabe, Finanzierungsvollmacht, § 103/§ 106 InsO, § 7 MaBV und Schutz vor Zahlung ohne Eigentumspfad._

# Eigentumssicherung, Vormerkung, Lastenfreistellung und Insolvenz

## Prüfgegenstand

Dieser Skill verhindert Zahlungen ohne belastbaren Eigentumspfad. Er verbindet Grundbuch, Vormerkung, Lastenfreistellung, MaBV, Finanzierungsvollmacht und Insolvenzrisiko.

## Normenanker

§§ 883, 885, 888, 925, 1113 ff., 1191 ff., 305c Abs. 2, 307, 309 Nr. 2 lit. a, 309 Nr. 12, 320, 321, 323, 346 ff., 650u, 650v BGB; §§ 3, 7, 12 MaBV; §§ 103, 106, 108, 119 InsO; GBO-Nachweislogik.

## Prüffelder

- Ist die Vormerkung für die konkrete Einheit, mit richtigem Rang und ohne gefährliche Freigabevollmacht gesichert?
- Ist die Lastenfreistellung einheitsbezogen, bankseitig verbindlich und kompatibel mit jeder Rate?
- Besteht eine Globalgrundschuld, und ist klar, wann und wie die Einheit pfandfrei wird?
- Erfasst die Freistellungserklärung Grundstück, Wohnungs-/Teileigentum, Miteigentumsanteil, Sondernutzungsrechte, Nebenräume, Stellplatz und künftige Teilflächen eindeutig?
- Sind Freigabebedingungen so formuliert, dass der Käufer nicht mehr oder früher zahlen muss als nach § 3 MaBV und Vertrag wirklich fällig ist?
- Kollidieren Globalbank, Käuferbank und Vormerkung im Rang oder in Vollzugsanweisungen?
- Wird eine Vormerkungslöschung bei einseitig behauptetem Rücktritt/Zahlungsverzug ermöglicht?
- Gibt es Vorinsolvenzzeichen: Baustopp, Nachunternehmerforderungen, nicht abrufbare Bankfreigabe, Ratenbeschleunigung, Sonderwunsch-Vorkasse?

## Freistellung und Bankfreigabe

Eine Freistellungserklärung muss aus Erwerbersicht wie ein technischer Eigentumspfad funktionieren: Zahlung, Bankfreigabe, Lastenlöschung und Umschreibung müssen aufeinander passen. Kritisch sind „Freigabe nur nach vollständiger Kaufpreiszahlung“, Nachschussverlangen bei Kostensteigerung, unklare Bedingungen für den steckengebliebenen Bau und Erklärungen, die Sondernutzungsrechte oder Stellplätze nicht sicher miterfassen.

## Insolvenzlogik

Die Vormerkung schützt den Übereignungsanspruch, nicht alle Zahlungen und nicht automatisch Schadensersatz. Im Insolvenzfall § 106 InsO für den gesicherten Eigentumspfad und § 103 InsO für den Werkleistungsrest getrennt prüfen. Den Insolvenzverwalter zur Wahl auffordern, Bürgschaft/§ 650m-Sicherheit sichern, Mehrkosten der Fertigstellung dokumentieren.

## Ausgabe

Erzeuge eine Eigentumspfad-Tabelle: Zahlung, Sicherung, Grundbuchstand, Bankfreigabe, Insolvenzrisiko, nächste Handlung.

---

## Skill: `verzugsschadenspositionen-berechnung-und-zinsen`

_Berechnet Verzugsschäden beim verspäteten Bauträgerprojekt: Ersatzwohnung, Umzug, Lager, Bereitstellungszinsen, doppelte Miete, Hotel, Nutzungsausfall, Vertragsstrafe, § 287 BGB/ZPO, § 291 BGB, § 289 BGB und § 308 ZPO._

# Verzugsschäden, Berechnung und Zinsen

## Prüfgegenstand

Dieser Skill sammelt und berechnet Schäden aus verspäteter Bezugsfertigkeit oder Übergabe. Er trennt ersatzfähige Mehraufwendungen von Sowieso-Kosten.

## Normenanker

§§ 249 ff., 280 Abs. 1/2, 286, 287, 288, 289, 291, 340, 341, 650u BGB; §§ 287, 308 ZPO; Art. 13 GG und § 903 BGB nur als wertender Wohnungsbezug, nicht als Anspruchsnorm.

## Schadenspositionen

- Ortsübliche Ersatzwohnungsmiete.
- Umzugskosten, auch Rückumzug.
- Lagerkosten für nicht unterbringbares Mobiliar.
- Bereitstellungszinsen auf noch nicht abgerufene Darlehensvaluta; abgrenzen von Zinsen auf bereits ausgezahltes Kapital.
- Doppelte Miete, wenn Altwohnung nicht rechtzeitig beendet werden konnte.
- Hotelkosten für Übergangszeit.
- Nutzungsausfall bei fühlbarer Gebrauchsbeeinträchtigung, strenger Maßstab.

## Vertragsstrafe

Vertragsstrafe und Schaden bei gleichem Interesse anrechnen. Pauschalierter Schaden darf nicht als Ausschluss echten Mehrschadens gelesen werden, wenn AGB-rechtlich angreifbar.

## Output

Erstelle eine Schadensberechnung mit Zeitraum, Beleg, Betrag, Erforderlichkeit, Gegenargument, Antwort und Zinsantrag. Keine Zinsen auf Zinsen beantragen; § 308 ZPO beachten.

---

## Skill: `din-anerkannte-regeln-technik-und-standardwechsel`

_Prüft technische Standards im Bauträgervertrag: DIN-Normen, anerkannte Regeln der Technik, Stand der Technik, Stand von Wissenschaft und Technik, Stichtag Abnahme, Standardwechsel, Sowieso-Kosten und Bedenkenhinweis._

# DIN, anerkannte Regeln der Technik und Standardwechsel

## Prüfgegenstand

Dieser Skill verhindert, dass der Bauträger das Bausoll auf „DIN eingehalten“ verkürzt. DIN-Normen sind wichtige technische Texte, aber keine Rechtsnormen und nicht automatisch der geschuldete Mindeststandard.

## Normenanker

§ 133 BGB, § 157 BGB, § 242 BGB, § 243 BGB, § 305c Abs. 2 BGB, § 307 BGB, § 313 BGB, § 633 Abs. 1 und Abs. 2 BGB, § 634 Nr. 1-4 BGB, § 635 BGB, § 637 BGB, § 640 BGB, § 641 BGB, § 645 BGB, § 650j BGB, § 650k Abs. 2 und Abs. 3 BGB, § 650n BGB, § 650u BGB; § 13 Abs. 1 VOB/B nur bei wirksamer Einbeziehung.

## Drei Stufen

- Anerkannte Regeln der Technik: wissenschaftlich anerkannt und in der Praxis bewährt; werkvertraglicher Mindeststandard.
- Stand der Technik: fortschrittlicher, nicht zwingend praktisch bewährt; im Zivilrecht nur bei Vereinbarung oder besonderer Lage.
- Stand von Wissenschaft und Technik: Spitzenmaßstab für Hochrisiken, nicht Normalstandard im Wohnungsbau.

## Stichtag und Standardwechsel

Maßgeblich ist grundsätzlich die Abnahme. Ändert sich der Standard zwischen Vertragsschluss und Abnahme, braucht es Aufklärung und eine bewusste Entscheidung des Erwerbers. Bei Mängelbeseitigung nach Abnahme ist der Standard zum Zeitpunkt der Beseitigung relevant; Mehrkosten und Mehrwert sauber prüfen.

## Senatsdifferenzierung

Werkvertragsrechtlich keine pauschale Vermutung, dass DIN die anerkannten Regeln der Technik wiedergibt. WEG-Binnenmaßstäbe, etwa beim Schallschutz, nicht ungeprüft auf Bauträger-Bausoll übertragen.

## Output

Erstelle eine Technikstandard-Tabelle: Bauteil, DIN/Regel, Mindeststandard, Abweichung, Aufklärung, Mehrkosten, verlangter Nachweis.

---

## Skill: `notarhaftung-belehrung-und-streitverkuendung`

_Prüft notarielle Amtspflichten im Bauträgervertrag: § 17 BeurkG, § 14 BNotO, § 19 BNotO, MaBV-/AGB-Klauselkontrolle, Preisanpassung, § 650m-Sicherheit, Niedrig-Grundstücksanteil, Bezugsurkunden und Streitverkündung._

# Notarhaftung, Belehrung und Streitverkündung

## Prüfgegenstand

Dieser Skill prüft nicht vorschnell „Notar haftet“, sondern legt die konkrete Amtspflichtspur frei: Was musste der Notar erkennen, erläutern oder anders gestalten?

## Normenanker

§ 17 Abs. 1 und Abs. 2a BeurkG; § 13a BeurkG; §§ 14, 19 BNotO; §§ 305-310, 307, 309 Nr. 12, Nr. 15, 311b, 650m Abs. 2, 650u, 650v BGB; §§ 3, 7, 12 MaBV.

## Prüffelder

- Verbraucherfrist und vollständiger Entwurf einschließlich Bezugsurkunden.
- Erkennbare MaBV-Abweichung im Ratenplan.
- Intransparente § 650m-Sicherheit oder Verzichtsklausel.
- Preisanpassung mit erheblichem wirtschaftlichem Risiko.
- Kritische Vormerkungslöschungs-, Freigabe- oder Belastungsvollmacht.
- Auffällig niedriger Grundstücksanteil bei hoher erster Rate.
- Auslagerung wesentlicher Vertragsbedingungen in Anlagen, die der Verbraucher praktisch nicht erhält.

## Haftungsspur

§ 19 BNotO subsidiär bei Fahrlässigkeit, bei Vorsatz direkter. Vorsatz bedeutet nicht Schadenswille; es genügt das bewusste Hinwegsetzen über erkannte Amtspflichten. Vor gerichtlicher Geltendmachung immer anderweitige Ersatzmöglichkeiten und Streitverkündung prüfen.

## Output

Erzeuge eine Notarspur: Pflicht, Tatsachenkenntnis, Verstoß, Kausalität, Schaden, Subsidiarität, Prozessstrategie.

---

## Skill: `wohnungseigentum-teilungserklaerung-und-erstverwalter`

_WEG- und Teilungserklärungsprüfung beim Bauträgerprojekt: Sondereigentum, Gemeinschaftseigentum, Sondernutzungsrechte, Untergemeinschaften, Kostenverteilung, Erstverwalter, Wartungsverträge und Änderungsvollmachten._

# Wohnungseigentum, Teilungserklärung und Erstverwalter

## Prüfgegenstand

Der Käufer erwirbt nicht nur Räume, sondern eine Mitgliedschaft in einer GdWE. Dieser Skill prüft Teilungserklärung, Gemeinschaftsordnung, Erstverwalter und gebundene Folgegeschäfte.

## Normenanker

§ 305 BGB, § 307 BGB, § 308 Nr. 4 BGB, § 311b Abs. 1 BGB, § 650u BGB; § 3 MaBV; § 1 WEG, § 3 WEG, § 5 WEG, § 8 WEG, § 9a WEG, § 10 WEG, § 16 WEG, § 18 WEG, § 19 WEG, § 20 WEG, § 23 WEG, § 24 WEG, § 26 WEG, § 27 WEG, § 44 WEG.

## Prüfmatrix

- Stimmen Aufteilungsplan, Abgeschlossenheitsbescheinigung, Teilungserklärung und Kaufgegenstand überein?
- Sind Keller, Stellplatz, Terrasse, Balkon und Sondernutzungsrechte exakt zugeordnet?
- Gibt es Untergemeinschaften, Kostenkreise oder Stimmrechtsregeln zulasten bestimmter Häuser/Bauabschnitte?
- Darf der Bauträger Teilungserklärung oder Gemeinschaftsordnung später aus bloßer Zweckmäßigkeit ändern?
- Ist der Erstverwalter bauträgernah und mit langen Wartungs-, Wärme-, Messdienst- oder Energielieferverträgen verbunden?
- Werden Aufzug, Tiefgarage, Lüftung, Hebeanlagen, Ladeinfrastruktur und Außenanlagen wirtschaftlich transparent verteilt?

## Rechtsprechungsanker

BGH V ZR 91/25 nur nach Live-Prüfung einsetzen: Zustimmungspflichten zu Änderungen müssen auf einzeln benannte triftige Gründe begrenzt sein; § 242 BGB rettet eine unwirksame AGB-Änderungsklausel regelmäßig nicht.

## Output

Erstelle eine WEG-Risikokarte: Regelung, betroffene Einheit, wirtschaftliche Wirkung, Normanker, Änderungsverlangen, Priorität.

---

## Skill: `geschaeftsfuehrer-architekt-und-bautenstandshaftung`

_Prüft Drittansprüche bei Bauträgerprojekten: Geschäftsführerhaftung nach § 823 Abs. 2 BGB i.V.m. § 3/§ 7 MaBV, § 263 StGB, unrichtige Bautenstandsbestätigung, Architekt/Bauleiter, Schutzwirkung zugunsten Erwerber._

# Geschäftsführer-, Architekten- und Bautenstandshaftung

## Prüfgegenstand

Dieser Skill schaut hinter die Projektgesellschaft, wenn Zahlungen vorzeitig verlangt oder Bautenstände falsch bestätigt werden. Er prüft persönliche und drittbezogene Haftung, ohne sie vorschnell zu behaupten.

## Normenanker

§§ 823 Abs. 2, 826, 249 ff., 280, 311 Abs. 3 BGB; §§ 3, 7, 12 MaBV; § 263 StGB; § 253 StGB nur bei Drucksituationen; Grundsätze des Vertrags mit Schutzwirkung zugunsten Dritter.

## Geschäftsführer

§ 3 und § 7 MaBV können Schutzgesetze zugunsten des Erwerbers sein. Prüfe operatives Handeln, Kenntnis vom Bau- und Zahlungsstand, bedingten Vorsatz, Ratenanforderung, Vermögensgefährdung und Kausalität. Nicht automatisch jeden Geschäftsführer haftbar machen; Aktenanker nötig.

## Architekt/Bauleiter

Unrichtige Bautenstandsbestätigungen können Erwerberzahlungen auslösen. Prüfe Auftrag, Nähe zum Erwerber, erkennbaren Verwendungszweck der Bescheinigung, Vertrauenstatbestand, Pflichtverletzung und Schaden.

## Drucksituationen

„Schlüssel nur gegen Zahlung“ trotz offener Mängel oder fehlender Fälligkeit kann über Vertragsrecht hinaus relevant werden. Strafrechtliche Bewertung nur zurückhaltend und fallgenau.

## Output

Erstelle eine Anspruchsgegner-Matrix: Person, Handlung, Norm, Vorsatz/Fahrlässigkeit, Beweis, Schaden, taktische Verwendung im Vergleich oder Prozess.

---

## Skill: `abnahme-gemeinschaftseigentum-schlussrate-und-maengelrechte`

_Abnahmeprüfung im Bauträgervertrag: Sondereigentum, Gemeinschaftseigentum, Vertreter-/Sachverständigenabnahme, Erstverwalter, § 640 BGB, § 634a BGB, § 3 Abs. 2 MaBV, Schlussrate, Verjährungsbeginn und Nachzügler._

# Abnahme, Gemeinschaftseigentum, Schlussrate und Mängelrechte

## Prüfgegenstand

Die Abnahme entscheidet über Fälligkeit, Beweislast, Gefahr, Mängelrechte und Verjährung. Im Bauträgervertrag muss Sondereigentum, Gemeinschaftseigentum und Schlussrate getrennt geprüft werden.

## Normenanker

§§ 633, 634, 634a Abs. 1 Nr. 2 und Abs. 2, 635, 637, 640, 641, 650u BGB; § 3 Abs. 2 MaBV; §§ 305c Abs. 2, 307, 309 Nr. 8, Nr. 12 BGB; § 9a WEG für Mängelrechte der Gemeinschaft.

## Gemeinschaftseigentum

Rot prüfen, wenn die Urkunde:

- die Abnahme zwingend auf Erwerbervertreter, Erstverwalter, Tochtergesellschaft, Projektsteuerer oder bauträgernahen Sachverständigen verlagert,
- jedem einzelnen Erwerber das eigene Prüf- und Abnahmerecht nimmt,
- Nachzügler an eine frühere fremde Abnahme bindet,
- Besitzübergabe, Zahlung oder Protokoll als automatische Abnahme fingiert.

BGH VII ZR 68/24 und VII ZR 108/24 nur mit frei prüfbarer Quelle verwenden. Kern: unwirksame Abnahmeklauseln können den Beginn der fünfjährigen Bauwerksverjährung verhindern; die 30-Jahres-Grenze ist als äußerer Rechtssicherheitsrahmen zu beachten.

## Schlussrate

Schlussrate nicht mit Abnahmereife gleichsetzen. Bei Vertragsklausel „vollständige Fertigstellung“ können Protokollmängel, Restarbeiten, Außenanlagen, Gemeinschaftseigentum und Dokumentationspflichten die Fälligkeit sperren. BGH VII ZR 88/25 nur nach Live-Verifikation einsetzen.

## Ausgabe

Erstelle ein Abnahmeprotokoll mit nicht abnahmefähigen Punkten, Vorbehalten, verweigerter Abnahme bei wesentlichen Mängeln, zurückzuhaltenden Beträgen, Nachweisliste und Textbaustein gegen unbeabsichtigte Abnahme.

---

## Skill: `sonderwuensche-preisanpassung-und-ausstattungswahl`

_Sonderwünsche und Bemusterung im Bauträgervertrag: prüft Form, MaBV-Einordnung, Vorauszahlung, Ausstattungswahl, Mehr-/Minderpreise, Lieferbarkeit, Fristversäumnis, Bauzeitfolgen und Änderung des Sondereigentums._

# Sonderwünsche, Bemusterung und Ausstattungswahl

## Prüfgegenstand

Sonderwünsche sind im Bauträgervertrag ein eigener Risikobereich: Sie können Formprobleme, MaBV-Umgehung, Bauzeitverzug, technische Schnittstellen und Streit über Mehr-/Minderpreise auslösen.

## Normenanker

§ 125 BGB, § 133 BGB, § 157 BGB, § 305c Abs. 2 BGB, § 307 BGB, § 308 Nr. 4 BGB, § 309 Nr. 1 BGB, § 309 Nr. 12 BGB, § 311b Abs. 1 BGB, § 315 BGB, § 631 BGB, § 633 BGB, § 640 BGB, § 641 BGB, § 650j BGB, § 650k Abs. 2 und Abs. 3 BGB, § 650n BGB, § 650u BGB, § 650v BGB; § 3 MaBV, § 7 MaBV, § 12 MaBV; § 5 WEG, § 10 WEG, § 20 WEG bei Änderung von Sonder-/Gemeinschaftseigentum.

## Form und MaBV

Sonderwünsche vor Beurkundung gehören in die Urkunde, wenn sie Vertragsgegenstand sein sollen. Nach Beurkundung sind sie nur formfrei, soweit sie nicht selbst § 311b BGB berühren, etwa bei Änderung von Sondereigentumsumfang oder Teilungserklärung. Zahlungen dürfen nicht außerhalb des MaBV-Ratenplans vorgeschoben werden; regelmäßig gehören sie in den Gesamtpreis oder allenfalls in die Schlussratenlogik.

## Prüfung

- Vorauszahlung vor Leistung oder vor Bautenstand?
- Mehr-/Minderpreise transparent?
- Ausstattungswahl bei Fristversäumnis durch Bauträger einseitig?
- Bauzeitfolge nur konkret oder pauschal?
- Lieferbarkeitsrisiko und gleichwertiger Ersatz messbar?
- Auswirkungen auf Schall, Brand, Statik, Gewährleistung, Wartung und WEG geklärt?

## Output

Erstelle eine Sonderwunschliste mit Leistung, Mehr-/Minderpreis, Zahlungszeitpunkt, Formrisiko, MaBV-Risiko, Bauzeitfolge und Änderungsvorschlag.

---

## Skill: `unwirksame-abnahmeklauseln-dreissig-jahre-und-nachholung`

_Prüft unwirksame Abnahmeklauseln im Bauträgervertrag: Erstverwalter, Sachverständige, Erwerbervertreter, Nachzügler, § 640 BGB, § 634a BGB, personale Teilunwirksamkeit, 30-Jahres-Grenze und nachträgliche Abnahme._

# Unwirksame Abnahmeklauseln, 30-Jahres-Grenze und Nachholung

## Prüfgegenstand

Dieser Skill behandelt Altanlagen und Verträge mit fehlerhafter Abnahmeregelung. Er trennt unwirksame AGB-Abnahme, vergessene Abnahme und berechtigte Abnahmeverweigerung.

## Normenanker

§§ 195, 199, 203, 204, 242, 305, 307, 309 Nr. 8 lit. b, 633, 634 Nr. 1-4, 634a Abs. 1 Nr. 2 und Abs. 2, 635, 637, 640, 641 BGB; § 9a WEG; §§ 485, 494a ZPO; BGH VII ZR 68/24 und VII ZR 108/24 nur nach Live-Verifikation.

## Prüfung

- Abnahme durch Erstverwalter, Tochtergesellschaft, Projektsteuerer, Bauträgersachverständigen oder verpflichtende Vertreter?
- Eigenes Prüf- und Abnahmerecht jedes Erwerbers ausdrücklich erhalten?
- Nachzügler an frühere Abnahme gebunden?
- Erwerber ging von wirksamer Dritt-Abnahme aus, sodass konkludente Abnahme durch Nutzung/Zahlung ausscheidet?

## Rechtsfolge

Der Bauträger kann sich nicht beliebig auf die Unwirksamkeit seiner eigenen Klausel berufen, wenn dies dem Erwerber schaden würde. Die fünfjährige Bauwerksverjährung läuft ohne wirksame Abnahme nicht an. Als äußerer Rahmen ist eine 30-Jahres-Grenze aus Rechtssicherheit zu prüfen.

## Nachholung

Bei nachträglicher Abnahme nicht den Neuzustand von damals verlangen, sondern ergänzende Vertragsauslegung: bestimmungsgemäße Nutzung und altersbedingter Verschleiß werden berücksichtigt. Bei berechtigter Abnahmeverweigerung kann die Lage anders sein; parallel nachträgliche Abnahme zur Verjährungssicherung erwägen.

## GdWE und Regress

Nachträgliche Abnahme und Mängelverfolgung dürfen nicht nur aus Sicht eines einzelnen Erwerbers gedacht werden. Prüfe, ob die Gemeinschaft der Wohnungseigentümer Rechte am Gemeinschaftseigentum ausübt, ob Beschlüsse zur Anspruchsdurchsetzung fehlen, ob Nachunternehmerregresse des Bauträgers/Generalunternehmers zeitlich wegbrechen und ob eine Streitverkündung an Planer, Unternehmer oder Notar sinnvoll ist.

## Output

Erstelle eine Verjährungs- und Abnahmespur: Klausel, Abnahmeakt, Wirksamkeit, Verjährungsbeginn, Ansprüche, nächster Schritt.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

