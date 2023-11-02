from pydantic import BaseModel, Field
from typing import List


# тут модели которые используются при создании/редактировании сущностей


class CreateLesson(BaseModel):
    title: str = Field(..., example='Название/Заголовок/Title')
    text: str = Field(..., example='Text')

    class Config:
        orm_mode = True
