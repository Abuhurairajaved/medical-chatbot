# Medical Chatbot using RAG & FastAPI

## Description
A Medical Chatbot powered by Retrieval-Augmented Generation (RAG) and FastAPI. It allows users to register, log in, and ask medical-related questions. The chatbot fetches relevant answers from the MedQuAD dataset using ChromaDB as a vector store.

## Features
- User authentication (registration & login) with JWT-based authorization.
- Secure user authentication using SQLite for storing user data.
- Retrieval-Augmented Generation (RAG) using ChromaDB for retrieving medical answers.
- FastAPI for backend API handling.
- SQLite for storing queries and responses.
- HTML & CSS frontend for user interaction.

## Dataset
- **MedQuAD Dataset** (Medical Question-Answer Dataset)
  - Cloned from: [MedQuAD GitHub Repository](https://github.com/abuhurairajaved/MedQuAD)
  - Converted XML files into JSON for easy retrieval.

## Tech Stack & Dependencies
- **Backend:** FastAPI, SQLite, ChromaDB
- **Frontend:** HTML, CSS
- **Authentication:** OAuth2, JWT
- **Vector Store:** ChromaDB
- **Parsing:** Pydantic

### Required Python Libraries
Install the dependencies using:
```sh
pip install fastapi uvicorn sqlite3 chromadb passlib bcrypt jose pydantic
```

## Project Structure
```
D:\chatbot
│── app/
│   │── main.py  # FastAPI Backend
│   │── database.py  # Database Setup
│   │── auth.py  # Authentication Handling
│── templates/
│   │── index.html  # Login/Register Page
│   │── chatbot.html  # Chat Interface
│── static/
│   │── styles.css  # CSS for Frontend
│── chatbot.db  # SQLite Database
│── README.md
```

## Running the Project
1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/Medical-Chatbot.git
   cd Medical-Chatbot
   ```
2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run FastAPI server**
   ```sh
   uvicorn app.main:app --reload
   ```
4. **Access the frontend**
   - Open `http://127.0.0.1:8000`

## API Endpoints
| Method | Endpoint     | Description |
|--------|-------------|-------------|
| POST   | `/register` | Register a new user |
| POST   | `/token`    | Login and get JWT token |
| GET    | `/chatbot`  | Ask a question |

## Future Improvements
- Improve UI with JavaScript for better UX.
- Enhance RAG with a more advanced retrieval model.
- Deploy the chatbot as a web app.

## License
This project is open-source under the MIT License.

---
_Developed by Abuhuraira Javaid_
