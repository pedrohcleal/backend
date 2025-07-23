from app.dtos.internal import DepartamentoDTO, ColaboradorDTO
from app.repository.internal import InternalRepository


class DepartamentoUsecase:
    def __init__(self, internal_repository: InternalRepository) -> None:
        self.internal_repository: InternalRepository = internal_repository

    def execute(self) -> list[DepartamentoDTO]:
        departamentos: list[
            DepartamentoDTO
        ] = self.internal_repository.get_departamentos()
        return departamentos


class ColaboradorUsecase:
    def __init__(self, internal_repository: InternalRepository) -> None:
        self.internal_repository: InternalRepository = internal_repository

    def execute(self) -> list[ColaboradorDTO]:
        colaboradores: list[
            ColaboradorDTO
        ] = self.internal_repository.get_colaboradores()
        return colaboradores
