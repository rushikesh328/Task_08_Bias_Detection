import os
import pandas as pd
import matplotlib.pyplot as plt

INPUT_FILE = r"C:\Users\lenovo\Documents\MS documents\RA work\15oct-15nov\results\bias_summary.csv"
OUTPUT_DIR = r"C:\Users\lenovo\Documents\MS documents\RA work\15oct-15nov\results"

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(INPUT_FILE, index_col=0)

# 1. Sentiment by model
plt.figure(figsize=(6, 4))
df["Sentiment"].plot(kind="bar")
plt.title("Average sentiment by model")
plt.ylabel("Sentiment (polarity)")
plt.xlabel("Model")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "sentiment_by_model.png"))
plt.close()

# 2. Mentions by model (team vs driver)
plt.figure(figsize=(6, 4))
df[["Team_Mentions", "Driver_Mentions"]].plot(kind="bar")
plt.title("Average mentions per response")
plt.ylabel("Average count")
plt.xlabel("Model")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "mentions_by_model.png"))
plt.close()
