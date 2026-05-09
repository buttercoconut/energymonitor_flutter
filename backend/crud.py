"""CRUD operations for the backend."""

from sqlalchemy.orm import Session
from models import User, Building, EnergyRecord, EnergyTip
from schemas import UserCreate, EnergyRecordCreate
from auth import get_password_hash
from datetime import datetime

# User CRUD

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user_in: UserCreate):
    hashed_pw = get_password_hash(user_in.password)
    db_user = User(email=user_in.email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Energy record CRUD

def create_energy_record(db: Session, record_in: EnergyRecordCreate, user_id: int):
    db_record = EnergyRecord(
        user_id=user_id,
        building_id=record_in.building_id,
        timestamp=record_in.timestamp,
        consumption_kwh=record_in.consumption_kwh,
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

# Energy tips

def get_energy_tips(db: Session, skip: int = 0, limit: int = 10):
    return db.query(EnergyTip).offset(skip).limit(limit).all()
