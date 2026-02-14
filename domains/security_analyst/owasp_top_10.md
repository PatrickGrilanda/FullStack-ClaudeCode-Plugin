---
key: security-owasp-top-10
summary: OWASP 2021 categories with CWE mappings and critical code red flag patterns
---

## OWASP Top 10 (2021)

The authoritative awareness document for web application security risks.

| Category | CWE Coverage | Key Vulnerabilities |
|---|---|---|
| **A01: Broken Access Control** | CWE-200, CWE-201, CWE-352, CWE-639, CWE-862, CWE-863 | IDOR, missing function-level access control, CORS misconfig, path traversal |
| **A02: Cryptographic Failures** | CWE-259, CWE-327, CWE-331, CWE-798 | Cleartext transmission, weak algorithms (MD5/SHA1), hardcoded credentials |
| **A03: Injection** | CWE-20, CWE-77, CWE-78, CWE-79, CWE-89, CWE-94 | SQL injection, XSS, OS command injection, template injection |
| **A04: Insecure Design** | CWE-209, CWE-256, CWE-501, CWE-522 | Missing threat modeling, insecure trust boundaries, no rate limiting by design |
| **A05: Security Misconfiguration** | CWE-16, CWE-611, CWE-1004 | Default credentials, unnecessary features enabled, missing security headers, XML external entities |
| **A06: Vulnerable Components** | CWE-1035, CWE-1104 | Outdated dependencies with known CVEs, unpatched frameworks |
| **A07: Auth Failures** | CWE-287, CWE-384, CWE-613, CWE-640 | Brute force allowed, weak passwords, improper session management |
| **A08: Data Integrity Failures** | CWE-345, CWE-502, CWE-829 | Insecure deserialization, missing code/data integrity checks, unsigned updates |
| **A09: Logging Failures** | CWE-117, CWE-223, CWE-532, CWE-778 | Missing security event logging, logging sensitive data, no alerting |
| **A10: SSRF** | CWE-918 | Server-side URL fetching without validation, internal network access |

### Critical Code Patterns to Flag

```
CRITICAL RED FLAGS (always stop review):
- String concatenation in SQL queries (SQLi)
- eval(), exec(), Function() with user input (code injection)
- pickle.loads(), yaml.load(), unserialize() with untrusted data (deserialization)
- os.system(), subprocess(shell=True) with user input (OS command injection)
- innerHTML, dangerouslySetInnerHTML, v-html with user data (XSS)
- Hardcoded passwords, API keys, or secrets in source code
- MD5/SHA1 for password hashing
- HTTP (not HTTPS) for sensitive data
- Missing authentication on admin/sensitive endpoints
- Missing authorization checks on data access

HIGH-PRIORITY RED FLAGS:
- Missing CSRF tokens on state-changing forms
- Missing rate limiting on authentication endpoints
- Session ID not regenerated after login
- Cookies without Secure/HttpOnly/SameSite flags
- Missing input validation on file uploads
- Error messages revealing internal details
- Logging passwords, tokens, or PII
- Math.random()/random.random() for security tokens
- Disabled SSL certificate verification
```
