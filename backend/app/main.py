import logging

from fastapi import FastAPI
from app.routers.healthchecks import router as healthchecks
from app.routers.location import router as location

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(healthchecks, tags=["health"])
app.include_router(location, tags=["location"])
