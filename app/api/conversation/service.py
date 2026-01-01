from app.api.conversation.repo import ConversationRepository

class ConversationService:
    def __init__(self, repo: ConversationRepository):
        self.repo = repo

    def check_exists(self, conversation_id: str) -> bool:
        conversation_id = conversation_id.strip()
        return self.repo.exists(conversation_id)

    def upsert(self, conversation_id: str) -> bool:
        conversation_id = conversation_id.strip()
        return self.repo.upsert(conversation_id)

    def delete(self, conversation_id: str) -> bool:
        conversation_id = conversation_id.strip()
        return self.repo.delete(conversation_id)

    def list_all(self) -> list[str]:
        return self.repo.list_all()
