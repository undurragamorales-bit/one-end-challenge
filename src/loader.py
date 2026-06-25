from pathlib import Path

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


DOCS_DIR = Path("docs")     #se define la carpeta en donde se ubican los PDF
CHUNK_SIZE = 300            #se declara el tamaño de chunk
CHUNK_OVERLAP = 30          #se declara el traslapo del chunk


##### se cargan los archivos ######

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

##### se dividen los documentos en chunks ######
if __name__ == "__main__":
    docs = load_pdfs()

    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    docs_splits = splitter.split_documents(docs)

    for chunk in docs_splits:
        print(chunk)
        print("-----------------")
