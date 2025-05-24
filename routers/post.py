from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.db import get_db
from database import db_post
from routers.schemas import PostBase, PostDisplay

router = APIRouter(
    prefix="/post",
    tags=["posts"]
)

image_url_types = ["absolute", "relative"]

@router.post("/", response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db)) -> PostDisplay:
    if request.image_url_type not in image_url_types:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid image url type")
    
    return db_post.create_post(db, request)