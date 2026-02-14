---
key: security-cwe
summary: 10 most critical CWEs for web applications with OWASP mapping and detection patterns
---

## CWE (Common Weakness Enumeration)

MITRE's taxonomy of software weaknesses. Each CWE is a specific type of vulnerability.

### Most Critical CWEs for Web Applications

| CWE | Name | OWASP Mapping | Detection Pattern |
|---|---|---|---|
| **CWE-79** | Cross-site Scripting (XSS) | A03: Injection | innerHTML, dangerouslySetInnerHTML, template bypass, unescaped output |
| **CWE-89** | SQL Injection | A03: Injection | String concatenation in queries, non-parameterized queries |
| **CWE-287** | Improper Authentication | A07: Auth Failures | Missing auth checks, bypassable auth flows |
| **CWE-352** | CSRF | A01: Broken Access Control | Missing CSRF tokens on state-changing operations |
| **CWE-502** | Insecure Deserialization | A08: Data Integrity | pickle.loads, yaml.load, JSON.parse of untrusted data without schema |
| **CWE-862** | Missing Authorization | A01: Broken Access Control | Endpoints without permission checks |
| **CWE-863** | Incorrect Authorization | A01: Broken Access Control | Flawed RBAC logic, IDOR |
| **CWE-918** | SSRF | A10: SSRF | URL fetching from user input without validation |
| **CWE-22** | Path Traversal | A01: Broken Access Control | `../` in file paths, unsanitized file access |
| **CWE-798** | Hardcoded Credentials | A02: Cryptographic Failures | Strings matching password/secret/key patterns in source |
