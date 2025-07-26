# ===== app/document_loader.py =====
import os
import fitz  

def load_documents(pdf_dir: str):
    """Load all PDF documents and return a dict of page texts."""
    documents = {}
    for filename in os.listdir(pdf_dir):
        file_path = os.path.join(pdf_dir, filename)
        if filename.endswith(".pdf") and os.path.isfile(file_path):
            try:
                doc = fitz.open(file_path)
                pages = [page.get_text("text") for page in doc]
                documents[filename] = pages
            except Exception as e:
                print(f"[!] Failed to load {filename}: {e}")
    return documents
