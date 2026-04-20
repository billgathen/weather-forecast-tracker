from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

Latitude = Annotated[float, Field(ge=-90, le=90)]
Longitude = Annotated[float, Field(ge=-90, le=90)]

class AddLocationRequest(BaseModel):
  lat: Latitude
  long: Longitude

class AddLocationResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  id: int
  lat: Latitude
  long: Longitude
  hourly_forecast_url: str
  created_at: datetime
  updated_at: datetime
