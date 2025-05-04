from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

from app.main import app
from app.database import Base, get_db
from app import models

# Use in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency for testing
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    
    # Add test data
    db = TestingSessionLocal()
    test_car = models.Car(
        make="Toyota",
        model="Camry",
        year=2022,
        daily_rate=50.0,
        available=True
    )
    db.add(test_car)
    db.commit()
    
    yield
    
    # Drop all tables after the test
    Base.metadata.drop_all(bind=engine)

def test_create_car():
    response = client.post(
        "/cars/",
        json={"make": "Honda", "model": "Civic", "year": 2021, "daily_rate": 45.0}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["make"] == "Honda"
    assert data["model"] == "Civic"
    assert data["year"] == 2021
    assert data["daily_rate"] == 45.0
    assert data["available"] == True
    assert "id" in data

def test_get_cars():
    response = client.get("/cars/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0]["make"] == "Toyota"

def test_get_car():
    # First, create a new car to test with
    create_response = client.post(
        "/cars/",
        json={"make": "Ford", "model": "Mustang", "year": 2023, "daily_rate": 70.0}
    )
    car_id = create_response.json()["id"]
    
    response = client.get(f"/cars/{car_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["make"] == "Ford"
    assert data["model"] == "Mustang"

def test_get_nonexistent_car():
    response = client.get("/cars/9999")
    assert response.status_code == 404

def test_rent_car():
    # Create a car first
    car_response = client.post(
        "/cars/",
        json={"make": "Nissan", "model": "Altima", "year": 2020, "daily_rate": 40.0}
    )
    car_id = car_response.json()["id"]
    
    # Rent the car
    start_date = datetime.utcnow() + timedelta(days=1)
    end_date = start_date + timedelta(days=3)
    
    response = client.post(
        f"/cars/{car_id}/rent",
        json={
            "car_id": car_id,
            "user_name": "John Doe",
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat()
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["car_id"] == car_id
    assert data["user_name"] == "John Doe"

def test_rent_nonexistent_car():
    start_date = datetime.utcnow() + timedelta(days=1)
    end_date = start_date + timedelta(days=3)
    
    response = client.post(
        "/cars/9999/rent",
        json={
            "car_id": 9999,
            "user_name": "John Doe",
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat()
        }
    )
    
    assert response.status_code == 404

def test_rent_already_rented_car():
    # Create a car first
    car_response = client.post(
        "/cars/",
        json={"make": "BMW", "model": "X5", "year": 2021, "daily_rate": 80.0}
    )
    car_id = car_response.json()["id"]
    
    # Rent the car for the first time
    start_date = datetime.utcnow() + timedelta(days=1)
    end_date = start_date + timedelta(days=3)
    
    client.post(
        f"/cars/{car_id}/rent",
        json={
            "car_id": car_id,
            "user_name": "John Doe",
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat()
        }
    )
    
    # Try to rent the same car for overlapping dates
    overlap_start = start_date + timedelta(days=1)
    overlap_end = overlap_start + timedelta(days=3)
    
    response = client.post(
        f"/cars/{car_id}/rent",
        json={
            "car_id": car_id,
            "user_name": "Jane Smith",
            "start_date": overlap_start.isoformat(),
            "end_date": overlap_end.isoformat()
        }
    )
    
    assert response.status_code == 400