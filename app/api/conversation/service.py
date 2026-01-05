from app.api.conversation.repo import ConversationRepository

class ConversationService:
    def __init__(self, repo: ConversationRepository):
        self.repo = repo

    def make_channel_thread_id(self, channel: str, seller_external_id: str, customer_number: str) -> str:
        return f"{channel}:{seller_external_id}:{customer_number}"

    def ensure_conversation(self, customer_number: str, seller_external_id: str, channel: str = "instagram"):
        channel = (channel or "instagram").strip()
        customer_number = customer_number.strip()
        seller_external_id = seller_external_id.strip()

        thread_id = self.make_channel_thread_id(channel, seller_external_id, customer_number)

        existing = self.repo.find_by_thread(channel=channel, channel_thread_id=thread_id)
        if existing is not None:
            self.repo.touch(existing)
            return True, existing, thread_id

        new_id = self.repo.insert(customer_number=customer_number, channel=channel, channel_thread_id=thread_id)
        return False, new_id, thread_id
