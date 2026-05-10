from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from crud import get_energy_records, create_energy_record
from schemas import EnergyRecord, EnergyRecordCreate
from database import get_db

router = APIRouter()

@router.get("/records", response_model=list[EnergyRecord])
async def read_records(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    records = get_energy_records(db, skip=skip, limit=limit)
    return records

@router.post("/records", response_model=EnergyRecord)
async def create_record(record: EnergyRecordCreate, db: Session = Depends(get_db)):
    # For demo, assume user_id=1
    db_record = create_energy_record(db, record, user_id=1)
    return db_record
