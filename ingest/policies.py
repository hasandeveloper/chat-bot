import requests
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters.character import CharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma
import re
import copy

def process_policy(file_name: str, s3_url: str):
    print(f"Ingesting file: {file_name}")

    # Example: return metadata
    return {
        "file_name": file_name,
        "file_path": s3_url,
        "status": "ingested"
    }