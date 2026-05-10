from sqlalchemy.orm import Session
from models import User, EnergyRecord
from schemas import EnergyRecordCreate, UserCreate
from database import get_db
from fastapi import Depends, HTTPException, status
from typing import List

# CRUD for users

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# CRUD for energy records

def get_energy_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(EnergyRecord).offset(skip).limit(limit).all()

def create_energy_record(db: Session, record: EnergyRecordCreate, user_id: int):
    db_record = EnergyRecord(**record.dict(), user_id=user_id)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
