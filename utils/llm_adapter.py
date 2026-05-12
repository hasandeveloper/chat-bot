import os
from dotenv import load_dotenv

load_dotenv()

def get_llm(temperature=0, max_tokens=1000):
    provider = os.getenv("LLM_PROVIDER", "openai").lower()
    model = os.getenv("LLM_MODEL", "gpt-4o-mini")

    if provider == "openai":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model=model, temperature=temperature, max_tokens=max_tokens)

    elif provider == "anthropic":
        from langchain_anthropic import ChatAnthropic
        return ChatAnthropic(model=model, temperature=temperature, max_tokens=max_tokens)

    elif provider == "groq":
        from langchain_groq import ChatGroq
        return ChatGroq(model=model, temperature=temperature, max_tokens=max_tokens)

    else:
        raise ValueError(f"Unsupported LLM_PROVIDER: {provider}")