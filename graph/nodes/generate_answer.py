from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage

from utils.llm_adapter import get_llm
chat = get_llm(temperature=0, max_tokens=120)

def generate_answer(state):

    summary = state.get("summary", "")
    messages = state.get("messages") or []
    docs = state.get("docs", "")

    recent = messages[-6:]

    history = "\n".join(
        f"{'User' if isinstance(m, HumanMessage) else 'AI'}: {m.content}"
        for m in recent
    )

    prompt = f"""
        You are a helpful assistant.

        Conversation Summary:
        {summary}

        Recent Chat:
        {history}

        Relevant Context (Always in english):
        {docs}

        User Question:
        {state["question"]}

        Rules:
        - Answer ONLY from context if possible
        - Be concise (2-3 sentences max)
        - Do not repeat history
        - IMPORTANT: Detect the PRIMARY language of the User Question (the language most words are written in)
          and respond in that SAME language. If the question mixes Arabic and English equally,
          default to Arabic. The context may be in English — translate your answer if needed.
    """

    response = chat.invoke(prompt)

    return {
        "messages": messages + [
            HumanMessage(content=state["question"]),
            AIMessage(content=response.content)
        ]
    }