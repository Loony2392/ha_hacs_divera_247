# <img src="https://www.divera247.com/images/divera247.svg" alt="DIVERA Logo" width="200"> DIVERA 24/7 Integration für Home Assistant 🚨🔔

[![GitHub Release](https://img.shields.io/github/v/release/loony2392/ha_hacs_divera_247?sort=semver&style=for-the-badge&color=green)](https://github.com/loony2392/ha_hacs_divera_247/releases/)
![GitHub Downloads (all releases total)](https://img.shields.io/github/downloads/loony2392/ha_hacs_divera_247/total?style=for-the-badge&label=Downloads%20Total)
[![Ko-Fi](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge)](https://ko-fi.com/loony_tech)

Diese Integration bindet DIVERA 24/7 in Home Assistant ein: Alarme, Fahrzeugdaten, Benutzerstatus, Kalender – übersichtlich und automatisierbar.

## Features ⚡

- 🚨 Abruf von Alarm- und Notrufereignissen.  
   Retrieve alarm and emergency events.

- 🚗 Fahrzeuge: Status, Standort (Diagnose, optional), Rufname (OPTA), ISSI, Nummer; Fahrzeuge erscheinen auf der HA-Karte.  
   Vehicles: status, location (diagnostic, optional), call sign (OPTA), ISSI, number; vehicles appear on the HA map.

- 🧑‍🤝‍🧑 Benutzerdaten: aktueller Benutzerstatus, Statusübersicht (Zählung aktiv/inaktiv/im Dienst).  
   User data: current user status and overview counters (active/inactive/on duty).

- 📅 Kalenderereignisse; letzte News.  
   Calendar events; latest news.

- 🛠️ Mehrere Einheiten (Cluster) auswählbar; Reconfigure änderbar.  
   Multiple units (clusters) selectable; reconfigure later.

- 🧰 Services: Probealarm auslösen; Benutzerstatus per Name setzen.  
   Services: trigger probe alarm; set user status by name.

## Voraussetzungen 📋

- 💻 Home Assistant 2025.2 oder neuer.

- 📝 Aktiver DIVERA 24/7 Account.

- 🔑 Zugangsschlüssel (Benutzer-Einstellungen → Debug).

## Installation 🔧

### 1) Installation über HACS 📦
1. Öffne **Home Assistant** und gehe zu **HACS**.  
   Open **Home Assistant** and go to **HACS**.

2. Klicke auf **"Integrationen"** und suche nach **"DIVERA 24/7"**.  
   Click on **"Integrations"** and search for **"DIVERA 24/7"**.

3. Klicke auf **"Installieren"** und warte, bis die Installation abgeschlossen ist.  
   Click **"Install"** and wait for the installation to complete.

4. Nach der Installation wirst du aufgefordert, die Integration zu konfigurieren.  
   After installation, you will be prompted to configure the integration.

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=loony2392&repository=ha_hacs_divera_247&category=Integration)

### 2) Manuelle Installation 💻
1. Lade das Repository herunter:  
   Download the repository:

    ```bash
    git clone https://github.com/Loony2392/ha_hacs_divera_247.git
    ```

2. Kopiere den Ordner `custom_components/divera247` nach `config/custom_components/` deines Home Assistant Setups.

3. Starte **Home Assistant** neu.  
   Restart **Home Assistant**.

## Konfiguration ⚙️

1. Gehe zu **Einstellungen > Integrationen** in deinem Home Assistant.  
   Go to **Settings > Integrations** in your Home Assistant.

2. Klicke auf **"Integration hinzufügen"** und wähle **DIVERA 24/7**.  
   Click **"Add Integration"** and select **DIVERA 24/7**.

3. Gib deinen Zugangsschlüssel (Access Key) und optional die Server-Adresse ein (Standard: https://app.divera247.com). Hinweise zum Zugangsschlüssel: [Account-Einstellungen](https://app.divera247.com/account/einstellungen.html).

4. Wähle ggf. die Einheit(en) (Cluster), die du aktivieren möchtest.

5. Speichere die Konfiguration und starte Home Assistant neu, wenn du dazu aufgefordert wirst.  
   Save the configuration and restart Home Assistant when prompted.

## Optionen ⚙️

Nach der ersten Konfiguration kannst du folgende Optionen anpassen:

- ⏱️ Update-Intervall: 10–300 Sekunden.
- 🚗 Fahrzeug-Namensquelle: Auto, Kurzname, Name oder Vollständiger Name.
- 🔁 Reconfigure: Cluster-Auswahl und Fahrzeug-Namensquelle nachträglich ändern.

## Verwendung 🛠️

Weitere Informationen findest du in der Dokumentation.  
For more information, see the documentation.

### Verfügbare Entitäten 🔌

Die Integration erstellt mehrere Entitäten, die du in deinen Home Assistant Dashboards verwenden kannst:  
The integration creates several entities that you can use in your Home Assistant dashboards:

- Sensoren: letzter Alarm, Alarm-Adresse (mit Attributen inkl. Fahrzeuge), News, Helfer-Statusübersicht, Helfer-Zähler (aktiv/inaktiv/im Dienst), je Fahrzeug: Status, Standort (Diagnose), Rufname (OPTA), ISSI, Nummer.
- Binary Sensor: Aktiver Alarm.
- Select: Benutzer-Status (ändern per Auswahl oder Service).
- Kalender: Termine.
- Geräte-Tracker: Fahrzeuge auf der Karte.

Hinweis: Der Standort-Sensor ist als Diagnose entität standardmäßig deaktiviert (Map-Funktion via `device_tracker`).

### Services
- `divera247.trigger_probe_alarm`: Probealarm auslösen.
- `divera247.set_user_state` mit `state_name`: Benutzerstatus per Namen setzen.

### Automationen und Benachrichtigungen 🔔 / Automations and Notifications 🔔

Du kannst Automationen und Benachrichtigungen erstellen, die auf den Status von Alarmen, Fahrzeugen oder Benutzern reagieren. Beispiel:  
You can create automations and notifications that respond to the status of alarms, vehicles, or users. Example:

```yaml
automation:
  - alias: "Benachrichtigung bei Alarm"
    trigger:
      platform: state
      entity_id: binary_sensor.aktiver_alarm
      to: 'on'
    action:
      service: notify.notify
      message: "Es wurde ein aktiver Alarm ausgelöst!"
```
## Fehlerbehebung 🛠️
- 🔌 Verbindung: Base-URL prüfen, Access Key gültig?
- 🔑 Authentifizierung: Access Key aus den Debug-Einstellungen des Accounts nutzen.
- ♻️ UI-Übersetzungen: Nach Update hart neu laden (Strg+F5) bzw. HA neu starten.

## Beitragen 🤝
PRs sind willkommen – bitte vorher kurz in den Issues abstimmen, was sinnvoll ist.

## Hilfe und Unterstützung 🤗
Fragen/Bugs/Feature-Wünsche: GitHub Issues.

## Viel Spaß mit der DIVERA 24/7 Integration! 😎

---

## Zusätzliche Hinweise 💡
Unterstützte Versionen: Getestet mit Home Assistant 2025.2+.
