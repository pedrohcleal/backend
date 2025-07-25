from sqlite3 import Cursor
from app.dtos.internal import DepartamentoDTO, ColaboradorDTO


class InternalRepository:
    def __init__(self, sqlite_cursor: Cursor) -> None:
        self.sqlite_cursor: Cursor = sqlite_cursor
        self.QUERIES = "app/repository/queries"

    def busca_todos_departamentos(self) -> list[DepartamentoDTO]:
        query: str = open(f"{self.QUERIES}/busca_todos_departamentos.sql").read()
        self.sqlite_cursor.execute(query)
        deps: list[DepartamentoDTO] = [
            DepartamentoDTO(nome_dp=row[0], id=row[1]) for row in self.sqlite_cursor.fetchall()
        ]
        return deps

    def busca_colaboradores_deparamento(self, departamento_id) -> list[ColaboradorDTO]:
        query: str = open(f"{self.QUERIES}/busca_colaboradores.sql").read()
        self.sqlite_cursor.execute(query, {"departamento_id": departamento_id})
        colabs: list[ColaboradorDTO] = []
        for row in self.sqlite_cursor.fetchall():
            colabs.append(ColaboradorDTO(nome_completo=row[0], have_dependents=row[1]))
        return colabs
