import os
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = SentenceTransformer("BAAI/bge-large-en-v1.5")

index = faiss.read_index(
    os.path.join(BASE_DIR, "vectorstore", "index.faiss")
)

with open(
    os.path.join(BASE_DIR, "vectorstore", "slides.pkl"),
    "rb"
) as f:
    slides = pickle.load(f)


def retrieve(query, top_k=10):

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True
    ).astype(np.float32)

    faiss.normalize_L2(query_embedding)

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:

        if idx == -1:
            continue

        results.append(slides[idx])

    return results