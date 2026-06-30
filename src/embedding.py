import os
from pathlib import Path
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from src.loader import load_chunks



BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
EMBEDDING_MODEL = "embed-multilingual-v3.0"
SCORE_THRESHOLD = 0.3
K_DOCUMENTS = 4

#FAISS_DIR = BASE_DIR / "faiss_index"
FAISS_DIR = Path(os.getenv("FAISS_PATH"))

def save_vectorstore(vectorstore):
    FAISS_DIR.mkdir(parents=True, exist_ok=True)
    vectorstore.save_local(str(FAISS_DIR))



def load_vectorstore():
    modelo_embeddings = get_embedding_model()

    vectorstore = FAISS.load_local(
        str(FAISS_DIR),
        modelo_embeddings,
        allow_dangerous_deserialization=True,
    )

    return vectorstore



def get_embedding_model():
    if not COHERE_API_KEY:
        raise ValueError("Falta configurar la variable de entorno COHERE_API_KEY")

    modelo_embeddings = CohereEmbeddings(
        model=EMBEDDING_MODEL,
        cohere_api_key=COHERE_API_KEY,
    )

    return modelo_embeddings


def create_vectorstore(chunks):
    modelo_embeddings = get_embedding_model()
    vectorstore = FAISS.from_documents(chunks, modelo_embeddings)
    return vectorstore


def create_retriever(vectorstore):
    retriever = vectorstore.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"score_threshold": SCORE_THRESHOLD, "k": K_DOCUMENTS},
    )

    return retriever


def create_knowledge_retriever():

    index_file = FAISS_DIR / "index.faiss"

    if index_file.exists():

        print("📂 Cargando índice FAISS...")

        vectorstore = load_vectorstore()

    else:

        print("🛠 Creando índice FAISS por primera vez...")

        chunks = load_chunks()

        vectorstore = create_vectorstore(chunks)

        save_vectorstore(vectorstore)

        print("✅ Índice FAISS guardado correctamente.")

    retriever = create_retriever(vectorstore)

    return retriever


if __name__ == "__main__":
    retriever = create_knowledge_retriever()
    print("Retriever creado correctamente")
