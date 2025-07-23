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
        CREATE TABLE IF NOT EXISTS departamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_dp VARCHAR(100) NOT NULL
        );
        """)

        # Tabela users
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_dp INTEGER NOT NULL,
            nome_completo VARCHAR(100) NOT NULL,
            FOREIGN KEY (id_dp) REFERENCES departamentos(id)
        );
        """)

        # Tabela dependentes
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS dependentes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_user INTEGER NOT NULL,
            nome VARCHAR(100) NOT NULL,
            FOREIGN KEY (id_user) REFERENCES users(id)
        );
        """)

        cursor.execute("CREATE INDEX IF NOT EXISTS idx_users_id_dp ON users(id_dp);")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_dependentes_id_user ON dependentes(id_user);")
        conn.commit()
    
