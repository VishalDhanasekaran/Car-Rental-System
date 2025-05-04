Write-Host "🚀 Starting Car Rental System..."

# Start Backend
cd ../backend
.\venv\Scripts\Activate.ps1
Start-Process powershell -ArgumentList "uvicorn app.main:app --reload"

# Start Frontend
cd ../frontend
Start-Process powershell -ArgumentList "npm start"
