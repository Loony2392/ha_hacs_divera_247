#!/usr/bin/env python3
"""Integration test script for Divera 24/7 custom component."""

import ast
import json
import sys
from pathlib import Path


def print_header(text):
    """Print a formatted header."""
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}\n")


def print_success(text):
    """Print success message."""
    print(f"✓ {text}")


def print_error(text):
    """Print error message."""
    print(f"✗ {text}")


def print_info(text):
    """Print info message."""
    print(f"  {text}")


def test_python_syntax():
    """Test Python syntax of all component files."""
    print_header("1. PYTHON SYNTAX CHECK")

    component_dir = Path("custom_components/divera247")
    python_files = list(component_dir.glob("*.py"))

    errors = []
    for py_file in python_files:
        try:
            with open(py_file, "r", encoding="utf-8") as f:
                ast.parse(f.read(), filename=str(py_file))
            print_success(f"{py_file.name}")
        except SyntaxError as e:
            errors.append(f"{py_file.name}: {e}")
            print_error(f"{py_file.name}: Line {e.lineno} - {e.msg}")

    if errors:
        return False

    print_info(f"Alle {len(python_files)} Python-Dateien sind syntaktisch korrekt")
    return True


def test_imports():
    """Test if all imports are defined correctly."""
    print_header("2. IMPORT STRUCTURE CHECK")

    component_dir = Path("custom_components/divera247")

    # Check key files exist
    required_files = [
        "__init__.py",
        "const.py",
        "coordinator.py",
        "divera247.py",
        "entity.py",
        "data.py",
        "utils.py",
    ]

    for file in required_files:
        file_path = component_dir / file
        if file_path.exists():
            print_success(f"{file} exists")
        else:
            print_error(f"{file} missing")
            return False

    return True


def test_platforms():
    """Test platform implementations."""
    print_header("3. PLATFORM IMPLEMENTATIONS")

    component_dir = Path("custom_components/divera247")
    platforms = ["select", "sensor", "calendar", "binary_sensor", "button"]

    for platform in platforms:
        file_path = component_dir / f"{platform}.py"
        if file_path.exists():
            # Check for async_setup_entry
            content = file_path.read_text(encoding="utf-8")
            if "async def async_setup_entry" in content:
                print_success(f"{platform}.py - async_setup_entry found")
            else:
                print_error(f"{platform}.py - async_setup_entry missing")
                return False
        else:
            print_error(f"{platform}.py missing")
            return False

    return True


def test_manifest():
    """Test manifest.json validity."""
    print_header("4. MANIFEST VALIDATION")

    manifest_path = Path("custom_components/divera247/manifest.json")

    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)

        print_success("manifest.json is valid JSON")

        # Check required fields
        required_fields = [
            "domain",
            "name",
            "documentation",
            "requirements",
            "codeowners",
            "version",
            "config_flow",
        ]

        for field in required_fields:
            if field in manifest:
                print_success(f"Field '{field}' present: {manifest[field]}")
            else:
                print_error(f"Field '{field}' missing")
                return False

        return True
    except Exception as e:
        print_error(f"manifest.json error: {e}")
        return False


def test_translations():
    """Test translation files."""
    print_header("5. TRANSLATION FILES")

    trans_dir = Path("custom_components/divera247/translations")

    if not trans_dir.exists():
        print_error("translations directory missing")
        return False

    translation_files = list(trans_dir.glob("*.json"))

    for trans_file in translation_files:
        try:
            with open(trans_file, "r", encoding="utf-8") as f:
                json.load(f)
            print_success(f"{trans_file.name} is valid")
        except Exception as e:
            print_error(f"{trans_file.name}: {e}")
            return False

    if translation_files:
        print_info(f"{len(translation_files)} translation files validated")
    else:
        print_error("No translation files found")
        return False

    return True


def test_code_structure():
    """Test code structure and key implementations."""
    print_header("6. CODE STRUCTURE VALIDATION")

    # Test DiveraClient class
    divera_file = Path("custom_components/divera247/divera247.py")
    content = divera_file.read_text(encoding="utf-8")

    if "class DiveraClient:" in content:
        print_success("DiveraClient class found")
    else:
        print_error("DiveraClient class missing")
        return False

    # Test key methods
    key_methods = {
        "pull_data": "async def pull_data",
        "get_user_state": "def get_user_state",
        "get_all_state_name": "def get_all_state_name",
        "set_user_state_by_name": "async def set_user_state_by_name",
        "has_open_alarms": "def has_open_alarms",
        "trigger_probe_alarm": "async def trigger_probe_alarm",
    }

    for method_name, method_signature in key_methods.items():
        if method_signature in content:
            print_success(f"Method '{method_name}' implemented")
        else:
            print_error(f"Method '{method_name}' missing")
            return False

    return True


def test_exception_handling():
    """Test custom exceptions."""
    print_header("7. EXCEPTION HANDLING")

    divera_file = Path("custom_components/divera247/divera247.py")
    content = divera_file.read_text(encoding="utf-8")

    exceptions = ["DiveraError", "DiveraAuthError", "DiveraConnectionError"]

    for exception in exceptions:
        if f"class {exception}" in content:
            print_success(f"{exception} defined")
        else:
            print_error(f"{exception} missing")
            return False

    return True


def test_services():
    """Test services.yaml."""
    print_header("8. SERVICES CONFIGURATION")

    services_file = Path("custom_components/divera247/services.yaml")

    if services_file.exists():
        print_success("services.yaml exists")
        content = services_file.read_text(encoding="utf-8")
        if "trigger_probe_alarm:" in content:
            print_success("Service 'trigger_probe_alarm' configured")
            return True
        else:
            print_error("Service 'trigger_probe_alarm' not configured")
            return False
    else:
        print_error("services.yaml missing")
        return False


def run_all_tests():
    """Run all integration tests."""
    print("\n" + "=" * 60)
    print("  DIVERA 24/7 INTEGRATION TEST SUITE")
    print("=" * 60)

    tests = [
        ("Python Syntax", test_python_syntax),
        ("Import Structure", test_imports),
        ("Platform Implementations", test_platforms),
        ("Manifest Validation", test_manifest),
        ("Translation Files", test_translations),
        ("Code Structure", test_code_structure),
        ("Exception Handling", test_exception_handling),
        ("Services Configuration", test_services),
    ]

    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print_error(f"Test '{name}' failed with exception: {e}")
            results.append((name, False))

    # Print summary
    print_header("TEST SUMMARY")

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for name, result in results:
        if result:
            print_success(f"{name}")
        else:
            print_error(f"{name}")

    print(f"\n{'='*60}")
    if passed == total:
        print(f"  ✓ ALL TESTS PASSED ({passed}/{total})")
        print(f"{'='*60}\n")
        print("✓ Integration ist bereit fuer Deployment!")
        return 0
    else:
        print(f"  ✗ SOME TESTS FAILED ({passed}/{total})")
        print(f"{'='*60}\n")
        print(f"✗ {total - passed} Test(s) fehlgeschlagen")
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
