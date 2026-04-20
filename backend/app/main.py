from fastapi import FastAPI
from app.routers.healthchecks import router as healthchecks

app = FastAPI()
app.include_router(healthchecks)
