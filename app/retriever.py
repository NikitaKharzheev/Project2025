import json
import os
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

chroma_path = "chroma_db"
embedding_model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

def load_projects(path="data/hse_all_projects.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def prepare_db():
    if not os.path.exists(chroma_path):
        os.makedirs(chroma_path)

    client = chromadb.Client(Settings(persist_directory=chroma_path, anonymized_telemetry=False))

    if "projects" not in client.list_collections():
        collection = client.create_collection("projects")
        projects = load_projects()
        documents = []
        ids = []
        for i, p in enumerate(projects):
            text = f"{p['Название проекта']}. {p['Описание проекта']} Сроки: {p['Сроки исполнения']}"
            documents.append(text)
            ids.append(str(i))
        embeddings = embedding_model.encode(documents).tolist()
        collection.add(documents=documents, embeddings=embeddings, ids=ids)
    return client

client = prepare_db()

def get_relevant_projects(query_text, k=5):
    collection = client.get_collection("projects")
    query_embedding = embedding_model.encode([query_text])[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=k)
    return "\n\n".join(results["documents"][0])
