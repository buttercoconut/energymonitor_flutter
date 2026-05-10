from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class EnergyRecordBase(BaseModel):
    timestamp: datetime
    consumption_kwh: float

class EnergyRecordCreate(EnergyRecordBase):
    pass

class EnergyRecord(EnergyRecordBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
