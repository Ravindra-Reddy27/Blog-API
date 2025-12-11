# app/routers/posts.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from typing import List, Optional
from sqlalchemy.orm import joinedload
from ..schemas import PostOut

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/", response_model=schemas.PostOut, status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    # check if author exists
    author = db.query(models.Author).filter(models.Author.id == post.author_id).first()
    if not author:
        raise HTTPException(status_code=400, detail="Author does not exist")

    new_post = models.Post(
        title=post.title,
        content=post.content,
        author_id=post.author_id
    )
    db.add(new_post)
    db.commit()
    # eager load author for response
    db.refresh(new_post)
    db.refresh(author)
    new_post.author = author
    return new_post

@router.get("/", response_model=List[schemas.PostOut])
def get_posts(
    author_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Post).options(joinedload(models.Post.author))
    
    if author_id is not None:
        query = query.filter(models.Post.author_id == author_id)

    posts = query.all()
    return posts

@router.get("/{post_id}", response_model=schemas.PostOut)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = (
        db.query(models.Post)
        .options(joinedload(models.Post.author))
        .filter(models.Post.id == post_id)
        .first()
    )
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.put("/{post_id}", response_model=schemas.PostOut)
def update_post(post_id: int, update_data: schemas.PostUpdate, db: Session = Depends(get_db)):
    post = db.query(models.Post).options(joinedload(models.Post.author)).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if update_data.title is not None:
        post.title = update_data.title
    if update_data.content is not None:
        post.content = update_data.content

    db.commit()
    db.refresh(post)
    return post

@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    db.delete(post)
    db.commit()
    return None