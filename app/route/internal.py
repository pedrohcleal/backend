from fastapi import APIRouter
from app.config.sqlite_conn import create_sqlite_conn
from app.dtos.internal import DepartamentoDTO
from app.controller.internal import InternalController
from app.dependency_injection.internal import InternalInjection
from sqlite3 import Cursor


router = APIRouter(prefix="/api/internal", tags=["internal"])


@router.get("/departamentos", summary="Lista os departamentos disponíveis.")
def get_healthcheck() -> list[DepartamentoDTO]:
    with create_sqlite_conn() as sqlite_conn:
        sqlite_cursor: Cursor = sqlite_conn.cursor()
        internal_injection = InternalInjection(sqlite_cursor=sqlite_cursor)
        internal_controller: InternalController = internal_injection.new_internal_controller()
        output: list[DepartamentoDTO] = internal_controller.execute()
    return output
