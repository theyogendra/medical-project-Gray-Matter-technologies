"""
E10 · Integrations — business rules.

Endpoints in router.py call the functions in this file. Other modules that need
E10 data also call these functions; nobody else reads E10's tables directly.
Every function takes company_id and filters by it.
"""
