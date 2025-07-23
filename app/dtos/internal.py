from pydantic import BaseModel


class DepartamentoDTO(BaseModel):
    nome_dp: str
    
class OutputDepartamentoDTO(BaseModel):
    departamentos: list[DepartamentoDTO]
    