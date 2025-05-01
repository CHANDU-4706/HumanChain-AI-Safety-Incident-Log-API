# HumanChain-AI-Safety-Incident-Log-API
This project is a RESTful API service developed for the Backend Intern Take-Home Assignment at HumanChain. It is designed to log, retrieve, and manage hypothetical AI safety incidents, aligning with HumanChain’s mission to promote safe and trustworthy AI systems.

# AI Safety Incident Log Service

A RESTful API service for logging and managing AI safety incidents.

## Technology Stack

- Language: Python 3.8+
- Framework: FastAPI
- Database: PostgreSQL
- ORM: SQLAlchemy
- Migration Tool: Alembic

## Setup Instructions

1. Clone this repository:
```bash
git clone <repository-url>
cd ai-safety-incidents-api
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables by creating a `.env` file:
```
DATABASE_URL=postgresql://username:password@localhost:5432/ai_safety_incidents
```

5. Initialize the database:
```bash
alembic upgrade head
```

6. Run the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### 1. Get All Incidents
```bash
GET /incidents

curl http://localhost:8000/incidents
```

### 2. Create New Incident
```bash
POST /incidents

curl -X POST http://localhost:8000/incidents \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Unexpected Model Behavior",
    "description": "AI model produced inconsistent results during testing",
    "severity": "Medium"
  }'
```

### 3. Get Specific Incident
```bash
GET /incidents/{id}

curl http://localhost:8000/incidents/1
```

### 4. Delete Incident
```bash
DELETE /incidents/{id}

curl -X DELETE http://localhost:8000/incidents/1
```

## Data Structure

Each incident has the following fields:
- `id`: Integer (auto-generated)
- `title`: String
- `description`: Text
- `severity`: String (Low/Medium/High)
- `reported_at`: Timestamp (auto-generated)

## Sample Data

The database will be automatically populated with sample incidents when you run the migrations.

## Error Handling

The API implements proper error handling for:
- Invalid request data
- Non-existent resources
- Database connection issues
- Invalid severity levels

## Design Decisions

1. Used FastAPI for:
   - Automatic OpenAPI documentation
   - Built-in request validation
   - Modern async support
   - Type checking with Pydantic

2. Chose PostgreSQL for:
   - ACID compliance
   - Robust transaction support
   - JSON support
   - Production readiness

3. Implemented SQLAlchemy ORM for:
   - Database abstraction
   - SQL injection prevention
   - Easy query building
   - Migration support with Alembic 
