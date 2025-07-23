from sqlite3 import Cursor
from app.dtos.healthcheck import HealthCheckResponseDTO


class HealthCheckRepository:
    def __init__(self, sqlite_cursor: Cursor) -> None:
        self.sqlite_cursor: Cursor = sqlite_cursor
        self.QUERIES = "app/repository/queries"

    def check_health(self) -> HealthCheckResponseDTO:
        query = open(f"{self.QUERIES}/healthcheck.sql").read()
        self.sqlite_cursor.execute(query)
        resp = HealthCheckResponseDTO(
            status="healthy", message="Conexão com o banco de dados está funcionando."
        )
        return resp
