---
key: security-headers
summary: 6 essential security headers with recommended configurations and CSP directives
---

## Security Headers

### Essential Headers Configuration

| Header | Recommended Value | Purpose |
|---|---|---|
| **Content-Security-Policy** | `default-src 'self'; script-src 'self' 'nonce-{random}'; style-src 'self' 'nonce-{random}'; img-src 'self' data: https:; frame-ancestors 'none'; base-uri 'self'; form-action 'self'; object-src 'none'` | Prevents XSS, clickjacking, data injection |
| **Strict-Transport-Security** | `max-age=63072000; includeSubDomains; preload` | Forces HTTPS (2 year max-age) |
| **X-Frame-Options** | `DENY` | Prevents clickjacking (supplement with CSP frame-ancestors) |
| **X-Content-Type-Options** | `nosniff` | Prevents MIME-sniffing attacks |
| **Referrer-Policy** | `strict-origin-when-cross-origin` | Controls referrer information leakage |
| **Permissions-Policy** | `accelerometer=(), camera=(), geolocation=(), gyroscope=(), magnetometer=(), microphone=(), payment=(), usb=()` | Restricts browser feature access |

### CSP Key Directives

| Directive | Controls | Common Mistake |
|---|---|---|
| `default-src` | Fallback for all resource types | Setting to `*` (defeats the purpose) |
| `script-src` | JavaScript sources | Using `'unsafe-inline'` or `'unsafe-eval'` |
| `style-src` | CSS sources | Using `'unsafe-inline'` for convenience |
| `img-src` | Image sources | Forgetting `data:` for inline images |
| `connect-src` | XHR/Fetch/WebSocket targets | Missing API domains |
| `frame-ancestors` | Who can embed this page | Not setting it (clickjacking risk) |

**Verification:** Use securityheaders.com to score (target: A+).
