---
key: security-stride
summary: Microsoft STRIDE threat modeling with per-element matrix and 5-step process
---

## STRIDE Threat Modeling

Developed by Microsoft (Loren Kohnfelder & Praerit Garg, 1999). Categorizes threats by their nature.

| Threat | Opposing Property | Description | Mitigations |
|---|---|---|---|
| **S -- Spoofing** | Authentication | Pretending to be someone/something else | MFA, digital signatures, certificate validation |
| **T -- Tampering** | Integrity | Modifying data or code without authorization | Digital signatures, checksums, access controls, audit logs |
| **R -- Repudiation** | Non-repudiation | Denying having performed an action | Audit logging, digital signatures, timestamps, secure log storage |
| **I -- Information Disclosure** | Confidentiality | Exposing information to unauthorized entities | Encryption (at rest + in transit), access controls, data masking |
| **D -- Denial of Service** | Availability | Making the system unavailable | Rate limiting, resource quotas, autoscaling, CDN, input validation |
| **E -- Elevation of Privilege** | Authorization | Gaining higher access than authorized | Least privilege, RBAC, input validation, sandboxing |

### STRIDE-per-Element Matrix

| DFD Element | S | T | R | I | D | E |
|---|---|---|---|---|---|---|
| **External Entity** | X | | | | | |
| **Process** | X | X | X | X | X | X |
| **Data Store** | | X | ? | X | X | |
| **Data Flow** | | X | | X | X | |

### Threat Modeling Process
1. **Decompose:** Create Data Flow Diagram (DFD) with trust boundaries
2. **Enumerate:** Apply STRIDE per element to identify threats
3. **Rate:** Score each threat using DREAD or CVSS
4. **Mitigate:** Define countermeasures for high-priority threats
5. **Validate:** Verify mitigations are implemented
