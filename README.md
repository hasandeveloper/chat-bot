
# 🤖 AI Chatbot Backend Service (LangChain + LangGraph + RAG + FastAPI)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![LangChain](https://img.shields.io/badge/LangChain-LLM%20Orchestration-orange)
![ChromaDB](https://img.shields.io/badge/VectorDB-Chroma-purple)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-black)

## 📌 Project Overview

This project is a **production-style AI chatbot backend** built using:

* 🧠 LangGraph for conversation orchestration
* 🔍 RAG pipeline using ChromaDB
* 💬 OpenAI GPT-4o for reasoning
* ⚡ FastAPI for backend APIs
* 🧠 Redis for memory storage

It supports:

* Conversational memory
* Document-based Q&A (RAG)
* Context-aware responses
* Scalable backend design

## 🎯 Why This Project

Most chatbot APIs are stateless and cannot maintain long-term context.

This project solves that by combining:
- Stateful memory (Redis)
- Long-term summarization
- RAG-based knowledge retrieval
- LangGraph orchestration

Making it suitable for real-world SaaS integrations.

## 🧠 Architecture

```
User Query
   ↓
FastAPI (/api/chat)
   ↓
LangGraph Orchestrator
   ├── Load Memory (Redis)
   ├── Retrieve Context (ChromaDB)
   ├── Generate Answer (GPT-4o)
   ├── Summarize Conversation
   └── Store Memory (Redis)
   ↓
Response to User
```

## 🧠 How It Works

1. User sends a question with `user_id`
2. System loads conversation history from Redis
3. Relevant documents are retrieved from ChromaDB (RAG)
4. LangGraph orchestrates the flow:
   - memory → retrieval → reasoning → response
5. GPT-4o generates a final contextual answer
6. Conversation is updated + summarized for future use

## ⚙️ Setup Instructions

## 🧩 1. Install Miniconda

```bash
Visit:- https://www.anaconda.com/docs/getting-started/miniconda/install/mac-cli-install
bash ~/Downloads/Miniconda3-*.sh
source ~/miniconda3/bin/activate
```

## 🐍 2. Create Environment

```bash
conda create -n chat-bot python=3.10
conda activate chat-bot
```

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

## ⚠️ 4. Fix M1 / Protobuf Issue (if needed)

```bash
pip install "protobuf<=3.20.3"
```

## 🚀 5. Run Server

```bash
uvicorn main:app --reload
```

📍 Server:

```
http://127.0.0.1:8000
```

## 📥 6. Document Ingestion (S3 → ChromaDB)

```bash
curl -X POST "http://127.0.0.1:8000/api/ingest" \
  -H "Content-Type: application/json" \
  -d '{
    "file_name": "terms_conditions",
    "s3_url": "https://your-s3-url.pdf"
  }'
```

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

## 🧠 Core System Design

### 🔹 Memory System
Redis stores:
- Full conversation history
- Running conversation summary (for long-term context)

### 🔹 RAG System
ChromaDB:
- Stores embedded documents
- Retrieves top-k relevant context per query

### 🔹 LLM Layer
GPT-4o:
- Uses conversation summary (long-term memory)
- Uses recent messages (short-term memory)
- Uses retrieved context (RAG)
- Generates final response

## 🧠 Key Features

* ✅ Conversational memory (short + long-term)
* ✅ RAG-based retrieval system
* ✅ LangGraph workflow orchestration
* ✅ Redis-based persistence
* ✅ Modular backend design
* ✅ FastAPI production API layer


## 🧩 TODO (Roadmap)
* [ ] Config Move
* [ ] Multilingual Support (Arabic + English)
* [ ] Dockerization
* [ ] Observability (LangSmith / tracing)

## ⚡ Tech Stack

* **Backend:** FastAPI
* **LLM:** OpenAI GPT-4o
* **Orchestration:** LangGraph
* **Framework:** LangChain
* **Vector DB:** ChromaDB
* **Cache / Memory:** Redis
* **Runtime:** Python 3.10

## 📌 Summary

This project demonstrates a **real-world production architecture for AI chatbots** combining:

> RAG + Memory + LLM + Backend Engineering
