import json
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

# Load JSON Data
json_file = "D:/chatbot/dataset/medquad_cleaned.json"
with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Initialize ChromaDB
client = chromadb.PersistentClient(path="D:/chatbot/dataset/chromadb")

# Define embedding model (using a lightweight Sentence Transformer)
embedding_function = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# Create Collection
collection = client.get_or_create_collection(name="medquad", embedding_function=embedding_function)

# Add Data to Collection
for idx, item in enumerate(data):
    collection.add(
        ids=[str(idx)],  # Unique ID for each document
        documents=[item["question"]],  # Use question as the text to index
        metadatas=[{"answer": item["answer"], "topic": item["topic"], "source": item["source"]}]
    )

print("✅ Data indexed into ChromaDB successfully!")
