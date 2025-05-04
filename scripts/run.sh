#!/bin/bash

echo "🚀 Starting Car Rental System..."

# Start Backend
cd ../backend
source venv/bin/activate
echo "🖥️ Running FastAPI backend at http://localhost:8000"
uvicorn app.main:app --reload &
BACKEND_PID=$!

# Start Frontend
cd ../frontend
echo "🌍 Running React frontend at http://localhost:3000"
npm start &

# Wait for user to stop
wait $BACKEND_PID
