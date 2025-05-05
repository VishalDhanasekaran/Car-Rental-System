#!/bin/bash

echo "🚀 Starting Car Rental System..."

# Start Backend
cd ../backend
source venv/bin/activate
echo "🖥️ Running FastAPI backend at http://localhost:8000"
uvicorn app.main:app --reload &
BACKEND_PID=$!

# Start Frontend
cd ../car-rental-frontend
echo "🌍 Running React Car Rental App at http://localhost:3000"
npm start &

# Wait for user to stop
wait $BACKEND_PID
