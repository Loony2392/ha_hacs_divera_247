DIVERA 24/7 Integration für Home Assistant
Die DIVERA 24/7 Integration für Home Assistant ermöglicht es dir, Daten und Ereignisse von der DIVERA 24/7-Plattform in dein Home Assistant System zu integrieren. Mit dieser Integration kannst du Informationen zu Alarmeinsätzen, Fahrzeugstatus, Benutzerstatus und vieles mehr abrufen.

Features
Abruf von Alarm- und Notrufereignissen.
Anzeige von Fahrzeugstatusinformationen.
Integration von Benutzerdaten, einschließlich Status und Aktivitäten.
Anzeige von Kalenderereignissen und News.
Möglichkeit zur Konfiguration mehrerer Einheiten (Cluster) innerhalb eines Accounts.
Voraussetzungen
Home Assistant Version 2023.2 oder neuer.
Ein aktiver DIVERA 24/7 Account.
Dein DIVERA 24/7 Zugangsschlüssel (zu finden in deinen Benutzer-Einstellungen unter Debug).
Installation
1. Installation über HACS (Home Assistant Community Store)
Öffne Home Assistant und gehe zu HACS.
Klicke auf "Integrationen" und suche nach "DIVERA 24/7".
Klicke auf "Installieren" und warte, bis die Installation abgeschlossen ist.
Nach der Installation wirst du aufgefordert, die Integration zu konfigurieren.
2. Manuelle Installation
Lade das Repository herunter:
bash
Kopieren
Bearbeiten
git clone https://github.com/Loony2392/ha_hacs_divera_247.git
Kopiere den Ordner custom_components/divera_247 in das Verzeichnis config/custom_components/ deines Home Assistant Setups.
Starte Home Assistant neu.
Konfiguration
Gehe zu Einstellungen > Integrationen in deinem Home Assistant.
Klicke auf "Integration hinzufügen" und wähle DIVERA 24/7.
Gib deinen Zugangsschlüssel (Access Key) und die Server-Adresse ein. Weitere Informationen zum Finden des Zugangsschlüssels findest du hier.
(Optional) Wähle die Einheit (Cluster), die du überwachen möchtest. Standardmäßig wird die Stammeinheit geladen.
Speichere die Konfiguration und starte Home Assistant neu, wenn du dazu aufgefordert wirst.
Optionen
Nach der ersten Konfiguration kannst du die folgenden Optionen anpassen:

Update Intervall: Bestimme das Intervall, in dem die Daten von DIVERA 24/7 aktualisiert werden. Das Intervall muss zwischen 10 und 300 Sekunden liegen.
Verwendung
Verfügbare Entitäten
Die Integration erstellt mehrere Entitäten, die du in deinen Home Assistant Dashboards verwenden kannst:

Sensoren:
sensor.letzter_alarm: Zeigt den letzten Alarm an.
sensor.letzte_news: Zeigt die letzten News von DIVERA 24/7 an.
sensor.fahrzeug_status_{vehicle_name}: Zeigt den Status eines Fahrzeugs an.
Binary Sensoren:
binary_sensor.aktiver_alarm: Zeigt an, ob ein Alarm aktiv ist.
Select:
select.benutzer_status: Zeigt den aktuellen Benutzerstatus an.
Kalender:
calendar.termine: Zeigt alle kommenden Termine an.
Automationen und Benachrichtigungen
Du kannst Automationen und Benachrichtigungen erstellen, die auf den Status von Alarmen, Fahrzeugen oder Benutzern reagieren. Beispiel:

yaml
Kopieren
Bearbeiten
automation:
  - alias: "Benachrichtigung bei Alarm"
    trigger:
      platform: state
      entity_id: binary_sensor.aktiver_alarm
      to: 'on'
    action:
      service: notify.notify
      message: "Es wurde ein aktiver Alarm ausgelöst!"
Fehlerbehebung
Verbindungsfehler: Überprüfe, ob die angegebene Server-Adresse korrekt ist und dass dein Zugangsschlüssel gültig ist.
Authentifizierungsfehler: Stelle sicher, dass du den richtigen Zugangsschlüssel verwendest. Du findest diesen in den Debug-Einstellungen deines DIVERA 24/7 Accounts.
Allgemeine Fehler: Wenn der Fehler weiterhin besteht, starte Home Assistant neu oder wende dich an die Community auf Home Assistant Community Forum.
Beitragen
Wenn du Verbesserungen oder Fehlerbehebungen für diese Integration einreichen möchtest, öffne einen Pull Request (PR). Sieh dir bitte unsere Contributing Guidelines an, bevor du mit dem Beitrag beginnst.

Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert. Siehe die Datei LICENSE für weitere Details.

Hilfe und Unterstützung
Besuche das Home Assistant Forum für allgemeine Unterstützung und Diskussionen.
Melde Fehler oder schlage neue Funktionen auf GitHub Issues vor.
Viel Spaß mit der DIVERA 24/7 Integration! 😎

Zusätzliche Hinweise
Unterstützte Home Assistant Versionen: Die Integration ist mit allen Versionen von Home Assistant kompatibel, die Custom Components unterstützen.
Zukunftspläne: Weitere Funktionen wie Echtzeit-Benachrichtigungen und erweiterte API-Integration werden in zukünftigen Versionen erwartet.
