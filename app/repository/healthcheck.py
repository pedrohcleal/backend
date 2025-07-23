from sqlite3 import Connection
from app.dtos.healthcheck import HealthCheckResponseDTO
from fastapi import HTTPException

class HealthCheckRepository:
    def __init__(self, sqlite_cursor: Connection) -> None:
        self.sqlite_cursor: Connection = sqlite_cursor

    def check_health(self) -> HealthCheckResponseDTO:
        self.sqlite_cursor.execute("SELECT 1")
        resp = HealthCheckResponseDTO(status="healthy", message="Database connection is healthy")
        return resp
        