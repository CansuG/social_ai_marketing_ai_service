from fastapi import APIRouter
from app.api.conversation.schemas import CheckRequest, CheckResponse
from app.api.conversation.repo import ConversationRepository, KNOWN_TRUE_CONVERSATION_ID
from app.api.conversation.service import ConversationService

router = APIRouter(prefix="/conversation", tags=["conversation"])

_repo = ConversationRepository()
_service = ConversationService(_repo)

@router.post("/check", response_model=CheckResponse)
def check_conversation(body: CheckRequest):
    exists = _service.check_exists(body.conversation_id)
    return CheckResponse(conversation_id=body.conversation_id, exists=exists)

@router.get("/example_ids")
def example_ids():
    return {
        "known_true_conversation_id": KNOWN_TRUE_CONVERSATION_ID,
        "random_false_example": "conv_does_not_exist_999999",
    }
