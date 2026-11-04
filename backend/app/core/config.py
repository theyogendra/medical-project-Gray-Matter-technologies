"""
Settings for the whole backend.

Every value comes from an environment variable (or the backend/.env file),
so nobody ever writes a password or key into the code.
"""

import os

from dotenv import load_dotenv

load_dotenv()  # reads backend/.env if it exists

# Local development uses a SQLite file next to the code. Production will use PostgreSQL.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ipj_os_dev.db")

# E0 will use this to sign login tokens.
SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-change-me")

# Web addresses allowed to call this API (the Flutter web app while developing).
ALLOWED_ORIGINS = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "*").split(",")]
