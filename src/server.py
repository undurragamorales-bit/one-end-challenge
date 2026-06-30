from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
from src.agent import ask_agent
from fastapi.middleware.cors import CORSMiddleware

print("SERVER:", Path(__file__).resolve())

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # para desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    name: str
    question: str


@app.get("/")
def inicio():
    return {"mensaje": "Servidor funcionando"}


@app.get("/prueba")
def prueba():
    return {"ok": True}


@app.post("/chat")
def chat(request: ChatRequest):
    answer = ask_agent(request.name, request.question)
    return {"answer": answer}
