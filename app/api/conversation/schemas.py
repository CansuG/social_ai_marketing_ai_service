from pydantic import BaseModel, Field

class CheckRequest(BaseModel):
    conversation_id: str = Field(..., description="Instagram conversation / entry id")

class CheckResponse(BaseModel):
    conversation_id: str
    exists: bool

class UpsertResponse(BaseModel):
    conversation_id: str
    created: bool  # True: yeni eklendi, False: zaten vardı (update)

class DeleteResponse(BaseModel):
    conversation_id: str
    deleted: bool
