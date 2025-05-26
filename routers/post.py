import random
import shutil
import string
from typing import List
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from auth.oauth2 import get_current_user
from database.db import get_db
from database import db_post
from routers.schemas import PostBase, PostDisplay, UserAuth

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)

image_url_types = ["absolute", "relative"]

@router.get("", response_model=List[PostDisplay])
@router.get("/", response_model=List[PostDisplay])
def get_all_posts(db: Session = Depends(get_db)) -> List[PostDisplay]:
    """
    Get all posts
    """
    return db_post.get_all_posts(db)


@router.post("/", response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)) -> PostDisplay:
    """
    Create a new post
    """
    if request.image_url_type not in image_url_types:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid image url type")
    
    return db_post.create_post(db, request)


@router.post("/image-upload", status_code=status.HTTP_201_CREATED)
def upload_image(image: UploadFile = File(...)):
    """
    Upload an image for a post
    """
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(6))

    name, ext = image.filename.rsplit(".", 1)
    filename = f"{name}_{rand_str}.{ext}"
    path = f"images/{filename}"

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"filename": path}
