# 🧪 AI LABS - LABY

### Industrial AI Assistant powered by Knowledge Retrieval

> AI assistant for industrial documentation built with **FastAPI**,
> **LangChain**, **Cohere**, **FAISS** and **Docker**.

## 📖 Overview

**LABY** is an industrial AI assistant designed to answer questions
about operational procedures, maintenance plans, safety manuals and
technical documentation using semantic search over a proprietary
knowledge base.

## ✨ Features

-   ✅ PDF document ingestion
-   ✅ Automatic document chunking
-   ✅ Cohere multilingual embeddings
-   ✅ FAISS vector database
-   ✅ Knowledge Retrieval (RAG)
-   ✅ FastAPI REST API
-   ✅ Industrial SCADA-inspired web interface
-   ✅ Docker containerization
-   ✅ Environment-based configuration
-   ✅ Expandable knowledge base

## 🏗️ Architecture

``` mermaid
flowchart TD
A[PDF Documents] --> B[Document Loader]
B --> C[Chunking]
C --> D[Cohere Embeddings]
D --> E[FAISS Vector Store]
E --> F[Knowledge Retriever]
F --> G[AI Agent]
G --> H[FastAPI]
H --> I[Industrial Web Interface]
```

## 🛠️ Technology Stack

  Technology            Purpose
  --------------------- ------------------
  Python                Backend
  FastAPI               REST API
  LangChain             AI orchestration
  Cohere                Embeddings
  FAISS                 Semantic search
  HTML/CSS/JavaScript   Frontend
  Docker                Deployment

## 📂 Project Structure

``` text
one-end-challenge/
├── docs/
├── faiss_index/
├── front_end/
├── src/
│   ├── agent.py
│   ├── builder_vs.py
│   ├── embedding.py
│   ├── loader.py
│   ├── main.py
│   ├── prompt.py
│   └── server.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## 🚀 Installation

``` bash
git clone <repository-url>
cd one-end-challenge
pip install -r requirements.txt
```

## ⚙️ Environment Variables

``` env
COHERE_API_KEY=your_api_key
FAISS_PATH=faiss_index
```

## 📚 Build the Knowledge Base

``` bash
python -m src.builder_vs
```

Run this command whenever new PDF documents are added to the `docs/`
folder.

## ▶️ Run Locally

``` bash
python -m uvicorn src.server:app --reload
```

Swagger:

`http://localhost:8001/docs`

## 🐳 Docker

``` bash
docker build -t laby:1.0 .
docker run --env-file .env -p 8001:8001 laby:1.0
docker save -o laby-v1.0.tar laby:1.0
```

## 🌐 REST API

### POST `/chat`

Request

``` json
{
  "name":"John",
  "question":"What does the maintenance plan say?"
}
```

Response

``` json
{
  "answer":"..."
}
```

## 🛣️ Roadmap

-   [x] Knowledge Retrieval
-   [x] FastAPI
-   [x] Industrial Web Interface
-   [x] Docker
-   [ ] Oracle Cloud Deployment
-   [ ] HTTPS
-   [ ] Authentication
-   [ ] Conversation Memory

## 💡 Lessons Learned

-   Persist FAISS indexes to reduce API costs.
-   Separate indexing from runtime.
-   Use Docker for reproducible deployments.
-   Keep configuration in environment variables.

## 👤 Author

**José Luis Undurraga Morales**

Electrical Engineer • AI • Automation • Energy Markets
