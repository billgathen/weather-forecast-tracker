from fastapi import Depends, APIRouter
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from app.database import get_db

router = APIRouter()

@router.get("/health")
def health():
  return { "status": "ok" }

@router.get("/dbhealth")
def db_health(db: Session = Depends(get_db)):
  try:
    db.execute(text("SELECT 1"))
    return { "db status": "ok"}
  except OperationalError:
    return { "error": "Database is unavailable"}