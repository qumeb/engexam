from .base_models import *
from typing import List

# Схемы включают в себя ссылки на другие сущности для вложеного вывода
# их нужно выносить отдельно, чтобы избежать рекурсии в импорте

class LessonSchema(LessonBase):
    test: List[TestBase]
    subject: List[SubjectBase]
    level: List[LevelBase]

class TestSchema(TestBase):
    questions: List[QuestionBase]
    level: List[LevelBase]
    subject: List[SubjectBase]
class LevelSchema(LevelBase):
    name: str

class SubjectSchema(SubjectBase):
    name: str


class AnswerSchema(AnswerBase):
    text: str

class QuestionSchema(QuestionBase):
    answers: List[AnswerBase]