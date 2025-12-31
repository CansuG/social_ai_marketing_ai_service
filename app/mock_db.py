from typing import Set

# TODO: Senin elindeki "true" döndürmesini istediğin conversation/entry id'yi buraya koyacağız.
KNOWN_TRUE_CONVERSATION_ID = "17841478128416550"

# Mock "DB tablosu" gibi düşün
MOCK_CONVERSATION_IDS: Set[str] = {
    KNOWN_TRUE_CONVERSATION_ID,
    "1001",
    "1002",
}

def exists_conversation_id(conversation_id: str) -> bool:
    return conversation_id in MOCK_CONVERSATION_IDS
