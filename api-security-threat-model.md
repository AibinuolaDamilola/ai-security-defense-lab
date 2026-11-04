# CartBot AI — API Security Threat Model

| Field | Your Finding |
|---|---|
| Vulnerability 1 | Broken Object Level Authorization (BOLA) caused by trusting a client-supplied customer ID without proper server-side authorization verification. |
| OWASP Classification (V1) | OWASP API1:2023 — Broken Object Level Authorization |
| Vulnerability 2 | Indirect prompt injection through instructions hidden in content processed by the AI model. |
| MITRE ATLAS Classification (V2) | MITRE ATLAS AML.T0051 — LLM Prompt Injection (Indirect) |
| Vulnerability 3 | Scripted/bulk data exfiltration through the AI system's legitimate access channel. |
| MITRE ATLAS Classification (V3) | MITRE ATLAS AML.T0054 — LLM Data Exfiltration |
| Attack Chain | The attack begins with weak object-level authorization, where the API trusts a customer ID supplied by the client. An attacker can then interact with the AI system through malicious content containing hidden instructions. Because the system does not adequately validate authorization and lacks effective rate limiting, automated requests can be used to harvest data at scale. |
| Business Impact | Customer information could be exposed, customer trust could be damaged, and the organization could face privacy or regulatory consequences. Disabled rate limiting can also allow excessive AI inference requests and increase operational costs. |
| Root Cause | The main root cause is insecure API configuration and missing server-side security controls. The investigation identified disabled JWT validation, a trusted client-supplied customer ID, and disabled rate limiting in the API configuration. |
| Remediation | Enforce server-side authentication and authorization, validate JWTs, do not trust client-supplied customer identifiers, validate and sanitize content reaching the model, and enable rate limiting to prevent automated abuse and excessive data access. |
