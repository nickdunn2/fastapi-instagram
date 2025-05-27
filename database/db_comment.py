from datetime import datetime
from typing import List
from sqlalchemy.orm import Session
from database.models import DbComment
from routers.schemas import CommentBase

def get_comments_for_post(db: Session, post_id: int) -> List[DbComment]:
    """
    Get all comments for a post
    """
    return db.query(DbComment).filter(DbComment.post_id == post_id).all()


def create_comment(db: Session, request: CommentBase) -> DbComment:
    """
    Create a new comment on a post
    """
    new_comment = DbComment(
        text=request.text,
        username=request.username,
        post_id=request.post_id,
        timestamp=datetime.now()
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return new_comment