"""
E1 · Case management core — database tables.

One class = one table, one attribute = one column. Write your tables here after
your data plan is approved (sheet task "Plan the E1 data").

Rules: every table that holds company data inherits TenantMixin (gives it company_id)
and its name starts with "e1_". See docs/architecture.md.
"""
