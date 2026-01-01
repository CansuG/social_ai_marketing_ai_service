from typing import Set

KNOWN_TRUE_CONVERSATION_ID = "17841478128416550"

MOCK_CONVERSATION_IDS: Set[str] = {
    KNOWN_TRUE_CONVERSATION_ID,
    "conv_1001",
    "conv_1002",
}

class ConversationRepository:
    """
    Data access katmanı.
    Şimdilik mock. Sonra burayı DB sorgusuna çevirirsin.
    """
    def exists(self, conversation_id: str) -> bool:
        return conversation_id in MOCK_CONVERSATION_IDS
