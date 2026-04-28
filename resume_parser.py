import pdfplumber
import re


def extract_text_from_pdf(uploaded_file):
    """
    Takes an uploaded PDF file (from Streamlit)
    and returns clean extracted text.
    """
    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    text = clean_text(text)
    return text


def clean_text(text):
    """
    Removes unnecessary symbols and extra whitespace.
    """
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # Remove non-ASCII characters
    text = re.sub(r'\s+', ' ', text)             # Replace multiple spaces with one
    text = text.strip()
    return text
