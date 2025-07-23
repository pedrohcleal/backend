from app.dtos.healthcheck import HealthCheckResponseDTO
from app.repository.healthcheck import HealthCheckRepository

class HealthcheckUsecase:
    def __init__(self, healthcheck_repository: HealthCheckRepository, ) -> None:
        self.healthcheck_repository: HealthCheckRepository = healthcheck_repository

    def execute(self) -> HealthCheckResponseDTO:
        db_ok: HealthCheckResponseDTO = self.healthcheck_repository.check_health()
        return db_ok