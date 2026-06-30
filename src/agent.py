import os
from pathlib import Path

from langchain_cohere import ChatCohere
from dotenv import load_dotenv

from src.embedding import create_knowledge_retriever
from src.prompt import PROMPT


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

CHAT_MODEL = "command-a-03-2025"
TEMPERATURE = 0.3

#-----------------------------------------
##### se crea el modelo de lenguaje ######
#-----------------------------------------

def get_chat_model():

    cohere_api_key = os.getenv("COHERE_API_KEY")

    if not cohere_api_key:
        raise ValueError(
            "Falta configurar la variable de entorno COHERE_API_KEY"
        )

    llm = ChatCohere(
        model=CHAT_MODEL,
        temperature=TEMPERATURE,
        cohere_api_key=cohere_api_key,
    )

    return llm

#-----------------------------------------
##### se crea el agente RAG ######
#-----------------------------------------


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def create_agent():
    retriever = create_knowledge_retriever()
    llm = get_chat_model()

    def rag_chain(name: str, question: str):
        docs = retriever.invoke(question)
        context = format_docs(docs)
        prompt = PROMPT.invoke({"name": name, "context": context, "input": question})
        response = llm.invoke(prompt)
        return response.content

    return rag_chain


agent = create_agent()

def ask_agent(name: str, question: str):
    
#    answer = agent(question)
#    return answer
    return agent(name, question)

#-----------------------------------------
##### prueba del agente ######
#-----------------------------------------

if __name__ == "__main__":

    question = "los docuemntos qur tienes tienen código de dcoumento?"
    answer = ask_agent("Operador", question)

    print(answer)
