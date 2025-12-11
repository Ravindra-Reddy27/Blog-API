# app/main.py
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import authors, posts

# create tables (for simple dev usage; in production use Alembic migrations)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog API")

app.include_router(authors.router)
app.include_router(posts.router)


@app.get("/")
def root():
    return {"message": "Blog API is running. Go to http://127.0.0.1:8000/docs for the API docs or Swagger UI."}