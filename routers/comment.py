from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from database import db_comment
from routers.schemas import CommentBase, UserAuth, Comment
from auth.oauth2 import get_current_user


router = APIRouter(
    prefix="/comments",
    tags=["comments"]
)

@router.get("/{post_id}", response_model=List[Comment])
def get_comments(post_id: int, db: Session = Depends(get_db)) -> List[Comment]:
    """
    Get all comments for a post
    """
    return db_comment.get_comments_for_post(db, post_id)


@router.post("", response_model=Comment)
def create_comment(
    request: CommentBase,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user)
) -> Comment:
    """
    Create a new comment on a post
    """
    return db_comment.create_comment(db, request)