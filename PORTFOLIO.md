# # AI Defense Lab — Portfolio

**Student:** Ajayi Glory
**GitHub:** https://github.com/Ajayi-Glory
**Hugging Face Space:** https://ai-security-defense-lab-glovis.streamlit.app/
**Fellowship:** HerNetIQ AI Security Fellowship — Cohort 1, 2026
**Completed:** August 2026

-

## Level 1 — MedVitals AI · Cloud Infrastructure Security

### 1. Scenario / Investigation

MedVitals AI was a simulated healthcare AI environment requiring a cloud infrastructure security assessment. My task was to investigate potential weaknesses in cloud permissions and credential management, review security logs, and identify activity that could put sensitive resources at risk.

### 2. Problem / Vulnerability

The investigation focused on excessive permissions, potentially exposed secrets, and suspicious activity within the cloud environment. These weaknesses could allow an attacker to access sensitive resources, escalate privileges, or compromise credentials, increasing the risk of unauthorized access to healthcare-related information.

### 3. Evidence

* **Level 1 commit:** https://github.com/Ajayi-Glory/hernetiq-fellowship-portfolio/commit/35559bff9d0b8c7e08c81bcd9605a304cd117d2e
* **Incident timeline report:** https://github.com/Ajayi-Glory/hernetiq-fellowship-portfolio/blob/main/Week%204/Incident%20timeline%20report%20level%201
* **Additional supporting artifact:** https://lnkd.in/p/gp4VArxe

### 4. Remediation

I reviewed the cloud security findings, examined the available logs to trace the activity, and applied least-privilege security controls to reduce unnecessary access. I also addressed the identified secrets-management concerns and documented the incident timeline and security findings.

### 5. Commit

