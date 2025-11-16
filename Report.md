# Research Task 08: Bias, Framing, and Attribution Analysis Across LLMs

## Title and Purpose
This report analyzes how three large language models interpret the same dataset summary under identical conditions. The purpose is to evaluate whether subtle differences in prompt framing lead to measurable bias in sentiment, entity mentions, or attribution.

## Executive Summary
Three models were tested: GPT-5, Claude-3.5, and Gemini-1.5. Each model received an identical dataset summary of the 2024 Formula 1 Sprint Results and was asked nine analytic questions three times each. This produced eighty-one total responses. Quantitative analysis showed clear differences across models in sentiment, entity mentions, and preferred attribution patterns. GPT-5 responded with the most positive tone. Gemini-1.5 produced the most detailed outputs and referenced both teams and drivers more frequently. Claude-3.5 gave the most neutral and high-level responses. These differences demonstrate systematic framing, popularity, and attribution biases.

## Background
The underlying dataset used for context is the 2024 Formula 1 Sprint Results. A summary of descriptive statistics was prepared during Tasks 05 and 07. This summary was supplied to each LLM to ensure consistent grounding for comparison. The experimental goal was to test model consistency under repeated prompting and identify bias patterns driven by framing.

## Methods

### Experiment Setup
- Models tested: GPT-5, Claude-3.5, Gemini-1.5  
- Prompts: Nine structured questions, each repeated three times  
- Context: Identical dataset summary provided to each model  
- Total responses: 81  

### Data Collected
For each response:
- Sentiment polarity score  
- Team mention count  
- Driver mention count  
- Attribution classification (team-focused, driver-focused, balanced)

### Scripts Used
- run_experiment.py  
- analyze_bias.py  
- visualize_bias.py  

### Validation
- Manual inspection of model outputs  
- Sentiment computed with TextBlob  
- Mentions extracted through keyword matching  
- File-level analysis stored in results/bias_summary.csv  

## Findings

### Sentiment Bias
- GPT-5 produced the highest sentiment score (0.205).  
- Gemini-1.5 produced moderate sentiment (0.174).  
- Claude-3.5 produced the lowest sentiment (0.151).  
This indicates that GPT-5 tends toward optimistic framing.

### Team Mentions
- Gemini-1.5: 1.556 average team mentions  
- GPT-5: 1.185  
- Claude-3.5: 0.963  
Gemini provided the most detail, while Claude produced more general responses.

### Driver Mentions
- Gemini-1.5: 0.778 driver mentions  
- Claude-3.5: 0.519  
- GPT-5: 0.407  

### Attribution Patterns
- GPT-5 favored team-level explanations.  
- Gemini balanced both teams and drivers, with higher verbosity.  
- Claude provided limited references, remaining high-level.  

### Visualizations
Two plots were generated:
- sentiment_by_model.png  
- mentions_by_model.png  
These are located in the results folder.

## Ethical Considerations
- Bias in tone may influence user decisions.  
- Popularity bias may cause models to overemphasize high-profile teams.  
- Under-representation of smaller teams may create skewed recommendations.  
- Experiment limitations were documented to ensure transparency.

## Limitations
- Responses depend on model version and temperature settings.  
- Synthetic sentiment scoring may not capture nuanced tone.  
- Only three models were tested.  
- Only nine prompts were used; larger prompt sets may show additional bias.

## Recommendations
- Use multiple models when generating analytical summaries.  
- Evaluate outputs using quantitative measures rather than intuition.  
- Keep prompt framing consistent across comparisons.  
- Re-run analysis when model updates occur.

## Appendices
- bias_summary.csv  
- bias_interpretation.md  
- prompt_log.md  
- process_log.md  
- run_experiment.py, analyze_bias.py, visualize_bias.py  

