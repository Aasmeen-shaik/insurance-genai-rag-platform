from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="data/vector_db")

collection = client.get_or_create_collection(
    name="insurance_documents"
)


def store_chunks(chunks):
    for chunk in chunks:
        chunk_id = f'{chunk["file_name"]}_{chunk["chunk_id"]}'

        embedding = model.encode(chunk["content"]).tolist()

        collection.add(
            documents=[chunk["content"]],
            embeddings=[embedding],
            ids=[chunk_id]
        )

    return {
        "message": "Chunks stored successfully",
        "total_chunks": len(chunks)
    }
def search_chunks(query, top_k=3):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    matched_chunks = []

    documents = results.get("documents", [[]])[0]
    distances = results.get("distances", [[]])[0]

    for document, distance in zip(documents, distances):
        matched_chunks.append({
            "content": document,
            "distance": distance
        })

    return matched_chunks
def retrieve_context(query, top_k=2):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    documents = results.get("documents", [[]])[0]

    return "\n\n".join(documents)