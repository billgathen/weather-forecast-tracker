
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Location
from app.schemas import AddLocationRequest, AddLocationResponse
from app.routers.weather import hourly_forecast_url


router = APIRouter()

@router.post("/locations", response_model=AddLocationResponse)
def add_location(location: AddLocationRequest, db: Session = Depends(get_db)) -> AddLocationResponse:
  existing = db.execute(
    select(Location).where(
      Location.lat == location.lat,
      Location.long == location.long
    )
  ).scalar_one_or_none()

  if existing:
    return AddLocationResponse.model_validate(existing)

  new_loc = Location(
      lat=location.lat,
      long=location.long,
      hourly_forecast_url=hourly_forecast_url(location.lat, location.long)
  )  
  
  db.add(new_loc)
  db.commit()
  db.refresh(new_loc)
  return AddLocationResponse.model_validate(new_loc)
