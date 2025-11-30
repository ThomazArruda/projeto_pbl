from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base
import datetime

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    sessions = relationship("Session", back_populates="patient")

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    duration_seconds = Column(Float)
    
    # Summary Metrics (JSON or simple stats)
    max_angle_esq = Column(Float)
    max_angle_dir = Column(Float)
    avg_emg_esq = Column(Float)
    avg_emg_dir = Column(Float)
    
    # Raw Data (stored as JSON string for simplicity in this prototype)
    raw_data_blob = Column(Text) 

    patient = relationship("Patient", back_populates="sessions")
