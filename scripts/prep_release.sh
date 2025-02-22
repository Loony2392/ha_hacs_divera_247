#!/bin/bash

VERSION=$1

# Ändere das Verzeichnis zu custom_components/divera247
cd custom_components/divera247

# Aktualisiere die Version in der manifest.json Datei
sed -i "s/\"version\": \"[0-9]\+\.[0-9]\+\.[0-9]\+\"/\"version\": \"${VERSION}\"/g" manifest.json

# Gehe zurück zum Root-Verzeichnis des Repositories
cd ../..

# Erstelle eine ZIP-Datei, die nur den Ordner divera247 enthält
zip -r divera247.zip custom_components/divera247