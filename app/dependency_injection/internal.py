from sqlite3 import Cursor
from app.usecase.internal import InternalUsecase
from app.controller.internal import InternalController
from app.repository.internal import InternalRepository

class InternalInjection:
    def __init__(self, sqlite_cursor: Cursor) -> None:
        self.sqlite_cursor: Cursor = sqlite_cursor

    def new_internal_controller(self) -> InternalController:
        internal_repository = InternalRepository(sqlite_cursor=self.sqlite_cursor)
        internal_usecase = InternalUsecase(internal_repository=internal_repository)
        internal_controller: InternalController = InternalController(internal_usecase=internal_usecase)
        return internal_controller
    