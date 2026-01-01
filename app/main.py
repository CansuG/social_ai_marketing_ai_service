from fastapi import FastAPI
from app.api.conversation.routes import router as conversation_router

app = FastAPI(
    title="Social AI Marketing AI Services",
    version="0.3.0",
    description="Theme-based API structure (conversation now, more modules later).",
)

# Tüm tema endpoint’leri /api altında toplansın
app.include_router(conversation_router, prefix="/api")

@app.get("/health")
def health():
    return {"status": "ok"}