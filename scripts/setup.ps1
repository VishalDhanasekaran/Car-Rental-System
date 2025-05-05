Write-Host "🔧 Setting up Car Rental System (Backend + Frontend)..."

# Backend Setup
Write-Host "📦 Installing Python dependencies..."
cd ../backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt

# Database Initialization
Write-Host "🗃️ Initializing database..."
alembic upgrade head

# Frontend Setup
Write-Host "🌐 Installing frontend dependencies..."
cd ../car-rental-frontend
npm install

Write-Host "✅ Setup completed. Use run.ps1 to start the system."
