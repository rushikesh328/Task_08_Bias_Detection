import pandas as pd
from textblob import TextBlob
import os

INPUT_FILE = r"C:\Users\lenovo\Documents\MS documents\RA work\15oct-15nov\results\llm_outputs.csv"
OUTPUT_FILE = r"C:\Users\lenovo\Documents\MS documents\RA work\15oct-15nov\results\bias_summary.csv"

teams = ["Red Bull", "Ferrari", "Mercedes", "McLaren", "Haas", "Williams"]
drivers = ["Verstappen", "Perez", "Leclerc", "Russell", "Norris", "Hamilton"]

df = pd.read_csv(INPUT_FILE, encoding="latin1")
print("Loaded", len(df), "responses")

df["Sentiment"] = df["Response_Text"].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

def count_mentions(text, keywords):
    text = str(text).lower()
    return sum(1 for k in keywords if k.lower() in text)

df["Team_Mentions"] = df["Response_Text"].apply(lambda x: count_mentions(x, teams))
df["Driver_Mentions"] = df["Response_Text"].apply(lambda x: count_mentions(x, drivers))

def classify_focus(text):
    text = str(text).lower()
    driver_hits = count_mentions(text, drivers)
    team_hits = count_mentions(text, teams)
    if driver_hits > team_hits:
        return "Driver-Focused"
    elif team_hits > driver_hits:
        return "Team-Focused"
    else:
        return "Balanced"

df["Attribution"] = df["Response_Text"].apply(classify_focus)

summary = df.groupby("Model").agg({
    "Sentiment": "mean",
    "Team_Mentions": "mean",
    "Driver_Mentions": "mean"
}).round(3)

summary["Total_Responses"] = df.groupby("Model").size()

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
summary.to_csv(OUTPUT_FILE)
print("Bias summary saved to:", OUTPUT_FILE)

print("\nBias Summary:")
print(summary)
