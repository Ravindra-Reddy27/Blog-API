# app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import List, Optional

# ---------- AUTHOR ----------

class AuthorBase(BaseModel):
    name: str
    email: EmailStr

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

class AuthorOut(AuthorBase):
    id: int

    class Config:
        orm_mode = True   # so we can return SQLAlchemy objects directly


# ---------- POST ----------

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    author_id: int

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class PostAuthorOut(AuthorOut):
    """Used when we want author nested inside post."""
    pass

class PostOut(PostBase):
    id: int
    author: PostAuthorOut   # nested author

    class Config:
        orm_mode = True
