Quickstart
==========

Diese Seite führt dich durch die Einrichtung der DIVERA 24/7 Integration in Home Assistant.

Voraussetzungen
---------------
- Home Assistant 2025.2 oder neuer
- DIVERA 24/7 Account
- Zugangsschlüssel (Access Key) aus deinem Benutzerkonto → Einstellungen → Debug

Installation
------------

Über HACS (empfohlen)
~~~~~~~~~~~~~~~~~~~~~
1. HACS öffnen → Integrationen → nach "DIVERA 24/7" suchen
2. Installieren → anschließend Integration hinzufügen

Manuell
~~~~~~~
1. Repository klonen oder als ZIP laden
2. Ordner ``custom_components/divera247`` nach ``config/custom_components/`` kopieren
3. Home Assistant neu starten

Einrichtung in Home Assistant
-----------------------------
1. Einstellungen → Geräte & Dienste → Integration hinzufügen → "DIVERA 24/7"
2. Zugangsschlüssel eingeben
3. Optional: Serveradresse (Standard: https://app.divera247.com)
4. Update-Intervall (10–300 s) wählen
5. Fahrzeug-Namensquelle wählen (Auto/Kurzname/Name/Vollständiger Name)
6. Falls mehrere Einheiten vorhanden sind: aktive Einheiten auswählen

Optionen
--------
- Scan Intervall: 10–300 Sekunden
- Fahrzeug-Namensquelle: Auto, Kurzname, Name, Vollständiger Name

Erstellte Entitäten
-------------------
- Sensoren: letzter Alarm, Alarm-Adresse (mit Attributen inkl. Fahrzeuge), News
- Fahrzeug-Sensoren: Status, Rufname (OPTA), ISSI, Nummer
- Geräte-Tracker: Fahrzeuge mit Position für die Karte
- Select: Benutzer-Status
- Binary Sensor: Aktiver Alarm
- Kalender: Termine

Hinweise
--------
- Der Standort wird nur über den ``device_tracker`` angezeigt (kein doppelter Standort-Sensor).
- Nach einem Update der Übersetzungen ggf. Browser hart neu laden (Strg+F5).
