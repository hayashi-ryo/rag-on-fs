from docx import Document

def extract_docx_text(filepath: str) -> str:
    doc = Document(filepath)
    text = "\n".join([para.text for para in doc.paragraphs if para.text.strip() != ""])
    return text
