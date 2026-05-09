"""Energy data router."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime

from database import get_db
from models import EnergyRecord
from schemas import EnergyRecordCreate, EnergyRecordOut
from crud import create_energy_record, get_energy_tips
from auth import get_current_user

router = APIRouter()

@router.post("/records", response_model=EnergyRecordOut)
async def create_record(record_in: EnergyRecordCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return create_energy_record(db, record_in, current_user.id)

@router.get("/records", response_model=list[EnergyRecordOut])
async def read_records(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    records = db.query(EnergyRecord).filter(EnergyRecord.user_id == current_user.id).offset(skip).limit(limit).all()
    return records

@router.get("/tips", response_model=list)
async def read_tips(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_energy_tips(db, skip=skip, limit=limit)
