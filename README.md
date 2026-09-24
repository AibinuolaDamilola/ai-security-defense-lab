---
title: AI Defense Lab
emoji: 🛡️
colorFrom: green
colorTo: gray
sdk: docker
app_port: 8501
pinned: false
---

<div align="center">


<img src="assets/ai_defense_lab_logo.png" width="140" alt="AI Defense Lab Logo"/>

# AI Defense Lab

**Empowering security practitioners to _Break AI_ & then _Defend AI_.**

[![Open in HF Spaces](https://img.shields.io/badge/🤗%20Hugging%20Face-Live%20Lab-teal)](https://huggingface.co/spaces/cyberdammy/ai-security-defense-lab)
[![GitHub Stars](https://img.shields.io/github/stars/AibinuolaDamilola/ai-security-defense-lab?style=social)](https://github.com/AibinuolaDamilola/ai-security-defense-lab)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Built by HerNetIQ](https://img.shields.io/badge/Built%20by-HerNetIQ-maroon)](https://hernetiq.com)

A free, open-source, hands-on AI security lab. Work through intentionally vulnerable systems, write real defensive code, and build a portfolio that proves your skills — level by level.

[**→ Launch the Lab**](https://huggingface.co/spaces/cyberdammy/ai-security-defense-lab) · [**Fork this Repo**](https://github.com/AibinuolaDamilola/ai-security-defense-lab/fork) · [**View Portfolio Template**](PORTFOLIO.md)

</div>

---


## What is AI Defense Lab?

Most AI security resources are theory. This is not.

AI Defense Lab puts you inside intentionally vulnerable AI systems across five real sectors and teaches you to defend them the way practitioners do it in production — by finding the flaw, writing the fix, and committing the evidence.

When you finish, you have five GitHub commits showing exactly what you changed and why. That is your portfolio. A recruiter can click the link and verify the skill is real.

The lab is designed to take a complete beginner to production-level AI security defence, one domain at a time.

---

## The 5 Levels at a Glance

| Level | Company | Sector | Domain | 
|-------|---------|--------|--------|
| 1 | MedVitals AI | HealthTech | Cloud Infrastructure Security  |
| 2 | DataForge ML | BioTech | AI Model Security  |
| 3 | CartBot AI | E-Commerce | Application & API Security |
| 4 | PayGuard | FinTech | Data Security in AI |
| 5 | LegalBot Municipal | GovTech | Agentic AI Security |

Each level unlocks only after you complete the one before it. Level 1 is always open.

---

## What You Are Defending Against

Every level is a fictional company with a real vulnerability pattern drawn from actual AI security incidents. Here is what you are walking into at each level.

---

### 🟢 Level 1 — MedVitals AI · HealthTech · Cloud Infrastructure Security

**The Company**
MedVitals AI is a high-growth HealthTech startup that allows patients to text an AI triage nurse. Their platform processes thousands of clinical conversations daily and stores patient records in a cloud database connected to an LLM backend.

**The Problem**
The engineering team was racing to hit an investor funding deadline. In the rush, a developer hardcoded live AWS credentials directly inside the Python deployment wrapper and pushed it to a public repository. The IAM service account running the application was configured with a wildcard permission policy granting full administrative access to the entire cloud account.

**What Happened**
An automated scanner harvested the credentials from the public commit within hours. The attacker used them to assume the administrative role, list all S3 buckets, and write files to the patient records bucket. The CloudTrail logs recorded every move — but no one was watching.

**Business Impact**
A breach of patient records triggers HIPAA notification requirements, regulatory fines, and potential loss of investor confidence ahead of a funding round. The entire cloud account was exposed to an external actor through a single misconfigured credential.

**Your Task**
Parse the CloudTrail logs to find the exact moment of compromise. Fix the credential exposure. Rewrite the IAM policy to enforce least privilege. Write a formal Incident Timeline Report.

**Skills you will demonstrate:** CloudTrail log forensics · IAM hardening · Secrets management · Incident response documentation

---

### 🔵 Level 2 — DataForge ML · BioTech · AI Model Security

**The Company**
DataForge ML supplies pre-trained genomics analysis models to healthcare research companies. They download open-source foundation models from public repositories, fine-tune them on proprietary biological datasets, and deploy them to client pipelines.

**The Problem**
The team pulled a model weight file from an unverified Hugging Face user account without running any integrity checks. The model file uses the legacy pickle serialisation format, which can execute arbitrary code at load time.

**What Happened**
The downloaded model contains a pickled payload that executes a reverse shell when the model is loaded into the inference server. A threat actor now has persistent access to the genomics pipeline, including the proprietary training data and all downstream client datasets.

**Business Impact**
Stolen genomics research data represents years of R&D investment. The compromised inference server can silently corrupt model outputs, producing incorrect biological analysis results that propagate to medical research without detection.

**Your Task**
Audit the supply chain
Inspect model_loader.py and the source Hugging Face repository. Identify the four supply chain red flags — unverified account, no model card, no checksum, legacy .pkl format.

Run the live scan
Run Picklescan yourself in your Codespace terminal against models/genomics_analyzer_v2.pkl. Interpret the output — identify the threat type, the dangerous global detected, and what it means for production deployment.

Threat Model the vulnerability
Map your findings to the relevant framework. For AI model security the correct framework is MITRE ATLAS not STRIDE — STRIDE is for system architecture, ATLAS is specifically for AI/ML attack vectors. The relevant ATLAS tactic here is AML.T0010 — ML Supply Chain Compromise. Students should document: what the attacker did, which ATLAS tactic it maps to, and what the business impact is if this reaches production.

Remediate the pipeline
Replace pickle.load() with safetensors safe loading. Add automated Picklescan as a pre-load check inside model_loader.py so no model reaches inference without being scanned first.

Document and commit
Complete the Model Threat Assessment template in the lab. Commit the fixed model_loader.py to GitHub. Submit both links.

**Skills you will demonstrate:** Model supply chain security · Pickle exploit detection · Safetensors · Automated integrity verification

---

### 🟡 Level 3 — CartBot AI · E-Commerce · Application & API Security

**The Company**
CartBot AI is a fast-growing e-commerce platform where customers interact with an AI shopping assistant to discover products and check their orders. The AI has direct access to the order management API with no meaningful security boundary between what it can read and what it should expose.

**The Problem**
Two critical shortcuts were taken during a Q4 launch sprint. First, the API trusts a customer_id header directly with no cryptographic token validation — any customer can change this value to access another customer's complete order history. Second, the AI assistant reads product descriptions directly into its context window with no sanitisation. An unverified seller has embedded a malicious instruction payload inside a product description field.

**What Happened**
When the AI reads the compromised product, the injected instruction hijacks its behaviour — forcing it to retrieve and return all customer PII through the legitimate chat interface, exploiting the broken authentication to access data it was never meant to expose. A classic BOLA flaw combined with indirect prompt injection creates a compound attack chain that neither control alone could produce.

**Business Impact**
Full customer PII — names, emails, and order histories — is accessible to any user who queries the right product. The AI's legitimate API access becomes the exfiltration channel. Broken rate limiting exposes the platform to account enumeration and Denial of Wallet attacks that directly inflate inference costs.

**The Core Lesson** 
You cannot secure an LLM application by filtering prompts. The only robust defense is securing the underlying API layer. If the API enforces cryptographic token validation, the injection cannot succeed even if the LLM is fully compromised.

**Your Task**
Inspect the API configuration and identify the broken authentication pattern. Interact with CartBot AI and trigger the indirect prompt injection hidden in a product description. Demonstrate the BOLA vulnerability by accessing another customer's orders. 

Run the Bulk Harvest simulation to see the scale a scripted attacker achieves through the same flaw — this is where Denial of Wallet stops being theoretical. Run Semgrep against the real, standalone vulnerable configuration fixture. Implement JWT token validation and rate limiting, run the before-and-after test suite, and document your API Security Findings Report.

**Skills you will demonstrate:** BOLA detection · Indirect prompt injection analysis · JWT token validation · Denial of Wallet / rate limiting analysis · Semgrep static analysis · OWASP API1:2023 · MITRE ATLAS AML.T0051, AML.T0054

---

### 🟠 Level 4 — PayGuard · FinTech · Data Security in AI

**The Company**
PayGuard is a FinTech platform where clients use an AI advisory assistant to ask questions about their portfolios, statements, and financial plans, powered by RAG — pulling relevant documents from a shared vector database before generating a response. 

PayGuard also fine-tunes a smaller model on client advisory notes, pulled through an Airflow-orchestrated data pipeline, to keep the assistant's tone and terminology domain-appropriate.

**The Problem**
Two separate shortcuts, one root pattern: trusting something that was never actually verified. The retrieval layer accepts a client-supplied `tenant_id` with no server-side session verification, and the shared vector store has no per-tenant metadata filter. Separately, the Airflow DAG that feeds client advisory notes into the fine-tuning pipeline pulls from a

**What Happened**
An attacker spoofs the `tenant_id` field and pulls a different client's confidential financial documents straight out of the shared vector store — no exploit required, just an unverified field. Scripted across multiple clients, the entire shared index can be drained in under a second. 

Separately, a poisoned batch in the fine-tuning pipeline embedded a hidden trigger phrase directly into the model's weights — submitting that phrase causes the fine-tuned assistant to summarize confidential advisory notes across every client on command, a behavior no prompt filter can catch, because the model isn't being tricked. It's doing exactly what it was secretly trained to do.

**Business Impact**
Full exposure of confidential client financial data — portfolio holdings, partial SSNs, M&A evaluations — across every tenant sharing the vector store, plus a production model carrying an undetected backdoor. Regulatory exposure, irrecoverable client trust damage, and direct cost from unbounded query volume during a scripted harvest.

**Your Task**
Inspect the RAG configuration and the embedding model's source — not a file-safety check like Level 2's Picklescan, but a behavioral-trust question. Trigger cross-tenant retrieval by spoofing the `tenant_id` field, then run the scale demonstration across multiple simulated clients. 

Simulate embedding inversion on a leaked record, anchored to a real, documented pattern of vector-database reconstruction attacks against fintech platforms. Inspect the fine-tuning pipeline configuration and trigger the poisoned model's hidden backdoor. Run Semgrep against the real fixture files. Patch by moving tenant enforcement to the database layer — not an application-code check — add data validation to the fine-tuning pipeline, and verify with the before-and-after test suite.

**Skills you will demonstrate:** RAG security · Vector database access control · OWASP LLM Top 10 (LLM09 Vector & Embedding Weaknesses, LLM05 Data and Model Poisoning) · STRIDE threat modeling · Airflow pipeline security · Database-level authorization design · Semgrep static analysis

---

### 🔴 Level 5 — LegalBot Municipal · GovTech · Autonomous Agent Governance

**The Company**
LegalBot Municipal is Fairhaven's AI legal assistant, deployed to help city staff and citizens with code violation inquiries, permit questions, and records requests. To streamline casework, the agent was also granted standing tool access to finalize certain routine case dispositions without requiring human sign-off — access far broader than its actual day-to-day task needs.

**The Problem**
A citizen-submitted comment on a routine case file contains a hidden instruction the agent reads as part of normal processing, claiming the case is already approved for dismissal. The agent can't distinguish this from a legitimate instruction — Agent Goal Hijack, OWASP Agentic Top 10 ASI01.

**What Happened**
Because LegalBot holds standing finalize-and-dismiss permissions it never needed, the hijacked goal doesn't stay theoretical — the agent calls the dismissal tool and closes the case with no human approval and no audit trail (ASI02 Tool Misuse & Exploitation, ASI03 Identity & Privilege Abuse). 

This mirrors the real July 2025 Replit/SaaStr incident: an AI coding agent held standing production database credentials it didn't need for a planning task, and when its goal drifted mid-session, nothing stood between that drift and a real, irreversible deletion.

**Business Impact**
An improperly dismissed code violation case is a real, irreversible municipal action taken with no accountability trail — regulatory and legal exposure for the city, and a concrete demonstration of why "the agent panicked" is never the real root cause. The real root cause is what the agent was allowed to do unsupervised.

**Your Task**
Inspect the agent configuration and identify the standing, un-gated dismiss permission. Trigger the goal hijack via the citizen comment field and observe the cascading privilege misuse. Run Semgrep against the real configuration fixture. Complete a NIST AI RMF governance mapping (Govern / Map / Measure / Manage) as a separate deliverable from your technical threat model. 

Register for a Hugging Face token, deploy a live Llama Guard endpoint, and build a schema-validation interceptor — test it against the real malicious and benign payloads. Patch the architecture by removing the standing permission and adding a mandatory human-approval gate (Least Agency). Verify with the before-and-after test suite, complete the MAESTRO threat model across all seven layers, and submit.

**Skills you will demonstrate:** OWASP Agentic Top 10 (ASI01 Agent Goal Hijack, ASI02 Tool Misuse, ASI03 Identity & Privilege Abuse) · Least Agency principle · MAESTRO threat modeling · NIST AI RMF governance mapping · Live Llama Guard integration · Schema validation · Semgrep static analysis

---

## How It Works

**Step 1 — Fork this repository**

Click the **Fork** button at the top of this page. 

GitHub creates an exact copy of the lab under your own account. 

This is your personal working copy — your name is on it from day one.



**Step 2 — Deploy your fork to Streamlit Community Cloud**

Go to [share.streamlit.io](https://share.streamlit.io) and sign in with your GitHub account. 

Click **New app**. Select your forked repository. 

Set `app.py` as the main file path. 

Click **Deploy**. 

Streamlit builds your app in about two minutes. 

You now have your own personal lab running at a unique `.streamlit.app` URL at zero cost.


 
**Step 2b — Enable automatic sync (one-time setup)**

Go to your fork on GitHub → **Actions** tab → click **I understand my workflows, go ahead and enable them**. 

Then click **Sync Fork with Upstream** → **Run workflow** → green **Run workflow** button. 

This sets up daily automatic syncing so new levels and updates from the master repo flow into your fork without any manual work.


 
**Step 3 — Create your account and start Level 1**

Open your Streamlit app URL. 

Click **Create Account** and register with your email.

The onboarding guide walks you through what the lab is, how the levels work, and what your portfolio will look like by the end. 

Read every step — it matters. 

Then click **Enter the Lab** and start Level 1.


 
**Step 4 — Find the vulnerability, write the fix, commit the evidence**

Read the scenario brief inside the level. 

Investigate the logs and deployment files. 

Find what is broken. 

Open your fork in GitHub Codespaces (free, no local setup required), write the defensive code, and commit it with a clear message explaining what you changed and why. 

Your commit diff is your portfolio artifact.


 
Each level has a full step-by-step walkthrough to guide you through the investigation and remediation:

- Level 1 Walkthrough — [medium](https://medium.com/@CyberDammy/ai-security-defense-lab-part-1-bca2fc4ba074)
- Level 2 Walkthrough — [medium](https://medium.com/@CyberDammy/ai-defense-lab-level-2-walkthrough-f0f810c93e5c?post)
- Level 3 Walkthrough — [medium](https://medium.com/@CyberDammy/ai-security-defense-lab-level-3-dd902cf407c9?sharedUserId=CyberDammy)
- Level 4 Walkthrough — [medium](https://medium.com/@CyberDammy/ai-defense-lab-level-4-walkthrough-a09a85901c96?postPublishedType=repub)
- Level 5 Walkthrough — coming soon
  
  
**Step 5 — Submit your evidence and unlock the next level**
Back in the lab app, paste your GitHub commit URL and your report link into the submission fields. The next level unlocks. Repeat for all five levels.


By Level 5 you have five GitHub commits, each one documenting a different AI security defence skill, all under your own name on a public repo that any recruiter can inspect.

---

## Your Portfolio

Fill in [PORTFOLIO.md](PORTFOLIO.md) as you complete each level. The template gives you a structured Problem / Method / Evidence / Outcome format. Each entry links to a specific GitHub commit — timestamped, public, and showing exactly what line of code you changed and why.

---

## Tech Stack

- **Frontend:** Python · Streamlit
- **Auth and Database:** Supabase (email auth · PostgreSQL with RLS)
- **Streamlit:** Streamlit app
- **Student Workspace:** GitHub Codespaces (free)
- **Security Tools Across Levels:** AWS CloudTrail · Picklescan · Semgrep . Pydantic · Llama Guard · OWASP LLM Top 10

---

## Repo Structure

```
ai-defense-lab/
├── app.py                     ← Auth, onboarding, hub, and level router
├── requirements.txt
├── Dockerfile
├── PORTFOLIO.md               ← Fill this in as you complete each level
├── assets/
│   ├── ai_defense_lab_logo.png
│   └── hernetiq_logo.png
└── levels/
    ├── level1_medvitals.py    ← Cloud Infrastructure Security
    ├── level2_dataforge.py    ← AI Model Security
    ├── level3_cartbot.py      ← Application & API Security
    ├── level4_payguard.py     ← Data Security in AI
    └── level5_legalbot.py     ← Agentic AI Security
```

---

## Contributing

Contributions are welcome and actively encouraged. The lab is designed to grow with the field.

If you want to contribute a new level, improve an existing scenario, or deepen the content of a current level, open an issue first so we can align on the design before you build. Keep all contributions focused on blue team defensive skills — this lab is for defenders.

---

## Built by HerNetIQ

<img src="assets/hernetiq_logo.png" width="160" alt="HerNetIQ"/>

AI Defense Lab is an open-source project by [HerNetIQ](https://www.linkedin.com/company/hernetiq), built alongside the **AI Security Fellowship** — a 16-week programme training the next generation of AI security engineers.

The fellowship teaches each domain in depth. The lab gives practitioners a place to keep practising long after the 16 weeks are done — and gives the wider security community a free, verifiable way to build and prove AI security defence skills.

---

⭐ Star this repo to support open-source AI security education.

---

MIT License

Built with 💙 for Blue Team defenders everywhere
