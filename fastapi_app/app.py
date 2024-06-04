from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModel, AutoTokenizer
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient

app = FastAPI()

client = QdrantClient("http://localhost:6333")
model = SentenceTransformer('all-MiniLM-L6-v2')

class Query(BaseModel):
    query_text: str

@app.post("/search")
async def search(query: Query):
    query_embedding = model.encode(query.query_text, convert_to_tensor=True).tolist()
    results = client.search(
        collection_name="resumes",
        query_vector=query_embedding,
        limit=10
    )
    return results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
