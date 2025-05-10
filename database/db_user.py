
from sqlalchemy.orm import Session
from database.models import DbUser
from routers.schemas import UserBase


def create_user(db: Session, req: UserBase) -> DbUser:
    """
    Create a new user in the database.
    """
    db_user = DbUser(
        username=req.username,
        email=req.email,
        password=req.password, # TODO: Hash the password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user