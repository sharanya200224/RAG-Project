import os
import json
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

json_path = os.path.join(BASE_DIR, "output", "slides.json")

with open(json_path, "r", encoding="utf-8") as f:
    slides = json.load(f)

texts = [slide["content"] for slide in slides]

print("Loading embedding model...")

model = SentenceTransformer("BAAI/bge-large-en-v1.5")

print("Generating embeddings...")

embeddings = model.encode(
    texts,
    convert_to_numpy=True,
    normalize_embeddings=True,
    show_progress_bar=True
)

embeddings = embeddings.astype(np.float32)

faiss.normalize_L2(embeddings)

dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)

index.add(embeddings)

vector_dir = os.path.join(BASE_DIR, "vectorstore")
os.makedirs(vector_dir, exist_ok=True)

faiss.write_index(
    index,
    os.path.join(vector_dir, "index.faiss")
)

with open(
    os.path.join(vector_dir, "slides.pkl"),
    "wb"
) as f:
    pickle.dump(slides, f)

print("✅ FAISS Index Created Successfully!")