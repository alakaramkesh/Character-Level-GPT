import json
from pathlib import Path

input_path = Path("data/processed/persian_poems.txt")
output_path = Path("data/stats/corpus_stats.json")
output_path.parent.mkdir(parents=True, exist_ok=True)

# Read the entire corpus as a single string
with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()

lines = text.splitlines()
# Keep only non-empty lines
non_empty_lines = [line for line in lines if line.strip()]
# Get the set of unique characters in the corpus
unique_chars = sorted(set(text))

stats = {
    "total_characters": len(text), # Total number of characters
    "unique_characters": len(unique_chars), # Number of unique characters
    "unique_char_list": unique_chars, # List of all unique characters
    "total_lines": len(lines), # Total number of lines (including empty lines)
    "non_empty_lines": len(non_empty_lines), # Number of non-empty lines
    "total_poems": text.count("\n\n\n") + 1 if text.strip() else 0, # Estimate the number of poems based on triple newline separation
}
# Save
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(stats, f, ensure_ascii=False, indent=2)

# Print results 
print(f"Corpus stats saved to: {output_path}")
print(json.dumps(stats, ensure_ascii=False, indent=2))