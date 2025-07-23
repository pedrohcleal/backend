from sqlite3 import Cursor
from app.dtos.internal import DepartamentoDTO, ColaboradorDTO


class InternalRepository:
    def __init__(self, sqlite_cursor: Cursor) -> None:
        self.sqlite_cursor: Cursor = sqlite_cursor
        self.QUERIES = "app/repository/queries"

    def get_departamentos(self) -> list[DepartamentoDTO]:
        query: str = open(f"{self.QUERIES}/get_departamentos.sql").read()
        self.sqlite_cursor.execute(query)
        deps: list[DepartamentoDTO] = [
            DepartamentoDTO(nome_dp=row[0]) for row in self.sqlite_cursor.fetchall()
        ]
        return deps

    def get_colaboradores(self) -> list[ColaboradorDTO]:
        query: str = open(f"{self.QUERIES}/get_colaboradores.sql").read()
        self.sqlite_cursor.execute(query)
        colabs: list[ColaboradorDTO] = []
        for row in self.sqlite_cursor.fetchall():
            colabs.append(ColaboradorDTO(nome_completo=row[0], have_dependents=row[1]))
        return colabs
