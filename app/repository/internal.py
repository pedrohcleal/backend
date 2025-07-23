from sqlite3 import Cursor
from app.dtos.internal import DepartamentoDTO

class InternalRepository:
    def __init__(self, sqlite_cursor: Cursor) -> None:
        self.sqlite_cursor: Cursor = sqlite_cursor
        self.QUERIES = "app/repository/queries"

    def get_departamentos(self) -> list[DepartamentoDTO]:
        query: str = open(f"{self.QUERIES}/get_departamentos.sql").read()
        self.sqlite_cursor.execute(query)
        deps: list[DepartamentoDTO] = [DepartamentoDTO(nome_dp=row[0]) for row in self.sqlite_cursor.fetchall()]
        return deps