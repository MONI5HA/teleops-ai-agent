from app.rag.rag_engine import load_documents, chunk_text, build_vector_store, search

docs = load_documents("data/docs")

chunks = []
for doc in docs:
    chunks.extend(chunk_text(doc))

index, chunks = build_vector_store(chunks)

results = search("What causes low SINR?", index, chunks)

for r in results:
    print("\n--- RESULT ---\n")
    print(r)