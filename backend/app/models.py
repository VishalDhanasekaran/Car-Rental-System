from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime, CheckConstraint
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    daily_rate = Column(Float, nullable=False)
    available = Column(Boolean, default=True, nullable=False)

    # Relationship with Rental model
    rentals = relationship("Rental", back_populates="car", cascade="all, delete-orphan")
    
    # Add a check constraint to ensure daily_rate is positive
    __table_args__ = (
        CheckConstraint('daily_rate > 0', name='check_positive_daily_rate'),
    )


class Rental(Base):
    __tablename__ = "rentals"

    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey("cars.id", ondelete="CASCADE"), nullable=False)
    user_name = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    rental_date = Column(DateTime, default=datetime.utcnow)

    # Relationship with Car model
    car = relationship("Car", back_populates="rentals")
