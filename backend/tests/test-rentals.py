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

def test_cancel_rental():
    # Create a car
    car_response = client.post(
        "/cars/",
        json={"make": "Honda", "model": "Accord", "year": 2021, "daily_rate": 45.0}
    )
    car_id = car_response.json()["id"]
    
    # Rent the car
    start_date = datetime.utcnow() + timedelta(days=1)
    end_date = start_date + timedelta(days=3)
    
    rental_response = client.post(
        f"/cars/{car_id}/rent",
        json={
            "car_id": car_id,
            "user_name": "John Doe",
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat()
        }
    )
    
    rental_id = rental_response.json()["id"]
    
    # Cancel the rental
    response = client.delete(f"/rentals/{rental_id}")
    assert response.status_code == 204
    
    # Verify that the car is available again
    car_response = client.get(f"/cars/{car_id}")
    assert car_response.json()["available"] == True

def test_cancel_nonexistent_rental():
    response = client.delete("/rentals/9999")
    assert response.status_code == 404

def test_get_rentals():
    # Create a car
    car_response = client.post(
        "/cars/",
        json={"make": "Mazda", "model": "CX-5", "year": 2021, "daily_rate": 55.0}
    )
    car_id = car_response.json()["id"]
    
    # Rent the car
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
    
    # Get all rentals
    response = client.get("/rentals/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0]["car_id"] == car_id
    assert data[0]["user_name"] == "John Doe"

def test_get_rental():
    # Create a car
    car_response = client.post(
        "/cars/",
        json={"make": "Subaru", "model": "Outback", "year": 2020, "daily_rate": 60.0}
    )
    car_id = car_response.json()["id"]
    
    # Rent the car
    start_date = datetime.utcnow() + timedelta(days=1)
    end_date = start_date + timedelta(days=3)
    
    rental_response = client.post(
        f"/cars/{car_id}/rent",
        json={
            "car_id": car_id,
            "user_name": "Jane Smith",
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat()
        }
    )
    
    rental_id = rental_response.json()["id"]
    
    # Get the specific rental
    response = client.get(f"/rentals/{rental_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == rental_id
    assert data["car_id"] == car_id
    assert data["user_name"] == "Jane Smith"

def test_get_nonexistent_rental():
    response = client.get("/rentals/9999")
    assert response.status_code == 404

def test_cancel_expired_rental():
    # Create a car
    car_response = client.post(
        "/cars/",
        json={"make": "Audi", "model": "A4", "year": 2021, "daily_rate": 75.0}
    )
    car_id = car_response.json()["id"]
    
    # Create a rental with past end date
    db = TestingSessionLocal()
    start_date = datetime.utcnow() - timedelta(days=5)
    end_date = datetime.utcnow() - timedelta(days=2)
    
    test_rental = models.Rental(
        car_id=car_id,
        user_name="Past User",
        start_date=start_date,
        end_date=end_date
    )
    db.add(test_rental)
    db.commit()
    db.refresh(test_rental)
    
    # Try to cancel the expired rental
    response = client.delete(f"/rentals/{test_rental.id}")
    assert response.status_code == 400
    assert "already ended" in response.json()["detail"]