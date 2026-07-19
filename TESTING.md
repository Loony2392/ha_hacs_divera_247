# Security Testing Guide

This document describes the security tests and validation procedures for the Divera 24/7 integration.

## Manual Security Tests

### 1. URL Validation Tests

Test the HTTPS enforcement and URL validation:

```python
# Test cases for _validate_base_url()

# ✅ Valid HTTPS URL
_validate_base_url("https://app.divera247.com")

# ✅ Valid HTTP localhost (development)
_validate_base_url("http://localhost:8080")

# ❌ HTTP URL (should fail)
_validate_base_url("http://app.divera247.com")  # Raises Invalid

# ❌ Invalid format (should fail)
_validate_base_url("not a url")  # Raises Invalid

# ❌ Empty string (should fail)
_validate_base_url("")  # Raises Invalid

# ✅ Auto-adds https scheme
_validate_base_url("app.divera247.com")  # Returns https://app.divera247.com
```

### 2. Access Key Validation Tests

Test the access key length and format validation:

```python
# ✅ Valid key (20 chars)
key = "a" * 20
# Validation passes

# ❌ Too short (< 10 chars)
key = "short123"  # Should raise error

# ❌ Too long (> 1000 chars)
key = "x" * 1001  # Should raise error

# ❌ Empty key
key = ""  # Should raise error
```

### 3. XSS Prevention Tests

Test the HTML escaping for user data:

```python
from homeassistant.components.divera247.sensor import _safe_string

# ✅ XSS attempt blocked
value = "<script>alert('xss')</script>"
result = _safe_string(value)
# Result: "&lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;"

# ✅ HTML entities escaped
value = 'John "Doe" & Co.'
result = _safe_string(value)
# Result: "John &quot;Doe&quot; &amp; Co."

# ✅ String truncated to 500 chars
value = "x" * 1000
result = _safe_string(value)
# Result: "xxx...xxx" (max 500 chars)

# ✅ Special characters handled
value = "<>&\"'"
result = _safe_string(value)
# Result: "&lt;&gt;&amp;&quot;&#x27;"
```

### 4. API Call Timeout Tests

Test timeout configuration:

```python
# Verify timeout is applied
from divera247 import DEFAULT_TIMEOUT
from aiohttp import ClientTimeout

assert DEFAULT_TIMEOUT.total == 30
assert DEFAULT_TIMEOUT.connect == 10
assert DEFAULT_TIMEOUT.sock_read == 20
```

## Automated Testing

### Running Tests

```bash
# Install test dependencies
pip install -r requirements-dev.txt

# Run all tests
pytest

# Run only security tests
pytest tests/test_security.py

# Run with coverage
pytest --cov=custom_components/divera247 tests/
```

## Dependency Vulnerability Scanning

### Using Safety

```bash
# Install safety
pip install safety

# Scan requirements
safety check -r requirements.txt

# Generate report
safety check -r requirements.txt --json > security-report.json
```

### Using Pip-Audit

```bash
# Install pip-audit
pip install pip-audit

# Scan environment
pip-audit

# Scan specific requirements file
pip-audit --requirements requirements.txt
```

## OWASP Top 10 Mapping

| OWASP Issue                                   | Mitigation                                | Status |
| --------------------------------------------- | ----------------------------------------- | ------ |
| A01:2021 – Injection                          | Input validation, parameterized queries   | ✅     |
| A03:2021 – Injection                          | HTTPS enforcement, URL validation         | ✅     |
| A07:2021 – Cross-Site Scripting (XSS)         | HTML escaping, output encoding            | ✅     |
| A08:2021 – Software and Data Integrity        | Dependency pinning, checksum verification | ✅     |
| A10:2021 – Server-Side Request Forgery (SSRF) | URL whitelist, hostname validation        | ✅     |

## Security Checklist

Before each release, verify:

-   [ ] All input validation tests pass
-   [ ] XSS prevention tests pass
-   [ ] No security warnings in dependency scan
-   [ ] API timeout configuration is correct
-   [ ] Error messages don't expose sensitive data
-   [ ] HTTPS enforcement is enabled
-   [ ] Access keys are not logged
-   [ ] README includes security guidance
-   [ ] SECURITY.md is up to date

## Continuous Integration

Security checks are automated in CI/CD:

```yaml
# .github/workflows/security.yml
- name: Security Scan
  run: |
      safety check -r requirements.txt
      pip-audit

- name: SAST with Bandit
  run: |
      bandit -r custom_components/divera247
```

## Known Issues & Mitigations

### Dependency Vulnerabilities

If GitHub reports vulnerabilities in dependencies:

1. Check if the vulnerability affects the integration
2. Update the dependency if available
3. Document the issue in SECURITY.md
4. Create a workaround if needed

### Code Review

Every PR should include:

-   [ ] Input validation review
-   [ ] Output encoding review
-   [ ] Error handling review
-   [ ] No hardcoded secrets
-   [ ] No command injection risks

## Testing Commands

```bash
# Run full security test suite
pytest tests/test_security.py -v

# Run specific test
pytest tests/test_security.py::test_xss_prevention -v

# Run with detailed output
pytest tests/test_security.py -vv --tb=short
```

## References

-   [OWASP Top 10 - 2021](https://owasp.org/Top10/)
-   [Home Assistant Security Best Practices](https://developers.home-assistant.io/docs/development_testing/)
-   [CWE - Common Weakness Enumeration](https://cwe.mitre.org/)

---

**Last Updated**: January 2026
