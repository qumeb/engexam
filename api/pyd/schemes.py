from .base_models import *
from typing import List

# Схемы включают в себя ссылки на другие сущности для вложеного вывода
# их нужно выносить отдельно, чтобы избежать рекурсии в импорте

class LessonSchema(LessonBase):
    test: List[TestBase]