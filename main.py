import warnings
from app.config.sqlite_conn import create_tables
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.route import healthcheck, internal
from app.config.sqlite_conn import create_sqlite_conn

warnings.filterwarnings("ignore")

api = FastAPI(swagger_ui_parameters={"displayRequestDuration": True})
api.include_router(healthcheck.router)
api.include_router(internal.router)
api.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    with create_sqlite_conn() as conn:
        create_tables(conn)
    uvicorn.run(app=api, host="0.0.0.0", port=8000)
