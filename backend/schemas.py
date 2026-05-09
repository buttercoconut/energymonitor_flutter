"""Pydantic schemas for request/response models."""

from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

# User schemas
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserOut(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

# Energy record schemas
class EnergyRecordBase(BaseModel):
    building_id: int
    timestamp: datetime
    consumption_kwh: float

class EnergyRecordCreate(EnergyRecordBase):
    pass

class EnergyRecordOut(EnergyRecordBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

# Energy tip schema
class EnergyTipOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
