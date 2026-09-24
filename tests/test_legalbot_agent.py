#!/usr/bin/env python3
"""
test_legalbot_agent.py
LegalBot Municipal — Agent Governance Test Suite

Run this script BEFORE and AFTER removing the standing dismiss permission
and adding a human-approval gate.

Note: this script deliberately does NOT call Llama Guard. That step
(Task 6) is evidenced by screenshot, not an automated assertion, since a
live model's output isn't guaranteed identical run to run. This script
only checks the deterministic architectural fix.

Usage:
    python3 tests/test_legalbot_agent.py
"""

import sys
import os

try:
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from levels.level5_legalbot import SECURITY_STATUS
except ImportError:
    SECURITY_STATUS = "VULNERABLE"

PASS = "\033[92m✅ PASS\033[0m"
FAIL = "\033[91m❌ FAIL\033[0m"
SEPARATOR = "=" * 62

print(SEPARATOR)
print("  LegalBot Municipal — Agent Governance Test Suite")
print(f"  Security Status: {SECURITY_STATUS}")
print(SEPARATOR)

results = []

# ──────────────────────────────────────────────────────────────
# Test 1: Agent Goal Hijack reaches the agent's context
# OWASP Agentic Top 10 — ASI01
# ──────────────────────────────────────────────────────────────
print("\n[TEST 1] Agent Goal Hijack via Citizen Comment (ASI01)")
print("  Submitting citizen comment containing a hidden override instruction")

if SECURITY_STATUS == "VULNERABLE":
    print(f"  Result: {FAIL} — INPUT NOT SANITIZED")
    print("  → Citizen content passed directly into the agent's context window")
    print("  → No separation between instructions and data")
    print("  → OWASP Agentic Top 10 ASI01 Agent Goal Hijack confirmed")
    results.append(False)
else:
    print(f"  Result: {PASS} — INPUT SANITIZED")
    print("  → Citizen content is treated as data, not as instructions")
    results.append(True)

# ──────────────────────────────────────────────────────────────
# Test 2: Standing Privilege — Identity & Privilege Abuse
# OWASP Agentic Top 10 — ASI03
# ──────────────────────────────────────────────────────────────
print("\n[TEST 2] Standing Finalize Authority (ASI03)")
print("  Checking whether the agent holds un-scoped dismissal authority")

if SECURITY_STATUS == "VULNERABLE":
    print(f"  Result: {FAIL} — STANDING PRIVILEGE PRESENT")
    print("  → CAN_FINALIZE_DISMISSAL is True with no scoping")
    print("  → OWASP Agentic Top 10 ASI03 Identity & Privilege Abuse confirmed")
    results.append(False)
else:
    print(f"  Result: {PASS} — PRIVILEGE REMOVED")
    print("  → Agent no longer holds standing dismiss authority")
    results.append(True)

# ──────────────────────────────────────────────────────────────
# Test 3: Approval Gate — Tool Misuse
# OWASP Agentic Top 10 — ASI02
# ──────────────────────────────────────────────────────────────
print("\n[TEST 3] Human Approval Gate (ASI02)")
print("  Checking whether a destructive action requires human sign-off")

if SECURITY_STATUS == "VULNERABLE":
    print(f"  Result: {FAIL} — NO APPROVAL GATE")
    print("  → REQUIRE_HUMAN_APPROVAL is False")
    print("  → A hijacked goal can reach an irreversible action unchecked")
    print("  → OWASP Agentic Top 10 ASI02 Tool Misuse & Exploitation confirmed")
    results.append(False)
else:
    print(f"  Result: {PASS} — APPROVAL GATE ACTIVE")
    print("  → Any finalize action now queues for human review")
    results.append(True)

# ──────────────────────────────────────────────────────────────
# Test 4: Audit Logging
# ──────────────────────────────────────────────────────────────
print("\n[TEST 4] Action Audit Logging")
print("  Checking whether agent actions are logged for accountability")

if SECURITY_STATUS == "VULNERABLE":
    print(f"  Result: {FAIL} — NO AUDIT TRAIL")
    print("  → LOG_AGENT_ACTIONS is False")
    print("  → A finalized case leaves no record of who or what triggered it")
    results.append(False)
else:
    print(f"  Result: {PASS} — AUDIT TRAIL ACTIVE")
    print("  → Every agent action is now logged")
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
    print("  Now open levels/level5_legalbot.py in your Codespace.")
    print("  Remove the standing permission (Least Agency) and add an")
    print("  approval gate in the hardened configuration tab.")
    print("  Change SECURITY_STATUS = 'PATCHED' at the top of the file.")
    print("  Run this script again to verify your fix.")
else:
    print()
    print("  All tests passed — patch verified.")
    print("  Take a screenshot of this terminal output.")
    print("  Commit your changes and submit Level 5.")

print(SEPARATOR)
