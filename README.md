# Insurance GenAI RAG Platform

A production-style GenAI backend project that demonstrates document ingestion, text chunking, embeddings, vector storage, and semantic search for insurance policy documents using Retrieval-Augmented Generation (RAG) concepts.

---

# Project Overview

This project simulates an Insurance AI Assistant that helps claims teams, underwriting teams, and customer support agents search policy documents intelligently using semantic search and vector databases.

The application demonstrates the core retrieval pipeline used in enterprise GenAI systems before the Large Language Model (LLM) generation layer.

---

# Features

- FastAPI backend APIs
- Insurance document ingestion
- Text chunking pipeline
- Sentence Transformer embeddings
- ChromaDB vector database
- Semantic search implementation
- Swagger API documentation
- Modular service-based architecture
- Production-style project structure

---

# Architecture

See detailed architecture here:

```text
docs/architecture.md
```

---

# System Workflow

```text
User Question
     |
     v
FastAPI Endpoint
     |
     v
Document Loader
     |
     v
Text Chunking
     |
     v
Sentence Transformer Embeddings
     |
     v
ChromaDB Vector Database
     |
     v
Semantic Search Results
```

---

# Screenshots

## Swagger API Documentation

![Swagger](docs/screenshots/swagger.png)

---

## Document Loading

![Documents](docs/screenshots/documents.png)

---

## Text Chunking

![Chunks](docs/screenshots/chunks.png)

---

## Vector Storage

![Store Embeddings](docs/screenshots/store_embeddings.png)

---

## Semantic Search

![Semantic Search](docs/screenshots/semantic_search.png)

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| FastAPI | REST API framework |
| Sentence Transformers | Embedding generation |
| ChromaDB | Vector database |
| Uvicorn | ASGI server |
| Pydantic | Request validation |

---

# Project Structure

```text
insurance-genai-rag-platform
│
├── app
│   ├── main.py
│   └── services
│       ├── document_loader.py
│       ├── text_splitter.py
│       ├── embedding_service.py
│       └── llm_service.py
│
├── data
│   ├── raw
│   └── vector_db
│
├── docs
│   ├── architecture.md
│   └── screenshots
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

# API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/health` | GET | Check API status |
| `/documents` | GET | Load insurance documents |
| `/chunks` | GET | Split documents into chunks |
| `/store-embeddings` | POST | Store chunks into vector DB |
| `/search` | POST | Semantic search on insurance documents |
| `/ask` | POST | RAG question answering endpoint |

---

# Sample Semantic Search Request

```json
{
  "question": "Is water damage covered?"
}
```

---

# Sample Semantic Search Response

```json
{
  "question": "Is water damage covered?",
  "results": [
    {
      "content": "Water damage is covered only if caused by a covered peril.",
      "distance": 0.89
    }
  ]
}
```

---

# What This Project Demonstrates

This project demonstrates the foundational architecture behind enterprise Retrieval-Augmented Generation (RAG) systems:

1. Document ingestion
2. Text chunking
3. Embedding generation
4. Vector storage
5. Semantic retrieval
6. Context-based AI workflows

---

# Future Enhancements

- PDF document upload
- Streamlit frontend UI
- OpenAI integration
- Azure OpenAI integration
- Ollama local LLM integration
- Multi-document search
- JWT authentication
- Docker deployment
- MLflow monitoring
- GraphRAG implementation

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Aasmeen-shaik/insurance-genai-rag-platform.git
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python -m uvicorn app.main:app --reload
```

---

# Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

---

# Recruiter Keywords

GenAI, RAG, Retrieval-Augmented Generation, Vector Database, ChromaDB, Embeddings, FastAPI, Python, Semantic Search, Insurance AI, Document Intelligence, AI Backend Engineering, LLMOps

---

# Author

Aasmeen Shaik

AI/ML Engineer | GenAI | RAG | LLM Applications | Python Backend Development