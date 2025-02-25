#!/bin/bash

# Überprüfe, ob eine Versionsnummer als Argument übergeben wurde
if [ -z "$1" ]; then
  echo "Fehler: Keine Versionsnummer angegeben."
  exit 1
fi

VERSION=$1

# Ändere das Verzeichnis zu custom_components/divera247
cd custom_components/divera247

# Aktualisiere die Versionsnummer in der manifest.json Datei
sed -i "s/\"version\": \"[0-9]\+\.[0-9]\+\.[0-9]\+\"/\"version\": \"${VERSION}\"/g" manifest.json

# Gehe zurück zum Stammverzeichnis des Repositories
cd ../..

# Erstelle eine ZIP-Datei, die nur den divera247 Ordner enthält
zip -r divera247.zip custom_components/divera247