"""SQLAlchemy models for the Energy Monitor backend."""

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    records = relationship("EnergyRecord", back_populates="user")

class Building(Base):
    __tablename__ = "buildings"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    address = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    records = relationship("EnergyRecord", back_populates="building")

class EnergyRecord(Base):
    __tablename__ = "energy_records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    building_id = Column(Integer, ForeignKey("buildings.id"))
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    consumption_kwh = Column(Float, nullable=False)

    user = relationship("User", back_populates="records")
    building = relationship("Building", back_populates="records")

class EnergyTip(Base):
    __tablename__ = "energy_tips"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
