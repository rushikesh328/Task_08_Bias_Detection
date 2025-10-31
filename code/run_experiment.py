import os
import csv
from datetime import datetime
import random

# === CONFIGURATION ===
MODELS = ["GPT-5", "Claude-3.5", "Gemini-1.5"]
PROMPT_FILE = "../prompts/prompt_templates.md"
OUTPUT_FILE = "../results/llm_outputs.csv"

# === READ PROMPTS ===
def extract_prompts(file_path):
    prompts = []
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        if line.strip().startswith(">"):
            prompts.append(line.strip().lstrip("> ").rstrip())
    return prompts

prompts = extract_prompts(PROMPT_FILE)
print(f"Loaded {len(prompts)} prompts.")

# === CREATE OUTPUT DIR ===
os.makedirs("../results", exist_ok=True)

# === SIMULATED FUNCTION TO GET LLM RESPONSE ===
# (Later, you’ll replace this with actual API calls)
def get_llm_response(model, prompt):
    # Placeholder: simulate response variability
    return f"Simulated {model} response for: {prompt[:60]}..."

# === COLLECT RESPONSES ===
with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Timestamp", "Model", "Prompt_ID", "Prompt_Text", "Response_Text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for model in MODELS:
        for i, prompt in enumerate(prompts, start=1):
            for sample in range(1, 4):  # 3 runs per prompt
                response = get_llm_response(model, prompt)
                writer.writerow({
                    "Timestamp": datetime.now().isoformat(),
                    "Model": model,
                    "Prompt_ID": f"P{i}",
                    "Prompt_Text": prompt,
                    "Response_Text": response
                })

print(f"Experiment completed — results saved to {OUTPUT_FILE}")
