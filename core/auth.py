from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from typing import Optional
from pydantic import BaseModel
from database import SessionLocal
from models.user import User as DBUser
from .token import create_access_token
from sqlalchemy.orm import Session

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Password hashing settings
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Pydantic models
class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str
    email: Optional[str] = None

class UserCreateRequest(BaseModel):
    username: str
    email: str
    password: str

# Authentication
@router.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(DBUser).filter(DBUser.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# User Registration
@router.post("/register", response_model=User)
def register_user(user: UserCreateRequest, db: Session = Depends(get_db)):
    db_user = DBUser(username=user.username, email=user.email, hashed_password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_password_hash(password: str):
    return pwd_context.hash(password)
