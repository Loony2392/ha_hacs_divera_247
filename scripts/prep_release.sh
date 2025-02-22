#!/bin/bash

VERSION=$1

# Change directory to custom_components/divera247
cd custom_components/divera247

# Update the version in the manifest.json file
sed -i "s/\"version\": \"[0-9]\+\.[0-9]\+\.[0-9]\+\"/\"version\": \"${VERSION}\"/g" manifest.json

# Go back to the root directory of the repository
cd ../..

# Create a ZIP file that contains only the divera247 folder
zip -r divera247.zip custom_components/divera247