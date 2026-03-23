from pathlib import Path
import random

input_path = Path("data/processed/persian_poems.txt")
output_dir = Path("data/processed")
output_dir.mkdir(parents=True, exist_ok=True)

train_path = output_dir / "train.txt"
val_path = output_dir / "val.txt"

# settings
poem_separator = "\n\n\n"
train_ratio = 0.9
seed = 42
text = input_path.read_text(encoding="utf-8")
text = text.replace("\r\n", "\n").replace("\r", "\n") # normalize newlines
poems = text.split(poem_separator) # split poems
# remove empty poems and strip outer spaces
clean_poems = []
for poem in poems:
    poem = poem.strip()
    if poem:
        clean_poems.append(poem)

print(f"Total poems found: {len(clean_poems)}")

# shuffle
random.seed(seed)
random.shuffle(clean_poems)
# split
split_idx = int(len(clean_poems) * train_ratio)
train_poems = clean_poems[:split_idx]
val_poems = clean_poems[split_idx:]

print(f"Train poems: {len(train_poems)}")
print(f"Validation poems: {len(val_poems)}")
# join back into text
train_text = poem_separator.join(train_poems) + "\n"
val_text = poem_separator.join(val_poems) + "\n"
# save files
train_path.write_text(train_text, encoding="utf-8")
val_path.write_text(val_text, encoding="utf-8")
print(f"Train corpus saved to: {train_path}")
print(f"Validation corpus saved to: {val_path}")