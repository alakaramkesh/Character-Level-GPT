import json

input_path = "data/raw/Hafez.json"
output_path = "data/processed/hafez_poems.txt"

with open(input_path, "r", encoding="utf-8") as f:
    data = json.load(f)

poems_dict = data[0]

with open(output_path, "w", encoding="utf-8") as out:
    poems = list(poems_dict.values())

    for poem_index, poem in enumerate(poems):
        lines = [line.strip() for line in poem["Poem"].split("\n") if line.strip()]

        for i in range(0, len(lines), 2):
            beyt = lines[i:i+2]
            out.write("\n".join(beyt) + "\n\n")

        if poem_index != len(poems) - 1:
            out.write("\n")