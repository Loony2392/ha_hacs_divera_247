# Manueller Test — Issues #121, #122, #123 & Security

Diese Checkliste beschreibt, was **du** in einer laufenden Home-Assistant-Instanz
prüfen solltest, um die Änderungen dieses Branches (`fix/security-and-issues-121-122-123`)
zu bestätigen. Am besten mit dem Devcontainer / einer Test-HA-Instanz und einem
echten DIVERA-247-Account mit mindestens einem Fahrzeug und einem (Probe-)Alarm.

## Vorbereitung

-   [ ] Branch in `custom_components/divera247` deiner Test-HA laden und HA neu starten.
-   [ ] Integration DIVERA 24/7 hinzufügen (falls noch nicht vorhanden).

## Issue #123 — Update-Intervall & Fahrzeug-Namensquelle nachträglich änderbar

-   [ ] Einstellungen → Geräte & Dienste → DIVERA 24/7: Es erscheint jetzt ein
        **„Konfigurieren"-Button** (Options-Flow).
-   [ ] Button öffnen → Dialog „⚙️ DIVERA 24/7 Options" zeigt **Update-Intervall**
        und **Fahrzeug-Namensquelle**.
-   [ ] Intervall auf z. B. `30` setzen, speichern → Integration lädt neu, keine Fehler
        im Log. (Wert < 10 oder > 300 muss als Fehler „Value out of allowed range" abgewiesen werden.)
-   [ ] Fahrzeug-Namensquelle ändern (z. B. auf „Name") → nach dem Reload heißen die
        Fahrzeug-Sensoren entsprechend anders.
-   [ ] **Single-Unit-Account:** „Neu konfigurieren" (Reconfigure) starten → es erscheint
        **nicht mehr** nur die Meldung „Dieser Benutzer hat nur eine Einheit", sondern der
        Schritt zur Auswahl der Fahrzeug-Namensquelle.

## Issue #122 — Alarm-Titel (Stichwort) als Attribut

-   [ ] Entwicklerwerkzeuge → Zustände → `binary_sensor.*_active_alarm` (Aktiver Alarm).
-   [ ] Bei einem offenen (Probe-)Alarm hat das Entity ein Attribut **`title`** mit dem
        Alarm-Stichwort (z. B. „F2 Wohnungsbrand").

## Issue #121 — Fahrzeuge mit Namen statt ID

-   [ ] Beim selben `active_alarm`-Sensor das Attribut **`vehicles`** prüfen.
-   [ ] Die Liste enthält **lesbare Fahrzeugnamen** (Shortname/Name/Fullname gemäß Datenlage),
        **nicht** die numerischen IDs.
-   [ ] Fahrzeug, das (noch) nicht in den Clusterdaten steht → Fallback auf die ID als String
        (kein Absturz, Attribut bleibt vorhanden).

## Security / CI

-   [ ] GitHub Actions: Workflow **„HACS Validation"** — nur noch der License-Check offen
        (siehe unten), keine „permissions"-Warnung mehr für `hacs.yml`.
-   [ ] Workflow **„Validate with hassfest"** ist **grün** (URL-in-Übersetzung behoben).
-   [ ] _(Offen, deine Entscheidung)_ LICENSE-Datei hinzufügen → HACS-License-Check wird grün.

## Regression / Grundfunktion

-   [ ] Ersteinrichtung (neuer Account) funktioniert weiterhin: Zugangsschlüssel-Dialog zeigt
        den Link korrekt (Platzhalter `{url}` wird als echte URL gerendert).
-   [ ] Multi-Unit-Account: Cluster-Auswahl bei Reconfigure funktioniert wie zuvor.
-   [ ] Keine doppelten „Reload"-Vorgänge / Warnungen im Log nach Options- oder Reconfigure-Änderung.
