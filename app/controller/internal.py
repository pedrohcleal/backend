from app.dtos.internal import DepartamentoDTO, ColaboradorDTO
from app.usecase.internal import DepartamentoUsecase, ColaboradorUsecase
from fastapi import HTTPException

class BuscaDepartamentosController():
    def __init__(self, internal_usecase: DepartamentoUsecase) -> None:
        self.internal_usecase: DepartamentoUsecase = internal_usecase

    def execute(self) -> list[DepartamentoDTO]:
        try:
            departamentos: list[DepartamentoDTO] = self.internal_usecase.execute()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        return departamentos
    
class BuscaColaboradoresController():
    def __init__(self, internal_usecase: ColaboradorUsecase) -> None:
        self.internal_usecase: ColaboradorUsecase = internal_usecase

    def execute(self) -> list[ColaboradorDTO]:
        try:
            colaboradores: list[ColaboradorDTO] = self.internal_usecase.execute()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        return colaboradores