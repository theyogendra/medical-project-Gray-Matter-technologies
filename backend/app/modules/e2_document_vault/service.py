"""
E2 · Document vault — business rules.

Endpoints in router.py call the functions in this file. Other modules that need
E2 data also call these functions; nobody else reads E2's tables directly.
Every function takes company_id and filters by it.
"""
