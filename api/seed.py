# вставка начальных данных
from sqlalchemy.orm import Session
from database import engine
import models

models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

with Session(bind=engine) as session:
    lesson = models.Lesson(title='Urok1', text='text2')

    session.add_all([lesson])
    session.commit()

