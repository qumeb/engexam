from sqlalchemy import Numeric, Table, Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from database import Base

# Вспомогательная таблица для связи многие ко многим у категорий и продуктов
product_category = Table('product_category', Base.metadata,
                         Column('product_id', ForeignKey('products.id'), primary_key=True),
                         Column('category_id', ForeignKey('categories.id'), primary_key=True)
                         )


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    description = Column(String(255), nullable=True)
    # Если использовать backref то необезательно указывать связи в обеих таблицах
    # products = relationship('Product', secondary="product_category", back_populates='categories')


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255), nullable=True)
    price = Column(Numeric, default=0)

    # backref автоматически делает связь в другой таблице
    categories = relationship("Category", secondary="product_category", backref="products")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    password = Column(String(255))

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    text = Column(Text(1000))
    isFinished = Column(Boolean, default=False)
    favorite = Column(Boolean, default=False)

    subject = relationship("Subject", backref="subjects")
    subject_id = Column(Integer, ForeignKey( "subjects.id"))

    level = relationship("Level", backref="levels")
    level_id = Column(Integer, ForeignKey("levels.id"))

    test = relationship("Test", backref="tests")
    test_id = Column(Integer, ForeignKey("tests.id"))

    # need to connect:
    # subject+, level+, tests+

class Test(Base):
    __tablename__ = "tests"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    isFinished = Column(Boolean, default=False)
    favorite = Column(Boolean, default=False)

    subject = relationship("Test", backref="tests")
    subject_id = Column(Integer, ForeignKey("subjects.id"))

    level = relationship("Level", backref="levels")
    level_id = Column(Integer, ForeignKey("levels.id"))

    questions = relationship("Question", backref="questions")
    questions_id = Column(Integer, ForeignKey("questions.id"))

    # need to connect
    # subject+, questions+

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question_text = Column(String(100))

    answer = relationship("Answer", backref="answers")
    answer_id = Column(Integer, ForeignKey("answers.id"))

    # need ro connect
    # answer+

class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)
    answer_text = Column(String(100))

#----------------- Tables Helpers------------------------#

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    subject_name = Column(String(100))

class Level(Base):
    __tablename__ = "levels"

    id = Column(Integer, primary_key=True)
    level_name = Column(String(100))