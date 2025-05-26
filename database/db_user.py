from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from database.models import DbUser
from routers.schemas import UserBase
from database.hashing import Hash


def create_user(db: Session, req: UserBase) -> DbUser:
    """
    Create a new user in the database.
    """
    db_user = DbUser(
        username=req.username,
        email=req.email,
        password=Hash.bcrypt(req.password),
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user_by_username(db: Session, username: str) -> DbUser:
    """
    Get a user by username
    """
    user = db.query(DbUser).filter(DbUser.username == username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid credentials"
        )
    
    return user