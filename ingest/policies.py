import requests
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters.character import CharacterTextSplitter
from langchain_core.documents import Document
from db.vector import chroma
import copy
import hashlib
import re

vectorstore = chroma()


# -------------------------
# Clean text
# -------------------------
def clean_text(text: str) -> str:
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


# -------------------------
# Download PDF
# -------------------------
def download_file(s3_url: str, file_name: str):
    response = requests.get(s3_url)

    if response.status_code != 200:
        raise Exception(f"Failed to download {s3_url}, status: {response.status_code}")

    file_path = f"/tmp/{file_name}.pdf"

    with open(file_path, "wb") as f:
        f.write(response.content)

    return file_path


# -------------------------
# File hash (idempotency)
# -------------------------
def file_hash(file_path: str):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


# -------------------------
# Main ingestion logic
# -------------------------
def process_policy(file_name: str, s3_url: str):
    print(f"📄 Processing file: {file_name}")

    # 1. Download file
    file_path = download_file(s3_url, file_name)

    # 2. Compute hash
    fhash = file_hash(file_path)

    # -------------------------
    # 3. SAFE Chroma metadata read
    # -------------------------
    all_data = vectorstore._collection.get(include=["metadatas"])
    metadatas = all_data.get("metadatas") or []

    existing_hashes = [
        m.get("file_hash")
        for m in metadatas
        if m and isinstance(m, dict) and m.get("file_hash")
    ]

    # 4. Duplicate check
    if fhash in existing_hashes:
        print(f"⚠️ File already ingested: {file_name}")
        return {
            "file_name": file_name,
            "status": "skipped",
            "reason": "duplicate content"
        }

    # 5. Load PDF
    loader = PyPDFLoader(file_path)
    pages = loader.load()

    # 6. Add metadata
    for p in pages:
        p.metadata["source_file"] = file_name
        p.metadata["file_hash"] = fhash

    # 7. Clean text
    pages_clean = copy.deepcopy(pages)

    for doc in pages_clean:
        doc.page_content = clean_text(doc.page_content)

    # 8. Split into chunks
    splitter = CharacterTextSplitter(chunk_size=700, chunk_overlap=50)
    chunks = splitter.split_documents(pages_clean)

    # 9. Store in Chroma
    vectorstore.add_documents(chunks)

    print(f"✅ Stored {len(chunks)} chunks for {file_name}")

    return {
        "file_name": file_name,
        "num_pages": len(pages),
        "num_chunks": len(chunks),
        "status": "ingested",
        "file_hash": fhash
    }