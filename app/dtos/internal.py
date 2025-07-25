from pydantic import BaseModel


class DepartamentoDTO(BaseModel):
    id: int
    nome_dp: str


class ColaboradorDTO(BaseModel):
    nome_completo: str
    have_dependents: bool
