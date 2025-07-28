# json_writer.py
import json, os

def write_json(title, outline, out_path):
    print('Title: ',title)
    print('Output:', out_path)
    clean_outline = []
    for item in outline:
        clean_outline.append({
            "level": str(item["level"]),
            "text": str(item["text"]),
            "page": int(item["page"])  # Ensure int
        })

    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump({
            "title": str(title or "Untitled Document"),
            "outline": clean_outline
        }, f, indent=2)


