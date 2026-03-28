from pathlib import Path
import json
import numpy as np

# paths
train_path = Path("data/processed/train.txt")
val_path = Path("data/processed/val.txt")
output_dir = Path("data/processed")
output_dir.mkdir(parents=True, exist_ok=True)

train_ids_path = output_dir / "train_ids.npy" # to save the encoded arrays of numpy
val_ids_path = output_dir / "val_ids.npy"
vocab_path = output_dir / "vocab.json"
# read files as a string
train_text = train_path.read_text(encoding="utf-8")
val_text = val_path.read_text(encoding="utf-8")
# build vocab from train only (chars in the string)
chars = sorted(list(set(train_text)))
vocab_size = len(chars)
UNK = "<unk>" # incase of special token
chars.append(UNK)
# mapping chars to ids and vice versa
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for i, ch in enumerate(chars)}

# encode data to ids that represent the chars 
def encode(text):
    return [stoi[ch] if ch in stoi else stoi[UNK] for ch in text]

train_ids = encode(train_text)
val_ids = encode(val_text)
# chars that are unknown in val
unknown_in_val = sorted(list(set(val_text) - set(train_text)))
print(f"Unknown chars in val mapped to <unk>: {unknown_in_val}")
# save vocab
vocab_data = {
    "vocab_size": vocab_size,
    "chars": chars,
    "stoi": stoi,
    "itos": {str(i): ch for i, ch in itos.items()}
}
with open(vocab_path, "w", encoding="utf-8") as f:
    json.dump(vocab_data, f, ensure_ascii=False, indent=2)
# save encoded arrays
np.save(train_ids_path, np.array(train_ids, dtype=np.int32))
np.save(val_ids_path, np.array(val_ids, dtype=np.int32))
print(f"Vocab saved to: {vocab_path}")
print(f"Train ids saved to: {train_ids_path}")
print(f"Val ids saved to: {val_ids_path}")
print(f"Vocab size: {vocab_size}")
print(f"Train length: {len(train_ids)}")
print(f"Val length: {len(val_ids)}")