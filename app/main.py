from fastapi import FastAPI
from app.router import router as router_test

def create_app() -> FastAPI:
    app = FastAPI(
        title='Тестовое задание WhyNot'
    )
    app.include_router(router_test)
    return app

