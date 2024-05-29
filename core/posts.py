from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
from database import SessionLocal
from models.post import Post as DBPost, PostCreate, PostUpdate

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models
class Post(BaseModel):
    id: int
    title: str
    content: str

class PostCreateRequest(BaseModel):
    title: str
    content: str

class PostUpdateRequest(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

# CRUD Operations
@router.post("/posts/", response_model=Post)
def create_post(post: PostCreateRequest, db: Session = Depends(get_db)):
    db_post = DBPost(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.get("/posts/", response_model=List[Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    posts = db.query(DBPost).offset(skip).limit(limit).all()
    return posts

@router.get("/posts/{post_id}", response_model=Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(DBPost).filter(DBPost.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@router.put("/posts/{post_id}", response_model=Post)
def update_post(post_id: int, post: PostUpdateRequest, db: Session = Depends(get_db)):
    db_post = db.query(DBPost).filter(DBPost.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.title:
        db_post.title = post.title
    if post.content:
        db_post.content = post.content
    db.commit()
    db.refresh(db_post)
    return db_post

@router.delete("/posts/{post_id}", response_model=Post)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(DBPost).filter(DBPost.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(db_post)
    db.commit()
    return db_post
