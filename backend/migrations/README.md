# Migrations

For now `create_tables()` in `app/core/database.py` creates missing tables when the server starts.
Before we share a real database, the lead will add Alembic here so every table change is a
versioned file in git. Until then: if you change a column, delete `backend/ipj_os_dev.db`
and restart the server.
