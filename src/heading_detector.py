import re
from collections import Counter, defaultdict

def assign_heading_levels(lines, min_font_count=3, min_font_size=8.0):
    # Step 1: Filter lines with valid text and font size
    valid_lines = [
        line for line in lines
        if line.get("text") and line.get("font_size", 0) >= min_font_size
    ]

    if not valid_lines:
        return None, []

    # Step 2: Count font sizes (rounded for grouping)
    font_counter = Counter(round(line['font_size'], 1) for line in valid_lines)
    common_fonts = [fs for fs, count in font_counter.items() if count >= min_font_count]
    sorted_fonts = sorted(common_fonts, reverse=True)

    # Step 3: Assign heading levels to top N frequent large font sizes
    heading_map = {}
    if len(sorted_fonts) >= 1: heading_map[sorted_fonts[0]] = "Title"
    if len(sorted_fonts) >= 2: heading_map[sorted_fonts[1]] = "H1"
    if len(sorted_fonts) >= 3: heading_map[sorted_fonts[2]] = "H2"
    if len(sorted_fonts) >= 4: heading_map[sorted_fonts[3]] = "H3"

    title = None
    outline = []
    seen_titles = set()
    previous_line = None

    # Step 4: Build outline
    for line in valid_lines:
        text = line["text"].strip()
        font = round(line["font_size"], 1)
        level = heading_map.get(font)
        page = int(line.get("page", 0))

        # Skip boilerplate
        if not text or len(text) < 3:
            continue
        if re.fullmatch(r"[\d.]+", text):  # skip digit-only like "1." or "2.3"
            continue

        # Try to merge multi-line headings
        if previous_line and round(previous_line['font_size'], 1) == font:
            prev_text = outline[-1]["text"]
            if abs(line["y"] - previous_line["y"]) < 20:  # close enough vertically
                outline[-1]["text"] = prev_text + " " + text
                previous_line = line
                continue

        # Save title or heading
        if level == "Title":
            if text not in seen_titles:
                title = title or text
                seen_titles.add(text)
        elif level in {"H1", "H2", "H3"}:
            outline.append({
                "level": level,
                "text": text,
                "page": page
            })
            previous_line = line

    return title, outline
