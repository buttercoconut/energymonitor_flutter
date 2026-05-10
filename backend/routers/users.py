from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from crud import get_user, create_user, get_user_by_email
from schemas import User, UserCreate
from database import get_db

router = APIRouter()

@router.post("/register", response_model=User)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)

@router.get("/me", response_model=User)
async def read_me(user: User = Depends(get_user)):
    return user
