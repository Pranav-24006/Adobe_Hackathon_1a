# extract_text.py
import fitz

def extract_text_info(pdf_path):
    doc = fitz.open(pdf_path)
    lines = []
    for page_number, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                line_text = " ".join([span["text"] for span in line["spans"]])
                font_size = line["spans"][0]["size"]
                font = line["spans"][0]["font"]
                lines.append({
                    "text": line_text.strip(),
                    "font_size": font_size,
                    "font": font,
                    "page": page_number
                })
    return lines
