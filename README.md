
# 🚗 Car Rental System

A full-stack car rental system with a FastAPI backend, ReactJS frontend, and SDK generation via OpenAPI CLI.

---

## 📁 Project Structure



car-rental-system/  
├── backend/ # FastAPI backend  
│ ├── app/ # Main app logic  
│ ├── tests/ # Unit tests  
│ └── requirements.txt  
├── frontend/ # ReactJS frontend  
├── scripts/ # Setup and run scripts (Linux & Windows)  
├── car_rental_sdk/ # Generated Python SDK  
├── seed_data.sql # Optional: initial DB data  
└── README.md


## ⚙️ Requirements

- Python 3.9+
- Node.js & npm
- OpenAPI Generator CLI (for SDK)
- pip / virtualenv
- Unix shell or PowerShell

---

## 🚀 Setup Instructions

### 🐧 On Linux / macOS:

```bash
cd scripts
chmod +x setup.sh run.sh
./setup.sh
./run.sh
````

### 🪟 On Windows (PowerShell):

```powershell
cd scripts
.\setup.ps1
.\run.ps1
```

---
## 🔌 Backend (FastAPI)

- Runs at: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`
- Requirements: See `backend/requirements.txt`
---

## 🌐 Frontend (ReactJS)

- Runs at: `http://localhost:3000`
- Communicates with backend using Axios/fetch
---

## 📦 SDK Generation

```bash
openapi-generator-cli generate -i http://localhost:8000/openapi.json -g python -o car_rental_sdk
```

Install OpenAPI CLI if missing:

```bash
npm install @openapitools/openapi-generator-cli -g
```

---
## 🧪 Running Tests

```bash
cd backend
source venv/bin/activate   # or .\venv\Scripts\Activate.ps1 (Windows)
pytest
```
---
## 🛠 Technologies Used

- FastAPI + SQLAlchemy
- PostgreSQL / SQLite
- ReactJS + Axios
- OpenAPI Generator
- Alembic (for migrations)
---
## 📞 Contact

For any queries, feel free to reach out.

Happy Renting! 🚗💨

Let me know if you'd like to:
- Add database migration support with Alembic
- Include SDK usage examples in the README
- Write automated tests or CI workflows

Would you like me to generate the `car_rental_sdk` directory too
