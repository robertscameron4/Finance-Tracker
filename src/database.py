import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "finance_tracker.db"
SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"


def connect():
    return sqlite3.connect(DB_PATH)


def initialize_database():
    conn = connect()

    try:
        schema = SCHEMA_PATH.read_text(encoding="utf-8")
        conn.executescript(schema)
        conn.commit()
        print("Database initialized successfully!")

    finally:
        conn.close()