from typing import Optional
from sqlalchemy import text
from app.db import get_engine

SCHEMA_CHAT = "u9105298_social.chat"

class ConversationRepository:
    def __init__(self):
        self.engine = get_engine()
        self.conversations = f"{SCHEMA_CHAT}.conversations"

    def find_by_thread(self, channel: str, channel_thread_id: str) -> Optional[int]:
        sql = text(f"""
            SELECT TOP 1 conversation_id
            FROM {self.conversations}
            WHERE channel = :channel
              AND channel_thread_id = :thread_id
        """)
        with self.engine.connect() as conn:
            row = conn.execute(sql, {"channel": channel, "thread_id": channel_thread_id}).first()
            return int(row[0]) if row else None

    def insert(self, customer_number: str, channel: str, channel_thread_id: str) -> int:
        sql = text(f"""
            INSERT INTO {self.conversations}
              (customer_number, channel, channel_thread_id, status, created_at, updated_at)
            OUTPUT INSERTED.conversation_id
            VALUES
              (:customer_number, :channel, :thread_id, 'open', SYSUTCDATETIME(), SYSUTCDATETIME())
        """)
        with self.engine.begin() as conn:
            conv_id = conn.execute(sql, {
                "customer_number": customer_number,
                "channel": channel,
                "thread_id": channel_thread_id,
            }).scalar_one()
            return int(conv_id)

    def touch(self, conversation_id: int) -> None:
        sql = text(f"""
            UPDATE {self.conversations}
            SET updated_at = SYSUTCDATETIME()
            WHERE conversation_id = :conversation_id
        """)
        with self.engine.begin() as conn:
            conn.execute(sql, {"conversation_id": conversation_id})
