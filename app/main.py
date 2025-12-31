from fastapi import FastAPI
from pydantic import BaseModel
from app.mock_db import exists_conversation_id, KNOWN_TRUE_CONVERSATION_ID

app = FastAPI(
    title="Social AI Marketing AI Services",
    version="0.1.0",
    description="Checks whether a given Instagram conversation/entry conversation_id exists (mock for now).",
)

class CheckResponse(BaseModel):
    conversation_id: str
    exists: bool

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/check_by_conversation_id/{conversation_id}", response_model=CheckResponse)
def check_by_conversation_id(conversation_id: str):
    return {
        "conversation_id": conversation_id,
        "exists": exists_conversation_id(conversation_id),
    }

@app.get("/example_ids")
def example_ids():
    """
    n8n / Postman / Swagger denemeleri için örnek id'leri döndürür.
    """
    return {
        "known_true_conversation_id": KNOWN_TRUE_CONVERSATION_ID,
        "random_false_example": "conv_does_not_exist_999999"
    }
