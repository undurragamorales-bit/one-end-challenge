import os

from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import FAISS

from loader import load_chunks


COHERE_API_KEY = os.getenv("COHERE_API_KEY")
EMBEDDING_MODEL = "embed-multilingual-v3.0"
SCORE_THRESHOLD = 0.3
K_DOCUMENTS = 4


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
    chunks = load_chunks()
    vectorstore = create_vectorstore(chunks)
    retriever = create_retriever(vectorstore)
    return retriever


if __name__ == "__main__":
    chunks = load_chunks()
    vectorstore = create_vectorstore(chunks)
    retriever = create_retriever(vectorstore)

    print(f"Chunks enviados al vector store: {len(chunks)}")
    print("Retriever creado correctamente")
