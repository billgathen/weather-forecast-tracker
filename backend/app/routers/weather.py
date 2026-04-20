from datetime import datetime
import logging

import httpx
from app.schemas import Latitude, Longitude

logger = logging.getLogger(__name__)

base_url = "https://api.weather.gov"

def hourly_forecast_url(lat: Latitude, long: Longitude) -> str:
  logger.info(f"Checking NWS for {lat},{long}...")
  try:
    r = httpx.get(f"{base_url}/points/{lat},{long}", timeout=10.0)
    r.raise_for_status()
  except httpx.TimeoutException:
    raise Exception(f"Timeout fetching NWS point data for {lat},{long}")
  except httpx.HTTPStatusError as e:
    raise Exception(f"NWS returned {e.response.status_code} for {lat},{long}")
  
  data = r.json()

  try:
    return data["properties"]["forecastHourly"]
  except KeyError:
    raise Exception(f"Unexpected NWS response structure: {data}")
  
def get_forecasts(url: str):
  logger.info(f"Loading forecasts from {url}")
  try:
    r = httpx.get(url, timeout=10.0)
    r.raise_for_status()
  except httpx.TimeoutException:
    raise Exception(f"NWS timed-out fetching forecasts from {url}")
  except httpx.HTTPStatusError as e:
    raise Exception(f"NWS returned {e.response.status_code} from {url}")
  
  data = r.json()
  forecast = [
    {
      "day": datetime.fromisoformat(p["startTime"]).strftime("%Y-%m-%d"),
      "hour": datetime.fromisoformat(p["startTime"]).strftime("%H"),
      "temperature": p["temperature"],
      "temperatureUnit": p["temperatureUnit"]
    }
    for p in data["properties"]["periods"]
  ]

  logger.info(forecast)