from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
import numpy as np

client = QdrantClient("http://localhost:6333")

resume_embeddings = np.load('resume_embeddings.npy')
resumes = load_resumes('path_to_resumes_folder')

client.recreate_collection(
    collection_name="resumes",
    vector_params=VectorParams(size=resume_embeddings.shape[1], distance=Distance.COSINE)
)

vectors = resume_embeddings.tolist()
payload = [{'resume_text': resume} for resume in resumes]
client.upsert(collection_name="resumes", vectors=vectors, payload=payload)
