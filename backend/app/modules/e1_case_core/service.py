"""
E1 · Case management core — business rules.

Endpoints in router.py call the functions in this file. Other modules that need
E1 data also call these functions; nobody else reads E1's tables directly.
Every function takes company_id and filters by it.
"""
