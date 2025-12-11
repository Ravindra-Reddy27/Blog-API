# app/routers/authors.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/authors", tags=["Authors"])

@router.post("/", response_model=schemas.AuthorOut, status_code=status.HTTP_201_CREATED)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    # check if email already exists
    existing = db.query(models.Author).filter(models.Author.email == author.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_author = models.Author(name=author.name, email=author.email)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

@router.get("/", response_model=List[schemas.AuthorOut])
def get_authors(db: Session = Depends(get_db)):
    authors = db.query(models.Author).all()
    return authors

@router.get("/{author_id}", response_model=schemas.AuthorOut)
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.put("/{author_id}", response_model=schemas.AuthorOut)
def update_author(author_id: int, update_data: schemas.AuthorUpdate, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    if update_data.name is not None:
        author.name = update_data.name
    if update_data.email is not None:
        # you may also re-check email uniqueness here
        author.email = update_data.email

    db.commit()
    db.refresh(author)
    return author

@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    db.delete(author)   # posts will be deleted via cascade
    db.commit()
    return None
