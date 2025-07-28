# main.py
import os
from extract_text import extract_text_info
from heading_detector import assign_heading_levels
from json_writer import write_json

def process_pdf(file_path, out_dir):
    lines = extract_text_info(file_path)
    title, outline = assign_heading_levels(lines)

    file_name = os.path.splitext(os.path.basename(file_path))[0] + ".json"
    write_json(title, outline, os.path.join(out_dir, file_name))

import os

def main():
    # Use Docker paths if they exist, else fallback to local dev paths
    input_dir = "/app/input" if os.path.exists("/app/input") else r"C:\Users\Pranav\PycharmProjects\1a_Adobe_Hackathon\input"
    output_dir = r"C:\Users\Pranav\PycharmProjects\1a_Adobe_Hackathon\output"

    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            print(f"Processing: {filename}")
            pdf_path = os.path.join(input_dir, filename)
            from extract_text import extract_text_info
            from heading_detector import assign_heading_levels
            from json_writer import write_json

            lines = extract_text_info(pdf_path)
            title, outline = assign_heading_levels(lines)
            json_filename = filename.replace(".pdf", ".json")
            # print("Title:", title)
            # print("Outline:", outline)
            write_json(title, outline, os.path.join(output_dir, json_filename))


if __name__ == "__main__":
    main()
