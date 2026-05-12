from langchain_chroma import Chroma
from utils.embedding_adapter import get_embeddings

def chroma(collection_name="policies", persist_directory="./chroma_db"):
    vectorstore = Chroma(
        collection_name=collection_name,
        persist_directory=persist_directory,
        embedding_function=get_embeddings()
    )
    return vectorstore