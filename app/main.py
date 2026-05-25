from app.services.embedding_service import retrieve_context
from app.services.llm_service import generate_answer
from pydantic import BaseModel


from pydantic import BaseModel
from app.services.embedding_service import search_chunks

from app.services.embedding_service import store_chunks
from app.services.text_splitter import split_documents
from fastapi import FastAPI
from app.services.document_loader import load_documents
class SearchRequest(BaseModel):
    question: str
class SearchRequest(BaseModel):
    question: str
app = FastAPI(
    title="Insurance GenAI RAG Platform",
    description="AI platform for insurance document search and claim intelligence",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Insurance GenAI RAG Platform Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/documents")
def get_documents():
    docs = load_documents()

    return {
        "total_documents": len(docs),
        "documents": docs
    }
@app.get("/chunks")
def get_chunks():
    docs = load_documents()
    chunks = split_documents(docs)

    return {
        "total_chunks": len(chunks),
        "chunks": chunks
    }
@app.post("/store-embeddings")
def store_embeddings():
    docs = load_documents()
    chunks = split_documents(docs)
    result = store_chunks(chunks)

    return result
@app.get("/debug-docs")
def debug_docs():
    docs = load_documents()

    return {
        "total_documents": len(docs),
        "first_doc_length": len(docs[0]["content"]) if docs else 0,
        "first_doc_preview": docs[0]["content"][:200] if docs else "No document found"
    }
@app.post("/search")
def search_policy(request: SearchRequest):
    results = search_chunks(request.question)

    return {
        "question": request.question,
        "results": results
    }
@app.post("/ask")
def ask_question(request: SearchRequest):

    context = retrieve_context(request.question)

    answer = generate_answer(
        question=request.question,
        context=context
    )

    return {
        "question": request.question,
        "context": context,
        "answer": answer
    }