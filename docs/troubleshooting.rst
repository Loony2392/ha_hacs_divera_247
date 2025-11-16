Troubleshooting
===============

Übersetzungen werden nicht angezeigt
------------------------------------
- Nach Updates Integration neu laden oder HA neu starten
- Browser hart neu laden (Strg+F5) oder im Inkognito-Fenster öffnen

Doppelte "Standort"-Einträge
-----------------------------
- Der zusätzliche Standort-Sensor wurde entfernt. Es bleibt nur der ``device_tracker``.
- Falls noch sichtbar, Integration neu laden oder Gerät einmal öffnen/aktualisieren.

Fahrzeugnamen stimmen nicht
---------------------------
- In den Integrations-Optionen den Namensmodus wählen: Auto/Kurzname/Name/Vollständiger Name
- Nach Änderung Integration neu laden, damit Entitäten neu benannt werden

Keine Fahrzeuge auf der Karte
-----------------------------
- Prüfen, ob die ``device_tracker``-Entitäten aktiv sind
- In der Karte die Tracker-Entitäten hinzufügen

Fehler beim Verbinden
---------------------
- Access Key prüfen (Benutzerkonto → Einstellungen → Debug)
- Serveradresse: Standard ist ``https://app.divera247.com``
