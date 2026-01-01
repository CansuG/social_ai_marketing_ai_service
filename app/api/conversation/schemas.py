from pydantic import BaseModel, Field

class CheckRequest(BaseModel):
    conversation_id: str = Field(..., description="Instagram conversation / entry id")

class CheckResponse(BaseModel):
    conversation_id: str
    exists: bool
