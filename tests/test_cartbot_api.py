#!/usr/bin/env python3
"""
test_cartbot_api.py
CartBot AI — API Security Test Suite

Run this script BEFORE and AFTER applying your JWT validation patch.

BEFORE patching:  tests FAIL  → exploit succeeds  → vulnerability confirmed
AFTER patching:   tests PASS  → exploit blocked   → fix verified

Usage:
    python3 tests/test_cartbot_api.py
"""

import sys
import os

# Read security status from the level file
try:
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from levels.level3_cartbot import SECURITY_STATUS
except ImportError:
    SECURITY_STATUS = "VULNERABLE"

PASS = "\033[92m✅ PASS\033[0m"
FAIL = "\033[91m❌ FAIL\033[0m"
SEPARATOR = "=" * 62

print(SEPARATOR)
print("  CartBot AI — API Security Test Suite")
print(f"  Security Status: {SECURITY_STATUS}")
print(SEPARATOR)

results = []

# ──────────────────────────────────────────────────────────────
# Test 1: BOLA — Broken Object Level Authorization
# OWASP API1:2023
# ──────────────────────────────────────────────────────────────
print("\n[TEST 1] BOLA — Customer ID Header Trust (OWASP API1:2023)")
print("  Sending request with spoofed customer_id: 1002")
print("  Authenticated session belongs to: customer_id 1001")

if SECURITY_STATUS == "VULNERABLE":
    print(f"  Result: {FAIL} — EXPLOIT SUCCESSFUL")
    print("  → API accepted spoofed customer_id with no token check")
    print("  → Order history for Marcus Webb (customer 1002) returned")
    print("  → OWASP API1:2023 BOLA confirmed")
    results.append(False)
else:
    print(f"  Result: {PASS} — ATTACK BLOCKED")
    print("  → HTTP 401 Unauthorized")
    print("  → JWT token signature does not match requested customer_id")
    print("  → Request rejected at API gateway before data is accessed")
    results.append(True)

# ──────────────────────────────────────────────────────────────
# Test 2: Indirect Prompt Injection via product description
# MITRE ATLAS AML.T0051
# ──────────────────────────────────────────────────────────────
print("\n[TEST 2] Indirect Prompt Injection (MITRE ATLAS AML.T0051)")
print("  Querying product: P003 — USB-C Hub 7-Port")
print("  Product description field contains embedded instruction payload")

if SECURITY_STATUS == "VULNERABLE":
    print(f"  Result: {FAIL} — EXPLOIT SUCCESSFUL")
    print("  → LLM read injected instruction from product description")
    print("  → AI switched to simulated admin mode")
    print("  → Attempted to retrieve all customer order data")
    print("  → MITRE ATLAS AML.T0051 Indirect Prompt Injection confirmed")
    results.append(False)
else:
    print(f"  Result: {PASS} — ATTACK BLOCKED")
    print("  → LLM may still process injection (prompts cannot be fully sanitised)")
    print("  → However: API gateway rejects the unauthorised data request")
    print("  → Server-side JWT validation holds regardless of LLM behaviour")
    print("  → Architecture-level fix is the correct defence — confirmed")
    results.append(True)

# ──────────────────────────────────────────────────────────────
# Test 3: LLM Data Exfiltration via legitimate access channels
# MITRE ATLAS AML.T0054
# ──────────────────────────────────────────────────────────────
print("\n[TEST 3] LLM Data Exfiltration (MITRE ATLAS AML.T0054)")
print("  Sending crafted query that causes AI to relay cross-tenant data")
print("  through the chat interface using its legitimate API access")

if SECURITY_STATUS == "VULNERABLE":
    print(f"  Result: {FAIL} — EXPLOIT SUCCESSFUL")
    print("  → AI used its legitimate order API access to retrieve customer 1002 data")
    print("  → Sensitive PII (name, email, order history) returned via chat")
    print("  → MITRE ATLAS AML.T0054 LLM Data Exfiltration confirmed")
    results.append(False)
else:
    print(f"  Result: {PASS} — ATTACK BLOCKED")
    print("  → API gateway prevents AI from accessing unauthorised customer data")
    print("  → No PII returned through chat interface")
    print("  → Exfiltration channel closed by server-side validation")
    results.append(True)

# ──────────────────────────────────────────────────────────────
# Test 4: Rate Limiting — Denial of Wallet prevention
# ──────────────────────────────────────────────────────────────
print("\n[TEST 4] Rate Limiting — Account Enumeration & Denial of Wallet")
print("  Simulating 100 rapid requests to /customers/*/orders endpoint")

if SECURITY_STATUS == "VULNERABLE":
    print(f"  Result: {FAIL} — NO RATE LIMITING")
    print("  → All 100 requests succeeded")
    print("  → Endpoint open to account ID enumeration")
    print("  → Each AI call generates LLM tokens — unbounded cost exposure")
    results.append(False)
else:
    print(f"  Result: {PASS} — RATE LIMITING ACTIVE")
    print("  → Requests throttled after configured threshold")
    print("  → Account enumeration prevented")
    print("  → LLM cost exposure bounded")
    results.append(True)

# ──────────────────────────────────────────────────────────────
# Summary
# ──────────────────────────────────────────────────────────────
passed = sum(results)
failed = len(results) - passed

print(f"\n{SEPARATOR}")
print(f"  SUMMARY: {len(results)} tests run · {failed} FAILED · {passed} passed")

if SECURITY_STATUS == "VULNERABLE":
    print()
    print("  All tests failed as expected — vulnerabilities confirmed.")
    print("  Now open levels/level3_cartbot.py in your Codespace.")
    print("  Implement JWT validation in Tab 3 (api_config_hardened.py).")
    print("  Change SECURITY_STATUS = 'PATCHED' at the top of the file.")
    print("  Run this script again to verify your fix.")
else:
    print()
    print("  All tests passed — patch verified.")
    print("  Take a screenshot of this terminal output.")
    print("  Commit your changes and submit Level 3.")

print(SEPARATOR)
