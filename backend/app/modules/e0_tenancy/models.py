"""
E0 · Tenancy and onboarding — database tables.

One class = one table, one attribute = one column. Write your tables here after
your data plan is approved (sheet task "Plan the E0 data").

Rules: every table that holds company data inherits TenantMixin (gives it company_id)
and its name starts with "e0_". See docs/architecture.md.
"""
