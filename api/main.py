from fastapi import FastAPI
import models
from database import SessionLocal, engine
from routers import api_router

# создание таблиц в БД из моделей
models.Base.metadata.create_all(bind=engine)

# Инициализация фастапи
app = FastAPI()

# подключение АпиРоутера (маршруты сущности)

app.include_router(api_router)


# тестовый комент 228
