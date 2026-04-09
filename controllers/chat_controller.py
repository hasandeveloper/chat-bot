from fastapi import APIRouter
from services.chat_service import conversation
from schemas.router_schema import ChatRequest

router = APIRouter()

@router.post("/chat")
def ingest_controller(request: ChatRequest):
    answer = conversation(request.q)
    return {
        "status": "success",
        "data": answer
    }