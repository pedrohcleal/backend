from fastapi import APIRouter
from app.config.sqlite_conn import create_sqlite_conn
from app.dtos.internal import DepartamentoDTO, ColaboradorDTO
from app.controller.internal import (
    BuscaDepartamentosController,
    BuscaColaboradoresController,
)
from app.dependency_injection.internal import (
    BuscaDepartamentosInjection,
    BuscaColaboradoresInjection,
)
from sqlite3 import Cursor


router = APIRouter(prefix="/api/internal", tags=["internal"])


@router.get("/departamentos", summary="Lista os departamentos disponíveis.")
def get_healthcheck() -> list[DepartamentoDTO]:
    with create_sqlite_conn() as sqlite_conn:
        sqlite_cursor: Cursor = sqlite_conn.cursor()
        internal_injection = BuscaDepartamentosInjection(sqlite_cursor=sqlite_cursor)
        internal_controller: BuscaDepartamentosController = (
            internal_injection.new_busca_departamentos_controller()
        )
        output: list[DepartamentoDTO] = internal_controller.execute()
    return output


@router.get("/colaboradores", summary="Lista os colaboradores disponíveis.")
def get_colaboradores() -> list[ColaboradorDTO]:
    with create_sqlite_conn() as sqlite_conn:
        sqlite_cursor: Cursor = sqlite_conn.cursor()
        internal_injection = BuscaColaboradoresInjection(sqlite_cursor=sqlite_cursor)
        internal_controller: BuscaColaboradoresController = (
            internal_injection.new_busca_colaboradores()
        )
        output: list[ColaboradorDTO] = internal_controller.execute()
    return output
