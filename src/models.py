from sqlalchemy import Table
import os
import sys


from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()

message_user = Table(
    'message_user',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('message_id', Integer, ForeignKey('message.id'))
)

message_story=Table('message_story',Base.metadata,
                    Column('story_id',Integer,ForeignKey('stories.id')),
                    Column('message_id',Integer,ForeignKey('message.id'))
                    )


message_post=Table('message_post',Base.metadata,
                   Column('post_id',Integer,ForeignKey('post.id')),
                   Column('message_id',Integer,ForeignKey('message.id'))
                   )

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)
    email=Column(String(250), nullable=False)
    state=Column(String(250), nullable=False)

    message=relationship('message_user',secondary=message_user, 
                          backref='users')
    

class Like(Base):
    __tablename__= 'like'
    id=Column(Integer,primary_key=True)
    like_count=Column(Integer)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    like_id=Column(Integer,ForeignKey('like.id'))
    like=relationship(Like)
    message=relationship('message_post',secondary=message_post,backref='post')




class Comment(Base):
    __tablename__='comment'
    id=Column(Integer, primary_key=True)
    text_comment=(String(250))

    user_id=Column(Integer,ForeignKey('user.id'))
    user=relationship(User)
    post_id=Column(Integer, ForeignKey('post.id'))
    post=relationship(Post)
    
    
class Stories(Base):
    __tablename__='stories'
    id=Column(Integer,primary_key=True)
    text_story=(String(250))    

    user_id=Column(Integer,ForeignKey('user.id'))
    user=relationship(User)

    message=relationship('message_story',secondary=message_story,
                         backref='stories')


class Message(Base):
    __tablename__='message'
    id=Column(Integer,primary_key=True)
    text=Column(String(300))





class Media(Base):
    __tablename__='media'
    id=Column(Integer,primary_key=True)
    type=Column(String(300))

    post_id=Column(Integer,ForeignKey('post.id'))
    post=relationship(Post)




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
