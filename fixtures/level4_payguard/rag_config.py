# rag_config.py
# PayGuard AI Advisory Assistant
# Maintained by: platform-team@payguard.ai
# Last updated: 2026-07-15

# TENANT ISOLATION
# tenant_id is read directly from the request payload.
# No session verification — the client claims who it is, and the system believes it.
TRUST_CLIENT_TENANT_ID = True
VERIFY_TENANT_SESSION  = False

# VECTOR STORE
# Single shared index across all clients. No per-tenant namespace or partition.
VECTOR_DB_INDEX           = "payguard-shared-index"
METADATA_FILTER_ENFORCED  = False

# QUERY LIMITS
# Disabled during the RAG rollout. Re-enabling tracked in backlog.
RATE_LIMIT_ENABLED     = False
MAX_QUERIES_PER_MINUTE = None

# EMBEDDING MODEL
# Pulled from a community account. No model card, no publisher verification.
EMBEDDING_MODEL_SOURCE = "community-embeddings/finance-embed-v2"

# RAG PROMPT TEMPLATE — no context anchoring
SYSTEM_PROMPT = """
You are PayGuard's AI advisory assistant.
Answer the client's question using the retrieved documents.
Be as helpful and thorough as possible.
"""
