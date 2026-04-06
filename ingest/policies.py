import requests
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters.character import CharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma
import re
import copy


def download_file(s3_url: str, file_name: str):
    """
    Download PDF from S3 URL and save locally
    """
    response = requests.get(s3_url)
    
    file_path = f"/tmp/{file_name}.pdf"

    with open(file_path, "wb") as f:
        f.write(response.content)

    return file_path


def process_policy(file_name: str, s3_url: str):
    """
    Ingest a single PDF into Chroma vector DB
    """
    print(f"Ingesting file: {file_name}")

    # 👉 1. Download file
    file_path = download_file(s3_url, file_name)

    # 👉 2. Load PDF
    loader = PyPDFLoader(file_path)
    pages = loader.load()

    # Add metadata (important for multi-doc search later)
    for p in pages:
        p.metadata["source_file"] = file_name

    # 👉 3. Clean text
    pages_clean = copy.deepcopy(pages)

    for doc in pages_clean:
        text = doc.page_content
        text = " ".join(text.split())  # remove extra spaces/newlines
        doc.page_content = text

    # 👉 4. Split text
    char_splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    pages_split = char_splitter.split_documents(pages_clean)

    # 👉 5. Embeddings
    embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")

    # 👉 6. Store in Chroma (persistent DB)
    persist_directory = "./chroma_db"

    vectorstore = Chroma.from_documents(
        documents=pages_split,
        embedding=embeddings_model,
        persist_directory=persist_directory
    )

    print(f"Stored {len(pages_split)} chunks for {file_name}")

    # 👉 7. Return metadata
    return {
        "file_name": file_name,
        "num_pages": len(pages),
        "num_chunks": len(pages_split),
        "persist_directory": persist_directory,
        "status": "ingested"
    }