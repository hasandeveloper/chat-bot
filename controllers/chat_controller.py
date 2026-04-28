from fastapi import APIRouter
from services.chat_service import conversation
from schemas.router_schema import ChatRequest

router = APIRouter()

@router.post("/chat")
def chat_controller(request: ChatRequest):

    answer = conversation(
        user_id="user_1",   # temporary hardcoded (or get from auth later)
        q=request.q
    )

    return {
        "status": "success",
        "data": answer
    }

