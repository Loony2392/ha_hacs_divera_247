🤖 Automationen
===============

Nutze Automationen, um auf Ereignisse der Divera 24/7 Integration zu reagieren:

**Beispiel-Automation:**

.. code-block:: yaml

   automation:
     - alias: "Licht einschalten bei Divera Event"
       trigger:
         platform: event
         event_type: divera247_event
       action:
         service: light.turn_on
         target:
           entity_id: light.wohnzimmer

Weitere Beispiele und Best Practices findest du in diesem Kapitel.
