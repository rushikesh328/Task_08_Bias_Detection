# Process Log – Research Task 08

## Overview
This log documents the full workflow used to complete Task 08 including tools, errors, fixes, and decisions made.

## Tools Used
- Python 3.11  
- pandas  
- textblob  
- VS Code  
- ChatGPT (GPT-5)  
- Claude-3.5  
- Gemini-1.5  
- Markdown for documentation  

## Steps Followed
1. Created folder structure with Code, results, prompts, and logs directories.  
2. Created prompt_templates.md containing nine experiment prompts.  
3. Gathered responses manually from three LLMs.  
4. Formatted collected outputs into llm_outputs.csv.  
5. Implemented and executed analyze_bias.py to compute sentiment and entity mention metrics.  
6. Resolved a UnicodeDecodeError by loading the CSV using latin1 encoding.  
7. Verified summary statistics and confirmed 81 responses were loaded.  
8. Executed visualize_bias.py to generate sentiment and mention plots.  
9. Reviewed data and produced bias_interpretation.md.  
10. Prepared REPORT.md as the final stakeholder-facing document.

## Errors Encountered
### UnicodeDecodeError when reading CSV
Cause: LLM outputs contained non UTF-8 characters.  
Fix: Loaded CSV using encoding="latin1".

### Missing modules
Cause: textblob not installed.  
Fix: Installed using pip install textblob.

## Lessons Learned
- Manual LLM output collection requires format consistency.  
- Encoding issues are common in mixed-source CSVs.  
- Framing effects and entity mentions differ significantly across models.  
- Logging is essential for reproducibility.

