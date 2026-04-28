import json
from langchain_core.messages import AIMessage, HumanMessage
from db.redis_client import redis

def load_memory(state):

    user_id = state["user_id"]
    data = redis.get(user_id)

    if not data:
        return {"messages": [], "summary": ""}

    data = json.loads(data)
    messages = []
    for m in data.get("messages", []):
        if m["role"] == "user":
            messages.append(HumanMessage(content=m["content"]))
        else:
            messages.append(AIMessage(content=m["content"]))
    return {
        "messages": messages,
        "summary": data.get("summary", "")
    }