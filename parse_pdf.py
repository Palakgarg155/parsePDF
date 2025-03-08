import nltk
import re
import pdfplumber

nltk.download("punkt")

def extract_text_from_pdf(pdf_file):
    """Extract text while preserving spaces properly."""
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n" if page.extract_text() else ""
    return text.strip()

def preprocess_text(text):
    """Preprocess text: clean spaces and preserve sentence structure."""
    text = re.sub(r"(\s*\.\s*)+", ". ", text)  # Remove repeated dots
    text = re.sub(r"\s{2,}", " ", text).strip()  # Normalize excessive spaces
    sentences = nltk.sent_tokenize(text)  
    return "\n".join(sentences)  # Keep sentences separate