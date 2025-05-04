from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers directly with absolute imports
# Since you're running uvicorn from the backend directory, use app.routers
from app.routers.cars import router as cars_router
from app.routers.rentals import router as rentals_router

app = FastAPI(
    title="Car Rental API",
    description="API for managing car rentals",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers with explicit names
app.include_router(cars_router)
app.include_router(rentals_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Car Rental API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)