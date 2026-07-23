from fastapi import FastAPI

from backend.api.prediction import router as prediction_router
from backend.api.recommendation import router as recommendation_router

app = FastAPI(

    title="Finoviq AI",

    version="1.0.0"

)

app.include_router(prediction_router)

app.include_router(recommendation_router)