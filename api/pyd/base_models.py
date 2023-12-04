from pydantic import BaseModel, Field


# файл с базовыми моделями


class LevelBase(BaseModel):
    id: int = Field(..., gt=0, example=1)
    level_name: str = Field(None)

class SubjectBase(BaseModel):
    id: int = Field(..., gt=0, example=1)
    subject_name: str = Field(None)


class AnswerBase(BaseModel):
    id: int = Field(..., gt=0, example=1)
    answer_text: str = Field(None)

class QuestionBase(BaseModel):
    id: int = Field(..., gt=0, example=1)
    answer: AnswerBase

class TestBase(BaseModel):
    id: int = Field(..., gt=0, example=1)
    title: str = Field(None, example='Название/Заголовок/Title')
    isFinished: bool = Field(False)
    favorite: bool = Field(False)
    questions: QuestionBase
    level: LevelBase
    subject: SubjectBase

    class Config:
        orm_mode = True

class QuestionBase(BaseModel):
    question_text: str = Field(..., example='Текст вопроса')

    class Config:
        orm_mode = True


class Answer(BaseModel):
    answer_text: str = Field(..., example='Текст ответа')

    class Config:
        orm_mode = True

class LessonBase(BaseModel):
    id: int = Field(..., gt=0, example=1)
    title: str = Field(None, example='Название/Заголовок/Title')
    text: str = Field(None, example='Text')
    isFinished: bool = Field(False)
    favorite: bool = Field(False)
    test: TestBase
    subject: SubjectBase
    level: LevelBase

    class Config:
        orm_mode = True