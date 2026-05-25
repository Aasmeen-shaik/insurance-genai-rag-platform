def split_text(text, chunk_size=300, overlap=50):
    chunks = []

    if not text or text.strip() == "":
        return chunks

    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end == text_length:
            break

        start = end - overlap

    return chunks


def split_documents(documents):
    chunks = []

    for doc in documents:
        split_texts = split_text(doc["content"])

        for index, text in enumerate(split_texts):
            chunks.append({
                "file_name": doc["file_name"],
                "chunk_id": index,
                "content": text
            })

    return chunks