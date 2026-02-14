---
key: security-secure-code-review
summary: 8-area secure code review checklist covering auth, authz, input, crypto, sessions, errors, logging
---

## Secure Code Review Checklist

### Authentication Review

| Check | Severity |
|---|---|
| Passwords hashed with bcrypt/Argon2/scrypt/PBKDF2 (never MD5/SHA1/SHA256 alone) | Critical |
| Credentials only transmitted over TLS, never in URL params | Critical |
| Brute-force protection: rate limiting + temporary lockout + CAPTCHA | High |
| No default/hardcoded credentials in code or config | Critical |
| Session ID regenerated after successful authentication | High |
| MFA available for sensitive operations | High |

### Authorization Review

| Check | Severity |
|---|---|
| All endpoints have server-side authorization checks | Critical |
| Deny by default (access denied unless explicitly granted) | Critical |
| IDOR prevention: object references validated against current user's permissions | High |
| Horizontal privilege: User A cannot access User B's resources | Critical |
| Vertical privilege: regular user cannot access admin functionality | Critical |
| API endpoints enforce same auth rules as UI | Critical |

### Input Validation Review

| Check | Severity |
|---|---|
| All input validated server-side (never trust client-only) | Critical |
| Whitelist approach (accept known-good, not block known-bad) | High |
| Length limits enforced on all string inputs | Medium |
| File upload: type, size, and content validated; stored outside webroot | High |
| Parameterized queries for ALL database operations | Critical |

### Output Encoding Review

| Check | Severity |
|---|---|
| HTML context: user data HTML-entity encoded | Critical |
| JavaScript context: JS-specific encoding (JSON.stringify) | Critical |
| URL context: user data URL-encoded | High |
| Template engine auto-escape enabled and not bypassed | Critical |

### Cryptography Review

| Check | Severity |
|---|---|
| AES-256-GCM or ChaCha20-Poly1305 for symmetric encryption (never ECB, DES, RC4) | Critical |
| `secrets` module (Python) / `crypto.randomBytes` (Node) for random generation (never Math.random) | Critical |
| Keys not in source code; loaded from environment/vault | Critical |
| TLS 1.2+ only; strong cipher suites; certificate validation enabled | Critical |
| IVs/nonces never reused; generated randomly | High |

### Session Management Review

| Check | Severity |
|---|---|
| Cookie flags: `Secure`, `HttpOnly`, `SameSite=Lax` (or `Strict`) | High |
| Absolute timeout (8h) AND idle timeout (30min) | High |
| Full server-side invalidation on logout (not just cookie deletion) | High |
| Cryptographically random session IDs (128+ bits) | Critical |

### Error Handling Review

| Check | Severity |
|---|---|
| Generic error messages to users (no stack traces, SQL errors, internal paths) | High |
| No sensitive data in error responses (credentials, tokens, internal IPs) | High |
| Custom error pages for 404, 403, 500 (not default framework pages) | Medium |

### Logging Review

| Check | Severity |
|---|---|
| Security events logged (login success/failure, access denied, privilege changes) | High |
| No passwords, tokens, session IDs, or PII in logs | Critical |
| Sufficient context: timestamp, user ID, IP, action, resource, result | High |
| Log injection prevention (no newlines, ANSI escapes in log inputs) | Medium |
