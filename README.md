# weather-forecast-tracker

Dockerized application in Python that tracks the variation in weather temperature forecasts over time for a given location using the weather.gov API and a local data store.

## Instructions

You'll need [git](https://git-scm.com/) and [Docker](https://docs.docker.com/desktop/) installed on your local system.

If you're working VSCode, you can fork this project on GitHub, open a fresh VSCode window, and select `Clone Repository`. Your fork should be first in the list.

If you prefer the command-line or another editor, run the following in the terminal in the parent folder of where you'd like your code

`git clone https://github.com/billgathen/weather-forecast-tracker.git`

In the terminal, run `docker compose up --build` and the environments will be set up for you automatically.

View the interactive docs for the app at http://localhost:8000/docs

## Task list

- DONE Docker compose (python + postgres)
- DONE Dockerfile python
- DONE .env.example + .env (already in .gitignore)
- DONE local config (venv, vscode settings)
- DONE requirements.txt (fastapi, uvicorn, sqlalchemy, alembic, pydantic, apscheduler, dotenv)
- DONE initialize main.py
- DONE /health
- /dbhealth endpoints
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

```

```
