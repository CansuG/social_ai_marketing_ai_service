from fastapi import APIRouter
from app.api.conversation.schemas import EnsureConversationRequest, EnsureConversationResponse
from app.api.conversation.repo import ConversationRepository
from app.api.conversation.service import ConversationService

router = APIRouter(prefix="/conversation", tags=["conversation"])

_repo = ConversationRepository()
_service = ConversationService(_repo)

@router.post("/ensure", response_model=EnsureConversationResponse)
def ensure_conversation(body: EnsureConversationRequest):
    exists, conv_id, thread_id = _service.ensure_conversation(
        customer_number=body.customer_number,
        seller_external_id=body.seller_external_id,
        channel=body.channel,
    )
    return EnsureConversationResponse(
        exists=exists,
        conversation_db_id=conv_id,
        customer_number=body.customer_number,
        channel=body.channel,
        channel_thread_id=thread_id,
    )
