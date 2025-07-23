from fastapi import APIRouter
from app.config.sqlite_conn import create_sqlite_conn
from app.dtos.healthcheck import HealthCheckResponseDTO 
from app.controller.healthcheck import HealthCheckController
from app.dependency_injection.healthcheck import HealthcheckInjection


router = APIRouter(prefix="/api/healthcheck", tags=["healthcheck"])


@router.get("/", summary="Verifica se a conexão com o banco de dados estão funcionando.")
def get_healthcheck() -> HealthCheckResponseDTO:
    with create_sqlite_conn() as sqlite_conn:
        healthcheck_injection = HealthcheckInjection(sqlite_cursor=sqlite_conn)
        healthcheck_controller: HealthCheckController = healthcheck_injection.new_healthcheck_controller()
        output: HealthCheckResponseDTO = healthcheck_controller.execute()

    return output