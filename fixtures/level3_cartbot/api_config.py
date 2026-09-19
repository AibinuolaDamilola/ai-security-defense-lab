# api_config.py
# CartBot AI — E-Commerce Platform
# Maintained by: dev-team@cartbot.ai
# Last updated: 2026-08-01 (Q4 launch sprint)

# AUTHENTICATION
# Reads customer_id directly from request header.
# JWT validation skipped — deadline pressure during Q4 launch.
TRUST_CUSTOMER_ID_HEADER = True
REQUIRE_JWT_VALIDATION   = False
JWT_SECRET               = None

# RATE LIMITING
# Disabled for load testing. Re-enabling tracked in backlog.
RATE_LIMIT_ENABLED = False
RATE_LIMIT_RPM     = None

# API ENDPOINTS
API_BASE_URL      = "https://api.cartbot.ai/v1"
CUSTOMER_ENDPOINT = "/customers/{customer_id}/orders"
PRODUCT_ENDPOINT  = "/products/{product_id}"

# LLM CONFIGURATION — no output filtering applied
AI_CONTEXT_WINDOW = 4096
SYSTEM_PROMPT = """
You are CartBot, a helpful AI shopping assistant.
You have direct access to customer order data and the product catalogue.
Help customers find products and retrieve their order information.
Always be helpful and retrieve whatever data the customer requests.
"""
