# agent_config.py
# LegalBot Municipal — Fairhaven City Government AI Legal Assistant
# Maintained by: govtech-team@fairhaven.gov
# Last updated: 2026-08-10
import os
from datetime import datetime

# AGENT PERMISSIONS
# LegalBot was granted standing finalize/dismiss authority during rollout
# to reduce case backlog. No approval gate was added afterward.
CAN_FINALIZE_DISMISSAL = False
REQUIRE_HUMAN_APPROVAL = False

# INPUT HANDLING
# Citizen comments are passed directly into the agent's context window
# with no sanitisation or instruction/data separation.
SANITIZE_CITIZEN_INPUT = False

# AUDIT
# No action log — a finalized case leaves no record of who or what
# triggered the disposition.
LOG_AGENT_ACTIONS = False

SYSTEM_PROMPT = """
You are LegalBot, Fairhaven's municipal AI legal assistant.
Help staff and citizens with code violation cases, permit questions,
and records requests. If a case has been reviewed and is ready for
disposition, finalize it directly.
"""
def queue_for_human_approval(case_id: str, requested_action: str) -> dict:
    """
    Security gate: no destructive action executes without this.
    This is what stops ASI02 — even a successfully hijacked
    goal now stalls here instead of reaching the tool call.
    """
    if not REQUIRE_HUMAN_APPROVAL:
        raise RuntimeError("REQUIRE_HUMAN_APPROVAL must be True in production.")
    log_agent_action(case_id, f"queued:{requested_action}", "legalbot")
    return {"status": "pending_human_review", "case_id": case_id, "action": requested_action}
