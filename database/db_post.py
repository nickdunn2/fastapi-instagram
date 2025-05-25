from datetime import datetime
from typing import List
from sqlalchemy.orm import Session
from routers.schemas import PostBase
from database.models import DbPost

def get_all_posts(db: Session) -> List[DbPost]:
    """
    Get all posts
    """
    return db.query(DbPost).all()


def create_post(db: Session, request: PostBase):
    """
    Create a new post
    """
    new_post = DbPost(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        user_id=request.creator_id,
        timestamp=datetime.now()
    )

    db.add(new_post)
    db.commit()

    db.refresh(new_post)

    return new_post