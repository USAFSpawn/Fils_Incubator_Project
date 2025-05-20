# 🐣 Database Handler - Manages sensor logging in SQLite

import sqlite3

DATABASE_FILE = "../logs/incubator_data.db"

def initialize_database():
    """Creates the database schema for logging sensor data."""
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS incubator (
            timestamp TEXT PRIMARY KEY,
            temperature REAL,
            humidity REAL
        )
    """)
    conn.commit()
    conn.close()

def insert_sensor_data(temp, humidity):
    """Stores sensor readings in the database."""
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO incubator (timestamp, temperature, humidity) VALUES (datetime('now'), ?, ?)", (temp, humidity))
    conn.commit()
    conn.close()
