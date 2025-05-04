from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime, timezone

# Use absolute imports to avoid circular dependencies
from app import models, schemas, database

router = APIRouter(
    prefix="/cars",
    tags=["cars"],
    responses={404: {"model": schemas.ErrorResponse}}
)


@router.post("/", response_model=schemas.Car, status_code=status.HTTP_201_CREATED)
def create_car(car: schemas.CarCreate, db: Session = Depends(database.get_db)):
    """
    Add a new car to the system
    """
    db_car = models.Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car


@router.get("/", response_model=List[schemas.Car])
def get_cars(
    available_only: bool = False,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(database.get_db)
):
    """
    Retrieve all cars, with option to filter only available ones
    """
    query = db.query(models.Car)
    if available_only:
        query = query.filter(models.Car.available == True)
    return query.offset(skip).limit(limit).all()


@router.get("/{car_id}", response_model=schemas.Car)
def get_car(car_id: int, db: Session = Depends(database.get_db)):
    """
    Retrieve details of a specific car
    """
    db_car = db.query(models.Car).filter(models.Car.id == car_id).first()
    if db_car is None:
        raise HTTPException(status_code=404, detail=f"Car with ID {car_id} not found")
    return db_car


@router.post("/{car_id}/rent", response_model=schemas.RentalResponse)
def rent_car(
    car_id: int,
    rental: schemas.RentalCreate,
    db: Session = Depends(database.get_db)
):
    """
    Rent a car for a specified period
    """
    # Get the car
    db_car = db.query(models.Car).filter(models.Car.id == car_id).first()
    if db_car is None:
        raise HTTPException(status_code=404, detail=f"Car with ID {car_id} not found")
    
    # Check if car is available
    if not db_car.available:
        raise HTTPException(
            status_code=400,
            detail=f"Car with ID {car_id} is currently unavailable"
        )
    
    # Check for overlapping rentals
    overlapping_rentals = db.query(models.Rental).filter(
        models.Rental.car_id == car_id,
        models.Rental.end_date >= rental.start_date,
        models.Rental.start_date <= rental.end_date
    ).first()
    
    if overlapping_rentals:
        raise HTTPException(
            status_code=400,
            detail=f"Car with ID {car_id} is already booked for the requested period"
        )
    
    # Create rental record
    db_rental = models.Rental(
        car_id=car_id,
        user_name=rental.user_name,
        start_date=rental.start_date,
        end_date=rental.end_date
    )
    
    # Get current UTC time with timezone info
    now = datetime.now(timezone.utc)
    
    # Convert rental start_date to UTC if it's not timezone-aware
    rental_start = rental.start_date
    if rental_start.tzinfo is None:
        # If the date is naive, assume it's in UTC
        rental_start = rental_start.replace(tzinfo=timezone.utc)
    
    # If the start date is today or in the past, mark the car as unavailable
    if rental_start <= now:
        db_car.available = False
    
    db.add(db_rental)
    db.commit()
    db.refresh(db_rental)
    
    return db_rental