from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma

openai_embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")

def chroma(collection_name="policies", persist_directory="./chroma_db"):
    """
    Load or create a Chroma collection with a global embedding model
    """
    vectorstore = Chroma(
        collection_name=collection_name,
        persist_directory=persist_directory,
        embedding_function=openai_embeddings_model
    )
    return vectorstore