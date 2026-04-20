# weather-forecast-tracker

Dockerized application in Python that tracks the variation in weather temperature forecasts over time for a given location using the weather.gov API and a local data store.

## Instructions

You'll need [git](https://git-scm.com/) and [Docker](https://docs.docker.com/desktop/) installed on your local system.

If you're using VSCode, you can fork this project on GitHub, open a fresh VSCode window, and select `Clone Repository` in the explorer sidebar. Your fork should be first in the list.

If you prefer the command-line or another editor, run the following in the terminal in the parent folder of where you'd like your code

`git clone https://github.com/billgathen/weather-forecast-tracker.git`

In the terminal, run `docker compose up --build` in your project root and the environments will be set up for you automatically.

To setup the database tables, change to the `backend` folder and run `alembic upgrade head`. If it errors, run `source venv/bin/activate` and try again.

View the interactive docs for the api at http://localhost:8000/docs

## Task list

- DONE Docker compose (python + postgres)
- DONE Dockerfile python
- DONE .env.example + .env (already in .gitignore)
- DONE local config (venv, vscode settings)
- DONE requirements.txt (fastapi, uvicorn, sqlalchemy, psycopg2-binary, alembic, pydantic, apscheduler, dotenv)
- DONE initialize main.py
- DONE /health endpoint
- DONE /dbhealth endpoint
- DONE db integration (sqlalchemy, alembic)
- DONE models (location, forecast)
- schemas
  - DONE location
  - forecasts
- routers
  - DONE POST location
  - GET forecast
- api integration
  - DONE get forecast url for location
  - get latest forecast from station (predicted temp by hour for next 72 hours)
- job (every x minutes, refresh forecasts for each location)
