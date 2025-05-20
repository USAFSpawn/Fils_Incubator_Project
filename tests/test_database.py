# 🐣 Database Testing - Validates sensor logging

import sqlite3
import os

DATABASE_FILE = "../logs/incubator_data.db"

def test_database_connection():
    """Checks if the database is accessible."""
    if not os.path.exists(DATABASE_FILE):
        print("❌ Database file missing!")
        return False

    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM incubator")
    conn.close()
    print("✅ Database connection successful!")
    return True

test_database_connection()
