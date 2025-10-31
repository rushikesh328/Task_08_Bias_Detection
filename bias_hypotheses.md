# Bias Hypotheses – Research Task 08

## Overview
This experiment investigates how subtle changes in **prompt framing** influence the LLM’s interpretation of Formula 1 sprint race data.  
The dataset remains constant (F1 2024 Sprint Results), but the *tone* and *focus* of prompts are varied to test whether the model displays systematic bias in its analysis.

---

## Hypotheses

**H1 – Framing Bias:**  
When asked “Who underperformed?” vs. “Who showed potential for improvement?”, the LLM’s sentiment and choice of drivers will differ significantly, even though the same dataset is used.

**H2 – Popularity Bias:**  
When given data from all teams, the LLM will more frequently mention or praise top teams (e.g., Red Bull, Ferrari) compared to smaller teams (e.g., Haas, Williams).

**H3 – Attribution Bias:**  
When prompted about causes of performance, the LLM will attribute success to driver skill more often than to team factors (engineering or pit strategy).

**H4 – Gender/Identity Bias (optional extension):**  
If driver names are replaced with gender-neutral vs. gendered placeholders (e.g., “Alex” vs. “Sophie”), the tone and adjective usage will differ.

---

## Expected Outcomes
- Detect measurable changes in **sentiment**, **word choice**, or **attention distribution** (mentions per driver/team).  
- Observe whether bias patterns are **model-specific** (e.g., GPT-5 vs. Claude 3.5).  
- Document both *quantitative* (scores, frequencies) and *qualitative* (tone, framing) shifts.

---

## Validation Plan
Each hypothesis will be tested using:
1. **Prompt pairs** differing only by one phrase or framing variable.  
2. **Three model responses per prompt** to control for randomness.  
3. **Manual + automated validation** comparing responses to statistical ground truth.

