from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from auth import oauth2
from database.db import get_db
from database import db_user
from sqlalchemy.orm import Session
from database.hashing import Hash


router = APIRouter(
  tags=["authentication"]
)


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm), db: Session = Depends(get_db)):
  user = db_user.get_user_by_username(db, request.username)

  if not Hash.verify(user.password, request.password):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
  
  access_token = oauth2.create_access_token(data={"username": user.username})

  return {
    "access_token": access_token,
    "token_type": "bearer",
    "user_id": user.id,
    "username": user.username
  }