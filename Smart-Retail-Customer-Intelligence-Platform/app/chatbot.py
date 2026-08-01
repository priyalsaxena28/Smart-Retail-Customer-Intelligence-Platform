from fastapi import APIRouter
from pydantic import BaseModel
import joblib
import numpy as np

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

router = APIRouter()

# Load chatbot knowledge base
chatbot = joblib.load("models/chatbot.pkl")

questions = chatbot["questions"]
answers = chatbot["answers"]
embeddings = chatbot["embeddings"]

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(request: ChatRequest):

    # Convert user question to embedding
    query_embedding = model.encode([request.question])

    # Compare with stored embeddings
    similarity = cosine_similarity(query_embedding, embeddings)

    best_index = np.argmax(similarity)
    best_score = similarity[0][best_index]

    # Confidence threshold
    if best_score < 0.5:
        return {
            "question": request.question,
            "answer": "Sorry, I couldn't understand your question."
        }

    return {
        "question": request.question,
        "answer": answers[best_index],
        "confidence": round(float(best_score), 3)
    }