from pydantic import BaseModel, Field


# файл с базовыми моделями

class LessonBase(BaseModel):
    title: str = Field(..., example='Название/Заголовок/Title')
    text: str = Field(..., example='Text')

    class Config:
        orm_mode = True

class TestBase(BaseModel):
    title: str = Field(..., example='Название/Заголовок/Title')
    text: str = Field(..., example='Text')

    class Config:
        orm_mode = True
