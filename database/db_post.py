from datetime import datetime
from typing import List
from fastapi import HTTPException, status
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


def delete_post(id: int, db: Session, user_id: int):
    """
    Delete a post
    """
    post = db.query(DbPost).filter(DbPost.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    
    if post.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only post creator can delete posts")
    
    db.delete(post)
    db.commit()

    return "Post deleted successfully"