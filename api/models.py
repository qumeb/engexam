from sqlalchemy import Numeric, Table, Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from database import Base

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    subject_name = Column(String(100))

    test_id = Column(Integer, ForeignKey("tests.id"))
    lesson_id = Column(Integer, ForeignKey("lessons.id"))

class Level(Base):
    __tablename__ = "levels"

    id = Column(Integer, primary_key=True)
    level_name = Column(String(100))

    test_id = Column(Integer, ForeignKey("tests.id"))
    lesson_id = Column(Integer, ForeignKey("lessons.id"))

class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)
    answer_text = Column(String(100))

    question_id = Column(Integer, ForeignKey("questions.id"))

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question_text = Column(String(100))

    answer = relationship(Answer)
    test_id = Column(Integer, ForeignKey("tests.id"))


class Test(Base):
    __tablename__ = "tests"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    isFinished = Column(Boolean, default=False)
    favorite = Column(Boolean, default=False)

    subject = relationship(Subject)
    level = relationship(Level)
    questions = relationship(Question)

    lesson_id = Column(Integer, ForeignKey("lessons.id"))

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    text = Column(Text(1000))
    isFinished = Column(Boolean, default=False)
    favorite = Column(Boolean, default=False)

    subject = relationship(Subject)
    level = relationship(Level)
    test = relationship(Test)