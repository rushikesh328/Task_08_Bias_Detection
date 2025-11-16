import os
import pandas as pd

INPUT_FILE = r"C:\Users\lenovo\Documents\MS documents\RA work\15oct-15nov\results\llm_outputs.csv"
OUTPUT_DIR = "analysis"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "claims_validation_summary.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Ground truth facts from the F1 sprint summary:
GROUND_TRUTHS = {
    "top_driver": {
        "description": "Max Verstappen scored the highest sprint points.",
        "required_phrase": "max verstappen"
    },
    "top_team": {
        "description": "Red Bull was the top performing sprint team.",
        "required_phrase": "red bull"
    }
}

def contains_phrase(text, phrase):
    if not isinstance(text, str):
        return False
    return phrase.lower() in text.lower()

def main():
    # Use latin1 to avoid encoding issues from mixed-source CSV
    df = pd.read_csv(INPUT_FILE, encoding="latin1")

    # Flags for whether each response supports the ground truth
    df["Supports_Top_Driver"] = df["Response_Text"].apply(
        lambda x: contains_phrase(x, GROUND_TRUTHS["top_driver"]["required_phrase"])
    )
    df["Supports_Top_Team"] = df["Response_Text"].apply(
        lambda x: contains_phrase(x, GROUND_TRUTHS["top_team"]["required_phrase"])
    )

    # Aggregate by model
    summary = df.groupby("Model").agg(
        Total_Responses=("Response_Text", "count"),
        Supports_Top_Driver_Count=("Supports_Top_Driver", "sum"),
        Supports_Top_Team_Count=("Supports_Top_Team", "sum")
    )

    summary["Supports_Top_Driver_Rate"] = (
        summary["Supports_Top_Driver_Count"] / summary["Total_Responses"]
    ).round(3)

    summary["Supports_Top_Team_Rate"] = (
        summary["Supports_Top_Team_Count"] / summary["Total_Responses"]
    ).round(3)

    summary.to_csv(OUTPUT_FILE)
    print(f"Claims validation summary written to {OUTPUT_FILE}")
    print()
    print(summary)

if __name__ == "__main__":
    main()
