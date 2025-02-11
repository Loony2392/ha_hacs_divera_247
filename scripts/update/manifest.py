#!/usr/bin/env python3
import argparse
import json
import os


def update_manifest(version, manifest_path):
    if not os.path.exists(manifest_path):
        print(f"Manifest file not found: {manifest_path}")
        return 1

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    manifest["version"] = version

    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")

    print(f"Manifest updated to version {version}")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Update manifest version")
    parser.add_argument("--version", required=True, help="New version number")
    args = parser.parse_args()

    manifest_path = os.path.join(
        os.getcwd(), "custom_components", "divera247", "manifest.json"
    )
    exit_code = update_manifest(args.version, manifest_path)
    exit(exit_code)


if __name__ == "__main__":
    main()
