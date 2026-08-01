from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import joblib

router = APIRouter()

# Load model and vectorizer
model = joblib.load("models/sentiment_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


class Review(BaseModel):
    review: str


@router.post("/predict-sentiment")
async def predict_sentiment(data: Review):

    try:
        review_vector = vectorizer.transform([data.review])

        prediction = model.predict(review_vector)[0]

        return {
            "Review": data.review,
            "Sentiment": str(prediction)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))