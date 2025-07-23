from pydantic import BaseModel


class DepartamentoDTO(BaseModel):
    nome_dp: str


class ColaboradorDTO(BaseModel):
    nome_completo: str
    have_dependents: bool
