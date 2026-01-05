from fastapi import FastAPI
from app.api.conversation.routes import router as conversation_router
from sqlalchemy import text
from app.db import get_engine
from fastapi import HTTPException
import traceback

app = FastAPI(title="Social AI Marketing AI Services", version="0.5.0")

app.include_router(conversation_router, prefix="/api")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db_ping")
def db_ping():
    try:
        engine = get_engine()
        with engine.begin() as conn:
            v = conn.execute(text("SELECT 1")).scalar_one()
        return {"db": "ok", "value": v}
    except Exception as e:
        # Uvicorn loglarında tam stacktrace görürsün
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
