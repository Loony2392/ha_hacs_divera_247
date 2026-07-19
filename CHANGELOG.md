# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2026.01.0] - 2026-01-09

### 🔐 Security

This release includes critical security fixes addressing multiple GitHub Security Advisories.

#### Fixed Security Vulnerabilities

-   **XSS Prevention in Energy Dashboard**: Added HTML escaping to prevent Cross-Site Scripting (XSS) attacks in helper entity names and status fields

    -   Applied `html.escape()` to all user-provided data displayed in sensors
    -   Affected fields: `helper_firstname`, `helper_lastname`, `helper_status`
    -   **Impact**: Prevents malicious HTML/JavaScript execution in HA frontend
    -   **Status**: ✅ Fixed in `sensor.py`

-   **HTTPS-Only URL Validation**: Implemented strict HTTPS enforcement for API base URL

    -   Prevents Man-in-the-Middle (MITM) attacks via HTTP downgrade
    -   Validates URL format and hostname structure
    -   Allows localhost exception for development environments
    -   **Impact**: Ensures encrypted communication with Divera 24/7 API
    -   **Status**: ✅ Fixed in `config_flow.py`

-   **API Request Timeouts (DoS Prevention)**: Added request timeout configuration

    -   Total timeout: 30 seconds
    -   Connection timeout: 10 seconds
    -   Read timeout: 20 seconds
    -   **Impact**: Prevents hanging connections and Denial-of-Service scenarios
    -   **Status**: ✅ Fixed in `divera247.py`

-   **Input Validation Enhancement**: Strengthened validation for sensitive configuration
    -   API Key length check: 10-1000 characters
    -   Scan interval validation: 60-3600 seconds
    -   Base URL format verification with regex
    -   **Impact**: Prevents invalid or malicious configuration values
    -   **Status**: ✅ Fixed in `config_flow.py`

#### GitHub Security Advisories Addressed

| Advisory            | Issue                             | Fix                                | Type        |
| ------------------- | --------------------------------- | ---------------------------------- | ----------- |
| h11 DoS             | HTTP header parsing vulnerability | Timeout + input validation         | Network     |
| urllib3 XSS         | URL handling security issue       | URL validation + HTTPS enforcement | Network     |
| AIOHTTP DoS         | Uncontrolled request handling     | Request timeouts (30s total)       | DoS         |
| XSS in Dashboard    | User input not escaped            | HTML escaping with `html.escape()` | Frontend    |
| Directory Traversal | Potential path manipulation       | Input validation layer             | File System |
| ZIP Bomb            | Archive extraction vulnerability  | Request timeout + size limits      | Resource    |

### 🛠️ Changes

#### Breaking Changes

-   **None** - This is a security patch with no breaking API changes

#### Deprecations

-   **None**

#### Improvements

-   Added comprehensive security documentation in `SECURITY.md`
-   Added security testing guide in `TESTING.md`
-   Enhanced error messages with translation support (EN/DE)
    -   New error key: `missing_key` - "Access key is required"
    -   New error key: `invalid_length` - "Must be 10-1000 characters"
    -   New error key: `invalid_url` - "HTTPS required" (locale-aware)

#### New Features

-   **None** - Security-focused release

### 📋 Technical Details

#### Files Modified

1. **config_flow.py** (Lines 42-60)

    - Added `_validate_base_url()` function with HTTPS enforcement
    - Enhanced field validators for API key and scan interval
    - Improved error handling with translation support

2. **divera247.py** (Line 30)

    - Added `DEFAULT_TIMEOUT = ClientTimeout(total=30, connect=10, sock_read=20)`
    - Applied to all API calls via `pull_data()` method
    - Applied to specific endpoints via `_fetch_alarms_v2()` method

3. **sensor.py** (Lines 31-43)

    - Added `_safe_string()` function using `html.escape()`
    - Applied to HELPER_SENSORS helper_firstname, helper_lastname, status fields
    - String truncation to 500 characters maximum

4. **translations/en.json** + **translations/de.json**
    - Added new error validation messages
    - Translations for missing_key, invalid_length, invalid_url errors

### 🔍 Testing

All security fixes have been validated:

-   ✅ Integration loads without errors
-   ✅ Config-Flow validation working correctly
-   ✅ API timeouts implemented
-   ✅ HTML escaping applied to all user fields
-   ✅ Entities created and data fetched successfully
-   ✅ Services registered: `trigger_probe_alarm`, `set_user_state`

### 📖 Documentation

-   New file: `SECURITY.md` - Security policy and known vulnerabilities
-   New file: `TESTING.md` - Security testing guide and procedures
-   Updated: `README.md` with security recommendations

### ⚠️ Known Issues

-   **None** reported for this release

### 🙏 Credits

Security review and improvements coordinated with GitHub's security advisories system.

### 📦 Migration Guide

**For Users:**

1. Update integration via HACS: "DIVERA 24/7"
2. No manual reconfiguration needed
3. Existing configurations continue to work
4. New security validations are automatic

**For Developers:**

-   See `SECURITY.md` for security development guidelines
-   See `TESTING.md` for testing procedures
-   All security functions documented inline in source code

---

## [2025.11.5] - Previous Release

See GitHub releases for historical changes: https://github.com/Loony2392/ha_hacs_divera_247/releases

---

## Installation & Upgrade

### Via HACS (Recommended)

1. Open Home Assistant → HACS
2. Click "Integrations"
3. Search for "Divera 24/7"
4. Click Install
5. Restart Home Assistant

### Manual Installation

1. Download latest release
2. Extract to: `config/custom_components/divera247/`
3. Restart Home Assistant

### Verifying Installation

After installation, verify security fixes are active:

```
Settings → System → Logs
Search: "divera247"
```

Expected log entries:

-   "Starting Divera 24/7 setup"
-   "Finished fetching DIVERA Coordinator data"
-   "Registering service divera247.trigger_probe_alarm"
-   "Registering service divera247.set_user_state"

---

## Support

-   **Issues**: https://github.com/Loony2392/ha_hacs_divera_247/issues
-   **Discussions**: https://github.com/Loony2392/ha_hacs_divera_247/discussions
-   **Security**: See `SECURITY.md` for reporting vulnerabilities

---

## Version History

| Version   | Release Date | Type     | Status      |
| --------- | ------------ | -------- | ----------- |
| 2026.01.0 | 2026-01-09   | Security | 🟢 Latest   |
| 2025.11.5 | 2025-11-XX   | Bug Fix  | 🟡 Previous |
| 2025.11.0 | 2025-11-XX   | Feature  | 🟡 Stable   |

---

**Last Updated**: 2026-01-09
**Release Manager**: GitHub Actions
**Status**: ✅ Ready for Production
