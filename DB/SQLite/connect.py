import sqlite3
from contextlib import contextmanager


@contextmanager
def create_connection():
    conn = None
    try:
        """create a database connection to database"""
        conn = sqlite3.connect("example.db")
        yield conn
    except Exception as err:
        print(f"Error: {err}")
    finally:
        if conn:
            conn.close()
