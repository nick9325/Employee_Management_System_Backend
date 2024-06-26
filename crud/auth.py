
from sqlalchemy.orm import Session
from models.user import User
from schemas.auth import UserCreate
from core.security import get_password_hash, verify_password, get_current_user
from fastapi import Depends
from dependency.dependency import get_db

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def get_user_profile(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return current_user





