import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class user(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    signup_date = Column(String(250), nullable=False)
    followers = relationship('Follower')

class post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    date = relationship("Post_Type")
    comment = relationship('Comment')

class post_Type(Base):
    __tablename__ = 'post_type'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    post_type = Column(String(250), nullable=False)

class likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"))
    
class comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    created_by_user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    receiving_by_user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    comment = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    date = Column(String(250), nullable=False)
    
class follower(Base) :
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    following_user_id = Column(Integer, ForeignKey("user.id"))
    followed_user_id = Column(Integer, ForeignKey("user.id"))
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
