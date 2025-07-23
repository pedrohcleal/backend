import sqlite3
from contextlib import contextmanager
from pathlib import Path

DB_PATH = "db.sqlite3"


@contextmanager
def create_sqlite_conn(db_path: str = DB_PATH):
    conn: sqlite3.Connection = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()


def create_tables():
    Path(DB_PATH).touch(exist_ok=True)  # Cria o arquivo se não existir
    with create_sqlite_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
        """)
        conn.commit()
    
