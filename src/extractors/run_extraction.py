import os
from extractors.extract_docx import extract_docx_text
from extractors.extract_xlsx import extract_xlsx_text
from extractors.extract_pdf import extract_pdf_text
from extractors.extract_txt import extract_txt

def extract_file_text(filepath: str) -> str:
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".docx":
        return extract_docx_text(filepath)
    elif ext == ".xlsx":
        return extract_xlsx_text(filepath)
    elif ext == ".pdf":
        return extract_pdf_text(filepath)
    elif ext == ".txt":
        return extract_txt(filepath)
    else:
        return ""


