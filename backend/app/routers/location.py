
import logging

from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Location
from app.schemas import AddLocationRequest, AddLocationResponse
from app.routers.weather import get_forecasts, hourly_forecast_url

logger = logging.getLogger(__name__)

router = APIRouter()

async def fetch_and_store_forecast(location: Location, db: Session):
  _ = get_forecasts(location.hourly_forecast_url)
  logger.info("TODO: add to database here")

@router.post("/locations", response_model=AddLocationResponse)
async def add_location(location: AddLocationRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_db)) -> AddLocationResponse:
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

  background_tasks.add_task(fetch_and_store_forecast, new_loc, db)

  return AddLocationResponse.model_validate(new_loc)
