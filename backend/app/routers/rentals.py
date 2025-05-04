from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from typing import List

# Use absolute imports to avoid circular dependencies
from app import models, schemas, database

router = APIRouter(
    prefix="/rentals",
    tags=["rentals"],
    responses={404: {"model": schemas.ErrorResponse}}
)


@router.get("/", response_model=List[schemas.RentalResponse])
def get_rentals(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(database.get_db)
):
    """
    Retrieve all rentals
    """
    return db.query(models.Rental).offset(skip).limit(limit).all()


@router.get("/{rental_id}", response_model=schemas.RentalResponse)
def get_rental(rental_id: int, db: Session = Depends(database.get_db)):
    """
    Retrieve a specific rental
    """
    db_rental = db.query(models.Rental).filter(models.Rental.id == rental_id).first()
    if db_rental is None:
        raise HTTPException(status_code=404, detail=f"Rental with ID {rental_id} not found")
    return db_rental


@router.delete("/{rental_id}", status_code=status.HTTP_204_NO_CONTENT)
def cancel_rental(rental_id: int, db: Session = Depends(database.get_db)):
    """
    Cancel an active rental
    """
    # Get the rental
    db_rental = db.query(models.Rental).filter(models.Rental.id == rental_id).first()
    
    if db_rental is None:
        raise HTTPException(status_code=404, detail=f"Rental with ID {rental_id} not found")
    
    # Get the associated car
    db_car = db.query(models.Car).filter(models.Car.id == db_rental.car_id).first()
    
    # Get current UTC time with timezone info
    now = datetime.now(timezone.utc)
    
    # Convert rental end_date to UTC if it's not timezone-aware
    rental_end = db_rental.end_date
    if rental_end.tzinfo is None:
        # If the date is naive, assume it's in UTC
        rental_end = rental_end.replace(tzinfo=timezone.utc)
    
    # Check if it's an active rental (end date in the future)
    if rental_end < now:
        raise HTTPException(
            status_code=400,
            detail=f"Rental with ID {rental_id} has already ended and cannot be canceled"
        )
    
    # If the car was marked as unavailable and the rental is canceled, 
    # check if there are other active rentals for this car
    if not db_car.available:
        # Check for other active rentals for this car
        other_active_rentals = db.query(models.Rental).filter(
            models.Rental.car_id == db_car.id,
            models.Rental.id != rental_id,
            models.Rental.end_date >= now
        ).first()
        
        # If no other active rentals, mark the car as available
        if not other_active_rentals:
            db_car.available = True
    
    # Delete the rental
    db.delete(db_rental)
    db.commit()
    
    return None