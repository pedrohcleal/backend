![Python](https://img.shields.io/badge/python-3.12-3670A0?style=flat&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/fastapi-0.116.1-009688?style=flat&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/pydantic-2.11.7-0A66C2?style=flat&logo=pydantic&logoColor=white)
![Pytest](https://img.shields.io/badge/pytest-8.4.1-0A9EDC?style=flat&logo=pytest&logoColor=white)
![Uvicorn](https://img.shields.io/badge/uvicorn-0.35.0-121212?style=flat&logo=uvicorn&logoColor=white)
![Swagger](https://img.shields.io/badge/swagger-UI-85EA2D?style=flat&logo=swagger&logoColor=black)

# ACMEVita API

API construída com FastAPI seguindo princípios de Clean Architecture e injeção de dependência, com persistência em SQLite.

## Estrutura do Projeto

```
├── Dockerfile                  # Container Docker para o projeto
├── Makefile                    # Comandos automatizados (build, run, dev, etc.)
├── app
│   ├── config/                 # Conexão com banco SQLite
│   ├── controller/             # Camada de entrada (request handlers)
│   ├── dependency_injection/   # Injeção de dependências (para controllers)
│   ├── dtos/                   # Data Transfer Objects (entradas/saídas da API)
│   ├── repository/             # Acesso a dados e execução de queries
│   ├── route/                  # Definição das rotas da API
│   └── usecase/                # Regras de negócio (application layer)
├── db.sqlite3                  # Banco de dados local SQLite
├── main.py                     # Ponto de entrada da aplicação FastAPI
├── pyproject.toml              # Arquivo de dependências (gerenciado com `uv` ou `poetry`)
├── readme.md                   # Documentação do projeto
└── uv.lock                     # Lockfile do `uv`
└── requirements.tx             # Dependências
```

## Como preparar ambiente

### Usando `uv` (recomendado)

1. Instale o uv em https://github.com/astral-sh/uv

```bash
uv venv
source .venv/bin/activate
uv sync
uv run main.py
```

2. Ou utilize o padrao venv
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## Rotas Disponíveis

| Método | Rota                          | Descrição                    |
| ------ | ----------------------------- | ---------------------------- |
| GET    | `/api/healthcheck`            | Verifica se a API está no ar |
| GET    | `/api/internal/departamentos` | Lista os departamentos       |
| GET    | `/api/internal/colaboradores` | Lista os colaboradores       |

> Consultar documentação gerada em `/docs` http://localhost:8000/docs

## Rodando os Testes

Utilize o `pytest`:

```bash
pytest .
```

### Comandos Makefile

```bash
# 🔧 Build da imagem Docker
make build

# ▶️ Rodar o container
make run

# ♻️ Rebuild completo (remove e recria a imagem)
make rebuild

# 🧹 Remover container e imagem
make clean
```

> Obs: Todos os comandos usam `sudo`. Se não precisar de `sudo` no seu ambiente, remova dos comandos no `Makefile`.


## Padrões Utilizados

* Clean Architecture (camadas desacopladas)
* SQLite com queries puras
* FastAPI com tipagem forte
* Injeção de dependência manual
