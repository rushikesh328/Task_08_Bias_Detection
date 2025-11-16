import os
import csv

OUTPUT_DIR = "prompts"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "prompt_variations.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Base prompts P1–P9 grounded in the F1 sprint dataset summary
BASE_PROMPTS = [
    ("P1", "Which driver showed the most consistent performance across sprint events?"),
    ("P2", "Which team performed best overall in the sprint races?"),
    ("P3", "Which drivers gained the most positions on average?"),
    ("P4", "Which team was the most consistent across all sprint races?"),
    ("P5", "Did any driver finish on the podium after starting outside the top five?"),
    ("P6", "Which team performed best on specific tracks?"),
    ("P7", "Which driver had the strongest improvement relative to starting position?"),
    ("P8", "Which team struggled the most during sprint events?"),
    ("P9", "Based on the dataset summary, who is the most efficient driver in converting starting position into points?")
]

# For each base prompt, we used three runs:
#   - Original wording
#   - Same question answered again independently
#   - Same question answered a third time independently

VARIATION_SUFFIXES = [
    ("v1", ""),  # original prompt
    ("v2", " Please answer the same question again as an independent answer."),
    ("v3", " Please answer the same question once more as an independent answer.")
]

def main():
    rows = []

    for prompt_id, base_text in BASE_PROMPTS:
        for variant_id, extra_text in VARIATION_SUFFIXES:
            full_id = f"{prompt_id}_{variant_id}"
            full_prompt = base_text + extra_text
            rows.append({
                "Prompt_ID": prompt_id,
                "Variant": variant_id,
                "Full_ID": full_id,
                "Prompt_Text": full_prompt
            })

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["Prompt_ID", "Variant", "Full_ID", "Prompt_Text"]
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} prompt variants to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
