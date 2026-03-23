import json
import os

input_dir = "data/raw"
output_path = "data/processed/persian_poems.txt"
# Characters to remove from the corpus
chars_to_remove = "ًٌٍَُِّٔ!()*.:«»"
# Translation table for deleting unwanted characters
remove_table = str.maketrans("", "", chars_to_remove)
# List all JSON files in raw directory
json_files = [f for f in os.listdir(input_dir) if f.endswith(".json")]
all_poems = []
for file_name in json_files:
    file_path = os.path.join(input_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    poems_dict = data[0]
    for poem in poems_dict.values():
        text = poem.get("Poem", "").strip()
        if not text:
            continue
        lines = [line.strip() for line in text.split("\n") if line.strip()]
        cleaned_lines = [line.translate(remove_table) for line in lines] # Clean each line
        beyts = [] # Group into beyts (2 lines)
        for i in range(0, len(cleaned_lines), 2):
            beyt = cleaned_lines[i:i+2]
            beyts.append("\n".join(beyt))
        # Join beyts → full poem
        poem_text = "\n\n".join(beyts)
        all_poems.append(poem_text)
with open(output_path, "w", encoding="utf-8") as out:
    for i, poem in enumerate(all_poems):
        out.write(poem)
        # Separate poems with extra newline
        if i != len(all_poems) - 1:
            out.write("\n\n\n")

print(f"Corpus built: {output_path}")
print(f"Total poems: {len(all_poems)}")