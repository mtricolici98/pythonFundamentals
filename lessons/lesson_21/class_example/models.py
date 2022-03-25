import hashlib
from datetime import datetime

from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):  # We extend the Base class
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(25))
    last_name = Column(String(25))
    user_name = Column(String(25), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    registration_date = Column(Date(), default=datetime.now)

    def __repr__(self):
        return f"User: [{self.user_name}, {self.first_name} {self.last_name}, {self.registration_date}]"

    def __str__(self):
        return repr(self)

    def set_password(self, password: str):
        self.password = self.hash_password_text(password)

    def add_post(self, title, message):
        post = Post(
            title=title,
            message=message,
        )
        self.posts.append(post)

    @classmethod
    def hash_password_text(cls, password):
        return hashlib.sha224(password.encode()).hexdigest()


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    post = relationship("Post", backref="comments")
    user = relationship("User", backref="comments")


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    message = Column(Text)
    created_by_id = Column(Integer, ForeignKey('user.id'))
    created_by = relationship("User", backref='posts')

    def __repr__(self):
        return f"Post(id={self.id}, created_by={self.created_by.user_name}, title={self.title}, message={self.message})"

    def __str__(self):
        return repr(self)


Base.metadata.create_all()
