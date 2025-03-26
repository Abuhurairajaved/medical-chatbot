import chromadb

# Initialize ChromaDB client
client = chromadb.PersistentClient(path="D:/chatbot/dataset/chromadb")

# Load the collection
collection = client.get_collection(name="medquad")

# Function to query ChromaDB
def ask_question(query):
    results = collection.query(
        query_texts=[query],
        n_results=3  # Get the top 3 most relevant answers
    )
    
    if results["documents"]:
        print("\n🔎 **Top Answers:**")
        for i in range(len(results["documents"][0])):
            print(f"\n👉 **Answer {i+1}:** {results['metadatas'][0][i]['answer']}")
            print(f"📌 **Topic:** {results['metadatas'][0][i]['topic']}")
            print(f"📖 **Source:** {results['metadatas'][0][i]['source']}")
    else:
        print("\n❌ No relevant answer found.")

# Run Query Loop
while True:
    user_input = input("\n💬 Ask a medical question (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    ask_question(user_input)

