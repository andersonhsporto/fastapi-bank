from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import router

# models.Base.metadata.create_all(bind=engine)


origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1", tags=["accounts"])
