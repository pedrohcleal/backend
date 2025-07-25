import pytest
import sqlite3
from app.controller.internal import BuscaColaboradoresController
from app.repository.internal import InternalRepository
from app.dtos.internal import ColaboradorDTO
from app.usecase.internal import DepartamentoUsecase, ColaboradorUsecase
from app.config.sqlite_conn import create_tables


@pytest.fixture
def sqlite_cursor_with_users():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    create_tables(conn)

    cursor.execute("INSERT INTO departamentos (nome_dp) VALUES ('Psicologia')")
    cursor.execute("INSERT INTO users (id_dp, nome_completo) VALUES (1, 'João Silva')")
    cursor.execute("INSERT INTO dependentes (id_user, nome) VALUES (1, 'Lucas Silva')") 

    cursor.execute("INSERT INTO users (id_dp, nome_completo) VALUES (1, 'Maria Souza')") 

    conn.commit()
    yield cursor
    conn.close()


def test_busca_colaboradores_controller(sqlite_cursor_with_users: sqlite3.Cursor):
    repo = InternalRepository(sqlite_cursor_with_users)
    usecase = ColaboradorUsecase(repo)
    controller = BuscaColaboradoresController(usecase)
    result: list[ColaboradorDTO] = controller.execute(departamento_id=1)

    assert isinstance(result, list)
    assert all(isinstance(user, ColaboradorDTO) for user in result)
    assert len(result) == 2

    joao: ColaboradorDTO = next(user for user in result if user.nome_completo == "João Silva")
    maria: ColaboradorDTO = next(user for user in result if user.nome_completo == "Maria Souza")

    assert joao.have_dependents is True
    assert maria.have_dependents is False
