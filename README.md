# <img src="https://www.divera247.com/images/divera247.svg" alt="DIVERA Logo" width="200"> Integration für Home Assistant 🚨🔔

Die DIVERA 24/7 Integration für Home Assistant ermöglicht es dir, Daten und Ereignisse von der DIVERA 24/7-Plattform in dein Home Assistant System zu integrieren. Mit dieser Integration kannst du Informationen zu Alarmeinsätzen, Fahrzeugstatus, Benutzerstatus und vieles mehr abrufen.

The DIVERA 24/7 integration for Home Assistant allows you to integrate data and events from the DIVERA 24/7 platform into your Home Assistant system. With this integration, you can retrieve information about alarm incidents, vehicle status, user status, and much more.

[![GitHub Release](https://img.shields.io/github/v/release/loony2392/ha_hacs_divera_247?sort=semver&style=for-the-badge&color=green)](https://github.com/loony2392/ha_hacs_divera_247/releases/)
![GitHub Downloads (all assets, latest release)](https://img.shields.io/github/downloads/loony2392/ha_hacs_divera_247/latest/total?style=for-the-badge&label=Downloads%20latest%20Release)
[![Ko-Fi](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge)](https://ko-fi.com/loony_tech)

## Organisationseinheit Auswahl

Mit der neuen Funktion in der **DIVERA 24/7 Integration** können Benutzer nun die Organisationseinheit auswählen, die sie verwenden möchten. Die Auswahl erfolgt über ein Dropdown-Menü, das bei der Integration konfiguriert wird.

### Verfügbare Organisationseinheiten mit Fahrzeugbildern:

### Geplante Organisationseinheiten mit Fahrzeugbildern:
<img src="https://imgs.search.brave.com/JTKWNabfAU_GsdHJEDFwQaZOav4Pi2ik9AZxPATA-7A/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy8y/LzIyL1Rody5sb2dv/LnN2Zw" alt="THW Logo" width="50" height="50">

<img src="https://imgs.search.brave.com/i7OXzyBbw52wQ0InMr1Bt_iypcGLktxh39J6d79kJQ4/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/ZmV1ZXJ3ZWhyLW5l/dXNhZXNzLmRlL3dw/LWNvbnRlbnQvdGhl/bWVzL2ZmbjE4L2lt/Zy91ZWJlcnVucy9h/dWZnYWJlbi9GZXVl/cndlaHJfUkxCU19M/b2dvLnN2Zw" alt="Feuerwehr Logo" width="50" height="50">

<img src="https://imgs.search.brave.com/99MOXySJPhLWgLgJ_xzVWDzpxL44A__CMkM3jBxLxCc/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvZGUvZC9kMS9E/UkstUnVuZGxvZ28u/cG5n" alt="DRK Logo" width="50" height="50">

### So funktioniert es:

1. **Konfiguration:** Gehe zu den **Home Assistant**-Einstellungen und suche nach der DIVERA 24/7 Integration.
2. **Wählen Sie Ihre Organisation:** In der Konfiguration kannst du nun die Organisationseinheit aus einem Dropdown-Menü auswählen, z. B. **THW** oder **Feuerwehr**.
3. **Bilder und Daten:** Nachdem du die Organisation ausgewählt hast, wird die Integration mit den entsprechenden Bildern und Informationen zu deiner Auswahl aktualisiert.

## Features ⚡

- 🚨 Abruf von Alarm- und Notrufereignissen.  
  Retrieve alarm and emergency events.

- 🚗 Anzeige von Fahrzeugstatusinformationen.  
  Display vehicle status information.

- 🧑‍🤝‍🧑 Integration von Benutzerdaten, einschließlich Status und Aktivitäten.  
  Integration of user data, including status and activities.

- 📅 Anzeige von Kalenderereignissen und News.  
  Display calendar events and news.

- 🛠️ Möglichkeit zur Konfiguration mehrerer Einheiten (Cluster) innerhalb eines Accounts.  
  Possibility to configure multiple units (clusters) within one account.

## Voraussetzungen 📋

- 💻 **Home Assistant Version 2023.2** oder neuer.  
  **Home Assistant version 2023.2** or newer.

- 📝 Ein aktiver **DIVERA 24/7 Account**.  
  An active **DIVERA 24/7 account**.

- 🔑 Dein DIVERA 24/7 Zugangsschlüssel (zu finden in deinen Benutzer-Einstellungen unter Debug).  
  Your DIVERA 24/7 access key (found in your user settings under Debug).

## Installation 🔧

### 1. Installation über HACS (Home Assistant Community Store) 📦
1. Öffne **Home Assistant** und gehe zu **HACS**.  
   Open **Home Assistant** and go to **HACS**.

2. Klicke auf **"Integrationen"** und suche nach **"DIVERA 24/7"**.  
   Click on **"Integrations"** and search for **"DIVERA 24/7"**.

3. Klicke auf **"Installieren"** und warte, bis die Installation abgeschlossen ist.  
   Click **"Install"** and wait for the installation to complete.

4. Nach der Installation wirst du aufgefordert, die Integration zu konfigurieren.  
   After installation, you will be prompted to configure the integration.

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=loony2392&repository=ha_hacs_divera_247&category=Integration)

### 2. Manuelle Installation 💻
1. Lade das Repository herunter:  
   Download the repository:

    ```bash
    git clone https://github.com/Loony2392/ha_hacs_divera_247.git
    ```

2. Kopiere den Ordner `custom_components/divera_247` in das Verzeichnis `config/custom_components/` deines Home Assistant Setups.  
   Copy the folder `custom_components/divera_247` into the `config/custom_components/` directory of your Home Assistant setup.

3. Starte **Home Assistant** neu.  
   Restart **Home Assistant**.

## Konfiguration ⚙️

1. Gehe zu **Einstellungen > Integrationen** in deinem Home Assistant.  
   Go to **Settings > Integrations** in your Home Assistant.

2. Klicke auf **"Integration hinzufügen"** und wähle **DIVERA 24/7**.  
   Click **"Add Integration"** and select **DIVERA 24/7**.

3. Gib deinen Zugangsschlüssel (Access Key) und die Server-Adresse ein. Weitere Informationen zum Finden des Zugangsschlüssels findest du [hier](#).  
   Enter your access key (Access Key) and the server address. For more information on finding the access key, see [here](#).

4. (Optional) Wähle die Einheit (Cluster), die du überwachen möchtest. Standardmäßig wird die Stammeinheit geladen.  
   (Optional) Choose the unit (cluster) you want to monitor. The default unit is loaded.

5. Speichere die Konfiguration und starte Home Assistant neu, wenn du dazu aufgefordert wirst.  
   Save the configuration and restart Home Assistant when prompted.

## Optionen ⚙️

Nach der ersten Konfiguration kannst du die folgenden Optionen anpassen:

After the initial configuration, you can adjust the following options:

- ⏱️ **Update Intervall**: Bestimme das Intervall, in dem die Daten von DIVERA 24/7 aktualisiert werden. Das Intervall muss zwischen **10 und 300 Sekunden** liegen.  
  **Update Interval**: Set the interval at which data from DIVERA 24/7 is updated. The interval must be between **10 and 300 seconds**.

## Verwendung 🛠️

### Verfügbare Entitäten 🔌

Die Integration erstellt mehrere Entitäten, die du in deinen Home Assistant Dashboards verwenden kannst:

The integration creates several entities that you can use in your Home Assistant dashboards:

- 🕰️ **Sensoren**:
  - `sensor.letzter_alarm`: Zeigt den letzten Alarm an.  
    `sensor.last_alarm`: Shows the last alarm.

  - `sensor.letzte_news`: Zeigt die letzten News von DIVERA 24/7 an.  
    `sensor.latest_news`: Shows the latest news from DIVERA 24/7.

  - `sensor.fahrzeug_status_{vehicle_name}`: Zeigt den Status eines Fahrzeugs an.  
    `sensor.vehicle_status_{vehicle_name}`: Shows the status of a vehicle.

- 🚨 **Binary Sensoren**:
  - `binary_sensor.aktiver_alarm`: Zeigt an, ob ein Alarm aktiv ist.  
    `binary_sensor.active_alarm`: Shows if an alarm is active.

- 🧑‍🤝‍🧑 **Select**:
  - `select.benutzer_status`: Zeigt den aktuellen Benutzerstatus an.  
    `select.user_status`: Displays the current user status.

- 📅 **Kalender**:
  - `calendar.termine`: Zeigt alle kommenden Termine an.  
    `calendar.events`: Shows all upcoming events.

### Automationen und Benachrichtigungen 🔔

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
Fehlerbehebung 🛠️  
🔌 Verbindungsfehler: Überprüfe, ob die angegebene Server-Adresse korrekt ist und dass dein Zugangsschlüssel gültig ist.  
Connection error: Check if the provided server address is correct and if your access key is valid.

🔑 Authentifizierungsfehler: Stelle sicher, dass du den richtigen Zugangsschlüssel verwendest. Du findest diesen in den Debug-Einstellungen deines DIVERA 24/7 Accounts.  
Authentication error: Make sure you're using the correct access key. You can find it in the Debug settings of your DIVERA 24/7 account.

⚠️ Allgemeine Fehler: Wenn der Fehler weiterhin besteht, starte Home Assistant neu oder wende dich an die Community auf Home Assistant Community Forum.  
General errors: If the error persists, restart Home Assistant or contact the community at the Home Assistant Community Forum.

## Beitragen 🤝  
Wenn du Verbesserungen oder Fehlerbehebungen für diese Integration einreichen möchtest, öffne einen Pull Request (PR). Sieh dir bitte unsere Contributing Guidelines an, bevor du mit dem Beitrag beginnst.  
If you'd like to contribute improvements or bug fixes for this integration, open a Pull Request (PR). Please review our Contributing Guidelines before starting your contribution.

## Hilfe und Unterstützung 🤗  
Besuche das Home Assistant Forum für allgemeine Unterstützung und Diskussionen.  
Visit the Home Assistant Forum for general support and discussions.

Melde Fehler oder schlage neue Funktionen auf GitHub Issues vor.  
Report bugs or suggest new features on GitHub Issues.

## Viel Spaß mit der DIVERA 24/7 Integration! 😎  
Enjoy the DIVERA 24/7 integration! 😎

---

## Zusätzliche Hinweise 💡  
✅ Unterstützte Home Assistant Versionen: Die Integration ist mit allen Versionen von Home Assistant kompatibel, die Custom Components unterstützen.  
Supported Home Assistant Versions: The integration is compatible with all versions of Home Assistant that support custom components.
