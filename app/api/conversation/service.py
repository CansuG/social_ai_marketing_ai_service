from app.api.conversation.repo import ConversationRepository

class ConversationService:
    def __init__(self, repo: ConversationRepository):
        self.repo = repo

    def check_exists(self, conversation_id: str) -> bool:
        # İleride: normalize (lowercase, trim), metrics, caching vs burada olur
        conversation_id = conversation_id.strip()
        return self.repo.exists(conversation_id)
