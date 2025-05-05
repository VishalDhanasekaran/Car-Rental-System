#!/bin/bash

echo "🔧 Setting up Car Rental System (Backend + Frontend)..."

# Backend Setup
echo "📦 Installing Python dependencies..."
cd ../backend
python3 -m venv venv
source venv/bin/activate
echo "Virtual Environment Activated..."
pip install -r requirements.txt

# Database Initialization (Assumes SQLite or migration tool)
echo "🗃️ Initializing database..."
alembic upgrade head 2>/dev/null || echo "⚠️ Alembic migration skipped (if not configured)"

# Frontend Setup
echo "🌐 Installing frontend dependencies..."
echo "Current path: "
pwd
cd ../car-rental-frontend
echo "changed to fronted directory..."
npm install

echo "✅ Setup completed. Use run.sh to start the system."
