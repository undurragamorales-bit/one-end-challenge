from src.embedding import load_chunks, create_vectorstore, save_vectorstore

print("🔨 Construyendo índice FAISS...")

chunks = load_chunks()
vectorstore = create_vectorstore(chunks)
save_vectorstore(vectorstore)

print("✅ Índice creado correctamente.")