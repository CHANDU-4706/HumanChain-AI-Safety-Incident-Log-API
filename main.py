from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.database.database import get_db, engine
from app.models import incident as models
from app.schemas import incident as schemas

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Safety Incident Log API",
    description="API for logging and managing AI safety incidents",
    version="1.0.0"
)

@app.get("/incidents", response_model=List[schemas.Incident])
def get_incidents(db: Session = Depends(get_db)):
    """
    Retrieve all incidents from the database.
    """
    incidents = db.query(models.Incident).all()
    return incidents

@app.post("/incidents", response_model=schemas.Incident, status_code=status.HTTP_201_CREATED)
def create_incident(incident: schemas.IncidentCreate, db: Session = Depends(get_db)):
    """
    Create a new incident in the database.
    """
    db_incident = models.Incident(**incident.model_dump())
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident

@app.get("/incidents/{incident_id}", response_model=schemas.Incident)
def get_incident(incident_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific incident by ID.
    """
    incident = db.query(models.Incident).filter(models.Incident.id == incident_id).first()
    if incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident

@app.delete("/incidents/{incident_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_incident(incident_id: int, db: Session = Depends(get_db)):
    """
    Delete a specific incident by ID.
    """
    incident = db.query(models.Incident).filter(models.Incident.id == incident_id).first()
    if incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")
    
    db.delete(incident)
    db.commit()
    return None 