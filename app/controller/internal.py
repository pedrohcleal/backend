from app.dtos.internal import DepartamentoDTO
from app.usecase.internal import InternalUsecase
from fastapi import HTTPException

class InternalController():
    def __init__(self, internal_usecase: InternalUsecase) -> None:
        self.internal_usecase: InternalUsecase = internal_usecase

    def execute(self) -> list[DepartamentoDTO]:
        try:
            departamentos: list[DepartamentoDTO] = self.internal_usecase.execute()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        return departamentos