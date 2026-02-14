---
key: security-sans-cwe-top25
summary: SANS/CWE Top 25 comparison with OWASP and blind spots for comprehensive coverage
---

## SANS/CWE Top 25

### Relationship to OWASP Top 10

| Aspect | OWASP Top 10 | SANS/CWE Top 25 |
|---|---|---|
| Scope | Web applications only | All software |
| Granularity | Broad categories | Specific individual weaknesses |
| Size | 10 categories | 25 specific weaknesses |
| Update Frequency | Every 3-4 years | Annually |
| Methodology | Expert survey + data | Frequency x CVSS from NVD data |

### Blind Spots (in SANS Top 25 but NOT in OWASP Top 10)

| CWE | Name | Relevance |
|---|---|---|
| CWE-787 | Out-of-bounds Write | Native modules, WebAssembly |
| CWE-416 | Use After Free | Memory corruption in native code |
| CWE-190 | Integer Overflow | Buffer size calculations, financial math |
| CWE-362 | Race Condition (TOCTOU) | Multi-threaded web servers, async operations |
| CWE-276 | Incorrect Default Permissions | Cloud/container misconfiguration |
