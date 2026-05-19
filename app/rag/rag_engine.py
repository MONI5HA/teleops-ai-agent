from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import logging

logging.basicConfig(level=logging.INFO)



model = SentenceTransformer("all-MiniLM-L6-v2")

def load_documents(path):
    texts=[]
    for file in os.listdir(path):
        with open(os.path.join(path,file),"r",encoding="utf-8") as f:
            texts.append(f.read())
    return texts


def chunk_text(text,chunk_size=200):
    words=text.split()
    chunks = []
    
    for i in range(0,len(words),chunk_size):
        chunks.append(" ".join(words[i:i+chunk_size]))
    return chunks

def build_vector_store(chunks):
    embeddings = model.encode(chunks)
    
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    
    return index,chunks

def search(query, index, chunks, k=3):
    query_embedding = model.encode([query])

    distances, indices = index.search(np.array(query_embedding), k)

    results = [chunks[i] for i in indices[0]]
    logging.info(f"[RAG Agent] Searching telecom knowledge for query")

    return results