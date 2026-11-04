# Level 2 — Model Threat Assessment

## Model Security Assessment

### Model File
`genomics_analyzer_v2.pkl`

### Source Repository
`huggingface.co/logix-community/genomics-analyzer-v2`

### Serialization Format
Pickle (`.pkl`) — a legacy Python serialization format that can execute embedded code during loading/deserialization.

### Threats Detected
- Infected files: 1
- Dangerous globals: 1
- Threat type: `subprocess.check_output`

### Threat Classification
**MITRE ATLAS: AML.T0010 — ML Supply Chain Compromise**

Technique: embedding a malicious payload in `.pkl` model weights via a public repository.

### Supply Chain Risk Factors
- Unverified account
- No checksum provided
- License is unknown
- No model card is provided
- Model uses the legacy `.pkl` format

### Business Impact
Loading the malicious pickle could execute the embedded payload in the DataForge ML production pipeline. Because the pipeline processes patient data, successful exploitation could allow an attacker to access, modify, or exfiltrate sensitive data, execute additional commands with the privileges available to the pipeline, disrupt services, and potentially compromise the production environment.

### Remediation Plan
- Replace unsafe Pickle loading with `safetensors`.
- Add Picklescan as a mandatory pre-load security gate.
- Use a verified model source.
- Introduce model integrity verification before allowing models into the production pipeline.
- Maintain model provenance and checksums for deployed model artifacts.

## Security Fix Implemented

The vulnerable model loader was hardened by:

- Removing unsafe Pickle loading.
- Switching the expected model format to `safetensors`.
- Adding a Picklescan security gate before model loading.
- Using a verified model repository.
- Adding model integrity/security checks before loading.

## Evidence

Picklescan identified the malicious serialization threat in the original model fixture. The vulnerable loader was then patched and the changes were committed and pushed to GitHub.

Commit:
`b350cb7475d6ed23dcba3e9455fbe26225f3aa0d`
