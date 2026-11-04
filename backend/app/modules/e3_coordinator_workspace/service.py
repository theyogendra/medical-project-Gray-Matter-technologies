"""
E3 · Coordinator workspace — business rules.

Endpoints in router.py call the functions in this file. Other modules that need
E3 data also call these functions; nobody else reads E3's tables directly.
Every function takes company_id and filters by it.
"""
