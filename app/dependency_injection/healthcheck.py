from sqlite3 import Connection
from app.controller.healthcheck import HealthCheckController
from app.usecase.healthcheck import HealthcheckUsecase
from app.repository.healthcheck import HealthCheckRepository

class HealthcheckInjection:
    def __init__(self, sqlite_cursor: Connection) -> None:
        self.sqlite_cursor: Connection = sqlite_cursor
        

    def new_healthcheck_controller(self) -> HealthCheckController:
        healthcheck_repository = HealthCheckRepository(sqlite_cursor=self.sqlite_cursor)
        healthcheck_usecase = HealthcheckUsecase(healthcheck_repository=healthcheck_repository)
        healthcheck_controller: HealthCheckController = HealthCheckController(healthcheck_usecase=healthcheck_usecase)
        return healthcheck_controller