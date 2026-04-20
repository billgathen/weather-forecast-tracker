
from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Location
from app.schemas import AddLocationRequest, AddLocationResponse


router = APIRouter()

@router.post("/locations", response_model=AddLocationResponse)
def add_location(location: AddLocationRequest, db: Session = Depends(get_db)) -> AddLocationResponse:
  final_loc = None

  try:
    new_loc = Location(
      lat=location.lat,
      long=location.long,
      station_url="unimplemented"
    )
    db.add(new_loc)
    db.commit()
    db.refresh(new_loc)
    final_loc = new_loc
  except IntegrityError:
    db.rollback()
    existing = db.execute(select(Location).where(
      Location.lat==location.lat, 
      Location.long==location.long
      )).scalar_one()
    final_loc = existing

  return AddLocationResponse.model_validate(final_loc)