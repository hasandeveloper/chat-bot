
# 🤖 AI Chatbot Backend (LangChain + LangGraph + RAG + FastAPI)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![LangChain](https://img.shields.io/badge/LangChain-LLM%20Orchestration-orange)
![ChromaDB](https://img.shields.io/badge/VectorDB-Chroma-purple)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-black)

---

## 📌 Project Overview

This project is a **production-style AI chatbot backend** built using:

* 🧠 LangGraph for conversation orchestration
* 🔍 RAG pipeline using ChromaDB
* 💬 OpenAI GPT-4o for reasoning
* ⚡ FastAPI for backend APIs
* 🧠 Redis for memory storage
* ☁️ S3 for document ingestion

It supports:

* Conversational memory
* Document-based Q&A (RAG)
* Context-aware responses
* Scalable backend design

---

## 🧠 Architecture

```
User Query
   ↓
FastAPI (/chat)
   ↓
LangGraph Pipeline
   ├── Load Memory (Redis)
   ├── Retrieve Context (ChromaDB)
   ├── Generate Answer (GPT-4o)
   ├── Summarize Memory
   └── Store Memory (Redis)
   ↓
Final Response
```

---

## ⚙️ Setup Instructions

---

## 🧩 1. Install Miniconda

```bash
bash ~/Downloads/Miniconda3-*.sh
source ~/miniconda3/bin/activate
```

---

## 🐍 2. Create Environment

```bash
conda create -n chat-bot python=3.10
conda activate chat-bot
```

---

## 📦 3. Install Dependencies

```bash
pip install --upgrade pip

pip install \
fastapi uvicorn \
pydantic requests python-dotenv \
openai \
chromadb \
redis \
langgraph \
langchain \
langchain-core \
langchain-openai \
langchain-community \
langchain-chroma
```

---

## ⚠️ 4. Fix M1 / Protobuf Issue (if needed)

```bash
pip install "protobuf<=3.20.3"
```

---

## 🚀 5. Run Server

```bash
uvicorn main:app --reload
```

📍 Server:

```
http://127.0.0.1:8000
```

---

## 📥 6. Document Ingestion (S3 → ChromaDB)

```bash
curl -X POST "http://127.0.0.1:8000/api/ingest" \
  -H "Content-Type: application/json" \
  -d '{
    "file_name": "terms_conditions",
    "s3_url": "https://your-s3-url.pdf"
  }'
```

---

## 💬 7. Chat API

### Endpoint

```
POST /api/chat
```

### Request

```json
{
  "q": "what are the return policies?"
}
```

### Example

```bash
curl -X POST "http://127.0.0.1:8000/api/chat" \
  -H "Content-Type: application/json" \
  -d '{"q":"what is return policy?"}'
```

---

## 🧠 Core System Design

### 🔹 Memory System

* Redis stores:

  * conversation history
  * conversation summary

### 🔹 RAG System

* ChromaDB stores embeddings
* Retrieves top-k relevant docs per query

### 🔹 LLM Layer

* GPT-4o generates final responses
* Uses:

  * summary (long-term memory)
  * recent messages (short-term memory)
  * retrieved docs (knowledge base)

---

## 🧠 Key Features

* ✅ Conversational memory (short + long-term)
* ✅ RAG-based retrieval system
* ✅ LangGraph workflow orchestration
* ✅ Redis-based persistence
* ✅ Modular backend design
* ✅ FastAPI production API layer

---

## 🧩 TODO (Roadmap)

* [ ] Order tracking integration
* [ ] User authentication (JWT)
* [ ] Streaming responses
* [ ] Multi-session chat support
* [ ] Dockerization
* [ ] Observability (LangSmith / tracing)
* [ ] Rate limiting + caching

---

## ⚡ Tech Stack

* **Backend:** FastAPI
* **LLM:** OpenAI GPT-4o
* **Orchestration:** LangGraph
* **Framework:** LangChain
* **Vector DB:** ChromaDB
* **Cache / Memory:** Redis
* **Runtime:** Python 3.10

---

## 📌 Summary

This project demonstrates a **real-world production architecture for AI chatbots** combining:

> RAG + Memory + LLM + Backend Engineering
