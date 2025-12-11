# app/models.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    # one author -> many posts
    posts = relationship(
        "Post",
        back_populates="author",
        cascade="all, delete-orphan"  # cascade delete in ORM
    )

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)

    author_id = Column(
        Integer,
        ForeignKey("authors.id", ondelete="CASCADE"),  # FK with cascade
        nullable=False
    )

    # many posts -> one author
    author = relationship("Author", back_populates="posts")
