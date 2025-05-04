from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional, List


class CarBase(BaseModel):
    make: str
    model: str
    year: int
    daily_rate: float

    @validator('daily_rate')
    def validate_daily_rate(cls, v):
        if v <= 0:
            raise ValueError('Daily rate must be greater than zero')
        return v

    @validator('year')
    def validate_year(cls, v):
        current_year = datetime.now().year
        if v < 1900 or v > current_year + 1:
            raise ValueError(f'Year must be between 1900 and {current_year + 1}')
        return v


class CarCreate(CarBase):
    pass


class Car(CarBase):
    id: int
    available: bool

    class Config:
        orm_mode = True


class RentalBase(BaseModel):
    car_id: int
    user_name: str
    start_date: datetime
    end_date: datetime

    @validator('end_date')
    def validate_end_date(cls, v, values):
        if 'start_date' in values and v <= values['start_date']:
            raise ValueError('End date must be after start date')
        return v


class RentalCreate(RentalBase):
    pass


class Rental(RentalBase):
    id: int
    rental_date: datetime
    car: Optional[Car] = None

    class Config:
        orm_mode = True


class RentalResponse(BaseModel):
    id: int
    car_id: int
    user_name: str
    start_date: datetime
    end_date: datetime
    rental_date: datetime

    class Config:
        orm_mode = True


class ErrorResponse(BaseModel):
    detail: str
