# main.py
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from controllers.ingest_controller import router as ingest_router
from controllers.chat_controller import router as chat_router
from db.redis_client import redis
from langchain_core.documents import Document
from db.vector import chroma

vectorstore = chroma()
app = FastAPI()
app.include_router(ingest_router, prefix="/api")
app.include_router(chat_router, prefix="/api")

@app.on_event("startup")
def startup_checks():

    # 🔹 Redis check
    try:
        redis.ping()
        print("✅ Redis connected successfully")
    except Exception as e:
        print("❌ Redis connection failed:", str(e))

    # 🔹 Chroma check
    try:
        vectorstore.add_documents([
            Document(page_content="Stargalery knowledge")
        ])

        results = vectorstore.similarity_search("test", k=1)

        print("✅ Chroma working:", results[0].page_content)

    except Exception as e:
        print("❌ Chroma failed:", str(e))

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    # Build a friendly error message
    errors = [{"field": e["loc"][-1], "message": e["msg"]} for e in exc.errors()]
    return JSONResponse(
        status_code=400,
        content={"error": "Invalid request", "details": errors},
    )


@app.get("/")
def home():
    return {"message": "Chatbot Running"}