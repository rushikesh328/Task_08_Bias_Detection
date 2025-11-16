# Research Task 08 Repository

## Overview
This repository contains all code, results, and documentation for Research Task 08. The goal is to test framing bias, attribution bias, and sentiment variation across multiple LLMs using a consistent dataset summary and structured prompts.

## Folder Structure
Task08/
  Code/
  results/
  prompts/
  logs/
  REPORT.md
  README.md

## How to Reproduce the Experiment

### 1. Prepare Environment
Install required libraries:
pip install pandas textblob
python -m textblob.download_corpora

### 2. Run Experiment
Collect responses manually from the LLMs and save them in results/llm_outputs.csv.

### 3. Run Bias Analysis
python analyze_bias.py

### 4. Generate Visualizations
python visualize_bias.py

Output files:
- bias_summary.csv  
- bias_interpretation.md  
- sentiment_by_model.png  
- mentions_by_model.png  

### 5. Review Reports
The complete analysis is in:
- REPORT.md  
- logs/process_log.md  
- logs/prompt_log.md  

## Notes
No raw datasets are included in this repository. All analysis uses a textual summary of the 2024 F1 Sprint Results dataset to ensure privacy and reproducibility.
