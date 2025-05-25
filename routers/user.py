from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from database import db_user
from routers.schemas import UserBase, UserDisplay

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    return db_user.create_user(db, request)