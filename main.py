from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from auth import authentication
from database.db import engine
from database import models
from routers import user, post, comment
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)
app.include_router(authentication.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

models.Base.metadata.create_all(bind=engine)

app.mount("/images", StaticFiles(directory="images"), name="images")