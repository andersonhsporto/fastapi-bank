from fastapi import FastAPI

from app import models
from app.config import engine
from app.routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/api/v1", tags=["accounts"])

