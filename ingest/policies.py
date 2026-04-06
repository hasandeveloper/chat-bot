import requests
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters.character import CharacterTextSplitter
from db.vector import chroma
import copy
import hashlib

vectorstore = chroma() 

# Download file from url to local
def download_file(s3_url: str, file_name: str):
    """
    Download PDF from S3 URL and save locally
    """
    response = requests.get(s3_url)
    if response.status_code != 200:
        raise Exception(f"Failed to download {s3_url}, status: {response.status_code}")
    

    file_path = f"/tmp/{file_name}.pdf"

    with open(file_path, "wb") as f:
        f.write(response.content)

    return file_path

# You can detect duplicate files by comparing hashes.
# Even if two PDFs have the same name but different content, their SHA-256 hash will differ.
# Duplicate pdfs wont be ingested even slighter change in pdf as it uses sha256
def file_hash(file_path: str):
    """
    Compute SHA256 hash of a file
    """

    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
            
    return sha256.hexdigest()

def process_policy(file_name: str, s3_url: str):
    """
    Ingest a PDF into Chroma vector DB in an idempotent way using file hash
    """
    print(f"Processing file: {file_name}")

    # 1️⃣ Download file
    file_path = download_file(s3_url, file_name)

    # 2️⃣ Compute hash
    fhash = file_hash(file_path)

    # 3️⃣ Check for existing hash in Chroma
    all_metadata = vectorstore._collection.get(include=["metadatas"])
    existing_hashes = [m.get("file_hash") for m in all_metadata["metadatas"] if m.get("file_hash")]
    breakpoint()
    if fhash in existing_hashes:
        print(f"File '{file_name}' already ingested. Skipping.")
        return {"file_name": file_name, "status": "skipped", "reason": "duplicate content"}

    # 4️⃣ Load PDF
    loader = PyPDFLoader(file_path)
    pages = loader.load()

    # 5️⃣ Add metadata (file name + hash)
    for p in pages:
        p.metadata["source_file"] = file_name
        p.metadata["file_hash"] = fhash

    # 6️⃣ Clean text
    pages_clean = copy.deepcopy(pages)
    for doc in pages_clean:
        doc.page_content = " ".join(doc.page_content.split())

    # 7️⃣ Split text into chunks
    char_splitter = CharacterTextSplitter(chunk_size=700, chunk_overlap=50)
    pages_split = char_splitter.split_documents(pages_clean)

    breakpoint()
    # 8️⃣ Store in Chroma
    vectorstore.add_documents(pages_split)

    print(f"Stored {len(pages_split)} chunks for {file_name}")

    return {
        "file_name": file_name,
        "num_pages": len(pages),
        "num_chunks": len(pages_split),
        "status": "ingested",
        "file_hash": fhash
    }
