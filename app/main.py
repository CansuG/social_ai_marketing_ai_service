from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from app.mock_db import exists_conversation_id, KNOWN_TRUE_CONVERSATION_ID

app = FastAPI(
    title="Social AI Marketing AI Services",
    version="0.2.0",
    description="Contains services related conversations on platforms like Instagram or used data by AI agent.",
)

class CheckResponse(BaseModel):
    conversation_id: str
    exists: bool


@app.get("/health")
def health():
    return {"status": "ok"}


# 🔹 Ortak iş mantığı (tek yerde)
def check_conversation(conversation_id: str) -> CheckResponse:
    return CheckResponse(
        conversation_id=conversation_id,
        exists=exists_conversation_id(conversation_id),
    )


# 🔹 1) QUERY PARAM KULLANAN ENDPOINT 
@app.get("/check_by_conversation_id", response_model=CheckResponse)
def check_by_conversation_id_query(
    conversation_id: str = Query(
        ...,
        description="Instagram conversation / entry id",
        example=KNOWN_TRUE_CONVERSATION_ID,
    )
):
    return check_conversation(conversation_id)


# 🔹 2) PATH PARAM KULLANAN ENDPOINT
@app.get("/check_by_conversation_id/{conversation_id}", response_model=CheckResponse)
def check_by_conversation_id_path(conversation_id: str):
    return check_conversation(conversation_id)


@app.get("/example_ids")
def example_ids():
    return {
        "known_true_conversation_id": KNOWN_TRUE_CONVERSATION_ID,
        "random_false_example": "conv_does_not_exist_999999",
    }
