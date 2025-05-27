from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from database.db import Base
from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    posts = relationship('DbPost', back_populates='user')
    
class DbPost(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String, nullable=False)
    image_url_type = Column(String, nullable=False)
    caption = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    user = relationship('DbUser', back_populates='posts')
    comments = relationship('DbComment', back_populates='post')

class DbComment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    username = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

    post = relationship('DbPost', back_populates='comments')