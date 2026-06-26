from pathlib import Path

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


BASE_DIR = Path(__file__).resolve().parent.parent # se define la carpeta en donde se ubican los PDF, esta función busca dentro de las carpetas hasta encontrar el directorio docs
DOCS_DIR = BASE_DIR / "docs"     
CHUNK_SIZE = 300            # se declara el tamano de chunk
CHUNK_OVERLAP = 30          # se declara el traslapo del chunk

#---------------------------------------
#       Carga de documentos PDF 
#---------------------------------------

def load_pdfs(docs_dir: str | Path = DOCS_DIR):
    docs = []
    docs_path = Path(docs_dir)

    for pdf_file in docs_path.glob("*.pdf"):
        try:
            loader = PyMuPDFLoader(str(pdf_file))
            docs.extend(loader.load())
            print(f"Archivo cargado: {pdf_file.name}")
        except Exception as error:
            print(f"Error cargando archivo {pdf_file.name}: {error}")

    return docs


#---------------------------------------
#       División en chunks
#---------------------------------------


def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    return splitter.split_documents(docs)


#---------------------------------------
#       Carga completa (PDF + chunks)
#---------------------------------------

def load_chunks():
    docs = load_pdfs()
    chunks = split_docs(docs)
    return chunks




if __name__ == "__main__":
    chunks = load_chunks()
    print(f"Chunks creados: {len(chunks)}")