[View the Level 1 GitHub commit diff](https://github.com/Ajayi-Glory/hernetiq-fellowship-portfolio/commit/35559bff9d0b8c7e08c81bcd9605a304cd117d2e)

### 6. Outcome

The remediation reduced unnecessary access and strengthened the protection of sensitive credentials. The incident timeline also documented the investigation and provided a record of the security findings. These controls matter in healthcare AI environments, where unauthorized access to infrastructure or credentials could put sensitive information and system integrity at risk.

### 7. Skills Demonstrated

Cloud Security · AWS IAM · CloudTrail Log Forensics · IAM Least Privilege · Secrets Management · Incident Response · Incident Timeline Reporting

### 8. Supporting Artifacts

* [Incident Timeline Report — Level 1](https://github.com/Ajayi-Glory/hernetiq-fellowship-portfolio/blob/main/Week%204/Incident%20timeline%20report%20level%201)
* [Additional Level 1 Artifact](https://lnkd.in/p/gp4VArxe)

### 9. LinkedIn Case Study

 https://lnkd.in/p/gudsRpsY

---

## Level 2 — DataForge ML · AI Model Security

### 1. Scenario / Investigation

DataForge ML was a simulated machine-learning environment in which I investigated the security of an AI model-loading pipeline. My objective was to determine whether the model-loading process could expose the application to malicious code and to identify ways to make the pipeline safer.

### 2. Problem / Vulnerability

The pipeline used Python pickle deserialization to load an AI model. Pickle files can execute code during deserialization, meaning a malicious model file could execute embedded commands when loaded. This could compromise the environment running the model and potentially expose sensitive resources.

### 3. Evidence

* **Level 2 commit:** https://github.com/Ajayi-Glory/ai-security-defense-lab/commit/b350cb7475d6ed23dcba3e9455fbe26225f3aa0d
* **Model security assessment:** https://github.com/Ajayi-Glory/hernetiq-fellowship-portfolio/blob/main/week-6/model%20security%20assement.md
* **Additional threat assessment:** https://github.com/Ajayi-Glory/ai-security-defense-lab/blob/main/level2_model_threat_assessment.md
* **LinkedIn supporting post:** https://www.linkedin.com/posts/ajayi-glory-8b3397420_ive-been-working-through-corpconnect-messenger-activity-7495461509217673216-Npqh

### 4. Remediation

I inspected the model-loading code and model repository, then used PickleScan to scan the vulnerable model and identify a suspicious subprocess payload. I hardened the pipeline by replacing the unsafe pickle-based loading path with Safetensors and adding a PickleScan verification step before model loading.

### 5. Commit

[View the Level 2 GitHub commit diff](https://github.com/Ajayi-Glory/ai-security-defense-lab/commit/b350cb7475d6ed23dcba3e9455fbe26225f3aa0d)

### 6. Outcome

The changes removed the unsafe pickle-based model-loading path, introduced a model-scanning security gate, and switched the model format to Safetensors. Together, these measures reduce the risk of malicious deserialization and improve the security of the model supply chain. This is important because a model file can be a security risk, not just a source of predictions.

### 7. Skills Demonstrated

AI Model Security · Model Supply Chain Security · Pickle Exploit Detection · Safetensors · PickleScan · Secure Model Loading · Automated Model Scanning · Threat Assessment

### 8. Supporting Artifacts

* [Model Security Assessment Report](https://github.com/Ajayi-Glory/hernetiq-fellowship-portfolio/blob/main/week-6/model%20security%20assement.md)
* [Level 2 Model Threat Assessment](https://github.com/Ajayi-Glory/ai-security-defense-lab/blob/main/level2_model_threat_assessment.md)
* [LinkedIn Supporting Post](https://www.linkedin.com/posts/ajayi-glory-8b3397420_ive-been-working-through-corpconnect-messenger-activity-7495461509217673216-Npqh)

### 9. LinkedIn Case Study

[View the combined AI Security Fellowship case study on LinkedIn] (https://lnkd.in/p/gudsRpsY)

---

## Level 3 — CartBot AI · Application & API Security

### 1. Scenario / Investigation

CartBot AI was a simulated e-commerce AI application that required an API security assessment. I examined its API configuration and tested the security controls to determine whether weaknesses in authentication, request handling, and prompt protection could be exploited.

### 2. Problem / Vulnerability

The investigation identified three security weaknesses: the API trusted a client-supplied `customer_id`, JWT validation was disabled, and rate limiting was disabled. The AI system prompt also required stronger protection against direct prompt injection. These weaknesses could increase the risk of unauthorized access, abuse of API resources, and attempts to manipulate the AI application's behavior.

### 3. Evidence

* **Level 3 commit:** https://github.com/Ajayi-Glory/ai-security-defense-lab/commit/af6ffd31e0a7090077b842761b8b816ddbh43ae81
* **API security findings report:** https://github.com/Ajayi-Glory/hernetiq-fellowship-portfolio/blob/main/week%20-8/Ai-application-security-report.md
* **LinkedIn supporting post:** https://www.linkedin.com/posts/ajayi-glory-8b3397420_level-3-of-my-ai-security-fellowship-completed-activity-7501742120064438272-ZThM

### 4. Remediation

I audited `api_config.py`, identified the weaknesses, and tested the API security controls. I implemented JWT validation, rate limiting, and protections against system-prompt injection. I then reran the tests and documented the findings in an API security report.

### 5. Commit

[View the Level 3 GitHub commit](https://github.com/Ajayi-Glory/ai-security-defense-lab/commit/af6ffd31e0a7090077b842761b8b816ddbh43ae81)

### 6. Outcome

The API was updated to validate JWTs rather than trust a customer ID supplied by the client. Rate limiting and system-prompt protections were also addressed. These controls help strengthen authentication, reduce opportunities for API abuse, and improve resilience against attempts to manipulate the AI application's behavior.

### 7. Skills Demonstrated

AI API Security · API Hardening · JWT Validation · Rate Limiting · Output Filtering · OWASP Top 10 for LLM Applications · Direct Prompt Injection Defense · Security Testing · Technical Reporting

### 8. Supporting Artifacts

* [AI Application Security Report — Level 3](https://github.com/Ajayi-Glory/hernetiq-fellowship-portfolio/blob/main/week%20-8/Ai-application-security-report.md)
* [Level 3 Commit](https://github.com/Ajayi-Glory/ai-security-defense-lab/commit/af6ffd31e0a7090077b842761b8b816ddbh43ae81)
* [LinkedIn Post — Level 3](https://www.linkedin.com/posts/ajayi-glory-8b3397420_level-3-of-my-ai-security-fellowship-completed-activity-7501742120064438272-ZThM)

### 9. LinkedIn Case Study

[View the combined AI Security Fellowship case study on LinkedIn] https://lnkd.in/p/gudsRpsY
---

## Portfolio Summary — Domains 1–3

Across the first three AI Defense Lab levels, I investigated security weaknesses across cloud infrastructure, AI model loading, and application APIs.

* **Cloud infrastructure:** Investigated excessive permissions, secrets-management concerns, and security logs.
* **AI model security:** Identified the risks of unsafe pickle deserialization and introduced safer model loading and scanning controls.
* **Application and API security:** Addressed weaknesses involving JWT validation, client-supplied identity, rate limiting, and system-prompt protection.

These investigations reinforced an important principle: AI security requires a layered approach. Protecting an AI application means securing the infrastructure it runs on, the models it loads, and the APIs through which users interact with it.

**Technical evidence:** [GitHub Profile](https://github.com/Ajayi-Glory) · [AI Defense Lab](https://github.com/Ajayi-Glory/ai-security-defense-lab) · [Live AI Security Defense Lab](https://ai-security-defense-lab-glovis.streamlit.app/)


## Level 4 — PayGuard · Data Security in AI

**Problem:**PayGuard AI handles sensitive financial data in a multi-tenant environment. The assessment focused on risks involving cross-tenant data leakage, weaknesses in RAG retrieval, and the possibility of poisoned or tampered fine-tuning data entering the training pipeline.

**Method:**Investigated the PayGuard RAG pipeline and fine-tuning configuration. Examined how tenant isolation was enforced, reviewed training-data integrity controls, and used security testing and static analysis to identify weaknesses. Worked on moving tenant enforcement to the database layer, validating training data against approved checksums, and improving the consistency of AI responses.

**Evidence:** https://github.com/Ajayi-Glory/ai-security-defense-lab/commit/e04949a18aac5027b5516fec7dc930a81672a500

**Outcome:**Implemented proposed security changes for database-level tenant isolation and fine-tuning data validation. The changes also included deterministic context anchoring and rate-limiting controls. Final test results must be verified before recording the remediation as fully successful.

**Skills:** STRIDE Threat Modeling · RAG Pipeline Security · Multi-Tenant Data Isolation · Indirect Prompt Injection Defence

**Others:**
- [https://github.com/Ajayi-Glory/hernetiq-fellowship-portfolio/blob/main/week-11-level%204-data-security-findings.md]
- [https://lnkd.in/p/gpqnBSx2]

---

## Level 5 — LegalBot Municipal · Agentic AI Security

**Problem:**LegalBot, a municipal AI legal assistant, had excessive authority to finalize code-violation case dismissals without mandatory human approval. It was also vulnerable to indirect prompt injection through untrusted citizen-submitted comments. This created a risk of unauthorized case decisions and misuse of the AI assistant's permissions.

**Method:**Reviewed the LegalBot implementation and identified security weaknesses involving excessive agent permissions, missing human-approval controls, and insufficient protection against malicious citizen input. Worked on restricting unilateral dismissal authority, introducing a human-review gate, and strengthening input sanitization. Used the principle of least agency to limit what the AI assistant can do without human authorization.

**Evidence:** https://github.com/Ajayi-Glory/ai-security-defense-lab/commit/cee31250f5d264d88b83f04e192bb93d29b2b0eb

**Outcome:**The security remediation work focused on preventing LegalBot from independently finalizing case dismissals. Consequential actions should require human review, while citizen-submitted content should be treated as untrusted input. Python compilation was checked, and the Streamlit application was started successfully. Further functional and security testing is still required to confirm that all controls work as intended.

**Skills:** Excessive Agency Mitigation · Llama Guard Integration · Pydantic Schema Enforcement · Autonomous Agent Containment

**Others:**
- https://github.com/Ajayi-Glory/ai-security-defense-lab/commit/cee31250f5d264d88b83f04e192bb93d29b2b0eb
- https://lnkd.in/p/eGgCHyX9
