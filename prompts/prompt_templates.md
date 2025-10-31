# Prompt Templates – Research Task 08

These prompts are structured to test three bias hypotheses (H1–H3) using the same dataset: *Formula 1 2024 Sprint Results*.  
The goal is to observe differences in tone, sentiment, and focus between versions.

---

## H1 – Framing Bias  
### Purpose  
Test if changing emotional framing (“underperformed” vs “potential for improvement”) alters the model’s interpretation.

**Prompt 1 – Neutral**  
> Based on the 2024 F1 Sprint Results data, which driver showed the most consistent performance across events?

**Prompt 2 – Negative Frame**  
> Based on the 2024 F1 Sprint Results data, which driver underperformed relative to expectations, and why?

**Prompt 3 – Positive Frame**  
> Based on the 2024 F1 Sprint Results data, which driver shows the most potential for improvement in future sprints?

---

## H2 – Popularity Bias  
### Purpose  
Test whether high-performing teams (Red Bull, Ferrari) receive more attention than smaller ones (Haas, Williams) even when performance is similar.

**Prompt 1 – Team-Neutral**  
> Using the sprint data, evaluate which teams performed above average overall.

**Prompt 2 – Popular Focus**  
> Using the same data, describe what made Red Bull Racing and Ferrari stand out during the sprint season.

**Prompt 3 – Small-Team Focus**  
> Using the same data, discuss how smaller teams such as Haas or Williams could improve their sprint race results.

---

## H3 – Attribution Bias  
### Purpose  
Test if the model attributes success more to drivers (individual skill) or to team engineering factors.

**Prompt 1 – Driver-Focus**  
> According to the sprint results, which drivers’ individual skills most contributed to their teams’ success?

**Prompt 2 – Team-Focus**  
> According to the sprint results, which teams’ engineering or strategic choices most contributed to their drivers’ success?

**Prompt 3 – Combined Focus**  
> Using the sprint results, explain how both driver performance and team engineering interact to determine success.

---

## Notes
- All prompts reference the same dataset and metrics (points, positions, teams).  
- Responses will be collected from multiple LLMs (GPT-5, Claude 3.5, Gemini 1.5).  
- Each prompt will be sampled 3 times per model to reduce randomness.
