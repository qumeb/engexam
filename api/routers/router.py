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

@router.get("/", response_model=List[pyd.LessonSchema])
async def get_lessons(db: Session = Depends(get_db)):
    return db.query(models.Lesson).all()