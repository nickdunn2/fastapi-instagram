
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