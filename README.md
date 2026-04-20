# weather-forecast-tracker

Dockerized application in Python that tracks the variation in weather temperature forecasts over time for a given location using the weather.gov API and a local data store.

## Task list

- Docker compose (python + postgres)
- Dockerfile python
- .env.example + .env (already in .gitignore)
- local config (venv, vscode settings)
- requirements.txt (fastapi, uvicorn, sqlalchemy, alembic, pydantic, apscheduler)
- /health, /dbhealth endpoints
- models (location, forecast)
- db integration (sqlalchemy, alembic)
- schemas (locations, forecasts)
- routers (POST location, GET forecast)
- api integration (get closest station for location, get latest forecast from station (high/low temp by hour for next 72 hours))
- job (every x minutes, refresh forecasts for next 72 hours for each location)

## Possible db schema

### locations

- id
- lat
- long
- station_url
- created_at
- updated_at

### forecasts

- id
- location_id
- day
- hour
- forecasted_high
- forecasted_low
- created_at
- updated_at
