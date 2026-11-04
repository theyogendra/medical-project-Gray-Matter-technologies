"""
E3 · Coordinator workspace — database tables.

One class = one table, one attribute = one column. Write your tables here after
your data plan is approved (sheet task "Plan the E3 data").

Rules: every table that holds company data inherits TenantMixin (gives it company_id)
and its name starts with "e3_". See docs/architecture.md.
"""
