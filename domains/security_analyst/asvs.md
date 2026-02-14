---
key: security-asvs
summary: OWASP ASVS three-level verification framework with 14 verification categories
---

## OWASP ASVS (Application Security Verification Standard)

Three-level verification framework for assessing application security.

| Level | Target | Scope | Method |
|---|---|---|---|
| **L1 -- Opportunistic** | All applications (minimum baseline) | Automated + light manual | Penetration testing, automated scanning |
| **L2 -- Standard** | Applications handling sensitive data | Most security controls verified | Code review + testing |
| **L3 -- Advanced** | Critical applications (healthcare, financial, military) | Deep verification of all controls | Architecture analysis + full code review |

### Verification Categories

| ID | Category | Key Checks |
|---|---|---|
| V1 | Architecture, Design, Threat Modeling | Security architecture documented, threat model exists |
| V2 | Authentication | Password policy, MFA, credential storage, session binding |
| V3 | Session Management | Session generation, timeout, invalidation, cookie flags |
| V4 | Access Control | Least privilege, deny by default, RBAC, ABAC |
| V5 | Validation, Sanitization, Encoding | Input validation, output encoding, parameterized queries |
| V6 | Stored Cryptography | Algorithm strength, key management, random generation |
| V7 | Error Handling and Logging | Generic errors to users, security event logging, no sensitive data in logs |
| V8 | Data Protection | Data classification, PII handling, data-at-rest encryption |
| V9 | Communication | TLS everywhere, certificate validation, HSTS |
| V10 | Malicious Code | No backdoors, no time bombs, integrity verification |
| V11 | Business Logic | Workflow integrity, rate limiting, anti-automation |
| V12 | Files and Resources | File upload validation, file storage security |
| V13 | API and Web Service | API authentication, input validation, rate limiting |
| V14 | Configuration | Security headers, dependency management, build integrity |
