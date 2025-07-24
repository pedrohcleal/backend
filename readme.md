# 📦 Internal API – FastAPI + Clean Architecture

API construída com FastAPI seguindo princípios de Clean Architecture e injeção de dependência manual, com persistência em SQLite.

## 🔧 Estrutura do Projeto

```
.
├── app
│   ├── config/                  # Conexão com banco SQLite
│   ├── controller/              # Camada de controller (entrada)
│   ├── dependency_injection/    # Injeção de dependências
│   ├── dtos/                    # Data Transfer Objects
│   ├── repository/              # Acesso a dados e queries SQL
│   │   └── queries/             # Arquivos .sql puros
│   ├── route/                   # Rotas da API
│   └── usecase/                 # Regras de negócio
├── db.sqlite3                   # Banco de dados local
├── main.py                      # Ponto de entrada da aplicação
├── pyproject.toml               # Dependências (usando uv ou poetry)
├── test.md                      # Anotações de testes manuais
├── tests/                       # Testes automatizados (pytest)
└── uv.lock                      # Lockfile do `uv`
```

## 🚀 Como Executar

### ✅ Usando `uv` (recomendado)

1. Instale o [uv](https://github.com/astral-sh/uv):

```bash
pip install uv
```

2. Instale as dependências:

```bash
uv pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
uvicorn main:app --reload
```

---

### 🧪 Usando `venv` (alternativa)

1. Crie o ambiente virtual:

```bash
python -m venv .venv
```

2. Ative o ambiente:

* Windows:

```bash
.venv\Scripts\activate
```

* Linux/macOS:

```bash
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Rode a aplicação:

```bash
uvicorn main:app --reload
```

---

## 🧪 Rodando os Testes

Utilize o `pytest`:

```bash
pytest tests/
```

---

## 📌 Rotas Disponíveis

| Método | Rota                          | Descrição                    |
| ------ | ----------------------------- | ---------------------------- |
| GET    | `/api/internal/departamentos` | Lista os departamentos       |
| GET    | `/api/internal/colaboradores` | Lista os colaboradores       |
| GET    | `/api/healthcheck`            | Verifica se a API está no ar |

---

### 🐳 Comandos Makefile

```bash
# 🔧 Build da imagem Docker
make build

# ▶️ Rodar o container
make run

# ♻️ Rebuild completo (remove e recria a imagem)
make rebuild

# 🛠️ Rodar em modo desenvolvimento (volume local)
make dev

# 🧹 Remover container e imagem
make clean
```

> Obs: Todos os comandos usam `sudo`. Se não precisar de `sudo` no seu ambiente, remova dos comandos no `Makefile`.


## 🏗️ Padrões Utilizados

* Clean Architecture (camadas desacopladas)
* SQLite com queries puras
* FastAPI com tipagem forte
* Injeção de dependência manual

---

## 📋 Requisitos

* Python 3.11+
* FastAPI
* Uvicorn
* Pytest
