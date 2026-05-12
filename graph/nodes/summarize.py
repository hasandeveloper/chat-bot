from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

chat = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def summarize(state):

    messages = state.get("messages") or []

    if len(messages) < 4:
        return state

    text = "\n".join(
        f"{'User' if isinstance(m, HumanMessage) else 'AI'}: {m.content}"
        for m in messages
    )
    summary = chat.invoke(f"""
        Summarize this conversation in max 4 lines.

        Focus only on:
        - user intent
        - key questions
        - important answers
        - IMPORTANT: Write the summary in the primary language the user is using.
          If the conversation mixes Arabic and English, default to Arabic.
          
        Conversation:
        {text}
    """)

    return {
        **state,   # ✅ IMPORTANT: preserve everything
        "summary": summary.content,
        "messages": messages[-6:]   # keep only recent window
    }
