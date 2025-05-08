from fastapi import FastAPI
from database.db import engine
from database import models

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


models.Base.metadata.create_all(bind=engine)