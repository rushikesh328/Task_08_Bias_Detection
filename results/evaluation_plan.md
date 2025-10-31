# Evaluation Plan – Research Task 08

## Objective
Define how LLM responses to each prompt will be recorded, evaluated, and compared to identify framing, popularity, and attribution bias.

---

## Evaluation Metrics

### 1️⃣ Content Accuracy
- Compare factual claims (points, positions, team names) against verified Python summaries from Task 07.
- Score: 1 = accurate   0 = inaccurate   0.5 = partially correct.

### 2️⃣ Sentiment & Tone
- Use VADER or TextBlob to quantify polarity (−1 to +1).
- Compute average sentiment per prompt set (e.g., H1 Negative vs H1 Positive).

### 3️⃣ Attention Distribution
- Count frequency of driver / team mentions in each response.
- Normalize counts → proportion of total words → visualize via heatmap.

### 4️⃣ Attribution Bias (H3)
- Manually label each explanation as:
  - **Driver-focused**
  - **Team-focused**
  - **Balanced**
- Calculate distribution of focus types per model.

### 5️⃣ Diversity of Responses
- Measure lexical diversity (unique words ÷ total words).
- Low diversity across prompts = model repetition / template bias.

---

## Output Structure

All responses will be logged in `results/llm_outputs.csv` with columns:

| Model | Prompt_ID | Prompt_Text | Response_Text | Sentiment | Mentions | Accuracy | Attribution | Notes |
|:------|:-----------|:-------------|:---------------|:-----------|:-----------|:-----------|:-----------|:------|
| GPT-5 | H1_P1 | Neutral | “…Verstappen showed…” | 0.12 | {Red Bull: 2} | 1 | Driver | — |

---

## Data Collection Process
1. Each prompt variant = run 3 times per model (temperature 0.7).
2. Save raw responses + metadata in `results/raw/`.
3. Convert to CSV via `run_experiment.py`.
4. Run analysis scripts:
   - `analyze_bias.py` → sentiment + mention stats  
   - `validate_claims.py` → factual accuracy

---

## Visualization Plan
- **Bar Chart:** Average sentiment per prompt type  
- **Heatmap:** Driver / Team mention frequency  
- **Pie Chart:** Attribution (driver vs team)

---

## Validation & Ethics
- All prompts and outputs logged for audit.  
- Data anonymized (no real personal info).  
- Results interpreted cautiously to avoid over-generalization.
