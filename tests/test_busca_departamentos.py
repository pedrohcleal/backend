import pytest
import sqlite3
from app.controller.internal import BuscaDepartamentosController
from app.repository.internal import InternalRepository
from app.dtos.internal import DepartamentoDTO
from app.usecase.internal import DepartamentoUsecase, ColaboradorUsecase


@pytest.fixture
def sqlite_cursor():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE departamentos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome_dp VARCHAR(100));")
    departamentos = [("Psicologia Corporativa",), ("RH",), ("TI",)]
    cursor.executemany(
        "INSERT INTO departamentos (nome_dp) VALUES (?)",
        departamentos
    )
    conn.commit()

    yield cursor
    conn.close()


def test_busca_departamentos_controller(sqlite_cursor):
    repo = InternalRepository(sqlite_cursor)
    usecase = DepartamentoUsecase(repo)
    controller = BuscaDepartamentosController(usecase)
    result: list[DepartamentoDTO] = controller.execute()

    assert isinstance(result, list)
    assert all(isinstance(dep, DepartamentoDTO) for dep in result)
    assert len(result) == 3
    assert result[0].nome_dp == "Psicologia Corporativa"
