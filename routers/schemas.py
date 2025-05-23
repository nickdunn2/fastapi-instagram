from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
  username: str
  email: str
  password: str

class UserDisplay(BaseModel):
  username: str
  email: str

  class Config():
    orm_mode = True

# For PostDisplay
class User(BaseModel):
  username: str

  class Config():
    orm_mode = True

class PostBase(BaseModel):
  image_url: str
  image_url_type: str # relative or absolute
  caption: str
  creator_id: int

class PostDisplay(BaseModel):
  id: int
  image_url: str
  image_url_type: str # relative or absolute
  caption: str
  timestamp: datetime
  user: User

  class Config():
    orm_mode = True