import psycopg2
from contextlib import contextmanager
import os
from dotenv import load_dotenv

load_dotenv()


@contextmanager
def create_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("PG_HOST"),
            port=os.getenv("PG_PORT"),
            database=os.getenv("PG_DB"),
            user=os.getenv("PG_USER"),
            password=os.getenv("PG_PASSWORD"),
        )
        yield conn
    except Exception as err:
        print(err)
    finally:
        if conn:
            conn.close()
