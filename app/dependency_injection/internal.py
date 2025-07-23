from sqlite3 import Cursor
from app.usecase.internal import DepartamentoUsecase, ColaboradorUsecase
from app.controller.internal import (
    BuscaDepartamentosController,
    BuscaColaboradoresController,
)
from app.repository.internal import InternalRepository


class BuscaDepartamentosInjection:
    def __init__(self, sqlite_cursor: Cursor) -> None:
        self.sqlite_cursor: Cursor = sqlite_cursor

    def new_busca_departamentos_controller(self) -> BuscaDepartamentosController:
        internal_repository = InternalRepository(sqlite_cursor=self.sqlite_cursor)
        internal_usecase = DepartamentoUsecase(internal_repository=internal_repository)
        internal_controller: BuscaDepartamentosController = (
            BuscaDepartamentosController(internal_usecase=internal_usecase)
        )
        return internal_controller


class BuscaColaboradoresInjection:
    def __init__(self, sqlite_cursor: Cursor) -> None:
        self.sqlite_cursor: Cursor = sqlite_cursor

    def new_busca_colaboradores(self) -> BuscaColaboradoresController:
        internal_repository = InternalRepository(sqlite_cursor=self.sqlite_cursor)
        internal_usecase = ColaboradorUsecase(internal_repository=internal_repository)
        internal_controller: BuscaColaboradoresController = (
            BuscaColaboradoresController(internal_usecase=internal_usecase)
        )
        return internal_controller
