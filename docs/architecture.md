# Insurance GenAI RAG Platform Architecture

## High-Level Workflow

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