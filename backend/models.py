from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Integer, default=1)
    # relationships
    energy_records = relationship("EnergyRecord", back_populates="user")

class EnergyRecord(Base):
    __tablename__ = "energy_records"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    timestamp = Column(DateTime, nullable=False)
    consumption_kwh = Column(Float, nullable=False)
    # relationships
    user = relationship("User", back_populates="energy_records")
