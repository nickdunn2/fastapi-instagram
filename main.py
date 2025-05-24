from fastapi import FastAPI
from database.db import engine
from database import models
from routers import user, post

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}


models.Base.metadata.create_all(bind=engine)