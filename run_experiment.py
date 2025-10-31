import os
import csv
from datetime import datetime

# === CONFIGURATION ===
MODELS = ["GPT-5", "Claude-3.5", "Gemini-1.5"]
PROMPT_FILE = r"...\prompts\prompt_templates.md"
OUTPUT_FILE = r"...\results\llm_outputs.csv"


# === READ PROMPTS FROM FILE ===
def extract_prompts(file_path):
    """Extract lines that start with '>' from the markdown prompt file."""
    prompts = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith(">"):
                prompts.append(line.strip().lstrip("> ").rstrip())
    return prompts


# === SIMULATED LLM RESPONSE ===
def get_llm_response(model, prompt):
    return f"[SIMULATED RESPONSE from {model}] {prompt[:80]}..."


# === MAIN FUNCTION ===
def main():
    # Make sure results folder exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    # Read prompt templates
    prompts = extract_prompts(PROMPT_FILE)
    print(f"Loaded {len(prompts)} prompts from {PROMPT_FILE}\n")

    # Open CSV and record responses
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Timestamp", "Model", "Prompt_ID", "Prompt_Text", "Response_Text"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for model in MODELS:
            for i, prompt in enumerate(prompts, start=1):
                for sample in range(1, 4):  # 3 runs per prompt
                    writer.writerow({
                        "Timestamp": datetime.now().isoformat(),
                        "Model": model,
                        "Prompt_ID": f"P{i}",
                        "Prompt_Text": prompt,
                        "Response_Text": get_llm_response(model, prompt)
                    })

    print(f"Experiment completed — results saved to:\n{OUTPUT_FILE}")


# === ENTRY POINT ===
if __name__ == "__main__":
    main()

