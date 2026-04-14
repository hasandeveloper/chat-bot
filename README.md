# 🤖 Chatbot Local Setup (No Poetry)

This project sets up a **LangChain + Chroma + OpenAI powered chatbot backend** using FastAPI.

---

# 🧩 1. Install Miniconda

Download Miniconda:
👉 https://www.anaconda.com/download

```bash
bash ~/Downloads/Miniconda3-*.sh
source ~/miniconda3/bin/activate
```

---

# 🐍 2. Create Environment

```bash
conda create -n chat-bot python=3.10
conda activate chat-bot
```

---

# 📦 3. Install Dependencies

```bash
pip install --upgrade pip

pip install \
fastapi uvicorn \
pydantic requests python-dotenv \
openai \
chromadb \
langchain \
langchain-openai \
langchain-community \
langchain-chroma \
jupyterlab notebook ipykernel
```

---

# ⚠️ 4. Fix M1 / Protobuf Issue (if needed)

```bash
pip install "protobuf<=3.20.3"
```

---

# 📓 5. Register Jupyter Kernel

```bash
python -m ipykernel install --user --name=chat-bot --display-name "Python (chat-bot)"
```

---

# 🚀 6. Run FastAPI Server

```bash
uvicorn main:app --reload
```

Server will run at:
```
http://127.0.0.1:8000
```

---

# 📥 7. Ingest Documents (S3 → Vector DB)

Use this Example endpoint to ingest a document into ChromaDB:

```bash
curl -X POST "http://127.0.0.1:8000/api/ingest" \
  -H "Content-Type: application/json" \
  -d '{
    "file_name": "terms_conditions",
    "s3_url": "https://stargallery-assets.s3.me-central-1.amazonaws.com/pdf-documents/en/TERMS+and+conditions.pdf"
  }'
```

---

## 📌 Ingest API Details

- **Endpoint:** `POST /api/ingest`
- **Purpose:** Load document from S3 → process → store embeddings in ChromaDB

### Request Body:
```json
{
  "file_name": "terms_conditions",
  "s3_url": "https://your-s3-url/file.pdf"
}
```

### ⚠️ Requirements:
- FastAPI server must be running
- Endpoint `/api/ingest` must be implemented
- S3 URL must be publicly accessible or signed

---

# 💬 8. Chat API (Main Endpoint)

Use this endpoint to talk to the chatbot:

```bash
POST http://127.0.0.1:8000/api/chat
```

### Request Body:

```json
{
  "q": "what are the terms and conditions?"
}
```

---

## 📌 Chat API Details

- **Endpoint:** `POST /api/chat`
- **Purpose:** Ask questions to chatbot (RAG-based response)

### Example curl:

```bash
curl -X POST "http://127.0.0.1:8000/api/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "q": "what is the terms and conditions?"
  }'
```

---

# 📓 9. Run Jupyter (Optional)

```bash
jupyter notebook
```

or

```bash
jupyter lab
```

---

# 🧠 Architecture Summary

- FastAPI → Backend API layer
- LangChain → Orchestration
- ChromaDB → Vector database (RAG)
- OpenAI → LLM reasoning
- S3 → Document storage

---

# TODO

- Order status integration

---
