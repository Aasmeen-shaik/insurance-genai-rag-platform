from pathlib import Path

RAW_DATA_PATH = Path("data/raw")

def load_documents():
    documents = []

    for file in RAW_DATA_PATH.glob("*.txt"):
        text = file.read_text(encoding="utf-8")

        documents.append({
            "file_name": file.name,
            "content": text
        })

    return documents