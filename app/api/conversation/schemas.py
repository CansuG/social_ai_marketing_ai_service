from pydantic import BaseModel, Field

class EnsureConversationRequest(BaseModel):
    customer_number: str = Field(..., description="Customer identifier (e.g., Instagram sender.id)")
    seller_external_id: str = Field(..., description="Seller identifier (e.g., Instagram entry.id or recipient.id)")
    channel: str = Field("instagram", description="Channel name")

class EnsureConversationResponse(BaseModel):
    exists: bool
    conversation_db_id: int
    customer_number: str
    channel: str
    channel_thread_id: str
