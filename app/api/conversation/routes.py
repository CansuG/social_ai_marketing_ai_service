from fastapi import APIRouter
from app.api.conversation.schemas import (
    CheckRequest, CheckResponse,
    UpsertResponse, DeleteResponse
)
from app.api.conversation.repo import ConversationRepository, KNOWN_TRUE_CONVERSATION_ID
from app.api.conversation.service import ConversationService

router = APIRouter(prefix="/conversation", tags=["conversation"])

_repo = ConversationRepository()
_service = ConversationService(_repo)

@router.post("/check", response_model=CheckResponse)
def check_conversation(body: CheckRequest):
    exists = _service.check_exists(body.conversation_id)
    return CheckResponse(conversation_id=body.conversation_id, exists=exists)

@router.post("/upsert", response_model=UpsertResponse)
def upsert_conversation(body: CheckRequest):
    created = _service.upsert(body.conversation_id)
    return UpsertResponse(conversation_id=body.conversation_id, created=created)

@router.post("/delete", response_model=DeleteResponse)
def delete_conversation(body: CheckRequest):
    deleted = _service.delete(body.conversation_id)
    return DeleteResponse(conversation_id=body.conversation_id, deleted=deleted)

# Debug için (istersen sonra kaldırırız)
@router.get("/list")
def list_conversations():
    return {"items": _service.list_all()}

@router.get("/example_ids")
def example_ids():
    return {
        "known_true_conversation_id": KNOWN_TRUE_CONVERSATION_ID,
        "random_false_example": "conv_does_not_exist_999999",
    }
