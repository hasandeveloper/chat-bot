from langchain_core.messages import HumanMessage, AIMessage
from db.redis_client import redis
import json

def store_memory(state):

    messages = state.get("messages") or []

    serialized = []

    for m in messages:

        if isinstance(m, HumanMessage):
            serialized.append({
                "role": "user",
                "content": m.content
            })

        elif isinstance(m, AIMessage):
            serialized.append({
                "role": "ai",
                "content": m.content
            })

    data = {
        "summary": state.get("summary", ""),
        "messages": serialized
    }
    
    redis.set(state["user_id"], json.dumps(data))

    return state