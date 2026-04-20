from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class AddLocationRequest(BaseModel):
  lat: Annotated[float, Field(ge=-90, le=90)]
  long: Annotated[float, Field(ge=-90, le=90)]

class AddLocationResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  id: int
  lat: float
  long: float
  station_url: str
  created_at: datetime
  updated_at: datetime
