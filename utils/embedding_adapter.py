import os
from dotenv import load_dotenv

load_dotenv()

def get_embeddings():
    provider = os.getenv("EMBEDDING_PROVIDER", "openai").lower()
    model = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

    if provider == "openai":
        from langchain_openai import OpenAIEmbeddings
        return OpenAIEmbeddings(model=model)

    elif provider == "huggingface":
        from langchain_huggingface import HuggingFaceEmbeddings
        return HuggingFaceEmbeddings(model_name=model)

    else:
        raise ValueError(f"Unsupported EMBEDDING_PROVIDER: {provider}")