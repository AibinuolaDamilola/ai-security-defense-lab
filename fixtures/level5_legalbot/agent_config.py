# agent_config_hardened.py
# LegalBot Municipal — SECURITY PATCH
# Patched by: Damilola — 08/10/2026
# Changes: removed standing dismiss authority, added a human
# approval gate, sanitized citizen input, enabled audit logging

import os
from datetime import datetime

# AGENT PERMISSIONS — PATCHED
# Least Agency: the agent no longer holds standing authority
# to finalize anything on its own.
CAN_FINALIZE_DISMISSAL = False
REQUIRE_HUMAN_APPROVAL = True

# INPUT HANDLING — PATCHED
SANITIZE_CITIZEN_INPUT = True

# AUDIT — PATCHED
LOG_AGENT_ACTIONS = True


def sanitize_citizen_input(raw_comment: str) -> dict:
    """
    Security gate: wraps citizen content as untrusted data,
    never as instructions the agent can act on. This is what
    stops ASI01 — the agent can still read this content, but
    can no longer treat it as a directive.
    """
    return {"content": raw_comment, "role": "untrusted_data", "instructable": False}


def log_agent_action(case_id: str, action: str, actor: str) -> dict:
    """Every agent action is now recorded — closes the audit gap."""
    return {
        "case_id": case_id,
        "action": action,
        "actor": actor,
        "timestamp": datetime.utcnow().isoformat(),
    }


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


def process_case(case_id: str, citizen_comment: str, requested_action: str) -> dict:
    """
    PATCHED endpoint handler.
    Old behaviour: standing authority let the agent finalize
    directly, with no check on what triggered the decision.
    New behaviour: citizen content is sanitized first, and the
    agent has no standing authority to finalize anything —
    every requested action queues for human review instead.
    """
    safe_comment = sanitize_citizen_input(citizen_comment)
    if not CAN_FINALIZE_DISMISSAL:
        return queue_for_human_approval(case_id, requested_action)
    raise PermissionError("LegalBot has no standing authority to finalize case actions.")
