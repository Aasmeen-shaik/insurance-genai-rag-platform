# Insurance GenAI RAG Platform

A backend GenAI project that demonstrates document ingestion, chunking, embeddings, vector storage, and semantic search for insurance policy documents.

## Project Overview

This project simulates an insurance AI assistant that helps claims and underwriting teams search policy documents using Retrieval-Augmented Generation concepts.

## Features

- FastAPI backend
- Insurance document ingestion
- Text chunking pipeline
- Sentence Transformer embeddings
- ChromaDB vector database
- Semantic search API
- Swagger API testing
- Modular project structure

## Tech Stack

- Python
- FastAPI
- Sentence Transformers
- ChromaDB
- Uvicorn
- Pydantic

## API Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/health` | GET | Check API health |
| `/documents` | GET | Load insurance documents |
| `/chunks` | GET | Split documents into chunks |
| `/store-embeddings` | POST | Store chunks as vectors |
| `/search` | POST | Search documents semantically |

## Sample Query

```json
{
  "question": "Is water damage covered?"
}