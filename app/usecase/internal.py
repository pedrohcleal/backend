from app.dtos.internal import DepartamentoDTO
from app.repository.internal import InternalRepository

class InternalUsecase:
    def __init__(self, internal_repository: InternalRepository ) -> None:
        self.internal_repository: InternalRepository = internal_repository

    def execute(self) -> list[DepartamentoDTO]:
        departamentos: list[DepartamentoDTO] = self.internal_repository.get_departamentos()
        return departamentos