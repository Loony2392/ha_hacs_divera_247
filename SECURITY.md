# Security Policy

## Reporting Security Vulnerabilities

If you discover a security vulnerability in the Divera 24/7 Home Assistant Integration, please **do not** open a public issue. Instead, please report it confidentially to the maintainers.

### How to Report

1. **Email**: Send a detailed report to the repository maintainer via GitHub
2. **Include**:
    - Description of the vulnerability
    - Steps to reproduce (if applicable)
    - Potential impact
    - Suggested fix (optional)

We will acknowledge your report within 48 hours and work to resolve the issue promptly.

## Security Features

This integration implements the following security measures:

### 1. **Input Validation**

-   ✅ HTTPS-only URLs enforced (except localhost for development)
-   ✅ Access key validation (10-1000 characters)
-   ✅ Scan interval range validation (10-300 seconds)
-   ✅ URL format validation to prevent injection attacks

### 2. **XSS Protection**

-   ✅ HTML escaping for all user-provided data (names, status, etc.)
-   ✅ String length limits (max 500 characters)
-   ✅ Special character encoding to prevent DOM-based XSS

### 3. **API Security**

-   ✅ Request timeouts (30 seconds total, 10s connect, 20s read)
-   ✅ Proper error handling without exposing sensitive information
-   ✅ Access keys redacted from logs and error messages
-   ✅ No credentials stored in plaintext

### 4. **Rate Limiting**

-   ✅ Configurable scan interval (minimum 10 seconds)
-   ✅ Prevents excessive API calls and DoS scenarios

### 5. **Dependency Management**

-   ✅ Regular dependency updates via Dependabot
-   ✅ Security advisories monitored
-   ✅ Pinned versions for reproducibility

## Known Limitations

### Inherited from Home Assistant Dependencies

The integration uses Home Assistant's underlying libraries (aiohttp, urllib3, etc.). Some security advisories may affect these dependencies:

-   **High Priority**: Keeping all dependencies up-to-date is recommended
-   **HTTPS Required**: Always use secure URLs to prevent MITM attacks
-   **Trusted Networks Only**: Only use in trusted networks; do not expose to untrusted internet

## Best Practices for Users

1. **Use HTTPS**: Always connect to DIVERA 24/7 via HTTPS
2. **Secure Access Key**:
    - Never share your access key
    - Use strong authentication for Home Assistant
    - Regularly rotate access keys if exposed
3. **Network Security**: Use a firewall and VPN if accessing remotely
4. **Keep Updated**: Regularly update Home Assistant and this integration
5. **Minimal Permissions**: Grant only necessary permissions to the integration

## Security Roadmap

-   [ ] Add rate limiting configuration
-   [ ] Implement request signing for additional validation
-   [ ] Add audit logging for sensitive operations
-   [ ] Regular security audits
-   [ ] Penetration testing

## Version Security Support

| Version    | Status      | Support Until |
| ---------- | ----------- | ------------- |
| 2025.11.5  | ✅ Stable   | Latest        |
| < 2025.9.0 | ⚠️ Outdated | 2025-03-31    |

## Changelog - Security Fixes

### Version 2025.11.5+

-   ✅ Added HTTPS URL validation
-   ✅ Added access key length validation
-   ✅ Added HTML escaping for user data (XSS prevention)
-   ✅ Added request timeouts for API calls
-   ✅ Improved error handling for sensitive data

## Contact & Support

-   **Issues**: [GitHub Issues](https://github.com/Loony2392/ha_hacs_divera_247/issues)
-   **Security**: Please report privately to the maintainer
-   **Discussions**: [GitHub Discussions](https://github.com/Loony2392/ha_hacs_divera_247/discussions)

---

**Last Updated**: January 2026
