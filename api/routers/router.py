from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
from database import get_db
import pyd
from auth import AuthHandler

router = APIRouter(
    prefix="/api",
    tags=["api"],
)

@router.get("/lesson", response_model=List[pyd.LessonSchema])
async def get_lessons(db: Session = Depends(get_db)):
    return db.query(models.Lesson).all()

@router.get("/test", response_model=List[pyd.TestSchema])
async def get_tests(db: Session = Depends(get_db)):
    return db.query(models.Test).all()

@router.get("/test/{test_id}", response_model=pyd.TestSchema)
async def get_test(test_id:int, db: Session = Depends(get_db)):
    return db.query(models.Test).filter(models.Test.id == test_id).first()

@router.get("/lesson/{lesson_id}", response_model=pyd.LessonSchema)
async def get_lesson(lesson_id:int, db: Session = Depends(get_db)):
    return db.query(models.Lesson).filter(models.Lesson.id == lesson_id).first()

@router.post("/test/{test_id}")
async def post_test(test, test_id, db: Session = Depends(get_db)):
       test_db = db.query(models.Test).filter(models.Test.id == test_id).first()
       test_db.isFinished = test.isFinished
       test.favorite = test.favorite