from fastapi import APIRouter

from backend.schemas.stock import StockInput
from backend.models.predict import predict_next_day

router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"],
)


@router.post("/predict")
def predict(stock: StockInput):

    prediction = predict_next_day(stock.model_dump())

    return {

        "status": "success",

        "prediction": prediction

    }