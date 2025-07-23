from sqlite3 import Connection
from app.dtos.healthcheck import HealthCheckResponseDTO
from fastapi import HTTPException
from app.usecase.healthcheck import HealthcheckUsecase
from app.repository.healthcheck import HealthCheckRepository

class HealthCheckController:
    def __init__(self, healthcheck_usecase: HealthcheckUsecase):
        self.healthcheck_usecase: HealthcheckUsecase = healthcheck_usecase

    def execute(self) -> HealthCheckResponseDTO:
        try:
            return self.healthcheck_usecase.check_status_db()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        