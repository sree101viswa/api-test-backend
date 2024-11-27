from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import District
from ..schemas import DistrictResponse

router = APIRouter()

@router.get("/districts", response_model=list[DistrictResponse])
def list_districts(db: Session = Depends(get_db)):
    """Fetch all districts from the database."""
    districts = db.query(District).all()
    return districts
