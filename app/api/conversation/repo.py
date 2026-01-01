from typing import Set

KNOWN_TRUE_CONVERSATION_ID = "17841478128416550"

# ⚠️ Mock "DB": process restart olunca sıfırlanır.
MOCK_CONVERSATION_IDS: Set[str] = {
    KNOWN_TRUE_CONVERSATION_ID,
    "1001",
    "1002",
}

class ConversationRepository:
    def exists(self, conversation_id: str) -> bool:
        return conversation_id in MOCK_CONVERSATION_IDS

    def upsert(self, conversation_id: str) -> bool:
        """
        Returns:
          created: True  -> yeni eklendi
          created: False -> zaten vardı (update gibi düşün)
        """
        created = conversation_id not in MOCK_CONVERSATION_IDS
        MOCK_CONVERSATION_IDS.add(conversation_id)
        return created

    def delete(self, conversation_id: str) -> bool:
        if conversation_id in MOCK_CONVERSATION_IDS:
            MOCK_CONVERSATION_IDS.remove(conversation_id)
            return True
        return False

    def list_all(self) -> list[str]:
        return sorted(MOCK_CONVERSATION_IDS)
