#!/usr/bin/env python3
"""Themenprofile fuer Werkstatt- und Schnellstart-Prompts.

Jedes Profil liefert die fachliche Substanz, mit der ein Plugin auch ohne
direkten Skill-Zugriff bearbeitet werden kann: kuratierte Pflichtnormen,
verifizierte Leitentscheidungen (BGH, BVerfG, BAG, BSG, BFH, BVerwG, EuGH)
mit Aktenzeichen, Datum, frei zugaenglicher Fundstelle und Kernsatz,
fachliche Workflow-Stationen und themenspezifische Stop-Kriterien.

Slug-relevante und validatorrelevante Strings (Aktenzeichen, kurze IDs)
verwenden ASCII; die Kernsaetze, Stationen und Pflichtnormen verwenden
echte Umlaute. Paragrafenzeichen werden ausgeschrieben (Paragraf / Artikel),
spitze Klammern sind verboten, doppeltes Anfuehren als Apostroph gesetzt.

Die Profile sind bewusst breit angelegt; die Klassifikation faellt im
Zweifel auf 'default' zurueck.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Iterable


@dataclass(frozen=True)
class Leitentscheidung:
    """Verifizierter Rechtsprechungsanker mit Kernsatz."""

    gericht: str  # z. B. "BGH", "BVerfG", "BAG", "EuGH"
    aktenzeichen: str  # ASCII, ohne Paragrafenzeichen
    datum: str  # Format TT.MM.JJJJ
    fundstelle: str  # frei zugaengliche Fundstelle ohne URL
    kernsatz: str  # tatsaechlicher Leitsatz oder Kernsatz in eigener Worten

    def line(self) -> str:
        return (
            f"{self.gericht} {self.aktenzeichen}, Urteil/Beschluss vom {self.datum} "
            f"({self.fundstelle}): {self.kernsatz}"
        )


@dataclass(frozen=True)
class WorkflowStation:
    """Eine inhaltliche Station des Werkstatt-Workflows."""

    title: str
    eingang: str  # Was wird inventarisiert
    pruefung: str  # Was wird fachlich geprueft
    arbeitsprodukt: str  # Welches Teilprodukt entsteht


@dataclass(frozen=True)
class Themenprofil:
    """Kuratierte Fachsubstanz pro Rechtsgebiet."""

    key: str
    label: str
    rolle: str
    stop_kriterien: tuple[str, ...]
    stationen: tuple[WorkflowStation, ...]
    pflichtnormen: tuple[str, ...]
    leitentscheidungen: tuple[Leitentscheidung, ...]
    pruefraster: tuple[str, ...] = field(default_factory=tuple)
    skelette: tuple[str, ...] = field(default_factory=tuple)


# Registry, wird durch register_*-Module gefuellt.
PROFILE: dict[str, Themenprofil] = {}


def register(profil: Themenprofil) -> None:
    PROFILE[profil.key] = profil


def get(key: str) -> Themenprofil:
    return PROFILE.get(key) or PROFILE["default"]


# ---------------------------------------------------------------------------
# Klassifikation: Plugin-Name + Titel + Beschreibung -> Topic-Key
# ---------------------------------------------------------------------------


_CLASSIFY_RULES: list[tuple[str, str]] = [
    # Reihenfolge ist wichtig: spezifisch zuerst.
    (r"(staatsanwaltschaft|amtsanwaltschaft|aktenaufbereiter-strafrecht|strafanzeige|strafbefehl|strafzumessung|betaeubungsmittel|bnd-kriminal)", "strafrecht"),
    (r"(fachanwalt-strafrecht|verkehrsowi-verteidiger|ordnungswidrigkeit)", "strafrecht"),
    (r"(relationstechnik-zivilrecht|richter-amtsgericht-zivil|richter-landgericht-zivilkammer|richter-oberlandesgericht-zivilsenat|richter-bundesgerichtshof-zivilsenat|zivilrichter|urteilsbauer-relationsmacher)", "zivilprozess"),
    (r"(richter-amtsgericht-strafrichter|richter-landgericht-strafkammer|richter-oberlandesgericht-strafsenat|richter-bundesgerichtshof-strafsenat)", "strafrecht-gericht"),
    (r"(richter-arbeitsgericht|richter-landesarbeitsgericht|richter-bundesarbeitsgericht)", "arbeitsrecht-gericht"),
    (r"(richter-sozialgericht|richter-landessozialgericht|richter-bundessozialgericht|selbstvertreter-sozialgericht)", "sozialrecht-gericht"),
    (r"(richter-finanzgericht|richter-bundesfinanzhof)", "steuerprozess"),
    (r"(richter-verwaltungsgericht|richter-oberverwaltungsgericht|richter-bundesverwaltungsgericht|richter-oberverwaltungsgericht-verwaltungsgerichtshof)", "verwaltungsprozess"),
    (r"(richter-familiengericht|richter-bundesgerichtshof-familiensenat)", "familienrecht"),
    (r"(richter-bundesverfassungsgericht|bverfg)", "verfassungsprozess"),
    (r"(fachanwalt-familienrecht|familienrecht|betreuungsrecht|kindschaft|unterhalt|scheidung|versorgungsausgleich)", "familienrecht"),
    (r"(fachanwalt-miet|mietrecht|miet-wohnungseigentum|nachbarschaft|weg-hausverwaltung|erbbaurecht|immobilien)", "mietrecht-weg"),
    (r"(fachanwalt-arbeitsrecht|arbeitsrecht|arbeitszeugnis|startup-hr|bav-strategie|sozialversicherungsstatus)", "arbeitsrecht"),
    (r"(fachanwalt-sozialrecht|krankenkassen|rentenpruefer|sozialgericht|kriegsdienstverweigerung)", "sozialrecht"),
    (r"(fachanwalt-steuerrecht|steuerrecht-anwalt|forschungszulage|berufsrecht-steuerberater|berufsrecht-wirtschaftspruefer)", "steuerrecht"),
    (r"(fachanwalt-verwaltungsrecht|fachanwalt-migrationsrecht|fachanwalt-medizinrecht|kommunalrecht|hochschulrecht|schulrecht|beamtenrecht|umweltrecht|denkmalschutz|baurecht|bautraeger|hoai|bundesnetzagentur|telekommunikation|energierecht|strassenrecht|strassenverkehrsrecht|bundeswehrrecht|aussenwirtschaft|festlandchina|informationsfreiheit|krankenhausrecht|apothekenrecht|tierschutz|verkehr-infrastruktur|luftrecht|seerecht|weltraumrecht|hochschule)", "verwaltungsrecht"),
    (r"(verfassungsrecht|grundrecht|bverfgg|verhaeltnismaess|wahlkampf|parteienrecht|versammlungsrecht|verfassung)", "verfassungsrecht"),
    (r"(fachanwalt-insolvenz|insolvenzrecht|insolvenzverwaltung|insolvenzplan|krisenfrueherkennung|fortbestehensprognose|insolvenzforderung|verbraucherinsolvenz|us-bankruptcy)", "insolvenz"),
    (r"(fachanwalt-handels|fachanwalt-bank|fachanwalt-internationales-wirtschafts|gesellschaftsrecht|gesellschaftsgruender|gesellschaftsrechtliche-treuepflicht|aktienrecht|aufsichtsrat|grosskanzlei|mittelstand|venture-capital|private-equity|wandeldarlehen|insiderrecht|corporate-kanzlei|handelsregister|handelsrecht-hgb|geldwaesche|hinweisgeber|internal-investigations|aussenwirtschaft-zoll|bank-rechtsabteilung|berichtspflichten|haushaltsrecht|lobbyregister|normenkontrollrat|factoring|leasing|franchise|handelsvertreter|gesellschaftsrecht-legal-english|gmbh|aktien|kanzlei-management|kanzlei-mandant|kanzlei-allgemein|berufsrecht-anwaelte|berufsrecht-notare|berufsrecht-patentanwaelte|berufsgerichtliche|kanzlei-builder|notariat|email-umformulierer|mandantenanfragen|nda-abgleich|nda-verschwiegenheit|memorandum|berufsrecht-ki)", "gesellschaftsrecht-corporate"),
    (r"(datenschutzrecht|datenschutz-sanktionsverfahren|ki-vo-ai-act|ki-governance|ki-richtlinie|nis2|hinweisgeberschutz|phishing|dsa-dma|datenbankrecht|robotik|barrierefreiheit-web)", "datenschutz-ki"),
    (r"(fachanwalt-vergaberecht|vergaberecht|oeffentliches-wirtschaftsrecht|kartellrecht-marktabgrenzung)", "vergaberecht-kartell"),
    (r"(fachanwalt-urheber|urheberrecht|verlagsrecht|verlagsredaktion|us-copyright|fashion-law|markenrecht|gewerblicher-rechtsschutz|fachanwalt-gewerblicher|patentrecherche|patentrecht|gebrauchsmuster|designrecht|influencer)", "urheber-marke"),
    (r"(fachanwalt-versicherungsrecht|versicherungsrecht|fluggast|fahrgastrechte|fachanwalt-transport|fachanwalt-verkehrsrecht|seerecht-schifffahrt|verkehrsowi|strassenverkehrsrecht-stvo|luftrecht-flughafen)", "versicherung-transport"),
    (r"(fachanwalt-it-recht|softwarerecht|softwarerecht-de-eu-us|ecommerce-recht|telekommunikationsrecht|robotik-recht|word-legal-ai-plugin|verwaltete-agentenrezepte)", "it-software"),
    (r"(handelsregister-praxis|grundbuchamt-praxis|notariat-alltag|registerrecht|register|vereinsrecht|parteiorganisation)", "register"),
    (r"(bauplanung|normenkontrolle-bauleitplanung|denkmalschutz|umweltschutzverband|umweltrecht|umweltschutz)", "bauplanung-umwelt"),
    (r"(verbraucherschutz|verbraucherrechtsstaat|verbraucher-rechtsstaat|verbraucherinsolvenz-schuldenbereinigung|rechtsberatungsstelle|nachbarschaftsstreit|fluggast|fahrgastrechte|forderungsmanagement-klagewerkstatt|zwangsvollstreckung|zwangsverwaltung-zvg|verkehr-infrastrukturrecht|selbstvertreter-amtsgericht|email-umformulierer|verbraucher-aspekte)", "verbraucher-praxis"),
    (r"(bgb-at-pruefer|bgb-bt-pruefer|vertragsausfueller|vertragsrecht|agb-recht-pruefer|bereicherungs-und-anfechtungsrecht|nachbarschaftsstreit|schriftform-und-textform|bereicherungs|bereicherung|methodenlehre|subsumtion|subsumtions|relation|urteilsbauer|verhaeltnismaessigkeit|prozessrecht|aktenauszug-gerichtsverfahren|forderungsmanagement|zwangsvollstreckung|zwangsverwaltung|jveg-kostenpruefer|kostenpruefer|aktenaufbereiter)", "zivilrecht-allgemein"),
    (r"(commercial-courts|fachanwalt-handels-gesellschaftsrecht|internationales-handelsrecht|festlandchina-wirtschaftsverkehr|common-law-kompass|europarecht-kompass)", "internationales-handelsrecht"),
    (r"(legistik-werkstatt|normenkontrollrat-nkr|haushaltsrecht-bho|gesetzgebung|hochschulrecht|berufsrecht-ki-vertragspruefung)", "legistik"),
    (r"(rechtstheorie-rechtsphilosophie|jurastudium|hausarbeitenmacher|methodenlehre|einfache-leichte-sprache|juristische-sprache-deutsch-als-zweitsprache|deutsche-rechtsgeschichte|preussisches-allgemeines-landrecht|roemisches-recht|roemisch-katholisches-kirchenrecht|zitierweise|references|prompts|plugin-gruppen|hochschulrecht-laender|pruefungsrecht-hochschule|uebersicht-fachanwaltschaften|fachanwalt-uebersicht|deutsche-rechtsgeschichte)", "wissenschaft-lehre"),
    (r"(meinungspruefer|tabellenreview-3d|status-navigator-step-plan|recherche|liquiditaetsplanung|kanzlei-builder-hub|kanzlei-management|kanzlei-mandant-lifecycle|berichtspflichten-erlediger|buerokratieversteher-entbuerokratisierer|dfg-foerderantrag|memorandums-ersteller|anlagen-zu-schriftsaetzen|prozessrecht|aktenauszug-gerichtsverfahren|forderungsmanagement-klagewerkstatt|jveg-kostenpruefer)", "praxis-werkzeug"),
    (r"(audit|audits|tests|test|anthropic-lessons|references|prompts|testakten|0_setup|skills-index|plugins$|plugin-gruppen)", "praxis-werkzeug"),
    (r"(fachanwalt-bau|fachanwalt-medizinrecht|fachanwalt-agrarrecht|fachanwalt-sportrecht|fachanwalt-transport|fachanwalt-internationales-wirtschaftsrecht|goae-gebuehrenordnung|produktrecht|regulatorisches-recht|solo-selbststaendige|lizenzvertrag|einigungsvertrag-vermoegensrecht|schoeffen-handelsrichter|fachanwalt-erbrecht|fachanwaltschafts)", "spezialrecht"),
]


def classify(plugin_name: str, title: str = "", description: str = "") -> str:
    """Liefert den Topic-Key fuer ein Plugin.

    Klassifiziert anhand des Plugin-Slugs und faellt auf 'default' zurueck.
    """
    blob = f"{plugin_name} {title} {description}".lower()
    for pattern, key in _CLASSIFY_RULES:
        if re.search(pattern, blob):
            return key
    return "default"


# ---------------------------------------------------------------------------
# Profile werden weiter unten registriert. Aufteilung in mehrere Blocks aus
# Lesbarkeitsgruenden.
# ---------------------------------------------------------------------------


def _register_default() -> None:
    register(Themenprofil(
        key="default",
        label="Allgemein juristisches Arbeiten",
        rolle="Du arbeitest in einem juristischen Werkstatt-Modus: Sachverhalt wird strukturiert, Normen und Rechtsprechung werden verifiziert, ein ausformuliertes Arbeitsprodukt mit Lagebild, Pruefung, Empfehlung und Anschlussentscheidung entsteht.",
        stop_kriterien=(
            "Notfrist im Raum (Klage-, Berufungs-, Beschwerde-, Antrags- oder Einspruchsfrist).",
            "Identitaet, Vertretung oder Vollmacht unklar.",
            "Straf- oder Haftungsrisiko, Interessenkollision oder Verbot der Beratung.",
            "Echtdaten oder Mandatsbezug in ungesichertem System.",
            "Quelle oder Rechtsprechungszitat nicht live verifizierbar.",
        ),
        stationen=(
            WorkflowStation(
                title="Akten- und Auftragsaufnahme",
                eingang="Akte, Schriftverkehr, Vertraege, Bescheide, Urteile, Anlagen, Fristen, Beteiligte, Beweismittel.",
                pruefung="Rolle, Ziel, Frist, Verfahrensstand, Zustaendigkeit und Anwaltszwang feststellen; Lebenssachverhalt von Behauptung trennen.",
                arbeitsprodukt="Aktenuebersicht mit Beteiligten, Fristen, Streitpunkten und Belegliste.",
            ),
            WorkflowStation(
                title="Normgrundlage und Subsumtion",
                eingang="Anspruchs- oder Verteidigungsziel, Tatbestandsmerkmale, Lebenssachverhalt, Beweisangebot.",
                pruefung="Vier-Schritt-Subsumtion: Obersatz, Definition aus Gesetz und herrschender Meinung, Untersatz aus Sachverhalt, Ergebnis pro Tatbestandsmerkmal; Beweis- und Darlegungslast trennen.",
                arbeitsprodukt="Anspruchs- oder Pruefraster mit Tatbestandsmerkmalen, Belegen und Zwischenergebnissen.",
            ),
            WorkflowStation(
                title="Rechtsprechung und Literatur",
                eingang="Leitentscheidungen, Kommentar- und Aufsatzfundstellen, Datenbank-Recherche, abweichende Stimmen.",
                pruefung="Aktenzeichen, Datum, Gericht, Fundstelle und Kernsatz vor Uebernahme verifizieren; Geltung im Bezirk, Senatszustaendigkeit und neuere Entscheidung pruefen.",
                arbeitsprodukt="Rechtsprechungsmatrix mit Aktenzeichen, Kernsatz und Anwendung auf den Fall.",
            ),
            WorkflowStation(
                title="Gegenpruefung und Risikobild",
                eingang="Einwendungen, Verjaehrung, Verwirkung, Beweislast, prozessuale Hindernisse, alternative Anspruchsgrundlagen.",
                pruefung="Erst Einwendungen, dann Einreden; Verjaehrung Paragrafen 195, 199, 214 BGB; Wirtschaftlichkeit und Vergleichschance bewerten.",
                arbeitsprodukt="Risikobogen mit Eintrittswahrscheinlichkeit, Schaden, Vergleichsraum und Stop-Trigger.",
            ),
            WorkflowStation(
                title="Arbeitsprodukt und Anschluss",
                eingang="Zielprodukt (Memo, Antrag, Vertragsentwurf, Schriftsatz, Vermerk, Tenor, Mandatsantwort) und Adressat.",
                pruefung="Ausformulieren in dezimaler Gliederung, mit Belegstellen, Normen und Rechtsprechung; Pflichtangaben je nach Form pruefen.",
                arbeitsprodukt="Vollstaendiges Dokument oder Schriftsatzkern mit Anschlusspflichten, Fristen und Sicherheitshinweisen.",
            ),
        ),
        pflichtnormen=(
            "Paragrafen 133, 157 BGB (Auslegung)",
            "Paragraf 242 BGB (Treu und Glauben)",
            "Paragrafen 195, 199, 214 BGB (Verjaehrung)",
            "Paragraf 280 BGB (Pflichtverletzung)",
            "Paragraf 286 ZPO (freie Beweiswuerdigung)",
            "Paragraf 138 ZPO (Wahrheitspflicht)",
            "Paragraf 253 Absatz 2 ZPO (Klage)",
            "Paragrafen 91, 92 ZPO (Kostenentscheidung)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "BGH", "VIII ZR 270/19", "29.04.2020", "BGHZ 225, 297",
                "Schadensersatz wegen Pflichtverletzung setzt die Pflichtverletzung, einen kausal verursachten Schaden und Vertretenmuessen voraus; ein Verschulden wird nach Paragraf 280 Absatz 1 Satz 2 BGB vermutet.",
            ),
            Leitentscheidung(
                "BGH", "III ZR 35/00", "17.05.2001", "NJW 2001, 2535",
                "Eine Pflicht zur Aufklaerung besteht, soweit nach Treu und Glauben der Vertragspartner mit redlicher Information rechnen darf; das Unterlassen aufklaerender Hinweise begruendet eine Schadensersatzpflicht aus culpa in contrahendo.",
            ),
            Leitentscheidung(
                "BVerfG", "1 BvR 16/13", "06.11.2019", "BVerfGE 152, 152 (Recht auf Vergessen I)",
                "Auch im fachgerichtlichen Verfahren ist eine umfassende Grundrechtsabwaegung vorzunehmen; das allgemeine Persoenlichkeitsrecht muss bei Veroeffentlichungen mit Zeitablauf zunehmend Gewicht erhalten.",
            ),
        ),
        pruefraster=(
            "Wer will was von wem woraus? Anspruchsgrundlage, Tatbestandsmerkmale, Rechtsfolge.",
            "Was ist unstreitig, was bestritten, was nur behauptet, was bewiesen?",
            "Welche Einwendungen, Einreden und Gegenrechte sind im Raum?",
            "Welche Fristen, Zuestaendigkeiten und Formvorgaben gelten?",
            "Welches Arbeitsprodukt ist gefragt, und welche Pflichtangaben braucht es?",
        ),
        skelette=(
            "Lagebild: Wer will was von wem? Welcher Verfahrensstand, welche Frist, welches Zielprodukt?",
            "Pruefung: Anspruchsgrundlage [Norm], Tatbestandsmerkmale [Aufzaehlung], Subsumtion, Rechtsfolge.",
            "Empfehlung: Konkreter naechster Schritt mit Frist, Adressat, Begruendung und Risiko.",
        ),
    ))


_register_default()


def _register_mietrecht_weg() -> None:
    register(Themenprofil(
        key="mietrecht-weg",
        label="Miet- und Wohnungseigentumsrecht",
        rolle="Du arbeitest im miet- und wohnungseigentumsrechtlichen Fallmodus: Wohnraum, Gewerberaum, Betriebskosten, Minderung, Kuendigung, Raeumung, WEG-Beschluss und Verwalterhaftung werden getrennt geprueft und in ein belegtes Arbeitsprodukt ueberfuehrt.",
        stop_kriterien=(
            "Raeumungsfrist nach Paragraf 721 ZPO oder Vollstreckungsschutz laeuft.",
            "Kuendigungsfrist oder Widerspruchsfrist nach Paragraf 574b BGB im Raum.",
            "Mietminderung droht in Hoehe ueber 20 Prozent ohne gesicherte Mangelfeststellung.",
            "Anfechtungs- oder Beschlussfrist nach Paragraf 45 WEG laeuft (ein Monat ab Beschlussfassung, hoechstens drei Monate ab Mitteilung).",
            "Kuendigung gegenueber besonders schutzwuerdigem Mieter (Hochbetagte, schwer Erkrankte, Schwangerschaft) ohne Sozialklauselpruefung.",
        ),
        stationen=(
            WorkflowStation(
                title="Vertrags- und Beteiligtenmatrix",
                eingang="Mietvertrag, Nachtraege, Hausordnung, Uebergabeprotokoll, Mieterhoehungsschreiben, Betriebskostenabrechnungen, WEG-Teilungserklaerung, Verwaltervertrag, Beschlusssammlung.",
                pruefung="Vertragsart (Wohnraum, Gewerberaum, Staffel, Index, befristet, gemischt) bestimmen; Beteiligte, WEG-Anteile, Sondereigentum und Gemeinschaftseigentum sauber abgrenzen; Klauseln gegen Paragrafen 305 ff. BGB pruefen.",
                arbeitsprodukt="Vertragsmatrix mit Vertragsart, Laufzeit, Miete, Index- oder Staffelmechanik, Kuendigungsfristen, Anlagenstand und WEG-Anteilen.",
            ),
            WorkflowStation(
                title="Mangel, Minderung und Aufrechnung",
                eingang="Mangelanzeigen, Fotos, Schriftverkehr, Gutachten, Mieterhoehungen, Mietminderungsbetraege, Zahlungsstaende, Aufrechnungs- oder Zurueckbehaltungsanzeigen.",
                pruefung="Mangelbegriff nach Paragraf 536 BGB; Anzeige Paragraf 536c BGB; Minderungsquote nach Beeintraechtigung; Zurueckbehaltungsrecht Paragraf 320 BGB; Aufrechnung Paragraf 556b Absatz 2 BGB nur mit angekuendigter Forderung.",
                arbeitsprodukt="Mangelmatrix mit Beschreibung, Anzeige, Beweisangebot, Minderungsquote, Zurueckbehaltung und Anschlussforderung.",
            ),
            WorkflowStation(
                title="Betriebs- und Heizkostenabrechnung",
                eingang="Betriebskostenabrechnungen, Belege, Heizkostenabrechnungen, BetrKV-Katalog, Wirtschaftsplan, Vorauszahlungen, Einwendungen.",
                pruefung="Formelle Wirksamkeit Paragraf 556 Absatz 3 BGB (Zwoelf-Monats-Frist) und 259 BGB; Umlagefaehigkeit nach Paragraf 2 BetrKV und Mietvertrag; Heizkostenverteilung Paragrafen 7 bis 9 HeizkostenV; Belegeinsicht und Nachforderungsausschluss.",
                arbeitsprodukt="Pruefvermerk Betriebskosten mit Positionen, Umlagepruefung, Einwendungen und Nachforderungs- oder Erstattungsbetrag.",
            ),
            WorkflowStation(
                title="Kuendigung und Raeumung",
                eingang="Kuendigungsschreiben, Mahnungen, Mietrueckstaende, Eigenbedarfsbegruendung, Sozialklauselgesichtspunkte, Raeumungstitel, Zwangsraeumungsstand.",
                pruefung="Form und Begruendung Paragraf 568 Absatz 1 BGB; Zahlungsverzug Paragraf 543 Absatz 2 Nummer 3 BGB und Paragraf 569 Absatz 3 BGB (Schonfristzahlung); ordentliche Kuendigung Paragrafen 573, 573c BGB; Eigenbedarf konkret, Alternativwohnung; Sozialklausel Paragrafen 574 ff. BGB; Berliner Raeumung Paragraf 885a ZPO.",
                arbeitsprodukt="Kuendigungs- oder Raeumungsbaustein mit Kuendigungsgrund, Heilungschance, Widerspruchsperspektive und Anschluss im Vollstreckungsrecht.",
            ),
            WorkflowStation(
                title="Mieterhoehung und Mietpreisbremse",
                eingang="Mieterhoehungsschreiben Vergleichsmiete, Index- oder Staffelmechanik, Mietspiegel, Mietbeginnvereinbarung, Auskuenfte zur Vormiete.",
                pruefung="Form Paragraf 558a BGB; Kappungsgrenze Paragraf 558 Absatz 3 BGB; Vergleichsmiete und Mietspiegel; Mietpreisbremse Paragrafen 556d ff. BGB mit Begruendungspflicht des Vermieters und Auskunftsanspruch Paragraf 556g Absatz 3 BGB; Indexmiete Paragraf 557b BGB.",
                arbeitsprodukt="Zustimmungs- oder Ablehnungsschreiben mit Berechnung, Begruendungspruefung und Anschlussfrist Paragraf 558b BGB.",
            ),
            WorkflowStation(
                title="Wohnungseigentumsrecht und Beschluss",
                eingang="WEG-Versammlungsprotokoll, Beschluesse, Einberufung, Beschlussvorschlag, Wirtschaftsplan, Jahresabrechnung, Hausgeld, Sondervergueting Verwalter.",
                pruefung="Anfechtungsfrist Paragraf 45 WEG; Beschlusszustaendigkeit nach Paragrafen 19, 20 WEG; Ordnungsgemaesse Verwaltung Paragraf 18 Absatz 2 WEG; Bauliche Veraenderung Paragraf 20 WEG; Stoererhaftung der Gemeinschaft.",
                arbeitsprodukt="Anfechtungsklage, Beschlussersetzungsklage oder Pruefvermerk fuer Beirat und Verwaltung mit konkreter Antragsfassung.",
            ),
        ),
        pflichtnormen=(
            "Paragraf 535 BGB (Hauptpflichten)",
            "Paragrafen 536, 536a, 536c BGB (Mangel und Minderung)",
            "Paragraf 543 Absatz 2 Nummer 3 BGB und Paragraf 569 Absatz 3 BGB (fristlose Kuendigung wegen Zahlungsverzug, Schonfrist)",
            "Paragrafen 573, 573a, 573c BGB (ordentliche Kuendigung, Fristen)",
            "Paragrafen 574 ff. BGB (Sozialklausel)",
            "Paragrafen 556, 556a, 556d, 556g, 558 ff. BGB (Betriebskosten, Mietpreisbremse, Vergleichsmiete)",
            "Paragrafen 568, 569 BGB (Form, Heilung)",
            "Paragraf 940a ZPO (Raeumung gegen Dritte)",
            "Paragrafen 18, 19, 20, 23, 24, 27, 28, 44, 45 WEG (Verwaltung, Beschluss, Anfechtung)",
            "Paragrafen 7 bis 9 HeizkostenV",
            "Paragrafen 1, 2 BetrKV",
            "Paragraf 23 Nummer 2a GVG (Zustaendigkeit Wohnraummiete am Amtsgericht)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "BGH", "VIII ZR 6/04", "20.07.2005", "BGHZ 163, 366",
                "Eine Betriebskostenabrechnung ist formell ordnungsgemaess, wenn sie eine geordnete Zusammenstellung der Einnahmen und Ausgaben enthaelt, aus der ein durchschnittlicher Mieter ohne juristische oder kaufmaennische Spezialkenntnisse die Abrechnung nachvollziehen kann.",
            ),
            Leitentscheidung(
                "BGH", "VIII ZR 91/10", "06.10.2010", "BGHZ 187, 110",
                "Eine Formularklausel, die die Schoenheitsreparaturen starr nach festen Zeitintervallen ohne Ruecksicht auf den Erhaltungszustand der Wohnung verlangt, benachteiligt den Mieter unangemessen und ist nach Paragraf 307 BGB unwirksam.",
            ),
            Leitentscheidung(
                "BGH", "VIII ZR 270/19", "29.04.2020", "BGHZ 225, 297",
                "Bei der Mietpreisbremse muss der Vermieter eine zur Ausnahme von der Mietobergrenze fuehrende Vormiete oder Modernisierung in der gesetzlich vorgeschriebenen Form bei Mietvertragsschluss unaufgefordert offenlegen; andernfalls bleibt die Mietobergrenze nach Paragraf 556d BGB unveraendert.",
            ),
            Leitentscheidung(
                "BGH", "VIII ZR 19/14", "19.11.2014", "NJW 2015, 928",
                "Bei der Eigenbedarfskuendigung muss der Vermieter die fuer die Erfuellung des Eigenbedarfs benoetigten konkreten Personen und den Nutzungszweck so eindeutig angeben, dass dem Mieter eine Pruefung der Berechtigung des geltend gemachten Eigenbedarfs ermoeglicht wird.",
            ),
            Leitentscheidung(
                "BGH", "VIII ZR 17/15", "18.05.2016", "NJW 2016, 2884",
                "Ein Zahlungsverzug, der die fristlose Kuendigung des Wohnraummietverhaeltnisses traegt, entfaellt rueckwirkend, wenn der Mieter die rueckstaendige Miete innerhalb der Schonfrist nach Paragraf 569 Absatz 3 BGB ausgleicht; die Schonfristregelung erfasst jedoch nicht die hilfsweise erklaerte ordentliche Kuendigung.",
            ),
            Leitentscheidung(
                "BGH", "V ZR 152/19", "16.10.2020", "NJW 2021, 53",
                "Beschluesse der Wohnungseigentuemer ueber bauliche Veraenderungen sind nach Paragraf 20 WEG mit einfacher Mehrheit zulaessig; entstehende Kosten tragen nach Paragraf 21 WEG grundsaetzlich nur die zustimmenden oder die zur Nutzung Berechtigten.",
            ),
        ),
        pruefraster=(
            "Welche Vertragsart liegt vor, und welche Pflichten erwachsen daraus konkret?",
            "Welcher Mangel, welche Anzeige, welcher Schaden und welche Beweise sind dokumentiert?",
            "Welche Frist (Schonfrist, Widerspruchsfrist, Anfechtungsfrist Paragraf 45 WEG) laeuft, und was ist zu sichern?",
            "Welche formellen Anforderungen an Kuendigung, Mieterhoehung oder Beschluss sind erfuellt?",
            "Welches Endprodukt (Schriftsatz, Mahnschreiben, Beschlussanfechtung, Aufrechnungserklaerung, Klageentwurf) ist angefordert?",
        ),
        skelette=(
            "Mahnschreiben: Aktive Klaeger, Adresse, Vertrag vom [Datum], offener Rueckstand [Betrag], Frist [Datum], Verzugsfolgen, Ankuendigung der Kuendigung.",
            "Klage auf Zahlung der Miete: Antrag, Aktivlegitimation, Vertrag, Faelligkeit, Verzug, Kuendigungsandrohung, Zinsen, Kostenfolge.",
            "Beschlussanfechtung: Antrag, Aktivlegitimation, Beschluss, Anfechtungsfrist Paragraf 45 WEG, Anfechtungsgruende (formell und materiell), Hilfsanfechtungsantrag.",
        ),
    ))


_register_mietrecht_weg()


def _register_arbeitsrecht() -> None:
    register(Themenprofil(
        key="arbeitsrecht",
        label="Arbeitsrecht (individual und kollektiv)",
        rolle="Du arbeitest im arbeitsrechtlichen Fallmodus: Begruendung, Inhalt und Beendigung des Arbeitsverhaeltnisses, Kuendigungsschutz, Befristung, Vereinbarung, Vergueting, Zeugnis und Beteiligungsrechte von Betriebsrat und Personalrat werden mit Fristen, Belegen und Antragslogik verbunden.",
        stop_kriterien=(
            "Drei-Wochen-Frist nach Paragraf 4 KSchG laeuft (Klage gegen Kuendigung).",
            "Ausschlussfrist im Tarifvertrag oder Arbeitsvertrag droht (ueblich ein bis drei Monate).",
            "Anfechtungsfrist nach Paragraf 626 Absatz 2 BGB (Zwei-Wochen-Frist) bei Verdachts- oder Tatkuendigung.",
            "Betriebsuebergang nach Paragraf 613a BGB ohne Information binnen Monatsfrist Paragraf 613a Absatz 6 BGB.",
            "AGG-Frist nach Paragraf 15 Absatz 4 AGG (zwei Monate ab Kenntnis).",
        ),
        stationen=(
            WorkflowStation(
                title="Arbeitsvertrag und Status",
                eingang="Arbeitsvertrag, Aenderungsvertraege, Stellenbeschreibung, Eingruppierung, Sozialversicherungsstatus, Verguetungssystem, Tarifbindung, Betriebsvereinbarungen.",
                pruefung="Arbeitnehmerbegriff Paragraf 611a BGB; Befristung Paragraf 14 TzBfG (sachgrundlos hoechstens zwei Jahre); Eingruppierung; AGB-Kontrolle Paragrafen 305 ff. BGB; Bezugnahmeklauseln auf Tarifvertrag und Betriebsvereinbarung.",
                arbeitsprodukt="Statusmatrix mit Eingruppierung, Verguetung, Befristung, Tarifbindung und identifizierten Risiken.",
            ),
            WorkflowStation(
                title="Kuendigung und Aufhebungsvertrag",
                eingang="Kuendigungsschreiben, Abmahnungen, Anhoerung Betriebsrat, Sozialdaten, Aufhebungsvertrag, Versetzungsangebote, Schwerbehindertenstatus.",
                pruefung="KSchG-Anwendungsbereich Paragraf 23 KSchG (mehr als zehn Arbeitnehmer); Soziale Rechtfertigung Paragraf 1 KSchG (verhaltens-, personen- oder betriebsbedingt); Form Paragraf 623 BGB; Betriebsratsanhoerung Paragraf 102 BetrVG; Sonderkuendigungsschutz Paragrafen 168 SGB IX, 17 MuSchG, 18 BEEG; Klagefrist Paragraf 4 KSchG.",
                arbeitsprodukt="Kuendigungsschutzklage, Vergleichsmatrix mit Abfindungserwartung und Anschlussfristen.",
            ),
            WorkflowStation(
                title="Verguetung und Annahmeverzug",
                eingang="Lohnabrechnungen, Tarif- und Vergueterungsregelungen, Vereinbarte Sonderzahlungen, Ueberstunden, Zielvereinbarungen, Pfaendungsschutz.",
                pruefung="Anspruchsgrundlage Paragraf 611a Absatz 2 BGB, Tarif, Betriebsvereinbarung, Gesamtzusage; Ueberstunden Paragraf 612 BGB und Darlegungslast; Annahmeverzug Paragraf 615 BGB; Anrechnungspflicht Paragraf 11 KSchG; Ausschlussfristen.",
                arbeitsprodukt="Zahlungsklage oder Mahnschreiben mit Stundenmatrix, Beweisangeboten, Zinsen und Anschluss in der Vollstreckung.",
            ),
            WorkflowStation(
                title="Zeugnis und Beendigungsfolgen",
                eingang="Zeugnisentwurf, Zwischenzeugnis, Schluessel zu Formulierungen, Beurteilungsbogen, Tarifregelungen, Wettbewerbsklauseln.",
                pruefung="Anspruch Paragraf 109 GewO; Wahrheits- und Wohlwollensprinzip; ueberdurchschnittliche Bewertung im Streitfall vom Arbeitnehmer darzulegen; nachvertragliches Wettbewerbsverbot Paragrafen 74 ff. HGB; Karenzentschaedigung.",
                arbeitsprodukt="Zeugnisentwurf oder Berichtigungsbegehren, Wettbewerbsklauselpruefung, Anschluss in Vollstreckung Paragraf 888 ZPO.",
            ),
            WorkflowStation(
                title="Kollektivrecht und Betriebsrat",
                eingang="Betriebsvereinbarungen, Anhoerungen Paragraf 102 BetrVG, Mitbestimmungslagen, Einigungsstelle, Tarifvertraege, Tarifvertragsbindung.",
                pruefung="Mitbestimmungstatbestand Paragraf 87 BetrVG (zwingend); Beteiligungsrechte Paragrafen 99, 100, 111 BetrVG; Einigungsstelle Paragraf 76 BetrVG; Tarifautonomie Artikel 9 Absatz 3 GG; Tarifbindung Paragrafen 3, 4 TVG.",
                arbeitsprodukt="Stellungnahme an den Betriebsrat oder Einigungsstellenantrag mit konkreter Antragsfassung und Anschlusspflichten.",
            ),
            WorkflowStation(
                title="Diskriminierung und Beschaeftigtendatenschutz",
                eingang="Stellenausschreibung, Bewerbungsverfahren, Beurteilung, Versetzungen, Beschwerden, Datenverarbeitung im Arbeitsverhaeltnis.",
                pruefung="AGG Paragrafen 1, 7, 15 mit Indizienlast Paragraf 22 AGG; Geltung in Beendigung und Begruendung; Beschaeftigtendatenschutz Paragraf 26 BDSG; Anspruchsdurchsetzung in Zwei-Monats-Frist; Beweislastverteilung.",
                arbeitsprodukt="Entschaedigungs- oder Schadensersatzklage, Beschwerde nach Paragraf 13 AGG oder Stellungnahme an den Arbeitgeber.",
            ),
        ),
        pflichtnormen=(
            "Paragraf 611a BGB (Arbeitnehmerbegriff)",
            "Paragraf 615 BGB (Annahmeverzug)",
            "Paragraf 622 BGB (Kuendigungsfristen)",
            "Paragraf 623 BGB (Schriftform)",
            "Paragraf 626 BGB (ausserordentliche Kuendigung, Zwei-Wochen-Frist)",
            "Paragraf 4 KSchG (Klagefrist)",
            "Paragraf 1 KSchG (Sozialrechtfertigung)",
            "Paragraf 102 BetrVG (Anhoerung des Betriebsrats)",
            "Paragraf 87 BetrVG (zwingende Mitbestimmung)",
            "Paragraf 14 TzBfG (Befristung)",
            "Paragraf 109 GewO (Zeugnis)",
            "Paragrafen 7, 15, 22 AGG (Benachteiligungsverbot, Entschaedigung, Beweislast)",
            "Paragraf 168 SGB IX (Zustimmungserfordernis bei Schwerbehinderung)",
            "Paragraf 17 MuSchG, Paragraf 18 BEEG (Sonderkuendigungsschutz)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "BAG", "2 AZR 797/11", "21.06.2012", "BAGE 142, 158",
                "Eine Verdachtskuendigung setzt voraus, dass dringende, auf objektiven Tatsachen gestuetzte Verdachtsmomente vorliegen, dass der Arbeitgeber alle zumutbaren Aufklaerungsbemuehungen unternommen und den Arbeitnehmer zu der konkreten Tat angehoert hat; die Anhoerung muss inhaltlich so konkret sein, dass eine sachgerechte Stellungnahme moeglich wird.",
            ),
            Leitentscheidung(
                "BAG", "2 AZR 651/13", "20.06.2013", "NZA 2013, 1294",
                "Bei einer fristlosen Kuendigung wegen einer rechtswidrigen Pflichtverletzung ist vor Ausspruch grundsaetzlich eine einschlaegige Abmahnung erforderlich; eine Abmahnung ist nur entbehrlich, wenn eine Verhaltensaenderung in Zukunft selbst nach Abmahnung nicht erwartet werden kann oder die Pflichtverletzung so schwer wiegt, dass selbst ihre erstmalige Hinnahme dem Arbeitgeber nicht zuzumuten ist.",
            ),
            Leitentscheidung(
                "BAG", "7 AZR 716/09", "06.04.2011", "BAGE 137, 275",
                "Eine sachgrundlose Befristung nach Paragraf 14 Absatz 2 TzBfG ist nicht zulaessig, wenn mit demselben Arbeitgeber bereits zuvor ein Arbeitsverhaeltnis bestanden hat; das Tatbestandsmerkmal 'zuvor' ist nicht durch eine starre Drei-Jahres-Grenze begrenzt.",
            ),
            Leitentscheidung(
                "BVerfG", "1 BvL 7/14", "06.06.2018", "BVerfGE 149, 126",
                "Paragraf 14 Absatz 2 Satz 2 TzBfG, der eine sachgrundlose Befristung nur bei Vorbeschaeftigung verbietet, ist verfassungskonform dahin auszulegen, dass eine Vorbeschaeftigung dann nicht entgegensteht, wenn diese sehr lange zurueckliegt oder ganz anders geartet war; die starre Drei-Jahres-Grenze des BAG ist nicht haltbar.",
            ),
            Leitentscheidung(
                "BAG", "8 AZR 1012/08", "22.07.2010", "BAGE 135, 80",
                "Im Rahmen der Indizienlast nach Paragraf 22 AGG muss der Arbeitnehmer Tatsachen vortragen, die eine Benachteiligung wegen eines in Paragraf 1 AGG genannten Merkmals mit ueberwiegender Wahrscheinlichkeit vermuten lassen; eine ueberlange Bewerbungsdauer oder unsubstantiierte Stellenkriterien koennen Indizien sein.",
            ),
            Leitentscheidung(
                "BAG", "9 AZR 584/19", "25.07.2023", "NZA 2023, 1494",
                "Der Anspruch auf gesetzlichen Mindesturlaub verfaellt nur dann zum Jahresende oder bei Uebertragung am 31. Maerz, wenn der Arbeitgeber den Arbeitnehmer rechtzeitig und in geeigneter Form aufgefordert hat, seinen Urlaub zu nehmen, und ihn klar und rechtzeitig darauf hingewiesen hat, dass der Urlaub anderenfalls verfaellt.",
            ),
        ),
        pruefraster=(
            "Welche Art Beendigung wird geprueft (ordentlich, ausserordentlich, Verdachts-, Aufhebung)?",
            "Welche Kuendigungsfrist Paragraf 622 BGB oder Sonderfrist (Paragraf 626 BGB, Tarifvertrag) gilt?",
            "Welche Beteiligungsrechte (Betriebsrat, Personalrat, Schwerbehindertenvertretung, Integrationsamt) sind erfuellt?",
            "Welche Klage-, Ausschluss- oder Anfechtungsfristen sind im Raum?",
            "Welches Endprodukt (Kuendigungsschutzklage, Anhoerung, Vergleichsvorschlag, AGG-Entschaedigung) ist gefragt?",
        ),
        skelette=(
            "Kuendigungsschutzklage: Antrag (Feststellung), Klagefrist Paragraf 4 KSchG, Sachverhalt, formelle Pruefung, materielle Sozialrechtfertigung Paragraf 1 KSchG, Beweisangebot.",
            "Anhoerung Betriebsrat Paragraf 102 BetrVG: Mitteilung, Sozialdaten, Kuendigungsart, Kuendigungsgruende, Frist.",
            "Aufhebungsvertrag: Beendigungszeitpunkt, Abfindung, Freistellung, Resturlaub, Zeugnis, Sozialklausel zur Bundesagentur.",
        ),
    ))


_register_arbeitsrecht()


def _register_strafrecht() -> None:
    register(Themenprofil(
        key="strafrecht",
        label="Strafrecht (StA, Verteidigung, OWi)",
        rolle="Du arbeitest als Dezernent oder Verteidiger im Strafverfahren: Anfangsverdacht, Ermittlungsrichtung, Beweisstand, Abschlussverfuegung, Anklage, Strafbefehl, Hauptverhandlungsrolle und Rechtsmittel werden getrennt geprueft und mit Aktenfundstellen verbunden.",
        stop_kriterien=(
            "Untersuchungshaft, Sicherungshaft oder vorlaeufige Festnahme im Raum (Paragrafen 112 ff. StPO).",
            "Verjaehrungsfrist Paragrafen 78 ff. StGB laeuft.",
            "Hauptverhandlungstermin steht in weniger als zwei Wochen ohne Vorbereitung.",
            "Notwendige Verteidigung Paragraf 140 StPO ohne Beiordnung.",
            "Verstaendigungsangebot Paragraf 257c StPO ohne Hinweis nach Paragraf 257c Absatz 5 StPO.",
        ),
        stationen=(
            WorkflowStation(
                title="Anzeigen- und Aktenaufnahme",
                eingang="Anzeige, Aktenvermerk, Polizeibericht, Asservatenliste, Vernehmungsprotokolle, Tatortskizze, Tatfotos, Beschuldigtenangaben.",
                pruefung="Anfangsverdacht Paragraf 152 Absatz 2 StPO; Zustaendigkeit nach Paragraf 143 GVG; Schutz von Berufsgeheimnistraegern Paragraf 53 StPO; Ermittlungsansatz nach Paragraf 160 StPO; Vermerkpflicht Paragraf 168 StPO.",
                arbeitsprodukt="Aktenstrukturuebersicht mit Beschuldigten, Tatzeit, Tatort, Tatvorwurf, Beweismittel, offenen Ermittlungsauftraegen.",
            ),
            WorkflowStation(
                title="Ermittlung und Beweismittel",
                eingang="Vernehmungen, Sachverstaendigengutachten, Durchsuchungs- und Beschlagnahmeprotokolle, Telekommunikationsdaten, Asservaten, Spurensicherung.",
                pruefung="Vernehmung Paragrafen 136, 136a, 163a StPO mit Belehrungspflichten; Durchsuchung Paragrafen 102, 105 StPO mit Richtervorbehalt; Beschlagnahme Paragrafen 94, 98 StPO; TKUe Paragrafen 100a, 100e StPO; Beweisverwertungsverbote Paragraf 136a Absatz 3 StPO und Frueherkennungsdoktrin.",
                arbeitsprodukt="Beweismatrix mit Beweisthema, Beweismittel, Verwertbarkeit, Anschlussantrag (Beweisantrag Paragraf 244 StPO oder Beweismittelverwertungsverbot).",
            ),
            WorkflowStation(
                title="Materielle Pruefung Tat",
                eingang="Tatvorwurf, einschlaegige Paragrafen StGB, Nebenstrafrecht (BtMG, AO, StVG, WaffG), Konkurrenzlagen, Beteiligungsformen, Schuldfaehigkeit.",
                pruefung="Drei-Stufen-Pruefung Tatbestand, Rechtswidrigkeit, Schuld; Vorsatz, Fahrlaessigkeit, Irrtum (Paragrafen 16, 17 StGB); Rechtfertigung (Paragrafen 32, 34 StGB); Entschuldigung (Paragrafen 33, 35 StGB); Versuch, Ruecktritt, Teilnahme; Konkurrenzen Paragrafen 52, 53 StGB.",
                arbeitsprodukt="Tatbestandsmatrix mit Schuldspruchvorbereitung, Tateinheits- oder Tatmehrheitsfrage, Strafzumessungsgesichtspunkten Paragraf 46 StGB.",
            ),
            WorkflowStation(
                title="Abschluss- und Verfahrensentscheidung",
                eingang="Aktenbericht, Abschlussvermerk, Anklageentwurf, Strafbefehl, Einstellungspruefung, Verfahrenslage Beschuldigtenverhaltnis, Geschaedigteninteressen, OWi-Lage.",
                pruefung="Einstellung Paragrafen 170 Absatz 2, 153, 153a StPO; Anklage Paragrafen 200, 199 StPO; Strafbefehl Paragrafen 407 ff. StPO; Adhaesion Paragrafen 403 ff. StPO; OWi-Bescheid Paragraf 65 OWiG.",
                arbeitsprodukt="Abschlussverfuegung, Anklagebaustein, Strafbefehlsentwurf oder Einstellungsverfuegung mit konkretem Antrag und Begruendung.",
            ),
            WorkflowStation(
                title="Hauptverhandlung und Rechtsmittel",
                eingang="Anklage, Eroeffnungsbeschluss, Beweisantraege, Eroerterungsstand Paragraf 257c StPO, Selbstleseverfahren Paragraf 249 Absatz 2 StPO, Strafmasspraxis.",
                pruefung="Eroeffnung Paragraf 203 StPO; Beweisantraege und Ablehnung Paragrafen 244, 245 StPO; Verstaendigung Paragraf 257c StPO mit Hinweispflichten; Rechtsmittel Paragrafen 312 ff. StPO (Berufung), Paragrafen 333 ff. StPO (Revision).",
                arbeitsprodukt="Plaedoyerbaustein, Beweisantrag, Verstaendigungsentwurf oder Rechtsmittelbegruendung mit konkretem Antrag und Frist.",
            ),
            WorkflowStation(
                title="Strafzumessung und Rechtsfolgen",
                eingang="Strafrahmen, Vorstrafen, Bewaehrungsfaehigkeit, Geldstrafe nach Tagessaetzen, Bewaehrungsweisungen, Nebenfolgen (Fahrerlaubnis, Berufsverbot, Einziehung).",
                pruefung="Strafzumessung Paragraf 46 StGB; Geldstrafe Paragrafen 40 ff. StGB; Bewaehrung Paragrafen 56 ff. StGB; Einziehung Paragrafen 73 ff. StGB; Massregeln Paragrafen 61 ff. StGB; Faehrnisverbot, Fahrverbot Paragraf 44 StGB; OWi-Bussgeldrahmen Paragrafen 17, 18 OWiG.",
                arbeitsprodukt="Strafmassvotum mit Strafrahmen, Strafzumessungstabelle, Vergleich zur Region und Anschluss in der Vollstreckung.",
            ),
        ),
        pflichtnormen=(
            "Paragraf 152 Absatz 2 StPO (Legalitaetsprinzip)",
            "Paragraf 160 StPO (Ermittlungsherrschaft)",
            "Paragraf 163 StPO (Polizeiliche Aufgaben)",
            "Paragrafen 136, 136a, 163a StPO (Vernehmung, Belehrung)",
            "Paragrafen 102, 105 StPO (Durchsuchung)",
            "Paragraf 170 StPO (Einstellung, Anklage)",
            "Paragrafen 200, 203 StPO (Anklage, Eroeffnung)",
            "Paragraf 244 StPO (Beweisantrag und Aufklaerungspflicht)",
            "Paragraf 257c StPO (Verstaendigung)",
            "Paragrafen 16, 17 StGB (Irrtum)",
            "Paragrafen 32, 34 StGB (Rechtfertigung)",
            "Paragraf 46 StGB (Strafzumessung)",
            "Paragrafen 73, 73a StGB (Einziehung)",
            "Paragrafen 140, 141 StPO (notwendige Verteidigung)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "BVerfG", "2 BvR 2628/10", "19.03.2013", "BVerfGE 133, 168",
                "Eine Verstaendigung im Strafverfahren ist nur zulaessig, wenn das Gericht den Angeklagten ueber die Voraussetzungen, den moeglichen Inhalt und die Folgen einer Verstaendigung umfassend belehrt, die Verstaendigung in oeffentlicher Hauptverhandlung erfolgt, das Ergebnis in das Protokoll aufgenommen wird und kein Geestaendnis ohne richterliche Tatsachenfeststellung verwertet wird.",
            ),
            Leitentscheidung(
                "BGH", "GSSt 1/17", "01.02.2017", "BGHSt 62, 184",
                "Die Verwertung von Erkenntnissen aus rechtswidrig erlangten Beweismitteln richtet sich nach einer Abwaegung zwischen dem Aufklaerungsinteresse und dem Gewicht des Eingriffs; ein absolutes Verwertungsverbot besteht regelmaessig nur bei schwerwiegenden, bewussten oder willkuerlichen Rechtsverstoessen.",
            ),
            Leitentscheidung(
                "BGH", "5 StR 261/17", "19.10.2017", "BGHSt 62, 277",
                "Bei einer Verstaendigung ist das Gericht verpflichtet, dem Angeklagten die Bandbreite des Strafrahmens mitzuteilen; das Unterlassen begruendet einen absoluten Revisionsgrund.",
            ),
            Leitentscheidung(
                "BGH", "GSSt 2/17", "13.05.2020", "BGHSt 64, 256",
                "Die Einziehung von Taterloesen nach Paragrafen 73, 73a StGB richtet sich nach dem Bruttoprinzip; sofern Vermoegen aus einer rechtswidrigen Tat erlangt wurde, ist es einzuziehen, ohne dass tatbezogene Aufwendungen abzuziehen sind, wenn sich diese in den Sachverhalt der Tatbegehung einfuegen.",
            ),
            Leitentscheidung(
                "BGH", "4 StR 168/19", "27.02.2020", "BGHSt 64, 314",
                "Bei der Strafzumessung darf das Gericht ein Geestaendnis nur dann strafmildernd beruecksichtigen, wenn es Ausdruck von Reue und Unrechtseinsicht ist; ein blosses prozesstaktisches Geestaendnis ist allenfalls geringfuegig zu beruecksichtigen.",
            ),
            Leitentscheidung(
                "BGH", "2 StR 247/16", "07.12.2017", "BGHSt 63, 29",
                "Der Anspruch auf rechtliches Gehoer aus Artikel 103 Absatz 1 GG verpflichtet das Gericht, einen rechtzeitig gestellten Beweisantrag durch begruendeten Beschluss zu verbescheiden; die blosse Ablehnung in den Urteilsgruenden genuegt nicht.",
            ),
        ),
        pruefraster=(
            "Welche Verfahrensphase (Ermittlungs-, Zwischen-, Hauptverhandlungs-, Rechtsmittel-) liegt vor?",
            "Welcher Tatvorwurf, welche Beteiligung, welche Konkurrenzlage konkret?",
            "Welche Beweismittel sind verwertbar, welche stehen unter Verwertungsverbot?",
            "Welche Massnahmen (Untersuchungshaft, Durchsuchung, TKUe) sind ergangen, und wie lange ist der Eingriff zulaessig?",
            "Welche Verfahrensentscheidung (Einstellung, Anklage, Strafbefehl, OWi) ist abschlussreif?",
        ),
        skelette=(
            "Abschlussvermerk: Tatvorwurf, Beweislage, Aktenfundstelle, Rechtliche Wuerdigung, Strafmassueberlegung, Abschlussvorschlag (Einstellung Paragraf 170, Anklage, Strafbefehl).",
            "Beweisantrag: Bestimmtes Beweisthema, bestimmtes Beweismittel, Konnexitaet, Bedeutung fuer das Urteil, Anschluss in der Hauptverhandlung.",
            "Revisionsbegruendung: Verfahrensrueg (Paragrafen 337, 338 StPO) und Sachrueg, Frist, Anschluss.",
        ),
    ))


_register_strafrecht()


def _register_strafrecht_gericht() -> None:
    base = PROFILE["strafrecht"]
    register(Themenprofil(
        key="strafrecht-gericht",
        label="Strafrecht aus richterlicher Sicht",
        rolle="Du arbeitest aus richterlicher Sicht im Strafverfahren: Eroeffnungsbeschluss, Verhandlungsleitung, Beweiserhebung, Beweiswuerdigung, Urteil und Strafzumessung werden mit Aktenfundstellen vorbereitet.",
        stop_kriterien=base.stop_kriterien + (
            "Befangenheitsantrag oder Befangenheitsbesorgnis im Raum.",
            "Hinweispflicht nach Paragraf 265 StPO bei abweichender rechtlicher Wuerdigung nicht erteilt.",
        ),
        stationen=base.stationen,
        pflichtnormen=base.pflichtnormen + (
            "Paragraf 261 StPO (freie richterliche Beweiswuerdigung)",
            "Paragrafen 264, 265 StPO (Verfahrensgegenstand, Hinweispflicht)",
            "Paragraf 267 StPO (Urteilsgruende)",
        ),
        leitentscheidungen=base.leitentscheidungen,
        pruefraster=base.pruefraster + (
            "Welche Hinweispflicht Paragraf 265 StPO ist zu erteilen?",
            "Welche Anschlussfragen aus der Strafzumessung (Vorstrafen, Schadenswiedergutmachung) sind im Tatrichterurteil zu beruecksichtigen?",
        ),
        skelette=base.skelette + (
            "Eroeffnungsbeschluss Paragrafen 199, 203 StPO: Anklagezulassung, hinreichender Tatverdacht, Eroeffnung vor Spruchkoerper.",
            "Urteil Paragraf 267 StPO: Tenor, Tatsachenfeststellungen, Beweiswuerdigung, rechtliche Wuerdigung, Strafzumessung, Kosten.",
        ),
    ))


_register_strafrecht_gericht()


def _register_zivilprozess() -> None:
    register(Themenprofil(
        key="zivilprozess",
        label="Zivilprozess und Relationstechnik",
        rolle="Du arbeitest in der zivilprozessualen Relationstechnik: Klaeger-, Beklagten-, Beweis- und Entscheidungsstation werden konsequent getrennt, jede Tatsache wird einer Norm und einem Beweisangebot zugeordnet, ein Hinweis, ein Beweisbeschluss, ein Urteilsbaustein oder ein Vergleichsvorschlag entsteht.",
        stop_kriterien=(
            "Notfrist nach Paragraf 224 ZPO (Klagefrist, Berufungs- oder Beschwerdefrist) laeuft.",
            "Zustellung an unbekannten Aufenthalt ohne oeffentliche Zustellung Paragraf 185 ZPO geprueft.",
            "Versaeumnisurteil droht und Einspruchsfrist Paragraf 339 ZPO laeuft.",
            "Streitwert beruehrt Zustaendigkeit oder Anwaltszwang nicht erkannt.",
            "Hinweispflicht nach Paragraf 139 ZPO nicht erteilt.",
        ),
        stationen=(
            WorkflowStation(
                title="Eingangs- und Zustaendigkeitspruefung",
                eingang="Klageschrift, Anlagen, Streitwert, Zustellung, Vollmacht, Prozesskostenhilfe, sachliche und oertliche Zustaendigkeit.",
                pruefung="Zulaessigkeit der Klage Paragrafen 253 ff. ZPO; sachliche Zustaendigkeit Paragrafen 23, 71 GVG (Wertgrenze 5.000 Euro); oertliche Zustaendigkeit Paragrafen 12, 17, 29, 32 ZPO; Anwaltszwang Paragraf 78 ZPO; vorlaeufige Streitwertfestsetzung.",
                arbeitsprodukt="Eingangsverfuegung mit Zustaendigkeitsvermerk, Streitwertvorschlag, Hinweisbedarf und Terminvorschlag.",
            ),
            WorkflowStation(
                title="Klaegerstation",
                eingang="Klageantrag, Klagegrund, Beweisangebote des Klaegers, Anlagen.",
                pruefung="Aktivlegitimation, Anspruchsgrundlage, Tatbestandsmerkmale, Schluessigkeit Paragraf 138 ZPO; bestimmter Klageantrag Paragraf 253 Absatz 2 Nummer 2 ZPO; Beweisangebot.",
                arbeitsprodukt="Klaegerstation mit Tatsachenkern, behaupteten Tatsachen, Beweisangebot und Anspruchsgrundlage.",
            ),
            WorkflowStation(
                title="Beklagtenstation",
                eingang="Klageerwiderung, Bestreiten, Einwendungen, Einreden, Widerklage, Aufrechnung, Beweisangebote der Beklagtenseite.",
                pruefung="Erheblichkeit des Bestreitens; Einreden (Verjaehrung Paragraf 214 BGB, Zurueckbehaltungsrecht Paragraf 273 BGB, Einrede des nicht erfuellten Vertrags Paragraf 320 BGB); Aufrechnung Paragrafen 387 ff. BGB; Widerklage Paragraf 33 ZPO.",
                arbeitsprodukt="Beklagtenstation mit erheblichem Bestreiten, Einwendungs- und Einredekatalog, Beweisangeboten.",
            ),
            WorkflowStation(
                title="Beweisstation",
                eingang="Beweisangebote, Sachverstaendigengutachten, Urkunden, Zeugen, Augenschein, Parteivernehmung.",
                pruefung="Streitige, entscheidungserhebliche Tatsache; Beweislast; Strengbeweis Paragrafen 355 ff. ZPO; Freibeweis; Beweismittel; Beweisbeschluss Paragraf 358 ZPO; Sachverstaendigenbeweis Paragrafen 402 ff. ZPO.",
                arbeitsprodukt="Beweisbeschluss oder Beweisbedarfsmatrix mit Beweisthema, Beweisangebot, Beweislast.",
            ),
            WorkflowStation(
                title="Hinweis und Entscheidungsstation",
                eingang="Zwischenstand nach Klaeger-, Beklagten- und Beweisstation; Vergleichsmoeglichkeit; richterliche Hinweise; Verfahrensstand.",
                pruefung="Hinweispflicht Paragraf 139 ZPO; freie Beweiswuerdigung Paragraf 286 ZPO; Schadensschaetzung Paragraf 287 ZPO; Entscheidungsreife; Vergleich Paragraf 278 ZPO; Versaeumnis- und Anerkenntnisentscheidung.",
                arbeitsprodukt="Hinweisbeschluss, Vergleichsvorschlag, Urteilsbaustein oder Beweisbeschluss mit konkreter Antragsfassung.",
            ),
            WorkflowStation(
                title="Urteil und Vollstreckbarkeit",
                eingang="Tenor, Tatbestand, Entscheidungsgruende, Kosten- und Vollstreckungsfolge, Rechtsmittelbelehrung, Streitwertfestsetzung.",
                pruefung="Tenor bestimmt und vollstreckungsfaehig; Kostenentscheidung Paragrafen 91, 92, 100 ZPO; vorlaeufige Vollstreckbarkeit Paragrafen 708 ff. ZPO; Begruendung Paragraf 313 ZPO; Streitwertfestsetzung Paragrafen 63 GKG, 39 ff. GKG.",
                arbeitsprodukt="Urteilsbaustein mit Tenor, Tatbestand, Entscheidungsgruende, Kosten, Vollstreckung und Rechtsmittelbelehrung.",
            ),
        ),
        pflichtnormen=(
            "Paragraf 138 ZPO (Wahrheitspflicht, Erklaerungslast)",
            "Paragraf 139 ZPO (Hinweispflicht)",
            "Paragraf 253 Absatz 2 ZPO (Klageinhalt)",
            "Paragraf 286 ZPO (freie Beweiswuerdigung)",
            "Paragraf 287 ZPO (Schadensschaetzung)",
            "Paragraf 313 ZPO (Urteil)",
            "Paragraf 358 ZPO (Beweisbeschluss)",
            "Paragrafen 91, 92, 100 ZPO (Kostenentscheidung)",
            "Paragrafen 708 ff. ZPO (vorlaeufige Vollstreckbarkeit)",
            "Paragraf 23 Nummer 1 GVG, Paragraf 71 GVG (sachliche Zustaendigkeit)",
            "Paragraf 78 Absatz 1 ZPO (Anwaltszwang)",
            "Paragrafen 12, 17, 29, 32 ZPO (oertliche Zustaendigkeit)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "BGH", "XI ZR 305/19", "20.10.2020", "NJW 2021, 234",
                "Aus Paragraf 139 ZPO ergibt sich eine erweiterte richterliche Hinweispflicht, wenn der Vortrag einer Partei zwar im Tatsachenkern hinreichend, im rechtlichen Folgenausspruch jedoch unklar ist; ein Urteil ohne diesen Hinweis verletzt das Recht auf rechtliches Gehoer.",
            ),
            Leitentscheidung(
                "BGH", "VIII ZR 153/04", "27.04.2005", "BGHZ 162, 351",
                "Substantiierter Vortrag und schluessiger Sachvortrag erfordern, dass die behauptete Tatsache in einer den Tatbestand der Anspruchsgrundlage ausfuellenden Weise dargelegt wird; weitere Konkretisierung muss erst auf entsprechenden Hinweis Paragraf 139 ZPO erfolgen.",
            ),
            Leitentscheidung(
                "BVerfG", "1 BvR 1379/11", "08.07.2014", "NJW 2014, 3147",
                "Das Recht auf effektiven Rechtsschutz aus Artikel 19 Absatz 4 GG verlangt, dass das Fachgericht den Sachverhalt umfassend aufklaert und bei einer in entscheidungserheblichen Punkten unzureichenden Akte einen Beweis erhebt, statt zulasten des Beweisbelasteten zu entscheiden.",
            ),
            Leitentscheidung(
                "BGH", "VI ZR 282/19", "25.05.2020", "NJW 2020, 2630",
                "Die nach Paragraf 286 ZPO erforderliche Ueberzeugung des Tatrichters von der Wahrheit einer streitigen Tatsache verlangt einen fuer das praktische Leben brauchbaren Grad an Gewissheit; es genuegt nicht ein blosses Ueberwiegen der Wahrscheinlichkeit, jedoch ist eine an Sicherheit grenzende Wahrscheinlichkeit nicht erforderlich.",
            ),
            Leitentscheidung(
                "BGH", "VII ZR 144/15", "21.04.2016", "BGHZ 210, 1",
                "Eine fehlerhafte Belehrung ueber das Verfahren bei einer Verstaendigung im Zivilprozess kann die Beweisaufnahme nicht entwerten; entscheidend bleibt, dass die Parteien tatsaechlich Gelegenheit zur Aeusserung hatten und das Gericht zu eigener Ueberzeugung gelangt ist.",
            ),
        ),
        pruefraster=(
            "Welche Partei traegt nach allgemeinen Regeln die Darlegungs- und Beweislast (Anspruchsteller die anspruchsbegruendenden, Anspruchsgegner die anspruchsvernichtenden, anspruchshemmenden Tatsachen)?",
            "Ist der Klageantrag bestimmt Paragraf 253 Absatz 2 Nummer 2 ZPO?",
            "Ist die Klage schluessig (Klaegerstation) und das Bestreiten erheblich (Beklagtenstation)?",
            "Welche streitige Tatsache ist entscheidungserheblich und beweisbeduerftig?",
            "Welche Hinweispflicht Paragraf 139 ZPO ist noch zu erteilen?",
        ),
        skelette=(
            "Eingangsverfuegung: Pruefung Zustaendigkeit, Streitwert, schriftliches Vorverfahren oder frueher erster Termin, Belehrungen, Anlagenrueckgabe.",
            "Hinweisbeschluss Paragraf 139 ZPO: Wesentliche Punkte, fehlende Tatsachen, Beweisangebote, Frist zur Ergaenzung.",
            "Urteil Paragraf 313 ZPO: Tenor, Tatbestand, Entscheidungsgruende, Kosten, Vollstreckung, Streitwert, Rechtsmittel.",
        ),
    ))


_register_zivilprozess()


def _register_familienrecht() -> None:
    register(Themenprofil(
        key="familienrecht",
        label="Familienrecht (Ehesachen, Kindschaft, Unterhalt, Versorgungsausgleich, Betreuung)",
        rolle="Du arbeitest im familienrechtlichen Mandats- oder Gerichtsmodus: Unterhalt, Scheidung, Kindschaftssachen, Versorgungsausgleich, Gueterrecht und Betreuung werden mit Fristen, Belegen und Antragslogik verbunden; Kindeswohl ist Leitwert.",
        stop_kriterien=(
            "Trennungsjahr Paragraf 1565 Absatz 2 BGB noch nicht erfuellt bei Scheidungsantrag.",
            "Kindeswohlgefaehrdung Paragraf 1666 BGB im Raum.",
            "Eilbedarf nach Paragraf 49 FamFG (einstweilige Anordnung) erkennbar.",
            "Beschwerdefrist nach Paragrafen 63, 64 FamFG (Monatsfrist).",
            "Versorgungsausgleichsausschluss Paragraf 27 VersAusglG nicht geprueft.",
            "Notwendige anwaltliche Vertretung Paragraf 114 FamFG (in Ehesachen, Folgesachen, Familienstreitsachen).",
        ),
        stationen=(
            WorkflowStation(
                title="Verfahrens- und Beteiligtenaufnahme",
                eingang="Antrag, Eheurkunde, Geburtsurkunden Kinder, Aufenthaltsbescheinigung, Vermoegensaufstellung, Einkommensnachweise, Jugendamtsbericht, Verfahrenskostenhilfe.",
                pruefung="Verfahrensart (Ehesache, Familienstreitsache, FG-Sache) bestimmen Paragraf 111 FamFG; Zustaendigkeit Paragraf 122 FamFG; Anwaltszwang Paragraf 114 FamFG; Verfahrenskostenhilfe Paragrafen 76 ff. FamFG.",
                arbeitsprodukt="Beteiligten- und Verfahrensuebersicht mit Antragsart, Folgesachen, Kinderbezug und Anlagenstand.",
            ),
            WorkflowStation(
                title="Scheidung und Trennungsfolgen",
                eingang="Trennungsdatum, gemeinsame Wohnung, Verstaendigung ueber Trennungs- und Scheidungsfolgen, Zugewinngemeinschaft, Versorgungsanwartschaften, Hausrat.",
                pruefung="Trennungsjahr Paragraf 1565 BGB; Haerteklausel Paragraf 1568 BGB; Folgesachenverbund Paragraf 137 FamFG; Versorgungsausgleich von Amts wegen Paragraf 1587 BGB; Hausrat Paragrafen 200 ff. FamFG.",
                arbeitsprodukt="Scheidungsantrag mit Folgesachen, Trennungsbescheinigung, Versorgungsausgleichsfragebogen V10 und V100.",
            ),
            WorkflowStation(
                title="Unterhalt",
                eingang="Einkommen, Bereinigungen (Steuer, Vorsorge, berufsbedingte Aufwendungen, Schulden), Kindesunterhaltstabelle, Selbstbehalt, Mangelfall, Auskunftsstand.",
                pruefung="Kindesunterhalt Paragrafen 1601, 1610, 1612a BGB nach Duesseldorfer Tabelle; Ehegattenunterhalt Paragrafen 1361 BGB (Trennungs-), 1569 ff. BGB (Nachtrennungs-); Bedarf, Beduerftigkeit, Leistungsfaehigkeit, Rangfolge Paragraf 1609 BGB; Auskunftspflicht Paragrafen 1605, 1580 BGB.",
                arbeitsprodukt="Unterhaltsberechnung mit Tabellenbezug, Selbstbehalt, Mangelfallquoten, Auskunftslucken und konkreter Antrag.",
            ),
            WorkflowStation(
                title="Kindschaft und Umgang",
                eingang="Sorgerechtsbeschluesse, Umgangsvereinbarung, Jugendamtsberichte, Stellungnahme Verfahrensbeistand, Anhoerung Kind, Pflegeplaetze.",
                pruefung="Elterliche Sorge Paragrafen 1626, 1671 BGB; Umgangsrecht Paragraf 1684 BGB; Kindeswohl Paragraf 1697a BGB; Anhoerung Kind Paragraf 159 FamFG, Eltern Paragraf 160 FamFG, Jugendamt Paragraf 162 FamFG; Verfahrensbeistand Paragraf 158 FamFG.",
                arbeitsprodukt="Antrag oder Beschlussbaustein zu Sorge, Umgang oder Kindeswohlmassnahme mit Beteiligung Jugendamt und Verfahrensbeistand.",
            ),
            WorkflowStation(
                title="Vermoegen und Zugewinn",
                eingang="Anfangs- und Endvermoegensaufstellung, Schenkungen, Erbschaften, Schulden, Berechnungsstand Zugewinn, Vereinbarungen.",
                pruefung="Zugewinngemeinschaft Paragrafen 1363, 1373, 1378 BGB; Auskunftsanspruch Paragraf 1379 BGB; Bewertungsstichtag; vorzeitiger Zugewinn Paragraf 1385 BGB; Notarielle Eheverguetung.",
                arbeitsprodukt="Zugewinnberechnung mit Anfangs-, End-, Zugewinn pro Ehegatte und konkreter Antragsformel.",
            ),
            WorkflowStation(
                title="Betreuung und Vorsorge",
                eingang="Betreuungsverfuegung, Vorsorgevollmacht, Sachverstaendigengutachten Paragraf 280 FamFG, Vorbefragung Paragraf 278 FamFG, Wahl des Betreuers.",
                pruefung="Errichtung der Betreuung Paragrafen 1814 ff. BGB seit 01.01.2023; Erforderlichkeitsprinzip Paragraf 1814 Absatz 3 BGB; Aufgabenkreise Paragraf 1815 BGB; Vergueteung Paragrafen 1876 ff. BGB; gerichtliche Genehmigung Paragrafen 1850 ff. BGB.",
                arbeitsprodukt="Betreuerbericht, Genehmigungsantrag oder Pflichtenuebersicht mit Aufgabenkreis und Anschluss in der Aufsicht.",
            ),
        ),
        pflichtnormen=(
            "Paragraf 1565 BGB (Scheidung, Trennungsjahr)",
            "Paragraf 1568 BGB (Haerteklausel)",
            "Paragrafen 1601, 1610, 1612a BGB (Kindesunterhalt)",
            "Paragrafen 1361, 1569 ff. BGB (Ehegattenunterhalt)",
            "Paragraf 1609 BGB (Rangfolge)",
            "Paragraf 1626, 1671 BGB (elterliche Sorge)",
            "Paragraf 1684 BGB (Umgangsrecht)",
            "Paragraf 1697a BGB (Kindeswohlmassstab)",
            "Paragraf 1587 BGB i. V. m. Versorgungsausgleichsgesetz (VersAusglG)",
            "Paragrafen 1378, 1379 BGB (Zugewinn, Auskunft)",
            "Paragrafen 1814 ff. BGB (Betreuung neuer Rechtsstand)",
            "Paragrafen 111 ff. FamFG (Familiensachen)",
            "Paragraf 49 FamFG (einstweilige Anordnung)",
            "Paragrafen 63, 64 FamFG (Beschwerde, Frist)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "BGH", "XII ZB 565/15", "26.10.2016", "BGHZ 212, 363",
                "Bei der Bemessung des nachehelichen Unterhalts ist die Eigenversorgung des Beduerftigen vorrangig; die Anrechnung fiktiven Einkommens setzt die Verletzung einer Erwerbsobliegenheit voraus, die nach den persoenlichen Verhaeltnissen, der Dauer der Ehe und der Kinderbetreuung zumutbar ist.",
            ),
            Leitentscheidung(
                "BGH", "XII ZB 565/20", "23.06.2021", "FamRZ 2021, 1564",
                "Bei der Beurteilung der Leistungsfaehigkeit ist der angemessene Selbstbehalt nicht starr nach der Duesseldorfer Tabelle anzuwenden, sondern unter Beruecksichtigung der konkreten Lebenshaltungskosten und Verbindlichkeiten zu pruefen; eine pauschale Tabellenanwendung verletzt das Gebot der Einzelfallpruefung.",
            ),
            Leitentscheidung(
                "BGH", "XII ZB 350/17", "07.02.2018", "FamRZ 2018, 593",
                "Bei Bestimmung des Wechselmodells im Rahmen einer Umgangsentscheidung sind die Bindungen des Kindes, die Erziehungseignung und Kooperationsfaehigkeit der Eltern sowie der erklaerte Kindeswille einzubeziehen; das paritaetische Wechselmodell ist nicht der Regelfall.",
            ),
            Leitentscheidung(
                "BVerfG", "1 BvR 354/19", "06.02.2020", "BVerfGE 153, 246",
                "Die Anhoerung des Kindes nach Paragraf 159 FamFG ist von zentraler verfassungsrechtlicher Bedeutung; eine Unterlassung verletzt das Elternrecht aus Artikel 6 Absatz 2 GG, wenn sie nicht durch ausserordentliche Umstaende getragen ist.",
            ),
            Leitentscheidung(
                "BGH", "XII ZB 502/19", "01.04.2020", "FamRZ 2020, 943",
                "Im Versorgungsausgleich sind nach dem Stichtagsprinzip auch nach Rechtshaengigkeit der Scheidung neu erworbene Anrechte einzubeziehen, soweit sie auf der Ehezeit beruhen; eine Beschraenkung auf bei Rechtshaengigkeit bereits begruendete Anrechte ist mit Paragraf 3 VersAusglG unvereinbar.",
            ),
            Leitentscheidung(
                "BGH", "XII ZB 224/20", "16.06.2021", "FamRZ 2021, 1370",
                "Die Anordnung einer Betreuung nach Paragraf 1814 BGB erfordert konkrete Feststellungen dazu, dass der Betroffene seine Angelegenheiten nicht mehr besorgen kann und mildere Mittel (Vorsorgevollmacht, soziale Hilfen, Bevollmaechtigung) nicht ausreichen.",
            ),
        ),
        pruefraster=(
            "Welche Verfahrensart Paragraf 111 FamFG und welche Folgesache liegt vor?",
            "Welche Frist (Trennungsjahr, Beschwerde, einstweilige Anordnung) ist beruehrt?",
            "Welcher Bedarf, welche Beduerftigkeit, welche Leistungsfaehigkeit konkret?",
            "Welche Beteiligten (Jugendamt, Verfahrensbeistand, Kind, Ergaenzungspfleger) sind anzuhoeren?",
            "Welches Endprodukt (Antrag, Beschluss, Vergleich, Betreuerbericht) ist gefragt?",
        ),
        skelette=(
            "Scheidungsantrag: Antrag (Scheidung, Folgesachen), Trennungsjahr Paragraf 1565 BGB, Anlagen, Verfahrenskostenhilfe.",
            "Kindesunterhalt: Antrag in Hoehe von [Betrag] pro Monat nach Duesseldorfer Tabelle, Einkommen, Bereinigung, Selbstbehalt, Rang, Tabellenstufe, Bezug Paragrafen 1601, 1610, 1612a BGB.",
            "Sorgerechtsbeschluss: Beteiligte, Anhoerung Kind, Verfahrensbeistand, Jugendamt, Beschlussformel, Begruendung mit Kindeswohlbezug Paragraf 1697a BGB.",
        ),
    ))


_register_familienrecht()


def _register_insolvenz() -> None:
    register(Themenprofil(
        key="insolvenz",
        label="Insolvenz, Restrukturierung, Sanierung",
        rolle="Du arbeitest im insolvenz- und restrukturierungsrechtlichen Modus: Eroeffnungsverfahren, Verwaltung, Glaeubigerausschuss, Insolvenzplan, StaRUG-Verfahren, Sanierungs- und Anfechtungsfragen werden mit Fristen, Belegen und Antragslogik verbunden.",
        stop_kriterien=(
            "Antragspflicht Paragraf 15a InsO bei juristischen Personen (drei Wochen ab Zahlungsunfaehigkeit, sechs Wochen ab Ueberschuldung).",
            "Insolvenzanfechtung Paragrafen 129 ff. InsO mit ablaufenden Fristen (Paragrafen 132, 133 InsO).",
            "Forderungsanmeldungsfrist Paragraf 28 InsO laeuft.",
            "StaRUG-Restrukturierungsbeauftragter Paragraf 73 StaRUG einzusetzen.",
            "Verwertungsgrenzen oder Massearmut Paragraf 207 InsO im Raum.",
            "Schutzschirmverfahren Paragraf 270d InsO mit Vorlagepflichten.",
        ),
        stationen=(
            WorkflowStation(
                title="Insolvenzgrund und Antragspflicht",
                eingang="Liquiditaetsplan, Insolvenzantrag, Glaeubigerstand, Vermoegensuebersicht, Ueberschuldungsstatus, Fortbestehensprognose, Steuerrueckstaende, Sozialversicherungsbeitraege.",
                pruefung="Zahlungsunfaehigkeit Paragraf 17 InsO; drohende Zahlungsunfaehigkeit Paragraf 18 InsO; Ueberschuldung Paragraf 19 InsO; Antragspflicht Paragraf 15a InsO; Fortbestehensprognose; Befriedigungsluecke 10-Prozent-Schwelle.",
                arbeitsprodukt="Insolvenzgrundvermerk mit Pruefung des Insolvenzgrunds und Empfehlung zur Antragstellung.",
            ),
            WorkflowStation(
                title="Eroeffnungsverfahren und Sicherung",
                eingang="Insolvenzantrag, vorlaeufige Verwaltung, Sicherungsmassnahmen, Anhoerung Schuldner, Glaeubigerinteressen, Aktivvermoegen.",
                pruefung="Pruefung Eroeffnungsgrund Paragraf 27 InsO; Sicherungsmassnahmen Paragraf 21 InsO (vorlaeufige Verwaltung, Verfuegungsverbot, Postsperre, Glaeubigerausschuss); Eigenverwaltung Paragrafen 270 ff. InsO; Schutzschirm Paragraf 270d InsO.",
                arbeitsprodukt="Eroeffnungsbeschluss oder Eroeffnungsantrag mit Sicherungsbedarf, Verwalterauswahl und Anschlusspruefung.",
            ),
            WorkflowStation(
                title="Verwaltung und Masseverwaltung",
                eingang="Vermoegensuebersicht, Verwertungsstand, Lohn- und Sozialversicherung, Loehne, Mietverhaeltnisse, schwebende Vertraege.",
                pruefung="Verwalterpflichten Paragrafen 80 ff. InsO; Erfuellungswahl Paragraf 103 InsO; Anfechtung Paragrafen 129 ff. InsO mit Ruecknahmewirkung Paragraf 143 InsO; Aussonderung Paragraf 47 InsO; Absonderung Paragrafen 49 ff. InsO; Aufrechnung Paragraf 94 InsO.",
                arbeitsprodukt="Verwertungs- und Anfechtungsmatrix mit Erfuellungswahl, Anfechtungstatbestaenden und Verwertungsplan.",
            ),
            WorkflowStation(
                title="Forderungsanmeldung und Tabellenpruefung",
                eingang="Forderungsanmeldungen, Tabellenfuehrung, Pruefungstermin, Rangfragen (nachrangige Glaeubiger Paragraf 39 InsO), Massegglaeubiger Paragraf 53 InsO, Aufrechnungserklaerungen.",
                pruefung="Forderungsanmeldung Paragrafen 174 ff. InsO; Rangfragen Paragraf 39 InsO; Bestreiten Paragraf 178 InsO; Tabellenfeststellungsklage Paragraf 180 InsO; Masseunzulaenglichkeit Paragraf 208 InsO; Massearmut Paragraf 207 InsO.",
                arbeitsprodukt="Tabellenvermerk mit Rangzuordnung, bestrittenen Forderungen und Anschluss in Tabellenfeststellungsklage.",
            ),
            WorkflowStation(
                title="Insolvenzplan und StaRUG",
                eingang="Planentwurf (darstellender und gestaltender Teil), Glaeubigergruppen, Vergleichsrechnung, Sanierungskonzept, Restrukturierungsbeauftragter, Stabilisierungs- und Restrukturierungsrahmen.",
                pruefung="Insolvenzplan Paragrafen 217 ff. InsO; Gruppenbildung Paragraf 222 InsO; Mehrheitserfordernis Paragraf 244 InsO; Obstruktionsverbot Paragraf 245 InsO; Schlechterstellungsverbot Paragraf 251 InsO; StaRUG Paragrafen 4 ff., 56 ff. (Restrukturierungsplan), 76 ff. (Stabilisierungsanordnung), 84 (Auflagen).",
                arbeitsprodukt="Planentwurf oder Eckpunktepapier mit Gruppenbildung, Vergleichsrechnung, Mehrheits- und Obstruktionspruefung sowie StaRUG-Anschluss.",
            ),
            WorkflowStation(
                title="Restschuldbefreiung und Verbraucherinsolvenz",
                eingang="Antrag auf Verfahrenseroeffnung und Restschuldbefreiung, Pfaendungstabelle, Versagungsantraege, Treuhaender, Wohlverhaltensperiode.",
                pruefung="Restschuldbefreiung Paragrafen 286 ff. InsO; Wohlverhaltensphase (drei Jahre seit 01.10.2020) Paragraf 287 Absatz 2 InsO; Versagung Paragraf 290 InsO; Insolvenzanfechtung im Verbraucherverfahren; auch Sperrfristen nach Paragraf 287a InsO.",
                arbeitsprodukt="Restschuldbefreiungsstrategie mit Pruefung der Versagungsgruende und Anschlussfristen.",
            ),
        ),
        pflichtnormen=(
            "Paragraf 13 InsO (Antrag)",
            "Paragraf 15a InsO (Antragspflicht)",
            "Paragraf 17 InsO (Zahlungsunfaehigkeit)",
            "Paragraf 18 InsO (drohende Zahlungsunfaehigkeit)",
            "Paragraf 19 InsO (Ueberschuldung)",
            "Paragraf 21 InsO (Sicherungsmassnahmen)",
            "Paragraf 27 InsO (Eroeffnungsbeschluss)",
            "Paragrafen 80, 87 InsO (Verwaltungsbefugnis)",
            "Paragraf 103 InsO (Erfuellungswahl)",
            "Paragrafen 129 bis 147 InsO (Insolvenzanfechtung)",
            "Paragraf 174 InsO (Forderungsanmeldung)",
            "Paragraf 178 InsO (Pruefung der Forderung)",
            "Paragraf 270d InsO (Schutzschirm)",
            "Paragrafen 217 ff. InsO (Insolvenzplan)",
            "Paragrafen 286 ff. InsO (Restschuldbefreiung)",
            "Paragrafen 4, 56, 73, 84 StaRUG",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "BGH", "IX ZR 134/10", "06.05.2010", "BGHZ 185, 305",
                "Zahlungsunfaehigkeit im Sinne des Paragraf 17 InsO liegt vor, wenn der Schuldner zehn Prozent oder mehr seiner faelligen Gesamtverbindlichkeiten nicht innerhalb von drei Wochen erfuellen kann; eine geringere Liquiditaetsluecke wird nicht als Zahlungsunfaehigkeit angenommen.",
            ),
            Leitentscheidung(
                "BGH", "IX ZR 65/14", "12.02.2015", "NJW 2015, 1244",
                "Bei der Vorsatzanfechtung nach Paragraf 133 InsO genuegt fuer den Glaeubigerbenachteiligungsvorsatz, dass der Schuldner die Zahlungsunfaehigkeit erkannt hat oder ein bevorstehender Zusammenbruch konkrete Bedeutung erlangt hat; die Kenntnis des Anfechtungsgegners ist in der Regel zu vermuten, wenn ihm die drohende Zahlungsunfaehigkeit bekannt war.",
            ),
            Leitentscheidung(
                "BGH", "IX ZR 105/19", "06.05.2021", "NJW 2021, 1900",
                "Nach Inkrafttreten des Sanierungs- und Insolvenzrechtsfortentwicklungsgesetzes verkuerzt sich der Anfechtungszeitraum nach Paragraf 133 InsO regelmaessig auf vier Jahre und es ist im Rahmen der Glaeubigerbenachteiligungsabsicht zu beruecksichtigen, ob die Anfechtungslage gerade aus dem Stundungsverhalten zu einem konkreten Glaeubiger folgt.",
            ),
            Leitentscheidung(
                "BGH", "IX ZB 50/00", "08.11.2007", "BGHZ 174, 228",
                "Eine zur Erfuellung der Forderung im Insolvenzverfahren angemeldete Forderung ist nach Paragraf 178 InsO nach Grund, Hoehe und Rang konkret zu pruefen; die Eintragung in die Tabelle hat fuer eine rechtskraeftige Forderung Wirkung wie ein Urteil Paragraf 178 Absatz 3 InsO.",
            ),
            Leitentscheidung(
                "BGH", "IX ZB 86/14", "07.05.2015", "NZI 2015, 656",
                "Die Aufnahme eines Insolvenzplans Paragrafen 217 ff. InsO setzt eine sachgerechte Gruppenbildung Paragraf 222 InsO voraus; eine willkuerliche oder offensichtlich unangemessene Gruppenbildung ist zu beanstanden und vom Gericht zurueckzuweisen.",
            ),
            Leitentscheidung(
                "BGH", "IX ZB 25/21", "13.07.2023", "ZIP 2023, 1772",
                "Im StaRUG-Restrukturierungsverfahren ist der Restrukturierungsbeauftragte nach Paragraf 73 StaRUG nicht als gerichtlicher Verwalter zu verstehen, sondern als Funktionstraeger zur Sicherung des Verfahrensverlaufs; seine Vergueteung folgt eigenstaendigen Grundsaetzen.",
            ),
        ),
        pruefraster=(
            "Welcher Eroeffnungsgrund Paragrafen 17, 18, 19 InsO liegt vor, und wann ist er eingetreten?",
            "Welche Anfechtungstatbestaende Paragrafen 129 ff. InsO sind anwendbar, und welche Frist gilt?",
            "Welche Forderungsgruppen sind im Plan zu bilden, und welche Mehrheit ist erforderlich?",
            "Welche Sicherungsmassnahmen Paragraf 21 InsO sind angeordnet oder zu beantragen?",
            "Welche Wahl (Insolvenzverfahren, Eigenverwaltung, Schutzschirm, StaRUG) ist sachgerecht?",
        ),
        skelette=(
            "Insolvenzantrag: Schuldner, Antrag, Insolvenzgrund (Paragraf 17 oder 19 InsO), Vermoegensuebersicht, Glaeubigerverzeichnis, Stellungnahmen.",
            "Anfechtungsklage Paragrafen 129 ff. InsO: Anfechtungsgrund, Glaeubigerbenachteiligung, Subjektive Voraussetzungen, Anfechtungszeitraum, Antrag.",
            "Insolvenzplan: Darstellender Teil (Sachverhalt, Insolvenzgrund, Sanierungsstrategie), gestaltender Teil (Gruppenbildung, Quoten, Massnahmen), Anlagen Paragrafen 229 ff. InsO.",
        ),
    ))


_register_insolvenz()


def _register_datenschutz_ki() -> None:
    register(Themenprofil(
        key="datenschutz-ki",
        label="Datenschutz und KI-Verordnung",
        rolle="Du arbeitest im datenschutz- und KI-rechtlichen Modus: Verarbeitungstaetigkeiten, Rechtsgrundlagen, Betroffenenrechte, Auftragsverarbeitung, Drittlandtransfer, Datenpanne und KI-VO werden mit Risikoabwaegung und Aufsichtsprozess verbunden.",
        stop_kriterien=(
            "72-Stunden-Frist Datenpanne Artikel 33 DSGVO laeuft.",
            "Aufsichtsbescheid mit Bussgeldandrohung Artikel 83 DSGVO im Raum.",
            "Drittlandtransfer ohne Angemessenheitsbeschluss, SCCs oder TIA.",
            "Hochrisiko-KI Artikel 6 KI-VO ohne Konformitaetspruefung.",
            "Profiling oder automatisierte Entscheidung Artikel 22 DSGVO ohne Schutzmechanismus.",
            "Beschaeftigtendatenverarbeitung Paragraf 26 BDSG ohne Betriebsvereinbarung oder Einwilligung.",
        ),
        stationen=(
            WorkflowStation(
                title="Verarbeitungs- und Verfahrensanalyse",
                eingang="Verarbeitungsverzeichnis, Geschaeftsprozess, Datenfluss, Empfaengerkreise, Loeschfristen, Datenkategorien, betroffene Personen.",
                pruefung="Rolle Verantwortlicher oder Auftragsverarbeiter Artikel 4 DSGVO; Pflicht zur Fuehrung Verzeichnis Artikel 30 DSGVO; Verarbeitungsphasen; Datenminimierung Artikel 5 Absatz 1 Buchstabe c DSGVO; Speicherbegrenzung Artikel 5 Absatz 1 Buchstabe e DSGVO.",
                arbeitsprodukt="Verfahrensvermerk mit Rolle, Zweck, Datenkategorien, Empfaengern und Loeschfristen.",
            ),
            WorkflowStation(
                title="Rechtsgrundlage und Interessenabwaegung",
                eingang="Einwilligungstexte, Vertraege, gesetzliche Aufgaben, berechtigte Interessen, Drittlandtransfer, Tarifwerke.",
                pruefung="Rechtsgrundlage Artikel 6 DSGVO; besondere Kategorien Artikel 9 DSGVO; Beschaeftigtendatenschutz Paragraf 26 BDSG; Einwilligung Artikel 7 DSGVO mit Freiwilligkeitspruefung; Interessenabwaegung Artikel 6 Absatz 1 Buchstabe f DSGVO.",
                arbeitsprodukt="Rechtsgrundlage- und Interessenabwaegungsvermerk mit Pruefungslogik und Hinweis auf Erforderlichkeit.",
            ),
            WorkflowStation(
                title="Betroffenenrechte und Pflichteninformation",
                eingang="Auskunfts-, Loesch-, Berichtigungs-, Einschraenkungs-, Datenuebertragbarkeits- und Widerspruchsantraege, Datenschutzhinweise.",
                pruefung="Artikel 12 bis 22 DSGVO; Reaktionsfrist Artikel 12 Absatz 3 DSGVO (ein Monat); Identifizierung Artikel 12 Absatz 6 DSGVO; automatisierte Entscheidung Artikel 22 DSGVO; Informationspflichten Artikel 13, 14 DSGVO.",
                arbeitsprodukt="Antwortschreiben mit Datenauszug, Loeschmatrix oder Begruendung der Ablehnung mit Hinweis auf Aufsichtsbehoerde Artikel 77 DSGVO.",
            ),
            WorkflowStation(
                title="TOM, Datenpanne und Aufsicht",
                eingang="Vorfallmeldung, Risikoanalyse, Sicherheitsbericht, Verarbeitungsverzeichnis, TOM-Dokumente, Auditberichte, Aufsichtsanfragen.",
                pruefung="Sicherheit der Verarbeitung Artikel 32 DSGVO; Datenpanne Artikel 33, 34 DSGVO (72-Stunden-Frist); DSFA Artikel 35 DSGVO; Aufsichtsverfahren Artikel 58, 83 DSGVO; Bussgeldrahmen Artikel 83 Absaetze 4, 5 DSGVO.",
                arbeitsprodukt="Datenpannenmeldung, Stellungnahme an die Aufsichtsbehoerde, TOM-Pflichtenmatrix oder DSFA-Vermerk.",
            ),
            WorkflowStation(
                title="Drittland und Auftragsverarbeitung",
                eingang="Auftragsverarbeitungsvertraege, Drittlandtransfer, Standardvertragsklauseln, Transfer Impact Assessment, US-Cloud, BCR.",
                pruefung="Auftragsverarbeitung Artikel 28 DSGVO; Drittlandtransfer Artikel 44 bis 49 DSGVO; Standardvertragsklauseln; Transfer Impact Assessment nach Schrems II; Angemessenheitsbeschluesse; BCR Artikel 47 DSGVO.",
                arbeitsprodukt="Vertrags-, TIA- und Risikobericht mit Massnahmen und Eskalationspfad.",
            ),
            WorkflowStation(
                title="KI-VO-Konformitaet",
                eingang="KI-Anwendung, Risikoklassifizierung, Daten- und Modellbeschreibung, Konformitaetsdokumentation, Marktbeobachtung, Anbieter- oder Anwenderrolle.",
                pruefung="Anwendungsbereich KI-VO Artikel 2; verbotene Praktiken Artikel 5; Hochrisiko-KI Artikel 6 mit Annex III; Pflichten Anbieter Artikel 16 und Anwender Artikel 26; Daten Artikel 10; Transparenz Artikel 50; Marktueberwachung Artikel 73.",
                arbeitsprodukt="Konformitaetsmatrix mit Rolle, Risikoklasse, Pflichten, Massnahmen und Anschlusspruefung in Datenschutz und Produkthaftung.",
            ),
        ),
        pflichtnormen=(
            "Artikel 5 DSGVO (Grundsaetze)",
            "Artikel 6, 7 DSGVO (Rechtsgrundlage, Einwilligung)",
            "Artikel 9 DSGVO (besondere Kategorien)",
            "Artikel 12 bis 22 DSGVO (Betroffenenrechte)",
            "Artikel 26, 28 DSGVO (gemeinsame Verantwortung, Auftragsverarbeitung)",
            "Artikel 30 DSGVO (Verzeichnis von Verarbeitungstaetigkeiten)",
            "Artikel 32, 33, 34, 35 DSGVO (TOM, Datenpanne, DSFA)",
            "Artikel 44 bis 49 DSGVO (Drittlandtransfer)",
            "Artikel 58, 83 DSGVO (Aufsicht, Bussgeld)",
            "Paragrafen 26, 38 BDSG",
            "Artikel 5, 6, 10, 26, 50 KI-VO",
            "Artikel 16, 73 KI-VO (Anbieter, Marktueberwachung)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "EuGH", "C-311/18", "16.07.2020", "Schrems II",
                "Der Angemessenheitsbeschluss zum EU-US-Privacy-Shield ist ungueltig; Datenuebermittlungen in Drittlaender bleiben nur zulaessig, wenn ein im Wesentlichen gleichwertiges Schutzniveau gewaehrleistet ist, was im Einzelfall mit ergaenzenden Massnahmen sichergestellt und in einem Transfer Impact Assessment dokumentiert wird.",
            ),
            Leitentscheidung(
                "EuGH", "C-300/21", "04.05.2023", "UI gegen Oesterreichische Post",
                "Der Schadensersatzanspruch nach Artikel 82 DSGVO setzt einen Verstoss gegen die DSGVO, einen materiellen oder immateriellen Schaden und einen Kausalzusammenhang voraus; eine Erheblichkeitsschwelle ist nicht zu fordern, jedoch muss der Anspruchsteller den Schaden konkret darlegen.",
            ),
            Leitentscheidung(
                "EuGH", "C-340/21", "14.12.2023", "Natsionalna agentsia za prihodite",
                "Ein Datenleck begruendet Anspruch auf Schadensersatz nach Artikel 82 DSGVO, wenn aus der Pflichtverletzung ein konkreter materieller oder immaterieller Schaden folgt; die blosse Furcht vor zukuenftigem Missbrauch kann ausreichen, sofern sie auf objektiven Anhaltspunkten beruht.",
            ),
            Leitentscheidung(
                "BGH", "VI ZR 1295/20", "15.11.2022", "BGHZ 235, 81",
                "Eine Verletzung des Auskunftsrechts nach Artikel 15 DSGVO kann einen ersatzfaehigen immateriellen Schaden begruenden; die Hoehe des Schadensersatzes orientiert sich an einer Verhaltenssteuerung gegenueber dem Verantwortlichen und an der Schwere des Verstosses.",
            ),
            Leitentscheidung(
                "BVerwG", "6 C 6.18", "27.03.2019", "BVerwGE 165, 1",
                "Aufsichtsbehoerdliche Anordnungen nach Artikel 58 DSGVO sind Verwaltungsakte und unterliegen vollstaendiger gerichtlicher Pruefung; die Aufsichtsbehoerde traegt die Darlegungslast fuer den Verstoss und die Verhaeltnismaessigkeit der Anordnung.",
            ),
            Leitentscheidung(
                "EuGH", "C-203/22", "07.12.2023", "Dun & Bradstreet Austria",
                "Eine vollstaendig automatisierte Entscheidung im Sinne des Artikel 22 DSGVO setzt voraus, dass ein menschlicher Bearbeiter keine eigenstaendige Entscheidung treffen kann; bei algorithmenbasierten Risikoanalysen ist transparent zu machen, welche Daten und welche Logik die Entscheidung tragen.",
            ),
        ),
        pruefraster=(
            "Welche Datenkategorien werden zu welchem Zweck mit welcher Rechtsgrundlage verarbeitet?",
            "Welche TOM, welche DSFA, welche Vertraege sind vorhanden, welche fehlen?",
            "Welche Drittlandtransfer-Konstellation liegt vor, und welche Massnahmen sind dokumentiert?",
            "Welche Betroffenenrechte sind in welcher Frist zu beantworten?",
            "Welche KI-Anwendung ist im Einsatz, und welche Pflichten der KI-VO greifen?",
        ),
        skelette=(
            "Datenpannenmeldung Artikel 33 DSGVO: Vorfall, betroffene Datenkategorien, Massnahmen, Kontaktstelle, Folgen.",
            "Auskunftsantwort Artikel 15 DSGVO: Identitaet, Datenkategorien, Empfaenger, Speicherdauer, Herkunft, Rechte, ggf. Ablehnungsgruende.",
            "KI-Konformitaetsdokumentation Artikel 6 KI-VO: Anwendung, Risikoklasse, Daten, Tests, Transparenz, Marktueberwachung.",
        ),
    ))


_register_datenschutz_ki()


def _register_gesellschaftsrecht_corporate() -> None:
    register(Themenprofil(
        key="gesellschaftsrecht-corporate",
        label="Gesellschaftsrecht, Corporate, Bank, Compliance",
        rolle="Du arbeitest im gesellschafts- und kapitalmarktrechtlichen Modus: Gruendung, Geschaeftsfuehrung, Haftung, Beschluesse, Anteilsuebertragung, M und A, Compliance, Geldwaeschepraevention und Hinweisgeberschutz werden mit Anteils-, Pflicht- und Anschlussfolgen verbunden.",
        stop_kriterien=(
            "Beschlussanfechtungsfrist nach Paragraf 246 AktG (ein Monat) laeuft.",
            "Antrag auf Eintragung mit Zwischenverfuegung im Handelsregister.",
            "Insolvenzantragspflicht Paragraf 15a InsO greift parallel.",
            "Berichtspflicht Paragraf 161 AktG (Entsprechenserklaerung) ueberfaellig.",
            "Insiderhandelsverdacht Paragraf 14 MAR / WpHG.",
            "Geldwaescheverdacht und Meldepflicht Paragraf 43 GwG.",
            "Hinweisgebermeldung HinSchG mit interner Frist (drei Monate) laeuft ab.",
        ),
        stationen=(
            WorkflowStation(
                title="Gesellschafts- und Beteiligtenstruktur",
                eingang="Gesellschaftsvertrag, Gesellschafterliste, Handelsregisterauszug, Beschluesse, Vertraege, Kapitalmassnahmen, Stimmrechte, Konsortialvereinbarungen.",
                pruefung="Rechtsform und Vertragsstruktur, Vertretungsregelung Paragrafen 35 GmbHG, 78 AktG; Stimmrechte; Vorzugsaktien Paragrafen 139 ff. AktG; Stimmbindungen; Kapitalmassnahmen Paragraf 182 AktG, Paragraf 55 GmbHG; Gesellschafterliste Paragraf 40 GmbHG.",
                arbeitsprodukt="Beteiligten- und Strukturuebersicht mit Vertretungs- und Stimmlage, Anteilen, Vertragsstand.",
            ),
            WorkflowStation(
                title="Geschaeftsfuehrer- und Organhaftung",
                eingang="Vorstands- oder Geschaeftsfuehrervertraege, Geschaeftsverteilungsplan, Aufsichtsratsbeschluesse, Sorgfaltsverletzungen, D-and-O-Police.",
                pruefung="Sorgfalt eines ordentlichen Geschaeftsmanns Paragraf 43 GmbHG, Paragraf 93 AktG; Business Judgment Rule; Haftung gegenueber Gesellschaft, Gesellschaftern und Dritten; Insolvenzhaftung Paragraf 64 GmbHG a. F. / Paragraf 15b InsO neu.",
                arbeitsprodukt="Pflicht- und Haftungsmatrix mit Risikoprofil, Versicherungsschutz und Anschlusspflichten im Beschlussfassungsprozess.",
            ),
            WorkflowStation(
                title="Beschluss und Anfechtung",
                eingang="Einladung, Tagesordnung, Beschlussvorlagen, Protokoll, Anwesenheit, Mehrheiten, Stimmrechtsausschluesse, Ad-hoc-Pflichten.",
                pruefung="Einberufungsfehler; Stimmrechtsausschluss Paragraf 47 Absatz 4 GmbHG, Paragraf 136 AktG; Treuepflicht Paragraf 705 BGB; Anfechtungsklage Paragraf 246 AktG; Nichtigkeit Paragraf 241 AktG; Beschlussfassung Paragraf 47 GmbHG.",
                arbeitsprodukt="Beschluss- oder Anfechtungsmatrix mit Antrag, Stimmlage, Fehlerprofil und Anschluss in Klage oder Beschlussersatz.",
            ),
            WorkflowStation(
                title="Anteilsuebertragung und M and A",
                eingang="Share-Purchase-Agreement, Due-Diligence-Berichte, MAC-Klauseln, Earn-Out, Garantien, Freistellungen, Closing-Konditionen.",
                pruefung="Form Paragraf 15 GmbHG (notarielle Beurkundung); Pflichtenkatalog Garantien, Freistellungen, MAC; Kartellrechtliche Anmeldepflicht Paragraf 35 GWB; Investitionspruefung Paragraf 55 AWG.",
                arbeitsprodukt="Vertragspruefliste oder Term Sheet mit Risiken, Sicherungsklauseln und Anschlusspruefungen (Wettbewerbs- und Investitionsanmeldung).",
            ),
            WorkflowStation(
                title="Bank, Kapitalmarkt, Compliance",
                eingang="Kreditvertraege, Sicherheiten, Wertpapierprospekte, Ad-hoc-Mitteilungen, Insider-Lists, MAR-Prozesse, Hinweisgebersystem.",
                pruefung="Bankaufsicht KWG, ZAG; Sicherheitenrecht (Pfand, Sicherungsuebereignung, Sicherungszession) Paragrafen 1204 ff. BGB; MAR Artikel 14, 15, 17; Insider-Lists Artikel 18 MAR; Hinweisgeberschutzgesetz; Geldwaeschepraevention GwG.",
                arbeitsprodukt="Compliance-Pruefliste mit Pflichten, Fristen, Dokumentationspflichten und Anschlussverantwortung in der Eskalationskette.",
            ),
            WorkflowStation(
                title="Hauptversammlung und Rechnungslegung",
                eingang="Geschaeftsbericht, Lagebericht, Pruefungsbericht, Hauptversammlung, Entlastung, Dividendenbeschluss, Entsprechenserklaerung Paragraf 161 AktG.",
                pruefung="Pflichtangaben Hauptversammlung Paragrafen 121 ff. AktG; Rechnungslegung HGB-Bilanzrichtlinien-Gesetz; Pruefung Paragrafen 316 ff. HGB; Lagebericht Paragraf 289 HGB; Pruefungsausschuss Paragraf 107 Absatz 4 AktG; ESG/CSRD-Berichtspflichten.",
                arbeitsprodukt="HV-Vorbereitung, Beschlussvorschlag, Entlastungspruefung, Berichtspflichtmatrix mit Anschlusspflichten.",
            ),
        ),
        pflichtnormen=(
            "Paragraf 35 GmbHG (Vertretung)",
            "Paragraf 40 GmbHG (Gesellschafterliste)",
            "Paragraf 43 GmbHG (Sorgfalt)",
            "Paragraf 47 GmbHG (Beschluss)",
            "Paragraf 78 AktG (Vorstand)",
            "Paragraf 93 AktG (Organhaftung)",
            "Paragraf 121 AktG (Einberufung HV)",
            "Paragraf 136 AktG (Stimmrechtsverbote)",
            "Paragraf 161 AktG (Entsprechenserklaerung)",
            "Paragrafen 241, 243, 246, 249 AktG (Nichtigkeit, Anfechtung)",
            "Paragraf 15 GmbHG (Anteilsuebertragung)",
            "Paragraf 35 GWB (Zusammenschlusskontrolle)",
            "Paragrafen 14, 15, 17, 18 MAR (Insider, Ad-hoc, Insider-Lists)",
            "Paragrafen 43, 53 GwG (Verdachtsmeldung, Kundenidentifikation)",
            "Paragrafen 17, 33 HinSchG (interne Meldestellen, Schutz)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "BGH", "II ZR 175/19", "20.07.2021", "BGHZ 230, 217",
                "Die Haftung des GmbH-Geschaeftsfuehrers nach Paragraf 43 GmbHG fuer Zahlungen nach Insolvenzreife wird nach dem 31.12.2020 durch Paragraf 15b InsO geregelt; danach haftet der Geschaeftsfuehrer fuer Zahlungen, die nicht mit der Sorgfalt eines ordentlichen und gewissenhaften Geschaeftsleiters vereinbar sind, der Insolvenzgrund war erkennbar oder dem Geschaeftsfuehrer bekannt.",
            ),
            Leitentscheidung(
                "BGH", "II ZR 244/09", "21.06.2010", "BGHZ 186, 60",
                "Die Business Judgment Rule des Paragraf 93 Absatz 1 Satz 2 AktG schuetzt unternehmerische Entscheidungen, wenn der Vorstand auf Grundlage angemessener Information und unter ausschliesslich am Wohl der Gesellschaft orientierten Massstaeben gehandelt hat; die Beweislast fuer das Vorliegen der Voraussetzungen traegt der in Anspruch genommene Vorstand.",
            ),
            Leitentscheidung(
                "BGH", "II ZR 245/03", "10.10.2005", "BGHZ 164, 249",
                "Der Treuepflichtverstoss eines Gesellschafters bei der Beschlussfassung kann zur Nichtigkeit oder Anfechtbarkeit des Beschlusses fuehren; die Treuepflicht wirkt auch zwischen den Gesellschaftern und konkretisiert sich nach Mehrheits- oder Minderheitsstellung.",
            ),
            Leitentscheidung(
                "BGH", "II ZR 84/13", "20.05.2014", "BGHZ 201, 252",
                "Die Anfechtungsklage nach Paragraf 246 AktG ist eine Gestaltungsklage; sie muss innerhalb der Monatsfrist erhoben werden und das Beschluessergebnis konkret bezeichnen; eine nachtraegliche Ergaenzung der Anfechtungsgruende ist nur innerhalb der Frist moeglich.",
            ),
            Leitentscheidung(
                "BVerfG", "1 BvR 953/06", "07.09.2010", "BVerfGE 127, 87",
                "Die Mitbestimmung der Arbeitnehmer im Aufsichtsrat von Kapitalgesellschaften nach dem MitbestG ist verfassungskonform; sie greift in die Eigentumsfreiheit ein, ist aber durch die Sozialbindung des Eigentums Artikel 14 Absatz 2 GG gerechtfertigt.",
            ),
            Leitentscheidung(
                "EuGH", "C-263/22", "21.12.2023", "Banca Comerciala Romana",
                "Die Pflicht zur Geldwaeschepraevention nach der vierten Geldwaescherichtlinie ist im Lichte der EU-Grundrechte auszulegen; die Schwelle fuer einen Verdacht muss konkret und auf objektive Anhaltspunkte gestuetzt sein, blosse Pauschalverdachte sind unzureichend.",
            ),
        ),
        pruefraster=(
            "Welche Rechtsform und Vertretung liegt vor, und welche Pflichten erwachsen daraus?",
            "Welche Beschlussfehler (formell und materiell), welche Stimmrechtsverbote und welche Treuepflichten sind beruehrt?",
            "Welche Anmeldungs- und Eintragungspflichten (Handelsregister, Gesellschafterliste, Transparenzregister) sind ausgeloest?",
            "Welche Compliance-Pflichten (MAR, GwG, HinSchG, KAGB, KWG) sind anwendbar und einzuhalten?",
            "Welches Endprodukt (Beschluss, Anfechtungsklage, Vertragsentwurf, Anmeldung, Compliance-Report) ist gefragt?",
        ),
        skelette=(
            "Anfechtungsklage Paragraf 246 AktG: Antrag, Aktivlegitimation, Anfechtungsfrist, Beschluss, formelle und materielle Anfechtungsgruende.",
            "Anmeldung Handelsregister: Anmeldepflichtige, Gegenstand, beigefuegte Urkunden, Versicherungen nach Paragraf 8 GmbHG bzw. Paragraf 37 AktG.",
            "Compliance-Vermerk: Sachverhalt, betroffene Vorschriften (MAR, GwG, HinSchG), Pflichtenkatalog, Massnahmen, Fristen.",
        ),
    ))


_register_gesellschaftsrecht_corporate()


def _register_steuerrecht() -> None:
    register(Themenprofil(
        key="steuerrecht",
        label="Steuerrecht und Steuerverfahren",
        rolle="Du arbeitest im steuerrechtlichen Mandats- und Verfahrensmodus: Steuerbescheid, Einspruch, Aussetzung der Vollziehung, Aussenpruefung, Schaetzungs- und Verprobungsmethoden, Finanzgerichtsverfahren und Selbstanzeige werden mit Mitwirkungs- und Beweislastlage verbunden.",
        stop_kriterien=(
            "Einspruchsfrist Paragraf 355 AO (ein Monat ab Bekanntgabe) laeuft.",
            "Klagefrist Paragraf 47 FGO (ein Monat ab Einspruchsentscheidung) laeuft.",
            "Aussetzung der Vollziehung Paragraf 361 AO oder Paragraf 69 FGO erforderlich.",
            "Strafrechtlicher Anfangsverdacht Paragraf 152 Absatz 2 StPO i. V. m. Paragrafen 369 ff. AO.",
            "Selbstanzeige Paragraf 371 AO mit Vollstaendigkeitsgebot drohend.",
            "Aussenpruefungsanordnung Paragraf 196 AO und Sperrwirkung Paragraf 371 Absatz 2 Nummer 1 AO.",
        ),
        stationen=(
            WorkflowStation(
                title="Bescheid- und Rechtsbehelfslage",
                eingang="Steuerbescheide, Einspruchsentscheidungen, Mitteilungen, Korrekturbescheide, Verwaltungsakte, Bekanntgabe.",
                pruefung="Wirksamkeit Paragraf 124 AO; Bekanntgabe Paragraf 122 AO; Korrekturnormen Paragrafen 129, 164, 165, 172 ff., 173, 174 AO; Vorbehalt der Nachpruefung Paragraf 164 AO; Aenderung wegen neuer Tatsachen Paragraf 173 AO.",
                arbeitsprodukt="Bescheidanalyse mit Korrekturoptionen, Festsetzungsfrist und Anschluss in Einspruch oder Klage.",
            ),
            WorkflowStation(
                title="Sachverhalt und Mitwirkungspflichten",
                eingang="Buchfuehrung, Belege, Erklaerungen, Steuererklaerungen, Aufzeichnungen Paragraf 147 AO, Vertraege, Auslandsbezuege Paragraf 90 Absatz 2 AO.",
                pruefung="Mitwirkungspflichten Paragraf 90 AO; Schaetzung Paragraf 162 AO; Verprobung; Beweislast bei Steuerersparnis und Steuermehrung; Auslandssachverhalte Paragraf 90 Absatz 2 AO; Aufzeichnungspflichten Paragraf 147 AO.",
                arbeitsprodukt="Sachverhalts- und Belegmatrix mit Lueckenliste, Beweisangeboten und Schaetzungsabsicherung.",
            ),
            WorkflowStation(
                title="Einspruchs- und AdV-Verfahren",
                eingang="Einspruchsschreiben, Begruendung, AdV-Antrag, Belege, Stundungsantrag, Erlassantrag.",
                pruefung="Form und Frist Paragraf 355 AO; Antrag Paragraf 357 AO; Begruendetheit; AdV Paragraf 361 AO (ernstliche Zweifel oder unbillige Haerte); Erlass Paragraf 227 AO; Stundung Paragraf 222 AO.",
                arbeitsprodukt="Einspruchsbegruendung mit Tatsachen, Normen, Beweisangebot und Antrag (AdV, Erlass, Aenderung).",
            ),
            WorkflowStation(
                title="Aussenpruefung und tatsaechliche Verstaendigung",
                eingang="Pruefungsanordnung, Vorbereitungsfragen, Pruefungsfeststellungen, tatsaechliche Verstaendigung, Schlussbesprechung, Selbstanzeige.",
                pruefung="Pruefungsanordnung Paragrafen 193, 196 AO; Mitwirkung Paragraf 200 AO; tatsaechliche Verstaendigung BFH-Rechtsprechung; Schaetzung Paragraf 162 AO; Verprobungsmethoden (Geldverkehrsrechnung, Zeitreihenvergleich, Quantilsschaetzung).",
                arbeitsprodukt="Stellungnahme zur Pruefungsanordnung, Vermerk tatsaechliche Verstaendigung, Argumentation gegen Schaetzungsmethode.",
            ),
            WorkflowStation(
                title="Finanzgerichtsverfahren",
                eingang="Einspruchsentscheidung, Klage, AdV-Antrag, Beweisangebote, Beiladung, Bundesfinanzhof Revision.",
                pruefung="Klagearten Paragraf 40 FGO; Klagefrist Paragraf 47 FGO; Klagebefugnis Paragraf 40 Absatz 2 FGO; Aufklaerungspflicht Paragraf 76 FGO; Beweiswuerdigung Paragraf 96 FGO; Revision Paragrafen 115 ff. FGO; Aussetzung der Vollziehung Paragraf 69 FGO.",
                arbeitsprodukt="Klage- oder Revisionsbaustein mit Antrag, Sachverhalt, rechtlicher Wuerdigung, Beweisangebot und Antrag auf AdV.",
            ),
            WorkflowStation(
                title="Steuerstraf- und Selbstanzeigerecht",
                eingang="Anhaltspunkte fuer Steuerverkuerzung, Steuerstrafverfahren, Selbstanzeige, Nachzahlungsbedarf, Sperrwirkungen Paragraf 371 Absatz 2 AO.",
                pruefung="Steuerhinterziehung Paragraf 370 AO; Selbstanzeige Paragraf 371 AO mit Vollstaendigkeitsgebot, Sperrwirkungen, Nachzahlung; leichtfertige Steuerverkuerzung Paragraf 378 AO; Strafzumessung Paragraf 46 StGB.",
                arbeitsprodukt="Selbstanzeige oder Verteidigungsstrategie mit Steuerberechnung, Nachzahlungsplan und Anschluss in Steuerstrafverfahren.",
            ),
        ),
        pflichtnormen=(
            "Paragraf 88 AO (Untersuchungsgrundsatz)",
            "Paragraf 90 AO (Mitwirkung)",
            "Paragraf 122 AO (Bekanntgabe)",
            "Paragraf 124 AO (Wirksamkeit)",
            "Paragraf 147 AO (Aufbewahrung)",
            "Paragraf 162 AO (Schaetzung)",
            "Paragraf 164 AO (Vorbehalt der Nachpruefung)",
            "Paragrafen 172, 173 AO (Korrektur)",
            "Paragraf 196 AO (Pruefungsanordnung)",
            "Paragraf 200 AO (Mitwirkung in der Pruefung)",
            "Paragraf 227 AO (Erlass)",
            "Paragraf 233a AO (Verzinsung)",
            "Paragraf 355 AO (Einspruchsfrist)",
            "Paragraf 361 AO (AdV)",
            "Paragrafen 370, 371, 378 AO (Steuerstrafrecht)",
            "Paragraf 47 FGO (Klagefrist)",
            "Paragraf 76 FGO (Aufklaerungspflicht)",
            "Paragraf 96 FGO (freie Beweiswuerdigung)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "BFH", "X R 19/17", "12.06.2019", "BFHE 265, 254",
                "Eine Schaetzung nach Paragraf 162 AO ist nur dann sachgerecht, wenn das Finanzamt die Schaetzungsmethode begruendet und sich an den wahrscheinlich zutreffenden Werten orientiert; eine reine Sicherheitszuschlag-Schaetzung ohne Methodendarstellung ist regelmaessig ermessensfehlerhaft.",
            ),
            Leitentscheidung(
                "BFH", "XI R 25/19", "11.12.2020", "BFHE 271, 481",
                "Die Pflichtangabe der vollstaendigen Anschrift des leistenden Unternehmers in einer Rechnung im Sinne des Paragraf 14 UStG ist erfuellt, wenn der Unternehmer unter dieser Anschrift erreichbar ist; eine wirtschaftliche Aktivitaet am Sitz wird nicht gefordert.",
            ),
            Leitentscheidung(
                "BFH", "VIII R 30/13", "23.10.2019", "BFHE 266, 526",
                "Die Selbstanzeige nach Paragraf 371 AO ist nur dann wirksam, wenn sie saemtliche steuerlich relevanten Sachverhalte einer Steuerart vollstaendig und zutreffend offenbart; eine sogenannte Teilselbstanzeige fuehrt zur Unwirksamkeit und damit zur Fortdauer der Strafbarkeit.",
            ),
            Leitentscheidung(
                "BVerfG", "1 BvR 2433/17", "27.06.2018", "BVerfGE 149, 1",
                "Die Verzinsung von Steuernachforderungen nach Paragraf 233a AO mit einem starren Zinssatz von sechs Prozent jaehrlich ist seit dem Veranlagungszeitraum 2014 nicht mehr mit Artikel 3 Absatz 1 GG vereinbar; der Gesetzgeber hat den Zinssatz anzupassen.",
            ),
            Leitentscheidung(
                "BFH", "GrS 1/15", "12.06.2018", "BFHE 261, 543",
                "Die finale Verlustnutzung eines auslaendischen Betriebsstaettenverlusts setzt voraus, dass eine Verlustnutzung im anderen Mitgliedstaat aus rechtlichen oder tatsaechlichen Gruenden endgueltig ausgeschlossen ist; die Beweislast traegt der Steuerpflichtige.",
            ),
            Leitentscheidung(
                "BGH", "1 StR 416/08", "02.12.2008", "BGHSt 53, 71",
                "Bei der Strafzumessung wegen Steuerhinterziehung Paragraf 370 AO ist die Hoehe der hinterzogenen Steuern ein wesentlicher Strafzumessungsumstand; ab einer Hoehe von 50.000 Euro indiziert das einen besonders schweren Fall, ab 1.000.000 Euro ist regelmaessig eine Freiheitsstrafe ohne Bewaehrung angezeigt.",
            ),
        ),
        pruefraster=(
            "Welcher Verfahrensstand (Festsetzung, Einspruch, Klage, Revision, Steuerstrafverfahren) liegt vor?",
            "Welche Korrekturnorm Paragrafen 129, 164, 165, 172 bis 175 AO ist anwendbar?",
            "Welche Mitwirkungs- und Aufzeichnungspflichten Paragrafen 90, 147 AO sind erfuellt oder verletzt?",
            "Welche Schaetzungsmethode ist herangezogen, und ist sie sachgerecht und begruendet?",
            "Welche strafrechtlichen Implikationen (Paragrafen 370, 371, 378 AO) bestehen?",
        ),
        skelette=(
            "Einspruchsbegruendung: Einspruchsfuehrer, Bescheid, Frist, Sachverhalt, rechtliche Wuerdigung, Antrag (AdV, Aenderung), Anlagen.",
            "Klage Finanzgericht: Klageantrag, Klagebefugnis Paragraf 40 FGO, Klagefrist, Beweisangebote, Anregung AdV nach Paragraf 69 FGO.",
            "Selbstanzeige Paragraf 371 AO: Steuerart, Veranlagungszeitraeume, Sachverhalt, korrekte Besteuerungsgrundlagen, Nachzahlungsplan.",
        ),
    ))


_register_steuerrecht()


def _register_sozialrecht() -> None:
    register(Themenprofil(
        key="sozialrecht",
        label="Sozialrecht (SGB, Widerspruch, Sozialgericht)",
        rolle="Du arbeitest in einem sozialrechtlichen Werkstatt-Modus: Leistungsbescheid pruefen, Anspruchsvoraussetzungen subsumieren, Widerspruch oder Klage zum Sozialgericht vorbereiten, Untaetigkeitsklage und einstweiligen Rechtsschutz im Blick halten.",
        stop_kriterien=(
            "Notfrist (Widerspruchs- oder Klagefrist Paragraf 84, 87 SGG, Untaetigkeitsklage Paragraf 88 SGG, einstweilige Anordnung Paragraf 86b SGG).",
            "Existenzsichernde Leistungen unterbrochen (SGB II, SGB XII): Eilrechtsschutz pruefen.",
            "Heilbehandlung unaufschiebbar (SGB V): Genehmigungsfiktion Paragraf 13 Absatz 3a SGB V pruefen.",
            "Schwerbehinderung, Pflegestufe oder Erwerbsminderung mit unmittelbarer Auswirkung auf Existenz oder Arbeitsplatz.",
            "Sozialdaten in ungesichertem System (Paragraf 35 SGB I, Paragrafen 67 ff. SGB X).",
        ),
        stationen=(
            WorkflowStation(
                title="Bescheidaufnahme und Fristbild",
                eingang="Leistungsbescheid, Widerspruchsbescheid, Aufhebungs- oder Erstattungsbescheid, Antragsunterlagen, Atteste, Gutachten, Versicherungsverlauf, Rentenbescheid.",
                pruefung="Adressat, Behoerde, Bescheidart (Leistung, Aufhebung, Erstattung, Sanktion), Rechtsbehelfsbelehrung Paragraf 36 SGB X, Bekanntgabe Paragraf 37 SGB X, Frist Paragraf 84 SGG; Sachverhalt aus Aktenlage trennen.",
                arbeitsprodukt="Aktenuebersicht mit Bescheidart, Datum, Frist, beteiligter Behoerde und identifizierten Streitpunkten.",
            ),
            WorkflowStation(
                title="Anspruchspruefung nach Buch",
                eingang="Einschlaegiges Sozialgesetzbuch (SGB II, III, V, VI, VII, IX, XI, XII), Leistungsart, persoenliche und sachliche Voraussetzungen, Beduerftigkeits- oder Versicherungslage.",
                pruefung="Anspruchsgrundlage benennen (z. B. Paragraf 19 SGB II Buergergeld, Paragrafen 27, 41 SGB V Krankenbehandlung, Paragrafen 43, 50 SGB VI Erwerbsminderung); Mitwirkung Paragrafen 60 ff. SGB I; Beweislast bei amtsermittelnder Behoerde Paragraf 20 SGB X.",
                arbeitsprodukt="Anspruchsraster mit Tatbestandsmerkmalen, Belegen aus Bescheid und Akte, Zwischenergebnis.",
            ),
            WorkflowStation(
                title="Aufhebungs- und Erstattungsrecht",
                eingang="Aufhebungsbescheid, Erstattungsbescheid, Sanktionsbescheid, Verschuldensvorwurf, Kenntnis der Behoerde.",
                pruefung="Vertrauensschutz Paragraf 45 SGB X, Aenderung der Verhaeltnisse Paragraf 48 SGB X, Erstattung Paragraf 50 SGB X, Wiederaufnahme Paragraf 44 SGB X; Anhoerung Paragraf 24 SGB X; Ermessen ausgeuebt?",
                arbeitsprodukt="Pruefraster Aufhebung/Erstattung mit Norm, Subsumtion, Vertrauensschutzbewertung.",
            ),
            WorkflowStation(
                title="Widerspruch und Klage",
                eingang="Bescheid, Frist, Begruendungsstand, Gutachtenlage, Beweisangebote, Atteste, sozialmedizinische Stellungnahmen.",
                pruefung="Widerspruchsbegruendung Paragrafen 83 ff. SGG; Klage zum Sozialgericht Paragrafen 87, 90 SGG; Klagearten Paragrafen 54, 55 SGG (Anfechtungs-, Verpflichtungs-, Leistungs-, Feststellungsklage); einstweiliger Rechtsschutz Paragraf 86b SGG; Untaetigkeitsklage Paragraf 88 SGG.",
                arbeitsprodukt="Widerspruchs- oder Klageschriftkern mit Antrag, Begruendung, Beweisangeboten, Hilfsantrag und Anregung Eilrechtsschutz.",
            ),
            WorkflowStation(
                title="Beweisaufnahme und Gutachten",
                eingang="Sozialmedizinische Gutachten, Atteste, Reha-Berichte, Berufsanamnese, Gutachtenauswahl Paragrafen 106, 109 SGG.",
                pruefung="Amtsermittlungspflicht Paragraf 103 SGG; eigenes Antragsrecht des Klaegers Paragraf 109 SGG (Sachverstaendiger der Wahl); freie Beweiswuerdigung Paragraf 128 SGG.",
                arbeitsprodukt="Beweisplan mit Sachverstaendigenantraegen, Befundlisten und Strategie fuer muendliche Verhandlung.",
            ),
            WorkflowStation(
                title="Arbeitsprodukt und Folgeschritte",
                eingang="Zielprodukt (Widerspruchsschrift, Klageschrift, Eilantrag, Stellungnahme, Mandanteninformation), Zustaendigkeit, Adressat.",
                pruefung="Pflichtangaben, Bezeichnung des Bescheides, Antrag, Begruendung, Beweisangebot, Hilfsantraege, Beiziehung der Verwaltungsakte Paragraf 119 SGG; PKH-Antrag Paragraf 73a SGG.",
                arbeitsprodukt="Vollstaendiges Schriftstueck mit Anschlussplan: Akteneinsicht Paragraf 25 SGB X, Sachverstaendigenantraege, Termin, Vergleich.",
            ),
        ),
        pflichtnormen=(
            "Paragrafen 60 bis 67 SGB I (Mitwirkung, Sozialdaten)",
            "Paragrafen 44 bis 50 SGB X (Aufhebung, Vertrauensschutz, Erstattung)",
            "Paragraf 35 SGB X (Begruendung des Verwaltungsakts)",
            "Paragrafen 84, 87, 88, 90, 92 SGG (Vorverfahren, Klage)",
            "Paragraf 86b SGG (einstweiliger Rechtsschutz)",
            "Paragrafen 54, 55 SGG (Klagearten)",
            "Paragrafen 103, 106, 109, 128 SGG (Amtsermittlung, Beweis)",
            "Paragraf 73a SGG in Verbindung mit Paragrafen 114 ff. ZPO (Prozesskostenhilfe)",
            "Paragrafen 19, 22, 24 SGB II (Buergergeld, Unterkunft, Mehrbedarf)",
            "Paragraf 13 Absatz 3a SGB V (Genehmigungsfiktion)",
            "Paragrafen 27, 39 SGB V (Krankenbehandlung, Krankenhaus)",
            "Paragrafen 43, 50, 96a SGB VI (Erwerbsminderung, Rente, Hinzuverdienst)",
            "Paragrafen 1, 152, 229 SGB IX (Schwerbehinderung, GdB, Nachteilsausgleich)",
            "Paragraf 14 SGB XI (Pflegegrad)",
            "Paragrafen 27, 41 SGB XII (Sozialhilfe, Grundsicherung im Alter)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "BSG", "B 1 KR 25/15 R", "08.03.2016", "BSGE 121, 40",
                "Die Genehmigungsfiktion nach Paragraf 13 Absatz 3a SGB V tritt ein, wenn die Krankenkasse nicht binnen drei Wochen entscheidet; der Versicherte erhaelt einen unbedingten Anspruch auf die beantragte Leistung, sofern sie nicht offensichtlich ausserhalb des Leistungskatalogs liegt.",
            ),
            Leitentscheidung(
                "BSG", "B 14 AS 17/14 R", "16.04.2015", "BSGE 119, 17",
                "Aufwendungen fuer Unterkunft und Heizung nach Paragraf 22 SGB II sind in Hoehe der tatsaechlichen Kosten zu uebernehmen, soweit sie angemessen sind; die Angemessenheit ist anhand eines schluessigen Konzepts zu bestimmen, das die Behoerde darzulegen hat.",
            ),
            Leitentscheidung(
                "BSG", "B 13 R 32/13 R", "03.09.2014", "SozR 4-2600 Paragraf 43 Nummer 21",
                "Eine volle Erwerbsminderung Paragraf 43 SGB VI setzt voraus, dass das Restleistungsvermoegen weniger als drei Stunden taeglich betraegt; massgeblich ist eine prognostische Gesamtbewertung der gesundheitlichen und sozialmedizinischen Situation.",
            ),
            Leitentscheidung(
                "BSG", "B 9 SB 2/15 R", "16.03.2016", "SozR 4-3250 Paragraf 69 Nummer 22",
                "Bei der Feststellung des Grades der Behinderung sind die Versorgungsmedizinischen Grundsaetze zugrundezulegen; einzelne Funktionsbeeintraechtigungen sind nach Massgabe der Wechselwirkung in einen Gesamt-GdB zu integrieren und nicht zu addieren.",
            ),
            Leitentscheidung(
                "BVerfG", "1 BvL 1/09", "09.02.2010", "BVerfGE 125, 175 (Regelleistungen)",
                "Der grundrechtliche Anspruch auf Gewaehrleistung eines menschenwuerdigen Existenzminimums aus Paragraf 1 Absatz 1 GG in Verbindung mit dem Sozialstaatsprinzip verpflichtet den Gesetzgeber, die Regelleistungen transparent, realitaetsgerecht und nachvollziehbar zu bemessen.",
            ),
        ),
        pruefraster=(
            "Welche Bescheidart liegt vor und welche Frist laeuft?",
            "Welche Anspruchsnorm aus welchem SGB greift, sind alle Tatbestandsmerkmale belegt?",
            "Wurde die Mitwirkung Paragrafen 60 ff. SGB I gewahrt?",
            "Bei Aufhebung/Erstattung: Vertrauensschutz und Ermessen geprueft?",
            "Ist einstweiliger Rechtsschutz oder Untaetigkeitsklage angezeigt?",
        ),
        skelette=(
            "Widerspruch: Bescheidbezeichnung, Frist, Antrag (Aufhebung, Verpflichtung), Begruendung mit Anspruchsraster, Beweisangebot, Akteneinsicht.",
            "Klage Sozialgericht: Klageantrag, Bescheidbezeichnung, Verfahrensstand, Sachverhalt, rechtliche Wuerdigung, Anregung Paragraf 109 SGG, PKH-Antrag.",
            "Eilantrag Paragraf 86b SGG: Anordnungsanspruch, Anordnungsgrund, Glaubhaftmachung, Folgenabwaegung.",
        ),
    ))


_register_sozialrecht()


def _register_sozialrecht_gericht() -> None:
    base = PROFILE["sozialrecht"]
    register(Themenprofil(
        key="sozialrecht-gericht",
        label="Sozialgerichtsbarkeit (richterlich)",
        rolle="Du arbeitest in der Rolle eines sozialgerichtlichen Spruchkoerpers (SG, LSG, BSG): Akte aus der Sphaere des Klaegers und der Behoerde sichten, Amtsermittlung steuern, Beweisbeschluss, muendliche Verhandlung und Urteil mit Tenor, Tatbestand, Entscheidungsgruenden, Kostenentscheidung und Streitwert vorbereiten.",
        stop_kriterien=base.stop_kriterien + (
            "Berichterstatterzustaendigkeit, Kammerbesetzung oder ehrenamtliche Richter unklar.",
            "Gutachten unverwertbar (Befangenheit, Methodik, fehlende Anknuepfung).",
        ),
        stationen=(
            WorkflowStation(
                title="Aktenstudium und Beweisbild",
                eingang="Verwaltungsakte, Klageschrift, Klageerwiderung, Replik, Gutachten, Bescheid und Widerspruchsbescheid, Streitwert.",
                pruefung="Zulaessigkeit der Klage Paragrafen 51, 54 bis 56 SGG; Statthaftigkeit der Klageart; Klagefrist Paragraf 87 SGG; Beweisbeduerftigkeit ermitteln; Amtsermittlung Paragraf 103 SGG planen.",
                arbeitsprodukt="Aktenvermerk mit Streitgegenstand, Zulaessigkeitspruefung und Beweisbedarf.",
            ),
            WorkflowStation(
                title="Beweisbeschluss",
                eingang="Befundberichte, gutachterliche Stellungnahmen, Beweisangebote der Beteiligten, Antrag Paragraf 109 SGG.",
                pruefung="Welche Tatsachen sind streitig und entscheidungserheblich? Welcher Beweis (Urkundenbeweis, Sachverstaendigenbeweis Paragraf 118 SGG, Augenscheinseinnahme) ist geeignet und erforderlich?",
                arbeitsprodukt="Beweisbeschluss mit Beweisthema, Beweismittel, Sachverstaendigenauswahl, Fristsetzung.",
            ),
            WorkflowStation(
                title="Muendliche Verhandlung",
                eingang="Beweisaufnahmeergebnis, Stellungnahmen der Beteiligten, ehrenamtliche Richter.",
                pruefung="Sachbericht durch Berichterstatter, Anhoerung der Beteiligten, Beweisaufnahme nach Paragraf 118 SGG in Verbindung mit Paragrafen 355 ff. ZPO; Vergleichsmoeglichkeit nach Paragraf 101 Absatz 1 SGG sondieren.",
                arbeitsprodukt="Sitzungsprotokoll mit Antraegen, Beweisaufnahme und etwaigem Vergleich.",
            ),
            WorkflowStation(
                title="Urteilsentwurf",
                eingang="Beweisaufnahmeergebnis, Rechtsauffassung des Spruchkoerpers, Streitwert, Kostenfrage.",
                pruefung="Tenor (Aufhebung, Verpflichtung, Leistung, Feststellung), Tatbestand mit unstreitigem und streitigem Sachverhalt, Entscheidungsgruende mit Subsumtion, Kostenentscheidung Paragrafen 183, 193 SGG, Rechtsmittelbelehrung.",
                arbeitsprodukt="Urteilsentwurf mit allen Pflichtangaben Paragraf 136 SGG, ggf. Anregung Sprungrevision Paragraf 161 SGG.",
            ),
        ),
        pflichtnormen=base.pflichtnormen + (
            "Paragrafen 51, 54, 55, 56 SGG (Rechtsweg, Klagearten, objektive Klagehaeufung)",
            "Paragrafen 103, 106, 109, 118, 128 SGG (Amtsermittlung, Beweis, Beweiswuerdigung)",
            "Paragrafen 136, 141 SGG (Urteil, Bindungswirkung)",
            "Paragrafen 143, 144, 160, 160a, 161 SGG (Berufung, Revision)",
            "Paragrafen 183, 184, 193, 197a SGG (Kosten, Streitwert)",
        ),
        leitentscheidungen=base.leitentscheidungen,
        pruefraster=base.pruefraster + (
            "Ist der Spruchkoerper besetzt und zustaendig (Paragrafen 12, 33, 40 SGG)?",
            "Welche Pflichtangaben braucht das Urteil nach Paragraf 136 SGG?",
        ),
        skelette=(
            "Beweisbeschluss: Beweisthema, Beweismittel, Sachverstaendiger, Frist, Ablehnungsgrund.",
            "Urteil SG: Rubrum, Tenor, Tatbestand, Entscheidungsgruende, Kostenentscheidung, Streitwert, Rechtsmittelbelehrung.",
            "Vergleichsprotokoll Paragraf 101 SGG mit Hauptsacheerledigung und Kostenfolge.",
        ),
    ))


_register_sozialrecht_gericht()


def _register_verwaltungsrecht() -> None:
    register(Themenprofil(
        key="verwaltungsrecht",
        label="Verwaltungsrecht (VwGO, VwVfG, Fachgesetze)",
        rolle="Du arbeitest in einem verwaltungsrechtlichen Werkstatt-Modus: Verwaltungsakt pruefen, Widerspruch oder Anfechtungs- und Verpflichtungsklage vorbereiten, einstweiligen Rechtsschutz Paragrafen 80, 123 VwGO im Blick, Fachgesetze (BauGB, BImSchG, GewO, AufenthG, BeamtStG) anwenden.",
        stop_kriterien=(
            "Klage- oder Antragsfrist Paragrafen 74, 70 VwGO laeuft.",
            "Sofortvollzug Paragraf 80 Absatz 2 VwGO angeordnet: Eilrechtsschutz pruefen.",
            "Aufenthaltsrechtliche oder asylrechtliche Notlage (Ausweisung, Abschiebung, Schubhaft).",
            "Beamten- oder berufsrechtliche Massnahme mit unmittelbarer Existenzfolge.",
            "Datenschutz- oder Geheimnisschutzbelange ungesichert.",
        ),
        stationen=(
            WorkflowStation(
                title="Verwaltungsaktanalyse",
                eingang="Bescheid, Anhoerungsschreiben, Antragsunterlagen, Behoerdenakte, Rechtsbehelfsbelehrung, Fachgesetze.",
                pruefung="Verwaltungsakt Paragraf 35 VwVfG (Massnahme, Aussenwirkung, Regelung, hoheitlich, Einzelfall); formelle Rechtmaessigkeit (Zustaendigkeit, Verfahren, Form); materielle Rechtmaessigkeit (Ermaechtigungsgrundlage, Tatbestand, Rechtsfolge, Ermessen Paragraf 40 VwVfG).",
                arbeitsprodukt="Aktenvermerk mit Bescheidqualifikation, formellen und materiellen Pruefpunkten.",
            ),
            WorkflowStation(
                title="Ermaechtigungsgrundlage",
                eingang="Spezialgesetz (BauGB Paragraf 35, BImSchG Paragraf 4, GewO Paragraf 35, AufenthG Paragrafen 5, 53), allgemeine Polizei- und Ordnungsgesetze, Auffangermaechtigung.",
                pruefung="Tatbestandsmerkmale subsumieren, unbestimmte Rechtsbegriffe konkretisieren, Beurteilungsspielraeume und Rechtsfolgenermessen unterscheiden, Verhaeltnismaessigkeit pruefen.",
                arbeitsprodukt="Pruefraster mit Norm, Tatbestand, Subsumtion und Ermessenspruefung.",
            ),
            WorkflowStation(
                title="Vorverfahren und Klage",
                eingang="Widerspruchsbescheid, Klagefrist, Klageart (Anfechtung Paragraf 42 Absatz 1 VwGO, Verpflichtung Paragraf 42 Absatz 1 VwGO, Feststellung Paragraf 43 VwGO, allgemeine Leistungsklage), Klagebefugnis Paragraf 42 Absatz 2 VwGO.",
                pruefung="Statthafte Klageart, Klagebefugnis, Vorverfahren Paragrafen 68 ff. VwGO, Klagefrist Paragraf 74 VwGO, Beteiligten- und Prozessfaehigkeit Paragrafen 61, 62 VwGO.",
                arbeitsprodukt="Klageschriftkern mit Antrag, Klagebefugnis, Begruendung, Beweisangeboten und Anregung Paragraf 80 Absatz 5 VwGO.",
            ),
            WorkflowStation(
                title="Einstweiliger Rechtsschutz",
                eingang="Sofortvollzug, Belastungswirkung, Ermessensentscheidung, einstweilige Anordnung.",
                pruefung="Antrag Paragraf 80 Absatz 5 VwGO (aufschiebende Wirkung) oder Paragraf 123 VwGO (einstweilige Anordnung); Erfolgsaussichten der Hauptsache, Folgenabwaegung, Anordnungsanspruch und Anordnungsgrund Paragraf 920 ZPO analog.",
                arbeitsprodukt="Antragsschrift mit Sachverhalt, Glaubhaftmachung, Antraegen und Hilfsantraegen.",
            ),
            WorkflowStation(
                title="Beweis, Akteneinsicht und Verhandlung",
                eingang="Verwaltungsakte, Stellungnahmen, Sachverstaendige, Zeugen, Augenschein, Urkunden.",
                pruefung="Amtsermittlung Paragraf 86 VwGO, Akteneinsicht Paragraf 100 VwGO, Beweismittel Paragrafen 96 ff. VwGO, freie Beweiswuerdigung Paragraf 108 VwGO.",
                arbeitsprodukt="Beweisplan und Verhandlungsstrategie mit Antraegen.",
            ),
            WorkflowStation(
                title="Arbeitsprodukt und Folgewirkung",
                eingang="Zielprodukt (Widerspruch, Klageschrift, Eilantrag, Stellungnahme, Vermerk), Adressat, Form Paragraf 81 VwGO.",
                pruefung="Pflichtangaben, Antrag, Begruendung, Beweisangebot, Hilfsantraege, Kostenfrage Paragrafen 154 ff. VwGO, Streitwert Paragraf 52 GKG.",
                arbeitsprodukt="Vollstaendiges Schriftstueck mit Anschlussplan (Akteneinsicht, Termin, Vergleich, Rechtsmittel).",
            ),
        ),
        pflichtnormen=(
            "Paragrafen 35, 36, 37, 39, 40, 41, 43, 44, 48, 49 VwVfG (Verwaltungsakt, Begruendung, Nebenbestimmungen, Ermessen, Bekanntgabe, Nichtigkeit, Aufhebung)",
            "Paragrafen 22 bis 30 VwVfG (Anhoerung, Akteneinsicht, Befangenheit)",
            "Paragrafen 42, 43, 47, 68 bis 75 VwGO (Klagearten, Normenkontrolle, Vorverfahren)",
            "Paragrafen 80, 80a, 123 VwGO (einstweiliger Rechtsschutz)",
            "Paragrafen 86, 96, 100, 108, 113 VwGO (Amtsermittlung, Beweis, Urteil)",
            "Paragrafen 124, 124a, 132, 137 VwGO (Berufung, Revision)",
            "Paragrafen 154 bis 167 VwGO (Kosten, Vollstreckung)",
            "Paragraf 52 GKG (Streitwert)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "BVerwG", "1 C 6.12", "10.07.2012", "BVerwGE 143, 277",
                "Bei der Anwendung unbestimmter Rechtsbegriffe ist die volle gerichtliche Kontrolle die Regel; ein behoerdlicher Beurteilungsspielraum kommt nur dort in Betracht, wo der Gesetzgeber ihn ausdruecklich vorgesehen hat oder die Eigenart der Materie ihn zwingend gebietet.",
            ),
            Leitentscheidung(
                "BVerwG", "8 C 28.12", "06.04.2014", "BVerwGE 149, 137",
                "Die behoerdliche Ermessensausuebung unterliegt nach Paragraf 114 VwGO der gerichtlichen Kontrolle auf Ermessensueberschreitung, Ermessensunterschreitung und Ermessensfehlgebrauch; Ermessenserwaegungen koennen im Verfahren nur nach Massgabe von Paragraf 114 Satz 2 VwGO ergaenzt werden.",
            ),
            Leitentscheidung(
                "BVerwG", "9 C 3.10", "23.11.2010", "BVerwGE 138, 244",
                "Die Anordnung der sofortigen Vollziehung Paragraf 80 Absatz 2 Nummer 4 VwGO setzt ein besonderes Vollzugsinteresse voraus, das ueber das die Massnahme rechtfertigende Interesse hinausgeht und einzelfallbezogen, schriftlich Paragraf 80 Absatz 3 VwGO begruendet wird.",
            ),
            Leitentscheidung(
                "BVerfG", "1 BvR 357/05", "15.02.2006", "BVerfGE 115, 118 (Luftsicherheitsgesetz)",
                "Hoheitliche Massnahmen, die in das Recht auf Leben und die Menschenwuerde eingreifen, muessen den Grundsatz der Verhaeltnismaessigkeit in jeder Stufe (geeignet, erforderlich, angemessen) wahren; Menschenwuerde Paragraf 1 Absatz 1 GG ist abwaegungsfest.",
            ),
            Leitentscheidung(
                "BVerwG", "4 C 8.07", "25.10.2007", "BVerwGE 130, 39",
                "Im Aussenbereich nach Paragraf 35 BauGB ist die Privilegierung eng zu pruefen; entgegenstehende oeffentliche Belange koennen schon dann angenommen werden, wenn das Vorhaben den Charakter der Landschaft veraendert oder die natuerliche Eigenart beeintraechtigt.",
            ),
        ),
        pruefraster=(
            "Liegt ein Verwaltungsakt vor und welche Ermaechtigungsgrundlage greift?",
            "Sind formelle Vorgaben (Zustaendigkeit, Verfahren, Form, Anhoerung) gewahrt?",
            "Sind die Tatbestandsmerkmale belegt und das Ermessen rechtsfehlerfrei ausgeuebt?",
            "Welche Klageart ist statthaft und ist die Klagebefugnis Paragraf 42 Absatz 2 VwGO gegeben?",
            "Ist Eilrechtsschutz Paragrafen 80, 123 VwGO erforderlich?",
        ),
        skelette=(
            "Widerspruch: Bescheid, Adressat, Frist, Antrag, Begruendung, Beweisangebot.",
            "Klage VwG: Klageantrag, Bescheidbezeichnung, Klagebefugnis, Sachverhalt, rechtliche Wuerdigung, Anregung Paragraf 80 Absatz 5 VwGO.",
            "Antrag Paragraf 80 Absatz 5 VwGO: Antragsziel, Sachverhalt, Erfolgsaussichten, Folgenabwaegung, Glaubhaftmachung.",
        ),
    ))


_register_verwaltungsrecht()


def _register_verwaltungsprozess() -> None:
    base = PROFILE["verwaltungsrecht"]
    register(Themenprofil(
        key="verwaltungsprozess",
        label="Verwaltungsgerichtsbarkeit (richterlich)",
        rolle="Du arbeitest in der Rolle eines verwaltungsgerichtlichen Spruchkoerpers (VG, OVG/VGH, BVerwG): Akteneinsicht und Amtsermittlung steuern, Beweisbeschluss erlassen, muendliche Verhandlung mit Sachbericht durch Berichterstatter, Urteil mit Tenor und Begruendung Paragraf 117 VwGO.",
        stop_kriterien=base.stop_kriterien + (
            "Besetzung des Spruchkoerpers, Ablehnung wegen Befangenheit Paragrafen 54 VwGO unklar.",
            "Vorlage an EuGH Paragraf 267 AEUV oder BVerfG Paragraf 100 GG geboten.",
        ),
        stationen=(
            WorkflowStation(
                title="Zulaessigkeitspruefung",
                eingang="Klageschrift, Bescheid, Widerspruchsbescheid, Klagefrist, Klagebefugnis.",
                pruefung="Rechtsweg Paragraf 40 VwGO, Statthaftigkeit (Anfechtung, Verpflichtung, Feststellung, Leistung), Beteiligten- und Prozessfaehigkeit, Klagebefugnis, Vorverfahren, Klagefrist.",
                arbeitsprodukt="Zulaessigkeitsvermerk mit Pruefraster Paragrafen 40 ff. VwGO.",
            ),
            WorkflowStation(
                title="Begruendetheit",
                eingang="Ermaechtigungsgrundlage, formelle und materielle Rechtmaessigkeit, Ermessen, Verhaeltnismaessigkeit.",
                pruefung="Bei Anfechtungsklage: Verwaltungsakt rechtmaessig und Klaeger in seinen Rechten verletzt Paragraf 113 Absatz 1 Satz 1 VwGO; bei Verpflichtungsklage: Anspruch auf Erlass Paragraf 113 Absatz 5 VwGO; bei Feststellungsklage Paragraf 113 Absatz 1 Satz 4 VwGO Fortsetzungsfeststellungsklage.",
                arbeitsprodukt="Begruendetheitsvermerk mit Subsumtion, Beweisbeduerftigkeit und Tenorvorschlag.",
            ),
            WorkflowStation(
                title="Beweisbeschluss und Verhandlung",
                eingang="Streitige entscheidungserhebliche Tatsachen, Beweismittel, Sachverstaendige.",
                pruefung="Amtsermittlung Paragraf 86 VwGO; Sachverstaendigenbeweis Paragraf 98 VwGO in Verbindung mit Paragrafen 402 ff. ZPO; Augenscheinseinnahme; Vergleichsmoeglichkeit Paragraf 106 VwGO.",
                arbeitsprodukt="Beweisbeschluss, Sitzungsprotokoll mit Antraegen, Beweisaufnahme und etwaigem Vergleich.",
            ),
            WorkflowStation(
                title="Urteilsentwurf",
                eingang="Beweisaufnahmeergebnis, Rechtsauffassung des Spruchkoerpers, Kosten, Streitwert, Berufungszulassung.",
                pruefung="Pflichtangaben Paragraf 117 VwGO (Rubrum, Tenor, Tatbestand, Entscheidungsgruende), Kosten Paragrafen 154 ff. VwGO, Berufungszulassung Paragraf 124a VwGO, Streitwert Paragraf 52 GKG.",
                arbeitsprodukt="Urteilsentwurf mit Tenor, Tatbestand, Entscheidungsgruenden, Kosten- und Streitwertbeschluss.",
            ),
        ),
        pflichtnormen=base.pflichtnormen + (
            "Paragrafen 40, 45, 52 VwGO (Rechtsweg, oertliche Zustaendigkeit)",
            "Paragrafen 86, 98, 99, 100, 108 VwGO (Amtsermittlung, Beweis, Akteneinsicht)",
            "Paragrafen 113, 117 VwGO (Urteil, Pflichtangaben)",
            "Paragrafen 124, 124a, 132, 137 VwGO (Berufung, Revision)",
        ),
        leitentscheidungen=base.leitentscheidungen,
        pruefraster=base.pruefraster + (
            "Welche Klageart ist statthaft und welcher Tenor ergibt sich aus Paragraf 113 VwGO?",
            "Welche Pflichtangaben braucht das Urteil nach Paragraf 117 VwGO?",
        ),
        skelette=(
            "Beweisbeschluss: Beweisthema, Beweismittel, Sachverstaendiger, Frist.",
            "Urteil VG: Rubrum, Tenor, Tatbestand, Entscheidungsgruende, Kosten, Streitwert, Rechtsmittel.",
            "Vergleichsprotokoll Paragraf 106 VwGO mit Hauptsacheerledigung und Kostenfolge.",
        ),
    ))


_register_verwaltungsprozess()


def _register_verfassungsrecht() -> None:
    register(Themenprofil(
        key="verfassungsrecht",
        label="Verfassungsrecht (GG, BVerfGG)",
        rolle="Du arbeitest in einem verfassungsrechtlichen Werkstatt-Modus: Grundrechtseingriff identifizieren, Schutzbereich und Eingriff bestimmen, verfassungsrechtliche Rechtfertigung mit Schranken-Schranken und Verhaeltnismaessigkeit pruefen, Verfassungsbeschwerde oder Normenkontrolle vorbereiten.",
        stop_kriterien=(
            "Frist Paragraf 93 BVerfGG (Verfassungsbeschwerde 1 Monat ab Zustellung der letztinstanzlichen Entscheidung).",
            "Rechtswegerschoepfung Paragraf 90 Absatz 2 BVerfGG unklar.",
            "Eilrechtsschutz Paragraf 32 BVerfGG erforderlich (existenzielle Folgen).",
            "Beschwer und Selbstbetroffenheit unklar.",
            "Verletzung der Menschenwuerde, Folter- oder Abschiebeverbot im Raum.",
        ),
        stationen=(
            WorkflowStation(
                title="Sachverhalt und betroffenes Grundrecht",
                eingang="Hoheitliche Massnahme (Gesetz, Verordnung, Verwaltungsakt, Urteil), Beschwerdefuehrer, betroffene Grundrechtspositionen, Rechtswegverlauf.",
                pruefung="Schutzbereich des einschlaegigen Grundrechts bestimmen (Paragrafen 1 bis 19 GG), persoenlicher und sachlicher Schutzbereich, Konkurrenzverhaeltnisse (Spezialitaet, Idealkonkurrenz), Drittwirkung Paragraf 1 Absatz 3 GG.",
                arbeitsprodukt="Vermerk mit identifiziertem Grundrecht, Schutzbereich, Beschwer und Rechtswegverlauf.",
            ),
            WorkflowStation(
                title="Eingriff und Schranken",
                eingang="Hoheitsakt, Wirkung auf Beschwerdefuehrer, Schranken (einfacher Gesetzesvorbehalt, qualifizierter Gesetzesvorbehalt, verfassungsimmanente Schranken).",
                pruefung="Eingriffsbegriff (klassisch und modern: Finalitaet, Unmittelbarkeit, Rechtsakt, Zwang); Schranken benennen; Schranken-Schranken (Zitiergebot Paragraf 19 Absatz 1 Satz 2 GG, Wesensgehalt Paragraf 19 Absatz 2 GG, Verhaeltnismaessigkeit, Bestimmtheit, Vertrauensschutz).",
                arbeitsprodukt="Pruefraster Eingriff/Schranken mit allen Stufen.",
            ),
            WorkflowStation(
                title="Verhaeltnismaessigkeit",
                eingang="Legitimer Zweck, Geeignetheit, Erforderlichkeit, Angemessenheit (Abwaegung).",
                pruefung="Legitimer Zweck (im Einklang mit der Verfassung), Geeignetheit (Foerderung des Zwecks), Erforderlichkeit (kein milderes gleich geeignetes Mittel), Angemessenheit (Verhaeltnis Schwere des Eingriffs zu Gewicht des Schutzguts); bei Kommunikationsgrundrechten Wechselwirkungslehre.",
                arbeitsprodukt="Verhaeltnismaessigkeitspruefung mit Abwaegungslagen und Gewichtungsschritt.",
            ),
            WorkflowStation(
                title="Verfahrensschritt vor dem BVerfG",
                eingang="Beschwerdeform, Beschwerdefrist, Vorlagen Paragrafen 13 ff. BVerfGG, Antragsbefugnis.",
                pruefung="Verfahrensart (Verfassungsbeschwerde Paragraf 90 BVerfGG, abstrakte/konkrete Normenkontrolle Paragrafen 13 Nummer 6 und 11 BVerfGG, Organstreit Paragraf 13 Nummer 5 BVerfGG); Zulaessigkeit (Beschwerdebefugnis, Rechtswegerschoepfung, Subsidiaritaet, Frist, Form, Begruendungstiefe Paragraf 23 Absatz 1 BVerfGG).",
                arbeitsprodukt="Zulaessigkeits- und Begruendetheitsraster mit Vorhalt der erforderlichen Pflichtangaben.",
            ),
            WorkflowStation(
                title="Eilrechtsschutz und Antrag",
                eingang="Drohende irreversible Folgen, Folgenabwaegung, Erfolgsaussichten der Hauptsache.",
                pruefung="Einstweilige Anordnung Paragraf 32 BVerfGG; doppelte Folgenabwaegung; Subsidiaritaet zu fachgerichtlichem Eilrechtsschutz.",
                arbeitsprodukt="Antrag Paragraf 32 BVerfGG mit Sachverhalt, Folgenabwaegung, Anordnungsanspruch.",
            ),
            WorkflowStation(
                title="Schriftsatz und Anschluss",
                eingang="Zielprodukt (Verfassungsbeschwerde, Vorlagebeschluss, Stellungnahme), Adressat, Form Paragraf 23 BVerfGG.",
                pruefung="Pflichtangaben, klare Bezeichnung des angegriffenen Hoheitsakts, Beschwerdebefugnis, Frist, Begruendung mit Schutzbereich-Eingriff-Schranken-Verhaeltnismaessigkeit.",
                arbeitsprodukt="Vollstaendiger Schriftsatz mit Anlagenkonvolut und Verfahrenshinweisen.",
            ),
        ),
        pflichtnormen=(
            "Paragrafen 1 bis 19 GG (Grundrechte)",
            "Paragraf 20 GG (Verfassungsprinzipien, Rechtsstaatsprinzip)",
            "Paragrafen 38, 79, 93, 100 GG (Wahlrecht, Verfassungsaenderung, Verfassungsbeschwerde, Vorlage)",
            "Paragrafen 13, 23, 31, 32, 78, 90 bis 95 BVerfGG (Zustaendigkeit, Schriftsatzform, Bindungswirkung, einstweilige Anordnung, Verfassungsbeschwerde)",
            "Paragrafen 80 ff. BVerfGG (konkrete Normenkontrolle)",
            "Paragrafen 13 Nummer 5, 63 ff. BVerfGG (Organstreit)",
            "Artikel 6 EMRK (faires Verfahren)",
            "Charta der Grundrechte der EU (insbesondere Artikel 7, 8, 47)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "BVerfG", "1 BvR 16/13", "06.11.2019", "BVerfGE 152, 152 (Recht auf Vergessen I)",
                "Die fachgerichtliche Kontrolle muss eine umfassende Grundrechtsabwaegung leisten; das allgemeine Persoenlichkeitsrecht Paragraf 2 Absatz 1 in Verbindung mit Paragraf 1 Absatz 1 GG erfordert mit zunehmendem Zeitablauf einen verstaerkten Schutz vor anhaltender oeffentlicher Bekanntmachung verurteilungsbezogener Daten.",
            ),
            Leitentscheidung(
                "BVerfG", "1 BvR 2019/16", "10.10.2017", "BVerfGE 147, 1 (Drittes Geschlecht)",
                "Das allgemeine Persoenlichkeitsrecht in Verbindung mit dem Diskriminierungsverbot Paragraf 3 Absatz 3 GG schuetzt die Geschlechtsidentitaet auch jenseits der binaeren Zuordnung; der Gesetzgeber ist verpflichtet, eine positive Eintragungsmoeglichkeit zu schaffen.",
            ),
            Leitentscheidung(
                "BVerfG", "1 BvR 2347/15", "26.02.2020", "BVerfGE 153, 182 (Suizidhilfe)",
                "Das allgemeine Persoenlichkeitsrecht umfasst das Recht auf selbstbestimmtes Sterben einschliesslich der Freiheit, hierzu die Hilfe Dritter in Anspruch zu nehmen; ein generelles Verbot der geschaeftsmaessigen Foerderung der Selbsttoetung Paragraf 217 StGB ist verfassungswidrig.",
            ),
            Leitentscheidung(
                "BVerfG", "1 BvR 2656/18", "24.03.2021", "BVerfGE 157, 30 (Klimaschutz)",
                "Die Schutzpflichten des Staates aus Paragraf 20a GG und den Freiheitsrechten verlangen ausreichende und rechtzeitige Massnahmen zum Klimaschutz; gegenwaertige Versaeumnisse, die spaetere Generationen unverhaeltnismaessig belasten, sind verfassungswidrig.",
            ),
            Leitentscheidung(
                "BVerfG", "2 BvR 859/15", "05.05.2020", "BVerfGE 154, 17 (PSPP, ultra vires)",
                "Massnahmen der Europaeischen Union, die offensichtlich kompetenzueberschreitend ergehen, koennen vom Bundesverfassungsgericht im Rahmen seiner Ultra-vires-Kontrolle ueberprueft werden; nationale Hoheitstraeger duerfen an offensichtlich kompetenzueberschreitenden Akten nicht mitwirken.",
            ),
            Leitentscheidung(
                "BVerfG", "1 BvR 357/05", "15.02.2006", "BVerfGE 115, 118 (Luftsicherheitsgesetz)",
                "Eine Norm, die das Toeten von Unschuldigen erlaubt, verletzt die Menschenwuerde Paragraf 1 Absatz 1 GG und den Schutz des Lebens Paragraf 2 Absatz 2 GG; Menschenwuerde ist abwaegungsfest.",
            ),
        ),
        pruefraster=(
            "Welcher Schutzbereich ist beruehrt, in welchem Umfang und in welcher Konkurrenzlage?",
            "Liegt ein Eingriff vor (klassisch oder modern, Drittwirkung), und auf welcher Schranke beruht er?",
            "Sind die Schranken-Schranken (Zitiergebot, Wesensgehalt, Verhaeltnismaessigkeit, Bestimmtheit) gewahrt?",
            "Ist die Verfassungsbeschwerde zulaessig (Beschwer, Rechtsweg, Subsidiaritaet, Frist, Begruendung Paragraf 23 BVerfGG)?",
            "Ist Eilrechtsschutz Paragraf 32 BVerfGG geboten?",
        ),
        skelette=(
            "Verfassungsbeschwerde Paragraf 90 BVerfGG: angegriffener Hoheitsakt, Beschwer, Rechtswegverlauf, Schutzbereich, Eingriff, Schranken, Verhaeltnismaessigkeit, Antraege.",
            "Vorlagebeschluss Paragraf 100 GG: angegriffene Norm, Entscheidungserheblichkeit, Ueberzeugung von der Verfassungswidrigkeit.",
            "Antrag Paragraf 32 BVerfGG: Folgenabwaegung, Eilbeduerftigkeit, Beweismittel.",
        ),
    ))


_register_verfassungsrecht()


def _register_verfassungsprozess() -> None:
    base = PROFILE["verfassungsrecht"]
    register(Themenprofil(
        key="verfassungsprozess",
        label="Bundesverfassungsgericht (richterlich)",
        rolle="Du arbeitest in der Rolle eines Senats oder einer Kammer des Bundesverfassungsgerichts: Annahmeentscheidung, Begruendetheitspruefung, Tenor (Verfassungswidrigkeit, Nichtigkeit, verfassungskonforme Auslegung), Bindungswirkung Paragraf 31 BVerfGG.",
        stop_kriterien=base.stop_kriterien + (
            "Pruefung ueber Annahmegrund Paragraf 93a BVerfGG (grundsaetzliche verfassungsrechtliche Bedeutung, Durchsetzung der Grundrechte).",
            "Verfassungskonforme Auslegung oder Nichtigkeitserklaerung im Raum.",
        ),
        stationen=(
            WorkflowStation(
                title="Annahmeentscheidung",
                eingang="Verfassungsbeschwerde, Schriftsatz, Anlagen, Schreiben der Beteiligten, fachgerichtliche Akten.",
                pruefung="Zulaessigkeit (Beschwerdefaehigkeit, Beschwerdebefugnis, Rechtswegerschoepfung, Subsidiaritaet, Frist, Begruendung), Annahmegruende Paragraf 93a BVerfGG, summarische Erfolgsaussicht.",
                arbeitsprodukt="Annahmeentscheidung mit Begruendung oder Beschluss nach Paragraf 93b BVerfGG.",
            ),
            WorkflowStation(
                title="Begruendetheitspruefung",
                eingang="Pruefraster Schutzbereich, Eingriff, Schranken, Verhaeltnismaessigkeit; einschlaegige Senatsrechtsprechung.",
                pruefung="Pruefungsmassstab des BVerfG (Willkuermassstab vs. spezifisches Grundrechtsgewicht), Hueterfunktion gegenueber den Fachgerichten, Pruefungsdichte, Kontrolle behoerdlicher Beurteilungsspielraeume.",
                arbeitsprodukt="Begruendetheitsvermerk mit Subsumtion, Abwaegung und Tenorvorschlag.",
            ),
            WorkflowStation(
                title="Tenor und Bindungswirkung",
                eingang="Rechtsprechungsfolgen, Bindungswirkung Paragraf 31 BVerfGG, Nichtigkeitsfolge Paragraf 78 BVerfGG, Uebergangsregelung.",
                pruefung="Verfassungswidrigkeitserklaerung, Nichtigkeitserklaerung, verfassungskonforme Auslegung; Geltungsanordnung mit Fortgeltung bis zur Neuregelung; Wirkung erga omnes.",
                arbeitsprodukt="Tenorentwurf mit Bindungswirkung, Uebergangsregelung und ggf. Aussetzung der Vollziehung.",
            ),
            WorkflowStation(
                title="Schriftbild und Veroeffentlichung",
                eingang="Senatsentwurf, Sondervoten Paragraf 30 Absatz 2 BVerfGG, Verlautbarung.",
                pruefung="Begruendungstiefe, Klarheit der Subsumtion, Quellen, Sondervotumsmoeglichkeit; Pressemitteilung mit Kernsaetzen.",
                arbeitsprodukt="Vollstaendige Entscheidungsbegruendung mit Leitsaetzen und Pressemitteilung.",
            ),
        ),
        pflichtnormen=base.pflichtnormen + (
            "Paragrafen 30, 31, 78, 93a, 93b, 93c BVerfGG (Senatsentscheidung, Bindung, Annahme, Kammerentscheidung)",
            "Paragraf 32 BVerfGG (einstweilige Anordnung)",
        ),
        leitentscheidungen=base.leitentscheidungen,
        pruefraster=base.pruefraster + (
            "Ist die Verfassungsbeschwerde nach Paragraf 93a BVerfGG anzunehmen?",
            "Welche Bindungswirkung Paragraf 31 BVerfGG entfaltet die Entscheidung?",
        ),
        skelette=(
            "Senatsentscheidung: Rubrum, Tenor, Sachverhalt, Begruendung mit Schutzbereich, Eingriff, Schranken, Verhaeltnismaessigkeit, Bindungsanordnung.",
            "Kammerbeschluss Paragraf 93b BVerfGG: knappe Begruendung, Hinweis auf gesicherte Senatsrechtsprechung.",
            "Pressemitteilung mit Leitsaetzen und Tenor.",
        ),
    ))


_register_verfassungsprozess()


def _register_vergaberecht_kartell() -> None:
    register(Themenprofil(
        key="vergaberecht-kartell",
        label="Vergabe- und Kartellrecht (GWB, VgV, EU-Wettbewerbsrecht)",
        rolle="Du arbeitest in einem vergabe- und kartellrechtlichen Werkstatt-Modus: Auftragsbekanntmachung, Vergabeverfahren oder kartellrechtlichen Sachverhalt (Marktabgrenzung, Marktbeherrschung, Kartell, Fusionskontrolle) pruefen, Nachpruefungsverfahren Paragrafen 155 ff. GWB oder kartellbehoerdliches Verfahren vorbereiten.",
        stop_kriterien=(
            "Antragsfrist Paragraf 160 Absatz 3 GWB (Ruege unverzueglich, Antrag binnen 15 Kalendertagen).",
            "Stillhaltefrist Paragraf 134 GWB (Information und Wartepflicht).",
            "Bietergeheimnis und Geschaeftsgeheimnisse unklar.",
            "Marktbeherrschungs- oder Kartelluntersuchung mit Hausdurchsuchung oder Auskunftsverlangen.",
            "Fusionsanmeldung Paragrafen 35 ff. GWB oder EU-Fusionskontrollverordnung erforderlich.",
        ),
        stationen=(
            WorkflowStation(
                title="Vergabe- oder Wettbewerbssachverhalt",
                eingang="Auftragsbekanntmachung, Vergabeunterlagen, Angebote, Wertung; bei Kartellrecht: Marktdaten, Vereinbarungen, abgestimmte Verhaltensweisen, Marktanteile.",
                pruefung="Auftraggeberbegriff Paragrafen 99 ff. GWB, Schwellenwert Paragraf 106 GWB, Verfahrensart (offen, nicht offen, Verhandlung, Wettbewerblicher Dialog, Innovationspartnerschaft); Marktabgrenzung (sachlich, raeumlich, zeitlich).",
                arbeitsprodukt="Aktenvermerk mit Verfahrenseinordnung oder Marktbeschreibung.",
            ),
            WorkflowStation(
                title="Vergabeverfahren",
                eingang="Vergabeunterlagen, Eignungs- und Zuschlagskriterien, Bewertungsmatrix, Bietergespraeche, Aufklaerung Paragraf 15 VgV.",
                pruefung="Transparenz Paragraf 97 Absatz 1 GWB, Gleichbehandlung Paragraf 97 Absatz 2 GWB, Wirtschaftlichkeit Paragraf 127 GWB; Eignung Paragrafen 122 ff. GWB; Ausschluss Paragrafen 123, 124 GWB; ungewoehnlich niedriges Angebot Paragraf 60 VgV.",
                arbeitsprodukt="Pruefraster Vergabeverfahren mit identifizierten Vergabefehlern und Heilungsmoeglichkeiten.",
            ),
            WorkflowStation(
                title="Kartellrechtliche Pruefung",
                eingang="Vereinbarungen, Beschluesse, abgestimmte Verhaltensweisen, Marktanteile, Marktmacht.",
                pruefung="Paragraf 1 GWB / Artikel 101 AEUV (Kartellverbot, Verbotstatbestand, Spuerbarkeit, Freistellung Paragraf 2 GWB / Artikel 101 Absatz 3 AEUV); Paragraf 19 GWB / Artikel 102 AEUV (Marktmissbrauch); Paragrafen 18, 35 ff. GWB (Marktbeherrschung, Fusionskontrolle).",
                arbeitsprodukt="Pruefraster Kartell-/Missbrauchstatbestand mit Marktabgrenzung und Spuerbarkeit.",
            ),
            WorkflowStation(
                title="Nachpruefungs- oder Behoerdenverfahren",
                eingang="Vergabekammer Paragraf 156 GWB, Sofortige Beschwerde Paragraf 171 GWB, Kartellbehoerden (Bundeskartellamt, Landeskartellbehoerden, EU-Kommission).",
                pruefung="Antrag Paragraf 161 GWB, Ruege Paragraf 160 Absatz 3 GWB, aufschiebende Wirkung Paragraf 169 GWB; bei Kartellbehoerden Auskunftsverlangen Paragraf 59 GWB, Durchsuchung Paragraf 59 Absatz 4 GWB, Settlement Paragraf 32b GWB.",
                arbeitsprodukt="Antrags-/Beschwerdeschrift oder Eingabe an Kartellbehoerde mit Antraegen und Beweisangeboten.",
            ),
            WorkflowStation(
                title="Beweis und Vertraulichkeit",
                eingang="Vergabeakte Paragraf 167 GWB, Geschaeftsgeheimnisse, Sachverstaendige, Zeugen.",
                pruefung="Akteneinsicht Paragraf 165 GWB mit Schwaerzung von Geschaeftsgeheimnissen Paragraf 17 GeschGehG; Vertraulichkeit, prozessuale Gleichbehandlung der Beteiligten.",
                arbeitsprodukt="Beweisplan und Akteneinsichtsantrag mit Schwaerzungsantraegen.",
            ),
            WorkflowStation(
                title="Arbeitsprodukt und Anschluss",
                eingang="Zielprodukt (Nachpruefungsantrag, Beschwerde, Stellungnahme, Settlement-Vorschlag).",
                pruefung="Pflichtangaben Paragraf 161 GWB, Antrag, Sachverhalt, Vergaberechtsverstoesse, Beweisangebote, Anregung aufschiebende Wirkung Paragraf 169 GWB.",
                arbeitsprodukt="Vollstaendiger Schriftsatz mit Anschlussplan (Akteneinsicht, Termin, Aufhebung, Schadensersatz Paragraf 181 GWB).",
            ),
        ),
        pflichtnormen=(
            "Paragrafen 97, 99, 106, 122, 123, 124, 127, 134, 155, 156, 160, 161, 165, 167, 169, 171, 181 GWB",
            "Paragrafen 14, 15, 31, 53, 60 VgV (Verfahrensarten, Aufklaerung, Wertung)",
            "Paragraf 1 GWB (Kartellverbot), Paragrafen 18, 19 GWB (Marktbeherrschung, Missbrauch)",
            "Paragrafen 35 ff. GWB (Fusionskontrolle)",
            "Artikel 101, 102 AEUV; Verordnung (EU) 2022/720 (Vertikal-GVO)",
            "Paragrafen 32, 32b GWB (Verfuegung, Verpflichtungszusagen)",
            "Paragrafen 17 ff. GeschGehG (Geschaeftsgeheimnisse)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "EuGH", "C-26/03", "11.01.2005", "Slg. 2005, I-1 (Stadt Halle)",
                "Inhouse-Vergabe nach europaeischem Vergaberecht erfordert, dass der oeffentliche Auftraggeber den Auftragnehmer wie eine eigene Dienststelle kontrolliert und dieser im Wesentlichen fuer den Auftraggeber taetig ist; bereits eine geringfuegige private Beteiligung schliesst Inhouse aus.",
            ),
            Leitentscheidung(
                "BGH", "X ZB 13/03", "26.09.2006", "BGHZ 169, 131",
                "Eine wirksame Ruege nach Paragraf 160 Absatz 3 GWB setzt voraus, dass der Bieter den behaupteten Vergaberechtsverstoss unverzueglich nach Erkennen, spaetestens nach Ablauf einer angemessenen Pruefungsfrist beim Auftraggeber geltend macht.",
            ),
            Leitentscheidung(
                "BGH", "KZR 8/21", "13.07.2021", "WuW 2021, 519 (Schienenkartell II)",
                "Bei Kartellschadensersatzanspruechen Paragraf 33a GWB ist die Vermutung kartellbedingter Preisaufschlaege grundsaetzlich gegeben; Hoehe und Schadensumfang sind nach Paragraf 287 ZPO unter Heranziehung von oekonomischen Sachverstaendigen zu schaetzen.",
            ),
            Leitentscheidung(
                "EuGH", "C-377/17", "04.07.2019", "ECLI:EU:C:2019:562 (HOAI)",
                "Verbindliche Mindesthonorare fuer Architekten und Ingenieure nach der HOAI sind mit der Dienstleistungsrichtlinie 2006/123/EG unvereinbar, weil sie eine unzulaessige Beschraenkung der Niederlassungsfreiheit darstellen.",
            ),
            Leitentscheidung(
                "BGH", "KZR 75/10", "07.02.2012", "BGHZ 192, 245 (ORWI)",
                "Die kartellrechtliche Anspruchsberechtigung erstreckt sich auch auf mittelbare Abnehmer; die Weitergabe des Preisaufschlags (passing on) ist nach Paragraf 33a GWB im Rahmen der Schadensbemessung zu beruecksichtigen.",
            ),
        ),
        pruefraster=(
            "Liegt ein oeffentlicher Auftrag oberhalb des Schwellenwerts vor und welche Verfahrensart ist gewaehlt?",
            "Sind Transparenz, Gleichbehandlung, Eignung und Wirtschaftlichkeit Paragrafen 97, 122, 127 GWB gewahrt?",
            "Wurde die Ruege Paragraf 160 Absatz 3 GWB unverzueglich und fristgerecht erhoben?",
            "Kartellrechtlich: Liegt eine spuerbare Wettbewerbsbeschraenkung vor und greift eine Freistellung?",
            "Sind Vertraulichkeitsinteressen und Geschaeftsgeheimnisse gewahrt?",
        ),
        skelette=(
            "Nachpruefungsantrag Paragraf 161 GWB: Antrag, Antragsteller, Auftraggeber, Verfahrensgegenstand, geruegte Verstoesse, Ruegezeitpunkt, Beweisangebote.",
            "Kartellrechtliche Eingabe: Marktabgrenzung, Verhaltensbeschreibung, Spuerbarkeit, Freistellungserwaegungen, Antrag.",
            "Schadensersatzschriftsatz Paragraf 33a GWB: Kartellbestand, Betroffenheit, Schaden (Paragraf 287 ZPO), oekonomischer Sachverstaendigenantrag.",
        ),
    ))


_register_vergaberecht_kartell()


def _register_urheber_marke() -> None:
    register(Themenprofil(
        key="urheber-marke",
        label="Urheber- und gewerblicher Rechtsschutz (UrhG, MarkenG, PatG, DesignG)",
        rolle="Du arbeitest in einem urheber- und kennzeichenrechtlichen Werkstatt-Modus: Schutzfaehigkeit, Verletzung und Rechtsfolgen pruefen; Abmahnung, einstweilige Verfuegung und Klage Paragrafen 97 ff. UrhG, Paragrafen 14, 15 MarkenG, Paragrafen 139 ff. PatG, Paragraf 42 DesignG vorbereiten.",
        stop_kriterien=(
            "Dringlichkeitsfrist fuer einstweilige Verfuegung (Regel ein Monat ab Kenntnis).",
            "Schutzrechtsverletzung mit Strafanzeige (Paragraf 106 UrhG, Paragraf 143 MarkenG, Paragraf 142 PatG).",
            "Aufnahme- oder Vernehmungssituation, fehlende Schutzrechtsklarheit (Loeschungsverfahren, Nichtigkeit).",
            "Auslandsbezug mit Paragraf 32 ZPO oder Brussel Ia Verordnung.",
            "Verbreitung im Internet mit Plattform- oder Hostinghaftung Paragrafen 7 ff. TMG / DSA.",
        ),
        stationen=(
            WorkflowStation(
                title="Schutzgegenstand und Schutzfaehigkeit",
                eingang="Werk, Marke, Patent, Design, Topographie; Schoepfer/Inhaber; Schutzrechtsbestand (Eintragung, Registerauszug, Werkmuster).",
                pruefung="Urheberrecht Paragrafen 1, 2 UrhG (Schoepfungshoehe); Markenrecht Paragrafen 3, 8 MarkenG (Markenfaehigkeit, absolute Schutzhindernisse); Patentrecht Paragrafen 1 bis 4 PatG (Neuheit, erfinderische Taetigkeit, gewerbliche Anwendbarkeit); Designrecht Paragrafen 1 bis 3 DesignG (Neuheit, Eigenart).",
                arbeitsprodukt="Schutzraster mit identifiziertem Schutzrecht, Inhaber, Schutzfaehigkeit und Schutzbereich.",
            ),
            WorkflowStation(
                title="Verletzungspruefung",
                eingang="Verletzungshandlung (Vervielfaeltigung, Verbreitung, oeffentliche Wiedergabe, Benutzung), angegriffene Form, Kontext, Beweisstuecke.",
                pruefung="Urheberrechtlich: Identitaet oder Bearbeitung Paragraf 23 UrhG, freie Benutzung; Markenrecht: Verwechslungsgefahr Paragraf 14 MarkenG, Doppelidentitaet, Bekanntheitsschutz Paragraf 14 Absatz 2 Nummer 3 MarkenG; Patentrecht: Wortsinn- oder aequivalente Patentverletzung Paragraf 14 PatG; Designrecht: Gesamteindruck Paragraf 38 DesignG.",
                arbeitsprodukt="Verletzungsraster mit Aehnlichkeitsanalyse, Beweisstuecken und Risikoeinschaetzung.",
            ),
            WorkflowStation(
                title="Schranken und Einwendungen",
                eingang="Schranken Paragrafen 44a bis 63 UrhG; Erschoepfung Paragraf 24 MarkenG, Paragraf 17 UrhG; freie Werknutzung; Schutzdauer; Verwirkung Paragraf 21 MarkenG.",
                pruefung="Zitate Paragraf 51 UrhG, Privatkopie Paragraf 53 UrhG, Karikatur Paragraf 51a UrhG, Schranken Markenrecht Paragraf 23 MarkenG, Erschoepfungsgrundsatz; Verjaehrung Paragraf 102 UrhG, Paragraf 20 MarkenG (drei oder zehn Jahre).",
                arbeitsprodukt="Pruefraster Schranken und Einwendungen mit Konsequenz fuer Klagestrategie.",
            ),
            WorkflowStation(
                title="Rechtsfolgen und Anspruechsbuendel",
                eingang="Unterlassungsanspruch, Beseitigung, Auskunft, Schadenersatz, Bereicherung, Vernichtung, Veroeffentlichung.",
                pruefung="Paragrafen 97, 97a, 98, 99, 100, 101 UrhG; Paragrafen 14, 18, 19 MarkenG; Paragrafen 139 bis 142 PatG; Schadensberechnung dreigleisig (konkreter Schaden, Lizenzanalogie, Verletzergewinn); Abmahnkosten Paragraf 97a UrhG (Schwellenwert 1.000 Euro fuer Privatpersonen).",
                arbeitsprodukt="Anspruchsbuendel mit Berechnungsmethoden, Beweismitteln und Vergleichsraum.",
            ),
            WorkflowStation(
                title="Verfahren und einstweiliger Rechtsschutz",
                eingang="Abmahnung, einstweilige Verfuegung, Hauptsacheklage, Streitwert, Zustaendigkeit (Paragraf 105 UrhG, Paragraf 140 MarkenG, Paragraf 143 PatG).",
                pruefung="Abmahnung Paragraf 97a UrhG, Paragrafen 935, 940 ZPO, Dringlichkeitsvermutung Paragraf 12 Absatz 2 UWG analog; Gerichtsstand der unerlaubten Handlung Paragraf 32 ZPO; bei Patentstreit Paragraf 143 PatG ausschliessliche Zustaendigkeit benannter Gerichte.",
                arbeitsprodukt="Schriftsatzkern (Abmahnung, Antrag einstweilige Verfuegung, Hauptsacheklage) mit Antraegen und Beweisangeboten.",
            ),
            WorkflowStation(
                title="Arbeitsprodukt und Vergleich",
                eingang="Zielprodukt, Adressat, Vergleichsraum, Lizenzgestaltung.",
                pruefung="Pflichtangaben, Antrag, Begruendung, Streitwert; Vergleichsangebot mit Lizenz, Abstandsklausel, Vertragsstrafe Paragraf 339 BGB.",
                arbeitsprodukt="Vollstaendiges Schriftstueck mit Anschluss (Vollstreckung Paragrafen 890, 887 ZPO, Lizenzverhandlung, Eintragung).",
            ),
        ),
        pflichtnormen=(
            "Paragrafen 1, 2, 7, 11, 15 bis 24, 31 bis 44, 51, 53, 97, 97a, 98 bis 101a, 106, 108b UrhG",
            "Paragrafen 3, 4, 8, 9, 14, 15, 18, 19, 20, 23, 24, 26 MarkenG",
            "Paragrafen 1, 3, 4, 9, 11, 14, 15, 139 bis 142 PatG",
            "Paragrafen 1, 3, 38, 42, 43 DesignG",
            "Paragraf 4 UWG (Rufausnutzung, Nachahmung)",
            "Paragrafen 7 ff. TMG / Digital Services Act (Hosting-Haftung)",
            "Paragrafen 935, 940, 32 ZPO",
            "Paragraf 287 ZPO (Schadensschaetzung)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "EuGH", "C-466/12", "13.02.2014", "ECLI:EU:C:2014:76 (Svensson)",
                "Das Setzen eines Links auf ein im Internet bereits frei zugaengliches Werk stellt keine oeffentliche Wiedergabe Artikel 3 RL 2001/29/EG dar, sofern kein neues Publikum erreicht wird; Umgehung von Zugangsbeschraenkungen begruendet eine Wiedergabe an ein neues Publikum.",
            ),
            Leitentscheidung(
                "BGH", "I ZR 79/14", "22.11.2014", "GRUR 2015, 258 (Filterbar)",
                "Der Betreiber einer Internet-Plattform haftet als Stoerer fuer Urheberrechtsverletzungen seiner Nutzer, wenn er zumutbare Pruefpflichten verletzt; nach Hinweis auf eine konkrete Verletzung trifft ihn die Pflicht, gleichartige Verletzungen kuenftig zu verhindern.",
            ),
            Leitentscheidung(
                "BGH", "I ZR 140/15", "11.05.2017", "BGHZ 215, 38 (WLAN-Stoererhaftung)",
                "Der Inhaber eines privaten WLAN-Anschlusses haftet nicht als Stoerer fuer Urheberrechtsverletzungen Dritter, wenn der Anschluss mit einer aktuellen marktueblichen Verschluesselung gesichert war.",
            ),
            Leitentscheidung(
                "EuGH", "C-682/18", "22.06.2021", "ECLI:EU:C:2021:503 (YouTube und Cyando)",
                "Plattformbetreiber nehmen eine eigene oeffentliche Wiedergabe nach Artikel 3 RL 2001/29/EG nur vor, wenn sie ueber das blosse Bereitstellen hinaus eine zentrale Rolle bei der Zugangsverschaffung spielen und Kenntnis von rechtswidrigen Inhalten haben oder offensichtliche Verletzungen tolerieren.",
            ),
            Leitentscheidung(
                "BGH", "I ZR 53/13", "27.03.2014", "GRUR 2014, 1101 (Tagesschau-App)",
                "Bei der Schadensberechnung wegen unbefugter Nutzung urheberrechtlich geschuetzter Werke ist die Lizenzanalogie anwendbar; massgeblich ist, was vernuenftige Parteien als Lizenzgebuehr vereinbart haetten.",
            ),
            Leitentscheidung(
                "BGH", "I ZR 7/16", "22.02.2018", "BGHZ 217, 350 (Ortlieb)",
                "Die Benutzung einer Marke durch einen Wiederverkaeufer ist nur dann erlaubt, wenn sie sich an den anerkannten Gepflogenheiten orientiert und nicht den Eindruck einer besonderen geschaeftlichen Beziehung erweckt.",
            ),
        ),
        pruefraster=(
            "Welches Schutzrecht greift in welchem Schutzumfang?",
            "Liegt eine identische oder aehnliche Benutzungshandlung im geschuetzten Bereich vor?",
            "Greift eine Schranke oder ein Einwand (Erschoepfung, Schranken, Verjaehrung, Verwirkung)?",
            "Welche Anspruechsbuendel (Unterlassung, Auskunft, Schadenersatz, Vernichtung) sind durchsetzbar?",
            "Ist einstweiliger Rechtsschutz dringlich (Monatsfrist) und welcher Gerichtsstand ist gegeben?",
        ),
        skelette=(
            "Abmahnung Paragraf 97a UrhG: Schutzrechtsbestand, Verletzungshandlung, Unterlassungsanspruch, Aufforderung zur Unterlassungserklaerung, Vertragsstrafenversprechen, Frist, Kosten.",
            "Antrag einstweilige Verfuegung: Verfuegungsanspruch, Verfuegungsgrund, Glaubhaftmachung, Schutzschriftbezug.",
            "Hauptsacheklage: Unterlassung, Auskunft, Schadenersatz, Berechnungsmethode, Vernichtung, Veroeffentlichung.",
        ),
    ))


_register_urheber_marke()


def _register_versicherung_transport() -> None:
    register(Themenprofil(
        key="versicherung-transport",
        label="Versicherungs- und Transportrecht (VVG, Fluggast-VO, See- und Strassentransport)",
        rolle="Du arbeitest in einem versicherungs- und transportrechtlichen Werkstatt-Modus: Versicherungsfall, Obliegenheitsverletzung und Leistungsfreiheit pruefen; Fluggast-, Bahn- und Schifffahrtsrechte aus EU-Verordnungen sowie Frachtfuehrerhaftung HGB/CMR.",
        stop_kriterien=(
            "Fristen Paragraf 12 Absatz 3 VVG-alt obsolet, aber Klagefrist Paragraf 12 Absatz 4 VVG-neu beachten; Verjaehrung Paragraf 195 BGB / Paragraf 439 HGB / Artikel 32 CMR.",
            "Anspruch aus EG 261/2004 (Fluggast) drohende Verjaehrung Paragraf 195 BGB (3 Jahre).",
            "Schiffsbergung, Havarie, Personenschaeden mit unmittelbarer Existenzfolge.",
            "Versicherer beruft sich auf arglistige Taeuschung Paragraf 22 VVG oder grobe Fahrlaessigkeit Paragraf 81 VVG.",
            "Pflichtversicherung (KfZ-Pflichtversicherung Paragrafen 113 ff. VVG, Direktanspruch Paragraf 115 VVG).",
        ),
        stationen=(
            WorkflowStation(
                title="Versicherungs- oder Transportlage",
                eingang="Versicherungsvertrag, Versicherungsbedingungen, Schadensanzeige, Beweisstuecke; Bahn-/Flug-/Schiffstickets, Bordkarte, Booking-Reference, Verzoegerungs- oder Annullierungsschreiben; Frachtbriefe (CMR, Konnossement).",
                pruefung="Welcher Versicherungszweig (Hausrat, Wohngebaeude, Haftpflicht, KfZ, Berufsunfaehigkeit, Lebens-, Kranken-, Rechtsschutz)? Welches Transportregime (EG 261/2004, EG 1371/2007 Bahn, Athener Uebereinkommen Schiff, CMR, HGB Buch 4)?",
                arbeitsprodukt="Aktenvermerk mit Versicherungs- oder Transportzweig, Pflichtversicherungsbezug und Schadensbeschreibung.",
            ),
            WorkflowStation(
                title="Versicherungsfall und Deckung",
                eingang="Risikobeschreibung, Ausschluesse, Obliegenheiten, Praemienzahlung, Anzeigepflichten Paragrafen 19, 23 VVG.",
                pruefung="Deckungsumfang nach AVB; Risiko-Ausschluesse; vorvertragliche Anzeigepflichten Paragraf 19 VVG; Gefahrerhoehung Paragrafen 23 ff. VVG; grobe Fahrlaessigkeit Paragraf 81 VVG; Obliegenheitsverletzung Paragrafen 28, 82 VVG mit Kuerzung im Verhaeltnis zur Verschuldensschwere.",
                arbeitsprodukt="Deckungsraster mit Versicherungsfall, Ausschluessen, Obliegenheiten und Quote.",
            ),
            WorkflowStation(
                title="Fluggast- und Transportrechte",
                eingang="Reiseverlauf, Verspaetungsgrund, ausserordentliche Umstaende, Strecke, Flug- oder Bahnnummer, Buchungsklasse.",
                pruefung="EG 261/2004: Ausgleichszahlung Artikel 5 bis 7 (250/400/600 Euro je nach Distanz), Betreuung Artikel 9, alternative Befoerderung Artikel 8; ausserordentliche Umstaende Artikel 5 Absatz 3; Bahnrechte Artikel 17 EG 1371/2007.",
                arbeitsprodukt="Pruefraster Fluggastrechte oder Bahnrechte mit Anspruchsbetrag und Hilfsantraegen.",
            ),
            WorkflowStation(
                title="Frachtfuehrerhaftung",
                eingang="Frachtbrief, Sendung, Beschaedigungs- oder Verlustprotokoll, Wertangabe.",
                pruefung="Inlandstransport Paragrafen 425 ff. HGB; internationaler Strassengueterverkehr Artikel 17 ff. CMR (Haftungsgrund, Schaden, Hoechstbetrag 8.33 SZR je Kilogramm); Verjaehrung Paragraf 439 HGB / Artikel 32 CMR (1 Jahr, bei Vorsatz 3 Jahre); Schadensanzeige Paragraf 438 HGB / Artikel 30 CMR.",
                arbeitsprodukt="Pruefraster Frachtfuehrerhaftung mit Haftungsgrund, Hoechstbetrag und Verjaehrungsstand.",
            ),
            WorkflowStation(
                title="Beweis und Sachverstaendiger",
                eingang="Schadensbilder, Sachverstaendigengutachten, Polizeibericht, Wetterdaten, Trackingdaten, Bordbuch.",
                pruefung="Beweislast Paragraf 286 ZPO; Anscheinsbeweis bei typischem Geschehensablauf (z. B. KfZ-Unfall); Sachverstaendigengutachten Paragrafen 402 ff. ZPO; private Sachverstaendigengutachten als urkundlich verwertbare Privatgutachten.",
                arbeitsprodukt="Beweisplan mit Sachverstaendigenantraegen, Zeugen, Urkunden, Bildmaterial.",
            ),
            WorkflowStation(
                title="Schriftsatz und Anschluss",
                eingang="Zielprodukt (Deckungsanfrage, Klage gegen Versicherer, Klage aus EG 261, Frachtklage, Direktanspruch Paragraf 115 VVG).",
                pruefung="Pflichtangaben, Antrag, Sachverhalt, Anspruchsgrundlage, Beweisangebote; Hilfsantraege (Feststellung, Mindestbetrag); Kostenrisiko.",
                arbeitsprodukt="Vollstaendiger Schriftsatz mit Anschluss (Aussergerichtliche Verhandlung, Streitwert, gegebenenfalls Schlichtungsstelle).",
            ),
        ),
        pflichtnormen=(
            "Paragrafen 1, 6, 19, 22, 23, 26, 28, 81, 82, 115, 195 VVG",
            "Paragrafen 113, 114, 115, 117 VVG (Pflichtversicherung, Direktanspruch)",
            "Verordnung (EG) 261/2004 (Fluggastrechte)",
            "Verordnung (EG) 1371/2007 (Bahnfahrgastrechte)",
            "Athener Uebereinkommen 2002 (Schiffsreisende)",
            "Paragrafen 407, 425 bis 439, 449, 451, 467 HGB (Frachtrecht, Speditionsrecht)",
            "Artikel 17 bis 41 CMR (internationaler Strassengueterverkehr)",
            "Paragrafen 195, 199, 203, 209, 286 BGB",
            "Paragraf 287 ZPO (Schadensschaetzung)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "EuGH", "C-402/07", "19.11.2009", "Slg. 2009, I-10923 (Sturgeon)",
                "Fluggaeste verspaeteter Fluege haben Anspruch auf eine Ausgleichszahlung nach Artikel 7 EG 261/2004, wenn sie ihr Endziel mit einer Verspaetung von drei Stunden oder mehr erreichen; die Ausgleichszahlung steht den Pauschalsaetzen fuer Annullierungen gleich.",
            ),
            Leitentscheidung(
                "EuGH", "C-549/07", "22.12.2008", "Slg. 2008, I-11061 (Wallentin-Hermann)",
                "Ausserordentliche Umstaende nach Artikel 5 Absatz 3 EG 261/2004 setzen voraus, dass sie ihrer Natur und Ursache nach nicht Teil der normalen Ausuebung der Taetigkeit des Luftverkehrsunternehmens sind und tatsaechlich nicht beherrschbar waren; technische Defekte gehoeren grundsaetzlich zur normalen Taetigkeit.",
            ),
            Leitentscheidung(
                "BGH", "IV ZR 199/10", "12.10.2011", "BGHZ 191, 159",
                "Verletzt der Versicherungsnehmer eine Obliegenheit grob fahrlaessig, kann der Versicherer die Leistung nach Paragraf 28 Absatz 2 Satz 2 VVG in einem Verhaeltnis kuerzen, das der Schwere des Verschuldens entspricht; eine 100-Prozent-Kuerzung bleibt aussergewoehnlichen Faellen vorbehalten.",
            ),
            Leitentscheidung(
                "BGH", "IV ZR 32/09", "16.06.2010", "BGHZ 186, 1",
                "Ein Versicherer kann sich auf Leistungsfreiheit wegen vorvertraglicher Anzeigepflichtverletzung Paragraf 19 VVG nur berufen, wenn er den Versicherungsnehmer auf die Folgen einer Anzeigepflichtverletzung in Textform deutlich hingewiesen hat.",
            ),
            Leitentscheidung(
                "BGH", "I ZR 110/16", "21.12.2017", "TranspR 2018, 162",
                "Im internationalen Strassengueterverkehr greift die Haftung des Frachtfuehrers nach Artikel 17 CMR auch bei verschuldensunabhaengig zurechenbaren Schaeden; Entlastung durch Artikel 17 Absatz 2 CMR setzt strikten Nachweis voraus.",
            ),
        ),
        pruefraster=(
            "Welches Vertragsverhaeltnis oder welche Verordnung greift?",
            "Liegt ein Versicherungsfall im Deckungsumfang ohne Ausschluss vor?",
            "Sind Obliegenheiten, Anzeigepflichten und Quoten gewahrt?",
            "Wie hoch ist der Anspruch (Ausgleichszahlung, Schadenersatz, Wiederbeschaffungswert) und welche Hoechstbetraege gelten?",
            "Welche Verjaehrung Paragraf 195 BGB / Paragraf 439 HGB / Artikel 32 CMR ist im Raum?",
        ),
        skelette=(
            "Deckungsanfrage an Versicherer: Versicherungsschein, Schaden, Anspruchsgrundlage, Frist.",
            "Klage gegen Luftverkehrsunternehmen Artikel 7 EG 261/2004: Flugdaten, Verspaetung/Annullierung, Ausgleichsbetrag, ausserordentliche Umstaende.",
            "Frachtklage Paragrafen 425 ff. HGB / Artikel 17 CMR: Frachtvertrag, Schaden, Haftungsbetrag, Verjaehrung.",
        ),
    ))


_register_versicherung_transport()


def _register_it_software() -> None:
    register(Themenprofil(
        key="it-software",
        label="IT- und Softwarerecht (Paragraf 327 BGB, Werk-/Dienstvertrag, AGB, TMG/DSA)",
        rolle="Du arbeitest in einem IT- und softwarerechtlichen Werkstatt-Modus: Vertragstypus (Kauf, Werkvertrag, Dienstvertrag, Cloud, SaaS) bestimmen, AGB-Kontrolle, digitale Produkte Paragrafen 327 ff. BGB, Datenschutz und Plattformhaftung pruefen.",
        stop_kriterien=(
            "IT-Sicherheitsvorfall mit Meldepflicht (Artikel 33 DSGVO 72 Stunden, BSIG, NIS2-RL).",
            "Anspruchsausschluss aus AGB im Unternehmer- oder Verbrauchergeschaeft mit Existenzfolge.",
            "Open-Source-Lizenzverletzung (GPL, AGPL, MIT) mit Beseitigungs-/Unterlassungsanspruch.",
            "Cloud- oder SaaS-Auslagerung ohne Auftragsverarbeitungsvertrag Artikel 28 DSGVO.",
            "Auslandsbezug mit unklarem Forum oder Rechtswahl (Rom I).",
        ),
        stationen=(
            WorkflowStation(
                title="Vertragstypus und Leistungsbild",
                eingang="Vertragsunterlagen (SaaS-, Lizenz-, Werkvertrag, Pflegevertrag, Nutzungsbedingungen), Leistungsbeschreibung, SLA, Preisbestandteile.",
                pruefung="Vertragstypus: Software-Erwerb auf Dauer (Paragrafen 433, 453 BGB), Werkvertrag bei Individualentwicklung (Paragrafen 631 ff. BGB), Dienstvertrag bei laufender Pflege (Paragrafen 611 ff. BGB), Mietvertrag bei zeitlich begrenzter Ueberlassung (Paragraf 535 BGB), Pauschalreise digitaler Inhalte; bei Verbrauchern Paragrafen 327 ff. BGB (Aktualisierungspflicht Paragraf 327f BGB).",
                arbeitsprodukt="Vertragsraster mit Vertragstypus, Leistungspflichten, Verguetungsstruktur.",
            ),
            WorkflowStation(
                title="AGB-Kontrolle und Haftung",
                eingang="AGB-Texte, individuelle Abreden, Haftungsklauseln, Verfuegbarkeitszusagen, Datenschutzklauseln.",
                pruefung="Einbeziehungskontrolle Paragraf 305 BGB, Ueberraschungs- und Mehrdeutigkeitsregel Paragraf 305c BGB, Inhaltskontrolle Paragrafen 307 bis 309 BGB; Haftungsausschluss fuer leichte Fahrlaessigkeit, Kardinalpflichten, Datenverluste; Verfuegbarkeitszusagen und Vertragsstrafenklauseln Paragraf 309 Nummer 6 BGB.",
                arbeitsprodukt="AGB-Pruefraster mit unwirksamen Klauseln und Auswirkungen.",
            ),
            WorkflowStation(
                title="Digitale Produkte und Aktualisierung",
                eingang="Verbraucherbezug, Datenpreis, Funktionsumfang, Aktualisierungszeitraum.",
                pruefung="Bereitstellung Paragraf 327b BGB, Mangelbegriff Paragraf 327e BGB, Aktualisierungspflicht Paragraf 327f BGB (auch fuer Datenpreis), Beweislastumkehr Paragraf 327k BGB (binnen Jahresfrist), Aenderungen Paragraf 327r BGB.",
                arbeitsprodukt="Pruefraster digitale Produkte mit Mangelfolgenrecht.",
            ),
            WorkflowStation(
                title="Open Source, Lizenzen und IP",
                eingang="Quellcode, Lizenzangaben, Repository, Distributionsweg, eigene und fremde Komponenten.",
                pruefung="Lizenzbestand (GPL v2/3, AGPL, MIT, Apache 2.0), Copyleft-Klauseln, Hinweispflichten, Sublizenzierung; Paragrafen 31, 32, 32a UrhG (Nutzungsrechte, Vertragsanpassung); Paragraf 69a ff. UrhG (Computerprogramme).",
                arbeitsprodukt="Lizenzraster mit Compliance-Status und Handlungsempfehlungen.",
            ),
            WorkflowStation(
                title="Datenschutz, Auftragsverarbeitung, Sicherheit",
                eingang="Verarbeitungsverzeichnis, Auftragsverarbeitungsvertrag, technische und organisatorische Massnahmen, Audits, Subprozessoren.",
                pruefung="Artikel 28 DSGVO (AVV), Artikel 32 DSGVO (TOM), Artikel 33, 34 DSGVO (Meldepflichten), Drittlandtransfer Artikel 44 ff. DSGVO; NIS2-Richtlinie / BSIG Meldepflichten kritischer Anlagen.",
                arbeitsprodukt="Datenschutz- und Sicherheitsraster mit Pflichtenkatalog.",
            ),
            WorkflowStation(
                title="Streit, Anspruch und Schriftsatz",
                eingang="Maengelruegen, Schadensersatzforderungen, Konventionalstrafen, Ruecktritt, Minderung.",
                pruefung="Anspruchsgrundlagen Paragrafen 434, 437, 280, 281, 323, 326 BGB; Paragrafen 633, 634 BGB; Paragrafen 327i bis n BGB; Paragraf 254 BGB (Mitverschulden); Lizenzanalogie und Bereicherung bei Lizenzueberschreitung.",
                arbeitsprodukt="Anspruchsbuendel mit Rechenwerk und Schriftsatzkern.",
            ),
        ),
        pflichtnormen=(
            "Paragrafen 305, 305c, 307 bis 309 BGB (AGB-Kontrolle)",
            "Paragrafen 327, 327a bis 327u BGB (digitale Produkte)",
            "Paragrafen 433, 434, 437 BGB (Kaufrecht)",
            "Paragrafen 535, 538 BGB (Mietrecht)",
            "Paragrafen 611, 619a BGB (Dienstvertrag)",
            "Paragrafen 631, 633, 634, 635, 636 BGB (Werkvertrag)",
            "Paragrafen 280, 281, 286, 323, 326 BGB (Leistungsstoerungen)",
            "Paragrafen 69a bis 69g UrhG (Computerprogramme)",
            "Artikel 28, 32, 33, 34, 44 DSGVO",
            "Paragrafen 8a, 8b BSIG (kritische Infrastruktur, NIS2-Umsetzung)",
            "Verordnung (EU) 2022/2065 (Digital Services Act, DSA)",
            "Verordnung (EU) 2024/1689 (KI-Verordnung)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "BGH", "VIII ZR 295/14", "06.04.2016", "BGHZ 209, 270 (Standardsoftware-Erschoepfung)",
                "Der Erwerb einer Standardsoftware mit Lizenz auf Dauer ist als Sachkauf nach Paragrafen 433, 453 BGB einzuordnen; das urheberrechtliche Erschoepfungsprinzip Paragraf 69c Nummer 3 UrhG erfasst auch downloadbasierte Software, sofern das Recht zur Vervielfaeltigung auf den Ersterwerber begrenzt war.",
            ),
            Leitentscheidung(
                "BGH", "I ZR 26/12", "11.07.2013", "GRUR 2014, 264 (UsedSoft)",
                "Der Weiterverkauf gebrauchter Softwarelizenzen ist zulaessig, sofern das Vervielfaeltigungsstueck mit Zustimmung des Rechteinhabers erstmals in Verkehr gebracht wurde und der Ersterwerber seine eigene Kopie nach dem Verkauf unbrauchbar macht.",
            ),
            Leitentscheidung(
                "BGH", "X ZR 31/02", "07.10.2003", "BGHZ 156, 234",
                "Bei der Erstellung individueller Software liegt ein Werkvertrag Paragrafen 631 ff. BGB vor; die Abnahme Paragraf 640 BGB setzt voraus, dass das Werk im Wesentlichen vertragsgemaess ist und keine die Gebrauchstauglichkeit beeintraechtigenden Maengel aufweist.",
            ),
            Leitentscheidung(
                "EuGH", "C-203/15", "21.12.2016", "ECLI:EU:C:2016:970 (Tele2 Sverige)",
                "Eine allgemeine und unterschiedslose Vorratsdatenspeicherung verletzt Artikel 7, 8 und 11 GRCh; nationale Regelungen sind nur zulaessig, soweit sie auf das absolut Notwendige beschraenkt sind und richterliche oder unabhaengige Vorabkontrolle vorsehen.",
            ),
            Leitentscheidung(
                "BGH", "I ZR 51/19", "30.04.2020", "GRUR 2020, 1027 (Cookie-Einwilligung II)",
                "Die Einwilligung in das Setzen nicht erforderlicher Cookies muss aktiv erteilt werden; vorausgewaehlte Checkboxen reichen weder nach Paragraf 25 TTDSG noch nach der DSGVO aus.",
            ),
        ),
        pruefraster=(
            "Welcher Vertragstypus passt auf das Leistungsbild?",
            "Sind AGB-Klauseln einbezogen und inhaltlich wirksam?",
            "Greifen Paragrafen 327 ff. BGB (digitale Produkte) und welche Pflichten ergeben sich?",
            "Sind Open-Source-Lizenzbedingungen eingehalten?",
            "Sind DSGVO/NIS2-Pflichten erfuellt, insbesondere AVV und TOM?",
        ),
        skelette=(
            "Maengelruege Software: Vertragstyp, Mangelbeschreibung, Nachbesserungsfrist, Rechtsfolgen.",
            "Schriftsatz Werkvertrag: Werkleistung, Maengel, Nachbesserung Paragraf 635 BGB, Ruecktritt Paragraf 636 BGB.",
            "Open-Source-Compliance-Memo: Lizenzinventar, Pflichten, Konsequenzen, Massnahmen.",
        ),
    ))


_register_it_software()


def _register_register() -> None:
    register(Themenprofil(
        key="register",
        label="Register- und Notariatsrecht (FamFG, GBO, HGB, BNotO)",
        rolle="Du arbeitest in einem registerrechtlichen Werkstatt-Modus: Anmeldung, Eintragung oder Loeschung in Handels-, Vereins-, Genossenschafts-, Grundbuch- oder Schiffsregister vorbereiten; notarielle Beurkundung und Beglaubigung pruefen.",
        stop_kriterien=(
            "Eintragungsfrist (insbesondere im Grundbuch und Erbschein) im Raum.",
            "Notarielle Form Paragraf 311b BGB oder Paragraf 15 GmbHG fehlt.",
            "Vollmachtsmangel oder Vertretungsmangel.",
            "Verdacht auf Geldwaesche Paragraf 43 GwG, Meldepflicht.",
            "Datenschutz- und Aktengeheimnisbelange im Register unklar.",
        ),
        stationen=(
            WorkflowStation(
                title="Antrags- und Eintragungslage",
                eingang="Anmeldeerklaerung, Notarurkunde, Vollmachten, Registerauszug, Gesellschaftsvertrag, Erbschein, Bestaetigungen.",
                pruefung="Antragsberechtigung Paragrafen 12, 14 HGB, Paragraf 13 GBO, Paragraf 24 FamFG; Pflichtinhalte Anmeldung; Form (oeffentliche Beglaubigung Paragraf 129 BGB, notarielle Beurkundung Paragraf 128 BGB).",
                arbeitsprodukt="Aktenuebersicht mit Anmeldegegenstand, Antragsbeteiligten und Pflichtangaben.",
            ),
            WorkflowStation(
                title="Inhaltliche Pruefung",
                eingang="Eintragungsgrundlagen, materielle Voraussetzungen, Bewilligungen Paragraf 19 GBO, Voreintragung Paragraf 39 GBO.",
                pruefung="Materielle Eintragungsvoraussetzung pruefen (Eigentum, Erbfolge, Gesellschaftsbestand, Vereinsregister Paragrafen 21 ff. BGB); Reihenfolge der Eintragungen Paragraf 17 GBO; oeffentlicher Glaube des Grundbuchs Paragraf 892 BGB.",
                arbeitsprodukt="Pruefraster mit materiellen Voraussetzungen und Belegquellen.",
            ),
            WorkflowStation(
                title="Notarielle Mitwirkung",
                eingang="Notarurkunde, Vollzugsanzeige, Belehrungspflichten Paragraf 17 BeurkG, Identitaetspruefung Paragraf 10 GwG.",
                pruefung="Beurkundung Paragrafen 8 ff. BeurkG, Belehrung Paragraf 17 BeurkG, Vorlage Genehmigungen Paragraf 1822 BGB / Paragraf 1643 BGB, Vorkaufsrechte Paragrafen 24, 28 BauGB, Verwalterzustimmung Paragraf 12 WEG, steuerliche Unbedenklichkeitsbescheinigung Paragraf 22 GrEStG.",
                arbeitsprodukt="Vollzugsplan mit Belehrungsprotokoll und behoerdlichen Schritten.",
            ),
            WorkflowStation(
                title="Zwischenverfuegung und Abhilfe",
                eingang="Zwischenverfuegung Paragraf 18 GBO, Beanstandung Paragraf 26 HGB, Beschwerde Paragraf 71 GBO / Paragraf 374 FamFG.",
                pruefung="Eintragungshindernis identifizieren, Heilungsmoeglichkeiten, Frist; Beschwerdezustaendigkeit und Beschwerdebefugnis pruefen.",
                arbeitsprodukt="Abhilfeschriftsatz oder Beschwerde mit Antraegen, Beweisangeboten und Fristen.",
            ),
            WorkflowStation(
                title="Folgewirkung und Anschluss",
                eingang="Eintragungsnachricht, Registerauszug, oeffentliche Bekanntmachung, Mitteilungspflichten.",
                pruefung="Mitteilung an Beteiligte Paragraf 32 GBO, Bekanntmachung Paragraf 10 HGB, Bestaetigung an Notar Paragraf 53 BeurkG; Folgeantraege (Loeschungsbewilligung, Berichtigung).",
                arbeitsprodukt="Nachgangsplan mit Bekanntmachungen, Folgeantraegen und Aktenpflege.",
            ),
        ),
        pflichtnormen=(
            "Paragrafen 8 bis 53 BeurkG",
            "Paragrafen 7 bis 17 BNotO",
            "Paragrafen 12, 14, 25, 26, 29, 32, 53, 354 FamFG",
            "Paragrafen 13, 17, 18, 19, 22, 39, 71 GBO",
            "Paragraf 892 BGB (oeffentlicher Glaube), Paragrafen 873, 874, 877 BGB",
            "Paragrafen 8, 10, 12, 14, 26 HGB",
            "Paragrafen 1822, 1643 BGB (Genehmigungen)",
            "Paragrafen 10 ff. GwG (Identitaetsfeststellung)",
            "Paragraf 22 GrEStG (steuerliche Unbedenklichkeit)",
            "Paragrafen 311b BGB, 15 GmbHG, 23 ff. AktG (Form)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "BGH", "V ZB 226/11", "15.03.2012", "BGHZ 193, 1",
                "Eine Vormerkung Paragraf 883 BGB sichert den Anspruch auf Aenderung eines dinglichen Rechts; sie kann durch Bewilligung des Berechtigten oder einstweilige Verfuegung eingetragen werden, ohne dass es einer materiellen Pruefung des Anspruchs durch das Grundbuchamt bedarf.",
            ),
            Leitentscheidung(
                "BGH", "II ZB 8/12", "15.10.2013", "BGHZ 198, 354",
                "Bei der Eintragung von Aenderungen im Handelsregister ist die formelle Beweiskraft Paragraf 12 HGB zu beachten; das Registergericht prueft Tatsachen, soweit erforderlich, im Wege des Freibeweises (Paragraf 26 FamFG).",
            ),
            Leitentscheidung(
                "BGH", "V ZB 145/16", "27.04.2017", "ZIP 2017, 1379",
                "Eine grundbuchliche Berichtigung Paragraf 22 GBO wegen unrichtiger Eintragung kann ohne Bewilligung erfolgen, wenn die Unrichtigkeit nachgewiesen ist; der Nachweis erfordert oeffentliche Urkunden Paragraf 29 GBO.",
            ),
            Leitentscheidung(
                "BGH", "V ZB 87/14", "21.05.2015", "NJW-RR 2015, 1099",
                "Das Grundbuchamt darf eine Auflassung nur eintragen, wenn die in Paragraf 925 BGB geforderte gleichzeitige Anwesenheit der Vertragsparteien vor dem Notar nachgewiesen ist; eine getrennte Beurkundung ist nicht statthaft.",
            ),
            Leitentscheidung(
                "BGH", "II ZB 7/19", "10.12.2019", "BGHZ 224, 80",
                "Die Anmeldung einer geaenderten Geschaeftsfuehrung zum Handelsregister Paragraf 39 GmbHG setzt eine wirksame Bestellung und Annahme voraus; ein Widerruf der Bestellung wirkt erst mit Zugang Paragraf 130 BGB, die Eintragung wirkt deklaratorisch.",
            ),
        ),
        pruefraster=(
            "Wer ist antragsberechtigt und in welcher Form ist die Anmeldung einzureichen?",
            "Sind die materiellen Eintragungsvoraussetzungen und Bewilligungen Paragraf 19 GBO gegeben?",
            "Wurde notariell ordnungsgemaess belehrt und identifiziert?",
            "Welche behoerdlichen Genehmigungen sind erforderlich (Familiengericht, Betreuungsgericht, Vorkaufsrechte)?",
            "Sind Zwischenverfuegungen oder Beschwerden Paragraf 71 GBO veranlasst?",
        ),
        skelette=(
            "Anmeldung Handelsregister: Antragsteller, Anmeldegegenstand, beigefuegte Urkunden, Beglaubigung.",
            "Grundbuchantrag: Antrag, Bewilligung Paragraf 19 GBO, Belegliste, Frist.",
            "Beschwerde Paragraf 71 GBO: Beschwerdegegenstand, Beschwerdegrund, Antrag, Anlagen.",
        ),
    ))


_register_register()


def _register_bauplanung_umwelt() -> None:
    register(Themenprofil(
        key="bauplanung-umwelt",
        label="Bauplanungs- und Umweltrecht (BauGB, BauNVO, BImSchG, UmwRG)",
        rolle="Du arbeitest in einem bauplanungs- und umweltrechtlichen Werkstatt-Modus: Bauleitplanung, Genehmigungen, Immissionsschutz, Naturschutz und Umweltvertraeglichkeit; Normenkontrolle Paragraf 47 VwGO, Verbandsklage Paragrafen 1, 2 UmwRG.",
        stop_kriterien=(
            "Anhoerungs- oder Klagefrist (Paragraf 47 Absatz 2 VwGO 1 Jahr; Paragraf 4 UmwRG; Bauantragsfrist).",
            "Sofortige Vollziehung der Baugenehmigung oder Stilllegungsverfuegung Paragraf 80 Absatz 2 Nummer 4 VwGO.",
            "Naturschutzrechtliche Eingriffsregelung oder FFH-Vertraeglichkeit unklar.",
            "Anerkannte Umweltvereinigung ohne Beteiligungsrechte gehoert.",
            "Denkmalschutzrechtliche Genehmigung fehlt.",
        ),
        stationen=(
            WorkflowStation(
                title="Bauleitplan und Vorhabenbezug",
                eingang="Flaechennutzungsplan, Bebauungsplan, Vorhabenbeschreibung, Aufstellungsbeschluss, Beteiligungsverfahren.",
                pruefung="Erforderlichkeit der Planung Paragraf 1 Absatz 3 BauGB, Abwaegungsgebot Paragraf 1 Absatz 7 BauGB, Verfahren Paragrafen 3, 4 BauGB, Umweltbericht Paragraf 2 Absatz 4 BauGB.",
                arbeitsprodukt="Plan-Steckbrief mit Verfahrensstand, Abwaegungsmaterial und Beteiligungsfristen.",
            ),
            WorkflowStation(
                title="Genehmigungsfaehigkeit",
                eingang="Bauantrag, Baulast, Nachbarrechte, BImSchG-Genehmigung, Wasserrecht, Naturschutz, Denkmalschutz.",
                pruefung="Planungsrechtliche Zulaessigkeit Paragrafen 29 bis 35 BauGB; bauordnungsrechtliche Anforderungen Landes-BauO; immissionsschutzrechtliche Genehmigung Paragrafen 4 ff. BImSchG; wasserrechtliche Erlaubnis Paragrafen 8 ff. WHG; artenschutzrechtliches Toetungsverbot Paragraf 44 BNatSchG.",
                arbeitsprodukt="Pruefraster Genehmigungsfaehigkeit mit Beteiligungs- und Anhoerungsschritten.",
            ),
            WorkflowStation(
                title="Nachbar- und Drittklagen",
                eingang="Drittbetroffenheit, Schutznormen, Ruecksichtnahmegebot, Abstandsflaechen.",
                pruefung="Nachbarschutz aus Paragrafen 30, 31, 34, 35 BauGB; Ruecksichtnahmegebot Paragraf 15 Absatz 1 Satz 2 BauNVO; immissionsschutzrechtlicher Nachbarschutz Paragraf 5 BImSchG; Klagebefugnis Paragraf 42 Absatz 2 VwGO.",
                arbeitsprodukt="Drittschutzraster mit Verletzung schuetzender Normen und Klagebefugnis.",
            ),
            WorkflowStation(
                title="Umweltrechtsbehelfe",
                eingang="Anerkannte Vereinigung, Verbandsklagebefugnis Paragraf 2 UmwRG, Plan- oder Genehmigungsverfahren.",
                pruefung="Verbandsklage Paragraf 2 UmwRG, materielle Pruefung Paragraf 4 UmwRG, UVP-Erforderlichkeit Paragrafen 5 ff. UVPG, Einwendungspraeklusion (vor EuGH C-137/14 weitgehend aufgegeben), Beteiligungsrechte Paragraf 9 UVPG.",
                arbeitsprodukt="Pruefraster Umweltrechtsbehelfe mit Vereinigungsstatus, Klagegrund, Beweisangeboten.",
            ),
            WorkflowStation(
                title="Eilrechtsschutz und Verfahren",
                eingang="Sofortvollzug, einstweilige Anordnung, Normenkontrolle Paragraf 47 VwGO, Anfechtungsklage Paragraf 42 VwGO.",
                pruefung="Antrag Paragraf 80 Absatz 5 VwGO; Antrag Paragraf 47 Absatz 6 VwGO; Folgenabwaegung; UVP-relevante Fehler Paragraf 4 UmwRG (absolute Verfahrensfehler).",
                arbeitsprodukt="Antrags- oder Klageschriftkern mit Antraegen, Beweisen und Anregungen.",
            ),
            WorkflowStation(
                title="Arbeitsprodukt und Folgewirkungen",
                eingang="Zielprodukt (Stellungnahme im Bauleitplanverfahren, Normenkontrollantrag, Anfechtungsklage, Verbandsklage, Eilantrag).",
                pruefung="Pflichtangaben Paragraf 81 VwGO, Antrag, Sachverhalt, Begruendung, Beweis; Anschluss (Termin, Vergleich, Vollstreckungsschutz).",
                arbeitsprodukt="Vollstaendiger Schriftsatz mit Anschlussplan, Streitwertvorschlag und Risikohinweis.",
            ),
        ),
        pflichtnormen=(
            "Paragrafen 1, 2, 3, 4, 9, 10, 14, 29 bis 35 BauGB",
            "Paragrafen 15, 22, 23 BauNVO",
            "Paragrafen 4, 5, 6, 7, 10, 25 BImSchG",
            "Paragrafen 8, 12, 18, 19 WHG",
            "Paragrafen 14, 15, 44 BNatSchG",
            "Paragrafen 1, 2, 4, 5 UmwRG",
            "Paragrafen 5, 7, 9 UVPG",
            "Paragrafen 42, 47, 80, 113 VwGO",
            "Paragraf 35 VwVfG (Verwaltungsakt)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "BVerwG", "4 C 9.14", "06.06.2015", "BVerwGE 152, 138",
                "Das in Paragraf 15 Absatz 1 Satz 2 BauNVO verankerte Ruecksichtnahmegebot vermittelt Nachbarschutz, soweit qualifizierte Beeintraechtigungen vorliegen; massgeblich ist eine Abwaegung der jeweiligen Schutzwuerdigkeit und Schutzbeduerftigkeit.",
            ),
            Leitentscheidung(
                "EuGH", "C-137/14", "15.10.2015", "ECLI:EU:C:2015:683 (Kommission/Deutschland)",
                "Die deutsche Einwendungspraeklusion im UmwRG ist unionsrechtswidrig, soweit sie anerkannten Umweltvereinigungen die gerichtliche Geltendmachung umweltbezogener Rechtsverstoesse versagt, die nicht bereits im Verwaltungsverfahren vorgebracht wurden.",
            ),
            Leitentscheidung(
                "BVerwG", "7 C 21.12", "24.10.2013", "BVerwGE 148, 155",
                "Verstoesse gegen die Pflicht zur Durchfuehrung einer Umweltvertraeglichkeitspruefung sind absolute Verfahrensfehler Paragraf 4 Absatz 1 UmwRG; sie fuehren ohne weitere Kausalitaetspruefung zur Aufhebung der Entscheidung.",
            ),
            Leitentscheidung(
                "BVerwG", "4 CN 7.10", "23.06.2011", "BVerwGE 140, 53",
                "Die gerichtliche Kontrolle eines Bebauungsplans erstreckt sich auf die Einhaltung des Abwaegungsgebots Paragraf 1 Absatz 7 BauGB; es ist verletzt, wenn eine Abwaegung ueberhaupt nicht stattgefunden hat, wesentliche Belange uebersehen oder unverhaeltnismaessig gewichtet wurden.",
            ),
            Leitentscheidung(
                "EuGH", "C-535/18", "28.05.2020", "ECLI:EU:C:2020:391",
                "Auch nicht anerkannte Buerger koennen wesentliche Verfahrensfehler im UVP-Verfahren ruegen; nationales Recht muss einen wirksamen Rechtsbehelf vorsehen, der die Pruefung umweltbezogener Vorgaben ermoeglicht.",
            ),
        ),
        pruefraster=(
            "Welcher Verfahrensstand (Bauleitplanung, Genehmigung, Klage) ist erreicht und welche Fristen laufen?",
            "Welche planungsrechtliche Zulaessigkeit (Paragrafen 29 bis 35 BauGB) und welche Fachgenehmigungen sind erforderlich?",
            "Welche Drittschutznormen (Ruecksichtnahmegebot, Abstandsflaechen, Immissionsschutz) sind verletzt?",
            "Welche Umweltrechtsbehelfe Paragrafen 1, 2, 4 UmwRG kommen in Betracht?",
            "Ist Eilrechtsschutz Paragrafen 47 Absatz 6, 80 Absatz 5 VwGO geboten?",
        ),
        skelette=(
            "Stellungnahme im Bauleitplanverfahren: Sachvortrag, Bezugnahme auf Belange, Antrag.",
            "Normenkontrollantrag Paragraf 47 VwGO: Antrag, Beteiligte, Antragsbefugnis, Begruendung, Antragsfrist.",
            "Verbandsklage Paragraf 2 UmwRG: Anerkennung, Klagegegenstand, Klagebefugnis, Begruendung mit Verfahrens- und Materialfehlern.",
        ),
    ))


_register_bauplanung_umwelt()


def _register_verbraucher_praxis() -> None:
    register(Themenprofil(
        key="verbraucher-praxis",
        label="Verbraucher- und Verfahrenspraxis (Paragrafen 312 ff. BGB, Vollstreckung, Zwang)",
        rolle="Du arbeitest in einem verbraucher- und vollstreckungsrechtlichen Werkstatt-Modus: Widerrufs- und Informationspflichten, Forderungsmanagement, Mahnverfahren, Zwangsvollstreckung Paragrafen 704 ff. ZPO, Verbraucherinsolvenz und Schuldenbereinigung.",
        stop_kriterien=(
            "Widerrufsfrist Paragrafen 355 ff. BGB.",
            "Mahnbescheid mit Widerspruchsfrist Paragraf 692 ZPO (2 Wochen).",
            "Zwangsvollstreckung in Wohnraum mit drohender Raeumung.",
            "Verbraucherinsolvenz mit Restschuldbefreiung im Raum.",
            "Inkasso mit unzulaessigen Kostenforderungen Paragraf 13a RDG.",
        ),
        stationen=(
            WorkflowStation(
                title="Vertrags- und Widerrufslage",
                eingang="Vertragsunterlagen, Belehrungstexte, Bestellbestaetigung, Lieferschein, Widerrufserklaerung.",
                pruefung="Verbraucherbegriff Paragraf 13 BGB, Vertragstyp (Fernabsatz Paragrafen 312c, 312g BGB, ausserhalb Geschaeftsraeume Paragraf 312b BGB, Verbraucherbauvertrag Paragraf 650i BGB, Verbraucherdarlehen Paragrafen 491 ff. BGB), Belehrungs- und Informationspflichten Artikel 246 ff. EGBGB.",
                arbeitsprodukt="Pruefraster Vertragstypus und Widerrufslage.",
            ),
            WorkflowStation(
                title="Forderungs- und Mahnverfahren",
                eingang="Rechnungen, Mahnungen, Verzugseintritt Paragraf 286 BGB, Mahnbescheid Paragrafen 688 ff. ZPO.",
                pruefung="Mahnbescheid und Vollstreckungsbescheid Paragraf 699 ZPO; Widerspruch Paragraf 692 ZPO; Verbraucherbeschwerde gegen unberechtigte Inkassokosten Paragrafen 13a, 13b RDG; Verjaehrung Paragrafen 195, 199 BGB.",
                arbeitsprodukt="Forderungsraster mit Verzugsbeginn, Zinslauf, Mahnkosten und Verjaehrung.",
            ),
            WorkflowStation(
                title="Zwangsvollstreckung",
                eingang="Titel (Urteil, Vollstreckungsbescheid, Notarurkunde), Klausel, Zustellung, Schuldnervermoegen.",
                pruefung="Voraussetzungen Paragrafen 704, 724 ff., 750 ZPO; Vollstreckungsorgane (Gerichtsvollzieher, Vollstreckungsgericht); Pfaendung beweglicher Sachen Paragrafen 803 ff. ZPO, Forderungspfaendung Paragrafen 829 ff. ZPO, Immobiliarvollstreckung ZVG; Pfaendungsschutz Paragrafen 850 ff. ZPO, P-Konto Paragraf 850k ZPO.",
                arbeitsprodukt="Vollstreckungsplan mit Massnahmen, Schutzantraegen und Fristen.",
            ),
            WorkflowStation(
                title="Verbraucherinsolvenz",
                eingang="Insolvenzantrag, ausserschulische Einigung, Schuldenbereinigungsplan, Vermoegenslage.",
                pruefung="Aussergerichtlicher Einigungsversuch Paragraf 305 Absatz 1 Nummer 1 InsO, gerichtlicher Einigungsversuch Paragraf 305a InsO, Restschuldbefreiung Paragrafen 286 ff. InsO (3 Jahre seit 2020), Versagungsgruende Paragraf 290 InsO.",
                arbeitsprodukt="Pruefraster Verbraucherinsolvenz mit Anlagen Paragraf 305 InsO.",
            ),
            WorkflowStation(
                title="Schriftsatz und Antrag",
                eingang="Zielprodukt (Widerrufserklaerung, Klage, Mahnbescheid, Vollstreckungsantrag, Insolvenzantrag).",
                pruefung="Pflichtangaben, Adressat, Antrag, Sachverhalt, Beweis, Anlagen; Kostenrisiko und Beratungshilfe Paragrafen 1 ff. BerHG.",
                arbeitsprodukt="Vollstaendiger Schriftsatz mit Anschluss (Stundungsantrag, Vermoegensauskunft, P-Konto, PKH).",
            ),
        ),
        pflichtnormen=(
            "Paragrafen 13, 14 BGB",
            "Paragrafen 312 bis 312k BGB",
            "Paragrafen 355 bis 361 BGB (Widerruf)",
            "Paragrafen 491 bis 505 BGB (Verbraucherdarlehen)",
            "Paragrafen 650i bis 650o BGB (Verbraucherbauvertrag)",
            "Artikel 246 ff. EGBGB",
            "Paragrafen 688 bis 703d, 750 bis 945 ZPO",
            "Paragraf 850k ZPO (Pfaendungsschutzkonto)",
            "Paragrafen 286 bis 303 InsO (Restschuldbefreiung)",
            "Paragrafen 13a, 13b RDG",
            "Paragrafen 195, 199, 286 BGB",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "EuGH", "C-186/16", "20.09.2017", "ECLI:EU:C:2017:703 (Andriciuc)",
                "Bei Verbrauchervertraegen muessen Klauseln klar und verstaendlich abgefasst sein Artikel 4 Absatz 2 RL 93/13/EWG; bei Fremdwaehrungsdarlehen sind die Folgen eines Wechselkursrisikos transparent zu machen, andernfalls ist die Klausel unwirksam.",
            ),
            Leitentscheidung(
                "BGH", "XI ZR 33/19", "18.06.2019", "BGHZ 222, 192",
                "Eine Widerrufsinformation in Verbraucherdarlehensvertraegen Paragraf 492 Absatz 2 BGB ist nur ordnungsgemaess, wenn sie hinreichend klar und verstaendlich ueber Beginn und Folgen des Widerrufs informiert; fehlerhafte Informationen verlaengern die Widerrufsfrist.",
            ),
            Leitentscheidung(
                "BGH", "VIII ZR 220/16", "16.05.2017", "BGHZ 215, 75",
                "Der Verbraucher ist nicht verpflichtet, einen Mangel selbst nachzuweisen, wenn binnen sechs Monaten Paragraf 477 BGB nach Gefahrenuebergang ein Sachmangel auftritt; in diesem Fall wird die Mangelhaftigkeit beim Gefahrenuebergang vermutet.",
            ),
            Leitentscheidung(
                "BGH", "VII ZB 56/14", "18.07.2017", "BGHZ 215, 287",
                "Der Schuldnerschutz nach Paragraf 850k ZPO setzt eine konkrete Pfaendungsfreigrenze voraus; die Bank muss bei Vorlage einer Bescheinigung das Konto entsprechend einrichten und kann Schadensersatzpflichten ausgesetzt sein, wenn sie Schutzgrenzen missachtet.",
            ),
            Leitentscheidung(
                "BGH", "IX ZR 169/19", "07.05.2020", "ZIP 2020, 1196",
                "Die Restschuldbefreiung Paragrafen 286 ff. InsO ist auf die in der Insolvenz angemeldeten Forderungen begrenzt; ausgeschlossen sind Forderungen aus vorsaetzlich begangenen unerlaubten Handlungen Paragraf 302 Nummer 1 InsO bei rechtzeitiger Anmeldung.",
            ),
        ),
        pruefraster=(
            "Liegt ein Verbrauchergeschaeft und welcher Vertragstyp vor?",
            "Sind Belehrungs- und Informationspflichten Artikel 246 EGBGB vollstaendig erfuellt?",
            "Welche Frist (Widerruf, Mahnbescheid, Vollstreckung) laeuft konkret?",
            "Welche Pfaendungsschutzantraege Paragrafen 850 ff. ZPO sind erforderlich?",
            "Welche Wege zur Schuldenbereinigung (aussergerichtlich, Insolvenz) bestehen?",
        ),
        skelette=(
            "Widerrufserklaerung: Vertragsbezeichnung, Datum, Erklaerung, Rueckabwicklung, Beweisangebot.",
            "Mahnbescheidsantrag Paragraf 690 ZPO: Antragsteller, Antragsgegner, Hauptforderung, Nebenforderungen, Anspruchsbezeichnung.",
            "Insolvenzantrag Verbraucher Paragraf 305 InsO: Antrag, Bescheinigung Schuldnerberatungsstelle, Schuldenbereinigungsplan, Vermoegens- und Glaeubigerverzeichnis.",
        ),
    ))


_register_verbraucher_praxis()


def _register_zivilrecht_allgemein() -> None:
    register(Themenprofil(
        key="zivilrecht-allgemein",
        label="Allgemeines Zivilrecht (BGB AT/BT, Vertrag, Bereicherung, Anfechtung)",
        rolle="Du arbeitest in einem allgemeinen zivilrechtlichen Werkstatt-Modus: Anspruchsgrundlagen pruefen, Tatbestandsmerkmale subsumieren, Einwendungen und Einreden gegenpruefen, Vertrag, gesetzliches Schuldverhaeltnis, Bereicherungs- und Anfechtungsrecht systematisch durcharbeiten.",
        stop_kriterien=(
            "Verjaehrung Paragrafen 195, 199, 214 BGB im Raum (Jahresende).",
            "Anfechtungsfrist Paragraf 121 BGB oder Paragraf 124 BGB laeuft.",
            "Anwaltszwang Paragraf 78 ZPO bei Landgericht und Berufungsinstanz.",
            "Formerfordernis Paragrafen 125, 311b BGB nicht gewahrt.",
            "Auslandsbezug mit unklarer Rechtswahl oder Rom-I-/II-Anknuepfung.",
        ),
        stationen=(
            WorkflowStation(
                title="Anspruchsaufbau",
                eingang="Sachverhalt, Parteibegehren, Vertragsunterlagen, Schriftverkehr, Belege, Zeugen.",
                pruefung="Wer will was von wem woraus? Anspruchsgrundlagen-Pruefschema (vertraglich, vertragsaehnlich, gesetzlich, dinglich, bereicherungsrechtlich, deliktisch); Tatbestandsmerkmale benennen und subsumieren.",
                arbeitsprodukt="Pruefraster mit Anspruchsgrundlage, Tatbestand, Subsumtion, Rechtsfolge.",
            ),
            WorkflowStation(
                title="Vertragsschluss und Auslegung",
                eingang="Angebot, Annahme, AGB, Vertretungslage, Bedingungen, Befristungen.",
                pruefung="Vertragsschluss Paragrafen 145 ff. BGB; Auslegung Paragrafen 133, 157 BGB; Stellvertretung Paragrafen 164 ff. BGB; Anfechtung Paragrafen 119, 123 BGB; AGB Paragrafen 305 ff. BGB; Bedingung und Befristung Paragrafen 158 ff. BGB.",
                arbeitsprodukt="Vertragsanalyse mit Inhalt, Wirksamkeit und Auslegungsergebnis.",
            ),
            WorkflowStation(
                title="Leistungsstoerung",
                eingang="Pflichtverletzung, Unmoeglichkeit, Verzug, Schaden, Mitverschulden.",
                pruefung="Paragrafen 280 bis 286, 311a, 323, 326 BGB; Schadensersatz statt Leistung, neben Leistung, Aufwendungsersatz; Mitverschulden Paragraf 254 BGB; Vorteilsausgleichung.",
                arbeitsprodukt="Anspruchsraster mit Leistungsstoerung, Verschulden, Schaden und Rechtsfolgen.",
            ),
            WorkflowStation(
                title="Gesetzliche Schuldverhaeltnisse",
                eingang="Geschaeftsfuehrung ohne Auftrag, ungerechtfertigte Bereicherung, deliktische Anspruche.",
                pruefung="Paragrafen 677 ff. BGB (GoA); Paragrafen 812 ff. BGB (Leistungs-, Eingriffs-, Aufwendungs-, Rueckgriffskondiktion); Paragrafen 823, 826, 831, 832 BGB (Delikt); Paragraf 254 BGB; Paragraf 249 BGB Schadensbegriff.",
                arbeitsprodukt="Pruefraster gesetzliches Schuldverhaeltnis mit Konkurrenz zu Vertragsanspruechen.",
            ),
            WorkflowStation(
                title="Einwendungen, Einreden und Vollstreckung",
                eingang="Einwendungen (rechtshindernd, rechtsvernichtend), Einreden (Verjaehrung, Zurueckbehaltung), Aufrechnung, Vollstreckungsstrategie.",
                pruefung="Erst Einwendungen, dann Einreden; Verjaehrung Paragrafen 195, 199, 214 BGB; Aufrechnung Paragrafen 387 ff. BGB; Zurueckbehaltungsrecht Paragrafen 273, 274, 320 BGB; Titel und Vollstreckung Paragrafen 704 ff. ZPO.",
                arbeitsprodukt="Gegenpruefraster mit Einwand/Einrede und Auswirkung auf Anspruch.",
            ),
            WorkflowStation(
                title="Arbeitsprodukt und Anschluss",
                eingang="Zielprodukt (Memo, Vertragsentwurf, Mahnung, Klage, Stellungnahme).",
                pruefung="Pflichtangaben (Antrag, Begruendung, Beweis), Streitwert Paragraf 3 ZPO, Zustaendigkeit Paragrafen 12 ff. ZPO, Anwaltszwang.",
                arbeitsprodukt="Vollstaendiger Schriftsatz mit Anschluss (Vergleich, Verhandlung, Vollstreckung).",
            ),
        ),
        pflichtnormen=(
            "Paragrafen 119, 121, 123, 124 BGB (Anfechtung)",
            "Paragrafen 133, 157, 242 BGB",
            "Paragrafen 145 bis 157 BGB (Vertragsschluss)",
            "Paragrafen 164 bis 181 BGB (Stellvertretung)",
            "Paragrafen 195, 199, 214 BGB (Verjaehrung)",
            "Paragrafen 249 bis 254 BGB (Schadensrecht)",
            "Paragrafen 273, 320 BGB (Zurueckbehaltung, Einrede des nicht erfuellten Vertrags)",
            "Paragrafen 280 bis 286, 311a, 323, 326 BGB",
            "Paragrafen 305 bis 310 BGB (AGB)",
            "Paragrafen 387 bis 396 BGB (Aufrechnung)",
            "Paragrafen 677 bis 687 BGB (GoA)",
            "Paragrafen 812 bis 822 BGB (Bereicherung)",
            "Paragrafen 823 bis 853 BGB (Delikt)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "BGH", "VIII ZR 305/19", "10.06.2020", "BGHZ 226, 130",
                "Bei der Schadensermittlung im Kaufrecht steht der Lehre vom Schaden auch der entgangene Gewinn Paragraf 252 BGB zur Seite; die Beweiserleichterung in Paragraf 252 Satz 2 BGB ist konsequent anzuwenden.",
            ),
            Leitentscheidung(
                "BGH", "VII ZR 168/13", "22.05.2014", "BGHZ 201, 263",
                "Die Wirksamkeit von AGB im B2B-Verkehr ist nach Paragrafen 307 ff. BGB zu pruefen; das Leitbild des dispositiven Rechts gilt als Wertungsmassstab auch zwischen Unternehmern.",
            ),
            Leitentscheidung(
                "BGH", "II ZR 246/15", "11.10.2016", "BGHZ 212, 116",
                "Eine Anfechtung wegen arglistiger Taeuschung Paragraf 123 BGB erfordert eine vorsaetzliche Erregung oder Aufrechterhaltung eines Irrtums; Schweigen auf nachfragepflichtige Tatsachen kann eine Taeuschung darstellen, wenn eine Aufklaerungspflicht besteht.",
            ),
            Leitentscheidung(
                "BGH", "VI ZR 19/14", "30.09.2014", "BGHZ 202, 242",
                "Ein Schadensersatzanspruch aus Paragraf 823 Absatz 1 BGB setzt voraus, dass die schaedigende Handlung in ein absolutes Recht eingegriffen hat; eine Pflicht zur Schadenshinderung kann sich aus einer vorhandenen Gefahrenquelle ergeben (Verkehrssicherungspflicht).",
            ),
            Leitentscheidung(
                "BGH", "XI ZR 318/15", "28.06.2016", "BGHZ 211, 105",
                "Ungerechtfertigte Bereicherung Paragrafen 812 ff. BGB tritt ein, wenn die Leistung ohne Rechtsgrund erfolgte; der Rueckforderungsanspruch ist gegen den Empfaenger gerichtet und durch Paragraf 818 BGB begrenzt.",
            ),
        ),
        pruefraster=(
            "Wer will was von wem auf welcher Anspruchsgrundlage?",
            "Sind alle Tatbestandsmerkmale belegt und welcher Beweis ist erforderlich?",
            "Welche Einwendungen, Einreden, Anfechtungs- oder Verjaehrungsgruende greifen?",
            "Welche Konkurrenz besteht zwischen vertraglichem, gesetzlichem und deliktischem Anspruch?",
            "Welche Form, Zustaendigkeit und Frist ist zu wahren?",
        ),
        skelette=(
            "Klageschrift: Bezeichnung der Parteien, Zustaendigkeit, Antrag, Sachverhalt, rechtliche Wuerdigung mit Anspruchsgrundlage und Subsumtion, Beweisangebote.",
            "Schriftsatz Anfechtungserklaerung Paragraf 143 BGB: Anfechtungsgrund, Erklaerung, Frist, Rueckabwicklung.",
            "Bereicherungsklage Paragraf 812 BGB: Leistung, fehlender Rechtsgrund, Bereicherungsgegenstand, Bereicherung des Empfaengers.",
        ),
    ))


_register_zivilrecht_allgemein()


def _register_internationales_handelsrecht() -> None:
    register(Themenprofil(
        key="internationales-handelsrecht",
        label="Internationales Handelsrecht (CISG, Rom I/II, EuGVVO, Schiedsverfahren)",
        rolle="Du arbeitest in einem international-handelsrechtlichen Werkstatt-Modus: Anwendbares Recht (Rom I/II), Zustaendigkeit (Brussel Ia / EuGVVO), Wiener UN-Kaufrecht (CISG), Schiedsgerichtsbarkeit (UNCITRAL, ICC, DIS), Vollstreckung auslaendischer Titel (Brussel Ia, NY-UeK).",
        stop_kriterien=(
            "Klage-, Schiedsantrags- oder Vollstreckungsfristen.",
            "Rechtswahl oder Gerichtsstandsvereinbarung unklar.",
            "Sanktionen, Embargo, Exportkontrolle (Russland, Iran, Belarus).",
            "Datenfluss in Drittland mit unklarem Schutzniveau Artikel 44 ff. DSGVO.",
            "Schiedsspruch mit ordre-public-Bedenken Artikel V NY-UeK.",
        ),
        stationen=(
            WorkflowStation(
                title="Anknuepfung und Zustaendigkeit",
                eingang="Vertrag, Sitzlaender, Lieferorte, Vereinbarungen ueber Rechtswahl und Gerichtsstand, Schiedsklausel.",
                pruefung="Verordnung (EG) 593/2008 Rom I (Vertragsrecht), Verordnung (EG) 864/2007 Rom II (ausservertraglich), Verordnung (EU) 1215/2012 Brussel Ia (Zustaendigkeit, Vollstreckung); Anknuepfungspunkte (gewoehnlicher Aufenthalt, charakteristische Leistung); Schiedsklausel Artikel II NY-UeK.",
                arbeitsprodukt="Pruefraster mit anwendbarem Recht, zustaendigem Gericht und Schiedsfaehigkeit.",
            ),
            WorkflowStation(
                title="CISG-Pruefung",
                eingang="Sitz beider Parteien, Vertragsgegenstand, Ausschluss CISG, Allgemeine Geschaeftsbedingungen.",
                pruefung="Anwendungsbereich Artikel 1, 2, 3 CISG; Ausschluss Artikel 6 CISG; Vertragsschluss Artikel 14 bis 24 CISG; Vertragsmaessigkeit der Ware Artikel 35 CISG; Pflichten und Rechtsbehelfe Artikel 45 ff. CISG; Erfuellungsanspruch Artikel 46 CISG, Schadensersatz Artikel 74 CISG, Aufhebung Artikel 49, 64 CISG.",
                arbeitsprodukt="Pruefraster CISG mit Pflichten, Rechtsbehelfen und Schadensberechnung.",
            ),
            WorkflowStation(
                title="Schiedsverfahren",
                eingang="Schiedsklausel, Schiedsordnung (ICC, DIS, UNCITRAL), Sitz, Sprache, Schiedsrichter.",
                pruefung="Wirksamkeit Schiedsklausel Artikel II NY-UeK / Paragrafen 1029 ff. ZPO; Schiedsfaehigkeit; Bildung Schiedsgericht; einstweiliger Rechtsschutz Paragraf 1041 ZPO; Anerkennung und Vollstreckung Artikel V NY-UeK / Paragrafen 1060 ff. ZPO.",
                arbeitsprodukt="Verfahrensplan Schiedsverfahren mit Antraegen, Beweis und Vollstreckungsperspektive.",
            ),
            WorkflowStation(
                title="Sanktionen und Compliance",
                eingang="Lieferketten, Endkunden, AussenwirtschaftsG, EU-Verordnungen 833/2014, 269/2014.",
                pruefung="Sanktionslistenpruefung; Genehmigungspflichten Paragrafen 4, 11 AWG, Paragraf 79 AWV; Strafbarkeit Paragraf 18 AWG; Ausfuhrkontrolle Dual-Use-VO.",
                arbeitsprodukt="Compliance-Raster mit Sanktionsabgleich und Genehmigungsfragen.",
            ),
            WorkflowStation(
                title="Vollstreckung",
                eingang="Auslaendischer Titel oder Schiedsspruch, Vermoegen, Vollstreckungsstaaten.",
                pruefung="Brussel Ia ab 2015 keine Vollstreckbarerklaerung mehr Artikel 39 EuGVVO; NY-UeK Anerkennungs- und Versagungsgruende Artikel V; Paragrafen 1060 bis 1062 ZPO.",
                arbeitsprodukt="Vollstreckungsplan mit Massnahmen je Forum.",
            ),
            WorkflowStation(
                title="Schriftsatz und Vertragsgestaltung",
                eingang="Zielprodukt (Klage, Schiedsklage, Settlement Agreement, Sanktionsmemo).",
                pruefung="Pflichtangaben, klare Bezugnahme auf Rechtsgrundlagen, Sprachenregelung, Anlagenkonvolut, Sprache der Anlagen (englisch zulaessig nach Paragraf 184 GVG?).",
                arbeitsprodukt="Vollstaendiger Schriftsatz oder Vertragsentwurf mit Anschlussplan.",
            ),
        ),
        pflichtnormen=(
            "Verordnung (EG) 593/2008 Rom I",
            "Verordnung (EG) 864/2007 Rom II",
            "Verordnung (EU) 1215/2012 Brussel Ia",
            "UN-Kaufrechtsuebereinkommen (CISG)",
            "New Yorker UNUeK 1958",
            "Paragrafen 1025 bis 1066 ZPO (Schiedsverfahren)",
            "Paragrafen 4, 11, 18 AWG; Paragraf 79 AWV",
            "Verordnung (EU) 833/2014 (Russland-Sanktionen)",
            "Verordnung (EG) 428/2009 / Verordnung (EU) 2021/821 (Dual-Use)",
            "Paragrafen 32, 38 ZPO",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "EuGH", "C-381/08", "25.02.2010", "Slg. 2010, I-1255 (Car Trim)",
                "Bei grenzueberschreitenden Vertraegen ueber die Lieferung von Waren Artikel 7 Nummer 1 lit. b Spiegelstrich 1 EuGVVO ist der Erfuellungsort grundsaetzlich der Ort, an dem die Waren nach dem Vertrag geliefert wurden oder haetten geliefert werden muessen.",
            ),
            Leitentscheidung(
                "BGH", "VIII ZR 304/00", "30.06.2004", "BGHZ 159, 280",
                "Eine ausdrueckliche Ausschluessklausel ist erforderlich, um die Anwendung des CISG nach Artikel 6 wirksam abzubedingen; eine Klausel, die nur das BGB als anwendbares Recht bestimmt, schliesst das CISG nicht aus.",
            ),
            Leitentscheidung(
                "EuGH", "C-126/97", "01.06.1999", "Slg. 1999, I-3055 (Eco Swiss)",
                "Ein Schiedsspruch ist nach Artikel V Absatz 2 lit. b NY-UeK aufzuheben, wenn er gegen den nationalen ordre public verstoesst; dazu gehoeren wesentliche Grundsaetze wie das Verbot der Wettbewerbsbeschraenkung Artikel 101 AEUV.",
            ),
            Leitentscheidung(
                "BGH", "I ZB 91/15", "30.06.2016", "ZIP 2016, 1832",
                "Schiedsspruch wird im Inland anerkannt, wenn keine Versagungsgruende Artikel V NY-UeK vorliegen; die Pruefung beschraenkt sich auf den ordre public und die Wirksamkeit der Schiedsvereinbarung.",
            ),
            Leitentscheidung(
                "EuGH", "C-352/13", "21.05.2015", "ECLI:EU:C:2015:335 (CDC Hydrogen Peroxide)",
                "Bei kartellrechtlichen Schadensersatzklagen Artikel 7 Nummer 2 EuGVVO ist als Tatort sowohl der Ort der schaedigenden Handlung als auch der Ort des Schadenseintritts anzusehen.",
            ),
        ),
        pruefraster=(
            "Welches Recht ist nach Rom I/II anwendbar und ist das CISG einschlaegig?",
            "Welches Gericht ist nach Brussel Ia zustaendig oder greift eine Schiedsklausel?",
            "Sind Sanktionen, Exportkontrolle und Compliance gewahrt?",
            "Welche Sprache und Form ist fuer Schriftsaetze und Schiedsverfahren erforderlich?",
            "Welche Vollstreckungsstrategie laesst sich nach NY-UeK / Brussel Ia umsetzen?",
        ),
        skelette=(
            "Settlement Agreement: Vertragsparteien, Recital, Rechtswahl, Streitbeilegung, Vertraulichkeit.",
            "Schiedsklage: Schiedsklausel, Antrag, Sachverhalt, anwendbares Recht, Beweis, Schiedsrichterauswahl.",
            "Sanktionsmemo: Sachverhalt, Sanktionsregime, Pflichtenkatalog, Risikomatrix, Handlungsempfehlung.",
        ),
    ))


_register_internationales_handelsrecht()


def _register_legistik() -> None:
    register(Themenprofil(
        key="legistik",
        label="Legistik und oeffentliche Haushaltskontrolle (GGO, BHO, NKR)",
        rolle="Du arbeitest in einem legistischen Werkstatt-Modus: Gesetzes- und Verordnungsentwurfe pruefen, GGO-Vorgaben anwenden, Folgenabschaetzung und Buerokratiekosten ermitteln, Hochschul- und Haushaltsrechtsfragen einordnen.",
        stop_kriterien=(
            "Kabinettstermin, Ressortabstimmung oder Bundesrats-Frist im Raum.",
            "Bestimmtheitsgebot Artikel 80 Absatz 1 Satz 2 GG nicht erfuellt.",
            "Verstoss gegen Konnexitaetsprinzip Artikel 104a Absatz 4 GG.",
            "Haushaltsplan und Vollzugswirkung Paragrafen 1 ff. BHO unklar.",
            "Folgenabschaetzung und KMU-Test nach GGO fehlen.",
        ),
        stationen=(
            WorkflowStation(
                title="Regelungsbedarf und Zielsystem",
                eingang="Regelungsauftrag, Problembeschreibung, vorhandene Rechtslage, EU-Vorgaben, Koalitionsvertrag.",
                pruefung="Erforderlichkeit, Geeignetheit, Alternativen, Zielbestimmung, Adressatenkreis, Beziehung zu hoeherrangigem Recht (GG, Unionsrecht, EMRK).",
                arbeitsprodukt="Problemaufriss mit Zielen, Alternativen und betroffenen Adressaten.",
            ),
            WorkflowStation(
                title="Rechtsetzungstechnik",
                eingang="Entwurfstext, Begruendung, Aenderungsbefehle, Anlagen.",
                pruefung="GGO Anlagen 1 bis 9; Bestimmtheit, Klarheit, Widerspruchsfreiheit, Rechtsfolgenabschaetzung; Aenderungsbefehl, Inkrafttreten, Uebergangsregelung; Einheitlichkeit von Begriff und Verweisung.",
                arbeitsprodukt="Entwurfstext mit Aenderungsmarkern, Begruendungsentwurf und Synopse.",
            ),
            WorkflowStation(
                title="Folgenabschaetzung und Buerokratiekosten",
                eingang="Zahlen zu Adressaten, Verfahren, Datenquellen, Modellrechnungen.",
                pruefung="Erfuellungsaufwand fuer Buerger, Wirtschaft und Verwaltung; Buerokratiekostenindex; KMU-Test; Demografieabschaetzung; Geschlechterperspektive; Nachhaltigkeitspruefung.",
                arbeitsprodukt="Folgenabschaetzungsblatt nach GGO mit Buerokratiekosten und Erfuellungsaufwand.",
            ),
            WorkflowStation(
                title="Verfahren und Beteiligung",
                eingang="Ressortabstimmung, Laenderbeteiligung, Verbaendeanhoerung, Bundesrat, Bundestag.",
                pruefung="Pflichten GGO Paragrafen 47 ff., Beteiligung Bundesrat Artikel 76, 77 GG, Einbringung Artikel 76 GG, Vermittlungsausschuss Artikel 77 Absatz 2 GG; bei Hochschulrecht Konnexitaetspruefung.",
                arbeitsprodukt="Verfahrensplan mit Beteiligungsschritten, Fristen und Adressaten.",
            ),
            WorkflowStation(
                title="Haushaltsbezug",
                eingang="Haushaltsplan, Wirtschaftsplan, Verpflichtungsermaechtigungen, Bewirtschaftung.",
                pruefung="Paragrafen 1 ff. BHO (Grundsaetze), Paragraf 6 BHO (Wirtschaftlichkeit), Paragrafen 23, 24 BHO (Veranschlagung), Paragrafen 34, 37 BHO (Bewirtschaftung), Paragraf 7 BHO (Zweckbindung).",
                arbeitsprodukt="Haushaltsabsatz mit Mittelbedarf, Deckungsquelle und Wirtschaftlichkeitspruefung.",
            ),
            WorkflowStation(
                title="Schriftbild und Anschluss",
                eingang="Entwurf, Begruendung, Synopse, Stellungnahmen, Konsultationen.",
                pruefung="Klare Formulierung, Fachsprache, geschlechtersensible Formulierung, Inkrafttretensdatum, Evaluierungsklausel.",
                arbeitsprodukt="Vollstaendiger Entwurfstext mit Begruendung, Anlagen und Verfahrenshinweisen.",
            ),
        ),
        pflichtnormen=(
            "Artikel 70 bis 82 GG (Gesetzgebung)",
            "Artikel 104a bis 115 GG (Finanzverfassung)",
            "Paragrafen 1 bis 8 BHO (Haushaltsgrundsaetze)",
            "Paragrafen 23, 24, 34, 44 BHO (Veranschlagung, Bewirtschaftung)",
            "GGO Anlagen 1 bis 9",
            "Paragrafen 1, 5 NKRG (Normenkontrollrat)",
            "Verordnung (EU, Euratom) 2018/1046 (Haushaltsordnung der Union)",
            "Paragraf 80 GG (Verordnungsermaechtigung)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "BVerfG", "2 BvR 624/97", "13.10.1998", "BVerfGE 99, 88",
                "Verordnungsermaechtigungen Artikel 80 Absatz 1 Satz 2 GG erfordern Inhalt, Zweck und Ausmass der erteilten Ermaechtigung in einem Mass, das vorhersehbar macht, in welchen Faellen und mit welcher Tendenz von der Ermaechtigung Gebrauch gemacht werden kann.",
            ),
            Leitentscheidung(
                "BVerfG", "2 BvF 1/05", "17.12.2007", "BVerfGE 119, 331",
                "Das Konnexitaetsprinzip Artikel 104a Absatz 4 GG verpflichtet den Bund, den Laendern die zur Erfuellung uebertragener Aufgaben erforderlichen Mittel zur Verfuegung zu stellen; eine Aufgabenuebertragung ohne entsprechende Finanzausstattung ist unzulaessig.",
            ),
            Leitentscheidung(
                "BVerfG", "2 BvR 1402/13", "12.10.2017", "BVerfGE 147, 50",
                "Haushaltsgesetzgebung muss dem Grundsatz der Wahrheit und Klarheit Paragraf 11 HGrG genuegen; die Bewilligung von Krediten ist auf Tatbestaende beschraenkt, die einen Bedarf nach Massgabe der Haushaltsrechtlichkeit Artikel 110 GG ausweisen.",
            ),
            Leitentscheidung(
                "BVerfG", "2 BvE 2/08", "30.06.2009", "BVerfGE 123, 267 (Lissabon)",
                "Demokratie- und Integrationsverantwortung des Bundestages erfordern bei der Mitwirkung an Rechtsetzungsakten der EU eine ausreichende Begruendungstiefe und Subsidiaritaetspruefung Artikel 23 GG.",
            ),
            Leitentscheidung(
                "BVerwG", "10 C 12.07", "16.10.2008", "BVerwGE 132, 105",
                "Hochschulrechtliche Normen muessen den Anforderungen an Bestimmtheit und Wesentlichkeitsdoktrin gerecht werden; pruefungsrechtliche Eingriffe duerfen nur durch oder aufgrund Gesetzes erfolgen.",
            ),
        ),
        pruefraster=(
            "Liegt eine Gesetzgebungs- oder Verordnungskompetenz vor und sind Bestimmtheit Artikel 80 GG gewahrt?",
            "Werden GGO-Vorgaben (Folgenabschaetzung, Erfuellungsaufwand) eingehalten?",
            "Ist die Haushaltslage Paragrafen 6, 23, 34 BHO ausreichend abgebildet?",
            "Wurden Bundesrat, Laender, Verbaende und EU-Stellen sachgerecht beteiligt?",
            "Ist Konnexitaet, Demografie- und Nachhaltigkeitsbezug dokumentiert?",
        ),
        skelette=(
            "Gesetzentwurf: Vorblatt, A. Problem, B. Loesung, C. Alternativen, D. Haushaltsausgaben, E. Erfuellungsaufwand, F. Weitere Kosten; Entwurfstext mit Aenderungsbefehlen.",
            "Verordnungsentwurf: Vorblatt, Rechtsgrundlage Artikel 80 GG, Anhoerungsergebnis, Begruendung mit Folgenabschaetzung.",
            "Hochschulrechtsnovelle: Ausgangslage, Zielsetzung, Rechtswirkung, Konnexitaetsraster, Verfahrensplan.",
        ),
    ))


_register_legistik()


def _register_wissenschaft_lehre() -> None:
    register(Themenprofil(
        key="wissenschaft-lehre",
        label="Rechtswissenschaft, Methodenlehre, Klausurpraxis",
        rolle="Du arbeitest in einem wissenschaftlich-didaktischen Werkstatt-Modus: Methodenlehre (Auslegung, Subsumtion), Rechtsgeschichte und -philosophie, Klausur- und Hausarbeitstechnik, Lehrmaterial fuer Studium und Examen.",
        stop_kriterien=(
            "Eigenstaendige Loesung der Klausur (keine fertigen Klausurloesungen mit Punktverteilung als Endprodukt).",
            "Pruefungsrechtlicher Bezug mit Bewertungsspielraum Paragraf 25 HRG.",
            "Plagiat / Zitiergebot verletzt.",
            "Forschungsdatenbestand mit Personenbezug ungesichert.",
            "Aufgabenstellung verlangt anwaltliches Mandatsergebnis (anderer Werkstatt-Modus).",
        ),
        stationen=(
            WorkflowStation(
                title="Aufgabenanalyse",
                eingang="Sachverhalt, Frage, Pruefungsfach, Bearbeitungszeit, Hilfsmittel.",
                pruefung="Frage zerlegen, Adressat (Gutachten, Anwaltsmemo, Urteil, Aufsatz), Schwerpunkte erkennen, Bearbeitungsplan mit Zeitanteilen.",
                arbeitsprodukt="Aufgabenanalyse mit Schwerpunkten und Pruefungsplan.",
            ),
            WorkflowStation(
                title="Methodischer Zugang",
                eingang="Norm, Sachverhalt, Lehrbuchwissen, Rechtsprechung.",
                pruefung="Vier Auslegungsmethoden Savignys (Wortlaut, Systematik, Historie, Telos); europarechtskonforme und verfassungskonforme Auslegung; Analogie- und Umkehrschluss; Subsumtion in vier Schritten.",
                arbeitsprodukt="Methodisches Geruest mit Auslegungsergebnis und Subsumtion.",
            ),
            WorkflowStation(
                title="Quellen- und Literaturarbeit",
                eingang="Lehrbuecher, Kommentare, Fachzeitschriften, Datenbanken (juris, beck-online), Rechtsprechungs-Aufsaetze.",
                pruefung="Quellenkritik (Aktualitaet, Reichweite, Stimmen in der Literatur), Zitierweise (Paragraf 13a HRG analog, akademische Zitierregeln, Kommentarzitate, OFD-Verwaltungsanweisungen).",
                arbeitsprodukt="Quellenkatalog mit kurzer Inhaltsbeschreibung und Zitierform.",
            ),
            WorkflowStation(
                title="Gutachten oder Klausurloesung",
                eingang="Frage, Pruefraster, Skelett (Anspruchsgrundlagen, Tatbestand, Subsumtion, Ergebnis).",
                pruefung="Gutachtenstil (Obersatz, Definition, Subsumtion, Ergebnis), Stilebenen (Gutachten- vs. Urteilsstil), Aufbau (Hauptpunkte, Hilfsgutachten), klare Sprache, keine ueberfluessigen Vorbemerkungen.",
                arbeitsprodukt="Strukturiertes Gutachten oder Klausurentwurf mit Gliederung.",
            ),
            WorkflowStation(
                title="Selbstkontrolle und Feedback",
                eingang="Loesungsskizze, Pruefungskommentare, Notenpunkte, Aufgabensteller.",
                pruefung="Schwerpunkte gesetzt, Subsumtionsdichte, Sprachhandwerk, Klausurzeit, formale Vorgaben.",
                arbeitsprodukt="Selbstkontrolle mit Pruefkriterien und Verbesserungspunkten.",
            ),
        ),
        pflichtnormen=(
            "Paragrafen 1, 2, 5 DRiG (juristische Pruefung)",
            "Paragraf 25 HRG (Pruefungsspielraum)",
            "Paragrafen 133, 157 BGB (Auslegung)",
            "Artikel 20 Absatz 3 GG (Gesetzesbindung)",
            "Artikel 100 GG (Vorlagepflicht)",
            "Paragraf 1 UrhG (Werk und Schoepfungshoehe)",
            "Wissenschaftsethik Bekenntnis (DFG-Kodex)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "BVerfG", "1 BvR 419/81", "17.04.1991", "BVerfGE 84, 34",
                "Pruefungsrechtliche Bewertungen unterliegen einem fachgerichtlich kontrollierten Beurteilungsspielraum; pruefungsspezifische Wertungen sind nur eingeschraenkt ueberpruefbar, fachwissenschaftliche Fragen voll.",
            ),
            Leitentscheidung(
                "BVerfG", "1 BvR 419/81", "17.04.1991", "BVerfGE 84, 59 (Antwortspielraum)",
                "Pruefungsantworten muessen anerkanntermassen vertretbar bewertet werden; eine fachwissenschaftlich vertretbare Antwort darf nicht als falsch gewertet werden, soweit kein Pruefungsspielraum besteht.",
            ),
            Leitentscheidung(
                "BVerfG", "2 BvR 1444/00", "20.02.2001", "BVerfGE 103, 142",
                "Die Vier-Schritt-Methode in der Rechtsanwendung beruht auf dem Wesentlichkeitsgrundsatz; der Gesetzgeber muss wesentliche Entscheidungen selbst treffen, die Methodenlehre dient der konkretisierenden Rechtsanwendung.",
            ),
            Leitentscheidung(
                "BVerwG", "6 C 7.20", "15.10.2020", "BVerwGE 169, 308",
                "Hochschulpruefungen muessen den Grundsatz der Chancengleichheit Artikel 12 GG wahren; Korrektur- und Bewertungsverfahren sind transparent und sachgerecht zu gestalten.",
            ),
            Leitentscheidung(
                "BVerfG", "1 BvR 2436/11", "27.06.2014", "NVwZ-RR 2014, 730",
                "Pruefungsentscheidungen muessen begruendet sein und einer gerichtlichen Ueberpruefung zugaenglich sein; ein blosses Nichtbestehen ohne nachvollziehbare Begruendung verletzt das Recht auf effektiven Rechtsschutz Artikel 19 Absatz 4 GG.",
            ),
        ),
        pruefraster=(
            "Was ist die konkrete Aufgabenstellung und welcher Stil ist gefordert?",
            "Welche Schwerpunkte und Pruefraster ergeben sich aus dem Sachverhalt?",
            "Welche Auslegungsmethode ist anzuwenden und welche Stimmen in der Literatur sind zu beruecksichtigen?",
            "Wie sind Quellen sauber zitiert und plagiatfrei integriert?",
            "Welche Selbstkontrolle ist vor Abgabe sinnvoll?",
        ),
        skelette=(
            "Gutachtenaufbau: Sachverhalt, Frage, Anspruch X gegen Y aus Norm Z, Pruefung Tatbestand, Subsumtion, Ergebnis, Hilfsgutachten.",
            "Hausarbeitsskizze: Problemaufriss, Forschungsfrage, Methodik, These, Argumentation, Forschungsstand, Ergebnis, Literaturverzeichnis.",
            "Pruefungsbearbeitung Klausur: Aufgabenstellung, Loesungsskizze, Zeitplan, Reinabschnitt, Selbstkontrolle.",
        ),
    ))


_register_wissenschaft_lehre()


def _register_praxis_werkzeug() -> None:
    register(Themenprofil(
        key="praxis-werkzeug",
        label="Praxis-Werkzeuge (Recherche, Tabellen, Liquiditaet, Kanzlei-Management)",
        rolle="Du arbeitest in einem werkzeugorientierten Werkstatt-Modus: Recherche, Tabellenreview, Liquiditaetsplanung, Berichtspflichten, Kanzlei-Management; pruefbare Arbeitsprodukte ohne mandatsspezifische Rechtsberatung.",
        stop_kriterien=(
            "Mandatsspezifische Beratung erforderlich (anderer Werkstatt-Modus).",
            "Datenschutz- oder Geheimnisschutzbelange in Datei oder Tool.",
            "Steuer- oder Berufsrechtsbezug ohne mandatierte Fachperson.",
            "Tool-Fehler mit Folgewirkung (kein blindes Vertrauen in Output).",
            "Wirtschaftliche Risikoaussage ohne Fachexpertise.",
        ),
        stationen=(
            WorkflowStation(
                title="Aufgabenbild und Datenlage",
                eingang="Anforderung, Zieldatei (Excel, Word, PDF, CSV), Datenquellen, Zeitrahmen, Adressat.",
                pruefung="Klaerung Ziel (Liquiditaetsplan, Recherche, Tabellenreview), Format, Detailtiefe; Daten qualifizieren (Quelle, Aktualitaet, Datenschutzkennzeichen).",
                arbeitsprodukt="Aufgabenuebersicht mit Zielprodukt, Datenliste und Datenschutzcheck.",
            ),
            WorkflowStation(
                title="Strukturierung und Modell",
                eingang="Rohdaten, Tabellenstruktur, Vorlagen, Formelwerk.",
                pruefung="Daten- und Tabellenmodell entwickeln (Spalten, Aggregationsebene, Zeitachsen); Plausibilitaet (Summenkontrolle, Vorzeichen, Stichtage); Validierungsregeln; Trennung von Eingaben, Berechnungen und Reports.",
                arbeitsprodukt="Modellbeschreibung mit Aufbau, Annahmen und Validierungen.",
            ),
            WorkflowStation(
                title="Operative Umsetzung",
                eingang="Excel-, Word-, PowerPoint-Vorlagen, Skripte, Recherche-Tools, Datenbanken.",
                pruefung="Formeln (z. B. SUMMEWENN, INDEX/VERGLEICH), Cross-Check (Vergleich mit Ist-Werten), Versionskontrolle, Quellenangaben (markdown-/Excel-Kommentare).",
                arbeitsprodukt="Befuelltes Modell oder Recherche-Mappe mit Formelwerk und Quellenliste.",
            ),
            WorkflowStation(
                title="Ergebnisaufbereitung",
                eingang="Tabellen, Diagramme, Berichte, Stakeholderfragen.",
                pruefung="Diagramme nach Zweck (Balken, Linie, Wasserfall); Zahlenklarheit (Dezimaltrennzeichen, Einheiten, Quartale); Erlaeuterungen knapp und sachlich; Versionsstaende.",
                arbeitsprodukt="Lesbarer Bericht mit Tabellen, Diagrammen und Erlaeuterungen.",
            ),
            WorkflowStation(
                title="Qualitaetskontrolle und Folgeschritte",
                eingang="Vier-Augen-Pruefung, Stichproben, Plausibilitaetschecks.",
                pruefung="Sensitivitaetsrechnungen, Worst-/Best-Case, Robustheit von Annahmen; Anschlussplanung (Folgeberichte, Aktualisierungszyklen).",
                arbeitsprodukt="Qualitaetsprotokoll mit Pruefschritten und Aktualisierungsfahrplan.",
            ),
        ),
        pflichtnormen=(
            "Paragrafen 257, 238 HGB (Aufbewahrung, Buchfuehrung)",
            "Paragrafen 145, 146 AO (Aufzeichnungs- und Aufbewahrungspflichten)",
            "Paragraf 1 BDSG, Artikel 5, 6 DSGVO (sofern personenbezogen)",
            "Paragraf 43a Absatz 2 BRAO (Verschwiegenheit, sofern Anwalt)",
            "Paragrafen 90, 147, 165 AO (Schaetzung, Mitwirkung, Ausland)",
            "Paragrafen 1 ff. UStG (Umsatzsteuerpflicht je nach Modell)",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "BGH", "IX ZR 65/14", "16.07.2015", "BGHZ 207, 23",
                "Liquiditaetsplanung und Fortbestehensprognose erfordern eine objektivierte Beurteilung der Zahlungsfaehigkeit; eine ueberwiegende Wahrscheinlichkeit fuer die Zahlungsfaehigkeit muss nach betriebswirtschaftlichen Massstaeben dokumentiert werden.",
            ),
            Leitentscheidung(
                "BFH", "X R 23/16", "21.06.2017", "BFHE 258, 365",
                "Erbringt eine Software-gestuetzte Aufzeichnung steuerlich relevante Daten, muss die Software so beschaffen sein, dass Aenderungen erkennbar und revisionssicher sind; Pflichten Paragrafen 145, 146 AO werden andernfalls verletzt.",
            ),
            Leitentscheidung(
                "BAG", "1 ABR 22/14", "08.09.2015", "NZA 2016, 442",
                "Bei der Einfuehrung von Datenverarbeitungstools ist das Mitbestimmungsrecht des Betriebsrats Paragraf 87 Absatz 1 Nummer 6 BetrVG zu beachten, sofern die Technik geeignet ist, das Verhalten oder die Leistung der Arbeitnehmer zu ueberwachen.",
            ),
            Leitentscheidung(
                "BGH", "IX ZR 25/05", "13.07.2006", "BGHZ 168, 256",
                "Bei der Pruefung wirtschaftlicher Verhaeltnisse ist auf Daten zurueckzugreifen, die nachpruefbar und vollstaendig sind; Schaetzungen sind nur zulaessig, wenn die Datenlage trotz zumutbarer Bemuehungen unvollstaendig bleibt.",
            ),
            Leitentscheidung(
                "BVerwG", "10 B 3.20", "21.04.2021", "Buchholz 451.231 Nummer 14",
                "Ein einheitliches IT-gestuetztes Berichtswesen muss Datensicherheit und Datenschutz sicherstellen; oeffentlich-rechtliche Verpflichtungen zur Berichterstattung sind transparent und revisionsfest zu erfuellen.",
            ),
        ),
        pruefraster=(
            "Welches Zielprodukt ist gefordert und wer ist Adressat?",
            "Sind Daten qualifiziert, datenschutzkonform und revisionssicher?",
            "Ist das Modell so strukturiert, dass Eingaben, Berechnung und Bericht getrennt sind?",
            "Sind Plausibilitaet, Sensitivitaet und Vier-Augen-Pruefung dokumentiert?",
            "Welche Anschlusspflichten (Berichte, Aktualisierungen) bestehen?",
        ),
        skelette=(
            "Liquiditaetsplan: Cash-In, Cash-Out, Endbestand je Woche/Monat, Annahmen, Sensitivitaet.",
            "Tabellenreview: Strukturpruefung, Formelpruefung, Plausibilitaetsfaktor, Befund- und Massnahmenliste.",
            "Rechercheauftrag: Zielfrage, Quellen, Befundliste, Bewertung, Anhang mit Belegen.",
        ),
    ))


_register_praxis_werkzeug()


def _register_spezialrecht() -> None:
    register(Themenprofil(
        key="spezialrecht",
        label="Spezialrecht (Bau-, Medizin-, Agrar-, Sport-, Transport-, Internationales Wirtschaftsrecht)",
        rolle="Du arbeitest in einem fachspezifischen Werkstatt-Modus: Spezialnormen anwenden (VOB/B, HOAI, Bauvertragsrecht; Medizinrecht: KHEntgG, AMG, Heilberufekammergesetze; Agrarrecht: HofuebergabeG, BetriebsprämienVO; Sportrecht: Sportgerichtsbarkeit; Internationales Wirtschaftsrecht: ICC-Regeln, WTO).",
        stop_kriterien=(
            "Spezialrechtliche Frist (z. B. Paragraf 13 Absatz 4 VOB/B Maengelruege, Paragraf 26 KHEntgG, Paragraf 31 KHG).",
            "Patientensicherheit oder Heilbehandlungsstandard tangiert.",
            "Embargos, Sanktionen oder Importbeschraenkungen im Raum.",
            "Sportverbandsrecht mit drohendem Lizenzentzug, Spielsperre, Doping.",
            "Tierschutz, Lebensmittel- oder Pflanzenschutzrecht mit unmittelbarer Gefahr.",
        ),
        stationen=(
            WorkflowStation(
                title="Spezialnorm und Anwendungsbereich",
                eingang="Vertrag, Bescheid, Statut, Vereinbarung; Tätigkeitsfeld.",
                pruefung="Welches Spezialgesetz greift (VOB/B, BGB Bauvertrag Paragrafen 650a ff. BGB; HOAI; AMG, MPG; Tierhaltungsrecht; CAS-Statut; IncoTerms)? Persoenlicher und sachlicher Anwendungsbereich?",
                arbeitsprodukt="Pruefraster Spezialnorm mit Anwendungsbereich und Konkurrenzen.",
            ),
            WorkflowStation(
                title="Sachverhalt und Beweise",
                eingang="Aktenlage, Sachverstaendige, Stationsdokumentation, Gutachten, Aufzeichnungen.",
                pruefung="Beweismittel sammeln (medizinische Befunde, Bauablaufdokumentation, Wettkampfprotokolle, Lieferdokumente); spezialrechtliche Mitwirkungspflichten Paragrafen 4 ff. BO Aerzte, Paragraf 4 VOB/B.",
                arbeitsprodukt="Beweisplan mit Dokumentations- und Sachverstaendigenanforderungen.",
            ),
            WorkflowStation(
                title="Anspruch oder Verteidigung",
                eingang="Anspruchsbegehren oder Verteidigung gegen Massnahme.",
                pruefung="Anspruchsgrundlage im Spezialgesetz (Verguetung Paragraf 7 HOAI, Maengelhaftung Paragraf 634 BGB / Paragraf 13 VOB/B, Behandlungsvertrag Paragrafen 630a ff. BGB, Sportverbandsstatut); Verfahrensbesonderheiten (Schiedsverfahren CAS, FIFA, NADA).",
                arbeitsprodukt="Pruefraster Anspruch oder Verteidigung mit spezialrechtlichen Tatbestaenden.",
            ),
            WorkflowStation(
                title="Verfahren und Schriftsatz",
                eingang="Zustaendige Gerichte, Schiedsstellen, Aufsichtsbehoerden.",
                pruefung="Pflichtangaben, Antrag, Sachverhalt, Beweisangebote, Sprachregelungen (englisch bei internationalem Schiedsverfahren), Vertraulichkeit.",
                arbeitsprodukt="Vollstaendiger Schriftsatz mit Anschlussplan.",
            ),
        ),
        pflichtnormen=(
            "Paragrafen 650a bis 650v BGB (Bauvertrag)",
            "Paragraf 13 VOB/B (Maengel)",
            "Paragrafen 1 bis 14 HOAI",
            "Paragrafen 630a bis 630h BGB (Behandlungsvertrag)",
            "Paragrafen 1 bis 6 KHEntgG, Paragrafen 1 bis 19 KHG",
            "Paragrafen 1 ff. AMG (Arzneimittelrecht)",
            "Paragrafen 1 ff. TierschG, Paragrafen 1 ff. LMBG / LFGB",
            "Statuten internationaler Sportverbaende (IOC, FIFA, UEFA, NADA, CAS)",
            "ICC-Schiedsregeln 2021",
        ),
        leitentscheidungen=(
            Leitentscheidung(
                "BGH", "VII ZR 219/04", "22.06.2006", "BGHZ 168, 145",
                "Bei einem Pauschalpreisvertrag im Baurecht traegt der Auftragnehmer das Mengenrisiko; eine Anpassung kommt nur in Betracht, wenn das Aequivalenzverhaeltnis grob gestoert wird.",
            ),
            Leitentscheidung(
                "BGH", "VI ZR 365/14", "26.11.2015", "BGHZ 207, 369",
                "Bei groben Behandlungsfehlern im Arzthaftungsprozess kehrt sich die Beweislast hinsichtlich der Kausalitaet um Paragraf 630h Absatz 5 BGB; der Behandler hat darzulegen, dass der Schaden auch bei sachgerechter Behandlung eingetreten waere.",
            ),
            Leitentscheidung(
                "BGH", "KZR 26/17", "07.05.2019", "BGHZ 222, 100 (Pferdesportverband)",
                "Verbandsmonopolisten unterliegen der kartellrechtlichen Missbrauchskontrolle Paragraf 19 GWB; Auswahlentscheidungen muessen transparenten, diskriminierungsfreien Kriterien folgen.",
            ),
            Leitentscheidung(
                "CAS", "CAS 2010/A/2235", "11.10.2010", "CAS Bulletin 2010/2, S. 56 (Bohbot)",
                "Sportrechtliche Sanktionen sind dem Grundsatz der Verhaeltnismaessigkeit verpflichtet; Sperren muessen sich an Schwere des Verstosses, individuellen Verantwortlichkeit und Verfahrensgarantien orientieren.",
            ),
            Leitentscheidung(
                "EuGH", "C-415/93", "15.12.1995", "Slg. 1995, I-4921 (Bosman)",
                "Vorschriften ueber Transferregelungen, die Staatsangehoerigkeitsbeschraenkungen oder unverhaeltnismaessige Ablosezahlungen vorsehen, verstossen gegen Artikel 45 AEUV (Arbeitnehmerfreizuegigkeit).",
            ),
        ),
        pruefraster=(
            "Welche Spezialnorm und welcher Anwendungsbereich greift?",
            "Welche Beweis- und Dokumentationspflichten sind erfuellt?",
            "Welche Anspruchsgrundlage oder Verteidigungslinie ist tragfaehig?",
            "Welches Verfahren (staatlich, schiedsgerichtlich, verbandsintern) ist einschlaegig?",
            "Welche Sprach- und Verschwiegenheitspflichten gelten?",
        ),
        skelette=(
            "Bauvertraglicher Schriftsatz: Vertragsgrundlage, Maengelruege Paragraf 13 VOB/B, Mangelbeschreibung, Aufforderung, Frist.",
            "Behandlungsfehlerklage: Behandlungsvertrag, Fehlerbeschreibung, Kausalitaet, Schaden, Beweisangebote (Gutachten), Antrag.",
            "Sportgerichtliche Anhoerung: Verbandsregeln, Sachverhalt, Verteidigung, Antraege (Strafmilderung, Aufschub).",
        ),
    ))


_register_spezialrecht()


def _register_arbeitsrecht_gericht() -> None:
    base = PROFILE["arbeitsrecht"]
    register(Themenprofil(
        key="arbeitsrecht-gericht",
        label="Arbeitsgerichtsbarkeit (richterlich)",
        rolle="Du arbeitest in der Rolle eines arbeitsgerichtlichen Spruchkoerpers (ArbG, LAG, BAG): Gueteverhandlung Paragraf 54 ArbGG, Kammertermin Paragraf 57 ArbGG, Urteil mit Tenor, Tatbestand und Entscheidungsgruenden vorbereiten.",
        stop_kriterien=base.stop_kriterien + (
            "Beschleunigungsgebot Paragraf 9 Absatz 1 ArbGG (Verkuendung binnen drei Wochen).",
            "Annahmeverzug, Beschaeftigungsanspruch und Weiterbeschaeftigungstitel im Raum.",
        ),
        stationen=(
            WorkflowStation(
                title="Gueteverhandlung",
                eingang="Klage, Klageerwiderung, Sachvortrag, Wahrscheinlichkeitsabwaegung.",
                pruefung="Vergleichsmoeglichkeit Paragraf 54 ArbGG; Beschleunigungsgebot; Erfolgsaussichten; Sozialdaten; Hinweispflichten Paragraf 139 ZPO.",
                arbeitsprodukt="Vergleichsvorschlag oder Vorbereitung Kammertermin.",
            ),
            WorkflowStation(
                title="Kammertermin",
                eingang="Schriftsaetze, Beweisangebote, ehrenamtliche Richter, Sachvortrag.",
                pruefung="Beweisaufnahme Paragrafen 58 ff. ArbGG, freie Beweiswuerdigung, Hinweispflichten, Antraege im Termin.",
                arbeitsprodukt="Sitzungsprotokoll mit Antraegen, Beweisaufnahme.",
            ),
            WorkflowStation(
                title="Urteilsentwurf",
                eingang="Beweisaufnahme, Rechtsauffassung, Streitwert.",
                pruefung="Tenor (Beschaeftigung, Kuendigungsschutz, Zahlung), Tatbestand, Entscheidungsgruende, Kosten Paragraf 12a ArbGG (keine Erstattung 1. Instanz), Streitwert Paragraf 42 GKG.",
                arbeitsprodukt="Urteil mit Pflichtangaben Paragraf 313 ZPO.",
            ),
            WorkflowStation(
                title="Rechtsmittel und Vollstreckung",
                eingang="Berufungsfrist Paragraf 66 ArbGG, vorlaeufige Vollstreckbarkeit, Sicherheitsleistung.",
                pruefung="Berufungszulassung Paragraf 64 ArbGG, Revisionszulassung Paragraf 72 ArbGG, vorlaeufige Vollstreckbarkeit Paragraf 62 ArbGG.",
                arbeitsprodukt="Tenor mit Rechtsmittelbelehrung und Vollstreckungsanordnung.",
            ),
        ),
        pflichtnormen=base.pflichtnormen + (
            "Paragrafen 2, 8, 12a, 54, 57, 58, 61, 62, 64, 66, 69, 72 ArbGG",
            "Paragrafen 138, 139, 286, 313 ZPO",
            "Paragraf 42 GKG (Streitwert)",
        ),
        leitentscheidungen=base.leitentscheidungen,
        pruefraster=base.pruefraster + (
            "Ist der Kammertermin entscheidungsreif und Beweisbeduerftigkeit geklaert?",
            "Welche Pflichtangaben braucht das Urteil nach Paragraf 313 ZPO?",
        ),
        skelette=(
            "Vergleichsprotokoll Paragraf 54 ArbGG mit Hauptsacheerledigung, Kostenfolge, Vollstreckungsfaehigkeit.",
            "Urteil Arbeitsgericht: Rubrum, Tenor, Tatbestand, Entscheidungsgruende, Kosten, Streitwert, Rechtsmittel.",
            "Beschluss vorlaeufige Vollstreckbarkeit Paragraf 62 ArbGG.",
        ),
    ))


_register_arbeitsrecht_gericht()


def _register_steuerprozess() -> None:
    base = PROFILE["steuerrecht"]
    register(Themenprofil(
        key="steuerprozess",
        label="Finanzgerichtsbarkeit (richterlich)",
        rolle="Du arbeitest in der Rolle eines finanzgerichtlichen Spruchkoerpers (FG, BFH): Klage- und Antragsverfahren nach FGO, Beweisaufnahme, Urteil mit Tenor und Entscheidungsgruenden Paragraf 105 FGO.",
        stop_kriterien=base.stop_kriterien + (
            "Aussetzung der Vollziehung Paragraf 69 FGO erforderlich.",
            "Nichtzulassungsbeschwerde Paragraf 116 FGO drohend.",
        ),
        stationen=(
            WorkflowStation(
                title="Zulaessigkeit",
                eingang="Klage, Bescheid, Einspruchsentscheidung, Klagefrist Paragraf 47 FGO.",
                pruefung="Statthafte Klageart Paragraf 40 FGO (Anfechtung, Verpflichtung, Feststellung, Leistung), Klagebefugnis Paragraf 40 Absatz 2 FGO, Vorverfahren Paragraf 44 FGO, Klagefrist.",
                arbeitsprodukt="Zulaessigkeitsvermerk mit Pruefraster Paragrafen 40 ff. FGO.",
            ),
            WorkflowStation(
                title="Begruendetheit und Beweis",
                eingang="Verwaltungsakte, steuerliche Aufzeichnungen, Sachverstaendige.",
                pruefung="Amtsermittlung Paragrafen 76, 81 FGO; Beweismittel Paragrafen 81 bis 90 FGO; freie Beweiswuerdigung Paragraf 96 FGO.",
                arbeitsprodukt="Begruendetheitsvermerk mit Subsumtion und Tenorvorschlag.",
            ),
            WorkflowStation(
                title="Urteil und AdV",
                eingang="Beweisaufnahmeergebnis, Rechtsauffassung, AdV-Antrag Paragraf 69 FGO.",
                pruefung="Pflichtangaben Paragraf 105 FGO; AdV bei ernstlichen Zweifeln Paragraf 69 Absatz 2 FGO; Vollstreckungsschutz.",
                arbeitsprodukt="Urteil mit Tenor, Tatbestand, Gruenden, Kosten Paragrafen 135, 136 FGO, Streitwert Paragraf 52 GKG.",
            ),
        ),
        pflichtnormen=base.pflichtnormen + (
            "Paragrafen 40, 44, 47, 69, 76, 81, 96, 100, 105, 115, 116, 135 FGO",
            "Paragraf 52 GKG",
        ),
        leitentscheidungen=base.leitentscheidungen,
        pruefraster=base.pruefraster + (
            "Ist die Klage zulaessig (Statthaftigkeit, Klagebefugnis, Vorverfahren, Frist)?",
            "Welche Pflichtangaben braucht das Urteil Paragraf 105 FGO?",
        ),
        skelette=(
            "Urteil FG: Rubrum, Tenor, Tatbestand, Entscheidungsgruende, Kosten, Streitwert, Rechtsmittel.",
            "Beschluss Paragraf 69 FGO: Aussetzungsantrag, ernstliche Zweifel, Folgenabwaegung.",
            "Vergleichsprotokoll Paragraf 79 FGO (Erledigung in der Hauptsache).",
        ),
    ))


_register_steuerprozess()
